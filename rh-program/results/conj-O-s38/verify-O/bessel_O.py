#!/usr/bin/env python3
"""Reader-O sanity check of the §7 addition (local Fourier coefficients of E over [X, 2X] at nu = 1/b, b in <R>):
  c_X(1/b) := (1/X) int_X^{2X} E(x) e(-x/b) dx   versus   c(1/b) = rho mu(b) b / (2 pi i phi(b)),
for the reader's T_0.75 realization (seed 1001: R = data/bern_O_..._Rprimes.npy, rho from the header). E is linear of slope -rho on
[n, n+1), so each unit interval is integrated in closed form. Claim checked: c_X = c + O(b^2 X^(alpha-1+eps)). Log: logs/bessel_O.log"""
import math, numpy as np
R = np.load("data/bern_O_a0.75_s1001_1e9_Rprimes.npy")
rho = float(open("data/bern_O_a0.75_s1001_1e9_dec.csv").readline().split("rho=")[1].split()[0])
Rs = set(R[:40].tolist())
def rnums(B):
    out = [(1, 1, 1)]                                   # (b, mu(b), phi(b)) squarefree R-numbers <= B
    for p in sorted(Rs):
        out += [(b * p, -mu, ph * (p - 1)) for (b, mu, ph) in out if b * p <= B]
    return sorted(out)
for X in (10**6, 10**7, 10**8):
    lo, hi = X, 2 * X
    f = np.ones(hi + 1, dtype=bool); f[0] = False
    for p in R[R <= hi].tolist(): f[p::p] = False
    base = int(np.count_nonzero(f[:lo]))                 # N(lo - 1)
    B = rnums(60); acc = np.zeros(len(B), dtype=complex); C = 10**7
    for a in range(lo, hi, C):
        b_ = min(a + C, hi)
        N = base + np.cumsum(f[a:b_], dtype=np.int64); base = int(N[-1])
        n = np.arange(a, b_, dtype=np.float64); e = N - rho * n              # E(n+u) = e - rho u on [n, n+1)
        for k, (b, mu, ph) in enumerate(B):
            w = -2j * math.pi / b; I0 = (np.exp(w) - 1) / w; I1 = np.exp(w) / w - (np.exp(w) - 1) / w ** 2
            acc[k] += ((e * I0 - rho * I1) * np.exp(w * (n % b))).sum()     # exp(w n) = exp(w (n mod b)): exact phases
    print(f"X = {X:.0e}: b:|c_X(1/b) - c(1/b)|/|c(1/b)|   (leakage scale b^2 X^(alpha-1) = b^2*{X ** -0.25:.4f})")
    print("   " + "  ".join(f"{b}:{abs(acc[k] / X - rho * mu * b / (2j * math.pi * ph)) / abs(rho * mu * b / (2j * math.pi * ph)):.4f}"
                          for k, (b, mu, ph) in enumerate(B)))
