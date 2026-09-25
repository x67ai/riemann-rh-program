#!/usr/bin/env python3
"""curve_ghost_groebner_O.py -- E3 reader (Opus 5), Session 28.

A DIFFERENT enumeration from the writer's verify/ scripts:
 (1) Point counts N_1..N_4 of S: y^2 = x^3 + x + 1 over F_7 by the quadratic-character sum
     N_d = q^d + 1 + sum_{x in F_{q^d}} chi(f(x)), chi(z) = z^((q^d-1)/2) (Euler's criterion),
     with F_{7^d} built from an irreducible polynomial found here; a_d by Moebius inversion.
 (2) The ghost-diagonal ideals computed ON THE CURVE ITSELF (the writer computed on F_7[x] only):
     R = F_7[x, y]/(y^2 - x^3 - x - 1); a finite set E' of closed points of several shapes and degrees
     (degree 1; degree 2 of shape (g2(x), y - h(x)); degree 2 of shape (x - x0, y^2 - c);
     degree 3 of shape (g3(x), y - h(x)); degree 4 of shape (g2(x), y^2 - r(x))); a box F;
     J = prod m^(1 + b_m); the ghost lattice L_F / J R^F inside (R/J)^F cut out by the congruences
     a_{j+e_m} - a_j in m^(1+j_m) (Theorem 3.1, re-derived by hand by the reader), with every quotient
     R/(m^k + J) computed by a Groebner basis over GF(7) (sympy), not by CRT or local models.
     Then for EVERY pair (m, n) in F: codim_{F_7} of {a_m - a_n} + J in R, compared with Theorem 3.3:
     deg(m-point) * (1 + min(m_P, n_P)) if m, n differ at exactly one point P, else 0.
 (3) An enumeration of ALL effective divisors n of degree N = 1..4 (points labeled, a_d of each degree),
     summing deg(Gamma_0 cap Gamma_n)/log 7 by the rule verified in (2); compared with N_N from (1)
     and with the record 5, 55, 380, 2475.
"""
import sys, time, itertools
from functools import reduce
import numpy as np
import sympy as sp

t0 = time.time()
P = 7
x, y = sp.symbols('x y')
F = x**3 + x + 1
CURVE = y**2 - F

def log(msg):
    print(msg, flush=True)

# ---------------- (1) point counts by character sums ----------------
def poly_irreducible_mod_p(coeffs):  # coeffs low->high, monic, over F_P
    g = sp.Poly(list(reversed(coeffs)), x, modulus=P)
    return g.is_irreducible

def find_irreducible(d):
    for tail in itertools.product(range(P), repeat=d):
        c = list(tail) + [1]
        if c[0] == 0:
            continue
        if poly_irreducible_mod_p(c):
            return c
    raise RuntimeError

def field_elems(d, mod):  # elements as tuples length d; arithmetic mod (mod)
    return itertools.product(range(P), repeat=d)

def fmul(a, b, mod, d):
    r = [0] * (2 * d - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                r[i + j] = (r[i + j] + ai * bj) % P
    for k in range(2 * d - 2, d - 1, -1):  # reduce by monic mod
        c = r[k]
        if c:
            for i in range(d + 1):
                r[k - d + i] = (r[k - d + i] - c * mod[i]) % P
    return tuple(r[:d])

def fpow(a, e, mod, d):
    res = tuple([1] + [0] * (d - 1)); base = a
    while e:
        if e & 1: res = fmul(res, base, mod, d)
        base = fmul(base, base, mod, d); e >>= 1
    return res

def count_points(d):
    if d == 1:
        mod = [0, 1]
    else:
        mod = find_irreducible(d)
    one = tuple([1] + [0] * (d - 1)); zero = tuple([0] * d)
    e = (P ** d - 1) // 2
    s = 0
    for a in field_elems(d, mod):
        a = tuple(a)
        if d == 1:
            v = ((a[0] ** 3 + a[0] + 1) % P,)
        else:
            a3 = fmul(fmul(a, a, mod, d), a, mod, d)
            v = tuple((a3[i] + a[i] + one[i]) % P for i in range(d))
        if v == zero:
            continue
        c = fpow(v, e, mod, d) if d > 1 else ((v[0] ** e) % P,)
        s += 1 if c == one else -1
    return P ** d + 1 + s

def mobius(n):
    r, m, p = 1, n, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0: return 0
            r = -r
        p += 1
    return -r if m > 1 else r

NN = {}
for d in range(1, 5):
    NN[d] = count_points(d)
a = {d: sum(mobius(d // e) * NN[e] for e in range(1, d + 1) if d % e == 0) // d for d in range(1, 5)}
log(f"(1) character sums: N_1..N_4 = {[NN[d] for d in range(1,5)]}  (record: [5, 55, 380, 2475]);  a_1..a_4 = {[a[d] for d in range(1,5)]}  [{time.time()-t0:.1f}s]")
assert [NN[d] for d in range(1, 5)] == [5, 55, 380, 2475]

# ---------------- (2) ghost lattice on the curve via Groebner bases ----------------
def gb(gens):
    return sp.groebner(list(gens) + [CURVE], x, y, modulus=P, order='grevlex')

def std_monomials(G, bound=40):
    lead = [sp.Poly(g, x, y, modulus=P).monoms(order='grevlex')[0] for g in G.exprs]
    mons = []
    for i in range(bound):
        for j in range(bound):
            if not any(i >= l[0] and j >= l[1] for l in lead):
                mons.append((i, j))
    assert all(i < bound - 1 and j < bound - 1 for i, j in mons)
    return mons

def coords(expr, G, mons):
    r = G.reduce(sp.expand(expr))[1]
    pr = sp.Poly(r, x, y, modulus=P)
    idx = {m: k for k, m in enumerate(mons)}
    v = [0] * len(mons)
    for mon, c in zip(pr.monoms(), pr.coeffs()):
        v[idx[mon]] = int(c) % P
    return v

def ideal_power(gens, k):
    out = [sp.Integer(1)]
    for _ in range(k):
        out = [sp.expand(u * g) for u in out for g in gens]
    return out

def ideal_product(list_of_gens):
    return reduce(lambda A, B: [sp.expand(u * v) for u in A for v in B], list_of_gens)

def find_points():
    pts = []
    # degree 1
    for x0 in range(P):
        for y0 in range(P):
            if (y0 * y0 - (x0 ** 3 + x0 + 1)) % P == 0:
                pts.append(("deg1", 1, [x - x0, y - y0], f"(x-{x0}, y-{y0})"))
    deg1 = pts[:2]
    # degree 2, shape (g2, y - h)
    q2 = None
    for c0, c1 in itertools.product(range(P), repeat=2):
        g = x ** 2 + c1 * x + c0
        if not sp.Poly(g, x, modulus=P).is_irreducible: continue
        for h0, h1 in itertools.product(range(P), repeat=2):
            h = h1 * x + h0
            if sp.Poly(sp.rem(sp.expand(h * h - F), g, x, modulus=P), x, modulus=P).is_zero:
                q2 = ("deg2a", 2, [g, y - h], f"({g}, y-({h}))"); break
        if q2: break
    # degree 2, shape (x - x0, y^2 - c), c non-square
    squares = {(t * t) % P for t in range(P)}
    q2b = None
    for x0 in range(P):
        c = (x0 ** 3 + x0 + 1) % P
        if c not in squares:
            q2b = ("deg2b", 2, [x - x0, y ** 2 - c], f"(x-{x0}, y^2-{c})"); break
    # degree 3, shape (g3, y - h)
    q3 = None
    for cs in itertools.product(range(P), repeat=3):
        g = x ** 3 + cs[2] * x ** 2 + cs[1] * x + cs[0]
        if not sp.Poly(g, x, modulus=P).is_irreducible: continue
        for hs in itertools.product(range(P), repeat=3):
            h = hs[2] * x ** 2 + hs[1] * x + hs[0]
            if sp.Poly(sp.rem(sp.expand(h * h - F), g, x, modulus=P), x, modulus=P).is_zero:
                q3 = ("deg3", 3, [g, y - h], f"({g}, y-({h}))"); break
        if q3: break
    # degree 4, shape (g2, y^2 - r), r = F mod g2 a non-square in F_49
    q4 = None
    for c0, c1 in itertools.product(range(P), repeat=2):
        g = x ** 2 + c1 * x + c0
        if not sp.Poly(g, x, modulus=P).is_irreducible: continue
        r = sp.rem(F, g, x, modulus=P)
        # test: r(alpha) non-square in F_49 <=> r^((49-1)/2) != 1 mod g
        t = sp.Poly(sp.rem(sp.expand(r) ** 24, g, x, modulus=P), x, modulus=P)
        if t != sp.Poly(1, x, modulus=P) and not sp.Poly(r, x, modulus=P).is_zero:
            if q2 is not None and sp.expand(g - q2[2][0]) == 0: continue
            q4 = ("deg4", 4, [g, y ** 2 - r], f"({g}, y^2-({r}))"); break
    return deg1, q2, q2b, q3, q4

deg1, q2, q2b, q3, q4 = find_points()
log(f"points: {deg1[0][3]} {deg1[1][3]} {q2[3]} {q2b[3]} {q3[3]} {q4[3]}")

def run_config(name, pts, box):
    t1 = time.time()
    k = len(pts)
    # check degrees
    for p_ in pts:
        G1 = gb(p_[2]); dimq = len(std_monomials(G1))
        assert dimq == p_[1], (p_, dimq)
    J = ideal_product([ideal_power(p_[2], 1 + b) for p_, b in zip(pts, box)])
    GJ = gb(J); monsJ = std_monomials(GJ); D = len(monsJ)
    assert D == sum(p_[1] * (1 + b) for p_, b in zip(pts, box)), (D,)
    basisJ = [x ** i * y ** j for i, j in monsJ]
    # projections R/J -> R/(m^k + J)
    proj = {}
    for t, (p_, b) in enumerate(zip(pts, box)):
        for kk in range(1, b + 2):
            Gk = gb(ideal_power(p_[2], kk) + J); monsk = std_monomials(Gk)
            M = np.array([coords(bm, Gk, monsk) for bm in basisJ], dtype=np.int64).T  # (dim_k x D)
            proj[(t, kk)] = M
    idx = list(itertools.product(*[range(b + 1) for b in box]))
    pos = {j: i for i, j in enumerate(idx)}
    nv = len(idx) * D
    rows = []
    for j in idx:
        for t in range(k):
            if j[t] < box[t]:
                j2 = list(j); j2[t] += 1; j2 = tuple(j2)
                M = proj[(t, 1 + j[t])]
                for r in M:
                    row = np.zeros(nv, dtype=np.int64)
                    row[pos[j2] * D:(pos[j2] + 1) * D] += r
                    row[pos[j] * D:(pos[j] + 1) * D] -= r
                    rows.append(row % P)
    A = np.array(rows, dtype=np.int64) if rows else np.zeros((0, nv), dtype=np.int64)
    K = nullspace_mod_p(A, nv)
    log(f"[{name}] box {box}, dim R/J = {D}, |F| = {len(idx)}, unknowns {nv}, conditions {A.shape[0]}, kernel dim {K.shape[0]}  [{time.time()-t1:.1f}s]")
    mism = 0; npairs = 0; diag = []
    for m_, n_ in itertools.combinations(idx, 2):
        V = (K[:, pos[m_] * D:(pos[m_] + 1) * D] - K[:, pos[n_] * D:(pos[n_] + 1) * D]) % P
        codim = D - rank_mod_p(V)
        diff = [t for t in range(k) if m_[t] != n_[t]]
        pred = pts[diff[0]][1] * (1 + min(m_[diff[0]], n_[diff[0]])) if len(diff) == 1 else 0
        npairs += 1
        if codim != pred:
            mism += 1; log(f"  MISMATCH {m_} {n_}: codim {codim} vs Theorem 3.3 {pred}")
        if all(v == 0 for v in m_):
            diag.append((n_, codim))
    log(f"[{name}] pairs checked {npairs}; mismatches against Theorem 3.3: {mism}")
    for n_, c in diag:
        log(f"   Gamma_0 cap Gamma_{n_}: deg/log7 = {c}")
    return mism

def rank_mod_p(M):
    M = M.copy() % P; r = 0; rows, cols = M.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c]: piv = i; break
        if piv is None: continue
        M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, c]), P - 2, P)
        M[r] = (M[r] * inv) % P
        nz = np.nonzero(M[:, c])[0]
        for i in nz:
            if i != r: M[i] = (M[i] - M[i, c] * M[r]) % P
        r += 1
        if r == rows: break
    return r

def nullspace_mod_p(A, n):
    M = A.copy() % P; rows = M.shape[0]; pivcols = []; r = 0
    for c in range(n):
        if r == rows: break
        piv = None
        nzc = np.nonzero(M[r:, c])[0]
        if len(nzc) == 0: continue
        piv = r + nzc[0]
        M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, c]), P - 2, P)
        M[r] = (M[r] * inv) % P
        nz = np.nonzero(M[:, c])[0]
        for i in nz:
            if i != r: M[i] = (M[i] - M[i, c] * M[r]) % P
        pivcols.append(c); r += 1
    free = [c for c in range(n) if c not in set(pivcols)]
    K = np.zeros((len(free), n), dtype=np.int64)
    for t, f in enumerate(free):
        K[t, f] = 1
        for i, pc in enumerate(pivcols):
            K[t, pc] = (-M[i, f]) % P
    assert not ((A @ K.T) % P).any()
    return K

total_mism = 0
total_mism += run_config("A", [deg1[0], deg1[1], q2], (2, 1, 2))
total_mism += run_config("B", [deg1[0], q2b, q3, q4], (1, 1, 1, 1))

# ---------------- (3) all effective divisors of degree N ----------------
def rule_deg(n_support):  # n given as dict point -> multiplicity; point = (deg, label)
    pts_ = [p_ for p_, c in n_support.items() if c > 0]
    return pts_[0][0] if len(pts_) == 1 else 0

points = [(d, i) for d in range(1, 5) for i in range(a[d])]
def divisors_of_degree(N, start=0):
    if N == 0:
        yield {}
        return
    for t in range(start, len(points)):
        d = points[t][0]
        if d > N: continue
        for rest in divisors_of_degree(N - d, t):
            r = dict(rest); r[points[t]] = r.get(points[t], 0) + 1
            yield r
ok = True
for N in range(1, 5):
    cnt = 0; s = 0
    for n_ in divisors_of_degree(N):
        cnt += 1; s += rule_deg(n_)
    log(f"(3) N = {N}: {cnt} effective divisors of degree {N}; sum deg(Gamma_0 cap Gamma_n)/log 7 = {s}; N_N = {NN[N]}  {'OK' if s == NN[N] else 'FAIL'}")
    ok &= (s == NN[N])
log(f"RESULT: pair mismatches {total_mism}; N-sums {'PASS' if ok else 'FAIL'}; total {time.time()-t0:.1f}s")
