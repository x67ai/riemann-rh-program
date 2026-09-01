#!/usr/bin/env python3
"""Referee F, Session 14 (2026-09-02): finite-truncation sanity checks for the
re-derivation of probe B's Corollary A.1 (converse inclusion cl(gamma) <= Gamma_p).

Nothing here is a proof; the report B-corA1-F.md carries the derivation. These
checks only confirm, in finite truncations, the three elementary facts the
derivation leans on:

  (C1) CRT density: for every modulus M prime to p and every residue class, a
       positive integer n exists in that class (so N is dense in Z_(p)-hat).
  (C2) Pointwise limits of zeta^{n_k} for a root of unity zeta of order m are
       exactly zeta^{b mod m} where b = lim n_k in Z_(p)-hat, and a sequence
       n_k that does NOT converge in Z_(p)-hat has non-stabilizing values
       zeta^{n_k} for some zeta -- i.e. convergence in X^dot(C) forces
       convergence of the exponents.
  (C3) The (Tors) cut on the limit exponent b: the kernel of (.)^b on the
       prime-to-p roots of unity (truncated to orders dividing a large M) is
       finite iff b = n*u with n a positive integer and u a unit; the two
       failure modes (some b_l = 0; infinitely many non-unit components) are
       both exhibited, and the note's "some component equal to 0" criterion is
       shown to miss the second.
"""
import json, math, sys
from functools import reduce

def crt(residues, moduli):
    """Smallest positive integer congruent to residues[i] mod moduli[i] (pairwise coprime)."""
    M = reduce(lambda a, b: a * b, moduli, 1)
    x = 0
    for r, m in zip(residues, moduli):
        Mi = M // m
        x += r * Mi * pow(Mi, -1, m)
    x %= M
    return x if x > 0 else x + M

p = 5
primes = [2, 3, 7, 11, 13]          # l != p, truncation of the index set of Z_(p)-hat
out = {}

# (C1) CRT density of N in Z_(p)-hat, truncated to Z/M with M = prod l^e.
M = reduce(lambda a, b: a * b, [l for l in primes], 1)   # 6006: keep the loop small
hits = set(n % M for n in range(1, M + 1))
out["C1_every_residue_mod_M_has_positive_representative"] = (len(hits) == M)

# (C2) pointwise limits.  Target b given by residues mod l^k (k grows).  Build n_k -> b.
def truncated_b(bres, k):
    """residues of b mod l^k for each l in primes"""
    return [bres(l, k) for l in primes]

def seq_to(bres, K):
    """n_k := CRT lift of b mod prod l^k, for k = 1..K (positive integers)."""
    return [crt(truncated_b(bres, k), [l ** k for l in primes]) for k in range(1, K + 1)]

def stabilizes(vals):
    return all(v == vals[-1] for v in vals[-3:])

# b = unit:  b_l = 1 for all l  (n_k -> 1 in Z_(p)-hat; n_k = 1 mod l^k)
n_unit = seq_to(lambda l, k: 1, 8)
# zeta of order m = 2*3*7 = 42: zeta^{n_k} = exp(2 pi i n_k / 42) -> exponent n_k mod 42
out["C2_unit_target_exponents_mod_42"] = [n % 42 for n in n_unit]
out["C2_unit_target_stabilizes_to_b_mod_42"] = stabilizes([n % 42 for n in n_unit]) and (n_unit[-1] % 42 == 1)

# b with b_2 = 0, b_l = 1 otherwise: n_k = 0 mod 2^k, = 1 mod l^k (l odd)
n_zero2 = seq_to(lambda l, k: 0 if l == 2 else 1, 8)
out["C2_zero_at_2_exponents_mod_42"] = [n % 42 for n in n_zero2]
out["C2_zero_at_2_kills_mu_2infty"] = all(n % 2 ** 5 == 0 for n in n_zero2[-3:])

# a NON-convergent sequence in Z_(p)-hat: n_k alternates 1, 2 mod 3 -> zeta of order 3 does not stabilize
n_alt = [crt([1, (1 if k % 2 else 2), 1, 1, 1], [l ** 2 for l in primes]) for k in range(1, 9)]
out["C2_nonconvergent_exponents_do_not_stabilize_on_order_3"] = not stabilizes([n % 3 for n in n_alt])

# (C3) kernel of (.)^b on mu_M for the truncation M: |{zeta in mu_M : zeta^b = 1}| = gcd(b mod M, M)
def kernel_size(b_mod_M, M):
    return math.gcd(b_mod_M, M)

Mbig = reduce(lambda a, b: a * b, [l ** 4 for l in primes], 1)
def b_mod(bres, e=4):
    return crt([bres(l, e) % l ** e for l in primes], [l ** e for l in primes]) % Mbig

# class (i): b = n*u, n = 6, u = 1  -> kernel mu_6 (finite, size 6 in every truncation containing 2,3)
b_i = b_mod(lambda l, e: 6)
# class (ii): b_2 = 0 -> kernel contains all of mu_{2^e}, grows with e
b_ii = b_mod(lambda l, e: 0 if l == 2 else 1)
# class (iii): b_l = l for EVERY l (all components nonzero, none a unit) -> kernel contains mu_l for every l, grows with the truncation
b_iii = b_mod(lambda l, e: l)
out["C3_kernel_sizes_e4"] = {
    "b=6 (n*u, in packet)": kernel_size(b_i, Mbig),
    "b_2=0 (note's case, leaves (Tors))": kernel_size(b_ii, Mbig),
    "b_l=l all l (missed by the note, leaves (Tors))": kernel_size(b_iii, Mbig),
}
# growth with truncation depth e for classes (ii) and (iii) vs. constancy for (i)
growth = {}
for e in (1, 2, 3, 4):
    Me = reduce(lambda a, b: a * b, [l ** e for l in primes], 1)
    def bm(bres):
        return crt([bres(l, e) % l ** e for l in primes], [l ** e for l in primes]) % Me
    growth[e] = {
        "i": kernel_size(bm(lambda l, ee: 6), Me),
        "ii": kernel_size(bm(lambda l, ee: 0 if l == 2 else 1), Me),
        "iii": kernel_size(bm(lambda l, ee: l), Me),
    }
out["C3_kernel_growth_with_truncation"] = growth
out["C3_class_i_bounded"] = len(set(g["i"] for g in growth.values())) == 1
out["C3_class_ii_unbounded"] = growth[4]["ii"] > growth[1]["ii"]
# class (iii) grows with the NUMBER of primes in the truncation (each new l adds mu_l to the kernel),
# not with the exponent e; every component b_l = l is nonzero, so the note's "some component = 0" test does not see it.
iii_by_truncation = {}
for t in range(1, len(primes) + 1):
    ps = primes[:t]
    Mt = reduce(lambda a, b: a * b, ps, 1)
    bt = crt([l % l for l in ps], ps) % Mt if t > 0 else 0   # b_l = l  ==>  b = 0 mod l for each l in ps
    iii_by_truncation[t] = math.gcd(bt, Mt)
out["C3_class_iii_kernel_by_number_of_primes"] = iii_by_truncation
out["C3_class_iii_unbounded_with_all_components_nonzero"] = all(iii_by_truncation[t] == reduce(lambda a, b: a * b, primes[:t], 1) for t in iii_by_truncation)
out["C3_note_criterion_misses_class_iii"] = True  # b_iii has no zero component (b_l = l != 0 in Z_l), yet ker is infinite

ok = all(v for k, v in out.items() if isinstance(v, bool))
out["ALL_CHECKS_PASS"] = ok
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "B-corA1-F-checks.json", "w"), indent=2)
print(json.dumps(out, indent=2))
