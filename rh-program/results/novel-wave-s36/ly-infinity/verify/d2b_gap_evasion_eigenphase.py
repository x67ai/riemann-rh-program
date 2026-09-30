"""d2b_gap_evasion_eigenphase.py -- second attempt at the coupling question of d2, with a direct
objective: push every eigenphase of V(t)U away from 0 (mod 2 pi) at every t of a fine grid.
J(U) = mean_t sum_k exp(-|1 - e^{i theta_k(t)}|^2 / w),  w = 0.05 (a zero of det(I - VU) <=> some
theta_k = 0).  Zero count: sign changes of the real form of det on a 3201-point grid.
Physics of the question (NOTE sec.4): eigenphases move monotonically and (generically) keep their
cyclic order, so no crossing in the window <=> the prime channel's 19.55 rad of winding is shared by
>= 4 eigenphases, none of which reaches 0.  Theorem 1' allows this once k >= 4 slow channels exist."""
import numpy as np, time, json
from scipy.linalg import expm
from scipy.optimize import minimize
rng = np.random.default_rng(2026)
T = 14.1
tf = np.linspace(-T, T, 3201); tc = np.linspace(-T, T, 281)
def channels(t, avals):
    s = 0.5 + 1j*t
    return np.array([np.exp(-1j*t*np.log(2.0))] + [(s - a)/(s - (1 - a)) for a in avals]).T
def herm(x, n):
    H = np.zeros((n, n), complex); iu = np.triu_indices(n, 1); m = len(iu[0])
    H[np.diag_indices(n)] = x[:n]; H[iu] = x[n:n+m] + 1j*x[n+m:n+2*m]
    return H + np.triu(H, 1).conj().T
def J(x, n, V, w=0.05):
    U = expm(1j*herm(x, n))
    ev = np.linalg.eigvals(V[:, :, None]*U[None])
    return float(np.mean(np.sum(np.exp(-np.abs(1 - ev)**2/w), axis=1)))
def count(U, V):
    F = np.linalg.det(np.eye(U.shape[0])[None] - V[:, :, None]*U[None])
    ph = np.unwrap(np.angle(np.prod(V, axis=1))) + np.angle(np.linalg.det(-U))
    R = np.real(F*np.exp(-0.5j*ph)); return int(np.sum(R[:-1]*R[1:] < 0))
out = []
for k in (3, 4, 5, 6):
    avals = list(0.5 + np.array([12.0, 25.0, 50.0, 100.0, 200.0, 400.0][:k]))
    Vc, Vf = channels(tc, avals), channels(tf, avals); n = k + 1
    best = None; t0 = time.time()
    for r in range(8):
        o = minimize(J, rng.standard_normal(n*n)*1.5, args=(n, Vc), method='L-BFGS-B', options=dict(maxiter=200))
        U = expm(1j*herm(o.x, n)); c = count(U, Vf)
        if best is None or c < best[0]: best = (c, o.fun, U)
        if c == 0: break
    ev0 = np.sort(np.mod(np.angle(np.linalg.eigvals(Vf[0][:, None]*best[2])), 2*np.pi))
    print(f'k = {k}: fewest zeros found in (-14.1, 14.1) = {best[0]}  (J = {best[1]:.3e}; eigenphases at t=-14.1: {np.round(ev0, 3).tolist()})  [{time.time()-t0:.1f}s]', flush=True)
    out.append(dict(k=k, fewest_zeros=best[0], J=best[1], U_abs=np.round(np.abs(best[2]), 3).tolist()))
json.dump(out, open('d2b_gap_evasion_eigenphase.json', 'w'), indent=1)
