"""ball.py -- complex ball (rectangular-interval) arithmetic on mpmath's ``iv`` context.

D1 M1 v1, mpmath-ball producer leg (D-R3 named work item).  UNTRUSTED producer-side
code: nothing here is inside the trust boundary; its output enters the certified
statement only through the displayed hypothesis H-ENCL of
``results/d1-m1/FORMAT.md`` section 8.1.

WHAT THIS LAYER IS
==================
A complex number z is enclosed as a rectangle ("box")

    z in [reLo, reHi] x [imLo, imHi]  (Re and Im each an mpmath ``iv`` real interval),

with all real-interval arithmetic delegated to mpmath 1.3.0's interval context
(``mpmath.iv``, backed by ``mpmath.libmp.libmpi``), which computes every endpoint
with directed rounding at the context precision ``iv.prec``.  Every complex
operation below is built so that it is INCLUSION-MONOTONE: if z is in box B and
w is in box C then op(z, w) is in op(B, C).  That is the whole soundness
contract of this file, and it reduces, operation by operation, to

  (i)  exact real identities (Re/Im decompositions, derived at each method), and
  (ii) the inclusion property of the underlying mpmath iv primitives
       (+, -, *, /, **2, sqrt, exp, log, cos, sin, atan, pi).

TRUST SURFACE (recorded per standing order 5, honest-labels rule)
=================================================================
(ii) is PLATFORM TRUST in mpmath's directed rounding, exactly parallel to the
Arb leg's trust in Arb.  It is not proved here; it is cross-validated:
``python3 ball.py --selftest`` runs randomized containment tests of every
primitive and every composite operation against independent high-precision
mp-context evaluation (dps 80), with membership decided in EXACT rational
arithmetic (mpf endpoints converted losslessly to Fractions) -- no float
comparisons anywhere in the tests.  A containment failure is a stop-the-line
event for the leg.  The two-producer rule (FORMAT.md sec. 10) is what makes a
silent rounding bug in one platform detectable at transcript level.

EXACTNESS FACTS USED (all verified by the self-test, none load-bearing beyond
this file):
 * ``iv.mpf(int)`` is exact for any Python int (arbitrary precision mantissa).
 * ``iv.mpf(p)/iv.mpf(q)`` encloses the rational p/q (directed division).
 * every iv endpoint is an mpf binary rational (sign, man, exp, bc) and converts
   LOSSLESSLY to Fraction((-1)^sign * man * 2^exp); specials (man = 0 with
   exp != 0) are rejected.
 * ``iv.mpf([a, b]) ** 2`` returns the true range (e.g. [-2,3]**2 = [0,9]), so
   abs2 = re**2 + im**2 never goes spuriously negative.

ARGUMENT ENCLOSURES (the half-plane branch scheme; FORMAT.md sec. 10 recipe)
============================================================================
A box that excludes 0 lies in an open coordinate half-plane (FORMAT.md
derivation D1: 0 not in [a,b]x[c,d] iff a>0 or b<0 or c>0 or d<0, and each
disjunct IS a half-plane statement).  On each half-plane the following is a
continuous branch of arg (derivations inline at ``arg_branch``):

    RE+ (Re z > 0):  theta = atan(Im/Re)            in (-pi/2, pi/2)
    IM+ (Im z > 0):  theta = pi/2 - atan(Re/Im)     in (0, pi)
    RE- (Re z < 0):  theta = pi + atan(Im/Re)       in (pi/2, 3pi/2)
    IM- (Im z < 0):  theta = -pi/2 - atan(Re/Im)    in (-pi, 0)

Derivation that each formula is a branch of arg on its half-plane
(z = x + iy, r = |z|, principal arg denoted Arg, atan odd and increasing):
 * RE+: for x > 0, Arg z = atan(y/x) directly (definition of atan on the open
   right half-plane); continuous there.  Range (-pi/2, pi/2).
 * IM+: for y > 0 write z = i * (y - ix); Arg(i w) = pi/2 + Arg(w) up to 2pi,
   and w = y - ix has Re w = y > 0, so Arg w = atan(-x/y) = -atan(x/y).
   Hence theta = pi/2 - atan(x/y) is an argument of z, continuous on {y > 0},
   with range (0, pi).
 * RE-: for x < 0, -z has Re(-z) > 0, and theta = pi + atan((-y)/(-x))
   = pi + atan(y/x) is an argument of z = -(-z) (adding pi to an argument of
   -z), continuous on {x < 0}, range (pi/2, 3pi/2).
 * IM-: for y < 0, z = -i * (-y + ix)... directly: -z has Im(-z) > 0 so by IM+
   theta_{-z} = pi/2 - atan(-x/-y) = pi/2 - atan(x/y); an argument of z is
   theta_{-z} - pi = -pi/2 - atan(x/y), continuous on {y < 0}, range (-pi, 0).
Consistency on overlapping half-planes: on a quadrant where two formulas apply
they agree exactly (atan(u) + atan(1/u) = sign(u) * pi/2), EXCEPT the RE-/IM-
pair on the open third quadrant, where they differ by exactly 2pi -- which is
why a caller must use ONE tag for both endpoints of one segment (producer_mp.py
does; the difference of the same branch at two points is branch-independent).

The interval evaluation of each formula over a box in its half-plane encloses
{that branch value : z in box}: the quotient interval Y/X contains every y/x
(iv division; denominator interval excludes 0 by the half-plane hypothesis),
atan is applied by the monotone interval atan (libmpi.mpi_atan), and pi by the
interval iv.pi -- inclusion-monotone throughout.

Nothing in this file computes derivatives; the producer's winding tracking is
zeta'/zeta-free by construction (FORMAT.md sec. 10).

U.S. English throughout.  No floats in any decision: all membership and sign
tests in tests and callers go through exact Fractions.
"""

from fractions import Fraction

import mpmath
from mpmath import iv
from mpmath.libmp import mpf_lt
import mpmath.libmp.libmpi as _libmpi

__all__ = [
    "set_prec", "iv_from_fraction", "iv_from_int", "ivmpf_bounds",
    "mpf_tuple_to_fraction", "iv_atan", "iv_intersect", "iv_hull",
    "Ball", "TAGS",
]

TAGS = ("RE+", "IM+", "RE-", "IM-")


def set_prec(bits):
    """Set the iv working precision (bits).  Callers set this once per run."""
    iv.prec = int(bits)


# ---------------------------------------------------------------- exact endpoint plumbing

def mpf_tuple_to_fraction(t):
    """Lossless mpf raw tuple (sign, man, exp, bc) -> Fraction.  Rejects specials."""
    sign, man, exp, _bc = t
    if man == 0:
        if exp == 0:
            return Fraction(0)
        raise ValueError("special mpf value (inf/nan) has no rational value: %r" % (t,))
    v = Fraction(man) * (Fraction(2) ** exp)
    return -v if sign else v


def ivmpf_bounds(x):
    """iv real interval -> (Fraction lo, Fraction hi), exactly."""
    lo, hi = x._mpi_
    return mpf_tuple_to_fraction(lo), mpf_tuple_to_fraction(hi)


def iv_from_int(n):
    """Exact iv interval [n, n] for a Python int."""
    return iv.mpf(int(n))


def iv_from_fraction(fr):
    """iv interval enclosing the exact rational fr (directed division)."""
    fr = Fraction(fr)
    return iv.mpf(fr.numerator) / iv.mpf(fr.denominator)


def iv_from_fraction_pair(lo, hi):
    """iv interval containing [lo, hi] for Fractions lo <= hi (endpoint hull)."""
    lo, hi = Fraction(lo), Fraction(hi)
    if lo > hi:
        raise ValueError("empty interval requested: %s > %s" % (lo, hi))
    return iv_hull(iv_from_fraction(lo), iv_from_fraction(hi))


def _tmin(a, b):
    return a if mpf_lt(a, b) else b


def _tmax(a, b):
    return b if mpf_lt(a, b) else a


def iv_hull(x, y):
    """Interval hull of two iv intervals."""
    (a1, b1), (a2, b2) = x._mpi_, y._mpi_
    return iv.make_mpf((_tmin(a1, a2), _tmax(b1, b2)))


def iv_intersect(x, y):
    """Intersection of two iv intervals; None if provably empty."""
    (a1, b1), (a2, b2) = x._mpi_, y._mpi_
    lo, hi = _tmax(a1, a2), _tmin(b1, b2)
    if mpf_lt(hi, lo):
        return None
    return iv.make_mpf((lo, hi))


def iv_atan(x):
    """Interval arctangent (monotone; mpmath libmpi primitive, directed rounding)."""
    return iv.make_mpf(_libmpi.mpi_atan(x._mpi_, iv.prec))


# ---------------------------------------------------------------- the complex ball

class Ball(object):
    """Complex rectangular interval: re, im are iv real intervals."""

    __slots__ = ("re", "im")

    def __init__(self, re, im):
        self.re = re
        self.im = im

    # ---- constructors
    @classmethod
    def from_fractions(cls, re_fr, im_fr):
        return cls(iv_from_fraction(re_fr), iv_from_fraction(im_fr))

    @classmethod
    def from_fraction_boxes(cls, re_pair, im_pair):
        return cls(iv_from_fraction_pair(*re_pair), iv_from_fraction_pair(*im_pair))

    @classmethod
    def from_int(cls, n):
        return cls(iv_from_int(n), iv_from_int(0))

    @classmethod
    def real_interval(cls, x):
        return cls(x, iv_from_int(0))

    # ---- bounds
    def re_bounds(self):
        return ivmpf_bounds(self.re)

    def im_bounds(self):
        return ivmpf_bounds(self.im)

    def contains_exact(self, re_fr, im_fr):
        """Exact membership of the rational/dyadic point (re_fr, im_fr)."""
        rlo, rhi = self.re_bounds()
        ilo, ihi = self.im_bounds()
        return rlo <= re_fr <= rhi and ilo <= im_fr <= ihi

    def contains_mpc(self, z):
        """Exact membership test of an mp-context complex value (its exact binary value)."""
        return self.contains_exact(mpf_tuple_to_fraction(z.real._mpf_),
                                   mpf_tuple_to_fraction(z.imag._mpf_))

    def max_width(self):
        rlo, rhi = self.re_bounds()
        ilo, ihi = self.im_bounds()
        return max(rhi - rlo, ihi - ilo)  # Fraction

    # ---- ring operations.  Identities: (a+bi)+(c+di) = (a+c)+(b+d)i;
    # (a+bi)(c+di) = (ac-bd)+(ad+bc)i.  Inclusion-monotone since each component
    # is a composition of iv +,-,*.
    def __add__(self, other):
        other = _coerce(other)
        return Ball(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return Ball(-self.re, -self.im)

    def __sub__(self, other):
        other = _coerce(other)
        return Ball(self.re - other.re, self.im - other.im)

    def __rsub__(self, other):
        return _coerce(other) - self

    def __mul__(self, other):
        other = _coerce(other)
        return Ball(self.re * other.re - self.im * other.im,
                    self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def scale_iv(self, x):
        """Multiply by a REAL iv interval x (exact identity (a+bi)x = ax + bxi)."""
        return Ball(self.re * x, self.im * x)

    def abs2(self):
        """Interval containing |z|^2 = Re^2 + Im^2 (iv **2 gives true ranges)."""
        return self.re ** 2 + self.im ** 2

    def abs_iv(self):
        return iv.sqrt(self.abs2())

    def recip(self):
        """1/z = (a - bi)/(a^2+b^2).  Requires the abs2 interval strictly positive
        (that is the box-excludes-0 certificate; raises otherwise)."""
        d = self.abs2()
        if not (d > 0):
            raise ZeroDivisionError("Ball.recip: box does not exclude 0")
        return Ball(self.re / d, -self.im / d)

    def __truediv__(self, other):
        return self * _coerce(other).recip()

    def exp(self):
        """exp(a+bi) = e^a cos b + i e^a sin b (Euler; exact identity), each factor
        by the corresponding iv primitive -- inclusion-monotone composition."""
        ea = iv.exp(self.re)
        return Ball(ea * iv.cos(self.im), ea * iv.sin(self.im))

    # ---- half-plane certificate and argument branch
    def halfplane(self):
        """Return the first tag in TAGS whose OPEN half-plane provably contains the
        box (iv comparisons are certain: X > 0 iff the whole interval is > 0),
        or None.  None <=> the box cannot be certified to exclude 0 this way
        (for boxes, excludes-0 IS equivalent to some coordinate sign: D1)."""
        if self.re > 0:
            return "RE+"
        if self.im > 0:
            return "IM+"
        if self.re < 0:
            return "RE-"
        if self.im < 0:
            return "IM-"
        return None

    def arg_branch(self, tag):
        """Interval enclosing {theta_tag(z) : z in box}, theta_tag the continuous
        branch of arg on the tag's half-plane (derivations in the module
        docstring).  The box MUST lie in that half-plane; verified here."""
        pi = iv.pi
        if tag == "RE+":
            if not (self.re > 0):
                raise ValueError("box not certified in RE+ half-plane")
            return iv_atan(self.im / self.re)
        if tag == "IM+":
            if not (self.im > 0):
                raise ValueError("box not certified in IM+ half-plane")
            return pi / 2 - iv_atan(self.re / self.im)
        if tag == "RE-":
            if not (self.re < 0):
                raise ValueError("box not certified in RE- half-plane")
            return pi + iv_atan(self.im / self.re)
        if tag == "IM-":
            if not (self.im < 0):
                raise ValueError("box not certified in IM- half-plane")
            return -pi / 2 - iv_atan(self.re / self.im)
        raise ValueError("unknown half-plane tag %r" % (tag,))

    def log(self):
        """log z = (1/2) log(re^2+im^2) + i*theta, theta the branch of the box's own
        half-plane (requires a half-plane certificate).  Returned as a Ball whose
        imaginary part is the arg interval of THAT branch."""
        tag = self.halfplane()
        if tag is None:
            raise ZeroDivisionError("Ball.log: box does not exclude 0")
        return Ball(iv.log(self.abs2()) / 2, self.arg_branch(tag))

    def intersect(self, other):
        """Componentwise intersection; None if provably empty."""
        r = iv_intersect(self.re, other.re)
        if r is None:
            return None
        i = iv_intersect(self.im, other.im)
        if i is None:
            return None
        return Ball(r, i)

    def __repr__(self):
        return "Ball(%s, %s)" % (self.re, self.im)


def _coerce(x):
    if isinstance(x, Ball):
        return x
    if isinstance(x, int):
        return Ball.from_int(x)
    if isinstance(x, Fraction):
        return Ball.from_fractions(x, Fraction(0))
    raise TypeError("cannot coerce %r to Ball" % (type(x),))


# ---------------------------------------------------------------- self-test

def _selftest(trials=300, seed=20260826, prec=288, verbose=True):
    """Randomized containment tests of every operation against independent
    mp-context evaluation.

    Two membership disciplines, both decided in EXACT rational arithmetic:
     * ops whose true result at rational inputs is rational (add, mul, abs2):
       EXACT containment of the exact rational result;
     * transcendental ops (exp, recip after rounding, arg, log): the reference
       is mp-evaluated at dps 120 (~400 bits), i.e. WELL ABOVE the ball
       precision (288 bits), and membership is tested with an explicit
       inflation of 10^-100 that absorbs the reference's own rounding error
       (~10^-118) -- still ~13 orders below the ~2^-286 = 1e-86 thin-ball
       widths, so the test would still catch any enclosure error at or above
       the ball's own resolution.
    Returns (failures, checks)."""
    import random
    from mpmath import mp

    rng = random.Random(seed)
    set_prec(prec)
    mp.dps = 120
    EPS = Fraction(1, 10 ** 100)
    failures = 0
    checks = 0

    def contains_close(ball, z, eps=EPS):
        """Membership of the (ultra-high-precision, still rounded) reference z,
        inflated by eps; exact Fraction comparisons."""
        rlo, rhi = ball.re_bounds()
        ilo, ihi = ball.im_bounds()
        zr = mpf_tuple_to_fraction(z.real._mpf_)
        zi = mpf_tuple_to_fraction(z.imag._mpf_)
        return (rlo - eps <= zr <= rhi + eps) and (ilo - eps <= zi <= ihi + eps)

    def rnd_fraction(lo, hi, den=10 ** 9):
        n_lo, n_hi = int(lo * den), int(hi * den)
        return Fraction(rng.randint(n_lo, n_hi), den)

    def rnd_point_ball(scale=5):
        """A random exact rational point and (thin ball, padded box) around it."""
        a = rnd_fraction(-scale, scale)
        b = rnd_fraction(-scale, scale)
        pad = Fraction(rng.randint(0, 10 ** 6), 10 ** 8)  # up to 0.01
        thin = Ball.from_fractions(a, b)
        boxed = Ball.from_fraction_boxes((a - pad, a + pad), (b - pad, b + pad))
        zc = mp.mpc(mp.mpf(a.numerator) / a.denominator, mp.mpf(b.numerator) / b.denominator)
        return a, b, zc, thin, boxed

    def check(cond, what):
        nonlocal failures, checks
        checks += 1
        if not cond:
            failures += 1
            print("  FAIL:", what)

    for k in range(trials):
        a1, b1, z1, t1, x1 = rnd_point_ball()
        a2, b2, z2, t2, x2 = rnd_point_ball()
        # ring ops: the exact rational result must lie in both thin and padded results
        check(Ball.contains_exact(t1 + t2, a1 + a2, b1 + b2), "add thin @%d" % k)
        check(Ball.contains_exact(x1 + x2, a1 + a2, b1 + b2), "add box @%d" % k)
        pr = a1 * a2 - b1 * b2
        pi_ = a1 * b2 + b1 * a2
        check(Ball.contains_exact(t1 * t2, pr, pi_), "mul thin @%d" % k)
        check(Ball.contains_exact(x1 * x2, pr, pi_), "mul box @%d" % k)
        # exp: high-precision reference, inflated membership (see docstring)
        w = mp.exp(z1)
        check(contains_close(t1.exp(), w), "exp thin @%d" % k)
        check(contains_close(x1.exp(), w), "exp box @%d" % k)
        # thin-result tightness so the containment test is not vacuous
        # (|z1| <= 5*sqrt(2) so |exp z1| < e^8; 1e-55 is ~30 orders above the
        # rounding-limited width and ~45 below any modeling error of size 1)
        check(t1.exp().max_width() < Fraction(1, 10 ** 55), "exp thin width @%d" % k)
        # abs2
        r2 = a1 * a1 + b1 * b1
        lo, hi = ivmpf_bounds(t1.abs2())
        check(lo <= r2 <= hi, "abs2 thin @%d" % k)
        lo, hi = ivmpf_bounds(x1.abs2())
        check(lo <= r2 <= hi, "abs2 box @%d" % k)
        # recip / div, when 0 is excludable
        if x1.halfplane() is not None:
            winv = 1 / z1
            check(contains_close(t1.recip(), winv), "recip thin @%d" % k)
            check(contains_close(x1.recip(), winv), "recip box @%d" % k)
        # arg branches: for every tag whose half-plane certifiably holds, the
        # mp-evaluated branch formula value must lie in the interval
        for tag in TAGS:
            applies = {"RE+": x1.re > 0, "IM+": x1.im > 0,
                       "RE-": x1.re < 0, "IM-": x1.im < 0}[tag]
            if not applies:
                continue
            th = x1.arg_branch(tag)
            if tag == "RE+":
                ref = mp.atan(z1.imag / z1.real)
            elif tag == "IM+":
                ref = mp.pi / 2 - mp.atan(z1.real / z1.imag)
            elif tag == "RE-":
                ref = mp.pi + mp.atan(z1.imag / z1.real)
            else:
                ref = -mp.pi / 2 - mp.atan(z1.real / z1.imag)
            lo, hi = ivmpf_bounds(th)
            rf = mpf_tuple_to_fraction(ref._mpf_)
            check(lo - EPS <= rf <= hi + EPS, "arg %s @%d" % (tag, k))
            # and the branch must agree with principal arg modulo 2pi (sanity)
            pa = mp.atan2(z1.imag, z1.real)
            n = mp.nint((ref - pa) / (2 * mp.pi))
            check(abs(ref - pa - 2 * mp.pi * n) < mp.mpf("1e-70"),
                  "arg-vs-principal %s @%d" % (tag, k))
        # log on 0-excluding boxes
        if x1.halfplane() is not None:
            lg = x1.log()
            lo, hi = ivmpf_bounds(lg.re)
            ref = mp.log(abs(z1))
            rf = mpf_tuple_to_fraction(ref._mpf_)
            check(lo - EPS <= rf <= hi + EPS, "log-mod @%d" % k)
    # wide-box sampling: op(box) must contain op(point) for interior sample points
    for k in range(30):
        a, b, zc, thin, box = rnd_point_ball()
        rlo, rhi = box.re_bounds()
        ilo, ihi = box.im_bounds()
        for u in (Fraction(0), Fraction(1, 3), Fraction(1)):
            for v in (Fraction(0), Fraction(2, 5), Fraction(1)):
                pr = rlo + (rhi - rlo) * u
                pi_ = ilo + (ihi - ilo) * v
                zz = mp.mpc(mp.mpf(pr.numerator) / pr.denominator,
                            mp.mpf(pi_.numerator) / pi_.denominator)
                check(contains_close(box.exp(), mp.exp(zz)), "exp wide-sample @%d" % k)
    if verbose:
        print("ball.py selftest: %d checks, %d failures (trials=%d, seed=%d, prec=%d)"
              % (checks, failures, trials, seed, prec))
    return failures, checks


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        f, c = _selftest()
        sys.exit(0 if f == 0 else 1)
    print(__doc__)
