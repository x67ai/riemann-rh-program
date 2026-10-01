# zeros_newton.py — Newton-verified zeros with Re s > 1/2, 0 < Im s < 100, for
#   L(s) = 1 + rho^s zeta(s, 1/2 + rho)  (lattice control; mpmath)            and
#   F_X(s) for S8(pi/16), X = 1e6 (own dump; numpy; exploratory, F_X is a truncation of zeta_P)
# Starts: local minima of |f| along the lines Re s = 0.55, 0.65, 0.75, 0.85, 0.95, step 0.1 in t.
import numpy as np, mpmath as mp, sys
rho = np.pi/16; X = 1e6; mp.mp.dps = 20
g = np.fromfile('/private/tmp/rh-s41-lemmaB-U5-obstruction/g_pi16_1e6.bin', dtype=np.float64)
G = np.concatenate([[1.0], g[g <= X]]); lg = np.log(G); EX = len(G) - rho*(X - 1) - 1
def F(s):
    s = np.atleast_1d(np.asarray(s, complex)); out = np.empty(len(s), complex)
    for j in range(0, len(s), 50): out[j:j+50] = np.exp(-np.outer(s[j:j+50], lg)).sum(1)
    return out + rho*X**(1 - s)/(s - 1) - EX*X**(-s)
def dF(s):
    return (-(lg*np.exp(-s*lg)).sum() - rho*np.log(X)*X**(1 - s)/(s - 1) - rho*X**(1 - s)/(s - 1)**2
            + EX*np.log(X)*X**(-s))
def L(s): return 1 + mp.mpf(rho)**s * mp.zeta(s, 0.5 + mp.mpf(rho))
ts = np.arange(0.5, 100.0, 0.1)
for name in ("L", "S8"):
    found = []
    for sg in (0.55, 0.65, 0.75, 0.85, 0.95):
        if name == "L": v = np.array([abs(complex(L(mp.mpc(sg, tt)))) for tt in ts])
        else: v = np.abs(F(sg + 1j*ts))
        mins = [i for i in range(1, len(ts) - 1) if v[i] < v[i-1] and v[i] < v[i+1] and v[i] < 0.6]
        for i in mins:
            z = complex(sg, ts[i])
            try:
                if name == "L": z = complex(mp.findroot(L, mp.mpc(z))); res = abs(complex(L(mp.mpc(z))))
                else:
                    for _ in range(40):
                        fz = F(z)[0]; z = z - fz/dF(z)
                    res = abs(F(z)[0])
            except Exception: continue
            if res < 1e-8 and 0.5 < z.real < 1.0 and 0 < z.imag < 100 and all(abs(z - w) > 1e-6 for w in found):
                found.append(z)
    found.sort(key=lambda w: w.imag)
    print(f"{name}: {len(found)} zeros with 1/2 < Re s < 1, 0 < Im s < 100 (Newton-verified, |f| < 1e-8):")
    for w in found: print(f"   {w.real:.6f} + {w.imag:.6f} i")
    sys.stdout.flush()
