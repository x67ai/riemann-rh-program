# read-O: the virtual curve V over F_5, Z(u) = (1 - 5u + 5u^2)/((1 - u)(1 - 5u)), u = 5^{-s}. Exact integers.
# (1) A_n by exact power-series division; A_n - 5^n/4 (as a Fraction);  (2) closed-point counts b_d by Moebius from
# a_n := n * [u^n] log Z = 5^n + 1 - (w1^n + w2^n), w1 + w2 = 5, w1 w2 = 5 (Newton/Lucas recursion, exact);
# (3) zeros of Z in s; (4) sign of Z(5^{-sigma}) on (0, 1).
from fractions import Fraction
from mpmath import mp, mpf, sqrt, log
mp.dps = 30
N = 40
num = [1, -5, 5] + [0]*N
den = [1, -6, 5] + [0]*N                  # (1 - u)(1 - 5u) = 1 - 6u + 5u^2
A = []
for n in range(N):                         # A = num / den, exact
    s = num[n] - sum(den[j]*A[n - j] for j in range(1, min(n, 2) + 1))
    A.append(s)                            # den[0] = 1
ok = all(A[n] == (5**n - 1)//4 and (5**n - 1) % 4 == 0 for n in range(1, N))
print("A_0..A_8:", A[:9], "  A_n == (5^n - 1)/4 for 1 <= n < 40:", ok)
print("A_n - 5^n/4 for n = 1..6:", [str(Fraction(A[n]) - Fraction(5**n, 4)) for n in range(1, 7)])
# power sums p_n = w1^n + w2^n: p_0 = 2, p_1 = 5, p_n = 5 p_{n-1} - 5 p_{n-2}
p = [2, 5]
for n in range(2, N + 1): p.append(5*p[-1] - 5*p[-2])
a = [None] + [5**n + 1 - p[n] for n in range(1, N + 1)]
def mob(n):
    r, q = 1, 2
    while q*q <= n:
        if n % q == 0:
            n //= q
            if n % q == 0: return 0
            r = -r
        q += 1
    return -r if n > 1 else r
b = {}
for d in range(1, N + 1):
    s = sum(mob(d//j)*a[j] for j in range(1, d + 1) if d % j == 0)
    assert s % d == 0
    b[d] = s//d
print("b_1..b_8:", [b[d] for d in range(1, 9)], "  all b_d >= 0 for d <= 40:", all(b[d] >= 0 for d in b))
# cross-check: prod_d (1 - u^d)^{-b_d} reproduces A_n up to n = 20 (exact)
M = 21
ser = [1] + [0]*(M - 1)
for d in range(1, M):
    for _ in range(b[d]) if False else [0]:
        pass
    # multiply by (1 - u^d)^{-b_d} = sum_j C(b_d + j - 1, j) u^{dj}
    from math import comb
    new = [0]*M
    for i in range(M):
        if ser[i] == 0: continue
        j = 0
        while i + d*j < M:
            new[i + d*j] += ser[i]*comb(b[d] + j - 1, j); j += 1
    ser = new
print("Euler product reproduces A_n for n < 21:", ser == A[:M])
u1, u2 = (5 - sqrt(5))/10, (5 + sqrt(5))/10
print("zeros: Re s =", mp.nstr(-log(u1)/log(5), 20), "and", mp.nstr(-log(u2)/log(5), 20))
Z = lambda sg: (1 - 5*mpf(5)**-sg + 5*mpf(5)**(-2*sg))/((1 - mpf(5)**-sg)*(1 - 5*mpf(5)**-sg))
print("Z(5^-sigma) at sigma = 0.5, 0.7, 0.79, 0.81, 0.9, 0.999:", [mp.nstr(Z(mpf(x)), 6) for x in ('0.5', '0.7', '0.79', '0.81', '0.9', '0.999')])
