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
