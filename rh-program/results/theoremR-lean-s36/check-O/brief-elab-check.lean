/- CHECK-O (checker-written, Session 36).  UNIT-BRIEF §0 gives items 4–6 in prose; their backticked fragments differ from the
   challenge text only by the binder ascriptions `n : ℕ` (hA9 of items 4–6) and `a b : ℕ` (hmul of item 5).  Below, the brief's
   LITERAL fragments are assembled into full statements (prose filled in literally: "hA9 as in 4 with cls := φ"; "p prime";
   "for 2 ≤ n"), elaborated, and compared with the types of the challenge constants by Expr equality (`==` is alpha-equivalence;
   `Expr.equal` also compares binder names).  A `true` means the brief's text and the challenge's text denote the same term. -/
import Challenge.ResidueRank

open Lean Meta

def brief4 : Prop := ∀ {ι : Type} (cls : ℕ → ι) (v : ι → ℝ) (κ : ℝ)
    (hA9 : ∀ n, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ cls m = cls n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (cls n)))
    (n : ℕ) (hn : 2 ≤ n),
    {m : ℕ | IsPrimePow m ∧ cls m = cls n}.Finite

def brief5 : Prop := ∀ {E : Type} [Monoid E] (φ : ℕ → E)
    (hmul : ∀ a b, φ (a * b) = φ a * φ b) (v : E → ℝ) (κ : ℝ)
    (hA9 : ∀ n, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ φ m = φ n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (φ n)))
    (p : ℕ) (hp : p.Prime) (a k : ℕ) (ha : 1 ≤ a) (hk : 1 ≤ k),
    φ (p ^ a) ≠ φ (p ^ (a + k))

def brief6 : Prop := ∀ {ι : Type} (cls : ℕ → ι) (v : ι → ℝ) (κ : ℝ) (hκ : 0 < κ)
    (hA9 : ∀ n, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ cls m = cls n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (cls n))),
    ¬ Module.Finite ℚ
      (Submodule.span ℚ (Set.range fun n : {n : ℕ // 2 ≤ n} => v (cls (n : ℕ))))

run_meta do
  for (b, c) in [(``brief4, ``ResidueRank.lemmaF_finite_fiber), (``brief5, ``ResidueRank.lemmaF_infinite_order),
                 (``brief6, ``ResidueRank.theoremR)] do
    let bv := (← getConstInfo b).value!
    let ct := (← getConstInfo c).type
    logInfo m!"{c}: brief's literal text == challenge type (alpha): {bv == ct}; with binder names (Expr.equal): {bv.equal ct}"
