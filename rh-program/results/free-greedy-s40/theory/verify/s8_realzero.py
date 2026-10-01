# theory unit, free-greedy-s40 (Session 40). S8(rho) with DRIFT-FREE prime positions p = 1 + (N(p-) - 1/2)/rho (the exact lattice
# formula of Lemma 1.2), recording sup E / min E per half-decade, then F_X(sigma) on the real axis and its real zero (bisection).
# F_X(s) = sum_{n<=X} n^-s + rho X^{1-s}/(s-1) - E(X) X^-s ;  zeta_P(sigma) = F_X(sigma) + sigma*int_X^oo E u^{-sigma-1} du, and the
# tail is > -X^{-sigma}/2 by Lemma 1.1 (E > -1/2).  Theorem 1.6 bound: zeta_P(sigma) > 1/2 - rho/(1 - sigma).
# Usage: python3 s8_realzero.py RHO X
import heapq, math, sys, time
import numpy as np
rho = eval(sys.argv[1]); X = float(sys.argv[2]); t0 = time.time()
val = [1.0]; lpf = [-1]; primes = []; cursor = []; heap = []
N = 1; supE = 0.0; minE = 0.0; recs = []; nextdec = 10.0
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
        Eleft = N - 1.0 - rho * (x - 1.0)
        if Eleft < minE: minE = Eleft
        N += 1; val.append(x); lpf.append(i); advance(i)
    else:
        x = xstar
        if x > X: break
        N += 1; primes.append(x); val.append(x); lpf.append(len(primes) - 1); cursor.append(0); advance(len(primes) - 1)
    E = N - 1.0 - rho * (x - 1.0)
    if E > supE: supE = E
    if x >= nextdec:
        recs.append((nextdec, N, len(primes), supE, minE)); nextdec *= 10 ** 0.5
EX = N - 1.0 - rho * (X - 1.0)
print(f"S8 rho={rho:.10f} X={X:g} N={N} pi={len(primes)} E(X)={EX:.3f} time={time.time()-t0:.1f}s  (1-2rho = {1-2*rho:.4f})")
print("      x         N      pi    supE   minE(left limits)   supE/log^2x")
for r in recs:
    print(f" {r[0]:9.3g} {r[1]:9d} {r[2]:7d} {r[3]:7.2f} {r[4]:8.4f}  {r[3]/math.log(r[0])**2:8.4f}")
v = np.array(val); lv = np.log(v)
def FX(s):
    return math.fsum(np.exp(-s * lv).tolist()) + rho * X ** (1 - s) / (s - 1) - EX * X ** (-s)
print(" sigma    F_X(sigma)   F_X - X^-s/2   1/2 - rho/(1-s)")
for s in [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 0.97, 0.99]:
    f = FX(s); print(f" {s:.2f}  {f:12.6f}  {f - 0.5 * X ** (-s):12.6f}  {0.5 - rho / (1 - s):10.4f}")
lo, hi = 0.3, 0.999
if FX(lo) > 0 and FX(hi) < 0:
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        if FX(mid) > 0: lo = mid
        else: hi = mid
    print(f"real zero of F_X: sigma* = {0.5*(lo+hi):.6f}")
else:
    print("no sign change of F_X on [0.3, 0.999]")
