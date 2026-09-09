# The glue `lambda_le_point2` (Session 16, 2026-09-06; RUN-REPORT §6 item 4, SPEC §8.3)

STATUS: IN PROGRESS.

## Inputs and their status at the time of writing

| hypothesis | status | where |
|---|---|---|
| H1 `ZeroVerification (116733/200000) 2500000097429` | DISPLAYED (named argument `hH1`) | SPEC §3.6, exact |
| H2-B `BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierMP` (and `…ARB`) | DISPLAYED (`hEncl`) | the Lane B legs, kernel-checked transcripts |
| H2-A, the final-time asymptotic nonvanishing (ii′) | DISPLAYED IN CONCLUSION FORM (`hLaneA`) — the Lane A checker/producers are a separate compute stream not yet run | SPEC §5, §8.3 |
| **[2026-09-09, Session 19]** H2-A and H-TAIL (the same row, updated; the row above is the 2026-09-06 state, kept) | DISPLAYED as `hAsym : AsymEnclOK (Ht t₀/Bt t₀) row2Asym*` (the window rows) and `hTail : TailOK (Ht t₀/Bt t₀) row2Asym*` (the tail) behind the kernel-checked `checkAsym` on the Lane A literals (`Instance02/Asym_{mp,arb}.lean`); `hLaneA` REPLACED per PLAN §1.5 (`lane-a/instance02-replacement.diff`) | SPEC §5, §8.1, §8.3; `lane-a/EMIT-NOTES.md` |
| H3 `Polymath15Bridge' ∧ HtEntire` | DISPLAYED (`hH3`) | Defs.lean v1.1 |
| L-B3 (`Bt` holomorphic, nonvanishing near R) | PROVED (BtFacts.lean) — no `hBt` | LB3-NOTES.md |
| `hHol` of the `_xy` legs | PROVED from `hH3.2` and L-B3 (`hHol_of_entire`) | Instance02.lean |
| the checker facts (`_chain`, `_prisms`) | kernel-checked (`decide +kernel`, Session 14) | Instance02/*.lean |
| L-G arithmetic (t₀ + y₀²/2 ≤ 1/5; H1 parameter identities) | `norm_num` | Instance02.lean |

Instance parameters, checked against SPEC §9: X = 5 000 000 194 858 (so X + 1 = 5 000 000 194 859 = rect.x2),
y₀ = 16733/100000, t₀ = 93/500 (= 186/1000; the data literal `row2T0n/row2T0d` is 93/500),
(1 + y₀)/2 = 116733/200000, X/2 = 2 500 000 097 429, 1 − 2t₀ = 157/250, t₀ + y₀²/2 = 3999993289/20000000000 ≤ 1/5.

## Result: PROVED (first build, 2026-09-06) — `lambda_le_point2` and `lambda_le_point2_arb`

File: `~/rh-lean-work/zeta-23-lean-main/Zeta23/DBN/Instance02.lean` §2 (new; §1 = the Session 14 legs, unchanged;
one new import `Zeta23.DBN.BtFacts`).  New declarations: `row2Rect_x1/x2/y1/y2`, `row2BarrierMP_t0`,
`row2BarrierARB_t0` (the rectangle's reals are the instance parameters, `norm_num`), `hHol_of_entire`
(hHol discharged from `HtEntire` + L-B3), `hH1_row2` (H1 exact-form ↔ parameter-form, `norm_num`),
`row2_bound_le_point2` (L-G: t₀ + y₀²/2 ≤ 1/5, `norm_num`), `row2_ray_mp`, `row2_ray_arb` (the bridge at row 2,
conclusion at t₀ + y₀²/2), `lambda_le_point2` (mp leg), `lambda_le_point2_arb` (Arb leg).  The two legs are two
theorems; nothing merged.

### The full theorem statement (source, verbatim)

    theorem lambda_le_point2
        (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
        (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierMP)
        (hLaneA : ∀ x y : ℝ, 5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y →
          y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (x + y * I) ≠ 0)
        (hH3 : Polymath15Bridge' ∧ HtEntire) :
        ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0

`lambda_le_point2_arb`: identical with `row2BarrierARB` in `hEncl`.  Proof: `hiii` := `row2_barrier_mp_xy Ht Bt
(hHol_of_entire row2BarrierMP rfl hH3.2) hEncl` (the kernel-checked Lane B leg as (iii′), after rewriting the
rectangle's reals to the literals); `hH3.1 (93/500) 5000000194858 (16733/100000)` with the four side conditions by
`norm_num`, `hH1_row2 hH1`, `hLaneA` as (ii′), `hiii` as (iii′); then `le_trans row2_bound_le_point2 ht`.

### `#check` (elaborated, verbatim) and `#print axioms` (verbatim; scratch `glue-axioms.lean` via `lake env lean`)

    'Zeta23.DBN.Instance02.lambda_le_point2' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.lambda_le_point2_arb' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.row2_ray_mp' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.row2_ray_arb' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Instance02.hHol_of_entire' depends on axioms: [propext, Classical.choice, Quot.sound]
    Zeta23.DBN.Instance02.lambda_le_point2 : Zeta23.DBN.ZeroVerification (116733 / 200000) 2500000097429 →
      Zeta23.DBN.BarrierEnclOK (fun t z => Zeta23.DBN.Ht t z / Zeta23.DBN.Bt t z) Zeta23.DBN.Instance02.row2BarrierMP →
        (∀ (x y : ℝ),
            5000000194858 + 1 ≤ x →
              16733 / 100000 ≤ y → y ^ 2 ≤ 1 - 2 * (93 / 500) → Zeta23.DBN.Ht (93 / 500) (↑x + ↑y * Complex.I) ≠ 0) →
          Zeta23.DBN.Polymath15Bridge' ∧ Zeta23.DBN.HtEntire →
            ∀ (t : ℝ), 1 / 5 ≤ t → ∀ (z : ℂ), Zeta23.DBN.Ht t z = 0 → z.im = 0
    Zeta23.DBN.Instance02.lambda_le_point2_arb : Zeta23.DBN.ZeroVerification (116733 / 200000) 2500000097429 →
      Zeta23.DBN.BarrierEnclOK (fun t z => Zeta23.DBN.Ht t z / Zeta23.DBN.Bt t z) Zeta23.DBN.Instance02.row2BarrierARB →
        (∀ (x y : ℝ),
            5000000194858 + 1 ≤ x →
              16733 / 100000 ≤ y → y ^ 2 ≤ 1 - 2 * (93 / 500) → Zeta23.DBN.Ht (93 / 500) (↑x + ↑y * Complex.I) ≠ 0) →
          Zeta23.DBN.Polymath15Bridge' ∧ Zeta23.DBN.HtEntire →
            ∀ (t : ℝ), 1 / 5 ≤ t → ∀ (z : ℂ), Zeta23.DBN.Ht t z = 0 → z.im = 0
    Zeta23.DBN.Instance02.row2_ray_mp : Zeta23.DBN.ZeroVerification (116733 / 200000) 2500000097429 →
      Zeta23.DBN.BarrierEnclOK (fun t z => Zeta23.DBN.Ht t z / Zeta23.DBN.Bt t z) Zeta23.DBN.Instance02.row2BarrierMP →
        (∀ (x y : ℝ),
            5000000194858 + 1 ≤ x →
              16733 / 100000 ≤ y → y ^ 2 ≤ 1 - 2 * (93 / 500) → Zeta23.DBN.Ht (93 / 500) (↑x + ↑y * Complex.I) ≠ 0) →
          Zeta23.DBN.Polymath15Bridge' ∧ Zeta23.DBN.HtEntire →
            ∀ (t : ℝ), 93 / 500 + (16733 / 100000) ^ 2 / 2 ≤ t → ∀ (z : ℂ), Zeta23.DBN.Ht t z = 0 → z.im = 0

Expected [propext, Classical.choice, Quot.sound] — obtained exactly that for all five, nothing else.  No STOP condition.

### Build log (`lake build Zeta23.DBN.Instance02`, verbatim tail)

    ✔ [3263/3263] Built Zeta23.DBN.Instance02 (1.5s)
    Build completed successfully (3263 jobs).
    lake build Zeta23.DBN.Instance02  1.99s user 2.03s system 143% cpu 2.805 total

`sorry` / `native_decide` / `axiom` sweep over Defs.lean, BtFacts.lean, Instance02.lean, BarrierCert.lean,
Instance02/Rect.lean, Instance02/mp_Barrier.lean, Instance02/arb_Barrier.lean: zero hits outside docstrings.

### THE HONEST LABEL (SPEC §3.7 form, amended for what is actually displayed today)

> `lambda_le_point2` — every H_t with t ≥ 1/5 has only real zeros (Λ ≤ 0.2 in ray form) — is kernel-checked
> modulo the displayed hypotheses: (H1) a producer-certified zero verification —
> `ZeroVerification (116733/200000) 2500000097429`, discharged by Platt–Trudgian Theorem 1; (H2-B)
> producer-certified barrier enclosures — `BarrierEnclOK (Ht/Bt) row2BarrierMP` (or `row2BarrierARB`), the
> prism transcripts themselves kernel-checked, from two independent producers, one leg per theorem; (H2-A) the
> final-time asymptotic nonvanishing (ii′) — DISPLAYED IN CONCLUSION FORM as `hLaneA`, because the Lane A
> producers and the `checkAsym` checker are a separate compute stream not yet run (so this is stronger than the
> SPEC §3.7 form, which displays only H2-A's window rows and H-TAIL behind a kernel-checked checker); (H3) the
> Polymath15 analytic package — Theorem 1.2 in the form `Polymath15Bridge'` and the entirety of H_t — as
> hypotheses.  L-B3 (the normalizer B_t holomorphic and nonvanishing near R) and `hHol` are PROVED, not displayed;
> `#print axioms` = propext, Classical.choice, Quot.sound.

Never "fully machine-checked".  The shorter sentence RUN-REPORT §6 item 4 speaks of ("Λ ≤ 0.2 in ray form,
kernel-checked modulo H1, H2, H3") is NOT licensed today, with or without a gloss: item 4's "only then" is gated
on item 3 (Lane A) as well, and "H2" is SPEC §6's conjunction H2-B ∧ H2-A ∧ H-TAIL behind a kernel-checked
checker, of which only H2-B exists in the Lean tree.  The licensed wording is the four-hypothesis label above,
with H2-A named as displayed in conclusion form.  (Auditor's ruling, v11/AUDIT.md §3, 2026-09-06.)

**[DATED NOTE 2026-09-09, Session 19 — the label above and the R-1 ruling's condition are superseded; both kept as the
record.]** Lane A landed: `hLaneA` is replaced in all four theorems by the pair `hAsym` (H2-A, the window-row floors
`AsymEnclOK (fun z => Ht (93/500) z / Bt (93/500) z) row2Asym*`) and `hTail` (H-TAIL, `TailOK … row2Asym*`), one Lane A
literal per leg, with (ii′) supplied by `row2_laneA_* hAsym hTail` — `cert_of_checkAsym` on the kernel fact
`row2Asym*_check` (`decide +kernel`) plus L-A1/L-A2 (`Zeta23/DBN/Asym.lean`).  The displayed hypotheses are now exactly
SPEC §3.7's five named Props (H1, H2-B, H2-A, H-TAIL, H3); `#print axioms` unchanged, `[propext, Classical.choice,
Quot.sound]` for `lambda_le_point2`, `lambda_le_point2_arb`, `row2_ray_mp`, `row2_ray_arb`, `row2_laneA_mp`,
`row2_laneA_arb`, and `[propext]` for `row2AsymMP_check`, `row2AsymARB_check` (`lane-a/final-axioms.log`).

> THE HONEST LABEL, now SPEC §3.7's as written: `lambda_le_point2` — every H_t with t ≥ 1/5 has only real zeros
> (Λ ≤ 0.2 in ray form) — is **kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3**: (H1) a producer-certified zero
> verification — `ZeroVerification (116733/200000) 2500000097429`, discharged by Platt–Trudgian Theorem 1; (H2)
> producer-certified enclosures — the barrier prisms (H2-B, `hEncl`), the final-time window rows (H2-A, `hAsym`) and
> the tail (H-TAIL, `hTail`), from two independent producers, one leg per theorem, the transcripts themselves
> kernel-checked (`checkBarrier`, `checkAsym`); (H3) the Polymath15 analytic package — Theorem 1.2 in the form
> `Polymath15Bridge'` and the entirety of H_t — as hypotheses.  L-B3, `hHol`, `cert_of_checkBarrier` and
> `cert_of_checkAsym` are PROVED, not displayed.

Never "fully machine-checked".  The shorter sentence RUN-REPORT §6 item 4 speaks of ("Λ ≤ 0.2 in ray form,
kernel-checked modulo H1, H2, H3") is now LICENSED — with SPEC §3.7's gloss that H2 is the conjunction
H2-B ∧ H2-A ∧ H-TAIL of producer-certified enclosure-type Props behind kernel-checked checkers, and "three displayed
hypotheses" only with that gloss: R-1's condition (item 3 landing) is met, so R-1 is discharged, not reversed.  Stated,
not glossed (PLAN-REVIEW §6): the window range N ∈ [630 783, 5 140 999] (x from 5.0·10¹² to ≈ 3.32·10¹⁴) is no longer a
displayed nonvanishing claim but a displayed floor enclosure plus the kernel-checked coverage argument; the displayed
nonvanishing conclusion that remains is `TailOK` on N(x) ≥ 5 141 000 with the y-band [y₀, yA], yA = 0.7924646 being
9.0·10⁻⁸ wider than `hLaneA`'s √(157/250) = 0.79246451… (yA − √(157/250) = 8.975·10⁻⁸; in the squares yA² − 157/250 =
1.42·10⁻⁷; the glue derives y ≤ yA from y² ≤ 157/250), so `TailOK` is "the
tail region N ≥ N₁, y ∈ [y₀, yA]", not "part of what `hLaneA` said"; and C-A6 (the tail row's Σ < 2K) is kernel-checked
but NOT consumed by `cert_of_checkAsym` — recorded evidence for Lemma T's prose discharge, never "the tail reduction is
kernel-checked".  [Figure corrected 2026-09-09 22:25 IST after the phase-3(d) audit (AUDIT-3d.md A-1): the earlier "1.5·10⁻⁷" was the gap in the squares.]

### Left for the Lane A stream (RUN-REPORT §6 item 3)

Producers P-9/P-10 (window floor T uniform in N and y ∈ [y₀, yA], the Theorem 1.3 defect E, Lemma T's Q₁…Q₄, E₁),
`checkAsym` + `cert_of_checkAsym` + L-A1/L-A2 in Lean, the transcript kernel-checked and cross-checked per row.
When it lands: replace `hLaneA` in `lambda_le_point2` by `cert_of_checkAsym` on the Lane A literal (with
`AsymEnclOK`/`TailOK` displayed), and re-run `#print axioms`.  Nothing in the present glue needs to change shape:
(ii′) is consumed exactly where `hLaneA` is passed.

**STATUS: DONE (2026-09-09, Session 19).** Producers P-9/P-10 run on both legs (`lane-a/asym-{mp,arb}.json`, 3 window rows
+ the tail row, cross-checked CONSISTENT in `lane-a/crosscheck-full.txt`); `checkAsym`, `cert_of_checkAsym`, L-A1/L-A2
in `Zeta23/DBN/Asym.lean` (PROVED, `lane-a/BUILD-NOTES.md`); the two literals emitted (`lane-a/emit_lean_lane_a.py`),
back-parse-verified (`lane-a/backparse.log`, 0 mismatches) and kernel-checked (`decide +kernel`, 2–4 ms each);
`hLaneA` replaced exactly as PLAN §1.5 foresaw and as this section said — at the one consumption point per leg, with
`AsymEnclOK`/`TailOK` displayed — and `#print axioms` re-run (`lane-a/final-axioms.log`, unchanged).  Nothing in the
glue changed shape.  Record: `lane-a/EMIT-NOTES.md`; audit: `lane-a/AUDIT-3d.md`.

STATUS: DONE (STEP 3).

### Whole-library check: `lake build Zeta23` (root module imports DBN.Defs, DBN.BarrierCert, DBN.Instance02)

    Build completed successfully (9139 jobs).
    lake build Zeta23  4.22s user 6.73s system 42% cpu 25.842 total

The replayed warnings in that log are pre-existing deprecation notices in Zeta23's own upstream files (Statement, ZetaReflect, Assembly, Tail, ZeroSide, GammaFacts/Mu); none is in a DBN file.
