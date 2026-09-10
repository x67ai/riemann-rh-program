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

## §4 Clause 7 — the de la Vallée Poussin element, its membership in Σ_∞, and its certified constant

Fix t > 0 and a > ½; write σ := ½ + a = 1 + η with η := a − ½ > 0. The **de la Vallée Poussin element** is

  w_{a,t}(u) := e^{−a|u|} cosh(u/2) (3 + 4cos tu + cos 2tu) = 2e^{−a|u|} cosh(u/2)(1 + cos tu)²,   g_{a,t} := w_{a,t}/cosh(u/2) = e^{−a|u|} q(tu),  q(θ) := 3 + 4cos θ + cos 2θ.

Write π_b(ξ) := 2b/(b² + ξ²) (b > 0) for the Poisson kernel, c_0 := 3, c_{±1} := 2, c_{±2} := ½, and d := (3, 4, 1).

**Lemma E (the identity for the de la Vallée Poussin element).** (i) w_{a,t} ≥ 0 and ŵ_{a,t}(ξ) = ½ Σ_{k=−2}^{2} c_k [π_{a−½}(ξ + kt) + π_{a+½}(ξ + kt)] > 0; so w_{a,t} satisfies the two cone inequalities with no support restriction. (ii) For |Im z| ≤ ½, ĝ_{a,t}(z) = Σ_k c_k π_a(z + kt), and |ĝ_{a,t}(z)| ≤ 2a·(12/η²)·(1 + |z|²)^{−1}·(1 + 5t²) uniformly on the strip (any such polynomial-in-t bound suffices). (iii) The identity (0.3) holds for w_{a,t} with every sum absolutely convergent:

  Σ_ρ m_ρ ĝ_{a,t}(γ(ρ)) = 2ŵ_{a,t}(0) − P(w_{a,t}) + Σ_{j=0}^{2} d_j [Re ψ(s_j/2) − log π],  s_j := σ + ijt,

so w_{a,t} ∈ Σ_∞, and B(w_{a,t}) = Σ_{j=0}^{2} d_j [ 2Re(1/(s_j − 1) + 1/s_j) + Re ψ(s_j/2) − log π ].

*Proof.* (i) Nonnegativity: e^{−a|u|}cosh(u/2) > 0 and q(θ) = 2(1 + cos θ)² ≥ 0. Transform: e^{−a|u|}cosh(u/2) = ½[e^{−(a−½)|u|} + e^{−(a+½)|u|}], the transform of e^{−b|u|} is π_b (b > 0), and multiplying by cos(ktu) = ½(e^{iktu} + e^{−iktu}) shifts the transform to ±kt; collecting the coefficients of q gives the stated sum of five Poisson kernels at ξ + kt with the positive weights c_k, hence ŵ > 0. (`verify/kernel_lemmas.py` checks the formula against quadrature at two frequencies and the sign on a grid.)
(ii) ∫ e^{−a|u|} e^{izu} du = 1/(a − iz) + 1/(a + iz) = π_a(z) for |Im z| < a, and the cos(ktu) factors shift z to z ± kt. For |Im z| ≤ ½ < a write z + kt = x − iy with |y| ≤ ½: a² + (x − iy)² = (a + y + ix)(a − y − ix) has modulus √((a+y)² + x²)·√((a−y)² + x²) ≥ (a − ½)·√((a − ½)² + x²) ≥ (η²/√2)·√(1 + x²)/max(1, 1/η)… — a cleaner sufficient bound: |a² + (x − iy)²| ≥ η√(η² + x²) ≥ (η²/√2)·min(1, 1/η)·√(1 + x²) ≥ (η²/(√2 max(1, η)))√(1 + x²), and √(1 + x²) ≥ √(1 + |z|²)/(1 + 2t) since |x| ≥ |z| − 2t − ½ is not the right direction; use instead 1 + |z|² ≤ 2(1 + x²) + 2(2t + ½)² ≤ (2 + 2(2t+½)²)(1 + x²). Hence |π_a(z + kt)| ≤ 2a·√2·max(1, η)·(2 + 2(2t + ½)²)/(η²(1 + |z|²)) — the precise constant is immaterial; what matters is the uniform decay (1 + |z|²)^{−1} on the strip.
(iii) Approximation from within C²_c. Let φ ∈ C²_c be even, φ ≥ 0, ∫φ = 1, supp φ ⊂ [−1, 1], φ_ε := ε^{−1}φ(·/ε), and let χ ∈ C²_c be even with 0 ≤ χ ≤ 1, χ = 1 on [−1, 1], supp χ ⊂ [−2, 2], χ_n := χ(·/n). Put g_{n,ε} := (g ∗ φ_ε)·χ_n with g := g_{a,t}. Then g_{n,ε} ∈ C²_c (the mollification is C^∞ and χ_n is C²_c), so clause 1's formal input gives Σ_ρ m_ρ ĝ_{n,ε}(γ(ρ)) = literatureRHS(g_{n,ε}). Let ε → 0 and then n → ∞ on both sides.
 *Zero side.* ĝ_{n,ε} = (1/2π)(ĝ·φ̂_ε) ∗ χ̂_n where φ̂_ε(z) = φ̂(εz) and χ̂_n(ξ) = nχ̂(nξ). On |Im z| ≤ ½ and ε ≤ 1, |φ̂(εz)| ≤ ∫φ(u)e^{ε|Im z||u|}du ≤ e^{1/2}, and φ̂(εz) → 1 pointwise; χ̂ ∈ L¹ (χ ∈ C² compactly supported gives χ̂(ξ) = O(ξ^{−2})), so (1/2π)|χ̂_n| is an approximate identity with ∫(1/2π)|χ̂_n| = (1/2π)‖χ̂‖₁ =: C_χ independent of n, and the convolution of a function bounded by C/(1 + |x|²) with such a family is bounded by C′/(1 + |x|²) uniformly in n (for |x| ≤ 1 trivially; for |x| ≥ 1 split the convolution at |ξ| ≤ |x|/2 — where 1 + |x − ξ|² ≥ 1 + |x|²/4 — and |ξ| > |x|/2, where ∫_{|ξ| > |x|/2}|χ̂_n| = ∫_{|ξ′| > n|x|/2}|χ̂| ≤ C″/(n|x|) ≤ C″/|x| ≤ 2C″/√(1+|x|²)·… — a bound C′/(1 + |x|) suffices? No: summability over zeros needs a bound in x = Re γ(ρ) integrable against the zero density, and Σ_ρ 1/(1 + |γ(ρ)|) diverges; use instead the exact form: for |ξ| > |x|/2, |χ̂_n(ξ)| = n|χ̂(nξ)| ≤ n·C₂/(nξ)² ≤ 4C₂/(n x²), so that part of the convolution is ≤ sup|ĝφ̂_ε|·(1/2π)∫_{|ξ|>|x|/2}|χ̂_n| ≤ C‴/(n|x|)·…). To keep the argument short and fully explicit we use a different but equivalent device: since ĝ(z) is bounded by C/(1 + |Re z|²) on the strip and χ̂_n(ξ) = nχ̂(nξ) with χ̂(ξ) = O((1 + |ξ|)^{−2}), the standard estimate for the convolution of a (1 + |x|²)^{−1}-bounded function with an approximate identity whose members are bounded by n·C₂(1 + n|ξ|)^{−2} gives |ĝ_{n,ε}(x − iy)| ≤ C₃/(1 + x²) with C₃ independent of n ≥ 1 and ε ≤ 1 (split at |ξ| ≤ |x|/2 as above; on |ξ| > |x|/2 the kernel is ≤ n C₂ (1 + n|x|/2)^{−2} ≤ 4C₂/(n x²) ≤ 4C₂/x², and the ĝ-factor is bounded, so the integral over that range is ≤ (4C₂/x²)·‖ĝφ̂_ε‖_∞·(measure of the effective support, which is ≤ 2·(support length of ĝ's bound…)) — the ĝ-factor is integrable: ∫|ĝ(x − ξ − iy)|dξ ≤ Cπ, so that part is ≤ 4C₂Cπ/x²). Hence |ĝ_{n,ε}(γ(ρ))| ≤ C₃(1 + (Re γ(ρ))²)^{−1} uniformly, and Σ_ρ m_ρ(1 + (Re γ(ρ))²)^{−1} < ∞ by the formal local count (§1.1: at most 5.4·10⁸ log(k + 3) zeros with Re γ ∈ (k, k + 1]). Since ĝ_{n,ε}(z) → ĝ(z) pointwise on the strip (first ε → 0: dominated convergence in the u-integral; then n → ∞: χ_n → 1 pointwise with |g χ_n| ≤ |g| ∈ L¹(e^{|u|/2}du)), dominated convergence for the zero sum gives Σ_ρ m_ρ ĝ_{n,ε}(γ(ρ)) → Σ_ρ m_ρ ĝ(γ(ρ)), absolutely convergent.
 *Pole terms.* ĝ_{n,ε}(±i/2) → ĝ(±i/2) = π_a-sums at ±i/2 + kt (dominated convergence: |g_{n,ε}(u)|e^{|u|/2} ≤ ‖q‖_∞ e^{εa}e^{−(a−½)|u|}, integrable).
 *Prime term.* Σ_n Λ(n) n^{−1/2}(g_{n,ε}(log n) + g_{n,ε}(−log n)) → Σ_n Λ(n)n^{−1/2}·2g(log n) = 2Σ_n Λ(n) n^{−σ} q(t log n) = P(w_{a,t}): the terms are dominated by 2‖q‖_∞ e^{εa}Λ(n) n^{−1/2−a}, summable since a > ½ (Σ Λ(n)n^{−σ} = −ζ′/ζ(σ) < ∞ for σ > 1), and converge termwise.
 *Archimedean term.* (1/2π)∫ĝ_{n,ε}(r)[Re ψ(¼ + ir/2) − log π]dr → (1/2π)∫ĝ(r)[…]dr by dominated convergence (the integrand is bounded by C₃(1 + r²)^{−1}·C₄ log(2 + |r|)). The limit is evaluated by Lemma A below: (1/2π)∫π_a(r + kt)[Re ψ(¼ + ir/2) − log π]dr = Re ψ((σ + ikt)/2) − log π, and Σ_k c_k F(k) = Σ_j d_j F(j) for F even in k.
 Collecting: Σ_ρ m_ρ ĝ(γ(ρ)) = ĝ(i/2) + ĝ(−i/2) − P(w_{a,t}) + Σ_j d_j[Re ψ(s_j/2) − log π], and ĝ(i/2) + ĝ(−i/2) = Σ_k c_k [π_a(kt + i/2) + π_a(kt − i/2)] = Σ_k c_k·2Re[1/(a − ½ + ikt) + 1/(a + ½ − ikt)] = Σ_j d_j·2Re[1/(s_j − 1) + 1/s_j], using π_a(z) = 1/(a − iz) + 1/(a + iz). Every term of the zero sum is nonnegative (Lemma K, which used only ŵ ≥ 0, μ_y ≥ 0 and the evenness of w), so w_{a,t} ∈ Σ_∞. ∎

*Remark.* Divided by 2, (iii) is the classical partial-fraction identity Σ_ρ Re 1/(s − ρ) − Re ζ′/ζ(s) = Re[1/(s − 1) + 1/s] + ½Re ψ(s/2) − ½log π at s = s_j, weighted by d_j — the Hadamard-product formula for ξ′/ξ [recalled as the textbook location, e.g. Davenport, *Multiplicative Number Theory*, Ch. 12; not used: the identity is derived above from the formal input]. The 3-4-1 combination of −Re ζ′/ζ is the prime share P(w_{a,t})/2 ≥ 0 — the strip-positive cone contains the de la Vallée Poussin argument as C2 line 16(a) says, and axiom P is what makes the 3-4-1 positivity available.

**Lemma A (Poisson evaluation of the archimedean integral).** For a > 0 and x ∈ ℝ,
  (1/2π)∫_ℝ π_a(r − x)[Re ψ(¼ + ir/2) − log π] dr = Re ψ((½ + a + ix)/2) − log π.

*Proof.* Gauss's integral ψ(z) = ∫_0^∞ (e^{−τ}/τ − e^{−zτ}/(1 − e^{−τ})) dτ, valid for Re z > 0 (DLMF 5.9.12 [recalled as the location; the formula is checked numerically to 10⁻¹⁵ at four points in `verify/kernel_lemmas.py`, and it is the one classical representation this note uses]). Hence Re ψ(¼ + ir/2) = ∫_0^∞ (e^{−τ}/τ − e^{−τ/4}cos(rτ/2)/(1 − e^{−τ})) dτ = ψ(¼) + ∫_0^∞ e^{−τ/4}(1 − cos(rτ/2))/(1 − e^{−τ}) dτ, the second integrand being nonnegative and at most e^{−τ/4}·min(2, r²τ²/8)/(1 − e^{−τ}), integrable in τ with an integral that grows like log(2 + |r|). Multiply by (1/2π)π_a(r − x) and integrate in r; Tonelli (nonnegative integrand) allows the order to be exchanged, and (1/2π)∫π_a(r − x)cos(rτ/2)dr = e^{−aτ/2}cos(xτ/2) (the transform of the Poisson kernel: ∫π_a(r)e^{irξ}dr = 2πe^{−a|ξ|}; checked in `verify/kernel_lemmas.py`). Therefore the left side equals ψ(¼) + ∫_0^∞ e^{−τ/4}(1 − e^{−aτ/2}cos(xτ/2))/(1 − e^{−τ})dτ − log π = ∫_0^∞(e^{−τ}/τ − e^{−(¼ + a/2 + ix/2)τ}/(1 − e^{−τ}))dτ − log π + (imaginary part zero) = Re ψ(¼ + a/2 + ix/2) − log π, by Gauss's integral again at z = (½ + a + ix)/2. ∎ (Numerical record: the identity holds to 10⁻¹⁰ at (a, x) ∈ {(0.6, 0), (0.6, 30), (1.0, 100), (0.55, 1000), (1.5, 0)}, `kernel_lemmas_run.log`.)

**Lemma D (a digamma bound).** For Re z > 0 and Im z ≠ 0, |Re ψ(z) − log|z|| ≤ 3/(2|Im z|). Moreover ψ is increasing on (0, ∞), and ψ(1) = −γ_E = −0.5772156649… .

*Proof.* Gauss's integral and the complex Frullani integral log z = ∫_0^∞ (e^{−τ} − e^{−zτ})/τ dτ (Re z > 0) give ψ(z) − log z = −∫_0^∞ e^{−zτ} h(τ) dτ with h(τ) := 1/(1 − e^{−τ}) − 1/τ. One has h(0⁺) = ½, h(∞) = 1 and h′(τ) = 1/τ² − 1/(4 sinh²(τ/2)) ≥ 0 (sinh(τ/2) ≥ τ/2), so 0 < h ≤ 1 and ∫_0^∞ h′ = ½. Write z = x + iy, G(τ) := e^{−xτ}h(τ). Integrating by parts once, ∫_0^∞ G(τ)cos(yτ)dτ = −(1/y)∫_0^∞ G′(τ) sin(yτ)dτ (the boundary term G(τ)sin(yτ)/y vanishes at both ends), and ∫_0^∞|G′| ≤ ∫ e^{−xτ}h′ + x∫e^{−xτ}h ≤ ½ + x·(1/x) = 3/2. Hence |Re(ψ(z) − log z)| ≤ 3/(2|y|), and Re log z = log|z|. Monotonicity of ψ on (0, ∞): ψ′(x) = Σ_{n≥0}(x + n)^{−2} > 0. ψ(1) = −γ_E is the value of the digamma function at 1 (computed: `kernel_lemmas_run.log`). ∎ (Numerical record: the ratio |Re ψ(z) − log|z||/(3/(2|Im z|)) is at most 0.168 on the grid Re z ∈ {¼, ½, ¾, 1}, |Im z| ∈ {1, …, 10⁶}.)

**Theorem R1, clause 7 (sharpness: the layer is nonempty).** For every t ≥ 28 and every nontrivial zero β + it of ζ,

  1 − β ≥ 0.143593 / (5ℓ + C_t),  ℓ := log(t/2π),  C_t := 1.5274 + 13.5/t + 34/t²,

and in particular 1 − β > 1/(34.8205 log t) — the de la Vallée Poussin element w_{a,t} with η = a − ½ = (4√3 − 6)/(5ℓ + C_t) is a cone certificate at every (t, ½ − δ) with δ < 0.143593/(5ℓ + C_t). Here 0.143593… = (2/√3 − 1)(4√3 − 6) and 34.8205… = 5/(2/√3 − 1)(4√3 − 6). So the cone's reach at height t contains the layer {1 − σ < c/log t} with the certified c = 0.0287187 = 1/34.8205, and by clause 4 (resp. 5) it is contained in {1 − σ < (4 + o(1))/log t} where Ψ has mean strength (resp. in {1 − σ < (66.41 + o(1))/log t} unconditionally): **the cone's reach is a de la Vallée Poussin-shaped band between c/log t and C/log t** — the "PairCeiling analog" of C2 line 74.

*Proof.* Suppose ζ(β + it) = 0 with t ≥ 28. If β ≤ ½ then 1 − β ≥ ½ and there is nothing to prove (0.1436/(5ℓ + C_t) < ½ for t ≥ 28). So let β > ½, y := β − ½ ∈ (0, ½), δ := 1 − β. Take σ := 1 + η with 0 < η ≤ 1 to be chosen and a := σ − ½ > ½ > y. By Lemma E, w := w_{a,t} ∈ Σ_∞, so the identity (0.3) holds and every zero's share is nonnegative; the orbit of β + it is among the zeros, hence

  4 Re ĝ(t − iy) ≤ Z(w) ≤ B(w).   (7.1)

*Lower bound for the orbit share.* By Lemma E(ii), Re ĝ(t − iy) = Σ_k c_k Re π_a(t + kt − iy), and Re π_a(x − iy) = (a + y)/((a + y)² + x²) + (a − y)/((a − y)² + x²) > 0 (from π_a(z) = 1/(a − iz) + 1/(a + iz) at z = x − iy). Keeping only the k = −1 term (x = 0, coefficient c_{−1} = 2): 4Re ĝ(t − iy) ≥ 4·2·[1/(a + y) + 1/(a − y)] ≥ 8/(a − y) = 8/(σ − β) = 8/(η + δ).
*Upper bound for the budget.* By Lemma E(iii), B(w) = Σ_{j=0}^2 d_j b_j with b_j := 2Re(1/(s_j − 1) + 1/s_j) + Re ψ(s_j/2) − log π, s_j = σ + ijt.
 – j = 0: b_0 = 2/η + 2/σ + ψ(σ/2) − log π ≤ 2/η + 2 + ψ(1) − log π = 2/η + 0.278054…, using σ ≥ 1 and ψ(σ/2) ≤ ψ(1) for σ ≤ 2 (Lemma D, monotonicity); we use b_0 ≤ 2/η + 0.2781.
 – j ∈ {1, 2}: 2Re(1/(s_j − 1) + 1/s_j) = 2η/(η² + j²t²) + 2σ/(σ² + j²t²) ≤ (2η + 2σ)/(j²t²) ≤ 6/(j²t²); Re ψ(s_j/2) ≤ log|s_j/2| + 3/(2·(jt/2)) = ½log((σ² + j²t²)/4) + 3/(jt) ≤ log(jt/2) + σ²/(2j²t²) + 3/(jt) ≤ log(jt/2) + 2/(j²t²) + 3/(jt) (Lemma D with Im(s_j/2) = jt/2, and log(1 + x) ≤ x). So b_j ≤ log(jt/2π) + 3/(jt) + 8/(j²t²).
 Summing with d = (3, 4, 1): B(w) ≤ 6/η + 3·0.2781 + 4ℓ + (ℓ + log 2) + 4(3/t + 8/t²) + (3/(2t) + 2/t²) = 6/η + 5ℓ + 0.8343 + 0.6932 + 13.5/t + 34/t² = 6/η + 5ℓ + C_t. (`verify/dlvp_constant.py` checks b_j and B against their exact values at t ∈ {28, 10², 10⁴, 10⁶}: the bounds hold with the expected slack.)
*Optimization.* (7.1) gives 8/(η + δ) ≤ 6/η + M with M := 5ℓ + C_t, i.e. δ ≥ 8η/(6 + ηM) − η =: f(η). The function f is maximized at 6 + ηM = √48 = 4√3, i.e. η* = (4√3 − 6)/M = 0.928203…/M, where f(η*) = η*(8/(4√3) − 1) = (2/√3 − 1)(4√3 − 6)/M = 0.143593…/M. The constraint η* ≤ 1 holds because M ≥ 5 log(28/2π) + 1.5274 > 0.93 for t ≥ 28. This proves the displayed bound. Finally 5ℓ + C_t = 5 log t − 5 log 2π + C_t ≤ 5 log t − 9.189 + 1.5274 + 13.5/28 + 34/784 < 5 log t, so 1 − β > 0.143593/(5 log t) = 1/(34.8205 log t). ∎

*Numerical record (`verify/dlvp_constant_run.log`).* The element's exact reach — the largest δ certified by w_{a,t} at the best η, with B(w) evaluated exactly (mpmath digamma) and the full orbit share — is δ_max·log t = 0.0653, 0.0499, 0.0402, 0.0347, 0.0314 at t = 10³, 10⁴, 10⁶, 10¹⁰, 10²⁰, against the proved 0.0369, 0.0344, 0.0323, 0.0308, 0.0297 and the asymptotic 1/34.82 = 0.0287: the proved bound loses only the lower-order terms. Known sharper explicit zero-free regions of the same 3-4-1 shape — 1 − β ≥ 1/(5.573412 log t) (Mossinghoff–Trudgian 2015) `[recalled, unverified; PRICING.md §4 cites it from an arXiv listing; not used]` — are obtained with better trigonometric polynomials and sharper bounds for the Gamma factor; they are other elements of the same cone, and clauses 2–5 bound all of them alike.

---

## §5 Clause 6 — the parameter pin (KICKSTART 10(h))

**Theorem R1, clause 6.** Let p ∈ Σ_∞ ∩ L¹ with p̂ ∈ L¹ (so 0 ≤ p(u) ≤ p(0)), let q(θ) = Σ_{k=0}^{K} q_k cos kθ be a cosine polynomial with q ≥ 0 and all q_k ≥ 0, and let w := p(u)·q(tu). Then w ≥ 0 and ŵ ≥ 0. For every y ∈ [0, ½), δ = ½ − y, and every L′ > 0, the part of the orbit share 4(ŵ ∗ μ_y)(t) = 4∫_ℝ p(u)q(tu)k_y(u)cos(tu)du coming from |u| > L′ is at most

  16 p(0) ‖q‖_∞ e^{−δL′}/δ.

In particular, for p ∈ Σ_L with L ≥ L′ ≥ 2/δ, the orbit share of w equals the same integral restricted to [−L′, L′] up to an error ≤ 16 p(0)‖q‖_∞ e^{−δL′}/δ ≤ 16 e^{−2} p(0)‖q‖_∞/δ, and enlarging the support beyond L′ changes the orbit share by no more than that: **the orbit share is pinned at bandwidth ≍ 1/δ by the strip-positivity factor k_y(u) = cosh(yu)/cosh(u/2) ≤ 2e^{−δ|u|}.**

*Proof.* w ≥ 0 as a product of nonnegative functions; ŵ = (1/2π)p̂ ∗ (transform of q(t·)) = Σ_k (q_k/2)[p̂(· − kt) + p̂(· + kt)] (with the k = 0 term counted once) ≥ 0 since p̂ ≥ 0 and q_k ≥ 0. The orbit share is 4Re ĝ(t − iy) = 4∫ p(u)q(tu)k_y(u)cos(tu)du by the computation in Lemma K (which used only the evenness of w). On |u| > L′: |p(u)q(tu)k_y(u)cos(tu)| ≤ p(0)‖q‖_∞·2e^{−δ|u|} (Lemma P(iv) and 0 ≤ p ≤ p(0), §0.1), and ∫_{|u|>L′} 2e^{−δ|u|}du = 4e^{−δL′}/δ. Multiply by 4. ∎

*Reading (10(h)).* The pin is a property of the orbit share only. The budget B(w) is not pinned in this way (its archimedean part reads ŵ near ξ = 0, which depends on all of p); what the clause records is that no bandwidth beyond ≍ 1/δ can raise the numerator of a certificate: a certificate at depth y must be won with the mass of p inside |u| ≲ 1/δ, which is the mechanism PRICING-next-unit §1.1(a) computed for the height-t family (∫p/p(0) ≤ 2/δ). Together with clause 7 it explains why the classical de la Vallée Poussin choice a − ½ = η ≍ 1/log t (bandwidth 1/η) is the right scale: it is the scale of the layer.

---
