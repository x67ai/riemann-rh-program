#!/usr/bin/env python3
"""emit_lean_lane_a.py -- UNTRUSTED JSON -> Lean emitter for the M2a LANE A (asymptotic-region) transcripts
(SPEC.md §7.2, §7.4, §8.2; PLAN.md §1.5 and §2.4; the successor of results/d1-m2a/emit_lean_m2a.py for the
`asymptotic` transcript kind).  Session 19, phase 3(d), 2026-09-09.

Writes, for one producer leg's transcript asym-<leg>.json and a Lean name prefix P in {mp, arb}:
  <lean-root>/Zeta23/DBN/Instance02/Asym_<P>.lean
containing
  * `row2Asym<PP> : AsymData`   (PP = P upper-cased: row2AsymMP / row2AsymARB) -- the literal, integers AS WRITTEN
                                in the JSON (K as written; N_start = 630783; N1 = 5141000);
  * `row2Asym<PP>_check : checkAsym row2Asym<PP> = true := by decide +kernel`   -- the kernel fact (C-A1 .. C-A6);
  * `row2Asym<PP>_t0 / _y0 / _yA`   -- the three `simp` facts At0/Ay0/AyA = 93/500, 16733/100000, 3962323/5000000;
  * `row2_laneA_<P>`   -- the glue lemma of PLAN.md §1.5, whose conclusion is character for character the type of
                         the former `hLaneA` binder of Zeta23/DBN/Instance02.lean.
The emitter is UNTRUSTED: its fidelity is established by backparse_lane_a.py (an independent regex back-parse of the
emitted module against the JSON, integer by integer, sharing no code with this file), and everything that matters is
re-checked by the kernel from the literal.  No arithmetic is performed on any emitted number: every integer is the
JSON's decimal string, re-validated as canonical (str(int(s)) == s) and written verbatim.  The float values in the
docstrings are for the reader only (computed from the integers, never emitted into a literal).  Output is
deterministic (the only stamp is the producer's own, copied from the JSON), so the SHA-256 of the module is a
function of the transcript.  Program header: Copyright 2026 Kunal Tyagi, Apache-2.0 (as the other program files).

usage: emit_lean_lane_a.py <asym-<leg>.json> <lean-root> <prefix: mp|arb> [--leg-desc "..."]
"""
import argparse, json, os, re, sys
from fractions import Fraction

HEADER = """/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library; it imports it.
-/
"""

# The instance pins (SPEC §9; Instance02.lean; PLAN §1.5).  The glue lemma's TEXT hardcodes these, so a transcript
# with other parameters must be refused here rather than fail at elaboration.
PIN_T0 = ("93", "500")
PIN_Y0 = ("16733", "100000")
PIN_YA = ("3962323", "5000000")
PIN_NSTART = "630783"        # the first row's Nlo = L-A1's constant in `row2_windowIdx_ge`
PIN_N1 = "5141000"           # the tail row's N1 (PLAN §2.3)
LEG_DESC = {"mp": "mpmath-ball leg", "arb": "Arb/FLINT leg"}

DEC = re.compile(r"^-?(0|[1-9][0-9]*)$")

def as_written(s, what):
    """A JSON integer field, kept as its canonical decimal string (never converted for emission)."""
    if isinstance(s, int): s = str(s)
    if not isinstance(s, str) or not DEC.match(s) or str(int(s)) != s:
        raise SystemExit(f"emit_lean_lane_a: {what} is not a canonical decimal integer string: {s!r}")
    return s

def pow10(s):
    """K displayed as 10^n when it is a power of ten (display only)."""
    if re.fullmatch(r"10*", s):
        n = len(s) - 1
        sup = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
        return "10" + str(n).translate(sup)
    return s

def precheck(K, t0, y0, yA, rows, tail):
    """UNTRUSTED Python pre-check of C-A1 .. C-A6 (the kernel re-does it from the literal).  Fail loud, never emit."""
    K_, t0n, t0d, y0n, y0d, yAn, yAd = (int(K), int(t0[0]), int(t0[1]), int(y0[0]), int(y0[1]), int(yA[0]), int(yA[1]))
    ca1 = (1 <= K_ and 1 <= t0d and 0 < t0n and 1 <= y0d and 0 < y0n and 1 <= yAd and 0 <= yAn
           and (t0d - 2 * t0n) * yAd ** 2 <= yAn ** 2 * t0d)
    ca2 = len(rows) > 0
    ca3 = all(int(r[0]) <= int(r[1]) and 0 <= int(r[3]) < int(r[2]) for r in rows)
    ca4 = all(int(rows[i + 1][0]) == int(rows[i][1]) + 1 for i in range(len(rows) - 1))
    ca5 = int(tail[0]) == int(rows[-1][1]) + 1
    ca6 = all(0 <= int(q) for q in tail[1:]) and sum(int(q) for q in tail[1:]) < 2 * K_
    checks = {"C-A1": ca1, "C-A2": ca2, "C-A3": ca3, "C-A4": ca4, "C-A5": ca5, "C-A6": ca6}
    bad = [k for k, v in checks.items() if not v]
    if bad:
        raise SystemExit(f"emit_lean_lane_a: the transcript fails the UNTRUSTED pre-check on {bad}; nothing emitted")
    return checks

def emit(json_path, root, prefix, leg_desc):
    d = json.load(open(json_path))
    if d.get("kind") != "asymptotic" or d.get("format") != "M2a-barrier-transcript":
        raise SystemExit(f"emit_lean_lane_a: not an asymptotic M2a transcript: kind={d.get('kind')!r} format={d.get('format')!r}")
    K = as_written(d["scales"]["K"], "K")
    t0 = (as_written(d["t0"]["n"], "t0.n"), as_written(d["t0"]["d"], "t0.d"))
    y0 = (as_written(d["y0"]["n"], "y0.n"), as_written(d["y0"]["d"], "y0.d"))
    yA = (as_written(d["yA"]["n"], "yA.n"), as_written(d["yA"]["d"], "yA.d"))
    rows = [tuple(as_written(r[k], f"rows[{i}].{k}") for k in ("Nlo", "Nhi", "T", "E")) for i, r in enumerate(d["rows"])]
    tail = tuple(as_written(d["tail"][k], f"tail.{k}") for k in ("N1", "Q1", "Q2", "Q3", "Q4", "E1"))
    # instance pins (the glue lemma's text depends on them)
    for name, got, want in (("t0", t0, PIN_T0), ("y0", y0, PIN_Y0), ("yA", yA, PIN_YA)):
        if got != want:
            raise SystemExit(f"emit_lean_lane_a: {name} = {got[0]}/{got[1]} is not the instance's {want[0]}/{want[1]}; nothing emitted")
    if rows[0][0] != PIN_NSTART:
        raise SystemExit(f"emit_lean_lane_a: first row Nlo = {rows[0][0]} ≠ N_start {PIN_NSTART} (L-A1's constant); nothing emitted")
    if tail[0] != PIN_N1:
        raise SystemExit(f"emit_lean_lane_a: tail N1 = {tail[0]} ≠ {PIN_N1} (PLAN §2.3); nothing emitted")
    checks = precheck(K, t0, y0, yA, rows, tail)
    prod = d.get("producer", {})
    stamp = prod.get("stamp", "?"); prec = prod.get("prec", "?"); Nc = prod.get("Nc", "?"); mpan = prod.get("m", "?")
    leg_src = prod.get("leg", "?")

    PP = prefix.upper()
    lit = f"row2Asym{PP}"
    glue = f"row2_laneA_{prefix}"
    other = {"mp": ("arb", "Asym_arb.lean", "Arb/FLINT leg's (K = 10¹²)"), "arb": ("mp", "Asym_mp.lean", "mpmath-ball leg's (K = 10²⁴)")}[prefix]
    Kf = Fraction(int(K))
    # display-only floats (from the integers; never emitted into a literal)
    def f7(n): return f"{float(Fraction(int(n)) / Kf):.7g}"
    def e3(n): return f"{float(Fraction(int(n)) / Kf):.3e}"
    nwin = int(rows[-1][1]) - int(rows[0][0]) + 1
    tsum = sum(int(q) for q in tail[1:])
    margin = float((2 * Kf - tsum) / Kf)
    row_lines = "\n".join(f"  row {i}: N ∈ [{r[0]}, {r[1]}] ({int(r[1]) - int(r[0]) + 1} windows), T/K ≈ {f7(r[2])}, E/K ≈ {e3(r[3])} (E/T ≈ {float(Fraction(int(r[3])) / int(r[2])):.2e})"
                          for i, r in enumerate(rows))
    doc = HEADER + f"""/-
Zeta23/DBN/Instance02/Asym_{prefix}.lean — the LANE A (asymptotic-region, final time t₀) literal of the {leg_desc}
of the Instance02 certificate for Polymath15 Table 1 row 2 (X = 5 000 000 194 858, t₀ = 93/500, y₀ = 16733/100000;
SPEC.md §5, §9; the stream plan results/d1-m2a/lane-a/PLAN.md), as an `AsymData` literal `{lit}` with its
kernel fact `{lit}_check : checkAsym {lit} = true` (`decide +kernel`; no `native_decide`), the three real-parameter
facts `{lit}_t0` / `_y0` / `_yA`, and the glue lemma `{glue}` (PLAN.md §1.5) that turns `cert_of_checkAsym`
on the literal into exactly the statement hypothesis (ii′) of `Polymath15Bridge'` consumes in Instance02.lean.

TRANSCRIPT (results/d1-m2a/lane-a/asym-{prefix}.json; producer {leg_src}, prec {prec}, N_c {Nc}, m {mpan} panels;
producer stamp {stamp}; UNTRUSTED).  K = {pow10(K)}; t₀ = {t0[0]}/{t0[1]}; y₀ = {y0[0]}/{y0[1]}; yA = {yA[0]}/{yA[1]};
{len(rows)} window rows covering N ∈ [{rows[0][0]}, {rows[-1][1]}] consecutively ({nwin} windows); tail row at N₁ = {tail[0]}:
{row_lines}
  tail: Q₁ + Q₂ + Q₃ + Q₄ + E₁ = {tsum} < 2K, i.e. Σ/K ≈ {float(tsum / Kf):.10f} (margin (2K − Σ)/K ≈ {margin:.3e});
  Q₁/K ≈ {f7(tail[1])}, Q₂/K ≈ {f7(tail[2])}, Q₃/K ≈ {f7(tail[3])}, Q₄/K ≈ {f7(tail[4])}, E₁/K ≈ {e3(tail[5])}.
Every integer is the JSON's decimal string written verbatim (floors ⌊K·lower⌋ for T, ceilings ⌈K·upper⌉ for E, Q, E₁,
taken on exact rationals by the producer; nothing here is computed).  Mechanically emitted by the UNTRUSTED
results/d1-m2a/lane-a/emit_lean_lane_a.py and back-parse-verified against the JSON, integer by integer, by
backparse_lane_a.py (results/d1-m2a/lane-a/backparse.log).

WHAT THE KERNEL CHECKS HERE (integers only; SPEC.md §7.4): C-A1 (K ≥ 1, denominators ≥ 1, t₀ > 0, y₀ > 0, yA ≥ 0,
yA² ≥ 1 − 2t₀ cross-multiplied), C-A2 (a nonempty row list), C-A3 (per row Nlo ≤ Nhi and 0 ≤ E < T), C-A4
(consecutive rows), C-A5 (N₁ = last Nhi + 1), C-A6 (Q₁ … Q₄, E₁ ≥ 0 and Q₁ + Q₂ + Q₃ + Q₄ + E₁ < 2K).  Nothing
analytic is asserted here: H2-A (`AsymEnclOK`, the window-row floors ‖g(x + iy)‖ ≥ (T − E)/K for N(x) ∈ [Nlo, Nhi],
y ∈ [y₀, yA]) and H-TAIL (`TailOK`, g(x + iy) ≠ 0 for N(x) ≥ N₁, y ∈ [y₀, yA]) stay DISPLAYED (SPEC.md §6, §8.1).

WHAT THE KERNEL DOES NOT USE (PLAN-REVIEW.md F-6; SPEC §5.1).  `cert_of_checkAsym` consumes only K ≥ 1, C-A3, C-A4
and C-A5.  C-A2, C-A6 (the tail row's Σ < 2K) and C-A1's yA² ≥ 1 − 2t₀ are kernel-checked on this literal but
never consumed by any proof: they are recorded evidence for the prose discharge of Lemma T (SPEC §5.4) and of the
y-band condition.  "C-A6 is kernel-checked" must not be read as "the tail reduction is kernel-checked".

THE GLUE (PLAN.md §1.5) AND WHAT IT BUYS (PLAN-REVIEW.md §6).  `{glue} hAsym hTail` has the conclusion
∀ x y, X + 1 ≤ x → y₀ ≤ y → y² ≤ 1 − 2t₀ → Ht t₀ (x + y·I) ≠ 0 — character for character the former `hLaneA`
binder of Instance02.lean — from `cert_of_checkAsym` on this literal, L-A1 (`row2_windowIdx_ge`: x ≥ X + 1 ⟹
N(x) ≥ 630783 = the first row's Nlo) and y ≤ yA from y² ≤ 157/250 < yA² (yA² − 157/250 = 3556329/(25·10¹²)).
Before the replacement the whole region x ≥ X + 1 was a DISPLAYED nonvanishing claim; now the window range
N ∈ [630783, 5140999] (x from ≈ 5.0·10¹² up to x_{{N₁}} ≈ 3.32·10¹⁴) is a displayed FLOOR ENCLOSURE (`AsymEnclOK`)
plus the kernel-checked coverage argument (C-A3, C-A4, C-A5 + L-A1 + L-A2), and the displayed nonvanishing
CONCLUSION that remains is `TailOK` only: N(x) ≥ 5 141 000, i.e. x ≳ 3.32·10¹⁴, on the y-band [y₀, yA].  One
asymmetry, stated not glossed: yA = 0.7924646 is 1.5·10⁻⁷ WIDER than the conclusion's y ≤ √(157/250) = 0.79246451…,
so `TailOK` (and `AsymEnclOK`) are hypotheses on the y-band [y₀, yA], a hair wider than the conclusion's y-range —
"the tail region N ≥ N₁, y ∈ [y₀, yA]", not "part of what `hLaneA` said".

The two producer legs are never merged (D-R3): this module is the {leg_desc}'s; {other[1]} is the {other[2]}, and each
leg pairs its own Lane A literal with its own Lane B literal in Instance02.lean.  The two-producer cross-check
(results/d1-m2a/lane-a/crosscheck-full.txt, CONSISTENT: T_lo and Q₁ … Q₄ agree to ≤ 5·10⁻⁷⁹ relative; the E upper
bounds are hull bounds, Arb's the larger on every row, Arb/mp = 1.027, 1.124, 1.261 on rows 0–2 and 1.000000 on E₁,
recorded not gated, etol 0.3) is producer-side evidence, not a proof.
Trust label (SPEC.md §3.7): "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3" — never "fully machine-checked".
-/
import Zeta23.DBN.Asym

open Complex (I)

namespace Zeta23
namespace DBN
namespace Instance02

/-- the {leg_desc}'s Lane A transcript (asym-{prefix}.json, producer stamp {stamp}), integers as written:
K = {pow10(K)}, t₀ = {t0[0]}/{t0[1]}, y₀ = {y0[0]}/{y0[1]}, yA = {yA[0]}/{yA[1]}; rows ⟨Nlo, Nhi, T, E⟩ with
T/K ≈ {", ".join(f7(r[2]) for r in rows)}; tail ⟨N₁, Q₁, Q₂, Q₃, Q₄, E₁⟩ with Σ/K ≈ {float(tsum / Kf):.10f} < 2. -/
def {lit} : AsymData :=
  {{ K := {K},
    t0n := {t0[0]},
    t0d := {t0[1]},
    y0n := {y0[0]},
    y0d := {y0[1]},
    yAn := {yA[0]},
    yAd := {yA[1]},
    rows := [
"""
    body = [doc]
    for i, r in enumerate(rows):
        sep = "," if i < len(rows) - 1 else "],"
        body.append(f"      ⟨{r[0]}, {r[1]}, {r[2]}, {r[3]}⟩{sep}\n")
    body.append(f"    tail := ⟨{tail[0]}, {tail[1]}, {tail[2]}, {tail[3]}, {tail[4]}, {tail[5]}⟩ }}\n\n")
    body.append(f"""/-- kernel fact: C-A1 … C-A6 (SPEC.md §7.4) hold for the literal — integer relations only, `decide +kernel`. -/
theorem {lit}_check : checkAsym {lit} = true := by decide +kernel

/-- the transcript's t₀, y₀, yA as reals are the instance parameters (SPEC.md §9), exactly. -/
theorem {lit}_t0 : At0 {lit} = {t0[0]} / {t0[1]} := by simp [At0, {lit}]
theorem {lit}_y0 : Ay0 {lit} = {y0[0]} / {y0[1]} := by simp [Ay0, {lit}]
theorem {lit}_yA : AyA {lit} = {yA[0]} / {yA[1]} := by simp [AyA, {lit}]

/-- **The glue (PLAN.md §1.5), {leg_desc}.**  From the DISPLAYED H2-A (`hAsym`, the window-row floors) and H-TAIL
(`hTail`) for g = Ht t₀ / Bt t₀ on this literal: hypothesis (ii′) of `Polymath15Bridge'` at row 2, character for
character the former `hLaneA` — `cert_of_checkAsym` on the kernel fact `{lit}_check`, applied at the first row
(Nlo = 630783 = L-A1's constant, `row2_windowIdx_ge`), with y ≤ yA from y² ≤ 157/250 < yA²; Ht ≠ 0 from Ht/Bt ≠ 0 is
`div_ne_zero_iff`.  Kernel-checked modulo `hAsym` and `hTail` (producers untrusted). -/
theorem {glue}
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) {lit})
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) {lit}) :
    ∀ x y : ℝ, 5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y →
      y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (x + y * I) ≠ 0 := by
  intro x y hx hy0 hy2
  have hyA : y ≤ 3962323 / 5000000 := by
    apply le_of_sq_le_sq _ (by norm_num)
    nlinarith
  have hg := cert_of_checkAsym _ {lit} {lit}_check hAsym hTail x y
    ⟨{rows[0][0]}, {rows[0][1]}, {rows[0][2]}, {rows[0][3]}⟩ (by simp [{lit}])
    (by rw [{lit}_t0]; exact row2_windowIdx_ge x hx)
    (by rw [{lit}_y0]; exact hy0) (by rw [{lit}_yA]; exact hyA)
  exact (div_ne_zero_iff.mp hg).1

end Instance02
end DBN
end Zeta23
""")
    path = os.path.join(root, "Zeta23", "DBN", "Instance02", f"Asym_{prefix}.lean")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = "".join(body)
    with open(path, "w", encoding="utf-8") as fh: fh.write(text)
    return path, checks, len(rows), nwin

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json_path"); ap.add_argument("root"); ap.add_argument("prefix", choices=("mp", "arb"))
    ap.add_argument("--leg-desc", default="")
    a = ap.parse_args()
    leg_desc = a.leg_desc or LEG_DESC[a.prefix]
    path, checks, nrows, nwin = emit(a.json_path, a.root, a.prefix, leg_desc)
    print(f"emitted {path}: {nrows} rows + tail ({nwin} windows); UNTRUSTED Python pre-check C-A1..C-A6 = {list(checks.values())} (the kernel re-does it)")

if __name__ == "__main__":
    main()
