#!/usr/bin/env python3
"""fit_O.py — reader O's exponent fits for verify-O/data/bernO_*.csv (and the controls).

Three estimators, windows [1e4, X], [1e5, X], [1e6, X] (and [1e7, X] when X >= 1e9):
  RS  (writer-comparable): per seed, least-squares slope of log10 M(x) vs log10 x, M = running sup of |E| over bins
      up to x; reported as mean +- standard error over seeds (seed-to-seed spread).
  BS  (independent): per bin b, L_b = mean over seeds of log10(sup_{x in b}|E(x)|) (per-bin sup, not running);
      slope of L_b vs log10(hi_b); error = standard deviation of that slope over 2000 bootstrap resamples of the seeds.
  RMS (independent): as BS with the per-bin RMS of E at x = n + U, U ~ Uniform[0,1).
Usage: python3 fit_O.py data/bernO_a0.60.csv ...
"""
import sys, math
import numpy as np


def load(path):
    runs = {}
    for line in open(path):
        if line.startswith('#') or not line.strip():
            continue
        r, lo, hi, sup, mx, mn, rms, cnt = line.strip().split(',')
        if int(hi) - int(lo) < 1:
            continue  # the single-point bin at X
        runs.setdefault(r, []).append((float(lo), float(hi), float(sup), float(rms)))
    return {r: np.array(v) for r, v in runs.items()}


def slope(x, y):
    return float(np.polyfit(np.log10(x), np.log10(y), 1)[0])


def main():
    rng = np.random.default_rng(2026)
    for path in sys.argv[1:]:
        runs = load(path)
        names = sorted(runs)
        hi = runs[names[0]][:, 1]
        X = hi.max()
        a = None
        if '_a' in names[0]:
            a = float(names[0].split('_a')[1].split('_')[0])
        print('== %s  seeds=%d  X=%.3g' % (path, len(names), X))
        if a is not None:
            print('   alpha/2=%.4f  1/(4-2a)=%.4f  1/(3-a)=%.4f  2a/(a+2)=%.4f' % (a / 2, 1 / (4 - 2 * a), 1 / (3 - a), 2 * a / (a + 2)))
        S = np.array([runs[r][:, 2] for r in names])      # seeds x bins, per-bin sup
        Rm = np.array([runs[r][:, 3] for r in names])     # seeds x bins, per-bin RMS
        M = np.maximum.accumulate(S, axis=1)
        wins = [1e4, 1e5, 1e6] + ([1e7] if X >= 1e9 else [])
        for w0 in wins:
            m = hi >= w0
            rs = np.array([slope(hi[m], M[i, m]) for i in range(len(names))])
            line = '   [%.0e, X]: RS=%.4f+-%.4f' % (w0, rs.mean(), rs.std(ddof=1) / math.sqrt(len(rs)) if len(rs) > 1 else float('nan'))
            for lab, A in (('BS', S), ('RMS', Rm)):
                est = slope(hi[m], 10 ** np.log10(A[:, m]).mean(axis=0))
                boots = []
                for _ in range(2000):
                    idx = rng.integers(0, len(names), len(names))
                    boots.append(slope(hi[m], 10 ** np.log10(A[idx][:, m]).mean(axis=0)))
                line += '  %s=%.4f+-%.4f' % (lab, est, float(np.std(boots)))
            print(line)
        top = [float(M[i, -1]) for i in range(len(names))]
        print('   sup|E| on [1, X] over seeds: min %.4g  median %.4g  max %.4g' % (min(top), float(np.median(top)), max(top)))


if __name__ == '__main__':
    main()
