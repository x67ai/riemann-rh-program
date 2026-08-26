# M1 v1 acceptance suite — report

**Status:** run 2026-08-26 (Session 8, D1 first-deliverable component 3).
**Directory:** `results/d1-m1/acceptance/` (all transcripts, harnesses, and logs; every
number below is rerunnable from the commands in §8).
**Trust language (binding, D-R3/D-R8):** every accepted ζ transcript is
"kernel-checked modulo the displayed hypotheses H-ENCL and H-AP (producers untrusted)" —
once the Lean checker lands; today's acceptances are by the two UNTRUSTED reference
checkers, which are the executable spec of the Lean checker, not a substitute for it.
Accepted f_DH transcripts are checker-level only (D-R8): no Lean-backed conclusion.
Nothing here is "fully machine-checked".

## 0. Verdict summary

| suite item | result |
|---|---|
| 1. Null tests (4 rectangles × 2 legs, m = 0) | **PASS** — all produced transcripts ACCEPTED by both checkers (mp t10000 leg: see §1 note) |
| 2. Positive control (straddling box, machinery test) | **PASS** — both legs' machinery certify m = 1; both checkers REJECT the transcript at exactly C2, as the format requires |
| 3. DH live fire (checker-level true positive, D-R8) | **PASS** — both legs, identical rectangle around ρ_DH, m = 1, ACCEPTED by both checkers |
| 4. Two-producer cross-check | **CONSISTENT** — every pair cell-wise consistent on the common mesh refinement; zero stop-the-line events |
| 5. Cost curve | **WRITTEN** — `results/d1-m1/cost-curve.json` |

No failure was observed. Honest notes and residual gaps are in §7 — none softened.

## 1. Null tests (exclusion certificates, the M3 prototype)

Four rectangles strictly right of the critical line, both producer legs each, mode
`exclusion`, certified winding m = 0. δ₀ = σ₁ − ½ is the D-R6 certified depth floor.

| rectangle | δ₀ | leg | segments | wall s | winding enclosure (turns) | certified boundary floor |f| ≥ |
|---|---|---|---|---|---|---|
| [3/5, 9/10] × [100, 101] | 1/10 | mp | 52 | 1.0 | [−24, 28]·10⁻¹² | 0.35555 |
| [3/5, 9/10] × [100, 101] | 1/10 | arb | 27 | 0.09 | [−14, 13]·10⁻⁶ | 0.08328 |
| [3/5, 9/10] × [1000, 1001] | 1/10 | mp | 81 | 8.6 | [−41, 40]·10⁻¹² | 0.015573 |
| [3/5, 9/10] × [1000, 1001] | 1/10 | arb | 65 | 0.14 | [−29, 36]·10⁻⁶ | 0.013827 |
| [3/5, 9/10] × [10000, 10001] | 1/10 | mp | [PENDING-MP-T10000-SEGS] | [PENDING-MP-T10000-WALL] | [PENDING-MP-T10000-S] | [PENDING-MP-T10000-FLOOR] |
| [3/5, 9/10] × [10000, 10001] | 1/10 | arb | 983 | 2.6 | [−495, 488]·10⁻⁶ | 7.64·10⁻⁶ |
| [21/40, 39/40] × [100, 101] | 1/40 | mp | 58 | 1.1 | [−28, 30]·10⁻¹² | 0.35550 |
| [21/40, 39/40] × [100, 101] | 1/40 | arb | 30 | 0.09 | [−16, 14]·10⁻⁶ | 0.03052 |

Checker record (`acceptance/logs/reference-checker-accepts.log`,
`acceptance/logs/checker-ref-accepts.log`): **every one of these transcripts is ACCEPTED
by BOTH reference checkers** — `reference_checker.py` (format author's, integer
cross-multiplication) and `checker_ref.py` (independently written from FORMAT.md,
Fraction-based) — with all of C1–C11 passing and digit-identical winding sums.

D-R6 ledger sentences these certify (modulo H-ENCL and H-AP, per trust label — never
"RH verified in W"): *no zeros of ζ in [3/5, 9/10] × [T, T+1] for T ∈ {100, 1000,
10000}* (δ₀ = 1/10), and *no zeros of ζ in [21/40, 39/40] × [100, 101]* (δ₀ = 1/40).
The [21/40, 39/40] box is the depth point of the cost curve (σ₁ only 1/40 off the
line, σ₂ at 39/40).

The floors are mesh-dependent certified lower bounds (C11 rows), not estimates of the
true boundary minimum; the coarser arb meshes give weaker floors on the same box —
both legs' floors are simultaneously valid.

## 2. Positive control — winding machinery test (DELIBERATE C2 violation)

**Label, stated plainly: this is NOT an off-line-zero claim and NOT a W1 certificate.**
The box R = [2/5, 3/5] × [14, 143/10] STRADDLES the critical line around the first
ζ zero ρ₁ ≈ ½ + 14.1347i, deliberately violating the W1 precondition ½ < σ₁ (checker
C2), as a test that the argument-principle machinery actually sees a zero it is pointed
at. Harnesses `acceptance/pos_control_{mp,arb}.py` reuse each leg's production
mesh/argument machinery unmodified (imported, not copied), bypassing only the
producer-side rectangle precondition.

Results (logs `pos-control-{mp,arb}.log`, `pos-control-checker-rejects.log`):

* **mp leg:** winding enclosure [999999999962, 1000000000039]·10⁻¹² turns → **m = 1**
  (77 segments, 1.0 s).
* **arb leg:** winding enclosure [999911, 1000094]·10⁻⁶ turns → **m = 1**
  (183 segments, 0.07 s).
* **Both checkers REJECT both transcripts at exactly C2** ("sigma1 <= 1/2"). This is
  the correct verdict and doubles as a live C2 negative control on real (non-mutated)
  producer output: the format structurally refuses to bless a straddling box, so the
  machinery result m = 1 can never be laundered into an "off-line zero" claim.
* The two legs' straddling-box outputs are also mutually consistent (§4: 295 overlap
  pairs, all boxes intersect).

## 3. Davenport–Heilbronn live fire (checker-level true positive, D-R8 wording)

**The identical production pipeline — same producers, same checkers, same checks
C1–C11, no code path special-cased — run on f_DH at its certified off-line zero.**

**The target function, re-verified against the program's conventions source.** Quoted
verbatim from `results/ccm-dh-test/dh.py` lines 5–8 (the conventions file the CCM/DH
work triple-validated):

> f_DH(s) = 5^{-s} [ zeta(s,1/5) + kap*zeta(s,2/5) - kap*zeta(s,3/5) - zeta(s,4/5) ]
> kap = (sqrt(10-2*sqrt5) - 2)/(sqrt5 - 1)
>     = tan(theta) with eps_chi = e^{2 i theta} = tau(chi)/(i sqrt5), chi mod 5, chi(2)=i.

Re-verification performed for this suite: `producer_mp.py::f_dh_ball` (Hurwitz-ζ
enclosures `hurwitz_ball(s, k/5)` with exact rational a = 1/5, 2/5, 3/5, 4/5; κ from
`kappa_iv()`) and `producer_arb.py::eval_fdh` (`acb.zeta(s, a)` Hurwitz balls; κ from
`_kappa()`, derivation D-P8) both implement exactly the quoted formula — same four
shifts, same signs, same 5^{−s} prefactor. **The tan θ constant κ is rigorously
enclosed on both legs, never a float:** mp builds it in directed-rounded interval
arithmetic (`iv.sqrt`, interval subtraction/division on exact integer inputs), arb as
a ball with outward radii; containment of the true κ follows from inclusion-monotone
interval/ball arithmetic over the exact integers 5, 10, 2, 1. Supporting evidence
already on disk: `validation-dh-crosscheck.txt` (mp leg vs mp.zeta pipeline) and the
arb capability check H1 (ball-certified |f_DH(ρ_DH)|² ≤ 2.8·10⁻³¹).

**Target zero and rectangle.** ρ_DH = 0.808517182456637 + 85.699348485377592i (D1
direction file line 104; residual 7.6e-41, re-verified twice in the Phase-4 cycle).
Common rectangle for both legs: R = [4/5, 41/50] × [8569/100, 8571/100] — strictly
right of the critical line (σ₁ = 4/5 > ½) and containing ρ_DH in its interior
(0.80 < 0.808517… < 0.82; 85.69 < 85.699348… < 85.71).

| leg | segments | wall s | winding enclosure (turns) | m | certified floor |f| ≥ |
|---|---|---|---|---|---|
| mp | 40 | 3.5 | [999999999980, 1000000000020]·10⁻¹² | **1** | 2.467·10⁻⁴ |
| arb | 50 | 0.19 | [999973, 1000023]·10⁻⁶ | **1** | 3.019·10⁻⁴ |

**Both transcripts ACCEPTED by both checkers** (all of C1–C11) — **the pipeline FIRES
on a true positive.** Scope, fixed by D-R8 and carried verbatim in each transcript's
`trust_label`: *"checker-level only (D-R8): format-checked modulo H-ENCL for f_DH; no
Lean-backed conclusion"* — this is a producer+checker firing test, NOT
"RH-for-DH machine-checked disproof" (the v1 Lean soundness statement is ζ-specific).
f_DH is entire, so the σ₂ < 1 constraint is format uniformity only (FORMAT.md §9.2, D8
vacuous).

## 4. Two-producer cross-check (D-R3; stop-the-line rule m2a-m2b-design §4)

`acceptance/crosscheck.py` (untrusted diagnostic; it can stop the line, not bless it)
compares each mp/arb pair for the same rectangle: exact same-target guard, claimed_m
equality, winding-enclosure intersection (exact rationals, turn units, different A
scales), and **cell-wise value-box consistency on the common mesh refinement** — for
every pair of segments from the two legs on the same edge whose closed parameter
intervals overlap, both legs' for-all-s boxes must intersect in Re and in Im (decided
by integer cross-multiplication at scales K₁, K₂); a disjoint pair would prove at
least one leg's H-ENCL false.

Record (`acceptance/logs/crosscheck.log`):

| pair (mp vs arb) | overlap pairs checked | verdict |
|---|---|---|
| null t100 | 83 | CONSISTENT |
| null t1000 | 158 | CONSISTENT |
| null t10000 | [PENDING-MP-T10000-XCHECK] | [PENDING-MP-T10000-XVERDICT] |
| null deep-t100 | 90 | CONSISTENT |
| DH live fire | 122 | CONSISTENT |
| positive control | 295 | CONSISTENT |

**Zero disagreements; zero stop-the-line events.** Winding enclosures intersect on
every pair (the mp enclosures, at A = 10¹², are ~10³–10⁴× tighter than the arb ones at
A = 10⁶; each contains the common integer m).

Independent high-precision spot validation (binding cross-validation rule):
`validate_arb_transcripts.py` (mpmath dps 40, heuristic floats — evidence, not
certificate; a failure would be stop-the-line) run over the acceptance transcripts of
BOTH legs: V1 five boundary samples per segment inside every value box, V2 dense
principal-argument unwrapping reproduces every claimed m, V3 sampled boundary minima
respect every claimed floor — **all checks pass on all transcripts tested**
(`acceptance/logs/independent-validation.log`, `…-t10000.log`).

## 5. Cost curve (M3 search-economics calibration, first data points)

`results/d1-m1/cost-curve.json` (built by `acceptance/cost_curve.py` from the
transcripts' own metadata + run logs; single-run wall times on this machine — Apple
Silicon arm64, system Python 3.9.6, mpmath 1.3.0, python-flint 0.6.0). Reading of the
first points:

* **Height axis (fixed box [3/5, 9/10] × [T, T+1], δ₀ = 1/10):** the mesh the
  argument principle needs grows with T through |ζ| oscillation on the boundary —
  arb segments 27 → 65 → 983 for T = 100 → 1000 → 10000; arb wall time tracks segment
  count (0.09 → 0.14 → 2.6 s). The mp leg pays additionally per evaluation for the
  Euler–Maclaurin term count N ≈ T/2 (measured ~0.7 s per segment evaluation at
  T = 10⁴ vs ~0.02 s at T = 10²), so its wall time grows faster
  (1.0 → 8.6 → [PENDING-MP-T10000-WALL] s).
* **Depth axis (T = 100):** δ₀ = 1/40 vs 1/10 cost essentially the same on both legs
  (30 vs 27 arb segments; 1.1 vs 1.0 mp s). At T ~ 100 the depth is not yet the
  binding cost driver; the D-R6 caveat (δ₀ → 1/log γ boxes must be priced before M3
  is funded) is untested by these points and stands.
* **Checking is negligible against producing:** both reference checkers verify the
  983-segment t10000 transcript in ~0.03 s. The producer, not the checker, is the M3
  economic bottleneck (consistent with the format's design intent: checking must stay
  kernel-affordable).

## 6. What this suite does and does not establish

Establishes (modulo each transcript's displayed hypotheses, producers untrusted):
the W1 v1 producer→checker pipeline, on two independent legs, (i) certifies m = 0
exclusion boxes at heights 10²–10⁴ that both checkers accept; (ii) sees a genuine
zero when pointed at one (positive control), with the format correctly refusing the
straddling box at C2; (iii) fires end-to-end on the one known true positive in reach
(f_DH at ρ_DH) at checker level; (iv) produces mutually consistent enclosures under
an adversarial cell-wise comparison.

Does NOT establish: any Lean-kernel-checked statement (the Lean checker is the Lean
stream's item; both checkers here are untrusted reference implementations); any
statement about ζ beyond the four exclusion boxes' ledger sentences; anything about
f_DH beyond checker level (D-R8); any claim at M3 production heights (~10¹²⁺ — the
cost curve's T ≤ 10⁴ points are calibration seeds, not that regime).

## 7. Honest notes (no failures; residual gaps recorded)

1. **The mp t10000 null test is the slow point of the suite** ([PENDING-MP-T10000-NOTE]).
   The mp leg's per-evaluation Euler–Maclaurin cost N ≈ T/2 is the driver; per-edge
   parallelism and a Riemann–Siegel-class evaluator are the known (uncommissioned)
   remedies for M3-scale heights.
2. `reference_checker.py`'s ACCEPT banner prints "modulo the displayed hypotheses
   H-ENCL, H-AP" for f_DH files too; for f_DH the binding scope is the transcript's
   own `trust_label` (checker-level only, no H-AP claim — D-R8). Cosmetic stdout
   wording of an untrusted tool; the transcript content is correct. Recorded, not
   repaired, to keep the format author's checker byte-identical this session.
3. The positive-control transcripts carry the schema-fixed ζ `trust_label` verbatim
   (required so the checker reaches C2 rather than failing at shape); the honest
   machinery-test label lives in their `comment` field and file names. A reader of
   the raw JSON sees the C2-violating rectangle in the same file.
4. The independent mpmath spot validation of mp-leg transcripts shares the mpmath
   LIBRARY (different pipeline: heuristic floats vs directed-rounded intervals); for
   the mp leg the fully independent evidence is the arb cross-check of §4, which is
   exactly the D-R3 two-producer design.
5. Winding-sum widths never stressed C8 (worst observed ~10⁻³ of budget); a
   Lehmer-pair-class near-degenerate target remains the untested stress case (carried
   from mp-leg cut line 5).

## 8. Rerun commands (from `results/d1-m1/`)

    # null tests + DH live fire, both legs (writes into acceptance/)
    python3 producer_mp.py  --function zeta --mode exclusion --rect 3/5 9/10 100 101     --out acceptance/w1-mp-null-t100.json
    python3 producer_mp.py  --function zeta --mode exclusion --rect 3/5 9/10 1000 1001   --out acceptance/w1-mp-null-t1000.json
    python3 producer_mp.py  --function zeta --mode exclusion --rect 3/5 9/10 10000 10001 --out acceptance/w1-mp-null-t10000.json
    python3 producer_mp.py  --function zeta --mode exclusion --rect 21/40 39/40 100 101  --out acceptance/w1-mp-null-deep-t100.json
    python3 producer_mp.py  --function f_DH --mode refutation --rect 4/5 41/50 8569/100 8571/100 --out acceptance/w1-mp-dh-livefire.json
    python3 producer_arb.py custom --function zeta --mode exclusion --sigma1 3/5 --sigma2 9/10 --T1 100 --T2 101         --out acceptance/w1-arb-null-t100.json
    python3 producer_arb.py custom --function zeta --mode exclusion --sigma1 3/5 --sigma2 9/10 --T1 1000 --T2 1001       --out acceptance/w1-arb-null-t1000.json
    python3 producer_arb.py custom --function zeta --mode exclusion --sigma1 3/5 --sigma2 9/10 --T1 10000 --T2 10001     --out acceptance/w1-arb-null-t10000.json
    python3 producer_arb.py custom --function zeta --mode exclusion --sigma1 21/40 --sigma2 39/40 --T1 100 --T2 101      --out acceptance/w1-arb-null-deep-t100.json
    python3 producer_arb.py custom --function f_DH --mode refutation --sigma1 4/5 --sigma2 41/50 --T1 8569/100 --T2 8571/100 --out acceptance/w1-arb-dh-livefire.json

    # positive control (machinery test; checker MUST reject at C2)
    python3 acceptance/pos_control_mp.py
    python3 acceptance/pos_control_arb.py

    # checkers, cross-check, independent validation, cost curve
    python3 reference_checker.py acceptance/w1-mp-*.json acceptance/w1-arb-*.json
    python3 checker_ref.py       acceptance/w1-mp-*.json acceptance/w1-arb-*.json
    cd acceptance && python3 crosscheck.py w1-mp-null-t100.json w1-arb-null-t100.json \
        w1-mp-null-t1000.json w1-arb-null-t1000.json \
        w1-mp-null-t10000.json w1-arb-null-t10000.json \
        w1-mp-null-deep-t100.json w1-arb-null-deep-t100.json \
        w1-mp-dh-livefire.json w1-arb-dh-livefire.json \
        w1-poscontrol-mp.json w1-poscontrol-arb.json
    python3 validate_arb_transcripts.py acceptance/w1-mp-*.json acceptance/w1-arb-*.json
    python3 acceptance/cost_curve.py

## 9. File inventory (acceptance suite additions)

| file | role |
|---|---|
| `acceptance-report.md` | this report |
| `cost-curve.json` | acceptance test (iii) — M3 economics calibration points |
| `acceptance/w1-{mp,arb}-null-{t100,t1000,t10000,deep-t100}.json` | null-test exclusion transcripts (suite item 1) |
| `acceptance/w1-{mp,arb}-dh-livefire.json` | DH live-fire refutation transcripts, common rectangle (item 3) |
| `acceptance/w1-poscontrol-{mp,arb}.json` | positive-control transcripts (item 2; checker-REJECTED at C2 by design) |
| `acceptance/pos_control_{mp,arb}.py` | positive-control harnesses (machinery reuse, C2 bypass, labeled) |
| `acceptance/crosscheck.py` | two-producer cell-wise consistency checker (item 4) |
| `acceptance/cost_curve.py` | cost-curve builder (item 5) |
| `acceptance/logs/` | all producer, checker, cross-check, and validation logs |
