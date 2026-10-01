#!/usr/bin/env python3
"""cluster_check.py — Lemma 3.6 (cluster lemma) on the tight Q-necklace R_tight (first M(2,N) primes after 4^N), N <= 16 (R-list of
the 1e10 run). For each N: c_N, the span h_N of the cluster, h_N / (c_N ln 4^N), and the lemma's guaranteed jump
J_N = c_N - 2^{pi_R(z)} - (rho_z - rho) h_N with z = 4^{N_z} chosen to maximize J_N; then the measured max |E| over the bins
containing [4^N, 4^N + h_N] (from the run's bins) — the lemma says max(|E(y)|, |E(y+h)|) >= J_N / 2."""
import math, numpy as np
R = sorted(int(l) for l in open("data/R_neck_a2_1e+10.txt"))
head = open("data/neck2_1e10.csv").readline(); rho = float(head.split(" rho=")[1].split()[0])
bins = [l.strip().split(",") for l in open("data/neck2_1e10.csv") if not l.startswith("#")]
blo = np.array([int(b[1]) for b in bins]); bhi = np.array([int(b[2]) for b in bins]); bmx = np.array([float(b[3]) for b in bins]); bmn = np.array([float(b[4]) for b in bins])
def M(N):
    from sympy import mobius
    return sum(mobius(N // d) * 2 ** d for d in range(1, N + 1) if N % d == 0) // N
cl = {}
for r in R:
    N = int(math.log(r, 4)) if 4 ** int(math.log(r, 4)) <= r else int(math.log(r, 4)) - 1
    while 4 ** (N + 1) <= r: N += 1
    while 4 ** N > r: N -= 1
    cl.setdefault(N, []).append(r)
print(" N   c_N   h_N        h/(c ln4^N)  J_N(best z)   J/2      max|E| near cluster   ratio max|E|/c_N")
for N in sorted(cl):
    c = cl[N]; assert len(c) == M(N), (N, len(c), M(N))
    h = c[-1] - 4 ** N; best = -1e18
    for Nz in range(0, N):
        small = [r for r in R if r < 4 ** (Nz + 1)]; z_count = len(small)
        if z_count > 60: break
        rho_z = math.prod(1 - 1 / r for r in small); J = len(c) - 2 ** z_count - (rho_z - rho) * h
        best = max(best, J)
    sel = (bhi >= 4 ** N) & (blo <= 4 ** N + h + 1)
    mE = max(bmx[sel].max(), -bmn[sel].min())
    print("%2d %6d %10d   %6.3f      %9.1f  %8.1f   %12.1f          %.3f" % (N, len(c), h, h / (len(c) * N * math.log(4)), best, best / 2, mE, mE / len(c)))
