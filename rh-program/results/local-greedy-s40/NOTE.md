# NOTE — unit `local-greedy-s40`: S7, integer-level feedback acting only at prime powers (the prime-local class on ℕ)

Session 40, 2026-10-01. Writer: Opus 5.5 (agent). Labels as in `u-offsurgery-s39/NOTE.md`: **[proved here]**, **[computed]** (script +
log under `verify/`), **[quoted]** (source on disk, page/line), **[recalled, unverified]** (never load-bearing), **[novelty: single-check]**.
Notation as there: [α, β]-system: ψ_P(x) = x + O(x^{α+ε}), N_P(x) = ρx + O(x^{β+ε}). **Conjecture U** (fr/NOTE §7.2): every discrete
[α, β]-system has α ≤ max{½, 2β}. Paths: `fr/` = `results/novel-wave-s37/beurling-frontier/`, `uo/` = `results/u-offsurgery-s39/`.

## §0. Close (filled last)

(pending)

## §1. The object, the generator, the controls

**Definition (BRIEF).** Fix ρ > 0. Walk n = 2, 3, …; A(n) = number of representations of n by the g-primes chosen so far; if n = p^k
is a prime power, m_n := max(0, ⌊ρ(n − 1) + 1 − N(n − 1) − A(n) + ½⌋) copies of n become g-primes; otherwise m_n := 0;
a_n = A(n) + m_n, N(n) = N(n − 1) + a_n. Write E(n) := N(n) − ρ(n − 1) − 1 (sup of N(x) − ρx − (1 − ρ) over [n, n + 1) is E(n), the
inf is E(n) − ρ), C(y) := N(y) − ρ⌊y⌋.

**Lemma 1.1 (structure)** [proved here]. Every g-prime is a prime power, so a_n = Π_{p^e‖n} c_p(e) with c_p(e) = [u^e] F_p(u),
F_p(u) = Π_{k≥1}(1 − u^k)^{−m_{p^k}}; a is multiplicative, ζ_P(s) = Σ a_n n^{−s} = Π_p F_p(p^{−s}) = ζ(s)L_g(s) for σ > 1, where
g = μ ∗ a is multiplicative with g(p^e) = c_p(e) − c_p(e − 1), g(p) = m_p − 1 ∈ {−1, 0, 1, …}.
*Proof.* A product of g-primes p₁^{k₁}⋯ (prime powers) equals n iff, for each prime p, the g-primes that are powers of p multiply to
the p-part of n; representations therefore factor over p, and the number of ways to write p^e as an unordered product of the
chosen powers of p (with multiplicities m_{p^k}) is [u^e]Π_k(1 − u^k)^{−m_{p^k}}. The Euler product converges absolutely for
σ > 1 because N(x) = ρx + o(x) on the data (§2) — as a statement for all x this is part of the system's definition as a density-ρ
system, not proved. g = μ ∗ a has local factor (1 − u)F_p(u). ∎

**Lemma 1.2 (the downward side is bounded by prime-power gaps)** [proved here]. After every prime-power step, E(q) > −½; for
consecutive prime powers q < q′ and q ≤ n < q′, E(n) > −½ − ρ(n − q); hence inf_{x≤X}(N(x) − ρx − (1 − ρ)) > −½ − ρ·G(X) with G(X)
the largest gap between consecutive prime powers up to X, and every multiplicity satisfies m_q < ρ + 1 + ρ·G(q).
*Proof.* Put y := ρ − E(q − 1) − A(q) + ½, so m_q = max(0, ⌊y⌋) and E(q) = E(q − 1) + A(q) + m_q − ρ = ½ − y + m_q. If ⌊y⌋ ≥ 1
then E(q) = ½ − {y} ∈ (−½, ½]; otherwise y < 1 and E(q) = ½ − y > −½. Between prime powers a_n ≥ 0, so E decreases by at most ρ per
step. Finally m_q ≤ y ≤ ρ + ½ − E(q − 1) (as A(q) ≥ 0) < ρ + 1 + ρ(q − 1 − q_prev), q_prev the previous prime power. ∎
(The unconditional size of G(X) is a printed gap theorem I have not opened: **[recalled, unverified]** G(X) ≪ X^{0.525}; Cramér's
conjecture would give log²X. On the data, max m_p = 79 at ρ = 0.6, X = 10⁹, against ρ·(max prime gap below 10⁹) — the gap itself
[recalled, unverified] 282 — the rule fills deficits well before the worst gap.)

**Generator** [computed]. `verify/s7gen.c`: segmented over [L, R) with R − L ≤ L, so every composite non-prime-power n in a segment
has all prime-power factors ≤ n/2 < L, already decided; prime powers in the segment are decided in increasing order (A(p^e) =
c_p^{old}(e) needs only m_{p^k}, k < e). Exact integer arithmetic for the rule: ρ = num/den, the floor computed in int128 as
⌊(2num(n − 1) + 2den(1 − N − A) + den)/(2den)⌋. **Irrational ρ** is not used here (the brief's densities are rational); the generator
takes num/den up to 10¹⁸, so an irrational ρ is run through a continued-fraction convergent p/q, and the run equals the true S7(ρ)
up to X unless some ρ(n − 1) + ½ falls within X|ρ − p/q| of an integer — a condition the int128 arithmetic can check at each prime
power. Memory: one byte per odd q ≤ X/2 (m_q), segment arrays of 2²² entries; 387 MB at X = 10⁹; 50 s per 10⁹.
**Independent generator** `verify/s7dp.c`: the additive DP of S5's generator (`uo/verify-F/s5gen_F.c`) — "a[kq] += a[k], k
increasing" for each copy of each g-prime — with the rule allowed only at prime powers; no multiplicativity is used.

**Controls** (`verify/check_s7.py`, `verify/logs/check_s7_1e7.log`, `verify/logs/controls/`) [computed]: (a) ρ = 1 returns the 664,579
primes ≤ 10⁷ with E ≡ 0 (both generators); (b) a_n identical term by term over n ≤ 10⁷ between s7gen and s7dp at ρ = 0.8, 1.5, 1
(0 mismatches; N(10⁷), sup E, inf E, max a_n agree); (c) a(mn) = a(m)a(n) on 10⁶ random coprime pairs (m log-uniform): 0 failures;
(d) Σ_{d|n} g(d) = a_n for n ≤ 10⁵: 0 mismatches; (e) max a_n against d(n) at 10⁷, ρ = 0.8: max a_n = 72 at 5,825,921 (d = 4);
max a_n/d(n) = 23.5 at the prime 9,353,411 (m = 47); a_n > d(n) for 287,082 n ≤ 10⁷.

## §2. The numbers [computed]

Logs: `verify/logs/sweep/s7_v0_r<num>-<den>_X<X>.log` (20 log-bins per decade: sup/inf E over real x, RMS of E at integers,
sup|ψ_P − x|, max/min M_g, sup|Tt|, sup|W|; per-decade prime decisions; E records), fits `verify/fit7.py` →
`logs/sweep/fits_v0_1e8.log`, `fits_v0_1e9.log`; half-decade tables `logs/sweep/halfdecade_r06_r08_1e9.log`. Exponents are
least-squares slopes of log(running sup) against log x over the bins of [10^k, X); b from sup|E|, a from sup|ψ_P − x|, μ from sup|M_g|.

**2.1 X = 10⁹, six densities** (ρ = 1.5 runs away already at 10⁷: N(10⁸)/10⁸ = 1.5099, b ≈ 0.9 — not a density-ρ system on the range):

| ρ | sup E | inf E | sup\|ψ_P − x\| | sup\|M_g\| | max a_n | max m_p | b_sup, k = 3…7 | a_sup, k = 3…7 | a − 2b, k = 3…7 |
|---|---|---|---|---|---|---|---|---|---|
| 0.6 | 948.8 | −93.2 | 5.57·10⁶ | 9087 | 550 | 79 | .315 .303 .281 .278 .264 | .794 .801 .802 .811 .808 | **+.16 +.20 +.24 +.26 +.28** |
| 0.75 | 763.0 | −93.0 | 9.14·10⁵ | 9212 | 234 | 93 | .333 .316 .276 .261 .267 | .718 .734 .735 .760 .843 | +.05 +.10 +.18 +.24 +.31 |
| 0.8 | 1048 | −103.6 | 1.03·10⁶ | 11610 | 270 | 104 | .353 .329 .297 .296 .276 | .715 .723 .712 .685 .696 | +.01 +.07 +.12 +.09 +.14 |
| 0.9 | 969.8 | −106.2 | 7.17·10⁵ | 6596 | 247 | 102 | .366 .340 .307 .282 .287 | .704 .699 .707 .733 .736 | −.03 +.02 +.09 +.17 +.16 |
| 1.1 | 3839 | −174.4 | 3.68·10⁶ | 20270 | 825 | 142 | .416 .393 .337 .274 .240 | .796 .801 .791 .790 .787 | −.04 +.02 +.12 +.24 +.31 |
| 1.25 | 23000 | −219 | 1.05·10⁷ | 45230 | 1827 | 219 | .466 .451 .425 .426 .454 | .830 .828 .826 .815 .843 | −.10 −.07 −.02 −.04 −.07 |

RMS exponents b_rms (k = 3…7) at ρ = 0.6: .265 .243 .228 .217 .204; the M_g exponent μ ≈ 0.50–0.52 at every density ≤ 1.1.
Integer-error fits fall as the window starts later at every ρ ≤ 1.1 (no sign of a rising exponent on [10³, 10⁹]); α-fits are flat.

**2.2 Anatomy: refused, doubled, tripled** (decade [10⁸, 10⁹), 45,086,079 primes; `D 8` lines of the logs). Fractions with
m_p = 0 / 1 / 2 / 3 / ≥ 4: ρ = 0.6: .844 / .022 / .017 / .017 / .100; 0.75: .854 / .017 / .016 / .018 / .095; 0.8: .865 / .013 /
.016 / .014 / .093; 0.9: .868 / .011 / .018 / .012 / .092; 1.1: .912 / .004 / .009 / .004 / .071; 1.25: .940 / .001 / .003 / .003 /
.052. Mean m_p per decade = 1.000 ± 0.005 at every density (the density condition Σ(m_p − 1)/p ≈ 0 is met on average). Higher prime
powers with m > 0 in that decade: 134–288. The refused fraction RISES with x (ρ = 0.8: .80 in [10⁶, 10⁷), .865 in [10⁸, 10⁹)), so the
support of a thins like Π_{refused p ≤ x}(1 − 1/p) and the values on it grow: the system becomes lumpier with x — the opposite of
the brief's expectation that local multiplicities stay small. Lemma 1.2 caps them by ρ·(prime-power gap) + 1 + ρ.

**2.3 Where E's records come from** (`logs/sweep/s7_v0_r3-5_X1000000000_dump.log`, lines `rec`). Records of E at ρ = 0.6 are
reached at moderate a_n (10–150), in bursts (e.g. 424.2, 437.8, 462.8 at n = 35,885,294, …333, …338): E's excursions are clusters
of large-valued g-integers, not a single multiplicity (contrast S5, where sup E equals the largest a_n: free-greedy-s40/CHARTER §0).
sup E/max a_n = 1.7 at ρ = 0.6, X = 10⁹.

**2.4 The decomposition E = Tt + W − (1 − ρ)** (task 5(i); Tt(n) = n(Σ_{d≤n} g(d)/d − ρ), W(n) = −Σ_{d≤n} g(d){n/d}). Neither
dominates: both are of the size of M_g and cancel to leave E. At ρ = 0.6 on [3.16·10⁸, 10⁹): sup|Tt| = 9055, sup|W| = 8973,
RMS 3028 and 3027, against sup E = 948.8 and RMS(E) = 95.4. The RMS ratio Tt : E GROWS with x — 2.0, 3.6, 6.2, 13, 32 at the
half-decades starting 10⁴, 10⁵, 10⁶, 10⁷, 3.16·10⁸ (ρ = 0.6; ρ = 0.8 alike): the two terms grow like M_g, E much more slowly. So the hyperbola-type bound through M_g (§5) is far from sharp here: E ≈ x^{0.3} while M_g ≈ x^{0.5}.
