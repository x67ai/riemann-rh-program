# U1-lookahead: rigorous lower bound for zeta_P(sigma) from the powers of the first prime (NOTE §4, Theorem 4.1).
# Any discrete system with E >= -tau everywhere and first prime p1 has N(u) >= 1 + k(u), k(u) = #{j >= 1 : p1^j <= u}, so
#   E(u) >= max(-tau, k(u) - rho(u-1)),  and (s40 Lemma 1.5, valid for sigma > theta under (B))
#   zeta_P(sigma) >= Lam(sigma) := 1 - tau - rho/(1-sigma) + sigma * Int_1^inf (k(u) + tau - rho(u-1))^+ u^{-sigma-1} du.
# The integral is a finite sum of closed forms. sigma_L := largest root of Lam in (0,1); then zeta_P(sigma_L - 0) > 0, so under (B)
# with theta < sigma_L the real zero lies in (sigma_L, 1).  Exact arithmetic in mpmath (40 digits); bisection to 1e-12.
import sys
from mpmath import mp, mpf, pi, log, floor
mp.dps = 40
def Lam(sigma, rho, tau, p1):
    s = mpf(sigma); tot = mpf(0); k = 0
    while True:
        lo = p1 ** k; ck = 1 + (k + tau) / rho          # integrand (k + tau + rho - rho*u) >= 0 iff u <= ck
        hi = min(p1 ** (k + 1), ck)
        if k > 0 and lo >= ck and p1 >= 1 + 1 / (k + rho + tau): break   # empty now and for all larger k (c_{k+1}/c_k < p1)
        if hi > lo:
            A = k + tau + rho
            F = lambda u: A * (-u ** (-s) / s) - rho * (u ** (1 - s) / (1 - s))
            tot += F(hi) - F(lo)
        k += 1
        if k > 10 ** 6: raise RuntimeError("no termination")
    return 1 - tau - rho / (1 - s) + s * tot
def root(rho, tau, p1):
    # scan down from 1 for the first sign change, then bisect
    grid = [1 - mpf(10) ** (-e) for e in [6, 5, 4, 3]] + [mpf(j) / 200 for j in range(199, 0, -1)]
    prev = None
    for g in sorted(set(grid), reverse=True):
        v = Lam(g, rho, tau, p1)
        if v > 0:
            lo, hi = g, prev
            for _ in range(60):
                m = (lo + hi) / 2
                if Lam(m, rho, tau, p1) > 0: lo = m
                else: hi = m
            return lo
        prev = g
    return None
for rho_name, rho in [("pi/16", pi / 16), ("pi/32", pi / 32)]:
    for tau in [mpf(1) / 2, mpf(1) / 4, mpf(1) / 10, mpf(1) / 20, mpf(1) / 50, mpf(1) / 100, mpf(1) / 1000]:
        p1 = 1 + tau / rho
        sL = root(rho, tau, p1); r0 = 1 - rho - tau
        print(f"rho={rho_name} tau={mp.nstr(tau, 4)} p1={mp.nstr(p1, 8)}  Thm1.6 floor r0/(r0+rho)={mp.nstr(r0 / (r0 + rho), 6)}  "
              f"power-bump root sigma_L={mp.nstr(sL, 8)}  1-sigma_L={mp.nstr(1 - sL, 4)}  U needs theta < sigma_L/2 = {mp.nstr(sL / 2, 6)}")
