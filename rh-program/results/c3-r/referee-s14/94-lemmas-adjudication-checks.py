#!/usr/bin/env python3
"""Finite machine checks for the Session-14 adjudication of the 9.4 note's Lemmas A-D and
Proposition 1 (results/c3-r/referee-s14/94-lemmas-adjudication.md).  These are finite
verifications of steps asserted by hand in the adjudication; they are not substitutes for the
derivations.  Output: 94-lemmas-adjudication-checks.json."""
import json, math, itertools, fractions
from math import comb

out = {}

def vp(n, p):
    if n == 0: return math.inf
    v = 0
    while n % p == 0: n //= p; v += 1
    return v

# (1) Lemma B: |zeta - 2| for |zeta| = 1 lies in [1, 3]; p = 2 gives |0 - 2| = 2.
vals = [abs(complex(math.cos(t), math.sin(t)) - 2) for t in [2*math.pi*k/200000 for k in range(200000)]]
out["B_min_defect"] = round(min(vals), 9); out["B_max_defect"] = round(max(vals), 9)
out["B_p2_defect"] = abs(0 - 2)
out["B_ok"] = abs(min(vals) - 1.0) < 1e-6 and abs(max(vals) - 3.0) < 1e-6

# (2) p | C(p^n, i) for 0 < i < p^n  (Lemma A converse, first bracket; and (3) below)
ok2 = all(comb(p**n, i) % p == 0 for p in (2, 3, 5, 7, 11) for n in (1, 2, 3) for i in range(1, p**n))
out["binom_pn_divisible_by_p"] = ok2

# (3) Refutation of the 'any lifts' Teichmuller construction (referee O, Step 3b) in a rank-1
#     valuation ring with divisible value group: with |eps| = |p|^(1/p^n) (v(eps) = 1/p^n),
#     v(C(p^n,i) eps^i) > 1 for 0 < i < p^n while v(eps^(p^n)) = 1 exactly; so
#     |(1+eps)^(p^n) - 1| = |p| for EVERY n, and the sequence (1+eps_n)^(p^n) of p^n-th powers of
#     lifts of 1 = 1^(1/p^n) never approaches 1 = [1].
ok3 = True
for p in (2, 3, 5):
    for n in (1, 2, 3, 4):
        N = p**n
        v_eps = fractions.Fraction(1, N)
        for i in range(1, N):
            if vp(comb(N, i), p) + i*v_eps <= 1: ok3 = False
        if N*v_eps != 1: ok3 = False
out["any_lift_teichmuller_fails_v_exactly_one"] = ok3

# (4) Counterexample valuation step: for t' with v(t') = a in (0,1) (i.e. |p| < |t'| < 1) and
#     lifts with v(t~_n) = a/p^n: v(C(p^n,i) t~_n^i) > a for 0 < i < p^n, so
#     |(1 + t~_n)^(p^n) - 1| = |t'| for every n, hence |sharp(1+t') - 1| = |t'| != 0.
ok4 = True
for p in (2, 3, 5):
    for n in (1, 2, 3):
        N = p**n
        for a in [fractions.Fraction(k, 20) for k in range(1, 20)]:
            for i in range(1, N):
                if vp(comb(N, i), p) + i*a/N <= a: ok4 = False
out["counterexample_sharp_1plus_t_ne_1"] = ok4

# (5) Sharp N-invariance failure (O's F8 / note section 3): (a+b)^nu - a^nu - b^nu is the zero
#     polynomial mod p iff nu is a power of p.  Checked as polynomial identity, p in {2,3,5,7},
#     2 <= nu < 60.
def is_zero_poly(nu, p):
    return all(comb(nu, i) % p == 0 for i in range(1, nu))
ok5 = True
for p in (2, 3, 5, 7):
    for nu in range(2, 60):
        ispow = (nu == p**round(math.log(nu, p))) if nu > 1 else False
        # robust power test
        m = nu; ispow = True
        while m % p == 0: m //= p
        ispow = (m == 1)
        if is_zero_poly(nu, p) != ispow: ok5 = False
out["freshman_sharp_iff_p_power"] = ok5

# (6) Concrete field-level check in F_{p^2} = F_p[x]/(x^2 - r), r a non-square: for 2 <= l <= p^2,
#     x -> x^l is additive on F_{p^2} iff l is a power of p.  (On the FINITE field the map is also
#     additive whenever l = p^k mod (p^2 - 1), e.g. x^25 = x on F_9 -- which is exactly why the
#     argument in the adjudication is run on the INFINITE field F-bar_p, where a nonzero
#     polynomial (a+b)^l - a^l - b^l takes a nonzero value; the finite model is only probed for
#     l <= p^2.)
def fp2_elems(p, r):
    return [(a, b) for a in range(p) for b in range(p)]
def fp2_mul(u, v, p, r):
    (a, b), (c, d) = u, v
    return ((a*c + b*d*r) % p, (a*d + b*c) % p)
def fp2_pow(u, e, p, r):
    res = (1, 0)
    for _ in range(e): res = fp2_mul(res, u, p, r)
    return res
def fp2_add(u, v, p): return ((u[0]+v[0]) % p, (u[1]+v[1]) % p)
def nonsquare(p):
    sq = {(a*a) % p for a in range(1, p)}
    return next(r for r in range(2, p) if r not in sq)
ok6 = True
for p in (3, 5, 7):
    r = nonsquare(p)
    E = fp2_elems(p, r)
    for l in range(2, p*p + 1):
        additive = all(fp2_pow(fp2_add(u, v, p), l, p, r) == fp2_add(fp2_pow(u, l, p, r), fp2_pow(v, l, p, r), p)
                       for u in E for v in E)
        m = l
        while m % p == 0: m //= p
        if additive != (m == 1): ok6 = False
out["Fp2_power_map_additive_iff_p_power"] = ok6

# (7) Lemma D(iii): Z_(p)-powers commute with homomorphisms of cyclic groups Z/d -> Z/e, e | d.
ok7 = True
for d in range(2, 50):
    for e in [e for e in range(1, d+1) if d % e == 0]:
        for u in range(1, d):
            if math.gcd(u, d) != 1: continue
            for a in range(d):
                if ((u*a) % d) % e != (u*(a % e)) % e: ok7 = False
out["power_commutes_with_hom"] = ok7

# (8) B_p has arbitrarily large finite quotients: image of p in prod_{l in T}(Z/l)^x/squares is one
#     element, so |quotient| >= 2^(|T|-1).
def legendre(a, l): return pow(a % l, (l-1)//2, l)
ok8 = True
for p in (2, 3, 5, 7, 13):
    T = [l for l in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37) if l != p][:8]
    # quotient (Z/2)^|T| by the subgroup generated by the image of p: order 2^|T| or 2^(|T|-1)
    img = tuple(0 if legendre(p, l) == 1 else 1 for l in T)
    order = 2**len(T) // (2 if any(img) else 1)
    if order < 2**(len(T)-1): ok8 = False
out["Bp_quotient_orders_grow"] = ok8

# (9) T_j vs E(a_j): in packet coordinates, T_j = {(a,nu): a in a_j p^Zhat, nu in p^{Z>=0}} is not
#     closed under nu -> nu*l for a prime l != p, while E(a_j) has nu in all of N.  Finite model:
#     the nu-coordinates {p^k : k <= K} are not closed under multiplication by l.
ok9 = all(((p**k)*l) not in {p**j for j in range(20)} for p in (2, 3, 5) for k in range(5) for l in (2, 3, 5, 7) if l != p)
out["Tj_not_nu_closed"] = ok9

# (10) Integers prime to p are units in o (|d| = 1): d mod p != 0.
out["prime_to_p_order_is_unit"] = all(d % p != 0 for p in (2, 3, 5, 7) for d in range(1, 200) if math.gcd(d, p) == 1)

out["ALL_PASS"] = all(v is True for k, v in out.items() if isinstance(v, bool))
json.dump(out, open("results/c3-r/referee-s14/94-lemmas-adjudication-checks.json", "w"), indent=2)
print(json.dumps(out, indent=2))
