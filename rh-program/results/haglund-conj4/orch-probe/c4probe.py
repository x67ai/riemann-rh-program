# c4probe.py -- orchestrator's exploratory probe for Haglund's Conjecture 4 (NOT a certificate; midpoint arithmetic with Arb radii watched).
# Starts from the registered evaluator results/arxiv/haglund-counterexample/certificate/producer-A/hag_core.py (imported, not copied).
import sys, os, math, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "arxiv", "haglund-counterexample", "certificate", "producer-A"))
from flint import acb, arb, ctx
from hag_core import Phi, Xi, XiN_L, tail_bound

def pair_T(k, z, M=None):
    """(Xi_{k+1}(z), Phi_{k+1}(z)) by route T: Xi_{k+1} = Xi - sum_{n=k+2}^{M} Phi_n - tail (tail as an error ball)."""
    x = abs(float(z.real.mid()))
    if M is None:
        M = max(k + 6, int(math.sqrt(x / (2 * math.pi))) + 6)
    v = Xi(z)
    for n in range(k + 2, M + 1):
        v -= Phi(n, z)
    E = tail_bound(z, M)
    v = v + acb(arb(0, E), arb(0, E))
    return v, Phi(k + 1, z)

def pair_L(k, z):
    """(Xi_{k+1}(z), Phi_{k+1}(z)) by the literal sum."""
    p = Phi(k + 1, z)
    return XiN_L(k, z) + p, p

def S(k, z, route="T", minbits=40):
    """S_k(z) = Xi_{k+1}(z)/Phi_{k+1}(z) as an acb; precision is raised until the relative radius is below 2^-minbits."""
    prec0 = ctx.prec
    try:
        while True:
            a, b = (pair_T if route == "T" else pair_L)(k, z)
            s = a / b
            m = abs(complex(s.mid()))
            r = float(s.rad()) if hasattr(s, "rad") else float(max(s.real.rad(), s.imag.rad()))
            if r <= max(m, 1e-300) * 2.0 ** (-minbits) or (m < 1e-30 and r < 1e-40):
                return s
            if ctx.prec > 200000:
                raise RuntimeError("precision runaway at z=%s" % z)
            ctx.prec *= 2
    finally:
        ctx.prec = prec0

def Smid(k, z, route="T"):
    s = S(k, z, route)
    return complex(s.real.mid(), s.imag.mid()) if False else s.mid() if hasattr(s, "mid") else s

def cS(k, z, route="T"):
    """complex (python) value of S at python complex z (double precision output; internal precision adaptive)."""
    s = S(k, acb(z.real, z.imag), route)
    return complex(float(s.real.mid()), float(s.imag.mid()))

def cSd(k, z, route="T", h=1e-6):
    """S and S' (central difference, step h) at python complex z."""
    s0 = cS(k, z, route)
    d = (cS(k, z + h, route) - cS(k, z - h, route)) / (2 * h)
    return s0, d
