# NOTE — unit `qcond-s38`: a Beurling system with Riemann's exact FE at conductor q > 1 — construct or refute (Q_cond)

Session 38, 2026-10-01. Writer: Opus 5.5 (unit agent). Status: COMPLETE — CLOSE T (stated classes) + G (§5). Built in order.
Conventions (as in the parent NOTE `novel-wave-s37/beurling-fe/NOTE.md`, cited below as "BFE"): every load-bearing claim is
(P) proved here, (C) computed in `verify/` with its log, or (Q) quoted from a file on disk at the line. `[recalled, unverified]`
marks statements that carry no load. Novelty: `[novelty: single-check]`.

## 0. The question, the digest's ranking, the headline

Setting (BFE §8(b)). dN ≥ 0 on [1, ∞) with polynomial growth, F(s) = ∫x^{−s}dN(x), Λ_F(s) = (q/π)^{s/2}Γ(s/2)F(s) satisfying (A):
Λ_F(s) = Λ_F(1 − s), poles only at 0 and 1 (simple), growth (G′). Beurling: dN = exp*(dΠ), dΠ ≥ 0 on (1, ∞) (multiplicative
exponential), so dN({1}) = 1. Theorem C (BFE): q ≥ 1, q = 1 only for ζ, and at q > 1 the identity (C_q) holds.
**Q_cond.** Is there a Beurling system (discrete, continuous or mixed; weights allowed) with Riemann's exact FE at some q > 1?

### 0.1 The digest's ranking of this unit (Q: `novel-wave-s37/insights-digest.md`, SHA-256 e86f642a…; absent at this unit's
start, on disk by 02:23 IST, read before the close)
§F.2 ranks this unit FIRST of the candidate next units — line 352: "1. **U2 — Q_cond** (`results/qcond-s38/BRIEF.md`, LAUNCHED)";
lines 355–357: "Why first: both outcomes are theorems; the construction branch gives the program's first Q-side control with {Euler
product, Λ ≥ 0, exact FE} (B5, B6); the refutation branch extends B1 to every conductor (then {Euler product, Λ ≥ 0, exact Riemann FE
at any conductor} has one model)". §F.1(a) (335): Theorem T above threshold, "Follow-ups: Q_cond (U2)". §B: B1 (130–135) moves the
question to q > 1; B5 (150–156) "the only drop not yet paid WITH Λ ≥ 0 and a discrete system is conductor q > 1 (Q_cond …)"; B6
(158–164) the rung-1 twin's Q-side location is q > 1. The consolidator's five notes (358–362) are answered: (i) the q = 4 example —
§1.2 (agrees, ρ_q = 3); (ii) read-O o5's q = 5 solution — §1.2(b); (iii) read-O R4(4), ρ₁ ≠ ρ₂ at conductor q — §1.6; (iv) theta
values on a bounded range are not a test — every self-duality check here uses the Fejér pairing with an explicit ξ^{−2} tail bound
(v1) or is exact via Poisson (v2 Part A); (v) rung 1 — §3 (reproduced: t ∈ {−5, …, 6}, RH-false t = ±5).

HEADLINE. Q_cond is REFUTED on the uniformly discrete class at every conductor (Theorem U_q, unconditional), for every system of the
form ζ·(finite Dirichlet polynomial) (Theorem L′), for every purely continuous system (Corollary E2), and — given Meyer's finite-values
theorem, on disk only second-hand — for every discrete Beurling system (Theorem D). What replaces the Fejér gap argument of BFE Theorem
T is a Landau (Pringsheim) obstruction on the finitely generated "q-part" of the frequencies, where the pole of ζ is invisible. Q_cond
stays open only for weighted/mixed systems with clustering integers and infinitely many distinct multiplicities. Close: T (for the
stated classes) + G (that residue). Rung 1 (§3) shows the obstruction is exactly the F_q condition with the pole term removed.

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

### 1.5 Addendum to §1.3 (sources found while writing §2; [here])
(Q8) Baake–Spindeler–Strungaru, J. Fourier Anal. Appl. 29 (2023) [here `arxiv-2104.06812-…txt`]: Thm 4.3 (664–673) an α-periodic
     eigenmeasure of F exists iff α = √n, and then μ = Σ_j c_j δ_{j/√n} ∗ δ_{√nZ} with c an eigenvector of the unitary n-point DFT
     (this is exactly the structure met in §2.4 Step 3: μ_q is √q-periodic, q ∈ N, c a DFT eigenvector); Thm 6.3 (1030–1040) all
     eigenmeasures with u.d. support; Thm 7.5 / Cor. 7.6 (1198–1235) eigenmeasures with locally finite, non-u.d. support and large
     gaps at 0 — complex and NOT translation bounded, hence (TB) never positive; §8 Outlook (lines after 1236): "the
     characterisation of all doubly sparse measures, an important open problem ... is equivalent to the characterisation of all
     doubly sparse eigenmeasures."
(Q4′) A second printed pointer to Meyer's finite-values theorem: Lev–Olevskii 2015 (`arxiv-1312.6884-…txt` 63–68): "A more general
     situation, when the atoms take finitely many different values, was considered in [17, p. 25] [Meyer, LNM 117], [6], [11]."
TASK-1 VERDICT. THEOREM (printed): the u.d. members of 𝓜_r are generalized Dirac combs on one lattice (Q1, Q8 Thm 6.3), the
periodic ones are DFT-eigenvector combs (Q8 Thm 4.3), and — via Meyer (Q4, Q4′) — so are the members with locally finite support
and finitely many masses. PROVED HERE: §1.4 (masses ≤ ρ, window bound, small-ρ lattice). OPEN (in print, Q8 §8): the
classification of self-dual measures with locally finite support; for POSITIVE ones with a gap no non-lattice-type example is
known (the Kurasov–Sarnak and BSS non-u.d. examples are not translation bounded, hence not positive self-dual).

### 1.6 The two-system version at conductor q (read-O R4(4), digest note (iii)) — (P)
Setting: dN₁, dN₂ ≥ 0 on [1, ∞), Λ_i(s) := (q/π)^{s/2}Γ(s/2)∫x^{−s}dN_i, Λ₁(s) = Λ₂(1 − s), poles of Λ₁ only at 0, 1 (simple), (G′).
As in BFE T′ (§12) with the scaling of Theorem C: μ₁ := ρ₂δ₀ + ν₁ + ν₁^∨ and μ₂ := ρ₁δ₀ + ν₂ + ν₂^∨ (ν_i = dN_i scaled by q^{−1/2},
ρ_i = Res_{s=1}Λ_i) satisfy μ̂₁ = μ₂, μ̂₂ = μ₁. Fejér pairing with φ_r both ways (r = q^{−1/2}):
      ρ₁ − rρ₂ = 2r∫S(rt)dν₁(t) ≥ 0,   ρ₂ − rρ₁ = 2r∫S(rt)dν₂(t) ≥ 0,   hence  q^{−1/2} ≤ ρ₁/ρ₂ ≤ q^{1/2}
(strictly, if both dN_i have an atom at 1). ANSWER. (a) For positive measures ρ₁ ≠ ρ₂ IS possible at every q > 1, and the band is
sharp: ν₁ = δ_{aN}, ν₂ = a^{−1}δ_{N/a} (a ∈ [r, 1/r]; Poisson) gives ρ₂ = 1, ρ₁ = 1/a, i.e. F₁ = (√q a)^{−s}ζ(s),
F₂ = a^{−1}(√q/a)^{−s}ζ(s); a = r and a = 1/r attain the two ends. (b) For two BEURLING systems (atoms at 1 on both sides) with 𝒩₁ ∪ 𝒩₂
uniformly discrete it is not possible, because there is no solution at all: μ₁ + μ₂ is self-dual, so §2.4 Steps 1–3 apply to its support and
make both c_i q-periodic (μ₂ = μ̂₁ and μ₁ = μ̂₂ are √q-periodic); S–W gives F_i = ζ·D_i; the Landau argument of Theorem L′, applied
to each F_i separately, makes D₁ and D₂ zero-free on Re s > 0; the FE D₂(1 − s) = q^{s−½}D₁(s) then makes D₁ zero-free everywhere, so
D₁ ≡ 1 (atom at 1), D₂ = √q·q^{−s}, and F₂ = √q q^{−s}ζ(s) has no atom at 1 unless q = 1. Outside the u.d. class: open, as Q_cond.

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

RADICAL (TWO-CLASS, NON-u.d.) CHECK OF THEOREM L′ (C: `verify/v4_radical_family.{py,log}`). q = 2, D = 1 + a·2^{−s/2} + √2·2^{−s}
(frequencies 1 ↔ 2 paired, √2 self-paired; FE checked to 3e−41 at a = 0.7), integers N ∪ √2·N, dN ≥ 0 ⟺ a ≥ 0: certified
infeasible for every a ≥ 0 (u²-coefficient 1 + √2 − a²/2 < 0 beyond 2.2074; the rest covered by witnesses at 2^{4/2}, 2^{3/2},
2^{5/2}; no failed piece). Its Beurling neighbour ζ(s)(1 + b·2^{−s/2}) (the primes with 2 replaced by √2 when b = 1) is Beurling
exactly for 0 ≤ b ≤ 1, while the FE at conductor √2 needs b = 2^{1/4} > 1, where the first negative mass is Π(8) = 1/3 − 2^{3/2}/6
= −0.138 (the parent unit's q = √2 failure; v4 prints the minimum over 2^{k/2}, k ≤ 12, which is −1/2 at 2⁶).

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
    [UPDATE: S–W′ is PROVED in §2.7 by checking the printed proof step by step; Theorem D there closes the discrete case given Q4.]
    THE STEP (S–W′): Saias–Weingartner Thm 2 (at least two primitive characters with non-zero Dirichlet-polynomial weights
    ⟹ zeros in Re s > 1; [here] `arxiv-0807.0783-…txt` 79–84) is proved for ORDINARY Dirichlet polynomials (their proof factors the
    weights over primes p ≤ y, lines 511–530). If it holds for weights with radical frequencies (the same factorization over p^{1/M}
    is available), then ψ is unique and trivial, F = ζ·P̃, and Theorem L′ closes every discrete case at every conductor.
(c) WEIGHTED or MIXED systems whose atom masses take infinitely many values: Meyer's theorem does not apply; only (a) is known.
(d) SHAPE OF ANY SOLUTION (collecting (a)–(c)): an infinite atomic prime set whose generalized integers cluster (pairs arbitrarily
    close), with c ≤ ρ_q, a thin continuous part, and — if discrete and Q4 holds — integers spread over ≥ 2 radical classes and a
    decomposition F = Σ_ψ P̃_ψL_ψ with at least two primitive characters (the trivial one, for the pole, and a non-trivial one; with
    the trivial one alone Theorem L′ applies). No such object is known; none was constructed (the rung-1 calibration, §3, says why
    the function-field twin has no counterpart of this kind).

### 2.7 The discrete case, conditional only on Meyer's theorem — THEOREM D (P given Q4)
LEMMA S–W′ (Saias–Weingartner Thm 2 with radical weights). Let ψ₁, …, ψ_n (n ≥ 2) be distinct primitive characters and P̃₁, …, P̃_n
non-zero finite sums Σ_κ c_κκ^{−s} with κ in the group generated by p₁^{1/M}, …, p_L^{1/M} (finitely many primes, M ∈ N). Then
F = Σ_jP̃_jL_{ψ_j} has zeros in 1 < Re s < 1 + η (≫ T of them up to height T, η = η(F) > 0).
 Proof. S–W §4 ([here] `arxiv-0807.0783-…txt` 508–621) verbatim with the variables z_l := p_l^{−s/M} in place of p_l^{−s}, after
 multiplying F by a monomial Π_l p_l^{a_l s/M} (no zero changes) so that all exponents are ≥ 0. The inputs, checked at the line:
 (i) F_j = h_j(z₁, …, z_L)·Π_{p>p_L}(1 − χ_j(p)p^{−s})^{−1} with h_j a non-zero rational function without poles in the open unit
 polydisk (weights are polynomials in z; the local factors (1 − χ_j(p_l)z_l^M)^{−1} are singular only on |z_l| = 1); (ii) Lemma 2
 (417–505) for arbitrary non-zero rational h_j — its general case only fixes the L phases so that h_j is finite and non-zero for
 1 ≤ σ ≤ 2 and then uses the tail p > p_L, which is untouched; (iii) the Weyl step (591–600) needs the joint equidistribution of
 (p_l^{it/M})_{l≤L} and (p^{it})_{p_L<p≤p_M}: true, since {M^{−1}log p_l} ∪ {log p} is Q-linearly independent; (iv) Rouché (617–621), unchanged. ∎
 `[single-check: an extension of a printed proof, read step by step]`
LEMMA Q (finitely valued quasi-periodic sequences are periodic). If W(n) = Σ_k b_k e^{2πiβ_k n} (finite sum) takes values in a finite
set V for all but finitely many n ∈ Z, then W is periodic and W(Z) ⊂ V.
 Proof. The closure T of {nβ mod 1} in the torus is a compact monothetic group; its identity component T₀ has finite index m and
 T/T₀ is generated by β, so mβ ∈ T₀ and {kmβ : k ≥ k₀} is dense in T₀ (one-sided orbits in compact groups are dense in the orbit
 closure). P(x) := Σ_k b_k e^{2πix_k} is continuous, takes values in V on a dense subset of each coset iβ + T₀, hence (V finite,
 T₀ connected) is constant there; so W(n) = P(nβ) depends only on n mod m. ∎
THEOREM D. Assume Meyer's theorem (Q4). A discrete Beurling system (multiset P of reals > 1, integer multiplicities) whose Λ_F
satisfies (A) at some conductor q > 0 is the rational primes, and q = 1.
 Proof. (1) E3: unit masses off 0; masses ∈ {1, ρ_q}; support locally finite; |μ̂_q| = μ_q translation bounded (TB). By Q4, μ_q = Σ_j
 g_jσ_j, finitely many trigonometrically weighted combs on lattice cosets. (2) §2.6(b): the classes [x] (x ∈ 𝒩) form a finite group
 Γ ⊂ R_{>0}/Q_{>0}. (3) Group the combs by commensurability of their lattices and merge each group over one refined lattice αZ; on a
 coset y + αZ the merged weight W(n) is of Lemma-Q form, and incommensurable groups meet it in finitely many points, so W(n) =
 μ_q({y + αn}) ∈ {0, 1, ρ_q} for all but finitely many n: W is periodic (Lemma Q). A coset with y/α ∉ Q meets each class at most
 once, so it carries ≤ |Γ| + 1 points of supp μ_q, W is eventually 0, hence W ≡ 0. The other cosets lie inside single classes, and
 cosets in one class have commensurable lattices. So μ_q = ρ_qδ₀ + Σ_{γ∈Γ}κ_γ, κ_γ a periodic {0,1}-comb inside class γ, and
 F(s) = Σ_γ β_γ^{−s}G_γ(s) with β_γ in class γ (β_γ^{|Γ|} ∈ Q) and G_γ ∈ H_{M′} (periodic coefficients). (4) S–W Thm 1 on each G_γ:
 F = Σ_ψ P̃_ψL_ψ, P̃_ψ = Σ_γβ_γ^{−s}P_{γ,ψ} (radical weights). (5) F ≠ 0 on Re s > 1 (§2.4 Step 4), so by S–W′ only one ψ has
 P̃_ψ ≢ 0; the pole at s = 1 makes it trivial: F = ζ·P̃. (6) Theorem L′: q = 1, P̃ ≡ 1; BFE Theorem T: the rational primes. ∎
STATUS. Theorem D is (P) GIVEN Q4; Q4 is printed (Meyer 1970, LNM 117) but on disk only as quoted by Kurasov–Sarnak (u-20b 43–44)
and pointed to by Lev–Olevskii 2015 (63–68). Unconditionally, D holds for every discrete system whose integers are u.d. (U_q).

## 3. Task 3 — rung 1 first: the exact dictionary with genus 1 over F₅ (C: `verify/v3_rung1_dictionary.{py,log}`)

Rung 1 (BFE §9). Over F_q a Beurling system is b_d ∈ Z_{≥0}; genus g means Z(u) = Π_d(1 − u^d)^{−b_d} = L(u)/((1 − u)(1 − qu)), L of
degree 2g with L(1/(qu)) = q^{−g}u^{−2g}L(u); "conductor" q^{2g−2}, minimal and rigid at g = 0 (Liouville ↔ BFE Theorem T). At
q = 5, g = 1: L = 1 − tu + 5u² = (1 − αu)(1 − βu), N_n = 5^n + 1 − (α^n + β^n). The Q-side twin of a genus-1 datum is its
transplant F_t := ζ(s)·L(5^{−s}) at conductor 25 — a member of the u.d. class of Theorem U_q (integers ⊂ N).
DICTIONARY (Q-side constraint of §1–§2 ↦ its image on rung 1):
 D1. dN ≥ 0 ↦ A_n ≥ 0 (effective divisors); Π ≥ 0 (Beurling) ↦ b_d ≥ 0 (F1).
 D2. Self-duality μ̂_q = μ_q (additive Fourier on R, the archimedean place) ↦ the FE of Z (Riemann–Roch); frequencies q^d are
     integral by construction, so the Fejér/Bohr facts of §1.4 and Prop. E (§2.1), which live on the additive group R, have NO
     rung-1 image: over F_q, A_n grows like q^n and no "mass ≤ ρ" bound exists.
 D3. Theorem T (gap ⟹ integers ⟹ ζ) ↦ genus-0 rigidity (L entire of degree 0 by Liouville).
 D4. THEOREM L′ (Landau on the finitely generated "q-part" G of the frequencies) ↦ Pringsheim for log Z: over F_q the radius of
     log Z is 1/q, attained at the POLE u = 1/q of the base zeta, which lives in the SAME local variable u as the zeros of L; so
     Landau only says L ≠ 0 on |u| < 1/q, i.e. |α|, |β| ≤ 5 (F3) — harmless. Over Q, on G the pole of ζ at s = 1 is invisible
     (ζ contributes only its local factors at p | q, singular on Re s = 0, i.e. |p^{−s}| = 1), so Landau's abscissa is ≤ 0 and D
     must be zero-free on Re s > 0 — impossible with the FE. EXACT IMAGE: the Q-side q-part positivity for F_t is
         log[L(u)/(1 − u)] ≥ 0 coefficientwise ⟺ α^n + β^n ≤ 1 for all n                              (Q4)
     i.e. the rung-1 condition N_n ≥ 0 (F2) with the pole term 5^n (the factor 1/(1 − 5u)) REMOVED.
 D5. The linear Q-side constraints of the brief's LP: dN ≥ 0 for F_t (Q1: c(n) = 1, 1 − t, 6 − t by v₅(n) = 0, 1, ≥ 2; t ≤ 1);
     E1 ρ_q ≥ 1 (Q2: ρ_q = 5L(1/5) = 6 − t; t ≤ 5); Prop. E at the prime 2 of weight 1 (Q3: (5 − t)/2 ≥ (2/5)S(1/25); t ≤ 4).
TABLE (v3; ✓ = satisfied, ✗ = violated; F1/F2 checked for d, n ≤ 60; Q4 gives the first n with α^n + β^n > 1):
 t  | RH  | F1 b_d ≥ 0 | F2 N_n ≥ 0 | F3 |α| ≤ 5 | Q1 dN ≥ 0 | Q2 ρ ≥ 1 | Q3 Prop.E p=2 | Q4 q-part Π ≥ 0 | min b_d
 −5 |  ✗  |     ✓      |     ✓      |     ✓      |     ✓     |    ✓     |      ✓        |   ✗ (n = 2)     |   0
 −4 |  ✓  |     ✓      |     ✓      |     ✓      |     ✓     |    ✓     |      ✓        |   ✗ (n = 2)     |   5
 −3 |  ✓  |     ✓      |     ✓      |     ✓      |     ✓     |    ✓     |      ✓        |   ✗ (n = 3)     |   9
 −2 |  ✓  |     ✓      |     ✓      |     ✓      |     ✓     |    ✓     |      ✓        |   ✗ (n = 3)     |   8
 −1 |  ✓  |     ✓      |     ✓      |     ✓      |     ✓     |    ✓     |      ✓        |   ✗ (n = 3)     |   7
  0 |  ✓  |     ✓      |     ✓      |     ✓      |     ✓     |    ✓     |      ✓        |   ✗ (n = 4)     |   6
  1 |  ✓  |     ✓      |     ✓      |     ✓      |     ✓     |    ✓     |      ✓        |   ✗ (n = 4)     |   5
  2 |  ✓  |     ✓      |     ✓      |     ✓      |     ✗     |    ✓     |      ✓        |   ✗ (n = 1)     |   4
  3 |  ✓  |     ✓      |     ✓      |     ✓      |     ✗     |    ✓     |      ✓        |   ✗ (n = 1)     |   3
  4 |  ✓  |     ✓      |     ✓      |     ✓      |     ✗     |    ✓     |      ✓        |   ✗ (n = 1)     |   2
  5 |  ✗  |     ✓      |     ✓      |     ✓      |     ✗     |    ✓     |      ✗        |   ✗ (n = 1)     |   1
  6 |  ✗  |     ✓ (Z≡1)|     ✓      |     ✓      |     ✗     |    ✗     |      ✗        |   ✗ (n = 1)     |   0
 Outside {−5..6}: F1 fails for every |t| ≤ 12 (v3); F2 and F3 admit exactly {−6..6}; Q1 admits all t ≤ 1 (down to −12),
 Q2 all t ≤ 5, Q3 all t ≤ 4; Q4 admits NO t in {−12..12}. F_{5,5} = F_{−5} (Π(25) = −7, as in §2.5); the virtual curve is t = 5.
READING (the calibration the brief asked for).
 (a) On rung 1 positivity does NOT force RH: F1 admits t = −5, 5 (RH-false) and 6 (the empty system) — reproduced (BFE §9).
 (b) The LINEAR Q-side constraints (Q1–Q3: the brief's LP ingredients) are weak on the rung where the answer is known: they admit
     RH-false data (t = −5, and every t ≤ −5 down to −12 for Q1–Q3) and data that are not Beurling on either side. An LP built
     from them could not have decided Q_cond; this is why §2 decides the u.d. class through the NON-linear multiplicative
     obstruction Q4 = Theorem L′ instead.
 (c) Q4 is exactly F2 minus the pole term, and it admits nothing: over F₅ the pole of the base zeta shares the local variable u
     with the zeros of L and absorbs them (the "q^d/d closed points of degree d" of BFE §9(iii)); over Q the conductor's local
     variables p^{−s} (p | q) do not carry the pole of ζ, so nothing absorbs the zeros of D. This is the precise sense in which
     the virtual-curve twin has NO counterpart in the u.d. (and, given Q4, the discrete) class over Q.

## 4. Attack log — on this unit's own theorems
(a) U_q, hypothesis by hypothesis. Uniform discreteness enters once (Lev–Olevskii, Step 1). The monoid property of 𝒩 (no cancellation
    in exp*(dΠ), dΠ ≥ 0) enters in Step 2. Self-duality enters in Step 3 (periodicity) and, through the FE, in L′(5). Π ≥ 0 enters twice:
    zero-freeness on Re s > 1 (Step 4, feeding Saias–Weingartner) and positivity on the finitely generated monoid G (L′(3)–(4)). Weights
    are allowed throughout; integrality of multiplicities is never used. (G′) enters only through Prop. R (as in BFE).
(b) Saias–Weingartner Thm 4 is used with σ₁ = 1: it asserts ≍ T zeros in 1 < Re s < 1 + η for large T, which contradicts F = e^{convergent}
    on Re s > 1. Their F_a is Σ_{n≥1}a_n n^{−s} with a q-periodic, exactly our F after Step 3. ✓
(c) L′: D is only assumed finite. Its frequencies need not be integers, rational or even algebraic; the finiteness of S (primes on which
    ζ and D interact) comes from Γ_D ∩ Q being finitely generated. The pole of F at s = 1 is not used in L′ (D is entire); it is used in
    U_q Step 4 and D Step (5) to make ψ trivial. ✓
(d) E2: the only input is the 2×2 minor of the positive-definite function (E′) at {0, 1}; the continuous part of w contributes no atom
    because σ has countably many atoms. At q = 1 it reproduces BFE T2's "no continuous part". ✓
(e) Theorem D: its only non-proved input is Q4 (secondary quote). Lemma S–W′ is an extension of a printed proof, read step by step
    (§2.7); Lemma Q is elementary. If Q4 were misquoted (e.g. if Meyer's theorem needs u.d. support), Theorem D would shrink to U_q.
(f) Where a solution of Q_cond can still hide (the complement of what is proved, sharpened): a Beurling system with (1) clustering
    generalized integers (not u.d.), (2) atom masses c(x) ≤ ρ_q taking infinitely many values — i.e. WEIGHTED primes (Π-masses not of
    the form 1/k at p^k) or a mixed system with a thin continuous part (∫u^{−1}dΠ_c ≤ log ρ_q), (3) ρ_q ≥ 1, (4) not of the form
    ζ·(finite multiplier), (5) all the Fejér identities of §2.1. No such object is known; the rung-1 mechanism (§3(c)) does not
    produce one, since it needs the pole of the base zeta in the conductor's local variables.
(g) Numerics carry no load: v1 (examples), v2 Part A (identity (E), exact), v2 Part B and v4 (interval certificates that re-decide
    special cases of L′/U_q), v3 (rung-1 table). The ξ^{−2} lesson (BFE §7) is respected: no theta value on a bounded range is used as
    evidence; the one Gaussian check in v1 is accompanied by the Fejér pairing with an explicit tail bound.
(h) Prior art (standing order 7). Nearest objects: Hamburger's theorem (ordinary series, conductor 1; BFE sources, Nakamura Thm D);
    the degree-1 classification in the Selberg class, where a degree-1 function with a pole is ζ `[recalled, unverified: Kaczorowski–
    Perelli; not load]` — U_q replaces Ramanujan and a rational-prime Euler product by Π ≥ 0 and u.d.; Saias–Weingartner (periodic
    coefficients, Q-side); Lagarias 1999 (Delone Beurling integers, title/abstract only); Hilberdink–Lapidus (3.5) (open in print).
    No statement of U_q, L′, E2 or D was found in the sources read here or in BFE §2/read-O §3. `[novelty: single-check]`

## 5. CLOSE — T (for a stated class, at every conductor) + G (the named residue)

T (unconditional, proved here; `[novelty: single-check]`):
 • THEOREM U_q (§2.4). A Beurling system (dN = exp*(dΠ), dΠ ≥ 0, weights allowed) whose generalized integers are uniformly discrete
   and whose Λ_F(s) = (q/π)^{s/2}Γ(s/2)F(s) satisfies Riemann's exact FE (poles only at 0, 1, simple; (G′)) has q = 1 and is ζ.
 • THEOREM L′ (§2.3). No Beurling system of the form ζ·D, D a non-constant finite generalized Dirichlet polynomial (any real
   frequencies), has Riemann's exact FE at any conductor. This covers every printed positive-coefficient solution (ζ(s)(1 + q^{½−s}),
   F_{5,5}, the cone 𝒦_r with finitely many atoms, the radical families).
 • COROLLARY E2 (§2.2). At every conductor, the continuous part of the prime measure satisfies ∫u^{−1}dΠ_c ≤ log ρ_q; no purely
   continuous Beurling system has Riemann's exact FE at any conductor. With E1 (ρ_q ≥ 1), E3 (discrete systems are free) and §1.4.
 • WHAT REPLACES THE FEJÉR GAP ARGUMENT. At q > 1 the gap (−q^{−1/2}, q^{−1/2}) no longer pins the integers (𝓜_r is large, §1.2);
   instead, in the u.d. class, Lev–Olevskii + the monoid pigeonhole + Saias–Weingartner reduce F to ζ·D, and the LANDAU OBSTRUCTION
   kills D: positivity of Π on the finitely generated monoid of D's frequencies, where the pole of ζ is invisible, forces D to be
   zero-free on Re s > 0, and the FE reflects that to all of C.
T given one printed theorem on disk only second-hand:
 • THEOREM D (§2.7). Given Meyer's finite-values theorem (Q4: Kurasov–Sarnak's statement, u-20b 43–44; Lev–Olevskii's pointer,
   1312.6884 63–68), every DISCRETE Beurling system with Riemann's exact FE at any conductor is ζ. Inputs: Lemma S–W′ (Saias–Weingartner
   Thm 2 with radical weights, checked against their proof line by line) and Lemma Q.
G (named residue — Q_cond is OPEN exactly here): Beurling systems with clustering (non-u.d.) generalized integers whose atom masses take
infinitely many values (weighted primes, or mixed systems with a thin continuous part); and the primary of Q4 (Meyer, LNM 117, p. 25),
whose reading would make D unconditional. No construction was found; no new Group-I control is claimed.
STOP LINE (brief). Not "a printed theorem settles Q_cond" (none found); not "a verified system" (none); the certificate clause is met in
the strong form available: inside the u.d. class EVERY q is excluded by Theorem U_q, and the reduced finite problem is independently
certified infeasible at q = 2, 3, 4, 5, 6, 9, 25 (B = 4, 9, 32, 25, 108, 81, 625; v2) — the theorem those certificates prove is U_q.
RUNG 1 (§3). On F₅, g = 1 positivity admits RH-false t = ±5; the linear Q-side constraints (the brief's LP) admit them too; the Landau
obstruction is F2 with the pole term removed and admits no t — the exact reason the virtual-curve twin has no counterpart in the u.d.
(and, given Q4, the discrete) class over Q.
WHAT IT MEANS FOR THE PROGRAM. Digest B1 now holds at EVERY conductor inside the u.d. class — {Euler product, Λ ≥ 0, exact Riemann FE
at any conductor, u.d. integers} has exactly one model, ζ — and, given Q4, for all discrete systems. Digest B5's "only unpaid price"
(conductor q > 1 with Λ ≥ 0 and a DISCRETE system) is thereby paid in the negative (given Q4): the Q-side twin of the virtual curve, if
it exists, is a weighted or mixed Beurling system with clustering integers and infinitely many distinct multiplicities.
SUCCESSOR QUESTIONS (ranked). (1) Read Meyer 1970 (LNM 117, p. 25) or Córdoba 1989 at the page, to make Theorem D unconditional
(fetch item). (2) Weighted discrete systems: does Q4-type structure hold for positive self-dual measures with unit-bounded but
infinitely-valued masses (c ≤ ρ_q)? — the one analytic gap left in Q_cond. (3) A dual read of U_q, L′, E2, D (standing order 7).
