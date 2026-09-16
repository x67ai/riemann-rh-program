# Sanity computation (pricing, <=10 min): on the function-field rung, is the "kernel measure"
# of a curve -- the coefficient sequence b_k = a_k q^{-k/2} of P(z/sqrt q), i.e. the Fourier
# coefficients of Xi_C(u) = prod_j (2cos u - 2cos theta_j) -- a NONNEGATIVE sequence (up to the
# global flip z -> -z, which negates odd-index b_k)?  Newman's class L consists of nonnegative
# measures, so a signed b would mean the Lee-Yang/class-L interface has no direct analogue on
# the rung where RH is a theorem.  Brute force: hyperelliptic y^2 = f(x), deg f in {5,6}, over F_p.
# Point counts N_1 (over F_p) and N_2 (over F_{p^2}) determine a_1, a_2 of the genus-2 Weil
# polynomial P(T) = 1 + a_1 T + a_2 T^2 + p a_1 T^3 + p^2 T^4:
#   a_1 = N_1 - p - 1 ;  N_2 = p^2 + 1 - s_2, s_2 = a_1^2 - 2 a_2  =>  a_2 = (N_2 - p^2 - 1 + a_1^2)/2.
# We count projective points on the smooth model: affine points + points at infinity
# (deg f = 5: one point at infinity; deg f = 6: 0, 1 or 2 depending on the leading coefficient).
import itertools, math, sys, time
t0 = time.time()

def legendre_table(p):
    sq = {}
    for x in range(p):
        sq.setdefault((x*x) % p, []).append(x)
    return sq

def count_affine(f, p, ext):
    # count solutions y^2 = f(x) over F_{p^ext}, ext in {1,2}; for ext=2 build F_{p^2} = F_p[t]/(t^2 - n), n a non-residue
    if ext == 1:
        sq = legendre_table(p)
        n = 0
        for x in range(p):
            v = sum(c * pow(x, i, p) for i, c in enumerate(f)) % p
            n += len(sq.get(v, []))
        return n
    # F_{p^2}
    nonres = next(a for a in range(2, p) if pow(a, (p-1)//2, p) == p-1)
    def mul(a, b):
        return ((a[0]*b[0] + nonres*a[1]*b[1]) % p, (a[0]*b[1] + a[1]*b[0]) % p)
    def add(a, b):
        return ((a[0]+b[0]) % p, (a[1]+b[1]) % p)
    elems = [(a, b) for a in range(p) for b in range(p)]
    sqtab = {}
    for e in elems:
        sqtab.setdefault(mul(e, e), []).append(e)
    n = 0
    for x in elems:
        v = (0, 0); xp = (1, 0)
        for c in f:
            v = add(v, mul((c % p, 0), xp)); xp = mul(xp, x)
        n += len(sqtab.get(v, []))
    return n

def points_at_infinity(f, p, ext):
    d = len(f) - 1
    if d == 5:
        return 1
    lead = f[-1] % p
    # y^2 = lead * x^6 near infinity: two points if lead is a square in F_{p^ext}, else 0
    if ext == 1:
        return 2 if pow(lead, (p-1)//2, p) == 1 else 0
    return 2  # every element of F_p is a square in F_{p^2}

def is_squarefree(f, p):
    # crude: check gcd(f, f') = 1 over F_p via resultant-free method: test no repeated root in F_{p^2} is overkill;
    # use polynomial gcd over F_p
    def trim(a):
        while a and a[-1] % p == 0: a = a[:-1]
        return a
    def polymod(a, b):
        a = trim([x % p for x in a]); b = trim([x % p for x in b])
        while len(a) >= len(b) and a:
            coef = (a[-1] * pow(b[-1], p-2, p)) % p
            shift = len(a) - len(b)
            a = trim([(a[i] - coef * (b[i-shift] if i >= shift else 0)) % p for i in range(len(a))])
        return a
    def gcd(a, b):
        a = trim(a); b = trim(b)
        while b:
            a, b = b, polymod(a, b)
        return a
    fp = [(i*c) % p for i, c in enumerate(f)][1:]
    g = gcd(f, fp)
    return len(trim(g)) == 1

found = []
for p in [3, 5, 7]:
    for d in [5, 6]:
        seen = set()
        for coeffs in itertools.product(range(p), repeat=d):
            f = list(coeffs) + [1]  # monic
            if not is_squarefree(f, p):
                continue
            N1 = count_affine(f, p, 1) + points_at_infinity(f, p, 1)
            N2 = count_affine(f, p, 2) + points_at_infinity(f, p, 2)
            a1 = N1 - p - 1
            a2 = (N2 - p*p - 1 + a1*a1)
            assert a2 % 2 == 0
            a2 //= 2
            key = (p, a1, a2)
            if key in seen: continue
            seen.add(key)
            b = [1.0, a1/math.sqrt(p), a2/p, a1/math.sqrt(p), 1.0]   # b_k = a_k p^{-k/2}, self-reciprocal
            # RH (Weil) check: roots of P(T) all of modulus p^{-1/2}
            import numpy as np
            roots = np.roots([p*p, p*a1, a2, a1, 1])
            rh_ok = all(abs(abs(r) - 1/math.sqrt(p)) < 1e-6 for r in roots)  # double roots cost ~sqrt(eps) in np.roots
            nonneg_plain = all(x >= 0 for x in b)
            nonneg_flip = all(x >= 0 for x in [b[0], -b[1], b[2], -b[3], b[4]])
            signed = not (nonneg_plain or nonneg_flip)
            found.append((p, d, a1, a2, N1, N2, rh_ok, nonneg_plain, nonneg_flip, signed, f))
            if time.time() - t0 > 540: break
        if time.time() - t0 > 540: break
print("p  deg  a1  a2  N1  N2  Weil-RH  b>=0  b>=0(flip)  SIGNED  example f (low->high, monic)")
for row in found:
    print(*row)
print("--- summary ---")
print("distinct (p,a1,a2) found:", len(found))
print("all satisfy Weil RH:", all(r[6] for r in found))
sig = [r for r in found if r[9]]
print("SIGNED kernel (no flip makes b>=0):", len(sig))
for r in sig[:10]:
    print("  p=%d deg=%d a1=%d a2=%d N1=%d N2=%d f=%s" % (r[0], r[1], r[2], r[3], r[4], r[5], r[10]))
zero_b1 = [r for r in found if r[2] == 0]
print("a1 = 0 (b_1 = 0: no +-1-spin partition function has a vanishing z^1 coefficient):", len(zero_b1))
for r in zero_b1[:6]:
    print("  p=%d deg=%d a2=%d N1=%d N2=%d f=%s" % (r[0], r[1], r[3], r[4], r[5], r[10]))

# --- Regularization check (Polya): multiply the signed example's P~(z) by (1+z)^m = m decoupled +-1 spins
import numpy as np
ex = next(r for r in found if r[9] and r[6])
p, a1, a2 = ex[0], ex[2], ex[3]
Pt = np.array([1.0, a1/math.sqrt(p), a2/p, a1/math.sqrt(p), 1.0])  # coefficients of P~(z) = P(z/sqrt p), low->high
print("regularization example: p=%d a1=%d a2=%d, P~ coefficients b =" % (p, a1, a2), Pt.round(4))
m_ok = None
for m in range(0, 60):
    q = Pt.copy()
    for _ in range(m):
        q = np.convolve(q, [1.0, 1.0])
    if (q > 0).all():
        m_ok = m; break
print("smallest m with all coefficients of P~(z)(1+z)^m positive:", m_ok)
if m_ok is not None:
    q = Pt.copy()
    for _ in range(m_ok): q = np.convolve(q, [1.0, 1.0])
    # the regularized polynomial's roots are those of P~ (on the circle, checked above via Weil-RH)
    # together with z = -1 with multiplicity m; np.roots is unstable at a multiple root, so check by
    # polynomial division instead: q / (1+z)^m must return P~ exactly.
    r = q.copy()
    for _ in range(m_ok):
        r, rem = np.polydiv(r[::-1], [1.0, 1.0]); r = r[::-1]
        assert np.all(np.abs(rem) < 1e-9)
    print("  q(z)/(1+z)^m == P~(z) exactly (max abs diff):", float(np.max(np.abs(r - Pt))))
    print("  hence roots of q = roots of P~ (unit circle) + {-1} x m: on the unit circle: True")
# --- g = 1 check: two +-1 spins, H = -J s1 s2, fugacity z per up spin:
#     Z(z) = e^{J}(1 + z^2) + 2 e^{-J} z ;  roots on |z|=1 iff J >= 0 ;  matching P~(z) = 1 + (a1/sqrt p) z + z^2
#     needs 2 e^{-2J} = |a1|/sqrt(p) (after the flip z -> -z when a1 > 0), i.e. J = -(1/2) log(|a1|/(2 sqrt p)),
#     and J >= 0  <=>  |a1| <= 2 sqrt p  <=>  Hasse bound  <=>  RH for the elliptic curve.  Numeric confirmation:
for p_, a1_ in [(5, -2), (5, 4), (7, -5), (11, 6), (13, 8)]:
    r = abs(a1_)/(2*math.sqrt(p_))
    J = -0.5*math.log(r) if r > 0 else float('inf')
    Z = np.array([math.exp(J), 2*math.exp(-J), math.exp(J)])  # low->high in z
    rts = np.roots(Z[::-1])
    print("g=1: p=%d a1=%d  |a1|/(2 sqrt p)=%.4f  J=%.4f  J>=0:%s  roots on circle:%s  Hasse:%s" % (
        p_, a1_, r, J, J >= 0, bool(np.all(np.abs(np.abs(rts)-1) < 1e-9)), abs(a1_) <= 2*math.sqrt(p_)))
print("elapsed s:", round(time.time() - t0, 1))
