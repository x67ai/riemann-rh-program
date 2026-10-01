# records.py — U7-patterns: record times of e_k (first cell where e reaches each new maximum) and the ratios
# (e_k + 1/2)/log^2 x_k <= sup_{u <= x_k} E(u)/log^2 x_k <= (e_k + 3/2)/log^2 x_k at those cells (tau = 1/2, no early placement).
import sys, math, numpy as np
pre, D = sys.argv[1], int(sys.argv[2]); rho = math.pi / D; t = 1 / rho; tau = 0.5
e = np.memmap(pre + '.e.u8', np.uint8, 'r'); n = len(e); B = 1 << 26; run = -1; recs = []
for a in range(0, n, B):
    ch = np.asarray(e[a:a + B]).astype(np.int16); acc = np.maximum.accumulate(ch)
    new = np.nonzero((acc > run) & (ch == acc) & (np.concatenate(([run], acc[:-1])) < ch))[0]
    for i in new:
        if ch[i] > run: run = int(ch[i]); recs.append((a + i + 1, run))
print("# records of e_k for %s: cell, x_k, e, lower ratio (e+1/2)/log^2 x, upper ratio (e+3/2)/log^2 x" % pre)
for k, v in recs:
    x = 1 + (k - 1 + tau) * t; L2 = math.log(x) ** 2
    if x > 1e3: print("%d %.6g %d %.4f %.4f" % (k, x, v, (v + 0.5) / L2, (v + 1.5) / L2))
