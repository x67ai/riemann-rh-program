#!/usr/bin/env python3
"""o5 -- OPUS READER.  Theorem C's identity (C_q) on an example NOT in the writer's list:
F(s) = zeta(s)(1 + 5^{1/2-s}) + L(s, chi_5), q = 5: coefficients 1 + chi_5(m) + sqrt5 1_{5|m} >= 0, conductor-5 FE (root number 1).
(C_q): rho_q (1 - q^{-1/2}) = 2 q^{-1/2} int S(t/q) dN(t),  rho_q = sqrt(q) Res_{s=1} F = sqrt5 + 1.  Prediction: both sides 4/sqrt5.
Also the conductor-5 FE of Lambda_F(s) = (5/pi)^{s/2} Gamma(s/2) F(s) at two points."""
import mpmath as mp
mp.mp.dps = 30
q = 5; a = mp.sqrt(5); chi = lambda m: [0, 1, -1, -1, 1][m % 5]
S = lambda t: (mp.sin(mp.pi * t) / (mp.pi * t)) ** 2 if t else mp.mpf(1)
coef = lambda m: 1 + chi(m) + (a if m % 5 == 0 else 0)
M = 200000
tail = lambda: mp.mpf(0)
rhs_trunc = 2 / a * mp.fsum(coef(m) * S(mp.mpf(m) / q) for m in range(1, M + 1))
# tail of sum_{m>M} c(m) S(m/5) ~ (q^2/pi^2) * mean_period[c(m) sin^2(pi m/q)] / M  (c 5-periodic here)
pmean = lambda c: mp.fsum(c(m) * mp.sin(mp.pi * m / q) ** 2 for m in range(1, q + 1)) / q
rhs = rhs_trunc + 2 / a * q * q / mp.pi ** 2 * pmean(coef) / M
rho_q = a * (1 + 1 / a)
print("(C_q) q=5: LHS rho_q(1-q^-1/2) =", mp.nstr(rho_q * (1 - 1 / a), 12), "  RHS (m <= 2e5, + mean-value tail) =", mp.nstr(rhs, 12),
      "  4/sqrt5 =", mp.nstr(4 / a, 12))
print("   predicted sub-identity sum_{m>=1} chi_5(m) S(m/5) = 0:", mp.nstr(mp.fsum(chi(m) * S(mp.mpf(m) / 5) for m in range(1, M + 1)) + q * q / mp.pi ** 2 * pmean(chi) / M, 5), "(with tail)")
F = lambda s: mp.zeta(s) * (1 + mp.power(5, mp.mpf(1) / 2 - s)) + mp.dirichlet(s, [0, 1, -1, -1, 1])
Lam = lambda s: mp.power(q / mp.pi, s / 2) * mp.gamma(s / 2) * F(s)
for s in (mp.mpc(0.2, 4), mp.mpc(1.7, -9)):
    print(f"   FE: |Lambda_F(s) - Lambda_F(1-s)| at s = {mp.nstr(s, 3)}: {mp.nstr(abs(Lam(s) - Lam(1 - s)), 4)}  (|Lambda_F| = {mp.nstr(abs(Lam(s)), 5)})")
