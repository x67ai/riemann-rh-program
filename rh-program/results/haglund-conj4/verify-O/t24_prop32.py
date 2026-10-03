# verify-O 2.4: the picture of Proposition 3.2 at the first positive lobe (gamma_2, gamma_3) and the one-critical-point fact.
from core import *
mp.mp.dps = 25
gs = [mp.zetazero(n).imag for n in range(1, 62)]
# one critical point per lobe: count sign changes of Xi' on a fine grid in each of the first 60 lobes
bad = 0
for j in range(60):
    a, b = gs[j], gs[j+1]
    N = 400
    vals = [mp.diff(lambda x: Xi(x).real, a + (b-a)*(i+0.5)/N) for i in range(N)]
    ch = sum(1 for i in range(N-1) if vals[i]*vals[i+1] < 0)
    if ch != 1: bad += 1; print("lobe", j+1, "sign changes of Xi':", ch)
print("lobes 1..60 between consecutive zeros (gamma_1..gamma_61 up to %s): lobes with != 1 critical point: %d" % (mp.nstr(gs[60], 6), bad))
# the curve C_1 over (gamma_2, gamma_3): Xi(x+iy) > 0
g2, g3 = gs[1], gs[2]
xs = mp.findroot(lambda x: mp.diff(lambda t: Xi(t).real, x), (g2+g3)/2)
M1 = Xi(xs).real
print("lobe (%s, %s): critical point %s, M_1 = %s" % (mp.nstr(g2, 10), mp.nstr(g3, 10), mp.nstr(xs, 12), mp.nstr(M1, 12)))
x = xs
for y in ('0.001', '0.01', '0.1', '0.3', '1', '2', '4', '8', '16', '32'):
    y = mp.mpf(y)
    x = mp.findroot(lambda x: Xi(mp.mpc(x, y)).imag, x)
    v = Xi(mp.mpc(x, y))
    # continuous argument along the horizontal line from iy to x+iy, by summing small phase steps
    steps = 4000; arg = mp.mpf(0); prev = Xi(mp.mpc(0, y))
    for i in range(1, steps+1):
        cur = Xi(mp.mpc(x*i/steps, y)); arg += mp.arg(cur/prev); prev = cur
    print("y=%6s  x_1(y)=%s  Xi=%s  arg/(2pi)=%s" % (mp.nstr(y, 3), mp.nstr(x, 12), mp.nstr(v.real, 12), mp.nstr(arg/(2*PI), 8)), flush=True)
