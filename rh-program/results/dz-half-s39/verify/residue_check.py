#!/usr/bin/env python3
"""residue_check.py — checks the f_C implementation against the printed template (17.39): for k = 1,
log|G(4(1 - rho_1))|^2 (closed form, (17.22)) = -2 int_0^oo a_1(t) cos(gamma_1 t) dt, a_1(t) = g(e^{t/4}) e^{-t/4} / 4,
gamma_1 = e^4, rho_1 = 3/4 + i e^4 (derived in NOTE §4.1 from (17.29)). Also (17.45) on a dense sample of [e^4, 1e8]."""
import math
import numpy as np
from dzcommon import g_of_logu, G_entire, fC, fR, CSTAR
lam, gam = 4.0, math.exp(4.0)
lhs = 2 * math.log(abs(G_entire(lam * (1 - (1 - 1 / lam + 1j * gam)))))
out = []
for h in (4e-4, 2e-4, 1e-4):
    t = np.arange(0, 300 + h / 2, h)
    a = g_of_logu(t / lam) / lam * np.exp(-t / lam)
    out.append((h, -2 * float(np.trapezoid(a * np.cos(gam * t), t))))
print("log|G(4(1-rho_1))|^2 = %.9f" % lhs)
for h, r in out:
    print("  -2 int a_1 cos, step %.0e: %.9f   diff %.2e" % (h, r, r - lhs))
rng = np.random.default_rng(1)
v = np.exp(rng.uniform(4, math.log(1e8), 2_000_000)); r = fC(v) / fR(v)
print("(17.45): f_C/f_R on [e^4, 1e8] in [%.4f, %.4f]; bounds [1-c, 1+c] = [%.4f, %.4f]" % (r.min(), r.max(), 1 - CSTAR, 1 + CSTAR))
