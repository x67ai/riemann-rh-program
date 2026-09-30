# Orchestrator's independent re-run of N1's decisive computation (Session 37, read-F).
# Claim (Theorem 1 / Corollary 2 / Theorem K): for ANY unitary U, F(t) = det(I - Z(t) U), Z(t) = diag(p_j^{-it}),
# has N zeros in (-14.1, 14.1) with |N - W*L/(2 pi)| < |d| (W = sum log p_j, L = 28.2, |d| = number of slots),
# hence N >= 3, and every gap between consecutive zeros is <= 2 pi |d| / W;  Xi has no zero in (-14.1, 14.1).
# Independent method: zeros of F <=> an eigenvalue of the unitary Z(t)U equals 1; eigenphases move monotonically,
# so zeros are counted by tracking sin-products on a fine grid (sign changes of the real function below).
import numpy as np, math, mpmath
rng = np.random.default_rng(20260930)
def haar(n):
    z = (rng.standard_normal((n, n)) + 1j*rng.standard_normal((n, n)))/math.sqrt(2)
    q, r = np.linalg.qr(z); d = np.diag(r); return q*(d/abs(d))
def realified(t, logs, U, c):
    # det(I - W)/sqrt(det W) is real up to a constant phase c (W unitary): use a continuous branch via det W = det(U) e^{-i t W_tot}
    W = np.diag(np.exp(-1j*t*logs)) @ U
    val = np.linalg.det(np.eye(len(logs)) - W) * np.exp(0.5j*t*logs.sum()) * c
    return val
L0, L1 = -14.1, 14.1
worst = 0.0; rows = []
for trial in range(40):
    n = int(rng.integers(1, 9))
    primes = rng.choice([2, 3, 5, 7, 11, 13, 17, 19, 23], size=n, replace=True)
    logs = np.log(primes.astype(float)); U = haar(n)
    c = np.exp(-0.5j*np.angle(np.linalg.det(U)))          # removes the constant phase: val is real up to sign (-i)^n factor
    ts = np.linspace(L0, L1, 400001)
    vals = np.array([realified(t, logs, U, c) for t in ts[::100]])  # coarse to find the constant phase
    ph = np.angle(vals[np.argmax(abs(vals))]); 
    f = lambda t: (realified(t, logs, U, c)*np.exp(-1j*ph)).real
    g = np.array([f(t) for t in ts])
    im_max = max(abs((realified(t, logs, U, c)*np.exp(-1j*ph)).imag) for t in ts[::997])
    sc = np.nonzero(np.sign(g[:-1]) * np.sign(g[1:]) < 0)[0]
    N = len(sc); Wt = logs.sum(); pred = Wt*(L1-L0)/(2*math.pi)
    zeros = ts[sc]; gap = np.diff(zeros).max() if N > 1 else float('nan')
    bound_gap = 2*math.pi*n/Wt
    worst = max(worst, abs(N - pred)/n)
    rows.append((n, list(map(int, primes)), N, round(pred, 3), round(abs(N-pred), 3), round(gap, 4), round(bound_gap, 4), im_max < 1e-9))
    assert N >= 3 and abs(N - pred) < n + 1e-9 and (N < 2 or gap <= bound_gap + 1e-3), rows[-1]
for r in rows[:12]: print(r)
print("trials:", len(rows), " min N:", min(r[2] for r in rows), " worst |N - pred|/|d|:", round(worst, 4), "(theorem: < 1)")
print("single prime 2: zeros of 1 - 2^{-it} u spaced exactly 2 pi/log 2 =", 2*math.pi/math.log(2))
mpmath.mp.dps = 25
print("zeta zeros with 0 < t < 14.2 (mpmath nzeros):", mpmath.nzeros(14.2), "; first zero:", mpmath.zetazero(1))
