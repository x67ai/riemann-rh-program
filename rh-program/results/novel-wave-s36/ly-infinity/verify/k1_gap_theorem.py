"""k1_gap_theorem.py -- numerical check of the counting/gap bound for Kronecker
restrictions of Lee-Yang polynomials in PRIME variables, and its collision with Xi.

Statement checked (Alon-Vinzant, arXiv:2208.xxxx 'Gap distributions ...', Thm 1.9, p.5,
re-derived in NOTE sec.2): for p Lee-Yang of multidegree d and positive l,
    | #zeros of p(exp(-i l t)) in (a,b)  -  <d,l>(b-a)/(2 pi) |  <=  |d|,
hence every gap <= 2 pi |d| / <d,l>.  In prime variables l_p = log p >= log 2, so
<d,l> >= |d| log 2 and every gap <= 2 pi / log 2 = 9.0647...

Test objects: F(t) = det(I - Z(t) U), Z(t) = diag(p_j^{-it}) (primes may repeat = higher
degree in z_p), U Haar-random unitary.  F is Lee-Yang (||Z U|| < 1 on the polydisc).
Real form: R(t) = w * exp(i W t/2) * F(t), w^2 = conj(det(-U)), is real on R.
Zeros = sign changes of R on a fine grid, refined by bisection.
Also: products prod_p (1 + p^{-1/2} z_p) +- prod_p (z_p + p^{-1/2}) (aligned) and the
seed's prod(1 - p^{-1/2} z_p) +- prod(z_p - p^{-1/2}).
Then: Xi's zero-free interval (-gamma_1, gamma_1), gamma_1 = 14.134725..., versus the bound.
"""
import numpy as np, mpmath as mp, sys, time

rng = np.random.default_rng(20260930)


def haar_unitary(n):
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    return q * (d / np.abs(d))


def realform_det(primes, U):
    ell = np.log(np.array(primes, dtype=float))
    W = ell.sum()
    dm = np.linalg.det(-U)
    w = np.sqrt(np.conj(dm))

    n = len(ell)
    I = np.eye(n)

    def R(t):
        t = np.atleast_1d(np.asarray(t, float))
        out = np.empty(t.shape)
        for s in range(0, len(t), 20000):
            tt = t[s:s + 20000]
            Z = np.exp(-1j * np.outer(tt, ell))                  # (m, n)
            M = I[None, :, :] - Z[:, :, None] * U[None, :, :]     # rows scaled by z_j
            F = np.linalg.det(M)
            v = w * np.exp(1j * W * tt / 2) * F
            out[s:s + 20000] = v.real
        return out
    return R, W


def zeros_by_sign(R, a, b, h):
    ts = np.arange(a, b + h, h)
    v = R(ts)
    z = []
    for i in range(len(ts) - 1):
        if v[i] == 0:
            z.append(ts[i])
        elif v[i] * v[i + 1] < 0:
            lo, hi, flo = ts[i], ts[i + 1], v[i]
            for _ in range(50):
                mid = 0.5 * (lo + hi)
                fm = R(mid)[0]
                if fm * flo <= 0:
                    hi = mid
                else:
                    lo, flo = mid, fm
            z.append(0.5 * (lo + hi))
    return np.array(z), ts, v


def check_config(primes, U, T=400.0, h=None):
    R, W = realform_det(primes, U)
    n = len(primes)
    h = h or min(0.02, 0.1 * 2 * np.pi / W)
    z, ts, v = zeros_by_sign(R, 0.0, T, h)
    # imaginary-part sanity: the non-real part of w e^{iWt/2} F must vanish
    # discrepancy over many windows
    worst = 0.0
    for L in (1.0, 3.0, 9.0, 27.0, 81.0):
        for x in np.linspace(0, T - L, 200):
            N = np.sum((z > x) & (z < x + L))
            worst = max(worst, abs(N - W * L / (2 * np.pi)))
    gaps = np.diff(z)
    return dict(n=n, W=W, nzeros=len(z), worst_disc=worst, bound=n,
                max_gap=gaps.max() if len(gaps) else np.nan, gap_bound=2 * np.pi * n / W)


def main():
    out = []
    print('== Check 1: random det(I - Z U) in prime variables; |disc| <= |d|, max gap <= 2 pi |d|/W')
    configs = [[2], [2, 3], [2, 3, 5], [2, 2, 3], [2, 3, 5, 7], [2, 2, 2, 5], [3, 5, 7, 11, 13],
               [2, 3, 5, 7, 11, 13], [2, 2, 3, 3, 5, 7], [29, 31, 37], [2, 3, 5, 7, 11, 13, 17, 19]]
    ok = True
    for pr in configs:
        for rep in range(3):
            U = haar_unitary(len(pr))
            r = check_config(pr, U)
            flag = (r['worst_disc'] <= r['bound'] + 1e-9) and (r['max_gap'] <= r['gap_bound'] + 1e-6)
            ok &= flag
            print(f"primes={pr} rep={rep} W={r['W']:.4f} zeros(0,400)={r['nzeros']} "
                  f"worst|disc|={r['worst_disc']:.3f} <= {r['bound']}  max_gap={r['max_gap']:.4f} "
                  f"<= {r['gap_bound']:.4f}  {'OK' if flag else 'VIOLATION'}")
    print('ALL CHECKS PASS' if ok else 'SOME CHECK FAILED')

    print('\n== Check 2: product-type (seed and aligned) Lee-Yang combinations')
    for S in ([2, 3, 5, 7], [2, 3, 5, 7, 11, 13]):
        P = float(np.prod(S))
        ell = np.log(np.array(S, float))
        for kind in ('seed', 'aligned'):
            for sgn in (+1, -1):
                sgnc = -1.0 if kind == 'seed' else +1.0   # Blaschke zero at +c (seed) or -c (aligned)

                def F(t):
                    t = np.atleast_1d(t)
                    z = np.exp(-1j * np.outer(t, ell))
                    c = np.array(S, float) ** -0.5
                    A = np.prod(1 + sgnc * c * z, axis=1)
                    B = np.prod(z + sgnc * c, axis=1)
                    return A + sgn * B
                # real form: F = A + sgn*B where B = z^1 conj(A) on R; e^{iWt/2}F*phase real
                W = ell.sum()

                def R(t):
                    v = np.exp(1j * W * np.atleast_1d(t) / 2) * F(t)
                    # choose the real or imaginary axis depending on sgn
                    return v.real if sgn == +1 else v.imag
                z, ts, v = zeros_by_sign(R, 0.0, 400.0, 0.002)
                worst = 0.0
                for L in (1.0, 3.0, 9.0, 27.0):
                    for x in np.linspace(0, 400 - L, 300):
                        N = np.sum((z > x) & (z < x + L))
                        worst = max(worst, abs(N - W * L / (2 * np.pi)))
                gaps = np.diff(z)
                print(f"S={S} kind={kind:8s} sign={sgn:+d} W=log P={W:.4f} zeros={len(z)} "
                      f"expected~{W*400/(2*np.pi):.1f} worst|disc|={worst:.3f} (<= {len(S)}) "
                      f"max_gap={gaps.max():.4f} (<= {2*np.pi*len(S)/W:.4f})")

    print('\n== Check 3: Xi versus the bound')
    mp.mp.dps = 30
    g1 = mp.zetazero(1).imag
    g2 = mp.zetazero(2).imag
    print('gamma_1 =', mp.nstr(g1, 15), ' gamma_2 =', mp.nstr(g2, 15))
    L = 2 * g1
    print('Xi zero-free interval (-gamma_1, gamma_1) length =', mp.nstr(L, 12))
    print('max gap allowed for ANY nonconstant prime-variable LY restriction: 2 pi/log 2 =',
          mp.nstr(2 * mp.pi / mp.log(2), 12))
    for Lint in (mp.mpf('28.2'), 2 * g1 - mp.mpf('1e-6')):
        lb = Lint * mp.log(2) / (2 * mp.pi) - 1
        print(f'interval length {mp.nstr(Lint, 10)}: every nonconstant restriction has N > |d|*{mp.nstr(lb, 8)}'
              f' >= {mp.nstr(lb, 8)} zeros, i.e. N >= {int(mp.floor(lb)) + 1}')
    # the extremal one-variable examples 1 +- 2^{-it}
    for c in (1, -1):
        zs = [(2 * k + (1 if c == 1 else 0)) * mp.pi / mp.log(2) for k in range(-3, 4)]
        inside = [z for z in zs if abs(z) < g1]
        print(f'p(z_2) = 1 {"+" if c == 1 else "-"} z_2: zeros in (-gamma_1, gamma_1):',
              [mp.nstr(z, 6) for z in inside])


if __name__ == '__main__':
    t0 = time.time()
    main()
    print(f'elapsed {time.time() - t0:.1f} s')
