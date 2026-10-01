# U3-firstbound: explicit constant of Theorem T1 (and §1.6 for threshold tau), from a finite run to X0.
# Usage: python3 t1_const.py RHO X0 [TAU]. Event loop as in t1_check.py (orch-verify/s8_meansq.py), prime at 1 + (N - 1 + tau)/rho.
import heapq, math, sys, time
rho = eval(sys.argv[1]); X0 = float(sys.argv[2]); tau = eval(sys.argv[3]) if len(sys.argv) > 3 else 0.5
r0 = 1.0 - rho - tau; kap = rho / (1.0 - tau)
t0 = time.time()
val = [1.0]; lpf = [-1]; ppw = [-2]; primes = []; cursor = []; heap = []
N = 1; x0 = 1.0; psi = 0.0; S = 0.0; Pt = 0.0; supEu = 0.0; argsup = 1.0; minE = 0.0; supE1 = -1.0; arg1 = 1.0
def advance(i):
    c = cursor[i] + 1
    while lpf[c] > i: c += 1
    cursor[i] = c
    heapq.heappush(heap, (primes[i] * val[c], i, c))
while True:
    xstar = 1.0 + (N - 1.0 + tau) / rho
    if heap and heap[0][0] <= xstar:
        x, i, c = heapq.heappop(heap); comp = True
    else:
        x = xstar; comp = False
    if x > X0: break
    Eleft = N - rho * (x - 1.0) - 1.0
    if Eleft < minE: minE = Eleft
    Pt += psi * (1.0 / x0 - 1.0 / x); N += 1; x0 = x
    if comp:
        isp = i if ppw[c] == i else -1
        val.append(x); lpf.append(i); ppw.append(isp); advance(i)
    else:
        isp = len(primes); primes.append(x); val.append(x); lpf.append(isp); ppw.append(isp); cursor.append(0); advance(isp)
    if isp >= 0:
        lp = math.log(primes[isp]); psi += lp; S += lp / x
    E = N - rho * (x - 1.0) - 1.0
    if E / x > supEu: supEu = E / x; argsup = x
    if E / (x - 1.0) > supE1: supE1 = E / (x - 1.0); arg1 = x
Pt += psi * (1.0 / x0 - 1.0 / X0)
P0 = primes[-1]; lX = math.log(X0)
D_X0 = lX - 1.0 - Pt
eta = (math.log(P0) + rho) / P0
# T(P0) = sum over g-primes p, j >= 2, p^j > P0 of log p / p^j: known primes exactly, primes > X0 bounded by the lattice
T = 0.0; lP = math.log(P0)
for p in primes:
    j0 = max(2, int(math.floor(lP / math.log(p))) + 1)
    while p ** (j0 - 1) > P0 and j0 > 2: j0 -= 1
    while p ** j0 <= P0: j0 += 1
    T += math.log(p) * p ** (-j0) / (1.0 - 1.0 / p)
a = X0 - 1.0 / rho        # lattice tail: sum_{x_k > X0} f(x_k) <= rho * int_a^inf log u/(u(u-1)) du <= rho (log a + 1)/(a - 1)
Ttail = rho * (math.log(a) + 1.0) / (a - 1.0)
eps0 = eta + (1.0 - tau) * (T + Ttail)
D0 = min(D_X0, (1.0 - tau) / rho - eps0 / rho)
Delta0 = (r0 * D0 - eps0) / (1.0 - tau)
Alarge = rho * tau / r0 + (1.0 - rho) * eps0 / (r0 * Delta0)
CE = max(supEu, Alarge)
print(f"S8 rho={rho:.12f} tau={tau} X0={X0:g}: N={N} primes={len(primes)} time={time.time()-t0:.1f}s; min E(x-) = {minE:.6f} (> -tau)")
print(f"sup_(u<=X0) E(u)/u = {supEu:.6f} at u = {argsup:.6f}   (1/(2 p1) = {0.5/(1+tau/rho):.6f} for tau = 1/2 only)")
print(f"P0 = {P0:.4f}; eta(P0) = {eta:.3e}; T(P0) known = {T:.3e}, lattice tail = {Ttail:.3e}; eps0 = {eps0:.4e}")
print(f"D(X0) = {D_X0:.5f} vs (1-tau)/rho = {(1-tau)/rho:.5f}; D0 = {D0:.5f}; Delta0 = {Delta0:.5f}")
print(f"record bound beyond X0: rho tau/r0 = {rho*tau/r0:.6f} + {(1-rho)*eps0/(r0*Delta0):.3e} = {Alarge:.6f}")
print(f"THEOREM T1 constant: E(x) <= {CE:.6f} x for all x >= 1; N(x) <= {rho+CE:.6f} x + {1-rho:.4f}")
# Theorem T1' (comparison u - 1): records of E(u)/(u-1) beyond X0 are <= u/D - rho <= rho tau/(1-tau) + eps0/((1-tau) D0)
D0p = min(D_X0, (1.0 - tau) / rho - eps0 / rho)
A1 = rho * tau / (1.0 - tau) + eps0 / ((1.0 - tau) * D0p)
C1 = max(supE1, A1)
print(f"T1': sup_(1<u<=X0) E(u)/(u-1) = {supE1:.6f} at u = {arg1:.6f}; records beyond X0 <= {A1:.6f}")
print(f"THEOREM T1' constant: E(x) <= {C1:.6f} (x - 1) for all x > 1; N(x) <= {rho + C1:.6f} (x - 1) + 1")
