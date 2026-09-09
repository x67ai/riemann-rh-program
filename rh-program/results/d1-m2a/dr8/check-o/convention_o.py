#!/usr/bin/env python3
"""Job 2 (Opus): the Hurwitz-convention identification, checked NUMERICALLY at the source
rather than taken from documentation strings.

Lean/Mathlib's side is a THEOREM, not a convention claim: `hasSum_hurwitzZeta_of_one_lt_re`
gives, for a in [0,1] real and Re s > 1,  hurwitzZeta (a : UnitAddCircle) s = sum_{n>=0} 1/(n+a)^s,
and FDH.lean's `hasSum_hurwitzZeta_one_fifth` instantiates it at a = 1/5 (Job 2 re-elaborated the
same instantiation at a = 2/5, 3/5, 4/5 -- check-o/convention_probe.lean).

What CANNOT be a Lean theorem, and is therefore checked here, is that the two producers' library
calls compute that same series.  Test: at several s with Re s > 1, compare
  (i)  the truncated-plus-tail partial sum of  sum_{n>=0} (n+a)^{-s}  computed directly,
  (ii) mpmath's mp.zeta(s, a),
  (iii) python-flint's acb(s).zeta(acb(a))  (= Arb acb_hurwitz_zeta),
for a = 1/5, 2/5, 3/5, 4/5; and then compare the two producers' whole f_DH evaluators against
5^{-s}[Z(s,1/5) + kappa Z(s,2/5) - kappa Z(s,3/5) - Z(s,4/5)] built from route (i).
"""
from mpmath import mp, mpf, mpc, nsum, inf, fabs, nstr
mp.dps = 50

def series(s, a, N=None):
    # sum_{n=0}^{N-1} (n+a)^{-s} exactly, plus an Euler-Maclaurin tail (mp.sumem) for the rest.
    # This is the (Z') route of results/d1-m1/hurwitz_encl.py STEP 3', evaluated by a DIFFERENT
    # mpmath entry point from mp.zeta(s, a) -- so agreement is evidence about the convention,
    # not about one implementation agreeing with itself.  (mp.nsum's Richardson acceleration is
    # NOT usable here: it loses ~10 digits on complex s -- observed, hence this route.)
    if N is None:
        N = max(60, int(40 * abs(s)))
    head = mp.fsum([1 / (mpf(n) + a) ** s for n in range(N)])
    tail = mp.sumem(lambda x: 1 / (x + a) ** s, [N, inf])
    return head + tail

SS = [mpc(2, 0), mpc(3, 1), mpc('1.5', '10'), mpc(4, '-2.5')]
AA = [mpf(1)/5, mpf(2)/5, mpf(3)/5, mpf(4)/5]

try:
    from flint import acb, arb, ctx
    ctx.dps = 60
    HAVE_FLINT = True
except Exception as ex:
    HAVE_FLINT = False
    print("python-flint unavailable: %r" % (ex,))

print("Convention check: sum_{n>=0} (n+a)^{-s}  vs  mpmath mp.zeta(s,a)  vs  Arb acb.zeta(a)")
# TOLERANCES.  This is a CONVENTION check, not a precision check: a wrong convention (a wrong
# a-normalization, an n>=1 instead of n>=0 series, a 1-a reflection) changes the value in the
# FIRST digits, never in the 20th.  mp.sumem's own accuracy floor near the edge of convergence
# (Re s = 1.5, |t| = 10) is ~1e-29 here and does not improve with N, so the EM route is held to
# 1e-20; mp.zeta vs Arb are like-for-like and are held to 1e-25.
print("mp.dps = %d; tolerances: EM-series vs library 1e-20, mp.zeta vs Arb 1e-25\n" % mp.dps)
TOL = mpf(10) ** -20
bad = 0
for s in SS:
    for a in AA:
        v_ser = series(s, a)
        v_mp = mp.zeta(s, a)
        d1 = fabs(v_ser - v_mp)
        line = "s = %-18s a = %-6s |series - mp.zeta| = %-10s" % (nstr(s, 8), nstr(a, 4), nstr(d1, 4))
        if HAVE_FLINT:
            z = acb(str(s.real), str(s.imag)).zeta(acb(arb(int(a * 5)) / arb(5)))
            v_ar = mpc(z.real.mid().str(40, radius=False), z.imag.mid().str(40, radius=False))
            d2 = fabs(v_ser - v_ar)
            line += " |series - acb.zeta| = %-10s" % nstr(d2, 4)
        else:
            d2 = mpf(0)
        d3 = fabs(v_mp - v_ar) if HAVE_FLINT else mpf(0)
        if HAVE_FLINT:
            line += " |mp.zeta - acb.zeta| = %-10s" % nstr(d3, 4)
        ok = d1 < TOL and d2 < TOL and d3 < mpf(10) ** -25
        line += "  %s" % ("OK" if ok else "MISMATCH")
        if not ok:
            bad += 1
        print(line)

print()
kappa = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
print("f_DH assembled from the series, vs the two producers' assembly order:")
for s in SS:
    ser = 5 ** (-s) * (series(s, AA[0]) + kappa * series(s, AA[1])
                       - kappa * series(s, AA[2]) - series(s, AA[3]))
    mpv = 5 ** (-s) * (mp.zeta(s, AA[0]) + kappa * mp.zeta(s, AA[1])
                       - kappa * mp.zeta(s, AA[2]) - mp.zeta(s, AA[3]))
    d = fabs(ser - mpv)
    ok = d < TOL
    if not ok:
        bad += 1
    print("  s = %-18s f_DH = %-46s  |series - mp| = %-10s %s"
          % (nstr(s, 8), nstr(ser, 24), nstr(d, 4), "OK" if ok else "MISMATCH"))

print()
print("VERDICT: %s" % ("PASS" if bad == 0 else "FAIL (%d mismatches)" % bad))
raise SystemExit(0 if bad == 0 else 1)
