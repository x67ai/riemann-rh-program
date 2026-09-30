#!/usr/bin/env python3
"""t3_kappa.py — conj-O-s38 task 3: log-power index of the decline of M(X)/M_diag(X), M_diag = rho^2 W(X)/12 (truncated Franel
diagonal), fitted as log(M/M_diag) = a - kappa*log(ln X) over dyadic windows X >= 1e6, versus the equivalent pure-power fit
log(M/M_diag) = a' + g*log X. Over one data range both fit; kappa ~ 2-3.5 for every greedy set, including c = 1, where
beta_2 >= alpha/2 is an UNCONDITIONAL theorem (fr Theorem C in mean-square form). Log: logs/t3_kappa.log"""
import sys, numpy as np; sys.path.insert(0, ".")
from dyadic_ms import load, windows
from t3_analysis import rnums_table, at
FR = "../../novel-wave-s37/beurling-frontier/verify"
CASES = [("greedy c=1 a=0.60 [Thm C: beta2>=a/2 uncond.]", FR + "/data_big/greedy_a0.60.csv", "rn/greedy_a0.60_c1.csv", None),
         ("greedy c=1 a=0.75 [Thm C: beta2>=a/2 uncond.]", FR + "/data_big/greedy_a0.75.csv", "rn/greedy_a0.75_c1.csv", None),
         ("greedy c=2 a=0.60 [Cor Z.1 (RH): beta2>=a/2]", FR + "/data_big/greedy_a0.60_c2.csv", "rn/greedy_a0.60_c2.csv", None),
         ("greedy c=2 a=0.75 [Cor Z.1 (RH): beta2>=a/2]", "data_big/greedy_a0.75_c2.csv", "rn/greedy_a0.75_c2.csv", None)]
for a in ("0.60", "0.75"):
    for s in (1, 2, 3, 4):
        CASES.append(("T_%s seed %d [Thm B]" % (a, s), FR + "/data_big/bern_a%s.csv" % a, "rn/bern_a%s_s%d.csv" % (a, s), "_s%d" % s))
import glob, os
for f in sorted(glob.glob("rn/feedback_*.csv")):
    tag = os.path.basename(f)[:-4]; csv = ("data_big/" if tag.endswith("1e10") else "data/") + tag + ".csv"
    if os.path.exists(csv): CASES.append(("design " + tag, csv, f, None))
print("%-52s %7s %7s %9s %9s %8s" % ("case (X >= 1e6)", "kappa", "+-", "g(power)", "+-", "M/diag@top"))
for lab, csv, rn, key in CASES:
    runs = load(csv); r = [k for k in runs if key is None or k.endswith(key)][0]; d = runs[r]
    X, Xe, M = windows(d); bh, Q, W = rnums_table(rn)
    ratio = M / (d["rho"] ** 2 * np.array([at(bh, W, x) for x in X]) / 12)
    m = X >= 1e6; y = np.log(ratio[m])
    A = np.vstack([np.ones(m.sum()), -np.log(np.log(X[m]))]).T; c, *_ = np.linalg.lstsq(A, y, rcond=None)
    res = y - A @ c; cov = (res @ res) / max(m.sum() - 2, 1) * np.linalg.inv(A.T @ A)
    B = np.vstack([np.ones(m.sum()), np.log10(X[m])]).T; c2, *_ = np.linalg.lstsq(B, y / np.log(10), rcond=None)
    res2 = y / np.log(10) - B @ c2; cov2 = (res2 @ res2) / max(m.sum() - 2, 1) * np.linalg.inv(B.T @ B)
    print("%-52s %7.2f %7.2f %9.3f %9.3f %8.3f" % (lab, c[1], np.sqrt(cov[1, 1]), c2[1], np.sqrt(cov2[1, 1]), ratio[-1]))
