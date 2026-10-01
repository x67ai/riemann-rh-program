# read-O (U1-lookahead), own code: greedy threshold-tau system written from the definition (NOTE §0 notation):
# T(x) = rho(x-1) + 1; a g-prime is placed at the first x with T(x) - N(x) >= tau, i.e. at y = 1 + (n - 1 + tau)/rho,
# n = N(y-) (count incl. the unit 1); a composite at y is counted first (infimum convention).
# Enumeration: min-heap of future g-integers, each generated ONCE as p_j * m with lp(m) <= j (lp = largest prime index),
# at the later of {m processed, p_j placed}. Arithmetic: mpmath, DPS digits. Certificate: the smallest relative gap
# |s - y|/y over all placement decisions (s = next composite, y = candidate) and |s - X|; with DPS = 80 and at most
# ~300 factors per product the computed values have relative error < 1e-76, so a margin > 1e-70 certifies every decision.
# Usage: python3 bf_greedy.py RHO_EXPR X TAU [DPS] [dumpfile]
import sys, heapq
import mpmath as mp
DPS = int(sys.argv[4]) if len(sys.argv) > 4 else 80
mp.mp.dps = DPS
rho = eval(sys.argv[1], {"pi": mp.pi, "mpf": mp.mpf}); X = mp.mpf(sys.argv[2]); tau = mp.mpf(eval(sys.argv[3]))
t = 1/rho
DUP1 = len(sys.argv) > 6 and sys.argv[6] == 'dup1'   # test system: the first g-prime placed twice (repeated g-prime)
P = []                      # placed primes (values)
past = [(mp.mpf(1), -1)]    # processed g-integers (value, lp)
heap = []                   # (value, lp)
n = 1                       # N counts the unit 1
supE = mp.mpf(-10); infEm = mp.mpf(10); margin = mp.mpf(1); maxgap = mp.mpf(0); ncomp = 0
def E_after(x, cnt): return cnt - rho*(x - 1) - 1
while True:
    y = 1 + (n - 1 + tau)*t
    s = heap[0][0] if heap else None
    if s is not None:
        margin = min(margin, abs(s - y)/y, abs(s - X)/X)
    if s is not None and s <= y:
        v, lp = heapq.heappop(heap)
        if v > X: break
        infEm = min(infEm, E_after(v, n)); n += 1; ncomp += 1
        supE = max(supE, E_after(v, n))
        for j in range(lp, len(P)):          # j >= lp(m)
            w = P[j]*v
            if w > X: break
            heapq.heappush(heap, (w, j))
        past.append((v, lp))
        continue
    if y > X: break
    margin = min(margin, abs(y - X)/X)
    i = len(P); P.append(y)
    if i > 0: maxgap = max(maxgap, y - P[i-1])
    for (m, lpm) in past[1:]:                # m = 1 gives the prime itself (handled here)
        w = y*m
        if w > X: continue
        heapq.heappush(heap, (w, i))
    w = y*y
    if w <= X: heapq.heappush(heap, (w, i))
    infEm = min(infEm, E_after(y, n)); n += 1
    supE = max(supE, E_after(y, n))
    past.append((y, i))
    if DUP1 and i == 0:                      # second copy of p1: products with every past element (incl. the first copy)
        i2 = 1; P.append(y)
        for (m, lpm) in past[1:]:
            if y*m <= X: heapq.heappush(heap, (y*m, i2))
        n += 1; supE = max(supE, E_after(y, n)); past.append((y, i2))
print(f"OWN-BF rho={mp.nstr(rho,12)} X={sys.argv[2]} tau={sys.argv[3]} dps={DPS}: N={n} pi={len(P)} comp={ncomp} "
      f"supE={mp.nstr(supE,10)} infE(x-)={mp.nstr(infEm,10)} maxgap={mp.nstr(maxgap,8)} p1={mp.nstr(P[0],12)} "
      f"sum_primes={mp.nstr(mp.fsum(P),20)} min_rel_margin={mp.nstr(margin,3)}")
if len(sys.argv) > 5:
    with open(sys.argv[5], "w") as f:
        for v, lp in past: f.write(mp.nstr(v, 30) + "\n")
