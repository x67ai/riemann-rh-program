# verify-O 2.1: Phi_n by Haglund's incomplete-gamma form vs the kernel integral, complex z; and Xi = sum Phi_n.
from core import *
pts = [0, 7, mp.mpc(20.6253, 2.6971), mp.mpc(3, -4), mp.mpc(45, 10), mp.mpc(-12, 30)]
for n in (1, 2, 3, 4):
    for z in pts:
        a, b = Phi_G(n, z), Phi_K(n, z)
        print("n=%d z=%s  PhiG=%s  rel.diff=%s" % (n, mp.nstr(z, 8), mp.nstr(a, 15), mp.nstr(abs(a-b)/abs(a), 3)))
for z in pts[:5]:
    s6 = XiN(6, z); x = Xi(z)
    print("Xi vs Xi_6 at z=%s: Xi=%s  |diff|=%s" % (mp.nstr(z, 8), mp.nstr(x, 15), mp.nstr(abs(x - s6), 3)))
