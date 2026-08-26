# The Arb/FLINT producer leg — install record, capability table, validation record

**Status:** DONE, 2026-08-26 (Session 8, D1 M1 v1 work item: the off-the-shelf leg of the
two-producer rule, D-R3). Producer: `producer_arb.py` (this directory). Trust: the leg is
UNTRUSTED BY DESIGN — its output enters the trusted statement only through the displayed
hypothesis H-ENCL (FORMAT.md §8.1); every public statement stays "kernel-checked modulo the
displayed hypotheses", never "fully machine-checked".

---

## 1. Install record (exactly what worked)

One command, first attempt, no retries needed (the retry loop was armed but never used):

```
python3 -m pip install --user python-flint
# -> Downloading python_flint-0.6.0-cp39-cp39-macosx_11_0_arm64.whl (9.8 MB)
# -> Successfully installed python-flint-0.6.0
```

* Interpreter: system Python 3.9.6 (`/usr/bin/python3`, Apple CommandLineTools framework
  build, arm64), pip 21.2.4.
* Installed to the user site: `~/Library/Python/3.9/lib/python/site-packages/flint/`.
* The wheel bundles its own FLINT/Arb dylibs — no brew, no headers, no compiler needed.
  The fallback ladder (`--break-system-packages`, `~/rh-arb-venv` venv on the uv-installed
  CPython 3.10.12 at `~/.local/bin/python3.10`, brew flint) was prepared but not required.
* Version installed: **python-flint 0.6.0** (the newest wheel available for cp39; newer
  0.7.x/0.8.x lines require Python ≥ 3.10 or later — irrelevant here, 0.6.0 exposes
  everything this leg needs). mpmath 1.3.0 was already present on the same interpreter
  (used ONLY for cross-validation, never inside the producer).

## 2. Capability table (verified LIVE — `arb_capability_check.py`, transcript `arb-capability-check-run.txt`, ALL CHECKS PASS)

| capability | API | verified how |
|---|---|---|
| Riemann zeta on complex balls | `acb(...).zeta()` | B1/C1 + F1/F2 cross-checks |
| Hurwitz zeta ζ(s, a) | `acb(...).zeta(acb(a))` | C2; exercised end-to-end by the f_DH residual H1 |
| Dirichlet L (bonus, unused in v1) | `acb.dirichlet_l` | C3 (existence only) |
| precision control | `ctx.prec` (bits) | B1: radius 2⁻⁹¹-class at 64 bits → 2⁻²⁹⁰-class at 256 bits |
| honest balls: exact midpoint + radius | `x.mid()`, `x.rad()`, both `is_exact()`, `man_exp()` → exact m·2ᵉ | D2–D5; zero edge case D4 |
| exact rational → containing ball | `arb(fmpq(n, d))` | D6 on 4 samples incl. a 30-digit numerator; re-verified at EVERY runtime conversion (producer `rat_ball`) |
| interval hull of two balls | `x.union(y)` (1-D balls are intervals, so the hull covers the whole segment) | capability F1 + producer `hull_ball` runtime re-check |
| directed bounds | `x.lower()` / `x.upper()` (exact dyadics; lower rounds toward −∞, upper toward +∞) | E1–E4: strict-both-sides tests on non-dyadic rationals of both signs + a wide-ball case |
| inclusion isotonicity (wide input balls) | any acb op | F1: ζ over the hull of a whole segment contains 5 independently (mpmath) computed interior values |
| interval atan2 | `arb.atan2(y, x)` — argument order verified (atan2(1,0)=π/2, atan2(1,−1)=3π/4) | G1 + the order probe recorded here |
| π as a ball | `arb.pi()` | G2 |
| certified comparisons (True only when certain) | `a > b` etc. | G3/G4 (straddling ball certifies neither side) |
| f_DH residual at ρ_DH | full Arb pipeline | H1: ball-certified \|f_DH(ρ_DH)\|² ≤ 2.8·10⁻³¹ at prec 300 |

**Balls are honest midpoint+radius:** `mid()` is an arf (exact dyadic at full stored
precision), `rad()` a mag (exact dyadic UPPER bound on the error — note `arb("1","0.5")`
stores radius 0.50000000093…, outward, never inward). The producer therefore converts
ball → integer (lo, hi) at scale K through the EXACT route `[mid − rad, mid + rad]` →
Fraction → floor/ceil (no directed-rounding call trusted), with `lower()`/`upper()` as a
redundant bracketing assert. Rounding direction is tested, not assumed (E1–E4).

## 3. What the producer implements (derivations in `producer_arb.py`, D-P0…D-P8)

* **Value rows:** segment-hull ball evaluation (D-P4 + Arb's inclusion isotonicity D-P0)
  gives one box valid for ALL s on the closed segment — the exact H-ENCL(a) quantifier;
  adaptive exact-rational bisection until the INTEGER box passes C6; outward integer
  conversion per D-P2 (widening only, so it preserves H-ENCL truth).
* **Argument rows:** the FORMAT.md §10 recipe, derived in full as D-P5 — same-rotation
  endpoint atan2: the C6 box pins an open coordinate half-plane; on it
  θ_φ = φ + atan2(rotated) is a continuous arg branch; two continuous branches over a
  connected interval differ by a constant 2πn, so Δ_k = atan2(rot f(q)) − atan2(rot f(p)),
  φ cancelling (same rotation both ends — different rotations per endpoint would be
  unsound). Rotations are exact component swaps/negations. Division by 2π via outward
  interval division by the `arb.pi()` interval; clamp to [−A/2, A/2] (A even) is sound by
  FORMAT.md D3 + intersection-of-enclosures.
* **Winding m:** produced as the unique integer in [S_lo/A, S_hi/A] after the C8 width
  check; the producer refuses to write a transcript contradicting its requested mode.
* **Modulus floor:** Fd = K, Fn = isqrt(min_k(mre²+mim²)) — C11 holds by construction
  (D-P7); C6 forces Fn ≥ 1.
* **Prevalidation:** every transcript is run through `reference_checker.py` before the
  file is written; a failing transcript is never written.

## 4. Produced transcripts (both ACCEPT; run transcript `arb-producer-run.txt`)

| file | mode/function | rectangle | segments | winding enclosure (turns) | m | certified floor |
|---|---|---|---|---|---|---|
| `w1-arb-zeta-exclusion.json` | exclusion / zeta | [3/5, 7/10] × [10, 11] | 18 | [−10, 8]/10⁶ | 0 | \|ζ\| ≥ 0.13142… on ∂R |
| `w1-arb-dh-refutation.json` | refutation / f_DH | [4/5, 41/50] × [8569/100, 8571/100] | 50 | [999973, 1000023]/10⁶ | 1 | \|f_DH\| ≥ 3.018…·10⁻⁴ on ∂R |

Scales K = 10³⁰, A = 10⁶, base precision 300 bits; each run < 0.2 s. The exclusion box is
the SAME rectangle as FORMAT.md §11's artificial example — now with real certified
enclosures (the D-R6 ledger sentence would read: no zeros of ζ in [3/5,7/10]×[10,11],
δ₀ = 1/10 — modulo H-ENCL and H-AP; never "RH verified in W"). The DH transcript is the
live-fire true-positive: the producer+checker pipeline FIRES on the certified off-line
zero ρ_DH = 0.808517182456637 + 85.699348485377592i (D1 direction file line 104), m = 1
pinned by an enclosure of width 50/10⁶ turns. Its trust label is the D-R8 checker-level
one — no Lean-backed conclusion about f_DH.

**Producer-side negative controls** (recorded at the end of `arb-producer-run.txt`): asked
for mode `refutation` on the zero-free zeta box the producer REFUSES (exit 1, "produced
winding m = 0", no file written); asked for mode `exclusion` on the DH box it REFUSES
("produced winding m = 1"). A harder probe — [21/40, 39/40] × [100, 101], σ₁ only 1/40
off the line and σ₂ at 39/40 — certifies m = 0 with 30 segments in under a second
(output kept in the session scratchpad only; rerunnable from the transcript's command).

## 5. Cross-validation record (binding rule: every rigorous enclosure vs independent high-precision evaluation)

`validate_arb_transcripts.py` (mpmath 1.3.0, dps 40 — independent library and algorithms;
heuristic floats, so a pass is evidence, a failure is stop-the-line):

* V1: 90 + 250 sampled boundary values, ALL inside the integer boxes;
* V2: dense principal-argument unwrapping gives winding 0.0 and 1.0, matching claimed_m
  and [S_lo, S_hi]/A on both transcripts;
* V3: sampled min |f| respects both claimed floors.

Plus, inside `arb_capability_check.py`: hull-containment (F1), point-value agreement at
prec 300 vs mpmath dps 80 within radius + decimal slack (F2), atan2/π enclosures (G1/G2).

**Harness lesson recorded (first run of the capability check had 2 FAILs, both harness
bugs, zero Arb bugs):** (i) `mpmath.mpc(0.65, 10)` evaluates at the FLOAT 0.65 ≠ 13/20 —
1e-17 off, vastly wider than a 1e-89 ball; (ii) comparing a 60-digit decimal print
against a 1e-61-wide ball by exact containment fails on print rounding alone. Fix: exact
rational inputs and containment-with-declared-decimal-slack. Kept here because the same
two traps will bite any future cross-validation script.

## 6. Independence discipline (D-R3 two-producer rule)

This leg shares with the mpmath leg ONLY the contract files `FORMAT.md` /
`w1-schema.json` (and the checker-side `reference_checker.py` for prevalidation, which
produces no numbers that enter any transcript). No evaluation code, no helpers, no
constants computed elsewhere: every number in an Arb-leg transcript comes from
python-flint balls + exact Python integer/Fraction arithmetic inside `producer_arb.py`.
The f_DH FORMULA is necessarily shared (it is the definition of the target, quoted
verbatim from `results/ccm-dh-test/dh.py` lines 5–8 via FORMAT.md §9.2) — formula
sharing, not code sharing. Disagreement between the two legs beyond stated radii is a
stop-the-line event (m2a-m2b-design.md §4).

## 7. File inventory (this leg's additions to the directory)

| file | role |
|---|---|
| `arb-leg-notes.md` | this record |
| `arb_capability_check.py` + `arb-capability-check-run.txt` | live capability verification, rerunnable |
| `producer_arb.py` | the Arb-leg producer (UNTRUSTED), derivations D-P0…D-P8 in the module docstring |
| `w1-arb-zeta-exclusion.json` | real exclusion transcript (null-test / M3-prototype instance) |
| `w1-arb-dh-refutation.json` | real live-fire refutation transcript (D-R8 checker-level true-positive) |
| `validate_arb_transcripts.py` | independent mpmath cross-validation (NOT the second producer leg) |
| `arb-producer-run.txt` | end-to-end run: producer → reference checker ACCEPT ×2 → cross-validation ALL PASS |
