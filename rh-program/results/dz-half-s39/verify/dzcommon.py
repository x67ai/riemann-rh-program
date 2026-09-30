"""dzcommon.py — Diamond–Zhang templates (book ch. 17) and helpers. Unit dz-half-s39.
f_R(v) = (1 - 1/v)/log v (Thm 17.11); f_C(v) = f_R(v) - 2 sum_k (g(v^{4^-k})/4^k) v^{-4^-k} cos(gamma_k log v),
gamma_k = exp(4^k), g = sum_n chi^{*n}/n, chi = 1_[e, e^2] (17.30), (17.44). In log variable w = log u,
chi^{*n}(e^w) = Irwin-Hall_n(w - n) (sum of n Uniform[1,2]); checked against (17.31) in selftest().
"""
import math
import numpy as np
from scipy.special import exp1, expi

C1 = 1 / math.e + 7 / (3 * math.e ** 4) + 3e-7   # DZ p. 216: c1 = 0.410616... (upper bound used)
CSTAR = 2 * C1 / (1 - math.exp(-4))              # (17.45): c = 2 c1 / (1 - e^-4)
EULER = 0.5772156649015329

def irwin_hall(n, t):
    t = np.asarray(t, dtype=float)
    out = np.zeros_like(t)
    ok = (t >= 0) & (t <= n)
    tt = t[ok]
    acc = np.zeros_like(tt)
    for j in range(0, n + 1):
        term = ((-1) ** j) * math.comb(n, j) * np.where(tt >= j, np.abs(tt - j) ** (n - 1), 0.0)
        acc += term
    out[ok] = acc / math.factorial(n - 1)
    return out

_GRID = None

def _renewal_grid(wmax=64.0, h=2e-5):
    """q(w) := w g(e^w) solves q(w) = w 1_[1,2](w) + int_{w-2}^{w-1} q(r) dr (from G = 1 - chi_hat, derived in NOTE §4.1);
    trapezoid cumulative integral on a grid of step h. Used for w > 5, where the Irwin-Hall sum cancels catastrophically."""
    global _GRID
    n = int(round(wmax / h)) + 1
    w = np.arange(n) * h
    q = np.zeros(n); Q = np.zeros(n)          # Q = cumulative integral of q from 0
    i1, i2 = int(round(1 / h)), int(round(2 / h))
    for i in range(n):
        wi = w[i]
        if wi < 1 - 1e-12:
            q[i] = 0.0
        else:
            j_hi = i - i1; j_lo = i - i2       # integral over [w-2, w-1]
            integ = (Q[j_hi] if j_hi >= 0 else 0.0) - (Q[j_lo] if j_lo >= 0 else 0.0)
            q[i] = (wi if wi <= 2 + 1e-12 else 0.0) + integ
        Q[i] = (Q[i - 1] + 0.5 * h * (q[i] + q[i - 1])) if i > 0 else 0.0
    _GRID = (w, q)
    return _GRID

def g_of_logu(w):
    """g(u) with w = log u (vectorized); g = 0 for w < 1. Exact Irwin-Hall for w <= 5, renewal grid above."""
    w = np.asarray(w, dtype=float)
    big = w > 5
    if big.any():
        gw, gq = _GRID if _GRID is not None else _renewal_grid()
        out = np.zeros_like(w)
        out[big] = np.interp(w[big], gw, gq) / w[big]
        out[~big] = _g_small(w[~big])
        return out
    return _g_small(w)

def _g_small(w):
    w = np.asarray(w, dtype=float)
    out = np.zeros_like(w)
    if w.size == 0:
        return out
    nmax = int(np.floor(np.max(w))) if np.max(w) >= 1 else 0
    for n in range(1, nmax + 1):
        m = (w >= n) & (w <= 2 * n)
        if m.any():
            out[m] += irwin_hall(n, w[m] - n) / n
    return out

def fR(v):
    v = np.asarray(v, dtype=float)
    return -np.expm1(-np.log(v)) / np.log(v)

def fC_correction(v, kmax=3):
    """sum_k 2 (g(v^{4^-k})/4^k) v^{-4^-k} cos(gamma_k log v); f_C = f_R - this."""
    v = np.asarray(v, dtype=float)
    L = np.log(v)
    out = np.zeros_like(v)
    for k in range(1, kmax + 1):
        lam = 4.0 ** k
        m = L >= lam
        if not m.any():
            continue
        gam = math.exp(lam)
        Lm = L[m]
        # cos(gam*L): reduce the argument in extended precision to keep ~1e-8 accuracy
        arg = np.mod(np.longdouble(gam) * Lm.astype(np.longdouble), np.longdouble(2 * math.pi))
        out[m] += 2 * (g_of_logu(Lm / lam) / lam) * np.exp(-Lm / lam) * np.cos(arg.astype(float))
    return out

def fC(v):
    return fR(v) - fC_correction(v)

def f_template(name):
    return fR if name == "R" else fC

def envelope(name, a):
    """sup of f over [a, inf): f_R decreasing; f_C <= (1 + c) f_R for v >= e^4 (17.45), = f_R below."""
    base = float(fR(np.array([a]))[0])
    return base if name == "R" else (1 + CSTAR) * base

def Ein(T):
    """int_0^T (1 - e^-t)/t dt = E1(T) + log T + gamma."""
    return float(exp1(T) + math.log(T) + EULER)

def FR(v):
    """int_1^v f_R = Ei(log v) - gamma - log log v."""
    L = np.log(np.asarray(v, dtype=float))
    return expi(L) - EULER - np.log(L)

def G_entire(z):
    return 1 - (np.exp(-z) - np.exp(-2 * z)) / z

def selftest():
    # (17.31): g = 1 on [e, e^2]; 1/2 log u - 1 on (e^2, e^3]; (1/6)log^2 u - (3/2) log u + 7/2 on (e^3, e^4]
    w = np.array([1.3, 1.9, 2.4, 2.9, 3.3, 3.8])
    ref = np.array([1, 1, 0.5 * 2.4 - 1, 0.5 * 2.9 - 1, 3.3 ** 2 / 6 - 1.5 * 3.3 + 3.5, 3.8 ** 2 / 6 - 1.5 * 3.8 + 3.5])
    assert np.allclose(g_of_logu(w), ref, atol=1e-12), (g_of_logu(w), ref)
    return True

if __name__ == "__main__":
    print("selftest", selftest(), "c =", CSTAR)
