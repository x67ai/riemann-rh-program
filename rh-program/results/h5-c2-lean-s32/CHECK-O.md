# H5 — CHECK-O: the Opus 5 clean-clone check of the Comparator topics `WeilContainmentC2One` and `WeilContainmentC2` (Session 32; BRIEF §3; KICKSTART 10(f), 10(j))

Checker: Opus 5, opened Tue Sep 29 06:53:02 IST 2026. Brief `BRIEF.md` SHA-256 `1a2e8a3acb4c6ba0623a9cf91ac515952490d49767717dd4b09af45f5c4e49ab` (recomputed; §7).
Clean clone: `~/rh-lean-work/checker-clone-s32-h5` — a NEW directory, `git clone https://github.com/anthropics/zeta-23-lean`,
`git checkout v1.0` (HEAD `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`), overlay of `rh-program/lean/` by the `lean/README.md` "Building"
recipe (`Zeta23/.`, `comparator/.`, `Zeta23.lean`). The builder's tree `~/rh-lean-work/checker-clone-s21` was not used for any build or
run. Logs of this check: `results/h5-c2-lean-s32/check-O/`. This checker edited no file outside `results/h5-c2-lean-s32/` and committed nothing.

**Verdict: FIX-FIRST — four prose items F1–F4 (§9); the Lean statements, proofs, label and every run are clean.**

## 1. Clone, cache, builds (`check-O/clone.log`, `check-O/cache-get.log`, `check-O/build-c2one.log`, `check-O/build-c2.log`)

* Clone at v1.0: HEAD `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`; `lean-toolchain` = `leanprover/lean4:v4.33.0-rc2`; manifest Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`
  (the checked-out `.lake/packages/mathlib` HEAD equals it). Overlay: `OVERLAY-OK`.
* `lake exe cache get`: "Decompressed 8489 already-cached file(s)", "Completed successfully", exit 0. Mathlib was never compiled from source.
* `lake build Solution.WeilContainmentC2One`: *Build completed successfully (8698 jobs)*, exit 0; the only modules built were
  `ChallengeDeps.WeilContainment` (6.3s) and `Solution.WeilContainmentC2One` (3.3s); 0 lines containing "warning" or "error".
* `lake build Solution.WeilContainmentC2` (after the first, one at a time): *Build completed successfully (8698 jobs)*, exit 0; only
  `Solution.WeilContainmentC2` (3.3s) built; 0 warnings, 0 errors. The builder's figures (8698 jobs each, 0/0) are reproduced.

## 2. #print axioms (`check-O/print-axioms.log`, `check-O/probe_h5.log`)

    'weilContainment_c2_interpolant_log3' depends on axioms: [propext, Classical.choice, Quot.sound]
    'weilContainment_c2_interpolant' depends on axioms: [propext, Classical.choice, Quot.sound]

No `sorryAx`, no `Lean.ofReduceBool`. The configs name one theorem each, so these are every theorem name. The probe
`check-O/probe_h5.lean` (run in the clone) adds: both helper theorems `WeilContainmentC2{,One}.Proof.interpolant` on the same three
axioms; `#check` of `interpolant` shows NO evenness hypothesis (the kernel's confirmation of ERRATA E2 / FIDELITY (D2));
`#print weilContainment_c2_interpolant_log3` shows the body `fun a g x hc hs => WeilContainmentC2One.Proof.interpolant a (Real.log 3) g hc hs`
(the evenness argument is bound and discarded); the brief's rung-1 spelling `∃ k,` (no ascription) is accepted as the type of the shipped
theorem (elaborates to the same term); and the witness is in the class `EF_lit` quantifies over (`ContDiff ℝ 2 k ∧ HasCompactSupport k`,
by `IsCompact.of_isClosed_subset isCompact_Icc (isClosed_tsupport k)`), which is what the headers' "a member of the class Zeta23's
`EF_lit` quantifies over" requires (`EF_lit` read at `Zeta23/ExplicitFormula.lean` line 81 in the clone: `∀ k : ℝ → ℂ, ContDiff ℝ 2 k →
HasCompactSupport k → …`; its prime term, lines 70–73, is `primeSide`'s body character for character).

## 3. Statement identity and trust greps (`check-O/statement-identity.log`, `check-O/brief-identity.log`, `check-O/trust-greps.log`)

* `results/d1-m2a/packaging/statement_identity.py <clone>` (the DBN topic, run as the regression the recipe names): `RESULT: IDENTICAL`, exit 0.
  `results/d1-m2a/packaging/trust_greps.py <clone>` (DBN): 7 permitted challenge placeholders, 0 other code hits, `RESULT: CLEAN`, exit 0.
  Neither tool looks at the H5 topics; the builder's per-topic copies do.
* `tools/statement_identity_h5.py <clone> WeilContainmentC2One weilContainment_c2_interpolant_log3`: 319 = 319 bytes, IDENTICAL, PASS;
  `… WeilContainmentC2 weilContainment_c2_interpolant`: 266 = 266 bytes, IDENTICAL, PASS.
* `tools/trust_greps_h5.py <clone>` with the seven topic files passed as SEPARATE arguments (a zsh array; the builder's first section
  passed them as one word): files present 7; code hits exactly `Challenge/WeilContainmentC2One.lean:46 sorry` and
  `Challenge/WeilContainmentC2.lean:50 sorry` — the two deliberate placeholders, nothing else. Imports (code lines): `ChallengeDeps` →
  `Mathlib`; both challenges and both solutions → `ChallengeDeps.WeilContainment` only; the print-axioms files → their solution. No
  Zeta23 import anywhere.
* The nine topic files in the clone are `cmp`-identical to `rh-program/lean/comparator/` (the overlay is what was checked);
  `ChallengeDeps/WeilContainment.lean` = `47c9a508…` = the D5 `hashes.txt` value (unchanged trusted layer).
* Against BRIEF §0 (`check-O/brief_identity.py`, whitespace-normalized): the family statement is IDENTICAL to §0 "The statement to
  ship". The rung-1 statement DIFFERS from §0 "Rung 1" in exactly one place: the brief writes `∃ k,`, the file writes `∃ k : ℝ → ℂ,`.
  The probe (`check-O/probe_h5.lean`, item (1)) shows the brief's spelling elaborates to the type of the shipped theorem, so the
  theorem is the brief's; the BUILD-NOTES sentence "character for character" is not literally true for rung 1 (item F4).

## 4. Comparator runs with nanoda from the clean clone (`check-O/comparator-c2one.log`, `check-O/comparator-c2.log`)

Runner `check-O/run.sh` = the builder's `tools/run.sh` with only the tree path changed (and its comment line); `diff` shows two lines.
Before each run `check-O/cleanup.sh` removed every comparator-layer artifact of both topics and of `ChallengeDeps.WeilContainment`
(`check-O/prerun-cleanup-c2one.log`, `check-O/prerun-cleanup-c2.log`: "remaining: 0"), so comparator built every comparator-layer
module itself. Tool SHA-256s printed in both logs equal `results/d1-m2a/packaging/COMPARATOR-RUN.md` §1 (comparator `fe1222e2…`,
lean4export `de4ffedf…`, nanoda `d6c87133…`, fake-landrun `167507c8…`). NOT sandboxed (the fake-landrun shim), as in every prior
macOS record.

| config | built by comparator | kernel lines | exit | wall |
|---|---|---|---|---|
| `config-weil-containment-c2-one.json` | `ChallengeDeps.WeilContainment` (2.9s); `Challenge.WeilContainmentC2One` (2.9s) with its one `sorry` warning at 41:8; `Solution.WeilContainmentC2One` (3.3s) | `Nanoda kernel accepts the solution`; `Lean default kernel accepts the solution`; `Your solution is okay!` | `--- comparator exit code: 0 ---` | 67.61 s |
| `config-weil-containment-c2.json` | `ChallengeDeps.WeilContainment` (2.9s); `Challenge.WeilContainmentC2` (2.0s) with its one `sorry` warning at 46:8; `Solution.WeilContainmentC2` (3.3s) | `Nanoda kernel accepts the solution`; `Lean default kernel accepts the solution`; `Your solution is okay!` | `--- comparator exit code: 0 ---` | 68.76 s, max RSS 5.9 GB |

The builder's two runs (`rung1-comparator.log`, `comparator-run.log`) are reproduced from a tree the builder never touched.

## 5. The challenge statements read against BRIEF §0, §1(4) and against FIDELITY.md — every sentence re-derived

**Hypotheses.** `Challenge/WeilContainmentC2.lean` lines 46–49 and `Challenge/WeilContainmentC2One.lean` lines 41–45 display exactly
`(∀ u, g (-u) = g u)`, `Continuous g`, `tsupport g ⊆ Set.Icc (-L) L` (rung 1: `Set.Icc (-(Real.log 3)) (Real.log 3)`) and nothing else;
no `[Fact …]`, no instance argument, no side condition on a or L. The conclusion is the brief's four conjuncts. The only non-Mathlib
constants either statement mentions are `WeilContainment.primeSide` and `WeilContainment.tiltedPrimeSide`, read in the unchanged
trusted file (lines 53–59): `primeSide k = ∑' n, ((Λ n / √n : ℝ) : ℂ) * (k (log n) + k (-log n))` (the prime term of Zeta23's
`literatureRHS`, lines 70–73 of `Zeta23/ExplicitFormula.lean` in the clone, character for character) and
`tiltedPrimeSide a g = ∑' n, (Λ n : ℂ) * ((n:ℝ)^(-a) : ℂ) * g (log n)`.

**Label.** BRIEF §1(4)'s A7 text occurs character for character (after joining wrapped lines) once each in BUILD-NOTES.md, FIDELITY.md,
`lean/README.md`, and twice in `lean/formalization.yaml` (description paragraph and `main_results`) — `check-O/brief-identity.log`.
No file says "IV.1's containment inside `EF_lit`" or anything about ζ or RH beyond "nothing … follows".

**Does anything claim more than "prime-side values; the C² witness is an interpolant at ±log n, not the tilted test; zero side
untouched"?** The two challenge headers, the two solution headers, the yaml description / `main_results` / row (x) / alignment rows,
the README section (lines 433–475), and the D5 (N2) FORMALIZED bracket (`results/d5-lean-s30/FIDELITY.md` line 50) were read in full.
None claims more about the THEOREM. Two sentences claim more than Lean states about NEIGHBORING facts (items F2 and F3 below). The
headers' "a member of the class Zeta23's `EF_lit` quantifies over" is true: `EF_lit` (`Zeta23/ExplicitFormula.lean` line 81) ranges over
`ContDiff ℝ 2 k → HasCompactSupport k`, and the probe derives `HasCompactSupport k` from `tsupport k ⊆ Set.Icc (-L) L` in one line.

### 5.1 FIDELITY §1 (covered) — every claim is a theorem in the file

| FIDELITY claim | verdict |
|---|---|
| (N2) for continuous g, every band: `weilContainment_c2_interpolant` | TRUE — `Challenge/WeilContainmentC2.lean` line 46, proved; comparator PASS |
| the band L = log 3: `weilContainment_c2_interpolant_log3` | TRUE — `Challenge/WeilContainmentC2One.lean` line 41; the solution instantiates the general lemma at `Real.log 3` (probe item (5)) |
| "hypotheses displayed are EXACTLY the three … no H-x anywhere" | TRUE (read above) |
| "every proof is over Mathlib alone … SHA-256 47c9a508…" | TRUE (imports; hash) |
| `#print axioms` = [propext, Classical.choice, Quot.sound] for both | TRUE (§2) |
| comparator PASSED on both topics, exit 0 | TRUE (§4, reproduced) |

### 5.2 FIDELITY §2 (NOT covered) — each sentence re-derived

* **(N1)** TRUE. Neither statement mentions a zero, a zero configuration, an explicit formula, or the archimedean term; the only
  constants beyond Mathlib are the two prime-side functionals.
* **(N2)** The substance is TRUE (the witness is a different function; the statement is existential; nothing says the tilted test is
  C²). Two sentences are FALSE AS WRITTEN — item **F2**: (i) the heading "The tilted test itself is not C²" read as a universal is false:
  g(u) := 2·e^{(a−1/2)|u|}·χ(u), χ any smooth even bump supported in [−L, L], is continuous, even, band-limited, and
  `weilTestOf a g = χ` is C^∞; what is true is D5's own wording, "the tilt does not preserve ContDiff ℝ 2"; (ii) "in general not C¹ at 0
  (`weilContainment_not_contDiff` at a = 1, g ≡ 1)" attributes a C¹ fact to a theorem that states only
  `¬ ContDiff ℝ 2 (weilTestOf 1 (fun _ => 1))` (`Challenge/WeilContainment.lean` line 117). The instance (1/2)e^{−|u|/2} is indeed not
  differentiable at 0 (one-sided derivatives ∓1/4) — a hand fact, not a Lean statement — and D5 CHECK-O F1 corrected exactly this "not
  even C¹" sentence in the D5 ledger (it presupposes g differentiable at 0).
* **(N3)** The substance is TRUE (no Zeta23 import; no statement mentions `EF_lit`; nothing is fed into it). One sentence is FALSE AS
  WRITTEN — item **F1**: "`EF_lit`, `literatureRHS`, `prime_term` do not occur in any of the seven topic files" (FIDELITY.md lines 43–44).
  `check-O/trust-greps.log`, last section: `EF_lit` occurs in comments of `Challenge/WeilContainmentC2.lean` (lines 23, 28 — three
  occurrences) and `Challenge/WeilContainmentC2One.lean` (line 26); `literatureRHS` occurs in comments of
  `ChallengeDeps/WeilContainment.lean` (lines 24, 25, 51), which is one of the seven files the builder's trust-greps list names. In CODE
  (comments stripped) all three names occur zero times. This is the D5 lesson's shape (a ledger sentence false as written, true as meant).
* **(N4)** TRUE, re-derived. g := indicator of {±log 2}, L = log 2: even; `tsupport g` = closure of {±log 2} = {±log 2} ⊆ [−log 2, log 2];
  `tiltedPrimeSide a g` = Λ(2)·2^{−a}·1 = 2^{−a} log 2 ≠ 0 for every real a (only n = 2 has log n ∈ {±log 2}; finitely supported, so the
  tsum is the finite sum). Every continuous k with `tsupport k ⊆ [−log 2, log 2]` has k(±log 2) = 0 (limit from outside), n = 0, 1 give
  Λ = 0, n ≥ 3 give ±log n outside the band, so `primeSide k = 0`. So the family statement with `Continuous g` dropped is false.
  "Continuity … used by the proof exactly once, through 'g = 0 on [L, ∞)'": TRUE at the line — `hc` is consumed only by `eq_zero_of_le`
  (Solution lines 46–57), reached through `tilted_term_zero` → `tilted_eq_sum_interior`.
* **(N5)** TRUE (nothing about the μ-band or any nonlinear function of g is stated).
* **(N6)** TRUE.
* **(N7)** TRUE. The tilted side is a finite sum by `cutoff` (Solution lines 60–74); the witness side is `tsum_eq_sum` over `interior L`
  (line 207) with the off-support terms shown zero (lines 220–227). Nothing about convergence is stated.
* **(N8)** TRUE.

### 5.3 FIDELITY §3 (differs from the prose) — rows D1–D6 at the Lean

* **(D1)** TRUE at lines 158–182: `φ : ContDiffBump (0 : ℝ) := ⟨Real.log M, L, hrIn, hMlt⟩` with M = `max'` of `interior L`,
  `P := Lagrange.interpolate (interior L) node (value a g)`, witness `fun u => P.eval ((u^2 : ℝ) : ℂ) * ((φ u : ℝ) : ℂ)`; `interior`
  (line 77) is the filter `2 ≤ n ∧ Real.log n < L` of `Finset.range (⌊Real.exp L⌋₊ + 1)`; values (1/2)·n^{1/2−a}·g(log n) (line 121);
  empty case k = 0 (line 231).
* **(D2)** TRUE — the probe's `#check` shows `interpolant` has no evenness hypothesis; the root theorem binds it as `_` (line 248).
* **(D3)** "the witness is C^∞" is true mathematically; "**the proof produces a smooth k and weakens**" (FIDELITY.md lines 71–72) is FALSE
  AT THE LINE — item **F3**: lines 187–193 of both solution files prove `ContDiff ℝ 2` directly (`contDiff_poly_eval` at index 2,
  `φ.contDiff (n := 2)`, `ContDiff.comp`, `ContDiff.mul`); no C^∞ statement is proved and nothing is weakened. Same in BUILD-NOTES.md
  line 100 ("C^∞ produced"). "The class stated is the one `EF_lit` quantifies over": the stated class (even, C², tsupport in the band) is
  a SUBCLASS of `EF_lit`'s (C², compact support); membership holds (probe item (2)). Not an item — the headers and the yaml say
  "a member of the class", which is exact.
* **(D4)** TRUE. At L = log 2, ⌊e^{log 2}⌋₊ = 2 and log 2 < log 2 fails, so `interior` is empty; for L < log 2 likewise; for L < 0
  `Set.Icc (-L) L` = ∅, so g = 0 and both sides are 0 (the empty branch covers it).
* **(D5)** TRUE (`cutoff`, lines 60–74, is the D5 proof re-proved locally; no import of `Solution.WeilContainment`).
* **(D6)** TRUE (the split is `by_cases hI : (interior L).Nonempty`, line 156).

## 6. PREDERIVATION-ERRATA E1–E7, at the pre-derivation (BRIEF §0) and at the Lean

* **E1 (gap at L = log 2) — RIGHT.** §0 (P1) covers L < log 2 and (P2) "otherwise"; at L = log 2, N = 2 and I = {n : 2 ≤ n ≤ 2, log n <
  log 2} = ∅, so (P3)'s "positive minimum over a finite nonempty set" has no set to range over. The conclusion holds there (k = 0; the
  n = 2 term vanishes because g(log 2) = g(L) = 0 by (P2)'s own edge argument). The Lean proof splits on `(interior L).Nonempty` (line 156).
  The gap does not change the statement's shape; stop line (iv) correctly did not fire.
* **E2 (evenness of g unused) — RIGHT**, confirmed by the kernel (probe `#check`; root theorem line 248 binds the hypothesis as `_`).
* **E3 (one bump × Lagrange interpolant in u²) — RIGHT.** φ = 1 on closedBall 0 (log M) ∋ ±log n for n ∈ I (`hφ1`, lines 166–174, via
  log n ≤ log M); φ(±log n) = 0 whenever L ≤ log n (`hφ0`, lines 176–180, `zero_of_le_dist` with rOut = L; the mirrored point via
  `ContDiffBump.neg`, line 181); nodes (log n)² distinct on I (`node_injOn`, lines 124–138: `pow_left_inj₀` on [0, ∞), then
  `Real.log_injOn_pos`); `Lagrange.eval_interpolate_at_node` (line 212). The witness interpolates at ±log n — the label's clause is exact.
  The legality condition 0 < rIn < rOut is `Real.log_pos` (M ≥ 2) and `log M < L` (M ∈ I).
* **E4 (closed-set argument) — RIGHT** at lines 45–57 (`isClosed_eq`, `closure_Ioi`, `closure_subset_iff`).
* **E5 (distinctness; the implicit δ < log 2) — RIGHT.** The half-minimum-distance clause includes the pair {log n, −log n} at distance
  2 log n, so δ < min_{n∈I} log n ≤ (log n + log m)/2, which is what the mirrored bumps need. (Moot in Lean: no δ.)
* **E6 (the rpow identity) — RIGHT** at lines 141–149 (`Real.sqrt_eq_rpow`, `Real.rpow_neg`, `Real.rpow_add` on (n : ℝ) > 0, then
  `ring` on the exponents −1/2 + (1/2 − a) = −a); hypothesis `0 < n`, used for n ∈ I (n ≥ 2).
* **E7 (smoothness index) — RIGHT.** `ContDiffBump.contDiff : ContDiff ℝ n f` with `{n : ℕ∞}` (Mathlib `BumpFunction/Basic.lean`
  line 115 variable, line 203 theorem, read in the clone); the proof instantiates `n := 2` and casts (line 191–192) — the "(or by
  instantiating n)" branch of E7, which is also why F3's sentence is wrong.
* **Mathlib line numbers.** `structure ContDiffBump` 70, `ContDiffBump.neg` 132, `one_of_mem_closedBall` 137, `tsupport_eq` 157,
  `zero_of_le_dist` 163, `contDiff` 203 — all re-read in the clean clone's `.lake/packages/mathlib` at 51e6992e; stop line (i) did not fire.
* **Pre-derivation (P1)–(P6)** otherwise re-derived with no further error: (P2)'s "every n > N has log n > L" (`Nat.lt_of_floor_lt`,
  `Real.lt_log_iff_exp_lt`); (P6)'s term identity (Λ/√n)·2c_n = Λ n^{−a} g(log n); the finite support of both tsums.

## 7. Hashes (`check-O/hashes-recompute.log`)

Every line of `hashes.txt` recomputed with `shasum -a 256` from `rh-program/`: **29 matched, 1 mismatched, 0 missing.** The one
mismatch is `SHARED.md`, which `hashes.txt` itself says is hashed "as it stood before its closing block": the first 39 lines of the
current file (everything before the blank separator line 40 and the closing block at line 41) hash to
`12ff22e51fc25f09ef9434eb6e499cf3d4f002286284063cf3d0d09a47f36b9f` = the recorded value. So all 30 recorded hashes are accounted for;
nothing the builder shipped has changed since 06:46:25 IST. The SHARED closing block's four hashes (BUILD-NOTES `421db9a6…`, FIDELITY
`bb499197…`, hashes.txt `2deb306d…`, ERRATA `bf31def4…`) also match. `ChallengeDeps/WeilContainment.lean` = `47c9a508…` in the tree, in
the clone, and in `results/d5-lean-s30/hashes.txt`.

## 8. Yaml, lint (`check-O/yaml-lint.log`, `check-O/yaml-validator.out`)

`python3 results/d1-m2a/dr8/validate_yaml_sigma_strong.py` (the D5 validator): `RESULT: PASS — errors: 0, undeclared names: 0`, exit 0.
The yaml parses; one `main_results` entry names WeilContainmentC2; two `alignment.statements` rows name the two theorems; row (x) is
present; row (u)'s (N2) sentence is kept with the dated FORMALIZED bracket after it (line 935). 10(g) lint: 0 hits in FIDELITY, ERRATA,
SHARED and the six Lean files; the one hit in BUILD-NOTES (line 130) and the one in BRIEF quote the banned list as the lint's subject.
No British spelling found in the H5 prose or Lean files. (Note: `ORCHESTRATOR-NOTES.md`, 06:48, appeared in this folder after the
builder closed; it is not in `hashes.txt`, is not the builder's, and was not read for this verdict beyond its first five lines.)

## 9. Verdict — FIX-FIRST (prose only; the Lean, the statements, the label and every run are CLEAN)

The theorems are what the brief asked for: both statements carry exactly the three displayed hypotheses, the family statement is
§0's character for character and the rung-1 statement elaborates to §0's; both build from a clean clone (8698 jobs, 0 errors, 0
warnings); `#print axioms` is [propext, Classical.choice, Quot.sound] for both; comparator with nanoda exits 0 on both configs; the
trust greps show only the two deliberate challenge `sorry`s; every recorded hash matches. The label is earned, verbatim A7. Nothing
claims more than "prime-side values; the C² witness is an interpolant at ±log n, not the tilted test; zero side untouched" about the
theorem. Four prose sentences are false as written (the D5 lesson's shape); none touches a Lean statement or proof.

* **F1** — `results/h5-c2-lean-s32/FIDELITY.md` lines 43–44, (N3): "`EF_lit`, `literatureRHS`, `prime_term` do not occur in any of the
  seven topic files" is false: `EF_lit` occurs in comments at `Challenge/WeilContainmentC2.lean` lines 23, 28 and
  `Challenge/WeilContainmentC2One.lean` line 26; `literatureRHS` at `ChallengeDeps/WeilContainment.lean` lines 24, 25, 51. Replace with
  "occur in no declaration, statement or import of the seven topic files (comments stripped; they appear in header comments only —
  `check-O/trust-greps.log`)".
* **F2** — the tilted test's regularity, over-stated in two ways: `FIDELITY.md` line 37 heading "(N2) The tilted test itself is not C²"
  (false as a universal: g = 2e^{(a−1/2)|u|}·χ, χ a smooth even bump in the band, gives `weilTestOf a g = χ`, C^∞) and lines 37–38
  "in general not C¹ at 0 (`weilContainment_not_contDiff` at a = 1, g ≡ 1)" (the theorem states only `¬ ContDiff ℝ 2`, D5
  `Challenge/WeilContainment.lean` line 117). The same two phrasings at `BUILD-NOTES.md` lines 16 and 97, `lean/README.md` line 469,
  `lean/formalization.yaml` line 981 (row (x)), and — as COMMENTS — `lean/comparator/Challenge/WeilContainmentC2.lean` lines 25–26 and
  `Challenge/WeilContainmentC2One.lean` line 25. Replace with D5's wording: "the tilt does not preserve the C² class
  (`weilContainment_not_contDiff`: at a = 1, g ≡ 1 the test is not C²; that this instance is not even differentiable at 0 is a hand
  fact, not a Lean statement)".
* **F3** — `FIDELITY.md` lines 71–72, (D3): "the proof produces a smooth k and weakens" is false at the line: both solution files,
  lines 187–193, prove `ContDiff ℝ 2` directly (index 2 instantiated in `contDiff_poly_eval` and `φ.contDiff (n := 2)`); no C^∞
  statement is proved. Same at `BUILD-NOTES.md` line 100 ("C^∞ produced"). Replace with "the witness is C^∞ (by hand — every factor
  is; the Lean proof instantiates the index at 2 directly)". Row (x4)'s "the witness is in fact C^∞" is true and may stay.
* **F4** — `BUILD-NOTES.md` lines 57–58: "Both statements are the brief's, character for character (§0 'The statement to ship' and
  'Rung 1')" is not literally true for rung 1: §0 writes `∃ k,`, `Challenge/WeilContainmentC2One.lean` line 44 writes
  `∃ k : ℝ → ℂ,`. The two elaborate to the same type (`check-O/probe_h5.lean` item (1)). Replace with "the family character for
  character; rung 1 differing only by the ascription `k : ℝ → ℂ`, which elaborates identically".

## 10. What the orchestrator should do

1. Apply F1–F4 as dated corrections in `FIDELITY.md`, `BUILD-NOTES.md`, `lean/README.md` line 469 and `lean/formalization.yaml`
   row (x) line 981, re-deriving each from the lines cited; re-run the yaml validator after the yaml edit; recompute `hashes.txt`.
2. For F2's two occurrences in the challenge-file COMMENTS: the least disruptive course is to leave the Lean files untouched (the
   comparator certifies statements, not comments) and let the dated FIDELITY correction govern. If the comments are edited, rebuild both
   topics, re-run the statement-identity tool, `#print axioms` and both comparator runs, and re-hash — the trusted files would change.
3. Nothing else: no Lean statement, proof, config, or trusted definition needs to change; the label stands verbatim; the D5 (N2)
   FORMALIZED bracket (`results/d5-lean-s30/FIDELITY.md` line 50) is accurate as written and may stay.

## 11. Every log of this check (under `results/h5-c2-lean-s32/check-O/`)

`clone.log` (clone, checkout v1.0, overlay, toolchain, manifest); `cache-get.log`; `build-c2one.log`; `build-c2.log`; `print-axioms.log`;
`probe_h5.lean` + `probe_h5.log`; `statement-identity.log`; `brief_identity.py` + `brief-identity.log`; `trust-greps.log`; `run.sh`;
`cleanup.sh`; `prerun-cleanup-c2one.log`; `comparator-c2one.log`; `prerun-cleanup-c2.log`; `comparator-c2.log`; `hashes-recompute.log`;
`yaml-lint.log`; `yaml-validator.out`. Clean clone: `~/rh-lean-work/checker-clone-s32-h5`.

Closed: Tue Sep 29 07:00:32 IST 2026.
