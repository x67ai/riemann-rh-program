#!/usr/bin/env python3
"""E1 rung 3 (H3): a positive-datum EXACT ghost pair — two cyclic cubic fields K_1, K_2 of the same conductor f = q_1 q_2
(q_i distinct primes = 1 mod 3), hence the same degree 3, signature (3,0), discriminant f^2 and archimedean functional A_K,
whose Dedekind data Lambda_{K_i}(n) agree for every n < p_0 and differ at n = p_0, where p_0 is the first prime that is
a non-cube modulo BOTH q_1 and q_2.  zeta_{K_i} = zeta * L(chi_i) * L(chi_i-bar) with chi_1 = chi_{q1} chi_{q2}, chi_2 = chi_{q1} chi_{q2}-bar
(cubic characters), so Lambda_K(p^k) = Lambda(p^k) * (1 + chi(p)^k + chi(p)^{-k}) = 3 Lambda(p^k) if chi(p)^k = 1 else 0, and
= Lambda(p^k) at the ramified p = q_i.  Exact integer arithmetic (indices mod 3); Lambda values printed as multiples of log p.
Search: q_1 < q_2 <= QMAX maximizing p_0.  No zero computation (brief H3(b))."""
import sys, time
from sympy import isprime, primerange, primitive_root, factorint
QMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 400
t0 = time.time()
qs = [q for q in primerange(7, QMAX + 1) if q % 3 == 1]
def cube_index(p, q, gen, table):
    # index of p mod q w.r.t. generator gen, reduced mod 3; None if p == q
    if p % q == 0: return None
    return table[p % q] % 3
tables = {}
for q in qs:
    g = primitive_root(q)
    tab = {}
    x = 1
    for k in range(q - 1):
        tab[x] = k
        x = x * g % q
    tables[q] = tab
primes = list(primerange(2, 3000))
best = []
for i, q1 in enumerate(qs):
    for q2 in qs[i + 1:]:
        for p in primes:
            if p == q1 or p == q2: continue
            a = tables[q1][p % q1] % 3; b = tables[q2][p % q2] % 3
            if a != 0 and b != 0:
                p0 = p; break
        best.append((p0, q1, q2))
best.sort(reverse=True)
print(f"search q_1 < q_2 <= {QMAX}, q_i = 1 mod 3 ({len(qs)} primes, {len(best)} pairs); top pairs by p_0 (first prime non-cube mod both):")
for p0, q1, q2 in best[:8]:
    print(f"  q_1 = {q1:4d}, q_2 = {q2:4d}, f = {q1*q2:7d}, |d_K| = f^2 = {q1*q2*q1*q2:12d}, p_0 = {p0}")
p0, q1, q2 = best[0]
print()
print(f"CHOSEN PAIR: conductor f = {q1}*{q2} = {q1*q2}; K_1 <-> chi_1 = chi_{q1} chi_{q2}, K_2 <-> chi_2 = chi_{q1} chi_{q2}^-1; p_0 = {p0}")
print("datum Lambda_{K_i}(n) / log p for prime powers n = p^k < p_0 (both fields), then at n = p_0:")
def lam(p, k, which):
    if p == q1 or p == q2: return 1
    a = tables[q1][p % q1] % 3; b = tables[q2][p % q2] % 3
    c = (a + b) % 3 if which == 1 else (a - b) % 3
    return 3 if (c * k) % 3 == 0 else 0
n = 2; agree = True
while n < p0:
    fac = factorint(n)
    if len(fac) == 1:
        p, k = next(iter(fac.items()))
        l1, l2 = lam(p, k, 1), lam(p, k, 2)
        tag = "split-split" if l1 == 3 and l2 == 3 else ("inert-inert" if l1 == 0 and l2 == 0 else ("ramified" if l1 == 1 else "DIFFER"))
        if l1 != l2: agree = False
        print(f"  n = {n:4d} = {p}^{k}: Lambda_K1 = {l1} log {p}, Lambda_K2 = {l2} log {p}   [{tag}]")
    n += 1
print(f"agreement for all prime powers n < p_0 = {p0}: {agree}")
print(f"  n = {p0:4d} = {p0}^1: Lambda_K1 = {lam(p0,1,1)} log {p0}, Lambda_K2 = {lam(p0,1,2)} log {p0}   [DIFFER: the ghost pair's first mismatch]")
import math
L = math.log(p0)
print(f"hence nu_K1, nu_K2 both lie in K_L(Lambda_K) for every L <= log p_0 = {L:.4f}, with the same A_K (degree 3, r1 = 3, |d| = {q1*q2*q1*q2}).")
# the count's strata for this pair: alpha(T) = L / ell_K(T), ell_K(T) = log(|d| T^3 / (2 pi)^3): alpha >= 1/2 iff T <= T_half
d = q1 * q2 * q1 * q2
T_half = 2 * math.pi * (p0 ** 2 / d) ** (1 / 3)
T_one = 2 * math.pi * (p0 / d) ** (1 / 3)
print(f"count strata at L = log p_0: alpha >= 1 for T <= {T_one:.4f}; alpha >= 1/2 for T <= {T_half:.4f}; free by count (alpha < 1/2) for T > {T_half:.4f}.")
print(f"elapsed {time.time()-t0:.2f} s")
