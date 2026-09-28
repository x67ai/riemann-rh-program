#!/usr/bin/env python3
"""kappa_trivial_lb.py -- the orchestrator's re-derivation (Session 29): an explicit kappa > 0 from IV.18 rider (ii)'s
own identity.  Conventions = results/c2-m5/verify-next/budget_floor.py (PRICING-next-unit.md section 0):
  B(w) = 2 what(0) + int (what * mu_0) A = Z(w) + P(w),  Z(w) >= 2 int what Psi_G,  P(w) >= 0,
  a := mu_0 * A,  A(r) = (1/2pi)(Re psi(1/4 + i r/2) - log pi),  mu_0(xi) = 1/cosh(pi xi),
  Psi_G(tau) := sum_{gamma in G} [mu_0(tau - gamma) + mu_0(tau + gamma)]/2   (even; G = verified on-line ordinates; Z >= 2 int what Psi_G
  holds for every finite G because every zero's share is >= 0 on the cone).
For theta in [0,1]:  B = theta B + (1-theta) B >= 2(1-theta) what(0) + int what [2 theta Psi_G + (1-theta) a].
If  2 theta Psi_G(tau) + (1-theta) a(tau) >= 0 for all tau  then  B(w) >= 2(1-theta) what(0), i.e. kappa >= 2(1-theta).
The condition binds only where a < 0 (|tau| < tau_0 = 6.31); the best theta has (1-theta)/theta = min_{a<0} 2 Psi_G / |a|.
"""
import numpy as np, mpmath as mp, json, time
t0=time.time()
from scipy.special import digamma
# A and a on grids
r = np.linspace(-80, 80, 160001); dr = r[1]-r[0]
A = (np.real(digamma(0.25 + 0.5j*r)) - np.log(np.pi))/(2*np.pi)
mu0 = lambda x: 1/np.cosh(np.clip(np.pi*x,-700,700))
taus = np.linspace(0, 7.0, 701)
a = np.array([np.sum(mu0(t - r)*A)*dr for t in taus])
i0 = np.argmax(a > 0); tau0 = taus[i0-1] + (taus[i0]-taus[i0-1])*(-a[i0-1])/(a[i0]-a[i0-1])
print(f"a(0) = {a[0]:.6f}   (record: -0.653847);  zero crossing tau_0 = {tau0:.3f} (record 6.310)")
out={"a0":float(a[0]),"tau0":float(tau0)}
for nz in (1, 10, 100):
    G = [float(mp.zetazero(k).imag) for k in range(1, nz+1)]
    Psi = np.zeros_like(taus)
    for g in G: Psi += (mu0(taus-g)+mu0(taus+g))/2
    neg = a < 0
    ratio = 2*Psi[neg]/np.abs(a[neg])          # (1-theta)/theta must be <= min ratio
    rmin = ratio.min(); jmin = np.argmin(ratio)
    eps = rmin/(1+rmin)                          # 1 - theta
    kappa_lb = 2*eps
    # verify pointwise positivity on the whole grid with this theta
    # NOTE: theta = 1 - eps is 1.0 exactly in double precision for eps ~ 1e-19; work with eps directly (2(1-eps)Psi + eps a)
    chk = (2*(1-eps)*Psi + eps*a).min()
    print(f"G = first {nz:3d} zeros (gamma_1 = {G[0]:.4f}): min_{{a<0}} 2Psi/|a| = {rmin:.3e} at tau = {taus[neg][jmin]:.2f};  "
          f"theta = 1 - {eps:.3e};  min over grid of 2 theta Psi + (1-theta) a = {chk:.2e} (>= 0 required);  KAPPA >= {kappa_lb:.3e}")
    out[f"kappa_lb_G{nz}"] = float(kappa_lb)
# closed-form check at tau = 0 with G = {gamma_1}:  Psi(0) = sech(pi gamma_1);  kappa >= 4 sech(pi gamma_1)/|a(0)| (1 + O(sech))
g1 = float(mp.zetazero(1).imag); cf = 4/np.cosh(np.pi*g1)/abs(a[0])
print(f"closed form 4 sech(pi gamma_1)/|a(0)| = {cf:.3e}  (should match the G=1 line to leading order)")
# negative control (V.4): a 10x larger theta-deficit must FAIL the pointwise test
G=[g1]; Psi=(mu0(taus-g1)+mu0(taus+g1))/2; eps=out["kappa_lb_G1"]/2*10
print(f"negative control: eps x10 -> min 2(1-eps)Psi + eps a = {(2*(1-eps)*Psi+eps*a).min():.2e} (must be < 0)")
# second control: eps x0.5 must pass
eps2=out["kappa_lb_G1"]/2*0.5
print(f"positive control: eps x0.5 -> min 2(1-eps)Psi + eps a = {(2*(1-eps2)*Psi+eps2*a).min():.2e} (must be >= 0)")
out["closed_form_G1"]=float(cf); out["seconds"]=time.time()-t0
json.dump(out, open("results/e5-kappa-s29/verify-orch/kappa_trivial_lb_out.json","w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
