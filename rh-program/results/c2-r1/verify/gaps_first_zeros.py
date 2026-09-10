#!/usr/bin/env python3
"""gaps_first_zeros.py -- Theorem G's computational range: consecutive gaps of the first zeros of zeta (mpmath.zetazero).

Theorem G (confinement-note.md section 3) needs every gap gamma_{n+1} - gamma_n <= 7.5 for gamma_n <= 2400 (the analytic
ranges start at T = 2303 via HSW (5.6) and at T = 2273 via TRU (2.5) with |S| <= 2); N(2400) ~ 1880.
This script computes gamma_1 .. gamma_M with M = 1900 (time guard 9 minutes), prints the ten largest gaps and the first ten zeros.
"""
import json, sys, time
import mpmath as mp
import numpy as np

t0 = time.time()
mp.mp.dps = 15
M = 1900
zs = []
for n in range(1, M + 1):
    zs.append(float(mp.zetazero(n).imag))
    if time.time() - t0 > 540:
        print(f"time guard at n = {n}"); break
zs = np.array(zs)
gaps = np.diff(zs)
order = np.argsort(gaps)[::-1][:10]
print(f"computed gamma_1..gamma_{len(zs)} in {time.time()-t0:.0f}s; gamma_{len(zs)} = {zs[-1]:.4f}")
print("first ten zeros:", [round(z, 4) for z in zs[:10]])
print("first ten gaps: ", [round(g, 4) for g in gaps[:10]])
print("ten largest gaps (n, gamma_n, gap):", [(int(i) + 1, round(zs[i], 3), round(gaps[i], 4)) for i in order])
print(f"max gap = {gaps.max():.4f} at n = {int(np.argmax(gaps))+1};  all gaps <= 7.5: {bool(np.all(gaps <= 7.5))};  all gaps <= 6.9: {bool(np.all(gaps <= 6.9))}")
out = dict(M=int(len(zs)), gamma_last=float(zs[-1]), first_ten=[float(z) for z in zs[:10]], max_gap=float(gaps.max()), argmax_n=int(np.argmax(gaps)) + 1,
           all_le_7_5=bool(np.all(gaps <= 7.5)), largest_gaps=[(int(i) + 1, float(zs[i]), float(gaps[i])) for i in order], runtime_s=time.time() - t0)
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "gaps_first_zeros_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
