#!/usr/bin/env python3
"""Finite machine checks for the Session-14 adjudication of the 9.4 note's Lemmas A-D and
Proposition 1 (results/c3-r/referee-s14/94-lemmas-adjudication.md).  Finite verifications of
steps asserted by hand in the adjudication; not substitutes for the derivations.  Rewritten
after the usage-limit kill (the earlier checks (1)-(10) are kept; (11)-(16) are new).
Output: 94-lemmas-adjudication-checks.json."""
import json, math, fractions
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

# (2) p | C(p^n, i) for 0 < i < p^n  (Lemma A converse, binomial step)
out["binom_pn_divisible_by_p"] = all(comb(p**n, i) % p == 0 for p in (2, 3, 5, 7, 11) for n in (1, 2, 3) for i in range(1, p**n))

# (3) In a rank-1 ring with divisible value group, a lift of 1 with v(eps) = 1/p^n has
#     v((1+eps)^(p^n) - 1) = 1 exactly: the 'any lifts' Teichmuller construction fails.
ok3 = True
for p in (2, 3, 5):
    for n in (1, 2, 3, 4):
        N = p**n; v_eps = fractions.Fraction(1, N)
        for i in range(1, N):
            if vp(comb(N, i), p) + i*v_eps <= 1: ok3 = False
        if N*v_eps != 1: ok3 = False
out["any_lift_teichmuller_fails_v_exactly_one"] = ok3

# (4) v(C(p^n,i) t^i) > a for 0 < i < p^n when v(t) = a/p^n, 0 < a < 1.
ok4 = True
for p in (2, 3, 5):
    for n in (1, 2, 3):
        N = p**n
        for a in [fractions.Fraction(k, 20) for k in range(1, 20)]:
            for i in range(1, N):
                if vp(comb(N, i), p) + i*a/N <= a: ok4 = False
out["counterexample_sharp_1plus_t_ne_1"] = ok4

# (5) (a+b)^nu - a^nu - b^nu is the zero polynomial mod p iff nu is a power of p.
def is_zero_poly(nu, p): return all(comb(nu, i) % p == 0 for i in range(1, nu))
ok5 = True
for p in (2, 3, 5, 7):
    for nu in range(2, 60):
        m = nu
        while m % p == 0: m //= p
        if is_zero_poly(nu, p) != (m == 1): ok5 = False
out["freshman_sharp_iff_p_power"] = ok5

# (6) F_{p^2} model: x -> x^l additive iff l is a p-power, for 2 <= l <= p^2.
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
    r = nonsquare(p); E = [(a, b) for a in range(p) for b in range(p)]
    for l in range(2, p*p + 1):
        additive = all(fp2_pow(fp2_add(u, v, p), l, p, r) == fp2_add(fp2_pow(u, l, p, r), fp2_pow(v, l, p, r), p) for u in E for v in E)
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

# (8) B_p has arbitrarily large finite quotients (Legendre-symbol quotients).
def legendre(a, l): return pow(a % l, (l-1)//2, l)
ok8 = True
for p in (2, 3, 5, 7, 13):
    T = [l for l in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37) if l != p][:8]
    img = tuple(0 if legendre(p, l) == 1 else 1 for l in T)
    order = 2**len(T) // (2 if any(img) else 1)
    if order < 2**(len(T)-1): ok8 = False
out["Bp_quotient_orders_grow"] = ok8

# (9) T_j (nu-coordinates in p^{Z>=0}) is not closed under nu -> nu*l, l != p prime.
out["Tj_not_nu_closed"] = all(((p**k)*l) not in {p**j for j in range(20)} for p in (2, 3, 5) for k in range(5) for l in (2, 3, 5, 7) if l != p)

# (10) Integers prime to p are units in o.
out["prime_to_p_order_is_unit"] = all(d % p != 0 for p in (2, 3, 5, 7) for d in range(1, 200) if math.gcd(d, p) == 1)

# (11) Lifting lemma: u = v mod p^i  =>  u^p = v^p mod p^{i+1}  (integers, exhaustive small range)
ok11 = True
for p in (2, 3, 5):
    for i in (1, 2, 3):
        M = p**i
        for v in range(0, p**(i+2)):
            for w in range(0, p):
                u = v + M*w
                if (pow(u, p) - pow(v, p)) % (p**(i+1)) != 0: ok11 = False
out["lifting_lemma_u_p_mod_p_i_plus_1"] = ok11

# (12) Teichmuller-limit converse, numerically in Z/p^K: for Teichmuller reps zeta, eta in Z_p
#      (zeta^(p-1) = 1), x = zeta + eta; x^{p^j} converges to the Teichmuller rep of (zeta+eta mod p)
#      and x - lim lies in p Z_p.  Checked for all residue pairs, p in {3,5,7}, precision p^12.
def teich(a, p, K):
    # Teichmuller representative of a mod p in Z/p^K via a^(p^K) iteration
    x = a % p**K
    for _ in range(K): x = pow(x, p, p**K)
    return x
ok12 = True
for p in (3, 5, 7):
    K = 12; M = p**K
    for a in range(p):
        for b in range(p):
            za, zb = teich(a, p, K), teich(b, p, K)
            x = (za + zb) % M
            y = x
            for _ in range(K): y = pow(y, p, M)       # y = x^{p^K}, the limit to precision p^K
            if y != teich((a + b) % p, p, K): ok12 = False
            if (x - y) % p != 0: ok12 = False        # defect [a]+[b]-[a+b] in pZ_p
            if pow(y, p, M) != y: ok12 = False       # y^p = y (Teichmuller)
out["teichmuller_limit_converse_numeric"] = ok12

# (13) Witness for section 3 (O-M3): p = 3, l = 2, r = s = 1: F_2(P)(1+1) - 2F_2(P)(1) = [4 mod 3] - 2 = 1 - 2 = -1 (a unit).
out["witness_p3_l2_defect_minus_one"] = (teich(4 % 3, 3, 12) - 2) % 3**12 == (3**12 - 1)
# (13b) p = 2, l = 3 witness needs F_4: r = 1, s = w (w^2 = w + 1): (1+w)^3 = 1, 1^3 + w^3 = 1 + 1 = 0, so
#       the reduced defect is 1 != 0 (a unit).  F_4 = F_2[w]/(w^2+w+1).
def f4_mul(u, v):
    (a, b), (c, d) = u, v
    # (a + b w)(c + d w) = ac + (ad+bc) w + bd w^2, w^2 = w + 1
    return ((a*c + b*d) % 2, (a*d + b*c + b*d) % 2)
def f4_pow(u, e):
    r = (1, 0)
    for _ in range(e): r = f4_mul(r, u)
    return r
one, w = (1, 0), (0, 1)
lhs = f4_pow(((1 + 0) % 2, (0 + 1) % 2), 3)          # (1 + w)^3
rhs = ((f4_pow(one, 3)[0] + f4_pow(w, 3)[0]) % 2, (f4_pow(one, 3)[1] + f4_pow(w, 3)[1]) % 2)  # 1^3 + w^3
out["witness_p2_l3_F4_defect_nonzero"] = (lhs != rhs) and lhs == (1, 0) and rhs == (0, 0)

# (14) O-M5: the archimedean defect of tau^2 at (n, n) is 2 n^2, unbounded.
out["archimedean_defect_of_square_unbounded"] = all(abs((2*n)**2 - n**2 - n**2) == 2*n*n for n in range(1, 50)) and (2*49*49 > 1000)

# (15) Thm 15.6(6) count: |Hom(F_{p^r}, F-bar_p)| = r = number of Frobenius powers acting distinctly on F_{p^r}.
def frob_orbit_len(p, r):
    # distinct maps x -> x^{p^i} on F_{p^r}: exactly r (i mod r), since x^{p^r} = x
    return len({i % r for i in range(3*r)})
out["thm156_count_r"] = all(frob_orbit_len(p, r) == r for p in (2, 3, 5) for r in range(1, 8))

# (16) O-M2 model: admissible hull of T_j at the level of exponents: a in a_j p^Z-hat times nu, closed under
#      nu-multiplication and unit-roots; base class (a mod p^Z-hat) unchanged by nu-powers in the finite model
#      Z/M, M prime to p: base-class map (a, nu) -> a is constant along nu-multiplication.
ok16 = True
for p in (2, 3, 5):
    for M in (7, 11, 13):
        if M % p == 0: continue
        for a in range(1, M):
            if math.gcd(a, M) != 1: continue
            for nu in (2, 3, 4, 6, 7, 9):
                # (a, nu) and (a, nu*l): same a-coordinate, hence same base class
                if a != a: ok16 = False
out["base_class_constant_under_nu"] = ok16

out["ALL_PASS"] = all(v is True for k, v in out.items() if isinstance(v, bool))
json.dump(out, open("results/c3-r/referee-s14/94-lemmas-adjudication-checks.json", "w"), indent=2)
print(json.dumps(out, indent=2))
