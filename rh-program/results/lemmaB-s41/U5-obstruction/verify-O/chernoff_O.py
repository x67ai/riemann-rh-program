# read-O: why a scan cannot see the zeros of L right of 1 (heuristic size, rigorous inequality for the random model).
# By Kronecker-Weyl (log ell_k independent), for sigma > 1 the distribution of X(sigma+it) over t is that of
# S = sum_k a_k e^{i theta_k}, theta_k iid uniform, a_k = ell_k^{-sigma}. A zero needs X = -1, so Re S <= -1.
# Chernoff: P(Re S <= -1) <= inf_lam e^{-lam} prod_k I0(lam a_k); tail k > K bounded by log I0(x) <= x^2/4.
from mpmath import mp, mpf, pi, besseli, log, zeta, exp
mp.dps = 20
rho = pi/16
def ell(k): return 1 + (k - mpf(1)/2)/rho
K = 20000
for sigma in (mpf('1.02'), mpf('1.05'), mpf('1.10')):
    a = [ell(k)**(-sigma) for k in range(1, K + 1)]
    tail2 = rho**(2*sigma)*zeta(2*sigma, mpf(1)/2 + rho) - sum(x*x for x in a)    # sum_{k>K} a_k^2
    best = None
    for lam in [mpf(2)**(j/4) for j in range(0, 60)]:
        lg = -lam + sum(log(besseli(0, lam*x)) for x in a) + lam**2*tail2/4
        if best is None or lg < best[0]: best = (lg, lam)
    print(f"sigma={sigma}: X(sigma)={mp.nstr(rho**sigma*zeta(sigma, mpf(1)/2+rho), 6)}  "
          f"P(Re X(sigma+it) <= -1) <= exp({mp.nstr(best[0], 6)}) = 10^{mp.nstr(best[0]/log(10), 4)}  (lambda={mp.nstr(best[1], 4)})", flush=True)
