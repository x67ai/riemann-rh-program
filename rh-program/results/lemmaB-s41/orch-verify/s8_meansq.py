# Orchestrator check for note O1 (Session 41): mean square of the integer error E of S8(rho) per half-decade block.
# Generator: event loop of the Session-40 prototype, with g-primes placed at the exact lattice point 1 + (N - 1/2)/rho
# (no incremental deficit). Between events E(u) = E0 - rho*(u - x0), so block integrals of E and E^2 are exact.
import heapq, math, sys, time
rho = eval(sys.argv[1]); X = float(sys.argv[2])
t0 = time.time()
val = [1.0]; lpf = [-1]; primes = []; cursor = []; heap = []
N = 1; x0 = 1.0
def E_at(x, n): return n - rho * (x - 1.0) - 1.0
def advance(i):
    c = cursor[i] + 1
    while lpf[c] > i: c += 1
    cursor[i] = c
    heapq.heappush(heap, (primes[i] * val[c], i))
edge = 10.0 ** 0.5; lo = 1.0
I1 = I2 = 0.0; sup = -1.0; rows = []
def integrate(a, b, n):
    """add the integrals of E and E^2 over [a, b) with count n constant there"""
    global I1, I2, sup
    Ea = E_at(a, n); Eb = E_at(b, n)
    I1 += (Ea + Eb) * (b - a) / 2.0
    I2 += (Ea ** 3 - Eb ** 3) / (3.0 * rho)
    if Ea > sup: sup = Ea
while True:
    xstar = 1.0 + (N - 0.5) / rho
    if heap and heap[0][0] <= xstar:
        x, i = heapq.heappop(heap); comp = True
    else:
        x = xstar; comp = False
    xe = min(x, X)
    a = x0
    while edge <= xe:                      # close blocks crossed before this event
        integrate(a, edge, N); a = edge
        L = edge - lo
        rows.append((lo, edge, I1 / L, math.sqrt(I2 / L), sup))
        lo = edge; edge *= 10.0 ** 0.5; I1 = I2 = 0.0; sup = -1.0
    integrate(a, xe, N)
    if x > X: break
    N += 1; x0 = x
    if comp:
        val.append(x); lpf.append(i); advance(i)
    else:
        primes.append(x); val.append(x); lpf.append(len(primes) - 1); cursor.append(0); advance(len(primes) - 1)
print(f"S8 rho={rho:.12f} X={X:g} N={N} primes={len(primes)} time={time.time()-t0:.1f}s")
print("block [lo, hi)          mean E    rms E    sup E   rms/log(hi)  rms/hi^0.1  sup/log^2(hi)")
for lo_, hi, m, r, s in rows:
    lg = math.log(hi)
    print(f"[{lo_:10.4g},{hi:10.4g})  {m:8.4f} {r:8.4f} {s:8.3f}   {r/lg:8.4f}    {r/hi**0.1:8.4f}    {s/lg**2:8.4f}")
