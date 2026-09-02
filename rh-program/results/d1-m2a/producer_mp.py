"""producer_mp.py -- the mpmath-ball BARRIER-TRANSCRIPT PRODUCER for M2a (SPEC.md v1.0, lane B).

D1 M2a work item (d).  UNTRUSTED by design: this program manufactures M2a barrier transcripts
(``barrier-schema.json``: one ``manifest`` plus one ``prism`` file per time prism); everything it
asserts enters the trusted statement only through the displayed hypothesis H2-B (SPEC.md sections
4, 6, 8.1).  The checker (Lean; reference implementation ``barrier_ref_checker.py``) re-verifies the
integer conditions C-B0..C-B13 from the emitted files and trusts nothing below.

It is the M1 producer (``results/d1-m1/producer_mp.py``: adaptive boundary mesh, whole-segment
hull boxes, derivative-free argument rows by the half-plane branch scheme of FORMAT.md sections
5-6/10, exact integer rounding) with the target function replaced by Polymath15's f_t and with the
two extra integers per prism, E and D, from Theorem 1.3 and the time step.  The f_t evaluator is
``ft_mp.py`` (module docstring: the transcribed formulas at PDF pages and the derivations D-F1..D-F9).

WHAT ONE PRISM CERTIFIES (SPEC 4.1-4.5; H2-B) and how each item is produced here
==============================================================================
  rows   : for every boundary segment k of the rectangle R = [x1,x2] x [y1,y2], a value box with
           reLo <= K Re f <= reHi, imLo <= K Im f <= imHi for ALL z on the closed segment (f = f_tau,
           the seam approximant, N = N0 constant on R: checked by D-F3 before meshing, SPEC P-3),
           and an argument row argLo <= A Delta_k/(2 pi) <= argHi in turn units.
           value box: ``FtEvaluator.evaluate`` on the segment's z-box (inclusion-monotone; one call
           covers the closed segment, corners included), bisected until the box certifies an open
           coordinate half-plane AND the integer sign witness survives rounding at scale K (C-B6);
           argument row: as in M1 -- Delta_k = theta_tag(f(end)) - theta_tag(f(start)) with the
           segment's own half-plane branch (FORMAT.md D1-D3 + ball.py branch derivations + the
           branch-difference argument in results/d1-m1/producer_mp.py), endpoint values by thin
           evaluations intersected with the segment box, / (2 pi), x A, outward-rounded, clamped to
           [-A/2, A/2] with A even.
  floor  : Fn/Fd = isqrt(min_k(mre_k^2 + mim_k^2)) / K  (C-B11 holds by construction).
  E      : |g_tau - f_tau| <= E/K on dR, g = H_t/B_t: E = ceil(K * E_bound(tau)), E_bound = the
           D-F4 + Prop. 6.6(vi) majorant of e_A + e_B + e_{C,0} evaluated by interval arithmetic
           over the WHOLE box R at t = tau (SPEC P-6).  For tau = 0 by the limit argument D-F9 (P-7).
  D      : |g_t - g_tau| <= D/K on dR for tau <= t <= tau': D = ceil(K * (E_prism + (tau'-tau) DT + E_bound(tau)))
           (D-F7), where E_prism = the majorant with t = [tau, tau'] and DT >= sup over every mesh
           segment box x [tau, tau'] of |d/dt f_t| (``FtEvaluator.evaluate(..., want_dt=True)`` with the
           t-interval; D-F6/D-F8).  The prism length is chosen adaptively: from the seam value of
           |d/dt f| a candidate Delta t = theta * (floor - 2 E_bound(tau)) / DT_seam, verified with the
           interval-t evaluation, halved on failure of the gate (E + D) Fd < Fn K (C-B12).
  winding: S_lo <= 0 <= S_hi with 2 (S_hi - S_lo) < A (C-B8/C-B9); if the certified winding is not
           0 the producer STOPS (the rectangle would contain a zero of f: no false transcript).

OUTPUT (SPEC 7.1; all integers as decimal strings; rationals as {n, d})
  <out>/prism-NNNN.json   one per prism (written the moment the prism is done -- RULE ONE)
  <out>/manifest.json     rewritten after every prism: t0 = the last certified time (PARTIAL,
                          labeled in `comment`) until the chain reaches the instance's t0.
  <out>/progress.json     seams done, timings (resume support: ``--resume``).
  <out>/producer.log      the running log.

USAGE
  python3 producer_mp.py --instance row2 --out transcripts/row2 [--K 24] [--A 12] [--h0 1/50]
      [--maxdepth 12] [--theta 1/2] [--max-prisms N] [--max-seconds S] [--resume]
  python3 producer_mp.py --instance mini --out transcripts/mini      (N = 5000 test instance)

THERMAL: single process (the moment files are computed beforehand by ``ft_mp.py moments``).
U.S. English throughout.
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

from ft_mp import (Ball, iv_from_fraction, iv_from_int, ivmpf_bounds, set_prec, iv_pi,
                   iv_from_fraction_pair, iv_from_fr, iv_lo, iv_hi, ball_abs_hi, ball_from_fr,
                   FtEvaluator, defect_bound, check_N_constant, PREC_DEFAULT)

TRUST_LABEL = "kernel-checked modulo the displayed hypotheses H1, H2 (H2-B, H2-A, H-TAIL) and H3 (producers untrusted)"

INSTANCES = {
    "row2": {   # P15 Table 1 row 2 (p64); SPEC.md section 9
        "x1": Fraction(5000000194858), "x2": Fraction(5000000194859),
        "y1": Fraction(16733, 100000), "y2": Fraction(1),
        "t0": Fraction(93, 500), "N": 630783,
        "zc_re": Fraction(10000000389717, 2), "zc_im": Fraction(116733, 200000),
        "plus": "moments/row2-plus.json", "minus": "moments/row2-minus.json",
    },
    "mini": {   # test instance: N = 5000, x_N = 4 pi 5000^2 = 314159265.36.., X = 314159300
        "x1": Fraction(314159300), "x2": Fraction(314159301),
        "y1": Fraction(16733, 100000), "y2": Fraction(1),
        "t0": Fraction(93, 500), "N": 5000,
        "zc_re": Fraction(628318601, 2), "zc_im": Fraction(116733, 200000),
        "plus": "moments/mini-plus.json", "minus": "moments/mini-minus.json",
    },
}


# ---------------------------------------------------------------- exact rounding helpers (as M1)

def floor_fr(x):
    return x.numerator // x.denominator


def ceil_fr(x):
    return -((-x.numerator) // x.denominator)


def value_row_ints(box, K):
    rlo, rhi = box.re_bounds()
    ilo, ihi = box.im_bounds()
    return (floor_fr(K * rlo), ceil_fr(K * rhi), floor_fr(K * ilo), ceil_fr(K * ihi))


def c6_ints(row):
    reLo, reHi, imLo, imHi = row
    return reLo > 0 or reHi < 0 or imLo > 0 or imHi < 0


def nice_floor(x, digits=3):
    """The largest rational with `digits` significant decimal digits that is <= x (x > 0)."""
    x = Fraction(x)
    if x <= 0:
        return x
    e = 0
    while x * Fraction(10) ** e < 10 ** (digits - 1):
        e += 1
    while x * Fraction(10) ** e >= 10 ** digits:
        e -= 1
    return Fraction(floor_fr(x * Fraction(10) ** e), 1) / Fraction(10) ** e


def rat(x):
    x = Fraction(x)
    return {"n": str(x.numerator), "d": str(x.denominator)}


# ---------------------------------------------------------------- mesh machinery (M1, with sigma->x, T->y)

class Segment(object):
    __slots__ = ("edge", "a", "b", "box", "tag", "vrow", "zbox")

    def __init__(self, edge, a, b, box, tag, vrow, zbox):
        self.edge, self.a, self.b = edge, a, b
        self.box, self.tag, self.vrow, self.zbox = box, tag, vrow, zbox


def seg_zbox(edge, a, b, rect):
    x1, x2, y1, y2 = rect
    lo, hi = (a, b) if a <= b else (b, a)
    if edge == "bottom":
        return Ball.from_fraction_boxes((lo, hi), (y1, y1))
    if edge == "right":
        return Ball.from_fraction_boxes((x2, x2), (lo, hi))
    if edge == "top":
        return Ball.from_fraction_boxes((lo, hi), (y2, y2))
    if edge == "left":
        return Ball.from_fraction_boxes((x1, x1), (lo, hi))
    raise ValueError(edge)


def seg_endpoints(edge, a, b, rect):
    x1, x2, y1, y2 = rect
    if edge == "bottom":
        return (a, y1), (b, y1)
    if edge == "right":
        return (x2, a), (x2, b)
    if edge == "top":
        return (a, y2), (b, y2)
    if edge == "left":
        return (x1, a), (x1, b)
    raise ValueError(edge)


class Producer(object):

    def __init__(self, inst, out_dir, K, A, h0, maxdepth, theta, prec, log):
        self.inst = inst
        self.out = out_dir
        self.K, self.A = K, A
        self.h0, self.maxdepth, self.theta = h0, maxdepth, theta
        self.log = log
        set_prec(prec)
        self.prec = prec
        with open(inst["plus"]) as fh:
            pd = json.load(fh)
        with open(inst["minus"]) as fh:
            md = json.load(fh)
        self.ev = FtEvaluator(pd, md, inst["zc_re"], inst["zc_im"])
        assert self.ev.N == inst["N"]
        self.rect = (inst["x1"], inst["x2"], inst["y1"], inst["y2"])
        x1, x2, y1, y2 = self.rect
        # delta_abs_max: the box's half-diagonal from the center, exactly upper-bounded
        dx = max(abs(x1 - inst["zc_re"]), abs(x2 - inst["zc_re"]))
        dy = max(abs(y1 - inst["zc_im"]), abs(y2 - inst["zc_im"]))
        d2 = dx * dx + dy * dy
        self.dmax = Fraction(math.isqrt(d2.numerator * d2.denominator) + 1, d2.denominator)
        self.x_iv = iv_from_fraction_pair(x1, x2)
        self.y_iv = iv_from_fraction_pair(y1, y2)
        self.stats = {}

    # ---- per-seam mesh
    def _refine_edge(self, edge, a, b, t_iv, depth=0):
        zbox = seg_zbox(edge, a, b, self.rect)
        f, _, _, _ = self.ev.evaluate(zbox, t_iv, want_dt=False)
        self.stats["evals"] += 1
        tag = f.halfplane()
        if tag is not None:
            vrow = value_row_ints(f, self.K)
            if c6_ints(vrow):
                return [Segment(edge, a, b, f, tag, vrow, zbox)]
        if depth >= self.maxdepth:
            raise SystemExit(
                "PRODUCER STOP (%s edge, [%s, %s], depth %d): cannot certify a 0-excluding value "
                "box for f_tau -- a zero of f lies on or near the boundary (or the box widths do "
                "not shrink).  Per FORMAT.md 6.2 / SPEC 4.3 the response is to move the rectangle, "
                "never to weaken the criterion." % (edge, a, b, depth))
        mid = (a + b) / 2
        return (self._refine_edge(edge, a, mid, t_iv, depth + 1)
                + self._refine_edge(edge, mid, b, t_iv, depth + 1))

    def build_mesh(self, t_iv):
        x1, x2, y1, y2 = self.rect
        edges = [("bottom", x1, x2), ("right", y1, y2), ("top", x2, x1), ("left", y2, y1)]
        segments, mesh = [], {}
        for edge, start, end in edges:
            n0 = max(1, int(math.ceil(abs(float(end - start)) / float(self.h0))))
            pieces = [start + (end - start) * Fraction(i, n0) for i in range(n0 + 1)]
            segs = []
            tE = time.time()
            for i in range(n0):
                segs.extend(self._refine_edge(edge, pieces[i], pieces[i + 1], t_iv))
            mesh[edge] = [sg.a for sg in segs] + [segs[-1].b]
            segments.extend(segs)
            self.log("    edge %-6s: %4d segments (%.1fs, %d evals so far)"
                     % (edge, len(segs), time.time() - tE, self.stats["evals"]))
        return segments, mesh

    def argument_rows(self, segments, t_iv):
        cache = {}

        def endpoint_ball(pt):
            if pt not in cache:
                f, _, _, _ = self.ev.evaluate(ball_from_fr(pt[0], pt[1]), t_iv, want_dt=False)
                cache[pt] = f
                self.stats["point_evals"] += 1
            return cache[pt]

        A = self.A
        rows = []
        two_pi = 2 * iv_pi()
        Aiv = iv_from_int(A)
        maxw = 0
        for k, sg in enumerate(segments):
            p_start, p_end = seg_endpoints(sg.edge, sg.a, sg.b, self.rect)
            th = []
            for pt in (p_start, p_end):
                thin = endpoint_ball(pt)
                inter = thin.intersect(sg.box)
                if inter is None:
                    raise SystemExit("PRODUCER STOP (segment %d, %s): thin endpoint enclosure and "
                                     "whole-segment box are DISJOINT -- an enclosure bug (stop-the-line)."
                                     % (k, sg.edge))
                th.append(inter.arg_branch(sg.tag))
            scaled = (th[1] - th[0]) / two_pi * Aiv
            lo, hi = ivmpf_bounds(scaled)
            argLo, argHi = floor_fr(lo), ceil_fr(hi)
            argLo = max(argLo, -(A // 2))
            argHi = min(argHi, A // 2)
            if argLo > argHi:
                raise SystemExit("PRODUCER STOP (segment %d): argument row empty after the D3 clamp." % k)
            maxw = max(maxw, argHi - argLo)
            rows.append((argLo, argHi))
        return rows, maxw

    def dt_bound(self, segments, T_iv):
        """DT >= sup over all segment boxes x T_iv of |d/dt f_t| (upper endpoint, Fraction),
        with the evaluator prepared for T_iv and derivatives."""
        worst = Fraction(0)
        worst_k = -1
        for k, sg in enumerate(segments):
            _, fdt, _, _ = self.ev.evaluate(sg.zbox, T_iv, want_dt=True)
            self.stats["dt_evals"] += 1
            b = ball_abs_hi(fdt)
            if b > worst:
                worst, worst_k = b, k
        return worst, worst_k

    # ---- one prism
    def produce_prism(self, index, tau, t0_final):
        K, A = self.K, self.A
        x1, x2, y1, y2 = self.rect
        tP = time.time()
        self.stats = {"evals": 0, "point_evals": 0, "dt_evals": 0}
        t_iv = iv_from_fr(tau)
        self.log("prism %d: seam tau = %s (%.6f)" % (index, tau, float(tau)))
        # (1) seam rows
        tq = time.time()
        self.ev.prepare(t_iv, self.dmax, want_dt=False)
        self.log("    prepare(seam) %.2fs; orders plus %s" % (time.time() - tq, self.ev.orders[0][1:4]))
        segments, mesh = self.build_mesh(t_iv)
        arows, maxw = self.argument_rows(segments, t_iv)
        S_lo = sum(r[0] for r in arows)
        S_hi = sum(r[1] for r in arows)
        self.log("    winding sum: S_lo=%d S_hi=%d (A=%d, max row width %d)" % (S_lo, S_hi, A, maxw))
        if not 2 * (S_hi - S_lo) < A:
            raise SystemExit("PRODUCER STOP: winding enclosure too wide for C-B8.")
        if not (S_lo <= 0 <= S_hi):
            raise SystemExit("PRODUCER STOP: certified winding of f_tau around dR is NOT 0 (S in [%d, %d]) -- "
                             "the rectangle contains a zero of f_tau; no barrier transcript is emitted." % (S_lo, S_hi))
        # (2) floor
        mins = []
        for sg in segments:
            reLo, reHi, imLo, imHi = sg.vrow
            mre = 0 if reLo <= 0 <= reHi else min(abs(reLo), abs(reHi))
            mim = 0 if imLo <= 0 <= imHi else min(abs(imLo), abs(imHi))
            mins.append(mre * mre + mim * mim)
        Fn = math.isqrt(min(mins))
        Fd = K
        floor_val = Fraction(Fn, Fd)
        maxabs = max(ball_abs_hi(sg.box) for sg in segments)
        self.log("    floor |f_tau| >= %d/K = %.6f on dR (max |f| box <= %.4f); %d segments"
                 % (Fn, float(floor_val), float(maxabs), len(segments)))
        # (3) E at the seam (whole box, t thin)
        E_seam, parts = defect_bound(self.x_iv, self.y_iv, t_iv, self.inst["N"])
        E_int = ceil_fr(K * E_seam)
        self.log("    E(tau) <= %.4e (eAB %.2e, eC0 %.2e, sigma_lo %.4f, F %.3e) -> E = %d"
                 % (float(E_seam), float(parts["eAB_hi"]), float(parts["eC0_hi"]), float(parts["sigma_lo"]),
                    float(parts["F_hi"]), E_int))
        if not 2 * E_seam < floor_val:
            raise SystemExit("PRODUCER STOP: 2 E(tau) >= floor -- no positive prism length is possible.")
        # (4) prism length: seam derivative bound, then interval verification
        tq = time.time()
        self.ev.prepare(t_iv, self.dmax, want_dt=True)
        DT_seam, kw = self.dt_bound(segments, t_iv)
        self.log("    |d/dt f| at the seam <= %.4g (worst segment %d, %.1fs)" % (float(DT_seam), kw, time.time() - tq))
        budget = floor_val - 2 * E_seam
        dt = self.theta * budget / DT_seam if DT_seam > 0 else (t0_final - tau)
        dt = min(dt, t0_final - tau)
        chosen = None
        for attempt in range(8):
            tau_next = tau + nice_floor(dt)
            if tau_next > t0_final:
                tau_next = t0_final
            if tau_next <= tau:
                raise SystemExit("PRODUCER STOP: prism length collapsed to 0.")
            T = iv_from_fraction_pair(tau, tau_next)
            tq = time.time()
            self.ev.prepare(T, self.dmax, want_dt=True)
            DT, kw = self.dt_bound(segments, T)
            E_prism, _ = defect_bound(self.x_iv, self.y_iv, T, self.inst["N"])
            D_val = E_prism + (tau_next - tau) * DT + E_seam
            D_int = ceil_fr(K * D_val)
            gate = (E_int + D_int) * Fd < Fn * K
            self.log("    try tau' = %s (dt %.3e): DT <= %.4g (seg %d), E_prism <= %.3e, D/K = %.4e -> gate %s (%.1fs)"
                     % (tau_next, float(tau_next - tau), float(DT), kw, float(E_prism), float(D_val),
                        "OK" if gate else "FAIL", time.time() - tq))
            if gate:
                chosen = (tau_next, DT, E_prism, D_val, D_int, kw)
                break
            dt = dt / 2
        if chosen is None:
            raise SystemExit("PRODUCER STOP: could not find a prism length satisfying C-B12 after 8 halvings.")
        tau_next, DT, E_prism, D_val, D_int, kw = chosen
        # (5) emit
        doc = {
            "format": "M2a-barrier-transcript", "version": "1.0", "kind": "prism",
            "index": str(index), "seam": rat(tau),
            "scales": {"K": str(K), "A": str(A)},
            "mesh": {e: [rat(v) for v in mesh[e]] for e in ("bottom", "right", "top", "left")},
            "segments": [{"reLo": str(sg.vrow[0]), "reHi": str(sg.vrow[1]), "imLo": str(sg.vrow[2]),
                          "imHi": str(sg.vrow[3]), "argLo": str(ar[0]), "argHi": str(ar[1])}
                         for sg, ar in zip(segments, arows)],
            "modulus_floor": {"Fn": str(Fn), "Fd": str(Fd)},
            "approx_defect": str(E_int),
            "displacement": str(D_int),
            "producer": {
                "implementation": "producer_mp.py + ft_mp.py (mpmath-ball leg, D-R3; M2a item (d))",
                "mpmath_version": mpmath.__version__, "python_version": sys.version.split()[0],
                "iv_prec_bits": self.prec,
                "N0": self.inst["N"],
                "evaluator": "block-Taylor stored moments (ft_mp.py D-F8), frozen-alpha correction, remainders added; "
                             "gamma by exp(log M0 difference) (D-F2)",
                "taylor_orders_plus": [list(o) for o in self.ev.orders[0]],
                "taylor_orders_minus": [list(o) for o in self.ev.orders[1]],
                "seam_time_float": float(tau), "next_seam": rat(tau_next), "delta_t": rat(tau_next - tau),
                "E_bound_seam": str(E_seam), "E_bound_seam_float": float(E_seam),
                "E_parts": {k: float(v) for k, v in parts.items()},
                "E_prism_bound": str(E_prism), "E_prism_bound_float": float(E_prism),
                "DT_sup_dt_f": str(DT), "DT_float": float(DT), "DT_worst_segment": kw,
                "DT_seam_float": float(DT_seam),
                "D_value": str(D_val), "D_value_float": float(D_val),
                "floor_float": float(floor_val), "max_abs_f_on_boundary_float": float(maxabs),
                "winding_sum": [S_lo, S_hi], "max_arg_row_width": maxw,
                "mesh_policy": "uniform h0=%s then bisection to depth<=%d until ball half-plane + integer C-B6 at K" % (self.h0, self.maxdepth),
                "argument_policy": "derivative-free half-plane branch, thin endpoint (cached) intersect segment box, "
                                   "outward-rounded, D3-clamped, A even",
                "prism_length_policy": "theta=%s of (floor - 2E)/DT_seam, then interval-t verification, halving on gate failure" % self.theta,
                "segment_evals": self.stats["evals"], "endpoint_evals": self.stats["point_evals"],
                "dt_evals": self.stats["dt_evals"],
                "started_utc": datetime.datetime.fromtimestamp(tP, datetime.timezone.utc).isoformat(),
                "wall_seconds": round(time.time() - tP, 1),
            },
            "comment": ("UNTRUSTED producer output (mpmath-ball leg). Rows enclose the seam approximant f_tau "
                        "(P15 (14) read with the overline on s_* in the second sum, ft_mp.py D-F1); E from "
                        "Prop. 6.6(iv)-(vi) uniformized on the box (D-F4); D from the interval-t bound on d/dt f_t "
                        "plus E at both ends (D-F7)."
                        + (" SEAM AT t = 0: Theorem 1.3 is applied at t = 0 by the limit argument ft_mp.py D-F9 "
                           "(SPEC P-7): H_t -> H_0 by dominated convergence, B_t -> B_0, f_t -> f_0 and the majorant "
                           "is continuous in t; this limit argument is part of H2-B's discharge at this seam."
                           if tau == 0 else "")),
        }
        path = os.path.join(self.out, "prism-%04d.json" % index)
        tmp = path + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(doc, fh, indent=0)
        os.replace(tmp, path)
        self.log("    wrote %s: %d rows, E=%d, D=%d, floor %d/K, next seam %s (%.1fs)"
                 % (os.path.basename(path), len(segments), E_int, D_int, Fn, tau_next, time.time() - tP))
        return {"index": index, "file": os.path.basename(path), "seam": tau, "next": tau_next,
                "rows": len(segments), "floor": float(floor_val), "E": float(E_seam), "D": float(D_val),
                "DT": float(DT), "delta_t": float(tau_next - tau), "seconds": round(time.time() - tP, 1)}

    def write_manifest(self, prisms, t0_final):
        last_next = prisms[-1]["next"]
        complete = (last_next == t0_final)
        x1, x2, y1, y2 = self.rect
        doc = {
            "format": "M2a-barrier-transcript", "version": "1.0", "kind": "manifest", "lane": "barrier",
            "trust_label": TRUST_LABEL,
            "rect": {"x1": rat(x1), "x2": rat(x2), "y1": rat(y1), "y2": rat(y2)},
            "t0": rat(last_next),
            "prisms": [{"index": str(p["index"]), "file": p["file"], "seam": rat(p["seam"])} for p in prisms],
            "producer": {
                "implementation": "producer_mp.py + ft_mp.py (mpmath-ball leg)",
                "instance": "P15 Table 1 row 2: X = %s, t0 = %s, y0 = %s, N0 = %d" % (x1, t0_final, y1, self.inst["N"]),
                "status": "COMPLETE: chain covers [0, t0]" if complete else
                          "PARTIAL: chain covers [0, %s] only (%.6f of t0 = %s); t0 above is the LAST CERTIFIED TIME, "
                          "not the instance's t0 -- a valid barrier certificate for that shorter time range" % (
                              last_next, float(last_next / t0_final), t0_final),
                "prism_summary": [dict(p, seam=str(p["seam"]), next=str(p["next"])) for p in prisms],
                "written_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            },
            "comment": ("UNTRUSTED producer output (mpmath-ball leg). " +
                        ("Complete barrier chain for the instance." if complete else
                         "PARTIAL barrier chain: certifies (modulo H2-B, H3) nonvanishing of H_t on R only for 0 <= t <= %s." % last_next)),
        }
        path = os.path.join(self.out, "manifest.json")
        tmp = path + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(doc, fh, indent=1)
        os.replace(tmp, path)
        return complete


def run(args):
    inst = INSTANCES[args.instance]
    os.makedirs(args.out, exist_ok=True)
    logpath = os.path.join(args.out, "producer.log")

    def log(s):
        line = "[%s] %s" % (datetime.datetime.now().strftime("%H:%M:%S"), s)
        print(line, flush=True)
        with open(logpath, "a") as fh:
            fh.write(line + "\n")

    K, A = 10 ** args.K, 10 ** args.A
    if A % 2 != 0 or A < 2:
        raise SystemExit("A must be even and >= 2")
    log("producer_mp (M2a): instance=%s K=1e%d A=1e%d h0=%s maxdepth=%d theta=%s prec=%d"
        % (args.instance, args.K, args.A, args.h0, args.maxdepth, args.theta, args.prec))
    set_prec(args.prec)
    # P-3: N constant on the closed box x [0, t0], and N^2 <= x1/(4 pi)
    N0 = check_N_constant(inst["x1"], inst["x2"], Fraction(0), inst["t0"])
    assert N0 == inst["N"], (N0, inst["N"])
    log("P-3: N = %d certified constant on [x1, x2] x [0, t0]; N^2 <= x1/(4 pi) certified" % N0)
    P = Producer(inst, args.out, K, A, Fraction(args.h0), args.maxdepth, Fraction(args.theta), args.prec, log)
    prog_path = os.path.join(args.out, "progress.json")
    prisms = []
    tau = Fraction(0)
    if args.resume and os.path.exists(prog_path):
        with open(prog_path) as fh:
            prog = json.load(fh)
        for p in prog["prisms"]:
            p["seam"] = Fraction(p["seam"])
            p["next"] = Fraction(p["next"])
        prisms = prog["prisms"]
        if prisms:
            tau = prisms[-1]["next"]
        log("resumed: %d prisms done, continuing from tau = %s" % (len(prisms), tau))
    t_start = time.time()
    while tau < inst["t0"]:
        if args.max_prisms and len(prisms) >= args.max_prisms:
            log("max-prisms reached; stopping (PARTIAL)")
            break
        if args.max_seconds and time.time() - t_start > args.max_seconds:
            log("time budget reached; stopping (PARTIAL)")
            break
        rec = P.produce_prism(len(prisms), tau, inst["t0"])
        prisms.append(rec)
        tau = rec["next"]
        complete = P.write_manifest(prisms, inst["t0"])
        with open(prog_path + ".tmp", "w") as fh:
            json.dump({"prisms": [dict(p, seam=str(p["seam"]), next=str(p["next"])) for p in prisms],
                       "complete": complete, "elapsed": round(time.time() - t_start, 1)}, fh, indent=1)
        os.replace(prog_path + ".tmp", prog_path)
        log("manifest: %d prisms, certified up to tau = %s (%.5f of t0)%s"
            % (len(prisms), tau, float(tau / inst["t0"]), "  COMPLETE" if complete else ""))
    log("done: %d prisms, %.0fs total, chain reaches %s (t0 = %s)" % (len(prisms), time.time() - t_start, tau, inst["t0"]))
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--instance", choices=sorted(INSTANCES), required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--K", type=int, default=24, help="K = 10^this")
    ap.add_argument("--A", type=int, default=12, help="A = 10^this (even)")
    ap.add_argument("--h0", default="1/50")
    ap.add_argument("--maxdepth", type=int, default=12)
    ap.add_argument("--theta", default="1/2")
    ap.add_argument("--prec", type=int, default=PREC_DEFAULT)
    ap.add_argument("--max-prisms", type=int, default=0)
    ap.add_argument("--max-seconds", type=float, default=0)
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args(argv)
    return run(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
