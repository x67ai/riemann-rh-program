# Global max-min of Pi_F on [1, X] over the weights, for the NOTE's q = 4 designs (lower atoms n/d in (1,2), d <= M).
# Differential evolution (global, derivative-free) on f(t, w) = min_x Pi_F(x), then SLSQP on the epigraph (max tau s.t. Pi_F >= tau).
import sys, time, numpy as np
from fractions import Fraction as Fr
from scipy.optimize import differential_evolution, minimize
from tprobe_core import TProbe
def design(q, M):
    sq = int(round(q ** 0.5))
    return sorted({Fr(n, d) for d in range(2, M + 1) for n in range(d + 1, sq * d) if 1 < Fr(n, d) < sq})
def solve(P, seeds=(1, 2, 3), tmax=4.0, wmax=2.0, maxiter=300):
    k = len(P.low); bounds = [(0, tmax)] + [(0, wmax)] * k
    f = lambda v: -P.Pi(v[0], v[1:]).min()
    best = None
    for sd in seeds:
        r = differential_evolution(f, bounds, seed=sd, maxiter=maxiter, popsize=25, tol=1e-10, polish=False)
        if best is None or r.fun < best.fun: best = r
    v0 = np.append(best.x, -best.fun)
    cons = {'type': 'ineq', 'fun': lambda z: P.Pi(z[0], z[1:-1]) - z[-1]}
    r2 = minimize(lambda z: -z[-1], v0, method='SLSQP', bounds=bounds + [(-10, 10)], constraints=[cons], options={'maxiter': 500, 'ftol': 1e-12})
    z = r2.x if (r2.success and P.Pi(r2.x[0], r2.x[1:-1]).min() > -best.fun - 1e-9) else v0
    Pi = P.Pi(z[0], z[1:-1]); i = int(np.argmin(Pi))
    return Pi.min(), z[:-1], P.G[i]
if __name__ == '__main__':
    q, X = int(sys.argv[1]), int(sys.argv[2]); Ms = [int(a) for a in sys.argv[3:]]
    for M in Ms:
        t0 = time.time(); B = design(q, M); P = TProbe(q, B, X)
        val, z, xb = solve(P)
        print("q=%d M=%d lower atoms=%s |G<=%d|=%d : max-min Pi_F = %.6f  at t=%.5f w=%s  binding x=%s  (%.0fs)" % (
            q, M, [str(b) for b in B], X, P.n, val, z[0], np.round(z[1:], 5).tolist(), xb, time.time() - t0), flush=True)
