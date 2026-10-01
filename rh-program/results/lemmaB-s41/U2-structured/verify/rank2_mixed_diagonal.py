#!/usr/bin/env python3
"""NOTE Theorem 2.1(ii) check: m_n = [z^n] log[(1 - 2sz + s z^2)/(1 - sz)^2] (s = 1 - tau) equals sum_{a+b=n, a,b>=1} F_(a,b)
for F = log(1 - tau + tau/((1-x)(1-y))), and has negative entries; first negative n listed. Exact rationals.
Usage: python3 rank2_mixed_diagonal.py > logs/rank2_mixed_diagonal.log"""
from fractions import Fraction as Fr
import itertools
from rank_cumulants import series_log, multivariate_first_negative
def mixed_diag(tau, N):
    s = 1 - tau
    num = [Fr(1), -2 * s, s] + [Fr(0)] * (N - 2)
    den = [Fr(0)] * (N + 1)
    for k in range(N + 1):                     # (1 - s z)^2 coefficients
        den[k] = Fr([1, -2, 1][k]) * s**k if k <= 2 else Fr(0)
    Ln, Ld = series_log(num[:N + 1], N), series_log(den, N)
    return [Ln[n] - Ld[n] for n in range(N + 1)]
def mixed_sum_direct(tau, n):
    s = 1 - tau; tot = Fr(0)
    from math import factorial
    for a in range(1, n):
        b = n - a
        for k in range(0, min(a, b) + 1):
            j = a + b - k
            mult = factorial(j) // (factorial(a - k) * factorial(b - k) * factorial(k))
            tot += -Fr(mult) * (-1) ** k * s**j / j
    return tot
for tau in (Fr(1, 20), Fr(1, 10), Fr(1, 4), Fr(1, 2), Fr(9, 10)):
    m = mixed_diag(tau, 60)
    agree = all(m[n] == mixed_sum_direct(tau, n) for n in range(2, 25))
    negs = [n for n in range(2, 61) if m[n] < 0]
    print(f"tau={str(tau):5s} diag-sum identity (n<=24)={agree}  first negative m_n: n={negs[0] if negs else None}  #neg(n<=60)={len(negs)}")
