"""v4b (qtwin-s39): global (grid + polish) max-min of Pi_F on [1, X] for the smallest truncations of the class T (NOTE §7),
where v4's random-restart local search is not reliable (it is non-monotone in M, e.g. q = 9: M = 3 below M = 2).
q = 4, M = 2: params (t, w_{3/2}) on [0,4] x [0,2];  q = 9, M = 2: params (t, w_{3/2}, w_{5/2}) on [0,6] x [0,2] x [0,2].
"""
import numpy as np, itertools, sys
from scipy.optimize import minimize
from v4_thick_mixture_probe import build, pi_F, pi_zeta

def grid_maxmin(Q, M, X, ranges, n):
    B, atoms, E, fac = build(M, X, Q)
    PZ = np.array([pi_zeta(e) for e in E])
    f = lambda p: pi_F(np.maximum(p, 0.0), B, atoms, E, fac, PZ, Q)[1:]
    best = (-1e18, None)
    axes = [np.linspace(lo, hi, n) for lo, hi in ranges]
    for p in itertools.product(*axes):
        v = np.min(f(np.array(p)))
        if v > best[0]:
            best = (v, np.array(p))
    r = minimize(lambda p: -np.min(f(p)), best[1], method='Nelder-Mead', options={'maxiter': 4000, 'xatol': 1e-10, 'fatol': 1e-13})
    p = np.maximum(r.x, 0) if -r.fun > best[0] else best[1]
    v = f(p)
    return B, E, float(np.min(v)), p, E[int(np.argmin(v)) + 1], best[0]

if __name__ == "__main__":
    for Q, ranges, n, X in ((2, [(0, 4), (0, 2)], 201, 64), (3, [(0, 6), (0, 2), (0, 2)], 41, 81)):
        B, E, val, p, worst, gridval = grid_maxmin(Q, 2, X, ranges, n)
        print(f"q={Q*Q}, M=2, B = {[str(b) for b in B]}: grid ({n} pts/axis) max-min = {gridval:.6f}; polished max-min Pi_F on [1,{X}] = {val:.6f} "
              f"at params {[round(float(x), 5) for x in p]} (binding x = {worst})")
        sys.stdout.flush()
