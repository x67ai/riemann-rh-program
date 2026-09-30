# THEOREM R's ARITHMETIC CORE in Lean: the Comparator topic `ResidueRank` — build notes (BUILDER, Opus 5.5; Session 36, 2026-09-30 17:19 – 17:50 IST)

Brief: `results/theoremR-lean-s36/UNIT-BRIEF.md` (SHA-256 `60b131b3353f944b101bca54609cd07f591fad4c20618fab5387b6a03d42068e`, computed at the start);
typing probe `typing-probe.lean` there (SHA-256 `881e024a9184e9e4aab0976e42a31f1d8f8f5f01b3cec10c773a00f236601a81`). Record: `results/beta-shapes-s35/NOTE.md`
§1.1, §2.0 (Lemma F), §2.3 (H3.3(b), Theorem R, the converse paragraph, T3); `read-O.md` §2.5. Pattern: the H4 unit (`results/h4-pair-lean-s33/`)
for the packaging, the tools and the logs; `results/d1-m2a/packaging/COMPARATOR-RUN.md` for the run. Tree: `~/rh-lean-work/checker-clone-s33-h4`
(the H4 checker's clean clone of `anthropics/zeta-23-lean` v1.0; Lean `v4.33.0-rc2`, commit d8b18978; Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`),
used as the build tree as the brief allows; only new files were added to it (`Zeta23/ResidueRank/`, `comparator/*/ResidueRank.lean`,
`comparator/config-residue-rank.json`), nothing of the H4 record there was edited. `rh-program/lean/` is the source of truth, mirror by `cp`,
`cmp`-identical for the six Lean files and the config (`trust-greps.log`, last section). One `lake` process at a time; Mathlib never compiled from
source (every build reused the tree's oleans; 8697–8701 jobs, only the new modules built). No commit by this job. No Lean file was edited after
the comparator run. Not independently checked yet: the clean-clone CHECKER (`CHECK-O.md`, UNIT-BRIEF §3) is the next job. Stage log with
`date` stamps: `SHARED.md`.

**Nothing about ζ's zeros or RH follows from anything below (10(c)).** Theorem R is RH-blind (NOTE §2.3 DH CHECK). The statements are about
logarithms of integers, von Mangoldt's function, ℚ-spans in ℝ, a map into a monoid, and real inequalities.

**Label, verbatim and binding (UNIT-BRIEF §1(3)), earned — every statement landed with no displayed hypothesis beyond its own binders, so the
"only if everything lands" clause holds:** **"Theorem R's arithmetic core Comparator-checked: the logarithms of the primes are ℚ-linearly
independent, a family of positive integers N_p with p | N_p has logarithms spanning an infinite-dimensional ℚ-space, the converse rank bound,
Lemma F, and Theorem R on the abstract pair (von Mangoldt weights, real fiber sums, one κ) — over Mathlib alone, no displayed hypothesis, the
three standard axioms, replayed by nanoda".** The refutation-shaped close (10(c)) is the "Lands" branch, in the brief's words: "the finite-rank
target kill's arithmetic is kernel-checked: a target whose diagonal-row values are κ⁻¹·log of integers N_p with p | N_p cannot have a
finite-dimensional ℚ-span, because the logarithms of the primes are ℚ-independent and there are infinitely many primes". Items 7–8 are in the
topic and are not named by the label (UNIT-BRIEF §0: SCOPED). The forbidden phrasings of §1(3) appear in no file of this unit (`lint-10g.log`).

Stop lines (10(m)): none fired — (i) no statement of the brief is false or differs from what the NOTE proves (PREDERIVATION-ERRATA §1; one
erratum, E1, is against a SKETCH, not a statement); (ii) item 1 closed in 54 lines with its two valuation helpers (lines 104–157 of the shipped `LogPrimes.lean`, 103–156 of the rung-1 file; no Mathlib lemma exists at the pin, the grep is recorded); (iii) no statement needed a displayed hypothesis; (iv) item 7's
algebra closed in 62 lines, statement included, at the first elaboration; (v) packaging reached at about 400k tokens, under the ≈ 600k line (the
comparator PASS at 17:37:55 IST).

## 0. The attack on the brief (deliverable 1; `PREDERIVATION-ERRATA.md`, `tools/errata_numbers.py`, `tools/errata_numbers.log`)

All eight statements true and faithful; the abstractions of the pair (an arbitrary class map, an arbitrary real diagonal row, A5 built in, A9 as
a `HasSum` with one κ) add no hypothesis. **E1** (the one error, in a sketch): "for κ ≤ 0 the hypothesis is contradictory at n = 2" holds for
κ = 0 only; for κ < 0 the hypotheses are satisfiable (cls = id, v = Λ/κ) and the theorem still holds; Theorem R's proof uses no hypothesis on κ.
Removable displayed hypotheses, kept verbatim: item 3's positivity (E4), item 4's `2 ≤ n` (E2 — the brief's question answered: not needed), item
5's `1 ≤ a` (E3), item 6's `κ > 0` (E1), item 8's `0 ≤ g` (E5) — each removal is a program-side Lean theorem (errata §4). Necessary (hand
counterexamples): item 2's `hpos` (N ≡ 0: Real.log 0 = 0) and `hdvd` (N ≡ 1), item 7's `hg` (g = −1, x = L = 1), item 8's `hκ` (κ = 0: Lean's
x / 0 = 0, d ≡ 1, g = 1). Item 7 re-derived step by step, g = 0 and x < 0 included (x < 0 is infeasible); its bound is ATTAINED at x = r²,
L = 1 + r² + 2gr (E7, exact by sympy). E8: the hint names checked at the pin (`vonMangoldt_apply` etc. exist; `HasSum` carries a `SummationFilter`;
`Infinite.exists_notMem_finset`). E9: no ChallengeDeps module. E10: the unused-variable linter fires at the pin on unused theorem hypotheses.

## 1. Files and statement decisions

| file | lines | content |
|---|---|---|
| `Zeta23/ResidueRank/LogPrimes.lean` | 246 | `import Mathlib`; namespace `Zeta23.ResidueRank`: `logP`, `expVec` (+ `_apply`, `_one`, `_mul`, `_prime`), `linearCombination_expVec_prime`, `linearCombination_expVec`, `log_mem_span_logP`, `padicValRat_finset_prod`, `padicValRat_prime`, `linearIndependent_logP`, **`log_primes_linearIndependent`**, **`span_log_not_finite`**, `rank_span_log_le_of_supp`, **`rank_span_log_le`** |
| `Zeta23/ResidueRank/Pair.lean` | 221 | `import Zeta23.ResidueRank.LogPrimes`: `log_two_le_vonMangoldt`, **`lemmaF_finite_fiber`**, `fiber_sum_eq_log`, **`lemmaF_infinite_order`**, `theoremR_of_A9`, **`theoremR`**, `lemmaF_finite_fiber_all`, `lemmaF_infinite_order_all` |
| `Zeta23/ResidueRank/GenusBound.lean` | 132 | `import Mathlib`: **`theoremS_bound`**, **`theoremS`**, `theoremS_abs` |
| `comparator/Challenge/ResidueRank.lean` | 116 | header with the WHAT IS CLAIMED / NOT paragraph; from `import Mathlib` to the end the typing probe character for character (the eight statements, namespace `ResidueRank`, each `:= by sorry`) |
| `comparator/Solution/ResidueRank.lean` | 93 | imports `Zeta23.ResidueRank.Pair` and `Zeta23.ResidueRank.GenusBound`; the eight statements byte-identical, each proof the program theorem of the same name applied to the same arguments; never imports the challenge |
| `comparator/PrintAxioms/ResidueRank.lean`, `comparator/config-residue-rank.json` | 27, — | the quick check; the 8 names `ResidueRank.*` in the challenge's order, `propext`/`Quot.sound`/`Classical.choice`, `enable_nanoda: true` |
| `lean/formalization.yaml` | — | a `status.scope` sentence, a `main_results` entry, `automation.methods[0].models` + "Claude Opus 5.5", fidelity row (aa), a `review.notes` paragraph, two `alignment.namespaces`, three `alignment.statements` rows; validator result in `yaml-validation.log` |
| `lean/README.md` | — | section "ResidueRank (Session 36, 2026-09-30)" before "What these build against" |

**Statement decisions, against UNIT-BRIEF §0–§1.** The eight statements are the probe's, byte for byte, binders and docstrings included
(`statement-identity.log` [B], [D]). **No ChallengeDeps module** (errata E9): the comparator needs a challenge module and a solution module; the
statements use Mathlib's vocabulary only, and the probe imports Mathlib, so the challenge does too. **No root import in `lean/Zeta23.lean`**: the
precedent adds none for its program modules (H4's `PairRow`/`PairCert` are not in it), and that root imports modules absent from the build tree,
so a `lake build Zeta23` there would fail for reasons unrelated to this unit. The program theorems carry the probe's binders except that the
two unused displayed hypotheses are named `_hpos` (`rank_span_log_le`) and `_hκ` (`theoremR`) — each the corollary of a program lemma that does
not assume it (`rank_span_log_le_of_supp`, `theoremR_of_A9`); the Solution passes every hypothesis on, so it builds with 0 warnings. Helper
lemmas and the errata's strengthenings (E1–E5) are program-side only; none is a statement of the topic. One pin-level design point: rewriting
under the coercion `Nat.Primes → ℕ` fails at 51e6992e when an anonymous constructor `⟨p, hp⟩` meets α = `Nat.Primes` (`rw`/`simp` refuse a target
"not type-correct under the implicit transparency level" — `Nat.Primes` is a `def`), so the internal work uses the named family `logP` and
variables of type `Nat.Primes`; item 1's statement is `logP`'s by definitional unfolding (`log_primes_linearIndependent := linearIndependent_logP`).

## 2. Builds (one `lake` at a time; the tree's oleans reused throughout; wall times from the logs)

* **Rung 1** (`rung1-build.log`, `rung1-print-axioms.log`): `LogPrimes.lean` alone — first elaboration 4 errors (the coercion issue above three
  times; one un-beta-reduced goal), second clean; `/usr/bin/time -l lake build Zeta23.ResidueRank.LogPrimes` *Built (10s)*, 8697 jobs, 13.23 s
  real, 0 warnings; `#print axioms` on the 15 names: the three standard axioms. (The file was later amended by one lemma, E4 — below.)
* **Items 4–8** (`program-build.log`): `Pair.lean` first elaboration 1 error (`hasSum_sum_of_ne_finset_zero`'s `SummationFilter` had to be named:
  `(L := SummationFilter.unconditional _)`) and 2 deprecation warnings (`push_neg`, `Set.mem_setOf_eq` — the step rewritten with
  `Set.eq_empty_of_forall_notMem`), second clean; `GenusBound.lean` clean at the first elaboration (7.8 s, `nlinarith` with explicit product
  hints). Then, TIMED, one at a time: `LogPrimes` (amended: `rank_span_log_le_of_supp`) *Built (3.2s)* 6.05 s real; `Pair` *Built (3.1s)* 5.09 s real;
  `GenusBound` *Built (7.3s)* 9.39 s real; 8697 / 8698 / 8697 jobs; 0 warnings; max RSS ≈ 5.9 GB (Mathlib's oleans mapped). The log's three empty
  `exit=` lines are a zsh artifact (`PIPESTATUS` is bash-only); the bash re-check appended to the log gives exit 0 for each.
* **The topic** (`build-comparator-topic.log`): `lake build Challenge.ResidueRank Solution.ResidueRank` — `Solution.ResidueRank` *Built (3.5s)* with
  0 warnings, `Challenge.ResidueRank` *Built (3.5s)* with exactly the 8 deliberate `sorry` warnings; *Build completed successfully (8701 jobs)*,
  5.61 s real, first try.

## 3. Checks

* `print-axioms.log`: `lake env lean comparator/PrintAxioms/ResidueRank.lean` — 8 lines, each `[propext, Classical.choice, Quot.sound]`;
  `program-axioms.log` (probe `program-axioms.lean`): all 27 program-side declarations, each `[propext, Classical.choice, Quot.sound]`. No
  `sorryAx`, no `Lean.ofReduceBool`.
* `statement-identity.log`: `tools/statement_identity_s36.py` (the H4/H5 extraction, extended): [A] challenge vs solution 8/8 IDENTICAL on the
  build tree AND on `rh-program/lean`; [B] challenge vs probe 8/8 IDENTICAL; [C] the config's `theorem_names` (prefix stripped) = the challenge's
  order, PASS; [D] the challenge's text from `import Mathlib` to the end = the probe's (3536 bytes), IDENTICAL; RESULT PASS.
* `trust-greps.log`: `tools/trust_greps_s36.py` (the H4 tool; nine words, comments stripped) on the six Lean files, both roots — exactly the 8
  deliberate challenge `sorry`s, nothing in the three program modules, the solution or the print-axioms file (exit 1 is the tool's "hits
  present" code, as in every prior record); the raw grep with comments included, for the record; imports (the challenge `import Mathlib`, the
  solution the two program modules, no `import Challenge` anywhere); no `set_option`, no attribute line; the mirror `cmp`-identical.
* `prerun-cleanup.log` (`tools/prerun-cleanup.sh`): the 16 artifacts of `Challenge/ResidueRank` and `Solution/ResidueRank` under
  `.lake/build/{lib/lean,ir}` removed, 0 remaining, so that comparator builds them itself (the program modules stay built — the untrusted side
  either way).
* **`comparator-run.log`: PASS** — 17:37:22–17:37:55 IST, `32.26 real`, max RSS 5.85 GB; runner `tools/run.sh` (the H4 runner; only the comment
  line and the `cd` target differ); comparator v4.33.0, lean4export v4.33.0-rc2, nanoda 0.4.17, the fake-landrun shim — NOT sandboxed, as in
  every prior macOS record (COMPARATOR-RUN.md §2); the four tool SHA-256s printed in the log equal COMPARATOR-RUN.md §1's. `Built
  Challenge.ResidueRank (2.0s)` with the 8 deliberate `sorry` warnings, `Built Solution.ResidueRank (3.0s)`, the export of the 8 names from both
  modules, `Running nanoda kernel on solution` / `Nanoda kernel accepts the solution` / `Running Lean default kernel on solution.` / `Lean default
  kernel accepts the solution` / `Your solution is okay!`, `--- comparator exit code: 0 ---`. What the run established: each solution statement
  coincides constant for constant with its challenge namesake (all constants are Mathlib's); the proofs use no axiom outside the three; nanoda
  re-checked the solution export and Lean's kernel replayed it. No CONTROL run: the tool chain is unchanged since the Session 25 records and the
  Session 32–33 runs (same four hashes).
* `yaml-validation.log`, `lint-10g.log`, `hashes.txt`: see §6.

## 4. Fidelity (FIDELITY.md; yaml row (aa))

Covered: the eight statements as theorems — H3.3(b), Theorem R's arithmetic core, the converse rank bound, Lemma F(a)'s finiteness, Lemma F(b),
Theorem R on the abstract pair (T3 at B = Spec Z), and the two scoped real-algebra statements. Not covered: the SPEC's A6–A8 and A7's graphs;
the existence or non-existence of a target Y; the general-base Theorem R; Lemma F(a)'s second clause as a topic statement (it is the program
lemma `fiber_sum_eq_log`) and Lemma F(c); the κ-scaling of the converse; the rung-1 side; the geometric reading of items 7–8; T1, T2, Prop.
2.2.1, Cor. 3.1–3.2, routes (a)/(b); ζ, its zeros, RH. Differs from the prose (r1–r11): the abstract pair; the indexing m, n ≥ 2; A5 built in;
A9 as an unconditional `HasSum` with one κ; κ's sign unused; Lemma F(b) on φ(p^a) without φ(1) = 1 but with `hmul` over all of ℕ, index 0 included (CHECK-O F1); "infinite-dimensional" as
`¬ Module.Finite`; Mathlib's totalizations; names; the program-side `_hpos`/`_hκ`; no trusted definition layer. **Fidelity divergences in the
brief's sense (a hypothesis beyond the statements' own): NONE.** Whether each proof uses each displayed hypothesis: FIDELITY §1, last paragraph
(`hκ` of item 6 is NOT used — the brief's question).

## 5. What the independent checker from a clean clone must do (`CHECK-O.md`; UNIT-BRIEF §3)

1. Clone `anthropics/zeta-23-lean` at tag `v1.0` into a new directory under `~/rh-lean-work/`, overlay from `rh-program/lean/` the three files
   `Zeta23/ResidueRank/{LogPrimes,Pair,GenusBound}.lean` and the four topic files `comparator/{Challenge,Solution,PrintAxioms}/ResidueRank.lean`,
   `comparator/config-residue-rank.json` (nothing else is needed: the modules import only Mathlib and each other); `lake exe cache get`; then, one
   at a time, `lake build Zeta23.ResidueRank.LogPrimes`, `Zeta23.ResidueRank.Pair`, `Zeta23.ResidueRank.GenusBound`, `Solution.ResidueRank`
   (expect ≈ 8697 / 8698 / 8697 / 8700 jobs, 0 errors, 0 warnings), and `Challenge.ResidueRank` (exactly the 8 deliberate `sorry` warnings).
2. `lake env lean comparator/PrintAxioms/ResidueRank.lean`: 8 lines, each `[propext, Classical.choice, Quot.sound]`; and
   `lake env lean results/theoremR-lean-s36/program-axioms.lean` (a copy placed in the clone) for the 27 program-side names.
3. `tools/statement_identity_s36.py ResidueRank <config> typing-probe.lean <clone> -- <the eight names>`; `tools/trust_greps_s36.py <clone>`
   (expect exactly the 8 challenge `sorry`s).
4. The Comparator run with nanoda from the clean clone (`tools/run.sh` with the clone's path; do NOT pre-build the comparator layer):
   `comparator/config-residue-rank.json`.
5. Read the eight challenge statements against NOTE §2.0, §2.3, §1.1 and read-O §2.5, and against FIDELITY.md: is every "covered" claim a theorem
   in the file with exactly the stated content; is every "not covered" sentence true; is any hypothesis present that the NOTE does not state; is
   the label exactly §1(3)'s; does any file, comment, yaml row or README line use a forbidden phrasing. Re-derive PREDERIVATION-ERRATA E1
   (κ < 0 satisfiable; the proof needs no κ hypothesis), E2–E5, E7 (item 7's derivation and its sharpness) and the necessity counterexamples.
6. Recompute every hash in `hashes.txt`; the yaml validation; the 10(g) lint.

## 6. Files written and SHA-256

`hashes.txt` (this directory) lists the SHA-256 of every file this job wrote or edited: the three Zeta23 modules, the three comparator Lean files
and the config, `lean/formalization.yaml`, `lean/README.md`, and every file under `results/theoremR-lean-s36/` except `SHARED.md` and
`hashes.txt` itself (their hashes are in `SHARED.md`'s final block and in the report to the orchestrator). Files under
`results/theoremR-lean-s36/` written by this job: `PREDERIVATION-ERRATA.md`, `SHARED.md`, `BUILD-NOTES.md`, `FIDELITY.md`, `hashes.txt`, the probes
`rung1-axioms.lean`, `program-axioms.lean`, the logs `rung1-build.log`, `rung1-print-axioms.log`, `program-build.log`, `program-axioms.log`,
`build-comparator-topic.log`, `print-axioms.log`, `statement-identity.log`, `trust-greps.log`, `prerun-cleanup.log`, `comparator-run.log`,
`yaml-validation.log`, `lint-10g.log`, and `tools/{run.sh, prerun-cleanup.sh, statement_identity_s36.py, trust_greps_s36.py, errata_numbers.py,
errata_numbers.log, lint_10g.py}`. 10(g) lint: U.S. English throughout; the four banned phrases and the brief's forbidden phrasings absent
(`lint-10g.log`).
