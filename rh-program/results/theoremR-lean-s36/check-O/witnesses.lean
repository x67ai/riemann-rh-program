/- CHECK-O (checker-written, Session 36): the necessity counterexamples and the non-vacuity witnesses of PREDERIVATION-ERRATA §1
   and FIDELITY §1, kernel-checked as a PROBE (never shipped; not a statement of the topic).  Run from the clean clone's root:
   lake env lean <this file>.  Each `example` is closed without `sorry`. -/
import Mathlib

open ArithmeticFunction

/-! ## Necessity: the hypothesis is needed (the statement without it is false) -/

-- item 7 without `hg`: g = −1, x = 1, L = 1 satisfy h1 and h2, and the bound is (1 − 2)(1 + (1 + √(−7))/2) = −3/2 < 1.
example : ¬ ∀ g x L : ℝ, (1 + x - L) ^ 2 ≤ 4 * g ^ 2 * x → (1 + x ^ 2 - L) ^ 2 ≤ 4 * g ^ 2 * x ^ 2 →
    L ≤ (1 + 2 * g) * (1 + (1 + Real.sqrt (1 + 8 * g)) / 2) := by
  intro h
  have h' := h (-1) 1 1 (by norm_num) (by norm_num)
  rw [Real.sqrt_eq_zero_of_nonpos (by norm_num : (1 : ℝ) + 8 * -1 ≤ 0)] at h'
  norm_num at h'

-- item 8 without `hκ` (κ = 0; Lean's x / 0 = 0): d ≡ 1, g = 1 satisfy both inequalities at every prime.
example : ¬ ∀ κ g : ℝ, 0 ≤ g → ∀ d : ℕ → ℝ,
    (∀ p : ℕ, p.Prime → (1 + d p - Real.log (p : ℝ) / κ) ^ 2 ≤ 4 * g ^ 2 * d p) →
    (∀ p : ℕ, p.Prime → (1 + d p ^ 2 - Real.log (p : ℝ) / κ) ^ 2 ≤ 4 * g ^ 2 * d p ^ 2) → False := by
  intro h
  exact h 0 1 (by norm_num) (fun _ => 1) (fun p _ => by norm_num) (fun p _ => by norm_num)

-- item 2 without `hpos`: N ≡ 0 (every p divides 0; Real.log 0 = 0, so the span is ⊥, finite).
example : ¬ ∀ N : Nat.Primes → ℕ, (∀ p : Nat.Primes, (p : ℕ) ∣ N p) →
    ¬ Module.Finite ℚ (Submodule.span ℚ (Set.range fun p : Nat.Primes => Real.log ((N p : ℕ) : ℝ))) := by
  intro h
  apply h (fun _ => 0) (fun p => dvd_zero _)
  have : Submodule.span ℚ (Set.range fun _ : Nat.Primes => Real.log (((0 : ℕ) : ℕ) : ℝ)) = ⊥ := by
    rw [Submodule.span_eq_bot]
    rintro _ ⟨p, rfl⟩
    simp
  rw [this]
  infer_instance

-- item 2 without `hdvd`: N ≡ 1 (positive; Real.log 1 = 0, so the span is ⊥, finite).
example : ¬ ∀ N : Nat.Primes → ℕ, (∀ p, 0 < N p) →
    ¬ Module.Finite ℚ (Submodule.span ℚ (Set.range fun p : Nat.Primes => Real.log ((N p : ℕ) : ℝ))) := by
  intro h
  apply h (fun _ => 1) (fun p => Nat.one_pos)
  have : Submodule.span ℚ (Set.range fun _ : Nat.Primes => Real.log (((1 : ℕ) : ℕ) : ℝ)) = ⊥ := by
    rw [Submodule.span_eq_bot]
    rintro _ ⟨p, rfl⟩
    simp
  rw [this]
  infer_instance

/-! ## Non-vacuity: the hypotheses of items 4–6 are jointly satisfiable, including for κ < 0 (E1) -/

-- the fibers of `id` are singletons, so A9 at n holds with κ · v n = Λ n.
theorem hasSum_id_fiber (n : ℕ) (hn : 2 ≤ n) :
    HasSum (fun m : {m : ℕ // 2 ≤ m ∧ id m = id n} => vonMangoldt (m : ℕ)) (vonMangoldt n) := by
  have h := hasSum_single (f := fun m : {m : ℕ // 2 ≤ m ∧ id m = id n} => vonMangoldt (m : ℕ))
    (⟨n, hn, rfl⟩ : {m : ℕ // 2 ≤ m ∧ id m = id n})
    (fun b hb => absurd (Subtype.ext b.2.2) hb)
  simpa using h

-- κ = −1 < 0, v = Λ / κ: A9 holds at every n ≥ 2 (E1: κ < 0 is SATISFIABLE, not contradictory).
example : ∃ (κ : ℝ) (v : ℕ → ℝ), κ < 0 ∧ ∀ n : ℕ, 2 ≤ n →
    HasSum (fun m : {m : ℕ // 2 ≤ m ∧ id m = id n} => vonMangoldt (m : ℕ)) (κ * v (id n)) := by
  refine ⟨-1, fun n => vonMangoldt n / (-1), by norm_num, fun n hn => ?_⟩
  have h := hasSum_id_fiber n hn
  convert h using 1
  simp only [id]
  ring

-- κ = 1 > 0 (the displayed case of item 6), v = Λ: A9 holds — theoremR's hypotheses are not contradictory.
example : ∃ (κ : ℝ) (v : ℕ → ℝ), 0 < κ ∧ ∀ n : ℕ, 2 ≤ n →
    HasSum (fun m : {m : ℕ // 2 ≤ m ∧ id m = id n} => vonMangoldt (m : ℕ)) (κ * v (id n)) :=
  ⟨1, fun n => vonMangoldt n, one_pos, fun n hn => by simpa using hasSum_id_fiber n hn⟩

-- κ = 0: A9 at n = 2 is contradictory (the fiber sum contains Λ(2) = log 2 > 0 and every term is ≥ 0).
example (ι : Type) (cls : ℕ → ι) (v : ι → ℝ)
    (hA9 : ∀ n : ℕ, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ cls m = cls n} => vonMangoldt (m : ℕ)) (0 * v (cls n))) : False := by
  have h := hA9 2 le_rfl
  rw [zero_mul] at h
  have hle : vonMangoldt 2 ≤ 0 :=
    le_hasSum h (⟨2, le_rfl, rfl⟩ : {m : ℕ // 2 ≤ m ∧ cls m = cls 2}) (fun _ _ => vonMangoldt_nonneg)
  have : (0 : ℝ) < vonMangoldt 2 := by
    rw [vonMangoldt_apply_prime Nat.prime_two]; exact Real.log_pos one_lt_two
  linarith

-- item 5's hypotheses are satisfiable: E = (ℕ, ·), φ = id, v = Λ, κ = 1.
example : ∃ (φ : ℕ → ℕ) (v : ℕ → ℝ) (κ : ℝ), (∀ a b : ℕ, φ (a * b) = φ a * φ b) ∧ ∀ n : ℕ, 2 ≤ n →
    HasSum (fun m : {m : ℕ // 2 ≤ m ∧ φ m = φ n} => vonMangoldt (m : ℕ)) (κ * v (φ n)) :=
  ⟨id, fun n => vonMangoldt n, 1, fun _ _ => rfl, fun n hn => by simpa using hasSum_id_fiber n hn⟩

/-! ## Item 7: the bound is attained (errata E7) — at g = 1: r = 2, x = r² = 4, L = 1 + r² + 2gr = 9 = the bound -/
example : (1 + (4 : ℝ) - 9) ^ 2 = 4 * 1 ^ 2 * 4 ∧ (1 + (4 : ℝ) ^ 2 - 9) ^ 2 = 4 * 1 ^ 2 * 4 ^ 2 ∧
    (9 : ℝ) = (1 + 2 * 1) * (1 + (1 + Real.sqrt (1 + 8 * 1)) / 2) := by
  refine ⟨by norm_num, by norm_num, ?_⟩
  rw [show (1 : ℝ) + 8 * 1 = 3 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]
  norm_num
