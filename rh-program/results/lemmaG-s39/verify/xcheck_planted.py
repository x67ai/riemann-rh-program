#!/usr/bin/env python3
"""xcheck_planted.py — second route for lg.c 'planted' mode at X = 1e5: Python greedy with the same weights; R-lists compared;
bins recomputed by inclusion-exclusion (as xcheck_small.py)."""
import math, subprocess, numpy as np
from sympy import primerange
a, c, s1, g1, A, X, Y = 0.6, 1.0, 0.45, 5.0, 1.0, 100000, 400000
out = subprocess.run(["./lg", "planted", str(a), str(c), str(s1), str(g1), str(A), "1e5", "4e5"], capture_output=True, text=True).stdout.splitlines()
head = [l for l in out if l.startswith("#")][0]; print(head)
rho = float(head.split(" rho=")[1].split()[0]); run = head.split("run=")[1].split()[0]
R = [int(l) for l in open("data/R_%s.txt" % run)]
F, cnt, Rpy = 0.0, 0, []
for p in primerange(2, Y + 1):
    lp = math.log(p); w = c * math.exp((a - 1) * lp) - 2 * A * math.exp((s1 - 1) * lp) * math.cos(g1 * lp); w = min(1.0, max(0.0, w))
    F += w
    if cnt < F:
        cnt += 1
        if p <= X: Rpy.append(p)
print("R-lists equal:", R == Rpy, len(R))
N = np.zeros(X + 1, dtype=np.int64); Rs = sorted(R); ms = [(1, 1)]
def rec(i, b, mu):
    for j in range(i, len(Rs)):
        if b * Rs[j] > X: break
        ms.append((b * Rs[j], -mu)); rec(j + 1, b * Rs[j], -mu)
rec(0, 1, 1)
n = np.arange(X + 1)
for m, mu in ms: N += mu * (n // m)
worst = 0
for l in out:
    if l.startswith("#"): continue
    b = l.split(","); lo, hi, s2 = int(b[1]), int(b[2]), float(b[5])
    k = np.arange(lo, hi + 1); ec = N[lo:hi + 1] - rho * (k + 0.5); worst = max(worst, abs(float((ec * ec).sum()) - s2) / max(1, abs(s2)))
print("max rel diff sumE2 (sieve vs inclusion-exclusion): %.2e ; #R-numbers <= X: %d" % (worst, len(ms)))
