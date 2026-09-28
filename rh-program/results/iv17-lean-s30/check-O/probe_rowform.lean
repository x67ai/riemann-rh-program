/- CHECKER probe (FIDELITY (v4)): (MI) in the paper's ROW form F1 ≥ 3M − 2N_d, over ℤ on every grid and its failure over ℚ
on the 65-site grid, each derived in two lines from the topic's Comparator-checked statements (imported from the Solution). -/
import Solution.IntegralityGap

open Finset IntegralityGap

theorem checker_mi_row_integer (n : ℕ) (m : ZMod (2 * n + 1) → ℤ) (hm : ∀ k, 0 ≤ m k) :
    ((3 * (∑ k, m k) - 2 * ((Finset.univ.filter (fun k => m k ≠ 0)).card : ℤ) : ℤ) : ℝ) ≤ gridRow n m := by
  rw [gridRow_eq]
  have := mi_holds_integer (2 * n + 1) m hm
  exact_mod_cast (by linarith : 3 * (∑ k, m k) - 2 * ((Finset.univ.filter (fun k => m k ≠ 0)).card : ℤ) ≤ ∑ k, (m k) ^ 2)

theorem checker_mi_row_fails_rational :
    ¬ ∀ (m : ZMod 65 → ℚ), (∀ k, 0 ≤ m k) →
      ((3 * (∑ k, m k) - 2 * ((Finset.univ.filter (fun k => m k ≠ 0)).card : ℚ) : ℚ) : ℝ) ≤ gridRowQ 32 m := by
  intro h
  have := h fracMark (corner_fails_rational.1)
  rw [fracMark_mass, fracMark_Nd, fracMark_row] at this
  norm_num at this

#print axioms checker_mi_row_integer
#print axioms checker_mi_row_fails_rational
