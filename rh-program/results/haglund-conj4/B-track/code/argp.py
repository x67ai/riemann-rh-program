"""Numerical argument principle (not interval-rigorous): adaptive sampling of arg f along segments,
refining until every consecutive pair of samples differs in arg by < pi/6 and is at most `hmax` apart.
count_window: zeros of a real-symmetric f in (0,X) x (-Y,Y) = (change of arg along X -> X+iY -> iY -> 0)/pi.
count_rect: zeros in a rectangle off the real axis = winding/(2 pi)."""
import mpmath as mp

class Arg:
    def __init__(self, f, hmax=0.25):
        self.f = f; self.cache = {}; self.hmax = hmax; self.nev = 0
    def val(self, z):
        key = (float(mp.re(z)), float(mp.im(z)))
        v = self.cache.get(key)
        if v is None:
            v = self.f(z); self.nev += 1
            if v == 0:
                raise ZeroDivisionError('f vanishes on the contour at %s' % z)
            self.cache[key] = v
        return v
    def seg(self, a, b, depth=0):
        fa, fb = self.val(a), self.val(b)
        d = mp.arg(fb/fa)
        if (abs(d) < mp.pi/6 and abs(b - a) <= self.hmax) or depth > 48:
            if depth > 48:
                raise RuntimeError('argp: refinement too deep near %s' % a)
            return d
        m = (a + b)/2
        return self.seg(a, m, depth + 1) + self.seg(m, b, depth + 1)
    def path(self, pts):
        return sum(self.seg(pts[i], pts[i + 1]) for i in range(len(pts) - 1))

def count_window(f, X, Y, hmax=0.25):
    A = Arg(f, hmax)
    X = mp.mpf(X); Y = mp.mpf(Y)
    d = A.path([mp.mpc(X, 0), mp.mpc(X, Y), mp.mpc(0, Y), mp.mpc(0, 0)])
    return d/mp.pi, A.nev

def count_rect(f, x0, x1, y0, y1, A=None, hmax=0.25):
    if A is None:
        A = Arg(f, hmax)
    c = [mp.mpc(x0, y0), mp.mpc(x1, y0), mp.mpc(x1, y1), mp.mpc(x0, y1), mp.mpc(x0, y0)]
    return A.path(c)/(2*mp.pi), A

def find_zeros(f, x0, x1, y0, y1, A=None, newton=None, minsize=0.5, out=None):
    """All zeros in the rectangle by recursive bisection + Newton (each found zero must lie in its box)."""
    if out is None: out = []
    w, A = count_rect(f, x0, x1, y0, y1, A)
    n = int(mp.nint(w))
    if abs(w - n) > 0.05:
        raise RuntimeError('non-integer winding %s on box %s' % (w, (x0, x1, y0, y1)))
    if n == 0:
        return out
    if n == 1 and max(x1 - x0, y1 - y0) <= minsize*4:
        try:
            z, st, it, d = newton(f, mp.mpc((x0 + x1)/2, (y0 + y1)/2))
            if x0 <= mp.re(z) <= x1 and y0 <= mp.im(z) <= y1:
                out.append(z); return out
        except (RuntimeError, ZeroDivisionError):
            pass
    if max(x1 - x0, y1 - y0) < 1e-6:
        raise RuntimeError('box too small with %d zeros at %s' % (n, (x0, x1, y0, y1)))
    if x1 - x0 >= y1 - y0:
        xm = (x0 + x1)/2
        find_zeros(f, x0, xm, y0, y1, A, newton, minsize, out)
        find_zeros(f, xm, x1, y0, y1, A, newton, minsize, out)
    else:
        ym = (y0 + y1)/2
        find_zeros(f, x0, x1, y0, ym, A, newton, minsize, out)
        find_zeros(f, x0, x1, ym, y1, A, newton, minsize, out)
    return out
