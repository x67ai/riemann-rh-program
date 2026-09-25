# SHARED — E1 (M5-U formulation slot, E7 folded in), writer Fable 5.1, Session 28

## Block 1 — §0–§1 landed (Sat Sep 26 01:51:26 IST 2026)
- Brief hash verified 52dc5420…dcc4e. Directory scaffolded (verify/, sources/). Lapidus 1505.01548 fetched to sources/ (SHA-256 85e2e128…). LMFDB pages for the rung-3 pair being fetched (sources/).
- §0: conventions unchanged from D1(b) §0.1; new object: the strip test family g_ψ = (ψ⋆ψ̃)/cosh(u/2) (0.1), which makes H1 hold on the strip.
- §1: sources at the page. Findings that change the record: (a) Yoshida 1992 p. 322 PRINTS "ζ_k's zero set is a uniqueness set for entire functions of exponential type" (D1(b) P3's recalled sentence, now at the page); Yoshida Prop. 7 pp. 322–324 is a printed unique-continuation theorem for the datum side (nearest neighbor of F1(b)). (b) Suzuki JLMS 2023 p. 11 prints −g″ = Ψ″ = W (the Weil distribution is the accelerant of the screw function g = −Ψ); Krein–Langer 2014 Theorem 5.1 (p. 34) is the extension theorem for screw functions with a positive (1+λ²)^{-1}-tempered measure — together they close D1(b) §4.2's gap (H5, §5). (c) Krein–Langer's uniqueness criterion is printed in three forms (p. 29 operator; pp. 29–30 completeness, necessary not sufficient; p. 40 Theorem 6.1 via a_f = ∫det H_f; p. 41 Krein's log-integral sufficient condition for indeterminacy). (d) Bombieri's Theorem 10 is at p. 221 and the trichotomy is the Corollary at p. 224 (the brief's "p. 228" is wrong); the Example p. 224 and Bourgain's remark p. 225 read as the brief expected (ℓ²-complex coefficients; nothing on integer weights). (e) Kaczorowski–Perelli 1999 p. 210 read for I.7. (f) Poltoratski is NOT on disk under c2-m5b (used from the record, dual-model).
- Computations so far (verify/): rung1_ghost_pair.py (1.2 s) — an exact genus-2 ghost pair over F_7 at m = 1 (answers Untried line 2's rung-1 item); rung3_cubic_pair.py — the cyclic cubic pair of conductor 229·367, p₀ = 19; h1_strip_test_check.py running (numerical sanity check of (0.1)).
- Next: §2 the contract theorem.

## Block 2 — §2 landed (Sat Sep 26 01:56:23 IST 2026)
- Clause 1 (H1) PROVED on the STRIP via g_ψ = (ψ⋆ψ̃)/cosh(u/2): the orbit sum is (2π)⁻¹(|ψ̂|² ∗ P_y)(x) with P_y(x) = 2π cosh(πx)cos(πy)/|cosh(π(x−iy))|² > 0 for |y| < ½ (checked to 10 digits); the plain family goes negative off the line (−6·10⁻⁴ at x = 6.5, y = ½) — Weil's mechanism, evaded.
- Clause 2: both parts of a ghost nonzero, infinite, and BALANCED at every scale ≥ 1/L (inequality (2.3)); μ₋ finite ⟹ μ = 0 (via F1(b)); sparse ⟺ sparse. Answers H2's "can μ₋ be sparse".
- Clause 3 (THEOREM, under RH): the real-weighted relaxation ℛ_L(Λ) contains ν_ζ + t·m (m finite real even on ζ's zeros with a gap [−L, L], from G_X = ∞) for every L — Krein INDETERMINATE at every bandwidth; a_g = +∞ for Suzuki's screw function. H4(a) decided NO; "integrality is the whole content".
- Clause 4: the soft-windowed datum at height T is a continuous PD function (Krein–Langer Thm 4.4 applies exactly) and is indeterminate at every (T, L) outside countably many T; integrality is invisible to it linearly. H4(c)'s first obstacle named.
- Clauses 5–7 and the dependency chain (no cycles); H2 restated with (i)–(iv) decided.
- Next: §3 ladder (rung-1 exact pair, rung-3 cyclic cubic pair + LMFDB confirmation, ζ has no partner).

## Block 3 — §3 landed (Sat Sep 26 01:58:45 IST 2026)
- Rung 1: NEW exact ghost pair at m = 1 < g = 2 over F_7 (two actual curves, same N₁ = 1, P differing at t²) — D1(b) Untried line 2's rung-1 item DONE. Every N₁ ∈ {1..15} carries ≥ 2 distinct P(t).
- Rung 3: the cyclic cubic pair of conductor 229·367 (|d| = 7063225849), p₀ = 19; LMFDB fields 3.3.7063225849.1 (K₂) and .2 (K₁) confirm every splitting type at 2..17 (all inert in both) and the first difference at 19. Datum equality argued from Yoshida (1.6) p. 284 (conductor in δ₀, Gamma factors in r₁V₁ + 2r₂V₂). Pair is an exact FREE-stratum ghost (α ≥ ½ only for T ≤ 0.023); it cannot reach the determined stratum.
- ζ has no partner: KP 1999 p. 210 read; ghosts of ζ are not L-function zero sets.
- Stop line (ii) fires (does not stop the slot). Next: §4 the positivity step and the DECISION.

## Block 4 — §4 landed (Sat Sep 26 02:00:01 IST 2026)
- DECISION: STOP at stop line (iii). (a) Krein determinacy REFUTED (indeterminate at every L, §2.3); (b) hard-window Toeplitz rejected (no finite system; leakage is an RvM-size infinite measure); (c) soft-windowed taper REFUTED as a YES-route (indeterminate at every (T, L), §2.4) but RETAINED as the contract's localized form; (d) M2 clause 7 rejected (pairs vs doubles; on-line ghosts); (e) crystalline-measure literature rejected at hypotheses (gap vs discrete spectrum; unit-mass constructions point the other way; [recalled, unverified], SPONSOR-FETCH candidate); (f) the arithmetic shape — first obstacle: the ghost has ζ's prime side by definition, so ζ's arithmetic is exhausted by the class's definition.
- Next: §5 E7 (H5 confirmed; proposed §4.2 correction), §6 zoo protocol + rider on II.1.

## Block 5 — §5–§6 landed (Sat Sep 26 02:01:32 IST 2026)
- H5 CONFIRMED at the page: E7 theorem proved from Krein–Langer 2014 Thm 5.1/Cor 5.2 (p. 34) + Suzuki 2023 Prop 3.1 (p. 10) and −g″ = Ψ″ = W (p. 11); the mollifier-limit gap is bypassed (the λ⁻² of the screw representation absorbs the divergent mass). Proposed §4.2 CORRECTION paragraph written in exact words (§5.2). C2 Untried line 3 leaves into this file.
- §6: zoo §0 items 1–7 run; proposed rider on II.1 in exact words; no Group-IV block.
- Next: §7 close, §8 C2 lines, §9 honesty + lint, closing hashes.

## Block 6 — §7–§9 landed; CLOSED (Sat Sep 26 02:04:27 IST 2026)
- §7: verdict table (H1 CONFIRMED+strengthened; H2 CONFIRMED as restated, 3 sub-clauses decided; H3 CONFIRMED with 2 precisions; H4 DECIDED — STOP at (iii), (a) and (c) refuted by theorem; H5 CONFIRMED at the page). The three 10(c) closes written; 10(m) labels; 10(o): 0 slots wasted; record corrections (Bombieri Thm 10 at p. 221, trichotomy = Corollary p. 224; Poltoratski not under c2-m5b; KL files in fetched-r2; r-22a irrelevant).
- §8: three Instruments rows; Untried lines 1–2 updated, line 3 LEFT into this file; work-log line; frontier sentence. §9: honesty + lint (banned words only inside the Lapidus quotation).
- Lint grep at close: only line 54 (verbatim Lapidus quote) and the lint sentence itself.
- FINAL HASHES: FORMULATION.md 7d7d00726e20c6876a44d5540d055614159e0041a4320056f2a559b245e40343; scripts and logs in verify/hashes.txt (rung1_ghost_pair.py c16d03bb…, rung3_cubic_pair.py abc963b5…, h1_strip_test_check.py 32bdab98…); sources: lapidus 85e2e128…, LMFDB .1 b54339d3…, .2 eb056078….
- Reader's hardest checks: (1) §2.1 identity (2.2) and the strip positivity (the whole of clause 1 rests on it); (2) §2.3(b)'s use of G_X = ∞ (record, RH) and the symmetrization steps; (3) §3.3(a) datum equality via Yoshida (1.6) — the conductor in δ₀ only; (4) §5.1 step (2), the passage from mean-zero smooth tests to Krein–Langer's kernel-PD definition; (5) §4's dismissals, adversarially.
- Files present: FORMULATION.md (no read-O.md yet) → launch the reader.

## Block 7 — the Opus READ landed (reader Opus 5; Sat Sep 26 02:22:35 IST 2026)
- Deliverable: `results/e1-m5u/read-O.md` (SHA-256 in `verify-O/hashes-O.txt`; fdd5031a17638432… at write). Inputs recomputed: BRIEF 52dc5420…dcc4e, FORMULATION 7d7d0072…0343 (both match).
- §P (written before FORMULATION §1 was opened): no printed uniqueness/non-uniqueness theorem for positive INTEGER-atomic measures with a spectral gap found; the real-weighted question is printed for FINITE positive measures — Mitkovski–Poltoratski "Determinacy for measures" (Thm 1.2 Riesz-type criterion; p. 2 "every non-zero measure σ with a spectral gap (−a, a) gives rise to two a-indeterminate measures"; Thm 1.5 Det(X) = G(X); Thm 1.6–1.7 alternation) — missing from the writer's §1 (A7). Sources saved under `sources-O/` (MP, Poltoratski 0908.2079, Lev–Reti 2101.04092, Limani 2604.24900, LMFDB .1/.2).
- Verdicts: §1 FIX-FIRST; clause 1/(2.2) CLOSES (re-run, `verify-O/h1_strip_reader_run.log`); clause 2 FIX-FIRST (ε ≤ 1 missing); §2.3(b) Krein indeterminacy CLOSES — NOT refuted, holds exactly (a short corollary of Bombieri p. 225 + Poltoratski Thm 2 + MP p. 2; not found printed for ζ); §2.4 CLOSES; rung 1 CLOSES (independent recount); rung-3 datum equality CLOSES at Yoshida p. 284; LMFDB transcription FIX-FIRST (class number of .1 is 3, not 12; rows agree at 29, 43–59); p₀ = 19 confirmed three ways; §4 CLOSES with an added candidate (g) (MP oscillation theory — rejected at its first obstacle); §5 CLOSES (step (2) re-derived; §5.2 exact); rider FIX-FIRST (4 word edits); C2 lines FIX-FIRST (2 edits); labels row by row.
- Page errors found: Bombieri p. 224 Corollary prints ℜ(ρ) ≠ ½ (writer quoted "= ½"); the A + Bx⁻¹ trichotomy is the Introduction, p. 185; Krein–Langer's a_f carries √det (p. 40); Yoshida Theorem 1's bound is 0 (p. 310); KP is in fetched-r2/.
- 27 amendments (A1–A28, A18 unused), exact OLD/NEW; none touches the decision. DECISION: STOP at stop line (iii) STANDS. Group-IV: none. Rider on II.1 earns [dual-model check 2026-09-26] with A19–A22.
- Scripts (one process each, all < 2 s): verify-O/rung3_check.py, rung1_pair_check.py (first run had a reader bug — N₁ counted over F₄₉ — fixed and logged), h1_strip_reader.py; writer's rung1/rung3 scripts re-run: identical output; writer's verify/hashes.txt re-verified.
- Nothing committed; FORMULATION.md, zoo, directions/, STATUS.md, LOG.md untouched.
