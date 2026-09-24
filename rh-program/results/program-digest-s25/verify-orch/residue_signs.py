# Orchestrator re-derivation (standing order 5), Session 25, 2026-09-25: signs of the on-line Mobius residues 1/(rho zeta'(rho)).
from mpmath import mp, zetazero, zeta, arg, pi
mp.dps=30
for n in range(1,17):
    r=zetazero(n); d=zeta(r,derivative=1); w=1/(r*d)
    print(f"n={n:2d} gamma={float(r.imag):12.6f}  Re w={float(w.real):+.5f}  Im w={float(w.imag):+.5f}  arg(1/zeta')={float(arg(1/d)/pi):+.3f}pi")
