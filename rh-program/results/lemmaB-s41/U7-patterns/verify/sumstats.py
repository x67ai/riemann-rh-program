# sumstats.py — U7-patterns: compact per-band table from a stats file (output of stats.c).
# Columns: band x-range, idle (g-prime) fraction pi', mean arrivals lam = 1 - pi' (+ drift), Fano(1), mean e, tail rate kappa of the
# stationary law P(e >= h) (least squares on log P over the h where P >= 1e-6), kappa / (2 pi'/lam) (Poisson-queue ratio, M/D/1
# heavy-traffic value 2(1-lam)/lam... we report kappa against the exact Poisson root of lam(e^k - 1) = k), excursions: count, mean
# height, corr(height, X1) with X1 = Delta E(W/p1) over the build-up, and the largest gap in the band.
import sys, re, math
import numpy as np
f = sys.argv[1]
bands, eh, exc, gap = {}, {}, {}, {}
for l in open(f):
    if l.startswith('BAND'):
        b = int(l.split()[1]); d = dict(re.findall(r'(\w+)=([-\d.e+]+)', l)); x = re.search(r'x=\[([\d.e+]+),([\d.e+]+)\)', l)
        d['x0'], d['x1'] = x.group(1), x.group(2); bands[b] = d
    elif l.startswith('EHIST'):
        p = l.split(); eh[int(p[1])] = {int(a): int(v) for a, v in (q.split(':') for q in p[2:])}
    elif l.startswith('EXC'):
        p = l.split(); b = int(p[1]); d = dict(re.findall(r'(\w+)=([-\d.e+na]+)', l)); exc[b] = d
    elif l.startswith('GAP'):
        p = l.split(); gap[int(p[1])] = max([int(q.split(':')[0]) for q in p[2:]] or [0])
def poisson_kappa(lam):
    lo, hi = 1e-9, 50.0
    for _ in range(200):
        m = (lo + hi) / 2
        if lam * (math.exp(m) - 1) - m > 0: hi = m
        else: lo = m
    return lo
print('| x band | pi\' (idle/cell) | lam (arrivals/cell) | Fano(1) | mean e | kappa (tail of e) | Poisson kappa | ratio | #exc | mean h | corr(h, X1) | max gap |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|')
for b in sorted(bands):
    d = bands[b]; H = eh.get(b, {}); n = sum(H.values())
    if n < 1000: continue
    hs = sorted(H); tail = np.cumsum([H[h] for h in hs][::-1])[::-1] / n
    pts = [(h, math.log(p)) for h, p in zip(hs, tail) if h >= 2 and p >= 1e-6 * 0 + 30.0 / n]
    kap = -np.polyfit([p[0] for p in pts], [p[1] for p in pts], 1)[0] if len(pts) >= 3 else float('nan')
    lam = float(d['mean_c']); pk = poisson_kappa(lam)
    E = exc.get(b, {})
    print('| [%s, %s) | %.4f | %.4f | %.3f | %.3f | %.3f | %.3f | %.2f | %s | %s | %s | %s |' % (d['x0'], d['x1'], float(d['prime_frac']), lam,
          float(d['var_c']) / lam, float(d['mean_e']), kap, pk, kap / pk, E.get('nexc', '-'), E.get('mean_h', '-'), E.get('corr_h_X1', '-'), gap.get(b, '-')))
