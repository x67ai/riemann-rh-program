# verify-O 2.4: the picture of Proposition 3.2 at the first positive lobe (gamma_2, gamma_3) and the one-critical-point fact.
from core import *
mp.mp.dps = 15
gs = [mp.zetazero(n).imag for n in range(1, 32)]
# one critical point per lobe: count sign changes of Xi' on a fine grid in each of the first 60 lobes
bad = 0
for j in range(30):
    a, b = gs[j], gs[j+1]
    N = 120
    vals = [mp.diff(lambda x: Xi(x).real, a + (b-a)*(i+0.5)/N) for i in range(N)]
    ch = sum(1 for i in range(N-1) if vals[i]*vals[i+1] < 0)
    if ch != 1: bad += 1; print("lobe", j+1, "sign changes of Xi':", ch)
print("lobes 1..30 between consecutive zeros (gamma_1..gamma_31 up to %s): lobes with != 1 critical point: %d" % (mp.nstr(gs[30], 6), bad))
# the curve C_1 over (gamma_2, gamma_3): Xi(x+iy) > 0
g2, g3 = gs[1], gs[2]
dXi = lambda t: mp.diff(lambda u: Xi(u).real, t)
xs = mp.findroot(dXi, (g2 + mp.mpf('0.001'), g3 - mp.mpf('0.001')), solver='illinois')
M1 = Xi(xs).real
print("lobe (%s, %s): critical point %s, M_1 = %s" % (mp.nstr(g2, 10), mp.nstr(g3, 10), mp.nstr(xs, 12), mp.nstr(M1, 12)))
show = [mp.mpf(v) for v in ('0.001', '0.01', '0.1', '0.3', '1', '2', '4', '8', '16', '32')]
ys = sorted(set([mp.mpf('0.001')*mp.mpf('1.15')**j for j in range(0, 74)] + show))
ys = [y for y in ys if y <= 32]
x = xs; prevval = M1
for y in ys:
    x = mp.findroot(lambda x: Xi(mp.mpc(x, y)).imag, x)
    v = Xi(mp.mpc(x, y)).real
    mono = v > prevval; prevval = v
    if y in show:
        arg = mp.nan
        if y >= mp.mpf('0.3'):
            steps = 2500; arg = mp.mpf(0); prev = Xi(mp.mpc(0, y))
            for i in range(1, steps+1):
                cur = Xi(mp.mpc(x*i/steps, y)); arg += mp.arg(cur/prev); prev = cur
        print("y=%6s  x_1(y)=%s  Xi=%s  increasing-so-far=%s  arg/(2pi)=%s" % (mp.nstr(y, 3), mp.nstr(x, 12), mp.nstr(v, 12), mono, mp.nstr(arg/(2*PI), 8)), flush=True)
