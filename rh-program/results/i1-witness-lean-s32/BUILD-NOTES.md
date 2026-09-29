# I.1 witness table in Lean — the Comparator pairs `EpsteinWitnessSix` (rung 1, Λ_Q(6)) and `I1Witness` (the table: Λ_Q(36) < 0, κ > 0, Λ_DH(3) < 0, Λ_DH(12) < 0, Λ_DH(4) < 0, Λ_DH(6) > 0, and the recursion as a theorem), built over Mathlib alone — build notes (BUILDER, Fable 5.1; Session 32, 2026-09-29 07:22 – 07:53 IST)

Brief: `results/i1-witness-lean-s32/BRIEF.md` (SHA-256 `54ad13fb0b6197d241bae84de43942d6e1e7396bc0050eb965cc503f62aa3b69`, recomputed at the
start). Record: `results/c3-r/m0-axiom-note.md` §6.1–§6.2; `results/c3-m0-epstein/n1_epstein_witness.{json,py}`; zoo I.1 and line 666.
Pattern: the D5 and H5 units (`results/d5-lean-s30/`, `results/h5-c2-lean-s32/` — BRIEF, BUILD-NOTES, FIDELITY, CHECK-O) and the packaging
standard (`lean/README.md` "Packaging", `results/d1-m2a/packaging/COMPARATOR-RUN.md`). Tree: the program's built clone
`~/rh-lean-work/checker-clone-s21` (Lean `v4.33.0-rc2`, commit d8b18978; Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`) — the only
toolchain. Mirror: `rh-program/lean/` is the source of truth; direction rh-program → clone by `cp`; `cmp`-identical for the seven topic
files and two configs at the end (`trust-greps.log`). No Zeta23 module is imported on either side (the trusted file imports `Mathlib`
only). Not independently checked yet: the Opus 5 clean-clone check (`CHECK-O.md`) is the next job. No commit by this job. Stage log with
`date` stamps: `results/i1-witness-lean-s32/SHARED.md`.

**Nothing about ζ or RH follows from anything below (10(c), first paragraph).** The theorems are VALUES of the von Mangoldt recursion on
two coefficient arrays (Epstein x² + 5y² with b₁ = 1; Davenport–Heilbronn a_n = (1, κ, −κ, −1, 0) mod 5), with log n replaced by the
exponent vector. The identification of the recursion's coefficient sequence with −F′/F for F(s) = Σ b_n n^{−s} is the classical identity
and is NOT formalized (FIDELITY (F-a)); nothing is stated about the Euler product of either function, about the Davenport–Heilbronn
function itself (series, continuation, functional equation, off-line zero), about the zeros of any Epstein zeta function, or about ζ.
This is a hardening of I.1's witness table from "computationally-verified" to kernel-checked, not an attack under the sponsor's criterion.

**Label, verbatim and binding (BRIEF §1(4)), earned — everything landed with NO displayed hypothesis:** **"I.1's witness table
kernel-checked — for the Epstein form x² + 5y² (h = 2), Λ_Q(36) = −4 log 2 − 4 log 3 < 0 (and Λ_Q(6) = 2 log 6 off prime powers); for
Davenport–Heilbronn, Λ_DH(3) = −κ log 3 < 0 and Λ_DH(12) = −κ(1 + κ²) log 12 < 0 with κ > 0 from its closed form — where Λ_f is the von
Mangoldt recursion's coefficient sequence on the array with b₁ = 1; over Mathlib alone, the three standard axioms, replayed by nanoda; the
identification of that sequence with −F′/F as Dirichlet series is not formalized"** — never "I.1 formalized"; never "DH has no Euler
product" as a theorem; nothing about ζ or RH. The refutation-shaped close (10(c)) is the "Lands" branch: I.1's axiom-level filter has
kernel-checked witnesses — Λ_Q(36) < 0 for x² + 5y² and Λ_DH(3), Λ_DH(12) < 0 for Davenport–Heilbronn — as values of the von Mangoldt
recursion on the coefficient arrays; I.1's STATUS may gain a `witnesses kernel-checked` rider at the next zoo stream (the orchestrator's
call).
Stop lines (BRIEF §2): none fired — (i) the n = 36 `decide` costs about 3.6 s of kernel time per coefficient, not minutes, so the 10(j)
split was not needed and E2 is SHIPPED, not OPEN; (ii) no statement needed a hypothesis the record does not state; (iii) the build took
well under half a slot (thirty-one minutes of wall clock from the first read to this file, both `lake build`s first try); (iv) the pre-derivation of (D2) is correct in
every value (§0).

## 0. The attack on the pre-derivation (deliverable 1; `PREDERIVATION-ERRATA.md`)

Every line of §0's (D2) derivation, every a_n it uses, every Epstein count and recursion value behind (E1)/(E2), the box-count definition
and the κ > 0 chain were re-derived by hand against the record and the on-disk script (`lam_exact`). Verdict: NO error that changes a
value (E1–E6, E10, E12: checks, no error). Two gaps of presentation, closed inside the proofs without changing a statement: **E7** — the
∀ p clause of (E2) is not a `decide` but the lemma `¬ p ∣ n → lambdaVec b n p = 0` plus "a prime dividing 2²·3² is 2 or 3"; **E13** — the
brief's "hence" from the two coefficients to the real value needs the non-dividing primes' coefficients (p = 5 at n = 6; p = 2 at n = 3;
p = 5, 7, 11 at n = 12) to vanish, which is the same lemma. Two typing notes: **E8** — `LambdaReal` takes a real array, the Epstein array
is cast, and `lambdaVec` is shown to commute with the cast; **E9** — `padicValNat` reduces in the kernel (measured; I had expected the
opposite), so the exponent is the brief's `padicValNat p n` with no replacement. One cost note, **E11** — the measured kernel times.

## 1. Files and statement decisions

| file | lines | content |
|---|---|---|
| `comparator/ChallengeDeps/I1Witness.lean` | 79 | the trusted layer, Mathlib only, namespace `I1Witness`: `lambdaVecAux` (fuel-structural recursion), `lambdaVec b n p := lambdaVecAux b p n n`, `LambdaReal`, `epsteinB`, `kappa`, `dhA`, each with a docstring restating the record's sentence; header with the NOT-formalized paragraph |
| `comparator/Challenge/EpsteinWitnessSix.lean` | 50 | rung 1: `epsteinB_one`, `epstein_six_coeff`, `epstein_witness_6`; `sorry`; header with the WHAT IS CLAIMED / what is NOT paragraph |
| `comparator/Challenge/I1Witness.lean` | 114 | the unit: `lambdaVec_rec`, `lambdaVec_one`, `lambdaVec_eq_zero_of_not_dvd`, `epsteinB_one`, `epstein_thirtysix_coeff`, `epstein_witness_36`, `kappa_pos`, `dhA_one`, `dh_three_coeff`, `dh_witness_3`, `dh_twelve_coeff`, `dh_witness_12`, `dh_four`, `dh_six`; `sorry`; the same paragraph, with (R)/(E)/(D) |
| `comparator/Solution/EpsteinWitnessSix.lean` | 144 | Mathlib only; namespace `EpsteinWitnessSix.Proof`: `lambdaVecAux_stable`, `lambdaVec_rec`, `lambdaVec_one`, `lambdaVec_zero`, `lambdaVec_eq_zero_of_not_dvd`, `lambdaVec_ratCast`, `prime_dvd_two_three`, `coeff_two`, `coeff_three` (`decide +kernel`); the three root theorems |
| `comparator/Solution/I1Witness.lean` | 305 | its own copy of the general lemmas (namespace `I1WitnessProof`: `lambdaVecAux_stable`, `rec'`, `one'`, `zero'`, `not_dvd'`, `ratCast'`, `prime_dvd_two_three`), the kernel facts `e36_two`, `e36_three` (`decide +kernel`), `e36_other`, `kpos`, the DH coefficients `d2`, `d3`, `d4`, `d6_two`, `d6_three`, `d12_two`, `d12_three`, the sum collapse `sum_two_three`, `log6`, `log12`; the fourteen root theorems |
| `comparator/PrintAxioms/EpsteinWitnessSix.lean`, `PrintAxioms/I1Witness.lean` | 22, 33 | the quick checks (3 and 14 names) |
| `comparator/config-epstein-witness-six.json`, `config-i1-witness.json` | — | 3 and 14 names; `propext`, `Quot.sound`, `Classical.choice`; `enable_nanoda: true` |
| `lean/formalization.yaml` | 1406 | a description paragraph, a `status.scope` sentence, a `main_results` entry, fidelity row (y), four `alignment.statements` rows; validator PASS (`yaml-validation.log`: errors 0, undeclared names 0; '(y)' occurs once) |
| `lean/README.md` | 627 | section "I1Witness (Session 32, 2026-09-29)" between "WeilContainmentC2" and "IntegralityGap" |

**Statement decisions, against BRIEF §0–§1.** The brief's statements are informal Lean; what is shipped is: (E1) `lambdaVec epsteinB 6 2 = 2
∧ lambdaVec epsteinB 6 3 = 2` as written, and the real value as `LambdaReal (fun n => (epsteinB n : ℝ)) 6 = 2 * Real.log 2 + 2 * Real.log 3`
with `0 < …` — the brief's `LambdaReal epsteinB 6` needs the cast (ERRATA E8); (E2) `lambdaVec epsteinB 36 2 = -4 ∧ lambdaVec epsteinB 36 3 =
-4 ∧ ∀ p, p.Prime → p ≠ 2 → p ≠ 3 → lambdaVec epsteinB 36 p = 0` as written, and `epstein_witness_36` with `-4 * Real.log 2 - 4 * Real.log 3`
and `< 0`; (D1) `lambdaVec dhA 3 3 = -kappa` and `LambdaReal dhA 3 = -kappa * Real.log 3 ∧ LambdaReal dhA 3 < 0`; (D2) `lambdaVec dhA 12 2 =
-kappa * (1 + kappa ^ 2) * 2 ∧ lambdaVec dhA 12 3 = -kappa * (1 + kappa ^ 2)` and `LambdaReal dhA 12 = -kappa * (1 + kappa ^ 2) * (2 * Real.log 2
+ Real.log 3) ∧ … < 0`; (D3) both rows, each as one theorem with coefficient(s), real value, sign. Additions, each recorded in FIDELITY §3:
a second form of each real value as a conjunct (`= 2 * Real.log 6`, `= -4 * Real.log 6`, `= -kappa * (1 + kappa ^ 2) * Real.log 12`) — the
record's own forms; the three recursion lemmas (R) so that the trusted fuel definition is certified to BE the record's recursion; `dhA_one`
(the DH normalization, a₁ = 1). Not added: any statement about the Dirichlet series, the Euler product, or a zero. The trusted definitions are
the brief's, with two decisions: the fuel (rung 0, `typing.log`) and `noncomputable section` around the four real/rational definitions
(compiler only; FIDELITY (D10)). Each solution is self-contained (neither imports the challenge or the other solution).

## 2. Rung 0, rung 1 (BRIEF §0, §2 items 2–3) and the unit (§2 item 4): PASS

**Rung 0 (`typing.log`).** `lambdaVec` is defined by structural recursion on a fuel argument set to n (a well-founded definition would not
reduce under `decide`); the record's recursion is a theorem (`lambdaVec_rec`, proved by showing the fuel irrelevant once ≥ n). Measured
kernel times, one theorem per file (`set_option profiler true`, `decide +kernel`): `epsteinB 6 = 2` 19 ms; `epsteinB 36 = 3` 772 ms;
`lambdaVec epsteinB 6 2 = 2 ∧ lambdaVec epsteinB 6 3 = 2` 77 ms; `lambdaVec epsteinB 36 2 = -4` 3.62 s; `lambdaVec epsteinB 36 3 = -4` 3.55 s;
`padicValNat 2 36 = 2 ∧ padicValNat 3 36 = 2` 0.56 ms (and the negative control `¬(padicValNat 2 36 = 3)` decided). Route for n = 36: the
direct `decide +kernel` on the recursion, one conjunct per `decide`; no split.

**Rung 1, topic `EpsteinWitnessSix`.** `lake build Solution.EpsteinWitnessSix`: first try, *Build completed successfully (8698 jobs)*, 0
errors, 0 warnings, `Built ChallengeDeps.I1Witness (2.8s)`, `Built Solution.EpsteinWitnessSix (4.0s)`, 9.43 s real. `rung1-print-axioms.log`:
three lines, each `[propext, Classical.choice, Quot.sound]`. `rung1-statement-identity.log`: 3 IDENTICAL on the tree and on the mirror
(`tools/statement_identity_i1.py` = the H5 tool, byte-copied). `rung1-trust-greps.log` (RERUN section — the first section passed the four
file names as one argument, the zsh word-splitting slip the D5 and H5 records also logged; kept and superseded): the 3 deliberate challenge
`sorry`s only; imports Mathlib / `ChallengeDeps.I1Witness` / `Solution.*` only; tree = mirror. `rung1-prerun-cleanup.log`: the topic's and the
trusted module's 16 build artifacts removed so that comparator builds every comparator-layer module itself. **Comparator
(`rung1-comparator.log`): PASS** — 07:40 IST, `30.45 real`, max RSS 5.96 GB, the runner `tools/run.sh` (the H5 runner byte for byte but for
its comment line; comparator v4.33.0, lean4export v4.33.0-rc2, nanoda 0.4.17, the fake-landrun shim — NOT sandboxed, as in every prior
macOS record; the four tool SHA-256s printed in the log equal COMPARATOR-RUN.md §1's), `Built ChallengeDeps.I1Witness (2.9s)`, `Built
Challenge.EpsteinWitnessSix (2.9s)` with its three deliberate `sorry` warnings, `Built Solution.EpsteinWitnessSix (3.2s)`, `Nanoda kernel
accepts the solution`, `Lean default kernel accepts the solution`, `Your solution is okay!`, exit 0. The unit was not started until this
run had passed.

**The unit, topic `I1Witness`.** `lake build Solution.I1Witness` (`build-i1witness.log`): first try, *Build completed successfully (8698
jobs)*, 0 errors, 0 warnings, `Built Solution.I1Witness (10s)`, 12.26 s real. `print-axioms.log`: fourteen lines, each `[propext,
Classical.choice, Quot.sound]`. `statement-identity.log`: 14 + 14 IDENTICAL (tree, mirror). `trust-greps.log`: over all seven topic files,
the 3 + 14 deliberate challenge `sorry`s and nothing else (the `grep "^import"` section shows one hit on the word "imports" inside the
solution's header comment); tree = mirror for the seven files and two configs. `prerun-cleanup.log`: 32 artifacts removed (the unit's, the
trusted module's, and the rung-1 topic's rebuilt by its comparator run). **Comparator (`comparator-run.log`): PASS** — 07:45 IST, `48.15
real`, max RSS 7.10 GB, `Built ChallengeDeps.I1Witness (2.9s)`, `Built Challenge.I1Witness (2.0s)` with its fourteen deliberate `sorry`
warnings, `Built Solution.I1Witness (10s)`, `Nanoda kernel accepts the solution`, `Lean default kernel accepts the solution`, `Your
solution is okay!`, `--- comparator exit code: 0 ---`. What the runs established: each solution statement coincides constant for constant
with its challenge namesake (including the trusted `lambdaVec`, `LambdaReal`, `epsteinB`, `kappa`, `dhA`); the proofs use no axiom outside
the three (in particular no `Lean.ofReduceBool`: every decision is `decide +kernel`, never `native_decide`); nanoda re-checked the whole
solution export and Lean's kernel replayed it. No CONTROL run: the tool chain is unchanged since the Session 25 records and both topic
runs passed. Mathlib was never compiled from source (every build 8698 jobs with only the topic modules built).

## 3. Fidelity (FIDELITY.md; yaml row (y))

Covered: the seventeen statements of §1 as kernel facts — the recursion as a theorem, b₁ = 1 and a₁ = 1, the Epstein coefficients and
values at 6 and 36, κ > 0, the DH coefficients and values at 3, 4, 6, 12, with the signs. Not covered: the −F′/F identification (F-a); the
Davenport–Heilbronn function itself; anything about Epstein zeta functions beyond the coefficient array; the "no Euler product" reading;
every decimal value; the rest of the record's tables; zoo 666's axiom-format statement; ζ, RH, any zero. Differs from the prose: two objects
for the record's Λ (D1); the fuel (D2); `padicValNat` and the unused non-prime / n = 0 values (D3); r_Q as a box count (D4); the ℚ array
cast to ℝ (D5); `dhA` by `n % 5` (D6); `Real.sqrt` in `kappa` (D7); two forms of each value (D8); the additions (D9); `noncomputable
section` (D10). Fidelity divergences in the brief's sense (a hypothesis the record does not state): NONE.

## 4. What an independent checker from a clean clone must do (`CHECK-O.md`; BRIEF §3)

1. Clone `anthropics/zeta-23-lean` at tag `v1.0`, overlay `rh-program/lean/` as `lean/README.md` "Building" says; `lake exe cache get`;
   `lake build Solution.EpsteinWitnessSix`, then `Solution.I1Witness` (expect 8698 jobs each, 0 errors, 0 warnings; the second about
   10 s for the module).
2. `lake env lean comparator/PrintAxioms/EpsteinWitnessSix.lean` (3 lines) and `…/I1Witness.lean` (14 lines): each `[propext,
   Classical.choice, Quot.sound]`; no `sorryAx`, no `Lean.ofReduceBool`.
3. `tools/statement_identity_i1.py <clone> EpsteinWitnessSix <3 names>` and `… I1Witness <14 names>`; `tools/trust_greps_i1.py <clone> <the
   seven topic files>` (expect exactly the 17 challenge `sorry`s).
4. The two Comparator runs with nanoda from the clean clone (`tools/run.sh` pattern with the clone's path; do NOT pre-build the comparator
   layer): `config-epstein-witness-six.json`, then `config-i1-witness.json`.
5. Read every statement against BRIEF §0 and the record (`m0-axiom-note.md` §6 table; `n1_epstein_witness.json`); re-derive (D2)'s two
   coefficients by hand (ERRATA E4); re-derive the Epstein counts at the divisors of 36 (E5); re-derive every FIDELITY sentence — in
   particular (F-a) (does any statement mention a Dirichlet series? — grep the statements, not the comments), (D4) (does the box contain
   every solution?), (D7) (are both radicands positive?), (N4) (does any theorem say more than a value?); is any hypothesis present that
   the prose does not state; is the label exactly §1(4)'s.
6. Recompute every hash in `hashes.txt`; the yaml validation; the 10(g) lint.

## 5. Files written and SHA-256

`hashes.txt` (this directory) lists the SHA-256 of every file touched: the 9 topic files under `lean/comparator/`, `lean/formalization.yaml`,
`lean/README.md`, and every file under `results/i1-witness-lean-s32/` (this file's own hash is in `SHARED.md`'s final block and in the chat
report). Files under `results/i1-witness-lean-s32/`: `PREDERIVATION-ERRATA.md`, `typing.log`, `SHARED.md`, `BUILD-NOTES.md`, `FIDELITY.md`,
`hashes.txt`, the logs `rung1-print-axioms.log`, `rung1-statement-identity.log`, `rung1-trust-greps.log`, `rung1-prerun-cleanup.log`,
`rung1-comparator.log`, `build-i1witness.log`, `print-axioms.log`, `statement-identity.log`, `trust-greps.log`, `prerun-cleanup.log`,
`comparator-run.log`, `yaml-validation.log`, `lint-10g.log`, and `tools/{run.sh, statement_identity_i1.py, trust_greps_i1.py}`. Edits outside
this folder: `lean/` only (the nine topic files, the yaml, the README). 10(g) lint: U.S. English throughout; the four banned phrases absent
(`lint-10g.log`).


## Corrections after CHECK-O (08:10 IST 2026-09-29, Session 32; orchestrator, each re-derived at the file)

1. **F1 (lines 67, 75 and wherever `lambdaVec_rec` is called "the record's recursion"):** true for arrays with b₁ = 1 only — the solved form drops the b₁ factor; both shipped arrays have b₁ = 1 (`epsteinB_one`, `dhA_one`). FIDELITY (D11) carries the statement; the challenge header's "prime index p" (lines 20–22) overstates — the theorem holds for every p; Lean comments recorded, not edited.
2. **F2:** "no Dirichlet series, no −F′/F … appears in any file" reads "in any statement"; the phrases occur in comments and docstrings (FIDELITY corrected in place).
3. **F3:** `lambdaVec b 0 p = 0` comes from the fuel-0 clause, not the `n < 2` branch; `Finset.sum_eq_single` is named in a comment and in ERRATA but used by no solution (both corrected in place).
4. **F4 (line 82 and README lines 504–505):** the rung-1 build figures at line 82 (`Built ChallengeDeps.I1Witness (2.8s)`, `Built Solution.EpsteinWitnessSix (4.0s)`, 9.43 s real) are the builder's console reading and appear in no log on disk; `build-i1witness.log` covers the I1Witness build only. The clean-clone checker's cold builds (`check-O/`) are the logged record of both builds.
