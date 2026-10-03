"""B-track evaluator for Haglund's approximants (arXiv:0910.5228v1, eqs (1)-(14)).
Independent of A-track / orch-probe / certificate producer-A: mpmath 1.3.0 only.
Phi_n(z) = 2 pi^2 n^4 G(z/2; pi n^2, 9/4) - 3 pi n^2 G(z/2; pi n^2, 5/4)       (14)
G(w; a, b) = Gamma(b+iw, a)/a^(b+iw) + Gamma(b-iw, a)/a^(b-iw)                 (10)
Xi(z) = xi(1/2 + i z)                                                          (1)
Xi_N = sum_{n<=N} Phi_n  (13);  route T: Xi_N = Xi - sum_{n>N} Phi_n  (main.tex, Thm sandwich)
"""
import mpmath as mp
from mpmath import mpf, mpc

GUP = 'mp'   # which upper incomplete gamma to use: 'mp' (mpmath.gammainc) or 'own'

def gup_cf(w, a, maxit=200000):
    """Own: upper incomplete gamma Gamma(w,a), a>0 real, by Legendre's continued fraction
    Gamma(w,a) = e^-a a^w / (a+1-w - 1(1-w)/(a+3-w - 2(2-w)/(a+5-w - ...))), modified Lentz.
    Convergence check: |delta-1| < 2^-(prec+8) on three consecutive steps."""
    tiny = mpf(2)**(-mp.mp.prec*4)
    b = a + 1 - w
    f = b if b != 0 else tiny
    C = f; D = mpc(0)
    ok = 0
    for j in range(1, maxit):
        an = -j*(j - w)
        b = b + 2
        D = b + an*D
        if D == 0: D = tiny
        C = b + an/C
        if C == 0: C = tiny
        D = 1/D
        delta = C*D
        f = f*delta
        if abs(delta - 1) < mpf(2)**(-mp.mp.prec-8):
            ok += 1
            if ok >= 3:
                return mp.exp(-a + w*mp.log(a))/f, j
        else:
            ok = 0
    raise RuntimeError('gup_cf: no convergence w=%s a=%s' % (w, a))

def gup_ser(w, a, maxit=2000000):
    """Own: Gamma(w,a) = Gamma(w) - gamma(w,a), gamma(w,a) = a^w e^-a sum_k a^k/(w(w+1)...(w+k)).
    Convergence: stop when |term| < 2^-(prec+8) |sum| after the terms have started decreasing.
    Returns (value, number of terms, cancellation in bits)."""
    term = 1/w
    s = term
    k = 0
    big = abs(term)
    while True:
        k += 1
        term = term*a/(w + k)
        s += term
        at = abs(term)
        if at > big: big = at
        if k > abs(a) and at < abs(s)*mpf(2)**(-mp.mp.prec-8):
            break
        if k > maxit:
            raise RuntimeError('gup_ser: no convergence')
    low = mp.exp(-a + w*mp.log(a))*s
    g = mp.gamma(w)
    val = g - low
    canc = 0
    if val != 0:
        lead = abs(mp.exp(-a + w*mp.log(a)))*big
        canc = float(mp.log(max(abs(g), abs(low), lead)/abs(val), 2))
    return val, k, canc

def gup(w, a):
    if GUP == 'mp':
        return mp.gammainc(w, a)
    # own: CF when |w| is not large compared with a, else the series
    if abs(w) < 0.9*a:
        return gup_cf(w, a)[0]
    v, k, canc = gup_ser(w, a)
    if canc > mp.mp.prec/2:
        return gup_cf(w, a)[0]
    return v

def Ghyp(w, a, b):
    p = b + 1j*w
    m = b - 1j*w
    return gup(p, a)*mp.exp(-p*mp.log(a)) + gup(m, a)*mp.exp(-m*mp.log(a))

def Phi(n, z):
    """Haglund (14)."""
    z = mp.mpmathify(z)
    a = mp.pi*n*n
    w = z/2
    return 2*mp.pi**2*n**4*Ghyp(w, a, mpf(9)/4) - 3*mp.pi*n**2*Ghyp(w, a, mpf(5)/4)

def Xi(z):
    """Haglund (1): Xi(z) = xi(1/2+iz); evaluated at s = 1/2 - i z when Im z > 0 (Xi is even)."""
    z = mp.mpmathify(z)
    s = mpf(1)/2 + 1j*z
    if mp.im(z) > 0:
        s = 1 - s
    return s*(s - 1)/2*mp.exp(-s/2*mp.log(mp.pi))*mp.gamma(s/2)*mp.zeta(s)

def XiN_lit(N, z):
    return mp.fsum(Phi(n, z) for n in range(1, N + 1))

def tail(N, z, scale=None, extra=10):
    """sum_{n>N} Phi_n(z), summed until a term is below 2^-(prec+extra) times scale."""
    s = mpc(0)
    n = N + 1
    first = None
    while True:
        p = Phi(n, z)
        s += p
        if first is None:
            first = abs(p)
            if scale is None:
                scale = first
        if abs(p) > scale:
            scale = abs(p)
        if abs(p) < scale*mpf(2)**(-mp.mp.prec - extra) and n > N + 1:
            break
        n += 1
        if n > N + 60:
            raise RuntimeError('tail: slow convergence')
    return s, n

def XiN_T(N, z):
    x = Xi(z)
    sc = abs(x)
    t, n = tail(N, z, scale=sc)
    if abs(t) > sc: sc = abs(t)
    return x - t

# ---- second formula for Phi_n (main.tex, Lemma relation; checked against (14) in the ladder) ----
# Phi_n(z) = (1/2) s(s-1) g_n(s) + (4 pi n^2 - 1) e^{-pi n^2},  s = 1/2 + i z,
# g_n(s) = Gamma(s/2, X) X^{-s/2} + Gamma((1-s)/2, X) X^{-(1-s)/2},  X = pi n^2.
def Phi_rel(n, z):
    z = mp.mpmathify(z)
    X = mp.pi*n*n
    s = mpf(1)/2 + 1j*z
    lX = mp.log(X)
    g = gup(s/2, X)*mp.exp(-s/2*lX) + gup((1 - s)/2, X)*mp.exp(-(1 - s)/2*lX)
    return s*(s - 1)/2*g + (4*X - 1)*mp.exp(-X)

PHI = Phi_rel   # engine used by the pencil code; Phi (eq. 14) is the check

def tailP(N, z, scale, extra=12):
    """sum_{n>N} PHI(n, z) until a term is below 2^-(prec+extra) * running scale."""
    s = mpc(0)
    n = N + 1
    while True:
        p = PHI(n, z)
        s += p
        ap = abs(p)
        if ap > scale: scale = ap
        if ap < scale*mpf(2)**(-mp.mp.prec - extra):
            return s, n
        n += 1
        if n > N + 80:
            raise RuntimeError('tailP: slow convergence at z=%s' % z)

def AB(k, z):
    """Pencil pieces at z: A = Xi_{k+1}(z) (route T), B = Phi_{k+1}(z).
    F_k(z,t) = Xi_k + t Phi_{k+1} = A - u B with u = 1 - t."""
    z = mp.mpmathify(z)
    x = Xi(z)
    B = PHI(k + 1, z)
    sc = max(abs(x), abs(B))
    t, n = tailP(k + 1, z, sc)
    A = x - t
    if mp.im(z) == 0:
        A = mp.re(A); B = mp.re(B)
    return A, B

def XiN(N, z):
    """Xi_N by route T with the PHI engine."""
    z = mp.mpmathify(z)
    x = Xi(z)
    t, n = tailP(N, z, abs(x))
    v = x - t
    return mp.re(v) if mp.im(z) == 0 else v

def dfd(f, z, fz=None, h=None):
    """forward-difference derivative of an analytic f (h ~ 2^(-prec/2) * max(1,|z|))."""
    if h is None:
        h = mpf(2)**(-mp.mp.prec//2)*max(1, abs(z))
    if fz is None:
        fz = f(z)
    return (f(z + h) - fz)/h

def newton(f, z0, tol=None, maxit=40):
    """Newton with forward-difference derivative. Returns (z, last step size, iterations, f'(z))."""
    if tol is None:
        tol = mpf(2)**(-mp.mp.prec + 12)*max(1, abs(z0))
    z = mp.mpmathify(z0)
    for it in range(1, maxit + 1):
        fz = f(z)
        d = dfd(f, z, fz)
        step = fz/d
        z = z - step
        if abs(step) < tol:
            return z, abs(step), it, d
    raise RuntimeError('newton: no convergence from %s (last step %s)' % (z0, step))

def bisect_real(f, a, b, tol=None):
    """Real zero of a real function with f(a) f(b) < 0: bisection to 8 bits, then secant-safeguarded."""
    a = mpf(a); b = mpf(b)
    fa = f(a); fb = f(b)
    assert fa*fb < 0
    if tol is None:
        tol = mpf(2)**(-mp.mp.prec + 10)*max(1, abs(b))
    while b - a > tol:
        m = (a + b)/2
        # secant guess, kept only if inside the inner half
        if fb != fa:
            c = b - fb*(b - a)/(fb - fa)
            if a + (b - a)/4 < c < b - (b - a)/4:
                m = c
        fm = f(m)
        if fm == 0:
            return m
        if fa*fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a + b)/2
