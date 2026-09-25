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

---

## §1 The localization theorem (H1): THEOREM F1, proved in full — and its numerical companion

**Verdict on H1: PROVED, in a form stronger and simpler than the brief's.** The brief's (a) is right for the right reason (the u = 0 singularity is the density at infinity, §0.2), its (b) is right and its reduction to even tests loses nothing (Lemma 0), and (b) holds at EVERY bandwidth L > 0 — not from some L on — and also for the height-modulated test family alone. Stop line (1) does not fire. Constants: none. Slack ledger: empty (every step is an identity, a limit, or a linear-independence statement).

### §1.1 Statement

**THEOREM F1 (no finite, windowed or periodic host for the conservation system).** Fix the archimedean functional A of §0.1 (axiom FE) and a bandwidth L > 0.

**(a) (Finite configurations.)** Let ν be a finite configuration (finitely many points of the closed strip, any marks, both symmetries). Then for every atomic datum π on {±log n} (positive or not), ν ∉ 𝒦_L(π): the system (0.1) fails on the dilated even bumps g_ε (§0.2) for every ε < min(L, log 2, 1), quantitatively

      |W_ν(g_ε)| ≤ ε·e^{ε/2}‖g‖₁·ν(S)   while   A(g_ε) − ∫g_ε dπ = A(g_ε) = g(0)·log(1/ε) + a(g) + o(1).

More generally, every ν ∈ 𝒦_L(π) satisfies W_ν(g_ε) = g(0)log(1/ε) + a(g) + o(1) as ε → 0: **membership in the class is a statement about the configuration at infinity** (its counting function must carry the archimedean density), read off at small u.

**(b) (Finite modifications of a solution are excluded at every bandwidth.)** Let ν₀ ∈ 𝒦_L(π₀) — for instance ζ's zero measure ν_ζ = Σ_ρ m_ρδ_{(ρ−½)/i} with π₀ = Λ, which lies in 𝒦_L(Λ) for every L > 0 by the Riemann–Weil explicit formula (C2 line 14 "For zeta this is the Riemann-Weil formula" `[record]`; the formal input is `EF_lit_zetaZeroConfig`, `Zeta23/WeilEF/Main.lean` 270, at g ∈ C²_c, zoo IV.18 clause (1) `[record]`). Let ν be a configuration such that μ := ν − ν₀ is a finite signed integer-atomic measure (finitely many points added, deleted, moved or re-marked, anywhere in the strip, the two symmetries kept), and let π be any atomic datum on {±log n}. If ν ∈ 𝒦_L(π), then **μ = 0 and Λ_π(n) = Λ_{π₀}(n) for every n with log n < L.** In particular the window-replacement configurations of the brief's H1(b) — ζ's zeros outside [T, T + W] together with any finite marked configuration inside — belong to no class 𝒦_L(π), for any L > 0 and any π, unless the inside configuration is ζ's own zeros with their marks.

**(b′) (The modulated family suffices.)** The conclusion of (b) holds if (0.1) is required only for the height-modulated tests g(u) = h(u)cos(Tu), h even ∈ C²_c(−L, L), at ONE height T (the reading of PRICING (1.2) with equality), with the weaker prime-side conclusion Λ_π(n) = Λ_{π₀}(n) for every n with log n < L and cos(T log n) ≠ 0.

**(c) (Periodic hosts.)** An N-periodic configuration is excluded by PRICING §1.2(b) `[record]`: "first-order rules read the Fourier SUPPORT of the counting measure (its transform must equal archimedean − π̂, supported on {± log n}), while a periodic configuration's support is the lattice {kℓ/N}, disjoint from {log n} except by coincidence" — the two-tooth rows force every lattice mode c_k, 1 ≤ k ≤ NL/ℓ, to vanish; banked as rider B on zoo IV.7, `[novelty: dual-model check 2026-09-10]` (BARRIER-ZOO.md line 422 read block) `[record]`. Nothing is added here; (c) is cited, not re-proved.

### §1.2 Proofs

*(a).* Let ν be finite with total mass ν(S) = Σm_γ. For the dilated bump g_ε(u) = g(u/ε), ĝ_ε(z) = εĝ(εz), and by the Paley–Wiener bound of §0.1 with supp g_ε ⊂ [−ε, ε] and |Im γ| ≤ ½: |ĝ_ε(γ)| ≤ εe^{ε/2}‖g‖₁. Summing, |W_ν(g_ε)| ≤ εe^{ε/2}‖g‖₁ν(S) → 0. On the right of (0.1), ∫g_ε dπ = 0 for ε < log 2 (the comb's first atoms sit at ±log 2), and A(g_ε) = g(0)log(1/ε) + a(g) + o(1) by the dilation law (0.3) (`[derivation]` in §0.2, `[computed]` in `verify/archimedean_kernel_check_run.log` (b): A(g_ε) − log(1/ε) = −0.694, −1.338, −1.466, −1.490, −1.4968, −1.4981 at ε = 0.5, 0.1, 0.02, 0.005, 0.001, 0.0002 for g = (1 − u²)³, the increments shrinking like ε). For g(0) = 1 the right side tends to +∞ and the left to 0, so (0.1) fails for all small ε. The "more generally" clause is (0.1) itself read on g_ε. ∎

*(b).* Subtract the system of ν₀ from that of ν: for every even g ∈ C²_c(−L, L),

      ⟨E_μ, g⟩ = W_ν(g) − W_{ν₀}(g) = [A(g) − ∫g dπ] − [A(g) − ∫g dπ₀] = ∫g d(π₀ − π) = Σ_{log n < L} c_n·2g(log n),   c_n := (Λ_{π₀}(n) − Λ_π(n))n^{−1/2}.

Both sides are even distributions on (−L, L), so by Lemma 0 the identity holds against every φ ∈ C_c^∞(−L, L): **E_μ = Σ_n c_n(δ_{log n} + δ_{−log n}) on (−L, L).** Now μ is finite, so E_μ(u) = Σ_{γ∈supp μ} μ({γ})cos(γu) is an entire function of u (§0.1), real and even. Test against φ supported in the open set U := (−L, L) ∖ {±log n : log n < L}: ∫E_μφ = 0 for all such φ, hence E_μ = 0 on U; U is dense in (−L, L) and E_μ is continuous, hence E_μ = 0 on (−L, L). Then, for φ ∈ C_c^∞(−L, L) peaked at log n (and, by evenness, at −log n) and vanishing at the other atoms, 0 = ⟨E_μ, φ⟩ = 2c_nφ(log n), so c_n = 0 for every n with log n < L: Λ_π(n) = Λ_{π₀}(n) there. Finally E_μ is entire and vanishes on an interval, so E_μ ≡ 0 on ℝ. Write E_μ(u) = Σ_{γ∈Γ} n_γcos(γu) with Γ ⊂ {Re γ ≥ 0, and Im γ ≥ 0 if Re γ = 0} a set of representatives of the sign classes {γ, −γ} in supp μ and n_γ ∈ ℤ the net integer weight of the class (the symmetry γ ↦ −γ of both ν and ν₀ makes μ symmetric, so this is well defined). Since 2cos(γu) = e^{iγu} + e^{−iγu} and the exponents {±γ : γ ∈ Γ} are pairwise distinct complex numbers, the functions e^{iλu} being linearly independent over ℂ for distinct λ (a nonzero finite exponential polynomial has isolated zeros — or: apply the differential operator Π_{λ′≠λ}(d/du − iλ′) to isolate one coefficient), every n_γ = 0: μ = 0. ∎

*Where marks enter.* A double at γ against two simples at γ, γ′ differ by μ = δ_γ − δ_{γ′} (with the symmetric images), E_μ = 2cos(γu) − 2cos(γ′u) ≢ 0. Nothing in the proof uses the positivity of π, the strip, or axiom RvM: finite modification is excluded for the purely analytic reason that a finite exponential sum is entire while the prime side is atomic. That is why the brief's (b), which invoked "linear independence of cos(λu) for distinct λ ≥ 0", needed no extra case: for complex γ the same independence holds, and the reflection symmetry only reduces the index set to sign classes.

*(b′).* With g = h(u)cos(Tu) the left side is ⟨E_μ·cos(T·), h⟩ and the right side Σ_n c_n cos(T log n)·2h(log n); E_μ(u)cos(Tu) is again a real even entire function, so the argument of (b) gives E_μ(u)cos(Tu) = 0 on (−L, L), hence E_μ = 0 on (−L, L) minus the zeros of cos(Tu) (isolated), hence on (−L, L), hence identically, hence μ = 0; and c_n cos(T log n) = 0 for log n < L. ∎

*(c).* Cited. ∎

### §1.3 What Theorem F1 does to the bilinear program of PRICING §1.1(v)

PRICING §1.1(v) `[record]`: "That is a bilinear program in (Λ_π(n) ≥ 0, positions, marks), not a filter on the A4 dictionary". Any instance of such a program has finitely many position/mark variables. Its configuration is then (a) finite — infeasible at every L > 0; (b) a finite modification of a fixed global solution (ζ's zeros outside a window, free inside) — feasible only at μ = 0, so the feasible set is the single point {ν₀|window, π₀} and the "optimum" is ν₀'s own N_d/N on the window (for ζ: 1, all simple, as far as computed); or (c) periodic — degenerate. **Corollary F1-C: the honest class has no finite instance; the bilinear program of PRICING §1.1(v) cannot be written with finitely many configuration variables; any non-uniqueness of 𝒦_L(π) — the only thing that could make "min N_d/N over the class" a question — is a property of INFINITE configurations, i.e. of E_ν outside the band and of the configuration at infinity.** `[derivation]` This is IV.7 rider B's statement one level up, as the brief anticipated: rider B kills the periodic host by SUPPORT (lattice against primes), F1(a) kills the finite host by the SINGULARITY at u = 0 (density at infinity), F1(b) kills the windowed host by ANALYTICITY (entire against atomic). `[novelty: single-check]` for the packaging; the mathematics of (a)–(b) is elementary and is not claimed as new (the brief's own (b) sketch; the literature's "finite exponential sums are entire" is folklore) — its consequence for the M5 program is what is new to the record.

### §1.4 The numerical companion — `verify/window_residual.py` → `window_residual_run.log`, `window_residual_out.json` `[computed]`

*Design (and a correction of the first version, recorded).* Zeros n = 3000…3039 by `mpmath.zetazero` (T = 3552.792 — the 40-zero mean; PRICING's 3630.9 was the 198-zero mean — ℓ = 6.3376, window length W = 39.186, mean gap 1.0048 against 2π/ℓ = 0.9914). The window's transform is c(u) = Σ_k e^{−iγ_ku} = e^{−iTu}S_ζ(u) with the ENVELOPE S_ζ(u) := Σ_k e^{−i(γ_k − T)u} band-limited to |ξ| ≤ W/2 (Nyquist spacing π/(W/2) = 0.160 in u), while c itself oscillates on the scale 2π/T = 0.0018. The first version of the script fitted c on a 0.013-grid — aliased — and excluded fixed 0.03-windows around every log n, which empties the grid beyond u ≈ 2.8 because the atoms log n become dense; its V.4 control then reported "positions 0.2 off with residual 10⁻¹⁰" — an artifact of an effectively L ≈ 2.8 fit of 40 free positions (under-determined by the count below), caught by the control and by an off-grid check (max |E| = 3.85 at a fit whose grid residual was 2.5·10⁻⁸). The version on disk fits the envelope: E(u) := S_c(u) − S_ζ(u), S_c(u) = Σ_j m_je^{−i(τ_j − T)u} for a marks-{1, 2} configuration of the same mass 40 with 7 doubles (N_d/N = 33/40 = 0.825, the nearest realization of 5/6 at N = 40) and with 6 doubles (0.85); grid spacing 0.02 on (0, L], excluding |u − log n| < 0.1/n (a fixed fraction of the local atom spacing, where a free positive π_L could absorb a mismatch); scipy `least_squares` (trf, analytic Jacobian), 12 starts per cell (8 merge-starts from ζ's own zeros, 4 random); every fit re-checked OFF the grid on a 0.005-grid including the excluded windows. Theorem F1(b) says E cannot vanish on any interval; the script measures how far from zero the best fit stays. 47 s.

*Result — the floor tracks the Slepian count.* With LW/π the number of real degrees of freedom of a function on a window of length W band-limited to (−L, L) (= 2αN in PRICING's units, since W = 2πN/ℓ) against the 33 (resp. 34) free positions:

| L | α = L/ℓ | count LW/π | 26s+7d: min RMS \|E\| (relative to RMS S) | off-grid max \|E\| | 28s+6d: relative |
|---|---|---|---|---|---|
| 0.5 | 0.079 | 6.2 | 1.8·10⁻⁹ (1.2·10⁻¹⁰) | 7.6·10⁻⁹ | 8.4·10⁻¹¹ |
| 1.0 | 0.158 | 12.5 | 2.3·10⁻⁸ (2.1·10⁻⁹) | 8.2·10⁻⁸ | 8.3·10⁻¹⁰ |
| 1.5 | 0.237 | 18.7 | 1.2·10⁻⁷ (1.3·10⁻⁸) | 3.4·10⁻⁷ | 5.1·10⁻⁹ |
| 2.0 | 0.316 | 24.9 | 4.7·10⁻⁵ (5.7·10⁻⁶) | 2.5·10⁻⁴ | 4.5·10⁻⁶ |
| 2.5 | 0.394 | 31.2 | 6.8·10⁻² (9.0·10⁻³) | 0.24 | 8.7·10⁻³ |
| 3.0 | 0.473 | 37.4 | 0.36 (5.0·10⁻²) | 1.7 | 4.6·10⁻² |
| 3.5 | 0.552 | 43.7 | 0.49 (7.2·10⁻²) | 0.92 | 6.4·10⁻² |
| 4.0 | 0.631 | 49.9 | 0.86 (0.13) | 2.4 | 0.10 |
| 5.0 | 0.789 | 62.4 | 1.10 (0.17) | 3.1 | 0.16 |
| 6.338 = ℓ | 1.000 | 79.1 | 1.96 (0.33) | 5.0 | 0.30 |
| 8.0 | 1.262 | 99.8 | 3.26 (0.53) | 7.2 | 0.48 |
| 12.0 | 1.893 | 149.7 | 3.55 (0.57) | 10.6 | 0.53 |

*Control (zoo V.4), 40 simple marks from a perturbed start (σ = 0.15):* at L = 1, 2 (count 12.5, 24.9 < 40) the fit finds OTHER positions (max deviation 0.22, 0.15 from ζ's zeros) with residual 1.8·10⁻⁷, 3.0·10⁻⁸ on and off the grid — the free regime, exhibited; at L = 3, 3.5, 5, ℓ, 12 (count 37.4 … 149.7) the ζ positions are recovered EXACTLY (residual 0.0, deviation 0.0): the instrument fires where it should and is silent where it should.

*Reading (`I infer` where marked).* (i) The theorem's "not zero" is 10⁻⁹–10⁻⁵ relative below the count and 1 %–57 % above it: **in a finite window the band data at α < ½ leave the marks free to all practical precision, and at α ≥ ½ they exclude a 1/6-doubles configuration by a margin that grows to more than half the transform's size at α ≥ 1.** (ii) The transition sits at count ≈ number of free positions — PRICING §1.1(iv)'s "2αN real numbers against N positions" `[record]` made visible: pinning by count at α = ½, not at α = 1. (iii) None of this is an honest instance (F1: the windowed system has no exact solution at any L); it is the count of §2, run on real zeros, and it is the shape the global question inherits height by height. (iv) The floor's smallness below the count is the prolate-spheroidal eigenvalue decay (§2.2, Landau–Pollak–Slepian): not a defect of the optimizer, a property of band-limited data (`I infer` the identification; the eigenvalues were not computed).

