/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library; it imports it.
-/
/-
Zeta23/PairCeiling/GridCorner.lean — the ε-BUDGET LP CORNER on the grid class: Theorem 2.3 of the
A4 no-go paper (theorems.md, unit T2) restricted to grid-supported configurations and laws — the
third documented TODO of GridParseval.lean.

Provenance: rh-program/results/a4-no-go/theorems.md, unit T2 (Lemma 2.2(a)/(b), Theorem 2.3,
Corollary 2.4); verified numerically in results/a4-no-go/verify/verify_t2.py (LP over grid
k-doubles columns matches the closed forms to ≤ 3.3e-16; exact Fraction identities).

THE CORNER.  Over laws w on mass-N integer-mark configurations with the bandwidth-one Frobenius
budget E_w[F1] ≤ (4/3)N(1+ε):

    min E_w[N_d]/N = 5/6 − (2/3)ε      and      min E_w[p1] = 2/3 − (4/3)ε ,

both attained by grid laws with marks {1, 2}.  On the GRID the whole proof is finite algebra,
because Theorem 1.2 (`trace_sq_grid`) makes the first step of the lower-bound chain an EQUALITY:
F1 = Σ m² exactly, and the two integrality levels (Lemma 2.2) finish.  Formalized here:

  * `mark_one_count_ge` — Lemma 2.2(b): `2·(Σ m) − Σ m² ≤ n₁` for nonnegative integer marks
    (per-site `1_{m=1} ≥ 2m − m²`; the simple-fraction sibling of `two_mul_distinct_ge`);
  * `gridRow_eq` — the literal SPEC-1.4 Frobenius row of a grid configuration IS the (cast)
    multiplicity count: the Theorem 1.2 equality in the form the corner chain consumes;
  * `grid_corner_pointwise` — Theorem 2.3's pointwise statement on the grid: any grid
    configuration with nonnegative integer marks, mass N, and F1-row ≤ (4/3)N(1+ε) has
    `N_d ≥ N(5/6 − (2/3)ε)` and `n₁ ≥ N(2/3 − (4/3)ε)`;
  * `grid_corner_law` — the LAW form: any finitely supported law (weights ≥ 0 summing to 1) of
    mass-N grid configurations with E_w[F1] ≤ (4/3)N(1+ε) has E_w[N_d] ≥ N(5/6 − (2/3)ε) and
    E_w[n₁] ≥ N(2/3 − (4/3)ε) — the LP lower bound with no discretization;
  * `grid_corner_attained` — ATTAINMENT, exact instance at N = 64, ε = 1/32: the marks-{1,2}
    grid configuration with 12 doubles and 40 simples (kernel-checked column data: mass 64,
    Σ m² = 88, N_d = 52, n₁ = 40) saturates the budget exactly — F1 = 88 = (4/3)·64·(1 + 1/32) —
    and meets BOTH corners with equality: N_d = 52 = 64·(5/6 − (2/3)/32) and
    n₁ = 40 = 64·(2/3 − (4/3)/32).  Both objectives are optimal simultaneously, by a marks-{1,2}
    grid column, exactly as Theorem 2.3's attainment paragraph states.

NOT formalized here (documented TODO, sharpened):
  * the ATOM-ONLY class at arbitrary positions (Theorem 2.3's full scope) — its lower-bound chain
    opens with Lemma 2.1, `F1 ≥ Σ m²` for arbitrary atom positions, whose proof is the
    position-space form `F1 = Σ_{i,i'} m_i m_{i'} K(θ_i − θ_{i'})` with `K = D² ≥ 0` pointwise;
    the repo has only the Fourier-side row, and the position-space/Fourier-side bridge (a finite
    Fourier-inversion computation, no analysis beyond `Complex.exp` identities) is not yet built.
    On the grid the bridge is unnecessary since the row is EQUAL to Σ m² (`gridRow_eq`);
  * general-ε attainment (the two-column law interpolating floor/ceil of k̄ = N(1/6 + (2/3)ε)) —
    elementary but unformalized; the exact integer instance ε = 1/32 above is the witness that the
    bound of `grid_corner_pointwise`/`grid_corner_law` is sharp.

Trust model: everything is proved from Mathlib with no `sorry` and no `native_decide`; the four
column-data facts of the attainment instance are kernel-checked (`decide +kernel`, NumericCert
discipline); the only transcendental object is `Complex.exp` through `zetaM`, as in
GridParseval.lean.
-/
import Zeta23.PairCeiling.GridParseval

noncomputable section

open Finset

namespace Zeta23
namespace PairCeiling
namespace GridCorner

open GridParseval

/-! ## 1. Lemma 2.2(b): the simple-fraction integrality level -/

variable {M : ℕ} [NeZero M]

/-- **theorems.md Lemma 2.2(b)**: for nonnegative integer marks, `2·(Σ m) − Σ m² ≤ n₁` where `n₁`
is the number of mark-1 sites; per site this is `1_{m = 1} ≥ 2m − m²` (equality iff m ∈ {0, 1, 2}
per site; on mass-N configurations, equality iff all marks lie in {1, 2}).  The simple-fraction
sibling of `two_mul_distinct_ge`. -/
theorem mark_one_count_ge (m : ZMod M → ℤ) (hm : ∀ k, 0 ≤ m k) :
    2 * (∑ k : ZMod M, m k) - (∑ k : ZMod M, (m k) ^ 2)
      ≤ ((Finset.univ.filter (fun k : ZMod M => m k = 1)).card : ℤ) := by
  have pointwise : ∀ k : ZMod M,
      2 * m k - (m k) ^ 2 ≤ (if m k = 1 then (1 : ℤ) else 0) := by
    intro k
    by_cases h : m k = 1
    · rw [h, if_pos rfl]
      norm_num
    · rw [if_neg h]
      have h0 := hm k
      rcases (by omega : m k = 0 ∨ 2 ≤ m k) with h1 | h1
      · rw [h1]
        norm_num
      · nlinarith
  calc 2 * (∑ k : ZMod M, m k) - (∑ k : ZMod M, (m k) ^ 2)
      = ∑ k : ZMod M, (2 * m k - (m k) ^ 2) := by
        rw [Finset.mul_sum, Finset.sum_sub_distrib]
    _ ≤ ∑ k : ZMod M, (if m k = 1 then (1 : ℤ) else 0) :=
        Finset.sum_le_sum fun k _ => pointwise k
    _ = ((Finset.univ.filter (fun k : ZMod M => m k = 1)).card : ℤ) := by
        rw [Finset.card_filter]
        push_cast
        rfl

/-! ## 2. The grid Frobenius row as a named quantity -/

/-- the literal SPEC-1.4 bandwidth-one Frobenius row of a grid configuration (the LHS of
`trace_sq_grid`): `tr Ĝ² = Σ_{j₁,j₂ ∈ B} (1/M)² |c_{j₁+j₂}|²`, `M = 2n+1`, `B = {−n, …, n}`. -/
def gridRow (n : ℕ) (m : ZMod (2 * n + 1) → ℤ) : ℝ :=
  ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
    (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1)) *
      Complex.normSq (dftMark (zetaM (2 * n + 1)) m
        ((j1 : ZMod (2 * n + 1)) + (j2 : ZMod (2 * n + 1))))

/-- **the Theorem 1.2 equality in corner-chain form**: on the grid the F1 row IS the (cast)
multiplicity count — the step that is only an inequality (Lemma 2.1) off the grid. -/
lemma gridRow_eq (n : ℕ) (m : ZMod (2 * n + 1) → ℤ) :
    gridRow n m = ((∑ k : ZMod (2 * n + 1), (m k) ^ 2 : ℤ) : ℝ) := by
  unfold gridRow
  rw [trace_sq_grid n m]
  push_cast
  rfl

/-! ## 3. Theorem 2.3 on the grid: the pointwise corner -/

/-- **Theorem 2.3, pointwise statement, grid class**: a grid configuration with nonnegative
integer marks, mass `N`, and bandwidth-one budget `F1 ≤ (4/3)N(1+ε)` satisfies BOTH corner
bounds: `N_d ≥ N(5/6 − (2/3)ε)` and `n₁ ≥ N(2/3 − (4/3)ε)`.  (No sign conditions on `ε` or `N`
are needed: the chain is linear.) -/
theorem grid_corner_pointwise (n : ℕ) (m : ZMod (2 * n + 1) → ℤ) (hm : ∀ k, 0 ≤ m k)
    (N : ℤ) (hmass : ∑ k : ZMod (2 * n + 1), m k = N) (ε : ℝ)
    (hbudget : gridRow n m ≤ 4 / 3 * (N : ℝ) * (1 + ε)) :
    (N : ℝ) * (5 / 6 - 2 / 3 * ε)
        ≤ ((Finset.univ.filter (fun k : ZMod (2 * n + 1) => m k ≠ 0)).card : ℝ) ∧
      (N : ℝ) * (2 / 3 - 4 / 3 * ε)
        ≤ ((Finset.univ.filter (fun k : ZMod (2 * n + 1) => m k = 1)).card : ℝ) := by
  have hQ := gridRow_eq n m
  have h1 := corner_transfer m hm N hmass
  have h2 := mark_one_count_ge m hm
  rw [hmass] at h2
  have h1' : (3 : ℝ) * N - ((∑ k : ZMod (2 * n + 1), (m k) ^ 2 : ℤ) : ℝ)
      ≤ 2 * ((Finset.univ.filter (fun k : ZMod (2 * n + 1) => m k ≠ 0)).card : ℝ) := by
    exact_mod_cast h1
  have h2' : (2 : ℝ) * N - ((∑ k : ZMod (2 * n + 1), (m k) ^ 2 : ℤ) : ℝ)
      ≤ ((Finset.univ.filter (fun k : ZMod (2 * n + 1) => m k = 1)).card : ℝ) := by
    exact_mod_cast h2
  rw [hQ] at hbudget
  constructor <;> linarith

/-! ## 4. Theorem 2.3 on the grid: the law (expectation) form -/

/-- **Theorem 2.3, law form, grid class**: for a finitely supported law — weights `w i ≥ 0` with
`Σ w = 1` — of mass-`N` grid configurations with expected budget `E_w[F1] ≤ (4/3)N(1+ε)`, both
corners hold in expectation:

    `E_w[N_d] ≥ N(5/6 − (2/3)ε)`      and      `E_w[n₁] ≥ N(2/3 − (4/3)ε)` .

This is the LP lower bound of Theorem 2.3 with no discretization — the bound the M2 gate's
940-record LP could not move (δ₀ = 0, absorption). -/
theorem grid_corner_law {ι : Type*} (s : Finset ι) (w : ι → ℝ)
    (hw : ∀ i ∈ s, 0 ≤ w i) (hw1 : ∑ i ∈ s, w i = 1)
    (n : ℕ) (m : ι → ZMod (2 * n + 1) → ℤ) (hm : ∀ i ∈ s, ∀ k, 0 ≤ m i k)
    (N : ℤ) (hmass : ∀ i ∈ s, ∑ k : ZMod (2 * n + 1), m i k = N) (ε : ℝ)
    (hbudget : ∑ i ∈ s, w i * gridRow n (m i) ≤ 4 / 3 * (N : ℝ) * (1 + ε)) :
    (N : ℝ) * (5 / 6 - 2 / 3 * ε)
        ≤ ∑ i ∈ s, w i *
            ((Finset.univ.filter (fun k : ZMod (2 * n + 1) => m i k ≠ 0)).card : ℝ) ∧
      (N : ℝ) * (2 / 3 - 4 / 3 * ε)
        ≤ ∑ i ∈ s, w i *
            ((Finset.univ.filter (fun k : ZMod (2 * n + 1) => m i k = 1)).card : ℝ) := by
  -- per-configuration corner chains, cast to ℝ, with the row substituted by `gridRow_eq`
  have hNd : ∀ i ∈ s, 3 * (N : ℝ) - gridRow n (m i)
      ≤ 2 * ((Finset.univ.filter (fun k : ZMod (2 * n + 1) => m i k ≠ 0)).card : ℝ) := by
    intro i hi
    rw [gridRow_eq]
    exact_mod_cast corner_transfer (m i) (hm i hi) N (hmass i hi)
  have hn1 : ∀ i ∈ s, 2 * (N : ℝ) - gridRow n (m i)
      ≤ ((Finset.univ.filter (fun k : ZMod (2 * n + 1) => m i k = 1)).card : ℝ) := by
    intro i hi
    rw [gridRow_eq]
    have h := mark_one_count_ge (m i) (hm i hi)
    rw [hmass i hi] at h
    exact_mod_cast h
  -- weighted sums of the per-configuration chains
  have key1 : ∑ i ∈ s, w i * ((3 * (N : ℝ) - gridRow n (m i)) / 2)
      ≤ ∑ i ∈ s, w i *
          ((Finset.univ.filter (fun k : ZMod (2 * n + 1) => m i k ≠ 0)).card : ℝ) :=
    Finset.sum_le_sum fun i hi =>
      mul_le_mul_of_nonneg_left (by linarith [hNd i hi]) (hw i hi)
  have key2 : ∑ i ∈ s, w i * (2 * (N : ℝ) - gridRow n (m i))
      ≤ ∑ i ∈ s, w i *
          ((Finset.univ.filter (fun k : ZMod (2 * n + 1) => m i k = 1)).card : ℝ) :=
    Finset.sum_le_sum fun i hi =>
      mul_le_mul_of_nonneg_left (hn1 i hi) (hw i hi)
  -- expand the left-hand sums into (Σ w) and E_w[F1]
  have expand1 : ∑ i ∈ s, w i * ((3 * (N : ℝ) - gridRow n (m i)) / 2)
      = 3 * (N : ℝ) / 2 * (∑ i ∈ s, w i)
        - (1 / 2) * (∑ i ∈ s, w i * gridRow n (m i)) := by
    rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl fun i _ => by ring
  have expand2 : ∑ i ∈ s, w i * (2 * (N : ℝ) - gridRow n (m i))
      = 2 * (N : ℝ) * (∑ i ∈ s, w i) - ∑ i ∈ s, w i * gridRow n (m i) := by
    rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl fun i _ => by ring
  rw [expand1, hw1] at key1
  rw [expand2, hw1] at key2
  constructor <;> linarith

/-! ## 5. Attainment: the exact marks-{1,2} instance at N = 64, ε = 1/32 -/

/-- the attaining grid column at N = 64, ε = 1/32: 12 doubles and 40 simples on 52 of the 65 grid
sites (theorems.md Theorem 2.3, attainment, `c_k` at `k = k̄ = N(1/6 + (2/3)ε) = 12` — integral, so
the single column suffices). -/
def attainMark : ZMod 65 → ℤ := fun k => if k.val < 12 then 2 else if k.val < 52 then 1 else 0

/-- kernel-checked column data: mass `Σ m = 64`. -/
theorem attainMark_mass : ∑ k : ZMod 65, attainMark k = 64 := by decide +kernel

/-- kernel-checked column data: `Σ m² = 88`. -/
theorem attainMark_sq : ∑ k : ZMod 65, (attainMark k) ^ 2 = 88 := by decide +kernel

/-- kernel-checked column data: `N_d = 52` occupied sites. -/
theorem attainMark_Nd :
    (Finset.univ.filter (fun k : ZMod 65 => attainMark k ≠ 0)).card = 52 := by decide +kernel

/-- kernel-checked column data: `n₁ = 40` simple sites. -/
theorem attainMark_n1 :
    (Finset.univ.filter (fun k : ZMod 65 => attainMark k = 1)).card = 40 := by decide +kernel

/-- the column's marks are nonnegative. -/
lemma attainMark_nonneg : ∀ k : ZMod 65, 0 ≤ attainMark k := by
  intro k
  simp only [attainMark]
  split_ifs <;> norm_num

/-- **Theorem 2.3, attainment (exact instance)**: at N = 64, ε = 1/32 the marks-{1,2} column
`attainMark` SATURATES the bandwidth-one budget exactly — its grid F1 row equals
`88 = (4/3)·64·(1 + 1/32)` — and attains BOTH corners with equality:

    `N_d = 52 = 64·(5/6 − (2/3)·(1/32))`      and      `n₁ = 40 = 64·(2/3 − (4/3)·(1/32))` .

Together with `grid_corner_pointwise`/`grid_corner_law` this pins the two optima at this budget:
the lower bounds are met by an explicit grid law (a single column), marks in {1, 2}, both
objectives optimal simultaneously — the corner the M2 gate's cubic block could not move. -/
theorem grid_corner_attained :
    gridRow 32 attainMark = 4 / 3 * 64 * (1 + 1 / 32) ∧
    ((Finset.univ.filter (fun k : ZMod 65 => attainMark k ≠ 0)).card : ℝ)
        = 64 * (5 / 6 - 2 / 3 * (1 / 32)) ∧
    ((Finset.univ.filter (fun k : ZMod 65 => attainMark k = 1)).card : ℝ)
        = 64 * (2 / 3 - 4 / 3 * (1 / 32)) := by
  refine ⟨?_, ?_, ?_⟩
  · rw [gridRow_eq 32 attainMark, attainMark_sq]
    norm_num
  · rw [attainMark_Nd]
    norm_num
  · rw [attainMark_n1]
    norm_num

end GridCorner
end PairCeiling
end Zeta23
