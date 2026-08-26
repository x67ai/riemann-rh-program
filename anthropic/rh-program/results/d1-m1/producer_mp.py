"""producer_mp.py -- the mpmath-ball W1 TRANSCRIPT PRODUCER (D-R3 named work item).

D1 M1 v1.  UNTRUSTED by design: this program manufactures W1 rectangle
transcripts (FORMAT.md v1.0 in this directory); everything it asserts enters
the trusted statement only through the displayed hypothesis H-ENCL
(FORMAT.md sec. 8.1).  The checker (Lean; reference implementations
checker_ref.py and reference_checker.py here) re-verifies all integer
conditions C1-C11 from the emitted file and trusts nothing below.

WHAT IT DOES
============
Given an exact-rational rectangle R = [sigma1, sigma2] x [T1, T2] in the
critical strip, a target function (zeta | f_DH) and a mode
(exclusion | refutation), it:

 1. walks the counterclockwise boundary mesh in the FORMAT.md sec. 4 order
    (bottom: sigma1 -> sigma2; right: T1 -> T2; top: sigma2 -> sigma1
    DECREASING; left: T2 -> T1 DECREASING), starting from a uniform mesh of
    step ~h0 per edge;
 2. computes, for every segment, a WHOLE-SEGMENT complex-ball enclosure of f
    (zeta_encl.py / hurwitz_encl.py evaluated at a BOX argument -- inclusion
    monotonicity makes one evaluation cover the entire closed segment,
    corners included), BISECTING the segment (exact rational midpoint) until
    the box certifies an open coordinate half-plane AND the sign witness
    survives integer rounding at scale K (the C6 mesh-admissibility criterion,
    FORMAT.md sec. 5.1/6.2 -- if the maximum depth is exhausted the producer
    STOPS and reports "zero on or near the boundary; move the rectangle",
    per the contract's mandated response);
 3. computes per-segment argument-increment enclosures WITHOUT ANY DERIVATIVE
    (zeta'/zeta-free): by FORMAT.md derivations D1-D3 the segment image lies
    in one open half-plane, on which the segment's branch theta_tag (ball.py,
    with derivations) is a continuous branch of arg f; therefore

        Delta_k = theta(1) - theta(0) = theta_tag(f(end)) - theta_tag(f(start))

    -- the FIRST equality is FORMAT.md derivation D2 (Delta_k, defined as
    Im of the segment integral of f'/f, equals the increment of any
    continuous argument branch along the path), and the SECOND holds because
    theta_tag composed with f o gamma is itself a continuous argument branch
    along the path (the path's image lies in the half-plane), and two
    continuous branches along the same path differ by a constant 2*pi*n
    (their difference is continuous, integer-valued in units of 2*pi, on a
    connected interval), so the endpoint DIFFERENCE is branch-independent.
    Producer recipe as recorded in FORMAT.md sec. 10: endpoint values are
    enclosed by thin point evaluations INTERSECTED with the whole-segment box
    (both enclose the same point value, so the intersection does; it is
    nonempty or the producer stops the line), the branch interval is
    evaluated on those, divided by 2*pi (interval pi), scaled by A, OUTWARD
    rounded to integers, and clamped to [-A/2, A/2] (sound by D3);
 4. sums the argument rows, extracts the UNIQUE integer m with
    S_lo <= A*m <= S_hi (uniqueness forced by the producer-side width check
    mirroring C8), verifies the mode<->m consistency (C10) HONESTLY -- a
    mismatch aborts the run rather than emitting a wrong-mode transcript;
 5. derives the optional modulus_floor row from the integer value boxes
    (Fn = isqrt(min_k(mre_k^2 + mim_k^2)), Fd = K, so C11 holds by
    construction of isqrt);
 6. emits the FORMAT.md/w1-schema.json-conformant JSON transcript (all
    integers as decimal strings; exact rationals as n/d pairs; fixed verbatim
    trust label per function) plus untrusted producer metadata.

INTEGER ROUNDING IS EXACT: iv endpoints are binary rationals, converted
losslessly to Fractions (ball.py), multiplied by K (or A) in exact rational
arithmetic, and floor/ceil'd exactly.  No float touches any emitted number.

THE TARGET FUNCTIONS
====================
  zeta : zeta_encl.zeta_ball (Euler-Maclaurin, derived remainder, validated).
  f_DH : the Davenport-Heilbronn function, definition quoted VERBATIM from
         the on-disk validated source results/ccm-dh-test/dh.py lines 5-8:

           f_DH(s) = 5^{-s} [ zeta(s,1/5) + kap*zeta(s,2/5)
                              - kap*zeta(s,3/5) - zeta(s,4/5) ]
           kap = (sqrt(10-2*sqrt5) - 2)/(sqrt5 - 1)

         implemented here with hurwitz_encl.hurwitz_ball for the four shifts,
         kap as a directed-rounded iv surd expression, and 5^{-s} =
         exp(-s log 5).  `--selftest-dh` cross-validates this ball
         implementation against the dh.py float implementation (imported from
         its on-disk path) at dps 100, including at the certified off-line
         zero rho_DH = 0.808517182456637 + 85.699348485377592i (D1 direction
         file line 104).  Per D-R8 an f_DH transcript is CHECKER-LEVEL ONLY;
         the trust label written into the file says exactly that.

USAGE
=====
  python3 producer_mp.py --function zeta --mode exclusion \
      --rect 3/5 7/10 10 11 --out w1-zeta-exclusion-t10.json
  python3 producer_mp.py --function f_DH --mode refutation \
      --rect 31/40 17/20 171/2 429/5 --out w1-dh-refutation-live-fire.json
  python3 producer_mp.py --selftest-dh

Options: --h0 F (initial mesh step, default 1/20), --maxdepth N (default 14),
--prec BITS (default 288), --K 10^k exponent (default 30), --A 10^k exponent
(default 12), --floor/--no-floor (default on).

THERMAL: single process, no parallelism (well under the 4-process cap).
"""

import argparse
import datetime
import json
import math
import os
import sys
import time
from fractions import Fraction

import mpmath
from mpmath import iv

from ball import (Ball, iv_from_fraction, iv_from_int, ivmpf_bounds, set_prec)
from zeta_encl import zeta_ball, pow_int_neg
from hurwitz_encl import hurwitz_ball

TRUST_LABELS = {
    "zeta": "kernel-checked modulo displayed hypotheses H-ENCL and H-AP (producers untrusted)",
    "f_DH": "checker-level only (D-R8): format-checked modulo H-ENCL for f_DH; no Lean-backed conclusion",
}

RHO_DH_RE = "0.808517182456637"
RHO_DH_IM = "85.699348485377592"


# ---------------------------------------------------------------- target functions

def kappa_iv():
    """kap = (sqrt(10 - 2 sqrt 5) - 2)/(sqrt 5 - 1), directed-rounded interval."""
    s5 = iv.sqrt(iv_from_int(5))
    return (iv.sqrt(iv_from_int(10) - 2 * s5) - iv_from_int(2)) / (s5 - iv_from_int(1))


def f_dh_ball(s_ball):
    k = kappa_iv()
    h1 = hurwitz_ball(s_ball, Fraction(1, 5))
    h2 = hurwitz_ball(s_ball, Fraction(2, 5))
    h3 = hurwitz_ball(s_ball, Fraction(3, 5))
    h4 = hurwitz_ball(s_ball, Fraction(4, 5))
    comb = h1 + h2.scale_iv(k) - h3.scale_iv(k) - h4
    return pow_int_neg(5, s_ball) * comb


FUNCTIONS = {"zeta": zeta_ball, "f_DH": f_dh_ball}


# ---------------------------------------------------------------- exact rounding helpers

def floor_fr(fr):
    return fr.numerator // fr.denominator


def ceil_fr(fr):
    return -((-fr.numerator) // fr.denominator)


def value_row_ints(box, K):
    """Outward integer rounding of the box at scale K (exact)."""
    rlo, rhi = box.re_bounds()
    ilo, ihi = box.im_bounds()
    return (floor_fr(K * rlo), ceil_fr(K * rhi), floor_fr(K * ilo), ceil_fr(K * ihi))


def c6_ints(row):
    reLo, reHi, imLo, imHi = row
    return reLo > 0 or reHi < 0 or imLo > 0 or imHi < 0


# ---------------------------------------------------------------- mesh machinery

class Segment(object):
    __slots__ = ("edge", "a", "b", "box", "tag", "vrow")

    def __init__(self, edge, a, b, box, tag, vrow):
        self.edge, self.a, self.b = edge, a, b
        self.box, self.tag, self.vrow = box, tag, vrow


def seg_ball(edge, a, b, rect):
    """The complex box covering the closed segment (a, b are the varying
    coordinate in TRAVERSAL order; a > b on top/left)."""
    s1, s2, t1, t2 = rect
    lo, hi = (a, b) if a <= b else (b, a)
    if edge == "bottom":
        return Ball.from_fraction_boxes((lo, hi), (t1, t1))
    if edge == "right":
        return Ball.from_fraction_boxes((s2, s2), (lo, hi))
    if edge == "top":
        return Ball.from_fraction_boxes((lo, hi), (t2, t2))
    if edge == "left":
        return Ball.from_fraction_boxes((s1, s1), (lo, hi))
    raise ValueError(edge)


def seg_endpoints(edge, a, b, rect):
    """(sigma, t) exact coordinates of start and end breakpoints, traversal order."""
    s1, s2, t1, t2 = rect
    if edge == "bottom":
        return (a, t1), (b, t1)
    if edge == "right":
        return (s2, a), (s2, b)
    if edge == "top":
        return (a, t2), (b, t2)
    if edge == "left":
        return (s1, a), (s1, b)
    raise ValueError(edge)


def refine_edge(fball, edge, a, b, rect, K, maxdepth, stats, depth=0):
    """Recursively bisect until the segment box certifies a half-plane and the
    sign witness survives integer rounding at scale K."""
    box = fball(seg_ball(edge, a, b, rect))
    stats["evals"] += 1
    tag = box.halfplane()
    if tag is not None:
        vrow = value_row_ints(box, K)
        if c6_ints(vrow):
            return [Segment(edge, a, b, box, tag, vrow)]
    if depth >= maxdepth:
        raise SystemExit(
            "PRODUCER STOP (%s edge, [%s, %s], depth %d): cannot certify a "
            "0-excluding value box -- a zero of f lies on or near the boundary. "
            "Per FORMAT.md sec. 6.2 the correct response is to MOVE the "
            "rectangle, never to weaken the criterion." % (edge, a, b, depth))
    mid = (a + b) / 2
    return (refine_edge(fball, edge, a, mid, rect, K, maxdepth, stats, depth + 1)
            + refine_edge(fball, edge, mid, b, rect, K, maxdepth, stats, depth + 1))


def build_mesh(fball, rect, h0, K, maxdepth, stats, log):
    """All four edges in traversal order; returns (segments, mesh_lists)."""
    s1, s2, t1, t2 = rect
    edges = [("bottom", s1, s2), ("right", t1, t2), ("top", s2, s1), ("left", t2, t1)]
    segments = []
    mesh = {}
    for edge, start, end in edges:
        n0 = max(1, int(math.ceil(abs(float(end - start)) / float(h0))))
        pieces = [start + (end - start) * Fraction(i, n0) for i in range(n0 + 1)]
        segs = []
        tE = time.time()
        for i in range(n0):
            segs.extend(refine_edge(fball, edge, pieces[i], pieces[i + 1],
                                    rect, K, maxdepth, stats))
        mesh[edge] = [sg.a for sg in segs] + [segs[-1].b]
        segments.extend(segs)
        log("  edge %-6s: %3d segments (%.1fs, %d evals so far)"
            % (edge, len(segs), time.time() - tE, stats["evals"]))
    return segments, mesh


# ---------------------------------------------------------------- argument rows

def argument_rows(fball, segments, rect, A, stats, log):
    """Per-segment [argLo, argHi] integer rows in turn units at scale A."""
    cache = {}

    def endpoint_ball(pt):
        if pt not in cache:
            cache[pt] = fball(Ball.from_fractions(pt[0], pt[1]))
            stats["point_evals"] += 1
        return cache[pt]

    rows = []
    two_pi = 2 * iv.pi
    Aiv = iv_from_int(A)
    for k, sg in enumerate(segments):
        p_start, p_end = seg_endpoints(sg.edge, sg.a, sg.b, rect)
        th = []
        for pt in (p_start, p_end):
            thin = endpoint_ball(pt)
            inter = thin.intersect(sg.box)
            if inter is None:
                raise SystemExit(
                    "PRODUCER STOP (segment %d, %s): thin endpoint enclosure "
                    "and whole-segment box are DISJOINT -- an enclosure bug "
                    "(stop-the-line event per m2a-m2b-design sec. 4)." % (k, sg.edge))
            th.append(inter.arg_branch(sg.tag))
        scaled = (th[1] - th[0]) / two_pi * Aiv
        lo, hi = ivmpf_bounds(scaled)
        argLo, argHi = floor_fr(lo), ceil_fr(hi)
        # D3 clamp (sound: the true increment lies in the intersection)
        argLo = max(argLo, -(A // 2))
        argHi = min(argHi, A // 2)
        if argLo > argHi:
            raise SystemExit(
                "PRODUCER STOP (segment %d): argument row empty after the D3 "
                "clamp -- enclosure inconsistency (stop-the-line)." % k)
        rows.append((argLo, argHi))
    return rows


# ---------------------------------------------------------------- assembly

def produce(function, mode, rect, out_path, h0=Fraction(1, 20), maxdepth=14,
            prec=288, K=10 ** 30, A=10 ** 12, want_floor=True, log=print):
    t0 = time.time()
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    set_prec(prec)
    s1, s2, t1, t2 = rect
    # producer-side rectangle sanity (the checker re-verifies as C2)
    if not (Fraction(1, 2) < s1 <= s2 < 1 and t1 < t2):
        raise SystemExit("bad rectangle: need 1/2 < sigma1 <= sigma2 < 1, T1 < T2")
    fball = FUNCTIONS[function]
    stats = {"evals": 0, "point_evals": 0}
    log("producer_mp: function=%s mode=%s rect=[%s, %s]x[%s, %s] prec=%d K=1e%d A=1e%d"
        % (function, mode, s1, s2, t1, t2, prec,
           len(str(K)) - 1, len(str(A)) - 1))
    segments, mesh = build_mesh(fball, rect, h0, K, maxdepth, stats, log)
    arows = argument_rows(fball, segments, rect, A, stats, log)

    S_lo = sum(r[0] for r in arows)
    S_hi = sum(r[1] for r in arows)
    log("  winding sum: S_lo=%d S_hi=%d width=%d (A=%d; C8 needs 2*width < A)"
        % (S_lo, S_hi, S_hi - S_lo, A))
    if not 2 * (S_hi - S_lo) < A:
        raise SystemExit("PRODUCER STOP: winding enclosure too wide for C8; "
                         "refine the mesh (raise precision or lower h0).")
    m_min = -((-S_lo) // A)   # ceil(S_lo/A)
    m_max = S_hi // A          # floor(S_hi/A)
    if m_min > m_max:
        raise SystemExit("PRODUCER STOP: no integer winding in [S_lo/A, S_hi/A] "
                         "-- enclosure bug (the true sum is an exact integer).")
    if m_min != m_max:
        raise SystemExit("PRODUCER STOP: winding ambiguous (width >= 1 turn?).")
    m = m_min
    log("  winding number m = %d (unique by width < 1/2 turn)" % m)
    if m < 0:
        raise SystemExit("PRODUCER STOP: negative winding for an analytic "
                         "function -- enclosure bug (stop-the-line).")
    if mode == "exclusion" and m != 0:
        raise SystemExit("PRODUCER STOP: mode=exclusion requested but certified "
                         "winding m=%d != 0.  Not emitting a false-mode "
                         "transcript." % m)
    if mode == "refutation" and m < 1:
        raise SystemExit("PRODUCER STOP: mode=refutation requested but certified "
                         "winding m=0 -- no zero in this rectangle.  Not "
                         "emitting." % ())

    # optional modulus floor (C11 holds by isqrt construction)
    floor_obj = None
    if want_floor:
        mins = []
        for sg in segments:
            reLo, reHi, imLo, imHi = sg.vrow
            mre = 0 if reLo <= 0 <= reHi else min(abs(reLo), abs(reHi))
            mim = 0 if imLo <= 0 <= imHi else min(abs(imLo), abs(imHi))
            mins.append(mre * mre + mim * mim)
        fn = math.isqrt(min(mins))
        if fn >= 1:
            floor_obj = {"Fn": str(fn), "Fd": str(K)}
            log("  modulus floor: |f| >= %d / 1e%d on dR" % (fn, len(str(K)) - 1))

    def rat(fr):
        return {"n": str(fr.numerator), "d": str(fr.denominator)}

    doc = {
        "format": "W1-rect-transcript",
        "version": "1.0",
        "mode": mode,
        "function": function,
        "trust_label": TRUST_LABELS[function],
        "rect": {"sigma1": rat(s1), "sigma2": rat(s2), "T1": rat(t1), "T2": rat(t2)},
        "scales": {"K": str(K), "A": str(A)},
        "claimed_m": str(m),
        "mesh": {e: [rat(v) for v in mesh[e]] for e in ("bottom", "right", "top", "left")},
        "segments": [
            {"reLo": str(sg.vrow[0]), "reHi": str(sg.vrow[1]),
             "imLo": str(sg.vrow[2]), "imHi": str(sg.vrow[3]),
             "argLo": str(ar[0]), "argHi": str(ar[1])}
            for sg, ar in zip(segments, arows)
        ],
        "producer": {
            "implementation": "producer_mp.py (mpmath-ball leg, D-R3)",
            "mpmath_version": mpmath.__version__,
            "python_version": sys.version.split()[0],
            "iv_prec_bits": prec,
            "euler_maclaurin": "m=14, N=max(20, ceil(0.5*(t_max+2m+1))); "
                               "remainder bound derived in zeta_encl.py / "
                               "hurwitz_encl.py docstrings (constant-2 "
                               "Backlund-style, certified C_{2m+2})",
            "subdivision_policy": "uniform h0=%s then bisection to depth<=%d "
                                  "until ball half-plane + integer C6" % (h0, maxdepth),
            "argument_policy": "derivative-free: per-segment half-plane branch, "
                               "endpoint thin-ball intersect segment-box, "
                               "outward-rounded, D3-clamped (FORMAT.md sec. 10)",
            "segment_evals": stats["evals"],
            "endpoint_evals": stats["point_evals"],
            "started_utc": started,
            "finished_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "wall_seconds": round(time.time() - t0, 1),
        },
        "comment": "UNTRUSTED producer output (mpmath-ball leg). Accepted only "
                   "modulo H-ENCL (+ H-AP for zeta); see trust_label.",
    }
    if floor_obj is not None:
        doc["modulus_floor"] = floor_obj
    with open(out_path, "w") as fh:
        json.dump(doc, fh, indent=1)
    log("  wrote %s (%d segments, %.1fs total)"
        % (out_path, len(segments), time.time() - t0))
    return doc


# ---------------------------------------------------------------- DH cross-validation

def selftest_dh(prec=288):
    """Cross-validate f_dh_ball against the on-disk dh.py float implementation
    (imported by path; the program's triple-validated DH source) at dps 100."""
    import importlib.util
    import random
    from mpmath import mp
    from ball import mpf_tuple_to_fraction as m2f

    here = os.path.dirname(os.path.abspath(__file__))
    dh_path = os.path.normpath(os.path.join(here, "..", "ccm-dh-test", "dh.py"))
    spec = importlib.util.spec_from_file_location("dh_ondisk", dh_path)
    dh = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dh)

    set_prec(prec)
    mp.dps = 100
    EPS = Fraction(1, 10 ** 80)
    rng = random.Random(5)
    fails = 0
    pts = []
    for k in range(24):
        sig = Fraction(rng.randint(510, 990), 1000)
        t = Fraction(rng.randint(-120000, 120000), 1000)
        pts.append((sig, t))
    print("f_DH ball cross-validation vs on-disk dh.py (%s) at dps 100, %d points"
          % (dh_path, len(pts)))
    for sig, t in pts:
        zball = f_dh_ball(Ball.from_fractions(sig, t))
        ref = dh.f_dh(mp.mpc(mp.mpf(sig.numerator) / sig.denominator,
                             mp.mpf(t.numerator) / t.denominator))
        rlo, rhi = zball.re_bounds()
        ilo, ihi = zball.im_bounds()
        ok = (rlo - EPS <= m2f(ref.real._mpf_) <= rhi + EPS and
              ilo - EPS <= m2f(ref.imag._mpf_) <= ihi + EPS)
        if not ok:
            fails += 1
            print("  FAIL at s = %s + %si" % (sig, t))
    print("  containment: %d/%d PASS" % (len(pts) - fails, len(pts)))
    # the certified off-line zero: |f_DH| enclosure must be tiny (the ball
    # contains f(rho_hat) for the 15-digit rounded rho_hat, which is ~1e-14
    # from the true zero, so expect |f| ~< 1e-13 there, not 1e-41)
    rho_re = Fraction(RHO_DH_RE)
    rho_im = Fraction(RHO_DH_IM)
    zb = f_dh_ball(Ball.from_fractions(rho_re, rho_im))
    _, ahi = ivmpf_bounds(zb.abs_iv())
    print("  |f_DH(rho_DH ~15 digits)| <= %.3e (expect ~1e-13-class: the "
          "quoted rho is a 15-digit rounding of the true zero)" % float(ahi))
    ok_zero = ahi < Fraction(1, 10 ** 10)
    if not ok_zero:
        fails += 1
        print("  FAIL: enclosure at rho_DH not small")
    return fails


# ---------------------------------------------------------------- CLI

def parse_fr(txt):
    if "/" in txt:
        n, d = txt.split("/")
        return Fraction(int(n), int(d))
    return Fraction(int(txt))


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--function", choices=("zeta", "f_DH"))
    ap.add_argument("--mode", choices=("exclusion", "refutation"))
    ap.add_argument("--rect", nargs=4, metavar=("S1", "S2", "T1", "T2"))
    ap.add_argument("--out")
    ap.add_argument("--h0", default="1/20")
    ap.add_argument("--maxdepth", type=int, default=14)
    ap.add_argument("--prec", type=int, default=288)
    ap.add_argument("--K", type=int, default=30, help="K = 10^this")
    ap.add_argument("--A", type=int, default=12, help="A = 10^this")
    ap.add_argument("--no-floor", action="store_true")
    ap.add_argument("--selftest-dh", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest_dh:
        return 1 if selftest_dh(prec=args.prec) else 0
    if not (args.function and args.mode and args.rect and args.out):
        ap.error("--function, --mode, --rect, --out are required (or --selftest-dh)")
    rect = tuple(parse_fr(x) for x in args.rect)
    produce(args.function, args.mode, rect, args.out,
            h0=parse_fr(args.h0), maxdepth=args.maxdepth, prec=args.prec,
            K=10 ** args.K, A=10 ** args.A, want_floor=not args.no_floor)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
