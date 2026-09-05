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
Zeta23/DBN/Instance02.lean — M2a item (e), the INSTANCE of the barrier certificate (Lane B of
rh-program/results/d1-m2a/SPEC.md v1.0) for Polymath15 Table 1 row 2: X = 5 000 000 194 858,
R = [X, X+1] × [16733/100000, 1], t₀ = 93/500 (SPEC §9) — and, since 2026-09-06 (Session 16), the GLUE
`lambda_le_point2` (SPEC §8.3; RUN-REPORT §6 item 4).

TWO INDEPENDENT PRODUCER TRANSCRIPTS, BOTH KERNEL-CHECKED (SPEC P-1, D-R3):
  * `row2BarrierMP`  — the mpmath-ball leg (results/d1-m2a/transcripts/row2, 39 prisms, 7 176 rows,
    K = 10²⁴, A = 10¹²), modules Instance02/mp_0000 … mp_0038, assembled in Instance02/mp_Barrier;
  * `row2BarrierARB` — the Arb/FLINT leg (results/d1-m2a/transcripts/row2-arb, 72 prisms, 10 771 rows,
    K = 10¹², A = 10⁶), modules Instance02/arb_0000 … arb_0071, assembled in Instance02/arb_Barrier.
Each per-prism module proves `checkPrism row2Rect <prism> = true` by `decide +kernel` (SPEC §7.6 packaging:
one module per prism, row chunks of ≤ 1 000, `set_option maxRecDepth 100000`); each `_Barrier` module proves
the chain fact `checkBarrierChain … = true` by `decide +kernel`, the split fact `∀ p ∈ prisms, checkPrism …`
by citing the per-prism theorems, and the monolithic `checkBarrier … = true`.  No `native_decide` anywhere.
The literals were emitted by the UNTRUSTED results/d1-m2a/emit_lean_m2a.py and back-parse-verified against
the JSON, field by field and row by row, by verify_lean_m2a.py (0 mismatches, both legs).

WHAT IS PROVED HERE (kernel-checked modulo the displayed hypotheses — never "fully machine-checked"):
  §1  `row2_barrier_mp`, `row2_barrier_arb` : for a normalized family G : ℝ → ℂ → ℂ, IF (hHol) G t is
      holomorphic on an open neighborhood of R for every t ∈ [0, t₀] and IF (hEncl) H2-B holds for the
      transcript — the producers' enclosure claims `BarrierEnclOK G row2Barrier*` — THEN G t z ≠ 0 for every
      t ∈ [0, t₀] and every z ∈ R.  This is `cert_of_checkBarrier` (BarrierCert.lean) instantiated on the
      kernel-checked literals; and `row2_barrier_mp_xy` / `row2_barrier_arb_xy` the coordinate forms
      (`cert_of_checkBarrier_xy`, for H = G·B) that hypothesis (iii′) of `Polymath15Bridge'` consumes.
  §2  `lambda_le_point2` (mpmath-ball leg) and `lambda_le_point2_arb` (Arb/FLINT leg): the target theorem of
      SPEC §1.1 in ray form, ∀ t ≥ 1/5, every zero of H_t is real — from the DISPLAYED hypotheses
        hH1    : ZeroVerification (116733 / 200000) 2500000097429                 (H1, exact; SPEC §3.6)
        hEncl  : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2Barrier*          (H2-B, one leg)
        hLaneA : ∀ x y, X + 1 ≤ x → y₀ ≤ y → y² ≤ 1 − 2t₀ → Ht t₀ (x + y·I) ≠ 0   (H2-A, see below)
        hH3    : Polymath15Bridge' ∧ HtEntire                                      (H3; Defs.lean v1.1)
      via `row2_ray_mp` / `row2_ray_arb` (the same, with the row's own conclusion t ≥ t₀ + y₀²/2).  The
      `hHol` of the `_xy` legs is DISCHARGED (`hHol_of_entire`) from `hH3.2` and L-B3 (BtFacts.lean: `Bt`
      holomorphic and nonvanishing on the open right half-plane, which contains R).  The two legs are kept
      as two theorems — the legs are never merged (D-R3).
      `#print axioms`: propext, Classical.choice, Quot.sound (recorded in results/d1-m2a/v11/GLUE-NOTES.md).

WHAT IS DISPLAYED, AND HOW THIS DIFFERS FROM THE SPEC §3.7 LABEL (stated honestly):
  * H2-A enters as `hLaneA` IN CONCLUSION FORM — the final-time asymptotic nonvanishing (ii′) itself, on
    x ≥ X + 1, y ≥ y₀, y² ≤ 1 − 2t₀.  SPEC §3.7 foresees H2-A as producer-certified window rows plus the tail
    H-TAIL, with a kernel-checked `checkAsym`/`cert_of_checkAsym` between them and (ii′); the Lane A producers
    (SPEC P-9/P-10) and that checker are a SEPARATE COMPUTE STREAM not run at 2026-09-06.  Until it lands,
    `hLaneA` is a displayed hypothesis STRONGER than the SPEC's H2-A (it is the lane's conclusion, with nothing
    kernel-checked behind it); when Lane A lands, `hLaneA` is replaced by `cert_of_checkAsym` on the Lane A
    literal with H2-A's rows and H-TAIL displayed, and the theorem statement changes accordingly.
  * H2-B, H1, H3 are displayed exactly as SPEC §3.7 says.
  * The two producers' cross-check (results/d1-m2a/INSTANCE-REPORT.md) is producer-side evidence for H2-B,
    not a proof.
Trust vocabulary (D-R3/D-R8, binding): "kernel-checked modulo the displayed hypotheses H1, H2-B, H2-A (in
conclusion form, pending the Lane A checker) and H3 (producers untrusted)".  The Λ bracket of record stays
0 ≤ Λ ≤ 0.2 (Rodgers–Tao; Platt–Trudgian Cor. 2).
-/
import Zeta23.DBN.Instance02.mp_Barrier
import Zeta23.DBN.Instance02.arb_Barrier
import Zeta23.DBN.BtFacts

open Complex (I)

namespace Zeta23
namespace DBN
namespace Instance02

/-! ## 1. Lane B: the two legs (Session 14, unchanged) -/

/-- the rectangle and final time, as reals: R = [X, X+1] × [y₀, 1], t₀ = 93/500 (sanity, `rfl`/`norm_num`). -/
example : row2BarrierMP.rect = row2Rect := rfl
example : row2BarrierARB.rect = row2Rect := rfl
example : t0 row2BarrierMP = (93 : ℝ) / 500 := by simp [t0, row2BarrierMP]
example : t0 row2BarrierARB = (93 : ℝ) / 500 := by simp [t0, row2BarrierARB]

/-- **Lane B, mpmath-ball leg.**  Kernel-checked modulo H2-B (`hEncl`) and `hHol`: G t ≠ 0 on the closed
rectangle R for every t ∈ [0, t₀]. -/
theorem row2_barrier_mp (G : ℝ → ℂ → ℂ)
    (hHol : ∀ t : ℝ, 0 ≤ t → t ≤ t0 row2BarrierMP →
      ∃ U : Set ℂ, IsOpen U ∧ BarrierRect row2BarrierMP ⊆ U ∧ DifferentiableOn ℂ (G t) U)
    (hEncl : BarrierEnclOK G row2BarrierMP) :
    ∀ t : ℝ, 0 ≤ t → t ≤ t0 row2BarrierMP → ∀ z ∈ BarrierRect row2BarrierMP, G t z ≠ 0 :=
  cert_of_checkBarrier G row2BarrierMP row2BarrierMP_chain row2BarrierMP_prisms hHol hEncl

/-- **Lane B, Arb/FLINT leg.**  Same statement from the independent transcript. -/
theorem row2_barrier_arb (G : ℝ → ℂ → ℂ)
    (hHol : ∀ t : ℝ, 0 ≤ t → t ≤ t0 row2BarrierARB →
      ∃ U : Set ℂ, IsOpen U ∧ BarrierRect row2BarrierARB ⊆ U ∧ DifferentiableOn ℂ (G t) U)
    (hEncl : BarrierEnclOK G row2BarrierARB) :
    ∀ t : ℝ, 0 ≤ t → t ≤ t0 row2BarrierARB → ∀ z ∈ BarrierRect row2BarrierARB, G t z ≠ 0 :=
  cert_of_checkBarrier G row2BarrierARB row2BarrierARB_chain row2BarrierARB_prisms hHol hEncl

/-- the coordinate form consumed by hypothesis (iii′) of the amended bridge (SPEC §3.3), for H = G·B
(instance: H = Ht, B = Bt): H t (x + iy) ≠ 0 on the box for t ∈ [0, t₀] — mpmath-ball leg. -/
theorem row2_barrier_mp_xy (H B : ℝ → ℂ → ℂ)
    (hHol : ∀ t : ℝ, 0 ≤ t → t ≤ t0 row2BarrierMP →
      ∃ U : Set ℂ, IsOpen U ∧ BarrierRect row2BarrierMP ⊆ U
        ∧ DifferentiableOn ℂ (fun z => H t z / B t z) U)
    (hEncl : BarrierEnclOK (fun t z => H t z / B t z) row2BarrierMP) :
    ∀ x y : ℝ, row2BarrierMP.rect.x1 ≤ x → x ≤ row2BarrierMP.rect.x2 →
      row2BarrierMP.rect.y1 ≤ y → y ≤ row2BarrierMP.rect.y2 →
      ∀ t : ℝ, 0 ≤ t → t ≤ t0 row2BarrierMP → H t (x + y * I) ≠ 0 :=
  cert_of_checkBarrier_xy H B row2BarrierMP row2BarrierMP_chain row2BarrierMP_prisms hHol hEncl

/-- the same, Arb/FLINT leg. -/
theorem row2_barrier_arb_xy (H B : ℝ → ℂ → ℂ)
    (hHol : ∀ t : ℝ, 0 ≤ t → t ≤ t0 row2BarrierARB →
      ∃ U : Set ℂ, IsOpen U ∧ BarrierRect row2BarrierARB ⊆ U
        ∧ DifferentiableOn ℂ (fun z => H t z / B t z) U)
    (hEncl : BarrierEnclOK (fun t z => H t z / B t z) row2BarrierARB) :
    ∀ x y : ℝ, row2BarrierARB.rect.x1 ≤ x → x ≤ row2BarrierARB.rect.x2 →
      row2BarrierARB.rect.y1 ≤ y → y ≤ row2BarrierARB.rect.y2 →
      ∀ t : ℝ, 0 ≤ t → t ≤ t0 row2BarrierARB → H t (x + y * I) ≠ 0 :=
  cert_of_checkBarrier_xy H B row2BarrierARB row2BarrierARB_chain row2BarrierARB_prisms hHol hEncl

/-! ## 2. The glue: `lambda_le_point2` (SPEC §8.3; Session 16) -/

/-- the rectangle's reals are the instance parameters, exactly (SPEC §9). -/
theorem row2Rect_x1 : row2Rect.x1 = 5000000194858 := by norm_num [RectData.x1, row2Rect]
theorem row2Rect_x2 : row2Rect.x2 = 5000000194858 + 1 := by norm_num [RectData.x2, row2Rect]
theorem row2Rect_y1 : row2Rect.y1 = 16733 / 100000 := by norm_num [RectData.y1, row2Rect]
theorem row2Rect_y2 : row2Rect.y2 = 1 := by norm_num [RectData.y2, row2Rect]
theorem row2BarrierMP_t0 : t0 row2BarrierMP = 93 / 500 := by norm_num [t0, row2BarrierMP]
theorem row2BarrierARB_t0 : t0 row2BarrierARB = 93 / 500 := by norm_num [t0, row2BarrierARB]

/-- `hHol` for either leg, DISCHARGED from H3's `HtEntire` and L-B3 (BtFacts.lean): the open right
half-plane is an open neighborhood of R = [X, X+1] × [y₀, 1] (X > 0) on which Ht t / Bt t is
differentiable. -/
theorem hHol_of_entire (d : BarrierData) (hd : d.rect = row2Rect) (hEnt : HtEntire) :
    ∀ t : ℝ, 0 ≤ t → t ≤ t0 d →
      ∃ U : Set ℂ, IsOpen U ∧ BarrierRect d ⊆ U ∧ DifferentiableOn ℂ (fun z => Ht t z / Bt t z) U := by
  intro t _ _
  refine ⟨{z : ℂ | 0 < z.re}, isOpen_rightHalfPlane, ?_, differentiableOn_Ht_div_Bt hEnt t⟩
  intro z hz
  have h1 : d.rect.x1 ≤ z.re := hz.1
  rw [hd, row2Rect_x1] at h1
  show 0 < z.re
  linarith

/-- H1 in the parameter form `Polymath15Bridge'` consumes at row 2, from the exact instance form
(SPEC §3.6: (1 + 16733/100000)/2 = 116733/200000 and 5000000194858/2 = 2500000097429, exactly). -/
theorem hH1_row2 (hH1 : ZeroVerification (116733 / 200000) 2500000097429) :
    ZeroVerification ((1 + 16733 / 100000) / 2) (5000000194858 / 2) := by
  have e1 : ((1 : ℝ) + 16733 / 100000) / 2 = 116733 / 200000 := by norm_num
  have e2 : (5000000194858 : ℝ) / 2 = 2500000097429 := by norm_num
  rw [e1, e2]; exact hH1

/-- L-G: the row's bound t₀ + y₀²/2 = 3999993289/20000000000 is at most 1/5 (exact rationals). -/
theorem row2_bound_le_point2 : (93 / 500 : ℝ) + (16733 / 100000) ^ 2 / 2 ≤ 1 / 5 := by norm_num

/-- **The bridge applied at row 2, mpmath-ball leg** — the conclusion at the row's own bound
t₀ + y₀²/2.  Kernel-checked modulo the displayed hypotheses `hH1` (H1), `hEncl` (H2-B), `hLaneA`
(H2-A in conclusion form — the Lane A producers and `checkAsym` are a separate compute stream not yet run;
see the file header) and `hH3` (H3). -/
theorem row2_ray_mp
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierMP)
    (hLaneA : ∀ x y : ℝ, 5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y →
      y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (x + y * I) ≠ 0)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, 93 / 500 + (16733 / 100000) ^ 2 / 2 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  have hiii := row2_barrier_mp_xy Ht Bt (hHol_of_entire row2BarrierMP rfl hH3.2) hEncl
  refine hH3.1 (93 / 500) 5000000194858 (16733 / 100000) (by norm_num) (by norm_num) (by norm_num)
    (by norm_num) (hH1_row2 hH1) hLaneA ?_
  intro x y hx1 hx2 hy1 hy2 t ht0 ht1
  exact hiii x y
    (by change row2Rect.x1 ≤ x; rw [row2Rect_x1]; exact hx1)
    (by change x ≤ row2Rect.x2; rw [row2Rect_x2]; exact hx2)
    (by change row2Rect.y1 ≤ y; rw [row2Rect_y1]; exact hy1)
    (by change y ≤ row2Rect.y2; rw [row2Rect_y2]; exact hy2)
    t ht0 (by rw [row2BarrierMP_t0]; exact ht1)

/-- **The bridge applied at row 2, Arb/FLINT leg** — the same from the independent transcript. -/
theorem row2_ray_arb
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierARB)
    (hLaneA : ∀ x y : ℝ, 5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y →
      y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (x + y * I) ≠ 0)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, 93 / 500 + (16733 / 100000) ^ 2 / 2 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  have hiii := row2_barrier_arb_xy Ht Bt (hHol_of_entire row2BarrierARB rfl hH3.2) hEncl
  refine hH3.1 (93 / 500) 5000000194858 (16733 / 100000) (by norm_num) (by norm_num) (by norm_num)
    (by norm_num) (hH1_row2 hH1) hLaneA ?_
  intro x y hx1 hx2 hy1 hy2 t ht0 ht1
  exact hiii x y
    (by change row2Rect.x1 ≤ x; rw [row2Rect_x1]; exact hx1)
    (by change x ≤ row2Rect.x2; rw [row2Rect_x2]; exact hx2)
    (by change row2Rect.y1 ≤ y; rw [row2Rect_y1]; exact hy1)
    (by change y ≤ row2Rect.y2; rw [row2Rect_y2]; exact hy2)
    t ht0 (by rw [row2BarrierARB_t0]; exact ht1)

/-- **Λ ≤ 0.2 in ray form (SPEC §1.1), mpmath-ball leg.**  Every H_t with t ≥ 1/5 has only real zeros —
kernel-checked modulo the displayed hypotheses: (H1) `hH1`, the producer-certified zero verification
`ZeroVerification (116733/200000) 2500000097429` (discharged in prose by Platt–Trudgian Theorem 1);
(H2-B) `hEncl`, the producer-certified barrier enclosures for the kernel-checked mpmath-ball transcript;
(H2-A) `hLaneA`, the final-time asymptotic nonvanishing (ii′) IN CONCLUSION FORM — the Lane A producers and
the `checkAsym` checker are a separate compute stream not yet run, so this is displayed as the lane's
conclusion, not as checked rows; (H3) `hH3`, the Polymath15 analytic package `Polymath15Bridge' ∧ HtEntire`.
L-B3 and `hHol` are proved, not displayed.  The word Λ appears in prose only (design note §1.2). -/
theorem lambda_le_point2
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierMP)
    (hLaneA : ∀ x y : ℝ, 5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y →
      y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (x + y * I) ≠ 0)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  intro t ht
  exact row2_ray_mp hH1 hEncl hLaneA hH3 t (le_trans row2_bound_le_point2 ht)

/-- **Λ ≤ 0.2 in ray form, Arb/FLINT leg.**  The same statement from the independent transcript
(same displayed hypotheses, with H2-B for `row2BarrierARB`). -/
theorem lambda_le_point2_arb
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierARB)
    (hLaneA : ∀ x y : ℝ, 5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y →
      y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (x + y * I) ≠ 0)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  intro t ht
  exact row2_ray_arb hH1 hEncl hLaneA hH3 t (le_trans row2_bound_le_point2 ht)

end Instance02
end DBN
end Zeta23
