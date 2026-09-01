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
