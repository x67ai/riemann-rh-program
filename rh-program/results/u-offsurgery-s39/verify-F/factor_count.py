# Orchestrator (Session 40).  Rigorous LOWER bounds for the multiplicity a_n of S5(4/5) at integers n > 10^9.
# a_n = number of multisets of g-primes with product n.  Using only the g-primes <= 10^9 (computed exactly by
# s5gen_F.c; every multiplicity m_q = 1) gives a lower bound a_n^known <= a_n: later g-primes can only add
# representations, and the g-primes <= 10^9 are fixed forever by the deterministic rule.
# Consequence used: E(n) - E(n-1) = a_n - rho and E >= -1 - rho, so sup_{u<=n}|N(u) - rho*floor(u)| >= (a_n - 3)/2.
import numpy as np, sys, math, time
SP = sys.argv[1]
gp = np.fromfile(SP + "/gpF_r08_1e9.u32", dtype=np.uint32).reshape(-1, 2)
assert (gp[:, 1] == 1).all()
G = gp[:, 0].astype(np.int64)          # sorted increasing
LIM = 10**9
def gdivisors(primes, exps):
    """all divisors d <= LIM of n = prod p^e that are g-primes; returns list of exponent vectors"""
    vals = np.array([1], dtype=np.int64); vecs = np.zeros((1, len(primes)), dtype=np.int16)
    for i, (p, e) in enumerate(zip(primes, exps)):
        newv, newx = [vals], [vecs]
        cur, curx = vals, vecs
        for j in range(1, e + 1):
            keep = cur <= LIM // p
            cur = cur[keep] * p; curx = curx[keep].copy(); curx[:, i] = j
            if len(cur) == 0: break
            newv.append(cur); newx.append(curx)
        vals = np.concatenate(newv); vecs = np.concatenate(newx)
    idx = np.searchsorted(G, vals); idx[idx >= len(G)] = len(G) - 1
    isg = (G[idx] == vals) & (vals > 1)
    return vals[isg], vecs[isg]
def count(primes, exps, exact=False):
    vals, vecs = gdivisors(primes, exps)
    shape = tuple(e + 1 for e in exps)
    f = np.zeros(shape, dtype=object if exact else np.float64)
    f[(0,) * len(primes)] = 1
    order = np.argsort(vals)
    for t in order:
        v = vecs[t]
        j = int(np.argmax(v > 0))
        for lev in range(v[j], exps[j] + 1):
            dst = tuple(lev if i == j else slice(int(v[i]), None) for i in range(len(primes)))
            src = tuple(lev - int(v[j]) if i == j else slice(0, exps[i] + 1 - int(v[i])) for i in range(len(primes)))
            f[dst] += f[src]
    return f[tuple(exps)], len(vals)
if __name__ == "__main__":
    # self-test against the exact dump: n = 902538000 = 2^4 3^2 5^3 7 13 19 29 must give 276
    a, k = count([2, 3, 5, 7, 13, 19, 29], [4, 2, 3, 1, 1, 1, 1], exact=True)
    print("self-test a(902538000) =", a, " (#g-prime divisors:", k, ")  expected 276")
    a, k = count([2, 3, 5, 7, 19], [4, 2, 2, 1, 1], exact=True)
    print("self-test a(478800) =", a, " expected 26")
