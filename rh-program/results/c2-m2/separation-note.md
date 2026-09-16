# The Gevrey-localized single-defect separation theorem (Theorem M2, α = 2) with the tight-pair corollary: a theorem note

**Deliverable:** C2's first theorem under mandatory repair 2 (`directions/C2-rigidity-conservation.md` lines 39 and 74), built to the contract of `results/c2-m5/PRICING-next-unit.md` §2.2 under the brief `results/c2-m2/BRIEF.md` (with its addendum). Written 2026-09-16 (Session 22, Job 1, the author, Fable 5.1). Dual check owed to Job 2 (`results/c2-m2/check-O.md`) and two blind referee reports (`referee-F.md`, `referee-O.md`) before anything here is banked. Structure and tone follow `results/c2-r1/confinement-note.md`.

**Summary of what landed (details in §13).** The eight clauses are proved as contracted, with the constants carried honestly and eight dated deviations (§0.4), of which three are substantive: (D2) the Fourier-decay constant that the Lean derivative bounds actually give for the contract's bump is c_B = 2/√(72e) = 0.1430, not the pricing's inferred 0.20 (that number belongs to a different bump); (D3) with that c_B the reflected orbit at −t is provably negligible only when the height is large against the bandwidth, t ≥ 21L (a "reflection condition" enters the hypotheses; numerically it is vacuous for every t ≥ 3); (D5) the out-window radius is R = R₀L with R₀ = 81 for every L ≥ 50 (the contract's (3/(4c_B))²(1 + o(1)) = 27.5 is not what its own hypothesis yields; the asymptotic constant under that hypothesis is (7/(8c_B))² = 37.4). Clause 5 — the one live failure mode — HOLDS uniformly over depth |y| ≤ ½ (§6): the failure branch of PRICING §2.9 does not fire. The two-sided edge law is proved with κ₋ = 1.4810 (a closed form, log(√(π/2)e^{−1/4}/Z)) and κ₊ = 1.5311 for all λ ≥ 25 (§3); the pricing's 1.515 was a least-squares fit, not an asymptotic constant. The DH negative control (zoo V.4) FIRES: the datum separates DH's own off-line orbit at height 85.7 from the on-line configuration by a factor above the theorem's bound at the theorem's bandwidth (§8). Lint (KICKSTART 10(g)): the four banned hedges do not occur in the body of this note.

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

**D3 (substantive — the reflected orbit, 17:49 IST; proved in §4).** Clause 1 as contracted, |E₋| ≤ 2δ²c(δL)²e^{−L} "for all t ≥ 3", is provable from Lemma G only when the Gevrey suppression at real part 2tL beats the strip weight e^{δL} and the target e^{−L}: the sufficient "reflection condition" (R) of §4 is implied by t ≥ 21L (`lemma_G_constants_run.log` (e); the asymptotic threshold is t/L ≥ 1/(8c_B²) = 6.1). The theorem is therefore stated with (R) among its hypotheses; equivalently the admissible bandwidths at height t are L*(t, δ) ≤ L ≤ t/21, a nonempty range for every t ≥ 21L*(t, δ). With the numerically observed decay rate 0.8 the threshold would be t/L ≥ 0.2, vacuous for every t ≥ 3 and L ≥ 50 (computed, not proved). The theorem's truth is not in question at small t (§8's DH control at t = 85.7, L = 87 shows the reflected pair at 10⁻¹⁵ of the main term); its PROOF with the on-disk constants is.

**D4 (precision and route — the in-window tail, 17:49 IST; proved in §5).** (a) The count of points with 1 < |Re γ − t| ≤ R needs a factor 2 (both sides of t): the contract's T₁ ≤ C₁log(3 + t + R)·C_B²Σ… reads 2C₁ℓ_R·C_B²Σ…. (b) With c_B = 0.143 the Gevrey form of T₁ falls below b₁C₁ℓ_R/L² only from L ≈ 1.1·10⁴ (`lemma_G_constants_run.log` (f)); the transcript's own polynomial route (tx_032 (iii): |B̂(η)| ≤ ‖B‴‖₁/|η|³) gives T₁ ≤ 2ζ(4)‖B‴‖₁²C₁ℓ_R/L⁶ ≤ b₁C₁ℓ_R/L² for L ≥ L₁ := (2ζ(4)‖B‴‖₁²/b₁)^{1/4}, which is below 50 (§5; ‖B‴‖₁ computed in `b1_constant_run.log`). The polynomial route is the operative one; the contract's Gevrey form is also proved, with its honest L₁.

**D5 (substantive — R₀, 17:49 IST; proved in §6).** The contract's "R₀ := (3/(4c_B))²(1 + o(1))" is replaced by an explicit R₀ valid for every L ≥ 50: the out-window sum is bounded by 2C₁log(3.5 + t + k) per shell, and under the theorem's own L-hypothesis the prefactors are absorbed as 2C₁ ≤ e^{L/8}/b₁ and log(3.5 + t) ≤ 1.05e^{L/8}, which puts 7/4 (not 3/2) in front of L in the exponent to beat. Hence R₀ = (7/(8c_B))²(1 + o(1)) asymptotically, and the explicit value proved for all L ≥ 50 is **R₀ = 81** (`lemma_G_constants_run.log` (d); (7/(8c_B))² = 37.4, (3/(4c_B))² = 27.5). The o(1) is genuinely o(1) only if log(C₁log t) = o(L), which the hypothesis L ≥ 4δ⁻¹(log log(3+t) + …) does not guarantee; the contract's form would follow under the stronger L ≥ Kδ⁻¹(…) with K → ∞.

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

---

## §2 Lemma G — the Fourier decay of B, proved from the Lean derivative bounds

Write g(x) := exp(−1/x) for x > 0 and g(x) := 0 for x ≤ 0 (Mathlib's `expNegInvGlue`), and B_raw(v) := exp(−1/(1 − 4v²)) on |v| < ½, 0 elsewhere, so B = B_raw/Z.

**Lemma G0 (factorization).** B_raw(v) = g(4v + 2)·g(2 − 4v) for every real v.

*Proof.* For |v| < ½ put x := v + ½ ∈ (0, 1); then 1 − 4v² = (1 − 2v)(1 + 2v) = 2(1 − x)·2x = 4x(1 − x), and 1/(x(1 − x)) = 1/x + 1/(1 − x), so exp(−1/(1 − 4v²)) = exp(−1/(4x))exp(−1/(4(1 − x))) = g(4x)g(4(1 − x)) = g(4v + 2)g(2 − 4v). For |v| ≥ ½ one of 4v + 2, 2 − 4v is ≤ 0 and the product vanishes, as does B_raw. ∎ (Checked to 10⁻³¹ on a grid: `verify/lemma_G_constants_run.log` (a).) Note the contrast with the Lean bump θ(x) = g(x)g(1 − x): B_raw(v) = θ(v + ½)^{1/4}.

**Lemma G1 (derivative bounds for B_raw from `gevrey_expNegInvGlue`).** For every k ≥ 1 and every real v,
  |B_raw^{(k)}(v)| ≤ (k + 1)·A₁^k·k^{2k},  A₁ := 72/e = 26.487…,
and consequently ‖B_raw^{(k)}‖₁ ≤ (k + 1)A₁^k k^{2k} (the support has length 1).

*Proof.* (i) Affine chain rule: for a C^∞ function φ and constants a, b, the k-th derivative of v ↦ φ(av + b) is a^kφ^{(k)}(av + b) (induction on k; Mathlib has the special cases `iteratedDeriv_comp_const_sub` used at `Gevrey.lean` line 249 and the scalar version, but the note does not need to name them — the statement is the k-fold chain rule for an affine map). Hence with the Lean bound (P1), |g^{(k)}(x)| ≤ (18/e)^k k^{2k} for k ≥ 1 and all real x (`gevrey_expNegInvGlue`, §1; for k = 0, 0 ≤ g ≤ 1), the two factors of Lemma G0 satisfy |d^k/dv^k g(4v + 2)| ≤ 4^k(18/e)^k k^{2k} = A₁^k k^{2k} and the same for g(2 − 4v), with the convention 0⁰ = 1 for k = 0. (ii) Leibniz: B_raw^{(k)} = Σ_{i=0}^{k} C(k, i)·(d^i g(4v+2))·(d^{k−i} g(2 − 4v)), so |B_raw^{(k)}| ≤ Σ_i C(k, i) A₁^i i^{2i} A₁^{k−i}(k − i)^{2(k−i)} = A₁^k Σ_i C(k, i)[i^i(k − i)^{k−i}]². (iii) The binomial theorem applied to k^k = (i + (k − i))^k gives C(k, i) i^i (k − i)^{k−i} ≤ k^k for every 0 ≤ i ≤ k, and trivially i^i(k − i)^{k−i} ≤ k^i k^{k−i} = k^k. Hence each of the k + 1 terms is ≤ k^k·k^k = k^{2k}, and the sum is ≤ (k + 1)k^{2k}. ∎ (The Lean proof of `abs_iteratedDeriv_theta_le` bounds the same sum by 2^k k^{2k} — `gb_mul_gb_le` plus Σ_iC(k, i) = 2^k — which would give A = 144/e and the decay constant 1/(6√e) = 0.1011; step (iii) is the one improvement over the on-disk route, and it is elementary. Numerical sanity of G1 at k ≤ 6: ratios ≤ 0.03, log (b).)

**Lemma G (Fourier decay of B from the Lean bounds).** For every real η,
  (G1)  |B̂(η)| ≤ C_B·(1 + (c_B/2)√|η|)·exp(−c_B√|η|),  c_B := 2/√(72e) = 0.142961…,  C_B := e²/Z = 33.284…;
  (G2)  |B̂(η)| ≤ C_B′·exp(−c_B′√|η|),  c_B′ := (7/8)c_B = 0.125091…,  C_B′ := 4e^{−3/4}C_B = 62.890….
Moreover, for every complex ζ = ξ − iη′ (ξ, η′ real): |B̂(ζ)| ≤ e^{|η′|/2}·G(|ξ|), where G(η) denotes the right-hand side of (G1) (a nonincreasing function of η ≥ 0).

*Proof.* For real η ≠ 0 and k ≥ 1, k integrations by parts (B ∈ C^∞_c) give B̂(η) = ∫B(v)e^{iηv}dv = (−1/(iη))^k∫B^{(k)}(v)e^{iηv}dv, so |B̂(η)| ≤ ‖B^{(k)}‖₁/|η|^k ≤ (k + 1)A₁^k k^{2k}/(Z|η|^k) by Lemma G1; also |B̂(η)| ≤ ∫B = 1. Put κ := √(|η|/A₁)/e. If κ ≥ 1, take k := ⌊κ⌋ ≥ 1; then log(A₁^k k^{2k}/|η|^k) = k(log A₁ + 2log k − log|η|) ≤ k(log A₁ + 2log κ − log|η|) = −2k ≤ −2(κ − 1), and k + 1 ≤ κ + 1, so |B̂(η)| ≤ (e²/Z)(1 + κ)e^{−2κ}. Since 2κ = 2√|η|/(e√A₁) = c_B√|η| with c_B = 2/(e√(72/e)) = 2/√(72e), this is (G1). If κ < 1, i.e. c_B√|η| < 2, then |B̂(η)| ≤ 1 while the right side of (G1) is ≥ (e²/Z)e^{−2} = 1/Z > 1: (G1) holds for all η. (G2): for s ≥ 0, (1 + s/2)e^{−s/8} ≤ sup_{s≥0}(1 + s/2)e^{−s/8} = 4e^{−3/4} (the supremum is at s = 6), so (1 + s/2)e^{−s} ≤ 4e^{−3/4}e^{−7s/8} with s = c_B√|η|. The complex case: for ζ = ξ − iη′, |e^{iζv}| = e^{η′v} ≤ e^{|η′|/2} on the support, and the same k integrations by parts give |B̂(ζ)| ≤ e^{|η′|/2}‖B^{(k)}‖₁/|ζ|^k ≤ e^{|η′|/2}‖B^{(k)}‖₁/|ξ|^k; the choice of k as above with |ξ| in place of |η| gives e^{|η′|/2}G(|ξ|). Monotonicity of G: (1 + s/2)e^{−s} has derivative −(½ + s/2)e^{−s} < 0. ∎

*Numerical record (`lemma_G_constants_run.log` (c)).* (G1) and (G2) hold at every tested η ∈ [0, 1.6·10⁴] with margins of at least 10^{1.5}; the envelope of |B̂| decays at the numerical rate ≈ 0.85 per √η [computed, not proved], six times faster than c_B. The gap is the price of three generous steps — Cauchy's estimate on the circle |z − x| = x/2 (the Lean (18/e)^k k^{2k}, which numerically overestimates |g^{(k)}| by factors 10²–10⁸ at k ≤ 6, log (b)), the affine factor 4^k, and Leibniz. The pricing's inferred "c_B ≥ 0.20" is 1/(3√e), the constant one obtains from the Lean (36/e)^k k^{2k} for θ — which is not the contract's bump (D2). Nothing below uses the numerical rate.

**10(n) — nearest published object.** Lemma G is the standard statement "a Gevrey-2 function with derivative bounds ‖φ^{(k)}‖₁ ≤ C A^k (k!)² has |φ̂(η)| ≤ C′exp(−c√|η|)" (Rodino, *Linear partial differential operators in Gevrey spaces*, 1993, Ch. 1, or Hörmander, *The analysis of linear partial differential operators I*, §1.4, for the construction of such functions — both `[recalled, unverified; not read for this note]`); the exact difference is that here the derivative bound is the machine-checked (18/e)^k k^{2k} of `Zeta23/Taper/Gevrey.lean` transported to the contract's bump, the constants c_B, C_B are explicit, and the proof is the three lines above rather than a citation — so nothing rests on the recalled references.

---

## §3 Clause 2 (the two-sided edge law) and clause 3 (the slack), proved

### §3.1 The Laplace representation

For λ > 0, since B is even, c(λ) = ∫B(v)cosh(λv)dv = ∫B(v)e^{λv}dv. Substituting v = ½ − s (s ∈ (0, 1)) and 1 − 4v² = 4s(1 − s) (Lemma G0's computation):

  **c(λ) = e^{λ/2}·I(λ)/Z,  I(λ) := ∫_0^1 exp(−λs − 1/(4s(1 − s)))ds.**   (3.1)

Write 1/(4s(1 − s)) = 1/(4s) + 1/(4(1 − s)) and 1/(1 − s) = 1 + s + s²/(1 − s), so that with μ := λ + ¼,

  I(λ) = e^{−1/4}∫_0^1 e^{−μs − 1/(4s)}·e^{−s²/(4(1−s))}ds.   (3.2)

Define J(μ) := ∫_0^∞ e^{−μs − 1/(4s)}ds and J₂(μ) := ∫_0^∞ s²e^{−μs − 1/(4s)}ds. Substituting s = σ/√μ and then σ = ½e^θ (so σ + 1/(4σ) = cosh θ, dσ = ½e^θdθ):

  J(μ) = μ^{−1/2}K₁(√μ),  J₂(μ) = ¼μ^{−3/2}K₃(√μ),  where K_ν(x) := ∫_0^∞ e^{−x cosh θ}cosh(νθ)dθ   (3.3)

(for J: ½∫_ℝ e^{−x cosh θ}e^θdθ = ½∫e^{−x cosh θ}(cosh θ + sinh θ)dθ = K₁(x), the sinh part being odd; for J₂: σ²dσ = ⅛e^{3θ}dθ and ⅛∫_ℝ e^{−x cosh θ}e^{3θ}dθ = ¼K₃(x)). These are the standard integral representations of the modified Bessel functions, but nothing below uses any property of K_ν beyond the two elementary bounds of Lemma K, proved from the integral itself. (All of (3.1)–(3.3) are checked against mpmath's `besselk` to 12 digits at three values: `edge_law_two_sided_run.log` (0).)

**Lemma K (elementary two-sided bounds).** For every x > 0,
  √(π/(2x))e^{−x}(1 + 3/(8x) − 3/(16x²)) ≤ K₁(x) ≤ √(π/(2x))e^{−x}(1 + 3/(8x)),  K₃(x) ≤ √(π/(2x))e^{−x}(1 + 4.5/x + 9/x² + 7.5/x³).

*Proof.* cosh θ = 1 + 2sinh²(θ/2); substitute y = sinh(θ/2), dθ = 2dy/√(1 + y²): K₁(x) = 2e^{−x}∫_0^∞ e^{−2xy²}(1 + 2y²)(1 + y²)^{−1/2}dy. The factor (1 + 2y²)(1 + y²)^{−1/2} lies between 1 + (3/2)y² − y⁴ and 1 + (3/2)y²: the upper bound is (1 + 2y²)² ≤ (1 + y²)(1 + (3/2)y²)², i.e. 1 + 4y² + 4y⁴ ≤ 1 + 4y² + (21/4)y⁴ + (9/4)y⁶; the lower bound uses (1 + y²)^{−1/2} ≥ 1 − y²/2, which holds for y² ≤ 3 because (1 − y²/2)²(1 + y²) = 1 − (3/4)y⁴ + y⁶/4 ≤ 1 there, and trivially for y² > 2 where 1 − y²/2 < 0. The Gaussian moments ∫_0^∞ y^{2n}e^{−2xy²}dy = ½√(π/(2x))·(2n − 1)!!/(4x)^n (n = 0, 1, 2, 3: 1, 1/(4x), 3/(16x²), 15/(64x³)) give the two K₁ bounds. For K₃: cosh 3θ = 4cosh³θ − 3cosh θ = 4(1 + 2y²)³ − 3(1 + 2y²) = 1 + 18y² + 48y⁴ + 32y⁶ > 0, and dropping (1 + y²)^{−1/2} ≤ 1 gives K₃(x) ≤ 2e^{−x}∫e^{−2xy²}(1 + 18y² + 48y⁴ + 32y⁶)dy = √(π/(2x))e^{−x}(1 + 18/(4x) + 144/(16x²) + 480/(64x³)). ∎ (Numerical record, log (1): the ratios K₁/upper ∈ [0.9962, 1), K₁/lower ∈ (1, 1.0033], K₃/upper ∈ [0.946, 1) on x ∈ [5, 60].)

### §3.2 Clause 2

Put κ(λ) := log c(λ) − λ/2 + √λ + ¾log λ, so that clause 2 reads κ₋ ≤ κ(λ) ≤ κ₊, and

  **κ_∞ := log(√(π/2)·e^{−1/4}/Z) = 1.480883….**

**Theorem M2, clause 2 (edge law, two-sided).** For every λ ≥ 25,
  e^{λ/2}exp(−√λ − ¾log λ + κ₋) ≤ c(λ) ≤ e^{λ/2}exp(−√λ − ¾log λ + κ₊),  **κ₋ := κ_∞ = 1.48088,  κ₊ := κ_∞ + 1/(4√25) + 1/(128·25^{3/2}) = 1.53095.**
More precisely, for every λ ≥ 25: κ_∞ ≤ κ(λ) ≤ κ_∞ + 1/(4√λ) + 1/(128λ^{3/2}).

*Proof.* Upper bound. In (3.2) drop e^{−s²/(4(1−s))} ≤ 1 and extend the range to (0, ∞): I(λ) ≤ e^{−1/4}J(μ) = e^{−1/4}μ^{−1/2}K₁(√μ) ≤ e^{−1/4}√(π/2)μ^{−3/4}e^{−√μ}(1 + 3/(8√μ)) by Lemma K. Hence κ(λ) ≤ κ_∞ + (√λ − √μ) + ¾log(λ/μ) + log(1 + 3/(8√μ)). Now μ = λ(1 + 1/(4λ)) and √(1 + ε) ≥ 1 + ε/2 − ε²/8 for ε ≥ 0, so √λ − √μ ≤ −1/(8√λ) + 1/(128λ^{3/2}); log(λ/μ) ≤ 0; and log(1 + 3/(8√μ)) ≤ 3/(8√μ) ≤ 3/(8√λ). Adding: κ(λ) ≤ κ_∞ + 1/(4√λ) + 1/(128λ^{3/2}), which is decreasing in λ and equals 1.53095 at λ = 25.

Lower bound. In (3.2) restrict to s ∈ (0, a] with a := ½ and use e^{−z} ≥ 1 − z and s²/(4(1 − s)) ≤ s²/(4(1 − a)) = s²/2 there:
  I(λ) ≥ e^{−1/4}∫_0^{a}e^{−μs − 1/(4s)}(1 − s²/2)ds ≥ e^{−1/4}[J(μ) − ∫_a^∞ e^{−μs}ds − ½J₂(μ)] = e^{−1/4}[μ^{−1/2}K₁(√μ) − e^{−μ/2}/μ − ⅛μ^{−3/2}K₃(√μ)].
By Lemma K, with x = √μ, this is ≥ e^{−1/4}√(π/2)μ^{−3/4}e^{−√μ}·[1 + 3/(8√μ) − 3/(16μ) − E₁(λ) − E₂(λ)], where
  E₁(λ) := √(2/π)·μ^{−1/4}·e^{√μ − μ/2},  E₂(λ) := (1/(8μ))(1 + 4.5/√μ + 9/μ + 7.5/μ^{3/2})
(E₁ is the tail term e^{−μ/2}/μ divided by the main factor; E₂ is ⅛μ^{−3/2}K₃ divided by it, using √(π/(2√μ)) = √(π/2)μ^{−1/4}). Hence
  κ(λ) ≥ κ_∞ + (√λ − √μ) + ¾log(λ/μ) + log(1 + u(λ)),  u(λ) := 3/(8√μ) − 3/(16μ) − E₁(λ) − E₂(λ),
and √λ − √μ ≥ −1/(8√λ) (from √μ ≤ √λ + 1/(8√λ)), ¾log(λ/μ) = −¾log(1 + 1/(4λ)) ≥ −3/(16λ). It remains to show D(λ) := −1/(8√λ) − 3/(16λ) + log(1 + u(λ)) ≥ 0 for λ ≥ 25. For λ ≥ 25: 0 < u ≤ 3/(8·5) = 0.075, so log(1 + u) ≥ u − u²/2 ≥ 0.9625u; √μ ≤ 1.005√λ gives 3/(8√μ) ≥ 0.3731/√λ; 3/(16μ) ≤ 3/(16λ); E₂(λ) ≤ (1/(8λ))(1 + 0.9 + 0.36 + 0.06) ≤ 0.29/λ; and E₁ is decreasing. So D(λ) ≥ 0.9625(0.3731/√λ − 3/(16λ) − 0.29/λ) − 1/(8√λ) − 3/(16λ) − 0.9625E₁(λ) ≥ 0.234/√λ − 0.647/λ − 0.9625E₁(λ) = (0.234√λ − 0.647)/λ − 0.9625E₁(λ) ≥ 0.52/λ − 0.9625E₁(λ). Finally λE₁(λ) ≤ 25E₁(25) = 0.0045 for λ ≥ 25 (E₁(λ) ≤ 0.8e^{−1.51√λ}, and λe^{−1.51√λ} is decreasing for λ ≥ 25), so D(λ) ≥ (0.52 − 0.0045)/λ > 0. ∎

*Numerical record (`edge_law_two_sided_run.log` (2)).* On 90 values λ ∈ [25, 10⁴] the exact κ(λ) (30-digit quadrature) lies between the proved lower bound (with E₁, E₂ evaluated) and the proved upper bound: at λ = 25, 1.50251 ≤ 1.51051 ≤ 1.52046 (the exact upper chain) ≤ 1.53095; at λ = 100, 1.49961 ≤ 1.50127 ≤ 1.50589; at λ = 10⁴, 1.48333 ≤ 1.48334 ≤ 1.48338. The lower bound exceeds κ_∞ by at least 0.0024 on the table (D(λ) > 0). **Gap to the contract's number (D6):** the pricing's 1.515 is the constant of a two-parameter least-squares fit (slope −1.0012, reproduced in the log); the proved band is [1.4809, 1.5310], containing every exact value, and the true asymptotic constant is κ_∞ = 1.4809. |κ± − 1.515| ≤ 0.035: stop condition (a) does not fire; λ₀ = 25 stands.

### §3.3 Clause 3

**Theorem M2, clause 3 (slack; c₀ = ½).** For every λ ≥ λ₀ = 25, c(λ)² ≥ e^{(1−c₀)λ} = e^{λ/2}.

*Proof.* By clause 2, c(λ)² ≥ e^{λ}exp(−2√λ − (3/2)log λ + 2κ_∞), so it suffices that m(λ) := λ/2 − 2√λ − (3/2)log λ + 2κ_∞ ≥ 0 for λ ≥ 25. m(25) = 12.5 − 10 − 4.828 + 2.962 = 0.6335 > 0 and m′(λ) = ½ − 1/√λ − 3/(2λ) ≥ ½ − 1/5 − 3/50 = 0.24 > 0 for λ ≥ 25. ∎ (Numerical record, log (3): the proved margin e^{m(25)} = 1.884 against the computed c(25)²/e^{12.5} = 1.999; the proved inequality holds from λ = 23 on, the contract's λ₀ = 25 is kept. The pricing's "2√λ ≤ c₀λ iff λ ≥ 16" (§2.1(c)) is the same balance without the log and constant terms.)

*Reading (repair 2).* The killer's inconsistency (C2 line 70) was that the design's polynomial edge law e^{λ/2}(c/λ)^{k+1} and the Gevrey taper could not coexist. Clauses 2–3 use one class, the Gevrey-2 bump, and its own law e^{λ/2}exp(−√λ − ¾log λ + κ): the loss against e^{λ/2} is e^{−√λ}λ^{−3/4}, and the slack (1 − c₀)λ = λ/2 absorbs it from λ = 25 (proved) — the contract's "the (1 − c₀)δL slack absorbs the Gevrey loss" is now a theorem with κ₋ = 1.4809.

---

## §4 Clause 1 — the orbit clause, with the four-point accounting and the reflection condition

**Theorem M2, clause 1 (orbit clause).** Let t > 0, 0 < δ ≤ ½, L > 0, and let Z contain the orbit {±t ± iδ} (each point with multiplicity one). The four orbit points contribute to W_Z(f_{t,L}) exactly

  −2δ²c(δL)² + E₋,  E₋ = 2Re[h_f(−t − iδ)·conj(h_f(−t + iδ))],  |E₋| ≤ 2(4t² + δ²)·e^{δL}·G(2tL)²,

with G the majorant of Lemma G. If moreover δL ≥ 25 and the **reflection condition**

  (R)  2c_B√(2tL) − 2log(1 + (c_B/2)√(2tL)) ≥ L + 2√(δL) + (3/2)log(δL) − 2κ₋ + log((4t² + δ²)C_B²/δ²)

holds — in particular if **t ≥ 21L** (then (R) holds for every δ ∈ [25/L, ½]) — then |E₋| ≤ 2δ²c(δL)²·e^{−L}, which is the contract's form.

*Proof.* The exact contribution is §0.2: the pair at +t gives −2δ²c(δL)², the pair at −t gives E₋. For the bound: by (0.1), h_f(−t ∓ iδ) = (−2t ∓ iδ)B̂(L(−2t ∓ iδ)), and Lemma G's complex case with ξ = −2tL, η′ = ±δL gives |B̂(L(−2t ∓ iδ))| ≤ e^{δL/2}G(2tL); hence |h_f(−t ∓ iδ)| ≤ √(4t² + δ²)e^{δL/2}G(2tL) and |E₋| ≤ 2|h_f(−t − iδ)||h_f(−t + iδ)| ≤ 2(4t² + δ²)e^{δL}G(2tL)². For the contract's form: by clause 2 (δL ≥ 25), c(δL)² ≥ e^{δL}exp(−2√(δL) − (3/2)log(δL) + 2κ₋), so |E₋| ≤ 2δ²c(δL)²e^{−L} follows from (4t² + δ²)G(2tL)² ≤ δ²e^{−L}exp(−2√(δL) − (3/2)log(δL) + 2κ₋), i.e. — taking logarithms with G(2tL)² = C_B²(1 + (c_B/2)√(2tL))²e^{−2c_B√(2tL)} — from (R). Finally, for δ ∈ [25/L, ½] one has 2√(δL) ≤ √(2L), (3/2)log(δL) ≤ (3/2)log(L/2), δ⁻² ≤ L²/625 and 4t² + δ² ≤ 4t² + ¼, so (R) is implied by

  (R′)  2c_B√(2tL) − 2log(1 + (c_B/2)√(2tL)) ≥ L + √(2L) + (3/2)log(L/2) − 2κ₋ + log((4t² + ¼)C_B²L²/625).

At t = 21L the difference (left − right) of (R′) equals 0.717 at L = 50 and is nondecreasing in L (its derivative is at least 2c_B√42 − 1 − 0.93/(1 + 0.46L) − 1/√(2L) − 3/(2L) − 4/L > 0.5 for L ≥ 50; checked on a fine grid to 1.3·10⁵, `lemma_G_constants_run.log` (e)), and the left side of (R′) grows with t faster than the right side (√t against log t), so t ≥ 21L suffices for every L ≥ 50. ∎

*Numerical record (`lemma_G_constants_run.log` (e); `four_point_accounting_run.log` (2)).* The least t satisfying (R′) is T₁(L) = 1040, 1383, 2073, 3457, 7389, 6.4·10⁴ at L = 50, 100, 200, 403, 1000, 10⁴ (T₁/L → 1/(8c_B²) = 6.12). The actual reflected pair is far smaller than the bound: at t = 30, δ = 0.3, L = 40 (where (R) fails by a wide margin) the direct quadrature gives |E₋|/(2δ²c²) = 7.8·10⁻²⁷ against e^{−L} = 4.2·10⁻¹⁸; at DH's (t, δ, L) = (85.7, 0.3085, 87), §8 finds the same order. **(D3.)** The contract's "for all t ≥ 3" is therefore replaced, in the theorem's hypotheses, by (R) — a condition that with the numerical decay rate 0.85 would read t ≥ 0.17L (vacuous for t ≥ 3, L ≥ 50; computed, not proved) and with the proved c_B reads t ≥ 21L. What the theorem loses is the range 3 ≤ t < 21L*(t, δ): heights below ≈ 21·L*(t, δ), i.e. (at δ = 0.1) below ≈ 8·10³. Nothing is lost at the heights of the numerics campaign (t = 10⁶: t/L* = 2478).

*What the clause does not say.* It does not assert that E₋ is small in absolute terms for t < 21L (it is, numerically, but that is not proved here); it asserts an explicit bound on E₋ for every (t, δ, L), and the contract's form under (R).

---

## §5 Clause 4 — the in-window on-line noise, with b₁ re-derived and the tail T₁ by two routes

**The constant b₁.** b₁ := sup_{η∈ℝ}|ηB̂(η)|². Its value is **b₁ = 8.64613** (attained at η* = 4.6727; the pricing's 8.646123549 at η = 4.675 on a coarser grid differs by 5·10⁻⁶), with the certified enclosure 8.64613 ≤ b₁ ≤ 8.6981 (`verify/b1_constant_run.log`: grid maximum on [0, 40] at step 10⁻² refined to 10⁻⁵ near the maximizer, plus the Lipschitz increment |d/dη(ηB̂)| ≤ 1 + η∫|v|B = 1 + 0.16723η per cell, plus the tail |ηB̂(η)| ≤ ‖B″‖₁/η ≤ 0.72 for η ≥ 40) and the hand-proved bound b₁ ≤ ‖B′‖₁² = 10.984 (tx_032's). Also from the same log: ‖B′‖₁ = 3.31428, ‖B″‖₁ = 28.7726, **‖B‴‖₁ = 642.301** (sign changes of B‴ on (0, ½) at 0.30527 and 0.44757; 30-digit quadrature on the sign-constant pieces). The three norms and b₁ are computed constants (`computationally-verified` in the zoo's V.3 vocabulary); every inequality below that uses them has slack far beyond the 0.6 % width of b₁'s enclosure, and the theorem may be read with b₁ replaced by 8.70 throughout at no visible cost.

**Theorem M2, clause 4 (in-window on-line noise).** Let Z ∈ 𝒞(C₁), t ≥ 3, L ≥ 50 and R ≥ 1, and suppose every point of Z with |Re γ − t| ≤ R other than the orbit {±t ± iδ} is real. Then, with ℓ_R := log(4 + t + R),

  0 ≤ N_Z := Σ_{γ∈Z real, |γ − t| ≤ R}|h_f(γ)|² ≤ b₁C₁ℓ_R/L² + T₁,  T₁ ≤ min(T₁^{poly}, T₁^{Gev}),

  T₁^{poly} := 2ζ(4)‖B‴‖₁²C₁ℓ_R/L⁶,  T₁^{Gev} := 2C₁ℓ_R·Σ_{k≥1}(k + 1)²G(Lk)² = 2C₁ℓ_R C_B²Σ_{k≥1}(k + 1)²(1 + (c_B/2)√(Lk))²e^{−2c_B√(Lk)},

and T₁ ≤ b₁C₁ℓ_R/L² for L ≥ L₁ := (2ζ(4)‖B‴‖₁²/b₁)^{1/4} = 17.9 — so for every L ≥ 50, **N_Z ≤ 2b₁C₁ℓ_R/L²**.

*Proof.* Every term is |h_f(γ)|² = (γ − t)²B̂(L(γ − t))² ≥ 0 by (0.1). Shell k = 0: the points with |γ − t| ≤ 1 number at most C₁log(3 + t) ≤ C₁ℓ_R, and each term is (L(γ − t))²B̂(L(γ − t))²/L² ≤ b₁/L². Shells k ≥ 1: the points with k ≤ |γ − t| < k + 1 lie in the two intervals [t + k, t + k + 1) and (t − k − 1, t − k], each contained in a window {|x − y| ≤ 1} of the class definition centered at y = t ± (k + ½), so their number is at most 2C₁log(3.5 + t + k) ≤ 2C₁ℓ_R for k ≤ R (D7). Polynomial route (tx_032 (iii)): three integrations by parts give |B̂(η)| ≤ ‖B‴‖₁/|η|³, so each term is ≤ (γ − t)²‖B‴‖₁²/(L|γ − t|)⁶ ≤ ‖B‴‖₁²/(L⁶k⁴); summing 2C₁ℓ_R‖B‴‖₁²L⁻⁶Σ_{k≥1}k⁻⁴ = T₁^{poly}. Gevrey route: each term is ≤ (k + 1)²G(Lk)² by Lemma G (G nonincreasing), giving T₁^{Gev}. T₁^{poly} ≤ b₁C₁ℓ_R/L² iff L⁴ ≥ 2ζ(4)‖B‴‖₁²/b₁ = 1.033·10⁵, i.e. L ≥ 17.9. ∎

*Reading and record.* The shell count needs the factor 2 the contract omitted (D4(a)). The contract's Gevrey form T₁^{Gev} is proved as stated (with the polynomial prefactor of (G1)), but with c_B = 0.143 it drops below b₁C₁ℓ_R/L² only from L ≈ 1.1·10⁴ (`lemma_G_constants_run.log` (f)); the transcript's polynomial route does it from L₁ = 17.9, and is the one the assembly uses (D4(b)). In the transcript, with an unspecified C³ bump, the tail was "≤ b₃A′₀log(t₀ + 3)/L⁶ with b₃ = ‖B‴‖₁²" — the same bound with the constants now explicit (‖B‴‖₁² = 4.13·10⁵, which is why L₁ is 18 and not 2). Numerical instance (`four_point_accounting_run.log` (3)): at L = 40 two real points at distances 0.55 and 1.3 from t contribute 3.1·10⁻⁴ and 5.8·10⁻⁶ against b₁/L² = 5.4·10⁻³.

---

## §6 Clause 5 — the out-window contamination, uniform over depth |y| ≤ ½ (the one live failure mode: it does not fail)

**Theorem M2, clause 5 (out-window contamination).** (a) Pointwise, for every point γ = x − iy of the strip (|y| ≤ ½) and every L > 0, with u := |x − t|:

  |h_f(γ)·conj(h_f(conj γ))| ≤ (u + ½)²·e^{L/2}·G(Lu)² = (u + ½)²·e^{L/2}·C_B²(1 + (c_B/2)√(Lu))²·exp(−2c_B√(Lu)),

and with (G2) in place of (G1) the contract's form (u + ½)²e^{L/2}C_B′²exp(−2c_B′√(Lu)). (b) Summed: let Z ∈ 𝒞(C₁), t ≥ 3, and L ≥ 50 with L ≥ 8(log log(3 + t) + log(2b₁C₁)) (the theorem's L-hypothesis implies this). Then for R := R₀L with **R₀ := 81**,

  S_Z := Σ_{γ∈Z, |Re γ − t| ≥ R}|h_f(γ)·conj(h_f(conj γ))| ≤ e^{−L},

the sum converging absolutely. The same R₀ works for every L ≥ 50; for L ≥ L₀ the smaller values R₀(L₀) of the table below suffice, and R₀(L₀) → (7/(8c_B))² = 37.46 as L₀ → ∞.

*Proof.* (a) By (0.1) and Lemma G's complex case, |h_f(γ)| = |x − t − iy|·|B̂(L(x − t) − iLy)| ≤ √(u² + y²)·e^{L|y|/2}G(Lu) ≤ √(u² + ¼)·e^{L/4}G(Lu), and the same bound holds for h_f(conj γ) (conj γ = x + iy, same u, same |y|). Multiply. Since √(u² + ¼) ≤ u + ½, (a) follows; G(Lu)² ≤ C_B′²e^{−2c_B′√(Lu)} is (G2). The strip weight e^{L|y|/2} per factor is at most e^{L/4} at the maximal depth |y| = ½: **the bound is uniform over the depth**, which is what the transcript's argument (polynomial decay e^{L/4}/|x|³, tx_032 (iv)) lacked and Gevrey decay supplies — at u ≥ R₀L the factor exp(−2c_B√(Lu)) ≤ exp(−2c_B√R₀·L) beats e^{L/2} by a fixed exponential margin.

(b) Shells. A point with |Re γ − t| ≥ R lies in a shell k ≤ u < k + 1 with k ≥ ⌊R⌋ ≥ R − 1 =: u₀; the shell holds at most 2C₁log(3.5 + t + k) points (as in §5), each bounded by (a) with (u + ½)² ≤ (k + 3/2)² and G(Lu) ≤ G(Lk). With log(3.5 + t + k) ≤ log(3.5 + t) + k (since log(1 + k/a) ≤ k/a ≤ k for a ≥ 1),

  S_Z ≤ 2C₁e^{L/2}[log(3.5 + t)·Σ₂ + Σ₃],  Σ_m := Σ_{k≥u₀}(k + 3/2)^{m}G(Lk)²   (m = 2, 3; using k(k + 3/2)² ≤ (k + 3/2)³).

Absorption of the prefactors through the L-hypothesis: 2C₁ ≤ e^{L/8}/b₁ (from L/8 ≥ log(2b₁C₁)) and log(3.5 + t) ≤ 1.05·log(3 + t) ≤ 1.05e^{L/8} (from L/8 ≥ log log(3 + t); the 1.05 covers log(3.5 + t)/log(3 + t) ≤ 1.045 for t ≥ 3). Hence S_Z ≤ (e^{3L/4}/b₁)(1.05Σ₂ + Σ₃), and it remains to bound the two sums.

The sums. For k ≥ u₀: (k + 3/2)^m ≤ β^m k^m with β := 1 + 3/(2u₀). The function φ_m(u) := u^m(1 + (c_B/2)√(Lu))²e^{−2c_B√(Lu)} has (log φ_m)′(u) = m/u + (c_B√L/(2√u))/(1 + (c_B/2)√(Lu)) − c_B√L/√u ≤ (m + 1)/u − c_B√L/√u < 0 for u > (m + 1)²/(c_B²L) — which holds on [u₀, ∞) since u₀ ≥ R₀·50 − 1 > 16/(c_B²·50) = 15.7. So Σ_m ≤ β^mC_B²[φ_m(u₀) + ∫_{u₀}^∞φ_m(u)du], and with u = s²/L,

  ∫_{u₀}^∞φ_m(u)du = (2/L^{m+1})∫_{s₀}^∞ s^{2m+1}(1 + (c_B/2)s)²e^{−2c_B s}ds,  s₀ := √(Lu₀),

a combination of three incomplete-gamma integrals ∫_{s₀}^∞s^ne^{−as}ds = e^{−as₀}Σ_{j=0}^{n}(n!/j!)s₀^j a^{−(n+1−j)} with a = 2c_B and n = 2m + 1, 2m + 2, 2m + 3 (coefficients 1, c_B, c_B²/4).

The relaxation that makes "for all L ≥ L₀" a one-point check. With R = R₀L: s₀ = √(L(R₀L − 1)) ≥ √R₀·L − 1/√R₀ (from √(1 − ε) ≥ 1 − ε), so e^{−2c_B s₀} ≤ e^{2c_B/√R₀}e^{−2c_B√R₀·L}; and u₀ ≤ R₀L, s₀ ≤ √R₀L in every polynomial factor; β ≤ 1 + 3/(2(R₀L₀ − 1)) for L ≥ L₀. Therefore

  S_Z ≤ e^{2c_B/√R₀}·e^{(3/4 − 2c_B√R₀)L}·P(L)/b₁,

where P is an explicit polynomial in L with nonnegative coefficients and degree 5 (from φ₃(u₀) ≤ (R₀L)³(1 + (c_B/2)√R₀L)² and from the j = 9 term of the m = 3 integral, (2/L⁴)·(√R₀L)⁹/a). Put F̃(L) := (7/4 − 2c_B√R₀)L + 2c_B/√R₀ + log(P(L)/b₁); then S_Z ≤ e^{−L} iff F̃(L) ≤ 0 (up to the relaxations, which only enlarge the bound). Since P has nonnegative coefficients, (log P)′ ≤ 5/L, so F̃ is decreasing on [5/(2c_B√R₀ − 7/4), ∞). Consequently: **if F̃(L₀) ≤ 0 and 5/(2c_B√R₀ − 7/4) ≤ L₀, then S_Z ≤ e^{−L} for every L ≥ L₀.** `verify/lemma_G_constants.py` (d) computes P exactly and finds the least R₀ (step ½) satisfying both conditions at L₀ = 50: R₀ = 81, with F̃(50) = −0.133 and F̃ decreasing from L = 6.1 on; F̃(L) at R₀ = 81 is −7.48, −37.9, −280, −767, −8166 at L = 60, 100, 403, 1000, 10⁴. Absolute convergence of the full sum W_Z(f) over Z ∈ 𝒞(C₁) is the same computation without the truncation at R. ∎

*Table (`lemma_G_constants_run.log` (d)) — R₀ as a function of the least admissible bandwidth L₀:* R₀(50) = 81, R₀(100) = 58.5, R₀(200) = 48, R₀(403) = 43, R₀(1000) = 40, R₀(10⁴) = 38 (each proved for all L ≥ L₀ by the one-point check plus the decrease). The limit is (7/(8c_B))² = 37.46 (D5); the contract's (3/(4c_B))² = 27.52 would need log(C₁log t) = o(L), which the L-hypothesis does not provide. **For the record, not used:** with the numerical decay rate 0.85 the same chain gives (7/(8·0.85))² ≈ 1.06 — the contract's "numerical c_B ≈ 0.8 would give R₀ ≈ 0.9" is of this size.

*Why the failure branch of PRICING §2.9 does not fire.* The transcript's gap was that polynomial decay ‖(B_Le^{yu})‴‖₁/|x|³ ~ e^{L/4}/|x|³ cannot beat e^{L/4} at any polynomial |x|, so it fell back to an exponential exclusion zone e^{L/8} or to global isolation. Lemma G's decay exp(−c_B√(L|x|)) at |x| = R₀L is exp(−2c_B√R₀·L) per pair of factors, an exponential in L with a coefficient (2c_B√R₀ ≥ 2.6) that exceeds the strip weight's ½ plus the target's 1 plus the absorbed prefactors' ¼ — uniformly in the depth, because the depth enters only through e^{L|y|/2} ≤ e^{L/4}. Clause 5 holds at every depth up to ½, with the window radius R₀L linear in L (α = 2: R = C_αL^{α−1} = C₂L, C2 line 39's form). The price of the honest c_B is R₀ = 81 instead of 14; the shape is unchanged.

*Hypothesis check (Job 2's item): what the proof uses.* Exactly: (i) Z is a multiset in |Im γ| ≤ ½ (the strip weight), (ii) the local count #{|Re γ − x| ≤ 1} ≤ C₁log(3 + |x|) for all x (the shell counts), (iii) L ≥ 50 and L ≥ 8(log log(3 + t) + log(2b₁C₁)) (the absorption). Nothing about the points inside the window, nothing about conjugation or reflection invariance, nothing about the orbit. ζ's configuration satisfies (ii) with C₁ = 5.4·10⁸ by `zeta_local_zero_count_explicit` (§1; the count there is of ordinates in (t, t + 1], which covers windows of length 2 by two applications); the Davenport–Heilbronn configuration satisfies (ii) with some C₁ by the Riemann–von Mangoldt formula for a Dirichlet series with functional equation and a Γ-factor of the same shape as ζ's `[recalled, unverified — the standard argument (Titchmarsh Ch. 9 for ζ) applies verbatim; no on-disk source; §8 uses only a finite window of DH zeros computed directly]`.

---

## §7 Clauses 6, 7, 8 — the assembly, the tight pair, the scope

### §7.1 The theorem, assembled (clause 6)

**Theorem M2 (Gevrey-localized single-defect separation; α = 2).** Constants: c₀ = ½, λ₀ = 25, C₀ = 4, b₁ = sup|ηB̂|² = 8.6461 (§5), c_B = 2/√(72e), C_B = e²/Z (§2), R₀ = 81 (§6), κ₋ = 1.4809, κ₊ = 1.5310 (§3). Let C₁ ≥ 1, t ≥ 3, 0 < δ ≤ ½, and

  L ≥ max(λ₀/δ, C₀δ⁻¹(log log(3 + t) + 2log(1/δ) + log(2b₁C₁)))  and  (R) of §4 (implied by t ≥ 21L);

put R := R₀L and ℓ_R := log(4 + t + R). Let Z, Z′ ∈ 𝒞(C₁) be such that within |Re γ − t| ≤ R all points of Z′ are real, while Z contains the orbit {±t ± iδ} and is otherwise real there; outside the window both are arbitrary. Then clauses 1–5 hold as stated in §§3–6, and

  **|W_Z(f_{t,L}) − W_{Z′}(f_{t,L})| ≥ 2δ²c(δL)²(1 − e^{−L}) − 2[b₁C₁ℓ_R/L² + T₁] − 2e^{−L} ≥ δ²e^{(1−c₀)δL} ≥ 1.**

Bandwidth-L first-order data separate the two classes.

*Proof.* Split each datum into the orbit part (Z only), the in-window real part and the out-window part: W_Z = (−2δ²c² + E₋) + N_Z + O_Z and W_{Z′} = N_{Z′} + O_{Z′}, with 0 ≤ N_Z, N_{Z′} ≤ b₁C₁ℓ_R/L² + T₁ =: N (clause 4; the hypothesis L ≥ λ₀/δ ≥ 50 covers L₁ = 17.9, and the reflected double or any other real point of Z′ is part of N_{Z′} or O_{Z′}) and |O_Z|, |O_{Z′}| ≤ e^{−L} (clause 5; its L-hypothesis L ≥ 8(log log(3 + t) + log(2b₁C₁)) follows from the displayed one since 4/δ ≥ 8 and 2log(1/δ) ≥ 0). Hence W_Z − W_{Z′} ≤ −2δ²c² + |E₋| + N + 2e^{−L}, so W_{Z′} − W_Z ≥ 2δ²c² − |E₋| − N − 2e^{−L} ≥ 2δ²c²(1 − e^{−L}) − 2N − 2e^{−L}, using clause 1 under (R) and N ≤ 2N (D8). For the second inequality: clause 3 at λ = δL ≥ 25 gives c² ≥ e^{δL/2}, and clause 4 gives N ≤ 2b₁C₁ℓ_R/L²; so it suffices that

  δ²e^{δL/2}(1 − 2e^{−L}) ≥ 4b₁C₁ℓ_R/L² + 2e^{−L}.   (7.1)

From the L-hypothesis, δL/2 ≥ 2(log log(3 + t) + 2log(1/δ) + log(2b₁C₁)), so e^{δL/2} ≥ (log(3 + t))²δ⁻⁴(2b₁C₁)² and δ²e^{δL/2} ≥ 4b₁²C₁²(log(3 + t))²/δ² ≥ 4b₁C₁·(log(3 + t))²·4 (using b₁C₁ ≥ 8.6 and δ ≤ ½). Since ℓ_R = log(4 + t + R₀L) ≤ log(4 + t) + log(1 + R₀L) ≤ 1.1log(3 + t) + L (for t ≥ 3 and R₀L ≤ e^L − 1, true at L ≥ 50) and L ≥ 50, one has ℓ_R/L² ≤ (1.1log(3 + t) + L)/L² ≤ 0.0005log(3 + t) + 0.02 ≤ 0.02log(3 + t) ≤ (log(3 + t))², so 4b₁C₁ℓ_R/L² ≤ 4b₁C₁(log(3 + t))², which is a quarter of the lower bound just obtained; the terms 2e^{−L} and 2e^{−L}·δ²e^{δL/2} are below 10⁻²⁰ of it (L ≥ 50). This proves (7.1) with room, hence ≥ δ²e^{δL/2}. Finally δ²e^{δL/2} ≥ 1 iff δL/2 ≥ 2log(1/δ), which the L-hypothesis gives with a factor 2 to spare (D8). ∎

*The constants' chain (10(g)), checked for cycles.* Z (quadrature) → b₁, ‖B‴‖₁, κ_∞ (computed / closed form); Lean (18/e) → A₁ = 72/e → c_B, C_B (Lemma G) → R₀ (clause 5; also uses b₁ for the absorption), the reflection constant 21 (clause 1; also uses κ₋), L₁ (clause 4; uses ‖B‴‖₁, b₁); κ₋ → λ₀ = 25 (clause 3); c₀ = ½ → C₀ = 2/(1 − c₀) = 4 (the balance (7.1)). No constant depends on a later one. *Slack ledger:* clause 3's margin e^{0.6335} = 1.88 at λ = 25 (§3.3); (7.1) holds with a factor ≥ 4 and the e^{−L} terms are ≤ 10⁻²⁰ of the main term; clause 5's F̃(50) = −0.133 (a margin of e^{0.133} at L = 50, growing like e^{0.9L}); the reflection condition at t = 21L has margin 0.72 nats at L = 50.

*What the theorem says and does not say.* (a) It is a statement about two abstract configurations and one explicit test; nothing arithmetic enters. (b) The window is large: R = R₀L ≈ 81·L (at δ = 0.1, t = 10⁶: L* = 403 and R ≈ 3.4·10⁴; the table of §6 gives R₀(403) = 43, R ≈ 1.7·10⁴). Within it, Z′ must be entirely on-line and Z on-line except for the orbit; the theorem does not control two configurations that both carry off-line points inside the window (the transcript's "clusters" and "interference" paragraphs, tx_033, describe what happens then: they add to the same negative direction or interfere, and the datum's sign is no longer decided by one defect). (c) It says nothing for t < 21L (D3) as proved; numerically the reflected pair is negligible there (§4, §8). (d) It uses no explicit formula: for ζ, what the datum W_ζ(f) equals in terms of primes is clause 8.

### §7.2 Clause 7 — the tight-pair corollary

**Theorem M2, clause 7 (tight pair).** Under the hypotheses of clause 6, let Z′ carry, in place of nothing, an on-line double at ±t (the points t and −t each with multiplicity two) and be otherwise as before. Then the same bound holds: |W_Z(f) − W_{Z′}(f)| ≥ δ²e^{δL/2} ≥ 1.

*Proof.* h_f(t) = (t − t)B̂(0) = 0 by (0.1), so the double at +t contributes 0 to W_{Z′}(f). The double at −t contributes 2·2|h_f(−t)|² = 16t²B̂(2tL)² ≥ 0 (D9), a real point of Z′ inside or outside the window, counted in N_{Z′} or O_{Z′} of clause 6's proof (the density hypothesis Z′ ∈ 𝒞(C₁) is on Z′ with the double). Nothing else changes. ∎

*Reading (C2 line 70, the killer's minor, adopted).* Zoo II.4 (`BARRIER-ZOO.md` lines 134–146), quoted: "On configurations of orthonormal on-line atoms (integer m_j ≤ c) plus b pair-blocks of eigenvalue c: 2c·tr(P+Q) − ‖P+Q‖²_F = Σ_j k_c(m_j) + c²b EXACTLY (k_c(p) = c² − ((c−p)₊)²) — the rank-trace certificate is saturated, and at c = 2 an on-line DOUBLE zero (k₂(2) = 4) is indistinguishable from an off-line pair at depth → 0 (charge 4). `Zeta23/ZeroSide/TightMult.lean` (lemmaR_tight, lines 93–122). Tightness is relative to the invariant list {tr, ‖·‖²_F, atom norms ≤ 1, n₊}". Clause 7 separates the double at t from the pair {t ± iδ} by the first-order datum W_Z(f_{t,L}) at bandwidth L*(t, δ). Three things this does and does not mean. (i) The datum is a single first-order sum rule evaluated at one test, not a function of {tr, ‖·‖²_F, n₊, integrality}: it is **outside II.4's data class**, so II.4's tightness — a theorem about that list — is untouched; no formalized no-go is "moved". (ii) **The separation degenerates as δ → 0**: L* ≥ max(25/δ, 4δ⁻¹(log log(3 + t) + 2log(1/δ) + log(2b₁C₁))) → ∞, and at fixed L the orbit's contribution −2δ²c(δL)² → 0 like δ² — this is II.4's "depth → 0" regime, in which the first-order datum also goes blind; the corollary is a separation at explicit positive depth with an explicit bandwidth, nothing more (the referee's "tight-pair marketing" minor, answered by stating the degeneration). (iii) The depth-continuity check II.4 asks for ("any separation claim must be depth-uniform or priced over the depth family") is priced: L*(t, δ) is the price, and it is not uniform in δ.

### §7.3 Clause 8 — scope: what the theorem does not say

**Theorem M2, clause 8 (scope).** Clauses 1–7 are statements about zero-side sums Σ_Zĝ(γ) of abstract configurations; they consume neither axiom P (Λ ≥ 0) nor any prime-side estimate, nor the explicit formula. Applied to ζ's configuration Z_ζ (which lies in 𝒞(5.4·10⁸) by `zeta_local_zero_count_explicit`), the datum is, by `EF_lit_zetaZeroConfig` and `prop_EF_of_lit` (§1) with k = g = f ⋆ f̃ (C^∞, compactly supported — the two hypotheses of `EF_lit`),

  W_{Z_ζ}(f) = Σ_ρ m_ρĝ(γ_ρ) = ĝ(i/2) + ĝ(−i/2) + (1/2π)∫ĝ(r)[Re ψ(¼ + ir/2) − log π]dr − Σ_nΛ(n)n^{−1/2}(g(log n) + g(−log n)),

and clause 6 says: if ζ had an orbit at (t, δ) and were otherwise on-line within R₀L* of t (and if t ≥ 21L*), this quantity would differ by at least 1 from its value on the on-line configuration obtained by deleting the orbit. Evaluating the prime sum on the right pointwise at height t — a Dirichlet polynomial of length e^{L*} = e^{403} at δ = 0.1, t = 10⁶, to absolute accuracy 1 — is the M6 detector behind the pointwise short-Dirichlet-polynomial wall (C2 line 64; mandatory repair 6, C2 line 74: "name the Lindelöf lock as a wall SHARED with the campaign residue — claim only the single-defect regime as new territory"; zoo IV.7's Session-6 closure, `BARRIER-ZOO.md` line 392: the cubic route "CLOSED at the proven operating point", the lock named there for the second-order system; and the referee's "does not compose", C2 line 71). **Not part of M2.** The theorem's content for ζ is the zero-side statement; its prime-side evaluation is a separate milestone with its own wall.
