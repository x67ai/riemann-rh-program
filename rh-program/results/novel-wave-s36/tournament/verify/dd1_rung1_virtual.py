"""DD1 rung 1: the virtual zeta Z(u) = (1 - a u + q u^2)/((1-u)(1-qu)), (q,a) = (5,5), a > 2 sqrt q.
Checks FE, N_N = 1 + q^N - (alpha^N + beta^N) >= 0 integral, closed-point counts b_d >= 0 integral,
and the zero modulus |u| = 1/alpha != q^{-1/2} (RH false).  Exact integer arithmetic."""
from fractions import Fraction
import math
q, a = 5, 5
# power sums L_N = alpha^N + beta^N via L_N = a L_{N-1} - q L_{N-2}
L = [2, a]
for N in range(2, 41):
    L.append(a * L[-1] - q * L[-2])
NN = [None] + [1 + q**N - L[N] for N in range(1, 41)]
def mobius(n):
    m, p, res = n, 2, 1
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0: return 0
            res = -res
        p += 1
    return -res if m > 1 else res
b = [None]
for d in range(1, 41):
    s = sum(mobius(d // e) * NN[e] for e in range(1, d + 1) if d % e == 0)
    b.append(Fraction(s, d))
alpha = (a + math.sqrt(a * a - 4 * q)) / 2
print("N_N, N=1..10:", NN[1:11])
print("min N_N (N<=40):", min(NN[1:]), " all integral: True (integer recursion)")
print("b_d, d=1..10:", [str(x) for x in b[1:11]])
print("all b_d (d<=40) nonnegative integers:", all(x.denominator == 1 and x >= 0 for x in b[1:]))
print(f"alpha = {alpha:.6f}, sqrt(q) = {math.sqrt(q):.6f}; zeros of 1 - a u + q u^2 at |u| = 1/alpha = {1/alpha:.6f} and 1/beta = {alpha/q:.6f}; RH needs {1/math.sqrt(q):.6f}")
print("sigma of zeros (u = q^-s):", math.log(alpha) / math.log(q), 1 - math.log(alpha) / math.log(q))
# FE: P(u) = q u^2 P(1/(q u)) for the numerator
import random
for _ in range(3):
    u = complex(random.uniform(-1, 1), random.uniform(-1, 1))
    P = lambda x: 1 - a * x + q * x * x
    print("FE residual:", abs(P(u) - q * u * u * P(1 / (q * u))))
