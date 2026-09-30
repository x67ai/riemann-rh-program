#!/usr/bin/env python3
"""Reader-O spot check of NOTE §3.5 (online error-feedback design) from the writer's CSV bins + rnums tables (data only).
Log: logs/feedback_O.log. Prints ms-slopes and M/M_diag at a few X for the `corr` runs quoted in the NOTE."""
import sys, numpy as np
sys.path.insert(0, sys.path[0]); from seeds_O import parse, ms_windows, ms_slope, sup_slope
WR = sys.path[0] + "/../verify/"
for tag, f in (("corr a=0.75 K=2 1e9", "data/feedback_a0.75_c1_K2_corr_1e9.csv"), ("corr a=0.75 K=2 1e10", "data_big/feedback_a0.75_c1_K2_corr_1e10.csv"),
               ("corr a=0.75 K=0.5 1e10", "data_big/feedback_a0.75_c1_K0.5_corr_1e10.csv"), ("plain a=0.75 c=1 K=2 1e10", "data_big/feedback_a0.75_c1_K2_1e10.csv"),
               ("plain a=0.60 c=1 K=0.5 1e9", "data/feedback_a0.60_c1_K0.5_1e9.csv")):
    (run, (rho, Y, a)), = parse(WR + f).items(); X = a[-1, 1]; W = ms_windows(a, rho)
    t = np.loadtxt(WR + "rn/" + f.split("/")[1], delimiter=",", comments="#"); Md = rho ** 2 * np.interp(W[:, 0], t[:, 0], t[:, 3]) / 12
    r = W[:, 1] / Md; pick = [np.argmin(np.abs(W[:, 0] - x)) for x in (1e4, 6e5, 1e7, 1.6e8, 6e8, 2.5e9) if x < X]
    print(f"{tag:<28} ms[1e4,X]={ms_slope(W, 1e4):.3f} ms[1e7,X]={ms_slope(W, 1e7):.3f} sup[1e4,X]={sup_slope(a, 1e4, X):.3f} | M/Mdiag at "
          + ", ".join(f"{W[i, 0]:.1e}:{r[i]:.3f}" for i in pick) + f" | min {r.min():.3f} at {W[np.argmin(r), 0]:.1e}")
