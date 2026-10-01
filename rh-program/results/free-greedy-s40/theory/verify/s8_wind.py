# theory unit (Session 40): exploratory argument-principle count of zeros of F_X (NOT a certificate) for S8(rho) at modest X.
# F_X(s) = sum_{n<=X} n^-s + rho X^{1-s}/(s-1) - E(X) X^-s.  Boundary sampled with adaptive refinement so phase steps stay < 0.5 rad.
# Usage: python3 s8_wind.py RHO X sig0 sig1 t0 t1 [sig0 sig1 t0 t1 ...]
import heapq, math, sys, cmath
import numpy as np
rho = eval(sys.argv[1]); X = float(sys.argv[2]); boxes = [tuple(map(float, sys.argv[i:i+4])) for i in range(3, len(sys.argv), 4)]
val = [1.0]; lpf = [-1]; primes = []; cursor = []; heap = []; N = 1
def advance(i):
    c = cursor[i] + 1
    while lpf[c] > i: c += 1
    cursor[i] = c; heapq.heappush(heap, (primes[i] * val[c], i))
while True:
    xs = 1.0 + (N - 0.5) / rho
    if heap and heap[0][0] <= xs:
        x, i = heapq.heappop(heap)
        if x > X: break
        N += 1; val.append(x); lpf.append(i); advance(i)
    else:
        x = xs
        if x > X: break
        N += 1; primes.append(x); val.append(x); lpf.append(len(primes) - 1); cursor.append(0); advance(len(primes) - 1)
lv = np.log(np.array(val)); EX = N - 1.0 - rho * (X - 1.0); LX = math.log(X)
def F(svec):
    svec = np.atleast_1d(np.asarray(svec, dtype=complex)); out = np.empty(svec.size, dtype=complex)
    for a in range(0, svec.size, 256):
        s = svec[a:a+256]; out[a:a+256] = np.exp(-np.outer(s, lv)).sum(axis=1) + rho * np.exp((1 - s) * LX) / (s - 1) - EX * np.exp(-s * LX)
    return out
def wind(path):
    tot = 0.0; minabs = 1e300
    for z0, z1 in zip(path[:-1], path[1:]):
        seg = np.linspace(z0, z1, max(8, int(abs(z1 - z0) / 0.02)))
        while True:
            f = F(seg); d = np.angle(f[1:] / f[:-1])
            if np.abs(d).max() < 0.5 or seg.size > 400000: break
            seg = np.linspace(z0, z1, 2 * seg.size)
        tot += d.sum(); minabs = min(minabs, np.abs(f).min())
    return tot / (2 * math.pi), minabs
print(f"S8 rho={rho:.8f} X={X:g} N={N}")
for (a, b, c, d) in boxes:
    w, m = wind([complex(a, c), complex(b, c), complex(b, d), complex(a, d), complex(a, c)])
    print(f"  box [{a}, {b}] x [{c}, {d}]: winding = {w:+.3f}   min|F_X| on boundary = {m:.4f}")
