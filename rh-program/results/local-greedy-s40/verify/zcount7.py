"""zcount7.py -- argument-principle zero counts of F_X on boxes [s_i, s_{i+1}] x [t_j, t_{j+1}] from scan7.sh output
(adapted from u-offsurgery-s39/verify/zcount.py).  Prints every box with a nonzero winding number, the strip totals, the
largest phase step on each contour (must be << pi) and min|F| on it; and the local minima of |F| on the vertical lines.
Usage: python3 zcount7.py logdir label X"""
import sys, glob, numpy as np
D, lab, X = sys.argv[1], sys.argv[2], sys.argv[3]
sig = ["0.55", "0.60", "0.65", "0.70", "0.75", "0.80", "0.85", "0.90", "0.95", "1.00", "1.10"]
ts = ["0.1", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
def load(fn):
    d = np.loadtxt(fn); return d[:, 0], d[:, 1], d[:, 2] + 1j * d[:, 3]
Vl = {s: load(f"{D}/{lab}_v{s}_X{X}.txt") for s in sig}
Hl = {t: load(f"{D}/{lab}_h{t}_X{X}.txt") for t in ts}
def darg(F):
    d = np.diff(np.angle(F)); d = (d + np.pi) % (2 * np.pi) - np.pi; return d.sum(), (np.abs(d).max() if len(d) else 0.0)
def vseg(s, ta, tb):
    _, t, F = Vl[s]; m = (t >= min(ta, tb) - 1e-7) & (t <= max(ta, tb) + 1e-7); F = F[m]; return F if ta < tb else F[::-1]
def hseg(t, sa, sb):
    sg, _, F = Hl[t]; m = (sg >= min(sa, sb) - 1e-7) & (sg <= max(sa, sb) + 1e-7); F = F[m]; return F if sa < sb else F[::-1]
print(f"# {lab} X={X}: boxes with nonzero winding number (sigma range, t range, count, max phase step, min|F| on contour)")
tot = np.zeros(len(sig) - 1); worst = 0
for i in range(len(sig) - 1):
    a, b = float(sig[i]), float(sig[i + 1])
    for j in range(len(ts) - 1):
        ta, tb = float(ts[j]), float(ts[j + 1])
        parts = [hseg(ts[j], a, b), vseg(sig[i + 1], ta, tb), hseg(ts[j + 1], b, a), vseg(sig[i], tb, ta)]
        w = sum(darg(p)[0] for p in parts) / (2 * np.pi); jmp = max(darg(p)[1] for p in parts); mn = min(np.abs(p).min() for p in parts)
        worst = max(worst, jmp); tot[i] += w
        if abs(w) > 0.5: print(f"box [{sig[i]},{sig[i+1]}] x [{ts[j]},{ts[j+1]}]: {w:+.3f}  (max step {jmp:.2f} rad, min|F| {mn:.3g})")
for i in range(len(sig) - 1): print(f"strip [{sig[i]},{sig[i+1]}] x [0.1,100]: {tot[i]:+.3f}")
print(f"total zeros in [0.55,1.10] x [0.1,100]: {tot.sum():+.3f}; largest phase step on any contour {worst:.2f} rad")
print("# local minima of |F| < 0.1 on the vertical lines (sigma, t, |F|)")
for s in sig:
    _, t, F = Vl[s]; A = np.abs(F); k = np.nonzero((A[1:-1] < A[:-2]) & (A[1:-1] < A[2:]) & (A[1:-1] < 0.1))[0] + 1
    for q in k: print(f"  {s} {t[q]:.3f} {A[q]:.4f}")
