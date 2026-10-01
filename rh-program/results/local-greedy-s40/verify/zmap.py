"""zmap.py -- locate zeros of F_X inside a box [s0, s1] x [t0, t1] (where the argument principle counted some) from Taylor moments at
centres spaced 0.5 apart in t on the mid-line (one zline pass for all centres), evaluated on a grid; prints grid minima of |F|.
Usage: python3 zmap.py a.u16 X num den s0 s1 t0 t1"""
import sys, subprocess, numpy as np, mpmath as mp
A, X, num, den = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); s0, s1, t0, t1 = map(float, sys.argv[5:9])
rho = num / den; K = 30; sm = 0.5 * (s0 + s1); cs = np.arange(t0 + 0.25, t1, 0.5)
PF = "/private/tmp/rh-s40-local-greedy/zmap_pts.txt"; open(PF, "w").write("".join("%.6f %.6f\n" % (sm, c) for c in cs))
out = subprocess.run(["/private/tmp/rh-s40-local-greedy/zline", A, X, str(num), str(den), "m", PF, str(K)], capture_output=True, text=True).stdout.split("\n")
M = {}; cur = None
for l in out:
    if l.startswith("C "): cur = float(l.split()[2]); M[cur] = []
    elif cur is not None and l.strip(): M[cur].append(complex(float(l.split()[1]), float(l.split()[2])))
best = []
for c in cs:
    co = np.array(M[min(M, key=lambda v: abs(v - c))])[::-1]
    for sg in np.linspace(s0, s1, 21):
        for t in np.linspace(c - 0.25, c + 0.25, 11):
            s = complex(sg, t); F = complex(rho * mp.zeta(s)) + np.polyval(co, s - complex(sm, c)); best.append((abs(F), sg, t))
best.sort()
print("# zmap %s X=%s rho=%d/%d box [%g,%g]x[%g,%g]: smallest |F| on the grid (|F|, sigma, t)" % (A.split('/')[-1], X, num, den, s0, s1, t0, t1))
for b in best[:8]: print("%.4f %.4f %.3f" % b)
