#!/usr/bin/env python3
"""t2_values.py — numerical companion to Theorem T2: zeta(rho1/k) != 0 (k = 2..5) and C(rho1/2) != 0 for R = {nextprime(p^2)}."""
import mpmath as mp
from sympy import primerange, nextprime
mp.mp.dps = 25
rho1 = mp.zetazero(1)
for k in (2, 3, 4, 5): print("k=%d  rho1/k = %s   |zeta(rho1/k)| = %s" % (k, mp.nstr(rho1 / k, 12), mp.nstr(abs(mp.zeta(rho1 / k)), 10)))
s0 = rho1 / 2; lr = mp.mpf(0)
for p in primerange(2, 100001): lr += mp.log(1 - mp.power(nextprime(p * p), -s0)) - mp.log(1 - mp.power(p, -2 * s0))
print("C(rho1/2) over p <= 1e5: %s  (|C| = %s); tail: |log C| changes by <= sum_{p>1e5} |s| g_p p^{-2.5} ~ 3e-7 (g_p ~ 23, |s| ~ 7.1); nonvanishing is anyway exact (absolutely convergent product)" % (mp.nstr(mp.e ** lr, 12), mp.nstr(abs(mp.e ** lr), 10)))
print("zeta'(rho1) = %s (simple zero: nonzero)" % mp.nstr(mp.zeta(rho1, derivative=1), 12))
