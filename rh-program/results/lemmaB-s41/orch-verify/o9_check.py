# Check of note O9: the one-block Chebyshev identity for S8(rho) and the Mertens constant c1.
import heapq, math, sys, bisect
rho = eval(sys.argv[1]); X = float(sys.argv[2]); XX = 2 * X
val = [1.0]; lpf = [-1]; primes = []; cursor = []; heap = []; N = 1
def advance(i):
    c = cursor[i] + 1
    while lpf[c] > i: c += 1
    cursor[i] = c
    heapq.heappush(heap, (primes[i] * val[c], i))
while True:
    xstar = 1.0 + (N - 0.5) / rho
    if heap and heap[0][0] <= xstar:
        x, i = heapq.heappop(heap)
        if x > XX: break
        N += 1; val.append(x); lpf.append(i); advance(i)
    else:
        x = xstar
        if x > XX: break
        N += 1; primes.append(x); val.append(x); lpf.append(len(primes) - 1); cursor.append(0); advance(len(primes) - 1)
cnt = lambda y: bisect.bisect_right(val, y)            # N(y)
p1 = primes[0]
theta = sum(math.log(p) for p in primes if X < p <= XX)
lhs = sum(math.log(v) for v in val if X < v <= XX)
s = 0.0; mert = 0.0
for p in primes:
    if p > XX / p1: break
    pk = p
    while pk <= XX / p1:
        s += math.log(p) * (cnt(XX / pk) - cnt(X / pk)); pk *= p
for p in primes:
    if p > X: break
    pk = p
    while pk <= X:
        mert += math.log(p) / pk; pk *= p
E = lambda y: cnt(y) - rho * (y - 1.0) - 1.0
print(f"rho={rho:.6f} X={X:g}  N(2X)={cnt(XX)}  p1={p1:.4f}")
print(f"theta_P(X,2X]         = {theta:.6f}")
print(f"sum log n - sum(...)  = {lhs - s:.6f}   (difference {theta - (lhs - s):.3e})")
print(f"theta_P(X,2X]/X       = {theta / X:.6f}")
print(f"Mertens sum to X - log X = {mert - math.log(X):.6f}   (template: -1/rho = {-1/rho:.6f};  -(1 - X^-rho)/rho = {-(1 - X**-rho)/rho:.6f})")
print(f"main term X(1 + rho log(p1/2)) / X = {1 + rho * math.log(p1 / 2):.6f};  E(X) = {E(X):.3f}")
