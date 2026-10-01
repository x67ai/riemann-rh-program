# theory unit (Session 40): the randomized rule S8^w of NOTE §3.1 (early placement), by blocks [B, p1*B).
# Composites in [B, p1 B) are products q*m with q, m < B (every factor of a composite n is <= n/p1), so a block's composites are
# known before its primes are placed.  Deficit bookkeeping counts each prime at its deficit time x* = 1 + (Nbook - 1/2)/rho; the
# prime's ACTUAL position is max(B, x* - w*U), U ~ Uniform(0,1) (the clip at B keeps its composites out of the current block).
# Since actual primes are no later than bookkeeping primes, the true deficit never exceeds the bookkeeping one: E > -1/2 holds for
# every realization (checked below).  w = 0 reproduces S8 exactly.  Usage: python3 s8w_block.py RHO X W SEED
import math, sys, bisect
import numpy as np
rho = eval(sys.argv[1]); X = float(sys.argv[2]); w = float(sys.argv[3]); seed = int(sys.argv[4])
rng = np.random.default_rng(seed); t = 1.0 / rho; p1 = 1.0 + t / 2.0
G = np.array([1.0]); L = np.array([-1], dtype=np.int64)          # sorted g-integers and largest prime index
primes = []; Nbook = 1; B = 1.0
while B < X:
    Bh = min(B * p1, X)
    comp = []; cl = []
    for i, q in enumerate(primes):
        if q * p1 >= Bh: break                                    # q*m >= q*p1 for m > 1
        lo = np.searchsorted(G, B / q, side='left'); hi = np.searchsorted(G, Bh / q, side='left')
        if hi <= lo: continue
        sel = (L[lo:hi] <= i) & (G[lo:hi] > 1.0)
        v = q * G[lo:hi][sel]; v = v[(v >= B) & (v < Bh)]
        if v.size: comp.append(v); cl.append(np.full(v.size, i, dtype=np.int64))
    if comp:
        cv = np.concatenate(comp); ci = np.concatenate(cl); o = np.argsort(cv, kind='stable'); cv = cv[o]; ci = ci[o]
    else:
        cv = np.array([]); ci = np.array([], dtype=np.int64)
    newp = []; j = 0
    while True:
        xstar = 1.0 + (Nbook - 0.5) / rho
        if j < cv.size and cv[j] <= xstar:
            Nbook += 1; j += 1
        else:
            if xstar >= Bh: break
            pos = max(B, xstar - w * rng.random()) if w > 0 else xstar
            primes.append(pos); newp.append((pos, len(primes) - 1)); Nbook += 1
    while j < cv.size: Nbook += 1; j += 1                        # (unreachable: loop exits only past the block)
    pv = np.array([p for p, _ in newp]); pi_ = np.array([k for _, k in newp], dtype=np.int64)
    allv = np.concatenate([G, cv, pv]); allL = np.concatenate([L, ci, pi_]); o = np.argsort(allv, kind='stable')
    G = allv[o]; L = allL[o]; B = Bh
    if primes and not all(primes[k] <= primes[k + 1] or w > 0 for k in range(len(primes) - 1)): pass
G = G[G <= X]; n = np.arange(1, G.size + 1, dtype=np.float64)       # N at each g-integer (right-continuous)
T = rho * (G - 1.0) + 1.0
Eleft = (n - 1.0) - T; Eright = n - T
lv = np.log(G); EX = G.size - (rho * (X - 1.0) + 1.0)
def FX(s): return math.fsum(np.exp(-s * lv).tolist()) + rho * X ** (1 - s) / (s - 1) - EX * X ** (-s)
lo_, hi_ = 0.05, 0.9999
for _ in range(45):
    mid = 0.5 * (lo_ + hi_)
    if FX(mid) > 0: lo_ = mid
    else: hi_ = mid
print(f"S8^w rho={rho:.8f} X={X:g} w={w} seed={seed}: N={G.size} pi={len(primes)}  min E(x-)={Eleft[1:].min():+.12f}  "
      f"min E={Eright.min():+.4f}  sup E={Eright.max():.3f}  sup E/log^2X={Eright.max()/math.log(X)**2:.4f}  sigma*={0.5*(lo_+hi_):.6f}")
