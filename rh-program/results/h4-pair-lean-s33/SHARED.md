# H4 — SHARED log (builder Fable 5.1, then checker Opus 5); Session 33, 2026-09-29

Unit brief `results/h4-pair-typing-s32/UNIT-BRIEF.md` SHA-256 `2d80f9db8ccf04765840b041189dc771813f5fdbb77767c40d471e8b9908cb94`. Every block dated by `date`. Nothing about ζ or RH
follows from anything in this unit.

## [builder] Tue Sep 29 11:21:44 IST 2026 — deliverable 1 landed: `PREDERIVATION-ERRATA.md` (+ `tools/h4_numbers.py`, `tools/h4_numbers.log`)
Verdict: the note's §2–§4 derivations are correct in substance; every anchor number reproduces (ā(1/4) = 1.10944370, ā(1/2) =
1.48140550, F1 − S2 = −0.0352002534 by closed form AND by the integer-frequency row; the reduced row gives −0.0144817; power sums
22880 / 14492192 / 10924353440 / 8964042662432; certified bound −0.033682 with L(3.141592) = 1.1060211, U(3.141593) = 1.4815182,
margin spent 0.001518; (MI) holds at the anchor, F1 − T = +3.67). Errata: E7 (the note's dyadic bracket 3294198/2²⁰ < π does not
follow from pi_gt_d6 — unused here), E5 (0.021 is an upper estimate of the per-cosh error at π/4, the value is 0.0162), E9 (the
Cauchy–Schwarz name is `sq_sum_le_card_mul_sum_sq`, Chebyshev.lean 136), E1/E10 design routes. No stop line fires.
SHA-256 `PREDERIVATION-ERRATA.md` = fb2a0683a8afef858c7f350d5cac26c729cf67dff341db765acb0c8fc99e154d.
Next: rung 1 — `lean/Zeta23/PairCeiling/PairRow.lean` items 1–4 (W2_eq, sum_W2_mul, pairRow_eq_gridRowQ, sum_W2_cosh), mirrored
to `~/rh-lean-work/checker-clone-s21`, `lake build Zeta23.PairCeiling.PairRow`, `rung1-print-axioms.log`.
