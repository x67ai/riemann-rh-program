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

## 2026-09-30 18:25 IST — unit 2: evaluator validated; first look at the critical line (verify/stair.py, test_stair.log, explore_line.log)

- `stair.py`: general theta-chain class (ζ; F_{a,q}; Davenport–Heilbronn; L(s, χ₄)); members E_w = full − tail (cancellation-free) and the direct truncated sum. Tail vs direct (160 digits) agree to 1e−41 at dps 40 for N = 1, 2, 3, 6 at six complex points up to t = 190.7. Each control's FULL theta split (all k) matches its independently computed completed function to ≤ 1.4e−49 (ζ, χ₄, DH via Hurwitz ζ as in `ccm-dh-test/dh.py`, F_{a,q} for three (a, q)) — the normalizations and modular relations are right. Chain members satisfy E(1−s) = E(s) and are real on the line to 1e−40.
- F_{a,q} control verified: zeros of q^s + a + q^{1−s} at s = ½ ± arccosh(a/2√q)/ln q + iπ(2j+1)/ln q are zeros of the completed function (|E| ~ 1e−42). **Correction to the charter's control recipe:** a = q + 1 factors as (1 + q^{−s})(1 + q^{1−s}) and puts the zeros exactly on Re s = 1 and 0 (a = 3, q = 2 gives Re s = 1.000); use a strictly between 2√q and q + 1 for zeros inside the strip — main control here a = 2.9, q = 2: zeros at Re s = 0.82387668016604458, t = 4.5323601418271938 (2j+1).
- Critical line, C1 members ξ_N (step 0.05, t ≤ 230; zeta has 96 zeros there): number of real zeros = 2, 6, 16, 32, 52, 80, 96, 96 for N = 1 … 8; last real zero at t = 19.564, 37.495, 66.883, 104.682, 147.326, 201.057 for N = 1 … 6 — against the predicted departure height 4(N+1)² = 16, 36, 64, 100, 144, 196. ξ_N(½+it)/c_N at t = 1000 is 0.9995, 0.9972, 0.9907, 0.9769, 0.9527, 0.9150, 0.8626, 0.7960 for N = 1 … 8 (→ 1, as predicted). The root positions in that log are grid-accurate only (mpmath findroot accepts any point where |f| < 1e−30, and |Ξ| ~ 1e−70 there); a relative-tolerance bracketing refiner replaces it for all reported coordinates.

## 2026-09-30 19:05 IST — unit 3: complete zero census of ξ_N, N = 1–4, box 0 < Im s ≤ 200 (verify/census.py, census_zeta_N*_T200.{log,json})

Method: real zeros by sign changes (step 0.02, relative-tolerance bracketing); total count Z_tot in [1−smax, smax] × [0, 200] by the argument principle (right edge + right half of top edge, using E(1−s̄) = conj E(s) and E > 0 on the real segment — bottom minimum 0.4971); off-line zeros located by secant from minima of |E| on a band around the predicted branch |Γ-part| = c_N; completeness = the number found equals (Z_tot − Z_line)/2.

| N | Z_tot | real | off-line pairs | complete | lowest off-line zero (22 digits) |
|---|---|---|---|---|---|
| 1 | 96 | 2 | 47 | yes | 5.165902026924569091939 + 22.91546577056082331413 i |
| 2 | 94 | 6 | 44 | yes | 1.961986713365167413097 + 41.18954784298466213527 i |
| 3 | 92 | 16 | 38 | yes | 1.724565520046782821944 + 70.09754749943411569924 i |
| 4 | 90 | 32 | 29 | yes | 2.096563629552527773359 + 107.8802626577714556081 i |

- Every off-line zero found lies OUTSIDE the critical strip (min Re s − ½ = 4.666, 1.462, 1.225, 1.597): at the discrete steps N → N+1 the zeros leave the line far out onto a branch Re s ≈ σ_c(t) (at t = 200 the N = 1 branch is at Re s ≈ 80).
- Ordering invariant (zeros in Re s ≥ ½, Im s > 0 listed by height have nondecreasing Re s − ½; real zeros first): holds for N = 1–4, 0 violations (verify/monotone_check.py).
- **Theorem D (proof in NOTE):** on the line ξ_N(½+it) = Ξ(t) + P_N(t), P_N(t) = ½(¼+t²) Σ_{n>N} g_n(½+it) > 0, because g_n(½+it) = 4∫₀^∞ k_n(u) cos(tu) du with k_n(u) = exp(−πn²e^{2u} + u/2) positive, decreasing and convex on [0, ∞) (4y² − 6y + ¼ > 0 for y ≥ πn² > 1.457) — Pólya's criterion. So the chain DECREASES pointwise on the line to Ξ, and every real zero of ξ_N sits, in pairs, inside a negative lobe of Ξ (real-zero counts 2, 6, 16, 32, 52, 80 are all even).

## 2026-09-30 19:40 IST — unit 4: N = 5 census; independent re-verification; the lobe law confirmed (verify/reverify_*.log, lobes_T320.{log,json})

- N = 5 (box 0 < Im s ≤ 200): Z_tot = 84, real 52, off-line pairs 16, complete; lowest off-line zero 1.394052189225349727093 + 150.1654942505646873446 i.
- Re-verification of the first three off-line zeros for each N = 1–5 (15 zeros) by the DIRECT truncated sum at 80 digits (census used the tail formula at 30 digits): all agree to 20–21 digits (shifts 1.3e−21 … 5e−20). Exclusion to the right: the argument-principle count in [smax, 3 smax] × [0.05, 200] is 0 (|count| < 1e−28) for every N = 1–5. (The circle-contour count in the first pass used a wrong radius — the zero itself was taken as its own nearest neighbour through a precision mismatch; fixed in reverify.py, re-run in progress.)
- **Lobe law, numerical confirmation of Theorem D's consequence:** P_N(t) > 0 on a grid of [0, 320] for N = 1–8 (minimum at t = 0: 6.6e−8, 4.5e−15, 7.3e−25, 2.5e−37, 1.7e−52, 2.3e−70, 5.9e−91, 3.0e−114; P_N(320)/c_N = 0.996 … 0.28). Counting 2 zeros for every negative lobe of Ξ (150 ζ-zeros up to 320, 75 negative lobes) where min(Ξ + P_N) < 0 predicts 2, 6, 16, 32, 52, 80, 116, 150 real zeros for N = 1 … 8 — **exactly the census counts for N = 1–6** (computed independently). First negative lobe without zeros ("departure lobe") and depth/P_N there: N=1 (25.01, 30.42) 0.0070; N=2 (40.92, 43.33) 0.20; N=3 (69.55, 72.07) 0.32; N=4 (107.17, 111.03) 0.24; N=5 (150.05, 150.93) 0.12; N=6 (202.49, 204.19) 0.27; N=7 (265.56, 266.61) 0.020. Departure height ≈ 4(N+1)² + 6 … 10. For N ≥ 2 the lowest off-line zero's height lies inside the departure lobe.
