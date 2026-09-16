"""CHECKER's INDEPENDENT transform of the bump B(v) = Z^{-1} exp(-1/(1-4v^2)) on (-1/2,1/2).

Nothing is imported from campaign_lib.py.  Method: Gauss-Legendre quadrature (numpy.polynomial.legendre.leggauss)
on [-1/2, 1/2] in double precision, cross-checked against mpmath tanh-sinh quadrature at 30-40 digits.
Convention (separation-note.md 0.1): Bhat(z) = int_{-1/2}^{1/2} B(v) e^{i z v} dv ; B even => Bhat(eta) = int B cos(eta v) dv,
Bhat(0) = 1, c(lam) = Bhat(i lam) = int B cosh(lam v) dv.
"""
import numpy as np, math
from mpmath import mp

_CACHE = {}
def gl(N):
    if N not in _CACHE:
        from scipy.special import roots_legendre
        x, w = roots_legendre(N)                      # on [-1,1] (fast asymptotic algorithm)
        v = x/2.0; wv = w/2.0                          # map to [-1/2,1/2]
        with np.errstate(over='ignore', divide='ignore', invalid='ignore'):
            b = np.exp(-1.0/(1.0-4.0*v*v))
        b[~np.isfinite(b)] = 0.0
        Znum = float(np.dot(wv, b))
        _CACHE[N] = (v, wv*b/Znum, Znum)               # weights already include B/Z, sum = 1
    return _CACHE[N]

def bhat(eta, N=12000):
    """Bhat at real eta (scalar or array), double precision."""
    v, w, _ = gl(N)
    e = np.atleast_1d(np.asarray(eta, dtype=float))
    out = np.empty_like(e)
    step = max(1, int(4e7//N))
    for i in range(0, len(e), step):
        out[i:i+step] = np.cos(np.outer(e[i:i+step], v)) @ w
    return out

def cedge(lam, N=12000):
    """c(lam) = Bhat(i lam) = int B cosh(lam v) dv (positive terms)."""
    v, w, _ = gl(N)
    l = np.atleast_1d(np.asarray(lam, dtype=float))
    out = np.empty_like(l)
    for i in range(len(l)):
        out[i] = np.dot(np.cosh(l[i]*v), w)
    return out

def Zconst(N=12000): return gl(N)[2]

# ---- mpmath reference (tanh-sinh, breakpoints at the cosine extrema) ----
def bhat_mp(eta, dps=40):
    with mp.workdps(dps):
        eta = mp.mpf(eta)
        Zn = mp.quad(lambda v: mp.exp(-1/(1-4*v*v)), [-mp.mpf(1)/2, -mp.mpf(1)/4, 0, mp.mpf(1)/4, mp.mpf(1)/2])
        f = lambda v: mp.exp(-1/(1-4*v*v))*mp.cos(eta*v)
        # breakpoints at the zeros of cos(eta v) inside (-1/2,1/2)
        pts = [-mp.mpf(1)/2]
        if eta != 0:
            n = int(mp.floor((abs(eta)/2 - mp.pi/2)/mp.pi)) + 1
            zs = sorted([mp.mpf(j+0.5)*mp.pi/eta for j in range(-n-2, n+3)] if eta > 0 else [])
            pts += [z for z in zs if -mp.mpf(1)/2 < z < mp.mpf(1)/2]
        pts += [mp.mpf(1)/2]
        tot = mp.mpf(0)
        for i in range(len(pts)-1):
            tot += mp.quad(f, [pts[i], pts[i+1]])
        return tot/Zn

def cedge_mp(lam, dps=40):
    with mp.workdps(dps):
        lam = mp.mpf(lam)
        Zn = mp.quad(lambda v: mp.exp(-1/(1-4*v*v)), [-mp.mpf(1)/2, -mp.mpf(1)/4, 0, mp.mpf(1)/4, mp.mpf(1)/2])
        return mp.quad(lambda v: mp.exp(-1/(1-4*v*v))*mp.cosh(lam*v), [-mp.mpf(1)/2, -mp.mpf(1)/4, 0, mp.mpf(1)/4, mp.mpf(1)/2])/Zn
