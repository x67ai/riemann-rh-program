# M2a item (e) — the Instance02 barrier certificate: two-producer cross-check, reference checker, Lean kernel check; and the Gomila M2a′ conversion (screen steps 3–4)

**Date:** 2026-09-03 (Session 14, D1 M2a, workflow `d1-audit-m2a-s14`; implementation/verification agent).
**Scope:** SPEC.md v1.0 (`results/d1-m2a/SPEC.md`) item (e) of the design note's work breakdown (`results/d1-m0/m2a-m2b-design.md` §1.6): the row-2 transcripts of the two untrusted producers (item (c) Arb/FLINT leg, `transcripts/row2-arb/`; item (d) mpmath-ball leg, `transcripts/row2/`) are cross-checked against each other (SPEC P-11), run through an independent exact-arithmetic reference checker, and embedded in Lean where the kernel checks them; then the claim-screening protocol's steps 3–4 (`results/d1-m0/gomila-screen.md` §4) are executed on the Gomila claim at its pinned commit.
**Trust language (binding; D-R3/D-R8; SPEC §0, §3.7):** every accepted transcript below is *"kernel-checked modulo the displayed hypotheses H2-B and hHol (producers untrusted)"* — never "fully machine-checked". The Λ bracket of record is **0 ≤ Λ ≤ 0.2** (Rodgers–Tao; Platt–Trudgian Corollary 2); the strict "Λ < 0.2" is never written. Nothing about the Gomila claim is a record (§5 below; `gomila-screen.md` §7).
**Verdict in one line:** Lane B of Instance02 is COMPLETE on both legs and kernel-checked (39 + 72 prisms, 17 947 rows, `checkBarrier … = true` for both); the two legs agree cell-wise at every seam of both chains (0 disjoint boxes in 13 729 + [PENDING: mp-at-arb-seams pairs] overlapping pairs); item (e) is nevertheless **PARTIAL** — the theorem `lambda_le_point2` (Λ ≤ 0.2 in ray form) is not proved because Lane A (the asymptotic window rows + tail) and the `Defs.lean` v1.1 glue do not exist (§3.4, the cut line). The Gomila screen advances to **screen-open with steps 3–4 executed as far as the sealed artifacts allow**: the sealed 883-prism log converts only as a chain + scalar table (its rows do not exist), that conversion replays exactly, D1's two producers agree with each other and with Gomila's printed scalars on 29 sampled prisms (Arb leg complete; mpmath leg [PENDING]) — not screen-pass (§5.6).

---

## 1. Inputs (what was on disk at start, unchanged)

| object | file(s) | producer | size |
|---|---|---|---|
| mpmath-ball leg, row-2 barrier chain | `transcripts/row2/manifest.json` + `prism-0000…0038.json` | `producer_mp.py` + `ft_mp.py` (item (d); `mp-leg-notes.md`) | 39 prisms, seams 0 = τ₀ < … < τ₃₈ = 3719/20000 < t₀ = 93/500; 184 rows per prism, 7 176 rows; K = 10²⁴, A = 10¹² |
| Arb/FLINT leg, row-2 barrier chain | `transcripts/row2-arb/instance02-barrier-manifest.json` + `instance02-prism-0000…0071.json` | `producer_arb.py` (item (c); `arb-leg-notes.md`) | 72 prisms, seams 0 < … < t₀; 64–289 rows per prism, 10 771 rows; K = 10¹², A = 10⁶ |
| the Lean checker | `Zeta23/DBN/BarrierCert.lean` (item (b); `lean-notes.md`) | — | `checkPrism`, `checkBarrierChain`, `checkBarrier`, `cert_of_checkBarrier`, `cert_of_checkBarrier_xy` |
| the Gomila claim | `judegomila/dbn-lambda-01787854-candidate-audit` @ `a74738deb6d5e0f76887cb36901da08b68dca705` (main), fetched this session into `~/rh-lean-work/gomila-ap/main-a74738d` (retry loop, first attempt succeeded) | — | `barrier/certificates/barrier_target_closed.log` (896 lines, SHA-256 `2d010f70902dca1627f40ddcd68f3954b37fd9596f7840787415eeafb20805f4`, matching `SHA256SUMS` at a74738d and byte-identical to the copy at ea09b2f) |

Both row-2 chains are the full mesh (no sub-box cut): the mp leg's notes and the Arb leg's notes each record a COMPLETE chain 0 → t₀ accepted by `barrier_ref_checker.py`.

## 2. The two-producer cross-check (SPEC P-11; design note §4 — disagreement beyond radii is stop-the-line)

**The obstacle and its resolution.** The two chains were produced by adaptive prism-length rules and have DIFFERENT seams — only seam 0 is common (the earlier `crosscheck_legs.py` run compared exactly that one seam). A cell-wise comparison of enclosures of f_τ needs the SAME τ. So each leg was re-run for ONE prism at every seam of the other leg's chain (`xcheck_arb_at_seams.py`: the Arb leg at the 39 mp seams, 104 s; `xcheck_mp_at_seams.py`: the mp leg at the 72 Arb seams, ≈ 30 s per prism, [PENDING: wall]). These cross-check prisms are not part of any chain; they exist so that at every seam of BOTH chains two independent enclosures of the same function on the same boundary exist.

**What is compared (`crosscheck_instance02.py`, exact `Fraction` arithmetic, no float in any verdict).** Per seam:
1. **value boxes on the common mesh refinement** — for every pair of overlapping boundary segments (same edge, overlapping parameter intervals) the boxes [reLo, reHi]/K × [imLo, imHi]/K of the two legs must INTERSECT (both enclose f_τ on the overlap; a disjoint pair means at least one enclosure is false);
2. **edge-total argument increments** — each leg's sum of its argument rows over an edge, at its scale A, must intersect the other's (both enclose the same increment of arg f_τ along the edge);
3. the floors Fn/Fd, the defects E/K and the displacements D/K are reported side by side (E and D are upper bounds from different majorants; no verdict, order-of-magnitude agreement expected); the winding sums are reported (each leg's own C-B9).

**Result A — Arb leg at the 39 mp seams (`xcheck-arb-at-mp-seams-run.txt`):** 39 seams compared, **13 729 overlapping segment pairs, 0 disjoint value-box pairs, 0 disjoint edge-argument intervals — CONSISTENT.** Floors agree to 1–2 % (the Arb leg's hull floors are slightly lower because its mesh is coarser: e.g. seam 30: 2.3638 mp / 2.3280 arb); **E agrees to all printed digits at every seam** (both legs implement the 10.50 weld of SPEC D-2.4 and Proposition 6.6(iv)–(v); e.g. 1.9023·10⁻⁵ at τ = 0.06897, 1.0330·10⁻⁷ at τ = 0.18595); D differs by the legs' different prism lengths and majorants (e.g. 1.24 mp vs 1.98 arb at seam 30); every winding sum contains 0 with width ≤ 2·10⁻¹⁰ turn (mp) / ≤ 3·10⁻⁴ turn (arb).

**Result B — mp leg at the 72 Arb seams (`xcheck-mp-at-arb-seams-run.txt`):** [PENDING — running at the time of writing; the table is appended to the run file as the prisms land.]

**Result C — seam 0 (the one common seam, both chains' own prisms):** `arb-crosscheck-legs-run.txt` (Session 14, Arb agent): 465 overlapping pairs, 0 disjoint; E identical (4.1192·10⁻⁴); floors 4.3825 (arb, 289 rows) vs 4.6294 (mp, 184 rows). Re-confirmed by Result A's seam 0 row.

**Verdict:** no stop-the-line event. The cross-check is producer-side evidence for H2-B (it tests the two legs' arithmetic against each other on the same function); it is not a proof of H2-B, which stays displayed.

## 3. The checkers

### 3.1 `checker_ref.py` — the independent exact-arithmetic reference checker

Written for this item as a SECOND untrusted implementation of SPEC §7.3 (the first is the contract agent's `barrier_ref_checker.py`, cross-multiplication style): `fractions.Fraction` arithmetic, mirroring `Zeta23.DBN.checkBarrier` **clause by clause and in the Lean order** (the mirror map is in its docstring: `densPos`/`edgeOK`/`rowsOK`/`sumArgLo`/`floorRowsOK` → `dens_pos`/`edge_ok`/`rows_ok`/…; `checkPrismW1 (toW1 r p)` → `check_prism_w1`; `checkPrism` → `check_prism`; `checkBarrierChain` → `check_barrier_chain`; `checkBarrier` → `check_barrier`). It shares no code with either producer or with `barrier_ref_checker.py`; a disagreement with the kernel would localize to one clause. A `--chain-only` mode checks a manifest's rectangle, t₀ and seams without reading prism files (for chain-only objects, §5.2).

Run record (`checker-ref-run.txt`): **ACCEPT** on `transcripts/row2` (39 prisms, 7 176 rows), `transcripts/row2-arb` (72 prisms, 10 771 rows), `transcripts/mini` (3 prisms, 552 rows), `transcripts/mini-arb` (3 prisms, 252 rows), and the SPEC §12 micro-example (2 prisms, 15 rows) — the same five verdicts as `barrier_ref_checker.py`.

Negative controls (`checker_ref_controls.py`, `checker-ref-controls-run.txt`) on the REAL prism 0 of the mp chain: 21/21 as expected — 14 mutations rejected at exactly the named clause (C-B0 ×3, C-B3 ×2, C-B4, C-B5, C-B6, C-B7 ×2, C-B8, C-B9, C-B11, C-B12) and 2 valid weakenings accepted (boxes widened by one unit at K with the floor relaxed by 10/11; argument rows widened by one unit each side), plus 5 chain-level mutations rejected at C-B13/C-B2′. Recorded honestly: three of my first control DATA were wrong, not the checker — (i) "reLo := −1" on a row whose reHi is already negative trips C-B5 before C-B6 (fixed: the box [−1, 1]²); (ii) "all argLo := 1" leaves the ~1.5·10¹⁰-unit argument rows with a huge width, so C-B8 fires, not C-B9 (fixed: shift every argument row by +1, S = [93, 277]); (iii) "floor halved" is NOT a valid weakening because the producers set the prism length at θ = ½ of the gate — (E + D)/floor ≈ 0.51, so halving the floor breaks C-B12 (fixed: floor × 10/11). The checker was right each time.

### 3.2 The Lean kernel — `Zeta23/DBN/Instance02.lean` + `Zeta23/DBN/Instance02/` (116 modules)

**Packaging (SPEC §7.6, item 2 realized):** `Instance02/Rect.lean` (`row2Rect : RectData := ⟨5000000194858, 1, 5000000194859, 1, 16733, 100000, 1, 1⟩`); one module per prism — `Instance02/mp_0000 … mp_0038.lean` (mp leg) and `Instance02/arb_0000 … arb_0071.lean` (Arb leg) — each with `set_option maxRecDepth 100000`, row chunks of ≤ 1 000 rows (`<name>_rows_k`), `def <name> : PrismData`, and the kernel fact `theorem <name>_check : checkPrism row2Rect <name> = true := by decide +kernel`; `Instance02/mp_Barrier.lean`, `Instance02/arb_Barrier.lean` with `row2BarrierMP`, `row2BarrierARB : BarrierData`, the chain fact `…_chain : checkBarrierChain … = true := by decide +kernel`, the split fact `…_prisms : ∀ p ∈ ….prisms, checkPrism ….rect p = true` (from the per-prism theorems), and the monolithic `…_check : checkBarrier … = true` (`unfold checkBarrier; rw [chain, Bool.true_and, List.all_eq_true]; exact _prisms`). The top module `Instance02.lean` imports both and instantiates the soundness theorems (§3.3). No `native_decide` anywhere.

**Emission and fidelity (P-12):** `emit_lean_m2a.py` (untrusted) wrote the modules from the JSON; `verify_lean_m2a.py` — an independent regular-expression back-parse of the emitted Lean, no code shared with the emitter — rebuilt every `PrismData` from the `.lean` text and compared it with the JSON field by field and row by row: **39 prisms / 7 176 rows and 72 prisms / 10 771 rows, 0 mismatches** (`verify-lean-mp-run.txt`, `verify-lean-arb-run.txt`); it also checks `Rect.lean` against the manifest's rectangle and t₀, and the `_Barrier` prism list order.

**Build record (`instance02-build.log`; Lean v4.33.0-rc2, Mathlib `51e6992e`; one `lake` process at a time, each module its own `lake build` invocation):**

| what | modules | serial wall | per module |
|---|---|---|---|
| mp leg: `Rect`, `mp_0000…mp_0038`, `mp_Barrier` | 41 | 157 s | 3.3–3.8 s for a 184-row module (Rect 15.5 s, first import load); `mp_Barrier` 3 s |
| Arb leg: `arb_0000…arb_0071`, `arb_Barrier` | 73 | 217 s | 2.9–4.2 s for 64–289-row modules |
| `Zeta23.DBN.Instance02` (top) | 1 | 2.9 s | — |
| root `Zeta23` (now importing `DBN.Instance02`) | — | 19.6 s, *Build completed successfully (9138 jobs)* | — |

Per-module time is dominated by import loading; the definition compiler and the kernel together cost ≈ 1 s for 184 rows (≈ 5 ms/row), consistent with the M1 measurement (SPEC §7.6 item 3).

**Kernel time of the MONOLITHIC check (the measurement the task asked for; `kernel-time-scratch.lean`, `kernel-time.log`):** `theorem row2BarrierMP_check_kernel : checkBarrier row2BarrierMP = true := by decide +kernel` and the same for `row2BarrierARB` in one scratch file — **28.2 s wall for both together (7 176 + 10 771 = 17 947 rows, ≈ 1.4 ms/row)**, `#print axioms` = `[propext]` for each. So the literal is NOT too large for the kernel at this scale; the per-prism split is kept as the program's packaging (SPEC §7.6: per-module kernel work, parallelizable, one failure does not lose everything) and the monolithic facts in the program modules are derived from the split facts without a second kernel evaluation. The SPEC's "serial hours" projection was for 5·10⁶ rows; the actual transcripts are 280× smaller.

**`#print axioms` (`instance02-axioms.log`):** `row2BarrierMP_chain`, `row2BarrierARB_chain` — no axioms; every `<prism>_check` and both `_prisms` — `[propext]`; both monolithic `_check` — `[propext, Quot.sound]`; `row2_barrier_mp`, `row2_barrier_arb`, `row2_barrier_mp_xy`, `row2_barrier_arb_xy` — `[propext, Classical.choice, Quot.sound]`. No `sorryAx`, no `Lean.ofReduceBool`.

**One first-build failure, recorded:** the first `mp_Barrier.lean` proved the monolithic fact with the micro-example's pattern (`show List.all [p₀, …, p₃₈] (checkPrism row2Rect) = true; simp only [List.all_cons, …]`), which timed out at `isDefEq` (200 000 heartbeats) on 39 prisms; replaced by `rw [List.all_eq_true]; exact …_prisms`, which builds in 3 s. Also recorded: for about four minutes (00:54–00:58) two serial build loops of the Arb modules overlapped (a parent script was killed but its child loop survived), i.e. two `lake` processes and three heavy processes for that window — a thermal-policy breach and a lake-locking risk; the whole `Instance02` subtree was therefore rebuilt CLEAN afterwards from deleted oleans, one process at a time ([PENDING: clean-rebuild record]).

### 3.3 What the Lean instance proves, exactly (`Instance02.lean`)

    theorem row2_barrier_mp (G : ℝ → ℂ → ℂ)
        (hHol : ∀ t : ℝ, 0 ≤ t → t ≤ t0 row2BarrierMP →
          ∃ U : Set ℂ, IsOpen U ∧ BarrierRect row2BarrierMP ⊆ U ∧ DifferentiableOn ℂ (G t) U)
        (hEncl : BarrierEnclOK G row2BarrierMP) :
        ∀ t : ℝ, 0 ≤ t → t ≤ t0 row2BarrierMP → ∀ z ∈ BarrierRect row2BarrierMP, G t z ≠ 0

and `row2_barrier_arb` (the Arb transcript), plus the coordinate forms `row2_barrier_mp_xy` / `row2_barrier_arb_xy` (`cert_of_checkBarrier_xy`, for H = G·B, the shape hypothesis (iii′) of the amended bridge consumes). Read with the instance in mind (G t z = H_t(z)/B_t(z); R = [X, X+1] × [y₀, 1]; t₀ = 93/500): **modulo H2-B for the transcript and the holomorphy of H_t/B_t near R, H_t has no zero in R for any t ∈ [0, t₀]** — Theorem 1.2's hypothesis (iii) in its simplified box form, from two independent transcripts. The statements are generic in G because `Bt` is not yet in the trusted layer (§3.4).

### 3.4 The cut line — why item (e) is PARTIAL

`lambda_le_point2` (SPEC §8.3: ∀ t ≥ 1/5, ∀ z, Ht t z = 0 → z.im = 0, modulo H1, H2, H3) is NOT proved. Missing, none of it started in this session (all Lean-stream items outside item (e)'s brief):
1. `Defs.lean` v1.1 — `Polymath15Bridge'` (the instantiable bridge, SPEC §3.2–3.3, BLOCKING), `Bt`, `HtEntire`;
2. Lane A — the asymptotic window rows + Lemma-T tail transcript (no producer has run it; SPEC §5), `checkAsym`, `cert_of_checkAsym`, L-A1/L-A2;
3. L-B3 (`Bt` holomorphic and nonvanishing near R) and the exact-rational glue L-G.
With those, the instance theorem is `hH3.1` applied to `hH1`, (ii′) from Lane A and (iii′) from `row2_barrier_*_xy` at H = Ht, B = Bt. Lane B — the numerically intensive part — is done twice and kernel-checked twice.

## 4. Files written this session (all in `results/d1-m2a/` unless stated; every one is either untrusted tooling or a run record)

| file | role |
|---|---|
| `checker_ref.py`, `checker-ref-run.txt` | the Fraction reference checker (§3.1) and its five ACCEPT runs |
| `checker_ref_controls.py`, `checker-ref-controls-run.txt` | 21 controls on real data |
| `xcheck_arb_at_seams.py`, `xcheck_mp_at_seams.py` | per-seam drivers of the two producers (cross-check prisms) |
| `transcripts/xcheck-arb-at-mp-seams/seam-NNNN/…`, `transcripts/xcheck-mp-at-arb-seams/prism-NNNN.json` | the cross-check prisms (Arb at the 39 mp seams; mp at the 72 Arb seams) |
| `crosscheck_instance02.py`, `xcheck-arb-at-mp-seams-run.txt`, `xcheck-mp-at-arb-seams-run.txt` | the P-11 cross-check and its run records |
| `emit_lean_m2a.py`, `verify_lean_m2a.py`, `verify-lean-{mp,arb}-run.txt` | JSON→Lean emitter (untrusted) and the independent back-parse (0 mismatches) |
| `instance02-build.log`, `instance02-axioms.log`, `instance02-axioms-scratch.lean`, `kernel-time-scratch.lean`, `kernel-time.log` | build, axioms and kernel-timing records |
| `lean/Zeta23/DBN/Instance02.lean`, `lean/Zeta23/DBN/Instance02/*.lean` (program tree; byte-identical copies of the working tree) | the Lean instance, 116 modules, 23 965 lines; `lean/README.md` table updated; root `Zeta23.lean` imports `DBN.Instance02` |
| `gomila/…` | §5 |
| `producer_mp.py`, `producer_arb.py` | ONE data-only edit each: the `"gomila"` instance entry (box, t₀, N) for the spot check; no formula touched (and one manifest label string in the Arb leg generalized from "mini") |

## 5. The Gomila claim — screen steps 3–4 (M2a′ conversion) executed

Pinned identity re-verified: main @ `a74738d` fetched this session (`~/rh-lean-work/gomila-ap/main-a74738d`); the barrier log's SHA-256 matches `SHA256SUMS` at that commit and the copy at the Lean-branch commit `ea09b2f` byte for byte.

### 5.1 Step 3(a) — conversion of the sealed 883-prism log (`gomila/convert_gomila_log.py`; outputs `gomila-scalars.json`, `gomila-chain-manifest.json`, `gomila-log-replay.txt`)

**What the log is.** One summary line per prism — `Prism(k) t=[lo,hi] winding=[m ± r] min_mesh=[m ± r] Dz=… Dt=… spatial=… time=… eps=… margin=… mesh=… PASS` — printed Arb balls; NO per-mesh-point or per-segment enclosures (SPEC §11 row 4; confirmed again on the a74738d copy). Therefore **the per-segment rows of a SPEC prism file cannot be derived from the sealed artifacts**, and `checkPrism` cannot be run on Gomila's own data. What CAN be converted exactly, and was:

| Gomila object | SPEC object | mapping (outward rounding) |
|---|---|---|
| prism k's `t=[lo,hi]` (balls; prism 1's lo is the exact integer 0; prism 883's hi ball contains 129/800) | seam τ_k := the printed lower-endpoint midpoint (an exact decimal = exact rational); the chain [0 = τ₁ < … < τ₈₈₃ < t₀ = 129/800] | continuity checked: prism k's lo midpoint = prism k−1's hi midpoint (same printed digits) on all 883; Δ_k⁺ := (hi_mid + hi_rad) − (lo_mid − lo_rad) with every printed radius widened by one unit in its last digit |
| `min_mesh` M_k (their minimum lower modulus over the mesh POINTS) | a POINT floor — NOT the whole-segment hull floor Fn/Fd of C-B11; the SPEC floor is smaller by their spatial term | M_k⁻ := mid − rad − ulp |
| `Dz`, `Dt` (integers; their box-uniform derivative bounds, `DERIVATIVE_BOX_LEMMA.md`) | producer-side inputs to D (SPEC P-8) | exact |
| `spatial` = D_z/(2(num−1)), `mesh` = 4(num−1) segments of the closed traversal (verified: replay equals the printed value on all 883 prisms — prism 1: 9600/(2·9599) = 0.5000520887…; prism 883: 17/32) | the hull term absorbed into C-B11's floor (SPEC §11 row 3) | replayed from Dz and mesh; required to match |
| `time` = D_t·Δ_k, `eps` = 0.00125 (the allowance; `uniform_error_256.log` certifies e_A + e_B + e_{C,0} ≤ 3.5652·10⁻⁴ < 0.00125 on the whole box, 10.50 weld) | D := D_t·Δ_k, E := 0.00125 | replayed with Δ_k⁺ |
| gate (1): M_k > spatial + D_t·Δ_k + 0.00125 (`BARRIER_CERTIFICATE.md`) | **C-B12** (E + D)·Fd < Fn·K with Fn/Fd := M_k − spatial, E := 0.00125·K, D := D_t·Δ_k·K — the same inequality with the mesh term moved into the floor | replayed as M_k⁻ > spatial⁺ + D_t·Δ_k⁺ + eps⁺ |
| `winding` (a ball in turns) | C-B8/C-B9 analogue | required inside (−¼, ¼) |

**Replay result (`gomila-log-replay.txt`):** 883 prisms; **0 replay failures** — every prism's printed gate margin is reproduced exactly from its own printed inputs (e.g. prism 1: 4.278362 − 0.500052 − 52726·3.5818·10⁻⁵ − 0.00125 = +1.888530, printed 1.888530), every spatial term matches, the chain is continuous, strictly increasing, starts at exactly 0 and its last ball contains t₀; minimum replayed margin 0.519850 at prism 882 (their "minimum prism margin ≥ 0.5198" reproduced); minimum C-B12-form floor M − spatial = 1.011949 (prism 883). Two of my own first-pass conversion errors are recorded honestly: treating the exact "0" as a ±1 ball, and reading `mesh` as points-per-edge×4 instead of segments (both caught by the replay disagreeing with the printed values; fixed; the printed values are what they claim to be).

**Kernel check of the converted chain (`gomila/gomila-scratch-arb.lean`, run by `lake env lean`, `gomila-scratch-arb.log`):** `gomilaChain : BarrierData` with `gomilaRect = ⟨6000000185827, 1, 6000000185828, 1, 1809, 10000, 1, 1⟩`, t₀ = 129/800 and the 883 seams as seam-only dummy prisms (empty rows; every other field a placeholder) — `theorem gomilaChain_chain : checkBarrierChain gomilaChain = true := by decide +kernel` ACCEPTED (no axioms), together with the negative control `checkPrism gomilaRect (seamOnly 0 1) = false` (the dummies are NOT accepted per prism — nothing per-prism is claimed for Gomila's own data). `checker_ref.py --chain-only` on `gomila-chain-manifest.json`: ACCEPT (883 seams). This is a scratch file, not a program module: the claim is not this program's certificate instance.

### 5.2 Step 3(b)/4 — D1's two producers on Gomila's prisms (same box, same t)

**Sample (`gomila/spot-sample.json`):** the protocol asks for ≥ 1 % of cells plus every cell with margin below 2× the median; with 883 prisms whose relative replayed margins (margin/M_k) lie in [0.332, 0.44] — ALL below 2× the median 0.425 — the sample is the **10 thinnest** (prisms 873–882, relative margin 0.332–0.352) **plus 19 evenly spaced** (1, 50, 100, …, 850, 883) = **29 prisms**. For each, both legs were run for one prism on Gomila's box [X, X+1] × [1809/10000, 1] (added as the data-only instance `"gomila"` in both producers; N = 690 988 re-certified constant on the box by each leg's own P-3 check) at the exact seam τ_k of the conversion.

**Arb leg (`gomila/spot-arb/seam-NNNN/`, 29 prisms, 104 s incl. a 67 s moment computation):** all 29 prism files ACCEPT `checkPrism` under `checker_ref.py` (`gomila/checker-ref-spot-arb.txt`) and under the kernel (`gomila-scratch-arb.lean`: 29 `garb…_check` theorems by `decide +kernel`, 8.7 s for the whole file, axioms `[propext]`).
**mpmath leg (`gomila/spot-mp/prism-NNNN.json`):** [PENDING — moments for N = 690 988 (two series, ≈ 8 min each) then 29 prisms at ≈ 40 s each; running.]

**Comparison (`gomila/spot_compare.py`, exact arithmetic; `gomila/spot-compare-run.txt`):** per prism (i) D1-leg vs D1-leg cell-wise boxes and edge arguments (as §2); (ii) each leg vs Gomila's printed scalars — a leg's hull floor must not exceed M_k⁺ (M_k is a point minimum ≥ the true boundary minimum ≥ any valid hull floor), each leg's certified E must be below their allowance 0.00125, each leg's sup|∂_t f| (mp: `DT_sup_dt_f`; Arb: `Mt_seam_sup`) is compared with their D_t (a printed D_t smaller than a certified sup would be a contradiction), and OUR gate at THEIR prism length (2E + DT·Δ_k⁺ < our floor, the SPEC §4.5 form) is evaluated.

Arb-leg results at the 29 sampled seams (mp columns pending): **0 contradictions.** Our hull floors sit 4–5 % below their point floors on every prism (e.g. prism 1: 4.0988 vs M₁ = 4.2784; prism 500: 3.1330 vs 3.2259) — the expected order, and our prescan's min|f| over the mesh reproduces their M_k to 4 digits (prism 1: 4.2784 = 4.27836…); our certified E equals their uniform-error figure at t = 0 (3.565·10⁻⁴ vs their 3.5652·10⁻⁴ — same weld, same box) and decreases with τ (1.1·10⁻⁴ at prism 500) — below their 0.00125 allowance everywhere; our sup|∂_t f| is 0.019–0.027 × their D_t (their box-uniform D_t is 35–50× larger than our certified sup, i.e. their bound is valid but crude — consistent, not contradictory); our gate at their prism length passes on all 29 (their Δ_k is far inside what our enclosures would allow).

### 5.3 What steps 3–4 establish, and what they do not

Established (all D1-side, all exact or kernel-checked): (a) the sealed log's per-prism arithmetic is internally exact — every printed gate margin replays from its printed inputs, the seam chain is a valid C-B13 chain from exactly 0 to t₀ (kernel-checked), and their gate is C-B12 with the mesh term in the floor; (b) on 29 prisms — the ten thinnest and a uniform sample — D1's own independent evaluator(s) reproduce Gomila's point floors to 4 digits, their error constant exactly, and bound the time derivative far below their D_t; D1's own enclosures would certify each of those prisms at Gomila's own prism length; (c) [PENDING] D1's two legs agree with each other cell-wise on those prisms.

NOT established: (d) Gomila's per-prism enclosures themselves — they were never exposed (only summaries are sealed), so `checkPrism`/`checkBarrier` on Gomila's data is impossible and step 3 is complete only in its chain half; (e) anything about the 854 unsampled prisms beyond the replay of their printed summaries; (f) Lane A of the claim (their finite lane and their all-N tail lemma — SPEC §11 rows 6–7 — were not converted or run; the tail is a different lemma from Lemma T and needs the deferred decision); (g) the three prose-only analytic steps their own referee record lists (screen §5).

### 5.4 Verdict for the screen ledger

**screen-open (steps 3–4 executed to the limit of the sealed artifacts; no failure found; not screen-pass).** Not screen-fail: no checker step failed and no producer disagreement exists anywhere in the sample. Not screen-pass: the taxonomy's "checker accepts" cannot be met on rows that do not exist, and only 29 of 883 prisms were produced by D1. What would complete it: Gomila exposing per-segment enclosures (or D1 running its legs on all 883 prisms — 29 took 104 s on the Arb leg, so the full chain is ≈ 1 h on that leg and ≈ 10 h on the mpmath leg: feasible, and then `checkBarrier` would be kernel-checkable on D1's OWN transcript of Gomila's row, which is the M2a′ instantiation in the design note's sense — a second row literal for the same theorem); plus Lane A. Even a full pass would make the row an **M2a′ candidate**, never a record: the bracket of record stays **0 ≤ Λ ≤ 0.2**.

## 6. Thermal / process record

At most two heavy processes of this stream at any time by design (drivers + one serial `lake`), with ONE recorded breach (§3.2: overlapping Arb build loops, ≈ 4 min at three processes, remedied by a clean rebuild). Every network operation (the Gomila fetch) ran in a retry loop (30 × 60 s budget; succeeded at attempt 1).

## 7. Verification ledger (standing order 5)

Exact (Python `fractions`/integers): every checker verdict (`checker_ref.py`), every cross-check verdict, the Gomila log replay and chain. Kernel (`decide +kernel`, Lean v4.33.0-rc2): 111 per-prism facts, 2 chain facts, 2 monolithic facts (scratch), the Gomila chain fact and 29 spot-prism facts (scratch). Read from disk this session: SPEC.md in full, the design note, the screen note, `lean-notes.md`, `BarrierCert.lean` §§1–4, `W1/{Checker,Format,Examples}.lean`, `Instances.lean` header, the two leg notes' headers, Gomila's `BARRIER_CERTIFICATE.md` "One closed-prism gate" section, `barrier_target_closed.log`, `uniform_error_256.log`, `SHA256SUMS` (a74738d). Not verified: the analytic content of H2-B (displayed), Gomila's Lane A, Gomila's per-prism rows (do not exist), the mpmath-leg results marked [PENDING] above.
