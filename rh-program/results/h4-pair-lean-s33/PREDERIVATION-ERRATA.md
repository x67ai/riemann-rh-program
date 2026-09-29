# H4 — the attack on the typing note's §2–§4 derivations and the brief's numbers (builder, Fable 5.1; Session 33, Tue Sep 29 11:21:44 IST 2026)

Brief: `results/h4-pair-typing-s32/UNIT-BRIEF.md`, SHA-256 `2d80f9db8ccf04765840b041189dc771813f5fdbb77767c40d471e8b9908cb94` (recomputed at the start; prefix 2d80f9db8ccf0476 as the
launch message says). Typing note: `results/h4-pair-typing-s32/TYPING-NOTE.md`, SHA-256 `744e42e1ba082d5eae6c29ddb690e6656150e14e6d35d400e5339e85ac9e4199`.
Method: every derivation of the note's §2 (the regrouping), §3 ((T1)), §4 (Prop. 4.5's expansion, the error budget, the two generic
cosh bounds, Route P) and every number the brief §0 and §2 item 1 carry were re-derived by hand and RECOMPUTED by the scratch script
`tools/h4_numbers.py` (mpmath at 30 digits for the transcendental values; exact integers and fractions for the power sums and the
certificate's rational bounds; output `tools/h4_numbers.log`). Mathlib names were re-read at the line in
`~/rh-lean-work/checker-clone-s21/.lake/packages/mathlib` (51e6992e). "No error found" entries name the check that was run.
Nothing about ζ or RH follows from anything here.

**Verdict up front.** The derivations of §2–§4 are correct in substance and every anchor number of the brief reproduces to the digits
stated. Statement shapes unchanged. One genuine arithmetic slip in the note (E7: the dyadic π bracket it offers as a consequence of
`pi_gt_d6` does not follow from it — unused by this unit), one Mathlib name settled that the note left unverified (E9), one per-cosh
error figure that is an over-estimate rather than the value (E5, harmless), and two design decisions for the Lean proofs recorded
(E1, E10). No stop line fires at this stage.

## The anchor numbers (brief §2 item 1; ORCHESTRATOR-NOTES item 1) — recomputed, no error found

| quantity | brief / note | recomputed (`h4_numbers.log`) |
|---|---|---|
| ā(1/4) = (1/65) Σ_{j=−32}^{32} cosh(π j/128) | 1.109444 (note: 1.1094437000) | 1.10944370003 |
| ā(1/2) = (1/65) Σ cosh(π j/64) | 1.481406 (note: 1.4814055033) | 1.48140550329 |
| F1 − S2 at (d, μ) = (1/4, 1/20), closed form 2μ²ā(2d)² − 4μ(ā(d)² − 1) | −0.0352003 (record −3.520·10⁻²) | −0.0352002533828 |
| the same by the integer-frequency row Σ_s W2(s)(φ₀(s) + 2μ cosh(βs))², W2(s) = (65 − \|s\|)/65², φ₀ = 64 at s = 0, −1 otherwise | (note §1.1: the same digits) | F1 = 63.9697997466, S2 = 64.005, difference −0.0352002533828 — identical to 13 digits |
| the mod-65-REDUCED row (the shipped `gridRowQ` shape with the pair's cosh at the reduced residue) | −0.0144817 | −0.01448171249 — a different number; the unit needs the new row (note §1.1 confirmed) |
| 2μ²ā(1/2)², 4μ(ā(1/4)² − 1) | 0.0109728, 0.0461731 | 0.01097281133, 0.04617306471 |
| (MI) at the anchor: T = 3M − 2N_d = 3(64 + 2μ) − 2·66 | T = 60.300, F1 − T = +3.67, S2 − T = 2(μ−1)(μ−2) ≈ 3.705 | T = 60.3, F1 − T = 3.6698, S2 − T = 3.705 — (MI) HOLDS at the anchor; only the floor F1 ≥ S2 fails |
| S₂, S₄, S₆, S₈ over j ∈ [−32, 32] | 22880, 14492192, 10924353440, 8964042662432 | 22880, 14492192, 10924353440, 8964042662432 (exact) |
| Σ_s W2(s) = 1; (T1) at d and 2d | (note §3) | 1.0; both residuals < 10⁻³⁰ |
| certified bound 2μ²U² − 4μ(L² − 1) | −0.0337, "0.0015 of margin spent" | −0.033682052 with L = L(3.141592) = 1.1060210969, U = U(3.141593) = 1.4815182153 (exact rationals; the numerator of the bound has 133 digits); margin spent 0.0015182 |
| the first-order budget: 8μā(1/4) δ₁ + 4μ²ā(1/2) δ₂ | 0.4438 δ₁ + 0.0148 δ₂; δ₁ < 0.0793, δ₂ < 2.376 | 0.443777 δ₁ + 0.0148141 δ₂; δ₁ < 0.07932, δ₂ < 2.3761 alone; actual δ₁ = ā(1/4) − L = 0.0034226, δ₂ = U − ā(1/2) = 0.000112712 |
| the chain at m = 1, d = 1/4 | (brief item 7) | F1 − S2 = 3.46566 ≥ 2m(mA² − A + 1) = 3.42631 > 0; at m = 2: 15.7096 ≥ 15.6309 |
| Cauchy–Schwarz ā(d)² ≤ (1 + ā(2d))/2 at d = 1/4 | (brief item 6) | 1.2308653 ≤ 1.2407028 |

The exact coefficients Route P needs (`h4_numbers.log`): L(π) = 1 + (11/1024) π² (from S₂/(2·128²·65) = 22880/2129920 = 11/1024);
U(π) = 1 + (11/256) π² + (34837/62914560) π⁴ + (5252093/1546188226560) π⁶ + (21548179477/886646176638566400) π⁸. The Lean
certificate states these sums with the power sums written out (S_k/(k!·64^k·65)), not with the reduced fractions; `norm_num` reduces.

## §2 The regrouping `sum_W2_mul` — no error found; one design decision (E1)

Check: W2 n s = Σ_{j ∈ B, s − j ∈ B} (1/M)², so Σ_s W2(s) g(s) = Σ_s Σ_{j ∈ B, s−j ∈ B} (1/M)² g(s) = Σ_{(j₁, j₂) ∈ B×B} (1/M)² g(j₁ + j₂)
under the bijection (j₁, j₂) ↦ (s, j) = (j₁ + j₂, j₁) with inverse (s, j) ↦ (j, s − j); the image of B×B under (j₁, j₂) ↦ j₁ + j₂
lies in [−2n, 2n], so the outer sum over Icc (−2n) (2n) loses nothing. Correct.
**E1 (design, no error).** The note's route (fibers of the map (j₁, j₂) ↦ j₁ + j₂ through `Finset.sum_fiberwise_of_maps_to`, then
`Finset.sum_product`, then a `sum_nbij'` per fiber) is sound; the Lean proof uses the equivalent shorter route: for fixed j₁ reindex
the inner sum Σ_{j₂ ∈ B} f(j₁ + j₂) as Σ_{s ∈ Icc (−2n) (2n)} [s − j₁ ∈ B] f(s) (`Finset.sum_nbij'` with j₂ ↦ j₁ + j₂, inverse
s ↦ s − j₁; `Finset.sum_filter`), swap the two sums (`Finset.sum_comm`), and read the inner Σ_{j₁ ∈ B} [s − j₁ ∈ B] (1/M)² g(s) as
W2 n s · g s (`Finset.sum_mul` on the definition). Same content, one reindexing instead of two.

## §2 The agreement lemma — no error found

Check: with no pair, `pairFormFactor n m ∅ s = dftMarkQ ζ m (s : ZMod M)` (the empty sum is 0), and `sum_W2_mul` with
g s = normSq (dftMarkQ ζ m (s : ZMod M)) gives Σ_{j₁, j₂} (1/M)² normSq (dftMarkQ ζ m ((j₁ + j₂ : ℤ) : ZMod M)); `gridRowQ` has
`(j₁ : ZMod M) + (j₂ : ZMod M)` — equal by `Int.cast_add`. Correct.

## §3 (T1) `sum_W2_cosh` — no error found

Check: cosh(β(j₁ + j₂)) = cosh βj₁ cosh βj₂ + sinh βj₁ sinh βj₂ (`Real.cosh_add`, `Mathlib/Analysis/Complex/Trigonometric.lean`
line 776 in the ℝ namespace — re-read); Σ_{j₁,j₂} u² (C₁C₂ + S₁S₂) = (Σ u C)² + (Σ u S)² (`Finset.sum_mul_sum`); Σ_{j∈B} u sinh βj = 0
by the involution j ↦ −j (`Finset.sum_involution`, `Real.sinh_neg`; the fixed point j = 0 has sinh 0 = 0). So the sum is ā(x)².
At x = 0: ā(0) = Σ u = 1 and the identity reads Σ_s W2 = 1. Correct. The argument identity 2π(j₁ + j₂)x/(2n) = 2πj₁x/(2n) + 2πj₂x/(2n)
holds by `ring` for every n including n = 0 (where Lean's x/0 = 0 makes every cosh argument 0 and every statement remains true).

## §4.2 Prop. 4.5's expansion — no error found (re-derived for every n)

With M = 2n + 1, band s ∈ [−2n, 2n]: φ₀(s) := dftMarkQ ζ (vacancyMark n) (s : ZMod M) = Σ_{k ≠ 0} χ(s k) = (Σ_k χ(s k)) − 1
= (if (s : ZMod M) = 0 then M else 0) − 1 (character orthogonality `sum_chi_mul` with the factor order r·k ↔ k·r by `mul_comm`) and
(s : ZMod M) = 0 iff s = 0 on the band (a multiple of M with |s| ≤ 2n < M is 0: `int_eq_zero_of_dvd_of_bounds`), so φ₀(s) = 2n at
s = 0 and −1 otherwise — the paper's "64 at s ≡ 0 and −1 otherwise" at n = 32. The pair at the hole contributes
2μ cosh(βs) · χ(s·0) = 2μ cosh(βs) (`chi_zero`), a real number, so |c_s|² = (φ₀(s) + 2μ cosh βs)² (`Complex.normSq_ofReal`). Then
  Σ_s W2 φ₀² = pairRow n (vacancyMark n) ∅ = gridRowQ n (vacancyMark n) = Σ_k (vacancyMark n k)² = 2n (the agreement lemma,
    `gridRowQ_eq`, and #{k ≠ 0} = M − 1 = 2n);
  Σ_s W2 φ₀ cosh(βs) = −Σ_s W2 cosh(βs) + W2(0)·M·cosh 0 = −ā(d)² + 1 (φ₀ = −1 + M·[s = 0]; W2(0) = M·(1/M)² = 1/M since the
    filter at s = 0 is the whole band);
  Σ_s W2 cosh²(βs) = Σ_s W2 (1 + cosh 2βs)/2 = (1 + ā(2d)²)/2 (cosh 2y = 2cosh²y − 1 from `Real.cosh_two_mul`, `Real.cosh_sq`;
    (T1) at x = 0 and x = 2d, with 2·(2πsd/(2n)) = 2πs(2d)/(2n)).
  Total: 2n + 4μ(1 − ā(d)²) + 4μ²(1 + ā(2d)²)/2 = (2n + 2μ²) + 2μ²ā(2d)² − 4μ(ā(d)² − 1). Correct — for every n, d, μ, with no
  hypothesis; the numbers of the table confirm it at n = 32 to 13 digits. Prop. 4.1's ledger is not used, as the note says.
**E2 (precision, no error).** The note's display writes the cross term as "4μ[W2(0)·2n − (ā(d)² − W2(0))]" = 4μ[(2n + 1)/(2n + 1) − ā(d)²]:
correct (W2(0)(2n + 1) = 1), and the same as −ā(d)² + 1 above.

## §4.3 The error budget — no error found

The bound 2μ²U² − 4μ(L² − 1) is increasing in U and decreasing in L; derivatives 4μ²U = 0.0148 and −8μL = −0.4438 at the anchor
values; tolerances 0.0793 and 2.376 alone (table). The safe split δ₁ ≤ 0.04, δ₂ ≤ 1.0 is far inside; the actual enclosure errors are
0.0034 and 0.00011.

## §4.4 The two generic cosh bounds — E5, E7, E9

**Lower, 1 + x²/2 ≤ cosh x — no error found.** cosh x = cosh(2·(x/2)) = cosh²(x/2) + sinh²(x/2) = 1 + 2sinh²(x/2); |sinh(x/2)| =
sinh |x/2| ≥ |x/2| (`Real.abs_sinh` at DerivHyp.lean line 419, `Real.self_le_sinh_iff` line 451 at the nonnegative |x/2|); so
2sinh²(x/2) ≥ 2(x/2)² = x²/2. Correct.
**E5 (over-estimate, harmless).** The note says "Error at |x| ≤ π/4: cosh x − 1 − x²/2 ≤ x⁴/24·cosh x ≤ 0.021": the value at π/4 is
0.016184; 0.021 is the stated upper estimate x⁴/24·cosh x, not the error. Both are under the tolerance.
**Upper, |x| ≤ 9/2 ⟹ cosh x ≤ 1 + x²/2 + x⁴/24 + x⁶/720 + x⁸/20160 — no error found.** `Complex.exp_bound'` (Exponential.lean
line 407: ‖x‖/(n+1) ≤ 1/2 → ‖exp x − Σ_{m<n} xᵐ/m!‖ ≤ ‖x‖ⁿ/n!·2) at n = 8 needs |x| ≤ 9/2; π/2 = 1.5708 qualifies (`max |πj/64| =
1.5708`). Transferred to ℝ (`Complex.ofReal_exp`, the norm of a real cast is its absolute value) and applied at x and −x: the odd
terms cancel in (eˣ + e⁻ˣ)/2 and the two remainders 2x⁸/8! average to x⁸/20160. Correct. The excess at π/2 is 0.000894 (the note's
"0.0018" is the remainder bound 2(π/2)⁸/40320 for ONE exponential, i.e. an upper estimate; the averaged excess is 0.000113).
**E7 (arithmetic slip in the note, unused here).** §4.4 says "the bracket 3294198/2²⁰ < π < 3294200/2²⁰ follows from the two d6
lemmas by `norm_num`": 3294198/2²⁰ = 3.1415920258 > 3.141592, so the lower end does NOT follow from `pi_gt_d6 : 3.141592 < π` (it is
true, but needs a sharper lemma). The bracket that does follow is 3294197/2²⁰ < π < 3294200/2²⁰. The unit uses the d6 decimals
directly and never this bracket; the label's "dyadic certificate" refers to the kernel-checked rational certificate, as the brief
uses the word.
**E9 (name settled).** The note's §6 row 4 left the Mathlib name for constant-weight Cauchy–Schwarz unverified. At 51e6992e it is
`sq_sum_le_card_mul_sum_sq : (∑ i ∈ s, f i) ^ 2 ≤ #s * ∑ i ∈ s, f i ^ 2` (`Mathlib/Algebra/Order/Chebyshev.lean` line 136, over a
linearly ordered semiring — ℝ qualifies); the two-function form is `Finset.sum_mul_sq_le_sq_mul_sq`
(`Mathlib/Algebra/Order/BigOperators/Ring/Finset.lean` line 159). With #B = 2n + 1 = M and u = 1/M: ā(d)² = u²(Σ C)² ≤ u²·M·Σ C² =
u Σ C² = u Σ (1 + cosh 2βj)/2 = (1 + ā(2d))/2. Brief item 6 correct.
The other names, re-read at the line: `Real.pi_gt_d6` (Pi/Bounds.lean 178), `Real.pi_lt_d6` (184), `Real.one_le_cosh` (DerivHyp
435), `Real.cosh_two_mul` (Trigonometric.lean 830), `Real.cosh_sq` (823), `Real.cosh_eq` (760), `Real.exp_bound` (Exponential.lean
517, |x| ≤ 1), `Real.exp_bound'` (523, 0 ≤ x ≤ 1 — the note's "Real version at line 517" is `exp_bound`, correct), `Finset.sum_involution`
(`prod_involution` Basic.lean 665, additive by `to_additive`), `Finset.sum_fiberwise_of_maps_to` (256), `Finset.sum_product`
(Sigma.lean 80), `Int.card_Icc` (Int/Interval.lean 96).

## §4.5 Route P — no error found; E10 (design)

The symbolic pass-through Σ_j (1/65) P(πj/64) = 1 + π²S₂/(2·64²·65) + … is linear algebra on the power sums; coefficients in the
table. The certificate's cells: the two generic lemmas, four `decide +kernel` power sums, the π bracket step (monotonicity of even
powers in π > 0, `pow_le_pow_left₀`), one `norm_num` on a rational inequality whose numerator has 133 digits (Unit B's
`cert_numeric` did 577 digits). The value −0.033682 < 0 with 0.001518 of the record's 0.0352 spent — the brief's "−0.0337, 0.0015" to
the digits given.
**E10 (design).** In Lean the sum bound is proved term by term (`Finset.sum_le_sum` with the generic lemma at c·j, c = π/64 or
π/128) and the polynomial sum is expanded once by a per-term `ring` identity plus `Finset.sum_add_distrib` / `Finset.mul_sum` /
`Finset.sum_const`, the power sums entering through `Int.cast_sum` from the kernel facts. No per-term enclosure, as the note says.

## The chain (brief item 7) — no error found

2m²A² − 4m(a² − 1) ≥ 2m²A² − 4m((1 + A)/2 − 1) = 2m²A² − 2m(A − 1) = 2m(mA² − A + 1) (using a² ≤ (1 + A)/2 and m ≥ 0), and for
m ≥ 1, A ≥ 1: mA² − A + 1 ≥ A² − A + 1 = (A − 1/2)² + 3/4 > 0. So the expression is > 0. Integrality enters as 1 ≤ m only; the
atom theorems `per_atom_slack` / `mi_holds_integer` are not involved. Correct.

## The label and the forbidden phrasings — checked against the numbers

At the anchor (MI) holds (F1 − T = +3.67 > 0) while the floor F1 ≥ S2 fails (F1 − S2 = −0.0352 < 0); `floor_fails_anchor` is the
failure of the floor for a real mark and says nothing about (MI). The three forbidden phrasings appear nowhere in this file.

Closing stamp: Tue Sep 29 11:21:44 IST 2026.
