#!/usr/bin/env python3
"""rung1_ff.py — lemmaG-s39, the function-field rung (F_q[T], RH true) of Conjecture O, degree-wise.
Necklace deletion: delete, for every N, M(a,N) = (1/N) sum_{d|N} mu(N/d) a^d monic irreducibles of degree N (any choice; here
the first ones in a fixed order), 2 <= a < q. Claim (NOTE §1.3): D_R(u) = prod_N (1-u^N)^{M(a,N)} = 1 - a u, so the number of
R-free monic polynomials of degree n is q^n - a q^{n-1} EXACTLY (n >= 1): E(n) = 0, while alpha_R = log a / log q.
(A) brute force in F_3[T], a = 2, degrees <= 9: actual factorization-free counting of R-free polynomials.
(B) exact generating-function counts to degree 60 for the necklace, 'regular' (r_N = round(a^N/N)) and random deletions."""
from fractions import Fraction as Fr
import random, math

def mobius(n):
    r, m, p = 1, n, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0: return 0
            r = -r
        p += 1
    return -r if m > 1 else r

def necklace(a, N):
    return sum(mobius(N // d) * a ** d for d in range(1, N + 1) if N % d == 0) // N

def pmul(f, g, q):                       # coefficient lists, low degree first, monic
    h = [0] * (len(f) + len(g) - 1)
    for i, x in enumerate(f):
        if x:
            for j, y in enumerate(g): h[i + j] = (h[i + j] + x * y) % q
    return h

def idx(f, q):                           # monic poly of degree n -> index of its lower coefficients
    return sum(c * q ** i for i, c in enumerate(f[:-1]))

def allmonic(n, q):
    for k in range(q ** n):
        f, m = [], k
        for _ in range(n): f.append(m % q); m //= q
        yield f + [1]

def brute(q, a, nmax):
    red = {n: bytearray(q ** n) for n in range(1, nmax + 1)}     # 1 = reducible
    irr = {}
    for n in range(1, nmax + 1):
        irr[n] = [f for f in allmonic(n, q) if not red[n][idx(f, q)]]
        for m in range(1, nmax - n + 1):                           # mark products f*g, deg g = m
            for g in allmonic(m, q):
                for f in irr[n]:
                    red[n + m][idx(pmul(f, g, q), q)] = 1
    assert all(len(irr[n]) == necklace(q, n) for n in irr), "irreducible count != M(q,n)"
    R = {n: irr[n][:necklace(a, n)] for n in irr}
    bad = {n: bytearray(q ** n) for n in range(1, nmax + 1)}      # 1 = divisible by some R-irreducible
    for n in R:
        for f in R[n]:
            bad[n][idx(f, q)] = 1
            for m in range(1, nmax - n + 1):
                for g in allmonic(m, q): bad[n + m][idx(pmul(f, g, q), q)] = 1
    out = []
    for n in range(1, nmax + 1):
        NP = q ** n - sum(bad[n]); out.append((n, len(irr[n]), len(R[n]), NP, q ** n - a * q ** (n - 1)))
    return out

def gf_counts(q, rN, nmax):              # N_P(n) = [u^n] prod_N (1-u^N)^{r_N} / (1 - q u), exact integers
    D = [0] * (nmax + 1); D[0] = 1
    for N in range(1, nmax + 1):          # multiply by (1 - u^N)^{r_N} = sum_j C(r_N, j) (-1)^j u^{N j}  (exact integers)
        r = rN[N]
        if r == 0: continue
        B = [0] * (nmax + 1); c = 1; j = 0
        while N * j <= nmax:
            B[N * j] = c * (-1) ** j; c = c * (r - j) // (j + 1); j += 1
        D = [sum(D[i] * B[k - i] for i in range(k + 1)) for k in range(nmax + 1)]
    NP, acc = [], 0
    for n in range(nmax + 1):
        acc = acc * q + D[n]; NP.append(acc)
    return NP, D

def rho_of(q, rN, Nmax):
    lr = 0.0
    for N in range(1, Nmax + 1): lr += rN(N) * math.log1p(-q ** (-N))
    return math.exp(lr)

q, a = 3, 2
print("(A) brute force F_3[T], a = 2, necklace deletion: n, #irr(n), #R(n) = M(2,n), N_P(n) counted, q^n - a q^(n-1)")
for row in brute(q, a, 8): print("   ", row, "OK" if row[3] == row[4] else "MISMATCH")
nmax = 60
print("(B) exact generating-function counts to degree %d, q = %d, a = %d; E(n) = N_P(n) - rho q^n" % (nmax, q, a))
rng = random.Random(20261001)
designs = {"necklace": lambda N: necklace(a, N), "regular round(a^N/N)": lambda N: max(0, round(a ** N / N))}
rr = {N: sum(1 for _ in range(necklace(q, N)) if rng.random() < a ** N / (N * necklace(q, N))) if N <= 22 else None for N in range(1, 23)}
for name, f in designs.items():
    rN = [0] + [f(N) for N in range(1, nmax + 1)]
    NP, D = gf_counts(q, rN, nmax)
    rho = rho_of(q, f, 400)
    E = [NP[n] - rho * q ** n for n in range(nmax + 1)]
    print("  %-22s rho=%.15f  E(n)/a^(n/2) at n=10,20,30,40,50,60: %s" % (name, rho, " ".join("%.3e" % (E[n] / a ** (n / 2)) for n in (10, 20, 30, 40, 50, 60))))
    print("  %-22s D_R coefficients d_0..d_12: %s" % ("", D[:13]))
# random deletion (independent choices, degrees <= 22 exactly; beyond: the mean a^N/N rounded, so E(n) for n <= 22 is the random part)
rN = [0] + [rr[N] for N in range(1, 23)] + [round(a ** N / N) for N in range(23, nmax + 1)]
NP, D = gf_counts(q, rN, 30)
fr = lambda N: rN[N] if N < len(rN) else round(a ** N / N)
rho = rho_of(q, fr, 400)
print("  %-22s rho=%.15f  E(n)/a^(n/2), n=6..22: %s" % ("random (seed 20261001)", rho, " ".join("%.2f" % ((NP[n] - rho * q ** n) / a ** (n / 2)) for n in range(6, 23, 2))))
