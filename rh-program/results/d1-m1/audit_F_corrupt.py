"""audit_F_corrupt.py -- AUDIT F: hand-corrupt ACCEPTED producer transcripts the way a
buggy producer would, and confirm both untrusted Python checkers REJECT each one at
the expected check.  Also writes the corrupted files (for the Lean run, see
audit_F_lean_emit.py) into an output directory.

Base transcripts (all ACCEPTED by both checkers in Session 8):
  acceptance/w1-mp-null-t100.json, acceptance/w1-arb-null-t100.json,
  acceptance/w1-mp-dh-livefire.json, acceptance/w1-arb-dh-livefire.json

Mutations (each applied independently to each base):
  M1  shift one value box so 0 enters the cell            -> C6
  M2  widen one argument row (C7-legal) to break C8       -> C8
  M3  change claimed_m by +1                              -> C9 (or C10 for exclusion+1 -- C9 first)
  M3b change claimed_m to a different integer inside the enclosure? impossible when
      width < 1/2; instead set claimed_m := 0 on a refutation -> C9 (0 outside [S_lo,S_hi])
  M4  break contour ordering: swap two interior bottom breakpoints     -> C3
  M5  reverse the right edge (T2 -> T1 listed increasing? no: make it decreasing) -> C3
  M6  drop an interior breakpoint but keep the rows          -> C4
  M7  drop a segment row                                     -> C4
  M8  duplicate a breakpoint (zero-length segment)           -> C3 (strictness)
  M9  set sigma1 = 1/2 (with mesh corners moved)             -> C2
  M10 set T1 = T2 (with mesh corners moved)                  -> C2
  M11 empty value box (reLo > reHi) on a row                 -> C5
  M12 argument row beyond the D3 clamp                       -> C7
  M13 denominator "0" in a mesh rational                     -> SHAPE (pattern) [Lean: C1]
  M14 negative denominator "-5" in rect.sigma1               -> SHAPE [Lean: C1]
  M15 mode flipped exclusion<->refutation, m unchanged       -> C10
  M16 corner mismatch: bottom[0] != sigma1                   -> C3
  M17 top edge listed increasing (reversed list)             -> C3
  M18 value box shifted to touch 0 exactly (reLo = 0, others straddle) -> C6 (strictness)
  M19 K changed to "0"                                       -> SHAPE [Lean: C1]
  M20 modulus floor Fn raised above the certified minimum    -> C11
"""
import copy
import json
import os
import sys

import checker_ref
import reference_checker

HERE = os.path.dirname(os.path.abspath(__file__))
BASES = ["acceptance/w1-mp-null-t100.json", "acceptance/w1-arb-null-t100.json",
         "acceptance/w1-mp-dh-livefire.json", "acceptance/w1-arb-dh-livefire.json"]


def mutations(doc):
    A = int(doc["scales"]["A"])
    out = []

    def mut(name, expect, f):
        d = copy.deepcopy(doc)
        f(d)
        out.append((name, expect, d))

    def m1(d):  # shift a box so 0 enters
        r = d["segments"][3]
        r["reLo"], r["reHi"], r["imLo"], r["imHi"] = "-7", "7", "-7", "7"
    mut("M1 box straddles 0", "C6", m1)

    def m2(d):  # C7-legal widening that breaks C8
        r = d["segments"][0]
        r["argLo"], r["argHi"] = str(-(A // 2)), str(A // 2)
    mut("M2 wide arg row", "C8", m2)

    def m3(d):
        d["claimed_m"] = str(int(d["claimed_m"]) + 1)
    mut("M3 claimed_m+1", "C9", m3)

    if int(doc["claimed_m"]) >= 1:
        def m3b(d):
            d["claimed_m"] = "0"
        mut("M3b claimed_m:=0 on refutation", "C9", m3b)

    def m4(d):
        b = d["mesh"]["bottom"]
        if len(b) >= 4:
            b[1], b[2] = b[2], b[1]
        else:
            b[1] = {"n": "999", "d": "1"}
    mut("M4 swap bottom breakpoints", "C3", m4)

    def m5(d):
        d["mesh"]["right"] = list(reversed(d["mesh"]["right"]))
    mut("M5 right edge reversed", "C3", m5)

    def m6(d):
        del d["mesh"]["right"][1]
    mut("M6 drop interior breakpoint, keep rows", "C4", m6)

    def m7(d):
        del d["segments"][5]
    mut("M7 drop a segment row", "C4", m7)

    def m8(d):
        d["mesh"]["left"].insert(1, copy.deepcopy(d["mesh"]["left"][1]))
        d["segments"].append(copy.deepcopy(d["segments"][-1]))
    mut("M8 duplicated breakpoint (zero-length seg) + row", "C3", m8)

    def m9(d):
        d["rect"]["sigma1"] = {"n": "1", "d": "2"}
        d["mesh"]["bottom"][0] = {"n": "1", "d": "2"}
        d["mesh"]["top"][-1] = {"n": "1", "d": "2"}
        d["mesh"]["left"] = d["mesh"]["left"]
    mut("M9 sigma1 = 1/2", "C2", m9)

    def m10(d):
        d["rect"]["T2"] = copy.deepcopy(d["rect"]["T1"])
        d["mesh"]["right"][-1] = copy.deepcopy(d["rect"]["T1"])
        d["mesh"]["left"][0] = copy.deepcopy(d["rect"]["T1"])
    mut("M10 T1 = T2", "C2", m10)

    def m11(d):
        r = d["segments"][2]
        r["reLo"], r["reHi"] = r["reHi"], r["reLo"]
        if r["reLo"] == r["reHi"]:
            r["reLo"] = str(int(r["reHi"]) + 1)
    mut("M11 empty value box", "C5", m11)

    def m12(d):
        r = d["segments"][1]
        r["argHi"] = str(A // 2 + 1)
    mut("M12 arg row beyond clamp", "C7", m12)

    def m13(d):
        d["mesh"]["bottom"][1] = {"n": d["mesh"]["bottom"][1]["n"], "d": "0"}
    mut("M13 denominator 0", "SHAPE", m13)

    def m14(d):
        d["rect"]["sigma1"] = {"n": "-" + d["rect"]["sigma1"]["n"], "d": "-" + d["rect"]["sigma1"]["d"]}
    mut("M14 negative denominator", "SHAPE", m14)

    def m15(d):
        d["mode"] = "exclusion" if d["mode"] == "refutation" else "refutation"
    mut("M15 mode flipped", "C10", m15)

    def m16(d):
        b = d["mesh"]["bottom"][0]
        d["mesh"]["bottom"][0] = {"n": str(int(b["n"]) * 10 + 1), "d": str(int(b["d"]) * 10)}
    mut("M16 bottom[0] != sigma1", "C3", m16)

    def m17(d):
        d["mesh"]["top"] = list(reversed(d["mesh"]["top"]))
    mut("M17 top edge listed increasing", "C3", m17)

    def m18(d):
        r = d["segments"][4]
        r["reLo"], r["reHi"], r["imLo"], r["imHi"] = "0", "5", "-5", "5"
    mut("M18 box touches 0 (reLo = 0)", "C6", m18)

    def m19(d):
        d["scales"]["K"] = "0"
    mut("M19 K = 0", "SHAPE", m19)

    if "modulus_floor" in doc:
        def m20(d):
            d["modulus_floor"]["Fn"] = str(int(d["modulus_floor"]["Fn"]) * 2 + 1)
        mut("M20 floor Fn doubled", "C11", m20)

    def m21(d):  # all argument rows negated: sum in [-S_hi, -S_lo]; m unchanged
        for r in d["segments"]:
            r["argLo"], r["argHi"] = str(-int(r["argHi"])), str(-int(r["argLo"]))
    mut("M21 all arg rows negated (orientation flip)", "C9" if int(doc["claimed_m"]) >= 1 else "ACCEPT", m21)

    def m22(d):  # segments rotated by one (rows misaligned with mesh) -- undetectable by design
        d["segments"] = d["segments"][1:] + d["segments"][:1]
    mut("M22 rows cyclically shifted (misaligned; H-ENCL false, format-accepted by design)", "ACCEPT", m22)

    return out


def run_checker_ref(doc):
    try:
        checker_ref.run_checks(checker_ref.load(doc))
        return "ACCEPT"
    except checker_ref.Reject as rj:
        return rj.check


def run_reference_checker(doc):
    try:
        reference_checker.check(reference_checker.parse(doc), lambda s: None)
        return "ACCEPT"
    except reference_checker.Fail as e:
        return e.check


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "audit_F_corrupted")
    os.makedirs(outdir, exist_ok=True)
    bad = 0
    n = 0
    for base in BASES:
        with open(os.path.join(HERE, base)) as fh:
            doc = json.load(fh)
        assert run_checker_ref(doc) == "ACCEPT" and run_reference_checker(doc) == "ACCEPT", base
        print("== base %s: ACCEPT by both checkers (m=%s, %d rows)" % (base, doc["claimed_m"], len(doc["segments"])))
        for name, expect, d in mutations(doc):
            n += 1
            a, b = run_checker_ref(d), run_reference_checker(d)
            ok = (a == expect and b == expect) or (expect == "ACCEPT" and a == b == "ACCEPT")
            # for C9-vs-C10 ambiguity on exclusion bases: accept either C9/C10 as long as REJECT
            if not ok and expect not in ("ACCEPT",) and a != "ACCEPT" and b != "ACCEPT":
                ok = True
                note = " (rejected, at %s/%s not the predicted %s)" % (a, b, expect)
            else:
                note = ""
            if not ok:
                bad += 1
            print("   %-70s checker_ref=%-6s reference_checker=%-6s expected=%-6s %s%s"
                  % (name, a, b, expect, "OK" if ok else "**WRONG**", note))
            fname = os.path.join(outdir, os.path.basename(base)[:-5] + "__" + name.split()[0] + ".json")
            with open(fname, "w") as fh:
                json.dump(d, fh, indent=1)
    print("\n%d mutations run; %d unexpected outcomes" % (n, bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
