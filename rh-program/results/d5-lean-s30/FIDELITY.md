# D5 (F3, G4) — FIDELITY ledger for the Comparator topics `WeilContainment` and `WeilContainmentOne` (barrier-zoo IV.1, the C1 containment theorem); builder Fable 5.1, Session 30, 2026-09-28/29

Mirrored in `lean/formalization.yaml` (`fidelity.divergences`, row (u) — the letters n, o, p, q, r, s, t, w were already taken, out of order). Brief: `results/d5-lean-s30/BRIEF.md` §1(1) "the fidelity
paragraph". The record the statements are read against: zoo IV.1 STATEMENT ("C1's entire (a,w)-family of prime-computable tilted-EF
observables was identified with classical Weil tests (1/2)ŵ(u)e^{−(a−1/2)|u|} on the same band via bounded-below multipliers — the
family spans exactly bandwidth-log X Weil-EF data; multi-a constraints follow from single-band data by analytic continuation
(information-free). 'No new data coordinate.'"), its source `results/adjudication-C1.json` fatal 2 and the mandatory repair ("the
full (a,w)-family of prime-computable tilted-EF observables at cutoff X lies inside the classical bandwidth-log X Weil-EF data
class"), and C1's MASTER FORMULA prime side "Σ_{n ≤ X} Λ(n) n^{−a} (cos-transform of w)(log n)".

**First paragraph, binding (10(c)).** Nothing about ζ or RH follows from anything below. The theorems are statements about two
prime-side FUNCTIONALS of a test function — Zeta23's classical prime term and C1's tilted prime term — and about the multiplier
e^{−(a−1/2)|u|}; no zero, no zero configuration, no explicit-formula identity, no archimedean term, and no property of ζ appears in
any statement. The label the unit earns (BRIEF §1(4)), verbatim: "IV.1 formalized-in-Lean (prime-side containment; Comparator-checked
over Mathlib alone, no displayed hypothesis, axioms propext/Classical.choice/Quot.sound, replayed by nanoda; built at
v4.33.0-rc2/51e6992e and v4.33.1/0df444a)". The Prove2Me kernel check is NOT part of it (nothing was posted).

## 1. What IS covered — each claim is a theorem in `lean/comparator/Challenge/WeilContainment.lean` (proved in `Solution/WeilContainment.lean`)

| record's claim | theorem | exact content |
|---|---|---|
| the identification of the (a, w)-family's prime side with classical Weil tests (1/2)ŵ(u)e^{−(a−1/2)|u|} — for EVERY real a | `weilContainment_identity` | ∀ a : ℝ, ∀ g : ℝ → ℂ even, `tiltedPrimeSide a g = primeSide (weilTestOf a g)`, i.e. Σ_n Λ(n)n^{−a}g(log n) = Σ_n (Λ(n)/√n)(k(log n) + k(−log n)) at k = (1/2)·g·e^{−(a−1/2)|·|}; no summability hypothesis (term-by-term identity of `tsum`s) |
| the same at C1's proven ray a = 1 (rung 1, topic `WeilContainmentOne`) | `weilContainment_identity_one` | the instance a = 1 |
| "at cutoff X" — the master formula's n ≤ X | `weilContainment_cutoff` | for tsupport g ⊆ [−L, L]: `tiltedPrimeSide a g = ∑ n ∈ Finset.range (⌊e^L⌋₊ + 1), Λ(n)·n^{−a}·g(log n)` — the sum over all n IS the finite sum over n ≤ X = e^L |
| "bounded-below multipliers … on the compact band", with the constants | `weilContainment_tilt_bounds`, `weilContainment_tilt_pos` | for |u| ≤ L: e^{−|a−1/2|L} ≤ tilt a u ≤ e^{|a−1/2|L}; tilt a u > 0 for all a, u |
| "on the same band" | `weilContainment_tsupport_eq` (and the weaker `weilContainment_tsupport`) | tsupport (weilTestOf a g) = tsupport g, for every a and g (no hypothesis) |
| the classical test is an admissible even test; continuity carries over | `weilContainment_even`, `weilContainment_continuous` | g even ⟹ weilTestOf a g even; g continuous ⟹ weilTestOf a g continuous |
| the level-(1 − a) tilt inverts the level-a tilt (the algebraic form of "multi-a constraints follow from single-band data") | `weilContainment_tilt_inv` | tilt a u · tilt (1 − a) u = 1 |
| the CONVERSE containment | `weilContainment_exact` | for every a, L and every even k with tsupport k ⊆ [−L, L]: ∃ even g with tsupport g ⊆ [−L, L] and primeSide k = tiltedPrimeSide a g (witness g = 2k·tilt (1 − a)) |
| "the family spans EXACTLY bandwidth-log X Weil-EF data" — the record's sentence as ONE statement | `weilContainment_range_eq` | ∀ a L : ℝ, { tiltedPrimeSide a g \| g even, tsupport g ⊆ [−L, L] } = { primeSide k \| k even, tsupport k ⊆ [−L, L] } as sets of complex numbers |
| the tilt does NOT preserve the C² class (the ledger's "not covered" fact, made a theorem) | `weilContainment_not_contDiff` | ¬ ContDiff ℝ 2 (weilTestOf 1 (fun _ => 1)): at a = 1, g ≡ 1 the test (1/2)e^{−|u|/2} is not C² (not even differentiable at 0) |

Every statement is concrete — NO displayed hypothesis, no "H-x" anywhere; every proof is over Mathlib alone (`import Mathlib`
through the trusted `ChallengeDeps/WeilContainment.lean`; no Zeta23 import on either side); `#print axioms` = [propext,
Classical.choice, Quot.sound] for all 13 names; the comparator (statement identity constant for constant, axiom check, Lean-kernel
replay, nanoda replay) PASSED on both topics (`rung1-comparator.log`, `comparator-run.log` second run); the same 13 statements
build and prove at Lean v4.33.1 / Mathlib 0df444a in the Prove2Me layout (`prove2me-build.log`, `prove2me-print-axioms.log`).

## 2. What is NOT covered (true statements about the files; none of these is claimed anywhere in Lean)

* **(N1) The zero side, at any level.** No statement mentions zeros, `ZeroConfig`, `EF_lit`, `literatureRHS` as a whole, `paperFT`,
  or an explicit-formula identity. The record's fatal 1 (the tilted EF's zero side is false below the in-window zero depth — the
  "cosh ghost") is untouched: IV.1 is a statement about the PRIME side, and so are these theorems.
* **(N2) The Zeta23 test class.** Zeta23's `EF_lit` quantifies over `ContDiff ℝ 2 k → HasCompactSupport k`. The tilt does not
  preserve `ContDiff ℝ 2` as a class (`weilContainment_not_contDiff` is the witness; in general, for g(0) ≠ 0 and a ≠ 1/2, k_{a,g}
  is not even C¹ at 0 [CORRECTION 00:45 IST 2026-09-29, Session 30 — CHECK-O F1 (Opus 5), re-derived by the orchestrator: this presupposes g differentiable at 0; for C1's family (windows w ≥ 0, w ≢ 0, at every a > 1/2) k_{a,g} is not differentiable at 0 (g ≤ g(0) = ∫w > 0); without differentiability of g the claim fails (g = 2e^{(a−1/2)|u|} gives k ≡ 1, `check-O/probe_E2_counterexample.lean`), and at a < 1/2 it fails for the Fejér window at a = 1/2 − 1/L. The theorem `weilContainment_not_contDiff` is unaffected.] — the one-sided derivatives differ by (a − 1/2)g(0), and for C1's windows w ≥ 0, w ≢ 0 one has
  g(0) = ∫w > 0; the errata E2 corrects the brief's "not C²" to this sharp form, which is FALSE for g vanishing to order ≥ 3 at 0).
  Consequently no statement here feeds `weilTestOf a g` into `EF_lit`, and the classical data class of these theorems is
  "even, band-limited, no regularity". The refinement "every tilted datum equals `primeSide k′` for some C² even k′ on the same band"
  is true by finite interpolation [CORRECTION 00:45 IST 2026-09-29, Session 30 — CHECK-O F2 (Opus 5), re-derived by the orchestrator: true for g continuous (every cos-transform of a window), false at a band edge otherwise — L = log 2, g the indicator of {±log 2}: tiltedPrimeSide = 2^{−a} log 2 while every continuous k′ with tsupport ⊆ [−log 2, log 2] has primeSide k′ = 0. Not claimed anywhere in Lean.] at the points ±log n, 2 ≤ n ≤ e^L, but is NOT formalized and NOT claimed.
* **(N3) The μ-band and every nonlinear function of the band** (IV.4's rider, the s25 sharpening carried by every digest since):
  outside the statements, which are linear in the test.
* **(N4) The archimedean term** Arch_a(w) of the master formula and the master formula itself (an identity with a zero side): not
  stated.
* **(N5) Summability as a datum.** `tsum` of a non-summable family is 0 in Mathlib; `weilContainment_identity` is an unconditional
  identity of `tsum`s because the summands agree term by term, so it says nothing about convergence. For the data the record
  speaks of (band-limited g) both sums are FINITE by `weilContainment_cutoff`, so the question does not arise there.
* **(N6) ζ, RH, any zero of anything.** Nothing.

## 3. Where the formal statement DIFFERS from the prose (each a deliberate choice, recorded)

* **(D1) `tsum` over all n : ℕ in place of "Σ_{n ≤ X}".** `tiltedPrimeSide` and `primeSide` sum over every natural number, with
  Λ(0) = Λ(1) = 0 and Mathlib's conventions log 0 = 0, √0 = 0, 0^{−a} ∈ {0, 1}. The n ≤ X form is recovered as the THEOREM
  `weilContainment_cutoff` (equality with the finite sum over n ≤ ⌊e^L⌋ when tsupport g ⊆ [−L, L]) — "equal by a theorem of the
  file", not by convention (errata E5).
* **(D2) The algebraic inverse in place of "analytic continuation".** The record derives multi-a constraints from single-band data
  "by analytic continuation"; the formal statements give the STRONGER, hypothesis-free algebraic route: tilt a · tilt (1 − a) = 1
  (`weilContainment_tilt_inv`), hence the explicit witness in `weilContainment_exact` and the set equality `weilContainment_range_eq`
  for every a at once. No analytic continuation, no convergence, no regularity is used or stated.
* **(D3) The restated prime term.** `primeSide k` is Zeta23's `literatureRHS` prime term (`Zeta23/ExplicitFormula.lean`,
  `∑' n : ℕ, ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) * (k (Real.log n) + k (-Real.log n))`) re-declared character
  for character in `ChallengeDeps/WeilContainment.lean` so that the trusted layer imports Mathlib only (the `Separation.ft` =
  `paperFT` precedent). It is definitionally the Zeta23 expression; no Lean statement of this unit ties it to Zeta23 by a theorem
  (none is needed — the containment is between two Mathlib-defined functionals), and a reader who wants the connection to
  `literatureRHS` compares the two lines by eye (the checker's item).
* **(D4) "cos-transform of w" is the even function g.** The prose parametrizes the family by the window w (via its cos-transform
  ĝ = cos-transform of w, which is even for EVERY w — errata E3); the formal statements quantify over the even function g directly,
  with evenness spelled out as `∀ u, g (−u) = g u` (no `Function.Even` API, no `Real.cos`, no integral). This is a strictly larger
  family (every even g, not only cos-transforms of windows with ŵ supported in the band), so the containment proved is stronger
  than the prose one; the record's "w ≥ 0" plays no role on the prime side and is not stated.
* **(D5) The tilt at every real a.** The master formula is stated for a > 1/2; the formal identity holds for every real a with no
  case split (a ≤ 1/2 "de-tilts"). Complex a is not treated.
* **(D6) The band is `Set.Icc (−L) L` on `tsupport`, L = log X**, exactly Zeta23's `prime_term` hypothesis (`tsupport k ⊆ Icc (−L) L`).
  For L < 0 the band is empty, every band-limited test is 0 and both sides are 0 — nothing breaks, nothing is claimed.
* **(D7) `tilt_bounds` drops the brief's redundant `0 ≤ L`** (implied by |u| ≤ L; errata E4) — a strictly stronger statement of the
  same content. **`tsupport` is stated as an EQUALITY** (errata E6) alongside the brief's inclusion.
* **(D8) Names in the Prove2Me layout.** The mirror names each theorem `WeilContainment.<suffix>` (the platform's slug rule
  `Thm_<name with dots as underscores>`) where the comparator topic names it `weilContainment_<suffix>`; the STATEMENT text is
  byte-identical in the three places (challenge, platform stub, platform solution), checked by `prove2me-print-axioms.log`.

## 4. What the label may and may not say

May: "IV.1 formalized-in-Lean (prime-side containment; …)" as in §0 above; "the level-a tilted prime data and the classical band-L
Weil prime data are the same set of numbers, for every a, through multipliers bounded by e^{±|a−1/2|L}" (the refutation-shaped
close, 10(c), "Lands"). May not: "the tilted explicit formula is formalized" (its zero side is false — fatal 1); "C1's family lies
in Zeta23's C² test class" (N2); anything about ζ or RH; "kernel-checked on Prove2Me" (nothing was posted).
