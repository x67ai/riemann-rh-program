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
Zeta23/W1/Ledger.lean — the M3 EXCLUSION LEDGER's Lean leaf (seed, 2026-09-10, Session 20):
one corollary of `cert_of_checkW1_ap` (m = 0 branch) per ledger leg, on the kernel-checked
literals of Instances.lean, consumed unchanged.  Record and format:
rh-program/results/d1-m3/{README.md, LEDGER.md, index.json, rows/<row-id>/ROW.json} and
rh-program/results/d1-m2a/dr8/PRICING-M3-ledger.md §1.2–1.6; build record dr8/BUILD-NOTES-fDH.md.

A ledger ROW is one closed box R = [σ₁, σ₂] × [T₁, T₂] with ½ < σ₁ ≤ σ₂ < 1 carried by TWO W1
exclusion transcripts (m = 0, one per producer leg), both Python-checker-ACCEPTED, both
kernel-checked (`<name>_check`, Instances.lean), cell-wise cross-checked CONSISTENT, each pinned by
its SHA-256.  Each leg's theorem here is the m = 0 branch of `cert_of_checkW1_ap` on that leg's
literal: `W1EnclOK riemannZeta d → ∀ s ∈ W1Rect d, riemannZeta s ≠ 0`.  The two legs are two
theorems with two hypotheses, never merged (D-R3).

THE FOUR SEED ROWS (the M1 v1 acceptance null tests; provenance `acceptance`, chosen for the cost
curve, not by any prior — results/d1-m1/acceptance-report.md §1):
  R1  zeta_3-5_9-10_100_101       [3/5, 9/10] × [100, 101]        δ₀ = 1/10   mpNullT100 / arbNullT100
  R2  zeta_3-5_9-10_1000_1001     [3/5, 9/10] × [1000, 1001]      δ₀ = 1/10   mpNullT1000 / arbNullT1000
  R3  zeta_3-5_9-10_10000_10001   [3/5, 9/10] × [10000, 10001]    δ₀ = 1/10   mpNullT10000 / arbNullT10000
  R4  zeta_21-40_39-40_100_101    [21/40, 39/40] × [100, 101]     δ₀ = 1/40   mpNullDeepT100 / arbNullDeepT100

HONEST LABEL, per row (binding; D-R6, lean/README.md "Honest label, binding"): "no zero of ζ in the
closed box, kernel-checked modulo H-ENCL (producers untrusted)" — equivalently, for the row's δ₀,
"no zeros of ζ with Re s ≥ ½ + δ₀ in [σ₁, σ₂] × [T₁, T₂]".  Never "RH verified in [T₁, T₂]": a box
has σ₁ > ½ strictly (clause C2), so no row and no tiling of rows reaches the line; a range statement
needs a Turing-method zero count the format does not carry.  Nothing about ζ outside the box;
nothing about Λ (a row is m = 0); isolated boxes extend no contiguous record (the rigorous
verification record stays 3·10¹², Platt–Trudgian); all four seed boxes lie far below it, so as facts
about ζ they are known — their value is that they are the program's OWN certificates in its own
trust vocabulary and the ledger's format-validation rows.

`#print axioms` on each: [propext, Classical.choice, Quot.sound] (dr8/fdh-axioms.log).
-/
import Zeta23.W1.ArgPrincipleBridge
import Zeta23.W1.Instances

noncomputable section

namespace Zeta23
namespace W1

/-- Ledger row zeta_3-5_9-10_100_101 (R1), mp leg: no zeros of ζ in the closed box, modulo H-ENCL. -/
theorem mpNullT100_exclusion (hEncl : W1EnclOK riemannZeta mpNullT100) :
    ∀ s ∈ W1Rect mpNullT100, riemannZeta s ≠ 0 :=
  (cert_of_checkW1_ap mpNullT100 (checkW1Floor_spec mpNullT100_check).1 hEncl).2 (by decide)

/-- Ledger row zeta_3-5_9-10_100_101 (R1), Arb leg: no zeros of ζ in the closed box, modulo H-ENCL. -/
theorem arbNullT100_exclusion (hEncl : W1EnclOK riemannZeta arbNullT100) :
    ∀ s ∈ W1Rect arbNullT100, riemannZeta s ≠ 0 :=
  (cert_of_checkW1_ap arbNullT100 (checkW1Floor_spec arbNullT100_check).1 hEncl).2 (by decide)

/-- Ledger row zeta_3-5_9-10_1000_1001 (R2), mp leg: no zeros of ζ in the closed box, modulo H-ENCL. -/
theorem mpNullT1000_exclusion (hEncl : W1EnclOK riemannZeta mpNullT1000) :
    ∀ s ∈ W1Rect mpNullT1000, riemannZeta s ≠ 0 :=
  (cert_of_checkW1_ap mpNullT1000 (checkW1Floor_spec mpNullT1000_check).1 hEncl).2 (by decide)

/-- Ledger row zeta_3-5_9-10_1000_1001 (R2), Arb leg: no zeros of ζ in the closed box, modulo H-ENCL. -/
theorem arbNullT1000_exclusion (hEncl : W1EnclOK riemannZeta arbNullT1000) :
    ∀ s ∈ W1Rect arbNullT1000, riemannZeta s ≠ 0 :=
  (cert_of_checkW1_ap arbNullT1000 (checkW1Floor_spec arbNullT1000_check).1 hEncl).2 (by decide)

/-- Ledger row zeta_3-5_9-10_10000_10001 (R3), mp leg: no zeros of ζ in the closed box, modulo H-ENCL. -/
theorem mpNullT10000_exclusion (hEncl : W1EnclOK riemannZeta mpNullT10000) :
    ∀ s ∈ W1Rect mpNullT10000, riemannZeta s ≠ 0 :=
  (cert_of_checkW1_ap mpNullT10000 (checkW1Floor_spec mpNullT10000_check).1 hEncl).2 (by decide)

/-- Ledger row zeta_3-5_9-10_10000_10001 (R3), Arb leg: no zeros of ζ in the closed box, modulo H-ENCL. -/
theorem arbNullT10000_exclusion (hEncl : W1EnclOK riemannZeta arbNullT10000) :
    ∀ s ∈ W1Rect arbNullT10000, riemannZeta s ≠ 0 :=
  (cert_of_checkW1_ap arbNullT10000 (checkW1Floor_spec arbNullT10000_check).1 hEncl).2 (by decide)

/-- Ledger row zeta_21-40_39-40_100_101 (R4), mp leg: no zeros of ζ in the closed box, modulo H-ENCL. -/
theorem mpNullDeepT100_exclusion (hEncl : W1EnclOK riemannZeta mpNullDeepT100) :
    ∀ s ∈ W1Rect mpNullDeepT100, riemannZeta s ≠ 0 :=
  (cert_of_checkW1_ap mpNullDeepT100 (checkW1Floor_spec mpNullDeepT100_check).1 hEncl).2 (by decide)

/-- Ledger row zeta_21-40_39-40_100_101 (R4), Arb leg: no zeros of ζ in the closed box, modulo H-ENCL. -/
theorem arbNullDeepT100_exclusion (hEncl : W1EnclOK riemannZeta arbNullDeepT100) :
    ∀ s ∈ W1Rect arbNullDeepT100, riemannZeta s ≠ 0 :=
  (cert_of_checkW1_ap arbNullDeepT100 (checkW1Floor_spec arbNullDeepT100_check).1 hEncl).2 (by decide)

end W1
end Zeta23

end
