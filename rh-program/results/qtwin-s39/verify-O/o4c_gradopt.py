# Multi-start SLSQP on the epigraph (max tau s.t. Pi_F(x) >= tau, x in G<=X) with ANALYTIC gradients of Pi_F in (t, w).
# du/dm_a = (I+T)^{-1}(r_a - T_a u); params v = (t, w_1..w_k) enter the atom masses affinely.
import sys, time, numpy as np, scipy.sparse as sp
from scipy.sparse.linalg import spsolve_triangular
from scipy.optimize import minimize
from tprobe_core import TProbe
from o4b_optimize import design
class Grad:
    def __init__(self, P):
        self.P = P; k = len(P.low); nA = P.nA; sq = float(P.sq)
        K = np.zeros((nA, k + 1))
        for i, b in enumerate(P.low): K[i, 1 + i] = 1.0; K[k + i, 1 + i] = sq / float(b)
        if nA == 2 * k + 2: K[2 * k, 0] = 1.0
        self.K = K
    def val_grad(self, v):
        P = self.P; mA = P.masses(v[0], v[1:]); n = P.n
        T = (sp.csr_matrix((mA[P.aidx], (P.rows, P.cols)), shape=(n, n)) + sp.identity(n, format='csr'))
        rhs = np.zeros(n); ok = P.atpos >= 0
        rhs[P.atpos[ok]] += mA[ok] * P.logx[P.atpos[ok]]
        u = spsolve_triangular(T, rhs, lower=True)
        R = np.zeros((n, P.nA)); R[P.atpos[ok], np.nonzero(ok)[0]] = P.logx[P.atpos[ok]]
        Y = sp.csr_matrix((u[P.cols], (P.rows, P.aidx)), shape=(n, P.nA)).toarray()
        Z = spsolve_triangular(T, (R - Y) @ self.K, lower=True)
        return u / P.logx + P.pz, Z / P.logx[:, None]
def run(P, starts=20, seed=0, tmax=4.0, wmax=2.0, verbose=False):
    g = Grad(P); k = len(P.low); rng = np.random.default_rng(seed); best = (-np.inf, None)
    bounds = [(0, tmax)] + [(0, wmax)] * k + [(-10, 10)]
    for s in range(starts):
        v = np.concatenate([[rng.uniform(0, 2.5)], rng.uniform(0, 0.8, k)])
        Pi, _ = g.val_grad(v); z0 = np.append(v, Pi.min())
        cons = {'type': 'ineq', 'fun': lambda z: g.val_grad(z[:-1])[0] - z[-1],
                'jac': lambda z: np.hstack([g.val_grad(z[:-1])[1], -np.ones((P.n, 1))])}
        r = minimize(lambda z: -z[-1], z0, jac=lambda z: np.append(np.zeros(len(z) - 1), -1.0), method='SLSQP',
                     bounds=bounds, constraints=[cons], options={'maxiter': 300, 'ftol': 1e-12})
        val = g.val_grad(r.x[:-1])[0].min()
        if verbose: print("  start %d: %.6f" % (s, val), flush=True)
        if val > best[0]: best = (val, r.x[:-1].copy())
    Pi = g.val_grad(best[1])[0]
    return best[0], best[1], P.G[int(np.argmin(Pi))]
if __name__ == '__main__':
    q, X, starts = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); Ms = [int(a) for a in sys.argv[4:]]
    for M in Ms:
        t0 = time.time(); B = design(q, M); P = TProbe(q, B, X)
        if M == Ms[0]:   # gradient check by central differences
            g = Grad(P); v = np.concatenate([[1.1], np.linspace(0.2, 0.6, len(B))]); Pi, J = g.val_grad(v); h = 1e-6; err = 0
            for j in range(len(v)):
                e = np.zeros(len(v)); e[j] = h; err = max(err, np.abs((g.val_grad(v + e)[0] - g.val_grad(v - e)[0]) / (2 * h) - J[:, j]).max())
            print("gradient check (max abs error vs central differences): %.2e" % err, flush=True)
        val, v, xb = run(P, starts=starts)
        print("q=%d M=%d (%d lower atoms) |G<=%d|=%d : best max-min Pi_F = %.6f  t=%.5f  w=%s  binding x=%s  (%.0fs)" % (
            q, M, len(B), X, P.n, val, v[0], np.round(v[1:], 5).tolist(), xb, time.time() - t0), flush=True)
