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

## 2026-10-01 06:20 IST — batch 3 (route (ii) model sets; route (iii) and the FE splitting)
- verify/v3_pisot_model_set.{py,log}: μ_k = Σ_{x∈Z[φ]}k(x^σ/5^{1/4})δ_{x/5^{1/4}} is exactly self-dual iff k̂ = k (Poisson on a unimodular
  lattice); acceptance test on the Gaussian: theta 2.7e−51, Fejér within the ξ^{−2} tail bound. The gap at q = √5φ^{2j} ⟺ k = 0 on the
  cut-and-project set Z_j (u.d., density 2/(5^{1/4}φ^j)). Finite Hermite k: excluded exactly (finitely many zeros). KNS 2023 Thm 1(ii)
  (fetched to sources/, at the page): zeros alone do NOT force k = 0 — my earlier "q < 4 uniqueness" heuristic is retracted.
- verify/v3d_pisot_beurling_probe.{py,log}: Gaussian weights fail Euler positivity (j = 0 at n = 4/φ; j ≥ 1 already on the unit orbit,
  Π(φ²) = c(φ²) − c(φ)²/2 < 0). Mechanism: super-polynomial decay breaks c(n₁n₂) ≳ c(n₁)c(n₂); admissible k must be non-smooth.
- NOTE §5 (route ii), §6: Proposition S (if F/ζ converges absolutely left of ½, the FE splits and the atomic part is itself a solution);
  Theorem L‴ general form; route (iii) verdict incl. the "zeta-zero repair" G = R(s) + q^{½−s}R(1−s), R with poles at zeros of ζ —
  an exact-FE family whose continuous part satisfies the FE alone, so it falls back on the atomic theory.
- Next: §7 instrument on the smallest open sub-class (thick positive Poisson mixtures), §8 prior art, attack log, close.

## 2026-10-01 06:50 IST — batch 4 (the instrument; the one-condition class 𝒯)
- NOTE §7.1: exact-certificate table — every parametrizable family on which the exact FE can be imposed is excluded by a theorem
  (G1, G1′, D, L′, L‴ + Prop. S, U_q, P1, W3). §7.2: the smallest open sub-class 𝒯 (positive J-symmetric Poisson mixtures with thick
  rational part): FE, self-duality, dN ≥ 0 and the gap are automatic; the ONLY open condition is Π_ζ + log*(m) ≥ 0.
- verify/v4_thick_mixture_probe.{py,log} (+ firstpass log), v4b_thick_grid.{py,log}: q = 4 truncations, max-min of Π_F on [1, 64]:
  M = 2 global −0.680; M = 3, 4 local −0.401, −0.311 (rising with more primes); q = 9: −0.506 / −0.526. Evidence only.
- Next: prior art at the page (arXiv API returning 503 — retry loop running in background), attack log, close §0.4, rows.

## 2026-10-01 07:10 IST — batch 5 (prior art at the page; attack log)
- sources/: KNS 2023 (2306.14013, pdf + txt), Córdoba 1989 landing page via Firecrawl (abstract only — body paywalled), arXiv
  sweeps q2–q6 (Beurling+FE; crystalline+positive; Fourier quasicrystal to 2026-08; three abstracts incl. Boyvalenkov–Favorov 2025,
  Favorov–Değer 2026). No printed theorem closes the weighted case; KS 2020 line 49 "probably very difficult"; BSS §8 open.
- NOTE §8 (prior-art table), §9 (attack log on Lemma M, M1, G1 Step 3, Prop. S, L‴, route (ii) P2 incl. the retracted heuristic).
- Next: §0.4 the close as THEOREM G; §10 the Instruments row, Untried entries, waste line; header status.
