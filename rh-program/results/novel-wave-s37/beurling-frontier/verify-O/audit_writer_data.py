#!/usr/bin/env python3
"""audit_writer_data.py (reader O) — reads the writer's CSVs (read-only) and prints, per seed and per decade,
max E+, min E-, sup|E|, RMS, and per-seed slopes of the running sup over the four windows, to locate the
upward drift of the [1e7, X] window. Usage: python3 audit_writer_data.py <csv> [<csv> ...]"""
import sys, numpy as np
for path in sys.argv[1:]:
    runs = {}
    for line in open(path):
        if line.startswith('#') or not line.strip(): continue
        r, lo, hi, mx, mn, s2, cnt, psi = line.strip().split(',')
        runs.setdefault(r, []).append((float(lo), float(hi), float(mx), float(mn), float(s2), float(cnt)))
    print('==', path.split('/')[-2] + '/' + path.split('/')[-1])
    for r, rows in runs.items():
        a = np.array(rows); hi = a[:, 1]; A = np.maximum(a[:, 2], -a[:, 3]); M = np.maximum.accumulate(A)
        out = []
        for d in range(4, int(np.log10(hi.max())) + 1):
            m = (hi > 10**(d-1)) & (hi <= 10**d * 1.0001)
            if not m.any(): continue
            out.append('%d:+%.0f/-%.0f rms%.0f' % (d, a[m, 2].max(), -a[m, 3].min(), np.sqrt(a[m, 4].sum() / a[m, 5].sum())))
        sl = []
        for w0 in (1e4, 1e5, 1e6, 1e7):
            m = hi >= w0
            sl.append(np.polyfit(np.log10(hi[m]), np.log10(M[m]), 1)[0])
        print('  %s slopes %s | %s' % (r, ' '.join('%.3f' % s for s in sl), '  '.join(out[-4:])))
