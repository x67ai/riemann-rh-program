"""Checker-written: on the Prop. 4.5 family (vacancy lattice n = 32 + one pair of real mark mu at the hole, depth d), is (MI) F1 >= T
ever violated?  F1 - T = [2(mu-1)(mu-2)] + [2mu^2 A^2 - 4mu(a^2 - 1)], a = abar(d), A = abar(2d) (prop45 + T = 60 + 6mu)."""
import math
def abar(x): return sum(math.cosh(2*math.pi*j*x/64) for j in range(-32, 33))/65
best = (1e9, None)
for i in range(1, 401):
    d = i*0.0025                      # d in (0, 1]
    a, A = abar(d), abar(2*d)
    for k in range(1, 601):
        mu = k*0.005                  # mu in (0, 3]
        v = 2*(mu-1)*(mu-2) + 2*mu*mu*A*A - 4*mu*(a*a-1)
        if v < best[0]: best = (v, (d, mu))
print("min over d in (0,1], mu in (0,3] of F1 - T on the Prop. 4.5 family: %.6f at (d, mu) = %s" % (best[0], best[1]))
a, A = abar(0.25), abar(0.5); mu = 0.05
print("anchor: F1 - S2 = %.7f, F1 - T = %.7f" % (2*mu*mu*A*A - 4*mu*(a*a-1), 2*(mu-1)*(mu-2) + 2*mu*mu*A*A - 4*mu*(a*a-1)))
