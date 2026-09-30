#!/usr/bin/env python3
"""Reader-O spot check of the one recalled input: |chi(sigma+it)| = (|t|/2pi)^(1/2-sigma) (1 + O(1/|t|)), zeta(s) = chi(s) zeta(1-s).
Two routes: (i) chi(s) = zeta(s)/zeta(1-s) evaluated directly by mpmath's zeta (no Gamma formula); (ii) the closed form
chi(s) = 2^s pi^(s-1) sin(pi s/2) Gamma(1-s) via loggamma. Prints R = |chi|(|t|/2pi)^(sigma-1/2) and t*|R-1|. Log: logs/stirling_O.log"""
import mpmath as mp
mp.mp.dps = 30
print(" sigma      t    R(route i)             R(route ii)            t*|R-1|")
for sig in (-0.4, 0.05, 0.2, 0.375, 0.6, 1.2):
    for t in (10, 30, 100, 1000, 10000):
        s = mp.mpc(sig, t)
        chi1 = mp.zeta(s) / mp.zeta(1 - s)
        chi2 = mp.exp(s * mp.log(2) + (s - 1) * mp.log(mp.pi) + mp.log(mp.sin(mp.pi * s / 2)) + mp.loggamma(1 - s))
        R1 = abs(chi1) * (t / (2 * mp.pi)) ** (sig - 0.5); R2 = abs(chi2) * (t / (2 * mp.pi)) ** (sig - 0.5)
        print(f"{sig:6.3f} {t:6d}  {mp.nstr(R1, 18):<22} {mp.nstr(R2, 18):<22} {mp.nstr(t * abs(R2 - 1), 6)}")
