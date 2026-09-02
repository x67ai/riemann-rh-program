#!/usr/bin/env python3
"""validate_arb_ft.py -- independent (mpmath) cross-validation of the Arb leg's f_t + E enclosure of H_t/B_t, and of the
Taylor/moment evaluator and its derivative and prism-uniform balls (results/d1-m2a/producer_arb.py).

NOT the second producer leg (that is the mpmath-BALL leg, a separate deliverable that shares no evaluation code with this
file): this is heuristic high-precision floating point (mpmath 1.3.0) used only to check that the Arb leg's rigorous
enclosures CONTAIN independently computed reference values.  A pass is evidence; a failure is stop-the-line.

Reference evaluator (independent code path, mpmath only; P15 = fetched/p3-22a4-polymath15-2019-upper-bound-debruijn-newman.pdf):
  * P15 (1)-(2) p1:  H_0(z) = (1/8) xi(1/2 + i z/2),  xi(s) = (s(s-1)/2) pi^{-s/2} Gamma(s/2) zeta(s).
  * P15 (3) p1 / (4) p2:  Phi(u) = sum_{n>=1} (2 pi^2 n^4 e^{9u} - 3 pi n^2 e^{5u}) exp(-pi n^2 e^{4u}),
                          H_t(z) = int_0^inf e^{t u^2} Phi(u) cos(zu) du.
  * DERIVATION D-V1 (heat-kernel form of H_t, used for t > 0 where the u-integrand oscillates too fast for quadrature at
    large x).  For real c and u:  (2 pi)^{-1/2} int_R e^{-w^2/2} cos((z + i c w) u) dw = cos(zu) e^{c^2 u^2 / 2}, because
    cos((z + icw)u) = (e^{izu} e^{-cwu} + e^{-izu} e^{cwu})/2 and (2 pi)^{-1/2} int e^{-w^2/2} e^{+-cwu} dw = e^{c^2 u^2/2}
    (complete the square).  With c = sqrt(2t) this is e^{t u^2} cos(zu).  Hence, by Fubini (|Phi(u)| decays like
    exp(-pi e^{4u}) and |cos((z+icw)u)| <= e^{(|Im z| + c|w|) u}, so the double integral converges absolutely),
       H_t(z) = int_0^inf Phi(u) (2 pi)^{-1/2} int_R e^{-w^2/2} cos((z + icw)u) dw du
              = (2 pi)^{-1/2} int_R e^{-w^2/2} H_0(z + i sqrt(2t) w) dw.
    For z = x + iy this is a NON-oscillatory Gaussian integral of xi along Im s = x/2, Re s = (1 - y - sqrt(2t) w)/2.
    D-V1 is itself checked numerically against the direct u-integral at x in {50, 120, 200} (section A).
  * B_t(z) = M_t((1+y-ix)/2) from P15 (6), (9), (10), (11) p4, re-implemented in mpmath (formula sharing, not code sharing).
  * Truncation of the w-integral to [-W, W]: the integrand is e^{-w^2/2} times |H_0(z + i c w)|/|H_0(z)| which grows at most
    like (x/2)^{c|w|/4} (the Gamma factor; sigma shifts by c w/2); at W = 16, x = 10^4, t = 0.2 that is e^{-128} * 5000^{2.5}
    ~ 1e-46 relative.  Quadrature: mpmath Gauss-Legendre on 81 equal panels of [-W, W] at dps 45 -- the integrand's modulus
    varies by many orders across the range, and a convergence study at (x, y, t) = (10^4, y0, 0.2) gave relative changes
    3.4e-14 (29 panels), 6.7e-19 (41 panels), < 1e-25 (81 vs 121 panels) -- so the reference is good to ~1e-25 relative.
    Section A' re-checks four points at dps 60 / W = 18 / 121 panels (threshold 1e-22).
The Arb side is called through producer_arb.point_hook (direct summation of (92) + the D-A2 defect bound) in section B and
through producer_arb.BoxEvaluator / SeamContext (the D-A4..D-A18 Taylor evaluator, the one used for the transcripts) in
sections C-E.

Containment test: exact rational arithmetic on the ball's mid/rad (Fractions) against the reference converted exactly from its
binary mantissa/exponent, with a declared decimal slack 1e-25 (M1 harness lesson: never compare prints, never feed floats).
"""
import os, sys, time
from fractions import Fraction
import mpmath
from mpmath import mp, mpf, mpc, pi, exp, cos, log, sqrt, gamma, zeta, quad, inf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import producer_arb as PA  # the Arb leg (its point hook, evaluator classes and the exact ball->rational helpers)

mp.dps = 45
SLACK = Fraction(1, 10 ** 25)


def Phi(u):
    s = mpf(0); n = 1
    while True:
        e4 = exp(4 * u)
        term = (2 * pi ** 2 * n ** 4 * exp(9 * u) - 3 * pi * n ** 2 * exp(5 * u)) * exp(-pi * n ** 2 * e4)
        s += term
        if abs(term) < mpf(10) ** (-mp.dps - 10) and n > 2:
            break
        n += 1
        if n > 200:
            break
    return s


def xi(s):
    return (s * (s - 1) / 2) * pi ** (-s / 2) * gamma(s / 2) * zeta(s)


def H0(z):
    return xi(mpf(1) / 2 + 1j * z / 2) / 8


def Ht_direct(z, t):
    f = lambda u: exp(t * u * u) * Phi(u) * cos(z * u)
    # Phi(u) ~ exp(9u - pi e^{4u}); negligible beyond u ~ 1.2
    return quad(f, mpmath.linspace(0, mpf("1.4"), 60))


def Ht_heat(z, t, W=16, n_sub=81):
    if t == 0:
        return H0(z)
    c = sqrt(2 * t)
    f = lambda w: H0(z + 1j * c * w) * exp(-w * w / 2)
    return quad(f, mpmath.linspace(-W, W, n_sub)) / sqrt(2 * pi)


def alpha_mp(s):
    return 1 / (2 * s) + 1 / (s - 1) + mpmath.log(s / (2 * pi)) / 2


def M0_mp(s):
    return (mpf(1) / 8) * (s * (s - 1) / 2) * pi ** (-s / 2) * sqrt(2 * pi) * exp((s / 2 - mpf(1) / 2) * mpmath.log(s / 2) - s / 2)


def Bt_mp(z, t):
    s = (1 + z.imag - 1j * z.real) / 2
    return exp(t / 4 * alpha_mp(s) ** 2) * M0_mp(s)


def g_ref(x, y, t):
    """Reference H_t/B_t at exact rationals x, y, t (converted exactly to mpf)."""
    z = mpc(mpf(x.numerator) / x.denominator, mpf(y.numerator) / y.denominator)
    tt = mpf(t.numerator) / t.denominator
    return Ht_heat(z, tt) / Bt_mp(z, tt)


def mpf_to_frac(v):
    sign, man, e, bc = mpmath.mpf(v)._mpf_
    q = Fraction(int(man)) * (Fraction(2) ** e)
    return -q if sign else q


def ball_box(f):
    re_lo, re_hi = PA.ball_interval(f.real); im_lo, im_hi = PA.ball_interval(f.imag)
    return (re_lo + re_hi) / 2, (im_lo + im_hi) / 2, max(re_hi - re_lo, im_hi - im_lo) / 2


def contained(f, E, r):
    """True iff the reference r lies in the disc around the ball's centre of radius (ball half-width + E + slack)."""
    mid_re, mid_im, rad = ball_box(f)
    rr, ri = mpf_to_frac(r.real), mpf_to_frac(r.imag)
    dist2 = (rr - mid_re) ** 2 + (ri - mid_im) ** 2
    allow = rad + Fraction(E) + SLACK
    dist = float(sqrt(mpf(dist2.numerator) / dist2.denominator))
    return dist2 <= allow * allow, dist, float(rad)


def main():
    out = []
    def log(msg):
        print(msg); out.append(msg); sys.stdout.flush()
        with open(os.path.join(HERE, "arb-validation-run.txt"), "w") as fh:
            fh.write("\n".join(out) + "\n")
    T0 = time.time()
    log(f"validate_arb_ft.py -- mpmath {mpmath.__version__} dps {mp.dps}; python-flint {PA.flint.__version__} prec {PA.PREC}; "
        f"{time.strftime('%Y-%m-%dT%H:%M:%S')} local")
    y0 = Fraction(16733, 100000); t0 = Fraction(93, 500)
    failures = 0
    # ---- Section A: D-V1 (heat-flow representation) against the direct u-integral
    log("A. D-V1 heat-kernel representation vs direct u-quadrature (moderate x):")
    # the direct u-integral loses ~ (pi x / 8) / ln 10 digits to cancellation (H_t ~ e^{-pi x/8} against an O(1) integrand),
    # so it is computed at dps 35 + that loss + 5; the heat-kernel form has no such loss (it is what the harness relies on).
    for (x, y, t) in ((50, mpf("0.3"), mpf("0.1")), (120, mpf(1), mpf("0.186")), (200, mpf("0.16733"), mpf("0.05"))):
        loss = int(float(pi) * x / 8 / 2.302585) + 5
        mp.dps = 45 + loss
        z = mpc(x, y)
        d = Ht_direct(z, t); h = Ht_heat(z, t)
        rd = abs(d - h) / abs(d)
        mp.dps = 45
        log(f"   x={x} y={y} t={t} (dps {45+loss}): direct={mpmath.nstr(d, 15)} heat={mpmath.nstr(h, 15)} rel.diff={mpmath.nstr(rd, 3)}")
        if not rd < mpf(10) ** -20:
            failures += 1; log("   D-V1 CHECK FAILED")
    log("   D-V1 agreement < 1e-20 at all three points" if failures == 0 else "   D-V1 FAILED")
    # ---- Section A': quadrature stability of the reference
    log("A'. reference stability: dps 45 / W=16 / 81 panels  vs  dps 60 / W=18 / 121 panels:")
    for (x, y, t) in ((Fraction(10000), y0, Fraction(1, 5)), (Fraction(10000), Fraction(1), Fraction(93, 500)),
                      (Fraction(1000), Fraction(1, 2), Fraction(1, 20)), (Fraction(3000), y0, Fraction(93, 500))):
        r1 = g_ref(x, y, t)
        mp.dps = 60
        z = mpc(mpf(x.numerator) / x.denominator, mpf(y.numerator) / y.denominator); tt = mpf(t.numerator) / t.denominator
        r2 = Ht_heat(z, tt, W=18, n_sub=121) / Bt_mp(z, tt)
        mp.dps = 45
        rd = abs(r1 - r2) / abs(r1)
        log(f"   x={x} y={float(y):.5f} t={float(t):.3f}: g={mpmath.nstr(r1, 25)} rel.diff={mpmath.nstr(rd, 3)}")
        if not rd < mpf(10) ** -22:
            failures += 1; log("   REFERENCE UNSTABLE")
    # ---- Section B: containment at 48 points in region (5), direct-sum evaluator + D-A2 defect
    log("B. containment H_t/B_t in f_t (+-) (rad + E): Arb direct-sum evaluator (point_hook) vs mpmath reference:")
    xs = [200, 1000, 3000, 10000]
    ts = [Fraction(0), Fraction(1, 20), Fraction(93, 500), Fraction(1, 5)]
    ys = [y0, Fraction(1, 2), Fraction(1)]
    n_ok = n_tot = 0; worst_ratio = 0.0; widths = []
    for x in xs:
        for t in ts:
            for y in ys:
                tA = time.time()
                r = g_ref(Fraction(x), y, t)
                d = PA.point_hook(Fraction(x), y, t)
                f = d["f"]; E = d["E"]
                ok, dist, rad = contained(f, E, r)
                ratio = dist / float(E)
                worst_ratio = max(worst_ratio, ratio)
                widths.append((x, float(t), float(y), rad, float(E)))
                n_tot += 1; n_ok += ok
                B = Bt_mp(mpc(x, mpf(y.numerator) / y.denominator), mpf(t.numerator) / t.denominator)
                Bm = complex(float(PA.ball_interval(d["B"].real)[0]), float(PA.ball_interval(d["B"].imag)[0]))
                bdiff = abs(mpc(Bm.real, Bm.imag) - B) / abs(B)
                log(f"   x={x:5d} t={float(t):.3f} y={float(y):.5f} N={d['N']:3d} |g|={float(abs(r)):.5f} |f|={float(abs(complex(*map(float, ball_box(f)[:2])))):.5f} "
                    f"rad_f={rad:.1e} E={float(E):.3e} (eC0={float(d['E_C0']):.2e} eAB={float(d['E_AB']):.2e}) |g-f|={dist:.3e} "
                    f"|g-f|/E={ratio:.3f} contained={ok} relB={mpmath.nstr(bdiff, 2)} {time.time()-tA:.1f}s")
                if not ok:
                    failures += 1
    log(f"   containment: {n_ok}/{n_tot} points; worst |g-f|/E = {worst_ratio:.4f} (must be <= 1)")
    log(f"   widths: rad_f (ball half-width of the Arb f_t) in [{min(w[3] for w in widths):.2e}, {max(w[3] for w in widths):.2e}]; "
        f"E in [{min(w[4] for w in widths):.2e}, {max(w[4] for w in widths):.2e}]; the enclosure of H_t/B_t has radius rad_f + E")
    # ---- Section C: the Taylor/moment evaluator (the one used for the transcripts) on a moderate-x box vs the reference
    X = Fraction(10000)
    Nb = PA.N_of(X, Fraction(0))
    assert PA.N_of(X + 1, t0) == Nb
    log(f"C. Taylor/moment evaluator (BoxEvaluator) on [{X}, {X+1}] x [{y0}, 1] x [0, {t0}], N = {Nb}: seam balls f (+-) E vs reference:")
    box = PA.BoxEvaluator(X, X + 1, y0, Fraction(1), t0, Nb, log=lambda m: log("   " + m))
    pts = [(X, y0), (X + 1, Fraction(1)), (X + Fraction(1, 3), y0), (X + Fraction(7, 10), Fraction(1)),
           (X, Fraction(3, 5)), (X + 1, Fraction(2, 5)), (X + Fraction(1, 2), y0), (X + Fraction(9, 10), Fraction(1))]
    nC = okC = 0; worstC = 0.0; wC = []
    for tt in (Fraction(0), Fraction(93, 500)):
        seam = box.seam(tt)
        for (xx, yy) in (pts if tt == 0 else pts[:6]):
            r = g_ref(xx, yy, tt)
            f = seam.eval(xx, yy)[0]
            ok, dist, rad = contained(f, seam.E, r)
            nC += 1; okC += ok; worstC = max(worstC, dist / float(seam.E)); wC.append(rad)
            if not ok:
                failures += 1
            log(f"   t={float(tt):.3f} z=({float(xx-X):.3f}+X, {float(yy):.5f}) rad_f={rad:.1e} E_box={float(seam.E):.3e} |g-f|={dist:.3e} ratio={dist/float(seam.E):.3f} contained={ok}")
    log(f"   Taylor evaluator containment: {okC}/{nC}; worst ratio {worstC:.4f}; rad_f in [{min(wC):.1e}, {max(wC):.1e}]")
    # ---- Section D: derivative balls vs finite differences of the direct sum; prism-uniform balls contain direct values
    log("D. derivative balls (f_z, f_t, f_zz, f_zt, f_tt) vs central differences of the direct sum (Arb, ft_direct), and D-A15 prism balls:")
    hz = Fraction(1, 10 ** 6); ht = Fraction(1, 10 ** 6)
    def fd(xx, yy, tt):
        return PA.ft_direct(PA.cpoint(xx, yy), tt, Nb)[0]
    def mid(b):
        m_re, m_im, _ = ball_box(b); return complex(float(m_re), float(m_im))
    nD = okD = 0
    for tt in (Fraction(1, 20), Fraction(93, 500)):
        seam = box.seam(tt)
        for (xx, yy) in pts[:4]:
            f, fz, ft, fzz, fzt, ftt = seam.eval(xx, yy)
            F0 = mid(fd(xx, yy, tt))
            Fxp, Fxm = mid(fd(xx + hz, yy, tt)), mid(fd(xx - hz, yy, tt))
            Ftp, Ftm = mid(fd(xx, yy, tt + ht)), mid(fd(xx, yy, tt - ht))
            Fxptp, Fxmtm = mid(fd(xx + hz, yy, tt + ht)), mid(fd(xx - hz, yy, tt - ht))
            Fxptm, Fxmtp = mid(fd(xx + hz, yy, tt - ht)), mid(fd(xx - hz, yy, tt + ht))
            h = float(hz)
            d_z = (Fxp - Fxm) / (2 * h); d_t = (Ftp - Ftm) / (2 * h)
            d_zz = (Fxp - 2 * F0 + Fxm) / (h * h); d_tt = (Ftp - 2 * F0 + Ftm) / (h * h)
            d_zt = (Fxptp - Fxptm - Fxmtp + Fxmtm) / (4 * h * h)
            checks = [("f_z", fz, d_z, 1e-6), ("f_t", ft, d_t, 1e-6), ("f_zz", fzz, d_zz, 1e-2), ("f_zt", fzt, d_zt, 1e-2), ("f_tt", ftt, d_tt, 1e-2)]
            line = f"   t={float(tt):.3f} z=({float(xx-X):.3f}+X,{float(yy):.5f}):"
            for name, b, ref, tol in checks:
                m = mid(b); w = ball_box(b)[2]
                err = abs(m - ref) / max(abs(ref), 1e-30)
                ok = err < tol   # finite-difference truncation ~ h^2 (2nd-order central), so 1e-6 / 1e-2 relative are the test's own limits
                nD += 1; okD += ok
                line += f" {name}={m:.6g} (fd {ref:.6g}, rel {err:.1e}, w {float(w):.1e}){'' if ok else ' MISMATCH'}"
            log(line)
        # prism-uniform balls (D-A15): must contain the direct value at several t' in the prism
        tp = tt + Fraction(1, 200)
        pctx = box.seam(tt, tp)
        for (xx, yy) in pts[:3]:
            f_p = pctx.eval(xx, yy)[0]
            allin = True
            for tq in (tt, tt + (tp - tt) / 3, tt + 2 * (tp - tt) / 3, tp):
                dv = fd(xx, yy, tq)
                dlo, dhi = PA.ball_interval(dv.real); plo, phi = PA.ball_interval(f_p.real)
                dlo2, dhi2 = PA.ball_interval(dv.imag); plo2, phi2 = PA.ball_interval(f_p.imag)
                inside = (plo <= dlo and dhi <= phi and plo2 <= dlo2 and dhi2 <= phi2)
                allin = allin and inside
            nD += 1; okD += allin
            if not allin:
                failures += 1
            log(f"   prism [{float(tt):.3f}, {float(tp):.3f}] z=({float(xx-X):.3f}+X,{float(yy):.5f}): prism ball width {ball_box(f_p)[2]*2:.2e} contains direct values at 4 times: {allin}")
    log(f"   derivative/prism checks: {okD}/{nD}")
    if okD != nD:
        failures += 1
    # ---- Section E: hull-box rows contain sampled values (the H2-B row quantifier) on the moderate-x box
    log("E. segment hull boxes (seg_box, D-A10/D-A10') contain 9 interior reference-free direct-sum values per segment (Arb vs Arb, exact):")
    seam = box.seam(Fraction(1, 20))
    nE = okE = 0
    for seg in (("h", X, X + Fraction(1, 50), y0), ("v", Fraction(1, 2), Fraction(1, 2) + Fraction(1, 50), X + 1),
                ("h", X + Fraction(1, 2), X + Fraction(1, 2) - Fraction(1, 50), Fraction(1)), ("v", Fraction(9, 10), Fraction(9, 10) - Fraction(1, 50), X)):
        bx, info = PA.seg_box(seam, seg, 10 ** 12)
        kind, a, b, c = seg
        for i in range(9):
            pnt = a + (b - a) * Fraction(i + 1, 10)
            xx, yy = (pnt, c) if kind == "h" else (c, pnt)
            dv = fd(xx, yy, Fraction(1, 20))
            rlo, rhi = PA.ball_interval(dv.real); ilo, ihi = PA.ball_interval(dv.imag)
            inside = (bx[0] <= rlo * 10 ** 12 and rhi * 10 ** 12 <= bx[1] and bx[2] <= ilo * 10 ** 12 and ihi * 10 ** 12 <= bx[3])
            nE += 1; okE += inside
            if not inside:
                failures += 1
        log(f"   segment {kind} from {float(a - (X if kind=='h' else 0)):.4f} to {float(b - (X if kind=='h' else 0)):.4f} at {float(c - (X if kind=='v' else 0)):.4f}: box half-widths {(bx[1]-bx[0])/2e12:.2e} x {(bx[3]-bx[2])/2e12:.2e}, r={float(info[6]):.2e} (D-A10 {float(info[7]):.2e}, D-A10' {float(info[8]):.2e})")
    log(f"   hull-box containment: {okE}/{nE}")
    verdict = "ALL PASS" if failures == 0 else f"FAIL ({failures} failing checks)"
    log(f"VERDICT: {verdict}  (total {time.time()-T0:.0f} s)")


if __name__ == "__main__":
    main()
