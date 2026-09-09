/-
asym-check-scratch.lean — BUILD VERIFICATION of Zeta23/DBN/Asym.lean (Session 19 builder, 2026-09-09).
NOT a program file; checked with `lake env lean` from ~/rh-lean-work/zeta-23-lean-main against the BUILT module.
Purpose: on the module's own names (namespace Zeta23.DBN, not the planner's LaneAScratch), (1) `decide +kernel` on a
3-row literal of the exact shape the emitter will produce (PLACEHOLDER integers from the float plan — NOT a certificate),
(2) the two negative controls (a row gap → C-A4 false; a tail sum ≥ 2K → C-A6 false), (3) the glue lemma `row2_laneA`
(PLAN §1.5) and (4) the reviewer's three composition tests feeding it into the real `lambda_le_point2`,
`lambda_le_point2_arb`, `row2_ray_mp` of the built Instance02.lean (PLAN-REVIEW §1 A18).
-/
import Zeta23.DBN.Asym
import Zeta23.DBN.Instance02

open scoped Real
open Complex (I)

noncomputable section

namespace Zeta23
namespace DBN
namespace AsymCheck

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

#print axioms row2AsymPH_check
#print axioms row2AsymPH_gap
#print axioms row2AsymPH_tail
#print axioms row2_laneA

end AsymCheck
end DBN
end Zeta23

end
