"""
rigor_xi1.py -- computer-assisted proof (interval arithmetic, mpmath.iv, outward rounding) about the first
C1 member  xi_1(s) = 1/2 + (1/2) s (s-1) g_1(s).

REPRESENTATION USED FOR ENCLOSURES (no catastrophic cancellation):
    xi_1(s) = xi(s) - R_1(s),   R_1(s) = (1/2) s (s-1) sum_{n>=2} g_n(s),
    xi(s)   = (1/2) s (s-1) pi^{-s/2} Gamma(s/2) zeta(s),
    g_n(s)  = h_n(s/2) + h_n((1-s)/2),  h_n(a) = X^{-a} Gamma(a, X), X = pi n^2.
  * zeta(s): Euler-Maclaurin to order K with N terms; remainder bounded by |s+2K+1|/(sigma+2K+1) times the
    first omitted term  [Edwards, Riemann's Zeta Function, sec. 6.4 -- recalled, standard];
  * Gamma(a): Gamma(a+m)/(a)_m, m = 25, Stirling to order M = 12 with remainder
    |R_M(z)| <= |B_{2M}| / (2M(2M-1)|z|^{2M-1}) sec^{2M}(arg z / 2)  for Re z > 0  [DLMF 5.11.ii -- recalled, standard];
  * h_n(a), n = 2, 3, 4: X^{-a}Gamma(a) - e^{-X} sum_{k<K} X^k/(a)_{k+1} - (tail), tail bounded by the first
    omitted term / (1 - X/(Re a + K + 1));
  * n >= 5: |h_n(a)| <= e^{-X}/(X - max(Re a - 1, 0))  (elementary: u^{b-1} <= X^{b-1} e^{(b-1)(u-X)/X}).

CLAIMS:
  (R1) xi_1(1/2+it) > 0 for all t >= 30  [separate asymptotic argument on u = 1/t in [0, 1/30]];
  (R2) on [0, 30] the enclosure of xi_1(1/2+it) excludes 0 except on two short intervals;
  (R3) exactly one zero of xi_1 in a small square around each of them (rigorous winding number), hence (by
       xi_1(1 - conj s) = conj xi_1(s)) on the line;  => exactly two zeros on the line with t > 0;
  (R4) exactly one zero of xi_1 in a square of half-width 1e-8 around 5.1659020269245690919 + 22.915465770560823314 i.
Usage: python rigor_xi1.py [R1] [R2] [R4]
"""
import sys, time, json
import mpmath as mp

iv = mp.iv
iv.dps = 60
PI = iv.pi
LOGPI = iv.log(PI)
MST = 12
BERN = [iv.mpf(mp.bernoulli(2*k)) for k in range(1, 40)]
FACT = [iv.mpf(mp.factorial(j)) for j in range(0, 90)]


def cabs_lower(z):
    re, im = z.real, z.imag
    rl = 0 if (re.a <= 0 <= re.b) else min(abs(re.a), abs(re.b))
    il = 0 if (im.a <= 0 <= im.b) else min(abs(im.a), abs(im.b))
    return iv.sqrt(iv.mpf(rl)**2 + iv.mpf(il)**2).a


def cabs_upper(z):
    ru = max(abs(z.real.a), abs(z.real.b))
    iu = max(abs(z.imag.a), abs(z.imag.b))
    return iv.sqrt(iv.mpf(ru)**2 + iv.mpf(iu)**2).b


def up(x):
    """an mp.mpf upper bound for a real interval / number x (outward: inflated by 1e-45 relative)."""
    try:
        v = mp.mpf(x.b)
    except AttributeError:
        v = mp.mpf(x)
    return v + abs(v)*mp.mpf(10)**(-45)


def disc(r):
    R = up(r)
    rr = iv.mpf([-R, R])
    return iv.mpc(rr, rr)


def cexp(z):
    return iv.exp(z.real) * iv.mpc(iv.cos(z.imag), iv.sin(z.imag))


def loggamma_stirling(z):
    assert z.real.a >= 20
    lz = iv.log(z)
    s = (z - iv.mpf(1)/2)*lz - z + iv.log(2*PI)/2
    zinv = 1/z
    zinv2 = zinv*zinv
    zp = zinv
    for k in range(1, MST):
        s += BERN[k - 1] / (2*k*(2*k - 1)) * zp
        zp = zp*zinv2
    absz = cabs_lower(z)
    ang = iv.atan2(iv.mpf(max(abs(z.imag.a), abs(z.imag.b))), iv.mpf(z.real.a)).b
    sec2 = (1/iv.cos(iv.mpf(ang)/2))**2
    R = abs(BERN[MST - 1]) / (2*MST*(2*MST - 1)) / iv.mpf(absz)**(2*MST - 1) * sec2**MST
    return s + disc(R.b)


def clog(z):
    """complex-interval logarithm (principal branch; the box must not meet the negative real axis or 0)."""
    return iv.log(z)


def gamma_iv(a, m=25):
    """Gamma(a) = exp(logGamma(a+m) - sum_{j<m} log(a+j)): log form, no complex products (no wrapping)."""
    L = loggamma_stirling(a + m)
    for j in range(m):
        L = L - clog(a + j)
    return cexp(L)


def zeta_iv(s, N=40, K=24):
    """Euler-Maclaurin in log form; valid for sigma + 2K + 1 > 0, s != 1.  T_k = B_2k/(2k)! prod_{j=0}^{2k-2}(s+j) N^{1-s-2k};
    remainder <= |s+2K+1|/(sigma+2K+1) |T_{K+1}|  [Edwards sec. 6.4, recalled, standard]."""
    S = iv.mpc(0, 0)
    for n in range(1, N):
        S += cexp(-s*iv.log(iv.mpf(n)))
    lN = iv.log(iv.mpf(N))
    S += cexp((1 - s)*lN)/(s - 1) + cexp(-s*lN)/2
    Lp = clog(s)                 # log prod_{j=0}^{2k-2}(s+j), k = 1
    for k in range(1, K + 2):
        B = BERN[k - 1]
        sgn = 1 if B > 0 else -1
        logT = Lp + (1 - s - 2*k)*lN + iv.log(abs(B)/FACT[2*k])
        Tk = cexp(logT)*sgn
        if k == K + 1:
            sig = s.real.a
            fac = cabs_upper(s + 2*K + 1) / (sig + 2*K + 1)
            S += disc(iv.mpf(fac) * iv.mpf(cabs_upper(Tk)))
            break
        S += Tk
        Lp = Lp + clog(s + 2*k - 1) + clog(s + 2*k)
    return S


def h_iv(a, X, K):
    """X^{-a} Gamma(a, X) = X^{-a} Gamma(a) - e^{-X} sum_{k<K} X^k/(a)_{k+1} - tail.  Each term in log form:
    X^k/(a)_{k+1} = exp(k log X - sum_{j<=k} log(a+j)); tail bounded with per-factor lower bounds
    |a+j| >= max(Re a + j, |Im a|) (no wrapping)."""
    lX = iv.log(X)
    s = iv.mpc(0, 0)
    L = iv.mpc(0, 0)
    for k in range(K):
        L = L + clog(a + k)
        s += cexp(k*lX - L)
    # tail: sum_{k>=K} X^k / |(a)_{k+1}|  <= X^K / prod_{j<=K} lb_j * 1/(1 - X/lb_{K+1})
    ra = mp.mpf(a.real.a)
    ia = min(abs(mp.mpf(a.imag.a)), abs(mp.mpf(a.imag.b))) if not (a.imag.a <= 0 <= a.imag.b) else mp.mpf(0)
    logden = mp.mpf(0)
    for j in range(K + 1):
        lb = max(ra + j, ia)
        assert lb > 0
        logden += mp.log(lb)
    lb_next = max(ra + K + 1, ia)
    q = mp.mpf(X.b) / lb_next
    assert q < 1, (q, K)
    tail = mp.exp(K*mp.log(mp.mpf(X.b)) - logden) / (1 - q) * (1 + mp.mpf(10)**(-30))
    lower = iv.exp(-X) * (s + disc(tail))
    return cexp(-a*lX) * gamma_iv(a) - lower


def h_bound(a, X):
    b = max(mp.mpf(a.real.b) - 1, 0)
    return up(iv.exp(-X) / (X - b))


def xi_iv(s):
    return s*(s - 1)/2 * cexp(-s/2*LOGPI) * gamma_iv(s/2) * zeta_iv(s)


def R1_iv(s):
    acc = iv.mpc(0, 0)
    for n in (2, 3, 4):
        X = PI*n*n
        K = int(3*mp.mpf(X.b)) + 60
        acc += h_iv(s/2, X, K) + h_iv((1 - s)/2, X, K)
    # n >= 5
    bnd = mp.mpf(0)
    for n in range(5, 40):
        X = PI*n*n
        bnd += h_bound(s/2, X) + h_bound((1 - s)/2, X)
    bnd *= mp.mpf(2)   # generous: covers n >= 40 (e^{-pi 1600} scale) many times over
    acc += disc(bnd)
    return s*(s - 1)/2 * acc


def xi1_iv(s):
    return xi_iv(s) - R1_iv(s)


def contains0(z):
    return (z.real.a <= 0 <= z.real.b) and (z.imag.a <= 0 <= z.imag.b)


def box(za, zb):
    return iv.mpc(iv.mpf([min(za.real, zb.real), max(za.real, zb.real)]),
                  iv.mpf([min(za.imag, zb.imag), max(za.imag, zb.imag)]))


def rigorous_winding(f, corners, nseg, maxsplit=12):
    """winding number of f along the closed polygon `corners`; each edge is cut into pieces whose interval
    enclosure (over the whole piece) excludes 0 (pieces are bisected adaptively up to `maxsplit` times).
    An enclosure excluding 0 is a rectangle in an open half-plane through 0, so the arg change over the piece
    is the principal arg of f(end)/f(start)."""
    total = mp.mpf(0)
    npieces = 0
    nb = len(corners)
    for e in range(nb):
        z0, z1 = corners[e], corners[(e + 1) % nb]
        stack = [(z0 + (z1 - z0)*mp.mpf(j + 1)/nseg, z0 + (z1 - z0)*mp.mpf(j)/nseg, 0) for j in range(nseg)]
        # process in order: pop from the end -> start with j = 0
        stack = stack[::-1]
        pieces = []
        work = [(z0 + (z1 - z0)*mp.mpf(j)/nseg, z0 + (z1 - z0)*mp.mpf(j + 1)/nseg, 0) for j in range(nseg)][::-1]
        while work:
            za, zb, d = work.pop()
            fb = f(box(za, zb))
            if contains0(fb):
                if d >= maxsplit:
                    return None, (za, zb), npieces
                zm = (za + zb)/2
                work.append((zm, zb, d + 1))
                work.append((za, zm, d + 1))
                continue
            fa = f(iv.mpc(za.real, za.imag))
            fbb = f(iv.mpc(zb.real, zb.imag))
            ca = mp.mpc(fa.real.mid, fa.imag.mid)
            cb = mp.mpc(fbb.real.mid, fbb.imag.mid)
            total += mp.arg(cb/ca)
            npieces += 1
    return total/(2*mp.pi), None, npieces


def run_R1(rep):
    T0 = 30
    Kr = 14
    E_PI = iv.exp(-PI)

    def rational_part(u):
        acc = iv.mpf(1)   # k = 0 term: (1/4+t^2) Re(1/a) = 1 identically (a = 1/4 + i t/2)
        for k in range(1, Kr):
            num = (u*u/4 + 1) * PI**k * u**(k - 1)
            den = iv.mpc(1, 0)
            for j in range(k + 1):
                den = den * iv.mpc(u*(iv.mpf(1)/4 + j), iv.mpf(1)/2)
            acc += (num/den).real
        return acc

    nsub = 300
    worst = None
    for j in range(nsub):
        u = iv.mpf([mp.mpf(j)/(nsub*T0), mp.mpf(j + 1)/(nsub*T0)])
        val = iv.mpf(1)/2 + E_PI*rational_part(u)
        worst = val.a if worst is None else min(worst, val.a)
    t = iv.mpf(T0)
    tail = ((iv.mpf(1)/4 + t*t)*(2/t)*(2*PI/t)**Kr/(1 - 2*PI/t)).b
    z = iv.mpc(iv.mpf(5)/4, t/2)
    gb = ((iv.mpf(1)/4 + t*t) * PI**(-iv.mpf(1)/4) * iv.sqrt(2*PI) * abs(z)**(iv.mpf(3)/4)
          * iv.exp(1/(6*abs(z))) * iv.exp(-PI*t/4) / abs(iv.mpc(iv.mpf(1)/4, t/2))).b
    low = worst - (E_PI*tail).b - gb
    print(f'(R1) min_u [1/2 + e^-pi rational] = {mp.nstr(worst, 10)}; e^-pi*tail <= {mp.nstr((E_PI*tail).b, 3)}; '
          f'Gamma term <= {mp.nstr(gb, 3)}; => xi_1(1/2+it) >= {mp.nstr(low, 8)} for all t >= {T0}')
    rep['R1'] = {'min_rational': mp.nstr(worst, 12), 'tail': mp.nstr((E_PI*tail).b, 4), 'gamma_term': mp.nstr(gb, 4),
                 'lower_bound': mp.nstr(low, 10), 'certified_positive_t_ge_30': bool(low > 0)}


def run_R2R3(rep, t00, ta=0, tb=30):
    half = mp.mpf(1)/2
    na = int(ta*10); nb = int(tb*10)
    todo = [(mp.mpf(j)/10, mp.mpf(j + 1)/10) for j in range(na, nb)][::-1]
    undecided = []
    nev = 0
    while todo:
        a, b = todo.pop()
        enc = xi1_iv(iv.mpc(iv.mpf(half), iv.mpf([a, b]))).real
        nev += 1
        if enc.a > 0 or enc.b < 0:
            continue
        if b - a < mp.mpf('1e-6'):
            undecided.append((a, b))
            continue
        m = (a + b)/2
        todo.append((m, b))
        todo.append((a, m))
    clusters = []
    for (a, b) in sorted(undecided):
        if clusters and a - clusters[-1][1] < mp.mpf('1e-5'):
            clusters[-1] = (clusters[-1][0], b)
        else:
            clusters.append((a, b))
    print(f'(R2) {nev} enclosures on [0,30]; undecided clusters: '
          f'{[(mp.nstr(a, 14), mp.nstr(b, 14)) for (a, b) in clusters]}  ({time.time()-t00:.0f}s)'); sys.stdout.flush()
    rep['R2'] = {'n_enclosures': nev, 'clusters': [[mp.nstr(a, 20), mp.nstr(b, 20)] for (a, b) in clusters]}
    rep['R3'] = []
    for (a, b) in clusters:
        c = (a + b)/2
        hw = max(mp.mpf('1e-4'), 3*(b - a))
        corners = [mp.mpc(half - hw, c - hw), mp.mpc(half + hw, c - hw), mp.mpc(half + hw, c + hw), mp.mpc(half - hw, c + hw)]
        w, bad, npc = rigorous_winding(xi1_iv, corners, 8)
        print(f'(R3) square half-width {mp.nstr(hw, 3)} at t = {mp.nstr(c, 16)}: winding = {mp.nstr(w, 8) if w is not None else None} '
              f'({npc} pieces){" FAILED at " + str(bad) if bad else ""}  ({time.time()-t00:.0f}s)'); sys.stdout.flush()
        rep['R3'].append({'t_center': mp.nstr(c, 20), 'halfwidth': mp.nstr(hw, 4),
                          'winding': mp.nstr(w, 10) if w is not None else None, 'pieces': npc})


def run_R4(rep, t00):
    z0 = mp.mpc('5.165902026924569091939', '22.91546577056082331413')
    hw = mp.mpf('1e-8')
    corners = [z0 + mp.mpc(-hw, -hw), z0 + mp.mpc(hw, -hw), z0 + mp.mpc(hw, hw), z0 + mp.mpc(-hw, hw)]
    w, bad, npc = rigorous_winding(xi1_iv, corners, 8)
    print(f'(R4) square half-width {hw} around {mp.nstr(z0, 22)}: winding = {mp.nstr(w, 8) if w is not None else None} '
          f'({npc} pieces){" FAILED at " + str(bad) if bad else ""}  ({time.time()-t00:.0f}s)')
    rep['R4'] = {'center': mp.nstr(z0, 22), 'halfwidth': str(hw), 'winding': mp.nstr(w, 10) if w is not None else None,
                 'pieces': npc}


if __name__ == '__main__':
    t00 = time.time()
    which = sys.argv[1:] or ['R1', 'R2', 'R4']
    rng = None
    if 'R2' in which and len(which) >= 3 and which[0] == 'R2':
        rng = (int(which[1]), int(which[2]))
    rep = {'which': which}
    mp.mp.dps = 50
    sys.path.insert(0, '.')
    import stair as st
    Z = st.Chain('zeta')
    # sanity: enclosures contain independent mp values (direct formula at 80 digits)
    for s0 in [mp.mpc('0.5', '14.1'), mp.mpc('5.2', '22.9'), mp.mpc('0.5', '29.5'), mp.mpc('0.5', '3'), mp.mpc('0.5', '19.5')]:
        enc = xi1_iv(iv.mpc(s0.real, s0.imag))
        with mp.workdps(80):
            ref = Z.E_direct(s0, st.w_trunc(1), 1)
        ok = (enc.real.a <= ref.real <= enc.real.b) and (enc.imag.a <= ref.imag <= enc.imag.b)
        print('sanity', mp.nstr(s0, 6), 'value', mp.nstr(ref, 12), 'enclosure width', mp.nstr(enc.real.delta, 3), 'contains:', ok)
        rep.setdefault('sanity', []).append([mp.nstr(s0, 6), bool(ok), mp.nstr(enc.real.delta, 3)])
    g1 = gamma_iv(iv.mpc(iv.mpf('0.25'), iv.mpf('11.3')))
    g2 = iv.gamma(iv.mpc(iv.mpf('0.25'), iv.mpf('11.3')))
    print('gamma_iv(0.25+11.3i) =', g1, '\n iv.gamma             =', g2)
    sys.stdout.flush()
    if 'R1' in which:
        run_R1(rep)
    if 'R4' in which:
        run_R4(rep, t00)
    if 'R2' in which:
        if rng:
            run_R2R3(rep, t00, rng[0], rng[1])
        else:
            run_R2R3(rep, t00)
    rep['elapsed_s'] = round(time.time() - t00)
    json.dump(rep, open('rigor_xi1_' + '_'.join(which) + '.json', 'w'), indent=1)
    print('saved', rep['elapsed_s'], 's')
