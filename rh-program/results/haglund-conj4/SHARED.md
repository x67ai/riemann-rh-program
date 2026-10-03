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

### A-track — 16:52 IST 2026-10-03 — P1 k = 4, 5 and P2 k = 26 final
P1 k = 4 ([0, 256.19] x [0, 68]): real Xi_4 / Xi_5 = 31 / 53; non-real 47 / 34; 47 branches: 11 land, 34 end, 2 exit;
largest step change of Im z -3.2e-7; smallest margin 0.797. P1 k = 5 ([0, 337.88] x [0, 79]): real 53 / 79 (Haglund
53 / 79); non-real 63 / 47; 63 branches: 13 land, 47 end, 3 exit; -3.0e-7; 0.828. All checks passed.
P2 k = 26, window [2876, 3176] x [0, 69]: real Xi_26 / Xi_27 = 45 / 263; non-real 133 / 17; 133 branches: 109 land
(= (263-45)/2 = the 109 local maxima of S_26 in (0,1)), 17 end at the 17 non-real zeros of Xi_27 in the window, 7 exit;
no local minimum of S_26 in (0,1); Im z decreased at every step (largest step change -3.0e-7), smallest margin 0.868.
Site: the certified zero 3143.2206824215 + 0.3152587994i of Xi_27 is the u = 0 end of the branch from the zero
3130.2619 + 52.4297i of Xi_26 (descending throughout, margin >= 0.970); the neighbor from 3132.1660 + 52.9056i lands at
x* = 3145.2290390 at u* = 3.3e-76 and produces the real zeros 3144.89466 and 3145.59985 of Xi_27. File:
A-track/data/frontier_k26.json.

### A-track — 16:55 IST 2026-10-03 — P1 k = 6 final (P1 for k = 1..6 complete)
k = 6 on [0, 432.12] x [0, 90]: real Xi_6 / Xi_7 = 79 / 113 (Haglund 79 / 113); non-real 82 / 62; 82 branches: 17 land
(= (113-79)/2), 62 end at the 62 non-real zeros of Xi_7 in W_6, 3 leave through Re z = 432.12 (one of them reaches its
zero of Xi_7 at 432.1548 + 63.0618i, just outside); Im z decreased at every step (largest step change -3.0e-7);
smallest margin 0.832; no local minimum of S_6 in (0,1) on [0, 432.12]; routes L and T agree to 2.6e-13 (relative) at
410 points. Over k = 1..6 the real counts reproduce Haglund's table except N = 4, where the census gives 31 (odd).

### L-lit — task 4 done (16:57 IST 2026-10-03)
- **Im f′/f < 0 above the axis, in print:** Titchmarsh, *The Theory of Functions* (2nd ed. 1939) §8.52, p. 266 — real entire f of order < 2 (or order 2, genus 1) with only real zeros: Im f′/f = −y{k/(x² + y²) + Σ 1/((x − z_n)² + y²)}. For ξ in the s-variable: Matiyasevich–Saidak–Zvengrowski (arXiv:1205.2773) pp. 4–5, citing Lagarias 1999 and Hinkkanen 1997.
- **Unconditional for Ξ above height ½** (useful for the charter's step 2): Csordas–Smith, Michigan Math. J. 47 (2000), p. 604, (2.5): Im f′/f < 0 for Im z > A when f ∈ S∞(A) (even, real, zeros in |Im z| ≤ A, not of exponential type). Ξ ∈ S∞(½) without RH (hypotheses checked against their Definition 1.2), so Im Ξ′/Ξ < 0 for Im z > ½ unconditionally. Only the band 0 < Im z ≤ ½ needs RH.
- **The f(z) = c consequence, in print in one form:** Csordas–Smith 2000, pp. 608–609, (3.3)–(3.4). Level curves are parametrized by e^{iθ}f(z(s)) = is (θ = π/2 gives f(z(s)) = s, i.e. the solutions of f = c); z′(s)·(f′/f) = 1/s, and "tangents are never horizontal" above height A. The direction (descent as |c| decreases) and "real solutions stay real" are not stated there. Each follows in one line (`PRIOR-ART.md` §4(b)), the second from the Laguerre inequality, which is in print (Titchmarsh p. 266).
- NOT REACHED: Levin, *Distribution of Zeros* (archive.org lending only, search-inside refused); Csordas–Smith–Varga, Analysis 12 (1992) 377–402 (paywalled, €30; only the abstract was read: "level set structure … application to the Riemann Hypothesis").

### A-track — 16:58 IST 2026-10-03 — P2 k = 27 final (the continuation of the Conjecture-1 site)
Window [3096, 3404] x [0, 70]: real Xi_27 / Xi_28 = 48 / 276; non-real 137 / 16; 137 branches: 114 land (= (276-48)/2
= the local maxima of S_27 in (0,1)), 16 end at the non-real zeros of Xi_28 in the window, 7 exit; no local minimum of
S_27 in (0,1); Im z decreased at every step (largest step change -3.0e-7), smallest margin 0.851; all checks passed.
The certified zero 3143.2206824215 + 0.3152587994i of Xi_27 lands, in pencil 27, at x* = 3143.2466268840, u* = 0.41051
(t = 0.58949), margin >= 0.993, and becomes the real zeros 3142.979457, 3143.567499 of Xi_28. The real zeros of Xi_27 at
3144.8946622 and 3145.5998496 stay real throughout and end at 3144.490488 and 3146.283528. File: A-track/data/frontier_k27.json.

## B-track — Q1 k = 2, main run (16:58 IST 2026-10-03; re-runs queued)
W_2 = [0, 130.531] x [0, 45]. Xi_2: 7 real + 23 non-real (AP 53); Xi_3: 15 real + 18 non-real (AP 51). S_2 on
[0, 142.5]: 4 local maxima in (0,1), no local minimum in (0,1). 23 branches: 4 land at x* = 44.560600 (tau* 3.24730),
50.852817 (8.29249), 57.272541 (13.06910), 62.128208 (15.97922); 18 end at the 18 non-real zeros of Xi_3 in W_2;
1 exits (129.2369+44.1967i -> 133.7312+32.7765i). Im z decreased at every grid step (largest increase -7.9e-8);
Im(dz/dt) < 0 at all 6,886 grid values. NUMERICAL.

### L-lit — closed (16:59 IST 2026-10-03)
- `L-lit/PRIOR-ART.md` complete: §0 (summary + LEDGER/TOOL rows + ASKED/DELIVERED), §3, §2, §1, §4, NOT REACHED. The check script `L-lit/check_task3.py` and its log are beside it. Third-party files are under `lit/`, all git-ignored (a tracked README rule, .gitignore l. 129, would have caught `lit/gh-baccaro/README.md.txt`; it was renamed before any commit).

### read-O — batch 2 (17:01 IST 2026-10-03)
- Pairs written in read-O.md §4–§5: FIX-FIRST F1 (Theorem 2.1(d)/(e), Remark 2.2: multiplicity ≥ 3 breaks (R) and (D); range 0 ≤ t < 1, values (0, 1]), F2 (Proposition 3.2: the single critical point per lobe and Ξ → ∞ along C_m are used but not proved; both supplied), F3 (the "Reading", l. 79: "tied … from both sides" is stronger than Proposition 4.2 + a frozen-level model); 12 minor. 18 pairs in all.
- §5(II) of the NOTE: the rise of |Ξ| = |L_t| goes with log(x/2π) (∂_y log|Ξ| = 1.9330 at (300, 10) against ½log(x/2π) = 1.9330 and ½log(x/2) = 2.5053), not log(x/2) (minor m7).
- Proposition 4.2's mechanism checked on the control f = Ξ + 5e−5: zero β = 28.6324463545442 + 8.52426881931311i, Im f′(β) > 0, and for k = 2…8 the pencil zero within 1e−6 of β has d(Im z)/dt > 0 at t = 0, ½, 1 (verify-O/t27_prop42_control.log). The rise is e^{−π(k+1)²}-small; its sign is what a census reads.

### A-track — 17:03 IST 2026-10-03 — P3 (real-axis test) k = 1..20 final
For every k = 1..20, on [0, 4(k+2)^2 + 40]: S_k has no local minimum with value in (0,1) (grid spacing/20, frontier part
rescanned at spacing/40 with identical results; every (0,1)-interval has the extrema its end types require); the number
of local maxima in (0,1) equals (R_{k+1} - R_k)/2 in every case; S_k(0) > 1 and S_k(end) < 0. The largest real zeros
of Xi_{k+1} reproduce Haglund's table for N = 2..10 to the printed 10 digits. Real counts R_N, N = 1..21: 1, 7, 15, 31, 53,
79, 113, 155, 207, 263, 327, 401, 483, 575, 673, 781, 899, 1027, ..., (files A-track/data/p3_k<k>.json). NUMERICAL.

### read-O — CLOSED (17:05 IST 2026-10-03)
- VERDICT: AGREES-WITH-CORRECTIONS on NOTE.md (hash 57ea9099…913d). 18 pairs: FIX-FIRST F1 (Theorem 2.1(d)/(e), Remark 2.2), F2 (Proposition 3.2 proof, two steps), F3 (the "Reading", l. 79); minor m1–m12. Every OLD quote checked as an exact substring of its NOTE line by script.
- ✓ at the line: Lemmas 1.1–1.3, Theorem 2.1(a)–(d), Proposition 2.3, Lemma 3.1, Lemma 4.1, Proposition 4.2, the PROVED items of §5. Prop. 3.2 (i) ✓, (ii)/(iii) GAP with fixes. Theorem 2.1(e) FALSE as an iff.
- Novelty: Theorem 2.1 new as a statement on a printed core (the paper's sandwich/tail/odd; Baccaro 2026 PDF pp. 3–4 for k = 1, and per L-lit his all-k record); Proposition 4.2 new in the sources reached (S1, S3, S5 at the page, on-disk grep, three arXiv queries, L-lit's census).
- For A/B: the real-axis test of (R) should also flag extrema of S_k with value in (0, 1] at which |S_k″| is small (F1's degenerate case); and strict descent everywhere in a window gives (R) there too (Baccaro's Lemma 4.3 argument, any k; read-O §7 A4).

### A-track — 17:06 IST 2026-10-03 — correction and positive controls
- Correction: the smallest margin for P1 k = 1 is 0.708 (at the start 20.6253 + 2.6972i), not 0.719 as posted at 16:43:
  the first tracer did not evaluate the margin at the start and end nodes; fixed, and all finished files re-summarized
  (no other table entry changes at 3 digits; A-track/NOTE.md §2 T4).
- Positive controls (pencil on Xi + 5e-5): the A-track axis scan finds the local minimum at 24.34012104 with value
  0.6119951561613 (read-O: 0.611995156161), and the A-track tracer gives margin -0.87 / -0.83 / -0.81 / -0.81 at the zero
  near beta = 28.6324 + 8.5243i for k = 2 / 3 / 5 / 8 (step increase +8.4e-7 at k = 2). Both detectors fire. §2 T5.

## B-track — Q1 k = 3, main run (17:24 IST 2026-10-03; re-runs queued)
W_3 = [0, 187.080] x [0, 60]. Xi_3: 15 real + 35 non-real (AP 85); Xi_4: 31 real (not 32) + 25 non-real (AP 81).
S_3 on [0, 199.1]: 8 local maxima in (0,1), no local minimum in (0,1). 35 branches: 8 land at x* = 67.930995 (tau*
0.22526), 73.067283 (3.31630), 78.002167 (7.89953), 83.534272 (12.12625), 87.983898 (15.96853), 93.140202 (19.20114),
96.958744 (21.52466), 102.069222 (25.82349); 25 end at the 25 non-real zeros of Xi_4 in W_3; 2 exit through Re = X_3.
Im z decreased at every grid step (largest increase -1.07e-7); Im(dz/dt) < 0 at all 11,974 grid values. NUMERICAL.

### A-track — 17:37 IST 2026-10-03 — P3 complete (k = 1..50) and P2 k = 15
P3: for every k = 1..50, on [0, 4(k+2)^2 + 40], S_k has no local minimum with value in (0,1); its 5558 local maxima with
value in (0,1) (in total) are all non-degenerate (S_k'' < 0; nu = -S''(x*) spacing^2/u* >= 3.09); #max = (R_{k+1}-R_k)/2
for every k; every maximal (0,1)-interval is consistent; S_k(0) > 1 and S_k(end) < 0; the frontier rescan at double
resolution agrees for every k (k = 41, 44 after a rounding fix in the comparison, logs/diag_rescan_k41/44.log). Real
counts R_N (N = 1..51) are odd and agree between consecutive scans: 1, 7, 15, 31, 53, 79, 113, 155, 207, 263, 327, 401,
..., 10155, 10629, 11117. Landings of pencil k lie in [4(k+1)^2, 4(k+2)^2 + 9] for k = 1, 5, 10, 20, 27, 49, 50.
P2 k = 15, window [984, 1196] x [0, 55]: real 37 / 145; non-real 74 / 16; 74 branches: 54 land, 16 end, 4 exit; Im z
decreased at every step (-3.0e-7), smallest margin 0.880; all checks passed. NUMERICAL. Files: A-track/data/p3_k*.json,
nondeg_k*.json, frontier_k15.json.

### A-track — 17:39 IST 2026-10-03 — P1 k = 7 and P2 k = 20 final
P1 k = 7 on [0, 538.94] x [0, 102]: real Xi_7 / Xi_8 = 113 / 155 (Haglund 113 / 155); non-real 103 / 80; 103 branches:
21 land, 80 end at the non-real zeros of Xi_8 in W_7, 2 exit; Im z decreased at every step (-3.1e-7); smallest margin
0.842; all checks passed. P2 k = 20, window [1724, 1976] x [0, 61]: real 40 / 196; non-real 101 / 17; 101 branches: 78
land, 17 end, 6 exit; -3.0e-7; 0.876; all checks passed. NUMERICAL. Files: A-track/data/census_k7.json, frontier_k20.json.

### A-track — 17:48 IST 2026-10-03 — P1 k = 8 and P2 k = 35 final
P1 k = 8 on [0, 658.32] x [0, 115]: real Xi_8 / Xi_9 = 155 / 207 (Haglund 155 / 207); non-real 127 / 98; 127 branches:
26 land, 98 end, 3 exit; Im z decreased at every step (-3.0e-7); smallest margin 0.850; all checks passed.
P2 k = 35, window [5144, 5516] x [0, 80]: real 53 / 363; non-real 182 / 19; 182 branches: 155 land, 19 end, 8 exit;
-3.0e-7; 0.876; all checks passed. NUMERICAL. Files: A-track/data/census_k8.json, frontier_k35.json.

### v2-check (second model) — 17:50 IST 2026-10-03 — integrity diff and the new sentences at the page
Own diff of v2/main.tex against ../main.tex: 14 hunks, 32 old / 49 new lines, byte-identical to the diff in
v2/CHANGES.md (which says "82 changed lines"; it is 81). Every hunk is in a listed span; no theorem, proof,
constant or formula touched. Every new sentence about W / V / J checked at the page: table, quotation, page
numbers, date, read date, URL TRUE. Open point found: J (the journal) was published online 2011-02-18, nine days
after W's date, so "the later copy" (v2 l.472) is not right against J. Details: arxiv/haglund-counterexample/
v2/INTEGRITY-DIFF.md (A.1, A.2).

### WRITER (note "On Haglund's Conjecture 4 ...") — 17:50 IST 2026-10-03 — started
Read: WRITER-BRIEF, BRIEF-WARNINGS, arxiv/README, KICKSTART item 17, NOTE.md (all), A-track/NOTE.md §0 (P1 k=1..7, P2 k=15,20,26,27, P3 k=1..50),
B-track/NOTE.md (§0 table still has NO rows; Q1 k=1,2,3 "main run finished" — used as B's final values), L-lit/PRIOR-ART.md §1-§4,
the v2 template, ORCH-NOTES N4-N6 (only for the wording of the far-field check that NOTE §6 cites). Writing main.tex section by section in
results/arxiv/haglund-conj4-note/. Gaps and wording choices go to WRITER-NOTES.md there.

### v2-check (second model) — 17:54 IST 2026-10-03 — Part A verdict
CLEAN-WITH-CORRECTIONS. F1: v2 l.472 "the later copy" -> "the author's web copy" (journal online 2011-02-18,
after W's 2011-02-09). F2: [Hag09] "Page and equation numbers in this paper refer to this version" now has
[HagW] exceptions. F3 (recommended): l.475-477 "ten-digit values ... cannot resolve" reads as a diagnosis of an
error W already removed; W's 13 digits do not resolve the N = 3 sum either (-2.2e-15 vs -7.0e-17). F6: PDF
outline has "Proof of Theorem ??" (v1 too; needs one more pdflatex pass or \texorpdfstring). F7: CHANGES.md
says §1.3/§1.5 for what the PDF numbers §1.4/§1.7. Now on Part B (the letter, ten statements).

### WRITER — 17:54 IST 2026-10-03 — §1 and §2 of the note drafted
main.tex: front matter (template footnote verbatim), abstract (draft), §1 (Haglund's p. 11 lead-in and Conjecture 4 quoted from
arXiv v1; (D), (R)), §1.2 (items by kind), §2 (NOTE Lemmas 1.1-1.3, Theorem 2.1 as corrected, Remark 2.2, Proposition 2.3 and the
paragraph after it, re-typed). No gap met so far. Next: §3 (frozen level, short proof), §4, §5 census, §6 heuristics, §7 prior work.

### v2-check (second model) — 18:00 IST 2026-10-03 — Part B (the letter, statements by number) done
TRUE AS WRITTEN: 1, 2, 3, 4, 6 (as a numerical report), 7, 8 (classical: Titchmarsh §8.52; Csordas-Smith 2000),
9 (hypotheses match Proposition 4.2 exactly), 10. NEEDS A WORD: 5 — 535 = 15+23+35+47+63+82+133+137 is right,
but the zeros lie in eight windows (one per k), and 26 of the 535 branches left their window (A stops at the
edge; B followed its 4 exits for k <= 3 to t = 1), so "from 0 to 1" needs "until it landed, reached t = 1, or
left the window". Record lag: NOTE §6 and ledger L-007 still say the real-axis test covers k <= 20; A's P3 now
covers k = 1..50 (all PASS), which is what supports statement 6 at k = 26, 27. FALSE: none.

### WRITER — 18:01 IST 2026-10-03 — full draft of the note compiles (11 pp.; trimming to <= 9)
§3 (Lemma 3.1 Titchmarsh, Prop. 3.2 "in substance" Csordas-Smith, short proof), §4 (Lemma 4.1, consequences, Prop. 4.2, Remarks 1-4,
the corrected "Reading"), §5 (one table built mechanically from A-track/NOTE.md §0-P1/P2 by a scratch script — rows k = 1..8 and
15, 20, 26, 27, 35, 50 are final there now; B on k = 1, 2, 3 from its Q1 sections; R_N for N = 1..51 from §0-P3), §6 (three regimes,
Lemma 6.1 = the proved sign/monotonicity of c(t)), §7 prior work, code URL, bibliography. No gap met.

### A-track — 18:04 IST 2026-10-03 — P1 k = 9 and P2 k = 50 final; routes L/T at the site
P1 k = 9 on [0, 790.27] x [0, 130]: real Xi_9 / Xi_10 = 207 / 263 (Haglund 207 / 263); non-real 153 / 122; 153
branches: 28 land, 122 end, 3 exit; Im z decreased at every step (-3.0e-7); smallest margin 0.861; all checks passed.
P2 k = 50, window [10364, 10856] x [0, 99]: real Xi_50 / Xi_51 = 58 / 546; non-real 274 / 19; 274 branches: 244 land
(= (546-58)/2), 19 end, 11 exit; -3.0e-7; 0.857; all checks passed. P2 is complete for k = 15, 20, 26, 27, 35, 50:
901 branches, 754 landings, no step with Im z increasing, smallest margin 0.851 (k = 27).
Site cross-check: S by route T and by the literal sum (up to 6592 bits) agree to <= 1.7e-14 (balls overlapping) at 15
points of the three site branches (A-track/data/site_routes_LT.json). NUMERICAL.

### WRITER — 18:10 IST 2026-10-03 — note at 9 pp. after compression; proofreading next
Cuts made to reach 9 pp. (no statement, proof step or number of the NOTE dropped from §2-§4): displays inlined, Remark 2.2 folded
into §5's real-axis paragraph, the NOTE's closing "Conjecture 1 ... unrelated" sentence and "What is NOT in this note" line dropped
(§1.2 states once that neither (D) nor (R) is proved for any k), FLINT bib entry dropped (Arb cited), enumitem compact lists.

### WRITER — 18:13 IST 2026-10-03 — checker ALL CHECKS PASSED (9 pp.); census table re-read
NOTE.md re-read at its 18:04 state (1122 branches; 5558 non-degenerate maxima for k <= 50). A-track/NOTE.md re-read 18:03: P1 now
k = 1..9 (k = 9 final), P2 k = 15, 20, 26, 27, 35, 50; all in the paper's table (programs: A; A and B for k = 1, 2, 3). B-track/NOTE.md
unchanged since 17:24 (§0 table still empty; Q1 k = 1, 2, 3 final). abstract.txt written. Final re-read of both unit NOTEs before the last build.

### WRITER — 18:15 IST 2026-10-03 — note delivered (9 pp.; checker: ALL CHECKS PASSED)
results/arxiv/haglund-conj4-note/: main.tex, main.pdf (9 pp.), abstract.txt, WRITER-NOTES.md (W1-W21: wording choices and number
provenance; no gap met). Unit NOTEs re-read just before the last build (A-track 18:03: P1 k = 1..9, P2 k = 15, 20, 26, 27, 35, 50,
P3 k = 1..50; B-track 17:24: Q1 k = 1, 2, 3; NOTE.md 18:04). Rows added to A-track after 18:03 are not in the paper: the table is
regenerated mechanically from A-track/NOTE.md §0 (the scratch extraction keeps the row format), then the abstract's "k <= 9" and the
readings sentence (1122 + column B) need the same update; a new P1 row may push the paper to 10 pp.

### REFEREE (second model, haglund-conj4-note) — 18:21 IST 2026-10-03 — batch 1: §2 re-derived
REFEREE-REPORT.md started (plan; outside read of main.pdf). Lemmas 2.1–2.3, Theorem 2.4 (corrected form: non-degenerate maxima,
values in (0,1]) and Proposition 2.5 re-derived step by step: no step lost, no hypothesis dropped. Recomputed Ξ(0) = 0.49712,
Q_1(0) = 1.71740e-4 ≤ c_1 = 1.71806e-4 (mpmath). One cosmetic point so far (Lemma 2.1, "x ≠ 0 ... first positive"). Next: §3, §4, Lemma 6.1.
