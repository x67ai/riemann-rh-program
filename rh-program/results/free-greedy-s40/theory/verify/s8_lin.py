# theory unit (Session 40): first-order displacement of the template zero.  zeta_c(s) = (s-1+rho)/(s-1) has zeta_c'(1-rho) = -1/rho,
# so the zero of zeta_P = zeta_c + s*Ehat sits near sigma_lin = (1 - rho) + rho*zeta_P(1 - rho), zeta_P(1-rho) ~ F_X(1-rho).
# Also R(u) = N(u) - rho*u >= r0 := inf R, and the Remark-1.6' floor r0/(r0 + rho).  Usage: python3 s8_lin.py X rho1 rho2 ...
import heapq, math, sys
import numpy as np
X = float(sys.argv[1])
for rs in sys.argv[2:]:
    rho = eval(rs); val = [1.0]; lpf = [-1]; primes = []; cursor = []; heap = []; N = 1; Rmin = 1.0 - rho
    def advance(i):
        c = cursor[i] + 1
        while lpf[c] > i: c += 1
        cursor[i] = c; heapq.heappush(heap, (primes[i] * val[c], i))
    while True:
        xstar = 1.0 + (N - 0.5) / rho
        if heap and heap[0][0] <= xstar:
            x, i = heapq.heappop(heap)
            if x > X: break
            Rmin = min(Rmin, N - rho * x); N += 1; val.append(x); lpf.append(i); advance(i)
        else:
            x = xstar
            if x > X: break
            Rmin = min(Rmin, N - rho * x); N += 1; primes.append(x); val.append(x); lpf.append(len(primes) - 1); cursor.append(0); advance(len(primes) - 1)
    lv = np.log(np.array(val)); EX = N - 1.0 - rho * (X - 1.0)
    FX = lambda s: math.fsum(np.exp(-s * lv).tolist()) + rho * X ** (1 - s) / (s - 1) - EX * X ** (-s)
    s0 = 1 - rho; f0 = FX(s0); lo, hi = 0.05, 0.9999
    for _ in range(45):
        mid = 0.5 * (lo + hi)
        if FX(mid) > 0: lo = mid
        else: hi = mid
    print(f"rho={rho:.6f}  1-rho={s0:.6f}  F_X(1-rho)={f0:+.6f}  sigma_lin={s0 + rho*f0:.6f}  sigma*={0.5*(lo+hi):.6f}  inf R={Rmin:.4f} (1/2-rho={0.5-rho:.4f})  floor r0/(r0+rho)={Rmin/(Rmin+rho):.4f}")
