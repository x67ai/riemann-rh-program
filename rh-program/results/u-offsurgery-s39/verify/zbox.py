"""zbox.py -- winding number of zeta_P around a box from zscan side files (bottom, right, top, left) and the tail bound
under the growth hypothesis H_theta: |C(u)| <= u^theta for all u > X, C(u) = N(u) - rho*floor(u):
|tail(s)| <= |C(X)| X^-sigma + |s| X^(theta-sigma)/(sigma-theta).  Usage: python3 zbox.py prefix theta"""
import sys, numpy as np
pre, th = sys.argv[1], float(sys.argv[2])
def load(fn):
    hdr = open(fn).readline(); X = float(hdr.split('X=')[1].split()[0]); CX = float(hdr.split('C(X)=')[1].split()[0])
    d = np.loadtxt(fn); return X, CX, d[:, 0] + 1j * d[:, 1], d[:, 2] + 1j * d[:, 3]
B, R, T, L = (load(f"{pre}_{k}.txt") for k in ("bottom", "right", "top", "left"))
X, CX = B[0], B[1]
pts = np.concatenate([B[2], R[2], T[2][::-1], L[2][::-1]]); F = np.concatenate([B[3], R[3], T[3][::-1], L[3][::-1]])
d = np.diff(np.angle(np.append(F, F[0]))); d = (d + np.pi) % (2 * np.pi) - np.pi
sg = pts.real; tail = abs(CX) * X**(-sg) + np.abs(pts) * X**(th - sg) / (sg - th)
print(f"X={X:.3g} C(X)={CX:.4g} points={len(F)}: winding = {d.sum()/(2*np.pi):+.6f}; max phase step {np.abs(d).max():.3f} rad")
print(f"min |F| on box = {np.abs(F).min():.4g}; max tail bound (H_theta, theta={th}) = {tail.max():.4g}; ratio = {np.abs(F).min()/tail.max():.2f}")
print("Rouche applies (one zero of the full zeta_P in the box) iff ratio > 1 and the phase steps resolve the contour (< pi/2).")
