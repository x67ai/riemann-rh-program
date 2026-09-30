"""k1_xi_lowzeros.py -- the zeta facts Theorem K uses, computed:
N(T) = number of zeros rho = beta + i gamma with 0 < gamma <= T (counted in the whole critical strip,
mpmath.nzeros uses the Riemann-Siegel/Gram-block count with Backlund/Turing-type verification) and
the first two ordinates (on the line).  Also the zero-free rectangle check by the argument principle for
xi on the box 0 < sigma < 1, 0 < t < 14.1 (no zeros), and the extended box to t < 21.0 (exactly one)."""
import mpmath as mp
mp.mp.dps = 30
print('nzeros(14.1) =', mp.nzeros(14.1), '  nzeros(14.2) =', mp.nzeros(14.2), '  nzeros(21.0) =', mp.nzeros(21.0), '  nzeros(21.1) =', mp.nzeros(21.1))
print('zetazero(1) =', mp.zetazero(1)); print('zetazero(2) =', mp.zetazero(2))
xi = lambda s: mp.mpf(1)/2*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def box_count(t1, t2, s1=-0.5, s2=1.5, n=4000):
    pts = []
    for k in range(n): pts.append(mp.mpc(s1 + (s2-s1)*k/n, t1))
    for k in range(n): pts.append(mp.mpc(s2, t1 + (t2-t1)*k/n))
    for k in range(n): pts.append(mp.mpc(s2 - (s2-s1)*k/n, t2))
    for k in range(n): pts.append(mp.mpc(s1, t2 - (t2-t1)*k/n))
    pts.append(pts[0]); tot = 0
    prev = xi(pts[0])
    for z in pts[1:]:
        cur = xi(z); tot += mp.arg(cur/prev); prev = cur
    return tot/(2*mp.pi)
print('argument principle for xi on [-0.5,1.5] x [0.5, 14.1]  :', mp.nstr(box_count(0.5, 14.1), 8))
print('argument principle for xi on [-0.5,1.5] x [0.5, 21.0]  :', mp.nstr(box_count(0.5, 21.0), 8))
print('argument principle for xi on [-0.5,1.5] x [-14.1, 14.1] (full central box):', mp.nstr(box_count(-14.1, 14.1, n=6000), 8))
