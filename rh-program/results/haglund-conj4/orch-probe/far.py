# far.py -- far-field probe for NOTE section 5 (III): k = 2, zeros of Xi_2 with real part near 500 (about nine times 2a = 2*pi*9),
# followed through the pencil Xi_2 + t Phi_3.  Prediction (heuristic): each descends by about 20.2 * Im(1/(T'/T)) ~ 8.4 and moves right ~2.5.
import math, cmath, time
from trace import *
ctx.prec = 256
k = 2
def absS1(z):                      # |S_k(z) - 1| : zero exactly at the zeros of Xi_k
    return abs(cS(k, z) - 1.0)
# coarse search along vertical lines for small |S - 1|, then Newton on S = 1
cands = []
for x in (495.0, 500.0, 505.0):
    best = None
    y = 100.0
    while y <= 170.0:
        v = absS1(complex(x, y))
        if best is None or v < best[0]: best = (v, y)
        y += 0.5
    cands.append(complex(x, best[1]))
zs = []
for c in cands:
    try:
        z = newton_zero(k, c, 1.0)
        if all(abs(z - w) > 1e-6 for w in zs) and z.imag > 1: zs.append(z)
    except Exception as e:
        print("newton failed from", c, e)
print("zeros of Xi_2 found:", ["%.6f%+.6fi" % (z.real, z.imag) for z in zs])
for z0 in zs:
    t0 = time.time()
    end, z, u, worst, path, ups = trace(k, z0, ds=0.1)
    w = 2.25 - 1j * z0 / 2
    TT = 0.5 * cmath.phase(w) - 0.5j * math.log(abs(w) / math.pi)
    pred = -20.2 * (1 / TT)
    print("start %.4f%+.4fi -> %s %.4f%+.4fi  moved %+.3f %+.3fi  predicted %+.2f %+.2fi  worst step dy=%.3g  up-events=%d  steps=%d (%.0fs)"
          % (z0.real, z0.imag, end, z.real, z.imag, z.real - z0.real, z.imag - z0.imag, pred.real, pred.imag, worst, len(ups), len(path), time.time() - t0))
