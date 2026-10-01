# theory unit (Session 40): exploratory Newton refinement of a zero of F_X (grid start in a box), at several X.  NOT a certificate.
# Usage: python3 s8_newton.py RHO sig0 sig1 t0 t1 X1 X2 ...
import heapq, math, sys
import numpy as np
rho = eval(sys.argv[1]); a, b, c, d = map(float, sys.argv[2:6]); Xs = [float(v) for v in sys.argv[6:]]
Xmax = max(Xs)
val = [1.0]; lpf = [-1]; primes = []; cursor = []; heap = []; N = 1
def advance(i):
    k = cursor[i] + 1
    while lpf[k] > i: k += 1
    cursor[i] = k; heapq.heappush(heap, (primes[i] * val[k], i))
while True:
    xs = 1.0 + (N - 0.5) / rho
    if heap and heap[0][0] <= xs:
        x, i = heapq.heappop(heap)
        if x > Xmax: break
        N += 1; val.append(x); lpf.append(i); advance(i)
    else:
        x = xs
        if x > Xmax: break
        N += 1; primes.append(x); val.append(x); lpf.append(len(primes) - 1); cursor.append(0); advance(len(primes) - 1)
V = np.array(val)
for X in Xs:
    lv = np.log(V[V <= X]); EX = lv.size - 1.0 - rho * (X - 1.0); LX = math.log(X)
    F = lambda s: complex(np.exp(-s * lv).sum() + rho * math.e ** ((1 - s) * LX) / (s - 1) - EX * math.e ** (-s * LX))
    if X == Xs[0]:
        best = min(((abs(F(complex(sg, tt))), complex(sg, tt)) for sg in np.linspace(a, b, 14) for tt in np.linspace(c, d, 60)), key=lambda z: z[0])
        z = best[1]
    for _ in range(40):
        h = 1e-6; fz = F(z); dz = (F(z + h) - F(z - h)) / (2 * h); step = fz / dz; z -= step
        if abs(step) < 1e-12: break
    print(f"rho={rho:.8f} X={X:g}: zero of F_X at {z.real:.6f} + {z.imag:.6f}i   |F_X|={abs(F(z)):.1e}")
