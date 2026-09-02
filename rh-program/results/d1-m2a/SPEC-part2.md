
---

## 3. The Lean-facing statement: `Defs.lean` as elaborated, one defect, and the amended bridge

### 3.1 The elaborated shapes (Defs, lines 82–117; `#print`-verified per the design note §7)

    def Phi (u : ℝ) : ℝ := ∑' n : ℕ+, (2 * π ^ 2 * (n : ℝ) ^ 4 * exp (9 * u) - 3 * π * (n : ℝ) ^ 2 * exp (5 * u)) * exp (-π * (n : ℝ) ^ 2 * exp (4 * u))
    def Ht (t : ℝ) (z : ℂ) : ℂ := ∫ u in Set.Ioi (0 : ℝ), Complex.exp (t * u ^ 2) * (Phi u : ℂ) * Complex.cos (z * u)
    def ZeroVerification (σ₀ T₀ : ℝ) : Prop := ∀ s : ℂ, riemannZeta s = 0 → σ₀ ≤ s.re → s.re ≤ 1 → 0 ≤ s.im → s.im ≤ T₀ → False
    def Polymath15Bridge : Prop :=
      ∀ t₀ X y₀ : ℝ, 0 < t₀ → 0 < X → 0 < y₀ → y₀ ≤ 1 →
        ZeroVerification ((1 + y₀) / 2) (X / 2) →
        (∀ x y : ℝ, X ≤ x → y₀ ≤ y → y ≤ 1 → ∀ t : ℝ, 0 ≤ t → t ≤ t₀ → Ht t (x + y * Complex.I) ≠ 0) →
        ∀ t : ℝ, t₀ + y₀ ^ 2 / 2 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0

The contract fits `Phi`, `Ht`, `ZeroVerification` as they stand. It does NOT fit `Polymath15Bridge`
as it stands, for the reason in §3.2.

### 3.2 DEFECT (blocking for Instance02): the merged "canopy" hypothesis of `Polymath15Bridge` is not dischargeable by any finite certificate

The second hypothesis of `Polymath15Bridge` demands H_t(x + iy) ≠ 0 for ALL x ≥ X, y ∈ [y₀, 1] and
ALL t ∈ [0, t₀] — in particular at t = 0 for every x ≥ X. **Derivation D-3.2.** By P15 eq. (1) (p1),
H₀(z) = ⅛·ξ(½ + iz/2); with z = x + iy, ½ + iz/2 = (1 − y)/2 + ix/2. So H₀(x + iy) = 0 iff ξ(s) = 0 at
s = (1 − y)/2 + ix/2, i.e. iff ζ has a zero with Re s = (1 − y)/2 and Im s = x/2 — equivalently (by
ξ(s) = ξ(1 − s)) a zero with Re s = (1 + y)/2 at height x/2. Hence the t = 0 slice of the canopy
hypothesis for x ≥ X says: ζ has no zeros with (1 + y₀)/2 ≤ Re s ≤ 1 at ANY height ≥ X/2. For the
instance (X/2 ≈ 2.5·10¹²) that is the Riemann hypothesis in the strip Re s ≥ 0.583665 at all
heights above PT's 3 000 175 332 800 — unproved, and not the object of any finite computation
(at t = 0 the effective approximation does not stabilize: Theorem 1.5's solidification region
x ≥ exp(C/t) escapes to infinity as t → 0, P15 p9–11). ∎

The Prop is TRUE as a mathematical statement (its hypotheses are stronger than Theorem 1.2's, so
it is a weaker implication than the theorem), which is why it type-checked and why the design
note's §7 check ("the merged form elaborates as written") could not catch this: elaboration does
not test instantiability. The design note's own §1.3 point 1 intended (ii) "on the finite rectangle
plus one analytic tail row … at final time t₀"; the merge over "0 ≤ t ≤ t₀" over-strengthened it.
With the Prop as written, `lambda_le_point2` cannot be proved from any transcript plus H1 — the
instance theorem of design §1.3 is unprovable. The repair is one definition:

### 3.3 The amended bridge (type-checked, `lean-shapes-scratch.lean` §A; to replace `Polymath15Bridge` in `Defs.lean` v1.1 with a dated deviation record in the file header and in the design note §7)

    /-- (H3) Polymath15 Theorem 1.2 with hypothesis (ii) at the FINAL time only and the simplified
    barrier box for (iii) — the instantiable form (SPEC §3.2). -/
    def Polymath15Bridge' : Prop :=
      ∀ t₀ X y₀ : ℝ, 0 < t₀ → 0 < X → 0 < y₀ → y₀ ≤ 1 →
        ZeroVerification ((1 + y₀) / 2) (X / 2) →
        (∀ x y : ℝ, X + 1 ≤ x → y₀ ≤ y → y ^ 2 ≤ 1 - 2 * t₀ →
            Ht t₀ (x + y * I) ≠ 0) →                                            -- (ii′)
        (∀ x y : ℝ, X ≤ x → x ≤ X + 1 → y₀ ≤ y → y ≤ 1 → ∀ t : ℝ, 0 ≤ t → t ≤ t₀ →
            Ht t (x + y * I) ≠ 0) →                                             -- (iii′)
        ∀ t : ℝ, t₀ + y₀ ^ 2 / 2 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0

**Derivation D-H3 (`Polymath15Bridge'` is implied by Theorem 1.2, hence is a legitimate displayed
form of it).** Fix parameters with 0 < t₀, 0 < X, 0 < y₀ ≤ 1 and assume (i), (ii′), (iii′). Theorem
1.2's (ii): take x ≥ X + √(1 − y₀²) and y₀ ≤ y ≤ √(1 − 2t₀) (so y² ≤ 1 − 2t₀). If x ≥ X + 1, (ii′)
gives H_{t₀}(x + iy) ≠ 0. Otherwise X ≤ X + √(1 − y₀²) ≤ x ≤ X + 1 (as 0 ≤ √(1 − y₀²) ≤ 1), and
y ≤ √(1 − 2t₀) ≤ 1, so (iii′) at t = t₀ gives it. Theorem 1.2's (iii): its region has X ≤ x ≤
X + √(1 − y₀²) ≤ X + 1, y ≥ √(y₀² + 2(t₀ − t)) ≥ y₀ and y ≤ √(1 − 2t) ≤ 1, 0 ≤ t ≤ t₀ — inside
(iii′)'s box. So Theorem 1.2 applies and gives the conclusion. ∎ (When 1 − 2t₀ < y₀², (ii′) is
vacuous; Theorem 1.2 still applies with its (ii) region empty, exactly as in the paper.)

The name: the amended Prop REPLACES the merged one (do not keep both — a Prop that cannot be
instantiated must not remain in the trusted layer under the name "Theorem 1.2"). Everywhere below,
"H3" means `Polymath15Bridge'` in conjunction with `HtEntire` (§3.5).

### 3.4 The normalizer B_t in the trusted layer (Defs.lean v1.1; type-checked, scratch §A)

The barrier rows enclose the NORMALIZED function g_t := H_t/B_t (P15 p4: "renormalise the function
H_t(x+iy) by dividing it by a nowhere vanishing explicit function B_t(x+iy)"; |H_t| itself is
e^{−(π/8 + o(1))x} ≈ 10^{−10¹²} at the instance's X and cannot be scaled into integers). The
contract fixes B_t CONCRETELY in the trusted layer rather than existentially ("∃ B nonvanishing
holomorphic with rows enclosing H_t/B") — so that a reader of the ~40 trusted lines sees which
function the rows are about — transcribed from P15 (6), (9), (10), (11) (p4):

    def alpha (s : ℂ) : ℂ := 1 / (2 * s) + 1 / (s - 1) + (1 / 2 : ℂ) * Complex.log (s / (2 * π))
    def M0 (s : ℂ) : ℂ :=
      (1 / 8 : ℂ) * (s * (s - 1) / 2) * (π : ℂ) ^ (-s / 2) * (Real.sqrt (2 * π) : ℂ)
        * Complex.exp ((s / 2 - 1 / 2) * Complex.log (s / 2) - s / 2)
    def Mt (t : ℝ) (s : ℂ) : ℂ := Complex.exp ((t : ℂ) / 4 * alpha s ^ 2) * M0 s
    def Bt (t : ℝ) (z : ℂ) : ℂ := Mt t ((1 - I * z) / 2)

Transcription notes (audit surface): Mathlib's `Complex.log` is the principal branch with argument
in (−π, π] — P15's "Log"; `(π : ℂ) ^ (-s / 2)` is `Complex.cpow` with a positive real base, i.e.
exp((−s/2)·log π) with real log π — P15's π^{−s/2}; (1 − iz)/2 = (1 + y − ix)/2 for z = x + iy.
Two facts about `Bt` are PROVED in `BarrierCert.lean` (Lean obligation L-B3, §8.3), not displayed:
for t ∈ ℝ and z with Im z ≠ 0 … more precisely on an open neighborhood of any rectangle with y₁ > 0
and x₁ > 1: `Bt t` is differentiable and nonvanishing (s = (1 − iz)/2 has Im s = −x/2 ≠ 0, so s ∉
(−∞, 1], both logs are off the cut, exp ≠ 0, cpow of a positive base ≠ 0, s ≠ 0, s − 1 ≠ 0). If
that proof turned out costly it may be displayed instead (fallback recorded in §13.2); the
statement shapes do not change.

### 3.5 The entirety of H_t (Defs.lean v1.1; type-checked)

    def HtEntire : Prop := ∀ t : ℝ, Differentiable ℂ (Ht t)

The argument principle needs g_t holomorphic on a neighborhood of R; `Ht` is a Bochner integral
whose holomorphy (differentiation under the integral against the super-exponentially decaying Φ) is
M2b-class analysis (design note §2 item 1). It is therefore DISPLAYED, as the second component of
the analytic package H3 := `Polymath15Bridge' ∧ HtEntire`. It is not folded into H2: H2 is where
producers enter; H3 is where Polymath15's analysis enters.

### 3.6 H1 for the instance — exact, no rounding (correcting design note §1.3 point 4)

Theorem 1.2(i) at row 2 needs `ZeroVerification ((1 + y₀)/2) (X/2)` with y₀ = 16733/100000 and
X = 5 000 000 194 858: (1 + y₀)/2 = 116733/200000 = 0.583665 exactly and X/2 = 2 500 000 097 429
exactly (X is even). The design note wrote σ₀ = 58367/100000 and called it a round-DOWN; but
58367/100000 = 0.58367 > 0.583665 — it is a round-UP, and `ZeroVerification` is monotone the wrong
way for that (a larger σ₀ is a WEAKER hypothesis, which does not imply the one the bridge consumes).
The instance therefore states H1 exactly:

    hH1 : ZeroVerification (116733 / 200000) 2500000097429

discharged in prose by PT Theorem 1 (p2: RH true up to height 3 000 175 332 800), with margin
3 000 175 332 800 − 2 500 000 097 429 = 500 175 235 371 (exact, `row2_arith.log`). PT's own pairing
sentence uses the rounded "H > 2.51·10¹²" (p5); 2.51·10¹² − X/2 = 9 999 902 571 > 0, consistent.

### 3.7 The honest label (final wording for M2a)

> kernel-checked modulo the displayed hypotheses: (H1) a producer-certified zero verification —
> `ZeroVerification (116733/200000) 2500000097429`, discharged by Platt–Trudgian Theorem 1; (H2)
> producer-certified enclosures — the barrier prisms (H2-B), the final-time window rows (H2-A) and the
> tail (H-TAIL), from two independent producers; (H3) the Polymath15 analytic package — Theorem 1.2
> in the form `Polymath15Bridge'` and the entirety of H_t — as hypotheses.

Never "fully machine-checked". The count is three named hypotheses with H2 a conjunction of three
enclosure-type Props; publications may say "three displayed hypotheses" only with that gloss.

---

## 4. Lane B — the barrier: mechanism and soundness

### 4.1 Overview

Fix R = [x₁, x₂] × [y₁, y₂] (instance: [X, X+1] × [y₀, 1]) and 0 = τ₀ < τ₁ < … < τ_{J−1} < τ_J := t₀.
Prism j is R × [τ_j, τ_{j+1}]. For each prism the transcript carries:

1. the **seam transcript** at time τ_j: a W1 exclusion transcript (FORMAT.md §§2–6, verbatim) for the
   producer's holomorphic approximant f = f_{τ_j} of g_{τ_j} = H_{τ_j}/B_{τ_j} — mesh of ∂R, per-segment
   value boxes at scale K, per-segment argument rows at scale A (turn units), claimed winding 0;
2. the **floor** (Fn, Fd): |f| ≥ Fn/Fd on ∂R (FORMAT.md §5.2 integer-squares scheme, check C11);
3. the **approximation defect** E ∈ ℕ: |g_{τ_j}(z) − f(z)| ≤ E/K for all z ∈ ∂R;
4. the **displacement** D ∈ ℕ: |g_t(z) − g_{τ_j}(z)| ≤ D/K for all z ∈ ∂R and τ_j ≤ t ≤ τ_{j+1}.

The checker verifies W1's C1, C3–C9 (with m = 0), C11, the general-rectangle C2′, and the one new
gate **C-B12: (E + D)·Fd < Fn·K** (i.e. E/K + D/K < Fn/Fd), plus the seam chain C-B13. Items 1–2 are
the M1 v1 checker with m = 0, exactly as the design note §1.3 point 1 prescribes; items 3–4 are the
two integers that carry Theorem 1.3 and the time step.

### 4.2 The seam rows: what f is, and what H-ENCL says about it

f is P15's f_t of eq. (14) at t = τ_j with N = N₀ constant on R (P15 p6: "f_t(x + iy) is a
holomorphic function of x + iy in the region (5) as long as N is constant"). For the instance,
N = 630783 on all of [X, X+1] × [0, t₀] (`row2_arith.log`: √(x/4π + t/16) ∈ [630783.1427963,
630783.1427965] at the four corners; the producer re-verifies with directed rounding, requirement
P-4). The rows assert, for every segment k (FORMAT.md §8.1(a),(b) with f in place of ζ):
reLo_k ≤ K·Re f ≤ reHi_k, imLo_k ≤ K·Im f ≤ imHi_k on the whole closed segment, and
argLo_k ≤ A·(Δ_k/2π) ≤ argHi_k for the log-derivative increment Δ_k of f. In Lean this is
`W1.RowEnclOK f p.K p.A` row-by-row against `W1.segs (toW1 r p)` — the M1 definitions, unchanged.
f is NOT defined in Lean (defining it would move (14)–(19) into the trusted layer); H2-B says
"there exists f, holomorphic on an open U ⊇ R, such that …" (§8.1), and the producers' f_t is the
intended witness. M2b, which defines f_t to prove Theorem 1.3, replaces the existential by it.

### 4.3 The winding: a W1 exclusion certificate for f

C8/C9 with m = 0 pin the winding number of f around ∂R to 0 (FORMAT.md D4); C6 gives f ≠ 0 on ∂R
(D1); the general-rectangle argument principle (`RectArgPrincipleGen`, §8.3 L-B0 — the proof of
`rectArgPrinciple_of_local` already discards the strip bounds, which appear as `_hhalf _hs2` in its
`intro`) then gives f ≠ 0 on R° and hence on R. The strip constraints of W1's C2 (½ < σ₁ ≤ σ₂ < 1)
are ζ-specific (they keep the pole out) and are REPLACED by C2′: x₁ < x₂, y₁ < y₂ (nondegenerate)
and y₁ > 0 (Theorem 1.2 needs y₀ > 0; B_t nonvanishing uses Im s ≠ 0).

### 4.4 The approximation defect E (Theorem 1.3 enters here, and only here)

E/K must bound e_A + e_B + e_{C,0} at t = τ_j uniformly on ∂R, from (71)–(72) + Proposition
6.6(iv)–(v) for e_A + e_B and the 10.50 form (D-2.4) for e_{C,0}; every factor bounded in its
conservative direction over the box (x ∈ [x₁, x₂], y ∈ [y₁, y₂]) — requirement P-6. The paper's own
budget for X₀ ≈ 6·10¹⁰ is 1.25·10⁻³ (Proposition 8.1, p39–42); the instance's indicative values
(`row2_errbudget_indicative.log`, heuristic floats, NOT a certificate): e_{C,0} ≤ 4.12·10⁻⁴ at
(X, y₀, t = 0) — the worst corner (smallest y, t = 0) — falling to 1.0·10⁻⁷ at t = t₀; e_A + e_B ≲
3·10⁻¹⁰. **The t = 0 endpoint.** Theorem 1.3 is stated on region (5), which has t > 0. The seam
τ₀ = 0 needs it at t = 0. Gomila's `BARRIER_CERTIFICATE.md` argues it by a limit t_j ↓ 0 (dominated
convergence for H_t, continuity of B_t, f_t and of the majorant on the compact box). This contract
does NOT rely on that argument in the checker; it is part of what H2-B asserts at the first seam,
and the producers must either (a) record the limit argument as their discharge of E at τ₀ = 0, or
(b) place the first seam at a small positive τ₀ > 0 and cover [0, τ₀] by … no: (b) is impossible,
the prism chain must start at 0 (C-B13) because Theorem 1.2(iii) starts at t = 0. Option (a) it is;
the SPEC records the limit argument as a producer obligation (P-7) and flags it for M2b (§13.3).

### 4.5 The displacement D (the time step)

D/K must bound sup{|g_t(z) − g_{τ_j}(z)| : z ∈ ∂R, τ_j ≤ t ≤ τ_{j+1}}. The producers obtain it as
D_t·(τ_{j+1} − τ_j) + (defect terms) from P15's (91) reasoning with Lemma 8.4's |∂f_t/∂t| majorant
(p46), UNIFORMIZED over the prism (pointwise Lemma 8.4 values at one corner are not box bounds —
Gomila's `DERIVATIVE_BOX_LEMMA.md` documents exactly this pitfall and its repair; requirement P-8),
and with the two defects E(τ_j) and E(t) added when the displacement is routed through f: |g_t −
g_{τ_j}| ≤ |g_t − f_t| + |f_t − f_{τ_j}| + |f_{τ_j} − g_{τ_j}| ≤ E_t + D_t·Δt + E_{τ_j}. (A producer
may instead bound |∂_t g_t| directly if it has an evaluator for it; the contract does not care how
D was obtained — only that the displayed clause holds.) **Why a displacement, not a Lipschitz
constant:** a row "sup |∂_t g_t| ≤ L" would make the trusted statement assert t-differentiability of
H_t/B_t (differentiation of the Bochner integral in t — M2b-class); the displacement clause is a
plain inequality between values of `Ht`, checkable by the producers' own arithmetic and stated with
no derivative. The design note's "slice-spacing × that bound < floor" is the same check with the
multiplication moved to the producer (recorded deviation, §4.7(i)).

### 4.6 Soundness of Lane B (the derivation the Lean theorem `cert_of_checkBarrier` formalizes)

Notation: G : ℝ → ℂ → ℂ the normalized family (instance: G t z = Ht t z / Bt t z), g_t := G t; U
an open set containing R on which the seam's f is holomorphic (H2-B); U_t an open set containing R
on which g_t is holomorphic (`hHol`, from H3's `HtEntire` + L-B3 for the instance). Fix prism
[τ, τ′] and t ∈ [τ, τ′].

* **D-B1 (seam exclusion for f).** C-B0..C-B9 (m = 0) with the row enclosures give: f ≠ 0 on ∂R
  (FORMAT D1); the four-edge increment sum of f is 2π·Z_f with Z_f ∈ ℕ (argument principle for f on
  U) and A·Z_f ∈ [S_lo, S_hi] ∋ A·0 with width < A/2 (FORMAT D4), so Z_f = 0; the Z = 0 clause of the
  argument principle gives f ≠ 0 on R°. Hence f ≠ 0 on R.
* **D-B2 (floor).** C-B11 + rows ⟹ |f| ≥ Fn/Fd on ∂R (FORMAT D6; Lean `floor_of_checkW1Floor`,
  already generic in f).
* **D-B3 (boundary perturbation).** For z ∈ ∂R: |g_t(z) − f(z)| ≤ |g_t(z) − g_τ(z)| + |g_τ(z) − f(z)|
  ≤ (D + E)/K < Fn/Fd ≤ |f(z)| by the two H2-B clauses and C-B12 ((E + D)·Fd < Fn·K, cross-
  multiplied with K, Fd ≥ 1). So g_t(z) ≠ 0, and h(z) := g_t(z)/f(z) satisfies |h(z) − 1| < 1,
  hence Re h(z) > 0 — h(∂R) lies in the open right half-plane.
* **D-B4 (holomorphy of h near R).** V := U ∩ U_t ∩ {z ∈ U : f z ≠ 0} is open (f continuous on U),
  contains R (D-B1), and h = g_t/f is holomorphic on V.
* **D-B5 (log-derivative additivity).** On each mesh segment γ ⊂ ∂R, f and h are holomorphic and
  nonvanishing near γ and g_t = h·f, so g_t′/g_t = h′/h + f′/f there, and (linearity of the interval
  integral, integrability from continuity on the compact segment) argIncrement(g_t, γ) =
  argIncrement(h, γ) + argIncrement(f, γ).
* **D-B6 (the half-plane lemma — the one new analytic lemma).** If h is holomorphic near the segment
  γ : [0,1] → ℂ from z to w and Re h > 0 on γ, then ∫₀¹ (h′/h)(γ(s))·γ′(s) ds = Log h(w) − Log h(z)
  for the principal Log: Log ∘ h ∘ γ is differentiable on [0,1] with derivative (h′/h)(γ)·γ′ (chain
  rule; `Complex.log` has derivative 1/w on the slit plane, and the right half-plane lies in it), so
  the fundamental theorem of calculus for the interval integral of a derivative applies. Taking
  imaginary parts: argIncrement(h, γ) = Arg h(w) − Arg h(z), Arg = `Complex.arg`.
* **D-B7 (telescoping).** Summing D-B6 over the segments of the closed counterclockwise traversal
  (FORMAT §4: each segment's end is the next segment's start, and the last segment ends at the first
  segment's start): Σ_γ argIncrement(h, γ) = 0 exactly.
* **D-B8 (conclusion).** Apply the argument principle to g_t on V (D-B3: g_t ≠ 0 on ∂R; D-B4):
  ∃ Z ∈ ℕ, 2πZ = Σ_edges argIncrement(g_t) = Σ_γ argIncrement(g_t, γ) (W1 L1 sub-segment
  additivity) = Σ_γ argIncrement(h, γ) + Σ_γ argIncrement(f, γ) (D-B5) = 0 + 2π·Z_f = 0 (D-B7,
  D-B1). So Z = 0 and g_t ≠ 0 on R°; with D-B3, g_t ≠ 0 on R. ∎
* **D-B9 (coverage in t).** C-B13 (0 = τ₀ < … < τ_{J−1} < t₀) with W1's `cover_chain` lemma: every
  t ∈ [0, t₀] lies in some [τ_j, τ_{j+1}].

For the instance, G t z = Ht t z / Bt t z, and `Bt t z ≠ 0` on R (L-B3) turns g_t ≠ 0 into Ht t z ≠ 0.
No Rouché theorem, no homotopy invariance and no zero-continuity in t is used: D-B6/D-B7 reduce the
time step to the same fixed-t argument principle W1 already has, applied twice (to f and to g_t),
plus one FTC-on-a-segment lemma.

### 4.7 Deviations from the design note, and the road not taken

1. **Displacement row D instead of a Lipschitz row.** Reason in §4.5. The checker's gate is the
   design note's inequality with the product formed producer-side.
2. **The rows enclose f, with Theorem 1.3's defect as a separate integer E.** Reason: the argument
   principle needs a holomorphic function whose winding the rows pin, and the two trusts — the
   producers' arithmetic (rows) and Polymath15's Theorem 1.3 (E) — are kept visibly apart.
3. **The road not taken — rows uniform in t (prism-uniform boxes and argument rows, no D).** It
   would remove the time step from the soundness theorem entirely (argument principle at every
   fixed t against t-uniform rows). It fails quantitatively: C8 needs the SUM of the argument-row
   widths below ½ turn; a t-uniform endpoint box has half-width ≈ D_t·Δt, which on Gomila's first
   prism is 1.89 against a modulus of 4.28 (`barrier_target_closed.log`, prism 1: time = 1.8885,
   min_mesh = 4.2784) — ≈ ±0.07 turn of argument uncertainty per segment; with ≈ 3.8·10⁴ segments
   per seam the sum width would be ≈ 5·10³ turns. Shrinking Δt by 10⁴ restores C8 at the price of
   ≈ 10⁷ prisms × 10⁴ rows = 10¹¹ rows. The seam-plus-displacement design keeps the argument rows
   sharp (endpoint enclosures at the exact seam) and pays one integer per prism for the time step —
   P15's (91) with the mesh term absorbed into the whole-segment hull boxes.
4. **B_t concrete** (§3.4) rather than "∃ B". 5. **`HtEntire` in H3**, not H2 (§3.5).
6. **General-rectangle C2′** replaces W1's strip C2 (§4.3); W1's own files are not modified.
