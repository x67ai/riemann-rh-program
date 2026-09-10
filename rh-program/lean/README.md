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
