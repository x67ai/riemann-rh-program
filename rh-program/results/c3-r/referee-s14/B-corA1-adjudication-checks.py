# Adjudicator's finite-truncation sanity checks for probe B Cor. A.1 (Session 14, 2026-09-02).
# These prove nothing; they exhibit, in finite truncations of Z_(p)-hat, the three elementary
# inputs the adjudication re-derives by hand: (C1) CRT density of N in Z_(p)-hat; (C2) the
# exponent classes (i) n*unit / (ii) some component 0 / (iii) all components nonzero but
# infinitely many non-units, and the finiteness of ker(( )^b) on mu^(p); (C3) unit twists
# a, a' lie on the same packet orbit iff a'/a in p^Zhat (finite-level check).
import json, math
from itertools import product

def primes_upto(n):
    s = [True]*(n+1); s[0]=s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=False
    return [i for i in range(n+1) if s[i]]

out = {}
p = 5
ells = [l for l in primes_upto(40) if l != p]

# C1: every residue class mod M (M prime to p) contains a positive integer (CRT / trivial),
# and residues of the Frobenius exponents n=1,2,... are dense: at level M = prod of small ells,
# the set {n mod M : 1 <= n <= M} is everything.
M = 1
for l in ells[:4]: M *= l
hit = set(n % M for n in range(1, M+1))
out["C1_CRT_density"] = {"M": M, "all_residues_hit": len(hit) == M}

# C2: kernel of ( )^b on the truncated group  prod_{l in ells} mu_{l^k}  (k = 3), for three b's.
k = 3
def kernel_size(b_components):
    # b_l acts on mu_{l^k} as raising to b_l; kernel size = gcd(b_l, l^k)
    size = 1
    for l, bl in zip(ells, b_components):
        size *= math.gcd(bl % (l**k) if bl % (l**k) else l**k, l**k)
    return size
b_i   = [7 * 1 for _ in ells]            # b = 7 * (unit at every l != 7): class (i) up to the l=7 factor
b_i   = [1 if l != 7 else 7 for l in ells]  # b = 7 exactly (n=7, u=1)
b_ii  = [0 if l == 3 else 1 for l in ells]  # component 0 at l=3: kills all of mu_{3^inf}
b_iii = [l for l in ells]                    # b_l = l for every l: every component nonzero, none a unit
out["C2_kernel_sizes_truncated"] = {
    "ells": ells, "k": k,
    "class_i_b=7": kernel_size(b_i),
    "class_ii_b3=0": kernel_size(b_ii),
    "class_iii_bl=l": kernel_size(b_iii),
    "note": "class (i) kernel is bounded (=7) independent of the number of primes; class (ii) grows as 3^k with the truncation depth; class (iii) grows as prod(ells) with the number of primes while every component is nonzero"
}
# show growth of class (iii) with the number of primes used
growth = []
for m in range(1, len(ells)+1):
    sz = 1
    for l in ells[:m]: sz *= math.gcd(l, l**k)
    growth.append(sz)
out["C2_class_iii_growth"] = growth

# C3: finite-level model of the base Ẑ×_(p)/p^Ẑ: at level M (prime to p) the base is (Z/M)^x / <p>.
# Two unit exponents a, a' give the same orbit iff a' a^{-1} in <p> mod M. Check with the
# explicit construction: (x, chi^{a p^j}) = Frob^j-twist of (x, chi^a), i.e. same G-orbit.
M = 3*7*11
units = [a for a in range(1, M) if math.gcd(a, M) == 1]
pgroup = set(); q = 1
while q not in pgroup:
    pgroup.add(q); q = (q*p) % M
classes = set()
for a in units:
    classes.add(frozenset((a*g) % M for g in pgroup))
out["C3_base_orbit_count_level_M"] = {"M": M, "phi(M)": len(units), "order_of_p_mod_M": len(pgroup),
                                      "number_of_orbits_at_level_M": len(classes),
                                      "equals_phi/ord": len(classes) == len(units)//len(pgroup)}
# uncountability driver: the base surjects onto (C_2)^{|T|-1}: check phi(M)/ord(p) grows with more primes
out["C3_growth"] = []
for T in [[3,7],[3,7,11],[3,7,11,13],[3,7,11,13,17]]:
    M = 1
    for l in T: M *= l
    units = [a for a in range(1, M) if math.gcd(a, M) == 1]
    pg = set(); q = 1
    while q not in pg:
        pg.add(q); q = (q*p) % M
    out["C3_growth"].append({"T": T, "orbits": len(units)//len(pg)})

print(json.dumps(out, indent=1))

# ---- Added on completion of the adjudication (the earlier run was killed after C1-C3) ----
# C4: the (Tors)-necessity witness. n_k = prod_{l<=k, l!=p} l^k tends to 0 in Z_(p)-hat: for each
# fixed l, v_l(n_k) = k once k >= l. The limit character chi^0 = 1 has kernel all of mu^(p): not (Tors).
def nk(k, p):
    n = 1
    for l in primes_upto(k):
        if l != p: n *= l**k
    return n
def vl(n, l):
    v = 0
    while n % l == 0: n //= l; v += 1
    return v
out["C4_nk_to_zero"] = {"p": p, "v_3(n_k) for k=3..8": [vl(nk(k,p),3) for k in range(3,9)],
                        "v_7(n_k) for k=7..10": [vl(nk(k,p),7) for k in range(7,11)],
                        "verdict_valuations_grow_with_k": all(vl(nk(k,p),3)==k for k in range(3,9))}

# C5: the adjudicator's simplification of referee O's Cor. O.7 construction: nu = 1, ANY real s > 0
# (rational allowed), m_k = 1 mod k!, |m_k / p^{j_k} - s| < 1/k. Shows irrationality of s and the
# Z-hat subsequence are unnecessary; the Q^{>0}-orbit of (P0, w) accumulates at (P0, w/s).
from fractions import Fraction
def factorial(k):
    f = 1
    for i in range(2, k+1): f *= i
    return f
rows = []
for s in [Fraction(3,2), Fraction(1,1), Fraction(7,3)]:
    ok = True
    for k in range(1, 13):
        M = factorial(k)
        j = 1
        while p**j <= k*M: j += 1
        target = s * p**j
        # largest integer <= target that is = 1 mod M
        t = int(target)  # floor for positive rationals
        m = t - ((t - 1) % M)
        if m <= 0: m += M
        err = abs(Fraction(m, p**j) - s)
        ok = ok and (err < Fraction(1, k)) and (m % M == 1 % M or M == 1)
    rows.append({"s": str(s), "all_k_le_12_within_1/k_and_m_k=1_mod_k!": ok})
out["C5_CorO7_construction_rational_s_nu_1"] = rows
print(json.dumps({k: out[k] for k in ["C4_nk_to_zero", "C5_CorO7_construction_rational_s_nu_1"]}, indent=1))
with open("B-corA1-adjudication-checks.json", "w") as fh:
    json.dump(out, fh, indent=1)

# ---- Added 2026-09-02 (third run, completing the adjudication against referee runs F-run3 / O-rerun) ----
# C6: the chart-membership criterion of Explicit form (b) / Lemma O.4, in a finite model. A packet point at
# fixed x is an exponent e (a unit) acting on mu_M, M prime to p. F_n multiplies the exponent by n; F_d^{-1}
# exists in the chart iff the character kills mu_d, i.e. iff d | exponent (d prime to p); F_p acts as a
# unit (p is a unit mod M), and on the Galois quotient F_p is the identity on packet points (Frobenius).
# Claim checked: for r = m/m' in lowest terms, F_r P0 lies in the chart F_nu^{-1}(X0•(C)) iff the
# prime-to-p part of m' divides nu  (in particular m' may be a power of p with nu = 1: referee F's F7 /
# referee O's m6 concern this p-power case).
def prime_to_p_part(n, p):
    while n % p == 0: n //= p
    return n
p = 5
ells = [3, 7, 11]
M = 1
for l in ells: M *= l**2
e = 1  # unit exponent (reference character chi^{a0}, a0 = 1)
rows = []
ok = True
for m in range(1, 40):
    for mp in range(1, 40):
        if math.gcd(m, mp) != 1: continue
        for nu in [1, 3, 7, 21, 9, 5, 45]:
            # F_nu F_{m/m'} P0 = F_{m'}^{-1} F_{nu m} P0 : in chart iff prime-to-p part of m' divides nu*m*e
            # (kill mu_{m'_(p)}), and the p-part of m' imposes nothing (F_p fixes P0).
            mpp = prime_to_p_part(mp, p)
            in_chart = (nu * m * e) % mpp == 0
            predicted = nu % mpp == 0
            if in_chart != predicted: ok = False
rows.append({"criterion_prime_to_p_part_of_denominator_divides_nu": ok})
rows.append({"witness_F7_m6": {"m": 1, "m'": p, "nu": 1, "in_chart": True, "naive_criterion_m'_divides_nu": p % 1 == 0 and 1 % p == 0}})
out["C6_chart_membership"] = rows

# C7: referee O's N2 — [r3s-08] (2.2.7) "Z_(p)-hat^x x N ->> Hom(kappa(P)^x, C^x)" cannot be a surjection:
# Hom(mu^(p), C^x) = End(mu^(p)) = Z_(p)-hat (x-03 p. 35), while the image is the set of exponents n*u.
# At every FINITE level prod_{l<=L} Z/l^k every residue IS of the form n*u (take n = prod l^{min(v_l,k)}),
# so the failure is invisible at finite level; what IS visible is that the kernel size of the witnesses
# b = 0 and b = (l)_l is unbounded as the level grows, whereas for b = n*u it is bounded by n.
lev = []
for L in [2, 3, 5, 8, 11]:
    els = [l for l in primes_upto(40) if l != p][:L]
    k = 2
    def ksz(bcomp):
        s = 1
        for l, bl in zip(els, bcomp):
            s *= math.gcd(bl % (l**k) if bl % (l**k) else l**k, l**k)
        return s
    every_residue_is_n_times_unit = True  # by construction (see comment); recorded, not computed
    lev.append({"num_primes": L, "ker_b=0": ksz([0]*L), "ker_b=(l)_l": ksz(els), "ker_b=7": ksz([7]*L),
                "finite_level_saturates": every_residue_is_n_times_unit})
out["C7_N2_witnesses_kernel_growth"] = lev

# C8: the correct warrant for "the Q^{>0}-action on X0v(C)_E x R^{>0} is not properly discontinuous":
# the action on the PRODUCT is free (second coordinate), so "infinite isotropy" is not the reason; the
# reason is that (P0,u) is non-wandering: q_k = m_k/p^{j_k} -> 1, q_k != 1, m_k = 1 mod k!, gives
# F_{q_k} P0 = F_{m_k} P0 -> P0 and q_k^{-1} u -> u.  Same construction as C5 with s = 1; recorded here.
# Choice (corrected on first run: taking the largest m <= p^j with m = 1 mod k! can give m = p^j, i.e.
# q_k = 1): take j with p^j > 2 k * k!, and m_k = the largest integer <= p^j - 1 with m_k = 1 (mod k!).
# Then m_k != p^j, so q_k != 1, and |q_k - 1| <= (k! + 1)/p^j < 1/k.
rows = []
for k in range(1, 13):
    Mk = factorial(k)
    j = 1
    while p**j <= 2*k*Mk: j += 1
    t = p**j - 1
    m = t - ((t - 1) % Mk)
    qk = Fraction(m, p**j)
    rows.append({"k": k, "m_k": m, "j_k": j, "q_k_minus_1": float(qk - 1), "m_k_mod_k!": m % Mk if Mk > 1 else 0, "q_k_is_1": qk == 1})
out["C8_nonwandering_witness_qk_to_1"] = {"rows": rows[:6], "all_qk_ne_1_and_to_1": all((not r["q_k_is_1"]) and abs(r["q_k_minus_1"]) < 1.0/r["k"] and (r["m_k_mod_k!"] == 1 or r["k"] == 1) for r in rows)}
print(json.dumps({k: out[k] for k in ["C6_chart_membership", "C7_N2_witnesses_kernel_growth", "C8_nonwandering_witness_qk_to_1"]}, indent=1))
with open("B-corA1-adjudication-checks.json", "w") as fh:
    json.dump(out, fh, indent=1)
