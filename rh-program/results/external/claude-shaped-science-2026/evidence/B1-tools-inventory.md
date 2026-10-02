# B1 — Tools inventory (evidence reader, side-session 2026-10-03)

Question (BRIEFS.md §B1): what reusable computational tools has the program built, where do they live, and how often did a later unit REUSE an earlier unit's code rather than write its own?

## Plan (at most 20 lines)

1. Census: list every code file (.py .c .sh .lean .rs .go .jl .gp .sage .m) under `rh-program/results/` and `rh-program/scripts/`, excluding `.lake/` and `sources/` folders; record size by folder (Python os.walk, no `$(ls)`).
2. Classify: print the first 25-30 lines (or module docstring) of each .py/.c/.sh in batches of 30-40 files; assign FUNCTION class and ROLE (WRITER / READER / INFRA) from folder and file names and headers; record in the working table below as I go.
3. Reuse: grep `sys.path`, cross-folder `import`, `cp `, `exec(open`, `runpy`, `importlib` across unit folders; `shasum -a 256` over all code files, group identical hashes across folders; grep NOTE files and briefs for "reused|reuses|adapted from|from results/".
4. Tool bugs: grep LOG.md (windowed), digests' §E, read-O/read-F files for `bug|float|drift|block-edge|off-by-one|overflow|precision loss|wrong window`.
5. Index: look for README/INDEX/MANUAL files, STATUS.md "Key artifacts", Instruments tables in `rh-program/directions/*.md`.
6. Write Tables 1-3, "Index or manual", "Counts"; append a dated block to SHARED.md after each batch.

Status (2026-10-03): complete — census, working table, Tables 1–3, Index or manual, Counts written below.

## Working table (classification, filled batch by batch)

Method. Census by a Python `os.walk` over `rh-program/results/` and `rh-program/scripts/`, skipping `.lake/`, `sources/`, `__pycache__/`; extensions .py .c .h .cpp .sh .lean .rs .go .js. Result: **1081 files** — 799 .py (779 in `results/`, 20 in `scripts/`), 126 .sh, 57 .c, 55 .lean, 33 .js (all in `scripts/`), 4 .h, 3 .rs, 3 .cpp, 1 .go. Every .py/.c/.sh/.cpp/.h/.rs/.go file (993) had its module docstring or leading comment block (first 30 lines) printed in batches of 40 and was classified from it; the classification is kept as path rules (first match wins) so the tallies below are computed, not hand-counted.

Roles. **W** = writer (a unit's own producer, including its own `verify/` checks and dual producers/scouts); **R** = reader (folders `verify-O/`, `verify-F/`, `check-O/`, `check-o/`, `checker-O/`, `referee-s14/`, `audit*/`, `verify-orch/`, `orch-verify/`, third-evaluation; the orchestrator's read-F re-runs are counted here); **I** = infra (zoo insertion, record editing, lint, apply-pairs, packaging, arXiv watch polls, the `scripts/*.js` workflow scripts); **C** = packaging copy (`results/arxiv/haglund-counterexample/certificate/`, byte copies of `haglund-cert-s37`).

Function classes. GEN generators of g-prime systems (S5, S7, S8, necklaces, thinning T_α, Diamond–Zhang); CNT counting functions N(x), E(x) and their statistics; ZL zeta/L/Beurling-zeta values and zeros (incl. Davenport–Heilbronn, Hurwitz, Epstein, ξ_N chains, zeros of F_X); CERT interval/ball-arithmetic certificate producers and checkers; WEIL explicit-formula / Weil-functional evaluators and their test-function constants; FIT fits and exponent estimates; SIEVE sieves and prime tables; LEAN comparator runners, statement-identity and trust-grep tools, axiom-print probes; PDF text extraction / fetch helpers; LIT arXiv novelty searches and watch polls; LINT linters, quote checks, OLD/NEW amendments, apply-pairs; REC record editing and zoo insertion; WF workflow scripts; LP linear programs and optimizations; RMT CUE Monte Carlo; LY Lee–Yang constructions; ARITH curves over F_q, function-field and number-field arithmetic; QC self-dual measures / quasicrystal designs; EXACT finite exact-arithmetic lemma checks; BENCH cost benchmarks; MOD other unit-specific numerics; PKG arXiv packaging check.

| folder (`rh-program/results/…`) | files | kB | roles | function classes (count) |
|---|---|---|---|---|
| a4-m2-gate | 11 | 150 | W11 | MOD 6, LP 4, RMT 1 |
| a4-no-go | 19 | 113 | W19 | MOD 12, LP 5, CERT 1, RMT 1 |
| arxiv | 19 | 68 | R2 I1 C16 | CERT 17, PKG 1, PDF 1 |
| beta-shapes-s35 | 11 | 52 | W3 R8 | LINT 5, LIT 4, MOD 2 |
| c2-followups | 1 | 42 | I1 | REC 1 |
| c2-m2 | 35 | 249 | W23 R11 I1 | WEIL 23, ZL 11, REC 1 |
| c2-m4 | 22 | 48 | W14 R8 | LEAN 18, WEIL 3, CERT 1 |
| c2-m5 | 6 | 40 | W6 | WEIL 2, ZL 2, MOD 2 |
| c2-m5b | 6 | 39 | W3 R3 | WEIL 2, ARITH 2, ZL 2 |
| c2-m6 | 18 | 108 | W18 | WEIL 15, ZL 3 |
| c2-r1 | 6 | 32 | W6 | WEIL 3, ZL 3 |
| c2-siegel | 8 | 82 | W4 R4 | ZL 8 |
| c3-m0-epstein | 1 | 8 | W1 | ZL 1 |
| c3-r | 16 | 97 | W1 R15 | EXACT 15, MOD 1 |
| ccm-dh-test | 12 | 58 | W12 | WEIL 9, ZL 2, FIT 1 |
| conj-O-s38 | 27 | 77 | W14 R13 | CNT 14, GEN 10, ZL 2, LIT 1 |
| d1-m0 | 9 | 63 | W9 | BENCH 4, WEIL 2, CERT 2, ZL 1 |
| d1-m1 | 39 | 314 | W14 R25 | CERT 29, LEAN 9, BENCH 1 |
| d1-m2a | 89 | 1908 | W63 R26 | LEAN 54, CERT 35 |
| d1-m3 | 2 | 22 | W2 | CERT 2 |
| d2-scout-s26 | 1 | 2 | R1 | EXACT 1 |
| d4-infty-s36 | 5 | 41 | W4 R1 | LIT 3, MOD 2 |
| d4-sign-sweep | 29 | 204 | W13 R15 I1 | WEIL 27, LINT 2 |
| d5-lean-s30 | 9 | 25 | W5 R4 | LEAN 9 |
| dz-half-s39 | 21 | 55 | W12 R9 | CNT 11, GEN 7, FIT 2, LIT 1 |
| e1-m5u | 6 | 17 | W3 R3 | ARITH 4, WEIL 2 |
| e3-borger-rung1 | 5 | 30 | W3 R2 | ARITH 5 |
| e5-kappa-s29 | 25 | 122 | W13 R10 I2 | LP 17, WEIL 6, REC 2 |
| f1-spec-s29 | 4 | 39 | W1 R3 | ARITH 2, LINT 1, PDF 1 |
| fejer-form-s39 | 17 | 57 | W10 R7 | ARITH 11, ZL 2, LP 2, WEIL 2 |
| free-greedy-s40 | 59 | 182 | W34 R25 | GEN 27, ZL 21, CNT 6, WEIL 2, FIT 1, SIEVE 1, LIT 1 |
| grossmann-rescout-s22 | 18 | 94 | W18 | LY 13, ARITH 5 |
| h4-pair-lean-s33 | 15 | 28 | W7 R8 | LEAN 12, MOD 3 |
| h4-pair-typing-s32 | 1 | 4 | W1 | LEAN 1 |
| h5-c2-lean-s32 | 7 | 10 | W3 R4 | LEAN 7 |
| haglund-cert-s37 | 16 | 60 | W16 | CERT 15, PDF 1 |
| i1-witness-lean-s32 | 11 | 13 | W3 R8 | LEAN 11 |
| iv17-lean-s30 | 11 | 18 | W5 R6 | LEAN 11 |
| lemmaB-s41 | 110 | 309 | W73 R37 | GEN 35, CERT 27, CNT 25, EXACT 9, ZL 7, MOD 5, ARITH 2 |
| lemmaG-s39 | 25 | 71 | W15 R10 | CNT 9, GEN 8, ARITH 5, ZL 2, SIEVE 1 |
| linux-check-s30 | 2 | 10 | I2 | LEAN 2 |
| local-greedy-s40 | 28 | 71 | W16 R12 | ZL 13, GEN 10, FIT 2, CNT 2, SIEVE 1 |
| novel-wave-s36 | 74 | 268 | W69 R5 | ZL 53, LY 9, LIT 5, CERT 3, ARITH 2, MOD 1, PDF 1 |
| novel-wave-s37 | 42 | 127 | W20 R22 | GEN 13, ZL 11, ARITH 8, FIT 4, CNT 3, LIT 1, LP 1, PDF 1 |
| program-digest-s25 | 1 | 0 | R1 | ZL 1 |
| qcond-s38 | 7 | 37 | W4 R3 | QC 5, ARITH 2 |
| qtwin-s39 | 15 | 41 | W6 R9 | QC 13, ARITH 2 |
| s5-multiplicity-s40 | 17 | 62 | W11 R6 | GEN 17 |
| scripts/ | 55 | 756 | I55 | WF 33, REC 19, LEAN 2, LINT 1 |
| theoremR-lean-s36 | 27 | 69 | W9 R18 | LEAN 21, LINT 4, MOD 2 |
| u-offsurgery-s39 | 31 | 58 | W14 R17 | GEN 18, ZL 10, LIT 2, FIT 1 |
| watch-S-record-eisenberg-2026-09 | 1 | 0 | R1 | ZL 1 |
| watch-lamzouri-2609.02882 | 1 | 6 | R1 | ZL 1 |
| watch-poll-s34 | 1 | 3 | I1 | LIT 1 |
| watch-poll-s35 | 2 | 7 | I2 | LIT 2 |
| watch-poll-s37 | 1 | 3 | I1 | LIT 1 |
| zoo-s25 | 8 | 15 | R6 I2 | ZL 4, LINT 1, SIEVE 1, EXACT 1, REC 1 |
| zoo-s26 | 2 | 8 | W1 I1 | LINT 1, ZL 1 |
| zoo-s27 | 5 | 28 | R2 I3 | LINT 3, ARITH 1, ZL 1 |
| zoo-s28 | 2 | 20 | I2 | LINT 1, REC 1 |
| zoo-s30 | 1 | 19 | I1 | REC 1 |
| zoo-s31 | 1 | 22 | I1 | REC 1 |
| zoo-s36 | 2 | 27 | I2 | REC 2 |
| zoo-s37 | 3 | 43 | I3 | REC 3 |

Role totals of the census: W 612, R 371, I 82, C 16 (sum 1081). Classification caveats: the role is read from the folder name and the docstring, not from a run; dual producers (`haglund-cert-s37/producer-A`, `producer-B`) and dual scouts (`grossmann-rescout-s22/pair2-lee-yang/F`, `/O`) are counted as W; orchestrator pre-derivations and read-F re-runs as R; `.lean` files under `results/` are axiom-print probes and scratch checks (the Lean library itself is `rh-program/lean/`, outside this scope).

## Table 1 — Per function class

Counts are files from the census (W = writer, R = reader; "u" = distinct top-level folders under `results/`). For the generator class the rows count distinct generator PROGRAMS per system, from the headers. "Validated against" quotes the record; "reused" says how a later unit got the code: import, copy, adaptation (declared in the header), run as a subprocess, data reuse, or rewritten.

| class | writer implementations | reader / checker implementations | languages | validated against (record) | reused by a later unit? |
|---|---|---|---|---|---|
| GEN, S8 free greedy | **11 programs, 2 streams**: `free-greedy-s40` `proto/s8_proto.py`, `compute/verify/s8_port.c`, `s8gen.c`, `s8win.c`, `theory/verify/s8_check.py`, `s8_mech.py`, `s8_realzero.py`, `s8w_block.py`; `lemmaB-s41` U1 `rules.cpp`/`rules2.cpp`, U4 `s8sp.c`, U5 `s8u5.c`, U6 `s8cert.c`, U7 `s8gen.c` | **10**: `s8o.cpp`, `s8_sqrt2_small_o.py`, `s8dd.c`, `r08_exact.py`, `legendre_check.py` (s40 reads); U1 `bf_greedy.py`, `bf_s8w.py`; U3 `s8gen.c`; U5 `s8_O.py`; U6 `s8gen.c` + `s8g_*.h`, `brute.py`; `lemmaB-s41/orch-verify/s8_meansq.py` | C, C++, Python | `lemmaB-s41/U6-certificate/read-O.md` l. 301: "generator agrees cell by cell with a 60-digit mpmath brute force at 2·10⁵ and count for count with two other generators (s8o, s8cert)" | Within s40 by port: `s8_port.c` l. 1 "line-by-line C port of proto/s8_proto.py". Across streams **rewritten**: `lemmaB-s41/CHARTER.md` l. 28 "Existing generators to cross-check against (never to import)"; U5 `s8u5.c` l. 1 "U5-obstruction's own S8(rho) generator"; pairwise line similarity ≤ 0.25. One copy: U3 `t1_check.py` l. 1 "Event loop copied from orch-verify/s8_meansq.py". Data reuse: U6 `crosscheck.py` l. 2 compares "with the s8o log of Session 40". |
| GEN, S5 integer greedy | **2 programs, 1 unit**: `u-offsurgery-s39/verify/pseudoN.c`, `pseudoN_check.py` (route 2); `s5-multiplicity-s40` (11 W files) counts on a dump | **5**: `u-offsurgery-s39/verify-O/gen.c`, `gen2.c`; `verify-F/s5gen_F.c`, `integer_greedy_rederive.py`; `s5-multiplicity-s40/verify-O/s5gen_O.c` | C, Python | `s5-multiplicity-s40/verify/omega_check.c` l. 1: "INDEPENDENT certification of the S5(4/5) dump by a different" route | Data, not code: `s5-multiplicity-s40/NOTE.md` l. 32 "`gpF_r08_1e9.u32`: SHA-256 f5563f1548375d70…d904a1 (matches the brief)". |
| GEN, S7 local greedy | **2**: `local-greedy-s40/verify/s7gen.c`, `s7dp.c` | **2**: `verify-O/gen7o.c`, `dp7o.c` | C | `s7dp.c` l. 1: "independent check of s7gen: S7(num/den) by the ADDITIVE dynamic program over multiples (as S5's generator" | Not found (method borrowed from S5, code not). |
| GEN, thinning T_α and deletion families | **4**: `novel-wave-s37/beurling-frontier/verify/thin.c`, `thin_aux.c`; `conj-O-s38/verify/thin2.c` (+ copy `thin_fr.c`); `lemmaG-s39/verify/lg.c` + `lg_core.h` | **6**: M1b `verify-O/thin_O.py`, `verify-F/rerun_thinning_numpy.py` (+ `_Y1e9`); `conj-O-s38/verify-O/thin_O.py`; `lemmaG-s39/verify-O/o_sieve_bins.c`, `o_neck_gen.py`, `o_sq_gen.py` | C, Python | `beurling-frontier/verify/check_small.py` l. 1: "Brute-force cross-check of thin.c (bern mode) on a small instance: same hash, same R, recount N_P and rho." | **Copy + extension**: `conj-O-s38/verify/thin2.c` l. 1 "Extends the frontier NOTE's thin.c (copied verbatim as thin_fr.c; same hash". **Format**: `lemmaG-s39/verify/lg_core.h` l. 1 "Bins and CSV format identical to cO/verify/thin2.c". |
| GEN, Diamond–Zhang random systems | **1**: `dz-half-s39/verify/dzgen.py` + `dzcommon.py` | **1**: `dz-half-s39/verify-O/dzsim.py` ("read-O independent simulation of the Diamond-Zhang construction", l. 1) | Python | not found | Not found. |
| GEN, other systems | `lemmaB-s41/U2-structured/verify/fq_greedy.py`, `pkappa.c`; `novel-wave-s37/beurling-fe/verify/v2_lsq_exotic_search.py` | `s5-multiplicity-s40/verify-O/lattice_O.c` | Python, C | not found | Not found. |

| CNT, N(x), E(x) and statistics | 48 files, 7u (`lemmaB-s41` 21, `conj-O-s38` 7, `lemmaG-s39` 6, `dz-half-s39` 5 incl. `dzcount.c`, `free-greedy-s40` 5, `local-greedy-s40` 2, `novel-wave-s37` 2) | 22 files, 6u (e.g. `dz-half-s39/verify-O/gcount.c` "read-O own enumerator of Beurling g-integers", l. 1) | Python, C | `conj-O-s38/verify/t3_rung1.py` l. 2: "the dyadic mean-square code must reproduce fr Prop. 5.1, rho 2^\|R\| / 12" | **Copy + import**: `lemmaG-s39/verify/dyadic.py` l. 2 "imported from dyadic_ms_cO.py, a verbatim copy of cO/verify/dyadic_ms.py". Otherwise rewritten per unit. |
| ZL, zeta / L / Beurling-zeta values and zeros | 113 files, 17u (`novel-wave-s36` 51, `free-greedy-s40` 15, `c2-m2` 8, `local-greedy-s40` 7, `u-offsurgery-s39` 7, …) | 50 files, 17u | Python (mpmath, python-flint/Arb), C, sh | Davenport–Heilbronn builder `ccm-dh-test/dh.py` l. 2 "construction, functional-equation check"; cited as "the on-disk validated source results/ccm-dh-test/dh.py lines 5-8" (`d1-m1/producer_mp.py` l. 70). Certified zeta zeros: `novel-wave-s36/fingerprint/verify/u3a_zeros_chunk.py` l. 2 "zeta zeros with Arb (acb.zeta_zeros, Platt-type". | **Import (the most reused module of the program)**: `ccm-dh-test/dh.py` imported by `c2-m2` (6 files), `c2-m6` (6), `d1-m0` (1), `novel-wave-s36` fingerprint and ly-infinity (1 each), e.g. `c2-m6/verify/dh_scaling_check.py` l. 7 "sys.path.insert(0, os.path.join(HERE, '..', '..', 'ccm-dh-test')); import dh". **Rewritten**: the zero finder for the truncation F_X of a g-prime system exists in `u-offsurgery-s39/verify/zscan.c` (l. 1 "evaluate zeta_P(s) = rho*zeta(s) + sum_{n<=X} (a_n - rho) n^{-s} for an N-supported system"), `local-greedy-s40/verify/zline.c` (l. 1, same formula), `free-greedy-s40/compute/verify/zeta_bm.py`, and the lemmaB-s41 U5/U6 evaluators; line similarity < 0.25. |
| CERT, interval / ball certificates | 71 files, 9u (`d1-m2a` 27, `haglund-cert-s37` 15, `d1-m1` 12, `lemmaB-s41` 10, …) + 15 packaging copies | 46 files, 5u (`d1-m1` audits F and O, `d1-m2a/audit`, `d1-m2a/dr8/check-o`, `lemmaB-s41` U1/U6 read-O, orchestrator third evaluation) | Python (mpmath `iv`, python-flint/Arb), C headers | `d1-m1/acceptance/crosscheck.py` l. 1 "Two-producer cross-check (D-R3 / m2a-m2b-design sec. 4 stop-the-line rule)"; `d1-m1/audit_O_lean_vs_py.py` l. 1 "DIFFERENTIAL TEST of the Lean kernel checker"; `lemmaB-s41/U6-certificate/read-O.md` l. 8 "Both certificates are reproduced by an independent second producer" | **Import**: `d1-m2a/ft_mp.py` l. 7 "``results/d1-m1/ball.py`` (imported; the complex rectangular-interval class ``Ball``"; also `d1-m2a/lane-a/p9_mp.py`. **Adaptation**: `d1-m2a/producer_mp.py` l. 9 "It is the M1 producer (``results/d1-m1/producer_mp.py``"; `d1-m2a/producer_arb.py` l. 16 "ball->integer helpers are copied from THIS leg's M1 producer". The Session-37 and Session-41 Arb certificates (`haglund-cert-s37`, `lemmaB-s41` U1/U6) are new code. |
| WEIL, explicit formula / Weil functional | 67 files, 12u (`c2-m2` 15, `c2-m6` 15, `d4-sign-sweep` 13, `ccm-dh-test` 9, …) | 31 files, 7u (incl. `d4-sign-sweep/checker-O/twsumO.go`) | Python, Rust, Go | `d4-sign-sweep/checker-O/compare.py` l. 1: "\|dP\|, \|dW\| of checker-O (twsumO) against Job 1's JSONs, tolerance 1e-10 + phase line" | **Import**: `ccm-dh-test/weilform.py` by `d1-m0` (`chi3_conductor_point.py` l. 47 `STACK = … 'ccm-dh-test'`; `m0i_certify.py` l. 50; `lambda_ladder_runner.py` l. 2 "the DH Weil-form stack (results/ccm-dh-test/weilform.py)"). **Adaptation**: `d4-sign-sweep/harness/d4_twisted_sum.rs` l. 1–2 "the M6 twisted sum `results/c2-m6/verify/twisted_sum.rs` carried above the verified height. Every change against the M6 source is marked `// D4:`"; `d4_arch.py` l. 2 "M6's ef_rhs_arch.py carried". **Copy**: Table 2 row 3. |
| LEAN, comparator runner, statement identity, trust greps, axiom probes | 80 files, 10u (`d1-m2a` 36, `c2-m4` 13, `theoremR-lean-s36` 7, `h4` 6, `d5` 5, `iv17` 5, `h5` 3, `i1` 3, …) | 73 files, 9u (`check-O/` of each Lean unit, `d1-m2a/packaging/check-o`) | sh, Python, Lean | `scripts/linux-comparator-check.sh` l. 2: "the program's independent kernel run on a LINUX host, with a REAL landrun sandbox" | **The most copied tool family**: byte copies or docstring-only edits in 7 units from Session 23 (`c2-m4`) to Session 36 (`theoremR-lean-s36`): Table 2 rows 4–6 and N1–N4. Checkers copy the builder's runner, e.g. `h5-c2-lean-s32/check-O/run.sh` l. 2: "the builder tools/run.sh with ONLY the tree path changed". |

| LP, linear programs and optimizations | 21 files, 4u (`e5-kappa-s29` 10, `a4-no-go` 5, `a4-m2-gate` 4, `fejer-form-s39` 2) | 8 files, 2u | Python (numpy/scipy) | `e5-kappa-s29/verify/rung0.py` l. 2: "dress rehearsal of the pipeline (kappa_pipeline.py) on instances with a KNOWN answer" | Not found across units. Within E5 the reader's `verify-O/rerun/` holds byte copies of the writer's pipeline (Table 2 row 9; `rung0A.py` l. 2 keeps the writer's docstring "rung0.py -- dress rehearsal of the pipeline"). |
| FIT, fits and exponent estimates | 7 files, 5u (`fit.py`, `fit7.py`, `fit_bins.py`, `finisher_fits.py`, …); most fits sit inside analysis scripts counted under CNT | 4 files, 3u | Python | not found; readers refit, e.g. `free-greedy-s40/compute/verify-O/fits_o.py` l. 1 "refit sup E (S8(pi/4)) against c log^2 x, c log^k x, C x^b" | Not found (no import of a fit module across folders). |
| SIEVE, sieves and prime tables | 1 standalone file; sieves are embedded in the generators (`conj-O-s38/verify/thin2.c` l. 1 "same hash, sieve, E1, bins") | 3 standalone (`gapo.c`, `o_sieve_bins.c`, `zoo-s25/verify-O/r6_S_count_L20.py`) | C, Python | not found | Readers write their own on purpose: `conj-O-s38/verify-O/thin_O.py` l. 3 "Shares no code with verify/: own segmented prime sieve"; `lemmaG-s39/verify-O/o_sieve_bins.c` l. 1 "nothing taken from verify/lg.c". |
| LIT, arXiv novelty searches and watch polls | 10 W files, 8 R, 4 I (watch polls) in at least 11 folders (`beta-shapes-s35`, `d4-infty-s36`, `conj-O-s38`, `dz-half-s39`, `u-offsurgery-s39`, `free-greedy-s40`, four `novel-wave-s36` seeds, `proof-mine`) | (included) | sh, Python | not applicable | **Rewritten per unit**: no cross-unit pair shares 50% of lines. Watch polls copied session to session (Table 2 row 11). |
| PDF / fetch / text extraction | 5 files: `haglund-cert-s37/producer-B/lit/html2txt.py` (l. 1 "Convert a saved DLMF page to plain text"), `novel-wave-s36/staircase/lit/tools/fc.sh` (l. 2 "Firecrawl scrape helper"), `proof-mine/verify/fetch_sources.sh`, `f1-spec-s29/verify-O/page_quotes_O.py` (l. 2 "extracting the named PDF page (pdftotext -layout)"), packaging copy | — | Python, sh | not applicable | Not found. |
| LINT, linters, quote checks, OLD/NEW amendments, apply-pairs | 1 W (`theoremR-lean-s36/tools/lint_10g.py`), 10 R, 8 I | — | Python | not applicable | Mostly rewritten (no pair ≥ 0.5 similar). **Run as a subprocess**: `zoo-s36/verify/numbers_check.py` l. 30 `LINT_S27 = ROOT / "results/zoo-s27/verify/lint_s27.py"`, l. 274 "lint_s27.py exit 0 on the proposed file"; also `zoo-s37/verify/numbers_check.py`. One shared tool: `scripts/apply-read-pairs.py` l. 2 "Apply the OLD/NEW pairs of a read file to a NOTE (Session 41)." |
| REC, record editing and zoo insertion | 32 I files: 18 `scripts/zoo-insert-sNN.py` (Sessions 16–41), 4 pre-reader copies, zoo-stream gate tests and numbers checks, `c2-followups/scripts/populate_instruments_untried.py`, `e5-kappa-s29/verify/finalize_note.py`, `repatch_note.py` | — | Python | not applicable | One new script per zoo session; consecutive scripts share 0.00–0.46 of lines (the inserted text is inside each script, so this overstates rewriting). |
| WF, workflow scripts | 33 `scripts/*.js` (dated Aug 11 – Sep 9 by file time; names carry sessions up to s19) | — | JavaScript | not applicable | One file per workflow run. |
| ARITH, QC, LY, EXACT, MOD, BENCH, RMT | ARITH 28 W/12u; QC 8 W/2u (`qcond-s38`, `qtwin-s39`); LY 21 W/2u (`grossmann-rescout-s22`, `novel-wave-s36/ly-infinity`); EXACT 7 W/1u; MOD 31 W/10u; BENCH 5 W/2u (`d1-m0`, `d1-m1`); RMT 2 W/2u | ARITH 23 R/11u; QC 10; LY 1; EXACT 19 R/4u; MOD 5 | Python | not applicable | Unit-specific; no cross-unit import or copy found except Table 2 row 3 and `zoo-s27/verify-O/witt_diag_O.py`, which names `d2-scout-s26/verify-orch/witt_diag_degree.py`. |

## Table 2 — Duplicate-hash groups

Method: `sha256` (Python `hashlib`, same digest as `shasum -a 256`) of every one of the 1081 files. **30 groups of byte-identical files (69 files); 29 span two or more folders.** A second pass hashed each file with comments, blank lines and the module docstring stripped, which adds **5 near-identical groups** (copies that differ only in a header line). Paths are under `rh-program/results/` unless they start with `scripts/`.

| # | files (role) | what is copied, and the copy's own words |
|---|---|---|
| 1 | 16 pairs: `haglund-cert-s37/producer-A/*` (6) and `producer-B/*` (10) (W) = `arxiv/haglund-counterexample/certificate/producer-A`, `producer-B` (C) | packaging copy of the dual-producer certificate for the arXiv deposit; not reuse by a later unit |
| 2 | `novel-wave-s36/staircase/verify-F/haglund_direct_arb.py`, `rerun_N27.py` (R) = `arxiv/…/certificate/third-evaluation/` (R) | packaging copy of the orchestrator's read-F re-run: "Orchestrator's own re-run (Session 37, read-F): Haglund's Xi_N evaluated LITERALLY" (`haglund_direct_arb.py` l. 1) |
| 3 | `c2-m5/verify-next/gevrey_edge_law.py` (W) = `c2-m2/verify/gevrey_edge_law_rerun.py` (W) | cross-unit byte copy: "sanity computation for candidate M2 (mandatory repair 2)" (l. 2 of both) |
| 4 | `run.sh` ×5: `c2-m4/verify`, `verify-iii`, `verify-A`, `verify-B`, `d1-m2a/packaging/comparator-run` (W) | the comparator runner: "Job 3 runner: run leanprover/comparator on one config from the Lean repository root" (l. 2) |
| 5 | `statement_identity_*.py` ×5: `c2-m4/verify`, `verify-iii`, `d5-lean-s30/tools`, `h5-c2-lean-s32/tools`, `i1-witness-lean-s32/tools` (W) | each later copy still carries the Session-23 docstring: "statement_identity_m4.py -- the challenge/solution statement-identity check for the M4 (i) topics (Session 23)" |
| 6 | `trust_greps_*.py` ×5, same five folders (W) | "trust_greps_m4.py -- KICKSTART 10(j) trust greps, comments stripped, for the M4 (i) Lean files (Session 23)" |
| 7 | `conj-O-s38/verify/dyadic_ms.py` = `lemmaG-s39/verify/dyadic_ms_cO.py` (W) | imported by `lemmaG-s39/verify/dyadic.py` l. 2: "imported from dyadic_ms_cO.py, a verbatim copy of cO/verify/dyadic_ms.py" |
| 8 | `novel-wave-s37/beurling-frontier/verify/thin.c` = `conj-O-s38/verify/thin_fr.c` (W) | `conj-O-s38/verify/thin2.c` l. 1: "Extends the frontier NOTE's thin.c (copied verbatim as thin_fr.c; same hash, sieve, E1, bins and CSV format" |
| 9 | `e5-kappa-s29/verify/kappa_pipeline.py`, `rung0B.py` (W) = `e5-kappa-s29/verify-O/rerun/` copies (R) | the reader re-ran the WRITER's code from a copy; the docstring reads "the E5 writer's primal/dual pipeline" (`verify-O/rerun/kappa_pipeline.py` l. 2) |
| 10 | `scripts/linux-comparator-check.sh` = `linux-check-s30/fixed-script/linux-comparator-check.fixed.sh` (I) | "the program's independent kernel run on a LINUX host, with a REAL landrun sandbox" (l. 2) |
| 11 | `watch-poll-s35/poll.py` = `watch-poll-s37/poll.py` (I) | the Session-37 copy keeps "Session 35 watch poll (orchestrator, zero agents)" (l. 2); `watch-poll-s34/poll.py` is 0.92 line-similar |
| 12 | `scripts/zoo-insert-s31.py` = `zoo-s31/zoo-insert-s31.pre-reader.py` (I) | pre-reader snapshot of the same insertion script |
| 13 | `d1-m2a/v11/glue-axioms-scratch.lean` = `repair-axioms-scratch.lean` (W) | same folder; a 427-byte axiom-print scratch file |
| N1 | `statement_identity_*.py`: 9 files in 6 units (`c2-m4` ×4, `d5-lean-s30`, `h4-pair-lean-s33`, `h5-c2-lean-s32`, `i1-witness-lean-s32`, `iv17-lean-s30`) | identical code after stripping comments; e.g. `h4-pair-lean-s33/tools/statement_identity_h4.py` l. 1: "the H5 tool byte for byte but for this docstring (Session 33, H4)" |
| N2 | `trust_greps_*.py`: 8 files in 5 units (`c2-m4` ×4, `d5`, `h5`, `i1`, `iv17`) | `h4-pair-lean-s33/tools/trust_greps_h4.py` l. 1: "the H5 tool with this docstring and the default file list changed" |
| N3 | `tools/run.sh` of `d5-lean-s30`, `h4-pair-lean-s33`, `h5-c2-lean-s32`, `i1-witness-lean-s32`, `iv17-lean-s30` (W) | `h5-c2-lean-s32/tools/run.sh` l. 2: "a byte-level copy of the D5 runner (results/d5-lean-s30/tools/run.sh)" |
| N4 | `h4-pair-lean-s33/check-O/run-clone.sh` (R) ≈ `theoremR-lean-s36/tools/run.sh` (W) | a later WRITER's runner equals an earlier CHECKER's runner after comment stripping; `theoremR-lean-s36/tools/run.sh` l. 2: "a byte-level copy of the H4 runner (results/h4-pair-lean-s33/tools/run.sh)" |
| N5 | `c2-m4/verify-A-O/stmt_identity_AO.py` ≈ `c2-m4/verify-B-O/stmt_identity_BO.py` (R) | the same checker's tool reused between its two jobs |

Outside these groups, the generator, zero-scanner and counter programs were compared pairwise by line similarity (Python `difflib`): the eight S8 generator programs of `free-greedy-s40` and `lemmaB-s41` share at most 25% of lines with one another, except `free-greedy-s40/compute/verify/s8gen.c` ~ `s8win.c` (0.79, same unit; `s8win.c` l. 1: "WINDOWED version of s8gen.c"). The 22 arXiv-query and watch-poll scripts share under 50% of lines across units (the watch polls of Sessions 34, 35 and 37 are 0.90–1.00 similar). The 19 lint and amendment scripts share under 50% of lines pairwise.

## Table 3 — Recorded tool bugs

Scope searched: `rh-program/LOG.md` (all lines, Python windows), the three wave digests, and all 112 `read-O*`, `read-F*`, `CHECK-O*`, `AUDIT*`, `referee*` and `*digest*` files under `results/`, for `bug|off-by-one|overflow|precision loss|wrong window|block-edge|fused-op`, then `float|drift|precision` in LOG.md and the digests. The LOG hits for "overflow" at l. 131, 157, 177, 215 concern agent output-token ceilings, not code, and are left out. Paths under `results/` unless stated.

| # | tool (role; session written) | what the bug was and what it changed (verbatim) | who caught it; when |
|---|---|---|---|
| 1 | `free-greedy-s40/proto/s8_proto.py` (orchestrator prototype; S40) | LOG l. 2225: "the charter's N(10^7) = 7,853,984 is the prototype's row value one event past 10^7; the exact count is 7,853,983); the prototype's incremental deficit drifts off the lattice beyond about 10^8 in double precision" | the compute unit (writer), S40; listed among charter errors caught by units, `novel-wave-s39/insights-digest.md` l. 528 "the charter's prototype drifts its g-primes by float error" |
| 2 | `free-greedy-s40/compute/verify/s8gen.c` (W; S40) | digest l. 512 (§E.9 F1): "'Certified' ordering rested on an asserted double-double error the code never bounds; now PROVED to 10¹⁰ by read-O's generator." A label, not a number, changed | read-O (own generator `s8o.cpp`), S41 |
| 3 | `free-greedy-s40/theory/verify/` double-precision run (W; S40) | digest l. 507 (§E.8 F2): "The floating-point audit omitted one of two decision classes; stated ordering margins 9–21× too large; certificates stand." | read-O (`s8dd.c`, 60-digit recheck), S41 |
| 4 | `free-greedy-s40/theory/verify/s8w_block.py` (W; S40) and `lemmaB-s41/U1-lookahead/verify/rules*.cpp` (W; S41) | LOG l. 2264: "can drop composites exactly on block edges — no effect at τ = ½ for π/4, π/16, wrong answers at small τ; after the fix the generator matches a 50-digit brute force". Effect on S40: LOG l. 2286 "w = 50 at 10⁷ sup E 58.18 → 49.67 and 171.18 → 336.18" | U1 writer found it in its own code, S41; U1 read-O showed it reaches S40 (`lemmaB-s41/U1-lookahead/read-O.md` l. 207 "F3 — the generator bug reaches the s40 randomized runs"); lag 1 session |
| 5 | `free-greedy-s40/compute/verify-O/s8o.cpp` (R; S41) | `free-greedy-s40/compute/read-O.md` l. 201: "the 92-bit format overflows above ~1.7·10¹⁰) — not run". A stated limit; no number changed | its author (reader), S41 |
| 6 | `d4-sign-sweep/checker-O/twsumO.go` (R; S25) | LOG l. 1689: "the checker's own fused-op bug (1.7·10⁻²⁰·t) passed the 10⁻¹⁰ tolerance and was caught only by the mpmath phase self-test"; `d4-sign-sweep/CHECK-O-A.md` l. 147 "The Go-contraction bug of §1 is a lesson for any future compiled second implementation in Go" | the checker's own self-test against mpmath, S25 (LOG l. 1689 lies in the Session 25 entry, from l. 1670) |
| 7 | `scripts/linux-comparator-check.sh` (I; S30) | `program-digest-s32.md` l. 22: "a brace group `{ …; exit $rc; } > "$L"`, which runs in the current shell", lines 91–92; LOG l. 1876 "ended run 1 after one config" | "found by the sponsor's run" (`program-digest-s32.md` l. 94), recorded in Session 32 (LOG l. 1872 heading); lag 2 sessions; fixed script adopted into the repo |
| 8 | `d1-m1/ball.py` premise, mpmath leg (W; S8) | `d1-m1/AUDIT-F.md` l. 14 (F-1 MAJOR): "mpmath 1.3.0's `iv` transcendental primitives are NOT correctly directed-rounded: `mpf_exp(x, 288, round_ceiling)` fell BELOW the true value in 11 of 40,000 samples"; repair "by outward inflation" (l. 161) | AUDIT F (reader), S14; lag about 6 sessions |
| 9 | `d1-m1/producer_mp.py` (W; S8) | `AUDIT-F.md` l. 15 (F-2 MAJOR): "with the legal option `--A 0` (A = 1) it EMITS a checker-ACCEPTED `exclusion` transcript (m = 0) for the DH live-fire rectangle, which contains a zero — a false certificate". Non-default path; l. 10: "the DH live fire, and every published number survive" | AUDIT F (reader), S14 |
| 10 | `d1-m2a` packaging generator (W) and the checker's extractor (R) | `d1-m2a/packaging/CHECK-O.md` l. 328–330: "my own extractor was mis-attaching docstrings across back-to-back one-line declarations, the same class of bug Job 1 records fixing in its generator. Fixed, then 79/79." | each by its own author |
| 11 | `theoremR-lean-s36/check-O/identity_checker.py` (R; S36) | `CHECK-O.md` l. 78–80: "[C] FAILED because it located "import Mathlib" by substring … a bug of the checker's script, kept as `statement-identity-run1-buggy.log`" | its author (checker), S36 |
| 12 | `iv17-lean-s30` checker script (R; S30) | `iv17-lean-s30/CHECK-O.md` l. 129: "`re.split` (my bug, fixed)" | its author, S30 |
| 13 | `e1-m5u/verify-O/rung1_pair_check.py` (R) | `e1-m5u/read-O.md` l. 136: "my first run counted y over F₄₉ for N₁ — a reader bug, fixed and logged" | its author (reader) |
| 14 | `novel-wave-s36/fingerprint/verify/` (W; S36) | `novel-wave-s36/insights-digest.md` l. 289: "bugs fixed in-run (15-digit zero parse, a missing Jacobian e^v, 53-bit constants; unit 3)" | the writer, in-run, S36 |
| 15 | `novel-wave-s36/staircase/verify/` (W; S36) | `novel-wave-s36/digest-SHARED.md` l. 19: "re-verification radius bug; rigor_xi1 crash on interval->float" | the writer, in-run, S36 |

Split. Caught by the tool's own author or its own self-test: rows 5, 6, 10–15 (8 rows; row 1 by the next agent to run the code). Caught by an independent reader or audit: rows 2, 3, 4 (effect on S40), 8, 9 (5 rows). Caught by the sponsor's run: row 7. Results that changed: row 1 (a charter count by one event), row 4 (S40 randomized-rule numbers); rows 2, 3 changed labels or stated margins; rows 8–9 changed no published number per `AUDIT-F.md` l. 10.

## Index or manual

- **Program-wide tool index, manual or register: not found.** Scope: file names matching `README|INDEX|MANUAL|TOOLS|INSTRUMENTS|CATALOG|REGISTER` (.md/.txt) anywhere in `rh-program/` outside `fetched*/`, `sources*/`, `.lake/`; 14 files match, every one about a single package or folder (below).
- **STATUS.md "Key artifacts"** (l. 71: "## Key artifacts (all durable, in this directory)") lists six items at l. 73–78, all documents or text extractions (`results/full-map.md`, `results/map-hooks.txt`, `results/literature.md`, `results/design-proposals.json`, `sources-extracted/`, the original PDFs). It names no script.
- **Instruments tables.** `directions/README.md` l. 34: "Every direction file gains two sections … `## Instruments` — a table (quantity | current best value | result file | dated), recording, never ranking". 8 of the 12 direction files have one (table lines: A3 3, A4 22, B2 51, B3 8, B4 5, C2 79, C3 27, D1 29). They record quantities; code appears only in the "result file" column (A4 4 code files named, B2 4, C2 30 mostly Lean, C3 10, D1 7; A3, B3, B4 none). Example `directions/B2-refutation-program.md` l. 146: "PROVED to 10¹⁰ for π/4, π/16, π/32 … by read-O's 128-bit fixed-point generator … \| `free-greedy-s40/compute/verify/s8win.c`; `compute/verify-O/s8o.cpp`". The wave-3 digest carries rows for them: `results/novel-wave-s39/insights-digest.md` l. 417 "§D Instruments rows — the four Session-40 units only".
- **Per-package manuals.** `scripts/README-LINUX-CHECK.md` (49 lines; "A self-contained package to re-run, on a Linux machine, the machine-checked verification of two Lean units", l. 3) and its S33 sibling; `results/arxiv/haglund-counterexample/certificate/README.md` (127 lines; "Reproducibility archive for the paper", l. 3); `rh-program/lean/README.md` (723 lines; the Lean files, outside this scope).
- **Registers of results, not tools.** `results/d1-m3/README.md` l. 3: "the program's durable register of certified ζ-exclusion boxes"; `rh-program/THEOREM-LEDGER.md` (theorems).
- **Rules about reusing code.** Not found in `KICKSTART.md` or `BRIEF-WARNINGS.md` (patterns `reuse|re-use|existing (code|script|generator|tool)|never import`; the only hits are KICKSTART l. 76, a Lean challenge file "that never imports" the solution, and l. 88, reuse of proved results). The one written rule on code is a prohibition in a charter: `results/lemmaB-s41/CHARTER.md` l. 28 "Existing generators to cross-check against (never to import)". Reader independence is stated file by file, e.g. `results/c2-m2/campaign/check-O/ind_transform.py` l. 3 "Nothing is imported from campaign_lib.py"; `results/d1-m2a/dr8/check-o/kappa_o.py` l. 3 "dr8/kappa_check.py is NOT imported, read or executed".

## Counts

**Code files by role** (1081 files under `results/` and `scripts/`, outside `.lake/` and `sources/`): WRITER 612, READER 371, INFRA 82, packaging COPY 16. Without the 55 `.lean` probes (W 28, R 27) and the 33 `.js` workflow scripts (I): W 584, R 344, I 49, C 16 (993 files). Readers wrote 37% of all code files (371 / 1081) and 35% of the non-Lean, non-JS code (344 / 993).

**Function classes with three or more WRITER implementations of the same object** (distinct programs, from the headers):
- S8 generator: 11 programs in 2 streams (`free-greedy-s40`, `lemmaB-s41` U1, U4, U5, U6, U7), plus 10 reader generators. Pairwise line similarity across units ≤ 0.25.
- Zero finder / evaluator for the truncation F_X of a g-prime system: at least 4 units (`u-offsurgery-s39`, `free-greedy-s40`, `local-greedy-s40`, `lemmaB-s41`), each its own code.
- Thinning and deletion-family generators: 4 programs in 3 units (one verbatim copy and two extensions among them).
- arXiv novelty-search helpers: at least 11 folders, none sharing 50% of lines with another unit's.
- Zoo-insertion scripts: 18, one per zoo session; lint scripts: at least 5 units.
- By file count, 16 classes have three or more WRITER files: ZL 113, GEN 88, LEAN 80, CERT 71, WEIL 67, CNT 48, MOD 31, ARITH 28, LP 21, LY 21, LIT 10, QC 8, EXACT 7, FIT 7, BENCH 5, PDF 3.

**Cross-unit reuse found:**
- *Imports*: 21 WRITER files in 5 units (`c2-m2` 6, `c2-m6` 6, `d1-m0` 5, `d1-m2a` 2, `novel-wave-s36` 2) import 4 modules from 2 earlier units: `ccm-dh-test/dh.py` (15 files), `ccm-dh-test/weilform.py` (4), `ccm-dh-test/finisher_weilext.py` (1), `d1-m1/ball.py` (2). No reader file imports another folder's module (method: Python `ast` imports matched against all 799 module names; `sys.path` lines read).
- *Run as a subprocess*: 2 files (`zoo-s36`, `zoo-s37` `verify/numbers_check.py` run `zoo-s27/verify/lint_s27.py`).
- *Byte copies*: 11 cross-folder identical groups that are not packaging copies — 6 between research units (Table 2 rows 3–8), 2 inside `e5-kappa-s29` (writer → reader re-run), 3 infra (rows 10–12); plus 5 near-identical groups (N1–N5).
- *Declared adaptations*: `d1-m1` → `d1-m2a` producers (mp and Arb legs); `c2-m6` → `d4-sign-sweep` twisted sum and archimedean term; `thin.c` → `thin2.c` → `lg_core.h` (format); `lemmaB-s41/orch-verify/s8_meansq.py` → U3 `t1_check.py`.
- *Data reuse checked by hash*: `s5-multiplicity-s40/NOTE.md` l. 32 (the S5(4/5) dump).
- *Names another unit's code file anywhere in its text* (any purpose): 54 files.

**Reader duplicates, by design.** 371 READER files. Independence is written into the files, e.g. `conj-O-s38/verify-O/thin_O.py` l. 3 "Shares no code with verify/: own segmented prime sieve, own RNG". Exceptions found: `e5-kappa-s29/verify-O/rerun/` re-runs byte copies of the writer's pipeline (Table 2 row 9), declared in `e5-kappa-s29/read-O.md` l. 3: "The re-run of the writer's rung-0 scripts is in `verify-O/rerun/`", alongside the reader's own scripts; the Lean checkers copy the builder's runner with the tree path changed (Table 1, LEAN row).

**What could not be checked.** The order of creation inside copy groups (file times on this iCloud tree are not reliable; the direction of copying is taken from the copies' own headers where they state it). Whether code was run as written: nothing was executed. Reuse by copy-and-edit that changed more than comments is only detected where a header declares it, or by the line-similarity checks run on the generator, zero-finder, counter, arXiv, lint and zoo-insert families. The role of a file is read from its folder and docstring.

**Census note.** Excluding `sources/` as the brief directs removes 4 `.sh` files, all arXiv or fetch helpers (`lemmaB-s41/U1-lookahead/verify-O/sources/arxiv_q.sh`, `fejer-form-s39/sources/fetch_sources.sh`, `novel-wave-s37/beurling-fe/sources/arxiv-queries/q.sh`, `s.sh`); with them the `.sh` count is 130. They add to the arXiv-helper rewrites counted under LIT.
