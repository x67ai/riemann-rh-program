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

## [builder] Tue Sep 29 01:04:21 IST 2026 — Comparator PASS with nanoda; the record edits landed
`prerun-cleanup.log` (the topic's three modules' artifacts removed); `comparator.log` (runner `tools/run.sh`, the D5 runner with the
s21 clone path; comparator v4.33.0, lean4export v4.33.0-rc2, nanoda 0.4.17, fake-landrun shim — NOT sandboxed; tool SHA-256s in the
log): Built ChallengeDeps.IntegralityGap (2.9s), Challenge.IntegralityGap (2.0s) with the 16 deliberate `sorry` warnings,
Solution.IntegralityGap (3.2s); "Nanoda kernel accepts the solution", "Lean default kernel accepts the solution", "Your solution is
okay!", `--- comparator exit code: 0 ---`, 31.09 s real, 00:58:17–00:58:49 IST.
Record edits (tree = source of truth; README + yaml mirrored tree → clone, cmp-identical): `lean/formalization.yaml` (status.scope
sentence, a main_results entry, fidelity row (v), a review.notes paragraph, three namespaces, two alignment.statements rows;
`yaml-validation.log`: first run validated the pre-edit file (an anchor slip aborted the edit script before writing), second run 0
schema errors + 2 "undeclared" hits that were bare MODULE names read as declarations, third run after expanding them: see the log's
last RESULT line); `lean/README.md` section "IntegralityGap (Session 30, 2026-09-29)" before "What these build against";
`results/a4-no-go/formalization-status.md` dated addendum (2026-09-29; the 2026-08-27 record untouched).
Next: FIDELITY.md, BUILD-NOTES.md, lint, hashes.

## [builder] Tue Sep 29 01:07:20 IST 2026 — CLOSE: every deliverable on disk; handing to the checker
`FIDELITY.md` (SHA-256 09a26a2b1c68880d5f64d1745263d8d9cea49b7f0cd93da407300df541b6a780), `BUILD-NOTES.md` (SHA-256 a3c3bd698b92f4deed1d73b39759739034ced9b906d884776efa77da613bb728), `lint-10g.log` (clean),
`hashes.txt` (SHA-256 7f74bc0e0ed3f94abe3e01b0b7536afb8142dd11e44c388534884324ceb6e204; every other file's hash is inside it). `yaml-validation.log` third run: PASS, 0 errors, 0 undeclared
names. Label earned (BRIEF §1(6), the "(1) lands" branch), no H-row displayed, no stop line fired, nothing posted anywhere, nothing
committed. The clone `~/rh-lean-work/checker-clone-s21` holds cmp-identical copies of the six Lean files, the config, README and yaml.
Next (orchestrator): launch the Opus 5 clean-clone checker per BRIEF §3 → `CHECK-O.md`.
