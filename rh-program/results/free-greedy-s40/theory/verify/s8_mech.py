# theory unit, free-greedy-s40 (Session 40). Mechanism measurements for S8(rho) (NOTE §2), drift-free generator.
# Per half-decade [x/sqrt10, x]: sup E, max prime gap G and the bound rho*G - 1/2 (Prop. 2.1), time-average of E vs the queue
# prediction rho*log(u)/2, the exponential tail rate of the time-distribution of E (fit on E in [mean, mean + 3 sd]) vs 2/(rho log u),
# and the real zero of F_X.  Usage: python3 s8_mech.py RHO X
import heapq, math, sys, time
import numpy as np
rho = eval(sys.argv[1]); X = float(sys.argv[2]); t0 = time.time()
val = [1.0]; lpf = [-1]; primes = []; cursor = []; heap = []
N = 1; mind = 1.0; mindx = 0.0
def advance(i):
    c = cursor[i] + 1
    while lpf[c] > i: c += 1
    cursor[i] = c
    heapq.heappush(heap, (primes[i] * val[c], i))
while True:
    xstar = 1.0 + (N - 0.5) / rho
    if heap and heap[0][0] <= xstar:
        x, i = heapq.heappop(heap)
        if x > X: break
        if (xstar - x) / x < mind: mind = (xstar - x) / x; mindx = x
        N += 1; val.append(x); lpf.append(i); advance(i)
    else:
        x = xstar
        if x > X: break
        N += 1; primes.append(x); val.append(x); lpf.append(len(primes) - 1); cursor.append(0); advance(len(primes) - 1)
v = np.array(val); P = np.array(primes)
print(f"S8 rho={rho:.10f} X={X:g} N={len(v)} pi={len(P)} time={time.time()-t0:.1f}s  ordering margin (min rel. dist. composite->live threshold) = {mind:.3e} at {mindx:.6g}")
# E on [v_j, v_{j+1}): E(u) = j + rho - rho*u  (j = index, N = j+1).  Right end value of piece j: E(v_{j+1}-) = j + rho - rho*v_{j+1}
j = np.arange(len(v), dtype=np.float64); a = np.append(v[1:], X)
Eleft = j + rho - rho * v          # value just after event j (right-continuous)
Eright = j + rho - rho * a         # value just before the next event
gaps = np.diff(P); gend = P[1:]
print("  window-top x   supE    maxgap G  rho*G-1/2   meanE(time)  rho*log(x)/2   tail-rate   2/(rho log x)   supE/log^2")
xs = []; x = 10 ** 2.5
while x <= X * 1.0000001: xs.append(x); x *= 10 ** 0.5
for xt in xs:
    lo = xt / 10 ** 0.5
    m = (v >= lo) & (v < xt)
    if m.sum() < 50: continue
    supE = Eleft[v < xt].max()
    G = gaps[gend <= xt].max() if (gend <= xt).any() else float('nan')
    # time-average of E over [lo, xt): integral of linear pieces
    vv = v[m]; aa = np.minimum(a[m], xt); e0 = Eleft[m]; e1 = j[m] + rho - rho * aa
    L = aa - vv; meanE = float(((e0 + e1) * 0.5 * L).sum() / L.sum())
    # time-distribution tail: fraction of time with E > h, h on a grid; fit log-fraction slope on [meanE, meanE + 3 sd]
    sd = math.sqrt(max(float((((e0 ** 2 + e0 * e1 + e1 ** 2) / 3.0) * L).sum() / L.sum()) - meanE ** 2, 1e-12))
    hs = np.linspace(meanE, meanE + 3 * sd, 13); fr = []
    for h in hs:
        # time with E > h on a linear decreasing piece from e0 to e1 (e0 >= e1)
        tpart = np.clip((e0 - h) / np.maximum(e0 - e1, 1e-300), 0.0, 1.0) * L
        fr.append(tpart.sum() / L.sum())
    fr = np.array(fr); ok = fr > 0
    rate = -np.polyfit(hs[ok], np.log(fr[ok]), 1)[0] if ok.sum() > 3 else float('nan')
    lx = math.log(xt)
    print(f" {xt:12.4g} {supE:7.2f} {G:9.2f} {rho*G-0.5:9.2f}   {meanE:9.3f}   {rho*lx/2:9.3f}    {rate:8.4f}    {2/(rho*lx):8.4f}    {supE/lx**2:7.4f}")
lv = np.log(v); EX = len(v) - 1.0 - rho * (X - 1.0)
def FX(s): return math.fsum(np.exp(-s * lv).tolist()) + rho * X ** (1 - s) / (s - 1) - EX * X ** (-s)
lo, hi = 0.05, 0.9999
if FX(lo) > 0 and FX(hi) < 0:
    for _ in range(45):
        mid = 0.5 * (lo + hi)
        if FX(mid) > 0: lo = mid
        else: hi = mid
    s = 0.5 * (lo + hi)
    print(f"real zero of F_X: sigma* = {s:.6f}   (1 - 2rho = {1-2*rho:.4f};  template zero 1 - rho = {1-rho:.4f})")
else: print("no sign change of F_X on [0.05, 0.9999]")
