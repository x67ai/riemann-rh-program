# read-O: real zero sigma* of F_X(s) = sum_{n<=X} n^-s + rho X^(1-s)/(s-1) - E(X) X^-s from a dump of all g-integers <= X (own bf_greedy.py).
import sys, math
import numpy as np, mpmath as mp
rho = float(eval(sys.argv[1], {"pi": math.pi})); X = float(sys.argv[2]); f = sys.argv[3]
G = np.array([float(l) for l in open(f)]); G = G[G <= X]; lv = np.log(G); EX = G.size - (rho*(X - 1) + 1)
def FX(s): return math.fsum(np.exp(-s*lv).tolist()) + rho*X**(1 - s)/(s - 1) - EX*X**(-s)
lo, hi = 0.5, 0.99999
assert FX(lo) > 0 or True
for _ in range(50):
    m = 0.5*(lo + hi)
    if FX(m) > 0: lo = m
    else: hi = m
print(f"{f}: N={G.size} E(X)={EX:.4f} sigma*={0.5*(lo+hi):.7f}")
