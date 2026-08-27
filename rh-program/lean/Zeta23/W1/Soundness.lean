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
Zeta23/W1/Soundness.lean — the SOUNDNESS layer of the M1 v1 W1 checker: the two displayed
hypotheses H-ENCL and H-AP as named Props, and the soundness theorem `cert_of_checkW1` turning
`checkW1 d = true` plus the two hypotheses into the analytic conclusion (¬RH witness for m ≥ 1;
zero-free closed rectangle for m = 0).

Binding contract: rh-program/results/d1-m1/FORMAT.md v1.0 (2026-08-26), §6.3 (the soundness
chain), §7.1 (the theorem shape), §8 (the hypothesis boundaries — normative).  Architecture
template: Zeta23/PairCeiling/RowCert.lean (`cert_of_checkRows`) and NumericCert.lean (`EnclOK`);
statement-surface pattern: comparator/ChallengeDeps.lean (definable from Mathlib's `riemannZeta`
plus this file's definitions).

TRUST MODEL (D-R3, binding).  The honest label for any accepted ζ transcript is, verbatim:
"kernel-checked modulo displayed hypotheses H-ENCL and H-AP (producers untrusted)".
  * H-ENCL (`W1EnclOK`, §8.1): the untrusted producers' interval arithmetic enters the trusted
    statement HERE and only here — per segment, (a) the value box encloses K·f on the whole
    closed segment, (b) the argument row encloses A·(Δ/2π), Δ the log-derivative increment
    integral of §6.1.
  * H-AP (`RectArgPrinciple`, §8.2): the rectangle argument principle for the EXACT
    counterclockwise traversal of §4 (bottom, right, top, left — corner order pinned in the
    statement, so an orientation/sign error cannot hide in the checker).  Mathlib 2025-26 ships
    no argument principle (verified, D-R3); this Prop is v1's displayed analytic debt, and its
    discharge (building on WeilEF/Contour.lean + the Mathlib divisor layer) is the named
    milestone v1.1.
  * Dated formulation note (2026-08-26): `RectArgPrinciple` is stated in CONSEQUENCE form —
    ∃ Z : ℕ with (i) the winding identity 2πZ = Σ of the four directed edge increments,
    (ii) Z = 0 → no zeros in the open rectangle, (iii) Z ≥ 1 → a zero in the open rectangle.
    This is implied by §8.2's statement (take Z := the zero count of f in R° with
    multiplicity), so v1.1's discharge obligation is unchanged, and the theorem here assumes
    strictly LESS than the full §8.2 statement.  The multiplicity-counting formalization is
    thereby deferred to v1.1, as FORMAT.md §7.1 explicitly permits.

WHAT IS PROVED HERE (all sorry-free; the Lean-side obligations of FORMAT.md §8.3):
  * L3, checker soundness = `cert_of_checkW1`, via the full §6.3 chain;
  * L1, additivity: the per-segment increments sum to the four directed edge increments
    (`edge_sum_eq` + the affine reparameterization `logDerivSegIntegral_affine`), with the
    integrability input PROVED for ζ (analyticity off s = 1 + checker-certified boundary
    nonvanishing), not assumed — the §8.1 anti-cheat note lands here: junk-value integrals
    cannot arise on the path the theorem actually uses;
  * the D1/D4/D7 derivations (0-exclusion, winding pinning, cross-multiplication soundness);
  * the C11 floor by-product `floor_of_checkW1Floor` (|ζ| ≥ Fn/Fd on ∂R under H-ENCL(a)).
D2/D3 (branch lifting, the C7 clamp's justification) are NOT formalized — per §8.3 the chain
does not use them; C7 stays an unexplained sound reject-more check.

The v1 statement is ζ-SPECIFIC (D-R8): `cert_of_checkW1` mentions `riemannZeta` only; an
accepted f_DH transcript is checker-level only and carries no theorem from this file.
-/
import Mathlib.NumberTheory.LSeries.RiemannZeta
import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.Analysis.Calculus.FDeriv.Analytic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Zeta23.W1.Checker

open scoped Real
open MeasureTheory

noncomputable section

namespace Zeta23
namespace W1

/-! ## 1. The real/complex reading of the transcript data -/

/-- the real value n/d of a transcript rational (n, d). -/
def ratVal (r : ℤ × ℤ) : ℝ := (r.1 : ℝ) / r.2

/-- σ₁ = p1/q1. -/
def sigma1 (d : W1Data) : ℝ := (d.p1 : ℝ) / d.q1
/-- σ₂ = p2/q2. -/
def sigma2 (d : W1Data) : ℝ := (d.p2 : ℝ) / d.q2
/-- T₁ = a1/b1. -/
def T1 (d : W1Data) : ℝ := (d.a1 : ℝ) / d.b1
/-- T₂ = a2/b2. -/
def T2 (d : W1Data) : ℝ := (d.a2 : ℝ) / d.b2

/-- the complex point x + iy. -/
def cpt (x y : ℝ) : ℂ := ⟨x, y⟩

@[simp] lemma cpt_re (x y : ℝ) : (cpt x y).re = x := rfl
@[simp] lemma cpt_im (x y : ℝ) : (cpt x y).im = y := rfl

/-- the closed rectangle [σ₁,σ₂] × [t₁,t₂] ⊂ ℂ. -/
def rectClosed (s₁ s₂ t₁ t₂ : ℝ) : Set ℂ :=
  {s | s₁ ≤ s.re ∧ s.re ≤ s₂ ∧ t₁ ≤ s.im ∧ s.im ≤ t₂}

/-- the open rectangle (σ₁,σ₂) × (t₁,t₂). -/
def rectOpen (s₁ s₂ t₁ t₂ : ℝ) : Set ℂ :=
  {s | s₁ < s.re ∧ s.re < s₂ ∧ t₁ < s.im ∧ s.im < t₂}

/-- the rectangle boundary ∂R (closed minus open; for the nondegenerate rectangles the checker
certifies this is the topological frontier). -/
def rectBdry (s₁ s₂ t₁ t₂ : ℝ) : Set ℂ :=
  rectClosed s₁ s₂ t₁ t₂ \ rectOpen s₁ s₂ t₁ t₂

/-- the transcript's closed rectangle R. -/
def W1Rect (d : W1Data) : Set ℂ := rectClosed (sigma1 d) (sigma2 d) (T1 d) (T2 d)

/-- the transcript's open rectangle R°. -/
def W1RectOpen (d : W1Data) : Set ℂ := rectOpen (sigma1 d) (sigma2 d) (T1 d) (T2 d)

/-- the transcript's boundary ∂R. -/
def W1Bdry (d : W1Data) : Set ℂ := rectBdry (sigma1 d) (sigma2 d) (T1 d) (T2 d)

/-- consecutive pairs of a list: [x₀, x₁, x₂, …] ↦ [(x₀,x₁), (x₁,x₂), …]. -/
def consecPairs {α : Type*} : List α → List (α × α)
  | [] => []
  | [_] => []
  | x :: y :: l => (x, y) :: consecPairs (y :: l)

/-- the point of the directed segment z → w at parameter t ∈ [0,1]. -/
def segPt (z w : ℂ) (t : ℝ) : ℂ := z + (t : ℂ) * (w - z)

/-- bottom-edge breakpoints as complex points (Im = T₁). -/
def bottomPts (d : W1Data) : List ℂ := d.bottom.map fun r => cpt (ratVal r) (T1 d)
/-- right-edge breakpoints (Re = σ₂). -/
def rightPts (d : W1Data) : List ℂ := d.right.map fun r => cpt (sigma2 d) (ratVal r)
/-- top-edge breakpoints (Im = T₂). -/
def topPts (d : W1Data) : List ℂ := d.top.map fun r => cpt (ratVal r) (T2 d)
/-- left-edge breakpoints (Re = σ₁). -/
def leftPts (d : W1Data) : List ℂ := d.left.map fun r => cpt (sigma1 d) (ratVal r)

/-- the boundary segments (endpoint pairs) in global traversal order (FORMAT.md §4):
bottom segments, then right, top, left.  `d.rows` indexes this list. -/
def segs (d : W1Data) : List (ℂ × ℂ) :=
  consecPairs (bottomPts d) ++ consecPairs (rightPts d)
    ++ consecPairs (topPts d) ++ consecPairs (leftPts d)

/-- the log-derivative contour integral along the directed segment z → w (FORMAT.md §6.1):
∫₀¹ (f′/f)(γ(t))·(w−z) dt, γ(t) = z + t(w−z).  (Bochner/interval integral; junk value 0 if the
integrand is not integrable — on the soundness path integrability is PROVED, see the header.) -/
def logDerivSegIntegral (f : ℂ → ℂ) (z w : ℂ) : ℂ :=
  ∫ t in (0:ℝ)..1, (deriv f (segPt z w t) / f (segPt z w t)) * (w - z)

/-- the argument increment Δ along the directed segment z → w: the imaginary part of the
log-derivative integral (FORMAT.md §6.1, derivation D2). -/
def argIncrement (f : ℂ → ℂ) (z w : ℂ) : ℝ := (logDerivSegIntegral f z w).im

/-! ## 2. The two displayed hypotheses (FORMAT.md §8 — exactly two, displayed, never hidden) -/

/-- H-ENCL for one row/segment pair (FORMAT.md §8.1): (a) the value box encloses K·f at EVERY
point of the closed segment; (b) the argument row encloses A·(Δ/2π) (turn units). -/
def RowEnclOK (f : ℂ → ℂ) (K A : ℤ) (row : W1Row) (zw : ℂ × ℂ) : Prop :=
  (∀ t : ℝ, 0 ≤ t → t ≤ 1 →
      ((row.reLo : ℝ) ≤ K * (f (segPt zw.1 zw.2 t)).re
        ∧ (K : ℝ) * (f (segPt zw.1 zw.2 t)).re ≤ row.reHi)
      ∧ ((row.imLo : ℝ) ≤ K * (f (segPt zw.1 zw.2 t)).im
        ∧ (K : ℝ) * (f (segPt zw.1 zw.2 t)).im ≤ row.imHi))
  ∧ ((row.argLo : ℝ) ≤ A * (argIncrement f zw.1 zw.2 / (2 * π))
      ∧ (A : ℝ) * (argIncrement f zw.1 zw.2 / (2 * π)) ≤ row.argHi)

/-- **H-ENCL** (FORMAT.md §8.1), the first displayed hypothesis: every transcript row encloses
the true boundary values and argument increments of f on its segment.  This is where the
untrusted producers enter the trusted statement — the `EnclOK` pattern of NumericCert.lean,
extended from one real sequence to (Re, Im, Δ) per segment. -/
def W1EnclOK (f : ℂ → ℂ) (d : W1Data) : Prop :=
  List.Forall₂ (RowEnclOK f d.K d.A) d.rows (segs d)

/-- **H-AP** (FORMAT.md §8.2), the second displayed hypothesis — the rectangle argument
principle in consequence form (see the header's dated formulation note), stated for the EXACT
§4 traversal: bottom (σ₁+it₁ → σ₂+it₁), right (→ σ₂+it₂), top (→ σ₁+it₂), left (→ σ₁+it₁).
If f is analytic on an open set containing the closed rectangle and nonvanishing on ∂R, some
Z : ℕ satisfies the winding identity and the two counting consequences.  Discharge = v1.1. -/
def RectArgPrinciple (f : ℂ → ℂ) : Prop :=
  ∀ s₁ s₂ t₁ t₂ : ℝ, 1/2 < s₁ → s₁ ≤ s₂ → s₂ < 1 → t₁ < t₂ →
  ∀ U : Set ℂ, IsOpen U → rectClosed s₁ s₂ t₁ t₂ ⊆ U → DifferentiableOn ℂ f U →
    (∀ s ∈ rectBdry s₁ s₂ t₁ t₂, f s ≠ 0) →
    ∃ Z : ℕ,
      2 * π * Z
          = argIncrement f (cpt s₁ t₁) (cpt s₂ t₁) + argIncrement f (cpt s₂ t₁) (cpt s₂ t₂)
            + argIncrement f (cpt s₂ t₂) (cpt s₁ t₂) + argIncrement f (cpt s₁ t₂) (cpt s₁ t₁)
        ∧ (Z = 0 → ∀ s ∈ rectOpen s₁ s₂ t₁ t₂, f s ≠ 0)
        ∧ (1 ≤ Z → ∃ ρ ∈ rectOpen s₁ s₂ t₁ t₂, f ρ = 0)

/-! ## 3. Cross-multiplication soundness (FORMAT.md derivation D7) -/

lemma ratVal_le_of_cross {r s : ℤ × ℤ} (hr : 1 ≤ r.2) (hs : 1 ≤ s.2)
    (h : r.1 * s.2 ≤ s.1 * r.2) : ratVal r ≤ ratVal s := by
  have hr' : (0 : ℝ) < r.2 := by exact_mod_cast hr
  have hs' : (0 : ℝ) < s.2 := by exact_mod_cast hs
  rw [ratVal, ratVal, div_le_div_iff₀ hr' hs']
  exact_mod_cast h

lemma ratVal_lt_of_cross {r s : ℤ × ℤ} (hr : 1 ≤ r.2) (hs : 1 ≤ s.2)
    (h : r.1 * s.2 < s.1 * r.2) : ratVal r < ratVal s := by
  have hr' : (0 : ℝ) < r.2 := by exact_mod_cast hr
  have hs' : (0 : ℝ) < s.2 := by exact_mod_cast hs
  rw [ratVal, ratVal, div_lt_div_iff₀ hr' hs']
  exact_mod_cast h

lemma ratVal_eq_of_cross {r s : ℤ × ℤ} (hr : 1 ≤ r.2) (hs : 1 ≤ s.2)
    (h : r.1 * s.2 = s.1 * r.2) : ratVal r = ratVal s := by
  have hr' : (r.2 : ℝ) ≠ 0 := by
    have : (0 : ℝ) < r.2 := by exact_mod_cast hr
    exact this.ne'
  have hs' : (s.2 : ℝ) ≠ 0 := by
    have : (0 : ℝ) < s.2 := by exact_mod_cast hs
    exact this.ne'
  rw [ratVal, ratVal, div_eq_div_iff hr' hs']
  exact_mod_cast h

/-! ## 4. Unpacking the checker -/

/-- the semantic content of `checkW1 d = true`, one field per checker clause (C1–C10). -/
structure ChecksOK (d : W1Data) : Prop where
  hK : 1 ≤ d.K
  hA : 1 ≤ d.A
  hq1 : 1 ≤ d.q1
  hq2 : 1 ≤ d.q2
  hb1 : 1 ≤ d.b1
  hb2 : 1 ≤ d.b2
  hdb : densPos d.bottom = true
  hdr : densPos d.right = true
  hdt : densPos d.top = true
  hdl : densPos d.left = true
  hC2a : d.q1 < 2 * d.p1
  hC2b : d.p1 * d.q2 ≤ d.p2 * d.q1
  hC2c : d.p2 < d.q2
  hC2d : d.a1 * d.b2 < d.a2 * d.b1
  hEb : edgeOK (d.p1, d.q1) (d.p2, d.q2) true d.bottom = true
  hEr : edgeOK (d.a1, d.b1) (d.a2, d.b2) true d.right = true
  hEt : edgeOK (d.p2, d.q2) (d.p1, d.q1) false d.top = true
  hEl : edgeOK (d.a2, d.b2) (d.a1, d.b1) false d.left = true
  hC4 : d.rows.length + 4 = d.bottom.length + d.right.length + d.top.length + d.left.length
  hRows : rowsOK d.A d.rows = true
  hC8 : 2 * (sumArgHi d.rows - sumArgLo d.rows) < d.A
  hC9a : sumArgLo d.rows ≤ d.A * d.m
  hC9b : d.A * d.m ≤ sumArgHi d.rows
  hC10 : 0 ≤ d.m

lemma checksOK_of_checkW1 {d : W1Data} (hc : checkW1 d = true) : ChecksOK d := by
  simp only [checkW1, Bool.and_eq_true, decide_eq_true_eq] at hc
  obtain ⟨hc, hC10⟩ := hc
  obtain ⟨hc, hC9b⟩ := hc
  obtain ⟨hc, hC9a⟩ := hc
  obtain ⟨hc, hC8⟩ := hc
  obtain ⟨hc, hRows⟩ := hc
  obtain ⟨hc, hC4⟩ := hc
  obtain ⟨hc, hEl⟩ := hc
  obtain ⟨hc, hEt⟩ := hc
  obtain ⟨hc, hEr⟩ := hc
  obtain ⟨hc, hEb⟩ := hc
  obtain ⟨hc, hC2d⟩ := hc
  obtain ⟨hc, hC2c⟩ := hc
  obtain ⟨hc, hC2b⟩ := hc
  obtain ⟨hc, hC2a⟩ := hc
  obtain ⟨hc, hdl⟩ := hc
  obtain ⟨hc, hdt⟩ := hc
  obtain ⟨hc, hdr⟩ := hc
  obtain ⟨hc, hdb⟩ := hc
  obtain ⟨hc, hb2⟩ := hc
  obtain ⟨hc, hb1⟩ := hc
  obtain ⟨hc, hq2⟩ := hc
  obtain ⟨hK, hq1⟩ := hc
  exact ⟨hK.1, hK.2, hq1, hq2, hb1, hb2, hdb, hdr, hdt, hdl, hC2a, hC2b, hC2c, hC2d,
    hEb, hEr, hEt, hEl, hC4, hRows, hC8, hC9a, hC9b, hC10⟩

lemma edgeOK_inc_spec {a b : ℤ × ℤ} {l : List (ℤ × ℤ)} (h : edgeOK a b true l = true) :
    2 ≤ l.length ∧ firstOK a l = true ∧ lastOK b l = true ∧ chainLt l = true := by
  simp only [edgeOK, if_true, Bool.and_eq_true, decide_eq_true_eq] at h
  exact ⟨h.1.1.1, h.1.1.2, h.1.2, h.2⟩

lemma edgeOK_dec_spec {a b : ℤ × ℤ} {l : List (ℤ × ℤ)} (h : edgeOK a b false l = true) :
    2 ≤ l.length ∧ firstOK a l = true ∧ lastOK b l = true ∧ chainGt l = true := by
  simp only [edgeOK, Bool.and_eq_true, decide_eq_true_eq] at h
  exact ⟨h.1.1.1, h.1.1.2, h.1.2, h.2⟩

lemma densPos_cons {r : ℤ × ℤ} {l : List (ℤ × ℤ)} :
    densPos (r :: l) = true ↔ 1 ≤ r.2 ∧ densPos l = true := by
  simp [densPos, Bool.and_eq_true, decide_eq_true_eq]

lemma rowsOK_mem {A : ℤ} : ∀ {l : List W1Row}, rowsOK A l = true → ∀ r ∈ l, rowOK A r = true := by
  intro l
  induction l with
  | nil => intro _ r hr; cases hr
  | cons a l ih =>
    intro h r hr
    simp only [rowsOK, Bool.and_eq_true] at h
    rcases List.mem_cons.mp hr with rfl | hr
    · exact h.1
    · exact ih h.2 r hr

/-- the C6 disjunction of an accepted row, in Prop form. -/
lemma rowOK_C6 {A : ℤ} {r : W1Row} (h : rowOK A r = true) :
    0 < r.reLo ∨ r.reHi < 0 ∨ 0 < r.imLo ∨ r.imHi < 0 := by
  simp only [rowOK, Bool.and_eq_true, Bool.or_eq_true, decide_eq_true_eq] at h
  tauto

/-! ## 5. List bookkeeping: consecutive pairs, chains, covering -/

lemma consecPairs_map {α β : Type*} (g : α → β) :
    ∀ l : List α, consecPairs (l.map g) = (consecPairs l).map fun p => (g p.1, g p.2)
  | [] => rfl
  | [_] => rfl
  | x :: y :: l => by
    simp only [List.map_cons, consecPairs, List.map]
    exact congrArg _ (by simpa using consecPairs_map g (y :: l))

lemma map_congr_fn {α β : Type*} {f g : α → β} (h : ∀ a, f a = g a) (l : List α) :
    l.map f = l.map g := by
  simp [funext h]

/-- the cross-multiplied strict increase check, at the real level, pairwise over the
consecutive pairs of the rational list. -/
lemma chainLt_spec : ∀ {l : List (ℤ × ℤ)}, densPos l = true → chainLt l = true →
    ∀ p ∈ consecPairs l, ratVal p.1 < ratVal p.2 := by
  intro l
  induction l with
  | nil => intro _ _ p hp; cases hp
  | cons r l ih =>
    intro hd hc p hp
    cases l with
    | nil => cases hp
    | cons s l' =>
      obtain ⟨hr2, hd'⟩ := densPos_cons.mp hd
      obtain ⟨hs2, _⟩ := densPos_cons.mp hd'
      simp only [chainLt, Bool.and_eq_true, decide_eq_true_eq] at hc
      rcases List.mem_cons.mp hp with rfl | hp
      · exact ratVal_lt_of_cross hr2 hs2 hc.1
      · exact ih hd' hc.2 p hp

/-- the cross-multiplied strict decrease check, at the real level, pairwise. -/
lemma chainGt_spec : ∀ {l : List (ℤ × ℤ)}, densPos l = true → chainGt l = true →
    ∀ p ∈ consecPairs l, ratVal p.2 < ratVal p.1 := by
  intro l
  induction l with
  | nil => intro _ _ p hp; cases hp
  | cons r l ih =>
    intro hd hc p hp
    cases l with
    | nil => cases hp
    | cons s l' =>
      obtain ⟨hr2, hd'⟩ := densPos_cons.mp hd
      obtain ⟨hs2, _⟩ := densPos_cons.mp hd'
      simp only [chainGt, Bool.and_eq_true, decide_eq_true_eq] at hc
      rcases List.mem_cons.mp hp with rfl | hp
      · exact ratVal_lt_of_cross hs2 hr2 hc.1
      · exact ih hd' hc.2 p hp

lemma firstOK_spec {t : ℤ × ℤ} {l : List (ℤ × ℤ)} (h : firstOK t l = true)
    (hd : densPos l = true) (ht : 1 ≤ t.2) : ∃ r, l.head? = some r ∧ ratVal r = ratVal t := by
  cases l with
  | nil => simp [firstOK] at h
  | cons r rest =>
    simp only [firstOK, ratEqB, decide_eq_true_eq] at h
    obtain ⟨hr2, _⟩ := densPos_cons.mp hd
    exact ⟨r, rfl, ratVal_eq_of_cross hr2 ht h⟩

lemma lastOK_spec {t : ℤ × ℤ} (ht : 1 ≤ t.2) :
    ∀ {l : List (ℤ × ℤ)}, lastOK t l = true → densPos l = true →
      ∃ r, l.getLast? = some r ∧ ratVal r = ratVal t
  | [] => by simp [lastOK]
  | [r] => by
    intro h hd
    simp only [lastOK, ratEqB, decide_eq_true_eq] at h
    obtain ⟨hr2, _⟩ := densPos_cons.mp hd
    exact ⟨r, rfl, ratVal_eq_of_cross hr2 ht h⟩
  | r :: s :: rest => by
    intro h hd
    have h' : lastOK t (s :: rest) = true := h
    have hd' : densPos (s :: rest) = true := (densPos_cons.mp hd).2
    obtain ⟨r', hr', hv⟩ := lastOK_spec ht h' hd'
    exact ⟨r', by simpa [List.getLast?_cons_cons] using hr', hv⟩

/-- the tail's consecutive pairs are among the full list's. -/
lemma consecPairs_tail_subset {α : Type*} (x : α) (l : List α) :
    ∀ p ∈ consecPairs l, p ∈ consecPairs (x :: l) := by
  intro p hp
  cases l with
  | nil => cases hp
  | cons y l' => exact List.mem_cons.mpr (Or.inr hp)

section ValChain

variable {α : Type*} (val : α → ℝ)

/-- head is a lower bound of every element's value, given adjacent-pair monotonicity. -/
lemma head_le_of_consec_le : ∀ {v : List α} {a : α}, v.head? = some a →
    (∀ p ∈ consecPairs v, val p.1 ≤ val p.2) → ∀ x ∈ v, val a ≤ val x := by
  intro v
  induction v with
  | nil => intro a ha; simp at ha
  | cons y l ih =>
    intro a ha hp x hx
    have hya : y = a := by simpa using ha
    subst hya
    rcases List.mem_cons.mp hx with rfl | hx
    · exact le_rfl
    · cases l with
      | nil => cases hx
      | cons z l' =>
        have hyz : val y ≤ val z := hp (y, z) (by simp [consecPairs])
        have := ih (a := z) (by simp) (fun p hp' => hp p (consecPairs_tail_subset _ _ p hp')) x hx
        linarith

/-- last is an upper bound of every element's value, given adjacent-pair monotonicity. -/
lemma getLast_ge_of_consec_le : ∀ {v : List α} {b : α}, v.getLast? = some b →
    (∀ p ∈ consecPairs v, val p.1 ≤ val p.2) → ∀ x ∈ v, val x ≤ val b := by
  intro v
  induction v with
  | nil => intro b hb; simp at hb
  | cons y l ih =>
    intro b hb hp x hx
    cases l with
    | nil =>
      have hyb : y = b := by simpa using hb
      subst hyb
      rcases List.mem_cons.mp hx with rfl | hx
      · exact le_rfl
      · cases hx
    | cons z l' =>
      have hb' : (z :: l').getLast? = some b := by simpa [List.getLast?_cons_cons] using hb
      have htail := ih hb' (fun p hp' => hp p (consecPairs_tail_subset _ _ p hp'))
      have hyz : val y ≤ val z := hp (y, z) (by simp [consecPairs])
      rcases List.mem_cons.mp hx with rfl | hx
      · have := htail z (by simp)
        linarith
      · exact htail x hx

lemma head?_lt_getLast? : ∀ {v : List α} {a b : α}, v.head? = some a → v.getLast? = some b →
    (∀ p ∈ consecPairs v, val p.1 < val p.2) → 2 ≤ v.length → val a < val b := by
  intro v
  induction v with
  | nil => intro a b ha; simp at ha
  | cons y l ih =>
    intro a b ha hb hp h2
    have hya : y = a := by simpa using ha
    subst hya
    cases l with
    | nil => simp at h2
    | cons z l' =>
      have hb' : (z :: l').getLast? = some b := by simpa [List.getLast?_cons_cons] using hb
      have hyz : val y < val z := hp (y, z) (by simp [consecPairs])
      cases l' with
      | nil =>
        have hzb : z = b := by simpa using hb'
        subst hzb
        exact hyz
      | cons u l'' =>
        have := ih (a := z) (by simp) hb'
          (fun p hp' => hp p (consecPairs_tail_subset _ _ p hp')) (by simp)
        linarith

/-- covering (increasing): a point between the first and last breakpoint values lies between
the values of some adjacent pair. -/
lemma cover_chain : ∀ (v : List α) (a b : α) (x : ℝ), v.head? = some a → v.getLast? = some b →
    (∀ p ∈ consecPairs v, val p.1 < val p.2) → 2 ≤ v.length → val a ≤ x → x ≤ val b →
    ∃ p ∈ consecPairs v, val p.1 ≤ x ∧ x ≤ val p.2 := by
  intro v
  induction v with
  | nil => intro a b x ha; simp at ha
  | cons y l ih =>
    intro a b x ha hb hp h2 hax hxb
    have hya : y = a := by simpa using ha
    subst hya
    cases l with
    | nil => simp at h2
    | cons z l' =>
      have hb' : (z :: l').getLast? = some b := by simpa [List.getLast?_cons_cons] using hb
      by_cases hxz : x ≤ val z
      · exact ⟨(y, z), by simp [consecPairs], hax, hxz⟩
      · rw [not_le] at hxz
        cases l' with
        | nil =>
          have hzb : z = b := by simpa using hb'
          subst hzb
          exact absurd hxb (not_le.mpr hxz)
        | cons u l'' =>
          obtain ⟨p, hpm, hp1, hp2⟩ := ih z b x (by simp) hb'
            (fun p hp' => hp p (consecPairs_tail_subset _ _ p hp')) (by simp) hxz.le hxb
          exact ⟨p, consecPairs_tail_subset _ _ p hpm, hp1, hp2⟩

/-- covering (decreasing): the mirrored version for the top and left edges. -/
lemma cover_chain_dec : ∀ (v : List α) (a b : α) (x : ℝ), v.head? = some a →
    v.getLast? = some b →
    (∀ p ∈ consecPairs v, val p.2 < val p.1) → 2 ≤ v.length → val b ≤ x → x ≤ val a →
    ∃ p ∈ consecPairs v, val p.2 ≤ x ∧ x ≤ val p.1 := by
  intro v
  induction v with
  | nil => intro a b x ha; simp at ha
  | cons y l ih =>
    intro a b x ha hb hp h2 hbx hxa
    have hya : y = a := by simpa using ha
    subst hya
    cases l with
    | nil => simp at h2
    | cons z l' =>
      have hb' : (z :: l').getLast? = some b := by simpa [List.getLast?_cons_cons] using hb
      by_cases hzx : val z ≤ x
      · exact ⟨(y, z), by simp [consecPairs], hzx, hxa⟩
      · rw [not_le] at hzx
        cases l' with
        | nil =>
          have hzb : z = b := by simpa using hb'
          subst hzb
          exact absurd hbx (not_le.mpr hzx)
        | cons u l'' =>
          obtain ⟨p, hpm, hp1, hp2⟩ := ih z b x (by simp) hb'
            (fun p hp' => hp p (consecPairs_tail_subset _ _ p hp')) (by simp) hbx hzx.le
          exact ⟨p, consecPairs_tail_subset _ _ p hpm, hp1, hp2⟩

end ValChain

/-! ## 6. Segment geometry and boundary covering -/

lemma segPt_mk_horiz (u v T t : ℝ) : segPt (cpt u T) (cpt v T) t = cpt (u + t * (v - u)) T := by
  apply Complex.ext
  · simp [segPt, cpt, Complex.add_re, Complex.mul_re, Complex.sub_re, Complex.sub_im,
      Complex.ofReal_re, Complex.ofReal_im]
  · simp [segPt, cpt, Complex.add_im, Complex.mul_im, Complex.sub_re, Complex.sub_im,
      Complex.ofReal_re, Complex.ofReal_im]

lemma segPt_mk_vert (S u v t : ℝ) : segPt (cpt S u) (cpt S v) t = cpt S (u + t * (v - u)) := by
  apply Complex.ext
  · simp [segPt, cpt, Complex.add_re, Complex.mul_re, Complex.sub_re, Complex.sub_im,
      Complex.ofReal_re, Complex.ofReal_im]
  · simp [segPt, cpt, Complex.add_im, Complex.mul_im, Complex.sub_re, Complex.sub_im,
      Complex.ofReal_re, Complex.ofReal_im]

lemma exists_t_inc {u v x : ℝ} (h : u < v) (h1 : u ≤ x) (h2 : x ≤ v) :
    ∃ t : ℝ, 0 ≤ t ∧ t ≤ 1 ∧ u + t * (v - u) = x := by
  have hne : v - u ≠ 0 := sub_ne_zero.mpr h.ne'
  refine ⟨(x - u) / (v - u), div_nonneg (by linarith) (by linarith),
    (div_le_one (by linarith)).mpr (by linarith), ?_⟩
  field_simp
  ring

lemma exists_t_dec {u v x : ℝ} (h : v < u) (h1 : v ≤ x) (h2 : x ≤ u) :
    ∃ t : ℝ, 0 ≤ t ∧ t ≤ 1 ∧ u + t * (v - u) = x := by
  have hne : u - v ≠ 0 := sub_ne_zero.mpr h.ne'
  refine ⟨(u - x) / (u - v), div_nonneg (by linarith) (by linarith),
    (div_le_one (by linarith)).mpr (by linarith), ?_⟩
  field_simp
  ring

/-- every boundary point lies on some transcript segment (the C3 mesh walk is sound: the four
edge chains cover ∂R). -/
lemma bdry_cover {d : W1Data} (hchk : ChecksOK d) :
    ∀ s ∈ W1Bdry d, ∃ zw ∈ segs d, ∃ t : ℝ, 0 ≤ t ∧ t ≤ 1 ∧ segPt zw.1 zw.2 t = s := by
  intro s hs
  obtain ⟨hcl, hno⟩ := hs
  obtain ⟨h1, h2, h3, h4⟩ := hcl
  -- the four edge data packs
  obtain ⟨h2b, hfb, hlb, hcb⟩ := edgeOK_inc_spec hchk.hEb
  obtain ⟨h2r, hfr, hlr, hcr⟩ := edgeOK_inc_spec hchk.hEr
  obtain ⟨h2t, hft, hlt', hct⟩ := edgeOK_dec_spec hchk.hEt
  obtain ⟨h2l, hfl, hll, hclf⟩ := edgeOK_dec_spec hchk.hEl
  rcases eq_or_lt_of_le h3 with e3 | l3
  · -- bottom edge: s.im = T₁
    obtain ⟨ra, hra, hva⟩ := firstOK_spec hfb hchk.hdb hchk.hq1
    obtain ⟨rb, hrb, hvb⟩ := lastOK_spec hchk.hq2 hlb hchk.hdb
    have hpairs := chainLt_spec hchk.hdb hcb
    obtain ⟨q, hqm, hq1, hq2⟩ := cover_chain ratVal d.bottom ra rb s.re hra hrb hpairs h2b
      (by rw [hva]; exact h1) (by rw [hvb]; exact h2)
    obtain ⟨t, ht0, ht1, hteq⟩ := exists_t_inc (hpairs q hqm) hq1 hq2
    refine ⟨(cpt (ratVal q.1) (T1 d), cpt (ratVal q.2) (T1 d)), ?_, t, ht0, ht1, ?_⟩
    · have : (cpt (ratVal q.1) (T1 d), cpt (ratVal q.2) (T1 d))
          ∈ consecPairs (bottomPts d) := by
        unfold bottomPts
        rw [consecPairs_map]
        exact List.mem_map.mpr ⟨q, hqm, rfl⟩
      simp [segs, List.mem_append, this]
    · rw [segPt_mk_horiz, hteq]
      exact Complex.ext rfl (by simpa using e3)
  rcases eq_or_lt_of_le h4 with e4 | l4
  · -- top edge: s.im = T₂
    obtain ⟨ra, hra, hva⟩ := firstOK_spec hft hchk.hdt hchk.hq2
    obtain ⟨rb, hrb, hvb⟩ := lastOK_spec hchk.hq1 hlt' hchk.hdt
    have hpairs := chainGt_spec hchk.hdt hct
    obtain ⟨q, hqm, hq1, hq2⟩ := cover_chain_dec ratVal d.top ra rb s.re hra hrb hpairs h2t
      (by rw [hvb]; exact h1) (by rw [hva]; exact h2)
    obtain ⟨t, ht0, ht1, hteq⟩ := exists_t_dec (hpairs q hqm) hq1 hq2
    refine ⟨(cpt (ratVal q.1) (T2 d), cpt (ratVal q.2) (T2 d)), ?_, t, ht0, ht1, ?_⟩
    · have : (cpt (ratVal q.1) (T2 d), cpt (ratVal q.2) (T2 d))
          ∈ consecPairs (topPts d) := by
        unfold topPts
        rw [consecPairs_map]
        exact List.mem_map.mpr ⟨q, hqm, rfl⟩
      simp [segs, List.mem_append, this]
    · rw [segPt_mk_horiz, hteq]
      exact Complex.ext rfl (by simpa using e4.symm)
  rcases eq_or_lt_of_le h1 with e1 | l1
  · -- left edge: s.re = σ₁
    obtain ⟨ra, hra, hva⟩ := firstOK_spec hfl hchk.hdl hchk.hb2
    obtain ⟨rb, hrb, hvb⟩ := lastOK_spec hchk.hb1 hll hchk.hdl
    have hpairs := chainGt_spec hchk.hdl hclf
    obtain ⟨q, hqm, hq1, hq2⟩ := cover_chain_dec ratVal d.left ra rb s.im hra hrb hpairs h2l
      (by rw [hvb]; exact l3.le) (by rw [hva]; exact l4.le)
    obtain ⟨t, ht0, ht1, hteq⟩ := exists_t_dec (hpairs q hqm) hq1 hq2
    refine ⟨(cpt (sigma1 d) (ratVal q.1), cpt (sigma1 d) (ratVal q.2)), ?_, t, ht0, ht1, ?_⟩
    · have : (cpt (sigma1 d) (ratVal q.1), cpt (sigma1 d) (ratVal q.2))
          ∈ consecPairs (leftPts d) := by
        unfold leftPts
        rw [consecPairs_map]
        exact List.mem_map.mpr ⟨q, hqm, rfl⟩
      simp [segs, List.mem_append, this]
    · rw [segPt_mk_vert, hteq]
      exact Complex.ext (by simpa using e1) rfl
  rcases eq_or_lt_of_le h2 with e2 | l2
  · -- right edge: s.re = σ₂
    obtain ⟨ra, hra, hva⟩ := firstOK_spec hfr hchk.hdr hchk.hb1
    obtain ⟨rb, hrb, hvb⟩ := lastOK_spec hchk.hb2 hlr hchk.hdr
    have hpairs := chainLt_spec hchk.hdr hcr
    obtain ⟨q, hqm, hq1, hq2⟩ := cover_chain ratVal d.right ra rb s.im hra hrb hpairs h2r
      (by rw [hva]; exact l3.le) (by rw [hvb]; exact l4.le)
    obtain ⟨t, ht0, ht1, hteq⟩ := exists_t_inc (hpairs q hqm) hq1 hq2
    refine ⟨(cpt (sigma2 d) (ratVal q.1), cpt (sigma2 d) (ratVal q.2)), ?_, t, ht0, ht1, ?_⟩
    · have : (cpt (sigma2 d) (ratVal q.1), cpt (sigma2 d) (ratVal q.2))
          ∈ consecPairs (rightPts d) := by
        unfold rightPts
        rw [consecPairs_map]
        exact List.mem_map.mpr ⟨q, hqm, rfl⟩
      simp [segs, List.mem_append, this]
    · rw [segPt_mk_vert, hteq]
      exact Complex.ext (by simpa using e2.symm) rfl
  · exact absurd ⟨l1, l2, l3, l4⟩ hno

/-- extract the related left element for a member of the right list of a `Forall₂`. -/
lemma forall₂_mem_right {α β : Type*} {R : α → β → Prop} :
    ∀ {l₁ : List α} {l₂ : List β}, List.Forall₂ R l₁ l₂ → ∀ b ∈ l₂, ∃ a ∈ l₁, R a b := by
  intro l₁ l₂ h
  induction h with
  | nil => intro b hb; cases hb
  | @cons a b l₁' l₂' hR hF ih =>
    intro c hc
    rcases List.mem_cons.mp hc with rfl | hc
    · exact ⟨a, by simp, hR⟩
    · obtain ⟨a', ha', hR'⟩ := ih c hc
      exact ⟨a', by simp [ha'], hR'⟩

/-- FORMAT.md derivation D1 at the point level: an H-ENCL row whose box passes C6 forces f ≠ 0
on the whole closed segment. -/
lemma row_box_excludes_zero {f : ℂ → ℂ} {K A : ℤ} {row : W1Row} {zw : ℂ × ℂ}
    (hE : RowEnclOK f K A row zw)
    (hC6 : 0 < row.reLo ∨ row.reHi < 0 ∨ 0 < row.imLo ∨ row.imHi < 0) :
    ∀ t : ℝ, 0 ≤ t → t ≤ 1 → f (segPt zw.1 zw.2 t) ≠ 0 := by
  intro t ht0 ht1 hf0
  obtain ⟨⟨hre1, hre2⟩, him1, him2⟩ := hE.1 t ht0 ht1
  rw [hf0] at hre1 hre2 him1 him2
  simp only [Complex.zero_re, Complex.zero_im, mul_zero] at hre1 hre2 him1 him2
  have hre1' : row.reLo ≤ 0 := by exact_mod_cast hre1
  have hre2' : (0 : ℤ) ≤ row.reHi := by exact_mod_cast hre2
  have him1' : row.imLo ≤ 0 := by exact_mod_cast him1
  have him2' : (0 : ℤ) ≤ row.imHi := by exact_mod_cast him2
  rcases hC6 with h | h | h | h <;> omega

/-- step 1 of the §6.3 chain: f ≠ 0 on all of ∂R. -/
lemma boundary_nonvanishing {f : ℂ → ℂ} {d : W1Data} (hchk : ChecksOK d) (hE : W1EnclOK f d) :
    ∀ s ∈ W1Bdry d, f s ≠ 0 := by
  intro s hs
  obtain ⟨zw, hzw, t, ht0, ht1, hpt⟩ := bdry_cover hchk s hs
  obtain ⟨row, hrow, hR⟩ := forall₂_mem_right hE zw hzw
  have hOK := rowsOK_mem hchk.hRows row hrow
  have := row_box_excludes_zero hR (rowOK_C6 hOK) t ht0 ht1
  rw [hpt] at this
  exact this

/-! ## 7. Sum enclosures (H-ENCL(b) rows → the total winding enclosure) -/

lemma im_list_sum : ∀ l : List ℂ, l.sum.im = (l.map Complex.im).sum := by
  intro l
  induction l with
  | nil => simp
  | cons a l ih => simp [List.sum_cons, Complex.add_im, ih]

/-- summing the H-ENCL(b) rows: S_lo ≤ A·(ΣΔ/2π) ≤ S_hi. -/
lemma sum_arg_encl {f : ℂ → ℂ} {K A : ℤ} :
    ∀ {rows : List W1Row} {ss : List (ℂ × ℂ)}, List.Forall₂ (RowEnclOK f K A) rows ss →
    (sumArgLo rows : ℝ) ≤ A * ((ss.map fun zw => argIncrement f zw.1 zw.2).sum / (2 * π))
      ∧ (A : ℝ) * ((ss.map fun zw => argIncrement f zw.1 zw.2).sum / (2 * π))
        ≤ (sumArgHi rows : ℝ) := by
  intro rows ss h
  induction h with
  | nil => simp [sumArgLo, sumArgHi]
  | @cons row zw rows' ss' hR hF ih =>
    simp only [sumArgLo, sumArgHi, List.map_cons, List.sum_cons, Int.cast_add, add_div,
      mul_add]
    obtain ⟨ih1, ih2⟩ := ih
    obtain ⟨hlo, hhi⟩ := hR.2
    constructor <;> linarith

/-! ## 8. L1: additivity of the log-derivative integral over the mesh (FORMAT.md §8.3) -/

@[simp] lemma segPt_zero (z w : ℂ) : segPt z w 0 = z := by simp [segPt]

@[simp] lemma segPt_one (z w : ℂ) : segPt z w 1 = w := by simp [segPt]

lemma segPt_comp (z w : ℂ) (t₁ t₂ s : ℝ) :
    segPt (segPt z w t₁) (segPt z w t₂) s = segPt z w (t₁ + (t₂ - t₁) * s) := by
  simp only [segPt]
  push_cast
  ring

lemma segPt_horiz_tau {u v : ℝ} (h : u ≠ v) (T y : ℝ) :
    segPt (cpt u T) (cpt v T) ((y - u) / (v - u)) = cpt y T := by
  rw [segPt_mk_horiz]
  congr 1
  have hne : v - u ≠ 0 := sub_ne_zero.mpr (Ne.symm h)
  field_simp
  ring

lemma segPt_vert_tau {u v : ℝ} (h : u ≠ v) (S y : ℝ) :
    segPt (cpt S u) (cpt S v) ((y - u) / (v - u)) = cpt S y := by
  rw [segPt_mk_vert]
  congr 1
  have hne : v - u ≠ 0 := sub_ne_zero.mpr (Ne.symm h)
  field_simp
  ring

lemma smul_comp_integral (F : ℝ → ℂ) (c d : ℝ) :
    (∫ s in (0:ℝ)..1, c • F (c * s + d)) = ∫ u in d..c + d, F u := by
  rw [intervalIntegral.integral_smul, intervalIntegral.smul_integral_comp_mul_add]
  norm_num

/-- affine reparameterization: the log-derivative integral over a sub-segment of z → w is the
interval integral of the edge integrand over the parameter interval. -/
lemma logDerivSegIntegral_affine (f : ℂ → ℂ) (z w : ℂ) (t₁ t₂ : ℝ) :
    logDerivSegIntegral f (segPt z w t₁) (segPt z w t₂)
      = ∫ t in t₁..t₂, (deriv f (segPt z w t) / f (segPt z w t)) * (w - z) := by
  have hsub : segPt z w t₂ - segPt z w t₁ = ((t₂ - t₁ : ℝ) : ℂ) * (w - z) := by
    simp only [segPt]
    push_cast
    ring
  have hcongr : logDerivSegIntegral f (segPt z w t₁) (segPt z w t₂)
      = ∫ s in (0:ℝ)..1, (t₂ - t₁) •
          ((deriv f (segPt z w ((t₂ - t₁) * s + t₁)) / f (segPt z w ((t₂ - t₁) * s + t₁)))
            * (w - z)) := by
    unfold logDerivSegIntegral
    apply intervalIntegral.integral_congr
    intro s _
    show (deriv f (segPt (segPt z w t₁) (segPt z w t₂) s)
          / f (segPt (segPt z w t₁) (segPt z w t₂) s)) * (segPt z w t₂ - segPt z w t₁)
        = (t₂ - t₁) • ((deriv f (segPt z w ((t₂ - t₁) * s + t₁))
          / f (segPt z w ((t₂ - t₁) * s + t₁))) * (w - z))
    have harg : t₁ + (t₂ - t₁) * s = (t₂ - t₁) * s + t₁ := by ring
    rw [segPt_comp, harg, hsub, Complex.real_smul]
    ring
  rw [hcongr]
  have key := smul_comp_integral
    (fun u : ℝ => (deriv f (segPt z w u) / f (segPt z w u)) * (w - z)) (t₂ - t₁) t₁
  have hb : t₂ - t₁ + t₁ = t₂ := by ring
  rw [hb] at key
  exact key

/-- adjacent-interval additivity over the consecutive pairs of a breakpoint list. -/
lemma sum_integral_consecPairs (F : ℝ → ℂ) :
    ∀ (v : List ℝ) (a b : ℝ), v.head? = some a → v.getLast? = some b →
    (∀ p ∈ consecPairs v, p.1 ≤ p.2) →
    (∀ u u' : ℝ, a ≤ u → u ≤ u' → u' ≤ b → IntervalIntegrable F volume u u') →
    ((consecPairs v).map fun p => ∫ t in p.1..p.2, F t).sum = ∫ t in a..b, F t := by
  intro v
  induction v with
  | nil => intro a b ha; simp at ha
  | cons y l ih =>
    intro a b ha hb hle hInt
    have hya : y = a := by simpa using ha
    subst hya
    cases l with
    | nil =>
      have hyb : y = b := by simpa using hb
      subst hyb
      simp [consecPairs, intervalIntegral.integral_same]
    | cons z l' =>
      have hb' : (z :: l').getLast? = some b := by simpa [List.getLast?_cons_cons] using hb
      have hyz : y ≤ z := hle (y, z) (by simp [consecPairs])
      have hzb : z ≤ b :=
        getLast_ge_of_consec_le (fun x : ℝ => x) hb'
          (fun p hp' => hle p (consecPairs_tail_subset _ _ p hp')) z (by simp)
      have hInt' : ∀ u u' : ℝ, z ≤ u → u ≤ u' → u' ≤ b → IntervalIntegrable F volume u u' :=
        fun u u' hu huu hu' => hInt u u' (le_trans hyz hu) huu hu'
      have hrec := ih z b (by simp) hb'
        (fun p hp' => hle p (consecPairs_tail_subset _ _ p hp')) hInt'
      have hys : consecPairs (y :: z :: l') = (y, z) :: consecPairs (z :: l') := rfl
      rw [hys, List.map_cons, List.sum_cons, hrec]
      exact intervalIntegral.integral_add_adjacent_intervals
        (hInt y z le_rfl hyz hzb) (hInt z b hyz hzb le_rfl)

/-- transfer of a pairwise property through `map` on consecutive pairs. -/
lemma consec_map_forall {α β : Type*} {P : β × β → Prop} {g : α → β} {l : List α}
    (h : ∀ q ∈ consecPairs l, P (g q.1, g q.2)) :
    ∀ p ∈ consecPairs (l.map g), P p := by
  intro p hp
  rw [consecPairs_map] at hp
  obtain ⟨q, hqm, rfl⟩ := List.mem_map.mp hp
  exact h q hqm

/-- the increasing affine parameter map: head/last/monotonicity facts for τ(y) = (y−e₀)/(e₁−e₀),
e₀ < e₁. -/
lemma tau_facts_inc {v : List ℝ} {e₀ e₁ : ℝ} (h : e₀ < e₁)
    (hhead : v.head? = some e₀) (hlast : v.getLast? = some e₁)
    (hlt : ∀ p ∈ consecPairs v, p.1 < p.2) :
    (v.map fun y => (y - e₀) / (e₁ - e₀)).head? = some 0
      ∧ (v.map fun y => (y - e₀) / (e₁ - e₀)).getLast? = some 1
      ∧ ∀ p ∈ consecPairs (v.map fun y => (y - e₀) / (e₁ - e₀)), p.1 ≤ p.2 := by
  have hne : e₁ - e₀ ≠ 0 := sub_ne_zero.mpr h.ne'
  refine ⟨?_, ?_, ?_⟩
  · rw [List.head?_map, hhead, Option.map_some]
    simp
  · rw [List.getLast?_map, hlast, Option.map_some]
    simp [div_self hne]
  · refine consec_map_forall fun q hq => ?_
    have hq12 := (hlt q hq).le
    simp only [div_eq_mul_inv]
    exact mul_le_mul_of_nonneg_right (by linarith)
      (inv_nonneg.mpr (by linarith))

/-- the decreasing affine parameter map: the mirrored facts for e₁ < e₀ (top and left edges). -/
lemma tau_facts_dec {v : List ℝ} {e₀ e₁ : ℝ} (h : e₁ < e₀)
    (hhead : v.head? = some e₀) (hlast : v.getLast? = some e₁)
    (hgt : ∀ p ∈ consecPairs v, p.2 < p.1) :
    (v.map fun y => (y - e₀) / (e₁ - e₀)).head? = some 0
      ∧ (v.map fun y => (y - e₀) / (e₁ - e₀)).getLast? = some 1
      ∧ ∀ p ∈ consecPairs (v.map fun y => (y - e₀) / (e₁ - e₀)), p.1 ≤ p.2 := by
  have hne : e₁ - e₀ ≠ 0 := sub_ne_zero.mpr h.ne
  refine ⟨?_, ?_, ?_⟩
  · rw [List.head?_map, hhead, Option.map_some]
    simp
  · rw [List.getLast?_map, hlast, Option.map_some]
    simp [div_self hne]
  · refine consec_map_forall fun q hq => ?_
    have hq12 := (hgt q hq).le
    simp only [div_eq_mul_inv]
    exact mul_le_mul_of_nonpos_right (by linarith)
      (inv_nonpos.mpr (by linarith))

/-- **L1** (FORMAT.md §8.3): the mesh-segment integrals of one edge sum to the full directed
edge integral, given a parameterization of the breakpoints by an affine chain 0 → 1 and
continuity of the edge integrand. -/
lemma edge_sum_eq {f : ℂ → ℂ} {z w : ℂ} (v : List ℝ) (g : ℝ → ℝ)
    (hhead : (v.map g).head? = some 0) (hlast : (v.map g).getLast? = some 1)
    (hle : ∀ p ∈ consecPairs (v.map g), p.1 ≤ p.2)
    (hcont : ContinuousOn (fun t : ℝ => (deriv f (segPt z w t) / f (segPt z w t)) * (w - z))
      (Set.Icc 0 1)) :
    ((consecPairs (v.map fun y => segPt z w (g y))).map
        fun p => logDerivSegIntegral f p.1 p.2).sum
      = logDerivSegIntegral f z w := by
  have hInt : ∀ u u' : ℝ, 0 ≤ u → u ≤ u' → u' ≤ 1 →
      IntervalIntegrable (fun t : ℝ => (deriv f (segPt z w t) / f (segPt z w t)) * (w - z))
        volume u u' := by
    intro u u' h0 huu h1
    apply ContinuousOn.intervalIntegrable
    apply hcont.mono
    rw [Set.uIcc_of_le huu]
    exact Set.Icc_subset_Icc h0 h1
  have hpairs : consecPairs (v.map fun y => segPt z w (g y))
      = (consecPairs (v.map g)).map fun p : ℝ × ℝ => (segPt z w p.1, segPt z w p.2) := by
    have h1 : (v.map fun y => segPt z w (g y)) = (v.map g).map fun t : ℝ => segPt z w t := by
      rw [List.map_map]
      simp only [Function.comp_def]
    rw [h1, consecPairs_map]
  rw [hpairs, List.map_map]
  have h2 : ((fun p : ℂ × ℂ => logDerivSegIntegral f p.1 p.2)
      ∘ fun p : ℝ × ℝ => (segPt z w p.1, segPt z w p.2))
      = fun p : ℝ × ℝ =>
          ∫ t in p.1..p.2, (deriv f (segPt z w t) / f (segPt z w t)) * (w - z) := by
    funext p
    exact logDerivSegIntegral_affine f z w p.1 p.2
  rw [h2]
  calc ((consecPairs (v.map g)).map fun p : ℝ × ℝ =>
        ∫ t in p.1..p.2, (deriv f (segPt z w t) / f (segPt z w t)) * (w - z)).sum
      = ∫ t in (0:ℝ)..1, (deriv f (segPt z w t) / f (segPt z w t)) * (w - z) :=
        sum_integral_consecPairs _ (v.map g) 0 1 hhead hlast hle hInt
    _ = logDerivSegIntegral f z w := by
        have h01 := logDerivSegIntegral_affine f z w 0 1
        rw [segPt_zero, segPt_one] at h01
        exact h01.symm

/-! ## 9. The ζ edge integrand is continuous (analyticity off s = 1 + boundary nonvanishing) -/

lemma continuousOn_zeta_logDeriv_seg {z w : ℂ}
    (hre : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → (segPt z w t).re < 1)
    (hnz : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → riemannZeta (segPt z w t) ≠ 0) :
    ContinuousOn
      (fun t : ℝ => (deriv riemannZeta (segPt z w t) / riemannZeta (segPt z w t)) * (w - z))
      (Set.Icc 0 1) := by
  have hUopen : IsOpen {s : ℂ | s.re < 1} := isOpen_lt Complex.continuous_re continuous_const
  have hdiff : DifferentiableOn ℂ riemannZeta {s : ℂ | s.re < 1} := by
    intro s hs
    refine (differentiableAt_riemannZeta ?_).differentiableWithinAt
    intro h1
    rw [h1] at hs
    simp at hs
  have hζ : AnalyticOnNhd ℂ riemannZeta {s : ℂ | s.re < 1} := hdiff.analyticOnNhd hUopen
  have hdC : ContinuousOn (deriv riemannZeta) {s : ℂ | s.re < 1} := hζ.deriv.continuousOn
  have hzC : ContinuousOn riemannZeta {s : ℂ | s.re < 1} := hζ.continuousOn
  have hseg : Continuous fun t : ℝ => segPt z w t := by
    unfold segPt
    exact continuous_const.add (Complex.continuous_ofReal.mul continuous_const)
  have hmaps : Set.MapsTo (fun t : ℝ => segPt z w t) (Set.Icc 0 1) {s : ℂ | s.re < 1} :=
    fun t ht => hre t ht.1 ht.2
  exact ((hdC.comp hseg.continuousOn hmaps).div (hzC.comp hseg.continuousOn hmaps)
    fun t ht => hnz t ht.1 ht.2).mul continuousOn_const

/-! ## 10. Winding pinning (FORMAT.md derivation D4) and the soundness theorem -/

/-- D4: a winding enclosure of width < ½ turn containing both A·z and A·m forces z = m. -/
lemma pin_m {A m z Slo Shi : ℤ} (hA : 1 ≤ A) (h8 : 2 * (Shi - Slo) < A)
    (h9a : Slo ≤ A * m) (h9b : A * m ≤ Shi) (hza : Slo ≤ A * z) (hzb : A * z ≤ Shi) :
    z = m := by
  rcases lt_trichotomy z m with h | h | h
  · exfalso
    have h1 : z + 1 ≤ m := by omega
    have h2 := mul_le_mul_of_nonneg_left h1 (by linarith : (0:ℤ) ≤ A)
    rw [mul_add, mul_one] at h2
    linarith
  · exact h
  · exfalso
    have h1 : m + 1 ≤ z := by omega
    have h2 := mul_le_mul_of_nonneg_left h1 (by linarith : (0:ℤ) ≤ A)
    rw [mul_add, mul_one] at h2
    linarith

/-- **W1 checker soundness** (FORMAT.md §6.3, the L3 obligation; theorem shape per §7.1).
Modulo the two displayed hypotheses H-ENCL (`W1EnclOK riemannZeta d`) and H-AP
(`RectArgPrinciple riemannZeta`), an accepted transcript certifies: for m ≥ 1, a zero ρ of ζ
with 1/2 < Re ρ < 1 and T₁ < Im ρ < T₂ (for f = ζ this is ¬RH, derivation D5); for m = 0, no
zeros of ζ in the closed rectangle R (the exclusion/M3 form; ledger language per D-R6).
Here `T1 d`/`T2 d` are literally the transcript rationals a1/b1, a2/b2 as reals. -/
theorem cert_of_checkW1 (d : W1Data) (hc : checkW1 d = true)
    (hEncl : W1EnclOK riemannZeta d) (hAP : RectArgPrinciple riemannZeta) :
    (1 ≤ d.m → ∃ ρ : ℂ, riemannZeta ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1
        ∧ T1 d < ρ.im ∧ ρ.im < T2 d)
    ∧ (d.m = 0 → ∀ s ∈ W1Rect d, riemannZeta s ≠ 0) := by
  have hchk := checksOK_of_checkW1 hc
  -- rectangle facts (D7 conversions of C2)
  have hhalf : 1 / 2 < sigma1 d := by
    have h12 : ratVal (1, 2) = 1 / 2 := by norm_num [ratVal]
    have h := ratVal_lt_of_cross (r := ((1:ℤ), (2:ℤ))) (s := (d.p1, d.q1)) (by norm_num)
      hchk.hq1 (show (1:ℤ) * d.q1 < d.p1 * 2 by have := hchk.hC2a; omega)
    rw [h12] at h
    exact h
  have hs12le : sigma1 d ≤ sigma2 d :=
    ratVal_le_of_cross (r := (d.p1, d.q1)) (s := (d.p2, d.q2)) hchk.hq1 hchk.hq2 hchk.hC2b
  have hs2lt1 : sigma2 d < 1 := by
    have h11 : ratVal (1, 1) = 1 := by norm_num [ratVal]
    have h := ratVal_lt_of_cross (r := (d.p2, d.q2)) (s := ((1:ℤ), (1:ℤ))) hchk.hq2
      (by norm_num) (show d.p2 * 1 < 1 * d.q2 by have := hchk.hC2c; omega)
    rw [h11] at h
    exact h
  have hT12 : T1 d < T2 d :=
    ratVal_lt_of_cross (r := (d.a1, d.b1)) (s := (d.a2, d.b2)) hchk.hb1 hchk.hb2 hchk.hC2d
  -- boundary nonvanishing (step 1 of the chain)
  have hbnz := boundary_nonvanishing hchk hEncl
  -- edge data
  obtain ⟨h2b, hfb, hlb, hcb⟩ := edgeOK_inc_spec hchk.hEb
  obtain ⟨h2r, hfr, hlr, hcr⟩ := edgeOK_inc_spec hchk.hEr
  obtain ⟨h2t, hft, hlt', hct⟩ := edgeOK_dec_spec hchk.hEt
  obtain ⟨h2l, hfl, hll, hclf⟩ := edgeOK_dec_spec hchk.hEl
  -- real breakpoint chains, heads and lasts
  obtain ⟨rba, hrba, hvba⟩ := firstOK_spec hfb hchk.hdb hchk.hq1
  obtain ⟨rbb, hrbb, hvbb⟩ := lastOK_spec hchk.hq2 hlb hchk.hdb
  have hheadb : (d.bottom.map ratVal).head? = some (sigma1 d) := by
    rw [List.head?_map, hrba, Option.map_some]
    exact congrArg some hvba
  have hlastb : (d.bottom.map ratVal).getLast? = some (sigma2 d) := by
    rw [List.getLast?_map, hrbb, Option.map_some]
    exact congrArg some hvbb
  have hpairsb : ∀ p ∈ consecPairs (d.bottom.map ratVal), p.1 < p.2 :=
    consec_map_forall fun q hq => chainLt_spec hchk.hdb hcb q hq
  -- σ₁ < σ₂ (forced by the bottom chain, C3)
  have hs12 : sigma1 d < sigma2 d :=
    head?_lt_getLast? (fun x : ℝ => x) hheadb hlastb hpairsb (by simpa using h2b)
  obtain ⟨rra, hrra, hvra⟩ := firstOK_spec hfr hchk.hdr hchk.hb1
  obtain ⟨rrb, hrrb, hvrb⟩ := lastOK_spec hchk.hb2 hlr hchk.hdr
  have hheadr : (d.right.map ratVal).head? = some (T1 d) := by
    rw [List.head?_map, hrra, Option.map_some]
    exact congrArg some hvra
  have hlastr : (d.right.map ratVal).getLast? = some (T2 d) := by
    rw [List.getLast?_map, hrrb, Option.map_some]
    exact congrArg some hvrb
  have hpairsr : ∀ p ∈ consecPairs (d.right.map ratVal), p.1 < p.2 :=
    consec_map_forall fun q hq => chainLt_spec hchk.hdr hcr q hq
  obtain ⟨rta, hrta, hvta⟩ := firstOK_spec hft hchk.hdt hchk.hq2
  obtain ⟨rtb, hrtb, hvtb⟩ := lastOK_spec hchk.hq1 hlt' hchk.hdt
  have hheadt : (d.top.map ratVal).head? = some (sigma2 d) := by
    rw [List.head?_map, hrta, Option.map_some]
    exact congrArg some hvta
  have hlastt : (d.top.map ratVal).getLast? = some (sigma1 d) := by
    rw [List.getLast?_map, hrtb, Option.map_some]
    exact congrArg some hvtb
  have hpairst : ∀ p ∈ consecPairs (d.top.map ratVal), p.2 < p.1 :=
    consec_map_forall fun q hq => chainGt_spec hchk.hdt hct q hq
  obtain ⟨rla, hrla, hvla⟩ := firstOK_spec hfl hchk.hdl hchk.hb2
  obtain ⟨rlb, hrlb, hvlb⟩ := lastOK_spec hchk.hb1 hll hchk.hdl
  have hheadl : (d.left.map ratVal).head? = some (T2 d) := by
    rw [List.head?_map, hrla, Option.map_some]
    exact congrArg some hvla
  have hlastl : (d.left.map ratVal).getLast? = some (T1 d) := by
    rw [List.getLast?_map, hrlb, Option.map_some]
    exact congrArg some hvlb
  have hpairsl : ∀ p ∈ consecPairs (d.left.map ratVal), p.2 < p.1 :=
    consec_map_forall fun q hq => chainGt_spec hchk.hdl hclf q hq
  -- the four edge continuity facts
  have hcontB := continuousOn_zeta_logDeriv_seg
    (z := cpt (sigma1 d) (T1 d)) (w := cpt (sigma2 d) (T1 d))
    (fun t ht0 ht1 => by
      rw [segPt_mk_horiz]
      simp only [cpt_re]
      nlinarith)
    (fun t ht0 ht1 => by
      apply hbnz
      rw [segPt_mk_horiz]
      simp only [W1Bdry, rectBdry, rectClosed, rectOpen, Set.mem_sdiff, Set.mem_ofPred_eq,
        cpt_re, cpt_im]
      refine ⟨⟨by nlinarith, by nlinarith, le_rfl, hT12.le⟩, ?_⟩
      rintro ⟨-, -, hlt, -⟩
      exact lt_irrefl _ hlt)
  have hcontR := continuousOn_zeta_logDeriv_seg
    (z := cpt (sigma2 d) (T1 d)) (w := cpt (sigma2 d) (T2 d))
    (fun t ht0 ht1 => by
      rw [segPt_mk_vert]
      simp only [cpt_re]
      exact hs2lt1)
    (fun t ht0 ht1 => by
      apply hbnz
      rw [segPt_mk_vert]
      simp only [W1Bdry, rectBdry, rectClosed, rectOpen, Set.mem_sdiff, Set.mem_ofPred_eq,
        cpt_re, cpt_im]
      refine ⟨⟨hs12le, le_rfl, by nlinarith, by nlinarith⟩, ?_⟩
      rintro ⟨-, hlt, -, -⟩
      exact lt_irrefl _ hlt)
  have hcontT := continuousOn_zeta_logDeriv_seg
    (z := cpt (sigma2 d) (T2 d)) (w := cpt (sigma1 d) (T2 d))
    (fun t ht0 ht1 => by
      rw [segPt_mk_horiz]
      simp only [cpt_re]
      nlinarith)
    (fun t ht0 ht1 => by
      apply hbnz
      rw [segPt_mk_horiz]
      simp only [W1Bdry, rectBdry, rectClosed, rectOpen, Set.mem_sdiff, Set.mem_ofPred_eq,
        cpt_re, cpt_im]
      refine ⟨⟨by nlinarith, by nlinarith, hT12.le, le_rfl⟩, ?_⟩
      rintro ⟨-, -, -, hlt⟩
      exact lt_irrefl _ hlt)
  have hcontL := continuousOn_zeta_logDeriv_seg
    (z := cpt (sigma1 d) (T2 d)) (w := cpt (sigma1 d) (T1 d))
    (fun t ht0 ht1 => by
      rw [segPt_mk_vert]
      simp only [cpt_re]
      exact lt_of_le_of_lt hs12le hs2lt1)
    (fun t ht0 ht1 => by
      apply hbnz
      rw [segPt_mk_vert]
      simp only [W1Bdry, rectBdry, rectClosed, rectOpen, Set.mem_sdiff, Set.mem_ofPred_eq,
        cpt_re, cpt_im]
      refine ⟨⟨le_rfl, hs12le, by nlinarith, by nlinarith⟩, ?_⟩
      rintro ⟨hlt, -, -, -⟩
      exact lt_irrefl _ hlt)
  -- the four edge sums (L1 per edge)
  have hsumB : ((consecPairs (bottomPts d)).map
      fun p => logDerivSegIntegral riemannZeta p.1 p.2).sum
      = logDerivSegIntegral riemannZeta (cpt (sigma1 d) (T1 d)) (cpt (sigma2 d) (T1 d)) := by
    obtain ⟨hgh, hgl, hgle⟩ := tau_facts_inc hs12 hheadb hlastb hpairsb
    have hbp : bottomPts d = (d.bottom.map ratVal).map
        fun y => segPt (cpt (sigma1 d) (T1 d)) (cpt (sigma2 d) (T1 d))
          ((y - sigma1 d) / (sigma2 d - sigma1 d)) := by
      unfold bottomPts
      rw [List.map_map]
      exact map_congr_fn (fun r => (segPt_horiz_tau hs12.ne (T1 d) (ratVal r)).symm) d.bottom
    rw [hbp]
    exact edge_sum_eq _ _ hgh hgl hgle hcontB
  have hsumR : ((consecPairs (rightPts d)).map
      fun p => logDerivSegIntegral riemannZeta p.1 p.2).sum
      = logDerivSegIntegral riemannZeta (cpt (sigma2 d) (T1 d)) (cpt (sigma2 d) (T2 d)) := by
    obtain ⟨hgh, hgl, hgle⟩ := tau_facts_inc hT12 hheadr hlastr hpairsr
    have hbp : rightPts d = (d.right.map ratVal).map
        fun y => segPt (cpt (sigma2 d) (T1 d)) (cpt (sigma2 d) (T2 d))
          ((y - T1 d) / (T2 d - T1 d)) := by
      unfold rightPts
      rw [List.map_map]
      exact map_congr_fn (fun r => (segPt_vert_tau hT12.ne (sigma2 d) (ratVal r)).symm) d.right
    rw [hbp]
    exact edge_sum_eq _ _ hgh hgl hgle hcontR
  have hsumT : ((consecPairs (topPts d)).map
      fun p => logDerivSegIntegral riemannZeta p.1 p.2).sum
      = logDerivSegIntegral riemannZeta (cpt (sigma2 d) (T2 d)) (cpt (sigma1 d) (T2 d)) := by
    obtain ⟨hgh, hgl, hgle⟩ := tau_facts_dec hs12 hheadt hlastt hpairst
    have hbp : topPts d = (d.top.map ratVal).map
        fun y => segPt (cpt (sigma2 d) (T2 d)) (cpt (sigma1 d) (T2 d))
          ((y - sigma2 d) / (sigma1 d - sigma2 d)) := by
      unfold topPts
      rw [List.map_map]
      exact map_congr_fn (fun r => (segPt_horiz_tau hs12.ne' (T2 d) (ratVal r)).symm) d.top
    rw [hbp]
    exact edge_sum_eq _ _ hgh hgl hgle hcontT
  have hsumL : ((consecPairs (leftPts d)).map
      fun p => logDerivSegIntegral riemannZeta p.1 p.2).sum
      = logDerivSegIntegral riemannZeta (cpt (sigma1 d) (T2 d)) (cpt (sigma1 d) (T1 d)) := by
    obtain ⟨hgh, hgl, hgle⟩ := tau_facts_dec hT12 hheadl hlastl hpairsl
    have hbp : leftPts d = (d.left.map ratVal).map
        fun y => segPt (cpt (sigma1 d) (T2 d)) (cpt (sigma1 d) (T1 d))
          ((y - T2 d) / (T1 d - T2 d)) := by
      unfold leftPts
      rw [List.map_map]
      exact map_congr_fn (fun r => (segPt_vert_tau hT12.ne' (sigma1 d) (ratVal r)).symm) d.left
    rw [hbp]
    exact edge_sum_eq _ _ hgh hgl hgle hcontL
  -- apply H-AP
  have hUopen : IsOpen {s : ℂ | s.re < 1} := isOpen_lt Complex.continuous_re continuous_const
  have hUsub : rectClosed (sigma1 d) (sigma2 d) (T1 d) (T2 d) ⊆ {s : ℂ | s.re < 1} := by
    intro s hs
    exact lt_of_le_of_lt hs.2.1 hs2lt1
  have hdiff : DifferentiableOn ℂ riemannZeta {s : ℂ | s.re < 1} := by
    intro s hs
    refine (differentiableAt_riemannZeta ?_).differentiableWithinAt
    intro h1
    rw [h1] at hs
    simp at hs
  obtain ⟨Z, hZeq, hZ0, hZ1⟩ := hAP (sigma1 d) (sigma2 d) (T1 d) (T2 d) hhalf hs12le hs2lt1
    hT12 _ hUopen hUsub hdiff hbnz
  -- total winding: the segment sum equals 2πZ
  have hsegsum : ((segs d).map fun p => logDerivSegIntegral riemannZeta p.1 p.2).sum
      = logDerivSegIntegral riemannZeta (cpt (sigma1 d) (T1 d)) (cpt (sigma2 d) (T1 d))
        + logDerivSegIntegral riemannZeta (cpt (sigma2 d) (T1 d)) (cpt (sigma2 d) (T2 d))
        + logDerivSegIntegral riemannZeta (cpt (sigma2 d) (T2 d)) (cpt (sigma1 d) (T2 d))
        + logDerivSegIntegral riemannZeta (cpt (sigma1 d) (T2 d)) (cpt (sigma1 d) (T1 d)) := by
    unfold segs
    rw [List.map_append, List.map_append, List.map_append, List.sum_append, List.sum_append,
      List.sum_append, hsumB, hsumR, hsumT, hsumL]
  have htot : ((segs d).map fun p => argIncrement riemannZeta p.1 p.2).sum = 2 * π * Z := by
    have h1 : ((segs d).map fun p => argIncrement riemannZeta p.1 p.2)
        = ((segs d).map fun p => logDerivSegIntegral riemannZeta p.1 p.2).map Complex.im := by
      rw [List.map_map]
      rfl
    rw [h1, ← im_list_sum, hsegsum]
    simp only [Complex.add_im]
    exact hZeq.symm
  -- the winding enclosure pins Z = m (steps 3–4 of the chain)
  obtain ⟨hlo, hhi⟩ := sum_arg_encl hEncl
  rw [htot] at hlo hhi
  have h2π : (2:ℝ) * π ≠ 0 := Real.two_pi_pos.ne'
  rw [mul_div_cancel_left₀ _ h2π] at hlo hhi
  have hloZ : sumArgLo d.rows ≤ d.A * (Z:ℤ) := by exact_mod_cast hlo
  have hhiZ : d.A * (Z:ℤ) ≤ sumArgHi d.rows := by exact_mod_cast hhi
  have hZm : (Z:ℤ) = d.m := pin_m hchk.hA hchk.hC8 hchk.hC9a hchk.hC9b hloZ hhiZ
  -- conclusions (steps 5–6)
  constructor
  · intro hm
    have hZ1' : 1 ≤ Z := by omega
    obtain ⟨ρ, hρmem, hρ0⟩ := hZ1 hZ1'
    obtain ⟨hr1, hr2, hi1, hi2⟩ := hρmem
    exact ⟨ρ, hρ0, lt_trans hhalf hr1, lt_trans hr2 hs2lt1, hi1, hi2⟩
  · intro hm
    have hZ0' : Z = 0 := by omega
    intro s hsmem
    by_cases hop : s ∈ rectOpen (sigma1 d) (sigma2 d) (T1 d) (T2 d)
    · exact hZ0 hZ0' s hop
    · exact hbnz s ⟨hsmem, hop⟩

/-! ## 11. The C11 modulus-floor by-product (FORMAT.md §5.2, derivation D6) -/

lemma checkW1Floor_spec {d : W1Data} {fl : W1Floor} (hc : checkW1Floor d fl = true) :
    checkW1 d = true ∧ 0 ≤ fl.Fn ∧ 1 ≤ fl.Fd ∧ floorRowsOK d.K fl.Fn fl.Fd d.rows = true := by
  simp only [checkW1Floor, Bool.and_eq_true, decide_eq_true_eq] at hc
  exact ⟨hc.1.1.1, hc.1.1.2, hc.1.2, hc.2⟩

lemma floorRowsOK_mem {K Fn Fd : ℤ} : ∀ {l : List W1Row}, floorRowsOK K Fn Fd l = true →
    ∀ r ∈ l, floorRowOK K Fn Fd r = true := by
  intro l
  induction l with
  | nil => intro _ r hr; cases hr
  | cons a l ih =>
    intro h r hr
    simp only [floorRowsOK, Bool.and_eq_true] at h
    rcases List.mem_cons.mp hr with rfl | hr
    · exact h.1
    · exact ih h.2 r hr

/-- D6, coordinate step: `mdist`² bounds x² from below for any real x inside the interval. -/
lemma mdist_sq_le {lo hi : ℤ} {x : ℝ} (h1 : (lo : ℝ) ≤ x) (h2 : x ≤ hi) :
    ((mdist lo hi : ℤ) : ℝ) ^ 2 ≤ x ^ 2 := by
  have hlohi : lo ≤ hi := by exact_mod_cast le_trans h1 h2
  unfold mdist
  split_ifs with h
  · norm_num
    positivity
  · rw [not_and_or] at h
    rcases h with h | h
    · rw [not_le] at h
      have e1 : |lo| = lo := abs_of_pos h
      have e2 : |hi| = hi := abs_of_pos (lt_of_lt_of_le h hlohi)
      rw [e1, e2, min_eq_left hlohi]
      have hx : (0 : ℝ) < lo := by exact_mod_cast h
      nlinarith [mul_nonneg (by linarith : (0:ℝ) ≤ x - lo) (by linarith : (0:ℝ) ≤ x + lo)]
    · rw [not_le] at h
      have e1 : |lo| = -lo := abs_of_neg (lt_of_le_of_lt hlohi h)
      have e2 : |hi| = -hi := abs_of_neg h
      rw [e1, e2, min_eq_right (by omega : -hi ≤ -lo)]
      have hx : (hi : ℝ) < 0 := by exact_mod_cast h
      push_cast
      nlinarith [mul_nonneg (by linarith : (0:ℝ) ≤ (hi:ℝ) - x)
        (by linarith : (0:ℝ) ≤ -((hi:ℝ) + x))]

/-- **C11 floor soundness** (FORMAT.md §5.2, derivation D6): an accepted floor variant
certifies the boundary-modulus floor |f| ≥ Fn/Fd on all of ∂R, under H-ENCL(a).  A certified
by-product for other components (M2a's `BarrierCert` t-interpolation, screen sensitivity);
never load-bearing for the W1 conclusion, and — like the checker arithmetic — generic in f. -/
theorem floor_of_checkW1Floor {f : ℂ → ℂ} (d : W1Data) (fl : W1Floor)
    (hc : checkW1Floor d fl = true) (hEncl : W1EnclOK f d) :
    ∀ s ∈ W1Bdry d, (fl.Fn : ℝ) / fl.Fd ≤ ‖f s‖ := by
  obtain ⟨hc1, hFn, hFd, hrows⟩ := checkW1Floor_spec hc
  have hchk := checksOK_of_checkW1 hc1
  intro s hs
  obtain ⟨zw, hzw, t, ht0, ht1, hpt⟩ := bdry_cover hchk s hs
  obtain ⟨row, hrow, hR⟩ := forall₂_mem_right hEncl zw hzw
  have hOK := floorRowsOK_mem hrows row hrow
  simp only [floorRowOK, decide_eq_true_eq] at hOK
  obtain ⟨⟨hre1, hre2⟩, him1, him2⟩ := hR.1 t ht0 ht1
  rw [hpt] at hre1 hre2 him1 him2
  have hmre := mdist_sq_le (lo := row.reLo) (hi := row.reHi)
    (x := (d.K : ℝ) * (f s).re) hre1 hre2
  have hmim := mdist_sq_le (lo := row.imLo) (hi := row.imHi)
    (x := (d.K : ℝ) * (f s).im) him1 him2
  have hKpos : (0 : ℝ) < (d.K : ℝ) := by
    have : (1 : ℝ) ≤ (d.K : ℝ) := by exact_mod_cast hchk.hK
    linarith
  have hFdpos : (0 : ℝ) < (fl.Fd : ℝ) := by
    have : (1 : ℝ) ≤ (fl.Fd : ℝ) := by exact_mod_cast hFd
    linarith
  have hFnn : (0 : ℝ) ≤ (fl.Fn : ℝ) := by exact_mod_cast hFn
  have hnormsq : ‖f s‖ ^ 2 = (f s).re ^ 2 + (f s).im ^ 2 := by
    rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply]
    ring
  have hC11 : (fl.Fn : ℝ) ^ 2 * (d.K : ℝ) ^ 2
      ≤ (((mdist row.reLo row.reHi : ℤ) : ℝ) ^ 2 + ((mdist row.imLo row.imHi : ℤ) : ℝ) ^ 2)
        * (fl.Fd : ℝ) ^ 2 := by exact_mod_cast hOK
  have hsum : ((mdist row.reLo row.reHi : ℤ) : ℝ) ^ 2 + ((mdist row.imLo row.imHi : ℤ) : ℝ) ^ 2
      ≤ (d.K : ℝ) ^ 2 * ‖f s‖ ^ 2 := by
    rw [hnormsq]
    nlinarith [hmre, hmim]
  have hK2 : (0 : ℝ) < (d.K : ℝ) ^ 2 := by positivity
  have hkey : (fl.Fn : ℝ) ^ 2 ≤ ‖f s‖ ^ 2 * (fl.Fd : ℝ) ^ 2 := by
    have hcomb : (fl.Fn : ℝ) ^ 2 * (d.K : ℝ) ^ 2
        ≤ ((d.K : ℝ) ^ 2 * ‖f s‖ ^ 2) * (fl.Fd : ℝ) ^ 2 := by
      calc (fl.Fn : ℝ) ^ 2 * (d.K : ℝ) ^ 2
          ≤ (((mdist row.reLo row.reHi : ℤ) : ℝ) ^ 2
              + ((mdist row.imLo row.imHi : ℤ) : ℝ) ^ 2) * (fl.Fd : ℝ) ^ 2 := hC11
        _ ≤ ((d.K : ℝ) ^ 2 * ‖f s‖ ^ 2) * (fl.Fd : ℝ) ^ 2 :=
            mul_le_mul_of_nonneg_right hsum (sq_nonneg _)
    have hcomb' : (d.K : ℝ) ^ 2 * (fl.Fn : ℝ) ^ 2
        ≤ (d.K : ℝ) ^ 2 * (‖f s‖ ^ 2 * (fl.Fd : ℝ) ^ 2) := by
      nlinarith [hcomb]
    exact le_of_mul_le_mul_left hcomb' hK2
  rw [div_le_iff₀ hFdpos]
  by_contra hlt
  rw [not_le] at hlt
  nlinarith [hkey, mul_nonneg (norm_nonneg (f s)) hFdpos.le]

end W1
end Zeta23

end
