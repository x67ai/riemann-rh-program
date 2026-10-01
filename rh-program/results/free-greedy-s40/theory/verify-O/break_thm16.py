# Opus reader: explicit systems against Theorem 1.6's hypothesis (A) E(u) = N(u) - rho(u-1) - 1 >= -c, c < 1.
# For each: rho, inf of E(u-) on [1, U] (the left limits are where E is smallest), and what Thm 1.6 would need (c < 1 - rho).
import math
from sympy import jacobi_symbol, factorint
def kron(d, n):                      # Kronecker symbol (d/n), d a fundamental discriminant
    r = 1
    for p, e in factorint(n).items():
        if p == 2: k = 0 if d % 2 == 0 else (1 if d % 8 in (1, 7) else -1)
        else: k = jacobi_symbol(d % p, p)
        r *= k ** e
    return r
def ideal_counts(d, U):              # a(n) = sum_{m | n} chi_d(m), n <= U
    chi = [0] + [kron(d, m) for m in range(1, U + 1)]
    a = [0] * (U + 1)
    for m in range(1, U + 1):
        if chi[m]:
            for n in range(m, U + 1, m): a[n] += chi[m]
    return a
def infE(coeffs, rho, U):           # coeffs[n] = number of g-integers equal to n (integer-supported systems)
    N, best, at = coeffs[1], 1e9, None                # u >= 1: the integer 1 counted
    for n in range(2, U + 1):
        e_left = N - rho * (n - 1) - 1          # E(n-), n >= 2
        if e_left < best: best, at = e_left, n
        N += coeffs[n]
    return best, at
U = 20000
odd = [0] + [1 if n % 2 else 0 for n in range(1, U + 1)]
cop6 = [0] + [1 if math.gcd(n, 6) == 1 else 0 for n in range(1, U + 1)]
print("odd integers   rho=1/2   inf E(u-) on [1,%d] = %.4f at %s  (Thm 1.6 needs c < 1/2)" % ((U,) + infE(odd, 0.5, U)))
print("coprime to 6   rho=1/3   inf E(u-) = %.4f at %s  (needs c < 2/3)" % infE(cop6, 1/3, U))
eps = (1 + math.sqrt(5)) / 2; rK = 2 * math.log(eps) / math.sqrt(5)
print("Q(sqrt5)       rho=%.6f inf E(u-) = %.4f at %s  (needs c < %.4f)" % ((rK,) + infE(ideal_counts(5, U), rK, U) + (1 - rK,)))
rK = math.pi / math.sqrt(163)
print("Q(sqrt-163)    rho=%.6f inf E(u-) = %.4f at %s  (needs c < %.4f)" % ((rK,) + infE(ideal_counts(-163, U), rK, U) + (1 - rK,)))
rK = 2 * math.pi * 1 / (6 * math.sqrt(3))   # Q(sqrt-3): h = 1, w = 6, |d| = 3
print("Q(sqrt-3)      rho=%.6f inf E(u-) = %.4f at %s  (needs c < %.4f)" % ((rK,) + infE(ideal_counts(-3, U), rK, U) + (1 - rK,)))
