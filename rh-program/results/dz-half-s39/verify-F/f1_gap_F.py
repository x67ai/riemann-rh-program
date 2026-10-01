# Orchestrator (Session 40): re-derivation of read-O's F1 before applying it.  One-scale variance at x = 22 on DZ's grid,
# template f_R(v) = (1 - 1/v)/log v:  grid sum  S = sum_k p_k (1 - p_k) c(v_k)^2  over the cells (v_k - 2^-n, v_k] in (11, 22],
# continuum  I = int_11^22 f_R(v) c(v)^2 dv  (split at the jump v = 2x/3 of n0),  c(v) = n0(x/v) - kappa*x*(-log(1 - 1/v)),
# n0(y) = 1 + [1.5 in P]*[y >= 1.5]  (N0 = 1 means the g-prime 1.5 is present).  Relative gap (S - I)/I.
import numpy as np, mpmath as mp
from scipy.special import expi
x = 22.0
def n0(y, N0): return 1.0 + (N0 * (y >= 1.5))
def c(v, kappa, N0): return n0(x / v, N0) - kappa * x * (-np.log1p(-1.0 / v))
G = lambda v: expi(np.log(v)) - np.log(np.log(v))          # antiderivative of (1 - 1/v)/log v
for kappa, N0 in [(1.0, 1), (0.7, 0), (0.7, 1), (1.0, 0)]:
    S = 0.0
    for n in range(11, 22):
        v = n + np.arange(1, 2**n + 1) / 2.0**n
        p = G(v) - G(v - 2.0**-n)
        S += float(np.sum(p * (1 - p) * c(v, kappa, N0)**2))
    mp.mp.dps = 30
    f = lambda v: (1 - 1/v) / mp.log(v) * ((1 + (N0 if x / v >= 1.5 else 0)) - kappa * x * (-mp.log(1 - 1/v)))**2
    I = mp.quad(f, [11, mp.mpf(2) * 22 / 3, 22])
    Iu = mp.quad(lambda v: f(v), mp.linspace(11, 22, 9))   # split points not at the jump: shows the artifact size
    print(f"kappa = {kappa}, N0 = {N0}: grid S = {S:.10f}  continuum I = {mp.nstr(I, 12)}  relative gap = {(S - float(I))/float(I):+.3e}   (unsplit-rule continuum {mp.nstr(Iu, 12)})")
