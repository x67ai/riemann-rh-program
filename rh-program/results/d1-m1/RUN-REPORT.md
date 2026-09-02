# RUN-REPORT — what D1 M1 v1 now is (after the reconciled audit of 2026-09-02)

**Companion to** `AUDIT.md` (the binding per-finding record). **Trust vocabulary (D-R3/D-R8,
binding):** producers are untrusted by design; the Lean side is "kernel-checked modulo the two
displayed hypotheses H-ENCL and H-AP"; the f_DH results are "checker-level only"; nothing here is
"fully machine-checked". The Λ bracket of record is 0 ≤ Λ ≤ 0.2 (Rodgers–Tao; Platt–Trudgian
Cor. 2); the strict "Λ < 0.2" is never written.

## 0. The one-paragraph statement

M1 v1 is the Certified Refutation Interface, v1, of the D1 direction file (FIRST DELIVERABLE):
a fixed transcript contract (`FORMAT.md` v1.0, unchanged in substance by the audit), a Lean 4
integer checker with a proved soundness theorem, two independent untrusted producers, and an
acceptance suite that both producers pass and that all three checkers — two Python, one Lean
kernel — accept. **After the audit it is repaired-clean: 0 FATAL, four MAJOR findings all
re-verified and repaired, no defect open against the format, the checker or the theorem.** What
it certifies, stated exactly: for an accepted ζ transcript with claimed winding m ≥ 1, *if* the
producers' enclosures are true (H-ENCL) *and* the rectangle argument principle holds for ζ on
the strip (H-AP), *then* ζ has a zero ρ with ½ < Re ρ < 1 inside the rectangle — ¬RH; for
m = 0, under the same two hypotheses, ζ has no zero in the closed rectangle. The kernel checks
the integer part; the two hypotheses are displayed, not hidden. The mp-leg producer's platform
premise was found false at the ulp level and has been repaired to a weak, tested assumption; the
transcripts it emitted were provably unaffected and have been re-emitted byte-identically. An
RH counterexample found by anyone, anywhere, still converts into a kernel-checked disproof
*modulo H-ENCL and H-AP* by filling in one transcript; "fully kernel-checked" waits for v1.1.

## 1. The components, as they now stand

### 1.1 The Lean layer (trusted checker; the ~100-line audit surface)

Files (`rh-program/lean/Zeta23/W1/`, byte-identical in the working tree
`~/rh-lean-work/zeta-23-lean-main`): `Format.lean` (data types), `Checker.lean` (`checkW1`,
`checkW1Floor`: C1–C10 and C11 in pure ℤ arithmetic), `Soundness.lean` (1 257 lines, the
hypotheses and the theorem), `Examples.lean` (the artificial §11 micro-examples), and — new at
the audit — `Instances.lean` (the ten acceptance transcripts and both positive controls as
kernel-checked checker instances). Toolchain Lean `v4.33.0-rc2`, Mathlib `51e6992e` (the
manifest; the "123d1576" in two earlier texts is wrong — `AUDIT.md` §1, last row).

The theorem, verbatim (`Soundness.lean` 928–932):

```lean
theorem cert_of_checkW1 (d : W1Data) (hc : checkW1 d = true)
    (hEncl : W1EnclOK riemannZeta d) (hAP : RectArgPrinciple riemannZeta) :
    (1 ≤ d.m → ∃ ρ : ℂ, riemannZeta ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1
        ∧ T1 d < ρ.im ∧ ρ.im < T2 d)
    ∧ (d.m = 0 → ∀ s ∈ W1Rect d, riemannZeta s ≠ 0)
```

and the floor by-product, generic in f (`Soundness.lean` 1208–1210):

```lean
theorem floor_of_checkW1Floor {f : ℂ → ℂ} (d : W1Data) (fl : W1Floor)
    (hc : checkW1Floor d fl = true) (hEncl : W1EnclOK f d) :
    ∀ s ∈ W1Bdry d, (fl.Fn : ℝ) / fl.Fd ≤ ‖f s‖
```

`#print axioms` on both: `propext, Classical.choice, Quot.sound` only (both auditors, and the
recorded builds: `Zeta23.W1.Soundness` 3 142/3 143 jobs, `Zeta23.W1.Instances` 656 jobs).
No `sorry`, no `admit`, no `native_decide`, no `ofReduceBool`. H-ENCL is the indexed
per-segment enclosure hypothesis of FORMAT §8.1 (value boxes for all t ∈ [0, 1] on each segment,
argument rows as the imaginary part of the log-derivative integral). H-AP is the rectangle
argument principle in **consequence form** (∃ Z : ℕ with the four-edge identity
2πZ = Σ argIncrement; Z = 0 ⟹ no zeros in R°; 1 ≤ Z ⟹ a zero in R°) under "f differentiable on
an open U ⊇ R and f ≠ 0 on ∂R" — a true statement for ζ, weaker than FORMAT §8.2, so the theorem
assumes strictly less. Consequences recorded by the audit: the Lean conclusion is the
existential form (one zero, not "m zeros with multiplicity" — FORMAT §6.3 v1-scope note);
`checkW1` has no mode clause (the split is at the theorem); C11 lives in `checkW1Floor`; and
the checker cannot see K, A, or the row↔segment alignment (FORMAT §8.1, "What the checker cannot
see") — those falsify H-ENCL, never the checker.

**Kernel evidence on real data (new).** `Instances.lean`: `checkW1Floor … = true` by
`decide +kernel` for all ten acceptance transcripts (27 to 1 294 rows, K = 10³⁰, A = 10⁶/10¹²),
`checkW1 … = false` for both positive controls; axioms `[propext]` / none; literal fidelity
proved by an independent back-parse (12 instances, 2 940 rows, 0 mismatches). Beyond the
deliverable, the two audits kernel-rejected 30 + 8 hand-corrupted transcripts and ran an
800 + 379-case Lean-vs-Python differential fuzz with full agreement. Build note: literals of
more than a few hundred rows need `set_option maxRecDepth 100000` (the definition compiler's
limit on the list literal, written by the emitter — not a kernel limit; `checkW1` on 1 294 rows
kernel-evaluates in seconds at the default once the data is imported).

### 1.2 The producers (untrusted; two independent legs)

* **Arb leg** (`producer_arb.py`, python-flint 0.6.0 / Arb balls): unchanged by the audit. Exact
  dyadic ball→interval conversion with the library's directed bounds as a redundant bracket;
  outward integer rounding; rotated-`atan2` argument rows with the sign-split outward division
  (re-derived by both auditors); A even enforced by construction.
* **mpmath-ball leg** (`ball.py`, `zeta_encl.py`, `hurwitz_encl.py`, `producer_mp.py`; mpmath
  1.3.0 `iv`): **repaired.** (i) The platform premise "every endpoint is correctly
  directed-rounded" was false for the transcendental primitives (F-1: `mpf_exp` ceilings below
  the truth in 11 of 40 000 samples at prec 288); every transcendental endpoint is now widened
  outward by 2⁻⁽ᵖʳᵉᶜ⁻¹⁶⁾ relative (`_inflate`), and the assumption actually relied on is stated
  in the file: each such endpoint lies within relative distance 2⁻²⁷² of the truth — tested
  against prec-1200 references (0 violations in 92 000 exact comparisons) and cross-checked by
  the Arb leg, never proved. (ii) The D3 clamp is an integer clamp, sound only for even A; the
  producer now refuses odd A (F-2: with A = 1 it once emitted a checker-accepted false exclusion
  transcript). The Euler–Maclaurin enclosure of ζ and ζ(s, a) — identity, remainder bound
  (RB) = C_{2m+2}|s+2m+1|/(σ+2m+1) × first omitted term, the certified C_{2m+2} — was re-derived
  independently by both auditors and matches the code line by line (F's direct test: true
  remainder ≤ 0.467 × the pad at 120 points). Self-tests after the repairs: 18 469 / 0 (ball),
  100/100 (ζ), 60/60 (Hurwitz), 24/24 (DH cross-validation). Every mp acceptance transcript was
  re-produced after the repairs with numeric content byte-identical to Session 8's
  (`recon_mp_reproduce.log`; t = 10⁴ in `recon_mp_reproduce_t10000.log`).
* **Independence:** no shared module in either direction (verified by both auditors from the
  import lists); different mathematics (hand-derived Euler–Maclaurin with certified constants
  vs Arb's own `acb.zeta`; half-plane branch endpoint differences vs rotated-`atan2` balls);
  κ = tan θ computed separately on each leg and agreeing with the Gauss-sum value to 10⁻⁶¹ and
  10⁻¹⁴¹. The two-producer cross-check (`acceptance/crosscheck.py`) is the only detector of the
  checker's by-design blind spots; it is mandatory, not optional.

### 1.3 The checkers (three)

`reference_checker.py` (format author's; now prints the function's own trust label on ACCEPT)
and `checker_ref.py` (independently written, Fraction-based) — both UNTRUSTED executable specs;
and the Lean kernel via `emit_lean.py` → `decide +kernel`. All three agree on every acceptance
transcript, every positive control, and every corruption either audit tried.

### 1.4 The acceptance suite after the repairs (all rerunnable; `recon_checker_pass.log`)

| transcript | leg | rows | claimed m | winding enclosure (turns) | certified floor \|f\| ≥ | Python ×2 | Lean kernel |
|---|---|---|---|---|---|---|---|
| null [3/5, 9/10]×[100, 101] | mp / arb | 52 / 27 | 0 | [−24, 28]·10⁻¹² / [−14, 13]·10⁻⁶ | 0.35555 / 0.08328 | ACCEPT | `checkW1Floor = true` |
| null [3/5, 9/10]×[1000, 1001] | mp / arb | 81 / 65 | 0 | [−41, 40]·10⁻¹² / [−29, 36]·10⁻⁶ | 0.015573 / 0.013827 | ACCEPT | true |
| null [3/5, 9/10]×[10000, 10001] | mp / arb | 1294 / 983 | 0 | [−679, 637]·10⁻¹² / [−495, 488]·10⁻⁶ | 8.13·10⁻⁵ / 7.64·10⁻⁶ | ACCEPT | true |
| null [21/40, 39/40]×[100, 101] | mp / arb | 58 / 30 | 0 | [−28, 30]·10⁻¹² / [−16, 14]·10⁻⁶ | 0.35550 / 0.03052 | ACCEPT | true |
| DH live fire [4/5, 41/50]×[85.69, 85.71], f_DH | mp / arb | 40 / 50 | 1 | [999999999980, 1000000000020]·10⁻¹² / [999973, 1000023]·10⁻⁶ | 2.467·10⁻⁴ / 3.019·10⁻⁴ | ACCEPT (checker-level, D-R8) | true (no theorem about f_DH) |
| positive control [2/5, 3/5]×[14, 14.3] (straddles ρ₁; C2 violated by design) | mp / arb | 77 / 183 | 1 | machinery sees m = 1 | — | REJECT at C2 | `checkW1 = false` |

Cross-check: 83 / 158 / 2 547 / 90 / 122 / 295 overlap pairs, all CONSISTENT (re-run by both
auditors). The DH winding was recomputed from scratch by both auditors (direct contour
integral, dense argument unwrapping, per-segment row containment): 1.0 turns to 61 digits,
every row containing its true value. Ledger sentences the four ζ boxes certify (D-R6): "no zeros
of ζ in [3/5, 9/10] × [T, T+1] for T ∈ {100, 1000, 10000}" (δ₀ = 1/10) and "in
[21/40, 39/40] × [100, 101]" (δ₀ = 1/40) — each "kernel-checked modulo H-ENCL and H-AP
(producers untrusted)", never "RH verified in W". The DH transcripts are a checker-level
true-positive firing test: the pipeline fires on the one known true positive in reach.

### 1.5 Cost curve (unchanged; `cost-curve.json`)

Checking is negligible (0.005–0.03 s per transcript in Python; seconds in the kernel); producing
dominates — the mp leg's Euler–Maclaurin term count N ≈ T/2 makes it 1 565 s at T = 10⁴ against
2.6 s for Arb. Winding-sum widths never stressed C8 (worst ~10⁻³ of budget); a Lehmer-pair-class
near-degenerate target is the untested stress case, carried forward.

## 2. What was wrong, and what changed (summary of `AUDIT.md`)

| finding | was | is |
|---|---|---|
| F-1 mp platform premise | "directed rounding" claimed for all primitives; false for exp/log/atan/pi at ~10⁻⁴ ulp | outward 2¹⁵-ulp inflation of every transcendental endpoint; the weak assumption stated and tested; transcripts unchanged |
| F-2 odd A | `producer_mp.py --A 0` emitted a false exclusion certificate the checkers accept | producer refuses odd A; FORMAT §1 requires A even (producer side; the checker was always sound) |
| O MAJOR-1 / F-6 Lean coverage | the Lean checker had never seen a producer transcript; "both checkers" = Python | `emit_lean.py` + `Instances.lean`: all 12 kernel-checked, literals back-parse-verified |
| O MAJOR-2 / F-3 recursion limit | ≥ ~900-row literals fail to build; cause disputed | cause settled (list literal, not the kernel); emitter writes the option; bulk-data packaging demanded for M2a |
| minors | one wrong ratio; f_DH banner; selftest regime gap; C10/C11/multiplicity/blind-spot wording | all corrected in place, dated |

## 3. What remains for v1.1 (D-R3): the argument principle in Lean

H-AP is v1's displayed analytic debt. It is stated in consequence form for f differentiable on an
open U ⊇ R with f ≠ 0 on ∂R, and the theorem applies it with U = {Re s < 1} (ζ is differentiable
there; integrability of the boundary integrand is *proved* on the soundness side from the
checker-certified nonvanishing). Discharging it means proving, for such f, that the four-edge
sum of argument increments is 2π times a natural number that is 0 iff f has no zeros in R° —
Mathlib 2025-26 ships no argument principle or residue theorem (verified in the Phase-4 cycle).
**Lead on disk:** `gomila-lean-branch-scout.md` — Gomila's `lean/certificate-and-argument-
principle` branch carries an Aristotle-generated `windingRect_eq_sum_analyticOrder` for ENTIRE
functions (Lean v4.28, Mathlib 8f9d9cff; MIT; no build record, no axioms output anywhere —
UNVERIFIED third-party work; an isolated verify build was launched by the orchestrator). If it
builds with standard axioms, v1.1 reduces to (a) generalizing entire → differentiable-on-U (or
using the entire surrogate (s−1)ζ(s) with a bookkeeping lemma) and (b) bridging its statement to
`RectArgPrinciple`'s four-edge form: estimated ½–1 session + 1–3 sessions. If it does not, v1.1
is the WeilEF/Contour route of D-R3: research-scale. Either way the multiplicity-counting form
("at least m zeros with multiplicity") is formalized with it (O MINOR-6). Nothing cites the
branch until its `#print axioms` output is on disk.

## 4. The f_t / H_t evaluator: status

**Not started on either leg.** Both legs evaluate ζ and f_DH only. What M2a must add is the
effective approximation of Polymath15 Theorem 1.3 (H_t/B_t = f_t + O_≤(e_A + e_B + e_{C,0}),
with the paper's explicit error terms; on disk as `fetched/p3-22a4-polymath15-2019-upper-bound-
debruijn-newman.pdf` and the published `p3-22a5`, verified present by the design note's ledger
§6 — the formulas are to be quoted from the PDF at exact page when implemented, never from
memory), as (c) an Arb-ball evaluator (~3–4 weeks) and (d) an mpmath-ball evaluator with a
DERIVED remainder for every truncation (~2 weeks on top of the M1 core), per
`m2a-m2b-design.md` §1.6/§4. What M1 supplies to it: the corrected ball layer (with its stated
platform assumption), the exact-rational→interval plumbing, the pattern of a derived,
certified remainder (`zeta_encl.py` STEPS 1–6), the mesh/argument-row machinery, the
cross-check tool, and the emitter. What it does not supply: any bound on f_t.

## 5. Gomila screen steps 3–4 (`results/d1-m0/gomila-screen.md` §4): what is cleared, what M2a must add

Both auditors reached the same conclusion independently; the reconciler concurs.

**Step 3 — format conversion + run `checkBarrier`: NOT CLEARED.** M1 v1 supplies the reusable
half: the enclosure convention (integer (lo, hi) at scale K, outward rounding, exact-rational
targets, cross-multiplication everywhere); the modulus-excludes-0 scheme (C6, Lean-proved
`row_box_excludes_zero`, scale-free); the winding-0 exclusion certificate a barrier t-slice IS
(`cert_of_checkW1`, m = 0 branch); the integer-squares floor the t-interpolation gate consumes
(`floor_of_checkW1Floor`, generic in f); a working, fidelity-checked JSON→Lean path
(`emit_lean.py`); and evidence that kernel checking scales to ~1 300 rows in seconds. **Missing:**
`BarrierCert.lean` — `BarrierCertData` (a general rectangle: W1's C2 hard-wires ½ < σ₁ ≤ σ₂ < 1,
so a barrier slice [X, X+1] × [y₀, 1] at X ≈ 6·10¹² cannot even be encoded; a t-slice list; the
Lipschitz-in-t row; per-slice floor consumption), `checkBarrier` reusing W1's C3–C9/C11
arithmetic, and a soundness theorem generic in f with H-AP restated for general rectangles
(design-note item (b), not started); the converter from the claim's sealed printed-decimal balls
to `BarrierCertData`; and — first — the bulk-data packaging decision (`AUDIT.md` D-1), because
the claim's finite lane is 3 149 013 rows and a single Lean list literal at that size is not
viable at any `maxRecDepth`.

**Step 4 — two-producer spot check: PARTIALLY CLEARED (architecture), NOT CLEARED (target).**
The architecture the step needs is built, validated end-to-end and re-run by both auditors: two
genuinely independent legs, whole-segment hull evaluation with adaptive bisection to C6, outward
integer conversion, derivative-free argument rows, honest stop-the-line aborts, a cell-wise
cross-check with reproduced overlap counts — and, since the audit, the mp leg is rigorous as
implemented under a stated assumption rather than a false one. **Missing:** the target function
on both legs (§4 above) — not one Gomila mesh cell is reproducible today.

**In order, M2a must add:** D-1 packaging decision → (c)/(d) the f_t evaluators on both legs →
(b) `BarrierCert.lean` + `checkBarrier` + soundness → the claim-format converter → `Instance02.lean`
glue (e) → comparator packaging (f). `Zeta23/DBN/Defs.lean` (a) is done and clean. Net: the screen
stays **screen-open**; the block is D1-side; the bracket of record stays 0 ≤ Λ ≤ 0.2.

## 6. Known limitations carried forward (honest list)

1. The mp leg trusts mpmath's transcendental primitives to 2⁻²⁷² relative — tested, cross-checked
   by Arb, not proved. The Arb leg trusts Arb. The two-producer rule is what makes either trust
   auditable at transcript level.
2. The checker cannot see K, A, or row↔segment alignment (FORMAT §8.1); only the cross-check can.
3. The Lean conclusion is existential (one zero), H-AP is displayed, and the f_DH results carry no
   theorem — v1.1 and "f_DH-in-Lean" are separate, unpriced/priced items (D-R3, D-R8).
4. The mp leg costs 26 min at T = 10⁴ (N ≈ T/2 Euler–Maclaurin terms); M3 heights need a
   Riemann–Siegel-class evaluator on that leg. Untested: Lehmer-pair-class C8 stress.
5. Audit scratch modules (`Zeta23/W1/AuditO*.lean`) remain in the working tree as evidence; they
   share identifiers with `Instances.lean` and must never be imported together.

## 7. Files at reconciliation

Changed: `ball.py`, `zeta_encl.py`, `hurwitz_encl.py`, `producer_mp.py`, `reference_checker.py`,
`mp-leg-notes.md`, `FORMAT.md`, `acceptance-report.md`, `lean/README.md`. New: `AUDIT.md` (this
report's companion), `RUN-REPORT.md`, `emit_lean.py`, `instances-doc.txt`,
`recon_instances_verify.py`, `recon_rounding.py`/`.log`, `recon_compare_transcripts.py`,
`recon_F2_before.log`, `recon_F2_after.log`, `recon_selftests_after.log`,
`recon_mp_reproduce.log`, `recon_mp_reproduce_t10000.log`, `recon_checker_pass.log`,
`recon_lean_instances.log`, `lean/Zeta23/W1/Instances.lean`. Untouched: `producer_arb.py`,
`checker_ref.py`, `w1-schema.json`, all `acceptance/*.json`, `Format/Checker/Soundness/Examples.lean`.
