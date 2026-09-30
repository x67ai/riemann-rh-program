"""
fp_moments.py -- compute (or load from cache) the full-precision Stieltjes moments c_m = s_{m+1} (real side) and
Li coefficients lambda_n (circle side) for FUNC, as Arb balls; cache = exact (mantissa, exponent, radius).
Shared by the injection (visibility) and control scripts.
"""
import os, sys, pickle, time
from math import comb
sys.path.insert(0, os.path.dirname(__file__))
from flint import arb, arb_series, ctx, fmpz

here = os.path.dirname(os.path.abspath(__file__))
tabdir = os.path.join(os.path.dirname(here), 'tables')

def _log_completed(FUNC, s, x, at_one):
    half = arb(1) / 2
    if FUNC == 'zeta' or FUNC.startswith('faq') or FUNC.startswith('eul'):
        logpi = arb.pi().log()
        if at_one:
            base = half.log() + s.log() - (s / 2) * logpi + (s / 2).lgamma() + (1 + x * s.zeta(deflate=True)).log()
        else:
            base = half.log() + (s * (1 - s)).log() - (s / 2) * logpi + (s / 2).lgamma() + (-(s.zeta())).log()
        if FUNC.startswith('faq') or FUNC.startswith('eul'):
            parts = FUNC.split(':')
            if FUNC.startswith('faq'):
                a = arb(parts[1]); q = arb(parts[2])
            else:
                q = arb(parts[1]); a = -(q + 1)
            u = (s - half) * q.log()
            fac = a / q.sqrt() + u.exp() + (-u).exp()
            if fac.coeffs()[0] < 0:
                fac = -fac
            base = base + fac.log()
        return base
    q = 4 if FUNC == 'chi4' else 5
    qq = arb(q)
    pre = ((s + 1) / 2) * (qq / arb.pi()).log() + ((s + 1) / 2).lgamma()
    if FUNC == 'chi4':
        L = (-(s * qq.log())).exp() * (s.zeta(arb(1) / 4) - s.zeta(arb(3) / 4))
    elif FUNC == 'dh':
        s5 = arb(5).sqrt()
        kap = ((10 - 2 * s5).sqrt() - 2) / (s5 - 1)
        L = (-(s * qq.log())).exp() * (s.zeta(arb(1) / 5) + kap * s.zeta(arb(2) / 5)
                                       - kap * s.zeta(arb(3) / 5) - s.zeta(arb(4) / 5))
    else:
        raise ValueError(FUNC)
    if L.coeffs()[0] < 0:
        L = -L
    return pre + L.log()

def _pack(x):
    m, e = x.mid().man_exp()
    return (int(m), int(e), float(x.rad()))

def _unpack(t):
    m, e, r = t
    v = arb(fmpz(m)) * arb(2) ** e if True else None
    return arb(v.mid(), r) if r > 0 else v

def real_moments(FUNC, P, M):
    """c_m = s_{m+1}, m = 0..M-1."""
    fn = os.path.join(tabdir, 'mom_real_%s_P%d_M%d.pkl' % (FUNC.replace(':', '-'), P, M))
    ctx.prec = P
    if os.path.exists(fn):
        return [_unpack(t) for t in pickle.load(open(fn, 'rb'))]
    ctx.cap = 2 * M + 3
    x = arb_series([0, 1]); s = arb(1) / 2 + x
    c = _log_completed(FUNC, s, x, False).coeffs()
    cm = [((-1) ** (m + 2)) * (m + 1) * c[2 * (m + 1)] for m in range(0, M)]
    pickle.dump([_pack(v) for v in cm], open(fn, 'wb'))
    return cm

def li_coefficients(FUNC, P, N):
    """lambda_0..lambda_{N+1} (lambda_0 = 0)."""
    fn = os.path.join(tabdir, 'lam_%s_P%d_N%d.pkl' % (FUNC.replace(':', '-'), P, N))
    ctx.prec = P
    if os.path.exists(fn):
        return [_unpack(t) for t in pickle.load(open(fn, 'rb'))]
    ctx.cap = N + 3
    w = arb_series([0, 1]); s1 = 1 + w
    at_one = (FUNC == 'zeta' or FUNC.startswith('faq') or FUNC.startswith('eul'))
    d = _log_completed(FUNC, s1, w, at_one).coeffs()
    lam = [arb(0)] + [n * sum((arb(comb(n - 1, j - 1)) * d[j] for j in range(1, n + 1)), arb(0)) for n in range(1, N + 2)]
    pickle.dump([_pack(v) for v in lam], open(fn, 'wb'))
    return lam

def toeplitz_from_lambda(lam):
    N = len(lam) - 2
    return [lam[n + 1] - 2 * lam[n] + (lam[1] if n == 0 else lam[n - 1]) for n in range(0, N + 1)]
