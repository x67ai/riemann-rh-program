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

## §2. Pushing the lower bound (task 2)

**2.1 The identity behind every tool [proved here].** Let G be any finite or infinite set of integers ≥ 2 with multiplicities m_q, and
f(n) the number of multisets from G (copies distinguished) with product n. For every completely additive h: ℕ → ℤ,

  h(n)·f(n) = Σ_{q∈G} m_q·h(q)·Σ_{k≥1, q^k | n} f(n/q^k).

*Proof.* Sum h(x) over all elements x of all multisets M with product n. Since h(ΠM) = Σ_{x∈M} h(x) = h(n), the total is h(n)f(n).
Grouping instead by the element: a given copy of q occurs in M with multiplicity j ≥ 0, contributing j·h(q) = h(q)·#{k ≥ 1: k ≤ j};
and multisets containing that copy at least k times are in bijection with all multisets of product n/q^k (remove k copies). ∎
Cases used: h = Ω gives task 3's recursion a(n)Ω(n) = Σ_{q^k|n} m_q Ω(q) a(n/q^k); **h = v_p** gives
v_p(n) f(n) = Σ_{q∈G, p|q} m_q v_p(q) Σ_{k: q^k|n} f(n/q^k), whose right side involves only f at divisors of n with smaller
p-exponent. In particular, if p ∥ n then f(n) = Σ_{q∈G, p | q | n} m_q f(n/q).

**2.2 Tools [computed].** `verify/fcount.c` (full divisor lattice, 128-bit, §1). `verify/search2.c`: one lattice DP (float) per
accepted move, every candidate move n → np and every swap n → np/q scored from that one array through the v_p identity (the
right side needs only f at divisors of n); moves +1 over the first K primes ranked by rate Δln f/Δln n, then swaps accepted while
they raise X(n) = ln f − 0.35 ln n without raising τ(n). Scores agree with a fresh DP after every move (the program prints a
WARNING otherwise; none occurred). `verify/fcert.c`: exact f_G(n) for n = n₀·p₁⋯p_j (p_i ∥ n) with memory τ(n₀) only — 128-bit
lattice on n₀, then the v_p identity at exponent 1 for the top primes, memoized; it reproduces the full-lattice counts (276;
107,416,400,010 at log₁₀n = 31.41 with two and with three top primes). `verify/fsplit.c` (counts only factorizations in which no
factor contains two primes of a chosen set L): loses a factor 4.7 to 150 on the same n — multi-large-prime g-primes carry much of
the count, so it is not used for bounds.

**2.3 Close K: an explicit integer beyond the Rouché tolerance [computed, two code paths].**

  n_K = 2⁸·3⁵·5⁹·7³·11²·13·17·19³·23·29²·37·41²·59·61·79·89·109·149
      = 3,779,321,386,617,192,025,903,153,574,378,164,500,000,000   (log₁₀ n_K = 42.577414),

  a_{n_K} ≥ f_G(n_K) = **3,403,961,916,617,140**   (G = the g-primes ≤ 10⁹ of S5(0.8); 2,525 of them divide n_K),

and f_G(n_K) > 3.76·n_K^{0.35} + 3, checked in exact integers as (25(f − 3))²⁰ > 94²⁰·n_K⁷; the ratio is f/(3.76 n^{0.35}) = 1.1342,
i.e. a_{n_K} ≥ 4.2647·n_K^{0.35} (exponent log f/log n = 0.36479). Paths: (1) `verify/fcert.c` — 128-bit lattice on n₀ = n_K/(89·109·149)
(τ(n₀) = 29,859,840) plus the exponent-1 v_p identity for 89, 109, 149, no overflow (`logs/fcert_K1.log`, 10 s); (2)
`verify/checkK.py` — shares no code: verifies that every listed divisor is in the g-prime dump (binary search) and that the list is
complete (all 500,886 divisors ≤ 10⁹ of n_K scanned), recounts by a numpy slice-DP plus a recursive derivation step modulo three
primes near 2³¹ — all three residues agree with (1) — and runs the exact-integer K test (`logs/checkK_K1.log`, 3 min). (3) The
float full-lattice DP of `search2.c` (τ = 238,878,720) gave log₁₀ f = 15.5320, matching. The list: `verify/certK/K1_gdiv.txt`
(SHA-256 2dfd9f2c…c935036e; largest member 999,086,975).

*Consequence [proved here, given the dump].* E(n) − E(n − 1) = C(n) − C(n − 1) = a_n − 0.8. If |C(u)| ≤ c·u^θ for all u > 10⁹ with
θ ≤ 0.35 and c < 1.88, then a_{n_K} − 0.8 ≤ c n_K^θ + c (n_K − 1)^θ < 3.76 n_K^{0.35}, contradicting a_{n_K} > 3.76 n_K^{0.35} + 3.
**So hypothesis H_θ of Theorem K′ is false for every θ ≤ 0.35 and every constant c < 1.88 (in particular for c = 1 as stated);
Theorem K′ is vacuous as stated** — the Rouché step at X = 10⁹ needs c < 0.0394/0.0210 = 1.876, and any valid constant must be
≥ (a_{n_K} − 0.8)/(2 n_K^{0.35}) ≥ 2.13. What this does NOT refute: Lemma H in its ≪ form (unspecified constant). A fixed finite G
cannot do that — f_G(n) ≤ (1 + log₂ n)^{|G|} — so refuting "≪ x^{0.35}" needs g-primes beyond any fixed bound, i.e. a theorem
(§4) or a growing exact system (§3). The data are the orchestrator's dump; its independent re-verification is §2.5.

*Anatomy.* The primes of n_K are 2, 3, 7, 11, 13, 17, 23, 37 (accepted) and **5, 19, 29, 41, 59, 61, 79, 89, 109, 149 — ten of the
eleven refused primes ≤ 149** (139 is the one left out). The search, told nothing about refusal, chose the refused primes: the
multiplicity is carried by refused primes, each entering through its carriers (§5).
