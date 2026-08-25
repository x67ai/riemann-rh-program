# A4 M2 decision gate — run report

**Program:** RH program, direction A4 (merged A2+A4 cubic-certificate direction, adjudicated survives-with-repairs 5.5, binding).
**Contract:** adjudication repairs R5 (gate re-specification) and R7 (fallback row system primary); full specification in `SPEC.md` (formulator); this file is the implementer's run report.
**Date:** 2026-08-26. **Machine:** shared MacBook (M5, 10-core); thermal policy <= 4 concurrent heavy processes respected throughout (all Monte Carlo and pricing pools ran 4-wide).
**Code:** `code/` (kernels.py, null_budgets.py, tier_a.py, dictionary.py, master_lp.py, column_gen.py, run_gate.py, report.py). **Raw outputs:** `runs/*.json`. **Machine-readable verdict:** `gate-result.json`. **Witness:** `witness_N64.json`.

---

## 1. Verdict

**ABSORPTION.** The corrected M2 gate does not bite. Over the entire pre-registered decision grid — mark alphabet W in {2, 3, 4, 6, 8}, ladder constant C_led in {10, 100, 1000}, tolerance knobs eps in {0.02, 0.05, 0.10} (extended to 0.002), fuzz modes {coupled, none, Gamma in {0.05, 0.10, 0.25}}, budget variants {matched-geometry, asymptotic}, error bars off/on, N = 64 and N = 128 — the marginal value of the entire cubic block (signed cubic equality row + all-V count ladder + garnish-capacity fuzz row) is

    delta_0 = P_full - P_base = 0    (|delta_0| < 1e-12 at every one of the 940 grid records; LP duality gap ~ 1e-9),

and the joint-LP optimum equals the two-moment (lemmaR_tight) baseline exactly:

    P(eps) = 5/6 - (2/3) eps        (exact, asymptotic budgets, every eps down to 0.002; -> 5/6 as eps -> 0).

An explicit absorbing law (Section 5) satisfies every Tier-1 row at centered budgets with E[N_d]/N = 0.80510 <= 5/6 + 0.01 at the primary decision point, and the absorption is stable under budget re-centering (asymptotic variant) and under N = 64 -> 128 (P = 0.80245 matched / 0.80000 asymptotic at eps = 0.05, delta_0 = 0 at all 40 N=128 records). Under the SPEC 5.4 pre-registered rules this is the ABSORPTION branch, with no "inconclusive" hedge needed: delta_0 is identically zero (the base-optimal law itself satisfies the full cubic block), not merely zero within error bars.

**Deliverable meaning (per the binding merge guidance, item 3):** the sharpened no-go — *the bandwidth-one ceiling is robust under Rudnick–Sarnak-range cubic augmentation with capacity control* — now has an explicit, hand-checkable witness family, and the absorption channel is identified: **position/interference freedom (grid decoupling + occupancy clustering), not spectral escape** (spectral escape is capped at 2*sqrt(2)*sqrt(C_led*eps_g)*N — re-derived and LP-confirmed here, Tier A). This is exactly the complement the adjudication predicted: "any future no-go must exploit position/interference freedom, not spectral escape."

---

## 2. Why the absorption happens: the grid-decoupling mechanism

The witness lives on the **psi_1-zero grid**: the 65 sites of spacing 64/65 on the circle of circumference N = 64. Two exact facts (both re-derived by hand and verified numerically to 1e-12):

1. **The lambda = 1 Frobenius row degenerates to the isolated-block count on the grid.** The flat bandwidth-one kernel at N = 64 has 65 harmonics; on the 65-site grid, Parseval telescoping over the 65-periodicity of the form factor gives

       tr G_1^2 = sum_z m_z^2   EXACTLY,

   for EVERY marked configuration supported on the grid (any site subset, any marks). Equivalently: all pairwise differences are zeros of psi_1, so the lambda = 1 reading sees only multiplicities, never positions. The lemmaR_tight extremal analysis then transfers verbatim: min N_d subject to tr = N, tr G_1^2 = (4/3)N(1 +/- eps) over grid configurations is 5/6 - (2/3)eps, attained with marks {1, 2}.

2. **The lambda' = 1/2 kernel is alive on the same grid.** Its 33 harmonics are not aliasing-aligned to the 65-grid, so the sub-grid arrangement (which sites, which marks, which clusters) freely tunes the lambda' Frobenius and cubic cross-terms. The occupancy-2 cross-term background (referee major-2; 54% of the Frobenius budget, 80% of the cubic budget at lambda' = 1/2 — reproduced by the null MC as 52.6% / 79.0% at n = 64) is exactly the freedom the adversary uses: clustered doubles-subsets generate the cubic cross-terms needed to meet the c_3 equality at zero cost in N_d and zero cost at lambda = 1.

**Continuum honesty.** This is not a finite-N artifact. The continuum analog is the mean-gap integer lattice under the bandwidth-one sinc kernel (sinc(pi k) = 0 for k != 0 — the classical "adversary lattice" of the campaign record): tr G_1^2 = sum m^2 (1 + o(1)) while psi_{1/2}(k) = sinc(pi k/2) = 2/(pi k) (odd k) keeps the half-band kernel alive on the lattice. The finite-N grid (spacing 64/65 instead of 1) is the periodized version, where the identity is exact rather than asymptotic.

**Relation to SPEC 1.2.** The spec's isolated-block identity (c = 3F - 2 on pairs at every depth; c = 3F - 2 + (m-1)(m-2) on atoms) already located ALL discriminating power of the cubic row in marks >= 3 and clustering cross-terms. The gate's outcome sharpens this: with position freedom, the clustering cross-terms are a free resource for the adversary rather than a signal for the certificate — the cubic budget is met by arrangement, not paid for in multiplicity structure. The witness uses marks {1, 2} only; no pairs, no marks >= 3, no spectral escape.

---

## 3. Sanity gates (all passed; standing order 5)

* **Sine moments, own sampler** (independent implementation and seeds from the formulator's verify suite): CUE MC at bandwidth 1 gives m_2(1) = 1.33383(114), m_3(1) = 2.00255(396) at n = 256 (n = 512 consistent) against 4/3 and 2. At lambda' = 1/2: 1/n extrapolation of the MC gives m_2 -> 2.16682(52) vs 13/6 = 2.16667 and m_3 -> 5.00056(311) vs 5 (closed forms m2 = 1/lam + lam/3, m3 = 1 + 1/lam^2, which also reproduce the formulator's quadrature). Anchor halt-check passed (largest-n MC within envelope; extrapolation within 2.5 SE).
* **Block laws from my own builder:** isolated atom of mark m -> eigenvalue m, Frobenius m^2, cubic m^3 (exact to 1e-15); isolated pair at dimensionless depth w -> eigenvalues m(1 +/- A'(w)) with A'(w) = sum_j u_j cosh(4 pi j d/N) (matched-geometry discrete A'; deviation from continuum sinh(w)/w is the finite-N window effect), cubic charge 2 m^3 (1 + 3 A'^2), position-independent to 1e-15.
* **Shallow-pair continuity (adjudication block-continuity):** w = 1/64 pair -> eigenvalues (-4.3e-5, +2.000043), cubic charge +8.0005 -> the double's +8. NOTE (also flagged in SPEC 1.2): the task brief's "+8 vs 0" for doubles-vs-tight-pairs is the superseded phase-model heuristic; under the exact Prop 4.1 block law the pair cubic charge is 2m^3(1+3A'^2) >= 8 m^3 at every depth (c = 3F - 2 per zero exactly), so isolated pairs are on the SAME affine plane as doubles and the cubic row is blind to them — consistent with, and sharpening, the mimicry finding.
* **Eig-vs-Fourier consistency:** every dictionary column asserts |eig-moments - Fourier-trace rows| < 1e-8 relative (typical 1e-15); inertia n_- <= p asserted per column; no violations in ~1400 columns generated across all runs.
* **ppp resonance constant:** re-sieved independently to 3e6: sum_p (log p)^3/(p-1)^2 = 2.315762 (matches adjudication and formulator).
* **Fuzz capacity constant:** re-derived analytically by hand (min-profile optimum: value 2*sqrt(2)*sqrt(C_led*eps_g), truncation tail 3/h_max) and LP-confirmed: 2.8244 at h_max = 400 vs 2*sqrt(2) = 2.8284 (gap = tail, as predicted). The SPEC F6 correction of the adjudicator's 2*sqrt(C eps) and the earlier 5/sqrt(3) is confirmed a third time.
* **Tier-A regressions (exact-rational simplex):** (i) lambda = 1 affine degeneracy: min N_d = 5/6 exactly, with and without the cubic row (G(1) = 0, the designer's 2 = 2); (ii) K1-as-written vacuity reproduced (garnish at divergent h0 satisfies every stated row at Frobenius cost 4/(3 h0) -> 0); (iii) ladder squeeze reproduced (single-height cap sqrt(eps C_led), sharp multi-height 2 sqrt 2 sqrt(C_led eps) << 4/3 as eps -> 0); (iv) lambda' iso-block LP: W = 2 infeasible (iso cubic max 4 < 5), W >= 3 feasible with min N_d dropping to ~0.48 — demonstrating why the abstract no-cross-term harness has no decision authority (SPEC 4.4).
* **Calibration (SPEC 5.1):** with the cubic block AND lambda'-Frobenius removed, the LP reproduces the lemmaR_tight corner exactly: at asymptotic budgets P_cal(eps) = 5/6 - (2/3)eps with the extremal law {2/3 x simples-lattice + 1/3 x doubles-lattice} (= 2/3 simple + 1/6 doubles per zero); the CUE null columns are feasible at centered budgets.

---

## 4. The runs and the numbers

### 4.1 Null model (SPEC 2; `runs/budgets_lam0p5.json`)

CUE eigenangles via QR-with-phase-fix of complex Ginibre, unfolded to circumference n; same row code path as every dictionary column. R adaptive to SE(m3) <= 0.5%; batch-means SE with jackknife check (agreement to <10% throughout).

| n | R | m2(lambda=1) | m2(1/2) | m3(1/2) |
|---|---|---|---|---|
| 64 (matched) | 4000 | 1.32363(74) | 2.11087(63) | 4.75867(362) |
| 128 (matched) | 2000 | 1.32867(77) | 2.13845(71) | 4.87769(411) |
| 256 | 600 | 1.33115(66) | 2.15231(63) | 4.93758(373) |
| 512 | 300 | 1.33199(86) | 2.15958(67) | 4.96843(413) |
| 1024 | 120 | 1.33364(110) | 2.16362(83) | 4.98715(476) |
| 2048 | 48 | 1.33400(94) | 2.16505(83) | 4.99323(504) |
| 1/n fit -> inf | | 1.33394(63) | 2.16682(52) | 5.00056(311) |
| closed form | | 4/3 | 13/6 | 5 |

Ladder feasibility floor of the null (matched n = 64): E[n(V)]/n = [0.2387, 0.0136, 0, ...] on V = [2, 3, 4, ...]; C_led^min = 3.82 (3.91 at n = 128); max |eig| over 4000 draws: 3.98. The scan grid C_led in {10, 100, 1000} = {max(10, 2 C_led^min), 100, 1000} per SPEC.

### 4.2 Tier B decision LP (SPEC 4.1/4.2/5; `runs/scans_N64.json`, `runs/tighteps_N64.json`, `runs/scans_N128.json`)

Master LP over explicit marked configurations (law variables w_c, coupled fuzz variable g), column generation with analytic-gradient multi-start pricing (gradient verified against finite differences to 5.6e-9), discrete mark/depth/pair moves, dedup by configuration key, per-column consistency asserts. Final solutions re-verified in Fraction arithmetic on 1e-12 rationalizations of the row data (all checks pass; fuzz tangent-relaxation gap reported and < 3e-6 of budget).

**Primary decision point** (flat/flat, lambda' = 1/2, N = 64, matched budgets, eps = 0.05, C_led = 100, coupled fuzz):

    P_full = P_base = 0.80510,   delta_0 = 0   (identical optimal laws),
    g* = 1.5e-4 (coupled fuzz used: cubic slack 22.1 = 7% of budget at Frobenius cost 0.0095 —
    the SPEC 4.2 honest-effectivity warning quantified); at fuzz = none the SAME P is attained
    (the fuzz row is not load-bearing for the absorption).

**Whole grid (N = 64):** 900 records (2 budget variants x 5 W x 3 C_led x 3 eps x 5 fuzz modes x bars on/off): delta_0 = 0 at every record (max |delta_0| < 1e-12); no infeasibility anywhere. P depends only on (budget variant, eps): P = P_cal at every record — **even the lambda'-Frobenius row alone adds nothing to the two-moment baseline** (P_base = P_cal; the SPEC 5.1 contingency "if the lambda'-Frobenius row alone moves the baseline off 5/6" is answered: it does not).

**eps -> 0 drill** (beyond-SPEC trend points, labeled; `runs/tighteps_N64.json`):

| eps | P (asymptotic budgets) | 5/6 - (2/3)eps | delta_0 |
|---|---|---|---|
| 0.02 | 0.8200000 | 0.8200000 | < 3e-13 |
| 0.01 | 0.8266667 | 0.8266667 | < 3e-13 |
| 0.005 | 0.8300000 | 0.8300000 | < 3e-13 |
| 0.002 | 0.8320000 | 0.8320000 | < 4e-13 |

The exact law P(eps) = 5/6 - (2/3) eps is the grid-decoupled lemmaR_tight corner; the limit is 5/6 exactly. Matched-variant values differ only through the finite-size budget center (e.g. 0.83686 at eps = 0.002, from B1 = 84.71 < (4/3)64).

**W-scaling (SPEC 5.3):** delta_0(W) = 0 for W = 2, 3, 4, 6, 8 identically; the fit delta_0(W) = delta_inf + c W^-kappa degenerates to delta_inf = 0 with zero residual. The sprinkling question is moot: the absorbing law needs only marks {1, 2} (it is inside every W-class), so enlarging W cannot restore a bite.

**Gamma-slope (SPEC 4.2):** delta_0(Gamma) = 0 at Gamma in {0, 0.05, 0.10, 0.25}; d delta_0 / d Gamma = 0. (The parametric fuzz only adds slack to a row that is already non-binding.)

**Ladder activity:** the ladder rows R-7 are never active at any optimum (the witness's spectra live below V = 4 except small n(2), n(3) counts far under C_led N V^-4); C_led-scan trivially stable. Bounded-height spectral escape is priced and blocked exactly as the adjudication's squeeze predicts (Tier A), and the absorber does not attempt it.

**Pricing verification (heuristic adversary-optimality):** no improving column (reduced cost < -1e-6) found in S = 200 restarts at the primary point and at the tightest asymptotic point, S = 100 at N = 128, S = 40 at each W-scan re-check. The ABSORPTION verdict does not rest on pricing optimality (the witness is exhibited and verified); pricing optimality is only the heuristic support for the exactness of delta_0 = 0 (the LP-over-dictionary equality P_full = P_base is exact for the accumulated dictionary regardless).

**N = 128 confirmation:** seed + colgen at the same anchors; P_full = P_base at all 40 records (matched 0.80245, asymptotic 0.80000 at eps = 0.05, both fuzz modes, bars on/off); delta_0 = 0 throughout.

### 4.3 Tier-2 diagnostic (near-CUE pinning; `runs/tier2_N64.json`)

Rows |E_w|c_j|^2 - j| <= tau2 for j = 1..63 added at lambda = 1 (the PairCeiling data class, edge row free). Not part of the primary verdict (SPEC 4.3; BGSTB24 flag F1).

| tau2 | eps | P_base^T2 | P_full^T2 | delta_0' |
|---|---|---|---|---|
| 4 | 0.05 | 0.81394 | 0.81522 | 1.3e-3 |
| 4 | 0.02 | 0.83026 | 0.83174 | 1.5e-3 |
| 1 | 0.05 | 0.833377 | 0.833377 | 0 |
| 1 | 0.02 | 0.836006 | 0.836012 | 6e-6 |

Convergence bar: the T2 pricing was still finding columns of reduced cost -2.9e-4 at the final S = 120 verification, so the small positive tau2 = 4 values carry a ~3e-4 heuristic-convergence uncertainty and are upper bounds on the converged delta_0'. Annotation (SPEC 5.4): at tight pinning (tau2 = 1) the near-CUE-pinned baseline lands essentially exactly at 5/6 (0.833377 at eps = 0.05) and the cubic row adds nothing even there — i.e., the absorption does not depend on the witness's anti-correlated (non-CUE) bandwidth-one data: near-CUE laws absorb the cubic row as well. The no-go wording may therefore drop the "re-reading of linear pair data" hedge: there is no ceiling-class escape AND no bite even inside the near-CUE class at this scale.

### 4.4 Exploratory lambda' scan and window scans (secondary, labeled)

**Exploratory lambda' scan** (labeled: lambda' > 1/2 + o(1) is OUTSIDE the proven theta < 1 ladder regime — R4; these are M5 payoff-curve data, not certificate claims; colgen at reduced budget, so positive values are heuristic upper-anchored):

| lambda' | eps | P_base | P_full | delta_0 |
|---|---|---|---|---|
| 0.55 | 0.05 | 0.80533 | 0.80533 | 0 |
| 0.55 | 0.02 | 0.82518 | 0.82518 | 0 |
| 0.60 | 0.05 | 0.80585 | 0.80622 | +3.7e-4 |
| 0.60 | 0.02 | 0.82568 | 0.82596 | +2.8e-4 |
| 0.65 | 0.05 | 0.80595 | 0.80861 | +2.7e-3 |
| 0.65 | 0.02 | 0.82637 | 0.82788 | +1.5e-3 |

The pre-registered expectation SPEC 8.5 is confirmed quantitatively: the cubic row's marginal value turns positive between lambda' = 0.55 and 0.60 — precisely where the flat-window moment margin 2 m2 - m3 = 2/lam + 2 lam/3 - 1 - 1/lam^2 changes sign (lam ~ 0.61) — and grows toward lambda' = 2/3 (the RS-range endpoint). The M5 payoff curve is real but small at this scale (delta_0 ~ 2e-3 at 0.65), and consuming it requires the MD(lambda, delta) large-value progress that R4 quarantines: at the PROVEN operating point lambda' = 1/2 + o(1) the value is exactly zero.

**Window scans** (secondary; marginal value of the cubic block only, per SPEC 2.5; matched budgets re-sampled per combo):

| v1 | v' | eps | delta_0 |
|---|---|---|---|
| flat | cos(1.6 s) | 0.05 / 0.02 | 0 / 0 |
| cos(sqrt2 s) [MT] | flat | 0.05 / 0.02 | +6.4e-5 / +2.3e-5 |
| cos(sqrt2 s) [MT] | cos(1.6 s) | 0.05 / 0.02 | +6.3e-5 / +1.9e-5 |

Annotation: changing the lambda' window changes nothing (the absorber's freedom is positional, not spectral). Changing the lambda = 1 window to the Montgomery–Taylor cosine breaks the EXACT grid degeneracy (a cosine window's kernel zeros are not equally spaced, so no site grid kills all lambda = 1 cross-terms simultaneously), leaving a microscopic residual delta_0 ~ 6e-5 — three orders below the eps-slack scale and within pricing-convergence uncertainty, but of the expected sign. If anything survives of the cubic mechanism at bandwidth-one reading, it lives in non-flat lambda = 1 windows; at this scale it is negligible.

---

## 5. The witness (absorbing family; `witness_N64.json`)

Primary decision point (N = 64, matched budgets, eps = 0.05, fuzz = none). Three columns, ALL supported on the 65-site psi_1-zero grid (spacing 64/65 = 0.98462); marks {1, 2} only; no pairs; n_- = 0.

| weight | column | N_d | F1 (= sum m^2, exact) | F' | C' |
|---|---|---|---|---|---|
| 0.52999 | vacancy lattice: 64 simples on 64 of the 65 sites | 64 | 64 | 125.0909 (= 4128/33) | 245.4509 |
| 0.16040 | 16 doubles + 32 simples on an explicit 48-site subset | 48 | 96 | 153.7604 | 411.0865 |
| 0.30961 | 32 doubles on an explicit 32-site subset | 32 | 128 | 135.1959 | 301.3542 |

Law aggregates: E[F1] = 88.948 (= upper edge B1(1+eps)); E[F'] = 132.818 (inside [128.34, 141.85]); E[C'] = 289.327 (= lower edge B3(1-eps)); E[n(V)] far below every ladder cap; E[N_d]/N = 0.805096. Every row re-verified in Fraction arithmetic; the columns' row values re-computed from their clean integer grid descriptions agree to 4e-5 (optimizer position rounding; the grid description is the canonical witness). Site subsets are recorded in `witness_N64.json`.

Reading: the vacancy lattice (a maximally rigid, |c_s|^2 = 1 configuration) is the "cross-term sink"; the two doubles-subsets are the N_d-reducers, whose sub-grid clustering supplies the lambda' cubic cross-terms (C' = 411 and 301 against the isolated-block values 160 = 16*8 + 32 and 256 = 32*8). As eps -> 0 the law deforms continuously (tighteps runs) with N_d -> 5/6.

Structural note for the no-go paper: the witness family is a **law** (mixture), exactly as in the PairCeiling 256-law architecture; the formalization queue item is the same exact-rational LP + enclosure format with the two kernels evaluated on the grid (all row data become rational + values of psi' at grid multiples).

---

## 6. Deviations from SPEC (recorded per contract)

1. **Eigenvalue assembly**: spectra computed from the Hermitian frequency-domain matrix B[j,j'] = sqrt(u_j u_j') c_{j-j'} (2J+1 dimensions), which is exactly the alias-free tight-frame compression (d'' = 2J+1 windows), rather than literal d' = lambda N windows. Reason: at critical sampling the closed-band edge aliases (65 harmonics vs 64 windows at lambda = 1) and would break the exact eig-moments == trace-rows identity that the SPEC's single-code-path principle (1.4) requires; with B the identity is exact and is asserted per column. Derivation recorded in code docstring.
2. **Rational re-verification** is at 1e-12 rationalization of the (transcendental) kernel row data, not exact-rational end-to-end (Tier A is exact-rational; the PairCeiling-style exact formalization is the queued follow-up, for which the grid witness makes all data algebraic).
3. **Pricing budgets**: 200-restart stop rule applied at the decision-relevant points (primary, tightest-eps; 100 at N = 128); scan re-checks at S = 40; alternation rounds at S = 48. (SPEC asked S = 200 generally; reduced at non-decision points for compute budget — all reduced-S points show delta_0 = 0 by exact LP equality on the accumulated dictionary, so the reduction affects only the heuristic optimality claim, not the absorption.)
4. **Minimum atom separation** (1/8 gap) was NOT enforced in pricing (positions fully free — strictly adversary-favorable, subsuming the halving check); the witness's minimum gap is 0.985 anyway. Depth-grid halving check subsumed: the witness contains no pairs, and the depth grid was available to the pricer throughout.
5. **Window scans** reduced to 3 combos at reduced colgen budget (secondary per SPEC 2.5/6); exploratory lambda' budgets use trimmed MC sizes (to n = 1024).
6. **Tight-eps points** eps in {0.01, 0.005, 0.002} added beyond the SPEC grid (labeled) to exhibit the asymptotic limit.
7. **Tier-2** colgen not run to full convergence (diagnostic only; residual improving columns of -2.9e-4 documented above).
8. **MC realization counts** at large n stopped at the SE target (e.g. R = 48 at n = 2048), below the 5000 cap (adaptive per SPEC).

## 7. Flags carried (not discharged here; SPEC 10)

* F2: the identification c_3(lambda') = sine m_3(lambda') rests on RS96-range GUE 3-level correlations and the section-5 diagonal method's uniformity in the near-critical polylog window. The gate consumed the sine value with eps_3 tolerance; the ABSORPTION verdict is insensitive (a different c_3 center within O(1) moves nothing: the eps-scan and Gamma-scan bracket it).
* F4: the all-V ladder rests on Theorem 1(ii)-repaired, whose R2 bridge is unproven. Per SPEC gate semantics the absorption branch is STRENGTHENED by assuming the ladder (absorption even with the ladder); nothing here depends on R2.
* F1 (Tier 2 only): BGSTB24 open-band F(alpha) status — Tier 2 kept diagnostic.
* Heuristic adversary-optimality: the delta_0 = 0 equalities are exact LP facts over the accumulated dictionary with dual certificates; the claim that NO configuration class outside the discovered dictionary would create a bite is supported by the restart protocol only (and is anyway the anti-absorption direction: more columns can only lower P_full and P_base together).
* Finite scale: N = 64 and N = 128 only (verdict-stable across both, and the grid-decoupling mechanism has an exact continuum analog — Section 2 — so the absorption is not expected to reverse at larger N; N = 256 scale-up cost estimate: ~4x the N = 128 run with the same architecture).

## 8. What this changes upstream (for the direction file / STATUS)

* The M2 gate (ACTION ONE) is decided: **absorption**. Per the binding adjudication and merge guidance, the direction's deliverable on this branch is the sharpened no-go publication (bandwidth-one ceiling robust under RS-range cubic augmentation with capacity control), with: killer 1's garnish construction (as-written vacuity) + the adjudicator's squeeze (spectral escape capped — both reproduced in Tier A) + THIS gate's new content: the explicit grid-decoupled witness law showing the position/interference channel absorbs the cubic row even with the full repaired row system, even under near-CUE pinning, at delta_0 = 0 exactly.
* The R2 bridge investment decision that the gate was built to price: **do not invest for the cubic-certificate payoff** (the payoff is delta_0 = 0). Theorem 1(ii)-repaired retains its standalone value (first spectral-tail statement for the matrix) and its other consumers (partial orthonormalization; the HL*(4) shift-range observation) per merge guidance items (1) and (5).
* lemmaR_tight bookkeeping: the degeneracy is NOT broken; the program's map entry stands, now with a stronger statement: two-bandwidth flat-window augmentation (Frobenius' + signed cubic' + all-V ladder + capacity fuzz at lambda' = 1/2) adds exactly zero to the two-moment optimum at N = 64/128 scale.
* Formalization queue: the witness law + the grid Parseval identity are PairCeiling-shaped (exact-rational data on the grid); queue as the "cubic-augmentation robustness" extension of the ceiling library.
