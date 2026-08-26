/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
/-
Zeta23/PairCeiling/GridParseval.lean — the GRID PARSEVAL DECOUPLING IDENTITY: the algebraic core of the
A4 M2-gate absorption result (gate decided ABSORPTION, 2026-08-26; barrier-zoo formalization-queue item 5).

Provenance: rh-program/results/a4-no-go/theorems.md, unit T1 (Lemma 1.1 general-band form, Theorem 1.2 at
bandwidth one); rh-program/results/a4-m2-gate/SPEC.md Section 1.4 (the Fourier assembly of the trace rows),
AUDIT.md Section 3.1 (the auditor's re-derivation), RUN-REPORT.md Section 2 (the mechanism).

THE IDENTITY.  Finite-circle model (SPEC 1.4): period N on the circle of circumference N; flat window at
bandwidth 1; harmonic band B = any set of M consecutive integers with uniform weights u_j = 1/M; and the
Frobenius (second-trace) row assembled by the Fourier double sum — the LP's literal code path —

    tr Ĝ² = Σ_{j₁,j₂ ∈ B} u_{j₁} u_{j₂} |c_{j₁+j₂}|² ,     c_s = Σ_z m_z e^{-2πi s θ_z / N} .

For a configuration supported on the M-site uniform grid θ_k = kN/M with integer marks m_k, the form
factor c is the DFT of the mark vector on ℤ/M — it depends on s only through s mod M — and

    tr Ĝ² = Σ_k m_k²   EXACTLY,

for EVERY site subset and EVERY mark assignment (absent sites have m_k = 0).  The bandwidth-one flat
reading on the grid sees only multiplicities, never positions: this is the absorption mechanism behind the
gate's δ₀ = 0 (the marks-{1,2} witness meets the lemmaR_tight corner with the whole λ' = 1/2 cubic block
feasible, the sub-grid arrangement paying the cubic budget through position freedom the λ = 1 row cannot
see).

WHICH FORM IS FORMALIZED, AND WHY.  We formalize the double-convolution assembly
Σ_{j₁,j₂ ∈ B} u u |c_{j₁+j₂}|² (not the folded single-convolution Σ_s W₂(s)|c_s|²) because it is SPEC
1.4's literal definition of the row — the form the gate's LP evaluated — and because the proof is then
structural: for each j₁ the map j₂ ↦ j₁ + j₂ mod M is a bijection from the band onto ℤ/M (M consecutive
integers form a complete residue system), so the double sum collapses to M · Σ_{r mod M} |c_r|², and DFT
Parseval on ℤ/M finishes.  This band collapse IS T1's triangular-weight telescoping stated structurally
(each residue class of the sum-set B + B carries total pair count exactly M); the literal weight form —
Σ_{s ≡ r (M), |s| ≤ N} (M − |s|)/M² = 1/M with M = N + 1 — is also proved below (`weight_telescoping`,
`weight_telescoping_rat`), by the explicit one/two-element residue-class decomposition of theorems.md T1.

STRUCTURE (all exact arithmetic; no analysis beyond `Complex.exp` at the ℂ specialization):
  1. the additive character x ↦ ζ^(x.val) of ℤ/M attached to a primitive M-th root of unity ζ in a
     commutative domain K, and its orthogonality Σ_r ζ^{(r·d).val} = M·[d = 0] (geometric sum);
  2. the mark DFT c_r = Σ_k m_k ζ^{(r·k).val} and the exact Parseval identity
     Σ_r c_r c_{−r} = M Σ_k m_k²  (marks are integers, so over ℂ c_{−r} = conj c_r and c_r c_{−r} = |c_r|²);
  3. the band collapse Σ_{j₁,j₂ ∈ Icc a (a+M−1)} f(j₁+j₂ mod M) = M Σ_{r : ℤ/M} f r, and the general-band
     theorem `flat_band_trace_sq` (T1 Lemma 1.1): Σ_{j₁,j₂ ∈ B} c(j₁+j₂) c(−(j₁+j₂)) = M² Σ_k m_k²;
  4. the ℂ specialization with ζ = e^{2πi/M}: `grid_parseval_decoupling` (T1 Theorem 1.2 for even N = 2n,
     M = N + 1 = 2n + 1, symmetric band B = {−n, …, n}), in norm-squared form, and the normalized
     `trace_sq_grid` — the literal tr Ĝ² = Σ_{j₁,j₂} (1/M)(1/M) |c_{j₁+j₂}|² = Σ_k m_k²;
  5. the literal triangular-weight telescoping of T1 (`weight_telescoping`, `weight_telescoping_rat`);
  6. the corner-transfer arithmetic (theorems.md Lemma 2.2(a)): 3N − Σ m² ≤ 2 N_d for nonnegative integer
     marks with mass N — the doubles-corner inequality whose equality case (marks ⊆ {1,2}) the grid law
     realizes with F1 = Σ m² exact by the main identity (lemmaR_tight interface).

Continued in GridWitness.lean (Session 8), discharging two of the three TODOs this header used to
carry: the worked exact value F' = 4128/33 of the N = 64 vacancy lattice (witness_N64.json) is now a
kernel-checked instance there (`vacancy_half_band_value`, with the exact spectrum proved algebraically
for every vacancy position), and the finite/algebraic half of Proposition 1.3 is formalized (the
triangular fold `half_band_fold`, weight positivity/non-constancy, the complete-residue window, and
the "alive" witness `half_band_alive`: F' = 4128/33 ≠ 64 = Σ m² where the λ = 1 row collapses).

NOT formalized (documented TODO, in the queue's terms):
  * Proposition 1.3's closing strict position-sensitivity statement (two grid configurations of equal
    mark multiset with different F') — needs a cyclotomic non-vanishing certificate; the precise
    remaining gap is documented in GridWitness.lean's header;
  * Theorem 2.3 (the ε-budget LP corner 5/6 − (2/3)ε and 2/3 − (4/3)ε) — the LP layer above this identity.

Trust model: everything in this file is proved from Mathlib with no `sorry`, no `native_decide`, and no
numeric certificates; the only transcendental object is `Complex.exp` in the ℂ specialization, entering
solely through `Complex.isPrimitiveRoot_exp`.
-/
import Mathlib.RingTheory.RootsOfUnity.Complex
import Mathlib.Data.Int.Interval
import Mathlib.Data.Complex.BigOperators
import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

noncomputable section

open Finset

namespace Zeta23
namespace PairCeiling
namespace GridParseval

/-! ## 0. Two integer bookkeeping lemmas (bounded multiples of a positive divisor) -/

/-- a multiple of `D > 0` lying strictly between `−D` and `D` is `0`. -/
lemma int_eq_zero_of_dvd_of_bounds {D s : ℤ} (hD : 0 < D) (hdvd : D ∣ s)
    (h1 : -D < s) (h2 : s < D) : s = 0 := by
  rcases hdvd with ⟨c, rfl⟩
  rcases lt_trichotomy c 0 with hc | hc | hc
  · exfalso
    have h3 : D * c ≤ D * (-1) := mul_le_mul_of_nonneg_left (by omega) hD.le
    linarith
  · simp [hc]
  · exfalso
    have h3 : D * 1 ≤ D * c := mul_le_mul_of_nonneg_left (by omega) hD.le
    linarith

/-- a multiple of `D > 0` lying strictly between `−2D` and `D` is `0` or `−D`. -/
lemma int_eq_zero_or_neg_of_dvd_of_bounds {D t : ℤ} (hD : 0 < D) (hdvd : D ∣ t)
    (h1 : -(2 * D) < t) (h2 : t < D) : t = 0 ∨ t = -D := by
  rcases hdvd with ⟨c, rfl⟩
  have hc : c = 0 ∨ c = -1 := by
    rcases lt_trichotomy c (-1) with hc | hc | hc
    · exfalso
      have h3 : D * c ≤ D * (-2) := mul_le_mul_of_nonneg_left (by omega) hD.le
      linarith
    · right; exact hc
    · left
      rcases lt_trichotomy c 0 with hc' | hc' | hc'
      · omega
      · exact hc'
      · exfalso
        have h3 : D * 1 ≤ D * c := mul_le_mul_of_nonneg_left (by omega) hD.le
        linarith
  rcases hc with rfl | rfl
  · left; ring
  · right; ring

/-! ## 1. The additive character `x ↦ ζ^(x.val)` on `ZMod M` and its orthogonality -/

variable {K : Type*} [CommRing K] {M : ℕ} [NeZero M]

/-- the additive character of `ZMod M` attached to an `M`-th root of unity `ζ`: `x ↦ ζ ^ x.val`.
On the `M`-site grid of T1 this is the elementary form-factor phase `e^{-2πi s θ_k / N}` in algebraic
clothing (the sign convention is immaterial: the statements below pair `r` with `−r`). -/
def chi (ζ : K) (x : ZMod M) : K := ζ ^ x.val

omit [NeZero M] in
@[simp] lemma chi_zero (ζ : K) : chi ζ (0 : ZMod M) = 1 := by
  simp [chi, ZMod.val_zero]

omit [NeZero M] in
/-- powers of an `M`-th root of unity only see the exponent mod `M`. -/
lemma pow_mod_eq_pow {ζ : K} (hζ1 : ζ ^ (M : ℕ) = 1) (a : ℕ) : ζ ^ (a % M) = ζ ^ a := by
  conv_rhs => rw [← Nat.div_add_mod a M]
  rw [pow_add, pow_mul, hζ1, one_pow, one_mul]

/-- the character is additive: this is exactly the `(N+1)`-periodicity of the grid form factor. -/
lemma chi_add {ζ : K} (hζ1 : ζ ^ (M : ℕ) = 1) (x y : ZMod M) :
    chi ζ (x + y) = chi ζ x * chi ζ y := by
  unfold chi
  rw [ZMod.val_add, pow_mod_eq_pow hζ1, pow_add]

lemma chi_mul_chi_neg {ζ : K} (hζ1 : ζ ^ (M : ℕ) = 1) (x : ZMod M) :
    chi ζ x * chi ζ (-x) = 1 := by
  rw [← chi_add hζ1, add_neg_cancel, chi_zero]

omit [NeZero M] in
/-- `chi (r·d)` is the `r.val`-th power of `chi d` (geometric-sum form). -/
lemma chi_mul_eq_pow {ζ : K} (hζ1 : ζ ^ (M : ℕ) = 1) (r d : ZMod M) :
    chi ζ (r * d) = chi ζ d ^ r.val := by
  unfold chi
  rw [ZMod.val_mul, pow_mod_eq_pow hζ1, mul_comm r.val d.val, pow_mul]

/-- reindexing a sum over `ZMod M` through `val` as a sum over `range M`. -/
lemma sum_val_eq_sum_range {β : Type*} [AddCommMonoid β] (f : ℕ → β) :
    ∑ r : ZMod M, f r.val = ∑ i ∈ range M, f i := by
  refine Finset.sum_nbij' (fun r => r.val) (fun i => (i : ZMod M)) ?_ ?_ ?_ ?_ ?_
  · intro r _
    exact mem_range.mpr r.val_lt
  · intro i _
    exact mem_univ _
  · intro r _
    exact ZMod.natCast_rightInverse r
  · intro i hi
    exact ZMod.val_cast_of_lt (mem_range.mp hi)
  · intro r _
    rfl

/-- **character orthogonality** on `ZMod M`: `Σ_{r : ZMod M} ζ^{(r·d).val} = M · [d = 0]`.
This is the geometric-sum orthogonality that makes the mark DFT a Parseval isometry. -/
theorem sum_chi_mul [IsDomain K] {ζ : K} (hζ : IsPrimitiveRoot ζ M) (d : ZMod M) :
    ∑ r : ZMod M, chi ζ (r * d) = if d = 0 then (M : K) else 0 := by
  have hζ1 : ζ ^ (M : ℕ) = 1 := hζ.pow_eq_one
  by_cases hd : d = 0
  · subst hd
    rw [if_pos rfl]
    have h1 : ∀ r : ZMod M, chi ζ (r * 0) = 1 := fun r => by rw [mul_zero, chi_zero]
    rw [Finset.sum_congr rfl fun r _ => h1 r, Finset.sum_const, Finset.card_univ, ZMod.card M,
      nsmul_eq_mul, mul_one]
  · rw [if_neg hd]
    calc ∑ r : ZMod M, chi ζ (r * d)
        = ∑ r : ZMod M, (ζ ^ d.val) ^ r.val :=
          Finset.sum_congr rfl fun r _ => chi_mul_eq_pow hζ1 r d
      _ = ∑ i ∈ range M, (ζ ^ d.val) ^ i := sum_val_eq_sum_range _
      _ = 0 := ?_
    have hxM : (ζ ^ d.val) ^ (M : ℕ) = 1 := by
      rw [← pow_mul, mul_comm, pow_mul, hζ1, one_pow]
    have hx1 : ζ ^ d.val ≠ 1 := by
      intro h1
      have hdvd : M ∣ d.val := hζ.dvd_of_pow_eq_one d.val h1
      have hlt : d.val < M := d.val_lt
      exact hd ((ZMod.val_eq_zero d).mp (Nat.eq_zero_of_dvd_of_lt hdvd hlt))
    have hgeom : (∑ i ∈ range M, (ζ ^ d.val) ^ i) * (ζ ^ d.val - 1) = 0 := by
      rw [geom_sum_mul, hxM, sub_self]
    rcases mul_eq_zero.mp hgeom with h | h
    · exact h
    · exact absurd (sub_eq_zero.mp h) hx1

/-! ## 2. The mark DFT and the exact Parseval identity -/

/-- the form factor (DFT) of an integer mark vector on the `M`-site grid:
`c_r = Σ_k m_k ζ^{(r·k).val}` — SPEC 1.4's `c_s` restricted to the grid, where it depends on `s`
only through `s mod M` (theorems.md T1, display (P)). -/
def dftMark (ζ : K) (m : ZMod M → ℤ) (r : ZMod M) : K :=
  ∑ k : ZMod M, (m k : K) * chi ζ (r * k)

/-- **DFT Parseval on `ZMod M`**, in the algebraic pairing `c_r · c_{−r}` (marks are integers, so over
`ℂ` this is `Σ_r |c_r|² = M Σ_k m_k²` — display (P) of theorems.md T1). -/
theorem sum_dftMark_mul_neg [IsDomain K] {ζ : K} (hζ : IsPrimitiveRoot ζ M) (m : ZMod M → ℤ) :
    ∑ r : ZMod M, dftMark ζ m r * dftMark ζ m (-r) = (M : K) * ∑ k : ZMod M, (m k : K) ^ 2 := by
  have hζ1 : ζ ^ (M : ℕ) = 1 := hζ.pow_eq_one
  have expand : ∀ r : ZMod M, dftMark ζ m r * dftMark ζ m (-r)
      = ∑ k : ZMod M, ∑ l : ZMod M, (m k : K) * (m l : K) * chi ζ (r * (k - l)) := by
    intro r
    unfold dftMark
    rw [Finset.sum_mul_sum]
    refine Finset.sum_congr rfl fun k _ => Finset.sum_congr rfl fun l _ => ?_
    have hchi : chi ζ (r * k) * chi ζ (-r * l) = chi ζ (r * (k - l)) := by
      rw [← chi_add hζ1]
      congr 1
      ring
    calc (m k : K) * chi ζ (r * k) * ((m l : K) * chi ζ (-r * l))
        = (m k : K) * (m l : K) * (chi ζ (r * k) * chi ζ (-r * l)) := by ring
      _ = (m k : K) * (m l : K) * chi ζ (r * (k - l)) := by rw [hchi]
  calc ∑ r : ZMod M, dftMark ζ m r * dftMark ζ m (-r)
      = ∑ r : ZMod M, ∑ k : ZMod M, ∑ l : ZMod M, (m k : K) * (m l : K) * chi ζ (r * (k - l)) :=
        Finset.sum_congr rfl fun r _ => expand r
    _ = ∑ k : ZMod M, ∑ r : ZMod M, ∑ l : ZMod M, (m k : K) * (m l : K) * chi ζ (r * (k - l)) :=
        Finset.sum_comm
    _ = ∑ k : ZMod M, ∑ l : ZMod M, ∑ r : ZMod M, (m k : K) * (m l : K) * chi ζ (r * (k - l)) :=
        Finset.sum_congr rfl fun k _ => Finset.sum_comm
    _ = ∑ k : ZMod M, ∑ l : ZMod M, (m k : K) * (m l : K) * (if k - l = 0 then (M : K) else 0) := by
        refine Finset.sum_congr rfl fun k _ => Finset.sum_congr rfl fun l _ => ?_
        rw [← Finset.mul_sum, sum_chi_mul hζ (k - l)]
    _ = ∑ k : ZMod M, (m k : K) * (m k : K) * (M : K) := by
        refine Finset.sum_congr rfl fun k _ => ?_
        have hdiag : ∀ l : ZMod M, (m k : K) * (m l : K) * (if k - l = 0 then (M : K) else 0)
            = if l = k then (m k : K) * (m l : K) * (M : K) else 0 := by
          intro l
          by_cases h : l = k
          · subst h
            simp
          · have h' : k - l ≠ 0 := sub_ne_zero.mpr (Ne.symm h)
            simp [h, h']
        calc ∑ l : ZMod M, (m k : K) * (m l : K) * (if k - l = 0 then (M : K) else 0)
            = ∑ l : ZMod M, (if l = k then (m k : K) * (m l : K) * (M : K) else 0) :=
              Finset.sum_congr rfl fun l _ => hdiag l
          _ = (m k : K) * (m k : K) * (M : K) := by
              rw [Finset.sum_ite_eq' Finset.univ k fun l => (m k : K) * (m l : K) * (M : K)]
              simp
    _ = (M : K) * ∑ k : ZMod M, (m k : K) ^ 2 := by
        rw [Finset.mul_sum]
        exact Finset.sum_congr rfl fun k _ => by ring

/-! ## 3. Flat-band collapse: `M` consecutive harmonics are a complete residue system -/

/-- summing any function of the residue over a band of `M` consecutive integers is summing over
`ZMod M` once: the band `Icc a (a + M − 1)` is a complete residue system mod `M`. -/
theorem sum_band {β : Type*} [AddCommMonoid β] (f : ZMod M → β) (a : ℤ) :
    ∑ s ∈ Finset.Icc a (a + (M : ℤ) - 1), f (s : ZMod M) = ∑ r : ZMod M, f r := by
  refine Finset.sum_nbij' (fun s => (s : ZMod M))
    (fun r => a + ((r - (a : ZMod M)).val : ℤ)) ?_ ?_ ?_ ?_ ?_
  · intro s _
    exact mem_univ _
  · intro r _
    have h := (r - (a : ZMod M)).val_lt
    rw [Finset.mem_Icc]
    omega
  · intro s hs
    rw [Finset.mem_Icc] at hs
    have h1 : (s : ZMod M) - (a : ZMod M) = ((s - a : ℤ) : ZMod M) := by
      push_cast
      ring
    rw [h1]
    have h2 : ((((s - a : ℤ) : ZMod M)).val : ℤ) = (s - a) % (M : ℤ) := ZMod.val_intCast _
    have h3 : (s - a) % (M : ℤ) = s - a := by
      have hM : 0 < (M : ℤ) := by
        have := Nat.pos_of_ne_zero (NeZero.ne M)
        omega
      exact Int.emod_eq_of_lt (by omega) (by omega)
    have h4 : ((((s - a : ℤ) : ZMod M)).val : ℤ) = s - a := by rw [h2, h3]
    omega
  · intro r _
    push_cast
    rw [ZMod.natCast_val, ZMod.cast_id]
    ring
  · intro s _
    rfl

/-- **flat-band double-sum collapse** (the structural form of T1's triangular-weight telescoping):
for any band of `M` consecutive integer harmonics,
`Σ_{j₁,j₂ ∈ B} f(j₁ + j₂ mod M) = M · Σ_{r : ZMod M} f r` — each residue class of the sum-set
`B + B` is hit by exactly `M` ordered pairs. -/
theorem sum_band_pair (f : ZMod M → K) (a : ℤ) :
    ∑ j1 ∈ Finset.Icc a (a + (M : ℤ) - 1), ∑ j2 ∈ Finset.Icc a (a + (M : ℤ) - 1),
        f ((j1 : ZMod M) + (j2 : ZMod M))
      = (M : K) * ∑ r : ZMod M, f r := by
  have hinner : ∀ j1 : ℤ,
      ∑ j2 ∈ Finset.Icc a (a + (M : ℤ) - 1), f ((j1 : ZMod M) + (j2 : ZMod M))
        = ∑ r : ZMod M, f r := by
    intro j1
    calc ∑ j2 ∈ Finset.Icc a (a + (M : ℤ) - 1), f ((j1 : ZMod M) + (j2 : ZMod M))
        = ∑ r : ZMod M, f ((j1 : ZMod M) + r) := sum_band (fun y => f ((j1 : ZMod M) + y)) a
      _ = ∑ r : ZMod M, f r := by
          simpa using Equiv.sum_comp (Equiv.addLeft (j1 : ZMod M)) f
  rw [Finset.sum_congr rfl fun j1 _ => hinner j1, Finset.sum_const]
  have hcard : (Finset.Icc a (a + (M : ℤ) - 1)).card = M := by
    rw [Int.card_Icc]
    omega
  rw [hcard, nsmul_eq_mul]

/-- **T1, Lemma 1.1 (general flat band, algebraic form).**  For ANY band of `M` consecutive integer
harmonics `B = Icc a (a+M−1)` and any integer mark vector on the `M`-site uniform grid,

    `Σ_{j₁,j₂ ∈ B} c(j₁+j₂) · c(−(j₁+j₂)) = M² · Σ_k m_k²`

— the unnormalized flat Frobenius row equals `M²` times the multiplicity count; dividing by the
uniform weights `u_j = 1/M` (squared) gives `tr Ĝ² = Σ_k m_k²` exactly.  Over `ℂ` the pairing
`c(s)·c(−s)` is `|c_s|²` (`dftMark_mul_neg_eq_normSq` below). -/
theorem flat_band_trace_sq [IsDomain K] {ζ : K} (hζ : IsPrimitiveRoot ζ M)
    (m : ZMod M → ℤ) (a : ℤ) :
    ∑ j1 ∈ Finset.Icc a (a + (M : ℤ) - 1), ∑ j2 ∈ Finset.Icc a (a + (M : ℤ) - 1),
        dftMark ζ m ((j1 : ZMod M) + (j2 : ZMod M))
          * dftMark ζ m (-((j1 : ZMod M) + (j2 : ZMod M)))
      = (M : K) ^ 2 * ∑ k : ZMod M, (m k : K) ^ 2 := by
  calc ∑ j1 ∈ Finset.Icc a (a + (M : ℤ) - 1), ∑ j2 ∈ Finset.Icc a (a + (M : ℤ) - 1),
        dftMark ζ m ((j1 : ZMod M) + (j2 : ZMod M))
          * dftMark ζ m (-((j1 : ZMod M) + (j2 : ZMod M)))
      = (M : K) * ∑ r : ZMod M, dftMark ζ m r * dftMark ζ m (-r) :=
        sum_band_pair (fun s => dftMark ζ m s * dftMark ζ m (-s)) a
    _ = (M : K) * ((M : K) * ∑ k : ZMod M, (m k : K) ^ 2) := by
        rw [sum_dftMark_mul_neg hζ m]
    _ = (M : K) ^ 2 * ∑ k : ZMod M, (m k : K) ^ 2 := by ring

/-! ## 4. Specialization to `ℂ`: the standard character, norm-squared form, headline theorem -/

/-- the standard primitive `M`-th root of unity `e^{2πi/M}` in `ℂ`. -/
def zetaM (M : ℕ) : ℂ := Complex.exp (2 * Real.pi * Complex.I / M)

lemma isPrimitiveRoot_zetaM (M : ℕ) [NeZero M] : IsPrimitiveRoot (zetaM M) M :=
  Complex.isPrimitiveRoot_exp M (NeZero.ne M)

lemma conj_zetaM (M : ℕ) : (starRingEnd ℂ) (zetaM M) = (zetaM M)⁻¹ := by
  unfold zetaM
  rw [← Complex.exp_conj, ← Complex.exp_neg]
  congr 1
  simp only [map_div₀, map_mul, Complex.conj_I, Complex.conj_ofReal, map_ofNat, map_natCast]
  ring

lemma conj_chi (x : ZMod M) :
    (starRingEnd ℂ) (chi (zetaM M) x) = chi (zetaM M) (-x) := by
  have hζ1 : (zetaM M) ^ (M : ℕ) = 1 := (isPrimitiveRoot_zetaM M).pow_eq_one
  have h1 : chi (zetaM M) x * chi (zetaM M) (-x) = 1 := chi_mul_chi_neg hζ1 x
  have h2 : (starRingEnd ℂ) (chi (zetaM M) x) = (chi (zetaM M) x)⁻¹ := by
    unfold chi
    rw [map_pow, conj_zetaM, inv_pow]
  rw [h2]
  exact (eq_inv_of_mul_eq_one_right h1).symm

/-- integer marks give a Hermitian form factor: `c_{−r} = conj c_r`. -/
lemma dftMark_neg (m : ZMod M → ℤ) (r : ZMod M) :
    dftMark (zetaM M) m (-r) = (starRingEnd ℂ) (dftMark (zetaM M) m r) := by
  unfold dftMark
  rw [map_sum]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [map_mul, map_intCast, conj_chi (r * k), neg_mul]

/-- over `ℂ` the algebraic pairing is the norm-squared: `c_r · c_{−r} = |c_r|²`. -/
lemma dftMark_mul_neg_eq_normSq (m : ZMod M → ℤ) (r : ZMod M) :
    dftMark (zetaM M) m r * dftMark (zetaM M) m (-r)
      = (Complex.normSq (dftMark (zetaM M) m r) : ℂ) := by
  rw [dftMark_neg, Complex.mul_conj]

/-- **T1, Theorem 1.2 — grid Parseval decoupling at bandwidth one (headline, unnormalized).**
Even period `N = 2n`, `M = N + 1 = 2n + 1` harmonics on the symmetric flat band `B = {−n, …, n}`
(`λ = 1`: `|j| ≤ N/2`), configuration on the `(N+1)`-site uniform grid with arbitrary integer marks
`m : ZMod (N+1) → ℤ`.  Then

    `Σ_{j₁,j₂ ∈ B} |c_{j₁+j₂}|² = (N+1)² · Σ_k m_k²`

exactly — for every site subset and every mark assignment.  With the uniform weights `u_j = 1/(N+1)`
this is `tr Ĝ² = Σ_k m_k²` (`trace_sq_grid`): the bandwidth-one flat reading sees only multiplicities
on the grid, never positions — the M2 gate's absorption mechanism. -/
theorem grid_parseval_decoupling (n : ℕ) (m : ZMod (2 * n + 1) → ℤ) :
    ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
        Complex.normSq (dftMark (zetaM (2 * n + 1)) m
          ((j1 : ZMod (2 * n + 1)) + (j2 : ZMod (2 * n + 1))))
      = ((2 * n + 1 : ℕ) : ℝ) ^ 2 * ∑ k : ZMod (2 * n + 1), (m k : ℝ) ^ 2 := by
  have hC := flat_band_trace_sq (K := ℂ) (isPrimitiveRoot_zetaM (2 * n + 1)) m (-(n : ℤ))
  have hband : (-(n : ℤ) + ((2 * n + 1 : ℕ) : ℤ) - 1) = (n : ℤ) := by
    push_cast
    ring
  rw [hband] at hC
  have hC2 : ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
      (Complex.normSq (dftMark (zetaM (2 * n + 1)) m
        ((j1 : ZMod (2 * n + 1)) + (j2 : ZMod (2 * n + 1)))) : ℂ)
      = ((2 * n + 1 : ℕ) : ℂ) ^ 2 * ∑ k : ZMod (2 * n + 1), ((m k : ℂ)) ^ 2 := by
    rw [← hC]
    exact Finset.sum_congr rfl fun j1 _ => Finset.sum_congr rfl fun j2 _ =>
      (dftMark_mul_neg_eq_normSq m _).symm
  exact_mod_cast hC2

/-- **T1, Theorem 1.2 — normalized form**: the literal SPEC-1.4 Frobenius row with uniform weights
`u_{j₁} u_{j₂} = (1/M)²`, `M = N + 1 = 2n + 1`:

    `tr Ĝ² = Σ_{j₁,j₂ ∈ B} u_{j₁} u_{j₂} |c_{j₁+j₂}|² = Σ_k m_k²`  exactly. -/
theorem trace_sq_grid (n : ℕ) (m : ZMod (2 * n + 1) → ℤ) :
    ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
        (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1)) *
          Complex.normSq (dftMark (zetaM (2 * n + 1)) m
            ((j1 : ZMod (2 * n + 1)) + (j2 : ZMod (2 * n + 1))))
      = ∑ k : ZMod (2 * n + 1), (m k : ℝ) ^ 2 := by
  simp only [← Finset.mul_sum]
  rw [grid_parseval_decoupling n m]
  have hM : ((2 * n + 1 : ℕ) : ℝ) = 2 * (n : ℝ) + 1 := by
    push_cast
    ring
  rw [hM]
  have hne : (2 * (n : ℝ) + 1) ≠ 0 := by positivity
  field_simp

/-! ## 5. The literal triangular-weight telescoping (T1's key-lemma bookkeeping)

The flat bandwidth-one weights at `M = N + 1` are `u_s = (M − |s|)/M²` on `|s| ≤ N` (the triangular
pair counts of the sum-set `B + B`, `B = {−N/2, …, N/2}`, divided by `M²`).  The telescoping: on every
residue class mod `M` inside `|s| ≤ N` they sum to exactly `1/M`.  The zero class meets the window in
`s = 0` alone (weight `M/M²`); every nonzero class `r` meets it in exactly the two points `r.val` and
`r.val − M`, whose triangular counts sum to `(M − r.val) + r.val = M`.  This is the residue-class
computation of theorems.md T1 / AUDIT 3.1 in its literal form; `sum_band_pair` above is the same fact
stated structurally, and it is what the main theorem consumes. -/

/-- **weight telescoping, integer core**: for every residue `r` mod `N + 1`,
`Σ_{s ∈ [−N, N], s ≡ r (N+1)} ((N+1) − |s|) = N + 1`. -/
theorem weight_telescoping (N : ℕ) (r : ZMod (N + 1)) :
    ∑ s ∈ (Finset.Icc (-(N : ℤ)) (N : ℤ)).filter (fun s : ℤ => (s : ZMod (N + 1)) = r),
        (((N : ℤ) + 1) - |s|) = (N : ℤ) + 1 := by
  have hs0cast : ((r.val : ℤ) : ZMod (N + 1)) = r := by
    push_cast
    exact ZMod.natCast_rightInverse r
  by_cases hr : r = 0
  · subst hr
    have hfilter : (Finset.Icc (-(N : ℤ)) (N : ℤ)).filter
        (fun s : ℤ => (s : ZMod (N + 1)) = 0) = {0} := by
      ext s
      simp only [Finset.mem_filter, Finset.mem_Icc, Finset.mem_singleton]
      constructor
      · rintro ⟨⟨h1, h2⟩, hcast⟩
        have hdvd : ((N : ℤ) + 1) ∣ s := by
          have h := (ZMod.intCast_zmod_eq_zero_iff_dvd s (N + 1)).mp hcast
          exact_mod_cast h
        exact int_eq_zero_of_dvd_of_bounds (by omega) hdvd (by omega) (by omega)
      · rintro rfl
        exact ⟨⟨by omega, by omega⟩, Int.cast_zero⟩
    rw [hfilter, Finset.sum_singleton]
    simp
  · have hval_pos : 1 ≤ (r.val : ℤ) := by
      have h0 : r.val ≠ 0 := fun h => hr ((ZMod.val_eq_zero r).mp h)
      omega
    have hval_le : (r.val : ℤ) ≤ (N : ℤ) := by
      have h := r.val_lt
      omega
    have hfilter : (Finset.Icc (-(N : ℤ)) (N : ℤ)).filter
        (fun s : ℤ => (s : ZMod (N + 1)) = r)
        = {(r.val : ℤ), (r.val : ℤ) - ((N : ℤ) + 1)} := by
      ext s
      simp only [Finset.mem_filter, Finset.mem_Icc, Finset.mem_insert, Finset.mem_singleton]
      constructor
      · rintro ⟨⟨h1, h2⟩, hcast⟩
        have hz : ((s - (r.val : ℤ) : ℤ) : ZMod (N + 1)) = 0 := by
          push_cast
          rw [hcast, ZMod.natCast_rightInverse r, sub_self]
        have hdvd : ((N : ℤ) + 1) ∣ (s - (r.val : ℤ)) := by
          have h := (ZMod.intCast_zmod_eq_zero_iff_dvd (s - (r.val : ℤ)) (N + 1)).mp hz
          exact_mod_cast h
        rcases int_eq_zero_or_neg_of_dvd_of_bounds (by omega) hdvd (by omega) (by omega)
          with h | h
        · left; omega
        · right; omega
      · have hsplit : (((r.val : ℤ) - ((N : ℤ) + 1) : ℤ) : ZMod (N + 1))
            = ((r.val : ℤ) : ZMod (N + 1)) - ((((N : ℤ) + 1) : ℤ) : ZMod (N + 1)) := by
          push_cast
          ring
        have hMzero : ((((N : ℤ) + 1) : ℤ) : ZMod (N + 1)) = 0 := by
          rw [ZMod.intCast_zmod_eq_zero_iff_dvd]
          exact_mod_cast dvd_refl ((N : ℤ) + 1)
        rintro (rfl | rfl)
        · exact ⟨⟨by omega, by omega⟩, hs0cast⟩
        · refine ⟨⟨by omega, by omega⟩, ?_⟩
          rw [hsplit, hMzero, hs0cast, sub_zero]
    rw [hfilter]
    have hne : (r.val : ℤ) ≠ (r.val : ℤ) - ((N : ℤ) + 1) := by omega
    rw [Finset.sum_pair hne]
    have h1 : |(r.val : ℤ)| = (r.val : ℤ) := abs_of_nonneg (by omega)
    have h2 : |(r.val : ℤ) - ((N : ℤ) + 1)| = ((N : ℤ) + 1) - (r.val : ℤ) := by
      rw [abs_of_nonpos (by omega)]
      ring
    rw [h1, h2]
    ring

/-- **weight telescoping, normalized form** (the literal T1 statement): with the flat bandwidth-one
harmonic weights `u_s = (M − |s|)/M²` (`M = N + 1`, support `|s| ≤ N`), every residue class mod `M`
carries total weight exactly `1/M`. -/
theorem weight_telescoping_rat (N : ℕ) (r : ZMod (N + 1)) :
    ∑ s ∈ (Finset.Icc (-(N : ℤ)) (N : ℤ)).filter (fun s : ℤ => (s : ZMod (N + 1)) = r),
        (((N : ℚ) + 1) - |(s : ℚ)|) / ((N : ℚ) + 1) ^ 2 = 1 / ((N : ℚ) + 1) := by
  have key := weight_telescoping N r
  have hcast : ∑ s ∈ (Finset.Icc (-(N : ℤ)) (N : ℤ)).filter
        (fun s : ℤ => (s : ZMod (N + 1)) = r), (((N : ℚ) + 1) - |(s : ℚ)|)
      = ((∑ s ∈ (Finset.Icc (-(N : ℤ)) (N : ℤ)).filter
          (fun s : ℤ => (s : ZMod (N + 1)) = r), (((N : ℤ) + 1) - |s|) : ℤ) : ℚ) := by
    push_cast
    rfl
  have hne : ((N : ℚ) + 1) ≠ 0 := by positivity
  simp only [div_eq_mul_inv]
  rw [← Finset.sum_mul, hcast, key]
  push_cast
  field_simp

/-! ## 6. Corner transfer: the doubles-corner arithmetic on grid marks (lemmaR_tight interface) -/

/-- **theorems.md Lemma 2.2(a), the doubles-corner inequality**: for any nonnegative integer marks,
`3·(Σ m) − Σ m² ≤ 2·N_d` where `N_d` is the number of occupied sites; equality forces marks ⊆ {1, 2}.
Per site this is `(m − 1)(m − 2) ≥ 0`.  Combined with the main identity (`F1 = Σ m²` on the grid,
`trace_sq_grid`) and mass `Σ m = N`, this is the corner bound `N_d ≥ (3N − F1)/2` that the two-moment
(lemmaR_tight) budget turns into the `5/6 − (2/3)ε` corner — the baseline the M2 gate showed the cubic
block cannot move.  (The ε-budget LP layer, Theorem 2.3, is not formalized here.) -/
theorem two_mul_distinct_ge (m : ZMod M → ℤ) (hm : ∀ k, 0 ≤ m k) :
    3 * (∑ k : ZMod M, m k) - (∑ k : ZMod M, (m k) ^ 2)
      ≤ 2 * ((Finset.univ.filter (fun k : ZMod M => m k ≠ 0)).card : ℤ) := by
  have pointwise : ∀ k : ZMod M,
      3 * m k - (m k) ^ 2 ≤ 2 * (if m k ≠ 0 then (1 : ℤ) else 0) := by
    intro k
    by_cases h : m k = 0
    · simp [h]
    · rw [if_pos h]
      have h1 : 1 ≤ m k := by
        have := hm k
        omega
      rcases (by omega : m k = 1 ∨ 2 ≤ m k) with hmk | h2
      · rw [hmk]
        norm_num
      · nlinarith [mul_nonneg (by omega : (0 : ℤ) ≤ m k - 1) (by omega : (0 : ℤ) ≤ m k - 2)]
  calc 3 * (∑ k : ZMod M, m k) - (∑ k : ZMod M, (m k) ^ 2)
      = ∑ k : ZMod M, (3 * m k - (m k) ^ 2) := by
        rw [Finset.mul_sum, Finset.sum_sub_distrib]
    _ ≤ ∑ k : ZMod M, 2 * (if m k ≠ 0 then (1 : ℤ) else 0) :=
        Finset.sum_le_sum fun k _ => pointwise k
    _ = 2 * ((Finset.univ.filter (fun k : ZMod M => m k ≠ 0)).card : ℤ) := by
        rw [← Finset.mul_sum, Finset.card_filter]
        push_cast
        rfl

/-- corner transfer with the mass row substituted: mass `Σ m = N` gives `3N − Σ m² ≤ 2 N_d`;
on the grid `Σ m² = F1` exactly (`trace_sq_grid`), so this reads `N_d ≥ (3N − F1)/2`. -/
theorem corner_transfer (m : ZMod M → ℤ) (hm : ∀ k, 0 ≤ m k) (N : ℤ)
    (hmass : ∑ k : ZMod M, m k = N) :
    3 * N - (∑ k : ZMod M, (m k) ^ 2)
      ≤ 2 * ((Finset.univ.filter (fun k : ZMod M => m k ≠ 0)).card : ℤ) := by
  rw [← hmass]
  exact two_mul_distinct_ge m hm

end GridParseval
end PairCeiling
end Zeta23
