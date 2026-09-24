/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does NOT import it: it imports Mathlib and the trusted
modules ChallengeDeps.Separation6b (hence Separation, SepConfig, Separation6) only.
-/
/-
comparator/ChallengeDeps/Separation5.lean — the TRUSTED definition layer added for the comparator topic `Separation5`
(Unit B of the M4 residue, Session 25 item 2: clause 5 of Theorem M2 modulo H-R₀; rh-program/results/c2-m2/separation-note.md
§6 and addendum A3; contract rh-program/results/c2-m4/PRICING-RESIDUE.md §1 Piece 1; build record
rh-program/results/c2-m4/BUILD-NOTES-B.md).  It IMPORTS the frozen ChallengeDeps.Separation6b (which imports the frozen
ChallengeDeps.{Separation, SepConfig, Separation6}) and re-declares nothing: `SepConfig`, `Hout`, `outWindow`, `Wsummand`,
`ftest`, `HB3`, `Hedge`, `Rstar`, `orbit`, `cB`, `CB`, `Z`, `b1sym` are the SAME declarations the M4 (iii) and Unit A runs
checked.  It adds, in the namespace `Separation`, the objects of the displayed one-point check H-R₀ — transcriptions,
term for term, of rh-program/results/c2-m2/verify/r0_73_check.py lines 22–33 (fidelity (r2); the diff at four values of L
is rh-program/results/c2-m4/verify-B/p23-diff.log):
  gammaPoly n a s := Σ_{j=0}^{n} (n!/j!)·s^j/a^{n+1−j}                         line 22–23, `gamma_poly(n, a, s)`
  Prelax m L      := β^m·C_B²·[(73L)^m(1 + (c_B/2)√73·L)²                       line 24–29, `P_relaxed(m, L, 73, 50)`:
                       + (2/L^{m+1})(γ_{2m+1} + c_Bγ_{2m+2} + (c_B²/4)γ_{2m+3})(2c_B, √73·L)],   a = 2c_B, sR = √73·L,
                     β = 1 + 3/(2(73·50 − 1))                                      u0 = 73L, beta = 1 + 3/(2(R0·L0 − 1))
  P2 L := Prelax 2 L,  P3 L := Prelax 3 L
  F13 L := (13/8 − 2c_B√73)·L + 2c_B/√73 + log((1.05·P2 L + P3 L)/b₁sym)        line 31–33, `Ftilde(L, 73, 50, 13/8)`,
                                                                                    with b₁ = b₁sym (Unit A's proved b₁)
  HR0 := F13 50 ≤ 0 ∧ 5/(2c_B√73 − 13/8) ≤ 50                                    the one-point check at L₀ = 50, R₀ = 73
(the script's b1 is the record's certified digit 8.69808; here b₁ is the real number (2e^{−1}/Z)², so the Lean F13(50)
is the script's −0.3227 minus log(10.984/8.698) = −0.556 — smaller, i.e. the check is EASIER with the proved b₁).
H-R₀ is a DISPLAYED real inequality about explicitly defined reals (c_B, C_B, Z, b₁sym from Mathlib alone); it is not
a theorem here.  1(b) (topic Separation5c, if it lands) proves it as a theorem from a 16-cell rational enclosure of Z.
A reader who wants to know WHAT is claimed reads this file, ChallengeDeps/{Separation, SepConfig, Separation6,
Separation6b}.lean and the challenge files only.
-/
import Mathlib
import ChallengeDeps.Separation6b

namespace Separation

noncomputable section

/-- γ_n(a, s) := Σ_{j=0}^{n} (n!/j!)·s^j/a^{n+1−j} — `r0_73_check.py` lines 22–23 (`gamma_poly`), term for term. -/
def gammaPoly (n : ℕ) (a s : ℝ) : ℝ :=
  ∑ j ∈ Finset.range (n + 1), (n.factorial : ℝ) / (j.factorial : ℝ) * s ^ j / a ^ (n + 1 - j)

/-- P_m(L) — `r0_73_check.py` lines 24–29 (`P_relaxed(m, L, 73, 50)`), term for term. -/
def Prelax (m : ℕ) (L : ℝ) : ℝ :=
  (1 + 3 / (2 * (73 * 50 - 1))) ^ m * CB ^ 2 *
    ((73 * L) ^ m * (1 + cB / 2 * (Real.sqrt 73 * L)) ^ 2 +
      2 / L ^ (m + 1) * (gammaPoly (2 * m + 1) (2 * cB) (Real.sqrt 73 * L)
        + cB * gammaPoly (2 * m + 2) (2 * cB) (Real.sqrt 73 * L)
        + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) (Real.sqrt 73 * L)))

/-- P₂ := P_relaxed(2, L, 73, 50). -/
def P2 (L : ℝ) : ℝ := Prelax 2 L

/-- P₃ := P_relaxed(3, L, 73, 50). -/
def P3 (L : ℝ) : ℝ := Prelax 3 L

/-- F₁₃(L) := (13/8 − 2c_B√73)L + 2c_B/√73 + log((1.05P₂(L) + P₃(L))/b₁sym) — `r0_73_check.py` lines 31–33
(`Ftilde(L, 73, 50, 13/8)`), term for term, with b₁ = b₁sym. -/
def F13 (L : ℝ) : ℝ :=
  (13 / 8 - 2 * cB * Real.sqrt 73) * L + 2 * cB / Real.sqrt 73 + Real.log ((105 / 100 * P2 L + P3 L) / b1sym)

/-- **H-R₀** (displayed): the one-point check of addendum A3 at L₀ = 50, R₀ = 73 — F₁₃(50) ≤ 0 and
5/(2c_B√73 − 13/8) ≤ 50 (the decrease of F₁₃ from 5/(2c_B√73 − 13/8) = 6.11 on). -/
def HR0 : Prop := F13 50 ≤ 0 ∧ 5 / (2 * cB * Real.sqrt 73 - 13 / 8) ≤ 50

end

end Separation
