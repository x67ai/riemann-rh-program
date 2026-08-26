# M2a/M2b split design note — the formal Λ-bracket milestone, restructured per D-R2

**Date:** 2026-08-26 (Session 7 queue item; drafted by the D1 formalization-architect agent).
**Mandate:** D1 direction file, mandatory repair **D-R2** (Phase-4 cycle wf_11e60b6b-3a1, convergent 6.5/7/7): split M2 into M2a (statement + checker, Polymath15 bridge displayed) and M2b (bridge discharge, horizon, not scheduled); decide the "0 ≤ Λ" question; delete the wrong sub-0.2 cost model; onboard the Gomila claim as prior-art item and first claim-screening customer.
**Status effect:** this note IS the D-R2 repair for the design layer. M2 was frozen until D-R2 landed; with this note on disk, **M2a is unfrozen for scheduling after M1 v1** (funding still a separate decision). M2b remains explicitly NOT scheduled.
**Verification discipline:** every load-bearing quote below was re-verified this session against the on-disk PDFs (`fetched/p3-22a4` = Polymath15 arXiv:1904.12438v2; `fetched/p3-22a1` = Platt–Trudgian, RH to 3·10¹²) via pdftotext extraction; extraction scratch copies in the session scratchpad. What could NOT be verified (network: arxiv.org, github.com, judegomila.com unreachable today; google.com/GCS reachable) is flagged inline per D-R10.

---

## 0. The corrected target pairing (D-R1, re-verified from source)

The machine-checked instance targets **Λ ≤ 0.2** via the Platt–Trudgian pairing, NOT the old "0.22 at 3·10¹²" mismatch. The verified chain, from the PDFs:

* **Polymath15 Theorem 1.2** (Upper bound criterion; p3-22a4, verified verbatim this session): if t₀, X > 0 and 0 < y₀ ≤ 1 satisfy
  * **(i)** no zeros ζ(σ + iT) = 0 with (1+y₀)/2 ≤ σ ≤ 1 and 0 ≤ T ≤ X/2 (numerical verification of RH at initial time 0);
  * **(ii)** no zeros H_{t₀}(x + iy) = 0 with x ≥ X + √(1−y₀²) and y₀ ≤ y ≤ √(1−2t₀) (asymptotic zero-free region at final time t₀);
  * **(iii)** no zeros H_t(x + iy) = 0 in the barrier region at X for 0 ≤ t ≤ t₀ (in practice the simpler region X ≤ x ≤ X+1, y₀ ≤ y ≤ 1, 0 ≤ t ≤ t₀ — stated in the paper immediately after the theorem);

  **then Λ ≤ t₀ + ½y₀².**
* **Table 1 row 2** (p3-22a4, "Conditional Λ Results", verified): X = 5·10¹² + 194858, t₀ = 0.186, y₀ = 0.16733, winding number 0, |f_t| lower bound 0.0376 ⟹ Λ ≤ 0.20. Arithmetic re-checked exactly: 0.16733² = 0.0279993289, so t₀ + ½y₀² = 0.19999966445 ≤ 0.2. ✓
* **Height conversion** (verified from p3-22a4 eq. (1): H₀(z) = ⅛·ξ(½ + iz/2), so ζ-height T ↔ x = 2T): row 2 consumes RH verified to X/2 = 2,500,000,097,429 ≈ 2.5000001·10¹².
* **Platt–Trudgian §3.4** (p3-22a1, verified verbatim): "The second row in Table 1 on page 65 of [24] shows that one may take Λ ≤ 0.2 provided one has shown H > 2.51·10¹². This leads to the following. **Corollary 2. We have Λ ≤ 0.2.**" PT's Theorem 1 verifies RH to height 3,000,175,332,800 ("3·10¹²"), which covers 2.51·10¹² with margin. (PT's 2.51·10¹² is a conservative round-up of the 2.50·10¹² conversion; we cite PT's published figure, not our re-derivation.)
* Also verified from p3-22a1 §3.4: "The next entry in Table 1 of [24] is conditional on taking H a little higher than 10¹³ … This would enable one to prove Λ < 0.19," and PT's own remark that "some extra decimals could be wrought out" of the existing calculation at H = 3·10¹². Both quotes are load-bearing below (cost model, Gomila screen).

Standing bracket of record: **0 ≤ Λ ≤ 0.2** (Rodgers–Tao lower half + PT Corollary 2 upper half). The STRICT "Λ < 0.2" remains unproven and is never written.

---

## 1. M2a — the Lean statement + checker, bridge displayed (months-scale; schedulable after M1 v1)

### 1.1 What M2a is

A machine-checked theorem of the shape "**modulo three displayed hypotheses, every H_t with t ≥ 0.2 has only real zeros**" — i.e., Λ ≤ 0.2 in ray form — where the kernel-checked content is a pure-integer certificate check on the barrier/asymptotic transcripts (the `NumericCert` discipline: `decide +kernel`, no `native_decide`), and the three displayed hypotheses are exactly the three trust boundaries, displayed in the statement rather than hidden in prose. This is the same trust model the repo already ships for the PairCeiling ceiling theorems (sole hypothesis `EnclOK`; `full-map.md`: "machine-checked modulo one finite interval-arithmetic computation") — extended from one displayed computation to two displayed computations plus one displayed ANALYTIC implication. The honest label, fixed here and to be used verbatim in any publication:

> kernel-checked modulo three displayed hypotheses: (H1) a producer-certified zero verification, (H2) producer-certified H_t enclosures, (H3) the Polymath15 upper-bound criterion (Theorem 1.2) as an analytic hypothesis — with two independent producers for (H2).

### 1.2 Why the conclusion is stated in ray form (no `Λ` constant in the statement)

Defining Λ itself in Lean (`sInf {t | H_t has only real zeros}`) drags in junk-value pitfalls (Mathlib's `sInf` on sets not known nonempty/bounded-below) and forces de Bruijn monotonicity + Hurwitz closure into the TRUSTED layer just to make the definition meaningful. The ray statement

  ∀ t ≥ 0.2, ∀ z, H t z = 0 → z.im = 0

is literally equivalent to Λ ≤ 0.2 given the ray structure {t : H_t real-zeroed} = [Λ, ∞) (the same structure the Phase-4 cycle re-derived twice), says exactly what a skeptical reader wants, and keeps the trusted definition surface to ONE object: H_t. Publications state "this is the assertion Λ ≤ 0.2" in prose with the classical references; the formal statement never mentions Λ.

Anti-cheat note (a feature, record it in the file header when written): H_t is defined by a Bochner integral; if the integrand were not integrable the definition would collapse to the junk value 0 everywhere, making EVERY z a zero and the conclusion FALSE, not vacuous. The statement cannot be satisfied by a degenerate definition — integrability is forced into the solution side, where it belongs.

### 1.3 Proposed Lean statement skeleton (Lean 4 pseudocode, repo style)

New directory `Zeta23/DBN/` (de Bruijn–Newman), trusted-layer definitions mirrored into `comparator/` per the ChallengeDeps pattern (statement definable from Mathlib alone — H_t is not in Mathlib, so the trusted layer defines it in ~30 lines from `MeasureTheory.integral` and `tsum`; those 30 lines are part of the audit surface, exactly like `ChallengeDeps.lean` §1).

```lean
/- Zeta23/DBN/Defs.lean — trusted definition layer (mirrored in comparator/ChallengeDeps) -/
noncomputable section
namespace Zeta23
namespace DBN

/-- Φ(u) = Σ_{n≥1} (2π²n⁴e^{9u} − 3πn²e^{5u})·exp(−πn²e^{4u})  (the heat-kernel density;
    Polymath15 eq. (2), = the density with H₀(z) = ⅛·ξ(½ + iz/2)). -/
def Phi (u : ℝ) : ℝ :=
  ∑' n : ℕ+, (2 * π ^ 2 * (n : ℝ) ^ 4 * exp (9 * u) - 3 * π * (n : ℝ) ^ 2 * exp (5 * u))
    * exp (-π * (n : ℝ) ^ 2 * exp (4 * u))

/-- H_t(z) = ∫₀^∞ e^{tu²} Φ(u) cos(zu) du  (Bochner integral; junk value 0 if not integrable —
    see the anti-cheat note: junk makes the target statement false, not vacuous). -/
def Ht (t : ℝ) (z : ℂ) : ℂ :=
  ∫ u in Set.Ioi (0 : ℝ), Complex.exp (t * u ^ 2) * (Phi u : ℂ) * Complex.cos (z * u)

/-- (H1) Producer-certified zero verification to ζ-height T₀, in the exact shape Theorem 1.2(i)
    consumes: no zeros with real part in [σ₀, 1] up to height T₀.  Displayed hypothesis;
    discharged in prose by Platt–Trudgian Theorem 1 (σ₀ = (1+y₀)/2, T₀ = X/2 ≤ 3·10¹²). -/
def ZeroVerification (σ₀ T₀ : ℝ) : Prop :=
  ∀ s : ℂ, riemannZeta s = 0 → σ₀ ≤ s.re → s.re ≤ 1 → 0 ≤ s.im → s.im ≤ T₀ → False

/-- (H2) The enclosure hypothesis for the barrier + asymptotic transcripts: the true values of
    Re/Im of the normalized evaluator f_t at the transcript's mesh points lie in the recorded
    integer enclosures at scale K.  EnclOK pattern, verbatim from PairCeiling/NumericCert. -/
def BarrierEnclOK (d : BarrierCertData) : Prop := …   -- EnclOK K (mesh values of f_t) encl

/-- (H3) THE DISPLAYED ANALYTIC HYPOTHESIS: Polymath15 Theorem 1.2, quantified over the
    parameters.  This Prop is stated, named, and NOT proved in M2a; discharging it is M2b. -/
def Polymath15Bridge : Prop :=
  ∀ t₀ X y₀ : ℝ, 0 < t₀ → 0 < X → 0 < y₀ → y₀ ≤ 1 →
    ZeroVerification ((1 + y₀) / 2) (X / 2) →
    (∀ x y : ℝ, X ≤ x → y₀ ≤ y → y ≤ 1 → ∀ t, 0 ≤ t → t ≤ t₀ →
        Ht t (x + y * Complex.I) ≠ 0) →           -- barrier + asymptotic canopy, merged form
    ∀ t, t₀ + y₀ ^ 2 / 2 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0

end DBN
end Zeta23
```

```lean
/- Zeta23/DBN/Instance02.lean — the instance (solution side) -/

/-- Row-2 certificate data (X = 5·10¹² + 194858, t₀ = 0.186, y₀ = 16733/100000):
    integer-enclosure transcripts for f_{t} on the barrier mesh (t-slices × boundary mesh)
    and the finite asymptotic-region check, plus rational targets.  Format: §4. -/
def row2 : BarrierCertData := …    -- literal data, produced outside Lean (Arb + mpmath)

theorem row2_check : checkBarrier row2 = true := by decide +kernel

/-- **Λ ≤ 0.2, ray form** — kernel-checked modulo the three displayed hypotheses. -/
theorem lambda_le_point2
    (hH1 : ZeroVerification (58367 / 100000) (2.51e12))     -- PT Thm 1: verified to 3·10¹²
    (hH2 : BarrierEnclOK row2)
    (hH3 : Polymath15Bridge) :
    ∀ t : ℝ, (0.2 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  -- kernel: row2_check + cert_of_check (soundness of the integer checker, proved in Lean)
  -- glue:   t₀ + y₀²/2 = 0.19999966445 ≤ 0.2 ≤ t  (exact rational arithmetic, norm_num)
  …
```

Design points, fixed now:

1. **The checker is M1's checker with m = 0.** Hypothesis (iii)'s content — no zeros of H_t in the barrier box — is certified by exactly the W1 argument-principle transcript format with target winding number 0 (an exclusion certificate), run at a finite mesh of t-slices with a Lipschitz-in-t enclosure row making the t-interpolation rigorous (the producer records an enclosure of sup |∂_t f_t| over the slab; the checker verifies slice-spacing × that bound < each slice's boundary-modulus floor, all in integer cross-multiplication). Hypothesis (ii)'s content is certified the same way on the finite rectangle [X + √(1−y₀²), X_far] plus ONE analytic tail row (the Theorem-1.5-type zero-free tail for x ≥ X_far), which in M2a is folded into H3's statement (the merged "canopy" form above) so that no unstated analytic step exists outside a displayed hypothesis. This reuse is why M2a is sequenced after M1: the checker soundness theorem `cert_of_check` is written ONCE (M1 v1) and instantiated twice.
2. **H1 is a Prop about `riemannZeta`, not a transcript.** Re-certifying PT's 3·10¹² computation is out of scope (it was a supercomputer run); H1 enters as a displayed producer-certified hypothesis with PT Theorem 1 as the named discharge, exactly parallel to how EnclOK enclosures cite an external computation. The statement uses the WEAK form Theorem 1.2(i) actually needs (zero-freeness only for Re s ≥ (1+y₀)/2 = 0.583665), so any future partial verification weaker than full RH-to-height could also discharge it.
3. **Comparator packaging.** `comparator/` gets a third config (`config-dbn.json`); the challenge statement is `lambda_le_point2` with the trusted layer = Mathlib + the ~30-line `Defs.lean` mirror. Audit surface stays ~100 lines.
4. **Numeric literals** are exact rationals (`16733/100000`, `58367/100000` — note (1+y₀)/2 = 0.583665 rounds DOWN to a valid σ₀ since ZeroVerification is monotone in σ₀; the instance uses the safe direction). No floating literals anywhere in the trusted layer.

### 1.4 Decision: drop "0 ≤ Λ" from the machine-checked claim — YES

**Decision: the machine-checked claim is the upper half only.** Rationale, per D-R2's demand that this be decided and justified:

* The lower half carries **zero load in D1's refutation logic**: the witness formats certify Λ > t₀ directly (W1/W3/W4), never via Rodgers–Tao; the bracket's lower end is context, not machinery.
* The ray-form statement (§1.2) does not even mention Λ, so "0 ≤ Λ" is not a droppable conjunct of the formal statement — it was only ever a prose companion. Prose keeps the full bracket 0 ≤ Λ ≤ 0.2 with citations (Rodgers–Tao Forum Math. Pi 8 (2020), e6, 62 pp.; PT Cor. 2).
* **Rodgers–Tao formalization, priced separately as demanded:** RT is a 62-page hard-analysis paper (heat-flow dynamics of zero ensembles, a variational argument over zero configurations, pair-correlation-type inputs) with no existing Mathlib infrastructure beyond what M2b would build for H_t. Rough price: **research-scale, order 2–5 person-years** — comparable to the whole existing Zeta23 development, and larger than M2b's own bridge discharge (RT needs everything M2b needs PLUS the variational/dynamical core). No D1 milestone consumes it; if the program ever wants a fully formal two-sided bracket, it is a separate sponsor-tier project ("M2c", explicitly unowned and unscheduled). This pricing is an estimate by analogy (Zeta23 itself; the public record of comparable analytic formalizations), not a verified quote — flagged as judgment-grade.

### 1.5 Corrected cost model for sub-0.2 pushes (D-R2 deletion executed here)

The old M2 text's cost model — "a Λ ≤ 0.15-class push = new rigorous verification height ≫ 3·10¹² + barrier rerun" — is **deleted and replaced** by the verified two-lane picture:

* **Lane A (same height, new row):** the existing H = 3·10¹² verification is NOT exhausted. PT themselves: "our value of H falls between the entries in this table; it is possible that some extra decimals could be wrought out" (p3-22a1 §3.4, verified). A fresh (t₀, y₀, X) row with X/2 ≤ 3·10¹² is barrier-computation-only — local-compute-priceable, no new verification. The Gomila claim (§3), if it screens pass, is exactly a Lane-A row and would hand M2a a second instantiation target Λ ≤ 0.1787854 for the SAME checker at zero marginal Lean cost.
* **Lane B (new height):** the next published Polymath15 TABLE row, Λ < 0.19, needs H > 10¹³ (p3-22a1 §3.4, verified; the published table row 3 = 2·10¹³ + 131252 in x-coordinates, arXiv table verified consistent). Λ ≤ 0.15-class via the EXISTING table needs H ≈ 10¹⁴–10¹⁵ (arXiv Table 1 rows: Λ = 0.161 at X = 3·10¹⁴, Λ = 0.153 at X = 2·10¹⁵) — outside the local-compute policy, individually sponsor-approved if ever proposed.
* Lane A's headroom is bounded: with X/2 ≤ 3·10¹² fixed, the achievable t₀ + ½y₀² is limited by how small the barrier/asymptotic computations can push (t₀, y₀) at that X — Polymath15's own optimizer landed at 0.19999966 for X = 5·10¹²; a large Lane-A improvement (e.g., the claimed 0.1787854) implies either materially better numerics or an error. That is precisely what the §3 screen decides; M2a itself makes no Lane-A promise.

### 1.6 M2a work breakdown

| # | Item | Depends on | Est. cost | Trust tier |
|---|------|-----------|-----------|------------|
| a | `Zeta23/DBN/Defs.lean` (trusted layer: Φ, Ht, ZeroVerification, Polymath15Bridge) | toolchain lands | 1–2 weeks | trusted (~30 dense lines + docstrings) |
| b | `BarrierCert.lean` format + `checkBarrier` + `cert_of_check` soundness | M1 v1 checker (reuse) | 2–3 weeks | Lean-proved |
| c | Arb-side f_t producer (Polymath15 Thm 1.3 effective A+B+C evaluator on top of Arb) | Polymath15 dbn code fetch (github — unreachable today) | 3–4 weeks | untrusted producer |
| d | mpmath-ball f_t producer (independent leg; shares D-R3's priced mpmath ball core with M1) | D-R3 item | +2 weeks over the M1 core | untrusted producer |
| e | `Instance02.lean` (row-2 data literal + `decide +kernel` run + glue arithmetic) | b, c, d | 1 week | kernel-checked |
| f | comparator config + `PrintAxioms` audit + README trust-model paragraph | a–e | 1 week | packaging |

Months-scale total, consistent with the direction file; runs after M1 v1 because (b) is a reuse and because M1's two-producer plumbing is the same plumbing.

---

## 2. M2b — the bridge discharge (horizon; NOT scheduled)

M2b = prove `Polymath15Bridge` in Lean, removing H3. Honest scale assessment of what that takes, decomposed against the actual proof in p3-22a4:

1. **H_t analytic foundations** (integrability, entirety, H₀ = ⅛ξ(½ + iz/2), order-1 growth, functional symmetry): builds on Mathlib's ξ/Γ layer + `Zeta23/GammaFacts`; the first genuinely new heat-flow analysis in Lean. Weeks–months.
2. **de Bruijn's Theorem 3.2** (the "canopy" theorem: no zeros with y₀ ≤ |Im z| ≤ 1 at time t₀ ⟹ Λ ≤ t₀ + ½y₀²) plus Polymath15 Proposition 3.3 and the zero-dynamics/continuity argument of their §3 (zeros move continuously, cannot enter the protected region). This is classical-but-real complex analysis: Hurwitz-type arguments, local zero counting, ODE-flavored continuity of zero sets. The repo's `WeilEF/` contour machinery (`Contour.lean`, `ZeroSumLimit.lean`) is the right seam but was built for ξ′/ξ zero sums, not zero dynamics. Months.
3. **Theorem 1.3, the effective Riemann–Siegel approximation** H_t/B_t = f_t + O_≤(e_A + e_B + e_{C,0}) with EXPLICIT error terms (verified present in p3-22a4 as displayed formulas): this is the research-scale core — an explicit-constant stationary-phase/saddle analysis, every constant auditable. It is also the piece with the largest reuse payoff: it is exactly the certified H_t evaluator that M5's Λ-conversion loop and B4's diffusive-scale program want (a Tier-2 verified evaluator would even retire H2's producer trust). Many months, plausibly the dominant cost.
4. **Theorem 1.5-type asymptotic zero-free region** (zeros of H_t with x ≥ exp(C/t) are real and "solidified") — needed to close the canopy at x → ∞ unless the H3 statement keeps a finite-X_far tail row certified numerically forever (a legitimate design dial: M2b can discharge the bridge with a WEAKER, finitely-checkable tail hypothesis retained, shrinking the analytic debt without eliminating it). Months.

**Total honest estimate: 1–3 person-years of formalization by someone fluent in both the repo and explicit-constant analytic number theory — research-scale, not bookkeeping** (the Phase-4 killer's phrase, adopted). Decision points that would change the estimate: Mathlib growth in explicit-constant asymptotics; whether the finite-tail dial (item 4) is taken. **M2b is named, bounded, and NOT scheduled** — it enters the queue only by explicit sponsor decision, and nothing in D1's refutation chain waits on it (the witness formats never consume the bridge).

---

## 3. The Gomila item — prior art + first claim-screening customer

**The claim:** Jude Gomila, 2026, unrefereed: **Λ ≤ 0.1787854** (judegomila.com; reportedly Polymath15 Theorems 1.2/1.3 re-run at a new parameter row consuming the existing 3·10¹² verification — i.e., a Lane-A row per §1.5). Status: snippet-verified only; the page was unreachable in the Phase-4 cycle and both it and github.com are unreachable today (D-R10). **NOT a record.** The bracket of record remains 0 ≤ Λ ≤ 0.2 unless and until the screen below returns screen-pass AND the result acquires refereed or kernel-checked standing.

**(a) As prior-art item:** logged in the M2 lineage as the first known third-party attempt at a Lane-A improvement. Consequences regardless of screen outcome: (i) it confirms same-height barrier space is considered non-exhausted by practitioners; (ii) it is a live test that D1's claim-screening service has a market of exactly the predicted shape (computer-assisted, unrefereed, no certificate discipline).

**(b) The screening protocol (designed NOW, executed when the network returns):**

*Required disclosures (what the claim's repo must expose to be evaluable):*
1. The exact parameter tuple (t₀, y₀, X) with the arithmetic claim t₀ + ½y₀² ≤ 0.1787854, as exact rationals.
2. The consumed verification height and source: X/2 ≤ 3,000,175,332,800 with citation to PT Theorem 1 (anything larger ⟹ the claim is conditional and cannot be screened as an unconditional bound).
3. Barrier transcripts: mesh, t-slices, enclosures (value + radius, any format convertible to (lo, hi) integer pairs at a scale K) for f_t on the barrier boundary, plus the winding-number-0 computation per slice and the t-interpolation bound (§1.3 point 1).
4. Asymptotic-region evidence: the Theorem 1.3/1.5 instantiation with explicit constants for x beyond the barrier — a checkable finite computation plus a citable analytic tail, with the split point stated.
5. Software identity: versions, rerun scripts, and the evaluator's provenance (fork of the Polymath15 dbn code vs reimplementation).

*What the D1 checker verifies (in order; stop at first failure):*
1. Arithmetic: the tuple's t₀ + ½y₀² and the height conversion X/2, exact rational cross-multiplication.
2. Coverage: hypothesis (i)'s (σ, T) region ⊆ PT Theorem 1's verified region.
3. Format conversion: transcripts → `BarrierCertData`; run `checkBarrier` (kernel or its verified-extraction equivalent) — enclosures exclude 0, winding 0, interpolation rows close.
4. Two-producer spot check: re-produce ≥ a fixed sample (e.g., 1% of mesh cells, plus every cell with margin below 2× median) with BOTH Arb and mpmath-ball producers; agreement within stated radii required.
5. Sensitivity: confirm the claimed bound has nonzero margin (a tuple with t₀ + ½y₀² = 0.1787854 exactly and zero slack in any enclosure is a red flag, reported as such).

*Outcome taxonomy (ledger vocabulary, fixed now):*
* **screen-pass** — all disclosures present, checker accepts, spot-check agrees. Consequence: the claim becomes M2a's natural second instantiation target (same theorem shape, new `row` literal; near-zero marginal Lean cost); D1 publishes the accepted transcript; the claim STILL is not "the record" until refereed/kernel-checked standing exists — screen-pass is a statement about certificates, not a promotion authority.
* **screen-fail** — disclosures present but a checker step fails or producers disagree beyond radii. Consequence: a documented, reproducible failure report to the ledger (and to the claimant); the specific failing cell/step published. Screen-fail is a statement about the exposed certificates, not a disproof of the claimed bound.
* **non-evaluable** — required disclosures absent, environment unreproducible, or the claim consumes an unverified height. Recorded as unscreened; re-openable on new disclosure. (Given the snippet-grade information today, the PRIOR expectation is non-evaluable-at-first-contact; the protocol's first execution step when github.com returns is simply an inventory of disclosures 1–5.)

This is the claim-screening service's v1 protocol generally: for Λ-bound claims, items 1–5 as above; for off-line-zero claims, the same skeleton with the B2 poster screen prepended and W1 as the checker.

---

## 4. Target arithmetic — enclosure formats, checker consumption, two-producer status

* **One enclosure convention, program-wide:** integer pairs (lo, hi) : ℤ × ℤ at a declared scale K (meaning lo ≤ K·x ≤ hi), lists ordered by a declared indexing — the `EnclOK` pattern of `PairCeiling/NumericCert.lean` (def at line 72) verbatim. All targets are exact rationals given as numerator/denominator pairs; ALL comparisons by integer cross-multiplication; no division, no floats, anywhere in checked code. Complex quantities as two enclosures (Re, Im); modulus-excludes-0 checked as lo_Re² + lo-side bounds via integer squares (the exact scheme to be fixed in `BarrierCert.lean`, following the M1 v1 checker).
* **Checker consumption (M2a):** `BarrierCertData` = { parameters (t₀, y₀, X as rationals), t-slice list, boundary mesh per slice, Re/Im enclosure lists per slice at scale K, per-slice modulus floor targets, the ∂_t-Lipschitz enclosure row, and the asymptotic-rectangle block in the same format }. Soundness theorem: `checkBarrier d = true → BarrierEnclOK d → (canopy nonvanishing Prop consumed by Polymath15Bridge)`. This is RowCert's `checkRows/cert_of_checkRows` architecture (RowCert.lean lines 24/52/134) transplanted.
* **Two-producer rule (binding, per D-R3):** every transcript is produced independently by (1) **Arb/FLINT** — the off-the-shelf leg for ζ (`acb_dirichlet`, verified live in the Phase-4 cycle) but NOT for f_t: the effective A+B+C evaluator of Polymath15 Thm 1.3 must be built on top of Arb (the Polymath15 dbn repository is the reference implementation — github.com unreachable today; fetch at execution, D-R10) — and (2) **mpmath ball arithmetic** — priced by D-R3 as a named work item, weeks not pip-install (complex ball ops + rigorous tails), shared with M1. **Pricing status today: the D-R3 mpmath item is priced (weeks) but not started; the f_t layer on BOTH legs is an M2a-specific increment (~3–4 weeks Arb-side, ~2 weeks mpmath-side on top of the M1 core) that D-R3 did not cover — this note is the pricing record for it.** Producers are untrusted by design; disagreement beyond stated radii is a stop-the-line event.

---

## 5. Milestone table and the first Lean file

| Milestone | Scale | Frozen until | Unfrozen by | First action |
|---|---|---|---|---|
| M2a — statement + checker, three displayed hypotheses; instance Λ ≤ 0.2 (ray form) via PT pairing | months (≈ 8–11 weeks of items a–f, after M1 v1) | D-R2 | **this note** (schedulable; funding decision separate; sequenced after M1 v1 for checker reuse) | write `Zeta23/DBN/Defs.lean` when the toolchain lands |
| M2a′ — second instance at the Gomila row | days–weeks | Gomila screen-pass | §3 protocol execution (needs network) | inventory of disclosures 1–5 on the claim's repo |
| M2b — bridge discharge (H3 proved; items §2.1–2.4) | 1–3 person-years, research-scale | — (not frozen; simply NOT scheduled) | explicit sponsor decision only | none (design dial: finite-tail variant, §2.4) |
| M2c — Rodgers–Tao formalization (two-sided formal bracket) | 2–5 person-years | — (unowned, unscheduled; named here per D-R2's "price it separately") | sponsor-tier decision only | none |
| Claim-screening service v1 | protocol done (this note); execution days per claim | network (github.com, judegomila.com) | network return | Gomila disclosure inventory |

**The first concrete Lean file: `Zeta23/DBN/Defs.lean`.** Import sketch (repo conventions: copyright header, module docstring stating the trust model, `noncomputable section`, `namespace Zeta23.DBN`):

```lean
import Mathlib.Analysis.SpecialFunctions.Complex.Circle   -- Complex.exp/cos toolchain
import Mathlib.Analysis.SpecialFunctions.Gamma.Basic       -- ξ-side cross-checks (docstrings)
import Mathlib.MeasureTheory.Integral.Bochner              -- the Ht integral
import Mathlib.Topology.Algebra.InfiniteSum.Basic          -- Φ as a tsum
import Mathlib.NumberTheory.LSeries.RiemannZeta            -- riemannZeta for ZeroVerification
```

Contents: `Phi`, `Ht`, `ZeroVerification`, `Polymath15Bridge` (§1.3), nothing else — the file is trusted-layer-thin on purpose; `BarrierCert.lean` (checker, imports `Zeta23.PairCeiling.NumericCert` for the EnclOK vocabulary or re-declares the two-line pattern locally to keep DBN import-light), `Instance02.lean`, and the comparator mirror follow in that order. No compilation this session (toolchain not built); the skeleton above is design-grade pseudocode consistent with `NumericCert.lean`/`RowCert.lean`/`ChallengeDeps.lean` style, to be type-checked at M2a kickoff.

---

## 6. Verification ledger for this note (standing order 5)

**Verified this session, from disk:** Polymath15 Thm 1.1 (Λ ≤ 0.22), Thm 1.2 full statement incl. all three hypotheses + conclusion Λ ≤ t₀ + ½y₀², the simplified barrier region, eq. (1) H₀(z) = ⅛ξ(½+iz/2), Thm 1.3's A+B+C shape, Thm 1.5's existence and role, Table 1 rows (incl. row 2's exact tuple and rows for §1.5 Lane B), the "Λ ≤ O(1/log T)" heuristic section (p3-22a4); PT §3.4 in full — the 2.51·10¹² pairing sentence, Corollary 2, the "higher than 10¹³ … Λ < 0.19" sentence, the "extra decimals" sentence, Theorem 1's exact height 3,000,175,332,800, and the Rodgers–Tao reference data "Forum of Math., Pi, 8(e6), 62pp." (p3-22a1). Row-2 arithmetic recomputed exactly. EnclOK/RowCert/NumericCert/ChallengeDeps patterns read from the Lean repo files directly.
**Not verifiable today (network; D-R10):** the Gomila page and repo (claim remains snippet-grade); the Polymath15 dbn GitHub code (referenced as producer seed, not load-bearing); Mathlib current-state claims are inherited from the Phase-4 cycle's verification (no argument principle), not re-checked today.
**Judgment-grade (flagged):** the person-year estimates in §1.4, §2 (analogy-based); the M2a week-counts in §1.6; the claim that (ii)+(iii) merge cleanly into the single canopy Prop of `Polymath15Bridge` (faithful to Thm 1.2's proof sketch as read, but the exact Prop boundary is to be settled when `Defs.lean` is type-checked).
