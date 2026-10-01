# chebyshev.py — U7-patterns: numerical check of the exact multiscale identity (Theorem 5.3 of the NOTE)
#   sum_{d<=x} Lambda(d) E(x/d) = E(x) log x - int_1^x E(u) du/u + rho x (log x - 1 - sum_{d<=x} Lambda(d)/d) + rho - (1-rho) psi(x)
# and of its one-sided consequence. Usage: python3 chebyshev.py primes.u32 D tau X1 X2 ...   (g-integers enumerated in float64)
import sys, math, numpy as np
pf, D, tau = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]); Xs = [float(v) for v in sys.argv[4:]]
rho = math.pi / D; t = 1 / rho; Xmax = max(Xs)
pk = np.fromfile(pf, np.uint32); P = 1 + (pk.astype(np.float64) - 1 + tau) * t; P = P[P <= Xmax]
G = []
def dfs(m, i):
    G.append(m)
    for j in range(i, len(P)):
        v = m * P[j]
        if v > Xmax: break
        dfs(v, j)
sys.setrecursionlimit(10000); dfs(1.0, 0); G = np.sort(np.array(G))
N = lambda y: np.searchsorted(G, y, side='right')
E = lambda y: N(y) - rho * (y - 1) - 1
for X in Xs:
    # prime powers d <= X with Lambda(d) = log p
    dl, lam = [], []
    for p in P:
        if p > X: break
        q = p
        while q <= X: dl.append(q); lam.append(math.log(p)); q *= p
    dl, lam = np.array(dl), np.array(lam)
    lhs = float((lam * E(X / dl)).sum()); psi = float(lam.sum()); S = float((lam / dl).sum())
    # integral of E(u)/u on [1, X]: on [g_i, g_{i+1}) N = i + 1, E = (i + 1) - rho(u - 1) - 1
    g = G[G <= X]; a = g; b = np.append(g[1:], X); i = np.arange(len(g)); A = (i + 1) - 1 + rho
    integ = float((A * np.log(b / a) - rho * (b - a)).sum())
    rhs = float(E(X)) * math.log(X) - integ + rho * X * (math.log(X) - 1 - S) + rho - (1 - rho) * psi
    print("rho=pi/%d x=%.0e: LHS=%.6f RHS=%.6f diff=%.2e | psi(x)/x=%.5f, sum Lambda(d)/d - log x = %.5f, Lambda-weighted mean of E over x/d = %.4f"
          % (D, X, lhs, rhs, lhs - rhs, psi / X, S - math.log(X), lhs / psi))
