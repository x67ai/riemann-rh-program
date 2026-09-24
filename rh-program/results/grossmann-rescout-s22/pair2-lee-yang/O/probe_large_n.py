#!/usr/bin/env python3
"""Scout O -- probe: full-generality search at larger n for one undecided target (env P, A1, A2, S, MS)."""
import os, sys, time, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
import feasibility as F
p, a1, a2, s = (int(os.environ[k]) for k in ("P", "A1", "A2", "S"))
t0 = time.time()
for m in [int(x) for x in os.environ["MS"].split(",")]:
    n = 4 + m
    parts = F.target_parts(p, [1, a1, a2, p * a1, p * p], s, m)
    T = [mp.mpf(X.numerator) / X.denominator + (mp.mpf(Y.numerator) / Y.denominator) / mp.sqrt(p) for X, Y in parts]
    best = F.solve(n, T, int(os.environ.get("TRIES", "6")))
    print("p=%d a1=%d a2=%d s=%d m=%d n=%d best max|log residual| = %.3e  Jmax=%.2f  (%.0fs)"
          % (p, a1, a2, s, m, n, best[0], best[1].max(), time.time() - t0), flush=True)
