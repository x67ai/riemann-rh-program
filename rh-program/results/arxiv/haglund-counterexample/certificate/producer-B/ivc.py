"""ivc.py -- rectangular complex intervals built ONLY on mpmath's real interval type (mp.iv, outward rounding).
Producer B, unit haglund-cert-s37.  No Arb / python-flint anywhere.
A box C(re, im) stands for the set {x + i y : x in re, y in im}; every operation returns a box containing the exact image.
"""
import mpmath as mp
from fractions import Fraction
from math import factorial

iv = mp.iv


def set_prec(bits):
    iv.prec = bits


def lo(x):
    """exact lower endpoint (mp.mpf) of a real interval -- all comparisons go through lo/hi (iv '>' may return None)."""
    return mp.make_mpf(x._mpi_[0])


def hi(x):
    return mp.make_mpf(x._mpi_[1])


def R(x):
    """real interval containing x (int, decimal string, Fraction, mpf or interval)."""
    if isinstance(x, Fraction):
        return iv.mpf(x.numerator) / iv.mpf(x.denominator)
    return iv.mpf(x)


def sqr(x):
    """[x]^2 as a real interval with nonnegative lower end (iv mult of an interval containing 0 would give < 0)."""
    a, b = lo(x), hi(x)
    if a >= 0 or b <= 0:
        return x * x
    m = max(-a, b)
    return iv.mpf([0, hi(iv.mpf(m) * iv.mpf(m))])


def hull(x, y):
    return iv.mpf([min(lo(x), lo(y)), max(hi(x), hi(y))])


class C:
    __slots__ = ('re', 'im')

    def __init__(self, re, im=0):
        self.re = R(re)
        self.im = R(im)

    def __add__(self, o):
        o = o if isinstance(o, C) else C(o)
        return C(self.re + o.re, self.im + o.im)
    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, C) else C(o)
        return C(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return C(o) - self

    def __neg__(self):
        return C(-self.re, -self.im)

    def __mul__(self, o):
        if not isinstance(o, C):
            o = R(o)
            return C(self.re * o, self.im * o)
        return C(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    __rmul__ = __mul__

    def inv(self):
        d = sqr(self.re) + sqr(self.im)
        if not lo(d) > 0:
            raise ZeroDivisionError('complex box contains 0')
        return C(self.re / d, -self.im / d)

    def __truediv__(self, o):
        if not isinstance(o, C):
            o = R(o)
            return C(self.re / o, self.im / o)
        return self * o.inv()

    def __rtruediv__(self, o):
        return C(o) * self.inv()

    def conj(self):
        return C(self.re, -self.im)

    def abs2(self):
        return sqr(self.re) + sqr(self.im)

    def absup(self):
        """mpf upper bound of |z| over the box."""
        return hi(iv.sqrt(self.abs2()))

    def abslo(self):
        """mpf lower bound of |z| over the box."""
        return lo(iv.sqrt(self.abs2()))

    def contains0(self):
        return lo(self.re) <= 0 <= hi(self.re) and lo(self.im) <= 0 <= hi(self.im)

    def widen(self, r):
        """add the closed disk of radius r (r: number or interval; its upper end is used), as a square."""
        rr = hi(R(r))
        e = iv.mpf([-rr, rr])
        return C(self.re + e, self.im + e)

    def mid(self):
        return mp.mpc((lo(self.re) + hi(self.re)) / 2, (lo(self.im) + hi(self.im)) / 2)

    def rad(self):
        return max(hi(self.re) - lo(self.re), hi(self.im) - lo(self.im)) / 2

    def __repr__(self):
        return 'C(%s, %s)' % (self.re, self.im)

    def nstr(self, n=12):
        return '[%s, %s] + i[%s, %s]' % (mp.nstr(lo(self.re), n), mp.nstr(hi(self.re), n),
                                         mp.nstr(lo(self.im), n), mp.nstr(hi(self.im), n))


def cexp(z):
    e = iv.exp(z.re)
    return C(e * iv.cos(z.im), e * iv.sin(z.im))


def clog_right(z):
    """principal log of a box lying in the open right half-plane Re > 0 (asserted)."""
    if not lo(z.re) > 0:
        raise ValueError('clog_right: box not in Re > 0')
    return C(iv.log(z.abs2()) / 2, iv.atan2(z.im, z.re))


def atan_iv(u):
    """real interval arctan(u), via atan2(u, 1) (second argument positive: the unambiguous case)."""
    return iv.atan2(u, R(1))


def clog_gen(z):
    """principal log of a box that does not meet the closed negative real axis: the box must lie in Re > 0,
    Im > 0 or Im < 0; the argument is then atan(y/x), pi/2 - atan(x/y) or -pi/2 - atan(x/y) respectively."""
    rl = iv.log(z.abs2()) / 2
    if lo(z.re) > 0:
        a = atan_iv(z.im / z.re)
    elif lo(z.im) > 0:
        a = iv.pi / 2 - atan_iv(z.re / z.im)
    elif hi(z.im) < 0:
        a = -iv.pi / 2 - atan_iv(z.re / z.im)
    else:
        raise ValueError('clog_gen: box meets the negative real axis or 0')
    return C(rl, a)


def arg_right(q):
    """principal argument of a box in Re > 0 (asserted); result lies in (-pi/2, pi/2)."""
    if not lo(q.re) > 0:
        raise ValueError('arg_right: box not in Re > 0')
    return iv.atan2(q.im, q.re)


def box(x0, x1, y0, y1):
    """the complex box [x0, x1] + i[y0, y1] (endpoints: decimal strings or numbers; hull taken outward)."""
    X = hull(R(x0), R(x1))
    Y = hull(R(y0), R(y1))
    return C(X, Y)


# ---- exact Bernoulli numbers (Fractions) via  sum_{j=0}^{n} binom(n+1, j) B_j = 0 ----
_BERN = [Fraction(1)]


def bernoulli(n):
    from math import comb
    while len(_BERN) <= n:
        k = len(_BERN)
        s = sum(comb(k + 1, j) * _BERN[j] for j in range(k))
        _BERN.append(-s / (k + 1))
    return _BERN[n]


def fact(n):
    return factorial(n)
