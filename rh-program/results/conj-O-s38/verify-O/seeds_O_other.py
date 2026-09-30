#!/usr/bin/env python3
"""Reader-O: alpha = 0.60 and 0.90 (fr seeds 1-4 at 1e10) with seeds_O's own estimators. Log: logs/seeds_O_other.log"""
import sys; sys.path.insert(0, sys.path[0])
from seeds_O import parse, sup_slope, ms_windows, ms_slope, stat, FR
for al in ("0.60", "0.90"):
    runs = parse(FR + f"data_big/bern_a{al}.csv"); S = []; M = []
    for r, (rho, Y, a) in runs.items():
        W = ms_windows(a, rho); S.append([sup_slope(a, w, 1e10) for w in (1e4, 1e6, 1e7)]); M.append([ms_slope(W, w) for w in (1e4, 1e6, 1e7)])
    print(f"alpha={al} sup: " + "  ".join(stat([s[i] for s in S]) for i in range(3)) + " | ms: " + "  ".join(stat([m[i] for m in M]) for i in range(3)))
