"""v2 (qcond-s38, task 2).

Part A. Identity (E) of NOTE §2.1 (Prop. E) is a consequence of self-duality alone, so it can be checked on the
non-Beurling self-dual examples:  2 q^{-1/2} sum_t c2(t) S(t/q) = rho (m1 - q^{-1/2} m0) + 2 sum_m w_m m^{-1} sum_{n<m} c(n)(1-n/m),
with dN2 = dN * w, w = sum_m w_m delta_m.  For dN a finite sum of combs a_j sum_n delta_{b_j n}, the left side is EXACT via
Poisson: T(e) := sum_{n>=1} S(n e) = ((1/e)(1 + 2 sum_{1<=k<e}(1-k/e)) - 1)/2   (no truncation, no tail).
Part B. The reduced uniformly-discrete family (NOTE §2.4 Steps 1-4): F = zeta * D, D = sum_{d|q} e_d d^{-s}, e_1 = 1,
e_{q/d} = e_d sqrt(q)/d.  Beurling on the q-part <=> log h has nonnegative coefficients, h = D * prod_{p|q} (1-p^{-s})^{-1}.
For q = 2,3,5 (no parameter), q = 4,9,25 (one parameter e = e_{sqrt q}), q = 6 (one parameter a = e_2) we certify, by
interval arithmetic on a subdivision of the parameter range allowed by c(n) >= 0, that some coefficient of log h of bounded
degree is NEGATIVE for every parameter value (an infeasibility certificate at a finite bound B = largest frequency used).
"""
import mpmath as mp
import sympy as sp
from fractions import Fraction

mp.mp.dps = 50
iv = mp.iv
iv.dps = 50

def T(e):
    e = mp.mpf(e)
    K = int(mp.floor(e))
    if K == e:
        K -= 1  # k < e strictly
    s = 1 + 2*mp.fsum((1 - k/e) for k in range(1, K+1))
    return (s/e - 1)/2

def partA():
    print("Part A: identity (E) on self-dual examples (exact Poisson closed form on the left)")
    ex = {
        "zeta (q=1)": (1, [(1, 1)]),
        "zeta(1+2^{1/2-s}) (q=2)": (2, [(1, 1), (2, mp.sqrt(2))]),
        "zeta(1+2^{1-2s}) (q=4)": (4, [(1, 1), (4, 2)]),
        "zeta(1+9^{1/2-s}) (q=9)": (9, [(1, 1), (9, 3)]),
        "F55 (q=25)": (25, [(1, 1), (5, 5), (25, 5)]),
    }
    sieves = {"w=delta1": {1: 1}, "w=d1-d2": {1: 1, 2: -1}, "w=d1-d3": {1: 1, 3: -1},
              "w=(d1-d2)(d1-d3)": {1: 1, 2: -1, 3: -1, 6: 1}, "w=(d1-d2)(d1-d3)(d1-d5)": {1: 1, 2: -1, 3: -1, 5: -1, 6: 1, 10: 1, 15: 1, 30: -1}}
    for name, (q, combs) in ex.items():
        q = mp.mpf(q)
        rho = mp.sqrt(q)*mp.fsum(mp.mpf(a)/b for b, a in combs)   # rho_q = sqrt(q) * Res F
        def c(n):
            return mp.fsum(a for b, a in combs if n % b == 0)
        print(f"== {name}: rho_q = {mp.nstr(rho, 15)}")
        for sname, w in sieves.items():
            lhs = 2/mp.sqrt(q)*mp.fsum(wm*a*T(m*b/q) for m, wm in w.items() for b, a in combs)
            m1 = mp.fsum(wm/mp.mpf(m) for m, wm in w.items()); m0 = mp.fsum(w.values())
            rhs = rho*(m1 - m0/mp.sqrt(q)) + 2*mp.fsum(wm/mp.mpf(m)*mp.fsum(c(n)*(1 - mp.mpf(n)/m) for n in range(1, m)) for m, wm in w.items())
            print(f"   {sname:28s} lhs = {mp.nstr(lhs, 20):>26s}  rhs = {mp.nstr(rhs, 20):>26s}  diff = {mp.nstr(lhs-rhs, 3)}")

def log_coeffs_1var(d, K):
    """coefficients l_1..l_K of log(sum_j d_j u^j), d_0 = 1, via k l_k = k d_k - sum_{j=1}^{k-1} j l_j d_{k-j}."""
    l = [0]*(K+1)
    dd = lambda j: d[j] if j < len(d) else 0
    for k in range(1, K+1):
        l[k] = sp.expand(dd(k) - sp.Rational(1, k)*sum(j*l[j]*dd(k-j) for j in range(1, k)))
    return l

def ivpoly(expr, var, I):
    """rigorous interval enclosure of a polynomial (sympy, coefficients algebraic) on the interval I."""
    P = sp.Poly(sp.expand(expr), var)
    acc = iv.mpf(0)
    for (k,), coef in P.terms():
        cv = mp.mpf(sp.N(coef, 60))
        cI = iv.mpf([cv - mp.mpf(10)**-45, cv + mp.mpf(10)**-45])
        acc += cI * I**k
    return acc

def ivpoly_horner(expr, var, I):
    """rigorous enclosure by Horner's scheme with interval coefficients (outward rounding by mpmath.iv)."""
    P = sp.Poly(sp.expand(expr), var)
    coeffs = P.all_coeffs()  # highest degree first
    acc = iv.mpf(0)
    for coef in coeffs:
        cv = mp.mpf(sp.N(coef, 60))
        cI = iv.mpf([cv - mp.mpf(10)**-45, cv + mp.mpf(10)**-45])
        acc = acc*I + cI
    return acc

def certify(polys, var, lo, hi, maxdepth=40):
    """cover [lo, hi] by subintervals on each of which some poly in polys (list of (label, expr)) is < 0 rigorously."""
    cover, stack, fails = [], [(mp.mpf(lo), mp.mpf(hi), 0)], []
    while stack:
        a, b, dep = stack.pop()
        I = iv.mpf([a, b])
        hit = None
        for lab, ex in polys:
            if ivpoly_horner(ex, var, I).b < 0:
                hit = lab; break
        if hit is not None:
            cover.append((a, b, hit))
        elif dep >= maxdepth:
            fails.append((a, b))
        else:
            m = (a + b)/2
            stack += [(a, m, dep+1), (m, b, dep+1)]
    cover.sort(key=lambda t: t[0])
    return cover, fails

def summarize(cover):
    # merge consecutive pieces with the same witness label
    out = []
    for a, b, lab in cover:
        if out and out[-1][2] == lab and abs(out[-1][1] - a) < mp.mpf(10)**-40:
            out[-1] = (out[-1][0], b, lab)
        else:
            out.append((a, b, lab))
    return out

def partB():
    print("\nPart B: reduced u.d. family F = zeta*D (NOTE §2.4 Step 4); positivity of Pi on the q-part <=> log h >= 0 coefficientwise")
    e = sp.Symbol('e', real=True)
    K = 14
    for p in (2, 3, 5):
        d = [1, sp.sqrt(p)]
        l = log_coeffs_1var(d, K)
        coefs = [(k, sp.nsimplify(l[k] + sp.Rational(1, k))) for k in range(1, K+1)]
        neg = [(k, float(v)) for k, v in coefs if float(v) < 0]
        print(f"== q={p}: D = 1 + sqrt({p}) {p}^-s (no parameter). Pi({p}^k) for k=1..6: " +
              ", ".join(f"{float(v):.4f}" for k, v in coefs[:6]) + f"; first negative at k={neg[0][0]} (frequency B = {p}^{neg[0][0]} = {p**neg[0][0]})")
    for p in (2, 3, 5):
        q = p*p
        d = [1, e, p]
        l = log_coeffs_1var(d, K)
        polys = [(f"k={k} (freq {p}^{k})", sp.expand(l[k] + sp.Rational(1, k))) for k in range(1, K+1)]
        E0 = mp.sqrt(2*p + 1) + mp.mpf('0.01')
        c2 = ivpoly_horner(polys[1][1], e, iv.mpf([E0, E0]))
        cover, fails = certify(polys, e, -1, E0)
        kmax = max(int(lab.split('=')[1].split(' ')[0]) for _, _, lab in cover) if cover else None
        print(f"== q={q}: D = 1 + e*{p}^-s + {p}*{q}^-s; c(n) >= 0 <=> e >= -1. Coef k=2 = {p} + 1/2 - e^2/2 < 0 for e >= {mp.nstr(E0,6)} "
              f"(upper enclosure at E0: {mp.nstr(mp.mpf(c2.b.b),8)}; it decreases for e > 0).")
        print(f"   [-1, {mp.nstr(E0,6)}] covered: {len(cover)} pieces, failures {len(fails)}; max degree used {kmax} (B = {p}^{kmax} = {p**kmax if kmax else None})")
        for a, b, lab in summarize(cover):
            print(f"     e in [{mp.nstr(a, 8)}, {mp.nstr(b, 8)}]: negative coefficient {lab}")
        if q == 25:
            v = [float((l[k] + sp.Rational(1, k)).subs(e, 5)) for k in range(1, 7)]
            print(f"   F55 (e = 5): Pi(5^k) = {', '.join(f'{x:.4f}' for x in v)}  (BFE: Lambda(5^k)/log 5 = k*Pi = 6, -14, 51, ...)")

def partB6(K=10):
    print("\n== q=6 (two primes): D = 1 + a 2^-s + a(sqrt6/2) 3^-s + sqrt6 6^-s; h = D/((1-2^-s)(1-3^-s)); u = 2^-s, v = 3^-s")
    a, t, x, y = sp.symbols('a t x y', real=True)
    b = a*sp.sqrt(6)/2
    D = 1 + a*t*x + b*t*y + sp.sqrt(6)*t**2*x*y
    ser = sp.series(sp.log(D), t, 0, K+1).removeO()
    ser = sp.expand(ser)
    polys = []
    for n in range(1, K+1):
        cn = sp.expand(ser.coeff(t, n))
        for i in range(0, n+1):
            j = n - i
            cij = sp.expand(cn.coeff(x, i).coeff(y, j))
            if j == 0: cij += sp.Rational(1, i)
            if i == 0: cij += sp.Rational(1, j)
            polys.append((f"u^{i}v^{j} (freq 2^{i}3^{j}={2**i*3**j})", sp.expand(cij)))
    lo = -2/mp.sqrt(6)   # c(n) >= 0 needs 1 + a >= 0 and 1 + a sqrt6/2 >= 0
    uv = [pp for pp in polys if pp[0].startswith("u^1v^1")][0]
    E0 = mp.sqrt(2) + mp.mpf('0.01')
    print(f"   c(n) >= 0 <=> a >= {mp.nstr(lo,8)}; coefficient at uv = sqrt6(1 - a^2/2) = {uv[1]} < 0 for a > sqrt2 (decreasing in |a|)")
    cover, fails = certify(polys, a, lo, E0)
    freqs = [int(lab.split('=')[1].rstrip(')')) for _, _, lab in cover]
    print(f"   [{mp.nstr(lo,6)}, {mp.nstr(E0,6)}] covered: {len(cover)} pieces, failures {len(fails)}; largest frequency used B = {max(freqs)}")
    for lo_, hi_, lab in summarize(cover):
        print(f"     a in [{mp.nstr(lo_, 8)}, {mp.nstr(hi_, 8)}]: negative coefficient {lab}")

if __name__ == "__main__":
    partA()
    partB()
    partB6()
