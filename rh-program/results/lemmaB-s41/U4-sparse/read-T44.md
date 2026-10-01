# read-T44 — second reader on Theorem 4.4 (scaling-limit macroscopic law) of `NOTE.md`

VERDICT: AGREES-WITH-CORRECTIONS — Theorem 4.4 is correct as stated, for every ρ ∈ (0, 1/16] (no transcendence used).
One GAP, fillable and filled in §2 (the local mass bound for κ_ρ in Step 3: the dominating measure was misnamed and
the local form of the smoothing was not written out). No step is FALSE. One sentence of the §0 Close is FALSE as
literally worded (it drops the x ≥ p₁² qualifier). The rest are editorial, plus commentary in §0/§4.8 on why the
argument fails at fixed ρ: it names a "margin f₀ > 0" that the proof never uses. OLD/NEW texts in §4.

Reader: Opus 5.5 (agent), referee pass started 18:14 IST 2026-10-01. Scope: `NOTE.md` §4 — Lemma 4.2, Lemma 4.3,
Theorem 4.4 (Steps 1–5), Lemma 4.6 — with the facts they quote from §1–§3 and from the Session-40 NOTE (Lemmas 1.0–1.2).
Method: every step re-derived by hand; cheap numerical checks in the reader's scratch directory (scripts and outputs
described in §3 below; nothing written into `verify/`). Marks: ✓ (re-derived), GAP (missing argument; fillable or not),
FALSE (counterexample or failing inequality).

## 1. Step-by-step

### 1a. Inputs from §1 and Session 40
| Item | Mark | Note |
|---|---|---|
| E > −½ everywhere; E(p) = ½ at every g-prime; g-primes on the lattice (S40 Lemmas 1.0–1.2) | ✓ | Re-derived for every ρ, ties included: a composite on a lattice point is counted first, so D < ½ there and no prime is placed; products involving a new prime p exceed p. Checked exactly at t = 18 and t = 32 (N2, §3). |
| U4 Lemma 1.1(i): every lattice point in [1, p₁²) is a g-prime | ✓ | Half-open interval matters: for integer t ≡ 2 (mod 4), p₁² is itself a lattice point (k = t/4 + 3/2) and carries the composite p₁·p₁, so it is busy (ρ = 1/18: p₁² = 100 = x₆). |
| U4 Lemma 1.2 (Lindley form, E(x_k) = e_k + ½) | ✓ | e_k = N(x_k) − (k + 1); prime at x_k ⟺ N(x_{k−1}) + c_k = k ⟺ e_{k−1} + c_k = 0. Zero mismatches in N2. |

### 1b. Lemma 4.2 (exact identities)
| Item | Mark | Note |
|---|---|---|
| (i) π(y,x] + C(y,x] = ρ(x − y) + E(x) − E(y) | ✓ | Definition of E with N = 1 + π + C. |
| (ii) C(y,x] = Σ_{M′} π(J_{M′}), elements of contributing M′ ≤ √x | ✓ | n ↦ (n minus one copy of P⁺(n), P⁺(n)) is a bijection from composite multisets with product in (y, x] onto pairs (M′ ≠ ∅, g-prime P ≥ P⁺(M′)) with m′P ∈ (y, x]; multiplicity is respected, so no transcendence is used. Q ∈ M′ ⇒ Q² ≤ Q·P ≤ x. |
| (iii) E(x) ≤ ½ + sup_{y<x}(C(y,x] − ρ(x − y))⁺ | ✓ | y = largest g-prime ≤ x, E(y) = ½, π(y, x] = 0; x itself a g-prime and x < p₁ are trivial. Identity checked exactly at every integer x ≤ 10⁷ (N2). Citation: E(p) = ½ is S40 l. 49–50 (claim 1.0(ii)), not l. 52 (E6). |

### 1c. Lemma 4.3 (integer regularity ⇒ vague prime law)
| Item | Mark | Note |
|---|---|---|
| (a) ν_ρ = exp*(μ̃_ρ) | ✓ | Euler product over the multiset monoid; holds with coincident products. |
| (b) ν_ρ(I) = ρ log(b/a) + E(b)/b − E(a)/a + ∫E u^{−2}; abs(ν_ρ(I) − abs(I)) ≤ ε_ρ abs(I) + β_ρ | ✓ | Re-derived: upper error ≤ ε_ρ abs(I) + ε_ρρ + (4K + 1)ρ, lower ≥ −ε_ρρ − (2K + 2)ρ, plus ≤ s₁ ≤ ρ log(1/ρ) when v₁ < s₁. Fits inside β_ρ = (4K + 6)ρ log(1/ρ). The name β_ρ clashes with β_ρ(v) of Thm 4.4 (E4). |
| (c) σ_ρ^{*n}([0, S]) ≤ 3^n(S + nβ_ρ)^n/n!, uniform tail | ✓ | Only σ_ρ restricted to [0, S] enters, so the density bound 3 is needed only there; n ≤ S/s₁ gives nβ_ρ ≤ (8K + 12)S. |
| (d) σ_ρ^{*n} → v^{n−1}/(n−1)! dv on intervals | ✓ (wording) | The hypothesis is known only on [0, S], so "restrictions to [0, S + 1]²" should read [0, S]² and "vaguely on [0, ∞)" should read "weakly on [0, S]" (E5). The argument is otherwise right: weak convergence of the restrictions, pushforward by addition, Lebesgue-null boundaries. |
| (e) convolution log; μ̃_ρ − μ_ρ mass ≤ 10ρ²; Mertens uniform by monotonicity | ✓ | Σ(−1)^{n+1}v^{n−1}/n! = f₀(v). Uniformity follows because both sides are nondecreasing in τ and the limit is continuous. |

### 1d. Theorem 4.4
| Item | Mark | Note |
|---|---|---|
| Statement | ✓ | Correct as written: one-sided in E, and x ≥ p₁² for the first two sups. The restriction is needed because a single lattice point costs 1/(ρx), which is 4ρ at x = p₁² but of order 1 at x ≍ t. The §0 paraphrase drops both qualifiers (E2). |
| α_ρ, β_ρ: nondecreasing, α_ρ ≤ 2 | ✓ | A sup over growing sets; set sup ∅ := 0 for e^{v/ρ} < p₁² (E7). abs(π − Π₀) ≤ ρ(x − y) + 1 (gaps ≥ t, 0 ≤ Π₀ ≤ ρ(x − y)), and 1/(ρx) ≤ 1/(ρp₁²) ≤ 4ρ. The β_ρ bound "Λ(S) + 2" holds only for small ρ (it uses S_ρ → Λ, Prop. 3.1), but nothing uses it: reverse Fatou needs only α_ρ ≤ 2. A(v) := limsup α_ρ(v) is nondecreasing, hence measurable. |
| Step 1: E(x) ≤ ½ + β_ρ(v)ρx | ✓ | (C − ρ(x−y))⁺ ≤ (C − Λ₀)⁺ needs only Π₀ ≥ 0, i.e. f₀ ≥ 0. For x < p₁², E ≤ ½ by Lemma 1.1(i), so the bound holds for every x ≤ e^{v/ρ}. |
| Step 2: α_ρ(v) ≤ 2β_ρ(v) + 4ρ, so A ≤ 2B | ✓ | π − Π₀ = (Λ₀ − C) + E(x) − E(y). Then abs(E(x) − E(y)) < 1 + β_ρ(v)ρx, using E(y) ≤ ½ + β_ρ(v)ρy ≤ ½ + β_ρ(v)ρx and E > −½. Same admissible set of pairs on both sides. Holds pointwise in v, so A(v) ≤ 2B(v). |
| Step 3, window errors in T₁ | ✓ | J_{M′} ⊂ [P⁺(M′), x/m′] ⊂ [p₁, ∞), so the left end is ≥ 1 and α_ρ applies with right end x/m′ = e^{(v−u)/ρ}; the closed left end is a limit of half-open windows. When x/m′ < p₁²: abs(π(J) − Π₀(J)) ≤ 1 + ρ(x/m′)s₁ (NOTE: 2s₁, weaker, fine). There are at most Q(x) such M′ with J ≠ ∅. |
| Step 3, Q(x) ≤ 4ρ²x e^{2S+4ρ} | ✓ (typo) | §2 has an extra + log x/log p₁; at x ≥ p₁² it costs ≤ 8ρ·ρx. Harmless (E1). σ_x ≤ τ_x + 2ρ re-derived from the digamma form. |
| Step 3, local mass κ_ρ(I) ≤ K_S(abs(I) + ρ log(1/ρ)) | GAP, fillable — filled in §2 | (1) "κ_ρ dominated by exp*(λ_ρ) − δ₀" is false at atoms of repeated-element multisets: {P, P} weighs 1/P² in κ_ρ but only 1/(2P²) in λ_ρ^{*2}/2!. The right majorant is exp*(λ̃_ρ) − δ₀ with prime powers included. (2) Lemma 4.3(c) is a total-mass bound; the local version needs the enlargement I + [0, 2nρ] and the factorial weights, which the NOTE does not write. Both repaired in §2. The bound then holds with abs(I) + ρ in place of abs(I) + ρ log(1/ρ), and the NOTE's K_S still works. N3 measures κ(I) ≤ 1.9(abs(I) + ρ) at ρ = 1/32 and 1/18. |
| Step 3, partition at scale δ_ρ | ✓ | α_ρ nondecreasing ⇒ Σ_i α_ρ(v − iδ)δ ≤ ∫₀^v α_ρ + 2δ (telescoping), and the ρ log(1/ρ) parts add 2K_S(v/δ + 1)ρ log(1/ρ). Total o(1) = O_S((ρ log(1/ρ))^{1/2}), uniform in v ≤ S and in y. |
| Step 3, T₂ via Lemma 4.6 | ✓ | See 1e. |
| Step 4: D_ρ(w) ≤ ∫₀^w α_ρ + o(1) | ✓ | Integration by parts: μ_ρ(I) − ∫_I f₀ = ∫_{(a,b]} dΔ/u with Δ(a) = 0. abs(Δ(u)) ≤ α_ρ(ρ log u)ρu for u ≥ a ≥ p₁², so the bound is ≤ ρα_ρ(w) + ∫_{w₁}^{w₂} α_ρ (NOTE: 2ρα_ρ, fine). Below 2s₁ the error is ≤ s₁ + 2ρ + 2s₁² = O(ρ log(1/ρ)), where s₁ covers the empty stretch [0, s₁). Straddling intervals split at 2s₁. Closed or open intervals follow by monotone limits. The busy point p₁² (E3) adds ≤ 4ρ². |
| Step 5: β_ρ(v) ≤ (K_S + L_S)∫₀^v α_ρ + o(1) | ✓ | For each admissible x with v_x ≤ v: ∫₀^{v_x} ≤ ∫₀^v (α ≥ 0), and D_ρ(v_x/2) ≤ ∫₀^{v_x} α_ρ + o(1). All o(1) terms are uniform. |
| Step 5: reverse Fatou | ✓ | 0 ≤ α_ρ ≤ 2 on [0, v]: limsup ∫α_ρ ≤ ∫ limsup α_ρ (and if ρ → 0 continuously, pass to a sequence realizing the limsup). |
| Step 5: Gronwall-type closing | ✓ (edge case) | A nondecreasing ⇒ A > 0 on (v₁, S]; for v₁ < v < v₁ + 1/(2c), c := 2(K_S + L_S): A(v) ≤ c(v − v₁)A(v) ≤ ½A(v), contradiction. The case v₁ = S (A = 0 on [0, S), A(S) > 0) is not covered by the displayed interval but is immediate: A(S) ≤ c∫₀^S A = 0 (E8). Monotonicity is not needed at all: a bounded measurable A with A ≤ c∫₀^v A vanishes (iterate to A ≤ 2(cv)^n/n!). B ≡ 0 then follows by reverse Fatou again, and Step 1 gives the E claim. |
| Mertens corollary | ✓ | From Lemma 4.3 with ε_ρ = β_ρ(S), K = ½, or directly from Step 4 (D_ρ(S) → 0). |

### 1e. Lemma 4.6 (cofactor functional is Lipschitz in the prime discrepancy)
| Item | Mark | Note |
|---|---|---|
| (a) closed form of g | ✓ | w = (x/m′)e^{−θ}: θ = 0 ↔ x/m′, θ = L ↔ y/m′, θ = (v − u − σ)/ρ ↔ P⁺(M′); ρ log w = v − u − ρθ ≥ σ > 0, so f₀ is evaluated only at positive arguments. g ∈ [0, 1]. f₀(τ) = ∫₀¹e^{−τs}ds gives abs(f₀′) ≤ ½, so abs(g − g₁) ≤ (ρ/2)∫θe^{−θ}dθ = ρ/2. Summed with weight 1/m′ (total ≤ e^{M}) on each side: O(ρ). Why g₁ is needed: g itself is not monotone in u (integrand rises, upper limit falls); g₁ = φ(Σu)·h(v − Σu − max u) is the product of a nondecreasing function of Σu and a nonincreasing function of Σu + max u. |
| (b) S8 side as Σ_j (1/j!)∫ g dμ_ρ^{⊗j} + O(ρ²) | ✓ | Distinct-element multisets correspond to j! ordered tuples. The repeated-element multisets weigh ≤ (Σ_a x_a^{−2})·h_{j−2} on the multiset side and ≤ (Σ_a x_a^{−2})σ^{j−2}/(2(j−2)!) on the ordered side; both sums over j are O(ρ²). The h_n bounds (Cauchy at ζ = n/2σ or p₁/2) were re-derived. |
| (b) template has the same largest-element decomposition | ✓ | exp*(μ₀) − δ₀ − μ₀ = Σ_{n≥2} μ₀^{*n}/n!. Since μ₀ has no atoms, μ₀^{⊗n}/n! = (1/(n−1)!)·μ₀^{⊗(n−1)} ⊗ μ₀ restricted to {last coordinate largest} (symmetry; ties are null). Multiplying by u = m′P to undo the 1/u weight turns the inner integral over the largest element into m′Π₀(J_{M′}) = ρx·g. Combined with Lemma 1.3, (exp*(f₀ds) − δ₀ − f₀ds = λ₀ds), this gives Λ₀(y,x] = ρxΣ_j (1/j!)∫g dμ₀^{⊗j}. Restricting to [0, v/2] loses nothing, since g = 0 unless Σu + max u ≤ v. Confirmed numerically (N1): agreement to (0.5–5)·10⁻⁵ at four (v, ρ, L). |
| (c) mixtures | ✓ | φ(s) = f₀(v − s) = φ(0) + ∫_{(0,v]}1{s ≥ r}dφ(r) on [0, v], with positive weights (f₀ ≥ 0, nonincreasing) and total φ(v) = 1. The layer-cake form h(r′) = ∫₀¹1{r′ > r_θ}dθ, r_θ = −ρ log(1 − θ) ≥ 0 (= +∞ for θ ≥ 1 − e^{−L}). φ's representation fails for Σu > v, but there every h-indicator vanishes (Σu + max u < v − r_θ ≤ v forces Σu < v), so the product mixture equals g₁ on all of [0, v/2]^j. |
| (c) interval sections | ✓ | In u_i with the other coordinates fixed: {Σu ≥ r} is a half-line; Σu + max u is continuous and nondecreasing in u_i, so {Σu + max u < c} is an initial segment; intersecting with [0, v/2] gives an interval (any end-type). D_ρ covers all end-types by monotone limits (μ_ρ({0}) = 0). |
| (c) telescoping bound | ✓ | μ^{⊗j} − μ₀^{⊗j} = Σ_i μ^{⊗(i−1)} ⊗ (μ − μ₀) ⊗ μ₀^{⊗(j−i)} (finite measures, Fubini). Integrate the i-th coordinate first over its interval section: ≤ D_ρ(v/2), then the remaining positive mass ≤ M^{j−1} with M = max(μ_ρ, μ₀)([0, v/2]) ≤ v/2 + 2ρ. Σ_j j M^{j−1}/j! = e^{M} ≤ e^{S/2+1/8} ≤ L_S. |

### 1f. The five points of the brief
(a) α_ρ, β_ρ, A ≤ 2B and B ≤ (K_S + L_S)∫A: correct. The admissible sets agree, and every o(1) is uniform in y and in v ≤ S. The o(1)s are: 4ρ (Step 2); K_S[(2 + 2v)(ρ log 1/ρ)^{1/2} + 2ρ log(1/ρ)], 2s₁K_S(v + ρ log 1/ρ) and Q/(ρx) ≤ 4ρe^{2S+4ρ} + 8ρ (Step 3); ρe^{M} + O(ρ²) (Lemma 4.6); 2ρ + O(ρ log 1/ρ) (Step 4). So ε_ρ = O_S((ρ log(1/ρ))^{1/2}).
(b) Gronwall closing: valid. A is nondecreasing and bounded, and reverse Fatou applies with dominating constant 2; edge case E8.
(c) Lemma 4.6: closed form, template decomposition, sections and telescoping are all correct.
(d) Local mass bound: GAP, filled in §2.
(e) Transcendental 1/ρ: nothing in §4 uses it. Every count is over multisets, the tie rule gives E(p) = ½ and E > −½ for all ρ, and Lemma 1.1(i) is stated on [1, p₁²). As a stress test, ρ = 1/18 was run exactly (N2): every composite of that system lies on a lattice point (10 is idempotent mod 18), with 46,992 tie-rule decisions and up to 6 multisets per value below 4·10⁶. All the identities hold exactly, and the window errors match ρ = 1/32.

## 2. The GAP in Step 3 and its fill (local mass bound for κ_ρ)

**What is wrong.** The NOTE's majorant exp*(λ_ρ) − δ₀ is not a majorant. The lattice multiset measure is
Σ_{M≠∅} δ_{ρ log m}/m = exp*(λ̃_ρ) − δ₀, with λ̃_ρ := Σ_a Σ_{k≥1} k^{−1}x_a^{−k} δ_{kρ log x_a}, by the Euler product exactly as
in Lemma 4.3(a). With λ_ρ alone, the n-fold term (1/n!)λ_ρ^{*n} sees a multiset with multiplicities (e_a) as n!/Πe_a! ordered tuples, so
it gives it the weight (1/n!)(n!/Πe_a!)(1/m) = (1/Πe_a!)(1/m). That undercounts every multiset with a repeated element. At the
point 2ρ log P, for example, κ_ρ has the atom 1/P² from {P, P} (when P²·P ≤ x), but λ_ρ^{*2}/2! has only 1/(2P²) there
(for transcendental t no other pair has the same product). Second, the smoothing of Lemma 4.3(c) bounds total mass on [0, S]. A local
bound on short intervals is what Step 3 needs, and the n-dependence of the smoothing error has to be absorbed.

**Fill (proved here by the reader; constants explicit).** Assume ρ ≤ 1/16, so p₁ ≥ 9 and log p₁ ≥ 2.
1. *Majorant.* 0 ≤ κ_ρ ≤ exp*(λ̃_ρ) − δ₀ on [0, v], since κ_ρ is a sub-sum of the lattice multiset measure.
2. *One-fold local bound.* For an interval I with v₁ < v₂: λ_ρ(I) = Σ 1/x_a over x_a ∈ (e^{v₁/ρ}, e^{v₂/ρ}] ≤ 1/x_first + (1/t)∫du/u ≤ abs(I) + 2ρ
   (1/x is decreasing, spacing t, x_first ≥ p₁ ≥ 1/(2ρ)). The prime-power part λ̃_ρ − λ_ρ has total mass
   Σ_aΣ_{k≥2}x_a^{−k}/k ≤ Σ_a x_a^{−2} = ρ²ψ′(½ + ρ) ≤ (π²/2)ρ² ≤ 5ρ². Hence λ̃_ρ(I) ≤ abs(I) + 2ρ + 5ρ² ≤ abs(I) + 3ρ.
3. *Smoothing.* Let U be uniform on [0, 2ρ]. Then λ̃_ρ * U has density λ̃_ρ([w − 2ρ, w])/(2ρ) ≤ (4ρ + 5ρ²)/(2ρ) ≤ 3,
   so (λ̃_ρ * U)^{*n} has density ≤ 3^n w^{n−1}/(n − 1)! at w. For any finite measure ν on [0, ∞) and interval
   I = (v₁, v₂]: ν(I) ≤ (ν * U^{*n})((v₁, v₂ + 2nρ]), since every shift s ∈ [0, 2nρ] keeps (v₁, v₂] inside the shifted
   window. Therefore, for I ⊂ [0, v], λ̃_ρ^{*n}(I) ≤ 3^n(abs(I) + 2nρ)·W^{n−1}/(n − 1)!, W := v + 2nρ.
4. *Only n ≤ v/s₁ occur.* λ̃_ρ lives on [s₁, ∞), s₁ = ρ log p₁, so λ̃_ρ^{*n}([0, v]) = 0 for n > v/s₁. For the remaining n,
   2nρ ≤ 2v/log p₁ ≤ v, so W ≤ 2v ≤ 2S.
5. *Sum with the factorial weights.* κ_ρ(I) ≤ Σ_{n≥1}(1/n!)·3^n(abs(I) + 2nρ)(2S)^{n−1}/(n − 1)!
   ≤ 3I₀(2√(6S))·abs(I) + 6I₀(2√(6S))·ρ, using n/n! = 1/(n−1)! and Σ_m z^m/(m!)² = I₀(2√z).
   So **κ_ρ(I) ≤ K′_S(abs(I) + ρ), K′_S := 6I₀(2√(6S))**, for every interval I ⊂ [0, S], uniformly in x ≤ e^{S/ρ} and in t
   (rational or not; atoms included).
6. *Constant.* 6I₀(2√(6S)) ≤ 0.70·4e^{2S+2} for every S ∈ (0, 200] (grid check, maximum ratio 0.697 at S ≈ 1.22), and
   the ratio tends to 0 beyond. So the NOTE's K_S = 4e^{2S+2} stays valid, and its weaker form K_S(abs(I) + ρ log(1/ρ))
   follows a fortiori. The rest of Step 3 is unchanged.
Numerically (N3, the full lattice multiset measure, which majorizes κ_ρ): max over windows of κ(I)/(abs(I) + ρ) is
1.88 (ρ = 1/32, S = 0.5) and 1.80 (ρ = 1/18, S = 0.8), attained by the single atom 1/p₁ ≈ 2ρ. The "+ρ" term is
genuinely needed, and the true constant is about 2.

## 3. Numerical checks (reader's scratch, each run < 20 s; Python/numpy/scipy)
Scripts live in the reader's session scratch directory (`…/scratchpad/t44/`: `n1_template.py`, `n2_exact.py`, `n3_kappa.py`
and their logs). They are not part of the record; the numbers below are the full output that matters.
- **N1 — template side of Lemma 4.6(a)–(b).** Λ₀(y, x]/(ρx), computed directly as ∫_{e^{−L}}^1(1 − f₀(v + ρ log r))dr, against
  Σ_{j≤6}(1/j!)∫g(Σu, max u)Πf₀(u_i)du with the closed-form g (j = 1 by quadrature, j ≥ 2 by Monte Carlo, 2·10⁶ points):
  (v, ρ, L) = (1, 0.05, 0.3): 0.094858 vs 0.094853; (2, 0.05, 1): 0.356856 vs 0.356824; (2, 0.02, 5): 0.560964 vs
  0.560914; (3, 0.03, 0.7): 0.343547 vs 0.343507. The differences, (0.5–5)·10⁻⁵, are within MC noise plus j > 6 truncation.
- **N2 — exact integer runs at even t** (lattice x_k = tk − t/2 + 1 is integral, so all g-integers are integers):
  t = 18 to 4·10⁶ (τ ≤ 0.845) and t = 32 to 10⁷ (τ ≤ 0.504). For t ≡ 2 (mod 4) the lattice residue r = t/2 + 1 is
  idempotent mod t, so every composite lies on a lattice point. t = 18: 47,430 busy lattice points, 46,992 decided by
  the tie rule, 12,144 composite values carrying ≥ 2 multisets (max 6). t = 32: 2,765 busy, 2,443 ties, max multiplicity
  5. In both runs: zero Lindley mismatches; min E(n−) = −½ exactly, attained only at primes and ties; min E(n) = ½ − (t − 1)/t
  > −½; E(p) = ½ at every g-prime (to 10⁻¹²); Lemma 4.2(iii) holds at every integer x. Window errors on a grid
  (y = x(1 − η), η ∈ {0.02, …, 0.98}): over x ∈ [10⁵, X], max abs(π − Π₀)/(ρx) = 0.0368 (t = 18), 0.0372 (t = 32), and
  max abs(C − Λ₀)/(ρx) = 0.0367, 0.0373. Over x ∈ [p₁², X] the maxima are 0.13 and 0.09, which is the 1/(ρx) granularity
  at x ≈ p₁². Σ_{p≤x}1/p − Ein(τ) = −0.035 (t = 18, τ = 0.845) and −0.034 (t = 32, τ = 0.504), the size of the offsets
  in NOTE §4.7. Nothing distinguishes the degenerate rational systems from the transcendental runs of the NOTE.
- **N3 — local mass (point d).** Shown in §2: κ(I) ≤ 1.9(abs(I) + ρ) on all windows, and 6I₀(2√(6S)) ≤ 0.70·4e^{2S+2} for every S.

## 4. Corrections for NOTE.md (OLD → NEW; the reader has not edited NOTE.md)
Line numbers refer to NOTE.md as of 18:22 IST (461 lines). NOTE.md was edited during this read: 17 lines were inserted
before §4, and the §4 text was re-read afterwards and is unchanged. The OLD strings are therefore the anchors; each was
checked to occur exactly once. "↵" marks a line break in OLD.

**G1 (GAP, Step 3, l. 279–280) — the local mass bound.**
OLD: `κ_ρ is dominated by the lattice monoid exp*(λ_ρ) − δ₀; smoothing λ_ρ (λ_ρ(I) ≤ |I| + 2ρ) by the uniform law on [0, 2ρ] as in↵Lemma 4.3(c) gives κ_ρ(I) ≤ K_S(|I| + ρ log(1/ρ)), K_S := 4e^{2S+2}.`
NEW: `κ_ρ is dominated by the lattice multiset measure exp*(λ̃_ρ) − δ₀, λ̃_ρ := Σ_aΣ_{k≥1}k^{−1}x_a^{−k}δ_{kρ log x_a} (Euler product; exp*(λ_ρ) alone gives a multiset with multiplicities (e_a) only 1/Πe_a! of its weight), and λ̃_ρ(I) ≤ |I| + 2ρ + Σ_a x_a^{−2} ≤ |I| + 3ρ for every interval I. With U uniform on [0, 2ρ], λ̃_ρ * U has density ≤ 3; since ν(I) ≤ (ν * U^{*n})(I + [0, 2nρ]) for every measure ν, λ̃_ρ^{*n}(I) ≤ 3^n(|I| + 2nρ)(2v)^{n−1}/(n − 1)! for I ⊂ [0, v] (only n ≤ v/s₁ occur, and then 2nρ ≤ 2v/log p₁ ≤ v). Dividing by n! and summing over n: κ_ρ(I) ≤ 6I₀(2√(6S))(|I| + ρ) ≤ K_S(|I| + ρ), K_S := 4e^{2S+2} (6I₀(2√(6S)) ≤ 0.7·4e^{2S+2} for all S > 0).`
(With |I| + ρ the rest of Step 3 is unchanged, a fortiori. Optional simplification, see §5: the partition can be replaced by a
layer-cake step.)

**E1 (Step 3, l. 277) — the Q bound.**
OLD: `Q(x) ≤ 4ρ²x e^{2S+4ρ} (§2):`
NEW: `Q(x) ≤ 4ρ²x e^{2S+4ρ} + log x/log p₁ ≤ ρx(4ρe^{2S+4ρ} + 8ρ) for x ≥ p₁² (§2):`

**E2 (FALSE as literally worded; §0 Close, l. 24–25).** Counterexample: at x = p₁ = 1 + t/2, E(p₁) = ½ and ρp₁ = ½ + ρ, so
E(x)/(ρx) → 1 rather than 0. Likewise π(1, p₁] − Π₀(1, p₁] = 1 − (½ + O(ρ log(1/ρ))), which is of order ρx and not o(ρx). Theorem 4.4's own
statement (one-sided in E, x ≥ p₁² for the first two) is right; the Close must carry the same qualifiers.
OLD: `For every S, uniformly on x ≤ e^{S/ρ} as ρ → 0: π(y, x] = Π₀(y, x] + o(ρx),↵C(y, x] = Λ₀(y, x] + o(ρx), E(x) = o(ρx), and Σ_{p≤x} 1/p → Ein(τ)`
NEW: `For every S, uniformly on 1 ≤ y < x, p₁² ≤ x ≤ e^{S/ρ} as ρ → 0: π(y, x] = Π₀(y, x] + o(ρx), C(y, x] = Λ₀(y, x] + o(ρx), E(x) = o(ρx); on all of 1 ≤ x ≤ e^{S/ρ}, −½ < E(x) ≤ ½ + o(ρx); and Σ_{p≤x} 1/p → Ein(τ)`

**E3 (Step 4, l. 285).**
OLD: `On [0, 2s₁] every lattice point is a g-prime`
NEW: `On [0, 2s₁) every lattice point is a g-prime (p₁² itself can be a busy lattice point — for integer t ≡ 2 mod 4, e.g. ρ = 1/18, p₁² = x₆ carries p₁·p₁ — and its mass 1/p₁² ≤ 4ρ² is absorbed)`

**E4 (Lemma 4.3(b)–(c), l. 252–255) — name clash with β_ρ(v) of Theorem 4.4.** Replace every `β_ρ` in Lemma 4.3 by `b_ρ`
(occurrences: `ε_ρ|I| + β_ρ`, `β_ρ := (4K + 6)ρ log(1/ρ)`, `2|I| + β_ρ`, `[0, β_ρ]`, `σ_ρ([w − β_ρ, w])/β_ρ`, `S + nβ_ρ` twice, `nβ_ρ ≤`).

