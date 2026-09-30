#!/usr/bin/env python3
"""t3_analysis.py — conj-O-s38 task 3 tables. Log: verify/logs/t3_analysis.log; JSON: verify/data/t3_summary.json.
For every design: dyadic mean square M(X) (dyadic_ms.windows: exact, non-overlapping windows [X, 1.995X], from 10^4),
  (1) pure-power slopes of log M over [10^k, Xmax], k = 4..7, and over the top three decades;
  (2) log-corrected fit  log M = a + b log X - kappa log ln X  over [10^4, Xmax] (b = exponent net of a log-power), and b with
      kappa fixed at the model value, and the local-slope-vs-1/lnX intercept;
  (3) with rnums files: local exponents of Q_R(X) (# squarefree R-numbers <= X) and of W(X), and the ratio
      M(X)/M_diag(X), M_diag = rho^2 W(X)/12 (the truncated Franel diagonal; exact for finite R over a period);
  (4) the random-R reference slope of X^alpha/ln X over the same windows.
Random designs: mean +- s.e. over seeds. Structured designs: one run; the spread over windows is the systematic.
"""
import sys, os, json, glob, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dyadic_ms import load, windows, slope, sup_slope

HERE = os.path.dirname(os.path.abspath(__file__))
FR = os.path.join(HERE, "..", "..", "novel-wave-s37", "beurling-frontier", "verify")

def logfit(X, M, kappa=None):
    L = np.log(X); LL = np.log(np.log(X)); y = np.log(M)
    if kappa is None:
        A = np.vstack([np.ones_like(L), L, -LL]).T
        c, res, *_ = np.linalg.lstsq(A, y, rcond=None)
        r = y - A @ c; s2 = (r @ r) / max(len(y) - 3, 1); cov = s2 * np.linalg.inv(A.T @ A)
        return float(c[1]), float(math.sqrt(cov[1, 1])), float(c[2]), float(math.sqrt(cov[2, 2]))
    A = np.vstack([np.ones_like(L), L]).T; c, *_ = np.linalg.lstsq(A, y + kappa * LL, rcond=None)
    return float(c[1])

def local_intercept(X, M):
    """local slopes over 2-decade windows regressed on 1/ln X; intercept = exponent extrapolated to X -> infinity."""
    xs, ss = [], []
    for i in range(len(X)):
        m = (X >= X[i]) & (X < X[i] * 100 * 0.999)
        if m.sum() >= 6 and X[i] * 100 <= X.max() * 2.1:
            xs.append(1 / math.log(math.sqrt(X[i] * X[m].max()))); ss.append(slope(X[m], M[m]))
    if len(xs) < 3:
        return float("nan"), float("nan")
    c = np.polyfit(xs, ss, 1)
    return float(c[1]), float(c[0])

def rnums_table(path):
    a = np.loadtxt(path, delimiter=",", comments="#")
    return a[:, 0], a[:, 2], a[:, 3]      # bin_hi, Q, W

def at(xs, ys, X):
    i = np.searchsorted(xs, X, side="right") - 1
    return ys[max(i, 0)]

def analyse(d, alpha, rn=None):
    X, Xe, M = windows(d)
    out = dict(rho=d["rho"], n_windows=int(len(X)), xmax=float(Xe.max()))
    for k in (4, 5, 6, 7):
        out["ms_%d" % k] = slope(X, M, 10 ** k); out["sup_%d" % k] = sup_slope(d, 10 ** k)
    out["ms_top3"] = slope(X, M, Xe.max() / 2e3); out["sup_top3"] = sup_slope(d, Xe.max() / 1e3)
    b, sb, kap, sk = logfit(X, M); out.update(logfit_b=b, logfit_b_se=sb, logfit_kappa=kap, logfit_kappa_se=sk)
    out["b_kappa1"] = logfit(X, M, 1.0); out["b_kappa2"] = logfit(X, M, 2.0); out["b_kappa3"] = logfit(X, M, 3.0)
    out["local_intercept"], out["local_coef"] = local_intercept(X, M)
    if alpha:
        out["ref_random"] = slope(X, X ** alpha / np.log(X), 10 ** 4)
    if rn is not None:
        bh, Q, W = rn
        Qx = np.array([at(bh, Q, x) for x in X]); Wx = np.array([at(bh, W, x) for x in X])
        out["Q_slope"] = slope(X, Qx, 10 ** 4); out["W_slope"] = slope(X, Wx, 10 ** 4)
        ratio = M / (d["rho"] ** 2 * Wx / 12.0)
        out["ratio_diag"] = [[float(x), float(r)] for x, r in zip(X[::3], ratio[::3])]
        out["ratio_slope"] = slope(X, ratio, 10 ** 4); out["ratio_top"] = float(ratio[-1])
        out["Q_at_xmax"] = float(Qx[-1])
    return out

def fmt(o, keys):
    return " ".join("%s=%s" % (k, ("%.3f" % o[k]) if isinstance(o.get(k), float) else o.get(k)) for k in keys)

if __name__ == "__main__":
    specs = json.load(open(sys.argv[1]))      # list of {name, csv, alpha, rnums(optional), group(optional)}
    summ, groups = {}, {}
    for s in specs:
        runs = load(s["csv"])
        for r, d in runs.items():
            rn = rnums_table(s["rnums"][r]) if s.get("rnums") and r in s["rnums"] else None
            o = analyse(d, s.get("alpha"), rn); o["design"] = s["name"]; summ[r] = o
            groups.setdefault(s.get("group", s["name"]), []).append(o)
    KEYS = ["ms_4", "ms_6", "ms_7", "ms_top3", "sup_4", "sup_7", "sup_top3", "logfit_b", "logfit_kappa", "b_kappa1",
            "b_kappa3", "local_intercept", "ref_random", "Q_slope", "W_slope", "ratio_slope", "ratio_top"]
    for g, L in groups.items():
        print("== %s (%d run%s)" % (g, len(L), "s" if len(L) > 1 else ""))
        for k in KEYS:
            v = np.array([o[k] for o in L if isinstance(o.get(k), float) and not math.isnan(o[k])])
            if len(v) == 0: continue
            if len(v) > 1:
                print("   %-16s %.3f +- %.3f  (min %.3f, max %.3f)" % (k, v.mean(), v.std(ddof=1) / math.sqrt(len(v)), v.min(), v.max()))
            else:
                print("   %-16s %.3f" % (k, v[0]))
    json.dump(summ, open(os.path.join(HERE, "data", "t3_summary.json"), "w"), indent=1)
