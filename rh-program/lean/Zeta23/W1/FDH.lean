/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library; it imports it.
-/
/-
Zeta23/W1/FDH.lean — D-R8 (2026-09-10, Session 20): the Davenport–Heilbronn function f_DH as a
Lean object, and the W1 checker soundness theorem instantiated on it — `cert_of_checkW1_fDH`, the
twin of `cert_of_checkW1_ap` with `fDH` in place of `riemannZeta` — plus the two live-fire
instance corollaries `mpDH_zero`, `arbDH_zero` on the literals `mpDH`, `arbDH` of `Instances.lean`
(consumed unchanged).  Record: rh-program/results/d1-m2a/dr8/{PRICING-fDH.md, BUILD-BRIEF-fDH.md,
BUILD-NOTES-fDH.md}.  Contract: rh-program/results/d1-m1/FORMAT.md §9.2 (the object, quoted from
results/ccm-dh-test/dh.py lines 5–8, never from memory):

    f_DH(s) = 5^{-s} [ zeta(s,1/5) + kap*zeta(s,2/5) - kap*zeta(s,3/5) - zeta(s,4/5) ]
    kap = (sqrt(10-2*sqrt5) - 2)/(sqrt5 - 1)

(Hurwitz zetas; kap = tan θ with ε_χ = e^{2iθ} = τ(χ)/(i√5), χ mod 5, χ(2) = i.)  κ = 0.28407904…,
reproduced from this file's `kappaDH` against mpmath to 60 digits by three routes
(results/d1-m2a/dr8/kappa-check.log).

WHAT IS PROVED HERE (sorry-free; `#print axioms`: [propext, Classical.choice, Quot.sound]):
  * `differentiable_fDH : Differentiable ℂ fDH` — f_DH is ENTIRE: the poles of the four Hurwitz
    zetas at s = 1 cancel pairwise (coefficients 1 + κ − κ − 1 = 0), Mathlib's
    `differentiable_hurwitzZeta_sub_hurwitzZeta` off the shelf; 5^{−s} by `Differentiable.const_cpow`.
  * `cert_of_checkW1_fDH` — the W1 soundness theorem for f_DH, modulo the single displayed
    hypothesis H-ENCL_DH (`W1EnclOK fDH d`): the generic `cert_of_checkW1_of_diffOn`
    (Soundness.lean, D-R8) at f = fDH with H-AP supplied by `rectArgPrinciple_of_local fDH` (v1.1,
    proved for every f).  Same shape and same trust boundary as the ζ theorem `cert_of_checkW1_ap`.
  * `mpDH_zero`, `arbDH_zero` — the live-fire instances: from `mpDH_check` / `arbDH_check`
    (kernel-decided integer facts, Instances.lean) and H-ENCL_DH for the literal, a zero ρ of f_DH
    with 1/2 < Re ρ < 1 and 85.69 < Im ρ < 85.71.
  * [Session 21, 2026-09-10] `cert_of_checkW1_fDH'`, `mpDH_zero'`, `arbDH_zero'` — the σ-strong
    (box-form) twins: the zero has 4/5 < Re ρ < 41/50 as well; see "σ-STRONG SIBLING" below.

HONEST LABEL (binding; PRICING-fDH.md §3.2, verbatim): "f_DH has at least one zero ρ with 1/2 < Re ρ < 1 and 85.69 < Im ρ < 85.71 (the live-fire window; the
transcript's rectangle is R = [4/5, 41/50] × [85.69, 85.71]) — kernel-checked modulo the displayed
hypothesis H-ENCL_DH (the two producers' enclosures of f_DH on ∂R are true; producers untrusted)."
What it does NOT say, and must never be read as: nothing about ζ (no zero of ζ, nothing about RH,
no change to any ζ transcript's label); nothing about Λ (the de Bruijn–Newman chain starts from a
zero of ζ or of H_t, and f_DH is neither); not a machine-checked disproof of "RH for DH" (the
theorem exhibits ONE off-line zero modulo H-ENCL_DH — the witness direction only — and the witness's
truth is the producers'); not "fully machine-checked" (H-ENCL_DH is where mpmath/Arb enter, exactly
as H-ENCL does for ζ); not a Mathlib fact about Davenport–Heilbronn (`fDH`, `kappaDH` and the
identification below are this program's).

σ-STRONG SIBLING (Session 21, 2026-09-10; owed by D-R8 — CHECK-fDH-O.md §12 FIX-FIRST 1,
BUILD-NOTES-fDH.md §7 (a); record results/d1-m2a/dr8/BUILD-NOTES-sigma-strong.md).  The primed
theorems `cert_of_checkW1_fDH'`, `mpDH_zero'`, `arbDH_zero'` (§4 below) are the box-form twins:
from `cert_of_checkW1_of_diffOn'` (Soundness.lean, witness branch keeping `sigma1 d < Re ρ <
sigma2 d`) they place the zero in the OPEN box itself — 4/5 < Re ρ < 41/50 (and, weakened from it,
1/2 < Re ρ < 1), 85.69 < Im ρ < 85.71.  For the primed theorems ONLY, the label is the box form
(PRICING-fDH.md §3.2, verbatim): "f_DH has at least one zero in R = [4/5, 41/50] × [85.69, 85.71]
with Re s > 1/2 — kernel-checked modulo the displayed hypothesis H-ENCL_DH (the two producers'
enclosures of f_DH on ∂R are true; producers untrusted)."  The unprimed theorems keep the
half-strip label above and are unchanged character-for-character; the never-say list applies to
both forms unchanged (nothing about ζ, RH or Λ; not "RH-for-DH disproved"; not "fully
machine-checked").

THE CONVENTION MATCH (META-level, not a Lean theorem; PRICING-fDH.md §1.3; standing order 5).
Three conventions must agree: Mathlib's `hurwitzZeta`, mpmath's `mp.zeta(s, a)`, and Arb's
`acb_hurwitz_zeta` as called by the two producers.  They do, at the API level, on the half-plane
where all three are defined by a series; uniqueness of analytic continuation carries the identity
everywhere else.  Mathlib: `hasSum_hurwitzZeta_of_one_lt_re` — for a ∈ [0, 1] (as a real, cast to
ℝ/ℤ) and Re s > 1, hurwitzZeta a s = Σ_{n ≥ 0} 1/(n + a)^s (the anchor `hasSum_hurwitzZeta_one_fifth`
below).  mpmath leg: results/d1-m1/hurwitz_encl.py STEP 3′ defines the enclosed object as
zeta(s, a) := Σ_{n=0}^∞ (n+a)^{−s} continued by Euler–Maclaurin, with mp.zeta(s, a) the validation
reference; producer_mp.py builds f_DH from hurwitz_ball(s, j/5), j = 1..4.  Arb leg: producer_arb.py
uses acb.zeta(a) = acb_hurwitz_zeta(s, a) = Σ_{n≥0} (n+a)^{−s}.  Same series, same a-normalization
(a = j/5 ∈ (0, 1)).  Consequently the producers' f_DH and this file's `fDH` are the same entire
function; the identification is of exactly the same standing as "mpmath's zeta(s) / Arb's acb_zeta
is Mathlib's riemannZeta" on the ζ leg.  It is where H-ENCL_DH's meaning lives.  Harmless subtlety:
Mathlib assigns `hurwitzZeta a 1` a junk value and `hurwitzZetaEven a 0` a special value; neither
point can lie on or inside a W1 rectangle (½ < σ₁, σ₂ < 1, clause C2), so no transcript row touches
them.  `W1Data` carries no function tag (the JSON `function` field is dropped at the JSON→Lean
boundary): the function enters ONLY through the hypothesis `W1EnclOK f d`, so the instance
corollaries name `fDH` in their statements (risk R4 of the pricing).

Mathlib pinned: 51e6992efd06126df61a496bebf8f49482a4e129 (`HurwitzZeta.hurwitzZeta`,
`differentiable_hurwitzZeta_sub_hurwitzZeta`, `hasSum_hurwitzZeta_of_one_lt_re`).
-/
import Mathlib.NumberTheory.LSeries.HurwitzZeta
import Zeta23.W1.ArgPrincipleBridge
import Zeta23.W1.Instances

open HurwitzZeta

noncomputable section

namespace Zeta23
namespace W1

/-! ## 1. The object (FORMAT.md §9.2, transcribed; κ reproduced in dr8/kappa-check.log) -/

/-- κ = (√(10 − 2√5) − 2)/(√5 − 1), FORMAT.md §9.2 verbatim (= tan θ, ε_χ = e^{2iθ} = τ(χ)/(i√5)).
Both radicands are positive and the denominator is nonzero, so no `Real.sqrt`/division junk
enters; κ = 0.28407904… -/
def kappaDH : ℝ := (Real.sqrt (10 - 2 * Real.sqrt 5) - 2) / (Real.sqrt 5 - 1)

/-- f_DH := 5^{-s}[ζ(s,1/5) + κ ζ(s,2/5) − κ ζ(s,3/5) − ζ(s,4/5)], FORMAT.md §9.2; entire.
`hurwitzZeta a s` is Mathlib's Hurwitz zeta with the shift `a : UnitAddCircle = ℝ/ℤ`; the casts
`((j/5 : ℝ) : UnitAddCircle)` are the probed form (pricing risk R3). -/
def fDH (s : ℂ) : ℂ := (5 : ℂ) ^ (-s) *
  (hurwitzZeta ((1/5 : ℝ) : UnitAddCircle) s + (kappaDH : ℂ) * hurwitzZeta ((2/5 : ℝ) : UnitAddCircle) s
    - (kappaDH : ℂ) * hurwitzZeta ((3/5 : ℝ) : UnitAddCircle) s - hurwitzZeta ((4/5 : ℝ) : UnitAddCircle) s)

/-- f_DH is entire: the poles at s = 1 cancel pairwise (Mathlib
`differentiable_hurwitzZeta_sub_hurwitzZeta`), and 5^{−s} is entire. -/
theorem differentiable_fDH : Differentiable ℂ fDH := by
  have h14 := differentiable_hurwitzZeta_sub_hurwitzZeta ((1/5 : ℝ) : UnitAddCircle) ((4/5 : ℝ) : UnitAddCircle)
  have h23 := differentiable_hurwitzZeta_sub_hurwitzZeta ((2/5 : ℝ) : UnitAddCircle) ((3/5 : ℝ) : UnitAddCircle)
  have hpow : Differentiable ℂ (fun s : ℂ => (5 : ℂ) ^ (-s)) :=
    Differentiable.const_cpow differentiable_neg (Or.inl (by norm_num))
  have hcomb : Differentiable ℂ (fun s : ℂ =>
      (hurwitzZeta ((1/5 : ℝ) : UnitAddCircle) s - hurwitzZeta ((4/5 : ℝ) : UnitAddCircle) s)
        + (kappaDH : ℂ) * (hurwitzZeta ((2/5 : ℝ) : UnitAddCircle) s - hurwitzZeta ((3/5 : ℝ) : UnitAddCircle) s)) :=
    h14.add (h23.const_mul _)
  have : fDH = fun s => (5 : ℂ) ^ (-s) *
      ((hurwitzZeta ((1/5 : ℝ) : UnitAddCircle) s - hurwitzZeta ((4/5 : ℝ) : UnitAddCircle) s)
        + (kappaDH : ℂ) * (hurwitzZeta ((2/5 : ℝ) : UnitAddCircle) s - hurwitzZeta ((3/5 : ℝ) : UnitAddCircle) s)) := by
    funext s; simp only [fDH]; ring
  rw [this]
  exact hpow.mul hcomb

/-- The series convention on Re s > 1 (the producer-convention anchor of the header, shift 1/5;
the other three shifts are the same Mathlib lemma at a = 2/5, 3/5, 4/5): hurwitzZeta a s is
Σ_{n ≥ 0} 1/(n + a)^s — the series `hurwitz_encl.py` (STEP 3′) and Arb's `acb_hurwitz_zeta`
define, so the three f_DH's agree on Re s > 1 and hence everywhere. -/
theorem hasSum_hurwitzZeta_one_fifth {s : ℂ} (hs : 1 < s.re) :
    HasSum (fun n : ℕ ↦ 1 / (n + (1/5 : ℝ) : ℂ) ^ s) (hurwitzZeta ((1/5 : ℝ) : UnitAddCircle) s) :=
  hasSum_hurwitzZeta_of_one_lt_re (by norm_num) hs

/-! ## 2. The theorem: W1 soundness for f_DH, modulo H-ENCL_DH only (PRICING-fDH.md §3.1 shape) -/

/-- **W1 checker soundness for f_DH** (D-R8), the twin of `cert_of_checkW1_ap`: modulo the single
displayed hypothesis H-ENCL_DH (`W1EnclOK fDH d` — the producers' enclosures of f_DH on ∂R are
true), an accepted transcript certifies, for m ≥ 1, a zero ρ of f_DH with 1/2 < Re ρ < 1 and
T₁ < Im ρ < T₂; for m = 0, no zeros of f_DH in the closed rectangle.  H-AP is a theorem for every
f (`rectArgPrinciple_of_local`), and f_DH is entire (`differentiable_fDH`), so nothing else is
assumed.  Honest label: the header's, verbatim; nothing about ζ or Λ follows. -/
theorem cert_of_checkW1_fDH (d : W1Data) (hc : checkW1 d = true) (hEncl : W1EnclOK fDH d) :
    (1 ≤ d.m → ∃ ρ : ℂ, fDH ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1 ∧ T1 d < ρ.im ∧ ρ.im < T2 d)
    ∧ (d.m = 0 → ∀ s ∈ W1Rect d, fDH s ≠ 0) :=
  cert_of_checkW1_of_diffOn fDH differentiable_fDH.differentiableOn d hc hEncl
    (rectArgPrinciple_of_local fDH)

/-- **W1 checker soundness for f_DH, σ-strong form** (Session 21, 2026-09-10): the same theorem
from `cert_of_checkW1_of_diffOn'`, so the witness satisfies `sigma1 d < Re ρ < sigma2 d` — the
zero lies in the open box R° = (σ₁, σ₂) × (T₁, T₂) of the transcript, not only in the half-strip.
Same single displayed hypothesis H-ENCL_DH; `cert_of_checkW1_fDH` is unchanged. -/
theorem cert_of_checkW1_fDH' (d : W1Data) (hc : checkW1 d = true) (hEncl : W1EnclOK fDH d) :
    (1 ≤ d.m → ∃ ρ : ℂ, fDH ρ = 0 ∧ sigma1 d < ρ.re ∧ ρ.re < sigma2 d
        ∧ T1 d < ρ.im ∧ ρ.im < T2 d)
    ∧ (d.m = 0 → ∀ s ∈ W1Rect d, fDH s ≠ 0) :=
  cert_of_checkW1_of_diffOn' fDH differentiable_fDH.differentiableOn d hc hEncl
    (rectArgPrinciple_of_local fDH)

/-! ## 3. The live-fire instances (`mpDH`, `arbDH` of Instances.lean, consumed unchanged) -/

/-- the transcript rationals of the live-fire rectangle, as reals: T₁ = 8569/100 = 85.69. -/
lemma mpDH_T1 : T1 mpDH = 8569 / 100 := by
  show ((8569 : ℤ) : ℝ) / ((100 : ℤ) : ℝ) = 8569 / 100
  norm_num
/-- T₂ = 8571/100 = 85.71 (mp leg). -/
lemma mpDH_T2 : T2 mpDH = 8571 / 100 := by
  show ((8571 : ℤ) : ℝ) / ((100 : ℤ) : ℝ) = 8571 / 100
  norm_num
/-- T₁ = 85.69 (Arb leg; identical rectangle). -/
lemma arbDH_T1 : T1 arbDH = 8569 / 100 := by
  show ((8569 : ℤ) : ℝ) / ((100 : ℤ) : ℝ) = 8569 / 100
  norm_num
/-- T₂ = 85.71 (Arb leg). -/
lemma arbDH_T2 : T2 arbDH = 8571 / 100 := by
  show ((8571 : ℤ) : ℝ) / ((100 : ℤ) : ℝ) = 8571 / 100
  norm_num

/-- **Live fire, mpmath-ball leg.**  From the kernel-decided `mpDH_check` and H-ENCL_DH for the
literal `mpDH` (`w1-mp-dh-livefire.json`, R = [4/5, 41/50] × [85.69, 85.71], m = 1): f_DH has a
zero ρ with 1/2 < Re ρ < 1 and 85.69 < Im ρ < 85.71.  Label: the header's, verbatim. -/
theorem mpDH_zero (hEncl : W1EnclOK fDH mpDH) :
    ∃ ρ : ℂ, fDH ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1 ∧ (8569/100 : ℝ) < ρ.im ∧ ρ.im < 8571/100 := by
  have h := (cert_of_checkW1_fDH mpDH (checkW1Floor_spec mpDH_check).1 hEncl).1 (by decide)
  rw [mpDH_T1, mpDH_T2] at h
  exact h

/-- **Live fire, Arb/FLINT leg.**  The same from `arbDH_check` and H-ENCL_DH for `arbDH`
(`w1-arb-dh-livefire.json`, same rectangle, m = 1).  The two legs are never merged (D-R3). -/
theorem arbDH_zero (hEncl : W1EnclOK fDH arbDH) :
    ∃ ρ : ℂ, fDH ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1 ∧ (8569/100 : ℝ) < ρ.im ∧ ρ.im < 8571/100 := by
  have h := (cert_of_checkW1_fDH arbDH (checkW1Floor_spec arbDH_check).1 hEncl).1 (by decide)
  rw [arbDH_T1, arbDH_T2] at h
  exact h

/-! ## 4. The box-form live-fire instances (Session 21, 2026-09-10; the σ-strong sibling owed by
D-R8).  Label for THIS section only, verbatim (PRICING-fDH.md §3.2): "f_DH has at least one zero
in R = [4/5, 41/50] × [85.69, 85.71] with Re s > 1/2 — kernel-checked modulo the displayed
hypothesis H-ENCL_DH (the two producers' enclosures of f_DH on ∂R are true; producers untrusted)."
The statements carry both the box bounds and the half-strip bounds, so a reader of either label
finds its clause in the statement. -/

/-- the transcript rationals of the live-fire rectangle, as reals: σ₁ = 4/5 (mp leg). -/
lemma mpDH_sigma1 : sigma1 mpDH = 4 / 5 := by
  show ((4 : ℤ) : ℝ) / ((5 : ℤ) : ℝ) = 4 / 5
  norm_num
/-- σ₂ = 41/50 = 0.82 (mp leg). -/
lemma mpDH_sigma2 : sigma2 mpDH = 41 / 50 := by
  show ((41 : ℤ) : ℝ) / ((50 : ℤ) : ℝ) = 41 / 50
  norm_num
/-- σ₁ = 4/5 (Arb leg; identical rectangle). -/
lemma arbDH_sigma1 : sigma1 arbDH = 4 / 5 := by
  show ((4 : ℤ) : ℝ) / ((5 : ℤ) : ℝ) = 4 / 5
  norm_num
/-- σ₂ = 41/50 (Arb leg). -/
lemma arbDH_sigma2 : sigma2 arbDH = 41 / 50 := by
  show ((41 : ℤ) : ℝ) / ((50 : ℤ) : ℝ) = 41 / 50
  norm_num

/-- **Live fire, mpmath-ball leg, box form.**  From the kernel-decided `mpDH_check` and H-ENCL_DH
for the literal `mpDH` (`w1-mp-dh-livefire.json`, R = [4/5, 41/50] × [85.69, 85.71], m = 1):
f_DH has a zero ρ with 4/5 < Re ρ < 41/50 (hence 1/2 < Re ρ < 1) and 85.69 < Im ρ < 85.71.
Label: the §4 box form.  `mpDH_zero` (half-strip form) is unchanged. -/
theorem mpDH_zero' (hEncl : W1EnclOK fDH mpDH) :
    ∃ ρ : ℂ, fDH ρ = 0 ∧ (4/5 : ℝ) < ρ.re ∧ ρ.re < 41/50 ∧ 1/2 < ρ.re ∧ ρ.re < 1
      ∧ (8569/100 : ℝ) < ρ.im ∧ ρ.im < 8571/100 := by
  have h := (cert_of_checkW1_fDH' mpDH (checkW1Floor_spec mpDH_check).1 hEncl).1 (by decide)
  rw [mpDH_sigma1, mpDH_sigma2, mpDH_T1, mpDH_T2] at h
  obtain ⟨ρ, hρ0, hr1, hr2, hi1, hi2⟩ := h
  exact ⟨ρ, hρ0, hr1, hr2, lt_trans (by norm_num) hr1, lt_trans hr2 (by norm_num), hi1, hi2⟩

/-- **Live fire, Arb/FLINT leg, box form.**  The same from `arbDH_check` and H-ENCL_DH for
`arbDH` (`w1-arb-dh-livefire.json`, same rectangle, m = 1).  The two legs are never merged (D-R3).
`arbDH_zero` (half-strip form) is unchanged. -/
theorem arbDH_zero' (hEncl : W1EnclOK fDH arbDH) :
    ∃ ρ : ℂ, fDH ρ = 0 ∧ (4/5 : ℝ) < ρ.re ∧ ρ.re < 41/50 ∧ 1/2 < ρ.re ∧ ρ.re < 1
      ∧ (8569/100 : ℝ) < ρ.im ∧ ρ.im < 8571/100 := by
  have h := (cert_of_checkW1_fDH' arbDH (checkW1Floor_spec arbDH_check).1 hEncl).1 (by decide)
  rw [arbDH_sigma1, arbDH_sigma2, arbDH_T1, arbDH_T2] at h
  obtain ⟨ρ, hρ0, hr1, hr2, hi1, hi2⟩ := h
  exact ⟨ρ, hρ0, hr1, hr2, lt_trans (by norm_num) hr1, lt_trans hr2 (by norm_num), hi1, hi2⟩

end W1
end Zeta23

end
