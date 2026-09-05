# L-B3 — `Bt` holomorphic and nonvanishing near the instance rectangle (Session 16, 2026-09-06)

STATUS: IN PROGRESS.

## What L-B3 says (SPEC §3.4, §8.3)

SPEC §3.4: "for t ∈ ℝ and z … on an open neighborhood of any rectangle with y₁ > 0 and x₁ > 1: `Bt t` is
differentiable and nonvanishing (s = (1 − iz)/2 has Im s = −x/2 ≠ 0, so s ∉ (−∞, 1], both logs are off the
cut, exp ≠ 0, cpow of a positive base ≠ 0, s ≠ 0, s − 1 ≠ 0)."  The instance consumes it through `hHol` of
`row2_barrier_*_xy`: for every t ∈ [0, t₀] an open U ⊇ R with `fun z => Ht t z / Bt t z` differentiable on U.

## Plan (new file `Zeta23/DBN/BtFacts.lean`)

The mechanism in SPEC §3.4 is exactly right and needs only x ≠ 0 (not x₁ > 1, not y₁ > 0): with
s = (1 − iz)/2, Im s = −Re z / 2, so Re z ≠ 0 puts s, s/2 and s/(2π) in Mathlib's `slitPlane`
(`Complex.mem_slitPlane_iff : z ∈ slitPlane ↔ 0 < z.re ∨ z.im ≠ 0`), and gives s ≠ 0, s ≠ 1.
Then: `Complex.differentiableAt_log`/`DifferentiableAt.clog` for the two logs, `DifferentiableAt.const_cpow`
(base π ≠ 0) for π^{−s/2}, `DifferentiableAt.cexp` for the exponentials; nonvanishing from
`Complex.exp_ne_zero`, `Complex.cpow_eq_zero_iff` (base ≠ 0), `Real.sqrt_ne_zero'`, and s(s−1)/2 ≠ 0.
Statements, stronger than SPEC §3.4 asks (pointwise on the open set {z | Re z ≠ 0}, then specialized to
the open right half-plane, which contains every rectangle with x₁ > 0):

    theorem Bt_ne_zero (t : ℝ) {z : ℂ} (hz : z.re ≠ 0) : Bt t z ≠ 0
    theorem differentiableAt_Bt (t : ℝ) {z : ℂ} (hz : z.re ≠ 0) : DifferentiableAt ℂ (Bt t) z
    theorem isOpen_rightHalfPlane : IsOpen {z : ℂ | 0 < z.re}
    theorem differentiableOn_Ht_div_Bt (hEnt : HtEntire) (t : ℝ) :
        DifferentiableOn ℂ (fun z => Ht t z / Bt t z) {z : ℂ | 0 < z.re}

## Result: PROVED (first build, 2026-09-06)

File: `~/rh-lean-work/zeta-23-lean-main/Zeta23/DBN/BtFacts.lean` (new; imports `Zeta23.DBN.Defs`,
`Mathlib.Analysis.SpecialFunctions.Complex.LogDeriv`, `…Pow.Deriv`, `…ExpDeriv`).  No `sorry`, no new axioms,
no displayed hypothesis: `hBt` is NOT needed in the glue.  Effort: about 25 minutes of the 90-minute budget.

Contents (all theorems):
  * `im_half_one_sub_I_mul : ((1 - I * z) / 2).im = -z.re / 2`
  * `mem_slitPlane_of_im_ne_zero'`, `ne_zero_of_im_ne_zero`, `sub_one_ne_zero_of_im_ne_zero`,
    `half_im_ne_zero`, `div_two_pi_im_ne_zero` — the five side conditions of SPEC §3.4's mechanism
  * `differentiableAt_alpha`, `differentiableAt_M0`, `differentiableAt_Mt` (hypothesis `s.im ≠ 0`)
  * `M0_ne_zero`, `Mt_ne_zero` (hypothesis `s.im ≠ 0`)
  * `Bt_ne_zero (t) (hz : z.re ≠ 0) : Bt t z ≠ 0`                        — L-B3, nonvanishing
  * `differentiableAt_Bt (t) (hz : z.re ≠ 0) : DifferentiableAt ℂ (Bt t) z` — L-B3, holomorphy
  * `isOpen_rightHalfPlane : IsOpen {z : ℂ | 0 < z.re}`
  * `differentiableOn_Ht_div_Bt (hEnt : HtEntire) (t) : DifferentiableOn ℂ (fun z => Ht t z / Bt t z) {z | 0 < z.re}`

Mathlib lemmas that carried it (for the record): `Complex.mem_slitPlane_iff`, `DifferentiableAt.clog`,
`DifferentiableAt.const_cpow` (with `Or.inl (π ≠ 0)`), `DifferentiableAt.cexp`, `Complex.cpow_eq_zero_iff`,
`Complex.exp_ne_zero`, `Real.sqrt_ne_zero'`, `Complex.div_ofNat_im`, `Complex.div_ofReal_im`.

Build (`lake build Zeta23.DBN.BtFacts`, verbatim):

    ✔ [3141/3141] Built Zeta23.DBN.BtFacts (1.6s)
    Build completed successfully (3141 jobs).
    lake build Zeta23.DBN.BtFacts  2.17s user 2.11s system 125% cpu 3.405 total

`#print axioms` and `#check` (scratch `btfacts-axioms.lean` via `lake env lean`, verbatim):

    'Zeta23.DBN.Bt_ne_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.differentiableAt_Bt' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.isOpen_rightHalfPlane' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.differentiableOn_Ht_div_Bt' depends on axioms: [propext, Classical.choice, Quot.sound]
    Zeta23.DBN.Bt_ne_zero : ∀ (t : ℝ) {z : ℂ}, z.re ≠ 0 → Zeta23.DBN.Bt t z ≠ 0
    Zeta23.DBN.differentiableAt_Bt : ∀ (t : ℝ) {z : ℂ}, z.re ≠ 0 → DifferentiableAt ℂ (Zeta23.DBN.Bt t) z
    Zeta23.DBN.differentiableOn_Ht_div_Bt : Zeta23.DBN.HtEntire →
      ∀ (t : ℝ), DifferentiableOn ℂ (fun z => Zeta23.DBN.Ht t z / Zeta23.DBN.Bt t z) {z | 0 < z.re}

Deviation from SPEC §3.4's wording (recorded, no contract change): the hypothesis proved is `Re z ≠ 0`, not
"x₁ > 1, y₁ > 0"; it is strictly weaker (more general) and the instance rectangle (x₁ = X > 0) is covered by
the open right half-plane.  SPEC §3.4's fallback (display L-B3) is NOT exercised; §13.2's open item L-B3 closes.

STATUS: DONE (STEP 2) — L-B3 PROVED.
