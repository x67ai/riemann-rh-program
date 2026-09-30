#!/usr/bin/env python3
"""t3_ratio.py — conj-O-s38 task 3: M(X), the truncated Franel diagonal M_diag(X) = rho^2 W(X)/12 and their ratio, per window
(every third dyadic window printed), for the designs with R-number enumerations. Log: logs/t3_ratio.log"""
import sys, numpy as np; sys.path.insert(0, ".")
from dyadic_ms import load, windows
from t3_analysis import rnums_table, at
FR = "../../novel-wave-s37/beurling-frontier/verify"
CASES = [("greedy c=1 a=0.60", FR + "/data_big/greedy_a0.60.csv", "rn/greedy_a0.60_c1.csv"),
         ("greedy c=1 a=0.75", FR + "/data_big/greedy_a0.75.csv", "rn/greedy_a0.75_c1.csv"),
         ("greedy c=2 a=0.60", FR + "/data_big/greedy_a0.60_c2.csv", "rn/greedy_a0.60_c2.csv"),
         ("greedy c=2 a=0.75", "data_big/greedy_a0.75_c2.csv", "rn/greedy_a0.75_c2.csv")]
for a in ("0.60", "0.75"):
    for s in (1, 2, 3, 4):
        CASES.append(("T_%s seed %d" % (a, s), FR + "/data_big/bern_a%s.csv" % a, "rn/bern_a%s_s%d.csv" % (a, s)))
for lab, csv, rn in CASES:
    runs = load(csv)
    key = [r for r in runs if ("_s%s" % lab.split()[-1]) in r][0] if lab.startswith("T_") else list(runs)[0]
    d = runs[key]; X, Xe, M = windows(d); bh, Q, W = rnums_table(rn)
    Wx = np.array([at(bh, W, x) for x in X]); Qx = np.array([at(bh, Q, x) for x in X]); diag = d["rho"] ** 2 * Wx / 12
    print("%s  [%s] rho=%.4f" % (lab, key, d["rho"]))
    print("   X        " + " ".join("%8.1e" % x for x in X[::3]))
    print("   M        " + " ".join("%8.3g" % m for m in M[::3]))
    print("   Q_R(X)   " + " ".join("%8.3g" % q for q in Qx[::3]))
    print("   M/diag   " + " ".join("%8.3f" % v for v in (M / diag)[::3]))
