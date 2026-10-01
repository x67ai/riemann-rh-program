# gaprec.py — U7-patterns: record g-prime gaps (in cells; length = cells*t) and G/log^3 x, G/log^2 x at the closing g-prime.
import sys, math, numpy as np
pre, D = sys.argv[1], int(sys.argv[2]); rho = math.pi / D; t = 1 / rho; tau = 0.5
pk = np.memmap(pre + '.primes.u32', np.uint32, 'r'); n = len(pk); B = 1 << 26; run = 0; prev = None; out = []
for a in range(0, n, B):
    ch = np.asarray(pk[a:a + B]).astype(np.int64)
    if prev is not None: ch = np.concatenate(([prev], ch))
    g = np.diff(ch); acc = np.maximum.accumulate(g); idx = np.nonzero((g == acc) & (g > run))[0]
    for i in idx:
        if g[i] > run: run = int(g[i]); out.append((int(ch[i + 1]), run))
    prev = int(ch[-1])
print("# record gaps %s: closing cell, x, gap (cells), G = gap*t, G/log^2 x, G/log^3 x" % pre)
for k, gc in out:
    x = 1 + (k - 1 + tau) * t; L = math.log(x)
    if x > 1e3: print("%d %.6g %d %.3f %.4f %.4f" % (k, x, gc, gc * t, gc * t / L**2, gc * t / L**3))
