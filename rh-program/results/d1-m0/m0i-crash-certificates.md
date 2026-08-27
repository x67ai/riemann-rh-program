# D1 M0(i): CERTIFIED Davenport-Heilbronn positivity-crash hunt

**Date:** 2026-08-26 (Session 7, computational lead, D1 arm; continuation of the
λ-ladder cost-curve reconnaissance in `lambda-ladder-cost-curve.md`).
**Mandate:** the M0(i) milestone of `directions/D1-certified-refutation-arm.md`
under repair D-R5's adopted rescope — certified negativity witnesses for the DH
Weil form, a certified upper bound on the crash support λ_c, the
baseline-departure record, and the μ ≳ 120 reconciliation.
**Machine:** MacBook Mac16,10 (Apple Silicon), Python 3.9.6, mpmath 1.3.0
pure-Python backend (no gmpy2, no Arb). Thermal policy: 4 concurrent processes.
**Stack under test:** `results/ccm-dh-test/weilform.py`
(`build_matrix(λ, N, 'dh')`), conventions triple-validated Sessions 4–6.
**Raw data:** `m0i-crash-certificates.json` (19 rungs with frozen witnesses,
certified intervals, decompositions, the zero scan, and the zero-side check).
**Scripts alongside:** `m0i_certify.py` (finder + iv certifier + analysis),
`m0i_dh_zeros.py`, `m0i_zeroside.py`, `m0i_aggregate.py`.

---

## 0. Scope discipline (state both, always)

1. **What this certifies:** the truncated Davenport–Heilbronn Weil quadratic
   form QW^{λ,N} is **not positive semidefinite at any support λ ≥ 5.55**
   (certified rungs listed below), on the autocorrelation/PSD test class on
   [1/λ, λ] in the Gram convention v†τv — the class and conventions repair
   D-R7 requires for witness format W3. The pole term of the explicit formula
   is handled per D-R7: the completed DH function is **entire, so no pole term
   exists to include** (the weilform stack includes the W₀,₂ pole row exactly
   for kind='zeta' and correctly omits it for 'dh'; docstring and Session-4–6
   validations in `results/ccm-dh-test/`). This is the M0 charter deliverable:
   the detector's end-to-end true-positive validation on a known RH-false
   object, and the computational prototype of witness W3.
2. **What this is NOT:** it is **not a statement about the Riemann zeta
   function, and not a Λ > 0 result.** The ζ-side W3 twin would additionally
   require the pole contribution h(±i/2); DH is the calibrated true-positive
   target only.

## 1. Certificate semantics

- **Finder** (untrusted): float mpmath eigensolve at dps 60 (`mp.eigsy` on the
  parity blocks; N = 128 throughout, one N = 160 robustness rung).
- **Witness freeze:** the ground eigenvector, unit 2-norm, rounded to **40
  decimal digits per entry**. The frozen decimal vector is the *exact* witness
  the certificate covers (any test vector bounds the minimum from above), and
  it is stored in full in the JSON for third-party re-verification.
- **Certifier** (the certificate): Q_DH(v) = v†τv and the Rayleigh quotient
  Q/(v,v) re-evaluated **from scratch in mpmath interval arithmetic at dps 60,
  directed rounding end-to-end**: λ as exact rational, L = 2 log λ, Λ_DH by
  the divisor recursion with κ from surd enclosures, prime sums, the
  archimedean composite Gauss–Legendre quadrature (M = N+10 panels × K = 48
  nodes), tail and constant terms, the O(N²) quadratic form, and the norm.
  `rayleigh_interval = [lo, hi]` with **hi < 0 certifies Q_DH(v) < 0**.
- **Quadrature-discretization rider:** the iv enclosure is rigorous for the
  stated finite quadrature rule; the rule's discretization error is controlled
  by the **grid-double rider** — the entire iv evaluation repeated on an
  independent, much finer rule (M = 200 panels × K = 64) at λ = 6.0 and
  λ = 8.0: certified centers shifted by **0.0 at the 30-digit record
  resolution** (i.e. < 1e-39 absolute at λ = 6, against a 1.9e-10 signal).
  The integrands are analytic on [0, L] (poles at Im y = ±π), so composite-GL
  convergence at panel width ~0.04 is superexponential; the rider measures it,
  no formal remainder theorem is claimed.

## 2. The certified ladder (all from this session's runs)

Rayleigh-quotient certified upper endpoints (hi), both parity sectors; iv
width column is the certified interval width; ~90–130 s iv build + <1 s
quadratic form per rung, 1.5–8.5 min wall per rung (positives skip the
certifier; grid-double rungs run it twice), 4-wide batches: 66 min total
process time, ≈ 20 min wall for all 19 rungs — far under the 1.5 h budget.

| λ | μ = λ² | certified even (hi) | certified odd (hi) | iv width |
|------|--------|----------------------|---------------------|----------|
| 5.55 | 30.80 | **−5.0020500e-30** | (odd +1.2e-25, recon) | 1.2e-57 |
| 5.6 | 31.36 | **−8.2153760e-30** | **−2.7950489e-27** | 1.0e-57 |
| 5.65 | 31.92 | **−2.2763718e-29** | **−1.7785394e-26** | 1.0e-57 |
| 5.7 | 32.49 | **−1.8616530e-23** | **−2.5168730e-26** | 2.4e-57 |
| 5.8 | 33.64 | **−1.2291330e-18** | **−8.1177889e-21** | 2.3e-57 |
| 5.9 | 34.81 | **−4.5342530e-16** | **−8.0115448e-16** | 3.5e-57 |
| 6.0 | 36.00 | **−1.9022707e-10** | **−4.9566087e-9** | 5.0e-57 |
| 6.25 | 39.06 | **−2.7990913e-4** | **−3.2578722e-3** | 8.0e-57 |
| 6.5 | 42.25 | **−0.15756790** | **−0.094876065** | 1.6e-56 |
| 7 | 49.00 | **−0.44567618** | **−0.39291526** | 1.7e-56 |
| 8 | 64.00 | **−1.0190002** | **−1.0159350** | 1.1e-56 |
| 9 | 81.00 | **−1.2540845** | **−1.2407500** | 1.4e-56 |
| 11 | 121.00 | **−1.5997803** | **−1.6173867** | 1.8e-56 |
| 13 | 169.00 | **−2.0557821** | **−2.0205113** | 2.2e-56 |

Full 30-digit two-endpoint intervals, witnesses, and timings in the JSON.
Instrument cross-checks: the λ = 13 finder minimum reproduces the archived
cost-curve value **digit-for-digit** (−2.05578214508); λ = 8 at N = 128
deepens the archived N = 64 value −0.98913 to −1.01900 (basis-monotone, as it
must); interval widths are 10²⁷–10⁵⁵ times smaller than the certified signals.

## 3. The certified upper bound on λ_c — and the onset bracket

**CERTIFIED: λ_c ≤ 5.55** (μ_c ≤ 30.8025) — the DH Weil form is not PSD at
support 5.55, witnessed by the even-sector certificate above. This tightens
the reconnaissance bracket λ_c ∈ (5.5, 6.0] by an order of magnitude in Δλ
and sharpens D-R5's original λ ∈ [11, 13] target window by a factor 3.9–5.5 in μ.

**The other side of the bracket (reconnaissance only, per the D-R5 failure
branch):** λ = 5.525 has float minimum **+7.49e-30** and λ = 5.5 has
**+4.07e-29** (N = 128, dps 60) — both *positive* and both on the
conductor-Fuchs law. Positivity is NOT certified: certifying the null branch
(interval Cholesky at collapse scale) is the expensive branch D-R5 prices
separately, and it is out of scope here. Stated per D-R5: at N = 128, dps 60,
the empirical onset sits in **λ_c ∈ (5.525, 5.55]**, μ_c ∈ (30.53, 30.80].
**Bandwidth robustness:** λ = 5.5 rerun at N = 160 stays positive
(+3.97e-29, a 2.4% drift from N = 128 — saturated); the E_N ladder is
monotone in N, so the certified bound can only improve with N, and at this λ
it has stopped moving.

## 4. The baseline-departure record (M0(i) deliverable)

Baseline: the archived DH conductor-Fuchs fit ln ε = 3.5069 − 2.6043 μ +
2.7101 ln μ (`chi3-conductor-point.json`, dh row; c ≈ 4π/5). Measured
min_even/ε_law approaching and crossing the onset (plot data in the JSON):

| λ | 5.0 | 5.25 | 5.5 | 5.5 (N160) | 5.525 | 5.55 | 5.6 | 5.65 | 5.7 | 6.0 |
|---|-----|------|-----|------------|-------|------|-----|------|-----|-----|
| min/ε_law | +1.30 | +1.40 | +1.94 | +1.89 | **+0.71** | **−0.96** | −6.4 | −73 | −2.5e8 | −1.8e25 |

The empirical shape of the departure:

- **Below onset the minimum rides the law** (ratio +1.3 to +1.9, inside the
  archived prefactor scatter), exactly as at the five fitted conductor points.
- **The first measurable departure is a *dip below* the law** (+0.71 at
  λ = 5.525): the off-line quadruple eats the margin before the sign flips.
  The ground-state decomposition (Section 6) shows this directly: at λ = 5.5
  the off-line term already cancels 70% of the on-line margin.
- **At the crossing the certified minimum equals minus the baseline scale**
  (−0.96·ε at λ = 5.55) — the signature of a level crossing, not of a new
  scale entering.
- **Past onset the departure is explosive but structured:** d ln|min|/dμ ≈
  +0.9 → +1.8 (5.55→5.65), then a jump of ~+24 per μ-unit into λ = 5.7 and
  ~+5 to +11 per μ-unit through λ = 6.0 (successive on-line prolate levels
  capitulating to the off-line coupling, not one smooth exponent), saturating
  toward the O(1) macroscopic minima by λ ≈ 6.5 and the slow deepening
  −0.16 → −2.06 across λ = 6.5 → 13.

## 5. Witness structure and the localization check

Is the certified negativity direction the off-line-zero packet? Two regimes,
one continuous mechanism (all decompositions in the JSON):

- **Source check — yes at every certified rung:** the zero-side decomposition
  Q(v) = S_on(v) + S_off(v) (S_off = the off-line quadruple's closed-form
  term; S_on := τ_e − S_off) gives **S_on(v) > 0 and S_off(v) < Q(v) < 0 at
  all 14 certified rungs** — the negativity is paid entirely by the off-line
  quadruple, with the on-line contribution positive throughout, e.g.
  λ = 6.25: −2.80e-4 = (+7.51e-3) + (−7.79e-3); λ = 13: −2.056 = (+0.113) +
  (−2.169).
- **Index-space localization — yes for λ ≥ 6.5:** witness argmax index vs
  packet prediction n₀ = t₀L/2π: 50/51.1 (6.5), 52/53.1 (7), 56/56.7 (8),
  59/59.9 (9), 66/65.4 (11), 71/70.0 (13), with 79–99% of witness mass within
  ±12 of n₀ and overlap 0.88–0.95 with the most-negative S_off direction p₁.
- **Near onset (5.55 ≤ λ ≤ 6.25) the witness is NOT the packet** — it is the
  low-frequency prolate (baseline) mode carrying a perturbative packet
  admixture: argmax at index 1–17, near-n₀ mass 1e-28 to 1e-2, overlap with
  p₁ = 1.3e-14 (5.55) → 1.7e-4 (6.0) → 0.097 (6.25) → 0.88 (6.5). The
  admixture is exactly consistent: S_off(v) ≈ −|ν₁|·overlap² to leading order
  (λ = 5.55: −0.682·(1.32e-14)² = −1.19e-28 = the measured S_off(v)). The
  crash onsets while the packet angle is still ~1e-14 **because the baseline
  floor ε is itself ~1e-29** — this is the reconciliation's core (next).
- **Parity note:** the onset certificate at 5.55 is even-sector (odd still
  positive there — the even-simple structure of Definition 5.3 holds *at* the
  onset); the odd sector crashes by 5.6 and is briefly the deeper sector
  (5.6–6.25), with even retaking the minimum from 6.5 on.

Convention validation (independent of the matrix build): for the λ = 8
witness, the explicit-formula zero side Σ 2|f̂(γ_j)|² over the 90 computed
on-line zeros (t ≤ 155) plus the quadruple term closes the matrix-side value
to **1.28%** (tail-limited, as expected at this cutoff), and the quadruple
term from the direct formula matches the matrix-path S_off to 11 digits
(`m0i_zeroside.py`, zeroside block of the JSON).

## 6. THE RECONCILIATION: μ ≳ 120 spectral visibility vs λ_c ≈ 5.54

The CCM verdict (`results/decisive-tests/ccm-dh-filter.json`) says the DH
off-line zero "becomes spectrally visible only at μ ≳ 120"; the certified
crash onsets at μ_c ≈ 30.7. Both numbers are now understood, measured, and
non-contradictory. Three findings:

**(i) The two statements price different functionals.** The μ ≳ 120 figure
prices *spectral resolution*: the D″/eigenvalue-ladder machinery exhibiting
the off-line zero as its own resolved feature against the on-line spectrum,
via the criterion [mode spacing π/log λ < mean on-line gap]. What crashes at
λ_c is the *minimum of the Weil form over the even test class* —
indefiniteness needs only ONE direction in which the off-line quadruple's
(sign-indefinite, analytically-continued) term outweighs that direction's
on-line leakage. By the Hurwitz argument the crash is mandatory at finite
support; its onset is a level-crossing against the collapsing baseline floor,
a strictly weaker event than resolution.

**(ii) The μ ≳ 120 number itself was built from a stale input.** This
session's scan of the actual DH on-line spectrum (90 zeros to t = 155,
`m0i_dh_zeros.py`) measures the mean gap near t = 85.7 as **1.662**, not the
verdict's recalled "~1.3". The verdict's own formula with the measured mean
gap gives λ ≥ e^{π/1.662} = 6.62, i.e. **μ_vis ≈ 43.8, not ~120**. Sharper:
the off-line zero sits mid-void in an anomalously wide on-line gap
(83.109 … 87.649, width 4.54 ≈ 2.7 mean gaps — the void that "holds" the two
missing on-line zeros of the quadruple), so the *local* resolution
requirement is set by the nearest-neighbor distance 1.95: λ ≥ e^{π/1.95} =
5.01, **μ ≥ 25.1**. The certified onset μ_c ∈ (30.53, 30.80] lands squarely
between the local-gap estimate (25.1) and the mean-gap estimate (43.8) — the
resolution physics is right once fed the true local zero configuration.

**(iii) The crossing estimate, done properly, predicts λ_c to 0.1%.** The
task's naive version — "baseline ε(μ) falls below the zero's coupling
strength" — FAILS if the coupling is taken at face value: the most-negative
eigenvalue of the off-line quadruple form S_off is O(1) (ν₁ = −0.66 at
λ = 5.5, measured), and ε < 0.66 already at μ ≈ 5 (λ ≈ 2.2), wildly early.
The coupling must be discounted by what the packet direction pays in on-line
leakage: the exact criterion (Schur complement of the rank-≤4 off-line
perturbation against the on-line form S_on' = S_on + S_off₊) is
**K_inv = max eig[(−S₋)^{1/2} S_on'⁻¹ (−S₋)^{1/2}] > 1 ⟺ indefinite.**
Measured K_inv(λ): 0.515 (5.0) → 0.677 (5.25) → 0.892 (5.5; 0.893 at N=160)
→ 0.959 (5.525) → **1.059 (5.55)** → 1.361 (5.6) → 2.99 (5.7) → 94.6 (6.0) →
4275 (6.25). Monotone, crossing 1 at **λ = 5.536** (log-interpolation) —
inside the certified bracket (5.525, 5.55], 0.04% below its midpoint. The
onset's razor sharpness is the same arithmetic: ε collapses like e^{−2.6μ}
while the discounted coupling varies slowly, so the crossing converts a
70%-eaten margin (λ = 5.5) into a certified negative in Δλ = 0.05.
(K_inv is float-grade and meaningful up to λ ≈ 6.25; past that S_on's
conditioning exceeds dps-60 resolution and the JSON flags it diagnostic-only.)
Depth's role: the off-line continuation weight λ^{2δ} (δ = 0.3085) is a
modest ×2.87 at onset — depth sets the coupling's scale, the *local gap*
sets where concentration becomes affordable, and the *baseline collapse
rate* (conductor-Fuchs) sets the crossing's sharpness.

**Residual honesty:** the CCM verdict's qualitative statement ("the
arithmetic-visible event lies far beyond both our range μ ≤ 14.44 and CCM's
own numerics μ ≤ 17") remains true and is now certified — the crash is at
μ_c ≈ 30.7, 2.1× beyond the verdict's probed range. Its quantitative "~120"
should be retired in favor of: **certified onset μ_c ∈ (30.53, 30.80];
resolution-model window [25, 44] once fed the measured local spectrum.** No
tension survives the measurement; nothing here was forced.

## 7. Verification statement (standing order 5)

Every number above is from this session's executed computations (19 rung
runs, the zero scan, the zero-side check; per-phase timings and peak RSS in
the JSON). Cross-checks: λ = 13 finder minimum digit-identical to the
archived cost-curve rung; λ = 5.0/5.25/5.5 minima on the archived
conductor-Fuchs law (ratios 1.3–1.9, prefactor-scatter grade); grid-double
certified shifts 0.0 at record resolution (λ = 6, 8); zero-side closure 1.28%
at λ = 8 with the S_off quadruple term matching the independent closed form
to 11 digits; the archived DH fit constants read from
`chi3-conductor-point.json` (not refit). NOT claimed: positivity certificates
below 5.55 (recon only); a formal quadrature-remainder theorem (measured
grid-double rider instead); K_inv rigor (analysis-grade float, exact-criterion
*formula*); any statement about ζ or Λ.
