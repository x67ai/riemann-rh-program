# Reader check (Opus 5): the w_B-weighted mean zero density Z_K/(2 int w^_B) at the seven discriminants
# quoted in the IV.18 rider (i); Z_K = B_K - P_K from (0.3_K), with a_K in closed form (D < 0).
from mpmath import mp, mpf, pi, sqrt, exp, log, psi, re, mpc, quad, inf
from sympy import factorint, primerange
mp.dps = 25
def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0
def kron(D, p):
    if p == 2:
        return 0 if D % 2 == 0 else (1 if D % 8 == 1 else -1)
    return jacobi(D, p)
def fundamental(D):
    if D % 4 == 1:
        return all(e == 1 for e in factorint(-D).values())
    if D % 4 == 0:
        m = D // 4
        return m % 4 in (2, 3) and all(e == 1 for e in factorint(-m).values())
    return False
w = lambda u: exp(-2*u*u)
what = lambda s: sqrt(pi/2)*exp(-s*s/8)
int_what = quad(what, [-inf, inf])          # = 2 pi w(0)
aK = lambda s, D: (re(psi(0, mpc(0.5, s/2))) - log(pi))/pi + log(-D)/(2*pi)
N = 5000                                    # w(log n) < e^{-144} beyond
primes = list(primerange(2, N))
for D in [-20, -10007, -1000003, -100000007, -(10**10+19), -(10**12+39), -(10**16+79)]:
    B = 2*what(0) + quad(lambda s: what(s)*aK(s, D), [-inf, 0, inf])
    P = mpf(0)
    for p in primes:
        c = kron(D, p); pk = p
        while pk < N:
            ch = c ** (1 if pk == p else int(round(log(pk)/log(p)))) if c != 0 else 0
            P += 4*log(p)*(1 + ch)*w(log(pk))/(pk + 1)
            pk *= p
    Z = B - P
    print(D, 'fundamental', fundamental(D), 'Z_K(w_B) = %.2f' % Z, 'mean Z/(2 int w^) = %.2f' % (Z/(2*int_what)), 'log|D|/4pi = %.2f' % (log(-D)/(4*pi)))
