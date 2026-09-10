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

*Proof.* (i) cosh(yu) e^{−iuξ} = ½[e^{−iu(ξ + iy)} + e^{−iu(ξ − iy)}], and the transform of 1/cosh(u/2) at a complex frequency ζ with |Im ζ| < ½ is 2π/cosh(πζ) (the standard integral ∫ e^{−iuζ}/cosh(u/2) du = 2π/cosh(πζ), which is the analytic continuation of the real-frequency formula, the integral converging absolutely for |Im ζ| < ½; the resulting closed form is checked by Fourier inversion — ∫μ_y(ξ)cos(uξ)dξ = k_y(u) to 1.3·10⁻¹⁶ at y ∈ {0, 0.25, 0.4, 0.45, 0.49}, u ∈ {0, 0.7, 3, 12} — in `verify/kernel_lemmas.py`). Hence μ_y(ξ) = ½[1/cosh(π(ξ + iy)) + 1/cosh(π(ξ − iy))] = Re[1/cosh(π(ξ + iy))]. Now cosh(πξ + iπy) = cosh πξ cos πy + i sinh πξ sin πy, whose modulus squared is cosh²πξ cos²πy + sinh²πξ sin²πy = cosh²πξ − sin²πy = ½(cosh 2πξ + cos 2πy); taking the real part of the reciprocal gives the closed form. Positivity: cos πy > 0 for y < ½ and cosh²πξ − sin²πy ≥ 1 − sin²πy > 0. Monotonicity: with c := cosh πξ and s := sin πy, μ_y = cos(πy)·c/(c² − s²), and d/dc [c/(c² − s²)] = −(c² + s²)/(c² − s²)² < 0 while c is strictly increasing in |ξ|.
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

**D6 (clause 5 landed).** Both fetch-list sources were located on arXiv by title (arXiv API query on the exact titles) and read at the page in-session (§3, §6): Hasanalizade–Shen–Wong arXiv:2107.06506v1 (PDF SHA-256 3fc4c89f49249924e61cb0d289d81559faed53fcbb838628ea32dc7ec6f89fbf) and Trudgian arXiv:1208.5846v2 (SHA-256 274b3a0a14d79400f23505ede664a2f77b0a6ad7278245d25ec6e06169e2a303); the sponsor's copies delivered during the session as `fetched-r6/r6-02-hasanalizade-shen-wong-2022-counting-zeros-arXiv2107.06506v1.pdf` and `fetched-r6/r6-01-trudgian-2014-argument-II-arXiv1208.5846v2.pdf` have the same hashes. The passages read are excerpted in `verify/sources-read-excerpts.txt`. Trudgian's arXiv v2 carries a Mathematics of Computation header; the fetch list's recalled venue (J. Number Theory 134) is HSW's Table 1 attribution for the 2014 journal version and is not verified here. Clause 5 is therefore stated and proved with explicit constants, not deferred. Trudgian's arXiv v2 constants (0.111, 0.275, 2.450) differ from the journal constants HSW's Table 1 attributes to Trudgian 2014 (0.1120, 0.2780, 3.3850); nothing here uses Trudgian's constants, only his identity (2.5) and the Platt-database bound HSW quote as (1.7).

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

**Lemma E (the identity for the de la Vallée Poussin element).** (i) w_{a,t} ≥ 0 and ŵ_{a,t}(ξ) = ½ Σ_{k=−2}^{2} c_k [π_{a−½}(ξ + kt) + π_{a+½}(ξ + kt)] > 0; so w_{a,t} satisfies the two cone inequalities with no support restriction. (ii) For |Im z| ≤ ½, ĝ_{a,t}(z) = Σ_k c_k π_a(z + kt), and |ĝ_{a,t}(z)| ≤ 16a(2 + 12t²)/(min(1, η²)(1 + |z|²)) uniformly on the strip |Im z| ≤ ½ (t ≥ 1). (iii) The identity (0.3) holds for w_{a,t} with every sum absolutely convergent:

  Σ_ρ m_ρ ĝ_{a,t}(γ(ρ)) = 2ŵ_{a,t}(0) − P(w_{a,t}) + Σ_{j=0}^{2} d_j [Re ψ(s_j/2) − log π],  s_j := σ + ijt,

so w_{a,t} ∈ Σ_∞, and B(w_{a,t}) = Σ_{j=0}^{2} d_j [ 2Re(1/(s_j − 1) + 1/s_j) + Re ψ(s_j/2) − log π ].

*Proof.* (i) Nonnegativity: e^{−a|u|}cosh(u/2) > 0 and q(θ) = 2(1 + cos θ)² ≥ 0. Transform: e^{−a|u|}cosh(u/2) = ½[e^{−(a−½)|u|} + e^{−(a+½)|u|}], the transform of e^{−b|u|} is π_b (b > 0), and multiplying by cos(ktu) = ½(e^{iktu} + e^{−iktu}) shifts the transform to ±kt; collecting the coefficients of q gives the stated sum of five Poisson kernels at ξ + kt with the positive weights c_k, hence ŵ > 0. (`verify/kernel_lemmas.py` checks the formula against quadrature at two frequencies and the sign on a grid.)
(ii) ∫ e^{−a|u|} e^{izu} du = 1/(a − iz) + 1/(a + iz) = π_a(z) for |Im z| < a, and the cos(ktu) factors shift z to z ± kt. For |Im z| ≤ ½ write z + kt = x − iy with |y| ≤ ½. Then a² + (x − iy)² = (a + y + ix)(a − y − ix), and both factors have modulus at least √(η² + x²) because a ± y ≥ a − ½ = η; so |a² + (x − iy)²| ≥ η² + x² ≥ min(1, η²)(1 + x²) (if η ≥ 1 use η² ≥ 1; if η < 1 use x² ≥ η²x²). Hence |π_a(z + kt)| ≤ 2a/(min(1, η²)(1 + x²)). Finally |z| ≤ |x| + 2t + ½ gives 1 + |z|² ≤ 1 + 2x² + 2(2t + ½)² = 1.5 + 2x² + 8t² + 4t ≤ (2 + 12t²)(1 + x²) for t ≥ 1 (the difference of the two sides is 0.5 + 4t² − 4t + 12t²x² ≥ 0). Summing over k with Σ_k c_k = 8 gives |ĝ_{a,t}(z)| ≤ 16a(2 + 12t²)/(min(1, η²)(1 + |z|²)) for t ≥ 1, which is the range used (t ≥ 28).
(iii) Approximation from within C²_c. Let φ ∈ C²_c be even, φ ≥ 0, ∫φ = 1, supp φ ⊂ [−1, 1], φ_ε := ε^{−1}φ(·/ε), and let χ ∈ C²_c be even with 0 ≤ χ ≤ 1, χ = 1 on [−1, 1], supp χ ⊂ [−2, 2], χ_n := χ(·/n). Put g_{n,ε} := (g ∗ φ_ε)·χ_n with g := g_{a,t}. Then g_{n,ε} ∈ C²_c (g ∗ φ_ε is C² because φ ∈ C²_c and g is continuous with exponential decay; χ_n is C²_c), so clause 1's formal input gives Σ_ρ m_ρ ĝ_{n,ε}(γ(ρ)) = literatureRHS(g_{n,ε}). Let ε → 0 and then n → ∞ on both sides.
 *Zero side.* ĝ_{n,ε} = (1/2π)(ĝ·φ̂_ε) ∗ χ̂_n, where φ̂_ε(z) = φ̂(εz) and χ̂_n(ξ) = nχ̂(nξ). On |Im z| ≤ ½ and ε ≤ 1, |φ̂(εz)| ≤ ∫φ(u)e^{ε|Im z||u|}du ≤ e^{1/2}, so by (ii) the function (ĝφ̂_ε)(x − iy) is bounded by F(x) := C₅/(1 + x²) with C₅ := e^{1/2}·16a(2 + 12t²)/min(1, η²), uniformly in ε ≤ 1 and |y| ≤ ½. Since χ ∈ C²_c, |χ̂(ξ)| ≤ min(‖χ‖₁, ‖χ″‖₁/ξ²) ≤ C₂/(1 + ξ²) with C₂ := ‖χ‖₁ + ‖χ″‖₁, hence |χ̂_n(ξ)| ≤ nC₂/(1 + n²ξ²) and ∫|χ̂_n| = ∫|χ̂| ≤ πC₂. Claim: (1/2π)∫F(x − ξ)|χ̂_n(ξ)|dξ ≤ 6C₂C₅/(1 + x²) for all x and all n ≥ 1. For |x| < 1 the left side is at most (1/2π)·C₅·πC₂ = C₂C₅/2 ≤ C₂C₅/(1 + x²). For |x| ≥ 1 split at |ξ| = |x|/2: where |ξ| ≤ |x|/2 one has |x − ξ| ≥ |x|/2, so F(x − ξ) ≤ 4C₅/(1 + x²) and that part is ≤ (1/2π)·4C₅·πC₂/(1 + x²) = 2C₂C₅/(1 + x²); where |ξ| > |x|/2 one has |χ̂_n(ξ)| ≤ nC₂/(1 + n²x²/4) ≤ 4C₂/(nx²) ≤ 8C₂/(1 + x²), and ∫F = πC₅, so that part is ≤ (1/2π)·8C₂·πC₅/(1 + x²) = 4C₂C₅/(1 + x²). This proves the claim, i.e. |ĝ_{n,ε}(γ(ρ))| ≤ 6C₂C₅(1 + (Re γ(ρ))²)^{−1} uniformly in n ≥ 1, ε ≤ 1. The formal local count (§1.1) gives at most 5.4·10⁸ log(k + 3) zeros with Re γ(ρ) ∈ (k, k + 1] for each integer k, so Σ_ρ m_ρ(1 + (Re γ(ρ))²)^{−1} < ∞. Pointwise, ĝ_{n,ε}(z) → ĝ(z) on the strip: g ∗ φ_ε → g pointwise as ε → 0 (g is continuous), |(g ∗ φ_ε)χ_n| ≤ ‖q‖_∞e^{εa}e^{−a|u|}, and |e^{izu}| ≤ e^{|u|/2}, so dominated convergence in the u-integral gives ĝ_{n,ε}(z) → ∫gχ_n e^{izu}du as ε → 0 and then → ĝ(z) as n → ∞. Dominated convergence for the zero sum then gives Σ_ρ m_ρ ĝ_{n,ε}(γ(ρ)) → Σ_ρ m_ρ ĝ(γ(ρ)), the limit sum converging absolutely.
 *Pole terms.* ĝ_{n,ε}(±i/2) → ĝ(±i/2) = π_a-sums at ±i/2 + kt (dominated convergence: |g_{n,ε}(u)|e^{|u|/2} ≤ ‖q‖_∞ e^{εa}e^{−(a−½)|u|}, integrable).
 *Prime term.* Σ_n Λ(n) n^{−1/2}(g_{n,ε}(log n) + g_{n,ε}(−log n)) → Σ_n Λ(n)n^{−1/2}·2g(log n) = 2Σ_n Λ(n) n^{−σ} q(t log n) = P(w_{a,t}): the terms are dominated by 2‖q‖_∞ e^{εa}Λ(n) n^{−1/2−a}, summable since a > ½ (Σ Λ(n)n^{−σ} = −ζ′/ζ(σ) < ∞ for σ > 1), and converge termwise.
 *Archimedean term.* (1/2π)∫ĝ_{n,ε}(r)[Re ψ(¼ + ir/2) − log π]dr → (1/2π)∫ĝ(r)[Re ψ(¼ + ir/2) − log π]dr by dominated convergence (the integrand is bounded by C₃(1 + r²)^{−1}·C₄ log(2 + |r|)). The limit is evaluated by Lemma A below: (1/2π)∫π_a(r + kt)[Re ψ(¼ + ir/2) − log π]dr = Re ψ((σ + ikt)/2) − log π, and Σ_k c_k F(k) = Σ_j d_j F(j) for F even in k.
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

## §3 Clause 3 — localization, and Theorem G (the gap condition holds for ζ at every height)

Put ε₃(δ) := 4.03 sin(πδ) e^{−4π} (≤ 4.03e^{−4π} = 1.4054·10⁻⁵ for every δ ∈ (0, ½]; `verify/clause5_constants_run.log`).

**Theorem R1, clause 3 (localization clause).** Let t ≥ 28, y ∈ [0, ½), δ = ½ − y. Suppose
 (i) 2/sin(πδ) + ε₃(δ) ≤ min_{|s − t| ≤ 4} Ψ(s), and
 (ii) every two consecutive positive ordinates of on-line zeros of ζ differ by at most G, where 1/cosh(πG/2) ≥ ε₃(δ) (G ≤ 7.554 suffices for every δ).
Then the hypothesis (D_{t,y}) of clause 2 holds, and no cone certificate excludes a zero at (t, y) at any bandwidth. **For ζ, (ii) holds unconditionally at every height with G = 7.5 (Theorem G below), so for ζ clause 3 reduces to (i).**

*Proof.* We verify the one-sided form 2[μ_y(t − s) + μ_y(t + s)] ≤ Ψ(s) for every s ≥ 0, in four ranges. Throughout, Lemma P(iii) gives μ_y(ξ) ≤ c_P sin(πδ)e^{−π|ξ|} with c_P = 2.012 for |ξ| ≥ 1, and Lemma P(i)–(ii) give μ_y ≤ 1/sin(πδ) everywhere. Under (ii), every s ≥ γ₁ lies within G/2 of some ordinate τ, so Ψ(s) ≥ μ_0(s − τ) ≥ 1/cosh(πG/2) ≥ ε₃(δ) there.
 (A) |s − t| ≤ 4. Then s ≥ 24 and t + s ≥ 2t − 4 ≥ 52, so 2μ_y(t − s) ≤ 2/sin(πδ) and 2μ_y(t + s) ≤ 2c_P sin(πδ)e^{−52π} < ε₃(δ). Hence the left side is ≤ 2/sin(πδ) + ε₃(δ) ≤ min_{|s−t|≤4}Ψ ≤ Ψ(s) by (i).
 (B) s ≥ t + 4. Then |t − s| ≥ 4 and t + s ≥ 60: the left side is ≤ 2c_P sin(πδ)[e^{−4π} + e^{−60π}] ≤ 4.024 sin(πδ)e^{−4π}(1 + e^{−56π}) < ε₃(δ) ≤ Ψ(s), the last by (ii) (s ≥ γ₁).
 (C) γ₁ ≤ s ≤ t − 4. Then t − s ≥ 4 and t + s ≥ 1: the left side is ≤ 2c_P sin(πδ)[e^{−π(t−s)} + e^{−π(t+s)}] = 2c_P sin(πδ)e^{−π(t−s)}(1 + e^{−2πs}) ≤ 4.024 sin(πδ)e^{−4π}(1 + e^{−2πγ₁}) < ε₃(δ) ≤ Ψ(s) by (ii). (This is where the contract's "automatic from γ₁" needed the gap condition: the bound Ψ(s) ≥ e^{−π|s − γ₁|} is useless for s far above γ₁; D4.)
 (D) 0 ≤ s ≤ γ₁. Then t − s ≥ t − γ₁ ≥ 13.8 and t + s ≥ 28: the left side is ≤ 2c_P sin(πδ)e^{−π(t−s)}(1 + e^{−2πs}) ≤ 4c_P sin(πδ)e^{−π(t−s)} ≤ 8.05 e^{−π(t−s)}, while Ψ(s) ≥ μ_0(s − γ₁) = 1/cosh(π(γ₁ − s)) ≥ e^{−π(γ₁ − s)}. The inequality 8.05e^{−π(t−s)} ≤ e^{−π(γ₁−s)} is e^{π(t − γ₁)} ≥ 8.05, true for t ≥ γ₁ + log(8.05)/π = 14.80, in particular for t ≥ 28.
 Since Ψ(−s) ≥ 0, the one-sided form implies (D_{t,y}). ∎

**Theorem G (the maximal gap between consecutive zero ordinates).** Every two consecutive positive ordinates γ_n < γ_{n+1} of zeros of ζ satisfy γ_{n+1} − γ_n ≤ 7.5. (The first gap, γ₂ − γ₁ = 21.022040 − 14.134725 = 6.887315, is the largest one below height 2400 — `verify/gaps_first_zeros_run.log`, `verify/normalization_zeta_check_run.log`.)

*Proof.* Write N(T) for the number of zeros with 0 < Im ρ ≤ T (multiplicity counted; both sources use this N). It suffices to show that every interval (T, T + 7.5] with T ≥ γ₁ contains an ordinate, i.e. N(T + 7.5) − N(T) > 0. For any bound |N(x) − M(x)| ≤ R(x) on an interval containing T and T + 7.5, with M(x) := (x/2π)log(x/2πe) + 7/8, one has N(T + 7.5) − N(T) ≥ M(T + 7.5) − M(T) − R(T) − R(T + 7.5) and M(T + 7.5) − M(T) = ∫_T^{T+7.5}(1/2π)log(x/2π)dx ≥ (7.5/2π)log(T/2π) for T ≥ 2π. Three sources, all read at the page on 2026-09-10 (`fetched-r6/`):
 (a) Trudgian, arXiv:1208.5846v2 (`r6-01-…pdf`), inequality (2.5): for T ≥ 1, |N(T) − (T/2π)log(T/2πe) − 7/8| ≤ 0.2/T + |S(T)|; and his (1.2): |S(T)| ≤ 1 for 0 ≤ T ≤ 280, |S(T)| ≤ 2 for 0 ≤ T ≤ 6.8·10⁶ (Trudgian attributes (1.2) to his references [3, 11]: "the statement that Gram's Law holds for all 0 ≤ T ≤ 280 and that Rosser's Rule holds for all 0 ≤ T ≤ 6.8·10⁶", footnote 1). With R = 1 + 0.2/T the count is positive once (7.5/2π)log(T/2π) > 2(1 + 0.2/T), i.e. T ≥ 33.9; with R = 2 + 0.2/T once T ≥ 179.6 — valid up to T + 7.5 ≤ 6.8·10⁶ (`clause5_constants_run.log`, Theorem G (c)).
 (b) Hasanalizade–Shen–Wong, arXiv:2107.06506v1 (`r6-02-…pdf`), Corollary 1.4 (T ≥ e): |S(T)| ≤ 0.1095 log T + 0.2042 log log T + 3.0305 (the second bound of the min); combined with Trudgian's (2.5) the count is positive for all T ≥ 1.22·10⁴ (Theorem G (d)). Independently of Trudgian, HSW's own Corollary 1.2 (T ≥ e): |N(T) − (T/2π)log(T/2πe)| ≤ 0.1038 log T + 0.2573 log log T + 9.3675, which this note uses with the constant term enlarged by 1/8 to E(T) := 0.1038 log T + 0.2573 log log T + 9.4925, so as to cover both the expression of their Theorem 1.1 (1.4), |N(T) − (T/2π)log(T/2πe) + 1/8|, and that of (1.5) — gives positivity for all T ≥ 1.096·10¹⁰ (Theorem G (b)); and HSW's (5.6), for e ≤ T ≤ 30 610 046 000: |N(T) − (T/2π)log(T/2πe) + 1/8| ≤ 2.5167 + 1/(50e) + 1 (from Platt's zero database, their (1.7)), gives positivity for 2304.2 ≤ T ≤ 30 610 046 000 − 7.5 (Theorem G (a)).
 (c) Below T = 33.9 the ordinates are γ₁ = 14.134725, γ₂ = 21.022040, γ₃ = 25.010858, γ₄ = 30.424876, γ₅ = 32.935062, γ₆ = 37.586178 (mpmath.zetazero, `normalization_zeta_check_run.log` and `gaps_first_zeros_run.log`), with gaps 6.887, 3.989, 5.414, 2.510, 4.651 ≤ 7.5.
 Ranges (a) [33.9, 6.8·10⁶ − 7.5], (b) [1.22·10⁴, ∞) and (c) [γ₁, 37.6] cover [γ₁, ∞); the HSW-only chain (c) + first-1900-zeros computation (to height ≈ 2400) + (5.6) [2304.2, 3.06·10¹⁰ − 7.5] + Corollary 1.2 [1.096·10¹⁰, ∞) covers it as well. Either chain proves the theorem. ∎

*Remarks.* (1) Theorem G is far from sharp (the true maximal gap is 6.887 as far as computed, and gaps shrink like 2π/log T on average); it is exactly what clause 3(ii) needs, with room: 1/cosh(7.5π/2) = 1.530·10⁻⁵ > 1.4054·10⁻⁵ ≥ ε₃(δ). (2) Both sources define S(T) as (1/π) times the continuous variation of arg ζ along the path from the real axis (Trudgian from 0, HSW from 2) to σ₁ + iT (or 2 + iT) and then to ½ + iT; Trudgian's (2.5) and HSW's (5.5)–(5.6) relate the same N(T) to it, and only N(T) enters here. (3) The 1/8 enlargement in E is a precaution against a possible misprint between HSW's (1.4) and (1.5); it costs nothing visible.

---

## §6 Clauses 4 and 5 — the layer corollaries

Let ℓ := log(t/2π). Recall ε₃(δ) ≤ ε̄₃ := 1.4054·10⁻⁵ and that clause 3 for ζ reduces to (i): 2/sin(πδ) + ε₃(δ) ≤ min_{|s−t|≤4}Ψ(s).

**Lemma L (from a lower bound on Ψ to the layer).** Let t ≥ 28 and suppose min_{|s−t|≤4}Ψ(s) ≥ M for some M > 2 + ε̄₃. Then every point (t, ½ − δ) with

  δ ≥ δ_M := (1/π) arcsin(2/(M − ε̄₃))

is uncertifiable by any cone element at any bandwidth; and δ_M ≤ (2/(π(M − ε̄₃)))·(1 − 4/(M − ε̄₃)²)^{−1/2}.

*Proof.* For δ ∈ [δ_M, ½], πδ ∈ [arcsin(2/(M − ε̄₃)), π/2], so sin(πδ) ≥ 2/(M − ε̄₃), i.e. 2/sin(πδ) + ε̄₃ ≤ M ≤ min Ψ; this is clause 3(i) (with ε₃(δ) ≤ ε̄₃), and clauses 3 and 2 apply (Theorem G supplies (ii)). The bound on δ_M is arcsin x ≤ x/√(1 − x²) (arcsin x = ∫_0^x dt/√(1 − t²) ≤ x/√(1 − x²)). ∎

**Theorem R1, clause 4 (layer corollary, conditional form).** Let t ≥ 28 and 0 ≤ ε < 1 with min_{|s−t|≤4}Ψ(s) ≥ (1 − ε)ℓ/2π and (1 − ε)ℓ/2π > 2 + ε̄₃. Then every point with

  1 − σ ≥ δ₄(t, ε) := (1/π) arcsin( 2 / ((1 − ε)ℓ/2π − ε̄₃) )

is uncertifiable, and δ₄(t, ε) = (4/ℓ)(1 + ε + O(ε²) + O(ℓ⁻²)); more precisely δ₄ ≤ (4/((1 − ε)ℓ − 2πε̄₃))·(1 − (4π/((1 − ε)ℓ − 2πε̄₃))²)^{−1/2}. **The cone sector's reach at such heights is contained in the layer {1 − σ < (4 + o(1))/log t}.** *Exact hypothesis:* the lower bound on the window minimum of Ψ; nothing else about the zeros is used. *Where the hypothesis comes from:* Ψ(s) = ∫μ_0(s − x)dN(x); with N = M + R (M the smooth main term, R = N − M) one has, integrating by parts, Ψ(s) = ∫μ_0(s − x)M′(x)dx + ∫R(x)·(−∂_xμ_0(s − x))dx, the first term being (1/2π)log(s/2π) + O(1/s) and the second bounded by 2 sup_{|x−s|≤H}|R(x)| + (tail ≤ 2 sup_{x}|R(x)|/(1 + x²)-weighted·e^{−πH}), since ∫|μ_0′| = 2μ_0(0) = 2. So ε = O(sup|R|/ℓ) over a window around t. Under the Riemann Hypothesis R(x) = S(x) + O(1/x) = O(log x/log log x) (Littlewood 1924 `[recalled, unverified; the standard reference is Titchmarsh, *The theory of the Riemann zeta-function*, Thm 14.13; not read for this note and not load-bearing — the clause is proved under its stated hypothesis]`), so ε → 0 and the layer constant tends to 4. Unconditionally the explicit bound of clause 5 gives sup|R| ≤ E(x) with E ≍ 0.1038 log x, which is NOT o(ℓ) — hence clause 5 proceeds differently (window count, not window mean).

*Proof.* Lemma L with M := (1 − ε)ℓ/2π; the asymptotic form is arcsin x = x + O(x³) with x = 2/(M − ε̄₃) = (4π/ℓ)(1 + ε + O(ε²) + O(1/ℓ)). ∎

**Theorem R1, clause 5 (layer corollary, unconditional form — read at the page, D6).** Let E(T) := 0.1038 log T + 0.2573 log log T + 9.4925 (HSW Corollary 1.2 with the constant enlarged by 1/8, §3(b)). For t ≥ 28 and 0 < H ≤ t − 4 − e put

  Ψ₅(t, H) := [ (H/π) log((t − 4 − H)/2π) − 2E(t + 4 + H) ] / cosh(πH).

Then min_{|s−t|≤4}Ψ(s) ≥ Ψ₅(t, H), and whenever Ψ₅(t, H) > 2 + ε̄₃ every point with 1 − σ ≥ (1/π)arcsin(2/(Ψ₅(t, H) − ε̄₃)) is uncertifiable. Consequently:
 (a) the asymptotic layer constant is **C_uncond := 2/(π m*) = 66.41**, where m* := max_H (H/π − 2·0.1038)/cosh(πH) = 0.009586 at H* = 0.9719: every point with 1 − σ ≥ (66.41 + o(1))/log t is uncertifiable, unconditionally;
 (b) the statement is non-vacuous from log t₀ = 377.4 on (t₀ = e^{377.4}; there Ψ₅ = 2), and the uncertifiable threshold δ₅(t) := min_H (1/π)arcsin(2/(Ψ₅ − ε̄₃)) satisfies δ₅·log t = 146.4, 113.5, 84.4, 71.8, 68.0, 66.6 at log t = 400, 500, 1000, 3000, 10⁴, 10⁵ (`verify/clause5_constants_run.log`).
The shape is the killer's; the constant is honest and weak.

*Proof.* For s ∈ [t − 4, t + 4] and 0 < H: every zero with ordinate τ ∈ (s − H, s + H] contributes m_ρ μ_0(s − τ) ≥ 1/cosh(πH) to Ψ(s), so Ψ(s) ≥ [N(s + H) − N(s − H)]/cosh(πH). By HSW Corollary 1.2 (T ≥ e), with the notation of Theorem G's proof, N(s + H) − N(s − H) ≥ ∫_{s−H}^{s+H}(1/2π)log(x/2π)dx − E(s − H) − E(s + H) ≥ (H/π)log((s − H)/2π) − 2E(s + H) ≥ (H/π)log((t − 4 − H)/2π) − 2E(t + 4 + H), E being increasing (both readings of HSW's expression are covered by the +1/8). This is Ψ₅(t, H). Lemma L gives the uncertifiability statement. For (a): as t → ∞ with H fixed, Ψ₅(t, H) = [(H/π − 0.2076)ℓ − O(log ℓ)]/cosh(πH), so the best constant is 2/(π m*) with m* the maximum of (H/π − 0.2076)/cosh(πH) over H > 0.2076π, computed by a grid search of step 10⁻⁴ (`clause5_constants.py`), and arcsin x = x(1 + O(x²)). For (b): direct evaluation, with every quantity computed in log t to avoid overflow. ∎

*Remarks.* (1) The window-count device is forced: E(T) ≍ 0.1038 log T is a positive fraction of the mean density ℓ/2π ≍ 0.159 log t, so the mean-value route of clause 4 cannot be made explicit from these sources — one needs H > 2πc₁ = 0.652 for the window count to be positive, and the price is the factor cosh(πH) ≈ 9.9 at the optimum. (2) The contract's pricing arithmetic used H = 4πc₁ = 1.304 (m = 0.006894, C ≈ 92) and the wrong local factor (1/sin instead of 2/sin), quoting "C_uncond of order 50–70 `[recalled, unverified]`"; the honest number is 66.4 at the optimal H, with the factor 2 included. (3) t₀ = e^{377} is astronomically large; below it the unconditional clause says nothing, and the ζ-anchored clauses 2–3 (with Ψ computed) are the operative statements at accessible heights (§7).

---

## §7 Numerical record (every number below is in a log under `verify/`)

**Table N — the identity checked against ζ (`normalization_zeta_check_run.log`; numpy 2.0.2, scipy 1.13.1, mpmath 1.3.0; 16 s).** a(0) = −0.653847, A(0) = −0.855010, τ₀ = 6.3100 (zero crossing of a), I₋ = 2.241523 (so 2 − I₋ = −0.241523); a(τ) agrees with (1/2π)log(τ/2π) to 4·10⁻⁴ at τ = 8 and to 10⁻⁵ at τ = 60. Fejér family (B(w_T) versus P + Z; P exact to 4·10⁶ plus tail; Z from the first 200 zeros):

| T | B(w_T) | P | P tail est. | Z | B − shares |
|---|---|---|---|---|---|
| 4 | 0.58099 | 0.56036 | 0.04188 | 0.00000 | −0.02125 |
| 8 | 0.18905 | 0.17851 | 0.02094 | 0.00000 | −0.01040 |
| 11 | 0.13597 | 0.12839 | 0.01523 | 0.00000 | −0.00764 |
| 12 | 0.15030 | 0.14328 | 0.01396 | 0.00004 | −0.00697 |
| 14 | 0.21866 | 0.19453 | 0.01197 | 0.01817 | −0.00600 |
| 15 | 0.27067 | 0.14792 | 0.01117 | 0.11715 | −0.00556 |
| 16 | 0.33348 | 0.09503 | 0.01047 | 0.23323 | −0.00526 |
| 20 | 0.67989 | 0.08835 | 0.00838 | 0.58734 | −0.00418 |
| 30 | 2.06570 | 0.07055 | 0.00558 | 1.99236 | −0.00280 |
| 40 | 3.99496 | 0.04798 | 0.00419 | 3.94488 | −0.00210 |

The residual has the sign and size of the tail estimate; the zero share switches on exactly as the triangle's support crosses γ₁ = 14.134725. Minimum of B(w_T)/ŵ_T(0) over the family: 0.13597 at T = 11 — the primal upper bound κ ≤ 0.136 of §8.4. These numbers reproduce `results/c2-m5/verify-next/budget_floor_run.log` line for line.

**Table E — the ζ-anchored domination at heights 10⁶, 10⁷, 10⁸ (`confinement_edge_run.log`; zeros by mpmath.zetazero, 37/45/52 of them within ±10 of t, indices from 1 747 128, 21 136 104, 248 007 999; 51 s).** Ψ on |s − t| ≤ 6: min/mean/max = 1.080/1.934/2.562 (t = 10⁶, ℓ/2π = 1.906), 1.349/2.312/3.227 (10⁷, 2.273), 1.775/2.701/3.524 (10⁸, 2.639); mean gaps 0.5348, 0.4402, 0.3860 against 2π/ℓ = 0.5246, 0.4400, 0.3789. (a) The contract's literal condition fails at s = −t at every height (left side ≥ 1, right side below double-precision underflow; analytically < 10⁻¹⁹). (b) Corrected exact edge δ*(t′) — the least δ with 2[μ_y(t′ − s) + μ_y(t′ + s)] ≤ Ψ(s) on |s − t′| ≤ 6, the tails outside being covered by Lemma P and Theorem G — at seven heights t′ ∈ t + {−2, −1, −½, 0, ½, 1, 2}:

| t | Ψ(t′) at the seven t′ | corrected δ*(t′) | δ*·ℓ | literal-on-window edge δ·ℓ (the pricing's quantity) |
|---|---|---|---|---|
| 10⁶ | 2.152, 1.884, 1.967, 1.633, 2.013, 2.036, 1.528 | 0.380, —, —, —, —, 0.479, — | 4.55, 5.73 | 1.84, 2.14, 2.03, 2.53, 2.00, 1.96, 2.78 |
| 10⁷ | 2.502, 2.661, 1.792, 1.490, 2.069, 2.043, 2.392 | 0.296, 0.271, —, —, 0.419, 0.437, 0.319 | 4.23, 3.87, 5.99, 6.24, 4.56 | 1.87, 1.75, 2.75, 3.40, 2.29, 2.33, 1.96 |
| 10⁸ | 2.426, 2.803, 2.797, 2.170, 1.893, 2.432, 2.836 | 0.309, 0.254, 0.254, 0.403, —, 0.310, 0.250 | 5.12, 4.21, 4.21, 6.69, 5.15, 4.14 | 2.24, 1.93, 1.93, 2.54, 2.95, 2.24, 1.90 |

"—" means no δ ∈ (0, ½] satisfies the domination (Ψ(t′) < 2: a pair weighs at least two on-line zeros). The last column reproduces PRICING-next-unit §1.1(c)'s table at t = 10⁶ digit for digit (0.1539, 0.1785, 0.1698, 0.2108, 0.1666, 0.1639, 0.2318 times ℓ), which confirms that the two computations of Ψ agree and that the difference is exactly the factor 2 and the missing s ≈ −t′ check (D1). (c) The window-minimum form of clause 3(i) says nothing at these three heights (min Ψ = 1.08, 1.35, 1.78 < 2); the pointwise form (clause 2 itself) is the operative statement below ≈ 10⁹, and the mean-density form (clause 4) needs ℓ/2π > 2, i.e. t > 2πe^{4π} ≈ 1.8·10⁶, with the window minimum lagging the mean by a factor ≈ 0.6–0.7 at these heights. Reading: where it applies, δ*·ℓ ≈ 4·(ℓ/2π)/Ψ(t′)·(1 + o(1)) — the layer constant at a given height is 4 times the ratio of mean to actual smoothed density, i.e. 4 at mean density, as clause 4 predicts.

**Clause 7 (`dlvp_constant_run.log`).** (2/√3 − 1)(4√3 − 6) = 0.14359354, /5 = 0.02871871, reciprocal 34.8205; 2 + ψ(1) − log π = 0.278054, 3× that + log 2 = 1.527311 ≤ 1.5274; b_j and B(w) bounds verified against exact values at t = 28, 10², 10⁴, 10⁶ (e.g. B = 457.717 ≤ 461.855 at t = 10⁶, η = η*); exact reach of the element δ_max·log t = 0.731, 0.145, 0.065, 0.050, 0.040, 0.035, 0.031 at t = 28, 10², 10³, 10⁴, 10⁶, 10¹⁰, 10²⁰.

**Lemmas (`kernel_lemmas_run.log`).** Closed form of μ_y by Fourier inversion to 1.3·10⁻¹⁶; mass 1.000000000000 and peak 1/cos(πy) to 10⁻¹² at y ∈ {0, 0.25, 0.4, 0.45, 0.49}; tail ratio ≤ 2.011240 (sharp constant 2(1 + e^{−2π})/(1 − e^{−2π})² = 2.011240); k_y e^{δ|u|} ≤ 2; Lemma D ratio ≤ 0.168; Gauss's integral and the Poisson-kernel transform to the quadrature's precision (see the log for the per-point residuals); Lemma A at five (a, x) pairs; the de la Vallée Poussin ŵ-formula against direct quadrature at two frequencies (t = 5, agreement to 10⁻⁸), w ≥ 0 (grid minimum −6.6·10⁻¹⁸, rounding) and ŵ > 0.

**Clause 5 and Theorem G (`clause5_constants_run.log`, `gaps_first_zeros_run.log`).** ε̄₃ = 1.4054·10⁻⁵, G_max = 7.554, 1/cosh(7.5π/2) = 1.530·10⁻⁵; Theorem G ranges (a) T ≥ 2304.2 (HSW (5.6), to 3.06·10¹⁰), (b) T ≥ 1.096·10¹⁰ (HSW Cor. 1.2), (c) [33.9, 272.5] and [179.6, 6.8·10⁶] (Trudgian (2.5)+(1.2)), (d) T ≥ 1.22·10⁴ (HSW Cor. 1.4 + Trudgian (2.5)); H* = 0.9719, m* = 0.009586, C_uncond = 66.41, log t₀ = 377.4; first zeros and gaps as quoted in §3.

---

## §8 The ladder, the S1–S5 bearing, prior art, the zoo protocol, and the open problem

### §8.1 The ladder (KICKSTART 10(b); PRICING-next-unit §1.5)

* **Rung 0 — the model world.** The brief's question: is a positive Chebyshev-growth datum (axiom P, C2 line 14) with an off-line pair at depth y and height t admissible, and if so is the theorem sharp? Honest answer: **Theorem R1 is one-sided.** It proves that no cone certificate at (t, y) exists when (D_{t,y}) holds; it does NOT construct a datum realizing (t, y), and it does not assert that every uncertifiable point is realizable. "Sharp" is claimed only in clause 7's sense — the layer is nonempty, the reach is a band between c/log t and C/log t — not in the strong sense. The existence question is M1's, and the budget-floor computation (§8.4: I₋ = 2.2415 > 2) says that its answer cannot come from finite-variation perturbations of the mean density. For an abstract datum with on-line part σ (a positive integer-atomic measure) the theorem holds verbatim with Ψ_σ(s) := ∫μ_0(s − τ)dσ(τ)|_{τ>0} in place of Ψ — clauses 1–3 use only the identity, the positivity of the shares and the kernel lemmas.
* **Rung 1 — function fields.** Degenerate: a curve's 2g zeros lie on one circle, the "archimedean" term is the finite denominator (1 − T)(1 − qT), and the cone is the nonnegative cosine polynomials in the angle θ. The analog of clause 2 is the finite statement that the 2g actual points dominate any hypothetical off-circle orbit in every nonnegative test once the pair's depth weight is at most the local point density; there is no height aspect and no layer. Stated for the record; nothing is proved on this rung.
* **Rung 2 — Davenport–Heilbronn / Epstein (RH false).** **Axiom P fails, so clause 1 fails, so the theorem is vacuous — for the right reason.** The witnesses are on disk with exact closed forms (`results/c3-r/m0-axiom-note.md` §6.1, read): Λ_DH(3) = −κ log 3 = −0.3120927…, Λ_DH(4) = −(2 + κ²)log 2 = −1.44223196…, Λ_DH(12) = −κ(1 + κ²)log 12 = −0.762877471988…, with κ = (√(10 − 2√5) − 2)/(√5 − 1) = 0.284079…; and for the Epstein zeta function of x² + 5y² (§6.2) Λ_Q(36) = −4 log 6 = −7.167037…. A negative Λ makes P(w) negative for suitable w ∈ Σ_L (a narrow tooth at u = log 3, say), so B(w) ≥ Z(w) fails and a "cone certificate" 4(ŵ ∗ μ_y)(t) > B(w) no longer excludes anything — consistently with DH's verified off-line zero ρ = 0.808517182456637 + 85.699348485377592i (§6.1, Newton residual 7.6·10⁻⁴¹), which a cone row would otherwise wrongly exclude. The named input violated by the RH-false world is P (zoo I.1 in its own form). The optional diagnostic of PRICING.md §2 rung 2 (a DH cone row with negative prime share, ≈ 1 hour with the D1 `f_DH` producers) was not run here.
* **Rung 3 — ζ_K = ζ·L(χ₋₂₀).** Λ_K ≥ 0 verified for n ≤ 200 (`m0-axiom-note.md` §6.2, "contrast object", read), the identity is the degree-2 explicit formula (not on disk in Lean), and the theorem transfers verbatim with the degree-2 archimedean functional and Ψ_K; the mean density is (1/2π)log(t²|D|/(2π)²) = (1/π)log(t√|D|/2π), so the layer is {1 − σ < (2 + o(1))/log(t√20/2π)} in the same normalization (the pair's weight 2/sin(πδ) against twice the density). Stated, not proved: the degree-2 identity is not among this note's inputs.
* **Rung 4 — ζ:** the theorem itself (§1–§6).

### §8.2 S1–S5 bearing, honestly (KICKSTART; PRICING-next-unit §1.6)

S1: the theorem CONSUMES axiom P (clause 1 drops the prime share) and is vacuous where P fails; it is an S1-shaped statement about the cone, and a NEGATIVE one — it says what the P-consuming sector cannot do. S2: not a proportion statement; a single-point statement (no certificate at (t, y)); III.1 does not bind. S3: depth enters only through 2/sin(πδ); the theorem confirms PRICING.md §1.3's finding that the cone separates a double from a pair by at most 2h(0)π(1/cos πy − 1), L-independent — clause 6 is the same fact from the u-side; no bearing on lemmaR_tight beyond that. S4: no positivity is asserted; the argument is a domination of two nonnegative kernels; IV.1's containment (the cone's observable is a Weil test times 1/cosh(u/2)) is the same HIT with the same evasion as PRICING.md §3 step 5 (the sign of the measure, not a new coordinate), now confirming IV.1's consequence that the cone restriction buys only the layer. S5: not engaged.

### §8.3 Prior art (corpus first; standing order 7 dual check owed; every novelty statement `[novelty: single-check]`)

* **The mechanism is classical.** The cone element of clause 7 IS de la Vallée Poussin's 3-4-1 argument (C2 line 16(a); Lemma E's remark), and the cap "orbit share ≤ 2·(pole term) = 4ŵ(0)" (ŵ ≤ ŵ(0), μ_y of mass one) is the continuous form of Fejér's a₁ ≤ 2a₀ for nonnegative cosine polynomials — zoo III.9 (BARRIER-ZOO.md lines 218–224, read): "The 3-4-1 inequality is Fejér-square positivity — the identical 1899 generator behind classical zero-free regions, edge-capped for 125 years", and the Granville–Soundararajan floor there ("all zero-location content from D-data is confined to the classical de la Vallée Poussin edge") is the program's own prior statement of the confinement at the pretentious level, as sweep-certified folklore. Zoo III.2 (lines 162–168, read) is the complementary bracket: small cones prove nothing.
* **Corpus (per PRICING-next-unit §1.7, whose sources were not re-read here; the brief assigns the corpus re-read to Job 2).** Platt–Trudgian p3-22a1 (RH to 3·10¹²): on disk, not needed (off-line zeros only enlarge Z). w-14, w-15, y-25 (Carneiro school, pair correlation under RH): zoo IV.7's Opus read (BARRIER-ZOO.md line 386, read) found no periodic-configuration statement in a text-layer sweep; the pricing infers the same for a first-order confinement statement; this note does not add to that inference. r-25a (Goldfeld–Hoffstein–Lieman appendix, effective ZFR): the classical method, no limit theorem. Heath-Brown 1992 (`fetched-r6/r6-03-…PLMS64.pdf`, on disk since this session, noisy text layer, NOT read for this note): the smoothed explicit-formula zero-free-region method — the same generator as a cone element; cited by listing only.
* **Network (PRICING-next-unit §1.7, fetched 2026-09-10 by the pricing agent; not re-fetched):** Mossinghoff–Trudgian 1410.3926, MTY 2212.06867, Kadiri — explicit ZFR constants from the positivity method; none states a cone-wide confinement theorem.
* **Finding `[novelty: single-check]`.** The cone-wide statement — no strip-positive certificate at any bandwidth excludes a zero at (t, y) once 2/sin(πδ) ≤ Ψ near t, with the bandwidth pinned at ≍ 1/δ and the explicit two-sided band c/log t ≤ reach ≤ C/log t — is not found in the corpus or in the pricing's network check; its mechanism (Fejér cap + explicit formula + sech kernels) is classical, so the novelty is the statement and its explicit form, which is what repair 1 asked for (C2 line 74). Two further items surfaced by this note and not in the pricing: (i) the factor 2 (a pair weighs two on-line zeros: D1) and (ii) Theorem G as the discharge of the gap condition from the read sources — both elementary.

### §8.4 The zoo brief-time protocol (BARRIER-ZOO.md §0, lines 17–33, read) — hits and evasions

Step 1, scope: **refutation channel** (a no-go theorem about a proof class). Step 2, model worlds: I.1 — P consumed exactly once, DH/Epstein refused at the axiom with the exact witnesses (§8.1 rung 2): PASS in I.1's own form. I.2 — the theorem uses the explicit formula (axiom FE) and ζ's zeros; in a Beurling world with Λ ≥ 0 but no functional equation clause 1 has no identity to stand on, so the theorem is FE-dependent — stated. I.3 — not applicable (no configuration LP). Step 3, ceilings: not certificate-class; II.4 consistent (S3 above). Step 4, structural: III.2 and III.9 MATCH by mechanism — evasion clause: the theorem does not evade them, it PROVES their content for this cone, with constants; III.1: exemption declared (single-point statement). Step 5, disguise: IV.1 HIT with the written evasion (the cone's observable is a Weil test with the multiplier 1/cosh(u/2); no new data coordinate is claimed; the theorem is about the sign of a measure); IV.2 PASS (untilted identity, pole exact); IV.7 template — "designer-anticipated failure mode made a fact" (BARRIER-ZOO.md line 377): the killer's line-70 verdict becomes a theorem with the constant 4 (mean density) / 66.41 (unconditional). Step 6, visibility (IV.9): the theorem IS a visibility statement — the cone's visible region at height t is the band c/log t ≤ 1 − σ < C/log t; below t ≈ 1.8·10⁶ the mean-density form is vacuous and the pointwise form applies only where Ψ(t) > 2 (Table E). Step 7, process: V.2 prior art as above (single-check; Opus dual check owed); V.3 — the recalled items are: ζ(½) ≠ 0 (not used), Littlewood's RH-conditional S(t) bound (a pointer in clause 4, not load-bearing), Mossinghoff–Trudgian's 5.573412 (not used), the textbook location of the Hadamard formula (not used: Lemma E derives the identity), DLMF 5.9.12 as the location of Gauss's integral (the integral itself is checked numerically and is the one classical representation used); every load-bearing constant is computed in `verify/` or read at the page of a file on disk.

### §8.5 The open problem — the configuration-free version, stated as M1's honest object (PRICING-next-unit §1.1(b)–(c), §1.3)

Theorem R1 anchors on ζ: the actual on-line zeros must dominate the hypothetical pair. The configuration-free version — "no cone certificate exists outside the layer, for every admissible datum" — needs a lower bound on the budget alone:

  **Budget-floor problem.** Determine κ := inf_{w ∈ Σ_∞} B(w)/ŵ(0). Is κ > 0, and if so, with what explicit value?

What is on record (Table N): the elementary "bathtub" bound B(w) ≥ (2 − I₋)ŵ(0) FAILS, because I₋ := ∫_{a<0}|a| = 2.241523 > 2 — the negative part of the archimedean density a = μ_0 ∗ A on |τ| < τ₀ = 6.31 outweighs the pole; and the Fejér family gives the primal upper bound κ ≤ 0.13597 (T = 11). If κ > 0 with explicit κ, the configuration-free layer constant is of the form C ≈ 4(1 + 0.24/κ) (pricing agent's assembly `[inferred, not re-derived here]`). LP duality (PRICING-next-unit §1.1(b)) shows what a proof must contain: a dual certificate is a pair (ψ ≥ 0 on the zero line, φ ≥ 0 on the prime line) with (2 − κ)δ₀ + a = ψ + φ̂/2π; since a(0) = −0.653847 < 0 while φ̂(0) = ∫dφ ≥ 0 for every finite positive φ, **no finite-mass prime measure and no finite-variation perturbation of the mean zero density can certify any κ > 0** `[the pricing's finding, novelty: single-check]` — the dual object must be a genuine infinite zero configuration with positive prime measure and pole weight below 2, which is the truncated-Hamburger existence set PRICING.md §1.1(v) named as M1's honest object. Grade: OPEN. This note proves the ζ-anchored theorem and records the configuration-free one as the problem it is.

---

## §9 Refutation-shaped close (KICKSTART 10(c); PRICING-next-unit §1.9), honesty note, and traceability

### §9.1 The close (the note landed; constants corrected per D1)

**The strip-positive cone sector (termwise-positive first-order conservation, any bandwidth) cannot yield a zero-free point outside a de la Vallée Poussin-shaped layer {1 − σ < C/log t}, because a hypothetical orbit's depth kernel μ_y has peak 1/sin(πδ) and mass one and puts two zeros at height t, while ζ's own sech-smoothed on-line density Ψ near t is ≍ log t/2π; whenever 2/sin(πδ) ≤ Ψ near t (exact hypothesis: (D_{t,y}) of clause 2, implied for ζ by clause 3(i), 2/sin(πδ) + ε₃(δ) ≤ min_{|s−t|≤4}Ψ(s), the gap condition being Theorem G) the orbit's share is dominated pointwise by the on-line share in every cone test, so no certificate exists at any bandwidth; the bandwidth is pinned at ≍ 1/δ by cosh(yu)/cosh(u/2) ≤ 2e^{−δ|u|}. The constant is C = 4 + o(1) where Ψ has mean strength (clause 4; under RH at every large height), C = 66.41 + o(1) unconditionally from the explicit zero-counting bound of Hasanalizade–Shen–Wong (clause 5, for t ≥ e^{377}), and the layer is nonempty: de la Vallée Poussin's element, a point of the cone, certifies 1 − σ < 1/(34.82 log t) (clause 7).**

Grade on landing (pending the dual check): theorem — clauses 1, 2, 3, 6, 7 proved in full from the on-disk formal explicit formula plus elementary analysis; clause 5 proved from a source read at the page; clause 4 proved under its stated hypothesis; Theorem G proved from sources read at the page plus a computation of the first 1900 zeros. `computationally-verified` numerics for Tables N and E. Binds: cone/positivity-class first-order certificates — C2 Sector I, the classical de la Vallée Poussin / Landau / Heath-Brown detectors as cone elements. Enters Group IV as the proposed entry `results/c2-r1/zoo-IV18-proposed.md` after Job 2 (standing order 7).

*The failure branch of PRICING-next-unit §1.9 did not fire:* the density input of clauses 3–5 is honest (the theorem says nothing where Ψ < 2, and says so), and the configuration-free version is recorded as open (§8.5), not claimed.

### §9.2 Honesty note (standing order 5) — what was read, computed, inferred; what the theorem does not say

* **Read at the page this session:** `Zeta23/WeilEF/Main.lean` 240–300, `Zeta23/ExplicitFormula.lean` 40–90, `Zeta23/Defs.lean` 44, 105, 120–123, `Zeta23/Statement/SeamClosed.lean` 22, 26, `Zeta23/WeilEF/Effective.lean` 924–927, `AUDIT.md` 18–30 (no Lean file modified; no Lean build run); Hasanalizade–Shen–Wong arXiv:2107.06506v1 pp. 1–3 and the proof of Corollary 1.2 (p. 15) — pdftotext plus a visual read of p. 2 for the 1/8; Trudgian arXiv:1208.5846v2 pp. 1–3 (Theorem 1, Corollary 1, (1.2), (2.5)); `results/c3-r/m0-axiom-note.md` §6.1–6.2; BARRIER-ZOO.md §0, III.1, III.2, III.9, IV.1, IV.7, IV.17; `directions/C2-rigidity-conservation.md` lines 14–20, 70–74, 81; `results/c2-m5/PRICING-next-unit.md` in full; `results/c2-m5/PRICING.md` §1.2–1.4, §5; the three scripts and logs of `results/c2-m5/verify-next/`. The two arXiv PDFs were located by title through the arXiv API (the recalled numbers in FETCH-LIST-ROUND6.md turned out correct) and match the copies the sponsor placed in `fetched-r6/` byte for byte (SHA-256 3fc4c89f… and 274b3a0a…).
* **Computed:** everything in `verify/` (six scripts, six logs, six JSON outputs; total ≈ 7 minutes, one process at a time).
* **Recalled and labeled (none load-bearing):** ζ(½) ≠ 0; Littlewood's RH-conditional S(t) = O(log t/log log t) and its Titchmarsh location; Mossinghoff–Trudgian's 1/(5.573412 log t); the Davenport chapter for the Hadamard partial-fraction formula; DLMF 5.9.12 as the location of Gauss's integral (the integral is verified numerically at four points and is the only classical special-function representation used, in Lemmas A and D).
* **Inferred, labeled:** the pricing's assembly C ≈ 4(1 + 0.24/κ) for the configuration-free version (§8.5); the pricing's reading of the Carneiro-school sweep (§8.3).
* **Not done:** the Opus dual check (Job 2); the `#print axioms` line for `EF_lit_zetaZeroConfig` (owed by the checker per 10(f)); the corpus re-read of w-14/w-15/y-25/r-25a (assigned to Job 2); the DH cone-row diagnostic; any Lean formalization of the theorem; reading Heath-Brown 1992 or Berry 1988 (both now on disk, neither needed here).
* **What the theorem does not say:** it does not locate any zero of ζ; it does not assert that any uncertifiable point is realizable by an admissible datum (rung 0); it does not bound the reach of arguments outside the strip-positive cone (Sector II's signed tests are untouched); it does not apply where Ψ < 2, and it is silent at most points of height ≤ 10⁶ (Table E). Its content is exactly: **the class of cone certificates has a reach of de la Vallée Poussin shape, with the constants stated, at every bandwidth.**

### §9.3 Traceability (every number to its source)

| number | where it comes from |
|---|---|
| μ_y closed form, mass 1, peak 1/sin(πδ), tail constant 2.0113, c_P = 2.012 | Lemma P proof; `kernel_lemmas_run.log` |
| ε̄₃ = 1.4054·10⁻⁵, G_max = 7.554, 1/cosh(7.5π/2) = 1.530·10⁻⁵ | `clause5_constants_run.log` |
| γ₁ = 14.134725, γ₂ = 21.022040, first gap 6.8873, all 1899 gaps ≤ 7.5 | `normalization_zeta_check_run.log`, `gaps_first_zeros_run.log` |
| HSW Cor. 1.2 constants 0.1038, 0.2573, 9.3675 (T ≥ e); (1.4)'s +1/8; Cor. 1.4; (1.7) 2.5167 to 30 610 046 000; (5.6) | `fetched-r6/r6-02-hasanalizade-shen-wong-2022-counting-zeros-arXiv2107.06506v1.pdf` pp. 2, 15 |
| Trudgian (2.5) 0.2/T + |S(T)|; (1.2) |S| ≤ 1 (T ≤ 280), ≤ 2 (T ≤ 6.8·10⁶); Thm 1 (0.111, 0.275, 2.450) | `fetched-r6/r6-01-trudgian-2014-argument-II-arXiv1208.5846v2.pdf` pp. 1–3 |
| Theorem G ranges 33.9, 179.6, 2304.2, 1.22·10⁴, 1.096·10¹⁰ | `clause5_constants_run.log` |
| c = 0.0287187 = 1/34.8205; 0.278054; 1.527311; b_j and B checks; exact reach table | `dlvp_constant_run.log` |
| H* = 0.9719, m* = 0.009586, C_uncond = 66.41, log t₀ = 377.4, δ₅ table | `clause5_constants_run.log` |
| a(0) = −0.653847, τ₀ = 6.3100, I₋ = 2.241523, κ ≤ 0.13597 (T = 11), Table N | `normalization_zeta_check_run.log` (reproduces `c2-m5/verify-next/budget_floor_run.log`) |
| Table E (Ψ statistics, corrected and literal edges at 10⁶, 10⁷, 10⁸) | `confinement_edge_run.log` |
| Λ_DH(3), Λ_DH(4), Λ_DH(12), κ, the DH off-line zero, Λ_Q(36) | `results/c3-r/m0-axiom-note.md` §6.1–6.2 |
| Lean statements | `Zeta23/WeilEF/Main.lean` 268–270, `Zeta23/ExplicitFormula.lean` 64, 69–73, 81–84, `Zeta23/Defs.lean` 44, 105, `Zeta23/Statement/SeamClosed.lean` 22, 26, `Zeta23/WeilEF/Effective.lean` 924–927 |

*End of note. SHA-256 in `results/c2-r1/hashes.txt`.*
