# read-O (U1-lookahead), own code: the early-placement rule S8^w AS IMPLEMENTED in s40 `s8w_block.py` (stated there in its
# header): bookkeeping count Nb (composites + each prime counted at its deficit time x* = 1 + (Nb - 1/2)/rho); the prime's
# actual position is max(B, x* - w*U), U = rng.random() drawn once per prime in placement order (numpy default_rng(seed)),
# B = the block start p1^k <= x* (float64 chain B_{k+1} = B_k*p1, B_0 = 1, as in s40), p1 = 1 + t/2 never moved.
# Enumeration: sweep over the bookkeeping events (no blocks); g-integers from ACTUAL positions via a heap, each generated
# once as p_j*m with lp(m) <= j, at the later of {m processed, p_j placed}. Arithmetic: mpmath DPS digits.
# Statistics on the ACTUAL multiset: N(X), pi, sup E after events, sigma* (root of F_X). Usage: RHO_EXPR X W SEED [DPS]
import sys, heapq, math
import numpy as np, mpmath as mp
mp.mp.dps = int(sys.argv[5]) if len(sys.argv) > 5 else 40
FIXED = len(sys.argv) > 6 and sys.argv[6] == 'fixed'   # U1 rules.cpp 'early': pos = max(B, x* - W) (U = 1, no draw)
rho = eval(sys.argv[1], {"pi": mp.pi}); X = mp.mpf(sys.argv[2]); w = float(sys.argv[3]); seed = int(sys.argv[4])
rng = np.random.default_rng(seed); t = 1/rho; p1 = 1 + t/2
rho_f = float(rho); p1_f = 1.0 + (1.0/rho_f)/2.0
Bs = [1.0]
while Bs[-1] < float(X): Bs.append(min(Bs[-1]*p1_f, float(X)))
def block_start(x):            # largest B_k <= x (B_k as float64, exactly as s40)
    lo, hi = 0, len(Bs) - 1
    while lo < hi:
        mid = (lo + hi + 1)//2
        if mp.mpf(Bs[mid]) <= x: lo = mid
        else: hi = mid - 1
    return mp.mpf(Bs[lo])
P = []; past = [(mp.mpf(1), -1)]; heap = []; Nb = 1
while True:
    xs = 1 + (Nb - mp.mpf(1)/2)*t
    if heap and heap[0][0] <= xs:
        v, lp = heapq.heappop(heap)
        if v > X: break
        Nb += 1
        for j in range(lp, len(P)):
            q = P[j]
            if q*v > X: continue          # P is not sorted when w > 0: no early break
            heapq.heappush(heap, (q*v, j))
        past.append((v, lp)); continue
    if xs > X: break
    if w == 0: pos = xs
    else:
        u = 1.0 if FIXED else rng.random()  # s40 draws for p1 too (its clip max(B, .) returns B = p1)
        pos = xs if len(P) == 0 else max(block_start(xs), xs - w*u)
    i = len(P); P.append(pos)
    for (m, lpm) in past[1:]:
        if pos*m <= X: heapq.heappush(heap, (pos*m, i))
    if pos*pos <= X: heapq.heappush(heap, (pos*pos, i))
    # the prime itself is an element of the ACTUAL multiset at pos (<= xs); bookkeeping counts it now
    Nb += 1; past.append((pos, i))
G = sorted(float(v) for v, _ in past if v <= X)
n = np.arange(1, len(G) + 1, dtype=np.float64); Ga = np.array(G)
Er = n - (rho_f*(Ga - 1.0) + 1.0)
lv = np.log(Ga); EX = len(G) - (rho_f*(float(X) - 1.0) + 1.0)
def FX(s): return math.fsum(np.exp(-s*lv).tolist()) + rho_f*float(X)**(1 - s)/(s - 1) - EX*float(X)**(-s)
lo_, hi_ = 0.05, 0.9999
for _ in range(45):
    mid = 0.5*(lo_ + hi_)
    if FX(mid) > 0: lo_ = mid
    else: hi_ = mid
print(f"OWN-S8w X={sys.argv[2]} w={w} seed={seed}: N={len(G)} pi={len(P)} supE={Er.max():.3f} sigma*={0.5*(lo_+hi_):.6f} "
     )
