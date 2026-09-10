# The Sector-I confinement theorem (Theorem R1, ζ-anchored): a theorem note

**Deliverable:** C2 mandatory repair 1 (`directions/C2-rigidity-conservation.md` line 74, "state the Sector-I confinement bound as an up-front THEOREM of the field"), built to the contract of `results/c2-m5/PRICING-next-unit.md` §1.2 under the brief `results/c2-r1/BRIEF.md`. Written 2026-09-10 (Session 21, Job 1, the author, Fable 5.1). Dual check owed to Job 2 (`results/c2-r1/check-O.md`) before anything here is banked.

**Status (read before citing).** This is a theorem note. Clauses 1, 2, 3, 6 and 7 are proved here in full from one formal input (the explicit formula `EF_lit_zetaZeroConfig` of `Zeta23/WeilEF/Main.lean`, quoted verbatim in §1) plus elementary analysis; clause 4 is proved under an explicit hypothesis on ζ's local zero density; clause 5 is proved unconditionally with explicit constants from a source read at the page in this session (Hasanalizade–Shen–Wong, arXiv:2107.06506v1, Corollary 1.2). Every number is either computed by a script under `results/c2-r1/verify/` with a log, or read at a page named here; the few recalled items are labeled `[recalled, unverified]` and nothing rests on them. The note also contains a dated deviation record (§0.4): the contract's clause 2 hypothesis, read literally over all real s, cannot be satisfied and the corrected hypothesis costs a factor 2 in the layer constant — the layer is 1 − σ < (4 + o(1))/log t, not (2 + o(1))/log t. The shape (the killer's C/log t) is unchanged; the constant is not, and every downstream sentence that quotes "2/log t" or "1/sin(πδ) ≤ Ψ" (PRICING-next-unit §1.1(c), §1.2 clauses 2–5, C2 line 81, the digest §E item 7) must be corrected by the orchestrator. Lint (KICKSTART 10(g)): the words "clearly", "obviously", "easy to see", "well known" do not occur in this note. U.S. English.

---

## §0 Objects, the identity in cone form, and the deviation record

### §0.1 Conventions (one normalization, used by every script in `verify/`)

* **Transform.** For w ∈ L¹(ℝ), ŵ(ξ) := ∫_ℝ w(u) e^{−iuξ} du. For an even real w, ŵ is even and real, and ŵ(0) = ∫ w. If w ≥ 0 then |ŵ(ξ)| ≤ ŵ(0) for every ξ; if ŵ ≥ 0 and ŵ ∈ L¹ then |w(u)| ≤ w(0) for every u (both are the triangle inequality applied to the integral defining the transform, the second after Fourier inversion). If ŵ is real then w is even (ŵ real forces w(−u) = conj(w(u)) = w(u) for real w).
* **The cone.** For 0 < L ≤ ∞ put
  Σ_L := { w ∈ C²(ℝ) : w ≥ 0, ŵ ≥ 0, supp w ⊂ [−L, L] } (L < ∞),
  the strip-positive cone of C2 line 16, with the C² requirement made explicit because the formal explicit formula used in clause 1 is stated for C²_c tests (§1). Elements of Σ_L are automatically even. Σ_∞ := { w : w ≥ 0, ŵ ≥ 0, and the identity (0.3) below holds for w with every sum absolutely convergent }; it contains every Σ_L (clause 1) and the de la Vallée Poussin elements of clause 7 (Lemma E, §4).
* **The test.** g := w / cosh(u/2). For z ∈ ℂ with |Im z| ≤ ½, ĝ(z) := ∫ g(u) e^{izu} du; this is the Lean `paperFT g z` (`Zeta23/Defs.lean` line 44: `paperFT (f : ℝ → ℂ) (z : ℂ) : ℂ := ∫ u : ℝ, f u * Complex.exp (Complex.I * z * (u : ℂ))`). For even g and real r, ĝ(r) = ∫ g(u) cos(ru) du = ĝ(−r), and ĝ(conj z) = conj(ĝ(z)) for real g.
* **Zeros.** ρ = β + iτ runs over the nontrivial zeros of ζ, with multiplicity m_ρ; γ(ρ) := (ρ − ½)/i = τ − i(β − ½) (the Lean `gammaOf`, `Zeta23/Defs.lean` line 105: `gammaOf (ρ : ℂ) : ℂ := (ρ - 1 / 2) / Complex.I`). An on-line zero ρ = ½ + iτ has γ(ρ) = τ ∈ ℝ. The set of nontrivial zeros is invariant under ρ ↦ conj ρ and ρ ↦ 1 − ρ; an off-line zero β + iτ with β > ½ therefore lies in an orbit of four zeros {β ± iτ, 1 − β ± iτ}, whose γ-values are {t − iy, t + iy, −t − iy, −t + iy} with t := τ and y := β − ½ ∈ (0, ½). Throughout, **y ∈ [0, ½) is the depth of a hypothetical orbit and δ := ½ − y = 1 − β its distance from the edge Re s = 1.**
* **Kernels.** For 0 ≤ y < ½,
  k_y(u) := cosh(yu)/cosh(u/2),   μ_y(ξ) := (1/2π) ∫ k_y(u) e^{−iuξ} du.
  Lemma P (§0.3) gives the closed form μ_y(ξ) = 2cos(πy)cosh(πξ)/(cosh 2πξ + cos 2πy) (C2 line 16), and μ_0(ξ) = 1/cosh(πξ).
* **The on-line density.** Ψ(s) := Σ_{ρ = ½ + iτ, τ > 0} m_ρ μ_0(s − τ), the sech-smoothed density of the on-line zeros with positive ordinate, counted with multiplicity. (Definition precision against the contract, recorded in §0.4: the sum runs over on-line zeros only; an off-line zero, if one existed, is accounted for separately in (0.3) and contributes a nonnegative term. Below height 3·10¹² there is none — Platt–Trudgian 2020, on disk as `fetched-r3/p3-22a1-platt-trudgian-2020-rh-true-up-to-3e12.pdf`, not re-read for this note and not load-bearing anywhere in it.) Ψ is finite everywhere and continuous: the local count N(τ, τ + 1] is at most 5.4·10⁸ log(|τ| + 3) (the formal `zeta_local_zero_count_explicit`, `Zeta23/WeilEF/Effective.lean` lines 926–927, quoted in §1), and μ_0 decays like 2e^{−π|ξ|}.
* **The archimedean density.** A(r) := (1/2π)[Re ψ(¼ + ir/2) − log π], where ψ = Γ′/Γ (the Lean `gammaBracket r := (Complex.digamma (1/4 + I*r/2)).re − Real.log π`, `Zeta23/ExplicitFormula.lean` line 64, divided by 2π).
* **The three functionals.** For w ∈ Σ_∞:
  B(w) := 2ŵ(0) + ∫_ℝ (ŵ ∗ μ_0)(r) A(r) dr   (pole plus archimedean: the budget),
  Z(w) := Σ_ρ m_ρ ĝ(γ(ρ))   (the zero share),
  P(w) := Σ_{n ≥ 1} Λ(n) n^{−1/2} (g(log n) + g(−log n)) = 4 Σ_{n ≥ 2} Λ(n) w(log n)/(n + 1)   (the prime share; n^{−1/2}/cosh(½ log n) = 2/(n + 1)).
* **Orbit share and certificate.** The share of a hypothetical orbit at (t, y) in the test g is the sum of ĝ over its four γ-values, which by the symmetries of ĝ equals 4 Re ĝ(t − iy) = 4(ŵ ∗ μ_y)(t) (Lemma K below). A **cone certificate at (t, y)** is an element w ∈ Σ_∞ with 4(ŵ ∗ μ_y)(t) > B(w); by the identity (0.3) and the positivity of every other share such a w proves that ζ has no zero at ½ + y + it (C2 line 16: the region {V > 1} is zero-free, V(t, y; L) := sup{4(ŵ ∗ μ_y)(t) : w ∈ Σ_L, B(w) ≤ 1}; C2 writes the orbit share as 2(ŵ ∗ μ_y) per conjugate pair, this note writes the full orbit, so its V is twice C2's — a labeling convention, not a change of content).

**Lemma K (strip positivity and the orbit share).** Let w ∈ Σ_∞, g = w/cosh(u/2), x ∈ ℝ, 0 ≤ y < ½. Then Re ĝ(x − iy) = (ŵ ∗ μ_y)(x) ≥ 0, and the sum of ĝ over the four points {±x ± iy} equals 4(ŵ ∗ μ_y)(x).

*Proof.* e^{i(x − iy)u} = e^{yu}(cos xu + i sin xu). Since g is even, the odd parts integrate to zero and Re ĝ(x − iy) = ∫ g(u) cosh(yu) cos(xu) du = ∫ w(u) k_y(u) cos(xu) du. The product w·k_y has transform (1/2π)(ŵ ∗ k̂_y) = ŵ ∗ μ_y (convolution theorem, both factors in L¹ ∩ L²; k_y ∈ L¹ because k_y(u) ≤ 2e^{−δ|u|}, Lemma P(iv)), and the transform of the even real function w k_y at x is ∫ w k_y cos(xu) du. Both ŵ and μ_y are nonnegative (Lemma P(i)), so the convolution is nonnegative. For the four points: ĝ(−z) = ĝ(z) (g even) and ĝ(conj z) = conj ĝ(z) (g real), so ĝ(x − iy) + ĝ(x + iy) + ĝ(−x − iy) + ĝ(−x + iy) = 2[ĝ(x − iy) + conj ĝ(x − iy)] = 4 Re ĝ(x − iy). ∎

### §0.2 The identity in cone form

For w ∈ Σ_∞,

  **B(w) = Z(w) + P(w),  with Z(w) ≥ 2 ∫_ℝ ŵ(s) Ψ(s) ds ≥ 0 and P(w) ≥ 0.**   (0.3)

This is clause 1 of the theorem for w ∈ Σ_L (proved in §1 from the formal explicit formula) and Lemma E for the de la Vallée Poussin elements (§4). The two consequences used everywhere: ŵ(0) = ∫w = sup ŵ, and the on-line part of Z is exactly 2∫ŵΨ:

  Z_on(w) := Σ_{ρ = ½ + iτ} m_ρ ĝ(τ) = Σ_{τ > 0} m_ρ [ĝ(τ) + ĝ(−τ)] + (share of a zero at ½, if any) ≥ 2 Σ_{τ > 0} m_ρ (ŵ ∗ μ_0)(τ) = 2 ∫ ŵ(s) Ψ(s) ds,   (0.4)

the last step by Tonelli (all terms nonnegative). ζ(½) ≠ 0 [recalled, unverified — the inequality (0.4) does not use it; a zero at ½ would only add a nonnegative term].

**The normalization was verified against ζ itself** (`verify/normalization_zeta_check.py` → `normalization_zeta_check_run.log`, `normalization_zeta_check_out.json`; reproducing PRICING-next-unit §0's check in this note's own code): for the Fejér family ŵ_T(τ) = (1 − |τ|/T)₊, w_T(u) = (T/2π) sinc²(Tu/2), ∫w_T = 1, the two sides of (0.3) — B(w_T) = 2 + ∫ŵ_T a with a := μ_0 ∗ A, against P(w_T) (exact von Mangoldt sieve to 4·10⁶ plus a tail estimate) plus Z(w_T) (the first 200 zeros) — agree to the size and sign of the tail estimate, and **the zero share is 0 for T ≤ 11 and switches on as the triangle's support crosses γ₁ = 14.134725**; the numbers are in §7 (Table N) and the log. (The Fejér elements are band-limited, not compactly supported in u, so they are Σ_∞-elements by the classical explicit formula for tests of this decay — the check is an illustration of the normalization, not an input to any proof below.)

### §0.3 Lemma P (Poisson peak and tails of the depth kernel; the parameter-pin inequality)

**Lemma P.** Let 0 ≤ y < ½, δ := ½ − y, and μ_y as in §0.1. Then:
(i) μ_y(ξ) = 2cos(πy)cosh(πξ)/(cosh 2πξ + cos 2πy) = Re[1/cosh(π(ξ + iy))]; μ_y is even, real-analytic, strictly positive, and strictly decreasing in |ξ|.
(ii) ∫_ℝ μ_y = 1 and μ_y(0) = 1/cos(πy) = 1/sin(πδ) = sup μ_y.
(iii) For every ξ, μ_y(ξ) ≤ sin(πδ) cosh(πξ)/sinh²(πξ); for |ξ| ≥ 1, μ_y(ξ) ≤ c_P sin(πδ) e^{−π|ξ|} with c_P := 2.012 (the sharp constant at |ξ| = 1 is 2(1 + e^{−2π})/(1 − e^{−2π})² = 2.01125…, `verify/kernel_lemmas.py`); in particular μ_y(ξ) ≤ 4πδ e^{−π|ξ|} there, which is the form the contract quotes.
(iv) k_y(u) = cosh(yu)/cosh(u/2) ≤ 2e^{−δ|u|} for all u, and k_y(0) = 1 = sup k_y.

*Proof.* (i) cosh(yu) e^{−iuξ} = ½[e^{−iu(ξ + iy)} + e^{−iu(ξ − iy)}], and the transform of 1/cosh(u/2) at a complex frequency ζ with |Im ζ| < ½ is 2π/cosh(πζ) (the standard integral ∫ e^{−iuζ}/cosh(u/2) du = 2π/cosh(πζ), which is the analytic continuation of the real-frequency formula, the integral converging absolutely for |Im ζ| < ½; checked numerically at y = 0, 0.25, 0.4, 0.45, 0.49 in `verify/kernel_lemmas.py`). Hence μ_y(ξ) = ½[1/cosh(π(ξ + iy)) + 1/cosh(π(ξ − iy))] = Re[1/cosh(π(ξ + iy))]. Now cosh(πξ + iπy) = cosh πξ cos πy + i sinh πξ sin πy, whose modulus squared is cosh²πξ cos²πy + sinh²πξ sin²πy = cosh²πξ − sin²πy = ½(cosh 2πξ + cos 2πy); taking the real part of the reciprocal gives the closed form. Positivity: cos πy > 0 for y < ½ and cosh²πξ − sin²πy ≥ 1 − sin²πy > 0. Monotonicity: with c := cosh πξ and s := sin πy, μ_y = cos(πy)·c/(c² − s²), and d/dc [c/(c² − s²)] = −(c² + s²)/(c² − s²)² < 0 while c is strictly increasing in |ξ|.
(ii) ∫μ_y = k_y(0) = 1 (Fourier inversion at u = 0, k_y continuous and μ_y ∈ L¹ by (iii)). μ_y(0) = cos πy/(1 − sin²πy) = 1/cos πy = 1/sin πδ; it is the supremum by (i).
(iii) cosh 2πξ + cos 2πy ≥ cosh 2πξ − 1 = 2 sinh²πξ gives the first bound. For |ξ| ≥ 1 write x := e^{−π|ξ|} ≤ e^{−π}: cosh πξ/sinh²πξ = 2x(1 + x²)/(1 − x²)², and (1 + x²)/(1 − x²)² is increasing in x on [0, 1), so it is at most its value at x = e^{−π}, namely 1.005624…; hence cosh πξ/sinh²πξ ≤ 2.0113 e^{−π|ξ|} ≤ c_P e^{−π|ξ|}. Finally sin(πδ) ≤ πδ and c_P < 4.
(iv) cosh(yu) ≤ e^{y|u|} and cosh(u/2) ≥ ½ e^{|u|/2}, so k_y(u) ≤ 2e^{(y − ½)|u|} = 2e^{−δ|u|}; k_y(0) = 1, and k_y(u) < 1 for u ≠ 0 since y < ½. ∎

*Numerical record (`verify/kernel_lemmas_run.log`):* mass and peak of μ_y at y ∈ {0, 0.25, 0.4, 0.45, 0.49} to 10⁻¹²; the tail ratio max_{|ξ| ≥ 1} μ_y(ξ)e^{π|ξ|}/sin(πδ) ≤ 2.0113 at every tabulated y; k_y(u)e^{δ|u|} ≤ 2 on a grid.

### §0.4 Deviation and precision record (dated 2026-09-10; contract = PRICING-next-unit §1.2)

**D1 (substantive — the factor 2).** The contract's clause 2 hypothesis reads "μ_y(t − s) + μ_y(t + s) ≤ Ψ(s) for every s ∈ ℝ". With Ψ supported (up to exponentially small tails) on s > 0, this fails at s = −t for every t > 0 and every y: the left side is ≥ μ_y(0) = 1/sin(πδ) ≥ 1 there while Ψ(−t) ≤ Σ_τ 2e^{−π(t + τ)} < 10⁻¹⁹ for t ≥ 0 (γ₁ = 14.13). The hypothesis as written is therefore never satisfied, and clause 2 as written is vacuous. The correct comparison uses the evenness of ŵ to fold the negative half-line onto the positive one (§2, proof of clause 2): the sufficient condition is

  **2[μ_y(t − s) + μ_y(t + s)] ≤ Ψ(s) + Ψ(−s) for every s ≥ 0,**   (D)

and its local content at s = t is **2/sin(πδ) ≤ Ψ(t)**, not 1/sin(πδ) ≤ Ψ(t). Reading: a hypothetical orbit puts two zeros at height +t, each carrying the depth weight μ_y(0) = 1/sin(πδ) against the weight 1 of an on-line zero, and the on-line zeros near +t must cover both; the contract's version would let a near-double pair (δ → ½) be dominated by one on-line zero's worth of density, which is false. Consequences: clause 3(i) reads 2/sin(πδ) + slack ≤ min Ψ; the layer of clauses 4–5 is 1 − σ < (4 + o(1))/log t (mean density ℓ/2π, ℓ = log(t/2π)), not (2 + o(1))/log t; the pricing's "exact layer edge" table (PRICING-next-unit §1.1(c), δ*·ℓ ≈ 2 at t = 10⁶) was computed with the literal condition on the window |s − t′| ≤ 2 only and is superseded by §7 Table E of this note; the theorem is vacuous wherever Ψ < 2 (a pair weighs at least two on-line zeros), which at t = 10⁶ is most points of the window (Ψ there ranges 1.08–2.15), so the first heights at which the ζ-anchored statement says anything are those with Ψ(t) > 2 — t ≳ 2π e^{4π} ≈ 1.8·10⁶ on mean density. The refutation-shaped close (§9) is stated with the corrected constant. The killer's shape C/log t (C2 line 70) is untouched.

**D2 (precision).** Ψ is defined over on-line zeros with positive ordinate (§0.1); the contract's wording "over the positive ordinates of the nontrivial zeros" is read that way, consistently with its own clause 1 ("nonnegative terms from off-line zeros of ζ, if any").

**D3 (precision).** Σ_L carries the C² requirement explicitly (the formal input's hypothesis). Σ_∞ is defined by the validity of (0.3), and the de la Vallée Poussin elements are shown to belong to it (Lemma E) rather than assumed to.

**D4 (constants, all within the contract's slack).** The tail constant of Lemma P(iii) is proved as c_P sin(πδ) = 2.012 sin(πδ) instead of the contract's 4πδ; the localization slack is written ε₃(δ) := 4.03 sin(πδ) e^{−4π} ≤ 1.41·10⁻⁵ in place of the contract's 4πδe^{−4π} (the two differ by at most 1 % at δ = ½ and the theorem's statement carries ε₃ explicitly). Clause 3(ii) is stated with the maximal gap G of consecutive zero ordinates and the condition 1/cosh(πG/2) ≥ ε₃(δ), which is what the proof uses (every s ≥ γ₁ is within G/2 of an ordinate); the contract's "within distance G" with "1/cosh(πG/2)" mixed the two. Clause 3's "below t − 4 automatic from γ₁" is corrected: for s between γ₁ and t − 4 the gap condition is needed as well (the bound Ψ(s) ≥ e^{−π|s − γ₁|} is useless far from γ₁); the contract's slack allocation is otherwise kept. **Clause 3(ii) is then discharged for ζ unconditionally at every height (Theorem G, §3)**, so for ζ clause 3 reduces to (i).

**D5 (clause 6's constant).** The parameter-pin bound is proved with constant 16 p(0)‖q‖_∞ e^{−δL′}/δ; the contract's "8 p(0) e^{−δL′}/δ · q-norm" names no norm and, with the sup norm, the factor 8 is what one gets for the two orbit points at height +t alone (2 Re ĝ) rather than the full orbit (4 Re ĝ). The pin's content (bandwidth beyond ≍ 1/δ changes the orbit share by an exponentially small amount) is unchanged.

**D6 (clause 5 landed).** Both fetch-list sources were located on arXiv by title and read at the page in-session (§5): Hasanalizade–Shen–Wong arXiv:2107.06506v1 (SHA-256 of the PDF 3fc4c89f…) and Trudgian arXiv:1208.5846v2 (SHA-256 274b3a0a…). Clause 5 is therefore stated and proved with explicit constants, not deferred. Trudgian's arXiv v2 constants (0.111, 0.275, 2.450) differ from the journal constants HSW's Table 1 attributes to Trudgian 2014 (0.1120, 0.2780, 3.3850); nothing here uses Trudgian's constants, only his identity (2.5) and the Platt-database bound HSW quote as (1.7).

---

## §1 The formal input and clause 1 (the identity clause)

### §1.1 The input, quoted as Lean states it (`~/rh-lean-work/zeta-23-lean-main`, read 2026-09-10; no Lean file was modified)

`Zeta23/WeilEF/Main.lean`, lines 268–270:

```
/-- **Hypothesis-free form**: [eq:EFstd] holds for the canonical
unconditional ζ zero configuration. -/
theorem EF_lit_zetaZeroConfig : Zeta23.EF.EF_lit zetaZeroConfig := EF_lit_zeta zetaSeam
```

with `EF_lit_zeta (hs : ZetaSeam) : Zeta23.EF.EF_lit (zetaZeros hs)` (same file, line 51), `zetaSeam : ZetaSeam := ZetaSeam.of_reflect zeta_reflect_zero zeta_mult_reflect` and `def zetaZeroConfig : ZeroConfig := zetaZeros zetaSeam` (`Zeta23/Statement/SeamClosed.lean`, lines 22 and 26). The predicate, `Zeta23/ExplicitFormula.lean` lines 81–84:

```
def EF_lit (Z : ZeroConfig) : Prop :=
  ∀ k : ℝ → ℂ, ContDiff ℝ 2 k → HasCompactSupport k →
    Summable (fun ρ : Z.carrier => (Z.mult ρ : ℂ) * paperFT k (gammaOf ρ)) ∧
    ∑' ρ : Z.carrier, (Z.mult ρ : ℂ) * paperFT k (gammaOf ρ) = literatureRHS k
```

and the right-hand side, lines 69–73:

```
def literatureRHS (k : ℝ → ℂ) : ℂ :=
  paperFT k (I / 2) + paperFT k (-I / 2)
  - ∑' n : ℕ, ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ)
      * (k (Real.log n) + k (-Real.log n))
  + (1 / (2 * π) : ℂ) * ∫ r : ℝ, paperFT k r * (gammaBracket r : ℂ)
```

with `gammaBracket (r : ℝ) : ℝ := (Complex.digamma (1 / 4 + I * r / 2)).re - Real.log π` (line 64) and `paperFT` as quoted in §0.1. **The hypotheses on the test are exactly two: `ContDiff ℝ 2 k` and `HasCompactSupport k`.** The docstring of `EF_lit` (lines 75–80) names the literature form: "[eq:EFstd]; [IK04, Thm 5.12] specialised to ζ / [Wei52] / [Bom00] … It is a hypothesis (structure field in Hypotheses.lean), never a Lean axiom" — and `EF_lit_zetaZeroConfig` discharges that hypothesis for ζ's zero configuration. Audit status (`AUDIT.md`, "Recorded results at this commit", read): `lake build` completes with no errors and no `sorry` under `Zeta23/`; declared axioms in the repository: 0; every `#print axioms` line of the 27 comparator statements is exactly `[propext, Classical.choice, Quot.sound]`. The theorem `EF_lit_zetaZeroConfig` itself is not among the 27 printed statements; per KICKSTART 10(f) its own `#print axioms` line is owed by the checker (Job 2) and is not claimed here.

The second formal input, used only for absolute convergence in Lemma E (§4) and for the finiteness of Ψ: `Zeta23/WeilEF/Effective.lean`, lines 924–927:

```
/-- **E2 — the fully explicit local zero count**:
N(t, t+1] ≤ 540000000·log(|t|+3) for every t ∈ ℝ, unconditionally. -/
theorem zeta_local_zero_count_explicit (t : ℝ) :
    (Zeta23.Ncount t (t + 1) : ℝ) ≤ 540000000 * Real.log (|t| + 3) := by
```

### §1.2 Clause 1 and its proof

**Theorem R1, clause 1 (identity clause).** For every L > 0 and every w ∈ Σ_L, the sum Z(w) = Σ_ρ m_ρ ĝ(γ(ρ)) converges absolutely, every one of its terms is real and nonnegative, and

  B(w) = Z(w) + P(w),  Z(w) = 2∫_ℝ ŵ Ψ + Σ_{off-line orbits} 4(ŵ ∗ μ_{y_j})(x_j) ≥ 2∫ŵΨ,  P(w) ≥ 0.

*Proof.* Let g := w/cosh(u/2). Since w ∈ C² has compact support and 1/cosh(u/2) is smooth, g ∈ C²_c(ℝ), so `EF_lit_zetaZeroConfig` applies to k := g (as a function ℝ → ℂ with zero imaginary part). Its first conjunct is the absolute convergence (summability in Lean's sense, which for a family of complex numbers means absolute summability); its second conjunct is the identity Σ_ρ m_ρ ĝ(γ(ρ)) = literatureRHS(g). Term by term:

* ĝ(i/2) + ĝ(−i/2) = ∫ g(u)(e^{−u/2} + e^{u/2}) du = ∫ 2 cosh(u/2) g(u) du = 2∫w = 2ŵ(0).
* The prime term is Σ_n Λ(n) n^{−1/2}(g(log n) + g(−log n)) = P(w), a finite sum (supp g compact), and P(w) ≥ 0 because Λ(n) ≥ 0 (axiom P, here a theorem: the von Mangoldt function is nonnegative by definition) and g ≥ 0.
* The archimedean term is (1/2π)∫ ĝ(r)[Re ψ(¼ + ir/2) − log π] dr = ∫ (ŵ ∗ μ_0)(r) A(r) dr, by Lemma K at y = 0 (ĝ(r) = Re ĝ(r) = (ŵ ∗ μ_0)(r) for real r) and the definition of A.
So literatureRHS(g) = 2ŵ(0) + ∫(ŵ ∗ μ_0)A − P(w) = B(w) − P(w), which is the identity. For the structure of Z(w): the zeros are invariant under ρ ↦ conj ρ and ρ ↦ 1 − ρ with multiplicities preserved (this is what `ZetaSeam.of_reflect zeta_reflect_zero zeta_mult_reflect` packages; for ζ it is the functional equation together with ζ(conj s) = conj ζ(s)). Group the zeros: an on-line zero ρ = ½ + iτ has γ(ρ) = τ real and ĝ(τ) = (ŵ ∗ μ_0)(τ) ≥ 0 (Lemma K, y = 0); ρ and conj ρ contribute the same amount, and summing over τ > 0 gives 2Σ_{τ>0} m_ρ(ŵ ∗ μ_0)(τ) = 2∫ŵΨ by (0.4) (a zero at s = ½, if there were one, adds (ŵ ∗ μ_0)(0) ≥ 0). An off-line zero β + iτ with β ≠ ½ lies in a four-element orbit whose total share is 4(ŵ ∗ μ_y)(|τ|) ≥ 0 with y = |β − ½| (Lemma K; orbits with τ = 0 would be two-element and contribute 2(ŵ ∗ μ_y)(0) ≥ 0). All terms being nonnegative, the regrouping is legitimate. ∎

*Remarks.* (1) The clause is unconditional: nothing about the location of ζ's zeros is used; if off-line zeros exist they only enlarge Z. (2) The one place where the Riemann–Weil formula's hypotheses bite is the test class: w ∈ C²_c. The cone Σ_L of C2 line 16 without the C² requirement is handled by mollification when needed; the note does not need it. (3) Axiom P is consumed exactly once, in "P(w) ≥ 0"; this is the S1 bearing of §6 and the reason the theorem is vacuous on the Davenport–Heilbronn rung (§6.2).

---

## §2 Clause 2 — the domination clause

**Theorem R1, clause 2 (domination clause; hypothesis corrected per §0.4 D1).** Let t > 0 and y ∈ [0, ½), δ = ½ − y, and suppose

  (D_{t,y})  2[μ_y(t − s) + μ_y(t + s)] ≤ Ψ(s) + Ψ(−s)  for every s ≥ 0.

Then for every w ∈ Σ_∞ — in particular for every L > 0 and every w ∈ Σ_L —

  4(ŵ ∗ μ_y)(t) ≤ 2∫_ℝ ŵ Ψ ≤ Z(w) ≤ B(w);

equivalently V(t, y; L) ≤ 1 for every L: **no strip-positive cone certificate excludes a zero at height t and depth y, at any bandwidth.** The sufficient one-sided form is 2[μ_y(t − s) + μ_y(t + s)] ≤ Ψ(s) for every s ≥ 0.

*Proof.* By Lemma K the orbit share is 4∫_ℝ ŵ(s) μ_y(t − s) ds. Split the integral at s = 0 and substitute s ↦ −s on the negative half-line, using ŵ(−s) = ŵ(s) (w is even, §0.1):

  4∫_ℝ ŵ(s) μ_y(t − s) ds = 4∫_0^∞ ŵ(s)[μ_y(t − s) + μ_y(t + s)] ds.

On the other side, by (0.4) and the same folding,

  2∫_ℝ ŵ(s) Ψ(s) ds = 2∫_0^∞ ŵ(s)[Ψ(s) + Ψ(−s)] ds.

Since ŵ ≥ 0, (D_{t,y}) integrated against ŵ on [0, ∞) gives 4(ŵ ∗ μ_y)(t) ≤ 2∫ŵΨ. The remaining two inequalities are (0.4) and (0.3) (P(w) ≥ 0), which hold for every w ∈ Σ_∞ by definition of Σ_∞ and for every w ∈ Σ_L by clause 1. A cone certificate at (t, y) would need 4(ŵ ∗ μ_y)(t) > B(w); it therefore does not exist. Nothing in the argument depends on L. ∎

*What the clause says and does not say.* (a) It is a statement about a proof class — the set of all certificates of the cone form — and not about ζ's zeros: whether ζ has a zero at (t, y) is not decided; only that this class of arguments cannot exclude one. (b) It consumes ζ through Ψ: the actual on-line zeros must carry, near t, at least the weight of the hypothetical pair. For an abstract admissible datum (C2 line 14) with on-line part σ the same proof gives the same statement with Ψ_σ in place of Ψ. (c) The factor 2 (D1): at s = t the hypothesis reads 2μ_y(0) + 2μ_y(2t) ≤ Ψ(t) + Ψ(−t), i.e. **2/sin(πδ) ≤ Ψ(t)** up to terms below 10⁻¹⁹ (Lemma P(iii) at ξ = 2t ≥ 56 and the bound on Ψ(−t) of §0.4). Since 2/sin(πδ) ≥ 2 for every δ ∈ (0, ½], the clause can only apply where Ψ(t) ≥ 2 — two on-line zeros' worth of smoothed density — which is the honest content of "a pair weighs at least a double". (d) Sign of the measure: the whole argument is the comparison of two nonnegative kernels integrated against a nonnegative ŵ; no positivity of anything is asserted beyond what the cone already carries (zoo IV.1's containment, §7).

---
