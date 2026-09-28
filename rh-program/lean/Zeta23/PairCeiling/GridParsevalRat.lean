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
Zeta23/PairCeiling/GridParsevalRat.lean — the GRID PARSEVAL DECOUPLING IDENTITY with RATIONAL marks: the
linear-algebra half of barrier-zoo IV.17's negation (formalization-queue item 10; brief
rh-program/results/iv17-lean-s30/BRIEF.md, clause (1); typing check TYPING-NOTE.md there).

Provenance: rh-program/results/a4-no-go/theorems.md, unit T1 (Theorem 1.2 = paper Theorem 3.9, "it is linear
algebra"); the integer-mark file Zeta23/PairCeiling/GridParseval.lean, whose Sections 1–4 are generalized here.

WHAT CHANGES, AND WHAT DOES NOT.  In GridParseval.lean the marks enter the DFT `dftMark ζ m r = Σ_k (m k : K) χ(r k)`
only through the cast `(m k : K)`, which every algebraic proof treats as an opaque ring element.  So the Parseval identity
and the flat-band collapse are stated here ONCE for a general coefficient vector `v : ZMod M → K` (`dftVec`,
`sum_dftVec_mul_neg`, `flat_band_trace_sq_vec`) over the same `[CommRing K] [IsDomain K]`, with the proofs of the
integer file transferred word for word; integer marks (`dftMark`, any commutative domain) and rational marks (`dftMarkQ`,
a field — `Rat.cast` needs `[DivisionRing K]`, so rational marks do NOT make sense over a general commutative domain;
this is the one typing fact item 10 asked to be checked) are its instances by `rfl`.  The ℂ specialization exchanges one
lemma: `map_ratCast` for `map_intCast` — rationals, like integers, are fixed by complex conjugation, so `c_{−r} = conj c_r`
and the pairing is `|c_r|²`.  The literal Frobenius row `Σ_{j₁,j₂ ∈ [−n, n]} (1/M)² |c_{j₁+j₂}|² = Σ_k m_k²` then holds for
rational marks (`trace_sq_grid_rat`), and `gridRowQ`/`gridRowQ_eq` are `gridRow`/`gridRow_eq` of GridCorner.lean with ℚ
for ℤ.

What is NOT here: any inequality.  The integrality theorem `two_mul_distinct_ge` (the master inequality (MI)) does not
generalize — over ℚ it is FALSE, and GridGap.lean proves that on this row.

Trust model: everything is proved from Mathlib with no `sorry` and no `native_decide`; the only transcendental object is
`Complex.exp` through `zetaM`, as in GridParseval.lean.
-/
import Zeta23.PairCeiling.GridCorner

noncomputable section

open Finset

namespace Zeta23
namespace PairCeiling
namespace GridParsevalRat

open GridParseval GridCorner

/-! ## 1. The DFT of a general coefficient vector, and Parseval -/

variable {K : Type*} [CommRing K] {M : ℕ} [NeZero M]

/-- the form factor (DFT) of an arbitrary coefficient vector `v : ZMod M → K` on the `M`-site grid:
`c_r = Σ_k v_k ζ^{(r·k).val}`.  Integer marks (`dftMark`) and rational marks (`dftMarkQ`) are the cases
`v = (m · : K)`. -/
def dftVec (ζ : K) (v : ZMod M → K) (r : ZMod M) : K :=
  ∑ k : ZMod M, v k * chi ζ (r * k)

/-- integer marks are a coefficient vector: `dftMark ζ m = dftVec ζ (fun k => (m k : K))`. -/
theorem dftMark_eq_dftVec (ζ : K) (m : ZMod M → ℤ) :
    dftMark ζ m = dftVec ζ (fun k => (m k : K)) := rfl

/-- **DFT Parseval on `ZMod M`** for a general coefficient vector, in the algebraic pairing `c_r · c_{−r}`:
`Σ_r c_r c_{−r} = M Σ_k v_k²`.  The proof is `sum_dftMark_mul_neg`'s with `v k` in place of `(m k : K)`. -/
theorem sum_dftVec_mul_neg [IsDomain K] {ζ : K} (hζ : IsPrimitiveRoot ζ M) (v : ZMod M → K) :
    ∑ r : ZMod M, dftVec ζ v r * dftVec ζ v (-r) = (M : K) * ∑ k : ZMod M, (v k) ^ 2 := by
  have hζ1 : ζ ^ (M : ℕ) = 1 := hζ.pow_eq_one
  have expand : ∀ r : ZMod M, dftVec ζ v r * dftVec ζ v (-r)
      = ∑ k : ZMod M, ∑ l : ZMod M, v k * v l * chi ζ (r * (k - l)) := by
    intro r
    unfold dftVec
    rw [Finset.sum_mul_sum]
    refine Finset.sum_congr rfl fun k _ => Finset.sum_congr rfl fun l _ => ?_
    have hchi : chi ζ (r * k) * chi ζ (-r * l) = chi ζ (r * (k - l)) := by
      rw [← chi_add hζ1]
      congr 1
      ring
    calc v k * chi ζ (r * k) * (v l * chi ζ (-r * l))
        = v k * v l * (chi ζ (r * k) * chi ζ (-r * l)) := by ring
      _ = v k * v l * chi ζ (r * (k - l)) := by rw [hchi]
  calc ∑ r : ZMod M, dftVec ζ v r * dftVec ζ v (-r)
      = ∑ r : ZMod M, ∑ k : ZMod M, ∑ l : ZMod M, v k * v l * chi ζ (r * (k - l)) :=
        Finset.sum_congr rfl fun r _ => expand r
    _ = ∑ k : ZMod M, ∑ r : ZMod M, ∑ l : ZMod M, v k * v l * chi ζ (r * (k - l)) :=
        Finset.sum_comm
    _ = ∑ k : ZMod M, ∑ l : ZMod M, ∑ r : ZMod M, v k * v l * chi ζ (r * (k - l)) :=
        Finset.sum_congr rfl fun k _ => Finset.sum_comm
    _ = ∑ k : ZMod M, ∑ l : ZMod M, v k * v l * (if k - l = 0 then (M : K) else 0) := by
        refine Finset.sum_congr rfl fun k _ => Finset.sum_congr rfl fun l _ => ?_
        rw [← Finset.mul_sum, sum_chi_mul hζ (k - l)]
    _ = ∑ k : ZMod M, v k * v k * (M : K) := by
        refine Finset.sum_congr rfl fun k _ => ?_
        have hdiag : ∀ l : ZMod M, v k * v l * (if k - l = 0 then (M : K) else 0)
            = if l = k then v k * v l * (M : K) else 0 := by
          intro l
          by_cases h : l = k
          · subst h
            simp
          · have h' : k - l ≠ 0 := sub_ne_zero.mpr (Ne.symm h)
            simp [h, h']
        calc ∑ l : ZMod M, v k * v l * (if k - l = 0 then (M : K) else 0)
            = ∑ l : ZMod M, (if l = k then v k * v l * (M : K) else 0) :=
              Finset.sum_congr rfl fun l _ => hdiag l
          _ = v k * v k * (M : K) := by
              rw [Finset.sum_ite_eq' Finset.univ k fun l => v k * v l * (M : K)]
              simp
    _ = (M : K) * ∑ k : ZMod M, (v k) ^ 2 := by
        rw [Finset.mul_sum]
        exact Finset.sum_congr rfl fun k _ => by ring

/-- **T1, Lemma 1.1 for a general coefficient vector**: for any band of `M` consecutive integer harmonics,
`Σ_{j₁,j₂ ∈ B} c(j₁+j₂) · c(−(j₁+j₂)) = M² · Σ_k v_k²`. -/
theorem flat_band_trace_sq_vec [IsDomain K] {ζ : K} (hζ : IsPrimitiveRoot ζ M)
    (v : ZMod M → K) (a : ℤ) :
    ∑ j1 ∈ Finset.Icc a (a + (M : ℤ) - 1), ∑ j2 ∈ Finset.Icc a (a + (M : ℤ) - 1),
        dftVec ζ v ((j1 : ZMod M) + (j2 : ZMod M))
          * dftVec ζ v (-((j1 : ZMod M) + (j2 : ZMod M)))
      = (M : K) ^ 2 * ∑ k : ZMod M, (v k) ^ 2 := by
  calc ∑ j1 ∈ Finset.Icc a (a + (M : ℤ) - 1), ∑ j2 ∈ Finset.Icc a (a + (M : ℤ) - 1),
        dftVec ζ v ((j1 : ZMod M) + (j2 : ZMod M))
          * dftVec ζ v (-((j1 : ZMod M) + (j2 : ZMod M)))
      = (M : K) * ∑ r : ZMod M, dftVec ζ v r * dftVec ζ v (-r) :=
        sum_band_pair (fun s => dftVec ζ v s * dftVec ζ v (-s)) a
    _ = (M : K) * ((M : K) * ∑ k : ZMod M, (v k) ^ 2) := by
        rw [sum_dftVec_mul_neg hζ v]
    _ = (M : K) ^ 2 * ∑ k : ZMod M, (v k) ^ 2 := by ring

/-! ## 2. Rational marks -/

section RationalMarks

variable {F : Type*} [Field F]

/-- the form factor (DFT) of a RATIONAL mark vector on the `M`-site grid, over a field `F`:
`c_r = Σ_k (m_k : F) ζ^{(r·k).val}`.  (The cast `ℚ → F` exists for a division ring, not for a general commutative
ring — the typing fact of item 10.) -/
def dftMarkQ (ζ : F) (m : ZMod M → ℚ) (r : ZMod M) : F :=
  ∑ k : ZMod M, (m k : F) * chi ζ (r * k)

theorem dftMarkQ_eq_dftVec (ζ : F) (m : ZMod M → ℚ) :
    dftMarkQ ζ m = dftVec ζ (fun k => (m k : F)) := rfl

/-- the integer theory is the restriction of the rational one: `dftMark ζ m = dftMarkQ ζ (m : ℚ)`. -/
theorem dftMark_eq_dftMarkQ (ζ : F) (m : ZMod M → ℤ) :
    dftMark ζ m = dftMarkQ ζ (fun k => (m k : ℚ)) := by
  funext r
  unfold dftMark dftMarkQ
  simp only [Rat.cast_intCast]

/-- **DFT Parseval with rational marks**: `Σ_r c_r c_{−r} = M Σ_k m_k²`. -/
theorem sum_dftMarkQ_mul_neg {ζ : F} (hζ : IsPrimitiveRoot ζ M) (m : ZMod M → ℚ) :
    ∑ r : ZMod M, dftMarkQ ζ m r * dftMarkQ ζ m (-r) = (M : F) * ∑ k : ZMod M, (m k : F) ^ 2 :=
  sum_dftVec_mul_neg hζ (fun k => (m k : F))

/-- **T1, Lemma 1.1 with rational marks**. -/
theorem flat_band_trace_sq_rat {ζ : F} (hζ : IsPrimitiveRoot ζ M) (m : ZMod M → ℚ) (a : ℤ) :
    ∑ j1 ∈ Finset.Icc a (a + (M : ℤ) - 1), ∑ j2 ∈ Finset.Icc a (a + (M : ℤ) - 1),
        dftMarkQ ζ m ((j1 : ZMod M) + (j2 : ZMod M))
          * dftMarkQ ζ m (-((j1 : ZMod M) + (j2 : ZMod M)))
      = (M : F) ^ 2 * ∑ k : ZMod M, (m k : F) ^ 2 :=
  flat_band_trace_sq_vec hζ (fun k => (m k : F)) a

end RationalMarks

/-! ## 3. Specialization to `ℂ` with rational marks -/

/-- rational marks give a Hermitian form factor: `c_{−r} = conj c_r` (rationals are fixed by conjugation:
`map_ratCast` in place of the integer file's `map_intCast`). -/
lemma dftMarkQ_neg (m : ZMod M → ℚ) (r : ZMod M) :
    dftMarkQ (zetaM M) m (-r) = (starRingEnd ℂ) (dftMarkQ (zetaM M) m r) := by
  unfold dftMarkQ
  rw [map_sum]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [map_mul, map_ratCast, conj_chi (r * k), neg_mul]

/-- over `ℂ` the algebraic pairing is the norm-squared: `c_r · c_{−r} = |c_r|²`. -/
lemma dftMarkQ_mul_neg_eq_normSq (m : ZMod M → ℚ) (r : ZMod M) :
    dftMarkQ (zetaM M) m r * dftMarkQ (zetaM M) m (-r)
      = (Complex.normSq (dftMarkQ (zetaM M) m r) : ℂ) := by
  rw [dftMarkQ_neg, Complex.mul_conj]

/-- **T1, Theorem 1.2 with rational marks (unnormalized)**: `M = 2n + 1`, symmetric band `B = {−n, …, n}`,
`Σ_{j₁,j₂ ∈ B} |c_{j₁+j₂}|² = (2n+1)² · Σ_k m_k²` for every `m : ZMod (2n+1) → ℚ`. -/
theorem grid_parseval_decoupling_rat (n : ℕ) (m : ZMod (2 * n + 1) → ℚ) :
    ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
        Complex.normSq (dftMarkQ (zetaM (2 * n + 1)) m
          ((j1 : ZMod (2 * n + 1)) + (j2 : ZMod (2 * n + 1))))
      = ((2 * n + 1 : ℕ) : ℝ) ^ 2 * ∑ k : ZMod (2 * n + 1), (m k : ℝ) ^ 2 := by
  have hC := flat_band_trace_sq_rat (F := ℂ) (isPrimitiveRoot_zetaM (2 * n + 1)) m (-(n : ℤ))
  have hband : (-(n : ℤ) + ((2 * n + 1 : ℕ) : ℤ) - 1) = (n : ℤ) := by
    push_cast
    ring
  rw [hband] at hC
  have hC2 : ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
      (Complex.normSq (dftMarkQ (zetaM (2 * n + 1)) m
        ((j1 : ZMod (2 * n + 1)) + (j2 : ZMod (2 * n + 1)))) : ℂ)
      = ((2 * n + 1 : ℕ) : ℂ) ^ 2 * ∑ k : ZMod (2 * n + 1), ((m k : ℂ)) ^ 2 := by
    rw [← hC]
    exact Finset.sum_congr rfl fun j1 _ => Finset.sum_congr rfl fun j2 _ =>
      (dftMarkQ_mul_neg_eq_normSq m _).symm
  exact_mod_cast hC2

/-- **T1, Theorem 1.2 with rational marks — normalized form**: the literal SPEC-1.4 Frobenius row with uniform
weights `(1/M)²`, `M = 2n + 1`:  `Σ_{j₁,j₂ ∈ B} (1/M)(1/M) |c_{j₁+j₂}|² = Σ_k m_k²`  exactly, for every rational
mark vector. -/
theorem trace_sq_grid_rat (n : ℕ) (m : ZMod (2 * n + 1) → ℚ) :
    ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
        (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1)) *
          Complex.normSq (dftMarkQ (zetaM (2 * n + 1)) m
            ((j1 : ZMod (2 * n + 1)) + (j2 : ZMod (2 * n + 1))))
      = ∑ k : ZMod (2 * n + 1), (m k : ℝ) ^ 2 := by
  simp only [← Finset.mul_sum]
  rw [grid_parseval_decoupling_rat n m]
  have hM : ((2 * n + 1 : ℕ) : ℝ) = 2 * (n : ℝ) + 1 := by
    push_cast
    ring
  rw [hM]
  have hne : (2 * (n : ℝ) + 1) ≠ 0 := by positivity
  field_simp

/-! ## 4. The grid Frobenius row of a rational mark vector, as a named quantity -/

/-- the literal SPEC-1.4 bandwidth-one Frobenius row of a grid configuration with RATIONAL marks (the LHS of
`trace_sq_grid_rat`): `tr Ĝ² = Σ_{j₁,j₂ ∈ B} (1/M)² |c_{j₁+j₂}|²`, `M = 2n+1`, `B = {−n, …, n}` —
`GridCorner.gridRow` with ℚ for ℤ. -/
def gridRowQ (n : ℕ) (m : ZMod (2 * n + 1) → ℚ) : ℝ :=
  ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
    (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1)) *
      Complex.normSq (dftMarkQ (zetaM (2 * n + 1)) m
        ((j1 : ZMod (2 * n + 1)) + (j2 : ZMod (2 * n + 1))))

/-- **the Theorem 1.2 equality with rational marks**: on the grid the F1 row IS the (cast) sum of squared marks,
whatever the marks' denominators — `gridRow_eq` with ℚ for ℤ. -/
lemma gridRowQ_eq (n : ℕ) (m : ZMod (2 * n + 1) → ℚ) :
    gridRowQ n m = ((∑ k : ZMod (2 * n + 1), (m k) ^ 2 : ℚ) : ℝ) := by
  unfold gridRowQ
  rw [trace_sq_grid_rat n m]
  push_cast
  rfl

/-- the integer row is the rational row of the cast marks: `gridRow n m = gridRowQ n (m : ℚ)`. -/
lemma gridRow_eq_gridRowQ (n : ℕ) (m : ZMod (2 * n + 1) → ℤ) :
    gridRow n m = gridRowQ n (fun k => (m k : ℚ)) := by
  unfold gridRow gridRowQ
  rw [dftMark_eq_dftMarkQ]

end GridParsevalRat
end PairCeiling
end Zeta23
