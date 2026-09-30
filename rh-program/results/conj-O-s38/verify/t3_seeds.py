#!/usr/bin/env python3
"""t3_seeds.py — conj-O-s38 task 3: T_0.75 at X = 1e10, seeds 1-4 (fr data_big) + 5-12 (this unit, thin_fr.c): the running-sup
slope (fr fit.py convention) and the dyadic mean-square slope side by side, per seed and mean +- s.e. Log: logs/t3_seeds.log"""
import sys, glob, math, numpy as np
sys.path.insert(0, ".")
from dyadic_ms import load, windows, slope, sup_slope
FR = "../../novel-wave-s37/beurling-frontier/verify"
W = [1e4, 1e6, 1e7]
def table(files, alpha):
    rows = []
    for f in files:
        for r, d in load(f).items():
            X, Xe, M = windows(d)
            rows.append((int(r.split("_s")[1]),) + tuple(sup_slope(d, w) for w in W) + tuple(slope(X, M, w) for w in W))
    rows.sort()
    print("alpha=%.2f  (alpha/2 = %.3f, 1/(3-alpha) = %.3f; ms target alpha = %.3f, random-R ref slope of X^a/lnX on [1e4,1e10] = %.3f)"
          % (alpha, alpha / 2, 1 / (3 - alpha), alpha, alpha - 1 / math.log(10 ** 7)))
    print("seed  sup[1e4]  sup[1e6]  sup[1e7] |  ms[1e4]  ms[1e6]  ms[1e7]")
    for r in rows: print("%4d  " % r[0] + "  ".join("%7.3f" % v for v in r[1:4]) + " | " + "  ".join("%7.3f" % v for v in r[4:]))
    a = np.array([r[1:] for r in rows])
    for lab, sel in (("seeds 1-4", a[[i for i, r in enumerate(rows) if r[0] <= 4]]), ("seeds 5-12", a[[i for i, r in enumerate(rows) if r[0] > 4]]), ("all", a)):
        if len(sel) < 2: continue
        m, se = sel.mean(0), sel.std(0, ddof=1) / math.sqrt(len(sel))
        print("%-11s" % lab + "  ".join("%.3f±%.3f" % (x, y) for x, y in zip(m, se)) + "   (n=%d)" % len(sel))
table([FR + "/data_big/bern_a0.75.csv"] + sorted(glob.glob("data_big/bern_a0.75_s*.csv")), 0.75)
table([FR + "/data_big/bern_a0.60.csv"], 0.60)
table([FR + "/data_big/bern_a0.90.csv"], 0.90)
