# U3-firstbound §1.8: margin of the early supremum. Largest E(u)/(u-1) over events u > p1 (p1 itself gives exactly rho).
# Event loop copied from orch-verify/s8_meansq.py (as in t1_check.py).
import heapq, math, sys
rho = eval(sys.argv[1]); X = float(sys.argv[2])
val = [1.0]; lpf = [-1]; primes = []; cursor = []; heap = []; N = 1
def advance(i):
    c = cursor[i] + 1
    while lpf[c] > i: c += 1
    cursor[i] = c; heapq.heappush(heap, (primes[i] * val[c], i))
best = (-1.0, 0.0); p1 = 1.0 + 0.5 / rho; atp1 = None
while True:
    xstar = 1.0 + (N - 0.5) / rho
    if heap and heap[0][0] <= xstar: x, i = heapq.heappop(heap); comp = True
    else: x = xstar; comp = False
    if x > X: break
    N += 1
    if comp: val.append(x); lpf.append(i); advance(i)
    else: primes.append(x); val.append(x); lpf.append(len(primes) - 1); cursor.append(0); advance(len(primes) - 1)
    r = (N - rho * (x - 1.0) - 1.0) / (x - 1.0)
    if abs(x - p1) < 1e-12: atp1 = r
    elif r > best[0]: best = (r, x)
print(f"S8 rho={rho:.12f} X={X:g}: E/(u-1) at p1 = {atp1:.15f} (rho = {rho:.15f}); largest over other events = {best[0]:.6f} at u = {best[1]:.6f}; margin below rho = {rho-best[0]:.6f}")
