#!/usr/bin/env python3
"""U4-sparse: Mertens-type law in the scaling limit. Cumulative sum_{p<=x} 1/p (from the per-bin field sinvp of s8sp) against
Ein(tau) = int_0^tau (1-e^{-v})/v dv (Theorem 4.4 / Lemma 4.3) and against the lattice sum sum_{x_a<=x} 1/x_a."""
import sys, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from ana import parse
from scipy.special import digamma
from scipy.integrate import quad
Ein = lambda t: quad(lambda v: (1-math.exp(-v))/v if v > 0 else 1.0, 0, t)[0]
for fn in sys.argv[1:]:
    rho, kv, rows = parse(fn); t = 1/rho; cum = 0.0
    print(f"# {fn} rho={rho:.6g}   x  tau  sum_{{p<=x}}1/p  Ein(tau)  diff  lattice_sum  Delta_rho")
    for r in rows:
        cum += r['sinvp']
        if r['b'] % 4 == 3:
            x = r['xhi']; tau = rho*math.log(x); A = math.floor((x-1)/t + 0.5)
            lat = rho*(digamma(A + 0.5 + rho) - digamma(0.5 + rho))
            D = rho*(math.log(1/rho) + digamma(0.5))
            print(f"  {x:.0e}  {tau:.4f}  {cum:.6f}  {Ein(tau):.6f}  {cum-Ein(tau):+.6f}  {lat:.6f}  {D:.6f}")
