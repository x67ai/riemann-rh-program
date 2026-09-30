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

