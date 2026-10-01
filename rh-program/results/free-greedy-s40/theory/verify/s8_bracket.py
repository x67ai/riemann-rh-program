# theory unit (Session 40): real-zero brackets and an ordering-safety check for the double-precision S8(rho) run.
# Ordering safety: the deficit process only sees counts at threshold times x* = 1 + (N - 1/2)/rho, so the computed run is S8(rho')
# (rho' = the double nearest the intended rho) whenever no composite lies within the rounding error of the threshold that is live
# when it arrives.  We report min over composites n of |n - x*_live| / n (x*_live = 1 + (N(n-) - 1/2)/rho), to compare with ~1e-14.
# Usage: python3 s8_bracket.py RHO X s1 s2 ...
import heapq, math, sys
import numpy as np
rho = eval(sys.argv[1]); X = float(sys.argv[2]); sig = [float(a) for a in sys.argv[3:]]
val = [1.0]; lpf = [-1]; primes = []; cursor = []; heap = []; N = 1; mind = 1.0; mindx = 0.0
def advance(i):
    c = cursor[i] + 1
    while lpf[c] > i: c += 1
    cursor[i] = c; heapq.heappush(heap, (primes[i] * val[c], i))
while True:
    xstar = 1.0 + (N - 0.5) / rho
    if heap and heap[0][0] <= xstar:
        x, i = heapq.heappop(heap)
        if x > X: break
        d = (xstar - x) / x
        if d < mind: mind = d; mindx = x
        N += 1; val.append(x); lpf.append(i); advance(i)
    else:
        x = xstar
        if x > X: break
        N += 1; primes.append(x); val.append(x); lpf.append(len(primes) - 1); cursor.append(0); advance(len(primes) - 1)
lv = np.log(np.array(val)); EX = N - 1.0 - rho * (X - 1.0)
print(f"rho={rho:.12f} X={X:g} N={N} pi={len(primes)} E(X)={EX:.4f}  min rel. distance composite->live threshold = {mind:.3e} at x={mindx:.6g}")
for s in sig:
    F = math.fsum(np.exp(-s * lv).tolist()) + rho * X ** (1 - s) / (s - 1) - EX * X ** (-s)
    L = math.log(X); I2 = X ** (-s) * (L * L / s + 2 * L / s ** 2 + 2 / s ** 3)
    print(f"  sigma={s:.4f}  F_X={F:+.8f}  floor X^-s/2={0.5*X**(-s):.2e}  tail per unit K (E<=K log^2 u): s*I2={s*I2:.4e}  K_max={abs(F)/(s*I2):.3f}")
