import Zeta23.W1.FDH
open HurwitzZeta Zeta23.W1
-- Job 2: the shift-cast check (pricing risk R3). If `((j/5 : ℝ) : UnitAddCircle)` were anything
-- other than the real j/5 mod 1, these four would not elaborate: `hasSum_hurwitzZeta_of_one_lt_re`
-- fixes `a : ℝ` and demands `a ∈ Icc 0 1`, then talks about `hurwitzZeta (a : UnitAddCircle)`.
example {s : ℂ} (hs : 1 < s.re) :
    HasSum (fun n : ℕ ↦ 1 / (n + (1/5 : ℝ) : ℂ) ^ s) (hurwitzZeta ((1/5 : ℝ) : UnitAddCircle) s) :=
  hasSum_hurwitzZeta_of_one_lt_re (by norm_num) hs
example {s : ℂ} (hs : 1 < s.re) :
    HasSum (fun n : ℕ ↦ 1 / (n + (2/5 : ℝ) : ℂ) ^ s) (hurwitzZeta ((2/5 : ℝ) : UnitAddCircle) s) :=
  hasSum_hurwitzZeta_of_one_lt_re (by norm_num) hs
example {s : ℂ} (hs : 1 < s.re) :
    HasSum (fun n : ℕ ↦ 1 / (n + (3/5 : ℝ) : ℂ) ^ s) (hurwitzZeta ((3/5 : ℝ) : UnitAddCircle) s) :=
  hasSum_hurwitzZeta_of_one_lt_re (by norm_num) hs
example {s : ℂ} (hs : 1 < s.re) :
    HasSum (fun n : ℕ ↦ 1 / (n + (4/5 : ℝ) : ℂ) ^ s) (hurwitzZeta ((4/5 : ℝ) : UnitAddCircle) s) :=
  hasSum_hurwitzZeta_of_one_lt_re (by norm_num) hs
-- the four shifts are pairwise distinct in ℝ/ℤ (no accidental collapse of the casts)
example : ((1/5 : ℝ) : UnitAddCircle) ≠ ((2/5 : ℝ) : UnitAddCircle) := by
  intro h
  rw [AddCircle.coe_eq_coe_iff_of_mem_Ico (hp := ⟨by norm_num⟩) (a := (0:ℝ))] at h
  · norm_num at h
  · constructor <;> norm_num
  · constructor <;> norm_num
-- kappaDH is the FORMAT §9.2 surd, spelled out
example : kappaDH = (Real.sqrt (10 - 2 * Real.sqrt 5) - 2) / (Real.sqrt 5 - 1) := rfl
-- fDH is literally the FORMAT §9.2 combination
example : ∀ s : ℂ, fDH s = (5 : ℂ) ^ (-s) *
    (hurwitzZeta ((1/5 : ℝ) : UnitAddCircle) s + (kappaDH : ℂ) * hurwitzZeta ((2/5 : ℝ) : UnitAddCircle) s
      - (kappaDH : ℂ) * hurwitzZeta ((3/5 : ℝ) : UnitAddCircle) s - hurwitzZeta ((4/5 : ℝ) : UnitAddCircle) s) :=
  fun _ => rfl
set_option pp.numericTypes true in
#print Zeta23.W1.fDH
