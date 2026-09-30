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

## 2. Task 2 — the Euler-side constraints, made rigorous, and what they decide

### 2.1 Sieved measures and their transforms — (P)
ADMISSIBLE SIEVES. Call 0 ≤ Π₁ ≤ Π admissible if exp(−∫u^{−s}dΠ₁(u)) = ∫u^{−s}dw(u) (σ large) for a finite signed measure w on
[1, ∞). Examples: Π₁ finite (w = Σ_j(−Π₁)^{*j}/j!, ‖w‖ ≤ e^{‖Π₁‖}); Π₁ = the full local factors of finitely many atomic primes
p ∈ S, i.e. Π₁ = Σ_{p∈S}Σ_k δ_{p^k}/k (w = Π_{p∈S}(δ₁ − δ_p) = Σ_{m|P_S}μ(m)δ_m, P_S = Π_{p∈S}p; needs Π ≥ Π₁, i.e. p is a prime of
weight ≥ 1). Then dN₂ := dN ∗ w (multiplicative convolution) has transform F·exp(−∫u^{−s}dΠ₁) = exp∫u^{−s}d(Π − Π₁), so
dN₂ = exp*(Π − Π₁) ≥ 0 (uniqueness of Mellin–Stieltjes transforms). Put m₁(w) := ∫u^{−1}dw = exp(−∫u^{−1}dΠ₁) and m₀(w) := ∫dw.
SCALED FORM. Let σ := ν + ν^∨ (so σ̂ = σ + ρδ₀ − ρλ, λ = Lebesgue, ρ = ρ_q) and D_u = push-forward by x ↦ ux. Since
FT(D_uσ) = u^{−1}D_{1/u}σ̂ = u^{−1}D_{1/u}σ + ρu^{−1}δ₀ − ρλ, the positive even measure σ₂ := ∫D_uσ dw(u) (the scaled dN₂) has
      σ̂₂ = ∫u^{−1}D_{1/u}σ dw(u) + ρ m₁(w) δ₀ − ρ m₀(w) λ,                                                       (E)
a locally finite measure (D_{1/u}σ puts mass ≍ u on [−1, 1], weighted by u^{−1}, integrated against the finite |w|).
PROPOSITION E (Fejér form). For admissible Π₁, with S(t) = (sin πt/πt)²:
      2q^{−1/2}∫S(t/q)dN₂(t) = ρ_q(m₁(w) − q^{−1/2}m₀(w)) + 2∫u^{−1}[∫_{[1,u)}(1 − n/u)dN(n)] dw(u)  (≥ 2q^{−1/2}S(1/q) > 0).
 Proof. Pair σ̂₂ with φ_r(x) = (1 − |x|/r)₊ (supp [−r, r], φ̂_r = rS(r·) ≥ 0), mollified exactly as in BFE §4 Step 1:
 ⟨σ₂, φ̂_r⟩ = ⟨σ̂₂, φ_r⟩; ⟨u^{−1}D_{1/u}σ, φ_r⟩ = u^{−1}∫φ_r(x/u)dσ(x) = 2u^{−1}∫_{[1,u)}(1 − n/u)dN(n) in unscaled n = √q·x;
 ⟨δ₀, φ_r⟩ = 1, ⟨λ, φ_r⟩ = r = q^{−1/2}; ⟨σ₂, φ̂_r⟩ = 2r∫S(rx)dν₂(x) = 2q^{−1/2}∫S(t/q)dN₂(t). The lower bound is the atom of
 dN₂ at 1 (dN₂({1}) = 1). ∎
 SPECIAL CASES. w = δ₁: (C_q) of BFE Theorem C. w = δ₁ − δ_p (remove a prime p of weight ≥ 1): m₁ = 1 − 1/p, m₀ = 0 and
      ρ_q(1 − 1/p) − (2/p)Σ_{n<p}c(n)(1 − n/p) = 2q^{−1/2}Σ_t c_{P∖p}(t)S(t/q) ≥ 2q^{−1/2}S(1/q),
 the NOTE-§11(iii) inequality of BFE, now an identity with an explicit positive remainder (generalized integers below p are
 unaffected by removing p). Möbius form (S finite set of primes of weight ≥ 1, w = Σ_{m|P_S}μ(m)δ_m):
      ρ_qΠ_{p∈S}(1 − 1/p) + 2Σ_{m|P_S}μ(m)m^{−1}Σ_{n<m}c(n)(1 − n/m) = 2q^{−1/2}Σ_t c_{P∖S}(t)S(t/q) ≥ 2q^{−1/2}S(1/q).
 These are linear in the small generalized integers (n < max m) and exact; they are consequences of self-duality + Euler.

### 2.2 The Bohr form of the Euler side — (P)
PROPOSITION E′. For admissible Π₁ the atoms of σ̂₂ are, by (E), σ̂₂({0}) = ρ_q m₁(w) and, for η ≠ 0,
σ̂₂({η}) = Σ_{u atom of w} u^{−1}σ({uη})w({u}) (the continuous part of w moves atoms continuously, so it contributes no atom; λ has
none). Since σ₂ ≥ 0, Lemma PD makes η ↦ σ̂₂({η}) positive definite. In unscaled terms (η = x/√q, σ({x/√q}) = c(x) := dN({x})):
      the function x ↦ Σ_{u} u^{−1}c(ux)w({u}) (x ≠ 0), := ρ_q m₁(w) at x = 0, is positive definite on R.            (E′)
COROLLARY E1 (ρ_q ≥ 1). w = δ₁, points {0, 1}: c(1)² ≤ ρ_q², and c(1) = dN({1}) = 1. (Also: c(x) ≤ ρ_q for every x — §1.4 Cor. 1.)
COROLLARY E2 (the continuous part of the prime measure is thin). Write Π = Π_a + Π_c (atomic + continuous). Then
      ∫_{(1,∞)} u^{−1}dΠ_c(u) ≤ log ρ_q.
 Proof. For y > 1, Π₁ := Π_c|_{(1,y]} is finite and continuous, so w = δ₁ + (continuous) (convolution powers of a continuous
 measure are continuous). (E′) on {0, 1}: σ̂₂ at x = 1 equals c(1)·1 = 1; at 0 it is ρ_q exp(−∫_{(1,y]}u^{−1}dΠ_c). The 2×2 minor
 gives 1 ≤ ρ_q exp(−∫_{(1,y]}u^{−1}dΠ_c). Let y → ∞. ∎
 Consequences. (a) Since F has a pole at 1, ∫u^{−1}dΠ = lim_{σ↓1}log F(σ) = ∞, so ∫u^{−1}dΠ_a = ∞: EVERY solution of Q_cond has an
 infinite atomic prime part, and NO purely continuous Beurling system has Riemann's FE at any conductor. (b) At q = 1 (ρ = 1, BFE
 T) it gives Π_c = 0 — the continuous half of BFE Corollary T2 by a second route. `[novelty: single-check]`
COROLLARY E3 (discrete systems are free). If dN is purely atomic with c(x) ∈ N (a discrete Beurling system, P a multiset of reals
 > 1), then P has no repeated element and no multiplicative relation Π_i p_i^{a_i} = Π_j p_j^{b_j} (disjoint supports), and
 c ≡ 1 on the generalized integers 𝒩_P. Proof. A repeated p gives c(p^k) ≥ k + 1; a relation gives an x with two factorizations
 and c(x^k) ≥ k + 1; both contradict c ≤ ρ_q. With neither, factorization is unique. ∎
 So for discrete systems μ_q = ρ_qδ₀ + Σ_{x∈𝒩_P}(δ_{x/√q} + δ_{−x/√q}): UNIT masses off the origin, and §1.4 Cor. 2 bounds the number of
 generalized integers in any interval of length < 1 by ⌊ρ_q²⌋; §1.4 Cor. 3 forces a lattice (hence, by §2.4, q = 1) if ρ_q < 1.366.

### 2.3 The Landau obstruction — Theorem L′ (P)
LEMMA L (Landau 1905; proved here to fix hypotheses). Let G ⊂ [1, ∞) be locally finite, a_g ≥ 0, and let f(s) = Σ_{g∈G}a_g g^{−s}
have abscissa of convergence σ_a ∈ R. Then f has no analytic continuation to any disk around σ_a.
 Proof. If it had one, of radius ε, pick c := σ_a + 1 and ε′ > 0 with (2ε′² + 2ε′)^{1/2} < ε; then f is analytic on B(c, 1 + ε′)
 (its points with Re s ≤ σ_a lie within ε of σ_a). Taylor at c: for 0 < t < 1 + ε′, f(c − t) = Σ_k (t^k/k!)Σ_g a_g(log g)^k g^{−c}, all
 terms ≥ 0; Tonelli gives Σ_g a_g g^{−(c−t)} < ∞ with c − t < σ_a for t > 1 — a contradiction. ∎
THEOREM L′ (no finite multiplier of ζ reaches conductor q ≠ 1). Let F = ζ·D with D(s) = Σ_{b∈B}d_b b^{−s} a finite generalized
Dirichlet polynomial (B ⊂ [1, ∞) finite, any real frequencies). If F is a Beurling zeta (dN = exp*(dΠ), dΠ ≥ 0) and Λ_F satisfies
(A) at some conductor q > 0, then D ≡ 1 and q = 1.
 Proof. (1) Λ_F = q^{s/2}ξ(s)D(s), so D(1 − s) = q^{s−½}D(s); D is entire, real on R, and d₁ = 1 (dN({1}) = 1).
 (2) The group Γ_D ⊂ R_{>0} generated by B is finitely generated; so is Γ_D ∩ Q_{>0}. Let S be the finite set of rational primes
 dividing its generators and G the monoid generated by B ∪ S (locally finite: finitely many generators > 1, ignoring 1). If a
 prime power p^k lies in G then p ∈ S (write p^k = γs, γ ∈ Γ_D, s ∈ ⟨S⟩; then γ ∈ Γ_D ∩ Q, so p ∈ S).
 (3) For σ large, log F = log ζ + log D termwise, so Π = Π_ζ + Π_D, with Π_D (coefficients of Σ_j(−1)^{j+1}(D − 1)^j/j) carried by
 G. On G, Π_ζ is Σ_{p∈S}Σ_k k^{−1}δ_{p^k} by (2). Hence h(s) := D(s)Π_{p∈S}(1 − p^{−s})^{−1} has log h(s) = Σ_{g∈G}Π({g})g^{−s}, a
 series with NONNEGATIVE coefficients (σ large).
 (4) Let σ_a be its abscissa. On Re s > max(σ_a, 0) the series and log h agree (both analytic; h is analytic on Re s > 0), so
 D = e^{series}Π_{p∈S}(1 − p^{−s}) ≠ 0 there and h(σ) ≥ 1 for real σ > max(σ_a, 0). If σ_a > 0: either D(σ_a) ≠ 0, then h(σ_a) ≥ 1
 and log h is analytic near σ_a, continuing the series — impossible by Lemma L; or D(σ_a) = 0, then h(σ) → 0 as σ ↓ σ_a,
 impossible since h ≥ 1. So σ_a ≤ 0 and D has no zeros in Re s > 0.
 (5) By (1) D has no zeros in Re s < 1 either. D is entire of exponential type without zeros, so D = e^{α+βs}; distinct
 exponentials e^{−s log b} are linearly independent, so B = {1}, D ≡ 1, and (1) forces q = 1. ∎
WHAT IT USES AND WHY IT WORKS. Only positivity of Π on the finitely generated monoid G, plus the FE. On G the pole of ζ at s = 1 is
invisible: ζ contributes only its local factors at p ∈ S, singular on Re s = 0; so Landau's abscissa for h is ≤ 0, while the FE puts
zeros of any non-constant D on or around Re s = ½. COVERAGE: ζ(s)(1 + q^{½−s}) for every q, F_{5,5}, every member of 𝒦_r whose
measure m has finitely many atoms, all radical-frequency multipliers such as ζ(s)(1 + a·2^{−s/2} + √2·2^{−s}). It strengthens BFE
§11(i) (finite Euler factors) to all finite Dirichlet-polynomial multipliers. `[novelty: single-check]`

### 2.4 THEOREM U_q — the uniformly discrete class is rigid at every conductor (P, using Q1 and Saias–Weingartner)
THEOREM U_q. Let dN = exp*(dΠ), dΠ ≥ 0, be a Beurling system of polynomial growth whose Λ_F(s) = (q/π)^{s/2}Γ(s/2)F(s)
satisfies (A) at some conductor q > 0. If the support 𝒩 of dN (the generalized integers) is uniformly discrete, then q = 1
and dN = Σ_{n≥1}δ_n (the rational primes). Weights are allowed (Π need not have integer masses).
 Proof. Step 0 (setting). By §1.1, μ_q = ρδ₀ + ν + ν^∨ ∈ 𝓜_r, r = q^{−1/2}; supp μ_q = {0} ∪ ±𝒩/√q is uniformly discrete (𝒩 ⊂ [1, ∞)
 is u.d. and ±𝒩/√q stays at distance ≥ r from 0). A u.d. support also means dN is purely atomic.
 Step 1 (lattice). μ̂_q = μ_q, so the spectrum equals the support: both u.d. Lev–Olevskii Thm 1 (Q1) puts supp μ_q in finitely many
 translates τ_j + hZ; hence 𝒩 ⊂ ∪_j(√qτ_j + √qhZ).
 Step 2 (integers; Hilberdink's pigeonhole as in BFE Prop. U). 𝒩 is an infinite multiplicative monoid (x, y ∈ 𝒩 ⟹ xy ∈ 𝒩, since
 dN = exp*(dΠ) with dΠ ≥ 0 has no cancellation). Some coset contains an infinite A ⊂ 𝒩; for x ∈ 𝒩, xA ⊂ 𝒩, so two a ≠ a′ in A have
 xa, xa′ in one coset: x(a − a′) ∈ √qhZ and a − a′ ∈ √qhZ∖{0}, so x ∈ Q. The cosets meeting 𝒩 then have rational representatives,
 𝒩 ⊂ D^{−1}Z for some D ∈ N, and x = a/b ∈ 𝒩 in lowest terms has x^k ∈ D^{−1}Z for all k, so b = 1: 𝒩 ⊂ N.
 Step 3 (periodicity). μ_q is carried by the lattice q^{−1/2}Z, so μ̂_q is √q-periodic; μ_q = μ̂_q is √q-periodic. The atom at 0
 (mass ρ_q > 0) forces √q ∈ q^{−1/2}Z, i.e. q ∈ N, and c(n + q) = c(n) for n ≥ 1 (c(n) := dN({n})): F(s) = Σ_{n≥1}c(n)n^{−s} has
 q-periodic coefficients.
 Step 4 (factorization; Saias–Weingartner). F ≠ 0 on Re s > 1: F = exp∫x^{−s}dΠ, and ∫x^{−s}dΠ converges for Re s > 1 by Lemma L
 applied to Π ≥ 0 (log F is analytic near every real σ > 1, where F(σ) > 0). Saias–Weingartner Thm 4 ([here]
 `arxiv-0807.0783-…txt` 104–110; with σ₁ = 1 it gives ≍ T zeros in 1 < Re s < 1 + η) says a q-periodic series outside every
 subspace E_{q,ψ} has zeros in Re s > 1; so F ∈ E_{q,ψ} for one primitive ψ, i.e. (their Thm 1 and the definition, lines 56–64)
 F = L_ψ(s)·Σ_{d | q/cond ψ}e_d d^{−s}. F has a pole at s = 1 (ρ_q > 0), so ψ is trivial and F = ζ·D with D = Σ_{d|q}e_d d^{−s}.
 Step 5. Theorem L′ gives D ≡ 1 and q = 1; then BFE Theorem T gives dN = Σδ_n. ∎
COROLLARY U1 (discrete systems with a small origin mass). A discrete Beurling system (integer multiplicities) with Riemann's FE at
any conductor and ρ_q < (1 + √3)/2 is ζ. (§2.2 Cor. E3: unit masses; §1.4 Cor. 3: the support is a lattice, hence u.d.; U_q.)
COROLLARY U2 (the "q-part" dichotomy). A solution of Q_cond, if one exists, has non-uniformly-discrete generalized integers:
pairs of generalized integers arbitrarily close together.
NEAREST PUBLISHED OBJECTS (10(n)). U_q ↔ Lagarias 1999, "Beurling generalized integers with the Delone property" (BFE sources,
title/abstract only: Delone g-integer systems contained in Z), and Hamburger's theorem (Nakamura Thm D, BFE sources). The step
"periodic + zero-free on Re s > 1 ⟹ P·L_ψ" is Saias–Weingartner's; the Landau step is Theorem L′ (§2.3). `[novelty: single-check]`

### 2.5 The finite feasibility problem, decided (C: `verify/v2_euler_identity_and_ud_family.{py,log}`)
WHY NOT THE BRIEF'S LP AS WRITTEN. The Euler-side constraints of §2.1 are linear in dN only once the primes are fixed, and the
Beurling condition Π = log*(dN) ≥ 0 is not linear in dN; worse, the known positive-coefficient solutions (ζ(s)(1 + q^{½−s}), F_{5,5},
all of 𝒦_r) satisfy every LINEAR constraint available on small integers (dN ≥ 0, (C_q), and the §2.1 identities hold for them —
Part A below) and fail only through Π < 0. A truncated LP in dN therefore cannot certify infeasibility. What §2.4 does instead is
reduce the u.d. class EXACTLY to a finite-dimensional family, which is then decided — for all q by Theorem L′, and here, as an
independent check, by rigorous interval certificates at a finite bound B for the brief's q.
PART A (identity (E) is right, signs and factors): on ζ (q = 1), ζ(s)(1 + 2^{½−s}) (q = 2), ζ(s)(1 + 2^{1−2s}) (q = 4),
ζ(s)(1 + 9^{½−s}) (q = 9) and F_{5,5} (q = 25), with w = δ₁, δ₁ − δ₂, δ₁ − δ₃, (δ₁ − δ₂)(δ₁ − δ₃), (δ₁ − δ₂)(δ₁ − δ₃)(δ₁ − δ₅), both sides
of Prop. E agree to ≤ 1e−50; the left side is evaluated EXACTLY through Σ_{n≥1}S(ne) = ((1/e)(1 + 2Σ_{1≤k<e}(1 − k/e)) − 1)/2 (Poisson),
so no truncation or ξ^{−2} tail enters. For ζ every sieved Fejér sum is 0 (sieved integers are integers), as BFE Theorem T requires.
PART B (the reduced u.d. family F = ζ·D, D = Σ_{d|q}e_d d^{−s}, e₁ = 1, e_{q/d} = e_d√q/d; Π ≥ 0 on the q-part ⟺ log h ≥ 0, h =
D·Π_{p|q}(1 − p^{−s})^{−1}; dN ≥ 0 gives the parameter range):
 q = 2, 3, 5 (no parameter): Π(q²) = (1 − q)/2 < 0; B = q² = 4, 9, 25.
 q = 4, 9, 25 (one parameter e, range e ≥ −1): the k = 2 coefficient p + ½ − e²/2 < 0 for e ≥ √(2p+1) + 0.01; the compact rest is
 covered by interval bisection (mpmath.iv, 50 digits, outward rounding), NO failed piece:
   q = 4: e ∈ [−1, −0.188] Π(2⁵) < 0; [−0.188, 0.623] Π(2⁴) < 0; [0.623, 2.246] Π(2³) < 0. B = 32.
   q = 9: e ∈ [−1, 0.828] Π(3⁴) < 0; [0.828, 2.656] Π(3³) < 0. B = 81.
   q = 25: e ∈ [−1, 1.163] Π(5⁴) < 0; [1.163, 3.327] Π(5³) < 0. B = 625. (F_{5,5} is e = 5: Π(25) = −7, as in BFE.)
 q = 6 (two primes, one parameter a = e₂, range a ≥ −2/√6): the uv-coefficient √6(1 − a²/2) < 0 for a > √2; the rest covered with
   witnesses Π(108), Π(36), Π(18), Π(9) < 0 on four pieces; B = 108.
VERDICT for these q: within the u.d. class, INFEASIBLE, by certificate (and for every q by Theorem U_q). Outside the u.d. class the
brief's truncated problem is not finite-dimensional (positions of the generalized integers are free), and §2.6 records how far
the structure theory goes instead.

### 2.6 Beyond the uniformly discrete class — what is proved, what is conditional, what is open
(a) EVERY solution of Q_cond (any weights, any mix): ρ_q ≥ 1 (E1); every atom mass c(x) ≤ ρ_q (§1.4 Cor. 1); continuous prime mass
    thin, ∫u^{−1}dΠ_c ≤ log ρ_q (E2), so the atomic prime part carries ∫u^{−1}dΠ_a = ∞; generalized integers NOT uniformly discrete
    (U_q); not of the form ζ·D with D a finite generalized Dirichlet polynomial (L′); and all Fejér identities of §2.1 hold. (P)
(b) DISCRETE solutions (integer multiplicities). Free, unit masses (E3); at most ⌊ρ_q²⌋ generalized integers in any interval of
    length < 1 (§1.4 Cor. 2); ρ_q ≥ (1 + √3)/2 (U1). (P)
    CONDITIONAL on Meyer's theorem (Q4, secondary quote): μ_q is a generalized Dirac comb (masses in {1, ρ_q}; |μ̂_q| = μ_q
    translation bounded). Then (P, given Q4): running §2.4 Step 2 over the finitely many lattices α_jZ gives x ∈ (α_i/α_j)Q for every
    generalized integer x; so the classes [x] ∈ R_{>0}/Q_{>0} form a finite submonoid, hence a finite group Γ, and x^M ∈ Q for a fixed
    M. If Γ = {1}: 𝒩 ⊂ Q, so 𝒩 ⊂ N, so 𝒩 is u.d. and U_q applies — no solution. If Γ ≠ {1} (generalized integers in several
    radical classes, like N ∪ √2·N): on each class the masses are a finitely-valued trigonometric sum along one lattice, hence
    periodic (orbit-closure argument), so F = Σ_ψ P̃_ψ(s)L_ψ(s) with P̃_ψ FINITE Dirichlet polynomials whose frequencies lie in the
    finite group of radical classes times Q.
    NAMED OPEN STEP (S–W′): Saias–Weingartner Thm 2 (at least two primitive characters with non-zero Dirichlet-polynomial weights
    ⟹ zeros in Re s > 1; [here] `arxiv-0807.0783-…txt` 79–84) is proved for ORDINARY Dirichlet polynomials (their proof factors the
    weights over primes p ≤ y, lines 511–530). If it holds for weights with radical frequencies (the same factorization over p^{1/M}
    is available), then ψ is unique and trivial, F = ζ·P̃, and Theorem L′ closes every discrete case at every conductor.
(c) WEIGHTED or MIXED systems whose atom masses take infinitely many values: Meyer's theorem does not apply; only (a) is known.
(d) SHAPE OF ANY SOLUTION (collecting (a)–(c)): an infinite atomic prime set whose generalized integers cluster (pairs arbitrarily
    close), with c ≤ ρ_q, a thin continuous part, and — if discrete and Q4 holds — integers spread over ≥ 2 radical classes and a
    decomposition F = Σ_ψ P̃_ψL_ψ with at least two primitive characters (the trivial one, for the pole, and a non-trivial one; with
    the trivial one alone Theorem L′ applies). No such object is known; none was constructed (the rung-1 calibration, §3, says why
    the function-field twin has no counterpart of this kind).
