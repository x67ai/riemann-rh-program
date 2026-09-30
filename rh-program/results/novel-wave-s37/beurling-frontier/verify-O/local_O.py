#!/usr/bin/env python3
"""local_O.py — local (per-decade) exponents: for each decade (10^(k-1), 10^k], the slope over bins in the two adjacent
decades (10^(k-2), 10^k] of the seed-mean of log10(per-bin RMS) (RMS column), with a bootstrap-over-seeds error.
Works on reader-O CSVs (8 cols, RMS in col 7) and writer CSVs (8 cols: sumE2/count in cols 6/7)."""
import sys, numpy as np
rng = np.random.default_rng(7)
for path in sys.argv[1:]:
    runs = {}
    for line in open(path):
        if line.startswith('#') or not line.strip(): continue
        f = line.strip().split(',')
        lo, hi = float(f[1]), float(f[2])
        if hi - lo < 1: continue
        rms = float(f[6]) if 'bernO' in f[0] else (float(f[5]) / float(f[6])) ** 0.5
        runs.setdefault(f[0], []).append((hi, rms))
    names = sorted(runs); H = np.array([h for h, _ in runs[names[0]]])
    L = np.log10(np.array([[r for _, r in runs[n]] for n in names]))
    out = []
    for k in range(4, int(round(np.log10(H.max()))) + 1):
        m = (H > 10 ** (k - 2)) & (H <= 10 ** k * 1.001)
        f = lambda A: np.polyfit(np.log10(H[m]), A[:, m].mean(axis=0), 1)[0]
        b = [f(L[rng.integers(0, len(names), len(names))]) for _ in range(1000)]
        out.append('1e%d-1e%d: %.3f+-%.3f' % (k - 2, k, f(L), np.std(b)))
    print('%s (%d seeds, RMS local slopes): %s' % (path.split('/')[-2] + '/' + path.split('/')[-1], len(names), '  '.join(out)))
