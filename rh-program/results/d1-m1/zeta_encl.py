"""zeta_encl.py -- rigorous complex-ball enclosures of the Riemann zeta function
by Euler-Maclaurin summation with a fully derived, explicit remainder bound.

D1 M1 v1, mpmath-ball producer leg (D-R3).  UNTRUSTED producer-side code; output
enters the certified statement only through H-ENCL (FORMAT.md sec. 8.1).

Standing order 5 (nothing load-bearing from memory): the remainder bound used
below is DERIVED here from first principles.  It is a Backlund-style bound with
constant 2 instead of the classical constant 1 -- the elementary derivation
below gives 2; the sharper classical constant needs an additional
alternating-remainder argument that is not reproduced here, so it is NOT used.
Every quantity in the bound is either exact rational arithmetic or a certified
interval computation; the one classical ingredient that is usually quoted
(sup of the Bernoulli polynomial deviation) is instead CERTIFIED NUMERICALLY at
run time by exact rational interval evaluation of the polynomial itself, so no
Bernoulli-polynomial inequality is trusted from the literature.

=============================================================================
DERIVATION (complete; each step checkable)
=============================================================================

Notation.  B_j are the Bernoulli numbers (B_0 = 1, B_1 = -1/2, B_2 = 1/6, ...,
defined by the recursion sum_{j=0}^{n} C(n+1, j) B_j = 0 for n >= 1, which the
code verifies EXACTLY for every index it uses).  B_j(x) are the Bernoulli
polynomials, B_j(x) = sum_{i=0}^{j} C(j, i) B_i x^{j-i}; the code verifies
exactly, coefficient by coefficient, that B_j'(x) = j*B_{j-1}(x) and
B_j(0) = B_j, and (for j >= 2) B_j(1) = B_j.  Bbar_j(x) := B_j({x}) is the
1-periodization ({x} = fractional part); for j >= 2 it is continuous because
B_j(0) = B_j(1), and Bbar_j'(x) = j*Bbar_{j-1}(x) on every open interval
(n, n+1), while for j >= 3 the continuous function Bbar_j/(j) is a piecewise-C^1
antiderivative of Bbar_{j-1} on all of R (continuity at the integer joints is
exactly B_j(0) = B_j(1)), so the fundamental theorem of calculus applies to it
across integers.  Odd Bernoulli numbers vanish: B_{2k+1} = 0 for k >= 1 (also
verified exactly by the recursion computation for the indices used).

STEP 1 (the basic identity).  For f in C^1[N, M], integers N < M:
    integral over [n, n+1] of (x - n - 1/2) f'(x) dx
      = [(x - n - 1/2) f(x)]_n^{n+1} - integral of f
      = (f(n) + f(n+1))/2 - integral_n^{n+1} f(x) dx        (parts).
Summing n = N..M-1, with Bbar_1(x) = x - n - 1/2 on (n, n+1):
    sum_{n=N}^{M} f(n)
      = integral_N^M f + (f(N) + f(M))/2 + integral_N^M Bbar_1(x) f'(x) dx.  (E0)

STEP 2 (iterate; two integrations by parts per Bernoulli pair).  Using the
antiderivative relations above, for k >= 0 and f in C^{2k+2}:
  (A) integral_N^M (Bbar_{2k+1}/(2k+1)!) f^{(2k+1)} dx
        = [ (Bbar_{2k+2}/(2k+2)!) f^{(2k+1)} ]_N^M
          - integral_N^M (Bbar_{2k+2}/(2k+2)!) f^{(2k+2)} dx
        = (B_{2k+2}/(2k+2)!) (f^{(2k+1)}(M) - f^{(2k+1)}(N))
          - integral_N^M (Bbar_{2k+2}/(2k+2)!) f^{(2k+2)} dx,
      because Bbar_{2k+2} = B_{2k+2} at integers;
  (B) - integral_N^M (Bbar_{2k+2}/(2k+2)!) f^{(2k+2)} dx
        = - [ (Bbar_{2k+3}/(2k+3)!) f^{(2k+2)} ]_N^M
          + integral_N^M (Bbar_{2k+3}/(2k+3)!) f^{(2k+3)} dx
        = 0 + integral_N^M (Bbar_{2k+3}/(2k+3)!) f^{(2k+3)} dx,
      because Bbar_{2k+3} at integers equals B_{2k+3} = 0 (odd index >= 3).
Applying (A) then (B) repeatedly to the last term of (E0), starting from
integral Bbar_1 f' = integral (Bbar_1/1!) f^{(1)}, gives by induction, for any
m >= 0 and f in C^{2m+1}:
    sum_{n=N}^{M} f(n) = integral_N^M f + (f(N) + f(M))/2
        + sum_{k=1}^{m} (B_{2k}/(2k)!) (f^{(2k-1)}(M) - f^{(2k-1)}(N))
        + integral_N^M (Bbar_{2m+1}(x)/(2m+1)!) f^{(2m+1)}(x) dx.          (EM)

STEP 3 (specialize; let M -> infinity).  Take f(x) = x^{-s}, s = sigma + it,
first with sigma > 1.  Derivatives: f^{(j)}(x) = (-1)^j (s)_j x^{-s-j} with the
rising factorial (s)_j = s (s+1) ... (s+j-1).  As M -> infinity every M-term in
(EM) tends to 0 (all involve M^{-sigma-j}, sigma > 1) and both remaining
integrals converge absolutely; therefore
    sum_{n=N}^{infty} n^{-s}
      = N^{1-s}/(s-1) + N^{-s}/2
        + sum_{k=1}^{m} (B_{2k}/(2k)!) (s)_{2k-1} N^{-s-2k+1} + R_{N,m}(s),  (T)
    R_{N,m}(s) = - ((s)_{2m+1}/(2m+1)!)
                   * integral_N^infty Bbar_{2m+1}(x) x^{-s-2m-1} dx,
using integral_N^infty x^{-s} dx = N^{1-s}/(s-1),
-f^{(2k-1)}(N) = +(s)_{2k-1} N^{-s-2k+1}  ((-1)^{2k-1} = -1), and
f^{(2m+1)}(x) = -(s)_{2m+1} x^{-s-2m-1}.  Adding the initial segment:
    zeta(s) = sum_{n=1}^{N-1} n^{-s} + [right side of (T)].               (Z)

STEP 4 (analytic continuation).  For fixed N, m the right side of (Z) minus the
remainder is an elementary analytic function of s on C minus {1}, and the
remainder integral converges locally uniformly for sigma > -2m (indeed
|Bbar_{2m+1}| is bounded and the integrand is O(x^{-sigma-2m-1})), hence is
analytic there.  Both sides of (Z) agree on sigma > 1 and both are analytic on
{sigma > -2m} minus {1}; by the identity theorem (Z) holds on all of
{sigma > -2m, s != 1}.  This leg only ever evaluates in 0 < sigma < 1, where
every m >= 1 qualifies.

STEP 5 (the remainder bound).  Let G(x) := (Bbar_{2m+2}(x) - B_{2m+2})/(2m+2).
Then G is continuous, G' = Bbar_{2m+1} across integers (antiderivative relation
plus continuity, as set out in the Notation), G(N) = 0, and
    |G(x)| <= C_{2m+2}/(2m+2),   C_j := sup_{x in [0,1]} |B_j(x) - B_j|,
by periodicity.  Integrating by parts (boundary term at infinity vanishes since
sigma + 2m + 1 > 0 and G is bounded; at x = N it vanishes since G(N) = 0):
    integral_N^infty Bbar_{2m+1}(x) x^{-s-2m-1} dx
      = (s + 2m + 1) * integral_N^infty G(x) x^{-s-2m-2} dx,
so, taking absolute values under the integral,
    |R_{N,m}(s)| <= (|(s)_{2m+1}| / (2m+1)!) * |s + 2m + 1|
                    * (C_{2m+2}/(2m+2)) * integral_N^infty x^{-sigma-2m-2} dx
      = |(s)_{2m+1}| * |s + 2m + 1| * C_{2m+2}
        / ( (2m+1)! * (2m+2) * (sigma + 2m + 1) ) * N^{-sigma-2m-1}.       (RB)
Validity: sigma + 2m + 1 > 0 (trivial in the strip).  Relation to the classical
Backlund bound: C_{2m+2} <= 2|B_{2m+2}| (from |Bbar| <= |B| at even index --
NOT assumed here; the code computes a certified C_{2m+2} directly), and
|first omitted term| = |B_{2m+2}/(2m+2)! * (s)_{2m+1} * N^{-s-2m-1}|, so (RB)
is at most  (C_{2m+2}/|B_{2m+2}|) * |(s+2m+1)/(sigma+2m+1)| * |first omitted|,
i.e. the classical shape with constant C_{2m+2}/|B_{2m+2}| (~ 2 in practice)
in place of Backlund's 1.  The factor is paid, never assumed away.

STEP 6 (certification of C_j).  B_j(x) - B_j is a polynomial with EXACT
rational coefficients (built from recursion-verified Bernoulli numbers).  The
code evaluates it over [0, 1] split into 512 subintervals by exact rational
interval Horner (all endpoints Fractions; interval product by 4-corner
min/max), and takes the maximum absolute bound: a rigorous upper bound C_j^ub
with NO analytic input.  A midpoint evaluation supplies a lower bound to
confirm the upper bound is within a factor ~1.01 of sharp (reported, not used).

STEP 7 (interval evaluation).  Every term of (Z) is evaluated in the complex
ball arithmetic of ball.py with s a BOX (Re and Im intervals): n^{-s} =
exp(-s log n) with exact integer logs, N^{1-s}/(s-1) with certified complex
reciprocal (the (s-1) box excludes 0 whenever sigma_hi < 1, which the caller's
rectangle guarantees; recip raises otherwise), rational coefficients
B_{2k}/(2k)!/N^{2k-1} as exact-fraction intervals, and the remainder (RB)
evaluated with upper bounds throughout (moduli upper endpoints, sigma lower
endpoint) and added as the box [-r, r] x [-r, r].  Inclusion monotonicity of
every ball op then gives: FOR EVERY s IN THE INPUT BOX, zeta(s) lies in the
output box.  That is exactly the per-segment statement H-ENCL(a) needs.

Parameter policy (N, m): NEVER load-bearing -- (Z)+(RB) are valid for every
N >= 1, m >= 1 in the strip; parameters only tune the width.  Defaults:
m = 14, N = max(20, ceil(0.5*(t_max + 2m + 1))), chosen so the term ratio
(|s| + 2m + 1)/(2 pi N) stays ~< 1/3.  Floats appear ONLY in this parameter
heuristic, never in any bound.

VALIDATION (run: python3 zeta_encl.py --validate): >= 200 random points s with
1/2 < sigma < 1, |t| <= 200: the enclosure must CONTAIN mp.zeta(s) computed
independently at dps 100 (mpmath's own float pipeline, a different code path
from libmpi interval arithmetic), membership decided exactly on Fractions with
inflation 10^-80 for the reference's own rounding; width statistics reported.
Plus wide boxes with interior sample points, and the a = 1 Hurwitz cross-check
lives in hurwitz_encl.py.
"""

import math
from fractions import Fraction

from mpmath import iv

from ball import iv_exp, iv_log   # outward-inflated transcendental endpoints (AUDIT F-1, repair R1)

from ball import (Ball, iv_from_fraction, iv_from_fraction_pair, iv_from_int,
                  ivmpf_bounds, set_prec)

__all__ = ["zeta_ball", "bern_exact", "bernoulli_poly_coeffs", "c_sup", "pow_int_neg"]


# ---------------------------------------------------------------- exact Bernoulli layer

_BERN_CACHE = {}


def bern_exact(n):
    """Exact Bernoulli number B_n as a Fraction, VERIFIED against the defining
    recursion sum_{j=0}^{k} C(k+1, j) B_j = 0 (k >= 1) in exact arithmetic.
    (mpmath.bernfrac supplies the candidate; the recursion check certifies it,
    so bernfrac is not trusted.)"""
    if n in _BERN_CACHE:
        return _BERN_CACHE[n]
    import mpmath
    # build all B_0..B_n and verify the recursion for every k up to n
    vals = []
    for j in range(n + 1):
        p, q = mpmath.bernfrac(j)
        vals.append(Fraction(p, q))
    if vals[0] != 1:
        raise ArithmeticError("B_0 != 1 from bernfrac")
    for k in range(1, n + 1):
        acc = Fraction(0)
        for j in range(k):
            acc += math.comb(k + 1, j) * vals[j]
        # recursion: sum_{j=0}^{k} C(k+1,j) B_j = 0  =>  C(k+1,k) B_k = -acc
        if Fraction(math.comb(k + 1, k)) * vals[k] != -acc:
            raise ArithmeticError("Bernoulli recursion FAILED at k=%d" % k)
    for j, v in enumerate(vals):
        _BERN_CACHE[j] = v
    return _BERN_CACHE[n]


_BPOLY_CACHE = {}


def bernoulli_poly_coeffs(n):
    """Coefficients [c_0, ..., c_n] (ascending powers) of B_n(x), exact Fractions,
    with exact verification of B_n'(x) = n B_{n-1}(x) (coefficientwise),
    B_n(0) = B_n, and (n >= 2) B_n(1) = B_n."""
    if n in _BPOLY_CACHE:
        return _BPOLY_CACHE[n]
    coeffs = [Fraction(0)] * (n + 1)
    for i in range(n + 1):           # B_n(x) = sum_i C(n,i) B_i x^{n-i}
        coeffs[n - i] += math.comb(n, i) * bern_exact(i)
    # exact self-checks
    if coeffs[0] != bern_exact(n):
        raise ArithmeticError("B_%d(0) != B_%d" % (n, n))
    if n >= 2 and sum(coeffs) != bern_exact(n):
        raise ArithmeticError("B_%d(1) != B_%d" % (n, n))
    if n >= 1:
        lower = bernoulli_poly_coeffs(n - 1) if n - 1 not in _BPOLY_CACHE else _BPOLY_CACHE[n - 1]
        if n - 1 not in _BPOLY_CACHE:
            _BPOLY_CACHE[n - 1] = lower
        for j in range(n):           # derivative: (j+1) c_{j+1} = n * lower_j
            if Fraction(j + 1) * coeffs[j + 1] != Fraction(n) * lower[j]:
                raise ArithmeticError("B_%d' != %d B_%d at power %d" % (n, n, n - 1, j))
    _BPOLY_CACHE[n] = coeffs
    return coeffs


def _interval_horner(coeffs, lo, hi):
    """Exact rational interval Horner: enclosure of {P(x) : x in [lo, hi]}.
    Interval product by 4-corner min/max (correct for any signs)."""
    alo = ahi = coeffs[-1]
    for c in reversed(coeffs[:-1]):
        p1, p2, p3, p4 = alo * lo, alo * hi, ahi * lo, ahi * hi
        alo, ahi = min(p1, p2, p3, p4) + c, max(p1, p2, p3, p4) + c
    return alo, ahi


_CSUP_CACHE = {}


def c_sup(n, pieces=512):
    """Certified upper bound on C_n = sup_{[0,1]} |B_n(x) - B_n| by exact
    rational interval evaluation on `pieces` subintervals (STEP 6).
    Returns (upper_bound, lower_bound) Fractions; only the upper bound is used."""
    if n in _CSUP_CACHE:
        return _CSUP_CACHE[n]
    coeffs = list(bernoulli_poly_coeffs(n))
    coeffs[0] -= bern_exact(n)          # P(x) = B_n(x) - B_n
    ub = Fraction(0)
    lb = Fraction(0)
    for j in range(pieces):
        lo, hi = Fraction(j, pieces), Fraction(j + 1, pieces)
        plo, phi = _interval_horner(coeffs, lo, hi)
        ub = max(ub, abs(plo), abs(phi))
        # midpoint exact evaluation for the (unused, reported) lower bound
        mid = (lo + hi) / 2
        acc = Fraction(0)
        for c in reversed(coeffs):
            acc = acc * mid + c
        lb = max(lb, abs(acc))
    _CSUP_CACHE[n] = (ub, lb)
    return _CSUP_CACHE[n]


# ---------------------------------------------------------------- integer-log cache

_LOG_CACHE = {}


def _log_int(n):
    key = (n, iv.prec)
    if key not in _LOG_CACHE:
        _LOG_CACHE[key] = iv_log(iv_from_int(n))
    return _LOG_CACHE[key]


def pow_int_neg(n, s_ball):
    """Ball enclosure of n^{-s} = exp(-s log n) for integer n >= 1, s a Ball."""
    ln = _log_int(n)
    return Ball((-s_ball.re) * ln, (-s_ball.im) * ln).exp()


# ---------------------------------------------------------------- the enclosure

def _auto_params(s_ball, m=None, N=None):
    if m is None:
        m = 14
    if N is None:
        tlo, thi = s_ball.im_bounds()
        tmax = max(abs(tlo), abs(thi))
        N = max(20, int(math.ceil(0.5 * (float(tmax) + 2 * m + 1))))
    return N, m


def zeta_ball(s_ball, N=None, m=None):
    """Rigorous enclosure of {zeta(s) : s in the input box}, by (Z) + (RB).

    Requirements (raised on violation, never silently assumed):
      * sigma_lo > 0  (scope guard for this leg; (Z) itself holds for
        sigma > -2m),
      * the (s - 1) box excludes 0 (certified inside recip; guaranteed by any
        caller whose rectangle has sigma_hi < 1).
    """
    N, m = _auto_params(s_ball, m, N)
    slo, _shi = s_ball.re_bounds()
    if not slo > 0:
        raise ValueError("zeta_ball scope guard: need sigma_lo > 0, got %s" % (slo,))

    # ---- partial sum  sum_{n=1}^{N-1} n^{-s}
    total = Ball.from_int(1)                    # n = 1 term
    for n in range(2, N):
        total = total + pow_int_neg(n, s_ball)

    # ---- N^{1-s}/(s-1)
    lnN = _log_int(N)
    one_minus_s = Ball.from_int(1) - s_ball
    n_pow_1ms = Ball(one_minus_s.re * lnN, one_minus_s.im * lnN).exp()
    total = total + n_pow_1ms * (s_ball - Ball.from_int(1)).recip()

    # ---- N^{-s}/2 and the Bernoulli sum
    NS = pow_int_neg(N, s_ball)
    total = total + NS.scale_iv(iv_from_fraction(Fraction(1, 2)))
    rising = s_ball                              # (s)_1
    for k in range(1, m + 1):
        if k >= 2:
            j = 2 * k - 3
            rising = rising * (s_ball + Ball.from_int(j)) * (s_ball + Ball.from_int(j + 1))
        c_k = bern_exact(2 * k) / math.factorial(2 * k) / Fraction(N ** (2 * k - 1))
        total = total + (NS * rising).scale_iv(iv_from_fraction(c_k))

    # ---- remainder bound (RB), all quantities as certified upper bounds
    # |(s)_{2m+1}| <= prod_{j=0}^{2m} sup|s+j|
    prod_ub = iv_from_int(1)
    for j in range(0, 2 * m + 1):
        prod_ub = prod_ub * (s_ball + Ball.from_int(j)).abs_iv()
    _, prod_ub_hi = ivmpf_bounds(prod_ub)
    _, s2m1_hi = ivmpf_bounds((s_ball + Ball.from_int(2 * m + 1)).abs_iv())
    c_ub, _c_lb = c_sup(2 * m + 2)
    denom = Fraction(math.factorial(2 * m + 1)) * (2 * m + 2) * (slo + 2 * m + 1)
    # N^{-(sigma_lo + 2m + 1)} upper bound, via interval exp of an exact exponent
    expo = iv_from_fraction(-(slo + 2 * m + 1)) * lnN
    _, npow_hi = ivmpf_bounds(iv_exp(expo))
    r = prod_ub_hi * s2m1_hi * c_ub * npow_hi / denom
    pad = iv_from_fraction_pair(-r, r)
    return total + Ball(pad, pad)


# ---------------------------------------------------------------- validation

def _validate(points=200, seed=1859, prec=288, verbose=True):
    import random
    from mpmath import mp

    rng = random.Random(seed)
    set_prec(prec)
    mp.dps = 100
    EPS = Fraction(1, 10 ** 80)
    failures = 0
    widths = []

    def frac(lo, hi, den=10 ** 6):
        return Fraction(rng.randint(int(lo * den), int(hi * den)), den)

    print("zeta_encl validation: %d random points, sigma in (0.501, 0.999), |t| <= 200,"
          " iv prec %d bits, reference mp.zeta at dps 100" % (points, prec))
    for k in range(points):
        sig = frac(0.501, 0.999)
        t = frac(-200, 200)
        s = Ball.from_fractions(sig, t)
        z = zeta_ball(s)
        ref = mp.zeta(mp.mpc(mp.mpf(sig.numerator) / sig.denominator,
                             mp.mpf(t.numerator) / t.denominator))
        rlo, rhi = z.re_bounds()
        ilo, ihi = z.im_bounds()
        from ball import mpf_tuple_to_fraction as m2f
        okc = (rlo - EPS <= m2f(ref.real._mpf_) <= rhi + EPS and
               ilo - EPS <= m2f(ref.imag._mpf_) <= ihi + EPS)
        w = z.max_width()
        widths.append(w)
        if not okc:
            failures += 1
            print("  CONTAINMENT FAIL at s = %s + %si" % (sig, t))
    widths.sort()
    med = widths[len(widths) // 2]
    wmax = widths[-1]
    print("  containment: %d/%d PASS" % (points - failures, points))
    print("  enclosure widths: median %.3e, max %.3e" % (float(med), float(wmax)))

    # wide boxes: 20 boxes, 9 interior sample points each
    box_fail = 0
    for k in range(20):
        sig = frac(0.55, 0.95)
        t = frac(-150, 150)
        dsig = Fraction(rng.randint(1, 200), 10 ** 4)   # up to 0.02
        dt = Fraction(rng.randint(1, 200), 10 ** 4)
        s = Ball.from_fraction_boxes((sig, sig + dsig), (t, t + dt))
        z = zeta_ball(s)
        rlo, rhi = z.re_bounds()
        ilo, ihi = z.im_bounds()
        from ball import mpf_tuple_to_fraction as m2f
        for u in (Fraction(0), Fraction(1, 2), Fraction(1)):
            for v in (Fraction(0), Fraction(1, 2), Fraction(1)):
                ps = sig + dsig * u
                pt = t + dt * v
                ref = mp.zeta(mp.mpc(mp.mpf(ps.numerator) / ps.denominator,
                                     mp.mpf(pt.numerator) / pt.denominator))
                ok = (rlo - EPS <= m2f(ref.real._mpf_) <= rhi + EPS and
                      ilo - EPS <= m2f(ref.imag._mpf_) <= ihi + EPS)
                if not ok:
                    box_fail += 1
                    print("  BOX CONTAINMENT FAIL at box (%s,%s)+(%s,%s) sample (%s,%s)"
                          % (sig, t, dsig, dt, u, v))
    print("  wide-box sampling: %d boxes x 9 points, %d failures" % (20, box_fail))

    # report the certified Bernoulli-deviation constant for the default m
    ub, lb = c_sup(2 * 14 + 2)
    b = abs(bern_exact(2 * 14 + 2))
    print("  certified C_30 = %.6e (lower bound %.6e; C_30 / |B_30| = %.4f; "
          "classical comparison constant 2)" % (float(ub), float(lb), float(ub / b)))
    return failures + box_fail


if __name__ == "__main__":
    import sys
    if "--validate" in sys.argv:
        pts = 200
        for a in sys.argv:
            if a.startswith("--points="):
                pts = int(a.split("=", 1)[1])
        rc = _validate(points=pts)
        sys.exit(0 if rc == 0 else 1)
    print(__doc__)
