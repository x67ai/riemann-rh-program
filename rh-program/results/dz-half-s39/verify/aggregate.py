#!/usr/bin/env python3
"""aggregate.py — table of the finite rung: slopes by window (mean ± seed s.e.), normalized dyadic mean squares, drift.
Reads data/*.stats.json; writes logs/aggregate.txt and data/aggregate.json."""
import json, glob, math
import numpy as np

groups = {"DZ R (Thm 17.11, P_R)": "data/dz_R_s*.stats.json", "DZ C (Thm 17.14, P_B)": "data/dz_C_s*.stats.json",
          "ctl: rational primes": "data/ctl_primes.stats.json", "ctl: P_det (grid, no selection)": "data/ctl_det.stats.json",
          "ctl: T1 surgery (w_p = 1/(1+log p))": "data/ctl_t1_s*.stats.json",
          "ctl: T_0.90 (frontier)": "data/ctl_ta0.90_s*.stats.json", "ctl: T_0.95 (frontier)": "data/ctl_ta0.95_s*.stats.json"}
lines, agg = [], {}
def ms(v):
    v = np.array([u for u in v if np.isfinite(u)])
    return (float(v.mean()), float(v.std(ddof=1) / math.sqrt(len(v))) if len(v) > 1 else float("nan"), len(v))
for g, pat in groups.items():
    files = sorted(glob.glob(pat))
    if not files:
        continue
    runs = [json.load(open(f)) for f in files]
    agg[g] = {}
    lines.append("== %s  (%d run%s, X = %.0e)" % (g, len(runs), "s" if len(runs) > 1 else "", runs[0]["X"]))
    lines.append("   rho: " + ", ".join("%.4f" % r["rho"] for r in runs))
    for w in ["1e3", "1e4", "1e5", "1e6"]:
        row = {q: ms([r["slopes"][w][q] for r in runs]) for q in ["sup", "supL", "ms", "msL"]}
        agg[g][w] = row
        lines.append("   window [%s, X]: " % w + "  ".join("%s=%.3f±%.3f" % (q, row[q][0], row[q][1]) for q in row))
    # normalized statistics per block (x_j = 1.5 * 2^j), averaged over runs
    js = sorted({b["j"] for r in runs for b in r["blocks"]})
    tab = []
    for j in js:
        bs = [b for r in runs for b in r["blocks"] if b["j"] == j]
        xm = bs[0]["xm"]; s = math.sqrt(xm / math.log(xm))
        tab.append((j, xm, np.mean([b["nrm"] for b in bs]), np.mean([b["mean"] / s for b in bs]),
                    np.std([b["mean"] / s for b in bs]), np.mean([b["pos"] for b in bs])))
    agg[g]["blocks"] = tab
    for (j, xm, nrm, mn, sd, pos) in tab:
        if j % 3 == 2 or j == js[-1]:
            lines.append("   j=%2d x~%.2e  MS/(x/log x)=%8.3f  mean(E)/sqrt(x/log x)=%+7.3f (seed sd %.3f)  frac(E>0)=%.2f" % (j, xm, nrm, mn, sd, pos))
open("logs/aggregate.txt", "w").write("\n".join(lines) + "\n")
json.dump(agg, open("data/aggregate.json", "w"), indent=1, default=float)
print("\n".join(lines))
