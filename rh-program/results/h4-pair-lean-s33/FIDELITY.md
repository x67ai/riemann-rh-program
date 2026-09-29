# H4 — FIDELITY ledger for the Comparator topic `PairChannel` (barrier-zoo IV.17's pair channel: Prop. 4.5, the integer-mark safety chain, the floor's failure at the anchor); builder Fable 5.1, Session 33, 2026-09-29

Mirrored in `lean/formalization.yaml` (`fidelity.divergences`, row (z)). Brief: `results/h4-pair-typing-s32/UNIT-BRIEF.md` §2 item 5. The
record the statements are read against: `results/a4-no-go/paper.md` §2.3 (the finite-circle row: "c_s = Σ_z m_z e^{−2πisθ_z/N} (a conjugate
pair at θ ± id contributes 2m cosh(2πsd/N) e^{−2πisθ/N})", "tr Ĝ² = Σ_s W2(s)|c_s|², W2(s) = Σ_{j∈B, s−j∈B} u_j u_{s−j}", "uniform weights
u_j = 1/M") and §4.2 (Prop. 4.5: "Let c_μ be the vacancy lattice (unit atoms on grid sites g_1..g_64) plus one pair at the hole g_0 with
depth d > 0 and REAL mark μ > 0. Then, exactly, F1(c_μ) − S2(c_μ) = 2μ²ā(2d)² − 4μ(ā(d)² − 1)"; "For integer marks the same family is
safe: at μ = m ∈ ℤ, the log-convexity bound ā(d)² − 1 ≤ (ā(2d) − 1)/2 gives F1 − S2 ≥ 2m²ā(2d)² − 2m(ā(2d) − 1) > 0"; "the numeric check at
(d, μ) = (0.25, 0.05) reproduces it to 1e-12, with F1 − S2 = −3.520e-2"); `results/a4-no-go/pair-channel.md` §1 (u_j = 1/65, w_s =
(65 − |s|)/65²), §2 ((T1), (T3)), §3 (Prop. 3.1 = Prop. 4.5); the typing note `results/h4-pair-typing-s32/TYPING-NOTE.md` §1–§4.

**First paragraph, binding (10(c)).** Nothing about ζ or RH follows from anything below. The theorems are statements about one quadratic
form (the bandwidth-one Frobenius row with the flat weights) on finite configurations — rational marks on a cyclic grid plus real-marked
pairs at grid sites — and about the flat average ā of cosh; no zero, no explicit formula, no law, no property of ζ appears in any
statement. The label the unit earns (UNIT-BRIEF §1(3)), verbatim: "IV.17's pair channel: Prop. 4.5 Comparator-checked for every depth and
real mark, the integer-mark safety chain a theorem, and **the floor F1 ≥ S2's failure** for a real-marked pair at (1/4, 1/20)
kernel-checked by a dyadic certificate — over Mathlib alone, no displayed hypothesis, the three standard axioms, replayed by nanoda". At
the anchor (MI) holds — see §2, first bullet — and `floor_fails_anchor` is the failure of the floor F1 ≥ S2 for a real mark, nothing more.

## 1. What IS covered — each claim is a theorem in `lean/comparator/Challenge/PairChannel.lean` (proved in `Solution/PairChannel.lean` by delegation to `Zeta23/PairCeiling/PairRow.lean` and `PairCert.lean`)

| record's claim | theorem | exact content |
|---|---|---|
| pair-channel.md §1: "assembly weights w_s = (65 − \|s\|)/65² for \|s\| ≤ 64 (the autocorrelation w = u ∗ u)" — for every n | `W2_eq` | ∀ n s, s ∈ Icc (−2n) (2n) → `W2 n s = ((2n + 1) − \|s\|)/(2n + 1)²`, where `W2 n s := Σ_{j ∈ B, s − j ∈ B} (1/(2n+1))²` is paper §2.3's W2 at u_j = 1/M |
| the single-convolution row IS the double band sum (paper §2.3's two forms of tr Ĝ²) | `sum_W2_mul` | ∀ n g, `Σ_{s ∈ [−2n, 2n]} W2 n s · g s = Σ_{j₁, j₂ ∈ B} (1/M)(1/M) · g (j₁ + j₂)` |
| the new row agrees with the shipped grid row when there is no pair (the queue's requirement) | `pairRow_eq_gridRowQ` | ∀ n m, `pairRow n m ∅ = gridRowQ n m` (`gridRowQ` the IntegralityGap row, character for character) |
| pair-channel.md (T1) "Σ_s w_s q^s = (Σ_j u_j q^j)²" at q = e^{β}, i.e. "Σ_s w_s cosh(βs) = ā(d)²" | `sum_W2_cosh` | ∀ n x, `Σ_s W2 n s · cosh(2πsx/(2n)) = abar n x ^ 2`, `abar n x := Σ_{j ∈ B} (1/M) cosh(2πjx/(2n))` |
| **Prop. 4.5** "F1(c_μ) − S2(c_μ) = 2μ²ā(2d)² − 4μ(ā(d)² − 1)", every depth, every real mark — and every n | `prop45` | ∀ n (d μ : ℝ), `pairRow n (vacancyMark n) {(0, μ, d)} − (2n + 2μ²) = 2μ² · abar n (2d)² − 4μ · (abar n d² − 1)`; `vacancyMark n k = if k = 0 then 0 else 1`; S2 = Σ_a m_a² + 2Σ_p m_p² = 2n + 2μ² written out |
| pair-channel.md (T3) "ā(y)² ≤ (1 + ā(2y))/2 (Cauchy–Schwarz on the positive weights)" | `abar_sq_le` | ∀ n d, `abar n d ^ 2 ≤ (1 + abar n (2d))/2` |
| "For integer marks the same family is safe … > 0" (paper §4.2; pair-channel.md Prop. 3.1 second display) | `floor_holds_integer` | ∀ n d (m : ℕ), 1 ≤ m → `0 < 2m² · abar n (2d)² − 4m · (abar n d² − 1)` — the right side of `prop45` at μ = m |
| "the numeric check at (d, μ) = (0.25, 0.05) … F1 − S2 = −3.520e-2" — the SIGN, kernel-checked | `floor_fails_anchor` | `pairRow 32 (vacancyMark 32) {((0 : ZMod 65), 1/20, 1/4)} < 64 + 2 · (1/20)²` |

All eight: no displayed hypothesis beyond the statements' own binders (`n : ℕ`, `d μ x : ℝ`, `g : ℤ → ℝ`, `m : ZMod (2n+1) → ℚ`, `1 ≤ m`,
the band membership `s ∈ Icc (−2n) (2n)` of `W2_eq`) — exactly the list of UNIT-BRIEF §1(1); axioms `[propext, Classical.choice,
Quot.sound]` for each (`print-axioms.log`), and for the 34 program-side names (`program-axioms.log`); statement identity
challenge/solution 8/8 and challenge/probe 8/8 (`statement-identity.log`); the Comparator run with nanoda PASS, exit 0
(`comparator-run.log`).

## 2. What is NOT covered — stated nowhere in Lean

* **(MI) at any anchor.** The master inequality F1 ≥ T = 3M − 2N_d (paper §4.2; pair-channel.md §0) appears in no statement of this
  topic. At the certificate's anchor (MI) HOLDS: M = 64 + 2μ = 64.1, N_d = 66, T = 60.3, F1 = 63.9698, F1 − T = +3.67 > 0, and
  S2 − T = 2(μ − 1)(μ − 2) = 3.705 — these are hand/Python facts (`tools/h4_numbers.log`), NOT Lean statements. `floor_fails_anchor`
  is the failure of the floor F1 ≥ S2 for the real mark μ = 1/20 and says nothing about (MI). The forbidden phrasings of UNIT-BRIEF
  §1(3) appear in no file of this unit (the phrase "(MI) fails" occurs nowhere; the words "formalized" and "closed" are not applied to
  IV.17 or to the pair channel; `lint-10g.log` records the grep).
* **Theorems 4.6–4.9 of the paper / Theorems A–D of pair-channel.md** (the single-pair and multi-pair closures, the capacity machinery,
  the 8/9 backstop, the crowding cap): the pair channel's closure stays at paper grade. Nothing about them is stated.
* **Laws and the LP.** No probability mixture of columns, no expectation, no LP column, no ε-budget appears; every statement is
  pointwise on one configuration or an identity for every configuration of the stated shape.
* **General positions.** Pairs sit on GRID SITES (`p.1 : ZMod (2n+1)`); the paper's row allows any real θ_p. The general-position row
  is not defined (a restriction of the paper's row, §3 (z1)); Prop. 4.5 needs only the hole g₀ = 0. Likewise the paper's W2 for
  general harmonics u_j is not defined — the flat value u_j = 1/(2n+1) is substituted in the definition of `W2` (§3 (z2)).
* **Prop. 4.1's ledger, (T2), (T4), (T5)** of pair-channel.md: not stated; Prop. 4.5's proof does not use them (the paper's proof does
  not either).
* **The value F1 − S2 = −0.0352.** The Lean statement `floor_fails_anchor` is the strict inequality only. The certificate's bound
  −0.03368 (from L = L(3.141592) = 1.10602…, U = U(3.141593) = 1.48152…) and the record's −0.0352 appear in the proof text
  (`PairCert.cert_numeric` states the rational inequality 2μ²U² − 4μ(L² − 1) < 0) and in comments; no theorem states a value of
  F1 − S2 or of ā.
* **ζ, RH, any zero, any explicit formula.**

## 3. Where the formal statements differ from the prose (the yaml row (z), item by item)

* **(z1) Pairs on grid sites.** `pairFormFactor` takes `pairs : Finset (ZMod (2n+1) × ℝ × ℝ)` — site, real mark, real depth — and the
  pair's phase is the character `chi (zetaM M) ((s : ZMod M) * θ)`; the paper's row has a pair at any real θ_p with phase
  e^{−2πisθ_p/N}. On grid sites the two agree (up to the sign convention (z5)); off the grid nothing is defined. Prop. 4.5's pair is at
  the hole g₀ = 0, a grid site.
* **(z2) The flat weights substituted.** Paper §2.3 defines W2(s) = Σ_{j∈B, s−j∈B} u_j u_{s−j} for general u and substitutes u_j = 1/M
  afterwards; `W2 n s` is that filtered double sum with (1/(2n+1))·(1/(2n+1)) written in — the shape of `gridRowQ`'s weights, so that the
  agreement lemma meets `gridRowQ` syntactically. The closed form (M − |s|)/M² of pair-channel.md is the theorem `W2_eq`, not a definition.
* **(z3) Every n, including n = 0.** The statements are for every `n : ℕ` with M = 2n + 1 sites and N = 2n written `2 * (n : ℝ)` in the
  cosh arguments; the record's geometry is n = 32 (N = 64, M = 65). At n = 0 the cosh arguments are x/0 = 0 by Lean's convention and every
  statement stays true (ā = 1, W2 0 0 = 1); nothing in the unit depends on that case. "Every n" is stronger than the brief's "every
  depth and real mark", which is the label's clause (stop line (ii) did not fire; general n needed no hypothesis).
* **(z4) Mark types.** Atom marks are `ℚ` (the shipped vocabulary `dftMarkQ`/`gridRowQ`; the vacancy lattice's marks 0 and 1); pair
  marks are `ℝ` (Prop. 4.5's "REAL mark μ"); the integer chain takes `m : ℕ` with `1 ≤ m` and casts it to ℝ (the paper's "μ = m ∈ ℤ",
  m ≥ 1 — the same set of marks). The pair mark μ of `prop45` is any real, including 0 and negatives (the paper says μ > 0; the identity
  holds for every μ and the statement says so).
* **(z5) The sign of the character.** `chi (zetaM M) x = e^{+2πi x.val/M}` where the paper's phase is e^{−2πisθ/N}; under `normSq` the
  two rows coincide (conjugating every term of c_s; the cosh factor is real and even in s) — as GridParseval.lean records for the atom
  rows. No value changes.
* **(z6) The row's range and shape.** `pairRow` sums over the literal integer range s ∈ Icc (−2n) (2n) with `W2 n s` as the weight and
  `Complex.normSq` for |c_s|²; the paper's Σ_s runs over all s with W2 = 0 outside [−2n, 2n]. Same number.
* **(z7) The chain's intermediate step is inside the proof.** The paper's display "F1 − S2 ≥ 2m²ā(2d)² − 2m(ā(2d) − 1) > 0" is the
  proof of `floor_holds_integer` (the two `have`s `h1`, `h2` in PairRow.lean), not a named statement; the named statements are the
  log-convexity step `abar_sq_le` and the positivity `floor_holds_integer`. The statement is about the right side of `prop45`; combined
  with `prop45` (a `rw` away) it is F1 − S2 > 0 for the integer-marked family — not stated as a separate theorem.
* **(z8) The certificate is a strict inequality, not a value.** `floor_fails_anchor` states `pairRow … < 64 + 2·(1/20)²`; the record's
  F1 − S2 = −3.520·10⁻² is not a Lean statement (§2). The Lean proof's route: `prop45` at (32, 1/4, 1/20), the two generic cosh bounds
  passed through the flat average symbolically (four integer power sums by `decide +kernel`), Mathlib's `pi_gt_d6`/`pi_lt_d6`, one
  `norm_num` on a rational inequality whose numerator has 133 digits — the "dyadic certificate" of the label is this kernel-checked
  rational certificate (the π bracket is the decimal d6 one, not a power-of-two one; PREDERIVATION-ERRATA E7).
* **(z9) `W2`'s summation binder is written `_j`.** The probe (`typing-probe.lean` line 18) writes `∑ j ∈ …` with `j` unused in the
  constant summand, which the linter flags; the shipped definition writes `∑ _j ∈ …` so the modules build with 0 warnings. The
  elaborated term is the same (the binder name is not part of it); the trusted layer and PairRow.lean agree character for character
  (`trust-greps.log`, 5/5); the one-character difference from the probe is recorded there too. The eight STATEMENTS are the probe's
  byte for byte (`statement-identity.log`).
* **(z10) Axioms of the kernel facts.** The four `decide +kernel` power sums print all three standard axioms (`Classical.choice`
  enters through Mathlib's `Finset`/`Int` instances), as IV.17's (v8) recorded; within the permitted set and within the label.
* **(z11) Names.** The eight names are the brief's / the probe's (`W2_eq`, `sum_W2_mul`, `pairRow_eq_gridRowQ`, `sum_W2_cosh`, `prop45`,
  `abar_sq_le`, `floor_holds_integer`, `floor_fails_anchor`); the program-side helpers (`card_band`, `sum_sinh_band`,
  `intCast_zmod_eq_zero_iff`, `dftMarkQ_vacancy`, `W2_zero`, `abar_zero`, `sum_vacancyMark_sq`, `sum_W2_vacancy_sq`,
  `sum_W2_vacancy_cosh`, `sum_W2_cosh_sq`, `one_le_abar`; `one_add_sq_half_le_cosh`, `exp_sub_sum_le`, `cosh_le_poly8`, `sum_pow2/4/6/8`
  and their `_real` casts, `card_band32`, `sum_poly2`, `sum_poly8`, `abar32`, `abar_quarter_ge`, `abar_half_le`, `abar_quarter_ge_L`,
  `abar_half_le_U`, `cert_numeric`) are not challenge statements; the two generic cosh bounds the brief names are among them, in
  `PairCert.lean`, with the brief's statements verbatim.
* **(z12) The trusted layer restates three definitions it does not use.** `PairChannel.dftMark`, `gridRow`, `fracMark` are restated
  from IntegralityGap (the brief: "the seven IntegralityGap definitions restated character for character") although no statement of
  this topic mentions them; the statements mention `chi`, `dftMarkQ`, `zetaM`, `gridRowQ` and the five new definitions. Definitions add
  no trust; they are there so that the two IV.17 topics share one vocabulary.

## 4. Character-for-character claims for the checker to `diff`

`PairChannel.chi`, `dftMark`, `dftMarkQ`, `zetaM`, `gridRow`, `gridRowQ`, `fracMark` against `comparator/ChallengeDeps/IntegralityGap.lean`
(7/7 identical `def` blocks, `trust-greps.log`; those in turn against the Zeta23 originals as IV.17's CHECK-O did — `dftMarkQ`'s binder
placement differs textually from `GridParsevalRat.lean`'s `variable` form, the same constant type, IV.17 CHECK-O O1);
`PairChannel.W2`, `pairFormFactor`, `pairRow`, `abar`, `vacancyMark` against `Zeta23/PairCeiling/PairRow.lean` (5/5 identical). The
delegations in `Solution/PairChannel.lean` typecheck only because these are definitionally equal after unfolding — the Solution's clean
build (0 errors, 0 warnings, `build-comparator-topic.log`) is itself the check, and the Comparator's statement comparison confirms the
challenge side.
