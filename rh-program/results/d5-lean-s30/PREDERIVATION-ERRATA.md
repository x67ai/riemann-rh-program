# D5 (F3, G4) — the attack on the orchestrator's pre-derivation of BRIEF.md §0 (builder, Fable 5.1; Session 30, 2026-09-28)

Brief: `results/d5-lean-s30/BRIEF.md`, SHA-256 `22e8656f36d04aeecbc908d46f45285f83c2b667fd092f8f7c13f8eb5f846fae` (recomputed 23:49 IST).
Method: every step of §0's pre-derivation ((T1), (T2), (T3) and the three "does NOT give" items) re-derived by hand from the
definitions the brief fixes in §1(1), with the Mathlib conventions that the formal statement will inherit (`tsum` of a non-summable
family is 0; `Real.log 0 = 0`; `Real.sqrt 0 = 0`; `(0 : ℝ) ^ y = if y = 0 then 1 else 0`; `vonMangoldt 0 = vonMangoldt 1 = 0`;
`Real.rpow_def_of_pos : 0 < x → x ^ y = exp (log x * y)`). "No error found" entries name the check that was run.
Verdict up front: **(T1) is correct as stated — stop line (iv) does not fire.** Six items below; two are omissions that change what
is SHIPPED (E1, E5 — statements added), four are precision errors in the prose that change no statement (E2, E3, E4, E6).

## (T1) the identity — no error found

Check: term by term. Fix a real `a`, an even `g : ℝ → ℂ`, and `k := weilTestOf a g`, i.e. `k u = (1/2) g u · tilt a u`,
`tilt a u = exp (−(a − 1/2) |u|)`.
* `n = 0`: left summand `Λ(0) · 0^(−a) · g (log 0) = 0 · (…) = 0`; right summand `(Λ(0)/√0) · (…) = (0/0) · (…) = 0 · (…) = 0`.
  Both 0 in Mathlib's conventions — no case split on `a` is needed (`0 ^ (−a)` is 1 at a = 0 and 0 otherwise, but it is multiplied by
  `Λ(0) = 0`).
* `n ≥ 1`: `log n ≥ 0`, so `|log n| = log n` and `tilt a (log n) = exp (−(a − 1/2) log n) = n^(1/2 − a)` (`rpow_def_of_pos`, n > 0).
  `k (log n) + k (−log n) = (1/2) g(log n) tilt a (log n) + (1/2) g(−log n) tilt a (−log n) = g(log n) tilt a (log n)` — uses that `g`
  is even AND that `tilt a` is even (`|−u| = |u|`); the pre-derivation says "[g and m_a even]", correct.
  `(Λ(n)/√n) · g(log n) · n^(1/2 − a) = Λ(n) · n^(−1/2) · n^(1/2 − a) · g(log n) = Λ(n) n^(−a) g(log n)` (`sqrt = rpow (1/2)`,
  `rpow_neg`, `rpow_add` on n > 0). Correct.
* The identity of `tsum`s then follows from `tsum_congr` with NO summability hypothesis: if the common summand is not summable both sides
  are 0 by Mathlib's convention. The pre-derivation's "no convergence hypothesis (a termwise identity of tsums)" is right, and the
  formal statement is exactly that. (Whether the number is a meaningful datum is a separate matter: with `tsupport g ⊆ Icc (−L) L`
  the summand vanishes for `n > e^L`, both sums are finite — see E5.)
* Sign: C1's master formula and Zeta23's `literatureRHS` both carry the prime sum with a MINUS sign; the identity is between the
  unsigned sums and the signs agree, so no sign flip is hidden. Checked against `ExplicitFormula.lean` line 72 and the MASTER FORMULA
  paragraph quoted in §0.
* Range of `a`: the master formula is stated for a > 1/2; the identity holds for every real a (no step used a > 1/2). Correct as the
  pre-derivation says. Complex a is not treated (it would need `Complex.cpow`); the brief never asks for it.

## (T2) the multiplier bounds — no error found; one redundant hypothesis (E4)

Check: `|−(a − 1/2)|u|| = |a − 1/2| · |u| ≤ |a − 1/2| · L` for `|u| ≤ L`, so `−|a − 1/2| L ≤ −(a − 1/2)|u| ≤ |a − 1/2| L`, and `exp` is
monotone. Positivity is `Real.exp_pos`. Correct.
**E4 (precision, no statement change in substance).** The hypothesis `0 ≤ L` in `weilContainment_tilt_bounds` is implied by `|u| ≤ L`
(`0 ≤ |u|`). The shipped statement DROPS it (a strictly stronger theorem with the same content); BUILD-NOTES §"Statement decisions"
records the change against the brief's list.

## (T3) the band and the inverse — correct; two omissions (E1, E5) and one weakening (E6)

* `tsupport (weilTestOf a g) ⊆ tsupport g`: `g u = 0 ⟹ weilTestOf a g u = 0`, so `support ⊆ support`, closure is monotone. Correct.
  **E6 (weakening).** Because `tilt a u > 0` and `1/2 ≠ 0`, `weilTestOf a g u = 0 ⟺ g u = 0`: the supports are EQUAL, hence
  `tsupport (weilTestOf a g) = tsupport g`. The pre-derivation states only `⊆`. Both are shipped (`weilContainment_tsupport`,
  `weilContainment_tsupport_eq`); the equality is what "the same band" literally means.
* Continuity: `weilTestOf a g = const · g · (ofReal ∘ exp ∘ (const · |·|))`, all continuous. Correct.
* `tilt a u · tilt (1 − a) u = exp (−(a − 1/2)|u| − ((1 − a) − 1/2)|u|) = exp 0 = 1` since `−(a − 1/2) − (1/2 − a) = 0`. Correct.
* The converse witness `g := 2 k · tilt (1 − a)`: even (k even, tilt even), `tsupport g = tsupport k ⊆ Icc (−L) L` (E6 again, or the
  ⊆ direction with the roles of the factors swapped), and `weilTestOf a g u = (1/2)(2 k u · tilt (1 − a) u) · tilt a u = k u`, so
  by (T1) `tiltedPrimeSide a g = primeSide (weilTestOf a g) = primeSide k`. Correct. Note that the support hypothesis on k is used ONLY
  to produce the support conclusion on g; the identity itself needs nothing.
* **E1 (omission — changes what is shipped).** The pre-derivation's sentence "(T1)+(T3) together are 'the family spans EXACTLY
  bandwidth-log X Weil-EF data' on the prime side: the level-a family and the classical band-L family are the same set of numbers"
  needs, for the ⊆ direction, that `weilTestOf a g` is itself an EVEN test on the band (the classical family is indexed by even
  band-limited k). Evenness of `weilTestOf a g` for even g is true (`tilt a` is even) but is stated NOWHERE in §0's list of
  theorems. Added: `weilContainment_even : ∀ a g, (∀ u, g (−u) = g u) → ∀ u, weilTestOf a g (−u) = weilTestOf a g u`, and the sentence
  itself as a theorem, `weilContainment_range_eq`: for every real a and L, the set `{ tiltedPrimeSide a g | g even, tsupport g ⊆
  Icc (−L) L }` EQUALS the set `{ primeSide k | k even, tsupport k ⊆ Icc (−L) L }`. This is the record's "spans exactly" sentence,
  character for character, as one Lean statement; without E1 the shipped list would only have implied it.
* **E5 (omission — changes what is shipped).** §0 says "the n ≤ X cutoff of the master formula is automatic when tsupport g ⊆
  [−log X, log X], since Λ(n) g(log n) = 0 for n > X", and §1's fidelity paragraph lists "`tsum` over all n in place of 'n ≤ X'
  (equal by the support)" as a divergence to be RECORDED. The equality is a theorem, not a divergence to be taken on trust: for
  `tsupport g ⊆ Icc (−L) L`, `tiltedPrimeSide a g = ∑ n ∈ Finset.range (⌊exp L⌋₊ + 1), Λ(n) n^(−a) g(log n)` (n > e^L ⟹ log n > L ⟹
  log n ∉ tsupport g ⟹ g (log n) = 0). Added as `weilContainment_cutoff`; the ledger row becomes "differs in form, equal by a theorem
  of the file", which is stronger than "equal by the support" said in prose. The argument in §0 is right (n > X, X = e^L, gives
  log n > L); it silently uses X ≥ 1 so that the band is non-empty — for X < 1 the band `Icc (−L) L` is empty, g = 0 and both
  sides are 0, so nothing breaks.

## The three "does NOT give" items — one precision error (E2), one imprecision (E3), one correct as stated

* **E2 (precision error in the prose; the CONCLUSION stands).** §0 (i) says "k_{a,g} is not C² at u = 0 for a ≠ 1/2 (|u| has a
  kink)". As a universal statement over g this is FALSE: if g vanishes to order ≥ 3 at 0 (or g ≡ 0) then `g · exp (−c|u|)` is C² at
  0 for every a. What is true, and sharper: for `g(0) ≠ 0` and `a ≠ 1/2`, `k_{a,g}` is not even C¹ at 0 — the one-sided derivatives at
  0 are `(1/2)(g'(0) ∓ (a − 1/2) g(0))` and differ by `(a − 1/2) g(0) ≠ 0`. For C1's family `g = ŵ` with a window `w ≥ 0`, `w ≢ 0`,
  one has `g(0) = ∫ w > 0`, so the failure is real for every member of the record's family and at every a ≠ 1/2. The conclusion —
  the Zeta23 test class `ContDiff ℝ 2` is NOT preserved by the tilt as a class, and no statement of this unit feeds `weilTestOf a g`
  into `EF_lit` — is correct. FIDELITY.md states the sharp form. (A witness theorem `¬ ContDiff ℝ 2 (weilTestOf 1 (fun _ => 1))` is
  a candidate addition if the budget allows — recorded in BUILD-NOTES either way.)
* **E3 (imprecision, no effect).** §0 writes "(C1's 'cos-transform of w' is ŵ, even when w is real and even)". The cos-transform
  `y ↦ ∫ w(t) cos(ty) dt` is even in y for EVERY w (cos is even) — no hypothesis on w is needed for evenness; it coincides with ŵ
  (Zeta23's `paperFT`, sign +i) exactly when the sine part `∫ w(t) sin(ty) dt` vanishes, e.g. for even w; realness of w gives
  realness of the cos-transform, not its evenness. The theorem quantifies over every even g, so the sentence's imprecision reaches
  no statement; the fidelity paragraph uses the corrected wording.
* (ii) "nothing is said about the zero side at level a" — correct: no statement of this unit mentions zeros, `ZeroConfig`, `EF_lit`
  or `literatureRHS`'s other terms. (iii) the μ-band and nonlinear functions of the band are outside — correct: every statement is
  linear in the test and speaks of the prime functional only.

## One more check the pre-derivation did not run: the C² refinement of the containment (recorded, not claimed)

The record's classical data class is Zeta23's `EF_lit` test class (C², compact support). The containment shipped here lands in the
class of even band-limited tests WITHOUT regularity. A refinement "every tilted datum is `primeSide k'` for some C² even k' on the
same band" is true by finite interpolation (the prime functional sees k only at the finitely many points ±log n, 2 ≤ n ≤ e^L) but is
NOT formalized and NOT claimed; FIDELITY.md lists it under "not covered". No error in §0 here — §0 never claimed it.

## Summary of what changed against §1's list because of this attack

Added: `weilContainment_even` (E1), `weilContainment_range_eq` (E1), `weilContainment_tsupport_eq` (E6), `weilContainment_cutoff` (E5).
Changed: `weilContainment_tilt_bounds` loses the redundant `0 ≤ L` (E4). Unchanged: everything else in §1(1)–(2), including every name.
Stop line (iv) — "the pre-derivation is wrong at (T1) in a way that changes the statement's shape" — did NOT fire.
