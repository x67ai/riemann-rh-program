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

