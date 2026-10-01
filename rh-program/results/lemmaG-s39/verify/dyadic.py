#!/usr/bin/env python3
"""dyadic.py — lemmaG-s39 analysis. Uses cO's exact dyadic statistic (imported from dyadic_ms_cO.py, a verbatim copy of
cO/verify/dyadic_ms.py): M(X) = (1/X') int_X^{X+X'} E^2 over non-overlapping 6-bin windows (X'/X = 10^0.3 - 1).
Adds: M_diag(X) = rho^2 W(X)/12 from lg's 'rn' rows (W at the window's upper edge), the ratio M/M_diag and its log-power index
kappa (fit log(M/M_diag) = a - kappa log ln X over X >= 1e6), pure-power slopes on [1e4,X], [1e6,X], top 3 decades, local
2-decade slopes, and a fit of the pole-at-alpha law E ~ A x^(1/2) (ln x)^(-3/4) cos(sqrt(2 ln x) + phi) (nsq family only)."""
import sys, json, math, re
import numpy as np
sys.path.insert(0, ".")
from dyadic_ms_cO import load, windows, slope, sup_slope

def load_rn(path):
    rn = {}
    for line in open(path):
        if not line.startswith("rn,"): continue
        f = line.strip().split(","); rn.setdefault(f[1], []).append((float(f[2]), float(f[3]), float(f[4])))
    return {k: np.array(v) for k, v in rn.items()}

def analyze(csv, rnfile):
    D = load(csv); RN = load_rn(rnfile) if rnfile else {}
    out = {}
    for run, d in D.items():
        X, Xe, M = windows(d)
        res = dict(run=run, rho=d["rho"], xmax=float(Xe.max()))
        for k in (4, 6): res["ms_%d" % k] = slope(X, M, 10 ** k)
        res["ms_top3"] = slope(X, M, Xe.max() / 1e3 / 1.9999)
        res["sup_4"] = sup_slope(d, 1e4)
        if run in RN:
            r = RN[run]; W = np.interp(Xe - 1, r[:, 0], r[:, 2]); Q = np.interp(Xe - 1, r[:, 0], r[:, 1])
            Md = d["rho"] ** 2 * W / 12.0; ratio = M / Md
            res["Q_slope_4"] = slope(Xe, Q, 1e4); res["Mdiag_slope_4"] = slope(Xe, Md, 1e4)
            m = X >= 1e6
            if m.sum() >= 3:
                A = np.vstack([np.ones(m.sum()), -np.log(np.log(X[m]))]).T
                coef, resid, *_ = np.linalg.lstsq(A, np.log(ratio[m]), rcond=None); res["kappa"] = float(coef[1])
            res["ratio"] = [(float(x), float(v)) for x, v in zip(X, ratio)]
        res["M"] = [(float(x), float(v)) for x, v in zip(X, M)]
        loc = []
        for i in range(len(X)):
            mm = (X >= X[i]) & (X < X[i] * 100 * 0.999)
            if mm.sum() >= 6 and X[i] * 100 <= Xe.max() * 1.01: loc.append((float(X[i]), slope(X[mm], M[mm])))
        res["local2dec"] = loc
        out[run] = res
    return out

if __name__ == "__main__":
    allres = {}
    for arg in sys.argv[1:]:
        csv, rn = (arg.split(":") + [None])[:2]
        allres.update(analyze(csv, rn))
    for run, r in allres.items():
        print("%-34s rho=%.6f ms[1e4,X]=%.3f ms[1e6,X]=%.3f top3=%.3f sup[1e4,X]=%.3f Qslope=%s Mdiag_slope=%s kappa=%s" % (run, r["rho"],
              r["ms_4"], r["ms_6"], r["ms_top3"], r["sup_4"], "%.3f" % r["Q_slope_4"] if "Q_slope_4" in r else "-",
              "%.3f" % r["Mdiag_slope_4"] if "Mdiag_slope_4" in r else "-", "%.2f" % r["kappa"] if "kappa" in r else "-"))
        if "ratio" in r:
            sel = [v for v in r["ratio"] if v[0] in (r["ratio"][0][0],) or abs(math.log10(v[0]) - round(math.log10(v[0]))) < 0.16]
            print("    M/M_diag at ~decades: " + "  ".join("%.0e:%.3g" % v for v in sel))
        print("    local 2-dec slopes: " + "  ".join("%.0e:%.3f" % v for v in r["local2dec"][::3]))
    json.dump(allres, open("data/dyadic_summary_%s.json" % (sys.argv[1].split("/")[-1].split(".")[0].split(":")[0]), "w"), indent=1)
