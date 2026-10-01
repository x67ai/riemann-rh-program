# print double-double constants (hi lo as %a hex floats) for t = 1/rho and rho, rho = pi/D
import sys
from mpmath import mp, mpf, pi
mp.dps = 60
D = int(sys.argv[1])
rho = pi / D
t = 1 / rho
def split(x):
    hi = float(x); lo = float(x - mpf(hi)); return hi, lo
th, tl = split(t); rh, rl = split(rho)
print(th.hex(), tl.hex(), rh.hex(), rl.hex())
