# read-O — unit `s5-multiplicity-s40` (Opus reader, second model of the dual check, Session 41)

**Reader:** Opus 5.5 (agent), started 14:44 IST 2026-10-01 under `results/novel-wave-s41/READ-BRIEF-O.md`.
**NOTE read:** `results/s5-multiplicity-s40/NOTE.md`, SHA-256 ced8b67448b79cddb4af13291230b550d15399ccb6fc349bf0fc7e8eaa5370ac,
331 lines (all line numbers below are at this hash). Also read: the unit's `BRIEF.md`, `SHARED.md` (blocks 1–8);
`results/u-offsurgery-s39/NOTE.md` (hash ef143a43…fc668, 236 lines) §2 (definition of S5(ρ)) and §4 (Theorem K′, Lemma H);
the unit's `verify/` sources and logs where a number is relied on (named per item below). NOT opened: any `read-F.md`, any
`verify-F/` folder (independence).
**Re-run:** `verify-O/` (my own code, written from the definitions: `s5gen_O.c`, `lattice_O.c`, `ktest_O.py`, logs in
`verify-O/logs/`); big scratch under `/private/tmp/rh-s41-read-s5mult/` (regeneration commands in §2).

**VERDICT LINE — AGREES-WITH-CORRECTIONS.** The close stands. K: n_K = 2⁸·3⁵·5⁹·7³·11²·13·17·19³·23·29²·37·41²·59·61·79·89·109·149
has f_G(n_K) = 3,403,961,916,617,140 > 3.76·n_K^{0.35} + 3 — reproduced digit for digit by my own exact code by a method
different from both of the NOTE's paths (my own sieve generator of S5(0.8), byte-identical to the dump on [1, 2·10⁹]; a
full-lattice checked-uint64 count), and the consequence "H_θ of Theorem K′ is false for every θ ≤ 0.35 and every constant
c < 1.88; K′ is vacuous as stated" is re-derived at the line. T: T1, T2, T3 (with its converse), Lemma A, T4, T4′ and §5.1 are
re-derived ✓ (no FALSE step; small gaps only: m3, m5, m6). Every number I re-ran reproduces, including the §3 extension and
§2.4's table, which I count exactly. Corrections: F1 the proposed zoo rider's headline asserts a barrier the NOTE itself lists
as open; F2 missed prior art on disk — T1's core is Olofsson 2010 pp. 10–11, the nearest printed relative of T2–T3 is Lagarias
1999 (ℕ-supported + Delone ⇒ finite surgery), and §5.1 is already in the program's record; F3 the U-implication in §0 and the
rider drops its condition α = Re ρ₁. 3 FIX-FIRST items (5 pairs), 12 minor items (13 pairs): 18 OLD/NEW pairs.

## §1. Re-derivations at the line (✓ = re-derived step by step; GAP; FALSE)

**1.1 §2.1 identity (l. 62–72) ✓.** Double count Σ_M Σ_{x∈M} h(x) = h(n)f(n) (complete additivity). Per copy c of q,
Σ_M mult_M(c) = Σ_{k≥1} #{M : mult_M(c) ≥ k}, and removing k copies is a bijection onto multisets of product n/q^k (inverse:
add k copies; needs q^k | n). h = v_p: terms with p ∤ q vanish, v_p(n/q^k) < v_p(n). If p ∥ n then v_p(q) = 1 and k = 1
(q² ∤ n), giving f(n) = Σ_{p|q|n} m_q f(n/q) ✓. (This last case is also the direct statement "exactly one factor contains p".)

**1.2 §2.3 consequence (l. 100–106) ✓.** E(n) − E(n − 1) = N(n) − N(n − 1) − 0.8 = a_n − 0.8. Under |C(u)| ≤ c u^θ for real
u > 10⁹ (C is constant on [n, n + 1), so the integers n_K and n_K − 1 > 10⁹ are covered): a_{n_K} − 0.8 ≤ c n_K^θ + c(n_K − 1)^θ
≤ 2c n_K^{0.35} < 3.76 n_K^{0.35} for θ ≤ 0.35, c < 1.88, contradicting f > 3.76 n_K^{0.35} + 3 (§2.3 here). "Vacuous as stated"
is exact: K′'s hypothesis H_θ (constant 1) is false for every θ ≤ 0.35. The least constant is 2.1324 (l. 104 "≥ 2.13" ✓) and
f_G ≤ (1 + log₂ n)^{|G|} (each exponent ≤ log₂ n; all m = 1) ✓ (l. 17, 105).

**1.3 §2.5 induction (l. 133–139) ✓.** With a(k), m_k correct for k < n, (I) at n reads Ω(n)(a(n) − m_n) = Σ_{q<n, q^k|n}
m_q Ω(q) a(n/q^k); the identity applied to the truncated system G_{<n} gives Ω(n)A(n) = the same sum, because a(d) = f_{G<n}(d)
for d < n (no g-prime ≥ n divides d). Ω(n) ≥ 1 ⇒ a(n) − m_n = A(n), and (II) is then the defining rule (N(n − 1) correct by
hypothesis) ✓. My §2.1 makes the conclusion independent of this argument anyway.

**1.4 §3 (l. 143–150) ✓.** For n ∈ (10⁹, 2·10⁹] a g-prime q < n with q | n has q ≤ n/2 ≤ 10⁹ and n/q^k ≤ 10⁹; so A(n) =
f_{G≤10⁹}(n) and the dump suffices ✓. Numbers reproduced (§2.1).

**1.5 §5.1 (l. 236–241) ✓.** 5E(n) = 5N(n) − 4n − 1 ∈ ℤ; the rule is m_n = max(0, ⌊1.3 − E(n − 1) − A(n)⌋) (0.8(n − 1) + 1 −
N(n − 1) = 0.8 − E(n − 1) ✓). In both cases a_n > 0.3 − E(n − 1) (⌊y⌋ > y − 1; or m_n = 0 ⇒ A(n) > 0.3 − E(n − 1)), so
E(n) > −0.5, hence ≥ −0.4 ✓. m_n ≥ 1 ⇒ A(n) ≤ 0.3 − E(n − 1) ≤ 0.7 ⇒ A(n) = 0, m_n = ⌊1.3 − E(n − 1)⌋ ≤ 1; iff-form ✓
(A(n) ≥ 1 would need E(n − 1) ≤ −0.7). My generator, which allows any m, found max m = 1 and no g-prime with A > 0.
Not new: u-offsurgery-s39 `read-O.md` l. 16 (1.2(b) "E(n) ≥ −½ at every integer", equivalent to ≥ −0.4 since 5E ∈ ℤ) and
l. 234 (A1: "Every multiplicity is 1 … the admission rule is exactly 'A(n) = 0 and E(n − 1) ≤ 3/10'") — see F2.

**1.6 T1 (l. 161–170) ✓.** Exact hypotheses: any discrete system of reals > 1 with finite multiplicities (ℕ-support is not
used). (iii)⇒(ii): two distinct multisets with one product differ by a nonzero exponent vector, a relation. (i)⇒(iii):
m_q ≥ 2 gives the k + 1 multisets "j copies of copy 1, k − j of copy 2" with product q^k; a relation λ = λ⁺ − λ⁻ gives two
distinct multisets of product n₀. Quantitative part: M_j = jM ⊎ (k − j)M′ has product n₀^k and mult_{M_j}(x) = k·mult_{M′}(x)
+ j(mult_M(x) − mult_{M′}(x)) is strictly monotone in j at any x where they differ ✓; r relations: two choices differ by
Σ(j_i − j′_i)λ_i ≠ 0 by linear independence ✓. **In print (core):** Olofsson 2010 p. 10–11 (F2).

**1.7 T2 (l. 172–177) ✓.** Hypothesis: P free, ℕ-supported. V = {g-primes ≤ x} ∖ {primes in (x/2, x]}: its primes are ≤ x/2
and a composite q ≤ x has every prime factor ≤ q/2 ≤ x/2, so V ⊂ ⟨primes ≤ x/2⟩ ≅ ℤ^{π(x/2)}; V is ℤ-independent (T1, m ≤ 1),
so |V| = A(x/2) + K(x) ≤ π(x/2), i.e. K(x) ≤ R(x/2) ✓; (b) by adding A(x) ✓. Sharp (the converse construction attains (a)).

**1.8 T3 (l. 181–190) ✓, quote checked at the page.** DMV (on disk, `novel-wave-s37/beurling-frontier/sources/p1-02-…txt`
l. 99–115) reads: "Landau's reasoning in fact provides a proof that if N_B(x) = κx + O(x^θ) (3) with κ > 0 and 0 ≤ θ < 1, then
ζ_B(s) satisfies (1) and π_B(x) satisfies (2) … π_B(x) = li(x) + O(x exp(−c√((1 − θ) log x))) for x ≥ 2. (5)" (radical lost in
extraction, as the NOTE says), and DMV's setting (l. 80–86) allows λ₁ ≤ λ₂ ≤ … with g-integers "counted with appropriate
multiplicity", so it covers ℕ-supported systems with repeated values ✓. Proof: D(y) = R(y) − R(y/2) ≥ 0 and ≤ π(y) − π_P(y)
by T2(b), ≤ C y e^{−c√((1−θ) log y)}; dyadic sum with log(x/2^j) ≥ ½ log x for x/2^j ≥ √x, remainder ≤ π(√x) ✓; c′ = c√((1−θ)/2).
**Converse ✓:** for R ⊆ odd primes, 2p is the only g-prime with v_p ≠ 0 (p ∈ R), so a relation has λ_{2p} = 0, then λ = 0;
K(x) = #{p ∈ R : 2p ≤ x} = R(x/2); ζ_P = ζ·H, Σ|h(d)|d^{−θ} ≤ Π_R(1 + p^{−θ})(1 − (2p)^{−θ})^{−1} < ∞; N = Σ_d h(d)⌊x/d⌋ =
H(1)x − xΣ_{d>x}h(d)/d − Σ_{d≤x}h(d){x/d}, both error terms ≤ x^θΣ|h(d)|d^{−θ} ✓; H(1) > 0 ✓ (Σ_R 1/p < ∞).
**Attempted counterexample (brief item (c)):** "a free system on ℕ that is dense and not a surgery". Under T3's hypothesis
none exists. Without the power saving one does: take R ⊆ odd primes with R(x) ≍ x/log²x (so Σ_R 1/p < ∞) and the same
(ℙ ∖ R) ∪ {2p}. Then Σ|h(d)|/d < ∞, so N_P(x) = H(1)x + o(x) (Kronecker: Σ_{d≤x}|h(d)| = o(x)), the system is free and dense,
and R(x), K(x) ≍ x/log²x ≫ x e^{−c√log x}. So T3's "O(x^θ)" cannot be relaxed to "∼ ρx" [proved here, single-check — §7 A3].

**1.9 §4(b) (l. 198–206).** (R1) ✓: multisets = j copies of 6 (0 ≤ j ≤ min(v₂, v₃)) plus primes; N = Σ_j⌊x/6^j⌋ = 6x/5 + O(log x).
(R2) **GAP (minor, m3):** "{2p : p prime}" contains 4 = 2·2; with it the factorizations are j₂ copies of 4 and j_p of 2p with
2j₂ + Σ_{p odd} j_p ≤ a, so a_n ≤ τ(m)(⌊a/2⌋ + 1), still ≪ n^ε; the stated "a_n ≤ τ(m)" needs p odd. The divergence argument
(ζ_P(σ)(σ − 1) → ∞) ✓. "S5(0.8) is no candidate (a_{n_K} ≥ 4.26 n_K^{0.35})" (l. 206) overstates: one value cannot refute
a_n ≪ n^ε, and S5(0.8) is not known to satisfy N = ρx + O(x^θ) (m4).

**1.10 Lemma A (l. 209–213) ✓** (wording m5: "sub-multisets" contradicts Z_V = Π(1 − q^{−σ})^{−1}, which counts multisets
with repetition; the proof and every use are the repetition version). Tail ≤ x^{−δ}Z_V(σ − δ) ≤ Z_V(σ)/2; head ≤ max·Z_Q(σ)
since f_V lives on Q-smooth n ✓.

**1.11 T4 (l. 214–221) ✓.** log(1/u) ≤ φ_σ(t) ≤ log(1/u) + u from u e^{−u} ≤ 1 − e^{−u} ≤ u ✓; log Z_V(σ) ≥ |V| log(1/c)
(q ≤ y, c ≤ 1) ✓; log Z_Q(σ) ≤ |Q| log(1/c) + Σ_Q log(log y/log p) + cθ(Q)/log y ✓; tail: φ_{σ/2} − φ_σ ≤ log 2 + (σ/2)log q,
so (σ/2)log x ≥ (|V| + 1)log 2 + (σ/2)Σ_V log q ⇔ the stated condition ✓.

**1.12 T4′ (l. 222–230) ✓.** Exact hypotheses: π_P(y) ∼ y/log y and dyadic refusal Σ_{y/2<p≤y} m_p ≤ (1 − δ)(π(y) − π(y/2)).
V's members have prime factors ≤ y/2 ✓; D ≥ (δ/2 − o(1))y/log y ✓; Σ_{p≤y/2} log(log y/log p) ≪ y/log²y (split at √y;
log(1 + t) ≤ t; Σ_{p≤y} log(y/p) = ∫₂^y π(t)dt/t) ✓; log x = (2 log 2/c + 1)(1 + o(1))y suffices (|V| ≤ π_P(y), Σ_V log q ≤
π_P(y) log y) ✓; κ = (½δ log(1/c) − c log 2)/(2 log 2/c + 1) > 0 for small c ✓; error bound from a_n − ρ ≤ 2 sup|C| ✓. The
two "[recalled, unverified]" Chebyshev inputs are not needed: π(t) ≪ t/log t and θ(y/2) = (½ + o(1))y ≤ y log 2 follow from the
quoted classical PNT (DMV (2), l. 38) for large y (m6). f_V ≤ a_n ✓.

**1.13 §5.3 — what is proved and what is a model (brief item (d)).** Proved: f(nℓ) = Σ_{s|n, ℓs∈G} f(n/s) for ℓ ∤ n, ℓ ∉ G
(the v_p identity at exponent 1), so g_ℓ(n) = f(nℓ)/f(n) is an exact ratio ✓; f_G ≤ (1 + log₂ n)^{|G|} ✓; β ≥ limsup log a_n/log n
(from a_n − ρ ≤ 2 sup|C|) ✓. Model: "≈ (c/ln(ℓs̄))Σ_{s|n}s^{−μ}" (carrier events treated as independent with the §5.2 density,
f(n/s)/f(n) ≈ s^{−μ}); the Bell(w) regime ([heuristic], labeled); the crossing scales (labeled [model]; the arithmetic
L = (rL₀ − F₀)/(r − 0.383) gives 63.5, 71.3, 88.2 for r = 0.42, 0.41, 0.40 ✓). "The true a_n crosses earlier" is plausible, not
proved (a_n ≥ f_G only says the true count is at least as large at the same n). **GAP in the U-sentence (F3):** "if limsup
log a_n/log n > 0.383 … S5(0.8) satisfies α ≤ 2β" needs α ≤ 0.766…, but the record has only α ≥ Re ρ₁ and that only under
H_θ, which §2.3 has just refuted: without H_θ the continuation of ζ_P to the box B, hence the zero itself, is uncertified
(at β ≈ 0.4 the K′ tail at X = 10⁹ is ≈ 0.07c > 0.0394). §5.3 l. 271–272 states the α = Re ρ₁ assumption; §0 l. 18–19 and the
rider l. 316 drop it.

**1.14 The close (§0) against the brief.** K: the brief's K close (BRIEF l. 10) — explicit n > 10⁹, exact integer count from a
stated list, checker script — is met, and I reproduce it by a third method (§2.2–2.3). T: T1–T4′ re-derived ✓ (with m3–m6).
4(b)'s open question is correctly posed and not decided by T4′ (x^{κ/log log x} is compatible with a_n ≪ n^ε) ✓.

## §2. Independent re-run (`verify-O/`; my code only, written from the definitions)

**2.1 The system itself, by a different method.** `verify-O/s5gen_O.c` generates S5(0.8) on [1, 2·10⁹] from the upstream
definition (u-offsurgery-s39 NOTE §2, l. 55–57) by the multiplicative (unbounded-knapsack) sieve: when n is accepted with m
copies, (1 − n^{−s})^{−m} is applied to the whole array at once, so a[n] = A(n) when the walk reaches n. Exact integers
(uint16 below 10⁹, 9-bit packed above, every addition range-checked, int64 N; general m allowed, not assumed ≤ 1). The NOTE's
route was the Ω-recursion (§2.5, §3); mine shares no code or identity with it. 31 s, peak 3.13 GB (`logs/s5gen_O_2e9.log`).
Reproduced, digit for digit:

| quantity | NOTE (line) | mine |
|---|---|---|
| SHA-256 of the g-prime list ≤ 10⁹ (uint32 pairs) | f5563f15…d904a1 (l. 32) | f5563f1548375d70a4e99df97bbd56dfd353fe4dec2a3b749c9ebaae40d904a1 — byte-identical |
| SHA-256 of a[0..10⁹] (uint16) | (dump `aF_r08_1e9.u16`) | 800ce6882c3e518b…bbc60d9d — byte-identical to the dump |
| g-primes ≤ 10⁹; max m; g-primes with A(n) > 0 | 50,829,666; all m = 1 (l. 32–33) | 50,829,666; max m = 1; 0 |
| N(10⁹), C(10⁹) | 800,000,008; 8 (l. 35) | 800,000,008; 8 |
| sup E ≤ 10⁹; a_n there; E(n − 1); inf E | 274.8 at 902,538,000; 276; −0.4; −0.4 (l. 36–37) | same (inf first attained at n = 19) |
| #{2 ≤ n ≤ 10⁹ : a_n = 0} | 539,856,374 (l. 42) | 539,856,374 |
| per-half-decade max a_n, [10⁴·⁵,10⁵) … [10⁸·⁵,10⁹) | 14, 21, 27, 42, 59, 83, 124, 178, 276 (l. 41) | same nine values |
| a-records quoted at l. 40 | 27@957,600 … 276@902,538,000 | all six reproduced |
| E-records in [10⁷, 10⁹]; single spikes (a ≥ 50) | 37; 19, E(n − 1) ≤ 37.6 (l. 37–38) | 37; 19, max E(n − 1) = 37.6 |
| g-primes in (10⁹, 2·10⁹]; SHA of that list | 47,353,731 (l. 146) | 47,353,731; c3aee0f9…9c35, byte-identical to `gp_ext_1e9_2e9.u32` |
| N(2·10⁹), C(2·10⁹) | 1,600,000,009; 9 (l. 146) | 1,600,000,009; 9 |
| max a_n on (10⁹, 2·10⁹]; sup E | 344 at 1,805,076,000; 348.0 at 1,805,076,001 (l. 147–148) | same |
| decade shares d = 4, 6, 8 (A = 0; accepted among A = 0) | 0.477/0.196, 0.541/0.121, 0.594/0.0844 (l. 247–249) | 0.4765/0.1961, 0.5407/0.1205, 0.5935/0.0844 |

So §1 (C1), §2.5's conclusion and §3 now rest on two independent generators that agree byte for byte; §3's "one code path"
label can be upgraded (minor pair m2).

**2.2 The decisive count, by a different method.** `verify-O/gdiv_O.py` enumerates the divisors ≤ 10⁹ of n_K (500,886 of them
≥ 2) and keeps those in MY list: **2,525, largest 999,086,975**, the same set as `verify/certK/K1_gdiv.txt` (2dfd9f2c…036e, set
equality checked). `verify-O/lattice_O.c` then counts f_G(n_K) over the **full** divisor lattice of n_K (τ = 238,878,720 cells,
uint64, every addition overflow-checked; one in-place knapsack pass per g; no top-prime reduction, no v_p identity, no modular
arithmetic — a different method from both of the NOTE's paths): **f_G(n_K) = 3,403,961,916,617,140, overflow 0**, 58 s,
1.91 GB (`logs/lattice_O_K1.log`). By-product: f_G(n_K/(89·109·149)) = 8,495,083,868,529. The same code, same list, gives the
self-tests 276 (902,538,000) and 26 (478,800), agrees with a_n at 24 random n ≤ 10⁹ (12 random, 12 multiples of 720,720),
and reproduces C3: **20,390 (148 g-prime divisors), 2,932,627 (318), 13,461,378,553 (652)** (`logs/lattice_O_C3.log`).

**2.3 The K inequality** (`verify-O/ktest_O.py`, exact integers + 60-digit Decimal; `logs/ktest_O.log`): (25(f − 3))²⁰ > 94²⁰n_K⁷
is TRUE; n_K = 3779321386617192025903153574378164500000000 (43 digits; l. 87 ✓); log₁₀ n_K = 42.5774138; log f/log n =
0.3647940; f/(3.76 n^{0.35}) = 1.134232; f/n^{0.35} = 4.264713; least admissible constant at θ = 0.35: (f − 0.8)/(2n^{0.35})
= 2.132357; margin +0.054702 in log₁₀. Even with c = 1.88 the hypothesis fails at n_K for every θ ≤ **0.351285**.
Rouché tolerance (upstream K′ box): at σ = 0.7459, t = 30.346, |s|X^{0.35−σ}/(σ − 0.35) = 0.020968 and |C(X)|X^{−σ} =
8·10^{−9σ} = 1.5·10⁻⁶, so the tail is ≤ c·0.020968 + 1.5·10⁻⁶ < 0.0394 iff c < 1.8790 — the NOTE's 1.876 = 0.0394/0.0210 is the
rounded, slightly conservative form; the conclusion "every c < 1.88" stands.

**2.4 The §2.4 search table, now exact** (`logs/lattice_O_table24.log`; same code and list). The NOTE's intermediate rows are
float-DP values from `search2.c`; I counted the six integers of the log exactly: f_G = **40,956** (log₁₀ n = 15.1731),
**4,847,695** (20.2983), **505,225,453** (25.4327), **28,461,915,556** (29.9325), **4,962,514,307,328** (35.6233),
**285,712,680,063,860** (39.9646; τ = 127,401,984, overflow 0). Their log₁₀ f are 4.6123, 6.6855, 8.7035, 10.4543, 12.6957,
14.4559 and the exponents 0.3040, 0.3294, 0.3422, 0.3493, 0.3564, 0.3617 — the NOTE's table l. 118–125, to every printed digit.

**2.5 Primes, carriers, inf E** (`verify-O/primes_O.c`, own sieve to 2·10⁹, `logs/primes_O.log`; `logs/carrier_share_O.log`;
`logs/infE_halfdecades_O.log`). π(2·10⁹) − π(10⁹) = 47,374,753 (l. 146 ✓). Decades 4, 6, 8: accepted / refused / composite
g-primes 1,601 / 6,762 / 6,807; 65,657 / 520,424 / 520,957; 3,523,361 / 41,562,718 / 41,543,940 (l. 247–249 ✓). Refused primes
≤ 149: 5, 19, 29, 41, 59, 61, 79, 89, 109, 139, 149 (eleven; n_K uses all but 139 — l. 108–109 ✓; the eight other primes of n_K
are accepted). The first 30 refused primes end at 359 and c_ℓ(10⁹)·ℓ/10⁹ ranges over 0.0390–0.0466 (l. 254: 0.039 … 0.047 ✓;
8,147,069 / 2,244,986 / 379,987 / 265,851 for ℓ = 5, 19, 109, 149 ✓). Accepted share among non-representable multiples of ℓ in
decade 8, times ln(10^{8.5}): 1.25 (ℓ = 5), 1.81 (19), 1.76 (29), 1.65 (109), 1.66 (149) (l. 256 ✓); the non-representable
share of multiples is 0.46–0.49 for ℓ ≥ 19 and 0.63 for ℓ = 5 ("about half", l. 257 ✓). min 5E = −2 in each of the 16
half-decades [10¹, 10^{1.5}) … [10^{8.5}, 10⁹) (l. 37 ✓). (These two scans read the dump's a-array, which §2.1 proved
byte-identical to mine.)

**2.6 One sentence that does not reproduce as worded** (l. 37–39): "the other 18 add ≤ 2.2 each (one adds 14.2) within 76
integers after a spike". The 18 counts, the step sizes and the 14.2 reproduce, but five of the 18 (13,376,008 … 13,376,077) are
209,008–209,077 integers after the nearest a_n ≥ 50 (13,167,000); they follow a_n = 14 at 13,376,000 (E 43.6 → 56.8), which
the sentence's own definition of "spike" (a_n ≥ 50) excludes, and 13,376,077 is 77 after it. Minor pair m1.

**2.7 Regeneration** (run from `results/s5-multiplicity-s40/`; S = `/private/tmp/rh-s41-read-s5mult`): `clang -O2 -o $S/s5gen_O
verify-O/s5gen_O.c && $S/s5gen_O $S` (31 s, 3.13 GB; writes `gp_O_1e9.u32` 407 MB and `gp_O_ext.u32` 379 MB to S);
`python3 verify-O/gdiv_O.py K1 '2^8,3^5,5^9,7^3,11^2,13,17,19^3,23,29^2,37,41^2,59,61,79,89,109,149' verify-O/certO/K1_gdiv_O.txt`;
`clang -O2 -o $S/lattice_O verify-O/lattice_O.c && $S/lattice_O verify-O/certO/K1_gdiv_O.txt` (58 s, 1.91 GB);
`python3 verify-O/ktest_O.py 3403961916617140`; `clang -O2 -o $S/primes_O verify-O/primes_O.c && $S/primes_O` (9 s).

## §3. Prior art at the page

| Source | Where read | What it says (quoted) | Bearing |
|---|---|---|---|
| Olofsson, "Properties of the Beurling generalized primes", preprint dated 8 July 2010; J. Number Theory 131 (2011) 45–58, DOI 10.1016/j.jnt.2010.06.014 (Crossref record, `verify-O/sources/crossref-olofsson.json`) | on disk: `novel-wave-s37/beurling-fe/sources/olofsson-2010-properties-beurling-primes.txt` l. 658–662 (paper pp. 10–11) | "if two different Beurling integers have the same value α, then there are at least n + 1 different Beurling integers having the value αⁿ, hence the remainder term is of at least logarithmic growth" | T1's quantitative core ("any relation forces a_{n₀^k} ≥ k + 1", log growth) is in print; NOTE l. 279–281 says "not found stated in the on-disk corpus" (F2) |
| Lagarias, "Beurling generalized integers with the Delone property", Forum Math. 11 (1999) 295–312 | zbMATH review Zbl 0927.11047 (fetched via the zbMATH Open API, `verify-O/sources/zbmath-api-lagarias.json`); the on-disk abstract `…/lagarias-1999-delone-abstract.md` is truncated; summaries on disk: Olofsson l. 649–658, Ruzsa p. 1 | review: "the author succeeds in classifying all such semigroups which are contained in the natural numbers. He proves that the set of generalized primes P consists of all but finitely many ordinary primes, plus finitely many other composites"; Delone: "R ≥ n_{i+1} − n_i ≥ r … This implies that G has the unique factorization property" | The printed "free ℕ-supported systems are surgeries" theorem — under bounded gaps, with a FINITE surgery. T3 is its analogue under N = ρx + O(x^θ) with a thin (infinite allowed) surgery; T3's converse shows infinite thin surgeries exist there (they have unbounded gaps, consistent with Lagarias). Not cited in the NOTE (F2) |
| Ruzsa, "Beurling integers with lacunarity", arXiv 2311.11127v1 (Math. Pannonica) | fetched, `verify-O/sources/ruzsa-2311.11127v1.{pdf,txt}`, p. 1 l. 23–31 | "If G is a set of multiplicatively independent integers, B will be a subset of positive integers, hence b_{i+1} − b_i ≥ 1. If furthermore G contains all but finitely many primes, then b_{i+1} − b_i will also be bounded from above. Lagarias [3] proved that there is no other example consisting of integers" | Confirms the Lagarias statement; Ruzsa's theorems concern non-integer generators (separated reals), outside the NOTE's ℕ-supported setting |
| Diamond–Montgomery–Vorhauer, Math. Ann. 334 (2006) pp. 2–3 | on disk, l. 80–86, 99–115 | quoted in 1.8 | The NOTE's one printed input, correctly quoted; setting covers multiplicities ✓ |
| Hilberdink, Acta Arith. 152 (2012) 217–241 | on disk, `novel-wave-s37/beurling-frontier/sources/p3-22c2-…txt` abstract | "if N has finitely many discontinuities per bounded interval, then N must be the counting function of the g-prime system containing the usual primes except for finitely many" | As the NOTE says (l. 279–280) ✓ |

Search for T2's rank count, T3, Lemma A/T4/T4′ themselves: not found on disk (grep of the s37–s40 sources for
"multiplicatively independent", "Delone", "rank", "Rankin" in Beurling sources) nor in the arXiv titles already on disk
(`dz-half-s39/sources/arxiv-generalized-numbers-2023-09-to-2026-10.txt`); I ran no new arXiv query (§8).

## §4. FIX-FIRST pairs (three items, five pairs; NOTE line numbers at hash ced8b674…70ac)

**F1 — the proposed zoo rider's headline states as a barrier what the NOTE itself lists as open.** T1–T3 prove: bounded
multiplicity ⇒ free ⇒ (with N = ρx + O(x^θ)) thin surgery; T4′ proves only max a_n ≥ x^{κ/log log x} under dense refusal,
which allows β = 0; §4(b) (l. 204–206) and UT-M5 state the dense-refusal case as open. "Cannot keep β small" for all dense
non-surgery systems on ℕ is therefore unproved; what is shown is one system's data (S5(0.8)) plus the theorems.
OLD (l. 316): — dense non-surgery systems on ℕ: integer-level feedback cannot keep β small — the multiplicity obstruction.]**
NEW (l. 316): — dense non-surgery systems on ℕ: the multiplicity obstruction — bounded multiplicity forces a thin surgery (T1–T3), and on the program's candidate S5(0.8) integer-level feedback did not keep the multiplicity below n^{0.35}; that every dense non-surgery system on ℕ has β bounded below is not proved (§4(b), UT-M5).]**

**F2 — missed prior art, on disk, that changes two labels.** (i) T1's quantitative core is printed in Olofsson 2010 (pp. 10–11;
on disk, `novel-wave-s37/beurling-fe/sources/olofsson-2010-properties-beurling-primes.txt` l. 658–662). (ii) The printed
theorem closest to T2–T3 is Lagarias 1999 (ℕ-supported + Delone ⇒ ℙ minus finitely many primes plus finitely many composites;
Zbl 0927.11047, fetched; on-disk summaries in Olofsson l. 649–658 and in Ruzsa 2311.11127 p. 1), not cited. (iii) §5.1 is
already in the program's record (u-offsurgery-s39 `read-O.md` l. 16 and A1 at l. 234), so its novelty label goes.
OLD (l. 281): systems are rigid" theme, in a different regime); not found stated in the on-disk corpus. Lemma A is Rankin's trick run in reverse
NEW (l. 281): systems are rigid" theme, in a different regime). In print and on disk: T1's quantitative core — Olofsson, preprint of 8 July 2010 (= J. Number Theory 131 (2011) 45–58, DOI 10.1016/j.jnt.2010.06.014), pp. 10–11 (`novel-wave-s37/beurling-fe/sources/olofsson-2010-properties-beurling-primes.txt` l. 658–662): "if two different Beurling integers have the same value α, then there are at least n + 1 different Beurling integers having the value αⁿ, hence the remainder term is of at least logarithmic growth"; and the nearest printed relative of T2–T3, Lagarias, Forum Math. 11 (1999) 295–312 (Zbl 0927.11047): an ℕ-supported system with the Delone property (bounded gaps) is ℙ minus finitely many primes plus finitely many composites (also reported by Olofsson l. 649–658 and Ruzsa, arXiv 2311.11127, p. 1). T3 is the analogue with N = ρx + O(x^θ) in place of bounded gaps and a thin, possibly infinite, surgery in place of a finite one (the converse construction has unbounded gaps). Lemma A is Rankin's trick run in reverse
OLD (l. 283): - **Novelty: single-check** for T2(a)/(b), T3's converse construction, T4/T4′, §5.1, and the K certificate (a computation).
NEW (l. 283): - **Novelty: single-check** for T2(a)/(b), T3 and its converse construction (new as statements beside Lagarias 1999), T4/T4′, and the K certificate (a computation, reproduced by an independent method in read-O §2). T1: core in print (Olofsson 2010, pp. 10–11). §5.1: already in the record (u-offsurgery-s39 `read-O.md` 1.2(b)–(c) and A1).

**F3 — the U-implication drops its condition in §0 and in the rider.** β > Re ρ₁/2 gives "α ≤ 2β" only if α = Re ρ₁ ≈ 0.766.
The record has α ≥ Re ρ₁ only, and only under H_θ (Theorem K′'s continuation step), which §2.3 refutes; a zero further right
(UT-M4) raises the threshold. §5.3 (l. 271–272) states the assumption; l. 19 and l. 316 drop it.
OLD (l. 19): limsup log a_n/log n > 0.383 = Re ρ₁/2, then β ≥ that and S5(0.8) obeys α ≤ 2β — no counterexample to U at all (§5.3) [model].
NEW (l. 19): limsup log a_n/log n > 0.383 = Re ρ₁/2, then β ≥ that, and S5(0.8) is no counterexample to U provided α = Re ρ₁ ≈ 0.766 — not established: the record gives α ≥ Re ρ₁ only under H_θ, now refuted, and a zero further right would raise the threshold (§5.3) [model].
OLD (l. 316): and if it passes Re ρ₁/2 = 0.383 the system obeys α ≤ 2β.
NEW (l. 316): and if it passes Re ρ₁/2 = 0.383 the system obeys α ≤ 2β provided α = Re ρ₁ (no zero further right; uncertified once H_θ fails).

## §5. Minor pairs (twelve items, thirteen pairs)

m1 — E-record sentence (2.6 here).
OLD (l. 38–39): the other 18 add ≤ 2.2 each (one adds 14.2) within 76 integers after a spike
NEW (l. 38–39): the other 18 add ≤ 2.2 each (one adds 14.2): 13 of them within 8 integers after a spike, the five at 13,376,008–13,376,077 within 77 integers after a_n = 14 at 13,376,000
m2 — §3 has a second, independent code path now (read-O §2.1: byte-identical lists and a-array).
OLD (l. 141): ## §3. The exact system beyond 10⁹ (task 3) [computed, one code path]
NEW (l. 141): ## §3. The exact system beyond 10⁹ (task 3) [computed, two code paths: Ω-recursion here, multiplicative sieve in read-O §2.1; byte-identical]
OLD (l. 310): one code path (Ω-recursion generator)
NEW (l. 310): two code paths (Ω-recursion generator; read-O's multiplicative sieve, byte-identical g-prime list SHA c3aee0f9…9c35)
m3 — (R2) contains 4 = 2·2, so "a_n ≤ τ(m)" fails as stated (1.9 here).
OLD (l. 201): (R2) ℙ ∪ {2p : p prime}:
NEW (l. 201): (R2) ℙ ∪ {2p : p odd prime}:
m4 — one value cannot refute a_n ≪ n^ε; S5(0.8)'s density is unproved.
OLD (l. 206): S5(0.8) is no candidate (a_{n_K} ≥ 4.26·n_K^{0.35}, §2.3).
NEW (l. 206): S5(0.8) is not a plausible candidate on the evidence (a_{n_K} ≥ 4.26·n_K^{0.35}, §2.3), though no finite computation refutes a_n ≪ n^ε and its density ρ = 0.8 is unproved.
m5 — Lemma A counts multisets with repetition (Z_V is Π(1 − q^{−σ})^{−1}).
OLD (l. 210): sub-multisets with product n,
NEW (l. 210): multisets of elements of V (repetition allowed, copies distinguished) with product n,
m6 — the Chebyshev inputs follow from the quoted classical PNT; no recalled input is needed.
OLD (l. 227–228): (Chebyshev π(t) ≪ t/log t [recalled, unverified — classical, elementary]). And θ(Q) ≤ θ(y/2) ≤ y log 2 (Chebyshev, same label).
NEW (l. 227–228): (π(t) ≪ t/log t, from the quoted classical PNT, DMV (2), l. 38). And θ(Q) ≤ θ(y/2) = (½ + o(1))y ≤ y log 2 for large y (same source).
m7 — the cited path does not exist.
OLD (l. 280): `fr/sources/p3-22c2`,
NEW (l. 280): `novel-wave-s37/beurling-frontier/sources/p3-22c2-hilberdink-2012-generalised-prime-systems-periodic-counting.txt`,
m8 — the intermediate exponents were float-DP values; they are now exact (read-O §2.4).
OLD (l. 311): exponent of the certified lower bound vs log₁₀ n
NEW (l. 311): exponent of the exact lower bound f_G(n) (exact at all six points: NOTE §2.3 and read-O §2.4) vs log₁₀ n
m9 — the marginal range 0.37–0.46 holds from 10¹⁵ on (l. 127: 0.31–0.37 below).
OLD (l. 18): with marginal exponents 0.37–0.46 and no decline (§2.4) [computed]
NEW (l. 18): with marginal exponents 0.37–0.46 from 10¹⁵ on (0.31–0.37 below) and no decline (§2.4) [computed]
m10 — the rider's test uses a float scorer; certification needs an exact count.
OLD (l. 316): compare the certified exponent of max a_n with Re ρ₁/2 before any tail theorem is assumed.
NEW (l. 316): count the best integer it finds exactly (`verify/fcert.c`, or a full-lattice exact count as in read-O §2.2), and compare that exponent with Re ρ₁/2 before any tail theorem is assumed.
m11 — the LOG line carries F3's unstated condition.
OLD (l. 331): max a_n 0.365 and rising — S5(0.8) likely obeys U.
NEW (l. 331): max a_n 0.365 and rising — S5(0.8) likely obeys U if α = Re ρ₁.

m12 — against BARRIER-ZOO I.2 (brief item (e)): I.2's Session-38 rider (1) already answers DMV's question non-constructively
(Prop. 2.1 of `novel-wave-s37/beurling-frontier`), so the rider should not describe it as a claim to refute. Otherwise the
proposed BLOCK:i2 sits consistently under I.2 (an ℕ-supported sub-case of the factory; its KILLS clause matches the frontier
rider's "surgery pays integer error"), once F1, F3b and m10 are applied.
OLD (l. 316): (or DMV's "θ < ½ ⇒ RH for discrete systems")
NEW (l. 316): (or give a constructive answer to DMV's question "does θ < ½ imply RH for discrete systems?", which I.2's rider (1) answers non-constructively)

**Total: 3 FIX-FIRST items (5 OLD/NEW pairs) and 12 minor items (13 pairs) — 18 pairs.**

## §6. Novelty per result

| Result | Verdict |
|---|---|
| K certificate (a_{n_K} ≥ 3,403,961,916,617,140 at n_K; H_θ of K′ false for θ ≤ 0.35, c < 1.88) | new (a computation on the program's own construction); now reproduced by a third, independent method |
| §2.1 identity (any completely additive h) | elementary; the h = log case is the classical recursion a(n) log n = Σ Λ_P(d)a(n/d) (cited at u-offsurgery-s39 NOTE l. 64); no novelty claim needed |
| T1 | **in print (core)**: Olofsson 2010, pp. 10–11 (relation ⇒ a_{α^n} ≥ n + 1 ⇒ log growth); the equivalence (i)–(iii) and the r-relation product bound are routine extensions |
| T2 (rank count K(x) ≤ R(x/2)) | new as a statement (not found on disk, nor in arXiv queries q1–q4 below); elementary |
| T3 (free + N = ρx + O(x^θ) ⇒ thin surgery) | new as a statement on printed cores: Landau's PNT (DMV 2006 pp. 2–3) and the rigidity theme of Lagarias 1999 (Delone ⇒ finite surgery) |
| T3 converse ((ℙ ∖ R) ∪ {2p}) | new as a statement; elementary |
| 4(b) examples R1, R2; the open question | elementary examples; the open question is well posed (T4′ does not decide it) |
| Lemma A, T4, T4′ | new as statements (Rankin-type), single-check; not found |
| §5.1 | **in the program's record** (u-offsurgery-s39 `read-O.md` 1.2(b)–(c), A1) |
| §5.2 data, §5.3 model | computations (reproduced, §2.5 here) and a heuristic, correctly labeled except F3 |

arXiv API, run 15:05–15:08 IST, one query at a time (`verify-O/sources/arxiv-O-q1…q4.xml`): abs:Beurling AND
abs:"unique factorization" (0 hits); abs:"generalized integers" AND abs:Beurling AND abs:"natural numbers" (0); abs:Beurling
AND abs:multiplicatively (46 hits; the only relevant one is Ruzsa 2311.11127, read); abs:Beurling AND abs:"rational
integers" (0).

## §7. Additions (single-check, Opus reader)

**A1. Third method for the K close.** Generator by the multiplicative sieve (not the Ω-recursion) and count over the full
divisor lattice in checked uint64 (no top-prime reduction, no modular arithmetic): byte-identical system on [1, 2·10⁹], and
f_G(n_K) = 3,403,961,916,617,140 digit for digit (§2). The K close no longer rests on the orchestrator's dump.

**A2. The §2.4 table is exact** at all six intermediate integers (§2.4 here) — the climb 0.2726 → 0.3040 → 0.3294 → 0.3422 →
0.3493 → 0.3564 → 0.3617 → 0.3648 is a sequence of exact lower bounds, not float estimates.

**A3. T3's power-saving hypothesis cannot be dropped** [proved here]: R ⊆ odd primes with R(x) ≍ x/log²x, P = (ℙ ∖ R) ∪ {2p}
is free with N_P(x) = H(1)x + o(x) and R(x), K(x) ≍ x/log²x (1.8 here).

**A4. Infinite thin surgeries have unbounded gaps** [proved here], so T3's converse never meets Lagarias's Delone class: in
P = (ℙ ∖ R) ∪ {2p : p ∈ R} (2 ∉ R) an integer n is a g-integer iff v₂(n) ≥ Σ_{p∈R} v_p(n). Given k, take distinct p₁, …, p_k ∈ R
and, by the Chinese remainder theorem, n with n ≡ 1 mod 2^{M} (M = ⌈log₂(k + 1)⌉ + 1, so v₂(n + i) ≤ log₂ k + 1 for 1 ≤ i ≤ k) and
n + i ≡ p_i^{e_i} mod p_i^{e_i+1} with e_i = v₂(n + i) + 1; then n + 1, …, n + k are not g-integers.

**A5. Sharper constants for the K consequence:** at n_K, H_θ with constant 1.88 fails for every θ ≤ 0.351285; the exact Rouché
tolerance at X = 10⁹ (with the known C(10⁹) = 8 term kept separate) is c < 1.8790 (§2.3 here). By-product for future
cross-checks: f_G(n_K/(89·109·149)) = 8,495,083,868,529.

## §8. What I could not check, and why

- Lagarias 1999 itself (paywalled at De Gruyter; zbMATH's HTML is a bot wall): read through the zbMATH Open API review
  (Zbl 0927.11047, quoted) and the on-disk summaries of Olofsson and Ruzsa. It enters only a prior-art label (F2), never a
  verdict on the NOTE's mathematics.
- Olofsson: the preprint of 8 July 2010 (pp. 10–11) was read; the journal version (JNT 131, 45–58) was not opened, so its page for the quoted sentence is not given. My arXiv queries q5–q6 found no arXiv record of it.
- Upstream inputs not re-run here: the box B and min|F_X| = 0.0394 of u-offsurgery-s39 §2.2(a) (that unit's claim, read there).
- `search2.c`'s float scoring was not audited line by line; it is no longer load-bearing (every table integer is now exact).
- Carrier probabilities: spot-checked for 5 of the 30 refused ℓ (§2.5); the c_ℓ range for all 30.
- Task 6 (zeros of F_X to height 300): not run by the NOTE (stop line), so nothing to check.

