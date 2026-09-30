# SHARED — unit `qtwin-s39` (the last corner of Q_cond: weighted / clustering Beurling systems with Riemann's exact FE at q > 1)

Append-only, dated blocks. Writer: Opus 5.5 (unit agent). Outputs only under `results/qtwin-s39/`. No git.

## 2026-10-01 04:50 IST — START
- Read whole: BRIEF.md; `qcond-s38/NOTE.md` (SHA-256 445cfe96…, 447 lines), its SHARED, verify v1–v4 (scripts + logs);
  `novel-wave-s37/beurling-fe/NOTE.md` §0–§4, §8–§12; `read-O.md` o3–o5, §6 R1–R4; digest (SHA-256 e86f642a…) §B5, §B6, §F.2;
  Meyer LNM 117 OCR scan pages 24–26 (`fetched-r9/r9-05-meyer-1970-LNM117.ocr.txt` lines 641–745).
- Plan: NOTE §0 (question, record, digest quotes) → §1 Lemma M (Meyer finite values via Lagrange interpolation; Theorem D
  unconditional) → §2 rung 1 for each design route → §3 design routes (i)–(iii) each to a theorem or a certificate → §4 LP/SDP
  instrument (exact duality certificates) → §5 prior art at the page → §6 attack log → §7 close as a theorem.
- Compute policy: one heavy process at a time, ≤ 30 min per run, load checked before each run (04:45: 1 process > 50%).

## 2026-10-01 05:20 IST — batch 1 (Meyer at the page; route (i) with finitely many lattices)
- NOTE §0 (setting, record at the line, digest §B5/§B6/§F.2 quoted), §1 Lemma M (Meyer p. 25 unit-mass argument + Lagrange
  interpolation P_v(a) = 1_{a=v} in B(R_d)), Cor. M1 (pure point ⟹ no exceptional points), THEOREM D UNCONDITIONAL (QC §2.7 with Q4
  discharged). §2 THEOREM G1: every Beurling solution whose μ_q is a FINITE generalized Dirac comb — any trigonometric weights,
  infinitely many mass values allowed — is ζ (new Step 3: irrational frequencies are carried to irrational cosets, which meet the
  finitely many radical classes in finitely many points, so they cancel). Cor. G1′: purely atomic + finitely many mass values ⟹ ζ.
- Next: rung 1 for the weighted mechanism (verify/v1), controls for G1 (verify/v2), route (i) with infinitely many lattices.

## 2026-10-01 05:45 IST — batch 2 (rung 1 weighted; route (i) with infinitely many lattices)
- verify/v1_rung1_weighted.{py,log}: genus 1 over F₅ with REAL t (weights): b_d ≥ 0 (d ≤ 60, rigorous arb root isolation) ⟺
  t ∈ [−5, 6]; RH-false part [−5, −2√5) ∪ (2√5, 6]; the Q-side q-part positivity s_n ≤ 1 is empty over R already from n ≤ 4.
- NOTE §3 (rung-1 image of each route: (i) finite L-polynomials only; (ii) degenerate; (iii) none) and §4: Lemma A (atomic
  reduction for ζ·(bounded-frequency multiplier)); THEOREM L‴: if the rational primes S in the atoms' group have abscissa σ_S < ½,
  no Beurling solution at any q ≠ 1 — covers the whole Poisson-pair cone 𝒦_r with thin rational part, continuous parts included.
- Residue of route (i) named: thick rational part (σ_S ≥ ½) and infinitely many twisted combs.
- Next: controls (verify/v2: exact self-duality test on F55, R1, a thick-S mixture probe; DH noted), route (ii) model sets.
