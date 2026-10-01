# rouche.py MOMFILE SIGMA0 T0 [r1 r2 ...] -- the Rouche margin for one zero z0 of F_X.
# zeta_P = F_X + R_X with |R_X(s)| <= |s| int_X^oo |E(u)| u^{-sigma-1} du.  If |E(u)| <= B log^2 u for u > X:
#   |R_X(s)| <= B K(s),  K(s) = |s| X^-sigma (log^2 X / sigma + 2 log X / sigma^2 + 2 / sigma^3).
# On the boundary of a square box of half-side r about z0: winding of F_X (= number of zeros inside), min |F_X|
# (sampled; minus max|F'| * h / 2 for the sampling gap), and B_max = min_boundary (|F_X| - gap) / K.
# Rouche: if |E(u)| <= B log^2 u for all u > X with B < B_max, zeta_P has exactly as many zeros in the box as F_X.
import sys, math, warnings, numpy as np
warnings.filterwarnings("ignore")
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from zeta_bm import load, F

D = load(sys.argv[1]); z0 = complex(float(sys.argv[2]), float(sys.argv[3]))
rs = [float(a) for a in sys.argv[4:]] or [0.005, 0.01, 0.02, 0.04]
X, lX = D["X"], D["logX"]
def K(s): sg = s.real; return abs(s) * X ** (-sg) * (lX ** 2 / sg + 2 * lX / sg ** 2 + 2 / sg ** 3)
print(f"# rouche {sys.argv[1]}  X = {X:.4e}  z0 = {z0}")
print("#  r        n/side  winding   min|F_X| (sampled)  max|F'|   min|F|-gap     max K      B_max(log^2)  B_max for |E| <= B u^b, b = 0.25 / 0.40 / 0.50")
for r in rs:
    n = 400
    corners = [z0 + complex(-r, -r), z0 + complex(r, -r), z0 + complex(r, r), z0 + complex(-r, r)]
    pts = []
    for a, b in zip(corners, corners[1:] + corners[:1]):
        pts += [a + (b - a) * k / n for k in range(n)]
    vals = [F(s, D, deriv=True) for s in pts]
    fv = np.array([v[0] for v in vals]); fd = np.array([abs(v[1]) for v in vals])
    ang = np.angle(np.append(fv, fv[0]))
    dang = np.angle(np.exp(1j * np.diff(ang)))
    wind = dang.sum() / (2 * math.pi)
    h = 2 * r / n
    mn = np.abs(fv).min(); gap = fd.max() * h / 2
    Kv = np.array([K(s) for s in pts])
    bmax = ((np.abs(fv) - gap) / Kv).min()
    ok = "" if np.abs(dang).max() < math.pi / 4 else "  (phase step > pi/4: refine)"
    bp = []
    for b in (0.25, 0.40, 0.50):
        Kb = np.array([abs(s) * X ** (b - s.real) / (s.real - b) for s in pts])
        bp.append(((np.abs(fv) - gap) / Kb).min())
    print(f"  {r:.4f}  {n:6d}  {wind:+8.4f}   {mn:.6e}      {fd.max():.3e}  {mn - gap:.6e}  {Kv.max():.4e}  {bmax:.4e}    {bp[0]:.3e} / {bp[1]:.3e} / {bp[2]:.3e}{ok}")
