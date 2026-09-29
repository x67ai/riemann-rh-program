# G8 — IV.17's fractional-mark integrality theorem and its rational-mark negation in Lean (Comparator topic `IntegralityGap`): independent check from a clean clone (CHECKER, Opus 5; Session 30, 2026-09-29 01:08 – 01:22 IST)

Brief: `results/iv17-lean-s30/BRIEF.md` §0, §1, §3 (SHA-256 `9aabf0db…2ffd70`, recomputed, matches). Builder's record: `BUILD-NOTES.md`
(SHA-256 `a3c3bd69…b728`, matches the builder's final SHARED block), `TYPING-NOTE.md`, `FIDELITY.md`, `hashes.txt`, `SHARED.md`. Shape
and standard: `results/d5-lean-s30/CHECK-O.md`, `results/c2-m4/CHECK-O-B.md`. Every command below was run by me from a directory created
in this job, `~/rh-lean-work/checker-clone-s30b` (a fresh clone of `anthropics/zeta-23-lean` at `v1.0`), never from the builder's tree
(`checker-clone-s21`). Logs: `results/iv17-lean-s30/check-O/NN-*.log`; my probes and tools sit beside them. No Prove2Me action;
`~/Downloads/assets/prove2me.md` was not read. No file outside `results/iv17-lean-s30/` (and the clone) was edited; nothing was
committed by me (the session's autocommit watchdog may pick up my files; that is not a commit of mine). Nothing about ζ or RH follows
from anything checked here.

## §0 Headline verdict

| # | Item | Verdict |
|---|---|---|
| 1 | Clone provenance (`v1.0` = `3635e748…`) and the `lean/README.md` "Building" overlay | **CLEAN** |
| 2 | `lake build` of `Zeta23.PairCeiling.GridParsevalRat`, `…GridGap`, `Solution.IntegralityGap`, `Challenge.IntegralityGap` | **CLEAN** (2081 / 2082 / 8702 / 8698 jobs; 0 errors; 0 warnings outside the 16 deliberate challenge `sorry`s) |
| 3 | `#print axioms`, 16 names | **CLEAN** (16 × `[propext, Classical.choice, Quot.sound]`; no `sorryAx`, no `Lean.ofReduceBool`) |
| 4 | Comparator with nanoda from the clean clone, the topic's build artifacts removed first | **CLEAN** — exit **0** |
| 5 | Statement identity (my own checker, the builder's tool on clone and tree) | **CLEAN** (16/16 IDENTICAL; config names = challenge names in order; every challenge proof exactly `by sorry`; no extra declaration in the solution) |
| 6 | Trust greps (the builder's tool, my raw 20-word grep) | **CLEAN** (exactly the 16 challenge `sorry`s; three `decide +kernel`, no `native_decide`) |
| 7 | Trusted vocabulary against its Zeta23 originals | **CLEAN as constants** (7/7 `rfl` on the `@`-constants); textually 6/7 byte-identical, `dftMarkQ` differs in where its `{F} [Field F]` binder is written (observation O1) |
| 8 | Rational Parseval = the integer identity with ℚ for ℤ; the ℤ theorem re-exported faithfully | **CLEAN** (statement texts identical under the substitution map; §6) |
| 9 | `per_atom_slack` is the line where integrality is consumed | **CLEAN in substance, proved by me in Lean** ((MI) follows from the slack alone, over ℚ; the integer (MI) follows with `per_atom_slack` as its ONLY integrality input) — but one docstring overstates it as a dependency (item F2) |
| 10 | The zoo's numbers are exactly the instance's | **CLEAN** (48 atoms of 4/3 on 65 sites, mass 64, Σm² = 256/3, N_d = 48, 96 > 256/3, row = (4/3)·64 at ε = 0; re-derived by hand and in Lean) |
| 11 | FIDELITY.md "covered" rows | **CLEAN** (16/16 rows, each a theorem in the challenge with exactly the stated content) |
| 12 | FIDELITY.md "not covered" facts and "differs" items | **CLEAN** (each true; (v4) and (v6) confirmed by probe) |
| 13 | Hypotheses the prose does not state | **CLEAN** — none; the only added hypotheses (`0 ≤ m`, mass, budget) sit inside negated universals, where they make the negation STRONGER |
| 14 | The label of BUILD-NOTES, word for word | **CLEAN** — earned; the pair channel is unformalized and the label, the challenge header and FIDELITY say so |
| 15 | `results/a4-no-go/formalization-status.md` addendum | **CLEAN** as to the record (append-only: 26 lines added, 0 removed, the 135-line prefix byte-identical); one sentence of the appended text is inaccurate (item F1) |
| 16 | `formalization.yaml` schema validation; 10(g) lint | **CLEAN** (errors 0, undeclared 0; lint clean) |
| 17 | Hashes: every SHA-256 in `hashes.txt` recomputed | **CLEAN** (28/28; `hashes.txt` itself = the builder's stated `7f74bc0e…e6204`) |

**OVERALL: FIX-FIRST, prose only — two items (F1, F2), both comments/prose about the proofs, neither touching a statement, a proof, a
definition, an axiom, the comparator result, or the label.** The Lean result itself is CLEAN.

**F1 (the "kernel-checked by `decide +kernel`" count is wrong in two places).** `lean/Zeta23/PairCeiling/GridGap.lean` lines 40–42:
"the five column-data facts of the instance (`fracMark_mass`, `fracMark_sq`, `fracMark_Nd`, and the two used through them) are
kernel-checked (`decide +kernel`, NumericCert discipline)". There are exactly THREE `decide +kernel` facts (lines 112, 115, 119;
`12-trust-greps.log`). The other two column facts are proved otherwise: `fracMark_nonneg` by `simp only [fracMark]; split_ifs <;>
norm_num`, and `fracMark_row` by `rw [gridRowQ_eq 32 fracMark, fracMark_sq]; norm_num` — through rational Parseval, which no decision
procedure could replace (the row contains `Complex.exp`). The phrase was evidently carried over from `GridCorner.lean` line 57, where
"the four column-data facts … are kernel-checked (`decide +kernel`)" is exact (four `decide +kernel` lines, 219–230). The same slip is in
the formalization-status addendum (`results/a4-no-go/formalization-status.md` lines 150–151: "mass 64, Σm² = 256/3, N_d = 48, row =
(4/3)·64 — kernel-checked by `decide +kernel`" — the row is not). BUILD-NOTES §1's table and FIDELITY §1 are correct (they attach
`decide +kernel` to the three facts only). **Fix:** in `GridGap.lean` replace "the five column-data facts of the instance
(`fracMark_mass`, `fracMark_sq`, `fracMark_Nd`, and the two used through them) are kernel-checked (`decide +kernel`, NumericCert
discipline)" by "the three column-data facts of the instance (`fracMark_mass`, `fracMark_sq`, `fracMark_Nd`) are kernel-checked
(`decide +kernel`, NumericCert discipline); `fracMark_nonneg` is `norm_num`, and `fracMark_row` is rational Parseval (`gridRowQ_eq`)
plus `fracMark_sq`"; in the addendum replace "row = (4/3)·64 — kernel-checked by `decide +kernel`)" by "row = (4/3)·64 — the first three
kernel-checked by `decide +kernel`, the row by rational Parseval)". The addendum edit is inside the builder's own dated block, so it
does not touch the 2026-08-27 record.

**F2 (`mi_holds_integer`'s docstring states a dependency that does not exist).** `GridGap.lean` line 93: "Its proof consumes integrality
at exactly `per_atom_slack`." The proof is `two_mul_distinct_ge m hm`, and `two_mul_distinct_ge` (GridParseval.lean 546–570, a module
upstream of GridGap) cannot and does not reference `per_atom_slack`; it carries its own inline copy of the slack (line 561,
`nlinarith [mul_nonneg (… m k − 1) (… m k − 2)]` at 2 ≤ m, after `omega` case splits). FIDELITY (v6) says this honestly ("a re-export
… not a re-proof through `per_atom_slack`"), and the brief's close ("the line where integrality is consumed is the named theorem
`per_atom_slack`") is TRUE IN CONTENT — I proved it (§7, probe `checker_mi_of_slack`: (MI) holds for every nonnegative RATIONAL mark
vector whose marks satisfy (m − 1)(m − 2) ≥ 0, no integrality used; `checker_mi_integer_via_slack`: the integer (MI) with
`per_atom_slack` as its only integrality input). Only the docstring's wording, read as "the proof term uses the constant", is false.
**Fix:** replace the sentence by "Its content is exactly `per_atom_slack` summed over occupied sites (2 − (3m − m²) = (m − 1)(m − 2));
the proof of `two_mul_distinct_ge` carries an inline copy of that step (GridParseval.lean, the `nlinarith` at 2 ≤ m)." Optionally (not
required by the brief) add the checker's `checker_mi_of_slack` to GridGap as `mi_of_slack` and restate the re-export through it, which
would make the dependency literal; that would change the Solution side only and need a rebuild and a comparator rerun.

**After F1/F2:** both Lean edits are comments in an UNTRUSTED module (`GridGap.lean`; the challenge and trusted files are untouched), so
no statement changes; but the file's hash changes, so for record hygiene rebuild `Zeta23.PairCeiling.GridGap` and `Solution.IntegralityGap`,
rerun the comparator once (≈ 31 s), and rehash `GridGap.lean`, `formalization-status.md`, and `hashes.txt`. If the orchestrator prefers
not to touch the Lean file, record both corrections in FIDELITY.md instead (the D5 precedent for comments).

**O1 (observation, no fix required).** "character for character" (BUILD-NOTES §1, TYPING-NOTE §4, FIDELITY §4, README line 448, yaml
line 633, and the trusted file's own header) is literally true for 6 of the 7 trusted definitions; for `dftMarkQ` the trusted file writes
`def dftMarkQ {F : Type*} [Field F] (ζ : F) …` where `GridParsevalRat.lean` has `def dftMarkQ (ζ : F) …` under a section
`variable {F : Type*} [Field F]`. The elaborated constants are identical — `#check` prints the same telescope `{M : ℕ} → [NeZero M] →
{F : Type u_1} → [Field F] → F → (ZMod M → ℚ) → ZMod M → F` for both, and `@IntegralityGap.dftMarkQ =
@Zeta23.PairCeiling.GridParsevalRat.dftMarkQ := rfl` checks (`14-trusted-defs-diff.log`) — which is the property the delegation needs
and is stronger than textual identity. I recommend NOT editing the trusted file's header (it would change the trusted hash for no change
of content); a one-clause qualifier in FIDELITY §4 ("`dftMarkQ`: same constant, the `Field` binder written inline") suffices at harvest.

**O2 (observation).** The brief anticipated `decide +kernel` facts "on `[propext, Quot.sound]` or fewer, as `GridCorner` records".
`GridCorner.lean` records no axiom list, and its own `attainMark_mass`/`attainMark_sq` print all three at this toolchain (my probe,
`13-probe-checker.log`), as do `fracMark_mass/sq/Nd`. FIDELITY (v8) and TYPING-NOTE §3 already say so; the label's axiom clause is
the three, so nothing changes.

## §1 Environment

| | clean zeta-23 clone |
|---|---|
| directory | `~/rh-lean-work/checker-clone-s30b` (new in this job) |
| source | `git clone https://github.com/anthropics/zeta-23-lean` (retry loop), `git checkout v1.0` → `3635e74826a4c1fcece7d1cd2b6fa75e43a00510` ("Merge pull request #3 from anthropics/xiprime-pairceiling") |
| overlay | `cp -R rh-program/lean/Zeta23/. Zeta23/`; `cp -R rh-program/lean/comparator/. comparator/`; `cp rh-program/lean/Zeta23.lean Zeta23.lean` (`lean/README.md` "Building"); 70 changed/added paths, the 7 topic files new |
| `lean-toolchain` | `leanprover/lean4:v4.33.0-rc2` (upstream pin) |
| `lean --version` | `Lean (version 4.33.0-rc2, arm64-apple-darwin24.6.0, commit d8b18978322de05a8f3dba51ef03cf5461676c17, Release)` |
| `lake --version` | `Lake version 5.0.0-src+d8b1897 (Lean version 4.33.0-rc2)` |
| Mathlib | `51e6992efd06126df61a496bebf8f49482a4e129`; `lake exe cache get`: "No files to download", 8489 decompressed; no Mathlib module compiled in any later build |
| comparator tool chain | comparator `fe1222e2…5d08`, lean4export `de4ffedf…7775`, nanoda_bin `d6c87133…48bb`, fake-landrun.sh `167507c8…8e4f` — each SHA-256 appears in `results/d1-m2a/packaging/COMPARATOR-RUN.md` (checked, `10-comparator.log` header) |
| host | macOS 27.0, arm64; Python 3.9.6 |

Comparator runs are NOT sandboxed (the fake-landrun shim; Landlock does not exist on macOS), as in every prior record; the
`WARNING: THIS IS NOT REAL LANDRUN!` line appears once per sandboxed step.

## §2 Commands and logs (every log under `results/iv17-lean-s30/check-O/`)

| # | command (in the clone unless stated) | log | result |
|---|---|---|---|
| 1 | `git clone …zeta-23-lean checker-clone-s30b` (retry loop ×30), `git checkout v1.0`, `git rev-parse HEAD` | `01-clone.log` | `3635e748…` |
| 2 | the three `cp` of the overlay; `git status --short` | `02-overlay.log` | 70 paths; 7 topic files new |
| 3 | `lake exe cache get` (retry loop); versions | `03-cache-get.log` | Mathlib `51e6992e`, no download |
| 4 | `lake build Zeta23.PairCeiling.GridParsevalRat` | `04-build-…GridParsevalRat.log` | *(2081 jobs)*, built GridParseval 2.4 s, GridCorner 1.5 s, GridParsevalRat 1.4 s; 0 warnings |
| 5 | `lake build Zeta23.PairCeiling.GridGap` | `05-build-…GridGap.log` | *(2082 jobs)*, GridGap 1.3 s (the three ℚ `decide +kernel` facts on `ZMod 65` included); 0 warnings |
| 6 | `lake build Solution.IntegralityGap` | `06-build-Solution.IntegralityGap.log` | *(8702 jobs)*, ChallengeDeps 3.6 s, Solution 3.0 s; 0 warnings |
| 7 | `lake build Challenge.IntegralityGap` | `07-build-Challenge.IntegralityGap.log` | *(8698 jobs)*; exactly 16 `declaration uses 'sorry'` warnings (lines 51, 61, 67, 73, 79, 83, 87, 92, 96, 104, 112, 120, 127, 131, 135, 139) |
| 8 | `lake env lean comparator/PrintAxioms/IntegralityGap.lean` | `08-print-axioms.log` | §3 |
| 9 | runner = the builder's `tools/run.sh` with only the tree path and the comment line changed (`09a-runner-diff.log`); every `.lake/build` file matching `*IntegralityGap*` removed (28 files; 0 remaining) | `09a-…`, `09b-prerun-cleanup.log` | — |
| 10 | `check-O/run-check.sh comparator/config-integrality-gap.json` | `10-comparator.log` | exit **0** (§4) |
| 11 | `python3 check-O/identity_check_o.py . IntegralityGap comparator/config-integrality-gap.json`; `python3 tools/statement_identity_g8.py <clone> IntegralityGap <16 names as 16 words>`, and the same on `rh-program/lean` | `11-statement-identity.log` | PASS ×3 (§5) |
| 12 | `python3 tools/trust_greps_g8.py . <6 files>`; raw `grep -nwE` of 20 words over the 6 files + config; `cmp` clone vs tree | `12-trust-greps.log` | §5 |
| 13 | `lake env lean check-O/probe_checker.lean` | `13-probe-checker.log` | exit 0 (§7) |
| 14 | `python3 check-O/defs_diff_o.py .`; `lake env lean check-O/probe_defeq.lean` | `14-trusted-defs-diff.log` | 6/7 byte-identical, 7/7 `rfl` (O1) |
| 15 | `git diff dcd1c4f -- results/a4-no-go/formalization-status.md` (from the `riemann` repository root) and a prefix `cmp` | `15-formalization-status-diff.log` | append-only (§8) |
| 16 | `lake env lean check-O/probe_rowform.lean` | `16-probe-rowform.log` | exit 0 (§6, (v4)) |
| 17 | `cd results/d1-m2a/dr8 && python3 validate_yaml_sigma_strong.py`; a supplementary name check | `17-yaml-validation.log` | PASS, 0 errors, 0 undeclared |
| 18 | 10(g) lint (British spellings, banned phrases) over the unit's text | `18-lint-10g.log` | clean (the hits are `pointwise`/`likewise` false positives) |
| 19 | rational statements against their integer originals (text, substitution map) | `19-rat-vs-int-statements.log` | §6 |
| 30 | `shasum -a 256 -c` of `hashes.txt`; `hashes.txt`, BUILD-NOTES, BRIEF, SHARED; clone overlay vs listed hashes | `30-hashes.log` | §9 |

Superseded passes kept in the logs, marked "RERUN": in `11-` my own identity script first crashed on a capturing group in its
`re.split` (my bug, fixed); in `17-` my supplementary name check reports the two FILE names `GridGap.lean`/`GridParsevalRat.lean` as
"MISSING" (my regex; annotated in the log). None is a finding about the unit.

## §3 `#print axioms` (verbatim, `08-print-axioms.log`)

```
'trace_sq_grid_rat' depends on axioms: [propext, Classical.choice, Quot.sound]
'gridRowQ_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'gridRow_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'gridRow_eq_gridRowQ' depends on axioms: [propext, Classical.choice, Quot.sound]
'fracMark_mass' depends on axioms: [propext, Classical.choice, Quot.sound]
'fracMark_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'fracMark_Nd' depends on axioms: [propext, Classical.choice, Quot.sound]
'fracMark_row' depends on axioms: [propext, Classical.choice, Quot.sound]
'mi_fails_rational' depends on axioms: [propext, Classical.choice, Quot.sound]
'corner_fails_rational' depends on axioms: [propext, Classical.choice, Quot.sound]
'corner_bound_fails_rational' depends on axioms: [propext, Classical.choice, Quot.sound]
'mi_holds_integer' depends on axioms: [propext, Classical.choice, Quot.sound]
'per_atom_slack' depends on axioms: [propext, Classical.choice, Quot.sound]
'per_atom_slack_fails_rational' depends on axioms: [propext, Classical.choice, Quot.sound]
'per_atom_floor' depends on axioms: [propext, Classical.choice, Quot.sound]
'per_atom_floor_fails_rational' depends on axioms: [propext, Classical.choice, Quot.sound]
exit=0
```

The PrintAxioms file imports `Solution.IntegralityGap` only, so these are the solution's constants. **The `decide +kernel` facts and
their axioms** (`13-probe-checker.log`): `Zeta23.PairCeiling.GridGap.fracMark_mass`, `fracMark_sq`, `fracMark_Nd` each print
`[propext, Classical.choice, Quot.sound]`; so does the non-kernel `fracMark_nonneg`; and so do GridCorner's `attainMark_mass`,
`attainMark_sq` at this toolchain (O2). No `Lean.ofReduceBool` anywhere, so no `native_decide` in any closure.

## §4 Comparator run (exit code)

| run | config | start – end (IST) | wall | lines | exit |
|---|---|---|---|---|---|
| 1 | `comparator/config-integrality-gap.json` (16 names; permitted `propext`, `Quot.sound`, `Classical.choice`; `enable_nanoda: true`) | 01:12:50 – 01:13:21 | 30.72 s, max RSS 5.85 GB | `Built ChallengeDeps.IntegralityGap (2.9s)` (rebuilt by the comparator itself — I had removed it), `Built Challenge.IntegralityGap (2.0s)` + its 16 `sorry` warnings, the export of the 16 names from `Challenge.IntegralityGap`, `Built Solution.IntegralityGap (3.0s)`, the export from `Solution.IntegralityGap`, `Running nanoda kernel on solution`, `Nanoda kernel accepts the solution`, `Lean default kernel accepts the solution`, `Your solution is okay!` | **0** |

What this establishes: each solution statement coincides, constant for constant, with its challenge namesake (both built over the one
trusted `ChallengeDeps.IntegralityGap`); the proofs use no axiom outside the three; nanoda re-checked the solution export and Lean's
kernel replayed it.

## §5 Statement identity and trust greps

`11-statement-identity.log`: my `identity_check_o.py` (comments stripped, declarations split, whitespace normalized) — imports:
`ChallengeDeps` ← `Mathlib` only; `Challenge` ← `ChallengeDeps.IntegralityGap` only; `Solution` ← `ChallengeDeps.IntegralityGap` and
`Zeta23.PairCeiling.GridGap` (never the challenge). Challenge and solution each contain exactly 16 declarations, all `theorem`; the
config's `theorem_names` equal the challenge's names in order (True, 16); the trusted file declares exactly the 7 `def`s; 16/16
statements IDENTICAL; every challenge proof is exactly `by sorry`; every solution proof is a one-line delegation to
`Zeta23.PairCeiling.{GridParsevalRat, GridCorner, GridGap}`. The builder's `statement_identity_g8.py` (byte comparison), given the
sixteen names as sixteen words: PASS on the clone and PASS on `rh-program/lean`.

`12-trust-greps.log`: the builder's `trust_greps_g8.py` (nine words, comments stripped) over the six topic Lean files: 16 hits, all
`sorry`, all in `Challenge/IntegralityGap.lean` (lines 58–140; exit 1 is the script's hit-count convention). My raw grep (comments
INCLUDED) over the six files + config for `axiom|native_decide|unsafe|implemented_by|extern|opaque|sorry|admit|ofReduceBool|decide|macro|
elab|set_option|attribute|instance|local|private|noncomputable|Lean.|@[`: the 16 challenge `sorry` lines, four `noncomputable section`
lines, the three `decide +kernel` lines of GridGap (112, 115, 119), and comment mentions in headers/docstrings — nothing else; no
`set_option`, no attribute, no instance. `cmp`: the seven topic files in the clean clone are byte-identical to `rh-program/lean/`, and the
clone's `GridParseval.lean`/`GridCorner.lean` (program overlays, untracked at v1.0) are byte-identical to the builder's s21 tree.

## §6 The statements against the record

The record, read at the line: zoo IV.17 (`BARRIER-ZOO.md` line 551 ff.) STATEMENT, EXECUTABLE TEST (1) and (3), and the 2026-09-10
repair note; `results/a4-no-go/theorems.md` Lemma 2.2 (line 169) and Theorem 2.3; `paper.md` §2.4 (line 138, the realizability paragraph:
"with fractional marks even the 5/6 baseline is false: mass N of mark-4/3 atoms on the grid of Theorem 3.9 has F1 = (4/3) N budget-tight
and N_d = (3/4) N < (5/6) N") and §4.2 (line 397 ff.: (MI), "Note S2 ≥ T for integer marks (per zero, m² − (3m − 2) = (m − 1)(m − 2) ≥
0)", Prop. 4.5, the integrality-gap Reading; grid g_k = k·64/65, i.e. 65 sites); formalization-queue item 10 (`BARRIER-ZOO.md` line 665).
The BRIEF §0 quotes match these lines.

**Lemma 2.2(a), re-derived by me.** For an integer m: if m ≤ 1, both m − 1 ≤ 0 and m − 2 < 0, so (m − 1)(m − 2) ≥ 0; if m ≥ 2, both
factors are ≥ 0. So (m − 1)(m − 2) ≥ 0 for EVERY integer (equality iff m ∈ {1, 2}), i.e. m² − 3m + 2 ≥ 0, i.e. 3m − m² ≤ 2. At an empty
site (m = 0) 3m − m² = 0 = 2·[m ≠ 0]. Summing over the M sites: 3Σm − Σm² ≤ 2·#{k : m_k ≠ 0} = 2N_d, which is Lemma 2.2(a)
(N_d ≥ (3N − Σm²)/2) and the paper's S2 ≥ T; on the grid F1 = Σm² (Thm 3.9) turns it into (MI) F1 ≥ 3M − 2N_d. The per-site identity
2 − (3q − q²) = (q − 1)(q − 2) holds for every q, so the per-site (MI) is EQUIVALENT to the slack at that site — for rationals too; over
ℚ it fails exactly for 1 < q < 2. Hence the slack is exactly the line where integrality is consumed. Lean confirms both halves (§7).

**The counterexample arithmetic, by hand.** 48 atoms × 4/3 = 64 = N (mass). Σm² = 48 × 16/9 = 768/9 = 256/3, and (4/3)·64 = 256/3, so F1 =
(4/3)N exactly: budget-tight at ε = 0 (the zoo's "(3/4)N·(16/9) = (4/3)N": (3/4)·64 = 48 ✓). N_d = 48 = (3/4)N. (MI) would demand F1 ≥
3·64 − 2·48 = 96 = (3/2)N (the zoo's "3N − (3/2)N"), and 96 > 256/3 ≈ 85.33, so (MI) fails; in the Lean form 3Σm − Σm² = 192 − 256/3 =
320/3 ≈ 106.67 > 96 = 2N_d. The corner: 64·(5/6 − 0) = 160/3 ≈ 53.33 > 48 = N_d. The slack at 4/3: (1/3)(−2/3) = −2/9 < 0. The floor at
1/2: 1/4 < 1/2. The grid: N + 1 = 65 = 2n + 1 with n = 32, the paper's g_k = k·64/65. `checker_arith` (probe) re-checks all thirteen
equalities/inequalities in Lean by `norm_num`.

**Each statement** (file `lean/comparator/Challenge/IntegralityGap.lean`, read line by line; the trusted file read in full):
* `trace_sq_grid_rat`, `gridRowQ_eq`: **genuinely the same identity with rational marks** — `19-rat-vs-int-statements.log`: the texts of
  `trace_sq_grid_rat`, `grid_parseval_decoupling_rat` and `gridRowQ_eq` are byte-identical (whitespace-normalized) to GridParseval's
  `trace_sq_grid`, `grid_parseval_decoupling` and GridCorner's `gridRow_eq` after the map ℚ→ℤ, `dftMarkQ`→`dftMark`, `gridRowQ`→`gridRow`.
  The marks are quantified over ALL of `ZMod (2n+1) → ℚ` — genuinely rational, not cast integers; `fracMark_row` uses it at 4/3. The
  flat-band lemma differs only in its coefficient ring (a field `F` for ℚ marks, a domain `K` for ℤ marks), the typing fact item 10 asked
  to be checked (TYPING-NOTE §2; FIDELITY (v7)). The proof (GridParsevalRat §1) is the integer proof with a general coefficient vector
  `v k` for `(m k : K)`, and `map_ratCast` for `map_intCast` — I read it through; it uses no property of the marks.
* `gridRow_eq`, `gridRow_eq_gridRowQ`: the integer row, and the integer row IS the rational row of the cast marks — so both halves of the
  topic sit on one row. Right.
* `fracMark_mass`, `fracMark_sq`, `fracMark_Nd`, `fracMark_row`: exactly the zoo's/item 10's numbers (above). `fracMark` = `if k.val < 48
  then 4/3 else 0` on `ZMod 65`: 48 distinct sites (0…47), 17 empty. Right.
* `mi_fails_rational`: the brief's statement character for character; `mi_holds_integer`'s statement at M = 65 with ℚ for ℤ. The
  hypothesis `∀ k, 0 ≤ m k` sits inside the negated universal — it weakens the universal and so STRENGTHENS the negation. Right.
* `corner_fails_rational`: every hypothesis of `grid_corner_pointwise` (whose signature I printed: marks ≥ 0, `Σ m = N`, `gridRow n m ≤
  4/3·N·(1+ε)`) at n = 32, N = 64, ε = 0, with ℚ for ℤ, plus the strict negation of its first conclusion `N·(5/6 − 2/3·ε) ≤ N_d`. Right.
  `corner_bound_fails_rational`: the same as a negated universal; its extra hypotheses (mass, budget) again only strengthen it. Right.
* `mi_holds_integer`: `two_mul_distinct_ge`'s statement with its section variables `{M} [NeZero M]` bound explicitly — the same
  telescope; re-exported by `two_mul_distinct_ge m hm`, and the solution's `fun _ _ m hm => …` typechecks against the challenge's
  `∀ (M : ℕ) [NeZero M] …`. **Faithful.** Over "every grid" `ZMod M`, not only odd M — stronger than the grid class.
* `per_atom_slack` (∀ m : ℤ — stronger than Lemma 2.2(a)'s m ≥ 1), `per_atom_floor` (∀ m : ℤ, m ≤ m² — the floor m² ≥ m), and their ℚ
  failures at 4/3 and 1/2: the two devices IV.17 STATEMENT and TEST (3) name, each a named theorem. Right.
* **Hypotheses the prose does not state: none.** The positive theorems carry only `0 ≤ m` (the prose's nonnegative marks; empty sites are
  0 — FIDELITY (v5)); the negations' extra hypotheses strengthen them. No hypothesis is hidden in a definition: the seven trusted
  definitions are plain `def`s over Mathlib and are, as constants, the Zeta23 originals (O1).

**(v4), checked in Lean.** The paper's row form of (MI): `checker_mi_row_integer` (for all n and nonnegative integer marks,
3Σm − 2N_d ≤ `gridRow n m`) and `checker_mi_row_fails_rational` (¬ ∀ nonnegative rational m on `ZMod 65`, 3Σm − 2N_d ≤ `gridRowQ 32 m`)
each follow in two lines from the topic's own Comparator-checked statements, imported from `Solution.IntegralityGap`
(`16-probe-rowform.log`, both on the three axioms). So "(MI) holds over ℤ and fails over ℚ on the same Frobenius row" is true in the
row form too, as (v4) says.

**FIDELITY.md, row by row.** "Covered" (§1): 16 rows, each naming a theorem present in the challenge file with exactly the stated
content — 16/16 CLEAN. "Not covered" (§2): laws — true (no law appears; the pointwise negation gives the one-column law's at once;
`grid_corner_law` exists at GridCorner.lean 162); the pair channel — true (no pair, depth or ā in any statement; Prop. 4.5's formula and
−3.520·10⁻² match paper §4.2 and the zoo); other budgets — true (only the λ = 1 symmetric band; GridWitness's half-band row exists and is
not used); off the grid — true (GridCorner's header, lines 47–48, records Lemma 2.1 unformalized); ℚ positive corner forms — true (none
stated); ζ — true. "Differs" (§3) (v1)–(v8) and "Naming": each true as stated ((v2)'s "under two seconds" — GridGap built in 1.3 s here
too; (v6) confirmed by the probe; (v8) confirmed, O2). §4's character-for-character list — see O1.

**The label, word for word.** "IV.17's master inequality is a Comparator-checked theorem over integer marks" — `mi_holds_integer`,
comparator exit 0 (§4); "and a Comparator-checked FALSEHOOD over rational marks" — `mi_fails_rational` (and the corner forms), same
run; "on the same Frobenius row" — `gridRow_eq`, `gridRowQ_eq`, `gridRow_eq_gridRowQ` in the topic, and the row forms re-derived above;
"(the mark-4/3 instance kernel-checked)" — the instance's three column facts are `decide +kernel`, and the whole topic was replayed by
two kernels; "over Mathlib alone" — the trusted layer imports `Mathlib` only and the challenge imports only it (§5); "no displayed
hypothesis" — none (above); "axioms propext/Classical.choice/Quot.sound" — §3; "replayed by nanoda" — `Nanoda kernel accepts the
solution` (§4). "The pair channel stays unformalized, and the label says so" — BUILD-NOTES states it beside the label, the challenge's
WHAT IS NOT paragraph says "nothing about the PAIR CHANNEL (paper Prop. 4.5 is not formalized — paper-certificate grade, item 10)", and
FIDELITY §2 repeats it. **Earned.** F1 and F2 do not touch it. The refutation-shaped close's "the line where integrality is consumed is
the named theorem `per_atom_slack`" is earned in content (§7); only F2's docstring overstates the mechanism.

## §7 Probes (`13-probe-checker.log`, `14-trusted-defs-diff.log`, `16-probe-rowform.log`; all exit 0, all on the three axioms)

* `checker_mi_of_slack {M} [NeZero M] (m : ZMod M → ℚ) (hm : ∀ k, 0 ≤ m k) (hs : ∀ k, 0 ≤ (m k − 1)(m k − 2)) : 3Σm − Σm² ≤ 2·N_d` — (MI)
  from the slack alone, over ℚ, no integrality. (The unused-variable lint on `hm` is itself informative: nonnegativity is not needed.)
* `checker_mi_integer_via_slack` — `two_mul_distinct_ge`'s statement proved from `checker_mi_of_slack` applied to the cast marks, with
  `GridGap.per_atom_slack` as the only integrality input.
* `checker_pointwise_identity : 2 − (3q − q²) = (q − 1)(q − 2)` (`ring`); `checker_arith` — the thirteen numbers of §6.
* `@IntegralityGap.X = @Zeta23….X := rfl` for all seven trusted definitions.
* `checker_mi_row_integer`, `checker_mi_row_fails_rational` — (v4).

## §8 `results/a4-no-go/formalization-status.md`

`15-formalization-status-diff.log`: the file's history is 09c2622 (2026-08-27, created), dcd1c4f (2026-08-28 00:18, the last edit before
this session), e6306cb (2026-09-29 01:02, this session's autocommit of the builder's edit). `git diff dcd1c4f` shows 26 lines added, 0
removed, one hunk at the end (`@@ -133,3 +133,29 @@`); the first 135 lines of the current file are byte-identical to dcd1c4f's 135.
**The 2026-08-27 record (as last edited 2026-08-28) is untouched; the addendum is dated and append-only.** Its content matches the unit,
except the "kernel-checked by `decide +kernel`" clause (F1). Two small readings, not findings: "the second integrality level of the
Remark above" refers to `theorems.md` Lemma 2.2's Remark (not a remark in this file); "the pair channel (Section 4.3, Prop. 4.5)" —
Prop. 4.5 is in paper §4.2 and the channel's closure in §4.3, matching the file's own line 102.

## §9 Hashes (`30-hashes.log`)

`shasum -a 256 -c` over `hashes.txt`: **28/28 OK, 0 mismatch** — the 7 topic Lean/config files, `lean/formalization.yaml`,
`lean/README.md`, `results/a4-no-go/formalization-status.md`, and the 18 files under `results/iv17-lean-s30/`. `hashes.txt` itself =
`7f74bc0e0ed3f94abe3e01b0b7536afb8142dd11e44c388534884324ceb6e204` and `BUILD-NOTES.md` = `a3c3bd69…b728`, both the values in the builder's
final SHARED block; `BRIEF.md` = `9aabf0db…2ffd70`, as BUILD-NOTES states. The 7 topic files in the clean clone match the listed
hashes. `SHARED.md` before my block: `0dfa0e3629395dff462356e05f4a0f9102bdf85f6eafb2411d9764b32a8a8554`.

| file | listed = recomputed |
|---|---|
| `lean/Zeta23/PairCeiling/GridParsevalRat.lean` | `d1b3bb7c…fa13` ✓ |
| `lean/Zeta23/PairCeiling/GridGap.lean` | `78c37aa6…c04d` ✓ |
| `lean/comparator/ChallengeDeps/IntegralityGap.lean` | `e99d4e72…0c43` ✓ |
| `lean/comparator/Challenge/IntegralityGap.lean` | `eb3293b9…5323` ✓ |
| `lean/comparator/Solution/IntegralityGap.lean` | `eb3326ab…bfac` ✓ |
| `lean/comparator/PrintAxioms/IntegralityGap.lean` | `131300be…f78f` ✓ |
| `lean/comparator/config-integrality-gap.json` | `360c50e6…c2b5` ✓ |
| `lean/formalization.yaml`, `lean/README.md` | `ab9e7bc5…c735`, `1982befd…533d` ✓ |
| `results/a4-no-go/formalization-status.md` | `b6e26ac7…c610` ✓ |
| 18 files under `results/iv17-lean-s30/` (BRIEF, TYPING-NOTE, typing-probe, zeta23-axioms, FIDELITY, 10 logs, 3 tools) | 18/18 ✓ (full list in the log) |

## §10 What the orchestrator should do

Apply F1 (GridGap.lean lines 40–42; formalization-status.md addendum lines 150–151) and F2 (GridGap.lean line 93) — comment/prose only.
Then `lake build Zeta23.PairCeiling.GridGap Solution.IntegralityGap`, remove the topic's artifacts, rerun the comparator on
`config-integrality-gap.json` once, and rehash `GridGap.lean`, `formalization-status.md`, and `hashes.txt`. (Or, without touching Lean,
record both corrections in FIDELITY.md.) Optionally add O1's qualifier to FIDELITY §4. Do not edit the trusted or challenge files. The
unit then stands with its label as earned: (MI) is a theorem over ℤ and a falsehood over ℚ on the same kernel-checked row, and the slack
is exactly where integrality is consumed. Nothing about ζ or RH follows.


## §11 [ORCHESTRATOR, 05:44 IST 2026-09-29, Session 32 — the sponsor's Linux replay: the fourth kernel replay of this unit, on a second OS, with the sandbox exercised for the first time]

Delivered by the sponsor as `~/Downloads/rh-linux-check-s30-logs.zip` (SHA-256 ab5b3b37f05ea2ee77109004c879dbe8b1633b9c1439ba685cc2e5396f99a816), unpacked to `results/linux-check-s30/` (26 files). Host: Ubuntu, kernel 7.0.0-34-generic, x86_64, 12 cores, 37 GB (`00-main.log` line 2). Three runs (`NOTE-linux-run.md`): run 1 (01:55 IST) installed and built everything and passed the first config, then the script stopped — re-derived at `scripts/linux-comparator-check.sh` lines 91–92 as shipped: the per-config block is a brace group `{ …; exit $rc; } > "$L"`, which runs in the current shell, so `exit $rc` ended the whole script after the first config with status 0 (a packaging error of Session 30, ours); the Linux session's fix (`fixed-script/linux-comparator-check.diff`: the brace group made a subshell; a second landrun test with the comparator's own flags) is adopted into `scripts/linux-comparator-check.sh` this session. Run 3 (05:35–05:38 IST) is the run of record. Lean 4.33.0-rc2 (x86_64-unknown-linux-gnu, commit d8b18978), Mathlib 51e6992efd — the Mac's first-build pair. Zeta23 replay build `Build completed successfully (9153 jobs)`; the only flagged lines are two warnings, a Mathlib deprecation at `Zeta23/XiPrime/FamilyHypsV.lean:276` and an unused-variable linter note at `Zeta23/XiPrime/ExplicitFormula/EntryError.lean:121`; no error. **Sandbox:** the script's strict test FAILS — `09-landrun-test.log`: "Got Landlock ABI v8, wanted {Landlock V9; FS: all; Net: all; Scoped: all}" — i.e. the pinned landrun build (811cfff, v0.1.18) asks for ABI v9 by default and this kernel supports v8 (`fixed-script/landlock-abi-probe.txt`: a direct `landlock_create_ruleset` version query prints 8); but the comparator invokes landrun with `--best-effort --ro / --rw /dev -ldd -add-exec` on every sandboxed step, and under those flags the sandbox is REAL: `09b-landrun-best-effort-test.log` shows a sandboxed child refused ("Permission denied") when writing outside the allowed paths, and each `11-comparator-*.log` contains ZERO `NOT REAL LANDRUN` lines (the summary's `fake-landrun warnings: 0`). So this is the first record in the program on which the Comparator's sandbox was exercised (Landlock ABI v8, best-effort mode; every prior record ran the fake-landrun shim — `COMPARATOR-RUN.md` §2). Tool hashes (`10-tool-hashes.txt`) differ from the Mac's, as `scripts/README-LINUX-CHECK.md` says they will (different OS and CPU; source revisions pinned by commit). Wall time per comparator run 35.5–51.1 s; peak RSS 7.20–7.24 GB. **This unit:** `comparator config-integrality-gap.json: PASS (exit 0; nanoda: 1; fake-landrun warnings: 0)` (`99-summary.txt`; `11-comparator-config-integrality-gap.log`: "Nanoda kernel accepts the solution", "Lean default kernel accepts the solution", "Your solution is okay!", `--- comparator exit code: 0 ---`, wall 35.53 s); `04-print-axioms-IntegralityGap.log`: 16 names (`trace_sq_grid_rat` … `per_atom_floor_fails_rational`), every one `[propext, Classical.choice, Quot.sound]`, `sorryAx: 0` — the same 16 names and axioms as row 3 of this record. **What changes:** nothing in the label; the record gains the sentence "replayed on Linux with a real Landlock sandbox (ABI v8, best-effort), 2026-09-29". The pair channel stays unformalized. Nothing about ζ or RH follows. Files and hashes: `results/linux-check-s30/` (26 files), listed in this unit's `hashes.txt` addendum of this date.
