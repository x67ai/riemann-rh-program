"""Baseline for seed M2: the virtual curve V=(q,a)=(5,5) and a genuine control E0/F5 with trace 4.
Exact integer arithmetic throughout (s_n = alpha^n + beta^n by the recurrence s_n = t s_{n-1} - q s_{n-2})."""
import math, itertools
from sympy import mobius

def traces(t, q, nmax):
    s = [2, t]
    for n in range(2, nmax + 1):
        s.append(t * s[-1] - q * s[-2])
    return s  # s[n] = alpha^n + beta^n

def counts(t, q, nmax):
    s = traces(t, q, nmax)
    N = [None] + [q**n + 1 - s[n] for n in range(1, nmax + 1)]
    b = [None]
    for d in range(1, nmax + 1):
        tot = sum(mobius(d // e) * N[e] for e in range(1, d + 1) if d % e == 0)
        assert tot % d == 0
        b.append(tot // d)
    return s, N, b

print("=== 1. The virtual curve V: L(u) = 1 - 5u + 5u^2 over F_5 ===")
q, t = 5, 5
s, N, b = counts(t, q, 60)
print("N_1..N_8 =", N[1:9]); print("b_1..b_8 =", b[1:9])
print("min N_n (n<=60) =", min(N[1:]), "; min b_d (d<=60) =", min(b[1:]), "; all integers: True (exact)")
al, be = (5 + math.sqrt(5)) / 2, (5 - math.sqrt(5)) / 2
print("alpha, beta = %.6f, %.6f ; alpha*beta = %.6f ; sqrt(q) = %.6f" % (al, be, al * be, math.sqrt(q)))
print("Re s of zeros: log(alpha)/log q = %.5f, log(beta)/log q = %.5f" % (math.log(al) / math.log(q), math.log(be) / math.log(q)))
phi = (1 + math.sqrt(5)) / 2
print("alpha/sqrt5 = %.9f = golden ratio %.9f ; beta/sqrt5 = %.9f = 1/phi" % (al / math.sqrt(5), phi, be / math.sqrt(5)))
print("s_n / 5^(n/2) = phi^n + phi^-n for n=1..8:", [round(s[n] / 5**(n / 2), 6) for n in range(1, 9)])
print("class number h = L(1) =", 1 - t + q, "; divisor counts A_n = (5^n - 1)/4, n=1..5:", [(5**n - 1) // 4 for n in range(1, 6)])
# functional equation: L(u) = q u^2 L(1/(q u))
for u in (0.3, -0.7, 1.9):
    L = lambda x: 1 - t * x + q * x * x
    print("FE residual at u=%.1f: %.2e" % (u, abs(L(u) - q * u * u * L(1 / (q * u)))))

print("\n=== 2. The control E0: y^2 = x^3 + A x + B over F_5 with #E0(F_5) = 2 (trace 4) ===")
p = 5
cands = []
for A, B in itertools.product(range(p), repeat=2):
    if (4 * A**3 + 27 * B**2) % p == 0:
        continue
    n = 1 + sum(1 for x in range(p) for y in range(p) if (y * y - x**3 - A * x - B) % p == 0)
    if p + 1 - n == 4:
        cands.append((A, B))
print("all (A,B) with trace 4:", cands)
A0, B0 = cands[0]
pts = [(x, y) for x in range(p) for y in range(p) if (y * y - x**3 - A0 * x - B0) % p == 0]
print("E0: y^2 = x^3 + %d x + %d ; affine points %s + infinity -> #E0(F_5) = %d" % (A0, B0, pts, len(pts) + 1))

print("\n=== 3. E0 over F_{5^n}, n = 1..4, by brute force in F_{5^n} = F_5[x]/(f) ===")
from sympy import Poly, symbols
X = symbols('X')
def irreducible(n):
    for coeffs in itertools.product(range(p), repeat=n):
        c = [1] + list(coeffs)  # monic, high degree first
        if Poly(c, X, modulus=p).is_irreducible:
            return c
def mulmod(a, b, f):  # a, b: lists low-degree first, length n; f monic high-first
    n = len(f) - 1; r = [0] * (2 * n - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                r[i + j] = (r[i + j] + ai * bj) % p
    low = [(-f[n - k]) % p for k in range(n)]  # X^n = sum low[k] X^k
    for d in range(2 * n - 2, n - 1, -1):
        c = r[d]
        if c:
            r[d] = 0
            for k in range(n):
                r[d - n + k] = (r[d - n + k] + c * low[k]) % p
    return r[:n]
def powmod(a, e, f):
    n = len(f) - 1; res = [1] + [0] * (n - 1); base = a[:]
    while e:
        if e & 1: res = mulmod(res, base, f)
        base = mulmod(base, base, f); e >>= 1
    return res
def count_curve(A, B, n):
    f = irreducible(n) if n > 1 else [1, 0]
    Q = p**n; one = [1] + [0] * (n - 1); zero = [0] * n; tot = 1  # point at infinity
    for xs in itertools.product(range(p), repeat=n):
        x = list(xs)
        fx = mulmod(mulmod(x, x, f), x, f)
        fx = [(fx[k] + A * x[k] + (B if k == 0 else 0)) % p for k in range(n)]
        if fx == zero: tot += 1
        elif powmod(fx, (Q - 1) // 2, f) == one: tot += 2
    return tot
s0 = traces(4, 5, 8)
for n in range(1, 5):
    Nn = count_curve(A0, B0, n)
    pred = 5**n + 1 - s0[n]
    print("n=%d: #E0(F_5^%d) brute force = %d ; 5^n+1-(alpha0^n+beta0^n) with alpha0=2+i: %d ; match: %s" % (n, n, Nn, pred, Nn == pred))
d = 2  # a non-square mod 5
At, Bt = (A0 * d * d) % p, (B0 * d**3) % p
Ntw = count_curve(At, Bt, 1)
print("quadratic twist E0^tw: y^2 = x^3 + %d x + %d ; #E0^tw(F_5) = %d ; N(E0) + N(E0^tw) = %d = 2(q+1) = %d" % (At, Bt, Ntw, count_curve(A0, B0, 1) + Ntw, 2 * (q + 1)))
print("E0: alpha0 = 2 + i, |alpha0|^2 = 5 = q ; Re s of zeros = 1/2 ; class number = #E0(F_5) = L(1) =", 1 - 4 + 5)
