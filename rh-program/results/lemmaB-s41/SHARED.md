# SHARED — stream lemmaB-s41 (append dated blocks; newest last)

## 16:55 IST 2026-10-01 — U7-patterns (Opus 5.5): started
Plan: own block generator of S8 (double-double, rigorous margin audit; cross-checked against s40 logs, never imported), ρ = π/16, π/32 to 10⁹; mine c_k, e_k for excursion anatomy, window variances, cross-scale correlations, Lyapunov candidates; variants τ = ¼, ¾ and early offsets. Outputs in `U7-patterns/`; scratch arrays in `/private/tmp/rh-s41-lemmaB-U7-patterns/`.

## 16:59 IST 2026-10-01 — ORCHESTRATOR: notes for all units in `results/lemmaB-s41/ORCH-NOTES.md`
O1: Theorem 1.6 holds with a MEAN-SQUARE bound on E in place of the pointwise one (so an "almost all intervals" statement is a legitimate target for U1, U3). O2: hypothesis (A) is only needed as a Mellin-average positivity at one point. O3: multiples of a small g-prime in a window are exactly as regular as N one scale down. O4: where the parity barrier sits. O5: the trivial lattice bound for the sparse regime (U4). O6: linear stability of the loop. Read the file before your close; re-derive anything you use.

## 17:04 IST 2026-10-01 — U6-certificate (Opus 5.5): start
Plan: own generator `U6-certificate/verify/s8cert.c` (lattice/cell form, every cell decision proved by a floating-point error bound or re-decided exactly in GMP integers from a rational enclosure of π), block moments for Σ n^{−σ} with rigorous error terms, arb (python-flint) evaluation of F_X, X to 10^9–10^10 for π/16 and π/32. Cross-checks against the s40 logs of s8o/s8dd (read-only). Early observation [proved here, to be written in NOTE §1]: since N is an integer and E > −½, E(u) ≥ ½ − {ρ(u−1)+½} for all u; at a lattice point X = x_K the tail σ∫_X^∞E u^{−σ−1}du is then > 0, so the certificate condition of Cor. 1.7(iii) becomes F_X(σ₁) ≥ 0 (no ½X^{−σ₁} term).

## 17:05 IST 2026-10-01 — U7-patterns: own generator exact to 10¹⁰ (π/16, π/32)
`U7-patterns/verify/s8gen.c` (block sweep, double-double, decision margins audited, FLAG = 0; reproduces the s40 logs digit for digit at 10⁷/10⁸). 10¹⁰ in 118 s (π/16) and 48 s (π/32), < 0.81 GB — anyone needing S8 data to 10¹⁰ can use it. sup E(10¹⁰) = 26.137 (π/16, 0.0493·log²x), 15.434 (π/32, 0.0291·log²x): the log² law holds to 10¹⁰. Largest g-prime gap G: 240 cells = 1222.3 (π/16), 73 cells = 743.6 (π/32); G/log²x rises (π/16: 1.29 at 10⁷ → 2.31 at 10¹⁰) while G/log³x is flat (π/32: 0.061 ± 0.003 on 10⁷–10¹⁰). So gaps follow a log³ law, E a log² law (queue heuristics predict exactly this): Prop. 2.1 loses a factor log x; Lemma G must be a log³-type statement. NOTE §2.
