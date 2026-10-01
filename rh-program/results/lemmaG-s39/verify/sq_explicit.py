#!/usr/bin/env python3
"""sq_explicit.py — second route for the prime-square mimic R = {nextprime(p^2)} (Theorem T2's mechanism). Under RH, Mellin inversion of
zeta_P(s) x^s / s with zeta_P = zeta(s) C(s) / zeta(2s) gives E(x) = sum_rho c_rho x^{rho/2} + O(1) + O(x^{0.03}),
c_rho = zeta(rho/2) C(rho/2) / (rho zeta'(rho)),  C(s) = prod_p (1 - r_p^{-s}) / (1 - p^{-2s}).
Each lg bin [lo, hi] carries sum of E at midpoints; its mean is compared with the exact bin average of the explicit sum
(int_lo^hi x^{rho/2} dx / (hi - lo)), over the first NZ zeros (zeros from mpmath.zetazero). Output: correlation, rms ratio, table."""
import sys, math
import numpy as np, mpmath as mp
mp.mp.dps = 20
NZ = int(sys.argv[1]) if len(sys.argv) > 1 else 60
R = [int(l) for l in open("data/R_sq_k2_1e+10.txt")]
from sympy import primerange
P = list(primerange(2, 100001)); assert len(R) == len(P) and all(r > p * p for r, p in zip(sorted(R), P))
Rs = sorted(R)
def C(s):
    lr = mp.mpf(0)
    for p, r in zip(P, Rs): lr += mp.log(1 - mp.power(r, -s)) - mp.log(1 - mp.power(p, -2 * s))
    return mp.e ** lr
coef = []
for n in range(1, NZ + 1):
    rho = mp.zetazero(n); s0 = rho / 2
    c = mp.zeta(s0) * C(s0) / (rho * mp.zeta(rho, derivative=1)); coef.append((complex(rho), complex(c)))
    if n <= 6: print("zero %d: rho=%s  |c_rho|=%.4e  c_rho=%s" % (n, mp.nstr(rho, 10), abs(complex(c)), mp.nstr(c, 6)))
bins = [l.strip().split(",") for l in open("data/sq2_1e10.sume")]
lo = np.array([float(b[0]) for b in bins]); hi = np.array([float(b[1]) for b in bins]); s1 = np.array([float(b[2]) for b in bins])
cnt = hi - lo + 1; meanE = s1 / cnt
pred = np.zeros_like(meanE)
for rho, c in coef:
    a = rho / 2 + 1
    avg = (np.power(hi + 1, a) - np.power(lo, a)) / (a * cnt)     # (1/(hi+1-lo)) int_lo^{hi+1} x^{rho/2} dx
    pred += 2 * (c * avg).real
m = lo >= 1e4
x = np.sqrt(lo * (hi + 1))
num = meanE[m] / x[m] ** 0.25; prd = pred[m] / x[m] ** 0.25
corr = np.corrcoef(num, prd)[0, 1]; resid = num - prd
print("bins with lo >= 1e4: %d ; corr(measured, predicted) of E/x^(1/4) = %.4f ; rms(measured) = %.4f ; rms(resid) = %.4f" % (m.sum(), corr, np.sqrt((num ** 2).mean()), np.sqrt((resid ** 2).mean())))
for cut in (1e6, 1e8):
    mm = lo >= cut; a_ = meanE[mm] / x[mm] ** 0.25; b_ = pred[mm] / x[mm] ** 0.25
    print("   lo >= %.0e: %d bins, corr = %.4f, rms(measured) = %.4f, rms(resid) = %.4f" % (cut, mm.sum(), np.corrcoef(a_, b_)[0, 1], np.sqrt((a_ ** 2).mean()), np.sqrt(((a_ - b_) ** 2).mean())))
for i in np.where(m)[0][::12]:
    print("   x=%.2e  E/x^0.25 measured % .4f  predicted % .4f" % (x[i], meanE[i] / x[i] ** 0.25, pred[i] / x[i] ** 0.25))
