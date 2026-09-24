# Reader check (Opus 5): size of |Gamma(3/4 + iu/2)| and of (5/pi)^{3/4}|Gamma| (the Xi_DH scale on the line)
# over the windows named in the V.3 rider: the record's +-30 window at t = 85.7 (36 points, 57.04 ... 112.38),
# the +-60 window, and the campaign's DH heights 114.16, 166.48, 176.70 (+-30).
from mpmath import mp, gamma, mpc, pi, exp, log10, fabs
mp.dps = 30
def scale(u):
    return (5/pi)**0.75*fabs(gamma(mpc(0.75, u/2)))
for lab, a, b in [('t=85.7 +-30 (recorded 57.04..112.38)', 57.0415, 112.377), ('t=85.7 +-60', 25.7, 145.7),
                  ('t=114.16 +-30', 84.16, 144.16), ('t=166.48 +-30', 136.48, 196.48), ('t=176.70 +-30', 146.70, 206.70)]:
    print(lab, ': |Gamma| %.2e .. %.2e ; e^{-pi u/4} %.2e .. %.2e ; (5/pi)^{3/4}|Gamma| %.2e .. %.2e' % (
        fabs(gamma(mpc(0.75, a/2))), fabs(gamma(mpc(0.75, b/2))), exp(-pi*a/4), exp(-pi*b/4), scale(a), scale(b)))
