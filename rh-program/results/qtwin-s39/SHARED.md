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

## 2026-10-01 05:12 IST — batch 1 (Meyer at the page; route (i) with finitely many lattices)
- NOTE §0 (setting, record at the line, digest §B5/§B6/§F.2 quoted), §1 Lemma M (Meyer p. 25 unit-mass argument + Lagrange
  interpolation P_v(a) = 1_{a=v} in B(R_d)), Cor. M1 (pure point ⟹ no exceptional points), THEOREM D UNCONDITIONAL (QC §2.7 with Q4
  discharged). §2 THEOREM G1: every Beurling solution whose μ_q is a FINITE generalized Dirac comb — any trigonometric weights,
  infinitely many mass values allowed — is ζ (new Step 3: irrational frequencies are carried to irrational cosets, which meet the
  finitely many radical classes in finitely many points, so they cancel). Cor. G1′: purely atomic + finitely many mass values ⟹ ζ.
- Next: rung 1 for the weighted mechanism (verify/v1), controls for G1 (verify/v2), route (i) with infinitely many lattices.

## 2026-10-01 05:24 IST — batch 2 (rung 1 weighted; route (i) with infinitely many lattices)
- verify/v1_rung1_weighted.{py,log}: genus 1 over F₅ with REAL t (weights): b_d ≥ 0 (d ≤ 60, rigorous arb root isolation) ⟺
  t ∈ [−5, 6]; RH-false part [−5, −2√5) ∪ (2√5, 6]; the Q-side q-part positivity s_n ≤ 1 is empty over R already from n ≤ 4.
- NOTE §3 (rung-1 image of each route: (i) finite L-polynomials only; (ii) degenerate; (iii) none) and §4: Lemma A (atomic
  reduction for ζ·(bounded-frequency multiplier)); THEOREM L‴: if the rational primes S in the atoms' group have abscissa σ_S < ½,
  no Beurling solution at any q ≠ 1 — covers the whole Poisson-pair cone 𝒦_r with thin rational part, continuous parts included.
- Residue of route (i) named: thick rational part (σ_S ≥ ½) and infinitely many twisted combs.
- Next: controls (verify/v2: exact self-duality test on F55, R1, a thick-S mixture probe; DH noted), route (ii) model sets.

## 2026-10-01 05:42 IST — batch 3 (route (ii) model sets; route (iii) and the FE splitting)
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

## 2026-10-01 05:58 IST — batch 4 (the instrument; the one-condition class 𝒯)
- NOTE §7.1: exact-certificate table — every parametrizable family on which the exact FE can be imposed is excluded by a theorem
  (G1, G1′, D, L′, L‴ + Prop. S, U_q, P1, W3). §7.2: the smallest open sub-class 𝒯 (positive J-symmetric Poisson mixtures with thick
  rational part): FE, self-duality, dN ≥ 0 and the gap are automatic; the ONLY open condition is Π_ζ + log*(m) ≥ 0.
- verify/v4_thick_mixture_probe.{py,log} (+ firstpass log), v4b_thick_grid.{py,log}: q = 4 truncations, max-min of Π_F on [1, 64]:
  M = 2 global −0.680; M = 3, 4 local −0.401, −0.311 (rising with more primes); q = 9: −0.506 / −0.526. Evidence only.
- Next: prior art at the page (arXiv API returning 503 — retry loop running in background), attack log, close §0.4, rows.

## 2026-10-01 06:00 IST — batch 5 (prior art at the page; attack log)
- sources/: KNS 2023 (2306.14013, pdf + txt), Córdoba 1989 landing page via Firecrawl (abstract only — body paywalled), arXiv
  sweeps q2–q6 (Beurling+FE; crystalline+positive; Fourier quasicrystal to 2026-08; three abstracts incl. Boyvalenkov–Favorov 2025,
  Favorov–Değer 2026). No printed theorem closes the weighted case; KS 2020 line 49 "probably very difficult"; BSS §8 open.
- NOTE §8 (prior-art table), §9 (attack log on Lemma M, M1, G1 Step 3, Prop. S, L‴, route (ii) P2 incl. the retracted heuristic).
- Next: §0.4 the close as THEOREM G; §10 the Instruments row, Untried entries, waste line; header status.

## 2026-10-01 06:02 IST — batch 6 (controls; the close)
- verify/v2_controls_G1.{py,log}: F_{5,5} passes the exact self-duality test (theta 0 at 50 digits; Fejér exact via Poisson ≤ 9e−50),
  goes through G1 Steps 0–4 (𝒩 = N, one class, masses {1, 6, 11} with period 25) and is excluded only at L′: Π(5), Π(25), Π(125)
  = 6, −7, 17. read-O R1: atoms +√5, −2, +2 — fails G1 Step 0. DH: Γ((s+1)/2), real coefficients of both signs — outside (A).
- NOTE §0.4 CLOSE inserted: THEOREM G (rigidity extended; obstruction to rigidity; obstruction to construction; residue R1–R4;
  smallest open sub-class 𝒯 with ONE open condition); §10 Instruments rows (3), Untried UT-QT1…UT-QT4 (labels avoid the digest's UT-1…UT-9), waste line.
- Status: COMPLETE pending the final consistency read.

## 2026-10-01 06:04 IST — CLOSE: G, stated as a theorem, with RIGIDITY extended
- Final consistency read done; fixes applied in place (the q² claim for non-integer q → q^{2k}; zeta-zero repairs are split
  directly, not by Prop. S; one vague coverage phrase in L‴; a table cell with a pipe).
- CLOSE (NOTE §0.4): THEOREM G. (1) Rigid: finite generalized Dirac combs with any weights (G1), purely atomic with finitely many
  masses (G1′), discrete systems (Theorem D, now UNCONDITIONAL via Meyer p. 25 at the page + Lagrange), ζ-divisible left of ½ with
  thin rational part (Prop. S + L‴). (2) Obstruction to rigidity: comb structure theory stops at finitely many lattices/values; the
  Landau obstruction stops at σ_S = ½ (the pole of ζ becomes visible on the multiplier's monoid — the rung-1 mechanism, no rung-1
  image). (3) Obstruction to construction: every parametrizable family excluded (§7.1); residue (R1)–(R4) infinite-dimensional.
  Smallest open sub-class 𝒯 = thick positive J-symmetric Poisson mixtures: ONE open condition, Π_ζ + log*(m) ≥ 0.
- No construction; no Group-I control claimed. Rows for the orchestrator in NOTE §10 (3 Instruments rows, UT-QT1…QT4, 10(o) line).
- Record note: the block stamps after START were first written ahead of the machine clock (estimates); corrected in place at 06:04
  IST to the file times (`ls -l verify/`); order unchanged.

## 11:14 IST 2026-10-01 — OPUS READER (Session 40 dual read), batch 1
- Reader: Opus 5.5, brief `novel-wave-s39/READ-BRIEF-O.md`. NOTE read whole at SHA-256 cebe0a96… (407 lines). Not opened: read-F, verify-F.
- Re-derived ✓: Lemma M (Meyer p. 25 checked as a page image: printed dμ_n = n^{−1}Ψ(n^{−1}x)dμ(x) = the NOTE's repair), G1 Steps 0–4,
  G1′, Lemma A, L‴ (Landau step proved by QC Lemma L's own proof — no local finiteness used), Prop. S (Wiener's lemma re-proved),
  L‴ general, route (iii) repair (FE and Mellin terms recomputed). M1 needs "μ̂ purely atomic" added (minor).
- Credit point: Lemma M + unconditional Theorem D were already proved in qcond-s38/read-O §2 (05:20) and are in QC-now (579f22e3…).
- Mis-attribution: zeta-zero repairs fail Prop. S hypothesis (i) (densities ≍ x^{−½}); covered by the direct splitting + §4 instead.
- verify-O/o1 (exact sympy root isolation): W1 for d ≤ 60, W2, W3 (exact certificate), W4 all reproduce; o2: a positive self-dual comb
  with an irrational frequency (self-dual to 60 digits) — it violates G1 Step 1 (not Beurling), so G1 Step 3 is genuinely needed.
- Next: §5 (Pisot, KNS at the page), §7 probe of 𝒯 at q = 4 by my own optimizer, prior art.

## 11:45 IST 2026-10-01 — OPUS READER, batch 2 (route ii; the 𝒯 probe; prior art)
- verify-O/o3 (own lattice sums, 50 digits): Pisot model-set self-duality 2.7e−51 / 0 / 1.1e−50; Z_0, Z_1 first points; unit-orbit
  Π(φ²) = −24.0, −7.0e4, −1.7e13 — all AGREE. P2 gap (minor): KNS gives f, f̂ vanishing on Z_j, not an even SELF-DUAL k; fixed via
  KNS Lemma 6 free interpolation at extra nodes (single-check).
- 𝒯 probe at q = 4, own code (exact atom positions; log*(m) by a sparse triangular solve of D′ = D·L′; DE + analytic-gradient SLSQP):
  M = 2: −0.680076, M = 3: −0.400711 — digit for digit; M = 4: −0.293651 (BETTER than the NOTE's −0.310622; exact-rational re-check by
  power series: −0.293650523). At each optimum about HALF the atoms in [1, 64] are negative and the total negative mass grows
  (4.51 → 27.30 → 62.82); beyond 64 the M = 4 optimum falls to −0.58 (x = 120), −1.13 (x = 225). The rising max-min is dilution,
  not approach to feasibility (min/mean|Π| ratio 2.3 → 2.6 → 5.5).
- Prior art on disk the NOTE misses: Hilberdink 2012 (Acta Arith. 152) Thm 4.3 (multivariable Landau, finitely many primes) and Thm 4.4
  (power sums τ_n ≤ 1 ∀n force |μ_r| < 1) — the latter contains W3's conclusion outright; KS lines 43–49, 56–58, 792–796 and BSS §8
  (line 1236) quoted correctly.
- Running: M = 5 DE + polish (one heavy process); arXiv queries q7–q9 (rate-limited, background).

## 11:51 IST 2026-10-01 — OPUS READER, batch 3 (pairs)
- read-O §3 prior-art table, §4 FIX-FIRST F1–F6, §5 minor m1–m10 written (16 pairs). FIX-FIRST: F1 credit (Lemma M/M1/Theorem D
  unconditional = QC read-O §2); F2 Hilberdink 2012 Thm 4.3/4.4 missed (W3 in print; L‴ finite-S core in print); F3 M = 4 probe value
  (≥ −0.293651, not −0.31; M = 5 ≥ −0.218541); F4 Cor. M1 false as written (μ = δ₀, μ̂ = Lebesgue) — add "μ̂ purely atomic"; F5 zeta-zero
  repairs are outside Prop. S/L‴(general) hypothesis (i); F6 §5.2 mechanism (b) is a heuristic labeled (P) — "k cannot be smooth" and
  §0.4(3) "every finite-dimensional family … excluded" are unproved (smooth even self-dual k vanishing on Z_j exist by KNS Lemma 6).
- M = 6 DE + polish running (one heavy process).
