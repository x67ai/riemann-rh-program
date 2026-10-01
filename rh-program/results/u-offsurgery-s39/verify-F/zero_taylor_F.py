# Orchestrator (Session 40): independent route for the zero of the truncation F_X of S5(4/5), X = 10^9.
#   F_X(s) = 0.8*zeta(s) + sum_{n<=X} (a_n - 0.8) n^{-s}.
# Route: Taylor moments at the box center s0:  c_k = sum (a_n - 0.8) n^{-s0} (-log n)^k / k!,  k = 0..K, one pass over the
# 10^9 exact coefficients a_n (from s5gen_F.c, the orchestrator's own generator), so that the Dirichlet-polynomial part is
# sum_k c_k h^k for s = s0 + h (|h| <= 0.03: the k = K term is < 1e-25).  zeta by mpmath.  Then: Newton for the zero,
# the minimum of |F_X| on the boundary of the NOTE's box B = [0.7459, 0.7859] x [30.306, 30.346], and the winding number.
import numpy as np, sys, time, mpmath as mp
SP = sys.argv[1]; X = 10**9; K = 28
s0 = complex(0.7659, 30.326)
a = np.memmap(SP + "/aF_r08_1e9.u16", dtype=np.uint16, mode="r")
c = np.zeros(K + 1, dtype=np.complex128)
CH = 4_000_000; t0 = time.time()
for lo in range(1, X + 1, CH):
    hi = min(lo + CH, X + 1)
    n = np.arange(lo, hi, dtype=np.float64); L = np.log(n)
    w = (a[lo:hi].astype(np.float64) - 0.8) * np.exp(-s0 * L)
    mL = -L
    for k in range(K + 1):
        c[k] += w.sum()
        w = w * mL / (k + 1)
print(f"moments done in {time.time()-t0:.0f}s; c0 = {c[0]:.12f}, c1 = {c[1]:.10f}")
np.save("zero_taylor_F_moments.npy", c)
mp.mp.dps = 30
def F(s):
    h = s - s0
    return complex(0.8 * mp.zeta(mp.mpc(s.real, s.imag))) + np.polyval(c[::-1], h)
def dF(s):
    h = s - s0
    dc = c[1:] * np.arange(1, K + 1)
    return complex(0.8 * mp.zeta(mp.mpc(s.real, s.imag), derivative=1)) + np.polyval(dc[::-1], h)
z = complex(0.77, 30.35)
for it in range(40):
    step = F(z) / dF(z); z -= step
    if abs(step) < 1e-14: break
print(f"zero of F_X (X = 1e9): {z.real:.10f} + {z.imag:.10f} i   |F| = {abs(F(z)):.2e}   |F'| = {abs(dF(z)):.4f}")
# boundary of the NOTE's box
x1, x2, y1, y2 = 0.7459, 0.7859, 30.306, 30.346
M = 100
pts = [complex(x1 + (x2 - x1) * i / M, y1) for i in range(M)] + [complex(x2, y1 + (y2 - y1) * i / M) for i in range(M)] + \
      [complex(x2 - (x2 - x1) * i / M, y2) for i in range(M)] + [complex(x1, y2 - (y2 - y1) * i / M) for i in range(M)]
vals = np.array([F(p) for p in pts])
ang = np.angle(vals[np.r_[1:len(vals), 0]] / vals)
print(f"box boundary ({len(pts)} points): min|F_X| = {np.abs(vals).min():.5f}   winding number = {ang.sum()/(2*np.pi):.6f}   max phase step = {np.abs(ang).max():.4f} rad")
