"""dt0_recheck.py -- settle the one FAIL of validation-ft-mp-instance.txt (row 2, d/dt f at
(x1, y1), t = 0) by computation.

Diagnosis (from reading ft_mp_validate.py lines 259-268): at t = 0 the harness clamps the lower
finite-difference point to 0, so the "central difference" silently becomes a ONE-SIDED forward
difference with step h = 1e-12, whose truncation error is h |d^2/dt^2 f|/2 -- at row 2 (x1, y1),
|f| ~ 33 and each d/dt brings a factor up to |L^2/4 - alpha L/2| ~ 45, so ~ 1e-12 * 45^2 * 33 / 2
~ 3e-8, while the derivative ball is only 1e-9 wide; the observed discrepancy was 2.0e-8.  The
absolute tolerance 1e-12 of the harness is far below that truncation error.  (The mini instance
passed at t = 0 only because its derivative ball was 1.4e-6 wide.)

This script replaces the estimate by two references at the failing point and two more:
  (R1) the ANALYTIC time derivative D-F6 in plain mp floating point (dps 60): an independent float
       pipeline (no Ball code), d/dt A_t(s) = sum b_n^t n^{-s_*(s)} (L^2/4 - alpha(s) L/2),
       d/dt gamma = gamma (alpha(s_-)^2 - alpha(s_+)^2)/4, d/dt f = dA(s_+) + dgamma A(s_-) + gamma dA(s_-);
  (R2) a genuine two-sided central difference (f_t is a finite sum, defined for t < 0) with
       h = 1e-12 (truncation ~ h^2 |f'''|/6 ~ 1e-24 * 1e6/6 ~ 1e-19) -- consistency with R1 is the
       check that R1 itself is right.
Membership is decided in exact rational arithmetic (Fraction endpoints of the Ball, EPS = 1e-30
absorbing the references' own rounding at dps 60 with magnitudes ~ 1e3).

UNTRUSTED validation code (D-R3).  U.S. English.
"""
import json
import os
import sys
import time
import datetime
from fractions import Fraction

import mpmath
from mpmath import mp

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import ft_mp  # noqa: E402
from ft_mp import (FtEvaluator, ball_from_fr, iv_from_fr, set_prec, ft_mp_reference, _mpf_fr,  # noqa: E402
                   mpf_tuple_to_fraction)

LOG = os.path.join(_HERE, "validation-ft-mp-dt0.txt")


def out(s=""):
    print(s, flush=True)
    with open(LOG, "a") as fh:
        fh.write(s + "\n")


def m2f(v):
    """Exact Fraction of an mp.mpf (lossless, via its binary mantissa/exponent).  NOTE: never go through
    mp.mpf(v) here -- outside the workdps(60) block that would re-round the value to the global 53-bit
    precision (a 1e-14 error, which made the first run of this script mis-report the three t = 0
    f-value checks, whose balls are 1e-27 wide, as FAIL; the derivative checks were unaffected)."""
    return mpf_tuple_to_fraction(v._mpf_)


def contains_close(ball, w, eps):
    rlo, rhi = ball.re_bounds()
    ilo, ihi = ball.im_bounds()
    wr, wi = m2f(w.real), m2f(w.imag)
    return rlo - eps <= wr <= rhi + eps and ilo - eps <= wi <= ihi + eps


def dft_reference(x, y, t, N, dps=60):
    """(f, d/dt f, gamma) by the analytic D-F6 identities in plain mp floats (independent pipeline)."""
    with mp.workdps(dps):
        x, y, t = _mpf_fr(x), _mpf_fr(y), _mpf_fr(t)

        def alpha(s):
            return 1 / (2 * s) + 1 / (s - 1) + mp.log(s / (2 * mp.pi)) / 2

        def logM0(s):
            return (mp.log(s) + mp.log(s - 1) - s / 2 * mp.log(mp.pi) + mp.log(mp.sqrt(2 * mp.pi) / 16)
                    + (s / 2 - mp.mpf(1) / 2) * mp.log(s / 2) - s / 2)

        sp = (1 + y - 1j * x) / 2
        sm = (1 - y + 1j * x) / 2
        ap, am = alpha(sp), alpha(sm)
        gam = mp.exp(t / 4 * (am ** 2 - ap ** 2) + logM0(sm) - logM0(sp))
        dgam = gam * (am ** 2 - ap ** 2) / 4

        def A_and_dA(s, a):
            st = s + t / 2 * a
            tot = mp.mpc(0)
            dtot = mp.mpc(0)
            for n in range(1, N + 1):
                L = mp.log(n)
                term = mp.exp(t / 4 * L * L - st * L)
                tot += term
                dtot += term * (L * L / 4 - a * L / 2)
            return tot, dtot

        Ap, dAp = A_and_dA(sp, ap)
        Am, dAm = A_and_dA(sm, am)
        return Ap + gam * Am, dAp + dgam * Am + gam * dAm, gam


def main():
    set_prec(288)
    inst = {"x1": Fraction(5000000194858), "x2": Fraction(5000000194859),
            "y1": Fraction(16733, 100000), "y2": Fraction(1),
            "zc_re": Fraction(10000000389717, 2), "zc_im": Fraction(116733, 200000)}
    with open(os.path.join(_HERE, "moments/row2-plus.json")) as fh:
        pd = json.load(fh)
    with open(os.path.join(_HERE, "moments/row2-minus.json")) as fh:
        md = json.load(fh)
    ev = FtEvaluator(pd, md, inst["zc_re"], inst["zc_im"])
    N = ev.N
    out("=" * 78)
    out("d/dt f RE-CHECK at t = 0 (row 2, N0 = %d): evaluator derivative ball vs (R1) analytic D-F6 float pipeline "
        "and (R2) two-sided central difference h = 1e-12  (%s UTC; mpmath %s; prec 288)"
        % (N, datetime.datetime.now(datetime.timezone.utc).isoformat(), mpmath.__version__))
    out("=" * 78)
    EPS = Fraction(1, 10 ** 30)
    fails = checks = 0
    dfails = 0
    points = [(inst["x1"], inst["y1"], Fraction(0)),          # the failing point
              (inst["x2"], inst["y2"], Fraction(0)),
              (inst["x1"] + Fraction(373, 1000), inst["y1"] + (inst["y2"] - inst["y1"]) * Fraction(511, 1000), Fraction(0)),
              (inst["x1"], inst["y1"], Fraction(1, 1000))]     # a t > 0 point: the harness's central difference there was genuine
    for (x, y, t) in points:
        t_iv = iv_from_fr(t)
        ev.prepare(t_iv, Fraction(66, 100), want_dt=True)
        z = ball_from_fr(x, y)
        f, fdt, g, _ = ev.evaluate(z, t_iv, want_dt=True)
        t0 = time.time()
        fref, dref, gref = dft_reference(x, y, t, N)
        t1 = time.time() - t0
        h = Fraction(1, 10 ** 12)
        t0 = time.time()
        fp, _ = ft_mp_reference(x, y, t + h, N, dps=60)
        fm, _ = ft_mp_reference(x, y, t - h, N, dps=60)
        with mp.workdps(60):
            dcd = (fp - fm) / _mpf_fr(2 * h)
        t2 = time.time() - t0
        ok_f = contains_close(f, fref, EPS)
        ok_d1 = contains_close(fdt, dref, EPS)
        ok_d2 = contains_close(fdt, dcd, Fraction(1, 10 ** 15))     # cd truncation ~ 1e-19 plus rounding
        checks += 3
        fails += (not ok_f) + (not ok_d1) + (not ok_d2)
        dfails += (not ok_d1) + (not ok_d2)
        with mp.workdps(20):
            out("  x=%s y=%s t=%s" % (x, y, t))
            out("    f ball re %s" % (tuple(str(float(v)) for v in f.re_bounds()),))
            out("    f ref (R1)     %s   %s" % (mp.nstr(fref, 18), "PASS" if ok_f else "FAIL"))
            out("    df/dt ball re [%s, %s] im [%s, %s]  width %.2e" % (
                mp.nstr(_mpf_fr(fdt.re_bounds()[0]), 16), mp.nstr(_mpf_fr(fdt.re_bounds()[1]), 16),
                mp.nstr(_mpf_fr(fdt.im_bounds()[0]), 16), mp.nstr(_mpf_fr(fdt.im_bounds()[1]), 16),
                float(fdt.max_width())))
            out("    df/dt (R1 analytic) %s   %s  (%.0fs)" % (mp.nstr(dref, 18), "PASS" if ok_d1 else "FAIL", t1))
            out("    df/dt (R2 central)  %s   %s  (%.0fs)   |R1-R2| = %.2e" % (
                mp.nstr(dcd, 18), "PASS" if ok_d2 else "FAIL", t2, float(abs(dref - dcd))))
    out("dt0 recheck: %d checks, %d failures (%d of them derivative checks)" % (checks, fails, dfails))
    if dfails == 0:
        out("VERDICT: the harness FAIL at (x1, y1, t=0) was a one-sided-difference artifact of the harness "
            "(step 1e-12 forward difference, truncation h|f''|/2 ~ 3e-8 > ball width 1e-9); "
            "at all %d points the evaluator's derivative ball CONTAINS the analytic derivative (R1), and R1 agrees "
            "with the genuine central difference (R2) to the printed |R1-R2|." % len(points))
    else:
        out("VERDICT: %d derivative checks FAILED -- the evaluator's derivative ball does NOT contain the reference "
            "at some point; this is a producer defect (stop-the-line), not a harness artifact." % dfails)
    return fails


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
