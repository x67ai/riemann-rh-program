"""fit7.py -- half-decade tables and exponents from s7gen logs (columns: bin_lo Emax Emin Erms sup|psi-x| Mgmax Mgmin
sup|Tt| sup|W| Ttrms Wrms; 20 bins per decade).  Exponents: least-squares slope of log(running sup) vs log x over the bins
of a window [10^k, Xmax) (the last, partial bin is dropped).  b_sup from sup|E| (E over real x: max(Emax, -Emin)),
b_pos from sup E, b_neg from sup(-E), b_rms from RMS of E at integers, a_sup from sup|psi_P - x|, mu from sup|M_g|.
Usage: python3 fit7.py [--half] log..."""
import sys, numpy as np
def load(fn):
    rows = [l.split() for l in open(fn) if l[0] not in '#D' and len(l.split()) == 11]
    return np.array([[float(v) for v in r] for r in rows])
def slope(x, y):
    m = (y > 0) & np.isfinite(y)
    if m.sum() < 3: return float('nan')
    A = np.vstack([np.log(x[m]), np.ones(m.sum())]).T
    return np.linalg.lstsq(A, np.log(y[m]), rcond=None)[0][0]
half = '--half' in sys.argv
for fn in [a for a in sys.argv[1:] if not a.startswith('--')]:
    d = load(fn); x = d[:, 0]
    Ep, En = d[:, 1], -d[:, 2]; Eabs = np.maximum(np.abs(d[:, 1]), np.abs(d[:, 2]))
    sE, sEp, sEn = (np.maximum.accumulate(v) for v in (Eabs, Ep, En))
    rms = d[:, 3]; sP = np.maximum.accumulate(d[:, 4]); sG = np.maximum.accumulate(np.maximum(np.abs(d[:, 5]), np.abs(d[:, 6])))
    top = x.max(); out = []
    for k in (3, 4, 5, 6, 7):
        w = (x >= 10**k) & (x < top)
        if w.sum() < 6: continue
        out.append("[1e%d,top) b_sup=%.3f b_pos=%.3f b_neg=%.3f b_rms=%.3f a_sup=%.3f mu=%.3f" % (k, slope(x[w], sE[w]), slope(x[w], sEp[w]),
                   slope(x[w], sEn[w]), slope(x[w], rms[w]), slope(x[w], sP[w]), slope(x[w], sG[w])))
    print("%s | top bin %.3g: sup|E|=%.4g supE=%.4g sup(-E)=%.4g sup|psi-x|=%.4g sup|Mg|=%.4g" % (fn.split('/')[-1], x[-2], sE[-2], sEp[-2], sEn[-2], sP[-2], sG[-2]))
    for o in out: print("   " + o)
    if half:
        print("   half-decade: x_lo  supE  infE  rmsE  sup|psi-x|  sup|Mg|  sup|Tt|  sup|W|  rmsTt  rmsW")
        hd = np.round(20 * np.log10(x)).astype(int) // 10
        for h in np.unique(hd):
            s = np.nonzero(hd == h)[0]; j = s[0]
            print("   %.3g %.4g %.4g %.4g %.4g %.4g %.4g %.4g %.4g %.4g" % (x[j], d[s, 1].max(), d[s, 2].min(), np.sqrt(np.mean(d[s, 3]**2)), d[s, 4].max(),
                  max(abs(d[s, 5]).max(), abs(d[s, 6]).max()), d[s, 7].max(), d[s, 8].max(), np.sqrt(np.mean(d[s, 9]**2)), np.sqrt(np.mean(d[s, 10]**2))))
