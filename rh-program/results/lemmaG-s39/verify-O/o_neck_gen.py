#!/usr/bin/env python3
"""read-O: R_tight (first c_N = M(2,N) primes after 4^N) up to 1e10 and its rho: exact product over N <= 16, cyclotomic tail
prod_{N>16}(1-4^-N)^{c_N} = (1/2)/prod_{N<=16}(...), times the first-order correction exp(sum_{N>16} c_N^2 ln(4^N)/(2*16^N))
for r_{N,j} - 4^N ~ j ln 4^N (a model, relative effect ~3e-12; its own error ~1e-14)."""
import sys
sys.argv = ['x', '16']
import mpmath as mp
import o_cluster_check as cc
from o_rung1_bruteforce import necklace
mp.mp.dps = 40
R = sorted(r for N in cc.clusters for r in cc.clusters[N] if r <= 10 ** 10)
corr = sum(mp.mpf(necklace(2, N)) ** 2 * N * mp.log(4) / (2 * mp.mpf(16) ** N) for N in range(17, 80))
rho = cc.rho * mp.e ** corr
open("/private/tmp/rh-s40-lemmaG/R_neck_1e10.txt", "w").write("\n".join(map(str, R)) + "\n")
hi = float(rho); lo = float(rho - mp.mpf(hi))
open("/private/tmp/rh-s40-lemmaG/rho_neck_1e10.txt", "w").write(f"{mp.nstr(rho, 35)}\n{hi!r}\n{lo!r}\n")
print(f"|R_tight cap [1,1e10]| = {len(R)}, rho (cyclotomic) = {mp.nstr(cc.rho, 22)}, tail corr = {mp.nstr(corr, 6)}, rho = {mp.nstr(rho, 22)}")
