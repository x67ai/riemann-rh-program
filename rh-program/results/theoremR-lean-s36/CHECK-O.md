# THEOREM R's ARITHMETIC CORE — CHECK-O, the Opus 5.5 clean-clone check of the Comparator topic `ResidueRank` (Session 36; UNIT-BRIEF §3; KICKSTART 10(f), 10(j))

Checker: Opus 5.5, started Wed Sep 30 17:47 IST 2026 (machine clock). Contract: `results/theoremR-lean-s36/UNIT-BRIEF.md` §3 (SHA-256
`60b131b3353f944b101bca54609cd07f591fad4c20618fab5387b6a03d42068e`, recomputed, equal to the value BUILD-NOTES quotes); typing probe
`typing-probe.lean` `881e024a9184e9e4aab0976e42a31f1d8f8f5f01b3cec10c773a00f236601a81` (equal to BUILD-NOTES'). Sources read for the
mathematics: `results/beta-shapes-s35/NOTE.md` §1.1, §2.0, §2.3 (SHA-256 `49eb8e12…`), `results/beta-shapes-s35/read-O.md` §2.2, §2.5
(`1614bcbb…`). Precedent for the procedure: `results/h4-pair-lean-s33/CHECK-O.md` and its `check-O/` scripts. The builder's tree
`~/rh-lean-work/checker-clone-s33-h4` was never used for a build or a run here. Every log below is under
`results/theoremR-lean-s36/check-O/`. Nothing committed; no Lean file, yaml, README or builder file edited.

(Verdict and the numbered findings: §10, written last.)

## 1. Clean clone, overlay, cache (`check-O/clone.sh`, `clone.log`, `overlay.sh`, `overlay.log`, `cache-get.log`)

`git clone https://github.com/anthropics/zeta-23-lean ~/rh-lean-work/checker-clone-s36-residue` (a NEW directory — the script refuses
an existing one; retry loop), `git checkout v1.0` → HEAD `3635e74826a4c1fcece7d1cd2b6fa75e43a00510` ("Merge pull request #3 from
anthropics/xiprime-pairceiling", the same commit as the Session-33 checker's v1.0); `lean-toolchain` `leanprover/lean4:v4.33.0-rc2`;
manifest Mathlib `rev` = `inputRev` = `51e6992efd06126df61a496bebf8f49482a4e129`. `lake exe cache get` (17:48–17:50 IST): "Decompressed
8489 already-cached file(s) … Completed successfully in 10489 ms"; the checked-out `.lake/packages/mathlib` HEAD is `51e6992e…`. Mathlib
was never compiled from source.

**Overlay — exactly the seven unit files, nothing else** (`overlay.sh`: `cp` then `cmp` against `rh-program/lean/`, each OK): the program
modules `Zeta23/ResidueRank/{LogPrimes,Pair,GenusBound}.lean` and the topic files `comparator/{Challenge,Solution,PrintAxioms}/ResidueRank.lean`,
`comparator/config-residue-rank.json`. None pre-existed in v1.0. `git status --short` after the overlay: five `??` entries (the new
directory `Zeta23/ResidueRank/` and the four topic files) and nothing modified. The import closure needs nothing more: `LogPrimes` and
`GenusBound` import `Mathlib` only, `Pair` imports `Zeta23.ResidueRank.LogPrimes`, the challenge `Mathlib`, the solution `Pair` +
`GenusBound`, the print-axioms file `Solution.ResidueRank`. The root `Zeta23.lean` was not touched (the unit adds no root import;
BUILD-NOTES §1 says why), so the modules are built by name.

## 2. Cold builds, one `lake` at a time (`check-O/build.sh`, `build-{logprimes,pair,genusbound,solution,challenge}.log`)

Each build started only after the previous `lake` exited (the script logs `pgrep -x lake` = 0 before each start).

| build (sequential) | result | module line | wall / max RSS |
|---|---|---|---|
| `lake build Zeta23.ResidueRank.LogPrimes` (17:50:40) | *Build completed successfully (8697 jobs)*, rc 0, 0 errors, 0 warnings | `Built Zeta23.ResidueRank.LogPrimes (6.3s)` | 9.36 s / 5.88 GB |
| `lake build Zeta23.ResidueRank.Pair` (17:51:04) | 8698 jobs, rc 0, 0 warnings | `Built Zeta23.ResidueRank.Pair (3.4s)` | 5.65 s / 5.87 GB |
| `lake build Zeta23.ResidueRank.GenusBound` (17:51:10) | 8697 jobs, rc 0, 0 warnings | `Built Zeta23.ResidueRank.GenusBound (7.7s)` | 9.95 s / 5.90 GB |
| `lake build Solution.ResidueRank` (17:51:25) | 8700 jobs, rc 0, 0 warnings | `Built Solution.ResidueRank (3.3s)` | 5.54 s / 5.85 GB |
| `lake build Challenge.ResidueRank` (17:51:31) | 8697 jobs, rc 0, **exactly 8 warnings, each "declaration uses `sorry`"**, at lines 51, 57, 65, 72, 81, 93, 103, 110 — the eight `theorem` lines | `Built Challenge.ResidueRank (3.3s)` | 5.64 s / 5.85 GB |

The job counts equal BUILD-NOTES §5's expectation (8697 / 8698 / 8697 / 8700). (The max RSS is Mathlib's oleans mapped by `lake`, as in
every prior record.) One procedural slip of this checker, repaired: the first call of `build.sh` passed a RELATIVE log path, so
`build-logprimes.log` was written into the clone's root; it was moved into `check-O/` at once (no other effect; `git status` of the clone
is otherwise the overlay's).

## 3. `#print axioms` for every name (`check-O/print-axioms.log`, `program-axioms-checker.lean`, `sorry-control.{lean,log}`)

* `lake env lean comparator/PrintAxioms/ResidueRank.lean` in the clean clone (17:51:59), rc 0 — the eight topic names:

| name | axioms |
|---|---|
| `ResidueRank.log_primes_linearIndependent` | `[propext, Classical.choice, Quot.sound]` |
| `ResidueRank.span_log_not_finite` | `[propext, Classical.choice, Quot.sound]` |
| `ResidueRank.rank_span_log_le` | `[propext, Classical.choice, Quot.sound]` |
| `ResidueRank.lemmaF_finite_fiber` | `[propext, Classical.choice, Quot.sound]` |
| `ResidueRank.lemmaF_infinite_order` | `[propext, Classical.choice, Quot.sound]` |
| `ResidueRank.theoremR` | `[propext, Classical.choice, Quot.sound]` |
| `ResidueRank.theoremS_bound` | `[propext, Classical.choice, Quot.sound]` |
| `ResidueRank.theoremS` | `[propext, Classical.choice, Quot.sound]` |

* The checker's own probe, GENERATED from every `def`/`theorem` line of the three program modules (27 names: `LogPrimes` 2 defs + 14
  theorems, `Pair` 8, `GenusBound` 3 — the same 27 the builder's `program-axioms.lean` lists, so the builder's "all 27 program-side
  declarations" is the whole of the three files): 27 lines, each `[propext, Classical.choice, Quot.sound]`, rc 0.
* `sorryAx`: 0 hits; `Lean.ofReduceBool` / `Lean.trustCompiler`: 0 hits.
* **Negative control** (`sorry-control.lean`): the same `#print axioms` on the CHALLENGE module prints `[propext, sorryAx,
  Classical.choice, Quot.sound]` for three of its names — the probe does detect a `sorry` when one is present.
* **Result: clean.** Every topic name and every program declaration uses exactly the three standard axioms.

## 4. Statement identity (`check-O/identity_checker.py`, `statement-identity.log`; `brief-elab-check2.{lean,log}`)

The checker's own script (extraction: the docstring above `theorem <name>` plus the text from `theorem <name>` to the first `:=`; the
builder's `tools/statement_identity_s36.py` was neither run nor read):
* [A] challenge = solution, byte for byte (docstring + statement), 8/8, in the clean clone AND in `rh-program/lean` (and the two copies
  of each file are `cmp`-identical, [F] 7/7).
* [B] challenge = typing probe `results/theoremR-lean-s36/typing-probe.lean`, byte for byte, 8/8.
* [C] the challenge from the LINE `import Mathlib` to EOF = the probe from its `import Mathlib` line to EOF: 3536 bytes, identical; the
  challenge and the probe each have exactly one import line, `import Mathlib`. (First run of the script: [C] FAILED because it located
  "import Mathlib" by substring and hit the phrase "From `import Mathlib` to the end" in the challenge's header comment — a bug of the
  checker's script, kept as `statement-identity-run1-buggy.log`; the line-anchored re-run passes.)
* [D] against UNIT-BRIEF §0: items 1, 2, 3, 7, 8 are printed in the brief as full backticked statements, and each equals the challenge
  statement after whitespace normalization, character for character. Items 4–6 are printed as prose with backticked fragments; every
  fragment occurs verbatim in the statement except `hA9 : ∀ n, 2 ≤ n → …` (challenge: `∀ n : ℕ, 2 ≤ n → …`) and item 5's `hmul : ∀ a
  b, φ (a * b) = …` (challenge: `∀ a b : ℕ, …`), plus the prose substitution "`cls := φ`". To settle whether those ascriptions change
  anything, `brief-elab-check2.lean` elaborates the brief's LITERAL fragments, assembled into theorem statements, and compares the
  resulting types with the challenge constants: `lemmaF_finite_fiber`, `lemmaF_infinite_order`, `theoremR` — alpha-equal `true`,
  `isDefEq` `true`, all three. (A first form, `brief-elab-check.lean`, elaborated them as `def … : Prop` and found item 6 unequal; the
  cause, located in `brief-elab-diff.log`, is that Lean's `def` elaborator abstracts the `CharZero ℝ` proof inside the `Module ℚ ℝ`
  instance into an auxiliary lemma `brief6._proof_1`, while a theorem statement keeps the proof term inline — an artifact of that probe,
  not of the statement.) So the brief's §0 text, the probe and the challenge denote the same eight terms.
* [E] config: `theorem_names` = `ResidueRank.` + the challenge's names in file order; `permitted_axioms` = `propext`, `Quot.sound`,
  `Classical.choice`; `enable_nanoda: true`; modules `Challenge.ResidueRank` / `Solution.ResidueRank`; no other key.
* RESULT: PASS.

## 5. Trust greps (`check-O/trust_greps_checker.py`, `trust-greps.log`)

The checker's own scan of the seven shipped files in the clean clone (word-bounded; each hit classified CODE or COMMENT with a
nesting-aware comment mask), 28 words — the brief's seven (`axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `opaque`,
`sorry`) plus `admit`, `ofReduceBool`, `decide`, `set_option`, `macro`, `elab`, `syntax`, `partial`, `attribute`, `instance`, `private`,
`noncomputable`, `Challenge`, `sorryAx`, `trustCompiler`, `run_cmd`, `run_meta`, `#eval` and others. Hits IN CODE: the 8 deliberate
challenge `sorry`s (lines 53, 61, 69, 78, 88, 99, 107, 114); the two `noncomputable def`s of `LogPrimes.lean` (`logP`, `expVec` —
`noncomputable` only withholds compiled code, it adds no axiom: both print the three standard axioms, §3); and the config's
`"challenge_module": "Challenge.ResidueRank"` field. Nothing else: no `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`,
`opaque`, `decide`, `set_option`, attribute, macro or instance anywhere in code. The raw `grep -n -w` with comments INCLUDED: `axiom` 2
hits (both in the print-axioms file's header comment: "quick axiom audit", "no other axiom"), `sorry` 9 (the 8 plus the challenge
header's "The `sorry`s below are deliberate"), the other five words 0. Declaration keywords in code: `LogPrimes` 2 `def` + 14
`theorem`, `Pair` 8, `GenusBound` 3, challenge 8, solution 8, print-axioms none. **Imports: the solution imports
`Zeta23.ResidueRank.Pair` and `Zeta23.ResidueRank.GenusBound` only; no file imports `Challenge.*`; the program modules import `Mathlib`
and `LogPrimes` only.** Clean.

## 6. Comparator run with nanoda from the clean clone (`check-O/run-clone.sh`, `cleanup.sh`, `prerun-cleanup.log`, `comparator-run.log`)

Runner: the builder's `tools/run.sh` with exactly two lines changed (the comment line 2 and the `cd` target → the clean clone; the `diff`
is in this session's transcript and reproducible: `diff tools/run.sh check-O/run-clone.sh`). Pre-run cleanup (the builder's
`prerun-cleanup.sh`, same two-line adaptation) removed the 16 comparator-layer artifacts of `Challenge/ResidueRank` and
`Solution/ResidueRank` under `.lake/build/{lib/lean,ir}`, "remaining: 0" (the program modules stay built — the untrusted side either
way); there is no ChallengeDeps module for this topic. Heavy processes (> 50 % CPU) before the start: none.

| comparator output (17:56:19–17:56:57 IST) | nanoda | Lean kernel | exit | wall / max RSS |
|---|---|---|---|---|
| `Built Challenge.ResidueRank (5.3s)` (the 8 deliberate `sorry` warnings), export of the 8 names + the 29 fixed targets from both modules, `Built Solution.ResidueRank (3.3s)`, `Your solution is okay!` | `Running nanoda kernel on solution` / `Nanoda kernel accepts the solution` | `Running Lean default kernel on solution.` / `Lean default kernel accepts the solution` | **0** | 37.53 s / 5.85 GB |

Tool SHA-256s printed in the log — comparator `fe1222e25fc3…`, lean4export `de4ffedf1412…`, nanoda_bin `d6c87133b59c…`, fake-landrun
`167507c89d8b…` — each occurs once in `results/d1-m2a/packaging/COMPARATOR-RUN.md` §1. Toolchain in the log `v4.33.0-rc2` (commit
d8b18978), Mathlib `51e6992e…`. NOT sandboxed (the fake-landrun shim prints "THIS IS NOT REAL LANDRUN" for each of the five steps), as in
every prior macOS record (COMPARATOR-RUN.md §2); the solution file was read here in full (§5, §7) and imports nothing trusted-side.
What the run establishes: each solution theorem's statement coincides constant for constant with its challenge namesake (all constants
are Mathlib's), the proofs use no axiom outside the three, nanoda re-checked the solution export, and Lean's kernel replayed it.
**PASS, reproduced from the clean clone.**
