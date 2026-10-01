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

## 2026-10-01 11:49 IST — STOP LINE (c) MET ON ROUTE 1 AT 10⁹ — reported before any proof attempt [computed]
`verify/logs/sweep/s7_v0_r*_X1000000000.log`, fits by `verify/fit7.py` (running sups over windows [10^k, 10⁹)), k = 3…7:
- ρ = 0.6: b_sup = 0.315, 0.303, 0.281, 0.278, 0.264; a_sup = 0.794, 0.801, 0.802, 0.811, 0.808 → **a − 2b = +0.16, +0.20, +0.24, +0.26,
  +0.28** (sup|E| = 948.8, inf E = −93.2, sup|ψ_P − x| = 5.57·10⁶ by 10⁹).
- ρ = 0.75: a − 2b = +0.05, +0.10, +0.18, +0.24, +0.31; ρ = 0.8: +0.01, +0.07, +0.12, +0.09, +0.14; ρ = 0.9: −0.03, +0.02, +0.09, +0.17, +0.16.
So "α > max{½, 2β} + 0.05 numerically over two decades" holds on route 1 for ρ = 0.6 on every window, and for 0.75 from 10⁴.
Caveat recorded now: route 1 for α is a running-sup slope; a random walk Σ(m_p − 1)log p with growing step variance would also give
a_sup > ½. Route 2 (zeros of F_X, stable under X) decides whether the excess is zero-driven. Doing route 2 at ρ = 0.6 next, then
4·10⁹; variants and the long theory are deferred by the stop rule.

## 2026-10-01 11:59 IST — route 2 at ρ = 0.6: two zeros of F_X with real part > 0.8, stable under X [computed]
`verify/zline.c` (F_X = ρζ + Σ_{n≤X}(a_n − ρ)n^{−s}, adapted from uo/verify/zscan.c), `verify/newton7.py`; logs
`verify/logs/zeros/newton_r06_X1e7.log`, `…_X1e8.log`. Newton (mpmath ζ, ζ′; D_X, D_X′ in C) from minima of |F_X| on the σ = 0.80
scan line: X = 10⁷: 0.8209861 + 11.0877395i (|F′| = 3.41), 0.8052896 + 20.2491013i (|F′| = 4.41); X = 10⁸: **0.8210037 + 11.0877501i,
0.8052939 + 20.2490886i** (moves 2·10⁻⁵, 4·10⁻⁶). Amplitude check: 2x^{0.821}/11.1 + 2x^{0.805}/20.3 ≈ 6·10⁶ at 10⁹ against the observed
sup|ψ_P − x| = 5.57·10⁶. So route 1's α ≈ 0.80 is zero-driven, and 2β ≈ 0.53–0.63. Full argument-principle scan at 10⁷ running;
then Newton at 10⁹, a winding-number box with the K′-type tail bound, and 4·10⁹.

## 2026-10-01 12:08 IST — zeros at X = 10⁹ and strip counts [computed]
Newton at X = 10⁹ (`verify/logs/zeros/newton_r06_X1e9.log`): **ρ₁ = 0.8209965 + 11.0877411i (|F′| = 3.412), ρ₂ = 0.8052963 + 20.2490762i
(|F′| = 4.406)**; moves 10⁸ → 10⁹: 1.2·10⁻⁵ and 1.3·10⁻⁵. Argument principle at X = 10⁷ on [0.55, 1.10] × [0.1, 100]
(`logs/zeros/zcount_r06_1e7.log`): strips σ ≥ 0.85 and [0.70, 0.80] contain no zero (phase steps ≤ 1.6 rad); [0.80, 0.85] contains
exactly ρ₁, ρ₂; [0.55, 0.70] counts 27 (phase steps up to 2.95 rad — indicative only). So the largest real part below height 100 is
0.8210, and route 2 agrees with route 1 (a_sup = 0.79–0.81). Running now: H_θ check, winding-number boxes at 10⁹ (Taylor moments,
validated at the corners by direct sums), the 4·10⁹ run (with Beurling Möbius sums M_P: Neamah–Hilberdink Thm 1 predicts γ = α).

## 2026-10-01 12:15 IST — certificates, H-check, 4·10⁹, third route (Möbius sums) [computed]
- Winding-number boxes at X = 10⁹ (Taylor moments, corners checked by direct sums to 1.8·10⁻¹²; `logs/zeros/cert_r06_z*_1e9.log`):
  B₁ = [0.8010, 0.8410] × [11.0677, 11.1077]: winding 1, min|F_X| = 0.0654, tail bound under H_0.40 = 0.00683 (ratio 9.6);
  B₂ = [0.7853, 0.8253] × [20.2291, 20.2691]: winding 1, min|F_X| = 0.0838, tail under H_0.40 = 0.0179 (ratio 4.7).
- **Theorem K₇ (NOTE §4): if |N(u) − 0.6⌊u⌋| ≤ u^{0.40} for all u > 10⁹, Conjecture U is false** (α ≥ 0.8010 > 2·0.40).
  H-check (`logs/zeros/hcheck_r06_1e9.log`): max|C(n)|/n^{0.40} per decade = 1.05, 0.86, 0.93, 0.60, 0.45, 0.35 (k = 3…8).
- X = 4·10⁹ (`logs/sweep/s7_v0_r3-5_X4000000000.log`, 1.17 GB, ~4 min): sup E = 1304.4, inf E = −105.6, sup|ψ_P − x| = 1.75·10⁷;
  b_sup over [10^k, 4·10⁹), k = 3…7: .307 .295 .276 .272 .259 (still falling); a_sup: .796 .802 .803 .810 .807.
- Third route: Beurling Möbius sums M_P (μ_P = a^{∗−1}; control: M(10⁶) = 212 at ρ = 1, independent numpy sieve): sup|M_P| = 4.37·10⁶
  by 4·10⁹; exponent γ = .795 .808 .807 .814 .817 — Neamah–Hilberdink Thm 1 (two largest of α, β, γ equal) predicts γ = α: it is.

## 2026-10-01 12:30 IST — route 2 at three more densities [computed]
Scans of F_X at X = 10⁷ on [0.70, 1.00] × [0.1, 100] (`logs/zeros/zcount_r075_1e7.log`, `…_r08_…`, `…_r11_…`), zeros located by
`verify/zmap.py` and refined by Newton at X = 10⁸ (`logs/zeros/newton_r*_X1e8.log`; moves 10⁷ → 10⁸ ≤ 1.1·10⁻⁴):
- ρ = 0.75: counts 3 / 1 / 0 in σ-strips [.70,.80] / [.80,.90] / [.90,1.0]; top zero **0.80563 + 92.34370i**; others 0.75449 + 46.69157i,
  0.72829 + 29.76598i, 0.70844 + 30.70061i.
- ρ = 0.8: counts 3 / 0 / 0; top zero **0.74647 + 30.69772i**; 0.74615 + 29.85767i, 0.73874 + 59.17205i.
- ρ = 1.1: counts 6 / 2 / 0; top zero **0.83989 + 20.33964i**; 0.81395 + 29.98087i.
Route 2 tracks route 1 (a_sup at 10⁹: 0.72–0.84, 0.69–0.72, 0.79–0.80). With b_sup at 10⁹ the crossing margins α − 2β are
+0.14…+0.28 (0.75), +0.04…+0.19 (0.8, marginal on early windows), +0.01…+0.36 (1.1, window-dependent). ρ = 0.6 stays the clearest case.

## 2026-10-01 12:33 IST — the capped variant S7^{≤2}(0.6) (m_n ≤ 2): tame AND across the line on route 1 [computed]
Run to settle the K-close's "tame multiplicities" clause (brief task 4, one variant; the others stay unrun under the stop rule).
`verify/logs/sweep/s7_v2_r3-5_X1000000000.log`, `fits_v2_r06_1e9.log`: m_p ∈ {0, 1, 2} (24.6M refused, 1.7M single, 24.5M doubled
below 10⁹ — a pseudo-quadratic-field local structure), max a_n = 72, a_n > d(n) for only 15,033 n ≤ 10⁹ (max a_n/d(n) = 2.5);
**sup E = 218.4, inf E = −197.8; b_sup (k = 3…7) = .215 .207 .204 .204 .192; a_sup = .794 .804 .804 .806 .827 → a − 2b = +.36…+.44.**
Bounded local multiplicities give a_n ≪ n^ε (the Ramanujan condition of Révész–Pintz's class; proof in NOTE §4). Next: route 2
for this variant (dump to 10⁹, scan, Newton, box), then the close.

## 2026-10-01 12:47 IST — S7^{≤2}(0.6), route 2: the K-candidate with tame multiplicities [computed + proved]
Scan at X = 10⁷ on [0.70, 1.00] × [0.1, 100] (`logs/zeros/zcount_v2r06_1e7.log`): exactly 2 zeros (σ ≥ 0.90: none). Newton
(`logs/zeros/newton_v2r06_X1e{7,8,9}.log`): **z₁ = 0.8243658 + 11.0306646i (|F′| = 3.617), z₂ = 0.7665284 + 20.2045626i**, stable to
9·10⁻⁶ from 10⁷ to 10⁹ — close to the uncapped system's ρ₁, ρ₂ (the two systems share their early decisions). Box at 10⁹
(`logs/zeros/cert_v2r06_z1_1e9.log`): B = [0.8044, 0.8444] × [11.0107, 11.0507], winding 1, min|F_X| = 0.0692, tail under H_0.40 =
0.00629 (ratio 11.0). H-check (`logs/zeros/hcheck_v2r06_1e9.log`): max|C(n)|/n^{0.40} per decade = 0.93, 0.52, 0.34, 0.21, 0.15,
**0.10** (k = 3…8) — H_0.40 holds on the whole computed range [10³, 10⁹]. Möbius route: γ = 0.78–0.82.
**Theorem K₇^{≤2} (NOTE §4.2): if |N(u) − 0.6⌊u⌋| ≤ u^{0.40} for all u > 10⁹, U is false — for a system with a_n ≪ n^ε (Lemma 4.1).**
