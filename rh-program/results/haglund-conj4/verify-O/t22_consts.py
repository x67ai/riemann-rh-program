# verify-O 2.2: sign at 0, c_1, the 1/x^2 limits, alpha_n, c(t); Lemma 4.1's Phi_n(0) bounds.
from core import *
X0 = Xi(0).real; P1 = Phi_G(1, 0).real
print("Xi(0) =", mp.nstr(X0, 20), " Q_1(0) = Xi(0)-Phi_1(0) =", mp.nstr(X0 - P1, 15))
c1 = mp.nsum(lambda n: (4*PI*n*n - 1)*mp.exp(-PI*n*n), [2, mp.inf])
print("c_1 =", mp.nstr(c1, 20), "  Xi_1(0) - (0.4971 - c_1) =", mp.nstr(P1 - (mp.mpf('0.4971') - c1), 6))
alpha = lambda n: (8*(PI*n*n)**3 - 30*(PI*n*n)**2 + 15*PI*n*n)*mp.exp(-PI*n*n)
# phit'(0) by numerical differentiation vs -alpha_n
for n in (1, 2, 3):
    d = mp.diff(lambda v: phit(n, v), 0)
    print("n=%d  phit'(0)=%s  -alpha_n=%s" % (n, mp.nstr(d, 15), mp.nstr(-alpha(n), 15)))
for N in (1, 2, 3, 4, 5):
    lim = -2*mp.fsum(alpha(n) for n in range(N+1, N+12))
    print("N=%d lim x^2 Xi_N = %s" % (N, mp.nstr(lim, 8)))
# x^2 Xi_1(x) at a large x vs the limit: direct check of the integration by parts
for x in (200, 800):
    print("x=%d  x^2*Xi_1(x) = %s" % (x, mp.nstr(x*x*(Xi(x) - mp.fsum(Phi_G(n, x) for n in range(2, 6))).real, 10)))
for k in (1, 2, 3):
    for t in (0, mp.mpf('0.5'), 1):
        u = 1 - t
        c = -2*(u*alpha(k+1) + mp.fsum(alpha(n) for n in range(k+2, k+14)))
        print("k=%d t=%s c(t)=%s" % (k, mp.nstr(t, 2), mp.nstr(c, 10)))
for n in range(2, 8):
    X = PI*n*n; h = Phi_G(n, 0).real/2
    lo, hi = (2*X-1)*mp.exp(-X), (2*X+3)*mp.exp(-X)
    print("n=%d (2X-1)e^-X <= Phi_n(0)/2 <= (2X+3)e^-X : %s  ratios lo/h=%s hi/h=%s" % (n, lo <= h <= hi, mp.nstr(lo/h, 8), mp.nstr(hi/h, 8)))
for k in range(1, 8):
    print("k=%d 4(k+2)^2=%d 2pi(k+1)^2=%s holds=%s" % (k, 4*(k+2)**2, mp.nstr(2*PI*(k+1)**2, 6), 4*(k+2)**2 < 2*PI*(k+1)**2))
