# M3 exclusion-ledger pricing — the LEDGER only (Session 20, queue item 2b)

**Written 2026-09-10 by pricing agent 2b (Claude Fable 5.1).** Brief: `results/d1-m2a/dr8/BRIEF.md` §2b. This file is a PRICING, not an implementation: nothing under `results/d1-m3/` is created, no producer is run, no Lean is edited, no build is launched. Authorities read in full: `directions/D1-certified-refutation-arm.md` (M3 at line 87 of the milestone ladder; the charter's "Exclusion ledger" clause at line 48; D-R6 at line 141; "Current frontier"); `directions/B2-refutation-program.md` ("Current frontier", line 99, quoted verbatim in §1.1 below); `results/d1-m1/FORMAT.md` §0, §2, §6.3, §8.1, §9.1–9.2, §12; `results/d1-m1/acceptance-report.md` §0–§1, §5–§7; `results/d1-m1/RUN-REPORT.md`; the cost curve `results/d1-m1/cost-curve.json` (the file used for every recorded number in §3 — the only W1 cost curve on disk; `results/d1-m0/lambda-ladder-cost-curve.{md,json}` is the M0 Weil-form eigenvalue ladder, a different instrument, and is NOT used); the producers' own run logs `results/d1-m1/acceptance/logs/{mp,arb}-null-t10000.log`; `results/d1-m2a/lane-a/EMIT-NOTES.md` §6; `lean/README.md`; `lean/Zeta23/W1/Instances.lean` and `ArgPrincipleBridge.lean` (declaration names and the statement of `cert_of_checkW1_ap` only); the sibling `results/d1-m2a/dr8/PRICING-fDH.md`; `KICKSTART.md` Part 2 item 10; `STATUS.md` (standing orders, the Session-20 queue); `BARRIER-ZOO.md` (group headings, Group IV). Paths below are relative to `rh-program/` unless absolute. Every SHA-256 in §2 was computed this session from the on-disk files (a read, not an M3 computation). One probe was run (Appendix A: six single `acb.zeta` evaluations per precision, one process, 0.4 s in all — the same probe grade as 2a's two `lake env lean` probes; not a producer run). U.S. English.

Status line: §0 one-paragraph answer — DONE; §1 format + layout + index — DONE; §2 first rows without compute — DONE; §3 cost of new rows — DONE; §4 what a row licenses / cannot certify / the zoo entry it does not create / GO-NO-GO — DONE; §5 refutation-shaped close — DONE; Appendix A (probe verbatim) — DONE.

## 0. One-paragraph answer

A ledger row is one closed box R = [σ₁, σ₂] × [T₁, T₂] with ½ < σ₁ ≤ σ₂ < 1, carried by TWO W1 exclusion transcripts (m = 0, one per producer leg, FORMAT §9.1), both accepted by the two Python checkers and kernel-checked in `W1/Instances.lean`-style literals, cell-wise cross-checked CONSISTENT, each pinned by its SHA-256, with the D-R6 sentence "no zeros of ζ with Re s ≥ ½ + δ₀ in [T₁, T₂]" (δ₀ = σ₁ − ½ recorded) and a prose provenance of the box choice. The four null boxes of the M1 v1 acceptance suite — eight transcripts, both legs — are already rows of exactly this kind and can seed the ledger with ZERO producer compute (§2: hashes, Lean names, checker and cross-check records all on disk); what the seed costs is bookkeeping plus eight three-line Lean corollaries (§1.6) and one leaf build. New rows are cheap on the Arb leg — minutes per box at 10⁶ and 10⁹, tens of minutes to an hour at 10¹² (single-evaluation cost 0.008 s → 0.16 s, radius 4·10⁻⁸⁵, Appendix A; per-row segment counts unmeasured above 10⁴ and bracketed 10³–10⁴, §3.4) — and IMPOSSIBLE on the mpmath leg above ≈ 10⁵ (Euler–Maclaurin with N ≈ T/2 terms: 62 s per evaluation at 10⁶, days at 10⁹, years at 10¹², from the recorded 0.62 s at 10⁴), so every row above 10⁵ is one-legged until a Riemann–Siegel-class rigorous evaluator is built for that leg (weeks-class producer work, RUN-REPORT §6.4) — and the two-producer rule is the only detector of the checker's blind spots (FORMAT §8.1), so a one-legged row is not a citable row. Neither Mathlib nor the kernel runs out at any of these heights (§3.6). A row licenses exactly the m = 0 branch of `cert_of_checkW1_ap` for its literal — no zeros of ζ in the closed box, kernel-checked modulo H-ENCL — and nothing else: never RH in a range (even a tiling of boxes stops at σ₁ > ½ + δ₀ and can never reach the line), never Λ > 0 (that is the m ≥ 1 mode), nothing about ζ outside the boxes, no zoo entry (§4). Recommendation (§4.4): **GO for the seed** (half a session, no compute, no 10(d) trigger) with three optional one-legged Arb calibration rows at 10⁶/10⁹/10¹² folded into the same session (≈ 1 h of one heavy job; they fix the segment-count axis this pricing had to bracket); **NO-GO now for a row program** — below the 3·10¹² record every row re-certifies known territory, above it every reachable row is one-legged and isolated, and B2's poster, quoted in §1.1, points at no height at all. GO-later triggers named in §4.4.

## 1. Format: what a row is, where it lives, how it is indexed

### 1.1 What the poster constrains — quoted, because it decides what "provenance of the box choice" can honestly say

`directions/B2-refutation-program.md`, "Current frontier" (line 99), verbatim:

> Survives as the program's refutation channel (consensus ~6.75) with deflated rhetoric: the "wanted poster" constrains only Ω(N)-dense off-line configurations — it does NOT address isolated/Lehmer-type or carrier-wave failure modes, and must say so. The first theorem (short-interval simplicity + off-line local-density cap) is verified provable and publishable on its own. Λ-channel (M6) pending literature check. Repairs are scoping/honesty fixes, not structural.

And the D1 direction file's own honesty clause (line 50): "the poster constrains only Ω(N)-dense off-line ensembles at scales ≥ γ^{0.5505}; isolated Lehmer-type configurations pass every poster constraint vacuously. So the poster prunes and prioritizes; it never guarantees the needle is findable."

Consequence for the ledger, stated once so no row can overstate it: **the poster names no height and no box.** A box's provenance can be one of exactly four kinds, and the index records which (§1.4, field `provenance.kind`): `acceptance` (the M1 null tests — instrument-validation boxes, chosen for the cost curve, not by any prior); `calibration` (boxes chosen to measure cost at a height); `prior` (a box chosen by a search PRIOR that the direction file names — Stopple's Lehmer-pair statistics near t = 10⁶, Bober–Hiary isolated windows at 10²⁴–8·10³⁴ — with the prior cited; the poster is never the cited reason); `pointer` (a box aimed by a detector hit or an external claim that passed the claim screen, with the screen record cited). "Poster-guided" in M3's title means the poster's PROFILE (shallow, locally sparse, mirror-paired) is what a `pointer` box is screened against; it is not a source of coordinates.

### 1.2 A row, exactly

One row = one box + two legs + the cross-check + the sentence + the provenance:

| component | content | source of truth |
|---|---|---|
| box | σ₁, σ₂, T₁, T₂ as exact rationals (strings), δ₀ = σ₁ − ½ | the transcripts' `rect` (identical on both legs, C2-checked) |
| leg mp | one W1 exclusion transcript (`function: "zeta"`, `mode: "exclusion"`, `claimed_m: "0"`), its SHA-256 and byte count, segments, K, A, winding enclosure [S_lo, S_hi]/A, C11 floor Fn/Fd, wall seconds, the two Python checker verdicts, the Lean literal name and its `_check` theorem with the build record | the JSON file; `Instances.lean` (or its successor module) |
| leg arb | the same for the Arb leg | idem |
| cross-check | `crosscheck.py` overlap-pair count and verdict CONSISTENT (a disjoint pair proves one leg's H-ENCL false: stop-the-line) | the cross-check log |
| sentence | D-R6 verbatim form: "no zeros of ζ with Re s ≥ ½ + δ₀ in T₁ ≤ Im s ≤ T₂ — equivalently no zeros of ζ in [σ₁, σ₂] × [T₁, T₂] — kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)"; never "RH verified in W" | D-R6; README v1.1 label |
| provenance | `kind` per §1.1 plus free prose: why this box, who chose it, what prior or pointer, what the negative means | the row's `PROVENANCE.md` |
| grade | `box` (an isolated W1 box) — D-R6 requires Turing-method-grade entries to be marked separately; the value `turing` is reserved and no row can carry it until such an entry format exists | D-R6 |
| status | `accepted` (both legs + cross-check + kernel), `one-leg` (one leg only — NOT citable in any sentence), `pending` | this pricing, §3.8 |

A row is not "a transcript": one transcript is half a row. The DH live-fire pair (m = 1, `f_DH`) and the two positive controls (checker-REJECTED by design) are not rows and never enter the ledger; the ledger is the ζ-exclusion register only.

**Label note (a silent-inconsistency channel of the kind standing order 5 exists for).** Every on-disk ζ transcript carries the schema-fixed v1.0 string `kernel-checked modulo displayed hypotheses H-ENCL and H-AP (producers untrusted)` (FORMAT §9.2, `w1-schema.json`); since v1.1 (2026-09-02) the licensed label is `kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)` (`lean/README.md`, "Honest label, binding"). An accepted transcript is never edited (its hash is its identity), so the ledger row carries the LICENSED label in its own `trust_label` field and records, once, in the README that the embedded string is the v1.0 contract string superseded by v1.1 for ζ. The same tension will be resolved contract-side whenever FORMAT is bumped (2a's label sweep is the DH half of the same item).

### 1.3 File layout under `results/d1-m3/` (proposed; nothing created)

```
results/d1-m3/
  README.md            charter paragraph (D1 line 48 + D-R6 verbatim), the licensed label, the v1.0-string note,
                       the four provenance kinds, how a row is added (the checklist below), never-say list
  LEDGER.md            human-readable, APPEND-ONLY, one dated line per row: id | box | δ₀ | status | sentence | hashes
  index.json           machine-readable index (§1.4), regenerated by ledger_check.py from rows/ — never hand-edited
  ledger-schema.json   JSON Schema 2020-12 for index.json (shape only, like w1-schema.json)
  ledger_check.py      UNTRUSTED validator: for every row re-hashes both transcripts, re-runs both Python checkers and
                       crosscheck.py, confirms the Lean names exist in the mirror and the recorded build log names them,
                       rebuilds index.json, exits nonzero on any drift
  rows/<row-id>/
    ROW.json           the row record (one index entry, canonical)
    PROVENANCE.md      the prose provenance (kind + text), the sentence, the added-by/added-when stamp
    mp.json  arb.json  the transcripts — a COPY for new rows; for the four seed rows a POINTER file (`mp.json.ref`
                       holding path + SHA-256) to results/d1-m1/acceptance/, so the acceptance suite stays the single
                       source of truth that Instances.lean's back-parse was verified against
    checker-mp.log  checker-arb.log  crosscheck.log   the three verdict logs (copies or pointer files, same rule)
```

Row id (filesystem-safe, content-determined): `zeta_<σ₁>_<σ₂>_<T₁>_<T₂>` with each rational written `num-den` (integers as themselves): `zeta_3-5_9-10_100_101`, `zeta_21-40_39-40_100_101`. Two rows on the same box are a versioning error, not two rows.

Checklist for adding a row (goes in README; each step is one command already on disk except the Lean corollary): both producers on the box → both Python checkers ACCEPT → `crosscheck.py` CONSISTENT → `validate_arb_transcripts.py` (evidence, not certificate) → emit the two Lean literals + `_check` theorems (`emit_lean.py`), build, back-parse (`recon_instances_verify.py`) → the two corollaries (§1.6) → hashes into `ROW.json` and LOG.md (10(i)) → `ledger_check.py` → commit.

### 1.4 The index entry (`ROW.json` = one element of `index.json`)

```json
{
  "row_id": "zeta_3-5_9-10_100_101",
  "function": "zeta", "mode": "exclusion", "claimed_m": "0",
  "box": {"sigma1": "3/5", "sigma2": "9/10", "T1": "100", "T2": "101"},
  "delta0": "1/10", "height": 100.0, "height_span": "1",
  "grade": "box", "status": "accepted",
  "trust_label": "kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)",
  "sentence": "no zeros of zeta with Re s >= 1/2 + 1/10 in 100 <= Im s <= 101 (no zeros of zeta in [3/5, 9/10] x [100, 101])",
  "legs": {
    "mp":  {"transcript": "../d1-m1/acceptance/w1-mp-null-t100.json", "sha256": "17f0…3212", "bytes": 16588,
            "segments": 52, "K": "1e30", "A": "1e12", "winding_lo_hi": ["-24", "28"], "floor": "Fn/Fd",
            "wall_seconds": 1.0, "python_checkers": {"reference_checker": "ACCEPT", "checker_ref": "ACCEPT"},
            "lean": {"module": "Zeta23.W1.Instances", "data": "mpNullT100", "floor": "mpNullT100_floor",
                     "check": "mpNullT100_check", "corollary": "mpNullT100_exclusion",
                     "build_record": "results/d1-m1/recon_lean_instances.log"}},
    "arb": {"…": "same shape"}
  },
  "crosscheck": {"log": "../d1-m1/acceptance/logs/crosscheck.log", "overlap_pairs": 83, "verdict": "CONSISTENT"},
  "provenance": {"kind": "acceptance", "note": "M1 v1 acceptance null test 1 (cost-curve height point); acceptance-report.md §1"},
  "added_utc": "…", "added_by": "…", "entry_sha256": "sha256 of this record with entry_sha256 blank"
}
```

Integers as decimal strings throughout (FORMAT §12.6's reason); `height` is a float for sorting only, never load-bearing. `ledger_check.py` regenerates `index.json` as the array of all `ROW.json` files sorted by (height, δ₀) and refuses a row whose `status` is `accepted` without both legs, both ACCEPTs, a CONSISTENT cross-check, and a `_check` name per leg.

### 1.5 What the index must make impossible to say

* No aggregate field. There is no "total height covered", no "RH verified up to": isolated boxes extend no contiguous record (D-R6, verbatim: "isolated boxes extend no contiguous record").
* No row without δ₀, and no sentence without it.
* No `accepted` status on one leg (§3.8).
* No `turing` grade until a Turing-method entry format exists (none is priced here).

### 1.6 The theorem shape a row carries in Lean (3 lines per leg; the seed's only Lean touch)

The m = 0 branch of `cert_of_checkW1_ap` (`W1/ArgPrincipleBridge.lean` line 449, statement read this session) instantiated on the literal, with the checker fact from `checkW1Floor_spec` (`Soundness.lean` line 1162):

```lean
/-- Ledger row zeta_3-5_9-10_100_101, mp leg: no zeros of ζ in the closed box, modulo H-ENCL. -/
theorem mpNullT100_exclusion (hEncl : W1EnclOK riemannZeta mpNullT100) :
    ∀ s ∈ W1Rect mpNullT100, riemannZeta s ≠ 0 :=
  (cert_of_checkW1_ap mpNullT100 (checkW1Floor_spec mpNullT100_check).1 hEncl).2 (by decide)
```

(`W1Data.m : ℤ`, so `mpNullT100.m = 0` is `by decide` or `rfl`; `W1Rect d` is the closed rectangle, `Soundness.lean` line 106.) Eight such corollaries for the seed, in a NEW leaf module `Zeta23/W1/Ledger.lean` importing `ArgPrincipleBridge` and `Instances` — not appended to `Instances.lean`, which is emitter-written and back-parse-verified as it stands. Expected `#print axioms`: `[propext, Classical.choice, Quot.sound]` (the DH twin of the same shape probed to exactly these in 2a, Appendix B). Nothing downstream imports the new file except the root `Zeta23.lean` (+1 import line), so the build is the leaf plus the root: seconds, no cascade. The corollary is what the ledger sentence points at; `#check` shows the box and the one displayed hypothesis and nothing else.

## 2. First rows within reach today: the eight null transcripts

All eight can be rows with **no new computation** — not one producer run, not one checker run: every verdict the row needs is already on disk and dated. Exactly which:

| row (box) | δ₀ | leg | file (`results/d1-m1/acceptance/`) | bytes | SHA-256 (computed 2026-09-10) | segments | winding [S_lo, S_hi]/A | floor \|ζ\| ≥ | Python ×2 | Lean (`W1/Instances.lean`) | cross-check |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **R1** [3/5, 9/10] × [100, 101] | 1/10 | mp | `w1-mp-null-t100.json` | 16 588 | `17f06458036b6df1a23e6406f409b5802757e776c376474e11900d81cba13212` | 52 | [−24, 28]·10⁻¹² | 0.35555 | ACCEPT | `mpNullT100`, `mpNullT100_check` | 83 pairs, CONSISTENT |
| | | arb | `w1-arb-null-t100.json` | 9 073 | `3248f7ca4a0160d5369bf61c8ac367ab95591e2bf5bd995b998878369e1899d5` | 27 | [−14, 13]·10⁻⁶ | 0.08328 | ACCEPT | `arbNullT100`, `arbNullT100_check` | |
| **R2** [3/5, 9/10] × [1000, 1001] | 1/10 | mp | `w1-mp-null-t1000.json` | 24 880 | `a18a7bf713b802ae4c7755d3f5f7041ef5c4b256f8fa40ec8f7572aabbcf8cc0` | 81 | [−41, 40]·10⁻¹² | 0.015573 | ACCEPT | `mpNullT1000`, `_check` | 158 pairs, CONSISTENT |
| | | arb | `w1-arb-null-t1000.json` | 19 504 | `36b7685a5ae464c6ad5dd6d93834bf2fa44fd63b32b090163c7fcedfd7809476` | 65 | [−29, 36]·10⁻⁶ | 0.013827 | ACCEPT | `arbNullT1000`, `_check` | |
| **R3** [3/5, 9/10] × [10000, 10001] | 1/10 | mp | `w1-mp-null-t10000.json` | 371 219 | `007c4977f2f58052b414dcd25eacf9eeccfb8046b6cfbff39d2d232267ee3168` | 1 294 | [−679, 637]·10⁻¹² | 8.13·10⁻⁵ | ACCEPT | `mpNullT10000`, `_check` | 2 547 pairs, CONSISTENT |
| | | arb | `w1-arb-null-t10000.json` | 270 942 | `5422646bd635edf0753874a44968a9e41c66d7aa7a4c054dbab3f2c5ca7381bf` | 983 | [−495, 488]·10⁻⁶ | 7.64·10⁻⁶ | ACCEPT | `arbNullT10000`, `_check` | |
| **R4** [21/40, 39/40] × [100, 101] | 1/40 | mp | `w1-mp-null-deep-t100.json` | 18 346 | `2faaec2e251a1451a0f5a5e2257b39b9d4e2bd12c78b6d69c142baa5c3249f59` | 58 | [−28, 30]·10⁻¹² | 0.35550 | ACCEPT | `mpNullDeepT100`, `_check` | 90 pairs, CONSISTENT |
| | | arb | `w1-arb-null-deep-t100.json` | 9 935 | `53cc7897dee89a4f9cbb740eb322e7bd787fdbe9b0cad4d184453f9a8d75ba27` | 30 | [−16, 14]·10⁻⁶ | 0.03052 | ACCEPT | `arbNullDeepT100`, `_check` | |

Records, all on disk and dated: Python verdicts `acceptance/logs/{reference-checker,checker-ref}-accepts.log` (2026-08-26) and `recon_checker_pass.log` (2026-09-02, after the mp-leg repairs, transcripts byte-identical in numeric content — RUN-REPORT §1.2); kernel `checkW1Floor … = true` by `decide +kernel` for all eight, `[propext]`, build `recon_lean_instances.log` (656 jobs, 13.9 s), back-parse 0 mismatches over 2 940 rows (`recon_instances_verify.py`); cross-check `acceptance/logs/crosscheck{,-t10000}.log`; independent float validation `independent-validation*.log` (evidence, not certificate). Not rows (§1.2): `w1-{mp,arb}-dh-livefire.json` (m = 1, `f_DH`; hashes `756b1447…` / `e39b90cb…`, recorded here only so nobody mistakes them for ledger material) and the two positive controls.

**What the seed needs that is not on disk:** the eight corollaries of §1.6 (one leaf build), the four `ROW.json` + `PROVENANCE.md` files (kind `acceptance`; the prose is acceptance-report §1 and the D-R6 sentences RUN-REPORT §1.4 already prints), `README.md`, `LEDGER.md`, `ledger_check.py` (mostly calls to the four existing scripts), the LOG.md hash entry. Half a session, one agent, zero producer compute, thermal: one short `lake build` of a leaf module and the root.

**What the four seed rows certify, and what they are worth.** The four D-R6 sentences RUN-REPORT §1.4 already licenses: no zeros of ζ with Re s ≥ 3/5 in [100, 101], [1000, 1001], [10000, 10001], and none with Re s ≥ 21/40 in [100, 101] — each kernel-checked modulo H-ENCL. All four lie far below the rigorous verification record 3·10¹² (Platt–Trudgian; D1 line 103), so as facts about ζ they are known; their ledger value is that they are the program's OWN certificates in the program's own trust vocabulary (two independent untrusted producers, one kernel), and that they are the ledger's format-validation rows — the same role the acceptance suite played for the checker. The ledger README says this in one sentence so no reader mistakes four boxes below height 10⁴ for a verification result.

## 3. Cost of new rows — the measured curve, one probe, and honest brackets

### 3.1 What the cost curve measured (`cost-curve.json`; single-run wall times, Apple Silicon, Python 3.9.6, mpmath 1.3.0, python-flint 0.6.0)

| box (δ₀ = 1/10 unless noted) | height T | mp segments | mp wall s | mp evaluations (segment + endpoint) | mp s / evaluation | arb segments | arb wall s | arb ms / segment |
|---|---|---|---|---|---|---|---|---|
| [3/5, 9/10] × [T, T+1] | 10² | 52 | 1.0 | 52 + 52 | 0.019 (N = 65 EM terms) | 27 | 0.092 | 3.4 |
| same | 10³ | 81 | 8.6 | 110 + 81 | 0.078 (N ≈ 515) | 65 | 0.135 | 2.1 |
| same | 10⁴ | 1 294 | 1 564.7 | 2 536 total (log) | **0.62** (N ≈ 5 015) | 983 | 2.608 | **2.65** |
| [21/40, 39/40] × [100, 101], δ₀ = 1/40 | 10² | 58 | 1.1 | 58 + 58 | 0.019 | 30 | 0.089 | 3.0 |

Derived facts, each from the file or the producer logs: (i) the Arb leg's cost is per segment and flat in T up to 10⁴ (2–3.4 ms per segment, ≈ 2–3 `acb.zeta` evaluations per segment at ≈ 1 ms each — Appendix A); (ii) the mp leg's cost per evaluation grows with its Euler–Maclaurin term count N = max(20, ⌈½(t_max + 29)⌉) ≈ T/2 (`mp-leg-notes.md` line 98; producer metadata), ×7.9 for the last decade — linear in N within measurement; (iii) the segment count is driven by the σ₁ edge: at T = 10⁴ the mp log records 50/76/91/**1 077** segments on bottom/right/top/left, the left edge being σ = 3/5 where the boundary passes closest to on-line zeros (floor 8.13·10⁻⁵ there vs 0.0156 at 10³) — the count is a property of the particular box's nearest zero, not a smooth function of T; (iv) checking is negligible: Python 0.03 s, kernel "seconds" for 1 294 rows, and the M2a barrier rows, same integer arithmetic, measured **≈ 1.4 ms per row** in the kernel (`lean/README.md`, `results/d1-m2a/kernel-time.log`); (v) depth: δ₀ = 1/40 vs 1/10 costs the same at T = 10² (the D-R6 caveat that δ₀ → 1/log γ boxes must be priced before M3 is funded is untested by these points and stands — acceptance-report §5).

### 3.2 The probe: single `acb.zeta` evaluations at σ = 3/5 up to height 10¹² (Appendix A, verbatim)

At the Arb leg's base precision 300 bits: 0.001 s per evaluation at 10⁴; **0.006–0.009 s at 10⁶; 0.008 s at 10⁹; 0.16 s at 10¹²**; enclosure radius 10⁻⁸⁸ at 10⁴, 5·10⁻⁸⁷ at 10⁶, 5·10⁻⁸⁶ at 10⁹, **4·10⁻⁸⁵ at 10¹²** — against the K = 10³⁰ scale the leg needs 10⁻³⁰, so precision is not within fifty orders of running out at 10¹². The 10⁹ → 10¹² factor (×20 for ×1000 in T) is the √T signature of a Riemann–Siegel-type main sum (the algorithm selection inside `acb_zeta` is Arb's; recorded here as the measured scaling, not as a documentation claim — no docs on disk, no network). Extrapolating that factor: ≈ 5 s per evaluation at 10¹⁵, ≈ 100–160 s at 10¹⁸.

### 3.3 The mp leg above 10⁴ (extrapolation of the recorded N ∝ T cost; labeled as such)

0.62 s per evaluation at N ≈ 5·10³ (recorded), linear in N: **≈ 62 s at 10⁶** (N ≈ 5·10⁵), **≈ 6·10⁴ s ≈ 17 h at 10⁹**, **≈ 6·10⁷ s ≈ 2 years at 10¹²** — per single evaluation, before the 10³–10⁴ evaluations a row needs. RUN-REPORT §6 item 4 already records the conclusion: "M3 heights need a Riemann–Siegel-class evaluator on that leg." Such an evaluator with a DERIVED certified remainder (Gabcke-class bound — the mp leg's rigor is its own hand-derived remainder, `zeta_encl.py` STEPS 1–6, re-derived by both auditors; mpmath's own `mp.zeta` uses Riemann–Siegel for large t but as a heuristic float, unusable as an enclosure) is producer work of the same class D-R3 priced at "weeks, not pip install", with the same audit standard as the audited Euler–Maclaurin module. It is needed by nothing else in the program today (M2a's Lane A/B evaluate Polymath15 approximants of H_t, not ζ at height).

### 3.4 The unmeasured axis: segments per row above 10⁴ (bracketed, not guessed)

Three data points (27, 65, 983 on the Arb leg) with the last dominated by a close approach on the σ₁ edge cannot be extrapolated. What can be said from the mechanism: the expected number of on-line zeros per unit height, (1/2π) log(T/2π), is 1.17 at 10⁴, 1.91 at 10⁶, 3.01 at 10⁹, 4.11 at 10¹² — so the number of near-approach events per unit-height box grows only ×3.5 from 10⁴ to 10¹², while the per-event bisection depth depends on how close the nearest zero comes to the edge (random; depth cap 40 on both legs, never hit so far). **Bracket used below: 10³–10⁴ segments per unit-height row at δ₀ = 1/10, 2–3 evaluations per segment.** The bracket is the reason the three calibration rows of §4.4 are worth their hour: one Arb row per decade at 10⁶, 10⁹, 10¹² turns it into three measured points at a cost of minutes each.

### 3.5 Rows per hour per leg (one process; the thermal policy allows 4 heavy jobs, so ×4 for a batch)

| height | Arb: s per row (3 evals × bracket × §3.2 cost) | **Arb rows / h / process** | mp: s per row | **mp rows / h / process** |
|---|---|---|---|---|
| 10⁴ (recorded) | 2.6 | ≈ 1 400 (recorded: 1 row in 2.6 s) | 1 565 (recorded) | 2.3 (recorded) |
| 10⁵ | ≈ 3–30 | 100–1 000 | ≈ 6 s/eval × 3·10³–3·10⁴ ≈ 5–50 h | 0.02–0.2 |
| 10⁶ | 23–230 | **16–160** | 62 s/eval × 3·10³–3·10⁴ ≈ 2–20 days | **≈ 0.002–0.02 (not viable)** |
| 10⁹ | 25–250 | **14–140** | 17 h/eval × 3·10³–3·10⁴ ≈ 6–60 years | **0 (impossible)** |
| 10¹² | 490–4 900 | **0.7–7** | 2 y/eval ⇒ millennia | **0 (impossible)** |
| 10¹⁵ (for the ceiling) | ≈ 1.5·10⁴–1.5·10⁵ | 0.02–0.2 (4–40 h per row) | — | — |
| 10¹⁸ | ≈ 3·10⁵–5·10⁶ | days to weeks per row | — | — |

Reading: the Arb leg makes rows at 10⁶ and 10⁹ for minutes each and at 10¹² for ten minutes to an hour and a half each; its practical ceiling for a ledger row is ≈ 10¹⁵ (hours per row); the Bober–Hiary heights 10²⁴⁺ that the D1 prior names are out of reach of `acb.zeta` by many orders (that is the "extreme-height rigorization" the brief excludes as contingent). The mp leg is dead above ≈ 10⁵ without the §3.3 evaluator.

### 3.6 Where precision, Mathlib, and the kernel run out — they do not, in this range

* **Arb precision:** radius 4·10⁻⁸⁵ at 10¹² and 300 bits (probe); the escalation cap is 6 000 bits (`producer_arb.py` line 155). Not a limit below ≈ 10⁵⁰-class heights, where time is the limit long before.
* **mp precision:** 288 bits; the Euler–Maclaurin sum of N ≈ T/2 O(1) terms loses ≈ log₂ N bits to accumulation (≈ 40 bits at 10¹²) against a 10⁻³⁰ target — not the limit; time is (§3.3).
* **Mathlib:** supplies `riemannZeta` and `differentiableAt_riemannZeta` and nothing height-dependent; the theorem is the same theorem at every height. Nothing to run out.
* **Kernel:** `decide +kernel` on the integer checker is linear in rows at ≈ 1.4 ms per row (§3.1 (iv)); the literals at T = 10¹² with K = 10³⁰ are integers of the same ≈ 45-digit size as today's (the box coordinates scale K, not T; mesh breakpoints are rationals like 10¹² + k/2ʲ). A 10⁴-row transcript kernel-checks in ≈ 15 s. The one Lean-side limit is the DEFINITION COMPILER's list-literal depth: `set_option maxRecDepth 100000` is tested to 1 294 rows (`Instances.lean` header) and untested above; the M2a chunk pattern (per-chunk literal modules, ≈ 3.5 s each import-dominated, then a concatenation) is the known remedy — about half a session of emitter work the first time a row exceeds ≈ 2 000 segments, and no soundness content.

### 3.7 The depth axis, flagged (not this brief's, but the ledger's real price tag)

At the heights above, 1/log γ = 0.072 (10⁶), 0.048 (10⁹), 0.036 (10¹²); the acceptance suite's deep box has δ₀ = 1/40 = 0.025, already below the poster's shallow scale at all three heights — but its cost is measured only at T = 10² (no penalty there). Near the line |ζ(½ + δ₀ + iγ)| ≈ δ₀·|ζ′(ρ)| at each on-line zero, so a δ₀ = 1/40 edge at height 10¹² meets ≈ 4 zeros per unit height at a distance where C6 needs bisection to depth ≈ log₂(1/δ₀)-plus; the segment bracket of §3.4 is for δ₀ = 1/10 and is NOT licensed for 1/40 at large T. D-R6's gate — "cost of δ₀ → 1/log γ boxes must be priced before M3 is funded" — is unmet by this pricing and by the data; one deep calibration row per decade would meet it at the same minutes-per-row cost on the Arb leg (added to the §4.4 calibration set).

### 3.8 The consequence of the two-producer rule (binding, FORMAT §8.1)

The checker cannot see K, A, or the row↔segment alignment; "the only detectors are the cell-wise two-producer cross-check … and the producers' own discipline, never the checker — one more reason the two-producer rule is mandatory" (FORMAT §8.1, verbatim). Hence a row with one leg is not an accepted row: it is `status: one-leg`, kept for calibration and provenance, never cited in a sentence. With the mp leg dead above ≈ 10⁵ (§3.3), **every new row at 10⁶, 10⁹, 10¹² is `one-leg` until the Riemann–Siegel-class mp evaluator exists** — so the true cost of accepted rows at those heights is not the Arb minutes of §3.5 but that evaluator (weeks) plus its audit, and, per §3.7, the deep-box calibration.

## 4. What a row licenses, what the ledger can never certify, the zoo entry it does not create, GO/NO-GO

### 4.1 The theorem shape a row licenses (verbatim consequence of `cert_of_checkW1_ap`, m = 0 branch)

For the row's literal `d` on each leg: `W1EnclOK riemannZeta d → ∀ s ∈ W1Rect d, riemannZeta s ≠ 0` — "no zeros of ζ in the closed box [σ₁, σ₂] × [T₁, T₂], kernel-checked modulo the displayed hypothesis H-ENCL (this leg's producer untrusted)"; two legs give two theorems with two hypotheses, never merged (each leg pairs with its own literal, as M2a does). The D-R6 sentence "no zeros of ζ with Re s ≥ ½ + δ₀ in [T₁, T₂]" is licensed only when σ₂ is joined to 1 by the classical nonvanishing on Re s ≥ 1 (in Mathlib `51e6992e` as `riemannZeta_ne_zero_of_one_le_re`, named in the header of `Mathlib/NumberTheory/LSeries/Nonvanishing.lean` line 22 — read this session, not probed) and the box family covers [σ₁, 1) — for a single box the licensed sentence is the box sentence, and the README says so.

### 4.2 What the ledger can never certify (each a structural fact, not a budget one)

1. **RH in a range — not even with a tiling.** C2 requires ½ < σ₁ strictly, and C6 (every boundary box excludes 0) fails on any edge through an on-line zero, so no box can have its left edge on the line: a family of boxes tiling [½ + δ₀, 1 − ε] × [T₁, T₂] certifies "no zeros with Re s ≥ ½ + δ₀ in the range" and leaves the strip ½ < Re s < ½ + δ₀ untouched at every δ₀ > 0. That strip is exactly the poster's shallow regime δ ≲ 1/log γ (D-R6: "a σ₁ > 1/2 box is structurally blind to the poster's own shallow δ ≲ 1/log γ regime"). RH-in-a-range needs a zero COUNT (Turing's method: the number of zeros in the whole strip up to T equals the number found on the line), which W1 does not carry; that is the reserved `turing` grade, unpriced. In particular the ledger can never discharge M2a's H1 (`ZeroVerification`, the Platt–Trudgian height), however many rows it holds.
2. **Λ > 0.** A row is m = 0. Λ > 0 is the m ≥ 1 mode's consequence (D1 line 33: a certified off-line zero ⇒ Λ > 0), and an exclusion ledger by definition never contains one. Nor any upper bound on Λ: that is the whole-strip Polymath15 barrier (M2a), a different format.
3. **Anything about ζ outside the boxes.** Each theorem quantifies over `W1Rect d` only; no row says anything about the next unit of height, and the index carries no aggregate (§1.5). Isolated boxes extend no contiguous record; the rigorous verification record stays 3·10¹² (Platt–Trudgian) whatever the ledger holds (D-R6's deleted "inherits the improvement" clause stays deleted).
4. **Anything about a specific claimed counterexample it did not box.** A `pointer` row that comes back m = 0 refutes the claim's box, not the claim's author's other boxes; the screen record says which.

### 4.3 The barrier-zoo entry it does NOT create

KICKSTART 10(c): "Barrier-zoo entries are extracted from these statements, not from prose." A ledger row is a certified FACT about ζ in one box, not a barrier: it kills no proof class (Group IV), instantiates no model world (Group I), caps no certificate class (Group II — a formalized fact is not a formalized ceiling), and is no structural no-go (Group III). The only zoo-shaped statement in this pricing is 4.2 (1) — "W1 boxes cannot reach the line, so an exclusion ledger is blind to depth < δ₀" — and that is already in the record twice: D-R6 (line 141) and the D1 barrier self-check item 3, the depth-resolution wall (line 95: "a FINDING wall, not a certifying wall"). No new entry; the zoo's count does not move. Nor does the ledger create a "verification record" entry: there is none to create.

### 4.4 GO/NO-GO against KICKSTART 10(d) and the sponsor's lean-budget rule

**GO — the seed, bounded, no signal, no 10(d) trigger.** Cost: half a session of one agent (the §1.3 files, four `ROW.json`/`PROVENANCE.md`, `ledger_check.py` assembled from the four existing scripts, eight three-line corollaries in a new leaf `W1/Ledger.lean`, one leaf + root build in seconds, LOG.md hashes per 10(i)), zero producer compute, one lake process. It discharges the charter's durable-ledger clause (D1 line 48) and D-R6's entry format in a form that any future negative — a `pointer` box from the conductor-Fuchs scanner, the claim-screening service, or a Lehmer-pair prior — lands in without inventing a format on the day. It is a "Lean-checked statement" in the letter of 10(d) and not in its spirit (eight corollaries of an already-audited theorem on already-kernel-checked literals change no belief); it must not pull anyone's budget. Fold in, at the orchestrator's option and in the same session: **three `calibration` rows on the Arb leg** at [3/5, 9/10] × [T, T+1], T = 10⁶, 10⁹, 10¹² (`status: one-leg`, ≈ 1 h of one heavy job by §3.5, kernel-checked, hashed) and three deep twins at δ₀ = 1/40 if the first three come in under the bracket — they replace §3.4's bracket and §3.7's gap with six measured points, which is what D-R6 asks for before M3 is funded. Sequence: after the D-R8 build 2a recommends, since `W1/Ledger.lean` and `DavenportHeilbronn.lean` touch the same import graph and the packaging of the W1 topic (10(j)) should ship both at once.

**NO-GO now — a row program (systematic new accepted rows at 10⁶–10¹²).** Three independent reasons, any one sufficient: (i) below 3·10¹² every row re-certifies Platt–Trudgian territory — instrument value only; (ii) above 3·10¹² and up to the Arb ceiling ≈ 10¹⁵ every row is `one-leg` (§3.8) until the Riemann–Siegel-class mp evaluator is built and audited (weeks, needed by nothing else), and even then an isolated unit-height box at δ₀ ≥ 1/40 is exactly the kind of negative D-R6 discounts and the poster does not point at (§1.1); (iii) the D-R6 depth gate is unmet (§3.7). Under the sponsor's rule — "we must be really smart about directions to pursue" — a program whose every output is a near-certain negative in a regime the theory owner says it does not constrain is the wrong purchase. **GO-later triggers, named:** (a) a `pointer` fires — a conductor-Fuchs anomaly, a Lehmer-pair candidate from the Stopple-class prior, or an external claim passing the poster screen: then the W1 box at that location is the deciding instrument (Arb in minutes; mp if T ≤ 10⁵, otherwise the evaluator first) and its negative is a ledger row with signal; (b) the mp Riemann–Siegel evaluator is funded for that reason; (c) a Turing-method-grade entry format is designed (then rows can say "RH in [T₁, T₂]", and that is a different milestone with its own pricing). None of these is in sight today; the seed makes sure the ledger is ready when one is.

## 5. Refutation-shaped close (KICKSTART 10(c))

1. **The format holds.** A row = one box + two W1 exclusion transcripts (m = 0) + both Python verdicts + the kernel facts + the cross-check + SHA-256s + the D-R6 sentence with δ₀ + a typed provenance; layout and index as §1.3–1.4; the licensed label is v1.1's, the transcripts' embedded string is v1.0's and is recorded, not edited.
2. **The seed holds without computation.** The eight acceptance null transcripts are four complete rows (R1–R4, §2): every verdict, hash, Lean literal and cross-check they need is on disk and dated; the only new artifacts are bookkeeping and eight three-line corollaries of `cert_of_checkW1_ap`.
3. **The Arb leg cannot be the cost driver at 10⁶–10¹²**, because a single evaluation costs 0.008–0.16 s with radius ≤ 4·10⁻⁸⁵ (Appendix A): rows are minutes at 10⁶ and 10⁹ and under two hours at 10¹² within the §3.4 bracket; its ceiling is ≈ 10¹⁵.
4. **The mp leg cannot produce a row above ≈ 10⁵**, because its certified Euler–Maclaurin enclosure costs N ≈ T/2 terms per evaluation (0.62 s at 10⁴, recorded; 62 s at 10⁶, 17 h at 10⁹, years at 10¹²); a Riemann–Siegel-class evaluator with a derived remainder is weeks-class producer work needed by nothing else.
5. **A one-legged row cannot be an accepted row**, because the checker cannot see K, A, or row alignment and the two-producer cross-check is the only detector (FORMAT §8.1); hence every new row at 10⁶–10¹² is `one-leg` until statement 4's evaluator exists.
6. **Neither Mathlib nor the kernel can run out at any reachable height**: the theorem is height-independent, the kernel is ≈ 1.4 ms per row on ≈ 45-digit integers regardless of T; the only Lean-side limit is the definition compiler's list literal above ≈ 1 300 rows, cured by the M2a chunk pattern.
7. **A row licenses exactly** `W1EnclOK riemannZeta d → ∀ s ∈ W1Rect d, riemannZeta s ≠ 0` per leg — "no zeros of ζ in the closed box, kernel-checked modulo H-ENCL" — and no shorter sentence.
8. **The ledger cannot certify RH in a range**, because C2 and C6 keep every box's left edge strictly right of the line: a tiling certifies "no zeros with Re s ≥ ½ + δ₀" and is blind to the strip below δ₀, which is the poster's own shallow regime; a range statement needs a Turing-method zero count the format does not carry (reserved grade `turing`, unpriced). It therefore can never discharge M2a's H1.
9. **The ledger cannot yield Λ > 0**, because Λ > 0 follows from a certified zero (m ≥ 1) and the ledger contains only m = 0; nor any bound on Λ, which is the whole-strip barrier of M2a.
10. **The ledger cannot say anything about ζ outside its boxes**, because each theorem quantifies over `W1Rect d` only, isolated boxes extend no contiguous record (D-R6), and the index carries no aggregate by construction.
11. **The ledger creates no barrier-zoo entry**, because a certified fact in a box kills no proof class, instantiates no world, and caps no certificate; the one zoo-shaped statement here (blindness below δ₀) is already in the record as D-R6 and the D1 self-check's depth-resolution wall.
12. **The poster cannot supply a box**, because B2's frontier constrains only Ω(N)-dense off-line configurations and "does NOT address isolated/Lehmer-type or carrier-wave failure modes"; provenance is therefore `acceptance`, `calibration`, `prior`, or `pointer`, never "the poster".
13. **GO holds for the seed** (half a session, no compute, no 10(d) trigger, sequenced with 2a's D-R8 build and the W1 packaging), with the six Arb calibration rows as the priced option that meets D-R6's depth gate; **NO-GO holds for a row program now**, with GO-later on a fired pointer, a funded mp evaluator, or a Turing-grade entry format.

## Appendix A — probe (verbatim; scratchpad `probe_arb_height.py`, not committed)

Run 2026-09-10, one Python process, python-flint 0.6.0 (Arb), `acb(arb(3)/5, arb(T)).zeta()` twice per height (first call, then repeat), σ = 3/5, at the Arb leg's base precision 300 bits and at 64 bits. Whole script 0.4 s wall. Output, in full:

```
prec 300 bits
  T=1e2  wall    0.004s /    0.000s  |zeta| ~ [2.36399092983373686… +/- 4.22e-89]  rad [1.2174…e-89 +/- 2.64e-178]
  T=1e3  wall    0.001s /    0.000s  |zeta| ~ [0.86811394640700567… +/- 2.24e-90]  rad [3.2028…e-89 +/- 7.27e-180]
  T=1e4  wall    0.001s /    0.001s  |zeta| ~ [0.44393544078314915… +/- 8.24e-91]  rad [1.0791…e-88 +/- 2.56e-177]
  T=1e6  wall    0.009s /    0.006s  |zeta| ~ [1.80466874320958539… +/- 3.30e-89]  rad [5.4736…e-87 +/- 2.17e-176]
  T=1e9  wall    0.008s /    0.008s  |zeta| ~ [1.93134801215148981… +/- 2.86e-90]  rad [4.7391…e-86 +/- 1.40e-175]
  T=1e12 wall    0.162s /    0.165s  |zeta| ~ [1.73566403808518878… +/- 2.92e-89]  rad [4.1038…e-85 +/- 9.07e-175]
prec 64 bits
  T=1e2  wall    0.000s /    0.000s  |zeta| ~ [2.36399092983373686 +/- 1.41e-18]  rad [7.40281394831545869e-19 +/- 4.37e-37]
  T=1e3  wall    0.000s /    0.000s  |zeta| ~ [0.868113946407005673 +/- 7.40e-20]  rad [3.22530338246823765e-18 +/- 1.12e-36]
  T=1e4  wall    0.000s /    0.000s  |zeta| ~ [0.443935440783149159 +/- 4.32e-19]  rad [1.14613812605903991e-17 +/- 3.26e-35]
  T=1e6  wall    0.000s /    0.000s  |zeta| ~ [1.80466874320958540 +/- 1.05e-18]  rad [6.04439893783502366e-16 +/- 3.47e-34]
  T=1e9  wall    0.003s /    0.003s  |zeta| ~ [1.93134801215148982 +/- 1.32e-18]  rad [5.23339038454550997e-15 +/- 3.13e-33]
  T=1e12 wall    0.093s /    0.093s  |zeta| ~ [1.73566403808518878 +/- 3.93e-18]  rad [4.53184610991801075e-14 +/- 2.68e-32]
```

(The 90-digit midpoints are abbreviated with "…" above for width; the full log is reproduced by re-running the script.) Source:

```python
import time, sys, signal
from flint import acb, arb, ctx
class TO(Exception): pass
def h(*a): raise TO()
signal.signal(signal.SIGALRM, h)
for prec in (300, 64):
    ctx.prec = prec
    print(f"prec {prec} bits")
    for T in (10**2, 10**3, 10**4, 10**6, 10**9, 10**12):
        s = acb(arb(3)/5, arb(T))
        try:
            signal.alarm(200)
            t0 = time.perf_counter(); v = s.zeta(); dt = time.perf_counter() - t0
            t0 = time.perf_counter(); v = s.zeta(); dt2 = time.perf_counter() - t0
            signal.alarm(0)
            r = max(v.real.rad(), v.imag.rad())
            print(f"  T=1e{len(str(T))-1:<2d} wall {dt:8.3f}s / {dt2:8.3f}s  |zeta| ~ {abs(v).mid()}  rad {r}")
        except TO:
            print(f"  T=1e{len(str(T))-1:<2d} TIMEOUT (> 200 s)")
        sys.stdout.flush()
```

*End of pricing. Nothing outside this file was edited; no producer, checker, emitter or build was run; one 0.4-second evaluation probe only.*
