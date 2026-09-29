# I.1 witness table — CHECK-O: the Opus 5 clean-clone check of the Comparator topics `EpsteinWitnessSix` and `I1Witness` (Session 32; BRIEF §3; KICKSTART 10(f), 10(j))

Checker: Opus 5, started Tue Sep 29 07:55:05 IST 2026 (machine clock). Contract: `BRIEF.md` §3 (SHA-256 `54ad13fb…aa3b69`, recomputed and
matched). Read in full before any run: `BRIEF.md`, `BUILD-NOTES.md`, `FIDELITY.md`, `PREDERIVATION-ERRATA.md`, `hashes.txt`, `typing.log`,
`SHARED.md`, every builder log in this folder, the nine shipped files under `lean/comparator/`, `lean/formalization.yaml` (the description
paragraph, the `status.scope` sentence, the `main_results` entry, row (y), the four alignment rows), `lean/README.md` §"I1Witness"; the record
`results/c3-r/m0-axiom-note.md` §6.1–§6.2, `results/c3-m0-epstein/n1_epstein_witness.json`, zoo I.1 (`BARRIER-ZOO.md` line 55 ff., both
Session-24 riders) and zoo line 666. The builder's tree `~/rh-lean-work/checker-clone-s21` was never used. Every log below is under
`results/i1-witness-lean-s32/check-O/`. Nothing committed; no file outside `results/i1-witness-lean-s32/` edited.

**Verdict: FIX-FIRST — four prose items F1–F4 (§8); the Lean statements, the proofs, the trusted definitions, the label and every run are
clean.** The one item with content is F1: the ledger and the challenge header call `lambdaVec_rec` "the record's recursion" for EVERY
array, but the solved form `Λ(n) = b_n e_p(n) − Σ_{d<n} Λ(d) b_{n/d}` is the record's recursion `b_n log n = Σ_{d|n} Λ(d) b_{n/d}` only when
b₁ = 1. No witness value is affected (both arrays have b₁ = 1, shipped as `epsteinB_one` and `dhA_one`).

## 1. Clean clone, cache, builds (`check-O/clone-build.sh`, `check-O/clone-build.log`)

`git clone https://github.com/anthropics/zeta-23-lean ~/rh-lean-work/checker-clone-s32-i1` (a NEW directory; retry loop), `git checkout
v1.0` → HEAD `3635e74826a4c1fcece7d1cd2b6fa75e43a00510` (tag `v1.0`); overlay per `lean/README.md` "Building" (`Zeta23/.`, `comparator/.`,
`Zeta23.lean`); toolchain `leanprover/lean4:v4.33.0-rc2`; `lake exe cache get` — "Decompressed 8489 already-cached file(s) … Completed
successfully"; Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`. Mathlib was not compiled from source (8698 jobs, only the topic modules
built). One `lake build` at a time:

| build | result | modules built | wall |
|---|---|---|---|
| `lake build Solution.EpsteinWitnessSix` (07:58:40) | *Build completed successfully (8698 jobs)*, rc 0, 0 errors, 0 warnings | `ChallengeDeps.I1Witness (6.9s)`, `Solution.EpsteinWitnessSix (3.3s)` | 12.97 s |
| `lake build Solution.I1Witness` (07:58:53) | *Build completed successfully (8698 jobs)*, rc 0, 0 errors, 0 warnings | `Solution.I1Witness (10s)` | 12.43 s |

The nine topic files in the clone are `cmp`-identical to `rh-program/lean/` (`check-O/identity-trust.log`, last section), and the seven
`.lean` files are untracked in the v1.0 checkout (`git status`: `??`), i.e. they come from the overlay only.

## 2. `#print axioms` and the kernel time of the n = 36 decision (`check-O/print-axioms.log`, `check-O/kernel-probe*.{lean,log}`)

`lake env lean comparator/PrintAxioms/EpsteinWitnessSix.lean`: 3 lines; `…/I1Witness.lean`: 14 lines; all 17 read `depends on axioms:
[propext, Classical.choice, Quot.sound]`; exit 0 each; `sorryAx` 0 hits, `Lean.ofReduceBool` 0 hits.

Kernel time, re-measured in the clean clone (`set_option profiler true`, `profiler.threshold 0`, `decide +kernel`, the checker's own probe
files). The profiler's "type checking" line is cumulative within one file; the single-theorem file fixes the reading:

| probe | type checking |
|---|---|
| `lambdaVec epsteinB 36 3 = -4`, alone in its file (`kernel-probe-single.log`) | **3.43 s** |
| `lambdaVec epsteinB 36 2 = -4` (first in `kernel-probe.log`) | **3.45 s** |
| `lambdaVec epsteinB 36 3 = -4` (increment) | 3.36 s |
| `lambdaVec epsteinB 36 5 = 0` (increment) | 3.3 s |
| `epsteinB 36 = 3` (increment) | 0.8 s |
| `epsteinB 9 = 3` (increment) | < 0.1 s |
| negative control `lambdaVec epsteinB 36 2 = -3` | REJECTED (`error: Tactic 'decide' failed`; exit 1) |

The builder's 3.62 s and 3.55 s per conjunct (`typing.log`) are reproduced to within 5 %. Note on the negative control: the rejection is
real, but the diagnostic Lean prints ("did not reduce to `isTrue` or `isFalse`") is the elaborator's fallback message, not a kernel
verdict of `false`; it shows that the kernel did not accept the wrong value, which is what a control needs.

## 3. Statement identity and trust greps on the clean clone (`check-O/identity-trust.log`, `check-O/overclaim-greps.log`)

The builder's `tools/statement_identity_i1.py`, run by the checker against the clone: 3/3 IDENTICAL (`EpsteinWitnessSix`), 14/14 IDENTICAL
(`I1Witness`), RESULT PASS each. The builder's `tools/trust_greps_i1.py` (comments stripped), the seven `.lean` files as seven arguments
(bash array): 17 hits, all `sorry` — 3 in `Challenge/EpsteinWitnessSix.lean`, 14 in `Challenge/I1Witness.lean`, none elsewhere; no
`axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `opaque`, `admit`, `ofReduceBool` outside comments (exit 1 is the tool's
response to any hit, here the 17 deliberate ones). The checker's own raw grep (`overclaim-greps.log`, comments NOT stripped): imports are
`Mathlib` (trusted file), `ChallengeDeps.I1Witness` (both challenges, both solutions), `Solution.*` (the two PrintAxioms files); no
`set_option`, `macro`/`elab`/`syntax`, `partial def` in any of the seven files. (A first attempt at this grep under zsh passed the seven
paths as one argument — the slip the D5 and H5 records logged; it was discarded and rerun under bash.)

## 4. Comparator runs with nanoda from the clean clone (`check-O/run-clone.sh`, `check-O/cleanup.sh`, `check-O/prerun-cleanup-*.log`, `check-O/comparator-*.log`)

Runner: the builder's `tools/run.sh` with only the tree path (and the comment line) changed to the clone (`diff` shown in the transcript;
two lines). Tool SHA-256s printed in both logs — comparator `fe1222e2…`, lean4export `de4ffedf…`, nanoda_bin `d6c87133…`, fake-landrun
`167507c8…` — each occurs in `results/d1-m2a/packaging/COMPARATOR-RUN.md` (1 hit each). NOT sandboxed (the fake-landrun shim), as in every
prior macOS record. Before each run the topic's and the trusted module's artifacts were removed (16 files each time, "remaining: 0"), so
comparator built every comparator-layer module itself.

| config | comparator output | nanoda | Lean kernel | exit | wall / max RSS |
|---|---|---|---|---|---|
| `comparator/config-epstein-witness-six.json` | `Built ChallengeDeps.I1Witness (2.9s)`, `Built Challenge.EpsteinWitnessSix (2.0s)` (3 deliberate `sorry` warnings), `Built Solution.EpsteinWitnessSix (3.2s)`, `Your solution is okay!` | `Nanoda kernel accepts the solution` | `Lean default kernel accepts the solution` | **0** | 30.42 s / 5.96 GB |
| `comparator/config-i1-witness.json` | `Built ChallengeDeps.I1Witness (2.9s)`, `Built Challenge.I1Witness (3.0s)` (14 deliberate `sorry` warnings, lines 45–111), `Built Solution.I1Witness (10s)`, `Your solution is okay!` | `Nanoda kernel accepts the solution` | `Lean default kernel accepts the solution` | **0** | 48.49 s / 7.11 GB |

Both configs list exactly the 3 and 14 names, `permitted_axioms` = `propext`, `Quot.sound`, `Classical.choice`, `enable_nanoda: true`.

## 5. Re-derivation by hand, independent of the builder's text (`check-O/rederive.py`, `check-O/rederive.log` — the checker's own script, from the record's definitions; the builder's code was neither imported nor run)

**(a) (D2), Davenport–Heilbronn at n = 12.** Array a_n = (1, κ, −κ, −1, 0) by n mod 5 (n ≡ 1, 2, 3, 4, 0): a₂ = κ, a₃ = −κ, a₄ = −1,
a₆ = a₁ = 1, a₁₂ = a₂ = κ. Recursion a_n log n = Σ_{d|n} Λ(d) a_{n/d} with Λ(1) = 0, a₁ = 1, so Λ(n) = a_n log n − Σ_{d|n, 1<d<n} Λ(d) a_{n/d}.
Λ(2) = κ log 2. Λ(3) = −κ log 3. Λ(4) = a₄ log 4 − Λ(2)a₂ = −2 log 2 − κ² log 2 = −(2 + κ²) log 2. Λ(6) = a₆ log 6 − [Λ(2)a₃ + Λ(3)a₂] =
log 6 + κ² log 2 + κ² log 3 = (1 + κ²) log 6. At n = 12 the divisors d with 1 < d < 12 are 2, 3, 4, 6 with 12/d = 6, 4, 3, 2:
Λ(2)a₆ + Λ(3)a₄ + Λ(4)a₃ + Λ(6)a₂ = κ log 2 + κ log 3 + κ(2 + κ²) log 2 + κ(1 + κ²)(log 2 + log 3).
Coefficient of log 2: κ + 2κ + κ³ + κ + κ³ = 4κ + 2κ³. Coefficient of log 3: κ + κ + κ³ = 2κ + κ³. Then Λ(12) = κ(2 log 2 + log 3) − that:
**log 2: 2κ − 4κ − 2κ³ = −2κ(1 + κ²); log 3: κ − 2κ − κ³ = −κ(1 + κ²)** — so `lambdaVec dhA 12 2 = −κ(1 + κ²)·2` and `lambdaVec dhA 12 3 =
−κ(1 + κ²)` as shipped, and Λ_DH(12) = −κ(1 + κ²)(2 log 2 + log 3) = **−κ(1 + κ²) log 12** (log 12 = 2 log 2 + log 3). The record's second form
−κ[κ² log 6 + (2 + κ²) log 2 + log 3] = −κ[(2 + 2κ²) log 2 + (1 + κ²) log 3], the same. The script (sympy, κ a symbol) returns
{2: −2κ(κ² + 1), 3: −κ(κ² + 1)} at 12, {2: −κ² − 2} at 4, {2: κ² + 1, 3: κ² + 1} at 6, {3: −κ} at 3 — every shipped coefficient.
Numerically Λ_DH(12) = −0.76287747198841, Λ_DH(3) = −0.31209272851616, Λ_DH(6) = +1.93635607662104 (record −0.762877471988…,
−0.3120927…, +1.93635607662…).

**(b) Epstein, Q = x² + 5y², at the divisors of 36.** By hand: r(1) = 2 [(±1, 0)]; r(2) = r(3) = 0; r(4) = 2 [(±2, 0)]; r(6) = 4 [(±1, ±1)];
r(9) = 6 [(±3, 0), (±2, ±1)]; r(12) = 0 [12, 7 not squares]; r(18) = 0 [18, 13]; r(36) = 6 [(±6, 0), (±4, ±2); y = ±1 gives 31, not a square].
b = r/2 = 1, 0, 0, 1, 2, 3, 0, 0, 3. Recursion in the exponent-vector basis. n = 6: p = 2: b₆·1 − [Λ(2)₂b₃ + Λ(3)₂b₂] = 2 − 0 = **2**;
p = 3 likewise **2**. n = 36, p = 2: b₃₆·e₂(36) = 3·2 = 6; the proper divisors contribute Λ(4)₂b₉ = (b₄·2)·3 = 6 and Λ(6)₂b₆ = 2·2 = 4, all
others 0 (Λ(2)₂ = b₂ = 0; Λ(12)₂ = 0·2 − [0 + 0 + 2·b₃ + 2·b₂] = 0; 2 ∤ 3, 9); so Λ(36)₂ = 6 − 10 = **−4**. p = 3: 3·2 = 6; Λ(9)₃b₄ =
(b₉·2)·1 = 6 and Λ(6)₃b₆ = 4, others 0; Λ(36)₃ = **−4**. So Λ_Q(6) = 2 log 2 + 2 log 3 = 2 log 6 and Λ_Q(36) = −4 log 2 − 4 log 3 = −4 log 6,
the record's values and `witness_ii`'s `(-4)*log(2) + (-4)*log(3)`. The script agrees and, over n ≤ 100, reproduces the record's negative set
{36, 54, 84} and support-off-prime-powers set {6, 14, 21, 36, 46, 54, 69, 84, 86, 94} exactly. It also checks the box: the count over
|x|, |y| ≤ n equals the count over all of ℤ² for every n ≤ 200 (the hand argument: x² ≤ n and 5y² ≤ n give |x|, |y| ≤ √n ≤ n for n ≥ 1,
and at n = 0 the box is {(0, 0)}, the only solution).

**(c) κ > 0 from the closed form.** Numerator: √(10 − 2√5) > 2 ⟺ 10 − 2√5 > 4 ⟺ √5 < 3 ⟺ 5 < 9 (the inner radicand 10 − 2√5 = 5.52786… is
positive, so `Real.sqrt` is the true root there). Denominator: √5 − 1 > 0 ⟺ 5 > 1. Hence κ > 0 (κ = 0.2840790438404122960282918323931261690911
at 40 digits, the record's number). This is exactly the chain of `kpos` (`Real.sqrt_lt'`, `Real.lt_sqrt`, `div_pos`). Signs: κ > 0 and
1 + κ² > 0 and log 2, log 3 > 0 give Λ_DH(3) < 0, Λ_DH(12) < 0, Λ_DH(4) = −(2 + κ²) log 2 < 0, Λ_DH(6) > 0.

**(d) `padicValNat` as e_p.** For n ≥ 1, n = Π_p p^{v_p(n)} with v_p(n) = `padicValNat p n` (the p-adic valuation; for p prime it is the
exponent of p in n, and it is 0 for p ∤ n), so log n = Σ_{p | n} v_p(n) log p, a finite sum, which is the sum over primes p ≤ n since a prime
divisor of n is ≤ n. The script's check: max |Σ_p v_p(n) log p − log n| over 1 ≤ n ≤ 10 000 is 1.8·10⁻¹⁵ (rounding). Consequence (the
content of FIDELITY (D1)): multiplying the coefficient recursion by log p and summing over primes turns
`b n · e_p(n) − Σ_{d<n} lambdaVec b d p · b(n/d)` into b_n log n − Σ_{d<n} Λ(d) b_{n/d}, i.e. `LambdaReal` satisfies the real recursion —
**provided b₁ = 1** (see F1); `padicValNat p n` for non-prime p is never consumed by `LambdaReal`.

## 6. Every statement read against BRIEF §0, the record and FIDELITY.md

**6.1 The trusted definitions (`ChallengeDeps/I1Witness.lean` lines 48–75).** `lambdaVecAux` is structural in the fuel (`| 0, _ => 0`; `|
fuel + 1, n => if n < 2 then 0 else b n * padicValNat p n − Σ_{d ∈ n.properDivisors} lambdaVecAux b p fuel d * b (n / d)`), `lambdaVec b n p
:= lambdaVecAux b p n n`; fuel n suffices (each call descends to a proper divisor d ≤ n − 1 with fuel n − 1). `LambdaReal` sums over
`(range (n+1)).filter Nat.Prime`, i.e. the primes p ≤ n. `epsteinB` is the halved card of the filter over `Icc (−n) n ×ˢ Icc (−n) n` in ℚ.
`kappa` is the record's closed form verbatim. `dhA` is 1, κ, −κ, −1, 0 at n % 5 = 1, 2, 3, 4, 0. Each is the brief's §0 object. Every
docstring restates a record sentence and says nothing more, with one exception, F1's "(with `b 1 = 1`)" — which is present in the trusted
file (lines 19, 54) and missing where the claim is repeated elsewhere.

**6.2 The statements (3 + 14, `Challenge/EpsteinWitnessSix.lean` 38–49, `Challenge/I1Witness.lean` 45–113).** Each witness theorem is
unconditional; (E1), (E2), (D1), (D2), (D3) are present exactly as BRIEF §0 wrote them, with the cast of E8 (`LambdaReal (fun n => (epsteinB n
: ℝ))`, forced: `LambdaReal` needs a real array) and the record's second form as an extra conjunct (FIDELITY (D8)). The recursion lemmas carry
`2 ≤ n` and `¬ p ∣ n`, the subjects of those lemmas, not conditions on a witness value. No hypothesis beyond the record. No statement
mentions a Dirichlet series, −F′/F, a zero, an Euler product, ζ or RH. `dh_twelve_coeff`'s `-kappa * (1 + kappa ^ 2) * 2` = −2κ(1 + κ²) (§5(a)).

**6.3 FIDELITY §1 (covered).** All 11 rows are theorems in the challenge files with the exact content shown (checked row by row against
the files; the 17 names are the configs' names). Row 1's left column "the recursion itself, on any array over any commutative ring" is F1.

**6.4 FIDELITY §2 (NOT covered), each sentence re-derived.**

| sentence | verdict |
|---|---|
| (F-a) "No theorem, definition or statement … mentions a Dirichlet series, a logarithmic derivative, `ζ_Q`, `F(s)`, or convergence; the phrase "−F′/F" occurs in header comments and docstrings only" | TRUE of statements and definition bodies; but `epsteinB`'s docstring (trusted file line 64) and header (line 28) carry "F(s) = ζ_Q(s)/2", so "definition … mentions `ζ_Q`, `F(s)`" is false if a docstring counts, and the first paragraph's "no Dirichlet series, no −F′/F, no convergence statement appears in any file" (line 16) is false of the comments (trusted file line 34: "no Dirichlet series, no −F′/F"). Wording only: F2 |
| (N2) DH function itself not stated | TRUE (no series, continuation, FE or zero in any statement) |
| (N3) nothing about Epstein zeta beyond the array; h = 2, D = −20 in comments only | TRUE (grep: "h = 2", "D = −20" occur in comments only) |
| (N4) no theorem says "DH has no Euler product", "Λ_DH is not supported on prime powers" as a universal, or "Λ(n) ≥ 0 fails" as a property | TRUE (every theorem is a value or a value's sign at one n; "witness" occurs in names and docstrings only) |
| (N5) no decimal value is a Lean statement | TRUE (the decimals −0.7629…, −0.3120927…, 0.28407904384… appear in comments; no statement contains a decimal) |
| (N6) Λ_Q(54), Λ_Q(84), the support list, Λ_DH(2^k), the Session-24 coefficient-support theorem, the genus identity, ζ_K not stated | TRUE; each referent exists in the record (m0-axiom-note §6.2 "negative values at {36, 54, 84}", the two structural checks; zoo I.1 Session-24 rider, "Λ_DH(2^k) = (−1)^{k−1}κ^k log 2 for odd k") |
| (N7) zoo 666's axiom-format statement not stated; only the witnesses half | TRUE |
| (N8) ζ, RH, any zero: nothing | TRUE |

**6.5 FIDELITY §3 (differs from the prose), at the Lean.**

| row | verdict |
|---|---|
| (D1) two objects; "the exponent-vector recursion is the record's recursion coefficient by coefficient because log n = Σ_p e_p(n) log p and the recursion is linear in Λ" | TRUE for arrays with b₁ = 1 (§5(d)); the b₁ = 1 condition is not stated here — F1 |
| (D2) fuel; "the record's recursion is recovered as the theorem `lambdaVec_rec` (for every n ≥ 2) … a reader who trusts the theorem need not trust the fuel" | the second clause TRUE (`lambdaVec_rec` and `lambdaVec_one` determine `lambdaVec b n p` for every n ≥ 1, which is all `LambdaReal` at n ≥ 1 consumes); the first clause needs "for b₁ = 1" — F1 |
| (D3) non-prime p never consumed; "`lambdaVec b 0 p = 0` by definition (n < 2), so b 0 is never consumed" | TRUE in content; the mechanism is the fuel-0 clause (`lambdaVec b 0 p = lambdaVecAux b p 0 0`, matched by `| 0, _ => 0`), not the n < 2 branch — F3. b 0 is never consumed: every `b (n / d)` in the recursion has n / d ≥ 2 and `b n` has n ≥ 2 (note: so b 1 is never consumed EITHER — the root of F1) |
| (D4) box |x|, |y| ≤ n contains every solution; `epsteinB 0 = 1/2` never consumed | TRUE (§5(b); the box check to n = 200) |
| (D5) ℚ array cast to ℝ, commutation proved (`ratCast'`) | TRUE (Solution/I1Witness.lean 87–101, induction on the fuel) |
| (D6) `dhA` by `n % 5`, `dhA 0 = 0` never consumed | TRUE |
| (D7) `Real.sqrt`; both radicands positive (5 and 10 − 2√5 = 5.527…); inner positivity used inside `kappa_pos` (4 < 10 − 2√5) | TRUE (§5(c); `Real.lt_sqrt` at `kpos` line 130 is exactly 2² < 10 − 2√5) |
| (D8) two forms of each value; `-kappa * (1 + kappa ^ 2) * 2` as the brief wrote it | TRUE |
| (D9) additions: the three (R) lemmas, `dhA_one`, `dh_four`, `dh_six`; every BRIEF §0 statement present | TRUE |
| (D10) `noncomputable section` forced by the compiler on the `Finset.Icc` ℤ instance path; kernel evaluation unaffected | TRUE — the checker's probe (`check-O/d10-probe.log`): the same definition outside the section fails with `error(lean.dependsOnNoncomputable): failed to compile definition … depends on 'Int.instCon…'`; the `decide +kernel` proofs pass (§2) |

**6.6 FIDELITY §4, BUILD-NOTES, README, yaml, comments — nothing claims more, except F1–F4.** The −F′/F identification is recorded as NOT
formalized in FIDELITY's first paragraph (lines 14–16), (F-a), the trusted file header (lines 34–37), both challenge headers, README §I1Witness
("the identification … is the classical identity, by hand") and yaml row (y) ("NOT covered … row (F-a)") — as BRIEF §0 requires. No file,
yaml entry, README sentence or comment says I.1 is formalized (`overclaim-greps.log`: 0 hits of "I.1 formalized" in the Lean; the phrase
occurs in FIDELITY, BUILD-NOTES and the yaml only inside "never" / "may not" sentences); "no Euler product" occurs in the Lean only inside "'DH has no Euler product' is the
zoo's reading, not a theorem here" (Challenge/I1Witness.lean line 31); in the Lean, ζ occurs only as `ζ_Q` in the record's normalization sentence and in "nothing about ζ or RH", and RH only there and in "Nothing here is an attack on RH". The label, character
for character (whitespace normalized across line breaks), against BRIEF §1(4) (`check-O/label-check.log`, 509 characters): exactly one
full occurrence each in BUILD-NOTES.md, FIDELITY.md, lean/README.md and lean/formalization.yaml; the yaml's second occurrence (main_results,
line 682) is an explicitly elided quotation ("— … the identification …"), not a variant. Yaml validator re-run
(`check-O/yaml-validation.log`): RESULT PASS, errors 0, undeclared names 0; row (y) occurs once; `yaml.safe_load` OK. 10(g) lint re-run
(`check-O/lint-10g.log`): 0 banned phrases in every builder file and topic file; no British spelling found.

**6.7 PREDERIVATION-ERRATA E1–E13.** Each "check, no error" entry agrees with §5 value for value (E2–E6, E10, E12); E7 and E13 (the ∀-prime
clause and the non-dividing primes are the lemma, not a decision) are TRUE at the solution (`e36_other`, `sum_two_three`); E8, E9 TRUE
(`padicValNat` reduced in the checker's probes too: `lambdaVec epsteinB 36 5 = 0` decided); E11's times reproduced (§2). E13's "(or
`Finset.sum_eq_single`)" names a lemma no solution uses — F3.

## 7. Hashes (`check-O/hash-recompute.log`)

Every line of `hashes.txt` (33 files) recomputed with `shasum -a 256` from `rh-program/`: **32 MATCH, 1 explained mismatch** —
`results/i1-witness-lean-s32/SHARED.md` (recorded `cdfec262…`, now different) because the builder appended its closing block (07:53:06)
after writing `hashes.txt` (07:52:36); the recorded value equals the SHA-256 of SHARED.md truncated before that block (`cdfec2627e98da79…`,
reproduced exactly), and this check's own SHARED block changes it again. The hashes quoted elsewhere also match: BRIEF.md `54ad13fb…aa3b69`,
BUILD-NOTES.md `ad100bc5…3722c`, FIDELITY.md `203d2de9…79c90`, hashes.txt `0d145c4c…eb4d3`, PREDERIVATION-ERRATA.md `6aea75b5…8c22c` (as in
SHARED.md's final builder block). The four comparator-tool hashes match COMPARATOR-RUN.md (§4). The SHA-256 of every file this check
wrote is in §10.

## 8. Verdict — FIX-FIRST (prose only; the Lean, the statements, the label and every run are CLEAN)

What is CLEAN: both builds from a clean v1.0 clone, first try, 0 errors, 0 warnings; 17/17 print-axioms lines on the three standard axioms, no
`sorryAx`, no `Lean.ofReduceBool`; 17/17 statements identical; trust greps: the 17 deliberate challenge `sorry`s only; both comparator runs
exit 0 with "Nanoda kernel accepts the solution" and "Lean default kernel accepts the solution"; the n = 36 kernel time 3.43–3.45 s per
coefficient; every shipped value re-derived by hand and by an independent script (§5); every FIDELITY §2 sentence and every §3 row true
in content (§6); no hypothesis beyond the record; the label verbatim; the −F′/F identification recorded as NOT formalized everywhere.

The items (none changes a statement, a proof or a value):

**F1 — "the record's recursion" is claimed for every array; it is the record's recursion only when b₁ = 1.** The record's recursion is
a_n log n = Σ_{d|n} Λ(d) a_{n/d}, whose d = n term is Λ(n)·a₁. `lambdaVec` (and `lambdaVec_rec`) is the SOLVED form Λ(n) = b_n e_p(n) −
Σ_{d|n, d<n} Λ(d) b_{n/d}, which drops the factor b₁ (b 1 is never read by the definition — see (D3)); for an array with b 1 ≠ 1 the
defined object does not satisfy the record's recursion (it satisfies the recursion with a₁ replaced by 1), and for b 1 = 0 the record's
recursion has no solution at all. The trusted file says "(with `b 1 = 1`)" (ChallengeDeps/I1Witness.lean lines 19, 54), but the claim is
repeated without the condition at: `Challenge/I1Witness.lean` lines 20–22 ("(R) The trusted object satisfies the record's recursion: for
every commutative ring R, array b and prime index p" — also "prime index p": the theorem quantifies over every p : ℕ) and line 44 (docstring
"the record's recursion holds for the trusted object"; the same at `Solution/I1Witness.lean` line 206 and line 16); `FIDELITY.md` line 28
(covered-table row 1, "the recursion itself, on any array over any commutative ring"), line 77 ((D1), "is the record's recursion coefficient
by coefficient"), line 80 ((D2), "The record's recursion is recovered as the theorem `lambdaVec_rec`"); `BUILD-NOTES.md` lines 67 and 75;
`lean/formalization.yaml` lines 675–676, 1027 ((y2)) and 1382 (alignment row source, "the recursion itself … for every commutative ring");
`lean/README.md` line 489 ("for every commutative ring"). The witness values are untouched: both arrays have b₁ = 1, shipped and
kernel-checked as `epsteinB_one` and `dhA_one`. Fix: at each place say "the record's recursion solved for Λ(n) under the normalization b₁ = 1
(for every commutative ring and every array, the solved form; it IS the record's recursion when b 1 = 1, which `epsteinB_one` and `dhA_one`
supply)"; change "prime index p" to "every index p"; add a FIDELITY §3 row (D11) and a yaml (y7): "`lambdaVec` hard-codes b₁ = 1: the d = n
term Λ(n)·b₁ of the record's recursion is taken as Λ(n), and b 1 is never read; the record normalizes b₁ = 1 for both arrays, so no witness is
affected." Editing the challenge header changes a trusted file's comment only: re-run statement identity and the `config-i1-witness.json`
comparator run afterwards (48 s).

**F2 — FIDELITY's "no … appears in any file" is false of the comments.** `FIDELITY.md` line 16: "no Dirichlet series, no −F′/F, no
convergence statement appears in any file" — the trusted file's comment line 34 reads "no Dirichlet series, no −F′/F", and "−F′/F" occurs in
four comment lines of the three trusted files (`overclaim-greps.log`). Line 50–51 ((F-a)): "No theorem, definition or statement … mentions … `ζ_Q`, `F(s)`" — `epsteinB`'s
docstring (ChallengeDeps/I1Witness.lean line 64) and the header (line 28) carry "F(s) = ζ_Q(s)/2". Fix: "no Dirichlet series, no −F′/F and no
convergence statement appears in any statement or definition body; the words occur only in comments and docstrings, restating the record".

**F3 — two mechanism descriptions are inaccurate (contents true).** `FIDELITY.md` lines 83–84 ((D3)): "`lambdaVec b 0 p
= 0` by definition (n < 2)" — `lambdaVec b 0 p` unfolds to `lambdaVecAux b p 0 0`, which is the fuel-0 clause `| 0, _ => 0`; the n < 2 branch
is never reached at n = 0 (the orchestrator's note §1 item 4 repeats "by the n < 2 branch"). `Solution/I1Witness.lean` line 23 and
`PREDERIVATION-ERRATA.md` line 97 (E13): "`Finset.sum_eq_add_of_mem` / `Finset.sum_eq_single`" and "(or `Finset.sum_eq_single`)" — no solution
uses `Finset.sum_eq_single` (grep: the name occurs only in these two comments); every sum is reduced with `Finset.sum_eq_add_of_mem`
(`sum_two_three`, `epstein_witness_6`). Fix: "by the fuel-0 clause"; delete the `sum_eq_single` mentions.

**F4 — the rung-1 build has no log on disk, and the README cites one log for two builds.** `lean/README.md` lines 504–505: "both solutions
*Build completed successfully (8698 jobs)*, 0 errors, 0 warnings, first try (`build-i1witness.log`)" — `build-i1witness.log` records only
`lake build Solution.I1Witness`; the rung-1 figures of `BUILD-NOTES.md` line 82 (`Built ChallengeDeps.I1Witness (2.8s)`, `Built
Solution.EpsteinWitnessSix (4.0s)`, 9.43 s real) exist only in prose (BUILD-NOTES, SHARED 07:42:51). Both builds are now on disk from the
clean clone (`check-O/clone-build.log`: 6.9 s / 3.3 s, 12.97 s real). Fix: cite `check-O/clone-build.log` for both builds (or state that the
rung-1 build was not logged).

Observation, not an item: `hashes.txt`'s SHARED.md line is stale by construction (§7); the orchestrator's LOG entry should hash SHARED.md
after this check's block.

## 9. What the orchestrator should do

1. Adjudicate F1 by re-derivation: read `ChallengeDeps/I1Witness.lean` lines 48–51 and confirm that `b 1` is never read (the recursion reads
   `b n` at n ≥ 2 and `b (n / d)` at n / d ≥ 2), then that a_n log n = Σ_{d|n} Λ(d) a_{n/d} reduces to `lambdaVec_rec`'s form exactly when
   a₁ = 1. Apply the F1 wording at each place listed in F1, add (D11) / (y7); then re-run `tools/statement_identity_i1.py` and the
   `config-i1-witness.json` comparator run (the challenge file's comment changed), and re-hash.
2. Apply F2, F3, F4 (ledger, yaml, README, errata and a solution comment; no statement changes; if `Solution/I1Witness.lean` line 23 is
   edited, re-run the same comparator config).
3. Then the label of BRIEF §1(4) stands as shipped, and the refutation-shaped close is the "Lands" branch; STATUS rank 4 may be closed.
   Nothing about ζ or RH follows.
4. Re-hash every edited file, and SHARED.md after this block.

## 10. Every log and script of this check (under `results/i1-witness-lean-s32/check-O/`), with SHA-256

All written by the checker in this job. Clone: `~/rh-lean-work/checker-clone-s32-i1` (v1.0 + overlay; kept for re-runs). CHECK-O.md's own
SHA-256 is in `SHARED.md`'s checker block.

| file | SHA-256 |
|---|---|
| `check-O/cleanup.sh` | `0ee89c1efa85c835bb12d72174787efdcf77280235e9c9ac50e3c95c032f7169` |
| `check-O/clone-build.log` | `3ee3e5a94b1a03c98bcf1b49a9b7d1d66953d3121c0abc875ba9836e56c8dcbd` |
| `check-O/clone-build.sh` | `0823765f41ef1058466a08dbc1fba635708b2189e2743566b88bc4df40cc6d5e` |
| `check-O/comparator-epstein-six.log` | `fe87bbcb1c9587090429d77f751ffc876083b49d4b01f2a8bd2f51469b5639a0` |
| `check-O/comparator-i1witness.log` | `b698dac94b91ba866da321424680f6129e9edfda3d1a0d98b66ba85ada31842a` |
| `check-O/d10-probe.lean` | `30da8282c990cabcede9e2a97a0356a767763dc1ca45dfb0e59173d467940a36` |
| `check-O/d10-probe.log` | `6cbe98f0f0acc583b4a72234662caa07b2baa526fa055861310c0932d662d08b` |
| `check-O/hash-recompute.log` | `bb1a1578ca7b2ef1f08900b03243d7a93649057c7b3e632e635c2eed2d0671ef` |
| `check-O/identity-trust.log` | `2e32381848d6e9fb297442a29ab802219d1702a458260dea9b66076386007132` |
| `check-O/kernel-probe-single.lean` | `4dbb6fe766307359dd9ec17613b8face8832186f8be310955337f66aac812c74` |
| `check-O/kernel-probe-single.log` | `6d30c797b2daad530d14cd14491ee2bdadcf9c112c1dae795f07eb313050ec02` |
| `check-O/kernel-probe.lean` | `facab1f4b6e836a1ee47552007615577ca9d84a5bd96c3aff36d3f61861a9443` |
| `check-O/kernel-probe.log` | `24acad5d608ea92ad3c5020c430afacfb3955a4113465dab73e9a13663ff2e0a` |
| `check-O/label_check.py` | `a293f6d90898189940af3ccd1470bb8c228a1c406a082aaad7853c38a2c2acfc` |
| `check-O/label-check.log` | `b10e1cc31359bdaf5493e71b3ce58405edb5abde1660c0a39e07795b37963a15` |
| `check-O/lint-10g.log` | `4b6a5a43d324026311b8934700d03ed3ff33592b5dfe2f5b3e59ca0e8cf9f8dd` |
| `check-O/overclaim-greps.log` | `17c74f92300367ed0fd4e441dadcfdc9a9bdb150b190b9aa324700d5ba523e2c` |
| `check-O/prerun-cleanup-epstein-six.log` | `abe674b1bc99f9b40d14ce9c3369c590917054777564dc2835bb9848ab787e78` |
| `check-O/prerun-cleanup-i1witness.log` | `4823f4716c8a8d67a7e719ab58cb7e1d7416efbfba5fe71f419810281927f217` |
| `check-O/print-axioms.log` | `3e877a53a32e73aaa5686dfa672494b98358e83f8d5940aa9247acc3e4b94b90` |
| `check-O/rederive.log` | `6fee10e180ade0312f3dd5ddce29beab4dc52b199b84a443d1c0ee626afea6e8` |
| `check-O/rederive.py` | `d9640d7833fbb664f11810394f1a3b1c2ae777261129b7249cc077fd9407bb30` |
| `check-O/run-clone.sh` | `935ee0177b7e9d35075af022295fe03b7bd0c07b6403a38195b11ff6caca025e` |
| `check-O/yaml-validation.log` | `4dbabf6adbcc87f2628d9792e83f4c78d244e2fb7c837950a4e4c6923773b0da` |

Closing machine-clock stamp of this file: Tue Sep 29 08:07:27 IST 2026.
