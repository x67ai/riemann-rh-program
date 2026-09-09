#!/usr/bin/env python3
"""backparse_lane_a.py -- independent BACK-PARSE of the Lane A literal modules written by emit_lean_lane_a.py against
the JSON transcripts (KICKSTART.md Part 2 item 10(j), the program's two-producer back-parse cross-check; the FORMAT.md
§10 discipline that verify_lean_m2a.py applied to Lane B).  Session 19, phase 3(d), 2026-09-09.

For each leg it reads <lean-root>/Zeta23/DBN/Instance02/Asym_<P>.lean with regular expressions only (no code shared
with the emitter), rebuilds {K, t0, y0, yA, rows, tail} from the `row2Asym<PP> : AsymData` literal and compares EVERY
integer with asym-<leg>.json (exact); checks that the kernel theorem `row2Asym<PP>_check : checkAsym row2Asym<PP> =
true := by decide +kernel` is present unaltered, that the three parameter facts carry the JSON's t0/y0/yA, that the
glue lemma `row2_laneA_<P>` is present with its conclusion CHARACTER FOR CHARACTER the type of the former `hLaneA`
binder of Instance02.lean and its pinned first row equal to the literal's first row, and that the module contains no
`sorry`, `native_decide`, `axiom`, `unsafe`, `implemented_by`, `extern` or `opaque` outside comments.
Then the two legs are compared with each other where they must agree: Nlo/Nhi per row and N1 exactly (the shared
UNTRUSTED plan), T/K and Q_i/K to rtol 1e-9 (the same derived reals computed independently; the exact integers need
only agree WITHIN a leg, the scales differ); E/K and E1/K are hull upper bounds — their Arb/mp ratios are RECORDED,
never gated, and the legs are never merged (D-R3).  Exit 0 = 0 mismatches.

usage: backparse_lean_a.py <lean-root> <asym-mp.json> <asym-arb.json>
"""
import json, os, re, sys
from fractions import Fraction

# the former `hLaneA` type, verbatim from Zeta23/DBN/Instance02.lean (Session 16 text), as the glue lemma's conclusion
HLANEA_CONCLUSION = ("∀ x y : ℝ, 5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y →\n"
                     "      y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (x + y * I) ≠ 0")
TRUST_WORDS = ("sorry", "native_decide", "axiom", "unsafe", "implemented_by", "extern", "opaque")

def strip_comments(src):
    """remove /- ... -/ block comments (nested one level is enough here) and -- line comments"""
    out = re.sub(r"/-.*?-/", "", src, flags=re.S)
    out = re.sub(r"--[^\n]*", "", out)
    return out

def parse_module(path, prefix):
    PP = prefix.upper(); lit = f"row2Asym{PP}"; glue = f"row2_laneA_{prefix}"
    src = open(path, encoding="utf-8").read()
    code = strip_comments(src)
    problems = []
    # 1. the literal
    m = re.search(r"def " + lit + r" : AsymData :=\n  \{(.*?)\}\n", code, re.S)
    if not m: raise SystemExit(f"{path}: literal `{lit}` not found")
    blk = m.group(1)
    def scalar(f):
        mm = re.search(r"(?<![A-Za-z0-9_])" + f + r" := (-?\d+)", blk)
        if not mm: raise SystemExit(f"{path}: field {f} missing in the literal")
        return int(mm.group(1))
    K = scalar("K")
    t0 = (scalar("t0n"), scalar("t0d")); y0 = (scalar("y0n"), scalar("y0d")); yA = (scalar("yAn"), scalar("yAd"))
    mr = re.search(r"rows := \[(.*?)\]", blk, re.S)
    if not mr: raise SystemExit(f"{path}: rows list missing")
    rows = [tuple(int(x.strip()) for x in t.split(",")) for t in re.findall(r"⟨([^⟩]*)⟩", mr.group(1))]
    if any(len(r) != 4 for r in rows): raise SystemExit(f"{path}: a row does not have 4 integers")
    mt = re.search(r"tail := ⟨([^⟩]*)⟩", blk)
    if not mt: raise SystemExit(f"{path}: tail missing")
    tail = tuple(int(x.strip()) for x in mt.group(1).split(","))
    if len(tail) != 6: raise SystemExit(f"{path}: the tail does not have 6 integers")
    # 2. the kernel fact, unaltered
    if not re.search(r"^theorem " + lit + r"_check : checkAsym " + lit + r" = true := by decide \+kernel$", code, re.M):
        problems.append("kernel theorem missing or altered")
    # 3. the three parameter facts carry the literal's own rationals
    facts = {}
    for f, fn in (("t0", "At0"), ("y0", "Ay0"), ("yA", "AyA")):
        mm = re.search(r"^theorem " + lit + "_" + f + r" : " + fn + " " + lit + r" = (\d+) / (\d+) := by simp \[" + fn + ", " + lit + r"\]$", code, re.M)
        if not mm: problems.append(f"parameter fact {lit}_{f} missing or altered"); continue
        facts[f] = (int(mm.group(1)), int(mm.group(2)))
    for f, v in (("t0", t0), ("y0", y0), ("yA", yA)):
        if f in facts and facts[f] != v: problems.append(f"parameter fact {f} = {facts[f]} ≠ literal {v}")
    # 4. the glue lemma: binders, conclusion verbatim, pinned first row, the kernel fact consumed
    g = re.search(r"^theorem " + glue + r"\n(.*?)\n  exact \(div_ne_zero_iff\.mp hg\)\.1$", code, re.M | re.S)
    if not g:
        problems.append(f"glue lemma {glue} missing or its closing line altered")
    else:
        gb = g.group(1)
        for h, P in (("hAsym", "AsymEnclOK"), ("hTail", "TailOK")):
            if f"({h} : {P} (fun z => Ht (93 / 500) z / Bt (93 / 500) z) {lit})" not in gb:
                problems.append(f"glue binder {h} missing or altered")
        if ("    " + HLANEA_CONCLUSION + " := by") not in gb:
            problems.append("glue conclusion is not character for character the former hLaneA type")
        pin = re.search(r"cert_of_checkAsym _ " + lit + " " + lit + r"_check hAsym hTail x y\n    ⟨([^⟩]*)⟩ \(by simp \[" + lit + r"\]\)", gb)
        if not pin: problems.append("glue: cert_of_checkAsym application (literal, kernel fact, pinned row) missing or altered")
        else:
            pinned = tuple(int(x.strip()) for x in pin.group(1).split(","))
            if pinned != rows[0]: problems.append(f"glue: pinned first row {pinned} ≠ literal's first row {rows[0]}")
        for step in (f"(by rw [{lit}_t0]; exact row2_windowIdx_ge x hx)", f"(by rw [{lit}_y0]; exact hy0)", f"(by rw [{lit}_yA]; exact hyA)"):
            if step not in gb: problems.append(f"glue step missing: {step}")
    # 5. trust words outside comments
    for w in TRUST_WORDS:
        for mm in re.finditer(r"(?<![A-Za-z0-9_])" + w + r"(?![A-Za-z0-9_])", code):
            problems.append(f"trust word `{w}` in code (outside comments) at offset {mm.start()}")
    return {"K": K, "t0": t0, "y0": y0, "yA": yA, "rows": rows, "tail": tail}, problems, src

def load_json(path):
    d = json.load(open(path))
    return {"K": int(d["scales"]["K"]), "t0": (int(d["t0"]["n"]), int(d["t0"]["d"])),
            "y0": (int(d["y0"]["n"]), int(d["y0"]["d"])), "yA": (int(d["yA"]["n"]), int(d["yA"]["d"])),
            "rows": [tuple(int(r[k]) for k in ("Nlo", "Nhi", "T", "E")) for r in d["rows"]],
            "tail": tuple(int(d["tail"][k]) for k in ("N1", "Q1", "Q2", "Q3", "Q4", "E1"))}

def compare_leg(L, J, prefix):
    mism = 0; n = 0
    for k in ("K", "t0", "y0", "yA"):
        n += 1 if k == "K" else 2
        if L[k] != J[k]: mism += 1; print(f"  MISMATCH {prefix} {k}: lean {L[k]} vs json {J[k]}")
    if len(L["rows"]) != len(J["rows"]):
        mism += 1; print(f"  MISMATCH {prefix} row count: lean {len(L['rows'])} vs json {len(J['rows'])}")
    for i, (lr, jr) in enumerate(zip(L["rows"], J["rows"])):
        for k, a, b in zip(("Nlo", "Nhi", "T", "E"), lr, jr):
            n += 1
            if a != b: mism += 1; print(f"  MISMATCH {prefix} row {i} {k}: lean {a} vs json {b}")
    for k, a, b in zip(("N1", "Q1", "Q2", "Q3", "Q4", "E1"), L["tail"], J["tail"]):
        n += 1
        if a != b: mism += 1; print(f"  MISMATCH {prefix} tail {k}: lean {a} vs json {b}")
    return mism, n

def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b)) if max(abs(a), abs(b)) else Fraction(0)

def main():
    root, jmp, jarb = sys.argv[1:4]
    d = os.path.join(root, "Zeta23", "DBN", "Instance02")
    total = 0; ints = 0; legs = {}
    for prefix, jp in (("mp", jmp), ("arb", jarb)):
        path = os.path.join(d, f"Asym_{prefix}.lean")
        L, problems, src = parse_module(path, prefix)
        J = load_json(jp)
        print(f"[{prefix}] {path} ({len(src)} bytes) vs {jp}")
        mism, n = compare_leg(L, J, prefix)
        for p in problems: print(f"  PROBLEM {prefix}: {p}")
        mism += len(problems); total += mism; ints += n
        print(f"  {n} integers compared, {mism} mismatches/problems; K = {L['K']}, rows {len(L['rows'])}, N ∈ [{L['rows'][0][0]}, {L['rows'][-1][1]}], N1 = {L['tail'][0]}")
        legs[prefix] = L
    # cross-leg (where the legs must agree; the legs are never merged)
    A, B = legs["mp"], legs["arb"]
    print("[cross-leg] mp vs arb, on the back-parsed literals:")
    xm = 0
    if len(A["rows"]) != len(B["rows"]):
        xm += 1; print(f"  MISMATCH row counts {len(A['rows'])} vs {len(B['rows'])}")
    for k in ("t0", "y0", "yA"):
        if A[k] != B[k]: xm += 1; print(f"  MISMATCH {k}: {A[k]} vs {B[k]}")
    for i, (ra, rb) in enumerate(zip(A["rows"], B["rows"])):
        if ra[:2] != rb[:2]: xm += 1; print(f"  MISMATCH row {i} window range {ra[:2]} vs {rb[:2]}")
        tA, tB = Fraction(ra[2], A["K"]), Fraction(rb[2], B["K"])
        rT = rel(tA, tB)
        if rT > Fraction(1, 10 ** 9): xm += 1; print(f"  MISMATCH row {i} T/K: mp {float(tA):.12g} vs arb {float(tB):.12g} (rel {float(rT):.2e} > 1e-9)")
        eA, eB = Fraction(ra[3], A["K"]), Fraction(rb[3], B["K"])
        print(f"  row {i} [{ra[0]}, {ra[1]}]: T/K rel diff {float(rT):.2e} (OK ≤ 1e-9); E/K mp {float(eA):.4e} arb {float(eB):.4e}, Arb/mp = {float(eB / eA):.4f} (hull bound, recorded, not gated)")
    if A["tail"][0] != B["tail"][0]: xm += 1; print(f"  MISMATCH N1 {A['tail'][0]} vs {B['tail'][0]}")
    for j, k in enumerate(("Q1", "Q2", "Q3", "Q4"), start=1):
        qA, qB = Fraction(A["tail"][j], A["K"]), Fraction(B["tail"][j], B["K"])
        rQ = rel(qA, qB)
        if rQ > Fraction(1, 10 ** 9): xm += 1; print(f"  MISMATCH tail {k}: rel {float(rQ):.2e} > 1e-9")
        print(f"  tail {k}/K rel diff {float(rQ):.2e} (OK ≤ 1e-9)")
    e1A, e1B = Fraction(A["tail"][5], A["K"]), Fraction(B["tail"][5], B["K"])
    print(f"  tail E1/K mp {float(e1A):.6e} arb {float(e1B):.6e}, Arb/mp = {float(e1B / e1A):.6f} (hull bound, recorded, not gated)")
    sA = Fraction(sum(A["tail"][1:]), A["K"]); sB = Fraction(sum(B["tail"][1:]), B["K"])
    print(f"  tail Σ/K: mp {float(sA):.12f}, arb {float(sB):.12f} (each < 2 is C-A6, kernel-checked per leg, not consumed)")
    total += xm
    print(f"backparse_lane_a: {ints} integers compared exactly (both legs), cross-leg {xm} mismatches; TOTAL {total} mismatches/problems -> {'OK' if total == 0 else 'FAIL'}")
    sys.exit(0 if total == 0 else 1)

if __name__ == "__main__":
    main()
