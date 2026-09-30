#!/usr/bin/env python3
"""Reader-O spot check of NOTE §3.4 (greedy sets) with own code from the CSV bins on disk. Log: logs/greedy_O.log
 ms-slopes (six-bin windows aligned at 1e4) on [1e4, X], [1e6, X], top three decades; sup-slope (fr convention) on [1e4, X];
 kappa0 := fit of log M = a + alpha*log X - kappa0*log ln X with the exponent FIXED at alpha (windows X >= 1e6), i.e. the log-power
 deficit relative to X^alpha; kappaD := fit of log(M/M_diag) = a - kappaD*log ln X with M_diag = rho^2 W(X)/12, W read from the
 writer's rnums tables (data, not code), evaluated at the window start. Errors = OLS standard errors."""
import sys, math
import numpy as np
sys.path.insert(0, sys.path[0]); from seeds_O import parse, sup_slope, ms_windows, ms_slope
HERE = sys.path[0]; FR = HERE + "/../../novel-wave-s37/beurling-frontier/verify/data_big/"; WR = HERE + "/../verify/"
CASES = (("greedy c=1, a=0.60", FR + "greedy_a0.60.csv", WR + "rn/greedy_a0.60_c1.csv", 0.60, 1),
         ("greedy c=1, a=0.75", FR + "greedy_a0.75.csv", WR + "rn/greedy_a0.75_c1.csv", 0.75, 1),
         ("greedy c=2, a=0.60", FR + "greedy_a0.60_c2.csv", WR + "rn/greedy_a0.60_c2.csv", 0.60, 2),
         ("greedy c=2, a=0.75", WR + "data_big/greedy_a0.75_c2.csv", WR + "rn/greedy_a0.75_c2.csv", 0.75, 2))

def ols(x, y):
    A = np.vstack([np.ones_like(x), x]).T; c, res, *_ = np.linalg.lstsq(A, y, rcond=None)
    r = y - A @ c; s2 = r @ r / (len(y) - 2); cov = s2 * np.linalg.inv(A.T @ A); return c[1], math.sqrt(cov[1, 1])

for name, f, rn, alpha, c in CASES:
    (run, (rho, Y, a)), = parse(f).items()
    X = a[-1, 1]; W = ms_windows(a, rho)
    s = [ms_slope(W, w) for w in (1e4, 1e6, X / 1e3)]; sup = sup_slope(a, 1e4, X)
    t = np.loadtxt(rn, delimiter=",", comments="#"); bh, Wd = t[:, 0], t[:, 3]
    m = W[:, 0] >= 1e6; x = W[m, 0]; M = W[m, 1]
    k0, e0 = ols(np.log(np.log(x)), np.log(M) - alpha * np.log(x)); k0 = -k0
    Md = rho ** 2 * np.interp(x, bh, Wd) / 12; kD, eD = ols(np.log(np.log(x)), np.log(M / Md)); kD = -kD
    r0 = W[0, 1] / (rho ** 2 * np.interp(W[0, 0], bh, Wd) / 12)
    print(f"{name}: X={X:.0e} ms [1e4,X]={s[0]:.3f} [1e6,X]={s[1]:.3f} top3={s[2]:.3f} | sup[1e4,X]={sup:.3f} | "
          f"kappa0={k0:.2f}±{e0:.2f} kappaD={kD:.2f}±{eD:.2f} | M/Mdiag {r0:.2f} (1e4) -> {M[-1] / Md[-1]:.2f} (top)")
