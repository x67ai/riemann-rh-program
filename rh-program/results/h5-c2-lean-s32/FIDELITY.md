# H5 — FIDELITY ledger for the Comparator topics `WeilContainmentC2` and `WeilContainmentC2One` (the D5 ledger's (N2) refinement of barrier-zoo IV.1, for continuous g); builder Fable 5.1, Session 32, 2026-09-29

Mirrored in `lean/formalization.yaml` (`fidelity.divergences`, row (x); the D5 row (u)'s (N2) sentence carries a dated FORMALIZED
pointer to it). Brief: `results/h5-c2-lean-s32/BRIEF.md` §0–§2. The record the statements are read against: D5 `FIDELITY.md` (N2) as
corrected 00:45 IST 2026-09-29 ("The refinement 'every tilted datum equals `primeSide k′` for some C² even k′ on the same band' is
true by finite interpolation [… true for g continuous …, false at a band edge otherwise …] at the points ±log n, 2 ≤ n ≤ e^L, but is
NOT formalized and NOT claimed"), D5 `CHECK-O.md` F2 ("The refinement is true for g continuous (so g(±L) = 0), which covers every ŵ of
the record"), and the reader's A7 ("what it gives: prime-side values only; the witness is an interpolant").

**First paragraph, binding (10(c)).** Nothing about ζ or RH follows from anything below. The two theorems are statements about the
prime-side VALUE of a test function: for every continuous even band-limited g and every real a, the number `tiltedPrimeSide a g` is
the number `primeSide k` for some even C² k on the same band. No zero, no zero configuration, no explicit-formula identity, no
archimedean term, no property of ζ, and no statement about Zeta23's `EF_lit` appears in any statement (Zeta23 is not imported on
either side). The label the unit earns (BRIEF §1(4), the reader's A7), verbatim: "IV.1 formalized-in-Lean — prime-side containment
into Zeta23's C² test class for continuous g (prime-side values; the C² witness is an interpolant at ±log n, not the tilted test; zero
side untouched)". It is a refinement of the D5 hardening of IV.1 — a barrier record, not an attack under the sponsor's criterion.

## 1. What IS covered — each claim is a theorem in the challenge files (proved in the solution files)

| record's claim | theorem | exact content |
|---|---|---|
| (N2), for g continuous, at every band: the prime-side number of every continuous even band-limited tilted datum is `primeSide` of a C² even function on the same band | `weilContainment_c2_interpolant` (`Challenge/WeilContainmentC2.lean`) | ∀ (a L : ℝ) (g : ℝ → ℂ), (∀ u, g (-u) = g u) → Continuous g → tsupport g ⊆ Set.Icc (-L) L → ∃ k : ℝ → ℂ, (∀ u, k (-u) = k u) ∧ ContDiff ℝ 2 k ∧ tsupport k ⊆ Set.Icc (-L) L ∧ primeSide k = tiltedPrimeSide a g |
| the same at the band L = log 3 (rung 1, topic `WeilContainmentC2One`; n = 2 interior, n = 3 at the edge) | `weilContainment_c2_interpolant_log3` (`Challenge/WeilContainmentC2One.lean`) | the instance L = Real.log 3, written out (`Set.Icc (-(Real.log 3)) (Real.log 3)`) |

The hypotheses displayed are EXACTLY the three of the brief — `∀ u, g (-u) = g u`, `Continuous g`, `tsupport g ⊆ Set.Icc (-L) L` — and
nothing else; no "H-x" anywhere. Every proof is over Mathlib alone (`import Mathlib` through the unchanged trusted
`ChallengeDeps/WeilContainment.lean`, SHA-256 47c9a508… as in the D5 record); `#print axioms` = [propext, Classical.choice, Quot.sound]
for both names (`rung1-print-axioms.log`, `print-axioms.log`); the comparator (statement identity constant for constant, axiom check,
Lean-kernel replay, nanoda replay) PASSED on both topics (`rung1-comparator.log`, `comparator-run.log`, exit 0 each).

## 2. What is NOT covered — stated nowhere in Lean (each sentence re-derived; the checker will re-derive them again)

* **(N1) The zero side, at any level.** Neither statement mentions a zero, a zero configuration, an explicit-formula identity, or the
  archimedean term. `primeSide` and `tiltedPrimeSide` are the two prime-side functionals of the D5 layer and nothing else; fatal 1's
  in-window "cosh ghost" is untouched. True by inspection of the two challenge files: the only constants they mention beyond Mathlib's
  are `WeilContainment.primeSide` and `WeilContainment.tiltedPrimeSide`.
* **(N2) The tilted test itself is not C², and is not claimed to be.** D5's (N2) stands: `weilTestOf a g = (1/2)·g·e^{−(a−1/2)|·|}` is
  in general not C¹ at 0 (`weilContainment_not_contDiff` at a = 1, g ≡ 1). The witness k of this unit is a DIFFERENT function — an
  interpolant that agrees with the tilted test's prime-side contribution only through the values k(±log n) — and the statement is
  existential, so nothing here says the tilted test lies in the C² class. What changed against D5's ledger is only the sentence
  "NOT formalized": the prime-side NUMBER of every continuous tilted datum is now reached by a member of the class `EF_lit` quantifies
  over.
* **(N3) `EF_lit` is not stated; nothing is fed into it.** No Zeta23 module is imported on either side; `EF_lit`, `literatureRHS`,
  `prime_term` do not occur in any of the seven topic files (the D5 layer restates the prime term character for character, D5
  FIDELITY (D3)). The D5 ledger's sentence "no statement here feeds `weilTestOf a g` into `EF_lit`" stays true, and so does "no
  statement feeds anything into `EF_lit`" for this unit.
* **(N4) The discontinuous case.** With `Continuous g` dropped the family statement is FALSE at a band edge: L = log 2 and g the
  indicator of {±log 2} (even, tsupport = {±log 2} ⊆ [−log 2, log 2]) has `tiltedPrimeSide a g = Λ(2)·2^{−a} = 2^{−a} log 2 ≠ 0`, while
  every continuous k with tsupport k ⊆ [−log 2, log 2] has k(±log 2) = 0 (the limit from outside the band), hence `primeSide k = 0`
  (n = 1 contributes Λ(1) = 0; n ≥ 3 lie outside the band). D5 CHECK-O F2's counterexample stands; continuity is load-bearing and is
  used by the proof exactly once, through "g = 0 on [L, ∞)".
* **(N5) The μ-band and every nonlinear function of the band** (IV.4's rider): outside the statements, which are linear in g.
* **(N6) The archimedean term and the master formula itself:** not stated.
* **(N7) Summability as a datum.** Both sides are `tsum`s; for the data at hand both are finite sums (the tilted side by the cutoff,
  re-proved inside each solution module; the witness side because k vanishes at ±log n for every n with log n ≥ L), so the question
  does not arise. Nothing is stated about convergence.
* **(N8) ζ, RH, any zero of anything.** Nothing.

## 3. Where the formal statement DIFFERS from the prose (each a deliberate choice, recorded)

* **(D1) The witness is an interpolant, not the brief's δ-separated family of bumps.** The brief's pre-derivation (P3)–(P5) builds k as
  Σ_{n∈I} c_n(φ_n(u) + φ_n(−u)) with one bump per interior point and a separation radius δ. The Lean witness is k(u) = P(u²)·φ(u): ONE
  Mathlib bump φ : `ContDiffBump (0 : ℝ)` with rIn = log (max I), rOut = L, times the Lagrange interpolant P (`Lagrange.interpolate`,
  nodes (log n)², values (1/2)·n^{1/2−a}·g(log n), n ∈ I = {2 ≤ n ≤ ⌊e^L⌋ : log n < L}); when I is empty, k = 0. Both are interpolants at
  ±log n with the same values; the statement is existential, so the witness's shape is not part of what is claimed
  (PREDERIVATION-ERRATA E3).
* **(D2) The evenness of g is displayed but not used.** `tiltedPrimeSide a g` reads g only at the points log n ≥ 0, and the witness is
  even by construction. The theorem therefore holds for every continuous g with tsupport g ⊆ Icc (−L) L; the hypothesis is kept
  because the brief fixes the statement and the record's family (cos-transforms of windows) is even (ERRATA E2). No strengthened
  variant is stated.
* **(D3) `ContDiff ℝ 2 k` is what is stated; the witness is C^∞.** The class stated is the one `EF_lit` quantifies over (the brief's
  statement); the proof produces a smooth k and weakens.
* **(D4) The band is `tsupport k ⊆ Set.Icc (-L) L`, the same set as g's, for every real L.** For L < log 2 (and at L = log 2) the interior
  set is empty and k = 0; for L < 0 the band is empty and both sides are 0. Nothing breaks, nothing is claimed beyond the statement.
* **(D5) `tsum` on both sides, as in D5's (D1).** The n ≤ X form is a theorem inside the solution (`cutoff`, the D5 proof re-proved
  locally so that no solution imports the D5 solution or the challenge).
* **(D6) The case L = log 2 is handled by the empty-interior branch**, not by the brief's split "L < log 2 / otherwise"
  (ERRATA E1 — the brief's (P3) presupposes a nonempty interior set, which fails at L = log 2).

## 4. What the label may and may not say

May: the A7 text of §0, verbatim; "for every continuous even band-limited g and every real a, the level-a tilted prime datum equals
Zeta23's prime term at some C² even test on the same band — a kernel-checked theorem over Mathlib alone; the C² witness interpolates
at ±log n and is not the tilted test; the zero side is untouched" (the refutation-shaped close, 10(c), "Lands"). May not: "IV.1's
containment inside `EF_lit`" (nothing is fed into `EF_lit`); "the tilted test is C²" (N2); "the tilted explicit formula is
formalized" (its zero side is false — fatal 1); anything about ζ or RH; anything for discontinuous g (N4).
