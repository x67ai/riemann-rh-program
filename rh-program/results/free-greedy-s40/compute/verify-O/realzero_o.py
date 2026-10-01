# realzero_o.py -- real zero of F_X from real moments (Taylor about sigma0) + F at given sigmas. Opus reader.
# usage: python3 realzero_o.py MOMFILE rho_expr sigma1 sigma2 ...   (all snapshots in the file)
import sys, math
import mpmath as mp
rho = float(eval(sys.argv[2], {'pi': mp.pi})); sig = [float(a) for a in sys.argv[3:]]
snaps = {}
for line in open(sys.argv[1]):
    f = line.split(); x = float(f[0])
    if float(f[4]) != 0.0: continue          # real centers only
    d = snaps.setdefault(x, {'N': int(f[1]), 's0': float(f[3]), 'lam': float(f[5]), 'm': {}})
    d['m'][int(f[6])] = float(f[7])
for X in sorted(snaps):
    d = snaps[X]; m = [d['m'][j] for j in range(len(d['m']))]; s0, lam = d['s0'], d['lam']
    EX = d['N'] - rho * (X - 1) - 1; lX = math.log(X)
    def F(s):
        h = -(s - s0) / lam; S = sum(m[j] * h ** j for j in range(len(m)))
        return S + rho * X ** (1 - s) / (s - 1) - EX * X ** (-s)
    a, b = s0 - 0.04, s0 + 0.04; fa, fb = F(a), F(b); z = float('nan')
    if fa * fb < 0:
        for _ in range(200):
            c = 0.5 * (a + b); fc = F(c)
            if fc * fa > 0: a, fa = c, fc
            else: b = c
            if b - a < 1e-15: break
        z = 0.5 * (a + b)
    print(f"X={X:.4g} N={d['N']} E(X)={EX:.6f} real zero {z:.10f} " + " ".join(f"F({s})={F(s):+.6f}" for s in sig))
