# theory unit (Session 40): the Legendre/sieve form (NOTE §3.4).  For S8(rho): M(z) = prod_{g-primes q <= z} (1 - 1/q) against
# (a) the PROVED floor from the lattice (all lattice points 1 + (k - 1/2)/rho as primes): M_lat(z) >= c(rho) z^{-rho}, and
# (b) the PNT-level size c/log z.  Also checks Legendre's identity pi(I) = sum_{d | P(sqrt u)} mu(d) N(I/d) on a few intervals.
# Usage: python3 s8_mertens.py RHO X
import heapq, math, sys, bisect
import numpy as np
rho = eval(sys.argv[1]); X = float(sys.argv[2])
val = [1.0]; lpf = [-1]; primes = []; cursor = []; heap = []; N = 1
def advance(i):
    c = cursor[i] + 1
    while lpf[c] > i: c += 1
    cursor[i] = c; heapq.heappush(heap, (primes[i] * val[c], i))
while True:
    xstar = 1.0 + (N - 0.5) / rho
    if heap and heap[0][0] <= xstar:
        x, i = heapq.heappop(heap)
        if x > X: break
        N += 1; val.append(x); lpf.append(i); advance(i)
    else:
        x = xstar
        if x > X: break
        N += 1; primes.append(x); val.append(x); lpf.append(len(primes) - 1); cursor.append(0); advance(len(primes) - 1)
P = np.array(primes); logM = np.cumsum(np.log1p(-1.0 / P))
print(f"S8 rho={rho:.8f} X={X:g} pi={len(P)}")
print("      z      M(z)     M(z)*log z    M_lat(z)*z^rho   (lattice floor, all k)")
for z in [10, 1e2, 1e3, 1e4, 1e5, 1e6, X]:
    j = np.searchsorted(P, z, side='right') - 1
    if j < 0: continue
    kmax = int(math.floor((z - 1.0) * rho + 0.5))
    lat = 1.0 + (np.arange(1, kmax + 1) - 0.5) / rho
    Mlat = math.exp(np.sum(np.log1p(-1.0 / lat)))
    print(f" {z:9.3g}  {math.exp(logM[j]):.6f}  {math.exp(logM[j])*math.log(z):9.4f}  {Mlat*z**rho:10.4f}")
# Legendre check on intervals I = (a, b] inside [X/4, X/2]: pi(I) vs sum over squarefree d | P(sqrt b) with d <= b of mu(d) N(I/d)
G = np.array(sorted(val)); Ncount = lambda y: int(np.searchsorted(G, y, side='right'))
small = [q for q in primes if q * q <= X / 2]
def legendre(a, b):
    tot = 0; stack = [(1.0, 1, 0)]        # (d, mu, next prime index), d squarefree with primes from 'small' below sqrt(b)
    lim = math.sqrt(b)
    while stack:
        d, mu, k = stack.pop()
        tot += mu * (Ncount(b / d) - Ncount(a / d))
        for j in range(k, len(small)):
            q = small[j]
            if q > lim or d * q > b: break
            stack.append((d * q, -mu, j + 1))
    return tot
Pl = list(primes)
for a in [X / 4, X / 4 + 1000.0, X / 3]:
    b = a + 200.0
    piI = bisect.bisect_right(Pl, b) - bisect.bisect_right(Pl, a)
    print(f"Legendre check on ({a:.1f}, {b:.1f}]: pi(I) = {piI}, sieve sum = {legendre(a, b)}")
