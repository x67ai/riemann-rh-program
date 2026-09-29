# I.1 witness table — FIDELITY ledger for the Comparator topics `EpsteinWitnessSix` and `I1Witness` (barrier-zoo I.1's one-line witnesses as kernel-checked values); builder Fable 5.1, Session 32, 2026-09-29

Mirrored in `lean/formalization.yaml` (`fidelity.divergences`, row (y)). Brief: `results/i1-witness-lean-s32/BRIEF.md` §0–§2. The record
the statements are read against: `results/c3-r/m0-axiom-note.md` §6.1 (DH: "a_n periodic mod 5, (a₁,…,a₅) = (1, κ, −κ, −1, 0)", κ =
(√(10−2√5) − 2)/(√5 − 1), the table Λ_DH(3) = −κ·log 3, Λ_DH(4) = −(2+κ²)·log 2, Λ_DH(6) = +(1+κ²)·log 6, Λ_DH(12) = −κ·(1+κ²)·log 12, and
"Closed forms below follow from the von Mangoldt recursion a_n log n = Σ_{d|n} Λ_DH(d) a_{n/d} on the periodic coefficient array") and
§6.2 (Epstein, Q = x² + 5y²: "F(s) = ζ_Q(s)/2, b_n = r_Q(n)/2, b₁ = 1; Λ_Q from −F′/F", "Λ_Q(6) = 2·log 2 + 2·log 3 = 2·log 6", "Λ_Q(36) =
−4·log 2 − 4·log 3 = −4·log 6"); `results/c3-m0-epstein/n1_epstein_witness.json` (`witness_i`, `witness_ii`); zoo I.1 STATEMENT and
EXECUTABLE TEST (c); zoo line 666.

**First paragraph, binding (10(c) and BRIEF §0 row (F-a)).** Nothing about ζ or RH follows from anything below. The theorems are VALUES
of a recursion: `lambdaVec b n p` is defined (ChallengeDeps/I1Witness.lean) by the von Mangoldt recursion `Λ(n) = b_n·e_p(n) −
Σ_{d | n, d < n} Λ(d)·b_{n/d}` on a coefficient array b with b₁ = 1, with log n replaced by the exponent vector (e_p(n) = padicValNat p n),
and `LambdaReal b n = Σ_{p ≤ n prime} lambdaVec b n p · Real.log p`. The identification "`LambdaReal b` is the coefficient sequence of
−F′/F for F(s) = Σ b_n n^{−s}" is the classical identity (Σ Λ(n) n^{−s})(Σ b_n n^{−s}) = Σ b_n log n · n^{−s} and is NOT formalized; no
Dirichlet series, no −F′/F, no convergence statement appears in any STATEMENT [CORRECTION 08:10 IST 2026-09-29, Session 32 — CHECK-O F2: the phrases do occur in header comments and docstrings, e.g. ChallengeDeps/I1Witness.lean lines 28, 34, 64; the sentence reads "in any statement"]. What is formalized is the recursion (as a theorem about the
defined object, `lambdaVec_rec`) and its values at the record's witnesses. The label the unit earns (BRIEF §1(4)), verbatim: "I.1's
witness table kernel-checked — for the Epstein form x² + 5y² (h = 2), Λ_Q(36) = −4 log 2 − 4 log 3 < 0 (and Λ_Q(6) = 2 log 6 off prime
powers); for Davenport–Heilbronn, Λ_DH(3) = −κ log 3 < 0 and Λ_DH(12) = −κ(1 + κ²) log 12 < 0 with κ > 0 from its closed form — where Λ_f
is the von Mangoldt recursion's coefficient sequence on the array with b₁ = 1; over Mathlib alone, the three standard axioms, replayed by
nanoda; the identification of that sequence with −F′/F as Dirichlet series is not formalized". It is a hardening of I.1's witnesses from
"computationally-verified" to kernel-checked — a barrier record, not an attack under the sponsor's criterion.

## 1. What IS covered — each claim is a theorem in the challenge files (proved in the solution files)

| record's claim | theorem (file) | exact content |
|---|---|---|
| the recursion itself, on any array over any commutative ring | `lambdaVec_rec` (`Challenge/I1Witness.lean`) | ∀ {R} [CommRing R] (b : ℕ → R) (p n : ℕ), 2 ≤ n → lambdaVec b n p = b n * (padicValNat p n : R) − ∑ d ∈ n.properDivisors, lambdaVec b d p * b (n / d) |
| Λ(1) = 0 | `lambdaVec_one` | lambdaVec b 1 p = 0 |
| a prime not dividing n contributes no log p at n | `lambdaVec_eq_zero_of_not_dvd` | ¬ p ∣ n → lambdaVec b n p = 0 |
| §6.2 "b₁ = 1" | `epsteinB_one` (both topics) | epsteinB 1 = 1 |
| §6.2 "Λ_Q(6) = 2·log 2 + 2·log 3 = 2·log 6" (`witness_i`) | `epstein_six_coeff`, `epstein_witness_6` (`Challenge/EpsteinWitnessSix.lean`) | lambdaVec epsteinB 6 2 = 2 ∧ lambdaVec epsteinB 6 3 = 2; LambdaReal (fun n => (epsteinB n : ℝ)) 6 = 2 * Real.log 2 + 2 * Real.log 3 ∧ … = 2 * Real.log 6 ∧ 0 < … |
| §6.2 "Λ_Q(36) = −4·log 2 − 4·log 3 = −4·log 6" (`witness_ii`); zoo 666 "Λ_Q(36) = −4log6" | `epstein_thirtysix_coeff`, `epstein_witness_36` | lambdaVec epsteinB 36 2 = -4 ∧ lambdaVec epsteinB 36 3 = -4 ∧ ∀ p, p.Prime → p ≠ 2 → p ≠ 3 → lambdaVec epsteinB 36 p = 0; LambdaReal (…) 36 = -4 * Real.log 2 - 4 * Real.log 3 ∧ … = -4 * Real.log 6 ∧ … < 0 |
| §6.1 κ = (√(10−2√5) − 2)/(√5 − 1) > 0 (the reader's A19: "the DH signs need only κ > 0 from its closed form") | `kappa_pos` | 0 < kappa |
| §6.1 a₁ = 1 | `dhA_one` | dhA 1 = 1 |
| §6.1 "Λ_DH(3) = −κ·log 3 … cheapest witness" | `dh_three_coeff`, `dh_witness_3` | lambdaVec dhA 3 3 = -kappa; LambdaReal dhA 3 = -kappa * Real.log 3 ∧ LambdaReal dhA 3 < 0 |
| §6.1 "Λ_DH(12) = −κ·(1+κ²)·log 12"; zoo I.1 "Λ_DH(12) = −0.7629 < 0 — the one-line witness" | `dh_twelve_coeff`, `dh_witness_12` | lambdaVec dhA 12 2 = -kappa * (1 + kappa ^ 2) * 2 ∧ lambdaVec dhA 12 3 = -kappa * (1 + kappa ^ 2); LambdaReal dhA 12 = -kappa * (1 + kappa ^ 2) * (2 * Real.log 2 + Real.log 3) ∧ … = -kappa * (1 + kappa ^ 2) * Real.log 12 ∧ … < 0 |
| §6.1 "Λ_DH(4) = −(2+κ²)·log 2 … negativity at a prime power" | `dh_four` | lambdaVec dhA 4 2 = -(2 + kappa ^ 2) ∧ LambdaReal dhA 4 = -(2 + kappa ^ 2) * Real.log 2 ∧ LambdaReal dhA 4 < 0 |
| §6.1 "Λ_DH(6) = +(1+κ²)·log 6 … support off prime powers" | `dh_six` | lambdaVec dhA 6 2 = 1 + kappa ^ 2 ∧ lambdaVec dhA 6 3 = 1 + kappa ^ 2 ∧ LambdaReal dhA 6 = (1 + kappa ^ 2) * Real.log 6 ∧ 0 < LambdaReal dhA 6 |

Displayed hypotheses: NONE in the brief's sense (a hypothesis the record does not state). The three recursion lemmas carry `2 ≤ n` and
`¬ p ∣ n`, which are the subjects of those lemmas, not conditions on a witness value; every witness-value theorem is unconditional. No
"H-x" anywhere. Every proof is over Mathlib alone (the trusted file imports `Mathlib` only; the challenge and solution files import
`ChallengeDeps.I1Witness` only; Zeta23 is not imported by any of the seven topic files); `#print axioms` = [propext, Classical.choice,
Quot.sound] for all seventeen names (`rung1-print-axioms.log`, `print-axioms.log`); the comparator (statement identity, axiom check,
Lean-kernel replay, nanoda replay) PASSED on both topics (`rung1-comparator.log`, `comparator-run.log`, exit 0 each).

## 2. What is NOT covered — stated nowhere in Lean (each sentence re-derived; the checker will re-derive them again)

* **(F-a) The −F′/F identification.** No theorem, definition or statement in the seven topic files mentions a Dirichlet series, a
  logarithmic derivative, `ζ_Q`, `F(s)`, or convergence [CORRECTION 08:10 IST 2026-09-29, Session 32 — CHECK-O F2: read "no theorem or statement"; the DEFINITIONS' docstrings and the file headers do name `ζ_Q`, `F(s)` and −F′/F as the record's sentences being restated (ChallengeDeps lines 28, 34, 64)]; the phrase "−F′/F" occurs in header comments and docstrings only, as the
  record's sentence being restated. What connects `LambdaReal epsteinB` to the record's Λ_Q is the classical identity in the first
  paragraph, by hand.
* **(N2) The Davenport–Heilbronn function itself.** Neither its Dirichlet series, its analytic continuation, its functional equation,
  nor its off-line zero ρ = 0.8085… + 85.699…i (zoo I.1) is stated. `dhA` is the coefficient array alone.
* **(N3) Anything about Epstein zeta functions beyond the coefficient array.** "h = 2", "D = −20", "RH-false class" are labels from the
  record repeated in comments; no class number, no discriminant, no zero of ζ_Q is a Lean object. `epsteinB` is the count of
  representations by x² + 5y² over the box, halved — nothing else.
* **(N4) The "no Euler product" reading.** The zoo reads Λ_DH(12) < 0 and Λ_Q(6) ≠ 0 at a non-prime-power as the failure of an intact
  Euler product and of Λ(n) ≥ 0. The Lean statements are the VALUES; no theorem says "DH has no Euler product", "Λ_DH is not
  supported on prime powers" as a universal, or "Λ(n) ≥ 0 fails" as a property of a function. The word "witness" in theorem names
  and docstrings is the zoo's vocabulary, not a formal claim.
* **(N5) The numeric values.** −0.7629…, −0.3120927…, +1.9364, 0.28407904384…, ±3.5835…, −7.1670… appear in comments only; no
  decimal approximation is a Lean statement. The closed forms are; the signs are.
* **(N6) The rest of the record's tables.** Λ_Q(54), Λ_Q(84) (the other negative values), the support list {6, 14, 21, 36, 46, 54, 69,
  84, 86, 94}, Λ_DH(2^k) and the coefficient-support theorem of the Session-24 rider, the genus identity and the contrast object ζ_K of
  §6.2's structural checks — none is stated.
* **(N7) The axiom-format statement of zoo line 666** ("the AXIOM-FORMAT statement with effectivity + duality axioms") is not stated;
  only "the exact witnesses" half of that line is formalized.
* **(N8) ζ, RH, any zero of anything.** Nothing.

## 3. Where the formal statement DIFFERS from the prose (each a deliberate choice, recorded)

* **(D1) Two objects for the record's one.** The record's Λ_f(n) is a real number; here `lambdaVec b n p` is the coefficient of log p
  (the recursion solved with log n replaced by the exponent vector, so that the arithmetic is ring arithmetic and the kernel can decide
  it) and `LambdaReal b n` is the finite sum Σ_{p ≤ n prime} lambdaVec b n p · Real.log p. The exponent-vector recursion is the
  record's recursion coefficient by coefficient because log n = Σ_p e_p(n) log p and the recursion is linear in Λ; this identification
  is the definition of `LambdaReal`, not a theorem.
* **(D2) The recursion is defined with a fuel.** `lambdaVec b n p := lambdaVecAux b p n n`, `lambdaVecAux` structural in its fuel
  argument (`typing.log`). The record's recursion is recovered as the theorem `lambdaVec_rec` (for every n ≥ 2), with `lambdaVec_one`;
  a reader who trusts the theorem need not trust the fuel.
* **(D3) e_p(n) is Mathlib's `padicValNat p n`.** `lambdaVec b n p` is defined for every p (also p = 0, 1 and composite p), but
  `LambdaReal` sums only over primes p ≤ n, so the non-prime values are never consumed. `padicValNat p 0 = 0`, but `lambdaVec b 0 p = 0` by
  definition (n < 2) [CORRECTION 08:10 IST 2026-09-29, Session 32 — CHECK-O F3, re-derived at ChallengeDeps line 38: at n = 0 the fuel is 0 and `lambdaVecAux` returns 0 by its fuel-0 clause `| 0, _ => 0`; the `n < 2` branch is never reached], so b 0 is never consumed either.
* **(D4) r_Q(n) is DEFINED as the count over the box |x|, |y| ≤ n.** `epsteinB n = card {(x, y) ∈ Icc (−n) n × Icc (−n) n : x² + 5y² = n} / 2`.
  The box contains every solution (x² ≤ n and 5y² ≤ n force |x|, |y| ≤ √n ≤ n for n ≥ 1; at n = 0 the box is {(0, 0)}), so this IS
  r_Q(n)/2 for every n — a hand fact; no second definition and no lemma `epsteinB_eq_count` was introduced (BRIEF §0). `epsteinB 0 = 1/2`
  (the origin, halved) is never consumed (D3).
* **(D5) The Epstein array is rational and is cast to ℝ inside `LambdaReal`.** `epsteinB : ℕ → ℚ` so that the kernel decides the
  coefficients; the real statements read `LambdaReal (fun n => (epsteinB n : ℝ))`. The solution proves that `lambdaVec` commutes with the
  cast (`ratCast'`, induction on the fuel), so the ℚ values are the ℝ values (PREDERIVATION-ERRATA E8).
* **(D6) `dhA : ℕ → ℝ` by `n % 5`.** `dhA n = 1, κ, −κ, −1, 0` at n % 5 = 1, 2, 3, 4, 0; `dhA 0 = 0` (0 ≡ 0), consistent with a₅ = 0
  and never consumed (D3).
* **(D7) `kappa` uses Mathlib's `Real.sqrt`,** which is 0 on negative arguments. Both radicands here are positive (5, and 10 − 2√5 =
  5.527…), so `kappa` is the record's real number; positivity of the inner radicand is used inside the proof of `kappa_pos` (4 < 10 − 2√5)
  but is not a separately shipped statement.
* **(D8) Two forms of each real value are stated.** `epstein_witness_6`, `epstein_witness_36` and `dh_witness_12` carry both the record's
  log 2 / log 3 form (the JSON's `exact` strings; the brief's statements) and the record's log 6 / log 12 form, as conjuncts; `dh_six`
  carries the log 6 form only (the record's), `dh_four` and `dh_witness_3` the single-log forms. `lambdaVec dhA 12 2` is written
  `-kappa * (1 + kappa ^ 2) * 2` as the brief wrote it (= −2κ(1 + κ²)).
* **(D9) Additions to the brief's list of statements:** the three recursion lemmas (R), `dhA_one`, and the optional (D3) rows `dh_four`,
  `dh_six` (each with its real value and sign). Every statement of BRIEF §0 (E1), (E2), (D1), (D2) is present with its brief name
  where the brief gave one (`epstein_witness_36`, `kappa_pos`); the others are named here (`epstein_six_coeff`, `epstein_witness_6`,
  `epstein_thirtysix_coeff`, `dh_three_coeff`, `dh_witness_3`, `dh_twelve_coeff`, `dh_witness_12`).
* **(D11) [added 08:10 IST 2026-09-29, Session 32 — CHECK-O F1, re-derived by the orchestrator] `lambdaVec_rec` is the record's recursion only for arrays with b₁ = 1.** The record's recursion reads b_n log n = Σ_{d | n} Λ(d) b_{n/d} = Λ(n)·b₁ + Σ_{d < n} Λ(d) b_{n/d}; the shipped solved form Λ(n) = b_n e_p(n) − Σ_{d < n} Λ(d) b_{n/d} drops the b₁ factor, so for a general array it is the record's recursion divided through by b₁ only when b₁ = 1. Both shipped arrays have b₁ = 1 as theorems (`epsteinB_one`, `dhA_one`), so every witness value is the record's; no value changes. Sentences calling `lambdaVec_rec` "the record's recursion" for every array (this ledger §1 row 1, §3 (D1)–(D2); BUILD-NOTES lines 67, 75; README line 489; yaml lines 675–676, 1027, 1382; the challenge file's header lines 20–22 — which also says "prime index p" where the theorem holds for every p — and docstring line 44; solution lines 16, 206) read with this qualifier. The Lean comment lines are recorded, not edited (the D5 rule: no Lean edit after the comparator runs).
* **(D10) `noncomputable section` around `epsteinB`, `LambdaReal`, `kappa`, `dhA`.** The compiler flags the elaborated `Preorder ℤ`
  instance path of `Finset.Icc` as noncomputable; this concerns compiled code only. Kernel evaluation under `decide +kernel` is unaffected
  and is what the proofs use (measured: `typing.log`).

## 4. What the label may and may not say

May: the BRIEF §1(4) text of the first paragraph, verbatim; the refutation-shaped close's "Lands" sentence (BRIEF 10(c)): "I.1's
axiom-level filter has kernel-checked witnesses: Λ_Q(36) < 0 for x² + 5y² and Λ_DH(3), Λ_DH(12) < 0 for Davenport–Heilbronn, as values
of the von Mangoldt recursion on the coefficient arrays". May not: "I.1 formalized" (the filter is a reading and an executable test,
not a theorem); "DH has no Euler product" or "Λ_DH ≥ 0 fails" as theorems (N4); "−F′/F formalized" (F-a); anything about the zeros of
either function (N2, N3); anything about ζ or RH (N8).
