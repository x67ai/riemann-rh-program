"""audit_O_encl_honesty.py -- AUDITOR O (independent audit of D1 M1 v1, Session 14).

Enclosure-honesty test of the Session-8 mpmath-ball evaluators, with the
auditor's OWN random seeds and OWN regime list (NOT the Session-8 validation
seeds 1859 / 1914 / 5).  For each sampled point s the dps-100 (and, in the
edge regimes, dps-140) mpmath reference value must lie inside the claimed
enclosure; membership is decided in EXACT Fraction arithmetic on the mpf
endpoints, with an inflation of 10^-90 that only absorbs the REFERENCE's own
rounding (enclosure widths here are 1e-25..1e-13, i.e. 60+ orders wider).

Regimes exercised (task item 2):
  Z1  zeta, sigma in (0.501, 0.999),  |t| <= 200          (base regime)
  Z2  zeta, sigma in (0.5000001, 0.502)                   (sigma NEAR 1/2)
  Z3  zeta, sigma in (0.998, 0.9999999)                   (sigma NEAR 1)
  Z4  zeta, sigma in (0.6, 0.9), t in [9999, 10002]       (LARGEST acceptance height)
  Z5  zeta, WIDE boxes, 9 interior sample points each
  H1  hurwitz, a in {1/5,2/5,3/5,4/5} and random p/q, base + edge sigmas
  H2  hurwitz, a = 1 vs zeta (identity cross-check)
  D1  f_DH random points
  D2  f_DH at / around the off-line zero rho_DH (the live-fire target)
  D3  f_DH on the live-fire rectangle boundary itself

Run: python3 audit_O_encl_honesty.py            (writes audit_O_encl_honesty.txt)
"""
import random, sys, time
from fractions import Fraction

from mpmath import mp, iv
from ball import Ball, set_prec, mpf_tuple_to_fraction as m2f, ivmpf_bounds
from zeta_encl import zeta_ball
from hurwitz_encl import hurwitz_ball
from producer_mp import f_dh_ball, kappa_iv

SEED = 902_2026_14            # auditor O's own seed, not Session 8's
PREC = 288
EPS = Fraction(1, 10 ** 90)

rng = random.Random(SEED)
set_prec(PREC)
mp.dps = 100

fails = []
nchecks = 0


def rat(lo, hi, den):
    return Fraction(rng.randint(int(lo * den), int(hi * den)), den)


def mpf_of(fr):
    return mp.mpf(fr.numerator) / mp.mpf(fr.denominator)


def member(z, ref, label, extra=""):
    """Exact membership of an mp reference complex value in a Ball."""
    global nchecks
    nchecks += 1
    rlo, rhi = z.re_bounds()
    ilo, ihi = z.im_bounds()
    zr, zi = m2f(ref.real._mpf_), m2f(ref.imag._mpf_)
    ok = (rlo - EPS <= zr <= rhi + EPS) and (ilo - EPS <= zi <= ihi + EPS)
    if not ok:
        # by how much, in units of the enclosure width
        dr = max(rlo - zr, zr - rhi, 0)
        di = max(ilo - zi, zi - ihi, 0)
        fails.append("%s %s  miss_re=%.3e miss_im=%.3e width=%.3e"
                     % (label, extra, float(dr), float(di), float(z.max_width())))
    return ok


def run():
    t0 = time.time()
    out = []

    def say(s):
        print(s); sys.stdout.flush(); out.append(s)

    say("AUDIT O -- enclosure honesty, seed %d, iv prec %d bits, eps 1e-90" % (SEED, PREC))

    # ---------------- Z1 base regime
    w = []
    for k in range(60):
        sig = rat(0.501, 0.999, 10 ** 7)
        t = rat(-200, 200, 10 ** 6)
        z = zeta_ball(Ball.from_fractions(sig, t))
        ref = mp.zeta(mp.mpc(mpf_of(sig), mpf_of(t)))
        member(z, ref, "Z1", "s=%s+%si" % (sig, t))
        w.append(z.max_width())
    w.sort()
    say("Z1 zeta base    : 60 pts, widths med %.3e max %.3e, fails %d"
        % (float(w[30]), float(w[-1]), len(fails)))

    # ---------------- Z2 sigma near 1/2
    n0 = len(fails)
    w = []
    for k in range(30):
        sig = rat(0.5000001, 0.502, 10 ** 9)
        t = rat(-200, 200, 10 ** 6)
        z = zeta_ball(Ball.from_fractions(sig, t))
        ref = mp.zeta(mp.mpc(mpf_of(sig), mpf_of(t)))
        member(z, ref, "Z2", "s=%s+%si" % (sig, t))
        w.append(z.max_width())
    w.sort()
    say("Z2 sigma~1/2    : 30 pts, widths med %.3e max %.3e, fails %d"
        % (float(w[15]), float(w[-1]), len(fails) - n0))

    # ---------------- Z3 sigma near 1
    n0 = len(fails)
    w = []
    for k in range(30):
        sig = rat(0.998, 0.9999999, 10 ** 9)
        t = rat(-200, 200, 10 ** 6)
        z = zeta_ball(Ball.from_fractions(sig, t))
        ref = mp.zeta(mp.mpc(mpf_of(sig), mpf_of(t)))
        member(z, ref, "Z3", "s=%s+%si" % (sig, t))
        w.append(z.max_width())
    w.sort()
    say("Z3 sigma~1      : 30 pts, widths med %.3e max %.3e, fails %d"
        % (float(w[15]), float(w[-1]), len(fails) - n0))

    # ---------------- Z4 largest acceptance height
    n0 = len(fails)
    w = []
    for k in range(12):
        sig = rat(0.6, 0.9, 10 ** 6)
        t = rat(9999, 10002, 10 ** 6)
        if k % 3 == 2:
            t = -t
        z = zeta_ball(Ball.from_fractions(sig, t))
        ref = mp.zeta(mp.mpc(mpf_of(sig), mpf_of(t)))
        member(z, ref, "Z4", "s=%s+%si" % (sig, t))
        w.append(z.max_width())
    w.sort()
    say("Z4 |t|~1e4      : 12 pts, widths med %.3e max %.3e, fails %d"
        % (float(w[6]), float(w[-1]), len(fails) - n0))

    # ---------------- Z5 wide boxes
    n0 = len(fails)
    for k in range(12):
        sig = rat(0.55, 0.95, 10 ** 6)
        t = rat(-150, 150, 10 ** 6)
        dsig = Fraction(rng.randint(1, 400), 10 ** 4)
        dt = Fraction(rng.randint(1, 400), 10 ** 4)
        z = zeta_ball(Ball.from_fraction_boxes((sig, sig + dsig), (t, t + dt)))
        for u in (Fraction(0), Fraction(1, 3), Fraction(1)):
            for v in (Fraction(0), Fraction(2, 5), Fraction(1)):
                ps, pt = sig + dsig * u, t + dt * v
                ref = mp.zeta(mp.mpc(mpf_of(ps), mpf_of(pt)))
                member(z, ref, "Z5", "box(%s,%s)+(%s,%s)@(%s,%s)" % (sig, t, dsig, dt, u, v))
    say("Z5 wide boxes   : 12 boxes x 9 pts, fails %d" % (len(fails) - n0))

    # ---------------- H1 hurwitz
    n0 = len(fails)
    w = []
    shifts = [Fraction(1, 5), Fraction(2, 5), Fraction(3, 5), Fraction(4, 5)]
    for k in range(60):
        if k % 5 == 4:
            qd = rng.randint(2, 60); a = Fraction(rng.randint(1, qd), qd)
        else:
            a = shifts[k % 4]
        if k % 7 == 0:
            sig = rat(0.5000001, 0.503, 10 ** 9)
        elif k % 7 == 1:
            sig = rat(0.997, 0.9999999, 10 ** 9)
        else:
            sig = rat(0.501, 0.999, 10 ** 7)
        t = rat(-200, 200, 10 ** 6)
        z = hurwitz_ball(Ball.from_fractions(sig, t), a)
        ref = mp.zeta(mp.mpc(mpf_of(sig), mpf_of(t)), mpf_of(a))
        member(z, ref, "H1", "s=%s+%si a=%s" % (sig, t, a))
        w.append(z.max_width())
    w.sort()
    say("H1 hurwitz      : 60 pts, widths med %.3e max %.3e, fails %d"
        % (float(w[30]), float(w[-1]), len(fails) - n0))

    # ---------------- H2 a = 1 identity
    n0 = len(fails); ov = 0
    for k in range(15):
        sig = rat(0.51, 0.99, 10 ** 6)
        t = rat(-120, 120, 10 ** 6)
        s = Ball.from_fractions(sig, t)
        zh, zz = hurwitz_ball(s, Fraction(1)), zeta_ball(s)
        ref = mp.zeta(mp.mpc(mpf_of(sig), mpf_of(t)))
        member(zh, ref, "H2h", "s=%s+%si" % (sig, t))
        member(zz, ref, "H2z", "s=%s+%si" % (sig, t))
        if zh.intersect(zz) is None:
            ov += 1
    say("H2 a=1 identity : 15 pts, overlap failures %d, containment fails %d"
        % (ov, len(fails) - n0))

    # ---------------- kappa
    klo, khi = ivmpf_bounds(kappa_iv())
    mp.dps = 140
    kref = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
    kref_fr = m2f(kref._mpf_)
    kok = klo - EPS <= kref_fr <= khi + EPS
    # independent identity: kappa should equal tan(theta), eps_chi = e^{2 i theta}
    tau = sum(mp.e ** (2j * mp.pi * n / 5) * {1: 1, 2: 1j, 3: -1j, 4: -1}[n] for n in (1, 2, 3, 4))
    eps_chi = tau / (1j * mp.sqrt(5))
    theta = mp.arg(eps_chi) / 2
    tan_theta = mp.tan(theta)
    say("KAPPA           : iv=[%.30f, %.30f] surd-ref %.30f in? %s ; tan(theta)=%.30f  |diff|=%.3e"
        % (float(klo), float(khi), float(kref), kok, float(tan_theta),
           float(abs(tan_theta - kref))))
    if not kok:
        fails.append("KAPPA surd reference outside interval")
    mp.dps = 100

    # ---------------- D1 f_DH random points
    n0 = len(fails)
    w = []
    for k in range(60):
        sig = rat(0.501, 0.999, 10 ** 7)
        t = rat(-120, 120, 10 ** 6)
        z = f_dh_ball(Ball.from_fractions(sig, t))
        ref = (mp.mpf(5) ** (-mp.mpc(mpf_of(sig), mpf_of(t)))) * (
            mp.zeta(mp.mpc(mpf_of(sig), mpf_of(t)), mp.mpf(1) / 5)
            + kref * mp.zeta(mp.mpc(mpf_of(sig), mpf_of(t)), mp.mpf(2) / 5)
            - kref * mp.zeta(mp.mpc(mpf_of(sig), mpf_of(t)), mp.mpf(3) / 5)
            - mp.zeta(mp.mpc(mpf_of(sig), mpf_of(t)), mp.mpf(4) / 5))
        member(z, ref, "D1", "s=%s+%si" % (sig, t))
        w.append(z.max_width())
    w.sort()
    say("D1 f_DH random  : 60 pts, widths med %.3e max %.3e, fails %d"
        % (float(w[30]), float(w[-1]), len(fails) - n0))

    # ---------------- D2 at the off-line zero
    n0 = len(fails)
    rho_re = Fraction("0.808517182456637")
    rho_im = Fraction("85.699348485377592")
    for (dr, di) in [(0, 0), (Fraction(1, 10 ** 6), 0), (0, Fraction(1, 10 ** 6)),
                     (Fraction(-1, 10 ** 4), Fraction(1, 10 ** 4)),
                     (Fraction(1, 100), Fraction(-1, 100))]:
        ps, pt = rho_re + dr, rho_im + di
        z = f_dh_ball(Ball.from_fractions(ps, pt))
        sc = mp.mpc(mpf_of(ps), mpf_of(pt))
        ref = (mp.mpf(5) ** (-sc)) * (
            mp.zeta(sc, mp.mpf(1) / 5) + kref * mp.zeta(sc, mp.mpf(2) / 5)
            - kref * mp.zeta(sc, mp.mpf(3) / 5) - mp.zeta(sc, mp.mpf(4) / 5))
        member(z, ref, "D2", "rho+(%s,%s)" % (dr, di))
        alo, ahi = ivmpf_bounds(z.abs_iv())
        say("   D2 rho+(%s,%s): |f| in [%.3e, %.3e], |ref|=%.3e"
            % (dr, di, float(alo), float(ahi), float(abs(ref))))
    say("D2 at rho_DH    : 5 pts, fails %d" % (len(fails) - n0))

    say("TOTAL: %d membership checks, %d FAILURES, %.1f s" % (nchecks, len(fails), time.time() - t0))
    for f in fails:
        say("  FAIL " + f)
    with open("audit_O_encl_honesty.txt", "w") as fh:
        fh.write("\n".join(out) + "\n")
    return len(fails)


if __name__ == "__main__":
    sys.exit(0 if run() == 0 else 1)
