/- CHECK-O (checker-written, Session 36), second form of brief-elab-check.lean.  The first form elaborated the brief's text as
   `def … : Prop := ∀ …`; Lean's `def` elaborator abstracts proof subterms of a def body into auxiliary lemmas (`brief6._proof_1`
   for the `CharZero ℝ` argument of `normedAlgebraRat` inside the `Module ℚ ℝ` instance), so item 6 compared unequal for a reason
   that lies in the probe, not in the statement (brief-elab-diff.log).  Here the brief's literal fragments are elaborated as
   THEOREM statements — the challenge's own elaboration path — with `sorry` bodies (this file is a probe, never shipped), and the
   types are compared by Expr equality; `isDefEq` is reported as well. -/
import Challenge.ResidueRank

open Lean Meta

namespace BriefText

theorem item4 {ι : Type} (cls : ℕ → ι) (v : ι → ℝ) (κ : ℝ)
    (hA9 : ∀ n, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ cls m = cls n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (cls n)))
    (n : ℕ) (hn : 2 ≤ n) :
    {m : ℕ | IsPrimePow m ∧ cls m = cls n}.Finite := by
  sorry

theorem item5 {E : Type} [Monoid E] (φ : ℕ → E)
    (hmul : ∀ a b, φ (a * b) = φ a * φ b) (v : E → ℝ) (κ : ℝ)
    (hA9 : ∀ n, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ φ m = φ n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (φ n)))
    (p : ℕ) (hp : p.Prime) (a k : ℕ) (ha : 1 ≤ a) (hk : 1 ≤ k) :
    φ (p ^ a) ≠ φ (p ^ (a + k)) := by
  sorry

theorem item6 {ι : Type} (cls : ℕ → ι) (v : ι → ℝ) (κ : ℝ) (hκ : 0 < κ)
    (hA9 : ∀ n, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ cls m = cls n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (cls n))) :
    ¬ Module.Finite ℚ
      (Submodule.span ℚ (Set.range fun n : {n : ℕ // 2 ≤ n} => v (cls (n : ℕ)))) := by
  sorry

end BriefText

run_meta do
  for (b, c) in [(``BriefText.item4, ``ResidueRank.lemmaF_finite_fiber), (``BriefText.item5, ``ResidueRank.lemmaF_infinite_order),
                 (``BriefText.item6, ``ResidueRank.theoremR)] do
    let bt := (← getConstInfo b).type
    let ct := (← getConstInfo c).type
    let d ← isDefEq bt ct
    logInfo m!"{c}: brief's literal text (as a theorem) == challenge type: alpha {bt == ct}; isDefEq {d}"
