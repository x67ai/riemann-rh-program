# far2.py -- far-field probe for NOTE section 5 (III): k = 2, zeros of Xi_2 with real part near 500 (2a = 2*pi*9 = 56.5),
# followed through the pencil Xi_2 + t Phi_3.  Start zeros by Newton on log S = 0 (S varies like an exponential here).
import math, cmath, time
from trace import *
ctx.prec = 256
k = 2
def lognewton(z, it=60):
    for _ in range(it):
        s, d = cSd(k, z, h=1e-7)
        dz = cmath.log(s) / (d / s)
        z -= dz
        if abs(dz) < 1e-12: break
    return z
zs = []
for x in (496.0, 498.0, 500.0, 502.0, 504.0):
    z = lognewton(complex(x, 161.0))
    if abs(cS(k, z) - 1) < 1e-8 and all(abs(z - w) > 1e-6 for w in zs): zs.append(z)
zs.sort(key=lambda w: w.real)
print("zeros of Xi_2 found:", ["%.5f%+.5fi" % (z.real, z.imag) for z in zs], flush=True)
q = abs(cS(k, complex(500.0, 120.0)))
print("floor |S| below the curve = %.4e ; ln(1/floor) = %.2f" % (q, math.log(1 / q)), flush=True)
for z0 in zs[:4]:
    t0 = time.time()
    end, z, u, worst, path, ups = trace(k, z0, ds=0.05)
    w = 2.25 - 1j * z0 / 2
    TT = 0.5 * cmath.phase(w) - 0.5j * math.log(abs(w) / math.pi)
    pred = -math.log(1 / q) * (1 / TT)
    print("start %.4f%+.4fi -> %s %.4f%+.4fi  moved %+.3f %+.3fi  predicted %+.2f %+.2fi  worst step dy=%.3g  up-events=%d  steps=%d (%.0fs)"
          % (z0.real, z0.imag, end, z.real, z.imag, z.real - z0.real, z.imag - z0.imag, pred.real, pred.imag, worst, len(ups), len(path), time.time() - t0), flush=True)
