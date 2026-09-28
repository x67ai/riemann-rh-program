# D5 (F3, G4) — the C1 containment theorem (barrier-zoo IV.1) in Lean: independent check from clean clones (CHECKER, Opus 5; Session 30, 2026-09-29 00:23 – 00:45 IST)

Brief: `results/d5-lean-s30/BRIEF.md` §0, §1, §3 (SHA-256 `22e8656f…f846fae`, recomputed, matches). Builder's record: `BUILD-NOTES.md`
(SHA-256 `788bb774…9b5e`, matches `hashes.txt` and the builder's SHARED block), `FIDELITY.md`, `PREDERIVATION-ERRATA.md`, `hashes.txt`,
`SHARED.md`. Precedent for the shape: `results/c2-m4/CHECK-O-iii.md`. Every command below was run by me from two directories created
in this job — `~/rh-lean-work/checker-clone-s30` (a fresh clone of `anthropics/zeta-23-lean` at `v1.0`) and `~/prove2me-check-s30` (a
fresh clone of `prove2me/prove2me_workspace`) — never from the builder's trees. Logs: `results/d5-lean-s30/check-O/NN-*.log`.
Nothing was posted to Prove2Me; `~/Downloads/assets/prove2me.md` was not read. No file outside `results/d5-lean-s30/` (and the two
clone directories) was edited; nothing was committed by me. Nothing about ζ or RH follows from anything checked here.

## §0 Headline verdict

| # | Item | Verdict |
|---|---|---|
| 1 | Clone provenance (`v1.0` = `3635e748…`) and the `lean/README.md` "Building" overlay | **CLEAN** |
| 2 | `lake build Solution.WeilContainmentOne`, `lake build Solution.WeilContainment` (and the two challenges) | **CLEAN** (8698 / 8698 / 8699 jobs, 0 errors, 0 solution warnings, exactly 1 + 12 challenge `sorry` warnings) |
| 3 | `#print axioms`, 1 + 12 names | **CLEAN** (13 × `[propext, Classical.choice, Quot.sound]`; no `sorryAx`, no `Lean.ofReduceBool`) |
| 4 | Comparator with nanoda from the clean clone, topic artifacts removed before each run | **CLEAN** (rung 1 exit 0; family exit 0, twice) |
| 5 | Statement identity (my own checker plus the builder's tool; the d1-m2a DBN tool as a regression) | **CLEAN** (1 + 12 IDENTICAL; config names = challenge names in order; imports clean) |
| 6 | Trust greps (the builder's tool, a raw grep, the d1-m2a DBN tool) | **CLEAN** (the 13 deliberate challenge `sorry`s only) |
| 7 | `primeSide` against Zeta23's `literatureRHS` prime term | **CLEAN** — identical text after whitespace normalization, AND proved the same term by `rfl` in Lean |
| 8 | Prove2Me layout at Lean v4.33.1 / Mathlib 0df444a in a fresh checkout: build, `#print axioms solution`, the platform's three rules, type identity | **CLEAN** (28 modules, 8733 jobs, exit 0; 13 × the three axioms; 13 × `solution` type `==` the stub's type) |
| 9 | Challenge statements read against the record (IV.1, fatal 2 and its repair, MASTER FORMULA) | **CLEAN** — every statement is the record's claim or stronger; no hypothesis the prose does not state |
| 10 | FIDELITY.md "covered" rows — each a theorem in the file | **CLEAN** (10/10 rows, 13 theorems) |
| 11 | FIDELITY.md "not covered" facts — each true | **FIX-FIRST** — two sentences are false as written (items F1, F2 below); no statement, proof, or label is affected |
| 12 | (T1) re-derived on paper; errata E1–E6 | **CLEAN** for (T1)–(T3), E1, E3, E4, E5, E6; **E2 is over-corrected** (item F1) |
| 13 | The label of BUILD-NOTES, word for word | **CLEAN** — earned |
| 14 | `formalization.yaml` schema validation | **CLEAN** (errors 0, undeclared names 0; the 13 `weilContainment_*` names checked separately, all declared) |
| 15 | Hashes: every SHA-256 in `hashes.txt` recomputed | **CLEAN** (61/61, plus `hashes.txt` itself = the builder's stated `3f261181…600f`) |

**OVERALL: FIX-FIRST, prose only — two items (F1, F2).** Both are sentences in the "not covered" part of the ledger (and their copies)
that state a false mathematical fact. Neither touches a Lean statement, a proof, a constant, a hash of a Lean file, or the label. The
fix is a text edit in `FIDELITY.md`, `PREDERIVATION-ERRATA.md`, `BUILD-NOTES.md` and `lean/formalization.yaml` row (u), then a rehash; no
build or comparator run needs repeating. The Lean result itself is CLEAN.

**F1 (the C¹ sentence — E2's replacement is itself false as a universal statement).** FIDELITY (N2) says: "in general, for g(0) ≠ 0
and a ≠ 1/2, k_{a,g} is not even C¹ at 0 — the one-sided derivatives differ by (a − 1/2)g(0), and for C1's windows w ≥ 0, w ≢ 0 one
has g(0) = ∫w > 0 [so the failure is real for every member of the record's family and at every a ≠ 1/2]"; the same claim is in
PREDERIVATION-ERRATA E2 ("What is true, and sharper: for g(0) ≠ 0 and a ≠ 1/2, k_{a,g} is not even C¹ at 0"), BUILD-NOTES §0 ("for
g(0) ≠ 0 the test is not even C¹ at 0"), and `formalization.yaml` line 877 ("for g(0) ≠ 0 and a ≠ 1/2 the test is not even C¹ at 0").
Two errors:
 (a) The derivative computation presupposes that g is differentiable at 0. Without that it is false: at a = 1 the even function
 g(u) = 2e^{|u|/2} has g(0) = 2 ≠ 0 and `weilTestOf 1 g` is the constant 1, which is C^∞. Proved in Lean, not argued:
 `check-O/probe_E2_counterexample.lean` (`checker_E2_counterexample : weilTestOf 1 (fun u => 2 * exp(|u|/2)) = fun _ => 1`, then
 `ContDiff ℝ ⊤` of it; axioms `[propext, Classical.choice, Quot.sound]`; log `check-O/16-probe-E2-counterexample.log`).
 (b) "for every member of the record's family and at every a ≠ 1/2" is false for a < 1/2. The Fejér window w(t) = (sin(Lt/2)/(t/2))² ≥ 0
 has cos-transform proportional to (L − |u|)_+, supported in [−L, L], so it is in C1's family, and its cos-transform is NOT
 differentiable at 0. At a = 1/2 − 1/L, k(u) ∝ (L − |u|)e^{|u|/L} = L(1 − y)e^{y} with y = |u|/L, and (1 − y)e^{y} = 1 − y²/2 − y³/3 − …,
 so k is C² near 0. What IS true (my proof): for every a > 1/2 — the MASTER FORMULA's range, which is the record's family — and every
 window w ≥ 0, w ≢ 0, k_{a,g} is not differentiable at 0. Reason: g(u) = ∫w(t)cos(tu)dt ≤ g(0) = ∫w > 0. If k were differentiable at
 0, evenness gives k′(0) = 0, so g(u) = 2k(u)e^{(a−1/2)|u|} = g(0)(1 + (a − 1/2)|u|) + o(|u|) > g(0) for small u ≠ 0, a contradiction.
 **Fix:** replace the sentence in the four places with: "for g differentiable at 0 with g(0) ≠ 0 and a ≠ 1/2, k_{a,g} is not C¹ at 0 (the
 one-sided derivatives differ by (a − 1/2)g(0)); for C1's family — windows w ≥ 0, w ≢ 0, at every a > 1/2 — k_{a,g} is not even
 differentiable at 0 (g ≤ g(0) = ∫w > 0); without differentiability of g the claim fails (g = 2e^{(a−1/2)|u|} gives k ≡ 1), and at
 a < 1/2 it fails for the Fejér window at a = 1/2 − 1/L." The theorem `weilContainment_not_contDiff` is correct and stays as is. The
 trusted file's header comment (`Challenge/WeilContainment.lean` line 36, "k_{a,g} is in general not C¹ at u = 0 when a ≠ 1/2 and
 g(0) ≠ 0") is loose in the same way, but "in general" can be read as "generically". I recommend NOT editing it: a comment change
 alters the trusted file's hash and would oblige a fresh comparator run for no change in content. Record it here instead.

**F2 (the C² refinement "by finite interpolation" — false at an edge).** FIDELITY (N2): "The refinement 'every tilted datum equals
`primeSide k′` for some C² even k′ on the same band' is true by finite interpolation at the points ±log n, 2 ≤ n ≤ e^L, but is NOT
formalized and NOT claimed"; the same in PREDERIVATION-ERRATA ("One more check…"), and in shorter form in yaml line 878 and the challenge
header. Over the Lean family (every even g with tsupport g ⊆ [−L, L], no regularity) this is false when e^L is a prime power and g(±L) ≠ 0.
Take L = log 2 and g = the indicator of {−log 2, log 2}: g is even, tsupport g = {±log 2} ⊆ [−L, L], and `tiltedPrimeSide a g = Λ(2)·2^{−a}
= 2^{−a} log 2 ≠ 0`. A continuous k′ with tsupport k′ ⊆ [−log 2, log 2] has k′(±log 2) = 0 (the limit from outside the band), so
`primeSide k′` = (Λ(2)/√2)(k′(log 2) + k′(−log 2)) = 0 (n = 1 contributes Λ(1) = 0; n ≥ 3 lie outside the band). No C² k′ on the same band
reproduces the datum. The refinement is true for g continuous (so g(±L) = 0), which covers every ŵ of the record. **Fix:** add "for g
continuous (e.g. every cos-transform of a window)" to the sentence in each place it appears. The prose already marks it as not claimed,
so this is a correction of a remark, not of a statement.

## §1 Environment

| | clean zeta-23 clone | fresh Prove2Me checkout |
|---|---|---|
| directory | `~/rh-lean-work/checker-clone-s30` (new) | `~/prove2me-check-s30` (new) |
| source | `git clone https://github.com/anthropics/zeta-23-lean`; `git checkout v1.0` → `3635e74826a4c1fcece7d1cd2b6fa75e43a00510` ("Merge pull request #3 from anthropics/xiprime-pairceiling") | `git clone https://github.com/prove2me/prove2me_workspace` → `cb8d8291bc0edcb706d4e8a03814de78832f6503` ("Bump to 0.11.4"), the same HEAD as `~/prove2me_workspace` |
| pin | the upstream `lean-toolchain` (`leanprover/lean4:v4.33.0-rc2`) and manifest | `lean-toolchain` and `lakefile.lean` copied from `~/prove2me_workspace` (= `references/lean-setup.md` §2 verbatim: v4.33.1, Mathlib `0df444a…`, `autoImplicit false`) |
| `lean --version` (printed by the tool) | `Lean (version 4.33.0-rc2, arm64-apple-darwin24.6.0, commit d8b18978322de05a8f3dba51ef03cf5461676c17, Release)` | `Lean (version 4.33.1, arm64-apple-darwin24.6.0, commit 819816b2e0a3bf405af45ae5c7af2491d8f5bee6, Release)` |
| `lake --version` | `Lake version 5.0.0-src+d8b1897 (Lean version 4.33.0-rc2)` | `Lake version 5.0.0-src+819816b (Lean version 4.33.1)` |
| `git -C .lake/packages/mathlib rev-parse HEAD` | `51e6992efd06126df61a496bebf8f49482a4e129` | `0df444a360eaa60ab8c11dca51a86af692955474` |
| Mathlib cache | `lake exe cache get`: "No files to download", 8489 decompressed; 0 Mathlib modules compiled in any later build | `lake update` then `lake exe cache get`: "No files to download", "Already decompressed 8690 file(s)"; 0 Mathlib modules compiled |
| comparator tool chain | `leanprover/comparator` binary `fe1222e2…5d08`, lean4export `de4ffedf…7775`, nanoda_bin `d6c87133…48bb`, fake-landrun.sh `167507c8…8e4f` — each SHA-256 appears in `results/d1-m2a/packaging/COMPARATOR-RUN.md` | — |

Host: macOS 27.0, arm64; Python 3.9.6. Comparator runs are NOT sandboxed (the fake-landrun shim; Landlock does not exist on macOS), as
in every prior record (`COMPARATOR-RUN.md` §2); the `WARNING: THIS IS NOT REAL LANDRUN!` line appears once per sandboxed step.

## §2 Commands and logs (every log under `results/d5-lean-s30/check-O/`)

| # | command (in the clone unless stated) | log | result |
|---|---|---|---|
| 1 | `git clone …zeta-23-lean checker-clone-s30` (retry loop ×30), `git checkout v1.0`, `git rev-parse HEAD` | `01-clone.log` | `3635e748…` |
| 2 | `cp -R rh-program/lean/Zeta23/. Zeta23/`; `cp -R rh-program/lean/comparator/. comparator/`; `cp rh-program/lean/Zeta23.lean Zeta23.lean`; `git status --short` | `02-overlay.log` | 63 changed/added paths; the 9 topic files new |
| 3 | `lake exe cache get` (retry loop) | `03-cache-get.log` | Mathlib `51e6992e`, no download |
| 4 | `lake build Solution.WeilContainmentOne` | `04-build-solution-one.log` | *Build completed successfully (8698 jobs)*, 13 s, 0 warnings |
| 5 | `lake build Solution.WeilContainment` | `05-build-solution.log` | *Build completed successfully (8698 jobs)*, 0 warnings |
| 6 | `lake build Challenge.WeilContainmentOne Challenge.WeilContainment` | `06-build-challenges.log` | *(8699 jobs)*, exactly 13 `declaration uses 'sorry'` warnings (1 + 12), 0 errors |
| 7 | `lake env lean comparator/PrintAxioms/WeilContainmentOne.lean`, `…/WeilContainment.lean` | `07-print-axioms.log` | §3 |
| 8 | pre-run cleanup: every `.lake/build` file matching `*WeilContainment*` removed (40 files; then 40 again before the second family run) | `08-prerun-cleanup.log` | 0 remaining each time |
| 9 | `check-O/run-check.sh comparator/config-weil-containment-one.json` (the builder's `tools/run.sh` with only the tree path and the comment line changed; `diff` in `09a-runner-diff.log`) | `09-comparator-one.log` | exit 0 |
| 10 | `check-O/run-check.sh comparator/config-weil-containment.json`, run twice (second after cleanup #2) | `10-comparator-family.log` | exit 0, exit 0 |
| 11 | `python3 check-O/identity_check_o.py . <Topic> <config> comparator/ChallengeDeps/WeilContainment.lean` ×2; `python3 tools/statement_identity_d5.py . WeilContainmentOne …` and `… WeilContainment <12 names>`; `python3 results/d1-m2a/packaging/statement_identity.py .` | `11-statement-identity.log` | §4 |
| 12 | `python3 tools/trust_greps_d5.py . <7 files>`; raw `grep -nwE` of 20 words over the 7 files and 2 configs; `python3 results/d1-m2a/packaging/trust_greps.py .` | `12-trust-greps.log` | §5 |
| 13 | Python: `literatureRHS`'s prime-term lines versus `primeSide`'s body | `13-primeSide-char-diff.log` | IDENTICAL (105 = 105 chars) |
| 14 | `lake build Zeta23.ExplicitFormula` | `14-build-zeta23-explicitformula.log` | *(3145 jobs)*, 0 errors |
| 15 | `lake env lean check-O/probe_primeSide_defeq.lean` | `15-probe-primeSide-defeq.log` | exit 0 (second run; §6) |
| 16 | `lake env lean check-O/probe_E2_counterexample.lean` | `16-probe-E2-counterexample.log` | exit 0 (F1(a)) |
| 17 | `grep` of the IV.1 STATEMENT bullet, the adjudication JSON's fatal 2 / repair / fatal 1, the MASTER FORMULA line | `17-record-quotes.log` | §7 |
| 20 | `git clone …prove2me_workspace prove2me-check-s30` (retry loop); copy `lean-toolchain`, `lakefile.lean` | `20-p2m-clone.log` | `cb8d8291…` |
| 21 | `lake update`; `lake exe cache get` (retry loops) | `21-p2m-update-cache.log` | Mathlib `0df444a…`, no download |
| 22 | copy the 27 files listed in `hashes.txt` from `~/prove2me_workspace`; re-generate them from the clean clone's `comparator/` with `tools/gen_prove2me_layout.py` and `gen_prove2me_solutions.py` into a scratch directory; `cmp` | `22-p2m-copy-regen.log` | 27 copied; 27/27 regenerated files byte-identical to the builder's |
| 23 | `lake build Solutions.SmokeTest Definitions.Def_WeilContainment <13 Thm_> <13 Sol_>` | `23-p2m-build.log` | *Build completed successfully (8733 jobs)*, 36.5 s, exit 0; 13 `sorry` warnings, all in `Theorems/Thm_*` stubs; no warning from any `Sol_` |
| 24 | per solution: grep for the three rules; a probe importing `Thm_X` and `Sol_X` that compares `(env.find? `solution).type == (env.find? `WeilContainment.X).type` (Lean `Expr` equality) and runs `#print axioms solution` | `24-p2m-rules-types-axioms.log` | §8 |
| 25 | statement text challenge = stub = solution, ×13; `Def_WeilContainment` body = `ChallengeDeps` body | `25-p2m-statement-text.log` | PASS (second pass; §8) |
| 30 | `shasum -a 256` of every file in `hashes.txt`; `hashes.txt` itself; the 27 files in my checkout; `cmp` of the 9 topic files in the clean clone against `rh-program/lean/comparator/` | `30-hashes.log` | §10 |
| 31 | `python3 validate_yaml_sigma_strong.py` (from `results/d1-m2a/dr8/`); a supplementary name check | `31-yaml-validation.log` | §9 |

Superseded passes kept in the logs, each marked "RERUN": in `11-` the builder's identity tool first got the twelve names as ONE argument
(zsh does not word-split an unquoted `$N` — the same slip the builder logged); in `15-` my second example first used
`with_reducible rfl` without unfolding the (non-reducible) `def` — a probe error; in `25-` my first regex required `:= by` and nine
solutions are term-mode; in `31-` the first pass was truncated by `head -40`. None is a finding about the unit.

## §3 `#print axioms` (verbatim, `07-print-axioms.log`)

```
== lake env lean comparator/PrintAxioms/WeilContainmentOne.lean
'weilContainment_identity_one' depends on axioms: [propext, Classical.choice, Quot.sound]
exit=0
== lake env lean comparator/PrintAxioms/WeilContainment.lean
'weilContainment_identity' depends on axioms: [propext, Classical.choice, Quot.sound]
'weilContainment_cutoff' depends on axioms: [propext, Classical.choice, Quot.sound]
'weilContainment_tilt_bounds' depends on axioms: [propext, Classical.choice, Quot.sound]
'weilContainment_tilt_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'weilContainment_tilt_inv' depends on axioms: [propext, Classical.choice, Quot.sound]
'weilContainment_even' depends on axioms: [propext, Classical.choice, Quot.sound]
'weilContainment_tsupport' depends on axioms: [propext, Classical.choice, Quot.sound]
'weilContainment_tsupport_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'weilContainment_continuous' depends on axioms: [propext, Classical.choice, Quot.sound]
'weilContainment_exact' depends on axioms: [propext, Classical.choice, Quot.sound]
'weilContainment_range_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'weilContainment_not_contDiff' depends on axioms: [propext, Classical.choice, Quot.sound]
exit=0
```

The PrintAxioms files import `Solution.*` only, so these are the solution's constants, which comparator then matched to the challenge's.

## §4 Comparator runs (exit codes)

| run | config | start (IST) | wall | lines | exit |
|---|---|---|---|---|---|
| rung 1 | `comparator/config-weil-containment-one.json` (1 name) | 00:28:01 | 30.56 s | `Built ChallengeDeps.WeilContainment (2.9s)`, `Built Challenge.WeilContainmentOne (2.0s)` + its 1 `sorry` warning (36:8), `Built Solution.WeilContainmentOne (3.1s)`, `Nanoda kernel accepts the solution`, `Lean default kernel accepts the solution`, `Your solution is okay!` | **0** |
| family, 1st | `comparator/config-weil-containment.json` (12 names) | 00:28:38 | 40.02 s | `Built Challenge.WeilContainment (3.1s)` + 12 `sorry` warnings (lines 54, 60, 67, 73, 77, 81, 86, 91, 96, 102, 109, 117), `Built Solution.WeilContainment (3.2s)`, nanoda accepts, Lean kernel accepts, `Your solution is okay!` | **0** |
| family, 2nd | the same, after cleanup #2 (so comparator rebuilt `ChallengeDeps.WeilContainment` itself: 24 s) | 00:40:27 | 70.72 s | the same lines | **0** |

The first family run reused the `ChallengeDeps.WeilContainment` olean that comparator had built during the rung-1 run (not one I had
pre-built); the second run removes even that, matching the "artifacts removed before each run" standard of `CHECK-O-iii.md`.

Statement identity and imports (`11-statement-identity.log`): my `identity_check_o.py` (comments stripped, whitespace normalized, helper
namespaces dropped) — WeilContainmentOne 1/1 and WeilContainment 12/12 IDENTICAL; config `theorem_names` = the challenge's names in
order (True, both); no extra root theorem in either solution; imports `ChallengeDeps.WeilContainment` ← `Mathlib` only, challenges and
solutions import `ChallengeDeps.WeilContainment` only, no `Zeta23`, no `Challenge.*` in a solution; every challenge proof is `by sorry`
(1 and 12). The builder's `statement_identity_d5.py`: PASS on both topics (byte comparison). The d1-m2a `statement_identity.py` is written
for the DBN topic only (`config-dbn.json`); run as asked, it reports the DBN topic IDENTICAL on the clean clone — a regression check,
not a check of this unit.

## §5 Trust greps (`12-trust-greps.log`)

The builder's `trust_greps_d5.py` over the seven topic files (nine words, comments stripped): 13 hits, all `sorry`, all on the challenge
side — `Challenge/WeilContainmentOne.lean:38` and `Challenge/WeilContainment.lean:57, 64, 70, 74, 78, 83, 88, 93, 98, 105, 113, 118`
(exit 1 is the script's convention: it counts every hit). My raw grep (comments included) over the 7 files and 2 configs for `axiom`,
`native_decide`, `unsafe`, `implemented_by`, `extern`, `opaque`, `sorry`, `admit`, `ofReduceBool`, `decide`, `macro`, `elab`,
`set_option`, `attribute`, `instance`, `local`, `private`, `noncomputable`, `@[`: the same 13 `sorry` lines, four `noncomputable
section` lines, and comment mentions in the headers — nothing else. The d1-m2a `trust_greps.py` (DBN-scoped) on the clean clone:
CLEAN (7 permitted DBN placeholders, 0 other hits).

## §6 `primeSide` is Zeta23's prime term — text and term

Text (`13-primeSide-char-diff.log`): the two lines of `Zeta23/ExplicitFormula.lean` `literatureRHS` (lines 72–73 of the clean clone,
`- ∑' n : ℕ, ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ)` / `* (k (Real.log n) + k (-Real.log n))`) with the leading
`- ` removed, and the body of `WeilContainment.primeSide`, both whitespace-normalized: IDENTICAL, 105 characters each (the only raw
difference is the indentation of the first line). The clean clone's `ExplicitFormula.lean` is `cmp`-identical to
`~/rh-lean-work/checker-clone-s21/Zeta23/ExplicitFormula.lean`, the file the brief cites.
Term (`15-probe-primeSide-defeq.log`): in the clean clone, importing `Zeta23.ExplicitFormula` and `ChallengeDeps.WeilContainment`,
```
Zeta23.EF.literatureRHS k = Zeta23.paperFT k (I / 2) + Zeta23.paperFT k (-I / 2) - WeilContainment.primeSide k
    + (1 / (2 * Real.pi) : ℂ) * ∫ r : ℝ, Zeta23.paperFT k r * (Zeta23.EF.gammaBracket r : ℂ)      -- by rfl
WeilContainment.primeSide k = ∑' n : ℕ, ((vonMangoldt n / Real.sqrt n : ℝ) : ℂ) * (k (log n) + k (-log n))
                                                                   -- by unfold; with_reducible rfl
```
both check. So D3's "definitionally the Zeta23 expression" is a checked fact, not a reading. The `#print` of both definitions is in
the log and shows the same elaborated sum.

## §7 The statements against the record

The record, read at the line (`17-record-quotes.log`): `BARRIER-ZOO.md` line 376 (IV.1 STATEMENT: "C1's entire (a,w)-family of
prime-computable tilted-EF observables was identified with classical Weil tests (1/2)ŵ(u)e^{−(a−1/2)|u|} on the same band via
bounded-below multipliers — the family spans exactly bandwidth-log X Weil-EF data; multi-a constraints follow from single-band data by
analytic continuation (information-free)."); `results/adjudication-C1.json` `adjudication` "(2) Data-class containment: … the
multipliers are bounded below on the compact band, so the family spans exactly bandwidth-log X Weil-EF data …" and
`mandatory_repairs` "Prove the containment theorem as the honest deliverable: the full (a,w)-family of prime-computable tilted-EF
observables at cutoff X lies inside the classical bandwidth-log X Weil-EF data class …"; `directions/C1-requirements-first-field.md`
line 18 (MASTER FORMULA: "for a > 1/2 and any window w >= 0 with hat-w supported in [-log X, log X], … = Arch_a(w) - Sigma_{n <= X}
Lambda(n) n^{-a} (cos-transform of w)(log n)"). The BRIEF §0 quotes match these lines.

**(T1), re-derived by me.** Fix a ∈ ℝ, g even, k = weilTestOf a g. At n = 0: Λ(0) = 0 kills the left summand; on the right,
(Λ(0)/√0 : ℝ) = 0/0 = 0 in Lean. At n = 1: Λ(1) = 0 on both sides. At n ≥ 2: log n > 0, |±log n| = log n, so tilt a (±log n) =
exp(−(a − 1/2) log n) = n^{1/2−a}; with g even, k(log n) + k(−log n) = g(log n)·n^{1/2−a}; (Λ(n)/√n)·n^{1/2−a} = Λ(n)·n^{−1/2}·n^{1/2−a}
= Λ(n)·n^{−a}. The summands agree for every n, so the `tsum`s agree (`tsum_congr`), summable or not. No step uses a > 1/2. (T1) is right,
and `weilContainment_identity` is exactly it.

**Each statement against the record** (file `lean/comparator/Challenge/WeilContainment.lean`, read line by line):
* `tiltedPrimeSide a g` = `∑' n, Λ(n)·(n^{−a} : ℝ)·g(log n)` — the MASTER FORMULA's prime sum with g for the cos-transform and all n
  for n ≤ X; `weilContainment_cutoff` proves the two equal under the band hypothesis. I checked its right-hand side: `Finset.range
  (⌊e^L⌋₊ + 1)` is {0, …, ⌊X⌋}, and an integer n satisfies n ≤ X exactly when n ≤ ⌊X⌋. For L < 0 the range is {0} and the n = 0 term is
  0, consistent.
* `weilTestOf a g u` = (1/2)·g(u)·e^{−(a−1/2)|u|}: the record's "(1/2)ŵ(u)e^{−(a−1/2)|u|}" with g for ŵ. For real w, ŵ and the
  cos-transform differ by i·(sine transform), which is odd, so the symmetric sum k(log n) + k(−log n) inside `primeSide` gives the same
  number for either — the choice of g loses nothing (FIDELITY D4 records it; E3's evenness remark is correct).
* `tilt_bounds`, `tilt_pos`: "bounded-below multipliers on the compact band", with both bounds explicit. Right.
* `tsupport_eq` (and `tsupport`), `even`, `continuous`: "on the same band"; the test is an even test. Right, and `tsupport_eq` is
  unconditional as stated.
* `tilt_inv`, `exact`, `range_eq`: "spans exactly"; `range_eq` is the sentence itself as a set equality for every real a and L. The
  classical side of `range_eq` is "even, band-limited" with no regularity; the record's "Weil-EF data class" carries Zeta23's C² class —
  FIDELITY (N2) says so, and the label says "prime-side containment". Right.
* `not_contDiff`: at a = 1, g ≡ 1, the test (1/2)e^{−|u|/2} is not C² — true (not differentiable at 0).
* Hypotheses: evenness of g (the cos-transform is even for every w — no new assumption), the band `tsupport ⊆ Icc (−L) L` (the prose's
  "bandwidth log X", Zeta23's `prime_term` form), |u| ≤ L (the band). **No hypothesis appears that the prose does not state**, and none is
  hidden in a definition: the four trusted definitions are plain `def`s over Mathlib, read in full.
* "multi-a constraints follow … by analytic continuation": the file gives the algebraic inverse instead (D2), which needs no
  continuation. Right, and it is stronger for the containment claim.

**FIDELITY.md, row by row.** "Covered" (§1), ten rows: every row names a theorem present in the challenge file with exactly the stated
content (13 theorems: `identity`, `identity_one` (in `Challenge/WeilContainmentOne.lean`), `cutoff`, `tilt_bounds`, `tilt_pos`,
`tsupport_eq`, `tsupport`, `even`, `continuous`, `tilt_inv`, `exact`, `range_eq`, `not_contDiff`). 10/10 CLEAN. "Not covered" (§2):
N1 true (no statement mentions zeros, `ZeroConfig`, `EF_lit`, `paperFT`); N2 — its first sentences true, its C¹ sentence false as
written (F1) and its interpolation sentence false at an edge (F2); N3 true (every statement is linear in the test); N4 true; N5 true (Mathlib's
`tsum` is 0 off summability; the identity is termwise); N6 true. "Differs" (§3) D1–D8: each true as stated (D1's "0^{−a} ∈ {0, 1}" is
Mathlib's `Real.zero_rpow`/`rpow_zero`; D6's "for L < 0 the band is empty and both sides are 0" is right).

**PREDERIVATION-ERRATA E1–E6.** E1 right (evenness of the test is needed for ⊆ in "same set"). E2: the criticism of the brief is right
(g ≡ 0, or g vanishing to order ≥ 3, gives a C² test); the replacement is over-stated — F1. E3 right. E4 right (0 ≤ |u| ≤ L). E5 right
(n > e^L ⟹ log n > L ⟹ g(log n) = 0 since log n ∉ tsupport g). E6 right (tilt > 0 and 1/2 ≠ 0 give equal supports).

**The label, word for word.** "IV.1 formalized-in-Lean (prime-side containment; Comparator-checked over Mathlib alone, no displayed
hypothesis, axioms propext/Classical.choice/Quot.sound, replayed by nanoda; built at v4.33.0-rc2/51e6992e and v4.33.1/0df444a)" —
"prime-side containment": the statements are about the prime functionals only (§7); "Comparator-checked": §4, exit 0 ×3; "over Mathlib
alone": the trusted module imports `Mathlib` only, and neither side imports `Zeta23` (§4, §5); "no displayed hypothesis": none (§7);
"axioms …": §3 and §8; "replayed by nanoda": `Nanoda kernel accepts the solution` in every run; "built at v4.33.0-rc2/51e6992e and
v4.33.1/0df444a": §1, §2 rows 4–6 and 23. **Earned.** F1 and F2 do not touch it. It correctly omits "kernel-checked on Prove2Me".

## §8 The Prove2Me layout at v4.33.1 / 0df444a (fresh checkout)

`23-p2m-build.log`: the smoke test, `Definitions.Def_WeilContainment`, the 13 `Theorems.Thm_WeilContainment_<suffix>` stubs and the 13
`Solutions.Sol_WeilContainment_<suffix>` — *Build completed successfully (8733 jobs)* (the builder's 8732 plus the smoke test), exit 0,
no Mathlib module compiled. `24-p2m-rules-types-axioms.log`, for each of the 13 solutions: exactly one line `theorem solution` at top
level, zero `namespace` lines (rule 1); imports exactly `Definitions.Def_WeilContainment` and `Mathlib`, zero `Theorems.` imports (rule
2 — so no `sorry`-carrying stub is in any solution's closure); zero `sorry`/`admit` words (rule 3); `solution`'s type is `Expr`-equal to
the stub's `WeilContainment.<suffix>` type (13/13 `true` — stricter than the platform's check); `#print axioms solution` = `[propext,
Classical.choice, Quot.sound]` (13/13). `25-p2m-statement-text.log`: challenge text = stub text = solution text, 13/13 IDENTICAL;
`Def_WeilContainment`'s body from `import` on = the `ChallengeDeps` body. `22-p2m-copy-regen.log`: re-running the builder's two
generators on the clean clone's `comparator/` reproduces all 27 files byte for byte. Nothing uploaded.

## §9 `formalization.yaml`

`31-yaml-validation.log`: schema validation (PyYAML 6.0.3, jsonschema 4.25.1, the three on-disk schemas IDENTICAL to upstream):
`RESULT: PASS — errors: 0, undeclared names: 0`, main_results 28, alignment.statements 30. The validator resolves only `Zeta23.*` names,
so the unit's 13 `weilContainment_*` names are outside its net; my supplementary check finds each of them declared in the challenge
files. Row (u) line 877 carries F1's sentence and line 878 F2's (fix them with FIDELITY).

## §10 Hashes (`30-hashes.log`)

Every SHA-256 in `hashes.txt` recomputed: **61/61 MATCH, 0 mismatch** — the 11 `lean/` files (source of truth in rh-program), the 27
Prove2Me-layout files in `~/prove2me_workspace`, and the 23 files under `results/d5-lean-s30/`. `hashes.txt` itself =
`3f261181dddc2f081b55302765037a0544c3408d8066ee6493e0824ab860600f`, the value in the builder's final SHARED block. The 27 files as
copied into my checkout: 27/27 match. The 9 topic files in the clean clone are `cmp`-identical to `rh-program/lean/comparator/`.
`SHARED.md` before my block: `2ce9b97364fb3aefa53a42c13f7a51cd32d7ef9196b4ccc222a33d5a6059bc01` (the builder states its own hash only in
the chat report, which I cannot see).

| file | listed = recomputed |
|---|---|
| `lean/comparator/ChallengeDeps/WeilContainment.lean` | `47c9a508…4b7c` ✓ |
| `lean/comparator/Challenge/WeilContainmentOne.lean` | `92dfd2e7…e3f2` ✓ |
| `lean/comparator/Challenge/WeilContainment.lean` | `88e60a36…7e50` ✓ |
| `lean/comparator/Solution/WeilContainmentOne.lean` | `54f75921…db4d` ✓ |
| `lean/comparator/Solution/WeilContainment.lean` | `338728a6…9254` ✓ |
| `lean/comparator/PrintAxioms/WeilContainmentOne.lean`, `…/WeilContainment.lean` | `57adaace…ecaa`, `044e4a2d…c56b` ✓ |
| `lean/comparator/config-weil-containment-one.json`, `config-weil-containment.json` | `4eace1c6…5ea5`, `8c8f6901…8b48` ✓ |
| `lean/formalization.yaml`, `lean/README.md` | `3f338b50…c2a4`, `cb8a4ec1…0152` ✓ |
| 27 Prove2Me files (`Definitions/`, 13 `Theorems/`, 13 `Solutions/`) | 27/27 ✓ (full list in the log) |
| 23 files under `results/d5-lean-s30/` (BRIEF, ERRATA, FIDELITY, BUILD-NOTES, 14 logs, 5 tools) | 23/23 ✓ (full list in the log) |

## §11 What the orchestrator should do

Apply F1 and F2 (text only) in `FIDELITY.md` (N2), `PREDERIVATION-ERRATA.md` (E2 and "One more check"), `BUILD-NOTES.md` §0, and
`lean/formalization.yaml` row (u) lines 877–878; revalidate the yaml; rehash those four files in `hashes.txt`. Do not edit the Lean files
(the one loose comment is recorded in F1). Then the unit stands with its label as earned. Nothing about ζ or RH follows.
