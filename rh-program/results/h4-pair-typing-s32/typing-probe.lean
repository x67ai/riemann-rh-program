/-
results/h4-pair-typing-s32/typing-probe.lean — the ONE scratch typing probe of the H4 typing note (BRIEF §5).
Run by `lake env lean` in the built clone ~/rh-lean-work/checker-clone-s21 (no `lake build`).  Every theorem is `sorry`:
this file confirms that the names and casts of TYPING-NOTE.md §1–§4 elaborate; it proves nothing.  Probe (i) is the one
kernel evaluation (a power sum over Finset.Icc ℤ), timed for §4.
-/
import Zeta23.PairCeiling.GridParsevalRat

open Finset
open Zeta23.PairCeiling.GridParseval Zeta23.PairCeiling.GridParsevalRat

noncomputable section

namespace PairRowProbe

-- §1: the assembly weight of paper §2.3 line 126 at the flat u_j = 1/(2n+1)
def W2 (n : ℕ) (s : ℤ) : ℝ :=
  ∑ j ∈ (Finset.Icc (-(n : ℤ)) (n : ℤ)).filter (fun j : ℤ => s - j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ)),
    (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1))

-- §1: the pair-containing form factor at the UNREDUCED integer frequency s
def pairFormFactor (n : ℕ) (m : ZMod (2 * n + 1) → ℚ)
    (pairs : Finset (ZMod (2 * n + 1) × ℝ × ℝ)) (s : ℤ) : ℂ :=
  dftMarkQ (zetaM (2 * n + 1)) m (s : ZMod (2 * n + 1))
    + ∑ p ∈ pairs,
        ((2 * p.2.1 * Real.cosh (2 * Real.pi * (s : ℝ) * p.2.2 / (2 * (n : ℝ))) : ℝ) : ℂ)
          * chi (zetaM (2 * n + 1)) ((s : ZMod (2 * n + 1)) * p.1)

-- §1: the row over the unreduced s ∈ [−2n, 2n]
def pairRow (n : ℕ) (m : ZMod (2 * n + 1) → ℚ) (pairs : Finset (ZMod (2 * n + 1) × ℝ × ℝ)) : ℝ :=
  ∑ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)), W2 n s * Complex.normSq (pairFormFactor n m pairs s)

-- §1: ā(x) = Σ_j u_j cosh(2π j x / N)
def abar (n : ℕ) (x : ℝ) : ℝ :=
  ∑ j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), (1 / (2 * (n : ℝ) + 1)) * Real.cosh (2 * Real.pi * (j : ℝ) * x / (2 * (n : ℝ)))

-- §4: the vacancy lattice, unit atoms off the hole 0
def vacancyMark (n : ℕ) : ZMod (2 * n + 1) → ℚ := fun k => if k = 0 then 0 else 1

-- (a) §1: the closed-form weight of pair-channel.md line 39
theorem W2_eq (n : ℕ) (s : ℤ) (hs : s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ))) :
    W2 n s = ((2 * (n : ℝ) + 1) - |(s : ℝ)|) / (2 * (n : ℝ) + 1) ^ 2 := by sorry

-- (b) §2: the generic regrouping (single sum over s → double sum over the band)
theorem sum_W2_mul (n : ℕ) (g : ℤ → ℝ) :
    ∑ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)), W2 n s * g s
      = ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
          (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1)) * g (j1 + j2) := by sorry

-- (b) §2: the agreement lemma
theorem pairRow_eq_gridRowQ (n : ℕ) (m : ZMod (2 * n + 1) → ℚ) :
    pairRow n m ∅ = gridRowQ n m := by sorry

-- (c) §3: (T1) at imaginary argument
theorem sum_W2_cosh (n : ℕ) (x : ℝ) :
    ∑ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)),
        W2 n s * Real.cosh (2 * Real.pi * (s : ℝ) * x / (2 * (n : ℝ))) = abar n x ^ 2 := by sorry

-- (d) Prop. 4.5 for every n, depth and real mark
theorem prop45 (n : ℕ) (d μ : ℝ) :
    pairRow n (vacancyMark n) {((0 : ZMod (2 * n + 1)), μ, d)} - (2 * (n : ℝ) + 2 * μ ^ 2)
      = 2 * μ ^ 2 * abar n (2 * d) ^ 2 - 4 * μ * (abar n d ^ 2 - 1) := by sorry

-- (e) the log-convexity chain and the integer-mark safety
theorem abar_sq_le (n : ℕ) (d : ℝ) : abar n d ^ 2 ≤ (1 + abar n (2 * d)) / 2 := by sorry
theorem floor_holds_integer (n : ℕ) (d : ℝ) (m : ℕ) (hm : 1 ≤ m) :
    0 < 2 * (m : ℝ) ^ 2 * abar n (2 * d) ^ 2 - 4 * (m : ℝ) * (abar n d ^ 2 - 1) := by sorry

-- (f) the certificate's target at the anchor: the floor F1 ≥ S2 FAILS
theorem floor_fails_anchor :
    pairRow 32 (vacancyMark 32) {((0 : ZMod 65), (1 / 20 : ℝ), (1 / 4 : ℝ))} < 64 + 2 * (1 / 20 : ℝ) ^ 2 := by sorry

-- (g) the two generic cosh bounds the certificate consumes
theorem one_add_sq_half_le_cosh (x : ℝ) : 1 + x ^ 2 / 2 ≤ Real.cosh x := by sorry
theorem cosh_le_poly8 (x : ℝ) (hx : |x| ≤ 9 / 2) :
    Real.cosh x ≤ 1 + x ^ 2 / 2 + x ^ 4 / 24 + x ^ 6 / 720 + x ^ 8 / 20160 := by sorry

-- (h) the Mathlib names consumed, by #check
#check @Real.pi_gt_d6
#check @Real.pi_lt_d6
#check @Real.exp_bound
#check @Complex.exp_bound'
#check @Real.cosh_eq
#check @Real.cosh_two_mul
#check @Real.cosh_sq
#check @Real.self_le_sinh_iff
#check @Real.abs_sinh
#check @Real.cosh_le_exp_half_sq
#check @Real.one_le_cosh
#check @Finset.sum_fiberwise_of_maps_to
#check @Finset.sum_involution
#check @Finset.sum_product
#check @Int.card_Icc

-- (i) one kernel evaluation of a power sum over Finset.Icc ℤ (route P of §4 needs four)
theorem sum_sq_Icc : (∑ j ∈ Finset.Icc (-32 : ℤ) 32, j ^ 2) = 22880 := by decide +kernel

end PairRowProbe
