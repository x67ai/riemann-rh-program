"""
dh.py -- the Davenport-Heilbronn function: construction, functional-equation check,
zero location (on- and off-line), and Lambda_DH coefficients.

f_DH(s) = 5^{-s} [ zeta(s,1/5) + kap*zeta(s,2/5) - kap*zeta(s,3/5) - zeta(s,4/5) ]
kap = (sqrt(10-2*sqrt5) - 2)/(sqrt5 - 1)
    = tan(theta) with eps_chi = e^{2 i theta} = tau(chi)/(i sqrt5), chi mod 5, chi(2)=i.
Completed:  Xi_DH(s) = (5/pi)^{(s+1)/2} Gamma((s+1)/2) f_DH(s) ;  FE: Xi(s) = Xi(1-s).
On the critical line  Z_DH(t) = Xi_DH(1/2+it)  is real (self-dual FE, real coefficients).
"""
import mpmath as mp


def kappa():
    s5 = mp.sqrt(5)
    return (mp.sqrt(10 - 2*s5) - 2)/(s5 - 1)


def f_dh(s):
    k = kappa()
    return 5**(-s)*(mp.zeta(s, mp.mpf(1)/5) + k*mp.zeta(s, mp.mpf(2)/5)
                    - k*mp.zeta(s, mp.mpf(3)/5) - mp.zeta(s, mp.mpf(4)/5))


def xi_dh(s):
    return (5/mp.pi)**((s + 1)/2)*mp.gamma((s + 1)/2)*f_dh(s)


def z_dh(t):
    """Real on the critical line."""
    v = xi_dh(mp.mpf('0.5') + 1j*t)
    return v.real, v.imag  # imag must be ~0


def kappa_from_gauss_sum():
    """Independent derivation: eps = tau(chi)/(i sqrt5), chi(2)=i; kap = tan(arg(eps)/2)."""
    e = lambda x: mp.e**(2j*mp.pi*x)
    chi = {1: mp.mpc(1), 2: mp.mpc(1j), 3: mp.mpc(-1j), 4: mp.mpc(-1)}
    tau = mp.fsum(chi[n]*e(mp.mpf(n)/5) for n in (1, 2, 3, 4))
    eps = tau/(1j*mp.sqrt(5))
    theta = mp.arg(eps)/2
    return mp.tan(theta), eps


def fe_check(samples=6, dps=None):
    """max |Xi(s)-Xi(1-s)|/|Xi(s)| over pseudorandom s in the strip."""
    rnd = mp.mpf('0.3712')
    worst = mp.mpf(0)
    pts = []
    for k in range(samples):
        sig = mp.mpf('0.1') + mp.mpf('0.8')*mp.fmod(mp.mpf(k)*mp.pi, 1)
        t = 3 + 11*mp.fmod(mp.mpf(k)*mp.e + rnd, 1) + 7*k
        s = sig + 1j*t
        a, b = xi_dh(s), xi_dh(1 - s)
        rel = abs(a - b)/max(abs(a), mp.mpf('1e-99'))
        pts.append((mp.nstr(s, 8), mp.nstr(rel, 3)))
        worst = max(worst, rel)
    return worst, pts


def find_zero(seed, tol_off=None):
    """Newton root of f_dh from complex seed; returns rho."""
    return mp.findroot(f_dh, seed, solver='muller')


def online_zeros(tmax, step=None):
    """Zeros of Z_DH on the critical line in (0.5, tmax) via sign changes + refine.
    Uses the real part of Xi_DH(1/2+it) (imag checked ~ 0)."""
    step = step or mp.mpf('0.18')
    zs = []
    t = mp.mpf('0.5')
    zprev = z_dh(t)[0]
    while t < tmax:
        t2 = t + step
        znew = z_dh(t2)[0]
        if mp.sign(znew) != mp.sign(zprev) and zprev != 0:
            r = mp.findroot(lambda u: z_dh(u)[0], (t, t2), solver='illinois')
            zs.append(r)
        t, zprev = t2, znew
    return zs


def offline_scan(sig_range, t_range, nsig, nt):
    """Grid |f| minima -> Newton -> collect zeros with Re != 1/2.
    Returns list of zeros found (each verified |f(rho)| tiny)."""
    found = []
    sigs = [sig_range[0] + (sig_range[1] - sig_range[0])*mp.mpf(i)/(nsig - 1)
            for i in range(nsig)]
    ts = [t_range[0] + (t_range[1] - t_range[0])*mp.mpf(j)/(nt - 1)
          for j in range(nt)]
    vals = {}
    for i, sg in enumerate(sigs):
        for j, t in enumerate(ts):
            vals[(i, j)] = abs(f_dh(sg + 1j*t))
    for i in range(1, nsig - 1):
        for j in range(1, nt - 1):
            v = vals[(i, j)]
            if all(v <= vals[(i + di, j + dj)]
                   for di in (-1, 0, 1) for dj in (-1, 0, 1)
                   if (di, dj) != (0, 0)):
                try:
                    r = find_zero(sigs[i] + 1j*ts[j])
                except Exception:
                    continue
                if abs(f_dh(r)) < mp.mpf('1e-20') and \
                   t_range[0] - 1 < r.imag < t_range[1] + 1:
                    if not any(abs(r - r0) < mp.mpf('1e-6') for r0 in found):
                        found.append(r)
    return sorted(found, key=lambda z: (abs(z.imag), z.real))


def lambda_dh_table(nmax):
    import weilform as wf
    return wf.lambda_dh(nmax)


if __name__ == '__main__':
    import json, sys, time
    mp.mp.dps = 30
    out = {}
    k1 = kappa()
    k2, eps = kappa_from_gauss_sum()
    out['kappa_surd'] = mp.nstr(k1, 25)
    out['kappa_gauss_sum'] = mp.nstr(k2, 25)
    out['kappa_match'] = mp.nstr(abs(k1 - k2), 3)
    out['eps_chi'] = mp.nstr(eps, 20)
    worst, pts = fe_check()
    out['fe_worst_rel'] = mp.nstr(worst, 3)
    out['fe_samples'] = pts
    print('kappa surd     =', out['kappa_surd'])
    print('kappa gauss    =', out['kappa_gauss_sum'], ' diff', out['kappa_match'])
    print('FE worst rel   =', out['fe_worst_rel'])

    # off-line zero hunt in the classical region around t ~ 85.7 and t <= 130
    t0 = time.time()
    off = offline_scan((mp.mpf('0.51'), mp.mpf('1.10')), (mp.mpf(60), mp.mpf(130)), 14, 120)
    out['offline_zeros_60_130'] = [mp.nstr(r, 20) for r in off]
    out['offline_residuals'] = [mp.nstr(abs(f_dh(r)), 3) for r in off]
    print('off-line zeros (sigma in (0.51,1.10), t in (60,130)):', out['offline_zeros_60_130'],
          f'({round(time.time()-t0)}s)')

    # on-line zeros to t = 130
    t0 = time.time()
    onl = online_zeros(mp.mpf(130))
    out['online_zeros_to_130'] = [mp.nstr(r, 15) for r in onl]
    print(f'{len(onl)} on-line zeros to t=130 ({round(time.time()-t0)}s)')

    # Lambda_DH values
    lam = lambda_dh_table(25)
    out['lambda_dh_2_25'] = {str(n): mp.nstr(v, 20) for n, v in sorted(lam.items())}
    print('Lambda_DH(n), n<=25:', {n: mp.nstr(v, 8) for n, v in sorted(lam.items())})

    with open('outputs/dh_validation.json', 'w') as fh:
        json.dump(out, fh, indent=1)
    print('saved outputs/dh_validation.json')
