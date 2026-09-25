# Zoo stream `zoo-s28`, Session 28 — READER report (Opus 5, independent second model, standing order 7)

**Opened Sat Sep 26 00:17 IST 2026; written Sat Sep 26 00:22:55 IST 2026 (machine clock, `date`).**
**Brief:** `results/zoo-s28/BRIEF.md` SHA-256 `d5f2bf2ce9f0be123c18116cff5b24a5288e41940d3b9725f242885adb787052` (recomputed, matches), section "The reader (Opus 5)". FORMAT precedent `results/zoo-s27/zoo-entries-read-O.md`.
**Writer's deliverables, recomputed:** `results/zoo-s28/zoo-entries-proposed.md` `13c652b4ea82b5497488c0fc2085d7819b0de7f88ed35e557e127ba18877a9f6` (matches); `scripts/zoo-insert-s28.py` `cfbce515755d209fe313f866cc4bd29c49c7723ec8fd3b0275e68d9998ab0d4e` (matches); `results/zoo-s28/dryrun-BARRIER-ZOO.md` `d8a3845e07bb0f313cb78f1863199b8a906a890284febbd4a5762f14bc598dce` (matches); `results/zoo-s28/SHARED.md` `00bfd20893eb25a21584514281dc7fe3a00642e671bae03de7140024abe82015` (matches, before my block). `BARRIER-ZOO.md` `ba6c7aec0ad63cdb703b7108318a77f227361968eb4829cad99dcd23628ef8aa` (matches; untouched by me).

---

## Verdicts, one table

| row | verdict | what I checked, in one line |
|---|---|---|
| `iv7` (IV.7 rider 1, F1) | **FIX-FIRST** → CLOSES after A1–A2 (+ script S1) | body = `705caf36…` §1 body except exactly the scope merge (difflib); head label = read-O §12 rows 1/4; every logged number at `window_residual_run.log` / `window_residual_O_run.log`; the SCOPE sentence misdescribes rider B's own scope (A2); the duplicated title struck from the HEAD, body kept (A1) |
| `ii1` (II.1 rider) | **CLOSES** after A3 (head only) | body byte-identical to `705caf36…` §2; Z-2/Z-3/Z-4 NEW present in full, OLD absent; Bombieri pp. 224–225 opened as images; the head's dual-model label is supported by read-O verdict rows 1 and 5, not by §12 row 5's words alone — cite them (A3) |
| `i3` (I.3 pointer) | **CLOSES** after A4 (+ script S2) | body byte-identical to `705caf36…` §3; Z-5 NEW present, OLD absent; w-09 pp. 3, 4, 9 opened as images; the `[printed: …]` label must be read-O §12 row 6's text exactly (A4) |
| `iii2` (III.2 correction) | **CLOSES** after A5–A6 | CC `fetched/y-03` p. 2 and Bombieri pp. 183, 224, 225, 226 opened by me as images; the quotation is exact; Theorem 12, p. 226 is the small-support positivity (|I| < log 2); version named honestly (A5); Theorem 12 is Yoshida's theorem reproved, so "printed in Bombieri 2000", not "Bombieri's" (A6) |
| `iv19` (IV.19 precision) | **CLOSES** after A7–A8 | every number at D4 lines 71, 72, 92, 250–255, 299, M6 line 10 and §7, `cost_line.json`; 3 606 s printed only in the D4 note (writer right); B2 116 / C2 121 PRECISION rows found at the line; two citation precisions (A7, A8) |
| `count` | **CLOSES** | 6 s27 lines (I.5, IV.4, III.20, IV.1 pointer, IV.10, xref) 649 → 655; `ba6c7aec…` is today's zoo; 6 lines + 1 blank = +7, 655 → 662; 8 + 5 + 21 + 19 + 5 = 58 counted in my dry-run output |
| `script` | **CLOSES** (two constants widen with A2 and A4: S1, S2; tested) | read in full; my dry run `results/zoo-s28/dryrun-BARRIER-ZOO-O.md` is byte-identical to the writer's (`d8a3845e…`); diff = six pure insertions (after 21 [2 lines], 72, 131, 191, 423, 550); numstat 7/0; 58 headings, 8/5/21/19/5; every original line survives in order; single trailing newline; zoo hash unchanged |
| Group-IV decision | **NO** | nothing here is a new proof class: F1 is rider B's finite/windowed twin (ORCHESTRATOR-NOTES item 4, §B.3 riders discipline); the other five lines are riders, pointers and corrections |

**Amendments: 8 exact OLD → NEW pairs inside the named blocks (A1–A8), plus 2 exact OLD → NEW pairs in `scripts/zoo-insert-s28.py` (S1, S2) that A2 and A4 require.** All ten are machine-readable in `results/zoo-s28/verify-O/amendments_O.py` (`16b21636…`); applied to scratch copies (never to the repo files), the amended proposed file hashes `ef03af6cfd5cebd2c7d5c0c6dbecf50aec1d4161e47e2ab12cd62ba1d8ccfd0c`, the amended script's dry run passes every assertion (+7, 655 → 662, 58, 8/5/21/19/5) and its output hashes `1de55c2ee319a7e89e724c94780ebf0626a4fa5f045968deafc66e4c7413d9ca`. Hashes: 26 / 26 of the writer's `verification` block match (§9).

---

## §1 `iv7` — IV.7 rider 1 (Theorem F1)

**Checks made.** (i) Body identity: split at the first `]**`; difflib against `results/c2-m5b/zoo-entries-proposed.md` line 7 body gives exactly two opcodes — the SCOPE sentence inserted before "Executable test:" and the clause "; inequality (cone) rows on finite configurations are not excluded by this rider (they are IV.18's and PRICING §1.2's business)" removed from the test sentence (carried in the scope sentence). Nothing else differs. (ii) Head = the brief's prescribed head verbatim; label `[novelty: dual-model check 2026-09-25]` = read-O §12 rows 1 and 4 (row 4: "with Z-1" — Z-1 NEW present in full, OLD "best relative residual" absent). (iii) Numbers at the log: `verify/window_residual_run.log` line 1 (T = 3552.792, ℓ = 6.3376, W = 39.186), configuration 26s+7d relative 1.238e-10 / 2.085e-09 / 5.705e-06 (L = 0.5 / 1 / 2), counts 6.2 / 12.5 / 24.9 vs 33, 9.007e-03 / 5.034e-02 / 3.251e-01 / 5.728e-01 (L = 2.5 / 3 / 6.338 / 12), counts 31.2 / 37.4 / 79.1 / 149.7; control 1.815e-07 / 3.042e-08 (L = 1, 2), 0.000e+00 "positions recovered" at L ≥ 3; `verify-O/window_residual_O_run.log` lines 19–20: relative 1.502e-12 and 2.084e-12. All as the rider prints them. (iv) SCOPE sentence against ranking-read-O §1.3 (lines 39–41) and zoo line 422: the A4 clause, "proposed once (PRICING §1.1(v), never run)", and "rider B's own named casualty" are at §1.3.

**Finding (material, A2).** "Scope, as rider B's: first-order EQUALITY rows …" misdescribes rider B. Rider B (zoo line 422) is proved with the two-tooth test h_{k,d} "in the strip-positive cone Σ_L" and "the cone row at every rotation φ gives |c_k| ≤ … (eq. (1.4))" — inequality (cone) rows; its "Executable test" is "the two-tooth row (1.4) with d → 0". So on PERIODIC hosts rider B already excludes cone rows, while F1 excludes only equality rows on finite/windowed hosts. As written, the sentence says rider B shares F1's equality-only limit and then says inequality rows are not excluded — a zoo reader would take cone rows on periodic hosts to be admissible, which rider B denies. ORCHESTRATOR-NOTES item 4's "the 'equality rows' limit rider B states" is the same slip; the "equality rows" wording is F1's own ("… equality rows either", ranking-read-O line 132).

**Flagged item (1), adjudicated: STRIKE the duplication, from the HEAD, keep the body.** The head title and the body's bold opening print the same 20-word sentence twice in one line. The body is the dual-checked record text (`705caf36…`); the head is this stream's new wording. Striking from the head keeps the body's identity with the record and needs NO widening of the script's identity check (the script allows any head and prints it). The house form keeps a title.

**A1** (block `iv7`, head) OLD:
```text
entered at the Session-28 zoo stream) — rider B one level up: no FINITE and no WINDOWED configuration hosts first-order (explicit-formula) equality rows either. `[novelty: dual-model check 2026-09-25]`
```
NEW:
```text
entered at the Session-28 zoo stream) — Theorem F1: rider B one level up. `[novelty: dual-model check 2026-09-25]`
```

**A2** (block `iv7`, body) OLD:
```text
Scope, as rider B's: first-order EQUALITY rows with a free positive prime datum — the A4 gate's LP
```
NEW:
```text
Scope: first-order EQUALITY rows with a free positive prime datum (rider B reaches further on PERIODIC hosts: its two-tooth rows (1.4) are strip-positive cone rows, that is, inequalities) — the A4 gate's LP
```

**S1** (`scripts/zoo-insert-s28.py`, the `SCOPE_RE` line; required by A2 — the scope-merge identity check otherwise exits) OLD:
```text
SCOPE_RE = re.compile(r"Scope, as rider B's: first-order EQUALITY rows with a free positive prime datum — .*?
```
NEW:
```text
SCOPE_RE = re.compile(r"Scope: first-order EQUALITY rows with a free positive prime datum \(rider B reaches further on PERIODIC hosts: its two-tooth rows \(1\.4\) are strip-positive cone rows, that is, inequalities\) — .*?
```
(The rest of the line is unchanged. The identity check is then widened by exactly that parenthetical and the dropped "as rider B's"; everything outside the scope sentence is still compared byte for byte.)

## §2 `ii1` — II.1 rider

**Checks made.** Body byte-identical to `705caf36…` line 11 body. Full Z-2, Z-3, Z-4 NEW strings (parsed from read-O §9) present in the block; OLD strings absent from every block (the OLD strings appear only in the writer's finding 3, as quotations). Bombieri p. 224 (PDF page 44) as an image: "An Example … same modulus q > 1 … same parity … p₀ ≥ 2 be the first prime for which χ(p₀) ≠ χ′(p₀) … compact support in (1/p₀, p₀) … Σ_ρ f̃(ρ) − Σ_ρ′ f̃(ρ′) = 0"; p. 225: "As pointed out by J. Bourgain, the existence of linear relations over intervals of arbitrary length also follows from the fact that the gap between consecutive γ's tends to 0 as γ → ∞" — Z-3's and Z-4's sources as stated. Rung-1 and Poltoratski clauses: record text, re-read by read-O (rows 5, 6); not reopened here.

**Finding (label sourcing, A3).** read-O §12 row 5 says only that the rider "stays single-check until Z-2–Z-4 are applied; after them the statement 'for POSITIVE integer-atomic measures nothing is printed in the sources opened' is dual-checked as far as the opened sources go". The head's `[dual-model check]` for the (0.5) statement and the Poltoratski clause is right — their present text IS the Opus reader's Z-2 and Z-3, from verdict rows 1 ("replaced by an exact band-limited-taper form") and 5 ("true for every closed set containing ζ's zeros") — but that support should be cited, and the label should carry the house `novelty:` prefix as in §12.

**A3** (block `ii1`, head) OLD:
```text
Label per `results/c2-m5b/read-O.md` §12 row 5: the (0.5) statement and the Poltoratski clause `[dual-model check 2026-09-25]`;
```
NEW:
```text
Label per `results/c2-m5b/read-O.md` §12 row 5, Z-2–Z-4 applied: the (0.5) statement and the Poltoratski clause `[novelty: dual-model check 2026-09-25]` (their text is the Opus reader's Z-2 and Z-3, re-derived at read-O verdict rows 1 and 5);
```

## §3 `i3` — I.3 pointer

**Checks made.** Body byte-identical to `705caf36…` line 15 body; Z-5 NEW present, OLD absent. `fetched/w-09` opened as images: p. 3, Theorem 2.4 (RH assumed; 𝒦_n = {supp η̂ ⊂ {ξ₁ + ⋯ + ξ_n ≠ 0 or |ξ₁| + ⋯ + |ξ_n| < 2}}, T-averaged (1/T)∫_T^{2T}; Montgomery n = 2, Hejhal n = 3, Rudnick–Sarnak n > 3); p. 4, §3 Theorem 3.1 (c_{j+1} − c_j ∈ {½, 1, 3/2, 2, …}, density-1 display) and §4.1 ("a point process supported on ½ℤ … We randomly translate"); p. 9, Theorem 4.7 (random ω ∈ [0, ½), "simple, ℝ-translation invariant", separations 1/2, 1, 3/2, …). The body's data-class reading and Z-5 are at the pages.

**Finding (label text, A4).** read-O §12 row 6 assigns `[printed: Lagarias–Rodgers 2020, Theorem 2.4 p. 3, §3 p. 4, Theorem 4.7 p. 9]`; the head inserts "= `fetched/w-09`" inside the label, which (a) is not the label as assigned (standing order 7: carried exactly) and (b) nests backticks, so the code span breaks when rendered. Move the file pointer outside.

**A4** (block `i3`, head) OLD:
```text
`[printed: Lagarias–Rodgers 2020 = `fetched/w-09`, Theorem 2.4 p. 3, §3 p. 4, Theorem 4.7 p. 9]` (read-O §12 row 6)
```
NEW:
```text
`[printed: Lagarias–Rodgers 2020, Theorem 2.4 p. 3, §3 p. 4, Theorem 4.7 p. 9]` (read-O §12 row 6; the paper is `fetched/w-09`)
```

**S2** (`scripts/zoo-insert-s28.py`, the i3 label check; required by A4) OLD:
```text
"`[printed: Lagarias–Rodgers 2020 = `fetched/w-09`, Theorem 2.4 p. 3, §3 p. 4, Theorem 4.7 p. 9]`"
```
NEW:
```text
"`[printed: Lagarias–Rodgers 2020, Theorem 2.4 p. 3, §3 p. 4, Theorem 4.7 p. 9]`"
```

## §4 `iii2` — III.2 record correction

**Checks made, pages opened by me with the Read tool.** `fetched/y-03` PDF pages 1–2: the title page reads "June 25, 2020" with the arXiv stamp "arXiv:2006.13771v1 [math.NT] 24 Jun 2020"; p. 2 prints "It is thus natural to implement this fundamental positivity in the semi-local framework applied to the finite set of places {∞, 2, 3, . . . , p}, and provide a conceptual reason for Weil's negativity for functions f fulfilling the support condition Support(f) ⊂ (p⁻¹, p)." — the block's quotation is exact, the ellipsis as printed. Bombieri PDF page 44 = printed p. 224 (the linear-relation example, as in §2; `pdftotext` renders the support as "(1=p0 ; p0 )", so the block's OCR remark is right); PDF page 45 = p. 225 ("12. Sets of positivity … the positivity statement needed for the proof of the Corollary to Theorem 8. Another proof can be found in Yoshida's paper [5]"); PDF page 46 = p. 226, "Theorem 12. If F(x) has compact support in an interval I of length |I| < log 2 we have T[F(x) ∗ \overline{F(−x)}] = Σ_γ F̂(γ)\overline{F̂(γ)} ≥ (log(1/|I|) − log⁺log(1/|I|) − O(1))‖F‖²", its proof noting "the contribution of the sum involving Λ(n) vanishes"; PDF page 3 = p. 183, abstract: "prove again Yoshida's theorem that it is positive definite if t is sufficiently small". The theorem named for the unconditional small-support positivity at its page: **Theorem 12, p. 226** — the writer is right. Nothing on pp. 224–226 states a "(1/p, p)" negativity. `results/literature.md` line 29 carries the dated correction (read; untouched). Zoo line 187 read.

**Flagged item (3), adjudicated.** The PDF on disk is arXiv:2006.13771v1 (June 2020); the record's "Connes–Consani 2021" is the journal year [recalled, unverified — no journal copy was opened]. Whether the p. 2 sentence reads the same, and sits on p. 2, in the journal version is NOT known from what was opened; the quotation and page are the v1 preprint's. The line must say so (A5). The attribution itself (the sentence is Connes–Consani's, not Bombieri's) holds on the version opened.

**Finding (A6).** Bombieri's §12 says "Another proof can be found in Yoshida's paper" and the abstract calls it "Yoshida's theorem … prove again": the positivity is printed in Bombieri 2000 as Theorem 12, not Bombieri's result. The block's parenthetical already quotes the abstract; the main clause should match it.

**A5** (block `iii2`) OLD:
```text
At the page the sentence is Connes–Consani 2021 (`fetched/y-03` = arXiv:2006.13771v1, p. 2):
```
NEW:
```text
At the page the sentence is Connes–Consani's (the record's "Connes–Consani 2021"; the copy on disk and opened is `fetched/y-03` = arXiv:2006.13771v1, dated June 25, 2020, p. 2 — the journal version was not opened):
```

**A6** (block `iii2`) OLD:
```text
is unchanged and is Bombieri's (Theorem 12, p. 226,
```
NEW:
```text
is unchanged and is printed in Bombieri 2000 (Theorem 12, p. 226,
```

## §5 `iv19` — IV.19 cost-line precision read

**Checks made, every number at its line.** D4 note line 71: 3742.0 s = 62.4 min, 49.8 ns/term, "the cost model's 3 606 s (M6 §7: 7.5·10¹⁰ × 181 ns + 2.05·10¹² × 2.05 ns, over the speed-up 4.93) — the model is 4 % low" (my arithmetic: (13 575 + 4 202.5)/4.93 = 3 606 s); line 72: 5299.0 s = 88.3 min, 70.5 ns/term, the concurrent replay, "one 8-thread process at a time"; line 92: 3 606 s "held to 4 % when the machine was otherwise idle"; lines 250–254: 63.1 (50.4), 68.2 (54.5), 68.9 (55.0), 68.7 (54.9), 70.3 (56.2) min (ns/term); line 255: "one 8-thread process at a time; the cost model 3 606 s is 5–17 % low"; line 299 lies in §12 (heading line 289) and reads "class A by the cost line, 63–70 min per point at L = 28.35". 62.4/60.1 = +3.8 %, 70.3/60.1 = +17.0 %: "4–17 % above the model" holds. M6 note line 10: 181 ns, 2.05 ns, speed-up 4.9, boundaries 28.35 / 31.61; §7 (lines 183–204): r_term = 181.4 ns, r_sieve = 2.05 ns, S = 4.93, classes A ≤ 1 h, A/B at L = 28.35 (X = 2.0·10¹², 7.5·10¹⁰ terms), B/C 31.61; `grep` for "3606 / 3 606 / 60.1" in the M6 note: none. `cost_line.json` `classes`: L_AB = 28.345043…, L_BC = 31.608…. So the writer's location of 3 606 s (D4 note, not M6) is right; the model is exactly one hour at L = 28.345 and 3 606 s at the rounded 28.35. CHECK-O-B line 258 read.

**Flagged item (2), adjudicated: the rows ARE at B2 line 116 and C2 line 121.** Both start "| ↳ [PRECISION 2026-09-25, Session 27 — measured at scale] the A/B boundary L = 28.35 is the cost MODEL's one-hour line (M6 §7: 3 606 s = 60.1 min at L = 28.35) …", C2's with the row-4 final clause; today B2 111 is the de Bruijn–Newman bracket row and C2 119 a 2026-09-24 CORRECTION row, so the brief's 111/119 are stale by the Session-27 insertions. The block's "line 116 … line 121" is right; C2 121's own internal pointer "B2 line 111" is stale for the same reason (a direction-file matter, outside this stream; noted for the orchestrator, not amended here).

**Findings (precision, A7–A8).** "one process at a time (D4 note lines 71, 250–254)": the "one process at a time" statement is at lines 72 and 255, and the rehearsal's idle-machine condition at line 92 — widen the citation. "its check … passed that sentence CLEAN": CHECK-O-B line 258 quotes and passes only the clause "does not bind — this is the evaluation route" against IV.19's STATUS; it does not check the timing clause — say what was passed.

**A7** (block `iv19`) OLD:
```text
one process at a time (D4 note lines 71, 250–254):
```
NEW:
```text
one process at a time (D4 note lines 71, 92, 250–255):
```

**A8** (block `iv19`) OLD:
```text
and its check (`results/d4-sign-sweep/CHECK-O-B.md` line 258) passed that sentence CLEAN.
```
NEW:
```text
and its check (`results/d4-sign-sweep/CHECK-O-B.md` line 258) passed that sentence's IV.19 item ("does not bind — this is the evaluation route") CLEAN.
```

## §6 `count`

The block is the brief's text verbatim. Session-27 lines: six (I.5, IV.4, III.20, the IV.1 pointer, IV.10, the cross-reference row — the s27 reader's verdict rows `i5`, `iv4`, `ra`, `ra_ptr`, `rb`, `xref`), 649 → 655; `ba6c7aec…` is the zoo as it stands now (recomputed). This stream: five rider/correction lines + this paragraph = six lines, plus the blank line before the paragraph = +7, 655 → 662 (the dry run confirms 662). 8 + 5 + 21 + 19 + 5 = 58, and my dry-run output has 58 `### ` headings, 8/5/21/19/5 (counted independently with a regex). No amendment. (After A1–A8 nothing in the paragraph changes.)

## §7 `script`

Read in full (289 lines). Order of guards: zoo hash first; C2 record hash `705caf36…`; six refuse-twice markers; blocks read at run time, one line each, lint, no headings; head prefixes; C2 bodies (i3, ii1 byte-equal; iv7 equal modulo the scope merge, rebuilt and compared byte for byte); Z-1…Z-5 NEW/OLD (with shortened NEW prefixes for Z-2, and "best relative residual 1.2" as the Z-1 OLD — weaker than the full strings, but my own full-string check in §2 covers them); labels; anchors by full neighboring text, each exactly once, each tied to its entry by the preceding `### ` heading and to the following blank + next heading; pure list insertion; subsequence check of every original line; 58 and 8/5/21/19/5; single trailing newline; +7 and 655 → 662; each marker exactly once. Run ONLY as `python3 "scripts/zoo-insert-s28.py" --dry-run "results/zoo-s28/dryrun-BARRIER-ZOO-O.md"`: exit 0, output `d8a3845e…` = the writer's dry run byte for byte; `diff` against the zoo shows only `22a23,24`, `72a75`, `131a135`, `191a196`, `423a429`, `550a557`; `git diff --no-index --numstat` 7 / 0. BARRIER-ZOO.md still `ba6c7aec…` afterwards. A1–A8 applied to a scratch copy of the proposed file with S1–S2 applied to a scratch copy of the script (ROOT and PROPOSED pointed at the scratch copies; output to the scratchpad): every assertion passes, +7, 58 headings; the S1 note prints the widened scope sentence. Without S1, A2 makes the script exit ("block iv7 does not carry the SCOPE sentence …"); without S2, A4 makes it exit ("i3 head lacks the read-O §12 row-6 label") — both fail closed, so a missed S cannot insert wrong text.

## §8 Group-IV decision

**NO.** F1 is the finite/windowed twin of IV.7 rider B, stated as a rider with rider B's form, elementary and dual-proved; the zoo's riders-unless-a-new-proof-class discipline and ORCHESTRATOR-NOTES item 4 ("not as a numbered entry; no referee pair is bought") apply, and nothing else in the six lines is a barrier statement. Count stays 58.

## §9 The writer's `verification` block, recomputed (Sat Sep 26 00:22 IST 2026)

26 / 26 SHA-256 values match: `BARRIER-ZOO.md`, `results/zoo-s28/BRIEF.md`, `results/c2-m5b/zoo-entries-proposed.md`, `read-O.md`, `FORMULATION.md`, `verify/window_residual_run.log`, `verify/rung1_newton_run.log`, `verify/archimedean_kernel_check_run.log`, `verify-O/window_residual_O_run.log`, `verify-O/rung1_O_run.log`, `ranking-read-O.md`, `ORCHESTRATOR-NOTES.md`, `d4-sweep-note.md`, `CHECK-O-B.md`, `m6-rung1-note.md`, `cost_line.json`, `literature.md`, B2, C2, `PRICING.md`, the three PDFs (`u-23a` `20bd544f…`, `y-03` `b8e0b54a…`, `w-09` `cf295b66…`), `results/zoo-s27/BRIEF.md`, `results/zoo-s27/zoo-entries-proposed.md`, `scripts/zoo-insert-s27.py`.

## §10 For the orchestrator

1. Apply A1–A8 to `results/zoo-s28/zoo-entries-proposed.md` inside the named blocks (keep a `*.pre-reader.md` copy) and S1–S2 to `scripts/zoo-insert-s28.py`; `results/zoo-s28/verify-O/amendments_O.py` holds all ten pairs verbatim (its `__main__` part writes only to the paths given; it asserts each OLD occurs exactly once). Expected: amended proposed file `ef03af6c…`; dry-run output `1de55c2e…` (if the amendments are applied byte-exactly as here).
2. Direction files (outside this stream): C2 line 121's internal pointer "B2 line 111" is stale (should be 116) — a dated line in C2 when next touched.
3. ORCHESTRATOR-NOTES item 4's phrase "the 'equality rows' limit rider B states" carries the same slip as the SCOPE sentence (rider B's mechanism is a cone-row inequality); record only.

Lint (10(g)): `grep -niE` for the five linted phrases finds no hit in this file. Nothing committed by the reader.
