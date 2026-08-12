"""
weilform.py -- Truncated Weil quadratic form QW^{lambda,N} of CCM arXiv:2511.22755,
for Riemann zeta AND for the Davenport-Heilbronn function.

Source of definitions (verified directly from the PDF of arXiv:2511.22755,
downloaded 2026-08-13; page/eq refs to that paper):

  * eq (3.19):  QW_lambda(f,f) = int_R |fhat(t)|^2 (2 theta'(t))/(2pi) dt
                 + 2 Re( fhat(i/2) conj(fhat(-i/2)) )
                 - sum_{1<n<=lambda^2} Lambda(n) <f|T(n)f>,
    on L^2([1/lambda, lambda], du/u), fhat(z) = int f(u) u^{-iz} du/u,
    theta(t) = -(t/2) log pi + Im log Gamma(1/4 + it/2)   (eq 3.9)
    <f|T(n)g> = n^{-1/2} [ (f^* star g)(n) + (f^* star g)(1/n) ]  (eq 3.20),
    star = multiplicative convolution, f^*(u) = conj(f(1/u)).

  * Basis (2.6)/(3.21): U_n(x) = L^{-1/2} exp(2 pi i n x / L) on [0,L], L = 2 log lambda,
    V_n = kappa(U_n), kappa(f)(u) = f(log(lambda u)).  E_N = span{V_n : |n| <= N}.

  * Lemma 2.3: q(U_j,U_k)(y), y in [0,L]:
        j != k :  [sin(2 pi j y/L) - sin(2 pi k y/L)] / (pi (k-j))
        j == k :  2 (1 - y/L) cos(2 pi j y / L)
    and tau_{jk} = QW(V_j, V_k) = Psi#( q(U_j,U_k)(log .) )  (eq 3.18, 5.1).

  * Lemma 5.1 structure: tau_{ii} = a_i, tau_{ij} = (b_i - b_j)/(i-j), a_{-i}=a_i,
    b_{-i} = -b_i  => tau commutes with the parity grading gamma(V_j) = V_{-j}.

  * Definition 5.3 (even-simple): smallest eigenvalue simple, eigenvector xi with
    gamma xi = xi.  Section 8 missing step (a): QW^{lambda,N} even-simple.

  * Theorem 5.10 / Lemma 5.4(iii): spectrum of the rank-one-perturbed scaling operator
    D'' is given (in index units s' = s L/(2 pi)) by the roots of
        sum_{j=-N}^{N} xi_j / (j - s') = 0,
    with xi normalized by <eta|xi> = 1, eta = sum_j V_j.  Physical eigenvalues
    s = (2 pi / L) s' should approximate the imag parts of the zeta (resp. DH) zeros.

Archimedean term, log-side representation (derived here; validated numerically
against the spectral-side t-integral in test_conventions.py before any use):

  W_infty(h) = (1/2pi) int_R hhat(t) w_a(t) dt,   w_a(t) = Re psi(a + it/2) + log(qcond/pi)
     (zeta: a = 1/4, qcond = 1  -> w = Re psi(1/4+it/2) - log pi = 2 theta'(t);
      DH:   a = 3/4, qcond = 5  -> completed FE  (5/pi)^{(s+1)/2} Gamma((s+1)/2) f(s) inv. s->1-s)

  For even F with F(y) = folded (h(y)+h(-y)) = q(y):
  (1/2pi) int_R qhat(t) w_a(t) dt =
      [log(qcond/pi) - gamma_E] q(0)
      + int_0^infty [ 2 e^{-2y} q(0) - 2 e^{-2ay} q(y) ] / (1 - e^{-2y}) dy
  and W_infty(h) = (1/2) * (that), since hhat + (h o iota)hat = qhat and w_a even.

Davenport-Heilbronn:
  f_DH(s) = 5^{-s} [ zeta(s,1/5) + kap zeta(s,2/5) - kap zeta(s,3/5) - zeta(s,4/5) ],
  kap = (sqrt(10 - 2 sqrt 5) - 2)/(sqrt 5 - 1); coefficients a_n periodic mod 5:
  (1, kap, -kap, -1, 0).  Lambda_DH(n) from a_n log n = sum_{d|n} Lambda_DH(d) a_{n/d}.
  DH form: tau_DH = (1/2) Arch_{3/4,5}(q) - sum_{1<n<=lambda^2} Lambda_DH(n) n^{-1/2} q(log n)
  (no W_{0,2} term: the completed DH function is entire, no pole).
"""

import mpmath as mp


# ---------------------------------------------------------------- q functions
def q_offdiag(j, k, L, y):
    """q(U_j,U_k)(y) for j != k, y in [0,L]  (Lemma 2.3)."""
    return (mp.sin(2*mp.pi*j*y/L) - mp.sin(2*mp.pi*k*y/L)) / (mp.pi*(k - j))


def q_diag(j, L, y):
    """q(U_j,U_j)(y), y in [0,L]  (Lemma 2.3)."""
    return 2*(1 - y/L)*mp.cos(2*mp.pi*j*y/L)


# ------------------------------------------------------- archimedean, log side
def arch_pair_sin(n, L, a, npanels=None):
    """int_0^L sin(2 pi n y / L) * (-2 e^{-2 a y} / (1 - e^{-2y})) dy
    == psi-part of Arch_a applied to s_n(y)=sin(2 pi n y/L) (which has s_n(0)=0).
    Stable near 0:  s_n(y)/(1-e^{-2y}) ~ (2 pi n /L) y / (2y).
    """
    w = 2*mp.pi*n/L

    def integrand(y):
        if y == 0:
            return -mp.mpf(2)*w/2  # limit: -2 * e^0 * (w y)/(2y)
        den = -mp.expm1(-2*y)      # 1 - e^{-2y} > 0
        return -2*mp.e**(-2*a*y) * mp.sin(w*y) / den

    pts = mp.linspace(0, L, max(4, int(abs(n)) + 2))
    return mp.quad(integrand, pts)


def arch_diag(j, L, a, logq_over_pi):
    """Arch_a(q_jj) = [log(qcond/pi) - gamma_E] * q(0)
        + int_0^infty [2 e^{-2y} q(0) - 2 e^{-2ay} q(y)]/(1-e^{-2y}) dy,  q = q_jj, q(0)=2.
    Split: [0,L] numeric + explicit tail  -q(0) log(1-e^{-2L}).
    Stable small-y form:
        num = 2[ q0 (e^{-2y} - e^{-2ay})  - e^{-2ay} (q(y)-q0) ]
        q(y)-q0 = 2[(cos wy - 1) - (y/L) cos wy],  cos wy - 1 = -2 sin^2(wy/2).
    """
    w = 2*mp.pi*j/L
    q0 = mp.mpf(2)

    def integrand(y):
        if y == 0:
            # limit: [q0 * (-2+2a) y - (q'(0)) y ] / (2y);  q'(0) = -2/L
            return (q0*(2*a - 2) + mp.mpf(2)/L) / 2
        den = -mp.expm1(-2*y)
        e2ay = mp.e**(-2*a*y)
        # e^{-2y} - e^{-2ay} = e^{-2ay} (e^{-(2-2a)y} - 1) = e^{-2ay} expm1(-(2-2a)y)
        d1 = e2ay*mp.expm1(-(2 - 2*a)*y)
        dq = 2*(-2*mp.sin(w*y/2)**2 - (y/L)*mp.cos(w*y))
        return (2*(q0*d1 - e2ay*dq)) / den

    pts = mp.linspace(0, L, max(4, abs(j) + 2))
    main = mp.quad(integrand, pts)
    tail = -q0*mp.log(-mp.expm1(-2*L))
    return (logq_over_pi - mp.euler)*q0 + main + tail


# ------------------------------------------------------------- W_{0,2} (zeta)
def w02_sin(n, L):
    """int_0^L sin(2 pi n y/L) * 2 cosh(y/2) dy   (closed form)."""
    w = 2*mp.pi*n/L
    # int sin(wy) e^{sy} dy = e^{sy}(s sin wy - w cos wy)/(s^2+w^2)
    def I(s):
        return (mp.e**(s*L)*(s*mp.sin(w*L) - w*mp.cos(w*L)) + w) / (s*s + w*w)
    return I(mp.mpf('0.5')) + I(mp.mpf('-0.5'))


def w02_diag(j, L):
    """int_0^L 2(1-y/L) cos(2 pi j y/L) * 2 cosh(y/2) dy   (numeric, cheap)."""
    w = 2*mp.pi*j/L

    def integrand(y):
        return 2*(1 - y/L)*mp.cos(w*y)*2*mp.cosh(y/2)
    pts = mp.linspace(0, L, max(4, abs(j) + 2))
    return mp.quad(integrand, pts)


# --------------------------------------------------------------- prime  sides
def lambda_von_mangoldt(nmax):
    """dict n -> Lambda(n) (mpf), 2 <= n <= nmax."""
    out = {}
    for p in range(2, nmax + 1):
        if all(p % d for d in range(2, int(p**0.5) + 1)):
            pk = p
            while pk <= nmax:
                out[pk] = mp.log(p)
                pk *= p
    return out


def dh_kappa():
    """kappa = (sqrt(10-2 sqrt5)-2)/(sqrt5-1)  (classical DH constant)."""
    s5 = mp.sqrt(5)
    return (mp.sqrt(10 - 2*s5) - 2)/(s5 - 1)


def dh_coeffs(nmax):
    """a_n for DH, periodic (1,kap,-kap,-1,0) mod 5."""
    kap = dh_kappa()
    pat = {1: mp.mpf(1), 2: kap, 3: -kap, 4: mp.mpf(-1), 0: mp.mpf(0)}
    return [None] + [pat[n % 5] for n in range(1, nmax + 1)]


def lambda_dh(nmax):
    """Lambda_DH(n) via a_n log n = sum_{d|n} Lambda_DH(d) a_{n/d}, Lambda(1)=0."""
    a = dh_coeffs(nmax)
    lam = [mp.mpf(0)]*(nmax + 1)
    for n in range(2, nmax + 1):
        s = a[n]*mp.log(n)
        for d in range(2, n):
            if n % d == 0:
                s -= lam[d]*a[n // d]
        lam[n] = s  # a_1 = 1
    return {n: lam[n] for n in range(2, nmax + 1) if lam[n] != 0}


def prime_sum_sin(n, L, lamdict):
    """sum_m Lambda(m) m^{-1/2} s_n(log m), s_n(y) = sin(2 pi n y/L)."""
    w = 2*mp.pi*n/L
    return mp.fsum(lam/mp.sqrt(m)*mp.sin(w*mp.log(m)) for m, lam in lamdict.items())


def prime_sum_diag(j, L, lamdict):
    """sum_m Lambda(m) m^{-1/2} q_jj(log m)."""
    w = 2*mp.pi*j/L
    return mp.fsum(lam/mp.sqrt(m)*2*(1 - mp.log(m)/L)*mp.cos(w*mp.log(m))
                   for m, lam in lamdict.items())


# -------------------------------------------------- composite GL quadrature
_GL_CACHE = {}


def gl_nodes(K):
    """K-point Gauss-Legendre nodes/weights on [-1,1] at current precision.
    numpy float64 seeds refined by mp Newton on P_K."""
    key = (K, mp.mp.dps)
    if key in _GL_CACHE:
        return _GL_CACHE[key]
    import numpy as np

    xs_f, _ = np.polynomial.legendre.leggauss(K)

    def PdP(x):
        p0, p1 = mp.mpf(1), x
        for k in range(2, K + 1):
            p0, p1 = p1, ((2*k - 1)*x*p1 - (k - 1)*p0)/k
        dp = K*(x*p1 - p0)/(x*x - 1)
        return p1, dp
    xs, ws = [], []
    for xf in xs_f:
        x = mp.mpf(float(xf))
        for _ in range(60):
            p, dp = PdP(x)
            dx = p/dp
            x -= dx
            if abs(dx) < mp.mpf(10)**(-mp.mp.dps - 5):
                break
        p, dp = PdP(x)
        xs.append(x)
        ws.append(2/((1 - x*x)*dp*dp))
    _GL_CACHE[key] = (xs, ws)
    return xs, ws


def composite_grid(L, M, K):
    """Nodes/weights of M-panel composite K-point GL on [0, L]."""
    xs, ws = gl_nodes(K)
    h = L/M
    Y, W = [], []
    for m in range(M):
        a_, b_ = m*h, (m + 1)*h
        c_, r_ = (a_ + b_)/2, (b_ - a_)/2
        for x, w in zip(xs, ws):
            Y.append(c_ + r_*x)
            W.append(r_*w)
    return Y, W


# ------------------------------------------------------------- matrix builder
def build_matrix(lam, N, kind='zeta', M=None, K=None):
    """Return (2N+1)x(2N+1) mp.matrix tau, index order j = -N..N.

    kind='zeta': tau = W02 + (1/2) Arch_{1/4, qcond=1}(q) - prime(Lambda)
    kind='dh'  : tau =        (1/2) Arch_{3/4, qcond=5}(q) - prime(Lambda_DH)

    Fast shared-node composite Gauss-Legendre engine; all integrands analytic
    on [0,L] (removable singularity at 0 handled by stable expm1 forms).
    """
    L = 2*mp.log(lam)
    nmax = int(mp.floor(lam**2 + mp.mpf('1e-9')))
    if kind == 'zeta':
        a, logqpi, lamdict, use02 = mp.mpf(1)/4, -mp.log(mp.pi), \
            lambda_von_mangoldt(nmax), True
    elif kind == 'dh':
        a, logqpi, lamdict, use02 = mp.mpf(3)/4, mp.log(5/mp.pi), \
            lambda_dh(nmax), False
    else:
        raise ValueError(kind)

    if M is None:
        M = N + 10
    if K is None:
        K = max(30, int(mp.mp.dps*0.8))
    Y, W = composite_grid(L, M, K)
    npts = len(Y)

    # shared node data
    q0 = mp.mpf(2)
    g_arch = []      # -2 e^{-2ay}/(1-e^{-2y})        (pairs with sin(w_n y), dq_j)
    s1_arch = []     # 2 q0 e^{-2ay} expm1(-(2-2a)y)/(1-e^{-2y})   (diag const part)
    cosh2 = []       # 2 cosh(y/2)
    for y in Y:
        den = -mp.expm1(-2*y)
        e2ay = mp.e**(-2*a*y)
        g_arch.append(-2*e2ay/den)
        s1_arch.append(2*q0*e2ay*mp.expm1(-(2 - 2*a)*y)/den)
        cosh2.append(2*mp.cosh(y/2))

    twopiL = 2*mp.pi/L

    # phi_n, n = 1..N  (phi_{-n} = -phi_n, phi_0 = 0)
    phi = {0: mp.mpf(0)}
    for n in range(1, N + 1):
        w_ = twopiL*n
        sins = [mp.sin(w_*y) for y in Y]
        arch = mp.fsum(W[i]*g_arch[i]*sins[i] for i in range(npts))
        val = mp.mpf('0.5')*arch - prime_sum_sin(n, L, lamdict)
        if use02:
            val += w02_sin(n, L)
        phi[n] = val
        phi[-n] = -val

    # diagonal a_j, j = 0..N
    diag = {}
    tail = -q0*mp.log(-mp.expm1(-2*L))
    for j in range(0, N + 1):
        w_ = twopiL*j
        # Arch: int S1 + g_arch * dq_j ; dq_j = 2[-2 sin^2(w y/2) - (y/L) cos(w y)]
        acc = []
        for i, y in enumerate(Y):
            dq = 2*(-2*mp.sin(w_*y/2)**2 - (y/L)*mp.cos(w_*y))
            acc.append(W[i]*(s1_arch[i] + g_arch[i]*dq))
        arch = mp.fsum(acc) + tail + (logqpi - mp.euler)*q0
        val = mp.mpf('0.5')*arch - prime_sum_diag(j, L, lamdict)
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


# --------------------------------------------------- parity blocks and eigen
def parity_blocks(T, N):
    """T in basis j=-N..N -> (T_even (N+1)x(N+1) basis {V0,(V_n+V_-n)/sqrt2},
                              T_odd  N x N     basis {(V_n-V_-n)/sqrt2})."""
    def idx(j):
        return j + N
    Te = mp.matrix(N + 1, N + 1)
    for m in range(0, N + 1):
        for n in range(0, N + 1):
            if m == 0 and n == 0:
                Te[0, 0] = T[idx(0), idx(0)]
            elif m == 0:
                Te[0, n] = (T[idx(0), idx(n)] + T[idx(0), idx(-n)])/mp.sqrt(2)
                Te[n, 0] = Te[0, n]
            elif n >= m:
                v = (T[idx(m), idx(n)] + T[idx(m), idx(-n)]
                     + T[idx(-m), idx(n)] + T[idx(-m), idx(-n)])/2
                Te[m, n] = v
                Te[n, m] = v
    To = mp.matrix(N, N)
    for m in range(1, N + 1):
        for n in range(m, N + 1):
            v = (T[idx(m), idx(n)] - T[idx(m), idx(-n)]
                 - T[idx(-m), idx(n)] + T[idx(-m), idx(-n)])/2
            To[m - 1, n - 1] = v
            To[n - 1, m - 1] = v
    return Te, To


def eig_sym(M):
    """Sorted eigenvalues + eigenvectors (mp.eigsy)."""
    E, V = mp.eigsy(M)
    ev = [E[i] for i in range(M.rows)]
    order = sorted(range(len(ev)), key=lambda i: ev[i])
    return [ev[i] for i in order], V, order


def ground_state_report(lam, N, kind='zeta'):
    """Build matrix, return dict with bottom spectrum data in both parity sectors."""
    T = build_matrix(lam, N, kind)
    Te, To = parity_blocks(T, N)
    ee, _, _ = eig_sym(Te)
    eo, _, _ = eig_sym(To)
    return {'lambda': str(lam), 'N': N, 'kind': kind,
            'even_low': [mp.nstr(x, 12) for x in ee[:6]],
            'odd_low': [mp.nstr(x, 12) for x in eo[:6]],
            'min_even': ee[0], 'min_odd': eo[0], 'T': T, 'Te': Te, 'To': To}


# ----------------------------------------------- D'' spectrum from eigenvector
def spectrum_from_xi(xi_full, N, L, smax_index):
    """Roots (index units) of sum_j xi_j/(j - s') = 0 between consecutive j,
    then scaled by 2 pi/L.  xi_full: list indexed j=-N..N."""
    def g(s):
        return mp.fsum(xi_full[j + N]/(j - s) for j in range(-N, N + 1))
    roots = []
    for j in range(-N, N):
        if j + 1 > smax_index:
            break
        a_, b_ = mp.mpf(j) + mp.mpf('1e-12'), mp.mpf(j + 1) - mp.mpf('1e-12')
        ga, gb = g(a_), g(b_)
        if mp.sign(ga) == mp.sign(gb):
            continue
        try:
            r = mp.findroot(g, (a_, b_), solver='anderson')
            roots.append(r*2*mp.pi/L)
        except Exception:
            pass
    return roots
