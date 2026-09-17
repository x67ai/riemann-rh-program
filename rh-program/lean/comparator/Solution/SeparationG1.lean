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
comparator/Solution/SeparationG1.lean — the UNTRUSTED comparator solution module for the topic `SeparationG1`: the
statement of Challenge/SeparationG1.lean, byte-identical, PROVED by delegating to Zeta23/Separation/LemmaG1.lean
(`Zeta23.Separation.abs_iteratedDeriv_Braw_le`, stated there for every k).  The challenge's `Separation.Braw` is
character for character `Zeta23.Separation.Braw`, so the delegation typechecks by definitional unfolding in the kernel.
This module never imports the challenge.  Nothing in this file is part of the trusted base: comparator re-checks that the
theorem below has exactly the statement of its Challenge namesake and uses only the permitted axioms.
-/
import ChallengeDeps.Separation
import Zeta23.Separation.LemmaG1

noncomputable section

/-- **Lemma G1** (separation note §2): |B_raw^{(k)}(v)| ≤ (k + 1)·(72/e)^k·k^{2k} for every k ≥ 1 and every real v. -/
theorem separation_braw_iteratedDeriv_le :
    ∀ k : ℕ, 1 ≤ k → ∀ v : ℝ,
      |iteratedDeriv k Separation.Braw v| ≤ ((k : ℝ) + 1) * (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) :=
  fun k _ v => Zeta23.Separation.abs_iteratedDeriv_Braw_le k v
