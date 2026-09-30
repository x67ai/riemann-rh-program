# Orchestrator's independent spot-check of Prop. 1.1(b) (conj-O-s38 NOTE): the corrected reflected diagonal
#   Sigma |class|^2 = rho^2 zeta(2-2s) Prod_{p in R} (1 + p^{-2s}(1 - p^{2s-2})(1-1/p)^{-2}),  0 < s < 1/2,
# against the brief's sketch (no factor (1 - p^{2s-2})), and against the NOTE's printed numbers for R = {2}, s = 0.2:
#   sum 6.92914577326 = corrected product 6.92914577326 != sketch 9.21491143894.
# The ratio sketch/corrected is normalization-free, so it tests the factor without knowing the NOTE's overall normalization.
from mpmath import mp, zeta, mpf
mp.dps = 30
s = mpf('0.2'); R = [2]
def bracket(with_factor):
    b = mpf(1)
    for p in R:
        f = (1 - mpf(p)**(2*s-2)) if with_factor else 1
        b *= 1 + mpf(p)**(-2*s) * f * (1 - mpf(1)/p)**(-2)
    return b
rho = mpf(1)
for p in R: rho *= (1 - mpf(1)/p)
corr = rho**2 * zeta(2-2*s) * bracket(True)
sketch = rho**2 * zeta(2-2*s) * bracket(False)
print("zeta(1.6) =", zeta(mpf('1.6')))
print("corrected (my normalization) =", corr, "  x4 =", 4*corr)
print("sketch    (my normalization) =", sketch, " x4 =", 4*sketch)
print("ratio sketch/corrected (mine)   =", sketch/corr)
print("ratio sketch/corrected (NOTE)   =", mpf('9.21491143894')/mpf('6.92914577326'))
# brute force of the additive form (a) for finite R over one period Q: (1/Q) int E^2 = rho 2^{|R|}/12 in rationals
from fractions import Fraction
def E_meansq(R):
    Q = 1
    for p in R: Q *= p
    rho = Fraction(1)
    for p in R: rho *= Fraction(p-1, p)
    # E(x) = N_P(x) - rho x on [0,Q); N_P counts n<=x coprime to all p in R. Piecewise linear between integers.
    coprime = [n for n in range(1, Q+1) if all(n % p for p in R)]
    tot = Fraction(0)
    N = 0
    for k in range(Q):
        # on [k, k+1): N_P(x) = N (count of coprime n <= k), E = N - rho x
        a = Fraction(N) ; 
        # int_k^{k+1} (a - rho x)^2 dx = a^2 - a rho (2k+1) + rho^2 ((k+1)^3 - k^3)/3
        tot += a*a - a*rho*(2*k+1) + rho*rho*Fraction((k+1)**3 - k**3, 3)
        if (k+1) in coprime: N += 1
    return tot / Q, rho * Fraction(2**len(R), 12)
for R in ([2], [2,3], [3,5], [2,3,5,7]):
    lhs, rhs = E_meansq(R)
    print("R =", R, " (1/Q) int E^2 =", lhs, " rho 2^|R|/12 =", rhs, " equal:", lhs == rhs)
