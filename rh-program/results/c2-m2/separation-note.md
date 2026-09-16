# The Gevrey-localized single-defect separation theorem (Theorem M2, α = 2) with the tight-pair corollary: a theorem note

**Deliverable:** C2's first theorem under mandatory repair 2 (`directions/C2-rigidity-conservation.md` lines 39 and 74), built to the contract of `results/c2-m5/PRICING-next-unit.md` §2.2 under the brief `results/c2-m2/BRIEF.md` (with its addendum). Written 2026-09-16 (Session 22, Job 1, the author, Fable 5.1). Dual check owed to Job 2 (`results/c2-m2/check-O.md`) and two blind referee reports (`referee-F.md`, `referee-O.md`) before anything here is banked. Structure and tone follow `results/c2-r1/confinement-note.md`.

**Summary of what landed (details in §13).** The eight clauses are proved as contracted, with the constants carried honestly and eight dated deviations (§0.4), of which three are substantive: (D2) the Fourier-decay constant that the Lean derivative bounds actually give for the contract's bump is c_B = 2/√(72e) = 0.1430, not the pricing's inferred 0.20 (that number belongs to a different bump); (D3) with that c_B the reflected orbit at −t is provably negligible only when the height is large against the bandwidth, t ≥ 25L (a "reflection condition" enters the hypotheses; numerically it is vacuous for every t ≥ 3); (D5) the out-window radius is R = R₀L with R₀ = 76.5 for every L ≥ 50 (the contract's (3/(4c_B))²(1 + o(1)) = 27.5 is not what its own hypothesis yields; the asymptotic constant under that hypothesis is (7/(8c_B))² = 37.4). Clause 5 — the one live failure mode — HOLDS uniformly over depth |y| ≤ ½ (§6): the failure branch of PRICING §2.9 does not fire. The two-sided edge law is proved with κ₋ = 1.4810 (a closed form, log(√(π/2)e^{−1/4}/Z)) and κ₊ = 1.5311 for all λ ≥ 25 (§3); the pricing's 1.515 was a least-squares fit, not an asymptotic constant. The DH negative control (zoo V.4) FIRES: the datum separates DH's own off-line orbit at height 85.7 from the on-line configuration by a factor above the theorem's bound at the theorem's bandwidth (§8). Lint (KICKSTART 10(g)): the four banned hedges do not occur in the body of this note.

---

## §0 Objects, conventions, the two accounting points, and the deviation record

### §0.1 Conventions (one normalization, used by every script under `results/c2-m2/verify/`)

* **Transform.** For a function k on ℝ (complex-valued allowed) and z ∈ ℂ, h_k(z) := ∫_ℝ k(u) e^{izu} du whenever the integral converges absolutely. This is the Lean `paperFT k z` (`Zeta23/Defs.lean` line 44, quoted in §1). For a real even k and real ξ, h_k(ξ) = ∫ k(u)cos(ξu)du is real and even, and then h_k(−z) = h_k(z) for every complex z (the integrand is even in u after the substitution u ↦ −u). For a compactly supported k with supp k ⊂ [−a, a]: |h_k(x − iy)| ≤ e^{a|y|}‖k‖₁ (Paley–Wiener growth, one line: |e^{i(x−iy)u}| = e^{yu} ≤ e^{a|y|}). Throughout, k̂ denotes h_k; nothing in this note uses a second transform convention.
* **The bump.** B(v) := Z⁻¹exp(−1/(1 − 4v²)) for |v| < ½, B(v) := 0 for |v| ≥ ½, with Z := ∫_{−½}^{½} exp(−1/(1 − 4v²))dv = 0.221996908… (`verify/b1_constant_run.log`, `verify/edge_law_two_sided_run.log`; the pricing's `gevrey_edge_law_out.json` key `normalization_Z` = 0.2219969080840397 is reproduced digit for digit by the re-run, `verify/gevrey_edge_law_rerun_DIFF.txt`). B is even, C^∞, B ≥ 0, ∫B = 1, supp B = [−½, ½]. B_L(u) := B(u/L)/L, so supp B_L = [−L/2, L/2], ∫B_L = 1, and B̂_L(z) = B̂(Lz) for every complex z.
* **The test.** For t > 0 and L > 0: f = f_{t,L}(u) := i(B_L)′(u)e^{−itu}, a C^∞ complex-valued function with supp f ⊂ [−L/2, L/2]. Integration by parts (no boundary terms) gives, for every complex r,
  h_f(r) = i∫(B_L)′(u)e^{i(r−t)u}du = i·(−i(r − t))∫B_L(u)e^{i(r−t)u}du = **(r − t)·B̂_L(r − t) = (r − t)·B̂(L(r − t)).**   (0.1)
  In particular h_f(t) = 0, and for real r: |h_f(r)|² = (r − t)²B̂(L(r − t))².
* **The Weil test.** f̃(u) := conj(f(−u)) and g = g_{t,L} := f ⋆ f̃, g(x) = ∫f(y)f̃(x − y)dy = ∫f(y)conj(f(y − x))dy (the Lean `EF.tilde`, `EF.weilTest`, `Zeta23/ExplicitFormula.lean` lines 47–52, §1). g is C^∞ with supp g ⊂ [−L, L], and for every complex z
  **ĝ(z) = h_f(z)·conj(h_f(conj z))**   (0.2)
  (`EF.paperFT_weilTest`, lines 189–191, quoted in §1; the elementary computation: h_{f̃}(z) = conj(h_f(conj z))). For real r, ĝ(r) = |h_f(r)|² ≥ 0. **g is Hermitian, not real** (§0.4 D1): with a(x) := ∫(B_L)′(y)(B_L)′(y − x)dy — real, even, the autocorrelation of the real odd function (B_L)′ — one has g(x) = e^{−itx}a(x), so g(−x) = conj g(x). Its symmetrization g_e(x) := ½(g(x) + g(−x)) = a(x)cos(tx) is real, even, C^∞, supported in [−L, L], with ĝ_e(z) = ½(ĝ(z) + ĝ(−z)); on a reflection-invariant multiset (below) Σĝ_e = Σĝ.
* **Configurations.** A configuration Z is a locally finite multiset of points of the closed strip {γ ∈ ℂ : |Im γ| ≤ ½}, invariant under γ ↦ conj γ and under γ ↦ −γ (multiplicities preserved). The dictionary to zeros is γ = (ρ − ½)/i (`gammaOf`, `Zeta23/Defs.lean` line 105): a zero ρ = β + iτ has γ = τ − i(β − ½), so γ is real iff β = ½, and the strip 0 ≤ β ≤ 1 is |Im γ| ≤ ½. The Lean reflection ρ ↦ 1 − conj ρ is γ ↦ conj γ; the conjugation ρ ↦ conj ρ is γ ↦ −conj γ; together they generate the two invariances above. A point γ = x − iy with y ≠ 0 lies in the orbit {±x ± iy} of four points (two if x = 0). **Throughout, δ := |Im γ| = |β − ½| is the distance of an off-line point from the critical line** (not, as in the R1 note, the distance from the edge of the strip). The class 𝒞(C₁), C₁ ≥ 1, consists of the configurations with #{γ ∈ Z : |Re γ − x| ≤ 1} ≤ C₁log(3 + |x|) for every real x, counted with multiplicity and over all depths.
* **The datum.** W_Z(f) := Σ_{γ∈Z} h_f(γ)·conj(h_f(conj γ)) = Σ_{γ∈Z} ĝ(γ) (by (0.2)), the Lean `Z.W f f` (`Zeta23/Defs.lean` lines 164–170, §1). For a conjugation-invariant Z the terms of γ and conj γ are complex conjugates of each other, so W_Z(f) is real; the terms of real γ are |h_f(γ)|² ≥ 0. Absolute convergence for Z ∈ 𝒞(C₁) is part of clause 5's proof (§6).
* **The edge function.** c(λ) := ∫_ℝ B(v)cosh(λv)dv = B̂(±iλ) (real, since B is even) — so B̂_L(±iδ) = c(δL). Since B ≥ 0 has mass one and support [−½, ½]: 1 ≤ c(λ) ≤ cosh(λ/2). Notation ℓ_R := log(4 + t + R) (§0.4 D7).

### §0.2 Accounting point (i): the orbit has four points — which of them carry the main term

The orbit of the defect is {t − iδ, t + iδ, −t − iδ, −t + iδ}: FOUR points of Z. By (0.1), h_f(t − iδ) = (−iδ)B̂_L(−iδ) = −iδ·c(δL) and h_f(t + iδ) = iδ·c(δL). Each of the two points at +t contributes h_f(γ)conj(h_f(conj γ)): for γ = t − iδ this is (−iδc)·conj(iδc) = (−iδc)(−iδc) = −δ²c²; for γ = t + iδ it is (iδc)·conj(−iδc) = (iδc)(iδc) = −δ²c². **The pair at +t contributes −2δ²c(δL)² — two zeros, −δ²c(δL)² each.** The two points at −t contribute E₋ := 2Re[h_f(−t − iδ)·conj(h_f(−t + iδ))] with h_f(−t ∓ iδ) = (−2t ∓ iδ)B̂(L(−2t ∓ iδ)), which is small because the transform is evaluated at real part −2tL (clause 1, §4). This is the transcript's ledger `sources-extracted/tx_032.txt` (i)–(ii) verbatim: "(i) The pair γ₀, γ̄₀: h(γ₀) = (−iδ)B̂_L(−iδ), h(γ̄₀) = (iδ)B̂_L(iδ), and B̂_L(±iδ) = ∫B_L(u)cosh(δu)du =: c(δL) ∈ [1, cosh(δL/2)] is real; the pair contributes 2Re[(−iδ)(−iδ)]c² = −2δ²c² ≤ −2δ² (times m₀ ≥ 1). (ii) The reflected pair at −t₀: |h(−t₀ ∓ iδ)| ≈ 2t₀|B̂_L(−2t₀ ∓ iδ)|, superpolynomially small in Lt₀ — negligible." Re-derived above; confirmed by direct quadrature of f against e^{iγu} at the four points (`verify/four_point_accounting_run.log`, (2): the pair at +t equals −2δ²c² to 10⁻¹⁵ relative, the reflected pair is 10⁻⁷ of it at t = 30, δ = 0.3, L = 40). **So the R1 lesson ("a pair = two zeros") is already built into the contract's main term: −2δ²c² counts the two zeros at height +t, and the constant of the contract is correct. Stop condition (c) of the brief does not fire.** If the orbit's points carry multiplicity m ≥ 1 the main term is −2mδ²c(δL)²; the theorem is stated at m = 1 and only improves for m > 1.

### §0.3 Accounting point (ii): sign and normalization of W_Z against the Lean definition

`Zeta23/Defs.lean` lines 164–170 define the summand m_ρ·h_f(γ_ρ)·conj(h_g(conj γ_ρ)) and W(f, g) as its sum over the distinct zeros (§1 quotes them). With f = g and γ real the summand is m_ρ|h_f(γ)|² ≥ 0: an on-line configuration has W_Z(f) ≥ 0 for every test, and a defect is the only source of negative terms. The sign of the orbit's contribution, −2δ²c², comes from (−i)² = (i)² = −1 in §0.2, not from any convention: it is the statement that (r − t)² is negative at r − t = ∓iδ. The two-point numerical instance: `verify/four_point_accounting_run.log` (3) computes W_Z(f) by direct quadrature on the eight-point configuration Z = {±t ± iδ, ±r₁, ±r₂} (t = 30, δ = 0.3, L = 40, r₁ = t + 0.55, r₂ = t − 1.3): the imaginary part vanishes to quadrature precision, the four real points contribute |h_f(±r_j)|² ≥ 0 each below b₁/L², and the total equals −2δ²c² + E₋ + Σ|h_f|². The Weil-test identity (0.2) is checked at one complex point by a double quadrature ((4) of the same log, relative difference 10⁻⁶ at trapezoid resolution), and g is verified Hermitian and not real on a grid.

### §0.4 Deviation and precision record (dated 2026-09-16; contract = PRICING-next-unit §2.2 as reproduced in the brief; opened before the proofs, appended as the work proceeded)

**D1 (precision, 17:49 IST).** The contract calls g = f ⋆ f̃ "even, real". It is Hermitian: g(x) = e^{−itx}a(x) with a real and even (§0.1), so g(−x) = conj g(x) and Im g ≢ 0 (`four_point_accounting_run.log` (4)). Nothing downstream needs g real: the formal input `EF_lit` takes k : ℝ → ℂ (§1), W_Z(f) = Σĝ(γ) holds by (0.2), and the datum is real for conjugation-invariant Z. The real even test that gives the same datum on reflection-invariant Z is g_e = a(x)cos(tx). The theorem below is stated for g; g_e may be substituted in every clause.

**D2 (substantive — the decay constant, 17:49 IST; proved in §2).** The pricing's "c_B ≥ 0.20 `I infer`" was computed as 2/(e√(36/e)) = 1/(3√e) = 0.2022 from the Lean constant (36/e)^k k^{2k} of `abs_iteratedDeriv_theta_le` — the bound for the LEAN bump θ(x) = g(x)g(1 − x) = exp(−1/(x(1 − x))), g(x) = exp(−1/x). The contract's bump is B(v) ∝ exp(−1/(1 − 4v²)), and with x = v + ½ one has 1 − 4v² = 4x(1 − x), so B(v) = Z⁻¹θ(x)^{1/4} = Z⁻¹g(4x)g(4(1 − x)) = Z⁻¹g(4v + 2)g(2 − 4v). B is not θ. Transferring the Lean bound |g^{(k)}| ≤ (18/e)^k k^{2k} to B costs the affine chain rule (a factor 4^k) and a Leibniz product; the sharpest Leibniz bound available from the Lean numbers is |B_raw^{(k)}| ≤ (k + 1)(72/e)^k k^{2k} (Lemma G, §2), and the resulting decay constant is **c_B = 2/√(72e) = 0.14298** (the crude 2^k-Leibniz route gives 1/(6√e) = 0.1011). The numerical decay rate of |B̂| is ≈ 0.8 (`lemma_G_constants_run.log` (c), computed, not proved). Every constant downstream of c_B (R₀, the reflection condition, the Gevrey form of T₁) is carried with 0.14298.

**D3 (substantive — the reflected orbit, 17:49 IST; proved in §4).** Clause 1 as contracted, |E₋| ≤ 2δ²c(δL)²e^{−L} "for all t ≥ 3", is provable from Lemma G only when the Gevrey suppression at real part 2tL beats the strip weight e^{δL} and the target e^{−L}: the sufficient "reflection condition" (R) of §4 is implied by t ≥ 25L (`lemma_G_constants_run.log` (e); the asymptotic threshold is t/L ≥ 1/(8c_B²) = 6.1). The theorem is therefore stated with (R) among its hypotheses; equivalently the admissible bandwidths at height t are L*(t, δ) ≤ L ≤ t/25, a nonempty range for every t ≥ 25L*(t, δ). With the numerically observed decay rate 0.8 the threshold would be t/L ≥ 0.2, vacuous for every t ≥ 3 and L ≥ 50 (computed, not proved). The theorem's truth is not in question at small t (§8's DH control at t = 85.7, L = 87 shows the reflected pair at 10⁻¹⁵ of the main term); its PROOF with the on-disk constants is.

**D4 (precision and route — the in-window tail, 17:49 IST; proved in §5).** (a) The count of points with 1 < |Re γ − t| ≤ R needs a factor 2 (both sides of t): the contract's T₁ ≤ C₁log(3 + t + R)·C_B²Σ… reads 2C₁ℓ_R·C_B²Σ…. (b) With c_B = 0.143 the Gevrey form of T₁ falls below b₁C₁ℓ_R/L² only from L ≈ 3·10³ (`lemma_G_constants_run.log` (f)); the transcript's own polynomial route (tx_032 (iii): |B̂(η)| ≤ ‖B‴‖₁/|η|³) gives T₁ ≤ 2ζ(4)‖B‴‖₁²C₁ℓ_R/L⁶ ≤ b₁C₁ℓ_R/L² for L ≥ L₁ := (2ζ(4)‖B‴‖₁²/b₁)^{1/4}, which is below 50 (§5; ‖B‴‖₁ computed in `b1_constant_run.log`). The polynomial route is the operative one; the contract's Gevrey form is also proved, with its honest L₁.

**D5 (substantive — R₀, 17:49 IST; proved in §6).** The contract's "R₀ := (3/(4c_B))²(1 + o(1))" is replaced by an explicit R₀ valid for every L ≥ 50: the out-window sum is bounded by 2C₁log(3.5 + t + k) per shell, and under the theorem's own L-hypothesis the prefactors are absorbed as 2C₁ ≤ e^{L/8}/b₁ and log(3.5 + t) ≤ 1.05e^{L/8}, which puts 7/4 (not 3/2) in front of L in the exponent to beat. Hence R₀ = (7/(8c_B))²(1 + o(1)) asymptotically, and the explicit value proved for all L ≥ 50 is **R₀ = 76.5** (`lemma_G_constants_run.log` (d); (7/(8c_B))² = 37.4, (3/(4c_B))² = 27.5). The o(1) is genuinely o(1) only if log(C₁log t) = o(L), which the hypothesis L ≥ 4δ⁻¹(log log(3+t) + …) does not guarantee; the contract's form would follow under the stronger L ≥ Kδ⁻¹(…) with K → ∞.

**D6 (precision — the edge-law constants, 17:49 IST; proved in §3).** The pricing's "κ = 1.515 ± 0.002" is a least-squares constant with the slope also fitted (C = 1.0012). The two-sided law is proved with the exact asymptotic constant κ_∞ := log(√(π/2)e^{−1/4}/Z) = 1.48098… as κ₋, and κ₊ := κ_∞ + 1/(4√25) + 1/(128·25^{3/2}) = 1.5311, both valid for every λ ≥ 25 (`edge_law_two_sided_run.log`); the exact κ(λ) := log c(λ) − λ/2 + √λ + ¾log λ decreases from 1.5105 at λ = 25 toward κ_∞. Gap to the contract's number: κ₋ − 1.515 = −0.034, κ₊ − 1.515 = +0.016, both within the brief's 0.1: stop condition (a) does not fire and λ₀ = 25 stands. Clause 3's margin at λ = 25 is e^{0.634} = 1.89 proved against the computed ratio c(25)²/e^{12.5} = 2.00.

**D7 (precision).** The density log appearing in clauses 4–6 is written ℓ_R := log(4 + t + R) in place of the contract's log(3 + t + R): the shell of points with k ≤ |Re γ − t| < k + 1 is covered by two windows of the class definition centered at t ± (k + ½), whose logs are log(3.5 + t + k) ≤ log(4 + t + R) for k ≤ R. In clause 6's chain the two logs differ by less than 3 %.

**D8 (precision — clause 6's chain).** The contract's first inequality in clause 6 omits E₋; the proved chain is |W_Z − W_{Z′}| ≥ 2δ²c(δL)²(1 − e^{−L}) − 2[b₁C₁ℓ_R/L² + T₁] − 2e^{−L}, which the contract's right-hand side implies once E₋ is folded in. (The factor 2 in front of the noise bracket is a safe overestimate: the difference of two nonnegative in-window noise sums each ≤ N has absolute value ≤ N, so one N would do; the contract's 2N is kept.) Also: under the theorem's L-hypothesis the condition "(1 − c₀)δL ≥ 2log(1/δ)" of the last sentence of clause 6 holds automatically (δL/2 ≥ 4log(1/δ)), so the separation is ≥ 1 whenever the theorem applies.

**D9 (precision — clause 7).** "h_f(t) = 0, so the double contributes nothing" is exact for the double at +t; the reflected double at −t contributes 2·2|h_f(−t)|² = 16t²B̂(2tL)² ≥ 0, a real-point term that is part of Z′'s in-window or out-window real part and is absorbed by clauses 4–5 exactly as any other real point of Z′ (§7).

---

## §1 The formal inputs, quoted as Lean states them (`~/rh-lean-work/zeta-23-lean-main`, read 2026-09-16; no Lean file created, modified or rebuilt)

Every line number below was read this session. The `#print axioms` lines were produced by compiling a scratch file OUTSIDE the tree with `lake env lean` against the existing build (`verify/print_axioms_run.log`, scratch source `verify/axioms_m2.lean.txt`, 4 s): all nine theorems named in this section depend on exactly `[propext, Classical.choice, Quot.sound]`.

**The transform and the datum** (`Zeta23/Defs.lean` lines 44, 105, 164–170):

```
def paperFT (f : ℝ → ℂ) (z : ℂ) : ℂ := ∫ u : ℝ, f u * Complex.exp (Complex.I * z * (u : ℂ))
def gammaOf (ρ : ℂ) : ℂ := (ρ - 1 / 2) / Complex.I
/-- Summand of Weil's form: m_ρ h_f(γ_ρ) conj(h_g(conj γ_ρ))  [eq:Wdef]. -/
def Wsummand (f g : ℝ → ℂ) (ρ : ℂ) : ℂ :=
  (Z.mult ρ : ℂ) * paperFT f (gammaOf ρ) * (starRingEnd ℂ) (paperFT g ((starRingEnd ℂ) (gammaOf ρ)))
/-- W(f,g) := Σ_ρ m_ρ h_f(γ_ρ) conj(h_g(conj γ_ρ)), "Σ_ρ runs over the DISTINCT nontrivial zeros (of
either sign of γ) and the multiplicity is written explicitly"  [eq:Wdef]. As a tsum over the
subtype of carrier; absolute convergence is part of hypothesis H-EF. -/
def W (f g : ℝ → ℂ) : ℂ := ∑' ρ : Z.carrier, Z.Wsummand f g ρ
```

The abstract configuration is `structure ZeroConfig` (lines 119–130): a set `carrier` of distinct points with `mult ≥ 1`, in the closed strip `0 ≤ ρ.re ≤ 1`, invariant under `reflect ρ := 1 − conj ρ` (line 108) with equal multiplicities, and locally finite in the ordinate. Its docstring quotes the paper: "Inequalities (eq:zeroside) hold for every locally finite multiset of points in the strip 0<β<1 that is invariant under ρ ↦ 1−ρ̄ and satisfies N(t+1)−N(t) ≪ log(t+3); they contain no arithmetic." The class 𝒞(C₁) of §0.1 is this structure plus the explicit local count, plus invariance under ρ ↦ conj ρ (which the ζ instance has and the structure does not require). W_Z(f) of §0.1 is `Z.W f f` with the multiset written as points with multiplicity.

**The Weil test and the identity (0.2)** (`Zeta23/ExplicitFormula.lean` lines 47–52 and 188–191):

```
/-- App. A: `g̃(u) := conj (g(−u))`. -/
def tilde (g : ℝ → ℂ) : ℝ → ℂ := fun u => conj (g (-u))
/-- App. A: the Weil test function `k := f ⋆ g̃`, i.e. `k(x) = ∫ f(t) g̃(x − t) dt` ... -/
def weilTest (f g : ℝ → ℂ) : ℝ → ℂ := f ⋆[ContinuousLinearMap.mul ℝ ℂ] tilde g
/-- App. A: `h_{f⋆g̃}(z) = h_f(z) · conj(h_g(conj z))` for all complex z. -/
theorem paperFT_weilTest {f g : ℝ → ℂ} (hf : Continuous f) (hg : Continuous g)
    (hfs : HasCompactSupport f) (hgs : HasCompactSupport g) (z : ℂ) :
    paperFT (weilTest f g) z = paperFT f z * conj (paperFT g (conj z)) := by
```

**The explicit formula for ζ** (`Zeta23/ExplicitFormula.lean` lines 64, 69–73, 81–84; `Zeta23/WeilEF/Main.lean` lines 268–270), used only in clause 8:

```
def gammaBracket (r : ℝ) : ℝ := (Complex.digamma (1 / 4 + I * r / 2)).re - Real.log π
def literatureRHS (k : ℝ → ℂ) : ℂ :=
  paperFT k (I / 2) + paperFT k (-I / 2)
  - ∑' n : ℕ, ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ)
      * (k (Real.log n) + k (-Real.log n))
  + (1 / (2 * π) : ℂ) * ∫ r : ℝ, paperFT k r * (gammaBracket r : ℂ)
def EF_lit (Z : ZeroConfig) : Prop :=
  ∀ k : ℝ → ℂ, ContDiff ℝ 2 k → HasCompactSupport k →
    Summable (fun ρ : Z.carrier => (Z.mult ρ : ℂ) * paperFT k (gammaOf ρ)) ∧
    ∑' ρ : Z.carrier, (Z.mult ρ : ℂ) * paperFT k (gammaOf ρ) = literatureRHS k
/-- **Hypothesis-free form**: [eq:EFstd] holds for the canonical
unconditional ζ zero configuration. -/
theorem EF_lit_zetaZeroConfig : Zeta23.EF.EF_lit zetaZeroConfig := EF_lit_zeta zetaSeam
```

and the bridge from the literature form to the Weil form, `EF.prop_EF_of_lit` (lines 699–711): for `EF_lit Z`, `0 < L`, `f g` of class `ContDiff ℝ 2` with `tsupport ⊆ Icc (−L/2) (L/2)` and two integrability side conditions on `weilTest f g`, it concludes `Summable (fun ρ => Z.Wsummand f g ρ)` and `Z.W f g = ∫ τ, paperFT f τ * conj (paperFT g τ) * nuX (exp L) τ`; its proof (lines 712–733) goes through `hterm : m_ρ h_k(γ_ρ) = Wsummand f g ρ` for `k = weilTest f g`, which is (0.2) applied termwise. The test k takes values in ℂ: nothing in these statements asks for a real or even test (D1).

**The local zero count for ζ** (`Zeta23/WeilEF/Effective.lean` lines 924–927), which places ζ's configuration in 𝒞(C₁) with C₁ = 5.4·10⁸ (rung 4, §8):

```
/-- **E2 — the fully explicit local zero count**:
N(t, t+1] ≤ 540000000·log(|t|+3) for every t ∈ ℝ, unconditionally. -/
theorem zeta_local_zero_count_explicit (t : ℝ) :
    (Zeta23.Ncount t (t + 1) : ℝ) ≤ 540000000 * Real.log (|t| + 3) := by
```

**The Gevrey infrastructure** (`Zeta23/Taper/Gevrey.lean`; the file header, lines 6–24, names P1–P4 and says of the tail lemma "Downstream: a Gevrey tail lemma gives TailInputs …" — it is not on disk, and Lemma G of §2 is its Fourier-side content for this note's bump):

```
structure GevreyProfile (s A B : ℝ) (ϱ : ℝ → ℝ) : Prop where          -- lines 45–52
  taper : TaperProfile ϱ
  smooth : ContDiff ℝ ((⊤ : ℕ∞) : WithTop ℕ∞) ϱ
  one_lt : 1 < s
  A_pos : 0 < A
  B_pos : 0 < B
  bound : ∀ k : ℕ, 1 ≤ k → ∀ x : ℝ, |iteratedDeriv k ϱ x| ≤ B * A ^ k * (k : ℝ) ^ (s * k)
/-- the bump θ(x) = g(x) g(1−x), g = expNegInvGlue. -/
def theta (x : ℝ) : ℝ := expNegInvGlue x * expNegInvGlue (1 - x)                       -- line 55
/-- **(P1)** Gevrey-2 bound for exp(−1/x): |g^{(k)}(x)| ≤ (18/e)^k k^{2k} for all k ≥ 1 and all real x
(Cauchy's estimate for G(z) = exp(−1/z) on the circle |z − x| = x/2, where ‖G‖ ≤ exp(−2/(9x))). -/
theorem gevrey_expNegInvGlue (k : ℕ) (hk : 1 ≤ k) (x : ℝ) :                            -- lines 183–185
    |iteratedDeriv k expNegInvGlue x| ≤ (18 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * (k : ℝ)) := by
/-- Leibniz ⇒ |θ^{(k)}| ≤ (36/e)^k k^{2k}. -/
lemma abs_iteratedDeriv_theta_le (k : ℕ) (x : ℝ) :                                     -- lines 282–284
    |iteratedDeriv k theta x| ≤ (36 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) := by
/-- **(P4)** ϱ₂ is a Gevrey-2 taper profile with explicit constants (A, B) = (36/e, 2e^8): ... -/
theorem gevreyProfile_rhoTwo : GevreyProfile 2 (36 / Real.exp 1) (2 * Real.exp 8) rhoTwo where   -- line 393
```

Here `expNegInvGlue` is Mathlib's g(x) = exp(−1/x) for x > 0 and 0 for x ≤ 0 (the file's own header, line 9). The Leibniz transfer (P2) is the proof of `abs_iteratedDeriv_theta_le` (lines 285–314), which bounds each product |g^{(i)}||g^{(k−i)}(1 − ·)| by `gb i * gb (k−i) ≤ (18/e)^k k^{2k}` (`gb_mul_gb_le`, lines 262–275, using i^{2i}(k − i)^{2(k−i)} ≤ k^{2k}) and sums the binomial coefficients to 2^k. The concrete ramps: `Zeta23/Taper/GevreyRamps.lean` lines 202–205,

```
/-- **Gevrey ramp lemma**: `‖φ^{(k)}‖_{L¹} ≤ 2B·w·(A/w)^k·k^{sk}` (`k ≥ 1`, `2w ≤ L`). -/
theorem integral_abs_iteratedDeriv_phi_le (hϱ : GevreyProfile s A B ϱ) (hw : 0 < w)
    (hwL : 2 * w ≤ L) {k : ℕ} (hk : 1 ≤ k) :
    ∫ u, |iteratedDeriv k (phi ϱ L w) u| ≤ 2 * B * w * (A / w) ^ k * (k : ℝ) ^ (s * k) := by
```

and the interface `Params.GevreyPhiBound` (`Zeta23/Taper/GevreyPhi.lean` lines 17–27: `bound : ∀ k ≥ 1, ∫ ‖φ^{(k)}‖ ≤ 2·B·w·(A/w)^k·k^{sk}`), produced by `Params.gevreyPhiBound_of_profile` (`GevreyRamps.lean` line 237). The ramp lemma and the interface concern the paper's taper φ = ϱ((L/2 − |u|)/w), not this note's bump; they are quoted because they are the on-disk shape of the L¹-derivative-bound-to-transform-decay step that Lemma G performs for B, and because M4 (formalization, downstream) would consume them.

**What is used where.** Clauses 1–7 use only (0.1), (0.2) and Lemma G (whose input is `gevrey_expNegInvGlue`); they are statements about abstract sums over configurations and consume no explicit formula. Clause 8 uses `EF_lit_zetaZeroConfig` and `prop_EF_of_lit` to say what the datum is for ζ, and `zeta_local_zero_count_explicit` to place ζ in 𝒞(C₁).
