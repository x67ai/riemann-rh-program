# CHECK-O-B — D4 Job 2 parts B and C (Opus 5, the independent second model): my own Control-1 launches, and the post-sweep re-check of the note

**Opened Fri Sep 25 16:22 IST 2026 (machine clock). Contract: `CHECK-O-B-BRIEF.md` (read in full), `BRIEF.md` "Job 2" parts B and C. Every number below is printed by a script under `checker-O/`, and the script's log is named in place. I edited nothing of Job 1's: not the note, not a JSON, not `hashes.txt`, not the harness. I wrote only under `checker-O/`, this file, and dated rows appended to `SHARED.md`. Nothing was committed by hand (the watchdogs do that). Standing orders 5 and 7 bind.**

**Hashes checked FIRST, before anything ran (`shasum -a 256`, 16:22:30 IST):**
* my evaluator, source `checker-O/twsumO.go` = 90e144f502fbaf6d0214fe605d9923ee0f0111da27193b1d315f2be768ff1437, and binary `checker-O/twsumO` = d57080a8eeee7da8e59322df2446c976a3b8ee64a18cf6064975dced489d0f45. Both match part A, so there was **no rebuild** and stop line (3) does not arise. `replayOB.py` asserts the binary hash again before each batch.
* The inputs, as the brief names them: `d4-sweep-note.md` 80a14ea23bc732a48c2b8b163d3ab5d0d487b6668a853470b222909d01852086; `SHARED.md` dea0d1810d1978af5bfbcf5924609388e51278d73fcc608c463953ea9ece180c (before my rows); `hashes.txt` bbc1426041f5ff129dfb95b2257790531064a9330acce9293f54cececbd82a2f; `CHECK-O-A.md` 261e53fea34ab605d801d020c5525736364c61ae239dd3faca6c1ba580815d3e; `BRIEF.md` 8ca22341af0eaa9b1e4be2c5175037918fcb1881a5025cb01322baeaf77d096d.

**Inputs read at the page:**
* `CHECK-O-B-BRIEF.md` and `CHECK-O-A.md`, in full.
* `d4-sweep-note.md`: §0–§5, §7–§12 in full, and §6 by script (all 133 rows are parsed in C.1).
* `SHARED.md`: the checkpoints, the Control-1 rows and the close block.
* `harness/eps_phi.json`, `sweep_plan.json`, `d4_twisted_sum.rs` (lines 1–40, 140–150, 380–410, 470–500), `d4_point.py` (the hashing and binary-call lines), `d4_plan.py` (the ladder line), `d4_run_tier.py` (the replay block).
* The five sidecars; the zeta, control1 and replayO JSONs (by script).
* The prior-art texts and the Odlyzko 1992 pages, in C.3.
* The directions files at the lines named, in C.6.

## §A The part-A re-check: the two items that changed (note §9, F1 and F2)

Script `checker-O/partA_recheck.py`, log `checker-O/logs/partA_recheck_run.log`, output `checker-O/out/partA_recheck.json`.

### (b) ε governance — CLEAN
* **`harness/eps_phi.json`.**
  * It carries `eps_phi_per_t` = 1.0266395604864687e-30, bit-equal to the proven value. Its basis reads "PROVEN a-priori bound … BINDING for every phase line, refusal and Control-1 tolerance".
  * The sampled maxima are under `measured_sample_max`, labeled "sample maxima over the n sampled, NOT bounds": 6.392019332313393·10⁻³¹ (Job 1) and 6.686·10⁻³¹ (mine).
  * The retired constants are under `retired`: 2.2·10⁻³¹, 6.392·10⁻³¹ and 2.1·10⁻³⁰.
* **The source.** `d4_twisted_sum.rs` line 149 sets `EPS_PHI_PER_T` = 1.0266395604864687e-30, equal to the proven value. Line 384 has `Option<f64> = None` (no compiled default), and lines 404–406 refuse to run without the flag.
* **The binary without `--eps-phi`: exit code 2**, run twice (once with no arguments, once with `--t 1e6 --L 10 --out x.json`), in an empty temporary directory. No file was written. The message, verbatim: "--eps-phi is mandatory: pass the governing per-unit-t phase bound explicitly (the proven bound is EPS_PHI_PER_T = 1.0266395604864687e-30; harness/eps_phi.json; checker-O/job1_ddlog_bound.py)".
* **Hashes on disk.** Binary `harness/d4_twisted_sum` = 2be891b6088871cbbac4c3a5d31a2dd5af19d1e8ababea7c389ea00d7aad46bc; source = 7893f32e6f739df517a1d33289b9d0b4a1ebb6e07dc8abfd9e2d32ee45a3c480. Both appear in `hashes.txt`'s fix-pass block, "# --- fix pass (Fri Sep 25 03:43:55 IST 2026 …", which is also where the `.v2`, `d4_point.py`, `d4_plan.py`, `sweep_plan.json`, `eps_phi.json`, sidecar-script and `d4_run_tier.py` lines are. Section C.1(i) re-hashes all of them.
* **`sweep_plan.json` v2.** All 121 ladder entries carry `phase_line_L22` and `accepted`, and all are accepted. Both tier-1 controls carry them too (5.63·10⁻¹⁴ and 3.40·10⁻¹⁰, both accepted). The six tier-2 entries carry `phase_line_L28.35` and `accepted`, from 4.526·10⁻¹⁶ at the PT edge to 9.295·10⁻⁹ at k = 117, all accepted. `tier2_refused` holds 10²⁰ at 1.509·10⁻⁸, `accepted: false`.
* **My own lines** use ε_proven and my own ℓ¹. Each ℓ¹ below is a sum computed by `twsumO`, not an estimate:
  * k = 117, t = 61609351296641974272: line **9.2947·10⁻⁹, accepted**;
  * k = 118, t = 71145368965766258688: line **1.0733·10⁻⁸, REFUSED**;
  * t = 10²⁰: line **1.5087·10⁻⁸, REFUSED**;
  * the largest tier-1 line at L = 22 is 2.1241·10⁻⁹ (k = 120).
* **t_ceil re-derived.** I used t_ceil(L) = 10⁻⁸/(ε·ℓ¹(L)), with **ℓ¹(L) = Σ_{n ≤ ⌊e^L⌋} |w_n|, w_n = 2Λ(n)n^{−1/2}·L⁻³A(log n / L)**. Each sum is exact over my own odd-only sieve, with A(v) by tanh–sinh and quintic Hermite (CHECK-O-A §1). The sums were printed by `twsumO` in `checker-O/out/zetaO_t1e12_L20.json`, `replayOB_t3000175332800_L22.json` and `zetaO_t3000175332900_L28.35.json`:

  | L | ℓ¹ (mine) | note §3 | t_ceil (mine) | note §3 |
  |---|---|---|---|---|
  | 20 | 12.539725546518047 | 12.54 | 7.77·10²⁰ | 7.8·10²⁰ |
  | 22 | 21.807415922058 | 21.81 | **4.47·10²⁰** (4.4666·10²⁰) | 4.47·10²⁰ |
  | 28.35 | 146.95060754424256 | 146.95 | **6.63·10¹⁹** (6.6284·10¹⁹) | 6.63·10¹⁹ |

  At L = 22 the plan's `l1_used` is 21.8095, the PNT estimate, where the exact sum is 21.8074. The plan's t_ceil(22) is therefore 4.4662·10²⁰ against my 4.4666·10²⁰. Both print as 4.47·10²⁰, and every line differs by 10⁻⁴ relative. Harmless, and the note §3 already calls 21.81 "the PNT estimate".
* **Every landed JSON (133 = 128 tier 1/2 + the PT edge + 4 rehearsal).**
  * `eps_phi_per_t_used` equals the proven value, bit for bit, in all **128** JSONs written after the fix pass.
  * The PT edge and the four rehearsal JSONs ran with the measured 6.392·10⁻³¹. For them the proven line is in the sidecar.
  * `phase_line` = ε_used·t·`l1_norm` to a relative 10⁻¹² in **133/133**.
  * The proven line ε_proven·t·`l1_norm` is present (in the JSON or in its sidecar) and equal in **133/133**.
  * The binary's own printed line (in the sum JSON, to 6 digits) equals the JSON's line in 129/133. Across the sweep the sum JSONs print ε = 1.02664e-30.
  * The four exceptions are the four rehearsal sum JSONs. Their binary line is exactly 2.2/6.392 of the JSON's (for example 2.75874·10⁻¹⁸ against 8.0154·10⁻¹⁸ at (10¹², 20)). The first build ran them with the compiled 2.2·10⁻³¹ before `--eps-phi` existed, and `d4_point.py` recomputed the line with the measured ε afterward. This is the historical defect that F1 names ("applied silently when `--eps-phi` was omitted"), not a new one, and the sidecars supersede both numbers.
* **The five sidecars.** Each sidecar's `sidecar_of_sha256` matches the landed JSON on disk. Each one's `eps_phi_per_t_used_in_run` equals its JSON's value, and its `phase_line_eps_proven` equals my ε_proven·t·ℓ¹ to 4 digits. `refused_eps_proven` is false in all five. The budget changes by at most 1.9·10⁻⁴ relative (at the PT edge: 8.9203 → 8.9220·10⁻¹³), W equals its JSON's W, and the Control-1 tolerance is 10⁻¹⁰ + the proven line. That is what §9 F1 says: "phase line recomputed with ε_proven … no budget changes beyond the third digit; none refused".

### (f) `binary_sha256` — CLEAN
* **The 128 JSONs written after the fix pass all carry `binary_sha256` = 2be891b6…**, together with `binary_hashed_at` = "launch, before the sum: the binary that ran (fix (f))". `sum_reused` is false in all 128, so the hash taken at launch is the hash of the binary that produced the sum.
* **The 129th sweep point, the PT edge (3 000 175 332 900, 28.35), carries f6256ded…**, the second build. It ran before the fix pass on that build throughout, so the key is right, as its sidecar says ("one build ran this point end to end; the key names the binary that ran").
* **So "every one of the 129 = 2be891b6…" (the brief's wording) holds for 128 of them.** The 129th is correctly f6256ded…. That is a property of the record, not a defect.
* **The code.** `d4_point.py` line 49 reads `bin_sha_launch = sha(BIN); src_sha_launch = sha(…d4_twisted_sum.rs)`, before the sum call at line 77, which runs `[BIN, '--mode', 'zeta', …, '--eps-phi', repr(eps), …]`. Line 145 stores `binary_sha256=bin_sha_launch` and `binary_sha256_at_assembly=sha(BIN)`. Line 111 is the DH call, on the same `BIN` with `--eps-phi`.
* **The (10¹², 28.35) sidecar** states the distinction correctly:
  * `binary_sha256_in_json` is f6256ded…, "hashed by d4_point.py v1 at ASSEMBLY time … it did NOT run this sum";
  * `binary_that_ran` is f97fc582… (`.v1`);
  * the reader rule is "for this JSON read `binary_sha256_ran`".
  * The landed JSON does carry `binary_sha256_ran` = f97fc582a546… and `source_sha256_ran` = ceeb3a28….
* **The other three rehearsal JSONs** carry f97fc582… (the first build, which ran them). This is consistent with note §2.

**§A verdict: (b) CLEAN, (f) CLEAN.** The fix pass did what CHECK-O-A asked. One wording point, for C.8 and not blocking: the brief's "all 129 = 2be891b6…" should read "128 = 2be891b6…, and the PT edge = f6256ded… (the build that ran it)".

## §C.1 The §6 table against the JSONs and `hashes.txt` — CLEAN (one MINOR wording point on the ladder formula)

Script `checker-O/table_check.py`, log `checker-O/logs/table_check_run.log`, output `checker-O/out/table_check.json`. Ladder detail: `checker-O/logs/ladder_diff_run.log`.

**(i) `hashes.txt`.** The file has 701 hash lines over 694 distinct paths.
* **Every path's latest entry matches the file on disk: 694/694. 0 mismatches, 0 missing files.** Stop line (2) does not fire.
* Seven earlier lines are superseded by a later line for the same path, and in each case the later line matches: the second-build source and binary (lines 2–3, superseded at 39–40), `d4_point.py`, `d4_plan.py`, `sweep_plan.json` and `eps_phi.json` (lines 8, 9, 12, 13, superseded in the fix-pass block), and the (10¹², 28.35) JSON (line 26, superseded at line 29 after the annotation). This is the file's append-only convention, not a defect.
* One correction to the brief: **the note's own hash IS in `hashes.txt`**, in the close block, line 696: 80a14ea2…, which matches the note on disk.

**(ii) The §6 rows.** 133 rows were parsed, with 27 checks per row. Printed numbers were compared with the JSON value to within half a unit of the last printed digit plus 2 ulp of the double. The derived columns were recomputed by me: X = ⌊e^L⌋ (mpmath), W₁ = pole + ARCH − P₁, |W₁ − W₂| from the replay JSON itself, tol = 10⁻¹⁰ + ε_proven·t·ℓ¹, the budget total as the sum of its lines, δ_vis from the law 0.1·(22.4(log t/log 10⁶)^{1/3}/L)^{3/2}, and the band as δ_vis/1.5^{3/2} and δ_vis·1.5^{3/2}. Cross-file checks:
* Each control1 JSON's P/W equals the replay JSON it names.
* Each control1 JSON's `replay_json_sha256` and `job1_json_sha256` equal the files on disk, and its twsumO hash is d57080a8….
* The term counts are equal between the harness and the replay.
* Control 2 equals its `out/planted_*` file (pair value, expected value, pass flag, δ = δ_vis).
* The DH column equals its `out/dhreg_*` file (P_dd within 10⁻¹² of 0.339995468928925, W = ARCH_DH − P < 0).
* The two hash prefixes equal the SHA-256 of the zeta JSON and of the replay JSON.
* The verdict is "silent (W > 0)" exactly when W > 0.

**Result: 0 discrepancies in 133 × 27 checks.** No §6 W differs from its JSON, so stop line (4) does not fire.

**(iii) Counts.**
* **133 zeta JSONs = 4 rehearsal + 129 sweep.** Of the sweep, 123 are at L = 22 and 6 at L = 28.35. **128 are strictly above PT's height**, 1 is at it (k = 0) and none is below. Every JSON has a row.
* control1 JSONs 129, replayO JSONs 128 (the PT edge uses part A's own `zetaO` run), planted 136, dhreg 133.
* At all 129 points W > 0, the verdict is silent, `controls_pass` is true and `stop_line` is null.
* **The ladder.** The plan's heights are exactly `float(round(PT * 10**(k/16)))` **evaluated in double arithmetic** (`harness/d4_plan.py` line 64), for all 121. Recomputed exactly (60-digit decimal, round, then the nearest double), **99 of 121 agree. The other 22 differ by one unit below 2⁵³ or by less than one ulp of the double above it**, at k = 38, 44, 50, 54–59, 67, 72, 78, 88, 90, 97, 98, 102, 108, 109, 113, 119, 120. The largest relative difference is 1.4·10⁻¹⁵. The JSONs record the doubles actually used, and C.3 checks those heights against the windows, so no result moves.
* **MINOR (wording, §5 (a), §7, §12, §11 B2 row):** "t_k = round(3 000 175 332 800·10^{k/16}) as a double" → "t_k = float(round(3 000 175 332 800·10^{k/16})) evaluated in double arithmetic (`d4_plan.py` line 64), within one unit or one ulp of the exactly rounded value; the exact doubles are in `sweep_plan.json` and §6".

## §C.2 §3, the budget — FIX-FIRST (three numbers stated as bounds are exceeded by the record; no conclusion moves) + MINOR

Script `checker-O/budget_check.py`, log `checker-O/logs/budget_check_run.log`, output `checker-O/out/budget_check.json`.

**Every per-point budget line re-derived from its definition, at all 133 points: all agree.**
* phase = ε_used·t·ℓ¹;
* interpolation = 3·max|A_interp error|/A(0)·ℓ¹, from the sum JSON's `A_interp_check`;
* quadrature = 10(|conv_h| + |conv_H|), from the arch JSON;
* pole = 10^{log₁₀ Lemma-G bound};
* cos = 2.3·10⁻¹⁶·ℓ¹;
* total = the sum of these + 10⁻¹⁴.

**The per-tier maxima from the JSONs**, with the proven ε:
* **L = 22: budget ≤ 2.1242·10⁻⁹** (k = 120, 9.49·10¹⁹; phase line 2.1241·10⁻⁹), minimum 1.41·10⁻¹³;
* **L = 28.35: ≤ 9.2956·10⁻⁹** (k = 117; line 9.2947·10⁻⁹), minimum 8.92·10⁻¹³ at the PT edge.
* The brief's "≤ 9.3·10⁻⁹" is confirmed. **"≤ 2.1·10⁻⁹" (§12) and "≤ 2.12·10⁻⁹" (§3 table, phase row; also §9 F1 and §3 "largest line 2.12·10⁻⁹") are rounded down: the value is 2.124·10⁻⁹.** MINOR: write "≤ 2.13·10⁻⁹" wherever a bound is meant.

**Line by line** (the note §3 table against the record):
* **Sieve / Λ exactness, 0.** Integers. It is corroborated independently: the harness and twsumO use two different sieves (a segmented sieve, and my odd-only byte sieve with dynamic segments), and they give the same term count at all 129 points (C.1). CLEAN.
* **Summation (Neumaier). There is no row in §3.** I derived the Kahan–Babuška bound |E| ≤ 2u|P| + 4n·u²·ℓ¹, which includes the 8-thread merge. It gives **≤ 6.3·10⁻¹⁸ at L = 22 and ≤ 2.1·10⁻¹⁸ at L = 28.35**: negligible, and below the 10⁻¹⁴ floor. MINOR: add the row, or say that the floor covers it.
* **The weight's own roundings: also no row.** The §3 "cos in double" row, 2.3·10⁻¹⁶·ℓ¹, covers the cosine only. `add_term` (`d4_twisted_sum.rs` line 295) forms w = λ/√n·2·a/L³ with about 3.5u of relative rounding (λ, √, ÷, ×a, L³, ÷), and the product w·cos adds 0.5u. So there is a worst-case **4u·ℓ¹ line not in the budget: 9.7·10⁻¹⁵ at L = 22 and 6.5·10⁻¹⁴ at L = 28.35**.
  * With it, the minimum budgets rise by 6.9 % (L = 22) and 7.3 % (L = 28.35). The maxima are unchanged, since the phase line dominates there.
  * min |W|/budget is still 3.3·10⁷ at L = 22 and 3.7·10⁶ at L = 28.35.
  * The measured two-implementation agreement at low t (1.3·10⁻¹⁵ at the PT edge, 28.35) sits 50 times below this worst case, as a random walk would.
  * MINOR: add the row "weights and product (4u·ℓ¹): 9.7·10⁻¹⁵ | 6.5·10⁻¹⁴", and raise the budget minima to 1.5·10⁻¹³ and 9.6·10⁻¹³.
* **A(v) interpolation. FIX-FIRST (number):** the tier-2 cell reads 8.7·10⁻¹³; **the record is 8.479·10⁻¹³** (3 × 3.197·10⁻¹⁴/16.622 × 146.95; the note's own formula with 3.2/16.6 also gives 8.50·10⁻¹³). Fix: "8.7·10⁻¹³" → "8.5·10⁻¹³". The tier-1 value 1.3·10⁻¹³ is right (1.258·10⁻¹³).
* **Archimedean quadrature. FIX-FIRST (number):** the tier-1 cell reads "≤ 10⁻¹⁶"; **the record's maximum at L = 22 is 5.55·10⁻¹⁶** (10 × |conv_H| = 10 × 5.55·10⁻¹⁷). Fix: tier-1 cell "≤ 10⁻¹⁶" → "≤ 5.6·10⁻¹⁶". The tier-2 cell is right (≤ 6.9·10⁻¹⁷).
* **Bracket two-path check. FIX-FIRST (number):** the note says "≤ 2.6·10⁻²⁰ (r = 85.7 … 10²⁰)". **The record's worst over the 133 points is 2.731·10⁻²⁰, at t = 533 515 002 082 491 (k = 36, L = 22)**. The tier-2 worst is 2.616·10⁻²⁰, over 13 nodes per point. Stop line (6)'s threshold 10⁻¹² is not approached. Fix in three places:
  * §3 table: "≤ 2.6·10⁻²⁰" → "≤ 2.8·10⁻²⁰ (worst 2.73·10⁻²⁰ at t = 533 515 002 082 491, L = 22)";
  * §10, stop line (6): "≤ 2.6·10⁻²⁰" → "≤ 2.8·10⁻²⁰";
  * §12, stop line (6): "two-path bracket ≤ 2.6·10⁻²⁰" → "≤ 2.8·10⁻²⁰". §4.3's "≤ 2.6·10⁻²⁰" is a PT-edge statement and is right there.
* **Pole terms.** Both cells are true but point at rehearsal points. "≤ 10^{−555 280} at 10¹²" is the (10¹², 20) rehearsal, and "≤ 10^{−661 116}" is (10¹², 28.35). The sweep's own worst cases are **10^{−1 008 780}** (L = 22, k = 0) and **10^{−1 145 152}** (L = 28.35, the PT edge). MINOR: quote the sweep's values.
* **The phase line.** It equals ε_proven·t·ℓ¹ at every point (§A). CLEAN.

**§3 verdict: FIX-FIRST** (the three number fixes above; each changes a stated bound, not a result), plus the MINOR rows. The ceiling paragraph and the priced-not-built paragraph are CLEAN (re-derived in §A).

## §C.3 §5, the coverage map — CLEAN for the gate (no height in any window; both controls inside); FIX-FIRST (one number) + MINOR

Script `checker-O/coverage_check_B.py` (part A's `coverage_check.py`, extended to the landed heights and the measure), log `checker-O/logs/coverage_check_B_run.log`, output `checker-O/out/coverage_check_B.json`. The plan's measure as a plain sum: `checker-O/logs/plan_measure_sum_run.log`.

**The sources, re-read at the page this session** (page images rendered with `pdftoppm` from the PDFs in `prior-art/`):
* **Odlyzko 1992, PDF p. 140 (Table 1.1 and Table 1.2).** Eight sets. N: count, first:
  * 10⁶: "1, 000, 1052", N + 1;
  * 10¹²: 1,592,196, N − 6,032;
  * 10¹⁴: 1,685,452, N − 736;
  * 10¹⁶: 16,480,973, N − 5,946;
  * 10¹⁸: 16,671,047, N − 8,839;
  * 10¹⁹: 16,749,725, N − 13,607;
  * 10²⁰: 175,587,726, N − 30,769,710;
  * 2·10²⁰: 101,305,325, N − 633,984.
  * The table also gives the approximate height of zero N. The 10¹²-th zero is at 2.677·10¹¹, below PT's height.
* **Odlyzko 1992, PDF p. 8 (= p. 5):** "The entry for N = 10²⁰, for example, means that 175,587,726 zeros were computed, starting with zero number 10²⁰ − 30,769,710, and ending with zero number 10²⁰ + 144,818,015". So last = first + count − 1. **My script derives the note's six end offsets from that rule and matches all six:** +1,684,715; +16,475,026; +16,662,207; +16,736,117; +144,818,015; +100,671,340.
* **Odlyzko 2001, PDF p. 3:** "1, 006, 374, 896 zeros of the zeta function starting with zero # 13, 048, 994, 265, 258, 476 (at height approximately 2.51327412288·10¹⁵)", at the page.
* **Gourdon 2004** `prior-art/…txt` lines 1846–1859: the offsets as the note quotes them (10¹⁴: 3 … 2·10⁹; 10¹⁵: 0 … 2·10⁹ − 1; 10¹⁶: 1 … 2·10⁹ − 1; 10¹⁷: 0 … 2·10⁹; 10¹⁸: 1 … 2·10⁹ − 1; 10¹⁹: 0 … 2·10⁹ + 1; 10²⁰: 4 … 2·10⁹ − 1).

**The fourteen windows: confirmed.** Seven Gourdon, six Odlyzko 1992 inside the range, one Odlyzko 2001. Their widths match the note's §5 list (4.35·10⁸ … 2.97·10⁸; 3.7·10⁵, 3.1·10⁶, 2.8·10⁶, 2.6·10⁶, 2.6·10⁷, 1.5·10⁷; 1.88·10⁸).

**No landed height in any window.** All 126 non-control points (the 121 ladder heights and the tier-2 heights 3 000 175 332 900, 10¹⁴, 10¹⁶, 10¹⁸ and 61609351296641974272) lie outside every window, even with each window padded by 1 000 mean spacings. The closest is ladder t = 22 498 141 090 488, **7.5·10¹⁰ mean spacings** from the edge of the Gourdon 10¹⁴ window. Stop line (5) does not fire. CLEAN.

**The controls, as the gate states them: both confirmed.**
* **15202440115920748544** is 8 592.2 mean spacings above the page value of zero #10²⁰. So it is zero #10²⁰ + 8 592, inside Odlyzko 1992's #10²⁰ − 30,769,710 … #10²⁰ + 144,818,015 and inside Gourdon's #10²⁰ + 4 … #10²⁰ + 2·10⁹ − 1.
* **2513274122900000** is 2.0000·10⁴ in t above the page's 12-digit start 2.51327412288·10¹⁵ (19 968.5 above my R-vM start, 1.07·10⁵ zeros), and 1.88·10⁸ in t below the window's end.

**FIX-FIRST (one number): the covered measure.**
* **The note says "Total measure 2.75·10⁹ in t". That is the plain sum of the fourteen window lengths:** `sweep_plan.json`'s `covered_measure_in_t` = 2 748 240 445.46 equals Σ(t_hi − t_lo) exactly. But five Odlyzko 1992 sets (N = 10¹⁴, 10¹⁶, 10¹⁸, 10¹⁹, 10²⁰) overlap the Gourdon windows, so the sum counts them twice.
* **The covered measure (the union) is 2.718·10⁹, from my windows and from Job 1's plan windows alike (2.71788·10⁹ against 2.71789·10⁹).** The fraction is 2.718·10⁻¹¹, so "2.7·10⁻¹¹" stands.
* **Fix**, in §5 (map bullet 2) and §9 F3:
  * "Total measure 2.75·10⁹ in t" → "Total measure (union) 2.72·10⁹ in t (the plain sum 2.75·10⁹ counts the five Odlyzko 1992 sets that overlap Gourdon's windows twice)";
  * `sweep_plan.json` `covered_measure_in_t` should be the union in a v3, or the key renamed `sum_of_window_lengths` (the orchestrator's call; the plan is Job 1's file).
* Correcting my part A: CHECK-O-A's "the covered measure changes by less than 10⁻³ of itself" was about adding the four windows; I did not compute the union then.

**MINOR: the precision of the plan's window edges.**
* §5 says the R-vM heights carry an "error a few units of t", and the plan pads each window by ±100.
* But the plan stores `t_lo`/`t_hi` as doubles. Above 10¹⁸ their ulp is 256–4 096. Against my 40-digit inversion the plan's edges differ by up to 773 (Gourdon 10²⁰ `t_lo`), 3 029 (its `t_hi`) and 3 874 / 5 849 (the 2·10²⁰ set). At several edges the plan's window is narrower than the unpadded window.
* No conclusion moves: the nearest non-control height is 7.5·10¹⁰ spacings away, and the control is 1 275 in t above zero #10²⁰, which is 2.2·10⁷ inside the window.
* MINOR wording in §5: "error a few units of t" → "error a few units of t below 10¹⁸; above it the double storage of the edges (ulp up to 4 096) dominates, irrelevant at the sweep's margins (≥ 7.5·10¹⁰ spacings)".

## §C.4 The numbers of §7 and §12 — FIX-FIRST (one visibility sentence claims more reach than the record) + MINOR

Script `checker-O/numbers_check.py`, log `checker-O/logs/numbers_check_run.log`. Max |ΔW| also comes from `checker-O/logs/table_check_run.log`, and the timeline from `harness/d4_run_tier{1,2}_run.log`, `harness/run_pt_edge_after_run.log`, my own part-A JSONs and SHARED.md.

**Confirmed from the JSONs:**
* **min W:** +0.0252902930 at t = 40007981065365 (k = 18, L = 22) and +0.0184337908 at t = 10¹⁶ (L = 28.35). max W at L = 22: +0.0895704 at 19482587526283665408.
* **δ_vis:** 0.1482 (PT's height) … 0.1875 (9.49·10¹⁹) at L = 22, and 0.1013 (the PT edge) … 0.1276 (k = 117) at L = 28.35. So **[0.1013, 0.1875]**. The band factor is 1.5^{3/2} = 1.8371, and the band's extremes are [0.0551, 0.3444]. The note's "[0.055, 0.344]" is right.
* **max |ΔW| = 6.804·10⁻¹⁴ at t = 53351500208249126912 (ladder k = 116, L = 22)**, with |ΔP| = 6.813·10⁻¹⁴ there. The tier-2 maximum is 5.392·10⁻¹⁴ at k = 117. At t ≤ 10¹⁶ the maximum is 3.5·10⁻¹⁶ (L = 22) and 1.26·10⁻¹⁵ (L = 28.35), so the note's "≤ 10⁻¹⁵ up to 10¹⁶" is right for tier 1.
* **Control 2, rel. diff ≤ 6.6·10⁻¹⁶ (§7, §12) against ≤ 4.3·10⁻¹⁶ (SHARED close block): both are right, over different sets.**
  * Over all 129 points the maximum is **6.583·10⁻¹⁶, at t = 19482587526283665408 (L = 22)**.
  * Over the six tier-2 points it is **4.325·10⁻¹⁶, at 10¹⁸ (L = 28.35)**.
  * The SHARED sentence sits inside the tier-2 bullet ("Tier 2 runner … Control 2 rel. ≤ 4.3·10⁻¹⁶"), so it is a tier-2 statement. §12's whole-sweep "≤ 6.6·10⁻¹⁶" is the one a reader of the close needs, and it is right.
* **min |W|/budget:** 3.34·10⁷ (L = 22) and 3.68·10⁶ (L = 28.35).
* **Tier-2 walls:**
  * the sums: 63.1, 68.2, 68.9, 68.7 and 70.3 min, plus the PT edge at 88.3 min;
  * the replays: 1 040–1 260 s (17–21 min);
  * the tier windows: 03:43:53 → 05:39:10 (115 min) for tier 1 and 05:40:07 → 13:00:16 for tier 2.
  * All as stated in §7 and §12. Stop line (7) (2 h) does not fire.

**"88 min once".** §12's "88 min once when two 8-thread jobs overlapped in the rehearsal" is right. §4.3's cause is incomplete. Job 1's PT-edge sum ran 02:04:05 → 03:32:34 (`run_pt_edge_after_run.log`). My part-A replays overlapped it **twice, back to back**: (10¹², 28.35) from 02:18:34 for 1 804 s, and the PT edge from 02:49:03 for 1 796 s (the `date` and `wall_s` fields of `checker-O/out/zetaO_t1e12_L28.35.json` and `zetaO_t3000175332900_L28.35.json`). So 61 of its 88 min shared the machine with a second 8-thread job, not only 02:18–02:48. MINOR (§4.3): "(02:18–02:48 IST)" → "(02:18–02:48 IST, then Job 2's PT-edge replay 02:49–03:19 IST)".

**FIX-FIRST: the δ = 0.1 visibility sentence (§7 "the silence intervals, both tiers", and §12 S2).** The note says "δ = 0.1 is visible at L = 28.35 only up to ≈ 3·10¹² (δ_vis = 0.1013 at the PT edge …)". But visibility needs δ ≥ δ_vis, and at the PT edge δ_vis = 0.1013 > 0.1. Solving the law exactly, **δ_vis(t, 28.35) = 0.1 at t = 1.46·10¹², below PT's height**. So **δ = 0.1 is visible at no sweep point.** No sweep point has δ_vis ≤ 0.1 (script: the list is empty). It was visible at the (10¹², 28.35) rehearsal point, where δ_vis = 0.0993. The sentence claims reach the record does not have. Fix:
* §7: "δ = 0.1 is visible at L = 28.35 only up to ≈ 3·10¹² (δ_vis = 0.1013 at the PT edge and rises to 0.1276 at the ceiling) and at no point of tier 1" → "δ = 0.1 is visible at no sweep point: δ_vis(t, 28.35) = 0.1 at t ≈ 1.5·10¹², below PT's height (δ_vis = 0.1013 at the PT edge, rising to 0.1276 at the ceiling; 0.0993 at the (10¹², 28.35) rehearsal point, inside PT's range)";
* §12 S2: "δ = 0.1 visible only at L = 28.35 up to ≈ 3·10¹²" → "δ = 0.1 visible at no sweep point (at L = 28.35 only below t ≈ 1.5·10¹², inside PT's range)".

**MINOR: δ = ¼ "visible at every point of both tiers" (§7, §12 S2).**
* This holds at the law's central value: the largest δ_vis is 0.1875.
* With the factor-1.5 band that the note itself carries, ¼ lies below the band's upper edge at every tier-2 point (upper edge ≤ 0.234). At no tier-1 point does it: the upper edge is 0.272–0.344, and at L = 22 it crosses ¼ at t ≈ 3.4·10¹⁰.
* Add: "(at the law's central value; within the factor-1.5 band at L = 28.35 only)". IV.9 asks that the visibility threshold be computed and the silence labeled below it, so the band belongs in the sentence.

**The stop-line record (1)–(8) of §12 against SHARED.md's timeline: consistent.**
* SHARED has no Job-1 STOP row.
* (4) fired at checkpoint 2 (01:08:43) and was superseded in the fix pass.
* (8): part A's FIX-FIRST at 03:35:04; the fix-pass block at 03:44:33.
* (7): the maximum is 88.3 min.
* (6): see C.2 for the bound's number (2.8·10⁻²⁰, not 2.6·10⁻²⁰).

**One sequencing wording, MINOR (§9 last line, the header).** "The sweep at scale was started after this ledger was on disk (SHARED fix-pass block, 03:44:33 IST; tier 1 launched 03:43:53 IST)" gives two times, and the second is 40 s before the first. The hashes.txt fix-pass block is stamped 03:43:55, two seconds after the launch.
* In substance the fixes preceded the launch. `d4_twisted_sum`, `eps_phi.json` and `sweep_plan.json` all carry an mtime of 03:42. The runner's first line prints ε_proven. All 128 sweep JSONs carry 2be891b6… and ε_proven (§A).
* Reword: "started once the fixes were built (binary, `eps_phi.json`, plan: 03:42 IST); the ledger rows were written in the same minute (hashes 03:43:55, SHARED 03:44:33; tier 1 launched 03:43:53)".

## §C.5 The "claims nothing / cannot / not evidence" sentences (§0, §1, §7, §8, §10, §12), S1–S5, and the zoo protocol — FIX-FIRST (one unlabeled inference) + MINOR

The reference, read at `BARRIER-ZOO.md` line 431, is IV.9's STATEMENT: "every mechanism has a computable threshold … below which a single off-line zero … is INVISIBLE, and every dead brief's evidence lived below its threshold". Its test: "a computed visibility threshold … and demonstrate its experiments … operate above it". IV.9 thus forbids calling below-threshold silence evidence. It does not say that above-threshold silence is nothing. It says that such silence has a stated reach. I also read IV.19 (lines 539–554) and V.2/V.4 (lines 556, 574). The sentences were found by grep (the list is in this section), and each was read in context.

**FIX-FIRST: δ_vis is an extrapolation, and the record does not label it.**
* Every silence sentence in the note leans on "shallower than δ_vis" (§1 line 20, §7 twice, §12). So do S2 and the B2 row ("visible depth δ_vis 0.148–0.188").
* δ_vis comes from the campaign's law L_sign ∝ δ^{−2/3}(log t)^{1/3}, which the IV.9 rider of 2026-09-24 states **"across 10³ ≤ t ≤ 10⁶"**, and BRIEF.md line 29 anchors it at 10⁶.
* The sweep applies it at 3·10¹² … 9.5·10¹⁹, **6.5 to 14 decades beyond the measured range**. The factor-1.5 band is the law's in-range tolerance, not a bound out of range.
* The note never says this: "extrapol" has 0 occurrences, and §10 lists "Inferred: none load-bearing".
* **Fix:**
  * add to §7 (both the tier-1 and the both-tiers paragraph) and to §12 S2: "δ_vis is the campaign's law (measured over 10³ ≤ t ≤ 10⁶, IV.9 rider 2026-09-24) extrapolated to 3·10¹²–9.5·10¹⁹ `[inferred: extrapolation, 6.5–14 decades; the factor-1.5 band is the in-range tolerance]`";
  * §10: "Inferred: δ_vis(t, L) above t = 10⁶ (the law's extrapolation; §7) — load-bearing for S2 and for the 'shallower than δ_vis' reach of the silence sentences";
  * the B2 row: see C.6.
* No sentence claims evidence from δ_vis. The label is what the record lacks.

**Sentence by sentence:**
* **§0.3 "What this claims. Nothing about RH. It is the sign channel's search range … a signal to certify … not a proof; there was none."** Exactly as strong as the record. CLEAN, given the δ_vis label.
* **§0.4 "What it does not claim …".** Its first four items are exact.
  * **"The silence is not evidence (zoo IV.9)" is weaker than the record, and loose.** IV.9 makes below-threshold silence not evidence. Above δ_vis (as extrapolated), the silence is precisely the search-range datum that §0.3 records.
  * MINOR: "The silence is not evidence" → "The silence is not evidence for RH (zoo IV.9); it is a floating-point record of no sign flip at 129 heights, for orbits of depth ≥ δ_vis within the kernel's reach of each height".
* **§0.2 "none containing a sweep height".** The two controls are sweep points inside windows by design. MINOR: → "none containing a non-control sweep height".
* **§1 "Silence at (t, L) certifies nothing (zoo IV.9; M6 §10 …) and says nothing about orbits shallower than δ_vis(t, L) … or about any other height."** "Certifies nothing" is exact: floating point is not interval arithmetic, and §8 is not run. CLEAN.
* **§1 "Therefore W_ζ(f_{t,L}) < 0 at any single (t, L) proves that ζ has a zero off the line"** is the exact-arithmetic statement, and the next paragraph (the caveat) confines it. CLEAN.
* **§7 tier 1 and the both-tiers close: "silence below the theorem's L* (≈ 1267, C2 line 103) and shallower than δ_vis is not evidence".**
  * C2 line 103 was read at the page: 1267 is L*(0.1, 10⁶) for ζ's C₁. At the sweep's heights L* is larger through log log t.
  * MINOR: "(≈ 1267, C2 line 103)" → "(≈ 1267 at (δ, t) = (0.1, 10⁶), C2 line 103; larger at the sweep's heights)".
* **§7 "a zero-side orbit of depth ≥ δ_vis would be seen by the datum at ITS height only within the kernel's reach |γ − t| ≲ a few units of 1/L·log".**
  * The reach is not computed anywhere on the record, and "1/L·log" is garbled.
  * From §1's own h_f(γ) = (γ − t)B̂(L(γ − t)), the scale is 1/L in γ − t: 0.045 at L = 22 and 0.035 at L = 28.35.
  * MINOR: → "within |γ − t| of a few times 1/L (1/L = 0.045 at L = 22) `[inferred: the reach is not measured here]`".
* **§7 "nothing at all about the heights the phase ceiling excludes (above 6.63·10¹⁹ at L = 28.35)".** CLEAN.
* **§8 "Nothing in this unit spends a token on either leg"; "never 'RH disproved'".** CLEAN.
* **§10.**
  * "Inferred: none load-bearing after the fix pass" is **wrong by the δ_vis extrapolation** (the FIX-FIRST above).
  * "Not run: … Job 2's own part-B launches" is now superseded by this file: 20 own launches (14 at L = 22, 6 at L = 28.35), all PASS; §B has the table. MINOR: update that line.
  * The stop-line (6) number: see C.2.
* **§12, the silence close.** "a datum that claims NOTHING about RH … and nothing about orbits shallower than δ_vis at those heights or about any other height" and "a positive one is not evidence for RH either" are exact. The second is the precise form §0.4 should copy. With the δ_vis label, CLEAN.
* **§12 S1–S5.**
  * S1 ("unchanged — it remains one"): CLEAN.
  * **S2: FIX-FIRST twice.** The δ = 0.1 clause is wrong (C.4), and δ_vis needs its extrapolation label (above). The δ = ¼ clause needs its band caveat (C.4, MINOR).
  * "S3–S5: none": CLEAN.

**The zoo protocol, as run in §12 — in order (I.1, IV.9, IV.19, V.2, V.4), nothing missing, one entry misapplied in strength:**
* **I.1:** applied correctly for a refutation channel. The RH-false world satisfies the inputs and the channel fires, on both implementations (my part-A DH runs reproduce −0.2698 and −0.7482). "The silence on ζ is then a statement about ζ's inputs only": CLEAN.
* **IV.9:** "the threshold is computed per point (δ_vis, §6)" should read "computed per point from the campaign's law, extrapolated beyond its measured range (§7)". This is the same FIX-FIRST label.
* **IV.19:** "does not bind — this is the evaluation route" matches IV.19's own STATUS line ("Does NOT bind: the evaluation route (class A/B by the cost line)"). CLEAN.
* **V.2:** CLEAN. The windows, their measure (see C.3's FIX) and the controls are as C.3 states.
* **V.4:** CLEAN.
  * It fired on a case known to fail (DH, coefficient side, visible regime) and stayed silent on cases known to hold (the rehearsal points inside Platt–Trudgian's range; k = 0 at the height itself).
  * The zero-side limitation is stated in §4.5.
* **I.8 (the Siegel-zero world),** which the brief's list omits: I checked whether it applies. It binds positive-Λ first-order instruments against a real zero of ζ_K at t = 0. The sweep reads ζ at t ≥ 3·10¹² and consumes no positivity of Λ in its verdict (the sign of W is read, not a cone certificate), so it does not bind. No action.

## §C.6 §11, the three Instruments rows — FIX-FIRST (a wrong file reference; two labels) + MINOR; corrected rows given

**The tables, read at the page:**
* **B2**: `directions/B2-refutation-program.md`. The Instruments heading is at line 99 and the columns at line 101 (Quantity | Current best value | Result file | Dated). The sign-channel row is line 110, "The first-order SIGN channel as an unconditional refutation channel (shared with C2 M6): prime-side cost on this machine". The table has no "↳" rows yet.
* **The "↳" convention** as C2 uses it (lines 102, 106, 111, 113, 115, 117): `| ↳ [CORRECTION <date>, Session <n> — record moved] … |`, a bracketed tag, then the text.
* **D1**: `directions/D1-certified-refutation-arm.md`. Instruments at line 163, the same four columns. The note's pointers are right: line 174 is "Cost of new M3 rows" (one-legged above 10⁵), and in Untried, line 185 is the Riemann–Siegel-class evaluator and line 186 is M2b.
* **C2**: `directions/C2-rigidity-conservation.md`. Instruments at line 93. Line 103 is ζ's C₁ with L*(0.1, 10⁶) ≈ 1267. **The prime-side sign-channel cost row is now line 118, not "near 104"** (the table has grown). Its units are ns/term, class boundaries in L and min.

**Every number in the three rows traced** (to §A, C.1–C.4 and `checker-O/logs/selftest_max_run.log`):
* the ranges and point counts; the minima +0.02529 and +0.01843; the agreement ≤ 6.8·10⁻¹⁴;
* δ_vis 0.148–0.188 and 0.101–0.128 (0.1482–0.1875 and 0.1013–0.1276, rounded);
* ε = 1.0266·10⁻³⁰ and its three pieces; t_ceil 7.8·10²⁰, 4.47·10²⁰ and 6.63·10¹⁹ with ℓ¹ 12.54, 21.81 and 146.95;
* 63–70 min and 50–56 ns/term; 7.5·10¹⁰ terms independent of t;
* the sampled maxima "5.2–6.7·10⁻³¹": 5.2445·10⁻³¹ (L = 22), 5.5485·10⁻³¹ (L = 28.35), 6.392·10⁻³¹ (L = 20), and my 6.686·10⁻³¹. The L = 10 samples are 3.39·10⁻³¹, so the range holds for L ≥ 20.

All trace. The defects are the following:

1. **FIX-FIRST: the B2 row's file column cites `check-O.md`.** No such file exists in `results/d4-sign-sweep/`. Part A is `CHECK-O-A.md` (the gate; the proven ε), and parts B and C are `CHECK-O-B.md` (this file: the own-launch replays and the post-sweep check). The row should cite both.
2. **FIX-FIRST: the δ_vis cells (B2) need the extrapolation label** (C.5).
3. **FIX-FIRST: the C2 row's "a 320-bit per-height phase (Go, checker-O) has line ≈ 5·10⁻¹⁴ at 10²⁰"** states a sample maximum as a line. The figure is 3.48·10⁻¹⁶ rad, the maximum over 5 000 sampled n (CHECK-O-A §1), times ℓ¹ — the very sample-for-bound substitution that part A (b) ruled out for Job 1. **My own CHECK-O-A §2(b) made the same slip** ("its phase line at 10²⁰ is ≈ 5·10⁻¹⁴"), and I correct it here. It needs the label "measured (sample max over 5 000 n); no proven bound derived for checker-O".
4. **MINOR:**
   * the B2 row lacks the "↳" bracket tag;
   * the file paths in the B2 and C2 rows are relative (`out/…`, `checker-O/…`), where the tables use repository paths (`results/…`);
   * the ladder formula wording (C.1);
   * the D1 row's quantity "(the certified-refutation arm's only mechanism-seeking search to date)" is a characterization that cannot be checked at the page, and the tables record rather than characterize, so drop it;
   * the D1 row should credit the proven ε to `CHECK-O-A.md` §2(b);
   * "sampled maxima 5.2–6.7·10⁻³¹" should say "(L ≥ 20)".

**Corrected rows (exact text for the orchestrator; values unchanged except where marked):**

B2 (successor line under line 110):

| ↳ [EXTENSION 2026-09-25, Session 26 — D4] The sign channel SWEPT above the verified height: the (D-c) search range | t ∈ [3 000 175 332 800, 9.49·10¹⁹] at L = 22 (123 points: the 121-height ladder t_k = float(round(PT·10^{k/16})), k = 0…120, + 2 covered-range controls) and t ∈ [3 000 175 332 900, 6.16·10¹⁹] at L = 28.35 (6 points: 3 000 175 332 900, 10¹⁴, 10¹⁶, 10¹⁸, 15202440115920748544, 61609351296641974272); W_ζ(f_{t,L}) > 0 at every point (min +0.02529 at L = 22, +0.01843 at L = 28.35); two implementations (Rust dd-phase harness, Go 320-bit-phase evaluator) agree to ≤ 6.8·10⁻¹⁴, confirmed by Job 2's own launches at 20 points (14 at L = 22, all 6 at L = 28.35); both IV.19 controls PASS at every point; visible depth δ_vis 0.148–0.188 (L = 22), 0.101–0.128 (L = 28.35) `[inferred: the campaign's law measured over 10³ ≤ t ≤ 10⁶, extrapolated]`; NO candidate; floating point, not interval arithmetic — an instrument datum that claims nothing about RH, not zoo material | `results/d4-sign-sweep/d4-sweep-note.md` §6, §7, §12; `results/d4-sign-sweep/out/zeta_t*_L*.json`, `out/control1_*.json`; `results/d4-sign-sweep/CHECK-O-A.md` (gate); `results/d4-sign-sweep/CHECK-O-B.md` (own-launch replays, post-sweep check) | 2026-09-25 |

D1 (new row):

| Sign-channel sweep: the (D-c) search range and its ceiling | swept [3 000 175 332 800, 9.49·10¹⁹] at L = 22 (123 pts) and [3 000 175 332 900, 6.16·10¹⁹] at L = 28.35 (6 pts): all positive, no candidate; ceiling of the dd-phase pipeline t_ceil(L) = 10⁻⁸/(ε·ℓ¹(L)) with ε = 1.027·10⁻³⁰ (proven bound on the dd log): 6.63·10¹⁹ at L = 28.35, 4.47·10²⁰ at L = 22; certification of a firing PRICED, not run: Leg A ≈ 1 slot (interval re-evaluation, two producers, L ≲ 26), Leg B one-legged above 10⁵ and weeks-class (D1 lines 174, 185), Λ-form unowned (M2b, line 186) | `results/d4-sign-sweep/d4-sweep-note.md` §3, §7, §8, §12; `results/d4-sign-sweep/CHECK-O-A.md` §2(b) (the proven ε) | 2026-09-25 |

C2 (new row under line 118):

| Prime-side sign channel: the phase ceiling of the double-double pipeline (per-term phase error ε·t, ε the PROVEN bound on `dd_log_u64`; allowance 10⁻⁸ on ε·t·ℓ¹) | ε = 1.0266·10⁻³⁰ per unit t (bit-exact emulation: S₁ 4.250·10⁻³¹ + dd add 5.916·10⁻³¹ + series 10⁻³²; sampled maxima 5.2–6.7·10⁻³¹ at L ≥ 20); t_ceil = 7.8·10²⁰ (L = 20, ℓ¹ 12.54), 4.47·10²⁰ (L = 22, ℓ¹ 21.81), 6.63·10¹⁹ (L = 28.35, ℓ¹ 146.95); measured cost at L = 28.35: 63–70 min per point on 8 threads (50–56 ns/term wall), the term count 7.5·10¹⁰ independent of t; a 320-bit per-height phase (Go, checker-O) has a MEASURED error of 3.5·10⁻¹⁶ rad at 10²⁰ (sample max over 5 000 n; no proven bound derived), i.e. a measured line ≈ 5·10⁻¹⁴ | `results/d4-sign-sweep/d4-sweep-note.md` §3; `results/d4-sign-sweep/checker-O/out/job1_ddlog_bound.json`; `results/d4-sign-sweep/CHECK-O-A.md` §1, §2(b) | 2026-09-25 |

**Each row now fits its table.** The four columns are in the table's own units. B2 uses the successor convention with a bracket tag. C2's row sits under its cost row (line 118).

## §C.7 10(g) lint, U.S. English, standing order 7 — CLEAN (one MINOR label)

Script `checker-O/lint_check.py`, log `checker-O/logs/lint_check_run.log`.

* **10(g) lint** ("clearly / obviously / easy to see / well known / trivially"): **0 hits in the note, 0 in this file** at the time of the scan.
* **U.S. English in the note:** 0 candidates. The scan covered -ise/-yse forms (with a whitelist of true -ise words), -our forms (excluding four/hour/your/…), -re forms, and the usual British spellings (towards, programme, modelling, labelled, behaviour, colour, analyse, …).
* **Standing order 7.** The scan looked for novelty, priority and prior-art words in the note: novel, first to, not previously, priority, prior art, new mathematical, ….
  * **No novelty or priority claim exists.**
    * Line 276, the 10(n) line, says "Not a new mathematical object", a disclaimer.
    * Line 301 says "novelty claimed: none (the harness is a search, not a theorem; the proven ε bound is Job 2's, `CHECK-O-A.md` (b))".
  * **One class of prior-art claims exists: the negative-coverage statements of §5.** They are "Rigorous coverage above PT's height: none" and "(a) Ranges no published computation covers", repeated in §0.2 ("none rigorous"), §12 V.2 and the 10(n) line.
    * They are prior-art claims, but not novelty claims.
    * They were checked by two models at the sources the gate opened: Job 1 §5, CHECK-O-A (c), and C.3 above, with the page images re-read this session.
    * I ran one web search this session ("Riemann hypothesis verified beyond 3·10¹² height … rigorous verification"). It returned nothing rigorous above Platt–Trudgian. One blog-grade "2026 status report" says "twenty trillion zeros are confirmed", without a source. That reads as Gourdon's non-rigorous 10¹³ (below PT's height) or a garble, and it is not a published rigorous computation. Not load-bearing.
  * MINOR: label the §5 "(a)" sentence and "Rigorous coverage above PT's height: none" with `[prior-art gate: dual-checked at the sources (a)–(g) opened at the page — Job 1 §5, CHECK-O-A (c), CHECK-O-B C.3; not an exhaustive literature search]`.
  * **No `[novelty: single-check]` mark is needed anywhere.**

Sources of the web search: [Timothy Trudgian (Wikipedia)](https://en.wikipedia.org/wiki/Timothy_Trudgian); [The Riemann Hypothesis: A 2026 Status Report (mathlumen)](https://www.mathlumen.com/articles/riemann-hypothesis-2026-status-report).

