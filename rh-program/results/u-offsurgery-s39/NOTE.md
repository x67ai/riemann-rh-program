# NOTE — unit `u-offsurgery-s39`: Conjecture U off the surgery class — proposed discrete systems with α > ½, β < ½, and the attempt to refute U

Session 39, 2026-10-01. Writer: Opus 5.5 (agent). Status labels as in `novel-wave-s37/beurling-frontier/NOTE.md`: **[proved here]**,
**[computed]** (script + log in `verify/`), **[quoted]** (source under `sources/` or the named record file, page/line given),
**[recalled, unverified]** (never load-bearing), **[novelty: single-check]**.

Notation. A Beurling system P = (p_j) (discrete: point masses with positive integer multiplicities, dN ≥ 0, Λ_P ≥ 0).
[α, β]-system: ψ_P(x) = x + O(x^{α+ε}), N_P(x) = ρx + O(x^{β+ε}) for every ε > 0, for no ε < 0.
**Conjecture U** (fr/NOTE.md §7.2): every discrete [α, β]-system has α ≤ max{½, 2β}. Paths: `fr/` = `results/novel-wave-s37/beurling-frontier/`.

## §0. Close (filled last)

**STOP CONDITION MET — reported before proving (brief: "α > max{½, 2β} + 0.05 numerically over two decades").** The integer-greedy
systems S5(ρ) (§2: ℕ-supported, g-primes chosen at every integer so that N(n) tracks ρ(n − 1) + 1; at ρ = 0.8 ninety per cent of the
primes are refused and composites like 15, 26, 35 become g-primes) are discrete Beurling systems with **β ≈ 0.30 and α ≈ 0.75–0.77**:
route 1 (running sups, exact counts to 10⁹, generator re-derived independently with 0 mismatches to 10⁶) and route 2 (a zero
ρ₁ = 0.76587 + 30.32606i of ζ_P, stable to 10⁻⁵ from X = 3·10⁷ to 10⁹, winding number 1 on a box at X = 10⁹) agree; three systems
(ρ = 0.8, 0.95, 1.05) sit 0.10–0.19 above α = 2β over six decades, robust to the tie-break.
**Close: K-conditional + T + G.**
- **K′ (Theorem, §4):** if |N_P(u) − 0.8⌊u⌋| ≤ u^{0.35} for all u > 10⁹ (true with constant 0.59 at exponent 0.32 on [10³, 10⁹]),
  then Conjecture U is false. Not unconditional: the brief's K needs β by a proved bound (Lemma H) and a 30-digit zero (ρ₁ is known to
  ~5 digits; its digits are limited by the tail, not by arithmetic).
- **T (proved):** design (i) in tracking form has β ≥ ½ (§3.2, a corollary of Hilberdink 2005 Remark C, in print); design (ii) in
  periodic form is an abelian number field or crosses U only through an off-line Dirichlet zero (§3.3).
- **G:** the exact missing lemma is Lemma H, a growth bound for one explicit Lindley-type recursion; smallest undecided class:
  S5(ρ), ρ ∈ (0.5, 1.3).
Consequence for the record: read-F P2 ("no non-surgery discrete [α, β]-system with α > ½ and β < ½ is known") is answered numerically
by an explicit construction; DMV's p. 4 speculation (θ < ½ ⇒ RH for discrete systems) gets an explicit numerical counterexample;
BDR's populating conjecture in the corner β < α/2 gets numerical support. RH is untouched: U ⇒ RH, not conversely.

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

**2.2 Winding number at X = 10⁹, robustness, and two more systems at 10⁹** [computed]. (a) Box B = [0.7459, 0.7859] × [30.306, 30.346]
around ρ₁ (`verify/run_box_r08.sh`, `verify/zbox.py`, `logs/zeros/box30_winding.log`): the truncation F_X (X = 10⁹, every a_n computed) has
winding number +1.000000 on ∂B (164 points, largest phase step 0.052 rad), min_{∂B}|F_X| = 0.0394, and C(10⁹) = N(10⁹) − 0.8·10⁹ = 8.
Tail bound under the growth hypothesis H_θ: |C(u)| ≤ u^θ for all u > 10⁹ gives |ζ_P − F_X| ≤ |C(X)|X^{−σ} + |s|X^{θ−σ}/(σ − θ) ≤ 0.0105
(θ = 0.32; ratio 3.76), 0.0210 (θ = 0.35; ratio 1.88), 0.0423 (θ = 0.38; ratio 0.93 — fails). On the computed range H_0.32 holds with
room: max_{10³≤u≤10⁹}(|E(u)| + 1)/u^{0.32} = 0.59, and 0.32–0.38 in the top decade (`logs/big/S5_r0.8_Hcheck.log`).
(b) Different tie-breaks give different systems (target ρ(n − 1) + 1 + δ; `verify/run_S5_robust.sh`, `logs/S5_robust_fits_1e8.log`,
window [10⁴, 10⁸]): α − 2b = +0.17, +0.09, +0.09 (ρ = 0.8; δ = −0.3, 0.3, 0.45), +0.11, +0.02, +0.16 (ρ = 0.95), +0.19, +0.14, +0.02
(ρ = 1.05) — every variant on or above the line, seven of nine by ≥ 0.09.
(c) X = 10⁹ (`logs/big/S5_fits_1e9.log`), windows [10^k, 10⁹], k = 3..6: ρ = 1.05: b_sup 0.312, 0.295, 0.277, 0.278; a_sup 0.751,
0.761, 0.764, 0.742 (sup|E| = 475, sup|ψ − x| = 2.17·10⁶). ρ = 0.95: b_sup 0.287, 0.272, 0.269, 0.255; a_sup 0.678, 0.680, 0.687, 0.701.
So three distinct systems sit 0.10–0.19 above α = 2β over six decades.

**2.3 The pattern in the (α, β) scatter.** Across the sweep the integer exponent is pinned near β ≈ 0.25–0.33 for every density in
[0.6, 1.1] (it is set by the one-sided overshoot of the greedy rule, E ≥ −1 − ρ always), while α wanders over 0.58–0.77 with ρ: the
scatter is horizontal, not along α = 2β. Densities ≥ 1.2 raise β (composites crowd the rule), and ρ ≥ √2 runs away (β = α = 1).
Quantitatively ψ_P − x ≈ −2Re(x^{ρ₁}/ρ₁) + …: amplitude 2x^{0.766}/30.3 = 5.1·10⁵ at 10⁹ against the observed 7.35·10⁵ — routes 1 and 2
for α agree.

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

## §4. What is proved: U reduces to one explicit growth bound

**Theorem K′ (conditional refutation of U)** [proved here, modulo the floating-point evaluation of F_X on ∂B recorded in §2.2(a)].
Let P = S5(0.8) (§2, δ = 0) and C(u) = N_P(u) − 0.8⌊u⌋. If (H_θ) |C(u)| ≤ u^θ for all u > 10⁹ holds for some θ ≤ 0.35, then ζ_P has
exactly one zero ρ₁ in B = [0.7459, 0.7859] × [30.306, 30.346], P is an [α, β]-system with α ≥ 0.7459 and β ≤ θ, and **Conjecture U
is false** (α ≥ 0.7459 > 0.70 ≥ 2β, and α > ½).
*Proof.* (1) Under H_θ, Σ_n(a_n − 0.8)n^{−s} has partial sums C(y) = O(y^θ), so it converges in σ > θ and ζ_P = F_X + T_X there, F_X := 0.8ζ + Σ_{n≤X}(a_n − 0.8)n^{−s},
with |T_X(s)| ≤ |C(X)|X^{−σ} + |s|∫_X^∞ u^{θ−σ−1}du = |C(X)|X^{−σ} + |s|X^{θ−σ}/(σ − θ) by partial summation. (2) On ∂B, |T_X| ≤ 0.0210 <
0.0394 ≤ |F_X| (§2.2(a)), so by Rouché ζ_P and F_X have the same number of zeros in B, namely the winding number 1. (3) N_P(x) − 0.8x =
C(x) − 0.8{x} = O(x^θ) gives β ≤ θ. (4) ψ_P(x) − x ≠ O(x^{σ}) for σ < Re ρ₁: otherwise −ζ′_P/ζ_P − s/(s − 1) = s∫(ψ_P − x)x^{−s−1}dx would be
analytic at ρ₁, but ζ_P(ρ₁) = 0 makes it a pole (fr/NOTE Prop. 2.1's argument). So α ≥ Re ρ₁ ≥ 0.7459. ∎
Whether α < 1 is not needed (the definition allows α = 1, as for the Diamond–Zhang [1, β₀]-system): U fails for every α ≥ 0.7459.
The data point to α ≈ 0.77 (no zero in [0.80, 1.10] × [0.1, 60], §2.1(a); a_sup ≈ 0.74–0.76 at 10⁹).

**G (the exact missing lemma).** *Lemma H.* For the deterministic sequence a_n of S5(0.8), sup_{u≤x}|N_P(u) − 0.8⌊u⌋| ≪ x^{0.35}.
It is a statement about one explicit Lindley-type recursion, E(n) = max{E(n − 1) + A(n) − ρ, r_n} with r_n ∈ [−ρ − 1, 0] the rounding
floor and A(n) the number of representations of n by the system's own earlier g-primes: the upward excursions of E are the bursts of
composites, absorbed at the rate of the refused primes. Verified on [10³, 10⁹] with constant 0.59 at θ = 0.32 (§2.2(a)); the data give
θ ≈ 0.30 (b_sup over six decades). Smallest undecided class: the integer-greedy systems S5(ρ), ρ ∈ (0.5, 1.3) — every one measured sits
on or above U's line; U holds or fails exactly as Lemma H (with any θ < Re ρ₁/2, given a zero ρ₁ certified as in §2.2) holds or fails
for one of them. Note the logical position: U implies RH, but U's failure says nothing about RH — S5 is a "virtual ℕ" (§3.1).

## §5. Prior art at the page, novelty, distance from upstream

- Hilberdink 2005 (fr/sources/w-18a): Thm 1 max{α, β} ≥ ½ (l. 195); Cor. 2(b) (l. 207–209): β < ½ ⇒ infinitely many zeros in every strip
  {η′ < σ < 1}, η′ ∈ (β, ½); Remark C (l. 496–500). S5 obeys all of them (α ≈ 0.77 > ½; ζ_P carries infinitely many zeros, the
  strip counts of §2.1 show three in σ ≥ 0.6 below height 60). Remark C is what kills design (i) in tracking form (§3.2).
- BDR 2309.01567v2 (fr/sources/z-02): the populating conjecture (l. 84–86) "for all α, β with max{α, β} ≥ 1/2, there must exist a
  corresponding [α, β]-system"; p. 4 (l. 171–181) "any method for approximating systems … which yields O(x^θ) control on either Π_P(x)
  or N_P(x), where θ < 1/2, should have an uncertainty of size at least x^{1/2−ε} … on the other"; "Instead of creating new systems from
  scratch, we will modify the classical system". S5 creates a system from scratch at the integer level; its prime uncertainty x^{0.77}
  is ≥ x^{½}, as their heuristic requires. Their Thm 1.3 (RH) needs β ≥ 2α/(α + 2) ≈ 0.55 at α = 0.77; S5 has β ≈ 0.30.
- DMV, Math. Ann. 334 (2006) p. 4 (fr/sources/p1-02 l. 203–207): "it may still be the case that (3) with θ < 1/2 does imply RH for discrete
  Beurling generalized numbers" — S5(0.8) is an explicit numerical counterexample (θ ≈ 0.30, zero at 0.766).
- Révész–Pintz arXiv:2407.12746 (abstract, `sources/abstracts-related.txt`): Carlson-type zero-density estimates for Beurling ζ with
  integers in ℕ and the Ramanujan condition — exactly S5's class; density theorems allow sparse zeros in (½, 1), no conflict.
- Broucke–Vindas 2102.08478 (fr/sources/z-18): random discretization of a target F; Diamond–Zhang Ch. 17 (fe/sources/t-50): Bernoulli
  selection, β = ½ for the random rung (sibling `results/dz-half-s39/`). Neither builds a system by integer-level feedback.
- Hilberdink 2012 (fr/sources/p3-22c2, abstract l. 30–40): N(x) − cx periodic ⇒ ℙ minus finitely many primes. S5's error is not
  periodic (it grows like x^{0.3}); the theorem does not reach it.
- arXiv sweeps on disk (fr/sources/arxiv-search-*.xml, 228 abstracts; read-O's 2026-10-01 sweep): no greedy, feedback, or
  integer-level construction of Beurling systems; a fresh API query from this unit was rate-limited ("Rate exceeded"), retried with a
  one-minute backoff, still rate-limited, and stopped (to spare the shared limit); the on-disk sweeps are the gate.
- **Novelty: single-check.** S5 as a construction, the numerical crossing, Theorem K′, Lemma H as the reduction; §3.2 is a direct
  corollary of a printed remark; §3.3(b) is a Parseval argument and may be classical.
- **Distance from upstream (10(n)).** Every proved statement here uses one printed input (Hilberdink's Remark C) or none; the crossing
  itself is the unit's own construction and computation, with no printed system nearer than BDR region III (RH-conditional, surgery).

## §6. Instruments rows (shape of `directions/B2-refutation-program.md`; records, never ranks; not applied — for the digest)

| Quantity | Current best value | Result file | Dated |
|---|---|---|---|
| (α, β) of the integer-greedy ℕ-supported system S5(ρ) (numerically the first non-surgery discrete system with α > ½, β < ½ on the record; numerical, not proved) | ρ = 0.8, X = 10⁹: β ≈ 0.30 (running sup of \|E\|, windows 10³…10⁶ → 10⁹: 0.305, 0.299, 0.297, 0.307), α ≈ 0.73–0.76 (running sup of \|ψ − x\|); ρ = 1.05: 0.28–0.31 / 0.74–0.76; ρ = 0.95: 0.26–0.29 / 0.68–0.70; α − 2β = +0.10…+0.19 over six decades; 19-density sweep at 10⁸; tie-break variants all on or above α = 2β. One producer; generator re-derived independently (0 mismatches to 10⁶) | `u-offsurgery-s39/NOTE.md` §2; `u-offsurgery-s39/verify/logs/big/S5_fits_1e9.log`, `…/S5_sweep_fits_1e8.log`, `…/S5_robust_fits_1e8.log` | 2026-10-01 |
| Off-line zero of S5(0.8)'s ζ_P (route 2 for α; the zero behind Theorem K′) | ρ₁ = 0.76587 + 30.32606i (Newton at X = 3·10⁷ … 10⁹, stable to 10⁻⁵; \|ζ′_P(ρ₁)\| = 2.03); winding number 1 on B = [0.7459, 0.7859] × [30.306, 30.346] at X = 10⁹, min\|F_X\| = 0.0394 against tail ≤ 0.021 under H_0.35; strip counts to height 60: zeros in σ ∈ [0.60, 0.65], [0.65, 0.70], [0.75, 0.80]. One producer | `u-offsurgery-s39/NOTE.md` §2.1–2.2; `…/verify/logs/zeros/box30_winding.log`, `…/r0.8_newton_30_Xconv.log`, `…/r0.8_zcount_X3e7.log` | 2026-10-01 |

## §7. Untried (format of the directions' lists)

- **UT-U1 Prove Lemma H** for S5(0.8): sup_{u≤x}|N(u) − 0.8⌊u⌋| ≪ x^{0.35} (with Theorem K′ it refutes U). First rung: the Lindley
  recursion E(n) = max{E(n − 1) + A(n) − ρ, r_n}, bounding the burst sizes of A over windows by the system's own prime counts. Target: B2.
- **UT-U2 The 30-digit zero.** Certify ρ₁ by interval arithmetic (python-flint arb) on ∂B with the 10⁹-term sum split into exact blocks;
  digits beyond ~6 need a tail theorem (Lemma H), not more arithmetic. Target: B2.
- **UT-U3 Why β ≈ 0.3.** The scatter is horizontal (§2.3): explain the universal overshoot exponent of the greedy rule and whether a
  smarter controller (look-ahead, real-valued g-primes) lowers β toward 0 while keeping a zero at 0.77 — the "virtual ℕ" question:
  does a discrete system with N(x) = ρx + O(x^ε) and an off-line zero exist? Target: B2, C2.
- **UT-U4 S3 and S4 (not run).** The planted pseudo-character twist (ζ_P = ζ·L_target·e^{R̃}, R̃ analytic in σ > 0, §1) and the quadratic
  base with sparse planted flips — the heuristic (R̃ random-like of size t^{½−σ} in σ < ½) predicts β ≥ ½ for S3; untested. Target: B2.
- **UT-U5 What survives of U.** Conjecture O (surgery class) is untouched by S5. Candidate replacements: U restricted to Euler products
  over the rational primes with periodic or automorphic local data (§3.3 shows the periodic case is a GRH statement). Target: B2.

## §8. Waste line (10(o))

Spent: the S1/S2 numerics were planned and dropped once Remark C settled S1 in print (no compute lost); the first S5 driver lost one
run to zsh's lack of word splitting (two seconds, re-run under bash). Found: the stop condition. Not done because of the stop rule: S3,
S4 numerics, a 30-digit certification, a proof attempt of Lemma H.
