# NOTE — unit `s5-multiplicity-s40`: the fate of Lemma H — multiplicity in S5(0.8) and in every dense ℕ-supported system

Session 40, 2026-10-01. Writer: Opus 5.5 (agent). Labels: **[proved here]**, **[computed]** (script + log in `verify/`),
**[quoted]** (source and line named), **[recalled, unverified]** (never load-bearing), **[novelty: single-check]**.
Brief: `BRIEF.md` (this folder). Record read first: `results/u-offsurgery-s39/NOTE.md` §2, §4; `READ-O-SUPPLEMENT.md` §C.
Big scratch: `/private/tmp/rh-s40-s5mult/`. Notation: a_n = number of multisets of g-primes with product n;
E(n) = N(n) − 0.8(n − 1) − 1; C(u) = N(u) − 0.8⌊u⌋; f_G(n) = number of multisets from a set G with product n.

## §0. Close (filled last)

(pending)

## §1. Reproduction of C1–C3 in exact arithmetic (task 1)

**Data.** `gpF_r08_1e9.u32`: SHA-256 f5563f1548375d70…d904a1 (matches the brief), 50,829,666 entries, strictly increasing, every
m_q = 1, last g-prime 999,999,835, a_q ≥ 1 at every g-prime (`verify/dump_records.c`, `logs/dump_records.log`) **[computed]**.

**C1 — reproduced [computed].** Exact int64 scan of `aF_r08_1e9.u16` (E in units of 1/5): N(10⁹) = 800,000,008, C(10⁹) = 8;
sup_{n≤10⁹} E = 1374/5 = 274.8 at n = 902,538,000 = 2⁴·3²·5³·7·13·19·29 with a_n = 276 and E(n − 1) = −2/5; inf E = −2/5 (attained
in every half-decade from 10¹ on; the a-priori floor is −1 − ρ = −1.8). Of the 37 E-records with n ≥ 10⁷, 19 are single spikes
E(n) − E(n − 1) = a_n − 0.8 at integers with a_n ≥ 50 and E(n − 1) ≤ 37.6; the other 18 add ≤ 2.2 each (one adds 14.2) within 76
integers after a spike (identity E(n) − E(n − 1) = a_n − 0.8 checked at every record: `ok=1` throughout the log).
Records of a_n with log a/log n: 27 at 957,600 (0.239); 124 at 90,253,800 (0.263); 155 at 1.389·10⁸ (0.269); 215 at 4.166·10⁸
(0.271); 244 at 7.637·10⁸ (0.269); 276 at 9.025·10⁸ (0.273). Per half-decade max a_n, windows [10⁴·⁵, 10⁵) … [10⁸·⁵, 10⁹): 14, 21, 27, 42, 59, 83, 124,
178, 276 (local exponents per half-decade 0.35, 0.22, 0.38, 0.30, 0.30, 0.35, 0.31, 0.38; full table in the log). New fact: **539,856,374 of the integers 2 ≤ n ≤ 10⁹ (54%) have a_n = 0** — mean
0.8 is carried by a minority of g-integers, many with multiplicity.

**C3 — reproduced exactly, two code paths [computed].** f_G(n) = #{multisets of g-primes ≤ 10⁹ with product n} ≤ a_n (the
g-primes ≤ 10⁹ are fixed forever by the rule; larger g-primes only add multisets; for n ≤ 10⁹ equality holds). Counter
`verify/fcount.c` (divisor-lattice unbounded knapsack, unsigned 128-bit, every addition overflow-checked); self-tests
f(902538000) = 276 and f(478800) = 26 pass (`logs/fcount_selftest_C3.log`). Second path: the orchestrator's object-dtype DP
(Python integers) gives the same two smaller counts.

| n | log₁₀ n | g-prime divisors | f_G(n) exact | log f/log n |
|---|---|---|---|---|
| 2⁵·3³·5⁴·7·11·13·19²·29·41 | 14.3655 | 148 | 20,390 | 0.29998 |
| 2⁶·3³·5⁷·7²·11·13·17·19²·23·29·41 | 20.2007 | 318 | 2,932,627 | 0.32015 |
| 2⁷·3⁵·5⁹·7²·11·13·17·19³·23·29²·37·41²·47 | 30.4482 | 652 | 13,461,378,553 | 0.33267 |

(The 20.20 integer was not named in the record; it is the orchestrator's greedy rule rerun over primes ≤ 47,
`logs/search_greedy_K15_orchestrator_cands.log`, which also re-finds the other two.) Divisor lists: `logs/gdiv_C3b.txt`, `gdiv_C3c.txt`.
