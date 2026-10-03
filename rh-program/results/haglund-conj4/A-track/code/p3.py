# p3.py -- A-track P3: the real-axis test (d) alone for pencils k on [0, 4(k+2)^2 + 40]: every local extremum of S_k with
# value in (0,1) must be a local maximum. Grid spacing/20 on the whole interval; the frontier part
# [4(k+1)^2 - 40, end] is scanned a second time at spacing/40 and the two results compared.
import sys, os, json, math, time
from a_core import *
from axis import scan, Sx

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

def one(k, route="T"):
    t0 = time.time()
    X = 4.0 * (k + 2) ** 2 + 40
    r = scan(k, 0.0, X, route, frac=20.0)
    xf = max(0.0, 4.0 * (k + 1) ** 2 - 40)
    r2 = scan(k, xf, X, route, frac=40.0)
    lo = lambda L: [z for z in L if z > xf + 1e-9]
    same = (len(lo(r["zeros_Xik"])) == r2["R_k"] and len(lo(r["zeros_Xik1"])) == r2["R_k1"] and
            sorted(round(e["x"], 6) for e in r["extrema01"] if e["x"] > xf) == sorted(round(e["x"], 6) for e in r2["extrema01"]))
    sa, sb = Sx(k, 0.0, route)[0], Sx(k, X, route)[0]
    out = {"k": k, "X": X, "R_k": r["R_k"], "R_k1": r["R_k1"], "n_max": r["n_max"], "n_min": r["n_min"],
           "n_unresolved": r["n_unresolved"], "all_consistent": r["all_consistent"], "frontier_rescan_agrees": same,
           "frontier_rescan": {"x0": xf, "n_max": r2["n_max"], "n_min": r2["n_min"], "consistent": r2["all_consistent"]},
           "S_at_0": sa, "S_at_X": sb, "landings_eq_half_real_diff": r["n_max"] - r["n_min"] == (r["R_k1"] - r["R_k"]) / 2.0,
           "maxima": [(e["x"], e["u"]) for e in r["extrema01"] if e["type"] == "max"],
           "minima": [(e["x"], e["u"]) for e in r["extrema01"] if e["type"] != "max"],
           "largest_real_zero_Xik": max(r["zeros_Xik"]) if r["zeros_Xik"] else None,
           "largest_real_zero_Xik1": max(r["zeros_Xik1"]) if r["zeros_Xik1"] else None,
           "ngrid": r["ngrid"] + r2["ngrid"], "secs": round(time.time() - t0, 1),
           "arb_maxrel": STATS["maxrel"], "arb_maxprec": STATS["maxprec"]}
    return out

if __name__ == "__main__":
    ks = [int(a) for a in sys.argv[1:]]
    ctx.prec = 96
    for k in ks:
        o = one(k)
        json.dump(o, open(os.path.join(DATA, "p3_k%d.json" % k), "w"), separators=(",", ":"))
        print("P3 k=%d X=%.0f R_k=%d R_k1=%d max=%d min=%d unres=%d consistent=%s rescan=%s S(0)=%.3g S(X)=%.3g half=%s (%.0fs)" % (
            k, o["X"], o["R_k"], o["R_k1"], o["n_max"], o["n_min"], o["n_unresolved"], o["all_consistent"],
            o["frontier_rescan_agrees"], o["S_at_0"], o["S_at_X"], o["landings_eq_half_real_diff"], o["secs"]), flush=True)
