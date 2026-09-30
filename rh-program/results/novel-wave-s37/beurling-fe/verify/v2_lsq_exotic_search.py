#!/usr/bin/env python3
"""v2 -- seed M1a beurling-fe.  The charter's experiment (item (4)): search for an exotic Beurling system by least squares
on the theta relation   rho + 2 psi(1/x) = sqrt(x) (rho + 2 psi(x)),   x on a log grid in [1/2, 2] (x = 1 excluded).

Model: K free generalized primes 1 < p_1 <= ... <= p_K < 12 (they are ALL generalized primes below 12), rho free.
Generalized integers >= 12 contribute <= exp(-pi*144/2) ~ 1e-98 to psi(x) for x >= 1/2: the truncation is exact to that level,
so on this grid the model is complete. A numerical near-solution is NOT an example (Theorem T says the only exact solution is Z,
rho = 1); the experiment maps the defect landscape and checks that the optimizer finds Z and nothing else at defect ~ 0.
"""
import numpy as np
from scipy.optimize import least_squares

rng = np.random.default_rng(20260930)
XS = np.exp(np.linspace(np.log(0.5), np.log(2.0), 42))
XS = XS[np.abs(XS - 1) > 1e-9]

def gen_integers(ps, X=12.0):
    ps = sorted(ps); out = [1.0]
    def rec(i0, v):
        for i in range(i0, len(ps)):
            w = v * ps[i]
            if w >= X: break
            out.append(w); rec(i, w)
    rec(0, 1.0)
    return np.array(out)

def residuals(theta):
    rho, ps = theta[0], np.sort(theta[1:])
    n = gen_integers(ps)
    psi = lambda x: np.exp(-np.pi * np.outer(x, n ** 2)).sum(axis=1)
    return (rho + 2 * psi(1 / XS)) - np.sqrt(XS) * (rho + 2 * psi(XS))

print("Z check: K=5 primes (2,3,5,7,11), rho=1  -> max|res| =",
      np.abs(residuals(np.array([1.0, 2, 3, 5, 7, 11]))).max())
summary = []
for K in range(1, 8):
    best = []
    for trial in range(300):
        p0 = np.sort(rng.uniform(1.05, 11.95, K)); r0 = rng.uniform(0.2, 3.0)
        try:
            sol = least_squares(residuals, np.concatenate([[r0], p0]),
                                bounds=([0.0] + [1.0001] * K, [10.0] + [11.999] * K), xtol=1e-15, ftol=1e-15, gtol=1e-15)
        except Exception as e:
            continue
        D = float(np.sqrt(np.mean(sol.fun ** 2)))
        best.append((D, sol.x[0], np.sort(sol.x[1:])))
    best.sort(key=lambda t: t[0])
    print(f"\nK = {K}: 300 random starts; five smallest RMS defects:")
    seen = 0
    for D, rho, ps in best:
        print(f"   RMS defect {D:.3e}   rho = {rho:.6f}   primes = {np.array2string(ps, precision=6)}")
        seen += 1
        if seen == 5: break
    summary.append((K, best[0][0], best[0][1], best[0][2]))
print("\nSUMMARY (best per K):")
for K, D, rho, ps in summary:
    print(f"  K={K}  best RMS defect {D:.3e}  rho={rho:.6f}  primes={np.array2string(ps, precision=6)}")
