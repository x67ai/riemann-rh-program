#!/usr/bin/env python3
"""read-O check of NOTE §3.6 (cluster lemma) on R_tight and of the read-O ADD (Selberg-sieve cluster bound), own code.
R_tight: for each N >= 1 the first c_N = M(2,N) primes after 4^N.  Route (different from a sieve): N_P(y) by inclusion-exclusion
N_P(y) = sum_{m in <R>, m <= y} mu(m) floor(y/m), <R> enumerated by depth-first search; rho from the cyclotomic identity:
rho = prod_{N<=NM} prod_j (1-1/r_{N,j}) * (1/2) / prod_{N<=NM}(1-4^-N)^{c_N}  (tail correction ~1e-15, ignored).
For each N: h_N (cluster span), E(4^N), E(4^N+h_N), the exact jump, and the exact sieve deviation
S(I, P_{<N}) - rho_{<N} h on I = (4^N, 4^N+h_N] (interval sieved directly), against h^{2/3}."""
import sys, numpy as np, mpmath as mp
from o_rung1_bruteforce import necklace
from o_zeta_checks import is_prime
mp.mp.dps = 40
NM = int(sys.argv[1]) if len(sys.argv) > 1 else 15
clusters = {}
for N in range(1, NM + 1):
    c, m, lst = necklace(2, N), 4 ** N, []
    while len(lst) < c:
        m += 1
        if is_prime(m): lst.append(m)
    clusters[N] = lst
R = sorted(r for N in clusters for r in clusters[N])
Y = max(R) + 1
# squarefree R-numbers <= Y with Moebius signs, by DFS
ms, mus = [], []
def dfs(start, prod, sign):
    ms.append(prod); mus.append(sign)
    for i in range(start, len(R)):
        p = R[i]
        if prod * p > Y: break
        dfs(i + 1, prod * p, -sign)
sys.setrecursionlimit(10000)
dfs(0, 1, 1)
ms = np.array(ms, dtype=np.int64); mus = np.array(mus, dtype=np.int64)
lr = mp.mpf(0)
for r in R: lr += mp.log1p(-mp.mpf(1) / r)
for N in range(1, NM + 1): lr -= necklace(2, N) * mp.log1p(-mp.mpf(4) ** (-N))
rho = mp.e ** lr / 2
def NP(y): return int(np.sum(mus * (y // ms)))
def E(y): return mp.mpf(NP(y)) - rho * y
print(f"R_tight N<= {NM}: |R| = {len(R)}, #<R> cap [1,{Y}] = {len(ms)}, rho = {mp.nstr(rho, 20)}")
for N in range(4, NM + 1):
    lo, cl = 4 ** N, clusters[N]; h = cl[-1] - lo; c = len(cl)
    small = [r for r in R if r < lo]
    # exact count of n in (lo, lo+h] coprime to all smaller R-primes
    I = np.ones(h, dtype=bool)                       # index k <-> n = lo + 1 + k
    for p in small:
        first = ((lo + 1 + p - 1) // p) * p
        I[first - lo - 1::p] = False
    S = int(I.sum()); rz = mp.mpf(1)
    for p in small: rz *= (1 - mp.mpf(1) / p)
    dev = S - rz * h
    e0, e1 = E(lo), E(lo + h)
    print(f"N={N:2d} c={c:5d} h/(c ln4^N)={h / (c * N * mp.log(4)):.3f} E(4^N)={mp.nstr(e0, 6):>9} "
          f"E(4^N+h)={mp.nstr(e1, 6):>9} jump/c={mp.nstr((e1 - e0) / c, 4)} sieve dev={mp.nstr(dev, 5)} "
          f"h^(2/3)={h ** (2 / 3):.0f} (rho_z-rho)h={mp.nstr((rz - rho) * h, 4)}")
    sys.stdout.flush()
