#!/usr/bin/env python3
"""U4-sparse: tau_c = root of Lambda(tau) := I1(2 sqrt tau)/sqrt tau - 1 = 1 (scaling-limit load of the lattice monoid), and the
finite-rho crossing S_rho(z) = 1 by bisection in z with the exact enumerator ./qs (log: logs/tauc.log)."""
import mpmath as mp, subprocess, math, sys
mp.mp.dps = 30
Lam = lambda t: mp.besseli(1, 2*mp.sqrt(t))/mp.sqrt(t) - 1
tc = mp.findroot(lambda t: Lam(t) - 1, 1.5)
print(f"tau_c = {mp.nstr(tc, 15)}   check Lambda(tau_c) = {mp.nstr(Lam(tc), 15)}   series check sum tau^j/(j!(j+1)!) = "
      f"{mp.nstr(mp.nsum(lambda j: tc**j/(mp.factorial(j)*mp.factorial(j+1)), [1, mp.inf]), 15)}")
qs = sys.argv[1]
for D in (16, 24, 32):
    lo, hi = 1e3, 1e14
    for _ in range(40):
        mid = math.sqrt(lo*hi)
        out = subprocess.run([qs, str(D), f"{mid:.6e}"], capture_output=True, text=True).stdout.splitlines()[1].split()
        if float(out[1]) < 1: lo = mid
        else: hi = mid
    rho = math.pi/D
    print(f"rho=pi/{D}: S_rho(z)=1 at z = {lo:.4e}, tau = rho*log z = {rho*math.log(lo):.4f}, Q(z) = {out[2]}")
