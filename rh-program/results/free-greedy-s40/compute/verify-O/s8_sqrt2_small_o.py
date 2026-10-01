# s8_sqrt2_small_o.py -- S8(rho = 1/sqrt2) to x = 7000 in EXACT Z[sqrt2] arithmetic (values (a + b sqrt2)/2^e as
# exact pairs; comparisons by sign of a + b sqrt2). Lists the g-primes' lattice indices and every multiplicity. Opus reader.
from fractions import Fraction as Q
import heapq, math
def sgn(a, b):          # sign of a + b*sqrt2, a, b rationals
    if a >= 0 and b >= 0: return (a > 0 or b > 0) - 0
    if a <= 0 and b <= 0: return -1 if (a < 0 or b < 0) else 0
    c = a * a - 2 * b * b                     # a and b of opposite signs
    return (1 if c > 0 else -1 if c < 0 else 0) * (1 if a > 0 else -1)
class V:
    __slots__ = ('a', 'b')
    def __init__(s, a, b): s.a, s.b = Q(a), Q(b)
    def __mul__(s, o): return V(s.a * o.a + 2 * s.b * o.b, s.a * o.b + s.b * o.a)
    def __lt__(s, o): return sgn(s.a - o.a, s.b - o.b) < 0
    def __eq__(s, o): return s.a == o.a and s.b == o.b
    def f(s): return float(s.a) + float(s.b) * math.sqrt(2)
XMAX = 7000.0
L = lambda k: V(1, Q(2 * k - 1, 2))         # 1 + (k - 1/2) sqrt2
G = []                                        # finalized g-integers > 1: (value, multiset of prime indices)
primes = []; prime_k = []; heap = []; seenvals = {}; mult = []
cnt = 1
def push(v, ms):
    if v.f() <= XMAX: heapq.heappush(heap, (v, ms))
while True:
    Lk = L(cnt)
    if heap and not (Lk < heap[0][0]):        # composite first on a tie
        v, ms = heapq.heappop(heap); key = (v.a, v.b)
        if key in seenvals: mult.append((round(v.f(), 6), seenvals[key], ms))
        else: seenvals[key] = ms
        G.append((v, ms)); cnt += 1
        for j in range(max(ms), len(primes)): push(v * primes[j], ms + (j,))
        continue
    if Lk.f() > XMAX: break
    pi = len(primes); primes.append(Lk); prime_k.append(cnt); cnt += 1
    for (n, ms) in G: push(n * Lk, ms + (pi,))
    push(Lk * Lk, (pi, pi)); G.append((Lk, (pi,)))
print("S8(1/sqrt2) exact to x =", XMAX, ": N =", cnt, " g-primes:", len(primes))
print("lattice indices of the first 30 g-primes:", prime_k[:30])
for k in (4, 6, 20, 23, 51): print(f"L_{k} = {L(k).f():.6f} is a g-prime: {k in prime_k}")
print("multiplicities (value, multiset 1, multiset 2; prime indices):", mult[:8], "count", len(mult))
