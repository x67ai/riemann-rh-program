# DE (global) + analytic-gradient SLSQP polish for an arbitrary lower-atom design at q (square), window [1, X].
# usage: python3 o4e_driver.py q X design popsize maxiter    design in {M5, M6, P7, P11, P13, ...}
import sys, time, numpy as np
from fractions import Fraction as Fr
from scipy.optimize import differential_evolution, minimize
from tprobe_core import TProbe
from o4b_optimize import design
from o4c_gradopt import Grad
from sympy import primerange
def lower(q, name):
    sq = int(round(q ** 0.5))
    if name[0] == 'M': return design(q, int(name[1:]))
    if name[0] == 'P': return sorted(Fr(p + 1, p) for p in primerange(2, int(name[1:]) + 1) if Fr(p + 1, p) < sq)
    raise ValueError(name)
q, X, name, pop, it = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
B = lower(q, name); P = TProbe(q, B, X); g = Grad(P); k = len(B); t0 = time.time()
print("q=%d X=%d design=%s lower atoms=%s |G|=%d" % (q, X, name, [str(b) for b in B], P.n), flush=True)
bounds = [(0, 4.0)] + [(0, 2.0)] * k
with np.errstate(all='ignore'):
    r = differential_evolution(lambda v: -P.Pi(v[0], v[1:]).min(), bounds, seed=7, maxiter=it, popsize=pop, tol=1e-9, polish=False)
    print("  DE: %.6f (%.0fs)" % (-r.fun, time.time() - t0), flush=True)
    z0 = np.append(r.x, -r.fun)
    cons = {'type': 'ineq', 'fun': lambda z: g.val_grad(z[:-1])[0] - z[-1], 'jac': lambda z: np.hstack([g.val_grad(z[:-1])[1], -np.ones((P.n, 1))])}
    s = minimize(lambda z: -z[-1], z0, jac=lambda z: np.append(np.zeros(k + 1), -1.0), method='SLSQP', bounds=bounds + [(-10, 10)], constraints=[cons], options={'maxiter': 400, 'ftol': 1e-13})
    v = s.x[:-1] if g.val_grad(s.x[:-1])[0].min() > -r.fun else r.x
    Pi = g.val_grad(v)[0]
print("  polished max-min Pi_F on [1,%d] = %.6f  t=%.5f w=%s  binding x=%s  (%.0fs total)" % (X, Pi.min(), v[0], np.round(v[1:], 5).tolist(), P.G[int(np.argmin(Pi))], time.time() - t0), flush=True)
np.save("o4e_best_%d_%d_%s.npy" % (q, X, name), v)
