# nondeg.py -- non-degeneracy of the landing maxima found by P3: S_k''(x*) < 0 at every local maximum x* of S_k with
# value u* in (0,1) (second central difference in Arb, h = 1e-4 * spacing, relative radius 2^-90). Reports
# nu = -S''(x*) spacing(x*)^2 / u* (dimensionless; nu > 0 means a non-degenerate maximum). Writes nondeg_k<k>.json.
import sys, os, json, math
from a_core import S, acb, arb, ctx
from axis import spacing
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
ctx.prec = 96
for k in [int(a) for a in sys.argv[1:]]:
    o = json.load(open(os.path.join(D, "p3_k%d.json" % k)))
    nus = []
    for (x, u) in o["maxima"]:
        sp = spacing(x)
        h = 1e-4 * sp
        a = S(k, acb(arb(x + h), 0), "T", 90); b = S(k, acb(arb(x), 0), "T", 90); c = S(k, acb(arb(x - h), 0), "T", 90)
        ctx.prec = 300
        d2 = (a - 2 * b + c).real / (arb(x + h) - arb(x)) / (arb(x) - arb(x - h))
        nu = float((-d2 * sp * sp / b.real).mid())
        ctx.prec = 96
        nus.append(nu)
    out = {"k": k, "n_max": len(nus), "nu_min": min(nus) if nus else None, "nu_max": max(nus) if nus else None,
           "all_nondegenerate": all(v > 0 for v in nus)}
    json.dump(out, open(os.path.join(D, "nondeg_k%d.json" % k), "w"))
    print("k=%d maxima %d  nu in [%.3g, %.3g]  all S''<0: %s" % (k, len(nus), out["nu_min"] or 0, out["nu_max"] or 0, out["all_nondegenerate"]), flush=True)
