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
`lambda_le_point2` (SPEC §8.3; RUN-REPORT §6 item 4); since 2026-09-09 (Session 19) the glue consumes the
kernel-checked LANE A literals (RUN-REPORT §6 item 3; results/d1-m2a/lane-a/).

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

LANE A (the asymptotic region at the final time t₀; since 2026-09-09, Session 19; results/d1-m2a/lane-a/), likewise
TWO INDEPENDENT PRODUCER TRANSCRIPTS, BOTH KERNEL-CHECKED:
  * `row2AsymMP`  — the mpmath-ball leg (lane-a/asym-mp.json: 3 window rows covering N ∈ [630783, 5140999]
    consecutively, the tail row at N₁ = 5 141 000, K = 10²⁴), module Instance02/Asym_mp with the kernel fact
    `row2AsymMP_check : checkAsym row2AsymMP = true` (C-A1 … C-A6, `decide +kernel`) and the glue lemma `row2_laneA_mp`;
  * `row2AsymARB` — the Arb/FLINT leg (lane-a/asym-arb.json: the same rows and tail, K = 10¹²), module
    Instance02/Asym_arb with `row2AsymARB_check` and `row2_laneA_arb`.
Emitted by the UNTRUSTED lane-a/emit_lean_lane_a.py and back-parse-verified against the JSON, integer by integer, by
lane-a/backparse_lane_a.py (0 mismatches, both legs); the two transcripts cross-checked per row (lane-a/crosscheck-full.txt:
T and Q₁ … Q₄ agree to ≤ 5·10⁻⁷⁹, the E hull bounds recorded, Arb's larger).  Each leg pairs its own Lane A literal with
its own Lane B literal — the legs are never merged (D-R3).

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
        hAsym  : AsymEnclOK (fun z => Ht t₀ z / Bt t₀ z) row2Asym*                (H2-A, one leg: the window-row floors)
        hTail  : TailOK (fun z => Ht t₀ z / Bt t₀ z) row2Asym*                    (H-TAIL, one leg: N(x) ≥ N₁)
        hH3    : Polymath15Bridge' ∧ HtEntire                                      (H3; Defs.lean v1.1)
      via `row2_ray_mp` / `row2_ray_arb` (the same, with the row's own conclusion t ≥ t₀ + y₀²/2), where
      hypothesis (ii′) of `Polymath15Bridge'` is `row2_laneA_* hAsym hTail` (Instance02/Asym_*.lean:
      `cert_of_checkAsym` on the kernel-checked literal, L-A1 `row2_windowIdx_ge`, L-A2; Asym.lean).  The
      `hHol` of the `_xy` legs is DISCHARGED (`hHol_of_entire`) from `hH3.2` and L-B3 (BtFacts.lean: `Bt`
      holomorphic and nonvanishing on the open right half-plane, which contains R).  The two legs are kept
      as two theorems — the legs are never merged (D-R3).
      `#print axioms`: propext, Classical.choice, Quot.sound (recorded in results/d1-m2a/v11/GLUE-NOTES.md).

WHAT IS DISPLAYED (since 2026-09-09: exactly the SPEC §3.7 label, as written):
  * H1 (`hH1`), H2-B (`hEncl`), H2-A (`hAsym`, the window-row floors), H-TAIL (`hTail`), H3 (`hH3`) — SPEC §3.7's
    named hypotheses and nothing else; `#print axioms` = propext, Classical.choice, Quot.sound (lane-a/final-axioms.log).
  * What the 2026-09-09 replacement of `hLaneA` bought (PLAN-REVIEW.md §6, stated not glossed): the window range
    N ∈ [630783, 5140999] (x from ≈ 5.0·10¹² up to x_{N₁} ≈ 3.32·10¹⁴) is no longer a displayed nonvanishing claim but
    a displayed FLOOR ENCLOSURE (‖g‖ ≥ (T − E)/K per window row) plus the kernel-checked coverage argument (C-A3, C-A4,
    C-A5 + L-A1 + L-A2 inside `cert_of_checkAsym`); the displayed nonvanishing CONCLUSION that remains is `TailOK`
    only — N(x) ≥ 5 141 000, i.e. x ≳ 3.32·10¹⁴, on the y-band [y₀, yA].  Asymmetry recorded: yA = 3962323/5000000 =
    0.7924646 is 1.5·10⁻⁷ WIDER than the former `hLaneA`'s y ≤ √(157/250) = 0.79246451…, so `TailOK` is "the tail region
    N ≥ N₁, y ∈ [y₀, yA]", not literally a sub-statement of `hLaneA` (the glue derives y ≤ yA from y² ≤ 157/250).
    C-A6 (the tail row's Q₁ + Q₂ + Q₃ + Q₄ + E₁ < 2K) is kernel-checked on each literal but NOT consumed by any proof:
    recorded evidence for Lemma T's prose discharge (SPEC §5.1, §5.4) — the tail REDUCTION is not kernel-checked.
  * The two producers' cross-checks (results/d1-m2a/INSTANCE-REPORT.md for Lane B; lane-a/crosscheck-full.txt for
    Lane A) are producer-side evidence for H2-B / H2-A, not proofs.
  * DATED RECORD, 2026-09-06 (Session 16) to 2026-09-09 (superseded, kept): in that interval H2-A entered as `hLaneA`
    IN CONCLUSION FORM — the final-time asymptotic nonvanishing (ii′) itself, on x ≥ X + 1, y ≥ y₀, y² ≤ 1 − 2t₀ —
    because the Lane A producers (SPEC P-9/P-10) and the `checkAsym` checker were a SEPARATE COMPUTE STREAM not yet
    run; that binder was a displayed hypothesis STRONGER than SPEC §3.7's H2-A (the lane's conclusion, with nothing
    kernel-checked behind it), and the label then read "H1, H2-B, H2-A (in conclusion form, pending the Lane A
    checker), H3".  On 2026-09-09 (Session 19; results/d1-m2a/lane-a/EMIT-NOTES.md, instance02-replacement.diff) the
    binder became the pair `hAsym`, `hTail` in the four theorems and the token `hLaneA` at the one consumption point
    per leg became `(row2_laneA_* hAsym hTail)`; nothing else in the proofs moved (PLAN.md §1.5).
Trust vocabulary (D-R3/D-R8, binding): "kernel-checked modulo the displayed hypotheses H1, H2 (H2-B, H2-A, H-TAIL)
and H3 (producers untrusted)" — SPEC §3.7's label; never "fully machine-checked".  The Λ bracket of record stays
0 ≤ Λ ≤ 0.2 (Rodgers–Tao; Platt–Trudgian Cor. 2).
-/
import Zeta23.DBN.Instance02.mp_Barrier
import Zeta23.DBN.Instance02.arb_Barrier
import Zeta23.DBN.BtFacts
import Zeta23.DBN.Instance02.Asym_mp
import Zeta23.DBN.Instance02.Asym_arb

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
t₀ + y₀²/2.  Kernel-checked modulo the displayed hypotheses `hH1` (H1), `hEncl` (H2-B), `hAsym` (H2-A: the
window-row floors of the kernel-checked Lane A literal `row2AsymMP`, N ∈ [630783, 5140999]), `hTail` (H-TAIL:
nonvanishing for N(x) ≥ N₁ = 5 141 000 on the y-band [y₀, yA]) and `hH3` (H3).  Hypothesis (ii′) of the bridge is
`row2_laneA_mp hAsym hTail` (Instance02/Asym_mp.lean: `cert_of_checkAsym` on `row2AsymMP_check` + L-A1/L-A2), which
since 2026-09-09 (Session 19) replaces the former conclusion-form binder `hLaneA` — see the file header. -/
theorem row2_ray_mp
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierMP)
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymMP)
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymMP)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, 93 / 500 + (16733 / 100000) ^ 2 / 2 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  have hiii := row2_barrier_mp_xy Ht Bt (hHol_of_entire row2BarrierMP rfl hH3.2) hEncl
  refine hH3.1 (93 / 500) 5000000194858 (16733 / 100000) (by norm_num) (by norm_num) (by norm_num)
    (by norm_num) (hH1_row2 hH1) (row2_laneA_mp hAsym hTail) ?_
  intro x y hx1 hx2 hy1 hy2 t ht0 ht1
  exact hiii x y
    (by change row2Rect.x1 ≤ x; rw [row2Rect_x1]; exact hx1)
    (by change x ≤ row2Rect.x2; rw [row2Rect_x2]; exact hx2)
    (by change row2Rect.y1 ≤ y; rw [row2Rect_y1]; exact hy1)
    (by change y ≤ row2Rect.y2; rw [row2Rect_y2]; exact hy2)
    t ht0 (by rw [row2BarrierMP_t0]; exact ht1)

/-- **The bridge applied at row 2, Arb/FLINT leg** — the same from the independent transcripts (Lane B
`row2BarrierARB`, Lane A `row2AsymARB` via `row2_laneA_arb`; the legs are never merged, D-R3). -/
theorem row2_ray_arb
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierARB)
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymARB)
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymARB)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, 93 / 500 + (16733 / 100000) ^ 2 / 2 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  have hiii := row2_barrier_arb_xy Ht Bt (hHol_of_entire row2BarrierARB rfl hH3.2) hEncl
  refine hH3.1 (93 / 500) 5000000194858 (16733 / 100000) (by norm_num) (by norm_num) (by norm_num)
    (by norm_num) (hH1_row2 hH1) (row2_laneA_arb hAsym hTail) ?_
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
(H2-A) `hAsym`, the producer-certified final-time window-row floors `AsymEnclOK (Ht t₀ / Bt t₀) row2AsymMP` for the
kernel-checked mpmath-ball Lane A transcript (N ∈ [630783, 5140999]; the step from the floors to nonvanishing on
that range is the kernel-checked coverage argument inside `cert_of_checkAsym`); (H-TAIL) `hTail`, the tail
`TailOK (Ht t₀ / Bt t₀) row2AsymMP` — nonvanishing for N(x) ≥ N₁ = 5 141 000 on y ∈ [y₀, yA], the one displayed
nonvanishing CONCLUSION that remains (Lemma T's reduction is prose; C-A6 is kernel-checked evidence for it, never
consumed by a proof); (H3) `hH3`, the Polymath15 analytic package `Polymath15Bridge' ∧ HtEntire`.
L-B3 and `hHol` are proved, not displayed.  Label (SPEC §3.7): "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL),
H3" — never "fully machine-checked".  The word Λ appears in prose only (design note §1.2). -/
theorem lambda_le_point2
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierMP)
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymMP)
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymMP)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  intro t ht
  exact row2_ray_mp hH1 hEncl hAsym hTail hH3 t (le_trans row2_bound_le_point2 ht)

/-- **Λ ≤ 0.2 in ray form, Arb/FLINT leg.**  The same statement from the independent transcripts
(same displayed hypotheses, with H2-B for `row2BarrierARB` and H2-A, H-TAIL for `row2AsymARB`; the legs are never
merged). -/
theorem lambda_le_point2_arb
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierARB)
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymARB)
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymARB)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  intro t ht
  exact row2_ray_arb hH1 hEncl hAsym hTail hH3 t (le_trans row2_bound_le_point2 ht)

end Instance02
end DBN
end Zeta23
