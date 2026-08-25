# A4 M2 decision gate — adversarial audit

**Role:** independent adversarial auditor (did not write SPEC.md or the implementation).
**Contract audited against:** adjudication repairs R5 and R7 (`results/adjudication-A4.json`, binding), direction file `directions/A4-lindelof-lock.md` (mechanism, Phase-4 verdicts, merge guidance), `results/full-map.md` (lemmaR_tight, Prop 4.1, PairCeiling), v5 SS7.2/7.3/7.5 (`sources-extracted/v5_p13.txt`, `v5_p14.txt`), tx_081/tx_082 (support arithmetic, pair-block spectrum).
**Artifacts audited:** `SPEC.md`, `code/` (all 8 modules read in full), `RUN-REPORT.md`, `gate-result.json`, `witness_N64.json`, `runs/*.json`, `verify/`.
**Audit code:** independent verification suite (position-space Gram traces — a different evaluation path from the implementation's Fourier/W3 assembly), own CUE sampler with fresh seeds, own LP re-solves. Scripts in the session scratchpad (`audit_verify.py`, `audit_tier2.py`); every number below re-derived, none recalled (standing order 5).
**Date:** 2026-08-26.

---

## 1. Audit verdict

**The ABSORPTION verdict stands.** I attempted to break it in every direction I could construct and failed. The gate is R5-conformant, the code implements the SPEC, the witness is real, and the decisive equality delta_0 = 0 is reproducible from independently recomputed data. Three qualifications (Section 5, findings 1–3) affect the *wording and completion path of the no-go deliverable*, not the gate decision. The R2-bridge investment question the gate was built to price is answered: the cubic-certificate payoff at the proven operating point is zero.

---

## 2. SPEC-vs-R5 conformance (component by component)

| R5 component | SPEC/implementation | verdict |
|---|---|---|
| Clustered sine-process null, occupancy-2 cross-term background, MC-sampled, convergence justified | CUE eigenangles n in {64,128,512,1024,2048}, R adaptive to SE(m3) <= 0.5%, batch-means + jackknife, 1/n extrapolation against closed forms m2 = 1/lam + lam/3, m3 = 1 + 1/lam^2 with halt condition; occupancy shares quantified (54% / 80%) | **conformant** (closed forms verified by me two independent ways, Section 3.2–3.3) |
| Marks/cluster alphabet to slowly divergent W; W-scaling reported | W in {2,3,4,6,8}, delta_0(W) reported, delta_inf fit; pair mult <= floor(W/2) | **conformant** (trend trivial: identically 0; the absorber needs only marks {1,2}, so W-divergence cannot restore a bite — the sprinkling question is answered, not dodged) |
| Depth-parametrized pair family u in [0, 1/L'] with TRUE Prop 4.1 block spectrum incl. shallow pairs | depth grid w in {1/64, 1/8, 1/4, 1/2, 3/4, 1} (+ deep probes 1.5, 2); exact block law m(1 +/- A(w)) matching tx_082 verbatim ("pair eigenvalues mL2a(1 ± A)"); shallow-pair continuity verified | **conformant**, and the SPEC goes beyond R5: it derives the exact per-zero identity c = 3F − 2 (pairs, every depth), which supersedes the adjudication's computation-8 phase model. I verified this independently (Section 3.4). |
| Realizability-only positional freedom, constraints stated with necessity/sufficiency | SPEC 3.2 states exactly (a)–(e), argues both directions explicitly | **conformant**; the argument is sound (see Section 4.4 for the one residual caveat) |
| Row system: density; Frobenius with split; signed cubic with honest content (R6); ALL-V ladder (not scalar tail — R1); n_- <= p; power-mean; Hoelder + o(N); garnish fuzz of order sqrt(eps C_led) re-derived | R-1..R-9 as specified; ladder on V-grid {2..16} covering all realized spectra, C_led in {10,100,1000} with null floor C_led^min = 3.82; nonlinear rows enforced per-column on explicit spectra (the correct configuration-by-configuration reading, same class as the parent PairCeiling); fuzz constant re-derived as 2*sqrt(2)*sqrt(C_led eps_g), correcting both the adjudicator's 2*sqrt(C eps) and the formulator's first-pass 5/sqrt(3) | **conformant**; I re-derived the fuzz optimum myself (min-profile N(h) = C min(a^-4, h^-4), a = sqrt(2C/eps): value 4C/a = 2 sqrt2 sqrt(C eps)) — the SPEC's constant is right |
| Decision criterion: delta_0 with error bars, W-stability, "inconclusive" rule | SPEC 5.4 pre-registered verbatim; SPEC 5.5 maps each R5 phrase to a rule | **conformant** |
| Verify recalled sine moments before use | verify suite V1/V4 + implementer's independent MC + my own third implementation | **discharged** |
| Gate before bridge investment; either branch a deliverable | run completed with no R2 input; F4 semantics correct (absorption is *strengthened* by assuming the ladder) | **conformant** |

**Silent-narrowing check (the R5 failure mode):** none found. The adversary class is wide where R5 demands width (marks to 8, pairs at six depths, continuous positions, mixtures, 3548 pricing-generated columns on top of 455 structured seeds). The only narrowings are numerical-hygiene filters (eig-consistency < 1e-8; n_- <= p assert), which can only reject buggy columns — and narrowing the adversary is anti-absorption, so it cannot have manufactured this verdict. Note the marks-{1,2} precedent cuts the other way here: a narrowed adversary fakes a *bite*, never an absorption.

---

## 3. Code-vs-SPEC conformance and independent recomputation

All checks below use my own code path: position-space Gram M[z,z'] = sqrt(m_z m_z') psi_J(gamma_z − gamma_z') with the Dirichlet kernel, traces from tr M^k, eigenvalues from eigh — never the implementation's c_s/W3 Fourier assembly.

### 3.1 The grid Parseval identity (the absorption mechanism)
Claim: on the 65-site grid (spacing 64/65), tr G_1^2 = sum m^2 exactly, for every site subset and mark assignment.
- **Analytic re-derivation (mine):** c_s is 65-periodic on the grid; the flat-window weights (65−|s|)/65^2 sum to exactly 1/65 on every residue class mod 65 within |s| <= 64; DFT Parseval on Z_65 then gives tr G_1^2 = sum m^2 with no error term. Verified.
- **Numeric:** 40 random grid configurations (random subsets, marks 1–8): max |F1 − sum m^2| = 4.5e-13.
- The continuum analog (integer lattice under sinc, tr G_1^2 = sum m^2 (1+o(1))) is the campaign record's "adversary lattice" (tx_081); the RUN-REPORT's continuum-honesty paragraph is correct.

### 3.2 Null-model budgets (re-run, fresh seeds, own sampler)
My CUE MC (independent QR sampler, seeds 777001/777002):

| n | m2(1) mine / theirs | m2(1/2) mine / theirs | m3(1/2) mine / theirs |
|---|---|---|---|
| 64 | 1.32317(105) / 1.32363(74) | 2.11120(84) / 2.11087(63) | 4.76099(491) / 4.75867(362) |
| 256 | 1.33045(132) / 1.33115(66) | 2.15305(103) / 2.15231(63) | 4.94059(616) / 4.93758(373) |

Every entry agrees within ~1 combined sigma. Closed forms anchor: m2(1/2) = 13/6, m3(1/2) = 5, m2(1) = 4/3.

### 3.3 The closed forms themselves (the budget centers)
- m2(lam) = 1/lam + lam/3: my hand re-derivation of the Fourier-side integral reproduces it exactly (and it equals the paper's unconditional prime-side kappa(lambda) — Theorem 5.8 — which is the strongest possible identity check at second order).
- m3(1/2) = 5: independent **real-space 2D quadrature** of 1 + 3∫(1−S^2)psi^2 + ∫∫rho3·psi psi psi (determinantal rho3, truncation X = 40/80): 4.9896 → 4.9932, trending to 5 with truncation. Together with the MC this confirms the cubic budget center from two routes disjoint from the implementation's.
- m3(1) = 2 and m2(1) = 4/3 match v5's recalled sine moments (v5_p13.txt line: m_k(1) = 1, 4/3, 2, 13/4) — the recalled values are now verified, discharging the adjudication's "m-values still recalled" caution for k <= 3.
- Doubles-plane diagnostic: G(1) = 2 − (3·4/3 − 2) = 0 (the designer's "2 = 2"), G(1/2) = +1/2; margin 2m2 − m3 at 1/2 = −2/3 < 0. All reproduce.

### 3.4 The pair block law (the mimicry structure)
My own Hermitian frequency matrix (rebuilt from the definition): for a single pair at depth w, at three unrelated positions each,
- eigenvalues = (m(1−A'), m(1+A')) to 1e-12, position-independent to 1e-12;
- cubic charge = 2m^3(1 + 3A'^2): 8.0005 at w = 1/64, 8.033 at w = 1/8 — **never 0 at any depth**;
- per-zero identity c = 3F − 2 holds exactly at every depth.

This confirms the SPEC's structural discovery and **falsifies the task brief's mechanism premise** ("a hyperbolic pair block contributes (+a)^3 + (−a)^3 = 0 to tr G^3 while a double contributes +8"): under the true Prop 4.1 spectrum (tx_082 verbatim: mL^2a(1 ± A), A >= 1) the pair block is not (±a); its cubic charge is >= 8m^3 at every depth, and pairs sit on the same affine plane c = 3F − 2 as doubles. It also supersedes the adjudication's computation-8 phase model ((+1,−1) at uL = 1, cubic ~ 0). Consequence, verified: the cubic row's entire isolated-block content is Sum m(m−1)(m−2) — zero on marks {1,2} and on all pairs — so all discriminating power was always in clustering cross-terms, which the gate shows to be adversary-tunable. The absorption is thereby structurally explained, not merely observed.

### 3.5 The witness (the load-bearing object)
Recomputed all three columns through my independent path: **every row value reproduces to 1e-6 or better** (F1 = 64/96/128 exactly; F' and C' to displayed precision; ladder counts identical; n_- = 0). Law aggregates: E[F1] = 88.9478, E[F'] = 132.818, E[C'] = 289.327, E[N_d]/N = 0.8050957 — feasibility re-confirmed for every Tier-1 row at centered matched budgets, at C_led = 100 **and** C_led = 10.
Exact-rational spot check: the vacancy lattice's F' = **4128/33** — my hand derivation (c_s = −(unit phase) off the 65-lattice zero mode; F' = 4096/33 + 32/33) matches the reported 125.0909... exactly. F1 = 64 exact.

### 3.6 LP re-solve (fresh, from re-derived data)
I recomputed the row data for **all 4003 dictionary columns** through my position-space path: max relative deviation vs the shipped rows = 3.3e-15; ladder-count mismatches: 0; stored Tier-2 form factors |c_j|^2: exact match; n_- <= p violations: 0 of 4003. Then my own linprog solves:

| cell | P_full | P_base | P_cal | delta_0 |
|---|---|---|---|---|
| primary (matched, eps .05, C 100) | 0.80509568 | 0.80509568 | 0.80509568 | −4e-14 |
| asymptotic, eps .002 | 0.83200000 | 0.83200000 | 0.83200000 | −1e-13 |
| asymptotic, eps .05 | 0.80000000 | 0.80000000 | 0.80000000 | −5e-14 |
| W in {2,3,4,6,8} (primary) | — | — | — | all < 4e-13 |

All match `gate-result.json` to LP tolerance. The eps law P = 5/6 − (2/3)eps is the analytic lemmaR_tight corner (my derivation: F1 >= sum m^2 rigorously — every off-diagonal term is psi^2 >= 0 for on-line configurations — so mark accounting binds; doubles are optimal at cost ratio 1/m maximized at m = 2), and the grid attains it with equality. The eps = 0.002 optimum's support meets the cubic equality genuinely: E[C'] = 320.64 in [319.36, 320.64].

### 3.7 Sanity/regression cross-checks
- ppp resonance: my sieve to 3e6 gives 2.315762 — matches SPEC, RUN-REPORT, adjudication.
- Tier-A regressions reproduce (lambda = 1 degeneracy 5/6 with and without cubic; squeeze LP 2.824 + tail vs 2 sqrt 2 = 2.8284; K1-as-written vacuity; W = 2 iso-block infeasibility).
- N = 128: 40/40 records delta_0 < 9e-13, all statuses 0.
- Scan grid: 900/900 records, max |delta_0| = 6.4e-13, no infeasibility.

---

## 4. Break attempts (what I tried, what happened)

The verdict is absorption, so the break directions are: (a) the witness secretly violates a row of the true system; (b) the LP omits a row R5/R7 mandates; (c) the equality delta_0 = 0 is a dictionary/solver artifact; (d) instability under scale/parameters/seeds.

1. **Independent witness recomputation** (different code path, different kernel evaluation, exact-rational spot check): reproduces exactly; feasible. FAILED to break.
2. **Harsher ladder than the SPEC's:** I imposed the ladder **per column** (not in expectation) at C_led = 4 — barely above the null's own floor 3.82 and below the SPEC's minimum 10. Absorption survives (P_full = P_base = 0.8 at asymptotic eps = 0.05, delta_0 = 8e-14). The absorption does not hide behind expectation-aggregation of the ladder or a generous C_led. FAILED.
3. **Missing-row hunt.** Every R5/R7 row is either imposed (density, F1, F', signed cubic, ladder, fuzz) or automatic on explicit spectra (inertia, Frobenius split, power-mean, Hoelder) — and I confirmed n_- <= p on all 4003 columns. Nonlinear rows acting per-column is the correct configuration-by-configuration certificate class (identical to the parent PairCeiling's). The only genuine data class beyond Tier-1 is the open-band form factor — probed by Tier-2 (next item). PARTIAL — see finding 2.
4. **Near-CUE pinning (the strongest realism row).** My own re-solve with pinning rows built from my own |c_j|^2 values: tau2 = 1, eps = 0.05: P_full = P_base = 0.8333622, delta_0' = 0 (exact match to their verify block). I then probed beyond the report at tighter eps (dictionary-limited, no colgen): delta_0' = 6.0e-6 (eps .02), 5.0e-4 (eps .01), 3.9e-4 (eps .005) — nonzero residuals, non-monotone, of the same order as the documented pricing-convergence uncertainty (~3e-4), and these are upper bounds (columns missing for P_full inflate it). No decision-relevant bite signal; but this is where any residual signal concentrates. See finding 2.
5. **Window-degeneracy probe.** The exact delta_0 = 0 rests on the flat-window grid decoupling. The run's own scan already shows the honest picture: MT-cosine at lambda = 1 leaves residual delta_0 ~ 2e-5–6.4e-5 (unconverged upper bounds). Three orders below decision scale, sign as expected. See finding 1.
6. **Base-corner attack via pairs.** The airtight sandwich (P_full <= witness value = analytic base minimum <= P_base <= P_full) is rigorous for **atom-only** adversaries (F1 >= sum m^2 proven; numeric sweep found no violation). For pair-containing configurations, cross-terms 2 Re psi(x+iy)^2 can in principle be negative at lambda = 1, so "F1 below sum m^2, freeing budget for more doubles" is not analytically excluded; pairs are cubic-invisible (c = 3F − 2), so such a channel would produce a *bite* through pair-pricing. The pricing search (gradients over positions, pair/depth moves, min_rc = 0 at S = 200 at the decision points) found nothing. Heuristic, not proof. See finding 4. FAILED to break, but this is the one channel not closed analytically.
7. **Budget-center stress (flag F2).** The absorption is insensitive to the c_3 center within the scanned brackets (eps 0.002–0.10, Gamma to 0.25, matched vs asymptotic centers differing by 5%): delta_0 = 0 everywhere. An O(1)-per-zero error in the c3(lambda') identification cannot flip the verdict. FAILED.
8. **Seed/scale stability.** Fresh-seed MC (mine) within 1 sigma; N = 64 → 128 stable; W-independence exact (the witness uses marks {1,2}, inside every W-class — this kills the sprinkling restoration route by inclusion, not by extrapolation). FAILED.

---

## 5. Findings

**FATAL: none.**

**MAJOR (qualify the deliverable, not the verdict):**

1. **The exact zero is window-specific.** delta_0 = 0 *exactly* holds at the primary flat/flat configuration, where the psi_1-zero grid kills every lambda = 1 cross-term identically. With the Montgomery–Taylor cosine window at lambda = 1 the degeneracy breaks and the scan leaves unconverged residuals delta_0 ~ 6e-5; Tier-2 near-CUE pinning at tight eps leaves unconverged residuals <= 5e-4 (my probes, item 4.4). All are orders below decision relevance (the M4 hope was delta_0 ~ 0.01–0.03), but the no-go paper must claim "delta_0 = 0 exactly at the primary configuration; <= O(1e-4) across the window family and <= O(5e-4) under near-CUE pinning at this scale, within pricing-convergence uncertainty" — not a universal exact zero. The RUN-REPORT states the window residual honestly; its suggestion that the no-go wording "may drop the re-reading hedge" is slightly too strong given the tight-eps Tier-2 residuals.
2. **The headline witness is not near-CUE.** The Tier-1 witness's bandwidth-one data is maximally anti-correlated (vacancy lattice: |c_j|^2 = 1 for all j), far from the near-CUE laws of the parent 256-law architecture (pinned to 3e-40). The truly comparable absorption — near-CUE-pinned, P ~ 5/6, delta_0' = 0 — exists (Tier-2) but is currently diagnostic-grade: colgen unconverged (documented −2.9e-4 residuals), N = 64 only, and its data class rests on the unfetched BGSTB24 statement (flag F1). **For the publishable no-go, a near-CUE witness must be promoted to decision grade** (converged colgen, N = 128 confirmation, BGSTB24 fetched and checked). Until then the no-go is fully supported against the lemmaR_tight data class (density + Frobenius + integrality), and supported at diagnostic strength against the near-CUE class.
3. **Scope of the no-go headline.** The gate decides the N_d >= 5/6 benchmark — exactly R5's criterion, correctly implemented. The proposed paper title ("the bandwidth-one ceiling is robust under RS-range cubic augmentation with capacity control") evokes the 0.6818287 *simple-fraction* ceiling, whose cubic-augmented rerun (a p1-objective variant, the old N4) was not performed. Either run the p1-objective variant (cheap: same dictionary, change the objective) or scope the claim to the distinct-zeros/5-6 benchmark.

**MINOR:**

4. For pair-containing adversaries the exactness of delta_0 = 0 rests on converged pricing (min_rc = 0, S = 200), not on the atom-only analytic sandwich; a lambda = 1 pair-interference channel lowering F1 below sum m^2 is not analytically excluded (it would surface as a bite via pair-pricing, which the cubic row cannot see — c = 3F − 2). The model-level theorem in the no-go paper should either restrict to atom-only configurations (where it is airtight) or close this channel analytically.
5. Tier-A's stated reason for W = 2 iso-block infeasibility ("iso cubic max 4 < 5") ignores deep pairs (iso cubic 1 + 3A^2 > 4 for w >~ 1); the conclusion is nevertheless correct for the sharper reason the SPEC itself establishes: the whole marks-{1,2}-plus-pairs iso world is confined to the affine plane c = 3F − 2, forcing c = 3(13/6) − 2 = 4.5 != 5. Cosmetic (calibration tier).
6. Bookkeeping drift: RUN-REPORT's Tier-2 table (0.833377) vs gate-result.json's verify block (0.8333622) reflect different dictionary snapshots; witness column tags (cg_rc-…) are not unique identifiers (content, which is recorded, is). Cosmetic.
7. The task brief's own "+8 vs 0" doubles-vs-pairs premise is falsified by the exact Prop 4.1 block law (Section 3.4) — a finding *for* the implementation, recorded here because it corrects the direction file's Step-4 narrative and the adjudication's computation 8; tx_082 was right all along.

---

## 6. Verdict on the two R5 questions

- **Does the gate bite?** No. delta_0 = 0 at the primary decision point, exactly, with an explicit verified witness; stable under every pre-registered scan and under my harsher probes. Not "inconclusive": the base-optimal law itself satisfies the full cubic block, and at the flat/flat configuration the equality is analytically airtight for the atom-only class.
- **Is the absorption publishable as the sharpened no-go?** Yes, with the three MAJOR qualifications: (i) state the exact zero as flat/flat-specific with the O(1e-4)-bounded window/pinning residuals; (ii) promote a near-CUE witness to decision grade (converged Tier-2 + BGSTB24 fetch) before claiming robustness against the parent ceiling's own data class; (iii) scope the headline to the N_d benchmark or add the cheap p1-objective rerun. The absorption channel identification (position/interference freedom — grid decoupling + occupancy clustering; spectral escape capped at 2 sqrt2 sqrt(C_led eps) N, constant verified) is exactly the complement the adjudication predicted and is correct.

## 7. Consequences upstream (audited view)

- ACTION ONE is decided on the absorption branch; **do not invest in the R2 bridge for the cubic-certificate payoff** (the payoff is 0 at the proven operating point; the exploratory lambda' scan's small positive values live outside the proven ladder regime and are M5 contingent, correctly labeled).
- lemmaR_tight stands, strengthened: two-bandwidth flat-window augmentation (F' + signed cubic + all-V ladder + capacity fuzz at lambda' = 1/2) adds exactly zero at N = 64/128 scale — and the structural reason (c = 3F − 2; iso content = sum m(m−1)(m−2); cross-terms adversary-tunable) is now explicit and independently verified.
- Formalization queue: the grid Parseval identity + witness law are PairCeiling-shaped and genuinely formalizable (all row data become algebraic on the grid); this is the right next Lean target for the no-go.
- Flags carried, correctly: F1 (BGSTB24 — now blocking the near-CUE promotion, so it should move up the fetch queue), F2 (c3 identification — absorption-insensitive, verified), F4 (ladder/R2 — absorption is strengthened by assuming it; nothing here depends on R2).
