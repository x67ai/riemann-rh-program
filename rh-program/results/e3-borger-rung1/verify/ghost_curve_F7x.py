#!/usr/bin/env python3
"""ghost_curve_F7x.py -- E3 (Session 28), writer's brute-force check of H2/H3/H5 on rung 1.

Model: R = F_7[x] (the affine line A^1 over F_7 -- the brief's rehearsal ring), E = the closed points of
degree <= DMAX (monic irreducible polynomials). The E-typical Witt vectors of R over itself, by the
theorem of NOTE.md section 3 (H1, proved from Borger 0801.1691 p. 2 + section 1.8), are the ghost vectors
    L = { a in R^{N^(E)} : a_{n+e_m} = a_n  (mod m^{1+n_m})  for all m in E, n }.
Everything here is F_7-LINEAR, so L restricted to a finite index box F and to polynomial entries of
degree < D is an F_7-subspace of F_7^{D*|F|}, computed exactly as a kernel. For two indices m, n in F,
    I_{m,n} := { a_m - a_n : a in L }
is an ideal of R = F_7[x] (a PID); its generator is the gcd of the images of a spanning set of the
truncated space. Prediction (NOTE.md section 3, Theorem 3.3):
    I_{m,n} = sum over closed points P with m_P != n_P of P^{1 + min(m_P, n_P)},
i.e. P^{1+min} when exactly one P differs, the unit ideal when two or more differ. In particular
    I_{0,n} = P if n = k e_P (k >= 1), R if n has two points in its support;  deg := log #(R/I).
The truncation is harmless: the box truncation L -> L_F is surjective (NOTE.md 3.2, extension by
clipping), and D just has to exceed the degree of every generator P^{1+min} in play.
Also checks H3's count on A^1: sum_{|n| = N} deg(Gamma_0 cap Gamma_n) / log 7 = sum_{d | N} d * a_d = 7^N.
Runs in well under a minute on one process.
"""
import itertools, sys, time
from math import log
t0 = time.time()
p = 7
DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2   # closed points of degree <= DMAX
BOX  = int(sys.argv[2]) if len(sys.argv) > 2 else 2   # index box: 0 <= n_P <= BOX for each P
D    = int(sys.argv[3]) if len(sys.argv) > 3 else 7   # polynomial entries of degree < D

# --- F_7[x] arithmetic on coefficient lists (low degree first) ---
def trim(a):
    while a and a[-1] % p == 0: a.pop()
    return a
def add(a, b):
    n = max(len(a), len(b)); return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(n)])
def sub(a, b): return add(a, [(-c) % p for c in b])
def mul(a, b):
    if not a or not b: return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] = (r[i + j] + x * y) % p
    return trim(r)
def divmod_(a, b):
    a = a[:]; q = [0] * max(1, len(a) - len(b) + 1); inv = pow(b[-1], p - 2, p)
    while len(a) >= len(b) and a:
        c = a[-1] * inv % p; k = len(a) - len(b); q[k] = c
        for i, y in enumerate(b): a[k + i] = (a[k + i] - c * y) % p
        trim(a)
    return trim(q), a
def gcd(a, b):
    while b: a, b = b, divmod_(a, b)[1]
    if a: inv = pow(a[-1], p - 2, p); a = [c * inv % p for c in a]
    return a
def powpoly(a, k):
    r = [1]
    for _ in range(k): r = mul(r, a)
    return r
def irreducibles(dmax):
    out = []
    for d in range(1, dmax + 1):
        for coeffs in itertools.product(range(p), repeat=d):
            f = list(coeffs) + [1]
            if any(divmod_(f, g)[1] == [] for g in out if len(g) - 1 <= d // 2): continue
            out.append(f)
    return out
E_all = irreducibles(DMAX)
a_d = {d: sum(1 for f in E_all if len(f) - 1 == d) for d in range(1, DMAX + 1)}
print(f"R = F_7[x]: closed points of degree d <= {DMAX}: a_d = {a_d}")
# the lattice is computed on the sub-box of indices supported on three chosen closed points
# (x), (x + 1), (x^2 + 1) [x^2 + 1 irreducible: -1 is a non-square mod 7]; clipping to a sub-box is surjective (NOTE.md 3.2)
E = [[0, 1], [1, 1], [1, 0, 1]]
degs = [len(f) - 1 for f in E]
assert all(f in E_all for f in E)
print(f"index sub-box on E' = {{(x), (x+1), (x^2+1)}}, degrees {degs}, 0 <= n_P <= {BOX}")
# index box
F = list(itertools.product(range(BOX + 1), repeat=len(E)))
idx = {n: i for i, n in enumerate(F)}
NV = D * len(F)   # unknowns: coefficient c_{n,i} of x^i in a_n
# congruence a_{n+e_P} - a_n in P^{1+n_P}: the remainder of (a_{n+e_P} - a_n) modulo P^{1+n_P} is zero,
# an F_7-linear condition on the coefficients: build the matrix by evaluating on basis vectors.
rows = []
for n in F:
    for j, P in enumerate(E):
        if n[j] + 1 > BOX: continue
        n2 = tuple(n[i] + (1 if i == j else 0) for i in range(len(E)))
        M = powpoly(P, 1 + n[j]); dm = len(M) - 1
        if D <= dm: continue   # nothing to impose beyond degree (never happens for our parameters, guard only)
        # each coefficient of the remainder is a linear form; compute columns
        cols = {}
        for (nn, sign) in ((n2, 1), (n, -1)):
            for i in range(D):
                r = divmod_([0] * i + [1], M)[1]
                for k, c in enumerate(r):
                    if c: cols[(idx[nn] * D + i, k)] = (cols.get((idx[nn] * D + i, k), 0) + sign * c) % p
        for k in range(dm):
            row = [0] * NV
            for (col, kk), c in cols.items():
                if kk == k: row[col] = c
            if any(row): rows.append(row)
# kernel over F_7 by Gaussian elimination
def kernel(rows, nv):
    rows = [r[:] for r in rows]; piv = []; r0 = 0
    for c in range(nv):
        pr = next((i for i in range(r0, len(rows)) if rows[i][c]), None)
        if pr is None: continue
        rows[r0], rows[pr] = rows[pr], rows[r0]; inv = pow(rows[r0][c], p - 2, p)
        rows[r0] = [v * inv % p for v in rows[r0]]
        for i in range(len(rows)):
            if i != r0 and rows[i][c]:
                f = rows[i][c]; rows[i] = [(vi - f * vr) % p for vi, vr in zip(rows[i], rows[r0])]
        piv.append(c); r0 += 1
        if r0 == len(rows): break
    free = [c for c in range(nv) if c not in piv]; basis = []
    for fc in free:
        v = [0] * nv; v[fc] = 1
        for i, pc in enumerate(piv): v[pc] = (-rows[i][fc]) % p
        basis.append(v)
    return basis
K = kernel(rows, NV)
print(f"index box {len(F)} indices, entries deg < {D}: {len(rows)} linear conditions, kernel dimension {len(K)} over F_7  [{time.time()-t0:.1f}s]")
def comp(v, n): return trim(v[idx[n] * D: idx[n] * D + D][:])
def ideal_gen(m, n):
    g = []
    for v in K: g = gcd(g, sub(comp(v, m), comp(v, n)))
    return g
def predicted(m, n):
    diff = [j for j in range(len(E)) if m[j] != n[j]]
    if len(diff) != 1: return [1]            # two or more differing points: the sum of coprime ideals is R
    j = diff[0]; return powpoly(E[j], 1 + min(m[j], n[j]))
def pstr(f):
    if not f: return "0"
    return " + ".join(f"{c}x^{i}" if i else f"{c}" for i, c in enumerate(f) if c)
zero = tuple([0] * len(E)); bad = 0; shown = 0
# H2 / H5: every pair (m, n) in the box
pairs = [(m, n) for m in F for n in F if m < n]
for m, n in pairs:
    g = ideal_gen(m, n); pr = predicted(m, n)
    if g != pr: bad += 1; print("MISMATCH", m, n, pstr(g), "predicted", pstr(pr))
print(f"pairs checked: {len(pairs)}; mismatches against Theorem 3.3: {bad}")
# print the diagonal row (Gamma_0 against every Gamma_n) with degrees
print("Gamma_0 cap Gamma_n, n in the box (|n| = sum n_P deg P; deg = log_7 #(R/I) in units of log 7):")
for n in F:
    if n == zero: continue
    g = ideal_gen(zero, n); absn = sum(n[j] * degs[j] for j in range(len(E)))
    print(f"  n = {n}  |n| = {absn}  I_0,n = ({pstr(g)})  deg/log7 = {len(g)-1}")
# H3 count on A^1 (P^1 minus infinity): sum_{|n|=N} deg = sum_{d|N} d a_d = 7^N (all n of degree N supported at one point)
for N in range(1, DMAX + 1):
    s = sum(d * a_d[d] for d in a_d if N % d == 0)   # one index n = (N/deg P) e_P per closed point P with deg P | N, each of degree deg P
    print(f"  N = {N}: sum over |n| = N of deg(Gamma_0 cap Gamma_n)/log 7 = sum_(d|N) d a_d = {s}; #A^1(F_7^{N}) = {7**N}  {'OK' if s == 7**N else 'FAIL'}")
print(f"done in {time.time()-t0:.1f}s")
