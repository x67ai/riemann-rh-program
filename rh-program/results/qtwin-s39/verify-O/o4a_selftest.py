# self-tests of the core against hand values (exact arithmetic where possible)
from tprobe_core import *
from fractions import Fraction as Fr
P = TProbe(4, [Fr(3, 2)], 64)
t, w = 2.0414, 0.24985
Pi = P.Pi(t, [w])
def at(x): return Pi[P.idx[Fr(x)]]
print("q=4, B={3/2}: |G<=64| =", P.n)
print("Pi(2) =", at(2), " expected 1 + t =", 1 + t)
print("Pi(4) =", at(4), " expected 1/2 + 2 - t^2/2 + 0 =", 0.5 + 2 - t*t/2)
print("Pi(16/3) =", at(Fr(16, 3)), " expected -4wt/3 =", -4*w*t/3)
print("Pi(3/2) =", at(Fr(3, 2)), " expected w;  Pi(8/3) =", at(Fr(8, 3)), " expected 4w/3 =", 4*w/3)
# zeta(s)(1 + q^{1/2-s}) at q = 2 is not square; use q = 4, D = 1 + 2*4^{-s}: Pi(4^k) = 1/(2k) + (-1)^{k+1} 2^k / k
P0 = TProbe(4, [], 256, include_sqrtq=False)
Pi0 = P0.Pi(0.0, [])
for k in range(1, 5):
    x = Fr(4**k); print("D = 1 + 2*4^-s: Pi(4^%d) = %.6f, expected %.6f" % (k, Pi0[P0.idx[x]], 1/(2*k) + (-1)**(k+1) * 2**k / k))
