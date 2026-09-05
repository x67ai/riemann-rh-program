# Independent audit of the M2a glue (Session 16, 2026-09-06) — `Defs.lean` v1.1, L-B3, `lambda_le_point2`

Auditor: Opus 5, D1/M2a, Session 16. Independent of the builder agent: every statement below was
re-read from the files on disk, every build and every `#print axioms` was re-run by the auditor in a
fresh scratch file, and no builder log was taken on trust.

Scope: RUN-REPORT §6 items 1, 2 and 4 as landed by the builder — `Zeta23/DBN/Defs.lean` v1.1,
`Zeta23/DBN/BtFacts.lean` (L-B3), `Zeta23/DBN/Instance02.lean` §2 (the glue), the copy-back to
`rh-program/lean/Zeta23/DBN/`, and the dated records in `lean/README.md`,
`directions/D1-certified-refutation-arm.md` and `results/d1-m0/m2a-m2b-design.md` §7.1.
Normative sources read for this audit: SPEC.md §1.1, §2.1, §3 (all), §6, §8, §9, §14; AUDIT.md F-5;
RUN-REPORT.md §6; design note §1.3, §7.

---

## §0. VERDICT — **REPAIRED-CLEAN-OWED**

**The mathematics, the Lean statements, the proof, the axioms, the instance parameters and the
copy-back are CLEAN.** Nothing in the trusted layer is wrong; nothing displayed is understated; no
`sorry`, no `native_decide`, no new axiom, no `hBt`. `lambda_le_point2` is exactly the SPEC §1.1
target in ray form, its four displayed hypotheses are exactly what the file says they are, and the
proof consumes the Lane B legs without strengthening them.

Three **documentation** repairs are OWED before this session is closed. None of them touches a
theorem, a proof, or a displayed hypothesis; each is applicable mechanically (exact strings in §5).

| # | severity | what | where |
|---|---|---|---|
| **R-1** | MEDIUM (trust vocabulary; the one place the builder's wording is permissive) | The claim that the short public sentence *"Λ ≤ 0.2 in ray form, kernel-checked modulo H1, H2, H3"* is "licensed with a gloss" is wrong: RUN-REPORT §6 item 4 gates that sentence on **item 3 (Lane A) as well**, and SPEC §6 defines H2 as `H2-B ∧ H2-A ∧ H-TAIL` behind a kernel-checked checker, of which only H2-B exists today. The sentence is **not licensed at all** yet, glossed or not. | `lean/README.md` line 144; `results/d1-m2a/v11/GLUE-NOTES.md` lines 101–103 |
| **R-2** | LOW (audit-surface accuracy) | Two docstrings in `BarrierCert.lean` still name the **removed** definition `Polymath15Bridge` and its hypothesis "(iii)". After Defs v1.1 that name does not exist; the clause consumed is (iii′) of `Polymath15Bridge'`. A reader of the trusted-adjacent layer is sent to a dangling name. | `Zeta23/DBN/BarrierCert.lean` lines 56 and 1065 (both trees) |
| **R-3** | LOW (SPEC erratum, append-only) | SPEC §3.4 states L-B3's hypothesis as *"z with Im z ≠ 0"*; its own parenthetical (`Im s = −x/2 ≠ 0`) shows the correct condition is **Re z ≠ 0**. The builder proved the correct (Re z ≠ 0) form; the SPEC text is the slip. SPEC §3.4 also places L-B3 in `BarrierCert.lean`; it landed in the new `BtFacts.lean`. | `results/d1-m2a/SPEC.md` §14 (append item 6) |

Consequence for the program's language, stated once and plainly:

> **Licensed today:** *"`lambda_le_point2` — every H_t with t ≥ 1/5 has only real zeros, i.e. Λ ≤ 0.2
> in ray form — is kernel-checked modulo the displayed hypotheses H1, H2-B, H2-A (in conclusion
> form, pending the Lane A checker) and H3; producers untrusted."*
> **Not licensed today:** *"…kernel-checked modulo H1, H2, H3"*, with or without a gloss. It becomes
> licensed when RUN-REPORT §6 item 3 lands and `hLaneA` is replaced by `cert_of_checkAsym`.
> Never "fully machine-checked". The Λ bracket of record stays 0 ≤ Λ ≤ 0.2.

---

## §1. Statement-faithfulness table

Every "SPEC says" cell was read from `results/d1-m2a/SPEC.md` this session; every "as landed" cell
from the file on disk and, where a shape is involved, from the auditor's own `#print` (§2.3).

### 1.1 The trusted layer, `Zeta23/DBN/Defs.lean` v1.1

| item | SPEC | as landed | verdict |
|---|---|---|---|
| `Polymath15Bridge` (v1.0, merged canopy) | §3.2–3.3: REMOVE, "do not keep both" | absent from `Zeta23/` except as a **comment** in the Defs deviation record and two stale docstrings (R-2). No declaration of that name exists | ✅ (R-2 is cosmetic) |
| `Polymath15Bridge'` — quantifier prefix | §3.3 `∀ t₀ X y₀ : ℝ, 0 < t₀ → 0 < X → 0 < y₀ → y₀ ≤ 1 →` | identical | ✅ |
| — hypothesis (i) | `ZeroVerification ((1 + y₀) / 2) (X / 2) →` | identical | ✅ |
| — hypothesis (ii′) | `(∀ x y : ℝ, X + 1 ≤ x → y₀ ≤ y → y ^ 2 ≤ 1 - 2 * t₀ → Ht t₀ (x + y * I) ≠ 0) →` | identical (auditor `#print`, §2.3) | ✅ region is `x ≥ X+1`, `y ≥ y₀`, `y² ≤ 1 − 2t₀`, **at t₀ only** |
| — hypothesis (iii′) | `(∀ x y : ℝ, X ≤ x → x ≤ X + 1 → y₀ ≤ y → y ≤ 1 → ∀ t : ℝ, 0 ≤ t → t ≤ t₀ → Ht t (x + y * I) ≠ 0) →` | identical | ✅ the box `[X, X+1] × [y₀,1] × [0,t₀]` |
| — conclusion (ray form) | `∀ t : ℝ, t₀ + y₀ ^ 2 / 2 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0` | identical | ✅ |
| derivation D-H3 still applies? | §3.3 | **re-derived independently by the auditor**, see §1.4 | ✅ sound; it does not even need the p3 simplified-region remark (see §1.4) |
| `alpha` | §3.4 = P15 (9) p4, second form | `1 / (2 * s) + 1 / (s - 1) + (1 / 2 : ℂ) * Complex.log (s / (2 * π))` | ✅ |
| `M0` | §3.4 = P15 (6) p4 | `(1/8 : ℂ) * (s * (s - 1) / 2) * (π : ℂ) ^ (-s / 2) * (Real.sqrt (2 * π) : ℂ) * Complex.exp ((s / 2 - 1 / 2) * Complex.log (s / 2) - s / 2)` | ✅ |
| `Mt` | §3.4 = P15 (10) p4 | `Complex.exp ((t : ℂ) / 4 * alpha s ^ 2) * M0 s` | ✅ |
| `Bt` | §3.4 = P15 (11) p4, `B_t(x+iy) = M_t((1+y−ix)/2)` | `Mt t ((1 - I * z) / 2)` | ✅ and `(1 − iz)/2 = (1 + y − ix)/2` for `z = x + iy` re-checked (`iz = ix − y`) |
| `HtEntire` | §3.5 | `∀ t : ℝ, Differentiable ℂ (Ht t)` | ✅ the right entirety statement (differentiable on all of ℂ, every t) |
| `Phi`, `Ht`, `ZeroVerification` | §3.1, unchanged from v1.0 | unchanged (byte-compared against SPEC §3.1) | ✅ |
| deviation record | §3.3 + design note §7 format, dated | file header items 1–4, dated **2026-09-06 (Session 16)**; design note **§7.1** addendum, same date | ✅ |
| trusted-layer size | §3.1 "nine definitions and nothing else" | exactly nine `def`s, zero theorems | ✅ |

Independent cross-check of P15's own algebra (standing order 5, nothing on trust): the SPEC quotes
(9) in two forms; the first, `1/s + 1/(s−1) − ½ log π + ½ Log(s/2) − 1/(2s)`, equals the second,
`1/(2s) + 1/(s−1) + ½ Log(s/(2π))`, and the second is `M₀′/M₀` for the `M0` above — the auditor
differentiated `log M₀ = c + log s + log(s−1) − (s/2)log π + (s/2 − ½)Log(s/2) − s/2` and obtained
`1/s + 1/(s−1) − ½ log π + ½ Log(s/2) + (s/2 − ½)/s − ½ = 1/(2s) + 1/(s−1) + ½ Log(s/(2π))`. The
Lean `alpha` is therefore the paper's α and is consistent with the `M0` in the same file. ✅

### 1.2 L-B3, `Zeta23/DBN/BtFacts.lean`

| item | required | as landed | verdict |
|---|---|---|---|
| L-B3 content | SPEC §3.4/§8.3: `Bt` differentiable **and** nonvanishing on an open neighborhood of the instance rectangle | `Bt_ne_zero (t) {z} (hz : z.re ≠ 0)` and `differentiableAt_Bt (t) {z} (hz : z.re ≠ 0)`, plus `isOpen_rightHalfPlane` and `differentiableOn_Ht_div_Bt : HtEntire → ∀ t, DifferentiableOn ℂ (fun z => Ht t z / Bt t z) {z | 0 < z.re}` | ✅ strictly stronger than required (a weaker hypothesis, an open set ⊇ R) |
| mechanism | SPEC §3.4: `Im s = −x/2 ≠ 0` ⇒ `s`, `s/2`, `s/(2π)` off the cut; `exp ≠ 0`; `π ≠ 0` base of the cpow; `√(2π) ≠ 0`; `s ≠ 0`, `s − 1 ≠ 0` | exactly that chain (`im_half_one_sub_I_mul`, `mem_slitPlane_of_im_ne_zero'`, `half_im_ne_zero`, `div_two_pi_im_ne_zero`, `Complex.cpow_eq_zero_iff`, `Real.sqrt_ne_zero'`, `Complex.exp_ne_zero`) | ✅ |
| hypothesis shape | SPEC §3.4 prints "z with **Im z ≠ 0**" | proved for **Re z ≠ 0** | ✅ the SPEC text is the slip (its own parenthetical says `Im s = −x/2`, and `x = Re z`) — **R-3** |
| file placement | SPEC §3.4/§8.3 say `BarrierCert.lean` | new file `BtFacts.lean` | ✅ benign; recorded in R-3 |
| displayed? | must NOT be displayed if proved | not displayed; `hBt` occurs nowhere in `Zeta23/` | ✅ |

### 1.3 The glue, `Zeta23/DBN/Instance02.lean` §2

| item | SPEC | as landed | verdict |
|---|---|---|---|
| conclusion | §1.1 `∀ t : ℝ, 1/5 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0` | identical, `(1 / 5 : ℝ)`, exact rational, no float | ✅ |
| X | §9 `5 000 000 194 858` | `5000000194858` (and `row2Rect = ⟨5000000194858, 1, 5000000194859, 1, 16733, 100000, 1, 1⟩`, so `x2 = X + 1`) | ✅ |
| t₀ | §9 `93/500` | data literal `row2T0n = 93`, `row2T0d = 500` in `Instance02/Rect.lean`; `row2BarrierMP.t0n/t0d = 93/500`, same for ARB | ✅ |
| y₀ | §9 `16733/100000` | `16733 / 100000` | ✅ |
| σ₀ of H1 | §3.6 `116733/200000` **exact** (58367/100000 is a round-UP and must not be used) | `hH1 : ZeroVerification (116733 / 200000) 2500000097429`; `hH1_row2` converts it to the bridge's `(1 + 16733/100000)/2` by `norm_num` | ✅ the round-UP never appears |
| T₀ of H1 | §3.6 `2 500 000 097 429` | `2500000097429`; `hH1_row2` proves `(5000000194858 : ℝ)/2 = 2500000097429` | ✅ |
| L-G | §6/§8.3 `t₀ + y₀²/2 ≤ 1/5` | `row2_bound_le_point2 : (93/500 : ℝ) + (16733/100000)^2/2 ≤ 1/5`, `norm_num`; auditor recomputed `= 3999993289/20000000000 = 0.19999966445` | ✅ matches SPEC §9 exactly |
| H2-B consumption | Instance02 `_xy` legs: `hEncl : BarrierEnclOK (fun t z => H t z / B t z) d`, `hHol` for `fun z => H t z / B t z` | glue passes `H := Ht`, `B := Bt`; displayed `hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierMP` — **the `_xy` hypothesis verbatim** | ✅ **no strengthening slipped in**; the `hHol` argument is *discharged*, not displayed |
| `hLaneA` | must be exactly (ii′) at t₀ | `∀ x y : ℝ, 5000000194858 + 1 ≤ x → 16733/100000 ≤ y → y^2 ≤ 1 - 2*(93/500) → Ht (93/500) (x + y*I) ≠ 0` — i.e. (ii′) with `t₀ := 93/500`, `X := 5000000194858`, `y₀ := 16733/100000` substituted, character for character | ✅ exactly (ii′); nothing more, nothing less |
| `hLaneA` honestly documented? | SPEC §3.7 foresees H2-A as rows + H-TAIL behind `checkAsym` | flagged as displayed **in conclusion form** and **stronger than SPEC §3.7's H2-A** in: the Instance02.lean file header, the `lambda_le_point2` docstring, `row2_ray_mp`'s docstring, `lean/README.md`, `GLUE-NOTES.md`, the direction file and design note §7.1 | ✅ documented in every record |
| `hH3` | §3.5 `Polymath15Bridge' ∧ HtEntire` | identical | ✅ |
| `hBt` | must be absent (L-B3 proved) | absent | ✅ |
| SPEC §8.3's `(c : Row2Cert)` / `hH2 : M2aEnclOK c` shape | §8.1–8.3 | **not implemented**: `Row2Cert`, `M2aEnclOK`, `AsymEnclOK`, `TailOK`, `checkAsym` do not exist in `Zeta23/` (they are Lane A vocabulary, RUN-REPORT §6 item 3) | ✅ honest, recorded deviation — the theorem displays only the H2 component that exists (H2-B) plus (ii′) |
| two legs never merged (D-R3) | required | `lambda_le_point2` (mp) and `lambda_le_point2_arb` (Arb) are two theorems with identical statements except `row2BarrierMP`/`row2BarrierARB` | ✅ |

### 1.4 D-H3 re-derived independently (the auditor did not take SPEC's derivation on trust)

Fix `0 < t₀`, `0 < X`, `0 < y₀ ≤ 1`, and assume (i), (ii′), (iii′) as `Polymath15Bridge'` states them.

* **Theorem 1.2(ii).** Let `x ≥ X + √(1 − y₀²)` and `y₀ ≤ y ≤ √(1 − 2t₀)`. Then `y > 0` and
  `y² ≤ 1 − 2t₀`. If `x ≥ X + 1`, (ii′) applies directly. Otherwise `X ≤ X + √(1 − y₀²) ≤ x ≤ X + 1`
  (using `0 ≤ √(1 − y₀²) ≤ 1`, valid since `0 < y₀ ≤ 1`) and `y ≤ √(1 − 2t₀) ≤ 1` (valid since
  `t₀ > 0`), so (iii′) at `t = t₀ ∈ [0, t₀]` applies. ✔
* **Theorem 1.2(iii).** Its region has `X ≤ x ≤ X + √(1 − y₀²) ≤ X + 1`,
  `y ≥ √(y₀² + 2(t₀ − t)) ≥ y₀` (as `t ≤ t₀`) and `y ≤ √(1 − 2t) ≤ 1` (as `t ≥ 0`), with
  `0 ≤ t ≤ t₀` — a subset of (iii′)'s box. ✔
* Theorem 1.2 then gives `Λ ≤ t₀ + ½y₀²`, which in the ray form of §1.1 is exactly the conclusion. ∎

Two remarks the auditor adds to SPEC's D-H3, both in the safe direction: (a) the derivation does not
actually need the paper's p3 "simplified region" remark — (iii′)'s box **contains** Theorem 1.2(iii)'s
region, so assuming (iii′) is *stronger* and the implication holds a fortiori; the p3 remark is what
makes (iii′) *the thing the producers computed*, not what makes D-H3 valid; (b) writing (ii′)'s
y-range as `y² ≤ 1 − 2t₀` rather than `y ≤ √(1 − 2t₀)` is sound because `y ≥ y₀ > 0`, so the two are
equivalent there — and it keeps every square root out of the trusted layer, as §1.3 of the SPEC
requires. D-H3 **still applies** to the definition as landed. ✅

### 1.5 The anti-cheat property survives the change (auditor's own check)

`Defs.lean`'s anti-cheat note says a non-integrable integrand would make `Ht ≡ 0`, so the target
conclusion would be *false*, not vacuous. Displaying `hLaneA` (a nonvanishing statement) re-opens a
vacuity channel in principle. It is closed by H2-B independently: `PrismEnclOK` forces
`‖G τ z − f z‖ ≤ E/K` on ∂R together with the kernel-checked floor `|f| ≥ Fn/Fd` and the gate
`(E + D)·Fd < Fn·K`, so `G = Ht/Bt ≡ 0` on ∂R is inconsistent with `hEncl`. The theorem is therefore
not satisfiable by a degenerate `Ht`. ✅

---

## §2. Build and axioms — the auditor's own runs, verbatim

One `lake` process at a time throughout; no `lake clean`, no `lake update`. Working tree
`/Users/jaytyagi/rh-lean-work/zeta-23-lean-main`.

### 2.1 `lake build Zeta23.DBN.Instance02` (auditor's run)

    Build completed successfully (3263 jobs).
    lake build Zeta23.DBN.Instance02  0.91s user 1.75s system 149% cpu 1.781 total
    EXIT=0

This run is a **replay** — lake's traces are current, so it proves the oleans correspond to the
sources as they stand, not that the sources were re-elaborated. The independent elaboration is 2.2.
Artifact dates confirm the builder's 2026-09-06 rebuild really did re-run every kernel check
downstream of `Defs.lean` v1.1:

    .lake/build/lib/lean/Zeta23/DBN/Defs.olean               Sep  6 02:58
    .lake/build/lib/lean/Zeta23/DBN/BarrierCert.olean        Sep  6 02:59
    .lake/build/lib/lean/Zeta23/DBN/Instance02/arb_0071.olean Sep  6 02:59
    .lake/build/lib/lean/Zeta23/DBN/Instance02/mp_0000.olean  Sep  6 03:00
    .lake/build/lib/lean/Zeta23/DBN/Instance02/mp_Barrier.olean Sep  6 03:00
    .lake/build/lib/lean/Zeta23/DBN/BtFacts.olean            Sep  6 03:02
    .lake/build/lib/lean/Zeta23/DBN/Instance02.olean         Sep  6 03:05

### 2.2 From-source elaboration of the three changed/new files (auditor's run)

    ### lake env lean Zeta23/DBN/Defs.lean
    lake env lean Zeta23/DBN/Defs.lean  1.12s user 1.06s system 102% cpu 2.118 total
    EXIT=0
    ### lake env lean Zeta23/DBN/BtFacts.lean
    lake env lean Zeta23/DBN/BtFacts.lean  1.60s user 1.08s system 117% cpu 2.279 total
    EXIT=0
    ### lake env lean Zeta23/DBN/Instance02.lean
    lake env lean Zeta23/DBN/Instance02.lean  1.39s user 1.11s system 113% cpu 2.193 total
    EXIT=0

Zero diagnostic output on all three: **no errors, no warnings, and in particular no
`declaration uses 'sorry'`.**

### 2.3 The auditor's own `#check` / `#print` / `#print axioms` (scratch `audit-tmp/auditor-axioms.lean`, `lake env lean`, verbatim)

    lambda_le_point2 : ZeroVerification (116733 / 200000) 2500000097429 →
      BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierMP →
        (∀ (x y : ℝ),
            5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y → y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (↑x + ↑y * I) ≠ 0) →
          Polymath15Bridge' ∧ HtEntire → ∀ (t : ℝ), 1 / 5 ≤ t → ∀ (z : ℂ), Ht t z = 0 → z.im = 0
    lambda_le_point2_arb : ZeroVerification (116733 / 200000) 2500000097429 →
      BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierARB →
        (∀ (x y : ℝ),
            5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y → y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (↑x + ↑y * I) ≠ 0) →
          Polymath15Bridge' ∧ HtEntire → ∀ (t : ℝ), 1 / 5 ≤ t → ∀ (z : ℂ), Ht t z = 0 → z.im = 0
    row2_ray_mp : ZeroVerification (116733 / 200000) 2500000097429 →
      BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierMP →
        (∀ (x y : ℝ),
            5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y → y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (↑x + ↑y * I) ≠ 0) →
          Polymath15Bridge' ∧ HtEntire →
            ∀ (t : ℝ), 93 / 500 + (16733 / 100000) ^ 2 / 2 ≤ t → ∀ (z : ℂ), Ht t z = 0 → z.im = 0
    row2_ray_arb : ZeroVerification (116733 / 200000) 2500000097429 →
      BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierARB →
        (∀ (x y : ℝ),
            5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y → y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (↑x + ↑y * I) ≠ 0) →
          Polymath15Bridge' ∧ HtEntire →
            ∀ (t : ℝ), 93 / 500 + (16733 / 100000) ^ 2 / 2 ≤ t → ∀ (z : ℂ), Ht t z = 0 → z.im = 0
    hHol_of_entire : ∀ (d : BarrierData),
      d.rect = row2Rect →
        HtEntire →
          ∀ (t : ℝ), 0 ≤ t → t ≤ t0 d → ∃ U, IsOpen U ∧ BarrierRect d ⊆ U ∧ DifferentiableOn ℂ (fun z => Ht t z / Bt t z) U
    hH1_row2 : ZeroVerification (116733 / 200000) 2500000097429 →
      ZeroVerification ((1 + 16733 / 100000) / 2) (5000000194858 / 2)
    row2_bound_le_point2 : 93 / 500 + (16733 / 100000) ^ 2 / 2 ≤ 1 / 5
    row2Rect_x1 : row2Rect.x1 = 5000000194858
    row2Rect_x2 : row2Rect.x2 = 5000000194858 + 1
    row2Rect_y1 : row2Rect.y1 = 16733 / 100000
    row2Rect_y2 : row2Rect.y2 = 1
    row2BarrierMP_t0 : t0 row2BarrierMP = 93 / 500
    row2BarrierARB_t0 : t0 row2BarrierARB = 93 / 500
    Bt_ne_zero : ∀ (t : ℝ) {z : ℂ}, z.re ≠ 0 → Bt t z ≠ 0
    differentiableAt_Bt : ∀ (t : ℝ) {z : ℂ}, z.re ≠ 0 → DifferentiableAt ℂ (Bt t) z
    isOpen_rightHalfPlane : IsOpen {z | 0 < z.re}
    differentiableOn_Ht_div_Bt : HtEntire → ∀ (t : ℝ), DifferentiableOn ℂ (fun z => Ht t z / Bt t z) {z | 0 < z.re}
    def Zeta23.DBN.Polymath15Bridge' : Prop :=
    ∀ (t₀ X y₀ : ℝ),
      0 < t₀ →
        0 < X →
          0 < y₀ →
            y₀ ≤ 1 →
              ZeroVerification ((1 + y₀) / 2) (X / 2) →
                (∀ (x y : ℝ), X + 1 ≤ x → y₀ ≤ y → y ^ 2 ≤ 1 - 2 * t₀ → Ht t₀ (↑x + ↑y * I) ≠ 0) →
                  (∀ (x y : ℝ), X ≤ x → x ≤ X + 1 → y₀ ≤ y → y ≤ 1 → ∀ (t : ℝ), 0 ≤ t → t ≤ t₀ → Ht t (↑x + ↑y * I) ≠ 0) →
                    ∀ (t : ℝ), t₀ + y₀ ^ 2 / 2 ≤ t → ∀ (z : ℂ), Ht t z = 0 → z.im = 0
    def Zeta23.DBN.HtEntire : Prop :=
    ∀ (t : ℝ), Differentiable ℂ (Ht t)
    def Zeta23.DBN.Bt : ℝ → ℂ → ℂ :=
    fun t z => Mt t ((1 - I * z) / 2)
    def Zeta23.DBN.Mt : ℝ → ℂ → ℂ :=
    fun t s => Complex.exp (↑t / 4 * alpha s ^ 2) * M0 s
    def Zeta23.DBN.M0 : ℂ → ℂ :=
    fun s =>
      1 / 8 * (s * (s - 1) / 2) * ↑Real.pi ^ (-s / 2) * ↑√(2 * Real.pi) *
        Complex.exp ((s / 2 - 1 / 2) * Complex.log (s / 2) - s / 2)
    def Zeta23.DBN.alpha : ℂ → ℂ :=
    fun s => 1 / (2 * s) + 1 / (s - 1) + 1 / 2 * Complex.log (s / (2 * ↑Real.pi))
    def Zeta23.DBN.ZeroVerification : ℝ → ℝ → Prop :=
    fun σ₀ T₀ => ∀ (s : ℂ), riemannZeta s = 0 → σ₀ ≤ s.re → s.re ≤ 1 → 0 ≤ s.im → s.im ≤ T₀ → False
    'Zeta23.DBN.Instance02.lambda_le_point2' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.lambda_le_point2_arb' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.row2_ray_mp' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.row2_ray_arb' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.hHol_of_entire' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.hH1_row2' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.row2_bound_le_point2' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.row2Rect_x1' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.row2Rect_x2' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.row2Rect_y1' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.row2Rect_y2' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.row2BarrierMP_t0' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.row2BarrierARB_t0' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Bt_ne_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.differentiableAt_Bt' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.isOpen_rightHalfPlane' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.differentiableOn_Ht_div_Bt' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.row2_barrier_mp_xy' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.row2_barrier_arb_xy' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.row2_barrier_mp' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.row2_barrier_arb' depends on axioms: [propext, Classical.choice, Quot.sound]

**Every declaration — all 21, including both `lambda_le_point2` theorems and every new
declaration — depends on exactly `[propext, Classical.choice, Quot.sound]`. No `sorryAx`, no
`Lean.ofReduceBool` (which is what `native_decide` would add), nothing else.**

### 2.4 Sweeps

`grep -rn "sorry|admit|native_decide|axiom|sorryAx|skipKernelTC|debug\.|unsafe|@[implemented_by]|partial def|trustCompiler"` over
`Zeta23/DBN/` (all 121 files, `Instance02/` included): **every hit is inside a docstring or comment**
(the files' own prose "no `native_decide`", "sorry-free", "`#print axioms` = …"). No declaration,
no tactic, no attribute. The only `set_option` anywhere in `Zeta23/DBN/` is
`set_option maxRecDepth 100000` (113 occurrences, the per-prism and `_Barrier` modules) — the SPEC
§7.6 packaging option, harmless to soundness.

`grep -rn "Polymath15Bridge"` excluding the primed name, over all of `Zeta23/`: three hits, all
comments — `Defs.lean:38` (the deviation record, correct and intentional) and
`BarrierCert.lean:56`, `BarrierCert.lean:1065` (**R-2**). **No declaration named `Polymath15Bridge`
exists**; the old name is gone from the trusted layer as SPEC §3.3 demands.

### 2.5 Copy-back

    diff -rq /Users/jaytyagi/rh-lean-work/zeta-23-lean-main/Zeta23/DBN \
             /Users/jaytyagi/Library/Mobile Documents/.../rh-program/lean/Zeta23/DBN
    DIFF: IDENTICAL   (exit 0)

Program tree contains `BarrierCert.lean`, `BtFacts.lean` (new), `Defs.lean`, `Instance02/`,
`Instance02.lean`. ✅ faithful.

---

## §3. Label ruling

**The label as written in the Lean files and in `lean/README.md` PASSES.** The binding sentence in
`Instance02.lean`'s header is

> "kernel-checked modulo the displayed hypotheses H1, H2-B, H2-A (in conclusion form, pending the
> Lane A checker) and H3 (producers untrusted)"

which is the SPEC §3.7 form **with the displayed hypotheses named as they actually are**. It is not
stronger than SPEC §3.7 — it is *weaker* (it assumes more: (ii′) itself instead of rows behind a
checker), and it says so, in those words, in seven places. `Defs.lean` continues to carry SPEC §3.7
verbatim as the milestone's trust model, correctly labeled as such. "Fully machine-checked" appears
in the corpus only inside prohibitions. The Λ bracket of record is untouched: 0 ≤ Λ ≤ 0.2; "Λ < 0.2"
is nowhere written. **Not a FAIL.**

**One clause is too permissive and is R-1.** `lean/README.md` (line 144) and `GLUE-NOTES.md`
(lines 101–103) say the short sentence *"Λ ≤ 0.2 in ray form, kernel-checked modulo H1, H2, H3"* is
"licensed only with the H2-A gloss". Two reasons that is wrong:

1. **The gate is two items, not one.** RUN-REPORT §6 item 4 reads "…from H1 (exact), **Lane A's
   (ii′)**, `row2_barrier_*_xy` … and `hH3.1`; finish with t₀ + y₀²/2 ≤ 1/5. **Only then** may a
   public sentence read 'Λ ≤ 0.2 in ray form, kernel-checked modulo H1, H2, H3'." The "(ii′)" in
   that sentence is *Lane A's*, i.e. item 3's `cert_of_checkAsym` output. Item 3 has not landed.
2. **"H2" names something that does not exist yet.** SPEC §6 defines H2 as `H2-B ∧ H2-A ∧ H-TAIL`,
   with H2-A and H-TAIL entering *behind* a kernel-checked `checkAsym`. Today `AsymEnclOK`,
   `TailOK`, `checkAsym` and `cert_of_checkAsym` are not in the Lean tree at all. A sentence naming
   "H2" therefore misnames the second hypothesis, and a gloss that has to be carried along to repair
   the naming is exactly the failure mode the trust-vocabulary rule (D-R3/D-R8) exists to prevent:
   glosses get dropped in quotation, hypothesis names do not.

The correct statement — and the wording R-1 installs — is: that sentence is **not licensed yet**;
the licensed wording is the four-hypothesis label, which names H2-A as displayed in conclusion form.
This is a tightening only; nothing in the Lean files needs to change.

---

## §4. Honesty

* **Nothing is claimed that is not true.** Every "PROVED" in the builder's records was re-verified
  here from source: L-B3 proved (four theorems, plus eleven supporting lemmas), `hHol` discharged,
  L-G proved, the two glue theorems proved, all with the three standard axioms only.
* **Nothing true is hidden.** The one place where the landed work is *weaker* than the SPEC's
  intended end state — H2-A displayed in conclusion form instead of behind `checkAsym` — is stated
  in the Lean file header, in both relevant docstrings, in `README.md`, in `GLUE-NOTES.md`, in the
  direction file and in design note §7.1, each time with the word "STRONGER" applied to the
  hypothesis (the correct direction: a stronger hypothesis is a weaker theorem). The auditor found
  no record in which the qualification is absent.
* **The deviations from SPEC §8.3 are recorded, not silent:** (a) the theorem takes `hEncl`/`hLaneA`
  rather than `(c : Row2Cert)` + `hH2 : M2aEnclOK c`, because the Lane A vocabulary does not exist;
  (b) L-B3 landed in `BtFacts.lean` rather than `BarrierCert.lean`; (c) L-B3's hypothesis is
  `Re z ≠ 0` rather than a rectangle neighborhood — stronger, not weaker. (a) and (b) are recorded
  by the builder; (c) is recorded by the builder and, with the SPEC's own slip, by R-3 here.
* **The dated records are accurate.** `Defs.lean` header deviation record (2026-09-06, Session 16,
  four numbered items, design-note §7 format); design note **§7.1** addendum, same date, and its
  claims ("116 downstream modules rebuilt clean", "trusted layer is now nine definitions, still no
  theorems", "H1 at the instance is exact") were each independently verified above;
  `lean/README.md` "## M2a glue (2026-09-06)" section and its licensing parenthetical for the
  fourteenth file (line 179); the direction file's 2026-09-06 work-log bullet. All dated, all
  accurate, subject to R-1's wording.
* **What today's result does NOT establish, stated plainly:** Λ ≤ 0.2 is *not* proved. Four
  hypotheses are displayed, one of them (`hLaneA`) is the entire final-time asymptotic lane in
  conclusion form with nothing kernel-checked behind it, and one (`hH3`) is Polymath15's Theorem 1.2
  plus the entirety of H_t. What *is* new today is that the chain from a kernel-checked barrier
  transcript to the ray-form statement is closed in Lean, with `hHol` and L-B3 discharged rather
  than assumed. The bracket of record remains 0 ≤ Λ ≤ 0.2 on the Rodgers–Tao / Platt–Trudgian
  literature, not on this artifact.
* **AUDIT.md F-5 (the 2026-09-03 cut line) is partially discharged:** items 1, 2 and 4 of
  RUN-REPORT §6 have landed and are clean; item 3 (Lane A) and item 5 (packaging) have not. F-5's
  demand — "no public sentence may say more than 'Lane B … modulo H2-B and hHol'" — is superseded
  by the §3 ruling above for the sentences about `lambda_le_point2`; the Lane B transcripts' own
  per-lane label is unchanged.

---

## §5. The owed repairs, with exact edits

Apply all three. None requires reading this report; each is a literal string replacement.

### R-1a — `rh-program/lean/README.md`

Replace (one occurrence, in the "## M2a glue (2026-09-06)" section):

    Lane A checker) and H3 (producers untrusted)"* — never "fully machine-checked"; the public sentence "Λ ≤ 0.2 in
    ray form, kernel-checked modulo H1, H2, H3" is licensed only with the H2-A gloss until Lane A lands. What Lane A
    changes when it lands: `hLaneA` is replaced by `cert_of_checkAsym` on the Lane A literal, nothing else moves.

with:

    Lane A checker) and H3 (producers untrusted)"* — never "fully machine-checked". The shorter sentence "Λ ≤ 0.2 in
    ray form, kernel-checked modulo H1, H2, H3" is NOT licensed yet, with or without a gloss: RUN-REPORT §6 item 4
    gates it on Lane A (item 3) landing as well, and "H2" is SPEC §6's conjunction H2-B ∧ H2-A ∧ H-TAIL behind a
    kernel-checked checker, of which only H2-B exists today. Until Lane A lands, the four-hypothesis label above is
    the only licensed wording. What Lane A changes when it lands: `hLaneA` is replaced by `cert_of_checkAsym` on the
    Lane A literal, nothing else moves.

### R-1b — `rh-program/results/d1-m2a/v11/GLUE-NOTES.md`

Replace (one occurrence, immediately after the block-quoted honest label):

    Never "fully machine-checked".  The public sentence RUN-REPORT §6 item 4 licenses ("Λ ≤ 0.2 in ray form,
    kernel-checked modulo H1, H2, H3") is licensed ONLY with the gloss that H2-A is displayed in conclusion form until
    Lane A lands; without that gloss the sentence overstates.

with:

    Never "fully machine-checked".  The shorter sentence RUN-REPORT §6 item 4 speaks of ("Λ ≤ 0.2 in ray form,
    kernel-checked modulo H1, H2, H3") is NOT licensed today, with or without a gloss: item 4's "only then" is gated
    on item 3 (Lane A) as well, and "H2" is SPEC §6's conjunction H2-B ∧ H2-A ∧ H-TAIL behind a kernel-checked
    checker, of which only H2-B exists in the Lean tree.  The licensed wording is the four-hypothesis label above,
    with H2-A named as displayed in conclusion form.  (Auditor's ruling, v11/AUDIT.md §3, 2026-09-06.)

### R-2 — `Zeta23/DBN/BarrierCert.lean` (apply in the WORKING TREE `/Users/jaytyagi/rh-lean-work/zeta-23-lean-main`, then rebuild, then rsync back)

Two literal replacements, both docstring text only:

1. line 56 — replace

        that `Polymath15Bridge`'s hypothesis (iii) consumes, for H = G·B.

   with

        that hypothesis (iii′) of `Polymath15Bridge'` consumes, for H = G·B.

2. line 1065 — replace

        /-- **The conclusion in the coordinate form `Polymath15Bridge`'s hypothesis (iii) consumes.**

   with

        /-- **The conclusion in the coordinate form hypothesis (iii′) of `Polymath15Bridge'` consumes.**

Then, in `/Users/jaytyagi/rh-lean-work/zeta-23-lean-main` (one lake process at a time):

    lake build Zeta23.DBN.Instance02

(expect a full downstream rebuild of the 116 transcript modules, ≈ 1 minute wall; it re-runs the
`decide +kernel` facts, which is harmless), then

    rsync -a --delete /Users/jaytyagi/rh-lean-work/zeta-23-lean-main/Zeta23/DBN/ \
      "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/lean/Zeta23/DBN/"

and re-confirm with `diff -rq` between the two `DBN` directories.

*(If the rebuild cost is judged not worth a comment fix this session, R-2 may instead be deferred to
the Lane A session, which will rebuild these modules anyway — but it must then be carried forward
explicitly in the RUN-REPORT §6 list, not dropped.)*

### R-3 — `rh-program/results/d1-m2a/SPEC.md` §14 (append-only errata)

Append as item 6 of §14:

    6. **§3.4, L-B3's hypothesis and its file.** The sentence "for t ∈ ℝ and z with Im z ≠ 0 … more precisely on an
       open neighborhood of any rectangle with y₁ > 0 and x₁ > 1" states the wrong coordinate: the mechanism in the
       same parenthetical ("s = (1 − iz)/2 has Im s = −x/2 ≠ 0") needs **Re z ≠ 0**, x being Re z. L-B3 as landed
       (2026-09-06, Session 16) proves the correct form — `Bt_ne_zero` and `differentiableAt_Bt` for every z with
       Re z ≠ 0, packaged as `differentiableOn_Ht_div_Bt` on the open right half-plane {z | 0 < Re z} ⊇ R — which is
       stronger than either reading of the §3.4 sentence, so nothing downstream changes. §3.4 and §8.3 also place
       L-B3 in `BarrierCert.lean`; it landed in the new `Zeta23/DBN/BtFacts.lean`. Wording and file placement only;
       no check, hypothesis or theorem shape changes. (Auditor, `results/d1-m2a/v11/AUDIT.md` §1.2.)

---

## §6. Files read and commands run (verification ledger for this audit)

Read: `results/d1-m2a/SPEC.md` (§1–§3, §6, §8, §9, §14), `results/d1-m2a/AUDIT.md` (F-5),
`results/d1-m2a/RUN-REPORT.md` §6, `results/d1-m0/m2a-m2b-design.md` §7.1,
`Zeta23/DBN/Defs.lean` (all 180 lines), `Zeta23/DBN/BtFacts.lean` (all 156 lines),
`Zeta23/DBN/Instance02.lean` (all 229 lines), `Zeta23/DBN/BarrierCert.lean` (§ definitions
lines 180–236 and `cert_of_checkBarrier`/`_xy` lines 1025–1100), `Zeta23/DBN/Instance02/Rect.lean`,
`Instance02/mp_Barrier.lean` and `arb_Barrier.lean` headers, `lean/README.md`,
`directions/D1-certified-refutation-arm.md`, `results/d1-m2a/v11/{DEFS-V11-NOTES,LB3-NOTES,GLUE-NOTES}.md`.

Ran (auditor's own, working tree `/Users/jaytyagi/rh-lean-work/zeta-23-lean-main`, one lake process
at a time): `lake build Zeta23.DBN.Instance02`; `lake env lean` on `Defs.lean`, `BtFacts.lean`,
`Instance02.lean`; `lake env lean audit-tmp/auditor-axioms.lean` (the auditor's own scratch with 17
`#check`, 7 `#print` and 21 `#print axioms`); the grep sweeps of §2.4; `diff -rq` of §2.5; `ls -la`
of the oleans in §2.1. Scratch and logs:
`audit-tmp/auditor-axioms.lean` in the working tree; logs in the session scratchpad
(`audit-build.log`, `from-source.log`, `auditor-axioms.log`).

No program file was modified by this audit.
