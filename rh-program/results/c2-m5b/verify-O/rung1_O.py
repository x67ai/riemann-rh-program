#!/usr/bin/env python3
"""rung1_O.py — the Opus reader's independent rung-1 computation (FORMULATION.md §3.1).
Own F_{7^n} arithmetic (polynomials over F_7 modulo a Conway-free irreducible found by search), own point counts
#C(F_{q^n}) = q^n + 1 + sum_x chi(f(x)) for y^2 = f(x), deg f odd (one point at infinity), own Newton identities
(exact Fractions), own functional equation a_{2g-k} = q^{g-k} a_k, own root check, own Toeplitz ranks (sympy exact).
"""
from fractions import Fraction as Fr
import itertools, time, sympy as sp
t0 = time.time(); p = 7
def pmod(a, m):       # a, m lists low->high over F_p, m monic
    a = a[:]
    while len(a) >= len(m):
        c = a[-1] % p
        if c:
            sh = len(a) - len(m)
            for i, mi in enumerate(m): a[sh+i] = (a[sh+i] - c*mi) % p
        a.pop()
    return [x % p for x in a]
def pmul(a, b, m):
    r = [0]*(len(a)+len(b)-1 if a and b else 0)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b): r[i+j] = (r[i+j] + x*y) % p
    return pmod(r, m)
def ppow(a, e, m):
    r = [1]; b = a[:]
    while e:
        if e & 1: r = pmul(r, b, m)
        b = pmul(b, b, m); e >>= 1
    return r
def is_irred(m, n):   # degree-n monic m irreducible iff x^{p^n} = x mod m and gcd conditions (n <= 4: check no roots in subfields by brute force)
    if n == 1: return True
    # brute: m has no factor of degree <= n//2
    for d in range(1, n//2 + 1):
        for coeffs in itertools.product(range(p), repeat=d):
            f = list(coeffs) + [1]
            if not any(pmod(m, f)): return False
    return True
def field(n):
    for coeffs in itertools.product(range(p), repeat=n):
        m = list(coeffs) + [1]
        if coeffs[0] and is_irred(m, n): return m
def elements(n):
    for c in itertools.product(range(p), repeat=n): yield list(c)
def strip(a):
    a = a[:]
    while a and a[-1] == 0: a.pop()
    return a
def count(fcoef, n):  # fcoef: integer coefficients low->high of f(x)
    m = field(n); q = p**n; S = 0
    for x in elements(n):
        # f(x) = sum_i c_i x^i, evaluated with explicit powers of x in F_{p^n}
        v = [0]*n; xp = [1]
        for c in fcoef:
            if c:
                t_ = xp + [0]*(n - len(xp))
                v = [(vi + c*ti) % p for vi, ti in zip(v, t_)]
            xp = pmul(xp, x, m) if strip(x) else [0]
            xp = xp or [0]
        v = strip(v)
        if not any(v): continue
        chi = strip(ppow(v, (q-1)//2, m))
        S += 1 if chi == [1] else -1
    return q + 1 + S
def newton(s, g, q):
    # P(t) = 1 + a1 t + ... ; power sums s_k of the roots alpha_i of prod(1 - alpha_i t): k a_k = -sum_{j=1}^{k} s_j a_{k-j}
    a = [Fr(1)]
    for k in range(1, g+1): a.append(-sum(Fr(s[j-1])*a[k-j] for j in range(1, k+1))/k)
    for k in range(g+1, 2*g+1): a.append(Fr(q)**(k-g)*a[2*g-k])
    return a
def powersums(a, K):
    # Newton: s_k = -k a_k - sum_{j=1}^{k-1} a_j s_{k-j}  (a_k = 0 for k > deg)
    d = len(a) - 1; s = [None]
    for k in range(1, K+1):
        s.append((-k*a[k] if k <= d else 0) - sum(a[j]*s[k-j] for j in range(1, min(k-1, d)+1)))
    return s[1:]
curves = {1: ("y^2 = x^3 + x + 1", [1, 1, 0, 1]), 2: ("y^2 = x^5 + 3x + 1", [1, 3, 0, 0, 0, 1]), 3: ("y^2 = x^7 + x + 1", [1, 1, 0, 0, 0, 0, 0, 1])}
x = sp.symbols('x'); tt = sp.symbols('t')
print("squarefree mod 7 check of the brief's y^2 = x^5 + x + 1:", sp.factor_list(x**5 + x + 1, modulus=7))
for g, (name, fc) in curves.items():
    fpoly = sum(c*x**i for i, c in enumerate(fc))
    print(f"\n== genus {g}: {name};  gcd(f, f') mod 7 = {sp.gcd(sp.Poly(fpoly, x, modulus=7), sp.Poly(sp.diff(fpoly, x), x, modulus=7))}; disc mod 7 = {sp.discriminant(fpoly, x) % 7}")
    Ns = [count(fc, n) for n in range(1, 5)]
    s = [p**n + 1 - N for n, N in zip(range(1, 5), Ns)]
    a = newton(s[:g], g, p)
    P = sum(sp.Rational(c.numerator, c.denominator)*tt**i for i, c in enumerate(a))
    spred = powersums(a, 4)
    print(f"  N_1..N_4 = {Ns};  s_1..s_4 = {s};  P(t) from s_1..s_{g} + FE = {sp.expand(P)} = {sp.factor(P)}")
    print(f"  predicted s_1..s_4 from P: {[int(v) for v in spred]}  match: {[int(v) for v in spred] == s}")
    roots = sp.Poly(sp.expand(tt**(2*g)*P.subs(tt, 1/tt)), tt).all_roots()
    print(f"  |alpha_i|^2 = {sorted(set([sp.nsimplify(sp.N(abs(r)**2, 30), rational=True) for r in roots]))} (q = 7);  distinct alphas: {len(set([sp.N(r, 25) for r in roots]))} of {2*g}  [{time.time()-t0:.1f} s]")
    for mm in range(1, g):
        c = [sp.Integer(2*g)] + [sp.Integer(s[k-1])/sp.sqrt(7)**k for k in range(1, mm+1)]
        Tm = sp.Matrix(mm+1, mm+1, lambda i, j: c[abs(i-j)])
        # relaxation: all sign patterns of c_1..c_m (the |c_k| data only)
        ranks = {}
        for signs in itertools.product((1, -1), repeat=mm):
            cc = [c[0]] + [sg*ck for sg, ck in zip(signs, c[1:])]
            ranks[signs] = sp.Matrix(mm+1, mm+1, lambda i, j: cc[abs(i-j)]).rank()
        print(f"  m = {mm} < g: T_m = {Tm.tolist()}; eigenvalues {[sp.nsimplify(e) for e in Tm.eigenvals()]}; rank {Tm.rank()} ; ranks over sign flips of c_k (|c_k|-only relaxation): {ranks}")
# exact minimum N_d below g by enumeration of small patterns, on the circle: conj pairs e^{+-i th} sqrt7 (s_k contribution 2*7^{k/2} cos k th) with multiplicity, real points +-sqrt7
print("\n== exact minima below g (reader's own reasoning, checked symbolically) ==")
b = sp.symbols('b', real=True)
# g=2, m=1: s1 = -3. N_d = 1 impossible (a single conj-invariant point is real: s1 = +-4 sqrt7). N_d = 2: pair (1 - b t + 7t^2)^2 -> 2b = -3
print("g=2,m=1: N_d=1 needs s1 = +-4*sqrt(7) =", [4*sp.sqrt(7), -4*sp.sqrt(7)], "!= -3; N_d=2: 2b = -3 ->", sp.solve(2*b+3, b), "|b| <= 2 sqrt7:", abs(sp.Rational(-3, 2)) <= 2*sp.sqrt(7))
print("g=2,m=1 relaxation (s1 -> +3): N_d=2 with b = 3/2, same minimum 2; also real pair {sqrt7 x2, -sqrt7 x2} has s1 = 0 != +-3")
# g=3, m=1,2: s1 = 0, s2 = -42
for pat, (s1, s2) in {"R+^3 R-^3 (1-7t^2)^3": (0, 42), "(1+7t^2)^3 (+-i sqrt7, mark 3)": (0, -42), "R+^6": (6*sp.sqrt(7), 42), "R-^6": (-6*sp.sqrt(7), 42)}.items():
    print(f"g=3 N_d<=2 pattern {pat}: s1 = {s1}, s2 = {s2}")
th = sp.symbols('theta', real=True)
print("g=3 N_d=2 general conj pair with mark 3: s1 = 6 sqrt7 cos th = 0 -> th = pi/2 -> s2 = 6*7*cos(2th) =", 6*7*sp.cos(2*sp.pi/2))
print("g=3 N_d=2 conj-pair + real point: masses 2k + (6-2k) with k in {1,2}... listed: pair mark k at angle th, real point +-sqrt7 mark 6-2k:")
for k in (1, 2):
    for sgn in (1, -1):
        sol = sp.solve(sp.Eq(2*k*sp.sqrt(7)*sp.cos(th) + sgn*(6-2*k)*sp.sqrt(7), 0), th)
        print(f"   k = {k}, real point {'+' if sgn>0 else '-'}sqrt7: s1 = 0 -> theta in {sol}; s2 at those =", [sp.simplify(2*k*7*sp.cos(2*x_) + (6-2*k)*7) for x_ in sol])
print(f"total {time.time()-t0:.1f} s")
