#!/usr/bin/env python3
"""nsq_bessel.py — test of Theorem T3's predicted law for R = {nextprime(n^2)} (pole of P_R at alpha_R = 1/2, residue a = 1/2):
D_R ~ exp(-a/(s - 1/2)) B(s) near 1/2, so Mellin inversion gives E(x) ~ x^{1/2} [K1 f1(L) + K2 f1'(L)], L = ln x,
f1(L) = J1(2 sqrt(a L)) / sqrt(L)  (the frequency 2 sqrt(a L) = sqrt(2L) is fixed by the residue; K1, K2 are fitted).
Data: lg bin sums of E (LG_SUME side file). Control: the same fit with the frequency multiplied by w (w = 0.7 ... 1.3); the predicted
w = 1 should be the best."""
import numpy as np
from scipy.special import j1
b = np.loadtxt("data/nsq2_1e10.sume", delimiter=",")
lo, hi, s1 = b[:, 0], b[:, 1], b[:, 2]; cnt = hi - lo + 1; x = np.sqrt(lo * (hi + 1)); m = lo >= 1e4
y = (s1 / cnt)[m] / np.sqrt(x[m]); L = np.log(x[m])
def fit(w):
    f1 = j1(w * np.sqrt(2 * L)) / np.sqrt(L)
    h = 1e-4; f1p = (j1(w * np.sqrt(2 * (L + h))) / np.sqrt(L + h) - j1(w * np.sqrt(2 * (L - h))) / np.sqrt(L - h)) / (2 * h)
    A = np.vstack([f1, f1p]).T; k, *_ = np.linalg.lstsq(A, y, rcond=None); r = y - A @ k
    return k, 1 - (r ** 2).sum() / ((y - y.mean()) ** 2).sum(), A @ k
print("bins: %d (x from %.1e to %.1e); rms of E/x^(1/2) = %.4f" % (m.sum(), x[m].min(), x[m].max(), np.sqrt((y ** 2).mean())))
for w in (0.7, 0.8, 0.9, 0.95, 1.0, 1.05, 1.1, 1.2, 1.3):
    k, R2, _ = fit(w); print("  frequency factor w = %.2f : K1 = % .4f  K2 = % .4f  R^2 = %.4f" % (w, k[0], k[1], R2))
k, R2, yy = fit(1.0)
print("predicted (w = 1) vs measured E/x^(1/2) at sample bins:")
for i in range(0, m.sum(), 15): print("   x=%.2e  measured % .5f  fit % .5f" % (x[m][i], y[i], yy[i]))
