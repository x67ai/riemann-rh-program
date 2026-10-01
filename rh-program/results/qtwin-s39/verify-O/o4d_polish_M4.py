# Polish the DE optimum for q=4, M=4 with analytic-gradient SLSQP; list active constraints; exact-rational re-evaluation of the min.
import numpy as np
from fractions import Fraction as Fr
from scipy.optimize import minimize
from tprobe_core import TProbe
from o4b_optimize import design
from o4c_gradopt import Grad
P = TProbe(4, design(4, 4), 64); g = Grad(P)
v0 = np.array([0.31847, 0.38637, 0.38637, 0.35508, 0.3018, 0.66502])
Pi0 = g.val_grad(v0)[0]; print("DE point: min Pi_F = %.6f" % Pi0.min())
z0 = np.append(v0, Pi0.min()); bounds = [(0, 4)] + [(0, 2)] * 5 + [(-10, 10)]
cons = {'type': 'ineq', 'fun': lambda z: g.val_grad(z[:-1])[0] - z[-1], 'jac': lambda z: np.hstack([g.val_grad(z[:-1])[1], -np.ones((P.n, 1))])}
r = minimize(lambda z: -z[-1], z0, jac=lambda z: np.append(np.zeros(6), -1.0), method='SLSQP', bounds=bounds, constraints=[cons], options={'maxiter': 500, 'ftol': 1e-14})
v = r.x[:-1]; Pi = g.val_grad(v)[0]; tau = Pi.min()
print("polished: max-min = %.6f at t=%.6f w=%s (SLSQP status %s)" % (tau, v[0], np.round(v[1:], 6).tolist(), r.message))
act = np.argsort(Pi)[:8]
print("8 smallest Pi_F (x, value):", [(str(P.G[i]), round(Pi[i], 6)) for i in act])
# exact-rational check: round weights to rationals, compute log*(m) by exact recursion over G (Fractions), report exact min
vr = [Fr(x).limit_denominator(10**6) for x in v]
mA = {}
for i, b in enumerate(P.low): mA[b] = vr[1 + i]; mA[Fr(4) / b] = 2 * vr[1 + i] / b
mA[Fr(2)] = vr[0]; mA[Fr(4)] = Fr(2)
# exact: L = log D via  x*l(x)... use the convolution-power series exactly (finite: atoms >= 5/4, X = 64 -> j <= 18)
E = dict(mA); powj = dict(E); logm = {x: c for x, c in E.items()}
for j in range(2, 19):
    new = {}
    for x, c in powj.items():
        for a, ca in E.items():
            y = x * a
            if y <= 64: new[y] = new.get(y, 0) + c * ca
    powj = new
    if not powj: break
    for x, c in powj.items(): logm[x] = logm.get(x, 0) + Fr((-1) ** (j + 1), j) * c
from tprobe_core import prime_power
def piz(x): return Fr(1, prime_power(x.numerator)) if (x.denominator == 1 and prime_power(x.numerator)) else Fr(0)
vals = {x: logm[x] + piz(x) for x in logm}
xm = min(vals, key=lambda x: vals[x])
print("EXACT (rational weights, power-series route, independent of the triangular solve): min Pi_F = %s = %.9f at x = %s; #points = %d" % ("<fraction>", float(vals[xm]), xm, len(vals)))
