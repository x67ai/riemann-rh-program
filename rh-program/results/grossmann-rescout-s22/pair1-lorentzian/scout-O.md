# PAIR 1 — W1-14 lorentzian-log-concavity — SCOUT O (Opus 5) — Session 24, item 2

**Written 2026-09-24, from 16:40 IST (machine clock), by scout O, blind to scout F.** Operating note: `LAUNCH-NOTE.md` (this folder). Contract: `../SCOUT-BRIEF.md` lines 5–11; `../PRICING.md` §0 (lines 11–22), §1 (lines 26–92), §4(i) (line 248), §4(iii)–(v) (lines 259–283). Sources read at the page: `../verify/bh-text.txt` (Brändén–Huh, arXiv:1902.03719), `../verify/milne-text.txt` (Milne, arXiv:1509.00797); `BARRIER-ZOO.md` I.1 (45–52), II.4 (136–149), III.6 (203–210), III.16 (288–298), III.20 (324–331), IV.1 (345–351), IV.18 (484–490), IV.19 (517–523), V.5 (557–565); `results/grossmann-sweep.json` `reports[14]` (file lines 960–1010, extracted with Python's `json` module); `results/c2-followups/insights-digest.md` §D(ii) (lines 200–207). Blindness kept: I did not open `scout-F.md`, any other block of `SHARED.md`, or any `adjudication.md`. No web access was used. Nothing was committed; the only files written are this report and my own `SHARED.md` block.

Line-number convention: `BH n` = `../verify/bh-text.txt` line n; `M n` = `../verify/milne-text.txt` line n; `Z n` = `BARRIER-ZOO.md` line n; `P n` = `../PRICING.md` line n; `J n` = `results/grossmann-sweep.json` line n; `D n` = `results/c2-followups/insights-digest.md` line n; `m0 n` = `results/c3-r/m0-axiom-note.md` line n.

---

## 1. The rung (R-b), re-derived at the page

### 1.1 What "Lorentzian" requires (the definition read, not inferred)

- The class P^d_n is "the open subset of polynomials all of whose coefficients are positive" (BH 269–270); Definition 2.1 builds the strictly Lorentzian class L̊^d_n inside P^d_n, with L̊²_n = {f ∈ P²_n : H_f nonsingular with exactly one positive eigenvalue} (BH 312–314), and "the limits of strictly Lorentzian polynomials are called Lorentzian" (BH 321–322).
- The closed description: L²_n is "the closed subset of quadratic forms with nonnegative coefficients that have at most one positive eigenvalue" (BH 77–79); for d > 2, L^d_n sits inside M^d_n, "the set of polynomials with nonnegative coefficients whose supports are M-convex" (BH 83–86); Theorem 2.25 (BH 1111) identifies L^d_n with the Lorentzian class, "a degree d homogeneous polynomial f with nonnegative coefficients is Lorentzian if and only if the support of f is M-convex and ∂^α f has at most one positive eigenvalue for every α ∈ Δ^{d−2}_n" (BH 1116–1118).
- **Finding (stop line (a) checked):** nonnegativity of every coefficient is part of the definition (BH 78, 85, 269–270, 1116). Stop line (a) does not fire.

For a quadratic form (d = 2) the test is therefore: nonnegative coefficients, M-convex support, and at most one positive eigenvalue of the Hessian (BH 1116–1118 with α = 0). The Hessian of a quadratic form f(w) = wᵀGw is 2G, so the eigenvalue condition is a condition on the inertia of the symmetric matrix G.

### 1.2 The two-line identities (re-derived; Milne cited at the line)

**(i) The point count is a von Mangoldt sum.** Milne defines Z(C, T) by d log Z(C, T)/dT = Σ_{n≥1} N_n T^{n−1} (M 56–60), with the Euler product Z(C, T) = ∏_P (1 − T^{deg P})^{−1} over closed points P and N𝔭 = q^{deg P} (M 61–66), and ζ(K, s) = Z(C, q^{−s}) (M 68). Taking T·d/dT of log of the product: T·(log Z)′ = Σ_P Σ_{k≥1} deg P · T^{k·deg P} = Σ_{n≥1} (Σ_{P : deg P | n} deg P) T^n. Comparing with M 58–59 gives N_n = Σ_{deg P | n} deg P. In the s variable, −ζ_K′/ζ_K(s) = (log q)·T·Z′/Z(T) at T = q^{−s}, so −ζ_K′/ζ_K(s) = Σ_n (N_n log q) q^{−ns}: the function field's von Mangoldt function is Λ(P^k) = deg P · log q = log N P ≥ 0 on the prime-power ideal P^k, and N_n log q is the sum of Λ over the prime-power ideals of norm q^n. So N_n is nonnegative von Mangoldt data of C, summed by norm.

**Record correction (sign convention).** The launch note (line 9) and the pricing (P 51, P 60) write "−Z′/Z = Σ N_n T^{n−1}". In Milne's T variable the identity carries no minus sign: Z′/Z(T) = Σ N_n T^{n−1} (M 58–59); the minus belongs to the s variable, −ζ_K′/ζ_K(s) = Σ N_n (log q) q^{−ns}, as derived above. The content the rung uses (N_n is the norm-summed von Mangoldt datum, and N_n ≥ 0) is unchanged.

**(ii) The point count is an intersection number on the square.** Milne's eq. (2), (X·Δ) = d₂(X) − Tr(X | H¹(C)) + d₁(X), with d₁(X) = (X · C × pt) and d₂(X) = (X · pt × C), is at **M 196–198** (the pricing's "line 195" is one line early; the equation number (2) is at M 196). For the Frobenius graph it reads (Γ_π · Δ) = 1 − "Tr(π | H¹(C))" + q (M 201–203), and "(Γ_π · Δ) = |C₀(k₀)|" (M 205). The tower form is Milne's (2.1): N_n = (Γ_{π^n} · Δ) = Σ_r (−1)^r Tr(π^n | H^r) (M 1473–1476). So N_n = (Γ_{π^n} · Δ) for every n ≥ 1, and with (i), each entry of the tower is a von Mangoldt datum.

**(iii) RH for C is the bound for every n, not for n = 1.** Milne: N_n = 1 + q^n − (a₁^n + … + a_{2g}^n) (M 97); RH implies |N_n − q^n − 1| ≤ 2g·(q^n)^{1/2}, "conversely, if this inequality holds for all n, then the Riemann hypothesis holds for C" (M 98–102). **Refinement of the pricing's YES criterion (P 60):** the pricing names the n = 1 inequality |N₁ − q − 1| ≤ 2g√q; that inequality alone is the Hasse–Weil bound for N₁, and RH for C is the conjunction over n ≥ 1 (M 102). The Lorentzian statement below is therefore taken over the tower Γ_{π^n}, one quadratic form per n, which is III.20's item 4 ("tower", Z 326, Z 328).

### 1.3 The intersection form on span{C × pt, pt × C, Δ, Γ_{π^n}}

Write F₁ = C × pt, F₂ = pt × C, Δ, Γ = Γ_{π^n} on V = C × C over the algebraic closure. Every entry below is read from Milne or computed from his lines:

- F₁² = 0 = F₂², F₁·F₂ = 1 (M 458–462).
- For the graph Γ_f of f : C₁ → C₂, d₂ = 1 and d₁ = deg f (M 505–506), and (Γ_f)² solves 2g₁ − 2 = (Γ_f)² + (2g₁ − 2)·1 + (2g₂ − 2)·deg f (M 508–511). With f = id (Γ_f = Δ, deg 1, g₁ = g₂ = g): Δ·F₁ = Δ·F₂ = 1 and Δ² = 2 − 2g. With f = π^n (deg f = q^n, the degree of the q^n-power Frobenius): Γ·F₁ = d₁ = q^n, Γ·F₂ = d₂ = 1, and Γ² = q^n(2 − 2g). Check against Milne: def(D) = 2d₁d₂ − D² (M 481–483) gives def(Δ) = 2 − (2 − 2g) = 2g and def(Γ_π) = 2q − q(2 − 2g) = 2gq, which are Milne's values (M 519).
- Δ·Γ = N_n (§1.2 (ii)).

Gram matrix G_n in the basis (F₁, F₂, Δ, Γ):

```
        F1     F2     Δ        Γ
F1  [   0      1      1        q^n        ]
F2  [   1      0      1        1          ]
Δ   [   1      1      2−2g     N_n        ]
Γ   [   q^n    1      N_n      q^n(2−2g)  ]
```

The volume polynomial of these four classes, vol(w) = (w₁F₁ + w₂F₂ + w₃Δ + w₄Γ)² (BH 2335–2341 with d = 2), has the coefficient of w₃² equal to Δ² = 2 − 2g and of w₄² equal to q^n(2 − 2g): **for g ≥ 2 both are negative, so the untranslated form is not in M²₄ and is not Lorentzian by definition (BH 78).** Consistently, Δ and Γ are not nef for g ≥ 2, since Δ·Δ < 0 and Γ·Γ < 0 violate "(D·C) ≥ 0 for every irreducible curve C" (BH 2349) at C = Δ and C = Γ. So the nef-translation Theorem 4.6 needs is not optional; it is carried out next.

### 1.4 The nef translation, with nonnegative coefficients

Take H₁ = F₁, H₂ = F₂, H₃ = Δ + g·F₁ + g·F₂, H₄ = Γ + (2g − 1)·F₁ (all with integer coefficients; the pricing's shape "Δ + a(C × pt) + b(pt × C)", P 60, with a = b = g, and a′ = 2g − 1, b′ = 0 for Γ).

**Nefness (why these classes carry Δ and Γ).** H₃·Δ = (2 − 2g) + g + g = 2 ≥ 0 and H₄·Γ = q^n(2 − 2g) + (2g − 1)q^n = q^n ≥ 0 (from the Gram matrix). For an irreducible curve E other than Δ (resp. Γ), H₃·E ≥ 0 (resp. H₄·E ≥ 0) follows from Δ·E ≥ 0, Γ·E ≥ 0, F₁·E ≥ 0 and F₂·E ≥ 0 — the standard surface facts that two distinct irreducible curves meet nonnegatively and that the fiber classes F₁, F₂ are nef, which are `[recalled, unverified]` (neither source on disk states them; BH 2324–2325 states only the transverse-count rule). F₁ and F₂ are nef on the same recalled ground. **The load-bearing equivalence in §1.5 does not use nefness** — it uses the definition (BH 78) and the index theorem (M 448); nefness is needed only to place the object literally under BH Theorem 4.6 (BH 2352), and that placement carries the one recalled step just named.

**Nonnegative coefficients (computed from the Gram matrix; exact in integers).** In the basis (H₁, H₂, H₃, H₄):
- H₁² = H₂² = 0; H₁·H₂ = 1; H₃·H₁ = 1 + g; H₃·H₂ = 1 + g; H₄·H₁ = q^n; H₄·H₂ = 1 + (2g − 1) = 2g;
- H₃² = (2 − 2g) + 2g + 2g + 2g² = 2 + 2g + 2g² > 0;
- H₄² = q^n(2 − 2g) + 2(2g − 1)q^n = 2g·q^n > 0;
- H₃·H₄ = N_n + (2g − 1) + g·q^n + g + g(2g − 1) = N_n + g·q^n + 2g² + 2g − 1 > 0, because N_n ≥ 0 (a point count, M 49).

So vol_H(w) = Σ_{i,j} (H_i·H_j) w_i w_j has every coefficient ≥ 0, and every coefficient except those of w₁² and w₂² is > 0 (for g ≥ 1). Its support is Δ²₄ minus {2e₁, 2e₂}. **M-convexity of this support** (BH 86–89) was checked by exhaustive enumeration over all pairs of support monomials (scratch script, §1.7): it holds. Stop line (b) does not fire.

### 1.5 The equivalence (the rung's content)

**Claim.** For every n ≥ 1, the quadratic form P_n(w) := vol_H(w) = (w₁H₁ + w₂H₂ + w₃H₃ + w₄H₄)², whose coefficients are the integers of §1.4 (polynomials in q^n, g and the single von Mangoldt datum N_n), is Lorentzian in the sense of BH Definition 2.1 **if and only if** |N_n − q^n − 1| ≤ 2g·q^{n/2}. Hence {P_n Lorentzian for all n ≥ 1} ⟺ RH for C (M 98–102).

**Proof (re-derived; two steps).**
1. *Reduction to the four original classes.* The basis change (F₁, F₂, Δ, Γ) → (H₁, …, H₄) is unitriangular, so the Gram matrix of the H's is Mᵀ G_n M with M invertible; the number of positive eigenvalues is basis-independent (Milne's "index … is independent of the basis", M 431–433 — Sylvester). Coefficients are nonnegative and the support is M-convex (§1.4), so by BH 1116–1118 (α = 0), P_n is Lorentzian ⟺ G_n has at most one positive eigenvalue.
2. *Orthogonal splitting.* Put Δ′ = Δ − F₁ − F₂ and Γ′ = Γ − F₁ − q^n F₂ — Milne's D − d₂C₁ − d₁C₂ (M 473) for D = Δ (d₁ = d₂ = 1) and D = Γ (d₁ = q^n, d₂ = 1). From G_n: Δ′·F₁ = Δ′·F₂ = Γ′·F₁ = Γ′·F₂ = 0; Δ′² = −2g; Γ′² = −2g·q^n; Δ′·Γ′ = N_n − q^n − 1 (each checked symbolically, §1.7). So span = span{F₁, F₂} ⊕ span{Δ′, Γ′} orthogonally; the first block [[0, 1], [1, 0]] has exactly one positive and one negative eigenvalue; so G_n has at most one positive eigenvalue ⟺ the block [[−2g, N_n − q^n − 1], [N_n − q^n − 1, −2g q^n]] has none ⟺ (trace < 0 for g ≥ 1, so) its determinant 4g²q^n − (N_n − q^n − 1)² ≥ 0 ⟺ |N_n − q^n − 1| ≤ 2g q^{n/2}. ∎

The inequality in step 2 is Milne's Corollary 1.6, |D·D′ − d₁d₂′ − d₂d₁′| ≤ (def(D) def(D′))^{1/2} (M 485–489), at D = Δ, D′ = Γ_{π^n} — exactly the instance Milne uses to prove RH for C (M 516–525). So the Lorentzian statement is **not weaker** than the Castelnuovo–Severi step Weil's proof consumes: it is that step, one n at a time.

**That P_n IS Lorentzian (the theorem side)** follows in two independent ways: (a) BH Theorem 4.6 (BH 2352) — the H_i are nef (§1.4, with its recalled step); (b) without nefness: the intersection form on N(V) has index 1 (Milne Corollary 1.3, M 448, from the Hodge index theorem, M 398–400); if G_n had two positive eigenvalues, the form would be positive definite on a 2-plane of span, the map span → N(V)_ℝ would be injective on that plane, and N(V)_ℝ would contain a positive-definite 2-plane, contradicting index 1. Both routes are the Hodge index theorem on the square; BH's own gloss says so: for a volume polynomial "the one positive eigenvalue condition for the Hessian … is equivalent to the validity of the Hodge–Riemann relations on the space of divisor classes" (BH 795–799), and the class was "Inspired by Hodge's index theorem for projective varieties" (BH 63).

**Answer to the rung's first half: YES.** On the bottom rung there is a Lorentzian polynomial (BH Def. 2.1) whose coefficients are von Mangoldt data (N_n, summed by norm, §1.2 (i)) together with the integers 1, q^n, g, and whose Lorentzian property, taken over the tower n ≥ 1, is equivalent to Weil's RH for C; it is the volume polynomial of nef translates of {C × pt, pt × C, Δ, Γ_{π^n}} — the intersection form of the square C × C. Its variables w₁, …, w₄ are indexed by divisor classes on C × C, not by closed points: the closed points enter only through the single aggregated coefficient N_n = Σ_{deg P | n} deg P.

### 1.6 The rung's second half — is any prime-variable Lorentzian object exhibited?

The question (P 61): does the rung exhibit any Lorentzian object in variables x_P (P closed points) with the iff, not passing through C × C? I read the four places the rung names.

- **Brändén–Huh.** The volume polynomial's variables index the divisors H₁, …, H_n (BH 2335–2341); Theorem 4.6 is about nef divisors on a projective variety over an algebraically closed field (BH 2318–2319, 2352); the paper's other instantiations are stable polynomials (BH 74–76, 332–338) and the matroid/linear-independence example (BH 2370–2378). No object in the text has variables indexed by the closed points of a curve over F_q or by primes.
- **Milne.** The closed points appear in the Euler product Z(C, T) = ∏_P (1 − T^{deg P})^{−1} (M 61–65) — a product of univariate factors in one variable T, not a multivariate Lorentzian polynomial; every positivity statement in the proof (M 398–400, 448, 466–479, 485–489, 516–525) is on divisor classes of C × C.
- **`reports[14]`.** Its `key_objects[1]` calls the Lorentzian generator "currently with NO zeta instantiation" (J 972); its only Lorentzian–zeta item is Cid-Ruiz's mixed Segre zeta function, "a power series encoding information about the mixed Segre classes" of homogeneous ideals in a polynomial ring (`../verify/abs-2507.06424.html` line 30; J 991) — no L-function, no primes; its `first_interface` is a conjecture-shaped statement, not an object (J 994).
- **The record.** PRICING §1(b)(vi) and §1(c) (P 48–51, P 61) exhibit only the square's form.

**One construction I checked so that the second half is not answered by accident.** BH Theorem 2.10: "If f(w) ∈ L^d_n, then f(Av) ∈ L^d_m for any n × m matrix A with nonnegative entries" (BH 588). So for any nonnegative 4 × |S| matrix A indexed by a finite set S of closed points, P_n(A x) is a Lorentzian polynomial in variables x_P, P ∈ S. It is Lorentzian because P_n is, i.e. because of the Hodge index theorem on C × C; its coefficients are P_n's coefficients pushed through a free choice of A (a design parameter, P 19 item 5); it is not multiaffine (it has x_P² terms), which the interface requires (J 994, "homogeneous multiaffine polynomials"). **This dressing passes through C × C by construction, so it does not answer the second half.** I record it only to show that the prime-variable *shape* is reachable as a relabeling of the square, which is what "passing through C × C" excludes.

**Answer to the second half: none exhibited.** In the two sources, `reports[14]` and the record, the only Lorentzian instantiation with RH content on the bottom rung is the square's; the only prime-variable Lorentzian objects I can form from them are nonnegative substitutions into the square's volume polynomial (BH 588), which pass through C × C. This is a statement about the branch's inventory as read at the page (V.5, THE DISTINCTION, Z 560: "The branch does not contain the object" — internal); it is not a claim that no such object can exist, and it is not used as evidence that none can.

### 1.7 Sanity computation (scratch, not a source)

`sq.py` in this session's scratchpad (outside the repository; SHA-256 `2ceadb52c33fe6d3a34794553c08aaee03eba591952f86027f6e9c63318233dc`; sympy, exact integer arithmetic; inertia by Descartes' sign rule on the characteristic polynomial, exact for a real symmetric matrix). For (q, g, n) ∈ {(2,1,1), (3,1,1), (5,2,1), (5,2,2), (7,3,1), (3,2,3), (4,2,1)} and every integer N_n in a range covering the Weil interval plus 3 on each side (182 cases, including the boundary equality cases at q^n = 4 where 2g·q^{n/2} is an integer), it built G_n and the translated Gram matrix, and checked: all coefficients ≥ 0; the support M-convex (exhaustive exchange check); same inertia before and after translation; and "Lorentzian" ⟺ |N_n − q^n − 1| ≤ 2g q^{n/2}. Result: 182 cases, **0 mismatches**. Symbolically: Δ′² = −2g, Γ′² = −2gq, Δ′·Γ′ = N − q − 1, and Δ′, Γ′ ⊥ F₁, F₂ (n = 1 form). The computation confirms the algebra of §1.4–§1.5; the argument does not rest on it.

---

## 2. The (R-b) return

**Return: YES-by-the-square** (PRICING §1(c), P 64). The Hodge-index form on span{C × pt, pt × C, Δ, Γ_{π^n}}, after the nef translation H₃ = Δ + g(C × pt) + g(pt × C), H₄ = Γ_{π^n} + (2g − 1)(C × pt), is a Brändén–Huh Lorentzian quadratic form with nonnegative integer coefficients and M-convex support (§1.4); its Lorentzian property is equivalent, for each n, to |N_n − q^n − 1| ≤ 2g q^{n/2}, which is Milne's Corollary 1.6 at (Δ, Γ_{π^n}) and, over all n, Weil's RH for C (§1.5; M 98–102, 516–525); and no prime-variable Lorentzian object with the iff that avoids C × C is exhibited in the two sources, `reports[14]` or the record (§1.6).

**Consequence for the grade (as P 64 fixes it in advance).** The dead-end grade on the unbuilt *independent* prime-side sector is restored on internal grounds, in the form: the Lorentzian branch contains no instantiation with RH content other than the one it shares with W1-04 (the square's intersection form). The branch is re-filed as an **instrument** — the Lorentzian / volume-polynomial vocabulary for the closed output condition of the geometric-substrate direction (III.20 items 2–3, Z 326–328; STATUS line 52, "the generator exists but the geometry does not"). It does not become grossmann-candidate.

**Refutation-shaped close (10(c)), verbatim from P 64 (the close PRICING §1(c) attaches to YES-by-the-square):**

*"A multiplicative-Lorentzian bridge with prime-side coefficients cannot be built independently of a doubled object, because on the only rung where RH is a theorem the Lorentzian polynomial with von Mangoldt coefficients is the Hodge-index form of C × C (Brändén–Huh Thm 4.6 + Castelnuovo–Severi), and on the Dirichlet rung unsquared Λ-data violate the definition's nonnegativity (Λ_{χ₄}(3) < 0)."*

**Rider to the close (my re-derivation; it narrows, it does not change the return):** the Lorentzian polynomial is one quadratic form per level n of the Frobenius tower Γ_{π^n}, and RH for C is the Lorentzian property at every n, not at n = 1 alone (M 98–102; §1.2 (iii)).

### 2.1 The two zero-slot notes the pair records (R-a, R-c)

- **(R-a), the S1 clause (c) at the axiom level — the record fact behind it.** Lorentzian coefficients are nonnegative by definition (§1.1). On DH, f_DH = L₁·F₂, so Λ_DH ≠ 0 exactly on {p^k : p ≡ ±1 (mod 5)} ∪ {n : all prime factors ≡ ±2 (mod 5)}, with Λ_DH(3) = −0.3120927285, Λ_DH(4) = −1.4422319646, Λ_DH(6) = +1.9363560766, Λ_DH(12) = −0.7628774720, and 8 562 nonzero coefficients at L = 10 (D 206, items (b)–(c); m0 372–375). A coefficient that is a single Λ_DH(p^k) < 0 puts the polynomial outside M^d_n (BH 85). But Λ_{χ₄}(3) = −log 3 = −1.0986… < 0 for the RH-true L(s, χ₄) (m0 414–416), so the filter is a positivity filter and excludes the Dirichlet rung unsquared (P 46; Z 298). On the bottom rung the question does not arise: Λ(P^k) = log N P ≥ 0 for every function field (§1.2 (i)) — the function field's von Mangoldt data are nonnegative without squaring, and what carries RH there is the square's inertia, not the coefficients' sign.
- **(R-c), III.6 scope.** Rodgers–Tao Λ ≥ 0 acts in the de Bruijn–Newman flow variable (Z 205–207); a certificate whose inputs are prime-side data has no evaluation at t ≠ 0, so III.6 binds only the heat-flow / preserver wing (Z 210; P 40, P 57). On the bottom rung III.6 has no object at all (no flow on Z(C, T)).

---

## 3. The report in the wave-1 schema (`scripts/rh-grossmann-sweep.js` lines 75–86)

**branch.** W1-14 Lorentzian polynomials & log-concavity technology — re-scout of the unbuilt prime-side sector (zoo III.16, SUSPENDED, Z 295–298).

**verdict.** **instrument.**

**confidence.** 0.85.

**Verdict sentences** (each quoted and labeled in `refinement_compliance`, §6):
- V1. On the function-field rung, the Lorentzian polynomial with von Mangoldt coefficients whose Lorentzian property is equivalent to Weil's RH for C is the volume polynomial of nef translates of {C × pt, pt × C, Δ, Γ_{π^n}} on C × C — the Hodge-index form of the square (§1.3–§1.5).
- V2. That polynomial's Lorentzian property at level n is exactly Milne's Corollary 1.6 at (Δ, Γ_{π^n}), so the Lorentzian class contains Weil's certificate and the certificate is not weakened by the translation (§1.5).
- V3. Its variables are divisor classes of C × C; the closed points enter only through the aggregated coefficient N_n, and the only prime-variable Lorentzian polynomials obtainable from the objects read are nonnegative substitutions into it (BH Theorem 2.10), which pass through C × C (§1.6).
- V4. Over Q, the interface's coefficient-nonnegativity clause is a positivity filter that excludes the RH-true L(s, χ₄) unsquared, so the branch's S1 input at the axiom level is Λ ≥ 0, which is not an Euler-product input (§2.1).
- V5. The branch's generator is therefore the Hodge index theorem on a doubled object, the same generator as W1-04 and III.20(B); the branch supplies that direction's closed output condition in Lorentzian vocabulary and supplies no substrate of its own (§2).
- V6. Grade: the dead-end grade on the unbuilt independent prime-side sector is restored on these internal grounds, and the branch is re-filed as an instrument of the geometric-substrate direction.

**fit** (scored against the internal properties above; the M2 instance of D 203 is the comparison for S1 and S2).
- **S1 — 1/5.** The only axiom-level input DH violates is coefficient nonnegativity (Λ_DH(3) < 0, m0 372), which the RH-true L(s, χ₄) also violates (m0 416): a positivity filter, not an Euler-product filter. Against the M2 instance ("it consumes no axiom P; the ζ/DH distinction is M6's", D 203): the branch does consume an input DH violates — unlike M2 — but that input fails the ladder's Dirichlet rung, so the S1 witness is over-broad; on the bottom rung the S1-relevant structure is the square itself, not the coefficients.
- **S2 — 1/5.** On the bottom rung the certificate sees a single off-line Frobenius eigenvalue: if |a_i| > q^{1/2} for one i, then |N_n − q^n − 1| = |Σ a_j^n| eventually exceeds 2g q^{n/2} (from M 97), and P_n fails to be Lorentzian at that finite n (§1.5). Over Q the branch has no object, so nothing matches the M2 instance's explicit bandwidth L*(t, δ) (D 203); the S2 point is the square's, not the branch's.
- **S3 — 2/5.** The invariant is the inertia n₊ ≤ 1 (BH 1116–1118), which is in II.4's list {tr, ‖·‖²_F, atom norms, n₊} (Z 138); on the bottom rung the Hessian entries are intersection numbers, not two-moment Weil-form data, and the certificate is RH itself there (on-line doubles satisfy the closed bound, an off-line pair violates it at some n); over Q, S3 is untested and II.4's depth-uniformity check (Z 141) applies to any future claim.
- **S4 — 2/5.** The generator is genuine and non-Weil (BH 795–799: the one-positive-eigenvalue condition for a volume polynomial is the Hodge–Riemann relation on divisor classes), but its only instantiation with RH content on the rung where RH is a theorem is the Hodge index on C × C (§1.5–§1.6); standalone over Q the branch has a generator with no substrate (STATUS line 52).
- **S5 — 2/5.** Survives III.6 by scope (no prime-side evaluation off t = 0, Z 210) and III.1 if clause (a)'s iff is exact; the built objects stay killed by III.16's internal ground (Z 296); any future over-Q object must pass IV.18 and IV.19 as run in §4, and III.20 returns it until the doubled object is named.

**key_objects.**
1. BH Definition 2.1 and the closed description L²_n / M^d_n (BH 77–86, 269–270, 312–330, 1116–1118): nonnegative coefficients are part of the definition.
2. BH Theorem 4.6 (BH 2352): volume polynomials of nef divisors are Lorentzian; the Hodge–Riemann gloss (BH 795–799).
3. BH Theorem 2.10 (BH 588): nonnegative linear substitution preserves the Lorentzian class — the mechanism of the prime-variable dressing (§1.6).
4. Milne eq. (2) and the Frobenius graph (M 196–205), (2.1) N_n = (Γ_{π^n}·Δ) (M 1476), the zeta function as a von Mangoldt generating series (M 56–68), RH ⟺ the bound for all n (M 97–102).
5. Milne Corollary 1.3 (index 1, M 448), Theorem 1.5 (Castelnuovo–Severi, M 466–479), Corollary 1.6 (M 485–489), Example 1.7 (graphs, M 505–514), the proof of RH for curves (M 516–525).
6. The object of the return: P_n(w) = (w₁F₁ + w₂F₂ + w₃(Δ + gF₁ + gF₂) + w₄(Γ_{π^n} + (2g − 1)F₁))², Lorentzian ⟺ |N_n − q^n − 1| ≤ 2g q^{n/2} (§1.5).

**prior_attacks.** The record's list (`reports[14].prior_attacks`, J 978–987: Jensen–Pólya, Csordas–Norfolk–Varga, GORZ, effective GORZ, Wagner, O'Sullivan, Rodgers–Tao/Dobner, Borcea–Brändén, Brändén–Huh) is carried forward unchanged; each item that died did so on the Taylor-coefficient / flow wing (P 38–42), which this re-scout does not reopen. The one attack on the rung where RH is a theorem is Weil's own proof in Milne's presentation (M 516–525), which §1.5 shows is a Lorentzian-property statement; it is alive as the model and it is the square's. The absence sentences of `reports[14].prior_attacks` (J 987, "arXiv has ZERO papers …") are not used (V.5, Z 559).

**live_entry_points.**
1. The Lorentzian formulation of III.20's closed output condition: for any proposed doubled object over Q carrying classes analogous to F₁, F₂, Δ, Γ (the C3-r direction), the target inequality can be stated as "the volume polynomial of their nef translates is Lorentzian" (§1.5) — the instrument role.
2. Cid-Ruiz's mixed Segre zeta functions (`../verify/abs-2507.06424.html` line 30; J 991) as a nearest published object: a denormalized-Lorentzian generating series with no L-function and no primes (P 83) — the distance to the branch's need is total.
3. The prime-variable dressing through BH Theorem 2.10 (§1.6), as a way to write the square's certificate in variables indexed by closed points for any consumer that needs that shape; it carries no content beyond the square.

**first_interface** (the instrument's interface, replacing the resurrection statement of J 994 for this grade):
*Given a doubled arithmetic object X over Q with classes f₁, f₂, δ, γ_T (for a parameter T of the counting tower) in a real vector space carrying a symmetric form with (f₁², f₂², f₁·f₂) = (0, 0, 1), δ·f_i = 1, γ_T·f₁ = e^T, γ_T·f₂ = 1, and δ·γ_T equal to the prime-side counting datum at T, the statement "the volume polynomial of nef translates of {f₁, f₂, δ, γ_T} is Lorentzian for every T" is equivalent to the Castelnuovo–Severi-type bound |δ·γ_T − e^T − 1|² ≤ def(δ)·def(γ_T) (the computation of §1.5 is formal in the Gram entries); proving it requires the index-one property of the form on X — III.20's generator on III.20's doubled object — and no Lorentzian-polynomial theorem supplies it.* (My own formalization of §1.5; `[novelty: single-check]`; it is the geometric-substrate target restated, not a new target.)

**access_failures.** None. Both sources were on disk in full text (`../verify/`); the Cid-Ruiz item was read from the on-disk abstract only (`../verify/abs-2507.06424.html`), which is all the rung needs.

**verified_online.** None — no web access was used (2026-09-24).

**recalled_unverified.**
1. That two distinct irreducible curves on a smooth projective surface meet nonnegatively, and that the fiber classes C × pt, pt × C are nef — used only to place P_n under BH Theorem 4.6 (§1.4), not in the equivalence (§1.5), which uses BH 1116–1118 and M 448 instead.
2. That Descartes' rule of signs counts positive roots exactly for a real-rooted polynomial — used only in the scratch sanity script (§1.7).
3. That the q^n-power Frobenius π^n has degree q^n as a morphism (d₁(Γ_{π^n}) = q^n): Milne gives d₁ = q for π (M 203, from eq. (2)) and deg f for a graph (M 506); the n-th power is my composition step.

---

## 4. Zoo gate — PRICING §1(d) (P 69–79) re-run in my own words, plus IV.18 and IV.19

| Entry | Bottom rung (C/F_q, the (R-b) object P_n) | The interface over Q (J 994) | Returns |
|---|---|---|---|
| **I.1** DH / Epstein filter (Z 45–52) | Not applicable: the rung is the RH-true calibration; there is no DH analog on a curve. The object's inputs are N_n ≥ 0 and the index theorem on C × C (§1.5). | EXECUTABLE TEST (c) (Z 50) passes at the axiom level on "consumes Λ ≥ 0; Λ_DH(3) < 0" (m0 372; D 206 (c)), but over-broadly: Λ_{χ₄}(3) < 0 for RH-true L(s, χ₄) (m0 416). | PASS with over-breadth flagged; the Dirichlet rung is not runnable with unsquared data (§2.1). |
| **III.16** (Z 288–298) | The rung resolves the suspension (Z 295): the Lorentzian instantiation with RH content is the square's (§1.5–§1.6). | EXECUTABLE TEST (Z 292): for a prime-side input (Λ ≥ 0 + multiplicativity) the input fails for DH (Λ_DH(12) < 0, Z 47), so it is not S1-empty in III.16's sense; the test returns "bridge must be exhibited", and none independent of C × C is exhibited (§1.6). | Suspension lifted on internal grounds: dead-end restored for the independent sector; instrument re-filing (§2). Built-object kills unchanged (Z 296). |
| **III.6** Rodgers–Tao (Z 203–210) | No flow on Z(C, T); nothing to run. | Scope rider (Z 210): no prime-side evaluation off t = 0. | No bind; zero-margin note recorded (§2.1). |
| **III.1** o(N)-blindness (Z 163–169) | P_n's Lorentzian property is an exact inertia condition, not a density statement; one off-line eigenvalue breaks it at a finite n (fit S2). | Clause (a)'s iff is exact; an "asymptotically Lorentzian" or "Lorentzian for n ≥ N(d)" statement would be the GORZ shape III.16 kills. | Passes if the iff is exact; returned otherwise. |
| **II.4** lemmaR_tight (Z 136–149) | The invariant is n₊ (in II.4's list, Z 138), but the Hessian entries are intersection numbers (N_n, q^n, g), not two-moment Weil-form data: II.4 does not bind. | Clause (b) (S3) is untested; any separation claim must state the provenance of the Hessian entries and pass II.4's depth-uniformity check (Z 141). | No bind on the rung; open over Q. |
| **III.20** S6 doubled-object rule (Z 324–331) | All four items present: doubled object C × C; external generator Hodge index (M 398–400, 448); closed output |N_n − q^n − 1| ≤ 2g q^{n/2} (§1.5); tower Γ_{π^n}·Δ = N_n (M 1476) with rationality (M 70–75). | Item 1 (the doubled object) is missing (STATUS line 52). | Conformant on the rung; over Q returned until the doubled object is named — which is where §2.1's positivity argument also lands. |
| **IV.1** Weil-positivity-in-disguise (Z 345–351) | The Lorentzian form is the full index theorem on the square; Weil positivity is its diagonal shadow (Z 326). Not in disguise. | No prime-variable object exists to express as a Weil test × bounded multiplier (Z 349); not run. | No bind on the rung; not run over Q. |
| **IV.18** Sector-I confinement (Z 484–490) — NEW row | Not applicable: IV.18 is a theorem about ζ's explicit formula and the strip-positive cone Σ_L (Z 486); a curve has no such cone. | Split the Lorentzian membership of any future P_N into two parts. (i) Coefficient nonnegativity (BH 85) is a first-order positivity condition on Λ-data — the same axiom P that IV.18's budget decomposition consumes "exactly once" (Z 486, clause (1)); any zero-free claim resting only on it is of the cone / positivity class IV.18 binds (Z 490), and at points where the density hypothesis holds it reaches only the de la Vallée Poussin layer (Z 487). (ii) The Hessian-inertia condition n₊ ≤ 1 (BH 1116–1118) is not a linear functional of Λ-data: it is a condition on minors, i.e. quadratic in the coefficients (at n = 1 on the rung, (N₁ − q − 1)² ≤ 4g²q, §1.5; BH Prop. 4.5, BH 2303–2304, the reverse Cauchy–Schwarz form). So the different invariant is named: **the inertia (signature) of a Gram matrix whose entries are first-order data**. The interface's clause (a) (zero-freeness up to T(N) at every depth) would have to be paid by part (ii), since part (i) alone is confined by IV.18. The branch makes no zero-free claim at any (t, δ) today, so IV.18's EXECUTABLE TEST (Z 488) has nothing to run on. | Not binding as stated (no claim to test); binding on any future claim that uses only coefficient positivity; the escape invariant is n₊ of the Gram matrix — which is also the invariant of II.4's list, so the two entries price the same coordinate from two sides. `[my reading; single-check]` |
| **IV.19** Kronecker sharpness (Z 517–523) — NEW row | Not applicable: no height variable; RH for C is a finite condition (N_n for all n are determined by finitely many of them, M 1316–1318). | The Lorentzian test of a finite P_N is itself an **evaluation** (a finite check on finitely many t-independent coefficients), which IV.19 does not bind (Z 523, "Does NOT bind: the evaluation route"). But clause (a) asserts that ONE t-independent coefficient set certifies zero-freeness at EVERY height up to T(N): its direction "P_N Lorentzian ⟹ no off-line zero up to T(N)" is a height-uniform conclusion from prime-side data. If that direction were proved by a bound on a prime sum of the shape P_X(g_t) = Σ_{n≤X} w_n cos(t log n) uniform over t ∈ [0, T(N)], IV.19 returns it: by Theorem (E) the supremum of such a sum over any window of length ≥ H₀ is the torus supremum Σ_p max_θ φ_p(θ) ≈ the ℓ¹ norm (Z 519), which exceeds the needed signal (Z 519, "8.4 to 1.3·10⁵"). So clause (a) could never be certified by a height-uniform prime-side estimate; it could be certified only through an invariant that is not a prime-sum estimate — on the bottom rung that invariant is the index theorem on C × C, where N_n = Γ_{π^n}·Δ is an exact count (M 1476), not an estimated sum. The cost currency of any evaluation over Q is the term count (Z 519, cost line). | Binds any proof of clause (a) that runs through a t-uniform prime-side estimate; does not bind the Lorentzian check itself (an evaluation). `[my reading; single-check]` |
| **V.5** Grossmann-condition rule (Z 557–565) | — | — | Complied with: every verdict sentence is labeled in §6; the struck absence sentences of III.16 (Z 296) and `reports[14]` (J 987, J 994 last-but-one clause) are not used. |

---

## 5. "Stop and report when" lines (PRICING §4(i), P 248) — verbatim, with whether each fired

- **(a)** "Brändén–Huh Definition 2.1 / the M^d_n definition (`verify/bh-text.txt` lines 78–86, 312–330) is found NOT to require nonnegative coefficients — then 1(b)(iv)–(v) are void and the rung is re-priced" — **did not fire.** The definition requires nonnegative coefficients (BH 78, 85) and the strict class requires positive ones (BH 269–270, 318).
- **(b)** "the Hodge-index form on span{C × pt, pt × C, Δ, Γ_π} cannot be translated to nef classes with nonnegative coefficients so that Theorem 4.6 applies — then the return is NO ("the Lorentzian class does not contain Weil's certificate") and the scout stops" — **did not fire.** The translation H₃ = Δ + g(C × pt) + g(pt × C), H₄ = Γ_{π^n} + (2g − 1)(C × pt) gives nef classes (with the recalled step of §1.4) and nonnegative integer coefficients with M-convex support (§1.4); the equivalence of §1.5 holds independently of the nefness step.
- **(c)** "a published prime-variable Lorentzian object with the iff on the function-field rung is found (V.2 pre-emption) — then the return is YES-with-object and the scout stops to report it rather than building on it" — **did not fire.** None is found in the places read (§1.6); the Theorem 2.10 dressing is not published, not multiaffine, and passes through C × C.

No stop line fired.

---

## 6. refinement_compliance (V.5, Z 557–565; SCOUT-BRIEF line 6)

Every sentence of the verdict (§3, V1–V6), plus the return sentence and the close, quoted and labeled.

| # | Sentence (quoted) | Label | Why |
|---|---|---|---|
| V1 | "On the function-field rung, the Lorentzian polynomial with von Mangoldt coefficients whose Lorentzian property is equivalent to Weil's RH for C is the volume polynomial of nef translates of {C × pt, pt × C, Δ, Γ_{π^n}} on C × C — the Hodge-index form of the square (§1.3–§1.5)." | **internal** | A derivation from BH 1116–1118, M 448, M 485–489 (§1.5). |
| V2 | "That polynomial's Lorentzian property at level n is exactly Milne's Corollary 1.6 at (Δ, Γ_{π^n}), so the Lorentzian class contains Weil's certificate and the certificate is not weakened by the translation (§1.5)." | **internal** | An equivalence proved at the page. |
| V3 | "Its variables are divisor classes of C × C; the closed points enter only through the aggregated coefficient N_n, and the only prime-variable Lorentzian polynomials obtainable from the objects read are nonnegative substitutions into it (BH Theorem 2.10), which pass through C × C (§1.6)." | **internal** | A statement about the objects' structure and about the inventory read at the page ("the branch does not contain the object", Z 560); it asserts nothing about what has or has not been published, and no conclusion is drawn from a search. |
| V4 | "Over Q, the interface's coefficient-nonnegativity clause is a positivity filter that excludes the RH-true L(s, χ₄) unsquared, so the branch's S1 input at the axiom level is Λ ≥ 0, which is not an Euler-product input (§2.1)." | **internal** | BH 85 plus a computed value (m0 416). |
| V5 | "The branch's generator is therefore the Hodge index theorem on a doubled object, the same generator as W1-04 and III.20(B); the branch supplies that direction's closed output condition in Lorentzian vocabulary and supplies no substrate of its own (§2)." | **internal** | Follows from V1–V3 and BH 795–799; "supplies no substrate" is the S4 statement "the generator has no instantiation in the class" that Z 560 lists as internal. |
| V6 | "Grade: the dead-end grade on the unbuilt independent prime-side sector is restored on these internal grounds, and the branch is re-filed as an instrument of the geometric-substrate direction." | **internal** | The grade P 64 fixes in advance for this return. |
| R | "Return: YES-by-the-square …" (§2, first paragraph) | **internal** | Restates V1–V3. |
| C | The refutation-shaped close (§2, verbatim from P 64). | **internal** | Each clause is a derivation (the square's form, §1.5) or a computed value (Λ_{χ₄}(3) < 0, m0 416); it contains no absence-of-literature clause. |

**Unlabeled absence sentences in the verdict: none.** Absence sentences present in inputs and NOT used: III.16 STATEMENT "arXiv contains literally zero papers …" and KILLS "no candidate exists" (Z 290–291, struck at Z 296); `reports[14]` `fit.S1` last clause "zero published attempts …" (J 964), `prior_attacks` last item (J 987), `verified_online` null-search item, and `first_interface` "No publication attempts any statement of this shape" (J 994).

---

## 7. Distance from upstream (10(n)), and honesty note

**10(n).** The rung builds nothing new. The object of §1.5 is, up to the nef translation, the intersection form of C × C that Milne's proof uses (M 466–479, 485–489, 516–525), read through BH Theorem 4.6 (BH 2352) and Definition 2.1; the exact difference from upstream is the translation to nonnegative coefficients (§1.4) and the observation that the Lorentzian test and Corollary 1.6 coincide one n at a time (§1.5). The prime-variable dressing (§1.6) is BH Theorem 2.10 (BH 588) applied to that object; nearest published object: Theorem 2.10 itself. The instrument interface of §3 is `[novelty: single-check]` and passes the dual-model check (standing order 7) before anything is built on it.

**Read at the page:** every line cited above. **Derived by me:** §1.2 (i) (the von Mangoldt reading of N_n and the sign correction), the Gram entries of §1.3 from Milne's Example 1.7, the translation and coefficients of §1.4, the equivalence of §1.5 (both steps), the Theorem 2.10 dressing of §1.6, and the IV.18 / IV.19 readings of §4 (marked single-check). **Computed:** the scratch sanity script of §1.7 (182 cases, 0 mismatches; exact arithmetic). **Recalled, not load-bearing:** the three items of `recalled_unverified`. **Corrections of record offered (for the adjudicator or harvest, not applied to any file):** (1) the launch note line 9 and P 51, P 60 write "−Z′/Z = Σ N_n T^{n−1}"; in Milne's T variable it is Z′/Z (M 58–59), the minus belonging to −ζ_K′/ζ_K(s); (2) Milne's eq. (2) is at M 196, not 195; (3) the pricing's YES criterion names the n = 1 inequality, while RH for C is the inequality for all n (M 102) — the return is unaffected because the Lorentzian object is defined at every level of the tower. **Files touched:** this report and one dated block appended to `SHARED.md`. Nothing committed.
