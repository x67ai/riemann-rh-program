/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does NOT import it: its imports are Mathlib-only.
-/
/-
comparator/Challenge/IntegralityGap.lean — CHALLENGE for the G8 unit: barrier-zoo IV.17, the fractional-mark integrality
barrier, as ONE topic: the master inequality (MI) of the A4 no-go paper (§4.2) HOLDS over integer marks and FAILS over
rational marks on the SAME bandwidth-one grid Frobenius row (rh-program/BARRIER-ZOO.md IV.17 STATEMENT; formalization-queue
item 10; results/a4-no-go/theorems.md Lemma 2.2, Theorem 2.3; paper.md §2.4, §4.2).  Trusted vocabulary:
ChallengeDeps.IntegralityGap (`IntegralityGap.{chi, dftMark, dftMarkQ, zetaM, gridRow, gridRowQ, fracMark}`, defined over Mathlib
alone).  Solution/IntegralityGap.lean (untrusted) proves exactly these statements; github.com/leanprover/comparator checks
statement equality, that only the axioms propext, Classical.choice, Quot.sound are used, and replays the proofs through the
Lean kernel and nanoda.

WHAT IS CLAIMED, and what is NOT.  On the (2n+1)-site uniform grid with the symmetric flat band {−n, …, n}:
  (1) `trace_sq_grid_rat`, `gridRowQ_eq` — grid Parseval with RATIONAL marks: the literal Frobenius row
        Σ_{j₁,j₂} (1/(2n+1))² |c_{j₁+j₂}|² equals Σ_k m_k² for every m : ZMod (2n+1) → ℚ (paper Theorem 3.9 = theorems.md
        Theorem 1.2, "it is linear algebra"); `gridRow_eq` is the integer form, and `gridRow_eq_gridRowQ` says the integer row IS
        the rational row of the cast marks — the two halves of the topic sit on one and the same row.
  (2) `fracMark_mass`, `fracMark_sq`, `fracMark_Nd`, `fracMark_row` — the instance, kernel-checked: 48 atoms of mark 4/3 on the
        65-site grid have mass 64, Σm² = 256/3 = (4/3)·64, N_d = 48, and grid row EXACTLY (4/3)·64·(1 + 0) — budget-tight at ε = 0.
  (3) `mi_fails_rational` — (MI), `3·Σm − Σm² ≤ 2·N_d`, stated for nonnegative RATIONAL marks on the 65-site grid, is FALSE
        (the zoo: "(MI) would demand F1 ≥ 3N − (3/2)N = (3/2)N" — here 96 > 256/3); `corner_fails_rational`,
        `corner_bound_fails_rational` — the 5/6 corner is false for fractional marks on the grid at ε = 0: fracMark meets every
        hypothesis of the grid corner theorem at N = 64, ε = 0 and has N_d = 48 < 64·(5/6 − 0).
  (4) `mi_holds_integer` — (MI) HOLDS for nonnegative INTEGER marks on every grid (theorems.md Lemma 2.2(a));
        `per_atom_slack` — the line where integrality is consumed (IV.17 EXECUTABLE TEST (3)): (m − 1)(m − 2) ≥ 0 for every
        integer m; `per_atom_slack_fails_rational` — false over ℚ (at 4/3); `per_atom_floor`, `per_atom_floor_fails_rational` —
        the mark-1 floor m ≤ m², true over ℤ, false over ℚ (at 1/2).
NO displayed hypothesis anywhere.  What is NOT claimed: nothing about ζ or RH; nothing about LAWS (probability mixtures of
columns — the pointwise failure is stated, the law form is not); nothing about the PAIR CHANNEL (paper Prop. 4.5 is not
formalized — paper-certificate grade, item 10); nothing about any budget other than the bandwidth-one grid row (no two-sided
band, no λ' row, no cubic row); nothing off the grid (atoms at arbitrary positions).  The instance sits at ε = 0.

The `sorry`s below are deliberate (this is the challenge side); expect "declaration uses 'sorry'" warnings when building this
module.
-/
import ChallengeDeps.IntegralityGap

noncomputable section

open Finset IntegralityGap

/-- **(1) grid Parseval with rational marks, normalized**: the literal Frobenius row equals `Σ_k m_k²`. -/
theorem trace_sq_grid_rat :
    ∀ (n : ℕ) (m : ZMod (2 * n + 1) → ℚ),
      ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
          (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1)) *
            Complex.normSq (dftMarkQ (zetaM (2 * n + 1)) m
              ((j1 : ZMod (2 * n + 1)) + (j2 : ZMod (2 * n + 1))))
        = ∑ k : ZMod (2 * n + 1), (m k : ℝ) ^ 2 := by
  sorry

/-- **(1) the rational row as a named quantity**: `gridRowQ n m = Σ_k m_k²` (cast to ℝ). -/
theorem gridRowQ_eq :
    ∀ (n : ℕ) (m : ZMod (2 * n + 1) → ℚ),
      gridRowQ n m = ((∑ k : ZMod (2 * n + 1), (m k) ^ 2 : ℚ) : ℝ) := by
  sorry

/-- **(1) the integer row** (GridCorner's `gridRow_eq`): `gridRow n m = Σ_k m_k²` (cast to ℝ). -/
theorem gridRow_eq :
    ∀ (n : ℕ) (m : ZMod (2 * n + 1) → ℤ),
      gridRow n m = ((∑ k : ZMod (2 * n + 1), (m k) ^ 2 : ℤ) : ℝ) := by
  sorry

/-- **(1) one row**: the integer row is the rational row of the cast marks. -/
theorem gridRow_eq_gridRowQ :
    ∀ (n : ℕ) (m : ZMod (2 * n + 1) → ℤ),
      gridRow n m = gridRowQ n (fun k => (m k : ℚ)) := by
  sorry

/-- **(2) instance data, kernel-checked**: mass `Σ m = 64`. -/
theorem fracMark_mass : ∑ k : ZMod 65, fracMark k = 64 := by
  sorry

/-- **(2) instance data, kernel-checked**: `Σ m² = 256/3`. -/
theorem fracMark_sq : ∑ k : ZMod 65, (fracMark k) ^ 2 = 256 / 3 := by
  sorry

/-- **(2) instance data, kernel-checked**: `N_d = 48` occupied sites. -/
theorem fracMark_Nd :
    (Finset.univ.filter (fun k : ZMod 65 => fracMark k ≠ 0)).card = 48 := by
  sorry

/-- **(2) the instance's grid row is exactly the budget at `ε = 0`**: `gridRowQ 32 fracMark = (4/3)·64·(1 + 0)`. -/
theorem fracMark_row : gridRowQ 32 fracMark = 4 / 3 * 64 * (1 + 0) := by
  sorry

/-- **(3) (MI) is FALSE over rational marks**: the integer theorem's statement with `ℚ` for `ℤ` fails on the 65-site grid. -/
theorem mi_fails_rational :
    ¬ ∀ (m : ZMod 65 → ℚ), (∀ k, 0 ≤ m k) →
      3 * (∑ k : ZMod 65, m k) - (∑ k : ZMod 65, (m k) ^ 2)
        ≤ 2 * ((Finset.univ.filter (fun k : ZMod 65 => m k ≠ 0)).card : ℚ) := by
  sorry

/-- **(3) the 5/6 corner fails for fractional marks on the grid at `ε = 0`**: `fracMark` has nonnegative marks, mass 64,
grid row `≤ (4/3)·64·(1 + 0)`, and `N_d = 48 < 64·(5/6 − (2/3)·0)`. -/
theorem corner_fails_rational :
    (∀ k, 0 ≤ fracMark k) ∧
    ∑ k : ZMod 65, fracMark k = 64 ∧
    gridRowQ 32 fracMark ≤ 4 / 3 * 64 * (1 + 0) ∧
    ((Finset.univ.filter (fun k : ZMod 65 => fracMark k ≠ 0)).card : ℝ) < 64 * (5 / 6 - 2 / 3 * 0) := by
  sorry

/-- **(3) the corner bound, stated for rational marks at `N = 64`, `ε = 0`, is FALSE.** -/
theorem corner_bound_fails_rational :
    ¬ ∀ (m : ZMod 65 → ℚ), (∀ k, 0 ≤ m k) → ∑ k : ZMod 65, m k = 64 →
      gridRowQ 32 m ≤ 4 / 3 * 64 * (1 + 0) →
      (64 : ℝ) * (5 / 6 - 2 / 3 * 0)
        ≤ ((Finset.univ.filter (fun k : ZMod 65 => m k ≠ 0)).card : ℝ) := by
  sorry

/-- **(4) (MI) HOLDS over integer marks** on every grid: `3·Σm − Σm² ≤ 2·N_d` for nonnegative integer marks. -/
theorem mi_holds_integer :
    ∀ (M : ℕ) [NeZero M] (m : ZMod M → ℤ), (∀ k, 0 ≤ m k) →
      3 * (∑ k : ZMod M, m k) - (∑ k : ZMod M, (m k) ^ 2)
        ≤ 2 * ((Finset.univ.filter (fun k : ZMod M => m k ≠ 0)).card : ℤ) := by
  sorry

/-- **(4) the per-atom slack** — the line where integrality is consumed: `(m − 1)(m − 2) ≥ 0` for every integer `m`. -/
theorem per_atom_slack : ∀ m : ℤ, 0 ≤ (m - 1) * (m - 2) := by
  sorry

/-- **(4) the per-atom slack is FALSE over ℚ** (at `m = 4/3`). -/
theorem per_atom_slack_fails_rational : ¬ ∀ q : ℚ, 0 ≤ q → 0 ≤ (q - 1) * (q - 2) := by
  sorry

/-- **(4) the mark-1 floor**: `m ≤ m²` for every integer `m`. -/
theorem per_atom_floor : ∀ m : ℤ, m ≤ m ^ 2 := by
  sorry

/-- **(4) the mark-1 floor is FALSE over ℚ** (at `m = 1/2`). -/
theorem per_atom_floor_fails_rational : ¬ ∀ q : ℚ, 0 ≤ q → q ≤ q ^ 2 := by
  sorry
