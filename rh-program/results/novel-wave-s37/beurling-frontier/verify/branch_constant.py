#!/usr/bin/env python3
"""branch_constant.py — predicted systematic term of the greedy (c = 1) deletion from Theorem C, vs the data.

Near s0 = alpha/2, zeta_P(s) = K0 * (2s - alpha)^{1/2} * (1 + O(s - s0)), with
  K0 = zeta(s0) * exp(-P(1 - alpha/2) - H(alpha/2)) * exp(-(P0 + H(alpha))/2) * prod_{j>=3} exp(-S1(j s0)/j),
  P(w) = sum_p p^-w (continued), exp(-P(w)) = prod_{m sqfree} zeta(m w)^(-mu(m)/m),  P0 = sum_{m>=2} mu(m) log zeta(m)/m,
  H(s) = S1(s) - P(s+1-alpha) = s * int_1^inf D(u) u^{-s-1} du,  D = pi_R - F  (greedy: D = ceil(F) - F in [0,1)),
  S1(s) = sum_{p in R} p^-s.
The branch point contributes to N_P(x) - rho x the term  B(x) = K0*sqrt(2)/s0 * x^{s0} (log x)^{-3/2} / Gamma(-1/2)  (+ lower order).
Greedy selection is vectorized: #R(<=p) = ceil(F(p)), so p in R iff ceil(F(p)) > ceil(F(p-)).
Usage: python3 branch_constant.py alpha [Y=2e8]
"""
import sys, math
import numpy as np
import mpmath as mp

alpha = float(sys.argv[1]); Y = int(float(sys.argv[2])) if len(sys.argv) > 2 else 200_000_000
s0 = alpha / 2
# primes up to Y (odd sieve)
sv = np.ones(Y // 2 + 1, dtype=bool); sv[0] = False
for i in range(1, int(Y ** 0.5) // 2 + 1):
    if sv[i]:
        p = 2 * i + 1; sv[p * p // 2::p] = False
primes = np.concatenate(([2], 2 * np.nonzero(sv)[0] + 1)); primes = primes[primes <= Y].astype(np.float64)
w = primes ** (alpha - 1.0)
F = np.cumsum(w)
cF = np.ceil(F - 1e-12)
prevc = np.concatenate(([0.0], cF[:-1]))
inR = cF > prevc
R = primes[inR]
D = cF - F                      # D on [p_i, p_{i+1})
def H(sig):
    nxt = np.concatenate((primes[1:], [np.inf]))
    return float(np.sum(D * (primes ** -sig - np.where(np.isinf(nxt), 0.0, nxt ** -sig))))
mp.mp.dps = 30
def mob(n):
    m, k, res = n, 2, 1
    while k * k <= m:
        if m % k == 0:
            m //= k
            if m % k == 0: return 0
            res = -res
        k += 1
    return -res if m > 1 else res
def expmP(wv):  # exp(-P(w)) = prod_m zeta(m w)^(-mu(m)/m); only m = 1 can have zeta < 0 (integer power -1 there)
    val = 1 / mp.zeta(wv)
    for m in range(2, 400):
        mu = mob(m)
        if mu == 0: continue
        if m * wv > 80: break
        val *= mp.power(mp.zeta(m * wv), -mp.mpf(mu) / m)
    return val
P0 = mp.fsum(mob(m) * mp.log(mp.zeta(m)) / m for m in range(2, 400) if mob(m) != 0)
H_a, H_s0 = H(alpha), H(s0)
S1j = [float(np.sum(R ** (-j * s0))) for j in range(3, 40)]
tailj = mp.fsum(-mp.mpf(S1j[j - 3]) / j for j in range(3, 40))
K0 = mp.zeta(s0) * expmP(1 - s0) * mp.e ** (-H_s0) * mp.e ** (-(P0 + H_a) / 2) * mp.e ** tailj
coef = K0 * mp.sqrt(2) / s0 / mp.gamma(-0.5)
print("alpha=%.3f  Y=%.2g  #R(Y)=%d  H(alpha)=%.6f  H(alpha/2)=%.6f  P0=%.6f  exp(-P(1-a/2))=%s  zeta(s0)=%s"
      % (alpha, Y, len(R), H_a, H_s0, float(P0), mp.nstr(expmP(1 - s0), 8), mp.nstr(mp.zeta(s0), 8)))
print("K0=%s   branch term B(x) = %s * x^%.3f (log x)^-1.5" % (mp.nstr(K0, 8), mp.nstr(coef, 8), s0))
for x in (1e6, 1e7, 1e8, 1e9, 1e10):
    print("   x=%.0e  B(x)=%9.3f" % (x, float(coef) * x ** s0 * math.log(x) ** -1.5))
