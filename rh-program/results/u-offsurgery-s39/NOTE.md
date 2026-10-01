# NOTE — unit `u-offsurgery-s39`: Conjecture U off the surgery class — proposed discrete systems with α > ½, β < ½, and the attempt to refute U

Session 39, 2026-10-01. Writer: Opus 5.5 (agent). Status labels as in `novel-wave-s37/beurling-frontier/NOTE.md`: **[proved here]**,
**[computed]** (script + log in `verify/`), **[quoted]** (source under `sources/` or the named record file, page/line given),
**[recalled, unverified]** (never load-bearing), **[novelty: single-check]**.

Notation. A Beurling system P = (p_j) (discrete: point masses with positive integer multiplicities, dN ≥ 0, Λ_P ≥ 0).
[α, β]-system: ψ_P(x) = x + O(x^{α+ε}), N_P(x) = ρx + O(x^{β+ε}) for every ε > 0, for no ε < 0.
**Conjecture U** (fr/NOTE.md §7.2): every discrete [α, β]-system has α ≤ max{½, 2β}. Paths: `fr/` = `results/novel-wave-s37/beurling-frontier/`.

## §0. Close (filled last)

(pending)

## §1. The designs (task: at least three non-surgery, non-number-field discrete systems aimed at α > ½, β < ½)

Principle used to design them. For a discrete system, ζ_P − ρs/(s − 1) = s∫(N_P − ρx)x^{−s−1}dx, so β < ½ needs ζ_P analytic with at most
polynomial growth on σ > β; α > ½ needs a zero (or singularity of ζ′_P/ζ_P) at Re s = α. Every design below plants or looks for a zero
in (½, 1) while trying to keep the integer counting function regular. Rational templates: R(s) = Π(s − z_i)/(s − p_i) (as many zeros as
poles, p₁ = 1), with log R(s) = ∫₁^∞ x^{−s}Σ_i(x^{p_i} − x^{z_i})dx/(x log x) [proved here: both sides have derivative Σ(1/(s − z_i) −
1/(s − p_i)) and vanish as s → +∞].

| id | construction | g-primes | class | how α > ½ is designed | what keeps β small (the hope) |
|---|---|---|---|---|---|
| S1 | greedy (deterministic) discretization of the planted template R₀(s) = (s − ρ₀)(s − ρ̄₀)/((s − 1)(s − (2β₀ − 1))) | reals q_j with Π_Q(x) − Π_{R₀}(x) ∈ [−½, ½] | brief (i), tracking form | zero of R₀ at ρ₀ = β₀ + iγ₀, exactly inherited | N_{R₀}(x) = ρx + c x^{2β₀−1} + c′; no random noise |
| S2 | Bernoulli selection on a fine grid from the same template (Diamond–Zhang style) | reals, random | brief (i), DZ rung | same zero, inherited in σ > ½ | none (control: β = ½ expected) |
| S3 | pseudo-character twist of N: m_{p,1} = 1 + f(p), m_{p,2} = (1 − f(p))/2, f(p) = ±1 chosen greedily so that Σ_{p≤x} f(p)log p tracks an explicit-formula target | rational primes p (0 or 2 copies) and some p² | brief (ii), dense twist | ζ_P = ζ·L_f, L_f = R_ρ₀(s)·e^{R̃(s)}, R̃ analytic in σ > 0 (§4) | prime-level balance with O(log x) discrepancy — no sparse deleted set, so no Theorem-B noise |
| S3₀ | the same with no planted zero (target = the Chebyshev-bias term only) | as S3 | control | none (α = Θ) | as S3 |
| S4 | quadratic character χ_{−4} with sparse greedy sign flips carrying the planted target | as S3 | brief (iii), calibration: number field + structured surgery | planted zero at ρ₀ | coherent base (β_K ≤ ⅓) |
| S5 | integer-greedy ("self-regulated") system of density ρ ∉ ℤ: g-prime multiplicities m_n ≥ 0 at every integer n chosen so that N(n) tracks ρ(n − 1) + 1 | integers n ≥ 2 with multiplicity | brief (ii), "choose primes first" in its extreme form | not planted: a discrete β ≈ 0 system is exactly where U says "RH"; off-line zeros of ρζ + D would refute U | the integer count is controlled at every step |

S3–S5 are supported on ℕ and are neither deletions/additions of rational primes in the sense of fr/NOTE §3–§5 (the modified set has
density one in S3, and S5's g-primes are composite integers as well) nor ideal systems of a number field (§5 proves that the periodic
version of S3 IS a number field — that is the rigidity). S4 is the deliberate calibration inside the excluded classes.

## §2. S5, the integer-greedy systems — the candidate that crosses the line numerically [computed]

**Definition.** Fix ρ > 0. Walk n = 2, 3, …; let A(n) = #{representations of n as a product of g-primes chosen so far} (with
multiplicity) and N(n − 1) the count so far. Put m_n := max(0, ⌊ρ(n − 1) + 1 − N(n − 1) − A(n) + ½⌋) copies of n into the g-prime list.
Then a_n = A(n) + m_n is the multiplicity of the g-integer n and N(n) = N(n − 1) + a_n. This is a discrete Beurling system (g-primes are
integers ≥ 2 with multiplicities m_n ≥ 0, so dN ≥ 0 and Λ_P ≥ 0), supported on ℕ; ρ = 1 returns the rational primes exactly
(`logs/S5_one_1e8.log`: 5,761,455 g-primes, E ≡ 0). The error E(x) := N(x) − ρx − (1 − ρ) satisfies E ≥ −1 − ρ by construction (the rule
can always add) and is pushed up only by composite g-integers arriving in bursts.

**Instruments.** `verify/pseudoN.c` (multiplicative DP, exact integer arithmetic, log-bins of 20 per decade: sup and inf of E over real x,
RMS at integers, sup|ψ_P(x) − x| with ψ_P = Σ_{q^k≤x} m_q log q); `verify/fit_bins.py` (least-squares slopes of log running-sup and
log RMS over windows [10^k, X]); route 2 for the counts: `verify/pseudoN_check.py` rebuilds the whole system by the log-derivative
recursion a(n) log n = Σ_{d|n} Λ_P(d)a(n/d) and compares a_n term by term with the C dump — **0 mismatches over n ≤ 10⁶ for ρ = 0.8
and ρ = 1.05** (`logs/pseudoN_check_0.8.log`, `logs/pseudoN_check_1.05.log`).

**Anatomy** (`verify/S5_structure.py`, `logs/S5_structure.log`, X = 10⁸). These are not surgeries on ℙ in any useful sense: at ρ = 0.75,
5,169,175 of the 5,761,455 primes below 10⁸ are NOT g-primes, and 5,170,715 composite integers are (15, 26, 35, 39, 51, 55, 74, 75, …;
e.g. 15 enters because 5 was refused). At ρ = φ the rational prime 2 and 132,407 others carry multiplicity 2.

**The sweep at X = 10⁸** (`logs/S5_sweep_fits_1e8.log`; slopes over [10⁴, 10⁸]; b = β-estimate from the running sup of |E|, a = α-estimate
from the running sup of |ψ_P − x|):

| ρ | b_sup | b_rms | a_sup | a − 2b |
|---|---|---|---|---|
| 1 (ℙ, control) | 0.000 | 0.000 | 0.489 | — |
| 0.52 | 0.323 | 0.199 | 0.591 | −0.06 |
| 0.60 | 0.283 | 0.177 | 0.614 | +0.05 |
| 0.75 | 0.316 | 0.201 | 0.671 | +0.04 |
| 0.80 | 0.292 | 0.180 | 0.726 | **+0.14** |
| 0.85 | 0.333 | 0.214 | 0.733 | +0.07 |
| 0.90 | 0.314 | 0.210 | 0.706 | +0.08 |
| 0.95 | 0.278 | 0.199 | 0.672 | **+0.12** |
| 0.99 | 0.283 | 0.221 | 0.577 | +0.01 |
| 1.01 | 0.268 | 0.194 | 0.607 | +0.07 |
| 1.05 | 0.300 | 0.206 | 0.771 | **+0.17** |
| 1.10 | 0.326 | 0.232 | 0.667 | +0.02 |
| 1.20 | 0.390 | 0.288 | 0.741 | −0.04 |
| 1.30 | 0.374 | 0.288 | 0.774 | +0.03 |
| 1.50 | 0.476 | 0.364 | 0.740 | −0.21 |
| φ | 0.544 | 0.406 | 0.859 | −0.23 |
| √2, 2 | ≈ 1.0 | ≈ 1.0 | ≈ 1.0 | (runaway: the composites alone exceed ρ per unit length; not ρ-density systems) |

The per-bin data are clean power laws, not transients: at ρ = 0.8, sup_{bin}E/x^{0.30} stays in [0.42, 0.61] and sup|ψ − x|/x^{0.73} in
[0.11, 0.22] for every bin from 10⁴ to 10⁸; ψ_P − x changes sign inside the bins (zero-driven oscillation, not a secondary main term).

**Extension to X = 10⁹, ρ = 0.8** (`logs/big/S5_r0.8_1e9.log`, 17 s, max a_n = 276, no saturation): windows [10^k, 10⁹], k = 3, 4, 5, 6:
b_sup = 0.305, 0.299, 0.297, 0.307; b_rms = 0.190, 0.175, 0.166, 0.163; a_sup = 0.730, 0.737, 0.751, 0.759; sup|E| = 274.8,
sup|ψ − x| = 7.35·10⁵ at the top. **So α ≈ 0.74–0.76 and β ≈ 0.30 over six decades: α − max{½, 2β} ≈ 0.14 — the brief's stop condition
("α > max{½, 2β} + 0.05 numerically over two decades") is met.** Route 2 for α (zeros of ζ_P) is §2.1.

## §3. The ladder and the other designs

**3.1 Rung 1 (over F_q) — what it teaches** [quoted + proved here]. For a Beurling system over F_q (norms q^n) the integer count A_n is
an integer sequence and "β" degenerates: for every genuine curve A_n = h(q^{n−g+1} − 1)/(q − 1) exactly for n > 2g − 2 (Riemann–Roch),
and Weil gives α = ½ — so U's analog holds for curves and is RH itself. The virtual curve V (fr/NOTE §5.4: Z = (1 − 5u + 5u²)/((1 − u)(1 − 5u)),
A_n = (5^n − 1)/4 exactly, zeros at Re s = 0.79899) has perfect regularity and RH false: U's analog FAILS on rung 1 as soon as geometry
(Castelnuovo/Hodge index) is dropped. Lesson recorded before §2 was run: integer regularity alone never confines zeros on rung 1; a line
α ≤ 2β over ℚ could only come from the archimedean continuum of norms (a "square-root price" paid by integers that move by real amounts).
§2 is the ℚ-analog of V: an ℕ-supported system with near-regular integers and zeros off the line, built by choosing the primes to fit the
integers (V is built the same way: b_d ≥ 0 closed points fitted to the prescribed A_n).

**3.2 Design (i) in tracking form is forbidden in print (S1)** [quoted; corollary proved here]. Hilberdink 2005 (w-18a, JNT 112), Remark C
(text l. 496–500, p. 340): "for an [α, β]-system with β < α, if ζ_P(s) has finitely many zeros for σ > η with η ∈ (β, α), then η ≥ ½"
(via Remark B(ii), l. 228–232: finitely many zeros ⇒ ζ_P and ζ′_P/ζ_P of zero order there). *Corollary.* Let R be a rational template
(finitely many zeros) and Q a discrete system with Π_Q(x) − Π_R(x) = O(x^{a}), a < ½. Then log(ζ_Q/R) = ∫x^{−s}d(Π_Q − Π_R) is analytic in
σ > a, so ζ_Q has exactly R's zeros in σ > a — finitely many — and Remark C forces β(Q) ≥ ½. *Proof.* If β(Q) < ½, pick η ∈ (max(β, a), ½);
ζ_Q has finitely many zeros in σ > η; Remark C gives η ≥ ½, contradiction. ∎ So S1 (greedy discretization with |Π_Q − Π_R| ≤ ½, a = 0)
of the planted template R₀ — whose density [1 + u^{2β₀−2} − 2u^{β₀−1}cos(γ₀ log u)]/log u = |1 − u^{β₀−1+iγ₀}|²/log u ≥ 0 makes it a
legitimate continuous system with α = β₀ — has β ≥ ½: consistent with U, and it is BDR's p. 4 heuristic (z-02 l. 171–179, derived there
from Hilberdink for the template s/(s − 1)) made a theorem for every rational template. Design (i) can only escape through a ≥ ½: random
selection (S2, the Diamond–Zhang rung: β = ½, the sibling unit `results/dz-half-s39/`) or a structured, ζ-like prime discrepancy.
Not run numerically: the printed theorem settles S1, and S2 is the sibling unit's object.

**3.3 Design (ii) in periodic form is a number field, or crosses U only through an off-line Dirichlet zero (S3 periodic)** [proved here].
Let P be supported on ℕ with m_{p,1} = F(p mod q) for p ∤ q (F: (ℤ/q)^× → ℤ_{≥0}), and write F = Σ_χ c_χ χ, so c_{χ₀} = 1 (simple pole)
and log ζ_P(s) = Σ_χ c_χ log L(s, χ) + h(s), h analytic in σ > ½ (the prime-square and higher terms converge absolutely there).
(a) Every zero or singularity of ζ_P in σ > ½ is a zero of some L(s, χ) with c_χ ≠ 0 (e^{h} ≠ 0). Hence **a zero of ζ_P with Re s > ½ is an
off-line zero of a Dirichlet L-function mod q**, and a U-crossing in this class planted by a zero needs an L-zero with Re > 2β(P). (b) If moreover c_χ ∈ ℤ_{≥0} for all χ (the
case without branch points), then F = [G : H]·1_H for a subgroup H of G = (ℤ/q)^×, i.e. P is the ideal system of the abelian field
fixed by H up to factors analytic in σ > ½. *Proof of (b).* Σ_a F(a) = |G|c_{χ₀} = |G|, Σ_a F(a)² = |G|Σ_χ c_χ² (Parseval), and F(a) ≤
F(1) = Σ_χ c_χ (positive-definite), so |G|Σc_χ² = ΣF² ≤ F(1)ΣF = |G|Σ c_χ. With c_χ ∈ ℤ_{≥0} this forces c_χ ∈ {0, 1} and equality
F(a)² = F(1)F(a), i.e. F ∈ {0, F(1)}; F = F(1)1_H with c_χ = (F(1)/|G|)Σ_{a∈H}χ̄(a) ∈ {0, 1}, which forces F(1) = |G|/|H| and every χ
with c_χ = 1 trivial on ⟨H⟩; counting such χ gives |⟨H⟩| ≤ |H|, so H is a subgroup. ∎ (Integrality of c_χ is what "no branch point at an
L-zero in σ > β" gives at each zero ρ: Σ_χ c_χ ord_ρ L(s, χ) ∈ ℤ; deducing c_χ ∈ ℤ needs a zero of L(s, χ) not shared with the other
L(s, χ′) mod q — recalled as known for a positive proportion of zeros, unverified here, so (b) is stated with integrality as hypothesis.)
So the periodic twisted class cannot cross U without an off-line Dirichlet zero; the class that crossed numerically (S5) is aperiodic.

**2.1 Route 2 for α: the zeros of ζ_P (ρ = 0.8)** [computed]. For an ℕ-supported system, ζ_P(s) − ρζ(s) = Σ_{n≥1}(a_n − ρ)n^{−s}, whose
partial sums C(y) = N(y) − ρ⌊y⌋ are O(y^{0.31}) on the data, so the series converges in σ > 0.31 and the truncation at X costs at most
|C(X)|X^{−σ} + |s|∫_X^∞|C(u)|u^{−σ−1}du. Instruments: `verify/zscan.c` (vertical lines by recurrence in t, horizontal segments by recurrence
in σ; ζ by Euler–Maclaurin, checked against mpmath at ½ + 14.13i), `verify/zcount.py` (argument principle on strips), `verify/zpoint.c` +
`verify/znewton.py` (Newton with ζ, ζ′ from mpmath). (a) Strip counts, X = 3·10⁷, t ∈ [0.1, 60] (`logs/zeros/r0.8_zcount_X3e7.log`):
one zero each in σ ∈ [0.60, 0.65], [0.65, 0.70], [0.75, 0.80]; none in [0.70, 0.75], [0.80, 1.10]. (b) Newton from 0.77 + 30.35i
(`logs/zeros/r0.8_newton_30_X3e7.log`, `…_Xconv.log`): the zero of the truncated function at X = 3·10⁷, 10⁸, 3·10⁸, 10⁹ is
0.7658596 + 30.3260636i, 0.7658709 + 30.3260583i, 0.7658696 + 30.3260661i, **ρ₁ = 0.7658722 + 30.3260650i** (|ζ′_P(ρ₁)| = 2.03): stable
to ~10⁻⁵ as X grows thirtyfold. So Re ρ₁ ≈ 0.766, matching route 1's α ≈ 0.74–0.76, and 2β ≈ 0.60 lies far below it. Other zeros near
0.66 + 40.75i and 0.62 + 42.95i (minima of |ζ_P| on the scanned lines).

