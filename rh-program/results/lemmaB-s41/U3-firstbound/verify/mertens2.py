# U3-firstbound §1.9 check: sum_{p<=x} 1/p - log log x, S(x) - log x, and the constants of the lower bound, for S8(rho).
# Event loop as in t1_check.py (copied from orch-verify/s8_meansq.py).
import heapq, math, sys
rho = eval(sys.argv[1]); X = float(sys.argv[2])
val = [1.0]; lpf = [-1]; ppw = [-2]; primes = []; cursor = []; heap = []; N = 1
def advance(i):
    c = cursor[i] + 1
    while lpf[c] > i: c += 1
    cursor[i] = c; heapq.heappush(heap, (primes[i] * val[c], i, c))
inv = 0.0; S = 0.0; marks = [10.0 ** k for k in range(2, 9)]; mi = 0; out = []
while True:
    xstar = 1.0 + (N - 0.5) / rho
    if heap and heap[0][0] <= xstar: x, i, c = heapq.heappop(heap); comp = True
    else: x = xstar; comp = False
    while mi < len(marks) and marks[mi] < x:
        m = marks[mi]; out.append((m, inv - math.log(math.log(m)), S - math.log(m))); mi += 1
    if x > X: break
    N += 1
    if comp:
        isp = i if ppw[c] == i else -1; val.append(x); lpf.append(i); ppw.append(isp); advance(i)
    else:
        isp = len(primes); primes.append(x); val.append(x); lpf.append(isp); ppw.append(isp); cursor.append(0); advance(isp)
        inv += 1.0 / x
    if isp >= 0: S += math.log(primes[isp]) / x
T2 = sum(1.0 / (p * (p - 1.0)) for p in primes)
print(f"S8 rho={rho:.12f} X={X:g} primes={len(primes)}; T2 = sum 1/(p(p-1)) over g-primes <= X = {T2:.5f}")
print("x        sum_{p<=x}1/p - loglog x    S(x) - log x")
for m, a, b in out: print(f"1e{round(math.log10(m))}     {a:+.5f}                  {b:+.5f}")
print(f"proved lower bound for sum 1/p - loglog x (as x -> oo): log rho - T2 - 0.59 = {math.log(rho) - T2 - 0.59:+.4f}")
