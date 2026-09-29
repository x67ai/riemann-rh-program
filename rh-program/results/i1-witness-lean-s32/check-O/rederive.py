# CHECK-O independent re-derivation (Opus 5 checker, written from scratch; does not import or run the builder's code).
import sympy as sp
from fractions import Fraction as Fr
from math import isqrt, log

def divisors(n): return [d for d in range(1, n+1) if n % d == 0]
def vp(p, n):
    e = 0
    while n % p == 0: n //= p; e += 1
    return e
def primes_upto(n): return [p for p in range(2, n+1) if all(p % q for q in range(2, isqrt(p)+1))]

def lamvec(b, N):
    """Solve a_n log n = sum_{d|n} L(d) a_{n/d} with b(1)=1, in the exponent-vector basis.  Returns dict n -> {p: coeff}."""
    L = {1: {}}
    for n in range(2, N+1):
        v = {p: b(n) * vp(p, n) for p in primes_upto(n) if n % p == 0}
        for d in divisors(n):
            if d == n: continue
            for p, c in L[d].items():
                v[p] = v.get(p, 0) - c * b(n // d)
        L[n] = {p: sp.expand(c) if not isinstance(c, (int, Fr)) else c for p, c in v.items()}
    return L

# (a) Davenport-Heilbronn, symbolic kappa
k = sp.Symbol('kappa')
tab = {1: 1, 2: k, 3: -k, 4: -1, 0: 0}
dh = lambda n: tab[n % 5]
L = lamvec(dh, 12)
print("(a) DH array a_1..a_12:", [dh(n) for n in range(1, 13)])
for n in (2, 3, 4, 6, 12):
    print(f"  Lambda_DH({n}) coefficient vector:", {p: sp.factor(c) for p, c in L[n].items()})
c2, c3 = L[12][2], L[12][3]
print("  check c2 == -2k(1+k^2):", sp.simplify(c2 - (-2*k*(1+k**2))) == 0)
print("  check c3 == -k(1+k^2):", sp.simplify(c3 - (-k*(1+k**2))) == 0)
print("  check L(4)_2 == -(2+k^2):", sp.simplify(L[4][2] + 2 + k**2) == 0, " L(6) == (1+k^2,1+k^2):",
      sp.simplify(L[6][2]-(1+k**2)) == 0 and sp.simplify(L[6][3]-(1+k**2)) == 0, " L(3)_3 == -k:", L[3][3] == -k)
# closed form: c2 log2 + c3 log3 = -k(1+k^2)(2 log 2 + log 3) = -k(1+k^2) log 12
# (c) kappa > 0 from the closed form, exactly
s5 = sp.sqrt(5)
kap = (sp.sqrt(10 - 2*s5) - 2)/(s5 - 1)
print("(c) kappa =", sp.N(kap, 40), "; radicand 10-2sqrt5 =", sp.N(10-2*s5, 12),
      "; numerator>0 iff 10-2sqrt5>4 iff sqrt5<3:", sp.N(s5) < 3, "; denominator sqrt5-1 =", sp.N(s5-1, 12))
kv = float(sp.N(kap, 30))
print("  Lambda_DH(12) numeric =", -kv*(1+kv**2)*log(12), "; Lambda_DH(3) =", -kv*log(3), "; Lambda_DH(6) =", (1+kv**2)*log(6))

# (b) Epstein Q = x^2 + 5y^2
def rQ_exact(n):  # all solutions, no box: |x| <= isqrt(n), |y| <= isqrt(n//5)
    return sum(1 for x in range(-isqrt(n), isqrt(n)+1) for y in range(-isqrt(n), isqrt(n)+1) if x*x + 5*y*y == n)
def rQ_box(n):
    return sum(1 for x in range(-n, n+1) for y in range(-n, n+1) if x*x + 5*y*y == n)
print("(b) Epstein counts r_Q(n) at divisors of 36 (exact / box |x|,|y|<=n):")
for d in divisors(36):
    print(f"  n={d}: r_Q={rQ_exact(d)} box={rQ_box(d)} b_n={Fr(rQ_exact(d), 2)}")
print("  box == exact for all n <= 200:", all(rQ_box(n) == rQ_exact(n) for n in range(0, 201)))
eb = lambda n: Fr(rQ_box(n), 2)
LE = lamvec(eb, 100)
print("  Lambda_Q(6) vector:", LE[6], " Lambda_Q(36) vector:", LE[36])
neg = [n for n in range(2, 101) if sum(float(c)*log(p) for p, c in LE[n].items()) < -1e-12]
supp_off = [n for n in range(2, 101) if len(sp.factorint(n)) > 1 and any(c != 0 for c in LE[n].values())]
print("  negative n<=100:", neg, "  support off prime powers n<=100:", supp_off)
# (d) padicValNat as exponent vector: sum_p e_p(n) log p == log n
print("(d) max |sum_p v_p(n) log p - log n| over 1<=n<=10000:",
      max(abs(sum(vp(p, n)*log(p) for p in sp.primefactors(n)) - log(n)) for n in range(1, 10001)))
