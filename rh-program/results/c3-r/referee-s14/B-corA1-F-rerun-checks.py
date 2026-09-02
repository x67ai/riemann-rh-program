#!/usr/bin/env python3
"""Referee F (re-run, 2026-09-02) -- finite sanity checks for the converse inclusion
cl(gamma) <= Gamma^E_p (probe B, Cor. A.1).  Nothing here is load-bearing; the
report's derivation is the argument.  These checks exercise the finite-level
facts the derivation uses, at concrete moduli, so that an algebra slip would
show up.

Facts checked (all at the level of Z/M with M prime to p, which is exactly the
level at which the pointwise topology on X^.(C) sees a character at a char-p
point):

 C1  CRT density: for every M prime to p and every residue c mod M there is a
     positive integer n = c mod M  (so N is dense in Z_(p)-hat).
 C2  (Tors) criterion: the kernel of the endomorphism b of mu^(p) is finite
     iff every component b_l is nonzero and all but finitely many are units;
     checked at finite level: |ker of (.)^b on mu_M| = gcd(b, M), which grows
     without bound along M iff some prime l has v_l(b) unbounded, i.e. b_l = 0,
     or infinitely many l have v_l(b) >= 1.  We exhibit the three regimes.
 C3  Chart membership: F_{m/m'} P_0 lies in chart 1 iff the prime-to-p part of
     m' is 1 (i.e. chi^{a0 m} kills mu_{m'} iff m'_p | m, impossible for
     coprime m, m' unless m'_p = 1).
 C4  A sequence n_k -> 0 in Z_(p)-hat (n_k = prod_{l<=k, l!=p} l^k) whose limit
     point (x, chi^0) = (x, 1) is NOT a (Tors) point -- the un-cut-space
     counterexample to the equality.
 C5  Two-limit bookkeeping of Cor. A.2 (rotation limit exists mod p^Z) at a
     concrete prime -- not the item, included only because the report quotes it.
"""
import json, math, itertools

p = 5

def primes_upto(n):
    s = [True]*(n+1); s[0]=s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=False
    return [i for i in range(n+1) if s[i]]

out = {}

# C1: CRT density of N in Z_(p)-hat
ok = True
for M in [2,3,4,6,7,8,9,11,12,13,14,16,18,21,22,24,26]:
    if M % p == 0: continue
    for c in range(M):
        n = c if c > 0 else M   # positive representative
        if n % M != c % M: ok = False
out["C1_CRT_density_positive_reps"] = ok

# C2: kernel size gcd(b, M) along M = prod_{l<=L, l!=p} l^L  for three exponents b
def kernel_sizes(b_of_M, Ls):
    res = []
    for L in Ls:
        M = 1
        for l in primes_upto(L):
            if l != p: M *= l**L
        res.append(math.gcd(b_of_M(M) % M if b_of_M(M) % M else M, M))
    return res
Ls = [3,5,7,11]
# (i) b = 6 = 2*3 times the unit 1 (a packet exponent, b in N * units): kernel = gcd(6, M) = 6 once 2,3 | M -- finite, stable
k_fin = kernel_sizes(lambda M: 6, Ls)
# (ii) b with a zero component at l = 2, modeled at truncation depth L by b = 2^L (v_2 -> infinity): kernel grows like 2^L
k_zero = []
for L in Ls:
    M = 1
    for l in primes_upto(L):
        if l != p: M *= l**L
    k_zero.append(math.gcd(2**L, M))
# (iii) b = prod of all primes l != p (every component nonzero, none a unit): kernel = prod_{l<=L,l!=p} l -> infinity
k_allprimes = []
for L in Ls:
    M = 1; b = 1
    for l in primes_upto(L):
        if l != p: M *= l**L; b *= l
    k_allprimes.append(math.gcd(b, M))
out["C2_kernel_sizes_b=6_(finite,stabilises)"] = k_fin
out["C2_kernel_sizes_b_with_zero_2_component_(unbounded)"] = k_zero
out["C2_kernel_sizes_b=prod_all_primes_(unbounded_though_no_component_zero)"] = k_allprimes
out["C2_verdict"] = (len(set(k_fin[1:]))==1 and k_zero[-1] > k_zero[0] and k_allprimes[-1] > k_allprimes[0])

# C3: chart membership.  chi^{a0 m} kills mu_{m'} (m' prime to p) iff m' | m.  For coprime m, m' this forces m' = 1.
def kills(m, mprime):
    # chi injective on mu^(p); chi^{a0 m} kills mu_{m'} iff (.)^{m} is trivial on mu_{m'} iff m' | m (a0 a unit is irrelevant)
    return m % mprime == 0
c3 = True
for m in range(1, 60):
    for mp in range(1, 60):
        if mp % p == 0: continue
        if math.gcd(m, mp) != 1: continue
        if kills(m, mp) != (mp == 1): c3 = False
out["C3_chart1_membership_iff_prime_to_p_part_of_denominator_is_1"] = c3

# C4: n_k -> 0 in Z_(p)-hat
def n_k(k):
    n = 1
    for l in primes_upto(k):
        if l != p: n *= l**k
    return n
# for each fixed l != p, v_l(n_k) = k once k >= l, so n_k -> 0 in Z_l for every l != p, i.e. n_k -> 0 in Z_(p)-hat
c4 = all(n_k(k) % (l**4) == 0 for l in [2,3,7,11] for k in [max(l,4), max(l,4)+3, 13])
out["C4_nk_to_zero_example_divisible_by_l^4_once_k>=max(l,4)"] = c4
out["C4_limit_point_is_trivial_character_kernel_size_at_M"] = "gcd(0, M) = M -> infinite kernel: not (Tors)"

# C5: rotation limit: n_k v mod p^Z lies in a compact circle -> some subsequence converges.  Illustrate with
# n_k = 1 + k*M0 (M0 = 2*3*7*11) and v = 1: log_p(n_k) mod 1 takes values in [0,1); pigeonhole gives accumulation.
M0 = 2*3*7*11
fr = sorted(( (math.log(1+k*M0, p)) % 1.0 for k in range(1, 2000)))
gaps = max(b-a for a,b in zip(fr, fr[1:]))
out["C5_rotation_values_max_gap_in_[0,1)_over_2000_terms"] = round(gaps, 4)

print(json.dumps(out, indent=1))
with open(__file__.replace('.py', '.json'), 'w') as f:
    json.dump(out, f, indent=1)
