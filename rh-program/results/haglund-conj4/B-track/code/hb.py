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
