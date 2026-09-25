# D1(b) — the honest M5 experiment: the FORMULATION slot (Session 27, queue item 2; writer Fable 5.1; Opus 5 reader to follow)

Opened Fri Sep 25 21:22:05 IST 2026. Brief: `results/c2-m5b/BRIEF.md` (SHA-256 91cba22ffbb9e9774fdc112ca666057595fe90f337a39c180bba0952fce16976, verified at open). Written to disk by section as each lands; a dated block goes to `results/c2-m5b/SHARED.md` after each. Scripts and logs: `results/c2-m5b/verify/`. Nothing outside `results/c2-m5b/` is edited; proposed texts only (§6, §7). Nothing is committed by the writer.

**Labels used** (the M2 note's discipline, `results/c2-m2/separation-note.md` §0): `[record]` = quoted from an on-disk result or direction file at the line named; `[read at the page]` = a printed source opened this session, page or line named; `[computed]` = a script under `verify/` with its log; `[derivation]` = proved in this note; `[recalled, unverified]` = literature from memory, never load-bearing; `I infer` = the writer's inference, not on the record; `[novelty: single-check]` = a novelty or prior-art claim awaiting the Opus reader (standing order 7).

**Reading order for the reader.** §0 (the object), §1 (Theorem F1 and its numerical companion), §2 (the global class and the gap literature — the place where the brief's H2 is wrong and where a mistake would be), §3 (the ladder, rung 1 computed), §4 (Krein and the band-limited Weil criterion), §5 (the contract theorem), §6 (zoo protocol), §7 (DECISION), §8 (honesty), §9 (lint).

---

## §0 The contract as the referee would state it (KICKSTART 10(g))

### §0.1 Conventions (one normalization; every script under `verify/` uses it)

* **Transform.** For an even g ∈ C²_c(ℝ) and z ∈ ℂ, ĝ(z) := ∫_ℝ g(u)e^{izu}du = ∫_ℝ g(u)cos(zu)du. This is C2 line 14's "ghat" and the M2 note's h_g (`separation-note.md` §0.1, the Lean `paperFT`); because g is even the sign of the exponent is immaterial, ĝ(−z) = ĝ(z), ĝ(z̄) = conj ĝ(z), and ĝ is real on ℝ and on iℝ. Two integrations by parts give ĝ(z) = −z^{−2}∫g″(u)e^{izu}du, so for supp g ⊂ [−L, L]: |ĝ(x − iy)| ≤ e^{L|y|}·min(‖g‖₁, ‖g″‖₁/|z|²). `[derivation]`
* **The datum (π, A)** — C2 line 14 verbatim `[record]`: "An admissible datum is a pair (pi, A): pi = sum_n Lambda(n) n^{-1/2} (delta_{log n} + delta_{-log n}) a POSITIVE measure with Chebyshev growth pi([0,x]) <= C e^{x/2} (axiom P — this is the (S1) input), and A the archimedean functional A(g) = ghat(i/2)+ghat(-i/2) + Int ghat(tau) mu_inf(tau) dtau, mu_inf(tau) = (2pi)^{-1} Re psi(1/4+i tau/2) - (log pi)/2pi (axiom FE)." Throughout, Λ_π(n) ≥ 0 denotes the datum's coefficients and π_L its restriction to n < e^L; ζ's datum is Λ_π = Λ. A is FIXED by axiom FE (it is ζ's; the degree-2 variant for ζ_K is §3 rung 3).
* **Configurations.** A configuration is a positive integer-atomic measure ν = Σ_{γ∈Z} m_γδ_γ, m_γ ∈ ℤ_{≥1}, on the closed strip S := {γ ∈ ℂ : |Im γ| ≤ ½}, locally finite, invariant under γ ↦ γ̄ and γ ↦ −γ with marks preserved (C2 line 14: "invariant under z -> z-bar and z -> -z, written Z = sigma + D"; dictionary γ = (ρ − ½)/i, `separation-note.md` §0.1). Z := supp ν. A point with Im γ ≠ 0 lies in a four-point orbit {±x ± iy} (two-point if x = 0). The class 𝒞(C₁), C₁ ≥ 1: #{γ ∈ Z : |Re γ − x| ≤ 1} ≤ C₁log(3 + |x|) for every real x, counted with marks and over all depths (axiom RvM; for ζ, C₁ ≤ 2.4·10⁹, C2 Instruments row "ζ's density constant C₁" `[record]`).
* **The zero side and its u-side reading.** For ν as above and even g ∈ C²_c, W_ν(g) := Σ_γ m_γĝ(γ) converges absolutely (the bound of the first bullet against the density of 𝒞(C₁)). E_ν denotes the even distribution on ℝ with ⟨E_ν, g⟩ = W_ν(g) — formally E_ν(u) = Σ_γ m_γe^{iγu}; for a FINITE ν it is the entire function E_ν(u) = Σ_γ m_γcos(γu), real and even by the two symmetries (a four-point orbit contributes 4m·cos(xu)cosh(yu), an on-line pair ±τ contributes 2m·cos(τu)). `[derivation]`
* **The conservation system** — C2 line 14 `[record]`: "for every even g in C^2_c with supp g in [-L,L]: Sum_{gamma in Z} ghat(gamma) = A(g) - Int g d(pi)". In the notation above:

      W_ν(g) = A(g) − ∫g dπ   for every even g ∈ C²_c with supp g ⊂ [−L, L].        (0.1)

### §0.2 The u-side of the datum: the archimedean kernel, its singularity, and the distribution F_π

**(0.2) The archimedean functional in the u-variable.** For even g ∈ C²_c,

      A(g) = ∫_ℝ g(u)·2cosh(u/2) du + A_∞(g),
      A_∞(g) := ∫_ℝ ĝ(τ)μ_∞(τ)dτ = −∫_0^∞ [g(u)e^{u/2} − g(0)]/sinh u · du − (log 4π + γ_E)·g(0).        (0.2)

`[read at the page]` Bombieri 2000 (bdim copy, SHA-256 20bd544f…, `Rend. Lincei` (9) 11, Theorem 2, p. 193 of the volume): T[f] = ∫_0^∞f + ∫_0^∞f* − Σ_nΛ(n){f(n) + f*(n)} − (log 4π + γ)f(1) − ∫_1^∞[f(x) + f*(x) − (2/x)f(1)]·x dx/(x² − 1) equals Σ_ρ f̃(ρ) over all complex zeros; with f(x) := x^{−1/2}g(log x), f*(x) = x^{−1}f(1/x) = x^{−1/2}g(−log x) = f(x), the substitution x = e^u gives ∫f + ∫f* = ∫g(u)·2cosh(u/2)du, Σ_nΛ(n){f(n) + f*(n)} = ∫g dπ_ζ, and the last integral equals ∫_0^∞[g(u)e^{u/2} − g(0)]/sinh u · du (since [f(x) + f*(x)]x/(x² − 1) = 2e^{−u/2}g(u)e^{2u}/(e^{2u} − 1) = g(u)e^{u/2}/sinh u and (2/x)f(1)·x/(x² − 1) = g(0)/sinh u). `[derivation]` **Numerically verified** against the direct integral ∫ĝμ_∞ with mpmath's digamma for two C² bumps, `verify/archimedean_kernel_check.py` → `archimedean_kernel_check_run.log` `[computed]` (values in the log; agreement to the quadrature tolerance stated there).

Writing ∫_0^∞[g(u)e^{u/2} − g(0)]/sinh u · du = ∫_0^∞(g(u) − g(0))e^{u/2}/sinh u · du + c₁g(0), c₁ := ∫_0^∞(e^{u/2} − 1)/sinh u · du = 2.26394350735… `[computed]`, the kernel of A is the even distribution

      K_A = 2cosh(u/2)·du − c_A·δ₀ − ½·fp[e^{|u|/2}/sinh|u|],   c_A := log 4π + γ_E + c₁ = 5.37218341922…,        (0.2′)

where fp[·] is the finite part regularized by subtracting g(0) (as displayed). **The singularity.** e^{|u|/2}/sinh|u| = 1/|u| + O(1) at u = 0, so K_A = −½·fp(1/|u|) + (a locally integrable even function) + (a multiple of δ₀) near 0: **K_A is not a measure near u = 0.** Its operational form is the **dilation law**: for even g ∈ C²_c with supp g ⊂ [−1, 1] and g_ε(u) := g(u/ε),

      A(g_ε) = g(0)·log(1/ε) + a(g) + o(1)   as ε → 0,   a(g) an explicit constant.        (0.3)

`[derivation]`: substitute u = εv in (0.2′): −½∫(g(v) − g(0))·ε e^{ε|v|/2}/sinh(ε|v|)dv → the integrand tends to (g(v) − g(0))/|v| on |v| ≤ 1 and to −g(0)/|v| on 1 ≤ |v| ≲ 1/ε, where ∫_1^{1/ε}dv/v = log(1/ε); the cosh term is O(ε); the δ₀ term is fixed. Equivalently, from the τ-side: ∫ĝ_εμ_∞ = ∫ĝ(s)μ_∞(s/ε)ds and μ_∞(s/ε) = (2π)^{−1}log(s/(2πε)) + O(ε²/s²), with (2π)^{−1}∫ĝ = g(0). **Reading:** the u = 0 singularity of the archimedean kernel IS the Riemann–von Mangoldt density (1/2π)log(τ/2π) of the datum, read at small u; any configuration satisfying (0.1) at any bandwidth L > 0 must reproduce (0.3) on the zero side, W_ν(g_ε) = g(0)log(1/ε) + O(1) for ε < min(L, log 2) — a statement about ν at INFINITY (its counting function), not about any window. `[computed]`: the same script tabulates A(g_ε) − g(0)log(1/ε) at ε = 0.5, 0.1, 0.02, 0.005, 0.001 and shows convergence to a(g).

**(0.4) The distribution F_π and the class.** F_π := K_A − π, an even distribution on ℝ (the comb π = Σ_nΛ_π(n)n^{−1/2}(δ_{log n} + δ_{−log n}) has its first atoms at ±log 2 = ±0.693…, so near u = 0 F_π is K_A alone). Then (0.1) reads ⟨E_ν − F_π, g⟩ = 0 for all even g ∈ C²_c(−L, L), i.e. **E_ν = F_π on (−L, L) as even distributions.**

**LEMMA 0 (even tests suffice).** If T is an even distribution on (−L, L) and ⟨T, g⟩ = 0 for every even g ∈ C²_c(−L, L), then T = 0 on (−L, L). *Proof.* For any φ ∈ C_c^∞(−L, L) write φ = φ_e + φ_o; ⟨T, φ_o⟩ = 0 because T is even, and ⟨T, φ_e⟩ = 0 by hypothesis (φ_e ∈ C²_c). A distribution vanishing on C_c^∞(−L, L) is zero. ∎ `[derivation]` Both E_ν and F_π are even (ν's two symmetries; K_A and π even), so the reduction of (0.1) to even tests loses nothing. This is the step the brief's stop line (1) asks about; it does not fire (§1).

### §0.3 Normalized units, the honest class, the honest M5, and the Frobenius functional

* **Height and mean gap.** T > 0 a height, ℓ := log(T/2π), so that μ_∞(T) = ℓ/2π + O(T^{−2}) is the mean density of ζ's zeros at T (C2 line 14 `[record]`; PRICING §1.1(ii)) and the mean gap is 2π/ℓ. Window [T, T + W]; N := ν([T, T + W]) (the MASS in the window, counted with marks; for ζ, N = Wℓ/2π + O(log T)); N_d := the number of DISTINCT points of Z in the window. The two-moment extremal has 2/3·N simple points and 1/6·N doubles: N_d/N = 5/6 (SPEC §0 line 13 via PRICING §1.1(i) `[record]`). Marks-{1, 2} configurations are the LP's dictionary; the honest class allows every mark.
* **Bandwidth.** L > 0 the bandwidth of the test class in (0.1); α := L/ℓ(T). The LP's "bandwidth 1" (PRICING (1.3): lattice u_k = kℓ/N, 1 ≤ k ≤ N) is u ∈ (−ℓ, ℓ), i.e. α = 1 `[record]`; α = ½ is u ∈ (−ℓ/2, ℓ/2). Because ℓ depends on T and L does not, **α is a function of height at fixed L**: α(T) = L/log(T/2π) → 0 as T → ∞. This one line is what §2 turns on.
* **DEFINITION (the honest class, the brief's 𝒦_L(π) — PRICING §1.1(v) `[record]` made global).** For a datum (π, A) and L > 0,

      𝒦_L(π) := { ν : a configuration (as in §0.1) in 𝒞(C₁) for some C₁, with E_ν = F_π on (−L, L) }.

  PRICING §1.1(v)'s object — "configurations Z on a window [T, T + W] (NOT periodized) such that there EXISTS a positive measure π_L on {± log n : n ≤ e^L} with Chebyshev growth for which Σ_{γ∈Z} ĝ(γ) = A(g) − ∫ g dπ_L for all even C² g with supp g ⊂ [−L, L]" — is the union over π_L ≥ 0 of these classes; §1 proves that no configuration supported on a window belongs to any of them, so the class is stated globally here, as the brief's H2 anticipates.
* **The honest M5.** For ν ∈ 𝒦_L(π), a height T and a window length W, write d_{T,W}(ν) := N_d/N over [T, T + W]. The honest M5 of PRICING §1.1(v) ("min N_d/N over the class, subject to ζ's Λ²-mean-value") is

      m(L; T, W) := inf { d_{T,W}(ν) : ν ∈ 𝒦_L(π_L), π_L ≥ 0 on {±log n : n < e^L} with ζ's Λ²-mean-value },

  and the question is whether m(L; T, W) > 5/6 for some L (the two-moment extremal excluded at that bandwidth), "no finite L" being the honest NO (digest §D D1, free design parameter `[record]`). The datum for ζ itself is π_L = Λ|_{n<e^L}.
* **The Frobenius functional in the honest class — a functional of F_π alone, up to out-of-band leakage.** `[derivation]` The windowed transform of the configuration is ĉ_{T,W}(u) := Σ_{γ∈Z, Re γ∈[T,T+W]} m_γe^{−iuγ} (on-line points at frequency Re γ; an orbit contributes its four terms, the cosh(yu) of PRICING (1.3)); the LP's coefficients are c_k = ĉ_{T,W}(u_k) up to the rotation phase (SPEC §1.4 `[record]`), and the Frobenius row tr Ĝ₁² = m₂(1)N = (4/3)N is a positive quadratic form in {|c_k|² : |u_k| ≤ ℓ} (PRICING §1.1(i) `[record]`). Now ĉ_{T,W} = E_ν ∗ ŵ_W with w_W the window's indicator (or a C² taper of it) and ŵ_W(u) = e^{−iu(T+W/2)}·2sin(uW/2)/u — an exact identity of distributions, because multiplying ν by the window is convolving its transform by the window's transform. Split E_ν = F_π·1_{(−L,L)} + E_ν·1_{|u|≥L} (legitimate on the class: E_ν = F_π on (−L, L)). Hence, for |u| ≤ ℓ,

      ĉ_{T,W}(u) = (F_π·1_{(−L,L)} ∗ ŵ_W)(u) + R_{T,W}(u),   R_{T,W} := (E_ν·1_{|v|≥L}) ∗ ŵ_W,        (0.5)

  and every two-moment row (|c_k|² at |u_k| ≤ ℓ) is a functional of **F_π and of the leakage R alone**. R is the sinc-tail contribution of the configuration's transform OUTSIDE the band; it is the ONLY channel through which the configuration's freedom enters any two-moment row, and for L ≥ ℓ it is a tail term (the window kernel at distance ≥ L − ℓ from the band edge; with a C² taper, decay (W(L − ℓ))^{−3} per unit of out-of-band mass). The first term carries the mean-density row (from the 2cosh(u/2) − c_Aδ₀ − ½fp part of K_A at u ≈ 0, which contributes the diagonal N = Wℓ/2π + O(1)) and the Λ²-mean-value: the comb's self-pairing Σ_n Λ_π(n)²n^{−1}·|ŵ_W|²-weights, which for π = Λ is Montgomery's F(α) = α on |α| ≤ 1 and gives κ(1) = 1 + 1/3 = 4/3 (SPEC §2.1 "the paper's unconditional prime-side κ(λ) EXACTLY" `[record]`; the identification of the diagonal with the Λ² mean value is Montgomery's, `[recalled, unverified]` as to the page, not load-bearing here). **Consequences stated for the record.** (i) In the honest class at α ≥ 1 the Frobenius row is not a constraint on the configuration beyond membership plus leakage; "subject to ζ's Λ²-mean-value" is a constraint on π_L. (ii) The two-moment LP is the relaxation that keeps |ĉ_{T,W}(u_k)|² and forgets arg ĉ_{T,W}(u_k) and the support of E_ν (PRICING §1.1(v), §1.2(b) `[record]`); but on the honest class both the modulus AND the argument of the first term of (0.5) are the DATUM's, not the configuration's — the configuration's own freedom lives in R, i.e. in |u| ≥ L. So "the phases are the new coordinate" (brief H5) must be read as: the phases of the band transform are the datum's, and what a certificate on the honest class prices is how R, the out-of-band content, can or cannot realize marks. §5 says what that costs.

### §0.4 The §F sentences this note is bound by (digest `results/program-digest-s25.md` §F, quoted verbatim with their line numbers) `[record]`

* Line 310, sentence 1 — **The amendment** (STATUS.md line 33): "Nothing forbids a route through existing tools in a new combination if a mechanism appears; the zoo says where not to look, not what to build."
* Line 311, sentence 2 — **The criterion** (STATUS.md line 33): "we really need to go further, wider, and deeper than what's already been done" — "a route is funded only if it starts beyond the ground the zoo already marks as covered".
* Line 314, sentence 5 — **The ladder rule** (KICKSTART.md line 69): "Any new instrument (S1–S5 spec) is first run on the rungs where the answer is KNOWN — function fields (RH true), Epstein / Davenport–Heilbronn (RH false), then Dirichlet L — and the write-ups are fed verbatim into the ζ brief. A brief that skips the ladder is returned."
* Line 315, sentence 6 — **M2's restricted sentence** (`results/c2-m2/check-O.md` §12.11, line 555): "*this* separation theorem cannot, without an arithmetic input, tell which configuration is ζ's: clauses 1–7 hold verbatim for DH (rung 2), so no consequence of them distinguishes ζ's configuration from DH's".
* Line 319, sentence 10 — **IV.1's executable test** (line 364): "Write the proposal's prime-computable observables explicitly; attempt to express each as (classical Weil test at bandwidth log X) × (multiplier bounded above and below on the band). Success of the expression = the route has no new data coordinate".
* Line 321, sentence 12 — **I.1's axiom-level requirement** (line 52): "PASS (for a full-RH brief) = at least one consumed input **provably fails** for DH/Epstein at the axiom level, with the failure named".
* Line 322, sentence 13 — **I.8's KILLS (ii)** (line 109): "Any S1 claim for a Λ ≥ 0-consuming first-order instrument that does not name an input the Siegel-zero world violates; there is none in {P, FE, RvM}."

### §0.5 Scope declaration (zoo §0 item 1) and the five hypotheses

Scope: **instrument** (digest §E rank 3: "its NO is a barrier"); a proportion-scope statement would be the YES, a Group-IV candidate the NO; no full-RH claim anywhere in this note. The orchestrator's hypotheses H1–H5 (brief, each `I infer` there) are decided in §1–§5 respectively and tabulated in §7; none is accepted on the brief's word.

