"""DD2 (row T27): Krein-Langer instrument.  K(s,w) = (F(s) + conj F(w)) / (s + conj(w) - 1), F = xi'/xi,
sampled at n points on a circle |s - c| = r inside Re s > 1 (Euler-product region).  RH-true (zeta): K PSD.
RH-false (DH, off-line zero 0.808517 + 85.699348 i): one negative square per off-line pair (Krein-Langer).
Reports min/max eigenvalues as a function of the circle's height T and of n (visibility pricing, zoo IV.9)."""
import sys
import mpmath as mp

mp.mp.dps = 70
S5 = mp.sqrt(5)
KAP = (mp.sqrt(10 - 2 * S5) - 2) / (S5 - 1)
C = [1, KAP, -KAP, -1]


def F_zeta(s):
    return (1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2 + mp.digamma(s / 2) / 2
            + mp.zeta(s, 1, 1) / mp.zeta(s))


def F_dh(s):
    f = sum(C[j] * mp.zeta(s, mp.mpf(j + 1) / 5) for j in range(4))
    fp = sum(C[j] * mp.zeta(s, mp.mpf(j + 1) / 5, 1) for j in range(4))
    # f_dh = 5^-s * f ;  f_dh'/f_dh = -log 5 + fp/f
    return mp.log(5 / mp.pi) / 2 + mp.digamma((s + 1) / 2) / 2 - mp.log(5) + fp / f


def eig_range(F, c, r, n):
    pts = [c + r * mp.expj(2 * mp.pi * k / n) for k in range(n)]
    vals = [F(s) for s in pts]
    M = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            M[i, j] = (vals[i] + mp.conj(vals[j])) / (pts[i] + mp.conj(pts[j]) - 1)
    E = mp.eighe(M, eigvals_only=True)
    E = sorted([mp.re(e) for e in E])
    return E


if __name__ == '__main__':
    r = mp.mpf(sys.argv[1]) if len(sys.argv) > 1 else mp.mpf('0.3')
    gam = mp.mpf('85.699348')
    for name, F in (('DH', F_dh), ('zeta', F_zeta)):
        for T in (gam, gam - 5, gam - 10, gam - 20):
            for n in (12, 24, 36):
                E = eig_range(F, mp.mpf('1.5') + 1j * T, r, n)
                print(f"{name:5s} c=1.5+{mp.nstr(T, 8)}i r={mp.nstr(r, 3)} n={n:2d}: "
                      f"min={mp.nstr(E[0], 6)} 2nd={mp.nstr(E[1], 6)} max={mp.nstr(E[-1], 6)} "
                      f"#neg(<-1e-55*max)={sum(1 for e in E if e < -mp.mpf(10)**-55 * E[-1])}",
                      flush=True)
