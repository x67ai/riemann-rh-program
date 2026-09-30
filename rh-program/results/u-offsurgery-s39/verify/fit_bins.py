"""fit_bins.py -- exponents from log-binned logs (columns: bin_lo Emax Emin Erms sup|psi-x|).
beta route 1: slope of log(running sup |E|) vs log x; route 2: slope of log(RMS E).
alpha: slope of log(running sup |psi-x|). Windows [10^k, Xmax], k = 3..6.  Usage: python3 fit_bins.py log..."""
import sys, numpy as np
def load(fn):
    rows = [l.split() for l in open(fn) if l[0] != '#']
    return np.array([[float(v) for v in r] for r in rows])
def slope(x, y):
    m = (y > 0) & np.isfinite(y)
    A = np.vstack([np.log(x[m]), np.ones(m.sum())]).T
    return np.linalg.lstsq(A, np.log(y[m]), rcond=None)[0][0]
for fn in sys.argv[1:]:
    d = load(fn); x = d[:, 0]; E = np.maximum(np.abs(d[:, 1]), np.abs(d[:, 2]))
    supE = np.maximum.accumulate(E); rms = d[:, 3]; supP = np.maximum.accumulate(d[:, 4])
    out = []
    for k in (3, 4, 5, 6):
        w = (x >= 10**k) & (x < x.max())
        out.append("[1e%d] b_sup=%.3f b_rms=%.3f a_sup=%.3f" % (k, slope(x[w], supE[w]), slope(x[w], rms[w]), slope(x[w], supP[w])))
    print(fn.split('/')[-1], "| top: supE=%.4g supPsi=%.4g |" % (supE[-2], supP[-2]), " ; ".join(out))
