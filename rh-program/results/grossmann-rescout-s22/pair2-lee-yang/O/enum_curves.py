#!/usr/bin/env python3
"""Scout O, PAIR 2 (W1-26 Lee-Yang), Session 24 item 2.

Independent enumeration of isogeny classes (p, a1[, a2]) of curves over F_p:
  g = 1: every smooth Weierstrass cubic over F_p, p in {2,3,5,7,11,13}
         (general Weierstrass form, discriminant != 0 mod p).
  g = 2: every y^2 = f(x), f squarefree of degree 5 or 6 over F_p, p in {3,5,7},
         leading coefficient in {1, nu} (nu a fixed non-square) -- scaling f by a
         square gives an isomorphic curve, so this covers every leading-coefficient
         class; odd p only (same range as verify/genus2_signed_kernel.log).
Convention (the pricing's, PRICING.md 2(b)(vii)): P(T) = sum_k a_k T^k,
  a1 = N1 - q - 1, a2 = (N2 - q^2 - 1 + a1^2)/2.
Weil RH is checked EXACTLY in integers (no root finding), see rh_exact().
Writes classes_g1.json, classes_g2.json next to this script.
"""
import itertools, json, math, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()


def legendre_table(p):
    sq = {(x * x) % p for x in range(1, p)}
    return [0] + [1 if a in sq else -1 for a in range(1, p)]


def nonsquare(p):
    sq = {(x * x) % p for x in range(1, p)}
    return min(a for a in range(1, p) if a not in sq)


# ---------------------------------------------------------------- g = 1
def weierstrass_count(p, a):
    a1, a2, a3, a4, a6 = a
    n = 1  # point at infinity
    for x in range(p):
        for y in range(p):
            if (y * y + a1 * x * y + a3 * y - (x ** 3 + a2 * x * x + a4 * x + a6)) % p == 0:
                n += 1
    return n


def weierstrass_disc(p, a):
    a1, a2, a3, a4, a6 = a
    b2 = a1 * a1 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 * a3 + 4 * a6
    b8 = a1 * a1 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 * a3 - a4 * a4
    return (-b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 * b6 + 9 * b2 * b4 * b6) % p


g1 = {}
for p in (2, 3, 5, 7, 11, 13):
    if p <= 3:
        tuples = itertools.product(range(p), repeat=5)
    else:  # odd p >= 5: short form y^2 = x^3 + a4 x + a6 is complete up to isomorphism
        tuples = ((0, 0, 0, a4, a6) for a4 in range(p) for a6 in range(p))
    for a in tuples:
        if weierstrass_disc(p, a) == 0:
            continue
        N1 = weierstrass_count(p, a)
        a1 = N1 - p - 1
        g1.setdefault((p, a1), {"p": p, "a1": a1, "N1": N1, "example": list(a)})
g1_list = sorted(g1.values(), key=lambda r: (r["p"], r["a1"]))
for r in g1_list:
    r["hasse"] = r["a1"] ** 2 <= 4 * r["p"]
json.dump(g1_list, open(os.path.join(HERE, "classes_g1.json"), "w"), indent=0)
print("g=1 classes:", len(g1_list), " all Hasse:", all(r["hasse"] for r in g1_list))
for p in (2, 3, 5, 7, 11, 13):
    print("  p=%d a1 values:" % p, [r["a1"] for r in g1_list if r["p"] == p])


# ---------------------------------------------------------------- g = 2
def poly_trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def poly_mod(a, b, p):
    a = a[:]
    inv = pow(b[-1], p - 2, p)
    while len(a) >= len(b) and a:
        c = (a[-1] * inv) % p
        s = len(a) - len(b)
        for i, bi in enumerate(b):
            a[s + i] = (a[s + i] - c * bi) % p
        poly_trim(a)
    return a


def poly_gcd_deg(a, b, p):
    a = poly_trim([x % p for x in a]); b = poly_trim([x % p for x in b])
    while b:
        a, b = b, poly_mod(a, b, p)
    return len(a) - 1


def squarefree(f, p):
    df = [(i * f[i]) % p for i in range(1, len(f))]
    if not poly_trim(df[:]):
        return False  # f' = 0 (cannot happen for deg 5, 6 and p >= 7; guard for p = 3, 5)
    return poly_gcd_deg(f, df, p) == 0


def rh_exact(q, a1, a2):
    """Weil RH for P(T)=1+a1 T+a2 T^2+q a1 T^3+q^2 T^4  <=>  the w-roots of
    w^2 + c1 w + (c2 - 2), c1 = a1/sqrt q, c2 = a2/q, are real and lie in [-2, 2].
    Integer form: disc a1^2 - 4 a2 + 8 q >= 0; 2q + a2 >= 0 and (2q+a2)^2 >= 4 q a1^2
    (i.e. value at w = +-2 nonnegative); vertex |a1| <= 4 sqrt q  <=> a1^2 <= 16 q."""
    if a1 * a1 - 4 * a2 + 8 * q < 0:
        return False
    if 2 * q + a2 < 0 or (2 * q + a2) ** 2 < 4 * q * a1 * a1:
        return False
    return a1 * a1 <= 16 * q


import numpy as np

g2 = {}
nsmooth = {}
for p in (3, 5, 7):
    chi = np.array(legendre_table(p))
    nu = nonsquare(p)
    # F_{p^2} = F_p[w]/(w^2 - nu); elements (u, v) = u + v w
    elems = [(u, v) for u in range(p) for v in range(p)]
    U = np.zeros((7, p * p), dtype=np.int64); V = np.zeros((7, p * p), dtype=np.int64)
    for j, (u, v) in enumerate(elems):
        cu, cv = 1, 0
        for k in range(7):
            U[k, j], V[k, j] = cu, cv
            cu, cv = (cu * u + cv * v * nu) % p, (cu * v + cv * u) % p
    in_Fp = np.array([v == 0 for (u, v) in elems])
    rows = []
    for deg in (5, 6):
        for lc in (1, nu):
            for low in itertools.product(range(p), repeat=deg):
                f = list(low) + [lc]
                if squarefree(f, p):
                    rows.append((deg, lc, f + [0] * (6 - deg)))
    nsmooth[p] = len(rows)
    C = np.array([r[2] for r in rows], dtype=np.int64)  # n x 7
    fu = (C @ U) % p; fv = (C @ V) % p
    norm = (fu * fu - nu * fv * fv) % p
    chi2 = chi[norm]                       # quadratic character on F_{p^2} via the norm
    chi1 = chi[fu[:, in_Fp]]               # F_p points: v = 0, value fu
    degs = np.array([r[0] for r in rows]); lcs = np.array([r[1] for r in rows])
    inf1 = np.where(degs == 5, 1, 1 + chi[lcs % p])
    inf2 = np.where(degs == 5, 1, 2)
    N1 = p + chi1.sum(axis=1) + inf1
    N2 = p * p + chi2.sum(axis=1) + inf2
    for i, r in enumerate(rows):
        n1, n2 = int(N1[i]), int(N2[i])
        a1 = n1 - p - 1
        a2x2 = n2 - p * p - 1 + a1 * a1
        assert a2x2 % 2 == 0
        a2 = a2x2 // 2
        key = (p, a1, a2)
        if key not in g2:
            g2[key] = {"p": p, "a1": a1, "a2": a2, "N1": n1, "N2": n2,
                       "deg": r[0], "lc": r[1], "f_low_to_high": r[2][:r[0] + 1],
                       "rh": rh_exact(p, a1, a2)}
    print("p=%d: smooth genus-2 models enumerated: %d; distinct classes so far: %d; %.1fs"
          % (p, len(rows), len(g2), time.time() - t0))
g2_list = sorted(g2.values(), key=lambda r: (r["p"], r["a1"], r["a2"]))
json.dump(g2_list, open(os.path.join(HERE, "classes_g2.json"), "w"), indent=0)
print("g=2 distinct (p,a1,a2) classes:", len(g2_list))
print("  per p:", {p: sum(1 for r in g2_list if r["p"] == p) for p in (3, 5, 7)})
print("  all satisfy Weil RH (exact integer test):", all(r["rh"] for r in g2_list))
# comparison with the record's 587 (verify/genus2_signed_kernel.log rows 2..588)
logp = os.path.join(HERE, "..", "..", "verify", "genus2_signed_kernel.log")
rec = set()
for line in open(logp):
    t = line.split()
    if len(t) > 6 and t[0].isdigit() and t[1] in ("5", "6") and t[6] in ("True", "False"):
        rec.add((int(t[0]), int(t[2]), int(t[3])))
mine = set(g2.keys())
print("record classes parsed from the log:", len(rec))
print("  record subset of mine:", rec <= mine, "| mine minus record:", len(mine - rec),
      "| record minus mine:", len(rec - mine))
print("  classes new in this enumeration (non-monic leading coefficient twists):",
      sorted(mine - rec))
print("elapsed s: %.1f" % (time.time() - t0))
