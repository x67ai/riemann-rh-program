"""ft_mp_validate.py -- validation of the mpmath-ball f_t evaluator layer (ft_mp.py).

Every test decides membership in EXACT rational arithmetic (mpf endpoints -> Fractions); float
references are inflated by an explicit EPS that absorbs only the reference's own rounding.

Modes (each appends a dated block to the log file given by --log):
  --largearg   Ball.exp containment at imaginary parts up to 1e14 (the gamma regime at X ~ 5e12)
               against a dps-150 reference; 200 thin samples + 40 wide boxes.
  --pieces     alpha, log M_0, gamma, ft_direct containment against the independent mp float
               pipeline (dps 60) at random points with x in [200, 1e13], N <= 40 (ft_direct with the
               true N only for x <= 2e4).
  --integral   THE THEOREM-1.3 TEST (the task's >= 30 points): H_t(x+iy)/B_t(x+iy) by mp.quad of
               the defining integral at dps >= 120, against the enclosure f_t-box + E*disk from
               ft_direct + defect_bound; the reference MUST lie in the enclosure.  Reports the
               enclosure width (2E + box width) and the actual |g - mid f| for each point.
  --mini       the block-Taylor evaluator (FtEvaluator on the N = 5000 mini-instance moments in
               moments/mini-*.json, box [314159300, 314159301] x [y0, 1]) against ft_direct: thin
               points (intersection nonempty + reference containment), segment boxes (contain
               interior direct values), and d/dt f against a central difference of the reference.
  --instance   the same on the row-2 moments (N0 = 630783), a few points (ft_direct ~ 100 s each).
"""
import argparse
import datetime
import random
import sys
import time
from fractions import Fraction

from mpmath import mp

from ft_mp import *  # noqa: F401,F403
import ft_mp

LOG = None


def out(s=""):
    print(s, flush=True)
    if LOG is not None:
        with open(LOG, "a") as fh:
            fh.write(s + "\n")


def m2f(v):
    return mpf_tuple_to_fraction(v._mpf_)


def contains_close(ball, w, eps):
    rlo, rhi = ball.re_bounds()
    ilo, ihi = ball.im_bounds()
    return (rlo - eps <= m2f(w.real) <= rhi + eps) and (ilo - eps <= m2f(w.imag) <= ihi + eps)


def header(title):
    out("=" * 78)
    out("%s  (%s UTC; mpmath %s; prec 288)" % (title, datetime.datetime.now(datetime.timezone.utc).isoformat(), mpmath.__version__))
    out("=" * 78)


# ---------------------------------------------------------------- --largearg

def test_largearg(seed=11):
    header("LARGE-ARGUMENT Ball.exp (Im up to 1e14) vs dps-150 reference, exact-Fraction membership with EPS = 1e-100")
    rng = random.Random(seed)
    set_prec(288)
    EPS = Fraction(1, 10 ** 100)
    fails = checks = 0
    with mp.workdps(150):
        for k in range(200):
            a = Fraction(rng.randint(-30 * 10 ** 9, 30 * 10 ** 9), 10 ** 9)
            b = Fraction(rng.randint(-10 ** 23, 10 ** 23), 10 ** 9)          # |Im| <= 1e14
            thin = Ball.from_fractions(a, b)
            w = mp.exp(mp.mpc(ft_mp._mpf_fr(a), ft_mp._mpf_fr(b)))
            checks += 1
            if not contains_close(thin.exp(), w, EPS):
                fails += 1
                out("  FAIL thin exp at a=%s b=%s" % (a, b))
            # tightness: relative width must be tiny
            ex = thin.exp()
            if ex.max_width() > Fraction(1, 10 ** 60) * ball_abs_hi(ex):
                fails += 1
                out("  FAIL thin exp width too large at a=%s b=%s: %s" % (a, b, float(ex.max_width())))
        for k in range(40):
            a = Fraction(rng.randint(-5 * 10 ** 9, 5 * 10 ** 9), 10 ** 9)
            b0 = Fraction(rng.randint(-10 ** 23, 10 ** 23), 10 ** 9)
            wd = Fraction(rng.randint(1, 3 * 10 ** 9), 10 ** 9)                # width up to 3
            box = Ball.from_fraction_boxes((a, a), (b0, b0 + wd))
            ex = box.exp()
            for u in (Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(4, 5), Fraction(1)):
                bb = b0 + wd * u
                w = mp.exp(mp.mpc(ft_mp._mpf_fr(a), ft_mp._mpf_fr(bb)))
                checks += 1
                if not contains_close(ex, w, EPS):
                    fails += 1
                    out("  FAIL wide exp at a=%s b=%s" % (a, bb))
    out("largearg: %d checks, %d failures" % (checks, fails))
    return fails


# ---------------------------------------------------------------- --pieces

def test_pieces(seed=12):
    header("PIECES: alpha, log M_0, gamma, ft_direct vs the independent mp float pipeline (dps 60), EPS = 1e-40 relative-ish")
    rng = random.Random(seed)
    set_prec(288)
    fails = checks = 0
    EPS = Fraction(1, 10 ** 40)
    with mp.workdps(60):
        for k in range(40):
            ex = rng.uniform(2.4, 13.0)
            x = Fraction(int(10 ** ex * 1000), 1000)
            y = Fraction(rng.randint(0, 1000), 1000)
            t = Fraction(rng.randint(1, 500), 1000)
            z = ball_from_fr(x, y)
            t_iv = iv_from_fr(t)
            sp, sm = s_plus(z), s_minus(z)
            xm, ym, tm = ft_mp._mpf_fr(x), ft_mp._mpf_fr(y), ft_mp._mpf_fr(t)
            spm = (1 + ym - 1j * xm) / 2
            smm = (1 - ym + 1j * xm) / 2

            def alpha(s):
                return 1 / (2 * s) + 1 / (s - 1) + mp.log(s / (2 * mp.pi)) / 2

            def logM0(s):
                return (mp.log(s) + mp.log(s - 1) - s / 2 * mp.log(mp.pi) + mp.log(mp.sqrt(2 * mp.pi) / 16)
                        + (s / 2 - mp.mpf(1) / 2) * mp.log(s / 2) - s / 2)
            scale = EPS * (1 + abs(int(x)))          # absolute tolerance scaled by the magnitudes involved (log M_0 ~ x log x)
            for name, bl, ref in (("alpha(s+)", alpha_ball(sp), alpha(spm)), ("alpha(s-)", alpha_ball(sm), alpha(smm)),
                                  ("logM0(s+)", logM0_ball(sp), logM0(spm)), ("logM0(s-)", logM0_ball(sm), logM0(smm))):
                checks += 1
                if not contains_close(bl, ref, scale * 100):
                    fails += 1
                    out("  FAIL %s at x=%s y=%s: ball re %s im %s ref %s" % (name, x, y, bl.re_bounds(), bl.im_bounds(), ref))
            g, gdt, _, _ = gamma_and_dt(z, t_iv)
            fref, gref = ft_mp_reference(x, y, t, 1, dps=60)
            checks += 1
            if not contains_close(g, gref, EPS):
                fails += 1
                out("  FAIL gamma at x=%s y=%s t=%s: ball %s ref %s" % (x, y, t, g, gref))
            if x <= 20000:
                _, N, N2 = N_of(iv_from_fr(x), t_iv)
                if N == N2:
                    f, _ = ft_direct(z, t_iv, N)
                    fref, _ = ft_mp_reference(x, y, t, N, dps=60)
                    checks += 1
                    if not contains_close(f, fref, EPS * 100):
                        fails += 1
                        out("  FAIL ft_direct at x=%s y=%s t=%s N=%d: ball %s ref %s" % (x, y, t, N, f, fref))
                    if k < 8:
                        out("  x=%-10s y=%.3f t=%.3f N=%3d  f=%s  width=%.2e" % (
                            float(x), float(y), float(t), N, mp.nstr(fref, 12), float(f.max_width())))
    out("pieces: %d checks, %d failures" % (checks, fails))
    return fails


# ---------------------------------------------------------------- --integral (Theorem 1.3)

def test_integral(npts=32, seed=13, dps=130):
    header("THEOREM 1.3 END-TO-END: H_t/B_t by mp.quad (dps %d) must lie in f_t-box + E*disk (ft_direct + defect_bound)" % dps)
    out("region (5): x >= 200, 0 <= y <= 1, 0 < t <= 1/2; points drawn with x in [200, 330] (H_t ~ e^{-pi x/8} ~ 1e-35..1e-56"
        " against an O(1) integrand, so the quadrature needs ~90+ digits of cancellation headroom)")
    rng = random.Random(seed)
    set_prec(288)
    fails = 0
    rows = []
    pts = []
    # a deterministic spread plus random points
    for x in (200, 233, 266, 300, 330):
        for (y, t) in ((Fraction(0), Fraction(1, 5)), (Fraction(1), Fraction(93, 500)), (Fraction(16733, 100000), Fraction(1, 2))):
            pts.append((Fraction(x), y, t))
    while len(pts) < npts:
        pts.append((Fraction(rng.randint(200000, 330000), 1000), Fraction(rng.randint(0, 1000), 1000),
                    Fraction(rng.randint(1, 500), 1000)))
    t_all = time.time()
    for (x, y, t) in pts:
        t0 = time.time()
        z = ball_from_fr(x, y)
        t_iv = iv_from_fr(t)
        _, N, N2 = N_of(iv_from_fr(x), t_iv)
        assert N == N2
        f, g = ft_direct(z, t_iv, N)
        E, parts = defect_bound(iv_from_fr(x), iv_from_fr(y), t_iv, N)
        gref, H, B, gcheck = Ht_over_Bt_reference(x, y, t, dps=dps)
        with mp.workdps(dps):
            quad_consistency = abs(gref - gcheck)
        gr, gi = m2f(gref.real), m2f(gref.imag)
        dist = point_in_ball_dist(f, gr, gi)
        # the reference's own uncertainty: two quadratures differ by quad_consistency; inflate by 100x that + 1e-40
        tol = Fraction(m2f(quad_consistency)) * 100 + Fraction(1, 10 ** 40)
        ok = dist <= E + tol
        if not ok:
            fails += 1
        # actual |g - mid(f)|
        rlo, rhi = f.re_bounds()
        ilo, ihi = f.im_bounds()
        mid_r, mid_i = (rlo + rhi) / 2, (ilo + ihi) / 2
        with mp.workdps(30):
            actual = mp.sqrt((ft_mp._mpf_fr(gr - mid_r)) ** 2 + (ft_mp._mpf_fr(gi - mid_i)) ** 2)
        row = ("  x=%-9s y=%.5f t=%.3f N=%2d  |f|=%.4f  E=%.4e (eAB %.1e, eC0 %.1e)  |g-f|=%.3e  ratio=%.3f  "
               "f-box width=%.1e  quad-consistency=%.1e  %s  (%.0fs)" % (
                   float(x), float(y), float(t), N, float(ball_abs_hi(f)), float(E), float(parts["eAB_hi"]),
                   float(parts["eC0_hi"]), float(actual), float(actual) / float(E), float(f.max_width()),
                   float(quad_consistency), "PASS" if ok else "FAIL", time.time() - t0))
        out(row)
        rows.append((float(actual) / float(E), float(f.max_width())))
    out("integral: %d points, %d failures; max actual/E ratio = %.3f; max f-box width = %.1e; total %.0fs" % (
        len(pts), fails, max(r[0] for r in rows), max(r[1] for r in rows), time.time() - t_all))
    return fails


# ---------------------------------------------------------------- --mini / --instance (the Taylor evaluator)

def test_taylor(plus_path, minus_path, xc, yc, x1, x2, y1, y2, t0, npts, seed=14, refN=None, label="mini"):
    header("BLOCK-TAYLOR EVALUATOR (%s) vs direct summation and the float reference" % label)
    rng = random.Random(seed)
    set_prec(288)
    with open(plus_path) as fh:
        pd = json.load(fh)
    with open(minus_path) as fh:
        md = json.load(fh)
    ev = FtEvaluator(pd, md, xc, yc)
    N = ev.N
    out("N = %d, blocks = %d, R = %d; box [%s, %s] x [%s, %s], center (%s, %s)" % (
        N, len(ev.plus.blocks), ev.plus.R, x1, x2, y1, y2, xc, yc))
    fails = checks = 0
    EPS = Fraction(1, 10 ** 40)
    dmax = Fraction(66, 100)
    for ti, t in enumerate((Fraction(0), Fraction(1, 20), Fraction(93, 500), Fraction(1, 1000))):
        if t > t0:
            continue
        t_iv = iv_from_fr(t)
        tp = time.time()
        ev.prepare(t_iv, dmax, want_dt=True)
        out("  t = %s: prepare %.2fs; orders (J,K) plus: %s" % (t, time.time() - tp, ev.orders[0][:6]))
        for k in range(npts):
            x = x1 + (x2 - x1) * Fraction(rng.randint(0, 1000), 1000)
            y = y1 + (y2 - y1) * Fraction(rng.randint(0, 1000), 1000)
            if k == 0:
                x, y = x1, y1
            if k == 1:
                x, y = x2, y2
            z = ball_from_fr(x, y)
            te = time.time()
            f, fdt, g, _ = ev.evaluate(z, t_iv, want_dt=True)
            te = time.time() - te
            td = time.time()
            fd, gd = ft_direct(z, t_iv, N)
            td = time.time() - td
            inter = f.intersect(fd)
            checks += 1
            if inter is None:
                fails += 1
                out("  FAIL disjoint Taylor/direct at x=%s y=%s t=%s: %s vs %s" % (x, y, t, f, fd))
            fref, gref = ft_mp_reference(x, y, t, N, dps=60)
            checks += 1
            if not contains_close(f, fref, EPS):
                fails += 1
                out("  FAIL Taylor box misses reference at x=%s y=%s t=%s: %s vs %s" % (x, y, t, f, fref))
            # d/dt f: central difference of the reference at dps 60 (h = 1e-12 -> truncation ~ h^2 |f'''| ~ 1e-24 * O(1e4))
            with mp.workdps(60):
                h = Fraction(1, 10 ** 12)
                tp_, tm_ = t + h, t - h
                if tm_ < 0:
                    tm_ = Fraction(0)
                fp, _ = ft_mp_reference(x, y, tp_, N, dps=60)
                fm, _ = ft_mp_reference(x, y, tm_, N, dps=60)
                dref = (fp - fm) / ft_mp._mpf_fr(tp_ - tm_)
            checks += 1
            if not contains_close(fdt, dref, Fraction(1, 10 ** 12)):
                fails += 1
                out("  FAIL d/dt f at x=%s y=%s t=%s: ball %s vs fd %s" % (x, y, t, fdt, dref))
            if k < 4 or not contains_close(f, fref, EPS):
                out("    x=%.6f y=%.5f  f=%s  Taylor width %.2e (%.2fs)  direct width %.2e (%.1fs)  |dt f|~%.3g width %.1e" % (
                    float(x), float(y), mp.nstr(fref, 14), float(f.max_width()), te, float(fd.max_width()), td,
                    float(abs(dref)), float(fdt.max_width())))
        # segment boxes: width h in x on the bottom edge and in y on the right edge
        for (h, edge) in ((Fraction(1, 100), "bottom"), (Fraction(1, 1000), "bottom"), (Fraction(1, 100), "right")):
            if edge == "bottom":
                xa = x1 + Fraction(rng.randint(0, 900), 1000)
                box = Ball.from_fraction_boxes((xa, xa + h), (y1, y1))
                pts = [(xa + h * u, y1) for u in (Fraction(0), Fraction(1, 3), Fraction(1))]
            else:
                ya = y1 + (y2 - y1) * Fraction(rng.randint(0, 900), 1000)
                box = Ball.from_fraction_boxes((x2, x2), (ya, ya + h))
                pts = [(x2, ya + h * u) for u in (Fraction(0), Fraction(1, 3), Fraction(1))]
            fb, fbdt, gb, _ = ev.evaluate(box, t_iv, want_dt=True)
            for (px, py) in pts:
                fref, _ = ft_mp_reference(px, py, t, N, dps=60)
                checks += 1
                if not contains_close(fb, fref, EPS):
                    fails += 1
                    out("  FAIL box (%s, h=%s) misses interior point %s,%s: %s vs %s" % (edge, h, px, py, fb, fref))
            out("    box %s h=%s: f-box width %.3e  |f| in [%.3f, %.3f]  |dt f| <= %.3g" % (
                edge, h, float(fb.max_width()), float(iv_lo(fb.abs_iv())), float(ball_abs_hi(fb)), float(ball_abs_hi(fbdt))))
        # a prism-wide t interval on a segment box (the D route)
        if ti == 0:
            T = iv_from_fraction_pair(Fraction(0), Fraction(1, 100))
            ev.prepare(T, dmax, want_dt=True)
            box = Ball.from_fraction_boxes((x1, x1 + Fraction(1, 100)), (y1, y1))
            fb, fbdt, gb, _ = ev.evaluate(box, T, want_dt=True)
            out("    t in [0, 0.01], box bottom h=0.01: f-box width %.3e, |dt f| <= %.4g" % (float(fb.max_width()), float(ball_abs_hi(fbdt))))
            for tt in (Fraction(0), Fraction(1, 200), Fraction(1, 100)):
                for u in (Fraction(0), Fraction(1, 2), Fraction(1)):
                    fref, _ = ft_mp_reference(x1 + u / 100, y1, tt, N, dps=60)
                    checks += 1
                    if not contains_close(fb, fref, EPS):
                        fails += 1
                        out("  FAIL t-interval box misses (x=%s, t=%s)" % (x1 + u / 100, tt))
            ev.prepare(t_iv, dmax, want_dt=True)
    out("%s: %d checks, %d failures" % (label, checks, fails))
    return fails


def main(argv):
    global LOG
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", default="validation-ft-mp.txt")
    ap.add_argument("--largearg", action="store_true")
    ap.add_argument("--pieces", action="store_true")
    ap.add_argument("--integral", action="store_true")
    ap.add_argument("--integral-npts", type=int, default=32)
    ap.add_argument("--integral-dps", type=int, default=130)
    ap.add_argument("--mini", action="store_true")
    ap.add_argument("--instance", action="store_true")
    ap.add_argument("--npts", type=int, default=6)
    args = ap.parse_args(argv)
    LOG = args.log
    fails = 0
    if args.largearg:
        fails += test_largearg()
    if args.pieces:
        fails += test_pieces()
    if args.integral:
        fails += test_integral(npts=args.integral_npts, dps=args.integral_dps)
    if args.mini:
        fails += test_taylor("moments/mini-plus.json", "moments/mini-minus.json", Fraction(628318601, 2), Fraction(116733, 200000),
                             Fraction(314159300), Fraction(314159301), Fraction(16733, 100000), Fraction(1), Fraction(93, 500),
                             args.npts, label="mini N=5000")
    if args.instance:
        fails += test_taylor("moments/row2-plus.json", "moments/row2-minus.json", Fraction(10000000389717, 2), Fraction(116733, 200000),
                             Fraction(5000000194858), Fraction(5000000194859), Fraction(16733, 100000), Fraction(1), Fraction(93, 500),
                             args.npts, label="row 2 N0=630783")
    out("TOTAL FAILURES: %d" % fails)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
