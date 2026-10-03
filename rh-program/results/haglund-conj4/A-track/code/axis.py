# axis.py -- A-track: the real-axis scan of S_k = Xi_{k+1}/Phi_{k+1} (test (d) / P3) and the real zero counts.
# On the axis S_k is real; zeros of Xi_k are S_k = 1, zeros of Xi_{k+1} are S_k = 0; a local max of S_k with value
# u* in (0,1) is a landing (a conjugate pair arrives at u = u*), a local min with value in (0,1) is a departure (witness).
import math, time
from a_core import *

BIG = 1e300

def Sx(k, x, route="T", bits=40):
    """S_k(x) for real x as a float (clipped to +-1e300), and the acb."""
    v = S(k, acb(arb(x), arb(0)), route, bits)
    m = v.real.mid()
    if abs(m) > arb("1e300"):
        return (BIG if m > 0 else -BIG), v
    return float(m), v

def dSx(k, x, route="T", h=1e-9):
    """S_k'(x) (real axis) by a central difference in Arb at relative radius 2^-90."""
    a = S(k, acb(arb(x) + arb(h), arb(0)), route, 90)
    b = S(k, acb(arb(x) - arb(h), arb(0)), route, 90)
    d = (a - b).real / (2 * arb(h))
    m = d.mid()
    if abs(m) > arb("1e300"):
        return BIG if m > 0 else -BIG
    return float(m)

def spacing(x):
    return 2 * math.pi / math.log(max(x, 40.0) / (2 * math.pi))

def grid(x0, x1, frac=20.0):
    xs = [x0]
    while xs[-1] < x1:
        xs.append(min(x1, xs[-1] + spacing(xs[-1]) / frac))
    return xs

def root(k, a, b, fa, fb, c, route="T", tol=1e-12):
    """solve S_k(x) = c on [a,b] with a sign change (Illinois regula falsi with bisection fallback)."""
    ga, gb = fa - c, fb - c
    side = 0
    for it in range(200):
        if b - a < tol * max(1.0, abs(a)):
            break
        m = b - gb * (b - a) / (gb - ga) if abs(gb - ga) < 1e299 and ga != gb else 0.5 * (a + b)
        if not (a < m < b) or it % 7 == 6:
            m = 0.5 * (a + b)
        gm = Sx(k, m, route)[0] - c
        if gm == 0:
            return m
        if (gm > 0) == (gb > 0):
            b, gb = m, gm
            if side == -1: ga *= 0.5
            side = -1
        else:
            a, ga = m, gm
            if side == 1: gb *= 0.5
            side = 1
    return 0.5 * (a + b)

def crit(k, a, b, route="T", tol=1e-12):
    """a zero of S_k' on [a,b] (S' changes sign) by bisection/secant; returns x*."""
    da, db = dSx(k, a, route), dSx(k, b, route)
    if (da > 0) == (db > 0):
        return None
    for it in range(200):
        if b - a < tol * max(1.0, abs(a)):
            break
        m = b - db * (b - a) / (db - da) if abs(db - da) < 1e299 else 0.5 * (a + b)
        if not (a < m < b) or it % 5 == 4:
            m = 0.5 * (a + b)
        dm = dSx(k, m, route)
        if (dm > 0) == (db > 0):
            b, db = m, dm
        else:
            a, da = m, dm
    return 0.5 * (a + b)
