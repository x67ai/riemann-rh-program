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

