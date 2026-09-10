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
