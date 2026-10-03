# SHARED — stream haglund-conj4 (append-only; each block dated by scripts/stamp.py)

### L-lit — task 3 done (16:18 IST 2026-10-03)
- The author's web copy is `preprints/rh8.pdf` on his Penn publications page (24 pp., dated February 9, 2011; SHA-256 a8daaab8…88df; in `lit/`). arXiv has v1 only (SHA-256 a28f7336…e18c, identical to S1). Full comparison: `L-lit/PRIOR-ART.md` §3 (12-row table).
- **Web copy corrects, V and the journal do not:** p. 4 table, N = 4: **31** real zeros (V and journal: 32); p. 10 the 1/x² paragraph now ends "the coefficient of 1/x² in ΞN(x) approaches zero from below as N → ∞" (V and journal: "positive for k ≥ 3"); the constants of (52) to 13 digits and the z⁻⁴ term of (47) corrected — both corrections re-derived by this unit (`L-lit/check_task3.py`).
- **Conjecture 4 and its lead-in: word for word the same in the web copy** (p. 11).
- FLAG for the letter and for the program's paper: `results/arxiv/haglund-counterexample/main.tex` l. 72, 202–203, 495–496 call the entry 32 at N = 4 inconsistent, and the paragraph after Prop. tail quotes the p. 10 "positive for k ≥ 3" claim — both are already corrected in the author's own web copy of 2011. Any text to the author should cite V/journal as the versions concerned and acknowledge his corrected copy.
- Minor (this unit's reading): in the web copy, (54)'s "for some c > 0" is not updated to the corrected sign (with c1 = 1, 0 ≤ ci ≤ 1 the coefficient is negative).

### L-lit — task 2 done (16:27 IST 2026-10-03)
- Baccaro's PDF read whole (5 pp.): Zenodo refuses this machine (403), the identical file came from the GitHub repo named on the record (md5 66e55682… = the md5 on the Zenodo record; SHA-256 c915171b…d27d; `lit/baccaro-hc4-k1-20260822.pdf`). Report at the page: `L-lit/PRIOR-ART.md` §2.
- Theorem 2.1 (p. 2) = Conjecture 4 for k = 1 only: zeros in the open first quadrant simple with Im z′(t) < 0; no forward escape; full Puiseux multiset stays real after a real collision. k ≥ 2 "remain open" (pp. 1, 5).
- **N1 verdict:** (1) Φ_{k+1} > 0 on ℝ and ∂_tF = Φ_{k+1}(x) > 0 — in Baccaro: PDF for k = 1 (p. 3, convex kernel), and for **every k** in his repo's scratch record `hc4_all_k_log_potential_next_summand_real_positivity_v1/RESULT.md` (not in the PDF). (2) "Ξ minus a positive level" — **not found** in the PDF or the repo files read. (3) the quotient criterion — in the PDF for k = 1 as g = −Φ1/Φ2 = 1 − S_1, Δ = Im(−Φ2·conj F_z) < 0.
- For A/B (real-axis test): his all-k record notes that with ∂_tF > 0, a real double zero stays real forward iff F_zz(x0, t0) < 0; a certified double with F_zz > 0 would be a counterexample to (R). Far zeros (k = 1): an analytic outer theorem, every zero with |z| ≥ 256 in the cone Re z > Im z > (3/2) log|z|.
- Lean: only an abstract local collision theorem is verified; the interval atlas and the final k = 1 theorem are not Lean results (his own READMEs). Side note: the conditional Lean interface `FirstQuadrantCertificate` requires Φ2 ≠ 0 on the whole open first quadrant, but Φ2 has two zeros there (his own record; |Φ2| ≈ 5e−19 at them with our evaluator), so that Lean theorem is vacuous — this does not touch the PDF's argument.

## B-track — ladder passed (16:27 IST 2026-10-03)
Evaluator: own mpmath code (`B-track/code/hb.py`), route T (Xi - tail) checked against the literal sum.
L1: Haglund's 19 zeros of Xi_1 (p. 16) reproduced to <= 6.9e-22. L2: largest real zeros of Xi_1..Xi_4 within 3e-11 of the
table. L3: Xi_27(3144.8946) = -1.76019463128e-1070, Xi_27(3144.8947) = +1.06871649226e-1070, route T at dps 30/60 and the
literal sum at dps 1100 agree. L4: zero of Xi_27 within 8e-29 (dps 30) / 3.9e-37 (dps 60) of z*. L0: mpmath.gammainc =
own continued fraction to 1.1e-37 at 8 points (|Im w| <= 1572). Details: `B-track/NOTE.md`, `B-track/data/ladder*.json`.

### A-track — 16:43 IST 2026-10-03 — k = 1 census final (P1)
Pencil k = 1 on W_1 = [0, 86.55] x [0, 41]: real zeros Xi_1 / Xi_2 in (0, 86.55]: 1 / 7 (Haglund's table: 1 / 7; largest
real zero of Xi_2 39.5324810798, as in the table). Non-real zeros in W_1: Xi_1 15, Xi_2 11; argument-principle counts
(floating point) 31 = 1 + 2*15 and 29 = 7 + 2*11, unchanged at Y = 164. 15 branches followed: 3 land (x = 22.14238,
31.25496, 38.51685 at u = 0.0837, 1.33e-4, 7.03e-7, the three local maxima of S_1 in (0,1)), 11 end at the 11 non-real
zeros of Xi_2, 1 leaves through Re z = 86.55 (from 85.2022 + 35.8750i, at u = 0.004). Im z decreased at every step of
every branch (largest step change -3.7e-7); smallest margin -Im S'/|S'| = 0.719. No local minimum of S_1 in (0,1) on
[0, 86.55]. Agrees with the orchestrator's k = 1 ladder (N2). Files: A-track/data/census_k1.json, A-track/logs/census_k1.log.

## B-track — Q1 k = 1, main run (16:45 IST 2026-10-03; dps-60 and halved-grid re-runs queued)
W_1 = [0, 86.549] x [0, 45]. Xi_1: 1 real + 15 non-real (AP 31 = 1 + 2x15); Xi_2: 7 real + 11 non-real (AP 29).
S_1 = Xi_2/Phi_2 on [0, 98.55]: 3 local maxima in (0,1), no local minimum in (0,1). 15 branches followed by Newton on
the tau-grid 0.1 (to 27.8, then t = 1): 3 land at x* = 22.142378 (tau* 2.48042), 31.254957 (8.92812), 38.516854
(14.16819); 11 end at the 11 non-real zeros of Xi_2 in W_1; 1 exits (85.2022+35.8750i -> 88.6268+27.5501i). Im z
decreased at every grid step of every branch (largest increase -3.3e-8); Im(dz/dt) < 0 at all 3,605 grid values.
NUMERICAL, not interval-rigorous. NOTE.md "Q1, k = 1".

### L-lit — task 1 done (16:45 IST 2026-10-03)
- Citing works found: 16 (Semantic Scholar 12, OpenAlex 8, Google Scholar 8, zbMATH 2, Zenodo, MathOverflow, web), each opened at the citation; table in `L-lit/PRIOR-ART.md` §1.
- **Only Baccaro 2026 touches Conjecture 4 (k = 1, proved).** Ahn 2012 (S6) computes zeros of four fixed members Φ1 + tΦ2, t = 0.1, 0.5, 0.9, 0.95, in [0.01, 250] × [0, 50] (appendix PDF pp. 78–81), checks Conjecture-1-type ordering only, never follows zeros in t and never names Conjecture 4. **Nothing found for k ≥ 2** — no statement, computation or counterexample (null search, sources listed).
- Side finds: Polson 2026 (SSRN 6954119, now withdrawn/under review there) surveys Haglund's conjectures, not Conjecture 4; Baccaro's other preprint (Zenodo 21941655) is about H_N + t·c_N and only names the "next-summand homotopy". Ahn quotes "c1 = 1 and 0 ≤ ci ≤ 1 for i > 1" from [Hag11] — the web copy's wording (§3 item 7), so that copy predates 2012.

### read-O (Opus reader of NOTE.md) — batch 1 (16:46 IST 2026-10-03)
- NOTE hash 57ea9099…913d, 87 lines. §1 Lemmas 1.1–1.3 re-derived ✓; Φ_n = 2∫φ̃_n cos(zv)dv checked off the axis by two routes (gammainc vs quad) to ≤ 1e−24 relative (verify-O/t21_routes.log).
- **Theorem 2.1(e) is false as an "iff"** (FIX-FIRST, cheap): a real zero of F_t of multiplicity m ≥ 3 (a critical point of S_k with S_k″ = 0 and value in (0, 1]) sends a conjugate pair off the axis just after t_0, so (R) and (D) fail there although S_k has no local minimum. Correct form: (R) ⟺ every critical point of S_k on ℝ with value in (0, 1] is a non-degenerate local maximum (S_k″ < 0); range 0 ≤ t < 1. Non-generic, so no census number changes; the A/B real-axis test should still flag |S_k″| tiny at an extremum with value in (0, 1].
- Target (h) reproduced with own code: λ = 0 three maxima (22.14237766: 0.0837083117225; 31.25495663: 1.32607281482e−4; 38.51685382: 7.02802749897e−7), no minimum; λ = 5e−5 minimum at 24.34012104, value 0.611995156161; λ = 1e−4 none (verify-O/t26_control.log).
- Lemma 4.1 holds in 25 tests (n = 2…6, R up to πn² − ½); actual/bound 0.078–0.105; the sup is at z = iR exactly (verify-O/t25_lemma41.log). The five 1/x² limits of the paper and α_n reproduced to every printed digit (t22_consts.log).

### A-track — 16:46 IST 2026-10-03 — k = 2, 3 census final (P1)
k = 2 on [0, 130.53] x [0, 50]: real Xi_2 / Xi_3 = 7 / 15 (Haglund 7 / 15); non-real 23 / 18; 23 branches: 4 land,
18 end at the non-real zeros of Xi_3, 1 exits; Im z decreased at every step (largest step change -3.1e-7); smallest
margin 0.806. k = 3 on [0, 187.08] x [0, 59]: real Xi_3 / Xi_4 = 15 / 31 (Haglund's table prints 32 for N = 4; 31 is odd,
as the program's corollary requires); non-real 35 / 25; 35 branches: 8 land, 25 end, 2 exit; largest step change -3.3e-7;
smallest margin 0.812. All checks passed for both (argument-principle counts, also at 4Y; ends = zeros of Xi_{k+1};
landings = (R_{k+1} - R_k)/2 = local maxima of S_k in (0,1); no local minimum in (0,1)). Files: A-track/data/census_k2.json,
census_k3.json.
