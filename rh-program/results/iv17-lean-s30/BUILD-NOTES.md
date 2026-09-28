# G8 — IV.17's fractional-mark integrality theorem and its rational-mark NEGATION in Lean (zoo formalization-queue item 10): the Comparator topic `IntegralityGap` — build notes (BUILDER, Fable 5.1; Session 30, 2026-09-29 00:47 – 01:10 IST)

Brief: `results/iv17-lean-s30/BRIEF.md` (SHA-256 `9aabf0dbfb74e602941c490a2a3d417e825f33cfad11e537e5c3ff45ee2ffd70`, recomputed at the
start). Record: zoo IV.17 STATEMENT and EXECUTABLE TEST (1)/(3); `results/a4-no-go/theorems.md` Lemma 2.2, Theorem 2.3; `paper.md` §2.4,
§4.2; formalization-queue item 10. Pattern: the D5 unit (`results/d5-lean-s30/BUILD-NOTES.md`, `tools/run.sh`, `SHARED.md`) and the
SeparationG1 delegation precedent (`comparator/Solution/SeparationG1.lean`). Tree: the program's built clone
`~/rh-lean-work/checker-clone-s21` (Lean `v4.33.0-rc2`, commit d8b18978; Mathlib `51e6992e`); `rh-program/lean/` is the source of
truth, mirror direction rh-program → clone by `cp`, `cmp`-identical for every file at the end of every stage (`trust-greps.log`
records the six Lean files + config; README and yaml were mirrored the same way). Local only: **no Prove2Me action** — no mission, no
proposal, no API call; `~/Downloads/assets/prove2me.md` was not read. One `lake build` at a time; Mathlib never compiled from source
(every build reused the clone's oleans: 2081–8703 jobs, all cached but the new modules). No commit by this job. Not independently
checked yet: the Opus 5 clean-clone check (`CHECK-O.md`) is the next job. Stage log with `date` stamps: `SHARED.md`.

**Label, verbatim and binding (BRIEF §1(6)), earned — clause (1) landed with NO displayed hypothesis, so the "if (1) lands" branch:**
**"IV.17's master inequality is a Comparator-checked theorem over integer marks and a Comparator-checked FALSEHOOD over rational marks on
the same Frobenius row (the mark-4/3 instance kernel-checked), over Mathlib alone, no displayed hypothesis, axioms
propext/Classical.choice/Quot.sound, replayed by nanoda"** — the pair channel stays unformalized, and the label says so. The
refutation-shaped close (10(c)) is the "Lands" branch: "IV.17 formalized-in-Lean: (MI) holds over ℤ and fails over ℚ on the same
kernel-checked row; the line where integrality is consumed is the named theorem `per_atom_slack`". **Nothing about ζ or RH follows.**
Stop lines (10(m)): none fired — (i) the rational generalization needed no new idea (TYPING-NOTE.md §2: the same proof for a general
coefficient vector, two cast lemmas exchanged); (ii) `decide +kernel` closed the three ℚ facts on `ZMod 65` without a timeout (8.53 s
for the probe file including the import; 1.3 s for the whole `GridGap` module build); (iii) the unit took about one slot.

## 0. The typing decision (deliverable 1; `TYPING-NOTE.md`, probe `typing-probe.lean`)

The marks enter the integer file's Parseval algebra only through the cast `(m k : K)`, treated as an opaque ring element; the ℂ step
uses one cast lemma (`map_intCast`). Probed in Lean before any theorem was written: rational marks do NOT cast into a general
`[CommRing K]` (no `RatCast`; "Type mismatch") and DO over a `[Field K]`; `map_ratCast`, `Complex.ofReal_ratCast`, `Rat.cast_intCast`
exist with the needed shapes; `decide +kernel` evaluates the ℚ-valued sum, sum of squares and filter-card over `ZMod 65` (Rat
arithmetic reduces in the kernel: `Nat.gcd`/`div`/`mod` are kernel-accelerated, `Rat`'s `DecidableEq` is structural). **Decision:**
the Parseval identity and the flat-band collapse are stated ONCE for a general coefficient vector `dftVec : ZMod M → K` over the integer
file's `[CommRing K] [IsDomain K]`, proofs transferred word for word; `dftMark` (ℤ, any commutative domain) and `dftMarkQ` (ℚ, a field)
are its instances by `rfl`. A cast lemma `m ↦ (m : ℚ)` alone would not have served (the instance's marks are genuinely rational) and is
not what carries the unit; the compatibility `dftMark ζ m = dftMarkQ ζ (m : ℚ)` is recorded as a theorem (`dftMark_eq_dftMarkQ`,
`gridRow_eq_gridRowQ`) so the integer theory is visibly the restriction of the rational one.

## 1. Files and statement decisions

| file | lines | content |
|---|---|---|
| `Zeta23/PairCeiling/GridParsevalRat.lean` | 249 | imports `GridCorner`; namespace `Zeta23.PairCeiling.GridParsevalRat`: `dftVec`, `dftMark_eq_dftVec`, `sum_dftVec_mul_neg`, `flat_band_trace_sq_vec`; `dftMarkQ`, `dftMarkQ_eq_dftVec`, `dftMark_eq_dftMarkQ`, `sum_dftMarkQ_mul_neg`, `flat_band_trace_sq_rat`; `dftMarkQ_neg` (`map_ratCast`), `dftMarkQ_mul_neg_eq_normSq`, `grid_parseval_decoupling_rat`, `trace_sq_grid_rat`; `gridRowQ`, `gridRowQ_eq`, `gridRow_eq_gridRowQ` |
| `Zeta23/PairCeiling/GridGap.lean` | 168 | imports `GridParsevalRat`; namespace `Zeta23.PairCeiling.GridGap`: `per_atom_slack`, `per_atom_slack_fails_rational`, `per_atom_floor`, `per_atom_floor_fails_rational`; `mi_holds_integer` (:= `two_mul_distinct_ge`); `fracMark`, `fracMark_nonneg`, `fracMark_mass`/`fracMark_sq`/`fracMark_Nd` (`decide +kernel`), `fracMark_row`; `mi_fails_rational`, `corner_fails_rational`, `corner_bound_fails_rational` |
| `comparator/ChallengeDeps/IntegralityGap.lean` | 77 | trusted, `import Mathlib` only, namespace `IntegralityGap`: `chi`, `dftMark`, `dftMarkQ`, `zetaM`, `gridRow`, `gridRowQ`, `fracMark` — character for character the Zeta23 definitions (the same `variable` line `{K} [CommRing K] {M} [NeZero M]`, so the implicit arguments agree) |
| `comparator/Challenge/IntegralityGap.lean` | 140 | sixteen statements, every proof `sorry`; the WHAT IS CLAIMED / NOT paragraph (nothing about ζ, laws, the pair channel — Prop. 4.5 not formalized — or any budget but the bandwidth-one grid row; the instance at ε = 0) |
| `comparator/Solution/IntegralityGap.lean` | 118 | imports `ChallengeDeps.IntegralityGap` and `Zeta23.PairCeiling.GridGap`; the sixteen statements byte-identical, each a one-line delegation (definitional unfolding of the trusted vocabulary against the Zeta23 originals); never imports the challenge |
| `comparator/PrintAxioms/IntegralityGap.lean`, `comparator/config-integrality-gap.json` | 35, — | the quick check; 16 names, `propext`/`Quot.sound`/`Classical.choice`, `enable_nanoda: true` |
| `lean/formalization.yaml` | 1275 | `status.scope` sentence, a `main_results` entry, fidelity row (v), a `review.notes` paragraph, three `alignment.namespaces`, two `alignment.statements` rows; schema validation PASS (`yaml-validation.log`, third run: 0 errors, 0 undeclared names, 111 names checked) |
| `lean/README.md` | 537 | section "IntegralityGap (Session 30, 2026-09-29)" before "What these build against" |
| `results/a4-no-go/formalization-status.md` | +29 | dated addendum (2026-09-29); the 2026-08-27 record untouched |

**Statement decisions, against BRIEF §1(1)–(4).** Kept verbatim: the names `dftMarkQ`, `trace_sq_grid_rat`, `gridRowQ`, `gridRowQ_eq`,
`fracMark` (with the brief's definition), `mi_fails_rational` (the brief's statement character for character), `corner_fails_rational`
(the brief's three facts as a conjunction, with `∀ k, 0 ≤ fracMark k` added so that it reads as "every hypothesis of
`grid_corner_pointwise` at N = 64, ε = 0, and the negation of its conclusion"), `mi_holds_integer` (`two_mul_distinct_ge`'s statement),
`per_atom_slack`. Generalized: clause (1)'s "rational marks" is stated for a general coefficient vector first (§0). Added:
`gridRow_eq` and `gridRow_eq_gridRowQ` (so the topic itself shows both halves on ONE row), `fracMark_row` (the budget-tight row value,
the brief's "gridRowQ 32 fracMark = 256/3 = (4/3)·64"), `corner_bound_fails_rational` (the negated-universal form of the corner, the
exact shape of Theorem 2.3's first conclusion with ℚ for ℤ), `per_atom_slack_fails_rational` (the slack fails at 4/3 — the single
failure that, 48 times over, IS the counterexample), `per_atom_floor` and `per_atom_floor_fails_rational` (IV.17 TEST (3) names both
devices, "the (m − 1)(m − 2) slack or the m² ≥ m floor"; both are now named theorems with their ℚ failures). `per_atom_slack` is stated
for EVERY integer m (FIDELITY (v6)). Not added: a re-proof of (MI) through `per_atom_slack` (the re-export is what the brief asks; the
proof text of `two_mul_distinct_ge` is where the slack is consumed, and the header of `GridGap.lean` says so); any law-form or
pair-channel statement.

## 2. Builds (one `lake build` at a time; the clone's Mathlib oleans reused throughout)

* `build-gridparsevalrat.log`: `lake build Zeta23.PairCeiling.GridParsevalRat` — *Build completed successfully (2081 jobs)*, the module
  in 1.6 s, 0 errors, 0 warnings, first try.
* `build-gridgap.log`: `lake build Zeta23.PairCeiling.GridGap` — first try two errors, both `Unknown identifier le_or_lt` (renamed at
  Mathlib 51e6992e); replaced by the integer file's own idiom `rcases (by omega : m ≤ 1 ∨ 2 ≤ m)`; second try *Build completed
  successfully (2082 jobs)*, the module in 1.3 s (the three `decide +kernel` facts over ℚ on `ZMod 65` included), 0 warnings.
* `build-comparator-topic.log`: `lake build Challenge.IntegralityGap Solution.IntegralityGap` — Built `ChallengeDeps.IntegralityGap`
  (18 s, the first load of Mathlib's oleans in that library; 2.9 s at the comparator run), `Challenge.IntegralityGap` (4.1 s) with
  exactly the 16 deliberate `sorry` warnings, `Solution.IntegralityGap` (4.2 s) with 0 warnings — every delegation typechecked by
  definitional unfolding, no `show`/`change`/`convert` needed; *Build completed successfully (8703 jobs)*, 25 s wall, first try.

## 3. Checks

* `print-axioms.log`: `lake env lean comparator/PrintAxioms/IntegralityGap.lean` — 16 lines, each `[propext, Classical.choice,
  Quot.sound]`; and a second section (`zeta23-axioms.lean`, kept in this directory) on the 19 Zeta23 sources plus GridCorner's
  `attainMark_mass`/`attainMark_sq` for comparison — all 21 print the same three (one, `grid_parseval_decoupling_rat`, across three
  lines). No `sorryAx`, no `Lean.ofReduceBool`. Note (FIDELITY (v8)): the `decide +kernel` facts carry `Classical.choice`, as
  GridCorner's do at this toolchain; the brief's "[propext, Quot.sound] or fewer" was not met and is not needed by the label.
* `statement-identity.log`: `tools/statement_identity_g8.py` (the D5 tool, docstring only changed) on the clone AND on the program
  tree — 16/16 IDENTICAL, RESULT PASS on both (a zsh word-splitting slip on the first run — the sixteen names passed as ONE argument —
  is recorded in the log and superseded by the bash second run).
* `trust-greps.log`: `tools/trust_greps_g8.py` (nine words, comments stripped) on the six topic Lean files, both roots — exactly the
  16 deliberate challenge `sorry`s, nothing else (the same slip and second run recorded); tree = mirror by `cmp` for the six files +
  config; imports: the trusted layer `import Mathlib` only, the challenge imports the trusted layer only, the solution imports the
  trusted layer and `Zeta23.PairCeiling.GridGap`.
* `prerun-cleanup.log`: the three modules' artifacts under `.lake/build/{ir,lib/lean}` removed so the comparator builds them itself.
* **`comparator.log`: PASS** — 00:58:17–00:58:49 IST, `31.09 real`, max RSS 5.9 GB; runner `tools/run.sh` (the D5 runner, one comment
  line changed; comparator v4.33.0, lean4export v4.33.0-rc2, nanoda 0.4.17, the fake-landrun shim — NOT sandboxed, as in every prior
  record; the four tool SHA-256s printed in the log); `Built ChallengeDeps.IntegralityGap (2.9s)`, `Built Challenge.IntegralityGap
  (2.0s)` with the 16 deliberate `sorry` warnings, `Built Solution.IntegralityGap (3.2s)`; the export of the 16 names from both
  modules; `Nanoda kernel accepts the solution`, `Lean default kernel accepts the solution`, `Your solution is okay!`,
  `--- comparator exit code: 0 ---`. What the run established: each solution statement coincides constant for constant with its
  challenge namesake (including the trusted `chi`, `dftMark`, `dftMarkQ`, `zetaM`, `gridRow`, `gridRowQ`, `fracMark`); the proofs use
  no axiom outside the three; nanoda re-checked the whole solution export and Lean's kernel replayed it. No CONTROL run this session:
  the tool chain is unchanged since the Session 25 records and the D5 runs earlier tonight.
* `yaml-validation.log`: three runs — the first validated the pre-edit yaml (the edit script had aborted on an anchor before writing;
  0 errors, 28 main_results), the second after the edits found 0 schema errors and 2 "undeclared names" that were the bare MODULE names
  `Zeta23.PairCeiling.GridGap`/`GridParsevalRat` in my strings (the validator reads every `Zeta23.<dotted>` token as a declaration),
  the third after expanding them: **PASS — 0 errors, 0 undeclared names**, 29 main_results, 32 alignment.statements, 111 names.
* `lint-10g.log`: U.S. English throughout; no "clearly / obviously / easy to see / well known".

## 4. Fidelity (FIDELITY.md; yaml row (v))

Covered: rational grid Parseval on the bandwidth-one row and the integer row on the SAME row; the zoo's instance kernel-checked with
the record's numbers verbatim (mass 64, Σm² = 256/3, N_d = 48, row = (4/3)·64); (MI) false over ℚ (96 > 256/3) and the 5/6 corner
false at ε = 0 (48 < 160/3), both as theorems; (MI) true over ℤ on every grid; the two integrality devices as named integer theorems
with their ℚ failures (4/3 and 1/2). Not covered: laws; the pair channel (Prop. 4.5, TEST (2)); any budget but the bandwidth-one grid
row; off the grid; ζ. Differs from the prose: the row's normalization (v1), `ZMod 65` for "the (N+1)-site grid" at N = 64 (v2), the
instance at ε = 0 (v3), (MI) negated in the `3·Σm − Σm²` form with the row form as a second theorem (v4), nonnegative marks with no
floor (v5), the slack for every integer (v6), the general-coefficient Parseval with rational marks over a field (v7), the three axioms
on the kernel facts (v8).

## 5. What an independent checker from a clean clone must do (`CHECK-O.md`; BRIEF §3)

1. Clone `anthropics/zeta-23-lean` at tag `v1.0`, overlay `rh-program/lean/` as `lean/README.md` "Building" says; `lake exe cache get`;
   `lake build Solution.IntegralityGap` (expect ≈ 8703 jobs, 0 errors, 0 warnings from the solution and the Zeta23 modules).
2. `lake env lean comparator/PrintAxioms/IntegralityGap.lean`: 16 lines, each `[propext, Classical.choice, Quot.sound]`; no `sorryAx`,
   no `Lean.ofReduceBool`. Optionally `lake env lean results/iv17-lean-s30/zeta23-axioms.lean` for the Zeta23 sources.
3. `tools/statement_identity_g8.py <clone> IntegralityGap <the sixteen names>` (bash arrays or one name per word — not a single
   quoted string); `tools/trust_greps_g8.py <clone> <the six topic files>` (expect exactly the 16 challenge `sorry`s).
4. The character-for-character claim (FIDELITY §4): `diff` the seven trusted definitions against their Zeta23 originals.
5. The Comparator run with nanoda from the clean clone (`tools/run.sh` pattern with the clone's path; do NOT pre-build the comparator
   layer): `config-integrality-gap.json`.
6. Read the sixteen challenge statements against IV.17's STATEMENT and TEST (1)/(3), `theorems.md` Lemma 2.2, item 10's numbers, and
   against FIDELITY.md: is every "covered" claim a theorem in the file, is every "not covered" fact true, is any hypothesis present
   that the prose does not state? Check by hand that 3·64 − 256/3 = 320/3 > 96 = 2·48 and 48 < 64·5/6 = 160/3, and that
   (4/3 − 1)(4/3 − 2) = −2/9.
7. Recompute every hash in `hashes.txt`; the yaml schema validation; the 10(g) lint.

## 6. Files written and SHA-256

`hashes.txt` (this directory) lists the SHA-256 of every file touched: the two Zeta23 modules, the five comparator files,
`lean/formalization.yaml`, `lean/README.md`, `results/a4-no-go/formalization-status.md`, and every file under
`results/iv17-lean-s30/` (this file's own hash is in `SHARED.md`'s final block and in the chat report). Files under
`results/iv17-lean-s30/`: `TYPING-NOTE.md`, `typing-probe.lean`, `zeta23-axioms.lean`, `SHARED.md`, `BUILD-NOTES.md`, `FIDELITY.md`,
`hashes.txt`, the logs `build-gridparsevalrat.log`, `build-gridgap.log`, `build-comparator-topic.log`, `print-axioms.log`,
`statement-identity.log`, `trust-greps.log`, `prerun-cleanup.log`, `comparator.log`, `yaml-validation.log`, `lint-10g.log`, and
`tools/{run.sh, statement_identity_g8.py, trust_greps_g8.py}`.
