#!/usr/bin/env python3
"""producer_arb.py -- the Arb/FLINT leg: UNTRUSTED W1 transcript producer.

Emits W1 rectangle transcripts (FORMAT.md v1.0 + w1-schema.json, this directory)
from Arb ball arithmetic via python-flint (acb.zeta: Riemann and Hurwitz zeta).

ROLE AND TRUST STATUS.  This is one of the two independent producers required by
the two-producer rule (D1 direction file, D-R3; m2a-m2b-design.md section 4).  It
is UNTRUSTED BY DESIGN: its output enters the trusted statement only through the
displayed hypothesis H-ENCL (FORMAT.md section 8.1).  An accepted transcript is
"kernel-checked modulo the displayed hypotheses H-ENCL and H-AP" -- never "fully
machine-checked".

INDEPENDENCE DISCIPLINE (binding).  This file shares the FORMAT contract with the
mpmath leg and NOTHING else: no evaluation code, no helper imports from any other
producer, no numerical constants computed elsewhere.  Everything numerical here
comes from python-flint's Arb balls plus exact Python integer/Fraction
arithmetic.  (The reference checker is checker-side, shared by both legs for
prevalidation only; it produces no numbers that enter a transcript.)

--------------------------------------------------------------------------------
DERIVATIONS (standing order 5: nothing load-bearing from memory; each step the
producer relies on is derived here or cited to an exact on-disk location).

D-P0 (Arb's ball contract -- the one imported fact).  Every Arb operation on
balls returns a ball containing f(x) for every x in the input ball(s) (inclusion
isotonicity).  This is the library's defining contract; it is spot-verified live
in arb_capability_check.py (checks F1/F2: a wide input ball's zeta box contains
independently computed interior values; a point ball agrees with mpmath at
higher precision) and cross-validated again per transcript by
validate_arb_transcripts.py.  Producer correctness is CONDITIONAL on D-P0 --
which is exactly the untrusted-producer status the format assigns.

D-P1 (exact ball -> rational interval; no directed rounding trusted).  For an
arb x, mid() and rad() are exact dyadics m*2^e (verified: is_exact() true and
man_exp() exact, capability checks D2-D5).  The interval
I(x) = [mid - rad, mid + rad], computed in exact Fraction arithmetic, contains
every point of the ball by definition of a ball.  All integer conversion below
uses I(x) only; lower()/upper() (directed-rounding calls, direction verified in
capability checks E1-E4) serve as a redundant cross-check assert.

D-P2 (outward integer bounds at scale S).  For rational bounds lo <= x <= hi and
integer scale S >= 1: floor(S*lo) <= S*x <= ceil(S*hi), with floor/ceil computed
exactly on Fractions (floor(n/d) = n//d for d > 0, Python floor division; ceil =
-((-n)//d)).  Hence (floor(S*lo), ceil(S*hi)) is a valid integer enclosure row.
Outward rounding can only WIDEN the enclosure, so it preserves H-ENCL truth.

D-P3 (exact rational -> ball, containment re-verified).  arb(fmpq(n, d)) returns
a ball; we do not trust the conversion blindly: rat_ball() re-verifies
n/d in I(ball) by exact cross-multiplied arithmetic and raises otherwise
(capability check D6 verified the containment on samples; this re-checks every
conversion at run time).

D-P4 (segment hull).  For rationals a, b, the union u = rat_ball(a).union(
rat_ball(b)) is a 1-D ball (interval) containing both endpoint balls; an
interval containing a and b contains all of [min(a,b), max(a,b)].  Re-verified
at run time: a, b in I(u).  An acb built from hull/fixed-coordinate balls
therefore contains every point s of the closed segment, so by D-P0 the value
ball of f over it yields a box valid for ALL s on the segment -- exactly the
H-ENCL(a) quantifier.

D-P5 (the argument row from same-rotation endpoint atan2 -- the FORMAT.md
section 10 recipe, derived here in the form actually implemented).  Fix segment
k with integer value row certifying C6.  By FORMAT.md derivation D1 the box, and
hence f(gamma_k([0,1])), lies in an open coordinate half-plane
H = {z : Re(e^{-i phi} z) > 0}, phi in {0, pi/2, pi, 3pi/2} read off the box
sign.  On H the function theta_phi(z) := phi + atan2(Im(e^{-i phi} z),
Re(e^{-i phi} z)) is a continuous branch of arg z (atan2 is continuous on the
open right half-plane, values in (-pi/2, pi/2)).  By FORMAT.md derivation D2
there is a continuous branch theta(t) of arg f(gamma_k(t)) with
Delta_k = theta(1) - theta(0).  The difference theta(t) - theta_phi(f(gamma_k(t)))
is continuous on connected [0, 1] with values in 2*pi*Z, hence constant; so
  Delta_k = theta_phi(f(q)) - theta_phi(f(p))
          = atan2(Im(e^{-i phi} f(q)), Re(e^{-i phi} f(q)))
          - atan2(Im(e^{-i phi} f(p)), Re(e^{-i phi} f(p)))
(the phi terms cancel -- SAME rotation at both endpoints; using different
rotations per endpoint would be unsound).  The rotations are exact component
swaps/negations on balls (no rounding):
  phi = 0    (reLo > 0):  rot(z) = ( re,  im)
  phi = pi/2 (imLo > 0):  rot(z) = ( im, -re)     # e^{-i pi/2} z = -i z
  phi = pi   (reHi < 0):  rot(z) = (-re, -im)
  phi = 3pi/2(imHi < 0):  rot(z) = (-im,  re)     # e^{-i 3pi/2} z = i z
Enclosure: evaluate f at the two endpoint POINTS as balls, require the rotated
balls certified Re > 0 (escalating precision until certain -- termination:
the true rotated Re is >= (box sign bound)/K > 0, so a shrinking ball around it
is eventually certified), take theta = atan2(rot_im, rot_re) balls, then
  Delta_k in I(theta_q) - I(theta_p)   (exact interval subtraction),
  turns   = Delta_k / (2 pi) in exact-rational division of the Delta interval
            by I(2*arb.pi()) (division by an interval strictly > 0; outward:
            lower = Delta_lo / twopi_hi or / twopi_lo by sign, see code),
and the integer row is the D-P2 outward rounding at scale A, then clamped to
[-A/2, A/2] (sound: FORMAT.md derivation D3 gives |Delta_k| < pi, so the true
scaled value lies in (-A/2, A/2); intersecting two enclosures of the same true
value is an enclosure).  A is chosen EVEN so A/2 is an integer.

D-P6 (winding number and mode).  S_lo = sum argLo_k, S_hi = sum argHi_k in
exact int arithmetic.  The produced m is the unique integer with
S_lo <= A*m <= S_hi when 2*(S_hi - S_lo) < A (FORMAT.md D4); the producer
computes it as the only candidate in [ceil(S_lo/A), floor(S_hi/A)] and errors
if that range is empty or non-singleton, or if m contradicts the requested
mode.  The producer never writes a transcript whose own arithmetic it has not
already seen pass the reference checker.

D-P7 (modulus floor).  With Fd = K and Fn = isqrt(min_k(mre_k^2 + mim_k^2))
(integer square root, rounded down), C11 holds:
(mre_k^2 + mim_k^2)*Fd^2 = (mre_k^2 + mim_k^2)*K^2 >= Fn^2*K^2 since
Fn^2 <= min <= mre_k^2 + mim_k^2.  The claimed floor is |f| >= Fn/K on dR
(FORMAT.md derivation D6).  C6 guarantees min >= 1, so Fn >= 1.

D-P8 (f_DH).  Definition quoted verbatim from results/ccm-dh-test/dh.py lines
5-8 (via FORMAT.md section 9.2):
    f_DH(s) = 5^{-s} [ zeta(s,1/5) + kap*zeta(s,2/5)
                       - kap*zeta(s,3/5) - zeta(s,4/5) ]
    kap = (sqrt(10-2*sqrt5) - 2)/(sqrt5 - 1)
Implemented entirely in Arb balls: sqrt5 = arb(5).sqrt(), Hurwitz zeta via
acb.zeta(a) with a = rat_ball(j/5), 5^{-s} via acb power.  Every constant is a
ball around the exact value (D-P0/D-P3), so the result is an enclosure of the
exact f_DH.  The residual at rho_DH is ball-certified < 1e-12 in
arb_capability_check.py (check H1: |f|^2 <= 2.8e-31).

--------------------------------------------------------------------------------
USAGE

  python3 producer_arb.py zeta-exclusion  [--out FILE]   # preset acceptance run
  python3 producer_arb.py dh-refutation   [--out FILE]   # preset live-fire run
  python3 producer_arb.py custom --function {zeta,f_DH} --mode {refutation,exclusion}
        --sigma1 N/D --sigma2 N/D --T1 N/D --T2 N/D [--out FILE]
        [--K INT] [--A EVEN_INT] [--prec BITS] [--max-depth N]

Defaults: K = 10^30, A = 10^6, prec = 300 bits, max subdivision depth 40.
The producer prevalidates its own output with reference_checker.py when
available and refuses to write a transcript that fails.
"""

import argparse
import datetime
import json
import math
import os
import subprocess
import sys
from fractions import Fraction

import flint
from flint import acb, arb, ctx, fmpq

HERE = os.path.dirname(os.path.abspath(__file__))

TRUST_LABELS = {
    "zeta": "kernel-checked modulo displayed hypotheses H-ENCL and H-AP (producers untrusted)",
    "f_DH": "checker-level only (D-R8): format-checked modulo H-ENCL for f_DH; no Lean-backed conclusion",
}

MAX_SEGMENTS = 20000
PREC_ESCALATION_CAP = 6000  # bits


class ProducerError(Exception):
    pass


# ------------------------------------------------------------------ exact ball -> rational


def _dyadic(man_exp_pair):
    m, e = int(man_exp_pair[0]), int(man_exp_pair[1])
    if e >= 0:
        return Fraction(m * (1 << e))
    return Fraction(m, 1 << (-e))


def ball_interval(x):
    """arb ball -> exact rational interval [mid - rad, mid + rad] (D-P1)."""
    m, r = x.mid(), x.rad()
    if not (m.is_exact() and r.is_exact()):
        raise ProducerError("mid/rad not exact -- non-finite ball?")
    mv, rv = _dyadic(m.man_exp()), _dyadic(r.man_exp())
    if rv < 0:
        raise ProducerError("negative radius")
    return (mv - rv, mv + rv)


def floor_frac(q):
    return q.numerator // q.denominator


def ceil_frac(q):
    return -((-q.numerator) // q.denominator)


def out_int_bounds(x, scale):
    """Integer (lo, hi) with lo <= scale*x_true <= hi for every x_true in the ball
    (D-P2), cross-checked against the library's directed lower()/upper()."""
    lo, hi = ball_interval(x)
    ilo, ihi = floor_frac(lo * scale), ceil_frac(hi * scale)
    # redundant directed-rounding cross-check (capability checks E1-E4):
    # lower() rounds mid - rad toward -inf, upper() rounds mid + rad toward
    # +inf, so they must bracket the exact interval
    dlo, dhi = _dyadic(x.lower().man_exp()), _dyadic(x.upper().man_exp())
    if not (dlo <= lo and hi <= dhi):
        raise ProducerError("lower()/upper() inconsistent with mid/rad interval")
    return ilo, ihi


def rat_ball(q):
    """Ball containing the exact rational q, containment re-verified (D-P3)."""
    b = arb(fmpq(q.numerator, q.denominator))
    lo, hi = ball_interval(b)
    if not (lo <= q <= hi):
        raise ProducerError(f"rat_ball containment failed for {q}")
    return b


def hull_ball(a, b):
    """Ball containing the whole rational interval [min(a,b), max(a,b)] (D-P4)."""
    u = rat_ball(a).union(rat_ball(b))
    lo, hi = ball_interval(u)
    if not (lo <= min(a, b) and max(a, b) <= hi):
        raise ProducerError("hull containment failed")
    return u


# ------------------------------------------------------------------ target functions

_KAPPA_CACHE = {}


def _kappa():
    """kap = (sqrt(10-2*sqrt5) - 2)/(sqrt5 - 1) as an arb ball (D-P8)."""
    key = ctx.prec
    if key not in _KAPPA_CACHE:
        sqrt5 = arb(5).sqrt()
        _KAPPA_CACHE[key] = ((arb(10) - 2 * sqrt5).sqrt() - 2) / (sqrt5 - 1)
    return _KAPPA_CACHE[key]


def eval_zeta(s):
    return s.zeta()


def eval_fdh(s):
    kap = acb(_kappa())
    total = (s.zeta(acb(rat_ball(Fraction(1, 5))))
             + kap * s.zeta(acb(rat_ball(Fraction(2, 5))))
             - kap * s.zeta(acb(rat_ball(Fraction(3, 5))))
             - s.zeta(acb(rat_ball(Fraction(4, 5)))))
    return acb(5) ** (-s) * total


EVALUATORS = {"zeta": eval_zeta, "f_DH": eval_fdh}


# ------------------------------------------------------------------ geometry


def segment_ball(seg):
    """acb ball containing every point of the closed segment (D-P4).

    seg = ('h', re_a, re_b, im_c)  horizontal: Re varies a->b, Im = c fixed
        | ('v', im_a, im_b, re_c)  vertical:   Im varies a->b, Re = c fixed
    """
    kind, a, b, c = seg
    if kind == "h":
        return acb(hull_ball(a, b), rat_ball(c))
    return acb(rat_ball(c), hull_ball(a, b))


def seg_endpoints(seg):
    kind, a, b, c = seg
    if kind == "h":
        return ((a, c), (b, c))
    return ((c, a), (c, b))


def int_box(fball, K):
    reLo, reHi = out_int_bounds(fball.real, K)
    imLo, imHi = out_int_bounds(fball.imag, K)
    return (reLo, reHi, imLo, imHi)


def c6_holds(box):
    reLo, reHi, imLo, imHi = box
    return reLo > 0 or reHi < 0 or imLo > 0 or imHi < 0


def refine_edge(f, seg, K, max_depth, depth=0):
    """Adaptively bisect one edge interval until every piece's INTEGER box
    passes C6.  Returns list of (sub-seg, box) in traversal order."""
    fb = f(segment_ball(seg))
    box = int_box(fb, K)
    if c6_holds(box):
        return [(seg, box)]
    if depth >= max_depth:
        raise ProducerError(
            f"C6 unreachable at depth {depth} on {seg}: a zero of f lies on or "
            "near this boundary piece -- MOVE the rectangle (FORMAT.md 6.2).")
    kind, a, b, c = seg
    mid = (a + b) / 2  # exact rational bisection
    left = refine_edge(f, (kind, a, mid, c), K, max_depth, depth + 1)
    right = refine_edge(f, (kind, mid, b, c), K, max_depth, depth + 1)
    if len(left) + len(right) > MAX_SEGMENTS:
        raise ProducerError("segment budget exceeded")
    return left + right


# ------------------------------------------------------------------ argument rows

ROTATIONS = {  # box sign -> exact component rotation (D-P5)
    0: lambda z: (z.real, z.imag),            # reLo > 0, phi = 0
    1: lambda z: (z.imag, -z.real),           # imLo > 0, phi = pi/2
    2: lambda z: (-z.real, -z.imag),          # reHi < 0, phi = pi
    3: lambda z: (-z.imag, z.real),           # imHi < 0, phi = 3pi/2
}


def rotation_index(box):
    reLo, reHi, imLo, imHi = box
    if reLo > 0:
        return 0
    if imLo > 0:
        return 1
    if reHi < 0:
        return 2
    if imHi < 0:
        return 3
    raise ProducerError("rotation_index called on a C6-failing box")


class EndpointCache:
    """f evaluated at breakpoints, at escalating precision until the rotated
    ball is certified in the open right half-plane (D-P5 termination note)."""

    def __init__(self, f, base_prec):
        self.f = f
        self.base_prec = base_prec
        self.cache = {}

    def theta(self, point, rot_idx):
        """Exact rational interval enclosing atan2 of the rotated f(point)."""
        prec = self.base_prec
        while True:
            ctx.prec = prec
            key = (point, prec)
            if key not in self.cache:
                s = acb(rat_ball(point[0]), rat_ball(point[1]))
                self.cache[key] = self.f(s)
            fb = self.cache[key]
            rot_re, rot_im = ROTATIONS[rot_idx](fb)
            if bool(rot_re > arb(0)):
                th = arb.atan2(rot_im, rot_re)
                return ball_interval(th)
            prec *= 2
            if prec > PREC_ESCALATION_CAP:
                raise ProducerError(
                    f"endpoint {point}: rotated ball not certified positive up "
                    f"to {PREC_ESCALATION_CAP} bits (rotation {rot_idx})")


def two_pi_interval():
    lo, hi = ball_interval(2 * arb.pi())
    if lo <= 0:
        raise ProducerError("2*pi interval not positive?!")
    return lo, hi


def div_interval_by_pos(num_lo, num_hi, den_lo, den_hi):
    """Outward [num_lo, num_hi] / [den_lo, den_hi] with den_lo > 0 (D-P5).

    For x in [nlo, nhi], d in [dlo, dhi] (0 < dlo <= dhi):
      x/d >= nlo/dhi if nlo >= 0 else nlo/dlo   (dividing a negative lower
        bound by the SMALLER denominator makes it more negative -> outward);
      x/d <= nhi/dlo if nhi >= 0 else nhi/dhi.
    Both cases verified by sign-splitting the monotonicity of x/d in d."""
    lo = num_lo / den_hi if num_lo >= 0 else num_lo / den_lo
    hi = num_hi / den_lo if num_hi >= 0 else num_hi / den_hi
    return lo, hi


def argument_row(cache, seg, box, A):
    """(argLo, argHi) integer row for one segment (D-P5)."""
    rot_idx = rotation_index(box)
    p, q = seg_endpoints(seg)
    tp_lo, tp_hi = cache.theta(p, rot_idx)
    tq_lo, tq_hi = cache.theta(q, rot_idx)
    d_lo, d_hi = tq_lo - tp_hi, tq_hi - tp_lo  # exact interval subtraction
    tp2_lo, tp2_hi = two_pi_interval()
    t_lo, t_hi = div_interval_by_pos(d_lo, d_hi, tp2_lo, tp2_hi)
    argLo, argHi = floor_frac(t_lo * A), ceil_frac(t_hi * A)  # D-P2 outward
    # clamp (FORMAT.md 6.1 last paragraph; sound by D3 + intersection of
    # enclosures of the same true value); A is even by construction
    argLo = max(argLo, -(A // 2))
    argHi = min(argHi, A // 2)
    if argLo > argHi:
        raise ProducerError("clamp produced empty row -- producer bug")
    return argLo, argHi


# ------------------------------------------------------------------ transcript assembly


def frac_json(q):
    return {"n": str(q.numerator), "d": str(q.denominator)}


def produce(function, mode, sigma1, sigma2, T1, T2, K, A, prec, max_depth):
    if A % 2 != 0:
        raise ProducerError("A must be even (integer clamp bound A/2)")
    if not (Fraction(1, 2) < sigma1 <= sigma2 < 1 and T1 < T2):
        raise ProducerError("rectangle violates C2 preconditions")
    f = EVALUATORS[function]
    ctx.prec = prec

    # edges in traversal order (FORMAT.md section 4)
    edges = {
        "bottom": ("h", sigma1, sigma2, T1),
        "right": ("v", T1, T2, sigma2),
        "top": ("h", sigma2, sigma1, T2),
        "left": ("v", T2, T1, sigma1),
    }
    mesh = {}
    rows = []
    cache = EndpointCache(f, prec)
    total_segs = 0
    for name in ("bottom", "right", "top", "left"):
        ctx.prec = prec
        pieces = refine_edge(f, edges[name], K, max_depth)
        total_segs += len(pieces)
        breakpoints = [pieces[0][0][1]] + [sg[2] for sg, _ in pieces]
        mesh[name] = breakpoints
        for sg, box in pieces:
            argLo, argHi = argument_row(cache, sg, box, A)
            rows.append(box + (argLo, argHi))

    S_lo = sum(r[4] for r in rows)
    S_hi = sum(r[5] for r in rows)
    if 2 * (S_hi - S_lo) >= A:
        raise ProducerError(
            f"C8 fails: winding enclosure width {S_hi - S_lo} >= A/2 = {A // 2}; "
            "raise --prec or refine")
    m_lo, m_hi = ceil_frac(Fraction(S_lo, A)), floor_frac(Fraction(S_hi, A))
    if m_lo != m_hi:
        raise ProducerError(f"no unique winding integer in [{S_lo}, {S_hi}]/A")
    m = m_lo
    if mode == "refutation" and m < 1:
        raise ProducerError(f"mode refutation but produced winding m = {m}")
    if mode == "exclusion" and m != 0:
        raise ProducerError(f"mode exclusion but produced winding m = {m}")

    # modulus floor (D-P7)
    def mcoord(lo, hi):
        return 0 if lo <= 0 <= hi else min(abs(lo), abs(hi))

    m2_min = min(mcoord(r[0], r[1]) ** 2 + mcoord(r[2], r[3]) ** 2 for r in rows)
    Fn = math.isqrt(m2_min)

    transcript = {
        "format": "W1-rect-transcript",
        "version": "1.0",
        "mode": mode,
        "function": function,
        "trust_label": TRUST_LABELS[function],
        "rect": {"sigma1": frac_json(sigma1), "sigma2": frac_json(sigma2),
                 "T1": frac_json(T1), "T2": frac_json(T2)},
        "scales": {"K": str(K), "A": str(A)},
        "claimed_m": str(m),
        "mesh": {name: [frac_json(q) for q in mesh[name]]
                 for name in ("bottom", "right", "top", "left")},
        "segments": [
            {"reLo": str(r[0]), "reHi": str(r[1]), "imLo": str(r[2]),
             "imHi": str(r[3]), "argLo": str(r[4]), "argHi": str(r[5])}
            for r in rows
        ],
        "modulus_floor": {"Fn": str(Fn), "Fd": str(K)},
        "producer": {
            "leg": "arb",
            "implementation": "producer_arb.py (results/d1-m1/), Arb via python-flint",
            "library": f"python-flint {flint.__version__} (FLINT/Arb; acb.zeta Riemann+Hurwitz)",
            "python": sys.version.split()[0],
            "prec_bits_base": prec,
            "prec_escalation_cap_bits": PREC_ESCALATION_CAP,
            "scheme": ("value rows: segment-hull ball evaluation (D-P4/D-P0); "
                       "argument rows: same-rotation endpoint atan2 (D-P5); "
                       "integer conversion: exact mid/rad outward rounding (D-P1/D-P2)"),
            "subdivision": f"adaptive bisection until integer C6, depth cap {max_depth}",
            "segments": total_segs,
            "winding_sum": {"S_lo": str(S_lo), "S_hi": str(S_hi)},
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc)
            .strftime("%Y-%m-%dT%H:%M:%SZ"),
            "independence": ("shares FORMAT.md/w1-schema.json with the mpmath leg; "
                             "shares NO evaluation code (D-R3 two-producer rule)"),
            "trust": "UNTRUSTED producer; output enters trusted statement only via H-ENCL",
        },
    }
    return transcript


def prevalidate(path):
    """Run the shared reference checker (checker-side, prevalidation only)."""
    checker = os.path.join(HERE, "reference_checker.py")
    if not os.path.exists(checker):
        print("WARNING: reference_checker.py not found; skipping prevalidation")
        return True
    r = subprocess.run([sys.executable, checker, path],
                       capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    sys.stderr.write(r.stderr)
    return r.returncode == 0


PRESETS = {
    # Null test (M3 prototype): a box strictly right of the critical line at
    # heights [10, 11] -- the same rectangle as FORMAT.md's ARTIFICIAL section 11
    # example, now with REAL certified enclosures.  Expected m = 0.
    "zeta-exclusion": dict(function="zeta", mode="exclusion",
                           sigma1=Fraction(3, 5), sigma2=Fraction(7, 10),
                           T1=Fraction(10), T2=Fraction(11)),
    # Live fire (D-R8 checker-level true-positive): a small box around the
    # certified off-line zero rho_DH = 0.808517182456637 + 85.699348485377592i
    # (D1 direction file line 104).  Expected m = 1.
    "dh-refutation": dict(function="f_DH", mode="refutation",
                          sigma1=Fraction(4, 5), sigma2=Fraction(41, 50),
                          T1=Fraction(8569, 100), T2=Fraction(8571, 100)),
}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--out", default=None)
    common.add_argument("--K", type=int, default=10 ** 30)
    common.add_argument("--A", type=int, default=10 ** 6)
    common.add_argument("--prec", type=int, default=300)
    common.add_argument("--max-depth", type=int, default=40)
    for name in PRESETS:
        sub.add_parser(name, parents=[common])
    cu = sub.add_parser("custom", parents=[common])
    cu.add_argument("--function", choices=("zeta", "f_DH"), required=True)
    cu.add_argument("--mode", choices=("refutation", "exclusion"), required=True)
    for fld in ("sigma1", "sigma2", "T1", "T2"):
        cu.add_argument("--" + fld, type=Fraction, required=True)
    args = ap.parse_args()

    if args.cmd in PRESETS:
        spec = dict(PRESETS[args.cmd])
        default_out = {"zeta-exclusion": "w1-arb-zeta-exclusion.json",
                       "dh-refutation": "w1-arb-dh-refutation.json"}[args.cmd]
    else:
        spec = dict(function=args.function, mode=args.mode, sigma1=args.sigma1,
                    sigma2=args.sigma2, T1=args.T1, T2=args.T2)
        default_out = "w1-arb-custom.json"
    out = args.out or os.path.join(HERE, default_out)

    t = produce(K=args.K, A=args.A, prec=args.prec, max_depth=args.max_depth, **spec)
    tmp = out + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(t, fh, indent=1)
        fh.write("\n")
    if not prevalidate(tmp):
        os.remove(tmp)
        raise SystemExit("prevalidation FAILED; transcript not written")
    os.replace(tmp, out)
    print(f"WROTE {out}: mode={t['mode']} function={t['function']} "
          f"m={t['claimed_m']} segments={len(t['segments'])} "
          f"S=[{t['producer']['winding_sum']['S_lo']}, "
          f"{t['producer']['winding_sum']['S_hi']}]/{t['scales']['A']} "
          f"floor={t['modulus_floor']['Fn']}/{t['modulus_floor']['Fd']}")


if __name__ == "__main__":
    main()
