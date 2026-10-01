#!/usr/bin/env python3
"""Rank 2: check F_(n,n) = -1/2 * int_{-1}^{1-2tau} ((1+t)/2)^(n-1) P_n(t) dt (exact, sympy), where F = log(1 - tau + tau/((1-x)(1-y))),
and list the sign of F_(n,n) for n <= 60 (exact rationals) for several tau.  Usage: python3 rank2_legendre.py > logs/rank2_legendre.log"""
import sympy as sp
from fractions import Fraction as Fr
import itertools
t = sp.symbols('t')

def F_nn_direct(tau, N):
    # mixed part of log(1 - s(x+y) + s x y), s = 1 - tau: coefficient of x^n y^n
    s = 1 - tau
    out = {}
    for n in range(1, N + 1):
        a = b = n
        tot = Fr(0)
        for k in range(0, n + 1):
            j = a + b - k
            # -(1/j) s^j * multinomial(j; a-k, b-k, k) * (-1)^k
            mult = sp.factorial(j) / (sp.factorial(a - k) * sp.factorial(b - k) * sp.factorial(k))
            tot += -Fr(int(mult)) * Fr((-1) ** k) * s ** j / j
        out[n] = tot
    return out

def F_nn_legendre(tau, n):
    c = 1 - 2 * sp.Rational(tau.numerator, tau.denominator)
    expr = ((1 + t) / 2) ** (n - 1) * sp.legendre(n, t)
    return -sp.Rational(1, 2) * sp.integrate(sp.expand(expr), (t, -1, c))

for tau in (Fr(1, 20), Fr(1, 10), Fr(1, 4), Fr(1, 2), Fr(9, 10)):
    d = F_nn_direct(tau, 60)
    ok = all(sp.Rational(d[n].numerator, d[n].denominator) == F_nn_legendre(tau, n) for n in (1, 2, 3, 5, 8, 13))
    signs = ''.join('+' if d[n] > 0 else ('-' if d[n] < 0 else '0') for n in range(1, 61))
    print(f"tau={str(tau):5s} legendre_formula_ok(n in 1,2,3,5,8,13)={ok}  signs n=1..60: {signs}")
