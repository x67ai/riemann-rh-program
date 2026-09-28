/- CHECKER probe (Opus 5, Session 30, G8/IntegralityGap). Not part of the unit; run with `lake env lean` from the clean clone.
(A) the per-atom slack is EXACTLY what (MI) consumes: (MI) holds for ANY nonnegative RATIONAL mark vector all of whose
    marks satisfy the slack (m − 1)(m − 2) ≥ 0 — no integrality used; and the integer (MI) follows from `per_atom_slack`
    as its ONLY integrality input.
(B) the pointwise identity 2 − (3m − m²) = (m − 1)(m − 2).
(C) the counterexample arithmetic, independently of the unit's proofs.
(D) axioms of the kernel facts, of GridCorner's attainment facts, and of the probe. -/
import Zeta23.PairCeiling.GridGap

open Finset Zeta23.PairCeiling

theorem checker_mi_of_slack {M : ℕ} [NeZero M] (m : ZMod M → ℚ) (hm : ∀ k, 0 ≤ m k)
    (hs : ∀ k, 0 ≤ (m k - 1) * (m k - 2)) :
    3 * (∑ k : ZMod M, m k) - (∑ k : ZMod M, (m k) ^ 2)
      ≤ 2 * ((Finset.univ.filter (fun k : ZMod M => m k ≠ 0)).card : ℚ) := by
  have pointwise : ∀ k : ZMod M, 3 * m k - (m k) ^ 2 ≤ 2 * (if m k ≠ 0 then (1 : ℚ) else 0) := by
    intro k
    by_cases h : m k = 0
    · simp [h]
    · rw [if_pos h]; nlinarith [hs k]
  calc 3 * (∑ k : ZMod M, m k) - (∑ k : ZMod M, (m k) ^ 2)
      = ∑ k : ZMod M, (3 * m k - (m k) ^ 2) := by rw [Finset.mul_sum, Finset.sum_sub_distrib]
    _ ≤ ∑ k : ZMod M, 2 * (if m k ≠ 0 then (1 : ℚ) else 0) := Finset.sum_le_sum fun k _ => pointwise k
    _ = 2 * ((Finset.univ.filter (fun k : ZMod M => m k ≠ 0)).card : ℚ) := by
        rw [← Finset.mul_sum, Finset.sum_boole]

theorem checker_mi_integer_via_slack {M : ℕ} [NeZero M] (m : ZMod M → ℤ) (hm : ∀ k, 0 ≤ m k) :
    3 * (∑ k : ZMod M, m k) - (∑ k : ZMod M, (m k) ^ 2)
      ≤ 2 * ((Finset.univ.filter (fun k : ZMod M => m k ≠ 0)).card : ℤ) := by
  have h := checker_mi_of_slack (fun k => (m k : ℚ)) (fun k => by exact_mod_cast hm k)
    (fun k => by exact_mod_cast GridGap.per_atom_slack (m k))
  simp only [ne_eq, Int.cast_eq_zero] at h
  exact_mod_cast h

theorem checker_pointwise_identity (q : ℚ) : 2 - (3 * q - q ^ 2) = (q - 1) * (q - 2) := by ring

theorem checker_arith :
    (48 : ℚ) * (4 / 3) = 64 ∧ (48 : ℚ) * (4 / 3) ^ 2 = 256 / 3 ∧ (4 / 3 : ℚ) * 64 = 256 / 3 ∧
    3 * (64 : ℚ) - 256 / 3 = 320 / 3 ∧ (320 / 3 : ℚ) > 2 * 48 ∧ 3 * (64 : ℚ) - 2 * 48 = 96 ∧ (96 : ℚ) > 256 / 3 ∧
    (64 : ℚ) * (5 / 6) = 160 / 3 ∧ (48 : ℚ) < 160 / 3 ∧ ((4 / 3 : ℚ) - 1) * (4 / 3 - 2) = -2 / 9 ∧
    (3 / 4 : ℚ) * 64 = 48 ∧ (3 / 4 : ℚ) * 64 * (16 / 9) = 4 / 3 * 64 ∧ 3 * (64 : ℚ) - 3 / 2 * 64 = 96 := by
  norm_num

#print axioms checker_mi_of_slack
#print axioms checker_mi_integer_via_slack
#print axioms checker_pointwise_identity
#print axioms checker_arith
#print axioms GridGap.fracMark_mass
#print axioms GridGap.fracMark_sq
#print axioms GridGap.fracMark_Nd
#print axioms GridGap.fracMark_nonneg
#print axioms GridCorner.attainMark_mass
#print axioms GridCorner.attainMark_sq
#print axioms GridParseval.two_mul_distinct_ge
#print axioms GridCorner.grid_corner_pointwise
#check @GridCorner.grid_corner_pointwise
#check @GridCorner.gridRow
#print GridParseval.dftMark
#print GridParseval.chi
#print GridParseval.zetaM
