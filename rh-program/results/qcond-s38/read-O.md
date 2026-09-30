# read-O — OPUS READER on unit `qcond-s38` (NOTE.md, Q_cond: Beurling systems with Riemann's exact FE at conductor q > 1)

Reader: Opus 5.5 (second model of the dual-model check; standing orders 5, 7, 11(c)). Date: 2026-10-01.
NOTE read whole at SHA-256 445cfe96dcb7d4ca4a7887cbbc0c2ea3dd033a8cdf4c3932123bfd63115fb54f (51 747 bytes, 446 lines); also read:
BRIEF.md, SHARED.md, verify/v1–v4 (+ logs), sources/, the M1a NOTE (`novel-wave-s37/beurling-fe/NOTE.md`, "BFE") with its read-O
and read-F, and Meyer LNM 117 (`fetched-r9/`, p. 25 as a page image). Independent re-run: `verify-O/` (nothing imported from
`verify/`). Conventions: ✓ = re-derived at the line; GAP = stated with the fix; (P)/(C)/(Q) as in the NOTE.

VERDICT LINE: AGREES-WITH-CORRECTIONS on the close "T for the stated classes at every conductor (U_q, L′, E2), conditional D,
G for the clustering-weighted corner". Every theorem re-derived at the line — U_q, L′ (with Lemma L), E1–E3, Prop. E/E′, §1.4
Cor. 1–3, §1.6, Lemma S–W′ (against S–W §4 at the page), Lemma Q, Theorem D — and none is false as stated; the v2/v3/v4 decisive
certificates re-run by exact Sturm/exact-symbolic routes agree to the witness. Three FIX-FIRST items, all record-level, and one of
them UPGRADES the close: (F1) THEOREM D IS UNCONDITIONAL — Meyer 1970 p. 25, now read at the page, is the unit-mass case, and it
applies VERBATIM to μ_q − (ρ_q − 1)·Lebesgue (after E3 every atom off 0 has mass 1); Kurasov–Sarnak's finite-values form (the NOTE's
Q4) is not needed (it is nevertheless true — proved in §2 through Meyer's Bohr-compactification passage, not through his statement);
(F2) prior art ON DISK was missed: Hilberdink 2012 (Acta Arith. 152; BFE `sources/p3-22c2-…txt`) §4 prints U_q's Step 4 argument
(Prop. 4.2: S–W Corollary + positivity ⟹ N̂ = Q·ζ, Q on the divisors of the period) and the integer-frequency case of L′'s Landau
mechanism (Thm 4.3 multivariable Landau; Thm 4.4 the power-sum condition τ_n ≤ 1 = the NOTE's rung-1 "Q4"); its Thm C already
excludes every SQUAREFREE conductor in the u.d. family — novelty labels of U_q and L′ must be split accordingly; (F3) the (Q4) quote is
replaced by the page (the conclusion there is "up to a finite set, a finite union of arithmetic progressions", for μ TB, 𝔉μ unit comb).
Corrected close: T at every conductor for u.d. integers (U_q), ζ·(finite multiplier) (L′), purely continuous systems (E2) AND every
DISCRETE Beurling system (D: P + Q at the page); G for weighted/mixed systems with clustering integers and infinitely many distinct
masses. Novelty (§4): U_q = new reduction (Steps 1–3 + FE reflection) on a printed core (Hilberdink 2012 §4); L′ = new in its
real-frequency statement, method printed for integer divisor-supported multipliers; E2, D, §1.6 not found in print (dual-checked).

## §1. Re-derivations at the line

(a) §1.1 reduction ✓. μ_q = ρ_qδ₀ + ν + ν^∨ ∈ 𝓜_r (r = q^{−1/2}) is BFE Theorem C's Prop. R at conductor q (read-O/read-F ✓);
    ρ_q = √q·Res F ✓. Converse (μ ∈ 𝓜_r carried off (−r, r) ⟹ dN at conductor r^{−2}) ✓ by (B)⟺(A) of Prop. R.
(b) §1.2 examples ✓. π_a self-dual (Poisson), gap needs a ∈ [r, 1/r] ✓; unscaled F = ζ(s)(b^{−s} + (√q/b)(q/b)^{−s}), b = √q a ✓;
    q = 4 example = π_{1/2}, mass 3 ✓; F_{5,5} ↔ π_{1/5} + (5/2)π_1: masses 6 + 5 = 11 ✓, unscaled ζ(1 + 5·5^{−s} + 5·25^{−s}) ✓.
    Continuous m ⟹ only atom at 0 ✓ (countably many a put an atom at a given x ≠ 0).
(c) §1.4 ✓. Lemma B: f_T = φ̂_T with φ_T(ξ) = Ŵ(T(ξ − η)) (FT of Ŵ is W(−·), W even) ✓, supp φ_T ⊂ [η − 1/T, η + 1/T], dominated
    convergence on the finite |μ̂|-mass of [η − 1, η + 1] ✓. Lemma PD: |Σa_ie^{2πiη_ix}|² expands to Σa_iā_j e^{2πi(η_i−η_j)x},
    whose smoothed mean is M^T_{η_j−η_i} ✓. Cor. 1 (2×2 minor) ✓; equality ⟹ η₀-periodic atoms by Krein
    |f(x) − f(y)|² ≤ 2f(0)(f(0) − Re f(x − y)) ✓. Cor. 2: off-diagonal entries f(e − e′) vanish because |e − e′| < r (gap) ✓, Schur
    complement ρ − |c|²/ρ ≥ 0 ✓; unscaled window length < r√q = 1 ✓. Cor. 3: Krein with x ↦ x + y: |f(x+y) − f(y)|² ≤ 2ρ(ρ − 1) < 1 ≤ f(y)²
    ⟹ f(x + y) ≠ 0; E = {0} ∪ atoms is a locally finite subgroup = hZ ✓; 2ρ² − 2ρ − 1 < 0 ⟺ ρ < (1 + √3)/2 ✓.
(d) §1.6 ✓. From Λ₁(s) = Λ₂(1 − s): μ₁ = ρ₂δ₀ + ν₁ + ν₁^∨ has μ̂₁ = μ₂ (the theta relation ρ₁ + 2ψ₂(1/x) = √x(ρ₂ + 2ψ₁(x)), BFE §12,
    rescaled) ✓. Pairing μ̂₁ = μ₂ with φ_r: ρ₁ = rρ₂ + 2r∫S(rt)dν₁ ✓, symmetric ✓ ⟹ q^{−1/2} ≤ ρ₁/ρ₂ ≤ q^{1/2} ✓; strict when dN₁({1}) > 0
    (atom of ν₁ at r, S(1/q) > 0) ✓. SHARPNESS ✓: ν₁ = δ_{aN}, ρ₂ = 1 makes μ₁ = δ_{aZ}, μ̂₁ = a^{−1}δ_{Z/a} = μ₂ (ρ₁ = 1/a, ν₂ = a^{−1}δ_{N/a});
    carried off (−r, r) iff a ∈ [r, 1/r] ✓; unscaled F₁ = (√q a)^{−s}ζ, F₂ = a^{−1}(√q/a)^{−s}ζ ✓; a = r gives the pair (ζ, √q q^{−s}ζ),
    checked: q^{s/2}ξ(s) = (q/π)^{(1−s)/2}Γ((1−s)/2)√q q^{s−1}ζ(1−s) ✓. (b) (two Beurling systems, u.d. union) ✓: each 𝒩_i is a
    monoid, so the pigeonhole runs per system; μ₁ ⊂ lattice ⟹ μ̂₁ = μ₂ √q-periodic, ρ₁ + ρ₂ > 0 at 0 ⟹ q ∈ N ✓; ρ_i > 0 from the
    strict band ✓; L′(2)–(4) uses only Π_i ≥ 0 (not the FE) ⟹ D₁, D₂ zero-free on Re s > 0 ✓; D₂(1 − s) = q^{s−½}D₁(s) ✓ reflects
    zeros of D₁ in Re s ≤ 0 to zeros of D₂ in Re s ≥ 1 ✓ ⟹ D₁ ≡ 1, D₂ = √q q^{−s}, no atom at 1 ✓.
(e) §2.1 Prop. E ✓. σ̂ = σ + ρδ₀ − ρλ from μ̂_q = μ_q ✓; FT(D_uσ) = u^{−1}D_{1/u}σ̂ ✓ and D_{1/u}λ = uλ, D_{1/u}δ₀ = δ₀ ⟹
    u^{−1}D_{1/u}σ̂ = u^{−1}D_{1/u}σ + ρu^{−1}δ₀ − ρλ ✓; σ₂ = ∫D_uσ dw is the scaled dN ∗ w ✓; (E) ✓. Pairing with φ_r: ⟨u^{−1}D_{1/u}σ, φ_r⟩
    = 2u^{−1}∫(1 − t/u)₊dN(t) (r√q = 1) ✓, ⟨λ, φ_r⟩ = r ✓. Mollification: σ̂₂ locally finite (|w| finite, D_{1/u}σ([−X, X]) ≤ CuX) ✓
    and N₂(X) ≤ ∫N(X/u)d|w| = O(X) ✓. Lower bound from dN₂({1}) = 1 ✓. w = δ₁ gives (C_q) ✓; w = δ₁ − δ_p reproduces BFE §11(iii) as
    an identity ✓. (E) is a consequence of self-duality ALONE — the reader's o1 checks it for signed, non-admissible w too.
    GAP (minor, m1): "p is a prime of weight ≥ 1" must mean Π({p^k}) ≥ 1/k for ALL k (Π ≥ Π₁); for weighted systems Π({p}) ≥ 1 alone
    does not give admissibility.
(f) §2.2 ✓. E′: D_{1/u}σ({η}) = σ({uη}) ✓; the continuous part of w gives no atom (σ has countably many atoms) ✓; σ₂ ≥ 0 tempered with
    σ̂₂ locally finite ⟹ Lemma PD ✓. E1 ✓. E2 ✓: Π₁ = Π_c|_{(1,y]} finite (Π((1, y]) ≤ y^σ∫x^{−σ}dΠ) and continuous; convolution powers of
    a continuous measure are continuous ✓; m₁(w) = exp(−∫u^{−1}dΠ₁) (Π₁ finite, so the Mellin identity holds at s = 1) ✓; f(1) = c(1) = 1 ✓.
    Consequence (a) ✓ WITHOUT Landau: if ∫u^{−1}dΠ < ∞ then F = exp∫u^{−s}dΠ on Re s > 1 (both analytic there) stays bounded as σ ↓ 1.
    (b) needs ρ = 1, which comes from BFE T — "a second route" only for the continuous-part half (m2). E3 ✓ (k + 1 factorizations of
    p^k, resp. of x^k; unique factorization after cancelling common factors).
(g) §2.3 ✓. Lemma L: for |s − c| < 1 + ε′ and Re s ≤ σ_a, |s − σ_a|² < 2ε′ + ε′² ✓; Taylor at c with nonnegative terms, Tonelli ✓ (uses
    G ⊂ [1, ∞), log g ≥ 0 ✓). THEOREM L′: (1) q^{s/2}ξ(s)D(s) = q^{(1−s)/2}ξ(s)D(1−s) ⟹ D(1−s) = q^{s−½}D(s) ✓; d real (F/ζ = F·Σμ(n)n^{−s}) ✓;
    min B ≥ 1 is automatic (F has an atom of mass d_{min B} at min B) ✓. (2) f.g. Γ_D, Γ_D ∩ Q ✓; p^k = γs ⟹ p ∈ S ✓. (3) Π|_G =
    Σ_{p∈S}Σ_k k^{−1}δ_{p^k} + Π_D ✓. (4) ✓, with one wording GAP (m3): "the series and log h agree" presupposes a logarithm of h on
    Re s > max(σ_a, 0); the rigorous line is e^{series} = h there (identity theorem), whence D ≠ 0 and h(σ) ≥ 1; the two cases at σ_a
    then run as written (h(σ_a) ≥ 1 by continuity ⟹ principal log h analytic at σ_a, equal to the series to its right ⟹ Landau). (5) ✓.
(h) §2.4 THEOREM U_q ✓, every step. Step 0: u.d. of ±𝒩/√q ∪ {0} ✓, purely atomic ✓. Step 1: LO15 Thm 1 hypotheses (2), (3) at
    `arxiv-1312.6884` (BFE sources) lines 83–106 — a (complex) measure on a u.d. set, temperate, FT a measure on a u.d. set ✓ (spectrum =
    support). Step 2: supp(exp*Π) is a monoid (no cancellation, Π ≥ 0) ✓; a − a′ ∈ √qhZ∖{0} with a, a′ ∈ Q ⟹ √qh ∈ Q ⟹ 𝒩 ⊂ D^{−1}Z ✓;
    b^k | D ∀k ⟹ b = 1 ✓. Step 3: measure on q^{−1/2}Z ⟹ transform √q-periodic ✓; √q ∈ supp ⊂ q^{−1/2}Z ⟹ q ∈ N ✓; c(n + q) = c(n) ✓
    (bonus: c(q) = ρ_q). Step 4: S–W Thm 4 (`sources/arxiv-0807.0783` lines 104–110) with σ₁ = 1 is admissible (1/2 < σ₁ < σ₂ ≤ 1 + η) ✓;
    σ_Π ≤ 1 by Landau for the atomic Π ≥ 0 ✓ ⟹ F = e^{convergent} ≠ 0 on Re s > 1 ✓; E_{q,ψ} (lines 55–57) ✓; pole ⟹ ψ trivial ✓. Step 5 ✓.
    U1 ✓ (E3 unit masses ≥ 1 + Cor. 3). U2 ✓.
(i) §2.5 ✓. The family: e_{q/d} = e_d√q/d from matching d^s-coefficients ✓ (reader re-solved it with sympy.solve, o2); c(n) ≥ 0 ranges
    ✓ (q = 4, 9, 25: e ≥ −1; q = 6: e₂ ≥ −2/√6, i.e. e₃ ≥ −1); Π on the q-part = coefficients of log h ✓; k = 2 coefficient p + ½ − e²/2 ✓;
    q = 6 uv-coefficient c − ab = √6(1 − a²/2) ✓ (reader's multinomial formula). The WHY-NOT-THE-LP paragraph is right: every linear
    constraint available holds on the non-Beurling self-dual examples (o1 re-proves (E) exactly on them). Radical check ✓: the FE of
    1 + a2^{−s/2} + √2·2^{−s} holds identically in a; dN ≥ 0 ⟺ a ≥ 0; the neighbour ζ(1 + b2^{−s/2}) is Beurling ⟺ 0 ≤ b ≤ 1 (even k = 2j:
    (2 − b^{2j})/(2j)); FE at conductor √2 forces b = 2^{1/4}; Π(8) = 1/3 − √2/3 = −0.138 ✓ (o2).
(j) §2.7 at the page. LEMMA S–W′ ✓. I read S–W §3–§4 (`arxiv-0807.0783` lines 262–621). The σ₁ ≥ 1 case of Thm 2 uses: (11) h_j
    rational without poles in the open polydisk; Lemma 2 (417–505), whose general case only FIXES the L small-prime phases so that
    h_j(p_1^{−σ−it₁}, …) is finite and non-zero for 1 ≤ σ ≤ 2 and then applies the h ≡ 1 case to the tail p > p_L (Lemma 1, PNT in APs,
    Brouwer) — nothing there uses that p_l is prime beyond |z_l| = p_l^{−σ} < 1, so z_l = p_l^{−s/M} = (p_l^{1/M})^{−s} is admissible
    verbatim; the choice of phases exists since N(z(σ, t)) is, for fixed σ, a non-zero trigonometric polynomial in t with frequency
    vectors (k_l log p_l/M)_l (distinct for distinct k) — the same genericity S–W assume in the integer case; the Weyl step (591–600)
    needs {M^{−1}log p_l}_{l≤L} ∪ {log p}_{p_L<p≤p_M} Q-independent ✓; Rouché (617–621) unchanged ✓. The common monomial Π_l p_l^{a_l s/M}
    must multiply F (all F_j at once) ✓ — as the NOTE says. LEMMA Q ✓ (T₀ open of finite index m, mβ ∈ T₀, the forward orbit of mβ is
    dense in T₀, P constant on each coset by continuity + finiteness of V + connectedness; T₀ trivial ⟹ T finite, W periodic outright).
    THEOREM D in the NOTE's form (given Q4) ✓, with one loose sentence (m4): "μ_q = ρ_qδ₀ + Σ_γ κ_γ, κ_γ a periodic {0,1}-comb" — cosets
    through 0 carry part of the mass ρ_q, so the κ_γ are {0,1}-valued only off 0; what the proof uses (F = Σ_γ β_γ^{−s}G_γ with G_γ
    q-periodic in n ≥ 1) is correct. Steps (4)–(6) ✓: P̃_ψ ≡ 0 iff every P_{γ,ψ} ≡ 0 (different classes have disjoint frequencies) ✓.
(k) §3 rung 1 ✓ (o3 recomputes it from the definitions; every set and every "first bad n" agrees). D4 ✓: log[L/(1 − u)] = Σ(1 − s_n)u^n/n,
    F2 adds 5^n/n ✓. D5 ✓: c(n) = 1, 1 − t, 6 − t; ρ = 5L(1/5) = 6 − t; (5 − t)/2 ≥ (2/5)S(1/25), S(1/25) ∈ [0.994743, 0.994748] ⟹ t ≤ 4.
    Reading (c) ✓, and note: the NOTE's "Q4 ⟺ α^n + β^n ≤ 1 ∀n" is verbatim Hilberdink 2012's condition (†) τ_n ≤ 1 (`p3-22c2` 1000–1012),
    whose Theorem 4.4 (1028–1066) proves, for degree k > 1, |μ_r| < 1 — here μ_r = α, β with αβ = 5, impossible: the rung-1 column "Q4
    admits NO t" is a special case of a printed theorem (see §4 row 1).

## §2. Meyer at the page — and the ruling on Theorem D

THE PAGE (`fetched-r9/r9-05-meyer-1970-LNM117-pisot-salem.pdf`, scan p. 25 = printed p. 25, read as a 150-dpi page image; the OCR
garbles the formulas). Y. Meyer, Nombres de Pisot, nombres de Salem et analyse harmonique, LNM 117 (1970), §4.2, p. 25, verbatim:
  « Supposons, en effet, qu'il existe une mesure, à valeurs complexes, μ telle que
    a) sup_{−∞<x<+∞} ∫_x^{x+1} d|μ|(t) < +∞
    b) 𝔉μ = Σ_{λ∈Λ} δ(x−λ).
  La somme Σ_{λ∈Λ} δ(x−λ) ne peut être une distribution que si elle est une mesure ; alors Λ est un ensemble fermé dont chaque élément
  est isolé. […] Il existe donc une mesure ν portée par le compactifié de Bohr de R dont la transformée de Fourier vaut 1 sur Λ et 0
  ailleurs (ν est la limite vague des μ_n). D'après une conséquence du théorème de Paul Cohen due à P.H. Rosenthal, ([7] th. 1.6 p.22)
  Λ est à un ensemble fini près, la réunion de k parties de R de la forme α_jZ + β_j (1 ≦ j ≦ k). »
  p. 26: « On retrouve donc la formule de Poisson habituelle. »  p. 24: f̂(y) = ∫exp(−2πixy)f(x)dx (the NOTE's convention).
  p. 63: « [7] ROSENTHAL (P.H.).- Thèse, Memoirs of the A.M.S. » (= H. P. Rosenthal, Mem. AMS 63, 1966 — identified by Córdoba
  1989's reference list, `verify-O/sources/cordoba-1989-springer.md`). The elided middle is the construction dμ_n = n^{−1}Ψ(x/n)dμ,
  ‖μ_n‖ bounded by a), μ̂_n(t) = Σ_λ φ(nt − nλ) → 1_Λ(t); re-derived ✓ (bounded measures on R embed isometrically in M(bR); weak-*
  limit ν; ν̂(t) = lim μ̂_n(t) for every t since the limit exists pointwise).
So the page proves the UNIT-MASS case (atoms of 𝔉μ all equal to 1; μ only translation bounded and complex; no u.d. assumption), and
its conclusion is about the SET Λ, up to a finite set. Nothing on pp. 24–27 (or elsewhere in the OCR: no other "Cohen", "Bohr" or
"nombre fini de valeurs" passage) treats finitely many values.

WHAT THEOREM D NEEDS. Only this: a positive μ = μ̂ with locally finite support, mass ρ at 0 and mass 1 at every other atom (E3), is a
finite combination of arithmetic-progression combs. The NOTE's (Q4) (finitely many values in {1, ρ_q}) is more than is needed.

REDUCTION TO THE PRINTED CASE (P, reader). Put μ′ := μ_q − (ρ_q − 1)·λ (λ = Lebesgue). (a) holds: |μ′| ≤ μ_q + |ρ_q − 1|λ and μ_q is
translation bounded (BFE Lemma TB: μ_q ≥ 0, μ̂_q = μ_q ≥ 0). (b) holds: 𝔉μ′ = μ_q − (ρ_q − 1)δ₀ = Σ_{λ∈Λ}δ_λ with Λ = {0} ∪ ±𝒩/√q, unit
masses by E3; Λ is closed and discrete (§1.4 Cor. 2). Meyer p. 25 ⟹ Λ Δ ∪_{j≤k}(α_jZ + β_j) is FINITE.
REMOVING THE FINITE SET (P). Inclusion–exclusion (an intersection of two progressions is ∅, a point, or a progression) gives
μ_q = (ρ_q − 1)δ₀ + Σ_{λ∈Λ}δ_λ = C + E, C = Σ_i ε_iδ_{A_i} (A_i progressions, ε_i ∈ Z), E a finite atomic measure. Ĉ is pure point
(FT δ_{αZ+β} = α^{−1}Σ_m e^{−2πiβm/α}δ_{m/α}); Ê = (Σ_f e_f e^{−2πifξ})dξ is absolutely continuous; μ̂_q = μ_q is pure point ⟹ Ê = 0 ⟹
E = 0. Hence μ_q = Σ_i ε_iδ_{A_i} EXACTLY — and, as a by-product, ρ_q = Σ_{A_i∋0} ε_i ∈ Z (a discrete solution would need ρ_q ∈ {2, 3, …}
by U1).
THE REST OF D ON THIS ROUTE (P). Pigeonhole over the finitely many A_i (x(a − a′) ∈ √qα_iZ, a − a′ ∈ √qα_jZ∖0) ⟹ classes [x] ∈ R_{>0}/Q_{>0}
form a finite group Γ ✓; an A_i with two points in one class lies wholly in that class (y = x₁ + (x₁ − x₂)m/n) ✓; so on class γ the
unscaled measure is (β_γ/D_γ)·(a Z-combination of rational progressions): G_γ has EXACTLY q′-periodic coefficients for n ≥ 1; then
S–W Thm 1, S–W′, the pole, L′ and BFE T exactly as in the NOTE's Steps (4)–(6). Lemma Q is not needed (the weights are constants ε_i).
THE FINITE-VALUES FORM (the orchestrator's sketch) — PROVED, with one correction of the object. Let μ be complex, translation bounded,
𝔉μ = Σ_{λ∈Λ}a_λδ_λ with Λ closed discrete and a_λ ∈ V finite. (i) Meyer's Bohr passage SURVIVES VERBATIM: the same μ_n give
μ̂_n(t) = Σ_λ a_λφ(n(t − λ)) → a_t (0 off Λ), ‖μ_n‖ bounded by a) alone, so a = ν̂ for some ν ∈ M(bR), i.e. a ∈ B(R_d). (ii) For v ∈ V∖{0} let
P_v be the Lagrange polynomial with P_v(v) = 1, P_v(w) = 0 on (V ∪ {0})∖{v}; P_v(0) = 0, so P_v(a) = Σ_k c_k ν̂^k = (Σ_k c_k ν^{*k})^ is an
idempotent of B(R_d). CORRECTION to the sketch: the convolution powers are those of ν in M(bR) — convolution powers of μ on R do not
exist in general (μ = Lebesgue) — which is exactly why the passage to bR is needed. (iii) Cohen's idempotent theorem (compact group bR,
dual R_d) puts Λ_v := {a = v} in the coset ring of R_d; Λ_v ⊂ Λ is closed discrete, so Rosenthal's consequence (the step Meyer
cites) makes each Λ_v a finite union of progressions up to a finite set. (iv) If moreover μ is crystalline (μ̂ pure point), the finite
exceptions vanish by the pure-point/absolutely-continuous argument above, and μ is a constant-weight generalized Dirac comb. So
(Q4) is TRUE in Kurasov–Sarnak's crystalline context — but it is a consequence of Meyer's ARGUMENT, not of his printed STATEMENT (the
statement is about unit masses and cannot be applied level set by level set: a TB measure on R with transform 1_{Λ_v} exists only a posteriori). Without the crystalline
hypothesis K–S's wording fails: μ = δ₀ has a_λ ∈ {1} and μ̂ = Lebesgue translation bounded, yet is not a generalized Dirac comb
(Meyer's "à un ensemble fini près" is essential).

QUOTATIONS OF MEYER AGAINST THE PAGE.
 • Kurasov–Sarnak 2020 (`u-20b` 43–44): "If aλ take values in a finite set and |µ̂| is translation bounded … then µ is a generalized
   Dirac comb", attributed to [24] = LNM 117 without a page. BROADER THAN THE PAGE in two ways (finite values; exact comb instead of
   "up to a finite set"), both harmless inside their definition (1) (crystalline measures) by (i)–(iv) above. Their own use (Thm 2(v),
   `u-20b` 777–779: "(aλ = 1 in our case)") is exactly the page's case ✓.
 • Lev–Olevskii 2015 (`arxiv-1312.6884` 63–68): "A more general situation, when the atoms take finitely many different values, was
   considered in [17, p. 25], [6], [11]. These results are based on the Helson-Cohen characterization of idempotent measures". The
   method sentence matches the page ✓; the finite-values attribution to p. 25 does NOT — p. 25 treats unit masses (it is "more general"
   than Córdoba's statement in another direction: μ complex and merely TB, no positivity of μ̂). The finite-values case belongs, as far
   as can be checked, to Córdoba 1989 [6] (abstract only on disk) and to the argument above.
 • The NOTE's (Q4) inherits K–S's over-attribution; (Q4′) inherits LO's. Neither affects D once D is routed through the page.

RULING (task 2). Theorem D is UNCONDITIONAL in the program's sense — (P) on top of a printed theorem read at the page (Meyer 1970,
p. 25). It does not shrink to U_q, and it is not conditional on the finite-values statement. The only input not on disk is inside
Meyer's printed proof: Rosenthal, Mem. AMS 63 (1966), Th. 1.6 p. 22 (a standard consequence of Cohen's idempotent theorem; cited in
the same role by Córdoba 1989). Label: `[D: dual-checked; Meyer p. 25 read at the page; Rosenthal Th. 1.6 cited, body not on disk]`.

## §3. Independent re-run (`verify-O/`; own routes, the writer's scripts read for inputs only, never imported or executed)

o1 `o1_identity_E_exact.{py,log}` — the MEASURE identity (E), EXACTLY (sympy over Q(√2, √3, √6); no floating point). Route: triangle
  of ARBITRARY width L = ℓ/√q, ℓ ∈ {1, 1/2, 2, 3/2, 3, 7/3} (Prop. E is ℓ = 1 only; the six widths test (E) as a measure identity);
  left side by the Fourier-series closed form Σ_{n≥1}S(ne) = {e}(1 − {e})/(2e²) (from Σcos(2πnθ)/n² = π²B₂(θ); v2 used Poisson; the two
  agree, e.g. T(3/2) = 1/18). 8 self-dual examples (the writer's 5 plus three new: ζ(1 + 3^{½−s}) at q = 3; ζ(1 + 2^{−s} + (√6/2)3^{−s} +
  √6·6^{−s}) at q = 6; the RADICAL ζ(1 + 2^{−s/2} + √2·2^{−s}) at q = 2) × 5 sieves (incl. the signed, non-admissible w = δ₁ − 2δ₃ + δ₇/2 +
  3δ_{5/2}): 240 exact checks, 0 nonzero differences. The ℓ = 1 values are the writer's Part A numbers as exact surds: √2/2, 4√2/9,
  32√2/75 (q = 2); 3/2, 1, 4/3, 64/75 (q = 4); 8/3, 3/2, 2, 39/50 (q = 9); 44/5, 5, 20/3, 29/9 (F_{5,5}) ✓. (A first run showed
  1e−16 residues from a Python int/int division in ρ_q; fixed before the logged run.)
o2 `o2_ud_family_exact.{py,log}` — the reduced u.d. family and the radical family, EXACT STURM certificates over Q. Route: the family
  re-solved from the FE by sympy.solve (it returns e₄ = 2, e₉ = 3, e₂₅ = 5, e_p = √p; at q = 6 it leaves e₃ free, e₂ = √6e₃/3, e₆ = √6);
  Π on the q-part by NEWTON power sums (q = p^k) and by a closed multinomial formula (q = 6); a witness P certifies [x, y] when P(x) < 0
  exactly and the norm A² − rB² of P = A + √r·B has no root in [x, y] (sympy count_roots = Sturm, exact); the tail by the k = 2
  coefficient. Results: q = 2, 3, 5: Π(p²) = (1 − p)/2 exactly. q = 4: [−1, 56/25] in 3 pieces, witnesses Π(2⁵), Π(2⁴), Π(2³) (break
  points −0.19, 0.62 vs the writer's −0.188, 0.623), tail −(e² − 5)/2 < 0 on [56/25, ∞). q = 9: Π(3⁴), Π(3³), tail from 53/20. q = 25:
  Π(5⁴), Π(5³), tail from 83/25; F_{5,5} (e = 5): Π(5^n) = 6, −7, 17, −87/2, 626/5, −2249/6 (writer: 6, −7, 17, −43.5, 125.2, −374.83 ✓).
  q = 6 (parameter e₃ ∈ [−1, ∞)): 4 pieces, witnesses Π(108), Π(36), Π(18), Π(9) — the writer's four, same order; tail −√6(e₃² − 3)/3.
  Radical (a ∈ [0, ∞)): 3 merged pieces, witnesses Π(2^{4/2}), Π(2^{3/2}), Π(2^{5/2}) — the writer's three; tail 1 + √2 − a²/2 from 221/100.
  No failed piece anywhere. The FE of every family re-checked (residuals ≤ 3e−176 at 60+ digits).
o3 `o3_rung1_from_definitions.{py,log}` — rung 1 from the DEFINITIONS, exact integers. b_d by successive Euler factorization of
  Z(u) = L(u)/((1 − u)(1 − 5u)) (no Möbius; v3 used Möbius), N_n both as Σ_{d|n}d·b_d and as 5^n + 1 − s_n (they agree for all t, n ≤ 60);
  F3 by the exact criterion (complex roots, or f(±5) ≥ 0); Q1 by Dirichlet convolution to n = 3000; Q2 exact rational; Q3 with a rational
  enclosure S(1/25) ∈ [0.99474311, 0.99474729]. Every set of the NOTE's §3 table and every first-failure n of Q4 reproduced; virtual
  curve N₁..N₆ = 1, 11, 76, 451, 2501, 13376 and b₁..b₆ = 1, 5, 25, 110, 500, 2215 ✓; t = −5 ↔ F_{5,5}, Π(25) = −7 ✓.
VERDICT OF THE RE-RUN: every decisive certificate of v2 (Part A identity; Part B, q = 2, 3, 4, 5, 6, 9, 25), v3 and v4 is reproduced by
an independent exact route; (E) additionally holds as a measure identity at six widths and for signed sieves.

## §4. Prior-art gate, at the page

Column 5: CONTAINS / PARTIAL (a printed theorem gives part of a proof) / METHOD / INPUT (used as a black box) / INCOMPARABLE.
Paths: BFE = `novel-wave-s37/beurling-fe/sources/`, here = `qcond-s38/sources/`, new captures in `verify-O/sources/`.

| # | source | where read | what it proves | relation to U_q, L′, E2, D |
|---|---|---|---|---|
| 1 | Hilberdink 2012, Acta Arith. 152, 217–241 | BFE `p3-22c2-…txt` (accepted version): Thm A 102–115, Thm B 120–124, outer systems Defs 1.2–1.3 313–330, class T 262–268, §3 488–655, Prop. 4.2 741–806 (S–W at 732–739), Thm 4.3 812–921 (Landau 862), (∗), (†) 966–1012, Thm 4.4 1028–1066, Lemma 4.5 + proof of Thm A 1069–1120, Thm C 1122–1146 | OUTER systems (Π ≥ 0, weights allowed) with N(x) − cx P-periodic, N ∈ T: jumps at integers, P ∈ N; N̂_J = Qζ, Q = Σ_{d∣P}q(d)d^{−s} (S–W Corollary + positivity ⟹ principal character); Q = Π_{p∣P}Q_p (multivariable Landau); each Q_p zero-free on Re s > 0 (τ_n ≤ 1 ⟹ abs(μ_r) ≤ 1, < 1 if deg Q_p > 1); squarefree P: outer ⟺ Q = Π(1 + q(p)p^{−s}), q(p) ∈ [−1, 1] | PARTIAL, and NOT cited by the NOTE. No FE anywhere in it. After U_q's Steps 1–3 (N − c̄x is q-periodic, N ∈ T), Prop. 4.2 + Thms 4.3–4.4 + the FE reflection finish U_q; for SQUAREFREE q, Thm C + e_q = √q > 1 finishes it (v2's q = 2, 3, 5, 6 are decided by a printed theorem). U_q Step 4 = Prop. 4.2's S–W step (principal character by positivity there, by the pole in U_q); L′(2)–(4) = a shorter real-frequency version of Thm 4.3 + (∗)/(†) + Thm 4.4; the rung-1 "Q4" is (†) |
| 2 | Saias–Weingartner 2009, Acta Arith. 140 | here `arxiv-0807.0783-…txt`: Thm 1 62–75, Thm 2 79–92, Thm 4 + Remark 103–116, §3–§4 262–621 | H_q = ⊕E_{q,ψ}; ≥ 2 characters with Dirichlet-polynomial weights ⟹ ≫ T zeros with Re s ∈ (σ₁, 1 + η); outside every E_{q,ψ} ⟹ ≍ T zeros | INPUT (U_q Step 4, D Step 4); S–W′ = their §4 with z_l = p_l^{−s/M}, checked here §1(j). No FE, no positivity: INCOMPARABLE as statements |
| 3 | Lev–Olevskii, Invent. 200 (2015); Adv. Math. (2017) | BFE `arxiv-1312.6884` 60–68, 83–125; here `arxiv-1512.08735` 62–72, 127–134 | u.d. support + u.d. spectrum ⟹ finitely many translates of one lattice (complex, R); positive in Rⁿ; Thm 2.2 | INPUT (U_q Step 1). INCOMPARABLE. Their Meyer pointer checked in §2 |
| 4 | Meyer 1970, LNM 117 | `fetched-r9/…pdf` p. 25 (page image), pp. 24, 26, 63 (OCR) | unit-mass case: μ complex TB, 𝔉μ = Σ_Λ δ_λ ⟹ Λ is, up to a finite set, a finite union of progressions α_jZ + β_j | INPUT (Theorem D, now at the page; §2) |
| 5 | Kurasov–Sarnak 2020, JMP 61 | BFE `u-20b` 20–50, 731–739, 777–795 | positive idempotent FQs, not GDCs, abs(μ̂) not TB | INCOMPARABLE; (TB) keeps them out of 𝓜_r; their Meyer quote checked in §2 |
| 6 | Córdoba 1989, Lett. Math. Phys. 17, 191–196 ("Dirac combs") | Firecrawl capture of the Springer page, `verify-O/sources/cordoba-1989-springer.md`: abstract 29–31, references 95–112 (Rosenthal Mem. AMS 63; Meyer 1972; Zygmund) | "tempered distributions given by linear combinations of delta functions … whose Fourier transform is also a sum of the delta functions … finite superpositions of periodic structures" | INCOMPARABLE as far as the abstract goes (hypotheses not stated there); body UNVERIFIED (paywall); Córdoba 1988 CRAS not reached. It cites Rosenthal in the role Meyer does |
| 7 | Hilberdink–Lapidus 2006 | BFE `p3-22c1` 125–128, 1025–1057 | FE ⟺ modular identity; which Beurling systems satisfy an FE is left open | Q_cond is the conductor-q case of their open question; U_q, L′, E2, D answer parts of it. No containment |
| 8 | Kaczorowski–Perelli 1999 (Acta Math. 182), as stated in Perelli's survey | BFE `arxiv-1605.02354` 1065–1074 (Thm 3.6) | F ∈ S (Selberg class), d_F = 1 ⟹ F = L(s + iθ, χ); with a pole, F = ζ | the Selberg-class analog of U_q/D at every conductor, with ordinary Dirichlet series, Ramanujan and a Selberg Euler product; U_q/D use real frequencies and Π ≥ 0 instead: INCOMPARABLE. Replaces the NOTE's `[recalled, unverified]` in §4(h) |
| 9 | Baake–Spindeler–Strungaru 2023 (JFAA 29) | here `arxiv-2104.06812` 660–674 (Thm 4.3), 1030–1040, 1198–1236 | α-periodic Fourier eigenmeasures exist iff α = √n (DFT eigenvectors); u.d. eigenmeasures classified; general case open | U_q Step 3's "q ∈ N" is the positive, self-dual case of their Thm 4.3; context. INCOMPARABLE |
| 10 | Landau 1905 / Pringsheim; Meyer 2016 PNAS; Olevskii–Ulanovskii 2020; Gonçalves 2023; Favorov 2024; Lagarias 1999 | Lemma L proved in the NOTE (✓ §1(g)); Hilberdink 2012 948 cites "Landau's Oscillation Theorem (cf. [3], p.137)"; BFE `meyer-2016-pnas.md` 9–51, 95, 627; the NOTE's Q3, Q6, Q7 line numbers spot-checked; Lagarias title/abstract only | classical abscissa-singularity theorem; crystalline measures that are not GDCs; unit-mass FQs; spectral-gap classification; separated Poisson measures | METHOD (Landau) / INCOMPARABLE (the rest) |

Reader's arXiv API queries (`verify-O/sources/arxiv-queries/reader-O-q1…q8.xml`, one at a time, HTTPS): "Beurling" AND "functional
equation" (5 hits; only Hilberdink–Lapidus relevant, on disk); "generalized primes" AND "functional equation" (0); "periodic
coefficients" AND "Beurling" (0); Dirichlet series AND positive definite AND Fourier quasicrystal (0); au:Hilberdink (11; the 2012 Acta
Arith. paper is not on arXiv, nothing else relevant); "generalised prime" (2); Beurling AND quasicrystal (0); "Riemann functional
equation" AND "nonnegative coefficients" (0). No further prior art.

GATE VERDICT. No source read prints U_q, L′, E2, D or §1.6 as a statement. Labels (replacing `[novelty: single-check]`):
 • U_q — `[novelty: dual-checked — statement not in print as read; Step 4 is Hilberdink 2012 Prop. 4.2's S–W step; Step 5 has a printed
   alternative (Hilberdink 2012 Thms 4.3–4.4) plus the FE reflection; NEW: the self-duality ⟹ periodicity reduction (Steps 1–3) at
   conductor q, and the reflection]`.
 • L′ — `[novelty: dual-checked — statement for arbitrary real frequencies not in print; the Landau mechanism is printed for integer,
   divisor-supported multipliers (Hilberdink 2012 Thm 4.3, (∗)/(†), Thm 4.4); the FE reflection is new]`.
 • E2, E3, §1.4 Cor. 1–3, §1.6 — `[novelty: dual-checked — not found; routine consequences of positive-definiteness/Krein]` (E2 is
   the most substantive of these).
 • D — `[novelty: dual-checked — not found; unconditional via Meyer p. 25 (§2)]`.

## §5. FIX-FIRST items (OLD/NEW pairs; not applied to NOTE.md)

No error was found that makes U_q, L′, E1–E3, Prop. E/E′, §1.4, §1.6, Lemma S–W′, Lemma Q or Theorem D false as stated. Three
record-level items must be fixed before the NOTE is filed; F1 changes the status of a theorem (upward).

F1 — Theorem D is unconditional (re-derivation §2). Pairs at lines 322–325, 334–335, 427–430 (and consequential edits in m5).
OLD (322–325):
    THEOREM D. Assume Meyer's theorem (Q4). A discrete Beurling system (multiset P of reals > 1, integer multiplicities) whose Λ_F
    satisfies (A) at some conductor q > 0 is the rational primes, and q = 1.
     Proof. (1) E3: unit masses off 0; masses ∈ {1, ρ_q}; support locally finite; |μ̂_q| = μ_q translation bounded (TB). By Q4, μ_q = Σ_j
     g_jσ_j, finitely many trigonometrically weighted combs on lattice cosets. (2) §2.6(b): the classes [x] (x ∈ 𝒩) form a finite group
NEW:
    THEOREM D. A discrete Beurling system (multiset P of reals > 1, integer multiplicities) whose Λ_F
    satisfies (A) at some conductor q > 0 is the rational primes, and q = 1.
     Proof. (1) E3: unit masses off 0; support locally finite (§1.4 Cor. 2); μ_q translation bounded (TB). Put μ′ := μ_q − (ρ_q − 1)λ
     (λ = Lebesgue): μ′ is TB and 𝔉μ′ = Σ_{λ∈Λ}δ_λ, Λ = {0} ∪ ±𝒩/√q. Meyer 1970, LNM 117, §4.2 p. 25 (read at the page, read-O §2) gives
     Λ = ∪_{j≤k}(α_jZ + β_j) up to a finite set; inclusion–exclusion writes μ_q = Σ_iε_iδ_{A_i} + E with progressions A_i, ε_i ∈ Z and E
     finite atomic; Ê is absolutely continuous while μ̂_q = μ_q and the transform of the comb part are pure point, so E = 0 and μ_q =
     Σ_iε_iδ_{A_i} exactly (a generalized Dirac comb with constant weights; Lemma Q is then not needed). (2) §2.6(b): the classes [x] (x ∈ 𝒩) form a finite group
OLD (334–335):
    STATUS. Theorem D is (P) GIVEN Q4; Q4 is printed (Meyer 1970, LNM 117) but on disk only as quoted by Kurasov–Sarnak (u-20b 43–44)
    and pointed to by Lev–Olevskii 2015 (63–68). Unconditionally, D holds for every discrete system whose integers are u.d. (U_q).
NEW:
    STATUS. Theorem D is (P) on top of Meyer 1970, LNM 117, p. 25 (unit-mass case; on disk `fetched-r9/`, read at the page by read-O §2;
    its proof cites Rosenthal, Mem. AMS 63 (1966), Th. 1.6 p. 22, not on disk). The finite-values form (Q4) is not needed.
OLD (427–430):
    T given one printed theorem on disk only second-hand:
     • THEOREM D (§2.7). Given Meyer's finite-values theorem (Q4: Kurasov–Sarnak's statement, u-20b 43–44; Lev–Olevskii's pointer,
       1312.6884 63–68), every DISCRETE Beurling system with Riemann's exact FE at any conductor is ζ. Inputs: Lemma S–W′ (Saias–Weingartner
       Thm 2 with radical weights, checked against their proof line by line) and Lemma Q.
NEW:
    T on top of one printed theorem read at the page:
     • THEOREM D (§2.7). Every DISCRETE Beurling system with Riemann's exact FE at any conductor is ζ. Inputs: Meyer 1970 p. 25 applied to
       μ_q − (ρ_q − 1)·Lebesgue (read-O §2), Lemma S–W′ (Saias–Weingartner Thm 2 with radical weights, checked against their proof line by
       line; re-checked by read-O §1(j)).

F2 — Hilberdink 2012 (on disk since BFE, never cited for U_q/L′) and the novelty labels (gate §4 row 1).
OLD (243–245):
    NEAREST PUBLISHED OBJECTS (10(n)). U_q ↔ Lagarias 1999, "Beurling generalized integers with the Delone property" (BFE sources,
    title/abstract only: Delone g-integer systems contained in Z), and Hamburger's theorem (Nakamura Thm D, BFE sources). The step
    "periodic + zero-free on Re s > 1 ⟹ P·L_ψ" is Saias–Weingartner's; the Landau step is Theorem L′ (§2.3). `[novelty: single-check]`
NEW:
    NEAREST PUBLISHED OBJECTS (10(n)). U_q ↔ Hilberdink 2012 (Acta Arith. 152; BFE `p3-22c2-…txt`): for OUTER systems (Π ≥ 0, weights
    allowed) with N(x) − cx periodic, Prop. 4.2 (741–806) is Step 4's S–W step (S–W Corollary ⟹ N̂ = P·L_χ; χ principal by positivity
    there, by the pole in U_q; N̂ = Q·ζ, Q on the divisors of the period), and Thms 4.3–4.4 (812–1066) give a printed alternative to Step 5 up to the FE reflection (Q = Π_pQ_p, each
    Q_p zero-free on Re s > 0); Thm C (1122–1146) alone excludes every squarefree conductor (it forces |e_q| ≤ 1 < √q). Also Lagarias
    1999 (title/abstract only) and Hamburger's theorem (Nakamura Thm D). NEW in U_q: Steps 1–3 (self-duality ⟹ integers ⟹ q-periodicity
    at conductor q) and the reflection. `[novelty: dual-checked (read-O §4)]`
OLD (216):
    §11(i) (finite Euler factors) to all finite Dirichlet-polynomial multipliers. `[novelty: single-check]`
NEW:
    §11(i) (finite Euler factors) to all finite Dirichlet-polynomial multipliers. For integer multipliers supported on the divisors of
    a period, the Landau mechanism is Hilberdink 2012 Thm 4.3 + (∗)/(†) + Thm 4.4 (`p3-22c2` 812–1066; its (†) τ_n ≤ 1 is §3's "Q4");
    L′'s single-variable argument is shorter and holds for arbitrary real frequencies; the FE reflection is new. `[novelty: dual-checked (read-O §4)]`
OLD (407–411):
    the degree-1 classification in the Selberg class, where a degree-1 function with a pole is ζ `[recalled, unverified: Kaczorowski–
    Perelli; not load]` — U_q replaces Ramanujan and a rational-prime Euler product by Π ≥ 0 and u.d.; Saias–Weingartner (periodic
    coefficients, Q-side); Lagarias 1999 (Delone Beurling integers, title/abstract only); Hilberdink–Lapidus (3.5) (open in print).
    No statement of U_q, L′, E2 or D was found in the sources read here or in BFE §2/read-O §3. `[novelty: single-check]`
NEW:
    the degree-1 classification in the Selberg class, where a degree-1 function with a pole is ζ (Kaczorowski–Perelli 1999, as stated in
    Perelli's survey, BFE `arxiv-1605.02354` 1065–1074, Thm 3.6) — U_q replaces Ramanujan and a rational-prime Euler product by Π ≥ 0 and
    u.d.; Saias–Weingartner (periodic coefficients, Q-side); Hilberdink 2012 §4 (periodic outer systems: Prop. 4.2 = U_q Step 4, Thms
    4.3–4.4 = L′'s mechanism for integer multipliers, Thm C); Lagarias 1999 (title/abstract only); Hilberdink–Lapidus (3.5) (open in
    print). No statement of U_q, L′, E2 or D was found in the sources read here, in BFE §2/read-O §3, or by read-O §4. `[novelty: dual-checked]`

F3 — the (Q4) quote is replaced by the page (lines 69–72, 82–83).
OLD (69–71): (Q4) Meyer 1970 as stated by Kurasov–Sarnak (`u-20b-…txt` 43–44): "If aλ take values in a finite set and |µ̂| is translation
     bounded, that is sup |µ̂|(x + [0, 1]) < ∞, then µ is a generalized Dirac comb." SECONDARY: the primary (Meyer, LNM 117) is not on
     disk.
NEW: (Q4) Meyer 1970, LNM 117, §4.2 p. 25 (`fetched-r9/`, read at the page by read-O §2): « Supposons […] qu'il existe une mesure, à
     valeurs complexes, μ telle que a) sup ∫_x^{x+1}d|μ|(t) < +∞ b) 𝔉μ = Σ_{λ∈Λ}δ(x−λ). […] Λ est à un ensemble fini près, la réunion de k
     parties de R de la forme α_jZ + β_j ». Kurasov–Sarnak's finite-values wording (`u-20b` 43–44) and Lev–Olevskii's pointer (63–68)
     are broader than the page; the finite-values form is true for crystalline measures by Meyer's argument (read-O §2).
OLD (82–83): (ii) μ ∈ 𝓜_r with locally finite support and finitely many distinct masses is a generalized Dirac comb (Q4 + TB) — conditional
      on the secondary quote (Q4).
NEW: (ii) μ ∈ 𝓜_r with locally finite support and finitely many distinct masses is a constant-weight generalized Dirac comb (Meyer's
      Bohr passage + Lagrange idempotents in M(bR) + Cohen–Rosenthal + TB; the finite exceptions vanish because μ̂ = μ is pure point —
      read-O §2); for masses 1 off the origin it follows from the printed statement itself applied to μ − (ρ − 1)·Lebesgue.

## §6. MINOR pairs (precision; no statement changes)

m1 — §2.1, lines 149–150 (what "weight ≥ 1" must mean for weighted systems).
OLD: needs Π ≥ Π₁, i.e. p is a prime of
     weight ≥ 1).
NEW: needs Π ≥ Π₁, i.e. Π({p^k}) ≥ 1/k for every k ≥ 1 —
     automatic for a prime of a discrete system, NOT implied by Π({p}) ≥ 1 alone).
m2 — §2.2, line 182 (the "second route" uses BFE T for ρ = 1).
OLD: T) it gives Π_c = 0 — the continuous half of BFE Corollary T2 by a second route. `[novelty: single-check]`
NEW: T) it gives Π_c = 0 — the continuous half of BFE Corollary T2 by a second route, once ρ = 1 is known from BFE T. `[novelty: dual-checked]`
m3 — §2.3, line 206 (log h is not known to exist before the conclusion).
OLD: (4) Let σ_a be its abscissa. On Re s > max(σ_a, 0) the series and log h agree (both analytic; h is analytic on Re s > 0), so
NEW: (4) Let σ_a be its abscissa. On Re s > max(σ_a, 0) the exponential of the series equals h (both analytic; equal for σ large), so
m4 — §2.7, line 330 (the mass ρ_q at 0 is shared by the cosets through 0).
OLD: cosets in one class have commensurable lattices. So μ_q = ρ_qδ₀ + Σ_{γ∈Γ}κ_γ, κ_γ a periodic {0,1}-comb inside class γ, and
NEW: cosets in one class have commensurable lattices. So, off the origin, μ_q = Σ_{γ∈Γ}κ_γ, κ_γ a {0,1}-valued comb of class γ, periodic
     along one lattice of that class, and
m5 — consequential edits of F1 (same wording each time): line 28–29 "— given Meyer's finite-values theorem, on disk only second-hand —
     for every discrete Beurling system (Theorem D)" → "for every discrete Beurling system (Theorem D, on top of Meyer 1970 p. 25 read at
     the page)"; line 285 "CONDITIONAL on Meyer's theorem (Q4, secondary quote): μ_q is a generalized Dirac comb" → "By Meyer 1970 p. 25
     applied to μ_q − (ρ_q − 1)·Lebesgue (read-O §2): μ_q is a constant-weight generalized Dirac comb"; lines 397–398 (§4(e)) → "Theorem D:
     its only printed input is Meyer p. 25 (read at the page); Lemma S–W′ is an extension of a printed proof, read step by step twice";
     lines 432–433 delete "and the primary of Q4 (Meyer, LNM 117, p. 25), whose reading would make D unconditional"; lines 441–442 delete
     both "given Q4"; line 444–445 SUCCESSOR (1) → "(1) Rosenthal, Mem. AMS 63, Th. 1.6 at the page (the last input of D not on disk)".
m6 — §0 HEADLINE, lines 29–30 (credit for the replacement mechanism).
OLD: T is a Landau (Pringsheim) obstruction on the finitely generated "q-part" of the frequencies, where the pole of ζ is invisible.
NEW: T is a Landau (Pringsheim) obstruction on the finitely generated "q-part" of the frequencies, where the pole of ζ is invisible (for
     periodic outer systems the obstruction is printed: Hilberdink 2012 Thms 4.3–4.4).
m7 — §3 D4, lines 353–355: add after "(Q4)": "— Hilberdink 2012's condition (†) (`p3-22c2` 1012), whose Thm 4.4 gives |μ_r| < 1 for
     degree 2; with αβ = 5 that is impossible, so 'Q4 admits no t' is a printed theorem on this family."

## §7. What the reader adds, and what next

R1 — THEOREM D WITHOUT THE FINITE-VALUES THEOREM (§2): subtract (ρ_q − 1)·Lebesgue and Meyer's printed unit-mass case applies; the finite
  exceptional set dies by pure point vs absolutely continuous; by-product ρ_q ∈ Z for any discrete candidate (≥ 2 with U1).
R2 — MEYER'S FINITE-VALUES FORM, PROVED from his Bohr passage (Lagrange idempotents in M(bR), Cohen, Rosenthal), with the counterexample
  μ = δ₀ showing that K–S's "is a generalized Dirac comb" needs their crystalline context. Q4 of the NOTE is therefore true, secondary no more.
R3 — U_q IS NOW DUAL-ROUTED: the NOTE's (S–W Thm 4 + L′) and the printed (Hilberdink 2012 Prop. 4.2 + Thms 4.3–4.4) + FE reflection;
  Thm C disposes of every squarefree conductor in one line. The Landau mechanism of L′ is the real-frequency extension of Hilberdink §4.
R4 — (E) is a measure identity valid for every finite signed sieve (o1: six widths, signed w), so the Euler-side identities carry no
  information beyond self-duality + the sieve — the LP could never see Π ≥ 0 (confirms §2.5's WHY-NOT at the level of identities).
NEXT (ranked). (1) The G corner, as a construct-or-refute unit: for a positive self-dual μ with locally finite support the atom function is
  a Fourier–Stieltjes transform on R_d (Meyer's passage needs only TB) and positive definite (Lemma PD); with infinitely many values no
  idempotent is available. Either prove that the monoid structure of a weighted Beurling system forces finitely many values of c on
  𝒩 (then D applies verbatim), or construct a positive self-dual non-GDC measure with a gap (none known in print: BSS §8, K–S). (2) Fetch
  Rosenthal Mem. AMS 63 Th. 1.6 (the last not-on-disk input of D), or prove the special case "a locally finite set in the coset ring of R_d
  is a finite union of progressions up to a finite set" in-house (the normal form a + H ∖ ∪(b_j + K_j) is elementary; the missing piece
  is a local Neumann lemma for dense H). (3) Apply F1–F3 and m1–m7 to NOTE.md, keep `NOTE.pre-reader.md`.
