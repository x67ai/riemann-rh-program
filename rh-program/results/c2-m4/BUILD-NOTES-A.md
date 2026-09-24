# C2 — Session 24 item 3, UNIT A (`Separation6b`): b₁ proved in symbolic form, the clause-7 fold, and "t ≥ 21L ⟹ (R*)" as a lemma — build notes (Job 1, BUILDER, Fable 5.1; Session 24, 2026-09-24, 19:20–19:55 IST)

Brief: `results/c2-m4/BRIEF-A.md`. Contract: `results/c2-m4/PRICING-RESIDUE.md` §1 Pieces 2, 3 (3-sym only; 3-digit NO-GO, not built), 6, §2 row A, §3's Unit-A paragraph and its four pricing observations. Mathematics: `results/c2-m2/separation-note.md` §5 (clause 4; b₁ ≤ ‖B′‖₁²), §7.1, §7.2 (clause 7, with check-O §12.3's corrected 8t²B̂(2tL)²), addendum A1 ((R*); "t ≥ 21L implies it"); `check-O.md` §12.2, §12.3. Pattern: the M4 (iii) unit (`BUILD-NOTES-iii.md`, `SHARED.md`, `verify-iii/`, `CHECK-O-iii.md`), repeated with the suffix `-A`. Tree `~/rh-lean-work/zeta-23-lean-main` (Lean `v4.33.0-rc2`, Mathlib `51e6992e`), mirror `rh-program/lean/` (`cmp`-identical for every file below; `verify-A/untouched.log`). Not independently checked yet: Job 2 (Opus 5, clean clone; `CHECK-O-A.md`) is the next step. No commit by this job (the watchdogs commit). Stage log with machine-clock timestamps: `results/c2-m4/SHARED.md` (the Unit A blocks). Nothing here is about ζ, RH or the prime side.

**Label, verbatim and binding, for the assembly of this unit (PRICING-RESIDUE §2 row A):** **"Theorem M2's clause-6 assembly is a Comparator-checked theorem over `SepConfig`, modulo the displayed H-edge, H-B‴ and H-out, on the three standard axioms, replayed by nanoda — with b₁ = ‖B′‖₁² proved, clause 7 folded, and (R*) implied by t ≥ 21L as a proved corollary" — never "Theorem M2 is formalized".** For the rung: "clause 4 of Theorem M2 is kernel-checked modulo H-B‴, with b₁ = ‖B′‖₁² proved" — never "clause 4 is formalized".

## 0. Which of the four pieces landed (brief §"The four deliverables"): ALL FOUR; no stop line fired

| piece | landed as | stop line | fired? |
|---|---|---|---|
| 1. 3-sym (a)–(c) | `Zeta23/Separation/B1Sym.lean` (222 lines): `abs_mul_norm_paperFT_Bc_le_integral`, `integral_norm_deriv_Bc` (= 2e^{−1}/Z), `b1sym`, `four_le_b1sym`, `hb1sym` | the `deriv B` sign step > 120 lines | NO — the sign step (`hasDerivAt_Braw` … `deriv_B_nonneg`) is 60 lines |
| 2. the re-stated pairs | `SeparationClause4b` (H-B‴ only) and `Separation6b` (three theorems), both Comparator PASS with nanoda | `absorb` does not close at 39/1000 with b₁ ≥ 4 | NO — `absorb_b` closes at 39/1000 and 1/1000 with `four_le_b1sym` only (the intermediate ℓ + 73L ≤ 2.71(Lℓ)² is replaced by ℓ + 73L ≤ (Lℓ)²; the closing step is 2bC₁ ≤ 0.624·b²C₁² from bC₁ ≥ 4) |
| 3. clause 7 | `wsum_double_plus` (= 0), `wsum_double_minus`, `clause7_tight_pair`; `separation_clause7_tight_pair` in the challenge | the double at −t is not 2·(2t)²‖B̂(−2tL)‖² | NO — `wsum_double_minus : mult ⟨1/2, −t⟩ = 2 → wsum mult (ftest t L) ⟨1/2, −t⟩ = 2·(2t)²·‖paperFT B (−2tL)‖²` (check-O §12.3's 8t²B̂(2tL)², B̂ even; not the note body's 16t²) |
| 4. `rstar_of_21L` | `Zeta23.Separation.rstar_of_21L` (library) and `rstar_of_21L` (challenge, third theorem) | the chain's margin negative at (1050, 50, 1/2) | NO — `linarith` closes the chain on the whole region; numerically the chain's own margin at (1050, 50, 1/2) is 40.1 nats (exact 50.38; A1's 50.4; the pricing's ≥ 47 used sharper constants) |

Pricing observation §0 (i) — "every consumer wants b₁ from below" — VERIFIED at the rung: `inWindowNoise_le_b` needs 4‖B‴‖₁²/L⁴ ≤ b₁ (0.264 ≤ 1 ≤ 4 ≤ b₁sym at L ≥ 50) and `absorb_b` needs b₁C₁ ≥ 4; neither needs a lower bound on Z. The only lower bound on Z in the unit is `one_div_eighteen_le_Z` (Z ≥ 1/18), PROVED, used inside `rstar_of_21L`'s C_B step (`log_CB_le`) only, displayed nowhere, in no statement (`verify-A/digit-grep-A.log`).

## 1. What was run, where, by what (brief rule 1)

* Runner `verify-A/run.sh` — a byte copy of `verify-iii/run.sh` (comparator v4.33.0, lean4export v4.33.0-rc2, nanoda 0.4.17, `fake-landrun.sh` shim: NOT sandboxed, as `COMPARATOR-RUN.md` §2 explains). Every run from the repository root, `lake env comparator <config>`, comparator building the comparator-layer modules itself after the pre-run cleanup (`verify-A/prerun-cleanup.log`: 30 artifacts before the CONTROL run; the topic's artifacts before each of the two runs).
* **CONTROL run (`comparator/config.json`, the parent's fifteen theorems): PASS** — `verify-A/control-run.log`, 19:22:03–19:24:58 IST, `174.54 real 138.96 user 17.74 sys`, lake `8699 jobs` / `8877 jobs` (identical to the D1, M4 (i), M4 (iii) records), `Nanoda kernel accepts the solution` / `Lean default kernel accepts the solution` / `Your solution is okay!`, exit 0. `lake build Zeta23` before any edit: *Build completed successfully (9148 jobs)*, 0 errors (`verify-A/lake-build-before.log`).

## 2. Files and declarations (line numbers; tree = mirror)

New files only; the ONE edit to an existing Lean file is the two additive imports in `Zeta23.lean` (`import Zeta23.Separation.B1Sym`, `import Zeta23.Separation.Assembly2`; `verify-A/untouched.log`). The old pairs `SeparationClause4` / `Separation6` and the trusted `SepConfig.lean` / `Separation6.lean` are untouched (frozen-area `git diff --stat` empty) and on the frozen probe. `ChallengeDeps/Separation6b.lean` IMPORTS the frozen `ChallengeDeps.Separation6` and adds one definition, so `Rstar`, `Hedge`, `HB3`, `Hout`, `orbit`, `edge`, `SepConfig`, `W`, `ftest` are the SAME declarations the M4 (iii) runs checked (identity by import, not by copy). `Hb1` stays defined in the frozen `SepConfig.lean`, consumed by no statement of this unit.

```
# decls-A.txt — 2026-09-24 19:49:16 IST; declaration list with line numbers, the nine Unit A Lean files (tree = mirror)
## Zeta23/Separation/B1Sym.lean (222 lines)
28:import Zeta23.Separation.LemmaG
41:def b1sym : ℝ := (2 * Real.exp (-1) / Z) ^ 2
46:theorem abs_mul_norm_paperFT_Bc_le_integral (η : ℝ) :
63:theorem Braw_of_abs_lt {u : ℝ} (hu : |u| < 1 / 2) : Braw u = Real.exp (-1 / (1 - 4 * u ^ 2)) := if_pos hu
66:theorem hasDerivAt_Braw {u : ℝ} (hu : |u| < 1 / 2) :
85:theorem deriv_Braw_of_abs_lt {u : ℝ} (hu : |u| < 1 / 2) :
90:theorem deriv_B (u : ℝ) : deriv B u = deriv Braw u / Z := by
94:theorem hasDerivAt_B (u : ℝ) : HasDerivAt B (deriv B u) u :=
97:theorem continuous_deriv_B : Continuous (deriv B) := (B_contDiff (n := 1)).continuous_deriv_one
100:theorem deriv_B_eq_zero_of_half_le {u : ℝ} (hu : 1 / 2 ≤ |u|) : deriv B u = 0 := by
118:theorem deriv_B_nonpos {u : ℝ} (h0 : 0 ≤ u) (h1 : u ≤ 1 / 2) : deriv B u ≤ 0 := by
133:theorem deriv_B_nonneg {u : ℝ} (h0 : -1 / 2 ≤ u) (h1 : u ≤ 0) : 0 ≤ deriv B u := by
148:theorem B_zero : B 0 = Real.exp (-1) / Z := by
152:theorem integral_norm_deriv_Bc : ∫ u, ‖iteratedDeriv 1 (fun v => (B v : ℂ)) u‖ = 2 * Real.exp (-1) / Z := by
187:theorem Braw_le_exp_neg_one (v : ℝ) : Braw v ≤ Real.exp (-1) := by
196:theorem Z_le_exp_neg_one : Z ≤ Real.exp (-1) := by
204:theorem four_le_b1sym : 4 ≤ b1sym := by
213:theorem hb1sym (η : ℝ) : (|η| * ‖paperFT (fun v => (B v : ℂ)) η‖) ^ 2 ≤ b1sym := by
## Zeta23/Separation/Assembly2.lean (461 lines)
37:import Zeta23.Separation.Assembly
38:import Zeta23.Separation.B1Sym
51:theorem term_le_b1sym {L : ℝ} (hL : 0 < L) (d : ℝ) :
64:theorem inWindowNoise_le_b {C₁ t L R : ℝ} (carrier : Set ℂ) (mult : ℂ → ℕ)
116:theorem absorb_b {C₁ t δ L : ℝ} (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2) (hL1 : 25 / δ ≤ L)
223:theorem clause6_assembly_b {C₁ t δ L : ℝ} (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
276:theorem wsum_double_plus {mult : ℂ → ℕ} {t L : ℝ} (hL : 0 < L) :
283:theorem wsum_double_minus {mult : ℂ → ℕ} {t L : ℝ} (hL : 0 < L) (hm : mult ⟨1 / 2, -t⟩ = 2) :
294:set_option linter.unusedVariables false in
299:theorem clause7_tight_pair {C₁ t δ L : ℝ} (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
328:theorem log_le_div_403_add_five {s : ℝ} (hs : 0 < s) : Real.log s ≤ s / 403 + 5 := by
341:theorem cB_ge : 1429 / 10000 ≤ cB := by
352:theorem exp_neg_four_thirds_le_Braw {v : ℝ} (hv : |v| ≤ 1 / 4) : Real.exp (-4 / 3) ≤ Braw v := by
364:theorem one_div_eighteen_le_Z : 1 / 18 ≤ Z := by
386:theorem log_CB_le : Real.log CB ≤ Real.log 25 + 2 := by
403:theorem rstar_of_21L {t δ L : ℝ} (ht : 3 ≤ t) (hL : 50 ≤ L) (hδ1 : 25 / L ≤ δ) (hδ : δ ≤ 1 / 2)
## comparator/ChallengeDeps/Separation6b.lean (42 lines)
29:import Mathlib
30:import ChallengeDeps.Separation6
38:def b1sym : ℝ := (2 * Real.exp (-1) / Z) ^ 2
## comparator/Challenge/SeparationClause4b.lean (43 lines)
33:import ChallengeDeps.Separation6b
39:theorem separation_clause4_in_window_noise_b (C₁ t L R : ℝ) (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hL : 50 ≤ L) (hR : 1 ≤ R)
## comparator/Solution/SeparationClause4b.lean (34 lines)
19:theorem below has exactly the statement of its Challenge namesake and uses only the permitted axioms.
23:import ChallengeDeps.Separation6b
24:import Zeta23.Separation.Assembly2
30:theorem separation_clause4_in_window_noise_b (C₁ t L R : ℝ) (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hL : 50 ≤ L) (hR : 1 ≤ R)
## comparator/Challenge/Separation6b.lean (100 lines)
49:import ChallengeDeps.Separation6b
56:theorem separation_clause6_assembly_b (C₁ t δ L : ℝ) (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
72:set_option linter.unusedVariables false in
77:theorem separation_clause7_tight_pair (C₁ t δ L : ℝ) (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
97:theorem rstar_of_21L (t δ L : ℝ) (ht : 3 ≤ t) (hL : 50 ≤ L) (hδ1 : 25 / L ≤ δ) (hδ : δ ≤ 1 / 2)
## comparator/Solution/Separation6b.lean (78 lines)
25:import ChallengeDeps.Separation6b
26:import Zeta23.Separation.Assembly2
33:theorem separation_clause6_assembly_b (C₁ t δ L : ℝ) (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
50:set_option linter.unusedVariables false in
55:theorem separation_clause7_tight_pair (C₁ t δ L : ℝ) (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
76:theorem rstar_of_21L (t δ L : ℝ) (ht : 3 ≤ t) (hL : 50 ≤ L) (hδ1 : 25 / L ≤ δ) (hδ : δ ≤ 1 / 2)
## comparator/PrintAxioms/SeparationClause4b.lean (22 lines)
20:import Solution.SeparationClause4b
22:#print axioms separation_clause4_in_window_noise_b
## comparator/PrintAxioms/Separation6b.lean (22 lines)
18:import Solution.Separation6b
20:#print axioms separation_clause6_assembly_b
21:#print axioms separation_clause7_tight_pair
22:#print axioms rstar_of_21L
```

Decisions: (i) 3-sym in two files — `B1Sym.lean` (imports `LemmaG` only: the three b₁ lemmas) and `Assembly2.lean` (imports `Assembly` + `B1Sym`: the consumers, clause 7, `rstar_of_21L`) — so the b₁ proof has no dependency on the assembly. (ii) `absorb_b` and `clause6_assembly_b` are re-proofs with `b1sym` as an opaque real (`set b := b1sym`; only `four_le_b1sym` is used); the theorem's conclusion and the two constants 39/1000, 1/1000 are unchanged. (iii) `clause7_tight_pair` / `separation_clause7_tight_pair` keep the assembly's conclusion (the contract's "same conclusion; literally `clause6_assembly_b` applied"); the four carrying hypotheses (the two points in `Z'.carrier`, multiplicity 2 at each) are therefore unused by the proof, and `set_option linter.unusedVariables false in` precedes that theorem in the library, the challenge and the solution — the double's accounting lives in the two library lemmas. (iv) `rstar_of_21L`'s binders are Piece 6's (`25 / L ≤ δ`, where the assembly writes `25 / δ ≤ L`); not identified in Lean. (v) No `Real.log 5`, `log 2` or `log 18` numerics: log 5 is dropped by (4t² + δ²)/((27/20)δ²) ≤ s⁴, log 18 ≤ log 25 reuses `log25_le`, log s uses the tangent at e⁶.

## 3. Checks (every acceptance line verbatim in the logs)

* **Builds.** `lake build Zeta23.Separation.B1Sym`: *2841 jobs*, 0 errors, 0 warnings from the module. `lake build Zeta23.Separation.Assembly2`: *2844 jobs*, 0 errors, 0 warnings. `lake build Solution.SeparationClause4b Solution.Separation6b`: *8711 jobs*, 0 errors, 0 warnings from the new modules. Full `lake build Zeta23` after the root imports: **9150 jobs** (the M4 (iii) record's 9148 plus two), 0 errors (`verify-A/lake-build.log`).
* **`#print axioms`.** The four root theorems (`verify-A/print-axioms-clause4b.log`, `print-axioms-separation6b.log`): `[propext, Classical.choice, Quot.sound]` ×4. Every theorem of `B1Sym.lean` and `Assembly2.lean` — 29 theorems (`verify-A/print-axioms-library-A.log`, probe `axioms_A_probe.lean.txt`): the standard three ×29, nothing else.
* **Trust greps** (`verify-A/trust_greps_A.py`, comments stripped, nine files; `trust-greps-A.log`): exactly the four deliberate challenge `sorry`s (`SeparationClause4b.lean` 43; `Separation6b.lean` 70, 93, 100). **Digit grep** (`digit-grep-A.log`; 8.7, 87/10, 10.99, 1099, 0.22, 10.98, Z_lo, 1/18, "eighteen", code lines only): only `one_div_eighteen_le_Z` and its use in `log_CB_le`.
* **Statement identity** (`statement_identity_A.py`): `separation_clause4_in_window_noise_b` 291 bytes IDENTICAL (`statement-identity-clause4b.log`); `separation_clause6_assembly_b` 889, `separation_clause7_tight_pair` 1057, `rstar_of_21L` 143 bytes, all IDENTICAL (`statement-identity-separation6b.log`); RESULT PASS both.
* **Frozen probe** (`frozen_probe.lean.txt`, `frozen-statements.log`): TWELVE statements — the six D1/R1, the three M4 (i) root statements + the G1 rung, and the two M4 (iii) root statements (`separation_clause4_in_window_noise`, `separation_clause6_assembly`) — `#check` text and `#print axioms` line byte-identical to `verify-iii/frozen-statements.log` for the ten it records (10 of 10), and the two M4 (iii) statements recorded here for the first time, on the standard three.
* **Comparator run, topic `SeparationClause4b` (`verify-A/comparator-run-clause4b.log`): PASS** — `Built ChallengeDeps.Separation6b (2.8s)`, `Built Challenge.SeparationClause4b (2.9s)` with its one deliberate `sorry` warning (39:8), *8701 jobs*; `Built Solution.SeparationClause4b (2.9s)`, *8710 jobs*; `Nanoda kernel accepts the solution` / `Lean default kernel accepts the solution` / `Your solution is okay!`; `77.57 real 65.28 user 18.93 sys`; `--- comparator exit code: 0 ---`.
* **Comparator run, topic `Separation6b` (`verify-A/comparator-run-separation6b.log`): PASS** — `Built Challenge.Separation6b (2.0s)` with its three deliberate `sorry` warnings (56:8, 77:8, 97:8), *8701 jobs*; export of `separation_clause6_assembly_b separation_clause7_tight_pair rstar_of_21L` from challenge and solution; `Built Solution.Separation6b (3.0s)`, *8710 jobs*; `Nanoda kernel accepts the solution` / `Lean default kernel accepts the solution` / `Your solution is okay!`; `87.95 real 75.62 user 18.83 sys`; `--- comparator exit code: 0 ---`. Five shim `WARNING: THIS IS NOT REAL LANDRUN!` lines per run (not sandboxed, as in the D1 record).
* **Untouched** (`verify-A/untouched.log`): `git status` of `lean/` shows only the new files and the root's two imports; `git diff --stat HEAD` over the frozen areas (M4 (i) and M4 (iii) pairs, DBN, W1, PairCeiling, `LemmaG1`, `LemmaG`, `Clause4`, `Assembly`, `SepConfig`, `Separation6`) empty; tree = mirror for 31 Separation-related files + `formalization.yaml`.
* **10(g) lint:** no "clearly / obviously / easy to see / well known" and no British spellings in the nine Lean files, FIDELITY (t)/(s)/(w), the yaml additions or the SHARED blocks (grep at packaging).

## 4. Packaging

* **`lean/formalization.yaml`** (805 → 929 lines; tree copy `cmp`-identical): project description (the Unit A paragraph with the label), `status.scope` (the four new challenge `sorry`s named; H-b₁ no longer displayed for the new topics), two `main_results` entries (`separation_clause4_in_window_noise_b`; `separation_clause6_assembly_b` + `separation_clause7_tight_pair` + `rstar_of_21L`), fidelity paragraphs (t) with (t1), (s) with (s1)–(s2), (w) with (w1)–(w2), two `review.notes` paragraphs quoting the runs (`review.status` stays `self-assessed`), two `alignment.statements` rows. Validation (`verify-A/yaml-validation.log`, `results/d1-m2a/dr8/validate_yaml_sigma_strong.py`, the upstream schema re-fetched and IDENTICAL): **VALIDATION errors: 0; RESULT: PASS — errors: 0, undeclared names: 0** (main_results 24, alignment.statements 25).
* **`results/d1-m2a/packaging/FIDELITY.md`**: sections (t), (s), (w) appended (64 lines now).
* **Fidelity, in one line each:** (t1) b₁ is the real number (2e^{−1}/Z)² = ‖B′‖₁², proved; no digit asserted; the note's 8.70 not stated; the L-hypothesis stronger by log(10.984/8.70) = 0.233 nats; on the record L*(0.1, 10⁶; C₁ = 1) = 403.5 → 412.8 (4·0.233/0.1 = 9.33; a dated Instruments row, no headline). (s1) the double's contribution is 8t²‖B̂(2tL)‖² per check-O §12.3 (stated at −2tL, as the point gives it), not the body's 16t². (s2) "double at ±t" = multiplicity 2 on the two carrier points 1/2 ± it; the tight-pair theorem's proof is the assembly applied. (w1) the constant 21 enters as the corollary's hypothesis only; (q3) amended. (w2) the lemma's proof is a direct tangent-line chain (Z ≥ 1/18 proved and used there only); the statement is A1's. (q7) superseded; (p1)/(q4)'s "b₁ = 87/10 displayed" superseded for the new topics.
* Files written under `results/c2-m4/`: `BUILD-NOTES-A.md` (this file), `hashes-A.txt`, the Unit A blocks of `SHARED.md`, `verify-A/{run.sh, prerun-cleanup.log, control-run.log, lake-build-before.log, lake-build.log, comparator-run-clause4b.log, comparator-run-separation6b.log, print-axioms-clause4b.log, print-axioms-separation6b.log, print-axioms-library-A.log, axioms_A_probe.lean.txt, statement_identity_A.py, statement-identity-clause4b.log, statement-identity-separation6b.log, trust_greps_A.py, trust-greps-A.log, digit-grep-A.log, frozen_probe.lean.txt, frozen-statements.log, untouched.log, yaml-validation.log, decls-A.txt}`.

## 5. What an independent checker from a clean clone must do (Job 2, Opus 5; `CHECK-O-A.md`)

1. Clone `anthropics/zeta-23-lean` at tag `v1.0`, overlay `rh-program/lean/Zeta23/`, `lean/comparator/`, `lean/Zeta23.lean`, `lean/formalization.yaml` as `lean/README.md` says; `lake exe cache get`; `lake build Zeta23` (expect *9150 jobs*, 0 errors); `lake build Solution.SeparationClause4b Solution.Separation6b`.
2. `lake env lean comparator/PrintAxioms/SeparationClause4b.lean` and `…/Separation6b.lean`: four lines, each `[propext, Classical.choice, Quot.sound]`; the probe `verify-A/axioms_A_probe.lean.txt` on all 29 theorems of `B1Sym.lean` + `Assembly2.lean`.
3. Trust greps (`verify-A/trust_greps_A.py <clone-root> <the nine files>`): exactly the four challenge `sorry`s. The digit grep (`verify-A/digit-grep-A.log`'s patterns): NO digit of b₁ (8.7, 87/10, 10.99, 1099, 10.98) and NO lower bound on Z (0.22, Z_lo, 1/18) outside `one_div_eighteen_le_Z` and its one use in `log_CB_le` — the brief's item (i), weighed hardest. Statement identity (`statement_identity_A.py`) for both topics. The character-for-character claim: `Separation.b1sym` (`ChallengeDeps/Separation6b.lean`) versus `Zeta23.Separation.b1sym` (`B1Sym.lean`) — `diff` of the `def` lines; and that `ChallengeDeps/Separation6b.lean` imports the frozen `ChallengeDeps.Separation6` rather than re-declaring anything.
4. The fidelity items (t1), (s1)–(s2), (w1)–(w2) one by one against PRICING-RESIDUE §1 Pieces 2, 3, 6 and the note's §5, §7.2, A1; in particular (ii) that `absorb_b` closes at the SAME 39/1000 and `separation_clause6_assembly_b`'s conclusion is unchanged (diff the two challenge statements: `hb1` gone, `87 / 10` → `Separation.b1sym`, nothing else), and (iii) that `wsum_double_minus`'s value matches check-O §12.3 and the tight-pair statement is the note's §7.2. A paper re-derivation of `integral_norm_deriv_Bc` (∫|B′| = 2B(0) = 2e^{−1}/Z) and of `rstar_of_21L`'s chain (its margin ≈ 40 nats at (1050, 50, 1/2)). The record consequence: L*(0.1, 10⁶; C₁ = 1) = 403.5 → 412.8 — recompute it (4·log(10.9844/8.7)/0.1 = 9.326).
5. The three Comparator runs with nanoda from the clean clone (`verify-A/run.sh` pattern; do NOT pre-build the comparator layer): CONTROL first, then `config-separation-clause4b.json`, `config-separation6b.json` (three theorem names).
6. The twelve frozen statements (`verify-A/frozen_probe.lean.txt`) against `verify-A/frozen-statements.log` and `verify-iii/frozen-statements.log`; the yaml schema validation; 10(g) lint.

## 6. SHA-256 (`hashes-A.txt`; this file's own hash is in `SHARED.md`'s final Unit A block and in the chat report)

**[DATED 2026-09-24 20:25 IST, orchestrator — the checker's three MINOR notes (`CHECK-O-A.md`): M1 the composed assembly with t ≥ 21L in place of (R*) is not shipped (FIDELITY (w1) says so; optional later); M2 the chain margin reads "39" in the `Assembly2.lean` header and "40.1" here (both correct: 39.6–40.1); M3 the `linter.unusedVariables` option is needed only in the library copy. No number or label moves.]**
