# zoo-s35 — the Opus 5 reader's read of the proposed Session-34 zoo additions (started Tue Sep 29 14:25:57 IST 2026; reader: Opus 5; contract `results/zoo-s35/BRIEF.md` "The reader (Opus 5)", SHA-256 `f08a250fa34e6645f90b7689e331253015309313a9dc5a4a61afa3aa2d941aa5`)

Read against: `results/zoo-s35/zoo-entries-proposed.md` `c10b00c81f33b906f30d539989079d712c722185d7b4d2612527b76988c78074` (75 lines, recomputed and matched), `scripts/zoo-insert-s35.py` (378 lines, read in full), `results/zoo-s35/dryrun-BARRIER-ZOO.md` `19488610…`, `numbers-check.log`, `SHARED.md`; format precedent `results/zoo-s33/zoo-entries-read-O.md`. Every line was checked at its RECORD (file and line named below), not against the writer's findings. `BARRIER-ZOO.md` read at `07a87152e58a04d07cb472e00871682580b516a05a93cd35accecb0b01fe064b`, 692 lines, 58 `### ` headings (I 8, II 5, III 21, IV 19, V 5). Nothing edited except this file; the proposed file, the script and the zoo untouched; nothing committed.

## Block 1 — the writer's dry run reproduced (Tue Sep 29 14:25:57 IST 2026)

`python3 scripts/zoo-insert-s35.py --dry-run /tmp/zoo-s35-reader-dryrun.md` (14:23:22 IST): rc 0; "+7 lines (692 -> 699); entries 58 (I 8, II 5, III 21, IV 19, V 5); Group IV 19 (no heading added); the six blocks at lines 35, 72, 145, 179, 400, 692". My output is **byte-identical** to the writer's `dryrun-BARRIER-ZOO.md` (both `19488610caa095788aaf26b708b37ec263cf4bb519a31999dfa8d57140de5871`); `diff` hunks 34a35,36 / 69a72 / 141a145 / 174a179 / 394a400 / 685a692; my own `grep -c '^### I\.[0-9]'` etc. on the result: 8/5/21/19/5 = 58; one trailing newline (`tail -c 2` = `2a 0a`). `BARRIER-ZOO.md` still `07a87152…` after the run. The script's arithmetic is right; the placement it encodes for `ii1`/`ii4` is adjudicated below (FIX-FIRST, P4–P5 and the script strings S1–S6).

## Block 2 — the three LINUX REPLAY lines at their records (Tue Sep 29 14:28:13 IST 2026)

Common clause of `i1`, `iv1`, `fq10`, each read at the line:
- "Ubuntu, kernel 7.0.0-34-generic, x86_64" — `00-main.log` line 2 "Linux jay-unix 7.0.0-34-generic #34-Ubuntu SMP PREEMPT_DYNAMIC … x86_64 GNU/Linux". ✓
- "12 cores, 37 GB" — `00-main.log` line 3 "host: jay-unix; cores: 12; mem: 37 GB; disk free: 400G". ✓
- "Lean 4.33.0-rc2 (d8b18978)" — `00-main.log` line 10 "Lean (version 4.33.0-rc2, x86_64-unknown-linux-gnu, commit d8b18978322de05a8f3dba51ef03cf5461676c17, Release)" (toolchain line 9 `leanprover/lean4:v4.33.0-rc2`). ✓
- "Mathlib 51e6992e" — `00-main.log` line 11 / `99-summary.txt` line 5 "cache: ok (mathlib 51e6992efd)". ✓
- "PASS, exit 0" — `99-summary.txt` lines 18–22, five times "PASS (exit 0; nanoda: 1; fake-landrun warnings: 0)". ✓
- "nanoda and the Lean kernel accept" — not in the five files the task names; it is at the comparator logs: every `11-comparator-config-*.log` prints "Nanoda kernel accepts the solution" and "Lean default kernel accepts the solution" (e.g. `…-pair-channel.log` 45, 47; `…-weil-containment-c2-one.log` 31, 33; `…-epstein-witness-six.log` 35, 37; `…-i1-witness.log` 56, 58; `…-weil-containment-c2.log` 30, 32), "Exit status: 0" at their last lines. ✓
- "sorryAx 0" — `99-summary.txt` lines 7–11 ("…; sorryAx: 0" each). ✓
- "name sets identical to the Mac's" — `HARVEST-NOTE.md` lines 9–13 (column "Name sets": IDENTICAL ×5) and line 15 ("five sets equal, every name on exactly [propext, Classical.choice, Quot.sound]"). ✓
- "a REAL Landlock sandbox (ABI v8, best-effort mode)" — `99-summary.txt` line 17 "REAL (--best-effort on Landlock ABI v8; write outside allowed paths denied)"; `09-landrun-test.log` line 1 "Got Landlock ABI v8, wanted {Landlock V9; …}" (the strict probe, which fails — `99-summary.txt` line 16 "landrun sandbox: FAIL"); `09b-landrun-best-effort-test.log` line 2 "… Permission denied"; `HARVEST-NOTE.md` line 18 ("Every comparator config therefore ran under a real Landlock sandbox at ABI v8, best-effort mode"). The line says REAL under best-effort, which is what the record says; it does not claim the strict probe passed. ✓
- "Label unchanged." — `HARVEST-NOTE.md` line 21 ("label text unchanged for each"). ✓
- Head "LINUX REPLAY 2026-09-29, Session 34 (`results/linux-check-s33/`; HARVEST-NOTE.md; …)" — `HARVEST-NOTE.md` line 1 ("14:06 IST 2026-09-29, Session 34"). ✓

**`iv1` — CLOSES.** "Both H5 topics (`WeilContainmentC2One`, `WeilContainmentC2`)" — HARVEST-NOTE lines 9–10 ("H5 rung 1, L = log 3"; "H5"). "1 + 1 names" — `99-summary.txt` lines 7–8; `04-print-axioms-WeilContainmentC2One.log` 1 line (`weilContainment_c2_interpolant_log3`), `04-print-axioms-WeilContainmentC2.log` 1 line (`weilContainment_c2_interpolant`), each on "[propext, Classical.choice, Quot.sound]" (= "propext/Classical.choice/Quot.sound", the form of the IV.1 precedent at zoo line 392). The script asserts the block equals staged line 6 plus the bracket phrase (my run: no exit). Placement after the Session-33 Suzuki RIDER at zoo line 394, before blank 395 and `### IV.2` 396 — the brief's "after the LAST line of that anchor's block, before the next heading" (the REFINEMENT anchor at 393 has one later dated line, 394). ✓

**`i1` — CLOSES.** "`EpsteinWitnessSix` (rung 1) and `I1Witness`" — HARVEST-NOTE lines 11–12 ("I.1 rung 1"; "I.1"). "3 + 14 names" — `99-summary.txt` lines 9–10; `04-print-axioms-EpsteinWitnessSix.log` 3 lines, `04-print-axioms-I1Witness.log` 14 lines (`grep -c .`), every line "[propext, Classical.choice, Quot.sound]" ("the three standard axioms"). Placement after the WITNESSES KERNEL-CHECKED bullet at 69 — the entry's last line (blank 70, `### I.2` 71); nothing dated follows the anchor. ✓

**`fq10` — CLOSES.** "8 names" — `99-summary.txt` line 11; `04-print-axioms-PairChannel.log` 8 lines. "`prop45`, `floor_holds_integer`, `floor_fails_anchor` among them" — that log's lines 5, 7, 8. "name set identical" — HARVEST-NOTE line 13. Four spaces then "- **[", as item 10's other sub-bullets (zoo 683–685) and item 11's (687–690). Placement after the PAIR CHANNEL sub-bullet at 685, before item 11 at 686. ✓

All three blocks equal their staged lines (`results/linux-check-s33/ZOO-LINES-STAGED.md` lines 6, 9, 12, hash `81bac262…` = brief) with only the bracket phrase added — the script's equality assertion passes in my run.

## Block 3 — the Lamzouri v2 rider (`ii1` = `ii4`) at its records; standing order 7 (Tue Sep 29 14:29:07 IST 2026)

Record: `results/watch-poll-s34/lamzouri-2609.02882v2.txt` (`de455968b82d0b60688767f9d3bfdb25e030dbe70244efaaefc80f62f8c91098`, recomputed), v1 extraction `lamzouri-2609.02882v1.txt` (`4d1c606d…`, recomputed), `V2-DELTA-s34.md` (`6d5fa6b1…` = brief), staged rider `results/watch-poll-s34/ZOO-LINES-STAGED.md` line 7 (`96fbf141…` = brief).

Clause by clause, at the line:
- Head "v2 of arXiv:2609.02882 (8 Sep 2026)" — v2 line 14 "arXiv:2609.02882v2 [math.NT] 8 Sep 2026". ✓
- "leaves Proposition 2.1's (2.4)–(2.5), C₀ = 0.67250… and C₁ = 0.83625… unchanged" — v2 (2.4) line 272 and (2.5) line 279 against v1 (2.4) line 220 and (2.5) line 226: the same displays (same hypotheses, v2 267–270 = v1 215–218); C₀/C₁: v2 lines 131–134 against v1 line 119 ("⩾ C0 = 0.67250 . . . and … ⩾ C1 := (C0+1)/2 = 0.83625 . . ."). ✓
- "adds (2.6) #{simple} + #{real} ≥ 3Σ1 − ΣK(z−s)²" — v2 line 284: Σ_{z∈Z, m_z=1} 1 + Σ_{z∈Z∩R} 1 ⩾ 3 Σ_{z∈Z} 1 − Σ_{z,s∈Z} K(z − s)². "#{real}" counts with multiplicity (v2 line 262, "sums over a multiset are understood to count elements with their multiplicities"); the rider's shorthand is faithful. ✓
- "the parametric (2.7)" — v2 lines 288–297: under Σ K(z−s)² ⩽ A Σ 1, 1 ⩽ A < 2, #{m_z = 1 or z ∈ R} ⩾ (5 + 2√2 − 2A)/(3 + 2√2) Σ 1. ✓
- "Theorem 1.1's two new unconditional estimates: N_{s∪0}/N ≥ C₂ = (1+2√2+2C₀)/(3+2√2) = 0.88762… (simple OR on the line) and (N_s + N_0)/2N ≥ C₁" — v2 lines 135–138 ("Moreover, … lim inf Ns∪0(T)/N(T) ⩾ C2 = 0.88762 . . . and lim inf (Ns(T) + N0(T))/(2N(T)) ⩾ C1 = 0.83625 . . ."), line 140 "C2 := (1+2√2+2C0)/(3+2√2)", line 142 "either simple or lie on the critical line (or both)"; "two new unconditional estimates" is the abstract's phrase (v2 line 15, "also yields two new unconditional estimates"). The rider drops "lim inf"; the phrase "Theorem 1.1's … estimates" carries it, and the staged text is the orchestrator's. Observation, no pair. ✓
- C₂ re-derived (Decimal, 40 digits) from C₀ = 0.672500703679 (zoo line 143, "2 − C_MT = 0.672500703679 (both models …)"): **C₂ = 0.8876200081732130853816088458206254303017**, printed "0.88762…" ✓; **1 − C₂ = 0.1123799918267869…** < 0.1124 ✓; C₁ = (C₀ + 1)/2 = 0.8362503518395 ✓; for Remark 1.2's comparison, (2 + C₀)/3 = 0.890833567893 (v2 line 164 "0.89083 . . .") ✓.
- "Remark 1.2: at most 1 − C₂ < 0.1124 of the zeros are both off the line and multiple" — v2 lines 147–149 ("the proportion of zeros that are simultaneously off the critical line and of multiplicity at least two is at most 1 − C2 < 0.1124"). ✓ "and if either proportion tends to C₀ the other tends to 1" — v2 lines 149–150 ("if either Ns(T)/N(T) or N0(T)/N(T) tends to the lower bound C0, then the other must tend to 1"). ✓
- The two quotations — v2 line 186 "both may be viewed as variants of a second-moment argument, and the optimization leads" ✓; line 187 "in both cases to the same Montgomery–Taylor extremal problem (see Remark 3.4 below)," ✓ — **with "below"** (Remark 3.4 itself is at v2 line 904, later in the paper). The block as proposed carries "(see Remark 3.4 below)": right.
- "Appendix A: a Comparator challenge file for the three main results at github.com/AxiomMath/ZetaZerosV2 (AxiomProver)" — v2 line 987 "Appendix A. Formal Certificate by AxiomProver", line 996 the URL, lines 997–998 "a formal challenge file containing the statements of the three main results, which can be mechanically verified using the Comparator tool in Lean". ✓ (The rider does not claim more: v2 lines 990–994 say Theorem 1.1's certificate is "under the assumptions of [3, Lemma 5] … and the standard Riemann–von Mangoldt asymptotic"; the rider says only "challenge file for the three main results", which is the author's wording.)
- Head "found by the Session 34 watch poll; … source `…/V2-DELTA-s34.md`" — V2-DELTA line 1. ✓

### Standing order 7 — (2.6) and (2.7) re-derived at the proof: **AGREE**

The question: do v2's (2.6)–(2.7) use only the diagonal coefficients α_j, Bessel's inequality and the split of Z into real/non-real × simple/multiple — the two-moment data class of (2.4)–(2.5)? I re-read the proof of Proposition 2.1 (v2 lines 313–666) and re-did the algebra of (2.29) by hand.

1. **The objects are v1's.** F(u,v) = Σ_z f_z(u) f_z(v) (v2 341); Σ K(z−s)² = ∬|F|² (v2 (2.12), lines 344–350 = v1 (2.10) line 267); the nested spaces U ⊂ V ⊂ W with real Gram–Schmidt basis ψ_j (v2 370–400 = v1 ~300–319); the diagonal coefficients α_j = ∬ F ψ_j ψ_j (v2 (2.17), lines 415–428 = v1 (2.15) line 345); Bessel ∬|F|² ≥ Σ α_j² (v2 (2.16), lines 408–412 = v1 (2.14) lines 327–331). The four range facts (2.18) Σ_U α_j ≥ Σ_{R2} m + 2Σ_S m (Parseval on U plus Bessel for h, lines 436–473), (2.19) Σ_{V∖U} α_j ≤ n (Bessel, 477–485), (2.20) α_j ≤ 0 on W∖V (490–491), (2.21) Σ_all α_j = Σ_Z 1 (the trace, 494–500) are shared by all four inequalities: line 429, "To prove the inequalities (2.4), (2.5), (2.6) and (2.7) we shall establish the corresponding lower bounds for the sum Σ α_j²".
2. **(2.6)** (lines 582–610). The only new step is the split S = S₁ ∪ S₂ of the distinct non-real elements into simple and multiple (lines 582–585, |S₁| = 2p, |S₂| = 2q) — with R = R₁ ∪ R₂ (lines 353–358) this is exactly the real/non-real × simple/multiple split. It enters once, through the integer atoms in (2.18): Σ_U α_j ≥ 2r + 2p + 4q (line 594, (2.28), using m ≥ 2 on R₂ and S₂). Then (2.29) (lines 599–607) combines a² + 4 ≥ 4a on U (the first inequality of (2.22)), a² + 1 ≥ 2a on V∖U ((2.23)), α_j² ≥ 3α_j on W∖V (from (2.20)); my own check: 4Σ_U − 4(r+p+q) ≥ 3Σ_U − 2r − 2p by (2.28); 2Σ_{V∖U} − n ≥ 3Σ_{V∖U} − 2n by (2.19); so Σ α_j² ≥ 3Σ α_j − (2n + 2r + 2p), and with (2.12), (2.16), (2.21) (line 610): 2n + 2r + 2p ≥ 3Σ1 − ΣK², while the left side of (2.6) is (n + 2p) + (n + Σ_{R₂} m) ≥ 2n + 2r + 2p (lines 585–589). Nothing else is consumed.
3. **(2.7)** (lines 611–666). Line 621: "In the second and third ranges we use the exact same ingredients as before, namely (2.20) and (2.23)"; the first range uses a² ≥ 2at − t² ((2.30), line 618); the hypothesis Σ K² ≤ A Σ 1 enters through the same (2.12), (2.16), (2.21) (line 632) — an upper bound on the SAME second moment ‖F‖²_HS, not a new invariant; (2.19) and (2.28) close it (line 644, (2.31)); t = 2 + √2 from t² − 4t + 2 = 0 (line 653) is an optimization of weights, not data.
4. **So the data read are {Σ m_z (trace), Σ K(z−s)² = ‖F‖²_HS, the multiplicity pattern (n, r, p, q)}** — the list II.4's note names ("No invariant outside {tr, ‖·‖²_F, n₊, integer atoms} is consumed", zoo line 174). The S₁/S₂ split is a finer reading of the integer atoms, not a new invariant, and it sits in the U-range bound (2.28) — which is what the rider's "the U-range split" names. The rider's "Same data class as v1 (Σ_j α_j, Bessel, integer atoms, the U-range split)" is correct.
5. **Cross-check against II.4's degeneracy (my own, not in the rider).** At the entry's two configurations — an on-line double at x against an off-line pair x ± iε — the left sides of the new inequalities are equal: (2.6)'s #{simple} + #{real} is 0 + 2 = 2 for the double and 2 + 0 = 2 for the pair, and (2.7)'s #{simple or real} is 2 and 2. The new targets are blind to the very swap II.4 records; the rider's "the degeneracy recorded here is untouched" holds, and more strongly than the rider says.

**Verdict: AGREE** with the rider's "Same data class as v1" sentence. Hence the label pair P1 below. (The note's own words "The targets differ from this entry's (the simple-AND-on-line count)" are right for both entries: II.1's DATED NOTE, zoo line 141, reads Prop. 2.1 as "#{simple real}", and II.4's lemmaR_tight is the N_{s∩0} certificate.)

### Pairs in `ii1` and `ii4`

The rider is one text placed twice and the script requires `ii1 == ii4` (script line 120), so each rider pair's OLD occurs **exactly twice** in the proposed file — once inside block `ii1`, once inside block `ii4` — and nowhere else (checked: `str.count` = 2 for both OLDs, 0 for both NEWs). Apply each to both blocks.

**P1 — standing order 7, the label (blocks `ii1` and `ii4`).**

OLD: found by the Session 34 watch poll; single-check — orchestrator's reading; source

NEW: found by the Session 34 watch poll; dual-checked (orchestrator Fable 5.1 + Opus 5 reader, Session 34); source

(The script already permits this substitution: `OLD_LABEL`/`NEW_LABEL`, lines 150–151, 158–160. No script change for P1.)

**P2 — FIX-FIRST: the rider says "the degeneracy recorded here" under II.1, which records a ceiling (blocks `ii1` and `ii4`).** II.1 is "The bandwidth-one certificate ceiling 0.6818287" (zoo line 133); its STATEMENT and STATUS (135, 139) record a ceiling and no degeneracy. Only II.4 is "the two-moment degeneracy" (zoo line 165). The record the rider cites keeps the two apart: V2-DELTA line 14 "the II.1 ceiling comparison (0.672500703679 vs 0.681837145932 for that r) is unchanged"; line 15 "II.4's degeneracy … is untouched". One text must serve both entries (the script's `ii1 == ii4` check), so it names both.

OLD: so the degeneracy recorded here is untouched.

NEW: so what this entry records (II.1's ceiling, II.4's degeneracy) is untouched.

(P2 departs from the staged line, which the brief allows — "carried VERBATIM except where the reader amends" — but the script's allowed set does not contain it: script string S1 is required, below.)

Verdict for `ii1` and `ii4`: **FIX-FIRST → CLOSES after P1, P2 and the placement pairs P4a–P5b with S2–S6.**

## Block 4 — the count paragraph; the writer's five flags; placement (Tue Sep 29 14:29:41 IST 2026)

### `count` — CLOSES after P3

Arithmetic: five one-line bullets + the paragraph + its blank line = +7, **692 → 699**, in my dry run as in the writer's. "The six lines entered at this stream" = five bullets + this paragraph, the house convention: zoo line 33 (Session 33) "The five lines" for four bullets + the paragraph, 686 → 692 (+6 with the blank); line 31 (Session 32) "The seven lines" for six + the paragraph, 678 → 686 (+8). Headings: 58, I 8 / II 5 / III 21 / IV 19 / V 5 by my own grep before and after; **Group IV unchanged at 19 — NO Group-IV entry**, as the paragraph says. "SHA-256 at launch 07a87152…" = the zoo I read. "the five topics shipped since the Session-30 replay … labels unchanged" = HARVEST-NOTE line 21. "v2 of arXiv:2609.02882 (8 Sep 2026)" = v2 line 14. One phrase follows the placement ruling below (the riders sit at the close of II.1 and II.4, below the notes and their later dated lines, not directly beneath the notes):

**P3 — block `count`.**

OLD: one beneath the II.1 DATED NOTE and one beneath the II.4 DATED NOTE

NEW: one at the close of II.1 and one at the close of II.4, each below that entry's Lamzouri DATED NOTE and its later dated lines

### The writer's five flags

1. **Remark 3.4 wording — CLOSES.** v2 line 187 reads "(see Remark 3.4 below)," — "below" is inside the parenthesis the rider quotes, and Remark 3.4 is at v2 line 904, after the comparison paragraph. The block already carries "below". No pair (the block is right as proposed).
2. **"entered at the Session-34 zoo stream" — CLOSES.** The brief requires it inside each bold bracket (BRIEF line 9); the precedents carry the stream in the same slot (zoo 392 and 684, "…; entered at the Session-32 zoo stream).]**"); this stream is "run at Session 34's close" (BRIEF line 1), so "Session-34" is right although the folder is `zoo-s35`. After insertion the phrase occurs exactly five times (the script's check, line 339; my dry run passes it). No pair.
3. **Top-level vs "indented one level" — CLOSES.** The brief's placement rule governs ("at the anchor's own indentation", BRIEF line 8); the staged files' leading spaces are the layout of their own numbered lists. The house precedent is the IV.1 LINUX REPLAY line, top-level (zoo 392), and item 10's four-space sub-bullets (683–685). `i1`, `iv1`, `ii1`, `ii4` top-level; `fq10` four spaces. No pair.
4. **Riders directly beneath the DATED NOTES vs after the entries' later blocks — FIX-FIRST: after the entries' last lines (II.1 after zoo line 147; II.4 after zoo line 178).** Three reasons, each at the record:
   (a) *The brief's rule.* BRIEF line 8: "Where the anchor already has dated lines after it (a later rider, a LINUX REPLAY line), the new line goes after the LAST line of that anchor's block, before the next heading or the next numbered item." Both notes have dated lines after them: the DUAL-MODEL CHECK of 2026-09-05 is a check OF the note (II.1 line 143: "Correction to the pair recorded above"; II.4 line 176: "Corrections to the note above"), followed in II.1 by the POINTER, READ and two RIDERs (144–147) and in II.4 by the Session-22 RIDER (178). The rule's end point is "before the next heading" — `### II.2` at 149, `### II.5` at 180. The blank lines at 142/175 and 177 are the Session-15/16 paragraph layout, not block boundaries, and the writer applied the end-of-entry reading himself at IV.1 (after the Suzuki RIDER at 394, which is not about the REFINEMENT anchor either).
   (b) *Deixis the insertion would break.* II.1's check at 143 says "this line is no longer single-check" and "the pair recorded above"; II.4's at 176 says "the note above". Inserting a Session-34 rider — which itself carries a single-check/dual-checked label — between the note and those lines puts a different line directly above them.
   (c) *File discipline and chronology.* Each entry's dated lines run in date order (II.1: 09-03, 09-05, 09-10, 09-10, 09-25, 09-26; II.4: 09-03, 09-05, 09-16). A 09-29 rider above the 09-05 check breaks that order; at the close it keeps it.
   The rider still names its subject in its own head ("v2 of arXiv:2609.02882"), so nothing is lost by the move. **Result positions in the 699-line file: 35, 72, 151, 183, 400, 692** (my patched dry run, below).
5. **"six lines" vs the brief's "five lines" — CLOSES.** The brief's "five lines" counts the bullets and names the paragraph separately ("five lines — … — plus the count-header paragraph", BRIEF line 1); the paragraph's own sentence follows the s32/s33 convention (bullets + paragraph; see `count` above). No pair.

### Placement pairs (proposed file, prose outside the blocks — the block headings must say where the script puts the line)

**P4a — the II.1 block heading.**

OLD: ## Block: II.1 — the Lamzouri v2 RIDER, one top-level bullet (directly AFTER the DATED NOTE whose head is

NEW: ## Block: II.1 — the Lamzouri v2 RIDER, one top-level bullet (placed per the reader's P4: directly AFTER the entry's LAST line, the Session-28 E1 RIDER at line 147 whose head is `- **[RIDER 2026-09-26, Session 28 (E1, M5-U formulation slot`, and directly BEFORE the blank line 148 and `### II.2` at 149 — not directly after the DATED NOTE, which is the rider's subject and whose head is

**P4b — the II.1 block heading, continued.**

OLD: — line 141 of the 692-line file — and directly BEFORE the blank line 142 and the DUAL-MODEL CHECK bullet at 143;

NEW: — line 141 of the 692-line file, followed by the blank line 142 and the note's DUAL-MODEL CHECK at 143;

**P5a — the II.4 block heading.**

OLD: ## Block: II.4 — the Lamzouri v2 RIDER, the same text, one top-level bullet (directly AFTER the DATED NOTE whose head is

NEW: ## Block: II.4 — the Lamzouri v2 RIDER, the same text, one top-level bullet (placed per the reader's P5: directly AFTER the entry's LAST line, the Session-22 RIDER at line 178 whose head is `- **[RIDER 2026-09-16, Session 22 — from Theorem M2 clause 7`, and directly BEFORE the blank line 179 and `### II.5` at 180 — not directly after the DATED NOTE, which is the rider's subject and whose head is

**P5b — the II.4 block heading, continued.**

OLD: — line 174 of the 692-line file — and directly BEFORE the blank line 175 and the DUAL-MODEL CHECK bullet at 176;

NEW: — line 174 of the 692-line file, followed by the blank line 175 and the note's DUAL-MODEL CHECK at 176;

Each of P3, P4a, P4b, P5a, P5b: OLD occurs exactly once in the proposed file, NEW zero times (checked by script before applying). The purpose paragraph (line 3) and finding 2 are the writer's record of his decision; this read supersedes them and they need no edit (they are not inserted).

Anchors of the new placement (my `grep -c -F` over the 692-line zoo): "- **[RIDER 2026-09-26, Session 28 (E1, M5-U formulation slot" → 1 (line 147; blank 148; `### II.2` 149); "- **[RIDER 2026-09-16, Session 22 — from Theorem M2 clause 7" → 1 (line 178; blank 177 above, blank 179 below; `### II.5` 180). Anchors of the unchanged placements, each 1: the Session-33 count paragraph (33), the I.1 WITNESSES bullet (69), the IV.1 Suzuki RIDER (394), item 10's PAIR CHANNEL sub-bullet (685), "11. **Theorem M2's Lemma G" (686). The DATED NOTE head occurs twice (141, 174) and the script tells them apart by continuation text + entry heading, as the writer says.

## Block 5 — script strings (for P2 and P4–P5), tested (Tue Sep 29 14:30:11 IST 2026)

`scripts/zoo-insert-s35.py` as written accepts P1 but refuses P2 (the rider would leave its allowed set, line 161) and places the riders at the notes (lines 262–278, 366–369). Nine string changes, each OLD occurring exactly once in the script (checked by `str.count` before applying):

**S1a** (permit P2 in the rider's allowed set)
```
OLD: OLD_LABEL = "single-check — orchestrator's reading"
NEW: OLD_TAIL = "so the degeneracy recorded here is untouched."
     NEW_TAIL = "so what this entry records (II.1's ceiling, II.4's degeneracy) is untouched."  # reader's P2: II.1 records a ceiling, not a degeneracy
     OLD_LABEL = "single-check — orchestrator's reading"
```
**S1b**
```
OLD: for s in (OLD_BRACKET_RIDER, OLD_QUOTE, OLD_LABEL):
NEW: for s in (OLD_BRACKET_RIDER, OLD_QUOTE, OLD_LABEL, OLD_TAIL):
```
**S1c**
```
OLD: base = staged_rider.replace(OLD_BRACKET_RIDER, NEW_BRACKET_RIDER)
NEW: base = staged_rider.replace(OLD_BRACKET_RIDER, NEW_BRACKET_RIDER).replace(OLD_TAIL, NEW_TAIL)
```
**S2a** (the two end-of-entry anchors)
```
OLD: NOTE_II4 = NOTE_HEAD + "The Hilbert-space form of this degeneracy"
NEW: NOTE_II4 = NOTE_HEAD + "The Hilbert-space form of this degeneracy"
     END_II1 = "- **[RIDER 2026-09-26, Session 28 (E1, M5-U formulation slot, `results/e1-m5u/FORMULATION.md` §2–§4; entered at the Session-29 zoo stream)"
     END_II4 = "- **[RIDER 2026-09-16, Session 22 — from Theorem M2 clause 7 (`results/c2-m2/separation-note.md` §7.2"
```
**S2b** (both asserted unique)
```
OLD: for a in (ANCHOR_COUNT, PREV_COUNT, ANCHOR_I1, PREV_I1, PREV2_I1, STATUS_I1, NOTE_II1, NOTE_II4, ANCHOR_IV1,
NEW: for a in (ANCHOR_COUNT, PREV_COUNT, ANCHOR_I1, PREV_I1, PREV2_I1, STATUS_I1, NOTE_II1, NOTE_II4, END_II1, END_II4, ANCHOR_IV1,
```
**S3** (II.1: the note's neighbor checks stay; the insertion moves to the entry's last line)
```
OLD: lines[i + 1:i + 1] = [blocks["ii1"]]
NEW: e = unique_index(lines, lambda ln: ln.startswith(END_II1), "II.1's last line (the Session-28 E1 RIDER)")
     entry_of(lines, e, "### II.1 ")
     if not (i + 2 < e) or lines[e + 1] != "" or not lines[e + 2].startswith("### II.2 "):
         sys.exit("II.1's Session-28 E1 RIDER is not the entry's last line after the DATED NOTE, before the blank and '### II.2'")
     lines[e + 1:e + 1] = [blocks["ii1"]]
```
**S4** (II.4, likewise; the shape note, blank, DUAL-MODEL CHECK, blank, RIDER is asserted)
```
OLD: lines[i + 1:i + 1] = [blocks["ii4"]]
NEW: e = unique_index(lines, lambda ln: ln.startswith(END_II4), "II.4's last line (the Session-22 RIDER)")
     entry_of(lines, e, "### II.4 ")
     if e != i + 4 or lines[e - 1] != "" or lines[e + 1] != "" or not lines[e + 2].startswith("### II.5 "):
         sys.exit("II.4's Session-22 RIDER is not the entry's last line (note, blank, DUAL-MODEL CHECK, blank, RIDER), before the blank and '### II.5'")
     lines[e + 1:e + 1] = [blocks["ii4"]]
```
**S5** (post-checks at the new positions; replace the four lines 366–369)
```
OLD: if lines[144] != blocks["ii1"] or not lines[143].startswith(NOTE_II1) or lines[145] != "" or not lines[146].startswith(DUAL_HEAD):
         sys.exit("the II.1 rider is not at line 145 directly after the II.1 DATED NOTE")
     if lines[178] != blocks["ii4"] or not lines[177].startswith(NOTE_II4) or lines[179] != "" or not lines[180].startswith(DUAL_HEAD):
         sys.exit("the II.4 rider is not at line 179 directly after the II.4 DATED NOTE")
NEW: if lines[150] != blocks["ii1"] or not lines[149].startswith(END_II1) or lines[151] != "" or not lines[152].startswith("### II.2 ") or not lines[143].startswith(NOTE_II1):
         sys.exit("the II.1 rider is not at line 151 directly after the entry's last line (the Session-28 E1 RIDER), before '### II.2'")
     if lines[182] != blocks["ii4"] or not lines[181].startswith(END_II4) or lines[183] != "" or not lines[184].startswith("### II.5 ") or not lines[177].startswith(NOTE_II4):
         sys.exit("the II.4 rider is not at line 183 directly after the entry's last line (the Session-22 RIDER), before '### II.5'")
```
(The "NEW:"/"OLD:" markers and the five-space continuation indent are presentation; the script's own indentation is zero spaces for `if`/`e =`/`lines[...]` and four for `sys.exit`.)

**S6** (the printed positions)
```
OLD: the six blocks at lines 35, 72, 145, 179, 400, 692; SHA-256 after
NEW: the six blocks at lines 35, 72, 151, 183, 400, 692; SHA-256 after
```
Non-functional, optional: the docstring (lines 6–8) and the comment at 359–361 still describe the note-adjacent placement and the positions 145/179.

**Tested.** In a scratch tree (the zoo `07a87152…`, both STAGED files, the proposed file with P1–P5b applied, the script with S1a–S6 applied; scratchpad, not the project): rc 0; "the rider carries the label 'dual-checked (orchestrator Fable 5.1 + Opus 5 reader, Session 34)'"; "+7 lines (692 -> 699); entries 58 (I 8, II 5, III 21, IV 19, V 5); Group IV 19 (no heading added); the six blocks at lines 35, 72, 151, 183, 400, 692"; `diff` hunks **34a35,36 / 69a72 / 147a151 / 178a183 / 394a400 / 685a692**; 699 lines, 58 headings 8/5/21/19/5 by my grep; lint `lint_s27.py` on the amended proposed file: "7 block(s) checked; British-spelling candidates … none"; the five 10(g) phrases: 0. SHA-256 in the scratch tree: amended proposed file `b4df557f326ca22d1d8a87a8de21d0b4425df4da4d661fb4643acc1f180410d3`, amended script `f065ca27c5b77400bd6b6255aae26bdf1580c2547fa47077dc82b87cd4dd1c37`, dry run `8e66cdc0de6f13f598191b5fd10c4a2e7220ef6d1af7397dd8f4157a25bdfae8`. If the orchestrator's application of the pairs reproduces these three hashes byte for byte, the application is exact.

**Observation, no pair.** Run without `--dry-run` the script writes `BARRIER-ZOO.md` itself (line 375, `out = dry if dry else ZOO`), whereas BRIEF line 12 says it "never writes BARRIER-ZOO.md itself" and line 18 has the orchestrator insert by `cp` of the dry run. The s33 script has the same line (its 395) and was accepted; the bytes are the same either way. The orchestrator should follow BRIEF line 18 (dry run, diff, `cp`).

## Block 6 — verdict table and verdict for the orchestrator (Tue Sep 29 14:30:38 IST 2026)

| row | verdict | one-line reason |
|---|---|---|
| `count` | **CLOSES after P3** | +7, 692 → 699, 58 = 8/5/21/19/5, Group IV NO; "six lines" is the house convention; one phrase follows the placement ruling |
| `i1` | **CLOSES** | every number at `00-main.log` 2, 3, 10, 11, `99-summary.txt` 9–10, 17–22, the two 04 logs (3, 14 lines), HARVEST-NOTE 11–12, 18, 21 |
| `iv1` | **CLOSES** | the same, `99-summary.txt` 7–8, the two 04 logs (1, 1 lines), HARVEST-NOTE 9–10 |
| `fq10` | **CLOSES** | the same, `99-summary.txt` 11, the PairChannel 04 log (8 lines; `prop45` 5, `floor_holds_integer` 7, `floor_fails_anchor` 8) |
| `ii1` | **FIX-FIRST → CLOSES after P1, P2, P4a–b + S1a–S6** | numbers and quotations all at v2 lines 14, 131–150, 186–187, 272–297, 987–998; "same data class" AGREED (standing order 7); "the degeneracy recorded here" is wrong for II.1; placement at the entry's close |
| `ii4` | **FIX-FIRST → CLOSES after P1, P2, P5a–b + S1a–S6** | as `ii1` (the same text); placement after the Session-22 RIDER at 178 |
| script | **FIX-FIRST (S1a–S6)** | refuses P2 as written; places the riders at the notes |
| Group IV | **NO** | five bullets and a paragraph; 58 headings, 8/5/21/19/5, before and after |

**Standing order 7: AGREE** — v2's (2.6)–(2.7) read only α_j (the diagonal coefficients, v2 (2.17)), Bessel ((2.16), (2.19)), the trace (2.21) and the integer atoms of the real/non-real × simple/multiple split (R₁/R₂ lines 353–358, S₁/S₂ lines 582–585, used in (2.28) line 594); (2.7)'s extra hypothesis is an upper bound on the same ‖F‖²_HS (line 632). The rider's label becomes "dual-checked (orchestrator Fable 5.1 + Opus 5 reader, Session 34)" (P1).

**Total OLD/NEW pairs for the proposed file: 7** (P1, P2 — each applied in both `ii1` and `ii4`, its OLD occurring exactly twice, once per block; P3, P4a, P4b, P5a, P5b — each OLD exactly once), **plus 9 script strings** (S1a, S1b, S1c, S2a, S2b, S3, S4, S5, S6).

**Closing verdict: AGREES-WITH-CORRECTIONS.** Apply P1–P5b to the proposed file and S1a–S6 to the script; run the dry run; it should add +7 lines (692 → 699) at hunks 34a35,36 / 69a72 / 147a151 / 178a183 / 394a400 / 685a692, print the label "dual-checked (…)" and the positions 35, 72, 151, 183, 400, 692, and reproduce the scratch hashes of Block 5 (proposed `b4df557f…`, script `f065ca27…`, dry run `8e66cdc0…`); then insert by `cp` as BRIEF line 18 says. Before applying, the orchestrator should re-derive two things itself: (i) that the zoo is still `07a87152…` (the script's gate does this), and (ii) the placement ruling (flag 4) — it overrides the writer's stated choice on the brief's own "before the next heading" clause, so the orchestrator should read zoo lines 141–149 and 174–180 and confirm.

Files: this read only. Proposed file (`c10b00c8…`), script (`1750f601…`) and zoo (`07a87152…`) re-hashed at Tue Sep 29 14:30:38 IST 2026: unchanged. Nothing committed.
