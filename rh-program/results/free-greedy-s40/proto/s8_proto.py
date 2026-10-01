# Orchestrator prototype (Session 40): S8(rho), the REAL-position integer-greedy system.
# g-primes are real numbers placed exactly when the deficit T(x) - N(x-) reaches 1/2, T(x) = rho*(x-1) + 1;
# they therefore sit on the lattice 1 + (k - 1/2)/rho, k integer.  For transcendental 1/rho distinct multisets of
# g-primes have distinct products (unique factorization in Q[t], t = 1/rho), so there are NO multiplicities:
# the g-integers form a free monoid of distinct reals.  Event-driven sweep with a heap of "next composite per g-prime".
import heapq, math, sys, time
rho = eval(sys.argv[1]) if len(sys.argv) > 1 else math.pi / 4
X = float(sys.argv[2]) if len(sys.argv) > 2 else 1e6
t0 = time.time()
val = [1.0]; lpf = [-1]          # sorted list of g-integers and index of their largest g-prime (-1 for the unit)
primes = []; cursor = []          # g-prime values; cursor[i] = index in val of the last multiplier used for prime i
heap = []                         # (position, prime index)
N = 1; x0 = 1.0; D0 = 0.0         # count, last event position, deficit T - N just after the last event (T(1) - N = 0)
psi = 0.0; powheap = []           # Chebyshev psi: add log q at q^k
supE = 0.0; supPsi = 0.0; maxcluster = 0
recs = []; nextdec = 10.0
lastpos = []                      # for cluster statistics: positions in a sliding unit window
from collections import deque
win = deque()
def advance(i):
    """push the next composite of g-prime i: q * (next entry after cursor with lpf <= i)"""
    c = cursor[i] + 1
    while lpf[c] > i: c += 1
    cursor[i] = c
    heapq.heappush(heap, (primes[i] * val[c], i))
while True:
    xstar = x0 + (0.5 - D0) / rho                 # time at which the deficit reaches 1/2 if nothing arrives
    if heap and heap[0][0] <= xstar:
        x, i = heapq.heappop(heap)
        if x > X: break
        # composite arrives: deficit grows linearly then drops by 1
        Dbefore = D0 + rho * (x - x0)
        D0 = Dbefore - 1.0; x0 = x; N += 1
        val.append(x); lpf.append(i)
        advance(i)
        E = -D0                                   # N - T just after the event
        if E > supE: supE = E
        isprime = False
    else:
        x = xstar
        if x > X: break
        D0 = -0.5; x0 = x; N += 1
        primes.append(x); val.append(x); lpf.append(len(primes) - 1); cursor.append(0)
        advance(len(primes) - 1)
        lq = math.log(x); psi += lq
        if x * x <= X: heapq.heappush(powheap, (x * x, x, lq))
        isprime = True
    while powheap and powheap[0][0] <= x:
        pw, q, lq = heapq.heappop(powheap); psi += lq
        if pw * q <= X: heapq.heappush(powheap, (pw * q, q, lq))
    d = abs(psi - x)
    if d > supPsi: supPsi = d
    win.append(x)
    while win[0] < x - 1.0: win.popleft()
    if len(win) > maxcluster: maxcluster = len(win)
    if x >= nextdec:
        recs.append((nextdec, N, len(primes), supE, supPsi, maxcluster, psi - x))
        nextdec *= 10 ** 0.5
print(f"S8 rho = {rho:.12f}  X = {X:g}  g-integers = {N}  g-primes = {len(primes)}  time = {time.time()-t0:.1f}s")
print("   x        N(x)      pi_P(x)   sup E   sup|psi-x|  max #g-int in a unit window   psi-x")
prev = None
for r in recs:
    s = ""
    if prev and prev[3] > 0 and prev[4] > 0:
        s = f"  slopes: E {math.log(r[3]/prev[3])/math.log(r[0]/prev[0]):+.3f}  psi {math.log(r[4]/prev[4])/math.log(r[0]/prev[0]):+.3f}"
    print(f"{r[0]:10.3g} {r[1]:10d} {r[2]:9d} {r[3]:8.2f} {r[4]:10.1f} {r[5]:5d} {r[6]:12.1f}{s}")
    prev = r
print("first g-primes:", [round(q, 4) for q in primes[:14]])
