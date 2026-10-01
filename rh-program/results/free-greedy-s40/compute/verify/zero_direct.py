# zero_direct.py GINTFILE X E(X) RHO SIGMA0 T0 -- Newton for a zero of F_X by the DIRECT sum over the dumped g-integers
# (no block moments): F_X(s) = sum_{n<=X} n^-s + rho X^{1-s}/(s-1) - E(X) X^-s,  F_X'(s) by the direct sum of -log n n^-s.
import sys, math, numpy as np
g = np.fromfile(sys.argv[1], dtype=np.float64).reshape(-1, 2)
X, EX, rho = float(sys.argv[2]), float(sys.argv[3]), float(eval(sys.argv[4], {"pi": math.pi}))
g = g[g[:, 0] <= X]; L = np.log(g[:, 0]) + g[:, 1] / g[:, 0]; lX = math.log(X)
def F(s):
    e = np.exp(-s * L); Xs = np.exp(-s * lX)
    v = complex(e.sum()) + rho * X * Xs / (s - 1) - EX * Xs
    d = -complex((L * e).sum()) - rho * X * Xs * (lX / (s - 1) + 1 / (s - 1) ** 2) + EX * Xs * lX
    return v, d
s = complex(float(sys.argv[5]), float(sys.argv[6]))
for it in range(30):
    v, d = F(s); ds = v / d; s -= ds
    if abs(ds) < 1e-14: break
print(f"# direct-sum Newton, X = {X:.3e} ({len(L)} g-integers): zero at {s.real:.12f} + {s.imag:.12f}i, |F_X| = {abs(F(s)[0]):.2e}, |F_X'| = {abs(F(s)[1]):.4f}")
