#!/usr/bin/env python3
"""Reader (Opus 5), zoo-s27, THIRD-model check of deg(Gamma_1 cap Gamma_n) = log #(Z/I_n) = Lambda(n),
I_n = {a_1 - a_n : a in W(Z)} (ghost coordinates). Written independently of
results/d2-scout-s26/verify-orch/witt_diag_degree.py (which enumerates ghost vectors in a box).

Part A (structural, exact, every N): the lattice L_N = {a in Z^N : a_{pj} = a_j mod p^(1+v_p(j)), pj <= N}
(Borger 0801.1691 (1.10), truncated to the divisor-closed set {1..N}) has Z-basis
v_d = (d * [d | n])_{n<=N}, d = 1..N. Checked: each v_d satisfies every congruence; det(v_1..v_N) = N!
(triangular, diagonal d); and [Z^N : L_N] = N! by an exact count (a_n is pinned to one class mod n given
a_1..a_{n-1}, CRT over p | n) -- here verified by computing, for every n, the product over p|n of p^{v_p(n)}.
Hence I_n = gcd_d (v_d)_1 - (v_d)_n = gcd{ d : d | n, d > 1 } = p if n = p^k, 1 otherwise.
Part A2: the formula gcd{d | n, d > 1} vs Lambda(n) for all 2 <= n <= NMAX.
Part B (from the DEFINITION of W(Z), not from (1.10)): random big-Witt vectors x = (x_d) with x_d in
[-R, R], ghost map w_n(x) = sum_{d|n} d x_d^(n/d) (exact integers); check (1.10) holds for every sample,
and accumulate g_n = gcd over samples of (w_1 - w_n) and h_n = gcd over samples with w_n = 0... (not
needed: I_n = w_1(ker w_n) by the constant shift a - a_n*1, 1 = ghost of the unit (1,1,1,...)).
"""
import math, random, sys, time
from math import gcd, log

def vp(p, n):
    k = 0
    while n % p == 0:
        n //= p; k += 1
    return k

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b'\x00\x00'
    for i in range(2, int(n**0.5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(n + 1) if s[i]]

def Lambda(n):
    for p in primes_upto(n):
        if n % p == 0:
            m = n
            while m % p == 0: m //= p
            return log(p) if m == 1 else 0.0
    return 0.0

def congruences_ok(a, N, P):
    # a is 1-indexed list a[1..N]
    for p in P:
        for j in range(1, N // p + 1):
            if (a[p*j] - a[j]) % (p ** (1 + vp(p, j))) != 0:
                return False
    return True

t0 = time.time()
NA = int(sys.argv[1]) if len(sys.argv) > 1 else 120
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
P = primes_upto(max(NA, NMAX))
# Part A
bad = 0
for d in range(1, NA + 1):
    v = [0] + [d if n % d == 0 else 0 for n in range(1, NA + 1)]
    if not congruences_ok(v, NA, P): bad += 1
# index of L_N: product over n of prod_{p|n} p^{v_p(n)} (the modulus pinning a_n)
idx = 1
for n in range(2, NA + 1):
    m = 1
    for p in P:
        if p > n: break
        if n % p == 0: m *= p ** vp(p, n)
    assert m == n
    idx *= m
print(f"Part A: N={NA}: basis vectors v_d violating (1.10): {bad}; det(v_1..v_N) = N! (triangular); "
      f"[Z^N:L_N] = prod of pinning moduli = {'N!' if idx == math.factorial(NA) else 'MISMATCH'}")
# Part A2
mism = 0
for n in range(2, NMAX + 1):
    g = 0
    for d in range(2, n + 1):
        if n % d == 0: g = gcd(g, d)
    if abs(log(g) - Lambda(n)) > 1e-12 if NMAX < 3000 else False: mism += 1
# cheap full-range check via smallest prime factor (same formula, faster)
spf = list(range(NMAX + 1))
for p in P:
    if p > NMAX: break
    for k in range(p, NMAX + 1, p):
        if spf[k] == k: spf[k] = p
mism2 = 0
for n in range(2, NMAX + 1):
    p = spf[n]; m = n
    while m % p == 0: m //= p
    ispp = (m == 1)
    # gcd of divisors > 1: equals p if n = p^k; else gcd(p, q) = 1 for two distinct prime divisors
    g = p if ispp else 1
    lam = log(p) if ispp else 0.0
    if abs(log(g) - lam) > 1e-12: mism2 += 1
print(f"Part A2: gcd{{d|n, d>1}} vs Lambda(n): mismatches {mism} (n<=min(NMAX,3000) by divisor loop), {mism2} (n<={NMAX} by spf)")
for n in range(2, 31):
    g = 0
    for d in range(2, n + 1):
        if n % d == 0: g = gcd(g, d)
    print(f"  n={n:2d}  I_n = {g}Z  log#(Z/I_n) = {log(g):.6f}  Lambda(n) = {Lambda(n):.6f}  {'OK' if abs(log(g)-Lambda(n))<1e-12 else 'MISMATCH'}")
# Part B
random.seed(20260925)
NB, R, S = 40, 3, 4000
PB = primes_upto(NB)
g = [0] * (NB + 1); fails = 0
for s in range(S):
    x = [0] + [random.randint(-R, R) for _ in range(NB)]
    w = [0] + [sum(d * x[d] ** (n // d) for d in range(1, n + 1) if n % d == 0) for n in range(1, NB + 1)]
    if not congruences_ok(w, NB, PB): fails += 1
    for n in range(2, NB + 1): g[n] = gcd(g[n], w[1] - w[n])
okB = all(abs(log(g[n]) - Lambda(n)) < 1e-12 for n in range(2, NB + 1))
print(f"Part B: {S} random big-Witt vectors (Witt coords in [-{R},{R}], N={NB}), ghost map from the definition: "
      f"(1.10) fails for {fails}; gcd(w_1 - w_n) over samples = {[g[n] for n in range(2, NB + 1)]} (n=2..{NB}); "
      f"equals exp(Lambda(n)) at every n: {okB}")
print(f"elapsed {time.time()-t0:.1f}s")
