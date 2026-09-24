# PAIR 1 — W1-14 lorentzian-log-concavity — SCOUT F (Fable 5.1), blind report on rung (R-b)

**Written 2026-09-24 (Session 24, item 2), by scout F, blind: `scout-O.md`, every `SHARED.md` block but my own, and any `adjudication.md` were not opened.** Contract: `results/grossmann-rescout-s22/pair1-lorentzian/LAUNCH-NOTE.md` (all of it); `results/grossmann-rescout-s22/SCOUT-BRIEF.md` lines 5–11; `results/grossmann-rescout-s22/PRICING.md` §0 (lines 11–22), §1 (lines 26–92), §4(i) line 248, §4(iii) lines 259–267, §4(iv)–(v) lines 276–283. Sources read at the page: `results/grossmann-rescout-s22/verify/bh-text.txt` (Brändén–Huh, arXiv:1902.03719; lines cited below) and `results/grossmann-rescout-s22/verify/milne-text.txt` (Milne, arXiv:1509.00797; lines cited below); `BARRIER-ZOO.md` I.1 (45–52), II.4 (136–149), III.1 (163–169), III.6 (203–210), III.16 (288–298), III.20 (324–331), IV.1 (345–351), IV.18 (484–492), IV.19 (517–523), V.5 (557–567); `results/grossmann-sweep.json` `reports[14]` (extracted with Python's `json` module, all fields); `results/c2-followups/insights-digest.md` §D(ii) (lines 200–207); `scripts/rh-grossmann-sweep.js` lines 12–17 (the S1–S5 spec) and 75–86 (the schema). Every factual sentence names its file and line; inferences of mine are marked "I infer"; nothing is quoted from memory. No web access was used. U.S. English. One computation (sympy/numpy, Appendix A, reproduced verbatim so that this file is the whole deliverable) checks the hand derivation of §2.4–§2.5; it decides nothing the reading does not decide.

---

## 1. Verdict block (wave-1 schema, `scripts/rh-grossmann-sweep.js` lines 75–86)

- **branch:** W1-14 lorentzian-log-concavity (Brändén–Huh Lorentzian polynomials; the unbuilt prime-side sector suspended by the III.16 rider of 2026-09-16, `BARRIER-ZOO.md` line 296).
- **verdict:** **instrument** (the re-filing PRICING §1(c) line 64 attaches to the return YES-by-the-square; the dead-end grade on an INDEPENDENT prime-side sector is restored on internal grounds in the precise form of §4 below).
- **confidence:** 0.88 in the verdict; the rung's mathematics (§2) is verified at the page and by the computation of Appendix A and carries no confidence discount.
- **(R-b) return:** **YES-by-the-square** — §4.

### fit (0–5, one line each, internal properties only; V.5 applied)

- **S1: 1** — On the only rung where RH is a theorem, the Lorentzian object with von Mangoldt coefficients (§2.4) consumes the point count N₁ as an intersection number Γ_π·Δ on C × C and gets its nonnegative coefficients from nef·effective (§2.4), not from an axiom "Λ ≥ 0"; the input DH violates is the doubled object itself (III.20 item 1, `BARRIER-ZOO.md` line 326: "Weil positivity over Z is the diagonal shadow of the missing Hodge-index inequality"), which is W1-04's input, not this branch's; the branch's own S1 clause (c) over Q is a positivity filter that also excludes the RH-true L(s, χ₄) (PRICING §1(b)(v) line 46; III.16 rider, `BARRIER-ZOO.md` line 298). Against the M2 instance (digest §D(ii) 2, line 203: "any branch offering an S1 witness must show what input of ITS object DH violates"): the branch's object has no input of its own that DH violates — the one it has is borrowed from the square.
- **S2: 1** — On the rung the family {vol_{H^{(n)}}}_{n≥1} of §2.5 is Lorentzian for every n iff RH holds for C (Milne lines 100–102 with §2.5), an exact single-violation detector — but it is the square's, not a prime-variable object; the branch's built objects over Q see an off-line zero at height T only at degree ~T² (`reports[14].fit.S2`, the Chassé/Farmer ground the III.16 rider keeps, `BARRIER-ZOO.md` line 296). No prime-variable datum exists in the inventory (§3) to set against the M2 datum W_Z(f_{t,L}) (digest §D(ii) 2, line 203).
- **S3: 2** — On the rung the Lorentzian condition is an inertia condition n₊ ≤ 1 on a Gram matrix of intersection numbers (§2.5): a repeated on-line inverse root (|a_i| = q^{1/2}, a_i = a_j) keeps every bound |N_n − qⁿ − 1| ≤ 2g q^{n/2} and so keeps the property, while an off-line inverse root breaks the bound at some finite n (Milne lines 97–111) and destroys it — the S3 shape holds exactly there, on the square's entries, where II.4 does not bind (§5, II.4 row). Over Q the clause is untested because no object exists in the inventory (§3).
- **S4: 2** — The generator exists as mathematics and is a sanctioned class (`scripts/rh-grossmann-sweep.js` line 16: "combinatorial (Lorentzian polynomials)"; Brändén–Huh lines 795–799: for a volume polynomial "the one positive eigenvalue condition … is equivalent to the validity of the Hodge–Riemann relations on the space of divisor classes"); its only instantiation with RH content on the bottom rung is the Hodge index on C × C (§2, §3), i.e. the algebraic generator of W1-04 in Lorentzian dress — the same generator, not a new one — and on C × C the natural prime-variable candidate degenerates (§3.2, "I infer").
- **S5: 2** — Rodgers–Tao (III.6) is scope-cleared for a prime-side certificate (§5, III.6 row, re-derived); Chassé/Farmer bind the built wing only (PRICING §1(b)(i) line 38, verified against `reports[14].fit.S2`); III.1 is passed by the exact iff on the rung (§2.5); IV.18 does not bind (the certificate is an inertia condition, not a strip-positive first-order sum rule — §5, IV.18 row); IV.19 fixes the currency and kills nothing on the rung (§5, IV.19 row); what the branch does not survive over Q is its own clause (c) on the ladder's Dirichlet rung (PRICING §1(b)(v) line 46).

---

## 2. The rung (R-b), first half: is the Lorentzian polynomial with von Mangoldt coefficients the Hodge-index form of the square?

### 2.1 The definition at the page — nonnegativity is required (stop line (a) checked first)

`verify/bh-text.txt` line 269–270: P^d_n is "the open subset of polynomials all of whose coefficients are positive". Line 312–314 (Definition 2.1): L̊²_n = {f ∈ P²_n | H_f is nonsingular and has exactly one positive eigenvalue}; line 318: L̊^d_n = {f ∈ P^d_n | ∂_i f ∈ L̊^{d−1}_n for all i}; line 321–322: "The polynomials in L̊^d_n are called strictly Lorentzian, and the limits of strictly Lorentzian polynomials are called Lorentzian." Line 77–79: L²_n is "the closed subset of quadratic forms with nonnegative coefficients that have at most one positive eigenvalue, which is the closure of L̊²_n"; line 83–86: L^d_n = {f ∈ M^d_n | ∂_i f ∈ L^{d−1}_n}, M^d_n "the set of polynomials with nonnegative coefficients whose supports are M-convex"; line 1111 (Theorem 2.25): "The closure of L̊^d_n in H^d_n is L^d_n." So a Lorentzian polynomial has nonnegative coefficients in every one of the three equivalent descriptions (strict class inside P^d_n; closure; L^d_n inside M^d_n). PRICING §1(b)(iv) line 44 is confirmed at the page. **Stop line (a) does not fire.** For d = 2 — the degree of every polynomial in this report — a quadratic form f(w) = wᵀGw with G symmetric is Lorentzian iff G has nonnegative entries and at most one positive eigenvalue (line 77–79; the Hessian is 2G).

### 2.2 The square and its four classes, re-derived at Milne's page

Milne line 458–462: V = C₁ × C₂, C₁ ≔ C₁ × pt, C₂ ≔ pt × C₂, C₁·C₁ = 0 = C₂·C₂, C₁·C₂ = 1. Line 464: d₁ = D·C₁, d₂ = D·C₂. Line 505–506 (Example 1.7): the graph Γ_f of a nonconstant morphism f : C₁ → C₂ is a divisor with d₂ = 1 and d₁ = deg f; line 511: 2g₁ − 2 = (Γ_f)² + (2g₁ − 2)·1 + (2g₂ − 2)·deg f (adjunction); line 514, eq. (7): def(Γ_f) = 2g₂ deg f, with def(D) ≔ 2d₁d₂ − (D²) (line 483). Take C₁ = C₂ = C̄ (Milne line 517–518: C the curve over the algebraic closure k of k₀ = F_q, π the Frobenius endomorphism), genus g.

- Δ = Γ_id: d₁ = d₂ = 1, and eq. (7) with deg f = 1 gives def(Δ) = 2g, so **Δ² = 2 − 2g** (line 519: "def(Δ) = 2g").
- Γ ≔ Γ_π: d₂ = 1, d₁ = deg π = q, and eq. (7) gives def(Γ) = 2gq (line 519: "def(Γ_π) = 2gq"), so **Γ² = 2q − 2gq = 2q(1 − g)**.
- **Γ·Δ = N₁** (line 524: "(Δ·Γ_π) = number of points on C rational over k₀"; line 205: "(Γ_π·Δ) = |C₀(k₀)|").

Gram matrix G₀ on the ordered basis (C₁, C₂, Δ, Γ):

    G₀ = [ 0   1    1        q      ]
         [ 1   0    1        1      ]
         [ 1   1   2−2g      N₁     ]
         [ q   1    N₁     2q(1−g)  ]

Milne's Hodge index theorem (line 398–400, Theorem 1.2: (D·H) = 0 ⟹ (D·D) ≤ 0 for a hyperplane section H; Corollary 1.3, line 448: "The intersection form on N(V) has index 1") says the form has exactly one positive eigenvalue on the nondegenerate quotient N(V); restricted to the span of the four classes it therefore has at most one positive eigenvalue, and exactly one since (C₁ + C₂)² = 2 > 0 (line 472).

### 2.3 The two identities, re-derived (the launch note's instruction; the pricing's "I infer" at PRICING line 51)

**(i) N_n = (Γ_{π^n}·Δ).** Γ_π ∩ Δ = {(x, x) : π(x) = x}. A point x ∈ C(k) with π(x) = x has coordinates fixed by a ↦ a^q, i.e. lies in C₀(k₀); conversely every k₀-point is fixed. The intersection is transverse at each such point because the differential of π vanishes (d(a^q) = q a^{q−1} da = 0 in characteristic p), so T_{(x,x)}Γ_π = {(v, 0)} while T_{(x,x)}Δ = {(v, v)}, and these meet only in 0. Hence (Γ_π·Δ) = #C₀(k₀) = N₁ — Milne's line 205 and 524. Replacing k₀ by k_n = F_{qⁿ} replaces π by πⁿ (the q-power map iterated n times is the qⁿ-power map), with the same vanishing differential, so **(Γ_{πⁿ}·Δ) = |C(k_n)| = N_n** (Milne line 46–49 defines N_n this way). Milne's trace form of the same identity: line 203, (Γ_π·Δ) = 1 − Tr(π|H¹(C)) + q, from eq. (2) at line 196 with d₂ = 1, d₁ = q; and line 97, N_n = 1 + qⁿ − (a₁ⁿ + ⋯ + a_{2g}ⁿ).

**(ii) The von Mangoldt identity.** Milne line 56–60 defines Z(C, T) by d log Z(C, T)/dT = Σ_{n≥1} N_n T^{n−1}, equivalently log Z = Σ N_n Tⁿ/n (line 90–92), and line 61–64 gives Z(C, T) = Π_P (1 − T^{deg P})^{−1} over the closed points P of C. Taking log of the product and expanding, log Z = Σ_P Σ_{k≥1} T^{k·deg P}/k, so the coefficient of Tⁿ/n is **N_n = Σ_{P : deg P | n} deg P** — the sum over prime powers P^k of norm qⁿ of Λ(P^k) = deg P·log q, divided by log q. With T = q^{−s} (line 68: ζ(K, s) = Z(C, q^{−s})): −ζ′(K, s)/ζ(K, s) = log q · Σ_{n≥1} N_n q^{−ns}, so **Λ_C(qⁿ) = N_n log q ≥ 0**, and N_n is at once the intersection number (i) and the function field's von Mangoldt datum. Both halves are at Milne's page (lines 58–59, 63–64); nothing is recalled.

**Sign note on the pricing's wording.** PRICING line 51 and line 60 write "−Z′/Z = Σ N_n T^{n−1}". At Milne's line 58–59 the T-derivative identity carries no minus sign: Z′(T)/Z(T) = Σ N_n T^{n−1}. The minus sign belongs to the s-derivative, −(d/ds) log Z(q^{−s}) = log q · Σ N_n q^{−ns}, as derived above. The content the pricing infers (N_n is the von Mangoldt datum) is right; the displayed sign is the s-form's. Recorded, not load-bearing.

### 2.4 The nef translation Theorem 4.6 needs — which classes carry Δ and Γ_π, and the coefficients stay nonnegative (stop line (b) checked)

Brändén–Huh line 2318–2319: Y a d-dimensional irreducible projective variety over an algebraically closed field F; line 2335–2341: vol_H(w) = (w₁H₁ + ⋯ + w_nH_n)^d for Q-divisors H_i; line 2349–2350: D is nef if (D·C) ≥ 0 for every irreducible curve C; line 2352 (Theorem 4.6): "If H₁, …, H_n are nef divisors on Y, then vol_H(w) is a Lorentzian polynomial"; proof at lines 2381–2404, whose last step (line 2401–2402) is "the Hodge index theorem [Har77, Theorem V.1.9] shows that the displayed quadratic form has exactly one positive eigenvalue". Y = C̄ × C̄ over k = F̄_q is a smooth irreducible projective surface over an algebraically closed field (Milne line 517–518, and Aside 1.8 at line 527–528: "except for the last few lines, the proof is purely geometric and takes place over an algebraically closed field"), so Theorem 4.6 applies with d = 2 once nef classes are chosen.

**Δ and Γ are not nef for g ≥ 2.** Δ is an irreducible curve with Δ·Δ = 2 − 2g < 0, and Γ is an irreducible curve with Γ·Γ = 2q(1 − g) < 0 (§2.2), so each fails the nef test on itself (line 2349–2350). The translation is forced; this is what PRICING line 60 anticipates.

**C₁ and C₂ are nef:** for an irreducible curve E, E·C₁ ≥ 0 and E·C₂ ≥ 0 because C₁ and C₂ are fibers of the two projections and E is either a fiber (self-intersection 0, line 461) or meets each fiber properly in a nonnegative number of points (Brändén–Huh line 2324–2325 for the transverse case; distinct irreducible curves on a smooth surface meet properly with nonnegative local multiplicities).

**The translates.** Set

    H_Δ ≔ Δ + (g − 1)(C₁ + C₂),        H_Γ ≔ Γ + (g − 1)(C₁ + q·C₂).

Nef check for H_Δ, against every irreducible curve E: E = C₁-type fiber: H_Δ·C₁ = 1 + (g − 1) = g ≥ 0; E = C₂-type fiber: H_Δ·C₂ = g ≥ 0; E = Δ: H_Δ·Δ = (2 − 2g) + 2(g − 1) = 0 ≥ 0; any other irreducible E: E·Δ ≥ 0 (distinct irreducible curves), E·C₁ ≥ 0, E·C₂ ≥ 0, and the coefficients g − 1 ≥ 0, so H_Δ·E ≥ 0. Hence **H_Δ is nef** (for g ≥ 1; for g = 0, H_Δ = Δ ≡ C₁ + C₂, nef). Nef check for H_Γ: H_Γ·C₁ = q + q(g − 1) = qg ≥ 0; H_Γ·C₂ = 1 + (g − 1) = g ≥ 0; H_Γ·Γ = 2q(1 − g) + (g − 1)q + (g − 1)q = 0 ≥ 0; any other irreducible E: E·Γ ≥ 0, E·C₁ ≥ 0, E·C₂ ≥ 0 with nonnegative coefficients. Hence **H_Γ is nef**. (Any a, b ≥ 0 with a + b ≥ 2g − 2 for Δ, and aq + b ≥ 2q(g − 1) for Γ, works; the choice above puts both translates on the nef boundary, H_Δ·Δ = H_Γ·Γ = 0. The alternative a = b = 2g − 2 for both is also computed in Appendix A; the inertia below does not depend on the choice, by Sylvester's law.)

**The Gram matrix of the four nef classes H = (C₁, C₂, H_Δ, H_Γ)**, computed by bilinearity from G₀ (hand derivation; reproduced symbolically in Appendix A):

- H_Δ·C₁ = H_Δ·C₂ = g;  H_Δ² = (2 − 2g) + 4(g − 1) + 2(g − 1)² = 2g(g − 1);
- H_Γ·C₁ = qg;  H_Γ·C₂ = g;  H_Γ² = 2q(1 − g) + 2q(g − 1) + 2q(g − 1) + 2q(g − 1)² = 2qg(g − 1);
- H_Δ·H_Γ = N₁ + (g − 1) + q(g − 1) + q(g − 1) + (g − 1) + q(g − 1)² + (g − 1)² = **N₁ + (g² − 1)(q + 1)**.

    G_H = [  0     1        g              qg          ]
          [  1     0        g               g          ]
          [  g     g     2g(g−1)     N₁ + (g²−1)(q+1)  ]
          [ qg     g   N₁ + (g²−1)(q+1)   2qg(g−1)     ]

Every entry is ≥ 0 for g ≥ 1 (N₁ ≥ 0), and for g = 0 the entries are 0, 1, 0, 0, 2, 2q and N₁ − q − 1 = 0 (P¹ has q + 1 points), also ≥ 0. So the volume polynomial **vol_H(w) = wᵀG_H w has nonnegative coefficients** — as it must, each entry being nef·effective — and Theorem 4.6 asserts it is Lorentzian. **Stop line (b) does not fire:** the translation to nef classes with nonnegative coefficients exists and is displayed.

### 2.5 The Lorentzian property of vol_H, evaluated, is exactly |N₁ − q − 1| ≤ 2g√q — and the tower gives Weil's RH

Change basis from (C₁, C₂, Δ, Γ) to (C₁, C₂, Δ′, Γ′) with Δ′ ≔ Δ − C₁ − C₂ and Γ′ ≔ Γ − C₁ − q·C₂ (Milne line 473's vectors D − d₂C₁ − d₁C₂ for D = Δ, Γ). By bilinearity from G₀: Δ′·C₁ = 1 − 0 − 1 = 0, Δ′·C₂ = 1 − 1 − 0 = 0, Γ′·C₁ = q − 0 − q = 0, Γ′·C₂ = 1 − 1 − 0 = 0; Δ′² = (2 − 2g) − 2 − 2 + 2 = −2g; Γ′² = 2q(1 − g) − 2q − 2q + 2q = −2gq; Δ′·Γ′ = N₁ − 1 − q − q − 1 + q + 1 = **N₁ − q − 1** (Appendix A reproduces all seven numbers). So in this basis the form is block-diagonal:

    [ 0 1 ]   ⊕   [ −2g        N₁−q−1 ]
    [ 1 0 ]       [ N₁−q−1     −2gq   ]

The first block has eigenvalues +1, −1. Both bases (C₁, C₂, H_Δ, H_Γ) and (C₁, C₂, Δ′, Γ′) are obtained from (C₁, C₂, Δ, Γ) by unimodular triangular changes of basis, so by Sylvester's law of inertia n₊(G_H) = n₊(G₀) = 1 + n₊(block₂). Therefore

**vol_H is Lorentzian ⟺ n₊(G_H) ≤ 1 ⟺ the 2 × 2 block is negative semidefinite ⟺ (−2g)(−2gq) − (N₁ − q − 1)² ≥ 0 ⟺ |N₁ − q − 1| ≤ 2g·q^{1/2}**

(the diagonal entries −2g, −2gq are already ≤ 0; for g = 0 the block is zero and the statement is 0 ≤ 0). The right-hand side is Milne's line 521, and Milne's line 493–503 (Corollary 1.6 from def(mΔ + nΓ) ≥ 0 for all m, n) is the same 2 × 2 negative-semidefiniteness written out: def(D) = −(D − d₂C₁ − d₁C₂)² by expansion (line 483 with line 477). So the Lorentzian statement is **not weaker** than Castelnuovo–Severi on this span; it is Corollary 1.6 for the pair (Δ, Γ_π), which is where the RH content sits (Castelnuovo–Severi for Γ alone, Γ² ≤ 2q, is the trivial 2q(1 − g) ≤ 2q). Numerical instance (Appendix A): g = 2, q = 5, 2g√q = 8.944; N₁ ∈ {0, 6, 14} give n₊(G_H) = 1 (Lorentzian), N₁ ∈ {15, 20} give n₊ = 2 (not Lorentzian) — the flip sits exactly at the Weil bound.

**The tower.** Replace Γ_π by Γ_{πⁿ}: d₁ = deg πⁿ = qⁿ, def = 2gqⁿ (eq. (7)), Γ_{πⁿ}·Δ = N_n (§2.3(i)); the same computation with H^{(n)} ≔ (C₁, C₂, H_Δ, Γ_{πⁿ} + (g − 1)(C₁ + qⁿC₂)) gives: **vol_{H^{(n)}} is Lorentzian ⟺ |N_n − qⁿ − 1| ≤ 2g·q^{n/2}**. Milne line 98–102: RH for C implies this inequality for every n, and "conversely, if this inequality holds for all n, then the Riemann hypothesis holds for C" (footnote 1, lines 103–111: the power series Σ a_iⁿ zⁿ converges for |z| ≤ q^{−1/2}, so |a_i| ≤ q^{1/2}, and the functional equation gives equality). Hence

**{vol_{H^{(n)}}}_{n≥1} is Lorentzian for every n ⟺ Weil's RH for C.**

This is a family of quadratic (d = 2) Lorentzian polynomials in four variables on one surface C̄ × C̄, whose n-dependent coefficient is the von Mangoldt datum N_n = Σ_{deg P | n} deg P (§2.3(ii)) and whose other coefficients are g, q, qⁿ and their polynomials — the shape of the interface's clause (a) ("P_N is Lorentzian for every N iff …", `reports[14].first_interface`) realized on the bottom rung, with the variables indexed by four divisor classes of the square and not by primes. The genus enters the certificate through Δ² = 2 − 2g (adjunction, Milne line 508–511), i.e. through 2g = deg P(C, T) (Milne line 75), the count of inverse roots — the rationality datum III.20 names ("finitely many eigenvalues of fixed weight", `BARRIER-ZOO.md` line 326).

### 2.6 What the first half returns

The object PRICING §1(c) line 60 asks for exists, is displayed (§2.4), is a Brändén–Huh Lorentzian polynomial by Theorem 4.6 (line 2352), has coefficients that are point counts and the integers g, q (§2.4), and its Lorentzian property, evaluated on the Frobenius graph, is |N₁ − q − 1| ≤ 2g√q, and on the tower is Weil's RH (§2.5). It is the volume polynomial of nef classes on the square C̄ × C̄ — the Hodge-index form of the square in Lorentzian dress — and not an object in variables indexed by closed points. **First half: YES, by the square.**

---

## 3. The rung (R-b), second half: is any prime-variable Lorentzian object (variables x_P, P a closed point, or x_p over Q) exhibited in the two sources, `reports[14]`, or the record?

### 3.1 Inventory check (bounded to the named documents; labeled in §7 as internal — "the branch does not contain the object" — and never weighed as a literature fact)

- **Brändén–Huh (`verify/bh-text.txt`, 3 213 lines):** a case-insensitive search for "zeta", "Frobenius", "finite field", "Riemann hyp", "L-function", "prime number", "von Mangoldt", "closed point" returns one line, 1646 ("over the finite fields F3 and F4 [COSW04]" — a matroid representability remark), and nothing else. The Lorentzian objects the paper exhibits are volume polynomials of convex bodies and projective varieties (line 74–76), homogeneous stable polynomials (line 332–336), Potts-model partition functions (line 2432–2440), matroid basis generating polynomials (line 2370–2379), with variables indexed by divisors, vectors, edges or ground-set elements. No polynomial in the text has variables indexed by the closed points of a curve or by primes, and none has an L-function or a point count among its coefficients.
- **Milne (`verify/milne-text.txt`, 3 546 lines):** the word "Lorentzian" does not occur (search, 0 hits). The Hodge-index / Castelnuovo–Severi material is at lines 398–525; the Rosati-positivity form Tr(α∘α†) > 0 at line 1116–1120 is a form on End(A), not a polynomial in prime-indexed variables.
- **`results/grossmann-sweep.json` `reports[14]`:** `key_objects[1]`: Lorentzian polynomials are "the only S4-sanctioned combinatorial positivity generator — currently with NO zeta instantiation"; `first_interface` is a theorem *statement* ("the statement whose proof would resurrect this branch") specifying P_N in variables x_p, not an object; `live_entry_points[1]`: Cid-Ruiz's object "is Segre-class generating series, not Riemann zeta". The report's absence sentences (`fit.S1` "zero published attempts"; `prior_attacks[8]` "NO RH attack has ever been mounted"; `verified_online[4]`) are struck as evidence per V.5 and the III.16 rider and are not used here.
- **The record:** PRICING §1(c) line 61 reads the same inventory and finds none; the III.16 rider (`BARRIER-ZOO.md` line 296) states the bridge is "an OPEN internal question, not a closed corner"; III.20's rider (line 331) records that the repair's coefficients come from a doubled object.

**Result: no prime-variable Lorentzian object with the iff is exhibited in the inventory named by the rung.** Stop line (c) — "a published prime-variable Lorentzian object with the iff on the function-field rung is found" — **does not fire**, because none was found in the inventory the rung names; this is a statement about what those documents contain, and it is the whole of what the second half asks.

### 3.2 One internal observation beyond the inventory (`I infer`; `[novelty: single-check]`)

On the square itself, closed points of C carry no independent divisor classes: for a closed point P of degree d, the fiber x × C̄ over any of its d geometric points is numerically equivalent to C₂ (all fibers of a projection are algebraically equivalent; Milne line 461: C₂·C₂ = 0 and line 533–534 defines valence zero by exactly these classes). So a volume polynomial "in variables x_P" formed from point-fibers on C̄ × C̄, vol(Σ_P x_P·(P × C̄)) = (Σ_P x_P deg P)²·C₂² = 0, is identically zero: on the square the prime side enters through one number per n, the coefficient N_n = Γ_{πⁿ}·Δ, and never through variables. A prime-variable Lorentzian object with RH content would therefore have to live off the square (a generating polynomial over closed points in the style of Brändén–Huh §4.3, with an inertia condition of its own); none is exhibited (§3.1), and the rung does not ask me to construct one (PRICING line 61: "The scout is not asked to construct one"). This observation is internal and is offered as the reason the square's instantiation is the only one *on the square*; it says nothing about objects off the square.

---

## 4. The (R-b) return and its refutation-shaped close

**Return: YES-by-the-square** (PRICING §1(c) line 64 and SCOUT-BRIEF line 10). The Lorentzian polynomial whose coefficients are von Mangoldt data of C is vol_H for the nef classes H = (C₁, C₂, H_Δ, H_Γ) on C̄ × C̄ (§2.4); its Lorentzian property is Brändén–Huh Theorem 4.6 applied to the square, i.e. the Hodge index theorem, and evaluated on the Frobenius graph it is |N₁ − q − 1| ≤ 2g√q, on the tower Weil's RH (§2.5). No prime-variable object is exhibited in the inventory (§3.1). Consequence, in PRICING's words (line 64): the dead-end grade on the unbuilt INDEPENDENT prime-side sector is restored on internal grounds in the precise form "the Lorentzian branch contains no instantiation with RH content other than the one it shares with W1-04", and the branch is re-filed as an **instrument** (the Lorentzian / volume-polynomial vocabulary for the target inequality of the geometric-substrate direction, III.20 items 2–3: external generator, closed output condition). Not grossmann-candidate: its substrate is the missing square.

**Refutation-shaped close (10(c)), verbatim from PRICING §1(c) line 64, which is the close attached to this return:**

*"A multiplicative-Lorentzian bridge with prime-side coefficients cannot be built independently of a doubled object, because on the only rung where RH is a theorem the Lorentzian polynomial with von Mangoldt coefficients is the Hodge-index form of C × C (Brändén–Huh Thm 4.6 + Castelnuovo–Severi), and on the Dirichlet rung unsquared Λ-data violate the definition's nonnegativity (Λ_{χ₄}(3) < 0)."*

**Sharpened form this report adds, on its own derivation (§2.5; `[novelty: single-check]`):** *On C × C the Lorentzian property of the volume polynomial of the four nef classes (C × pt, pt × C, Δ + (g−1)(C × pt + pt × C), Γ_π + (g−1)(C × pt + q·pt × C)) is exactly the inequality |N₁ − q − 1| ≤ 2g√q, and the family over Γ_{πⁿ} is Lorentzian for every n exactly when Weil's RH holds for C — so the Lorentzian class contains Weil's certificate, as the square's volume polynomial, with the genus entering as the self-intersection of the diagonal.*

---

## 5. Zoo gate (PRICING §1(d) re-run in my own words, plus the IV.18 and IV.19 rows the launch note requires)

| Entry | What it returns for the (R-b) rung and for the interface — my reading at the page |
|---|---|
| **I.1** DH / Epstein filter (`BARRIER-ZOO.md` 45–52) | On the rung: not applicable — there is no DH curve and no DH square; the rung is the RH-true calibration. For the interface over Q: EXECUTABLE TEST (c) (line 50) is passable at the axiom level — the definition consumes coefficient nonnegativity (§2.1), and on the record Λ_DH(3) = −0.3120927285, Λ_DH(4) = −1.4422319646, Λ_DH(12) = −0.7628774720 with support {p^k : p ≡ ±1 (mod 5)} ∪ {n : all prime factors ≡ ±2 (mod 5)}, 8 562 nonzero coefficients at L = 10 (digest §D(ii) 5(b)–(c), line 206) — but over-broadly, since Λ_{χ₄}(3) = −log 3 < 0 for the RH-true L(s, χ₄) (PRICING line 46; III.16 rider line 298). Returns: PASS with the over-breadth flagged; the Dirichlet rung is not runnable with unsquared data; the DH datum is used here only as the record fact behind note R-a (launch note item 2). |
| **III.16** (288–298) | EXECUTABLE TEST (line 292): "Does the brief's hyperbolicity input hold for an RH-false extended-Selberg member?" For the rung's object the input is the Hodge index on C × C, which has no extended-Selberg member at all; for the interface's prime-side input (Λ ≥ 0 + multiplicativity) DH fails it at the axiom level (I.1 row), so the input is not S1-empty and the test returns "bridge must be exhibited" — which the rung answers: the only bridge exhibited on the bottom rung is the square's (§2, §3). The rider's SUSPENSION (line 296) is resolved by this return in the direction the STATUS addendum (line 295) leaves open: the grade on the unbuilt independent sector is restored on internal grounds (§4), and the built-object kills (Jensen–Pólya/Turán, Lorentzian dressings of Ξ's Taylor coefficients, heat-flow/preserver) stand untouched. |
| **III.6** Rodgers–Tao (203–210) | Re-derived against the interface: the STATEMENT and EXECUTABLE TEST (line 205, 207) act in the de Bruijn–Newman flow variable t on Ξ; the rung's certificate is a Gram matrix of intersection numbers (§2.4) with no flow variable, and the interface's certificate over Q has coefficients that are finite Λ-sums, which H_t does not carry for t ≠ 0 (the rider at line 210, from PRICING §1(b)(ii), which I confirm by the same reading: nothing in the flow touches a_n). Returns: no bind on a prime-side certificate; the general zero-margin remark is in the flow variable, not in coefficient space; note R-c recorded, no object produced. |
| **III.1** o(N)-blindness (163–169) | The rung's statement is an exact iff (§2.5: Lorentzian for every n ⟺ RH for C, Milne 100–102), not a density statement; the interface's clause (a) is likewise an iff. Returns: passes on the rung; over Q the pair must not accept "Lorentzian for d ≥ N(d)" (the GORZ shape III.16 kills) — no such object is offered. |
| **II.4** lemmaR_tight (136–149) | The Lorentzian condition is the inertia invariant n₊ ≤ 1 (§2.1), which is on II.4's list {tr, ‖·‖²_F, atom norms, n₊} (line 138). II.4 binds when the matrix entries are two-moment Weil-form data; on the rung the entries are intersection numbers — g, q, qg, N₁ + (g² − 1)(q + 1), 2g(g − 1), 2qg(g − 1) (§2.4) — not Weil-form moments, so II.4 does not bind there; the rung's S3 shape (§1, S3) holds on those entries. Over Q the S3 clause (b) is untested (no object), and any separation claim would owe II.4's depth-uniformity check (line 141) and the rider's first-order regime note (line 149). |
| **III.20** S6 doubled-object rule (324–331) | Conformance audit (line 328), four items, on the rung: doubled object = C̄ × C̄; external generator = Hodge index (Milne 398–400; Brändén–Huh 2401–2402); closed output = |N_n − qⁿ − 1| ≤ 2g q^{n/2} (§2.5); tower/rationality = Γ_{πⁿ}·Δ = N_n with 2g = deg P(C, T) entering as Δ² = 2 − 2g (§2.3, §2.5). Conformant on the rung. Over Q item 1 is the missing square, and the rider (line 331) already records that the interface's repair takes its coefficients from a doubled object — which §2.4 exhibits from the geometric side: the nonnegative coefficients are nef·effective on the square. Returns: conformant on the rung; over Q returned until a doubled object is named. |
| **IV.1** Weil-positivity-in-disguise (345–351) | On the rung the certificate is the Hodge index on span{C₁, C₂, Δ, Γ_π}, of which Weil positivity (Milne 1116–1120, Tr(α∘α†) > 0) is a consequence — the generator itself, not a reparametrized restriction of explicit-formula data; the diagonal entries −2g, −2gq of the block in §2.5 are adjunction data, not prime data. Returns: not in disguise on the rung; the EXECUTABLE TEST (line 349) is for prime-computable observables over Q, and there is no prime-variable object to run it on (§3.1). |
| **IV.18** Sector-I confinement (484–492) — NEW row | KILLS (line 487): "any brief claiming that a strip-positive (cone / positivity-class / dlVP-type) first-order certificate, at any bandwidth, yields a zero-free point at a height and depth where the theorem's density hypothesis holds"; BINDS (line 490): "cone / positivity-class first-order certificates"; and "Does NOT bind: Sector II signed separations". My reading of the branch against it: (i) on the rung the certificate is n₊ ≤ 1 of a Gram matrix of intersection numbers, with no test function and no sum rule — outside IV.18's class. (ii) Over Q, the interface's clause (a) would claim "no off-line zero up to T(N)" from "P_N Lorentzian"; its coefficients are nonnegative first-order Λ-sums (Definition 2.1 consumes Λ ≥ 0 exactly there, PRICING line 44), but the certificate's condition is an inertia condition on the Hessian: unwound for d = 2, it says zᵀGz ≤ 0 for every z with zᵀGw = 0, w in the positive orthant (`verify/bh-text.txt` 781–785, the proof of Theorem 2.16). Each such zᵀGz is a first-order Λ-sum with a SIGNED test (the quadratic form in z), i.e. a Sector-II signed separation in IV.18's own reading (line 487: "the interior of the strip belongs to Sector II (signed tests) or to nothing yet"), not a strip-positive cone element (w ≥ 0, ŵ ≥ 0). So **any zero-free claim the branch would make is not of the cone class IV.18 binds; the different invariant is the inertia n₊ of a Hessian of Λ-sums, equivalently a family of signed first-order sum rules indexed by a hyperplane** (`I infer`; `[novelty: single-check]`). IV.18 returns nothing on the rung and does not bind the interface's certificate class; it would bind only a reading of clause (a) that reduced the inertia condition to a single positive-test budget inequality B = Z + P, which the definition does not do. What IV.18 does say to the branch: a nonnegative-coefficient rule alone (the cone's ingredient) reaches only a dlVP layer; the branch's content, if any, is in the signed quadratic-form condition, which is exactly what the interface leaves unspecified (§0 item 5). |
| **IV.19** Kronecker sharpness (517–523) — NEW row | KILLS (line 520): certifying the silence or firing of a first-order datum at a specific height by a t-uniform prime-side estimate; pricing a prime-side evaluation by the theorem's L* rather than by the term count; the cost currency is the term count e^{L} (line 519). My reading: (i) on the rung, the Lorentzian property is decided by an exact evaluation of finitely many integers (N₁ by counting points; g, q given), never by an estimate — the evaluation route, with term count = the number of degree-1 closed points; IV.19 kills nothing there. (ii) Over Q, the interface's clause (a) "P_N is Lorentzian for every N iff ζ has no off-line zero up to height T(N)" has coefficients that are FINITE nonnegative Λ-sums (weighted sums over prime powers p^k ≤ X(N)); their values are evaluations with term count ≍ X(N), and the inertia test is on deg P_N ≤ π(X(N)) variables. **Clause (a) would never be certified by a height-uniform prime-side estimate**: whether the coefficients carry a height parameter (the interface does not say — a free parameter, PRICING §1(c) (R-a), line 55) or not, the certificate of "P_N Lorentzian" is the evaluation of its coefficients plus an exact inertia computation, and any pricing of clause (a) by "the Λ-sums are bounded uniformly in t" is returned by IV.19's KILLS. The currency for the interface is the term count of its coefficient sums; if the coefficients were ever made t-dependent (cos(t log n) weights, as in IV.19's P_X(g_t)), Theorem (E) (line 519) says their supremum over any window of length ≥ H₀ is the ℓ¹ norm, so no uniform bound below that norm exists. IV.19 returns nothing on the rung and fixes the currency over Q. |
| **V.5** (557–567) — process | Every verdict sentence is labeled in §7; the report's null results (§3.1) are inventory statements about named documents and are labeled internal ("the branch does not contain the object", line 560), never weighed as literature facts; `reports[14]`'s absence sentences are struck as evidence (§3.1). |

---

## 6. Remaining schema fields

- **key_objects:** (1) Brändén–Huh Definition 2.1 and the closed class L²_n = {quadratic forms with nonnegative coefficients and at most one positive eigenvalue} (`verify/bh-text.txt` 77–79, 312–322). (2) Theorem 4.6, volume polynomials of nef divisors are Lorentzian (line 2352; proof 2381–2404, last step the Hodge index theorem). (3) The four nef classes on C̄ × C̄: C₁ = C × pt, C₂ = pt × C, H_Δ = Δ + (g − 1)(C₁ + C₂), H_Γ = Γ_π + (g − 1)(C₁ + qC₂), with Gram matrix G_H (§2.4) and the block form of §2.5. (4) The identities N_n = (Γ_{πⁿ}·Δ) (Milne 205, 524; §2.3(i)) and Z′/Z = Σ N_n T^{n−1}, N_n = Σ_{deg P | n} deg P (Milne 58–64; §2.3(ii)). (5) Milne Theorem 1.5 / Corollary 1.6 (466–503) and the RH-for-curves finish (516–525), with lines 98–111 for the "all n" equivalence. (6) The Hodge–Riemann gloss, Brändén–Huh 795–799, and Theorem 2.16 (801–804), the one-positive-eigenvalue statement on the positive orthant.
- **prior_attacks:** inherited from `reports[14].prior_attacks[0–8]` for the built wing (Jensen–Pólya; GORZ; Farmer's critique; Rodgers–Tao/Dobner; Borcea–Brändén), each of whose deaths is internal (dispersal, extended-Selberg genericity, zero margin) and stands per the III.16 rider (line 296); the two absence-shaped items (`prior_attacks[7]` "arXiv search … returns zero papers"; `prior_attacks[8]` "Not died — never born") are struck as evidence. For the prime-side sector there is no prior attack on record to cite; this report's rung is the first reading of it and is not an attack.
- **live_entry_points:** (1) Brändén–Huh Theorem 4.6 on C̄ × C̄ (this report, §2.4–§2.5) — the Lorentzian formulation of Castelnuovo-on-the-square, usable by C3-r as closed-output vocabulary (III.20 item 3). (2) `reports[14].live_entry_points[1]` (Cid-Ruiz, arXiv:2507.06424; the pricing's `verify/abs-2507.06424.html`): a Segre-class generating series, the measured extent of the gap — not read at the page this session. (3) Brändén–Huh Question 4.9 (line 2412–2420): which Lorentzian polynomials are volume polynomials — relevant if anyone ever asks whether a prime-variable Lorentzian object could be realized as a volume polynomial of some variety (the paper answers only n ≤ 3, lines 2422–2430).
- **first_interface (unchanged in shape; sharpened by the rung):** the statement of `reports[14].first_interface` stands as the referee-evaluable target for an independent prime-side sector, with two record facts now attached: (i) its clause (c) as written fails the ladder's Dirichlet rung (Λ_{χ₄}(3) < 0; PRICING §4(iii) 1, line 263), so any P_N must take its coefficients from a doubled object; (ii) on the bottom rung the object satisfying clause (a)'s shape is vol_{H^{(n)}} on C̄ × C̄ (§2.5), in four class-indexed variables, so the target is now: *exhibit P_N in prime-indexed variables whose Lorentzian property on the function-field rung reproduces §2.5 without passing through C × C.* The rung reports that nothing in the inventory does this (§3).
- **access_failures:** none — both sources are on disk in full text; `BARRIER-ZOO.md`, `reports[14]` and the digest were read at the lines cited. Not read at the page this session: Hartshorne V.1.9 (cited by Brändén–Huh line 2401 and by Milne's Theorem 1.2 as the same theorem; not needed — Milne's proof at 398–429 is on disk), the Cid-Ruiz abstract (`verify/abs-2507.06424.html`, cited through `reports[14]` and PRICING line 83 only).
- **verified_online:** none — no web access was used in this report.
- **recalled_unverified:** (1) "Distinct irreducible curves on a smooth projective surface meet with nonnegative local intersection multiplicities" — used in §2.4 for the nef checks; the transverse case is Brändén–Huh line 2324–2325, the general case is textbook (Hartshorne V.1.4) and is not at a cited line on disk. (2) "Fibers of a projection C̄ × C̄ → C̄ over different points are algebraically, hence numerically, equivalent" — used in §3.2; consistent with Milne line 533–534 (valence zero) but not stated there as such. (3) Sylvester's law of inertia (used in §2.5 for the basis change) — standard linear algebra, not at a cited line. (4) "The differential of the q-power Frobenius vanishes" (§2.3(i)) — standard; Milne asserts the resulting identity at line 205 and 524 without this step. None of the four is load-bearing for the return: §2.5's equivalence is a finite computation on G₀ (Appendix A), and G₀'s entries are Milne's lines 461–462, 505–514, 519, 524.

---

## 7. refinement_compliance — every sentence of the verdict, labeled internal / absence

The verdict as I state it, sentence by sentence:

1. "The branch is re-filed as an instrument: the Lorentzian / volume-polynomial vocabulary for the target inequality of the geometric-substrate direction." — **internal** (a grading consequence of sentences 2–5, per PRICING line 64).
2. "On the only rung where RH is a theorem, the Lorentzian polynomial whose coefficients are von Mangoldt data of C is the volume polynomial of four nef classes on C̄ × C̄, and its Lorentzian property is Brändén–Huh Theorem 4.6 applied to the square, i.e. the Hodge index theorem." — **internal** (§2.4; Brändén–Huh 2352, 2401–2402; Milne 398–400).
3. "Evaluated on the Frobenius graph that Lorentzian property is exactly |N₁ − q − 1| ≤ 2g√q, and over the tower Γ_{πⁿ} it is exactly Weil's RH for C." — **internal** (§2.5; Milne 100–111, 521; Appendix A).
4. "The two sources, `reports[14]` and the record exhibit no Lorentzian polynomial in variables indexed by closed points or primes whose Lorentzian property carries the iff." — **internal** (an inventory statement about four named documents: "the branch does not contain the object", V.5 line 560; §3.1). It is NOT a statement about the literature and is not weighed as one: it answers the rung's second half, which asks only about this inventory (PRICING line 61).
5. "On the square itself, variables indexed by closed points collapse numerically to the two fiber classes, so the prime side enters the square's certificate only through the coefficient N_n." — **internal** (§3.2; `I infer`, single-check).
6. "The dead-end grade on the unbuilt INDEPENDENT prime-side sector is restored on internal grounds in the form 'the Lorentzian branch contains no instantiation with RH content other than the one it shares with W1-04'." — **internal** (sentences 2–5; PRICING line 64). The word "no instantiation" here quantifies over the rung's inventory and the square (sentences 4–5), not over publications.
7. "The interface as written cannot run the ladder's Dirichlet rung with unsquared Λ-data, because Lorentzian polynomials have nonnegative coefficients by definition and Λ_{χ₄}(3) = −log 3 < 0." — **internal** (§2.1; PRICING line 46 and §4(iii) 1, line 263; `results/c3-r/m0-axiom-note.md` §6.3 as cited there).
8. "The built objects of the branch stay dead on the internal ground the III.16 rider keeps (dispersal, extended-Selberg genericity, zero margin)." — **internal** (`BARRIER-ZOO.md` line 296; `reports[14].fit.S1–S2`, the internal halves).

No sentence of the verdict is an absence sentence. The three absence-shaped strings encountered in the inputs (`reports[14].fit.S1` "zero published attempts", `prior_attacks[8]` "never born", `verified_online[4]` "no multiplicative coupling … has ever been attempted") are quoted only to record that they were struck (§3.1, §6 prior_attacks) and carry no weight in any score or sentence above.

---

## 8. "Stop and report when" lines (PRICING §4(i), line 248) — status

- **(a)** "Brändén–Huh Definition 2.1 / the M^d_n definition (lines 78–86, 312–330) is found NOT to require nonnegative coefficients" — **did not fire**: nonnegativity is required in all three descriptions of the class (§2.1: lines 77–79, 85, 269–270, 312–314, 1111).
- **(b)** "the Hodge-index form on span{C × pt, pt × C, Δ, Γ_π} cannot be translated to nef classes with nonnegative coefficients so that Theorem 4.6 applies" — **did not fire**: the translation H_Δ = Δ + (g − 1)(C₁ + C₂), H_Γ = Γ_π + (g − 1)(C₁ + qC₂) is nef and its Gram matrix has nonnegative entries (§2.4).
- **(c)** "a published prime-variable Lorentzian object with the iff on the function-field rung is found (V.2 pre-emption)" — **did not fire**: none is exhibited in the inventory the rung names (§3.1).

No stop line fired; the report runs to the return.

---

## 9. Honesty note (standing order 5)

- **Read at the page:** every line cited above, in the two extracted texts, the zoo, the sweep JSON, the digest, the pricing, the brief, the launch note, and the sweep script's spec and schema lines.
- **Computed:** Appendix A (sympy 4 × 4 symbolic Gram matrices, the orthogonal basis, the block determinant, the alternative translate; numpy eigenvalues at g = 2, q = 5 for N₁ ∈ {0, 6, 14, 15, 20}). Runtime under two seconds; output reproduced verbatim in the appendix. The computation confirms the hand derivation of §2.4–§2.5 and decides nothing the reading does not.
- **Inferred (marked "I infer" where they occur):** §3.2 (closed-point variables collapse on the square); the IV.18 row's reading of the inertia condition as a family of signed first-order tests (Sector II); the IV.19 row's reading of clause (a)'s certificate as an evaluation. Each is `[novelty: single-check]` and is offered to the adjudicator, not asserted as a record fact.
- **Deviations from the pricing, recorded:** (1) the sign in "−Z′/Z = Σ N_n T^{n−1}" (PRICING lines 51, 60) is the s-form's; Milne's T-form at line 58–59 has no minus sign (§2.3). (2) The pricing's zoo table (line 71–79) predates IV.18 and IV.19; both rows are added (§5), per the launch note. (3) The pricing's inference at line 51 ("the intersection form … has Lorentzian signature … and N_n is the function field's von Mangoldt datum") is verified, with the one refinement that the raw form on (C₁, C₂, Δ, Γ_π) is NOT itself in L²_n for g ≥ 2 (its coefficients 2 − 2g and 2q(1 − g) are negative); the Lorentzian object is the nef-translated volume polynomial, whose inertia is the same by Sylvester (§2.4–§2.5).
- **Recalled, never load-bearing:** the four items of `recalled_unverified` (§6).
- **Novelty, single-check:** §2.5's exact-equivalence computation as a statement about Lorentzian polynomials (the underlying Castelnuovo–Severi content is Milne's, and Brändén–Huh's Theorem 4.6 is the general statement; the specific four-class form and its equivalence to the Weil bound are this report's), §3.2, and the two new zoo rows' readings.
- **Files touched:** this file and my own dated block in `results/grossmann-rescout-s22/pair1-lorentzian/SHARED.md`. Nothing else was modified; nothing was committed.
- **Blindness:** `scout-O.md` (if it exists), every `SHARED.md` block but my own, and any `adjudication.md` were not opened. A directory listing at start showed only `LAUNCH-NOTE.md` in the pair folder; a listing at the end (16:46 IST) showed `scout-O.md` and `SHARED.md` had appeared meanwhile, and neither was opened — my block was appended to `SHARED.md` with a shell append, without reading the file.

---

## Appendix A — the verification script and its output (reproduced verbatim so that this file is the whole deliverable)

Script (`python3`, sympy + numpy; run 2026-09-24 in the session scratchpad):

```python
# Scout F (pair 1, W1-14): nef translation of span{C1, C2, Delta, Gamma_pi} on C x C and the inertia check.
import sympy as sp
g, q, N1 = sp.symbols('g q N1')
# Gram of (C1, C2, Delta, Gamma): Milne lines 461-462 (C1^2=C2^2=0, C1.C2=1), Ex. 1.7 (d2=1, d1=deg f),
# eq. (7) def(Gamma_f)=2 g2 deg f => Delta^2 = 2-2g, Gamma^2 = 2q(1-g); Delta.Gamma = N1 (line 524).
G0 = sp.Matrix([[0,1,1,q],[1,0,1,1],[1,1,2-2*g,N1],[q,1,N1,2*q*(1-g)]])
# nef translates: H_D = Delta + (g-1)(C1+C2); H_G = Gamma + (g-1)(C1 + q C2)
T = sp.Matrix([[1,0,0,0],[0,1,0,0],[g-1,g-1,1,0],[g-1,q*(g-1),0,1]])  # rows = new basis in old coords
GH = sp.simplify(T*G0*T.T)
print("Gram on (C1, C2, H_Delta, H_Gamma):"); sp.pprint(GH)
# nef checks: H_D . Delta, H_D . C1, H_D . C2, H_G . Gamma, H_G . C1, H_G . C2
old = {'C1':sp.Matrix([1,0,0,0]),'C2':sp.Matrix([0,1,0,0]),'D':sp.Matrix([0,0,1,0]),'Gm':sp.Matrix([0,0,0,1])}
HD = T.row(2).T; HG = T.row(3).T
for name,v in old.items():
    print(f"H_Delta . {name} =", sp.expand((HD.T*G0*v)[0]), " | H_Gamma .", name, "=", sp.expand((HG.T*G0*v)[0]))
# orthogonal basis: Delta' = Delta - C1 - C2, Gamma' = Gamma - C1 - q C2
Dp = sp.Matrix([-1,-1,1,0]); Gp = sp.Matrix([-1,-q,0,1])
for name,v in [('C1',old['C1']),('C2',old['C2'])]:
    print(f"Delta'.{name} =", sp.expand((Dp.T*G0*v)[0]), f" Gamma'.{name} =", sp.expand((Gp.T*G0*v)[0]))
print("Delta'^2 =", sp.expand((Dp.T*G0*Dp)[0]), " Gamma'^2 =", sp.expand((Gp.T*G0*Gp)[0]), " Delta'.Gamma' =", sp.expand((Dp.T*G0*Gp)[0]))
# det of the 2x2 block
blk = sp.Matrix([[(Dp.T*G0*Dp)[0],(Dp.T*G0*Gp)[0]],[(Dp.T*G0*Gp)[0],(Gp.T*G0*Gp)[0]]])
print("2x2 block det =", sp.factor(blk.det()))
# characteristic polynomial of GH factors? and numeric inertia at g=2, q=5 over N1
import numpy as np
for n1 in [0, 6, 14, 15, 20]:
    M = np.array(GH.subs({g:2,q:5,N1:n1}).tolist(), dtype=float)
    ev = np.linalg.eigvalsh(M)
    print(f"g=2,q=5,N1={n1}: |N1-q-1|={abs(n1-6)} vs 2g sqrt q={4*5**0.5:.3f}; eigenvalues={np.round(ev,4)}; n+={int((ev>1e-9).sum())}; min entry={M.min()}")
# also a = b = 2g-2 alternative (both translates), to show choice does not matter for inertia
T2 = sp.Matrix([[1,0,0,0],[0,1,0,0],[2*g-2,2*g-2,1,0],[2*g-2,2*g-2,0,1]])
GH2 = sp.simplify(T2*G0*T2.T); print("Alt translate a=b=2g-2 Gram:"); sp.pprint(GH2)
```

Output:

```
Gram on (C1, C2, H_Delta, H_Gamma):
⎡ 0   1            g                      g⋅q          ⎤
⎢                                                      ⎥
⎢ 1   0            g                       g           ⎥
⎢                                                      ⎥
⎢                                      2      2        ⎥
⎢ g   g       2⋅g⋅(g - 1)        N₁ + g ⋅q + g  - q - 1⎥
⎢                                                      ⎥
⎢              2      2                                ⎥
⎣g⋅q  g  N₁ + g ⋅q + g  - q - 1      2⋅g⋅q⋅(g - 1)     ⎦
H_Delta . C1 = g  | H_Gamma . C1 = g*q
H_Delta . C2 = g  | H_Gamma . C2 = g
H_Delta . D = 0  | H_Gamma . D = N1 + g*q + g - q - 1
H_Delta . Gm = N1 + g*q + g - q - 1  | H_Gamma . Gm = 0
Delta'.C1 = 0  Gamma'.C1 = 0
Delta'.C2 = 0  Gamma'.C2 = 0
Delta'^2 = -2*g  Gamma'^2 = -2*g*q  Delta'.Gamma' = N1 - q - 1
2x2 block det = -N1**2 + 2*N1*q + 2*N1 + 4*g**2*q - q**2 - 2*q - 1
g=2,q=5,N1=0: |N1-q-1|=6 vs 2g sqrt q=8.944; eigenvalues=[-9.6604 -0.7479 -0.1761 34.5845]; n+=1; min entry=0.0
g=2,q=5,N1=6: |N1-q-1|=0 vs 2g sqrt q=8.944; eigenvalues=[-14.6934  -0.8635  -0.1588  39.7157]; n+=1; min entry=0.0
g=2,q=5,N1=14: |N1-q-1|=8 vs 2g sqrt q=8.944; eigenvalues=[-2.20046e+01 -9.35400e-01 -1.66000e-02  4.69566e+01]; n+=1; min entry=0.0
g=2,q=5,N1=15: |N1-q-1|=9 vs 2g sqrt q=8.944; eigenvalues=[-2.29431e+01 -9.40400e-01  1.00000e-03  4.78825e+01]; n+=2; min entry=0.0
g=2,q=5,N1=20: |N1-q-1|=14 vs 2g sqrt q=8.944; eigenvalues=[-27.6851  -0.9587   0.0832  52.5606]; n+=2; min entry=0.0
Alt translate a=b=2g-2 Gram:
⎡     0          1                  2⋅g - 1                           2⋅g + q  ↪
⎢                                                                              ↪
⎢     1          0                  2⋅g - 1                             2⋅g -  ↪
⎢                                                                              ↪
⎢                                  2                               2           ↪
⎢  2⋅g - 1    2⋅g - 1           8⋅g  - 10⋅g + 2            N₁ + 8⋅g  + 2⋅g⋅q - ↪
⎢                                                                              ↪
⎢                              2                                2              ↪
⎣2⋅g + q - 2  2⋅g - 1  N₁ + 8⋅g  + 2⋅g⋅q - 10⋅g - 2⋅q + 2    8⋅g  + 2⋅g⋅q - 12 ↪

↪ - 2            ⎤
↪                ⎥
↪ 1              ⎥
↪                ⎥
↪                ⎥
↪  10⋅g - 2⋅q + 2⎥
↪                ⎥
↪                ⎥
↪ ⋅g - 2⋅q + 4   ⎦
```

(The alternative-translate matrix prints wrapped by sympy's pretty-printer; its entries are 2g − 1, 2g + q − 2, 8g² − 10g + 2, N₁ + 8g² + 2gq − 10g − 2q + 2, 8g² + 2gq − 12g − 2q + 4, all nonnegative for g ≥ 1 and q ≥ 2, and its inertia equals G_H's by Sylvester's law.)

*End of scout F report.*
