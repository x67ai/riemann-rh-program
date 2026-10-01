#!/usr/bin/env python3
"""Control for NOTE §6: the monoid G_m = {1} ∪ mℕ (not free). Its Dirichlet series Z(s) = 1 + m^{-s} ζ(s) has
N(u) - u/m = 1 + floor(u/m) - u/m ∈ (0, 1] and a real zero in (0, 1); log Z has NEGATIVE coefficients (no Euler product with
nonnegative prime measure). Computes the log coefficients exactly (Dirichlet-series log via L(n) log n = sum_{d|n} ...),
lists the first negative ones, and the real zero of 1 + m^{-s} ζ(s) by mpmath.  Usage: python3 monoid_mN.py > logs/monoid_mN.log"""
from fractions import Fraction as Fr
import mpmath as mp
N = 2000
for m in (2, 3, 5, 10):
    a = [Fr(0)] * (N + 1); a[1] = Fr(1)
    for k in range(m, N + 1, m): a[k] = Fr(1)
    # log of Dirichlet series: n*L... use Lambda-type recursion: a(n) log n = sum_{d|n} Lam(d) a(n/d); L(n) = Lam(n)/log n
    # exact rational version: write log-coefficients c(n) via  sum_{d|n} c(d)*Omega-weight... use the 'derivation' by
    # completely additive f(n) = number of prime factors with multiplicity (any completely additive f works):
    # f·a = (f·c) * a  =>  (f c)(n) = f(n)a(n) - sum_{d|n, d<n} (f c)(d) a(n/d)
    from sympy import factorint
    f = [0] * (N + 1)
    for n in range(2, N + 1): f[n] = sum(factorint(n).values())
    fc = [Fr(0)] * (N + 1)
    for n in range(2, N + 1):
        s = f[n] * a[n]
        d = 1
        divs = [d for d in range(1, n) if n % d == 0]
        for d in divs:
            if fc[d] != 0 and a[n // d] != 0: s -= fc[d] * a[n // d]
        fc[n] = s
    c = [fc[n] / f[n] if n >= 2 else Fr(0) for n in range(N + 1)]
    neg = [(n, c[n]) for n in range(2, N + 1) if c[n] < 0]
    z = mp.findroot(lambda s: 1 + mp.power(m, -s) * mp.zeta(s), 1 - 1.0 / m if m > 2 else 0.5)
    print(f"m={m:2d}: real zero of 1 + m^-s zeta(s) at s = {mp.nstr(z, 10)};  #negative log-coefficients n<={N}: {len(neg)}; first: {[(n, str(v)) for n, v in neg[:4]]}")
