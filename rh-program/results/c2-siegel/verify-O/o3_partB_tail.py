#!/usr/bin/env python3
"""o3_partB_tail.py -- Opus check, item 3: the scout's Part B Poisson entries.

The scout's planted_real_zero.py Part B integrates Arch_K(w) = int what(s) a_K(s) ds on the grid Sg = [-20, 20] only
(lines 102-103 and 142 of that script). For the Poisson elements what = pi_a = 2a/(a^2 + s^2) the tail |s| > 20 carries
int_{|s|>20} pi_a a_K > 0 (a_K grows like log|s|/pi), so the truncated Arch is too small and the margins too large.
Here: full-line Arch with the closed form a_K(s) = (1/pi)[Re psi(1/2 + is/2) - log pi] + log|D|/2pi, versus the same
integral truncated to |s| <= 20, for the scout's elements Poisson a = 0.55, 0.6; share 2 int pi_a mu_y by adaptive quadrature.
Also: margin/what(0) maximized over my continuous Gaussian / pure-Poisson / Fejer families at D = -20.
"""
import math, json
import numpy as np
from scipy.integrate import quad
from scipy.special import digamma as sdg
from scipy.optimize import minimize_scalar
LOG = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); LOG.append(s)
LOGPI = math.log(math.pi)
def aK(s, absD): return (np.real(sdg(0.5 + 0.5j * s)) - LOGPI) / math.pi + math.log(absD) / (2 * math.pi)
def mu(s, de):
    sd = math.sin(math.pi * de)
    if math.pi * abs(s) > 300: return 2 * sd * math.exp(-math.pi * abs(s))
    sh = math.sinh(math.pi * s); return sd * math.cosh(math.pi * s) / (sh * sh + sd * sd)
def I(f, lo, hi, pts):
    e = [lo] + [p for p in pts if lo < p < hi] + [hi]
    return sum(quad(f, a, b, limit=400, epsabs=1e-13, epsrel=1e-11)[0] for a, b in zip(e[:-1], e[1:]))
def poisson_margin(a, de, absD, cut=None, mult=1):
    wh = lambda s: 2 * a / (a * a + s * s)
    share = 2 * 2 * I(lambda s: wh(s) * mu(s, de), 0, math.inf, [de, 10 * de, 100 * de, 1, 5, 20])
    hi = math.inf if cut is None else cut
    arch = 2 * I(lambda s: wh(s) * aK(s, absD), 0, hi, [1, 5, 20])
    return mult * share - 2 * (2 / a) - arch, arch
say("scout Part B Poisson elements, D = -20: single margin with full-line Arch vs Arch truncated to |s| <= 20 (the scout's grid)")
rows = []
for a in (0.55, 0.6):
    for de in (0.1, 0.05, 0.02, 0.01, 0.001):
        mf, af = poisson_margin(a, de, 20); mt, at = poisson_margin(a, de, 20, cut=20)
        rows.append(dict(a=a, delta=de, full=mf, trunc=mt))
        say("  Poisson a=%.2f delta=%.3f: margin full %+.5f ; truncated %+.5f ; Arch tail |s|>20 = %.5f" % (a, de, mf, mt, af - at))
say("scout log (planted_real_zero_run.log lines 36-40) prints +0.64509 [a=0.6], +0.98866, +1.26438, +1.36468, +1.45884 [a=0.55]")
for absD, a in ((2005, 0.55), (1e6, 0.55)):
    for de in (0.1, 0.001):
        mf, _ = poisson_margin(a, de, absD, mult=2); mt, _ = poisson_margin(a, de, absD, cut=20, mult=2)
        say("  double, |D| = %g, Poisson a=%.2f delta=%.3f: margin full %+.5f ; truncated %+.5f" % (absD, a, de, mf, mt))
# margin / what(0), continuous families, D = -20
fams = {
 "gauss": (lambda s, p: math.exp(-s*s/(2*p*p)), lambda p: 1.0, lambda p: 12*p),
 "poisson": (lambda s, p: 2*p/(p*p+s*s), lambda p: 2/p, lambda p: math.inf),
 "fejer": (lambda s, p: max(0.0, 1-abs(s)/p), lambda p: 1.0, lambda p: p),
}
def ratio(fam, p, de, absD):
    wh, w0, hi = fams[fam]; H = hi(p)
    share = 4 * I(lambda s: wh(s, p) * mu(s, de), 0, H, [de, 10*de, 100*de, 0.3, 1, 3, p])
    arch = 2 * I(lambda s: wh(s, p) * aK(s, absD), 0, H, [0.5, 2, 10, p])
    return (share - 2 * w0(p) - arch) / w0(p)
say("best single margin / what(0) at D = -20 (continuous parameter), compare scout 'reach vs |D| = 20': +0.59470 (delta 0.1), +0.65953 (delta 0.01)")
for de in (0.1, 0.01):
    parts = []
    for fam, rng in (("gauss", (0.05, 5)), ("poisson", (0.02, 5)), ("fejer", (0.1, 12))):
        xs = np.exp(np.linspace(math.log(rng[0]), math.log(rng[1]), 50)); v = [ratio(fam, x, de, 20) for x in xs]; i = int(np.argmax(v))
        r = minimize_scalar(lambda x: -ratio(fam, x, de, 20), bounds=(xs[max(i-1,0)], xs[min(i+1,49)]), method="bounded")
        parts.append("%s %+.5f (p %.4f)" % (fam, max(-r.fun, v[i]), r.x))
    say("  delta=%.2f: " % de + " ; ".join(parts))
open(__file__.replace(".py", "_run.log"), "w").write("\n".join(LOG) + "\n")
json.dump(rows, open(__file__.replace(".py", "_out.json"), "w"), indent=1)
