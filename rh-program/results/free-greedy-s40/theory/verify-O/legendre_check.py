# Opus reader: NOTE 3.4 checks for S8(pi/16), independent small generator (Python floats; margins at this size ~1e-8).
# (1) Legendre's identity pi(I) = sum_{d | P(sqrt b)} mu(d) #(G cap I/d) on several I = (a, b], a >= sqrt b (exact integers).
# (2) M_lat(z) z^rho (claimed -> 1.0127) and M(z) log z against the Diamond-Zhang Thm 5.10 limit e^-gamma / rho.
import math, bisect
rho = math.pi / 16; t = 1 / rho; X = 2.0e5
P = []; G = [1.0]; N = 1; thr = 1 + 0.5 * t; LO = 1.0
p1 = 1 + t / 2
def walk(i0, prod, depth, HI, out):
    for i in range(i0, len(P)):
        q = prod * P[i]
        if q > HI: break
        if depth >= 1 and q > LO: out.append(q)
        walk(i, q, depth + 1, HI, out)
while LO < X:
    HI = min(LO * p1 * (1 - 1e-12), X); out = []; walk(0, 1.0, 0, HI, out); out.sort()
    for c in out:
        while thr < c: P.append(thr); G.append(thr); N += 1; thr = 1 + (N - 0.5) * t
        G.append(c); N += 1; thr = 1 + (N - 0.5) * t
    while thr <= HI: P.append(thr); G.append(thr); N += 1; thr = 1 + (N - 0.5) * t
    LO = HI
G.sort(); print(f"S8(pi/16) to {X:g}: N = {len(G)}, pi = {len(P)}  (s8dd: N(1e5) = 19637, pi(1e5) = 8415; here N(1e5) = {bisect.bisect_right(G, 1e5)}, pi(1e5) = {bisect.bisect_right(P, 1e5)})")
def cnt(lo, hi): return bisect.bisect_right(G, hi) - bisect.bisect_right(G, lo)
def legendre(a, b):
    ps = [p for p in P if p <= math.sqrt(b)]; total = 0
    def rec(i, d, mu):
        nonlocal total
        total += mu * cnt(a / d, b / d)
        for j in range(i, len(ps)):
            if d * ps[j] > b: break           # larger d: I/d lies below 1, count 0
            rec(j + 1, d * ps[j], -mu)
    rec(0, 1.0, 1); return total, bisect.bisect_right(P, b) - bisect.bisect_right(P, a)
for a, b in [(1000, 1200), (5000, 5200), (20000, 20200), (50000, 50500), (90000, 100000), (100000, 200000)]:
    L, pi_I = legendre(a, b); print(f"Legendre I=({a},{b}]: sum = {L}, pi(I) = {pi_I}, equal = {L == pi_I}")
g = 0.5772156649015329
for z in [1e2, 1e3, 1e4, 1e5]:
    Mlat = 1.0; k = 1
    while 1 + (k - 0.5) * t <= z: Mlat *= 1 - 1 / (1 + (k - 0.5) * t); k += 1
    M = math.prod(1 - 1 / p for p in P if p <= z)
    print(f"z = {z:g}: M_lat z^rho = {Mlat * z**rho:.5f}   M(z) log z = {M * math.log(z):.4f}   (limit e^-gamma/rho = {math.exp(-g) / rho:.4f})")
