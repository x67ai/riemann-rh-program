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
Zeta23/PairCeiling/GridWitness.lean — the WORKED WITNESS INSTANCE of the grid Parseval decoupling
(A4 no-go paper: the N = 64 vacancy lattice of witness_N64.json) and the finite/algebraic half of
Proposition 1.3 (the λ' = 1/2 half-band row on the same grid) — the first two documented TODOs of
GridParseval.lean.

Provenance: rh-program/results/a4-no-go/theorems.md, unit T1 — the "worked exact value" following
Proposition 1.3, and Proposition 1.3 itself; rh-program/results/a4-m2-gate/witness_N64.json (first
law column: N_d = 64, F1 = 64, F' = 125.09090…); AUDIT.md Section 3.5 (the exact-rational spot
check 4128/33).

THE WITNESS.  N = 64, grid M = N + 1 = 65 sites: the "vacancy lattice" — unit marks on 64 of the
65 grid sites, one site vacant.  Its ℤ/65 mark DFT is `c_r = 65·[r = 0] − χ(r·k₀)` (k₀ the vacancy
position), so the power spectrum is |c₀|² = 64² = 4096 and |c_r|² = 1 for every r ≠ 0 — proved here
ALGEBRAICALLY, for every vacancy position, over any integral domain with a primitive 65th root of
unity (`vacancy_pairing`), then specialized to ℂ (`vacancy_normSq`).  Consequences, all exact:

  * `vacancy_F1` — the bandwidth-one row: F1 = Σ m² = 64 (Theorem 1.2 instance; blind to k₀);
  * `vacancy_half_band_value` — the λ' = 1/2 half-band row (M' = 33 harmonics, band {−16, …, 16},
    uniform weights 1/33): F' = 4096/33 + 32/33 = **4128/33** — theorems.md's hand-checkable worked
    value and the shipped witness column (F' = 125.090909…), for EVERY vacancy position k₀.  The
    integer core Σ_{j₁,j₂ ∈ [−16,16]} (4096·[j₁+j₂ = 0] + [j₁+j₂ ≠ 0]) = 136224 is kernel-checked
    (`decide +kernel`; NumericCert discipline — no native_decide);
  * `half_band_alive` — the two-bandwidth decoupling made explicit: F' = 4128/33 ≠ 64 = Σ m², so
    the half-band kernel does NOT collapse to the multiplicity count on the grid (the λ = 1 row
    does, by Theorem 1.2): the "alive" half of Proposition 1.3, in witness form.

PROPOSITION 1.3, THE FINITE/ALGEBRAIC HALF.  The displayed formula of Prop 1.3 is formalized:
  * `sum_band_pair_tri` — the general triangular fold: for ANY band Icc a b and any g,
    Σ_{j₁,j₂ ∈ [a,b]} g(j₁+j₂) = Σ_{s ∈ [2a,2b]} ((b−a+1) − |s−a−b|)·g(s), by the exact fiber
    count `band_pair_card` (#{(j₁,j₂) : j₁+j₂ = s} = (b−a+1) − |s−a−b| on the window);
  * `half_band_fold` — the literal Prop 1.3 display: F' = Σ_{|s| ≤ 32} ((33−|s|)/33²)·|c_s|²,
    the s-window {−32, …, 32} read through the ℤ/65 DFT;
  * `sum_window_residues` — that window is a COMPLETE residue system mod 65 (each class hit once:
    no residue-class telescoping can occur, unlike the λ = 1 band of `weight_telescoping`);
  * `half_band_weight_pos`, `half_band_weight_nonconstant` — the folded weights (33−|s|)/33² are
    strictly positive on the whole window and non-constant (33/33² at s = 0 vs 32/33² at |s| = 1).

NOT formalized here (sharpened TODO).  Prop 1.3's closing sentence — strict position-sensitivity,
i.e. two grid configurations with the SAME mark multiset and DIFFERENT F' — is not yet landed.
What it needs, precisely: the natural witness pairs (e.g. two-vacancy configurations at different
separations d) have F' differing by Dirichlet-kernel values (sin(33πd/65)/sin(πd/65))², elements of
the real cyclotomic field ℚ(ζ₆₅)⁺ of degree 24 — individually irrational, so no rational/decide
certificate applies directly.  The finite/algebraic route that WOULD land it: express the difference
as an explicit integer polynomial P(ζ₆₅), exhibit an explicit division P = q·Φ₆₅ + r with r ≠ 0 and
deg r < 48 = deg Φ₆₅ (checkable coefficient arithmetic, via computable coefficient lists — Mathlib's
`Polynomial` is noncomputable so a small eval bridge is required), and conclude P(ζ₆₅) ≠ 0 from
`Polynomial.cyclotomic_eq_minpoly_rat` (Φ₆₅ is the minimal polynomial of e^{2πi/65} over ℚ).  No
analytic input is missing — only that cyclotomic certificate layer.

Trust model: everything is proved from Mathlib with no `sorry` and no `native_decide`; the single
kernel-checked computation is the integer double sum `half_band_core` (`decide +kernel`); the only
transcendental object is `Complex.exp` entering through `zetaM`, exactly as in GridParseval.lean.
-/
import Zeta23.PairCeiling.GridParseval

noncomputable section

open Finset

namespace Zeta23
namespace PairCeiling
namespace GridWitness

open GridParseval

/-! ## 1. The vacancy configuration and its exact spectrum (any domain, any vacancy position) -/

variable {K : Type*} [CommRing K] {M : ℕ} [NeZero M]

/-- the vacancy lattice: unit marks on every one of the `M` grid sites except the vacancy `k₀`
(witness_N64.json, first law column, at `M = 65`). -/
def vacancyMark (k0 : ZMod M) : ZMod M → ℤ := fun k => if k = k0 then 0 else 1

omit [NeZero M] in
lemma vacancyMark_cast (k0 k : ZMod M) :
    ((vacancyMark k0 k : ℤ) : K) = if k = k0 then 0 else 1 := by
  unfold vacancyMark
  split <;> simp

/-- the full-lattice form factor: `Σ_k χ(r·k) = M·[r = 0]` (orthogonality read along the site sum). -/
lemma dftMark_one [IsDomain K] {ζ : K} (hζ : IsPrimitiveRoot ζ M) (r : ZMod M) :
    dftMark ζ (fun _ => (1 : ℤ)) r = if r = 0 then (M : K) else 0 := by
  unfold dftMark
  have h1 : ∀ k : ZMod M, ((1 : ℤ) : K) * chi ζ (r * k) = chi ζ (k * r) := fun k => by
    rw [Int.cast_one, one_mul, mul_comm]
  rw [Finset.sum_congr rfl fun k _ => h1 k]
  exact sum_chi_mul hζ r

/-- **the vacancy form factor**: `c_r = M·[r = 0] − χ(r·k₀)` — removing one site from the full
lattice subtracts a single unit phase (theorems.md T1, worked value). -/
lemma dftMark_vacancy [IsDomain K] {ζ : K} (hζ : IsPrimitiveRoot ζ M) (k0 r : ZMod M) :
    dftMark ζ (vacancyMark k0) r = (if r = 0 then (M : K) else 0) - chi ζ (r * k0) := by
  unfold dftMark
  have hsplit : ∀ k : ZMod M, ((vacancyMark k0 k : ℤ) : K) * chi ζ (r * k)
      = chi ζ (k * r) - (if k = k0 then chi ζ (r * k) else 0) := by
    intro k
    rw [vacancyMark_cast]
    by_cases h : k = k0
    · simp [h, mul_comm]
    · simp [h, mul_comm]
  rw [Finset.sum_congr rfl fun k _ => hsplit k, Finset.sum_sub_distrib, sum_chi_mul hζ r,
    Finset.sum_ite_eq' Finset.univ k0 (fun k => chi ζ (r * k))]
  simp

/-- **the vacancy power spectrum, algebraic pairing form**: `c_r · c_{−r} = (M−1)²·[r = 0] + [r ≠ 0]`
— for EVERY vacancy position `k₀`, over any integral domain with a primitive `M`-th root of unity. -/
theorem vacancy_pairing [IsDomain K] {ζ : K} (hζ : IsPrimitiveRoot ζ M) (k0 r : ZMod M) :
    dftMark ζ (vacancyMark k0) r * dftMark ζ (vacancyMark k0) (-r)
      = if r = 0 then ((M : K) - 1) ^ 2 else 1 := by
  have hζ1 : ζ ^ (M : ℕ) = 1 := hζ.pow_eq_one
  rw [dftMark_vacancy hζ k0 r, dftMark_vacancy hζ k0 (-r)]
  by_cases h : r = 0
  · subst h
    simp only [neg_zero, zero_mul, chi_zero, if_true]
    ring
  · have h' : -r ≠ 0 := fun hc => h (neg_eq_zero.mp hc)
    rw [if_neg h, if_neg h', if_neg h]
    have hone : chi ζ (r * k0) * chi ζ (-r * k0) = 1 := by
      rw [neg_mul, chi_mul_chi_neg hζ1]
    calc (0 - chi ζ (r * k0)) * (0 - chi ζ (-r * k0))
        = chi ζ (r * k0) * chi ζ (-r * k0) := by ring
      _ = 1 := hone

/-- the vacancy power spectrum over `ℂ`: `|c_r|² = (M−1)²·[r = 0] + [r ≠ 0]`. -/
theorem vacancy_normSq (k0 r : ZMod M) :
    Complex.normSq (dftMark (zetaM M) (vacancyMark k0) r)
      = if r = 0 then ((M : ℝ) - 1) ^ 2 else 1 := by
  have h := vacancy_pairing (K := ℂ) (isPrimitiveRoot_zetaM M) k0 r
  rw [dftMark_mul_neg_eq_normSq] at h
  by_cases hr : r = 0
  · rw [if_pos hr] at h ⊢
    exact_mod_cast h
  · rw [if_neg hr] at h ⊢
    exact_mod_cast h

/-- the vacancy multiplicity count: `Σ_k m_k² = M − 1`. -/
lemma vacancyMark_sq_sum (k0 : ZMod M) :
    ∑ k : ZMod M, (vacancyMark k0 k) ^ 2 = (M : ℤ) - 1 := by
  have h : ∀ k : ZMod M, (vacancyMark k0 k) ^ 2 = 1 - (if k = k0 then 1 else 0) := by
    intro k
    unfold vacancyMark
    by_cases hk : k = k0 <;> simp [hk]
  rw [Finset.sum_congr rfl fun k _ => h k, Finset.sum_sub_distrib,
    Finset.sum_ite_eq' Finset.univ k0 (fun _ => (1 : ℤ))]
  simp [Finset.card_univ, ZMod.card]

/-- the vacancy mass: `Σ_k m_k = M − 1` (at `M = 65`: 64 simple marks, mass N = 64). -/
lemma vacancyMark_sum (k0 : ZMod M) :
    ∑ k : ZMod M, vacancyMark k0 k = (M : ℤ) - 1 := by
  have h : ∀ k : ZMod M, vacancyMark k0 k = (vacancyMark k0 k) ^ 2 := by
    intro k
    unfold vacancyMark
    by_cases hk : k = k0 <;> simp [hk]
  rw [Finset.sum_congr rfl fun k _ => h k]
  exact vacancyMark_sq_sum k0

lemma vacancyMark_sq_sum_real (k0 : ZMod M) :
    ∑ k : ZMod M, ((vacancyMark k0 k : ℤ) : ℝ) ^ 2 = (M : ℝ) - 1 := by
  have h := vacancyMark_sq_sum (M := M) k0
  have hcast : ∑ k : ZMod M, ((vacancyMark k0 k : ℤ) : ℝ) ^ 2
      = ((∑ k : ZMod M, (vacancyMark k0 k) ^ 2 : ℤ) : ℝ) := by
    push_cast
    rfl
  rw [hcast, h]
  push_cast
  ring

/-! ## 2. The N = 64 instance: the bandwidth-one row is blind (`F1 = 64`) -/

/-- **the witness's bandwidth-one row** (witness_N64.json first column, F1 = 64): on the 65-site
grid the λ = 1 flat Frobenius row of the vacancy lattice equals Σ m² = 64 exactly — for every
vacancy position (Theorem 1.2 instance; the row is BLIND to `k₀`). -/
theorem vacancy_F1 (k0 : ZMod 65) :
    ∑ j1 ∈ Finset.Icc (-32 : ℤ) 32, ∑ j2 ∈ Finset.Icc (-32 : ℤ) 32,
        (1 / (65 : ℝ)) * (1 / 65) *
          Complex.normSq (dftMark (zetaM 65) (vacancyMark k0) ((j1 : ZMod 65) + (j2 : ZMod 65)))
      = 64 := by
  have h := trace_sq_grid 32 (vacancyMark k0)
  have h2 := vacancyMark_sq_sum_real (M := 65) k0
  norm_num at h h2 ⊢
  rw [h, h2]

/-! ## 3. The N = 64 instance: the half-band row and the exact value 4128/33 -/

/-- the λ' = 1/2 half-band Frobenius row at N = 64: M' = 33 harmonics on the band {−16, …, 16},
uniform weights 1/33, SPEC-1.4 double-sum form, evaluated on grid configurations through the ℤ/65
mark DFT (Proposition 1.3's `F'`). -/
def halfBandRow (m : ZMod 65 → ℤ) : ℝ :=
  ∑ j1 ∈ Finset.Icc (-16 : ℤ) 16, ∑ j2 ∈ Finset.Icc (-16 : ℤ) 16,
    (1 / (33 : ℝ)) * (1 / 33) *
      Complex.normSq (dftMark (zetaM 65) m ((j1 : ZMod 65) + (j2 : ZMod 65)))

/-- **the kernel-checked integer core** of the witness value: over the half band,
`Σ_{j₁,j₂ ∈ [−16,16]} (4096·[j₁+j₂ = 0] + 1·[j₁+j₂ ≠ 0]) = 33·4096 + (33² − 33) = 136224`. -/
theorem half_band_core :
    ∑ j1 ∈ Finset.Icc (-16 : ℤ) 16, ∑ j2 ∈ Finset.Icc (-16 : ℤ) 16,
      (if j1 + j2 = 0 then (4096 : ℤ) else 1) = 136224 := by
  decide +kernel

/-- **the worked exact value of the witness** (theorems.md T1; witness_N64.json first column;
AUDIT 3.5): the half-band row of the N = 64 vacancy lattice is

    `F' = 4096/33 + 32/33 = 4128/33 = 125.0909…`

exactly, for EVERY vacancy position `k₀` — while `F1 = 64` (`vacancy_F1`): the two-bandwidth
decoupling of the absorption mechanism, as one exact rational identity. -/
theorem vacancy_half_band_value (k0 : ZMod 65) :
    halfBandRow (vacancyMark k0) = 4128 / 33 := by
  unfold halfBandRow
  have hterm : ∀ j1 ∈ Finset.Icc (-16 : ℤ) 16, ∀ j2 ∈ Finset.Icc (-16 : ℤ) 16,
      Complex.normSq (dftMark (zetaM 65) (vacancyMark k0) ((j1 : ZMod 65) + (j2 : ZMod 65)))
        = if j1 + j2 = 0 then (4096 : ℝ) else 1 := by
    intro j1 hj1 j2 hj2
    rw [Finset.mem_Icc] at hj1 hj2
    have hcast : (j1 : ZMod 65) + (j2 : ZMod 65) = ((j1 + j2 : ℤ) : ZMod 65) := by
      push_cast
      ring
    have hiff : (((j1 + j2 : ℤ) : ZMod 65) = 0) ↔ j1 + j2 = 0 := by
      constructor
      · intro h0
        have hdvd : ((65 : ℕ) : ℤ) ∣ (j1 + j2) :=
          (ZMod.intCast_zmod_eq_zero_iff_dvd _ 65).mp h0
        exact int_eq_zero_of_dvd_of_bounds (D := 65) (s := j1 + j2) (by norm_num)
          (by exact_mod_cast hdvd) (by omega) (by omega)
      · intro h0
        rw [h0]
        exact Int.cast_zero
    rw [hcast, vacancy_normSq]
    simp only [hiff]
    norm_num
  calc ∑ j1 ∈ Finset.Icc (-16 : ℤ) 16, ∑ j2 ∈ Finset.Icc (-16 : ℤ) 16,
        (1 / (33 : ℝ)) * (1 / 33) *
          Complex.normSq (dftMark (zetaM 65) (vacancyMark k0) ((j1 : ZMod 65) + (j2 : ZMod 65)))
      = ∑ j1 ∈ Finset.Icc (-16 : ℤ) 16, ∑ j2 ∈ Finset.Icc (-16 : ℤ) 16,
          (1 / (33 : ℝ)) * (1 / 33) * (if j1 + j2 = 0 then (4096 : ℝ) else 1) :=
        Finset.sum_congr rfl fun j1 hj1 => Finset.sum_congr rfl fun j2 hj2 => by
          rw [hterm j1 hj1 j2 hj2]
    _ = (1 / (33 : ℝ)) * (1 / 33) * ∑ j1 ∈ Finset.Icc (-16 : ℤ) 16,
          ∑ j2 ∈ Finset.Icc (-16 : ℤ) 16, (if j1 + j2 = 0 then (4096 : ℝ) else 1) := by
        simp only [Finset.mul_sum]
    _ = (1 / (33 : ℝ)) * (1 / 33) *
          ((∑ j1 ∈ Finset.Icc (-16 : ℤ) 16, ∑ j2 ∈ Finset.Icc (-16 : ℤ) 16,
            (if j1 + j2 = 0 then (4096 : ℤ) else 1) : ℤ) : ℝ) := by
        congr 1
        push_cast [apply_ite (Int.cast : ℤ → ℝ)]
        rfl
    _ = 4128 / 33 := by
        rw [half_band_core]
        norm_num

/-- **Proposition 1.3, the "alive" half in witness form**: the half-band row does NOT collapse to
the multiplicity count on the grid — on the vacancy lattice `F' = 4128/33 ≠ 64 = Σ m²` (the λ = 1
row DOES collapse, `vacancy_F1`): the two-bandwidth decoupling is strict. -/
theorem half_band_alive (k0 : ZMod 65) :
    halfBandRow (vacancyMark k0) ≠ ∑ k : ZMod 65, ((vacancyMark k0 k : ℤ) : ℝ) ^ 2 := by
  rw [vacancy_half_band_value, vacancyMark_sq_sum_real]
  norm_num

/-! ## 4. Proposition 1.3, the finite/algebraic half: the triangular fold of the half-band row -/

/-- **the exact pair count** (theorems.md T1, key lemma bookkeeping): on the window `[2a, 2b]`,
`#{(j₁,j₂) ∈ [a,b]² : j₁+j₂ = s} = (b−a+1) − |s−a−b|` — the triangular weights of the sum-set;
the fiber is the graph of `j ↦ (j, s−j)` over `[max a (s−b), min b (s−a)]`. -/
lemma band_pair_card (a b s : ℤ) (h1 : 2 * a ≤ s) (h2 : s ≤ 2 * b) :
    ((Finset.Icc a b ×ˢ Finset.Icc a b).filter (fun p : ℤ × ℤ => p.1 + p.2 = s)).card
      = ((b - a + 1) - |s - a - b|).toNat := by
  have hcard : ((Finset.Icc a b ×ˢ Finset.Icc a b).filter
        (fun p : ℤ × ℤ => p.1 + p.2 = s)).card
      = (Finset.Icc (max a (s - b)) (min b (s - a))).card := by
    refine Finset.card_nbij' (fun p => p.1) (fun j => (j, s - j)) ?_ ?_ ?_ ?_
    · intro p hp
      simp only [Finset.mem_coe, Finset.mem_filter, Finset.mem_product, Finset.mem_Icc] at hp
      simp only [Finset.mem_coe, Finset.mem_Icc, max_le_iff, le_min_iff]
      omega
    · intro j hj
      simp only [Finset.mem_coe, Finset.mem_Icc, max_le_iff, le_min_iff] at hj
      simp only [Finset.mem_coe, Finset.mem_filter, Finset.mem_product, Finset.mem_Icc]
      omega
    · intro p hp
      simp only [Finset.mem_coe, Finset.mem_filter] at hp
      have h5 : p.1 + p.2 = s := hp.2
      show (p.1, s - p.1) = p
      rw [show s - p.1 = p.2 by omega]
    · intro j _
      rfl
  rw [hcard, Int.card_Icc]
  rcases abs_cases (s - a - b) with ⟨h, _⟩ | ⟨h, _⟩ <;> rw [h] <;> omega

/-- **the general triangular fold** (the structural content of Prop 1.3's display): for ANY band
`[a, b]` and any `g`,

    `Σ_{j₁,j₂ ∈ [a,b]} g(j₁+j₂) = Σ_{s ∈ [2a,2b]} ((b−a+1) − |s−a−b|) · g(s)` .

At `[a,b] = [−16,16]` this is the half-band fold with weights `33 − |s|` on `|s| ≤ 32`; at
`[a,b] = [−n,n]` with `g` `(2n+1)`-periodic it recovers the flat-band collapse of
`sum_band_pair` (there the folded weights telescope to a constant; here they need not). -/
theorem sum_band_pair_tri (a b : ℤ) (g : ℤ → ℝ) :
    ∑ j1 ∈ Finset.Icc a b, ∑ j2 ∈ Finset.Icc a b, g (j1 + j2)
      = ∑ s ∈ Finset.Icc (2 * a) (2 * b), (((b - a + 1) - |s - a - b| : ℤ) : ℝ) * g s := by
  rw [← Finset.sum_product']
  have hmaps : ∀ p ∈ Finset.Icc a b ×ˢ Finset.Icc a b,
      p.1 + p.2 ∈ Finset.Icc (2 * a) (2 * b) := by
    intro p hp
    rw [Finset.mem_product, Finset.mem_Icc, Finset.mem_Icc] at hp
    rw [Finset.mem_Icc]
    omega
  rw [← Finset.sum_fiberwise_of_maps_to hmaps (fun p => g (p.1 + p.2))]
  refine Finset.sum_congr rfl fun s hs => ?_
  rw [Finset.mem_Icc] at hs
  have hconst : ∑ p ∈ (Finset.Icc a b ×ˢ Finset.Icc a b).filter
        (fun p : ℤ × ℤ => p.1 + p.2 = s), g (p.1 + p.2)
      = ∑ _p ∈ (Finset.Icc a b ×ˢ Finset.Icc a b).filter
          (fun p : ℤ × ℤ => p.1 + p.2 = s), g s :=
    Finset.sum_congr rfl fun p hp => by rw [(Finset.mem_filter.mp hp).2]
  rw [hconst, Finset.sum_const, band_pair_card a b s hs.1 hs.2, nsmul_eq_mul]
  congr 1
  have hnn : (0 : ℤ) ≤ (b - a + 1) - |s - a - b| := by
    rcases abs_cases (s - a - b) with ⟨h, _⟩ | ⟨h, _⟩ <;> omega
  exact_mod_cast congrArg (Int.cast : ℤ → ℝ) (Int.toNat_of_nonneg hnn)

/-- **Proposition 1.3, displayed formula**: on the grid the half-band row folds to the ℤ/65 power
spectrum with the triangular weights `(33 − |s|)/33²` over the window `s ∈ {−32, …, 32}`:

    `F' = Σ_{|s| ≤ 32} ((33 − |s|)/33²) · |c_s|²` ,

`c` the ℤ/65 mark DFT.  The weights are strictly positive (`half_band_weight_pos`) and non-constant
(`half_band_weight_nonconstant`), and the window is a complete residue system mod 65
(`sum_window_residues`) — so `F'` reads the FULL grid power spectrum with a non-uniform weight,
subject only to Parseval (`sum_dftMark_mul_neg`): the structural sense in which the λ' = 1/2 kernel
stays alive where the λ = 1 kernel collapses. -/
theorem half_band_fold (m : ZMod 65 → ℤ) :
    halfBandRow m = ∑ s ∈ Finset.Icc (-32 : ℤ) 32,
      (((33 - |s| : ℤ) : ℝ) / 33 ^ 2) *
        Complex.normSq (dftMark (zetaM 65) m ((s : ℤ) : ZMod 65)) := by
  unfold halfBandRow
  have hcast : ∀ j1 j2 : ℤ, (j1 : ZMod 65) + (j2 : ZMod 65) = ((j1 + j2 : ℤ) : ZMod 65) := by
    intro j1 j2
    push_cast
    ring
  calc ∑ j1 ∈ Finset.Icc (-16 : ℤ) 16, ∑ j2 ∈ Finset.Icc (-16 : ℤ) 16,
        (1 / (33 : ℝ)) * (1 / 33) *
          Complex.normSq (dftMark (zetaM 65) m ((j1 : ZMod 65) + (j2 : ZMod 65)))
      = (1 / (33 : ℝ)) * (1 / 33) * ∑ j1 ∈ Finset.Icc (-16 : ℤ) 16,
          ∑ j2 ∈ Finset.Icc (-16 : ℤ) 16,
            Complex.normSq (dftMark (zetaM 65) m (((j1 + j2 : ℤ) : ZMod 65))) := by
        simp only [Finset.mul_sum]
        exact Finset.sum_congr rfl fun j1 _ => Finset.sum_congr rfl fun j2 _ => by
          rw [hcast j1 j2]
    _ = (1 / (33 : ℝ)) * (1 / 33) * ∑ s ∈ Finset.Icc (-32 : ℤ) 32,
          (((33 - |s| : ℤ) : ℝ) *
            Complex.normSq (dftMark (zetaM 65) m ((s : ℤ) : ZMod 65))) := by
        congr 1
        have h := sum_band_pair_tri (-16) 16
          (fun s => Complex.normSq (dftMark (zetaM 65) m ((s : ℤ) : ZMod 65)))
        norm_num at h
        convert h using 2 <;> norm_num
    _ = ∑ s ∈ Finset.Icc (-32 : ℤ) 32,
          (((33 - |s| : ℤ) : ℝ) / 33 ^ 2) *
            Complex.normSq (dftMark (zetaM 65) m ((s : ℤ) : ZMod 65)) := by
        rw [Finset.mul_sum]
        exact Finset.sum_congr rfl fun s _ => by ring

/-- the fold window `{−32, …, 32}` is a complete residue system mod 65: summing any function of
the residue over it is one pass over ℤ/65 (`sum_band` instance — Prop 1.3's "the s-range is a
complete residue system"). -/
theorem sum_window_residues {β : Type*} [AddCommMonoid β] (f : ZMod 65 → β) :
    ∑ s ∈ Finset.Icc (-32 : ℤ) 32, f ((s : ℤ) : ZMod 65) = ∑ r : ZMod 65, f r := by
  have h := sum_band (M := 65) f (-32)
  norm_num at h
  exact h

/-- the folded half-band weights are strictly positive across the whole window (minimum `1/33²`
at `|s| = 32`): every spectral line is read. -/
theorem half_band_weight_pos {s : ℤ} (hs : s ∈ Finset.Icc (-32 : ℤ) 32) :
    (0 : ℝ) < ((33 - |s| : ℤ) : ℝ) / 33 ^ 2 := by
  rw [Finset.mem_Icc] at hs
  have h : (0 : ℤ) < 33 - |s| := by
    rcases abs_cases s with ⟨h, _⟩ | ⟨h, _⟩ <;> omega
  have h' : (0 : ℝ) < ((33 - |s| : ℤ) : ℝ) := by exact_mod_cast h
  positivity

/-- the folded half-band weights are NON-constant (`33/33²` at `s = 0`, `32/33²` at `|s| = 1`):
no residue-class telescoping occurs — the hypothesis of `weight_telescoping` (band length = grid
size) genuinely fails at λ' = 1/2, and `F'` weighs the spectrum non-uniformly. -/
theorem half_band_weight_nonconstant :
    ((33 - |(0 : ℤ)| : ℤ) : ℝ) / 33 ^ 2 ≠ ((33 - |(1 : ℤ)| : ℤ) : ℝ) / 33 ^ 2 := by
  norm_num

end GridWitness
end PairCeiling
end Zeta23
