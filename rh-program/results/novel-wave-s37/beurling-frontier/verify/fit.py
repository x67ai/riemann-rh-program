#!/usr/bin/env python3
"""fit.py — error-exponent fits for the M1b simulations (reads verify/data/*.csv written by thin / thin_aux).

For each run and each log-bin [lo, hi] of integers: A = sup_{x in bin} |N(x) - rho x| (= max(maxEplus, -minEminus)),
RMS = sqrt(sumE2/count) with E evaluated at n + 1/2. Derived: running sup M(x) = max over bins up to x.
Fitted slopes (least squares in log10-log10) over windows [1e4, Xmax], [1e5, Xmax], [1e6, Xmax], [1e7, Xmax]:
  sup   : log M(x) vs log x          (the [alpha,beta] exponent is lim sup log|E|/log x; M is its finite-range proxy)
  rms   : log RMS_bin vs log x        (mean-square exponent)
  rmsL  : log(RMS_bin * sqrt(log x))  (model RMS ~ x^b / sqrt(log x), predicted by Var ~ #R-numbers/log-type factors)
Error bars: mean over seeds +- standard error (std/sqrt(n)); the window-to-window spread is reported separately.
Usage: python3 fit.py [datadir]  -> prints a table; writes datadir/fit_summary.json
"""
import sys, os, glob, json, math
import numpy as np

D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

def load(path):
    runs = {}
    for line in open(path):
        if line.startswith("#") or not line.strip():
            continue
        r, lo, hi, mx, mn, s2, cnt, psi = line.strip().split(",")
        runs.setdefault(r, []).append((int(lo), int(hi), float(mx), float(mn), float(s2), int(cnt), float(psi)))
    out = {}
    for r, rows in runs.items():
        a = np.array(rows, dtype=float)
        lo, hi = a[:, 0], a[:, 1]
        A = np.maximum(a[:, 2], -a[:, 3])
        rms = np.sqrt(a[:, 4] / a[:, 5])
        M = np.maximum.accumulate(A)
        out[r] = dict(lo=lo, hi=hi, A=A, rms=rms, M=M, psi=a[:, 6])
    return out

def slope(x, y, lo, hi):
    m = (x >= lo) & (x <= hi) & (y > 0)
    if m.sum() < 5:
        return float("nan")
    X = np.log10(x[m]); Y = np.log10(y[m])
    return float(np.polyfit(X, Y, 1)[0])

WINDOWS = [(1e4, None), (1e5, None), (1e6, None), (1e7, None)]

def fit_run(d):
    xmax = d["hi"].max()
    hi = d["hi"]; mid = np.sqrt(np.maximum(d["lo"], 1) * d["hi"])
    res = {}
    for (w0, _) in WINDOWS:
        key = "%.0e" % w0
        res[key] = dict(
            sup=slope(hi, d["M"], w0, xmax),
            rms=slope(mid, d["rms"], w0, xmax),
            rmsL=slope(mid, d["rms"] * np.sqrt(np.log(mid)), w0, xmax),
        )
    return res

def candidates(alpha):
    return {"alpha/2": alpha / 2, "alpha/3": alpha / 3, "alpha/4": alpha / 4, "1/(4-2a)": 1 / (4 - 2 * alpha),
            "1/(3-a)": 1 / (3 - alpha), "2a/(a+2) [BDR]": 2 * alpha / (alpha + 2), "a-1/2": alpha - 0.5}

def main():
    summary = {}
    for path in sorted(glob.glob(os.path.join(D, "*.csv"))):
        name = os.path.basename(path)[:-4]
        runs = load(path)
        fits = {r: fit_run(d) for r, d in runs.items()}
        agg = {}
        for key in ["%.0e" % w for (w, _) in WINDOWS]:
            agg[key] = {}
            for q in ("sup", "rms", "rmsL"):
                v = np.array([fits[r][key][q] for r in fits if not math.isnan(fits[r][key][q])])
                if len(v):
                    agg[key][q] = (float(v.mean()), float(v.std(ddof=1) / math.sqrt(len(v))) if len(v) > 1 else float("nan"), len(v))
        alpha = None
        if "_a" in name:
            alpha = float(name.split("_a")[1].split("_")[0])
        xmax = max(d["hi"].max() for d in runs.values())
        topM = [float(d["M"][-1]) for d in runs.values()]
        summary[name] = dict(alpha=alpha, nruns=len(runs), xmax=xmax, windows=agg,
                             supE_at_xmax=[min(topM), max(topM)],
                             psiR_ratio_at_xmax=[float(d["psi"][-1]) for d in runs.values()][:8],
                             candidates=candidates(alpha) if alpha else None)
        print("== %s  (runs=%d, xmax=%.3g, sup|E| at xmax in [%.4g, %.4g])" % (name, len(runs), xmax, min(topM), max(topM)))
        if alpha:
            print("   candidates: " + ", ".join("%s=%.4f" % kv for kv in candidates(alpha).items()))
        for key, dd in agg.items():
            print("   window [%s, xmax]: " % key + "  ".join("%s=%.4f±%.4f(n=%d)" % (q, *dd[q]) for q in dd))
    json.dump(summary, open(os.path.join(D, "fit_summary.json"), "w"), indent=1, default=float)

if __name__ == "__main__":
    main()
