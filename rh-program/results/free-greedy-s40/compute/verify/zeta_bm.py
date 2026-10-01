# zeta_bm.py -- F_X(s) = sum_{n<=X} n^-s + rho X^{1-s}/(s-1) - E(X) X^-s from the generator's block moments.
#   zeta_P(s) = F_X(s) + s * int_X^oo E(u) u^{-s-1} du   (E = N - T, T(x) = rho (x - 1) + 1).
# Block b: centre c_b = (b + 1/2) w, moments M[b, j] = sum_{n in b} (log n - c_b)^j, j = 0..6, so that
#   sum_{n in b} n^-s = e^{-s c_b} sum_j (-s)^j / j! M[b, j]   (truncation (|s| w / 2)^7 / 7!).
# CLI: python3 zeta_bm.py validate MOMFILE GINTFILE   (direct sum over the dumped g-integers at a few points)
import sys, math, warnings, numpy as np
warnings.filterwarnings("ignore")
from math import factorial

def load(path):
    h = np.fromfile(path, dtype=np.float64, count=8)
    w, nb, X, N, EX, rh, rl, nm = h
    nb, nm = int(nb), int(nm)
    M = np.fromfile(path, dtype=np.float64, offset=64, count=nb * nm).reshape(nb, nm)
    return dict(w=w, nb=nb, X=X, N=int(N), EX=EX, rho=rh + rl, M=M, c=(np.arange(nb) + 0.5) * w, logX=math.log(X))

def _corr(s, D):
    X, lX, rho, EX = D["X"], D["logX"], D["rho"], D["EX"]
    Xs = np.exp(-s * lX)
    return rho * X * Xs / (s - 1) - EX * Xs, Xs

def F(s, D, deriv=False):
    """F_X(s) (and F_X'(s)) by block moments, vectorized over blocks."""
    s = complex(s); M, c = D["M"], D["c"]
    nm = M.shape[1]
    e = np.exp(-s * c)
    co = [(-s) ** j / factorial(j) for j in range(nm)]
    P = M @ np.array(co)
    corr, Xs = _corr(s, D)
    val = complex((e * P).sum()) + corr
    if not deriv: return val
    Q = M[:, 1:] @ np.array(co[:nm - 1])     # sum_n delta e^{-s delta}
    X, lX, rho, EX = D["X"], D["logX"], D["rho"], D["EX"]
    dval = -complex((e * (c * P + Q)).sum()) - rho * X * Xs * (lX / (s - 1) + 1 / (s - 1) ** 2) + EX * Xs * lX
    return val, dval

def F_grid(sigma, D, tmax=200.0, L=2 ** 21):
    """F_X(sigma + i t_m), t_m = m * 2 pi / (L w), 0 <= t_m <= tmax, via 7 FFTs."""
    M, c, w = D["M"], D["c"], D["w"]
    nb, nm = M.shape
    assert nb <= L
    dt = 2 * math.pi / (L * w)
    mmax = int(tmax / dt) + 2
    t = np.arange(mmax) * dt
    damp = np.exp(-sigma * c)
    acc = np.zeros(mmax, dtype=complex)
    s = sigma + 1j * t
    ph = np.exp(-1j * t * w / 2)
    for j in range(nm):
        a = np.zeros(L); a[:nb] = M[:, j] * damp
        G = np.fft.fft(a)[:mmax] * ph            # sum_b a_b e^{-i t c_b}
        acc += (-s) ** j / factorial(j) * G
    corr, _ = _corr(s, D)
    return t, acc + corr

def direct(s, logn, D):
    s = complex(s)
    corr, _ = _corr(s, D)
    return complex(np.exp(-s * logn).sum()) + corr

if __name__ == "__main__" and sys.argv[1] == "validate":
    D = load(sys.argv[2])
    g = np.fromfile(sys.argv[3], dtype=np.float64).reshape(-1, 2)
    g = g[g[:, 0] <= D["X"]]
    logn = np.log(g[:, 0]) + g[:, 1] / g[:, 0]
    print(f"# validate {sys.argv[2]}: X = {D['X']:.6e}, N = {D['N']} (dumped g-integers <= X: {len(logn)}), E(X) = {D['EX']:.6f}")
    print("#  s                      F_X block-moment                         F_X direct sum                          |diff|")
    for s in [2.0, 0.6 + 10j, 0.75 + 50j, 0.9 + 150j, 0.55 + 199j, 0.51 + 3.3j, 1.0 + 100j]:
        a, b = F(s, D), direct(s, logn, D)
        print(f"  {s!s:22s} {a.real:+.15e}{a.imag:+.15e}i  {b.real:+.15e}{b.imag:+.15e}i  {abs(a - b):.2e}")
    for sg in [0.6, 0.9]:
        t, Fg = F_grid(sg, D, tmax=200.0)
        idx = [1, len(t) // 3, len(t) - 3]
        print(f"#  FFT grid vs block-moment direct, sigma = {sg}: " + "  ".join(f"t={t[i]:.4f} |diff|={abs(Fg[i] - F(sg + 1j * t[i], D)):.2e}" for i in idx))
