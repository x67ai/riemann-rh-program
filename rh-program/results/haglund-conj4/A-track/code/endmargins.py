# endmargins.py -- post-pass (17:10 IST fix): the tracer of the first runs recorded the margin -Im S'/|S'| at the
# accepted interior nodes only. This adds the margin at each branch's start (a zero of Xi_k) and, for u = 0 ends, at the
# end (a zero of Xi_{k+1}), updates min_margin, and re-summarizes. No other field changes.
import sys, json
from a_core import SdS, ctx
from census import summarize
ctx.prec = 96
for fn in sys.argv[1:]:
    R = json.load(open(fn))
    k = R["k"]
    worst_change = 0
    for r in R["branches"]:
        z0 = complex(*r["start"])
        s, d = SdS(k, z0)
        r["margin_start"] = -d.imag / abs(d)
        ms = [r["margin_start"]] if z0.imag > 1e-6 else []
        if r["end"] == "u0":
            ze = complex(*r["z_end"])
            s, d = SdS(k, ze)
            r["margin_end"] = -d.imag / abs(d)
            if ze.imag > 1e-6:
                ms.append(r["margin_end"])
        new = min([r["min_margin"]] + ms)
        if new < r["min_margin"]:
            worst_change = max(worst_change, r["min_margin"] - new)
            r["min_margin"] = new
    s = summarize(R)
    json.dump(R, open(fn, "w"), separators=(",", ":"))
    print(fn.split("/")[-1], "min_margin now %.4f (largest decrease of a branch minimum %.3g)" % (s["min_margin"], worst_change), flush=True)
