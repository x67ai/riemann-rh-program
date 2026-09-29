# H5 — the D5 F2 refinement in Lean: IV.1's prime-side containment into Zeta23's C² test class for continuous g — the Comparator pairs `WeilContainmentC2One` (rung 1, L = log 3) and `WeilContainmentC2` (every band), built over Mathlib alone — build notes (BUILDER, Fable 5.1; Session 32, 2026-09-29 06:22 – 06:47 IST)

Brief: `results/h5-c2-lean-s32/BRIEF.md` (SHA-256 `1a2e8a3acb4c6ba0623a9cf91ac515952490d49767717dd4b09af45f5c4e49ab`, recomputed at the start and again here).
Record: D5 `FIDELITY.md` (N2) as corrected 00:45 IST 2026-09-29 (CHECK-O F2); the reader's M4 and A7; the digest §D H5. Pattern: the D5 unit
(`results/d5-lean-s30/` BRIEF, BUILD-NOTES, FIDELITY, CHECK-O) and the packaging standard (`lean/README.md` "Packaging",
`results/d1-m2a/packaging/COMPARATOR-RUN.md`). Tree: the program's built clone `~/rh-lean-work/checker-clone-s21` (Lean `v4.33.0-rc2`,
commit d8b18978; Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`) — the only toolchain, as the brief prescribes (no Prove2Me mirror).
Mirror: `rh-program/lean/` is the source of truth; direction rh-program → clone by `cp`, `cmp`-identical for every topic file at the end
(`trust-greps.log`, RERUN section). The trusted layer is the D5 file `ChallengeDeps/WeilContainment.lean`, UNCHANGED (SHA-256
47c9a508… = the D5 `hashes.txt`); no new trusted definition was needed; the D5 Lean files were not touched. Not independently
checked yet: the Opus 5 clean-clone check (`CHECK-O.md`) is the next job. No commit by this job. Stage log with `date` stamps:
`results/h5-c2-lean-s32/SHARED.md`.

**Nothing about ζ or RH follows from anything below (10(c), first paragraph).** The two theorems are about prime-side VALUES: for every
continuous even band-limited g and every real a, the number `tiltedPrimeSide a g` is `primeSide k` for some even C² k on the same
band. The C² witness is an interpolant at ±log n, not the tilted test (which is in general not C¹ — [CORRECTION 07:02 IST 2026-09-29, Session 32 — CHECK-O F2 (Opus 5), re-derived by the orchestrator at `Challenge/WeilContainment.lean` line 117: `weilContainment_not_contDiff` proves ¬ContDiff ℝ 2 for the ONE instance a = 1, g ≡ 1 and nothing about C¹; for other g the tilted test can be smooth (g = 2e^{(a−1/2)|u|}·χ with χ a smooth even bump gives `weilTestOf a g = χ`). Read: the tilted test is not in general C², and is not claimed to be.] D5's `weilContainment_not_contDiff`
stands); the zero side of every explicit formula at every level is untouched; `EF_lit` is not stated and nothing is fed into it.

**Label, verbatim and binding (BRIEF §1(4), the reader's A7), earned — (1)–(3) landed with NO displayed hypothesis beyond the three:**
**"IV.1 formalized-in-Lean — prime-side containment into Zeta23's C² test class for continuous g (prime-side values; the C² witness is
an interpolant at ±log n, not the tilted test; zero side untouched)"** — never "IV.1's containment inside `EF_lit`", never anything
about ζ. The refutation-shaped close (10(c)) is the "Lands" branch: for every continuous even band-limited g and every real a, the
level-a tilted prime datum equals Zeta23's prime term at some C² even test on the same band — a kernel-checked theorem over Mathlib
alone; the D5 ledger's (N2) sentence is corrected from "NOT formalized" to formalized-for-continuous-g (the dated pointer is appended
to `results/d5-lean-s30/FIDELITY.md`, the only edit outside this folder and `lean/`).
Stop lines (10(m)): none fired — (i) `ContDiffBump` and the four lemmas the brief names are present at 51e6992e at the lines it gives
(70, 137, 157, 203; re-read); (ii) no statement needed a hypothesis beyond the three displayed (one displayed hypothesis is UNUSED —
§0 E2 — the opposite of a divergence); (iii) the build took a quarter of a slot (twenty-five minutes of wall clock; two lake builds of
the solutions, one retry); (iv) the pre-derivation is correct in substance (one gap at L = log 2, repaired inside the proof; §0).

## 0. The attack on the pre-derivation (deliverable 1; `PREDERIVATION-ERRATA.md`)

Every step (P1)–(P6) re-derived against the D5 definitions and Mathlib at 51e6992e. Verdict: correct in substance; the statement's
shape is unchanged. **E1 (gap):** the split "(P1) L < log 2 / (P2) otherwise" leaves L = log 2 in (P2) with an EMPTY interior set, where
(P3)'s "positive minimum over a finite nonempty set" is false; the conclusion is true there (k = 0) and the Lean proof splits on
I = ∅ instead. **E2 (unused hypothesis):** the evenness of g is never used — kept as displayed because the brief fixes the statement
(FIDELITY (D2)). **E3 (design):** one bump at 0 with rIn = log (max I), rOut = L, times Mathlib's Lagrange interpolant in u² replaces
the δ-separated family of bumps; still an interpolant at ±log n, so the label's clause is exact. **E4–E7 (checks, no error):** the
closed-set argument for "g = 0 on [L, ∞)"; distinctness of the points and the implicit δ < log 2; the rpow identity; the
`WithTop ℕ∞` smoothness index. Rung 1 (L = log 3: N = 3, I = {2}, n = 3 at the edge) checked. Stop line (iv) did not fire.

## 1. Files and statement decisions

| file | lines | content |
|---|---|---|
| `comparator/ChallengeDeps/WeilContainment.lean` | 63 | the D5 trusted layer, UNCHANGED (`primeSide`, `tiltedPrimeSide` are what the new statements mention) |
| `comparator/Challenge/WeilContainmentC2One.lean` | 46 | `weilContainment_c2_interpolant_log3`; `sorry`; header with the WHAT IS CLAIMED / what is NOT paragraph |
| `comparator/Challenge/WeilContainmentC2.lean` | 50 | `weilContainment_c2_interpolant`; `sorry`; the same paragraph for every band, with the band-edge counterexample named |
| `comparator/Solution/WeilContainmentC2One.lean` | 249 | Mathlib only; namespace `WeilContainmentC2One.Proof`: `contDiff_poly_eval`, `eq_zero_of_le`, `cutoff` (the D5 proof, re-proved), `interior`, `mem_interior`, `le_log_of_notMem`, `tilted_term_zero`, `tilted_eq_sum_interior`, `node`, `value`, `node_injOn`, `rpow_identity`, `interpolant` (every band L; no evenness hypothesis); the root theorem instantiates L = Real.log 3 |
| `comparator/Solution/WeilContainmentC2.lean` | 248 | its own copy of the same proof (namespace `WeilContainmentC2.Proof`), so that each topic is self-contained; the root theorem is the general statement |
| `comparator/PrintAxioms/WeilContainmentC2One.lean`, `PrintAxioms/WeilContainmentC2.lean` | 20, 20 | the quick checks |
| `comparator/config-weil-containment-c2-one.json`, `config-weil-containment-c2.json` | — | one name each; `propext`, `Quot.sound`, `Classical.choice`; `enable_nanoda: true` |
| `lean/formalization.yaml` | 1330 | a description paragraph, a `status.scope` sentence, a `main_results` entry, fidelity row (x), the dated FORMALIZED pointer inside row (u)'s (N2) sentence (the sentence kept), two `alignment.statements` rows; validator PASS (`yaml-validation.log`: errors 0, undeclared names 0) |
| `lean/README.md` | — | section "WeilContainmentC2 (Session 32, 2026-09-29)" before "IntegralityGap" |
| `results/d5-lean-s30/FIDELITY.md` | — | (N2): "[FORMALIZED 06:42 IST 2026-09-29, Session 32, for g continuous: …]" appended after "NOT formalized and NOT claimed." |

**Statement decisions, against BRIEF §0–§1.** Both statements are the brief's, character for character (§0 "The statement to ship" and
"Rung 1") [CORRECTION 07:02 IST 2026-09-29, Session 32 — CHECK-O F4: rung 1 writes `∃ k : ℝ → ℂ,` where the brief wrote `∃ k,`; same elaborated type (the checker's probe); the family statement is character for character], with the three displayed hypotheses `(∀ u, g (-u) = g u)`, `Continuous g`, `tsupport g ⊆ Set.Icc (-L) L` (rung 1:
`Set.Icc (-(Real.log 3)) (Real.log 3)`) and no fourth. Helper lemmas added inside the solution modules only (the list above); none is a
trusted definition. Not added: a variant without the evenness hypothesis (E2; footprint), a theorem tying `primeSide` to Zeta23 (not
needed, as in D5). The witness is E3's (FIDELITY (D1)), not the brief's δ-family; the statement is existential, so the choice is
invisible to the theorem. Each solution re-proves the D5 cutoff rather than importing `Solution.WeilContainment` (the brief's
"Mathlib + ChallengeDeps only").

## 2. Rung 1 (BRIEF §0, §1(2)) and the family (§1(3)): PASS

**Rung 1, topic `WeilContainmentC2One`.** `lake build Solution.WeilContainmentC2One`: first try 4 errors (an instance-path mismatch under
`simpa` in `contDiff_poly_eval`, written as `simp only` + `exact`; the explicit `r` argument of `Lagrange.eval_interpolate_at_node`;
`tsupport 0` versus `tsupport fun _ => 0` in the empty branch), second try *Build completed successfully (8698 jobs)*, 0 errors, 0
warnings. `rung1-print-axioms.log`: `[propext, Classical.choice, Quot.sound]`. `rung1-prerun-cleanup.log`: the topic's comparator-layer
artifacts and `ChallengeDeps.WeilContainment`'s removed so that comparator builds every comparator-layer module itself. **Comparator
(`rung1-comparator.log`): PASS** — 06:36 IST, `68.70 real`, the runner `tools/run.sh` (the D5 runner byte for byte but for its comment
line; comparator v4.33.0, lean4export v4.33.0-rc2, nanoda 0.4.17, the fake-landrun shim — NOT sandboxed, as in every prior macOS
record; the four tool SHA-256s printed in the log equal COMPARATOR-RUN.md §1's), `Built ChallengeDeps.WeilContainment (2.9s)`, `Built
Challenge.WeilContainmentC2One (2.9s)` with its one deliberate `sorry` warning (41:8), `Built Solution.WeilContainmentC2One (3.3s)`,
`Nanoda kernel accepts the solution`, `Lean default kernel accepts the solution`, `Your solution is okay!`, exit 0. The family was not
started until this run had passed.

**The family, topic `WeilContainmentC2`.** `lake build Solution.WeilContainmentC2`: *Build completed successfully (8698 jobs)*, 0 errors,
0 warnings, first try. `print-axioms.log`: `[propext, Classical.choice, Quot.sound]`. `statement-identity.log`: 1 + 1 IDENTICAL on the
tree AND on the mirror (`tools/statement_identity_h5.py` = the D5 tool, byte-copied). `trust-greps.log` (RERUN section — the first
section passed the seven file names as one argument, the zsh word-splitting slip D5 also logged; kept and superseded): the 2
deliberate challenge `sorry`s (C2One line 46, C2 line 50), nothing else; imports Mathlib / `ChallengeDeps.WeilContainment` /
`Solution.*` only; tree = mirror for the 7 topic files and 2 configs. `prerun-cleanup.log`: artifacts removed. **Comparator
(`comparator-run.log`): PASS** — 06:39 IST, `68.13 real`, max RSS 5.9 GB, `Built Challenge.WeilContainmentC2 (2.9s)` with its one
deliberate `sorry` warning (46:8), `Built Solution.WeilContainmentC2 (3.3s)`, `Nanoda kernel accepts the solution`, `Lean default
kernel accepts the solution`, `Your solution is okay!`, `--- comparator exit code: 0 ---`. What the runs established: each solution
statement coincides constant for constant with its challenge namesake (including the trusted `primeSide`, `tiltedPrimeSide`); the
proofs use no axiom outside the three; nanoda re-checked the whole solution export and Lean's kernel replayed it. No CONTROL run: the
tool chain is unchanged since the Session 25 records and both topic runs passed. Mathlib was never compiled from source (every build
8698 jobs with only the topic modules built).

## 3. Fidelity (FIDELITY.md; yaml row (x))

Covered: the prime-side number of every continuous even band-limited tilted datum is `primeSide` of a C² even function on the same
band, for every real a and L (`weilContainment_c2_interpolant`), and at L = log 3 (`weilContainment_c2_interpolant_log3`). Not covered:
the zero side at any level; the tilted test itself is not C² (D5 (N2) stands) [CORRECTION 07:02 IST 2026-09-29, Session 32 — CHECK-O F2 (Opus 5), re-derived by the orchestrator at `Challenge/WeilContainment.lean` line 117: `weilContainment_not_contDiff` proves ¬ContDiff ℝ 2 for the ONE instance a = 1, g ≡ 1 and nothing about C¹; for other g the tilted test can be smooth (g = 2e^{(a−1/2)|u|}·χ with χ a smooth even bump gives `weilTestOf a g = χ`). Read: the tilted test is not in general C², and is not claimed to be.]; `EF_lit` not stated, nothing fed into it; the
discontinuous case (D5 CHECK-O F2's band-edge counterexample stays a counterexample); the μ-band; the archimedean term;
summability as a datum; ζ, RH. Differs from the prose: the witness is one bump times a Lagrange interpolant (D1); the evenness of g is
displayed but unused (D2); `ContDiff ℝ 2` stated, C^∞ produced [CORRECTION 07:02 IST 2026-09-29, Session 32 — CHECK-O F3: the proof proves ContDiff ℝ 2 directly; nothing smoother is proved] (D3); every real L including the empty-interior bands (D4); `tsum` on
both sides (D5); the L = log 2 case handled by the empty-interior branch (D6). Fidelity divergences in the brief's sense (a hypothesis
beyond the three): NONE.

## 4. What an independent checker from a clean clone must do (`CHECK-O.md`; BRIEF §3)

1. Clone `anthropics/zeta-23-lean` at tag `v1.0`, overlay `rh-program/lean/` as `lean/README.md` "Building" says; `lake exe cache get`;
   `lake build Solution.WeilContainmentC2One`, then `Solution.WeilContainmentC2` (expect 8698 jobs each, 0 errors, 0 warnings).
2. `lake env lean comparator/PrintAxioms/WeilContainmentC2One.lean` and `…/WeilContainmentC2.lean`: one line each,
   `[propext, Classical.choice, Quot.sound]`; no `sorryAx`, no `Lean.ofReduceBool`.
3. `tools/statement_identity_h5.py <clone> WeilContainmentC2One weilContainment_c2_interpolant_log3` and
   `… WeilContainmentC2 weilContainment_c2_interpolant`; `tools/trust_greps_h5.py <clone> <the seven topic files>` (expect exactly the 2
   challenge `sorry`s); `ChallengeDeps/WeilContainment.lean` SHA-256 = 47c9a508… (the D5 record, unchanged).
4. The two Comparator runs with nanoda from the clean clone (`tools/run.sh` pattern with the clone's path; do NOT pre-build the
   comparator layer): `config-weil-containment-c2-one.json`, then `config-weil-containment-c2.json`.
5. Read the challenge statements against §0 and against FIDELITY.md: is every "covered" claim a theorem in the file; is every "not
   covered" sentence true (re-derive each, in particular (N2) — the witness is not the tilted test — and (N4) — the band-edge
   counterexample); is any hypothesis present that the prose does not state (the three, and only the three); is the label exactly A7's;
   does anything in the files say more than "prime-side values". Read PREDERIVATION-ERRATA E1–E7 and say whether each is right (E1: is
   the interior set empty at L = log 2; E2: is evenness of g really unused — grep the solution for the hypothesis).
6. Recompute every hash in `hashes.txt`; the yaml validation; the 10(g) lint.

## 5. Files written and SHA-256

`hashes.txt` (this directory) lists the SHA-256 of every file touched: the 8 topic files under `lean/comparator/` (the unchanged
trusted file included), `lean/formalization.yaml`, `lean/README.md`, `results/d5-lean-s30/FIDELITY.md`, and every file under
`results/h5-c2-lean-s32/` (this file's own hash is in `SHARED.md`'s final block and in the chat report). Files under
`results/h5-c2-lean-s32/`: `PREDERIVATION-ERRATA.md`, `SHARED.md`, `BUILD-NOTES.md`, `FIDELITY.md`, `hashes.txt`, the logs
`rung1-print-axioms.log`, `rung1-prerun-cleanup.log`, `rung1-comparator.log`, `print-axioms.log`, `statement-identity.log`,
`trust-greps.log`, `prerun-cleanup.log`, `comparator-run.log`, `yaml-validation.log`, `lint-10g.log`, and `tools/{run.sh,
statement_identity_h5.py, trust_greps_h5.py}`. 10(g) lint: U.S. English throughout; no "clearly / obviously / easy to see / well known"
(`lint-10g.log`).
