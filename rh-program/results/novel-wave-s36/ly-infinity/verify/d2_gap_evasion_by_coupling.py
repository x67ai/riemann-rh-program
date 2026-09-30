"""d2_gap_evasion_by_coupling.py -- where exactly does the gap no-go stop?

Theorem 1' (NOTE sec.2): for a Lee-Yang polynomial p of multidegree d evaluated along inner
channels v_j (|v_j| < 1 on sigma > 1/2, unimodular on the line), the zero count on an interval I
satisfies |N - (1/2pi) sum_j d_j |Delta_I arg v_j|| < |d|.  For det(I - V U) (d = (1,...,1)),
the loss |d| = number of channels.  With ONE prime channel 2^{-it} alone, (-14.1, 14.1) must
contain >= 3 zeros.  Question: coupled to k slowly winding archimedean channels
b_a(s) = (s - a)/(s - (1 - a)), a real > 1/2 far to the right (Gamma-type Blaschke factors), can a
unitary U remove ALL zeros from (-14.1, 14.1)?  (Xi has none there.)
We maximize min_t |det(I - V(t) U)| over the window (softmin objective), count zeros of the real
form of det on the line, and report the smallest k that succeeds.
"""
import numpy as np, time, json
from scipy.linalg import expm
from scipy.optimize import minimize

rng = np.random.default_rng(11)
T = 14.1
ts = np.linspace(-T, T, 1601)          # fine grid for zero counting
tsc = np.linspace(-T, T, 241)          # coarse grid for the optimizer


def channels(t, avals):
    s = 0.5 + 1j * t
    cols = [np.exp(-1j * t * np.log(2.0))]
    for a in avals:
        cols.append((s - a) / (s - (1 - a)))
    return np.array(cols).T          # (len(t), k+1), all unimodular on the line


def herm(x, n):
    H = np.zeros((n, n), complex)
    iu = np.triu_indices(n, 1)
    H[np.diag_indices(n)] = x[:n]
    m = len(iu[0])
    H[iu] = x[n:n + m] + 1j * x[n + m:n + 2 * m]
    return H + np.triu(H, 1).conj().T


def detF(U, V):
    n = U.shape[0]
    M = np.eye(n)[None] - V[:, :, None] * U[None]
    return np.linalg.det(M)


def obj(x, n, V):
    U = expm(1j * herm(x, n))
    a = np.abs(detF(U, V))
    beta = 40.0
    return -(-np.log(np.mean(np.exp(-beta * a))) / beta)   # maximize soft-min |F|


def real_form_zero_count(U, V, t):
    F = detF(U, V)
    ph = np.unwrap(np.angle(np.prod(V, axis=1))) + np.angle(np.linalg.det(-U))
    R = np.real(F * np.exp(-0.5j * ph))
    return int(np.sum(R[:-1] * R[1:] < 0)), float(np.max(np.abs(np.imag(F * np.exp(-0.5j * ph)))) / (np.max(np.abs(R)) + 1e-300))


def main():
    out = []
    print('window (-14.1, 14.1); prime channel 2^{-it} winds', round(2 * T * np.log(2), 4), 'rad')
    V1 = channels(ts, [])
    # baseline: prime channel alone, U = e^{i phi} scalar: zeros = solutions of 2^{-it} e^{i phi} = 1
    best1 = min(real_form_zero_count(np.array([[np.exp(1j * ph)]]), V1, ts)[0] for ph in np.linspace(0, 2 * np.pi, 73))
    print('k = 0 (prime channel alone): minimal number of zeros over all U in U(1):', best1)
    out.append(dict(k=0, min_zeros=best1))
    for k in range(1, 6):
        avals = list(0.5 + np.array([12.0, 25.0, 50.0, 100.0, 200.0, 400.0][:k]))
        V = channels(ts, avals); Vc = channels(tsc, avals)
        wind = [4 * np.arctan(T / (a - 0.5)) for a in avals]
        n = k + 1
        best = None
        t0 = time.time()
        for r in range(6):
            x0 = rng.standard_normal(n * n) * 1.2
            o = minimize(obj, x0, args=(n, Vc), method='L-BFGS-B', options=dict(maxiter=120))
            U = expm(1j * herm(o.x, n))
            nz, imres = real_form_zero_count(U, V, ts)
            mn = float(np.min(np.abs(detF(U, V))))
            if best is None or (nz, -mn) < (best[0], -best[1]):
                best = (nz, mn, U, imres)
        lower = (2 * T * np.log(2) + sum(wind)) / (2 * np.pi) - n
        print(f'k = {k} archimedean channels a-1/2 = {[a - 0.5 for a in avals]} (windings {np.round(wind, 3).tolist()} rad): '
              f'best U has {best[0]} zeros in the window, min|det| = {best[1]:.3e} '
              f'(Theorem 1\' lower bound: N > {lower:.3f}); real-form residual {best[3]:.1e}  [{time.time() - t0:.1f}s]', flush=True)
        out.append(dict(k=k, a_minus_half=[a - 0.5 for a in avals], min_zeros=best[0], min_abs_det=best[1],
                        lower_bound=lower, U_abs=np.round(np.abs(best[2]), 3).tolist()))
    with open('d2_gap_evasion_by_coupling.json', 'w') as fh:
        json.dump(out, fh, indent=1)


if __name__ == '__main__':
    t0 = time.time()
    main()
    print(f'elapsed {time.time() - t0:.1f} s')
