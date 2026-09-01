"""audit_F_slack.py -- AUDIT F: how far are the mp leg's EMITTED integer rows from being
changed by a sub-ulp endpoint error?  Re-runs producer_mp's mesh + argument machinery on the
t100 null box and the DH live-fire box (deterministic; the emitted rows are identical to the
acceptance files, verified in audit_F_reproduce.log), and reports the minimum "rounding
slack" min(K*lo - floor(K*lo), ceil(K*hi) - K*hi) over all value rows and the analogous
argument-row slack at scale A.  If the minimum slack exceeds the platform error budget
(finding F-1: <= ~10^4 transcendental ops x 2^-286 relative per evaluation, i.e. < 1e-80 on
values of size O(1..10^2)), the emitted integer rows are provably unaffected by F-1 for
these transcripts."""
from fractions import Fraction
from ball import set_prec, ivmpf_bounds
from producer_mp import FUNCTIONS, build_mesh, argument_rows, floor_fr, ceil_fr
import producer_mp
from mpmath import iv

K, A = 10 ** 30, 10 ** 12
set_prec(288)
for function, rect in (("zeta", (Fraction(3, 5), Fraction(9, 10), Fraction(100), Fraction(101))),
                       ("f_DH", (Fraction(4, 5), Fraction(41, 50), Fraction(8569, 100), Fraction(8571, 100)))):
    fball = FUNCTIONS[function]
    stats = {"evals": 0, "point_evals": 0}
    segments, mesh = build_mesh(fball, rect, Fraction(1, 20), K, 14, stats, lambda s: None)
    minslack = Fraction(10)
    for sg in segments:
        for lo, hi in (sg.box.re_bounds(), sg.box.im_bounds()):
            minslack = min(minslack, K * lo - floor_fr(K * lo), ceil_fr(K * hi) - K * hi)
    # argument rows: replicate argument_rows but capture the pre-rounding interval
    cache = {}
    def endpoint_ball(pt):
        if pt not in cache:
            cache[pt] = fball(producer_mp.Ball.from_fractions(pt[0], pt[1]))
        return cache[pt]
    two_pi = 2 * iv.pi; Aiv = producer_mp.iv_from_int(A)
    minaslack = Fraction(10)
    for sg in segments:
        p_start, p_end = producer_mp.seg_endpoints(sg.edge, sg.a, sg.b, rect)
        th = [endpoint_ball(pt).intersect(sg.box).arg_branch(sg.tag) for pt in (p_start, p_end)]
        lo, hi = ivmpf_bounds((th[1] - th[0]) / two_pi * Aiv)
        minaslack = min(minaslack, lo - floor_fr(lo), ceil_fr(hi) - hi)
    print("%-5s %s: %d segments; min value-row rounding slack = %.3e (units of 1/K); min argument-row slack = %.3e (units of 1/A)"
          % (function, rect, len(segments), float(minslack), float(minaslack)))
print("Interpretation: an endpoint error e changes an emitted integer bound only if K*e (resp. A*e) exceeds the slack; F-1's per-evaluation budget is < 1e-80 absolute on these values (K*e < 1e-50, A*e < 1e-68).")
