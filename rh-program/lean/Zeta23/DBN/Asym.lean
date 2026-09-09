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
Zeta23/DBN/Asym.lean — the ASYMPTOTIC-LANE layer (Lane A) of the de Bruijn–Newman milestone M2a
(rh-program/results/d1-m2a/SPEC.md v1.0, 2026-09-02: §5, §7.2, §7.4, §8.1–8.3; the stream plan
rh-program/results/d1-m2a/lane-a/PLAN.md of 2026-09-09, reviewed in PLAN-REVIEW.md): the transcript
data types (`AsymRow`, `TailRow`, `AsymData`; SPEC §7.2, §8.2), the integer checker `checkAsym`
(C-A1 … C-A6, SPEC §7.4), the displayed hypotheses H2-A (`AsymEnclOK`) and H-TAIL (`TailOK`)
(SPEC §8.1), the soundness theorem `cert_of_checkAsym` (SPEC §8.3, proof = SPEC §5.6), and the two
window-index lemmas L-A2 (`windowIdx_mono`) and L-A1 at row 2 (`row2_windowIdx_ge`) (SPEC §5.3, §6).

WHAT THE CERTIFICATE CERTIFIES (SPEC §1.3, Lane A).  For a normalized function g : ℂ → ℂ
(instance: g z = H_{t₀}(z)/B_{t₀}(z) at t₀ = 93/500), the window index N(x) = ⌊√(x/(4π) + t₀/16)⌋
(Polymath15 (19), p6), a y-band [y₀, yA] with yA² ≥ 1 − 2t₀, a list of consecutive window rows
[N₋, N₊] each carrying a modulus floor T/K and a defect bound E/K with 0 ≤ E < T, and a tail row
at N₁ = (last N₊) + 1.  Conclusion (`cert_of_checkAsym`):

    ∀ x y, (some row's N₋ ≤ N(x)) → y₀ ≤ y → y ≤ yA → g (x + y·I) ≠ 0.

Either N(x) lies in a row — then H2-A's floor (T − E)/K > 0 forbids a zero — or N(x) ≥ N₁ and
H-TAIL applies.  The coverage step (C-A3, C-A4, C-A5 + `cover_of_consecutive`) is what the kernel
adds to the displayed hypotheses; L-A1 + L-A2 connect x ≥ X + 1 to N(x) ≥ N₋ of the first row.

TRUST MODEL (D-R3 / D-R8, binding; SPEC §3.7, §6).  The honest label is, verbatim, "kernel-checked
modulo the displayed hypotheses" — here H2-A (`AsymEnclOK g d`, the window-row floors) and H-TAIL
(`TailOK g d`, nonvanishing beyond N₁), besides H1, H2-B, H3 of Instance02.lean.  Never "fully
machine-checked".  The producers (results/d1-m2a/lane-a/p9_mp.py, p9_arb.py) are UNTRUSTED; their
numbers enter the trusted statement only through the displayed hypotheses and the integer literal.
The kernel checks integer relations only (`decide +kernel` on the literal; +, ·, ^2, comparisons
on ℤ and a ℕ length; no `native_decide`); it does not see t₀, x, y or any real number.

WHAT THE KERNEL DOES NOT USE (PLAN-REVIEW F-6, SPEC §5.1).  `cert_of_checkAsym` consumes only
K ≥ 1 (one conjunct of C-A1), C-A3, C-A4 and C-A5.  C-A2, C-A6 (the tail row's Q₁+Q₂+Q₃+Q₄+E₁ < 2K)
and C-A1's yA² ≥ 1 − 2t₀ are checked by `decide +kernel` on the literal but never used by the
proof: they are recorded evidence for the prose discharge of Lemma T (SPEC §5.4) and of the y-band
condition, exactly as SPEC §5.1 designs it ("the row is evidence, the reduction is displayed").
"C-A6 is kernel-checked" must not be read as "the tail reduction is kernel-checked".

WHAT IS PROVED HERE (all sorry-free; `#print axioms` = propext, Classical.choice, Quot.sound):
  * `cover_of_consecutive` — coverage: in a consecutive row list every integer between some row's
    N₋ and the last N₊ lies in a row (uses C-A4 only);
  * `cert_of_checkAsym`    — the soundness theorem (SPEC §8.3, statement verbatim; proof SPEC §5.6);
  * `windowIdx_mono`       — L-A2: N(x) is monotone in x;
  * `row2_windowIdx_ge`    — L-A1 at row 2: x ≥ 5 000 000 194 859 ⟹ N(x) ≥ 630 783 at t₀ = 93/500,
    from π < 3.141593 (`Real.pi_lt_d6`); margin ≈ 1.71·10⁶ (PLAN §1.3, PLAN-REVIEW A13).

NOT HERE.  The Lane A literals (one per producer leg, never merged: D-R3), their kernel facts
`checkAsym row2Asym… = true := by decide +kernel`, and the glue lemmas that turn
`cert_of_checkAsym` into the exact statement `lambda_le_point2` consumes (PLAN §1.5) live in
Zeta23/DBN/Instance02/Asym_mp.lean and Asym_arb.lean, emitted from the producers' transcripts
after the run; Instance02.lean imports them.  Every definition and proof below is the text of
results/d1-m2a/lane-a/laneA-shapes-scratch.lean (elaborated 2026-09-09, log
laneA-shapes-typecheck.log) and of the reviewer's re-elaboration review-shapes.lean,
re-namespaced from `Zeta23.DBN.LaneAScratch` to `Zeta23.DBN`.

Builder stamp: 2026-09-09 (Session 19); `lake build -j2`; Lean v4.33.0-rc2, Mathlib 51e6992.
-/
import Zeta23.DBN.Defs
import Mathlib.Analysis.Real.Pi.Bounds

open scoped Real
open Complex (I)

noncomputable section

namespace Zeta23
namespace DBN

/-! ## Asymptotic-lane data (SPEC §7.2, §8.2) -/

/-- the window index N(x) = ⌊√(x/(4π) + t/16)⌋ (Polymath15 (19), p6). -/
def windowIdx (t x : ℝ) : ℕ := ⌊Real.sqrt (x / (4 * π) + t / 16)⌋₊

/-- a window row (SPEC §5.2): windows N ∈ [Nlo, Nhi], modulus floor T/K, defect bound E/K. -/
structure AsymRow where
  Nlo : ℤ
  Nhi : ℤ
  T : ℤ
  E : ℤ

/-- the tail row (SPEC §5.4, Lemma T): N₁ and the five parts Q₁ … Q₄, E₁ (each ⌈K·⌉). -/
structure TailRow where
  N1 : ℤ
  Q1 : ℤ
  Q2 : ℤ
  Q3 : ℤ
  Q4 : ℤ
  E1 : ℤ

/-- the Lane A transcript data: scale K, t₀ = t0n/t0d, y₀ = y0n/y0d, yA = yAn/yAd, rows, tail. -/
structure AsymData where
  K : ℤ
  t0n : ℤ
  t0d : ℤ
  y0n : ℤ
  y0d : ℤ
  yAn : ℤ
  yAd : ℤ
  rows : List AsymRow
  tail : TailRow

/-- C-A3 per row: Nlo ≤ Nhi and 0 ≤ E < T. -/
def checkAsymRow (r : AsymRow) : Bool :=
  decide (r.Nlo ≤ r.Nhi) && decide (0 ≤ r.E) && decide (r.E < r.T)

/-- C-A4: consecutive rows (next.Nlo = Nhi + 1). -/
def consecutive : List AsymRow → Bool
  | [] => true
  | [_] => true
  | r :: s :: l => decide (s.Nlo = r.Nhi + 1) && consecutive (s :: l)

/-- the last row's Nhi (0 on the empty list, which C-A2 excludes). -/
def lastNhi : List AsymRow → ℤ
  | [] => 0
  | [r] => r.Nhi
  | _ :: s :: l => lastNhi (s :: l)

/-- **`checkAsym`** — C-A1 … C-A6 (SPEC §7.4).  Integer arithmetic only: `decide +kernel` on a literal. -/
def checkAsym (d : AsymData) : Bool :=
  decide (1 ≤ d.K) && decide (1 ≤ d.t0d) && decide (0 < d.t0n) && decide (1 ≤ d.y0d)
    && decide (0 < d.y0n) && decide (1 ≤ d.yAd) && decide (0 ≤ d.yAn)
    -- C-A1: yA² ≥ 1 − 2t₀  ⟺  (t0d − 2·t0n)·yAd² ≤ yAn²·t0d
    && decide ((d.t0d - 2 * d.t0n) * d.yAd ^ 2 ≤ d.yAn ^ 2 * d.t0d)
    && decide (0 < d.rows.length)                                        -- C-A2
    && d.rows.all checkAsymRow && consecutive d.rows                      -- C-A3, C-A4
    && decide (d.tail.N1 = lastNhi d.rows + 1)                            -- C-A5
    && decide (0 ≤ d.tail.Q1) && decide (0 ≤ d.tail.Q2) && decide (0 ≤ d.tail.Q3)
    && decide (0 ≤ d.tail.Q4) && decide (0 ≤ d.tail.E1)
    && decide (d.tail.Q1 + d.tail.Q2 + d.tail.Q3 + d.tail.Q4 + d.tail.E1 < 2 * d.K)   -- C-A6

/-- t₀ of the transcript as a real. -/
def At0 (d : AsymData) : ℝ := (d.t0n : ℝ) / d.t0d
/-- y₀ of the transcript as a real. -/
def Ay0 (d : AsymData) : ℝ := (d.y0n : ℝ) / d.y0d
/-- yA of the transcript as a real. -/
def AyA (d : AsymData) : ℝ := (d.yAn : ℝ) / d.yAd

/-- **H2-A** (SPEC §8.1): every window row's floor holds for the normalized function at time t₀. -/
def AsymEnclOK (g : ℂ → ℂ) (d : AsymData) : Prop :=
  ∀ r ∈ d.rows, ∀ x y : ℝ, (r.Nlo : ℝ) ≤ windowIdx (At0 d) x → (windowIdx (At0 d) x : ℝ) ≤ r.Nhi →
    Ay0 d ≤ y → y ≤ AyA d → ((r.T : ℝ) - r.E) / d.K ≤ ‖g (x + y * I)‖

/-- **H-TAIL** (SPEC §8.1, conclusion form): nonvanishing beyond the last window. -/
def TailOK (g : ℂ → ℂ) (d : AsymData) : Prop :=
  ∀ x y : ℝ, (d.tail.N1 : ℝ) ≤ windowIdx (At0 d) x → Ay0 d ≤ y → y ≤ AyA d → g (x + y * I) ≠ 0

/-! ## The soundness theorem (SPEC §5.6, §8.3) -/

/-- coverage: in a consecutive row list, every integer n between some row's Nlo and the last Nhi lies in a row. -/
theorem cover_of_consecutive : ∀ (l : List AsymRow) (r : AsymRow), r ∈ l → consecutive l = true →
    ∀ n : ℤ, r.Nlo ≤ n → n ≤ lastNhi l → ∃ r' ∈ l, r'.Nlo ≤ n ∧ n ≤ r'.Nhi
  | [], _, hr, _, _, _, _ => absurd hr List.not_mem_nil
  | [r0], r, hr, _, n, hlo, hhi => by
      have h := List.mem_singleton.mp hr
      subst h
      exact ⟨r, List.mem_singleton.mpr rfl, hlo, hhi⟩
  | r0 :: s :: l, r, hr, hc, n, hlo, hhi => by
      simp only [consecutive, Bool.and_eq_true, decide_eq_true_eq] at hc
      obtain ⟨hs, hc'⟩ := hc
      have hlast : lastNhi (r0 :: s :: l) = lastNhi (s :: l) := rfl
      rw [hlast] at hhi
      rcases List.mem_cons.mp hr with hr0 | hr'
      · subst hr0
        by_cases hn : n ≤ r.Nhi
        · exact ⟨r, List.mem_cons_self, hlo, hn⟩
        · have hsn : s.Nlo ≤ n := by rw [hs]; omega
          obtain ⟨r', hm, h1, h2⟩ := cover_of_consecutive (s :: l) s List.mem_cons_self hc' n hsn hhi
          exact ⟨r', List.mem_cons_of_mem _ hm, h1, h2⟩
      · obtain ⟨r', hm, h1, h2⟩ := cover_of_consecutive (s :: l) r hr' hc' n hlo hhi
        exact ⟨r', List.mem_cons_of_mem _ hm, h1, h2⟩

/-- **`cert_of_checkAsym`** (SPEC §8.3, statement verbatim; proof = SPEC §5.6): for x with N(x) at or beyond some
row's Nlo and y ∈ [y₀, yA], g(x + iy) ≠ 0 — either N(x) is in a row (C-A3, C-A4: floor (T − E)/K > 0) or
N(x) ≥ N₁ (C-A5: the tail).  Consumes K ≥ 1, C-A3, C-A4, C-A5 only (the remaining clauses are checked evidence). -/
theorem cert_of_checkAsym (g : ℂ → ℂ) (d : AsymData) (hc : checkAsym d = true)
    (hEncl : AsymEnclOK g d) (hTail : TailOK g d) :
    ∀ x y : ℝ, ∀ r ∈ d.rows, (r.Nlo : ℝ) ≤ windowIdx (At0 d) x →
      Ay0 d ≤ y → y ≤ AyA d → g (x + y * I) ≠ 0 := by
  intro x y r hr hlo hy0 hyA
  simp only [checkAsym, Bool.and_eq_true, decide_eq_true_eq, List.all_eq_true] at hc
  obtain ⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨⟨hK, -⟩, -⟩, -⟩, -⟩, -⟩, -⟩, -⟩, -⟩, hrows⟩, hcons⟩, hN1⟩, -⟩, -⟩, -⟩, -⟩, -⟩, -⟩ := hc
  set n : ℕ := windowIdx (At0 d) x with hn
  have hlo' : r.Nlo ≤ (n : ℤ) := by exact_mod_cast hlo
  by_cases hle : (n : ℤ) ≤ lastNhi d.rows
  · obtain ⟨r', hm, h1, h2⟩ := cover_of_consecutive d.rows r hr hcons n hlo' hle
    have hfloor := hEncl r' hm x y (by exact_mod_cast h1) (by exact_mod_cast h2) hy0 hyA
    have hrow := hrows r' hm
    simp only [checkAsymRow, Bool.and_eq_true, decide_eq_true_eq] at hrow
    obtain ⟨⟨-, -⟩, hET⟩ := hrow
    have hpos : (0 : ℝ) < ((r'.T : ℝ) - r'.E) / d.K := by
      apply div_pos
      · have : (r'.E : ℝ) < r'.T := by exact_mod_cast hET
        linarith
      · have : (1 : ℝ) ≤ d.K := by exact_mod_cast hK
        linarith
    intro h0
    rw [h0, norm_zero] at hfloor
    linarith
  · push Not at hle
    have hN1' : (d.tail.N1 : ℝ) ≤ n := by
      have : d.tail.N1 ≤ (n : ℤ) := by rw [hN1]; omega
      exact_mod_cast this
    exact hTail x y hN1' hy0 hyA

/-! ## L-A2 and L-A1 (SPEC §5.3, §6) -/

/-- **L-A2**: `windowIdx` is monotone in x (floor ∘ sqrt ∘ affine, all monotone). -/
theorem windowIdx_mono (t : ℝ) {x x' : ℝ} (h : x ≤ x') : windowIdx t x ≤ windowIdx t x' := by
  unfold windowIdx
  apply Nat.floor_mono
  apply Real.sqrt_le_sqrt
  have hpi : (0 : ℝ) ≤ 4 * π := by positivity
  have := div_le_div_of_nonneg_right h hpi
  linarith

/-- **L-A1** at row 2 (the instance of Instance02.lean: t₀ = 93/500, X = 5000000194858, N_start = 630783):
N(x) ≥ 630783 for every x ≥ X + 1 = 5000000194859, from π < 3.141593 (`Real.pi_lt_d6`):
630783² · 4 · 3.141593 − 3.141593 · (93/500)/4 = 4 999 998 482 392.06 < 5 000 000 194 859
(margin ≈ 1.71·10⁶, three quarters of the 2.26·10⁶ slack of x_{N₀}; SPEC §5.3, PLAN §1.3). -/
theorem row2_windowIdx_ge (x : ℝ) (hx : 5000000194858 + 1 ≤ x) :
    (630783 : ℝ) ≤ windowIdx (93 / 500) x := by
  have h : (630783 : ℕ) ≤ windowIdx (93 / 500) x := by
    unfold windowIdx
    apply Nat.le_floor
    apply Real.le_sqrt_of_sq_le
    have hpi := Real.pi_lt_d6
    have hpi0 := Real.pi_pos
    have key : ((630783 : ℕ) : ℝ) ^ 2 - 93 / 500 / 16 ≤ x / (4 * π) := by
      rw [le_div_iff₀ (by positivity)]
      push_cast
      nlinarith
    linarith
  exact_mod_cast h

end DBN
end Zeta23

end
