# read-O: exact mean squares of E_L for the lattice control (piecewise-linear E_L, closed-form piece integrals), rho = pi/16.
# (1) 2*pi*int_1^X E_L^2 u^{-2 sigma - 1} du, X = 1e5, sigma = 0.3, 0.45  (NOTE 3.3: 0.6875, 0.3955)
# (2) block mean squares (1/U) int_U^{2U} E_L^2 (NOTE 3.2: 0.083395, 0.083349, 0.083333, 0.083333)
# (3) sigma -> 0+: sigma * int_1^inf E_L^2 u^{-2 sigma - 1} du  vs 1/24 (sharp) and 1/(48 log 2) (NOTE l. 160)
from mpmath import mp, mpf, pi, log
mp.dps = 30
rho = pi/16
def ell(k): return 1 + (k - mpf(1)/2)/rho
def pieces(X):                          # (a, b, alpha): on [a, b), E_L(u) = alpha - rho*u
    out = [(mpf(1), min(ell(1), X), rho)]           # E = -rho(u - 1) = rho - rho*u
    k = 1
    while ell(k) < X:
        a, b = ell(k), min(ell(k + 1), X)
        out.append((a, b, mpf(1)/2 + rho*a)); k += 1
    return out
def F(u, alpha, p):                      # antiderivative of (alpha - rho u)^2 u^{-p}
    return alpha**2*u**(1 - p)/(1 - p) - 2*alpha*rho*u**(2 - p)/(2 - p) + rho**2*u**(3 - p)/(3 - p)
def wint(X, sigma):
    p = 2*sigma + 1
    return sum(F(b, al, p) - F(a, al, p) for a, b, al in pieces(X))
def block(U):
    tot = mpf(0)
    for a, b, al in pieces(2*U):
        a2, b2 = max(a, U), b
        if b2 > a2: tot += ((al - rho*a2)**3 - (al - rho*b2)**3)/(3*rho)
    return tot/U
for s in (mpf('0.3'), mpf('0.45')):
    print(f"2*pi*int_1^1e5 E_L^2 u^(-2s-1), s={s}: {mp.nstr(2*pi*wint(mpf(10)**5, s), 6)}", flush=True)
for U in (mpf(10)**3, mpf(10)**4, mpf(10)**5, mpf('4.9e5')):
    print(f"block mean square U={mp.nstr(U, 3)}: {mp.nstr(block(U), 8)}", flush=True)
X = mpf(10)**6
base = {}
for s in (mpf('0.05'), mpf('0.02'), mpf('0.01'), mpf('0.005')):
    v = wint(X, s) + (mpf(1)/12)*X**(-2*s)/(2*s)      # tail: E_L^2 has mean 1/12 over each period (error O(X^{-2s-1}))
    print(f"sigma={s}: sigma*int = {mp.nstr(s*v, 8)}   (1/24 = {mp.nstr(mpf(1)/24, 8)}, 1/(48 log 2) = {mp.nstr(1/(48*log(2)), 8)})", flush=True)
