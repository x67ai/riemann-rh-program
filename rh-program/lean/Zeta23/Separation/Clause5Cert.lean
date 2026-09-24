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
Zeta23/Separation/Clause5Cert.lean — Unit B leg 1(b) (rh-program/results/c2-m4/PRICING-RESIDUE.md §1 Piece 1 item 11):
the one-point check H-R₀ of addendum A3 — F₁₃(50; 73) ≤ 0 and 5/(2c_B√73 − 13/8) ≤ 50 — PROVED (`F13_50_neg : HR0`) from
rational enclosures of the constants and one finite rational inequality checked by `norm_num` (the `NumericCert`
discipline).  The enclosures: e ∈ [2.7182818283, 2.7182818286] (`Real.exp_one_gt_d9`, `exp_one_lt_d9`); c_B = 2/√(72e)
∈ [c_lo, c_hi] (width 2·10⁻¹⁰, `Real.sqrt_le_left`, `Real.le_sqrt`); √73 ∈ [r_lo, r_hi] (width 2·10⁻¹⁰); Z ∈ [421/2000,
233651/10⁶] (ZEnclosure.lean, 16 cells per half); hence C_B = e²/Z ≤ e_hi²/Z_lo and b₁sym = (2e^{−1}/Z)² ≥ (2/(e_hi Z_hi))².
Every monomial of P₂, P₃ is monotone in c_B (up in the prefactors, down through a = 2c_B in γ_n), in C_B (up) and in
√73 (up) (`gammaPoly_le`, `Prelax_50_le`), so 1.05P₂(50) + P₃(50) ≤ Q_hi with the endpoints substituted; then
F₁₃(50) ≤ 0 ⟸ Q_hi/b₁_lo ≤ e^{E_lo}, E_lo := 100c_lo r_lo − 325/4 − 2c_hi/r_lo ≤ 2c_B√73·50 − 13/8·50 − 2c_B/√73
(`Real.log_le_iff_le_exp`), and e^{E_lo} = e^{40}·e^{E_lo − 40} ≥ e_lo⁴⁰·Σ_{i<6}(E_lo − 40)^i/i! (`Real.exp_nat_mul`,
`Real.sum_le_exp_of_nonneg`).  The margin: F₁₃(50) at the endpoints is −0.347 (rh-program/results/c2-m4/verify-B/
cert-numbers.log; the pricing's −0.349), against the script's −0.3227 at the record's b₁ = 8.698 and −0.556 at b₁sym.
The second conjunct holds with 2c_B√73 − 13/8 ≥ 2c_lo r_lo − 13/8 = 0.818 ≥ 1/10.  Nothing here is about ζ or RH.
-/
import Zeta23.Separation.Clause5
import Zeta23.Separation.ZEnclosure

namespace Zeta23
namespace Separation

noncomputable section

/-! ### §1 The rational enclosures -/

/-- e_lo = 2.7182818283 (`Real.exp_one_gt_d9`). -/
def eLo : ℝ := 27182818283 / 10000000000
/-- e_hi = 2.7182818286 (`Real.exp_one_lt_d9`). -/
def eHi : ℝ := 13591409143 / 5000000000
/-- c_lo ≤ c_B = 2/√(72e). -/
def cLo : ℝ := 14296064739 / 100000000000
/-- c_B ≤ c_hi. -/
def cHi : ℝ := 14296064759 / 100000000000
/-- r_lo ≤ √73. -/
def rLo : ℝ := 427200187261 / 50000000000
/-- √73 ≤ r_hi. -/
def rHi : ℝ := 427200187271 / 50000000000
/-- Z_lo (ZEnclosure.lean). -/
def ZLo : ℝ := 421 / 2000
/-- Z_hi (ZEnclosure.lean). -/
def ZHi : ℝ := 233651 / 1000000
/-- C_B ≤ e_hi²/Z_lo. -/
def CBHi : ℝ := eHi ^ 2 / ZLo
/-- b₁sym ≥ (2/(e_hi Z_hi))². -/
def b1Lo : ℝ := (2 / (eHi * ZHi)) ^ 2

theorem eLo_le : eLo ≤ Real.exp 1 := by
  have h := Real.exp_one_gt_d9; unfold eLo; norm_num at h ⊢; linarith

theorem le_eHi : Real.exp 1 ≤ eHi := by
  have h := Real.exp_one_lt_d9; unfold eHi; norm_num at h ⊢; linarith

theorem cB_bounds : cLo ≤ cB ∧ cB ≤ cHi := by
  have he1 := eLo_le
  have he2 := le_eHi
  have he0 := Real.exp_pos 1
  have h72 : 0 < 72 * Real.exp 1 := by positivity
  have hs : 0 < Real.sqrt (72 * Real.exp 1) := Real.sqrt_pos.mpr h72
  unfold cB
  constructor
  · rw [le_div_iff₀ hs]
    have h : Real.sqrt (72 * Real.exp 1) ≤ 2 / cLo := by
      rw [Real.sqrt_le_left (by unfold cLo; norm_num)]
      unfold eHi at he2; unfold cLo; norm_num at he2 ⊢; linarith
    have hcLo : 0 < cLo := by unfold cLo; norm_num
    calc cLo * Real.sqrt (72 * Real.exp 1) ≤ cLo * (2 / cLo) := by gcongr
      _ = 2 := by field_simp
  · rw [div_le_iff₀ hs]
    have h : 2 / cHi ≤ Real.sqrt (72 * Real.exp 1) := by
      rw [Real.le_sqrt (by unfold cHi; norm_num) h72.le]
      unfold eLo at he1; unfold cHi; norm_num at he1 ⊢; linarith
    have hcHi : 0 < cHi := by unfold cHi; norm_num
    calc (2 : ℝ) = cHi * (2 / cHi) := by field_simp
      _ ≤ cHi * Real.sqrt (72 * Real.exp 1) := by gcongr

theorem sqrt73_bounds : rLo ≤ Real.sqrt 73 ∧ Real.sqrt 73 ≤ rHi := by
  constructor
  · rw [Real.le_sqrt (by unfold rLo; norm_num) (by norm_num)]; unfold rLo; norm_num
  · rw [Real.sqrt_le_left (by unfold rHi; norm_num)]; unfold rHi; norm_num

theorem CB_le_CBHi : CB ≤ CBHi := by
  have hZ := Z_enclosure.1
  have hZ0 := Z_pos
  have he := le_eHi
  have he0 := Real.exp_pos 1
  unfold CB CBHi
  have hZLo : 0 < ZLo := by unfold ZLo; norm_num
  calc Real.exp 1 ^ 2 / Z ≤ eHi ^ 2 / Z := by gcongr
    _ ≤ eHi ^ 2 / ZLo := by
        unfold ZLo at hZLo ⊢
        exact div_le_div_of_nonneg_left (by positivity) hZLo hZ

theorem b1Lo_le_b1sym : b1Lo ≤ b1sym := by
  have hZ := Z_enclosure.2
  have hZ0 := Z_pos
  have he := le_eHi
  have he0 := Real.exp_pos 1
  unfold b1sym b1Lo
  have e1 : 2 * Real.exp (-1) / Z = 2 / (Real.exp 1 * Z) := by
    rw [Real.exp_neg]; field_simp
  have hZHi : 0 < ZHi := by unfold ZHi; norm_num
  have heHi : 0 < eHi := by unfold eHi; norm_num
  have h1 : 2 / (eHi * ZHi) ≤ 2 * Real.exp (-1) / Z := by
    rw [e1]
    refine div_le_div_of_nonneg_left (by norm_num) (by positivity) ?_
    unfold ZHi at hZ ⊢
    exact mul_le_mul he hZ hZ0.le heHi.le
  exact pow_le_pow_left₀ (by positivity) h1 2

/-! ### §2 The monotone substitution of the endpoints into P₂(50), P₃(50) -/

/-- γ_n is antitone in a and monotone in s. -/
theorem gammaPoly_le (n : ℕ) {a a' s s' : ℝ} (ha' : 0 < a') (haa : a' ≤ a) (hs : 0 ≤ s) (hss : s ≤ s') :
    gammaPoly n a s ≤ gammaPoly n a' s' := by
  have hs' : 0 ≤ s' := le_trans hs hss
  unfold gammaPoly
  refine Finset.sum_le_sum fun j _ => ?_
  gcongr

/-- P_m(50) with the endpoints substituted: C_B → C_B,hi, c_B → c_hi in the prefactors and c_lo in a = 2c_B, √73 → r_hi. -/
def PrelaxQ (m : ℕ) : ℝ :=
  (1 + 3 / (2 * (73 * 50 - 1))) ^ m * CBHi ^ 2 *
    ((73 * 50) ^ m * (1 + cHi / 2 * (rHi * 50)) ^ 2 +
      2 / 50 ^ (m + 1) * (gammaPoly (2 * m + 1) (2 * cLo) (rHi * 50)
        + cHi * gammaPoly (2 * m + 2) (2 * cLo) (rHi * 50)
        + cHi ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cLo) (rHi * 50)))

theorem Prelax_50_le (m : ℕ) : Prelax m 50 ≤ PrelaxQ m := by
  obtain ⟨hc1, hc2⟩ := cB_bounds
  obtain ⟨hr1, hr2⟩ := sqrt73_bounds
  have hCB := CB_le_CBHi
  have hc := cB_pos
  have hC := CB_pos
  have h73 := Real.sqrt_nonneg 73
  have hcLo : 0 < cLo := by unfold cLo; norm_num
  have hcHi : 0 ≤ cHi := by unfold cHi; norm_num
  have hrHi : 0 ≤ rHi := by unfold rHi; norm_num
  have hs : 0 ≤ Real.sqrt 73 * 50 := by positivity
  have hsr : Real.sqrt 73 * 50 ≤ rHi * 50 := by linarith
  have hg1 := gammaPoly_le (2 * m + 1) (a := 2 * cB) (a' := 2 * cLo) (by positivity) (by linarith) hs hsr
  have hg2 := gammaPoly_le (2 * m + 2) (a := 2 * cB) (a' := 2 * cLo) (by positivity) (by linarith) hs hsr
  have hg3 := gammaPoly_le (2 * m + 3) (a := 2 * cB) (a' := 2 * cLo) (by positivity) (by linarith) hs hsr
  have hg10 := gammaPoly_nonneg (2 * m + 1) (a := 2 * cB) (s := Real.sqrt 73 * 50) (by positivity) hs
  have hg20 := gammaPoly_nonneg (2 * m + 2) (a := 2 * cB) (s := Real.sqrt 73 * 50) (by positivity) hs
  have hg30 := gammaPoly_nonneg (2 * m + 3) (a := 2 * cB) (s := Real.sqrt 73 * 50) (by positivity) hs
  unfold Prelax PrelaxQ
  gcongr

/-! ### §3 The finite rational inequality and the exponential lower bound -/

/-- E_lo := 100c_lo r_lo − (13/8)·50 − 2c_hi/r_lo ≤ 2c_B√73·50 − (13/8)·50 − 2c_B/√73. -/
def ELo : ℝ := 50 * (2 * cLo * rLo) - 13 / 8 * 50 - 2 * cHi / rLo

/-- **the certificate inequality**, one finite inequality over ℚ: Q_hi/b₁_lo ≤ e_lo⁴⁰·Σ_{i<6}(E_lo − 40)^i/i!. -/
theorem cert_numeric :
    (105 / 100 * PrelaxQ 2 + PrelaxQ 3) / b1Lo
      ≤ eLo ^ 40 * ∑ i ∈ Finset.range 6, (ELo - 40) ^ i / (i.factorial : ℝ) := by
  unfold PrelaxQ b1Lo ELo CBHi
  unfold cLo cHi rLo rHi eLo eHi ZLo ZHi gammaPoly
  simp only [Finset.sum_range_succ, Finset.sum_range_zero]
  norm_num [Nat.factorial]

theorem exp_ELo_ge : eLo ^ 40 * ∑ i ∈ Finset.range 6, (ELo - 40) ^ i / (i.factorial : ℝ) ≤ Real.exp ELo := by
  have hE : 0 ≤ ELo - 40 := by unfold ELo cLo cHi rLo; norm_num
  have heLo : 0 ≤ eLo := by unfold eLo; norm_num
  have h1 : eLo ^ 40 ≤ Real.exp 40 := by
    rw [show (40 : ℝ) = ((40 : ℕ) : ℝ) * 1 by norm_num, Real.exp_nat_mul]
    exact pow_le_pow_left₀ heLo eLo_le 40
  have h2 : ∑ i ∈ Finset.range 6, (ELo - 40) ^ i / (i.factorial : ℝ) ≤ Real.exp (ELo - 40) :=
    Real.sum_le_exp_of_nonneg hE 6
  calc eLo ^ 40 * ∑ i ∈ Finset.range 6, (ELo - 40) ^ i / (i.factorial : ℝ)
      ≤ Real.exp 40 * Real.exp (ELo - 40) := mul_le_mul h1 h2 (by positivity) (Real.exp_pos _).le
    _ = Real.exp ELo := by rw [← Real.exp_add]; ring_nf

/-! ### §4 H-R₀ discharged -/

/-- **H-R₀ is a theorem**: F₁₃(50; 73) ≤ 0 and 5/(2c_B√73 − 13/8) ≤ 50 (addendum A3's one-point check). -/
theorem F13_50_neg : HR0 := by
  obtain ⟨hc1, hc2⟩ := cB_bounds
  obtain ⟨hr1, hr2⟩ := sqrt73_bounds
  have hb1 := b1Lo_le_b1sym
  have hb4 := four_le_b1sym
  have hb0 : 0 < b1sym := by linarith
  have hc := cB_pos
  have h73 : 0 < Real.sqrt 73 := Real.sqrt_pos.mpr (by norm_num)
  have hcLo : 0 < cLo := by unfold cLo; norm_num
  have hrLo : 0 < rLo := by unfold rLo; norm_num
  have hprod : 2 * cLo * rLo ≤ 2 * cB * Real.sqrt 73 := by
    have := mul_le_mul hc1 hr1 hrLo.le hc.le
    linarith
  constructor
  · unfold F13
    have hQle : 105 / 100 * P2 50 + P3 50 ≤ 105 / 100 * PrelaxQ 2 + PrelaxQ 3 := by
      unfold P2 P3; linarith [Prelax_50_le 2, Prelax_50_le 3]
    have hQ0 : 0 < 105 / 100 * P2 50 + P3 50 := by
      have := Prelax_pos 2 (L := 50) (by norm_num)
      have := Prelax_pos 3 (L := 50) (by norm_num)
      unfold P2 P3; positivity
    have hb1Lo : 0 < b1Lo := by unfold b1Lo eHi ZHi; norm_num
    have hQhi : 0 ≤ 105 / 100 * PrelaxQ 2 + PrelaxQ 3 := le_trans hQ0.le hQle
    have hlog : Real.log ((105 / 100 * P2 50 + P3 50) / b1sym) ≤ ELo := by
      rw [Real.log_le_iff_le_exp (by positivity)]
      calc (105 / 100 * P2 50 + P3 50) / b1sym ≤ (105 / 100 * PrelaxQ 2 + PrelaxQ 3) / b1Lo := by
            gcongr
        _ ≤ eLo ^ 40 * ∑ i ∈ Finset.range 6, (ELo - 40) ^ i / (i.factorial : ℝ) := cert_numeric
        _ ≤ Real.exp ELo := exp_ELo_ge
    have hlin : (13 / 8 - 2 * cB * Real.sqrt 73) * 50 + 2 * cB / Real.sqrt 73 ≤ -ELo := by
      unfold ELo
      have h2 : 2 * cB / Real.sqrt 73 ≤ 2 * cHi / rLo := by
        rw [div_le_div_iff₀ h73 hrLo]
        have := mul_le_mul hc2 hr1 hrLo.le (by unfold cHi; norm_num)
        linarith
      linarith
    linarith
  · have hslope := slope_pos
    rw [div_le_iff₀ hslope]
    unfold cLo rLo at hprod
    norm_num at hprod
    linarith

end

end Separation
end Zeta23
