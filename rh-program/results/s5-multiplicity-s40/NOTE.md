# NOTE — unit `s5-multiplicity-s40`: the fate of Lemma H — multiplicity in S5(0.8) and in every dense ℕ-supported system

Session 40, 2026-10-01. Writer: Opus 5.5 (agent). Labels: **[proved here]**, **[computed]** (script + log in `verify/`),
**[quoted]** (source and line named), **[recalled, unverified]** (never load-bearing), **[novelty: single-check]**.
Brief: `BRIEF.md` (this folder). Record read first: `results/u-offsurgery-s39/NOTE.md` §2, §4; `READ-O-SUPPLEMENT.md` §C.
Big scratch: `/private/tmp/rh-s40-s5mult/`. Notation: a_n = number of multisets of g-primes with product n;
E(n) = N(n) − 0.8(n − 1) − 1; C(u) = N(u) − 0.8⌊u⌋; f_G(n) = number of multisets from a set G with product n.

## §0. Close — K (stop line (b) fired) + T

**K [computed; two code paths; data certified by a third].** n_K = 2⁸·3⁵·5⁹·7³·11²·13·17·19³·23·29²·37·41²·59·61·79·89·109·149
(≈ 3.78·10⁴²) has a_{n_K} ≥ f_G(n_K) = 3,403,961,916,617,140 > 3.76·n_K^{0.35} + 3 (ratio 1.134; exact-integer test), counted from
its 2,525 g-prime divisors ≤ 10⁹ (`verify/certK/K1_gdiv.txt`) by `fcert.c` (128-bit) and by `checkK.py` (independent, mod three
primes) (§2.3); the g-prime list itself is re-certified at every n ≤ 10⁹ by the Ω-identity and the rule, 0 failures (§2.5).
Since E(n) − E(n − 1) = a_n − 0.8, **hypothesis H_θ of Theorem K′ is false for every θ ≤ 0.35 and every constant c < 1.88; Theorem K′
is vacuous as stated** [proved here]. Not refuted: Lemma H with an unspecified constant — no fixed finite G can refute it
(f_G(n) ≤ (1 + log₂ n)^{|G|}). The orchestrator's C1–C3 are reproduced exactly (§1); C4 is confirmed and sharpened: the certified
exponent of max a_n climbs 0.273 (10⁹) → 0.3648 (10⁴²·⁶) with marginal exponents 0.37–0.46 and no decline (§2.4) [computed]; if
limsup log a_n/log n > 0.383 = Re ρ₁/2, then β ≥ that and S5(0.8) obeys α ≤ 2β — no counterexample to U at all (§5.3) [model].
**T [proved here].** T1: sup a_n < ∞ ⇔ a_n ≤ 1 ⇔ independent g-primes with m_q ≤ 1; any relation forces a_{n₀^k} ≥ k + 1. T2: in a
free ℕ-supported system K(x) ≤ R(x/2) and π_P(x) ≤ π(x) − [R(x) − R(x/2)]. T3: free + N = ρx + O(x^θ), θ < 1 ⇒ refused primes and
added composites are both O(x e^{−c√log x}) (via Landau's PNT, [quoted] DMV 2006 pp. 2–3); converse construction for any R with
Σ_R p^{−θ} < ∞. 4(b): bounded multiplicity is settled by T1+T3; under Ramanujan alone dense composites occur (ℙ ∪ {2p}), and the
dense-refusal + Ramanujan + good-N case is stated as open. T4/T4′: a rank excess D among the g-primes ≤ y forces
max_{n≤x} f ≥ ½e^{D log(1/c) − …} at log x ≍ y; with a positive proportion of refused primes and the PNT, max_{n≤x} a_n ≥ x^{κ/log log x}.
§5.1: in S5(0.8), E ≥ −0.4, every m_n ∈ {0, 1}, and n is a g-prime iff A(n) = 0 and E(n − 1) ≤ 0.3.
**Also [computed]:** the exact system extended to 2·10⁹ (max a_n = 344 at 1,805,076,000, sup E = 348.0; §3); carriers c_ℓ(10⁹) ≈
0.043·10⁹/ℓ for every refused ℓ tested, carrier probability (1.6–1.8)/ln n (§5.2). Task 6 not run (stop line; §7 UT-M4).

## §1. Reproduction of C1–C3 in exact arithmetic (task 1)

**Data.** `gpF_r08_1e9.u32`: SHA-256 f5563f1548375d70…d904a1 (matches the brief), 50,829,666 entries, strictly increasing, every
m_q = 1, last g-prime 999,999,835, a_q ≥ 1 at every g-prime (`verify/dump_records.c`, `logs/dump_records.log`) **[computed]**.

**C1 — reproduced [computed].** Exact int64 scan of `aF_r08_1e9.u16` (E in units of 1/5): N(10⁹) = 800,000,008, C(10⁹) = 8;
sup_{n≤10⁹} E = 1374/5 = 274.8 at n = 902,538,000 = 2⁴·3²·5³·7·13·19·29 with a_n = 276 and E(n − 1) = −2/5; inf E = −2/5 (attained
in every half-decade from 10¹ on; the a-priori floor −1 − ρ = −1.8 is never approached, and §5.1 proves E ≥ −0.4 always). Of the 37 E-records with n ≥ 10⁷, 19 are single spikes
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
they raise X(n) = ln f − 0.35 ln n without raising τ(n). The score of every accepted +1 move agrees with the fresh DP that follows
it to 10⁻³ in ln f (the program prints a WARNING otherwise; none occurred). `verify/fcert.c`: exact f_G(n) for n = n₀·p₁⋯p_j (p_i ∥ n) with memory τ(n₀) only — 128-bit
lattice on n₀, then the v_p identity at exponent 1 for the top primes, memoized; it reproduces the full-lattice counts (276;
107,416,400,010 at log₁₀n = 31.41 with two and with three top primes). `verify/fsplit.c` (counts only factorizations in which no
factor contains two primes of a chosen set L): 22,898,392,936 and 718,932,573 on the same n — losses of 4.7 and 149 — so
multi-large-prime g-primes carry much of the count and it is not used for bounds. All of this: `logs/tool_crosschecks.log`.

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

**2.4 The search that found n_K [computed].** `search2.c` over the first 60 primes (≤ 281), rate-greedy plus swaps, from the record
holder 902,538,000 (`logs/search2_rate_K60.log`, 3.7 min; stopped by hand at the first float crossing). Float log₁₀ f; "excess" =
log₁₀ f − log₁₀(3.76 n^{0.35}); "rate" = marginal exponent Δlog f/Δlog n of the step:

| log₁₀ n | log₁₀ f | log f/log n | excess | rate | τ(n) |
|---|---|---|---|---|---|
| 8.96 | 2.441 | 0.2726 | −1.269 | — | 960 |
| 15.17 | 4.612 | 0.3040 | −1.274 | 0.382 | 17,920 |
| 20.30 | 6.686 | 0.3294 | −0.994 | 0.407 | 161,280 |
| 25.43 | 8.704 | 0.3422 | −0.773 | 0.398 | 1,128,960 |
| 29.93 | 10.454 | 0.3493 | −0.597 | 0.386 | 4,423,680 |
| 35.62 | 12.696 | 0.3564 | −0.348 | 0.393 | 35,389,440 |
| 39.97 | 14.456 | 0.3617 | −0.107 | 0.402 | 127,401,984 |
| 42.58 | 15.532 | 0.3648 | +0.055 | 0.418 | 238,878,720 |

The marginal exponent of the +1 steps is 0.31–0.37 below 10¹⁵ and 0.371–0.464 from 10¹⁵ to 10⁴²·⁶, with no decline; the
cumulative exponent climbs toward it. With
candidates ≤ 47 only (the orchestrator's set) the same rule reaches 0.3327 at 10³⁰·⁴⁵; allowing primes to 281 adds the refused
primes 59, 61, 79, 89, 109, 149, each entering at rate ≈ 0.39–0.42 — refused primes are the cheapest source of multiplicity.
Cost is set by τ(n) (memory 4 bytes per cell in float, 16 in exact arithmetic on n₀ = n/(top primes)).

**2.5 Independent certification of the dump [computed].** The K-close rests on the orchestrator's g-prime list. `verify/omega_check.c`
re-derives it by a different identity: for every 2 ≤ n ≤ 10⁹ it checks (I) Ω(n)a(n) = Σ_{q^k | n} m_q Ω(q) a(n/q^k) (§2.1, h = Ω,
q = n included; Ω by its own segmented sieve) and (II) the rule m_n = max(0, ⌊0.8(n − 1) + 1 − N(n − 1) − (a(n) − m_n) + ½⌋) in exact
integers. *Induction [proved here]:* if a(k), m_k are correct for k < n, then (I) at n says Ω(n)(a(n) − m_n) = Σ_{q<n, q^k|n} m_q Ω(q)
a(n/q^k) = Ω(n)A(n) (the identity for the system truncated below n, whose count at n/q^k < n is a(n/q^k)), so a(n) − m_n = A(n), and
(II) is then the defining rule. **Result: 0 failures of (I) and 0 of (II) over all n ≤ 10⁹** (`logs/omega_check.log`; 3.5 min,
peak 707 MB). So the dump is S5(0.8) on [1, 10⁹], and every one of the 2,525 g-primes in `certK/K1_gdiv.txt` is a g-prime of S5(0.8).

## §3. The exact system beyond 10⁹ (task 3) [computed, one code path]

For 10⁹ < n ≤ 2·10⁹ every g-prime q < n dividing n is ≤ 10⁹ and every n/q^k is ≤ 10⁹, so the Ω-recursion of §2.1 gives A(n) =
acc(n)/Ω(n) from the certified dump alone, and the rule gives m_n; `omega_check.c` runs this as its generator mode (division
exact at all 10⁹ new n — an internal check — and no memory beyond the segment). Results (`logs/omega_check.log`):
N(2·10⁹) = 1,600,000,009, C(2·10⁹) = 9; 47,353,731 g-primes in (10⁹, 2·10⁹] (π(2·10⁹) − π(10⁹) = 47,374,753 by `verify/pi.c`, `logs/pi.log`),
list in `/private/tmp/rh-s40-s5mult/gp_ext_1e9_2e9.u32`; **max a_n on (10⁹, 2·10⁹] = 344 at 1,805,076,000 = 2·902,538,000 =
2⁵·3²·5³·7·13·19·29** (log a/log n = 0.2740), **sup E = 348.0 at 1,805,076,001**; local exponent of max a_n against [10⁸·⁵, 10⁹):
log(344/276)/log 2 = 0.318. The record holder doubled, as the anatomy predicts (one more factor 2 multiplies the carrier choices).
Dress rehearsal: §2.5 checks the 10⁹ dump entry by entry (stronger than a sub-range hash).
*Not done, priced:* the next half-decade [2·10⁹, 10⁹·⁵] needs a(j) stored to 1.58·10⁹ and the g-primes to 1.58·10⁹ (≈ 2 GB beyond the
dump), and [10⁹·⁵, 10¹⁰] needs a(j) to 5·10⁹ — over the 4 GB cap. It buys one exact half-decade, while the certified bound already
reaches 10⁴²·⁶ (§2.3); skipped after the stop line fired.

## §4. Structure theorems (task 4)

Setting: P an ℕ-supported discrete system — integers q ≥ 2 with multiplicities m_q ≥ 0, finitely many ≤ x; a_n = #multisets
(copies distinguished) with product n; π_P(x) = Σ_{q≤x} m_q. Write A(x) = #{rational primes p ≤ x with m_p ≥ 1} ("accepted"),
R(x) = π(x) − A(x) ("refused"), K(x) = Σ_{q ≤ x composite} m_q, A(y, x] = A(x) − A(y), etc. P is *free* if a_n ≤ 1 for all n.

**Theorem T1 (bounded multiplicity is freeness) [proved here].** The following are equivalent: (i) sup_n a_n < ∞; (ii) a_n ≤ 1
for all n; (iii) every m_q ≤ 1 and the g-primes are multiplicatively independent in ℚ^×. Quantitatively: if two distinct multisets
have product n₀, then a_{n₀^k} ≥ k + 1 for every k, so max_{n≤x} a_n ≥ ⌊log x/log n₀⌋ + 1; and if λ₁, …, λ_r ∈ ℤ^{(G)} are linearly
independent relations (Π q^{λ_i(q)} = 1, λ_i = λ_i⁺ − λ_i⁻, height n_i = Π q^{λ_i⁺(q)}), then a_m ≥ Π_i (k_i + 1) at m = Π n_i^{k_i}.
*Proof.* (iii)⇒(ii): two distinct multisets with one product differ by a nonzero integer relation. (ii)⇒(i): trivial. (i)⇒(iii):
m_q ≥ 2 gives a_{q^k} ≥ k + 1 (how many of the k factors are the first copy); a relation gives unbounded a by the quantitative part.
Quantitative part: the multisets M_j = j·M ⊎ (k − j)·M′ (j = 0, …, k) all have product n₀^k, and they are distinct: at an element
x with mult_M(x) ≠ mult_{M′}(x), mult_{M_j}(x) = j·mult_M(x) + (k − j)·mult_{M′}(x) is strictly monotone in j. For r relations take
Σ_i [j_i λ_i⁺ + (k_i − j_i) λ_i⁻], 0 ≤ j_i ≤ k_i; two choices differ by Σ_i (j_i − j′_i) λ_i ≠ 0. ∎
So "a_n ≤ M for all n" collapses to the free case; any relation already forces logarithmic growth along powers.

**Theorem T2 (free systems on ℕ: the rank count) [proved here].** Let P be free. Then for every x ≥ 2:
 (a) K(x) ≤ R(x/2);  (b) π_P(x) ≤ π(x) − [R(x) − R(x/2)] ≤ π(x);  equivalently R(x) − R(x/2) ≤ π(x) − π_P(x).
*Proof.* By T1 the g-primes are independent with m_q ≤ 1. Let V = {g-primes ≤ x} minus the rational primes in (x/2, x]. Every q ∈ V
is a prime ≤ x/2 or a composite q = pk ≤ x with k ≥ 2, so all its prime factors are ≤ x/2: V lies in the free abelian group
⟨primes ≤ x/2⟩ of rank π(x/2), and V is independent, so |V| = A(x/2) + K(x) ≤ π(x/2), i.e. K(x) ≤ R(x/2). Then
π_P(x) = A(x) + K(x) ≤ A(x) + R(x/2) = π(x) − R(x) + R(x/2). ∎
(The orchestrator's sketch had the right count; its two "facts" about prime factors are true for every integer, and the content is
the independence. The sharp form is (a): each composite g-prime ≤ x uses up one refused prime ≤ x/2.)

**Corollary T3 (free + Landau ⇒ thin surgery of ℙ) [proved here, from a quoted PNT].** *Quoted* (Diamond–Montgomery–Vorhauer,
Math. Ann. 334 (2006), pp. 2–3, `novel-wave-s37/beurling-frontier/sources/p1-02-…txt` l. 99–115): "Landau's reasoning in fact
provides a proof that if N_B(x) = κx + O(x^θ) with κ > 0 and 0 ≤ θ < 1, then … π_B(x) = li(x) + O(x exp(−c√((1 − θ) log x)))" (the
radical is lost in the text extraction; (2) at l. 38 is the classical π(x) = li(x) + O(x exp(−c√log x))). Let P be free with
N_P(x) = ρx + O(x^θ), θ < 1. Then R(x) = O(x exp(−c′√log x)) and K(x) = O(x exp(−c′√log x)) for some c′ = c′(θ) > 0: P is ℙ with
a set of refused primes and a set of added composites, both of counting function O(x e^{−c′√log x}) — a thin surgery.
*Proof.* By T2(b) and the two PNTs, D(y) := R(y) − R(y/2) ≤ |π(y) − li(y)| + |li(y) − π_P(y)| ≤ C y e^{−c√((1−θ) log y)}. Summing
dyadically, R(x) = Σ_{j≥0} D(x/2^j): the terms with x/2^j ≥ √x total ≤ 2Cx e^{−c√((1−θ)(log x)/2)}; the remaining terms
telescope to R(x/2^{j₀}) ≤ π(√x) ≤ √x.
K(x) ≤ R(x/2) by T2(a). ∎
*Converse (how thin is enough) [proved here].* For any set R of odd primes with Σ_{p∈R} p^{−θ} < ∞ (0 < θ < 1), the system
(ℙ ∖ R) ∪ {2p : p ∈ R} is free (2 is kept; each 2p brings its own new prime, so the exponent vectors are triangular) and attains T2(a) with equality, K(x) = R(x/2); its zeta function is ζ(s)H(s), H(s) =
Π_{p∈R}(1 − p^{−s})/(1 − (2p)^{−s}) = Σ h(n)n^{−s} with Σ|h(n)|n^{−θ} ≤ Π_{p∈R}(1 + p^{−θ})(1 − (2p)^{−θ})^{−1} < ∞, hence
N_P(x) = Σ_{d≤x} h(d)⌊x/d⌋ = H(1)x + O(x^θ). So the necessary O(x e^{−c√log x}) and the sufficient Σ_R p^{−θ} < ∞ bracket the truth;
whether a free system with N = ρx + O(x^θ) can refuse ≍ x^{θ″} primes with θ < θ″ < 1 is left open (it needs H with cancellation
between deletions and carriers, not available from absolute convergence).

**4(b) — what survives under a_n ≤ M and under Ramanujan [proved here, examples].** a_n ≤ M ⇒ free (T1) ⇒, with N = ρx + O(x^θ),
a thin surgery of ℙ (T3): complete. Under a_n ≪ n^ε the system need not be free, and composites need not be few unless density
is imposed: (R1) ℙ ∪ {6}: a_n = min(v₂(n), v₃(n)) + 1 ≤ log₂ n + 1 and N(x) = Σ_{j≥0}⌊x/6^j⌋ = (6/5)x + O(log x) — a finite,
non-free surgery with an excellent integer count. (R2) ℙ ∪ {2p : p prime}: for n = 2^a m (m odd) the factorizations are the choices
0 ≤ j_p ≤ v_p(m) (copies of 2p) with Σ j_p ≤ a, so a_n ≤ τ(m) ≪ n^ε; but N(x)/x is unbounded (if N(x) ≤ Cx then ζ_P(σ) =
σ∫N x^{−σ−1}dx ≤ Cσ/(σ − 1), while ζ_P(σ) ≥ ζ(σ)Π_p(1 + (2p)^{−σ}) and Σ_p 1/(2p) diverges). So Ramanujan permits dense composites;
the density ρx is what must exclude them. **Open (stated precisely):** is there an ℕ-supported system with N(x) = ρx + O(x^θ), θ < 1,
a_n ≪ n^ε, and a positive proportion of refused primes? By T4 below such a system has max_{n≤x} a_n ≥ x^{κ/log log x} — compatible
with Ramanujan, so T4 does not decide it; S5(0.8) is no candidate (a_{n_K} ≥ 4.26·n_K^{0.35}, §2.3).

**4(c) — a large relation lattice forces multiplicity [proved here].**
*Lemma A.* Let V be a finite multiset of integers ≥ 2, Q the set of primes dividing its members, f_V(n) the number of
sub-multisets with product n, Z_V(σ) = Π_{q∈V}(1 − q^{−σ})^{−1}, Z_Q(σ) = Π_{p∈Q}(1 − p^{−σ})^{−1}. If 0 < δ < σ and
x^δ ≥ 2Z_V(σ − δ)/Z_V(σ), then max_{n≤x} f_V(n) ≥ Z_V(σ)/(2Z_Q(σ)).
*Proof.* Σ_{n>x} f_V(n)n^{−σ} ≤ x^{−δ}Σ_n f_V(n) n^{−σ+δ} = x^{−δ}Z_V(σ − δ) ≤ Z_V(σ)/2, so Σ_{n≤x} f_V(n)n^{−σ} ≥ Z_V(σ)/2; and since
f_V lives on Q-smooth n, Σ_{n≤x} f_V(n)n^{−σ} ≤ max_{n≤x} f_V(n) · Z_Q(σ). ∎
*Theorem T4.* Let V be a finite multiset of integers in [2, y], Q its prime support, D = |V| − |Q|, θ(Q) = Σ_{p∈Q} log p, and
0 < c ≤ 1. If log x ≥ (2 log 2/c)(|V| + 1) log y + Σ_{q∈V} log q, then
  max_{n≤x} f_V(n) ≥ ½ exp( D log(1/c) − Σ_{p∈Q} log(log y/log p) − c θ(Q)/log y ).
*Proof.* With φ_σ(t) = −log(1 − t^{−σ}) and u = σ log t > 0: 1 − e^{−u} ≤ u and 1 − e^{−u} ≥ u e^{−u} (as e^u − 1 ≥ u) give
log(1/u) ≤ φ_σ(t) ≤ log(1/u) + u. Take σ = c/log y, δ = σ/2. Then log Z_V(σ) ≥ Σ_V log(log y/(c log q)) ≥ |V| log(1/c), and
log Z_Q(σ) ≤ Σ_Q [log(log y/(c log p)) + c log p/log y] = |Q| log(1/c) + Σ_Q log(log y/log p) + cθ(Q)/log y; subtract.
For the tail condition, log Z_V(σ/2) − log Z_V(σ) ≤ Σ_V [log(2/(σ log q)) + (σ/2)log q − log(1/(σ log q))] = |V| log 2 +
(σ/2)Σ_V log q, so x^{σ/2} ≥ 2Z_V(σ/2)/Z_V(σ) holds once (c/(2 log y)) log x ≥ (|V| + 1) log 2 + (c/(2 log y))Σ_V log q. Lemma A. ∎
*Corollary T4′.* Let P be ℕ-supported with π_P(y) = (1 + o(1)) y/log y (true under N = ρx + O(x^θ), θ < 1, by the quoted Landau
PNT) and with a positive proportion of refused primes in dyadic ranges: Σ_{y/2<p≤y} m_p ≤ (1 − δ)(π(y) − π(y/2)) for large y. Then
max_{n≤x} a_n ≥ exp(κ log x/log log x) for large x, with κ = κ(δ) > 0; hence sup_{u≤x}|N(u) − ρ⌊u⌋| ≥ ½(exp(κ log x/log log x) − ρ).
*Proof.* Take V = {g-primes ≤ y} minus the primes in (y/2, y] (multiplicity counted); Q ⊆ {p ≤ y/2} as in T2. By the classical PNT
(DMV l. 38), D ≥ π_P(y) − Σ_{y/2<p≤y} m_p − π(y/2) ≥ (δ/2 − o(1)) y/log y. Next Σ_{p≤y/2} log(log y/log p) ≪ y/log² y: primes ≤ √y give
O(√y log log y), and for p > √y, log(log y/log p) ≤ 2 log(y/p)/log y with Σ_{p≤y} log(y/p) = ∫₁^y π(t)dt/t ≪ y/log y (Chebyshev
π(t) ≪ t/log t [recalled, unverified — classical, elementary]). And θ(Q) ≤ θ(y/2) ≤ y log 2 (Chebyshev, same label). So
log max ≥ (y/log y)(½δ log(1/c) − c log 2 − o(1)) at log x = (2 log 2/c + 1)(1 + o(1)) y; fix c = c(δ) small and solve for y. The
error statement follows from a_n − ρ = C(n) − C(n − 1). ∎
So the rank excess forces divisor-function-size multiplicity, not a power: T4′ alone says nothing about β. The power-size
multiplicity of S5(0.8) at the computed scales (§2) is a property of its carriers, not of rank alone (§5).

## §5. Carriers and the model (tasks 5 and 2(ii))

**5.1 Two exact facts about the rule [proved here].** (a) E(n) ≥ −0.4 for all n ≥ 1: E takes values in ⅕ℤ; if m_n ≥ 1 then
a_n = A(n) + ⌊1.3 − E(n − 1) − A(n)⌋ > 0.3 − E(n − 1), and if m_n = 0 then 1.3 − E(n − 1) − A(n) < 1, i.e. A(n) > 0.3 − E(n − 1);
either way E(n) = E(n − 1) + a_n − 0.8 > −0.5, so E(n) ≥ −0.4 (E(1) = 0). (Here 0.8(n − 1) + 1 − N(n − 1) = 0.8 − E(n − 1), so the
rule reads m_n = max(0, ⌊1.3 − E(n − 1) − A(n)⌋).) (b) Hence m_n ≥ 1 forces A(n) ≤ 0.3 − E(n − 1) ≤ 0.7, i.e. A(n) = 0, and then
m_n = ⌊1.3 − E(n − 1)⌋ ≤ 1: **every multiplicity is 0 or 1, and n is a g-prime iff n is not representable by smaller g-primes and
E(n − 1) ≤ 0.3.** (Matches the dump: all m_q = 1; inf E = −0.4.)

**5.2 Data [computed]** (`verify/carriers.c`, `logs/carriers.log`, 12 s). Per decade [10^d, 10^{d+1}):

| d | non-representable n (A = 0), share | accepted share of those | × ln(10^{d+½}) | accepted primes | refused primes | composite g-primes |
|---|---|---|---|---|---|---|
| 4 | 0.477 | 0.196 | 2.03 | 1,601 | 6,762 | 6,807 |
| 6 | 0.541 | 0.121 | 1.80 | 65,657 | 520,424 | 520,957 |
| 8 | 0.594 | 0.0844 | 1.65 | 3,523,361 | 41,562,718 | 41,543,940 |

Composite g-primes replace refused primes one for one in every decade (decade 8: difference 18,778 out of 4.2·10⁷) — the PNT
balance π_P ≈ π, held by the rule. Refused share of primes: 81% (d = 4) → 92% (d = 8). Carriers: for each of the first 30 refused
primes ℓ (5, 19, 29, 41, 59, 61, 79, 89, 109, 139, 149, 163, …, 359), the number of composite g-primes ≤ 10⁹ divisible by ℓ is
**c_ℓ(10⁹) = (0.039 … 0.047)·10⁹/ℓ** — e.g. 8,147,069 for ℓ = 5, 2,244,986 for 19, 379,987 for 109, 265,851 for 149 — i.e. ≈ 0.043 =
0.9/ln 10⁹ of the multiples of ℓ, the same for every ℓ; among the non-representable multiples of ℓ in decade 8 the accepted share is
1.6–1.8/ln n, as for all integers (ℓ = 5: 1.25/ln n). **So the heuristic holds: a multiple n of a refused prime is a carrier with
probability ≈ c/ln n, c ≈ 1.6–1.8, given that it is not representable by smaller g-primes (about half of the multiples are not).** Which refused primes carry the
most carriers: the smallest, in proportion to 1/ℓ (5 alone has 8.1·10⁶); per unit of log ℓ they are all alike, which is why the
search of §2 takes the refused primes in increasing order (59, 61, 79, 89, 109, 149) at nearly equal rates 0.39–0.42.

**5.3 The model.** A factorization of n must cover each refused ℓ | n by carriers ℓs (s | n/ℓ; or multi-ℓ carriers), so adding a
new refused prime multiplies the count by g_ℓ(n) = Σ_{s | n, ℓs ∈ G} f(n/s)/f(n) ≈ (c/ln(ℓs̄))·Σ_{s|n} s^{−μ}, μ the current exponent.
For highly composite n, Σ_{s|n} s^{−μ} = Π_{p^e ∥ n}(1 + p^{−μ} + … + p^{−eμ}) grows without bound as n gains small primes, so the
marginal rate ln g_ℓ/ln ℓ can stay above μ and μ climbs — the observed 0.27 → 0.365 with marginal 0.37–0.46 (§2.4), not the
decreasing divisor-function shape n^{c/log log n} (which is only the rank lower bound T4′). With all g-primes available
(sizes unbounded, carrier density c/ln) the same count for squarefree n with w prime factors is ≈ Σ_{partitions} Π_blocks c/ln(block)
≈ Bell(w)·Π(c/ln), exponent → 1 (set-partition regime) [heuristic]. With G ≤ 10⁹ fixed the certified exponent must eventually
fall (f_G(n) ≤ (1 + log₂ n)^{|G|}). **Crossings [model]:** f_G ≥ 3.76 n^{0.35}: certified at 10^{42.6} (§2.3). f_G ≥ n^{0.383} (= half
the zero's real part): if the marginal rate r persists, at log₁₀ n ≈ (42.577 r − 15.532)/(r − 0.383) = 64 (r = 0.42), 71 (0.41),
88 (0.40); the true a_n crosses earlier. If limsup log a_n/log n > 0.383, then β ≥ that > Re ρ₁/2 and S5(0.8) satisfies α ≤ 2β —
it would not be a counterexample to U at all (taking α = Re ρ₁ ≈ 0.766 as the record estimates; a zero further right at larger
height, UT-M4, would raise the threshold).

## §6. Prior art, novelty, distance from upstream

- The only printed input used in a proof is Landau's PNT for Beurling systems as stated by Diamond–Montgomery–Vorhauer (Math. Ann.
  334 (2006) pp. 2–3, l. 99–115 of the on-disk text) and the classical PNT (same paper, (2), l. 38); Chebyshev's bounds are
  [recalled, unverified] and enter only T4′'s constants. Everything else (T1, T2, T4, Lemma A, §2.1, §5.1) is proved on the page.
- T1's "a relation forces a_{n^k} ≥ k + 1" and T2's rank count are elementary and may be folklore (Hilberdink 2012, on disk as
  `fr/sources/p3-22c2`, studies systems with N(x) − cx periodic and finds ℙ minus finitely many primes — the same "ℕ-supported
  systems are rigid" theme, in a different regime); not found stated in the on-disk corpus. Lemma A is Rankin's trick run in reverse
  (a lower bound for a maximum from an Euler-product ratio); T4/T4′ as stated: not found on disk.
- **Novelty: single-check** for T2(a)/(b), T3's converse construction, T4/T4′, §5.1, and the K certificate (a computation).
- **Distance from upstream (10(n)):** the K-close is pure computation on the program's own construction; the theorems use one
  printed source (DMV 2006 for Landau's and the classical PNT). No external work is needed or waited for.

## §7. Untried (the directions' format; each with its first rung)

- **UT-M1 Lemma H with unspecified constant (the ≪ form).** Refuting it needs g-primes beyond any fixed bound: a lower bound for
  a_n that uses the rule itself (§5.1: n is a g-prime iff A(n) = 0 and E(n − 1) ≤ 0.3) to guarantee carriers of every refused ℓ among
  the non-representable ℓk at all scales. First rung: prove that each refused ℓ ≤ y has ≥ 1 carrier ℓs with s ≤ y^C (heuristic
  only: the data show c_ℓ(x) ≈ 0.9(x/ℓ)/ln x for every ℓ tested, §5.2). Target: B2.
- **UT-M2 Certify the exponent 0.383.** Exact f_G beyond 10⁴²·⁶: the lattice costs τ(n); replace it by the top-prime derivation
  recursion (fcert) with more top primes and a sparse memo, and enlarge G with the 2·10⁹ extension. Goal: f_G(n) ≥ n^{0.383} at an
  explicit n (model: 10⁶⁴–10⁸⁸). If reached, S5(0.8) obeys α ≤ 2β on the record (no U counterexample). Target: B2.
- **UT-M3 Theorem K″.** A refutation of U from S5(ρ) for some ρ now needs a hypothesis with constant ≥ 2.13 at θ = 0.35, hence a
  larger truncation X′ (tail ∝ c·X′^{θ−σ}); price the exact system to X′ = 10¹¹ with the Ω-recursion (§3) — and first check, by §2's
  search on that system, that max a_n has not already outgrown n^{Re ρ₁/2}. Target: B2.
- **UT-M4 Task 6 (not run, stop line).** Zeros of F_X (X = 10⁹), σ > ½, t ≤ 300: block moments in log n (blocks of width 0.01,
  ~25 Taylor terms, one 10⁹-term pass), Euler–Maclaurin tail for 0.8ζ, grid + argument principle; question: does the largest real
  part rise with height? Target: B2, B4.
- **UT-M5 The open case of 4(b):** an ℕ-supported system with N = ρx + O(x^θ), a_n ≪ n^ε and a positive proportion of refused primes —
  construct (balanced carriers across many ℓ, so that Σ_K q^{−s} − Σ_R p^{−s} continues analytically) or refute. Target: C2.

## §8. Instruments rows (shape of `directions/B2-refutation-program.md`: | Quantity | Current best value | Result file | Dated |; records, never ranks; not inserted)

| Quantity | Current best value | Result file | Dated |
|---|---|---|---|
| Certified multiplicity of S5(0.8) beyond the computed range (lower bound a_n ≥ f_G(n), G = g-primes ≤ 10⁹, exact integers) | a_n ≥ 3,403,961,916,617,140 = 4.2647·n^{0.35} = n^{0.36479} at n_K = 2⁸·3⁵·5⁹·7³·11²·13·17·19³·23·29²·37·41²·59·61·79·89·109·149 (log₁₀ = 42.577); kills H_θ of Theorem K′ for θ ≤ 0.35, c < 1.88. Two code paths (fcert 128-bit; checkK mod 3 primes); dump re-certified by the Ω-identity, 0 failures to 10⁹. One producer | `s5-multiplicity-s40/NOTE.md` §2.3, §2.5; `…/verify/logs/fcert_K1.log`, `checkK_K1.log`, `omega_check.log`; list `verify/certK/K1_gdiv.txt` | 2026-10-01 |
| Exact S5(0.8) beyond 10⁹ | to 2·10⁹: N = 1,600,000,009, C(2·10⁹) = 9, max a_n = 344 at 1,805,076,000, sup E = 348.0; one code path (Ω-recursion generator) | `s5-multiplicity-s40/NOTE.md` §3; `…/verify/logs/omega_check.log` | 2026-10-01 |
| Growth of max a_n (S5(0.8)): exponent of the certified lower bound vs log₁₀ n | 0.2726 (9.0), 0.3294 (20.3), 0.3493 (29.9), 0.3617 (40.0), 0.3648 (42.6); marginal 0.37–0.46, no decline; model crossing of n^{0.383}: 10⁶⁴–10⁸⁸ | `s5-multiplicity-s40/NOTE.md` §2.4, §5.3; `…/verify/logs/search2_rate_K60.log` | 2026-10-01 |

## §9. Proposed zoo rider (BLOCK format of `results/fejer-form-s39/NOTE.md` §11; NOT inserted — for the next zoo stream)

<!-- BLOCK:i2 -->
- **[RIDER 2026-10-01, Session 40 (`results/s5-multiplicity-s40/NOTE.md` §0, §2.3, §2.5, §4, §5) — dense non-surgery systems on ℕ: integer-level feedback cannot keep β small — the multiplicity obstruction.]** For an ℕ-supported discrete system, C(n) − C(n − 1) = a_n − ρ, so the integer error is at least half the largest multiplicity: β ≥ limsup log a_n/log n. Multiplicity and the surgery class are tied: bounded a_n ⇔ free g-primes (T1), free + N = ρx + O(x^θ) ⇒ refused primes and added composites both O(x e^{−c√log x}) (T2–T3, via Landau's PNT as quoted in DMV 2006 pp. 2–3), while a positive proportion of refused primes forces max_{n≤x} a_n ≥ x^{κ/log log x} (T4′, a Rankin-type lemma on the rank excess). On the program's candidate S5(0.8) (u-offsurgery-s39) the multiplicity grows like a power over every computed scale: a_n ≥ 4.26·n^{0.35} = n^{0.3648} at an explicit n ≈ 3.8·10⁴² (exact count 3,403,961,916,617,140 from 2,525 certified g-prime divisors, two code paths), which makes the hypothesis of Theorem K′ false for every constant its Rouché step tolerates; the certified exponent climbs 0.27 → 0.365 from 10⁹ to 10⁴²·⁶ with marginal 0.37–0.46, and if it passes Re ρ₁/2 = 0.383 the system obeys α ≤ 2β. KILLS: briefs that refute U (or DMV's "θ < ½ ⇒ RH for discrete systems") by an integer-greedy / feedback construction on ℕ while assuming a growth bound for N_P − ρx below the multiplicity exponent; RETURNS them to the multiplicity question (UT-M1/M2). EXECUTABLE TEST: run `verify/search2.c` (v_p-identity scoring) on the candidate's g-primes and compare the certified exponent of max a_n with Re ρ₁/2 before any tail theorem is assumed. `[novelty: single-check]`
<!-- END:i2 -->

## §10. The waste line (KICKSTART 10(o), with 10(m)'s labels)

Found, correctly (not waste): the K integer (stop line (b)), by a search the brief asked for, in 3.7 min of compute after about
15 minutes of tool building. Spent on the wrong thing: the first greedy (`search.c`, full DP per candidate move, 6 min) was superseded by
`search2.c` (one DP per move, all moves scored by the v_p identity) and killed; the one-large-prime split counter (`fsplit.c`)
was built and dropped after it lost a factor 4.7–150 against the full count (cost ~5 min). Label (iii) none: two NOTE slips
fixed in place (an over-broad sentence on E-records; an exponent typo 0.34 → 0.35), a misparsed table fixed by a re-parse.
(ii) budget / stop line — re-queued with the missing input named: task 6 (UT-M4: block-moment scanner, ~1–2 h), the exact system
past 2·10⁹ (§3: ≈ 2 GB of stored a(n) beyond the dump; UT-M3), the 0.383 certification (UT-M2: a lattice-free exact counter).
Candidate LOG line: "s5-multiplicity-s40: K. a_n ≥ 3,403,961,916,617,140 > 3.76 n^0.35 + 3 at n = 2⁸3⁵5⁹7³11²·13·17·19³·23·29²·37·41²
·59·61·79·89·109·149 (10⁴²·⁶; two code paths; dump re-certified by the Ω-identity, 0 failures to 10⁹) — Theorem K′'s hypothesis is
false for every tolerated constant; T1–T4′ (bounded ⇔ free; free ⇒ thin surgery; dense refusal ⇒ x^{κ/log log x}); exponent of
max a_n 0.365 and rising — S5(0.8) likely obeys U. Spent for nothing: one superseded greedy and one lossy split counter (~11 min)."
