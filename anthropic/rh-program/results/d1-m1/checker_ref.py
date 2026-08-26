"""checker_ref.py -- independent REFERENCE CHECKER for W1 rectangle transcripts.

D1 M1 v1, mpmath-ball leg deliverable 4.  This file is an EXECUTABLE SPEC of the
checker normatively defined in results/d1-m1/FORMAT.md sec. 7 (checks C1-C11,
contract v1.0): the Lean kernel checker (`checkW1`, FORMAT.md sec. 7.1) mirrors
these checks; this Python rendering exists for producer prevalidation and for
two-implementation cross-validation.  It is UNTRUSTED -- acceptance here is
producer-side evidence only; the trusted verdict is the Lean one, and even that
is "kernel-checked modulo the displayed hypotheses H-ENCL and H-AP", never
"fully machine-checked".

INDEPENDENCE (by construction):
 * shares NO code with the producer leg (imports: json, re, sys, fractions
   only; no ball/zeta_encl/hurwitz_encl/producer_mp imports);
 * written independently of reference_checker.py (the format author's
   implementation in this directory): that one compares rationals by integer
   cross-multiplication; this one uses exact Fraction comparisons, which agree
   with cross-multiplication by FORMAT.md derivation D7 (for d1, d2 >= 1:
   n1/d1 < n2/d2 iff n1*d2 < n2*d1 -- Fraction implements the left side
   exactly).  Agreement of the two on the same files is a two-implementation
   check of the spec reading, exercised in checker-ref-run.txt.

WHAT IS CHECKED (verbatim from FORMAT.md sec. 7; row checks in pure int):
  SHAPE  w1-schema.json semantics, hand-implemented (field lists, const/enum
         values, per-function verbatim trust label, integer-string patterns,
         list minimums, the exclusion => claimed_m = "0" schema tie).
  C1     K >= 1, A >= 1; every rational's d >= 1.
  C2     1/2 < sigma1 <= sigma2 < 1;  T1 < T2.
  C3     mesh walk: bottom[0] = sigma1, bottom[last] = sigma2, strictly
         increasing; right[0] = T1, right[last] = T2, strictly increasing;
         top[0] = sigma2, top[last] = sigma1, strictly decreasing;
         left[0] = T2, left[last] = T1, strictly decreasing.
  C4     |segments| = (|bottom|-1) + (|right|-1) + (|top|-1) + (|left|-1).
  C5     reLo_k <= reHi_k and imLo_k <= imHi_k, every k.
  C6     reLo_k > 0 or reHi_k < 0 or imLo_k > 0 or imHi_k < 0, every k.
  C7     argLo_k <= argHi_k and -A <= 2*argLo_k and 2*argHi_k <= A, every k.
  C8     2*(S_hi - S_lo) < A,  S_lo = sum argLo_k, S_hi = sum argHi_k.
  C9     S_lo <= A*m <= S_hi.
  C10    mode refutation => m >= 1;  mode exclusion => m = 0.
  C11    (only if modulus_floor present)
         (mre_k^2 + mim_k^2) * Fd^2 >= Fn^2 * K^2, every k, with
         mre_k = 0 if reLo_k <= 0 <= reHi_k else min(|reLo_k|, |reHi_k|),
         mim_k likewise.

USAGE
  python3 checker_ref.py FILE.json [...]     -> per-file ACCEPT/REJECT report;
                                                exit 0 iff all ACCEPT
  python3 checker_ref.py --controls FILE.json -> run the six FORMAT.md sec. 11
         negative-control mutations of FILE and verify each is rejected at
         exactly the intended check; exit 0 iff all six behave as specified
"""

import json
import re
import sys
from fractions import Fraction

_INT = re.compile(r"^-?(0|[1-9][0-9]*)$")
_NAT = re.compile(r"^(0|[1-9][0-9]*)$")
_POS = re.compile(r"^[1-9][0-9]*$")

_LABELS = {
    "zeta": "kernel-checked modulo displayed hypotheses H-ENCL and H-AP (producers untrusted)",
    "f_DH": "checker-level only (D-R8): format-checked modulo H-ENCL for f_DH; no Lean-backed conclusion",
}
_REQ = ("format", "version", "mode", "function", "trust_label",
        "rect", "scales", "claimed_m", "mesh", "segments")
_OPT = ("modulus_floor", "producer", "comment")
_ROWK = ("reLo", "reHi", "imLo", "imHi", "argLo", "argHi")


class Reject(Exception):
    def __init__(self, check, why):
        super().__init__("%s: %s" % (check, why))
        self.check = check


# ------------------------------------------------------------------ shape layer

def _istr(v, pat, where):
    if not isinstance(v, str) or not pat.match(v):
        raise Reject("SHAPE", "%s: bad integer string %r" % (where, v))
    return int(v)


def _rational(v, where):
    if not isinstance(v, dict) or sorted(v.keys()) != ["d", "n"]:
        raise Reject("SHAPE", "%s: rational must have exactly n, d" % where)
    return (_istr(v["n"], _INT, where + ".n"), _istr(v["d"], _POS, where + ".d"))


def load(doc):
    """Shape-validate per w1-schema.json semantics; return the literal data."""
    if not isinstance(doc, dict):
        raise Reject("SHAPE", "root must be an object")
    missing = [k for k in _REQ if k not in doc]
    if missing:
        raise Reject("SHAPE", "missing %s" % ", ".join(missing))
    extra = [k for k in doc if k not in _REQ + _OPT]
    if extra:
        raise Reject("SHAPE", "unknown field(s) %s" % ", ".join(extra))
    if doc["format"] != "W1-rect-transcript":
        raise Reject("SHAPE", "format != W1-rect-transcript")
    if doc["version"] != "1.0":
        raise Reject("SHAPE", "version != 1.0")
    if doc["mode"] not in ("refutation", "exclusion"):
        raise Reject("SHAPE", "bad mode %r" % (doc["mode"],))
    if doc["function"] not in _LABELS:
        raise Reject("SHAPE", "bad function %r" % (doc["function"],))
    if doc["trust_label"] != _LABELS[doc["function"]]:
        raise Reject("SHAPE", "trust_label is not the fixed verbatim string "
                              "for function %s" % doc["function"])
    rect = doc["rect"]
    if not isinstance(rect, dict) or sorted(rect) != ["T1", "T2", "sigma1", "sigma2"]:
        raise Reject("SHAPE", "rect must have sigma1, sigma2, T1, T2")
    scales = doc["scales"]
    if not isinstance(scales, dict) or sorted(scales) != ["A", "K"]:
        raise Reject("SHAPE", "scales must have K, A")
    mesh = doc["mesh"]
    if not isinstance(mesh, dict) or sorted(mesh) != ["bottom", "left", "right", "top"]:
        raise Reject("SHAPE", "mesh must have bottom, right, top, left")
    m_claim = _istr(doc["claimed_m"], _NAT, "claimed_m")
    # NOTE: w1-schema.json's allOf also ties mode "exclusion" to claimed_m "0".
    # That tie is deliberately NOT enforced at the shape layer here: it is the
    # semantic check C10's job on the translated literals (the Lean checker has
    # no mode field at all -- the theorem splits on m), and FORMAT.md sec. 11's
    # negative control expects the mode/m mismatch to be REJECTED AT C10.
    # reference_checker.py reads the contract the same way.
    data = {
        "mode": doc["mode"],
        "function": doc["function"],
        "m": m_claim,
        "K": _istr(scales["K"], _POS, "scales.K"),
        "A": _istr(scales["A"], _POS, "scales.A"),
        "rect": {k: _rational(rect[k], "rect." + k) for k in rect},
        "mesh": {},
        "rows": [],
        "floor": None,
    }
    for e in ("bottom", "right", "top", "left"):
        lst = mesh[e]
        if not isinstance(lst, list) or len(lst) < 2:
            raise Reject("SHAPE", "mesh.%s must be a list of >= 2 rationals" % e)
        data["mesh"][e] = [_rational(v, "mesh.%s[%d]" % (e, i))
                           for i, v in enumerate(lst)]
    segs = doc["segments"]
    if not isinstance(segs, list) or len(segs) < 4:
        raise Reject("SHAPE", "segments must be a list of >= 4 rows")
    for i, row in enumerate(segs):
        if not isinstance(row, dict) or sorted(row) != sorted(_ROWK):
            raise Reject("SHAPE", "segments[%d] must have exactly %s" % (i, ", ".join(_ROWK)))
        data["rows"].append(tuple(_istr(row[k], _INT, "segments[%d].%s" % (i, k))
                                  for k in _ROWK))
    if "modulus_floor" in doc:
        fl = doc["modulus_floor"]
        if not isinstance(fl, dict) or sorted(fl) != ["Fd", "Fn"]:
            raise Reject("SHAPE", "modulus_floor must have Fn, Fd")
        data["floor"] = (_istr(fl["Fn"], _NAT, "modulus_floor.Fn"),
                         _istr(fl["Fd"], _POS, "modulus_floor.Fd"))
    if "producer" in doc and not isinstance(doc["producer"], dict):
        raise Reject("SHAPE", "producer must be an object")
    if "comment" in doc and not isinstance(doc["comment"], str):
        raise Reject("SHAPE", "comment must be a string")
    return data


# ------------------------------------------------------------------ checks C1-C11

def _fr(pair):
    n, d = pair
    return Fraction(n, d)     # exact; comparisons match cross-multiplication (D7)


def run_checks(d):
    """Run C1-C11 on loaded data; raise Reject at the first failure; return the
    ordered list of passed check names."""
    passed = []

    def ok(name, cond, why):
        if not cond:
            raise Reject(name, why)
        if name not in passed:
            passed.append(name)

    # C1 -- scales and denominators
    ok("C1", d["K"] >= 1 and d["A"] >= 1, "K, A must be >= 1")
    for k, pair in d["rect"].items():
        ok("C1", pair[1] >= 1, "rect.%s denominator < 1" % k)
    for e, lst in d["mesh"].items():
        for i, pair in enumerate(lst):
            ok("C1", pair[1] >= 1, "mesh.%s[%d] denominator < 1" % (e, i))
    if d["floor"] is not None:
        ok("C1", d["floor"][1] >= 1, "modulus_floor.Fd < 1")

    # C2 -- rectangle (Fraction comparisons = cross-multiplication, D7)
    s1, s2 = _fr(d["rect"]["sigma1"]), _fr(d["rect"]["sigma2"])
    t1, t2 = _fr(d["rect"]["T1"]), _fr(d["rect"]["T2"])
    ok("C2", Fraction(1, 2) < s1, "sigma1 <= 1/2")
    ok("C2", s1 <= s2, "sigma1 > sigma2")
    ok("C2", s2 < 1, "sigma2 >= 1")
    ok("C2", t1 < t2, "T1 >= T2")

    # C3 -- mesh walk
    walks = (("bottom", s1, s2, +1), ("right", t1, t2, +1),
             ("top", s2, s1, -1), ("left", t2, t1, -1))
    for e, first, last, direction in walks:
        vals = [_fr(p) for p in d["mesh"][e]]
        ok("C3", vals[0] == first, "%s[0] != required endpoint" % e)
        ok("C3", vals[-1] == last, "%s[last] != required endpoint" % e)
        for i in range(len(vals) - 1):
            if direction > 0:
                ok("C3", vals[i] < vals[i + 1], "%s not strictly increasing at %d" % (e, i))
            else:
                ok("C3", vals[i] > vals[i + 1], "%s not strictly decreasing at %d" % (e, i))

    # C4 -- row count
    M = sum(len(d["mesh"][e]) - 1 for e in ("bottom", "right", "top", "left"))
    ok("C4", len(d["rows"]) == M, "|segments| = %d != M = %d" % (len(d["rows"]), M))

    # C5, C6, C7 -- per-row
    A = d["A"]
    for k, (reLo, reHi, imLo, imHi, argLo, argHi) in enumerate(d["rows"]):
        ok("C5", reLo <= reHi and imLo <= imHi, "empty value box at row %d" % k)
        ok("C6", reLo > 0 or reHi < 0 or imLo > 0 or imHi < 0,
           "value box at row %d does not exclude 0" % k)
        ok("C7", argLo <= argHi and -A <= 2 * argLo and 2 * argHi <= A,
           "argument row %d invalid or outside the D3 clamp" % k)

    # C8, C9 -- winding enclosure
    S_lo = sum(r[4] for r in d["rows"])
    S_hi = sum(r[5] for r in d["rows"])
    ok("C8", 2 * (S_hi - S_lo) < A,
       "winding width 2*%d >= A" % (S_hi - S_lo))
    ok("C9", S_lo <= A * d["m"] <= S_hi,
       "A*m = %d outside [%d, %d]" % (A * d["m"], S_lo, S_hi))

    # C10 -- mode tie
    if d["mode"] == "refutation":
        ok("C10", d["m"] >= 1, "refutation with m = 0")
    else:
        ok("C10", d["m"] == 0, "exclusion with m != 0")

    # C11 -- optional floor
    if d["floor"] is not None:
        Fn, Fd = d["floor"]
        K = d["K"]
        for k, (reLo, reHi, imLo, imHi, _al, _ah) in enumerate(d["rows"]):
            mre = 0 if reLo <= 0 <= reHi else min(abs(reLo), abs(reHi))
            mim = 0 if imLo <= 0 <= imHi else min(abs(imLo), abs(imHi))
            ok("C11", (mre * mre + mim * mim) * Fd * Fd >= Fn * Fn * K * K,
               "floor fails at row %d" % k)
    return passed


def check_file(path, verbose=True):
    with open(path) as fh:
        doc = json.load(fh)
    try:
        data = load(doc)
        passed = run_checks(data)
    except Reject as rj:
        if verbose:
            print("%s: REJECT at %s (%s)" % (path, rj.check, rj))
        return False, rj.check
    if verbose:
        n_rows = len(data["rows"])
        S_lo = sum(r[4] for r in data["rows"])
        S_hi = sum(r[5] for r in data["rows"])
        print("%s: ACCEPT (%s/%s, m=%d, %d segments, S=[%d, %d], A=%d; "
              "checks passed: %s%s)"
              % (path, data["function"], data["mode"], data["m"], n_rows,
                 S_lo, S_hi, data["A"], " ".join(passed),
                 "" if data["floor"] is None else "; floor verified"))
    return True, None


# ------------------------------------------------------------------ negative controls

def _mutate(doc, which):
    """The six FORMAT.md sec. 11 negative-control mutations (deep-copied)."""
    d = json.loads(json.dumps(doc))
    if which == "C6":       # a value box containing 0
        d["segments"][0].update(reLo="-5", reHi="5", imLo="-5", imHi="5")
    elif which == "C8":     # over-wide argument row, kept C7-clamp-legal:
        # row 0 -> [-A/2, A/2] adds width >= A - (old row width) so the total
        # width at least doubles past A/2 -- trips C8 while every 2*|arg| <= A
        A = int(d["scales"]["A"])
        d["segments"][0]["argLo"] = str(-(A // 2))
        d["segments"][0]["argHi"] = str(A // 2)
    elif which == "C9":     # claimed_m off by one
        d["claimed_m"] = str(int(d["claimed_m"]) + 1)
    elif which == "C10":    # exclusion with m = claimed nonzero
        d["mode"] = "exclusion"
    elif which == "C3":     # bottom[last] != sigma2
        d["mesh"]["bottom"][-1] = {"n": "1", "d": "2"}
    elif which == "C2":     # sigma1 = 1/2
        d["rect"]["sigma1"] = {"n": "1", "d": "2"}
        d["mesh"]["bottom"][0] = {"n": "1", "d": "2"}
        d["mesh"]["left"][-1] = {"n": "1", "d": "2"}
    return d


def controls(path):
    """Each mutation must be rejected at exactly the intended check.  The C10
    control needs a refutation transcript as its base (m >= 1)."""
    with open(path) as fh:
        base = json.load(fh)
    ok_all = True
    print("negative controls on %s (FORMAT.md sec. 11 list):" % path)
    for which in ("C6", "C8", "C9", "C10", "C3", "C2"):
        mut = _mutate(base, which)
        try:
            run_checks(load(mut))
            got = "ACCEPT"
        except Reject as rj:
            got = rj.check
        good = got == which
        ok_all &= good
        print("  mutate-for-%s -> %s %s" % (which, got, "OK" if good else "WRONG"))
    return ok_all


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "--controls":
        return 0 if controls(argv[1]) else 1
    all_ok = True
    for path in argv:
        ok, _ = check_file(path)
        all_ok &= ok
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
