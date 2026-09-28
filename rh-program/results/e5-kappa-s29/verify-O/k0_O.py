#!/usr/bin/env python3
"""k0_O.py -- Opus reader, E5: Theorem K0 recomputed with the reader's own code.
a(0) from the DEFINITION (mpmath quadrature of sech(pi r) A(r)), not from the closed form; gamma_1 from mpmath.zetazero;
m = 2 Psi_G(0)/|a(0)|, eps* = m/(1+m), kappa_K0 = 2 eps*; everything with eps directly (1 - eps is 1.0 in float64).
Pointwise check of 2 Psi_G - eps (2 Psi_G - a) >= 0 on [0, tau_0] on a grid at 40 digits (the analytic reason the min is at
tau = 0: Psi_{gamma_1} is increasing on [0, gamma_1] and |a| is decreasing on [0, tau_0] -- Lemma A3)."""
import mpmath as mp, json, time
mp.mp.dps = 40; t0 = time.time(); out = {}
def log(m): print(m, flush=True)
A = lambda r: (mp.re(mp.digamma(mp.mpf(1)/4 + 0.5j*r)) - mp.log(mp.pi))/(2*mp.pi)
a0_def = mp.quad(lambda r: mp.sech(mp.pi*r)*A(r), [-40 + k for k in range(81)])
g1 = mp.im(mp.zetazero(1))
log(f"gamma_1 = {mp.nstr(g1, 25)};  a(0) by definition = {mp.nstr(a0_def, 20)}")
Psi0 = mp.sech(mp.pi*g1)                      # Psi_G(0) = (1/2)[sech(pi(0-g1)) + sech(pi(0+g1))] = sech(pi g1)
m = 2*Psi0/abs(a0_def); eps = m/(1 + m); kap = 2*eps
log(f"Psi_G(0) = sech(pi gamma_1) = {mp.nstr(Psi0, 15)};  m = {mp.nstr(m, 15)};  eps* = {mp.nstr(eps, 15)};  kappa_K0 = 2 eps* = {mp.nstr(kap, 15)}")
log(f"4 sech(pi gamma_1)/|a(0)| = {mp.nstr(4*Psi0/abs(a0_def), 15)};  float64 trap: 1 - float(eps) == 1.0 -> {1 - float(eps) == 1.0}")
aC = lambda t: (mp.re((1 - 1j*t)*mp.digamma(0.5 + 0.5j*t) + 1j*t*mp.digamma(1 + 0.5j*t)) - 1 - mp.log(mp.pi))/(2*mp.pi)
zs = [g1] + [mp.im(mp.zetazero(k)) for k in range(2, 31)]
def Psi(t, G): return sum(mp.sech(mp.pi*(t - g)) + mp.sech(mp.pi*(t + g)) for g in G)/2
for name, G in (("G={g1}", [g1]), ("G=first 30", zs)):
    for fac, lab in ((1, "eps*"), (mp.mpf(10), "10 eps*"), (mp.mpf('0.5'), "eps*/2")):
        e = eps*fac; mn = None; arg = None
        for k in range(0, 1263):
            t = mp.mpf(k)*mp.mpf('0.005')
            v = 2*Psi(t, G) - e*(2*Psi(t, G) - aC(t))
            if mn is None or v < mn: mn, arg = v, t
        log(f"  {name:11s} {lab:8s}: min over [0, 6.31] (0.005 grid) of 2Psi - eps(2Psi - a) = {mp.nstr(mn, 6)} at tau = {mp.nstr(arg, 4)}")
        out[f"{name}_{lab}"] = float(mn)
# the ratio 2 Psi/|a| increasing on [0, tau_0): check at the grid
rat = [2*Psi(mp.mpf(k)*mp.mpf('0.01'), [g1])/abs(aC(mp.mpf(k)*mp.mpf('0.01'))) for k in range(0, 631)]
log(f"ratio 2Psi_g1/|a| increasing on [0, 6.30] (0.01 grid): {all(rat[i+1] > rat[i] for i in range(len(rat)-1))}")
out.update(gamma1=float(g1), a0=float(a0_def), m=float(m), eps_star=float(eps), kappa_K0=float(kap), seconds=time.time()-t0)
json.dump(out, open("k0_O_out.json", "w"), indent=1); log(f"done in {time.time()-t0:.1f}s")
