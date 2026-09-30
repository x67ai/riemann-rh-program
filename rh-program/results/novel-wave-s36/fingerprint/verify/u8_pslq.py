"""
u8_pslq.py -- integer-relation searches (mpmath.pslq) on the fingerprint.
(0) sanity: recover s_1 = -4 + (pi^2 + 8G)/8 + (1/2)(zeta''/zeta - (zeta'/zeta)^2)(1/2) from its value.
(1) alpha_1..alpha_6, b_1^2, b_2^2, Verblunsky alpha_0, 1-alpha_0 against B = {1, pi, pi^2, log pi, log 2, gamma, G,
    zeta(3), zeta'(1/2)/zeta(1/2), zeta''(1/2)/zeta(1/2)}, 60 digits, coefficients <= 10^5.
(2) the same with the products/ratios suggested by the S-fraction algebra (al_1 = s_2/s_1, so test s_1*al_1 = s_2
    against B plus s_1-type terms) -- expected: relations only through the closed forms of s_m.
"""
import json, os, mpmath as mp
here = os.path.dirname(os.path.abspath(__file__)); tab = os.path.join(os.path.dirname(here), 'tables')
# The tables store 60-digit strings; PSLQ with 11 numbers at 60 digits returns SPURIOUS relations of size ~10^5
# (a first run did exactly that).  Recompute the inputs at 1200 bits with Arb and run PSLQ at 300 digits.
import sys; sys.path.insert(0, here)
from flint import arb, arb_series, ctx
import fp_core as fc
ctx.prec = 1300; ctx.cap = 30
x_ = arb_series([0, 1]); s_ = arb(1) / 2 + x_
cc = (arb(1).__truediv__(2).log() + (arb(1) / 4 - x_ * x_).log() - (s_ / 2) * arb.pi().log() + (s_ / 2).lgamma() + (-(s_.zeta())).log()).coeffs()
sm_ = [None] + [((-1) ** (m + 1)) * m * cc[2 * m] for m in range(1, 13)]
al_ = fc.sfrac_from_series([sm_[m + 1] for m in range(0, 12)], 8)
aJ_, b2_ = fc.jfrac_from_sfrac(al_)
ctx.cap = 6
w_ = arb_series([0, 1]); s1_ = 1 + w_
dd = (arb(1).__truediv__(2).log() + s1_.log() - (s1_ / 2) * arb.pi().log() + (s1_ / 2).lgamma() + (1 + w_ * s1_.zeta(deflate=True)).log()).coeffs()
lam1 = dd[1]; lam2 = 2 * (dd[1] + dd[2])
a0_ = (lam2 - 2 * lam1) / (2 * lam1)
mp.mp.dps = 330
cv = lambda v: mp.mpf(v.str(340, radius=False))
s = [None] + [cv(v) for v in sm_[1:6]]
al = [cv(v) for v in al_[:6]]
b2 = [cv(v) for v in b2_[:2]]
a0 = cv(a0_)
print('input digits (certified): al_6', fc.digits(al_[5]), ' alpha_0', fc.digits(a0_))
z = mp.zeta(mp.mpf(1) / 2); z1 = mp.zeta(mp.mpf(1) / 2, derivative=1); z2 = mp.zeta(mp.mpf(1) / 2, derivative=2)
G = mp.catalan
# NOTE: z'/z(1/2) is NOT independent: z'/z(1/2) = (pi + 2 log pi + 6 log 2 + 2 gamma)/4 (xi'(1/2) = 0; a first run
# with it in the basis returned exactly this basis relation) -- it is dropped; (z'/z)^2 and z''/z are kept.
names = ['1', 'pi', 'pi^2', 'log pi', 'log 2', 'gamma', 'G', 'zeta(3)', "z''/z(1/2)", "(z'/z)^2"]
basis = [mp.mpf(1), mp.pi, mp.pi ** 2, mp.log(mp.pi), mp.log(2), mp.euler, G, mp.zeta(3), z2 / z, (z1 / z) ** 2]
rel0 = mp.pslq(basis, maxcoeff=10 ** 5, maxsteps=10 ** 6)
print('basis self-relation (should be None):', rel0)
out = {}
mp.mp.dps = 300
# (0) sanity
rel = mp.pslq([s[1], mp.mpf(1), mp.pi ** 2, G, z2 / z, (z1 / z) ** 2], maxcoeff=10 ** 4, maxsteps=10 ** 6)
print('sanity: relation for [s_1, 1, pi^2, G, z\'\'/z, (z\'/z)^2] =', rel)
out['sanity'] = str(rel)
tests = [('al_%d' % (i + 1), al[i]) for i in range(6)] + [('b1^2', b2[0]), ('b2^2', b2[1]), ('Verblunsky alpha_0', a0), ('1 - alpha_0', 1 - a0)]
for nm, x in tests:
    rel = mp.pslq([x] + basis, maxcoeff=10 ** 8, maxsteps=10 ** 6)
    print('%-20s relation with B: %s' % (nm, rel))
    out[nm] = str(rel)
# (2) s_1 * al_1 - s_2 = 0 exactly (algebra) -- the only relations are through the s_m
rel = mp.pslq([s[1] * al[0], s[2]], maxcoeff=10, maxsteps=10 ** 4)
print('check s_1 al_1 = s_2:', rel)
json.dump(out, open(os.path.join(here, 'u8_pslq.json'), 'w'), indent=1)
