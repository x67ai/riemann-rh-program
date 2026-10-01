# U3-firstbound, ATTEMPT 1 checks. Event loop copied from orch-verify/s8_meansq.py (exact lattice placement
# 1 + (N - 1/2)/rho; heap of next composite per g-prime; composites n = p_i * m with P+(m) <= p_i, so each multiset once).
# Tracks psi, S = sum Lambda(d)/d, Psi~ = int psi/u^2, E; checks Step B (F(y) <= (log y + rho)/y at g-primes),
# Step C (F <= eps on decades), Step D (min of D), Step E (records of E(u)/u and the record inequality), identity (*).
import heapq, math, sys, time, bisect
rho = eval(sys.argv[1]); X = float(sys.argv[2])
t0 = time.time()
val = [1.0]; lpf = [-1]; ppw = [-2]; primes = []; cursor = []; heap = []
N = 1; x0 = 1.0
psi = 0.0; S = 0.0; Pt = 0.0            # psi, S, Psi~ at the current point (after the event)
ppl = []                                 # prime powers (d, log p) for the identity check
def advance(i):
    c = cursor[i] + 1
    while lpf[c] > i: c += 1
    cursor[i] = c
    heapq.heappush(heap, (primes[i] * val[c], i, c))
maxBviol = -1e9; nB = 0                  # max of F(y) - (log y + rho)/y over g-primes
dec = {}                                 # per decade: max F, min D, min Delta
recs = []                                # records of E(x)/x
A = 0.0
checks = [10.0 ** k for k in (3, 4, 5, 6)]
def F_of(x): return psi / (2 * x) + rho * Pt - rho * (math.log(x) - 1.0)
while True:
    xstar = 1.0 + (N - 0.5) / rho
    if heap and heap[0][0] <= xstar:
        x, i, c = heapq.heappop(heap); comp = True
    else:
        x = xstar; comp = False
    if x > X: break
    # advance Psi~ over [x0, x) with psi constant; F decreases there (checked at the endpoints only)
    Pt += psi * (1.0 / x0 - 1.0 / x)
    N += 1; x0 = x
    if comp:
        isp = i if ppw[c] == i else -1
        val.append(x); lpf.append(i); ppw.append(isp); advance(i)
    else:
        isp = len(primes)
        primes.append(x); val.append(x); lpf.append(isp); ppw.append(isp); cursor.append(0); advance(isp)
    if isp >= 0:
        lp = math.log(primes[isp]); psi += lp; S += lp / x; ppl.append((x, lp))
    E = N - rho * (x - 1.0) - 1.0
    lx = math.log(x)
    F = F_of(x); Dv = lx - 1.0 - Pt; Dl = lx - 1.0 - S
    k = int(math.floor(lx / math.log(10.0)))
    m = dec.get(k)
    if m is None: dec[k] = [F, Dv, Dl, E / x]
    else:
        if F > m[0]: m[0] = F
        if Dv < m[1]: m[1] = Dv
        if Dl < m[2]: m[2] = Dl
        if E / x > m[3]: m[3] = E / x
    if not comp:
        v = F - (lx + rho) / x; nB += 1
        if v > maxBviol: maxBviol = v
    if E / x > A:
        A = E / x
        u = psi / x
        lhs = (A + rho) * Dl; rhs = (1 - rho) * u - rho / x
        recs.append((x, A, E, u, Dv, Dl, lhs - rhs, comp))
print(f"S8 rho={rho:.12f} X={X:g} N={N} primes={len(primes)} time={time.time()-t0:.1f}s")
print(f"Step B: g-primes checked {nB}, max[F(y) - (log y + rho)/y] = {maxBviol:.6g}  (must be <= 0)")
print("decade   max F      min D     min Delta   max E/x    [1/(2rho) = %.4f, rho/(1-2rho) = %.4f]" % (1/(2*rho), rho/(1-2*rho)))
for k in sorted(dec):
    m = dec[k]; print(f"1e{k:<3d}  {m[0]:9.5f}  {m[1]:9.5f}  {m[2]:9.5f}  {m[3]:.3e}")
print(f"records of E(x)/x: {len(recs)}; last ten:")
print("   x            A=E/x       E      psi/x     D       Delta   (A+rho)Delta-[(1-rho)psi/x-rho/x] (<=0)  comp")
for r in recs[-10:]:
    print(f"{r[0]:12.6f} {r[1]:10.6f} {r[2]:7.4f} {r[3]:8.5f} {r[4]:8.5f} {r[5]:8.5f}   {r[6]:+.3e}   {r[7]}")
print(f"max over all records of the record-inequality residual: {max(r[6] for r in recs):+.3e}")
# identity (*) at a few points: E(x)logx - int E/u = psi + rho x Psi~ - rho x (log x - 1) - rho + sum Lambda(d) E(x/d)
def Nof(y): return bisect.bisect_right(val, y)
def Eof(y): return Nof(y) - rho * (y - 1.0) - 1.0
def intEu(x):   # int_1^x E(u)/u du exactly: N constant between g-integers
    tot = 0.0; prev = 1.0; n = 1
    for v in val[1:]:
        if v > x: break
        tot += (n - 1.0 + rho) * math.log(v / prev) - rho * (v - prev); prev = v; n += 1
    tot += (n - 1.0 + rho) * math.log(x / prev) - rho * (x - prev)
    return tot
for xc in checks:
    if xc > X: continue
    ps = sum(lp for d, lp in ppl if d <= xc)
    pt = 0.0; prev = 1.0; cur = 0.0
    for d, lp in ppl:
        if d > xc: break
        pt += cur * (1.0 / prev - 1.0 / d); cur += lp; prev = d
    pt += cur * (1.0 / prev - 1.0 / xc)
    lhs = Eof(xc) * math.log(xc) - intEu(xc)
    rhs = ps + rho * xc * pt - rho * xc * (math.log(xc) - 1.0) - rho + sum(lp * Eof(xc / d) for d, lp in ppl if d <= xc)
    print(f"identity (*) at x={xc:g}: lhs={lhs:.6f} rhs={rhs:.6f} diff={lhs-rhs:+.2e}")
print(f"done {time.time()-t0:.1f}s")
