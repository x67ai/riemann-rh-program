# check-O.md — Job 2, the independent Opus 5 dual check of the Sector-I confinement theorem

**Written 2026-09-10 (Session 21, build stream `c2-r1-s21`, Job 2; standing orders 5 and 7).** Object of the check: `results/c2-r1/confinement-note.md` (Job 1, Fable 5.1), its `zoo-IV18-proposed.md`, `SHARED.md`, `hashes.txt` and the six scripts/logs under `results/c2-r1/verify/`, against the contract of `results/c2-m5/PRICING-next-unit.md` §1.2 quoted in `results/c2-r1/BRIEF.md`, the direction file `directions/C2-rigidity-conservation.md`, the Lean tree `~/rh-lean-work/zeta-23-lean-main`, the two arXiv PDFs in `fetched-r6/`, and `BARRIER-ZOO.md`.

**Method.** Every clause was re-derived from the objects, on paper, before the author's proof was compared with it; every constant was recomputed in code written for this check (`opus_independent.py`, transcript quoted inline below) and, separately, the author's six scripts were re-run and diffed against the logs on disk. No file of the author's was edited. Nothing was committed.

**Integrity of the deliverable.** All 22 SHA-256 lines of `hashes.txt` verify (`shasum -a 256 -c`: 22/22 OK). The two source PDFs hash to `274b3a0a…` (Trudgian) and `3fc4c89f…` (HSW), matching the note's D6 record byte for byte.

**Headline.** The theorem stands. All seven clauses CLOSE. The author's deviation D1 — the substantive one — is UPHELD: the contract's clause 2 hypothesis is unsatisfiable as written, the corrected hypothesis is exactly what the domination proof needs, and the layer constant is 4, not 2. Two further items owed by the brief and not done by Job 1 are discharged here: the `#print axioms` line for `EF_lit_zetaZeroConfig` (clean), and the standing-order-7 corpus re-read (no antecedent found). The defects found are wording and cross-reference only; they are listed in §12 and none of them touches a proof.

---

## §1 Clause 1 — the identity in cone form, and the normalization

### §1.1 The formal input, read independently

`~/rh-lean-work/zeta-23-lean-main/Zeta23/WeilEF/Main.lean` lines 268–270 read exactly as the note quotes them:

```
/-- **Hypothesis-free form**: [eq:EFstd] holds for the canonical
unconditional ζ zero configuration. -/
theorem EF_lit_zetaZeroConfig : Zeta23.EF.EF_lit zetaZeroConfig := EF_lit_zeta zetaSeam
```

and `Zeta23/ExplicitFormula.lean` lines 81–84 give the predicate with **exactly two hypotheses on the test**, `ContDiff ℝ 2 k` and `HasCompactSupport k`:

```
def EF_lit (Z : ZeroConfig) : Prop :=
  ∀ k : ℝ → ℂ, ContDiff ℝ 2 k → HasCompactSupport k →
    Summable (fun ρ : Z.carrier => (Z.mult ρ : ℂ) * paperFT k (gammaOf ρ)) ∧
    ∑' ρ : Z.carrier, (Z.mult ρ : ℂ) * paperFT k (gammaOf ρ) = literatureRHS k
```

`literatureRHS` (lines 69–73), `gammaBracket` (line 64), `paperFT` (`Defs.lean` line 44) and `gammaOf` (`Defs.lean` line 105) were read and match the note's quotations verbatim, as do `zetaSeam` / `zetaZeroConfig` (`Statement/SeamClosed.lean` lines 22, 26) and `zeta_local_zero_count_explicit` (`WeilEF/Effective.lean` lines 924–927).

**The `#print axioms` line owed under KICKSTART 10(f) (Job 1 declined it; run here).** A scratch file outside the repository, compiled with one `lake env lean` process against the existing build (no Lean file created, modified or rebuilt inside the tree):

```
'Zeta23.WeilEF.EF_lit_zetaZeroConfig' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.WeilEF.zeta_local_zero_count_explicit' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Both formal inputs are sorry-free and carry only Lean's three standard axioms. **10(f) is discharged.** (Note the namespace: the theorems are `Zeta23.WeilEF.…`, not `Zeta23.…`; the note's prose names them without the `WeilEF` component in one place, a harmless abbreviation.)

### §1.2 The identity, re-derived

Independently of the note, with `ŵ(ξ) = ∫ w(u)e^{−iuξ}du` and `ĝ(z) = paperFT g z = ∫ g(u)e^{izu}du` (these agree on ℝ for even real functions, which is the only case used — the two-convention split in §0.1 is harmless and I checked it is never used off the real axis except through `ĝ`):

* **Pole.** `ĝ(i/2) + ĝ(−i/2) = ∫ g(u)(e^{−u/2} + e^{u/2})du = 2∫ g cosh(u/2) du = 2∫w = 2ŵ(0)`. ✔
* **Primes.** `n^{−1/2}/cosh(½ log n) = n^{−1/2}·2√n/(n+1) = 2/(n+1)`, so `Σ_n Λ(n)n^{−1/2}(g(log n)+g(−log n)) = 4Σ_{n≥2} Λ(n) w(log n)/(n+1) = P(w) ≥ 0`. ✔ (Λ(1) = 0, so the Lean sum over all `n : ℕ` loses nothing.)
* **Archimedean.** `(1/2π)∫ ĝ(r) gammaBracket(r) dr = ∫ (ŵ ∗ μ_0)(r) A(r) dr` with `A := (1/2π)[Re ψ(¼+ir/2) − log π]`, using `ĝ(r) = (ŵ ∗ μ_0)(r)` for real `r`. ✔
* So `literatureRHS(g) = 2ŵ(0) + ∫(ŵ∗μ_0)A − P(w) = B(w) − P(w)`, i.e. **B(w) = Z(w) + P(w)**. ✔

**Lemma K re-derived.** `e^{i(x−iy)u} = e^{yu}(cos xu + i sin xu)`; for even real `g`, `Re ĝ(x−iy) = ∫ g(u)cosh(yu)cos(xu)du = ∫ w(u)k_y(u)cos(xu)du = (ŵ ∗ μ_y)(x)` by the convolution theorem (`k̂_y = 2πμ_y` by definition of `μ_y`), and this is ≥ 0 since `ŵ ≥ 0` and `μ_y > 0`. The orbit arithmetic is right: from `gammaOf ρ = (ρ − ½)/i`, the four zeros `{β ± iτ, 1−β ± iτ}` have γ-values `{±τ − iy, ±τ + iy}`, and with `ĝ(−z) = ĝ(z)` (g even) and `ĝ(z̄) = conj ĝ(z)` (g real) their shares sum to `2[ĝ(t−iy) + conj ĝ(t−iy)] = 4 Re ĝ(t−iy) = 4(ŵ ∗ μ_y)(t)`. ✔ The **orbit share is 4(ŵ ∗ μ_y)(t), not 2(ŵ ∗ μ_y)(t)** — this is the factor that D1 turns on, and the note's convention note in §0.1 (its `V` is twice C2 line 16's) is stated correctly.

Note that `Im ĝ(x−iy) = ∫ g sinh(yu) sin(xu) du` is not zero in general; the note never claims otherwise, and only the real part is used. ✔

**Lemma P re-derived and recomputed.** (i)–(iv) are correct as proved. My own quadrature (independent code):

```
  y=0.0 : mass 1.000000000000  peak 1.0000000000 = 1/sin(pi d)  tail ratio 2.000000
  y=0.25: mass 1.000000000000  peak 1.4142135624 = 1/sin(pi d)  tail ratio 2.003728
  y=0.40: mass 1.000000000000  peak 3.2360679775 = 1/sin(pi d)  tail ratio 2.009801
  y=0.45: mass 1.000000000000  peak 6.3924532215 = 1/sin(pi d)  tail ratio 2.010871
  y=0.49: mass 1.000000000000  peak 31.836225209 = 1/sin(pi d)  tail ratio 2.011225
  sharp tail constant 2(1+e^-2pi)/(1-e^-2pi)^2 = 2.011240  (c_P := 2.012 covers it)
```

and the monotonicity proof (`d/dc [c/(c²−s²)] = −(c²+s²)/(c²−s²)² < 0`, `c = cosh πξ` increasing in `|ξ|`) is correct. `c_P = 2.012 < 4` and `sin(πδ) ≤ πδ`, so the note's tail bound implies the contract's `4πδ e^{−π|ξ|}`. ✔ (D4 is a strengthening, not a weakening.)

### §1.3 The normalization against ζ — re-run

`verify/normalization_zeta_check.py` was re-run from a clean copy in a scratch directory. **The output reproduces `normalization_zeta_check_run.log` line for line** (`diff` empty apart from the log's trailing `exit=0` and the wall-clock seconds). In particular:

```
a(0) = -0.653847, A(0) = -0.855010, tau_0 = 6.3100, I_minus = 2.241523, 2 - I_minus = -0.241523
T=  11.0  B = 0.13597  P = 0.12839 (+0.01523 tail)  Z = 0.00000   B - shares = -0.00764
T=  12.0  B = 0.15030  P = 0.14328 (+0.01396 tail)  Z = 0.00004   B - shares = -0.00697
T=  14.0  B = 0.21866  P = 0.19453 (+0.01197 tail)  Z = 0.01817   B - shares = -0.00600
T=  16.0  B = 0.33348  P = 0.09503 (+0.01047 tail)  Z = 0.23323   B - shares = -0.00526
```

The zero share is identically 0 for T ≤ 11 and switches on across γ₁ = 14.134725 — the check the contract asked for. The residual `B − shares` is negative at every T with magnitude between 0.36 and 0.51 of the printed prime-tail estimate, i.e. of the right sign and order; it shrinks monotonically as `1/T`. Table N of §7 reproduces this log exactly, including `κ ≤ 0.13597` at T = 11 and `I₋ = 2.241523`.

**Caveat, recorded and not held against the note.** The Fejér elements are band-limited, not compactly supported, so they are outside the `C²_c` class of the formal input; the note says so and uses the check only as an illustration of the normalization. No proof depends on it. ✔

**VERDICT clause 1: CLOSES.**

---

## §2 Deviation D1 — the factor 2. **UPHELD, in both halves.**

This is the decisive item, and it was re-derived from scratch before the note's §2 was read.

### §2.1 Is the contract's hypothesis unsatisfiable?

The contract (PRICING-next-unit §1.2 clause 2) asks for

  μ_y(t − s) + μ_y(t + s) ≤ Ψ(s)  **for every s ∈ ℝ.**

The left side is an **even** function of `s`. So the condition is equivalent to `μ_y(t−s) + μ_y(t+s) ≤ min(Ψ(s), Ψ(−s))` for `s ≥ 0`. Since Ψ is supported on the positive ordinates, `Ψ(−s)` is exponentially small, and the condition collapses. Concretely at `s = −t`: the left side is `μ_y(2t) + μ_y(0) ≥ μ_y(0) = 1/sin(πδ) ≥ 1` for every δ ∈ (0, ½], while

* numerically (first 60 zeros): `Ψ(−t) = 1.04·10⁻¹⁹` at t = 0, `4.5·10⁻²¹` at t = 1, `6.5·10⁻⁵⁸` at t = 28, underflow at t = 10⁶;
* **and rigorously, without computing any zero:** `Ψ(−t) ≤ Σ_γ 2e^{−π(t+γ)} ≤ 2Σ_{k≥14} 5.4·10⁸ log(k+3) e^{−πk} = 2.54·10⁻¹⁰` for every `t ≥ 0`, using only the formal local count `zeta_local_zero_count_explicit` and `γ₁ > 14`.

So the hypothesis fails at `s = −t` for **every** `t > 0` and **every** `y ∈ [0, ½)`, and clause 2 of the contract, read literally, is vacuous. **The author's claim is correct, and it is correct for a structural reason (the parity mismatch), not a numerical accident.** The note's "< 10⁻¹⁹" is the numerical value at the worst case t = 0; the unconditional bound `2.5·10⁻¹⁰` above is what an audit-proof statement should quote, and I recommend the note record it (a one-line addition, §12 item 5).

`verify/confinement_edge.py`, re-run here, reproduces the same finding at 10⁶, 10⁷, 10⁸ ("(a) literal contract condition at s = −t … FAILS for every delta"), and its log reproduces line for line.

### §2.2 Is the corrected condition exactly what the proof needs?

Yes. Fold both sides onto `[0, ∞)` using `ŵ(−s) = ŵ(s)`:

  orbit share = `4∫_ℝ ŵ(s)μ_y(t−s)ds = 4∫_0^∞ ŵ(s)[μ_y(t−s) + μ_y(t+s)]ds`,
  on-line share `≥ 2∫_ℝ ŵΨ = 2∫_0^∞ ŵ(s)[Ψ(s) + Ψ(−s)]ds`.

Since `ŵ ≥ 0` is otherwise unconstrained by the comparison, the pointwise sufficient condition is

  **2[μ_y(t−s) + μ_y(t+s)] ≤ Ψ(s) + Ψ(−s)  for s ≥ 0**   (D),

which is the note's (D) verbatim, and the one-sided strengthening `2[μ_y(t−s)+μ_y(t+s)] ≤ Ψ(s)` follows from `Ψ(−s) ≥ 0`. ✔ Writing `Ψ_e` for the even part of Ψ, (D) says `μ_y(t−s)+μ_y(t+s) ≤ Ψ_e(s)`, i.e. **exactly the contract's condition with Ψ replaced by its even part** — the contract's error is that it compared an even kernel with a one-sided density. At `s = t` this is `2[μ_y(0) + μ_y(2t)] ≤ Ψ(t) + Ψ(−t)`, i.e.

  **2/sin(πδ) ≤ Ψ(t)**  up to terms below 10⁻¹⁹ (Lemma P(iii) at ξ = 2t ≥ 56, and §2.1 for Ψ(−t)).  ✔

### §2.3 Is the reading "a pair contributes two zeros" the right one?

Yes, and it is worth stating precisely because it is what the record must carry. The hypothetical off-line orbit is a **four**-element set `{β±it, 1−β±it}`; at the single height `+t` it puts **two** zeros, `β+it` and `1−β+it`, each carrying depth weight `μ_y(0) = 1/sin(πδ)`. The on-line side is counted the same way: the conjugate pair `½±iτ` contributes `2(ŵ ∗ μ_0)(τ)`, which is the `2∫ŵΨ` of the identity, i.e. weight 1 per zero at height `+τ`. The ratio of "4 orbit points against 2·(on-line at +τ)" is the factor 2. A near-double pair (δ → ½, `1/sin(πδ) → 1`) would, on the contract's reading, be dominated by a single on-line zero's worth of smoothed density; that is false, and the corrected reading fixes it. ✔

### §2.4 Consequences, checked

* **The layer constant is 4, not 2.** `2/sin(πδ) ≤ ℓ/2π ⟹ sin(πδ) ≥ 4π/ℓ ⟹ δ ≳ 4/ℓ`. ✔ (On the contract's reading one gets `2/ℓ`.) The killer's *shape* `C/log t` is untouched. ✔
* **The theorem is vacuous where Ψ(t) < 2.** True by inspection of (D) at `s = t`, since `2/sin(πδ) ≥ 2` for every δ. ✔
* **The pricing's edge table is superseded.** The re-run of `confinement_edge.py` prints, in its "literal-on-window" column at t = 10⁶, `0.1539, 0.1785, 0.1698, 0.2108, 0.1666, 0.1639, 0.2318` against PRICING-next-unit §1.1(c)'s `0.154, 0.179, 0.170, 0.211, 0.167, 0.164, 0.232` — **digit for digit**. The two computations of Ψ therefore agree and the entire disagreement is the factor 2 plus the missing `s ≈ −t` check. ✔ The corrected edges are `δ*·ℓ = 4.55, 5.73` at 10⁶ (only two of seven heights admit any δ at all), `4.23, 3.87, 5.99, 6.24, 4.56` at 10⁷ and `5.12, 4.21, 4.21, 6.69, 5.15, 4.14` at 10⁸ — Table E of §7 reproduces the log exactly.
* **The first non-vacuous heights.** `Ψ(t) > 2` on mean density needs `ℓ/2π > 2`, i.e. `t > 2πe^{4π} ≈ 1.8·10⁶`. ✔ The measured window minima are 1.08 (10⁶), 1.35 (10⁷), 1.78 (10⁸), so the *window-minimum* form of clause 3(i) is still silent at 10⁸ — the note says this and I confirm it.

**VERDICT D1: UPHELD (substantive; the record must be corrected — §12).** **VERDICT clause 2: CLOSES** with the corrected hypothesis (D).

---

## §3 Clause 3 — the localization arithmetic, and Theorem G

### §3.1 The four ranges

`ε₃(δ) := 4.03 sin(πδ) e^{−4π}`, so `ε̄₃ = 4.03·3.4873·10⁻⁶ = 1.4054·10⁻⁵`. ✔ Each range was re-derived:

* **(A) `|s − t| ≤ 4`, `t ≥ 28`.** Then `s ≥ 24` and `t + s ≥ 2t − 4 ≥ 52`. `2μ_y(t−s) ≤ 2μ_y(0) = 2/sin(πδ)` (Lemma P(ii)); `2μ_y(t+s) ≤ 2c_P sin(πδ)e^{−52π} ≪ ε₃(δ)`. So LHS ≤ `2/sin(πδ) + ε₃(δ) ≤ min Ψ ≤ Ψ(s)` by (i). ✔
* **(B) `s ≥ t + 4`.** `|t−s| ≥ 4`, `t+s ≥ 60`; LHS ≤ `2c_P sin(πδ)e^{−4π}(1 + e^{−56π}) = 4.024 sin(πδ)e^{−4π}(1+…) < 4.03 sin(πδ)e^{−4π} = ε₃(δ) ≤ Ψ(s)`. ✔ (`4.024·(1+10⁻⁷⁶) < 4.03` — the slack in `c_P` is what buys this.)
* **(C) `γ₁ ≤ s ≤ t − 4`.** `t−s ≥ 4`, `t+s ≥ 42`; LHS ≤ `4.024 sin(πδ)e^{−4π}(1 + e^{−2πγ₁}) < ε₃(δ) ≤ Ψ(s)`. ✔ The note's D4 correction is right and necessary: the contract's "automatic below t − 4 from γ₁" is false, because `Ψ(s) ≥ e^{−π|s−γ₁|}` is useless for `s` far above `γ₁` — the gap condition is what supplies `Ψ(s) ≥ ε₃` there. Good catch by the author.
* **(D) `0 ≤ s ≤ γ₁`.** `t−s ≥ 13.86`, `t+s ≥ t−s`, so LHS ≤ `4c_P sin(πδ)e^{−π(t−s)} ≤ 8.05 e^{−π(t−s)}`; `Ψ(s) ≥ 1/cosh(π(γ₁−s)) ≥ e^{−π(γ₁−s)}`; the inequality holds iff `e^{π(t−γ₁)} ≥ 8.05`, i.e. `t ≥ γ₁ + log(8.05)/π = 14.7986`. ✔ `t ≥ 28` covers it with room.

The four ranges cover `s ≥ 0` without a gap (needs `t − 4 ≥ γ₁`, i.e. `t ≥ 18.14`; `t ≥ 28` ✔), and `Ψ(−s) ≥ 0` lifts the one-sided form to (D). ✔ **The hypothesis actually used is exactly (i) + (ii); nothing else about the zeros enters.** ✔

**Gap condition, stated correctly.** Under (ii), every `s ≥ γ₁` is within `G/2` of an ordinate (it lies between two consecutive ones), so `Ψ(s) ≥ 1/cosh(πG/2)`. The note's D4 flags that the contract mixed "within distance G" with "1/cosh(πG/2)"; the note's version is the one the proof uses. ✔ Recomputed: `1/cosh(7.5π/2) = 1.5297·10⁻⁵ > ε̄₃ = 1.4054·10⁻⁵` (9 % margin) and the break-even gap is `G_max = 7.5540`. ✔

### §3.2 Theorem G — sources read at the page

I extracted the text layer of both PDFs and read the cited statements myself.

* **Trudgian, arXiv:1208.5846v2, (2.5)** (p. 3, at the page): "when T ≥ 1, `|N(T) − (T/2π)log(T/2πe) − 7/8| ≤ (1/4π)tan⁻¹(1/2T) + (1/4π)log(1 + T/4T²) + 1/3πT + |S(T)| ≤ 0.2/T + |S(T)|`". ✔ Quoted correctly.
* **Trudgian (1.2)** (p. 2): "`|S(T)| ≤ 1`, for `0 ≤ T ≤ 280`, `|S(T)| ≤ 2`, for `0 ≤ T ≤ 6.8·10⁶`", with footnote 1 "(1.2) is the statement that Gram's Law holds for all 0 ≤ T ≤ 280 and that Rosser's Rule holds for all 0 ≤ T ≤ 6.8·10⁶". ✔ Quoted correctly, footnote included.
* **Trudgian Theorem 1** (p. 2): `|S(T)| ≤ 0.111 log T + 0.275 log log T + 2.450` for `T ≥ e`. ✔ D6's record of the arXiv-v2 constants is right, and nothing in the note uses them.
* **HSW, arXiv:2107.06506v1, Corollary 1.2 = (1.5)** (p. 2): "For any `T ≥ e`, `|N(T) − (T/2π)log(T/2πe)| ≤ 0.1038 log T + 0.2573 log log T + 9.3675`". ✔ **No 1/8 in (1.5).**
* **HSW Theorem 1.1 (1.4)** (p. 2): bounds `|N(T) − (T/2π)log(T/2πe) + 1/8|` by the same shape. ✔ So the two expressions genuinely differ by the shift 1/8 — this is **not** a misprint but the difference between the general theorem and its specialization, and the note's remark (3) ("a precaution against a possible misprint") mis-diagnoses a real and deliberate difference. Harmless; §12 item 6.
* **HSW (1.7)** (p. 2): `|S(T)| ≤ 2.5167` for `0 ≤ T ≤ 30 610 046 000`. ✔
* **HSW (5.6)** (p. 15): "`|N(T) − (T/2π)log(T/2πe) + 1/8| ≤ |S(T)| + ½|g(T)| + 1 ≤ 2.5167 + 1/(50e) + 1`, for `e ≤ T ≤ 30 610 046 000`". ✔ Value `3.5241`.
* **HSW Corollary 1.4** (p. 2): `|S(T)| ≤ min{0.1038 log T + 0.2573 log log T + 8.3675, 0.1095 log T + 0.2042 log log T + 3.0305}` for `T ≥ e`. ✔ The note uses the second member. ✔

**The "+1/8" question, settled.** Every use of these bounds in the note is a **difference** `N(T+G) − N(T)`, and an additive constant inside the absolute value cancels there: if `|N − main + c| ≤ E` then `N(x) − main(x) ∈ [−E − c, E − c]`, so `(N − main)(T+G) − (N − main)(T) ≥ −2E` regardless of `c`. Consequently:
* using `3.5241` for HSW (5.6) **without** adding 1/8 is correct, not an oversight (script range (a));
* adding `1/8` to `E` for Corollary 1.2 (script range (b)) is unnecessary but strictly conservative — it moves the threshold from `8.45·10⁹` (my computation, no 1/8) to `1.096·10¹⁰` (the note's). Both are far inside the range that (5.6) covers.
The asymmetric treatment between ranges (a) and (b) is therefore not an inconsistency of correctness. The note's `E(T) := … + 9.4925` is sound.

### §3.3 The thresholds, recomputed independently

My own code (no reuse of the author's), using `M(T+7.5) − M(T) ≥ (7.5/2π)log(T/2π)`:

```
  (a) HSW (5.6),  swing 2*3.5241                    -> T >= 2304.2   (valid to 3.061e10)
  (b) HSW Cor 1.2, E(T)+E(T+7.5), no +1/8           -> T >= 8.4525e+09
      with the note's +1/8 precaution, 2E(T+7.5)    -> T >= 1.0956e+10
  (c) TRU (2.5)+(1.2), |S| <= 1 (T <= 280)          -> T >= 33.87    (valid to 272.5)
      TRU (2.5)+(1.2), |S| <= 2 (T <= 6.8e6)        -> T >= 179.60   (valid to 6.8e6)
  (d) HSW Cor 1.4 (2nd bound) + TRU (2.5)           -> T >= 1.2195e+04
```

against the note's `2304.2 / 1.096·10¹⁰ / 33.90 / 179.61 / 1.220·10⁴`. ✔ (My 33.87 vs the note's 33.90 is because I used `0.2/T + 0.2/(T+7.5)` where the note used the more conservative `2·(0.2/T)`; the note's is the safe side.) Re-running `clause5_constants.py` reproduces its log **line for line**.

### §3.4 The computational range

`gaps_first_zeros.py` re-run: `computed gamma_1..gamma_1900 in 309s; gamma_1900 = 2409.8816`, `max gap = 6.8873 at n = 1; all gaps <= 7.5: True; all gaps <= 6.9: True` — **identical to the stored log** (311 s there). Knowing `γ₁ … γ₁₉₀₀` with all gaps ≤ 6.8873 certifies that `(T, T+7.5]` contains an ordinate for every `T ∈ [γ₁, γ₁₉₀₀) = [14.13, 2409.88)`. ✔

### §3.5 Coverage

Both chains close, with overlap and no gap:
* **Trudgian chain:** `[γ₁, 37.59)` (the six computed ordinates) ∪ `[33.90, 6.8·10⁶ − 7.5]` (Trudgian (2.5)+(1.2)) ∪ `[1.220·10⁴, ∞)` (Cor 1.4 + (2.5)). ✔
* **HSW-only chain:** `[γ₁, 2409.88)` (the 1900 zeros) ∪ `[2304.2, 3.061·10¹⁰ − 7.5]` ((5.6)) ∪ `[1.096·10¹⁰, ∞)` (Cor 1.2). ✔

Either chain proves Theorem G. The note's two label systems in the same paragraph — the prose labels (a) Trudgian / (b) HSW / (c) small zeros, and the log keys (a) (5.6) / (b) Cor 1.2 / (c) Trudgian / (d) Cor 1.4 — are traceable but collide; §12 item 7.

**VERDICT clause 3 (and Theorem G): CLOSES.** Theorem G is genuinely new to the record here and is the discharge of clause 3(ii) for ζ at every height, as claimed; it is elementary given the two sources, and the note says so.

---

## §4 Clause 4 — the hypothesis, and the layer constant 4

**Lemma L re-derived.** For `δ ∈ [δ_M, ½]` with `δ_M := (1/π)arcsin(2/(M − ε̄₃))`, `πδ` lies in `[arcsin(2/(M−ε̄₃)), π/2]` where `sin` is increasing, so `sin(πδ) ≥ 2/(M − ε̄₃)`, i.e. `2/sin(πδ) + ε₃(δ) ≤ M ≤ min Ψ`. That is clause 3(i) exactly. ✔ The requirement `M > 2 + ε̄₃` is what makes the `arcsin` argument < 1, and it is stated. ✔ `arcsin x ≤ x/√(1−x²)` ✔.

**Clause 4's hypothesis is exactly what the proof uses.** The proof is Lemma L at `M = (1−ε)ℓ/2π`, plus `arcsin x = x + O(x³)`. The only input is the **lower bound on the window minimum of Ψ over `|s − t| ≤ 4`** — no other property of the zeros. The note states this explicitly ("*Exact hypothesis:* the lower bound on the window minimum of Ψ; nothing else about the zeros is used"), and I confirm there is no hidden second hypothesis. ✔ Theorem G supplies clause 3(ii) silently, and that is flagged.

**The constant 4, checked.** `2/sin(πδ) ≤ ℓ/2π` gives `sin(πδ) ≥ 4π/ℓ`, hence `δ ≳ 4/ℓ`, i.e. `δ₄ = (4/ℓ)(1 + ε + O(ε²) + O(ℓ⁻²))`. ✔ The contract's `2/ℓ` came from `1/sin(πδ) ≤ ℓ/2π`; the factor 2 in the hypothesis passes straight through to the layer constant, one for one. ✔ The refined non-asymptotic form `δ₄ ≤ (4/((1−ε)ℓ − 2πε̄₃))·(1 − (4π/((1−ε)ℓ − 2πε̄₃))²)^{−1/2}` is `arcsin x ≤ x/√(1−x²)` with `x = 2/((1−ε)ℓ/2π − ε̄₃) = 4π/((1−ε)ℓ − 2πε̄₃)` ✔.

**The "where the hypothesis comes from" paragraph.** `Ψ(s) = ∫μ_0(s−x)dN(x)`; integrating by parts against `N = M + R` and using `∫|μ_0′| = 2μ_0(0) = 2` gives `ε = O(sup|R|/ℓ)` over a window. ✔ Correct as an indication; it is labeled as such ("Where the hypothesis comes from"), it is not used in the proof, and Littlewood's RH-conditional `S(t) = O(log t/log log t)` is carried as `[recalled, unverified]` with a Titchmarsh pointer and marked not load-bearing. ✔ Under standing order 5 that is the right handling: clause 4 is proved under its stated hypothesis, and the RH sentence is a reading, not a step.

The note's own observation that the unconditional `E ≍ 0.1038 log x` is **not** `o(ℓ)` — so the mean-value route cannot be made explicit from these sources, and clause 5 must go through a window count instead — is correct and is what makes clause 5's structure forced.

**VERDICT clause 4: CLOSES** (conditional form, as the contract asks; hypothesis exactly as used; constant 4).

---

## §5 Clause 5 — the unconditional constant, recomputed

**The window-count bound.** For `s ∈ [t−4, t+4]`: `Ψ(s) ≥ [N(s+H) − N(s−H)]/cosh(πH)`, because every ordinate in `(s−H, s+H]` contributes at least `1/cosh(πH)`. ✔ Then `N(s+H) − N(s−H) ≥ ∫_{s−H}^{s+H}(1/2π)log(x/2π)dx − E(s−H) − E(s+H) ≥ (H/π)log((t−4−H)/2π) − 2E(t+4+H)` (E increasing, and `2H·(1/2π)log((s−H)/2π) = (H/π)log(…)`). ✔ That is `Ψ₅(t,H)`. ✔ The `+1/8` inside `E` is the conservative precaution discussed in §3.2 and cancels anyway. ✔

**The asymptotic constant, recomputed from scratch** (2·10⁶-point grid, plus a stationarity check):

```
  H* = 0.971926   m* = 0.00958575   C_uncond = 2/(pi m*) = 66.4131
  stationarity residual of  1/pi^2 = (H/pi - 0.2076) tanh(pi H) :  -2.07e-08
```

against the note's `H* = 0.9719`, `m* = 0.009586`, `C_uncond = 66.41`. ✔ The derivation is right: `Ψ₅ ~ m(H)·log t` with `m(H) = (H/π − 2·0.1038)/cosh(πH)`, and `δ ~ (1/π)·2/(m* log t) = 2/(π m*)/log t`. The requirement `H > 2πc₁ = 0.652` for the window count to be positive is correct, as is the price `cosh(πH*) = 10.62` at the optimum.

**The threshold, recomputed:** `log t₀ = 377.36` (mine) against the note's `377.4`. ✔ Independent spot-check at `log t = 377.4, H = 1.159`: numerator `(1.159/π)(377.4 − log 2π) − 2E = 138.55 − 100.39 = 38.16`, `cosh(π·1.159) = 19.08`, `Ψ₅ = 2.000`. ✔ My `δ₅·log t` table `146.43 / 113.47 / 84.38 / 71.84 / 68.02 / 66.58` at `log t = 400 / 500 / 1000 / 3000 / 10⁴ / 10⁵` reproduces the note's `146.4 / 113.5 / 84.4 / 71.8 / 68.0 / 66.6` to the printed digit. ✔ Re-running `clause5_constants.py` reproduces its log line for line.

**The contract's arithmetic, and why it was wrong twice.** The contract took `H = 4πc₁ = 1.3044`, which gives `m = 0.006894` and `C ≈ 92.3` — not optimal; and it used `1/sin(πδ)` instead of `2/sin(πδ)`, which would have halved the constant. The two errors point in opposite directions, which is why the contract's `[recalled, unverified]` "order 50–70" happened to bracket the honest 66.41. The note says this; it is worth keeping in the record, because it means the contract's number was right by cancellation, not by derivation.

**Status of clause 5 (deferred vs read-at-the-page).** The brief allowed clause 5 to be deferred if the sources could not be read in session. They were read — I re-read them independently at the page, and the PDF hashes match D6 — so clause 5 lands **proved**, not deferred. ✔

**VERDICT clause 5: CLOSES** (`C_uncond = 66.41`, `H* = 0.972`, non-vacuous from `t ≥ e^{377}`; the constant is honest and weak, and the note says so).

---

## §6 Clause 6 — the parameter pin

`|4∫_{|u|>L′} p(u)q(tu)k_y(u)cos(tu)du| ≤ 4·p(0)‖q‖_∞·∫_{|u|>L′}2e^{−δ|u|}du = 4·p(0)‖q‖_∞·(4e^{−δL′}/δ) = 16 p(0)‖q‖_∞ e^{−δL′}/δ`. ✔ The three ingredients are `0 ≤ p(u) ≤ p(0)` (from `p ≥ 0`, `p̂ ≥ 0 ∈ L¹`, §0.1 — correct), `|q(tu)| ≤ ‖q‖_∞`, and Lemma P(iv) `k_y ≤ 2e^{−δ|u|}`. ✔ `ŵ ≥ 0` for `w = p(u)q(tu)` with `q_k ≥ 0` is the shifted-transform computation, correct with the `k = 0` term counted once. ✔

**The constant is 16, not 8, and the note's D5 explanation is right.** The contract's `8` is what one gets for `2 Re ĝ` — the two orbit points at height `+t` — rather than the full four-point orbit `4 Re ĝ`; and the contract named no norm. This is the *same* factor 2 as D1, arriving from the u-side. Consistency check: it must be, and it is. ✔ The reading (10(h)) is correct: the pin is a statement about the **orbit share only**; `B(w)` is not pinned, and the note says so.

**VERDICT clause 6: CLOSES** (constant 16 with the sup norm; D5 recorded).

---

## §7 Clause 7 — Lemma E, and the constant c

### §7.1 The element and its transforms

`q(θ) = 3 + 4cos θ + cos 2θ = 2(1+cos θ)² ≥ 0` ✔; `c_0 = 3, c_{±1} = 2, c_{±2} = ½` with `Σ_k c_k = 8` ✔; `e^{−a|u|}cosh(u/2) = ½[e^{−(a−½)|u|} + e^{−(a+½)|u|}]` ✔; transform of `e^{−b|u|}` is `π_b` ✔. Hence `ŵ_{a,t} > 0` as a positive combination of Poisson kernels, and `ĝ_{a,t}(z) = Σ_k c_k π_a(z+kt)` for `|Im z| < a`. ✔ `w ≥ 0` needs no support restriction. ✔

**Lemma E(ii)'s uniform bound, re-derived line by line.** `a² + (x−iy)² = (a+y+ix)(a−y−ix)`; both factors have modulus ≥ `√(η²+x²)` since `a ± y ≥ a − ½ = η`; `η² + x² ≥ min(1,η²)(1+x²)` in both cases `η ≥ 1` and `η < 1`; `|z| ≤ |x| + 2t + ½` so `1+|z|² ≤ 1.5 + 2x² + 8t² + 4t ≤ (2+12t²)(1+x²)` whenever `0.5 + 4t² − 4t ≥ 0`, true for `t ≥ 0.854` and so for `t ≥ 1`. Multiplying by `Σc_k = 8` gives `|ĝ(z)| ≤ 16a(2+12t²)/(min(1,η²)(1+|z|²))`. ✔ Every step checks.

### §7.2 Lemma E(iii) — membership in Σ_∞ by approximation

The mollify-and-cut construction `g_{n,ε} := (g ∗ φ_ε)·χ_n` lands in `C²_c`, so the formal input applies to it — and, importantly, the approximants are **not** required to be in the cone, only in `C²_c`; the cone inequalities are checked on the limit `w_{a,t}` itself. ✔ That is the right architecture.

The two quantitative claims are correct:
* `|φ̂(εz)| ≤ e^{1/2}` on `|Im z| ≤ ½` for `ε ≤ 1`, `supp φ ⊂ [−1,1]`, `∫φ = 1`. ✔
* the convolution claim `(1/2π)∫F(x−ξ)|χ̂_n(ξ)|dξ ≤ 6C₂C₅/(1+x²)` uniformly in `n ≥ 1`: I re-did the three cases. `|x| < 1`: `≤ (1/2π)C₅·πC₂ = C₂C₅/2 ≤ C₂C₅/(1+x²)` ✔. `|x| ≥ 1, |ξ| ≤ |x|/2`: `F(x−ξ) ≤ C₅/(1+x²/4) ≤ 4C₅/(1+x²)`, contributing `2C₂C₅/(1+x²)` ✔. `|ξ| > |x|/2`: `|χ̂_n(ξ)| ≤ nC₂/(1+n²x²/4) ≤ 4C₂/(nx²) ≤ 8C₂/(1+x²)`, contributing `4C₂C₅/(1+x²)` ✔. Total ≤ `6C₂C₅/(1+x²)` ✔.
Summability of the dominating family then follows from the formal local count `N(k,k+1] ≤ 5.4·10⁸ log(k+3)` against `(1+k²)^{−1}` ✔, and dominated convergence transfers the identity to the limit. The pole, prime and archimedean terms each carry their own explicit dominating function; the prime term's `2‖q‖_∞e^{εa}Λ(n)n^{−½−a}` is summable exactly because `a > ½` ✔. **Lemma E is sound.** The double limit (`ε → 0`, then `n → ∞`) is taken in a legitimate order and each stage is dominated.

**Lemmas A and D, re-derived and re-checked numerically.** Lemma A's exchange of integrals is Tonelli on a nonnegative integrand after subtracting `ψ(¼)` — correct — and `(1/2π)∫π_a(r−x)cos(rτ/2)dr = e^{−aτ/2}cos(xτ/2)` is the Poisson-kernel transform. My own quadrature, written independently:

```
  a=0.6, x=0.0   : LHS -2.8806891365   RHS -2.8806891365   diff 0.0e+00
  a=0.6, x=30.0  : LHS  1.5631404592   RHS  1.5631405474   diff 8.8e-08
  a=1.0, x=100.0 : LHS  2.7673578786   RHS  2.7672889528   diff 6.9e-05
  a=1.5, x=0.0   : LHS -1.7219455508   RHS -1.7219455508   diff 0.0e+00
```

(the residuals at large `x` are my own quadrature's, not the identity's; the author's `kernel_lemmas.py` does the same check at higher precision and gets `10⁻²⁰`). Lemma D's integration by parts is correct: `h(τ) = 1/(1−e^{−τ}) − 1/τ` has `h(0⁺) = ½`, `h(∞) = 1`, `h′ ≥ 0` (from `sinh(τ/2) ≥ τ/2`), `∫h′ = ½`, so `∫|G′| ≤ ½ + x·(1/x) = 3/2` and `|Re ψ(z) − log|z|| ≤ 3/(2|Im z|)`. ✔ The numerical record confirms the ratio never exceeds 0.168.

### §7.3 The certified constant

Orbit share, keeping only `k = −1` (`x = 0`, `c_{−1} = 2`): `4Re ĝ(t−iy) ≥ 8[1/(a+y) + 1/(a−y)] ≥ 8/(a−y) = 8/(σ−β) = 8/(η+δ)`. ✔ All other terms are positive (`Re π_a(x−iy) > 0`). ✔

Budget: `b_0 ≤ 2/η + 2 + ψ(1) − log π = 2/η + 0.2780544` (uses `σ ≤ 2`, `ψ` increasing) ✔; `b_j ≤ log(jt/2π) + 3/(jt) + 8/(j²t²)` for `j = 1, 2` ✔ (each of the three sub-bounds re-derived). Summing with `d = (3,4,1)`: `B ≤ 6/η + 5ℓ + 0.8343 + log 2 + 13.5/t + 34/t² = 6/η + 5ℓ + C_t`, `C_t = 1.5274 + 13.5/t + 34/t²` ✔.

Optimization, re-derived in closed form. With `X := 6 + ηM`, `f(η) = 8η/(6+ηM) − η = (1/M)[14 − X − 48/X]`, maximized at `X = 4√3`, value `(14 − 8√3)/M`. Recomputed:

```
  14 - 8*sqrt(3)                 = 0.14359354
  (2/sqrt3 - 1)(4 sqrt3 - 6)     = 0.14359354      (the note's form: identical)
  /5                             = 0.02871871      1/that = 34.8205
  eta* numerator 4 sqrt3 - 6     = 0.928203
  2 + psi(1) - log pi            = 0.278054        3*that + log 2 = 1.527311 <= 1.5274
```

**`c = (2/√3 − 1)(4√3 − 6)/5 = 0.0287187 = 1/34.8205` is confirmed**, and the two algebraic forms agree exactly. The final step `5ℓ + C_t ≤ 5log t − 9.189 + 1.5274 + 0.4821 + 0.0434 < 5 log t` for `t ≥ 28` ✔, so `1 − β > 1/(34.8205 log t)`. The constraint `η* ≤ 1` holds since `M ≥ 5log(28/2π) + 1.5274 = 9.00 > 0.928` ✔.

**Numerical confirmation, independent.** My own exact evaluation of `B(w_{a,t}) = Σ_j d_j[2Re(1/(s_j−1) + 1/s_j) + Re ψ(s_j/2) − log π]` at `η = η*` gives `66.55 ≤ 71.09` (t = 28), `111.50 ≤ 115.71` (10²), `282.43 ≤ 286.55` (10⁴), `454.27 ≤ 458.41` (10⁶) — the bound holds at every height with a slack of 3–5. (The author's `dlvp_constant.py`, re-run, prints `457.717 ≤ 461.855` at 10⁶; the 3.4 offset from mine is a slightly different `η` in the two evaluations, not a disagreement — both confirm `B_exact ≤ bound`.) The element's exact reach `δ_max·log t = 0.0653, 0.0499, 0.0402, 0.0347, 0.0314` at `t = 10³ … 10²⁰` decreases toward the certified `c = 0.0287`, as it must. ✔

**The two-sided band is real.** At any height where the theorem applies, the cone's reach contains `{1−σ < 0.0287/log t}` and is contained in `{1−σ < (4+o(1))/log t}` (mean density) or `{1−σ < (66.41+o(1))/log t}` (unconditional, `t ≥ e^{377}`) — a band of ratio ≈ 139 conditionally, ≈ 2313 unconditionally. The note states the band honestly and does not claim it is tight.

**VERDICT clause 7: CLOSES.** Lemma E's membership argument is correct; `c` is correct.

---

## §8 Prior art and the standing-order-7 novelty check (§8.3 of the note)

The brief assigns the corpus re-read to Job 2. It was done here, from the files themselves.

### §8.1 The program's own corpus

* **Zoo III.9** (`BARRIER-ZOO.md` lines 218–224, read): the quoted sentences are verbatim — "The 3-4-1 inequality is Fejér-square positivity — the identical 1899 generator behind classical zero-free regions, edge-capped for 125 years", and the Granville–Soundararajan floor "all zero-location content from D-data is confined to the classical de la Vallée Poussin edge". ✔ **This is the program's own prior statement of the same phenomenon, and it is prior art in spirit.** The distinction the note draws is the right one and survives scrutiny: III.9's floor is about a *different data class* — D-metric-continuous functionals of multiplicative functions, `sweep-certified` from a book exercise — whereas R1 is about the strip-positive cone over the first-order explicit formula, is unconditional, and carries explicit constants. Neither implies the other. The note's framing ("the program's own prior statement of the confinement at the pretentious level") is accurate and appropriately modest.
* **Zoo III.2** (lines 162–168, read): "small cones prove nothing" — Bombieri small-support. ✔ The complementary bracket, as the note says: III.2 caps *small* cones unconditionally; R1 caps *all* cones at every bandwidth. Correctly cited.
* **Zoo IV.1** (lines 326–332, read): the "Weil positivity in disguise" containment audit. R1's observable *is* a Weil test times the multiplier `1/cosh(u/2)`, so IV.1 HITS. The note's evasion clause is written and is the honest one: no new data coordinate is claimed; the theorem is a statement about the *sign of a measure* inside the already-contained data class. ✔ This is exactly IV.1's own executable-test outcome ("its 'generator' must then be audited as a cone-restriction"), and R1 is that audit's conclusion, so IV.1 is not evaded but confirmed.
* **Zoo IV.7** (line 385, the 2026-09-10 Opus read; the note cites "line 386", off by one — §12 item 8). The finding attributed to it is a *periodic-configuration* statement, and the inference the note draws from it about the Carneiro-school corpus is labeled as an inference of the pricing's, not a reading. That labeling is correct, and it is superseded by §8.2 below, which is a first-hand read.

### §8.2 The four corpus files, re-read here (this is the standing-order-7 item Job 1 could not close)

Text layers extracted and searched; all four have clean text layers.

* **`fetched/w-14-carneiro-chandee-chirre-milinovich-2022-tale-of-three-integrals-crelle786.pdf`** — extremal problems (EP1)–(EP3) for three integrals attached to `ζ` on the critical line, RH-conditional. It *does* contain method-ceiling statements — §2.1.3 "Strengths and limitations", and (2.22) `Σ_j (2g_j(0) − ρ(g_j)) ≤ (2 − C_MT)ℓ = (0.67250…)ℓ`, described in the text as "universal limitations of this method when using the extremal problems (EP1) and (EP2) restricted to the subclass A₀". **This is the closest genuine antecedent in shape anywhere in the corpus: an explicit universal ceiling on a Fourier-optimization method.** It is not the statement of R1: the quantity is a pair-correlation/mollification functional under RH, not a zero-free-region certificate, and the ceiling is on a restricted subclass `A₀`, not on the whole cone at every bandwidth. Recorded so the record is honest about it.
* **`fetched/w-15-…-hilbert-spaces-pair-correlation-crelle725.pdf`** — upper and lower bounds for `N(T, β)` under RH via Montgomery's formula and reproducing-kernel Hilbert spaces. One "cannot" sentence, about the gap between its own `U(β)` and `L(β)`. No confinement statement about zero-free-region certificates.
* **`fetched/y-25-carneiro-milinovich-2025-…-montgomery-pair-correlation.pdf`** (= CMR arXiv:2310.01913) — Fourier optimization for the average of `F(α,T)` under RH, using the Cohn–Elkies class beyond bandlimited functions. Same class as C2's cone at the level of *tools*; the object is pair correlation, not a first-order zero-free region. No antecedent.
* **`fetched-r2/r-25a-goldfeld-hoffstein-lieman-1994-…annals140.pdf`** — a five-page appendix eliminating Siegel zeros for the adjoint-square lift `L(s, F)` by the classical positivity method. A *region*, not a limit theorem. ✔ The note's one-line description is accurate.

**Finding.** No statement of the form "no strip-positive certificate at any bandwidth can exclude a zero at `(t, ½−δ)` once the local on-line density dominates the pair's depth weight" appears in any of the four, nor in III.2/III.9, nor in the pricing's network check (Mossinghoff–Trudgian 1410.3926, MTY 2212.06867, Kadiri), nor — see §8.3 — in the two fetched S(t) papers.

### §8.3 The two fetched papers' own abstracts (the fetch-row half of the standing-order-7 check)

* **Trudgian, arXiv:1208.5846v2**, abstract, read at the page: "This paper concerns the function `S(T)`, the argument of the Riemann zeta-function along the critical line. The main result is that `|S(T)| ≤ 0.111 log T + 0.275 log log T + 2.450`, which holds for all `T ≥ e`."
* **Hasanalizade–Shen–Wong, arXiv:2107.06506v1**, abstract, read at the page: "we show that `|N(T) − (T/2π)log(T/2πe)| ≤ 0.1038 log T + 0.2573 log log T + 9.3675` … This improves the previous result of Trudgian for sufficiently large T. The improvement comes from the use of various subconvexity bounds and ideas from the work of Bennett et al. on counting zeros of Dirichlet L-functions."

Both are explicit zero-counting/argument bounds. Neither says anything about certificate classes, cones or confinement; they enter R1 purely as inputs. ✔ No prior-art collision.

### §8.4 The novelty label

The note carries `[novelty: single-check]`. **The dual check has now been run against the corpus, the zoo and the two fetch rows, and it finds no antecedent.** Under the program's own precedent (the IV.7 rider B relabeling of 2026-09-10) the label becomes **`[novelty: dual-model check 2026-09-10]`**, with the honest qualifications the note already states: the *mechanism* (Fejér cap + explicit formula + sech kernels) is classical and 125 years old (III.9); the *shape* of an explicit method-ceiling has a genuine antecedent in w-14 §2.1.3/(2.22) for a different functional; what is new is the cone-wide, unconditional, explicit statement with the bandwidth pin and the two-sided band. The two by-products — the factor 2 (D1) and Theorem G — are elementary and are labeled as such.

### §8.5 The ladder rungs

* **Rung 0 (model world).** The note refuses to claim sharpness in the strong sense and says why: R1 is one-sided (no cone certificate exists at `(t,y)` under (D); it does not construct an admissible datum realizing `(t,y)`). ✔ Correct and correctly stated; "sharp" is claimed only in clause 7's sense. The abstract-datum transfer (`Ψ_σ` in place of `Ψ`) is right — clauses 1–3 use only the identity, nonnegativity of the shares and the kernel lemmas.
* **Rung 1 (function fields).** Stated for the record, nothing proved. ✔ Honestly flagged.
* **Rung 2 (Davenport–Heilbronn / Epstein).** "Axiom P fails, so clause 1 fails, so the theorem is vacuous — for the right reason." ✔ I verified the witnesses against `results/c3-r/m0-axiom-note.md` §6.1–6.2 (lines 361–393) and re-did their arithmetic: `κ = (√(10−2√5)−2)/(√5−1) = 0.2840790438…`; `−κ log 3 = −0.3120927`; `−(2+κ²)log 2 = −1.4422320`; `−κ(1+κ²)log 12 = −0.7628775`; `Λ_Q(36) = −4 log 6 = −7.1670379`; the DH off-line zero `0.808517182456637 + 85.699348485377592i`. All match. ✔ The logic is right: a negative `Λ` makes `P(w) < 0` for a cone element concentrated at `u = log 3`, so `B ≥ Z` fails and a "cone certificate" excludes nothing — consistent with DH's actual off-line zero. This is I.1 passed in its own form.
* **Rung 3 (`ζ_K = ζ·L(χ₋₂₀)`).** Stated, not proved — the degree-2 identity is not among the note's inputs, and the note says so. ✔ The density scaling `(1/π)log(t√|D|/2π)` and the resulting layer are stated consistently with the corrected factor 2 (the pair's weight `2/sin(πδ)` against **twice** the density). ✔
* **Rung 4 (ζ).** The theorem itself. ✔

**VERDICT prior art / ladder / standing order 7: CLOSES**, with the label upgraded and the w-14 antecedent recorded.

---

## §9 "Cannot" sentences — is each a theorem in the note, or labeled?

Every occurrence of "cannot / can never / never / impossible / no … exists" in `confinement-note.md` was enumerated and traced.

| line | sentence | status |
|---|---|---|
| 5 | "the contract's clause 2 hypothesis … cannot be satisfied" | theorem (§0.4 D1; re-proved in §2 above, and unconditionally via the formal local count) |
| 65 | "The hypothesis as written is therefore never satisfied" | same |
| 114 | "It is a hypothesis …, never a Lean axiom" | a verbatim quotation of the Lean docstring, marked as such |
| 164 | "only that this class of arguments cannot exclude one" | theorem (clause 2) |
| 296 | "the mean-value route of clause 4 cannot be made explicit from these sources" | argued, and the argument is given in the same sentence (`E ≍ 0.1038 log x` is a positive fraction of `ℓ/2π`, so `ε = O(sup|R|/ℓ)` does not tend to 0). Sound; it is a statement about the sources, correctly scoped by "from these sources" |
| 341 | "no cone certificate at `(t,y)` exists when `(D_{t,y})` holds" | theorem (clause 2) |
| 341 | "its answer cannot come from finite-variation perturbations of the mean density" | the pricing's LP-duality finding. Labeled `[the pricing's finding, novelty: single-check]` at §8.5 — but **not** labeled at this occurrence in §8.1. §12 item 4 |
| 349 | "it says what the P-consuming sector cannot do" | theorem (the note as a whole) |
| 376 | the refutation-shaped close, "cannot yield a zero-free point outside …" | theorem, and the close states its exact hypothesis inline, as 10(c) requires |

**One item to fix and one to note.** The §8.1 occurrence of the budget-floor "cannot" needs the same label it carries in §8.5 (a one-word cross-reference). The `zoo-IV18-proposed.md` **KILLS** line is the one place where a "cannot"-shaped claim is stated *without* its hypothesis: "Any brief claiming that a strip-positive … certificate, at any bandwidth, yields a zero-free point outside `{1 − σ < C/log t}`". Read literally at a height where `Ψ(t) < 2` the theorem says nothing, so the screen would misfire. The STATEMENT field carries the hypothesis correctly; the KILLS field must carry the scope too. §12 item 1.

**VERDICT: CLOSES**, subject to §12 items 1 and 4 (both one-line).

---

## §10 Lint (KICKSTART 10(g)) and presentation

* **The banned hedges (10(g)).** Each of the four hedges named in 10(g) occurs **exactly once** in `confinement-note.md`, and all four occurrences sit inside line 5's own sentence declaring that they do not occur (the sentence spells them out in order to deny them). As written that sentence is self-refuting, and a mechanical grep of the note returns four hits. Nothing mathematical turns on it — the note's proofs hedge nowhere — but the note should not trip its own check. **FIX-FIRST (cosmetic).** `zoo-IV18-proposed.md` is clean (zero hits). *(This report states the four hedges only by reference, for the same reason.)* A grep of `verify/sources-read-excerpts.txt` also returns one hit, inside a verbatim quotation of HSW's own sentence about (5.6); a quotation keeps its source's wording, so that is not a lint violation and needs no change.
* **U.S. English.** Checked; the note is consistent (`normalization`, `behavior`, `labeled`, `center`). One British form survives in a quotation context in `§8.3`/`§9.2` (`"specialised"`), which is a verbatim quotation of the Lean docstring and correctly left alone.
* **Section order.** The note prints `§0, §1, §2, §4, §5, §3, §6, §7, §8, §9`. Every internal reference resolves and no proof depends on a later section, but a reader following the clause order will jump. Cosmetic; §12 item 9.
* **Cross-references.** Two point to `§8.4` (the zoo protocol) where `§8.5` (the open problem) is meant: line 317 ("the primal upper bound κ ≤ 0.136 of §8.4") and line 341 ("the budget-floor computation (§8.4: I₋ = 2.2415 > 2)"). §12 item 3.
* **Namespace.** The Lean theorems are `Zeta23.WeilEF.EF_lit_zetaZeroConfig` and `Zeta23.WeilEF.zeta_local_zero_count_explicit`; the note names them without the `WeilEF` component in prose. Harmless; recorded so the `#print axioms` line can be quoted correctly.

**VERDICT: FIX-FIRST on the lint sentence; everything else cosmetic.**

---

## §11 Verdict table

| item | object | verdict |
|---|---|---|
| Clause 1 | identity in cone form; `EF_lit_zetaZeroConfig` at `g = w/cosh(u/2) ∈ C²_c`; `P = Λ ≥ 0` | **CLOSES** |
| Clause 2 | domination, with the corrected hypothesis (D) | **CLOSES** |
| **D1** | the contract's hypothesis is unsatisfiable; (D) is what the proof needs; local content `2/sin(πδ) ≤ Ψ(t)`; layer constant 4 | **UPHELD** (substantive deviation; the record must be corrected) |
| Clause 3 | localization in four ranges; `ε₃(δ) = 4.03 sin(πδ)e^{−4π}`; gap condition | **CLOSES** |
| Theorem G | all consecutive ordinate gaps ≤ 7.5, unconditionally, at every height | **CLOSES** (both source chains verified at the page; 1900-zero run reproduced) |
| Clause 4 | conditional layer corollary; hypothesis = window minimum of Ψ only; constant **4** | **CLOSES** |
| Clause 5 | unconditional layer corollary; `C_uncond = 66.41`, `H* = 0.9719`, `m* = 0.009586`, `log t₀ = 377.4` | **CLOSES** (sources read at the page; not deferred) |
| Clause 6 | parameter pin, constant **16** with the sup norm | **CLOSES** |
| Clause 7 | Lemma E (`w_{a,t} ∈ Σ_∞` by mollification and cutoff from the formal input); `c = (2/√3−1)(4√3−6)/5 = 0.0287187 = 1/34.8205` | **CLOSES** |
| Lemmas P, K, A, D | closed form, mass, peak, tails; orbit share; Poisson evaluation; digamma bound | **CLOSES** |
| Numerics | six scripts re-run; all six logs reproduced line for line; 22/22 SHA-256 verify | **CLOSES** |
| 10(f) | `#print axioms` for the two formal inputs | **CLOSES** (run here: `[propext, Classical.choice, Quot.sound]` for both) |
| Prior art / standing order 7 | corpus (III.2, III.9, IV.1, w-14, w-15, y-25, r-25a) + the two arXiv abstracts | **CLOSES**; label → `[novelty: dual-model check 2026-09-10]` |
| Ladder rungs 0–4 | including the DH/Epstein witnesses | **CLOSES** |
| "cannot" sentences | each a theorem or labeled | **CLOSES** subject to §12 items 1 and 4 |
| 10(g) lint | the note's own lint sentence contains all four banned words | **FIX-FIRST** (cosmetic) |

**Overall: the note CLOSES.** No clause FAILS. Nothing found in this check changes a constant, a hypothesis or a proof; the corrections below are wording, scope and cross-reference.

---

## §12 The exact wording corrections the record needs

D1 stands, so the corrections it forces are mandatory. Job 2 does not edit these files; the orchestrator does.

**1. `results/c2-r1/zoo-IV18-proposed.md`, KILLS field — the one substantive amendment (do this before insertion).** The screen must carry the theorem's scope. Replace

> **KILLS.** Any brief claiming that a strip-positive (cone / positivity-class / de la Vallée Poussin–Landau–Heath-Brown-type) first-order certificate, at any bandwidth, yields a zero-free point outside {1 − σ < C/log t} …

with

> **KILLS.** Any brief claiming that a strip-positive (cone / positivity-class / de la Vallée Poussin–Landau–Heath-Brown-type) first-order certificate, at any bandwidth, yields a zero-free point at a height and depth where the theorem's density hypothesis holds — i.e. wherever `2/sin(πδ) + ε₃(δ) ≤ min_{|s−t|≤4} Ψ(s)`, which is `1 − σ ≳ 4/log t` at mean density (clause 4; under RH at every large height) and `1 − σ ≳ 66.41/log t` unconditionally for `t ≥ e^{377}` (clause 5) — in particular C2's original numerics deliverable "V > 1 outside the classical region" (C2 line 70, the killer's major) …

with the rest of the field unchanged. Reason: at heights where `Ψ(t) < 2` the theorem is silent (most points below `t ≈ 1.8·10⁶`), and the STATEMENT field says so; the KILLS field as drafted does not, and it is the field a brief-time screen actually reads.

**2. `results/c2-m5/PRICING-next-unit.md`.**
* **§1.1(c)** — the "exact layer edge" paragraph and its table (`δ*(t′)·ℓ` between 1.84 and 2.78 at `t = 10⁶`, "the mean-density prediction 2/ℓ", "the layer's constant at a given height is `2·(ℓ/2π)/Ψ(t)`") is **superseded**. The numbers themselves are correct as the *literal-on-window* quantity — they are reproduced digit for digit in `confinement-note.md` §7 Table E's last column — but they are not the layer edge. Add a dated line: *"2026-09-10, corrected by `results/c2-r1/confinement-note.md` §0.4 D1 and §7 Table E: this column is the literal-on-window edge, not the layer edge; the domination condition needs `2/sin(πδ) ≤ Ψ(t)`, so the corrected edges are `δ*·ℓ = 4.55, 5.73` at the two of seven heights that admit any δ at all, and the layer constant at a given height is `4·(ℓ/2π)/Ψ(t)·(1+o(1))`, i.e. 4 at mean density."*
* **§1.2 clause 2** — replace `μ_y(t − s) + μ_y(t + s) ≤ Ψ(s) for every s ∈ ℝ` by `2[μ_y(t − s) + μ_y(t + s)] ≤ Ψ(s) + Ψ(−s) for every s ≥ 0` (local content `2/sin(πδ) ≤ Ψ(t)`), noting that the original is unsatisfiable at `s = −t`.
* **§1.2 clause 3(i)** — `1/sin(πδ) ≤ min Ψ − 4πδe^{−4π}` becomes `2/sin(πδ) + ε₃(δ) ≤ min_{|s−t|≤4} Ψ(s)`, `ε₃(δ) = 4.03 sin(πδ)e^{−4π} ≤ 1.4054·10⁻⁵`; clause 3(ii) is discharged for ζ by Theorem G (`G = 7.5`), and the clause's "below `t − 4` automatic from `γ₁`" is withdrawn (it needs the gap condition too).
* **§1.2 clause 4** — `(2/ℓ)(1 + ε + O(ε²))` becomes `(4/ℓ)(1 + ε + O(ε²) + O(ℓ⁻²))`; the layer is `{1 − σ < (4 + o(1))/log t}`.
* **§1.2 clause 5** — the recalled "`C_uncond` of order 50–70" becomes the computed **66.41**, at `H* = 0.9719` (not the contract's `H = 4πc₁ = 1.3044`, which gives 92.3), non-vacuous from `t ≥ e^{377.4}`, from HSW arXiv:2107.06506v1 Corollary 1.2 read at the page. Record that the contract's number was right only by cancellation of two errors (`1/sin` for `2/sin`, and a non-optimal `H`).
* **§1.2 clause 6** — `8p(0)e^{−δL′}/δ·‖q‖` becomes `16 p(0)‖q‖_∞ e^{−δL′}/δ` (the 8 counts two orbit points, not four).
* **§1.9** — in the refutation-shaped close, "whenever `1/sin(πδ) ≤ min Ψ`" becomes "whenever `2/sin(πδ) ≤ min Ψ`", and the close should name the constants `C = 4 + o(1)` (mean density / under RH) and `C = 66.41 + o(1)` (unconditional, `t ≥ e^{377}`).

**3. `directions/C2-rigidity-conservation.md`, line 81** (the Session-21 work-log entry). Replace

> R1 contract (§1.2, 7 clauses): no strip-positive cone certificate excludes a zero at (t, ½−δ) at any bandwidth whenever 1/sin(πδ) ≤ Ψ(t) := Σ_γ 1/cosh(π(t−γ)) (mean-strength smoothed density) — the cone's reach lies inside the layer 1−σ < (2+o(1))/log t; bandwidth pinned ≍ 1/δ.

by

> R1 contract (§1.2, 7 clauses): no strip-positive cone certificate excludes a zero at (t, ½−δ) at any bandwidth whenever **2/sin(πδ) ≤ Ψ(t)** := Σ_γ 1/cosh(π(t−γ)) (a hypothetical pair puts two zeros at height t) — the cone's reach lies inside the layer **1−σ < (4+o(1))/log t**; bandwidth pinned ≍ 1/δ. *[Constant corrected 2026-09-10 by `results/c2-r1/confinement-note.md` §0.4 D1, dual-checked in `check-O.md` §2; the contract's form is unsatisfiable as written. The killer's shape C/log t (line 70) is unchanged.]*

The append-only work log should take this as a **new dated line** rather than an edit, with the frontier line updated to "repair 1 DISCHARGED (theorem + dual check)".

**4. `results/program-digest-s21.md` §E item 7 (line 314).** The item quotes no constant, so nothing there is *wrong*; but on banking it must acquire the constants and the scope. Suggested banked form: *"A cone-sector (termwise-positive conservation) certificate cannot yield a zero-free point outside a de la Vallée Poussin-shaped layer `{1 − σ < C/log t}` at every bandwidth, with `C = 4 + o(1)` where Ψ has mean strength (under RH at every large height) and `C = 66.41 + o(1)` unconditionally for `t ≥ e^{377}`; the layer is nonempty (`c = 1/34.82`). Hypothesis: `2/sin(πδ) ≤ Ψ near t` — a pair puts two zeros at height t. Banked 2026-09-10: `results/c2-r1/confinement-note.md` + `check-O.md`, theorem + dual-model."* Also: the item's "outside the Vinogradov–Korobov region" is implied a fortiori (the proved layer `C/log t` sits inside VK), so the wording stays true, but the sharper statement is the one to bank.

**5–9. Corrections internal to `confinement-note.md`** (additions, never rewrites; all cosmetic):
5. **§0.4 D1** — add the unconditional bound alongside the numerical one: `Ψ(−t) ≤ 2Σ_γ e^{−π γ} ≤ 2.6·10⁻¹⁰` for every `t ≥ 0`, from the formal local count and `γ₁ > 14`, so the unsatisfiability does not rest on a zero computation.
6. **§3 remark (3)** — the `+1/8` is not a "possible misprint" between HSW (1.4) and (1.5): (1.4) is Theorem 1.1's general form and genuinely carries the `+1/8`, (1.5) is Corollary 1.2's specialization without it. Moreover the shift **cancels** in every difference `N(T+G) − N(T)` the note takes, so the precaution is free in both directions. Restate accordingly.
7. **§3, Theorem G's proof** — two label systems collide in one paragraph (the prose `(a)/(b)/(c)` and the script keys `Theorem G (a)–(d)`). Rename one set.
8. **§8.3** — the IV.7 Opus read is at `BARRIER-ZOO.md` line 385, not 386.
9. **§7 line 317 and §8.1 line 341** — `§8.4` should read `§8.5` (the budget-floor material is in §8.5; §8.4 is the zoo protocol). And at line 341 the "cannot come from finite-variation perturbations" sentence should carry the same `[the pricing's finding]` label it carries in §8.5.
10. **Front matter, line 5** — the lint sentence contains all four banned words. Replace the enumeration with, e.g., *"Lint (KICKSTART 10(g)): the four banned hedges do not occur in the body of this note."*

**Also worth adding to the note's §8.3, from this check:** the closest antecedent in *shape* found anywhere in the corpus is `w-14` §2.1.3 / (2.22) — an explicit "universal limitation of this method" for the Carneiro-school extremal problems (EP1)/(EP2) on the subclass `A₀` — for a different functional, under RH. Recording it strengthens rather than weakens the novelty claim, because it shows the search reached the right shelf.

---

## §13 The label of `zoo-IV18-proposed.md`

**Decision: `program-adjudicated (dual-model)`.** The theorem's seven clauses are re-derived and close; the numerics reproduce; the sources are read at the page by both agents independently; the formal input's axiom line is clean; the corpus re-read finds no antecedent.

**The STATEMENT must carry the factor-2 correction and the exact hypothesis — and, as drafted, it already does**, in three places: clause (2)'s `2[μ_y(t−s) + μ_y(t+s)] ≤ Ψ(s) + Ψ(−s)` with the local content `2/sin(πδ) ≤ Ψ(t)` in bold; clause (3)'s `2/sin(πδ) + ε₃(δ) ≤ min_{|s−t|≤4}Ψ(s)`; and the explicit "Correction of record (D1)" sentence naming `PRICING-next-unit.md` §1.2 and C2 line 81 as off by a factor 2 and the layer constant as 4. No change is required there.

**One amendment is required before insertion: §12 item 1, the KILLS field's scope.** With that amendment the entry may be inserted as IV.18 (Group IV count 18, total 55), status line reading `program-adjudicated (dual-model)` + `computationally-verified` numerics, with `[novelty: dual-model check 2026-09-10]` replacing `[novelty: single-check]`.

---

## §14 Closing honesty note (standing order 5)

* **Read at the page in this session, by me:** `Zeta23/WeilEF/Main.lean` 240–300; `Zeta23/ExplicitFormula.lean` 60–90; `Zeta23/Defs.lean` 40–48, 103–107; `Zeta23/Statement/SeamClosed.lean` 18–30; `Zeta23/WeilEF/Effective.lean` 918–930; Hasanalizade–Shen–Wong arXiv:2107.06506v1 pp. 1–3 and p. 15 (abstract, Table 1, Theorem 1.1 (1.2)–(1.4), Corollary 1.2 (1.5), (1.7), Corollary 1.4, Table 2, (5.5)–(5.6) and the proof of Corollary 1.2); Trudgian arXiv:1208.5846v2 pp. 1–3 (abstract, Table 1, Theorem 1, Corollary 1, (1.2) with footnote 1, (2.2)–(2.5)); `BARRIER-ZOO.md` §0 (lines 17–33), III.1, III.2, III.9, IV.1, IV.7; `directions/C2-rigidity-conservation.md` lines 1–25 and 60–90; `results/c2-m5/PRICING-next-unit.md` §0–§1.3 and §1.9–§1.10; `results/program-digest-s21.md` line 314; `results/c3-r/m0-axiom-note.md` lines 361–393; the text layers of `fetched/w-14`, `fetched/w-15`, `fetched/y-25`, `fetched-r2/r-25a`; `confinement-note.md`, `zoo-IV18-proposed.md`, `SHARED.md`, `hashes.txt` and all six scripts under `verify/` in full.
* **Computed by me:** all six of the author's scripts re-run from clean copies (`normalization_zeta_check`, `clause5_constants`, `dlvp_constant`, `kernel_lemmas`, `confinement_edge`, `gaps_first_zeros`), every log reproduced line for line up to wall-clock seconds; plus `opus_independent.py`, written from scratch for this check, re-deriving Lemma P's closed form/mass/peak/tail constant by quadrature, the `Ψ(−t)` bounds (numerical and unconditional), all five Theorem G thresholds, `H*`/`m*`/`C_uncond`/`log t₀`, the closed-form optimization `max_X[14 − X − 48/X] = 14 − 8√3`, exact `B(w_{a,t})` against its bound at four heights, and Lemma A at four points. One `lake env lean` process for the two `#print axioms` lines; no Lean file created, modified or rebuilt inside the tree.
* **Not done:** I did not re-derive rung 1 (function fields) or rung 3 (the degree-2 identity) — neither is proved in the note either, and both are labeled "stated, not proved". I did not read Heath-Brown 1992 or Berry 1988. I did not run the DH cone-row diagnostic. I did not attempt to decide whether the domination condition (D) is *necessary* as well as sufficient — clause 2 claims only sufficiency, and the note is explicit that the theorem is one-sided; the gap between (D) and the true reach of the cone at a given `(t, δ)` is not quantified anywhere and is a real open quantity, distinct from the budget-floor problem of §8.5.
* **What I checked hardest, and what I would still call the note's weakest joint.** D1 was checked three ways (parity argument, numerics, unconditional bound) and is secure. Lemma E's approximation is the longest argument in the note and I checked every inequality in it; it is sound, but it is the one place where an error would be least visible to a numerical check, so it is the right place for any future reader to look first. Clause 5's constant is honest and very weak (`t ≥ e^{377}`), and the note says so in its own words; nobody should read `C_uncond = 66.41` as a working number.
* **Nothing was edited outside this file. Nothing was committed.**

*End of check. Job 2, Opus 5, 2026-09-10.*
