-- CHECK-O probe (Opus 5, Session 32): run from the clean clone with `lake env lean <this file>`.
import Solution.WeilContainmentC2One
import Solution.WeilContainmentC2
open WeilContainment

-- (1) the rung-1 statement in the brief's spelling (`∃ k,` without the type ascription) is the shipped type, by rfl.
example : (∀ (a : ℝ) (g : ℝ → ℂ), (∀ u, g (-u) = g u) → Continuous g →
    tsupport g ⊆ Set.Icc (-(Real.log 3)) (Real.log 3) → ∃ k, (∀ u, k (-u) = k u) ∧ ContDiff ℝ 2 k ∧
    tsupport k ⊆ Set.Icc (-(Real.log 3)) (Real.log 3) ∧ primeSide k = tiltedPrimeSide a g) :=
  weilContainment_c2_interpolant_log3

-- (2) the witness lands in the class Zeta23's EF_lit quantifies over (ContDiff ℝ 2 ∧ HasCompactSupport).
example (a L : ℝ) (g : ℝ → ℂ) (he : ∀ u, g (-u) = g u) (hc : Continuous g) (hs : tsupport g ⊆ Set.Icc (-L) L) :
    ∃ k : ℝ → ℂ, ContDiff ℝ 2 k ∧ HasCompactSupport k ∧ primeSide k = tiltedPrimeSide a g := by
  obtain ⟨k, -, hk2, hks, hkp⟩ := weilContainment_c2_interpolant a L g he hc hs
  exact ⟨k, hk2, IsCompact.of_isClosed_subset isCompact_Icc (isClosed_tsupport k) hks, hkp⟩

-- (3) evenness of g is not needed: the solution's general lemma has no such hypothesis.
#check @WeilContainmentC2.Proof.interpolant
#check @WeilContainmentC2One.Proof.interpolant

-- (4) axioms of the helper theorem as well.
#print axioms WeilContainmentC2.Proof.interpolant
#print axioms WeilContainmentC2One.Proof.interpolant

-- (5) the rung-1 root is literally the general lemma at L = log 3.
#print weilContainment_c2_interpolant_log3
