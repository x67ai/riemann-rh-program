# tail_shape.py TAG -- shape of the time-weighted tail of E in the last two half-decade windows:
# log10 P(E > y) at y = 5, 10, ..., and the local decay rate between consecutive levels (constant = exponential tail).
import sys, math, numpy as np
tag = sys.argv[1]
H = np.fromfile(f"/private/tmp/rh-s40-free-greedy/{tag}.hist", dtype=np.float64).reshape(-1, 8193)
edges = -1 + np.arange(8193) / 16
for k in (len(H) - 2, len(H) - 1):
    m = H[k, 1:] - H[k - 1, 1:]; m[m < 1.0] = np.where(m[m < 1.0] < 0, 0, m[m < 1.0])
    tot = m.sum(); surv = 1 - np.cumsum(m) / tot
    print(f"# window ending x = {H[k, 0]:.3e} (log x = {math.log(H[k, 0]):.2f}); level y : log10 P(E > y) : local rate over [y-5, y]")
    prev = None
    for y in range(0, 85, 5):
        j = int((y + 1) * 16) - 1
        p = surv[j]
        if p <= 0: break
        rate = (math.log(prev) - math.log(p)) / 5 if prev else float("nan")
        print(f"  {y:3d}  {math.log10(p):8.3f}  {rate:7.4f}")
        prev = p
