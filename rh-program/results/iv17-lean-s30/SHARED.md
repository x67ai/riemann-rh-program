# G8 / IV.17 — SHARED log (builder Fable 5.1, then checker Opus 5); Session 30, 2026-09-29

Brief `BRIEF.md` SHA-256 `9aabf0dbfb74e602941c490a2a3d417e825f33cfad11e537e5c3ff45ee2ffd70`. Every block dated by `date`.

## [builder] Tue Sep 29 00:50:30 IST 2026 — deliverable 1 landed: `TYPING-NOTE.md` (+ the probe `typing-probe.lean`)
Both Zeta23 files read in full. The mark type enters the Parseval algebra only through the cast `(m k : K)`, used as an opaque ring
element; the ℂ step uses one cast lemma (`map_intCast`). Probe through the built clone: rational marks do NOT cast into a general
`CommRing` (need `Field`); `map_ratCast`, `Complex.ofReal_ratCast`, `Rat.cast_intCast` exist; `decide +kernel` closes the three
ℚ facts on `ZMod 65` (mass 64, Σm² = 256/3, N_d = 48) in one 8.53 s file. Decision: Parseval stated once for a general coefficient
vector `dftVec` over the integer file's `[CommRing K] [IsDomain K]`, with `dftMark` (ℤ) and `dftMarkQ` (ℚ, `[Field K]`) as `rfl`
instances. Stop lines (i) and (ii) do not fire. Note: the ℚ kernel facts depend on all three standard axioms (not `[propext, Quot.sound]`).
SHA-256 TYPING-NOTE.md = fd3b5464000352689645b0a73f36a48970b526bb3aa18ba87df8a2d71e37fb7d.
Next: `Zeta23/PairCeiling/GridParsevalRat.lean`, built alone.

## [builder] Tue Sep 29 00:58:17 IST 2026 — the Lean files landed and built; the three quick checks PASS
Files (source of truth `rh-program/lean/`, mirrored rh-program → `~/rh-lean-work/checker-clone-s21` by `cp`, `cmp`-identical, logged in
`trust-greps.log`): `Zeta23/PairCeiling/GridParsevalRat.lean` (general-coefficient Parseval `dftVec`, rational marks `dftMarkQ`,
`trace_sq_grid_rat`, `gridRowQ`, `gridRowQ_eq`, `gridRow_eq_gridRowQ`; `build-gridparsevalrat.log`: Built, 2081 jobs, first try, 0
warnings), `Zeta23/PairCeiling/GridGap.lean` (`per_atom_slack`/`per_atom_floor` and their ℚ failures, `fracMark` + kernel facts,
`mi_holds_integer`, `mi_fails_rational`, `corner_fails_rational`, `corner_bound_fails_rational`; `build-gridgap.log`: one fix —
`le_or_lt` no longer exists at 51e6992e, replaced by the integer file's `rcases (by omega : …)` split — then Built, 2082 jobs, 0 warnings),
`comparator/ChallengeDeps/IntegralityGap.lean` (Mathlib only; `chi`, `dftMark`, `dftMarkQ`, `zetaM`, `gridRow`, `gridRowQ`, `fracMark`
character for character), `Challenge/IntegralityGap.lean` (16 statements, `sorry`), `Solution/IntegralityGap.lean` (16 delegations to the
Zeta23 modules), `PrintAxioms/IntegralityGap.lean`, `config-integrality-gap.json`. `build-comparator-topic.log`: `lake build
Challenge.IntegralityGap Solution.IntegralityGap` — Built ChallengeDeps.IntegralityGap (18s), Challenge (4.1s) with exactly the 16
deliberate `sorry` warnings, Solution (4.2s) with 0 warnings, *Build completed successfully (8703 jobs)*, 25 s wall.
* `print-axioms.log`: the 16 topic names and the 21 Zeta23 originals (incl. GridCorner's `attainMark_mass`/`attainMark_sq` for
  comparison) ALL print `[propext, Classical.choice, Quot.sound]`; no `sorryAx`, no `Lean.ofReduceBool`.
* `statement-identity.log`: 16/16 IDENTICAL on the clone AND on the program tree (a zsh word-splitting slip on the first run is
  recorded there and superseded by the bash second run).
* `trust-greps.log`: nine words, comments stripped, six files, both roots — exactly the 16 challenge `sorry`s, nothing else; tree =
  mirror for the 6 Lean files + config; the trusted layer imports Mathlib only.
Next: pre-run cleanup of the topic's artifacts, then the comparator run with nanoda (`tools/run.sh`, the D5 runner).
