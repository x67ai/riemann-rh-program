# Re-check (Opus 5) of the Siegel-zero world scout after the fix pass — Session 24, changed items only

**Written 2026-09-24 to the orchestrator's re-check brief. Objects: `results/c2-siegel/siegel-world-scout.md` as the fix pass left it (SHA-256 6aa3b2c0ca2b4761da3d07c4574118cc9fd3234cf9ac365d4a1980dd62aabf04, matching `verify/hashes.txt` line 1 and `SHARED.md` block 3), `results/c2-siegel/FIX-BRIEF.md`, and `verify/planted_real_zero_fix.py` with its `_run.log` and `_out.json` (hashes match `verify/hashes.txt` lines 3, 7 and 11). My first check is `results/c2-siegel/check-O.md` (SHA-256 b11f970d…53ec, unchanged). New code of my own: `verify-O/o4_recheck.py`, with `o4_recheck_run.log` and `o4_recheck_out.json` (one process, under 1 s; hashes appended to `verify-O/hashes.txt`). Log citations: `fix:N` is line N of `verify/planted_real_zero_fix_run.log`; `o1:`, `o2:`, `o3:`, `o4:` are lines of my own `verify-O/*_run.log` files. Report line numbers refer to the file before my edits (223 lines) unless marked "now". I applied four one-line edits to the report myself (§9 rows 26–28, listed under item 8). Nothing was committed.**

## Verdicts in one table

| item | verdict | what was checked, in one line |
|---|---|---|
| 2 sharpenings adopted into §2.2 | **CLOSES** | closed form a_K, D₀ = 64π²e^{2γ}, D₁ = 16π²e^{2γ}, D₁ sharp, parity D₁⁺ = 3701.45 and D₀⁺ = 46368.1, root 1.5384, negative mass 0.812946: all at `fix:2–14` and equal to my `o1:19–24`, `o2:1–2` |
| 3 planted-zero table, V.4 | **CLOSES** | the 32-element column reproduced independently in u-space to every printed digit (`o4:15–35`), including the new leader Gauss σ = 1 at +0.5947; closing conductors equal my `o2:42–47`; every FIRES/silent label stands |
| 4 §3 Deuring–Heilbronn | **CLOSES** (after one parity edit I applied, row 28) | classical column 3.87 / 8.48 and 2.85 / 7.46 re-derived; envelope sketch copied faithfully; "Turán's power-sum method" |
| 5 close, I.8, rider A6, row A7, GHL, novelty | **CLOSES** (after two one-line edits I applied to §1, rows 26–27) | I.8 lines 159–163 are check-O lines 146–150 byte for byte; A6 and A7 are verbatim; GHL quotation matches the page image of p. 178; the close follows from §1–§3 |
| 6 §4 twin primes, B–H | **CLOSES** | the twin-prime sentence is labeled; Definition 1 now reads E ⩾ 3 |
| 7 lint, U.S. English, numbers to logs | **CLOSES** | the eight numbers of check-O item 7 each now sit at a log line or are corrected; no banned hedge; "normalised" occurs only inside quotations |
| 8 §9 ledger completeness | **CLOSES** | 25 rows cover every fix of check-O items 2–7 and amendments A1–A8; three rows (26–28) added by me |

**I.8 may be inserted as it stands in the report: YES.** Its text (report lines 159–163) is the text of check-O item 5(d) without change, and nothing this re-check found touches it.

---

## Item 2 — the adopted sharpenings (§2.2): CLOSES

- **Closed form and thresholds.** Report line 69 prints a_K(s) = (1/π)[Re ψ(½ + is/2) − log π] + log|D|/2π for χ_D odd, which is check-O line 50. The fix script evaluates it against quadrature of μ₀ ∗ A_K in the two-digamma form at seven points, with maximum difference 2.79·10⁻¹⁶ (`fix:2–9`). D₁ = 500.936739 and D₀ = 2003.746956 with D₀/D₁ = 4 (`fix:10–11`) equal my `o1:19` and `o2:2`. The monotonicity is now argued from ∂_y Re ψ > 0 (report line 71), which is check-O line 54, and the §8 "inferred" entry is removed (report line 179).
- **Which hypothesis does what.** Report line 65 carries the three statements of check-O lines 44–46 (cap: w ≥ 0 only; single element: ŵ ≥ 0 and a_K ≥ 0 on supp ŵ; cone-wide: a_K(0) ≥ 0 ⇔ |D| ≥ D₁).
- **Sharpness.** Report line 71 states D₁ sharp by the narrow-Gaussian argument of check-O line 57 and prints the closing conductors 111.06, 148.16, 256.35, 393.14, 462.30, 496.85 (`fix:78–83`). These equal my `o2:42–47` to every digit, including 148.16 at δ = 0.05 (`o2:43`), which check-O's text did not print but my log did.
- **Parity.** D₁⁺ = 3701.45 and D₀⁺ = 46368.1 (`fix:12`) equal my `o1:20`. The report's reading rule (line 71) scopes every later "|D| ≥ 501" to D < 0 and adds D ≥ D₁⁺ for D > 0.
- **D = −20 constants.** A_K(0) = −0.733233, a_K(0) = −0.512598, root 1.5384, negative mass 0.812946 (`fix:13`) equal my `o1:21` and `o1:24`.

## Item 3 — the planted-real-zero table and the V.4 controls: CLOSES

**(a) The Part B column, recomputed independently.** The fix script computes the share in ξ-space against a_K in closed form (`verify/planted_real_zero_fix.py`, functions `share_w` and `arch1_w`). My `o4_recheck.py` instead computes the share in u-space, as 2∫w k_y with k_y(u) = cosh(yu)/cosh(u/2), from the closed-form inverse transforms of the four families (Fejér (1 − cos Tu)/(πTu²); Fejér² (2/(Tu²) − 2 sin(Tu)/(T²u³))/π; Gaussian (σ/√2π)e^{−σ²u²/2}; Poisson e^{−a|u|}). The u-space and ξ-space shares agree to 3·10⁻¹³ on four elements at two depths (`o4:6–13`). The family has 32 elements (`o4:1`), namely 9 Fejér, 9 Fejér², 8 Gaussians and 6 Poisson, as report line 85 states (the count "31" survives only as a stale label string at `fix:57` and in the script's line 14 docstring; the list itself is 32, `fix:19`). Results at D = −20:

| δ | report column 7 | my best single (`o4:16–20`) | runner-up |
|---|---|---|---|
| 0.1 | +0.595 (Gauss σ = 1) | +0.59470 [Gauss σ = 1] | +0.56504 [Gauss σ = 1.5] |
| 0.05 | +0.861 (Poisson 0.55) | +0.86069 [Poisson 0.55] | +0.82758 [Poisson 0.6] |
| 0.02 | +1.136 | +1.13641 | +1.05531 |
| 0.01 | +1.237 | +1.23671 | +1.13776 |
| 0.001 | +1.331 | +1.33087 | +1.21498 |

The Gaussian σ = 1 leader at δ = 0.1 is right: the full-line Poisson a = 0.6 margin is +0.50549 (`o4:21`, equal to my first-check `o3:7`), and Poisson a = 0.55 gives +0.47398 there (`o4:22`), so the tail correction moved the leader from Poisson to Gaussian. The pole-cap ratio 0.999882 (`o4:14`) equals `fix:20`.

**(b) The controls at |D| = 2005 and 10⁶.** My best double margins at |D| = 2005 are +2.27145, +3.04487, +3.59630, +3.79690, +3.98523 (`o4:25–29`), equal to `fix:36–40`; the end points equal my first-check `o3:13–14`. The best single margins −0.57877 … −0.07257 (2005) and −1.17311 … −0.25836 (10⁶) equal `fix:36–46` (`o4:25–35`). Report line 91 prints these values.

**(c) Labels.** For each of 5 depths × 4 conductors (D = −20, −4, 2005, 10⁶), the fix log's single and double labels (`fix:24–46`) equal those of the first print (`planted_real_zero_run.log` lines 36–58); I compared all 40 pairs. My own run gives the same labels at D = −20, 2005 and 10⁶ (`o4:16–35`). Part A (columns 2–6) was not rerun by the fix pass and was reproduced in my first check (check-O item 3(a), `o2:7–26`). **Every FIRES/silent label of the planted-zero table stands.**

**(d) The other moved numbers.** The ledger constant 6.830 and z* = 0.343146 (`fix:15–16`); the saturation roots 0.33443 and 0.09716 (`fix:17–18`, equal to my `o2:66–67`); the dlVP values 0.4021, 0.3705, 0.3563 (`fix:90–92`, equal to `o2:35–37`); the pure-Poisson and Gaussian δ_max·log|D| series and the three asymptotes 0.343146, 0.686292, 1.003449 (`fix:93–100`, equal to `o2:51–58`); the positive control over the wide window −11.5105, −22.6049, −72.3018, −182.8258 (`fix:102–105`, equal to `o2:27–30`). Report lines 87–91 print them with those citations.

## Item 4 — §3, the Deuring–Heilbronn reading: CLOSES (after edit row 28)

- **Classical column.** Report lines 111–116 print (2/3)log(1/(δ₀ log|D|)) = 3.87 / 8.48 at |D| = 20 and 2.85 / 7.46 at |D| = 10⁶ (`fix:109–114`). By hand: log 20 = 2.9957, so (2/3)log(1/(10⁻³·2.9957)) = (2/3)(5.8105) = 3.874 and (2/3)log(1/(10⁻⁶·2.9957)) = 8.479; log 10⁶ = 13.8155, giving 2.855 and 7.460. The plain value (2/3)log(1/δ₀) = 4.61 / 9.21 is also printed (report line 118; `fix:108`). The ratio ranges "1.4 to 8.5" (plain) and "1.2 to 6.9" (Heath-Brown's normalization) are the minimum and maximum of `fix:109–114` (1.44 and 8.54; 1.21 and 6.91). The caption carries both caveats of check-O line 103 (q large, δ small; element-to-theorem).
- **Envelope (A2).** Report line 122 states the envelope sentence and the sketch in the terms of check-O lines 97–101: the split at |s − t| ≤ t/2, c_P = 2.012, the two conditions, the band (8 + o(1))/log(|D|t²/16π²), the comparison c₂ log δ⁻¹ > 8 + o(1), vacuity for |D| < D₁, and the label `[checker's sketch, single-check]`. The derivation of the band: a_K(t/2) = (1/π)[Re ψ(½ + it/4) − log π] + log|D|/2π ≈ (1/2π)log(|D|t²/16π²) for large t, and 4/(πδ) ≤ that gives δ ≥ 8/log(|D|t²/16π²). The sketch uses the odd-character closed form of a_K, so it is proved for D < 0; the report said "|D| > D₁" in §3 and in the close with no sign. **Edit applied (§9 row 28):** "for |D| > D₁" → "for D < 0 with |D| > D₁", in the §3 envelope sentence and in the close. For D > 0 the analogous sketch with D₁⁺ was not written out by either agent.
- **Expansion and attribution.** The corrected expansion 1 − k_{y₀}(u) = δ₀u·tanh(u/2) + O(δ₀²u²) is at report line 105 (check-O line 93). "Turán's power-sum method", with the p. 267 sentence quoted, replaces "Linnik's power sums" at report line 122 and in §8 (line 180), as check-O line 109 requires.
- **Saturation roots in §3.** 0.33443 / 0.09716 with the measured 0.3195 / 0.0931 below them (report line 122; `fix:17–18`; my `o2:64–67`).

## Item 5 — the close, I.8, the rider, the Instruments row, GHL, novelty: CLOSES (after edits rows 26–27)

**(a) The rescoped sentence (A8).** The refuted claim is withdrawn in §1 (report line 47) with the bound Z_K(w) ≥ w(0)·log|D| − C(w) and the seven Z_K(w_B) values 1.45 … 34.93 and ŵ-means 0.12 … 2.06 … 2.78 (`fix:116–122`, equal to my `o1:26–32` line for line). C(w_B) = 1.915 (`fix:123`) uses P_ζ directly instead of my bound P_ζ ≤ B_ζ; it is a sharper constant for the same inequality, and at D = −20 it gives log 20 − 1.915 = 1.081 ≤ 1.452 (`fix:116`). Two defects in the §1 text, both fixed by me:
- The seventh discriminant is printed "−(10¹⁶ + 63)". 10¹⁶ + 63 is not prime (sympy `isprime`, run in this re-check), and the discriminant actually computed is −10000000000000079 = −(10¹⁶ + 79) (`fix:122`; my `o1:32`). **Edit applied (§9 row 26).**
- "the pole cap … rules out every cone certificate against a single real zero once |D| ≥ D₁, at every conductor above 501" carries no sign on D and stands before the reading rule of §2.2. For D > 0 with 501 ≤ D < D₁⁺ = 3701.45 the even-character density is negative at 0 (D₁⁺ is its zero-crossing conductor, `fix:12`), so §2.2 does not support the claim there. **Edit applied (§9 row 27):** "once D < 0 with |D| ≥ D₁ (for D > 0: D ≥ D₁⁺ = 3701.45), at every such conductor".
The factor-2 slip is fixed: report line 43 states the local content 1/sin(πδ) ≤ Ψ_K(0), and line 47 explains the log's folded form once.

**(b) The close (§6, report line 156) against §1–§3 as now printed, clause by clause.**
- Single real zero uncertifiable for D < 0, |D| ≥ D₁ and D > 0, D ≥ D₁⁺; D₁ sharp: §2.2 (report line 71; `fix:10–12`, `fix:78–83`). Follows.
- Two real zeros or a double one within c/log|D|, with c ≥ 0.343 / 0.686 / 1.003 and "the cone's optimum not computed": §2.3 (report line 89; `fix:86–100`). Follows.
- Complex zeros at t ≥ 28 within c/log(|D|(2 + t)): §2.4(iii) (report line 95; `dh_repulsion_run.log` column "none"). "t ≥ 28" is restored. Follows.
- "has the shape of the classical exceptional-zero clause … by the pole cap — a printed antecedent is GHL 1994": §2.2 and §2.4 (report lines 65, 95). Follows; "exactly" no longer describes the relation (the only "exactly" left in §2.4 is the sentence "'Shape', not 'exactly'").
- R1's mechanism absent at D = −20 and at small conductor; at large conductor clause 2 may hold, redundantly: §1 (report line 47). Follows.
- Repulsion bounded, saturating, uniform over the cone by the envelope: §3 (report line 122), now with D < 0 on both sides (row 28). Follows.
- No bearing on RH for ζ: §3 "Labels" (report line 124). Follows.

**(c) I.8, A6, A7 — verbatim.** A byte comparison (Python, this re-check) gives: report lines 159–163 equal check-O lines 146–150 exactly; the quoted rider in report line 165 equals the quoted A6 text of check-O line 152 exactly (432 characters); the check's A7 row text (check-O line 154) occurs verbatim inside report line 171, preceded by the row's name cell. Report line 164 adds a parenthetical fix-pass note beside the entry about the `_fix` script, and leaves the entry's text as the check printed it. The EXECUTABLE TEST pointer is the check's own (A5).

**(d) GHL 1994 at the page.** I rendered `fetched-r2/r-25a-goldfeld-hoffstein-lieman-1994-appendix-effective-zero-free-region-annals140.pdf` (SHA-256 ddcc7a2d5bb1a86e1f5d45bfcdea9935e3821133b2fcb823754deedd0d9a4d05, as the report prints) PDF pages 3–4 (journal pp. 178–179) at 200 dpi and read them as images. The report's quotation (line 65) matches the page word for word: "LEMMA. Let φ(s) be a Dirichlet series with nonnegative coefficients, absolutely convergent for Re (s) > 1. Suppose also that φ(s) has an Euler product, so φ(s) ≠ 0 for Re (s) > 1, and φ′(s)/φ(s) is negative for s real and > 1. Let φ(s) have a pole of order m at s = 1 [and let Λ(s) = s^m(1 − s)^m G(s)φ(s) satisfy Λ(s) = Λ(1 − s), with Λ(s) entire of order 1. Here G(s) = D^s ∏_{i=1}^{l} Γ((s + c_l)/2) with D > 1 the "level" of φ(s).] Then there exists an effective constant c, depending only on l and m, such that φ(s) has at most m real zeros in the range 1 − c/log M < s < 1". The bracketed passage is what the report's "…" elides; it is where l is defined, so the elision loses no hypothesis that bears on the use made of the lemma. The page continues "where M = 1 + D max{|c_l|}". p. 179 prints the proof "Σ_{i=1}^{n} 1/(s − β_i) ≤ m/(s − 1) + c₁ log M … Let s = 1 + δ/log M … a contradiction is obtained whenever n ≥ m + 1", as the report paraphrases. The report's page attribution (lemma p. 178, proof p. 179) is right. The pdftotext rendering of φ as "so" is confirmed by my own pdftotext run.

**(e) Novelty labels.** The label check-O item 5(c) prescribes appears at report line 65, after the GHL quotation, with "no web search" and the list of pages read; the I.8 STATUS carries `[novelty: dual-model check 2026-09-24]` for the cone-wide form and the sharp D₁ (report line 163). The header (report line 3) states the relabeling rule. The one remaining `[novelty: single-check]` (report line 105, the Deuring–Heilbronn "one-line consequence" as a cone-sector reading) was not a subject of check-O and correctly stays single-check.

## Item 6 — §4 twin primes and Bondarenko–Heap: CLOSES

- Report line 132: "Twin primes have no known implication in either direction with RH `[recalled, unverified; no source on disk — zoo III.4 states the parity block, not this]`", as check-O line 165 requires; §8 (line 180) lists it among recalled items.
- Report line 130: "1 − β = 1/(E log q) with E ⩾ 3, along an exceptional sequence q_j → ∞, B–H pp. 1–2", which is check-O line 164's replacement text; the note that "E → ∞" is not in Definition 1 is kept as history.

## Item 7 — lint, U.S. English, numbers to logs: CLOSES

- **Lint.** A search of the report for "clearly", "obviously", "easy to see", "well known" and "well-known" finds none (Python search, this re-check). The only non-U.S. spelling found by a suffix search (-ise, -ised, -ising, -isation, -yse, -our) is "normalised", twice, both inside the Bondarenko–Heap quotation at report line 130.
- **The eight numbers of check-O item 7.** (1) 2.830 → 6.830 (report line 89; `fix:15`). (2) 0.32 → 0.33443 (line 122; `fix:17`). (3) classical column in δ·L units (lines 111–118; `fix:108–114`). (4) Part B column full-line (line 85; `fix:24–28`; independently `o4:16–20`). (5) the refuted "never ≥ 2" sentence withdrawn (line 47; `fix:116–123`). (6) ≈ 230 → ≥ 256.35 (line 87; `fix:80`). (7) the positive-control window stated (line 91; `fix:102–106`). (8) 1.540 → 1.5384 (line 71; `fix:13`). Each old value now appears only as a quoted "first print" reference (Python search for each old string, this re-check).

## Item 8 — the §9 ledger against my item list: CLOSES

Every fix of check-O maps to a ledger row: item 2 sharpenings 1–3 → rows 1, 3, 4 and "which hypothesis" → row 2; 3(b) → row 5; 3(c) → row 6; 3(d) → rows 7–8; 3(e) → row 9; 3(f) → row 10; 4(a) → row 11; 4(b)/A2 → row 12; 4(c) → row 13; 4(d) → row 14; 5(a)/A8 → rows 15–16; 5(b) → row 17 (with rows 4, 12, 15); 5(c) → row 18; 5(d)/A1, A3, A4, A5 → row 19; 5(e)/A6 → row 20; 5(f)/A7 → row 21; 6 → rows 22–23; 7.1–7.8 → rows 7, 8, 13, 9, 15, 5, 10, 24. Row 25 (31 → 32 elements) is the author's own find and is right (`fix:19`; `o4:1`). The check-O line numbers cited in rows 1–24 match check-O's lines. I added rows 26–28 (below) with a dated note after the table.

## Edits I applied to the report (2026-09-24, Opus 5; §9 rows 26–28)

1. §1 (now line 47): "−(10¹⁶ + 63)" → "−(10¹⁶ + 79)".
2. §1 (now line 47): "once |D| ≥ D₁, at every conductor above 501 and at every depth" → "once D < 0 with |D| ≥ D₁ (for D > 0: D ≥ D₁⁺ = 3701.45), at every such conductor and at every depth".
3. §3 envelope (now line 122): "for |D| > D₁ (so a_K ≥ a_K(0) > 0)" → "for D < 0 with |D| > D₁ (so a_K ≥ a_K(0) > 0)".
4. §6 close (now line 156): "for |D| > D₁ and t ≥ t₀(D)" → "for D < 0 with |D| > D₁ and t ≥ t₀(D)".

None moves a number or a label. The report is now 228 lines (three ledger rows and one note line added).

## Not examined

The band 0 < t < 28; t₀(D) of the envelope; the cone's optimal double-zero constant; the D > 0 version of the envelope sketch. None of these is asserted by the report.

## Hashes

- `results/c2-siegel/siegel-world-scout.md` before my edits: 6aa3b2c0ca2b4761da3d07c4574118cc9fd3234cf9ac365d4a1980dd62aabf04; after: 56d2bbf6814d4c35ae587ec5b66579909a30af89f2c8b41b4d53192fae4cfc9d. (`verify/hashes.txt` line 1 still records the pre-edit value; the author's other twelve hashes verify, `shasum -c`, this re-check.)
- `verify-O/o4_recheck.py` 5cf6dbfb…8edf, `o4_recheck_run.log` b910b4d6…436d, `o4_recheck_out.json` 772802d6…a063 (full values in `verify-O/hashes.txt`).
