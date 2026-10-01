# read-O — unit `s5-multiplicity-s40` (Opus reader, second model of the dual check, Session 41)

**Reader:** Opus 5.5 (agent), started 14:44 IST 2026-10-01 under `results/novel-wave-s41/READ-BRIEF-O.md`.
**NOTE read:** `results/s5-multiplicity-s40/NOTE.md`, SHA-256 ced8b67448b79cddb4af13291230b550d15399ccb6fc349bf0fc7e8eaa5370ac,
331 lines (all line numbers below are at this hash). Also read: the unit's `BRIEF.md`, `SHARED.md` (blocks 1–8);
`results/u-offsurgery-s39/NOTE.md` (hash ef143a43…fc668, 236 lines) §2 (definition of S5(ρ)) and §4 (Theorem K′, Lemma H);
the unit's `verify/` sources and logs where a number is relied on (named per item below). NOT opened: any `read-F.md`, any
`verify-F/` folder (independence).
**Re-run:** `verify-O/` (my own code, written from the definitions: `s5gen_O.c`, `lattice_O.c`, `ktest_O.py`, logs in
`verify-O/logs/`); big scratch under `/private/tmp/rh-s41-read-s5mult/` (regeneration commands in §2).

(Sections below are filled as the read proceeds; the VERDICT LINE is written last, at the top of §0.)

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
label can be upgraded (minor pair m3).

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

