"""lobe_margins.py -- margins of the ordering invariant per N from the lobe scans.
For each N and each chain (seed xi_N: negative lobes vs P_N; Haglund Xi_N: positive lobes vs Q_N):
  r_fail  = depth/level of the first failing lobe (< 1);
  r_after = max depth/level over the same-sign lobes after it (a violation needs r_after > 1);
  margin  = -log10(r_after)   (> 0: no violation; its trend in N is the invariant's margin);
  r_before_min = min depth/level over passing lobes below the first failing one (how narrowly they pass).
Reads lobe_scan_*.json."""
import json, glob, math
rows = {}
for fn in sorted(glob.glob('lobe_scan_*.json')):
    if fn == 'lobe_scan_6_30.json':
        continue
    d = json.load(open(fn))
    for N, rec in d.items():
        rows[int(N)] = rec
print(' N | window          | chain   | first fail (lobe, r)              | r_after_max | margin=-log10 | r_before_min')
for N in sorted(rows):
    rec = rows[N]
    for key in ('seed', 'hag'):
        seq = [(float(a), float(b), float(r)) for (a, b, r) in rec[key]['ratios']]
        k = next((i for i, (_, _, r) in enumerate(seq) if r <= 1), None)
        if k is None:
            print(f'{N:2d} | {rec["window"]} | {key:7s} | no failing lobe in window')
            continue
        after = [r for (_, _, r) in seq[k + 1:]]
        before = [r for (_, _, r) in seq[:k] if r > 1]
        ra = max(after) if after else float('nan')
        print(f'{N:2d} | [{float(rec["window"][0]):6.0f},{float(rec["window"][1]):6.0f}] | {key:7s} | ({seq[k][0]:.3f}, {seq[k][1]:.3f}) r={seq[k][2]:.4g} | {ra:.4g} | {(-math.log10(ra)) if after else float("nan"):.3f} | {min(before) if before else float("nan"):.4g}')
