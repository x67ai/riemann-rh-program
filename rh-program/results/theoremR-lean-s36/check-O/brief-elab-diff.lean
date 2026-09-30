/- CHECK-O (checker-written, Session 36): where does the brief's literal item-6 text differ from the challenge's type?
   Compare binder by binder (types, binder names, binder infos) and the conclusion, printing both with pp.all. -/
import Challenge.ResidueRank

open Lean Meta

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

partial def walk (a b : Expr) (depth : Nat) : MetaM Unit := do
  match a, b with
  | .forallE n1 t1 b1 i1, .forallE n2 t2 b2 i2 =>
      logInfo m!"binder {depth}: names {n1} / {n2}; infos {repr i1} / {repr i2}; types alpha-equal: {t1 == t2}"
      if !(t1 == t2) then
        logInfo m!"  brief type: {t1}\n  chal  type: {t2}"
        let s1 ← withOptions (fun o => o.setBool `pp.all true) (ppExpr t1)
        let s2 ← withOptions (fun o => o.setBool `pp.all true) (ppExpr t2)
        logInfo m!"  brief pp.all: {s1}\n  chal  pp.all: {s2}"
      walk b1 b2 (depth + 1)
  | _, _ =>
      logInfo m!"conclusion alpha-equal: {a == b}"
      if !(a == b) then
        let s1 ← withOptions (fun o => o.setBool `pp.all true) (ppExpr a)
        let s2 ← withOptions (fun o => o.setBool `pp.all true) (ppExpr b)
        logInfo m!"  brief pp.all: {s1}\n  chal  pp.all: {s2}"

run_meta do
  for (b, c) in [(``brief5, ``ResidueRank.lemmaF_infinite_order), (``brief6, ``ResidueRank.theoremR)] do
    logInfo m!"==== {c}"
    walk (← getConstInfo b).value! (← getConstInfo c).type 0
