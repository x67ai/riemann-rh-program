"""audit_F_constants.py -- AUDIT F: independent checks of two constants the mp leg certifies
or quotes.

(1) C_30 = sup_{[0,1]} |B_30(x) - B_30| (zeta_encl.c_sup(30)): the certified upper bound must
    dominate a dense high-precision sampling of the exact polynomial (a LOWER bound on the
    sup), and the ratio C_30/|B_30| should be ~2 (the classical fact |B_n(x)| <= 2|B_n|... wait:
    the classical bound is |B_{2k}(x)| <= |B_{2k}|, so |B_n(x) - B_n| <= 2|B_n|; the certified
    constant must therefore satisfy lb <= C_30^ub and C_30^ub is expected ~<= 2.03|B_30|).
(2) kappa = (sqrt(10 - 2 sqrt 5) - 2)/(sqrt 5 - 1) = tan(theta) with e^{2 i theta} =
    tau(chi)/(i sqrt5), chi mod 5, chi(2) = i (the dh.py definition FORMAT.md sec. 9.2 quotes):
    recomputed here from the Gauss sum directly at dps 60, and the DH combination
    (1-i kap)/2 L(s,chi) + (1+i kap)/2 L(s,chi-bar) is checked against the producer formula
    5^{-s}[zeta(s,1/5) + kap zeta(s,2/5) - kap zeta(s,3/5) - zeta(s,4/5)] at random s.
    Both producer kappa enclosures (mp kappa_iv, arb _kappa) must contain the dps-60 value.
"""
import random
from fractions import Fraction
from mpmath import mp, iv
from zeta_encl import c_sup, bern_exact, bernoulli_poly_coeffs
from ball import ivmpf_bounds, set_prec, mpf_tuple_to_fraction as m2f
import producer_mp, producer_arb
from flint import ctx

mp.dps = 60
# (1) C_30
ub, lb = c_sup(30)
coeffs = list(bernoulli_poly_coeffs(30)); coeffs[0] -= bern_exact(30)
best = mp.mpf(0)
N = 20000
for j in range(N + 1):
    x = mp.mpf(j) / N
    acc = mp.mpf(0)
    for c in reversed(coeffs):
        acc = acc * x + mp.mpf(c.numerator) / c.denominator
    best = max(best, abs(acc))
# refine around the max with golden-section-free local search: use findroot on derivative
d1 = [Fraction(k) * coeffs[k] for k in range(1, 31)]
def P(x):
    acc = mp.mpf(0)
    for c in reversed(coeffs):
        acc = acc * x + mp.mpf(c.numerator) / c.denominator
    return acc
def dP(x):
    acc = mp.mpf(0)
    for c in reversed(d1):
        acc = acc * x + mp.mpf(c.numerator) / c.denominator
    return acc
# candidate maxima: x = 1/2 (B_30(1/2) - B_30 = (2^{1-30}-1)B_30 - B_30 = -(2 - 2^{-29}) B_30)
x_half = mp.mpf(1) / 2
print("C_30 certified upper bound = %s, code's lower bound = %s" % (mp.nstr(mp.mpf(ub.numerator) / ub.denominator, 12), mp.nstr(mp.mpf(lb.numerator) / lb.denominator, 12)))
print("dense sampling (20001 pts) sup lower bound = %s; |P(1/2)| = %s; 2|B_30|(1 - 2^-30) = %s"
      % (mp.nstr(best, 12), mp.nstr(abs(P(x_half)), 12), mp.nstr(2 * abs(mp.mpf(bern_exact(30).numerator) / bern_exact(30).denominator) * (1 - mp.mpf(2) ** -30), 12)))
print("ub >= sampled sup: %s ; ub/|B_30| = %s ; endpoint check P(0) = %s" % (mp.mpf(ub.numerator) / ub.denominator >= best, mp.nstr(mp.mpf(ub.numerator)/ub.denominator / abs(mp.mpf(bern_exact(30).numerator)/bern_exact(30).denominator), 8), P(0)))

# (2) kappa from the Gauss sum
chi = {1: 1, 2: 1j, 3: -1j, 4: -1}   # chi(2)=i, chi(3)=chi(2)^3=-i, chi(4)=chi(2)^2=-1
tau = sum(mp.mpc(chi[a]) * mp.exp(2j * mp.pi * a / 5) for a in chi)
eps = tau / (1j * mp.sqrt(5))
theta = mp.arg(eps) / 2
kap_theta = mp.tan(theta)
kap_formula = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
print("|eps_chi| = %s (must be 1); theta = %s; tan(theta) = %s; formula kappa = %s; |diff| = %s"
      % (mp.nstr(abs(eps), 20), mp.nstr(theta, 20), mp.nstr(kap_theta, 30), mp.nstr(kap_formula, 30), mp.nstr(abs(kap_theta - kap_formula), 5)))
# note: theta is defined mod pi (e^{2i theta}); tan is pi-periodic, so the check is well posed.
# combination identity at random s
rng = random.Random(3)
maxdiff = mp.mpf(0)
for _ in range(10):
    s = mp.mpc(rng.uniform(0.3, 1.5), rng.uniform(-100, 100))
    L = mp.power(5, -s) * sum(mp.mpc(chi[a]) * mp.zeta(s, mp.mpf(a) / 5) for a in chi)
    Lbar = mp.power(5, -s) * sum(mp.conj(mp.mpc(chi[a])) * mp.zeta(s, mp.mpf(a) / 5) for a in chi)
    f_std = (1 - 1j * kap_formula) / 2 * L + (1 + 1j * kap_formula) / 2 * Lbar
    f_prod = mp.power(5, -s) * (mp.zeta(s, mp.mpf(1) / 5) + kap_formula * mp.zeta(s, mp.mpf(2) / 5) - kap_formula * mp.zeta(s, mp.mpf(3) / 5) - mp.zeta(s, mp.mpf(4) / 5))
    maxdiff = max(maxdiff, abs(f_std - f_prod))
print("max |DH standard combination - producer formula| over 10 random s: %s" % mp.nstr(maxdiff, 5))
# producer kappa enclosures contain the dps-60 value
set_prec(288); ctx.prec = 300
kf = m2f(kap_formula._mpf_)
lo, hi = ivmpf_bounds(producer_mp.kappa_iv())
alo, ahi = producer_arb.ball_interval(producer_arb._kappa())
print("mp kappa_iv encloses: %s (width %.2e); arb _kappa encloses: %s (width %.2e)" % (lo <= kf <= hi, float(hi - lo), alo <= kf <= ahi, float(ahi - alo)))
