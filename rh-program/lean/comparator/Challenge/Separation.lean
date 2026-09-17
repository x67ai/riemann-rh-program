/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does NOT import it: its imports are Mathlib-only.
-/
/-
comparator/Challenge/Separation.lean — CHALLENGE for M4 (i): Lemma G of Theorem M2's separation note
(rh-program/results/c2-m2/separation-note.md §2), the Fourier decay of the bump B = B_raw/Z.  Trusted vocabulary:
ChallengeDeps.Separation (`Braw`, `Z`, `B`, `ft`, `cB`, `CB`, all defined from Mathlib alone) and Mathlib.
Solution/Separation.lean (untrusted) proves exactly these three statements by delegating to Zeta23/Separation/LemmaG.lean;
github.com/leanprover/comparator checks statement equality, that only the axioms propext, Classical.choice, Quot.sound are
used, and replays the proofs through the Lean kernel and nanoda.

WHAT IS CLAIMED, and what is NOT.  With B̂ := ft (B : ℝ → ℂ) the paper's transform h_B(z) = ∫ B(u) e^{izu} du,
c_B = 2/√(72e) and C_B = e²/Z:
  (G1)  `separation_bump_fourier_decay`          ∀ η : ℝ, ‖B̂(η)‖ ≤ C_B (1 + (c_B/2)√|η|) e^{−c_B√|η|};
  (G, ℂ) `separation_bump_fourier_decay_complex`  ∀ z : ℂ, ‖B̂(z)‖ ≤ e^{|Im z|/2} · C_B (1 + (c_B/2)√|Re z|) e^{−c_B√|Re z|};
  (G2)  `separation_bump_fourier_decay_pure_exp` ∀ η : ℝ, ‖B̂(η)‖ ≤ 4e^{−3/4} C_B · e^{−(7/8)c_B√|η|}.
NO displayed hypothesis: B, Z, c_B, C_B are concrete; Z and C_B are real numbers defined by an integral and no digit of
either is asserted (Z ≈ 0.222, C_B ≈ 33.28 are remarks of the note, not content).  The transform is the paper's convention
(sign +i, no 2π, complex argument), re-declared as `ft` in ChallengeDeps.Separation; nothing is claimed for Mathlib's `𝓕`.
The strip weight e^{|Im z|/2} is the one for the support [−1/2, 1/2] of B; the note's clause-5 use at the argument
L(x − t) − iLy is an instance by scaling and is NOT stated here.  Nothing is claimed about the numerical decay rate of B̂
(≈ 0.85 per √η, computed, not proved — the note §2), about ζ, or about Theorem M2's other clauses.  The number 2/√(72e)
comes from the derivative bound (72/e)^k k^{2k} of Lemma G1 (Challenge/SeparationG1.lean); that provenance is not a theorem.

The `sorry`s below are deliberate (this is the challenge side); expect "declaration uses 'sorry'" warnings when building
this module.
-/
import ChallengeDeps.Separation

noncomputable section

/-- **Lemma G (G1)** (separation note §2): ‖B̂(η)‖ ≤ C_B (1 + (c_B/2)√|η|) e^{−c_B√|η|} for every real η. -/
theorem separation_bump_fourier_decay (η : ℝ) :
    ‖Separation.ft (fun v => (Separation.B v : ℂ)) η‖
      ≤ Separation.CB * (1 + Separation.cB / 2 * Real.sqrt |η|)
        * Real.exp (-(Separation.cB * Real.sqrt |η|)) := by
  sorry

/-- **Lemma G, complex-argument form** (separation note §2): ‖B̂(z)‖ ≤ e^{|Im z|/2} · G(|Re z|) for every z ∈ ℂ,
G the right-hand side of (G1). -/
theorem separation_bump_fourier_decay_complex (z : ℂ) :
    ‖Separation.ft (fun v => (Separation.B v : ℂ)) z‖
      ≤ Real.exp (|z.im| / 2)
        * (Separation.CB * (1 + Separation.cB / 2 * Real.sqrt |z.re|)
          * Real.exp (-(Separation.cB * Real.sqrt |z.re|))) := by
  sorry

/-- **Lemma G (G2)** (separation note §2): ‖B̂(η)‖ ≤ C_B′ e^{−c_B′√|η|} with c_B′ = (7/8)c_B, C_B′ = 4e^{−3/4}C_B. -/
theorem separation_bump_fourier_decay_pure_exp (η : ℝ) :
    ‖Separation.ft (fun v => (Separation.B v : ℂ)) η‖
      ≤ 4 * Real.exp (-3 / 4) * Separation.CB
        * Real.exp (-(7 / 8 * Separation.cB * Real.sqrt |η|)) := by
  sorry
