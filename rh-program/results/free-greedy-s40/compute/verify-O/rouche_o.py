# rouche_o.py -- F_X on a box from the generator's moments (Taylor in s about the center), Newton, winding,
# min|F|, and Rouche margins B_max for tails |E(u)| <= B log^2 u and <= B u^b (u > Xt). Opus reader, Session 41.
# usage: python3 rouche_o.py MOMFILE X CENTER_INDEX [box_sig box_t r] [Xtail] [Ebound_between]
import sys, math, cmath
import mpmath as mp
mp.mp.dps = 30
rho = float(mp.pi / 4) if len(sys.argv) < 9 else float(eval(sys.argv[8], {"pi": mp.pi}))
mom, X, ci = sys.argv[1], float(sys.argv[2]), int(sys.argv[3])
M = {}; N = None
for line in open(mom):
    f = line.split()
    if float(f[0]) != X or int(f[2]) != ci: continue
    N = int(f[1]); s0 = complex(float(f[3]), float(f[4])); lam = float(f[5])
    M[int(f[6])] = complex(float(f[7]), float(f[8]))
J = len(M); m = [M[j] for j in range(J)]
EX = N - rho * (X - 1) - 1
lX = math.log(X)
def F(s):
    h = -(s - s0) / lam; S = 0; Sp = 0; p = 1
    for j in range(J):
        S += m[j] * p
        if j + 1 < J: Sp += (j + 1) * m[j + 1] * p * (-1 / lam)
        p *= h
    Xs = cmath.exp(-s * lX); main = rho * X * Xs / (s - 1)
    return S + main - EX * Xs, Sp + main * (-lX - 1 / (s - 1)) + EX * lX * Xs
print(f"# X={X:.6g} N={N} E(X)={EX:.10f} center={s0} lam={lam} J={J}")
s = s0
for it in range(30):
    f, fp = F(s); ds = f / fp; s -= ds
    if abs(ds) < 1e-15: break
f, fp = F(s)
print(f"zero {s.real:.12f} {s.imag:+.12f} |F|={abs(f):.2e} |F'|={abs(fp):.6f}")
if len(sys.argv) > 4:
    bs, bt, r = float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
    Xt = float(sys.argv[7]) if len(sys.argv) > 7 else X
    Eb = float(sys.argv[9]) if len(sys.argv) > 9 else 0.0     # sup|E| on (X, Xt], if Xt > X
    L = math.log(Xt); n = 4000
    pts = []
    for k in range(4):
        for i in range(n):
            u = -r + 2 * r * i / n
            pts.append([complex(bs + r, bt + u), complex(bs - u, bt + r), complex(bs - r, bt - u), complex(bs + u, bt - r)][k])
    vals = [F(p) for p in pts]
    wind = 0.0
    for i in range(len(pts)):
        a, b = vals[i][0], vals[(i + 1) % len(pts)][0]
        wind += cmath.phase(b / a)
    h = 2 * r / n; maxd = max(abs(v[1]) for v in vals)
    def K2(p):  return abs(p) * Xt ** (-p.real) * (L * L / p.real + 2 * L / p.real ** 2 + 2 / p.real ** 3)
    def Kb(p, b): return abs(p) * Xt ** (b - p.real) / (p.real - b)
    def gapE(p): return abs(p) * Eb * (X ** (-p.real) - Xt ** (-p.real)) / p.real if Xt > X else 0.0
    low = [abs(v[0]) - maxd * h / 2 - gapE(p) for p, v in zip(pts, vals)]
    print(f"box sigma {bs}+-{r}, t {bt}+-{r}: winding {wind / (2 * math.pi):+.6f}; min|F_X| (samples) {min(abs(v[0]) for v in vals):.6f}; "
          f"lower bound {min(low):.6f} (max|F'| {maxd:.3f}, step {h:.1e}); Xtail={Xt:.3g}, max gap term {max(gapE(p) for p in pts):.2e}")
    print(f"B_max log^2: {min(l / K2(p) for l, p in zip(low, pts)):.1f}   (min|F|/max K: {min(low) / max(K2(p) for p in pts):.1f})")
    for b in (0.25, 0.4, 0.5):
        print(f"B_max u^{b}: {min(l / Kb(p, b) for l, p in zip(low, pts)):.4g}")
