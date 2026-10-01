# zeros_L_S8.py — exploratory zero counts (argument principle) for
#   L(s) = 1 + rho^s zeta(s, 1/2 + rho)   (lattice control)      and
#   F_X(s) = sum_{n<=X} n^{-s} + rho X^{1-s}/(s-1) - E(X) X^{-s}   (S8(pi/16), X = 1e5, own dump)
# on boxes [a,b] x [c,d]; plus sigma_1 for L (X_L(sigma_1) = 1, where X_L = L - 1) and a search for
# a zero of L with real part in (1, sigma_1) by Newton from minima of |L| on a line.
import numpy as np, mpmath as mp, sys
rho = np.pi/16; t = 1/rho
g = np.fromfile('/private/tmp/rh-s41-lemmaB-U5-obstruction/g_pi16_1e5.bin', dtype=np.float64)
g = np.concatenate([[1.0], g]); X = 1e5; g = g[g <= X]
EX = len(g) - rho*(X - 1) - 1; lg = np.log(g)
print(f"S8 pi/16 dump: N(1e5)={len(g)} E(X)={EX:.4f}")
def FX(s):
    s = np.atleast_1d(np.asarray(s, dtype=complex)); out = np.empty(len(s), complex)
    for j in range(0, len(s), 64):
        ss = s[j:j+64]; out[j:j+64] = np.exp(-np.outer(ss, lg)).sum(1)
    return out + rho*X**(1 - s)/(s - 1) - EX*X**(-s)
mp.mp.dps = 20
def Lf(s): return complex(1 + mp.mpf(rho)**s * mp.zeta(s, 0.5 + mp.mpf(rho)))
def Lv(s): return np.array([Lf(complex(z)) for z in np.atleast_1d(s)])
def winding(f, a, b, c, d, n=4000):
    side = [np.linspace(a, b, n) + 1j*c, b + 1j*np.linspace(c, d, n), np.linspace(b, a, n) + 1j*d,
            a + 1j*np.linspace(d, c, n)]
    z = np.concatenate(side); v = f(z); ph = np.unwrap(np.angle(v))
    jump = np.max(np.abs(np.diff(np.angle(v) - 0)))  # not used for check; unwrap needs small steps
    steps = np.abs(np.diff(ph)); return (ph[-1] - ph[0])/(2*np.pi), steps.max(), np.abs(v).min()
for nm, f in [("S8 F_1e5", FX), ("L", Lv)]:
    for box in [(0.55, 0.99, 0.5, 100.0), (0.80, 0.99, 0.5, 100.0), (0.55, 0.99, 100.0, 200.0)]:
        w, st, mn = winding(f, *box, n=6000 if nm == "L" else 20000)
        print(f"{nm:9s} box {box}: winding {w:+.4f}  max phase step {st:.3f}  min|f| on boundary {mn:.4f}"); sys.stdout.flush()
# sigma_1 for L: rho^s zeta(s, a) = 1
s1 = mp.findroot(lambda s: mp.mpf(rho)**s * mp.zeta(s, 0.5 + mp.mpf(rho)) - 1, 1.5)
print(f"L: sigma_1 (X_L(sigma_1) = 1) = {mp.nstr(s1, 10)}; zeros of L with Re s >= 1 can only lie in [1, sigma_1)")
# search for a zero of L in Re s in (1, sigma_1): minima of |L| on sigma = 1.02, t in [1, 1000]
ts = np.arange(1.0, 1000.0, 0.05); vals = np.abs(Lv(1.02 + 1j*ts))
idx = np.argsort(vals)[:8]
for i in sorted(idx):
    try:
        z = mp.findroot(lambda s: 1 + mp.mpf(rho)**s * mp.zeta(s, 0.5 + mp.mpf(rho)), mp.mpc(1.02, ts[i]))
        print(f"  start t={ts[i]:.2f} |L|={vals[i]:.4f} -> Newton zero {mp.nstr(z, 12)}  |L(z)|={mp.nstr(abs(Lf(complex(z))), 3)}")
    except Exception as e:
        print(f"  start t={ts[i]:.2f} |L|={vals[i]:.4f} -> no convergence")
