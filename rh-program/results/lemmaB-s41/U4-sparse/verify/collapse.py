#!/usr/bin/env python3
"""U4-sparse: compare runs of different rho at common tau. For each target tau and run, the bin whose top has tau closest:
D(m) = Var/mean of counts in aligned windows of m steps, against the one-hit-per-component prediction
D_pred(m) = 1 - m*rho^2*psi1(1/2+rho)/lam (psi1 = trigamma); tail-rate ratio (measured / Poisson-queue kappa);
mean-queue ratio (measured / lam^2/(2(1-lam))). Usage: collapse.py tau1 tau2 ... -- files..."""
import sys, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import numpy as np
from ana import parse, kappa
from scipy.special import polygamma
i = sys.argv.index('--'); taus = [float(z) for z in sys.argv[1:i]]; files = sys.argv[i+1:]
runs = [(fn, *parse(fn)) for fn in files]
for T in taus:
    print(f"## tau = {T}")
    print("#  rho      tau_bin  nsteps     lam    D(1) pred   D(4) pred   D(16) pred  tailratio  meanEratio  phi-f0")
    for fn, rho, kv, rows in runs:
        cand = [r for r in rows if r['nsteps'] >= 2000]
        if not cand: continue
        r = min(cand, key=lambda r: abs(rho*math.log(r['xhi']) - T))
        tb = rho*math.log(r['xhi'])
        if abs(tb - T) > 0.03: continue
        n = r['nsteps']; lam = r['ncomp']/n; c = rho**2*float(polygamma(1, 0.5+rho))/lam
        D = []
        for j in (0, 2, 4):
            nw, w1, w2 = r['win'][j]; mu = w1/nw; D.append((w2/nw - mu*mu)/mu)
        he = r['he'][:-1].astype(float); tail = (np.cumsum(he[::-1])[::-1] + r['he'][-1])/n
        hs = [h for h in range(1, 47) if tail[h]*n >= 30 and tail[h] < 0.2]
        tr = (-np.polyfit(hs, np.log(tail[hs]), 1)[0]/kappa(lam)) if len(hs) >= 3 else float('nan')
        me = (r['se']/n)/(lam**2/(2*(1-lam)))
        f0 = (1-math.exp(-tb))/tb
        print(f"  {rho:.5f}  {tb:.4f} {n:>10d}  {lam:.4f}  {D[0]:.3f} {1-c:.3f}  {D[1]:.3f} {1-4*c:.3f}  {D[2]:.3f} {1-16*c:.3f}"
              f"   {tr:.3f}      {me:.3f}      {r['nidle']/n - f0:+.4f}")
