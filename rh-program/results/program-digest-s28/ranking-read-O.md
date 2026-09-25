# Session 28 — Opus 5 read of the program-wide consolidation digest (standing order 7 shape; KICKSTART 10(a), 10(d))

**Written Sat Sep 26 03:04:20 IST 2026 (machine clock, `date`), one agent (Opus 5), reads only.** Brief `results/program-digest-s28/READ-BRIEF-O.md` SHA-256 cf7c9de6b6411083e4e3eaf95d4ef2bdcaffee3f2922b8eac7673b3955834ba9 (18 lines, recomputed). Digest `results/program-digest-s28.md` SHA-256 c8a4ff98641c7effe6349a33ed931cd2a32b9cb4246b65b56618cf6984957363 (303 lines, recomputed; equal to the writer's SHARED block). Writer brief `results/program-digest-s28/BRIEF.md` read in full. Every anchor below is quoted at the CURRENT line of the file named, with that file's SHA-256 where it matters:

- `BARRIER-ZOO.md` 1de55c2ee319a7e89e724c94780ebf0626a4fa5f045968deafc66e4c7413d9ca (662 lines; unchanged since the digest).
- `results/e1-m5u/FORMULATION.md` c4b4561850209106fccb08a8b166780f5a6eb7c8cc920ec2f715e5e3b0f7ef2e (315 lines); `results/e1-m5u/read-O.md` fdd5031a17638432921b18214d3eef161d180d71c5fda744e4751f694f6b8bf5.
- `results/e3-borger-rung1/NOTE.md` d71fb8a0189bbcb2b910e036f4849e1b8df2487f2d1b46be1e077ff79f9330c5 (150 lines by `wc -l`); `results/e3-borger-rung1/read-O.md` 0065879234660a4bf9c025a2b64aca81430d4f5c9a0e5624cd97096a57d54cb2.
- Direction files, all equal to the digest's hashes: C2 90e80d25…, C3 d53c53c9…, D1 cb985682…, B2 76f248e8…, A4 c4bdaf73….
- `STATUS.md` is now 1b6070816162b839… (moved since the digest's c780e18b… by the orchestrator's item-4 lines; lines 31–36 and 112–121 re-read tonight). `LOG.md` 08214325… (1772 lines).
- Krein–Langer, IEOT 78 (2014): `fetched-r2/r-02a-krein-langer-2014-continuation-hermitian-positive-definite-ieot78.pdf` 805a08052aa200b1053ab1a79bb7e327b94ec94cb02a22f3fb7cf6eeb45abd8a. Pages 33–35 were extracted with `pdftotext -layout` and read (§5.1: the class G_a; Theorem 5.1, p. 34; Corollary 5.2, p. 34).

**Method.** I opened every source a finding rests on, and whole lines before declaring a sentence absent (ORCHESTRATOR-NOTES precedent). About 90 quotations of the digest were tested by script against their stated file and line (`grep -F` on the exact quoted string at the line, then on the whole file). The pointer rows were also checked against the s27 reconciliation commit 1460f06 (`git show 1460f06:rh-program/directions/…`), to see when each pointer went stale. No new mathematics is claimed. The one mathematical reading below (§1 M1) takes the IV.18 rider's own identity at its own bandwidth, is labeled `[reader's reading]`, and is for the orchestrator to re-derive (standing order 5).

---

## §1 Factual check of §0–§C

### MATERIAL

**M1 — Rank 1's premise fails at κ's own bandwidth. The κ-dual is not a Krein–Langer continuation set, and the proposed product ("the largest κ with the modified screw function in G_∞") is empty at every κ.** (The digest, lines 61, 138, 203, 244–252.)

The sources, at the line:
- **IV.18's budget-floor rider (ii), BARRIER-ZOO.md line 522.** It defines κ := inf_{w ∈ Σ_∞} B(w)/ŵ(0). IV.18's STATEMENT (line 516) sets the budget as B(w) = 2ŵ(0) + ∫(ŵ ∗ μ₀)A = ∫ŵ d[2δ₀ + a], with a = μ₀ ∗ A on the zero line. The dual certificate is "a pair (ψ ≥ 0 on the zero line, φ ≥ 0 on the prime line) with (2 − κ)δ₀ + a = ψ + φ̂/2π". The line adds that "a(0) = −0.653847 < 0" and that the negative part of a on |τ| < 6.31 has mass I₋ = 2.241523 > 2.
- **E1 §2.3(a), FORMULATION line 106, and §5.1, line 221.** Both apply Krein–Langer to ONE FIXED datum, F_Λ = K_A − Λ-comb. The positive measure is sought with σ̂ = F on (−L, L), and the only free object is σ.
- **Krein–Langer Theorem 5.1 (p. 34).** It characterizes a single given g ∈ G_a by the representation (5.2) with τ ≥ 0. Corollary 5.2 gives one continuation g ∈ G_∞. At a = ∞ there is no continuation freedom: the theorem is then the Lévy–Khintchine-type representation of one function.

`[reader's reading]` of these sources:
- **At Σ_∞ (the rider's κ).** A single dual pair that certifies B(w) − κŵ(0) ≥ 0 for every compactly supported w in the cone must satisfy the identity against every such ŵ, that is, as distributions on the whole line. So ψ = (2 − κ)δ₀ + a − φ̂/2π is DETERMINED by φ. What remains is whether some positive φ on the prime line makes that measure positive. No interval appears, no datum is prescribed on (−L, L), and Theorem 5.1 adds nothing beyond Bochner–Schwartz.
- **The digest's closed-form product is the fiber φ = 0 at a = ∞.** That fiber asks for "the screw function of (2 − κ)δ₀ + a in G_∞" (line 203). By (5.2), that means τ = (2 − κ)δ₀ + a ≥ 0. This fails for every κ, because a < 0 on |τ| < 6.31 (the rider, line 522). "The largest κ for which …" therefore names no κ.
- **At finite bandwidth L (κ_L, with κ = lim κ_L).** The identification holds only fiberwise. For each FIXED positive φ on (−L, L), the ψ's form a Krein–Langer continuation set of the datum "(2 − κ) + â − φ on (−L, L)", and Theorem 5.1 decides that fiber. The κ-question is the union over the free φ, which is the rider's LP dual restated. Theorem 5.1 supplies no criterion for it.

Hence:
- The digest's "I infer … its non-emptiness is decided by Theorem 5.1's criterion at each κ" (line 203) and "re-prices … from a hypothesis into a printed criterion" (line 244) do not hold.
- Rank 1's clause (1) (line 247) returns at once "not of that form (at Σ_∞); at finite L, fiberwise only". By the digest's own stop line, "E5 stands as at s27".

A second, smaller misreading sits in the same contract. Clause (2) (line 248) and F2's 10(n) line (205) say "the pole weight enters the δ₀-coefficient linearly, E1 (3.1), line 167 … by D1(b) (0.2′)". In E1's g-normalization the δ₀-coefficient is the conductor or archimedean constant: "(log A_k)·δ₀" (FORMULATION line 167), and "− c_A·δ₀" with c_A = 5.37218… (`results/c2-m5b/FORMULATION.md` line 34). The pole weight is the coefficient 2 of 2cosh(u/2)du (FORMULATION line 16). It becomes a δ₀-coefficient only on the zero line of IV.18's w-normalization (2ŵ(0), line 516). A brief would send the unit to the wrong coefficient.

**M2 — §A(vii) rows 1–6 are stale at birth once the batch is inserted, and the digest's causal account of the stale pointers is wrong.** (The digest, line 107: "Five Session-27 pointer/correction rows already disagree … because Session 28's insertions moved the lines they cite".)

Most of these pointers were already wrong when they were inserted. At the s27 reconciliation commit 1460f06:
- **D1 181's targets.** B2's sweep row was already at line 117 (not 112), and C2's phase-ceiling row at line 122 (not 120).
- **D1 182's targets.** The Riemann–Siegel evaluator was already at line 189 and M2b at line 190 (not 187 and 188).
- **C2 104 (then 103).** Its "label after Unit A, line 129" pointed at a row that was at line 133.
- **C2 129 (then 128).** Its "(line 130)" and "(129)" pointed at rows that were at lines 134 and 133.
- **B2 109.** Its "C2 lines 117–118" pointed at rows that were at 118–119.

D1 and B2 have no Session-28 line at all (the digest's own §A, lines 79 and 91). Their pointers were stale AT INSERTION, because the pointers were computed before the 15-row batch landed. Session 28 added exactly one C2 line above the table (the work-log line 93), which explains the extra shift of 1 in C2.

The consequence matters more than the history. Inserting rows 1–8 as a batch shifts the very lines that rows 1–6 cite:
- In D1, rows 1–2 go in under line 181, so the Untried evaluator moves 189 → 191 and M2b 190 → 192. Row 2's "read 187 as 189, 188 as 190" is then wrong on arrival.
- In C2, rows 4–6 go in under lines 104, 129 and 139, so the rows at 119–120, 123, 134–135, 141 and 143 move by one to three. That breaks rows 1 and 3–6.
- In B2, row 3 moves the sweep row 117 → 118, which breaks row 1.

Remedy: insert the rows with the line numbers struck and the first-words titles kept (each row already carries its titles), or recompute every number after the batch has landed. The digest's lesson on line 120 ("by row title") is right; the rows as written do not yet follow it.

**M3 — IV.17 is missing from every sentence about M5-U's integrality ground.**
- **What IV.17 already kills.** BARRIER-ZOO.md IV.17 (heading line 541) has the KILLS clause "Any brief that relaxes marks to reals — or uses a continuous-density adversary, a convex-hull-of-moments argument, or 'LP duality shows …' for the pair channel — and reads off a bound for the integer-mark class; any baseline or closure argument … that names no integrality step" (line 544). Its EXECUTABLE TEST (3) reads "locate the line where integrality is consumed … and return the brief if there is none" (line 545).
- **Where the digest leaves it out.** E1's decisive conclusion is that no real-weighted relaxation decides M5-U and that "integrality … [is] its entire content" (FORMULATION line 114). That is the IV.17 class on a new datum (the Krein band datum). Neither E1 (grep: no "IV.17" in FORMULATION.md or read-O.md) nor the digest (its only IV.17 mentions are the line anchors at lines 95 and 127) links them.

This changes:
- §B's Sector-II cell (line 134) and items 12, 14 and 16. The "integrality alone" ground is a ground whose gate is already printed in the zoo; it is not unmarked territory.
- §C sentence 6(b) (line 180). E1's theorem is a rider, and it is even less a new proof class than the digest argues. Its class ("relax marks to reals") is IV.17's.
- The queued E1 rider on II.1 (FORMULATION line 245). It should carry a pointer to IV.17, and its executable test should cite IV.17 test (3).
- F4's trigger (b) (line 219). "A printed integrality theorem for Krein continuations" must pass IV.17 test (3) at brief time.

**M4 — F1's "one clause the compilation lacked" (line 189, repeated at line 254) is already in the zoo, and the SPEC's price departs from the adjudicated figure without saying so.**
- **The clause is already printed.** IV.10's rider R-b′ (BARRIER-ZOO.md line 462, quoted by the digest itself at §F item 14) reads: "item 2 of III.20 needs a two-dimensional host over a base below Z; a one-dimensional doubled object … can pass the log p clause … and still carry no Castelnuovo–Severi step". The s27 SPEC list already contained "IV.10's Hom test and HOST-DIMENSION check" (`results/program-digest-s27.md` line 305, as the digest quotes it at line 189).
- **What E3 adds.** E3's target clause (NOTE line 119) adds the comparison-map form ("a comparison map that would carry the ghost components onto Cartier divisors of a two-dimensional object with a canonical class"). That is a sharpening of the R-b′ requirement, not a new axiom. F1's own stop line (ii) ("the target clause turns out to be III.20's item 2 restated") is therefore the likely close, and should be tested at brief time against line 462, not discovered by the unit.
- **The price.** The adjudicated SPEC price is 1 slot: "Kept as the standing-order-6 fallback at 1 slot, NOT funded until E3 returns" (`results/program-digest-s27/ORCHESTRATOR-NOTES.md` line 14), and "the standing-order-6 axiom-level SPEC … (1 slot …) waits on item 2's return" (STATUS.md line 119). The digest prices ½ from the s27 read's "(≤ ½ slot)" (`ranking-read-O.md` line 169), which the adjudication did not adopt. The closing note (line 297) compares only to "the s27 digest's 1". I agree with ½ or less on the merits (M4's first point), but the departure from the adjudication must be stated as one.

### MINOR

1. **The Z-form I-infer (§A C3 (iv), line 69; the rank-0 question, line 242) over-reaches in its premise, and its question is already answered by the record.** Its premise is "Theorems 3.3–4.2 are proved for a Dedekind domain R with (D1)–(D2)". What the NOTE actually establishes:
   - §3 opens "Throughout, U = Spec R is an affine open of S" (NOTE line 56).
   - Only Theorem 3.3 is transferred to Z: "With R = Z the same proof (it uses only (D1)–(D2)) gives …" (line 77).
   - Theorems 3.4 and 4.2 are curve statements (q, N_N, Z(S, t); lines 81–85, 102).
   - Theorem 4.1(b)'s argument ((F1)–(F3), line 93) is general, but it is not stated for Z.
   - Theorem 3.1's Z case is Borger's printed §1.10 (line 66).
   - The Z-analog of Theorem 4.2's consequence IS on the record, as a corollary reading: NOTE §6 H6, line 119: "its intrinsic data are, by the IV.10 rider (2026-09-25), deg(Γ₁ ∩ Γ_n) = Λ(n) … the exact analog of Theorem 3.4 with Theorem 4.2's consequence: nothing beyond ζ's own data."
   - The queued IV.10 rider (NOTE line 132) carries only Theorem 3.3's Z closed form ("over Z the same closed form corrects the naive reading (Γ₂, Γ₃) = log 6 to 0"). It carries no Z-form of 4.1(b) or 4.2.

   The rank-0 question can therefore be re-worded as a scope check: should the rider cite H6 (line 119) for the Z-analog? It is not an open inference.
2. **"The only mechanism that has EVER proved an RH" is attributed to the zoo** ("s27 line 68, quoting line 347", digest line 67). The phrase occurs nowhere in BARRIER-ZOO.md (`grep -n "EVER proved"`: no hit; line 347 reads "In every fully-proven RH case, BOTH hold …"). Its source is `results/completeness-critic.json` ("it is the only mechanism that has EVER proved an RH (Weil/Deligne)"). The misattribution descends from `results/program-digest-s25.md` line 191 ("III.20 (B), line 341") through the s27 digest. This is the s27 hygiene lesson (2): a quotation inherited without being opened.
3. **Quotation fidelity (the digest's rule (1), line 3).** Four quotations are paraphrases set in quotation marks, and four are misanchored:
   - Paraphrases:
     - "the prime relations cancel" (line 57): FORMULATION line 203 reads "it cancels in E_μ = 0 — so no prime relation is produced".
     - "a LOCAL version of Theorem 1.6 would be precisely clause 6's input (III)" (line 219): line 205 reads "a LOCAL form of Theorem 1.6 would be exactly clause 6's input (III)".
     - "an instrument by shape" (line 180): line 34 reads "**Instrument**, 'deeper' …".
     - §F item 11 turns the file's double quotation marks around "positive integer-atomic measures …" (line 245) into single ones.
   - Misanchors:
     - "a ghost carries ζ's prime side by definition" is at FORMULATION line 265, not 203.
     - "cannot be an L-function's zero set" is at line 294 (the proposed C2 Untried text), not §3.4 line 179.
     - "a self-pairing is not" is NOTE lines 104 and 127, not E3 `read-O.md` line 44.
     - "no construction is licensed" is C3 lines 216 and 242, not 240.

   None changes a verdict. Each is the defect class the digest says it applied as a rule.
4. **"Ranks 4–5 … unfunded (STATUS.md line 119)"** (lines 168, 172; the brief's line 7 wording). Line 119 reads "**Then** E5 κ > 0 (≥ 2 slots, inside C2's budget, after item 3) and E4 …". That is queued, with the NOT-funded items listed separately. It bears on §5 (the record's order).
5. **Row counts disagree between §A C2 (i) and §A(vii).** Line 51 says "41 rows in 45 table lines (98–143)". Line 105 says "C2 lines 99–143 (45 table lines: 35 primary rows, 10 dated …)". There are 10 ↳ rows at lines 104, 105, 109, 114, 116, 118, 120, 122, 124 and 129, so 35 primary rows. Line 51 is the error.
6. **§C sentence 5 and the §E last line ("no candidate OBJECT for the one mechanism shape", lines 178, 266) state more than the record.** The record's sentence is "outside the four killed classes" (HARVEST line 3). The record also carries:
   - two watch lines for exactly this ingredient: C3 Untried line 228 ([CC7], the Connes–Consani square, inside K1) and line 229 ("Substrates outside Deninger's class: (D) the condensed archimedean FF-curve … a doubled object with an archimedean component"; HARVEST P8 places the global prismatic square inside K4);
   - the Q-S4⁗ object, open in print inside K3 (§B item 11).

   Scope the sentence to "no printed candidate outside K1–K4".
7. **Two IV.18 riders are labeled "(ii)":** the budget-floor rider at line 522 and the Lorentzian rider at line 525. Rank 1's contract and F2 cite "IV.18 rider (ii), line 522", which is correct, but a brief should name it "the budget-floor rider (ii) of 2026-09-16".
8. §0's E3 NOTE "151 lines": `wc -l` gives 150. This is cosmetic.

Everything else I tested in §0–§C holds at the line. That includes:
- the three closures' quotations (NOTE 3, 11, 102, 119, 123, 125, 132, 135; FORMULATION 106, 108, 112, 114, 122, 124, 130, 138, 144, 173, 183, 197, 209, 211, 217, 225, 229, 245, 265, 279, 311; both read-Os' verdict lines);
- the 10(o) labels against STATUS 116–118 and LOG 1764, 1767, 1770;
- the LOG token counts (1763, 1764, 1767, 1770) and the missing writer counts (1766, 1769);
- the stale headers (C2 line 5, C3 line 5) and the C3 Untried hash precision (line 225: "writer f962e737… amended");
- the absence of a §4.2 note beside `results/c2-m5b/`;
- every §F anchor except those listed in 2 and 3 above. §F items 1–10 and 12–15 were checked by exact string at the stated line; §F item 6's zoo line 429 carries a paraphrase of Theorem F1, and the verbatim text is `results/c2-m5b/FORMULATION.md` lines 90–96, as the item also cites.

---

## §2 The Instruments reconciliation

| # | Row | Verdict | Basis (file:line, current) |
|---|---|---|---|
| 1 | D1 181 → B2 117, C2 123 | **AGREE** on the targets. Strike the line numbers at insertion (M2). | B2 117 "[EXTENSION 2026-09-25, Session 26 — D4] The sign channel SWEPT above the verified height"; C2 123 "Prime-side sign channel: the phase ceiling of the double-double pipeline". Both were already at 117 and 122 at 1460f06, so the pointer was stale at birth. |
| 2 | D1 182 → 175, 189, 190 | **AGREE** on the targets. The row is stale on arrival if rows 1–2 are inserted with numbers (191, 192). | D1 189 "A Riemann–Siegel-class rigorous evaluator for the mp leg"; D1 190 "M2b — the Polymath15 analytic bridge discharged in Lean"; D1 175 unchanged. |
| 3 | B2 109 → C2 119–120 | **AGREE** on the targets. Shifted by row 4's insertion. | C2 119 "Off-line zeros of f_DH in the strip (negative-control heights)"; 120 "[CORRECTION 2026-09-24, Session 24 — record moved]". At 1460f06 they were at 118–119. |
| 4 | C2 104 → 103, 134 | **AGREE**. Shifted by its own insertion. | C2 103 "M2 separation bandwidth L*(δ, t) …"; 134 "… label after Unit A". |
| 5 | C2 129 → 134, 135 | **AGREE**. Shifted by rows 4–5. | C2 135 "… label after Unit B", "kernel-checked modulo H-edge, H-B‴"; 134 "… label after Unit A". |
| 6 | C2 139 (regimes) → 141, 143 | **DISAGREE on the defect class and the header; AGREE on the body text** (see note (a) below). | C2 139: "Poltoratski's gap theorem (G_X = 2πC_X, arXiv:0908.2079 Thm 2) gives NO pinning: C_X = ∞ …; no theorem on the record decides integer-atomic gaps". C2 141. The cited `read-O.md` rows 2c, 3c and 4 exist (lines 83, 88, 90). |
| 7 | C3 213 → 222, 5/55/380/2475 | **AGREE**. | NOTE line 87 "a₁, a₂, a₃, a₄ = 5, 25, 125, 605; … 5, 55, 380, 2475 = N₁ … N₄"; `verify/curve_g1_points_N4_run.log` present; `verify-O/curve_ghost_groebner_O_run.log` line 2 "character sums: N_1..N_4 = [5, 55, 380, 2475] … a_1..a_4 = [5, 25, 125, 605]" and line 43 "sum … = 2475; N_N = 2475 OK". |
| 8 | C3 after 219, pairwise degrees over Z (optional) | **AGREE**. Population row; the closed form is the one NOTE line 77 proves. | NOTE line 77 "I_{m,n} = p^{1+min(v_p(m), v_p(n))}Z when … differ at exactly one prime p and Z otherwise"; `verify/witt_pairs_Z_run.log` line 2 "pairs 1 <= m < n <= 24 … 0 mismatches"; `verify-O/witt_pairs_Z_lattice_O_run.log` line 3 "pairs m < n in the box: 1770; mismatches … 0". |

Note (a), on row 6. The row's first clause is a true statement about Poltoratski's theorem for finite complex measures, and it is not contradicted. E1 §2.3(b) strengthens it to positive continuations of the real-weighted relaxation. That is a precision or extension, not a supersession, a caveat the digest itself records at line 298. Enter it as "↳ [POINTER 2026-09-26, Session 28 — strengthened, from E1 §2.3–§2.4]", not "record moved", and strike the line numbers (M2).

**The digest's "consistent" list — AGREE.** I re-checked every in-table line pointer by script (the full list: C2 104, 122, 124, 129; D1 168, 170, 172, 177, 179–182; B2 107, 109, 111, 112, 114, 116; A4 202–203; C3 212–213; B4 81–82; B3 84). C2 122's "B2 line 116" is current. B2 107 "D1 line 176", 112 "D1 line 168 (and 169)" and "B4 line 81", and 114 "D1 lines 174–175" are current. B4 82 and B3 84 are current. C3 212 (`m0-axiom-note.md` lines 372–375: the DH witness table) and C3 213 (`referee-m1.md` line 27: "5/55/380") are current. A4 202's "BARRIER-ZOO.md lines 394, 508" is stale, and A4 203 is stale against the 662-line zoo (IV.7 at 418, IV.17 at 541), but 203 is self-dated with the 655-line hash and states the "by number" rule. So no row is needed: AGREE with the digest.

**MISSING (my own) — two, both outside the Instruments tables, for the rank-0 stream:**
- **X1 (zoo, bookkeeping).** A pointer from the queued E1 rider on II.1 (FORMULATION line 245) to IV.17's KILLS (line 544) and EXECUTABLE TEST (3) (line 545), per M3.
- **X2 (C2 κ row 102, or the IV.18 budget-floor rider — the orchestrator's choice of home).** A one-line dated record note: the κ-dual at Σ_∞ determines ψ from φ, and its φ = 0 fiber is empty at every κ (a < 0 on |τ| < 6.31); Krein–Langer Theorem 5.1 applies only fiberwise at finite L and returns the LP dual. The note carries the label `[reader's reading, to be re-derived]`, per M1.

I found no missing Instruments row.

**Tally.** AGREE 7 (rows 1, 2, 3, 4, 5, 7, 8; rows 1–5 conditional on striking the line numbers at insertion). DISAGREE 1 (row 6, class and header only). MISSING 2 (X1, X2, both bookkeeping lines outside the tables).

---

## §3 The §B table — cells I would change

| Cell (digest line) | Change | The entry that changes it |
|---|---|---|
| Sector II / M5-U (134); items 12, 14, 16 (156, 158, 160) | Add: "the integrality-only ground is gated by IV.17: any argument that relaxes marks to reals is killed in kind (KILLS, line 544), and every YES brief must locate its integrality step (test (3), line 545). E1's theorem is IV.17's phenomenon on the Krein band datum." The status stays NOT EXCLUDED and BANKED. | BARRIER-ZOO.md IV.17, lines 541–545 (M3) |
| Positivity / cone, κ (138); item 3 (147) | Replace the I-infer with: "the κ-dual at the rider's bandwidth (Σ_∞) is not a continuation problem (ψ is determined by φ); at finite L it is a union over a free positive prime measure of Krein–Langer continuation sets, which Theorem 5.1 decides fiber by fiber without deciding the union." The status stays NOT EXCLUDED; OPEN; unchanged. | BARRIER-ZOO.md line 522; Krein–Langer Thm 5.1 p. 34; FORMULATION lines 106, 221 (M1) |
| Spectral / geometric substrates (133), (a) | "A name for the missing ingredient" → "a sharpened form of IV.10 R-b′'s requirement (line 462: 'a two-dimensional host over a base below Z'): the target of a comparison map with Cartier images (NOTE line 119)". | BARRIER-ZOO.md line 462 (M4) |
| Same row, (b) | "Theorem 4.2's Z-analog, … I-infer flag" → "on the record at NOTE §6 H6, line 119, as a corollary reading; the queued IV.10 rider carries Theorem 3.3's Z closed form only". | NOTE lines 77, 119, 132 (MINOR 1) |
| Item 4 (148) | Add the watch lines C3 Untried 228 ([CC7], K1) and 229 (condensed archimedean FF-curve; HARVEST P8: inside K4). "NO first rung remains on any printed object" stands. | `directions/C3-geometric-substrate.md` lines 228–229; HARVEST line 17 |
| Item 17 (161) | "NEW … NOT EXCLUDED as ground" → "NOT new in kind: the requirement is IV.10 R-b′ (line 462) and the archimedean-component watch is C3 Untried 229; what is new is E3's comparison-map form and its rung-1 instance (the triple (W_S*(S), S ×_k S, c))". It is still NOT EXCLUDED, and no printed candidate exists. | BARRIER-ZOO.md line 462; C3 line 229; NOTE lines 119, 132 |

I searched the zoo and the results for anything that DOES cover the other "still open" items:
- **Item 5** is not an RH route (I.8 STATUS, line 116). I agree.
- **Item 6** is unchanged.
- **Item 10** is covered by the closure text, which I re-read tonight (`grossmann-sweep2.json` `closure.still_unswept[0–2]`).
- **Item 11** stays "open in print" at line 533.

---

## §4 Per §D candidate

**F1 — the axiom-level SPEC.**
- *Beyond the zoo:* AGREE ("not applicable").
- *Ladder:* AGREE. Rung 1 is the record: E3's Theorems 3.4 and 4.1–4.2 and Cor. 7.6, and III.21 at line 357 for DH.
- *Nearest object:* on disk (`results/e3-borger-rung1/sources/arxiv-abs-0906.3146.html`; `results/d2-scout-s26/sources/O-arxiv-0906.3146.pdf`; `results/c3-r/m0-axiom-note.md`, 724 lines).
- *Stop line (ii):* DISAGREE on its placement. It should be TESTED AT BRIEF TIME against IV.10 R-b′ (line 462), where it most likely fires (M4).
- *Price:* DISAGREE as cited. The adjudicated price is 1 slot (ORCHESTRATOR-NOTES line 14; STATUS line 119). I support ≤ ½, or ¼ if stop line (ii) fires at brief time, but that is a re-adjudication, and the digest must say so.

**F2 — E5 κ > 0.**
- *Beyond the zoo:* AGREE (inside IV.18; "deeper" on covered ground, not a route).
- *Ladder, first rung (the one-page identification):* DISAGREE. The answer is determinable from the rider's own text (M1). The ¼-slot first line would buy a sentence already on the record.
- *Stop line (iii):* AGREE, with care. It looks first to Suzuki 2026 Thm 1.4 (`fetched/y-09-…`, on disk; E1 line 46). The small-a lowest eigenvalue of the prime-free Weil form is a related quantity, but it is normalized by ‖f‖², not ŵ(0). Proposed only as a place to look.
- *Price of the explicit unit:* AGREE (≥ 2 slots explicit, 1 non-explicit; rider line 522). Its brief must state the dual correctly: a positivity condition on (2 − κ)δ₀ + a − φ̂/2π over a free positive φ, not a Krein continuation.

**F3 — D5 in Lean.** AGREE on every field; `results/adjudication-C1.json` is present.

**F4 — BANKED.** AGREE. Add IV.17 test (3) as the brief-time gate on its trigger (b) (M3).

**F5 — the other square, NO.** AGREE. NOTE line 119 and Cor. 7.6 as quoted at NOTE line 102; Borger's caveat verbatim at NOTE line 117.

**F6 — the disproof side.** AGREE (STATUS line 135; D1 lines 175, 180, 188).

**F7 — the explicit sentence.** AGREE, with item 17 re-scoped per §3.

**[reader's addition]** — no new unit. Two bookkeeping lines go into rank 0 (X1, X2 of §2), at 0 extra slots inside rank 0's ¼.
- *X1's "beyond the zoo":* none. It is a pointer between II.1's rider and IV.17.
- *X2:* a record note on IV.18's covered ground.

---

## §5 The ranking — AGREES-WITH-CORRECTIONS

- **Rank 0 (the zoo stream, bookkeeping, ¼): AGREE, with four changes.**
  - The eight rows go in with the line numbers struck, or recomputed after the batch (M2).
  - Row 6 goes in as "strengthened", not "record moved".
  - X1 and X2 are added.
  - The Z-form question is re-worded as a scope check against NOTE line 119 (MINOR 1).
- **Rank 1 (F2's first line, ¼): DISAGREE — not funded as a unit.** Its clause (1) is answered by the rider's text (M1). The digest's own stop ("the identity is not a band-prescription problem … E5 stands as at s27", lines 247 and 252) applies now. Its clause (3) (F1(a) against the rider's finite-mass sentence) was already framed by the s27 read as "not the same statement" (`ranking-read-O.md` line 146). It needs no unit; X2 records it.
- **Is the order F2-first-line above F1 settled by the record?**
  - *By the record:* the broad order "E5 before the SPEC". STATUS line 119 queues "Then E5 κ > 0 (≥ 2 slots …)" while the SPEC "waits on item 2's return", and the brief (line 8) places the SPEC as "§E's last line".
  - *By preference:* the carve-out of a separate ¼-slot first line and its placement at rank 1. The digest labels this a judgment call (line 297), and it rests on the I-infer that M1 removes.
- **My ranking, settled where the sources allow:**
  - **0.** The zoo stream (¼; bookkeeping), as amended above.
  - **1.** F1, the SPEC (bookkeeping under standing order 6). Before the brief is written, stop line (ii) is pre-tested against IV.10 R-b′ (line 462). If it fires, F1 becomes a one-line III.20 note inside rank 0. If it does not, F1 runs at the price the orchestrator re-adjudicates (≤ ½ on the merits; 1 on the record).
  - **2.** F2, E5 at the record's price (≥ 2 explicit or 1 non-explicit; STATUS line 119 "Then"), with its dual stated correctly (§4).
  - **3.** F3 (2; on the next Lean stream).
  - *Order.* Putting F1 before F2 is my judgment: it costs a quarter to a half of F2's price, and F2 is "deeper on covered ground" (the digest, line 204). If the orchestrator reads STATUS line 119 as binding, F2 precedes F1, and I would not contest that.
  - *NOT FUNDED:* F4, F5, F6, D7, Units C/D and the two referee pairs, as the digest has them.
- **10(d) and "no referee pair now": AGREE.** No trigger fired by the letter: no Group-IV entry (zoo-s28 read-O line 20; E3 read-O line 83; E1 read-O line 244), author plus one reader only, and no Lean. On merit both theorems are riders. E1's class is IV.17's (M3), and E3's is IV.10's HOST-DIMENSION check (line 462).

---

## §6 Verdict for the orchestrator

**One line.** AGREES-WITH-CORRECTIONS. Rank 0 stands, with the rows' line numbers struck. Rank 1 (the κ-dual as a Krein–Langer problem) is withdrawn as a unit, because at κ's own bandwidth the dual is not a continuation problem and the proposed "largest κ in G_∞" is empty. F1 moves up, but only after its stop line (ii) is tested against IV.10 R-b′ line 462 at brief time.

**What must change before rank 1 (as the digest wrote it) could be briefed.** Nothing salvages it as written:
1. The identification sentence at digest line 203 must be replaced by the fiberwise statement (M1). The "largest κ with the modified screw function in G_∞" product must be struck.
2. The pole-weight coefficient reference in clause (2) must be corrected: it is the cosh(u/2) coefficient at FORMULATION line 16, not the δ₀-coefficient of (3.1).
3. After 1 and 2, the unit has no product the record lacks, and it should not be launched. What survives goes into rank 0 as X2, and into F2's brief at its s27 price.

**Before any §A(vii) row is inserted:** strike or recompute the line numbers (M2), and re-class row 6.

**Before F1 is briefed:**
- quote IV.10 R-b′ line 462 and state what the target clause adds beyond it;
- state the price as a re-adjudication of ORCHESTRATOR-NOTES item 8's 1 slot;
- scope "no candidate OBJECT" to "outside K1–K4" (MINOR 6).

**Before the E1 rider enters the zoo:** add the IV.17 pointer (M3).

Lint (10(g)): the four forbidden phrases were checked by `grep -ci` on this file (count recorded in SHARED.md). U.S. English. No file was written other than this one and a dated block in `results/program-digest-s28/SHARED.md`. Nothing was committed.
