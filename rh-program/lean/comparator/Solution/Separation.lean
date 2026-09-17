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
comparator/Solution/Separation.lean — the UNTRUSTED comparator solution module for the topic `Separation`: the three
statements of Challenge/Separation.lean, byte-identical, each PROVED by delegating to Zeta23/Separation/LemmaG.lean
(`Zeta23.Separation.norm_paperFT_Bc_ofReal_le`, `norm_paperFT_Bc_le`, `norm_paperFT_Bc_ofReal_le'`).  The challenge's
`Separation.Braw`, `Z`, `B`, `cB`, `CB` are character for character `Zeta23.Separation`'s, and `Separation.ft` is character
for character `Zeta23.paperFT`, so each delegation typechecks by definitional unfolding in the kernel.  This module never
imports the challenge.  Nothing in this file is part of the trusted base: comparator re-checks that every theorem below has
exactly the statement of its Challenge namesake and uses only the permitted axioms.
-/
import ChallengeDeps.Separation
import Zeta23.Separation.LemmaG

noncomputable section

/-- **Lemma G (G1)** (separation note §2): ‖B̂(η)‖ ≤ C_B (1 + (c_B/2)√|η|) e^{−c_B√|η|} for every real η. -/
theorem separation_bump_fourier_decay (η : ℝ) :
    ‖Separation.ft (fun v => (Separation.B v : ℂ)) η‖
      ≤ Separation.CB * (1 + Separation.cB / 2 * Real.sqrt |η|)
        * Real.exp (-(Separation.cB * Real.sqrt |η|)) :=
  Zeta23.Separation.norm_paperFT_Bc_ofReal_le η

/-- **Lemma G, complex-argument form** (separation note §2): ‖B̂(z)‖ ≤ e^{|Im z|/2} · G(|Re z|) for every z ∈ ℂ,
G the right-hand side of (G1). -/
theorem separation_bump_fourier_decay_complex (z : ℂ) :
    ‖Separation.ft (fun v => (Separation.B v : ℂ)) z‖
      ≤ Real.exp (|z.im| / 2)
        * (Separation.CB * (1 + Separation.cB / 2 * Real.sqrt |z.re|)
          * Real.exp (-(Separation.cB * Real.sqrt |z.re|))) :=
  Zeta23.Separation.norm_paperFT_Bc_le z

/-- **Lemma G (G2)** (separation note §2): ‖B̂(η)‖ ≤ C_B′ e^{−c_B′√|η|} with c_B′ = (7/8)c_B, C_B′ = 4e^{−3/4}C_B. -/
theorem separation_bump_fourier_decay_pure_exp (η : ℝ) :
    ‖Separation.ft (fun v => (Separation.B v : ℂ)) η‖
      ≤ 4 * Real.exp (-3 / 4) * Separation.CB
        * Real.exp (-(7 / 8 * Separation.cB * Real.sqrt |η|)) :=
  Zeta23.Separation.norm_paperFT_Bc_ofReal_le' η
