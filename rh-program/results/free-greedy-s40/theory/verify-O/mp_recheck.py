# Opus reader: recheck at 60 digits every S8 decision whose double-double relative margin is < 1e-12.
# Input: s8dd_<R>_<X>.close.txt (decision kind, composite value, count N) and path_<R>_<X>.txt (factorization
# as lattice indices n_k, g-prime = 1 + (n_k - 1/2) t).  Decision "below-threshold": composite < 1 + (N - 1/2) t.
# Decision "after-prime": the prime 1 + (N - 1 - 1/2) t was placed first, i.e. it is < composite.
import mpmath as mp, sys, os
mp.mp.dps = 60
print("# dd_err compares the 60-digit product with the %.17g DECIMAL printout of the double-double value; it is limited (~1e-17)\n# by that printout, not by the arithmetic. The decision itself is recomputed from the factorization alone.")
TV = {"pi16": 16/mp.pi, "pi4": 4/mp.pi, "pi32": 32/mp.pi}
here = os.path.dirname(os.path.abspath(__file__))
for R, X in [("pi16", "1e7"), ("pi4", "1e7"), ("pi32", "1e8")]:
    t = TV[R]
    paths = {}
    for l in open(os.path.join(here, f"path_{R}_{X}.txt")):
        p = l.split(); paths[(p[1], p[2])] = [int(v) for v in p[4:]]
    worst_err, ok, n = 0, 0, 0
    for l in open(os.path.join(here, f"s8dd_{R}_{X}.audit.close.txt")):
        p = l.split(); kind = p[1]; hi = p[2].split("=")[1]; lo = p[3]; N = int(p[4].split("=")[1])
        ns = paths[(hi, lo)]
        c = mp.fprod([1 + (k - mp.mpf(1)/2) * t for k in ns])
        M = N if kind == "below-threshold" else N - 1
        L = 1 + (M - mp.mpf(1)/2) * t
        good = (c < L) if kind == "below-threshold" else (c > L)
        err = abs(c - (mp.mpf(hi) + mp.mpf(lo))) / c
        worst_err = max(worst_err, err); ok += good; n += 1
        print(f"{R} {X} {kind:16s} c={mp.nstr(c, 22)} factors={len(ns)} lattice M={M} rel.margin(60 dig)={mp.nstr(abs(c-L)/c, 6)} decision_ok={good} dd_err={mp.nstr(err, 3)}")
    print(f"SUMMARY {R} {X}: {ok}/{n} decisions confirmed at 60 digits; worst double-double relative error {mp.nstr(worst_err, 3)}")
