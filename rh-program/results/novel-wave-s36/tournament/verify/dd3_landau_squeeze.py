"""DD3 (row T22): the exact squeeze for zeta.  D_1^X(sigma) = int_1^X (psi_F(x) - x)^2 x^{-sigma-1} dx,
whose abscissa of convergence is 2*Theta (Theta = sup Re rho) by Landau (nonnegative integrand).
Local growth exponent g(sigma) = log10(D(10X)/D(X)) ~ max(0, 2Theta - sigma).
Worlds: zeta (Theta = 1/2 expected), F_{2.9,2} (Theta = 0.82388), DH (Theta = 0.80852, off-line zero at height 85.7).
psi_F = sum_{n<=x} Lambda_F(n); midpoint rule per unit interval with the exact +1/12 variance term."""
import math, sys, time
import numpy as np

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**7
SIG = [0.9, 1.0, 1.1, 1.3, 1.5, 1.6, 1.7, 1.9]
CHECK = [10**k for k in range(4, int(round(math.log10(X))) + 1)]


def lambda_zeta(N):
    lam = np.zeros(N + 1)
    s = np.ones(N + 1, dtype=bool); s[:2] = False
    for p in range(2, math.isqrt(N) + 1):
        if s[p]:
            s[p * p::p] = False
    P = np.nonzero(s)[0]
    lam[P] = np.log(P)
    for p in P[P <= math.isqrt(N)]:
        q = int(p) * int(p)
        while q <= N:
            lam[q] = math.log(p); q *= int(p)
    return lam


def lambda_dh(N):
    s5 = math.sqrt(5.0); kap = (math.sqrt(10 - 2 * s5) - 2) / (s5 - 1)
    per = np.array([0.0, 1.0, kap, -kap, -1.0])
    a = per[np.arange(N + 1) % 5]; a[0] = 0.0
    lam = np.zeros(N + 1); acc = np.zeros(N + 1)
    logn = np.zeros(N + 1); logn[1:] = np.log(np.arange(1, N + 1, dtype=float))
    for n in range(2, N + 1):
        v = a[n] * logn[n] - acc[n]
        lam[n] = v
        if v != 0.0 and 2 * n <= N:
            k = N // n
            acc[2 * n::n][:k - 1] += v * a[2:k + 1]
    return lam


def squeeze(name, lam, main_term):
    N = len(lam) - 1
    psi = np.cumsum(lam)
    n = np.arange(1, N, dtype=float)
    E = psi[1:N] - main_term * (n + 0.5)
    base = E * E + 1.0 / 12.0
    print(f"== {name}", flush=True)
    rows = {}
    for sg in SIG:
        c = np.cumsum(base * (n + 0.5) ** (-sg - 1.0))
        vals = [c[x - 2] for x in CHECK]
        g = [math.log10(vals[i + 1] / vals[i]) for i in range(len(vals) - 1)]
        rows[sg] = (vals, g)
        print(f"   sigma={sg:4.2f}  D(10^k), k={[round(math.log10(x)) for x in CHECK]}: "
              f"{['%.4g' % v for v in vals]}   growth per decade: {['%.3f' % x for x in g]}", flush=True)
    return rows


if __name__ == '__main__':
    t0 = time.time()
    lz = lambda_zeta(X)
    squeeze(f"zeta (X={X:.0e})", lz, 1.0)
    # F_{2.9,2} = zeta * (1 - alpha 2^-s)(1 - beta 2^-s), alpha+beta = -2.9, alpha*beta = 2
    a, q = 2.9, 2.0
    d = math.sqrt(a * a - 4 * q); al, be = (-a + d) / 2, (-a - d) / 2
    lF = lz.copy(); k = 1
    while q ** k <= X:
        lF[int(q ** k)] += -(al ** k + be ** k) * math.log(q); k += 1
    squeeze(f"F_(2.9,2) (Theta_F = {math.log(-be)/math.log(q):.5f})", lF, 1.0)
    print(f"   [time so far {time.time()-t0:.1f}s]", flush=True)
    NDH = min(X, int(float(sys.argv[2])) if len(sys.argv) > 2 else X)
    ld = lambda_dh(NDH)
    CHECK[:] = [c for c in CHECK if c <= NDH]
    squeeze(f"DH (X={NDH:.0e}; Theta_DH = 0.808517)", ld, 0.0)
    print(f"   [total time {time.time()-t0:.1f}s]")
