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
R = [X, X+1] × [16733/100000, 1], t₀ = 93/500 (SPEC §9).

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
  `row2_barrier_mp`, `row2_barrier_arb` : for a normalized family G : ℝ → ℂ → ℂ, IF (hHol) G t is
  holomorphic on an open neighborhood of R for every t ∈ [0, t₀] and IF (hEncl) H2-B holds for the transcript
  — the producers' enclosure claims `BarrierEnclOK G row2Barrier*` — THEN G t z ≠ 0 for every t ∈ [0, t₀] and
  every z ∈ R.  This is `cert_of_checkBarrier` (BarrierCert.lean) instantiated on the kernel-checked literals;
  and `row2_barrier_mp_xy` / `row2_barrier_arb_xy` the coordinate forms (`cert_of_checkBarrier_xy`, for H = G·B)
  that hypothesis (iii′) of the amended bridge consumes.  For the instance G t z = Ht t z / Bt t z; `Bt`,
  `Polymath15Bridge'` and `HtEntire` are the Defs.lean v1.1 items (SPEC §3.3–3.5) — NOT yet in the trusted
  layer, so the statements below are generic in G / H, B.

WHAT IS NOT PROVED HERE (the cut line, stated honestly):
  * the theorem `lambda_le_point2` (SPEC §8.3, "Λ ≤ 0.2 in ray form") — it needs Defs.lean v1.1
    (`Polymath15Bridge'`, `Bt`, `HtEntire`), the asymptotic lane (`checkAsym`, `cert_of_checkAsym`, a Lane-A
    transcript — none produced yet) and L-B3 (`Bt` holomorphic and nonvanishing near R).  None of these exists
    in the working tree at 2026-09-03; item (e) is therefore PARTIAL: Lane B complete on both legs, Lane A and
    the glue absent.
  * anything analytic: H2-B (the rows enclose SOME holomorphic f approximating G τ to E/K, and G moves by ≤ D/K
    in the prism) and hHol stay displayed; the two producers' cross-check (results/d1-m2a/INSTANCE-REPORT.md)
    is producer-side evidence for H2-B, not a proof.
Trust vocabulary (D-R3/D-R8, binding): "kernel-checked modulo the displayed hypotheses H2-B and hHol
(producers untrusted)".  The Λ bracket of record stays 0 ≤ Λ ≤ 0.2 (Rodgers–Tao; Platt–Trudgian Cor. 2).
-/
import Zeta23.DBN.Instance02.mp_Barrier
import Zeta23.DBN.Instance02.arb_Barrier

open Complex (I)

namespace Zeta23
namespace DBN
namespace Instance02

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

end Instance02
end DBN
end Zeta23
