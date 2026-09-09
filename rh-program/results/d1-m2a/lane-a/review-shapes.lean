/-
laneA-shapes-scratch.lean — Lane A (SPEC §5, §7.4, §8.3) shape-and-proof scratch, Session 19 (2026-09-09).
NOT a program file; lives in results/d1-m2a/lane-a/ and is checked with `lake env lean` from
~/rh-lean-work/zeta-23-lean-main WITHOUT touching the tree.  Purpose: (1) re-elaborate the SPEC §8 Lane A shapes
against the pinned toolchain (Lean v4.33.0-rc2, Mathlib 51e6992), (2) PROVE `cert_of_checkAsym` (SPEC §5.6), L-A1 and
L-A2 with `#print axioms`, (3) show the one-line substitution that replaces `hLaneA`, (4) time `decide +kernel` on a
3-row literal.  The literal below is a PLACEHOLDER built from the float plan (rows-plan.json) — NOT a certificate;
the real literal is emitted from the producers' transcripts (PLAN.md §3) after the run.
-/
import Zeta23.DBN.Instance02
import Mathlib.Analysis.Real.Pi.Bounds

open scoped Real
open Complex (I)

noncomputable section

namespace Zeta23
namespace DBN
namespace LaneAReview

/-! ## C. Asymptotic-lane data (SPEC §7.2, §8.2; text as lean-shapes-scratch.lean §C) -/

/-- the window index N(x) = ⌊√(x/(4π) + t/16)⌋ (Polymath15 (19), p6). -/
def windowIdx (t x : ℝ) : ℕ := ⌊Real.sqrt (x / (4 * π) + t / 16)⌋₊

structure AsymRow where
  Nlo : ℤ
  Nhi : ℤ
  T : ℤ
  E : ℤ

structure TailRow where
  N1 : ℤ
  Q1 : ℤ
  Q2 : ℤ
  Q3 : ℤ
  Q4 : ℤ
  E1 : ℤ

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

def checkAsymRow (r : AsymRow) : Bool :=
  decide (r.Nlo ≤ r.Nhi) && decide (0 ≤ r.E) && decide (r.E < r.T)

def consecutive : List AsymRow → Bool
  | [] => true
  | [_] => true
  | r :: s :: l => decide (s.Nlo = r.Nhi + 1) && consecutive (s :: l)

def lastNhi : List AsymRow → ℤ
  | [] => 0
  | [r] => r.Nhi
  | _ :: s :: l => lastNhi (s :: l)

/-- C-A1 … C-A6 (SPEC §7.4). -/
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

def At0 (d : AsymData) : ℝ := (d.t0n : ℝ) / d.t0d
def Ay0 (d : AsymData) : ℝ := (d.y0n : ℝ) / d.y0d
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
N(x) ≥ N₁ (C-A5: the tail). -/
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

/-- **L-A1** at row 2: N(x) ≥ N_start = 630783 for every x ≥ X + 1 = 5000000194859, from π < 3.141593
(`Real.pi_lt_d6`): 630783² · 4π < 397887193089 · 12.566372 = 4 999 998 482 392.4… < 5 000 000 194 859 (margin
≈ 1.71·10⁶; SPEC §5.3). -/
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

/-! ## The row-2 literal shape (PLACEHOLDER integers from the float plan — NOT a certificate) and the glue -/

/-- PLACEHOLDER (float plan at K = 10²⁴, rows-plan.json; the producers' integers replace these). -/
def row2AsymPH : AsymData :=
  { K := 1000000000000000000000000, t0n := 93, t0d := 500, y0n := 16733, y0d := 100000,
    yAn := 3962323, yAd := 5000000,
    rows := [⟨630783, 746495, 12024973119483228431447, 103072746104089832⟩,
             ⟨746496, 1469440, 12023753401990763464701, 75688472821864900⟩,
             ⟨1469441, 5140999, 154429988491065955935610, 21290645196871800⟩],
    tail := ⟨5141000, 1780738467557306359267955, 178607151155365129202580, 18638466997109619932572,
             19014989006495779111373, 1822922214943886⟩ }

theorem row2AsymPH_check : checkAsym row2AsymPH = true := by decide +kernel

/-- negative controls: a gap in the rows (C-A4) and a tail sum ≥ 2K (C-A6). -/
theorem row2AsymPH_gap : checkAsym { row2AsymPH with
    rows := [⟨630783, 746495, 12024973119483228431447, 103072746104089832⟩,
             ⟨746497, 1469440, 12023753401990763464701, 75688472821864900⟩,
             ⟨1469441, 5140999, 154429988491065955935610, 21290645196871800⟩] } = false := by decide +kernel
theorem row2AsymPH_tail : checkAsym { row2AsymPH with
    tail := ⟨5141000, 1780738467557306359267955, 178607151155365129202580, 18638466997109619932572,
             19014989006495779111373, 1822922214943886 + 4000000000000000000000⟩ } = false := by decide +kernel

theorem row2AsymPH_t0 : At0 row2AsymPH = 93 / 500 := by simp [At0, row2AsymPH]
theorem row2AsymPH_y0 : Ay0 row2AsymPH = 16733 / 100000 := by simp [Ay0, row2AsymPH]
theorem row2AsymPH_yA : AyA row2AsymPH = 3962323 / 5000000 := by simp [AyA, row2AsymPH]

/-- **The glue lemma**: from the kernel fact, H2-A and H-TAIL for the literal, exactly the statement `hLaneA`
that `lambda_le_point2` consumes (Instance02.lean §2) — so the replacement there is the one-line substitution
`hLaneA ↦ row2_laneA hAsym hTail`. -/
theorem row2_laneA
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymPH)
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymPH) :
    ∀ x y : ℝ, 5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y →
      y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (x + y * I) ≠ 0 := by
  intro x y hx hy0 hy2
  have hyA : y ≤ 3962323 / 5000000 := by
    apply le_of_sq_le_sq _ (by norm_num)
    nlinarith
  have hg := cert_of_checkAsym _ row2AsymPH row2AsymPH_check hAsym hTail x y
    ⟨630783, 746495, 12024973119483228431447, 103072746104089832⟩ (by simp [row2AsymPH])
    (by rw [row2AsymPH_t0]; exact row2_windowIdx_ge x hx)
    (by rw [row2AsymPH_y0]; exact hy0) (by rw [row2AsymPH_yA]; exact hyA)
  exact (div_ne_zero_iff.mp hg).1


/-! ## REVIEWER'S TRUST-CRITICAL CHECK (Session 19 review, 2026-09-09)
The definitive test that `cert_of_checkAsym`'s conclusion, routed through the glue lemma, is
EXACTLY what `lambda_le_point2` consumes as `hLaneA`: feed `row2_laneA hAsym hTail` into the real
`Zeta23.DBN.Instance02.lambda_le_point2` (and `_arb`, and `row2_ray_mp`) from the built tree.
If the shapes disagreed by one character this file would not elaborate. -/

open Zeta23.DBN.Instance02 in
example
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierMP)
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymPH)
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymPH)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 :=
  lambda_le_point2 hH1 hEncl (row2_laneA hAsym hTail) hH3

open Zeta23.DBN.Instance02 in
example
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierARB)
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymPH)
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymPH)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 :=
  lambda_le_point2_arb hH1 hEncl (row2_laneA hAsym hTail) hH3

open Zeta23.DBN.Instance02 in
example
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierMP)
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymPH)
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymPH)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, 93 / 500 + (16733 / 100000) ^ 2 / 2 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 :=
  row2_ray_mp hH1 hEncl (row2_laneA hAsym hTail) hH3

-- the window count and C-A5 as kernel facts on the plan's integers
theorem review_windows : (5141000 : ℤ) - 630783 = 4510217 := by decide +kernel
theorem review_rowwidths :
    (746495 - 630783 + 1) + (1469440 - 746496 + 1) + (5140999 - 1469441 + 1) = (4510217 : ℤ) := by
  decide +kernel
theorem review_CA5 : lastNhi row2AsymPH.rows + 1 = row2AsymPH.tail.N1 := by decide +kernel
theorem review_CA1 : (500 - 2 * 93) * 5000000 ^ 2 ≤ (3962323 : ℤ) ^ 2 * 500 := by decide +kernel

#print axioms row2_laneA

#print axioms cert_of_checkAsym
#print axioms windowIdx_mono
#print axioms row2_windowIdx_ge
#print axioms row2AsymPH_check
#print axioms row2_laneA

end LaneAReview
end DBN
end Zeta23
