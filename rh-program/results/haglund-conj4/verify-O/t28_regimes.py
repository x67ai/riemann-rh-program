# verify-O 2.7b: numbers inside the HEURISTIC items of NOTE §5 (II).
from core import *
mp.mp.dps = 25
for (x, y) in ((40, 1), (60, 3), (100, 5), (300, 10), (600, 20)):
    z = mp.mpc(x, y)
    L = mp.diff(Xi, z)/Xi(z)
    dy = mp.diff(lambda s: mp.log(abs(Xi(mp.mpc(x, s)))), y)
    print("x=%d y=%d  d/dy log|Xi| = %s   (1/2)log(x/2pi) = %s   (1/2)log(x/2) = %s   Xi'/Xi = %s   model -pi/4 - (i/2)log(x/2pi) = %s" % (
        x, y, mp.nstr(dy, 5), mp.nstr(mp.log(x/(2*PI))/2, 5), mp.nstr(mp.log(mp.mpf(x)/2)/2, 5), mp.nstr(L, 5),
        mp.nstr(mp.mpc(-PI/4, -mp.log(x/(2*PI))/2), 5)), flush=True)
for k in (3, 5, 8):
    a = PI*(k+1)**2
    x = (4*(k+2)**2 + 2*a)/2
    for y in (1, 3, 6, 10):
        z = mp.mpc(x, y)
        print("k=%d x=%s y=%d  arg(Phi_{k+2}/Phi_{k+1}) = %s rad" % (k, mp.nstr(x, 5), y, mp.nstr(mp.arg(Phi_G(k+2, z)/Phi_G(k+1, z)), 4)), flush=True)
