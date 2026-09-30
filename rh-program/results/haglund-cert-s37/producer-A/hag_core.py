# hag_core.py -- producer A, unit haglund-cert-s37 (Session 37).  Arb ball arithmetic via python-flint 0.6.0.
# Objects exactly as in Haglund, arXiv:0910.5228, pp. 1-3 (text on disk: novel-wave-s36/staircase/lit/):
#   Xi(z)      = 1/2 (1/2+iz)(-1/2+iz) pi^{-(1/2+iz)/2} Gamma((1/2+iz)/2) zeta(1/2+iz)            (1)
#   G(w;a,b)   = Gamma(b+iw,a)/a^{b+iw} + Gamma(b-iw,a)/a^{b-iw}                                   (10)
#   Phi_n(z)   = 2 pi^2 n^4 G(z/2; n^2 pi, 9/4) - 3 pi n^2 G(z/2; n^2 pi, 5/4)                     (14)
#   Xi_N       = sum_{n<=N} Phi_n  (13);   Xi = sum_{n>=1} Phi_n  (12)
# Every function returns an Arb enclosure (acb box) valid for EVERY z in the input box.
from flint import acb, arb, ctx

I = acb(0, 1)

def G(w, a, b):
    """Haglund (10).  w: acb (point or box); a: arb > 0; b: arb.  a^{-s} = exp(-s log a) (a > 0 real).
    python-flint convention (checked in the ladder log): acb(x).gamma_upper(s) = Gamma(s, x)."""
    A = acb(a)
    la = acb(a.log())
    s1 = acb(b) + I * w
    s2 = acb(b) - I * w
    return A.gamma_upper(s1) * (-s1 * la).exp() + A.gamma_upper(s2) * (-s2 * la).exp()

def Phi(n, z):
    """Haglund (14): Phi_n(z) = 2 pi^2 n^4 G(z/2; n^2 pi, 9/4) - 3 pi n^2 G(z/2; n^2 pi, 5/4)."""
    pi = arb.pi()
    a = pi * n * n
    w = z / 2
    return 2 * pi * pi * n**4 * G(w, a, arb(9) / 4) - 3 * pi * n * n * G(w, a, arb(5) / 4)

def XiN_L(N, z):
    """Route (L): the literal finite sum (13).  Rigorous for any input, but only SHARP for point inputs at high precision."""
    tot = acb(0)
    for n in range(1, N + 1):
        tot += Phi(n, z)
    return tot

def Xi(z):
    """Riemann's Xi via (1) with s = 1/2 + iz, from Arb's zeta and gamma (acb_zeta, acb_gamma)."""
    s = acb(arb(1) / 2) + I * z
    pi = arb.pi()
    return s * (s - 1) / 2 * (-(s / 2) * acb(pi.log())).exp() * (s / 2).gamma() * s.zeta()

def tail_bound(z, M):
    """Upper bound E with |sum_{n>M} Phi_n(z)| <= E for every z in the box (proof: CERT.md, Lemma T).
    U_n = 2 e^{-a}(2 pi^2 n^4 + 3 pi n^2)/(a - beta9 + 1), a = pi n^2, beta9 = 9/4 + |Im z|/2;  sum_{n>M} U_n <= 2 U_{M+1}."""
    y = z.imag.abs_upper()                      # rigorous upper bound for |Im z| on the box
    beta9 = arb(9) / 4 + y / 2
    n = M + 1
    pi = arb.pi()
    a = pi * n * n
    den = a - beta9 + 1
    assert den > 1, "tail bound needs a - beta9 + 1 > 1"   # also gives a > beta9 - 1 (Lemma T hypothesis)
    U = 2 * (-a).exp() * (2 * pi * pi * n**4 + 3 * pi * n * n) / den
    return (2 * U).upper()                       # an arb upper bound (exact point)

def XiN_T(N, z, M=None):
    """Route (T): Xi_N = Xi - sum_{n=N+1}^{M} Phi_n - (tail n > M), the tail added as a proved error ball."""
    if M is None:
        M = N + 4
    v = Xi(z)
    for n in range(N + 1, M + 1):
        v -= Phi(n, z)
    E = tail_bound(z, M)
    return v + acb(arb(0, E), arb(0, E))

# ---------------------------------------------------------------------------------------------------------------
# Rigorous winding number (argument principle) along the boundary of the axis-parallel square S = c + [-r, r]^2.
# Exact boundary points P_k (exact decimals/rationals) are carried as tiny Arb boxes B_k (B_k contains P_k).
# Piece k = exact segment [P_k, P_{k+1}], covered by the box union(B_k, B_{k+1}) (a box is convex).
# (i)  E_k = f(piece box) must satisfy one of Re>0, Re<0, Im>0, Im<0 for EVERY element: then f(segment) lies in an
#      open half-plane H through 0, the continuous arg of f along the segment varies inside an interval of length < pi,
#      and its increment equals the principal Arg(f(P_{k+1})/f(P_k)).
# (ii) D_k = Arg(F_{k+1}/F_k) with F_k = f(B_k) (point enclosures); |D_k| < pi is checked.
# (iii) winding = sum_k D_k / (2 pi): an Arb ball that must lie within 1/2 of a single integer.
# If (i) fails for a piece it is bisected (at the exact midpoint), up to maxdepth levels.

def _excl0(E):
    if E.real > 0: return "Re>0"
    if E.real < 0: return "Re<0"
    if E.imag > 0: return "Im>0"
    if E.imag < 0: return "Im<0"
    return None

def square_vertices(cx, cy, r):
    """Counterclockwise corners of c + [-r, r]^2 from exact decimal strings (Arb boxes containing the exact corners)."""
    X, Y, R = arb(cx), arb(cy), arb(r)
    return [acb(X - R, Y - R), acb(X + R, Y - R), acb(X + R, Y + R), acb(X - R, Y + R)]

def winding(f, verts, K0, maxdepth=12, out=print, tag=""):
    import time
    t0 = time.time()
    # initial exact points: K0 equal pieces per side
    segs = []
    for i in range(4):
        A, B = verts[i], verts[(i + 1) % 4]
        pts = [A + (B - A) * j / K0 for j in range(K0 + 1)]
        for j in range(K0):
            segs.append((pts[j], pts[j + 1], 0))
    accepted = []          # list of (P, Q, E, halfplane)
    stack = list(reversed(segs))
    nsplit = 0
    while stack:
        P, Q, d = stack.pop()
        box = acb(P.real.union(Q.real), P.imag.union(Q.imag))
        E = f(box)
        hp = _excl0(E)
        if hp is None:
            if d >= maxdepth:
                out("%s FAIL: piece cannot exclude 0 at depth %d: box %s  encl %s" % (tag, d, box.str(20), E.str(5)))
                return None
            M = (P + Q) / 2
            nsplit += 1
            stack.append((M, Q, d + 1))
            stack.append((P, M, d + 1))
            continue
        accepted.append((P, Q, E, hp, d))
    out("%s pieces accepted: %d (initial %d, bisections %d)" % (tag, len(accepted), 4 * K0, nsplit))
    # endpoint values and increments
    total = arb(0)
    Fprev = f(accepted[0][0])
    F0 = Fprev
    for k, (P, Q, E, hp, d) in enumerate(accepted):
        Fq = F0 if k == len(accepted) - 1 else f(Q)
        D = (Fq / Fprev).arg()
        if not (D.abs_upper() < arb.pi()):
            out("%s FAIL: increment not within (-pi, pi) at piece %d: %s" % (tag, k, D.str(10)))
            return None
        total += D
        out("%s piece %4d d=%d %s | z in [%s, %s] | f(piece) in %s + %s i | f(end) = %s + %s i | dArg = %s" % (
            tag, k, d, hp, P.real.str(20, more=True) + " " + P.imag.str(20, more=True), Q.real.str(20, more=True) + " " + Q.imag.str(20, more=True),
            E.real.str(6, more=True), E.imag.str(6, more=True), Fq.real.str(8, more=True), Fq.imag.str(8, more=True), D.str(8, more=True)))
        Fprev = Fq
    W = total / (2 * arb.pi())
    out("%s total Arg increment = %s ; winding = %s ; (%.1fs)" % (tag, total.str(15), W.str(15), time.time() - t0))
    k = int(round(float(W.mid())))
    ok = (W - k).abs_upper() < arb(1) / 2
    out("%s winding number certified = %s" % (tag, k if ok else "UNDETERMINED"))
    return k if ok else None
