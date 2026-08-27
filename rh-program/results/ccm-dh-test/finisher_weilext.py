"""
finisher_weilext.py -- Session-5 FINISHER extension of weilform.py (original left untouched).

Adds kind='chi5': the Legendre symbol mod 5 -- the EVEN real primitive character of
conductor 5. This is the decisive SAME-CONDUCTOR control for the collapse-rate
interpretation: L(s,chi5) has an intact Euler product and (numerically) true RH,
while Davenport-Heilbronn has conductor 5, a broken Euler product and off-line zeros.
If the chi5 Weil-form ground eigenvalue collapses at the same exponential rate in
mu = lambda^2 as DH's, the collapse RATE measures archimedean/conductor data, not
Euler-product input.

kind='chi4' (odd real character mod 4: same gamma-factor shape a=3/4 as DH,
conductor 4) already exists in weilform.build_matrix; the cross-conductor scaling
control uses it directly.

build_matrix_ext mirrors weilform.build_matrix line-for-line (same composite-GL
engine, same conventions), with the parameter table factored out and extended.
"""
import mpmath as mp
import weilform as wf


def lambda_chi5(nmax):
    """Lambda_chi(n) = chi5(p)^k log p for n = p^k, chi5 = Legendre symbol mod 5
    (chi5(1)=chi5(4)=1, chi5(2)=chi5(3)=-1, chi5(5)=0).  Even character => a=1/4."""
    leg = {0: 0, 1: 1, 2: -1, 3: -1, 4: 1}
    out = {}
    for p in range(2, nmax + 1):
        if all(p % d for d in range(2, int(p**0.5) + 1)):
            c = leg[p % 5]
            if c != 0:
                pk, k = p, 1
                while pk <= nmax:
                    out[pk] = (c**k)*mp.log(p)
                    pk *= p
                    k += 1
    return out


def params(kind, nmax):
    """(a, log(qcond/pi), lamdict, use02) per kind. First three kinds identical to
    weilform.build_matrix's inline table (verified by eye + by the reverify script)."""
    if kind == 'zeta':
        return mp.mpf(1)/4, -mp.log(mp.pi), wf.lambda_von_mangoldt(nmax), True
    if kind == 'dh':
        return mp.mpf(3)/4, mp.log(5/mp.pi), wf.lambda_dh(nmax), False
    if kind == 'chi4':
        return mp.mpf(3)/4, mp.log(4/mp.pi), wf.lambda_chi4(nmax), False
    if kind == 'chi5':
        return mp.mpf(1)/4, mp.log(5/mp.pi), lambda_chi5(nmax), False
    raise ValueError(kind)


def build_matrix_ext(lam, N, kind, M=None, K=None):
    """(2N+1)x(2N+1) tau matrix; mirror of weilform.build_matrix with params()."""
    L = 2*mp.log(lam)
    nmax = int(mp.floor(lam**2 + mp.mpf('1e-9')))
    a, logqpi, lamdict, use02 = params(kind, nmax)

    if M is None:
        M = N + 10
    if K is None:
        K = max(30, int(mp.mp.dps*0.8))
    Y, W = wf.composite_grid(L, M, K)
    npts = len(Y)

    q0 = mp.mpf(2)
    g_arch, s1_arch, cosh2 = [], [], []
    for y in Y:
        den = -mp.expm1(-2*y)
        e2ay = mp.e**(-2*a*y)
        g_arch.append(-2*e2ay/den)
        s1_arch.append(2*q0*e2ay*mp.expm1(-(2 - 2*a)*y)/den)
        cosh2.append(2*mp.cosh(y/2))

    twopiL = 2*mp.pi/L

    phi = {0: mp.mpf(0)}
    for n in range(1, N + 1):
        w_ = twopiL*n
        sins = [mp.sin(w_*y) for y in Y]
        arch = mp.fsum(W[i]*g_arch[i]*sins[i] for i in range(npts))
        val = mp.mpf('0.5')*arch - wf.prime_sum_sin(n, L, lamdict)
        if use02:
            val += wf.w02_sin(n, L)
        phi[n] = val
        phi[-n] = -val

    diag = {}
    tail = -q0*mp.log(-mp.expm1(-2*L))
    for j in range(0, N + 1):
        w_ = twopiL*j
        acc = []
        for i, y in enumerate(Y):
            dq = 2*(-2*mp.sin(w_*y/2)**2 - (y/L)*mp.cos(w_*y))
            acc.append(W[i]*(s1_arch[i] + g_arch[i]*dq))
        arch = mp.fsum(acc) + tail + (logqpi - mp.euler)*q0
        val = mp.mpf('0.5')*arch - wf.prime_sum_diag(j, L, lamdict)
        if use02:
            val += mp.fsum(W[i]*2*(1 - Y[i]/L)*mp.cos(w_*Y[i])*cosh2[i]
                           for i in range(npts))
        diag[j] = val
        diag[-j] = val

    dim = 2*N + 1
    T = mp.matrix(dim, dim)
    for ji, j in enumerate(range(-N, N + 1)):
        for ki, k in enumerate(range(-N, N + 1)):
            if j == k:
                T[ji, ki] = diag[j]
            else:
                T[ji, ki] = (phi[j] - phi[k])/(mp.pi*(k - j))
    return T
