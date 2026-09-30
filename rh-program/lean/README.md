# `rh-program/lean` — this program's own Lean 4 files

13 hand-written files, ~8,570 lines (3,265 of them the data literals of `W1/Instances.lean`, added
2026-09-02; 1,092 of them `DBN/BarrierCert.lean`, added the same day), plus the 116 mechanically emitted
modules of `DBN/Instance02.lean` + `DBN/Instance02/` (23,965 lines of transcript literals, added 2026-09-03).
They are **additions to the `Zeta23` library**, not a standalone project, and they are the only Lean files
in this repository.
Since 2026-09-09 (Session 19, M2a Lane A) also the hand-written `DBN/Asym.lean` (246 lines) and the two mechanically
emitted Lane A literal modules `DBN/Instance02/Asym_mp.lean` (120) and `Asym_arb.lean` (120) — see the
"M2a Lane A (2026-09-09)" section below.
Since 2026-09-10 (Session 20, packaging) also the comparator topic `DBN` under `comparator/` (the trusted `ChallengeDeps/DBN.lean`
and `ChallengeDeps/DBN/Instance02.lean`, `Challenge/DBN.lean`, `Solution/DBN.lean`, `PrintAxioms/DBN.lean`, `config-dbn.json`) and
`formalization.yaml` — see the "Packaging (2026-09-10)" section below.

| File | Lines | What it carries |
|---|---|---|
| `Zeta23/PairCeiling/GridParseval.lean` | 583 | The grid-Parseval decoupling identity — the algebraic core of the A4 absorption result (Lemma 3.8 and Theorem 3.9 of the A4 paper) |
| `Zeta23/PairCeiling/GridWitness.lean` | 402 | The 4128/33 witness, for every vacancy position |
| `Zeta23/PairCeiling/GridCorner.lean` | 263 | The corner theorem: Lemma 4.2 and Theorem 4.3, pointwise, in law form, and with exact attainment |
| `Zeta23/W1/Soundness.lean` | 1534 | W1 checker soundness — generic in the function since 2026-09-10 (`cert_of_checkW1_of_diffOn`; ζ instance `cert_of_checkW1` unchanged); σ-strong sibling `cert_of_checkW1_of_diffOn'` (Session 21, 2026-09-10) — see the "σ-strong sibling" section below |
| `Zeta23/W1/FDH.lean` | 249 | **D-R8 (2026-09-10):** f_DH in Lean — `kappaDH`, `fDH`, `differentiable_fDH`, `cert_of_checkW1_fDH` (modulo H-ENCL_DH only), `mpDH_zero`, `arbDH_zero` — see the "D-R8" section below; **Session 21 (2026-09-10):** the box-form twins `cert_of_checkW1_fDH'`, `mpDH_zero'`, `arbDH_zero'` — see the "σ-strong sibling" section below |
| `Zeta23/W1/Ledger.lean` | 95 | **M3 seed (2026-09-10):** the eight 3-line corollaries of `cert_of_checkW1_ap` (m = 0 branch) for the four seed rows of `results/d1-m3/` — see the "M3 seed" section below |
| `Zeta23/W1/{Checker,Examples,Format}.lean` | 385 | The W1 checker, its examples and its output format |
| `Zeta23/W1/Instances.lean` | 3265 | The ten M1 v1 acceptance transcripts and the two positive controls as kernel-checked checker instances (`checkW1Floor … = true` ×10, `checkW1 … = false` ×2 by `decide +kernel`); mechanically emitted by `results/d1-m1/emit_lean.py` and back-parse-verified against the JSON; needs `set_option maxRecDepth 100000` (written by the emitter) for the 983/1294-row literals — added at the reconciled audit of 2026-09-02, `results/d1-m1/AUDIT.md` |
| `Zeta23/W1/ArgPrinciple/Rect.lean` | 492 | The rectangle-integral machinery of the argument principle: `Rect`, `RectFrontier`, the four-edge `rectIntegral` in Mathlib's boundary convention, `windingRect`, the rectangle residue integral `rectIntegral_inv_sub` (∮ (ζ−a)⁻¹ dζ = 2πi — the piece Mathlib lacks), and the factored forms for entire cofactors. **Ported** (see the v1.1 note below) |
| `Zeta23/W1/ArgPrinciple/General.lean` | 249 | The general argument principle on rectangles for entire functions: zero factorization, finiteness of the zero set, `windingRect_eq_sum_analyticOrder`. **Ported** |
| `Zeta23/W1/ArgPrincipleBridge.lean` | 459 | **v1.1, D-R3: H-AP discharged.** Generalizes the ported theorem from entire functions to `DifferentiableOn ℂ f U` on an open `U ⊇ R`, bridges the two rectangle/winding vocabularies, handles the degenerate rectangle σ₁ = σ₂, and proves `rectArgPrinciple_of_local : ∀ f, RectArgPrinciple f`, `rectArgPrinciple_riemannZeta`, and `cert_of_checkW1_ap` — checker soundness with H-AP removed |
| `Zeta23/DBN/Defs.lean` | 117 | De Bruijn–Newman definitions |
| `Zeta23/DBN/BarrierCert.lean` | 1092 | **M2a Lane B (added 2026-09-02).** The barrier-certificate transcript data (`PrismData`, `RectData`, `BarrierData`), the integer checker `checkBarrier` (per-prism `checkPrism` = W1's C1, C3–C9 with the strip-free C2′, m = 0, the C11 floor and the gate C-B12 (E+D)·Fd < Fn·K; global `checkBarrierChain` = C-B13), the displayed hypothesis H2-B (`BarrierEnclOK`), and the soundness theorem `cert_of_checkBarrier` — PROVED, not displayed: the rectangle argument principle on a general rectangle (`rectArgPrincipleGen`, from the v1.1 bridge), the strip-free W1 mesh chain, and the one new analytic lemma `logDerivSegIntegral_eq_log_sub` (∫ h′/h = Log h(w) − Log h(z) when Re h > 0 on the segment) with log-derivative additivity; no Rouché, no zero-continuity in t. Plus `cert_of_checkBarrier_xy`, the coordinate form `Polymath15Bridge`'s (iii) consumes. Contract: `results/d1-m2a/SPEC.md`; record: `results/d1-m2a/lean-notes.md` |
| `Zeta23/DBN/Instance02.lean` + `Zeta23/DBN/Instance02/` (116 modules) | 23965 | **M2a item (e), Lane B instance (added 2026-09-03).** The Polymath15 Table-1 row-2 barrier transcripts of BOTH untrusted producers as kernel-checked checker instances: `Instance02/Rect.lean` (`row2Rect`), `Instance02/mp_0000…mp_0038.lean` (mpmath-ball leg, 39 prisms, 7 176 rows, K = 10²⁴) and `Instance02/arb_0000…arb_0071.lean` (Arb/FLINT leg, 72 prisms, 10 771 rows, K = 10¹²), each proving `checkPrism row2Rect <prism> = true` by `decide +kernel`; `Instance02/{mp,arb}_Barrier.lean` (`row2Barrier{MP,ARB} : BarrierData`, the chain fact by `decide +kernel`, the split per-prism fact, the monolithic `checkBarrier … = true`); `Instance02.lean` instantiates `cert_of_checkBarrier` / `cert_of_checkBarrier_xy` on both (`row2_barrier_{mp,arb}`, `_xy`), generic in G. Emitted by `results/d1-m2a/emit_lean_m2a.py` (untrusted), back-parse-verified by `verify_lean_m2a.py` (0 mismatches); record `results/d1-m2a/INSTANCE-REPORT.md`. **PARTIAL by design:** Lane A, `Defs.lean` v1.1 and the glue theorem `lambda_le_point2` are NOT here (cut line stated in the module header) |
| `Zeta23/DBN/Asym.lean` + `Zeta23/DBN/Instance02/Asym_{mp,arb}.lean` | 246 + 120 + 120 | **M2a Lane A (added 2026-09-09).** `Asym.lean` (hand-written, Session 19 builder): the asymptotic-lane transcript data (`AsymRow`, `TailRow`, `AsymData`), the integer checker `checkAsym` (C-A1 … C-A6, SPEC §7.4), the window index `windowIdx`, the displayed hypotheses H2-A (`AsymEnclOK`) and H-TAIL (`TailOK`), the soundness theorem `cert_of_checkAsym` (SPEC §8.3, proof = SPEC §5.6 via `cover_of_consecutive`) — PROVED — and L-A2 `windowIdx_mono`, L-A1 `row2_windowIdx_ge` (from `Real.pi_lt_d6`). `Instance02/Asym_mp.lean`, `Asym_arb.lean` (mechanically emitted by `results/d1-m2a/lane-a/emit_lean_lane_a.py`, untrusted; back-parse-verified integer by integer by `backparse_lane_a.py`, 0 mismatches): the two producers' Lane A literals `row2AsymMP` (mpmath-ball leg, K = 10²⁴) and `row2AsymARB` (Arb/FLINT leg, K = 10¹²) — 3 window rows covering N ∈ [630783, 5140999] consecutively plus the tail row at N₁ = 5 141 000 — each with its kernel fact `checkAsym … = true` by `decide +kernel` (`[propext]`) and the glue lemma `row2_laneA_{mp,arb}` (PLAN §1.5) that hands `cert_of_checkAsym` on the literal to `Polymath15Bridge'` as (ii′). `Instance02.lean`'s four theorems now display `hAsym`/`hTail` instead of `hLaneA`. Records: `results/d1-m2a/lane-a/{PLAN,PLAN-REVIEW,BUILD-NOTES,EMIT-NOTES}.md`, `final-axioms.log`, `trust-greps.log` |

`#print axioms` on every machine-checked theorem here reports only Lean's three standard
axioms — `propext`, `Classical.choice`, `Quot.sound`. This now covers, besides the twelve
theorems recorded before, all 45 declarations of `W1/ArgPrinciple/{Rect,General}.lean` and all 18
of `W1/ArgPrincipleBridge.lean`, `cert_of_checkW1_ap` included
(`results/d1-m1/v11/audit/audit-print-axioms.log`), and all 28 theorems and lemmas of
`DBN/BarrierCert.lean`, `cert_of_checkBarrier` included (`results/d1-m2a/barriercert-axioms.log`). No `sorryAx`, no `Lean.ofReduceBool`, and
no real `sorry` or `admit` anywhere in the development. The twelve `_check` theorems of
`W1/Instances.lean` report `[propext]` (the ten `checkW1Floor` instances) or no axioms at all
(the two rejections) — they are integer facts about literals; **since 2026-09-02 the ζ conclusion
for the eight ζ transcripts is `cert_of_checkW1_ap` modulo the single displayed hypothesis
H-ENCL** (H-AP is a theorem; see the v1.1 note below), and the two f_DH instances carry no
theorem about f_DH (D-R8). Build record for `Instances.lean`: `lake build Zeta23.W1.Instances` —
*Build completed successfully (656 jobs)*, 13.9 s, Lean `v4.33.0-rc2`, Mathlib `51e6992e`
(`results/d1-m1/recon_lean_instances.log`).

## v1.1 (2026-09-02): H-AP is discharged; H-ENCL is the only displayed hypothesis left

`W1/Soundness.lean` proves W1 checker soundness (`cert_of_checkW1`) modulo two displayed
hypotheses, H-ENCL (`W1EnclOK riemannZeta d`) and H-AP (`RectArgPrinciple riemannZeta`, the
rectangle argument principle for the exact counterclockwise traversal of FORMAT.md §4).
**H-AP is now a theorem**: `Zeta23.W1.rectArgPrinciple_of_local : ∀ f : ℂ → ℂ,
RectArgPrinciple f` in `W1/ArgPrincipleBridge.lean`, with `rectArgPrinciple_riemannZeta` its ζ
instance and

    Zeta23.W1.cert_of_checkW1_ap (d : W1Data) (hc : checkW1 d = true)
        (hEncl : W1EnclOK riemannZeta d) : <the conclusion of cert_of_checkW1, unchanged>

the restatement of soundness without it. `Soundness.lean` is imported, not rewritten. How: the
ported theorem `windingRect_eq_sum_analyticOrder` is generalized from `Differentiable ℂ H`
(entire) to `DifferentiableOn ℂ H U` for an open `U` containing the closed rectangle — the
identity theorem is applied on the preconnected closed rectangle, so `U` itself need not be
connected — the two rectangle/winding vocabularies are bridged by unconditional (junk-value-safe)
change-of-variables lemmas, and the degenerate rectangle σ₁ = σ₂ that clause C2b admits is proved
directly with `Z = 0`. No ζ-specific analytic input is consumed anywhere.

Build: `lake build Zeta23.W1.ArgPrincipleBridge` — *Build completed successfully (3145 jobs)*,
6 s from deleted oleans, no warnings, Lean `v4.33.0-rc2`, Mathlib `51e6992e`. (Since 2026-09-02
evening the root `Zeta23.lean` imports every program module, `DBN/BarrierCert` and `W1/Instances`
included; `lake build Zeta23` — *Build completed successfully (9023 jobs)*.) Adversarial audit, by a different model: `results/d1-m1/v11/AUDIT.md` — verdict CLEAN.

**Honest label, binding.** An accepted ζ transcript is *"kernel-checked modulo the displayed
hypothesis H-ENCL (producers untrusted)"*. Never "fully machine-checked": H-ENCL is where the
untrusted producers' interval arithmetic enters the trusted statement, and it stays.

**Attribution for the two ported files.** `W1/ArgPrinciple/Rect.lean` and
`W1/ArgPrinciple/General.lean` are ported, statement-for-statement unchanged, from the Lean
development in `github.com/judegomila/dbn-lambda-01787854-candidate-audit` (branch
`lean/certificate-and-argument-principle`, commit `ea09b2f`), **Copyright (c) 2026 Jude Gomila,
MIT License**, generated with Harmonic Aristotle; ported and adapted here (imports narrowed,
proofs repaired for a newer Mathlib, namespace changed). `W1/ArgPrincipleBridge.lean` adapts
seven of those lemmas and carries the same notice. The MIT license text is reproduced verbatim in
the repository's [`NOTICE`](../NOTICE), in dated sections; the port record is
`results/d1-m1/v11/port-notes.md`, the discharge record `results/d1-m1/v11/discharge-notes.md`,
and the independent build/axiom verification of the source branch
`results/d1-m1/gomila-lean-branch-verify.md`.

## M2a Lane B (2026-09-02): `DBN/BarrierCert.lean`

The barrier-certificate layer of the Λ ≤ 0.2 instance, implementing `results/d1-m2a/SPEC.md`
v1.0. Honest label for an accepted barrier transcript: *"kernel-checked modulo the displayed
hypotheses H2-B (`BarrierEnclOK G d`) and `hHol` (G t holomorphic near the rectangle), producers
untrusted"*. The theorem

    Zeta23.DBN.cert_of_checkBarrier (G : ℝ → ℂ → ℂ) (d : BarrierData)
        (hchain : checkBarrierChain d = true) (hprisms : ∀ p ∈ d.prisms, checkPrism d.rect p = true)
        (hHol : ∀ t, 0 ≤ t → t ≤ t0 d → ∃ U, IsOpen U ∧ BarrierRect d ⊆ U ∧ DifferentiableOn ℂ (G t) U)
        (hEncl : BarrierEnclOK G d) :
        ∀ t, 0 ≤ t → t ≤ t0 d → ∀ z ∈ BarrierRect d, G t z ≠ 0

takes the checker facts in the split form of SPEC §7.6 (per-prism kernel facts in per-prism
modules). Build: `lake build Zeta23.DBN.BarrierCert` — *Build completed successfully (3147 jobs)*,
3.2 s from a deleted olean, no warnings (`results/d1-m2a/barriercert-build.log`). The SPEC §12
micro-example checks by `decide +kernel` against the built module, with four negative controls
(`results/d1-m2a/barriercert-example-scratch.lean`, `.log`). `Defs.lean` is unchanged (v1.0); its
v1.1 additions (`Polymath15Bridge'`, `Bt`, `HtEntire`) and the asymptotic lane are the next items of the
Lean stream.

## M2a Lane B instance (2026-09-03): `DBN/Instance02.lean` + `DBN/Instance02/`

Both producers' row-2 barrier transcripts are kernel-checked, one module per prism (SPEC §7.6):
`checkPrism row2Rect <prism> = true` by `decide +kernel` for all 39 + 72 prisms, `checkBarrierChain … = true`
by `decide +kernel` for both chains, and `checkBarrier row2Barrier{MP,ARB} = true` assembled from them
(`List.all_eq_true`). Serial build (one `lake` process at a time): 157 s for the mp modules, 217 s for the
arb modules, ≈ 3.1–3.8 s per 100–300-row module, most of it import loading; the monolithic `decide +kernel`
on the full 7 176-row and 10 771-row literals also runs — 28 s for both together (≈ 1.4 ms/row), measured in
`results/d1-m2a/kernel-time.log`. `#print axioms`: the chain facts use no axioms, the per-prism and split facts
`[propext]`, the monolithic facts `[propext, Quot.sound]`, the instantiated barrier theorems the three standard
axioms (`results/d1-m2a/instance02-axioms.log`). Honest label: *"kernel-checked modulo the displayed hypotheses
H2-B and hHol (producers untrusted)"* — and the theorem `lambda_le_point2` (Λ ≤ 0.2 in ray form) is NOT
proved: Lane A and the Defs v1.1 glue do not exist yet (the cut line is in the module header). The root
`Zeta23.lean` imports `DBN.Instance02`; `lake build Zeta23` — *Build completed successfully (9138 jobs)*.

## M2a glue (2026-09-06): `DBN/Defs.lean` v1.1, `DBN/BtFacts.lean`, `lambda_le_point2` in `DBN/Instance02.lean`

**`Defs.lean` v1.1.** The v1.0 `Polymath15Bridge` (merged "canopy" form) is REMOVED — its t = 0 slice was RH in a
half-strip above the verified height, not dischargeable by any finite certificate (SPEC §3.2, D-3.2) — and replaced
by `Polymath15Bridge'` exactly as SPEC §3.3 prints it ((ii′) at the final time only; (iii′) on the box
X ≤ x ≤ X + 1, y₀ ≤ y ≤ 1, 0 ≤ t ≤ t₀). Added: `alpha`, `M0`, `Mt`, `Bt` (the concrete P15 normalizer, SPEC §3.4)
and `HtEntire` (SPEC §3.5). Nine definitions, no theorems; dated deviation record in the file header and in the
design note §7.1; `#print` record in `results/d1-m2a/v11/DEFS-V11-NOTES.md`. All 116 downstream modules rebuilt
clean with no adaptation.

**`BtFacts.lean` (L-B3, PROVED).** `Bt_ne_zero` and `differentiableAt_Bt` for every z with Re z ≠ 0 (the point
s = (1 − iz)/2 has Im s = −Re z/2, so both principal logs are off the cut, s ≠ 0, s ≠ 1), and the packaged
`differentiableOn_Ht_div_Bt : HtEntire → ∀ t, DifferentiableOn ℂ (fun z => Ht t z / Bt t z) {z | 0 < z.re}`.
Nothing displayed; no `hBt` anywhere.

**`lambda_le_point2` (and `lambda_le_point2_arb`, the Arb/FLINT leg — two theorems, never merged).** The SPEC §1.1
target, ∀ t ≥ 1/5, every zero of H_t is real, from FOUR displayed hypotheses, each a named argument:
`hH1 : ZeroVerification (116733/200000) 2500000097429` (H1, exact; Platt–Trudgian Theorem 1 in prose);
`hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierMP` (H2-B, the kernel-checked mp transcript);
`hLaneA : ∀ x y, 5000000194858 + 1 ≤ x → 16733/100000 ≤ y → y² ≤ 1 − 2·(93/500) → Ht (93/500) (x + y·I) ≠ 0`
(H2-A **in conclusion form** — the Lane A producers and `checkAsym` are a separate compute stream not yet run, so
this is displayed as the lane's conclusion with nothing kernel-checked behind it, which is STRONGER than the SPEC
§3.7 form); `hH3 : Polymath15Bridge' ∧ HtEntire` (H3). `hHol` is discharged (`hHol_of_entire`) from `hH3.2` and
L-B3; the arithmetic glue L-G (t₀ + y₀²/2 = 3999993289/20000000000 ≤ 1/5; the H1 parameter identities) is
`norm_num`. `#print axioms Zeta23.DBN.Instance02.lambda_le_point2` = `[propext, Classical.choice, Quot.sound]`
(the same for `_arb`, `row2_ray_mp/_arb`, `hHol_of_entire`; `results/d1-m2a/v11/GLUE-NOTES.md`, verbatim).
Honest label: *"kernel-checked modulo the displayed hypotheses H1, H2-B, H2-A (in conclusion form, pending the
Lane A checker) and H3 (producers untrusted)"* — never "fully machine-checked". The shorter sentence "Λ ≤ 0.2 in
ray form, kernel-checked modulo H1, H2, H3" is NOT licensed yet, with or without a gloss: RUN-REPORT §6 item 4
gates it on Lane A (item 3) landing as well, and "H2" is SPEC §6's conjunction H2-B ∧ H2-A ∧ H-TAIL behind a
kernel-checked checker, of which only H2-B exists today. Until Lane A lands, the four-hypothesis label above is
the only licensed wording. What Lane A changes when it lands: `hLaneA` is replaced by `cert_of_checkAsym` on the
Lane A literal, nothing else moves.

**[DATED NOTE 2026-09-09, Session 19 — the R-1 paragraph above is superseded and kept as the record.]** Lane A LANDED
(RUN-REPORT §6 item 3; the "M2a Lane A (2026-09-09)" section below). `hLaneA` is gone from `Instance02.lean`: in `row2_ray_mp`,
`row2_ray_arb`, `lambda_le_point2` and `lambda_le_point2_arb` the binder is now the pair
`hAsym : AsymEnclOK (fun z => Ht (93/500) z / Bt (93/500) z) row2Asym*` (H2-A, the window-row floors) and
`hTail : TailOK (fun z => Ht (93/500) z / Bt (93/500) z) row2Asym*` (H-TAIL), MP in the mp theorems and ARB in the Arb
theorems (each leg pairs its own Lane A literal with its own Lane B literal; the legs are never merged), and hypothesis
(ii′) of `Polymath15Bridge'` is `row2_laneA_* hAsym hTail` — `cert_of_checkAsym` on the kernel-checked literal plus
L-A1/L-A2. Nothing else in the proofs moved (`results/d1-m2a/lane-a/instance02-replacement.diff`). The displayed
hypotheses are now exactly SPEC §3.7's — H1, H2-B, H2-A, H-TAIL, H3 — and `#print axioms` is unchanged:
`[propext, Classical.choice, Quot.sound]` for all six theorems, `[propext]` for the two kernel facts
(`results/d1-m2a/lane-a/final-axioms.log`). **Honest label, verbatim: "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3"**, with SPEC §3.7's own gloss: (H1) a producer-certified zero verification — `ZeroVerification (116733/200000) 2500000097429`, discharged by Platt–Trudgian Theorem 1; (H2) producer-certified enclosures — the barrier prisms (H2-B), the final-time window rows (H2-A) and the tail (H-TAIL), from two independent producers, behind the kernel-checked checkers `checkBarrier` and `checkAsym`; (H3) the Polymath15 analytic package — Theorem 1.2 in the form `Polymath15Bridge'` and the entirety of H_t — as hypotheses. The count is three named hypotheses with H2 a conjunction of three enclosure-type Props; "three displayed hypotheses" only with that gloss. Never "fully machine-checked".
**The shorter sentence "Λ ≤ 0.2 in ray form, kernel-checked modulo H1, H2, H3" is therefore now LICENSED, with that
gloss** (RUN-REPORT §6 item 4's "only then" is met: items 1–4 have all landed; audit ruling R-1 is discharged, not
reversed — its condition was Lane A landing). What the replacement actually buys — stated, not glossed — is
PLAN-REVIEW §6 verbatim:

> Today `hLaneA` displays the *conclusion* "no zero of `H_{93/500}` anywhere in x ≥ 5 000 000 194 859, y₀ ≤ y,
> y² ≤ 157/250". After the replacement:
>
> * the window range **N ∈ [630 783, 5 140 999]** — i.e. x from 5.0·10¹² up to x_{N₁} ≈ **3.32·10¹⁴** — stops being a
>   displayed nonvanishing claim. What is displayed there is `AsymEnclOK`, a *floor enclosure* (‖g‖ ≥ (T−E)/K on each
>   window), and the step from those floors to nonvanishing on the whole range is the kernel-checked coverage
>   argument (C-A3, C-A4, C-A5 + L-A1 + L-A2). That is the real gain.
> * what remains a displayed nonvanishing *conclusion* is `TailOK`: N(x) ≥ 5 141 000, i.e. **x ≳ 3.32·10¹⁴**.
> * one asymmetry worth recording rather than glossing: `TailOK`'s y-band is [y₀, yA] with yA = 0.7924646, which is
>   **1.5·10⁻⁷ wider** than `hLaneA`'s y ≤ √(157/250) = 0.79246451… So `TailOK` is not literally a sub-statement of
>   `hLaneA`; it is a vastly smaller x-region with a hair-wider y-band. Both directions are covered — the glue lemma
>   derives y ≤ yA from y² ≤ 157/250 — but the label should say "the tail region N ≥ N₁, y ∈ [y₀, yA]", not "part of
>   what `hLaneA` said".
>   [DATED CORRECTION 2026-09-09 22:25 IST, phase-3(d) audit (AUDIT-3d.md A-1).] "1.5·10⁻⁷ wider" above is the gap in the
>   SQUARES (yA² − 157/250 = 3556329/(25·10¹²) = 1.4225·10⁻⁷). The gap in y itself is yA − √(157/250) = 8.975·10⁻⁸ ≈
>   9.0·10⁻⁸. The bullet's point — that `TailOK`'s y-band is a hair WIDER than the conclusion's, so `TailOK` is not
>   literally a sub-statement of `hLaneA` — is unaffected.
> * C-A6 (the tail row's Σ < 2K) is kernel-checked but **not consumed** by `cert_of_checkAsym` (§1, A9). It is
>   recorded evidence for Lemma T's prose discharge, exactly as SPEC §5.1 designs it. The label must not imply the
>   kernel checked the tail *reduction*.

## M2a Lane A (2026-09-09): `DBN/Asym.lean`, `DBN/Instance02/Asym_mp.lean`, `Asym_arb.lean`, `hLaneA` replaced in `DBN/Instance02.lean`

**Producers (results/d1-m2a/lane-a/, UNTRUSTED).** P-9/P-10 of SPEC §5 implemented twice from the quoted Polymath15
formulas (`p9_mp.py`, mpmath `iv` prec 288; `p9_arb.py`, python-flint `arb` prec 320): the plan's 3 window rows
[630783, 746495], [746496, 1469440], [1469441, 5140999] (4 510 217 windows; floors T/K ≈ 0.01202, 0.01202, 0.1544; defects
E/K ≤ 1.06·10⁻⁷, E/T ≤ 9·10⁻⁶) and the tail row at N₁ = 5 141 000 (Q₁ + Q₂ + Q₃ + Q₄ + E₁ = 1.99699937… < 2, margin
3.0·10⁻³; side conditions (S1)–(S4) true; `--direct` term-by-term validation contained on both legs). Cross-check
(`crosscheck-full.txt`, CONSISTENT): T and Q₁ … Q₄ agree across the legs to ≤ 5·10⁻⁷⁹ relative; the E upper bounds are
hull bounds — Arb's the larger on every row (Arb/mp = 1.027, 1.124, 1.261; E₁ 1.000042) — recorded, not gated (etol 0.3;
PLAN-REVIEW F-2). Each leg keeps its own E in its own literal and its own theorem.

**Lean.** `DBN/Asym.lean` (builder, `lane-a/BUILD-NOTES.md`): `checkAsym`, `AsymEnclOK`, `TailOK`, `cert_of_checkAsym`
(PROVED), `windowIdx_mono`, `row2_windowIdx_ge`; `#print axioms` standard (`lane-a/asym-axioms.log`). `Instance02/Asym_mp.lean`,
`Asym_arb.lean` (emitter, `lane-a/EMIT-NOTES.md`): the literals as written in `asym-{mp,arb}.json` (25 integers each), the
kernel facts `row2AsymMP_check`, `row2AsymARB_check` by `decide +kernel` — the kernel's type checking takes **2.0 ms and
4.1 ms** (`lane-a/asym-literal-kernel-time.log`); each module builds in 1.4–1.9 s, import-dominated — and the glue
lemmas `row2_laneA_mp`, `row2_laneA_arb`. Back-parse (`lane-a/backparse.log`): 50 integers compared exactly, 0
mismatches; cross-leg window ranges and N₁ identical, T/K and Q/K to ≤ 5·10⁻¹¹. Root build after the replacement:
*Build completed successfully (9142 jobs)*, `Built Zeta23.DBN.Instance02 (1.7s)`, `Built Zeta23 (11s)`, no warning in any
DBN file (`lane-a/asym-literal-build.log`). Trust greps over `Zeta23/DBN/` (`axiom`, `native_decide`, `unsafe`,
`implemented_by`, `extern`, `opaque`, `sorry`): 0 hits in code, every hit in header prose (`lane-a/trust-greps.log`).
SHA-256 (10(i)), after the phase-3(d) fix pass (22:27 IST; header-only edits, AUDIT-3d.md A-1/A-2 — the pass-1 hashes are in
`lane-a/EMIT-NOTES.md` §5): `Asym_mp.lean` 609e55f223331e4c99554853792a7e7fa97b752f6c2872481de68b289449512a, `Asym_arb.lean`
d669fc31b1908b8db1688f1d0b87d7118541fef4a3806644c835212af6a44740, `Instance02.lean`
810ee7d8d9c73c2cc320b7147bf5ecbc9aae3821884076a06cc65092aa1ca4de.

**What the kernel does not use (PLAN-REVIEW F-6; SPEC §5.1).** `cert_of_checkAsym` consumes only K ≥ 1, C-A3, C-A4
and C-A5. C-A2, C-A6 (the tail row's Σ < 2K) and C-A1's yA² ≥ 1 − 2t₀ are kernel-checked on both literals but never
consumed by a proof: recorded evidence for the prose discharge of Lemma T (SPEC §5.4). "C-A6 is kernel-checked" must
not be read as "the tail reduction is kernel-checked". And `TailOK`'s y-band [y₀, yA] is 9.0·10⁻⁸ wider than the
former `hLaneA`'s y ≤ √(157/250) (yA − √(157/250) = 8.975·10⁻⁸; in the squares yA² − 157/250 = 1.42·10⁻⁷): the tail
hypothesis is "the tail region N ≥ N₁, y ∈ [y₀, yA]", not "part of what `hLaneA` said". [Figure corrected 2026-09-09 22:25 IST after the phase-3(d) audit (AUDIT-3d.md A-1): the earlier "1.5·10⁻⁷" was the gap in the squares.]

**Honest label (SPEC §3.7, verbatim): "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3"** — never "fully machine-checked". The Λ bracket of record stays
0 ≤ Λ ≤ 0.2 (Rodgers–Tao; Platt–Trudgian): nothing here proves Λ ≤ 0.2; what is new is that the whole chain from two
kernel-checked barrier transcripts and two kernel-checked window/tail transcripts to the ray-form statement is closed
in Lean modulo H1, the four enclosure-type Props of H2, and H3.

## Packaging (2026-09-10): the comparator topic `DBN` — `comparator/{ChallengeDeps,Challenge,Solution,PrintAxioms}/DBN.lean`, `ChallengeDeps/DBN/Instance02.lean`, `config-dbn.json`; `formalization.yaml`

**What the topic is (Session 20, RUN-REPORT §6 item 5; record `results/d1-m2a/packaging/BUILD-NOTES.md`).** The M2a ray theorem is
shipped in the parent library's Comparator layout ("one topic per file", `comparator/README.md`), so that a reader who trusts only
Mathlib and the Lean kernel can see WHAT is claimed without reading anything under `Zeta23/`:

| file (under `comparator/`) | module | trusted? | content |
|---|---|---|---|
| `ChallengeDeps/DBN.lean` (562 lines) | `ChallengeDeps.DBN` | yes — read it | the statement vocabulary, `import Mathlib` only: the nine definitions of `DBN/Defs.lean` v1.1, the W1 transcript vocabulary (`W1Row`, `W1Data`, the checker helpers, `segs`, `RowEnclOK`), the barrier lane (`PrismData`, `RectData`, `BarrierData`, `checkPrism`, `checkBarrierChain`, `checkBarrier`, `PrismEnclOK`, `BarrierEnclOK`) and the asymptotic lane (`AsymData`, `checkAsym`, `AsymEnclOK`, `TailOK`) — 79 declarations, each CHARACTER FOR CHARACTER the Zeta23 block (mechanically extracted; source lines in `packaging/gen-challengedeps-table.txt`), under `DBN.*` / `DBN.W1.*` |
| `ChallengeDeps/DBN/Instance02.lean` (20 157 lines) | `ChallengeDeps.DBN.Instance02` | yes — data only | the row-2 literals emitted a SECOND time from the same JSON (`packaging/emit_challengedeps_instance02.py`, a re-targeting of the two program emitters): `row2Rect`, `mp0000…mp0038` + `row2BarrierMP`, `arb0000…arb0071` + `row2BarrierARB`, `row2AsymMP`, `row2AsymARB` — 227 `def` blocks, every one byte-identical to the Zeta23 module's (`cmp-literal-blocks.log`: 2 355 096 bytes, 17 947 row literals, 0 differences); no theorem, no `decide` |
| `Challenge/DBN.lean` | `Challenge.DBN` | yes — read it | seven statements, every proof `sorry`: (G) `dbn_ray_le_point2_of_certificates` — for ANY checker-accepted barrier data on the instance rectangle/final time and ANY checker-accepted asymptotic data with the instance's t₀, y₀, yA and a row at or below N_start, the five displayed hypotheses imply the ray conclusion; (I) `dbn_ray_le_point2_mp`, `dbn_ray_le_point2_arb` — the referee's statements of `lambda_le_point2` / `_arb`, the five hypotheses verbatim over the trusted literal copies; (K) `dbn_row2Barrier{MP,ARB}_checked`, `dbn_row2Asym{MP,ARB}_checked` — the copied literals pass the copied integer checkers |
| `Solution/DBN.lean` | `Solution.DBN` | no (checked by comparator) | the same seven statements byte-for-byte, proved by delegating to `Zeta23.DBN.*`: `rfl` bridges for the copied `def`s, field-wise transports for the re-declared structures with commutation lemmas for the checkers and the enclosure Props, the literal identities decided in the kernel (`decide +kernel`), and one NEW generic lemma `DBNBridge.ray_of_certificates` for (G) (Zeta23 proves only the instance form — fidelity item (f)) |
| `config-dbn.json`, `PrintAxioms/DBN.lean` | — | yes / — | comparator configuration (the seven names; `propext`, `Quot.sound`, `Classical.choice`; `enable_nanoda: true`) and the quick check |

**Quick check (no extra tooling), from the repository root:**

```sh
lake build Solution.DBN && lake env lean comparator/PrintAxioms/DBN.lean
# the three ray statements: '<name>' depends on axioms: [propext, Classical.choice, Quot.sound]
# the four kernel facts (K): [propext, Quot.sound] (barrier) / [propext] (asymptotic) — integer facts on literals
python3 results/d1-m2a/packaging/statement_identity.py .     # challenge = solution statements, textually; exit 0
python3 results/d1-m2a/packaging/trust_greps.py .            # eight patterns, comments stripped; only the 7 challenge sorrys
```

Recorded run (2026-09-10; `results/d1-m2a/packaging/{print-axioms,statement-identity,trust-greps-packaging}.log`):
`Built Solution.DBN (11s)`, *Build completed successfully (8827 jobs)*; the trusted vocabulary module 28 s, the trusted literal
module 38 s; all seven `#print axioms` as stated above, no `sorryAx`, no `Lean.ofReduceBool`; statement identity IDENTICAL ×7; trust
greps code-only 0 for every pattern except the seven `sorry` placeholders of `Challenge/DBN.lean`. The full comparator run (with the
independent `nanoda` kernel) is the stronger check: `lake env /path/to/comparator comparator/config-dbn.json` — see `comparator/README.md`
and, for this program's run, `results/d1-m2a/packaging/COMPARATOR-RUN.md` (Session 20 queue item 1, Job 3).

**Honest label, verbatim (SPEC §3.7): "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3"** — never "fully machine-checked". Every
statement of the topic has the shape "if the displayed hypotheses hold then every H_t with t ≥ 1/5 has only real zeros"; Λ ≤ 0.2 is
not proved and the bracket of record stays 0 ≤ Λ ≤ 0.2. The window range N ∈ [630783, 5140999] is a displayed floor enclosure plus
kernel-checked coverage; the only displayed nonvanishing conclusion is `TailOK` on N ≥ 5 141 000 with the y-band [y₀, yA]
(9.0·10⁻⁸ wider than √(157/250)); C-A6 is kernel-checked but not consumed. The fidelity ledger — where the formal statements differ
from the prose one — is `results/d1-m2a/packaging/FIDELITY.md`, mirrored in `formalization.yaml` (`fidelity.divergences`).
`formalization.yaml` (schema v0.4, at `rh-program/lean/formalization.yaml`) records the program's Lean additions with honest
`automation` (agent; Claude Fable 5.1 and Claude Opus 5; Claude Code) and `review` (`self-assessed`: no human has read
`Challenge/DBN.lean` against the prose statement) fields.

## D-R8 (2026-09-10): f_DH in Lean — `W1/FDH.lean`; `W1/Soundness.lean` generic in the function

**What landed (Session 20; record `results/d1-m2a/dr8/BUILD-NOTES-fDH.md`, pricing `dr8/PRICING-fDH.md`, brief `dr8/BUILD-BRIEF-fDH.md`).**
`Soundness.lean`'s only ζ-specific content (the §9 edge-continuity lemma and the inline `hdiff` block) is replaced by the
generic `continuousOn_logDeriv_seg_of_diffOn` (any f differentiable on an open U ⊇ the segment), and the soundness theorem is
restated as

    Zeta23.W1.cert_of_checkW1_of_diffOn (f : ℂ → ℂ) (hf : DifferentiableOn ℂ f {s | s.re < 1}) (d : W1Data)
        (hc : checkW1 d = true) (hEncl : W1EnclOK f d) (hAP : RectArgPrinciple f) : <the v1 conclusion with f for ζ>

with the v1 body verbatim (`riemannZeta` → `f`, 16 occurrences); `cert_of_checkW1` is its ζ instance with the v1 docstring
and statement character-for-character, and `cert_of_checkW1_ap` in the bridge is untouched (`#check` before/after identical:
`dr8/no-regression.log`). `W1/FDH.lean` (new, 176 lines) defines `kappaDH := (√(10 − 2√5) − 2)/(√5 − 1)` and
`fDH s := 5^{−s}[ζ(s,1/5) + κ ζ(s,2/5) − κ ζ(s,3/5) − ζ(s,4/5)]` on Mathlib's `HurwitzZeta.hurwitzZeta` (FORMAT.md §9.2
verbatim; κ reproduced to 60 digits by three mpmath routes, `dr8/kappa-check.log`), proves `differentiable_fDH` (the poles at
s = 1 cancel pairwise, Mathlib `differentiable_hurwitzZeta_sub_hurwitzZeta`), and states

    Zeta23.W1.cert_of_checkW1_fDH (d : W1Data) (hc : checkW1 d = true) (hEncl : W1EnclOK fDH d) :
        (1 ≤ d.m → ∃ ρ : ℂ, fDH ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1 ∧ T1 d < ρ.im ∧ ρ.im < T2 d)
        ∧ (d.m = 0 → ∀ s ∈ W1Rect d, fDH s ≠ 0)
    Zeta23.W1.mpDH_zero (hEncl : W1EnclOK fDH mpDH) :
        ∃ ρ : ℂ, fDH ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1 ∧ (8569/100 : ℝ) < ρ.im ∧ ρ.im < 8571/100      (and arbDH_zero likewise)

on the UNCHANGED live-fire literals `mpDH`, `arbDH` of `W1/Instances.lean`. `#print axioms` on all of them:
`[propext, Classical.choice, Quot.sound]` (`dr8/fdh-axioms.log`); trust greps with comments stripped: 0 hits
(`dr8/fdh-trust-greps.log`). Build: `lake build Zeta23` — *Build completed successfully (9144 jobs)*, 68 s (the cascade
through `DBN/BarrierCert` and the 116 DBN modules re-elaborated; no DBN or comparator SOURCE changed — SHA-256 identical to the
packaging record, `dr8/untouched.log`; `lake build Solution.DBN` and `PrintAxioms/DBN.lean` re-run clean,
`dr8/solution-dbn-rebuild.log`).

**Honest label, binding (PRICING-fDH.md §3.2, verbatim).** *"f_DH has at least one zero ρ with 1/2 < Re ρ < 1 and 85.69 < Im ρ < 85.71 (the live-fire window; the transcript's rectangle is R = [4/5, 41/50] × [85.69, 85.71]) — kernel-checked modulo the displayed hypothesis H-ENCL_DH (the two producers' enclosures of f_DH on ∂R are true; producers untrusted)."*
What it does NOT say: nothing about ζ (no zero of ζ, nothing about RH, no ζ transcript's label changes); nothing about Λ
(the de Bruijn–Newman chain runs from a zero of ζ or of H_t; f_DH is neither); not "RH-for-DH machine-checked disproof"
(one off-line zero modulo H-ENCL_DH — the witness direction only; the witness's truth is the producers'); not "fully
machine-checked" (H-ENCL_DH is where mpmath/Arb enter, exactly as H-ENCL does for ζ); not a Mathlib fact about
Davenport–Heilbronn. The identification of the producers' f_DH with Lean's `fDH` is a META-level convention match
(Mathlib `hasSum_hurwitzZeta_of_one_lt_re` / `hurwitz_encl.py` STEP 3′ / Arb `acb_hurwitz_zeta`, all Σ_{n≥0}(n+a)^{−s}
with a = j/5 ∈ (0,1)), written in the file's header and in `formalization.yaml` fidelity item (l), never a Lean theorem.
`W1Data` carries no function tag, so the instance corollaries name `fDH` in their statements. The label was swept
through FORMAT.md §9.2, `w1-schema.json`, both producers, both Python checkers and the two DH JSONs (label + comment fields
only; arithmetic byte-identical; re-checked — `dr8/label-sweep-checkers.log`). The module doc of `W1/Instances.lean`
(emitter-written, back-parse-verified, deliberately NOT regenerated) still says "there is NO theorem about f_DH at all":
read that sentence as dated 2026-09-02; this section supersedes it.

## σ-strong sibling (2026-09-10, Session 21): `cert_of_checkW1_of_diffOn'` and the box-form f_DH corollaries

**What landed (record `results/d1-m2a/dr8/BUILD-NOTES-sigma-strong.md`; brief `dr8/BUILD-BRIEF-sigma-strong.md`; the item owed by
D-R8 after the independent checker's FIX-FIRST 1, `dr8/CHECK-fDH-O.md` §12).** The D-R8 witness branch held
`hρmem : ρ ∈ rectOpen (sigma1 d) (sigma2 d) (T1 d) (T2 d)` and weakened its real bounds to the half-strip by `lt_trans`, so
no theorem stated that the zero lies in the transcript's box. `W1/Soundness.lean` now adds, beside the unprimed theorem,

    Zeta23.W1.cert_of_checkW1_of_diffOn' (f : ℂ → ℂ) (hf : DifferentiableOn ℂ f {s : ℂ | s.re < 1})
        (d : W1Data) (hc : checkW1 d = true) (hEncl : W1EnclOK f d) (hAP : RectArgPrinciple f) :
        (1 ≤ d.m → ∃ ρ : ℂ, f ρ = 0 ∧ sigma1 d < ρ.re ∧ ρ.re < sigma2 d
            ∧ T1 d < ρ.im ∧ ρ.im < T2 d) ∧ (d.m = 0 → ∀ s ∈ W1Rect d, f s ≠ 0)

whose body is the unprimed proof line for line with the single witness line `exact ⟨ρ, hρ0, hr1, hr2, hi1, hi2⟩` in place of
the `lt_trans` line (`hhalf`, `hs2lt1` stay in use elsewhere in the body, so nothing is unused). `W1/FDH.lean` adds its f_DH twin
`cert_of_checkW1_fDH'` (same statement shape with `fDH`, H-ENCL_DH the only displayed hypothesis), four unfolding lemmas of the
`mpDH_T1` kind (`mpDH_sigma1 : sigma1 mpDH = 4/5`, `mpDH_sigma2 : sigma2 mpDH = 41/50`, and the Arb twins), and the box-form
live-fire corollaries

    Zeta23.W1.mpDH_zero' (hEncl : W1EnclOK fDH mpDH) :
        ∃ ρ : ℂ, fDH ρ = 0 ∧ (4/5 : ℝ) < ρ.re ∧ ρ.re < 41/50 ∧ 1/2 < ρ.re ∧ ρ.re < 1
          ∧ (8569/100 : ℝ) < ρ.im ∧ ρ.im < 8571/100                                        (and arbDH_zero' likewise)

on the unchanged literals `mpDH`, `arbDH`. `#print axioms` on the four new theorems (and the four lemmas):
`[propext, Classical.choice, Quot.sound]` (`dr8/sigma-strong-axioms.log`). The six frozen theorems `cert_of_checkW1`,
`cert_of_checkW1_ap`, `cert_of_checkW1_fDH`, `cert_of_checkW1_of_diffOn`, `mpDH_zero`, `arbDH_zero` are unchanged
character-for-character, `#check` and axioms before/after identical (`dr8/sigma-strong-no-regression.log`); trust greps with
comments stripped on the two edited files: 0 hits (`dr8/sigma-strong-trust-greps.log`); all 143 files under `Zeta23/DBN/` and
`comparator/` byte-identical before and after (`dr8/sigma-strong-untouched.log`). Build: `lake build Zeta23` — *Build completed
successfully (9144 jobs)*, 0 errors, 83 s (`dr8/sigma-strong-build.log`).

**Label (binding).** For the PRIMED theorems `cert_of_checkW1_fDH'`, `mpDH_zero'`, `arbDH_zero'` only, the box form of
`dr8/PRICING-fDH.md` §3.2 applies, verbatim: *"f_DH has at least one zero in R = [4/5, 41/50] × [85.69, 85.71] with Re s > 1/2 — kernel-checked modulo the displayed hypothesis H-ENCL_DH (the two producers' enclosures of f_DH on ∂R are true; producers untrusted)."*
The unprimed theorems keep the half-strip label of the D-R8 section above. The never-say list is unchanged for both forms:
nothing about ζ, RH or Λ; not "RH-for-DH machine-checked disproof" (one off-line zero modulo H-ENCL_DH, the witness direction
only, the witness's truth the producers'); not "fully machine-checked"; not a Mathlib fact about Davenport–Heilbronn. The trust
label printed by the producers, checkers, `w1-schema.json` and the two live-fire JSONs is not changed: it describes the checker's
acceptance, not the theorem. Fidelity item (m) of `formalization.yaml` is CLOSED by this section.

## M3 seed (2026-09-10): `W1/Ledger.lean` and `results/d1-m3/`

The exclusion ledger of D1's charter (line 48) and D-R6 is SEEDED with the four M1 v1 acceptance null boxes — eight ζ
exclusion transcripts already on disk, zero producer compute (`results/d1-m2a/dr8/PRICING-M3-ledger.md` §2; layout §1.3).
`W1/Ledger.lean` (new, 95 lines) carries one corollary per leg, the m = 0 branch of `cert_of_checkW1_ap` on the unchanged
literal:

    Zeta23.W1.mpNullT100_exclusion (hEncl : W1EnclOK riemannZeta mpNullT100) : ∀ s ∈ W1Rect mpNullT100, riemannZeta s ≠ 0

(and `arbNullT100`, `mpNullT1000`, `arbNullT1000`, `mpNullT10000`, `arbNullT10000`, `mpNullDeepT100`, `arbNullDeepT100`
likewise; each `(cert_of_checkW1_ap d (checkW1Floor_spec d_check).1 hEncl).2 (by decide)`; axioms
`[propext, Classical.choice, Quot.sound]`). Rows R1 [3/5, 9/10] × [100, 101], R2 [3/5, 9/10] × [1000, 1001],
R3 [3/5, 9/10] × [10000, 10001] (δ₀ = 1/10), R4 [21/40, 39/40] × [100, 101] (δ₀ = 1/40); provenance `acceptance`; status
`accepted` (both legs ACCEPTed by both Python checkers, kernel-checked, cross-check CONSISTENT, hashes re-verified —
`results/d1-m3/ledger_check.py` PASS, `dr8/ledger-check.log`). **Label per row (binding):** *"no zeros of ζ in the closed
box, kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)"* — the single-box sentence; never "RH
verified in [T₁, T₂]" (a box has σ₁ > ½ strictly; a range statement needs a Turing-method count the format does not carry);
nothing about ζ outside the box; nothing about Λ; no aggregate (isolated boxes extend no contiguous record). All four boxes
lie far below the 3·10¹² record: they are format-validation rows in the program's own trust vocabulary, not a verification
result. No row program (2b: NO-GO), no calibration rows run.

## WeilContainment (Session 30, 2026-09-28/29): barrier-zoo IV.1 in Lean over Mathlib alone — `comparator/{ChallengeDeps,Challenge,Solution,PrintAxioms}/WeilContainment.lean`, `Challenge/Solution/PrintAxioms/WeilContainmentOne.lean`, `config-weil-containment{,-one}.json`

**What the topics are (D5, F3/G4; brief `results/d5-lean-s30/BRIEF.md`, build record `results/d5-lean-s30/BUILD-NOTES.md`, ledger
`results/d5-lean-s30/FIDELITY.md`).** The C1 containment theorem of the barrier zoo (IV.1; `results/adjudication-C1.json` fatal 2 and its
mandatory repair: "the full (a,w)-family of prime-computable tilted-EF observables at cutoff X lies inside the classical
bandwidth-log X Weil-EF data class") as Comparator pairs whose TRUSTED side imports Mathlib only — no Zeta23 module is imported on
either side, so a reader who trusts Mathlib and the kernel reads `ChallengeDeps/WeilContainment.lean` (63 lines) and the two
challenge files and nothing else:

| file (under `comparator/`) | module | trusted? | content |
|---|---|---|---|
| `ChallengeDeps/WeilContainment.lean` | `ChallengeDeps.WeilContainment` | yes — read it | namespace `WeilContainment`: `tilt a u := exp(−(a − 1/2)·|u|)`; `weilTestOf a g u := (1/2)·g u·tilt a u`; `primeSide k := ∑' n : ℕ, (Λ(n)/√n)·(k(log n) + k(−log n))` — Zeta23's `literatureRHS` prime term CHARACTER FOR CHARACTER (`Zeta23/ExplicitFormula.lean`), re-declared so that the module imports Mathlib only; `tiltedPrimeSide a g := ∑' n : ℕ, Λ(n)·n^{−a}·g(log n)` — C1's master-formula prime side |
| `Challenge/WeilContainmentOne.lean` | `Challenge.WeilContainmentOne` | yes — read it | rung 1 (10(l)): `weilContainment_identity_one` — for every even g, `tiltedPrimeSide 1 g = primeSide (weilTestOf 1 g)`; `sorry` |
| `Challenge/WeilContainment.lean` | `Challenge.WeilContainment` | yes — read it | twelve statements, every proof `sorry`: (T1) `weilContainment_identity` (every real a, every even g, no summability hypothesis), `weilContainment_cutoff` (tsupport g ⊆ [−L, L] ⟹ the tsum IS the finite sum over n ≤ ⌊e^L⌋); (T2) `weilContainment_tilt_bounds` (e^{−|a−1/2|L} ≤ tilt a u ≤ e^{|a−1/2|L} on |u| ≤ L), `weilContainment_tilt_pos`; (T3) `weilContainment_tilt_inv` (tilt a · tilt (1−a) = 1), `weilContainment_even`, `weilContainment_tsupport`, `weilContainment_tsupport_eq` (= tsupport g), `weilContainment_continuous`, `weilContainment_exact` (the converse containment, witness g = 2k·tilt (1−a)), `weilContainment_range_eq` (for every real a and L: {tilted data over even band-[−L, L] tests} = {classical prime data over even band-[−L, L] tests}); and `weilContainment_not_contDiff` (¬ ContDiff ℝ 2 (weilTestOf 1 1): the C² class is not preserved by the tilt) |
| `Solution/WeilContainmentOne.lean`, `Solution/WeilContainment.lean` | `Solution.*` | no (checked by comparator) | the same statements byte-for-byte, proved over Mathlib alone: the term-by-term rpow computation (`tilt a (log n) = n^{1/2−a}`, `(Λ/√n)·n^{1/2−a} = Λ·n^{−a}`, Λ(0) = 0 at n = 0) and `tsum_congr` for (T1); `tsum_eq_sum` for the cutoff; `exp_le_exp` for (T2); support/continuity lemmas, `exp_add` and `linear_combination` for (T3); `not_differentiableAt_abs_zero` through `Complex.reCLM` for the witness |
| `config-weil-containment-one.json`, `config-weil-containment.json`, `PrintAxioms/WeilContainment{One,}.lean` | — | yes / — | comparator configurations (1 and 12 names; `propext`, `Quot.sound`, `Classical.choice`; `enable_nanoda: true`) and the quick checks |

**Quick check (no extra tooling), from the repository root:**

```sh
lake build Solution.WeilContainmentOne Solution.WeilContainment
lake env lean comparator/PrintAxioms/WeilContainmentOne.lean     # [propext, Classical.choice, Quot.sound]
lake env lean comparator/PrintAxioms/WeilContainment.lean        # twelve lines, each [propext, Classical.choice, Quot.sound]
python3 results/d5-lean-s30/tools/statement_identity_d5.py . WeilContainment <the twelve names>   # IDENTICAL ×12
python3 results/d5-lean-s30/tools/trust_greps_d5.py . <the seven topic files>                     # the 13 challenge sorrys only
```

Recorded runs (2026-09-28/29, `results/d5-lean-s30/`): `rung0-program-tree.log` (challenges: *8699 jobs*, the 1 + 12 deliberate
`sorry` warnings), rung 1 and the family solutions *Build completed successfully (8698 / 8699 jobs)*, 0 errors, 0 warnings;
`rung1-print-axioms.log`, `print-axioms.log`; `statement-identity.log` (1 + 12 IDENTICAL); `trust-greps.log`; the Comparator runs with
nanoda `rung1-comparator.log` and `comparator-run.log` (second run, twelve names) — `Nanoda kernel accepts the solution`, `Lean
default kernel accepts the solution`, `Your solution is okay!`, exit 0 (runner `tools/run.sh`; NOT sandboxed, the fake-landrun shim
as in every prior record).

**The second toolchain (rung 0 of the brief, the check build across the toolchain gap).** The same trusted vocabulary and the same
13 statements were built a second time at Lean **v4.33.1** / Mathlib **0df444a360eaa60ab8c11dca51a86af692955474** — Prove2Me's
default environment — in the platform's layout at `~/prove2me_workspace` (`Definitions/Def_WeilContainment.lean`, thirteen
`Theorems/Thm_WeilContainment_<suffix>.lean` stubs ending `by sorry`, thirteen `Solutions/Sol_WeilContainment_<suffix>.lean` with a
top-level `theorem solution`, generated from the challenge files by `results/d5-lean-s30/tools/gen_prove2me_{layout,solutions}.py`
so that the statement text is byte-identical in the three places): `rung0-prove2me-env.log` (*8718 jobs*), `prove2me-build.log`
(*8732 jobs*, 0 errors), `prove2me-print-axioms.log` (`#print axioms solution` ×13 = the three axioms; the platform's three gating
rules checked). **Nothing was posted to Prove2Me** — no mission, no proposal, no API call; that is the sponsor's decision.

**Honest label, verbatim (BRIEF §1(4)): "IV.1 formalized-in-Lean (prime-side containment; Comparator-checked over Mathlib alone,
no displayed hypothesis, axioms propext/Classical.choice/Quot.sound, replayed by nanoda; built at v4.33.0-rc2/51e6992e and
v4.33.1/0df444a)".** What it means: the level-a tilted prime data and the classical band-L Weil prime data are the same set of
numbers, for every real a, through multipliers bounded by e^{±|a−1/2|L}. What it does NOT say (FIDELITY.md §2): nothing about the
ZERO side of any explicit formula at any level (fatal 1's "cosh ghost" stands), nothing about Zeta23's C² test class `EF_lit` (the
tilt breaks it — the witness theorem), nothing about the μ-band or any nonlinear function of the band, nothing about ζ or RH. The
fidelity ledger — `tsum` over all n in place of "n ≤ X" (equal by the theorem `weilContainment_cutoff`), the algebraic inverse in
place of "analytic continuation", the restated prime term, an arbitrary even g in place of the cos-transform of a window — is
`results/d5-lean-s30/FIDELITY.md`, mirrored in `formalization.yaml` (`fidelity.divergences` row (u)). The brief's single-model
pre-derivation was attacked first; its six errata (`results/d5-lean-s30/PREDERIVATION-ERRATA.md`) added `even`, `tsupport_eq`,
`cutoff`, `range_eq` and dropped a redundant hypothesis — the statements follow the corrected mathematics, not the brief.

## WeilContainmentC2 (Session 32, 2026-09-29): the D5 ledger's (N2) refinement for continuous g — `comparator/{Challenge,Solution,PrintAxioms}/WeilContainmentC2.lean`, `Challenge/Solution/PrintAxioms/WeilContainmentC2One.lean`, `config-weil-containment-c2{,-one}.json`

**What the topics are (H5; brief `results/h5-c2-lean-s32/BRIEF.md`, build record `results/h5-c2-lean-s32/BUILD-NOTES.md`, ledger
`results/h5-c2-lean-s32/FIDELITY.md`).** The D5 ledger's "not covered" item (N2), as corrected by CHECK-O F2 — "the refinement 'every
tilted datum equals `primeSide k′` for some C² even k′ on the same band' is true for g continuous … but is NOT formalized" — made a
theorem, for continuous g, over the SAME Mathlib-only trusted layer (`ChallengeDeps/WeilContainment.lean`, unchanged; `primeSide`,
`tiltedPrimeSide`). No new trusted definition; no Zeta23 import on either side:

| file (under `comparator/`) | module | trusted? | content |
|---|---|---|---|
| `Challenge/WeilContainmentC2One.lean` | `Challenge.WeilContainmentC2One` | yes — read it | rung 1 (10(l)), the band L = log 3 (n = 2 interior, n = 3 at the edge): `weilContainment_c2_interpolant_log3` — for every real a and every g even, continuous, with `tsupport g ⊆ Set.Icc (-(Real.log 3)) (Real.log 3)`, `∃ k, (∀ u, k (-u) = k u) ∧ ContDiff ℝ 2 k ∧ tsupport k ⊆ Set.Icc (-(Real.log 3)) (Real.log 3) ∧ primeSide k = tiltedPrimeSide a g`; `sorry` |
| `Challenge/WeilContainmentC2.lean` | `Challenge.WeilContainmentC2` | yes — read it | the family: `weilContainment_c2_interpolant` — for every real a and L and every g even, continuous, with `tsupport g ⊆ Set.Icc (-L) L`, the same conclusion on the band [−L, L]; `sorry` |
| `Solution/WeilContainmentC2One.lean`, `Solution/WeilContainmentC2.lean` | `Solution.*` | no (checked by comparator) | the same statements byte-for-byte, proved over Mathlib alone (each module self-contained; neither imports the challenge or the D5 solution). Witness: with I = {2 ≤ n ≤ ⌊e^L⌋ : log n < L}, if I = ∅ then k = 0; else k(u) = P(u²)·φ(u), φ one `ContDiffBump (0 : ℝ)` with rIn = log (max I), rOut = L (`one_of_mem_closedBall`, `zero_of_le_dist`, `tsupport_eq`, `ContDiffBump.neg`, `ContDiffBump.contDiff`), P = `Lagrange.interpolate` with nodes (log n)² and values (1/2)·n^{1/2−a}·g(log n) (`eval_interpolate_at_node`; nodes distinct by `pow_left_inj₀` and `Real.log_injOn_pos`); the prime side term by term (the D5 rpow identity on I; Λ(0) = Λ(1) = 0; φ(±log n) = 0 and g(log n) = 0 for log n ≥ L — the zero set of a continuous g is closed and contains (L, ∞)); `tsum_eq_sum`, `Finset.sum_subset`, and the D5 cutoff re-proved locally |
| `config-weil-containment-c2-one.json`, `config-weil-containment-c2.json`, `PrintAxioms/WeilContainmentC2{One,}.lean` | — | yes / — | comparator configurations (one name each; `propext`, `Quot.sound`, `Classical.choice`; `enable_nanoda: true`) and the quick checks |

**Quick check (no extra tooling), from the repository root:**

```sh
lake build Solution.WeilContainmentC2One Solution.WeilContainmentC2
lake env lean comparator/PrintAxioms/WeilContainmentC2One.lean   # [propext, Classical.choice, Quot.sound]
lake env lean comparator/PrintAxioms/WeilContainmentC2.lean      # [propext, Classical.choice, Quot.sound]
python3 results/h5-c2-lean-s32/tools/statement_identity_h5.py . WeilContainmentC2One weilContainment_c2_interpolant_log3
python3 results/h5-c2-lean-s32/tools/statement_identity_h5.py . WeilContainmentC2 weilContainment_c2_interpolant
python3 results/h5-c2-lean-s32/tools/trust_greps_h5.py . <the seven topic files>   # the 2 challenge sorrys only
```

Recorded runs (2026-09-29, `results/h5-c2-lean-s32/`): both solutions *Build completed successfully (8698 jobs)*, 0 errors, 0 warnings;
`rung1-print-axioms.log`, `print-axioms.log`; `statement-identity.log` (1 + 1 IDENTICAL, tree and mirror); `trust-greps.log`; the
Comparator runs with nanoda `rung1-comparator.log` and `comparator-run.log` — `Nanoda kernel accepts the solution`, `Lean default kernel
accepts the solution`, `Your solution is okay!`, exit 0 (runner `tools/run.sh`; NOT sandboxed, the fake-landrun shim as in every prior
macOS record).

**Honest label, verbatim (BRIEF §1(4), the reader's A7): "IV.1 formalized-in-Lean — prime-side containment into Zeta23's C² test class
for continuous g (prime-side values; the C² witness is an interpolant at ±log n, not the tilted test; zero side untouched)".** What it
means: for every continuous even band-limited g and every real a, the level-a tilted prime NUMBER of g is the classical prime datum
of some even C² test on the same band — a member of the class `EF_lit` quantifies over. What it does NOT say (FIDELITY.md §2): the
tilted test k_{a,g} itself is not in general C² and is not claimed to be (D5's (N2) and `weilContainment_not_contDiff` stand; that theorem is the one instance a = 1, g ≡ 1 — CHECK-O F2, Session 32); nothing about the
ZERO side of any explicit formula at any level; `EF_lit` is not stated and nothing is fed into it; nothing for discontinuous g (the
band-edge counterexample of D5 CHECK-O F2 stands); nothing about the μ-band, ζ, or RH. The hypotheses displayed are exactly g even,
`Continuous g`, `tsupport g ⊆ Set.Icc (-L) L`; the evenness of g is not used by the proof (`results/h5-c2-lean-s32/PREDERIVATION-ERRATA.md`
E2). The fidelity ledger is `results/h5-c2-lean-s32/FIDELITY.md`, mirrored in `formalization.yaml` (`fidelity.divergences` row (x)); the D5
row (u)'s (N2) sentence carries a dated FORMALIZED pointer to it.

## I1Witness (Session 32, 2026-09-29): barrier-zoo I.1's one-line witnesses as kernel-checked values of the von Mangoldt recursion — `comparator/{ChallengeDeps,Challenge,Solution,PrintAxioms}/I1Witness.lean`, `Challenge/Solution/PrintAxioms/EpsteinWitnessSix.lean`, `config-i1-witness.json`, `config-epstein-witness-six.json`

**What the topics are (H3 item 6; brief `results/i1-witness-lean-s32/BRIEF.md`, typing record `typing.log`, build record
`BUILD-NOTES.md`, ledger `FIDELITY.md`).** The exact witnesses of zoo I.1 and of formalization-queue item 6 (BARRIER-ZOO.md line 666:
"the witness arithmetic is kernel-checkable") — Epstein Λ_Q(6) = 2 log 6 and Λ_Q(36) = −4 log 6 for x² + 5y², Davenport–Heilbronn
Λ_DH(3), Λ_DH(4), Λ_DH(6), Λ_DH(12) — as VALUES of the von Mangoldt recursion on the coefficient arrays, over a Mathlib-only trusted
layer. The recursion is solved with log n replaced by the exponent vector (`lambdaVec b n p` = the coefficient of log p), so that the
Epstein values are ring arithmetic on ℚ the kernel decides, and the DH values are polynomial identities in κ closed by `ring`:

| file (under `comparator/`) | module | trusted? | content |
|---|---|---|---|
| `ChallengeDeps/I1Witness.lean` | `ChallengeDeps.I1Witness` | yes — read it | Mathlib only, namespace `I1Witness`: `lambdaVecAux` (the recursion with a fuel), `lambdaVec b n p := lambdaVecAux b p n n`, `LambdaReal b n := Σ_{p ≤ n prime} lambdaVec b n p · Real.log p`, `epsteinB n := (card of {(x, y) ∈ Icc (−n) n × Icc (−n) n : x² + 5y² = n} : ℚ) / 2`, `kappa := (√(10 − 2√5) − 2)/(√5 − 1)`, `dhA n := (1, κ, −κ, −1, 0)` at n % 5 = 1, 2, 3, 4, 0 |
| `Challenge/EpsteinWitnessSix.lean` | `Challenge.EpsteinWitnessSix` | yes — read it | rung 1 (10(l)): `epsteinB_one`, `epstein_six_coeff` (2 and 2 at p = 2, 3), `epstein_witness_6` (= 2 log 2 + 2 log 3 = 2 log 6 > 0); `sorry` |
| `Challenge/I1Witness.lean` | `Challenge.I1Witness` | yes — read it | fourteen statements: the recursion lemmas `lambdaVec_rec` (for every commutative ring — the record's recursion for arrays with b₁ = 1, CHECK-O F1: `2 ≤ n → lambdaVec b n p = b n * padicValNat p n − ∑ d ∈ n.properDivisors, lambdaVec b d p * b (n / d)`), `lambdaVec_one`, `lambdaVec_eq_zero_of_not_dvd`; Epstein `epsteinB_one`, `epstein_thirtysix_coeff` (−4, −4, and 0 at every other prime), `epstein_witness_36` (= −4 log 2 − 4 log 3 = −4 log 6 < 0); DH `kappa_pos`, `dhA_one`, `dh_three_coeff`, `dh_witness_3` (= −κ log 3 < 0), `dh_twelve_coeff` (−κ(1 + κ²)·2 and −κ(1 + κ²)), `dh_witness_12` (= −κ(1 + κ²)(2 log 2 + log 3) = −κ(1 + κ²) log 12 < 0), `dh_four` (= −(2 + κ²) log 2 < 0), `dh_six` (= (1 + κ²) log 6 > 0); `sorry` |
| `Solution/EpsteinWitnessSix.lean`, `Solution/I1Witness.lean` | `Solution.*` | no (checked by comparator) | the same statements byte-identical, proved over Mathlib alone (each module self-contained): the fuel is shown irrelevant once ≥ n (strong induction), which gives the recursion; the Epstein coefficients by `decide +kernel` (77 ms at n = 6, about 3.6 s per coefficient at n = 36 — `typing.log`); the other primes by `lambdaVec_eq_zero_of_not_dvd` (a prime dividing 2^a·3^b is 2 or 3); the DH coefficients through the recursion over `Nat.properDivisors` (decided) and `ring`; `kappa_pos` by `Real.lt_sqrt`, `Real.sqrt_lt'` |
| `config-epstein-witness-six.json`, `config-i1-witness.json`, `PrintAxioms/EpsteinWitnessSix.lean`, `PrintAxioms/I1Witness.lean` | — | yes / — | comparator configurations (3 and 14 names; `propext`, `Quot.sound`, `Classical.choice`; `enable_nanoda: true`) and the quick checks |

**Quick check (no extra tooling), from the repository root:**

```sh
lake build Solution.EpsteinWitnessSix Solution.I1Witness
lake env lean comparator/PrintAxioms/EpsteinWitnessSix.lean   # 3 lines, each [propext, Classical.choice, Quot.sound]
lake env lean comparator/PrintAxioms/I1Witness.lean           # 14 lines, each [propext, Classical.choice, Quot.sound]
python3 results/i1-witness-lean-s32/tools/statement_identity_i1.py . EpsteinWitnessSix epsteinB_one epstein_six_coeff epstein_witness_6
python3 results/i1-witness-lean-s32/tools/statement_identity_i1.py . I1Witness <the fourteen names>
python3 results/i1-witness-lean-s32/tools/trust_greps_i1.py . <the seven topic files>   # the 3 + 14 challenge sorrys only
```

Recorded runs (2026-09-29, `results/i1-witness-lean-s32/`): both solutions *Build completed successfully (8698 jobs)*, 0 errors, 0
warnings, first try (`build-i1witness.log` covers the I1Witness build; the rung-1 build's figures are the builder's console reading, logged only in the checker's `check-O/` — CHECK-O F4, Session 32); `rung1-print-axioms.log`, `print-axioms.log`; `rung1-statement-identity.log`,
`statement-identity.log` (3 + 14 IDENTICAL, tree and mirror); `rung1-trust-greps.log`, `trust-greps.log`; the Comparator runs with
nanoda `rung1-comparator.log` (30 s) and `comparator-run.log` (48 s) — `Nanoda kernel accepts the solution`, `Lean default kernel
accepts the solution`, `Your solution is okay!`, exit 0 (runner `tools/run.sh`; NOT sandboxed, the fake-landrun shim as in every prior
macOS record).

**Honest label, verbatim (BRIEF §1(4)): "I.1's witness table kernel-checked — for the Epstein form x² + 5y² (h = 2), Λ_Q(36) = −4 log 2
− 4 log 3 < 0 (and Λ_Q(6) = 2 log 6 off prime powers); for Davenport–Heilbronn, Λ_DH(3) = −κ log 3 < 0 and Λ_DH(12) = −κ(1 + κ²) log 12 < 0
with κ > 0 from its closed form — where Λ_f is the von Mangoldt recursion's coefficient sequence on the array with b₁ = 1; over Mathlib
alone, the three standard axioms, replayed by nanoda; the identification of that sequence with −F′/F as Dirichlet series is not
formalized".** What it means: the one-line witnesses I.1's executable test points at ("consumes Λ(n) ≥ 0; Λ_DH(12) < 0") are now
kernel-checked values, not computations. What it does NOT say (FIDELITY.md §2): the identification of the recursion's sequence with −F′/F
is the classical identity, by hand; nothing about the Euler product of either function as a theorem (the witness is a value; "no Euler
product" is the zoo's reading); nothing about the analytic continuation, functional equation or off-line zero of the Davenport–Heilbronn
function, nothing about the zeros of any Epstein zeta function; no decimal value is stated; nothing about ζ or RH. No displayed
hypothesis (the recursion lemmas' `2 ≤ n` and `¬ p ∣ n` are their subjects). The fidelity ledger is `results/i1-witness-lean-s32/FIDELITY.md`,
mirrored in `formalization.yaml` (`fidelity.divergences` row (y)).

## IntegralityGap (Session 30, 2026-09-29): barrier-zoo IV.17 in Lean — the master inequality holds over ℤ and FAILS over ℚ on the same grid row — `Zeta23/PairCeiling/GridParsevalRat.lean`, `GridGap.lean`, `comparator/{ChallengeDeps,Challenge,Solution,PrintAxioms}/IntegralityGap.lean`, `config-integrality-gap.json`

**What the topic is (G8; brief `results/iv17-lean-s30/BRIEF.md`, typing check `TYPING-NOTE.md`, build record `BUILD-NOTES.md`, ledger
`FIDELITY.md`).** The fractional-mark integrality barrier of the barrier zoo (IV.17; A4 no-go paper §2.4, §4.2; `theorems.md` Lemma 2.2;
formalization-queue item 10) as ONE Comparator topic: the master inequality (MI) `3·Σm − Σm² ≤ 2·N_d` — the whole content of the 5/6
corner — is a theorem over nonnegative INTEGER marks on every grid and a FALSEHOOD over nonnegative RATIONAL marks on the SAME
bandwidth-one Frobenius row, witnessed by the zoo's instance (48 atoms of mark 4/3 on the 65-site grid: mass 64, Σm² = 256/3, N_d = 48,
3·64 − 2·48 = 96 > 256/3), with the line where integrality is consumed a named theorem. The integer half was already on disk
(`GridParseval.two_mul_distinct_ge`, `GridCorner.gridRow_eq`); what this unit adds is grid Parseval with rational marks, the
kernel-checked instance, the negations, and the packaging:

| file | module | trusted? | content |
|---|---|---|---|
| `Zeta23/PairCeiling/GridParsevalRat.lean` | `Zeta23.PairCeiling.GridParsevalRat` | no (source of the proofs) | Parseval and the flat-band collapse for a GENERAL coefficient vector `dftVec : ZMod M → K` over `[CommRing K] [IsDomain K]` (the integer file's proofs word for word); `dftMarkQ` (rational marks, over a `Field` — the cast ℚ → K needs a division ring, item 10's typing fact) and `dftMark` as its `rfl` instances; the ℂ specialization with `map_ratCast` for `map_intCast`; `trace_sq_grid_rat`, `gridRowQ`, `gridRowQ_eq`, `gridRow_eq_gridRowQ` |
| `Zeta23/PairCeiling/GridGap.lean` | `Zeta23.PairCeiling.GridGap` | no (source of the proofs) | `per_atom_slack : ∀ m : ℤ, 0 ≤ (m − 1)(m − 2)` and `per_atom_floor : ∀ m : ℤ, m ≤ m²` with their failures over ℚ (at 4/3 and 1/2); `fracMark` and its kernel facts (`decide +kernel`: mass 64, Σm² = 256/3, N_d = 48; row = (4/3)·64·(1 + 0)); `mi_holds_integer` (re-export of `two_mul_distinct_ge`); `mi_fails_rational`; `corner_fails_rational`, `corner_bound_fails_rational` |
| `comparator/ChallengeDeps/IntegralityGap.lean` | `ChallengeDeps.IntegralityGap` | yes — read it | Mathlib only, namespace `IntegralityGap`: `chi`, `dftMark`, `dftMarkQ`, `zetaM`, `gridRow`, `gridRowQ`, `fracMark`, character for character the Zeta23 definitions |
| `comparator/Challenge/IntegralityGap.lean` | `Challenge.IntegralityGap` | yes — read it | the sixteen statements with `sorry`, and the WHAT IS CLAIMED / NOT paragraph |
| `comparator/Solution/IntegralityGap.lean` | `Solution.IntegralityGap` | no | the sixteen statements byte-identical, each proved by delegation to the Zeta23 modules (definitional unfolding) |
| `config-integrality-gap.json`, `PrintAxioms/IntegralityGap.lean` | — | yes / — | comparator configuration (16 names; `propext`, `Quot.sound`, `Classical.choice`; `enable_nanoda: true`) and the quick check |

**Quick check (no extra tooling), from the repository root:**

```sh
lake build Solution.IntegralityGap
lake env lean comparator/PrintAxioms/IntegralityGap.lean          # sixteen lines, each [propext, Classical.choice, Quot.sound]
python3 results/iv17-lean-s30/tools/statement_identity_g8.py . IntegralityGap <the sixteen names>   # IDENTICAL ×16
python3 results/iv17-lean-s30/tools/trust_greps_g8.py . <the six topic files>                       # the 16 challenge sorrys only
```

Recorded runs (2026-09-29, `results/iv17-lean-s30/`): `build-gridparsevalrat.log`, `build-gridgap.log` (each module built alone, 0
errors, 0 warnings), `build-comparator-topic.log` (`lake build Challenge.IntegralityGap Solution.IntegralityGap`: *8703 jobs*, the 16
deliberate `sorry` warnings of the challenge, 0 warnings from the solution); `print-axioms.log` (16 root names + 21 Zeta23 sources);
`statement-identity.log` (16 IDENTICAL, tree and mirror); `trust-greps.log`; the Comparator run with nanoda `comparator.log` —
`Nanoda kernel accepts the solution`, `Lean default kernel accepts the solution`, `Your solution is okay!`, exit 0, 31 s (runner
`tools/run.sh`; NOT sandboxed, the fake-landrun shim as in every prior record).

**Honest label, verbatim (BRIEF §1(6)): "IV.17's master inequality is a Comparator-checked theorem over integer marks and a
Comparator-checked FALSEHOOD over rational marks on the same Frobenius row (the mark-4/3 instance kernel-checked), over Mathlib alone,
no displayed hypothesis, axioms propext/Classical.choice/Quot.sound, replayed by nanoda".** What it means: the textbook integrality gap
of IV.17's Reading is a kernel-checked fact on the grid — the same inequality, the same row, integer marks yes, rational marks no — and
the line where integrality is consumed is `per_atom_slack` (IV.17 EXECUTABLE TEST (3) can now point at a theorem name). What it does
NOT say (FIDELITY.md §2): nothing about LAWS (the pointwise failure is stated, the law form is not), nothing about the PAIR CHANNEL (paper Prop. 4.5 is not in this topic — [Session 33: it is the topic PairChannel, section below; Theorems 4.6–4.9 stay at paper grade]), nothing about the two-sided band or any budget other than the
bandwidth-one grid row, nothing off the grid, nothing about ζ or RH. The fidelity ledger — the row's normalization, `ZMod 65` for "the
(N+1)-site grid", the instance at ε = 0, (MI) negated in the `3·Σm − Σm²` form, the general-coefficient Parseval — is
`results/iv17-lean-s30/FIDELITY.md`, mirrored in `formalization.yaml` (`fidelity.divergences` row (v)).

## PairChannel (Session 33, 2026-09-29): barrier-zoo IV.17's pair channel in Lean — Prop. 4.5 for every depth and real mark, the integer-mark safety chain, and the floor F1 ≥ S2's failure at the anchor kernel-checked — `Zeta23/PairCeiling/PairRow.lean`, `PairCert.lean`, `comparator/{ChallengeDeps,Challenge,Solution,PrintAxioms}/PairChannel.lean`, `config-pair-channel.json`

**What the topic is (H4; unit brief `results/h4-pair-typing-s32/UNIT-BRIEF.md`, typing note `TYPING-NOTE.md` there, build record
`results/h4-pair-lean-s33/BUILD-NOTES.md`, ledger `FIDELITY.md`, the attack on the note's derivations `PREDERIVATION-ERRATA.md`).** The
pair channel of barrier-zoo IV.17 (A4 no-go paper §2.3, §4.2 Prop. 4.5; `pair-channel.md` §0–§4 Prop. 3.1, (T1), (T3)) as ONE Comparator
topic. The shipped grid rows `gridRow`/`gridRowQ` index the form factor at the REDUCED residue mod 2n+1, which is right for grid atoms and
wrong for a conjugate pair: its factor 2μ cosh(2πsd/N) grows with |s|. So `PairRow.lean` defines the paper's row over the UNREDUCED
integer frequency s ∈ [−2n, 2n] — `W2 n s` (the flat-weight autocorrelation), `pairFormFactor` (atoms' DFT at the reduced residue plus,
per pair on a grid site, 2μ cosh(2πsd/N) at the unreduced s times the character), `pairRow`, `abar` (ā(x) = Σ_j (1/M) cosh(2πjx/N)),
`vacancyMark` (unit atoms off the hole) — and proves, for every n:

| file | module | trusted? | content |
|---|---|---|---|
| `Zeta23/PairCeiling/PairRow.lean` | `Zeta23.PairCeiling.PairRow` | no (source of the proofs) | `W2_eq` (the closed form (2n+1 − \|s\|)/(2n+1)²), `sum_W2_mul` (the regrouping of the single s-sum into the double band sum), `pairRow_eq_gridRowQ` (with NO pair the new row IS the shipped rational grid row — the agreement lemma), `sum_W2_cosh` (the generating identity (T1) at imaginary argument, Σ_s W2(s) cosh(2πsx/N) = ā(x)²); `prop45` — Prop. 4.5 for EVERY n, depth d and real mark μ: on the vacancy lattice plus one pair at the hole, F1 − S2 = 2μ²ā(2d)² − 4μ(ā(d)² − 1), S2 = 2n + 2μ²; `abar_sq_le` (ā(d)² ≤ (1 + ā(2d))/2, Cauchy–Schwarz on the flat weights), `floor_holds_integer` (for an INTEGER mark m ≥ 1 the expression is > 0 — integrality enters as 1 ≤ m, nowhere else) |
| `Zeta23/PairCeiling/PairCert.lean` | `Zeta23.PairCeiling.PairCert` | no (source of the proofs) | the dyadic certificate at the record's anchor n = 32, (d, μ) = (1/4, 1/20): `floor_fails_anchor : pairRow 32 (vacancyMark 32) {(0, 1/20, 1/4)} < 64 + 2·(1/20)²` — the floor F1 ≥ S2 FAILS for this real mark. Two generic bounds `one_add_sq_half_le_cosh` (1 + x²/2 ≤ cosh x) and `cosh_le_poly8` (cosh x ≤ 1 + x²/2 + x⁴/24 + x⁶/720 + x⁸/20160 for \|x\| ≤ 9/2; the ℝ transfer of `Complex.exp_bound'`) passed through the flat average symbolically; the four integer power sums S₂ = 22880, S₄ = 14492192, S₆ = 10924353440, S₈ = 8964042662432 by `decide +kernel`; `Real.pi_gt_d6`/`pi_lt_d6`; one `norm_num` (`cert_numeric`, a rational with a 133-digit denominator). The module builds in 1.8 s (`cert-build.log`) |
| `comparator/ChallengeDeps/PairChannel.lean` | `ChallengeDeps.PairChannel` | yes — read it | Mathlib only, namespace `PairChannel`: the seven IntegralityGap definitions (`chi`, `dftMark`, `dftMarkQ`, `zetaM`, `gridRow`, `gridRowQ`, `fracMark`) and the five of PairRow.lean (`W2`, `pairFormFactor`, `pairRow`, `abar`, `vacancyMark`), character for character |
| `comparator/Challenge/PairChannel.lean` | `Challenge.PairChannel` | yes — read it | the eight statements with `sorry` (the typing probe's text byte for byte), and the WHAT IS CLAIMED / NOT paragraph |
| `comparator/Solution/PairChannel.lean` | `Solution.PairChannel` | no | the eight statements byte-identical, each proved by delegation to the two Zeta23 modules (definitional unfolding) |
| `config-pair-channel.json`, `PrintAxioms/PairChannel.lean` | — | yes / — | comparator configuration (8 names; `propext`, `Quot.sound`, `Classical.choice`; `enable_nanoda: true`) and the quick check |

**Quick check (no extra tooling), from the repository root:**

```sh
lake build Solution.PairChannel
lake env lean comparator/PrintAxioms/PairChannel.lean                # eight lines, each [propext, Classical.choice, Quot.sound]
python3 results/h4-pair-lean-s33/tools/statement_identity_h4.py . PairChannel <the eight names>   # IDENTICAL ×8
python3 results/h4-pair-lean-s33/tools/trust_greps_h4.py . <the six topic files>                  # the 8 challenge sorrys only
```

Recorded runs (2026-09-29, `results/h4-pair-lean-s33/`): `rung1-print-axioms.log` (items 1–4 built alone first), `cert-build.log` (the
certificate module timed: 1.8 s), `build-comparator-topic.log` (`lake build Challenge.PairChannel Solution.PairChannel`: *8704 jobs*, the
8 deliberate `sorry` warnings of the challenge, 0 warnings from the solution); `print-axioms.log` (8 root names) and `program-axioms.log`
(34 program-side names); `statement-identity.log` (8 IDENTICAL, tree and mirror, and against the probe); `trust-greps.log`; the
Comparator run with nanoda `comparator-run.log` — `Nanoda kernel accepts the solution`, `Lean default kernel accepts the solution`,
`Your solution is okay!`, exit 0, 46.9 s (runner `tools/run.sh`; NOT sandboxed, the fake-landrun shim as in every prior macOS record).

**Honest label, verbatim (UNIT-BRIEF §1(3)): "IV.17's pair channel: Prop. 4.5 Comparator-checked for every depth and real mark, the
integer-mark safety chain a theorem, and the floor F1 ≥ S2's failure for a real-marked pair at (1/4, 1/20) kernel-checked by a dyadic
certificate — over Mathlib alone, no displayed hypothesis, the three standard axioms, replayed by nanoda".** What it means: the floor
F1 ≥ S2 cannot serve as the pair channel's closing inequality for real marks — at (1/4, 1/20) the floor fails, kernel-checked — while for
integer marks it holds, as a theorem; the interference identity behind both is a theorem for every depth and real mark. What it does NOT say
(FIDELITY.md §2): nothing about (MI) F1 ≥ 3M − 2N_d — at this anchor (MI) HOLDS (T = 60.3, F1 − T = +3.67, a Python fact, not a Lean
statement) and the theorem is the failure of the floor for a real mark, nothing more; nothing about Theorems 4.6–4.9 of the paper (the
pair channel's closure stays at paper grade); nothing about laws, the LP, pairs off the grid, or any budget other than the bandwidth-one
row; nothing about ζ or RH. The fidelity ledger — pairs on grid sites, the flat weights substituted into `W2`, every n including 0, the
mark types, the character's sign, the certificate as a strict inequality with Mathlib's d6 decimals for π, `W2`'s `_j` binder — is
`results/h4-pair-lean-s33/FIDELITY.md`, mirrored in `formalization.yaml` (`fidelity.divergences` row (z)).

## ResidueRank (Session 36, 2026-09-30): Theorem R's arithmetic core in Lean — the logarithms of the primes are ℚ-independent, Lemma F, and Theorem R on the abstract pair — `Zeta23/ResidueRank/LogPrimes.lean`, `Pair.lean`, `GenusBound.lean`, `comparator/{Challenge,Solution,PrintAxioms}/ResidueRank.lean`, `config-residue-rank.json`

**What the topic is (unit brief `results/theoremR-lean-s36/UNIT-BRIEF.md`, typing probe `typing-probe.lean` there, build record
`results/theoremR-lean-s36/BUILD-NOTES.md`, ledger `FIDELITY.md`, the attack on the brief's statements and sketches
`PREDERIVATION-ERRATA.md`).** The arithmetic core of Theorem R of `results/beta-shapes-s35/NOTE.md` (§2.0 Lemma F, §2.3 H3.3(b), Theorem R,
T3; the reader's converse, `read-O.md` §2.5) as ONE Comparator topic over Mathlib alone — there is no ChallengeDeps module, since every
constant the statements mention (`Nat.Primes`, `Real.log`, `Submodule.span ℚ`, `Module.Finite`, `Module.rank`, `LinearIndependent`,
`HasSum`, `IsPrimePow`, `ArithmeticFunction.vonMangoldt`, `Real.sqrt`) is Mathlib's. The pair is abstract: `cls : ℕ → ι` stands for
n ↦ c(Γ_n), `v : ι → ℝ` for the diagonal row, the weights are von Mangoldt's Λ (the SPEC's A5), and A9 is a `HasSum` over each fiber
{m ≥ 2 : cls m = cls n} with value κ · v(cls n) for ONE real κ.

| file | module | trusted? | content |
|---|---|---|---|
| `Zeta23/ResidueRank/LogPrimes.lean` | `Zeta23.ResidueRank.LogPrimes` | no (source of the proofs) | `expVec` (the exponent vector of n on the primes) and `linearCombination_expVec` (Σ_q v_q(n) log q = log n); `log_primes_linearIndependent` (over ℤ first by `LinearIndependent.iff_fractionRing ℤ ℚ`, then an integer relation makes Π p^{m_p} = 1 and the q-adic valuation gives m_q = 0 — Mathlib at the pin has no such lemma); `span_log_not_finite` (coordinates by `LinearIndependent.repr`; a prime outside the finite union of the generators' supports has coordinate v_q(N q) ≥ 1); `rank_span_log_le` (with `rank_span_log_le_of_supp`, which needs no positivity) |
| `Zeta23/ResidueRank/Pair.lean` | `Zeta23.ResidueRank.Pair` | no (source of the proofs) | `lemmaF_finite_fiber` (a prime power weighs ≥ log 2; a summable nonnegative family has finitely many terms ≥ log 2), `fiber_sum_eq_log` (κ·v(cls n) = log Π minFac over the fiber's prime powers), `lemmaF_infinite_order` (the injective family j ↦ p^{a+jk} in one fiber), `theoremR_of_A9` (Theorem R with no hypothesis on κ: the ℚ-linear map x ↦ κx and `span_log_not_finite`), `theoremR` (the displayed κ > 0, unused), and the errata's E2/E3 (`lemmaF_finite_fiber_all`, `lemmaF_infinite_order_all`) |
| `Zeta23/ResidueRank/GenusBound.lean` | `Zeta23.ResidueRank.GenusBound` | no (source of the proofs) | `theoremS_bound` (L ≤ (1 + 2g)(1 + (1 + √(1 + 8g))/2) from the two inequalities; `nlinarith` on the brief's derivation), `theoremS` (a prime above exp(κ · bound)), `theoremS_abs` (E5: no `0 ≤ g`) — SCOPED real algebra |
| `comparator/Challenge/ResidueRank.lean` | `Challenge.ResidueRank` | yes — read it | the eight statements with `sorry` (from `import Mathlib` to the end, the typing probe character for character), namespace `ResidueRank`, and the WHAT IS CLAIMED / NOT paragraph |
| `comparator/Solution/ResidueRank.lean` | `Solution.ResidueRank` | no | the eight statements byte-identical, each the program theorem of the same name applied to the same arguments |
| `config-residue-rank.json`, `PrintAxioms/ResidueRank.lean` | — | yes / — | comparator configuration (the 8 names `ResidueRank.*`; `propext`, `Quot.sound`, `Classical.choice`; `enable_nanoda: true`) and the quick check |

**Quick check (no extra tooling)** — the two `lake` lines from the Lean tree's root, the two `python3` lines from `rh-program/` (root `lean`):

```sh
lake build Solution.ResidueRank
lake env lean comparator/PrintAxioms/ResidueRank.lean      # eight lines, each [propext, Classical.choice, Quot.sound]
python3 results/theoremR-lean-s36/tools/statement_identity_s36.py ResidueRank lean/comparator/config-residue-rank.json \
  results/theoremR-lean-s36/typing-probe.lean lean -- <the eight names>               # IDENTICAL ×8, RESULT: PASS
python3 results/theoremR-lean-s36/tools/trust_greps_s36.py lean                       # the 8 challenge sorrys only
```

Recorded runs (2026-09-30, `results/theoremR-lean-s36/`): `rung1-build.log` and `rung1-print-axioms.log` (items 1–3 built alone first),
`program-build.log` (the three modules, one `lake` at a time: 3.2 s / 3.1 s / 7.3 s of Lean, 0 warnings), `program-axioms.log` (all 27
program-side names), `build-comparator-topic.log` (`lake build Challenge.ResidueRank Solution.ResidueRank`: 8701 jobs, the 8 deliberate
`sorry` warnings of the challenge, 0 from the solution), `print-axioms.log`, `statement-identity.log`, `trust-greps.log`, and the
Comparator run with nanoda `comparator-run.log` — `Nanoda kernel accepts the solution`, `Lean default kernel accepts the solution`,
`Your solution is okay!`, exit 0, 32.3 s (runner `tools/run.sh`; NOT sandboxed, the fake-landrun shim as in every prior macOS record).

**Honest label, verbatim (UNIT-BRIEF §1(3)): "Theorem R's arithmetic core Comparator-checked: the logarithms of the primes are ℚ-linearly
independent, a family of positive integers N_p with p | N_p has logarithms spanning an infinite-dimensional ℚ-space, the converse rank
bound, Lemma F, and Theorem R on the abstract pair (von Mangoldt weights, real fiber sums, one κ) — over Mathlib alone, no displayed
hypothesis, the three standard axioms, replayed by nanoda".** What it means: a target whose diagonal-row values are κ⁻¹ · log of integers
N_p with p | N_p cannot have a finite-dimensional ℚ-span, because the logarithms of the primes are ℚ-independent and there are infinitely
many primes — kernel-checked. What it does NOT say (FIDELITY.md §2): nothing about the SPEC's geometric clauses A6–A8 or A7's graph
structure; nothing about the existence or non-existence of a target Y; not the general-base Theorem R; not the geometric reading of the two
scoped real-algebra statements (items 7–8, whose reading belongs to the Session-36 unit `results/d4-infty-s36/`, under read); nothing about
ζ, its zeros, or RH (Theorem R is RH-blind). The displayed κ > 0 of `theoremR` is the SPEC's and is not used by the proof
(PREDERIVATION-ERRATA E1). The fidelity ledger is `results/theoremR-lean-s36/FIDELITY.md`, mirrored in `formalization.yaml`
(`fidelity.divergences` row (aa)).

## What these build against, and why it is not here

They extend **Zeta23**, the Lean 4 formalization released as the companion artifact to
*More than two thirds of the zeros of the Riemann zeta function lie on the critical line*
(arXiv:2608.13637).

> Zeta23 is **Copyright 2026 Anthropic, PBC**, released under the **Apache License 2.0**.
> Its canonical home is <https://github.com/anthropics/zeta-23-lean>.

That library was kept locally during the program **for reference**, and an earlier state of this
repository redistributed a copy of it. It has been removed: it is Anthropic's work, it is already
published at the address above, and there is no reason for a second copy to live here. Apache 2.0
permits redistribution — nothing improper was done — but a dependency is better cited than copied.

## Building

**[Recipe replaced 2026-09-10 (Session 20) after the independent checker's FIX-FIRST 1 (`results/d1-m2a/packaging/CHECK-O.md` §8): the old recipe cloned upstream HEAD, which moved the library into a `zeta23/` subdirectory on 2026-08-27, never copied `comparator/`, and this mirror lacked the root `Zeta23.lean`.]** These files overlay the parent library at its tag **v1.0** (commit `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`); the working tree differs from that commit only by the program additions mirrored here and by fifteen `import` lines added to the root `Zeta23.lean` (now mirrored as `lean/Zeta23.lean`). The scratch probes `Zeta23/W1/AuditO*.lean` of the working tree are deliberately not mirrored (nothing imports them).

```sh
git clone https://github.com/anthropics/zeta-23-lean
cd zeta-23-lean
git checkout v1.0        # 3635e74826a4c1fcece7d1cd2b6fa75e43a00510 — the base these files overlay;
                         # main has since moved the library into a zeta23/ subdirectory
cp -R /path/to/this/repo/rh-program/lean/Zeta23/. Zeta23/
cp -R /path/to/this/repo/rh-program/lean/comparator/. comparator/
cp    /path/to/this/repo/rh-program/lean/Zeta23.lean Zeta23.lean
lake exe cache get && lake build Zeta23 && lake build Solution.DBN
```

Toolchain, as pinned by upstream and used for every recorded build: Lean `v4.33.0-rc2`, Mathlib
commit `51e6992efd06126df61a496bebf8f49482a4e129`. Measured on a cold clean clone by the independent
checker (2026-09-10, `CHECK-O.md` §1): `lake build Zeta23` — *Build completed successfully (9142 jobs)*, 397 s,
0 errors, no warnings from any program module; `lake build Solution.DBN` — 8826 jobs, 54 s;
`lake build Challenge.DBN` — 8699 jobs with exactly the seven deliberate `sorry` warnings. (The earlier
"2081 jobs" figure was the A4-era partial build.) The A4 formalization record — the environment, the
theorem-by-theorem map to the A4 paper's numbering, the `#print axioms` output — is
`rh-program/results/a4-no-go/formalization-status.md`.

## Licensing (settled 2026-08-27)

These thirteen files (fourteen with `DBN/BtFacts.lean`, added 2026-09-06 under this header from the start) (fifteen with `DBN/Asym.lean`, added 2026-09-09 under this header from the start; the emitted `DBN/Instance02/Asym_{mp,arb}.lean` carry it too) are **Copyright 2026 Kunal Tyagi**, released under the **Apache License 2.0**
(see the repository's [`LICENSE`](../../LICENSE) and [`NOTICE`](../../NOTICE)).
(`W1/Instances.lean`, added 2026-09-02, was written under this header from the start; so were the
three argument-principle files of the same day and `DBN/BarrierCert.lean`, which carry in addition the MIT notice for the
portions ported from the Gomila/Aristotle development — see the v1.1 section above and the dated
sections of [`NOTICE`](../../NOTICE). The relicensing record below concerns the original eight.)

They previously carried `Copyright (c) 2026 Anthropic, PBC` — copied from the surrounding library's
header convention when they were written inside it, and pointing at a `LICENSE` file that is no
longer in this repository. That attribution was wrong: these are this program's own work, not part
of Anthropic's Zeta23 release. Each header now says so explicitly, and records that the file
contains no code from Zeta23 but imports it. Apache-2.0 is kept rather than swapped for something
else, so that there is no compatibility question with the library these files extend or with
mathlib, both of which are Apache-2.0.

Verified before relicensing: none of the eight carries an upstream-derivation notice, and none
sits under `Zeta23/FromPNTPlus/`, which is where Zeta23's own NOTICE records its derived files.
They are original.
