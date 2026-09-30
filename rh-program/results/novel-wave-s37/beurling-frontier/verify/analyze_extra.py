#!/usr/bin/env python3
"""analyze_extra.py — diagnostics beyond fit.py (reads data/ and data_big/ CSVs).
(a) supL3: slope of log(M(x) (ln x)^{3/2}) — the model E ~ C x^{a/2} (log x)^{-3/2} predicted by the prime-square branch point
    (2s - a)^{1/2} of zeta_P at s = a/2 (NOTE Theorem C) for structured deletions.
(b) drift: per top-decade bin, d = ((maxE+) + (minE-))/((maxE+) - (minE-)) in [-1, 1]; |d| near 1 = one-signed error (systematic drift).
(c) variance heuristic: RMS of E at the top decade vs sqrt(rho * Q(x)/12), Q(x) = (6/pi^2) x^a / a = expected # squarefree R-numbers <= x.
"""
import sys, os, glob, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fit import load, slope
base = os.path.dirname(os.path.abspath(__file__))
def rho_of(path):
    out = {}
    for line in open(path):
        if line.startswith("# run="):
            r = line.split("run=")[1].split()[0]
            out[r] = float(line.split("rho=")[1].split()[0]) if "rho=" in line else float("nan")
    return out
for sub in ("data", "data_big"):
    for path in sorted(glob.glob(os.path.join(base, sub, "*.csv"))):
        name = os.path.basename(path)[:-4]
        if name.startswith(("mean", "none", "cramer")):
            continue
        a = float(name.split("_a")[1].split("_")[0])
        runs = load(path); rhos = rho_of(path)
        rows = []
        for r, d in runs.items():
            hi, M = d["hi"], d["M"]; xmax = hi.max()
            sl3 = slope(hi, M * np.log(hi) ** 1.5, 1e5, xmax)
            sl = slope(hi, M, 1e5, xmax)
            top = hi >= xmax / 10
            mx = d["A"]  # not signed; reload signed from file below
            rows.append((r, sl, sl3, top))
        # signed drift from raw file
        raw = {}
        for line in open(path):
            if line.startswith("#"): continue
            f = line.split(",")
            raw.setdefault(f[0], []).append((float(f[2]), float(f[3]), int(f[1]), int(f[2 - 1 + 1])))
        print("== %s/%s  a=%.2f  (candidates a/2=%.4f, a/3=%.4f, a-1/2=%.4f)" % (sub, name, a, a / 2, a / 3, a - 0.5))
        for (r, sl, sl3, top) in rows:
            d = runs[r]; xmax = d["hi"].max()
            vals = [(float(l.split(",")[3]), float(l.split(",")[4])) for l in open(path) if l.startswith(r + ",") and int(l.split(",")[2]) >= xmax / 10]
            drift = np.median([(p + q) / (p - q) for p, q in vals if p - q > 0]) if vals else float("nan")
            rms_top = float(np.sqrt(np.mean(d["rms"][d["hi"] >= xmax / 10] ** 2)))
            Q = 6 / math.pi ** 2 * xmax ** a / a
            heur = math.sqrt(rhos.get(r, float("nan")) * Q / 12)
            print("   %-28s sup-slope[1e5,x]=%.4f  supL3-slope=%.4f  drift=%+.2f  RMS_top=%.4g  sqrt(rho Q/12)=%.4g  ratio=%.2f"
                  % (r, sl, sl3, drift, rms_top, heur, rms_top / heur))
