#!/usr/bin/env python3
"""read-O: max |E| for R_tight on [4^N - 3h, 4^N + 6h] (grid of 4000 integer points, plus all cluster primes) for N = 12..16;
E by inclusion-exclusion (as in o_cluster_check.py, whose objects are re-used by import)."""
import sys
sys.argv = ['x', '16']
import numpy as np, mpmath as mp
import o_cluster_check as cc
for N in range(12, 17):
    lo, cl = 4 ** N, cc.clusters[N]; h = cl[-1] - lo; c = len(cl)
    pts = sorted(set([int(x) for x in np.linspace(lo - 3 * h, lo + 6 * h, 4000)] + [r - 1 for r in cl] + cl))
    vals = [(abs(float(cc.E(y))), y) for y in pts]
    m, y = max(vals)
    print(f"N={N} c={c} max|E| on grid = {m:.1f} = {m / c:.3f} c at y = 4^N + {(y - lo) / h:.2f} h")
