# NOTE — unit `dz-half-s39`: Diamond–Zhang's random Beurling systems have β = ½ almost surely

**Writer:** Opus 5.5 (subagent of Session 39), 2026-10-01. Brief: `BRIEF.md`. Record read at the line: frontier
`read-O.md` §4 A3 and §7(a); frontier `NOTE.md` §4 Theorem B (as repaired by read-O F2); digest
`novel-wave-s37/insights-digest.md` §F.2 item 4 (U5a); Diamond–Zhang book (AMS Surv. 213, 2016) ch. 17 at the page
(`sources/t-50-diamond-zhang-2016-book.txt`, extracted from `fetched-r2/t-50-…-BOOK.pdf`); BDR z-02 p. 3 fn. 4.
Labels: [proved here], [quoted, file:line], [recalled, unverified], [computed], [heuristic].

## §0. Close

(written last)

## §1. The objects, read at the page

**1.1 The construction** [quoted, `sources/t-50-diamond-zhang-2016-book.txt`; book pp. 196–202]. A template density f ≥ 0 on
[1, ∞); an increasing sequence 1 = v₀ < v₁ < … → ∞; p_k := ∫_{v_{k−1}}^{v_k} f(v) dv (Lemma 17.5, "satisfies 0 < p_k ≤ 1 for
k ≥ k₀"); X_k independent with P[X_k = 1] = p_k, P[X_k = 0] = 1 − p_k (proof of Lemma 17.2, book p. 197); the g-primes are
the v_k with X_k = 1. DZ take the grid (17.13), book p. 201: "v₀ = 1 and v_k = n + ℓ/2ⁿ, for k = 2ⁿ + ℓ, n = 0, 1, 2, …,
1 ≤ ℓ < 2ⁿ". As printed the index set {2ⁿ + ℓ : 1 ≤ ℓ < 2ⁿ} omits k = 1, 2, 4, 8, …; the grid meant is
Γ := {1} ∪ {n + ℓ/2ⁿ : n ≥ 1, 0 ≤ ℓ < 2ⁿ} (Remark 17.6's "closed under addition and multiplication" needs the integers,
e.g. 1.5 + 1.5 = 3). Nothing below depends on the reading: the proof uses only independence, p_k = ∫_{cell} f, and
max{p_k : v_k ∈ (x/2, x]} → 0; on Γ that maximum is ≤ 2^{−⌊x/2⌋}.

**1.2 The two templates.** Theorem 17.11 (the RH example P_R): f_R(v) = (1 − v⁻¹)/log v (book p. 206, "Consider the template
continuous density"). Theorem 17.14 (the DLVP example P_B): f_C of (17.44), book p. 218,
f_C(v) = (1 − v⁻¹)/log v − 2Σ_{k≥1} (g(v^{4^{−k}})/4^k) v^{−4^{−k}} cos(γ_k log v), γ_k = e^{4^k}, β_k = 1 − 4^{−k}
(p. 214), g = Σ_n χ^{*n}/n with χ = 1_{[e,e²]} (17.30); and (17.45), p. 218: "(1 − c)(1 − v⁻¹)/log v ≤ f_C(v) ≤
(1 + c)(1 − v⁻¹)/log v holds for v ≥ e⁴", c = 2c₁/(1 − e⁻⁴), c₁ = 0.410616… (p. 216), so c = 0.8366… < 1 [computed].
For v < e⁴, f_C = f_R (p. 218). Both templates therefore satisfy
  (H) c_* /log v ≤ f(v) ≤ C_*/log v for v ≥ v_*, with (c_*, C_*) = (0.49, 1) for f_R (v_* = 100), (0.16, 1.84) for f_C.

**1.3 What DZ prove about the result** [quoted]. Thm 17.14 (book p. 208): "(i) N_B(x) = k₂x + O(x^{1/2} exp{c(log x)^{2/3}})
with k₂ > 0; (ii) ζ_B(s) is analytic for σ > 1/2 except for a simple pole at s = 1 with residue k₂; (iii) ζ_B(s) has
infinitely many zeros on the curve σ = 1 − 1/log t, t ≥ e², and no zeros to its right; (iv) lim sup / lim inf of
(ψ_B(x) − x)/(x exp{−2√log x}) = 2 / −2." Thm 17.11 (p. 205): the same (i)–(ii) for N_R with k₁ > 0, no zeros in σ > ½, and
"(iv) π_R(x) = li(x) + O(x^{1/2})". The proofs select the subsequence by Lemma 17.2, whose conclusion holds off a
Borel–Cantelli null set (Remark 17.4: "for almost all subsequences (in the statistical sense)"), then argue
deterministically; so (i)–(iv) hold for almost every realization. DZ's representation (p. 219):
ζ_B(s) = ζ_C(s) exp{−F₁(s) + F₂(s)}, F₁(s) = ∫{v^{−s} + log(1 − v^{−s})}dπ_B(v), F₂(s) = ∫ v^{−s}{dπ_B(v) − f_C(v)dv}, both
analytic on σ > ½. Remark 17.12 (p. 205): "by making a finite number of changes in the g-primes … we can produce a system
that … satisfies k₁ = 1 … (These remarks apply as well for the example in Theorem 17.14.)"

**1.4 The question** [quoted, z-02 l. 133–136, 165]. BDR: "that of a [1, β₀]-system⁴ is in [7, Ch. 17] (which is based on
the papers [6] and [17]) for some β₀ ≤ 1/2"; fn. 4: "Most likely the value of β₀ equals 1/2, but in principle it is still
possible that β₀ could be smaller." Also l. 122–124, on Zhang's system: "Due to the probabilistic nature of the method,
no precise value of α and β could be determined." BDR's definition (l. 97–101): β = lim sup log|N(x) − ax|/log x.
**1.5 DMV** [quoted, fr `sources/p1-02-…txt` l. 935–945]: DMV's Lemma 9 uses the same selection ("let X_k be independent
Bernoulli variables with parameters p_k = ∫_{v_{k−1}}^{v_k} 1 dΠ_C(v) … The v_k must increase sufficiently slowly to
ensure that p_k ≤ 1/2"), so §2 applies to DMV's random system as soon as dΠ_C satisfies (H) (not checked at the page).

## §2. The theorem and its proof

(pending)

## §3. The variance, computed two ways

(pending)

## §4. Finite rung: simulation of the construction to 10⁸, five seeds, with controls

(pending)

## §5. Prior-art gate: is BDR fn. 4 settled after BDR?

(pending)

## §6. Distance from upstream, Instruments row, Untried, waste line

(pending)
