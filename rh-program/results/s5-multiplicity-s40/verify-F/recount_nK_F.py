# Orchestrator (Session 40): independent recount of f_G(n_K), the number of factorizations of
#   n_K = 2^8 3^5 5^9 7^3 11^2 13 17 19^3 23 29^2 37 41^2 59 61 79 89 109 149
# into the g-primes <= 10^9 of S5(4/5) (the orchestrator's own generator dump), by the orchestrator's own
# divisor-lattice dynamic program (int64 cells; the claimed value 3,403,961,916,617,140 < 2^63).
# Unit s5-multiplicity-s40 claims f_G(n_K) = 3403961916617140 with 2525 g-prime divisors.
import numpy as np, sys, time, math
gp = np.fromfile("/private/tmp/rh-s40-shared/s5/gpF_r08_1e9.u32", dtype=np.uint32).reshape(-1, 2)
assert (gp[:, 1] == 1).all()
G = gp[:, 0].astype(np.int64); LIM = 10**9
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 37, 41, 59, 61, 79, 89, 109, 149]
exps   = [8, 5, 9, 3, 2, 1, 1, 3, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1]
n = 1
for p, e in zip(primes, exps): n *= p**e
print("n_K =", n, " log10 =", math.log10(n), flush=True)
vals = np.array([1], dtype=np.int64); vecs = np.zeros((1, len(primes)), dtype=np.int8)
for i, (p, e) in enumerate(zip(primes, exps)):
    newv, newx = [vals], [vecs]; cur, curx = vals, vecs
    for j in range(1, e + 1):
        keep = cur <= LIM // p
        cur = cur[keep] * p; curx = curx[keep].copy(); curx[:, i] = j
        if len(cur) == 0: break
        newv.append(cur); newx.append(curx)
    vals = np.concatenate(newv); vecs = np.concatenate(newx)
idx = np.searchsorted(G, vals); idx[idx >= len(G)] = len(G) - 1
isg = (G[idx] == vals) & (vals > 1)
gv, gx = vals[isg], vecs[isg]
print("divisors <= 1e9:", len(vals), " g-prime divisors:", len(gv), flush=True)
shape = tuple(e + 1 for e in exps)
f = np.zeros(shape, dtype=np.int64); f[(0,) * len(primes)] = 1
t0 = time.time()
for c, t in enumerate(np.argsort(gv)):
    v = gx[t]; j = int(np.argmax(v > 0))
    for lev in range(int(v[j]), exps[j] + 1):
        dst = tuple(lev if i == j else slice(int(v[i]), None) for i in range(len(primes)))
        src = tuple(lev - int(v[j]) if i == j else slice(0, exps[i] + 1 - int(v[i])) for i in range(len(primes)))
        f[dst] += f[src]
    if c % 250 == 0: print(f"  {c} / {len(gv)} g-primes, {time.time()-t0:.0f}s", flush=True)
fn = int(f[tuple(exps)])
print("f_G(n_K) =", fn, "  max cell =", int(f.max()), " (int64 limit 9.22e18)")
print("claimed    3403961916617140   equal:", fn == 3403961916617140)
# the K test in exact integers: (25(f - 3))^20 > 94^20 * n^7   <=>  f - 3 > 3.76 * n^0.35
print("K test (25(f-3))^20 > 94^20 n^7 :", (25 * (fn - 3))**20 > 94**20 * n**7, "  exponent log f/log n =", math.log(fn) / math.log(n))
