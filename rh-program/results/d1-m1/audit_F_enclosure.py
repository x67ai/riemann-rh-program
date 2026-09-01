"""audit_F_enclosure.py -- AUDIT F (Session 14, 2026-09-02): fresh-seed enclosure
honesty test of every M1 v1 evaluator against dps-100 mpmath reference values.

Independent of Session 8's validation runs: own seeds, own point sets, edge
regimes (sigma near 1/2, sigma near 1, |t| near 10^4 = the largest height in the
acceptance suite, and f_DH at its off-line zero, including a 40-digit refined
zero computed here).  Membership decided EXACTLY on Fractions, with an inflation
of 10^-80 for the reference's own rounding (reference dps 100 -> ~1e-100
relative error; enclosure widths are >= 1e-19, so the inflation is 60 orders
below anything an evaluator bug would produce).

Evaluators under test:
  mp leg : zeta_encl.zeta_ball, hurwitz_encl.hurwitz_ball, producer_mp.f_dh_ball
  arb leg: producer_arb.eval_zeta, producer_arb.eval_fdh (ball -> exact
           [mid-rad, mid+rad] via producer_arb.ball_interval)

Any reference value outside its enclosure is a FATAL finding (task item 2).
Run from results/d1-m1/:  python3 audit_F_enclosure.py
"""
import random
import sys
import time
from fractions import Fraction

from mpmath import mp, iv
import mpmath

from ball import Ball, ivmpf_bounds, set_prec, mpf_tuple_to_fraction as m2f
from zeta_encl import zeta_ball
from hurwitz_encl import hurwitz_ball
from producer_mp import f_dh_ball, RHO_DH_RE, RHO_DH_IM
import producer_arb
from flint import acb, arb, ctx, fmpq

EPS = Fraction(1, 10 ** 80)
SEED = 20260902
FAILS = []
COUNTS = {}


def frac_from_mpf(x):
    return m2f(x._mpf_)


def mp_point(sig, t):
    return mp.mpc(mp.mpf(sig.numerator) / sig.denominator, mp.mpf(t.numerator) / t.denominator)


def ref_zeta(sig, t):
    mp.dps = 100
    return mp.zeta(mp_point(sig, t))


def ref_hurwitz(sig, t, a):
    mp.dps = 100
    return mp.zeta(mp_point(sig, t), mp.mpf(a.numerator) / a.denominator)


def ref_fdh(sig, t):
    mp.dps = 100
    s = mp_point(sig, t)
    kap = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
    return mp.power(5, -s) * (mp.zeta(s, mp.mpf(1) / 5) + kap * mp.zeta(s, mp.mpf(2) / 5)
                              - kap * mp.zeta(s, mp.mpf(3) / 5) - mp.zeta(s, mp.mpf(4) / 5))


def contains_ball(z, ref, tag):
    rlo, rhi = z.re_bounds()
    ilo, ihi = z.im_bounds()
    rr, ri = frac_from_mpf(ref.real), frac_from_mpf(ref.imag)
    ok = (rlo - EPS <= rr <= rhi + EPS) and (ilo - EPS <= ri <= ihi + EPS)
    COUNTS[tag] = COUNTS.get(tag, [0, 0])
    COUNTS[tag][1] += 1
    if ok:
        COUNTS[tag][0] += 1
    else:
        FAILS.append((tag, str(z), str(ref)))
        print("  CONTAINMENT FAIL [%s]: ref=%s encl re=[%s,%s] im=[%s,%s]"
              % (tag, mpmath.nstr(ref, 30), float(rlo), float(rhi), float(ilo), float(ihi)))
    return ok, max(rhi - rlo, ihi - ilo)


def contains_acb(fb, ref, tag):
    rlo, rhi = producer_arb.ball_interval(fb.real)
    ilo, ihi = producer_arb.ball_interval(fb.imag)
    rr, ri = frac_from_mpf(ref.real), frac_from_mpf(ref.imag)
    ok = (rlo - EPS <= rr <= rhi + EPS) and (ilo - EPS <= ri <= ihi + EPS)
    COUNTS[tag] = COUNTS.get(tag, [0, 0])
    COUNTS[tag][1] += 1
    if ok:
        COUNTS[tag][0] += 1
    else:
        FAILS.append((tag, str(fb), str(ref)))
        print("  CONTAINMENT FAIL [%s]: ref=%s ball=%s" % (tag, mpmath.nstr(ref, 30), fb))
    return ok, max(rhi - rlo, ihi - ilo)


def rnd_frac(rng, lo, hi, den=10 ** 7):
    return Fraction(rng.randint(int(lo * den), int(hi * den)), den)


def regime_points(rng, regime, n):
    pts = []
    for _ in range(n):
        if regime == "generic":
            sig, t = rnd_frac(rng, 0.51, 0.99), rnd_frac(rng, -300, 300)
        elif regime == "sigma~1/2":
            sig, t = Fraction(1, 2) + rnd_frac(rng, 0.0000001, 0.001), rnd_frac(rng, -200, 200)
        elif regime == "sigma~1":
            sig, t = Fraction(1) - rnd_frac(rng, 0.0000001, 0.001), rnd_frac(rng, -200, 200)
        elif regime == "t~1e4":
            sig, t = rnd_frac(rng, 0.51, 0.99), rnd_frac(rng, 9990, 10001) * rng.choice([1, -1])
        elif regime == "t~85.7":
            sig, t = rnd_frac(rng, 0.51, 0.99), rnd_frac(rng, 85.5, 85.9)
        pts.append((sig, t))
    return pts


def main():
    t0 = time.time()
    set_prec(288)
    ctx.prec = 300
    rng = random.Random(SEED)
    print("AUDIT F enclosure honesty: seed %d, EPS 1e-80, reference mpmath dps 100" % SEED)

    # ---------------- mp leg: zeta_ball
    for regime, n in (("generic", 60), ("sigma~1/2", 50), ("sigma~1", 50), ("t~1e4", 50)):
        widths = []
        tE = time.time()
        for sig, t in regime_points(rng, regime, n):
            z = zeta_ball(Ball.from_fractions(sig, t))
            ok, w = contains_ball(z, ref_zeta(sig, t), "zeta_ball/" + regime)
            widths.append(w)
        widths.sort()
        print("  zeta_ball %-10s n=%d  widths median %.2e max %.2e  (%.1fs)"
              % (regime, n, float(widths[n // 2]), float(widths[-1]), time.time() - tE))

    # ---------------- arb leg: eval_zeta (same regimes, fresh points)
    for regime, n in (("generic", 60), ("sigma~1/2", 50), ("sigma~1", 50), ("t~1e4", 50)):
        widths = []
        for sig, t in regime_points(rng, regime, n):
            s = acb(producer_arb.rat_ball(sig), producer_arb.rat_ball(t))
            ok, w = contains_acb(producer_arb.eval_zeta(s), ref_zeta(sig, t), "arb_zeta/" + regime)
            widths.append(w)
        widths.sort()
        print("  arb zeta  %-10s n=%d  widths median %.2e max %.2e"
              % (regime, n, float(widths[n // 2]), float(widths[-1])))

    # ---------------- mp leg: hurwitz_ball (DH shifts + random a), edge regimes
    shifts = [Fraction(j, 5) for j in (1, 2, 3, 4)]
    for regime, n in (("generic", 60), ("sigma~1/2", 50), ("sigma~1", 50), ("t~1e4", 24)):
        widths = []
        tE = time.time()
        for k, (sig, t) in enumerate(regime_points(rng, regime, n)):
            a = shifts[k % 4] if k % 2 == 0 else Fraction(rng.randint(1, 97), 97)
            z = hurwitz_ball(Ball.from_fractions(sig, t), a)
            ok, w = contains_ball(z, ref_hurwitz(sig, t, a), "hurwitz_ball/" + regime)
            widths.append(w)
        widths.sort()
        print("  hurwitz_ball %-10s n=%d widths median %.2e max %.2e  (%.1fs)"
              % (regime, n, float(widths[n // 2]), float(widths[-1]), time.time() - tE))

    # ---------------- f_DH both legs, near the zero height and generic
    for regime, n in (("t~85.7", 50), ("generic", 30), ("sigma~1/2", 20), ("sigma~1", 20)):
        for sig, t in regime_points(rng, regime, n):
            ref = ref_fdh(sig, t)
            contains_ball(f_dh_ball(Ball.from_fractions(sig, t)), ref, "f_dh_ball/" + regime)
            s = acb(producer_arb.rat_ball(sig), producer_arb.rat_ball(t))
            contains_acb(producer_arb.eval_fdh(s), ref, "arb_fdh/" + regime)
        print("  f_DH both legs %-10s n=%d done" % (regime, n))

    # ---------------- f_DH at its off-line zero: 15-digit quoted rho and a 40-digit refinement
    mp.dps = 120
    rho15 = mp.mpc(RHO_DH_RE, RHO_DH_IM)

    def fdh_mp(s):
        kap = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
        return mp.power(5, -s) * (mp.zeta(s, mp.mpf(1) / 5) + kap * mp.zeta(s, mp.mpf(2) / 5)
                                  - kap * mp.zeta(s, mp.mpf(3) / 5) - mp.zeta(s, mp.mpf(4) / 5))
    rho = mp.findroot(fdh_mp, rho15)
    print("  refined rho_DH (dps 120): %s" % mpmath.nstr(rho, 45))
    print("  |f_DH(rho refined)| = %s" % mpmath.nstr(abs(fdh_mp(rho)), 5))
    # exact rational 40-digit truncation of the refined zero
    rho_re40 = Fraction(mpmath.nstr(rho.real, 40, strip_zeros=False))
    rho_im40 = Fraction(mpmath.nstr(rho.imag, 40, strip_zeros=False))
    for (re, im, tag) in ((Fraction(RHO_DH_RE), Fraction(RHO_DH_IM), "rho15"),
                          (rho_re40, rho_im40, "rho40")):
        ref = ref_fdh(re, im)
        zb = f_dh_ball(Ball.from_fractions(re, im))
        ok, w = contains_ball(zb, ref, "f_dh_ball@" + tag)
        _, ahi = ivmpf_bounds(zb.abs_iv())
        s = acb(producer_arb.rat_ball(re), producer_arb.rat_ball(im))
        fb = producer_arb.eval_fdh(s)
        ok2, w2 = contains_acb(fb, ref, "arb_fdh@" + tag)
        print("  f_DH at %s: |ref| = %s; mp-ball |f| <= %.3e (width %.2e); arb ball %s"
              % (tag, mpmath.nstr(abs(ref), 5), float(ahi), float(w), fb.abs_lower() if hasattr(fb, 'abs_lower') else ""))
        rlo, rhi = zb.re_bounds(); ilo, ihi = zb.im_bounds()
        print("     mp box contains 0: %s" % (rlo <= 0 <= rhi and ilo <= 0 <= ihi))

    # ---------------- wide boxes (segment-like, as the producers use them), interior samples
    for evname, ev in (("zeta_ball", lambda b: zeta_ball(b)),
                       ("hurwitz_ball(1/5)", lambda b: hurwitz_ball(b, Fraction(1, 5))),
                       ("f_dh_ball", f_dh_ball)):
        bad = 0
        for k in range(12):
            sig = rnd_frac(rng, 0.52, 0.95)
            t = rnd_frac(rng, -150, 150)
            dsig = Fraction(rng.randint(1, 500), 10 ** 4)
            dt = Fraction(rng.randint(1, 500), 10 ** 4)
            horizontal = (k % 2 == 0)
            box = (Ball.from_fraction_boxes((sig, sig + dsig), (t, t)) if horizontal
                   else Ball.from_fraction_boxes((sig, sig), (t, t + dt)))
            z = ev(box)
            for u in (Fraction(0), Fraction(1, 7), Fraction(1, 2), Fraction(6, 7), Fraction(1)):
                ps = sig + (dsig * u if horizontal else 0)
                pt = t + (0 if horizontal else dt * u)
                ref = (ref_zeta(ps, pt) if evname == "zeta_ball"
                       else ref_hurwitz(ps, pt, Fraction(1, 5)) if evname.startswith("hurwitz")
                       else ref_fdh(ps, pt))
                ok, _ = contains_ball(z, ref, "widebox/" + evname)
                bad += (not ok)
        print("  wide segment boxes %-18s 12 boxes x 5 samples, %d failures" % (evname, bad))
    # arb wide boxes
    bad = 0
    for k in range(12):
        sig = rnd_frac(rng, 0.52, 0.95)
        t = rnd_frac(rng, -150, 150)
        dsig = Fraction(rng.randint(1, 500), 10 ** 4)
        dt = Fraction(rng.randint(1, 500), 10 ** 4)
        horizontal = (k % 2 == 0)
        seg = ("h", sig, sig + dsig, t) if horizontal else ("v", t, t + dt, sig)
        fb = producer_arb.eval_zeta(producer_arb.segment_ball(seg))
        for u in (Fraction(0), Fraction(1, 7), Fraction(1, 2), Fraction(6, 7), Fraction(1)):
            ps = sig + (dsig * u if horizontal else 0)
            pt = t + (0 if horizontal else dt * u)
            ok, _ = contains_acb(fb, ref_zeta(ps, pt), "widebox/arb_zeta")
            bad += (not ok)
    print("  wide segment boxes arb_zeta            12 boxes x 5 samples, %d failures" % bad)

    print("\nSUMMARY (pass/total per tag):")
    for tag in sorted(COUNTS):
        print("  %-28s %d/%d" % (tag, COUNTS[tag][0], COUNTS[tag][1]))
    print("TOTAL FAILURES: %d   (wall %.1fs)" % (len(FAILS), time.time() - t0))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
