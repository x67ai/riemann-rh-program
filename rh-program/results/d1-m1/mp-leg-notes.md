# mpmath-ball producer leg — build record, rigor status, and cut lines

**Status:** built and validated, 2026-08-26 (Session 8, D1 M1 v1; the D-R3 named work item
"independent mpmath ball-arithmetic producer").
**Trust language (binding):** everything in this leg is UNTRUSTED producer-side work by design.
An accepted transcript is "kernel-checked modulo the displayed hypotheses" once the Lean checker
lands; today's acceptances are by the two untrusted reference checkers only. Nothing here is
"fully machine-checked", and no claim in this file exceeds checker-level.

## 1. What was built (the four commissioned components)

| component | file | status |
|---|---|---|
| complex ball layer on mpmath `iv` | `ball.py` | DONE; selftest 5068 checks / 0 failures |
| rigorous ζ(s) enclosures (Euler–Maclaurin, derived remainder) | `zeta_encl.py` | DONE; 200/200 containment vs mp.zeta at dps 100, widths median 2.9e−19 max 5.6e−17; wide-box 180/180 |
| rigorous ζ(s, a) enclosures (same discipline) | `hurwitz_encl.py` | DONE; 200/200 containment vs mp.zeta(s, a) at dps 100, widths median 7.5e−19 max 5.4e−17; a = 1 cross-check vs the independently written ζ evaluator 0 failures; wide-box 135/135 |
| W1 transcript producer (adaptive mesh, derivative-free winding) | `producer_mp.py` | DONE; three transcripts produced and two-checker-accepted (see §4); honest-abort paths exercised live |
| reference checker (Fraction-based executable spec) | `checker_ref.py` | DONE; accepts all five transcripts; all six FORMAT §11 negative controls fail at exactly the intended check; agrees with `reference_checker.py` everywhere tested |

## 2. Where the load-bearing mathematics lives (standing order 5 compliance)

* **Euler–Maclaurin identity + remainder bound:** DERIVED in full in the `zeta_encl.py` module
  docstring (STEPS 1–7: the integration-by-parts induction, the tail specialization, the
  analytic continuation, the G-antiderivative remainder transform, the certified-constant
  bound). The Hurwitz shift is re-derived in `hurwitz_encl.py` (STEPS 3′–7′). The final bound:

      |R_{N,m}(s)| ≤ |(s)_{2m+1}| · |s+2m+1| · C_{2m+2}
                      / ((2m+1)! · (2m+2) · (σ+2m+1)) · (N+a)^{−σ−2m−1},

  valid for σ + 2m + 1 > 0, with C_j = sup_{[0,1]} |B_j(x) − B_j|.
* **The constant C_{2m+2} is CERTIFIED, not quoted:** exact-rational interval Horner over 512
  subintervals of [0,1] on the exact Bernoulli polynomial (`zeta_encl.c_sup`). At the default
  m = 14: certified C_30 = 1.218048e9 against lower bound 1.203150e9 (ratio 1.0124 — the
  overestimate is the interval evaluation's, and it is paid, not assumed away).
* **Bernoulli numbers are exact and recursion-verified:** `bern_exact` re-verifies
  Σ_{j≤k} C(k+1, j) B_j = 0 for every index used, in exact `Fraction` arithmetic, so
  `mpmath.bernfrac` is an untrusted candidate source, not an input. Bernoulli polynomial
  coefficients likewise carry exact self-checks (B_n(0) = B_n, B_n(1) = B_n, B_n′ = n·B_{n−1}).
* **Honest constant: 2, not Backlund's 1.** The elementary derivation gives the classical bound
  shape with C_{2m+2}/|B_{2m+2}| ≈ 2 where Backlund's sharper argument gives 1. The sharper
  constant needs the alternating-remainder comparison, which is NOT reproduced here — so it is
  NOT used. Cost: at most one extra Bernoulli pair of accuracy; rigor: everything on the page.
* **Argument increments without derivatives:** FORMAT.md D1–D3 + the branch derivations in
  `ball.py` (four half-plane branch formulas, each derived) + the branch-difference argument in
  the `producer_mp.py` docstring (two continuous argument branches along one path differ by a
  constant 2πn, so Δ_k = θ_tag(f(end)) − θ_tag(f(start))). No ζ′, no f′, anywhere.
* **Exact emission:** iv endpoints are binary rationals converted losslessly to `Fraction`
  (`ball.mpf_tuple_to_fraction`); scaling by K and A and floor/ceil are exact integer
  arithmetic. No float touches any number written into a transcript.

## 3. The trust surface, stated plainly

The single trusted-by-the-leg ingredient is **mpmath 1.3.0's interval core**
(`libmp.libmpi`: +, −, ×, /, **2, sqrt, exp, log, cos, sin, atan, pi). This is platform trust,
exactly parallel to the Arb leg's trust in Arb, and it is why the two-producer rule exists
(FORMAT.md §10; m2a-m2b-design §4: disagreement beyond stated radii is a stop-the-line event).

**Corrected 2026-09-02 (AUDIT F finding F-1, re-verified at reconciliation — `AUDIT.md`).** The
Session-8 wording "directed-rounding interval core" overstated the platform: the ring primitives
(+, −, ×, /, **2, sqrt) are correctly directed-rounded, but `mpf_exp`/`mpf_log`/`mpf_atan`/`mpf_pi`
directed-round a guard-bit *approximation* (`libelefun.py`), so a ceiling can land below the truth
(demonstrated: 11 of 40 000 `mpf_exp` ceilings at prec 288, ~6.6·10⁻⁹¹ relative; `recon_rounding.log`).
`ball.py` now widens every transcendental endpoint outward by 2⁻⁽ᵖʳᵉᶜ⁻¹⁶⁾ relative (`_inflate`,
mpmath's own `mpi_cos_sin` recipe with a 2¹⁵-ulp margin), so the platform assumption actually
relied on is the weak one: each transcendental endpoint lies within relative distance 2⁻²⁷² of the
truth. The emitted acceptance transcripts are unchanged by the repair (numeric content byte-identical,
`recon_mp_reproduce*.log`).
Mitigation shipped here: every primitive and composite is containment-tested against mpmath's
independent float pipeline at reference precision ABOVE the interval precision (400 vs 288
bits), with membership decided in exact rational arithmetic — `validation-ball.txt`,
`validation-zeta.txt`, `validation-hurwitz.txt`, `validation-dh-crosscheck.txt`.

Everything else — the EM identity, the remainder bound, the constants, the branch formulas, the
rounding — is derived in-file or certified by exact computation as itemized in §2.

## 4. Produced transcripts and checker record (all rerunnable)

| file | function/mode | rect | segments | winding enclosure S/A | result |
|---|---|---|---|---|---|
| `w1-zeta-exclusion-t10.json` | zeta/exclusion | [3/5, 7/10] × [10, 11] | 44 | [−23, 21]·10⁻¹² | m = 0 certified; floor \|ζ\| ≥ 1.234 |
| `w1-zeta-exclusion-t100.json` | zeta/exclusion | [3/5, 9/10] × [100, 101] | 52 | [−24, 28]·10⁻¹² | m = 0 certified; floor \|ζ\| ≥ 0.3556 |
| `w1-dh-refutation-live-fire.json` | f_DH/refutation | [31/40, 17/20] × [171/2, 429/5] | 57 | [0.999999999973, 1.000000000030] | **m = 1 certified — the live-fire test FIRES** (4.6 s wall) |

The DH transcript is the D1 direction file's acceptance test (ii): the pipeline produces an
ACCEPTED refutation transcript around ρ_DH = 0.808517182456637 + 85.699348485377592i. Per D-R8
this is a checker-level true-positive firing test with the fixed f_DH trust label in the file —
NOT a Lean-backed conclusion, NOT "RH-for-DH machine-checked disproof". The two ζ exclusions are
acceptance test (i) (null tests, M3 prototype entries; D-R6 ledger language applies: "no zeros
of ζ in the box", never "RH verified in W").

Checker evidence: `checker-ref-run.txt` — `checker_ref.py` (this leg, Fraction) and
`reference_checker.py` (format author, integer cross-multiplication) both ACCEPT all five
transcripts in the directory with digit-identical winding sums, and each rejects all six
FORMAT §11 negative controls at exactly the intended checks. Producer honest-abort paths
(wrong-mode refusal; zero-on-boundary mesh-admissibility stop with the move-the-rectangle
message) exercised live in `producer-negative-controls.txt`.

Scales: K = 10³⁰, A = 10¹² (defaults; CLI-adjustable). Precision: iv 288 bits. EM parameters:
m = 14, N = max(20, ⌈0.5·(t_max + 29)⌉) — parameters tune width only and are never
load-bearing (the identity and bound hold for every N, m ≥ 1 in the strip).

Rerun commands (from this directory; Python 3.9, mpmath 1.3.0):

    python3 ball.py --selftest
    python3 zeta_encl.py --validate
    python3 hurwitz_encl.py --validate
    python3 producer_mp.py --selftest-dh
    python3 producer_mp.py --function zeta --mode exclusion --rect 3/5 7/10 10 11 --out /tmp/t10.json
    python3 producer_mp.py --function f_DH --mode refutation --rect 31/40 17/20 171/2 429/5 --out /tmp/dh.json
    python3 checker_ref.py w1-*.json
    python3 checker_ref.py --controls w1-example-refutation.json

## 5. Design notes and deviations recorded

* **Shape layer vs C10:** `w1-schema.json`'s allOf ties mode "exclusion" to claimed_m "0";
  both reference checkers deliberately leave that tie to the semantic check C10 on translated
  literals (the Lean checker has no mode field — the theorem splits on m), so the FORMAT §11
  control "mode exclusion with m = 1" fails at C10 as specified. Documented in `checker_ref.py`.
* **C6 must survive integer rounding:** a ball-level sign witness thinner than 1/K dies under
  outward rounding; the producer treats integer-level C6 as the acceptance criterion and keeps
  bisecting until it holds (never bumping K silently).
* **Endpoint tightening:** argument rows use thin endpoint enclosures INTERSECTED with the
  whole-segment box (both enclose the same value; intersection sound, and its nonemptiness is a
  producer-bug tripwire that stops the line).
* **Two checkers, one contract:** `checker_ref.py` was written from FORMAT.md alone and shares
  no code with either the producer or `reference_checker.py`; agreement on five accepts and six
  intended rejections is the two-implementation reading check of the contract.

## 6. Cut lines (what is NOT in this leg, honestly)

1. **The Arb/FLINT leg** (the other D-R3 producer) — separate work item, not started here.
   Until it runs, the two-producer redundancy for these specific transcripts is one-legged:
   the cross-checks above are against mpmath's own float pipeline, not an independent library.
2. **The Lean kernel checker** (`checkW1`/`cert_of_checkW1`) — the Lean stream's item; the
   FORMAT.md §7.1 sketch plus these reference checkers are its executable spec.
3. **Acceptance test (iii), the certified cost curve** (cost vs depth δ and height T) — not
   commissioned in this task's four components; the three produced transcripts give first
   calibration points (0.5 s / 0.9 s / 4.6 s wall) but no curve.
4. **Backlund constant 1** — cut as documented in §2; constant 2 shipped instead, derived.
5. **Near-zero boxes / deep-refutation stress:** the D3 clamp and the C8 budget were never
   stressed (winding widths came out ~5×10⁻¹¹ turns); a Lehmer-pair-class target would be the
   real stress test.
6. **No parallelism** in the producer (single process, well under the 4-process thermal cap);
   per-edge multiprocessing is an easy later win if M3-scale runs need it.
7. **`iv.gamma` is never used** (mpmath's interval gamma has known-fragile corners); nothing
   here needs it. The only libmpi primitives consumed are the ones listed in §3.

## 7. File inventory added by this leg

| file | role |
|---|---|
| `ball.py` | complex ball layer (+ selftest) |
| `zeta_encl.py` | ζ enclosures, EM derivation, certified constants (+ validation) |
| `hurwitz_encl.py` | ζ(s, a) enclosures (+ validation incl. a = 1 cross-check) |
| `producer_mp.py` | W1 transcript producer (+ f_DH implementation + DH cross-validation) |
| `checker_ref.py` | independent Fraction-based reference checker (+ negative controls) |
| `w1-zeta-exclusion-t10.json`, `w1-zeta-exclusion-t100.json` | produced exclusion transcripts (real data) |
| `w1-dh-refutation-live-fire.json` | produced DH refutation transcript (live-fire, m = 1) |
| `validation-ball.txt`, `validation-zeta.txt`, `validation-hurwitz.txt`, `validation-dh-crosscheck.txt` | validation run transcripts |
| `checker-ref-run.txt` | two-checker cross-validation record |
| `producer-negative-controls.txt` | honest-abort paths, live |
| `mp-leg-notes.md` | this file |
