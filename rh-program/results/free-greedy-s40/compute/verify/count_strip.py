# count_strip.py MOMFILE SIGMA_L SIGMA_R TMAX -- number of zeros of F_X in SIGMA_L < sigma < SIGMA_R, 0.01 < t < TMAX by the
# argument principle: the two vertical edges are sampled on the FFT grid (dt ~ 0.030), every step whose arg change exceeds
# pi/8 is refined by direct block-moment evaluation (bisection); the short horizontal edges are evaluated directly.
import sys, math, warnings, numpy as np
warnings.filterwarnings("ignore")
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from zeta_bm import load, F_grid, Gfun
from zeros_scan import arg_path
D = load(sys.argv[1]); sl, sr, tmax = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
t0 = 0.01
def vertical(sg):                                  # arg change of G along sigma = sg from t0 to tmax (upward)
    t, Fv = F_grid(sg, D, tmax=tmax + 1.0)
    sel = (t > t0) & (t < tmax); t = t[sel]; G = (sg + 1j * t - 1) * Fv[sel]
    pts = [complex(sg, t0)] + [complex(sg, x) for x in t] + [complex(sg, tmax)]
    gs = [Gfun(pts[0], D)] + list(G) + [Gfun(pts[-1], D)]
    tot, nref = 0.0, 0
    for k in range(len(pts) - 1):
        r = gs[k + 1] / gs[k]; d = math.atan2(r.imag, r.real)
        if abs(d) >= math.pi / 8: d = arg_path(pts[k], pts[k + 1], D, gs[k], gs[k + 1]); nref += 1
        tot += d
    return tot, nref
right, nr = vertical(sr)
left, nl = vertical(sl)
bottom = arg_path(complex(sl, t0), complex(sr, t0), D)
top = arg_path(complex(sr, tmax), complex(sl, tmax), D)
w = (bottom + right + top - left) / (2 * math.pi)
print(f"# count_strip {sys.argv[1]}: X = {D['X']:.3e}; {sl} < sigma < {sr}, {t0} < t < {tmax}: winding = {w:.4f}  (refined steps: right {nr}, left {nl})")
