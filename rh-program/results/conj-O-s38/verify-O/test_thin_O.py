#!/usr/bin/env python3
"""Checks for thin_O.py at small X: (1) segmented sieve == simple sieve; (2) bins == brute force from the deleted set."""
import sys, math, numpy as np
sys.path.insert(0, ".")
import thin_O
Y = 4 * 10**6
seg = np.concatenate(list(thin_O.prime_segments(Y, seg=333337)))
ref = thin_O.base_primes(Y)
print("segmented sieve == simple sieve:", np.array_equal(seg, ref), seg.size)
out = "data/test_a0.75_s7_1e6"
dX = np.load(out + "_Rprimes.npy"); X = 10**6
hdr = open(out + "_dec.csv").readline(); rho = float(hdr.split("rho=")[1].split()[0])
f = np.ones(X + 1, dtype=bool); f[0] = False
for p in dX.tolist(): f[p::p] = False
N = np.cumsum(f); n = np.arange(X + 1)
rows = np.loadtxt(out + "_dec.csv", delimiter=",", comments="#")
bad = 0
for lo, hi, mx, mn, s2, ct in rows:
    lo, hi = int(lo), int(hi); sl = slice(lo, hi + 1)
    Ep = N[sl] - rho * n[sl]; Em = Ep - rho; Ec = Ep - rho / 2
    ok = abs(Ep.max() - mx) < 1e-5 and abs(Em.min() - mn) < 1e-5 and abs((Ec * Ec).sum() - s2) <= 1e-8 * max(1, s2) and ct == hi - lo + 1
    bad += (not ok)
print("dec bins checked:", len(rows), "mismatches:", bad, " N(X) =", int(N[X]))
