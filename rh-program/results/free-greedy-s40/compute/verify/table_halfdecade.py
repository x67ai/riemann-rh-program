# table_halfdecade.py TAG [XMIN] -- task 1's per-half-decade table as markdown, from verify/logs/TAG.log (S rows) and
# the time-weighted E histogram (/private/tmp/rh-s40-free-greedy/TAG.hist).  Window = (previous sample, x].
import sys, math, numpy as np
V = __file__.rsplit("/", 1)[0]
tag = sys.argv[1]; xmin = float(sys.argv[2]) if len(sys.argv) > 2 else 1e3
S = [[float(v) for v in ln.split()[1:]] for ln in open(f"{V}/logs/{tag}.log") if ln.startswith("S ")]
H = np.fromfile(f"/private/tmp/rh-s40-free-greedy/{tag}.hist", dtype=np.float64).reshape(-1, 8193)
edges = -1 + np.arange(8193) / 16
print("| x | N(x) | π_P(x) | sup E | E(x) | mean E (win) | q50 / q90 / q99 (win) | longest busy period (win): length, peak E | max # in unit window | min gap (win): abs, rel | min threshold margin (rel) | sup\\|ψ−x\\| | ψ−x |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
prev = np.zeros(8192)
for k, r in enumerate(S):
    m = H[k, 1:] - prev; prev = H[k, 1:].copy()
    if r[0] < xmin: continue
    m = np.where(m < 0, 0, m); tot = m.sum(); cdf = np.cumsum(m) / tot
    def q(a):
        j = min(int(np.searchsorted(cdf, a)), 8191); c0 = cdf[j - 1] if j > 0 else 0.0
        return edges[j] + (a - c0) / max(cdf[j] - c0, 1e-300) / 16
    print(f"| {r[0]:.3g} | {int(r[1]):,} | {int(r[2]):,} | {r[4]:.2f} | {r[5]:.2f} | {r[6]:.2f} | {q(.5):.1f} / {q(.9):.1f} / {q(.99):.1f} | {r[8]:.0f}, {r[10]:.1f} | {int(r[11])} | {r[12]:.1e}, {r[13]:.1e} | {r[16]:.1e} | {r[19]:.4g} | {r[20]:.4g} |")
