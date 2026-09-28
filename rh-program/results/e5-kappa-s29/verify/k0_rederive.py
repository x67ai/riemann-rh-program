#!/usr/bin/env python3
"""k0_rederive.py -- the E5 writer's OWN re-derivation of Theorem K0 (PREDERIVATION.md), independent of
verify-orch/kappa_trivial_lb.py: own closed form for a(tau) (conventions_check.py, Lemma A1), own zero ordinates
(mpmath.zetazero at 30 digits), all arithmetic in mpmath at 40 digits, the pointwise test done WITHOUT ever forming
1 - eps (the floating-point trap: 1 - 1e-19 == 1.0 in double precision).

  Theorem K0 (contract): for every w in the cone and every eps in [0,1],
     B(w) >= 2 eps what(0) + int what [ 2(1-eps) Psi_G + eps a ],   Psi_G(tau) = (1/2) sum_{g in G} [mu_0(tau-g) + mu_0(tau+g)].
  If  2(1-eps)Psi_G(tau) + eps a(tau) >= 0 for all tau, then kappa >= 2 eps.
  Equivalent pointwise form used here (no 1-eps):  2 Psi_G(tau) >= eps (2 Psi_G(tau) - a(tau))   for all tau,
  i.e.  eps <= 2 Psi_G / (2 Psi_G + |a|)  wherever a < 0  (automatic where a >= 0).  Hence
     eps* = min_{a<0} 2Psi_G/(2Psi_G + |a|) = m/(1+m),  m = min_{a<0} 2Psi_G/|a|,   kappa_lb = 2 eps*.
Controls (V.4): eps* x 10 must FAIL the pointwise test; eps* x 1/2 must pass; the ratio 2Psi/|a| must be increasing
on [0, tau_0] (so the minimum is at tau = 0 and the grid cannot miss it).
"""
import mpmath as mp, json, time
t0 = time.time(); mp.mp.dps = 40
LOGPI = mp.log(mp.pi)
def a_mp(t):
    t = mp.mpf(t); z = mp.mpc(0, t/2)
    return (mp.re((1 - mp.mpc(0, t))*mp.digamma(mp.mpf('0.5') + z) + mp.mpc(0, t)*mp.digamma(1 + z)) - 1 - LOGPI)/(2*mp.pi)
mu0 = lambda x: 1/mp.cosh(mp.pi*x)
out = {}
a0 = a_mp(0); tau0 = mp.findroot(a_mp, 6.31)
print(f"a(0) = {mp.nstr(a0, 12)}   tau_0 = {mp.nstr(tau0, 10)}")
out["a0"] = float(a0); out["tau0"] = float(tau0)
zeros = [mp.zetazero(k).imag for k in range(1, 31)]
print(f"gamma_1 = {mp.nstr(zeros[0], 20)}  (30 zeros loaded; gamma_30 = {mp.nstr(zeros[-1], 8)})")
out["gamma1"] = float(zeros[0])
def Psi(t, G):
    return sum((mu0(t - g) + mu0(t + g))/2 for g in G)
grid = [mp.mpf(i)/200 for i in range(0, int(7*200) + 1)]      # step 0.005 to tau = 7 > tau_0
for nz in (1, 10, 30):
    G = zeros[:nz]
    ratios = [(2*Psi(t, G)/(-a_mp(t)), t) for t in grid if a_mp(t) < 0]
    m, tmin = min(ratios)
    eps = m/(1 + m); kap = 2*eps
    # monotonicity of the ratio on {a<0}: consecutive differences all positive?
    inc = all(ratios[i+1][0] > ratios[i][0] for i in range(len(ratios) - 1))
    # pointwise test on the grid, in the trap-free form 2Psi - eps(2Psi - a) >= 0
    worst = min(2*Psi(t, G) - eps*(2*Psi(t, G) - a_mp(t)) for t in grid)
    print(f"G = first {nz:2d} zeros: m = min 2Psi/|a| = {mp.nstr(m, 8)} at tau = {mp.nstr(tmin, 4)}; ratio increasing on {{a<0}}: {inc}; "
          f"eps* = {mp.nstr(eps, 8)}; min over grid of 2Psi - eps(2Psi - a) = {mp.nstr(worst, 4)} (>= 0 required); KAPPA >= {mp.nstr(kap, 8)}")
    out[f"kappa_lb_G{nz}"] = float(kap); out[f"ratio_increasing_G{nz}"] = bool(inc)
G1 = zeros[:1]
m1 = 2*Psi(0, G1)/(-a0); eps1 = m1/(1 + m1)
cf = 4/mp.cosh(mp.pi*zeros[0])/(-a0)
print(f"closed form 4 sech(pi gamma_1)/|a(0)| = {mp.nstr(cf, 8)};  exact 2m/(1+m) with m = 2 sech(pi gamma_1)/|a(0)|: {mp.nstr(2*eps1, 12)}")
print(f"orchestrator's kappa_lb_G1 = 6.34642725583418e-19;  this script's = {mp.nstr(2*eps1, 15)}")
out["closed_form_G1"] = float(cf); out["kappa_lb_G1_exact"] = float(2*eps1)
# controls
for fac, must in ((10, "FAIL"), (mp.mpf(1)/2, "PASS")):
    e = eps1*fac
    worst = min(2*Psi(t, G1) - e*(2*Psi(t, G1) - a_mp(t)) for t in grid)
    print(f"control eps* x {mp.nstr(fac,3)}: min over grid = {mp.nstr(worst, 4)}  -> {'fails' if worst < 0 else 'passes'} (must {must})")
    out[f"control_x{float(fac)}"] = float(worst)
# floating-point trap, recorded
import numpy as np
e = float(2*eps1)/2
print(f"floating-point trap: eps = {e:.3e}; (1 - eps) == 1.0 in double: {(1.0 - e) == 1.0}; 2*(1-eps)*Psi(0) + eps*a(0) in double = {2*(1-e)*float(Psi(0,G1)) + e*float(a0):.3e} (spurious sign possible); trap-free form 2Psi(0) - eps(2Psi(0) - a(0)) = {2*float(Psi(0,G1)) - e*(2*float(Psi(0,G1)) - float(a0)):.3e}")
# sensitivity to gamma_1: d log kappa / d gamma = -pi tanh(pi gamma_1) ~ -pi
print(f"sensitivity: d ln(kappa_lb)/d gamma_1 = {mp.nstr(-mp.pi*mp.tanh(mp.pi*zeros[0]), 6)} per unit of gamma_1 (a 1e-6 error in gamma_1 moves kappa_lb by 3e-6 relative)")
out["seconds"] = time.time() - t0
json.dump(out, open("k0_rederive_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
