#!/usr/bin/env python3
"""read-O second route for Thm R1 + the rung-1 controls (NOTE §1.2), from the NOTE's definitions only.
Exact integer power series mod u^(D+1): D_R(u) = prod_N (1-u^N)^{r_N}, N_P(n) = [u^n] D_R(u)/(1-qu),
rho = prod_N (1-q^-N)^{r_N} in mpmath (120 digits, N to 600), E(n) = N_P(n) - rho q^n.
Families (q=3, a=2): necklace r_N = M(2,N); regular r_N = round(2^N/N); random r_N ~ Bin(M(3,N), 2^N/(N M(3,N)))
(own RNG: numpy PCG64 seed 20261001 -- a different realization from the unit's)."""
import mpmath as mp, numpy as np
from o_rung1_bruteforce import necklace
mp.mp.dps = 120
q, a, D, NMAX = 3, 2, 60, 600

def series(r):          # r: dict N -> multiplicity (N <= D used exactly)
    c = [0] * (D + 1); c[0] = 1
    for N in range(1, D + 1):
        m = r[N]
        if m == 0: continue
        # multiply by (1-u^N)^m = sum_k binom(m,k)(-1)^k u^{Nk}
        new = [0] * (D + 1); b = 1
        for k in range(0, D // N + 1):
            if k: b = b * (m - k + 1) // k
            t = (-1) ** k * b
            for i in range(0, D + 1 - N * k):
                if c[i]: new[i + N * k] += t * c[i]
        c = new
    return c

def rho_of(r):
    s = mp.mpf(0)
    for N in range(1, NMAX + 1):
        s += r[N] * mp.log1p(-mp.mpf(q) ** (-N))
    return mp.e ** s

def report(name, r, nrange, scale):
    d = series(r); rho = rho_of(r)
    NP = [sum(d[k] * q ** (n - k) for k in range(n + 1)) for n in range(D + 1)]
    E = [mp.mpf(NP[n]) - rho * mp.mpf(q) ** n for n in range(D + 1)]
    vals = [scale(n, E[n]) for n in nrange]
    print(f"{name}: rho = {mp.nstr(rho, 30)}; d_1..d_12 = {d[1:13]}")
    print(f"   scaled E over n={nrange[0]}..{nrange[-1]}: min {mp.nstr(min(vals), 4)}, max {mp.nstr(max(vals), 4)}")
    return d, rho, E

nk = {N: necklace(a, N) for N in range(1, NMAX + 1)}
d, rho, E = report("necklace M(2,N)", nk, list(range(1, D + 1)), lambda n, e: e)
print(f"   D_R == 1 - 2u mod u^61: {d == [1, -2] + [0] * (D - 1)}; rho - 1/3 = {mp.nstr(rho - mp.mpf(1)/3, 5)}; "
      f"max_n<=60 |E(n)| = {mp.nstr(max(abs(x) for x in E[1:]), 5)}")
reg = {N: int(round(2 ** N / N)) if N <= 200 else int(mp.nint(mp.mpf(2) ** N / N)) for N in range(1, NMAX + 1)}
assert all(reg[N] <= necklace(q, N) for N in range(1, 80))
report("regular round(2^N/N)", reg, list(range(20, D + 1)), lambda n, e: e * n ** 1.5 / mp.mpf(2) ** (n / 2.0))
g = np.random.Generator(np.random.PCG64(20261001)); rnd = {}
for N in range(1, NMAX + 1):
    mu = mp.mpf(2) ** N / N
    if N <= 38:
        rnd[N] = int(g.binomial(necklace(q, N), float(mu / necklace(q, N))))
    elif N <= 70:
        rnd[N] = int(mp.nint(mu + mp.sqrt(mu) * g.standard_normal()))
    else:
        rnd[N] = int(mp.nint(mu))
report("random (own seed)", rnd, list(range(6, 23)), lambda n, e: e / mp.mpf(2) ** (n / 2.0))
