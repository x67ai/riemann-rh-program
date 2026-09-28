-- CHECKER probe (D5, Session 30): Zeta23's literatureRHS prime term and the trusted `WeilContainment.primeSide` are the SAME term.
import Zeta23.ExplicitFormula
import ChallengeDeps.WeilContainment

open Complex in
example (k : ℝ → ℂ) :
    Zeta23.EF.literatureRHS k =
      Zeta23.paperFT k (I / 2) + Zeta23.paperFT k (-I / 2) - WeilContainment.primeSide k
      + (1 / (2 * Real.pi) : ℂ) * ∫ r : ℝ, Zeta23.paperFT k r * (Zeta23.EF.gammaBracket r : ℂ) := by
  rfl

-- the prime term alone, after unfolding `primeSide` once, `rfl` at REDUCIBLE transparency (a near-syntactic check)
example (k : ℝ → ℂ) :
    WeilContainment.primeSide k =
      ∑' n : ℕ, ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) * (k (Real.log n) + k (-Real.log n)) := by
  unfold WeilContainment.primeSide; with_reducible rfl

#print Zeta23.EF.literatureRHS
#print WeilContainment.primeSide
