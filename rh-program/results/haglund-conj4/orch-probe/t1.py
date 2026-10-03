import time, cmath
from c4probe import *
ctx.prec = 160
# ladder: Haglund's appendix zero of Xi_1 (p. 16) -> S_0? check Xi_1 vanishes; and S_1 = Xi_2/Phi_2 equals 1 there
z0 = acb("20.62534600592171760132974", "2.697151842339519632505712")
print("Xi_1(z0) route L:", XiN_L(1, z0).str(8))
a, b = pair_T(1, z0); print("S_1(z0) route T:", (a / b).str(20))
a, b = pair_L(1, z0); print("S_1(z0) route L:", (a / b).str(20))
# speed
t = time.time()
for i in range(50): cS(1, complex(30 + 0.1 * i, 3.0))
print("50 evals k=1 route T: %.3fs" % (time.time() - t))
t = time.time()
for i in range(20): cS(27, complex(3140 + 0.1 * i, 3.0))
print("20 evals k=27 route T: %.3fs" % (time.time() - t))
t = time.time()
for i in range(20): cS(10, complex(900 + 0.1 * i, 60.0))
print("20 evals k=10 far (x=900,y=60) route T: %.3fs" % (time.time() - t))
print("route cross-check k=3 at 70+5i:", cS(3, 70 + 5j, "T"), cS(3, 70 + 5j, "L"))
print("route cross-check k=3 at 150+20i:", cS(3, 150 + 20j, "T"), cS(3, 150 + 20j, "L"))
