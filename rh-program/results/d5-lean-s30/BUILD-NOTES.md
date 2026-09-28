# D5 (F3, G4) — the C1 containment theorem (barrier-zoo IV.1) in Lean over Mathlib alone: the Comparator pairs `WeilContainmentOne` (rung 1) and `WeilContainment`, built at BOTH toolchains — build notes (BUILDER, Fable 5.1; Session 30, 2026-09-28 23:49 – 2026-09-29 00:21 IST)

Brief: `results/d5-lean-s30/BRIEF.md` (SHA-256 `22e8656f36d04aeecbc908d46f45285f83c2b667fd092f8f7c13f8eb5f846fae`, recomputed at the start).
Record: zoo IV.1 STATEMENT; `results/adjudication-C1.json` fatal 2 and its mandatory repair; C1's MASTER FORMULA prime side
(`directions/C1-requirements-first-field.md`); the classical vocabulary of `Zeta23/ExplicitFormula.lean` (`literatureRHS`, `prime_term`).
Pattern: the Lemma G / SeparationG1 unit (`results/c2-m4/BRIEF-iii.md`, `BUILD-NOTES-iii.md`, `CHECK-O-iii.md`) and the packaging
standard (`lean/README.md` "Packaging", `results/d1-m2a/packaging/COMPARATOR-RUN.md`). Trees: the program's built clone
`~/rh-lean-work/checker-clone-s21` (Lean `v4.33.0-rc2`, Mathlib `51e6992e`) and the Prove2Me workspace `~/prove2me_workspace`
(Lean `v4.33.1`, Mathlib `0df444a360eaa60ab8c11dca51a86af692955474`). Mirror `rh-program/lean/` is the source of truth; direction
rh-program → clone by `cp`, `cmp`-identical for every file at the end of each stage (logged in `rung0-program-tree.log`,
`trust-greps.log`). Not independently checked yet: the Opus 5 clean-clone check (`CHECK-O.md`) is the next job. No commit by this job
(the watchdogs and the orchestrator commit). **Nothing was posted to Prove2Me** — no mission, no proposal, no API call; the key file
`~/Downloads/assets/prove2me.md` was not read. Stage log with `date` stamps: `results/d5-lean-s30/SHARED.md`.

**Label, verbatim and binding (BRIEF §1(4)), earned — every clause (0)–(3) landed with NO displayed hypothesis:**
**"IV.1 formalized-in-Lean (prime-side containment; Comparator-checked over Mathlib alone, no displayed hypothesis, axioms
propext/Classical.choice/Quot.sound, replayed by nanoda; built at v4.33.0-rc2/51e6992e and v4.33.1/0df444a)"** — never "the tilted
explicit formula is formalized", never "kernel-checked on Prove2Me". The refutation-shaped close (10(c)) is the "Lands" branch: IV.1's
containment is a kernel-checked theorem over Mathlib alone — the level-a tilted prime data and the classical band-L Weil prime data
are the same set of numbers, for every real a, through multipliers bounded by e^{±|a−1/2|L}. **Nothing about ζ or RH follows;**
nothing about the ZERO side of any explicit formula at any level (fatal 1's cosh ghost is untouched); nothing about the μ-band.
Stop lines (10(m)): none fired — (i) rung 0 built Mathlib-only at v4.33.1/0df444a on the first try; (ii) no statement needed a
hypothesis the prose does not state (one REDUNDANT hypothesis of the brief was dropped, see §2); (iii) the plumbing took well under
one slot; (iv) the pre-derivation is correct at (T1).

## 0. The attack on the pre-derivation (deliverable 1; `PREDERIVATION-ERRATA.md`)

Every step of BRIEF §0's single-model pre-derivation re-derived by hand against the definitions of §1(1) and Mathlib's conventions.
(T1) correct — term by term, n = 0 by Λ(0) = 0, n ≥ 1 by `tilt a (log n) = n^(1/2 − a)` and `(Λ/√n)·n^(1/2−a) = Λ·n^(−a)`; the
`tsum` identity needs no summability (`tsum_congr`). (T2) correct. (T3) correct. Six items: **E1** evenness of `weilTestOf a g` is
needed for the "same set of numbers" sentence and was missing from the theorem list — added `weilContainment_even` and the sentence
itself, `weilContainment_range_eq`; **E5** the "n ≤ X cutoff is automatic" remark is a theorem — added `weilContainment_cutoff`;
**E6** the support inclusion is an equality — added `weilContainment_tsupport_eq`; **E4** `0 ≤ L` in `tilt_bounds` is implied by
|u| ≤ L — dropped; **E2** "k_{a,g} is not C² at 0 for a ≠ 1/2" is false as a universal statement (g vanishing to order ≥ 3 at 0) and
the true statement is sharper (for g(0) ≠ 0 the test is not even C¹ at 0 [CORRECTION 00:45 IST 2026-09-29, Session 30 — CHECK-O F1 (Opus 5), re-derived by the orchestrator: this presupposes g differentiable at 0; for C1's family (windows w ≥ 0, w ≢ 0, at every a > 1/2) k_{a,g} is not differentiable at 0 (g ≤ g(0) = ∫w > 0); without differentiability of g the claim fails (g = 2e^{(a−1/2)|u|} gives k ≡ 1, `check-O/probe_E2_counterexample.lean`), and at a < 1/2 it fails for the Fejér window at a = 1/2 − 1/L. The theorem `weilContainment_not_contDiff` is unaffected.]; C1's windows have g(0) = ∫w > 0) — the ledger uses the
sharp form, and the witness `weilContainment_not_contDiff` was added to the topic (§3); **E3** the cos-transform of w is even for
every w, no hypothesis on w needed. Stop line (iv) did not fire.

## 1. Rung 0 — the toolchain gap (BRIEF §1(0)): PASS in both environments

* Program tree (`rung0-program-tree.log`, two sections): Lean 4.33.0-rc2 (d8b18978), Mathlib 51e6992e; `lake build
  Challenge.WeilContainmentOne Challenge.WeilContainment` — *Build completed successfully (8699 jobs)*, `Built
  ChallengeDeps.WeilContainment (25s)` (first load of Mathlib's oleans; 2.8 s on every later build), 0 errors, exactly the
  deliberate `sorry` warnings (1 + 11; second section, after §3's addition, 1 + 12), 35 s wall.
* Prove2Me environment (`rung0-prove2me-env.log`, three sections — two false starts kept in the log: `lake build Definitions Theorems`
  fails with "bad imports" because the workspace's `lean_lib`s have no root module (its own smoke test is built by module name too),
  and a zsh word-splitting slip "unknown target"): Lean 4.33.1 (819816b2), Mathlib 0df444a; the 13 modules built by name —
  *Build completed successfully (8718 jobs)*, 0 errors, the 12 deliberate `sorry` warnings (13 after §3). The Mathlib cache had been
  fetched by the orchestrator's `setup-s30.sh` ("== smoke exit 0"); no Mathlib module compiled from source at any point.
* Decision (a), Mathlib-only, held: every object is `Real.exp`, `abs`, `Real.rpow`, `Real.sqrt`, `Real.log`, `ArithmeticFunction.vonMangoldt`,
  `tsum`, `tsupport`, `Set.Icc`, `Finset.range`, `Nat.floor`, `ContDiff`; no import missing at either Mathlib.

## 2. Files and statement decisions

| file | lines | content |
|---|---|---|
| `comparator/ChallengeDeps/WeilContainment.lean` | 63 | trusted, `import Mathlib` only, namespace `WeilContainment`: `tilt a u := Real.exp (-(a - 1/2) * |u|)`; `weilTestOf a g u := (1/2 : ℂ) * g u * (tilt a u : ℂ)`; `primeSide k := ∑' n : ℕ, ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) * (k (Real.log n) + k (-Real.log n))` — Zeta23's `literatureRHS` prime term character for character (`Zeta23/ExplicitFormula.lean`, the `- ∑' n : ℕ, …` lines; the sign is the formula's, not the term's); `tiltedPrimeSide a g := ∑' n : ℕ, ((ArithmeticFunction.vonMangoldt n : ℝ) : ℂ) * (((n : ℝ) ^ (-a) : ℝ) : ℂ) * g (Real.log n)` |
| `comparator/Challenge/WeilContainmentOne.lean` | 38 | `weilContainment_identity_one : ∀ g : ℝ → ℂ, (∀ u, g (-u) = g u) → tiltedPrimeSide 1 g = primeSide (weilTestOf 1 g)`; `sorry` |
| `comparator/Challenge/WeilContainment.lean` | 118 | twelve statements, every proof `sorry` (names and content: FIDELITY.md §1) |
| `comparator/Solution/WeilContainmentOne.lean` | 69 | Mathlib only; namespace `WeilContainmentOne.Proof`: `tilt_even`, `tilt_of_nonneg`, `summand_eq` (every n), `identity` (every real a); the root theorem instantiates a = 1 |
| `comparator/Solution/WeilContainment.lean` | 233 | Mathlib only; namespace `WeilContainment.Proof` (its own copy of the (T1) computation, so each topic is self-contained): `tilt_even`, `tilt_pos`, `tilt_of_nonneg`, `tilt_mul_tilt`, `summand_eq`, `identity`, `support_weilTestOf`, `tsupport_weilTestOf`, `weilTestOf_even`, `exact`; the twelve root theorems |
| `comparator/PrintAxioms/WeilContainmentOne.lean`, `PrintAxioms/WeilContainment.lean` | 20, 31 | the quick checks |
| `comparator/config-weil-containment-one.json`, `config-weil-containment.json` | — | 1 and 12 names; `propext`, `Quot.sound`, `Classical.choice`; `enable_nanoda: true` |
| `lean/formalization.yaml` | 1197 | project name and description paragraph, `status.scope`, a `main_results` entry, `automation.tool_setup` (the second toolchain), fidelity row (u), a `review.notes` paragraph, `alignment.namespaces` + two statements rows; schema validation PASS (`yaml-validation.log`, 0 errors, 0 undeclared names) |
| `lean/README.md` | 490 | section "WeilContainment (Session 30)" before "What these build against" |

**Statement decisions, against BRIEF §1(1)–(2)'s list.** Kept verbatim: `weilContainment_identity`, `weilContainment_tilt_pos`,
`weilContainment_tsupport`, `weilContainment_continuous`, `weilContainment_tilt_inv`, `weilContainment_exact`, `weilContainment_identity_one`,
the topic and config names, the trusted definitions (with `Even g` spelled `∀ u, g (-u) = g u` as the brief asks). Changed:
`weilContainment_tilt_bounds` loses the redundant `0 ≤ L` (E4; a strictly stronger statement of the same content). Added (E1, E5, E6, and
§3): `weilContainment_even`, `weilContainment_tsupport_eq`, `weilContainment_cutoff`, `weilContainment_range_eq`, `weilContainment_not_contDiff`.
Not added: a theorem tying `primeSide` to `Zeta23.literatureRHS` (none is needed — the containment is between two Mathlib-defined
functionals; the character-for-character claim is the checker's `diff` item, FIDELITY (D3)); the C² refinement by finite interpolation [CORRECTION 00:45 IST 2026-09-29, Session 30 — CHECK-O F2 (Opus 5), re-derived by the orchestrator: true for g continuous (every cos-transform of a window), false at a band edge otherwise — L = log 2, g the indicator of {±log 2}: tiltedPrimeSide = 2^{−a} log 2 while every continuous k′ with tsupport ⊆ [−log 2, log 2] has primeSide k′ = 0. Not claimed anywhere in Lean.]
(FIDELITY (N2), not attempted). The `Solution` modules import no Zeta23 module (the brief allowed it with a record; none was needed).
Prove2Me naming: the mirror names each theorem `WeilContainment.<suffix>` so that the platform's module slug
(`Thm_<theorem_name with dots as underscores>`) is `Thm_WeilContainment_<suffix>`, as the brief's file names ask; the statement TEXT is
byte-identical to the challenge in the stub and in the `Sol_` file (checked, `prove2me-print-axioms.log`).

## 3. Rung 1 (BRIEF §1(2)) and the family (§1(3)): PASS

**Rung 1, topic `WeilContainmentOne`.** `lake build Solution.WeilContainmentOne`: *Build completed successfully (8698 jobs)*, 0 errors,
0 warnings, first try. `rung1-print-axioms.log`: `[propext, Classical.choice, Quot.sound]`. `rung1-prerun-cleanup.log`: the topic's
comparator-layer artifacts removed. **Comparator (`rung1-comparator.log`): PASS** — 00:03:11–00:03:47 IST, `30.55 real`, the runner
`tools/run.sh` (the verify-iii runner with the s21 clone path; comparator v4.33.0, lean4export v4.33.0-rc2, nanoda 0.4.17, the
fake-landrun shim — NOT sandboxed, as in every prior record; the four tool SHA-256s printed in the log and equal to COMPARATOR-RUN.md §1's),
`Built ChallengeDeps.WeilContainment (2.8s)`, `Built Challenge.WeilContainmentOne (2.8s)` with its one deliberate `sorry` warning (36:8),
`Built Solution.WeilContainmentOne (2.0s)`, `Nanoda kernel accepts the solution`, `Lean default kernel accepts the solution`,
`Your solution is okay!`, exit 0. The family was not started until this run had passed.

**The family, topic `WeilContainment`.** First build of the solution: two errors — the absolute-value parse ambiguity `|-(a - 1/2) * |u||`
(written `abs (…)`) and `Set.mem_setOf_eq` deprecated at 51e6992e (dropped; membership in `setOf` unfolds definitionally, and the name
might not exist at 0df444a) — then *Build completed successfully (8698 jobs)*, 0 errors, 0 warnings. Checks on eleven statements
(first sections of the logs), then the twelfth added: `weilContainment_not_contDiff : ¬ ContDiff ℝ 2 (weilTestOf 1 (fun _ => (1 : ℂ)))`
— the ledger's "the C² test class is not preserved by the tilt" made a theorem (proof: if C² then differentiable at 0; the real part is
(1/2)e^{−|u|/2}; `−2·log` of twice it is |u|; `not_differentiableAt_abs_zero`) — and every check re-run on twelve (second sections):
`print-axioms.log` 12 × `[propext, Classical.choice, Quot.sound]`; `statement-identity.log` 1 + 12 IDENTICAL on the tree AND on the
mirror (an earlier zsh word-splitting slip is recorded and superseded in the log); `trust-greps.log` (nine words, comments stripped,
seven files, tree and mirror): the 13 deliberate challenge `sorry`s, nothing else; imports Mathlib / `ChallengeDeps.WeilContainment` /
`Solution.*` only; tree = mirror for the 9 topic files. **Comparator (`comparator-run.log`, SECOND RUN): PASS** — 00:12 IST,
`42.59 real`, max RSS 5.9 GB, `Built Challenge.WeilContainment (2.9s)` with the 12 deliberate `sorry` warnings, `Built
Solution.WeilContainment (3.1s)`, `Nanoda kernel accepts the solution`, `Lean default kernel accepts the solution`, `Your solution is
okay!`, `--- comparator exit code: 0 ---` (the first run, on eleven, passed the same way at 00:06). What the runs established: each
solution statement coincides constant for constant with its challenge namesake (including the trusted `tilt`, `weilTestOf`, `primeSide`,
`tiltedPrimeSide`); the proofs use no axiom outside the three; nanoda re-checked the whole solution export and Lean's kernel replayed it.
No CONTROL run this session: the tool chain is unchanged since the Session 25 records and the two topic runs passed.

**The Prove2Me-layout mirror at v4.33.1 / 0df444a** (`prove2me-build.log`, `prove2me-print-axioms.log`): `Definitions/Def_WeilContainment.lean`
(the vocabulary verbatim, comparator headers stripped), 13 `Theorems/Thm_WeilContainment_<suffix>.lean` stubs ending `by sorry`,
13 `Solutions/Sol_WeilContainment_<suffix>.lean` — each self-contained (imports `Definitions.Def_WeilContainment` and Mathlib only;
never its own `Thm_` stub and no other stub, so no `sorry` is in any solution's dependency closure), helper lemmas as `private theorem`s,
top-level `theorem solution`, statement text byte-identical to the challenge — generated by `tools/gen_prove2me_layout.py` and
`tools/gen_prove2me_solutions.py` (re-runnable by the checker). `lake build` of the 27 modules by name: *Build completed successfully
(8732 jobs)*, 0 errors, 0 warnings from the solutions; `#print axioms solution` ×13 = the three standard axioms; the platform's three
gating rules checked by grep (rule 1: one top-level `theorem solution` per file, no `namespace`; rule 2: no `Theorems.` import; rule 3: no
`sorry`); stub = solution = challenge statement text, 13 × IDENTICAL. **Nothing uploaded.**

## 4. Fidelity (FIDELITY.md; yaml row (u))

Covered: the prime-side containment of the whole (a, g)-family for every real a (`identity`, `cutoff`), the multiplier bounds with the
explicit constants (`tilt_bounds`, `tilt_pos`), the same band (`tsupport_eq`), evenness and continuity of the classical test, the
level-(1−a) inverse (`tilt_inv`), the converse containment (`exact`), the exact two-way containment as a set equality (`range_eq`), and the
C² non-preservation witness (`not_contDiff`). Not covered: the zero side at any level; Zeta23's C² class (the classical class here is
"even, band-limited, no regularity"; the C² refinement by finite interpolation [CORRECTION 00:45 IST 2026-09-29, Session 30 — CHECK-O F2 (Opus 5), re-derived by the orchestrator: true for g continuous (every cos-transform of a window), false at a band edge otherwise — L = log 2, g the indicator of {±log 2}: tiltedPrimeSide = 2^{−a} log 2 while every continuous k′ with tsupport ⊆ [−log 2, log 2] has primeSide k′ = 0. Not claimed anywhere in Lean.] is not formalized); the μ-band and nonlinear functions of the
band; the archimedean term; summability as a datum; ζ. Differs from the prose: `tsum` over all n for "n ≤ X" (equal by `cutoff`), the
algebraic inverse for "analytic continuation", the restated prime term, an arbitrary even g for the cos-transform of a window (a larger
family — stronger), every real a for a > 1/2, the redundant `0 ≤ L` dropped, the Prove2Me theorem names.

## 5. What an independent checker from a clean clone must do (`CHECK-O.md`; BRIEF §3)

1. Clone `anthropics/zeta-23-lean` at tag `v1.0`, overlay `rh-program/lean/` as `lean/README.md` "Building" says; `lake exe cache get`;
   `lake build Solution.WeilContainmentOne Solution.WeilContainment` (expect 8698 / 8699 jobs, 0 errors, 0 warnings from the solutions).
2. `lake env lean comparator/PrintAxioms/WeilContainmentOne.lean` and `…/WeilContainment.lean`: 1 + 12 lines, each
   `[propext, Classical.choice, Quot.sound]`; no `sorryAx`, no `Lean.ofReduceBool`.
3. `tools/statement_identity_d5.py <clone> WeilContainmentOne weilContainment_identity_one` and `… WeilContainment <the twelve names>`;
   `tools/trust_greps_d5.py <clone> <the seven topic files>` (expect exactly the 13 challenge `sorry`s).
4. The character-for-character claim: `primeSide`'s summand versus `Zeta23/ExplicitFormula.lean` `literatureRHS`'s prime term (a `diff` of
   the two lines, modulo the leading minus sign and line break); the trusted definitions against BRIEF §1(1).
5. The two Comparator runs with nanoda from the clean clone (`tools/run.sh` pattern with the clone's path; do NOT pre-build the
   comparator layer): `config-weil-containment-one.json`, then `config-weil-containment.json`.
6. A SECOND fresh checkout of `~/prove2me_workspace` pinned to v4.33.1 / 0df444a (`lake update`, `lake exe cache get`); re-generate the
   layout with the two generators from `rh-program/lean/comparator`; `lake build` the 27 modules by name; `#print axioms solution` per file;
   the three platform rules.
7. Read the challenge statements against the record (§0 of the brief, IV.1 STATEMENT, fatal 2, the MASTER FORMULA) and against
   FIDELITY.md: is every "covered" claim a theorem in the file, is every "not covered" fact true, is any hypothesis present that the prose
   does not state? Re-derive (T1) on paper. Read PREDERIVATION-ERRATA.md E1–E6 and say whether each is right.
8. Recompute every hash in `hashes.txt`; the yaml schema validation; the 10(g) lint.

## 6. Files written and SHA-256

`hashes.txt` (this directory) lists the SHA-256 of every file touched: the 9 topic files under `lean/comparator/`, `lean/formalization.yaml`,
`lean/README.md`, the 27 Prove2Me-layout files, and every file under `results/d5-lean-s30/` (this file's own hash is in `SHARED.md`'s final
block and in the chat report). Files under `results/d5-lean-s30/`: `PREDERIVATION-ERRATA.md`, `SHARED.md`, `BUILD-NOTES.md`, `FIDELITY.md`,
`hashes.txt`, the logs `rung0-program-tree.log`, `rung0-prove2me-env.log`, `rung1-print-axioms.log`, `rung1-prerun-cleanup.log`,
`rung1-comparator.log`, `print-axioms.log`, `statement-identity.log`, `trust-greps.log`, `prerun-cleanup.log`, `comparator-run.log`,
`prove2me-build.log`, `prove2me-print-axioms.log`, `yaml-validation.log`, `lint-10g.log`, and `tools/{run.sh, statement_identity_d5.py,
trust_greps_d5.py, gen_prove2me_layout.py, gen_prove2me_solutions.py}`. 10(g) lint: U.S. English throughout; no "clearly / obviously /
easy to see / well known" (`lint-10g.log`).
