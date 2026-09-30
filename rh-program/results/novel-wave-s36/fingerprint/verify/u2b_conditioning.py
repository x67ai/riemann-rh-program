"""
u2b_conditioning.py -- how much of the precision loss is intrinsic (conditioning) and how much is ball
over-estimation?  Run the S-fraction (real side) and Levinson (circle side) twice: (i) in ball arithmetic,
(ii) in midpoint-only arithmetic (radii stripped every step) at precisions P and 2P; the midpoint difference
between P and 2P is the ACTUAL error of the P-run; compare with the ball radius of the P-run.
"""
import sys, os, json, time
from math import comb
sys.path.insert(0, os.path.dirname(__file__))
from flint import arb, arb_series, ctx
import fp_core as fc

def mid(x):
    return arb(x.mid())

def zeta_inputs(P, M, N):
    ctx.prec = P
    half = arb(1) / 2; logpi = arb.pi().log()
    ctx.cap = 2 * M + 1
    x = arb_series([0, 1]); s = half + x
    c = (half.log() + (arb(1) / 4 - x * x).log() - (s / 2) * logpi + (s / 2).lgamma() + (-(s.zeta())).log()).coeffs()
    cm = [((-1) ** (m + 2)) * (m + 1) * c[2 * (m + 1)] for m in range(0, M)]
    ctx.cap = N + 3
    w = arb_series([0, 1]); s1 = 1 + w
    d = (half.log() + s1.log() - (s1 / 2) * logpi + (s1 / 2).lgamma() + (1 + w * s1.zeta(deflate=True)).log()).coeffs()
    lam = [arb(0)] + [n * sum((arb(comb(n - 1, j - 1)) * d[j] for j in range(1, n + 1)), arb(0)) for n in range(1, N + 2)]
    mm = [lam[n + 1] - 2 * lam[n] + (lam[1] if n == 0 else lam[n - 1]) for n in range(0, N + 1)]
    return cm, mm

def sfrac_mid(c, nmax):
    """Viskovatov with radii stripped after every operation (floating-point at ctx.prec)."""
    L = len(c)
    F = [mid(v / c[0]) for v in c]
    al = []
    for n in range(1, nmax + 1):
        if len(F) < 2:
            break
        ctx.cap = len(F)
        inv = (1 / arb_series(F)).coeffs()
        inv = [mid(v) for v in inv] + [arb(0)] * (len(F) - len(inv))
        G = [(-inv[k]) for k in range(len(F))]
        a = mid(G[1])
        al.append(a)
        F = [mid(v / a) for v in G[1:]]
    return al

def levinson_mid(m, nmax):
    phi = [arb(1)]; h = mid(m[0]); alpha = []
    for n in range(0, nmax):
        r = mid(sum((phi[k] * m[k + 1] for k in range(n + 1)), arb(0)))
        a = mid(r / h); alpha.append(a)
        zphi = [arb(0)] + phi; star = list(reversed(phi)) + [arb(0)]
        phi = [mid(zphi[k] - a * star[k]) for k in range(n + 2)]
        h = mid(h * (1 - a * a))
    return alpha

M, N = 120, 120
res = {}
for P in (3000, 6000):
    cm, mm = zeta_inputs(P, M, N)
    ctx.prec = P
    t0 = time.time()
    res[P] = {
        'al_ball': fc.sfrac_from_series(cm, M - 1, stop_on_zero=False),
        'al_mid': sfrac_mid([mid(v) for v in cm], M - 1),
        'V_ball': fc.verblunsky_levinson(mm, N)[0],
        'V_mid': levinson_mid([mid(v) for v in mm], N),
    }
    print('P', P, 'done %.1fs' % (time.time() - t0), flush=True)

import mpmath as mp
mp.mp.dps = 50
def errdig(a, b):
    """digits of agreement between two arb midpoints (relative)."""
    ctx.prec = 6000
    d = abs(a - b); aa = abs(b)
    if d == 0:
        return 9999
    q = (d / aa)
    try:
        return int(-float(q.log().mid()) / 2.302585093)
    except Exception:
        return None

out = {'real': [], 'circle': []}
for n in (1, 10, 20, 40, 60, 80, 100, 118):
    i = n - 1
    out['real'].append({'n': n,
                        'ball_certified_digits_P3000': fc.digits(res[3000]['al_ball'][i]),
                        'actual_digits_mid_P3000_vs_P6000': errdig(res[3000]['al_mid'][i], res[6000]['al_mid'][i])})
for n in (0, 5, 10, 20, 30, 40, 60, 80, 100, 119):
    out['circle'].append({'n': n,
                          'ball_certified_digits_P3000': fc.digits(res[3000]['V_ball'][n]),
                          'actual_digits_mid_P3000_vs_P6000': errdig(res[3000]['V_mid'][n], res[6000]['V_mid'][n])})
for k in out:
    print(k)
    for r in out[k]:
        print('  ', r)
with open(os.path.join(os.path.dirname(__file__), 'u2b_conditioning.json'), 'w') as fh:
    json.dump(out, fh, indent=1)
