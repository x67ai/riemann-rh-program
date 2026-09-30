# SHARED — seed N2 `staircase` (novel-approach wave, Session 36)

Dated blocks, appended after every unit of work. Agent: Opus 5.5 (seed N2). Charter: `../WAVE-CHARTER.md`.

## 2026-09-30 17:50 IST — unit 0: start

- Read: the charter in full; STATUS.md lines 72–103 (hard constraints, S1–S5); BARRIER-ZOO.md §0, I.1, IV.1, IV.9.
- Folder created: `results/novel-wave-s36/staircase/` with `verify/` (scripts + logs) and `lit/` (prior art on disk).
- Plan, in order: (1) verify the C1 identity to high precision at complex s; (2) prior art (Haglund; Ki; Lagarias–Suzuki; Hermite–Biehler + zeta; is the prime chain C2 in print) — delegated to a literature sub-agent writing only into `lit/`; (3) cancellation-free evaluator for the approximants; (4) complete zero census by the argument principle on rectangles + Newton; (5) invariant hunt; (6) controls (Davenport–Heilbronn chain, F_{a,q} chain, L(s, χ₄)); (7) rigorous pieces (mpmath.iv); (8) NOTE.md.
- Pre-computation analysis (to be verified, not yet load-bearing): on the critical line, for fixed N, the C1 approximant ξ_N(s) := ½ + ½ s(s−1) Σ_{n≤N} g_n(s) should tend to the constant c_N = ½ + Σ_{n≤N} (1 − 4πn²) e^{−πn²} > 0 as |t| → ∞ (the γ(a, x) expansion of each incomplete gamma), while ξ_N grows like Γ(s/2) along the real axis. If both hold, every ξ_N has only finitely many zeros on the line and infinitely many off it, and "all zeros of every C1 member are real" is false for every N. The height where zeros should start leaving the line is estimated at t ≈ 4(N+1)². Checked numerically below before anything rests on it.

## 2026-09-30 18:05 IST — unit 1: the C1 identity verified (verify/c1_identity.py, .log)

- Λ(s) = π^{−s/2}Γ(s/2)ζ(s) = −1/s − 1/(1−s) + Σ_{n≥1} g_n(s), g_n as in the charter (upper incomplete gamma): relative error 1e−61 … 4e−60 at 60 digits and 1e−91 … 7e−90 at 90 digits, at s = 2+3i, 0.3+7i, −1.5+2i, 5−11i, 12+25i (off the line), 0.8+30i, −7.25+40.5i; on the line (s = ½+14.1347i, ½+60i) the series loses ~27 and ~21 digits to cancellation (Λ is 1e−27 and 1e−21 there) and still agrees to 38 and 45 digits. The two precisions agree with each other to the lower one. mpmath.gammainc checked against direct quadrature at a = 0.25+7i, x = π: 5.6e−42. **The seed's formula is correct; no erratum on the identity.**
- The constants c_N = ½ + Σ_{n≤N}(1 − 4πn²)e^{−πn²} = Σ_{n>N}(4πn² − 1)e^{−πn²} (the two forms agree to 20 digits for N ≤ 4, which is the theta identity 4ψ′(1) + ψ(1) = −½): c₁ = 1.7180566258547875025e−4, c₂ = 5.891258854396012012e−11, c₃ = 2.9589851955455663928e−20, c₄ = 2.434200904905601706e−32, c₅ = 3.44351962408264896e−47, c₆ = 8.595254198824244e−65, c₇ = 3.843818345749113e−85, c₈ = 3.110164390253682e−108. All strictly positive.
