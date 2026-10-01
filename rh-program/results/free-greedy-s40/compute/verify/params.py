# params.py NAME -> prints "RHO_HI RHO_LO T_HI T_LO" (double-double split of rho and t = 1/rho, from 50-digit mpmath)
import sys
from mpmath import mp, mpf, pi, e, sqrt
mp.dps = 50
R = {
    "pi4": pi / 4,                      # transcendental 1/rho
    "pi16": pi / 16,                    # rho < 1/4: the theory unit's real-zero regime (Thm 1.6)
    "pi32": pi / 32,
    "eoverpi": e / pi,
    "rsqrt2": 1 / sqrt(2),              # 1/rho = sqrt 2, algebraic of degree 2
    "r0995": mpf("0.95") * pi / 3,
    "r098": mpf("0.6") * sqrt(2) * pi / e,
    "r08": mpf(4) / 5,                  # rational control: lattice (10k + 3)/8
    "one": mpf(1),                      # rational-prime control (sieve mode)
}
def split(v):
    hi = float(v)
    lo = float(v - mpf(hi))
    return hi, lo
r = R[sys.argv[1]]
rh, rl = split(r)
th, tl = split(1 / r)
print(repr(rh), repr(rl), repr(th), repr(tl))
