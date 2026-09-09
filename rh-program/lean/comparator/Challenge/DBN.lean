/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does NOT import it: its imports are Mathlib-only.
-/
/-
comparator/Challenge/DBN.lean — CHALLENGE: the de Bruijn–Newman milestone M2a (Λ ≤ 0.2 in RAY FORM, modulo displayed
hypotheses).  Trusted vocabulary: ChallengeDeps.DBN (the nine definitions of the trusted layer, the W1 vocabulary, the
barrier and asymptotic lanes' data, checkers and enclosure Props) and ChallengeDeps.DBN.Instance02 (the instance
literals of Polymath15 Table 1 row 2), both over Mathlib alone.  Solution/DBN.lean (untrusted) proves exactly these
statements by delegating to the Zeta23 library; github.com/leanprover/comparator checks statement equality, that only
the axioms propext, Classical.choice, Quot.sound are used, and replays the proofs through the kernel.

WHAT IS CLAIMED, and what is NOT.  Every statement below has the shape "IF the displayed hypotheses hold THEN every
zero of H_t is real for all t ≥ 1/5" — the ray form of the de Bruijn–Newman bound Λ ≤ 0.2 (the constant Λ is never
defined; design note §1.2).  Λ ≤ 0.2 is NOT proved: the bracket of record stays 0 ≤ Λ ≤ 0.2 on the literature.
The honest label (SPEC §3.7), verbatim: "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3" — never "fully
machine-checked" — with SPEC §3.7's gloss: (H1) a producer-certified zero verification, `ZeroVerification
(116733/200000) 2500000097429`, discharged by Platt–Trudgian Theorem 1; (H2) producer-certified enclosures — the
barrier prisms (H2-B, `BarrierEnclOK`), the final-time window rows (H2-A, `AsymEnclOK`) and the tail (H-TAIL, `TailOK`),
from two independent producers, behind the kernel-checked checkers `checkBarrier` and `checkAsym`; (H3) the Polymath15
analytic package — Theorem 1.2 in the form `Polymath15Bridge'` and the entirety of H_t (`HtEntire`) — as hypotheses.
The count is three named hypotheses with H2 a conjunction of three enclosure-type Props.  The producers are UNTRUSTED;
their numbers enter only through the displayed hypotheses over the literals of ChallengeDeps/DBN/Instance02.lean.

What the window range means (PLAN-REVIEW §6 / EMIT-NOTES §4, stated not glossed): on N ∈ [630783, 5140999] (x from
≈ 5.0·10¹² up to x_{N₁} ≈ 3.32·10¹⁴) what is displayed is a FLOOR ENCLOSURE (`AsymEnclOK`: ‖g‖ ≥ (T − E)/K per window
row), and the step from those floors to nonvanishing on the whole range is the kernel-checked coverage argument
(C-A3, C-A4, C-A5 + L-A1 + L-A2 inside Zeta23's `cert_of_checkAsym`); the only displayed nonvanishing CONCLUSION is
`TailOK` on N(x) ≥ 5 141 000 with the y-band [y₀, yA], yA = 3962323/5000000 = 0.7924646 being 9.0·10⁻⁸ wider than
√(157/250) = 0.79246451… (yA − √(157/250) = 8.975·10⁻⁸; 1.42·10⁻⁷ in the squares); C-A6 (the tail row's
Q₁ + Q₂ + Q₃ + Q₄ + E₁ < 2K) is kernel-checked on each literal but not consumed by any proof — Lemma T's reduction
(SPEC §5.4) is prose.

Three kinds of statement (root namespace, descriptive names):
  (G) `dbn_ray_le_point2_of_certificates` — the GENERIC soundness statement, literal-free: for ANY barrier data `d` the
      checker accepts, on the instance's rectangle and final time, and ANY asymptotic data `a` the checker accepts, with
      the instance's t₀, y₀, yA and a row starting at or below N_start = 630783, the five hypotheses imply the ray
      conclusion.  Zeta23 proves only the instance form; the solution derives this from Zeta23's `cert_of_checkBarrier_xy`,
      `cert_of_checkAsym`, L-A1, L-B3 and the glue arithmetic (a new lemma on the solution side; BUILD-NOTES §1.4).
  (I) `dbn_ray_le_point2_mp`, `dbn_ray_le_point2_arb` — the INSTANCE statements: exactly the referee's statement of
      Zeta23/DBN/Instance02.lean's `lambda_le_point2` / `lambda_le_point2_arb`, the five displayed hypotheses verbatim,
      over the trusted copies of the literals (one theorem per producer leg; the legs are never merged, D-R3).
  (K) `dbn_row2BarrierMP_checked`, `dbn_row2BarrierARB_checked`, `dbn_row2AsymMP_checked`, `dbn_row2AsymARB_checked` —
      the kernel facts: the copied literals pass the copied integer checkers (C-B0…C-B13 per prism and chain; C-A1…C-A6).
      Integer facts only; nothing analytic.

The `sorry`s below are deliberate (this is the challenge side); expect "declaration uses 'sorry'" warnings when
building this module.
-/
import ChallengeDeps.DBN
import ChallengeDeps.DBN.Instance02

open DBN

noncomputable section

/-- **(G) Generic soundness of the two-lane certificate at Polymath15 Table 1 row 2.**  For ANY barrier data `d` on the
instance rectangle R = [X, X+1] × [y₀, 1] (X = 5 000 000 194 858, y₀ = 16733/100000) with final time t₀ = 93/500 that the
integer checker `checkBarrier` accepts, and ANY asymptotic data `a` with t₀ = 93/500, y₀ = 16733/100000, yA = 3962323/5000000
and some window row starting at or below N_start = 630783 that `checkAsym` accepts: modulo the displayed hypotheses (H1)
`hH1`, (H2-B) `hEncl`, (H2-A) `hAsym`, (H-TAIL) `hTail`, (H3) `hH3`, every H_t with t ≥ 1/5 has only real zeros — Λ ≤ 0.2 in
ray form.  Label (SPEC §3.7): "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3" — never "fully machine-checked".  The
window range N ∈ [Nlo, …] is a displayed floor enclosure plus kernel-checked coverage; the only displayed nonvanishing
conclusion is `TailOK` on N(x) ≥ N₁ with the y-band [y₀, yA]. -/
theorem dbn_ray_le_point2_of_certificates
    (d : BarrierData) (hx1 : d.rect.x1 = 5000000194858) (hx2 : d.rect.x2 = 5000000194858 + 1)
    (hy1 : d.rect.y1 = 16733 / 100000) (hy2 : d.rect.y2 = 1) (ht0 : t0 d = 93 / 500)
    (hchk : checkBarrier d = true)
    (a : AsymData) (ha0 : At0 a = 93 / 500) (hay0 : Ay0 a = 16733 / 100000)
    (hayA : AyA a = 3962323 / 5000000) (hrow : ∃ r ∈ a.rows, r.Nlo ≤ 630783)
    (hachk : checkAsym a = true)
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) d)
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) a)
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) a)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  sorry

/-- **(I) Λ ≤ 0.2 in ray form, mpmath-ball leg** (the referee's statement of Zeta23's `lambda_le_point2`, over the trusted
copies `row2BarrierMP`, `row2AsymMP` of the mpmath-ball producer's two transcripts).  Every H_t with t ≥ 1/5 has only real
zeros — kernel-checked modulo the displayed hypotheses: (H1) `hH1`, the producer-certified zero verification
`ZeroVerification (116733/200000) 2500000097429` (Platt–Trudgian Theorem 1, prose); (H2-B) `hEncl`, the producer-certified
barrier enclosures for the kernel-checked mpmath-ball transcript (39 prisms, 7 176 rows); (H2-A) `hAsym`, the producer-certified
final-time window-row floors on N ∈ [630783, 5140999] (the step from the floors to nonvanishing there is kernel-checked
coverage); (H-TAIL) `hTail`, nonvanishing for N(x) ≥ N₁ = 5 141 000 on y ∈ [y₀, yA] — the one displayed nonvanishing
CONCLUSION (Lemma T's reduction is prose; C-A6 is kernel-checked evidence, never consumed); (H3) `hH3`, the Polymath15
analytic package `Polymath15Bridge' ∧ HtEntire`.  Label (SPEC §3.7): "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL),
H3" — never "fully machine-checked".  Λ ≤ 0.2 is not proved; the word Λ appears in prose only. -/
theorem dbn_ray_le_point2_mp
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierMP)
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymMP)
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymMP)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  sorry

/-- **(I) Λ ≤ 0.2 in ray form, Arb/FLINT leg** — the same statement from the independent producer's transcripts
(`row2BarrierARB`: 72 prisms, 10 771 rows; `row2AsymARB`), the referee's statement of Zeta23's `lambda_le_point2_arb`.
The two legs are two theorems, never merged (D-R3).  Label (SPEC §3.7): "kernel-checked modulo H1, H2 (H2-B, H2-A,
H-TAIL), H3" — never "fully machine-checked". -/
theorem dbn_ray_le_point2_arb
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierARB)
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymARB)
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymARB)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  sorry

/-- **(K) The mpmath-ball barrier transcript passes the integer checker** (C-B0…C-B13 for the chain and all 39 prisms).
An integer fact about the literal; nothing analytic — H2-B stays displayed. -/
theorem dbn_row2BarrierMP_checked : checkBarrier row2BarrierMP = true := by
  sorry

/-- **(K) The Arb/FLINT barrier transcript passes the integer checker** (all 72 prisms).  Integer fact only. -/
theorem dbn_row2BarrierARB_checked : checkBarrier row2BarrierARB = true := by
  sorry

/-- **(K) The mpmath-ball Lane A transcript passes the integer checker** (C-A1…C-A6).  Integer fact only; C-A6 is
checked here but consumed by no proof (the tail reduction is prose). -/
theorem dbn_row2AsymMP_checked : checkAsym row2AsymMP = true := by
  sorry

/-- **(K) The Arb/FLINT Lane A transcript passes the integer checker** (C-A1…C-A6).  Integer fact only. -/
theorem dbn_row2AsymARB_checked : checkAsym row2AsymARB = true := by
  sorry

end
