#!/usr/bin/env python3
"""t3_rung1.py — ladder rung 1 (finite R): the dyadic mean-square code must reproduce fr Prop. 5.1, rho 2^|R| / 12.
Inputs: data/finite_*.csv from `thin2 finite 1e8 ...` (header carries the exact one-period mean square in long double).
Log: logs/t3_rung1.log"""
import sys, re; sys.path.insert(0, ".")
from dyadic_ms import load, windows
for f in ["data/finite_2-13_1e8.csv", "data/finite_3-19_1e8.csv"]:
    for r, d in load(f).items():
        pred = float(re.search(r"pred_rho_2k_over_12=([0-9.]+)", d["meta"]).group(1))
        per = float(re.search(r"period_ms=([0-9.]+)", d["meta"]).group(1)); Q = int(re.search(r"Q=(\d+)", d["meta"]).group(1))
        X, Xe, M = windows(d)
        print("%s  Q=%d  rho*2^|R|/12=%.12f  exact one-period mean square=%.12f  rel=%.1e" % (r, Q, pred, per, per / pred - 1))
        for x, m in list(zip(X, M))[::3] + [(X[-1], M[-1])]:
            print("   dyadic window X=%.3g  M(X)=%.8f  M/pred-1=%+.2e  (Q/X=%.1e)" % (x, m, m / pred - 1, Q / x))
