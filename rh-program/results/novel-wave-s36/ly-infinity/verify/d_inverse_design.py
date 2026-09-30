"""d_inverse_design.py -- task (d): inverse design of a unitary coupling U between primes.

F_U(t) = det(I - Z(t) U),  Z(t) = diag(p_j^{-it})  (slots p_j, repetition allowed),  U in U(n).
Lee-Yang for every U; zero density W/2pi with W = sum log p_j.  We place the window at the
height T* where 2 theta'(T*) = W (densities match) and fit U so that F_U vanishes at zeta's zeros
in a TRAINING half-window; we then measure the predicted zeros against zeta's zeros in the
held-out TEST half-window.

Objective:  J(U) = mean_j min_k |1 - exp(i theta_k(gamma_j))|^2 over training zeros gamma_j,
theta_k(t) = eigenphases of Z(t)U  (F_U(gamma) = 0 iff some eigenvalue of Z(gamma)U equals 1).
Parametrization U = expm(i H), H Hermitian: n^2 real parameters; gauge U -> D U D^{-1}
(D diagonal unitary) leaves F_U invariant, so the effective count is n^2 - (n-1).

Honest comparison on the TEST half (mean |gamma - nearest model zero| / mean spacing):
  fitted U  |  best of 200 Haar-random U (selected on TRAIN)  |  Gram (prime-free)  |
  LY-aligned product A = prod(1 + p^{-1/2 - it}) with linearized phase (no free parameters).
Also: structure of the fitted U (moduli, eigenphases, closeness to diagonal/permutation).
"""
import numpy as np, mpmath as mp, time, json, sys
from scipy.linalg import expm
from scipy.optimize import minimize

rng = np.random.default_rng(7)
mp.mp.dps = 20


def theta_np(t):
    t = np.asarray(t, float)
    return (t / 2) * np.log(t / (2 * np.pi)) - t / 2 - np.pi / 8 + 1 / (48 * t) + 7 / (5760 * t ** 3)


def thetap(t):
    return 0.5 * np.log(t / (2 * np.pi)) - 1 / (48 * t ** 2)


def solve_Tstar(W):
    T = 2 * np.pi * np.exp(W)
    for _ in range(60):
        T = T - (2 * thetap(T) - W) * T
    return T


def zeta_zeros(a, b, h):
    ts = np.arange(a, b + h, h)
    v = np.array([float(mp.siegelz(x)) for x in ts])
    z = []
    for i in range(len(ts) - 1):
        if v[i] * v[i + 1] < 0:
            z.append(float(mp.findroot(mp.siegelz, (mp.mpf(ts[i]), mp.mpf(ts[i + 1])), solver='anderson')))
    return np.array(z)


def herm(x, n):
    H = np.zeros((n, n), complex)
    iu = np.triu_indices(n, 1)
    H[np.diag_indices(n)] = x[:n]
    m = len(iu[0])
    H[iu] = x[n:n + m] + 1j * x[n + m:n + 2 * m]
    H = H + np.triu(H, 1).conj().T
    return H


def eigphases(U, ell, t):
    out = []
    for tt in np.atleast_1d(t):
        Z = np.exp(-1j * ell * tt)
        w = np.linalg.eigvals(Z[:, None] * U)
        out.append(np.angle(w))
    return np.array(out)


def J(x, n, ell, gam):
    U = expm(1j * herm(x, n))
    ph = eigphases(U, ell, gam)
    return np.mean(np.min(np.abs(1 - np.exp(1j * ph)) ** 2, axis=1))


def model_zeros_det(U, ell, W, lo, hi):
    dm = np.linalg.det(-U); w = np.sqrt(np.conj(dm))
    h = 2 * np.pi / W / 60
    ts = np.arange(lo, hi + h, h)
    Z = np.exp(-1j * np.outer(ts, ell))
    M = np.eye(len(ell))[None] - Z[:, :, None] * U[None]
    R = np.real(w * np.exp(1j * W * ts / 2) * np.linalg.det(M))
    idx = np.nonzero(R[:-1] * R[1:] < 0)[0]
    # linear interpolation is enough at h = spacing/60 for scoring
    return ts[idx] - R[idx] * (ts[idx + 1] - ts[idx]) / (R[idx + 1] - R[idx])


def model_zeros_fun(f, lo, hi, h):
    ts = np.arange(lo, hi + h, h)
    v = f(ts)
    idx = np.nonzero(v[:-1] * v[1:] < 0)[0]
    return ts[idx] - v[idx] * (ts[idx + 1] - ts[idx]) / (v[idx + 1] - v[idx])


def score(zeta, mz, delta):
    if len(mz) == 0:
        return np.nan
    return float(np.mean([np.min(np.abs(mz - g)) for g in zeta]) / delta)


def run(slots, restarts=12, maxiter=400, Hwin=None):
    ell = np.log(np.array(slots, float)); n = len(slots); W = ell.sum()
    Tst = solve_Tstar(W)
    delta = 2 * np.pi / np.log(Tst / (2 * np.pi))
    H = Hwin or min(np.sqrt(0.4 * Tst), 40.0)
    zz = zeta_zeros(Tst - H - 1, Tst + H + 1, delta / 20)
    zz = zz[(zz > Tst - H) & (zz < Tst + H)]
    train = zz[zz < Tst]; test = zz[zz >= Tst]
    npar = n * n; neff = n * n - (n - 1)
    res = dict(slots=slots, n=n, W=W, Tstar=Tst, H=H, delta=delta, n_train=len(train), n_test=len(test),
               n_params=npar, n_params_effective=neff)
    # fitted U
    best = None
    t0 = time.time()
    for r in range(restarts):
        x0 = rng.standard_normal(npar) * 1.5
        o = minimize(J, x0, args=(n, ell, train), method='L-BFGS-B', options=dict(maxiter=maxiter))
        if best is None or o.fun < best.fun:
            best = o
    U = expm(1j * herm(best.x, n))
    lo, hi = Tst - H - 1, Tst + H + 1
    mzU = model_zeros_det(U, ell, W, lo, hi)
    res['fit_J_train'] = float(best.fun)
    res['fitted_train'] = score(train, mzU, delta)
    res['fitted_test'] = score(test, mzU, delta)
    res['fit_time_s'] = round(time.time() - t0, 1)
    # random U, selected on train
    bestR = None
    for r in range(200):
        z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2)
        q, rr = np.linalg.qr(z); q = q * (np.diag(rr) / abs(np.diag(rr)))
        s_tr = score(train, model_zeros_det(q, ell, W, lo, hi), delta)
        if bestR is None or s_tr < bestR[0]:
            bestR = (s_tr, q)
    mzR = model_zeros_det(bestR[1], ell, W, lo, hi)
    res['random_best_train'] = bestR[0]
    res['random_best_test'] = score(test, mzR, delta)
    # Gram and LY-aligned (no free parameters)
    gram = model_zeros_fun(lambda t: np.cos(theta_np(t)), lo, hi, delta / 60)
    res['gram_train'] = score(train, gram, delta); res['gram_test'] = score(test, gram, delta)

    def ly_aligned(t):
        A = np.ones(np.shape(t), complex)
        for p in slots:
            A *= 1 + p ** -0.5 * np.exp(-1j * t * np.log(p))
        return np.real(np.exp(1j * (theta_np(Tst) + (t - Tst) * W / 2)) * A)
    al = model_zeros_fun(ly_aligned, lo, hi, delta / 60)
    res['LYaligned_train'] = score(train, al, delta); res['LYaligned_test'] = score(test, al, delta)
    # structure of U
    ev = np.angle(np.linalg.eigvals(U))
    res['U_abs'] = np.round(np.abs(U), 3).tolist()
    res['U_eigphases_sorted'] = np.round(np.sort(ev), 4).tolist()
    res['U_diag_abs'] = np.round(np.abs(np.diag(U)), 4).tolist()
    res['p^-1/2'] = np.round(np.array(slots, float) ** -0.5, 4).tolist()
    return res


if __name__ == '__main__':
    out = []
    for slots in ([2, 3, 5, 7], [2, 3, 5, 7, 11], [2, 2, 3, 5, 7], [2, 3, 5, 7, 11, 13]):
        t0 = time.time()
        r = run(slots)
        out.append(r)
        print(f"\n=== slots={slots} n={r['n']} W={r['W']:.4f} T*={r['Tstar']:.2f} +-{r['H']:.1f} "
              f"train/test zeros = {r['n_train']}/{r['n_test']}  params {r['n_params']} (effective {r['n_params_effective']})")
        print(f"  fitted U      : J_train={r['fit_J_train']:.3e}  train {r['fitted_train']:.4f}  TEST {r['fitted_test']:.4f}")
        print(f"  best random U : train {r['random_best_train']:.4f}  TEST {r['random_best_test']:.4f}")
        print(f"  Gram (no primes): train {r['gram_train']:.4f}  TEST {r['gram_test']:.4f}")
        print(f"  LY-aligned product (no fit): train {r['LYaligned_train']:.4f}  TEST {r['LYaligned_test']:.4f}")
        print(f"  |U| = {r['U_abs']}")
        print(f"  eigphases(U) = {r['U_eigphases_sorted']}  |diag U| = {r['U_diag_abs']}  p^-1/2 = {r['p^-1/2']}")
        print(f"  [{time.time() - t0:.1f} s]"); sys.stdout.flush()
    with open('d_inverse_design.json', 'w') as fh:
        json.dump(out, fh, indent=1)
