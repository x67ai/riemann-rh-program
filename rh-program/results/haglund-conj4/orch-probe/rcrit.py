# rcrit.py -- numerical look at the criterion of NOTE Prop. 2.3 in its unconditional form:
# a lift-off at x0 forces (log Xi)''(x0) >= (log L_t)''(x0).  We tabulate, on the part of the real axis where Xi > 0,
#   ratio(x) = max_u [-(log L_u)''(x)] / [-(log Xi)''(x)],   L_u = u Phi_{k+1} + Q_{k+1},
# by central differences on Arb midpoints.  ratio < 1 everywhere on the range  =>  no lift-off on the range (numerical, not a certificate).
import sys, math
from c4probe import *
ctx.prec = 400
def vals(k, x):
    z = acb(x)
    xi = Xi(z).real
    a, b = pair_T(k, z)                 # a = Xi_{k+1}(x), b = Phi_{k+1}(x)
    q = xi - a.real                     # Q_{k+1}(x)
    return xi, b.real, q
def d2log(f0, fp, fm, h):
    d1 = (fp - fm) / (2 * h); d2 = (fp - 2 * f0 + fm) / (h * h)
    return d2 / f0 - (d1 / f0) ** 2
def run(k, X, step=0.02):
    h = arb("1e-12")
    worst = (0.0, None); n = 0
    minsig = 1e300; maxm = 0.0
    x = 0.01
    while x <= X:
        xi0, p0, q0 = vals(k, x)
        if xi0 > 0:
            xip, pp, qp = vals(k, arb(x) + h); xim, pm, qm = vals(k, arb(x) - h)
            sig = -float(d2log(xi0, xip, xim, h).mid())           # -(log Xi)''  (positive under RH)
            m = 0.0
            for u in (0.0, 0.25, 0.5, 0.75, 1.0):
                L0 = p0 * u + q0; Lp = pp * u + qp; Lm = pm * u + qm
                m = max(m, -float(d2log(L0, Lp, Lm, h).mid()))
            n += 1
            minsig = min(minsig, sig); maxm = max(maxm, m)
            r = m / sig
            if r > worst[0]: worst = (r, x)
        x += step
    print("k=%2d  X=%7.1f  points with Xi>0: %6d   max ratio = %.3e at x=%.2f   min -(log Xi)'' = %.4f   max -(log L_u)'' = %.3e   [1/(2 pi^2 (k+1)^4) = %.3e]"
          % (k, X, n, worst[0], worst[1], minsig, maxm, 1 / (2 * math.pi ** 2 * (k + 1) ** 4)))
if __name__ == "__main__":
    for k in [int(a) for a in sys.argv[1:]]:
        run(k, 4 * (k + 2) ** 2 + 40)
