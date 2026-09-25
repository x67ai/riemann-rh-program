#!/usr/bin/env python3
"""witt_pairs_Z.py -- E3 (Session 28), H5: the full pairwise table on W*(Spec Z).
I_{m,n} := {a_m - a_n : a in W(Z)} (ghost coordinates). Two computations, compared:
 (A) from the Z-basis v_d = (d [d | j])_j of the ghost lattice (IV.10 rider, Opus reader): I_{m,n} = gcd{d : d divides exactly one of m, n};
 (B) from the DEFINITION: random big-Witt vectors x = (x_d), ghost map w_j = sum_{d|j} d x_d^{j/d}, gcd over samples of w_m - w_n;
 (C) the closed form of NOTE.md Theorem 3.3 transported to Z: p^{1+min(v_p(m), v_p(n))} if m and n differ at exactly one prime p, 1 otherwise.
The brief's H5 example (Gamma_2, Gamma_3) = log 6 is tested.
"""
import random, sys, time
from math import gcd, log
t0 = time.time(); NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 24; SAMPLES = 3000; R = 5
random.seed(28)
def vp(p, n):
    k = 0
    while n % p == 0: n //= p; k += 1
    return k
def primes(n): return [p for p in range(2, n + 1) if all(p % r for r in range(2, int(p ** .5) + 1))]
P = primes(NMAX)
def formA(m, n): 
    g = 0
    for d in range(1, NMAX + 1):
        if (m % d == 0) != (n % d == 0): g = gcd(g, d)
    return g
def formC(m, n):
    diff = [p for p in P if vp(p, m) != vp(p, n)]
    return P and (diff[0] ** (1 + min(vp(diff[0], m), vp(diff[0], n))) if len(diff) == 1 else 1)
G = {}
for _ in range(SAMPLES):
    x = [0] + [random.randint(-R, R) for _ in range(NMAX)]
    w = [0] + [sum(d * x[d] ** (j // d) for d in range(1, j + 1) if j % d == 0) for j in range(1, NMAX + 1)]
    for m in range(1, NMAX + 1):
        for n in range(m + 1, NMAX + 1):
            G[(m, n)] = gcd(G.get((m, n), 0), abs(w[m] - w[n]))
bad = 0; badB = 0
for m in range(1, NMAX + 1):
    for n in range(m + 1, NMAX + 1):
        A, C, B = formA(m, n), formC(m, n), G[(m, n)]
        if A != C: bad += 1; print("A != C at", m, n, A, C)
        if B != A: badB += 1; print("definition-sample gcd != basis formula at", m, n, B, A, "(box artifact if the box cannot hold a difference)")
print(f"pairs 1 <= m < n <= {NMAX}: basis formula vs closed form: {bad} mismatches; definition samples vs basis: {badB} mismatches")
for (m, n) in [(1, 2), (1, 4), (2, 4), (2, 3), (2, 6), (4, 6), (3, 9), (1, 6), (6, 12), (4, 8)]:
    A = formA(m, n); print(f"  (Gamma_{m}, Gamma_{n}): I = {A}Z, deg = log {A}" + ("  [brief's H5 said log 6: CORRECTED to 0]" if (m, n) == (2, 3) else ""))
print(f"done in {time.time()-t0:.1f}s")
