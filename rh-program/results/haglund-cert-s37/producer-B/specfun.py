"""specfun.py -- rigorous box enclosures (mp.iv) of Gamma, zeta and h(w) = X^{-w} Gamma(w, X).  Producer B.
Every truncation adds an explicit disk whose radius is the PROVED remainder bound (CERT.md section B).
"""
from ivc import *


def _stirling(w, K):
    """Ln Gamma(w) for a box with Re w > 0: DLMF 5.11.1 with K-1 terms, remainder <= sec^{2K}(ph w / 2) * first
    neglected term (DLMF 5.11(ii), lit/dlmf-5.11.txt).  sec^2(th/2) = 2/(1+cos th), cos th = Re w/|w| >= Re_min/|w|_max."""
    if not lo(w.re) > 0:
        raise ValueError('stirling needs Re w > 0')
    lw = clog_right(w)
    L = (w - R('0.5')) * lw - w + iv.log(2 * iv.pi) / 2
    winv = w.inv()
    winv2 = winv * winv
    p = winv
    for k in range(1, K):
        L = L + p * (R(bernoulli(2 * k)) / (2 * k * (2 * k - 1)))
        p = p * winv2
    cosmin = R(lo(w.re)) / R(w.absup())
    sec2K = (R(2) / (1 + cosmin)) ** K
    B = abs(R(bernoulli(2 * K)))
    bound = sec2K * B / (2 * K * (2 * K - 1)) / R(w.abslo()) ** (2 * K - 1)
    return L.widen(bound), hi(bound)


def lngamma(w):
    """a box Lg with Gamma(w) = exp(Lg):  Lg = LnGamma(w+m) - sum_{j<m} Log(w+j)  (Gamma(w+m) = Gamma(w) prod (w+j);
    principal logs of boxes off the negative axis, so no wrapping from a long complex product; any 2 pi i ambiguity
    disappears on exponentiation).  Shift m chosen so that the Stirling remainder is tiny."""
    if lo(w.re) >= 0 and w.abslo() >= 300:
        m, K = 0, 20
    else:
        m = max(0, int(mp.ceil(45 - lo(w.re))))
        K = 30
    L, bnd = _stirling(w + m, K)
    for j in range(m):
        L = L - clog_gen(w + j)
    return L


def gamma(w):
    return cexp(lngamma(w))


def zeta_em(s, relbits):
    """zeta(s) by Euler-Maclaurin (DLMF 2.10.1 with f(x) = x^{-s}, a = N):
       zeta(s) = sum_{n<N} n^{-s} + N^{1-s}/(s-1) + N^{-s}/2 + sum_{k=1}^{m-1} B_2k/(2k)! (s)_{2k-1} N^{1-s-2k} + R_m,
       |R_m| <= (2 - 2^{1-2m}) |B_2m|/(2m)! |(s)_{2m}| N^{1-sigma-2m} / (sigma + 2m - 1)   [DLMF 24.9.2 bounds B_2m - B~_2m].
       Stops at the first m with bound <= 2^-relbits.  Returns (box, N, m, bound)."""
    smax = s.absup()
    N = max(40, int(mp.ceil(smax / mp.pi)) + 10)
    sig, t = s.re, s.im
    S = C(0)
    for n in range(1, N):
        ln = iv.log(n)
        mag = iv.exp(-sig * ln)
        ang = t * ln
        S = S + C(mag * iv.cos(ang), -mag * iv.sin(ang))
    lN = iv.log(N)
    NP = cexp((1 - s) * lN)                      # N^{1-s}
    S = S + NP / (s - 1) + cexp(-s * lN) / 2
    invN2 = 1 / R(N) ** 2
    P = s                                        # (s)_{2k-1} for k = 1
    Npow = NP * invN2                            # N^{1-s-2k} for k = 1
    tol = mp.mpf(2) ** (-relbits)
    sigmin = lo(sig)
    k = 1
    prevb = None
    while True:
        S = S + P * Npow * (R(bernoulli(2 * k)) / fact(2 * k))
        k += 1                                   # candidate m = k
        P = P * (s + (2 * k - 3)) * (s + (2 * k - 2))      # (s)_{2k-1}
        Npow = Npow * invN2
        s2m = (P * (s + (2 * k - 1))).absup()               # |(s)_{2m}|, m = k
        if sigmin + 2 * k - 1 <= 0:
            continue
        bnd = (2 - R(2) ** (1 - 2 * k)) * abs(R(bernoulli(2 * k))) / fact(2 * k) * R(s2m) \
            * iv.exp((1 - R(sigmin) - 2 * k) * lN) / (R(sigmin) + 2 * k - 1)
        b = hi(bnd)
        if b <= tol or k > 400 or (prevb is not None and b > prevb):
            if b > tol:
                print('WARNING zeta_em: tolerance not reached, bound', mp.nstr(b, 5))
            return S.widen(bnd), N, k, b
        prevb = b


def h_ibp(w, X, relbits, Kmax=1500):
    """h(w) = X^{-w} Gamma(w,X) = int_1^oo e^{-Xu} u^{w-1} du, X > 0 real.  K-fold integration by parts:
       h = e^{-X} [ sum_{k<K} tau_k + rho ],  tau_k = (w-1)...(w-k)/X^{k+1},
       |rho| <= |tau_K| X / (X - max(Re w - 1 - K, 0))   (proof: CERT.md B3).  Returns box or None if not convergent."""
    tau = C(1 / X)
    S = C(0)
    tol = mp.mpf(2) ** (-relbits)
    prev = None
    wremax = hi(w.re)
    for k in range(0, Kmax):
        S = S + tau
        tau = tau * (w - (k + 1)) / X                       # tau_{k+1}
        K = k + 1
        beta = max(wremax - 1 - K, 0)
        if not lo(X) > beta:
            continue
        bnd = R(tau.absup()) * X / (X - beta)
        a = tau.absup()
        if hi(bnd) <= tol * S.absup():
            return (S.widen(bnd)) * iv.exp(-X)
        if prev is not None and a >= prev and K > wremax + 2:
            return None                                     # terms growing: asymptotic regime exhausted
        prev = a
    return None


def h_lower(w, X, relbits, Kmax=4000):
    """h(w) = X^{-w} Gamma(w) - e^{-X} sum_{k<K} X^k/(w)_{k+1} - rho,   |rho| <= e^{-X} X^K/|(w)_K|
       valid when Re w + K >= X + 1 and w not in {0,-1,...} (proof: CERT.md B4)."""
    main = cexp(lngamma(w) - w * iv.log(X))              # X^{-w} Gamma(w)
    u = w.inv()                                            # u_0 = 1/w
    S = C(0)
    tol = mp.mpf(2) ** (-relbits)
    remin = lo(w.re)
    eX = iv.exp(-X)
    for K in range(1, Kmax):
        S = S + u                                          # S = sum_{k<K} u_k
        if remin + K >= hi(X) + 1:
            bnd = X * R(u.absup())                         # X^K/|(w)_K| = X |u_{K-1}|
            if hi(bnd) <= tol * S.absup():
                return main - (S.widen(bnd)) * eX
        u = u * X / (w + K)
    raise RuntimeError('h_lower: no convergence')


def h_enclose(w, X, relbits):
    r = h_ibp(w, X, relbits)
    if r is not None:
        return r, 'ibp'
    return h_lower(w, X, relbits), 'lower'
