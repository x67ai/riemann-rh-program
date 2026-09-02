# INDICATIVE tail quantities for row 2 (heuristic float64/numpy) -- NOT a certificate.
import numpy as np, math
t0 = 0.186; y0 = 0.16733; yA = 0.7924646
def sigma_lb(N, y):   # (21) at x = x_N = 4pi(N^2 - t/16): Re s* >= (1+y)/2 + t/4 log(x/4pi) - t/(2x^2)(...)_+
    x = 4*math.pi*(N*N - t0/16)
    return (1+y)/2 + t0/4*math.log(x/(4*math.pi)) - t0/(2*x*x)*max(1-3*y+4*y*(1+y)/x**2, 0)
def gamma_ub(N, y):   # (20) at x = x_N
    x = 4*math.pi*(N*N - t0/16)
    return math.exp(0.02*y)*(x/(4*math.pi))**(-y/2)
def kappa_ub(N, y):
    x = 4*math.pi*(N*N - t0/16); return t0*y/(2*(x-6))
def sums(N, y):
    n = np.arange(1, N+1, dtype=np.float64); ln = np.log(n)
    b = np.exp(t0/4*ln*ln)
    s = sigma_lb(N, y); k = kappa_ub(N, y); g = gamma_ub(N, y)
    A = np.sum(b*np.exp(-s*ln))                     # sum b_n / n^sigma  (n=1 term = 1)
    B = g*np.sum(b*np.exp((y - s + k)*ln))          # |gamma| sum n^y b_n / n^{sigma-|kappa|}
    return s, g, A, B
for N in [630783, 1500000, 3000000, 6000000]:
    for y in [y0, yA]:
        s,g,A,B = sums(N,y)
        print(f"N={N:8d} y={y:.7f} sigma_lb={s:.5f} |gamma|<={g:.4e} A={A:.4f} B={B:.4e} 2-A-B={2-A-B:.4f}")
