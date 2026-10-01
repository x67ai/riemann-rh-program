# read-O independent check of the lattice control L_rho(s) = 1 + rho^s * zeta(s, 1/2 + rho)  (Hurwitz)
# Written from the NOTE's definitions only. mpmath, 40 digits.
from mpmath import mp, mpf, pi, zeta, findroot, floor, nsum, inf, log, exp, quad
mp.dps = 30

def ell(k, rho):            # lattice point 1 + (k - 1/2)/rho
    return 1 + (k - mpf(1)/2)/rho

def L(s, rho):
    return 1 + rho**s * zeta(s, mpf(1)/2 + rho)

def L_direct(s, rho, K=3000):  # 1 + sum_{k<=K} ell_k^{-s} + Euler-Maclaurin tail (independent of Hurwitz)
    S = mpf(0)
    for k in range(1, K+1): S += ell(k, rho)**(-s)
    f  = lambda x: (1 + (x - mpf(1)/2)/rho)**(-s)
    fp = lambda x: -s/rho*(1 + (x - mpf(1)/2)/rho)**(-s-1)
    f3 = lambda x: -s*(s+1)*(s+2)/rho**3*(1 + (x - mpf(1)/2)/rho)**(-s-3)
    tail = rho*f(K)**((s-1)/s)/(s-1) if False else rho*(1 + (K - mpf(1)/2)/rho)**(1-s)/(s-1)
    tail += -f(K)/2 - fp(K)/12 + f3(K)/720
    return 1 + S + tail

def N_L(x, rho):            # 1 + #{k >= 1 : ell_k <= x}, counted from the atoms themselves
    # ell_k <= x  <=>  k <= rho(x-1) + 1/2 ; count by explicit loop over k for small x (independent of the floor formula)
    c = 1; k = 1
    while ell(k, rho) <= x:
        c += 1; k += 1
    return c

def E_L(x, rho):
    return N_L(x, rho) - rho*(x - 1) - 1

out = []
for name, rho in [("pi/64", pi/64), ("pi/32", pi/32), ("pi/16", pi/16), ("pi/8", pi/8)]:
    # 1. Dirichlet series = Hurwitz form
    d1 = abs(L(3, rho) - L_direct(3, rho)); d2 = abs(L(mpf('2.5'), rho) - L_direct(mpf('2.5'), rho))
    # 2. real zero in (1-2rho, 1)
    lo, hi = 1 - 2*rho, mpf(1) - mpf(10)**-12
    sstar = findroot(lambda s: L(s, rho), (lo + mpf(10)**-9, hi), solver='illinois')
    # sign check at the bracket ends
    sg = (L(lo + mpf(10)**-6, rho) > 0, L(mpf(1) - mpf(10)**-6, rho) < 0)
    # 3. Theorem 1.6 floor L(sigma) >= 1/2 - rho/(1-sigma) on a grid in (0,1)
    floor_ok = all(L(mpf(j)/200, rho) >= mpf(1)/2 - rho/(1 - mpf(j)/200) for j in range(1, 200))
    # 4. first-order value s0 + rho*L(s0), s0 = 1 - rho;  L(0) = 1 - rho
    s0 = 1 - rho
    fo = s0 + rho*L(s0, rho)
    L0 = L(mpf(0), rho)
    # 5. sigma_1: rho^s zeta(s, 1/2+rho) = 1  (absolute abscissa of log L)
    s1 = findroot(lambda s: rho**s*zeta(s, mpf(1)/2 + rho) - 1, (1 + mpf(10)**-9, mpf(3)), solver='illinois')
    print(f"{name}: |L-direct|(3)={mp.nstr(d1,3)} (2.5)={mp.nstr(d2,3)}  sigma*_L={mp.nstr(sstar,15)}  "
               f"signs(+ at 1-2rho, - at 1-)={sg}  Thm1.6floor_ok={floor_ok}  s0+rhoL(s0)={mp.nstr(fo,8)}  "
               f"L(0)={mp.nstr(L0,10)} (1-rho={mp.nstr(1-rho,10)})  sigma_1={mp.nstr(s1,12)}", flush=True)

# 6. E_L range near atoms and at random points (rho = pi/16)
rho = pi/16
import random
random.seed(1)
vals = []
for k in range(1, 400):
    a = ell(k, rho)
    for x in (a - mpf(10)**-20, a, a + mpf(10)**-20):
        if x >= 1: vals.append(E_L(x, rho))
for _ in range(1500):
    x = 1 + mpf(random.random())*200
    vals.append(E_L(x, rho))
out.append(f"E_L over {len(vals)} points (atoms +-1e-20 and random x in [1,201]): min={mp.nstr(min(vals),25)} max={mp.nstr(max(vals),25)}")
out.append("E_L at atoms ell_k exactly: " + str(sorted(set(mp.nstr(E_L(ell(k, rho), rho), 20) for k in range(1, 50)))))
out.append("E_L just below atoms: " + str(sorted(set(mp.nstr(E_L(ell(k, rho) - mpf(10)**-25, rho), 20) for k in range(1, 50)))))
for line in out: print(line)
