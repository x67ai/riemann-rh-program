#!/usr/bin/env python3
"""Capability + honesty check for the Arb/FLINT producer leg (D1 M1 v1, Session 8).

Verifies, LIVE, everything producer_arb.py relies on from python-flint:

  A. version + module identity;
  B. precision control (ctx.prec) actually changes enclosure widths;
  C. acb zeta (Riemann) and Hurwitz zeta (acb.zeta(a)) exist and return balls;
  D. balls are honest midpoint+radius objects: mid() and rad() are EXACT dyadics
     (man_exp() decomposition m*2^e with no hidden rounding), so the producer can
     do all scale-K integer conversion in EXACT Python integer arithmetic with no
     trust in any directed-rounding call;
  E. rounding direction of lower()/upper() (used only as a cross-check in the
     producer; the primary path is the exact mid/rad route) — verified against
     exact rational arithmetic on crafted cases where rounding must occur, in
     both signs;
  F. inclusion isotonicity spot-check: zeta evaluated on a WIDE input ball
     contains zeta at interior points (the property the segment-hull evaluation
     of producer_arb.py stands on), cross-validated against mpmath at higher
     precision (independent library, independent algorithm);
  G. atan2 on balls, pi as a ball, certified comparisons (needed for the
     argument rows);
  H. the DH residual: f_DH at the certified off-line zero
     rho_DH = 0.808517182456637 + 85.699348485377592i (direction file line 104)
     encloses a value of magnitude < 1e-12 — the live-fire target is real.

Every check prints PASS/FAIL and the script exits nonzero on any FAIL.
Run transcript: arb-capability-check-run.txt (same directory).

Trust status: this script is producer-side and UNTRUSTED, like everything on
the producer side of the W1 contract (FORMAT.md section 10). What it certifies
is only that the library behaves as the producer assumes; the trusted statement
is always "kernel-checked modulo displayed hypotheses".
"""

import sys
from fractions import Fraction

FAILURES = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f" -- {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)


# ---------------------------------------------------------------- A. version
import flint
from flint import arb, acb, fmpq, ctx

print("python-flint:", flint.__version__)
print("module file:", flint.__file__)
check("A1 version is 0.6.0 (recorded in arb-leg-notes.md)", flint.__version__ == "0.6.0",
      f"found {flint.__version__}")

# ------------------------------------------------------- B. precision control
ctx.prec = 64
w64 = acb("0.75", "100").zeta()
r64 = w64.real.rad().man_exp()
ctx.prec = 256
w256 = acb("0.75", "100").zeta()
r256 = w256.real.rad().man_exp()


def dyadic_frac(me):
    m, e = int(me[0]), int(me[1])
    return Fraction(m) * Fraction(2) ** e


check("B1 ctx.prec controls enclosure width",
      dyadic_frac(r256) < dyadic_frac(r64) / Fraction(10) ** 20,
      f"rad@64 = 2^{r64[1]}-class, rad@256 = 2^{r256[1]}-class")

# ------------------------------------------------- C. zeta + Hurwitz present
ctx.prec = 200
z = acb("0.75", "100").zeta()
check("C1 acb.zeta returns an acb ball", isinstance(z, acb))
h = acb("0.75", "100").zeta(acb(arb(fmpq(1, 5))))
check("C2 Hurwitz zeta via acb.zeta(a) returns an acb ball", isinstance(h, acb))
check("C3 acb.dirichlet_l also exposed (bonus, recorded)", hasattr(acb, "dirichlet_l"))

# ------------------------------------- D. exact mid/rad (the no-trust route)


def ball_to_exact_interval(x):
    """arb ball -> exact rational interval [mid - rad, mid + rad].

    Uses only man_exp() on mid() and rad(), both of which must be EXACT
    (is_exact() == True); everything after that is exact Python arithmetic.
    """
    m = x.mid()
    r = x.rad()
    assert m.is_exact() and r.is_exact(), "mid/rad not exact dyadics"
    mv = dyadic_frac(m.man_exp())
    rv = dyadic_frac(r.man_exp())
    assert rv >= 0
    return (mv - rv, mv + rv)


x = arb(1) / arb(3)
lo, hi = ball_to_exact_interval(x)
third = Fraction(1, 3)
check("D1 exact interval of arb(1)/arb(3) contains 1/3", lo <= third <= hi,
      f"width = {float(hi - lo):.3e}")
check("D2 mid() is exact", x.mid().is_exact())
check("D3 rad() is exact", x.rad().is_exact())
# zero-mantissa edge case
z0 = arb(0)
m0, e0 = z0.mid().man_exp()
check("D4 man_exp on exact zero returns (0, 0)", int(m0) == 0 and int(e0) == 0,
      f"({m0}, {e0})")
# negative value
xn = arb(-1) / arb(3)
lon, hin = ball_to_exact_interval(xn)
check("D5 exact interval works for negatives", lon <= Fraction(-1, 3) <= hin)
# fmpq constructor containment (used for exact rational -> ball conversion)
for (n, d) in [(1, 3), (-7, 11), (8569, 100), (123456789012345678901234567890, 7)]:
    xb = arb(fmpq(n, d))
    l2, h2 = ball_to_exact_interval(xb)
    check(f"D6 arb(fmpq({n},{d})) contains {n}/{d}", l2 <= Fraction(n, d) <= h2)

# --------------------------- E. lower()/upper() rounding-direction tests
# The producer's PRIMARY integer conversion is the exact mid/rad route above;
# lower()/upper() are used as a redundant cross-check. Verify their direction
# on cases where rounding MUST occur (1/3 is not dyadic at any precision).
for (n, d) in [(1, 3), (-1, 3), (2, 3), (-2, 3), (10, 7), (-10, 7)]:
    ctx.prec = 40
    xb = arb(n) / arb(d)
    lo_a = xb.lower()
    hi_a = xb.upper()
    check(f"E1 lower()/upper() of {n}/{d} ball are exact dyadics",
          lo_a.is_exact() and hi_a.is_exact())
    lov = dyadic_frac(lo_a.man_exp())
    hiv = dyadic_frac(hi_a.man_exp())
    q = Fraction(n, d)
    check(f"E2 lower() <= {n}/{d} <= upper()", lov <= q <= hiv,
          f"lo-q = {float(lov - q):.2e}, hi-q = {float(hiv - q):.2e}")
    check(f"E3 rounding actually occurred for {n}/{d} (strict on both sides)",
          lov < q < hiv)
ctx.prec = 200
# wide-ball case: arb from midpoint 2.5, radius 0.75 must have
# lower <= 1.75 and upper >= 3.25
xw = arb("2.5", "0.75")
low, hiw = ball_to_exact_interval(xw)
check("E4 wide ball [2.5 +/- 0.75]: exact interval covers [1.75, 3.25]",
      low <= Fraction(7, 4) and hiw >= Fraction(13, 4),
      f"[{float(low)}, {float(hiw)}]")

# -------------------------- F. inclusion isotonicity + mpmath cross-check
# Segment: sigma in [3/5, 7/10] at T = 10 (a bottom-edge segment of the
# planned zeta exclusion box). Hull ball via union of endpoint balls.
ctx.prec = 200
re_hull = arb(fmpq(3, 5)).union(arb(fmpq(7, 10)))
s_hull = acb(re_hull, arb(10))
z_hull = s_hull.zeta()
zr_lo, zr_hi = ball_to_exact_interval(z_hull.real)
zi_lo, zi_hi = ball_to_exact_interval(z_hull.imag)
print(f"     hull zeta box: Re [{float(zr_lo):.6f}, {float(zr_hi):.6f}], "
      f"Im [{float(zi_lo):.6f}, {float(zi_hi):.6f}]")

import mpmath  # independent library, used ONLY as a cross-check here
mpmath.mp.dps = 60
ok_all = True
for t in [Fraction(3, 5), Fraction(5, 8), Fraction(13, 20), Fraction(27, 40), Fraction(7, 10)]:
    v = mpmath.zeta(mpmath.mpc(mpmath.mpf(t.numerator) / t.denominator, 10))
    # rational enclosure of the mpmath value (mpmath is not interval arithmetic;
    # at dps 60 its error is far below the slack we test against)
    vr = Fraction(str(v.real))
    vi = Fraction(str(v.imag))
    inside = (zr_lo <= vr <= zr_hi) and (zi_lo <= vi <= zi_hi)
    ok_all = ok_all and inside
    print(f"     mpmath zeta({float(t):.4f}+10i) = {complex(v):.8f} inside hull box: {inside}")
check("F1 hull ball contains independently computed interior values", ok_all)

# Point-value cross-check at higher precision: Arb ball vs mpmath dps 80.
# mpmath is NOT exact: mpf('0.65') is a binary rounding of 13/20 (error ~1e-81
# at dps 80) and the printed decimal is itself rounded, so the honest test is
# agreement WITHIN the ball radius plus an explicit decimal slack — never exact
# containment of an approximate value in an exact-width ball. (First run of
# this script used exact containment and float 0.65, and failed for exactly
# those two harness reasons; recorded in arb-leg-notes.md.)
ctx.prec = 300
zp = acb(arb(fmpq(13, 20)), arb(10)).zeta()
pr_lo, pr_hi = ball_to_exact_interval(zp.real)
pi_lo, pi_hi = ball_to_exact_interval(zp.imag)
mpmath.mp.dps = 80
vp = mpmath.zeta(mpmath.mpc(mpmath.mpf(13) / 20, 10))
vpr = Fraction(mpmath.nstr(vp.real, 75))
vpi = Fraction(mpmath.nstr(vp.imag, 75))
slack = Fraction(1, 10 ** 70)  # mpf(13)/20 rounding + zeta error + print rounding
check("F2 point ball (prec 300) agrees with mpmath dps-80 value within rad+1e-70",
      pr_lo - slack <= vpr <= pr_hi + slack and pi_lo - slack <= vpi <= pi_hi + slack,
      f"ball widths {float(pr_hi - pr_lo):.2e}/{float(pi_hi - pi_lo):.2e}")

# ------------------------------------------- G. atan2, pi, comparisons
ctx.prec = 200
a = arb.atan2(arb(1), arb(1))
al, ah = ball_to_exact_interval(a)
# pi/4 = 0.7853981633974483... ; compare against mpmath at dps 60
# dps 100 makes the mpmath decimal error ~1e-98, far below the prec-200 ball
# width ~6e-61, so containment-with-slack is decisive (same harness lesson as F2)
mpmath.mp.dps = 100
gslack = Fraction(1, 10 ** 95)
pi4 = Fraction(mpmath.nstr(mpmath.pi / 4, 98))
check("G1 arb.atan2(1,1) encloses pi/4 (within decimal slack)",
      al - gslack <= pi4 <= ah + gslack)
p = arb.pi()
pl, ph = ball_to_exact_interval(p)
piv = Fraction(mpmath.nstr(mpmath.pi, 98))
check("G2 arb.pi() encloses pi (within decimal slack)",
      pl - gslack <= piv <= ph + gslack)
# certified comparisons: True only when certain; ambiguous -> False both ways
check("G3 certified strict comparison (positive ball > 0)", bool(arb("1", "0.5") > arb(0)))
straddle = arb("0", "1")
check("G4 straddling ball: neither > 0 nor < 0 certified",
      (not bool(straddle > arb(0))) and (not bool(straddle < arb(0))))

# ------------------------------------------------------ H. the DH residual
# f_DH(s) = 5^{-s} [ zeta(s,1/5) + kap*zeta(s,2/5) - kap*zeta(s,3/5) - zeta(s,4/5) ]
# kap = (sqrt(10-2*sqrt5) - 2)/(sqrt5 - 1)
# (quoted verbatim from results/ccm-dh-test/dh.py lines 5-8 via FORMAT.md 9.2)
ctx.prec = 300


def f_dh(s):
    sqrt5 = arb(5).sqrt()
    kap = ((arb(10) - 2 * sqrt5).sqrt() - 2) / (sqrt5 - 1)
    kapc = acb(kap)
    terms = (s.zeta(acb(arb(fmpq(1, 5))))
             + kapc * s.zeta(acb(arb(fmpq(2, 5))))
             - kapc * s.zeta(acb(arb(fmpq(3, 5))))
             - s.zeta(acb(arb(fmpq(4, 5)))))
    return acb(5) ** (-s) * terms


rho = acb(arb("0.808517182456637"), arb("85.699348485377592"))
fr = f_dh(rho)
fr_lo, fr_hi = ball_to_exact_interval(fr.real)
fi_lo, fi_hi = ball_to_exact_interval(fr.imag)
mag_sq_hi = max(fr_lo ** 2, fr_hi ** 2) + max(fi_lo ** 2, fi_hi ** 2)
check("H1 |f_DH(rho_DH)|^2 upper bound < 1e-24 (residual real, ball-certified)",
      mag_sq_hi < Fraction(1, 10 ** 24), f"|f|^2 <= {float(mag_sq_hi):.3e}")

# ---------------------------------------------------------------- verdict
print()
if FAILURES:
    print("RESULT: FAIL --", len(FAILURES), "check(s) failed:", ", ".join(FAILURES))
    sys.exit(1)
print("RESULT: ALL CHECKS PASS")
