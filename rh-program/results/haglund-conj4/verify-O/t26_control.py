# verify-O 2.6 (target (h)): k = 1, the real-axis quotient S_lam(x) = (Xi_2(x) + lam)/Phi_2(x) on [0.5, 45], step 0.005.
# Route L: Xi_2 = Phi_1 + Phi_2 by Haglund's (10),(14) (real x: the two incomplete-gamma terms are conjugate).
# Route T (check at the refined extrema): Xi_2 = Xi - Phi_3 - Phi_4 - Phi_5 with Xi from zeta.
# Reports every local extremum of S_lam with value in (0, 1), refined by findroot on S' (numerical derivative).
import sys
from core import *
mp.mp.dps = 25

def Gr(w, a, b):  # real w: G = 2 Re Gamma(b+iw,a)/a^(b+iw)
    p = b + 1j*w
    return 2*(mp.gammainc(p, a)/mp.power(a, p)).real

def Phr(n, x):
    X = PI*n*n; w = mp.mpf(x)/2
    return 2*PI**2*n**4*Gr(w, X, mp.mpf(9)/4) - 3*PI*n*n*Gr(w, X, mp.mpf(5)/4)

def XiT2(x):
    return Xi(x).real - Phr(3, x) - Phr(4, x) - Phr(5, x)

h = mp.mpf('0.005'); xs = [mp.mpf('0.5') + j*h for j in range(int((45-0.5)/0.005) + 1)]
P1 = []; P2 = []
for x in xs:
    P1.append(Phr(1, x)); P2.append(Phr(2, x))
with open('t26_grid.txt', 'w') as f:
    for x, a, b in zip(xs, P1, P2):
        f.write("%s %s %s\n" % (mp.nstr(x, 8), mp.nstr(a, 22), mp.nstr(b, 22)))
print("grid done:", len(xs), "points", flush=True)

for lam in (mp.mpf(0), mp.mpf('5e-5'), mp.mpf('1e-4')):
    S = [(a + b + lam)/b for a, b in zip(P1, P2)]
    found = 0
    for j in range(1, len(xs) - 1):
        if (S[j] - S[j-1])*(S[j+1] - S[j]) < 0:
            kind = 'max' if S[j] > S[j-1] else 'min'
            if not (0 < S[j] < 1):
                continue
            Sf = lambda x: (Phr(1, x) + Phr(2, x) + lam)/Phr(2, x)
            xr = mp.findroot(lambda x: mp.diff(Sf, x), xs[j])
            vL = Sf(xr); vT = (XiT2(xr) + lam)/Phr(2, xr)
            found += 1
            print("lam=%s %s x=%s  S(route L)=%s  S(route T)=%s  rel.diff=%s  S''=%s" % (
                mp.nstr(lam, 3), kind, mp.nstr(xr, 10), mp.nstr(vL, 12), mp.nstr(vT, 12),
                mp.nstr(abs(vL - vT)/abs(vL), 3), mp.nstr(mp.diff(Sf, xr, 2), 4)), flush=True)
    print("lam=%s: %d extrema with value in (0,1)" % (mp.nstr(lam, 3), found), flush=True)
