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

def _sgn(v, c):
    return 1 if v > c else (-1 if v < c else 0)

def scan(k, x0, x1, route="T", frac=20.0, out=None):
    """scan S_k on [x0, x1]. Returns dict: zeros of Xi_k (S=1), zeros of Xi_{k+1} (S=0), extrema with value in (0,1),
    the (0,1)-intervals with their endpoint types, and the consistency check of every interval."""
    t0 = time.time()
    xs = grid(x0, x1, frac)
    vals = [Sx(k, x, route)[0] for x in xs]
    z1, z0 = [], []
    for i in range(len(xs) - 1):
        for c, lst in ((1.0, z1), (0.0, z0)):
            if _sgn(vals[i], c) * _sgn(vals[i + 1], c) < 0:
                lst.append(root(k, xs[i], xs[i + 1], vals[i], vals[i + 1], c, route))
            elif _sgn(vals[i], c) == 0:
                lst.append(xs[i])
    ext = []
    nref = 0
    for i in range(1, len(xs) - 1):
        a, b, c = vals[i - 1], vals[i], vals[i + 1]
        if (b - a) * (c - b) >= 0:
            continue
        if min(abs(a), abs(b), abs(c)) > 1e12:
            continue
        den = a - 2 * b + c
        v = b - (c - a) ** 2 / (8 * den) if den != 0 else b
        if not (-10 < v < 11 or min(abs(a), abs(b), abs(c)) < 10):
            continue
        nref += 1
        xs_ = crit(k, xs[i - 1], xs[i + 1], route)
        if xs_ is None:
            # no sign change of S' between the outer points: try the two halves
            for (p, q) in ((xs[i - 1], xs[i]), (xs[i], xs[i + 1])):
                xs_ = crit(k, p, q, route)
                if xs_ is not None:
                    break
        if xs_ is None:
            ext.append({"x": xs[i], "u": b, "type": "unresolved"})
            continue
        u = Sx(k, xs_, route)[0]
        typ = "max" if b > a else "min"
        if 0 < u < 1:
            ext.append({"x": xs_, "u": u, "type": typ})
    # zeros of Xi_{k+1} bracketing a max in (0,1) that the grid did not separate
    extra0 = []
    for e in ext:
        if e["type"] == "max":
            left = [z for z in z0 if z < e["x"]]
            right = [z for z in z0 if z > e["x"]]
            ok = left and right and not any(z1v for z1v in z1 if left[-1] < z1v < right[0])
            if not (left and right and e["x"] - left[-1] < 3 * spacing(e["x"]) and right[0] - e["x"] < 3 * spacing(e["x"])):
                e["note"] = "bracketing zeros of Xi_{k+1} not both in the grid list"
    # (0,1)-intervals and their consistency
    pts = sorted([(z, 1) for z in z1] + [(z, 0) for z in z0])
    ints = []
    for j in range(len(pts) - 1):
        (pa, ta), (pb, tb) = pts[j], pts[j + 1]
        mid = 0.5 * (pa + pb)
        sm = Sx(k, mid, route)[0]
        if 0 < sm < 1:
            inside = [e for e in ext if pa < e["x"] < pb]
            nmax = sum(1 for e in inside if e["type"] == "max")
            nmin = sum(1 for e in inside if e["type"] == "min")
            want = {(0, 0): 1, (1, 1): -1}.get((ta, tb), 0)
            ints.append({"a": pa, "b": pb, "ends": "%d%d" % (ta, tb), "nmax": nmax, "nmin": nmin,
                         "consistent": nmax - nmin == want})
    res = {"k": k, "x0": x0, "x1": x1, "frac": frac, "route": route, "ngrid": len(xs), "nrefined": nref,
           "zeros_Xik": z1, "zeros_Xik1": z0, "R_k": len(z1), "R_k1": len(z0),
           "extrema01": ext, "intervals01": ints,
           "n_max": sum(1 for e in ext if e["type"] == "max"), "n_min": sum(1 for e in ext if e["type"] == "min"),
           "n_unresolved": sum(1 for e in ext if e["type"] == "unresolved"),
           "all_consistent": all(I["consistent"] for I in ints), "secs": time.time() - t0}
    return res
