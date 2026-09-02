# M2a item (b) — `Zeta23/DBN/BarrierCert.lean`: build record, axioms, and the displayed hypotheses

**Status:** DONE, 2026-09-02 19:12 IST (Session 14, D1 M2a Lean stream, workflow `d1-audit-m2a-s14`).
**Contract implemented:** `results/d1-m2a/SPEC.md` v1.0 — §7.1/§8.2 (data), §7.3/§8.2 (checker),
§8.1 (H2-B), §8.3 (`cert_of_checkBarrier`), §4.6 (the D-B1…D-B9 proof plan), §7.6 (split checker
facts). The Lean shapes of `lean-shapes-scratch.lean` §§B, D are realized verbatim (names, field
order, statement text); the scratch's `sorry` for `cert_of_checkBarrier` is discharged.
**Files:** working tree `~/rh-lean-work/zeta-23-lean-main/Zeta23/DBN/BarrierCert.lean` (1 092 lines)
= `rh-program/lean/Zeta23/DBN/BarrierCert.lean` (byte-identical, program header). Root import added
to `Zeta23.lean` (`import Zeta23.DBN.BarrierCert`, after `DBN.Defs`); `lake build Zeta23` succeeds.
Scratch (this directory, not program files): `barriercert-axioms-scratch.lean` + `.log`,
`barriercert-example-scratch.lean` + `.log`, `barriercert-build.log`.

## 1. The honest label (binding; D-R3/D-R8)

An accepted barrier certificate is **"kernel-checked modulo the displayed hypotheses H2-B and
`hHol` (producers untrusted)"**. Never "fully machine-checked". The kernel checks integer relations
on the literals (C-B0…C-B13, `decide +kernel`, no `native_decide`); it does not see t, f, or any
real number. The analytic content of the certificate — that nonvanishing at the seams plus the
E/D perturbation bounds imply nonvanishing on every prism — is **proved** in this module
(§3 below), not displayed: no Rouché theorem, no homotopy invariance and no zero-continuity in t
is used or assumed. What remains displayed is exactly the producers' enclosure claims (H2-B) and
the holomorphy of G t near R (`hHol`; for the instance, from H3's `HtEntire` and L-B3, the
Instance02 step).

## 2. Build record

`barriercert-build.log` (fresh build from deleted olean):

    # lake build Zeta23.DBN.BarrierCert — fresh build from deleted olean, 2026-09-02 19:12 IST
    # Lean (version 4.33.0-rc2, arm64-apple-darwin24.6.0, commit d8b18978…, Release); mathlib 51e6992efd
    ✔ [3147/3147] Built Zeta23.DBN.BarrierCert (3.2s)
    Build completed successfully (3147 jobs).

Zero errors, zero warnings (the first build had four errors — two `IsLocallyFiniteMeasure` metavariables
where the measure of `ContinuousOn.intervalIntegrable_of_Icc` had to be pinned to `volume`, and two
`linarith` failures from syntactically different atoms — and four deprecation warnings for
`Set.mem_setOf_eq` → `Set.mem_ofPred_eq`; all fixed at the second build). Then `lake build Zeta23`
(the root module, now importing `DBN.BarrierCert`): *Build completed successfully (9023 jobs)*, 16 s
for the root, only the two pre-existing upstream deprecation warnings in `XiPrime/FamilyHypsV.lean`.
`grep -n "sorry\|admit\|native_decide"` on the module: hits only inside the header comment
("all sorry-free", "no `native_decide`"). One `lake` process at a time throughout; the two scratch
runs were `lake env lean` on small files (light).

## 3. `#print axioms` — every theorem and lemma (`barriercert-axioms.log`, 28 declarations)

All 28 report a subset of `[propext, Classical.choice, Quot.sound]`; no `sorryAx`, no
`Lean.ofReduceBool`:

    sigma1_toW1, sigma2_toW1, T1_toW1, T2_toW1, W1Rect_toW1, W1Bdry_toW1   [propext, Classical.choice, Quot.sound]
    meshOK_of_checkPrismW1, checkPrism_spec, checkBarrierChain_spec         [propext]
    bdry_cover_gen, boundary_nonvanishing_gen, floor_of_meshOK              [propext, Classical.choice, Quot.sound]
    rectArgPrincipleGen                                                     [propext, Classical.choice, Quot.sound]
    bottom_seg_mem, right_seg_mem, top_seg_mem, left_seg_mem                [propext, Classical.choice, Quot.sound]
    continuousOn_logDeriv_seg, exclusion_of_checkPrismW1                    [propext, Classical.choice, Quot.sound]
    re_div_pos_of_norm_sub_lt                                               [propext, Classical.choice, Quot.sound]
    logDerivSegIntegral_div_add, logDerivSegIntegral_eq_log_sub, edge_decomp [propext, Classical.choice, Quot.sound]
    prism_nonvanishing, cover_prisms, seamTime_head_eq_zero                 [propext, Classical.choice, Quot.sound]
    cert_of_checkBarrier, cert_of_checkBarrier_xy                           [propext, Classical.choice, Quot.sound]

(The six `rfl` bridge lemmas report the three axioms because their *statements* mention ℝ, whose
construction depends on them; the three checker-unpacking lemmas are pure ℤ/Bool facts.)

## 4. The kernel-checked example (`barriercert-example-scratch.lean`, `.log`)

The SPEC §12 micro-example (ARTIFICIAL data, same literals as `lean-shapes-scratch.lean` §E) against
the built module, in `namespace Zeta23.DBN.M2aExample`: nine facts by `decide +kernel`, all
accepted by the kernel, `#print axioms` = `[propext]` or none:

| fact | kind | result |
|---|---|---|
| `exBarrier_chain : checkBarrierChain exBarrier = true` | C-B0 global, C-B2′, C-B13 | ✓ (no axioms) |
| `exPrism0_check`, `exPrism1_check : checkPrism exRect exPrism_i = true` | the per-module facts of SPEC §7.6 | ✓ `[propext]` |
| `exBarrier_check : checkBarrier exBarrier = true` | monolithic checker | ✓ `[propext]` |
| `exPrism0_bad_D` (D := 400) `= false` | negative control, C-B12 | ✓ |
| `exBarrier_bad_seam` (first seam 1/1) `= false` | negative control, C-B13 first seam | ✓ (no axioms) |
| `exBarrier_bad_t0` (t₀ := 1/20 = last seam) `= false` | negative control, C-B13 last seam < t₀ | ✓ (no axioms) |
| `exPrism1_bad_row` (a row whose Re AND Im intervals straddle 0) `= false` | negative control, C-B6 | ✓ |
| `exBarrier_prisms : ∀ p ∈ exBarrier.prisms, checkPrism exBarrier.rect p = true` | the split-form assembly from the two per-prism facts | ✓ |

plus an `example` instantiating `cert_of_checkBarrier` on `exBarrier` with the analytic hypotheses
as parameters (shape check only). **Recorded honestly:** my first version of the C-B6 negative
control used the row ⟨−40, 10, 280, 360, …⟩ and `decide` refuted the claimed `= false` — the box's
Im interval [280, 360] is clear of 0, so C-B6 correctly ACCEPTS it. The checker was right; the test
datum was wrong and was replaced by ⟨−40, 10, −5, 360, …⟩ (both intervals straddle 0). The log in
`barriercert-example.log` is the corrected run.

## 5. Exact statements of the displayed hypotheses (verbatim from the module)

**H2-B, per prism** (SPEC §8.1, unchanged):

    def PrismEnclOK (G : ℝ → ℂ → ℂ) (d : BarrierData) (p : PrismData) (τ' : ℝ) : Prop :=
      ∃ (U : Set ℂ) (f : ℂ → ℂ), IsOpen U ∧ BarrierRect d ⊆ U ∧ DifferentiableOn ℂ f U ∧
        List.Forall₂ (W1.RowEnclOK f p.K p.A) p.rows (W1.segs (toW1 d.rect p)) ∧
        (∀ z ∈ BarrierBdry d, ‖G (seamTime p) z - f z‖ ≤ (p.E : ℝ) / p.K) ∧
        (∀ t : ℝ, seamTime p ≤ t → t ≤ τ' →
          ∀ z ∈ BarrierBdry d, ‖G t z - G (seamTime p) z‖ ≤ (p.D : ℝ) / p.K)

**H2-B** (the displayed hypothesis; `nextSeams d = d.prisms.tail.map seamTime ++ [t0 d]`):

    def BarrierEnclOK (G : ℝ → ℂ → ℂ) (d : BarrierData) : Prop :=
      List.Forall₂ (PrismEnclOK G d) d.prisms (nextSeams d)

**`hHol`** (a hypothesis of the theorem, not a named Prop; for the instance it is discharged from
H3's `HtEntire` + L-B3 in Instance02.lean):

    (hHol : ∀ t : ℝ, 0 ≤ t → t ≤ t0 d →
      ∃ U : Set ℂ, IsOpen U ∧ BarrierRect d ⊆ U ∧ DifferentiableOn ℂ (G t) U)

where `BarrierRect d = RectClosedOf d.rect = W1.rectClosed d.rect.x1 d.rect.x2 d.rect.y1 d.rect.y2`,
`BarrierBdry d = W1.rectBdry …` (the same four reals), `RectData.x1 r = (r.xn1 : ℝ) / r.xd1` etc.,
`seamTime p = (p.tn : ℝ) / p.td`, `t0 d = (d.t0n : ℝ) / d.t0d`. `W1.RowEnclOK` and `W1.segs` are the
M1 v1 definitions, unchanged (`W1/Soundness.lean`); `toW1 d.rect p` is the seam transcript as a
`W1.W1Data` with `m := 0`.

**The soundness theorem** (SPEC §8.3, verbatim shape):

    theorem cert_of_checkBarrier (G : ℝ → ℂ → ℂ) (d : BarrierData)
        (hchain : checkBarrierChain d = true)
        (hprisms : ∀ p ∈ d.prisms, checkPrism d.rect p = true)
        (hHol : ∀ t : ℝ, 0 ≤ t → t ≤ t0 d →
          ∃ U : Set ℂ, IsOpen U ∧ BarrierRect d ⊆ U ∧ DifferentiableOn ℂ (G t) U)
        (hEncl : BarrierEnclOK G d) :
        ∀ t : ℝ, 0 ≤ t → t ≤ t0 d → ∀ z ∈ BarrierRect d, G t z ≠ 0

**The bridge-shaped corollary** (added; the coordinate form `Polymath15Bridge`/`Polymath15Bridge'`
hypothesis (iii) consumes, for H = G·B — instance: H = `Ht`, B = `Bt`):

    theorem cert_of_checkBarrier_xy (H B : ℝ → ℂ → ℂ) (d : BarrierData)
        (hchain : checkBarrierChain d = true)
        (hprisms : ∀ p ∈ d.prisms, checkPrism d.rect p = true)
        (hHol : ∀ t : ℝ, 0 ≤ t → t ≤ t0 d →
          ∃ U : Set ℂ, IsOpen U ∧ BarrierRect d ⊆ U
            ∧ DifferentiableOn ℂ (fun z => H t z / B t z) U)
        (hEncl : BarrierEnclOK (fun t z => H t z / B t z) d) :
        ∀ x y : ℝ, d.rect.x1 ≤ x → x ≤ d.rect.x2 → d.rect.y1 ≤ y → y ≤ d.rect.y2 →
          ∀ t : ℝ, 0 ≤ t → t ≤ t0 d → H t (x + y * I) ≠ 0

No nonvanishing of B is needed for this direction (H = 0 forces H/B = 0 in Lean); B ≠ 0 near R is
what discharges `hHol` from the entirety of H in the instance (L-B3), and it is what makes the
producers' enclosures of G = H/B meaningful — that is H2-B's business, outside the theorem.

## 6. What is proved (the SPEC §4.6 chain, item by item) and how

| SPEC | Lean | how |
|---|---|---|
| L-B0 | `rectArgPrincipleGen` | W1's `RectArgPrinciple` restated for a general nondegenerate rectangle (no strip clauses); the proof is the nondegenerate branch of `rectArgPrinciple_of_local` (ArgPrincipleBridge.lean) verbatim, on the `_on` lemmas of that file |
| L-B0 (mesh refactor) | `MeshOK`, `meshOK_of_checkPrismW1`, `bdry_cover_gen`, `boundary_nonvanishing_gen`, `floor_of_meshOK` | `ChecksOK` minus hC2a/hC2c, with C2′ and m = 0; proofs copied from Soundness.lean §6/§11 with the structure renamed; nothing in `W1/` modified |
| D-B1 | `exclusion_of_checkPrismW1` | the `cert_of_checkW1` chain generic in f: f ≠ 0 on the closed rectangle AND the four-edge argument increment of f is 0 (the second clause is what D-B8 needs); the ζ-specific continuity lemma replaced by `continuousOn_logDeriv_seg` (from `DifferentiableOn` on an open set + nonvanishing; the integrability inputs are proved, no junk-value path) |
| D-B2 | `floor_of_meshOK` | D6, as in W1 |
| D-B3 | `re_div_pos_of_norm_sub_lt` + C-B12 cross-multiplied (`div_lt_div_iff₀`) | ‖g − f‖ < ‖f‖ ⟹ g ≠ 0 ∧ Re(g/f) > 0 |
| D-B4 | inside `prism_nonvanishing` | W := V ∩ (U ∩ f⁻¹'{≠0}), open by `ContinuousOn.isOpen_inter_preimage` |
| D-B5 = L-B2 | `logDerivSegIntegral_div_add` | pointwise `HasDerivAt.div` + `field_simp; ring`, then `intervalIntegral.integral_add` with both integrands continuous on [0,1] |
| D-B6 = L-B1 | `logDerivSegIntegral_eq_log_sub` | s ↦ Log h(γ(s)) has derivative (h′/h)(γ)·(w−z) on [0,1] by `HasDerivAt.scomp` + `HasDerivAt.clog_real` (right half-plane ⊂ `slitPlane`); `intervalIntegral.integral_eq_sub_of_hasDerivAt` |
| D-B7 | `ring`/`linarith` inside `prism_nonvanishing` | the four Log differences telescope on the closed traversal |
| D-B8 | `prism_nonvanishing` | L-B0 for g on V pins Z; the winding of g = winding of g/f (= 0, D-B7) + winding of f (= 0, D-B1) |
| D-B9 = L-B4 | `cover_prisms` + `seamTime_head_eq_zero` | list induction on the `Forall₂` of H2-B; only "first seam = 0" (C-B13's `firstOK (0,1)`) is a soundness input |

**Deviation from SPEC §4.6, recorded:** D-B5–D-B7 are applied to the four WHOLE edges, not to the
mesh segments — the per-segment additivity (W1's L1, `edge_sum_eq`) is needed only for f (whose
rows are per segment), so `segs` never enters the g side, and the telescoping (D-B7) is over four
terms, closed by `ring`. Same theorem, shorter proof; SPEC §4.6's text is not wrong, it is the
segment-level version of the same argument.

**Deviation recorded:** SPEC §4.6 D-B9 says "C-B13 … with W1's `cover_chain`". The proof uses
neither `cover_chain` nor the strict monotonicity of the seams: `cover_prisms` finds the prism by
walking the `Forall₂`, and only the first seam = 0 is consumed. C-B13's monotonicity and
"last seam < t₀" stay in the checker as reject-more checks (they keep a certificate honest — a
non-monotone chain would be accepted by soundness but would have to contain overlapping/empty
prisms whose D-clauses the producers must still discharge); they are not soundness inputs.

**Not touched, by design (out of item (b)'s scope):** `Defs.lean` v1.1 (SPEC §3.3–3.5:
`Polymath15Bridge'`, `Bt`, `HtEntire`), the asymptotic lane (`checkAsym`, `cert_of_checkAsym`,
SPEC §5/§8.3 — item (c) of the Lean stream), and `Instance02.lean`. `BarrierCert.lean` imports
`Zeta23.DBN.Defs` (unchanged, v1.0) and `Zeta23.W1.ArgPrincipleBridge`; it is generic in G and does
not mention `Ht`.

## 7. Contents of the module, in order

1. Data: `PrismData` (13 ℤ/list fields), `RectData` (8 ℤ), `BarrierData`, `toW1`, `seams`.
2. Checker: `checkPrismW1` (C-B0…C-B9 via W1's helpers on `toW1`), `checkPrism` (+ C-B0 seam,
   C-B11 floor, C-B12 gate), `checkBarrierChain` (C-B0 global, C-B2′, C-B13), `checkBarrier`.
3. Real reading + H2-B: `RectData.x1/x2/y1/y2`, `seamTime`, `t0`, `RectClosedOf`, `RectBdryOf`,
   `BarrierRect`, `BarrierBdry`, `nextSeams`, `PrismEnclOK`, `BarrierEnclOK`; six `rfl` bridges to
   W1's `sigma1/sigma2/T1/T2/W1Rect/W1Bdry` of `toW1`.
4. Checker unpacking: `MeshOK`, `meshOK_of_checkPrismW1`, `checkPrism_spec`, `checkBarrierChain_spec`.
5. L-B0 mesh chain: `bdry_cover_gen`, `boundary_nonvanishing_gen`, `floor_of_meshOK`.
6. L-B0: `rectArgPrincipleGen`.
7. Edge geometry: `bottom/right/top/left_seg_mem`, `continuousOn_logDeriv_seg`.
8. D-B1: `exclusion_of_checkPrismW1`.
9. D-B3: `re_div_pos_of_norm_sub_lt`.
10. L-B2, L-B1: `logDerivSegIntegral_div_add`, `logDerivSegIntegral_eq_log_sub`, `edge_decomp`.
11. D-B8: `prism_nonvanishing`.
12. D-B9 + soundness: `cover_prisms`, `seamTime_head_eq_zero`, `cert_of_checkBarrier`,
    `cert_of_checkBarrier_xy`.

## 8. Verification ledger (standing order 5)

* Every mathematical step is a Lean proof checked by the kernel (§3); nothing numeric is
  implemented in this module, so no bound is derived or quoted here — the bounds (E, D, floors)
  are the producers' and enter only through H2-B.
* Mathlib facts consumed, by name (all in Mathlib `51e6992e`): `HasDerivAt.clog_real`
  (`Mathlib/Analysis/SpecialFunctions/Complex/LogDeriv.lean:87`), `Complex.mem_slitPlane_iff`
  (`Analysis/Complex/Basic.lean:634`), `intervalIntegral.integral_eq_sub_of_hasDerivAt`
  (`MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean:1148`), `HasDerivAt.scomp`
  (`Analysis/Calculus/Deriv/Comp.lean:107`), `HasDerivAt.ofReal_comp` (`Analysis/Complex/RealDeriv.lean:102`),
  `ContinuousOn.isOpen_inter_preimage` (`Topology/ContinuousOn.lean:188`),
  `ContinuousOn.intervalIntegrable_of_Icc` (`IntervalIntegral/Basic.lean:506`),
  `intervalIntegral.integral_add` (ibid. 774), `HasDerivAt.div` (`Deriv/Inv.lean:173`),
  `Complex.abs_re_le_norm`, `div_sub_one`, `norm_div`, `isOpen_ne`, `Real.two_pi_pos`.
* Program facts consumed: `W1/Soundness.lean` (the mesh/segment vocabulary, `pin_m`, `sum_arg_encl`,
  `edge_sum_eq`, `tau_facts_inc/dec`, `mdist_sq_le`, …) and `W1/ArgPrincipleBridge.lean` (the `_on`
  argument principle, `Rect_cpt`, `RectFrontier_cpt`, `edge_sum_eq_rectIntegral`) — unchanged.
