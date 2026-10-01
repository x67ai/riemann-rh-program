# read-O: own S8(rho) generator from s40 NOTE 1.0 (p_{k+1} = inf{x >= p_k : T(x) - N_k(x) >= 1/2}, T = rho(x-1)+1),
# written from the definition only: Lindley deadline iteration x = p_k + (1 + c)/rho, c = composites in (p_k, x].
# Double precision (statistics, not certificates). Reports pi(X), sup E, the composite excess Q(X) (Kadane), sup E - Q.
import heapq, bisect, sys, math
rho = math.pi/16 if len(sys.argv) < 3 else math.pi/float(sys.argv[2])
X = float(sys.argv[1]) if len(sys.argv) > 1 else 1e6
p1 = 1 + 1/(2*rho)
small = [1.0]            # sorted g-integers <= X/p1 (the only ones ever used as cofactors)
heap = []                # pending composites (> current prime), <= X
primes = []
def add_prime(p):
    lim = X/p
    base = small[:bisect.bisect_right(small, lim)]      # G_{k-1} up to X/p (snapshot before adding p)
    new = []
    for m in base:
        v = m*p
        while v <= X:
            new.append(v); v *= p
    for v in new:
        if v != p: heapq.heappush(heap, v)
        if v <= X/p1: bisect.insort(small, v)
# sweep
pk, N = 1.0 - 1/(2*rho), 1   # virtual start: D(1) = 0, so the first deadline is 1 + 1/(2 rho) (s40 1.0, p_1 = 1 + t/2)
supE, comps = 0.0, []
while True:
    c = 0; x = pk + 1/rho
    swept = []
    while True:
        while heap and heap[0] <= x:
            swept.append(heapq.heappop(heap)); c += 1
        xn = pk + (1 + c)/rho
        if xn == x: break
        x = xn
    for v in swept:                                   # composites in (pk, x): E jumps up at each
        if v > X: continue
        N += 1; supE = max(supE, N - rho*(v - 1) - 1); comps.append(v)
    if x > X: break
    N += 1; primes.append(x); supE = max(supE, N - rho*(x - 1) - 1)
    add_prime(x); pk = x
# leftover composites beyond the last prime but <= X
while heap:
    v = heapq.heappop(heap)
    if v <= X:
        N += 1; supE = max(supE, N - rho*(v - 1) - 1); comps.append(v)
comps.sort()
best, mn = 1.0, float('inf')
for j, cj in enumerate(comps, start=1):
    mn = min(mn, (j - 1) - rho*cj)
    best = max(best, (j - rho*cj) - mn)
print(f"rho=pi/{round(math.pi/rho)} X={X:g}: pi(X)={len(primes)} composites={len(comps)} N(X)={N} supE={supE:.4f} Q={best:.4f} supE-Q={supE-best:+.4f}")
