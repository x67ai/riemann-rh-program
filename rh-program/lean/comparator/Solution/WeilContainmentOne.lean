/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does not import it: it imports Mathlib only
(through ChallengeDeps.WeilContainment).
-/
/-
comparator/Solution/WeilContainmentOne.lean — the UNTRUSTED comparator solution module for the topic `WeilContainmentOne`
(rung 1 of the D5 unit): the statement of Challenge/WeilContainmentOne.lean, byte-identical, PROVED over Mathlib alone.
The proof is the term-by-term computation of the record: for n ≥ 1, `tilt a (log n) = n^(1/2 − a)` and
`(Λ n / √n) · n^(1/2 − a) = Λ n · n^(−a)`; at n = 0 both summands vanish (Λ 0 = 0); `tsum_congr` finishes.  The lemmas are
stated for every real a (namespace `WeilContainmentOne.Proof`) and instantiated at a = 1.  This module never imports the
challenge.  Nothing in this file is part of the trusted base: comparator re-checks that the theorem below has exactly the
statement of its Challenge namesake and uses only the permitted axioms.
-/
import ChallengeDeps.WeilContainment

noncomputable section

open WeilContainment

namespace WeilContainmentOne.Proof

theorem tilt_even (a u : ℝ) : tilt a (-u) = tilt a u := by
  simp [tilt, abs_neg]

theorem tilt_of_nonneg (a u : ℝ) (hu : 0 ≤ u) : tilt a u = Real.exp (-(a - 1 / 2) * u) := by
  simp [tilt, abs_of_nonneg hu]

/-- the summand identity, for every n : ℕ (n = 0 by Λ 0 = 0; n ≥ 1 by the rpow computation). -/
theorem summand_eq (a : ℝ) (g : ℝ → ℂ) (hg : ∀ u, g (-u) = g u) (n : ℕ) :
    ((ArithmeticFunction.vonMangoldt n : ℝ) : ℂ) * (((n : ℝ) ^ (-a) : ℝ) : ℂ) * g (Real.log n)
      = ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ)
          * (weilTestOf a g (Real.log n) + weilTestOf a g (-Real.log n)) := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · simp
  · have hn' : (0 : ℝ) < n := by exact_mod_cast hn
    have hlog : 0 ≤ Real.log n := Real.log_nonneg (by exact_mod_cast hn)
    have h1 : weilTestOf a g (Real.log n) + weilTestOf a g (-Real.log n)
        = g (Real.log n) * (tilt a (Real.log n) : ℂ) := by
      simp only [weilTestOf, hg, tilt_even]; ring
    have h2 : tilt a (Real.log n) = (n : ℝ) ^ (1 / 2 - a) := by
      rw [tilt_of_nonneg _ _ hlog, Real.rpow_def_of_pos hn']; congr 1; ring
    have h3 : ArithmeticFunction.vonMangoldt n / Real.sqrt n * (n : ℝ) ^ (1 / 2 - a)
        = ArithmeticFunction.vonMangoldt n * (n : ℝ) ^ (-a) := by
      rw [Real.sqrt_eq_rpow, div_eq_mul_inv, ← Real.rpow_neg hn'.le, mul_assoc, ← Real.rpow_add hn']
      congr 2; ring
    have h3' : ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) * (((n : ℝ) ^ (1 / 2 - a) : ℝ) : ℂ)
        = ((ArithmeticFunction.vonMangoldt n : ℝ) : ℂ) * (((n : ℝ) ^ (-a) : ℝ) : ℂ) := by
      rw [← Complex.ofReal_mul, h3, Complex.ofReal_mul]
    rw [h1, h2, ← h3']; ring

/-- (T1) for every real a. -/
theorem identity (a : ℝ) (g : ℝ → ℂ) (hg : ∀ u, g (-u) = g u) :
    tiltedPrimeSide a g = primeSide (weilTestOf a g) := by
  unfold tiltedPrimeSide primeSide
  exact tsum_congr (fun n => summand_eq a g hg n)

end WeilContainmentOne.Proof

/-- **IV.1 at level a = 1**: the tilted prime side at level 1 equals the classical prime datum at the test weilTestOf 1 g. -/
theorem weilContainment_identity_one :
    ∀ g : ℝ → ℂ, (∀ u, g (-u) = g u) → tiltedPrimeSide 1 g = primeSide (weilTestOf 1 g) :=
  fun g hg => WeilContainmentOne.Proof.identity 1 g hg
