/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean.
-/
/-
Zeta23/Separation/Assembly2.lean — Theorem M2's clause-6 assembly with b₁ PROVED, the clause-7 fold, and
"t ≥ 21L ⟹ (R*)" as a lemma (Session 24 item 3, Unit A `Separation6b`; contract
rh-program/results/c2-m4/PRICING-RESIDUE.md §1 Pieces 2, 3 (3-sym), 6 and §2 row A; separation note §5, §7.1, §7.2,
addendum A1; check-O §12.2, §12.3). Solution side of comparator/Challenge/{SeparationClause4b, Separation6b}.lean.

§1  clause 4 at b₁sym: `term_le_b1sym`, `inWindowNoise_le_b` — `Clause4.inWindowNoise_le` with the displayed H-b₁ replaced
    by the theorem `hb1sym` (B1Sym.lean); the relaxation 4‖B‴‖₁²/L⁴ ≤ b₁ closes at L ≥ 50 from b₁sym ≥ 4 (0.264 ≤ 4).
§2  the L-hypothesis absorptions at b₁sym: `absorb_b` — `Assembly.absorb` re-proved with log(2·b₁sym·C₁) in place of
    log(2·(87/10)·C₁); the SAME constants 39/1000 and 1/1000. The step ℓ + 73L ≤ (Lℓ)² is used in place of the old
    ℓ + 73L ≤ 2.71·(Lℓ)², and the closing step uses b₁sym·C₁ ≥ 4 only (the pricing observation §0 (i): every consumer
    wants b₁ from BELOW; verified here).
§3  `clause6_assembly_b` — `Assembly.clause6_assembly` with `hb1 : Hb1` GONE and `hL2` re-written; same conclusion.
§4  clause 7 (the tight pair; note §7.2 with check-O §12.3's corrected value): `wsum_double_plus` (the on-line point
    ⟨1/2, t⟩ contributes 0: h_f(t) = (t − t)·B̂(0)), `wsum_double_minus` (the on-line point ⟨1/2, −t⟩ with multiplicity 2
    contributes 2·(2t)²·‖B̂(−2tL)‖² = 8t²‖B̂(2tL)‖², B̂ being even — NOT the note body's 16t²), and `clause7_tight_pair`
    (the assembly's hypotheses with Z′ carrying ⟨1/2, ±t⟩ at multiplicity 2; the same conclusion — literally
    `clause6_assembly_b` applied, because Z′ is already arbitrary on-line inside the window).
§5  `rstar_of_21L`: 3 ≤ t → 50 ≤ L → 25/L ≤ δ → δ ≤ 1/2 → 21L ≤ t → Rstar t δ L, by a direct chain of tangent-line
    bounds (log s ≤ s/403 + 5 from e⁶ ≥ 403; log(1 + (c_B/2)s) ≤ log 25 + (1 + (c_B/2)s)/25 − 1; c_B ≥ 0.1429 from
    `exp_one_lt_d9`; C_B ≤ 18e² from Z ≥ 1/18, which is B_raw ≥ e^{−4/3} on |v| ≤ 1/4 and e^{4/3} ≤ e² < 9). The lower
    bound Z ≥ 1/18 is PROVED and used in this lemma's own C_B step only; it is not displayed and not exported to any
    other statement. Margin at (t, L, δ) = (1050, 50, 1/2): about 39 nats in this chain (the exact margin is 50.4, A1).
Label, binding: "Theorem M2's clause-6 assembly is a Comparator-checked theorem over `SepConfig`, modulo the displayed
H-edge, H-B‴ and H-out, on the three standard axioms, replayed by nanoda — with b₁ = ‖B′‖₁² proved, clause 7 folded, and
(R*) implied by t ≥ 21L as a proved corollary" — never "Theorem M2 is formalized".
-/
import Zeta23.Separation.Assembly
import Zeta23.Separation.B1Sym

namespace Zeta23
namespace Separation

open Complex MeasureTheory
open scoped ContDiff

noncomputable section

/-! ### §1 Clause 4 with b₁ proved -/

/-- the term of a real point, every shell: d²·‖B̂(Ld)‖² ≤ b₁sym/L² (`hb1sym` in place of the displayed H-b₁). -/
theorem term_le_b1sym {L : ℝ} (hL : 0 < L) (d : ℝ) :
    d ^ 2 * ‖paperFT (fun v => (B v : ℂ)) ((L * d : ℝ) : ℂ)‖ ^ 2 ≤ b1sym / L ^ 2 := by
  have h := hb1sym (L * d)
  rw [abs_mul, abs_of_pos hL] at h
  rw [le_div_iff₀ (by positivity)]
  have e : (L * |d| * ‖paperFT (fun v => (B v : ℂ)) ((L * d : ℝ) : ℂ)‖) ^ 2
      = d ^ 2 * ‖paperFT (fun v => (B v : ℂ)) ((L * d : ℝ) : ℂ)‖ ^ 2 * L ^ 2 := by
    rw [mul_pow, mul_pow, sq_abs]; ring
  rw [e] at h
  exact h

/-- **clause 4 with b₁ proved** (the rung `SeparationClause4b`), over raw data: 0 ≤ N ≤ 2·b₁sym·C₁·log(4 + t + R)/L²
for t ≥ 3, L ≥ 50, R ≥ 1 — modulo the displayed H-B‴ only. -/
theorem inWindowNoise_le_b {C₁ t L R : ℝ} (carrier : Set ℂ) (mult : ℂ → ℕ)
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hL : 50 ≤ L) (hR : 1 ≤ R) (hB3 : HB3) :
    0 ≤ ∑' ρ : ↥(carrier ∩ {ρ | ρ.re = 1 / 2 ∧ |ρ.im - t| ≤ R}),
        (mult ρ : ℝ) * ‖paperFT (ftest t L) (gammaOf ρ)‖ ^ 2 ∧
      ∑' ρ : ↥(carrier ∩ {ρ | ρ.re = 1 / 2 ∧ |ρ.im - t| ≤ R}),
        (mult ρ : ℝ) * ‖paperFT (ftest t L) (gammaOf ρ)‖ ^ 2
      ≤ 2 * b1sym * C₁ * Real.log (4 + t + R) / L ^ 2 := by
  have hL0 : 0 < L := by linarith
  have hb4 := four_le_b1sym
  have hb0 : 0 ≤ b1sym := by linarith
  refine ⟨tsum_nonneg fun ρ => by positivity, ?_⟩
  have hterm : ∀ ρ : ℂ, ρ.re = 1 / 2 →
      ‖paperFT (ftest t L) (gammaOf ρ)‖ ^ 2
        = (ρ.im - t) ^ 2 * ‖paperFT (fun v => (B v : ℂ)) ((L * (ρ.im - t) : ℝ) : ℂ)‖ ^ 2 := by
    intro ρ hρ
    rw [gammaOf_of_re_eq_half hρ, paperFT_ftest hL0, norm_mul, mul_pow,
      show ((L : ℂ) * ((ρ.im : ℂ) - (t : ℂ))) = ((L * (ρ.im - t) : ℝ) : ℂ) by push_cast; ring,
      ← Complex.ofReal_sub, Complex.norm_real, Real.norm_eq_abs, sq_abs]
  have key := shell_sum_le (t := t) (R := R) (a := b1sym / L ^ 2) (b := (64231 / 100) ^ 2 / L ^ 6)
    carrier mult hfin hcount
    (by linarith) (by linarith) hR (div_nonneg hb0 (by positivity)) (by positivity)
    (fun ρ => (mult ρ : ℝ) * ‖paperFT (ftest t L) (gammaOf ρ)‖ ^ 2)
    (fun ρ hρ => by
      rw [hterm ρ hρ.2.1]
      exact mul_le_mul_of_nonneg_left (term_le_b1sym hL0 _) (Nat.cast_nonneg _))
    (fun ρ hρ k hk hkd => by
      rw [hterm ρ hρ.2.1, div_div]
      exact mul_le_mul_of_nonneg_left (term_le_B3 hB3 hL0 (by exact_mod_cast hk) hkd) (Nat.cast_nonneg _))
  refine key.trans ?_
  have hℓ0 : 0 ≤ Real.log (4 + t + R) := Real.log_nonneg (by linarith)
  have hC0 : 0 ≤ C₁ := by linarith
  have hL4 : (50 : ℝ) ^ 4 ≤ L ^ 4 := pow_le_pow_left₀ (by norm_num) hL 4
  -- the relaxation 4‖B‴‖₁²/L⁴ ≤ b₁ at L ≥ 50: 0.264 ≤ 1 ≤ 4 ≤ b₁sym
  have hb : 4 * ((64231 / 100 : ℝ) ^ 2 / L ^ 6) ≤ b1sym / L ^ 2 := by
    have e : 4 * ((64231 / 100 : ℝ) ^ 2 / L ^ 6) = (4 * (64231 / 100) ^ 2 / L ^ 4) / L ^ 2 := by
      field_simp
    rw [e]
    refine div_le_div_of_nonneg_right ?_ (by positivity)
    calc 4 * (64231 / 100 : ℝ) ^ 2 / L ^ 4 ≤ 1 := by
          rw [div_le_iff₀ (by positivity)]; nlinarith [hL4]
      _ ≤ 4 := by norm_num
      _ ≤ b1sym := hb4
  calc C₁ * Real.log (4 + t + R) * (b1sym / L ^ 2 + 4 * ((64231 / 100) ^ 2 / L ^ 6))
      ≤ C₁ * Real.log (4 + t + R) * (b1sym / L ^ 2 + b1sym / L ^ 2) := by gcongr
    _ = 2 * b1sym * C₁ * Real.log (4 + t + R) / L ^ 2 := by ring

/-! ### §2 The L-hypothesis absorptions at b₁sym (the same 39/1000 and 1/1000) -/

/-- from L ≥ 25/δ and L ≥ (4/δ)(log log(3 + t) + 2log(1/δ) + log(2·b₁sym·C₁)), with U := δ²e^{δL/2}:
N = 2·b₁sym·C₁ℓ_R/L² ≤ 0.039·U, 2e^{−L} ≤ 0.001·U, and U ≥ 1 — `absorb` re-proved at b₁ = b₁sym ≥ 4, same constants. -/
theorem absorb_b {C₁ t δ L : ℝ} (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2) (hL1 : 25 / δ ≤ L)
    (hL2 : 4 / δ * (Real.log (Real.log (3 + t)) + 2 * Real.log (1 / δ) + Real.log (2 * b1sym * C₁)) ≤ L) :
    2 * b1sym * C₁ * Real.log (4 + t + 73 * L) / L ^ 2 ≤ 39 / 1000 * (δ ^ 2 * Real.exp (δ * L / 2)) ∧
      2 * Real.exp (-L) ≤ 1 / 1000 * (δ ^ 2 * Real.exp (δ * L / 2)) ∧
      1 ≤ δ ^ 2 * Real.exp (δ * L / 2) := by
  have hb4 := four_le_b1sym
  set b := b1sym with hb
  have hb0 : 0 < b := by linarith
  have hL50 : 50 ≤ L := by
    have : (50 : ℝ) ≤ 25 / δ := by rw [le_div_iff₀ hδ0]; linarith
    linarith
  have hL0 : 0 < L := by linarith
  have hC0 : 0 ≤ C₁ := by linarith
  have hbC : 0 < 2 * b * C₁ := by positivity
  set ℓ := Real.log (3 + t) with hℓ
  have hℓ1 : 138 / 100 ≤ ℓ := by
    have h4 : Real.log 4 ≤ ℓ := Real.log_le_log (by norm_num) (by linarith)
    have : Real.log 4 = 2 * Real.log 2 := by
      rw [show (4 : ℝ) = 2 ^ 2 by norm_num, Real.log_pow]; push_cast; ring
    have h2 : (69 : ℝ) / 100 < Real.log 2 := lt_trans (by norm_num) Real.log_two_gt_d9
    linarith
  have hℓ0 : 0 < ℓ := by linarith
  set Q := Real.log ℓ + 2 * Real.log (1 / δ) + Real.log (2 * b * C₁) with hQ
  have h4Q : 4 * Q ≤ δ * L := by
    have e : 4 / δ * Q * δ = 4 * Q := by field_simp
    calc 4 * Q = 4 / δ * Q * δ := e.symm
      _ ≤ L * δ := mul_le_mul_of_nonneg_right hL2 hδ0.le
      _ = δ * L := by ring
  set X := Real.exp (δ * L / 2) with hX
  have hX0 : 0 < X := Real.exp_pos _
  have hXge : ℓ ^ 2 * (1 / δ) ^ 4 * (2 * b * C₁) ^ 2 ≤ X := by
    have e : ℓ ^ 2 * (1 / δ) ^ 4 * (2 * b * C₁) ^ 2 = Real.exp (2 * Q) := by
      rw [hQ, mul_add, mul_add, Real.exp_add, Real.exp_add,
        show 2 * (2 * Real.log (1 / δ)) = ((4 : ℕ) : ℝ) * Real.log (1 / δ) by push_cast; ring,
        show 2 * Real.log ℓ = ((2 : ℕ) : ℝ) * Real.log ℓ by push_cast; ring,
        show 2 * Real.log (2 * b * C₁) = ((2 : ℕ) : ℝ) * Real.log (2 * b * C₁) by push_cast; ring,
        Real.exp_nat_mul, Real.exp_nat_mul, Real.exp_nat_mul, Real.exp_log hℓ0, Real.exp_log (by positivity),
        Real.exp_log hbC]
    rw [e, hX]
    exact Real.exp_le_exp.mpr (by linarith)
  have hU : 4 * ℓ ^ 2 * (2 * b * C₁) ^ 2 ≤ δ ^ 2 * X := by
    have h1 : 4 ≤ (1 / δ) ^ 2 := by
      rw [div_pow, one_pow, le_div_iff₀ (by positivity)]
      nlinarith
    have e : δ ^ 2 * (ℓ ^ 2 * (1 / δ) ^ 4 * (2 * b * C₁) ^ 2)
        = (δ * (1 / δ)) ^ 2 * ((1 / δ) ^ 2 * ℓ ^ 2 * (2 * b * C₁) ^ 2) := by ring
    calc 4 * ℓ ^ 2 * (2 * b * C₁) ^ 2 ≤ (1 / δ) ^ 2 * ℓ ^ 2 * (2 * b * C₁) ^ 2 := by gcongr
      _ = δ ^ 2 * (ℓ ^ 2 * (1 / δ) ^ 4 * (2 * b * C₁) ^ 2) := by
          rw [e, mul_one_div_cancel hδ0.ne', one_pow, one_mul]
      _ ≤ δ ^ 2 * X := by gcongr
  have hU1 : 1 ≤ δ ^ 2 * X := by
    have : (1 : ℝ) ≤ 4 * ℓ ^ 2 * (2 * b * C₁) ^ 2 := by
      calc (1 : ℝ) ≤ 4 * (138 / 100) ^ 2 * (2 * 4) ^ 2 * 1 ^ 2 := by norm_num
        _ ≤ 4 * ℓ ^ 2 * (2 * b) ^ 2 * C₁ ^ 2 := by gcongr
        _ = 4 * ℓ ^ 2 * (2 * b * C₁) ^ 2 := by ring
    linarith
  refine ⟨?_, ?_, hU1⟩
  · have hℓR : Real.log (4 + t + 73 * L) ≤ ℓ + 73 * L := by
      have h1 : 4 + t + 73 * L ≤ (3 + t) * Real.exp (73 * L) := by
        have := Real.add_one_le_exp (73 * L)
        calc 4 + t + 73 * L ≤ (3 + t) * (73 * L + 1) := by nlinarith
          _ ≤ (3 + t) * Real.exp (73 * L) := by gcongr
      calc Real.log (4 + t + 73 * L) ≤ Real.log ((3 + t) * Real.exp (73 * L)) :=
            Real.log_le_log (by positivity) h1
        _ = ℓ + 73 * L := by rw [Real.log_mul (by positivity) (Real.exp_pos _).ne', Real.log_exp]
    have ha : 50 * ℓ ≤ L * ℓ := mul_le_mul_of_nonneg_right hL50 hℓ0.le
    have hb' : 138 / 100 * L ≤ L * ℓ := by
      have := mul_le_mul_of_nonneg_left hℓ1 hL0.le; linarith
    have hLℓ : 69 ≤ L * ℓ := by nlinarith only [ha, hℓ1]
    have hsq : 69 * (L * ℓ) ≤ (L * ℓ) ^ 2 := by
      nlinarith only [mul_nonneg (sub_nonneg.mpr hLℓ) (by positivity : (0 : ℝ) ≤ L * ℓ)]
    -- ℓ + 73L ≤ (Lℓ)²  (in place of the old 2.71·(Lℓ)²)
    have hkey : ℓ + 73 * L ≤ L ^ 2 * ℓ ^ 2 := by
      have e : L ^ 2 * ℓ ^ 2 = (L * ℓ) ^ 2 := by ring
      rw [e]; linarith only [hsq, ha, hb', hLℓ]
    -- the constant: 2·b·C₁·(Lℓ)² ≤ (39/1000)·4ℓ²(2bC₁)²·L², since b·C₁ ≥ 4 (0.624·4 = 2.496 ≥ 2)
    have hP : 0 ≤ C₁ * (L ^ 2 * ℓ ^ 2) := by positivity
    have hbC4 : 4 ≤ b * C₁ := by nlinarith
    have hprod : 2 * b * C₁ * (L ^ 2 * ℓ ^ 2) ≤ 39 / 1000 * (4 * ℓ ^ 2 * (2 * b * C₁) ^ 2) * L ^ 2 := by
      have h1 : 4 * (b * (C₁ * (L ^ 2 * ℓ ^ 2))) ≤ (b * C₁) * (b * (C₁ * (L ^ 2 * ℓ ^ 2))) :=
        mul_le_mul_of_nonneg_right hbC4 (mul_nonneg hb0.le hP)
      nlinarith [h1, mul_nonneg hb0.le hP]
    rw [div_le_iff₀ (by positivity)]
    calc 2 * b * C₁ * Real.log (4 + t + 73 * L) ≤ 2 * b * C₁ * (ℓ + 73 * L) :=
          mul_le_mul_of_nonneg_left hℓR hbC.le
      _ ≤ 2 * b * C₁ * (L ^ 2 * ℓ ^ 2) := mul_le_mul_of_nonneg_left hkey hbC.le
      _ ≤ 39 / 1000 * (4 * ℓ ^ 2 * (2 * b * C₁) ^ 2) * L ^ 2 := hprod
      _ ≤ 39 / 1000 * (δ ^ 2 * X) * L ^ 2 := by gcongr
  · have h1 : Real.exp (-L) ≤ Real.exp (-50) := Real.exp_le_exp.mpr (by linarith)
    have h25 : (338 : ℝ) ≤ Real.exp 25 := by
      have := Real.quadratic_le_exp_of_nonneg (show (0 : ℝ) ≤ 25 by norm_num)
      linarith
    have h2 : (114244 : ℝ) ≤ Real.exp 50 := by
      rw [show (50 : ℝ) = ((2 : ℕ) : ℝ) * 25 by norm_num, Real.exp_nat_mul]
      calc (114244 : ℝ) = 338 ^ 2 := by norm_num
        _ ≤ Real.exp 25 ^ 2 := pow_le_pow_left₀ (by norm_num) h25 2
    have h3 : Real.exp (-50) ≤ 1 / 114244 := by
      rw [Real.exp_neg, one_div]
      exact inv_anti₀ (by norm_num) h2
    have h4 : 1 / 1000 ≤ 1 / 1000 * (δ ^ 2 * X) := by
      have := mul_le_mul_of_nonneg_left hU1 (by norm_num : (0 : ℝ) ≤ 1 / 1000); linarith
    linarith

/-! ### §3 The assembly with b₁ proved -/

/-- **Theorem M2, clause 6, with b₁ proved** (separation note §7.1 with the addendum's hypotheses), library form over
raw data — modulo the displayed H-B‴, H-edge and H-out (for Z and for Z′); H-b₁ is gone. -/
theorem clause6_assembly_b {C₁ t δ L : ℝ} (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
    (hL1 : 25 / δ ≤ L)
    (hL2 : 4 / δ * (Real.log (Real.log (3 + t)) + 2 * Real.log (1 / δ) + Real.log (2 * b1sym * C₁)) ≤ L)
    (hRstar : Rstar t δ L)
    (carrier : Set ℂ) (mult : ℂ → ℕ)
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (carrier' : Set ℂ) (mult' : ℂ → ℕ)
    (hfin' : ∀ T₁ T₂ : ℝ, (carrier' ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount' : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier' ∩ {ρ | |ρ.im - x| ≤ 1}, mult' ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (hZorb : orbit t δ ⊆ carrier) (hZmult : ∀ ρ ∈ orbit t δ, mult ρ = 1)
    (hZ : ∀ ρ ∈ carrier, |ρ.im - t| ≤ 73 * L → ρ ∉ orbit t δ → ρ.re = 1 / 2)
    (hZ' : ∀ ρ ∈ carrier', |ρ.im - t| ≤ 73 * L → ρ.re = 1 / 2)
    (hB3 : HB3) (hedge : Hedge)
    (houtZ : Summable (fun ρ : ↥(carrier ∩ {ρ | 73 * L < |ρ.im - t|}) => ‖wsum mult (ftest t L) ρ‖) ∧
      ‖∑' ρ : ↥(carrier ∩ {ρ | 73 * L < |ρ.im - t|}), wsum mult (ftest t L) ρ‖ ≤ Real.exp (-L))
    (houtZ' : Summable (fun ρ : ↥(carrier' ∩ {ρ | 73 * L < |ρ.im - t|}) => ‖wsum mult' (ftest t L) ρ‖) ∧
      ‖∑' ρ : ↥(carrier' ∩ {ρ | 73 * L < |ρ.im - t|}), wsum mult' (ftest t L) ρ‖ ≤ Real.exp (-L)) :
    δ ^ 2 * Real.exp (δ * L / 2)
        ≤ ‖(∑' ρ : carrier, wsum mult (ftest t L) ρ) - ∑' ρ : carrier', wsum mult' (ftest t L) ρ‖ ∧
      1 ≤ δ ^ 2 * Real.exp (δ * L / 2) := by
  obtain ⟨hN, hexp, hU1⟩ := absorb_b hC ht hδ0 hδ hL1 hL2
  refine ⟨?_, hU1⟩
  have hL50 : 50 ≤ L := by
    have : (50 : ℝ) ≤ 25 / δ := by rw [le_div_iff₀ hδ0]; linarith
    linarith
  have hL0 : 0 < L := by linarith
  have ht0 : 0 < t := by linarith
  have hδL : 25 ≤ δ * L := by
    have := (div_le_iff₀ hδ0).mp hL1; linarith
  rw [W_decomp hfin houtZ.1, W_decomp hfin' houtZ'.1, tsum_inWindow_eq, tsum_inWindow_eq]
  have hA' : (∑' ρ : ↥(carrier' ∩ {ρ | |ρ.im - t| ≤ 73 * L ∧ ρ.re ≠ 1 / 2}), wsum mult' (ftest t L) ρ) = 0 := by
    have : IsEmpty ↥(carrier' ∩ {ρ | |ρ.im - t| ≤ 73 * L ∧ ρ.re ≠ 1 / 2}) :=
      ⟨fun ρ => by obtain ⟨hc, hw, hre⟩ := ρ.2; exact hre (hZ' ρ hc hw)⟩
    exact tsum_empty
  rw [hA']
  have hAre := re_tsum_offline_le ht0 hδ0 hL0 hfin hZorb hZmult hZ
  have hbnd := rstar_exp hδ0 hRstar
  obtain ⟨hNz0, hNzle⟩ := inWindowNoise_le_b (R := 73 * L) carrier mult hfin hcount hC ht hL50 (by linarith) hB3
  obtain ⟨hNz0', _⟩ := inWindowNoise_le_b (R := 73 * L) carrier' mult' hfin' hcount' hC ht hL50 (by linarith) hB3
  have hOre := (abs_le.mp ((Complex.abs_re_le_norm _).trans houtZ.2)).2
  have hOre' := (abs_le.mp ((Complex.abs_re_le_norm _).trans houtZ'.2)).1
  have hc2 := edge_sq_ge hedge hδL
  have hc2' := mul_le_mul_of_nonneg_left hc2 (sq_nonneg δ)
  set X := Real.exp (δ * L / 2) with hX
  rw [norm_sub_rev]
  refine le_trans ?_ (Complex.re_le_norm _)
  simp only [Complex.sub_re, Complex.add_re, Complex.ofReal_re, Complex.zero_re]
  linarith [hAre, hbnd, hNzle, hN, hNz0', hOre, hOre', hc2', hexp]

/-! ### §4 Clause 7 — the tight pair (note §7.2; check-O §12.3) -/

/-- the on-line point ⟨1/2, t⟩ (γ = t) contributes nothing: h_f(t) = (t − t)·B̂(0) = 0. -/
theorem wsum_double_plus {mult : ℂ → ℕ} {t L : ℝ} (hL : 0 < L) :
    wsum mult (ftest t L) ⟨1 / 2, t⟩ = 0 := by
  have hγ : gammaOf ⟨1 / 2, t⟩ = (t : ℂ) := gammaOf_of_re_eq_half rfl
  rw [wsum, hγ, paperFT_ftest hL, sub_self, zero_mul, mul_zero, zero_mul]

/-- the double at −t: with multiplicity 2, the on-line point ⟨1/2, −t⟩ contributes 2·(2t)²·‖B̂(−2tL)‖²
(check-O §12.3's 8t²B̂(2tL)², B̂ being even; the note body's 16t² is the slip §12.3 records). -/
theorem wsum_double_minus {mult : ℂ → ℕ} {t L : ℝ} (hL : 0 < L) (hm : mult ⟨1 / 2, -t⟩ = 2) :
    wsum mult (ftest t L) ⟨1 / 2, -t⟩
      = ((2 * (2 * t) ^ 2 * ‖paperFT (fun v => (B v : ℂ)) ((-(2 * t * L) : ℝ) : ℂ)‖ ^ 2 : ℝ) : ℂ) := by
  rw [wsum_real rfl, hm]
  have hγ : gammaOf ⟨1 / 2, -t⟩ = ((-t : ℝ) : ℂ) := gammaOf_of_re_eq_half rfl
  rw [hγ, paperFT_ftest hL, norm_mul, mul_pow,
    show ((L : ℂ) * (((-t : ℝ) : ℂ) - (t : ℂ))) = ((-(2 * t * L) : ℝ) : ℂ) by push_cast; ring,
    show (((-t : ℝ) : ℂ) - (t : ℂ)) = ((-(2 * t) : ℝ) : ℂ) by push_cast; ring,
    Complex.norm_real, Real.norm_eq_abs, sq_abs]
  push_cast; ring

set_option linter.unusedVariables false in
/-- **Theorem M2, clause 7 (the tight pair)**, library form: the assembly's hypotheses with Z′ carrying the on-line
double at ±t (multiplicity 2 at ⟨1/2, t⟩ and at ⟨1/2, −t⟩); the same conclusion — `clause6_assembly_b` applied, since
Z′ is already arbitrary on-line inside the window (note §7.2: "nothing else changes"); the double's accounting is
`wsum_double_plus` (0 at +t) and `wsum_double_minus` (2·(2t)²‖B̂(−2tL)‖² at −t). -/
theorem clause7_tight_pair {C₁ t δ L : ℝ} (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
    (hL1 : 25 / δ ≤ L)
    (hL2 : 4 / δ * (Real.log (Real.log (3 + t)) + 2 * Real.log (1 / δ) + Real.log (2 * b1sym * C₁)) ≤ L)
    (hRstar : Rstar t δ L)
    (carrier : Set ℂ) (mult : ℂ → ℕ)
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (carrier' : Set ℂ) (mult' : ℂ → ℕ)
    (hfin' : ∀ T₁ T₂ : ℝ, (carrier' ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount' : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier' ∩ {ρ | |ρ.im - x| ≤ 1}, mult' ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (hZorb : orbit t δ ⊆ carrier) (hZmult : ∀ ρ ∈ orbit t δ, mult ρ = 1)
    (hZ : ∀ ρ ∈ carrier, |ρ.im - t| ≤ 73 * L → ρ ∉ orbit t δ → ρ.re = 1 / 2)
    (hZ' : ∀ ρ ∈ carrier', |ρ.im - t| ≤ 73 * L → ρ.re = 1 / 2)
    (hZ'plus : (⟨1 / 2, t⟩ : ℂ) ∈ carrier') (hZ'minus : (⟨1 / 2, -t⟩ : ℂ) ∈ carrier')
    (hZ'plus2 : mult' ⟨1 / 2, t⟩ = 2) (hZ'minus2 : mult' ⟨1 / 2, -t⟩ = 2)
    (hB3 : HB3) (hedge : Hedge)
    (houtZ : Summable (fun ρ : ↥(carrier ∩ {ρ | 73 * L < |ρ.im - t|}) => ‖wsum mult (ftest t L) ρ‖) ∧
      ‖∑' ρ : ↥(carrier ∩ {ρ | 73 * L < |ρ.im - t|}), wsum mult (ftest t L) ρ‖ ≤ Real.exp (-L))
    (houtZ' : Summable (fun ρ : ↥(carrier' ∩ {ρ | 73 * L < |ρ.im - t|}) => ‖wsum mult' (ftest t L) ρ‖) ∧
      ‖∑' ρ : ↥(carrier' ∩ {ρ | 73 * L < |ρ.im - t|}), wsum mult' (ftest t L) ρ‖ ≤ Real.exp (-L)) :
    δ ^ 2 * Real.exp (δ * L / 2)
        ≤ ‖(∑' ρ : carrier, wsum mult (ftest t L) ρ) - ∑' ρ : carrier', wsum mult' (ftest t L) ρ‖ ∧
      1 ≤ δ ^ 2 * Real.exp (δ * L / 2) :=
  clause6_assembly_b hC ht hδ0 hδ hL1 hL2 hRstar carrier mult hfin hcount carrier' mult' hfin' hcount'
    hZorb hZmult hZ hZ' hB3 hedge houtZ houtZ'

/-! ### §5 "t ≥ 21L ⟹ (R*)" as a lemma (addendum A1's statement; a direct chain, not A1's δ-monotonicity) -/

/-- log s ≤ s/403 + 5 for s > 0 (the tangent line of log at e⁶, with e⁶ ≥ 403 from `exp_one_gt_d9`). -/
theorem log_le_div_403_add_five {s : ℝ} (hs : 0 < s) : Real.log s ≤ s / 403 + 5 := by
  have h1 : Real.log s = Real.log (s / Real.exp 6) + 6 := by
    rw [Real.log_div hs.ne' (Real.exp_pos _).ne', Real.log_exp]; ring
  have h2 := Real.log_le_sub_one_of_pos (div_pos hs (Real.exp_pos 6))
  have h403 : (403 : ℝ) ≤ Real.exp 6 := by
    have e1 := Real.exp_one_gt_d9
    rw [show (6 : ℝ) = ((6 : ℕ) : ℝ) * 1 by norm_num, Real.exp_nat_mul]
    calc (403 : ℝ) ≤ (2.7182818283 : ℝ) ^ 6 := by norm_num
      _ ≤ Real.exp 1 ^ 6 := pow_le_pow_left₀ (by norm_num) e1.le 6
  have h3 : s / Real.exp 6 ≤ s / 403 := div_le_div_of_nonneg_left hs.le (by norm_num) h403
  linarith

/-- c_B = 2/√(72e) ≥ 0.1429 (from e < 2.7182818286). -/
theorem cB_ge : 1429 / 10000 ≤ cB := by
  unfold cB
  have hs0 : 0 < Real.sqrt (72 * Real.exp 1) := Real.sqrt_pos.mpr (by positivity)
  have hsq : Real.sqrt (72 * Real.exp 1) ≤ 20000 / 1429 := by
    rw [Real.sqrt_le_left (by norm_num)]
    have := Real.exp_one_lt_d9
    linarith
  rw [le_div_iff₀ hs0]
  linarith

/-- B_raw ≥ e^{−4/3} on |v| ≤ 1/4 (there 1 − 4v² ≥ 3/4). -/
theorem exp_neg_four_thirds_le_Braw {v : ℝ} (hv : |v| ≤ 1 / 4) : Real.exp (-4 / 3) ≤ Braw v := by
  have hv' : |v| < 1 / 2 := by linarith
  rw [Braw_of_abs_lt hv']
  apply Real.exp_le_exp.mpr
  have h := abs_le.mp hv
  have hg : 3 / 4 ≤ 1 - 4 * v ^ 2 := by nlinarith
  have hg0 : 0 < 1 - 4 * v ^ 2 := by linarith
  rw [le_div_iff₀ hg0]
  linarith

/-- Z ≥ 1/18: ∫_{−1/4}^{1/4} B_raw ≥ (1/2)·e^{−4/3} ≥ 1/18 (e^{4/3} ≤ e² < 9). PROVED, for `rstar_of_21L`'s C_B step
only; not displayed anywhere. -/
theorem one_div_eighteen_le_Z : 1 / 18 ≤ Z := by
  have hexp : 1 / 9 ≤ Real.exp (-4 / 3) := by
    have h3 := Real.exp_one_lt_three
    have h2 : Real.exp 2 ≤ 9 := by
      rw [show (2 : ℝ) = ((2 : ℕ) : ℝ) * 1 by norm_num, Real.exp_nat_mul]
      calc Real.exp 1 ^ 2 ≤ 3 ^ 2 := pow_le_pow_left₀ (Real.exp_pos _).le h3.le 2
        _ = 9 := by norm_num
    have h43 : Real.exp (4 / 3) ≤ 9 := (Real.exp_le_exp.mpr (by norm_num)).trans h2
    rw [show (-4 / 3 : ℝ) = -(4 / 3) by norm_num, Real.exp_neg, one_div]
    exact inv_anti₀ (Real.exp_pos _) h43
  have hmono : ∫ v in (-1 / 4 : ℝ)..(1 / 4), Braw v ≤ ∫ v in (-1 / 2 : ℝ)..(1 / 2), Braw v :=
    intervalIntegral.integral_mono_interval (by norm_num) (by norm_num) (by norm_num)
      (Filter.Eventually.of_forall fun v => Braw_nonneg v) (Braw_continuous.intervalIntegrable _ _)
  have hlow : ∫ _ in (-1 / 4 : ℝ)..(1 / 4), Real.exp (-4 / 3) ≤ ∫ v in (-1 / 4 : ℝ)..(1 / 4), Braw v :=
    intervalIntegral.integral_mono_on (by norm_num) (continuous_const.intervalIntegrable _ _)
      (Braw_continuous.intervalIntegrable _ _)
      (fun x hx => exp_neg_four_thirds_le_Braw (abs_le.mpr ⟨by linarith [hx.1], hx.2⟩))
  rw [intervalIntegral.integral_const, smul_eq_mul] at hlow
  unfold Z
  linarith

/-- log C_B ≤ log 25 + 2 (C_B = e²/Z ≤ 18e²). -/
theorem log_CB_le : Real.log CB ≤ Real.log 25 + 2 := by
  have hZ := Z_pos
  have h18 := one_div_eighteen_le_Z
  have hCB : CB ≤ 18 * Real.exp 1 ^ 2 := by
    unfold CB
    rw [div_le_iff₀ hZ]
    have : 18 * Real.exp 1 ^ 2 * (1 / 18) ≤ 18 * Real.exp 1 ^ 2 * Z := by gcongr
    linarith
  calc Real.log CB ≤ Real.log (18 * Real.exp 1 ^ 2) := Real.log_le_log CB_pos hCB
    _ = Real.log 18 + 2 := by
        rw [Real.log_mul (by norm_num) (by positivity), Real.log_pow, Real.log_exp]; push_cast; ring
    _ ≤ Real.log 25 + 2 := by
        linarith [Real.log_le_log (by norm_num : (0 : ℝ) < 18) (by norm_num : (18 : ℝ) ≤ 25)]

/-- **"t ≥ 21L implies (R*)"** (separation note addendum A1; the record's D3 / IV.9 / C2 line 83): for t ≥ 3,
L ≥ 50, 25/L ≤ δ ≤ 1/2 and 21L ≤ t, the reflection condition `Rstar t δ L` holds. The proof is a direct chain of
tangent-line bounds with s = √(2tL) ≥ 324 (not A1's δ-monotonicity argument); the constant 21 enters Lean here only. -/
theorem rstar_of_21L {t δ L : ℝ} (ht : 3 ≤ t) (hL : 50 ≤ L) (hδ1 : 25 / L ≤ δ) (hδ : δ ≤ 1 / 2)
    (h21 : 21 * L ≤ t) : Rstar t δ L := by
  unfold Rstar
  have hL0 : 0 < L := by linarith
  have ht0 : 0 < t := by linarith
  have hδL : 25 ≤ δ * L := by have := (div_le_iff₀ hL0).mp hδ1; linarith
  have hδ0 : 0 < δ := by
    have : 0 < 25 / L := by positivity
    linarith
  have hcB := cB_pos
  have hCB := CB_pos
  set s := Real.sqrt (2 * t * L) with hs
  have hs0 : 0 ≤ s := Real.sqrt_nonneg _
  have hs2 : s ^ 2 = 2 * t * L := Real.sq_sqrt (by positivity)
  have hs324 : 324 ≤ s := by
    have h1 : (324 : ℝ) ^ 2 ≤ s ^ 2 := by rw [hs2]; nlinarith
    nlinarith [sq_nonneg (s - 324), sq_nonneg (s + 324)]
  have hspos : 0 < s := by linarith
  have hLs : 25 / 4 * L ≤ s := by
    have h1 : (25 / 4 * L) ^ 2 ≤ s ^ 2 := by rw [hs2]; nlinarith
    nlinarith [sq_nonneg (s - 25 / 4 * L), sq_nonneg (s + 25 / 4 * L)]
  -- (i) the left-hand logarithm: (4t² + δ²)C_B²/((27/20)δ²) ≤ s⁴·C_B², so log(…) ≤ 4 log s + 2 log C_B
  have hX : (4 * t ^ 2 + δ ^ 2) * CB ^ 2 / (27 / 20 * δ ^ 2) ≤ s ^ 4 * CB ^ 2 := by
    rw [div_le_iff₀ (by positivity)]
    have h1 : 4 * t ^ 2 + δ ^ 2 ≤ s ^ 4 * (27 / 20 * δ ^ 2) := by
      have e : s ^ 4 = (2 * t * L) ^ 2 := by rw [← hs2]; ring
      rw [e]
      have h2 : (25 : ℝ) ^ 2 ≤ (δ * L) ^ 2 := pow_le_pow_left₀ (by norm_num) hδL 2
      have h3 : δ ^ 2 ≤ t ^ 2 := pow_le_pow_left₀ hδ0.le (by linarith) 2
      nlinarith [sq_nonneg t, mul_nonneg (sq_nonneg t) (sub_nonneg.mpr h2)]
    calc (4 * t ^ 2 + δ ^ 2) * CB ^ 2 ≤ s ^ 4 * (27 / 20 * δ ^ 2) * CB ^ 2 :=
          mul_le_mul_of_nonneg_right h1 (sq_nonneg _)
      _ = s ^ 4 * CB ^ 2 * (27 / 20 * δ ^ 2) := by ring
  have hlogX : Real.log ((4 * t ^ 2 + δ ^ 2) * CB ^ 2 / (27 / 20 * δ ^ 2))
      ≤ 4 * Real.log s + 2 * Real.log CB := by
    have hpos : 0 < (4 * t ^ 2 + δ ^ 2) * CB ^ 2 / (27 / 20 * δ ^ 2) := by positivity
    calc Real.log ((4 * t ^ 2 + δ ^ 2) * CB ^ 2 / (27 / 20 * δ ^ 2)) ≤ Real.log (s ^ 4 * CB ^ 2) :=
          Real.log_le_log hpos hX
      _ = 4 * Real.log s + 2 * Real.log CB := by
          rw [Real.log_mul (by positivity) (by positivity), Real.log_pow, Real.log_pow]; push_cast; ring
  -- (ii) the two tangent lines and the three constants
  have hlogs := log_le_div_403_add_five hspos
  have hlogCB := log_CB_le
  have hlogc : Real.log (1 + cB / 2 * s) ≤ Real.log 25 + ((1 + cB / 2 * s) / 25 - 1) := by
    have hpos : 0 < 1 + cB / 2 * s := by positivity
    have e : Real.log (1 + cB / 2 * s) = Real.log 25 + Real.log ((1 + cB / 2 * s) / 25) := by
      rw [← Real.log_mul (by norm_num) (by positivity)]; congr 1; field_simp
    rw [e]
    linarith [Real.log_le_sub_one_of_pos (by positivity : (0 : ℝ) < (1 + cB / 2 * s) / 25)]
  have h25 := log25_le
  have hcBs : 1429 / 10000 * s ≤ cB * s := mul_le_mul_of_nonneg_right cB_ge hs0
  have hδL2 : δ * L ≤ L / 2 := by nlinarith
  -- (iii) the linear combination: about 39 nats of room at s = 324
  linarith [hlogX, hlogs, hlogCB, hlogc, h25, hcBs, hδL2, hLs, hs324]

end

end Separation
end Zeta23
