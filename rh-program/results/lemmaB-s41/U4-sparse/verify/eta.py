#!/usr/bin/env python3
"""U4-sparse: limit-model constants. lambda0(tau) = 1 - (1-e^-tau)/tau; kappa0 = positive root of lambda0 (e^k - 1) = k;
eta(tau) = tau/kappa0(tau) (predicted limit of rho * max queue up to x = e^{tau/rho}); M/D/1 mean lambda0^2/(2(1-lambda0))."""
import math, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from ana import kappa
lam0 = lambda t: 1 - (1 - math.exp(-t))/t
print("# tau  lambda0  kappa0  eta=tau/kappa0  MD1mean  | large-tau check: eta ~ tau^2/2")
for t in (0.1, 0.2, 0.31, 0.5, 0.61, 1.0, 1.19, 1.5, 2.0, 2.2, 3.0, 5.0, 10.0):
    l = lam0(t); k = kappa(l)
    print(f"{t:5.2f}  {l:.5f}  {k:.5f}  {t/k:.5f}  {l*l/(2*(1-l)):.5f}  | {t*t/2:.3f}")
