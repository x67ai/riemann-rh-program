"""
test_conventions.py -- numerical arbitration of every convention before production runs.

T1: archimedean log-side formula vs direct spectral-side t-integral (Gaussian test fn),
    and vs the paper's (3.15) W#_R form.  Decides the correct Arch normalization.
T2: full matrix vs Weil explicit formula zero side:  c^T T c  ==  sum_rho |fhat(t_rho)|^2
    for f = V_{-1} - 2 V_0 + V_1  (C^1, so |fhat|^2 ~ t^-6, fast-converging zero sum).
T3: D'' spectrum from the ground eigenvector vs actual zeta zeros (CCM Thm 5.10 / Table).
Run:  python3 test_conventions.py
"""
import time
import mpmath as mp
import weilform as wf

mp.mp.dps = 30
OUT = []


def log(s):
    print(s, flush=True)
    OUT.append(str(s))


# ---------------------------------------------------------------- T1
def t1():
    a = mp.mpf(1)/4
    F = lambda y: mp.e**(-y*y)          # even test function
    Fhat = lambda t: mp.sqrt(mp.pi)*mp.e**(-t*t/4)
    w = lambda t: mp.re(mp.digamma(a + 1j*t/2)) - mp.log(mp.pi)

    S = mp.quad(lambda t: Fhat(t)*w(t), [-40, 0, 40])/(2*mp.pi)

    # mine
    def integrand(y):
        den = -mp.expm1(-2*y) if y != 0 else None
        if y == 0:
            return mp.mpf(0)
        return (2*mp.e**(-2*y)*F(0) - 2*mp.e**(-2*a*y)*F(y))/den
    A = (-mp.log(mp.pi) - mp.euler)*F(0) + mp.quad(integrand, [0, 1, 5, 20, 60])

    # paper (3.15):  W#_R(F) = (1/2)(log 4pi + gamma) F(0)
    #                + int_0^inf [e^{y/2}F(y) - F(0)]/(2 sinh y) dy ; pairing = 2*(-W#_R)
    def integrand2(y):
        if y == 0:
            return mp.mpf(0)
        return (mp.e**(y/2)*F(y) - F(0))/(2*mp.sinh(y))
    WR = mp.mpf('0.5')*(mp.log(4*mp.pi) + mp.euler)*F(0) + \
        mp.quad(integrand2, [0, 1, 5, 20, 60])
    B = -2*WR

    log(f"T1 spectral   S = {mp.nstr(S, 20)}")
    log(f"T1 mine       A = {mp.nstr(A, 20)}   diff {mp.nstr(A-S, 3)}")
    log(f"T1 paper3.15  B = {mp.nstr(B, 20)}   diff {mp.nstr(B-S, 3)}")
    return abs(A - S), abs(B - S)


# ---------------------------------------------------------------- T2
def vhat(n, L, t):
    """V_n^hat(t) = L^{-1/2} (-2i sin(tL/2)) / (2 pi i n/L - i t); t real or complex."""
    num = -2j*mp.sin(t*L/2)
    den = 2j*mp.pi*n/L - 1j*t
    if abs(den) < mp.mpf('1e-25'):      # t -> 2 pi n / L limit
        return mp.sqrt(L)*mp.e**(1j*t*L/2)*mp.mpc(1)  # limit of int: L^{1/2} approx
    return num/(mp.sqrt(L)*den)


def t2():
    lam, N = mp.mpf(2), 6
    L = 2*mp.log(lam)
    T = wf.build_matrix(lam, N, 'zeta')
    c = {j: mp.mpf(0) for j in range(-N, N + 1)}
    c[-1], c[0], c[1] = mp.mpf(1), mp.mpf(-2), mp.mpf(1)
    Qmat = mp.fsum(c[j]*c[k]*T[j + N, k + N]
                   for j in range(-N, N + 1) for k in range(-N, N + 1))

    fhat = lambda t: mp.fsum(c[j]*vhat(j, L, t) for j in (-1, 0, 1))
    K = 1200
    t0 = time.time()
    zs = [mp.zetazero(k).imag for k in range(1, K + 1)]
    log(f"T2 fetched {K} zeros in {time.time()-t0:.0f}s, last = {mp.nstr(zs[-1],10)}")
    Qzero = mp.fsum(2*abs(fhat(g))**2 for g in zs)   # zeros come in +-gamma pairs
    log(f"T2 matrix side  = {mp.nstr(Qmat, 20)}")
    log(f"T2 zero side    = {mp.nstr(Qzero, 20)}  (first {K} zeros, tail ~ t^-5)")
    log(f"T2 rel diff     = {mp.nstr(abs(Qmat-Qzero)/abs(Qmat), 3)}")
    return abs(Qmat - Qzero)/abs(Qmat)


# ---------------------------------------------------------------- T3
def t3():
    lam, N = mp.mpf(3), 24
    L = 2*mp.log(lam)
    rep = wf.ground_state_report(lam, N, 'zeta')
    Te = rep['Te']
    ee, V, order = wf.eig_sym(Te)
    log(f"T3 lambda=3 N={N}: even lows {[mp.nstr(x,8) for x in ee[:4]]}")
    log(f"                 : odd  lows {rep['odd_low'][:4]}")
    gcol = order[0]
    xi_e = [V[i, gcol] for i in range(N + 1)]
    xi = [mp.mpf(0)]*(2*N + 1)
    xi[N] = xi_e[0]
    for n in range(1, N + 1):
        xi[N + n] = xi_e[n]/mp.sqrt(2)
        xi[N - n] = xi_e[n]/mp.sqrt(2)
    roots = wf.spectrum_from_xi(xi, N, L, N)
    pos = [r for r in roots if r > 0][:8]
    zs = [mp.zetazero(k).imag for k in range(1, 9)]
    log("T3   D'' eigenvalue        zeta zero          error")
    for r, g in zip(pos, zs):
        log(f"     {mp.nstr(r,12):20} {mp.nstr(g,12):18} {mp.nstr(r-g,3)}")
    return pos, zs


if __name__ == '__main__':
    dA, dB = t1()
    r2 = t2()
    t3()
    with open('outputs/test_conventions.log', 'w') as fh:
        fh.write('\n'.join(OUT) + '\n')
