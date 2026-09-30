# SHARED — seed N4 `tournament` (novel-approach wave, Session 36)

Agent: Opus 5.5 (subagent), 2026-09-30. Charter: `results/novel-wave-s36/WAVE-CHARTER.md` (read in full).

## 2026-09-30 block 1 — reading done, folder created

- Read: charter (full); STATUS.md lines 72–103 (hard constraints; S1–S5); BARRIER-ZOO.md §0 and the STATEMENT lines of I.1–I.8, II.1–II.5, III.1–III.21, IV.1–IV.19, V.4–V.5 (riders not read); `results/d4-infty-s36/BRIEF.md` §2 (Proposition N = the degree clause; Theorem S; Proposition B = regrading of the primes as a formal curve over F_2; Proposition A; Proposition C = the distributional cell is Weil's criterion with multiplier 1).
- Tools located: `results/ccm-dh-test/dh.py` (f_dh, xi_dh, find_zero; off-line zero near 0.808517 + 85.699348i); arXiv search pattern `results/beta-shapes-s35/verify/arxiv_search.sh`.
- Next: generate the 30+ candidate list (NOTE §1), verify the F_{a,q} control first (charter rule 2 says "verify it before use").

## 2026-09-30 block 2 — F_{a,q} control verified (`verify/faq_control.py` → `faq_control.log`)

- FE: q^s·π^{−s/2}Γ(s/2)ζ(s)P(s), P(s) = 1 + a q^{−s} + q^{1−2s}, is symmetric under s → 1−s (derived: P(1−s) = q^{2s−1}P(s); rel. err ≤ 1.2e-30 at 3 points × 4 parameter pairs).
- Zeros of P: u = q^{−s} real negative, u₁u₂ = 1/q, so σ₁ + σ₂ = 1, σ ≠ ½ whenever a > 2√q. Examples: (a,q) = (3,2): σ = 1 and 0 (ON the 1-line, a Re s = 1 zero!); (5,5): σ = 0.79899; (2.9,2): 0.82388; (4.5,5): 0.56932. Height Im s = π/log q (and its translates by 2π/log q): 4.5324 for q = 2, 1.9520 for q = 5 — the control's off-line zeros are LOW and infinitely many (periodic in t), so every test sees them at height ≤ 5.
- Where it breaks the axioms: Dirichlet coefficients c_n = 1 + a[q|n] + q[q²|n] ≥ 0 and a product over primes exist, but the local factor at q is (1 + a u + q u²)/(1 − u) = (1−αu)(1−βu)/(1−u) with α,β < 0 real, |β| > √q (Ramanujan fails at q) and Λ_F(q²) = log q·(1 − α² − β²) < 0 (e.g. −4 log 2 at (3,2)): Λ_F ≥ 0 fails; the local factor is a POLYNOMIAL numerator, not an inverse polynomial. It passes any test that uses only c_n ≥ 0, FE, and a product over primes.
