# verify-O 2.5: test Lemma 4.1, |Phi_n(z)/Phi_n(0) - 1| <= 3.1 R^2/(pi^2 n^4) for |z| <= R, pi n^2 >= R + 1/2.
# By the maximum principle the sup over the disc is attained on |z| = R; sample 721 points of the circle
# (even and real-symmetric: a quarter circle suffices; 1-degree steps. Exact fact: |Phi(z)-Phi(0)| <= Phi(iR)-Phi(0) on |z|=R,
# since |cos(zv)-1| <= cosh(Rv)-1 with equality at z = iR, so the sup sits at arg = 90 deg.)
from core import *
mp.mp.dps = 25
rows = []
for n in (2, 3, 4, 5, 6):
    X = PI*n*n
    Rmax = X - mp.mpf('0.5')
    for frac in (mp.mpf('0.1'), mp.mpf('0.25'), mp.mpf('0.5'), mp.mpf('0.75'), 1):
        R = frac*Rmax
        P0 = Phi_G(n, 0).real
        worst = mp.mpf(0); wth = 0
        M = 90
        for j in range(M+1):
            th = (PI/2)*j/M
            z = R*mp.expj(th)
            v = abs(Phi_G(n, z)/P0 - 1)
            if v > worst: worst, wth = v, th
        bound = mp.mpf('3.1')*R**2/(PI**2*n**4)
        print("n=%d R=%8s  sup|Phi/Phi(0)-1|=%s at arg=%s deg   bound=%s   ratio=%s  ok=%s" % (
            n, mp.nstr(R, 6), mp.nstr(worst, 6), mp.nstr(wth*180/PI, 4), mp.nstr(bound, 6), mp.nstr(worst/bound, 4), worst <= bound), flush=True)
