# zeros.py -- A-track: zeros of Xi_N off the real axis: argument-principle counts (floating point, adaptive) and location.
# Facts used (checked in NOTE.md): Xi_N(conj z) = conj Xi_N(z); Xi_N(iy) > 0 for real y (Phi_n(z) = int_0^oo phi_n(t)
# cos(zt) dt with phi_n > 0 on [0, oo)); so the count in [0,X] x [-Y,Y] is (arg change along (X,0)->(X,Y)->(0,Y))/pi.
import math, cmath, time
from a_core import *

def farg(N, z, route="T"):
    v = XiN(N, az(z), route, 24)
    w = acb(v.real.mid(), v.imag.mid())          # exact midpoint: arg of a negative real number is +pi, not a cut ball
    return float(w.arg().mid())

def _wrap(d):
    return (d + math.pi) % (2 * math.pi) - math.pi

def argpath(N, pts_fn, s0, s1, ds=0.25, route="T", dmax=math.pi / 4, minlen=1e-9):
    """arg change of Xi_N along z(s), s in [s0, s1] (pts_fn: s -> complex). Adaptive bisection until every
    consecutive increment is below dmax. Returns (total, nsamples, nflag)."""
    n = max(2, int(math.ceil((s1 - s0) / ds)))
    S_ = [s0 + (s1 - s0) * j / n for j in range(n + 1)]
    A_ = [farg(N, pts_fn(s), route) for s in S_]
    total = 0.0
    nsamp = len(S_)
    nflag = 0
    stack = [(S_[j], A_[j], S_[j + 1], A_[j + 1]) for j in range(n)][::-1]
    while stack:
        a, fa, b, fb = stack.pop()
        d = _wrap(fb - fa)
        if abs(d) > dmax and b - a > minlen:
            m = 0.5 * (a + b)
            fm = farg(N, pts_fn(m), route)
            nsamp += 1
            stack.append((m, fm, b, fb))
            stack.append((a, fa, m, fm))
            continue
        if abs(d) > dmax:
            nflag += 1
        total += d
    return total, nsamp, nflag

def count_sym(N, X, Y, ds=0.25, route="T"):
    """number of zeros of Xi_N in [0,X] x [-Y,Y] (floating point argument principle on the upper half of the boundary)."""
    t0 = time.time()
    r1, n1, f1 = argpath(N, lambda s: complex(X, s), 0.0, Y, ds, route)
    r2, n2, f2 = argpath(N, lambda s: complex(X - s, Y), 0.0, X, ds, route)
    a_end = farg(N, complex(0.0, Y), route)
    tot = r1 + r2
    val = tot / math.pi
    return {"N": N, "X": X, "Y": Y, "count_float": val, "count": int(round(val)), "dev": abs(val - round(val)),
            "arg_at_(0,Y)": a_end, "samples": n1 + n2, "flags": f1 + f2, "ds": ds, "secs": round(time.time() - t0, 2)}

def count_rect(N, x0, x1, y0, y1, ds=0.25, route="T"):
    """number of zeros of Xi_N in the rectangle [x0,x1] x [y0,y1] (floating point argument principle, full boundary)."""
    r = 0.0
    nf = 0
    ns = 0
    for (fn, a, b) in ((lambda s: complex(x0 + s, y0), 0.0, x1 - x0), (lambda s: complex(x1, y0 + s), 0.0, y1 - y0),
                       (lambda s: complex(x1 - s, y1), 0.0, x1 - x0), (lambda s: complex(x0, y1 - s), 0.0, y1 - y0)):
        t, n, f = argpath(N, fn, a, b, ds, route)
        r += t
        nf += f
        ns += n
    val = r / (2 * math.pi)
    return int(round(val)), val, nf, ns

def dXiN_ratio(N, z, route="T", h=1e-9):
    """Xi_N(z)/Xi_N'(z) (Newton step) with Xi_N' by an Arb central difference; exact float shifted points."""
    zp, zm = complex(z.real + h, z.imag), complex(z.real - h, z.imag)
    f0 = XiN(N, az(z), route, 90)
    fp = XiN(N, az(zp), route, 90)
    fm = XiN(N, az(zm), route, 90)
    prec0 = ctx.prec
    ctx.prec = 256
    r = f0 * (arb(zp.real) - arb(zm.real)) / (fp - fm)
    ctx.prec = prec0
    return C(r)

def newton_XiN(N, z, route="T", it=50, tol=1e-14, maxmove=None):
    z0 = complex(z)
    for _ in range(it):
        dz = dXiN_ratio(N, z, route)
        z = z - dz
        if maxmove is not None and abs(z - z0) > maxmove:
            return z, False
        if abs(dz) < tol * max(1.0, abs(z)):
            return z, True
    return z, False

def dedup(zs, tol=1e-8):
    out = []
    for z in sorted(zs, key=lambda w: (w.real, w.imag)):
        if not any(abs(z - w) < tol * max(1.0, abs(z)) for w in out):
            out.append(z)
    return out

def march(N, known, X, route="T", maxnew=5000):
    """extend a list of non-real zeros of Xi_N (upper half plane) to the right, up to real part X, by linear
    extrapolation from the last two and Newton. Returns the extended sorted list."""
    zs = dedup([z for z in known if z.imag > 1e-9])
    zs.sort(key=lambda w: w.real)
    added = 0
    while zs and zs[-1].real < X and added < maxnew:
        a = zs[-2] if len(zs) >= 2 else zs[-1] - 4.0
        b = zs[-1]
        step = b - a
        got = None
        for fac in (1.0, 0.7, 1.3, 0.5, 1.6, 0.85, 1.15):
            for dy in (0.0, 0.3 * abs(step), -0.3 * abs(step)):
                seed = b + fac * step + 1j * dy
                z, ok = newton_XiN(N, seed, route, maxmove=1.5 * abs(step))
                if ok and z.imag > 1e-9 and z.real > b.real + 0.15 * step.real and all(abs(z - w) > 1e-8 for w in zs):
                    got = z
                    break
            if got is not None:
                break
        if got is None:
            break
        zs.append(got)
        zs.sort(key=lambda w: w.real)
        added += 1
        if added % 10 == 0:
            print("    march N=%d: %d added, last %.4f%+.4fi" % (N, added, got.real, got.imag), flush=True)
    return zs
