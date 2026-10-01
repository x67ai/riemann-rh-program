"""zcount.py -- argument-principle zero counts for zeta_P in strips [s_i, s_{i+1}] x [t0, t1] from zscan output files.
Usage: python3 zcount.py prefix X sig1 sig2 ... (files prefix_v{sig}_X{X}.txt and prefix_h{t0|t1}_X{X}.txt)"""
import sys, numpy as np
pre, X = sys.argv[1], sys.argv[2]; sigs = sys.argv[3:]
def load(fn):
    d = np.loadtxt(fn); return d[:, 0], d[:, 1], d[:, 2] + 1j * d[:, 3], d[:, 5]
V = {s: load(f"{pre}_v{s}_X{X}.txt") for s in sigs}
t0, t1 = V[sigs[0]][1][0], V[sigs[0]][1][-1]
H0 = load(f"{pre}_h{t0:g}_X{X}.txt"); H1 = load(f"{pre}_h{t1:g}_X{X}.txt")
def darg(F):
    ph = np.angle(F); d = np.diff(ph); d = (d + np.pi) % (2 * np.pi) - np.pi
    return d.sum(), np.abs(d).max()
def hseg(H, a, b):   # values along the horizontal segment from sigma=a to sigma=b
    sg = H[0]; m = (sg >= min(a, b) - 1e-9) & (sg <= max(a, b) + 1e-9); F = H[2][m]
    return F if a < b else F[::-1]
tot = 0
for a, b in zip(sigs[:-1], sigs[1:]):
    A, B = float(a), float(b)
    parts = [hseg(H0, A, B), V[b][2], hseg(H1, B, A), V[a][2][::-1]]
    d = sum(darg(p)[0] for p in parts); jmp = max(darg(p)[1] for p in parts)
    mn = min(np.abs(p).min() for p in parts); tb = max(V[a][3].max(), V[b][3].max())
    n = d / (2 * np.pi); tot += n
    print(f"strip sigma in [{a},{b}] x t in [{t0:g},{t1:g}]: zeros = {n:+.3f}  (max phase step {jmp:.2f} rad, min|F| on contour {mn:.3g}, tail bound <= {tb:.2g})")
print(f"total over [{sigs[0]},{sigs[-1]}]: {tot:+.3f}")
