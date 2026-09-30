# Orchestrator's independent re-run of N4's decisive computations (Session 37, read-F): deep dive DD1.
# (1) Epstein zeta of x^2 + 5y^2 (class number 2): Lambda_F(n) from a(n) log n = sum_{d|n} Lambda_F(d) a(n/d); first negative n.
# (2) the virtual curve Z(u) = (1 - 5u + 5u^2)/((1-u)(1-5u)) over F_5: point counts, closed-point counts (exact integers), zeros.
# (3) F_{a,q}: Lambda_F(q^2)/log q = 1 - a^2 + 2q.      Exact/rational arithmetic where possible.
import math
from fractions import Fraction
def epstein_coeffs(A, B, C, nmax):
    # a(n) = r_Q(n)/2 for Q = A x^2 + B x y + C y^2 (positive definite), normalized so that a(1) = 1 when Q represents 1 twice
    r = [0]*(nmax+1)
    lim = int(math.isqrt(4*nmax)) + 2
    for x in range(-lim, lim+1):
        for y in range(-lim, lim+1):
            v = A*x*x + B*x*y + C*y*y
            if 0 < v <= nmax: r[v] += 1
    return [Fraction(c, r[1]) for c in r]
def lam_coeffs(a, nmax):
    # returns L(n) with Lambda_F(n) = L(n) (as a dict of rational multiples of log d collected numerically)
    lam = [0.0]*(nmax+1)
    for n in range(2, nmax+1):
        s = float(a[n])*math.log(n)
        for d in range(2, n):
            if n % d == 0: s -= lam[d]*float(a[n//d])
        lam[n] = s            # a(1) = 1
    return lam
for (A, B, C, name) in [(1, 0, 1, "x^2+y^2 (h=1, Euler product)"), (1, 0, 5, "x^2+5y^2 (h=2)")]:
    a = epstein_coeffs(A, B, C, 400)
    lam = lam_coeffs(a, 400)
    neg = [(n, lam[n]) for n in range(2, 401) if lam[n] < -1e-9]
    print(name, ": first negative Lambda:", neg[:3], " count<=400:", len(neg))
    if neg: print("   Lambda(36)/log 36 =", lam[36]/math.log(36))
# (2) virtual curve: N_n = 1 + 5^n - (alpha^n + beta^n), alpha, beta roots of x^2 - 5x + 5  (power sums by recurrence, exact)
p = [2, 5]
for n in range(2, 61): p.append(5*p[-1] - 5*p[-2])
N = [None] + [1 + 5**n - p[n] for n in range(1, 61)]
def mobius(n):
    res, m, d = 1, n, 2
    while d*d <= m:
        if m % d == 0:
            m //= d
            if m % d == 0: return 0
            res = -res
        d += 1
    if m > 1: res = -res
    return res
b = [None]
for d in range(1, 61):
    tot = sum(mobius(d//e)*N[e] for e in range(1, d+1) if d % e == 0)
    assert tot % d == 0, d
    b.append(tot//d)
print("virtual curve: N_1..N_6 =", N[1:7], " b_1..b_6 =", b[1:7])
print("   all N_n >= 1 and all b_d >= 0 integers for d <= 60:", all(x >= 1 for x in N[1:]), all(x >= 0 for x in b[1:]))
alpha = (5 + math.sqrt(5))/2
print("   alpha =", alpha, " > sqrt 5 =", math.sqrt(5), " ; zero at sigma = log alpha/log 5 =", math.log(alpha)/math.log(5),
      " and", 1 - math.log(alpha)/math.log(5))
# functional equation of the numerator: L(u) = 1 - 5u + 5u^2,  L(1/(5u)) = L(u)/(5u^2)
u = 0.137 + 0.2j
L = lambda u: 1 - 5*u + 5*u*u
print("   FE residual |L(1/(5u)) - L(u)/(5u^2)| =", abs(L(1/(5*u)) - L(u)/(5*u*u)))
# (3) F_{a,q}
for (a, q) in [(2.9, 2), (5, 5), (3, 2)]:
    print("F_{%s,%s}: Lambda(q^2)/log q = 1 - a^2 + 2q = %s  (a > 2 sqrt q = %.4f: %s)" % (a, q, 1 - a*a + 2*q, 2*math.sqrt(q), a > 2*math.sqrt(q)))
