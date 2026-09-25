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

