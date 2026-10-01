# curveV_check.py — re-derivation of the orchestrator's rung-1 control (SHARED 17:30):
# Z(u) = (1 - 5u + 5u^2)/((1 - u)(1 - 5u)); A_n = coefficient of u^n; N_n = 1 + 5^n - a^n - b^n (a, b roots of X^2 - 5X + 5);
# closed-point counts b_d from N_n = sum_{d|n} d b_d (Moebius); zeros u = (5 -+ sqrt5)/10, s = -log u / log 5.
from fractions import Fraction
import math
M = 16
A = [0]*(M + 1); geo = [(5**(n + 1) - 1)//4 for n in range(M + 1)]     # coefficients of 1/((1-u)(1-5u))
for n in range(M + 1):
    A[n] = geo[n] - (5*geo[n - 1] if n >= 1 else 0) + (5*geo[n - 2] if n >= 2 else 0)
print("A_n:", A[:8], " check A_n == (5^n-1)/4 for n>=1:", all(A[n] == (5**n - 1)//4 for n in range(1, M + 1)),
      " A_n - 5^n/4 = -1/4 for n>=1")
# power sums of roots of X^2 - 5X + 5: p_n = 5 p_{n-1} - 5 p_{n-2}, p_0 = 2, p_1 = 5
p = [2, 5]
for n in range(2, M + 1): p.append(5*p[-1] - 5*p[-2])
Nn = [None] + [1 + 5**n - p[n] for n in range(1, M + 1)]
def mob(n):
    r, q = 1, 2
    while q*q <= n:
        if n % q == 0:
            n //= q
            if n % q == 0: return 0
            r = -r
        q += 1
    return -r if n > 1 else r
bd = [None] + [sum(mob(n//d)*Nn[d] for d in range(1, n + 1) if n % d == 0)//n for n in range(1, M + 1)]
ok = all(sum(mob(n//d)*Nn[d] for d in range(1, n + 1) if n % d == 0) % n == 0 for n in range(1, M + 1))
print("N_n:", Nn[1:7], " b_d:", bd[1:9], " integral:", ok, " all b_d >= 0:", all(b >= 0 for b in bd[1:]))
for u in ((5 - math.sqrt(5))/10, (5 + math.sqrt(5))/10):
    print(f"zero u = {u:.6f}: s = {-math.log(u)/math.log(5):.5f} (+ 2 pi i k / log 5)")
