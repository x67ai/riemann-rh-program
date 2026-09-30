#!/usr/bin/env python3
"""o6 -- OPUS READER.  (a) NOTE §5(h) near-misses by the closed-form Fejer sum of o1 (S_F = sum_e E(e) T(e));
(b) NOTE §9 CONTROL 1: genus-1 data over F_5, L = 1 - t u + 5 u^2: b_d >= 0 for d <= 60 exactly for which t in [-12, 12];
    virtual curve t = 5: N_1..N_6, b_1..b_6.  Independent code (integer arithmetic, Moebius inversion)."""
import mpmath as mp
from fractions import Fraction
mp.mp.dps = 30
def T(c):
    c = mp.mpf(c); K = int(mp.ceil(c)) - 1
    return ((1 + 2 * (K - mp.mpf(K) * (K + 1) / (2 * c))) / c - 1) / 2
kmax = 400
# 2 -> 2.01: E = (delta_1 - delta_2) * sum_k delta_{2.01^k}
sf1 = mp.fsum(T(mp.mpf('2.01') ** k) - T(2 * mp.mpf('2.01') ** k) for k in range(kmax))
# (P \ {2}) u {sqrt2}: E telescopes to delta_1 + delta_{sqrt2}
sf2 = T(1) + T(mp.sqrt(2))
# P u {1.5}: E = sum_k delta_{1.5^k}
sf3 = mp.fsum(T(mp.mpf('1.5') ** k) for k in range(kmax))
print(f"(a) S_F: '2 -> 2.01' = {mp.nstr(sf1, 6)};  '(P minus 2) u sqrt2' = {mp.nstr(sf2, 6)};  'P u 1.5' = {mp.nstr(sf3, 6)}"
      "   (NOTE §5(h): 2.0e-3, 6.1e-2, 8.9e-2)")
def mobius(n):
    m, p, r = n, 2, 1
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0: return 0
            r = -r
        p += 1
    return -r if m > 1 else r
q, D = 5, 60
ok = []
for t in range(-12, 13):
    s = [2, t]
    for n in range(2, D + 1): s.append(t * s[-1] - q * s[-2])
    N = [None] + [q ** n + 1 - s[n] for n in range(1, D + 1)]
    b = [None] + [sum(mobius(d // e) * N[e] for e in range(1, d + 1) if d % e == 0) for d in range(1, D + 1)]
    assert all(b[d] % d == 0 for d in range(1, D + 1))
    b = [None] + [b[d] // d for d in range(1, D + 1)]
    if all(x >= 0 for x in b[1:]): ok.append(t)
    if t == 5: print("(b) t = 5 (virtual curve): N_1..N_6 =", N[1:7], "  b_1..b_6 =", b[1:7], "  min_{d<=60} b_d =", min(b[1:]))
print("    t in [-12,12] with b_d >= 0 for all d <= 60:", ok, "   Hasse |t| <= 2 sqrt5 = 4.47: t in [-4, 4]")
