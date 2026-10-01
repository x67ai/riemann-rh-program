# theory unit, free-greedy-s40 (Session 40). Checks the Section-1 lemmas of theory/NOTE.md on the S8(rho) system and evaluates
# F_X(sigma) on the REAL axis.  Generator = the orchestrator's proto/s8_proto.py core (same event order, same tie rule).
# Checks: (b) prime gaps >= 1/rho; lattice p = 1 + (N(p-) - 1/2)/rho; (a) E > -1/2 after every event, E(x-) >= -1/2 before it;
# (d) pi(x) = floor(M(x) + 1/2), M = running sup of V = rho(x-1) - C(x) (sup includes left limits), and E - (M - V) in (-1/2, 1/2];
# (e) F_X(s) = zeta_c(s) + s*int_1^X E(u) u^{-s-1} du exactly, F_X(s) = sum_{n<=X} n^-s + rho X^{1-s}/(s-1) - E(X) X^-s.
# Usage: python3 s8_check.py RHO X
import heapq, math, sys, time
import numpy as np
rho = eval(sys.argv[1]) if len(sys.argv) > 1 else math.pi / 4
X = float(sys.argv[2]) if len(sys.argv) > 2 else 1e6
t0 = time.time()
val = [1.0]; lpf = [-1]; primes = []; cursor = []; heap = []
N = 1; x0 = 1.0; D0 = 0.0
C = 0; P = 0; M = 0.0                      # composites, primes, running sup of V
bad_refl = 0; bad_E = 0; bad_gap = 0; bad_latt = 0; maxdev = 0.0; ties = 0
lastp = None
def advance(i):
    c = cursor[i] + 1
    while lpf[c] > i: c += 1
    cursor[i] = c
    heapq.heappush(heap, (primes[i] * val[c], i))
while True:
    xstar = x0 + (0.5 - D0) / rho
    if heap and heap[0][0] <= xstar:
        x, i = heapq.heappop(heap)
        if x > X: break
        if x == xstar: ties += 1
        Vleft = rho * (x - 1.0) - C          # V(x-)
        if Vleft > M: M = Vleft
        Dbefore = D0 + rho * (x - x0)
        if Dbefore > 0.5 + 1e-9: bad_E += 1  # E(x-) >= -1/2 violated
        D0 = Dbefore - 1.0; x0 = x; N += 1; C += 1
        val.append(x); lpf.append(i); advance(i)
    else:
        x = xstar
        if x > X: break
        Vleft = rho * (x - 1.0) - C
        if Vleft > M: M = Vleft
        if lastp is not None and x - lastp < 1.0 / rho - 1e-9: bad_gap += 1
        if abs(x - (1.0 + (N - 0.5) / rho)) > 1e-9 * x: bad_latt += 1   # N = N(p-) here
        lastp = x
        D0 = -0.5; x0 = x; N += 1; P += 1
        primes.append(x); val.append(x); lpf.append(len(primes) - 1); cursor.append(0)
        advance(len(primes) - 1)
    V = rho * (x - 1.0) - C
    E = -D0
    if E <= -0.5 - 1e-9: bad_E += 1
    if not (-1e-6 <= M - (P - 0.5) < 1.0 - 1e-6): bad_refl += 1   # pi = floor(M + 1/2) with M = pi - 1/2 at primes
    dev = E - (M - V)
    if not (-0.5 + 1e-6 < dev <= 0.5 + 1e-6): bad_refl += 1
    maxdev = max(maxdev, abs(E - P + V))   # identity E = pi - V (exact by N = 1 + pi + C)
EX = (N - (rho * (X - 1.0) + 1.0))
print(f"S8 rho={rho:.12f} X={X:g} N={N} pi={P} C={C} time={time.time()-t0:.1f}s ties={ties}")
print(f"violations: E>-1/2 {bad_E}  reflection {bad_refl}  gap>=1/rho {bad_gap}  lattice {bad_latt}  max|E-(pi-V)| {maxdev:.2e}")
v = np.array(val); v.sort()
print(f"E(X) = {EX:.4f}")
print(" sigma      F_X(sigma)      zeta_c+s*int_1^X E      diff      F_X - X^-s/2")
# exact integral of E on each gap: on [v_j, v_{j+1}) E(u) = (j+1) - 1 - rho(u-1) = j + rho - rho*u   (N = j+1 there)
j = np.arange(len(v), dtype=np.float64)
a = np.append(v[1:], X)
for s in [0.30, 0.40, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95]:
    FX = math.fsum((v ** (-s)).tolist()) + rho * X ** (1 - s) / (s - 1) - EX * X ** (-s)
    c0 = j + rho                          # E(u) = c0 - rho*u on [v_j, a_j)
    I = c0 * (v ** (-s) - a ** (-s)) / s - rho * (a ** (1 - s) - v ** (1 - s)) / (1 - s)
    zc = (s - 1 + rho) / (s - 1)
    G = zc + s * math.fsum(I.tolist())
    print(f" {s:.2f}  {FX:16.8f}  {G:16.8f}  {FX-G:10.2e}  {FX - 0.5*X**(-s):14.8f}")
