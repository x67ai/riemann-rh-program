#!/usr/bin/env python3
"""read-O: build R = {nextprime(p^2)} up to X and rho = prod_{p}(1 - 1/nextprime(p^2)) to ~30 digits, own code.
rho: exact product over p <= P0 (r_p by deterministic Miller-Rabin), tail prod_{p>P0}(1 - 1/r_p) = exp(-sum_{p>P0} 1/p^2 - ...) with
sum_{p>P0} p^-2 = primezeta(2) - sum_{p<=P0} p^-2 (mpmath, 40 digits); the neglected terms sum_{p>P0} (r_p - p^2)/p^4 and
sum_{p>P0} p^-4/2 are < 1e-18 for P0 = 1e6.  Writes R list (r <= X) and rho (decimal, and as a double-double pair hi/lo)."""
import sys, mpmath as mp
from o_zeta_checks import nextprime, primes_upto
mp.mp.dps = 40
X = int(float(sys.argv[1])); P0 = int(float(sys.argv[2])) if len(sys.argv) > 2 else 10 ** 6
ps = primes_upto(P0)
s_log = mp.mpf(0); s_p2 = mp.mpf(0); s_p4 = mp.mpf(0); R = []
for p in ps:
    r = nextprime(p * p)
    if r <= X: R.append(r)
    s_log += mp.log1p(-mp.mpf(1) / r); s_p2 += mp.mpf(1) / (p * p); s_p4 += mp.mpf(1) / mp.mpf(p) ** 4
tail = -(mp.primezeta(2) - s_p2) - (mp.primezeta(4) - s_p4) / 2
rho = mp.e ** (s_log + tail)
assert len(set(R)) == len(R), "collision in nextprime(p^2)"
R.sort()
hi = float(rho); lo = float(rho - mp.mpf(hi))
tag = f"{X:.0e}".replace("+", "")
with open(f"/private/tmp/rh-s40-lemmaG/R_sq_{tag}.txt", "w") as f:
    f.write("\n".join(map(str, R)) + "\n")
with open(f"/private/tmp/rh-s40-lemmaG/rho_sq_{tag}.txt", "w") as f:
    f.write(f"{mp.nstr(rho, 35)}\n{hi!r}\n{lo!r}\n")
print(f"X={X} P0={P0}: |R cap [1,X]| = {len(R)}, max r = {R[-1]}, rho = {mp.nstr(rho, 30)} (hi={hi!r}, lo={lo!r}), tail = {mp.nstr(tail, 12)}")
