#!/usr/bin/env python3
"""Reader (Opus 5) independent check, zoo-s27: at the first N=200 nontrivial zeros rho_k
of zeta, compute c_k = Re[1/(rho_k * zeta'(rho_k))] (the Mobius-side residue of 1/(s zeta(s))
at rho_k) and the residue of 1/xi at rho_k, r_k = 1/xi'(rho_k), where
xi(s) = (1/2) s (s-1) pi^(-s/2) Gamma(s/2) zeta(s).
Reports: #c_k>0, #c_k<0, sign changes in the sequence c_1..c_N, the arguments of r_k,
and whether the sign of Im r_k alternates at all consecutive pairs.
Written independently of results/zoo-s26/verify/*; mpmath only."""
import sys, time
import mpmath as mp
mp.mp.dps = 30
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
t0 = time.time()
cs, rs, azs = [], [], []
for k in range(1, N + 1):
    rho = mp.zetazero(k)
    assert abs(mp.re(rho) - mp.mpf(1)/2) < mp.mpf(10)**-25
    zp = mp.zeta(rho, derivative=1)
    c = mp.re(1 / (rho * zp))
    xip = mp.mpf(1)/2 * rho * (rho - 1) * mp.power(mp.pi, -rho/2) * mp.gamma(rho/2) * zp  # xi'(rho), since zeta(rho)=0
    r = 1 / xip
    cs.append(c); rs.append(r); azs.append(mp.arg(1/zp)/mp.pi)
    print(f"k={k:3d} t={mp.nstr(mp.im(rho),15):>18s} c={mp.nstr(c,8):>14s} "
          f"arg(res 1/xi)/pi={mp.nstr(mp.arg(r)/mp.pi,12):>14s} |Re r/|r||={mp.nstr(abs(mp.re(r))/abs(r),3)}")
pos = sum(1 for c in cs if c > 0); neg = sum(1 for c in cs if c < 0)
sc = sum(1 for a, b in zip(cs, cs[1:]) if (a > 0) != (b > 0))
maxdev = max(abs(abs(mp.arg(r)) - mp.pi/2) for r in rs)
alt = sum(1 for a, b in zip(rs, rs[1:]) if (mp.im(a) > 0) != (mp.im(b) > 0))
print(f"SUMMARY N={N}: c>0 at {pos}, c<0 at {neg}, sign changes {sc} in {N-1} steps; "
      f"max | |arg r| - pi/2 | = {mp.nstr(maxdev,3)}; Im r alternates at {alt} of {N-1} consecutive pairs; "
      f"arg(1/zeta'(rho))/pi in [{mp.nstr(min(azs),6)}, {mp.nstr(max(azs),6)}], Re(1/zeta'(rho))<0 at k={[i+1 for i,a in enumerate(azs) if abs(a)>0.5]}; "
      f"first sign of Im r_1: {'+' if mp.im(rs[0])>0 else '-'}; elapsed {time.time()-t0:.1f}s")
