#!/usr/bin/env python3
"""analyze.py — error statistics for one run: E(e) = N(e) - rho*e at the bin edges e = 2^j (1 + (i+1)/K), e <= X.
Per dyadic block j (edges in (2^j, 2^{j+1}]): A_j = max|E|, M_j = running max of A, MS_j = mean E^2 (dyadic mean square),
mean_j = mean E, pos_j = fraction of E > 0; xm_j = mean edge of the block (partial top block too). Slopes (least squares, log10-log10) over windows [10^a, X], a = 3..6:
  sup  : log M_j vs log x_j        (x_j = top edge of block j)       -> beta
  supL : log(M_j sqrt(log x_j))                                     -> beta, with the predicted (log x)^{-1/2}
  ms   : log MS_j vs log xm_j / 2  (xm_j = 1.5 * 2^j)               -> beta (half the mean-square slope)
  msL  : log(MS_j log xm_j) / 2
Also nrm_j = MS_j / (xm_j / log xm_j) (the one-scale prediction is O(1)).
Usage: analyze.py RUNPREFIX  (reads RUNPREFIX.i64 + RUNPREFIX.json [rho, X, K, J]) -> RUNPREFIX.stats.json
"""
import sys, json, math
import numpy as np

WINDOWS = [3, 4, 5, 6]

def slope(x, y):
    m = (y > 0) & np.isfinite(y)
    if m.sum() < 4:
        return float("nan")
    return float(np.polyfit(np.log10(x[m]), np.log10(y[m]), 1)[0])

def run_stats(prefix, rho=None, X=None, K=1024, J=27):
    meta = json.load(open(prefix + ".json"))
    rho = meta["rho"] if rho is None else rho
    X = meta["X"] if X is None else X
    K = meta.get("K", K); J = meta.get("J", J)
    c = np.fromfile(prefix + ".i64", dtype=np.int64)
    assert c.size == K * J
    j = np.repeat(np.arange(J), K); i = np.tile(np.arange(K), J)
    e = np.ldexp(1.0 + (i + 1) / K, j)
    N = 1 + np.cumsum(c)
    keep = e <= X
    E = N[keep] - rho * e[keep]; jj = j[keep]; ee = e[keep]
    blocks = []
    for b in range(1, J):
        m = jj == b
        if m.sum() < K // 4:
            continue
        Eb = E[m]
        blocks.append(dict(j=b, x=float(ee[m].max()), xm=float(ee[m].mean()), n=int(m.sum()),
                           A=float(np.abs(Eb).max()), MS=float(np.mean(Eb ** 2)), mean=float(Eb.mean()),
                           pos=float(np.mean(Eb > 0))))
    A = np.array([b["A"] for b in blocks]); Mrun = np.maximum.accumulate(A)
    for b, mr in zip(blocks, Mrun):
        b["M"] = float(mr)
        b["nrm"] = b["MS"] / (b["xm"] / math.log(b["xm"]))
    x = np.array([b["x"] for b in blocks]); xm = np.array([b["xm"] for b in blocks])
    MS = np.array([b["MS"] for b in blocks])
    res = {}
    for a in WINDOWS:
        w = x >= 10.0 ** a
        res["1e%d" % a] = dict(
            sup=slope(x[w], Mrun[w]), supL=slope(x[w], Mrun[w] * np.sqrt(np.log(x[w]))),
            ms=0.5 * slope(xm[w], MS[w]), msL=0.5 * slope(xm[w], MS[w] * np.log(xm[w])))
    out = dict(prefix=prefix, rho=rho, X=X, blocks=blocks, slopes=res,
               top=dict(E_at_X=float(E[-1]), maxabsE=float(np.abs(E).max()), N_at_X=int(N[keep][-1])))
    json.dump(out, open(prefix + ".stats.json", "w"), indent=1)
    return out

if __name__ == "__main__":
    o = run_stats(sys.argv[1])
    print(json.dumps(o["slopes"]), json.dumps(o["top"]))
