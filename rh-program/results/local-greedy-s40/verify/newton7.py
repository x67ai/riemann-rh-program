"""newton7.py -- Newton refinement of zeros of F_X(s) = rho*zeta(s) + D_X(s) for several starting points at once.
D_X and D_X' come from `zline ... p pts` (one pass over the a_n per Newton step, all points together); zeta, zeta' from mpmath.
Usage: python3 newton7.py a.u16 X num den steps s1r,s1i s2r,s2i ...   -> per step: s, |F|, |F'| for every point"""
import sys, subprocess, mpmath as mp
mp.mp.dps = 30
A, X, num, den, steps = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
rho = mp.mpf(num) / den
pts = [complex(*map(float, a.split(','))) for a in sys.argv[6:]]
ZL = "/private/tmp/rh-s40-local-greedy/zline"; PF = "/private/tmp/rh-s40-local-greedy/newton_pts_%s.txt" % X
print("# newton7 X=%s rho=%d/%d" % (X, num, den))
for it in range(steps):
    with open(PF, "w") as f:
        for s in pts: f.write("%.15f %.15f\n" % (s.real, s.imag))
    out = subprocess.run([ZL, A, X, str(num), str(den), "p", PF], capture_output=True, text=True).stdout.split("\n")
    rows = [l.split() for l in out if l and l[0] != '#']
    new = []
    for s, r in zip(pts, rows):
        D = complex(float(r[2]), float(r[3])); Dp = complex(float(r[4]), float(r[5]))
        z = mp.zeta(mp.mpc(s.real, s.imag)); zp = mp.zeta(mp.mpc(s.real, s.imag), derivative=1)
        F = complex(rho * z) + D; Fp = complex(rho * zp) + Dp
        print("it %d  s = %.10f %+.10fi  |F| = %.3e  |F'| = %.4f" % (it, s.real, s.imag, abs(F), abs(Fp)))
        new.append(s - F / Fp)
    pts = new
    sys.stdout.flush()
