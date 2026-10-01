#!/usr/bin/env python3
"""Clipped-cumulant model of the forced overshoot (NOTE §3): squarefree points with k generators.
Exact-flat needs b_k = kappa_k(tau) (Bernoulli cumulants, Theorem 2.1(a)); the greedy cannot go below 0, so model
b_j = kappa_j for j < k0 (first negative cumulant), b_j = 0 for j >= k0. Then the composite load at a squarefree point with
k generators, in units of the per-point target tau, is c_k/tau = (M_k - b_k)/tau, M_k = k! [t^k] exp(sum_{j<k0} kappa_j t^j/j!).
Also: the same with every b_j clipped at 0 for ALL j (b_j = max(kappa_j, 0)) - the 'positive part' model.
Usage: python3 clipped_cumulant_model.py > logs/clipped_cumulant_model.log"""
from fractions import Fraction as Fr
from math import factorial
def cumulants(tau, K):
    G = [Fr(1)] + [tau / factorial(n) for n in range(1, K + 1)]
    F = [Fr(0)] * (K + 1)
    for n in range(1, K + 1):
        s = G[n] * n
        for k in range(1, n): s -= k * F[k] * G[n - k]
        F[n] = s / n
    return [F[k] * factorial(k) for k in range(K + 1)]
def exp_series(c, K):  # c[k] = coefficient of t^k/k!; returns moments M_k = k![t^k] exp(sum c_k t^k/k!)
    a = [Fr(0)] + [c[k] / factorial(k) for k in range(1, K + 1)]
    E = [Fr(1)] + [Fr(0)] * K
    for n in range(1, K + 1):   # n E_n = sum_{k=1}^n k a_k E_{n-k}
        E[n] = sum(k * a[k] * E[n - k] for k in range(1, n + 1)) / n
    return [E[k] * factorial(k) for k in range(K + 1)]
K = 24
for t in (Fr(3, 100), Fr(3, 40), Fr(3, 20), Fr(3, 10)):
    kap = cumulants(t, K)
    k0 = next(k for k in range(1, K + 1) if kap[k] < 0)
    trunc = [kap[j] if j < k0 else Fr(0) for j in range(K + 1)]
    pos = [max(kap[j], Fr(0)) for j in range(K + 1)]
    Mt, Mp = exp_series(trunc, K), exp_series(pos, K)
    ct = [float((Mt[k] - trunc[k]) / t) for k in range(K + 1)]
    cp = [float((Mp[k] - pos[k]) / t) for k in range(K + 1)]
    print(f"tau={float(t):.3f} k0={k0}")
    print("  truncated model c_k/tau, k=2..24: " + " ".join(f"{ct[k]:.3g}" for k in range(2, K + 1)))
    print("  positive-part model c_k/tau     : " + " ".join(f"{cp[k]:.3g}" for k in range(2, K + 1)))
    print("  ratio c_{k+1}/c_k (truncated)   : " + " ".join(f"{ct[k+1]/ct[k]:.3g}" for k in range(k0, K)))
