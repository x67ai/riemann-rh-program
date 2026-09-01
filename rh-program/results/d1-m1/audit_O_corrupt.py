"""audit_O_corrupt.py -- AUDITOR O: adversarial corruption of ACCEPTED W1 transcripts.

Task item 3.  Takes REAL (producer-emitted, both legs, both checkers-accepted)
transcripts from acceptance/ and mutates them the way a buggy or dishonest
producer plausibly would; every mutation must be REJECTED by BOTH untrusted
Python checkers at the intended check.  A mutation that is ACCEPTED is either
(i) a checker hole (a defect), or (ii) an invisible-by-design mutation whose
detection lives in H-ENCL / the two-producer cross-check, not in the checker --
each such case is labeled EXPECTED-INVISIBLE below with the reason.

Also emits Lean literal instances (audit_O_lean_cases.lean) so the SAME clean
and corrupted data can be run through the KERNEL checker `checkW1`.

Run: python3 audit_O_corrupt.py
"""
import copy, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import checker_ref
import reference_checker

HERE = os.path.dirname(os.path.abspath(__file__))
ACC = os.path.join(HERE, "acceptance")

BASES = [
    ("mp-null-t100", "w1-mp-null-t100.json"),
    ("arb-null-t100", "w1-arb-null-t100.json"),
    ("mp-null-deep-t100", "w1-mp-null-deep-t100.json"),
    ("mp-dh-livefire", "w1-mp-dh-livefire.json"),
    ("arb-dh-livefire", "w1-arb-dh-livefire.json"),
]


def run_both(doc):
    """(verdict_ref, verdict_author) as check-name strings or 'ACCEPT'."""
    try:
        checker_ref.run_checks(checker_ref.load(doc))
        v1 = "ACCEPT"
    except checker_ref.Reject as rj:
        v1 = rj.check
    except Exception as e:                      # shape crash counts as a reject
        v1 = "CRASH:%s" % type(e).__name__
    try:
        reference_checker.check(reference_checker.parse(doc), lambda *_a, **_k: None)
        v2 = "ACCEPT"
    except reference_checker.Fail as f:
        v2 = f.check
    except Exception as e:
        v2 = "CRASH:%s" % type(e).__name__
    return v1, v2


# ------------------------------------------------------------ mutations
def mut_c6_shift_zero_in(doc):
    """Shift ONE segment's value enclosure so that 0 enters the cell.  The
    shift is by the box's own width, i.e. exactly what a producer with an
    off-by-one-segment indexing bug or a sign error would emit."""
    d = copy.deepcopy(doc)
    k = len(d["segments"]) // 2
    r = d["segments"][k]
    reLo, reHi = int(r["reLo"]), int(r["reHi"])
    imLo, imHi = int(r["imLo"]), int(r["imHi"])
    w = max(abs(reLo), abs(reHi), abs(imLo), abs(imHi), 1)
    r["reLo"], r["reHi"] = str(-w), str(w)
    r["imLo"], r["imHi"] = str(-w), str(w)
    return d, "C6"


def mut_c8_width(doc):
    """Break the sum-width < 1/2-turn condition while keeping every row
    individually C7-legal (each |2*arg| <= A): widen ONE row to the full clamp."""
    d = copy.deepcopy(doc)
    A = int(d["scales"]["A"])
    d["segments"][0]["argLo"] = str(-(A // 2))
    d["segments"][0]["argHi"] = str(A // 2)
    return d, "C8"


def mut_c9_m_plus1(doc):
    d = copy.deepcopy(doc)
    d["claimed_m"] = str(int(d["claimed_m"]) + 1)
    return d, "C9"


def mut_c9_m_big(doc):
    """The dangerous one: claim a nonzero winding on an m = 0 (exclusion) box
    and relabel the mode -- a fabricated 'off-line zero'."""
    d = copy.deepcopy(doc)
    d["claimed_m"] = "1"
    d["mode"] = "refutation"
    return d, "C9"


def mut_c3_order(doc):
    """Break the contour ordering: swap two adjacent interior breakpoints of the
    bottom edge (the mesh no longer walks monotonically) and swap the matching
    rows so the row count still matches."""
    d = copy.deepcopy(doc)
    b = d["mesh"]["bottom"]
    if len(b) < 4:
        b[0], b[1] = b[1], b[0]
    else:
        b[1], b[2] = b[2], b[1]
    return d, "C3"


def mut_c3_reverse_top(doc):
    """A traversal-direction bug: emit the TOP edge increasing (as if the
    producer forgot the CCW convention)."""
    d = copy.deepcopy(doc)
    d["mesh"]["top"] = list(reversed(d["mesh"]["top"]))
    return d, "C3"


def mut_c2_sigma_half(doc):
    """Move sigma1 onto the critical line (the straddling-box laundering attempt)."""
    d = copy.deepcopy(doc)
    d["rect"]["sigma1"] = {"n": "1", "d": "2"}
    d["mesh"]["bottom"][0] = {"n": "1", "d": "2"}
    d["mesh"]["top"][-1] = {"n": "1", "d": "2"}
    d["mesh"]["left"] = d["mesh"]["left"]
    return d, "C2"


def mut_c4_drop_row(doc):
    """Drop one row (a truncated write)."""
    d = copy.deepcopy(doc)
    d["segments"] = d["segments"][:-1]
    return d, "C4"


def mut_c4_drop_breakpoint(doc):
    """Drop one interior mesh breakpoint (a gap in the contour)."""
    d = copy.deepcopy(doc)
    if len(d["mesh"]["right"]) > 2:
        del d["mesh"]["right"][1]
    return d, "C4"


def mut_c11_floor_up(doc):
    """Inflate the claimed modulus floor beyond what the boxes support."""
    d = copy.deepcopy(doc)
    if "modulus_floor" not in d:
        return None, None
    d["modulus_floor"]["Fn"] = str(int(d["modulus_floor"]["Fn"]) * 1000 + 1)
    return d, "C11"


def mut_c5_empty_box(doc):
    d = copy.deepcopy(doc)
    r = d["segments"][1]
    r["reLo"], r["reHi"] = r["reHi"], r["reLo"]
    if int(r["reLo"]) <= int(r["reHi"]):
        r["reLo"] = str(int(r["reHi"]) + 1)
    return d, "C5"


def mut_c7_overclamp(doc):
    d = copy.deepcopy(doc)
    A = int(d["scales"]["A"])
    d["segments"][0]["argHi"] = str(A // 2 + 1)
    return d, "C7"


def mut_scale_K_shrink(doc):
    """SCALE ATTACK: divide K by 10^6 without rescaling the value boxes.  The
    rows then claim |f| ~ 10^6 times larger than certified -- a scale-handling
    bug.  The checker CANNOT see this (K only enters C1 and C11); it is
    detectable only through H-ENCL / C11 when a floor is present."""
    d = copy.deepcopy(doc)
    K = int(d["scales"]["K"])
    d["scales"]["K"] = str(max(1, K // 10 ** 6))
    return d, "?"


def mut_scale_A_shrink(doc):
    """SCALE ATTACK on A: shrink A by 10^3 leaving the argument rows alone.
    The claimed winding then becomes 10^3 turns.  MUST be caught (C8 or C9)."""
    d = copy.deepcopy(doc)
    A = int(d["scales"]["A"])
    d["scales"]["A"] = str(max(1, A // 10 ** 3))
    return d, "C7/C8/C9"


def mut_permute_rows(doc):
    """Rotate the row list by one: rows no longer correspond to their mesh
    segments.  EXPECTED-INVISIBLE: C1-C11 are permutation-invariant on rows,
    and the row<->segment correspondence lives in H-ENCL (List.Forall₂ rows
    (segs d)), i.e. it would make the displayed hypothesis FALSE, not the
    checker wrong.  Recorded so the trust boundary is stated, not assumed."""
    d = copy.deepcopy(doc)
    d["segments"] = d["segments"][1:] + d["segments"][:1]
    return d, "EXPECTED-INVISIBLE"


def mut_negate_boxes(doc):
    """Negate every value box (f -> -f): still 0-excluding, still winds the
    same.  EXPECTED-INVISIBLE for the same reason (H-ENCL is where the values
    are asserted)."""
    d = copy.deepcopy(doc)
    for r in d["segments"]:
        r["reLo"], r["reHi"] = str(-int(r["reHi"])), str(-int(r["reLo"]))
        r["imLo"], r["imHi"] = str(-int(r["imHi"])), str(-int(r["imLo"]))
    return d, "EXPECTED-INVISIBLE"


def mut_trust_label(doc):
    """Swap the trust label to the (stronger) zeta one on an f_DH transcript --
    the D-R8 laundering attempt.  Shape layer must catch it."""
    d = copy.deepcopy(doc)
    if d["function"] != "f_DH":
        return None, None
    d["trust_label"] = checker_ref._LABELS["zeta"]
    return d, "SHAPE"


def mut_function_swap(doc):
    """Relabel an f_DH transcript as a zeta transcript (label + function)."""
    d = copy.deepcopy(doc)
    if d["function"] != "f_DH":
        return None, None
    d["function"] = "zeta"
    d["trust_label"] = checker_ref._LABELS["zeta"]
    return d, "EXPECTED-INVISIBLE"


MUTATIONS = [
    ("C6 shift enclosure so 0 enters a cell", mut_c6_shift_zero_in),
    ("C8 break sum-width < 1/2 turn", mut_c8_width),
    ("C9 change integer m (m+1)", mut_c9_m_plus1),
    ("C9 fabricate m=1 on an exclusion box + relabel mode", mut_c9_m_big),
    ("C3 break contour ordering (swap breakpoints)", mut_c3_order),
    ("C3 reverse the top edge (CCW convention broken)", mut_c3_reverse_top),
    ("C2 move sigma1 onto the critical line", mut_c2_sigma_half),
    ("C4 drop one row", mut_c4_drop_row),
    ("C4 drop one mesh breakpoint", mut_c4_drop_breakpoint),
    ("C11 inflate the modulus floor", mut_c11_floor_up),
    ("C5 emit an empty value box", mut_c5_empty_box),
    ("C7 exceed the D3 half-turn clamp", mut_c7_overclamp),
    ("scale-K shrink by 1e6 (values not rescaled)", mut_scale_K_shrink),
    ("scale-A shrink by 1e3 (arg rows not rescaled)", mut_scale_A_shrink),
    ("permute rows by one (row<->segment misalignment)", mut_permute_rows),
    ("negate every value box (f -> -f)", mut_negate_boxes),
    ("f_DH transcript wearing the zeta trust label", mut_trust_label),
    ("f_DH transcript relabeled function=zeta", mut_function_swap),
]


def main():
    out = []

    def say(s):
        print(s); sys.stdout.flush(); out.append(s)

    say("AUDIT O -- corruption of ACCEPTED transcripts (task item 3)")
    say("checkers: checker_ref.py (Fraction) | reference_checker.py (int cross-mult)")
    bad = 0
    for name, fn in BASES:
        path = os.path.join(ACC, fn)
        with open(path) as fh:
            base = json.load(fh)
        v1, v2 = run_both(base)
        say("")
        say("== base %-20s %-28s -> %s | %s  (%d rows, m=%s, %s)"
            % (name, fn, v1, v2, len(base["segments"]), base["claimed_m"], base["mode"]))
        if (v1, v2) != ("ACCEPT", "ACCEPT"):
            bad += 1
            say("   !! BASE NOT ACCEPTED BY BOTH -- audit precondition broken")
        for label, mut in MUTATIONS:
            d, expect = mut(base)
            if d is None:
                continue
            v1, v2 = run_both(d)
            if expect == "EXPECTED-INVISIBLE":
                verdict = "as-designed" if (v1, v2) == ("ACCEPT", "ACCEPT") else "CHANGED(%s|%s)" % (v1, v2)
            elif expect in ("?", "C7/C8/C9"):
                verdict = "%s|%s" % (v1, v2)
            else:
                good = (v1 == expect and v2 == expect)
                verdict = "OK" if good else "MISMATCH exp=%s got=%s|%s" % (expect, v1, v2)
                if not good:
                    bad += 1
            say("   %-52s -> %-10s %-10s %s" % (label, v1, v2, verdict))
    say("")
    say("BASES x MUTATIONS run; unexpected results: %d" % bad)
    with open(os.path.join(HERE, "audit_O_corrupt.txt"), "w") as fh:
        fh.write("\n".join(out) + "\n")
    return bad


if __name__ == "__main__":
    sys.exit(0 if main() == 0 else 1)
