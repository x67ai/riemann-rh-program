/- CHECK-O (checker-written, Session 36): a PROBE, never shipped.  The topic's statement 5 (`ResidueRank.lemmaF_infinite_order`)
   assumes `hmul : ∀ a b : ℕ, φ (a * b) = φ a * φ b` for ALL a, b — including 0, where the NOTE's φ (a monoid map on M = ℕ≥1,
   NOTE §1.1) is not defined.  At a = 0 or b = 0, `hmul` demands φ 0 = φ 0 * φ b = φ a * φ 0 for all a, b, which a nontrivial φ into
   a group cannot meet.  This file checks that the topic's statement nevertheless IMPLIES Lemma F(b) for a φ₀ multiplicative on the
   positive integers only (no φ₀ 1 = 1 either): pass to `WithZero E₀`, send 0 to the adjoined zero.  It imports the SOLUTION (the
   proved topic theorem) and uses nothing else. -/
import Solution.ResidueRank

open ArithmeticFunction

theorem lemmaF_b_on_positive {E₀ : Type} [Monoid E₀] (φ₀ : ℕ → E₀)
    (hmul₀ : ∀ a b : ℕ, 0 < a → 0 < b → φ₀ (a * b) = φ₀ a * φ₀ b) (v₀ : E₀ → ℝ) (κ : ℝ)
    (hA9 : ∀ n : ℕ, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ φ₀ m = φ₀ n} => vonMangoldt (m : ℕ)) (κ * v₀ (φ₀ n)))
    (p : ℕ) (hp : p.Prime) (a k : ℕ) (ha : 1 ≤ a) (hk : 1 ≤ k) :
    φ₀ (p ^ a) ≠ φ₀ (p ^ (a + k)) := by
  classical
  let φ : ℕ → WithZero E₀ := fun n => if n = 0 then 0 else ((φ₀ n : E₀) : WithZero E₀)
  have hφ : ∀ n, n ≠ 0 → φ n = ((φ₀ n : E₀) : WithZero E₀) := fun n hn => if_neg hn
  have hmul : ∀ a b : ℕ, φ (a * b) = φ a * φ b := by
    intro a b
    rcases Nat.eq_zero_or_pos a with rfl | ha
    · simp [φ]
    rcases Nat.eq_zero_or_pos b with rfl | hb
    · simp [φ]
    rw [hφ _ (Nat.mul_pos ha hb).ne', hφ _ ha.ne', hφ _ hb.ne', hmul₀ a b ha hb, WithZero.coe_mul]
  let v : WithZero E₀ → ℝ := fun e => Option.elim e 0 v₀
  have hA9' : ∀ n : ℕ, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ φ m = φ n} => vonMangoldt (m : ℕ)) (κ * v (φ n)) := by
    intro n hn
    have hn0 : n ≠ 0 := by omega
    let e : {m : ℕ // 2 ≤ m ∧ φ m = φ n} ≃ {m : ℕ // 2 ≤ m ∧ φ₀ m = φ₀ n} :=
      Equiv.subtypeEquivRight fun m => by
        constructor
        · rintro ⟨h2, h⟩
          refine ⟨h2, ?_⟩
          rw [hφ m (by omega), hφ n hn0] at h
          exact WithZero.coe_injective h
        · rintro ⟨h2, h⟩
          refine ⟨h2, ?_⟩
          rw [hφ m (by omega), hφ n hn0, h]
    have h0 := hA9 n hn
    have h1 := (e.hasSum_iff (f := fun m : {m : ℕ // 2 ≤ m ∧ φ₀ m = φ₀ n} => vonMangoldt (m : ℕ))).mpr h0
    have hv : v (φ n) = v₀ (φ₀ n) := by rw [hφ n hn0]; rfl
    rw [hv]
    exact h1
  have key := ResidueRank.lemmaF_infinite_order φ hmul v κ hA9' p hp a k ha hk
  intro heq
  apply key
  rw [hφ _ (pow_ne_zero _ hp.ne_zero), hφ _ (pow_ne_zero _ hp.ne_zero), heq]

#print axioms lemmaF_b_on_positive

/-- The index-0 demand is a real constraint: for φ into a group with φ 2 ≠ 1, `hmul` at (0, 2) fails. -/
example {G : Type} [Group G] (φ : ℕ → G) (h2 : φ 2 ≠ 1) : ¬ ∀ a b : ℕ, φ (a * b) = φ a * φ b := by
  intro hmul
  have := hmul 0 2
  rw [zero_mul] at this
  exact h2 (by simpa using this)
