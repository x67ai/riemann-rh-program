/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and imports nothing from it: its only import is Mathlib.
-/
/-
Zeta23/ResidueRank/GenusBound.lean — two REAL-ALGEBRA statements (unit brief rh-program/results/theoremR-lean-s36/UNIT-BRIEF.md,
items 7–8; build record BUILD-NOTES.md there).  SCOPED: they are true on their face as statements about real numbers; their
reading as "no finite self-intersection of the diagonal" (the Session-36 Theorem S, rh-program/results/d4-infty-s36/) belongs
to that unit and is not asserted here.

  `theoremS_bound` — (7) if g ≥ 0, (1 + x − L)² ≤ 4g²x and (1 + x² − L)² ≤ 4g²x², then L ≤ (1 + 2g)(1 + r) with
                     r = (1 + √(1 + 8g))/2.  Route (PREDERIVATION-ERRATA E7): for g > 0, x ≥ 0 and, with s = √x,
                     L − 1 − x ≤ 2gs and 1 + x² − L ≤ 2gx, so s(s + 1)(s² − s − 2g) ≤ 0, hence s ≤ r (r² = r + 2g) and
                     L ≤ 1 + s² + 2gs ≤ 1 + r² + 2gr = (1 + 2g)(1 + r); for g = 0, L = 1 + x = 1 + x², so x ∈ {0, 1}, L ≤ 2.
                     The bound is attained at x = r², L = 1 + r² + 2gr (errata E7; not stated here);
  `theoremS`       — (8) no real g ≥ 0 and κ > 0 satisfy the two inequalities with L = log p / κ at every prime p: item (7)
                     bounds log p / κ, and there are primes above exp(κ · bound);
  `theoremS_abs`   — PREDERIVATION-ERRATA E5 kernel-checked: (8) needs no `0 ≤ g` (the hypotheses see g only through g²).
                     Program side only; not a statement of the Comparator topic.

WHAT IS NOT HERE.  No surface, no intersection form, no Castelnuovo–Severi inequality as such, no diagonal: the reading of
(7)–(8) belongs to the Session-36 unit under read; nothing about ζ or its zeros.

Trust model: proved from Mathlib alone; the three standard axioms only (program-axioms.log).
-/
import Mathlib

namespace Zeta23.ResidueRank

/-- **(7) The real-algebra core of Theorem S**: the two inequalities at `p` and `p²` bound `L` in terms of `g` alone. -/
theorem theoremS_bound (g x L : ℝ) (hg : 0 ≤ g)
    (h1 : (1 + x - L) ^ 2 ≤ 4 * g ^ 2 * x)
    (h2 : (1 + x ^ 2 - L) ^ 2 ≤ 4 * g ^ 2 * x ^ 2) :
    L ≤ (1 + 2 * g) * (1 + (1 + Real.sqrt (1 + 8 * g)) / 2) := by
  have ht0 : 0 ≤ Real.sqrt (1 + 8 * g) := Real.sqrt_nonneg _
  have ht2 : Real.sqrt (1 + 8 * g) ^ 2 = 1 + 8 * g := Real.sq_sqrt (by linarith)
  rcases hg.lt_or_eq with hgpos | hg0
  · -- g > 0
    have ht1 : 1 ≤ Real.sqrt (1 + 8 * g) := by nlinarith
    -- r := (1 + √(1 + 8g))/2 satisfies r ≥ 1 and r² = r + 2g
    obtain ⟨r, hr⟩ : ∃ r, r = (1 + Real.sqrt (1 + 8 * g)) / 2 := ⟨_, rfl⟩
    rw [← hr]
    have hr1 : 1 ≤ r := by rw [hr]; linarith
    have hr2 : r ^ 2 = r + 2 * g := by rw [hr]; nlinarith
    -- x ≥ 0, from h1
    have hx : 0 ≤ x := by
      by_contra hx
      have hneg : 4 * g ^ 2 * x < 0 :=
        mul_neg_of_pos_of_neg (by positivity) (lt_of_not_ge hx)
      nlinarith [sq_nonneg (1 + x - L)]
    obtain ⟨s, hs⟩ : ∃ s, s = Real.sqrt x := ⟨_, rfl⟩
    have hs0 : 0 ≤ s := by rw [hs]; exact Real.sqrt_nonneg x
    have hs2 : s ^ 2 = x := by rw [hs]; exact Real.sq_sqrt hx
    -- from h1: L − 1 − x ≤ 2gs;  from h2: 1 + x² − L ≤ 2gx
    have hA : L - 1 - x ≤ 2 * g * s := by
      by_contra hA
      have hA' : 2 * g * s < L - 1 - x := lt_of_not_ge hA
      have hgs : 0 ≤ 2 * g * s := by positivity
      nlinarith [mul_lt_mul_of_pos_left hA' (by linarith : (0 : ℝ) < L - 1 - x + 2 * g * s)]
    have hB : 1 + x ^ 2 - L ≤ 2 * g * x := by
      by_contra hB
      have hB' : 2 * g * x < 1 + x ^ 2 - L := lt_of_not_ge hB
      have hgx : 0 ≤ 2 * g * x := by positivity
      nlinarith [mul_lt_mul_of_pos_left hB' (by linarith : (0 : ℝ) < 1 + x ^ 2 - L + 2 * g * x)]
    -- s ≤ r
    have hsr : s ≤ r := by
      by_contra hsr
      have hrs : r < s := lt_of_not_ge hsr
      have hspos : 0 < s := by linarith
      -- s(s + 1)(s² − s − 2g) ≤ 0 from hA, hB and s² = x
      have hkey : s * (s + 1) * (s ^ 2 - s - 2 * g) ≤ 0 := by
        have : s ^ 4 - s ^ 2 - 2 * g * s ^ 2 - 2 * g * s ≤ 0 := by
          have hx2 : x ^ 2 = s ^ 4 := by rw [← hs2]; ring
          nlinarith
        nlinarith
      -- but s > r gives s² − s − 2g = (s − r)(s + r − 1) > 0
      have hq : 0 < s ^ 2 - s - 2 * g := by
        have : s ^ 2 - s - 2 * g = (s - r) * (s + r - 1) := by nlinarith
        rw [this]
        exact mul_pos (by linarith) (by linarith)
      have : 0 < s * (s + 1) * (s ^ 2 - s - 2 * g) := by positivity
      linarith
    -- L ≤ 1 + s² + 2gs ≤ 1 + r² + 2gr = (1 + 2g)(1 + r)
    nlinarith [mul_nonneg (sub_nonneg.mpr hsr) (add_nonneg hs0 (by linarith : (0 : ℝ) ≤ r)),
      mul_nonneg hg (sub_nonneg.mpr hsr)]
  · -- g = 0: L = 1 + x = 1 + x², so x ∈ {0, 1} and L ≤ 2
    subst hg0
    have e1 : 1 + x - L = 0 := by nlinarith [sq_nonneg (1 + x - L)]
    have e2 : 1 + x ^ 2 - L = 0 := by nlinarith [sq_nonneg (1 + x ^ 2 - L)]
    have hs1 : Real.sqrt (1 + 8 * 0) = 1 := by norm_num
    rw [hs1]
    nlinarith [sq_nonneg (x - 1)]

/-- **(8) Theorem S**: no real `g ≥ 0` satisfies the two inequalities at every prime. -/
theorem theoremS (κ g : ℝ) (hκ : 0 < κ) (hg : 0 ≤ g) (d : ℕ → ℝ)
    (h1 : ∀ p : ℕ, p.Prime → (1 + d p - Real.log (p : ℝ) / κ) ^ 2 ≤ 4 * g ^ 2 * d p)
    (h2 : ∀ p : ℕ, p.Prime →
      (1 + d p ^ 2 - Real.log (p : ℝ) / κ) ^ 2 ≤ 4 * g ^ 2 * d p ^ 2) : False := by
  obtain ⟨B, hB⟩ : ∃ B, B = (1 + 2 * g) * (1 + (1 + Real.sqrt (1 + 8 * g)) / 2) := ⟨_, rfl⟩
  -- a prime above exp(κ B)
  obtain ⟨p, hp_ge, hp⟩ := Nat.exists_infinite_primes (⌈Real.exp (κ * B)⌉₊ + 1)
  have hbound : Real.log (p : ℝ) / κ ≤ B := by
    rw [hB]
    exact theoremS_bound g (d p) (Real.log (p : ℝ) / κ) hg (h1 p hp) (h2 p hp)
  have hpgt : Real.exp (κ * B) < (p : ℝ) := by
    have hc := Nat.le_ceil (Real.exp (κ * B))
    have hp' : ((⌈Real.exp (κ * B)⌉₊ + 1 : ℕ) : ℝ) ≤ (p : ℝ) := by exact_mod_cast hp_ge
    push_cast at hp'
    linarith
  have hlog : κ * B < Real.log (p : ℝ) := by
    rw [← Real.log_exp (κ * B)]
    exact Real.log_lt_log (Real.exp_pos _) hpgt
  have hlt : B < Real.log (p : ℝ) / κ := by
    rw [lt_div_iff₀ hκ]
    linarith
  linarith

/-- PREDERIVATION-ERRATA E5: Theorem S needs no `0 ≤ g` — the hypotheses see `g` only through `g²`. -/
theorem theoremS_abs (κ g : ℝ) (hκ : 0 < κ) (d : ℕ → ℝ)
    (h1 : ∀ p : ℕ, p.Prime → (1 + d p - Real.log (p : ℝ) / κ) ^ 2 ≤ 4 * g ^ 2 * d p)
    (h2 : ∀ p : ℕ, p.Prime →
      (1 + d p ^ 2 - Real.log (p : ℝ) / κ) ^ 2 ≤ 4 * g ^ 2 * d p ^ 2) : False :=
  theoremS κ |g| hκ (abs_nonneg g) d (fun p hp => by rw [sq_abs]; exact h1 p hp)
    (fun p hp => by rw [sq_abs]; exact h2 p hp)

end Zeta23.ResidueRank
