# a_core.py -- A-track (stream haglund-conj4) evaluator layer.
# Derived from the orchestrator's probe orch-probe/c4probe.py (2026-10-03); like it, imports the registered evaluator
# results/arxiv/haglund-counterexample/certificate/producer-A/hag_core.py (python-flint 0.6.0, Arb balls).
# Objects: S_k = Xi_{k+1}/Phi_{k+1}; zeros of the pencil Xi_k + t Phi_{k+1} at u = 1 - t are the solutions of S_k = u.
# Route T: Xi_{k+1} = Xi - sum_{n=k+2}^{M} Phi_n - tail (tail as a proved error ball, Lemma T); M raised until the
#          tail ball is below 2^-(bits+8) |value|.   Route L: the literal sum (13).
import sys, os, math, time
HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.abspath(os.path.join(HERE, "..", "..", ".."))          # rh-program/results
sys.path.insert(0, os.path.join(RES, "arxiv", "haglund-counterexample", "certificate", "producer-A"))
from flint import acb, arb, ctx
from hag_core import Phi, Xi, XiN_L, tail_bound

STATS = {"maxrel": 0.0, "maxprec": 0, "nevals": 0, "maxM": 0}
_PREC = {}

def _rel(v):
    """relative radius of an acb, computed in Arb (no double underflow): max(rad re, rad im)/|mid| as a float."""
    r = arb(max(float(v.real.rad()), 0.0)) if False else None
    m = abs(acb(v.real.mid(), v.imag.mid()))
    if m == 0:
        return float("inf")
    rr = (arb(v.real.rad()) + arb(v.imag.rad())) / m
    return float(rr.mid()) if rr.is_finite() else float("inf")

def Phi_fast(n, z):
    """Phi_n(z); for z exactly real (imaginary part the exact zero) the two terms of G are complex conjugates and
    G = 2 Re(first term) (half the incomplete-gamma calls); otherwise hag_core.Phi. Checked against hag_core.Phi."""
    if z.imag == 0 and z.imag.rad() == 0:
        pi = arb.pi()
        a = pi * n * n
        A = acb(a)
        la = acb(a.log())
        w = z / 2
        def g(b):
            s1 = acb(b) + acb(0, 1) * w
            return 2 * (A.gamma_upper(s1) * (-s1 * la).exp()).real
        v = 2 * pi * pi * n ** 4 * g(arb(9) / 4) - 3 * pi * n * n * g(arb(5) / 4)
        return acb(v, 0)
    return Phi(n, z)

def XiN_T_ad(N, z, bits):
    """Xi_N(z) by route T with adaptive M (returns acb). Initial M = max(N + 2, ceil(sqrt(x/4 + 15))): the tail after M
    is about exp(-pi (M+1)^2), against |Xi_N| >~ exp(-pi x/4) below the frontier and ~ exp(-pi (N+1)^2) beyond it; M is
    raised by 4 until the proved tail ball is below 2^-(bits+8) |value|."""
    x = abs(float(z.real.mid()))
    M = max(N + 2, int(math.ceil(math.sqrt(x / 4.0 + 15.0))))
    while True:
        v = Xi(z)
        for n in range(N + 1, M + 1):
            v -= Phi_fast(n, z)
        E = tail_bound(z, M)
        w = v + acb(arb(0, E), arb(0, E))
        av = abs(acb(v.real.mid(), v.imag.mid()))
        if av > 0 and arb(E) < av * arb(2) ** (-(bits + 8)):
            STATS["maxM"] = max(STATS["maxM"], M)
            return w
        if M > N + 400:
            return w
        M += 4

def XiN(N, z, route="T", bits=40):
    """Xi_N(z) as an acb with relative radius <= 2^-bits (precision raised as needed)."""
    key = ("X", N, route)
    prec0 = ctx.prec
    p = _PREC.get(key, 96)
    _t0 = time.time()
    try:
        while True:
            ctx.prec = p
            v = XiN_T_ad(N, z, bits) if route == "T" else XiN_L(N, z)
            if _rel(v) <= 2.0 ** (-bits):
                _PREC[key] = max(64, int(p * 0.8))
                STATS["maxprec"] = max(STATS["maxprec"], p)
                if time.time() - _t0 > 2.0:
                    print("    SLOW XiN N=%d z=%s prec=%d %.1fs" % (N, z.str(12), p, time.time() - _t0), flush=True)
                return v
            if p > 20000:
                raise RuntimeError("precision runaway XiN N=%d z=%s" % (N, z.str(10)))
            p *= 2
    finally:
        ctx.prec = prec0

def S(k, z, route="T", bits=40):
    """S_k(z) = Xi_{k+1}(z)/Phi_{k+1}(z) as an acb with relative radius <= 2^-bits."""
    key = ("S", k, route)
    prec0 = ctx.prec
    p = _PREC.get(key, 96)
    _t0 = time.time()
    try:
        while True:
            ctx.prec = p
            num = XiN_T_ad(k + 1, z, bits) if route == "T" else XiN_L(k + 1, z)
            s = num / Phi_fast(k + 1, z)
            rel = _rel(s)
            if rel <= 2.0 ** (-bits):
                _PREC[key] = max(64, int(p * 0.8))
                STATS["maxprec"] = max(STATS["maxprec"], p)
                STATS["maxrel"] = max(STATS["maxrel"], rel)
                STATS["nevals"] += 1
                if time.time() - _t0 > 2.0:
                    print("    SLOW S k=%d z=%s prec=%d %.1fs" % (k, z.str(12), p, time.time() - _t0), flush=True)
                return s
            if p > 20000:
                raise RuntimeError("precision runaway S k=%d z=%s" % (k, z.str(10)))
            p *= 2
    finally:
        ctx.prec = prec0

def C(v):
    """acb -> python complex (only for values of moderate size)."""
    return complex(float(v.real.mid()), float(v.imag.mid()))

def az(z):
    """python complex -> exact acb point."""
    return acb(arb(z.real), arb(z.imag))

def Sc(k, z, route="T", bits=40):
    return C(S(k, az(z), route, bits))

def SdS(k, z, route="T", h=1e-9, bits=90):
    """(S_k(z), S_k'(z)) as python complex; S' by a central difference computed in Arb at relative radius 2^-bits.
    The shifted points z +- h are python floats (exact binary points); the divisor is their exact difference."""
    zp, zm = complex(z.real + h, z.imag), complex(z.real - h, z.imag)
    s0 = S(k, az(z), route, bits)
    sp = S(k, az(zp), route, bits)
    sm = S(k, az(zm), route, bits)
    prec0 = ctx.prec
    ctx.prec = 256
    d = (sp - sm) / (arb(zp.real) - arb(zm.real))
    ctx.prec = prec0
    return C(s0), C(d)
