# site_lt.py -- routes L (literal sum, precision raised until the relative radius is 2^-40) and T at 5 points of each of
# the site branches: pencil 26 from 3130.2619 + 52.4297i (ends at the Xi_27 zero 3143.2207 + 0.3153i) and from
# 3132.1660 + 52.9056i (lands at 3145.2290), pencil 27 from 3143.2207 + 0.3153i (lands at 3143.2466).
import json, time
from a_core import S, az, ctx, STATS
ctx.prec = 96
out = []
for (fn, k, x0) in (("../data/frontier_k26.json", 26, 3130.2619), ("../data/frontier_k26.json", 26, 3132.1660),
                    ("../data/frontier_k27.json", 27, 3143.2207)):
    R = json.load(open(fn))
    br = [r for r in R["branches"] if abs(r["start"][0] - x0) < 1e-3][0]
    P = br["path"]
    for j in sorted(set([0, len(P) // 4, len(P) // 2, (3 * len(P)) // 4, len(P) - 1])):
        u, x, y = P[j]
        z = complex(x, y)
        t0 = time.time(); a = S(k, az(z), "T", 40); tT = time.time() - t0
        p0 = STATS["maxprec"]
        t0 = time.time(); b = S(k, az(z), "L", 40); tL = time.time() - t0
        ctx.prec = 256
        rel = float((abs(a - b) / abs(a)).mid())
        ov = (a - b).contains(0)
        ctx.prec = 96
        rec = {"k": k, "branch": x0, "z": [x, y], "S_T": a.str(12), "S_L": b.str(12), "rel_diff": rel, "balls_overlap": bool(ov),
               "secs_T": round(tT, 3), "secs_L": round(tL, 2)}
        out.append(rec)
        print(json.dumps(rec), flush=True)
json.dump(out, open("../data/site_routes_LT.json", "w"), indent=0)
print("max prec used", STATS["maxprec"])
