"""o2 (read-O, qcond-s38): the reduced uniformly-discrete family (NOTE §2.4 Step 4, §2.5 Part B) and the radical family
(v4), decided by EXACT Sturm certificates over Q (no floating point, no interval library) -- independent of verify/v2, v4.

Route (own derivations, nothing imported from verify/):
 (1) the family: D(s) = sum_{d|q} e_d d^{-s}, e_1 = 1, with the conductor-q FE D(1-s) = q^{s-1/2} D(s) imposed by
     matching the coefficients of d^s (solved by sympy.solve, not by hand);
 (2) dN >= 0: c(n) = sum_{d | gcd(n,q)} e_d >= 0 for every divisor g = gcd(n, q);
 (3) Pi on the q-part: single prime q = p^k: D = prod_r (1 - mu_r u), u = p^{-s}; power sums s_n of the mu_r by NEWTON's
     identities; Pi(p^n) = (1 - s_n)/n (the -log(1-u) of zeta adds 1/n).  q = 6: closed multinomial formula for the
     coefficients of log(1 + a u + b v + c uv); Pi(2^i 3^j) = [log D]_{ij} + 1/i [j=0] + 1/j [i=0].
     Radical family (q = 2): D = 1 + a w + sqrt2 w^2, w = 2^{-s/2}, h = D/(1 - w^2): Pi(2^{k/2}) = -s_k/k + (2/k)[k even].
 (4) certificate: the parameter half-line is covered by closed rational intervals [x, y], each carrying a witness
     P (a Pi-coefficient) with P(x) < 0 EXACTLY and NO real root of the norm N = A^2 - r B^2 (P = A + sqrt(r) B,
     A, B in Q[t]) in [x, y] by Sturm (sympy count_roots, exact over Q); the unbounded end by the k = 2 coefficient.
"""
import sympy as sp
from math import comb, factorial

R = sp.Rational
t = sp.Symbol('t', real=True)

def family(q):
    s = sp.Symbol('s')
    ds = sp.divisors(q)
    E = {d: (sp.Integer(1) if d == 1 else sp.Symbol(f"e{d}")) for d in ds}
    # D(1-s) = sum (e_d/d) d^s ; q^{s-1/2} D(s) = sum e_d q^{-1/2} (q/d)^s  -> match coefficients of d'^s
    eqs = [sp.Eq(E[dp]/sp.Integer(dp), E[q//dp]/sp.sqrt(q)) for dp in ds]
    unknowns = [E[d] for d in ds if d != 1]
    sol = sp.solve(eqs, unknowns, dict=True)[0]
    Es = {d: sp.simplify(E[d].subs(sol)) if d != 1 else sp.Integer(1) for d in ds}
    free = sorted({x for d in ds for x in sp.sympify(Es[d]).free_symbols}, key=str)
    D = sum(Es[d]*sp.Integer(d)**(-s) for d in ds)
    chk = [sp.N((D.subs(s, 1 - z) - q**(z - R(1, 2))*D.subs(s, z)).subs({f: R(7, 10) for f in free}), 40) for z in (R(3, 10) + 2*sp.I, -R(6, 5) + sp.I/7)]
    return Es, free, max(abs(c) for c in chk)

def power_sums(coeffs, N):
    """D(u) = 1 + c1 u + ... + ck u^k = prod (1 - mu_r u): return s_1..s_N via Newton (e_j = (-1)^j c_j)."""
    k = len(coeffs) - 1
    e = [1] + [(-1)**j*coeffs[j] for j in range(1, k + 1)]
    s = [None]*(N + 1)
    for n in range(1, N + 1):
        acc = 0
        for j in range(1, min(n - 1, k) + 1):
            acc += (-1)**(j - 1)*e[j]*s[n - j]
        if n <= k:
            acc += (-1)**(n - 1)*n*e[n]
        s[n] = sp.expand(acc)
    return s

def logcoef_2var(a, b, c, i, j):
    """coefficient of u^i v^j in log(1 + a u + b v + c u v): sum over (al, be, ga), al+ga = i, be+ga = j."""
    tot = 0
    for ga in range(0, min(i, j) + 1):
        al, be = i - ga, j - ga
        m = al + be + ga
        if m == 0:
            continue
        tot += R((-1)**(m + 1), m)*R(factorial(m), factorial(al)*factorial(be)*factorial(ga))*a**al*b**be*c**ga
    return sp.expand(tot)

def split_surd(P, r):
    P = sp.expand(P)
    if r == 1:
        return sp.Poly(P, t), sp.Poly(0, t)
    B = sp.expand(P.coeff(sp.sqrt(r)))
    A = sp.expand(P - sp.sqrt(r)*B)
    assert not A.has(sp.sqrt(r)), (P, A)
    return sp.Poly(A, t, domain='QQ'), sp.Poly(B, t, domain='QQ')

def sign_surd(A, B, r):
    """exact sign of A + sqrt(r) B for rational A, B, r > 0."""
    if B == 0 or r == 1:
        return sp.sign(A + (B if r == 1 else 0))
    if A >= 0 and B >= 0:
        return 1 if (A > 0 or B > 0) else 0
    if A <= 0 and B <= 0:
        return -1
    d = A*A - r*B*B
    return sp.sign(d) if A > 0 else -sp.sign(d)

def neg_on(P, r, x, y):
    A, B = split_surd(P, r)
    if sign_surd(A.eval(x), B.eval(x), r) >= 0:
        return False
    Nrm = A**2 - (r if r != 1 else 0)*B**2 if r != 1 else A
    if Nrm.is_zero:
        return False
    return Nrm.count_roots(x, y) == 0

def cover(polys, r, lo, hi, depth=0, maxdepth=30):
    for lab, P in polys:
        if neg_on(P, r, lo, hi):
            return [(lo, hi, lab)], []
    if depth >= maxdepth:
        return [], [(lo, hi)]
    mid = (lo + hi)/2
    c1, f1 = cover(polys, r, lo, mid, depth + 1, maxdepth)
    c2, f2 = cover(polys, r, mid, hi, depth + 1, maxdepth)
    return c1 + c2, f1 + f2

def merged(cv):
    out = []
    for a, b, lab in cv:
        if out and out[-1][2] == lab and out[-1][1] == a:
            out[-1] = (out[-1][0], b, lab)
        else:
            out.append((a, b, lab))
    return out

def tail_ok(P, r, x0):
    """P < 0 on [x0, oo): P(x0) < 0 and no root of the norm in [x0, oo) and leading coefficient of the norm/P negative."""
    A, B = split_surd(P, r)
    Nrm = A**2 - r*B**2 if r != 1 else A
    return sign_surd(A.eval(x0), B.eval(x0), r) < 0 and Nrm.count_roots(x0, None) == 0

def main():
    K = 12
    print(__doc__.strip().splitlines()[0])
    for q in (2, 3, 5, 4, 9, 25, 6):
        Es, free, res = family(q)
        print(f"\n== q = {q}: FE-solved family e_d = {Es}; free parameters {free}; FE residual at 2 points = {sp.N(res, 3)}")
        g_constraints = {g: sp.simplify(sum(Es[d] for d in sp.divisors(g))) for g in sp.divisors(q)}
        print(f"   c(n) by g = gcd(n,q): {g_constraints}")
        if not free:
            p = q
            s = power_sums([1, Es[p]], 6)
            Pi = [sp.nsimplify(sp.expand((1 - s[n])/n)) for n in range(1, 7)]
            print(f"   Pi(p^n), n=1..6 (Newton): {Pi};  Pi(p^2) = {Pi[1]} = (1-p)/2: {sp.simplify(Pi[1] - R(1 - p, 2)) == 0}  -> INFEASIBLE (exact)")
            continue
        if q in (4, 9, 25):
            p = sp.primefactors(q)[0]
            e = free[0]
            coeffs = [1, Es[p].subs(e, t), Es[q]]
            s = power_sums(coeffs, K)
            polys = [(f"Pi({p}^{n})", sp.expand((1 - s[n])/n)) for n in range(1, K + 1)]
            lo = -1     # c(n) >= 0 <=> 1 + e >= 0 (and 1 + e + p >= 0)
            r = 1
            import math; x0 = R(math.isqrt((2*p + 1)*10000) + 1, 100)
        else:  # q = 6
            a = free[0]
            b, c = sp.expand(Es[3].subs(a, t)), sp.expand(Es[6])
            aa = sp.expand(Es[2].subs(a, t))
            polys = []
            for tot in range(1, K + 1):
                for i in range(0, tot + 1):
                    j = tot - i
                    P = logcoef_2var(aa, b, c, i, j) + (R(1, i) if (j == 0 and i > 0) else 0) + (R(1, j) if (i == 0 and j > 0) else 0)
                    polys.append((f"Pi(2^{i}3^{j}={2**i*3**j})", sp.expand(P)))
            # sympy's solve leaves t = e_3 free (e_2 = sqrt6 t/3): c(n) >= 0 <=> 1 + t >= 0 and 1 + sqrt6 t/3 >= 0 <=> t >= -1
            assert sp.simplify(Es[2] - sp.sqrt(6)*a/3) == 0 and a == sp.Symbol('e3')
            lo = -1
            r = 6
            x0 = R(174, 100)       # > sqrt 3: Pi(6) = sqrt6 (1 - t^2/3) < 0 beyond
        tailP = [P for lab, P in polys if lab.startswith(f"Pi({sp.primefactors(q)[0]}^2)") or lab.startswith("Pi(2^13^1")][0]
        print(f"   tail witness {sp.factor(tailP)} < 0 on [{x0}, oo): {tail_ok(tailP, r, x0)}")
        cv, fails = cover(polys, r, sp.nsimplify(lo), x0)
        print(f"   [{lo}, {x0}] covered by {len(cv)} exact Sturm pieces; failures: {len(fails)}")
        for a1, b1, lab in merged(cv):
            print(f"     [{float(a1):+.6f}, {float(b1):+.6f}]  witness {lab} < 0")
        if q == 25:
            print(f"   F_(5,5) = the point e = 5: Pi(5^n), n=1..6 = {[sp.nsimplify(P.subs(t, 5)) for lab, P in polys[:6]]}")
    # radical family, q = 2
    print("\n== radical family (v4): D = 1 + a w + sqrt2 w^2, w = 2^{-s/2}; FE, dN >= 0 and Pi >= 0 on <sqrt2>")
    s_ = sp.Symbol('s')
    D = lambda z, av: 1 + av*2**(-z/2) + sp.sqrt(2)*2**(-z)
    fe = max(abs(sp.N(D(1 - z, R(7, 10)) - 2**(z - R(1, 2))*D(z, R(7, 10)), 40)) for z in (R(3, 10) + 2*sp.I, -R(9, 5) + sp.I/3))
    print(f"   FE residual D(1-s) - 2^(s-1/2) D(s) at a = 7/10, two points: {sp.N(fe, 3)} (identity: 1<->2 paired, sqrt2 self-paired)")
    s = power_sums([1, t, sp.sqrt(2)], K)
    polys = [(f"Pi(2^({n}/2))", sp.expand(-s[n]/n + (R(2, n) if n % 2 == 0 else 0))) for n in range(1, K + 1)]
    print(f"   Pi(2) = {sp.expand(polys[1][1])};  tail < 0 on [221/100, oo): {tail_ok(polys[1][1], 2, R(221, 100))}")
    cv, fails = cover(polys, 2, sp.Integer(0), R(221, 100))
    print(f"   [0, 2.21] covered by {len(cv)} exact Sturm pieces; failures: {len(fails)}")
    for a1, b1, lab in merged(cv):
        print(f"     [{float(a1):+.6f}, {float(b1):+.6f}]  witness {lab} < 0")
    # the Beurling neighbour zeta(s)(1 + b 2^{-s/2})
    bb = sp.Symbol('b', positive=True)
    sb = power_sums([1, bb], 8)
    Pib = [sp.expand(-sb[n]/n + (R(2, n) if n % 2 == 0 else 0)) for n in range(1, 9)]
    print(f"   neighbour zeta(1 + b 2^(-s/2)): Pi(2^(n/2)) = {Pib[:4]} ...; even n = 2j: (2 - b^(2j))/(2j) >= 0 for all j <=> b <= 1")
    b_fe = sp.solve(sp.Eq(bb*2**(-R(1, 2)), 2**(-R(1, 4))), bb)
    print(f"   FE at conductor sqrt2 forces b = {b_fe}; Pi(8) = Pi(2^(6/2)) at that b = {sp.nsimplify(Pib[5].subs(bb, b_fe[0]))} = {sp.N(Pib[5].subs(bb, b_fe[0]), 6)}")

if __name__ == "__main__":
    main()
