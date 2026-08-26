# D1 / D-R5: the lambda-ladder cost curve for the DH Weil-form stack

**Date:** 2026-08-26 (Session 6, computational lead, D1 arm).
**Mandate:** repair D-R5 of `directions/D1-certified-refutation-arm.md` — publish the
λ-ladder cost curve BEFORE funding the M0(i) DH crash hunt at λ ∈ [11, 13]
(μ = λ² ∈ [121, 169]), with the explicit failure branch (certified lower bound on the
crash support λ_c + escalation gate) if infeasible.
**Machine:** MacBook Mac16,10 (Apple-Silicon M-class), 10 cores, 24 GB; thermal policy
4 concurrent processes max. **Software:** Python 3.9.6, mpmath 1.3.0 on the
**pure-Python backend** — `gmpy2` NOT installed, `python-flint` (Arb) NOT installed
(both verified this session; nothing was installed).
**Raw data:** `lambda-ladder-cost-curve.json` (29 measured rungs + micro-benchmarks +
iv sample, all from this session). **Runner:** `lambda_ladder_runner.py`,
`micro_bench.py` (fit: `lambda_ladder_analyze.py`; iv sample: `iv_overhead_sample.py`).
Stack under test: `results/ccm-dh-test/weilform.py` (`build_matrix(λ, N, 'dh')` →
`parity_blocks` → `mp.eigsy`), conventions triple-validated in Sessions 4–6.

---

## 1. What actually drives the cost (read from the code, then measured)

The brief's background line "prime sums whose length grows exponentially in λ" is
**not what the code does**: `build_matrix` cuts the coefficient sum at
`nmax = floor(λ²)` (the autocorrelation test class on [1/λ, λ] has support [1/λ², λ²],
so the cutoff λ² is *complete*, not a truncation). At λ = 13 that is 123 nonzero
Λ_DH terms with max |Λ_DH(n)| = 6.78 — the coefficient recursion costs ≤ 0.007 s and
the prime sums are invisible in the profile (builds at fixed N = 64:
λ = 3 → 3.56 s, λ = 8 → 3.76 s, λ = 13 → 3.93 s). The exponential in the problem
lives in the **precision demand of the null branch** (ε ~ e^{−4πμ/5}), not in
enumeration. The measured cost drivers, comparable at production size:

1. **Matrix build:** ~N·(N+10)·K(dps) transcendental mpmath evals,
   K = max(30, 0.8·dps) quadrature points per panel;
2. **Eigensolve:** `mp.eigsy` on the (N+1) even + N odd parity blocks, ~(N+1)³ mpf ops
   each, nearly precision-flat below 200 digits (mpf multiply is 0.72–0.99 µs from
   30 to 200 digits on this backend).

Memory is a non-issue: peak RSS 95 MB at the largest rung (N = 160); ≲ 0.5 GB
extrapolated at N = 200 / 200 digits. 4-wide batching fits trivially in 24 GB.

## 2. Measured ladder (kind='dh'; 29 rungs, wall seconds, single core each)

Selected rungs (full set in the JSON). `min_even` is the smallest even-block
eigenvalue — *indicative only where |min| is below the eigensolver's resolution at
that dps*; entries marked ✓law match the archived conductor-Fuchs DH fit
(`ln ε = 3.5069 − 2.6043 μ + 2.7101 ln μ`, `chi3-conductor-point.json`).

| λ | N | dps | build s | eig s (e+o) | total s | min_even |
|---|---|----|---------|-------------|---------|----------|
| 2 | 16 | 30 | 0.5 | 0.1 | 0.7 | 4.12e-2 |
| 3 | 32 | 30 | 1.2 | 0.9 | 2.0 | 7.79e-7 |
| 4 | 48 | 30 | 2.3 | 2.9 | 5.2 | 4.40e-14 ✓law (4.9e-14) |
| 5 | 64 | 30 | 3.7 | 6.2 | 10.0 | 1.594e-23 ✓law (1.0e-23) |
| 5.5 | 72 | 60 | 9.2 | 10.1 | 19.3 | **+5.52e-29** ✓law (2.1e-29) |
| 6 | 80 | 60 | 11.1 | 13.4 | 24.6 | **−6.039e-11** (= dps-30 value, digit-identical) |
| 6.5 | 88 | 30 | 6.5 | 15.0 | 21.6 | **−0.1447** |
| 7 | 96 | 30 | 7.8 | 19.4 | 27.2 | **−0.4413** |
| 8 | 64 | 30 | 3.8 | 5.4 | 9.2 | **−0.98913429050** |
| 8 | 64 | 60 | 7.7 | 6.7 | 14.3 | **−0.98913429050** (digit-identical) |
| 9 | 112 | 30 | 10.6 | 28.7 | 39.4 | **−1.2531** |
| 11 | 128 | 30 | 13.4 | 40.3 | 53.9 | **−1.5998** |
| 13 | 128 | 30 | 13.3 | 37.6 | 51.1 | **−2.05578** |
| 13 | 128 | 60 | 27.7 | 44.9 | 72.7 | **−2.05578214508** (min_odd −2.0205) |
| 13 | 160 | 30 | 20.2 | 75.3 | 95.8 | −2.05832 (N-saturation: 0.12% vs N=128) |
| 13 | 32 | 100/150/200 | 6.8/14.0/23.6 | 0.8/0.9/1.0 | 7.6/14.9/24.7 | 4.252160e-58, bit-identical at all three dps |
| 5 | 64 | 100/150/200 | 18.7/36.8/60.0 | 9.4/10.1/11.1 | 28.1/46.9/71.2 | 1.5937672e-23, identical at all three dps |

Precision-stability of the instrument is directly demonstrated: minima are
digit-identical across dps 30→60 (λ = 3, 5, 6, 8, 9, 13) and dps 100→200 (λ = 13,
N = 32), and the positive branch reproduces the archived law within prefactor
scatter at every overlapping point.

## 3. The fitted cost law

With t_sin(dps) the measured per-call mpmath sine cost (3.70 / 5.11 / 7.75 / 11.48 /
14.88 / 26.46 µs at 30 / 60 / 100 / 150 / 200 / 300 digits — between linear and
quasilinear in digits on this backend, exponent ≈ 0.75 over 30–300):

- **t_build [s] ≈ N·(N+10)·K(dps) · (5.4 + 6.1·t_sin(dps)) × 10⁻⁶**, K = max(30, 0.8·dps)
- **t_eig(both parities) [s] ≈ 2·(N+1)³ · (10.3 + 0.039·dps) × 10⁻⁶**
- coefficient recursion, parity split, packet evaluation: negligible (< 0.5 s total).

The model reproduces all 29 measured rungs within a factor **[0.65, 1.22]**
(most within ±15%); quote extrapolations with **±35%** honest error bars.
Cost is polynomial throughout: ~N²·dps^1.75 (build) + N³ (eig). No wall exists
below several hundred digits — a hypothetical λ = 20 / dps = 460 / N = 200 rung
extrapolates to ~70 min, still one lunch.

## 4. Extrapolation to the D-R5 production points (with ±35% bars)

N = 200 is the conservative basis size (packet center n₀ = t₀L/2π ≈ 65–70 at
λ = 11–13, so N = 128 already expresses the crash mode; N = 160 changed the λ = 13
minimum by 0.12%). "Certified" = interval-arithmetic build (×3.4 measured) + float
eigensolve as pointer + certified iv quadratic form (0.06 s at N = 128).

| production point | N=128 float | N=200 float | N=200 certified-witness |
|---|---|---|---|
| λ = 11, 150 digits | 3.8 min | **10.7 min** | 26 min |
| λ = 12, 175 digits | 4.8 min | **13.0 min** | 33 min |
| λ = 13, 200 digits | 5.8 min | **15.6 min** | 41 min |

Full 21-rung sweep of λ ∈ [11, 13] at Δλ = 0.1, N = 200, null-branch precision:
**≈ 4.6 h sequential, ≈ 1.2 h at the 4-wide thermal policy.** Precision check
(recomputed this session from the fitted law): null-branch ε at μ = 121/144/169 is
10^−130 / 10^−156 / 10^−184, so dps 150/175/200 resolves λ ≤ 12.6 and **λ = 13
honestly wants dps ≈ 210–220** (+ ~10% cost — included in the error bars). On the
realized branch (below) none of this precision is needed.

**Interval overhead, measured on a sample rung** (λ = 13, N = 128, dps = 60 kernel:
6624-node quadrature sum): iv/float = **3.4×** (micro factors: sin 2.9–3.7×,
exp 1.8–2.1×, mul 2.3–2.5×); the iv enclosure width was 1.06e-57 — millions of times
tighter than the −2.06 signal requires. mpmath.iv has no eigensolver: the certified
path is float-eig-as-pointer + iv re-evaluation of v†Tv on the extracted
eigenvector v (variationally valid: any test vector bounds the minimum from above).

## 5. VERDICT (D-R5 classification): **yes-this-machine**

The λ ∈ [11, 13] hunt at full null-branch precision (150–200 digits, N = 200) costs
**hours, not days**, on this machine under the existing thermal policy. No
escalation gate is required for M0(i).

### 5a. Reconnaissance carried by the ladder itself (indicative, NOT certified)

The cost rungs double as a low-precision scan, and they show the hunt terminating on
the cheap branch:

- **The DH Weil form is already indefinite far below the [11,13] window.** Macroscopic
  negative minima: −0.145 (λ=6.5), −0.441 (7), −0.989 (8), −1.253 (9), −1.600 (11),
  −2.056 (13, both parities). Values are digit-identical at dps 30 vs 60 — far above
  any numerical floor.
- **Crash-onset bracket: λ_c ∈ (5.5, 6.0]** (μ_c ∈ (30.25, 36]): λ = 5.5 is positive
  exactly on the conductor-Fuchs law (+5.5e-29 vs predicted 2.1e-29); λ = 6 is
  negative (−6.04e-11, dps-stable 30→60).
- **The crashed mode localizes exactly at the off-line zero:** at λ = 8 the ground
  eigenvector peaks at index 56 vs packet prediction n₀ = 56.7, with 99.6% of its
  mass within ±12 of n₀ ↔ spectral height t ≈ 85.7 = Im ρ_DH. The detector fires
  end-to-end as designed.
- **The a-priori Gaussian packet is NOT a witness:** its Rayleigh quotient is +3.5 to
  +5.3 at every rung. The eigensolve is the finder; the extracted eigenvector is the
  witness payload for the certified W3-format evaluation.
- Implication for D-R5's own premise: the "spectrally visible only at μ ≳ 120"
  threshold is empirically pessimistic by ~4× in μ — it prices the *global null
  floor*, whereas the localized crash competes at O(1) scale. "Sign resolution past
  onset is macroscopic" is confirmed: dps 30 sees −0.99 at λ = 8. The production
  hunt should therefore run λ ∈ [5.5, 13] (21+ rungs, the low end refining λ_c at
  dps 60–100), at a total cost measured in tens of minutes for the negative branch,
  reserving the 150–200-digit rungs for null-branch *positivity certification*
  below onset (λ ≤ 5.5 needs only dps ≈ 40; the heavy precision is only needed if
  one insists on certifying the near-onset sliver λ ∈ (5.5, 6)).

These minima are float results at working precision, cross-validated across dps and
N but **not interval-certified**; certification is exactly the funded M0(i) step
(certified Q_DH < 0 by iv evaluation of the eigenvector quadratic form, priced above
at minutes per point).

## 6. Failure branch (stated per D-R5, though empirically not the realized branch)

If certification at production precision were to find NO negative minimum on
λ ∈ [11, 13] (i.e., the reconnaissance minima failed interval certification — not
expected given dps-stability margins of 10²⁶⁺), the deliverable converts to a
certified LOWER bound in the format:

> **λ_c > λ_max**, where λ_max is the largest rung with a certified positive-definite
> QW^{λ,N} (certified via interval Cholesky of Te and To — ~N³/3 iv multiplies
> ≈ 30–60 s at N = 200, new code ~days), stated as: "the truncated DH Weil form is
> certified positive definite on E_N for all λ ≤ λ_max at the stated N, dps; hence
> no Weil-negativity witness of bandwidth ≤ N and support ≤ λ_max exists."

Escalation gate, in order of cost (algorithmic, no new hardware; NONE needed for
[11, 13]):
1. **Install gmpy2** (one pip install, not executed per no-install discipline):
   mpmath switches backend automatically; ×3–10 on 150–300-digit transcendentals.
2. **Basis windowing:** restrict E_N to the packet band n ∈ [n₀−w, n₀+w] — any
   subspace still yields valid variational witnesses; dim drops from 201 to ~2w+1,
   killing the N³ eigsy term (~×10).
3. **Arb port (python-flint / acb):** rigorous ball arithmetic ~50–100× mpmath on
   transcendental kernels, and `acb_mat` eigen-enclosures replace the hand-rolled
   certification; verified NOT currently installed — a port is days of work and is
   the right vehicle for the eventual W3 certificate publication, not for the hunt.

## 7. Verification statement (standing order 5)

Every number above was computed or measured this session on this machine (29 rungs,
micro-benchmarks, iv sample — all in the JSON with per-phase timings). Cross-checks
against prior program artifacts: λ = 4, 5, 5.5 minima vs the archived DH
conductor-Fuchs fit (agree within prefactor scatter); λ = 3 minimum vs the archived
Session-4 ladder (7.48e-7 at N = 64 vs archived 7.56e-7 at N = 48 — consistent
saturation trend); the DH fit constants (a, c, b) read from
`chi3-conductor-point.json`; null-scale arithmetic at μ = 121/144/169 recomputed
here, agreeing with D-R5's 10^−131-at-μ=121 figure. Not verified/not claimed: the
negative minima are not interval-certified (Section 5a labels them indicative);
the CCM paper's own μ ≳ 120 visibility claim was not re-derived — only empirically
superseded. Network: not needed; nothing unreachable this task (D-R10: no entries).
