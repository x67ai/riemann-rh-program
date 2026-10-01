# SHARED — unit `s5-multiplicity-s40` (dated blocks, appended as work lands)

## 11:25 IST 2026-10-01 — block 1: start
Read BRIEF.md in full; read u-offsurgery-s39 NOTE.md (§2, §4, all), READ-O-SUPPLEMENT.md §C, verify-F/ (s5gen_F.c, factor_count.py,
ascent.py, anatomy_records.py, zero_taylor_F.log), the 1e9 generation log on /private/tmp/rh-s40-shared/s5/. Load at start: 3 heavy
processes (other agents) — under the limit of 4. Plan: task 1 (exact reproduction, own generator as second code path), task 2 (exact
counter in C with 128-bit counts, smarter search), task 4 (structure theorems), task 5 (carrier model), task 3 (extension, priced), task 6.

## 11:34 IST 2026-10-01 — block 2: task 1 done (C1, C3 reproduced exactly)
gp list SHA-256 matches; dump scan (`verify/dump_records.c`): sup E = 274.8 at 902538000 (a = 276, E(n−1) = −0.4), inf E = −0.4,
54% of n ≤ 10⁹ have a_n = 0. Exact counter `verify/fcount.c` (128-bit): self-tests 276/26 pass; C3 exact: 20390; 2932627 (the
20.20 integer, re-found by rerunning the orchestrator's greedy over primes ≤ 47); 13461378553. Second path (orchestrator's
Python-int DP) agrees on the two smaller. NOTE §1 written. Running: greedy ascent over the first 25 primes (full DP, double),
`logs/search_greedy_K25.log` — already exponent 0.3535 at log₁₀n = 33.4 (excess vs 3.76n^0.35: −0.46 in log₁₀), rates ≈ 0.39.
Finding: the one-large-prime split counter (`verify/fsplit.c`) loses a factor 4.7–150 — multi-large-prime g-primes matter.

## 11:46 IST 2026-10-01 — block 3: CLOSE K FOUND (stop line (b)); verified by two code paths
n_K = 2⁸·3⁵·5⁹·7³·11²·13·17·19³·23·29²·37·41²·59·61·79·89·109·149 (log₁₀ = 42.5774): a_{n_K} ≥ f_G(n_K) = 3,403,961,916,617,140
> 3.76·n_K^0.35 + 3 (ratio 1.1342; exact-integer test). fcert.c (128-bit) and checkK.py (numpy mod 3 primes, independent; list
membership and completeness verified against the dump) agree. Hence H_θ of Theorem K′ fails for all θ ≤ 0.35, all c < 1.88.
Not refuted: Lemma H with unspecified constant (fixed G gives only polylog growth). Search: `search2.c` (v_p-identity scoring),
log `logs/search2_rate_K60.log`. Next: independent re-verification of the dump itself (Ω-identity + rule check, §2.5), then T.

## 11:53 IST 2026-10-01 — block 4: dump certified independently; exact system to 2·10⁹
`omega_check.c`: Ω-identity (I) and rule (II) checked at every n ≤ 10⁹ — 0 failures each; induction ⇒ the dump is S5(0.8) on
[1, 10⁹] (NOTE §2.5), so the K certificate's 2,525 g-primes are genuine. Generator mode to 2·10⁹: N = 1,600,000,009, C = 9,
47,353,731 new g-primes, max a_n = 344 at 1,805,076,000 (= 2·902,538,000), sup E = 348.0 (NOTE §3). Next: T theorems (§4).

## 11:56 IST 2026-10-01 — block 5: §4 structure theorems written
T1 bounded a_n ⇔ free (with the quantitative relation bound); T2 free systems: K(x) ≤ R(x/2), π_P ≤ π, R(x) − R(x/2) ≤ π − π_P;
T3 free + Landau PNT (quoted, DMV pp. 2–3 l. 99–115) ⇒ refused primes and composites both O(x e^{−c√log x}), converse with
Σ_R p^{−θ} < ∞ via (ℙ∖R) ∪ {2p}; 4(b) Ramanujan examples ℙ ∪ {6}, ℙ ∪ {2p}, open question stated; T4 (Rankin-type lemma):
rank excess D among g-primes ≤ y ⇒ max f ≥ ½exp(D log(1/c) − …) at log x ≍ y; T4′: positive-proportion refusal + PNT ⇒
max a_n ≥ x^{κ/log log x} (divisor-function size, not a power). Next: §5 carriers/model, then §0 close.

## 11:58 IST 2026-10-01 — block 6: §5 carriers and model
Proved: E ≥ −0.4 always; hence m_n ∈ {0,1} and n is a g-prime iff A(n) = 0 and E(n − 1) ≤ 0.3. Data (`carriers.c`): composite
g-primes match refused primes per decade to 0.05%; c_ℓ(10⁹) ≈ 0.043·10⁹/ℓ for each of the first 30 refused ℓ; carrier
probability ≈ (1.6–1.8)/ln n among non-representable multiples. Model crossing of n^{0.383} for f_G (G ≤ 10⁹): 10⁶⁴–10⁸⁸ if the
marginal rate 0.40–0.42 persists. Next: §0 close, zoo line, Instruments, Untried, waste.

## 12:00 IST 2026-10-01 — block 7: NOTE complete (§0 close K + T, §6–§10)
§0 close written (K + T, model statements labeled); §6 prior art (one printed input: Landau PNT via DMV 2006); §7 Untried UT-M1…M5;
§8 three Instruments rows; §9 zoo rider BLOCK:i2 (not inserted); §10 waste line + candidate LOG line. Final checks next.

## 12:03 IST 2026-10-01 — block 8: final review done; unit closed (K + T)
NOTE re-read end to end; fixes: marginal-rate range 0.37–0.46 (measured), DP-check wording, converse construction needs R ⊆ odd
primes, T4′ error bound ½(e^{…} − ρ), U-threshold caveat (α = Re ρ₁ assumed rightmost), zoo-rider wording, waste times. Every count
cited has a log in verify/logs (tool_crosschecks.log added for §2.2). No processes left running. Scratch kept in
/private/tmp/rh-s40-s5mult/ (gbits.bin 125 MB, gp_ext_1e9_2e9.u32 379 MB, binaries).

## 14:45 IST 2026-10-01 — read-O block 1: Opus read started (Session 41)
Reader: Opus 5.5 under `results/novel-wave-s41/READ-BRIEF-O.md`. NOTE hash ced8b674…70ac (331 lines). Read BRIEF, NOTE whole,
upstream S5 definition and Theorem K′. Plan: own exact generator of S5(0.8) to 2·10⁹ (multiplicative sieve, a different method
from the NOTE's Ω-recursion), own full-lattice uint64 count of f_G(n_K) (no top-prime trick), re-derivation of §2.1, §2.5,
§4 T1–T4′, §5.1, prior art at the page. Deliverable `read-O.md`; re-run `verify-O/`. read-F / verify-F not opened.

## 14:53 IST 2026-10-01 — read-O block 2: decisive numbers reproduced by independent methods
Own sieve generator (`verify-O/s5gen_O.c`, 31 s, 3.1 GB): S5(0.8) on [1, 2·10⁹] byte-identical to the dump (g-prime lists ≤ 10⁹
and (10⁹, 2·10⁹], and a[0..10⁹], by SHA-256); C1 numbers, half-decade maxima, E-record counts, §3 numbers all reproduce.
Own full-lattice uint64 counter (`verify-O/lattice_O.c`, 238,878,720 cells, no top-prime trick, 58 s): f_G(n_K) =
3,403,961,916,617,140 exactly; 2,525 g-prime divisors (same set as certK); C3 20,390 / 2,932,627 / 13,461,378,553; self-tests
276 / 26. K inequality TRUE in exact integers; ratio 1.134232; least constant 2.132357. read-O §2 written.
