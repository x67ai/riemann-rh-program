# read-O: the signed Euler exponents of L = 1 + sum_k ell_k^{-s}, by two exact routes in the free commutative
# power-series ring Z[[X_1..X_K]] (X_k <-> ell_k^{-s}; distinct multisets <-> distinct products for transcendental t).
# Route 1: coefficients of log(1 + sum X_k) (exact Fractions) + Moebius inversion over perfect powers.
# Route 2: Witt-style peeling: m_mu := coeff of (current quotient) at mu, divide by (1 - X^mu)^{-m_mu}, in graded order.
# Then a numerical check with real values at rho = pi/16 (all products <= 400, truncated product vs L at s = 3, 2.5).
from fractions import Fraction
from itertools import combinations_with_replacement
from math import factorial, gcd
from functools import reduce
K, D = 5, 7                      # 5 variables, total degree <= 7

def monos(deg):                  # exponent tuples of total degree deg
    out = []
    for c in combinations_with_replacement(range(K), deg):
        e = [0]*K
        for i in c: e[i] += 1
        out.append(tuple(e))
    return out
ALL = [e for d in range(1, D+1) for e in monos(d)]

def mul(A, B):                   # truncated product of dict power series
    C = {}
    for ea, ca in A.items():
        for eb, cb in B.items():
            e = tuple(x+y for x, y in zip(ea, eb))
            if sum(e) <= D: C[e] = C.get(e, 0) + ca*cb
    return {e: c for e, c in C.items() if c != 0}

one = {tuple([0]*K): Fraction(1)}
X = {tuple(1 if i == j else 0 for i in range(K)): Fraction(1) for j in range(K)}
# Route 1: log(1+X) = sum_{m>=1} (-1)^{m+1} X^m / m
logL, P = {}, dict(one)
for m in range(1, D+1):
    P = mul(P, X)
    for e, c in P.items(): logL[e] = logL.get(e, 0) + Fraction((-1)**(m+1), m)*c
def mobius(n):
    r, p, m = 1, 2, n
    while p*p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0: return 0
            r = -r
        p += 1
    return -r if m > 1 else r
m1 = {}
for e in ALL:
    g = reduce(gcd, [x for x in e if x])
    m1[e] = sum(Fraction(mobius(j), j)*logL.get(tuple(x//j for x in e), 0) for j in range(1, g+1) if g % j == 0)
# Route 2: peeling. Q starts as 1 + X; for mu in graded order: m_mu = coeff of Q at mu; Q := Q * (1 - X^mu)^{m_mu}
Q = mul(one, {**one, **X})
m2 = {}
def power_series_binom(e, m):    # (1 - X^e)^m truncated, m integer of either sign
    out, term, j = dict(one), Fraction(1), 0
    while True:
        j += 1
        if sum(e)*j > D: break
        # coefficient of (X^e)^j in (1 - y)^m is (-1)^j * binom(m, j) (generalized)
        b = Fraction(1)
        for i in range(j): b = b*(m - i)/(i + 1)
        out[tuple(x*j for x in e)] = (-1)**j*b
    return out
for d in range(1, D+1):
    for e in monos(d):
        c = Q.get(e, 0)
        assert c.denominator == 1, ("non-integer exponent", e, c)
        m2[e] = c
        if c != 0: Q = mul(Q, power_series_binom(e, int(c)))
assert all(v == 0 for e, v in Q.items() if sum(e) > 0), "peeling did not reduce to 1"
agree = all(m1[e] == m2[e] for e in ALL)
print("route1 == route2 on all", len(ALL), "monomials of degree <=", D, "with", K, "variables:", agree)
print("all exponents integers:", all(m2[e].denominator == 1 for e in ALL))
def c_formula(e):
    k = sum(e); return Fraction((-1)**(k+1)*factorial(k-1), reduce(lambda a, b: a*b, [factorial(x) for x in e]))
print("log-coefficient == (-1)^{k+1}(k-1)!/prod e_i! everywhere:", all(logL[e] == c_formula(e) for e in ALL))
samples = {"l1": (1,0,0,0,0), "l1 l2": (1,1,0,0,0), "l1^2": (2,0,0,0,0), "l1 l2 l3": (1,1,1,0,0), "l1..l4": (1,1,1,1,0),
           "l1..l5": (1,1,1,1,1), "l1^2 l2": (2,1,0,0,0), "l1^3": (3,0,0,0,0), "l1^3 l2": (3,1,0,0,0), "l1^4": (4,0,0,0,0),
           "l1^2 l2^2": (2,2,0,0,0), "l1^6": (6,0,0,0,0), "l1^2 l2 l3": (2,1,1,0,0), "l1^4 l2^2": (4,2,0,0,0)}
for nm, e in samples.items():
    print(f"  m[{nm}] = {m2[e]}   Pi_L weight (log-coeff) = {logL[e]}")
distinct_ok = all(m2[e] == (-1)**(sum(e)+1)*factorial(sum(e)-1) for e in ALL if max(e) == 1)
print("m = (-1)^{k+1}(k-1)! at every product of k distinct atoms (k<=5):", distinct_ok)
print("m = -1 at every 2-fold product (incl. squares):", all(m2[e] == -1 for e in monos(2)))
