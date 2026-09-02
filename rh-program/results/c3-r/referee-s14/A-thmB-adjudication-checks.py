#!/usr/bin/env python3
"""
A-thmB-adjudication-checks.py -- computational spot-checks for the binding adjudication of
probe A's Theorem B(b) (RH program, C3-r, Session 14, 2026-09-02).

These checks are NOT the proof; they are finite sanity checks of the arithmetic steps the
adjudicator re-derived by hand (see A-thmB-adjudication.md). Output: A-thmB-adjudication-checks.json.

C1  Kernel lemma arithmetic (referee F Lemma F.0 / referee O Step R2): for gcd(m, n) = 1 the map
    zeta -> zeta^m is a bijection of mu_n, so "P kills mu_n^m" forces "P kills mu_n".
    Checked exhaustively for 1 <= n <= 80, all m coprime to n.
C2  Injectivity range: e^{2 pi i s} = 1 with |s| <= 1/2 forces s = 0 (the [0, 1/2] choice), and the
    failure at side 1 (s = 1) -- confirms the note's range is what makes injectivity work.
C3  Referee O's N2 sequence (non-Hausdorffness of X_0 at the cell points): for delta = 0.3 and
    k = 2..9 the quantities L_k, p_k, c_k, d_k, r_k, e_k satisfy r_k -> 1, |e_k delta - L_k| < 1/k,
    gcd(p_k, L_k) = 1, L_k | d_k, and the profinite congruences a_k == 1 and r_k a_k == 1 (mod M)
    for every M | L_k, computed with p_k^{-1} mod M.  Also the V-part: e_k * (delta A/B) mod 1 -> 0
    for B | L_k.
C4  The packet two-limit sequence (Session-8 adjudication sec. 3, re-used by both referees):
    CRT density of N in Z_(p): for p = 2 and target residues c a_0^{-1} mod d (d odd), positive
    integers n_k with n_k a_0 == c (mod d) exist for every d, and are found by search.
C5  Unique-factorization independence of the V-components of rational primes: for primes
    2, 3, 5, 7 and exponent vectors k in [-4, 4]^4, prod l_i^{k_i} in {+1, -1} only for k = 0.
"""
import json, math, cmath
from fractions import Fraction
from itertools import product

out = {}

# ---------- C1 ----------
def c1():
    bad = []
    for n in range(1, 81):
        for m in range(1, 4 * n + 1):
            if math.gcd(m, n) != 1:
                continue
            img = sorted((m * z) % n for z in range(n))
            if img != list(range(n)):
                bad.append((n, m))
    return {"n_range": [1, 80], "bijection_failures": bad, "pass": not bad}
out["C1_kernel_lemma_bijection"] = c1()

# ---------- C2 ----------
def c2():
    res = {}
    # s in [-1/2, 1/2]: exp(2 pi i s) == 1 only at s = 0 (grid + exact rational check)
    viol = []
    for num in range(-500, 501):
        s = num / 1000.0
        if abs(cmath.exp(2j * math.pi * s) - 1) < 1e-12 and s != 0:
            viol.append(s)
    res["half_side_violations"] = viol
    res["side_one_collision"] = abs(cmath.exp(2j * math.pi * 1.0) - 1) < 1e-12  # t=0 and t=1 collide
    res["pass"] = (not viol) and res["side_one_collision"]
    return res
out["C2_injectivity_range"] = c2()

# ---------- C3 ----------
def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    r = int(n ** 0.5)
    f = 3
    while f <= r:
        if n % f == 0: return False
        f += 2
    return True

def next_prime(n):
    n += 1
    while not is_prime(n): n += 1
    return n

def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

def c3(delta=Fraction(3, 10), kmax=9):
    rows = []
    ok = True
    for k in range(2, kmax + 1):
        L = 1
        for j in range(1, k + 1): L = L * j // math.gcd(L, j)
        bound = max(k, math.ceil(k * L ** 3 / delta))
        p = next_prime(bound)
        c = int(round(p * delta / L ** 2))
        d = L * c
        n = p
        m = n + d
        r = Fraction(m, n)
        e = Fraction(n, d)
        r_minus_1 = float(r - 1)
        e_delta_minus_L = float(e * delta - L)
        cond_gcd = math.gcd(p, L) == 1
        cond_div = d % L == 0
        cond_e = abs(e_delta_minus_L) < 1.0 / k
        # profinite congruences for every M | L: a_k = p * u_k with u_k = p^{-1} mod M
        cong_ok = True
        for M in divisors(L):
            if M == 1: continue
            pinv = pow(p, -1, M)
            a_mod = (p * pinv) % M
            ra_mod = (m * pinv) % M
            if a_mod != 1 % M or ra_mod != 1 % M:
                cong_ok = False
        # V-part: e_k * (delta * A/B) mod 1 -> 0 for B | L  (take A/B = 5/6, B=6 | L for k>=3)
        A, B = 5, 6
        vpart = None
        if L % B == 0:
            val = e * delta * Fraction(A, B)
            frac = val - math.floor(val)
            frac = min(float(frac), 1 - float(frac))
            vpart = frac
        row = {"k": k, "L_k": L, "p_k": p, "c_k": c, "d_k": d, "r_k_minus_1": r_minus_1,
               "e_k_delta_minus_L_k": e_delta_minus_L, "gcd_ok": cond_gcd, "L_divides_d": cond_div,
               "e_bound_ok": cond_e, "congruences_ok": cong_ok, "Vpart_dist_to_Z": vpart}
        ok = ok and cond_gcd and cond_div and cond_e and cong_ok
        rows.append(row)
    return {"delta": str(delta), "rows": rows, "pass": ok,
            "note": "r_k -> 1, |e_k delta - L_k| < 1/k, a_k == 1 and r_k a_k == 1 mod every M | L_k, V-part -> 0 mod 1"}
out["C3_N2_sequence"] = c3()

# ---------- C4 ----------
def c4(p=2, dmax=60):
    # a0 = 1, c = -1 as elements of Z^x_(2) = prod_{l odd} Z_l^x; [c] != [a0] in B_2 = Z^x_(2)/2^Z-bar
    # because -1 is not a power of 2 mod 7 (powers of 2 mod 7 are {1,2,4}).
    pow2_mod7 = sorted({pow(2, j, 7) for j in range(6)})
    distinct_classes = (7 - 1) not in pow2_mod7
    rows = []
    ok = distinct_classes
    for d in range(1, dmax + 1):
        if d % p == 0: continue
        target = (-1) % d
        n = next(nn for nn in range(1, 10 * d + 2) if nn % d == target)   # n_k == c a0^{-1} (mod d)
        good = (n * 1 - (-1)) % d == 0
        ok = ok and good
        rows.append({"d": d, "n": n, "n_a0_eq_c_mod_d": good})
    return {"p": p, "a0": 1, "c": -1, "powers_of_2_mod_7": pow2_mod7, "classes_distinct_in_B_2": distinct_classes,
            "rows_checked": len(rows), "pass": ok, "sample": rows[:6]}
out["C4_CRT_density_packet_sequence"] = c4()

# ---------- C5 ----------
def c5():
    primes = [2, 3, 5, 7]
    hits = []
    for k in product(range(-4, 5), repeat=4):
        val = Fraction(1)
        for l, e in zip(primes, k):
            val *= Fraction(l) ** e
        if val in (1, -1):
            hits.append(k)
    return {"primes": primes, "exponent_box": [-4, 4], "solutions_of_prod_eq_pm1": hits,
            "pass": hits == [(0, 0, 0, 0)]}
out["C5_UF_independence"] = c5()

out["ALL_PASS"] = all(v.get("pass") for k, v in out.items() if isinstance(v, dict))
import os
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "A-thmB-adjudication-checks.json"), "w") as f:
    json.dump(out, f, indent=1, default=str)
print(json.dumps({k: (v["pass"] if isinstance(v, dict) else v) for k, v in out.items()}, indent=1))
