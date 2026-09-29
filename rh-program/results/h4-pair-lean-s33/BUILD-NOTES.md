# H4 — IV.17's pair channel (Prop. 4.5) in Lean with a dyadic certificate on ā: the Comparator topic `PairChannel` — build notes (BUILDER, Fable 5.1; Session 33, 2026-09-29 11:09 – 11:50 IST)

Brief: `results/h4-pair-typing-s32/UNIT-BRIEF.md` (SHA-256 `2d80f9db8ccf04765840b041189dc771813f5fdbb77767c40d471e8b9908cb94`, recomputed at the start). Record: `paper.md` §2.3, §4.2
(Prop. 4.5); `pair-channel.md` §0–§4 (Prop. 3.1, (T1), (T3)); the typing note `results/h4-pair-typing-s32/TYPING-NOTE.md` and its probe
`typing-probe.lean` / `typing-probe.log`. Pattern: the IV.17 unit (`results/iv17-lean-s30/`) for the packaging and the H5 unit
(`results/h5-c2-lean-s32/`) for the tools and the CHECK-O lessons. Tree: the program's built clone `~/rh-lean-work/checker-clone-s21`
(Lean `v4.33.0-rc2`, commit d8b18978; Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`); `rh-program/lean/` is the source of truth,
mirror direction rh-program → clone by `cp`, `cmp`-identical for the six Lean files and the config (`trust-greps.log`). One `lake build` at
a time; Mathlib never compiled from source (every build reused the clone's oleans; 2274–8704 jobs, only the new modules built). No
commit by this job. No Lean file was edited after the comparator run. Not independently checked yet: the Opus 5 clean-clone check
(`CHECK-O.md`) is the next job. Stage log with `date` stamps: `SHARED.md`.

**Nothing about ζ or RH follows from anything below (10(c), first paragraph).** The theorems are about one quadratic form on finite
configurations of a cyclic grid and the flat average ā of cosh; no zero, no explicit formula, no law appears in any statement.

**Label, verbatim and binding (UNIT-BRIEF §1(3)), earned — every statement landed with no displayed hypothesis beyond its own binders, so
the "only if everything lands" clause holds:** **"IV.17's pair channel: Prop. 4.5 Comparator-checked for every depth and real mark, the
integer-mark safety chain a theorem, and the floor F1 ≥ S2's failure for a real-marked pair at (1/4, 1/20) kernel-checked by a dyadic
certificate — over Mathlib alone, no displayed hypothesis, the three standard axioms, replayed by nanoda".** The refutation-shaped close
(10(c)) is the "Lands" branch: the pair channel cannot be closed by the floor F1 ≥ S2 for real marks, because at (1/4, 1/20) the floor
fails (kernel-checked), while for integer marks it holds (theorem). At that anchor (MI) HOLDS (F1 − T = +3.67 — a Python fact, not a
Lean statement; FIDELITY §2); Theorems 4.6–4.9 stay at paper grade; the three forbidden phrasings appear nowhere (`lint-10g.log`).
Stop lines (10(m)): none fired — (i) `sum_W2_mul` closed on the first build attempt in 34 lines (statement and proof); (ii) `prop45` for GENERAL n closed with no
hypothesis (the theorem 20 lines; the whole §4 with its eight helper lemmas and docstrings 153 lines, under the 250-line stop; the
n = 32 restatement was not needed); (iii) the certificate module builds in 1.8 s
(ten-minute line); (iv) the ℝ transfer of `Complex.exp_bound'` closed in 16 lines (`exp_sub_sum_le`, statement and proof); (v) no statement needed a
displayed hypothesis; (vi) the builder reached packaging at about one slot (the whole build from the errata to the comparator PASS took
11:09–11:42 IST of wall clock).

## 0. The attack on the pre-derivation (deliverable 1; `PREDERIVATION-ERRATA.md`, `tools/h4_numbers.py`, `tools/h4_numbers.log`)

Every derivation of the note's §2–§4 re-derived; every number recomputed (mpmath at 30 digits; exact integers and fractions for the power
sums and the certificate's rationals). Verdict: correct in substance; every anchor number reproduces — ā(1/4) = 1.10944370, ā(1/2) =
1.48140550, F1 − S2 = −0.0352002534 by the closed form AND by the direct integer-frequency row (identical to 13 digits; the mod-65-reduced
row gives −0.0144817, a different number — the reason the unit needed a new row); S₂ = 22880, S₄ = 14492192, S₆ = 10924353440,
S₈ = 8964042662432; the certified bound −0.033682 with L(3.141592) = 1.1060211, U(3.141593) = 1.4815182 (0.0015182 of the record's margin
spent); (MI) at the anchor: T = 60.3, F1 − T = +3.67, S2 − T = 3.705. Errata: **E7** — the note's dyadic bracket "3294198/2²⁰ < π" does
not follow from `pi_gt_d6` (3294198/2²⁰ = 3.1415920258 > 3.141592); unused by the unit, which applies the d6 decimals directly. **E5** —
the note's per-cosh error "0.021" at π/4 is the upper estimate x⁴/24·cosh x, the value is 0.0162 (harmless). **E9** — the Mathlib name for
flat-weight Cauchy–Schwarz, unverified by the note, is `sq_sum_le_card_mul_sum_sq` (`Mathlib/Algebra/Order/Chebyshev.lean` line 136;
root namespace; NOT reachable from `GridParseval`'s imports, so `PairRow.lean` imports that file). **E1/E10** — design routes (the
regrouping by one inner reindex + `sum_comm`; the certificate's sum bound term by term with one polynomial expansion). Everything else:
no error found (the expansion of Prop. 4.5 re-derived for every n; the error budget; the two generic bounds; the chain).

## 1. Files and statement decisions

| file | lines | content |
|---|---|---|
| `Zeta23/PairCeiling/PairRow.lean` | 477 | imports `GridParsevalRat`, `Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp`, `Mathlib.Algebra.Order.Chebyshev`; namespace `Zeta23.PairCeiling.PairRow`: §1 `W2`, `pairFormFactor`, `pairRow`, `abar`, `vacancyMark`; §2 `card_band`, `W2_eq`, `sum_W2_mul`; §3 `pairRow_eq_gridRowQ`, `sum_sinh_band`, `sum_W2_cosh`; §4 `intCast_zmod_eq_zero_iff`, `dftMarkQ_vacancy`, `W2_zero`, `abar_zero`, `sum_vacancyMark_sq`, `sum_W2_vacancy_sq`, `sum_W2_vacancy_cosh`, `sum_W2_cosh_sq`, `prop45`; §5 `one_le_abar`, `abar_sq_le`, `floor_holds_integer` |
| `Zeta23/PairCeiling/PairCert.lean` | 244 | imports `PairRow`, `Mathlib.Analysis.Real.Pi.Bounds`, `…Trigonometric.DerivHyp`; namespace `Zeta23.PairCeiling.PairCert`: `one_add_sq_half_le_cosh`, `exp_sub_sum_le`, `cosh_le_poly8`; `sum_pow2/4/6/8` (`decide +kernel`) and `_real` casts; `card_band32`, `sum_poly2`, `sum_poly8`, `abar32`, `abar_quarter_ge`, `abar_half_le`, `abar_quarter_ge_L`, `abar_half_le_U`, `cert_numeric`, `floor_fails_anchor` |
| `comparator/ChallengeDeps/PairChannel.lean` | 111 | trusted, `import Mathlib` only, namespace `PairChannel`: the seven IntegralityGap definitions and the five of PairRow.lean, character for character (`trust-greps.log`: 7/7, 5/5) |
| `comparator/Challenge/PairChannel.lean` | 94 | the eight statements (the probe's text byte for byte), every proof `sorry`; the WHAT IS CLAIMED / NOT paragraph (nothing about (MI), Theorems 4.6–4.9, laws, the LP, general positions, ζ) |
| `comparator/Solution/PairChannel.lean` | 70 | imports `ChallengeDeps.PairChannel` and `Zeta23.PairCeiling.PairCert`; the eight statements byte-identical, each a one-line delegation (definitional unfolding of the trusted vocabulary against the Zeta23 originals); never imports the challenge |
| `comparator/PrintAxioms/PairChannel.lean`, `comparator/config-pair-channel.json` | 27, — | the quick check; 8 names, `propext`/`Quot.sound`/`Classical.choice`, `enable_nanoda: true` |
| `lean/formalization.yaml` | — | `status.scope` sentence, a `main_results` entry, fidelity row (z), a `review.notes` paragraph, three `alignment.namespaces`, two `alignment.statements` rows; validator result in `yaml-validation.log` |
| `lean/README.md` | — | section "PairChannel (Session 33, 2026-09-29)" before "What these build against" |
| `results/a4-no-go/formalization-status.md` | — | dated addendum (Session 33); the earlier records untouched |

**Statement decisions, against UNIT-BRIEF §0–§1.** The eight statements are the probe's, byte for byte, binders included
(`statement-identity.log`, third section); the two generic cosh bounds are the brief's statements verbatim (`PairCert.lean`). The five
row definitions are the probe's with ONE deviation: the unused summation binder of `W2` is `_j` (the probe's `j` draws the linter's
"unused variable" warning; the term is the same; FIDELITY (z9)). `prop45` is stated for general n, as in the probe (the brief's n = 32
fallback was not needed). Helper lemmas were added on the program side only; none is a trusted definition. The trusted layer restates the
seven IntegralityGap definitions as the brief asks, three of them (`dftMark`, `gridRow`, `fracMark`) unused by the statements (FIDELITY
(z12)). The Solution delegates (no self-contained re-proof was needed; the Comparator's import discipline — the solution may import Zeta23 —
is the IV.17 one).

## 2. Builds (one `lake build` at a time; the clone's oleans reused throughout; every wall time from the logs)

* **Rung 1** (`rung1-print-axioms.log`): `lake build Zeta23.PairCeiling.PairRow` with §1–§3 only — first try 2 errors (an extra `ring`
  after `field_simp` had closed `W2_eq`; a no-op `beta_reduce`), second try *Built (1.6s), 2274 jobs, 0 errors, 0 warnings*; `#print
  axioms` on the six names: the three standard axioms. Then §4–§5 appended: two more rounds (a rewrite inside an `if` condition that
  the decidable instance blocks — replaced by a case split; `Finset.sum_div` is not a name at 51e6992e — the 1/2 folded out with
  `Finset.mul_sum`; two extra `ring`s), then *Built (1.9s), 2282 jobs, 0 errors, 0 warnings*.
* **The certificate** (`cert-build.log`, TIMED): `/usr/bin/time -l lake build Zeta23.PairCeiling.PairCert` — first try *Built (1.8s)* with
  one linter warning (`gcongr <;> linarith` on a single goal; written as two lines), the timed rebuild *Built (1.8s), Build completed
  successfully (2296 jobs)*, **2.72 s real for the lake call, max RSS 2.57 GB**; `lake env lean` of the file alone **2.38 s real**; the four
  `decide +kernel` power sums alone (scratch `tools/powersums-timing.lean`, profiler): **type checking 58 ms in total**. The note's
  estimate was 15–30 s; the ten-minute line (stop (iii)) is under by a factor of about 200.
* **The topic** (`build-comparator-topic.log`): `lake build Challenge.PairChannel Solution.PairChannel` — Built `ChallengeDeps.PairChannel`
  (18 s, the first load of Mathlib's oleans in that library; 5.2 s at the comparator run), `Challenge.PairChannel` (3.0 s) with exactly the
  8 deliberate `sorry` warnings, `Solution.PairChannel` (4.0 s) with 0 warnings — every delegation typechecked by definitional unfolding,
  no `show`/`change`/`convert`; *Build completed successfully (8704 jobs)*, 24.8 s wall, first try.

## 3. Checks

* `print-axioms.log`: `lake env lean comparator/PrintAxioms/PairChannel.lean` — 8 lines, each `[propext, Classical.choice, Quot.sound]`;
  `program-axioms.log` (probe `program-axioms.lean`): the 34 names of `PairRow` + `PairCert` — all three axioms, nothing else. No
  `sorryAx`, no `Lean.ofReduceBool`.
* `statement-identity.log`: `tools/statement_identity_h4.py` (the H5/D5 tool, docstring only changed) on the clone AND on the program
  tree — 8/8 IDENTICAL, RESULT PASS on both (the names passed one per word, bash array); a third section compares the challenge
  statements with the probe's by the same extraction — 8/8 IDENTICAL; a fourth checks the config's `theorem_names` order = the
  challenge's order — PASS.
* `trust-greps.log`: `tools/trust_greps_h4.py` (nine words, comments stripped) on the six topic files, both roots — exactly the 8
  deliberate challenge `sorry`s, nothing else (exit 1 is the tool's "hits present" code, as in every prior record); the raw grep with
  comments included, for the record (the words occur in header comments that say "no `native_decide`", "no `sorry`"); imports: the
  trusted layer `import Mathlib` only, the challenge imports the trusted layer only, the solution imports the trusted layer and
  `Zeta23.PairCeiling.PairCert`; tree = mirror by `cmp` for the six files + config; the 7 + 5 trusted definitions character for character
  against IntegralityGap and PairRow; the five definitions against the probe's — one difference, `W2`'s `_j`.
* `prerun-cleanup.log`: the three modules' 25 artifacts under `.lake/build/{ir,lib/lean}` removed so that comparator builds them itself
  (the program modules stay built — the untrusted side either way).
* **`comparator-run.log`: PASS** — 11:40:58–11:41:45 IST, `46.93 real`, max RSS 5.8 GB; runner `tools/run.sh` (the H5 runner, one comment
  line changed; comparator v4.33.0, lean4export v4.33.0-rc2, nanoda 0.4.17, the fake-landrun shim — NOT sandboxed, as in every prior macOS
  record; the four tool SHA-256s printed in the log equal COMPARATOR-RUN.md §1's); `Built ChallengeDeps.PairChannel (5.2s)`, `Built
  Challenge.PairChannel (3.0s)` with the 8 deliberate `sorry` warnings, `Built Solution.PairChannel (3.0s)`; the export of the 8 names from
  both modules; `Nanoda kernel accepts the solution`, `Lean default kernel accepts the solution`, `Your solution is okay!`,
  `--- comparator exit code: 0 ---`. What the run established: each solution statement coincides constant for constant with its challenge
  namesake (including the trusted `chi`, `dftMarkQ`, `zetaM`, `gridRowQ`, `W2`, `pairFormFactor`, `pairRow`, `abar`, `vacancyMark`); the
  proofs use no axiom outside the three; nanoda re-checked the whole solution export and Lean's kernel replayed it. No CONTROL run: the
  tool chain is unchanged since the Session 25 records and the Session 32 runs.
* `yaml-validation.log`, `lint-10g.log`, `hashes.txt`: see §6.

## 4. Fidelity (FIDELITY.md; yaml row (z))

Covered: the eight statements as theorems — the closed-form weight, the regrouping, the agreement lemma, (T1), Prop. 4.5 for every n,
depth and real mark, the log-convexity step, the integer-mark safety chain, and the floor's failure at the anchor (the record's sign,
kernel-checked). Not covered: (MI) at any anchor (it holds at this one — a Python fact); Theorems 4.6–4.9; laws and the LP; general
positions (pairs off the grid; general harmonics); Prop. 4.1's ledger; the VALUE −0.0352 (the statement is the strict inequality); ζ, RH.
Differs from the prose: pairs on grid sites (z1); the flat weights substituted in `W2` (z2); every n including 0 (z3); atom marks ℚ, pair
marks ℝ, chain marks ℕ ≥ 1 (z4); the character's sign (z5); the row's literal range (z6); the chain's intermediate step inside the proof
(z7); the certificate as a strict inequality with the d6 decimals (z8); `W2`'s binder (z9); the three axioms on the kernel facts (z10);
names (z11); three unused restated definitions (z12). Fidelity divergences in the brief's sense (a hypothesis beyond the statements'
own): NONE.

## 5. What an independent checker from a clean clone must do (`CHECK-O.md`; UNIT-BRIEF §3)

1. Clone `anthropics/zeta-23-lean` at tag `v1.0`, overlay `rh-program/lean/` as `lean/README.md` "Building" says; `lake exe cache get`;
   `lake build Zeta23.PairCeiling.PairRow`, then `Zeta23.PairCeiling.PairCert` (re-measure its time with `/usr/bin/time -l`), then
   `Solution.PairChannel` (expect ≈ 2282 / 2296 / 8704 jobs, 0 errors, 0 warnings outside the 8 deliberate challenge `sorry`s).
2. `lake env lean comparator/PrintAxioms/PairChannel.lean`: 8 lines, each `[propext, Classical.choice, Quot.sound]`; and
   `lake env lean results/h4-pair-lean-s33/program-axioms.lean` for the 34 program-side names.
3. `tools/statement_identity_h4.py <clone> PairChannel <the eight names>` (one name per word); the challenge against the probe;
   `tools/trust_greps_h4.py <clone> <the six topic files>` (expect exactly the 8 challenge `sorry`s); `diff` the 7 + 5 trusted definitions
   (FIDELITY §4).
4. The Comparator run with nanoda from the clean clone (`tools/run.sh` pattern with the clone's path; do NOT pre-build the comparator
   layer): `config-pair-channel.json`.
5. Read the eight challenge statements against UNIT-BRIEF §0 and against `pair-channel.md` / `paper.md` §2.3, §4.2, and against
   FIDELITY.md: is every "covered" claim a theorem in the file with exactly the stated content; is every "not covered" sentence true
   (re-derive each — in particular that (MI) holds at the anchor: T = 60.3, F1 = 63.9698); is any hypothesis present that the prose does
   not state; is the label exactly §1(3)'s; does any file, comment, yaml row or README line use a forbidden phrasing. Re-derive Prop. 4.5's
   expansion and the chain by hand; recompute ā(1/4), ā(1/2), the power sums, L, U and the certified bound independently (a scratch
   Python under `check-O/`); check PREDERIVATION-ERRATA E5, E7, E9 at the line.
6. Recompute every hash in `hashes.txt`; the yaml validation; the 10(g) lint.

## 6. Files written and SHA-256

`hashes.txt` (this directory) lists the SHA-256 of every file this job wrote or edited: the two Zeta23 modules, the four comparator files
and the config, `lean/formalization.yaml`, `lean/README.md`, `results/a4-no-go/formalization-status.md`, and every file under
`results/h4-pair-lean-s33/` (this file's own hash is in `SHARED.md`'s final block and in the chat report). Files under
`results/h4-pair-lean-s33/`: `PREDERIVATION-ERRATA.md`, `SHARED.md`, `BUILD-NOTES.md`, `FIDELITY.md`, `hashes.txt`, the probes
`rung1-axioms.lean`, `program-axioms.lean`, the logs `rung1-print-axioms.log`, `cert-build.log`, `build-comparator-topic.log`,
`program-axioms.log`, `print-axioms.log`, `statement-identity.log`, `trust-greps.log`, `prerun-cleanup.log`, `comparator-run.log`,
`yaml-validation.log`, `lint-10g.log`, and `tools/{run.sh, statement_identity_h4.py, trust_greps_h4.py, h4_numbers.py, h4_numbers.log,
powersums-timing.lean}`. 10(g) lint: U.S. English throughout; the four banned phrases absent (`lint-10g.log`).
