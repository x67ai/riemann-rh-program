# H4 — IV.17's pair channel: CHECK-O, the Opus 5 clean-clone check of the Comparator topic `PairChannel` (Session 33; UNIT-BRIEF §3; KICKSTART 10(f), 10(j))

Checker: Opus 5, started Tue Sep 29 11:53 IST 2026 (machine clock). Contract: `results/h4-pair-typing-s32/UNIT-BRIEF.md` §3 (SHA-256
`2d80f9db8ccf04765840b041189dc771813f5fdbb77767c40d471e8b9908cb94`, recomputed, equal to the one BUILD-NOTES quotes). Read before any run:
UNIT-BRIEF in full; `BUILD-NOTES.md`, `FIDELITY.md`, `PREDERIVATION-ERRATA.md`, `hashes.txt`, `SHARED.md`, the builder's logs and `tools/`;
the precedent CHECK-O files of I.1 (s32), H5 (s32) and IV.17 (s30) for shape. `ORCHESTRATOR-NOTES.md` was NOT opened before this file was
written. The builder's tree `~/rh-lean-work/checker-clone-s21` was never used for a build or a run. Every log below is under
`results/h4-pair-lean-s33/check-O/`. Nothing committed; no Lean file, yaml, README or builder note edited.

(Verdict and the numbered findings: §11, written last.)

## 1. Clean clone, overlay, cache (`check-O/clone.log`, `check-O/overlay.sh`, `check-O/overlay.log`, `check-O/cache-get.log`)

`git clone https://github.com/anthropics/zeta-23-lean ~/rh-lean-work/checker-clone-s33-h4` (a NEW directory; retry loop), `git checkout
v1.0` → HEAD `3635e74826a4c1fcece7d1cd2b6fa75e43a00510` ("Merge pull request #3 from anthropics/xiprime-pairceiling"); `lean-toolchain`
`leanprover/lean4:v4.33.0-rc2`; manifest Mathlib `inputRev` `51e6992efd06126df61a496bebf8f49482a4e129`; after `lake exe cache get`
("Decompressed 8489 already-cached file(s) … Completed successfully") the checked-out `.lake/packages/mathlib` HEAD is
`51e6992efd06126df61a496bebf8f49482a4e129`. Mathlib was never compiled from source.

**Overlay — narrower than the H5 / I.1 checkers' whole-tree overlay, and why.** The H5 and I.1 checkers overlaid the whole of
`rh-program/lean/Zeta23/`, `lean/comparator/` and `lean/Zeta23.lean` (README "Building"). This check was asked to overlay only the unit's
files; v1.0 does not contain the unit's Zeta23 import closure, so the overlay (`overlay.sh`, each file `cp` then `cmp`-verified) is:
the seven unit files (`PairRow.lean`, `PairCert.lean`, the four `comparator/*/PairChannel.lean`, `config-pair-channel.json`); the three
Zeta23 modules of `PairCert`'s import closure that v1.0 lacks (`GridParseval.lean`, `GridCorner.lean`, `GridParsevalRat.lean` — earlier,
separately checked units; the closure was computed by following `import Zeta23.*` lines from `PairCert.lean`: exactly these five modules,
all five absent from v1.0); `comparator/ChallengeDeps/IntegralityGap.lean` (only for the 7/7 `diff`, never built); and the root
`Zeta23.lean` as every prior overlay copied it (not built here). `git status` after the overlay: `M Zeta23.lean` and eleven `??` files —
nothing else of v1.0 was touched. Note: the root `Zeta23.lean` of `rh-program/lean/` imports neither `PairRow` nor `PairCert` (nor
`GridParsevalRat`), so `lake build Zeta23` does not build this unit; the modules are built by name (§2).

## 2. Cold builds, one at a time (`check-O/build-pairrow.log`, `check-O/build-paircert.log`, `check-O/build-comparator.log`, `check-O/cert-profile.log`)

| build (sequential, never two at once) | result | modules built | wall |
|---|---|---|---|
| `lake build Zeta23.PairCeiling.PairRow` (11:56:59) | *Build completed successfully (2282 jobs)*, rc 0, 0 errors, 0 warnings | `GridParseval (3.3s)`, `GridCorner (1.6s)`, `GridParsevalRat (1.4s)`, `PairRow (2.1s)` | 9.47 s |
| `/usr/bin/time -l lake build Zeta23.PairCeiling.PairCert` | *Build completed successfully (2296 jobs)*, rc 0, 0 warnings | `PairCert (1.8s)` | **2.68 s real, max RSS 2.57 GB** |
| `lake build ChallengeDeps.PairChannel` (11:57:21) | 8697 jobs, rc 0 | `ChallengeDeps.PairChannel (6.1s)` | 8.83 s |
| `lake build Challenge.PairChannel` | 8698 jobs, rc 0, **exactly 8 warnings, each "declaration uses `sorry`"** (lines 53, 58, 65, 70, 76, 82, 86, 92 — the eight `theorem` lines) | `Challenge.PairChannel (3.1s)` | 5.20 s |
| `lake build Solution.PairChannel` | 8703 jobs, rc 0, 0 warnings | `Solution.PairChannel (3.0s)` | 5.00 s |
| `lake build PrintAxioms.PairChannel` | `error: unknown target` — `PrintAxioms` is not a `lean_lib` in the lakefile (as in every prior topic); the file is run with `lake env lean` (§3) | — | — |

**The certificate's kernel time on the clean clone** (`cert-profile.log`: `lake env lean -Dprofiler=true -Dprofiler.threshold=0
Zeta23/PairCeiling/PairCert.lean` under `/usr/bin/time -l`): 2.76 s real for the whole file (import 910 ms of it), max RSS 2.53 GB;
the profiler's cumulative **type checking 125 ms** over 27 declarations (largest single declaration 18.6 ms); norm_num 300 ms, tactic
execution 222 ms. The builder's figures (2.72 s real for the lake call, 1.8 s module, 2.38 s `lake env lean`, 58 ms type checking for
the four power sums alone) are reproduced in order of magnitude; the ten-minute stop line (iii) is out of reach by a factor above 200.

## 3. `#print axioms` for every name (`check-O/print-axioms.log`, `check-O/program-axioms-checker.lean`)

* `lake env lean comparator/PrintAxioms/PairChannel.lean`: 8 lines, each `depends on axioms: [propext, Classical.choice, Quot.sound]`, rc 0.
* The checker's own probe, GENERATED from every `def`/`lemma`/`theorem` line of `PairRow.lean` and `PairCert.lean` (44 names: 27 + 17,
  the five definitions included): 43 lines read `[propext, Classical.choice, Quot.sound]`; `Zeta23.PairCeiling.PairRow.vacancyMark`
  reads `[propext, Quot.sound]` (a subset — within "the three standard axioms or fewer"). rc 0.
* `sorryAx`: 0 hits; `Lean.ofReduceBool`: 0 hits. **Result: clean.**
* Coverage remark (finding F2, §11): the builder's `program-axioms.lean` probes 34 names; the 10 not probed there are the five definitions
  `W2`, `pairFormFactor`, `pairRow`, `abar`, `vacancyMark` and the five lemmas `card_band32`, `sum_pow2_real`, `sum_pow4_real`,
  `sum_pow6_real`, `sum_pow8_real`. All ten are clean in the checker's probe; but the builder's sentence "the 34 names of `PairRow` +
  `PairCert` — all three axioms, nothing else" reads as the whole of the two files, which it is not, and one name there has two axioms.

## 4. Statement identity and trusted definitions (`check-O/statement-identity.log`, `check-O/identity_checker.py`)

* The builder's `tools/statement_identity_h4.py` on the clean clone, the eight names as eight arguments: 8/8 IDENTICAL, RESULT PASS.
* The checker's own script (a different extraction: `theorem <name>` to the `:=` before `by`): challenge = solution byte for byte 8/8;
  challenge = typing probe `results/h4-pair-typing-s32/typing-probe.lean` byte for byte 8/8; all three equal after whitespace
  normalization; and each equals the backticked text of UNIT-BRIEF §0 items 1–8 after whitespace normalization 8/8.
* Trusted definitions: `PairChannel.{chi, dftMark, dftMarkQ, zetaM, gridRow, gridRowQ, fracMark}` against
  `comparator/ChallengeDeps/IntegralityGap.lean` — 7/7 IDENTICAL; `{W2, pairFormFactor, pairRow, abar, vacancyMark}` against
  `Zeta23/PairCeiling/PairRow.lean` — 5/5 IDENTICAL; against the probe 4/5, the one difference being `W2`'s summation binder `_j` (probe:
  `j`), the same term — FIDELITY (z9) records it.
* Read by eye, against UNIT-BRIEF §0's prose and the record: `W2` sums the constant (1/M)² over `j ∈ B` with `s − j ∈ B` — the
  autocorrelation u ∗ u at u_j = 1/M (paper.md §2.3 "W2(s) = Sum_{j in B, s-j in B} u_j u_{s-j}"); `pairFormFactor` = the atoms' DFT at the
  REDUCED residue `(s : ZMod (2n+1))` plus, per pair `(θ, μ, d)`, `2μ cosh(2π s d/(2n))` at the UNREDUCED `(s : ℝ)` times `χ(s·θ)`; with
  the grid g_k = k·64/65 of paper §4.2, e^{−2πi s g_k/64} = e^{−2πi sk/65}, so `χ` = ζ_65^{(sk).val} is the record's phase up to
  conjugation (immaterial under `normSq`; FIDELITY (z5)); `pairRow` sums over `Icc (−2n) (2n)` = |s| ≤ 64 at n = 32 (pair-channel.md
  §1 "F1 = Sum_{|s| <= 64} w_s |c_s|^2"); `abar` = Σ_j u_j cosh(2πjx/N) with N = 2n (pair-channel.md §2); `vacancyMark` = unit atoms off
  site 0. Agreement with the brief and the record: yes, all five.

## 5. Trust greps (`check-O/trust-greps.log`)

The builder's `tools/trust_greps_h4.py` on the clean clone, the seven unit files as seven arguments (bash array; the config included):
8 hits, all `sorry`, all in `comparator/Challenge/PairChannel.lean` (lines 55, 62, 67, 73, 79, 83, 88, 94); rc 1 (the tool's "hits
present" code). The checker's raw word-bounded grep with comments NOT stripped, for the nine words: `unsafe`, `implemented_by`, `extern`,
`opaque`, `admit` 0 hits; `axiom` 3, `native_decide` 3, `ofReduceBool` 1 and 2 of the 10 `sorry` hits are all inside header comments
that say "no `native_decide`", "no new axiom", "no `sorry`", "No sorryAx, no Lean.ofReduceBool". Imports: trusted layer `import Mathlib`
only; challenge `ChallengeDeps.PairChannel` only; solution `ChallengeDeps.PairChannel` + `Zeta23.PairCeiling.PairCert`; program modules
`GridParsevalRat` / `PairRow` plus three Mathlib files. No `set_option`, `macro`, `elab`, `syntax`, `partial def` or attribute in any of
the seven files; the only kernel-reduction devices are the four `decide +kernel` power sums (`PairCert.lean` lines 114–117). **Clean.**

## 6. Comparator run with nanoda from the clean clone (`check-O/run-clone.sh`, `check-O/cleanup.sh`, `check-O/prerun-cleanup.log`, `check-O/comparator-run.log`)

Runner: the builder's `tools/run.sh` with exactly two lines changed (the comment line 2 and the `cd` target → the clean clone; `diff`
in the transcript). Pre-run cleanup removed the topic's 24 comparator-layer artifacts under `.lake/build/{ir,lib/lean}`
(`ChallengeDeps/Challenge/Solution` `PairChannel.*`), "remaining: 0", so comparator built every comparator-layer module itself.
Config `comparator/config-pair-channel.json`: the eight names in the challenge's order, `permitted_axioms` `propext`, `Quot.sound`,
`Classical.choice`, `enable_nanoda: true`.

| comparator output | nanoda | Lean kernel | exit | wall / max RSS |
|---|---|---|---|---|
| `Built ChallengeDeps.PairChannel (2.0s)`, `Built Challenge.PairChannel (3.0s)` (8 deliberate `sorry` warnings), `Built Solution.PairChannel (3.0s)`, `Your solution is okay!` | `Nanoda kernel accepts the solution` | `Lean default kernel accepts the solution` | **0** | 43.56 s / 5.85 GB |

Tool SHA-256s printed in the log — comparator `fe1222e25fc3…`, lean4export `de4ffedf1412…`, nanoda_bin `d6c87133b59c…`, fake-landrun
`167507c89d8b…` — each occurs in `results/d1-m2a/packaging/COMPARATOR-RUN.md` (1 hit each). NOT sandboxed (the fake-landrun shim), as in
every prior macOS record. Toolchain in the log `v4.33.0-rc2`, Mathlib `51e6992e…`.

## 7. Re-derivation by hand and the anchor numbers (`check-O/rederive_h4.py`, `check-O/rederive.log`, `check-O/mi_family_scan.py`, `check-O/mi-family-scan.log`, `check-O/z10-probe.{lean,log}`)

The checker's own script, written from the record's definitions (pair-channel.md §1, §3; paper.md §2.3, §4.2); the builder's
`tools/h4_numbers.py` was neither read nor imported. mpmath at 40 digits; the power sums and the certificate's rational in exact
`Fraction`s.

**Prop. 4.5's expansion, for general n.** M = 2n + 1 sites, band B = {−n, …, n}, u = 1/M, W2(s) = #{j ∈ B : s − j ∈ B}/M². Three facts:
(a) Σ_{s ∈ [−2n, 2n]} W2(s) = Σ_{j₁, j₂ ∈ B} 1/M² = 1 (regrouping at g ≡ 1); (b) W2(0) = #B/M² = 1/M; (c) (T1) at imaginary argument,
Σ_s W2(s) cosh(βs) = Σ_{j₁,j₂} u² cosh(β(j₁ + j₂)) = (Σ_j u cosh βj)² + (Σ_j u sinh βj)² by cosh(a + b) = cosh a cosh b +
sinh a sinh b, and the sinh sum over the symmetric band vanishes, so the sum is ā(d)² with β = 2πd/N, N = 2n; at 2β it is ā(2d)². The vacancy DFT: Σ_{k ≠ 0} ζ^{sk} = M·[s ≡ 0 mod M] − 1, and for |s| ≤ 2n < M, s ≡ 0 iff s = 0; so φ₀(s) = 2n at
s = 0 and −1 otherwise (at n = 32: 64 and −1, as paper §4.2). The pair at site 0 has character 1, so c_s = φ₀(s) + 2μC_s,
C_s = cosh(βs), real. Then |c_s|² = φ₀(s)² + 4μφ₀(s)C_s + 4μ²C_s², and with φ₀(s) = −1 + M·[s = 0]:

  Σ W2 φ₀² = Σ W2 · 1 + W2(0)(M² − 2M) = 1 + M − 2 = 2n;
  Σ W2 φ₀ C = −Σ W2 C + W2(0)·M·C₀ = −ā(d)² + 1;
  Σ W2 C² = Σ W2 (1 + cosh 2βs)/2 = (1 + ā(2d)²)/2.

F1 = 2n + 4μ(1 − ā(d)²) + 2μ²(1 + ā(2d)²) = (2n + 2μ²) + 2μ²ā(2d)² − 4μ(ā(d)² − 1). With S2 = Σ_a m_a² + 2μ² = 2n + 2μ² (2n unit
atoms, pair members counted μ² each): **F1 − S2 = 2μ²ā(2d)² − 4μ(ā(d)² − 1)**, for every n (n = 0: F1 = W2(0)(2μ)² = 4μ² = S2 + 2μ²·1,
checked), every d, every real μ. This is exactly the three sums of `prop45`'s proof (`sum_W2_vacancy_sq`, `sum_W2_vacancy_cosh`,
`sum_W2_cosh_sq`), and it uses (T1), W2(0) = 1/M, the vacancy DFT and cosh² = (1 + cosh 2x)/2 — not Prop. 4.1's ledger.

**The integer chain.** (T3): ā(d)² = (Σ_j u cosh βj)² ≤ (Σ_j u)(Σ_j u cosh² βj) = Σ_j u (1 + cosh 2βj)/2 = (1 + ā(2d))/2 (Cauchy–Schwarz
with Σ u = 1). Write A = ā(2d) ≥ 1 (each cosh ≥ 1, weights sum to 1). Then 4m(ā(d)² − 1) ≤ 4m((1 + A)/2 − 1) = 2m(A − 1) for m ≥ 0, so
the expression ≥ 2m²A² − 2m(A − 1) = 2m(mA² − A + 1) ≥ 2m(A² − A + 1) (as m ≥ 1, A² ≥ 0) and A² − A + 1 = (A − 1/2)² + 3/4 > 0, so it
is > 0 for every integer m ≥ 1. This is paper §4.2's display and the `h1`/`h2` of `floor_holds_integer`'s proof. Where integrality
enters: only m ≥ 1 (a real μ ∈ (0, 1) breaks mA² ≥ A², which is what the anchor exploits).

**The anchor numbers, recomputed** (n = 32, u_j = 1/65, (d, μ) = (1/4, 1/20)):

| quantity | checker's value | builder / record |
|---|---|---|
| ā(1/4) | 1.10944370003314 | 1.10944370 / 1.109444 |
| ā(1/2) | 1.48140550328865 | 1.48140550 / 1.481406 |
| F1 − S2, closed form | −0.0352002533827736 | −0.0352002534; record −3.520e-2 |
| F1 − S2, direct row (W2 by its definition, c_s at the UNREDUCED s from the vacancy DFT + pair) | −0.0352002533827736 (difference 2.5·10⁻³⁹) | identical to 13 digits |
| F1 − S2 with the pair factor at the residue reduced mod 65 (the shipped `gridRowQ` convention) | −0.01448171249 | −0.0144817 — a different number, the reason for the new row |
| F1, S2 | 63.9697997466172, 64.005 | F1 = 63.9698 |
| max \|W2(s) − (M − \|s\|)/M²\|, Σ W2 | 0.0, 1.0 | — |
| (T1) residual at x = 1/4, 1/2 | 2.3·10⁻⁴¹, 9.2·10⁻⁴¹ | — |
| S₂, S₄, S₆, S₈ over j ∈ [−32, 32] (exact) | 22880, 14492192, 10924353440, 8964042662432 | the same four |
| L = 1 + (3.141592/128)²·S₂/(2·65) | 1.1060210969 (ā(1/4) − L = 0.0034226) | 1.1060211 |
| U = (1/65)Σ_j poly8(3.141593·j/64) = 1 + Σ_k (3.141593/64)^{2k} S_{2k}/((2k)!·65) | 1.4815182153 (U − ā(1/2) = 0.0001127) | 1.4815182 |
| certified bound 2μ²U² − 4μ(L² − 1), exact rational | −0.03368205225 (< 0: True); margin spent 0.0015182 | −0.033682; 0.0015182 |
| the literal rational of `cert_numeric` (reduced) | the same value; numerator 132 digits, denominator 133 digits | "a 133-digit numerator" (F3) |
| largest cosh argument in `abar_half_le` | π/2 = 1.5708 ≤ 9/2 | — |
| **(MI) at the anchor**: M = 64 + 2μ = 64.1, N_d = 66, T = 3M − 2N_d | **T = 60.3, F1 − T = +3.669799747, S2 − T = 3.705 = 2(μ − 1)(μ − 2)** | T = 60.3, F1 − T = +3.67, 3.705 |
| threshold μ* = 2(ā(d)² − 1)/ā(2d)² at d = 1/4 (F1 < S2 for 0 < μ < μ*) | 0.2103976 | — |

**(MI) at the anchor: CONFIRMED to HOLD** (F1 − T = +3.6698 > 0), while the floor F1 ≥ S2 fails (F1 − S2 = −0.0352). Further, on the
whole Prop. 4.5 family F1 − T = 2(μ − 1)(μ − 2) + 2μ²ā(2d)² − 4μ(ā(d)² − 1); the checker's grid scan over d ∈ (0, 1] (step 0.0025) and
μ ∈ (0, 3] (step 0.005) finds min F1 − T = +1.750 (at d = 0.0025, μ = 0.75): **on this family (MI) is never violated** — see
observation O1 (§11).

**Errata E5, E7, E9 checked at the line.** E5: TYPING-NOTE.md's lower-bound bullet ("Error at |x| ≤ π/4: cosh x − 1 − x²/2 ≤
x⁴/24·cosh x ≤ 0.021") — the value at π/4 is 0.016184 and x⁴/24·cosh x = 0.021001, so 0.021 is the upper estimate, as E5 says;
harmless. (The errata's companion remark on the upper bound: poly8(π/2) − cosh(π/2) = 0.000894 and 2(π/2)⁸/40320 = 0.00184 — both
reproduced.) E7: the note's π bullet ("the bracket `3294198/2²⁰ < π < 3294200/2²⁰` follows from the two d6 lemmas by `norm_num`") —
3294198/2²⁰ = 3.14159202575684 > 3.141592, so the lower end does NOT follow from `pi_gt_d6`; 3294197/2²⁰ = 3.14159107 < 3.141592 and
3294200/2²⁰ = 3.14159393 > 3.141593 — E7's corrected bracket reproduced; the unit uses the d6 decimals directly (`abar_quarter_ge_L`,
`abar_half_le_U`), so nothing depends on it. E9: `sq_sum_le_card_mul_sum_sq : (∑ i ∈ s, f i) ^ 2 ≤ #s * ∑ i ∈ s, f i ^ 2` is at
`Mathlib/Algebra/Order/Chebyshev.lean` line 136 in the clone's Mathlib (read at the line), and `abar_sq_le`'s proof uses it
(PairRow.lean line 428). All three errata confirmed.
**FIDELITY (z10)'s mechanism checked** (`z10-probe.log`): the bare definition `Finset.Icc (-32 : ℤ) 32` and the bare PROPOSITION of
`sum_pow2` already depend on `[propext, Classical.choice, Quot.sound]`, so the three axioms of the `decide +kernel` facts come from
Mathlib's interval instances on ℤ, not from the kernel decision — as (z10) says.

## 8. The challenge statements against the brief and the record; the ledger sentences re-derived

**Per statement** (read at the line against UNIT-BRIEF §0, pair-channel.md §0–§4, paper.md §2.3 and §4.2):

| # | statement | vs UNIT-BRIEF §0 | vs the record | hypotheses beyond binders | verdict |
|---|---|---|---|---|---|
| 1 | `W2_eq` | identical (normalized) | pair-channel.md §1 "w_s = (65 − \|s\|)/65² for \|s\| ≤ 64", for every n | none (band membership is the subject) | CLEAN |
| 2 | `sum_W2_mul` | identical | paper §2.3's single-convolution = double-band form of tr Ĝ² | none | CLEAN |
| 3 | `pairRow_eq_gridRowQ` | identical | the agreement with the shipped row on pair-free columns (queue requirement) | none | CLEAN |
| 4 | `sum_W2_cosh` | identical | (T1) of pair-channel.md line 71 at q = e^{β}; Prop. 3.1's "Σ_s w_s cosh(βs) = ā(d)²" | none | CLEAN |
| 5 | `prop45` | identical | paper Prop. 4.5 display, with S2 = 2n + 2μ² written out; stronger (every n, every real μ incl. μ ≤ 0, d = 0) | none | CLEAN |
| 6 | `abar_sq_le` | identical | (T3) "ā(y)² ≤ (1 + ā(2y))/2" | none | CLEAN |
| 7 | `floor_holds_integer` | identical | paper §4.2 "For integer marks the same family is safe … > 0", about prop45's right side at μ = m | `1 ≤ m` (the brief's list) | CLEAN |
| 8 | `floor_fails_anchor` | identical | the SIGN of "F1 − S2 = −3.520e-2" at (d, μ) = (0.25, 0.05), n = 32; says nothing about (MI) | none | CLEAN |

The five trusted definitions agree with the brief's prose and the record (§4). The label of UNIT-BRIEF §1(3) is reproduced verbatim in
BUILD-NOTES, FIDELITY, the yaml description, the README and the status addendum (checked by eye against the brief; the "**…**" bold
around "the floor F1 ≥ S2's failure" in the brief is markup only). The challenge header's WHAT IS CLAIMED / NOT paragraph: every claim
is a statement in the file; the NOT list (MI; Theorems 4.6–4.9; laws; LP; off-grid pairs; other budgets; ζ, RH) is correct.

**FIDELITY.md re-derived sentence by sentence.** §1 table: every row's "exact content" is the Lean statement read at the line; every
quotation of the record is found at its place (pair-channel.md §1 line 39, (T1) line 71, (T3) §2, Prop. 3.1; paper §2.3 line 126,
§4.2) — correct, except the closing sentence's "and for the 34 program-side names" (F2). §2: (MI) bullet — every number reproduced
(M = 64.1, N_d = 66, T = 60.3, F1 = 63.9698, F1 − T = +3.67, S2 − T = 3.705); Theorems 4.6–4.9 / A–D: stated nowhere in the topic
(true); laws/LP: true; general positions: true (`p.1 : ZMod (2n+1)`); Prop. 4.1, (T2), (T4), (T5): not stated and not used by
`prop45`'s proof (true, §7) — and the paper's proof does not use them either (true: it uses φ₀ and (T1) only); the value: true
(`cert_numeric` states the rational inequality, no theorem states a value; L = 1.10602…, U = 1.48152…, −0.03368 reproduced). §3:
(z1) grid sites — true, and on grid sites the phase agrees: g_k = 64k/65 gives e^{−2πisg_k/64} = e^{−2πisk/65}, the conjugate of `chi`;
(z2) true; (z3) true, n = 0 checked (§7); (z4) true; (z5) true (GridParseval.lean line 143 records the sign convention for the atom
rows); (z6) true; (z7) true (`h1`, `h2` at the line); (z8) true except "whose numerator has 133 digits" (F3); (z9) true; (z10) true
(probe above); (z11) true; (z12) true. §3's heading "the yaml row (z), item by item" is not literally true (F6). §4: true (the O1
qualifier on `dftMarkQ` is carried).

**The yaml, README and status addendum.** The new yaml rows (description, `status.scope` sentence, row (z), review paragraph, two
alignment rows) are correct in substance and carry the label verbatim; `validate_yaml_sigma_strong.py` re-run from `rh-program`:
RESULT PASS, errors 0, undeclared names 0 (`check-O/yaml-validation.log`). Three problems: the 34-name / "every new name" axiom
sentences (F2); two OLDER present-tense sentences in the yaml and README that this unit has made false (F1); the 133-digit figure in the
README (F3). The status addendum handles the older "Still NOT formalized: the pair channel" line correctly with a dated re-reading.

## 9. Forbidden phrasings (`check-O/forbidden-greps.log`)

Case-insensitive fixed-string greps over 32 files — the six Lean files and the config (rh-program/lean/), `formalization.yaml`,
`README.md`, `formalization-status.md`, and every file in `results/h4-pair-lean-s33/` (notes, logs, tools; comments included;
ORCHESTRATOR-NOTES.md excluded, unread by design): "(MI) fails" — 1 hit, `lint-10g.log` line 20, which QUOTES the rule as a search
string; "IV.17 is formalized" — the same one quotation; "pair channel is closed" / "channel is closed" — the same one quotation;
"is formalized" — 14 older yaml lines, each of the form 'never "Theorem M2 is formalized"' / 'never "clause 4 is formalized"'
(other units' rules, quoted), none about IV.17. "(MI) … fail/false/violat" within 60 characters: yaml line 1478 (the Session-30
IV.17 ATOM row "(MI) is FALSE for fractional marks, at the baseline itself" — the mark-4/3 atom column, true and not this unit's) and
yaml line 1018 ((v4) `mi_fails_rational`, the same Session-30 atom fact); every H4 hit is a sentence saying (MI) HOLDS at the anchor.
**No sentence of this unit attributes the anchor's failure to (MI); the three forbidden phrasings are applied nowhere.**

## 10. Hashes (`check-O/hash-recompute.log`)

Every one of the 32 SHA-256s in `hashes.txt` recomputed with `shasum -a 256`: **32 matched, 0 mismatched**. `hashes.txt` itself
(`f33f488e…fdd1fe4`) and `BUILD-NOTES.md` (`11d0dca3…6f1955`) equal the values in SHARED.md's final builder block.

## 11. Verdict, findings, observations

(Every OLD: string below occurs exactly once in its file, line breaks read as spaces — checked by script.)

**Verdict: FIX-FIRST — prose only (F1–F7). The eight Lean statements, the proofs, the trusted definitions, the certificate, every
build and the comparator run are CLEAN; the label of UNIT-BRIEF §1(3) is earned verbatim; no forbidden phrasing is applied anywhere.**
The two items with content are F1 (two older present-tense ledger sentences that this unit has made false) and F2 (the axiom-footprint
sentences claim "every new name" / "the 34 program-side names" as if they were the whole of the two files; there are 44, and one of
them has two axioms, not three). F3–F7 are small accuracy fixes. None of them touches a theorem.

**F1 (ledger; stale present tense).** `lean/formalization.yaml`, the Session-30 IV.17 `main_results` description (the entry whose
declaration line begins "trace_sq_grid_rat, gridRowQ_eq"), sentence beginning "The pair channel (paper Prop. 4.5) stays
unformalized": after this unit it is false as a present-tense statement, and it now sits directly above the Session-33 entry that says
the opposite. The same in row (v)'s NOT-covered list ("NOT covered, and stated nowhere in Lean: … the PAIR CHANNEL (paper Prop. 4.5 …
— paper-certificate grade, item 10)") and in `lean/README.md`'s IntegralityGap section, sentence beginning "What it does NOT say
(FIDELITY.md §2)". The status addendum already re-reads the analogous formalization-status line with a dated rider; the yaml and README
need the same (dated, not a rewrite of history).
OLD: The pair channel (paper Prop. 4.5) stays unformalized; nothing about laws, the
NEW: The pair channel (paper Prop. 4.5) is not in this topic [Session 33: Prop. 4.5 and the floor's failure at its anchor are the Comparator topic PairChannel, the next entry; Theorems 4.6–4.9 stay at paper grade]; nothing about laws, the
OLD: the PAIR CHANNEL (paper Prop. 4.5 = pair-channel.md Prop. 3.1, F1 − S2 = 2μ²ā(2d)² − 4μ(ā(d)² − 1) — paper-certificate grade, item 10);
NEW: the PAIR CHANNEL (paper Prop. 4.5 = pair-channel.md Prop. 3.1, F1 − S2 = 2μ²ā(2d)² − 4μ(ā(d)² − 1) — not in this topic; [Session 33: Comparator-checked as the topic PairChannel, row (z)]);
OLD: nothing about the PAIR CHANNEL (paper Prop. 4.5 stays unformalized — paper-certificate grade),
NEW: nothing about the PAIR CHANNEL (paper Prop. 4.5 is not in this topic — [Session 33: it is the topic PairChannel, section below; Theorems 4.6–4.9 stay at paper grade]),

**F2 (axiom-footprint sentences over-claim coverage).** The builder's `program-axioms.lean` probes 34 names; `PairRow.lean` +
`PairCert.lean` declare 44 (the five definitions `W2`, `pairFormFactor`, `pairRow`, `abar`, `vacancyMark` and `card_band32`,
`sum_pow2_real` … `sum_pow8_real` are not probed); the checker's 44-name probe is clean, with `vacancyMark` at `[propext, Quot.sound]`.
Sentences: `results/a4-no-go/formalization-status.md` addendum, "Axiom footprint of every new name"; `BUILD-NOTES.md` §3, "`program-axioms.log`
(probe `program-axioms.lean`): the 34 names of `PairRow` + `PairCert`"; `FIDELITY.md` §1, closing paragraph "All eight: no displayed
hypothesis …", clause "and for the 34 program-side names"; `lean/formalization.yaml` review paragraph "Comparator run, topic
PairChannel", clause "#print axioms on the 8 root names and the 34 program-side names".
OLD: Axiom footprint of every new name (`results/h4-pair-lean-s33/print-axioms.log`, `program-axioms.log`): `[propext, Classical.choice, Quot.sound]`
NEW: Axiom footprint of every new name (the 8 topic statements, `results/h4-pair-lean-s33/print-axioms.log`; all 44 declarations of `PairRow.lean` and `PairCert.lean`, `results/h4-pair-lean-s33/check-O/print-axioms.log`): `[propext, Classical.choice, Quot.sound]`, except `PairRow.vacancyMark` with `[propext, Quot.sound]`
OLD: the 34 names of `PairRow` + `PairCert` — all three axioms, nothing else.
NEW: 34 of the 44 names of `PairRow` + `PairCert` (the five definitions and `card_band32`, `sum_pow2_real` … `sum_pow8_real` not probed; CHECK-O probed all 44: the three axioms, `vacancyMark` two of them) — nothing else.
OLD: and for the 34 program-side names (`program-axioms.log`);
NEW: and for all 44 program-side declarations of PairRow.lean and PairCert.lean (`program-axioms.log`, 34 names; `check-O/print-axioms.log`, 44 — `vacancyMark` at `[propext, Quot.sound]`);
OLD: #print axioms on the 8 root names and the 34 program-side names of Zeta23/PairCeiling/PairRow.lean and PairCert.lean: [propext, Classical.choice, Quot.sound]
NEW: #print axioms on the 8 root names and the 44 program-side declarations of Zeta23/PairCeiling/PairRow.lean and PairCert.lean: [propext, Classical.choice, Quot.sound], vacancyMark [propext, Quot.sound] (program-axioms.log, 34 names; results/h4-pair-lean-s33/check-O/print-axioms.log, all 44)

**F3 (a number).** `FIDELITY.md` (z8), sentence beginning "The Lean proof's route", and `lean/README.md` PairCert row ("a 133-digit
numerator"), and PREDERIVATION-ERRATA §4 ("whose numerator has 133 digits"): the literal rational of `cert_numeric`, reduced, has a
132-digit numerator and a 133-digit denominator (`rederive.log`).
OLD: one `norm_num` on a rational inequality whose numerator has 133 digits
NEW: one `norm_num` on a rational inequality whose value, reduced, has a 132-digit numerator and a 133-digit denominator
OLD: (`cert_numeric`, a 133-digit numerator)
NEW: (`cert_numeric`, a rational with a 133-digit denominator)

**F4 (a number, in a trusted comment).** `comparator/Challenge/PairChannel.lean` header item (4), clause "the certificate's bound
−0.0336": the certificate's rational is −0.03368205… (UNIT-BRIEF and yaml row (z) say −0.0337); "−0.0336" truncates rather than
rounds. (PairCert.lean's "the certificate proves F1 − S2 ≤ −0.0336 < 0" is a true weaker statement and needs nothing.) Editing a
trusted file changes its hash and needs a comparator re-run; if the orchestrator prefers not to touch the trusted file, a one-clause
note in FIDELITY §2 suffices.
OLD: (the record's F1 − S2 = −3.520·10⁻²; the certificate's bound −0.0336)
NEW: (the record's F1 − S2 = −3.520·10⁻²; the certificate's bound −0.03368)

**F5 (a count).** `BUILD-NOTES.md` §3, bullet beginning "`prerun-cleanup.log`: the three modules'": the log lists 24 paths (the
checker's own cleanup removed 24 as well). (SHARED.md's "25 artifacts removed" is a log line; leave it.)
OLD: the three modules' 25 artifacts under `.lake/build/{ir,lib/lean}` removed
NEW: the three modules' 24 artifacts under `.lake/build/{ir,lib/lean}` removed

**F6 (cross-reference).** `FIDELITY.md` §3 heading "Where the formal statements differ from the prose (the yaml row (z), item by
item)": the yaml row (z) carries (z1)–(z11), without FIDELITY's (z11) "Names", and its (z11) is FIDELITY's (z12).
OLD: ## 3. Where the formal statements differ from the prose (the yaml row (z), item by item)
NEW: ## 3. Where the formal statements differ from the prose (mirrored in the yaml row (z) as (z1)–(z11): (z11) "Names" is not carried there, and the yaml's (z11) is (z12) here)

**F7 ("character for character", the IV.17 O1 lesson carried forward).** `comparator/Solution/PairChannel.lean` header, sentence
beginning "The challenge's `PairChannel.{chi, dftMarkQ, …}` are character for character the Zeta23 definitions": for `dftMarkQ` it is
not — the trusted `def dftMarkQ {F : Type*} [Field F] (ζ : F) …` vs `GridParsevalRat.lean`'s `def dftMarkQ (ζ : F) …` under a section
`variable` (read at the line in the clone; IV.17 CHECK-O O1 showed the constants are equal by `rfl`). The trusted header of
`ChallengeDeps/PairChannel.lean` repeats it transitively ("themselves character for character the … originals"); per the IV.17 O1
recommendation, do NOT edit the trusted header — FIDELITY §4 already carries the qualifier. The untrusted Solution header can be fixed
freely:
OLD: are character for character the
Zeta23 definitions, so each delegation typechecks by definitional unfolding in the kernel.
NEW: are character for character the
Zeta23 definitions (`dftMarkQ` up to where its `Field` binder is written — the same constant, IV.17 CHECK-O O1), so each delegation typechecks by definitional unfolding in the kernel.

**Observations (no fix required of this unit).**
* **O1 — the record, not the unit.** `pair-channel.md` §0 item 1 reads "(MI) is FALSE for real (fractional) marks — an explicit
  vacancy-lattice + shallow-pair family violates even F1 >= S2 for every depth d > 0 at small real pair mark (Proposition 3.1 …)". On
  that family F1 − T = 2(μ − 1)(μ − 2) + [F1 − S2] and the checker's scan finds min F1 − T = +1.750 over d ∈ (0, 1], μ ∈ (0, 3]
  (`mi-family-scan.log`): the family never violates (MI); and for μ < 1, S2 > T, so F1 ≥ S2 is the STRONGER inequality and "even"
  reads backwards. (MI)'s falsity over fractional marks is true through the Session-30 atom column (mark 4/3), not through this
  family. The unit's own files avoid the slip (they say (MI) holds at the anchor); the record sentence is for the orchestrator.
* **O2 — overlay scope.** This check overlaid the unit's files plus the three-module import closure v1.0 lacks, not the whole mirror
  (§1). Every Lean file compiled here is `cmp`-identical to `rh-program/lean/`.
* **O3 — the root.** `rh-program/lean/Zeta23.lean` imports neither `PairRow`, `PairCert` nor `GridParsevalRat`, so `lake build Zeta23`
  does not build this unit; the README's quick check builds `Solution.PairChannel` by name, which works (§2).
* **O4 — trusted header, `dftMarkQ`** (see F7): no edit recommended.
* **O5 — independence.** A `grep` for "0.0336|0.0337" over `results/h4-pair-lean-s33/*.md`, run while collecting F4's sentences AFTER
  §1–§10 of this file were written, printed one line of ORCHESTRATOR-NOTES.md (its item 6, the certificate's L, U and −0.03368). Every
  number in §7 had already been computed and written; nothing else of that file was read.

**OVERALL.** Mathematics and machine checks: CLEAN — cold builds on a fresh v1.0 clone (0 errors; exactly the 8 deliberate `sorry`
warnings), `#print axioms` on all 8 + 44 names within the three standard axioms, statement identity 8/8 (challenge = solution = probe =
brief §0), trusted definitions 7/7 + 5/5, trust greps clean, comparator exit 0 with "Nanoda kernel accepts the solution", the
certificate's module 2.68 s (type checking 125 ms), every anchor number reproduced independently, Prop. 4.5 and the chain re-derived by
hand, (MI) confirmed to HOLD at the anchor (F1 − T = +3.6698). Ledger: FIX-FIRST on F1–F7 (prose; F1 and F2 the ones that matter).
Nothing about ζ or RH follows from anything here.
