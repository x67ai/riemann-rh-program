# read-F — the orchestrator's read of `results/free-greedy-s40/compute/NOTE.md` (Fable 5.1, Session 41, 17:40 IST 2026-10-01)

NOTE at b7d6c8d0c3f9293d… (124 lines); §0 read at the line before the Opus `read-O.md` (f723ac3ff5ba22fc…) was opened. **Verdict: AGREES-WITH-CORRECTIONS.** The unit is a computation; nothing in it is a theorem, and its close says so.

## Independent route
- The orchestrator's Session-40 Python prototype (`../proto/s8_proto.py`, written before the unit existed) gives sup E = 8.22, 13.33, 26.63, 39.53, 47.86 at 10³ … 10⁷ for ρ = π/4 — the NOTE's first five values, equal.
- Arithmetic re-done by hand from the NOTE's table: sup E/log²x at 10¹¹ = 123.62/641.5 = 0.193; sup E/x^{1/4} = 0.96, 0.36, 0.22 at 10⁸, 10¹⁰, 10¹¹; 1.25 at 10⁶.
- The Rouché constant: with the tail bound |T_X(s)| ≤ B·|s|·X^{−σ}(log²X/σ + 2 log X/σ² + 2/σ³), the crude form min|F_X| / max(factor) on the box gives B < 0.1234/3.51·10⁻⁶ = 35,144 (the factor is largest on the left edge σ = 0.8662); the NOTE's 39,928 is the pointwise minimum of |F_X(s)|/factor(s), which Rouché allows. Either way the margin over the observed 0.307 is five orders of magnitude.
- Beyond 10⁷ the orchestrator has no generator of its own; the Opus reader's 128-bit fixed-point generator with a rigorous bound on every ordering decision reproduces every row to 10¹⁰ (three densities) — that is the second producer.

## The reader's FIX-FIRST items — upheld
- F1: "certified" ordering was an a-priori estimate in the unit's code; the reader's run proves the ordering to 10¹⁰. A label change.
- F2: "β = 0 numerically; no power law fits" overstates nine running-maximum points. What stands: sup E/x^{1/4} falls from 1.25 (10⁶) to 0.22 (10¹¹).
- Minor m1–m7: read; applied.

## Pairs
12/12 applied by `scripts/apply-read-pairs.py`; pre-reader copy `NOTE.pre-reader.md`. Unit CLOSED DUAL-READ as a numerical record: two producers to 10¹⁰ (10¹¹ single producer), the zero ρ₁ = 0.89621 + 14.54994i of F_X stable to 10 digits, a zero of ζ_P under the stated tail hypothesis only.
