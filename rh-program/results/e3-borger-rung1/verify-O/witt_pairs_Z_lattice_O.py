#!/usr/bin/env python3
"""witt_pairs_Z_lattice_O.py -- E3 reader (Opus 5), Session 28: H5 corrected closed form on W*(Spec Z).

A DIFFERENT enumeration from the writer's witt_pairs_Z.py (which used the basis v_d, random Witt
components through the ghost polynomials, and the closed form). Here the ghost lattice of W(Z),
truncated to the BOX of divisors of B = 5040 = 2^4 3^2 5 7 (60 indices), is taken from Borger's PRINTED congruences
(0801.1691 Sec. 1.10 p. 10: a_j == a_{pj} mod p^(1+ord_p(j)) for all j >= 1 and all primes p),
and an exact Z-basis of that lattice is computed by integer column reduction (extended-gcd
Hermite reduction of [C | -diag(moduli)], its integer kernel projected to the box coordinates).
Then I_{m,n} = {a_m - a_n : a in L} = g Z with g = gcd over the basis, for every pair m < n in the box,
compared with the writer's corrected closed form:
    g = p^(1 + min(v_p(m), v_p(n)))  if m and n differ at exactly one prime p,  g = 1 otherwise,
including the brief's example (Gamma_2, Gamma_3): predicted g = 1 (degree 0), not 6.
Truncation to a box is exact (NOTE Lemma 3.2's clipping argument, re-checked by the reader: extend a
vector on the box by a_j := a_{gcd(j, B)} -- at a prime p with v_p(j) >= v_p(B) both j and pj clip to the
same index; otherwise the step is a step inside the box with the same p-coordinate).
"""
import sys, time
from math import gcd
t0 = time.time()
B = int(sys.argv[1]) if len(sys.argv) > 1 else 5040
IDX = [d for d in range(1, B + 1) if B % d == 0]
POS = {d: i for i, d in enumerate(IDX)}
M = B

def vp(p, n):
    k = 0
    while n % p == 0:
        n //= p; k += 1
    return k
primes = [p for p in range(2, 60) if all(p % r for r in range(2, int(p ** .5) + 1))]
cons = []  # (pos j, pos pj, modulus)
for j in IDX:
    for p in primes:
        if B % (p * j) == 0:
            cons.append((POS[j] + 1, POS[p * j] + 1, p ** (1 + vp(p, j))))
R = len(cons); D = len(IDX)
ncols = D + R
# matrix rows: for constraint r: a_j - a_pj - mod_r * b_r = 0
A = [[0] * ncols for _ in range(R)]
for r, (j, pj, mod) in enumerate(cons):
    A[r][j - 1] += 1; A[r][pj - 1] -= 1; A[r][D + r] = -mod
# column reduction: maintain U (ncols x ncols) with A*U = H
U = [[1 if i == k else 0 for k in range(ncols)] for i in range(ncols)]
def colop(c1, c2, a, b, c, d):  # (col c1, col c2) <- (a*c1 + b*c2, c*c1 + d*c2)
    for Mx in (A, U):
        for row in Mx:
            u, v = row[c1], row[c2]
            row[c1], row[c2] = a * u + b * v, c * u + d * v
def egcd(a, b):
    if b == 0: return (a, 1, 0) if a >= 0 else (-a, -1, 0)
    g, s, t = egcd(b, a % b)
    return g, t, s - (a // b) * t
piv = 0
for r in range(R):
    for c in range(piv + 1, ncols):
        if A[r][c] != 0:
            u, v = A[r][piv], A[r][c]
            g, s, t = egcd(u, v)
            # new piv col = s*piv + t*c ; new c col = (-v/g)*piv + (u/g)*c  (unimodular)
            colop(piv, c, s, t, -v // g, u // g)
    if A[r][piv] != 0:
        piv += 1
# kernel columns: columns >= piv of U (A*U has zeros there)
kernel = [[U[i][c] for i in range(ncols)] for c in range(piv, ncols)]
# verify kernel vectors satisfy the congruences
for kv in kernel:
    a = kv[:D]
    for (j, pj, mod) in cons:
        assert (a[j - 1] - a[pj - 1]) % mod == 0
basis = [kv[:D] for kv in kernel]
print(f"box = divisors of {B} ({D} indices): {R} printed congruences, integer kernel rank {len(kernel)} (projected generators of L)  [{time.time()-t0:.2f}s]", flush=True)
def closed(m, n):
    diff = [p for p in primes if vp(p, m) != vp(p, n)]
    return diff[0] ** (1 + min(vp(diff[0], m), vp(diff[0], n))) if len(diff) == 1 else 1
mism = 0; tot = 0
for i, m in enumerate(IDX):
    for n in IDX[i + 1:]:
        g = 0
        for a in basis:
            g = gcd(g, a[POS[m]] - a[POS[n]])
        tot += 1
        if g != closed(m, n):
            mism += 1; print(f"MISMATCH ({m},{n}): lattice {g} vs closed form {closed(m, n)}")
print(f"pairs m < n in the box: {tot}; mismatches lattice vs closed form: {mism}")
for (m, n) in [(1, 2), (1, 4), (2, 4), (2, 3), (2, 6), (3, 9), (4, 12), (6, 12), (8, 24), (5, 35), (10, 15), (1, 6), (16, 48), (9, 63)]:
    g = 0
    for a in basis: g = gcd(g, a[POS[m]] - a[POS[n]])
    print(f"  (Gamma_{m}, Gamma_{n}): I = {g}Z   closed form {closed(m, n)}")
print(f"done in {time.time()-t0:.2f}s")
