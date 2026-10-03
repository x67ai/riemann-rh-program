# read-O verification core (Opus reader, 2026-10-03). Own code from the NOTE's and Haglund's definitions.
# No code of A-track, B-track or orch-probe is used or imported.
import mpmath as mp
mp.mp.dps = 30
PI = mp.pi

def Xi(z):
    """Xi(z) = xi(1/2 + i z), xi(s) = s(s-1)/2 pi^{-s/2} Gamma(s/2) zeta(s)  (Haglund (1))."""
    s = mp.mpf('0.5') + 1j*mp.mpmathify(z)
    return s*(s-1)/2 * mp.power(PI, -s/2) * mp.gamma(s/2) * mp.zeta(s)

def G(w, a, b):
    """Haglund (10): G(w;a,b) = Gamma(b+iw,a)/a^(b+iw) + Gamma(b-iw,a)/a^(b-iw) (upper incomplete gamma)."""
    w = mp.mpmathify(w)
    p, q = b + 1j*w, b - 1j*w
    return mp.gammainc(p, a)/mp.power(a, p) + mp.gammainc(q, a)/mp.power(a, q)

def Phi_G(n, z):
    """Haglund (14): Phi_n(z) = 2 pi^2 n^4 G(z/2; pi n^2, 9/4) - 3 pi n^2 G(z/2; pi n^2, 5/4)."""
    X = PI*n*n
    w = mp.mpmathify(z)/2
    return 2*PI**2*n**4*G(w, X, mp.mpf(9)/4) - 3*PI*n*n*G(w, X, mp.mpf(5)/4)

def phit(n, v):
    """NOTE l. 11 kernel: 2y(2y-3) e^{v/2-y}, y = pi n^2 e^{2v}."""
    y = PI*n*n*mp.exp(2*v)
    return 2*y*(2*y-3)*mp.exp(v/2 - y)

def Phi_K(n, z):
    """Second route: Phi_n(z) = 2 int_0^inf phit_n(v) cos(z v) dv, by quadrature in y = X e^{2v}."""
    X = PI*n*n
    z = mp.mpmathify(z)
    f = lambda y: (2*y-3)*mp.power(y/X, mp.mpf(1)/4)*mp.exp(-y)*mp.cos(z*mp.log(y/X)/2)
    pts = [X, X+2, X+8, X+25, X+60, X+140, X+260]
    return 2*mp.quad(f, pts)

def XiN(N, z):
    return mp.fsum(Phi_G(n, z) for n in range(1, N+1))
