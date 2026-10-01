# SHARED — unit `local-greedy-s40` (S7: integer-level feedback acting only at prime powers)

Dated blocks, appended as work lands (machine clock, IST). Writer: Opus 5.5 agent.

## 2026-10-01 11:29 IST — start
Read at the line: BRIEF.md; fr/NOTE.md §7 (Conjecture U); u-offsurgery-s39/NOTE.md §0–§8 (S5 definition §2, periodic class §3.3,
Theorem K′ §4, Lemma H); free-greedy-s40/CHARTER.md §0 (S5's error = largest multiplicity). Machine: Apple M4 (arm64: `long double`
is `double`, so all long sums use compensated double-double accumulation). Plan: segmented multiplicative generator `verify/s7gen.c`
(exact integer rule; a_n = product of local coefficients c_p(e); no full-length array needed), controls, then the sweep.

## 2026-10-01 11:42 IST — generator built and controlled; sweep at 10⁸ [computed]
`verify/s7gen.c` (segmented, multiplicative, exact int128 rule) and the independent `verify/s7dp.c` (additive DP over multiples,
no multiplicativity used). Controls (`verify/logs/check_s7_1e7.log`, `logs/controls/`): ρ = 1 returns the 664,579 primes ≤ 10⁷,
E ≡ 0; a_n identical term by term (0 mismatches over n ≤ 10⁷) between the two generators at ρ = 0.8, 1.5, 1; multiplicativity
a(mn) = a(m)a(n) on 10⁶ random coprime pairs: 0 failures; Σ_{d|n} g(d) = a_n for n ≤ 10⁵: 0 mismatches.
**Anatomy (new, unexpected):** the local multiplicities do NOT stay small. At ρ = 0.8, X = 10⁸: 4,808,005 of 5,761,455 primes are
refused (m_p = 0), the rest get m_p up to 78 (= |inf E|), mean m_p = 1.000 per decade; a_n reaches 144, a_n > d(n) for 2.8·10⁶ n.
Mechanism: between prime powers E drifts down at rate ρ wherever a_n = 0 and the rule refills the whole deficit at the next prime.
Sweep at 10⁸ (`logs/sweep/fits_v0_1e8.log`; windows [10^k, 10⁸)): b_sup / a_sup = ρ 0.6: 0.29–0.33 / 0.78–0.80; 0.75: 0.26–0.35 /
0.68–0.79; 0.8: 0.31–0.38 / 0.54–0.73; 0.9: 0.26–0.39 / 0.67–0.73; 1.1: 0.20–0.46 / 0.75–0.81; 1.25: 0.42–0.52 / 0.80–0.83;
1.5: runaway (N(10⁸)/10⁸ = 1.510, b ≈ 0.9). **Face-value a − 2b is +0.1…+0.2 at ρ = 0.6, 0.75, 0.9 on windows from 10⁵ — the
K-trigger region — but this is 10⁸, not the contracted 10⁹, and route 1 alone (a random walk with growing step size also gives
a_sup > ½).** Next: 10⁹ for six densities, 4·10⁹ for two, then route 2 (zeros).
