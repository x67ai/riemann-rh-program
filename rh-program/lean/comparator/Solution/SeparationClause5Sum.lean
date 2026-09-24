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
comparator/Solution/SeparationClause5Sum.lean — the UNTRUSTED comparator solution module for the topic
`SeparationClause5Sum`: the statement of Challenge/SeparationClause5Sum.lean, byte-identical, PROVED by delegating to
Zeta23/Separation/Clause5.lean (`Zeta23.Separation.clause5_summable`, stated there for any carrier and multiplicity
function with the local finiteness, the local count and the strip; the fields of the trusted `Separation.SepConfig`
are passed one by one).  The trusted `Separation.{B, Z, ft, gammaOf, ftest, BL}`, `Separation.SepConfig.{Wsummand,
outWindow}` are character for character `Zeta23.Separation.{B, Z, ftest, BL}`, `Zeta23.paperFT`, `Zeta23.gammaOf` and
`Zeta23.Separation.wsum` over the raw fields, so the delegation typechecks by definitional unfolding in the kernel.
This module never imports the challenge.  Nothing in this file is part of the trusted base: comparator re-checks that
the theorem below has exactly the statement of its Challenge namesake and uses only the permitted axioms.
Label, binding: "clause 5's summability is Comparator-checked" — never "Theorem M2 is formalized".
-/
import ChallengeDeps.Separation6b
import Zeta23.Separation.Clause5

noncomputable section

/-- **Theorem M2, clause 5 — summability** (separation note §6 (b), absolute convergence): for Z ∈ 𝒞(C₁), t ≥ 3 and
L > 0, the out-window family ‖m_ρ h_f(γ_ρ) conj(h_f(conj γ_ρ))‖ over |Im ρ − t| > 73L is summable — the first conjunct
of `Separation.SepConfig.Hout` at R = 73L, with no numerics and no displayed hypothesis. -/
theorem separation_clause5_summable (C₁ t L : ℝ) (Z : Separation.SepConfig C₁) (ht : 3 ≤ t) (hL : 0 < L) :
    Summable (fun ρ : Z.outWindow t (73 * L) =>
      ‖Z.Wsummand (Separation.ftest t L) (Separation.ftest t L) ρ‖) :=
  Zeta23.Separation.clause5_summable Z.carrier Z.mult Z.finite_window Z.localCount Z.strip ht hL
