# NOTE — unit `qcond-s38`: a Beurling system with Riemann's exact FE at conductor q > 1 — construct or refute (Q_cond)

Session 38, 2026-10-01. Writer: Opus 5.5 (unit agent). Built section by section as results landed; the close is §5.
Conventions (as in the parent NOTE `novel-wave-s37/beurling-fe/NOTE.md`, cited below as "BFE"): every load-bearing claim is
(P) proved here, (C) computed in `verify/` with its log, or (Q) quoted from a file on disk at the line. `[recalled, unverified]`
marks statements that carry no load. Novelty: `[novelty: single-check]`.

## 0. The question, the digest's ranking, the headline

Setting (BFE §8(b)). dN ≥ 0 on [1, ∞) with polynomial growth, F(s) = ∫x^{−s}dN(x), Λ_F(s) = (q/π)^{s/2}Γ(s/2)F(s) satisfying (A):
Λ_F(s) = Λ_F(1 − s), poles only at 0 and 1 (simple), growth (G′). Beurling: dN = exp*(dΠ), dΠ ≥ 0 on (1, ∞) (multiplicative
exponential), so dN({1}) = 1. Theorem C (BFE): q ≥ 1, q = 1 only for ζ, and at q > 1 the identity (C_q) holds.
**Q_cond.** Is there a Beurling system (discrete, continuous or mixed; weights allowed) with Riemann's exact FE at some q > 1?

Digest ranking of this unit: see §0.1 (filled at the close; the digest `novel-wave-s37/insights-digest.md` was not on disk at start).

Headline: see §5 (filled at the close).

## 1. Task 1 — positive self-dual measures with an atom at 0 and a gap (−r, r)

### 1.1 The class and the reduction (P)
Fix r ∈ (0, 1). 𝓜_r := {μ ≥ 0 tempered on R : μ̂ = μ, μ|_{(−r,r)} = ρδ₀ for some ρ ≥ 0} (convention f̂(ξ) = ∫f(x)e^{−2πixξ}dx).
REDUCTION (BFE Prop. R and the proof of Theorem C, used verbatim). Under (A) at conductor q, with ν := image of dN under
t ↦ t/√q (carried by [r, ∞), r = q^{−1/2}) and ρ_q := √q·Res_{s=1}F, the even measure μ_q := ρ_qδ₀ + ν + ν^∨ lies in 𝓜_r;
conversely μ ∈ 𝓜_r with μ|_{(0,∞)} carried by [r, ∞) gives, by rescaling, a measure dN on [1, ∞) whose F satisfies (A) at q = r^{−2}.
N(x) = O(x) and F converges absolutely for Re s > 1 (BFE §3). So Q_cond asks: which μ ∈ 𝓜_r have ν = scaled exp*(dΠ), dΠ ≥ 0?

### 1.2 Examples in 𝓜_r (P, with the checks in `verify/v1_selfdual_examples.{py,log}` (C))
(a) POISSON PAIRS. For a ∈ [r, 1/r]: π_a := δ_{aZ} + a^{−1}δ_{Z/a} ∈ 𝓜_r, mass 1 + 1/a at 0 (Poisson: FT δ_{aZ} = a^{−1}δ_{Z/a}).
    The closed convex cone 𝒦_r they generate (positive measures m on [r, 1/r], μ = ∫π_a dm(a)) lies in 𝓜_r. In Dirichlet-series
    terms, with b = √q·a ∈ [1, q]: F(s) = ζ(s)·∫(b^{−s} + √q b^{−1}(q/b)^{−s})dm, i.e. F = ζ·D with D(1 − s) = q^{s−½}D(s).
    The brief's q = 4 example: Σ_nδ_{n/2} + 2Σ_nδ_{2n} = π_{1/2} ∈ 𝓜_{1/2} — CHECKED (v1: theta relation to 1e−40 at y = 0.37, 1, 2.2;
    Fejér pairing at widths L = 0.3, 0.7, 1.3, 2.9 within the explicit ξ^{−2} tail bound). It is ζ(s)(1 + 2^{1−2s}), mass 3 at 0.
    Generally ζ(s)(1 + q^{½−s}) ↔ π_r (mass 1 + √q). F_{5,5} = ζ(s)(1 + 5·5^{−s} + 5^{1−2s}) ↔ π_{1/5} + (5/2)π_1 ∈ 𝓜_{1/5}
    (v1: both pairings, mass 11 = ρ_q at 0). If m is continuous, ∫π_a dm(a) has its only atom at 0 (for x ≠ 0 the set of a
    with x ∈ aZ ∪ a^{−1}Z is countable) — so 𝓜_r contains measures that are continuous off the origin.
(b) TWISTED COMBS (signed, gap-free). For χ a real even primitive character mod m, τ_χ := Σ_{n∈Z}χ(n)δ_{n/√m} is self-dual
    (v1: m = 5, 8, 12, 13, both pairings; the Gauss sum of such χ is √m `[recalled, used only as the reason; the check is (C)]`).
    Positive combinations with Poisson pairs lie in 𝓜_r and leave 𝒦_r: e.g. ζ(s)(1 + 5^{½−s}) + L(s, χ₅) (coefficients
    1 + χ₅(n) + √5·1_{5|n} ≥ 0, q = 5; checked in the parent unit, `novel-wave-s37/beurling-fe/verify-O/o5_*.log`).
(c) So 𝓜_r ⊋ 𝒦_r: it contains 𝒦_r and the positive members of the span of Poisson pairs and twisted combs with a gap (all
    generalized Dirac combs in Meyer's sense, §1.3). None of the examples is a Beurling system (BFE §8(b); §3–§4 below).

### 1.3 What is in print (Q; paths under `novel-wave-s37/beurling-fe/sources/` unless marked [here] = `qcond-s38/sources/`)
(Q1) Lev–Olevskii, Invent. 2015, Thm 1 (`arxiv-1312.6884-…txt` 103–105): a (complex) measure on R whose support and spectrum are
     both uniformly discrete (u.d.) has support "contained in a finite union of translates of a certain lattice"; Thm 3 (112–121):
     μ = Σ_j P_j Σ_{λ∈L+θ_j}δ_λ with trigonometric polynomials P_j.
(Q2) Lev–Olevskii, Adv. Math. 2017 [here `arxiv-1512.08735-…txt`]: Thm 1.1 (65–71) the same for positive measures in Rⁿ; Thm 2.2
     (129–133) in R, u.d. support + spectrum with sup_x #(S ∩ [x, x+1]) < ∞ suffices; Thm 1.2 (81–83) discrete closed support and
     spectrum do NOT suffice (a non-periodic complex example).
(Q3) Olevskii–Ulanovskii 2020 (`p2-19b-…txt`): Prop. 1 (64–70) μ ≥ 0 with |μ̂| tempered ⟹ μ(a, b) ≤ C(1 + b − a); Cor. 1 (110–112)
     unit masses ⟹ support relatively u.d.; Thm 1 (40–48) an FQ with unit masses has support = the zero set of an exponential
     polynomial with real simple zeros; Remark 1 (342–349) the same for masses in N (zeros not necessarily simple).
(Q4) Meyer 1970 as stated by Kurasov–Sarnak (`u-20b-…txt` 43–44): "If aλ take values in a finite set and |µ̂| is translation
     bounded, that is sup |µ̂|(x + [0, 1]) < ∞, then µ is a generalized Dirac comb." SECONDARY: the primary (Meyer, LNM 117) is not on
     disk. Generalized Dirac comb (Meyer, PNAS 2016, `meyer-2016-pnas.md` line 95): Σ_j g_jσ_j, σ_j a Dirac comb on a coset
     x_j + Γ_j of a lattice, g_j a trigonometric sum — the lattices Γ_j may differ (be incommensurable).
(Q5) Kurasov–Sarnak 2020, Thm 2 (`u-20b-…txt` 731–739): positive "idempotent" Fourier quasicrystals (unit masses) that are not
     generalized Dirac combs, Λ Delone, S not Delone, and (v) "|µ̂| is not translation bounded"; they answer Meyer's question for
     "a positive crystalline measure which is not a generalized Dirac comb" (795).
(Q6) Gonçalves 2023, Thm 5 (`u-28b-…txt` 662–668): u.d. support, masses ≥ δ > 0, spectral gap (0, b) ⟹ an entire Hermite–Biehler
     E of exponential type describes μ (a trigonometric polynomial if the spectrum is locally finite).
(Q7) Favorov 2024, Thm 4 (`u-34b-…txt` 95–105): non-negative Poisson measure with masses ≥ c > 0 and separation ≥ β on the support
     ⟹ supp μ = ∪_j(T_jZ^d + λ_j).
CONSEQUENCES FOR 𝓜_r (P, from the quotes and BFE Lemma TB: μ ≥ 0 and μ̂ = μ ≥ 0 ⟹ |μ̂| = μ is translation bounded).
 (i)  μ ∈ 𝓜_r with u.d. support is a generalized Dirac comb on finitely many translates of ONE lattice (Q1; spectrum = support).
 (ii) μ ∈ 𝓜_r with locally finite support and finitely many distinct masses is a generalized Dirac comb (Q4 + TB) — conditional
      on the secondary quote (Q4).
 (iii) The Kurasov–Sarnak measures lie in no 𝓜_r (Q5(v) contradicts TB). So the only printed positive crystalline measures that
      are not generalized Dirac combs cannot be self-dual; 𝓜_r receives nothing from them.
 (iv) NOT FOUND IN PRINT (sources above, plus BFE §2 and read-O §3): any μ ∈ 𝓜_r, any r < 1, outside the closed cone spanned by
      positive generalized Dirac combs; nor a classification of 𝓜_r. Open as far as read `[single-check]`.

### 1.4 Three structural facts for 𝓜_r — (P)
Fix a real even k ∈ C_c^∞, supp k ⊂ [−½, ½], k ≢ 0, and put W := (F^{−1}k)²/∫k². Then W ∈ S(R), W ≥ 0, W even, Ŵ = k∗k/∫k² is
supported in [−1, 1] and Ŵ(0) = ∫W = 1. For a measure μ put M_η^T(μ) := T^{−1}∫e^{−2πiηx}W(x/T)dμ(x) (smoothed Bohr mean).
LEMMA B (Bohr means are atoms). If μ is tempered and μ̂ is a locally finite measure, then lim_{T→∞}M_η^T(μ) = μ̂({η}) for all η.
 Proof. f_T(x) := T^{−1}e^{−2πiηx}W(x/T) is the Fourier transform of φ_T(ξ) := Ŵ(T(ξ − η)) (W even). So M_η^T(μ) = ⟨μ, φ̂_T⟩ =
 ⟨μ̂, φ_T⟩ = ∫Ŵ(T(ξ − η))dμ̂(ξ). For T ≥ 1 the integrand is supported in [η − 1, η + 1], bounded by ‖Ŵ‖_∞, and tends to 1_{ξ=η};
 dominated convergence gives μ̂({η}). ∎
LEMMA PD. If moreover μ ≥ 0, then η ↦ μ̂({η}) is positive definite on R (as a discrete group): Σ_{i,j}a_i ā_j μ̂({η_j − η_i}) ≥ 0.
 Proof. 0 ≤ T^{−1}∫|Σ_i a_i e^{2πiη_i x}|²W(x/T)dμ(x) = Σ_{i,j}a_iā_j M^T_{η_j−η_i}(μ) → Σ a_iā_j μ̂({η_j − η_i}) (Lemma B). ∎
For μ ∈ 𝓜_r (μ̂ = μ) write f(η) := μ({η}), so f(0) = ρ and f is positive definite. Three consequences:
COROLLARY 1 (mass bound). μ({η}) ≤ ρ for every η. If μ({η₀}) = ρ, the atomic part of μ is η₀-periodic.
 Proof. 2×2 minor on {0, η}. Periodicity: Krein's inequality |f(x) − f(y)|² ≤ 2f(0)(f(0) − Re f(x − y)) for positive-definite f
 (the 3×3 minor on {0, x, y}) gives f(y + η₀) = f(y) for all y. ∎
COROLLARY 2 (window bound). If E ⊂ (0, ∞) is a finite set of atoms of μ ∈ 𝓜_r with diam E < r, then Σ_{e∈E}μ({e})² ≤ ρ².
 Proof. Differences of distinct elements of E lie in (−r, r)∖{0}, where μ has no atoms. The minor on {0} ∪ E is [[ρ, cᵀ],[c, ρI]]
 with c_e = μ({e}); its Schur complement ρ − |c|²/ρ ≥ 0. ∎
 For a discrete Beurling system (atom masses c(n) ∈ N) this says: at most ⌊ρ_q²⌋ generalized integers lie in any interval of
 length < 1 (unscaled) — a quantitative form of (Q3) Cor. 1.
COROLLARY 3 (small mass at 0 forces a lattice). If every non-zero atom of μ ∈ 𝓜_r has mass ≥ 1, the atoms are locally finite,
 and 2ρ(ρ − 1) < 1 (ρ < (1+√3)/2 ≈ 1.366), then {0} ∪ {atoms} is a lattice hZ.
 Proof. For atoms x, y (either sign, or 0): Krein gives |f(x + y) − f(y)|² ≤ 2ρ(ρ − f(x)) ≤ 2ρ(ρ − 1) < 1 ≤ f(y)², so f(x+y) ≠ 0.
 So E := {0} ∪ atoms is closed under addition and E = −E: a locally finite subgroup of R, i.e. hZ. ∎
REMARK. Everything in §1.4 uses only μ ≥ 0 and μ̂ = μ; the multiplicative (Euler) structure enters from §2 on. `[novelty:
single-check]` for the corollaries as stated for 𝓜_r; Lemma B is the standard "Fourier–Bohr coefficient = atom of μ̂" fact, proved
here to fix hypotheses.
