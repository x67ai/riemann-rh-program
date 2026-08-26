# W1 rectangle-transcript format — the M1 v1 producer/checker contract

**Status:** v1.0, 2026-08-26 (Session 8, D1 M1 first work item).
**This file is the contract.** The Lean stream building the M1 v1 checker (`Zeta23/…` in
`anthropic/zeta-23-lean-main`) reads THIS file as the normative specification of the transcript
data, the checker's integer checks, and the two displayed hypotheses; the untrusted producers
(Arb/FLINT leg, mpmath-ball leg) write files conforming to `w1-schema.json` in this directory.
Any change to the checks or the hypotheses is a version bump of both files, recorded here.

**Trust language (binding, per the D1 direction file, Risks item 2):** every public statement
about an accepted transcript reads "kernel-checked modulo the displayed hypotheses" — never
"fully machine-checked". Producers are UNTRUSTED by design; their output enters the trusted
statement only through the displayed hypothesis H-ENCL (§8).

**Mandate and sources (exact locations):**

* D1 direction file, FIRST DELIVERABLE + repair D-R3 + frontier entry:
  `anthropic/rh-program/directions/D1-certified-refutation-arm.md` (lines 72–80, 138, 154–156).
  D-R3 fixes the two-displayed-hypotheses rescope adopted here (Mathlib 2025-26 ships no
  argument principle; the rectangle argument principle is hypothesis H-AP in v1, discharged by
  the named milestone v1.1).
* Enclosure conventions (BINDING): `anthropic/rh-program/results/d1-m0/m2a-m2b-design.md` §4 —
  "integer pairs (lo, hi) : ℤ × ℤ at a declared scale K (meaning lo ≤ K·x ≤ hi), lists ordered
  by a declared indexing … All targets are exact rationals given as numerator/denominator
  pairs; ALL comparisons by integer cross-multiplication; no division, no floats, anywhere in
  checked code." That section left one item open — "modulus-excludes-0 checked as … the exact
  scheme to be fixed in `BarrierCert.lean`, following the M1 v1 checker" — **this file fixes
  that scheme** (§5, checks C6/C11).
* Lean architecture template: `anthropic/zeta-23-lean-main/Zeta23/PairCeiling/NumericCert.lean`
  (`EnclOK` at line 72, `check` at line 124, `cert_of_check` at line 253) and
  `RowCert.lean` (`RowCertData` line 24, `checkRows` line 52, `cert_of_checkRows` line 134).
  The W1 checker mirrors the `checkRows`/`cert_of_checkRows` split exactly: a Bool-valued pure
  integer function on literal data, evaluated by `decide +kernel` (no `native_decide`), plus a
  soundness theorem turning `check = true` and the displayed hypotheses into the analytic
  conclusion.

---

## 0. What a W1 transcript certifies

A W1 transcript describes a closed rectangle in the critical strip,

  R = [σ₁, σ₂] × [T₁, T₂] ⊂ ℂ,  s = σ + iT,  ½ < σ₁ ≤ σ₂ < 1,  T₁ < T₂,

a mesh of its positively-oriented boundary ∂R, per-segment integer enclosures of the boundary
values of the target function f (Re/Im boxes at scale K), per-segment integer enclosures of the
argument increments (at scale A, in turn units), and a claimed winding number m ≥ 0.

The checker (§7) verifies a fixed finite list of **integer comparisons** on this data. If it
accepts, then — modulo the two displayed hypotheses H-ENCL and H-AP of §8 —

* **mode `refutation` (m ≥ 1):** f has at least m zeros, counted with multiplicity, in the open
  rectangle R°; in particular a zero ρ with Re ρ > σ₁ > ½. For f = ζ this is ¬RH (derivation
  D5, §6.3).
* **mode `exclusion` (m = 0):** f has no zeros in the **closed** rectangle R (interior by the
  winding count, boundary by the nonvanishing rows). This is the M3/null-test form. Ledger
  language per repair D-R6: an exclusion entry claims "no zeros of ζ in
  [σ₁,σ₂]×[T₁,T₂]" — equivalently "no zeros with Re s ≥ ½ + δ₀ in the window", δ₀ = σ₁ − ½,
  recorded with the entry — and **never** "RH verified in W".

The pole of ζ at s = 1 lies outside R because Re 1 = 1 > σ₂ (checker C2); ζ is analytic on a
neighborhood of R, so the argument principle counts zeros only (derivation D8). The identical
format carries the Davenport–Heilbronn live-fire variant (§9.2, checker-level only per D-R8).

---

## 1. Number encoding (applies to every field)

* **Integers** are decimal strings matching `^-?(0|[1-9][0-9]*)$` (arbitrary precision; JSON
  native numbers are FORBIDDEN for checked data — IEEE-754 readers silently corrupt integers
  beyond 2⁵³, and enclosure scales are 10³⁰-class in production).
* **Rationals** are objects `{"n": "<integer string>", "d": "<positive integer string>"}`
  meaning n/d. Denominators are syntactically positive (schema pattern `^[1-9][0-9]*$`); the
  checker re-verifies d ≥ 1 on the translated literals (C1). Fractions need NOT be reduced;
  all comparisons are by cross-multiplication, which never divides (derivation D7).
* **Scales.** `K ≥ 1` (value scale): a value box row `(reLo, reHi, imLo, imHi)` for a segment γ
  asserts reLo ≤ K·Re f(s) ≤ reHi and imLo ≤ K·Im f(s) ≤ imHi **for every s on the closed
  segment** — the m2a-m2b-design §4 convention, one box per complex quantity as two (lo, hi)
  pairs. `A ≥ 1` (argument scale, turn units): an argument row `(argLo, argHi)` asserts
  argLo ≤ A·(Δγ/2π) ≤ argHi, where Δγ is the argument increment along γ (§6.1). K and A are
  independent; producers choose them.
* **No floats, no division, no transcendental constants anywhere in checked data or checks.**
  π and 2π never appear in the transcript: argument rows are in TURN units (the increment
  divided by 2π), so the winding number is pinned by pure integer containment (C8/C9).

---

## 2. Transcript fields (top level)

| field | type | meaning |
|---|---|---|
| `format` | const `"W1-rect-transcript"` | format tag |
| `version` | const `"1.0"` | contract version (this file) |
| `mode` | `"refutation"` \| `"exclusion"` | target statement (C10 ties it to m) |
| `function` | `"zeta"` \| `"f_DH"` | target function (§9.2 for f_DH) |
| `trust_label` | fixed string per function | the honest label, verbatim (§9) |
| `rect` | `{sigma1, sigma2, T1, T2}`, each rational | R = [σ₁,σ₂]×[T₁,T₂] |
| `scales` | `{K, A}`, positive integer strings | §1 |
| `claimed_m` | nonnegative integer string | the winding number m |
| `mesh` | `{bottom, right, top, left}`, rational lists | §4 |
| `segments` | array of row objects, global order (§4) | §5–§6 |
| `modulus_floor` | OPTIONAL `{Fn, Fd}` | §5.2 (C11) |
| `producer` | OPTIONAL free-form object | untrusted provenance metadata (§10) |
| `comment` | OPTIONAL string | untrusted |

Row object: `{reLo, reHi, imLo, imHi, argLo, argHi}`, all integer strings.

`w1-schema.json` (this directory) is the machine-readable shape contract (JSON Schema
2020-12). The schema enforces SHAPE only; every arithmetic and cross-field condition is the
checker's (§7). A file can be schema-valid and checker-rejected.

---

## 3. Rectangle block

`rect` holds σ₁ = p₁/q₁, σ₂ = p₂/q₂, T₁ = a₁/b₁, T₂ = a₂/b₂ as exact rationals. The checker
verifies (C2), all by integer cross-multiplication with the positive denominators:

* ½ < σ₁ ⟺ q₁ < 2·p₁
* σ₁ ≤ σ₂ ⟺ p₁·q₂ ≤ p₂·q₁
* σ₂ < 1 ⟺ p₂ < q₂
* T₁ < T₂ ⟺ a₁·b₂ < a₂·b₁

No sign constraint on T₁, T₂ is needed for soundness (D5 uses only Re ρ > ½), but production
refutation targets have T₁ > 0 by usage.

---

## 4. Boundary mesh: ordering convention and corner handling

**Orientation.** ∂R is traversed COUNTERCLOCKWISE (positive orientation) in the standard
identification of ℂ with ℝ² (Re horizontal increasing rightward, Im vertical increasing
upward), starting at the bottom-left corner σ₁ + iT₁. Edge order and traversal directions:

1. `bottom`: Im = T₁ fixed, Re from σ₁ to σ₂ (increasing);
2. `right` : Re = σ₂ fixed, Im from T₁ to T₂ (increasing);
3. `top`   : Im = T₂ fixed, Re from σ₂ to σ₁ (**decreasing**);
4. `left`  : Re = σ₁ fixed, Im from T₂ to T₁ (**decreasing**).

The orientation convention is not a checker degree of freedom: H-AP (§8.2) is STATED for this
exact traversal, so an orientation/sign error cannot hide in the checker — it would be a false
displayed hypothesis, visible in the ~100-line trusted Lean layer.

**Mesh encoding.** Each edge stores only its VARYING coordinate: `mesh.bottom` and `mesh.top`
are lists of rationals (Re values), `mesh.right` and `mesh.left` are lists of rationals (Im
values). Each list has length ≥ 2 and includes both endpoints. The checker verifies (C3):

* `bottom[0] = σ₁`, `bottom[last] = σ₂`, strictly increasing;
* `right[0] = T₁`, `right[last] = T₂`, strictly increasing;
* `top[0] = σ₂`, `top[last] = σ₁`, strictly decreasing;
* `left[0] = T₂`, `left[last] = T₁`, strictly decreasing —

equalities and inequalities of rationals by cross-multiplication (D7). This forces the four
edge chains to cover ∂R exactly once, in order, with no gaps and no overlaps beyond shared
endpoints.

**Corner handling.** Each corner appears exactly twice in the file — as the last breakpoint of
one edge and the first breakpoint of the next — and C3's endpoint equalities pin both
occurrences to the rectangle parameters, so the chains are automatically joined at the
corners. Segments never straddle a corner: every segment lies wholly in one edge. Corners
carry no rows of their own; a corner value f(corner) is covered by BOTH adjacent segments'
value boxes (each closed segment includes its endpoints).

**Segment enumeration.** Segment k (k = 0, 1, …, M−1) is the k-th consecutive breakpoint pair
in the traversal order bottom-segments, right-segments, top-segments, left-segments;
M = (|bottom|−1) + (|right|−1) + (|top|−1) + (|left|−1). `segments[k]` is the row for segment
k. The checker verifies |segments| = M (C4). This is the "declared indexing" required by
m2a-m2b-design §4.

---

## 5. Value rows and the nonvanishing scheme (the fixed modulus-excludes-0 scheme)

### 5.1 Per-segment value boxes and 0-exclusion (C5, C6)

For segment k with closed sub-segment γ_k ⊂ ∂R, the row asserts (under H-ENCL(a)):

  reLo_k ≤ K·Re f(s) ≤ reHi_k  and  imLo_k ≤ K·Im f(s) ≤ imHi_k  for ALL s ∈ γ_k.

The checker verifies box nonemptiness reLo_k ≤ reHi_k ∧ imLo_k ≤ imHi_k (C5; producer-bug
tripwire — an empty box makes H-ENCL false and the theorem vacuous, so rejecting is honesty,
not soundness) and the **exact 0-exclusion scheme**, fixed here per m2a-m2b-design §4:

  **C6 (nonvanishing / mesh admissibility):  reLo_k > 0 ∨ reHi_k < 0 ∨ imLo_k > 0 ∨ imHi_k < 0.**

**Derivation D1 (C6 is exactly "0 ∉ box", and it yields a coordinate half-plane).** The box
B_k = [reLo_k, reHi_k] × [imLo_k, imHi_k] (scaled by K, which fixes no sign issues since
K > 0) contains 0 iff reLo_k ≤ 0 ≤ reHi_k AND imLo_k ≤ 0 ≤ imHi_k. Negating: 0 ∉ B_k iff
0 ∉ [reLo_k, reHi_k] or 0 ∉ [imLo_k, imHi_k], i.e. iff reLo_k > 0 ∨ reHi_k < 0 ∨ imLo_k > 0 ∨
imHi_k < 0 — which is C6 verbatim. Moreover each disjunct places the whole box in an OPEN
coordinate half-plane: {Re > 0}, {Re < 0}, {Im > 0}, {Im < 0} respectively. So C6 gives, for
free, that B_k lies in an open half-plane through 0 — the fact D3 (§6.1) needs. ∎

Sign-based exclusion is preferred over a modulus inequality for the mandatory check because it
is EXACT for boxes (no slack lost to squaring) and costs four comparisons. The quantitative
squares scheme is the OPTIONAL floor row:

### 5.2 Optional modulus floor (C11) — the integer-squares scheme

When `modulus_floor` = {Fn, Fd} is present (claiming |f| ≥ Fn/Fd on all of ∂R — used by the
Gomila-screen sensitivity step 5 and by M2a's `BarrierCert` t-interpolation, which needs a
positive boundary-modulus floor), the checker computes for each k, in ℤ:

  mre_k := 0 if reLo_k ≤ 0 ≤ reHi_k, else min(|reLo_k|, |reHi_k|)
  mim_k := 0 if imLo_k ≤ 0 ≤ imHi_k, else min(|imLo_k|, |imHi_k|)

  **C11:  (mre_k² + mim_k²) · Fd² ≥ Fn² · K²  for every k.**

**Derivation D6 (C11 certifies the floor).** For x ∈ [lo, hi]: if lo ≤ 0 ≤ hi then min x² over
the interval is 0 = mre²; otherwise the interval lies strictly on one side of 0 and x ↦ x² is
monotone away from 0 on it, so min x² = min(lo², hi²) = min(|lo|,|hi|)². Hence for
(x, y) ∈ B_k: x² + y² ≥ mre_k² + mim_k² (the minima are attained coordinatewise
independently on a box). Under H-ENCL(a), (K·Re f(s), K·Im f(s)) ∈ B_k, so
K²·|f(s)|² ≥ mre_k² + mim_k², and C11 gives K²·|f(s)|²·Fd² ≥ Fn²·K², i.e.
|f(s)|² ≥ (Fn/Fd)², i.e. |f(s)| ≥ Fn/Fd, for every s ∈ γ_k, hence on ∂R. All integer, no
division. ∎

C11 is not load-bearing for the W1 conclusion (§6.3); it is a certified by-product consumed by
other components.

---

## 6. Winding-number enclosure rows — the argument-increment scheme

### 6.1 The enclosed quantity

For segment k, parameterize γ_k(t) = s_k + t·(s_{k+1} − s_k), t ∈ [0, 1] (endpoints in
traversal order, §4). Define the **argument increment**

  Δ_k := Im ∫₀¹ (f′(γ_k(t)) / f(γ_k(t))) · (s_{k+1} − s_k) dt.

Under H-ENCL(a) + C6, f is nonvanishing on the compact segment (D1), f′/f is continuous
there, and the integral is a genuine (finite) integral. The argument row asserts (under
H-ENCL(b)):

  argLo_k ≤ A · (Δ_k / 2π) ≤ argHi_k   (turn units).

**Derivation D2 (Δ_k is the increment of a continuous argument branch).** Let
u(t) := ∫₀ᵗ (f′/f)(γ_k(τ))·γ_k′(τ) dτ. Then (d/dt)[e^{−u(t)} f(γ_k(t))] =
e^{−u}·(−u′·f∘γ_k + (f′∘γ_k)·γ_k′) = 0, so e^{u(t)} = f(γ_k(t))/f(γ_k(0)) for all t. Hence
θ(t) := arg f(γ_k(0)) + Im u(t) is a continuous branch of arg f(γ_k(t)), and
Δ_k = Im u(1) = θ(1) − θ(0). ∎

**Derivation D3 (a-priori bound |Δ_k| < π, i.e. |A·Δ_k/2π| < A/2).** By D1, the value box —
hence the whole image f(γ_k) — lies in one open coordinate half-plane H = {z : Re(e^{−iφ}z) >
0}, φ ∈ {0, π/2, π, 3π/2}. Arguments of points of H form the open arcs
(φ − π/2 + 2πn, φ + π/2 + 2πn), n ∈ ℤ — disjoint open intervals of length π spaced 2π apart.
The continuous function θ(t) of D2 takes values in their union; [0,1] is connected, so θ stays
in ONE interval; therefore |Δ_k| = |θ(1) − θ(0)| < π. ∎

D3 justifies the clamp check C7 (below): a row with 2·|argLo_k| > A or 2·argHi_k > A could
never be a clamped enclosure of a true increment. Producers MUST clamp their computed
enclosures to [−A/2, A/2] before writing (sound: the true value lies in the intersection).

### 6.2 The checks (C7–C10)

* **C7 (row validity + clamp):** argLo_k ≤ argHi_k ∧ −A ≤ 2·argLo_k ∧ 2·argHi_k ≤ A, every k.
  (Tripwire justified by D3; not load-bearing in §6.3.)
* **C8 (sum width):** S_lo := Σ_k argLo_k, S_hi := Σ_k argHi_k;  2·(S_hi − S_lo) < A
  — the total-winding enclosure [S_lo/A, S_hi/A] has width < ½ turn.
* **C9 (integer containment):** S_lo ≤ A·m ≤ S_hi, with m = `claimed_m`.
* **C10 (mode):** mode `refutation` ⟹ m ≥ 1; mode `exclusion` ⟹ m = 0.

**Derivation D4 (width < ½ pins m uniquely).** If A·m and A·m′ both lie in [S_lo, S_hi] with
m, m′ ∈ ℤ, then A·|m − m′| ≤ S_hi − S_lo < A/2, so |m − m′| < ½, so m = m′. ∎

**The EXACT mesh-admissibility criterion the checker verifies is C6** (§5.1): each segment's
value enclosure excludes 0 — a box excluding 0 lies in an open coordinate half-plane (D1), so
the argument increment along the segment is well-defined (D2, plus integrability of f′/f on a
compact nonvanishing segment) and a-priori bounded by half a turn (D3), consistent with its
clamped row. If a producer cannot achieve C6 at any refinement, a zero of f lies on or near
∂R: the correct response is to MOVE the rectangle, never to weaken the criterion.

### 6.3 The soundness chain (the theorem the Lean stream proves)

Given `checkW1 d = true` (all of C1–C10, and C11 if the floor is present), H-ENCL(d) (§8.1),
and H-AP (§8.2), for f the function named by `function` (Lean v1: f = ζ only, §9.2):

1. **Boundary nonvanishing.** H-ENCL(a) puts f(γ_k) in box B_k for every k; C6 + D1 give
   0 ∉ B_k; C3/C4 give ∂R = ⋃_k γ_k. Hence f ≠ 0 on ∂R.
2. **Counting.** By step 1 and H-AP: the zero count Z of f in R° (with multiplicity) is finite
   and 2π·Z = Σ_edges Im ∮ f′/f. By additivity of the integral over concatenated segments
   (Lean obligation L1, §8.3 — provable, not displayed), Σ_edges = Σ_k Δ_k.
3. **Enclosure of Z.** H-ENCL(b) and step 2: A·Z = Σ_k A·(Δ_k/2π) ∈ [S_lo, S_hi].
4. **Pinning.** C9 puts A·m in the same interval; C8 + D4 force Z = m.
5. **Refutation conclusion (m ≥ 1).** Z ≥ 1: some ρ ∈ R° with f(ρ) = 0 and
   Re ρ > σ₁ > ½ (C2).
   **Derivation D5 (for f = ζ this is ¬RH):** ρ ∈ R° has ½ < Re ρ < 1 (C2: σ₂ < 1), so ρ is a
   zero of ζ in the open critical strip off the critical line. RH asserts every zero of ζ with
   0 < Re s < 1 has Re s = ½ (the trivial zeros −2, −4, … all have Re s < 0 ≤ ½ < Re ρ, so ρ
   is not one of them). Hence ¬RH. ∎
6. **Exclusion conclusion (m = 0).** Z = 0 (no zeros in R°) and step 1 (none on ∂R): no zeros
   of f in the closed rectangle R.

Load-bearing map: C2 → steps 5–6; C3/C4 → step 1; C6 → steps 1–2; C8/C9 → step 4; C10 → the
mode split; C1 underlies every cross-multiplication (D7). C5, C7, C11 are tripwires/optional
by-products — sound to check, not needed by the chain.

**Derivation D7 (cross-multiplication is sound).** For rationals n₁/d₁, n₂/d₂ with d₁, d₂ > 0:
n₁/d₁ < n₂/d₂ ⟺ n₁·d₂ < n₂·d₁ (multiply/divide by d₁·d₂ > 0, which preserves order), and
similarly for ≤ and =. C1's d ≥ 1 verification is what licenses every C2/C3 comparison. ∎

**Derivation D8 (the pole is outside; the count is zeros-only).** ζ is analytic on ℂ ∖ {1};
every s ∈ R has Re s ≤ σ₂ < 1 = Re 1 (C2), so 1 ∉ R and ζ is analytic on a neighborhood of
the compact R. H-AP is therefore stated for an analytic-on-R function and its conclusion
counts zeros with no pole correction. (For f_DH the point is vacuous — the function is entire;
see §9.2.) ∎

---

## 7. The checker, normatively (all checks, in order)

Input: the transcript translated to literal data (JSON for the reference checker; a Lean
structure literal for the kernel checker — the translation is mechanical and is itself
producer-side, untrusted; both consume the SAME numbers). Output: a single Bool. The checker
is a pure function; the check list is a conjunction — order is fixed only for failure
reporting, and short-circuiting does not affect the accepted set.

* **C1** scales and denominators: K ≥ 1, A ≥ 1; every rational's d ≥ 1.
* **C2** rectangle: q₁ < 2p₁; p₁q₂ ≤ p₂q₁; p₂ < q₂; a₁b₂ < a₂b₁  (§3).
* **C3** mesh walk: endpoint equalities and strict monotonicity per edge, cross-multiplied (§4).
* **C4** row count: |segments| = M (§4).
* **C5** box validity: reLo_k ≤ reHi_k ∧ imLo_k ≤ imHi_k, every k.
* **C6** nonvanishing/admissibility: reLo_k > 0 ∨ reHi_k < 0 ∨ imLo_k > 0 ∨ imHi_k < 0, every k.
* **C7** argument rows: argLo_k ≤ argHi_k ∧ −A ≤ 2·argLo_k ∧ 2·argHi_k ≤ A, every k.
* **C8** sum width: 2·(S_hi − S_lo) < A.
* **C9** containment: S_lo ≤ A·m ≤ S_hi.
* **C10** mode: refutation ⟹ m ≥ 1; exclusion ⟹ m = 0.
* **C11** (only if `modulus_floor` present): (mre_k² + mim_k²)·Fd² ≥ Fn²·K², every k (§5.2).

Every check is an integer comparison over transcript data (+, ·, |·|, min, max on ℤ only) —
`decide +kernel`-expressible, mirroring `NumericCert.check`'s discipline (only +, ·, max, |·|
on ℤ; comparisons by cross-multiplication).

### 7.1 Lean data structure and theorem shape (the contract for the Lean stream)

```lean
structure W1Row where
  reLo reHi imLo imHi argLo argHi : ℤ

structure W1Data where
  p1 : ℤ; q1 : ℤ    -- σ₁ = p1/q1   (q's checked ≥ 1 by C1, not typed ℕ+ : keep literals flat)
  p2 : ℤ; q2 : ℤ    -- σ₂
  a1 : ℤ; b1 : ℤ    -- T₁
  a2 : ℤ; b2 : ℤ    -- T₂
  K : ℤ; A : ℤ
  m : ℤ             -- claimed winding; mode is m ≥ 1 vs m = 0 at the theorem level
  bottom right top left : List (ℤ × ℤ)   -- rational breakpoints (n, d) per edge, §4 order
  rows : List W1Row                       -- global segment order, §4
  -- optional floor: (Fn, Fd) with (0,0) ∉ use; simplest is a separate structure/variant

def checkW1 (d : W1Data) : Bool := …   -- the conjunction C1–C10 (C11 in the floor variant),
                                       -- a fold over rows in RowCert's rowsOK style

theorem cert_of_checkW1 (d : W1Data) (hc : checkW1 d = true)
    (hEncl : W1EnclOK riemannZeta d)       -- H-ENCL, §8.1
    (hAP : RectArgPrinciple riemannZeta)   -- H-AP, §8.2
    : (1 ≤ d.m → ∃ ρ : ℂ, riemannZeta ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1
                        ∧ (d.a1/d.b1 : ℝ) < ρ.im ∧ ρ.im < d.a2/d.b2)
    ∧ (d.m = 0 → ∀ s : ℂ, s ∈ W1Rect d → riemannZeta s ≠ 0) := …
```

The statement surface follows the comparator pattern (`comparator/ChallengeDeps.lean`):
definable from Mathlib's `riemannZeta` plus this file's small definitions; instance files
prove `checkW1 d = true` by `decide +kernel`. The exact Lean formulation (names, how the
rectangle membership and the m-fold zero count with multiplicity are phrased) is the Lean
stream's to settle; the DATA fields, the CHECKS, and the HYPOTHESIS boundaries above are
normative.

---

## 8. The two displayed hypotheses (per D-R3 — exactly two, displayed, never hidden)

### 8.1 H-ENCL (the enclosure hypothesis; producers enter here)

For every segment k (γ_k as in §6.1, f the named function):

* **(a) value rows:** ∀ t ∈ [0,1]:
  reLo_k ≤ K·Re f(γ_k(t)) ≤ reHi_k  ∧  imLo_k ≤ K·Im f(γ_k(t)) ≤ imHi_k;
* **(b) argument rows:**  argLo_k ≤ A·(Δ_k/2π) ≤ argHi_k, with Δ_k the integral of §6.1.

This is the `EnclOK` displayed-hypothesis pattern of `NumericCert.lean` (line 72) /
`RowCert.lean`, extended from one real sequence to (Re, Im, Δ) per segment. H-ENCL is where
the untrusted producers' interval arithmetic enters the trusted statement; two independent
producers (Arb/FLINT `acb_dirichlet` leg; mpmath-ball leg — both D-R3 work items) make silent
producer bugs detectable but do not move the trust boundary. Anti-cheat note (Lean junk
values): if f vanished somewhere on γ_k, (a) + C6 would be contradictory — so the Bochner
integral in (b) can never silently be the junk value of a non-integrable integrand under the
hypotheses actually used; integrability is forced on the soundness side, where it belongs
(same pattern as the M2a design note §1.2 anti-cheat remark).

### 8.2 H-AP (the rectangle argument principle; v1's analytic debt, discharged by v1.1)

For the function f, stated for the EXACT traversal of §4: if f is analytic on an open set
containing R and f ≠ 0 on ∂R, then the number Z of zeros of f in R° counted with multiplicity
is finite and

  2π·Z = Σ_{e ∈ {bottom, right, top, left}} Im ∫_e f′/f ds,

the four edge integrals taken in the §4 directions. Status per D-R3 (direction file line 138):
Mathlib 2025-26 ships NO argument principle/residue theorem (verified in the Phase-4 cycle
against the community tracking pages; the 2025-26 meromorphic/divisor layer is an assist, not
the theorem). H-AP is therefore v1's second displayed hypothesis; **v1.1** (named, costed
milestone: build on `Zeta23/WeilEF/Contour.lean` + the Mathlib divisor layer) discharges it.
Success-criterion wording, fixed by D-R3: "converts into a kernel-checked disproof modulo the
two displayed hypotheses; fully kernel-checked after v1.1."

### 8.3 Lean-side proof obligations that are NOT hypotheses

* **L1 (additivity):** Σ over an edge's sub-segments of the §6.1 integrals = the edge's
  integral (interval additivity of the integral; uses only integrability from §8.1's
  anti-cheat note). Bridges the mesh-level rows to H-AP's four-edge statement.
* **L2 (D1–D8):** the eight derivations of this file — elementary real/complex arithmetic and
  the D2/D3 branch-lifting lemmas. D2/D3 are only needed if the Lean statement wants to
  EXPRESS the clamp C7's justification; the soundness chain (§6.3) does not use them, so a
  minimal v1 can omit them and keep C7 as an unexplained (sound) reject-more check.
* **L3 (checker soundness):** `cert_of_checkW1` per §6.3, mirroring
  `cert_of_checkRows` (`RowCert.lean` line 134): unpack the Bool conjunction, run the chain.

---

## 9. Variants

### 9.1 Exclusion certificates (mode `exclusion`, m = 0)

Same format, same checker; C10 requires m = 0. The certified statement is §6.3 step 6.
This is the M3 ledger's entry format and the null-test half of M1's acceptance tests
(direction file line 78: "boxes strictly right of the line at heights with certified m = 0").
Ledger language is fixed by D-R6 (§0). The exclusion mode is also the m = 0 building block
M2a's `BarrierCertData` reuses per t-slice (m2a-m2b-design §1.3 point 1); the t-interpolation
(Lipschitz row, slice spacing × sup |∂_t f_t| < per-slice modulus floor — where C11's floor
row is consumed) is OUTSIDE W1 v1 and lives in the BarrierCert format.

### 9.2 The Davenport–Heilbronn live-fire variant (`function`: `"f_DH"`) — checker-level only

Same fields, same checks, same row semantics with f = f_DH, where (on-disk source, quoted
verbatim from `anthropic/rh-program/results/ccm-dh-test/dh.py`, lines 5–8):

> f_DH(s) = 5^{-s} [ zeta(s,1/5) + kap*zeta(s,2/5) - kap*zeta(s,3/5) - zeta(s,4/5) ]
> kap = (sqrt(10-2*sqrt5) - 2)/(sqrt5 - 1)

(Hurwitz zetas; kap = tan θ with ε_χ = e^{2iθ} = τ(χ)/(i√5), χ mod 5, χ(2) = i — same file.)
f_DH is ENTIRE (no pole anywhere; the D1 direction file's M0 entry records "DH entire"), so
the σ₂ < 1 constraint is kept only for format uniformity and D8 is vacuous. The live-fire
acceptance target is a small rectangle around the certified off-line zero
ρ_DH = 0.808517182456637 + 85.699348485377592i (direction file line 104; residual 7.6e-41,
re-verified twice in the Phase-4 cycle) with mode `refutation`, m ≥ 1.

**Scope, per D-R8 (binding):** the v1 Lean soundness theorem is ζ-SPECIFIC; f_DH-in-Lean is
unpriced work. A `function: "f_DH"` transcript is accepted or rejected by the same checker
ARITHMETIC (C1–C11 mention no function), and an accepted DH transcript is a **checker-level
true-positive firing test** — proof that the producer+checker pipeline fires on a true
positive — and is NOT a Lean-backed conclusion about f_DH, NOT "RH-for-DH machine-checked
disproof". The trust labels, fixed verbatim (schema-enforced per function):

* `zeta`:  `kernel-checked modulo displayed hypotheses H-ENCL and H-AP (producers untrusted)`
* `f_DH`:  `checker-level only (D-R8): format-checked modulo H-ENCL for f_DH; no Lean-backed conclusion`

Future function tags (e.g. H_t slices for M2a) enter only by a version bump of this contract.

---

## 10. Producer requirements (informative — outside the trust boundary)

* Two independent producers per transcript (D-R3): Arb/FLINT (`acb_dirichlet` ζ enclosures;
  rigorous contour subdivision) and an independent mpmath ball-arithmetic implementation at
  different precision. Disagreement beyond stated radii is a stop-the-line event
  (m2a-m2b-design §4).
* A sound way for a producer to compute an argument row, recorded here so both legs implement
  the same mathematics: certify the segment's value box (interval evaluation over the whole
  sub-segment, subdividing until C6 holds); the box lies in a coordinate half-plane (D1);
  on that half-plane the principal-style branch φ-rotated argument is continuous, so
  Δ_k ∈ [min − max, max − min] of the rotated endpoint-argument enclosures — or, tighter,
  interval atan2 on the rotated endpoint boxes; clamp to [−A/2, A/2] (D3), outward-round to
  integers at scale A. Producer-side only; the checker never does trigonometry.
* Producers fill `producer` metadata: implementation, version, precision, subdivision policy,
  timestamps. Untrusted, unchecked, required by the two-producer bookkeeping.
* The JSON→Lean literal emitter is producer-side and untrusted; the kernel re-checks
  everything that matters from the literals.

---

## 11. Worked micro-example (tiny mesh, ARTIFICIAL data)

**Honesty label:** the numbers below are artificial — invented to exercise every check with
small integers. No producer certified H-ENCL for them; "the checker accepts" here means
exactly and only that C1–C11 pass. The files `w1-example-refutation.json` (this example) and
`w1-example-exclusion.json` (its m = 0 twin) sit in this directory and are re-checkable with
`reference_checker.py` (untrusted reference implementation; transcript of the run in
`reference-checker-run.txt`).

**Data.** mode `refutation`, function `zeta` (artificial), K = 100, A = 1000, m = 1.
Rectangle: σ₁ = 3/5, σ₂ = 7/10, T₁ = 10/1, T₂ = 11/1.
Mesh: bottom [3/5, 13/20, 7/10]; right [10/1, 21/2, 11/1]; top [7/10, 13/20, 3/5];
left [11/1, 21/2, 10/1] — two segments per edge, M = 8. Floor Fn/Fd = 1/4.

Rows (global order k = 0…7; boxes chosen to rotate once around 0, increments ≈ ⅛ turn):

| k | edge | reLo | reHi | imLo | imHi | argLo | argHi | C6 witness | mre | mim | mre²+mim² |
|---|------|------|------|------|------|-------|-------|------------|-----|-----|-----------|
| 0 | bottom | 50 | 90 | −25 | 25 | 110 | 140 | reLo = 50 > 0 | 50 | 0 | 2500 |
| 1 | bottom | 20 | 70 | 20 | 70 | 120 | 130 | reLo = 20 > 0 | 20 | 20 | 800 |
| 2 | right | −25 | 25 | 50 | 90 | 115 | 135 | imLo = 50 > 0 | 0 | 50 | 2500 |
| 3 | right | −70 | −20 | 20 | 70 | 120 | 140 | reHi = −20 < 0 | 20 | 20 | 800 |
| 4 | top | −90 | −50 | −25 | 25 | 105 | 130 | reHi = −50 < 0 | 50 | 0 | 2500 |
| 5 | top | −70 | −20 | −70 | −20 | 125 | 145 | reHi = −20 < 0 | 20 | 20 | 800 |
| 6 | left | −25 | 25 | −90 | −50 | 110 | 125 | imHi = −50 < 0 | 0 | 50 | 2500 |
| 7 | left | 20 | 70 | −70 | −20 | 120 | 138 | reLo = 20 > 0 | 20 | 20 | 800 |

**What the checker computes, in integers, check by check:**

* C1: K = 100 ≥ 1 ✓; A = 1000 ≥ 1 ✓; denominators 5, 10, 1, 1, 20, 2, 4 all ≥ 1 ✓.
* C2: σ₁ > ½: q₁ = 5 < 2·p₁ = 6 ✓. σ₁ ≤ σ₂: 3·10 = 30 ≤ 7·5 = 35 ✓. σ₂ < 1: 7 < 10 ✓.
  T₁ < T₂: 10·1 = 10 < 11·1 = 11 ✓.
* C3 (bottom): 3/5 = σ₁ (3·5 = 3·5) ✓; 3/5 < 13/20 (3·20 = 60 < 13·5 = 65) ✓;
  13/20 < 7/10 (13·10 = 130 < 7·20 = 140) ✓; 7/10 = σ₂ ✓. Right, top, left likewise
  (top and left checked DEcreasing).
* C4: M = 2+2+2+2 = 8 = |segments| ✓.
* C5: every reLo ≤ reHi, imLo ≤ imHi ✓ (by inspection of the table).
* C6: witness column above — every row has a strict coordinate sign ✓.
* C7: every argLo ≤ argHi ✓; max 2·|arg| = 2·145 = 290 ≤ A = 1000 ✓.
* C8: S_lo = 110+120+115+120+105+125+110+120 = **925**;
  S_hi = 140+130+135+140+130+145+125+138 = **1083**;
  2·(1083 − 925) = 316 < 1000 ✓ (total-winding enclosure [0.925, 1.083] turns, width 0.158).
* C9: S_lo = 925 ≤ A·m = 1000·1 = 1000 ≤ 1083 = S_hi ✓. (D4 in action: the only integer
  multiple of A in [925, 1083] is 1000 — 0 and 2000 are outside — so m = 1 is forced.)
* C10: mode refutation, m = 1 ≥ 1 ✓.
* C11 (floor 1/4): threshold Fn²·K² = 1·10000 = 10000; each row's (mre²+mim²)·Fd² =
  (mre²+mim²)·16 ∈ {2500·16 = 40000, 800·16 = 12800}, both ≥ 10000 ✓.

**Verdict: ACCEPT.** Modulo H-ENCL (false here — the data is artificial) and H-AP, the
transcript would certify: ζ has exactly 1 zero (with multiplicity) in (3/5, 7/10) × (10, 11)
and none on the boundary, hence a zero ρ with Re ρ > 3/5 > ½ — ¬RH. The conditional's
antecedent being undischarged is precisely what the displayed-hypothesis trust model makes
visible. (In reality ζ has no zeros in this box; a real producer could never certify
H-ENCL(b) rows summing near a full turn here.)

**Exclusion twin** (`w1-example-exclusion.json`): same rectangle and mesh; all boxes in the
right half-plane (reLo > 0), argument rows straddling 0 — S_lo = −92, S_hi = 148,
2·240 = 480 < 1000 ✓, S_lo ≤ A·0 = 0 ≤ S_hi ✓, mode exclusion m = 0 ✓ → ACCEPT; would
certify (modulo the hypotheses) "no zeros of ζ in [3/5, 7/10] × [10, 11]" — the D-R6 ledger
sentence with δ₀ = σ₁ − ½ = 1/10.

**Negative controls** (mutations of the example, exercised in `reference-checker-run.txt`):
box containing 0 → C6 fails; over-wide argument rows → C8 fails; claimed_m = 2 → C9 fails;
mode exclusion with m = 1 → C10 fails; bottom[last] ≠ σ₂ → C3 fails; σ₁ = ½ → C2 fails.

---

## 12. Design record (decisions taken here, and the road not taken)

1. **Per-segment (not per-point) value boxes.** The load-bearing facts are "f ≠ 0 on ALL of
   ∂R" and "Δ_k well-defined" — both statements about whole segments; segment boxes deliver
   them directly and cover the corners for free (§4). Point boxes would add rows without
   adding certified content.
2. **Argument rows in turn units.** Keeps 2π out of the transcript and makes C8/C9 pure
   integer statements; matches the W1 description in the direction file (line 37: enclosure of
   the winding integral "of width < ½ containing an integer m ≥ 1").
3. **Sign-based 0-exclusion as the mandatory scheme, integer-squares floor as optional.**
   D1 shows the sign test is EXACT for boxes; the squares scheme (§5.2) is strictly for
   quantitative floors that other components (M2a interpolation, screen sensitivity) consume.
   This fixes the scheme m2a-m2b-design §4 left open.
4. **The road not taken (recorded for v1.1 consideration): the sector-walk scheme.** The
   argument rows could be eliminated entirely: by D1 every 0-excluding box lies in a coordinate
   half-plane; label each segment R+/I+/R−/I− (quarter index 0/1/2/3), REQUIRE consecutive
   labels never opposite (index difference ≠ 2 mod 4), read off the per-transition quarter-turn
   increment d_k ∈ {−1, 0, +1} (the unique representative of the index difference mod 4 in
   that range), and conclude winding m = (Σ d_k)/4 by the D3 lifting argument applied
   per-transition — no producer argument enclosures, strictly smaller H-ENCL (values only).
   v1 chose the argument-increment rows because (i) they match the commissioned W1 format and
   the direction file's wording, (ii) H-ENCL(b) is a clean integral statement while the
   sector-walk soundness needs the full lifting lemma chain in Lean on day one, and (iii)
   argument rows degrade gracefully near m-ambiguity (width is visible and reportable as
   margin). The sector-walk is a trust-surface REDUCTION available later at pure-Lean cost;
   it would change the format (label rows replace argument rows) and hence the version.
5. **Mode explicit in JSON, implicit in Lean.** The service layer wants the intent named
   (`refutation` vs `exclusion`, C10); the Lean theorem naturally splits on m ≥ 1 vs m = 0
   without a mode field.
6. **All integers as decimal strings in JSON.** Production scales (K ~ 10³⁰⁺, per the M0
   certificates' 10⁻⁵⁷-width enclosures) overflow IEEE-754-faithful JSON readers; strings are
   lossless everywhere and cost nothing in the Lean literal translation.

## 13. File inventory (this directory) and validation record

| file | role | trust |
|---|---|---|
| `FORMAT.md` | this contract | normative |
| `w1-schema.json` | machine-readable shape contract (JSON Schema 2020-12) | normative (shape only) |
| `w1-example-refutation.json` | §11 micro-example | artificial data, honesty label §11 |
| `w1-example-exclusion.json` | §11 exclusion twin | artificial data |
| `reference_checker.py` | reference implementation of C1–C11 + shape checks | UNTRUSTED (producer-side prevalidation; the trusted checker is the Lean one) |
| `reference-checker-run.txt` | run transcript: both examples ACCEPT; six negative controls each fail at the intended check | evidence, rerunnable |

Cross-validation performed at write time (recorded in `reference-checker-run.txt`): the §11
arithmetic (sums 925/1083, width 316, floor products) was computed independently by the
reference checker and matches this document digit for digit; every negative control fails at
exactly the check named in §11. The reference checker validates shape (schema semantics
hand-implemented — no external jsonschema dependency) before running the checks, so a
transcript that passes it is both schema-valid and checker-accepted.
