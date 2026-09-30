#!/usr/bin/env python3
"""dyadic_ms.py — conj-O-s38 task 3. Exact dyadic mean square M(X) = (1/X') int_X^{X'} E(x)^2 dx, X' = 10^0.3 X (= 1.995 X),
from the thin / thin_fr / thin2 CSV bins (20 per decade; row: run,lo,hi,maxEplus,minEminus,sumE2,count,psi).
On [n, n+1) E is linear with slope -rho, so int_n^{n+1} E^2 = (N(n) - rho(n + 1/2))^2 + rho^2/12 EXACTLY: a bin contributes
sumE2 + count*rho^2/12. Dyadic windows = 6 consecutive bins aligned at 10^4 (non-overlapping). rho is read from the '# run=' header.
Fits (least squares, log10 M vs log10 X over windows with X >= 10^k, k = 4..7, and over the top three decades) and the frontier
NOTE's running-sup slope (fit.py convention: running max of max(maxEplus, -minEminus) vs bin upper edge) for side-by-side use.
Optional: rnums files (from rnums.c) give Q_R(X) (# squarefree R-numbers <= X) and W(X) = sum_{b<=X} prod_{p|b}(p+1)/(p-1), and
the diagonal prediction M_diag(X) = rho^2 W(X)/12 (exact for finite R over a period: Prop. 5.1).
"""
import sys, re, json, math
import numpy as np

def load(path):
    runs, rho, meta = {}, {}, {}
    for line in open(path):
        if line.startswith("#"):
            m = re.search(r"run=(\S+)", line)
            if m:
                r = m.group(1)
                rho[r] = float(re.search(r" rho=([0-9.eE+-]+)", line).group(1))
                meta[r] = line.strip()
            continue
        if not line.strip():
            continue
        f = line.strip().split(",")
        runs.setdefault(f[0], []).append([float(v) for v in f[1:7]])
    out = {}
    for r, rows in runs.items():
        a = np.array(rows)
        out[r] = dict(lo=a[:, 0], hi=a[:, 1], mx=a[:, 2], mn=a[:, 3], s2=a[:, 4], cnt=a[:, 5], rho=rho[r], meta=meta[r])
    return out

def windows(d, start_exp=4.0, nb=6):
    """non-overlapping windows of nb bins from 10^start_exp; returns X (lower edge), X' (upper edge), M (exact mean square)."""
    lo, hi, s2, cnt, rho = d["lo"], d["hi"], d["s2"], d["cnt"], d["rho"]
    k0 = int(np.searchsorted(lo, math.ceil(10 ** start_exp - 1e-9)))
    Xs, Xe, M = [], [], []
    k = k0
    while k + nb <= len(lo):
        c = cnt[k:k + nb].sum()
        if c <= 0:
            break
        Xs.append(lo[k]); Xe.append(hi[k + nb - 1] + 1)
        M.append((s2[k:k + nb].sum() + c * rho * rho / 12.0) / c)
        k += nb
    return np.array(Xs), np.array(Xe), np.array(M)

def slope(x, y, lo=None, hi=None):
    m = np.isfinite(y) & (y > 0)
    if lo is not None: m &= x >= lo
    if hi is not None: m &= x <= hi
    if m.sum() < 3:
        return float("nan")
    return float(np.polyfit(np.log10(x[m]), np.log10(y[m]), 1)[0])

def sup_slope(d, w0):
    A = np.maximum(d["mx"], -d["mn"]); Mr = np.maximum.accumulate(A)
    return slope(d["hi"], Mr, w0, d["hi"].max())

def fit(d, extra=None):
    X, Xe, M = windows(d)
    xmax = Xe.max()
    res = dict(X=X.tolist(), M=M.tolist(), xmax=float(xmax))
    for k in (4, 5, 6, 7):
        res["ms_%d" % k] = slope(X, M, 10 ** k)
        res["sup_%d" % k] = sup_slope(d, 10 ** k)
    res["ms_top3"] = slope(X, M, xmax / 1e3 / 1.9999)
    res["sup_top3"] = sup_slope(d, xmax / 1e3)
    # local 2-decade mean-square slopes (sliding by one window)
    loc = []
    for i in range(len(X)):
        m = (X >= X[i]) & (X < X[i] * 100 * 0.999)
        if m.sum() >= 6 and X[i] * 100 <= xmax * 1.01:
            loc.append((float(X[i]), slope(X[m], M[m])))
    res["local2dec"] = loc
    return res

if __name__ == "__main__":
    for path in sys.argv[1:]:
        for r, d in load(path).items():
            f = fit(d)
            print(f"{r}: rho={d['rho']:.9g} windows={len(f['X'])} xmax={f['xmax']:.3g}")
            print("   ms-slope  [1e4,X] %.3f [1e5,X] %.3f [1e6,X] %.3f [1e7,X] %.3f top3 %.3f" %
                  (f["ms_4"], f["ms_5"], f["ms_6"], f["ms_7"], f["ms_top3"]))
            print("   sup-slope [1e4,X] %.3f [1e5,X] %.3f [1e6,X] %.3f [1e7,X] %.3f top3 %.3f" %
                  (f["sup_4"], f["sup_5"], f["sup_6"], f["sup_7"], f["sup_top3"]))
            print("   M(X) at top windows:", ", ".join("%.3g:%.4g" % (x, m) for x, m in zip(f["X"][-3:], f["M"][-3:])))
