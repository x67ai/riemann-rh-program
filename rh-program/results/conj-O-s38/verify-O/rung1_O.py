#!/usr/bin/env python3
"""Reader-O rung 1 (NOTE §3.2): finite R = {2..13}, {3..19}. (i) exact one-period mean square in integers:
12 Q^3 (1/Q)int_0^Q E^2 = 12 sum A_n^2 - 12 phi sum A_n + 4 Q phi^2, A_n = Q N(n) - phi n, against phi 2^|R| Q^2 (= 12 Q^3 rho 2^|R|/12);
(ii) own dyadic windows [X, 2X): M(X) = (1/X) sum_n [(N(n) - rho(n+1/2))^2 + rho^2/12] vs rho 2^|R|/12. Log: logs/rung1_O.log"""
import math, numpy as np
for R in ((2, 3, 5, 7, 11, 13), (3, 5, 7, 11, 13, 17, 19)):
    Q = math.prod(R); phi = math.prod(p - 1 for p in R); rho = phi / Q; pred = rho * 2 ** len(R) / 12
    n = np.arange(Q, dtype=np.int64); f = np.ones(Q, dtype=bool); f[0] = False
    for p in R: f[::p] = False
    N = np.cumsum(f).astype(np.int64)                    # N(n) = #{1 <= k <= n : (k, Q) = 1}
    A = (Q * N - phi * n).tolist()
    lhs = 12 * sum(a * a for a in A) - 12 * phi * sum(A) + 4 * Q * phi * phi; rhs = phi * 2 ** len(R) * Q * Q
    print(f"R={R} Q={Q}: exact period mean square == rho 2^|R|/12 : {lhs == rhs}  ({lhs / (12 * Q ** 3):.15f} vs {pred:.15f})")
    for X in (6 * 10**5, 5 * 10**6, 4 * 10**7):
        g = np.ones(2 * X + 1, dtype=bool); g[0] = False
        for p in R: g[::p] = False
        Nn = np.cumsum(g)[X:2 * X].astype(np.float64); m = np.arange(X, 2 * X, dtype=np.float64)
        M = (((Nn - rho * (m + 0.5)) ** 2).sum() + X * rho * rho / 12) / X
        print(f"   window [{X:.0e}, {2*X:.0e}): M/pred - 1 = {M / pred - 1:+.2e}  (Q/X = {Q / X:.2g})")
