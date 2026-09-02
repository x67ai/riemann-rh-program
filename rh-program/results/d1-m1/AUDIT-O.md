# AUDIT-O — adversarial audit of D1 M1 v1 (`results/d1-m1/`), auditor O

**Date:** 2026-09-02 (Session 14). **Auditor:** O, one of two independent auditors; nothing below
assumes anything about auditor P's findings. **Scope:** everything Session 8 built in
`results/d1-m1/` — the W1 transcript contract (`FORMAT.md` v1.0, `w1-schema.json`), the
mpmath-ball producer leg (`ball.py`, `zeta_encl.py`, `hurwitz_encl.py`, `producer_mp.py`), the
Arb leg (`producer_arb.py`), the two reference checkers (`reference_checker.py`,
`checker_ref.py`), the acceptance suite (`acceptance/`, `acceptance-report.md`,
`cost-curve.json`), and the Lean W1 layer
(`Zeta23/W1/{Format,Checker,Soundness,Examples}.lean`, `Zeta23/DBN/Defs.lean`).

**Discipline followed:** standing order 5 — every mathematical bound below is re-derived here from
first principles or quoted from an on-disk source with an exact location; no Session-8 file was
modified (repairs are PROPOSED as replacement text/code for the reconciler to apply); thermal
policy respected (at most two heavy local processes at a time; one `lake` process at a time).

---

## 0. VERDICT

| | count |
|---|---|
| **FATAL** | **0** |
| **MAJOR** | **2** |
| MINOR | 6 |
| INFO / nit | 3 |

**No bound in `zeta_encl.py`, `hurwitz_encl.py`, the DH κ enclosure, or either producer's
ball→integer conversion is non-rigorous as implemented.** Every enclosure honesty test I ran —
2 035 fresh membership checks against independent dps-100/dps-140 references at my own seeds, plus
~5 200 boundary point-samples tested against the shipped transcripts' own rows — passed with zero violations. The
winding scheme's geometry (C6 ⟹ half-plane ⟹ |Δ_k| < π; C8+C9 ⟹ Z = m) re-derives correct. Thirteen
classes of hand-corruption of five ACCEPTED producer transcripts were rejected at exactly the
intended check by both Python checkers, and eight of them again by the Lean kernel. The Lean
soundness theorem builds, is `sorry`-free, uses no `native_decide`, and `#print axioms` shows only
`propext`, `Classical.choice`, `Quot.sound`.

The two MAJORs are **coverage/packaging defects in the shipped Lean layer, not soundness holes**:
(M-1) the Lean checker had never been run on a single producer-emitted transcript — the acceptance
suite's "two checkers" are both Python — because the JSON→Lean literal emitter that `FORMAT.md` §10
names was never written; and (M-2) a Lean data module carrying ≳ 10³ transcript rows does not build
at Lean's default `maxRecDepth`, which the shipped 8-row artificial examples could not reveal. This
audit closes (M-1) by writing the emitter and kernel-checking all ten acceptance transcripts plus
both positive controls plus eight corruptions, and it localizes (M-2) to the **`def`'s list literal**
(fails at 8 000, passes at 40 000, for 1 294 rows) — `decide +kernel` itself needs no raised limit.

**Correction made on the resumed run (2026-09-02).** This report was written in one pass that was
cut off before it returned; the resumed pass re-ran every `audit_O_*` script and re-checked every
Lean claim (§10). All numerical results reproduced **exactly**. One finding did not survive
re-examination as written: **MAJOR-2's diagnosis was wrong** and has been rewritten — the
recursion-depth wall is hit by the *data literal in the emitted `def`*, not by `decide +kernel`
evaluation of `checkW1`, and the tail-recursion rewrite of `Checker.lean` that the first draft
proposed is **withdrawn**. Two small numbers were corrected (§3.3 line count, §4 import list), and
one new verification was added that the first pass had left open (§3.3: the Lean literals are
faithful to the JSON — without which every kernel verdict here would be vacuous).

---

## 1. Re-derivation of the Euler–Maclaurin remainder (task item 1)

### 1.1 The derivation, done independently

Let `f ∈ C^1[N, M]`, `N < M` integers. Integration by parts on `[n, n+1]` with the primitive
`x − n − 1/2` of `1`:

  ∫_n^{n+1} (x − n − ½) f′(x) dx = [(x − n − ½) f(x)]_n^{n+1} − ∫_n^{n+1} f
    = ½f(n+1) + ½f(n) − ∫_n^{n+1} f.

Summing `n = N … M−1` and using `Σ_{n=N}^{M−1} ½(f(n)+f(n+1)) = Σ_{n=N}^{M} f(n) − ½(f(N)+f(M))`:

  **(E0)**  Σ_{n=N}^{M} f(n) = ∫_N^M f + ½(f(N)+f(M)) + ∫_N^M B̄₁(x) f′(x) dx,   B̄₁(x) = {x} − ½.

Iterate with `B̄_{j}′ = j·B̄_{j−1}` (valid across integers for `j ≥ 3` because `B_j(0) = B_j(1)`,
and for `j = 2` because `B₂(0) = B₂(1) = 1/6`), noting `(2k+2)·(2k+1)! = (2k+2)!`:

* **(A)** ∫ (B̄_{2k+1}/(2k+1)!) f^{(2k+1)} = (B_{2k+2}/(2k+2)!)·[f^{(2k+1)}]_N^M − ∫ (B̄_{2k+2}/(2k+2)!) f^{(2k+2)}
  (the boundary term uses B̄_{2k+2}(integer) = B_{2k+2});
* **(B)** −∫ (B̄_{2k+2}/(2k+2)!) f^{(2k+2)} = +∫ (B̄_{2k+3}/(2k+3)!) f^{(2k+3)}
  (its boundary term vanishes because B_{2k+3} = 0 for `2k+3 ≥ 3`).

Induction gives, for `f ∈ C^{2m+1}`:

  **(EM)** Σ_{n=N}^{M} f(n) = ∫_N^M f + ½(f(N)+f(M))
      + Σ_{k=1}^{m} (B_{2k}/(2k)!)·(f^{(2k−1)}(M) − f^{(2k−1)}(N))
      + ∫_N^M (B̄_{2m+1}(x)/(2m+1)!)·f^{(2m+1)}(x) dx.

Specialize `f(x) = (x+a)^{−s}`, `a ∈ (0,1]` (the case `a = 0`, shifted, is `ζ`; the code's `ζ` leg
uses `f(x) = x^{−s}` on `[N,∞)` which is the same computation with the sample points at the
integers). Then `f^{(j)}(x) = (−1)^j (s)_j (x+a)^{−s−j}` with `(s)_j = s(s+1)…(s+j−1)`. Hence
`−f^{(2k−1)}(N) = +(s)_{2k−1}(N+a)^{−s−2k+1}` (because `(−1)^{2k−1} = −1`) and
`f^{(2m+1)}(x) = −(s)_{2m+1}(x+a)^{−s−2m−1}`. Letting `M → ∞` at `σ > 1` (every `M`-term is
`O(M^{−σ})`):

  **(T′)** Σ_{n=N}^{∞}(n+a)^{−s} = (N+a)^{1−s}/(s−1) + (N+a)^{−s}/2
      + Σ_{k=1}^{m} (B_{2k}/(2k)!)(s)_{2k−1}(N+a)^{−s−2k+1} + R_{N,m}(s,a),
  R_{N,m}(s,a) = −((s)_{2m+1}/(2m+1)!) ∫_N^{∞} B̄_{2m+1}(x)(x+a)^{−s−2m−1} dx.

The remainder integral converges locally uniformly, hence is analytic, on `{σ > −2m}`; the explicit
part is analytic on `ℂ∖{1}`; both sides agree on `σ > 1`; so (T′) holds on `{σ > −2m, s ≠ 1}` by
the identity theorem.

**Remainder bound.** Put `G(x) := (B̄_{2m+2}(x) − B_{2m+2})/(2m+2)`. Then `G` is continuous,
`G′ = B̄_{2m+1}` (a.e., and `G` is a genuine antiderivative across the integer joints because
`B_{2m+2}(0) = B_{2m+2}(1)`), `G(N) = 0` for integer `N`, and `|G| ≤ C_{2m+2}/(2m+2)` with
`C_j := sup_{[0,1]} |B_j(x) − B_j|`. With `u(x) = (x+a)^{−s−2m−1}`, `u′ = −(s+2m+1)(x+a)^{−s−2m−2}`:

  ∫_N^{∞} B̄_{2m+1}(x)(x+a)^{−s−2m−1} dx = [G u]_N^{∞} + (s+2m+1)∫_N^{∞} G(x)(x+a)^{−s−2m−2} dx
      = (s+2m+1)∫_N^{∞} G(x)(x+a)^{−s−2m−2} dx

(the boundary at `∞` vanishes because `σ + 2m + 1 > 0` and `G` is bounded; at `x = N` because
`G(N) = 0`). Since `∫_N^{∞}(x+a)^{−σ−2m−2} dx = (N+a)^{−σ−2m−1}/(σ+2m+1)`:

  **(RB′)**  |R_{N,m}(s,a)| ≤ |(s)_{2m+1}| · |s+2m+1| · C_{2m+2} · (N+a)^{−σ−2m−1}
                              / ( (2m+1)! · (2m+2) · (σ+2m+1) ),   valid for σ + 2m + 1 > 0.

Setting `a = 0` and shifting the sample points to `{N, N+1, …}` gives the `ζ` form (RB) verbatim.
**This reproduces `zeta_encl.py` STEPS 1–5 and `hurwitz_encl.py` STEPS 3′–5′ exactly, including
every sign.** The files' own derivations are correct as written.

### 1.2 Does the implementation match the derivation?

| item | derivation | code | verdict |
|---|---|---|---|
| first-omitted-term index | Bernoulli sum `k = 1…m` uses `(s)_{2k−1}`; the remainder carries `B̄_{2m+1}` and the constant `C_{2m+2}` | `zeta_encl.py:310–315` (`rising` starts at `(s)_1`; at `k ≥ 2` it multiplies by `(s+2k−3)(s+2k−2)`, so `rising = (s)_{2k−1}` — checked for k = 1,2,3), `:324` `c_sup(2*m+2)`, `:320–321` `Π_{j=0}^{2m}|s+j| ≥ |(s)_{2m+1}|` (2m+1 factors) | **no off-by-one** |
| σ-condition | needs `σ + 2m + 1 > 0`; scope guard `σ_lo > 0`; `(s−1)` must exclude 0 | `zeta_encl.py:291–293` raises unless `σ_lo > 0`; `Ball.recip` (`ball.py:267–273`) raises unless the `abs2` interval is strictly positive | **enforced, never assumed** |
| rounding direction of `σ` | smaller `σ` ⟹ larger bound, so use `σ_lo` | `denom` uses `slo` (`:325`), `N^{−(σ+2m+1)}` uses `slo` (`:327`) — both the conservative direction | **correct** |
| the bound's own arithmetic | must never round down | `prod_ub_hi`, `s2m1_hi`, `npow_hi` come from `ivmpf_bounds`, which returns **exact `Fraction`s** (`ball.py:126–129`, via lossless mpf→Fraction at `:115–123`); `c_ub`, `denom` are exact `Fraction`s; so `r` at `:329` is an **exact rational upper bound** — no float rounding anywhere in the bound | **rigorous** |
| padding the box | `\|R\| ≤ r` ⟹ `\|Re R\| ≤ r` and `\|Im R\| ≤ r` | `pad = iv_from_fraction_pair(−r, r)`; `total + Ball(pad, pad)` (`:330–331`) | **correct (conservative)** |
| `\|t\|` large | `N = max(20, ⌈(t_max + 2m + 1)/2⌉)`, `t_max` = sup\|Im\| over the **box**; the bound uses sup over the box of every `\|s+j\|` | `_auto_params` `:271–278`; `abs_iv()` over the box `:321,323` | **correct**; floats appear only in this parameter heuristic, never in a bound |
| `C_j` | `C_j = sup_{[0,1]}\|B_j(x) − B_j\|`, needed only as an upper bound | `c_sup` (`:227–248`): exact-rational interval Horner on 512 subintervals, `ub = max\|endpoints\|` — a rigorous upper bound with **no literature inequality trusted**; Bernoulli numbers re-verified against `Σ_{j≤k} C(k+1,j)B_j = 0` and the polynomials against `B_n′ = nB_{n−1}`, `B_n(0)=B_n`, `B_n(1)=B_n` (n≥2), all in exact `Fraction`s | **rigorous** |
| Hurwitz shift | `(N+a)^{−(2k−1)}` accumulator; `(n+a)^{−s} = exp(−s(log(nq+p) − log q))` with exact integer logs; `G(N) = 0` still holds because the shift does not move the integer sample points | `hurwitz_encl.py:117–124, 84–87, 108`; derivation note at `:50–53` | **correct** |

**Verified claim in the header, independently:** `C_30 = 1.218048e9`, `|B_30| = 6.0158e8`,
ratio 2.0247 — the "constant 2 instead of Backlund's 1" is paid, not assumed
(`validation-zeta.txt` line 4; reproduced by me).

**One thing the derivation does NOT need and the code does not claim:** `|B̄_j| ≤ |B_j|` at even
index. The file says so explicitly (`zeta_encl.py:102–103`) and computes `C_j` instead. Correct
practice; recorded as a positive finding.

### 1.3 The DH `tan θ` enclosure

`κ = (√(10 − 2√5) − 2)/(√5 − 1)`, quoted verbatim in both legs from
`results/ccm-dh-test/dh.py` lines 5–8 (I re-read that file's lines this session).

* **mp leg** (`producer_mp.py:126–129`): built by `iv.sqrt` / interval subtraction / interval
  division on **exact integer** inputs 5, 10, 2, 1. Denominator interval `√5 − 1 ∋ 1.236 > 0`, so
  no division-by-zero; inclusion-monotone throughout, so the interval contains the true `κ`.
  Independent check (mine): the interval is
  `[0.284079043840412270860440457909, …]` and the dps-140 surd value lies inside.
* **Arb leg** (`producer_arb.py:228–235`): the same expression in Arb balls, cached **by
  `ctx.prec`** (so a precision change cannot reuse a stale ball) — correct.
* **Identity check (mine, not in the Session-8 files):** with `ε_χ = τ(χ)/(i√5)` for `χ mod 5`,
  `χ(2) = i`, I computed `θ = ½ arg ε_χ` at dps 140 and found `|tan θ − κ| = 2.6 × 10⁻¹⁴¹`. The
  surd and the `tan θ` characterization agree; the constant is the right one.

No defect. (Script: `audit_O_encl_honesty.py`, section `KAPPA`.)

---

## 2. Enclosure honesty (task item 2) — 0 failures in 2 035 fresh checks

`audit_O_encl_honesty.py`, seed **902202614** (mine; Session 8 used 1859 / 1914 / 5 / 20260826 —
no overlap), iv prec 288 bits, references from mpmath's **float** pipeline at dps 100 (dps 140 for
κ), membership decided in exact `Fraction` arithmetic with a 10⁻⁹⁰ inflation that absorbs only the
reference's own rounding (enclosure widths are 10⁻²⁰…10⁻¹⁵, i.e. 55+ orders wider).

| regime | points | median width | max width | failures |
|---|---|---|---|---|
| Z1 ζ, σ ∈ (0.501, 0.999), \|t\| ≤ 200 | 60 | 3.85e−19 | 4.81e−17 | 0 |
| Z2 ζ, **σ near ½** (0.5000001 … 0.502) | 30 | 1.57e−18 | 3.96e−17 | 0 |
| Z3 ζ, **σ near 1** (0.998 … 0.9999999) | 30 | 7.44e−19 | 6.29e−18 | 0 |
| Z4 ζ, **\|t\| ≈ 10⁴** (the largest acceptance height), σ ∈ (0.6, 0.9) | 12 | 1.49e−15 | 8.83e−15 | 0 |
| Z5 ζ, wide boxes × 9 interior samples | 12 × 9 | — | — | 0 |
| H1 Hurwitz, a ∈ {1/5,2/5,3/5,4/5} ∪ random p/q, incl. σ near ½ and near 1 | 60 | 1.15e−18 | 4.58e−17 | 0 |
| H2 a = 1 identity (Hurwitz vs ζ leg, overlap + containment) | 15 | — | — | 0 |
| D1 f_DH random | 60 | 4.14e−20 | 3.17e−18 | 0 |
| D2 f_DH **at and around ρ_DH** (5 offsets, incl. exactly at the 15-digit ρ) | 5 | — | — | 0 |
| **total** | **395 membership checks** | | | **0** |

At `ρ_DH` the enclosure gives `|f_DH| ∈ [5.301e−16, 5.302e−16]`, matching the independent reference
to every printed digit and matching the Arb capability check H1 (`|f|² ≤ 2.8e−31`, i.e.
`|f| ≤ 5.29e−16`) — the two legs agree at the live-fire target.

**Additional coverage I added (see MINOR-2):** `audit_O_ball_largearg.py`, 1 640 checks of
`Ball.exp`, `iv.cos`, `iv.sin` and `pow_int_neg` at imaginary arguments up to `2 × 10⁵`
(the regime `zeta_ball` actually enters at `T = 10⁴`), against a dps-140 reference: **0 failures.**

---

## 3. Winding scheme: geometry re-derived, and corruption tests (task item 3)

### 3.1 Does C6 imply the claimed argument-increment bound? — YES

Re-derived independently:

1. A box `B = [a,b] × [c,d]` contains 0 iff `a ≤ 0 ≤ b` **and** `c ≤ 0 ≤ d`. Negating,
   `0 ∉ B ⟺ a > 0 ∨ b < 0 ∨ c > 0 ∨ d < 0` — exactly C6, and each disjunct puts the whole box in
   an **open half-plane through 0**: `{Re > 0}`, `{Re < 0}`, `{Im > 0}`, `{Im < 0}`.
   (Scaling by `K ≥ 1 > 0` changes nothing.)
2. On `H = {z : Re(e^{−iφ}z) > 0}` the set of arguments of points of `H` is
   `⋃_{n∈ℤ} (φ − π/2 + 2πn, φ + π/2 + 2πn)` — **disjoint** open intervals of length `π` spaced
   `2π` apart.
3. `u(t) := ∫_0^t (f′/f)(γ(τ))γ′(τ)dτ` satisfies `(d/dt)[e^{−u}f∘γ] = 0`, so `e^{u(t)} =
   f(γ(t))/f(γ(0))` and `θ(t) := arg f(γ(0)) + Im u(t)` is a **continuous** branch of
   `arg f(γ(t))` with `Δ = Im u(1) = θ(1) − θ(0)`.
4. `θ([0,1])` is connected and lands in the disjoint union of step 2, hence in **one** interval of
   length `π`. Therefore `|Δ| < π`, i.e. `|A·Δ/2π| < A/2` — which is what C7's clamp asserts and
   what makes the producers' clamping sound (intersecting two enclosures of the same true value).
5. `Z ∈ ℤ` and `A·Z ∈ [S_lo, S_hi]` (H-ENCL(b) summed, plus H-AP), `A·m ∈ [S_lo, S_hi]` (C9), and
   `S_hi − S_lo < A/2` (C8) give `A|Z − m| < A/2`, so `|Z − m| < ½`, so **`Z = m`**.

So the mesh-admissibility criterion C6 does imply the claimed bound, and C8+C9 do pin `m`. The
`FORMAT.md` derivations D1–D4 are correct as written. (D1, D4, D7 and the C6 ⟹ nonvanishing step
are additionally **machine-checked** in `Soundness.lean`: `row_box_excludes_zero` at line 642,
`boundary_nonvanishing` at 657, `pin_m` at 906, `ratVal_*_of_cross` at 186–208.)

A pleasing detail worth recording: `row_box_excludes_zero` does not need `K > 0` at all — it
substitutes `f = 0` into H-ENCL(a) to get `reLo ≤ 0 ≤ reHi ∧ imLo ≤ 0 ≤ imHi` and contradicts C6
by `omega`. The soundness of the 0-exclusion is therefore scale-free.

### 3.2 Corruption of ACCEPTED transcripts — every intended corruption is rejected

`audit_O_corrupt.py` (output: `audit_O_corrupt.txt`). Bases: five **real, producer-emitted,
both-checkers-accepted** transcripts — `w1-mp-null-t100` (52 rows), `w1-arb-null-t100` (27),
`w1-mp-null-deep-t100` (58), `w1-mp-dh-livefire` (40), `w1-arb-dh-livefire` (50). Each was verified
ACCEPT by both checkers before mutation.

| corruption (a buggy producer's plausible failure) | intended | `checker_ref.py` | `reference_checker.py` |
|---|---|---|---|
| **shift one enclosure so 0 enters the cell** (middle row, box widened to ±max) | C6 | C6 ✓ | C6 ✓ |
| **break sum-width < ½ turn** (row 0 widened to the full C7 clamp — stays C7-legal) | C8 | C8 ✓ | C8 ✓ |
| **change the integer m** (m + 1) | C9 | C9 ✓ | C9 ✓ |
| fabricate m = 1 on an exclusion box **and relabel the mode** | C9 | C9 ✓ | C9 ✓ |
| **break the contour ordering** (swap two adjacent bottom breakpoints) | C3 | C3 ✓ | C3 ✓ |
| reverse the top edge (CCW convention broken) | C3 | C3 ✓ | C3 ✓ |
| move σ₁ onto the critical line | C2 | C2 ✓ | C2 ✓ |
| drop one row / drop one mesh breakpoint | C4 | C4 ✓ | C4 ✓ |
| inflate the modulus floor | C11 | C11 ✓ | C11 ✓ |
| emit an empty value box | C5 | C5 ✓ | C5 ✓ |
| exceed the D3 half-turn clamp | C7 | C7 ✓ | C7 ✓ |
| shrink A by 10³ leaving the rows alone | any | C7 ✓ | C7 ✓ |
| f_DH transcript wearing the ζ trust label | SHAPE | SHAPE ✓ | SHAPE ✓ |

**No checker accepted a corruption it was supposed to catch.** (The two "MISMATCH" lines in
`audit_O_corrupt.txt` are harness no-ops: the "fabricate m = 1 + relabel to refutation" mutation is
the identity on the two DH transcripts, which are already `m = 1 / refutation`.)

**Corruptions that are invisible BY DESIGN** — recorded so the trust boundary is stated rather than
assumed (see MINOR-5): rotating the row list by one (row↔segment misalignment); negating every
value box (`f → −f`); shrinking `K` without rescaling the boxes; **halving `A` and doubling `m`**.
Each is accepted by both Python checkers *and* by the Lean kernel (I proved
`checkW1 mpDH_ahalf = true` for the last one), and each is harmless because it makes the displayed
hypothesis H-ENCL **false**, so the theorem's conclusion is vacuous rather than wrong. But the
checker offers **zero** redundancy on `K`, on `A`, or on the row↔segment correspondence: the only
detectors are H-ENCL itself and the two-producer cross-check, which is an untrusted diagnostic.

### 3.3 Running the LEAN checker on the same data — the acceptance claim, reproduced and extended

**How Session 8 ran the Lean checker on transcripts: it did not.** `Zeta23/W1/Examples.lean`
contains only the two ARTIFICIAL 8-row micro-examples of `FORMAT.md` §11 (I verified their literals
against `w1-example-{refutation,exclusion}.json` field by field — they match exactly) plus two
negative controls. No JSON→Lean emitter exists anywhere in the repository, although `FORMAT.md` §10
last bullet names one ("The JSON→Lean literal emitter is producer-side and untrusted"). See
**MAJOR-1**.

**The acceptance report's claim is reproducible as literally written.** §0/§1 say the eight null
transcripts are "ACCEPTED by BOTH reference checkers — `reference_checker.py` … and
`checker_ref.py`", and §6 states plainly that the suite does NOT establish "any Lean-kernel-checked
statement". I re-ran both Python checkers on all twelve acceptance transcripts: **8/8 null ACCEPT ×
2 checkers; 2/2 DH ACCEPT × 2 checkers; 2/2 positive controls REJECT at C2 × 2 checkers.** The
report is honest.

**What I added.** I wrote the missing emitter (`audit_O_lean_emit.py`), generated
`Zeta23/W1/AuditOCases.lean` (4 665 lines of literal data) and kernel-evaluated `checkW1` /
`checkW1Floor` with `decide +kernel`:

| Lean instance | rows | `checkW1` | note |
|---|---|---|---|
| `mpNullT100`, `arbNullT100`, `mpNullDeepT100`, `arbNullDeepT100` | 52/27/58/30 | **true** | + `checkW1Floor … = true` |
| `mpNullT1000`, `arbNullT1000` | 81/65 | **true** | + floor |
| `mpNullT10000`, `arbNullT10000` | 1294/983 | **true** | + floor |
| `mpDH`, `arbDH` (live fire) | 40/50 | **true** | + floor |
| `posMP_rej`, `posARB_rej` (positive controls) | 77/183 | **false** | rejected, as C2 requires |
| `mpDH_c6`, `mpDH_c8`, `mpDH_c9`, `mpDH_c3`, `mpDH_c2` | 40 | **false** | the §3.2 corruptions |
| `arbNullT100_c6`, `arbNullT100_c9`, `arbNullT10000_c3` | 27/27/983 | **false** | |
| `mpDH_ahalf` (A halved, m doubled) | 40 | **true** | the by-design blind spot, §3.2 |

`#print axioms` on these instance theorems: *"does not depend on any axioms"* (the floor variants:
`[propext]`). **The Lean checker agrees with both Python checkers on every real transcript and on
every corruption.** This is new evidence that did not exist before this audit.

**Are the Lean literals actually the acceptance transcripts?** (Gap the first pass left open;
closed on the resumed run.) The emitter is untrusted by construction, so its output must be
checked rather than believed: had it silently altered a row, every kernel verdict above would be
evidence about nothing. `audit_O_leancases_verify.py` (output `audit_O_leancases_verify.txt`)
**parses `AuditOCases.lean` back** with an independent tokenizer that shares no code with the
emitter, re-applies each declared mutation from its own re-implementation, and compares field by
field against `acceptance/*.json`: all 21 instances, all 11 scalar fields, all four mesh edges, and
all **4 217 rows** (6 integers each) — **0 mismatches**. The kernel verdicts are therefore genuinely
about the shipped transcripts.

### 3.4 Differential test: is the Lean check the SAME predicate? (task item 7)

`audit_O_lean_vs_py.py` generates random `W1Data` (a valid base plus one targeted single-clause
perturbation, so the accept/reject split is balanced), emits them as Lean literals, and requires
the kernel verdict to equal the Python verdict — read **mode-free** (accept iff some mode would
accept, i.e. C1–C9 and `m ≥ 0`) and with C11 routed to `checkW1Floor`, which is exactly what the
two files' documented split means.

* seed 20260902, **500 cases** (220 accept / 280 reject) — full agreement;
* seed 424242, **800 cases** (321 accept / 479 reject) plus **379 `checkW1Floor` cases** — full
  agreement.

Clause-by-clause the two are identical (C1 ↔ `1 ≤ K, A` + `1 ≤ q1,q2,b1,b2` + `densPos ×4`;
C2 ↔ the four cross-multiplications; C3 ↔ `edgeOK ×4`; C4 ↔ `rows.length + 4 = Σ lengths`, the
ℕ-subtraction-free form of `|rows| = M`; C5/C6/C7 ↔ `rowOK`; C8, C9 ↔ verbatim; C11 ↔ `floorRowOK`
with `mdist` = §5.2's mre/mim). The only two differences are documented and are recorded here as
MINOR-3 and MINOR-4.

---

## 4. Rounding directions, scales, exact rationals, checker independence (task item 4)

**Outward rounding, mp leg.** `producer_mp.py:147–159`: `floor_fr(q) = q.n // q.d`,
`ceil_fr(q) = −((−q.n) // q.d)` on exact `Fraction`s, applied as
`(⌊K·reLo⌋, ⌈K·reHi⌉, ⌊K·imLo⌋, ⌈K·imHi⌉)` where the endpoints come from `ivmpf_bounds`, which is a
**lossless** mpf→`Fraction` conversion (`ball.py:115–129`, specials rejected). Argument rows
(`:276–281`): the scaled interval's endpoints are floored/ceiled the same way, then clamped to
`[−A//2, A//2]`. **Outward in every position; no float touches an emitted number.** ✓

**Outward rounding, Arb leg.** `producer_arb.py:172–199`: `ball_interval` converts `mid ± rad` to
exact `Fraction`s from `man_exp()` (raising unless both are exact), then `out_int_bounds` floors /
ceils at the scale — and additionally **cross-checks against the library's own directed
`lower()`/`upper()`**, raising if they do not bracket the mid/rad interval. Argument rows
(`:366–393`): exact interval subtraction `d_lo = θ_q^lo − θ_p^hi`, `d_hi = θ_q^hi − θ_p^lo`, then
`div_interval_by_pos`, whose four sign cases I re-derived and confirm are the outward ones
(`x/d` is maximized at `x = n_hi` with `d = d_lo` if `n_hi ≥ 0`, else `d = d_hi`; symmetrically for
the minimum), then floor/ceil at scale `A`, then the clamp with `A` **even by construction** so
`A//2 = A/2` exactly. ✓

**Rotation bookkeeping (Arb).** I verified `ROTATIONS` (`producer_arb.py:308–313`) against
`e^{−iφ}z`: `φ=π/2 → (Im, −Re)`, `φ=π → (−Re, −Im)`, `φ=3π/2 → (−Im, Re)` — all correct, and in
each case the "rotated `Re > 0`" test is exactly the box's C6 witness. Both endpoints of a segment
use the **same** rotation (the D-P5 requirement); using different ones would be unsound and the
code does not. ✓

**Half-plane bookkeeping (mp).** `refine_edge` requires *both* `box.halfplane() ≠ None` (a
statement about the ball) *and* `c6_ints(vrow)` (a statement about the rounded row). The branch tag
comes from the ball, the checker's C6 from the row; they may be witnessed by different coordinates
and that is still sound, because the ball's half-plane is a true statement about `f` on the whole
segment. ✓

**Scale K.** `K` enters the soundness chain **nowhere** except through C11: the W1 conclusion needs
only "the box excludes 0", which is scale-invariant for `K > 0` (§3.1 step 1, and `row_box_excludes_zero`
needs no sign hypothesis on `K` at all). C11's floor claim `|f| ≥ Fn/Fd` **is** `K`-dependent, and
the derivation D6 is correct: for `x ∈ [lo,hi]`, `min x² = 0` if the interval straddles 0 and
`min(|lo|,|hi|)²` otherwise, so `K²|f|² ≥ mre² + mim²`, and C11 gives `|f|² ≥ (Fn/Fd)²`. Producers
set `Fd = K` and `Fn = isqrt(min_k(mre²+mim²))`, so C11 holds by construction of `isqrt`
(`producer_mp.py:337–349`, `producer_arb.py:449–454`, derivation D-P7). ✓

**Exact-rational rectangle data.** `rect` and every mesh breakpoint are `{n, d}` integer strings;
`d` is syntactically positive in the schema and re-verified `≥ 1` by C1; every comparison in both
Python checkers and in Lean is by cross-multiplication (D7, machine-checked at
`Soundness.lean:186–208`). No division and no float anywhere in checked code. ✓

**Checker/producer code independence.** `checker_ref.py` imports exactly `json, re, sys,
fractions`; `reference_checker.py` imports exactly `copy, json, os, re, sys` (all stdlib).
**Neither imports
`ball`, `zeta_encl`, `hurwitz_encl`, `producer_mp`, `producer_arb`, `mpmath` or `flint`** — so no
evaluation code is shared with any producer. Verified by grep over all import statements. ✓

---

## 5. Independence of the two producer legs, and the cross-check re-run (task item 5)

**No shared code, in either direction.** `producer_arb.py` imports `flint` (Arb) and stdlib only —
it never imports `ball`, `zeta_encl`, `hurwitz_encl` or `producer_mp`. `producer_mp.py` /
`ball.py` / `zeta_encl.py` / `hurwitz_encl.py` never import `flint` or `producer_arb`. The two legs
share **only** the format contract. They also differ mathematically, not just in library:

* mp leg: hand-derived Euler–Maclaurin with the certified `C_{2m+2}` constant, mpmath `iv`
  directed-rounding intervals, argument rows from **half-plane branch endpoint differences**;
* Arb leg: `acb.zeta` (Arb's own algorithms), Arb balls, argument rows from **rotated-atan2 balls**
  with escalating precision.

**Cross-check re-run by me** (`acceptance/crosscheck.py`, four pairs):

| pair | overlap pairs checked | report's figure | verdict |
|---|---|---|---|
| null t100 | 83 | 83 | CONSISTENT |
| null t1000 | 158 | 158 | CONSISTENT |
| null deep-t100 | 90 | 90 | CONSISTENT |
| DH live fire | 122 | 122 | CONSISTENT |

Every overlap count reproduces the report exactly; all cell-wise value boxes intersect; the winding
enclosures intersect and contain the common integer `m`. ✓

---

## 6. Every number in `acceptance-report.md` and `cost-curve.json` (task item 6)

`audit_O_report_check.py` recomputes each printed figure from the JSON artifacts.

* **Segment counts** — all twelve match (52/27, 81/65, 1294/983, 58/30, 40/50, 77/183). ✓
* **Winding enclosures** — every `(S_lo, S_hi)` matches the report's printed pair exactly, in both
  the `·10⁻¹²` (mp, A = 10¹²) and `·10⁻⁶` (arb, A = 10⁶) unit conventions. ✓
* **Claimed `m`, C8 and C9** — recomputed and hold for all twelve. ✓
* **Certified floors** — all match to the report's printed precision (the only two "mismatches" my
  script flagged, 8.13195e−05 vs "8.13e−05" and 7.63776e−06 vs "7.64e−06", are correct
  3-significant-figure roundings; my tolerance was too tight, not the report wrong). ✓
* **Wall times** — the report's `wall s` column matches each transcript's own producer metadata /
  the cost-curve entry (1.0, 0.09, 8.6, 0.14, 1564.7, 2.6, 1.1, 0.09, 3.5, 0.19). ✓
* **`cost-curve.json`** — all ten entries name an existing transcript; every `segments` and
  `wall_seconds` matches; and I verified the derived field `winding_width_turns` equals
  `(S_hi − S_lo)/A` for all ten (5.2e−11, 8.1e−11, 1.316e−9, 5.8e−11, 2.7e−5, 6.5e−5, 9.83e−4,
  3e−5, 4e−11, 5e−5). `depth_delta0` = σ₁ − ½ and `height_T` = T₁ are correct in every row. ✓

**Independent recomputation of the DH live-fire winding, from scratch** (`audit_O_dh_winding.py`,
output `audit_O_dh_winding.txt`). Method deliberately different from both legs: `mp.zeta(s, a)`
float pipeline at dps 60, `f_DH` rebuilt from the `dh.py` formula, winding by **dense principal-
argument unwrapping** (24 sub-points per transcript segment).

* Newton refinement from scratch (dps 80) gives
  `ρ_DH = 0.808517182456637385553351960607 + 85.6993484853775921719292677089·i`,
  `|f_DH(ρ)| = 4.8 × 10⁻⁸⁰`, strictly inside `[4/5, 41/50] × [8569/100, 8571/100]` — the direction
  file's 15-digit value is a correct rounding of it.
* Recomputed winding = **1.0 turns** to 61 digits on both transcripts; inside each transcript's own
  enclosure `[0.99999999998, 1.00000000002]` (mp) and `[0.999973, 1.000023]` (arb).
* **H-ENCL spot test:** all 40 + 50 value rows contain `K·Re f` and `K·Im f` at every sampled point
  (0 violations); all 40 + 50 argument rows contain `A·Δ_k/2π` (0 violations); both certified
  modulus floors are respected (0 violations).

**Same test extended to the ζ null transcripts** (`audit_O_zeta_rows.py`): five transcripts
(mp/arb t100, mp/arb deep-t100, arb t1000), 0 value-box violations, 0 argument-row violations,
0 floor violations, recomputed winding `= 0` to 52 digits and inside each transcript's enclosure.

---

## 7. The Lean layer (task item 7)

* **`lake build Zeta23.W1.Soundness` — PASSES** (cached from 01:52; re-verified this session,
  3 142 jobs, exit 0). Working tree `/Users/jaytyagi/rh-lean-work/zeta-23-lean-main`, Lean
  v4.33.0-rc2. I did **not** rebuild the library.
* **`#print axioms` (scratch module `Zeta23/W1/AuditO.lean`):**

  ```
  'Zeta23.W1.cert_of_checkW1'                 depends on axioms: [propext, Classical.choice, Quot.sound]
  'Zeta23.W1.floor_of_checkW1Floor'           depends on axioms: [propext, Classical.choice, Quot.sound]
  'Zeta23.W1.boundary_nonvanishing'           depends on axioms: [propext, Classical.choice, Quot.sound]
  'Zeta23.W1.pin_m'                           depends on axioms: [propext, Classical.choice, Quot.sound]
  'Zeta23.W1.exampleRefutation_accepted'      does not depend on any axioms
  'Zeta23.W1.exampleExclusion_accepted'       does not depend on any axioms
  'Zeta23.W1.exampleRefutation_floor_accepted' depends on axioms: [propext]
  'Zeta23.W1.exampleRefutation_C6_control'    does not depend on any axioms
  'Zeta23.W1.exampleRefutation_C9_control'    does not depend on any axioms
  ```

  Only the three standard Mathlib axioms; **no `sorryAx`**. `grep` over `Zeta23/W1/` and
  `Zeta23/DBN/` finds no `sorry` and no `native_decide` outside prose comments. The four program
  files in the working tree are byte-identical to their copies under `rh-program/lean/Zeta23/`.
* **Statement audit.** `RowEnclOK` / `W1EnclOK` (`Soundness.lean:152–169`) state H-ENCL exactly as
  `FORMAT.md` §8.1 does, per segment, with the row↔segment correspondence carried by
  `List.Forall₂ … d.rows (segs d)` — i.e. the declared indexing is *inside* the hypothesis, which is
  why a row permutation is a false hypothesis rather than a checker hole (§3.2).
  `RectArgPrinciple` (`:173–184`) is stated in **consequence form** (∃ Z : ℕ with the winding
  identity, `Z = 0 → no zeros in R°`, `1 ≤ Z → ∃ zero in R°`). I confirm the header's claim that
  this is *implied by* §8.2 (take `Z` := the zero count with multiplicity) and therefore **assumes
  strictly less** — the theorem is stronger, not weaker. I also confirm `RectArgPrinciple` is a
  **true** statement (`∮ f′/f = 2πi·Z` by the argument principle; `Im` of that is `2πZ`; `Z ∈ ℕ`),
  so v1.1 has a dischargeable target, and it is not vacuous for degenerate `σ₁ = σ₂` (there
  `Z = 0` works and the increments cancel).
  The conclusion (`:928–932`) is `1 ≤ m → ∃ ρ, ζ(ρ) = 0 ∧ ½ < Re ρ < 1 ∧ T₁ < Im ρ < T₂` and
  `m = 0 → ∀ s ∈ closed R, ζ(s) ≠ 0`. The `m = 0` branch really is the **closed** rectangle
  (`W1Rect = rectClosed`), matching §6.3 step 6. ✓
* **Proof audit (structure).** `checksOK_of_checkW1` unpacks the Bool conjunction; `bdry_cover`
  proves `∂R = ⋃ γ_k` from C3+C4; `boundary_nonvanishing` is step 1; `edge_sum_eq` +
  `logDerivSegIntegral_affine` discharge L1 (additivity) with integrability **proved** for ζ from
  analyticity off `s = 1` plus checker-certified boundary nonvanishing (`continuousOn_zeta_logDeriv_seg`);
  `hAP` is applied with `U = {s : Re s < 1}` and `DifferentiableOn ℂ riemannZeta U` discharged from
  `differentiableAt_riemannZeta`; `sum_arg_encl` + `pin_m` give `Z = m`. The chain is exactly
  `FORMAT.md` §6.3. ✓

---

## 8. FINDINGS

### MAJOR-1 — the Lean checker had never been run on a producer-emitted transcript; the JSON→Lean emitter named by the contract does not exist

**Where:** `Zeta23/W1/Examples.lean` (only `exampleRefutation` / `exampleExclusion`, 8 artificial
rows each); `FORMAT.md` §10 last bullet ("The JSON→Lean literal emitter is producer-side and
untrusted") — no such emitter is on disk; `acceptance-report.md` §0/§1 ("both checkers" = the two
Python ones).

**Why it matters.** M1 v1's whole point is that the *trusted* checker is the Lean one. Before this
audit, the evidence that the Lean checker and the format agree consisted of 8 rows of invented
data with 3-digit integers, while the acceptance transcripts carry up to 1 294 rows with 10³⁰-scale
integers. The cross-validation the report describes ("two implementations of the spec") was
Python-vs-Python. This is a *coverage* gap, not a soundness claim error — the report explicitly
says in §6 that the suite establishes no Lean-kernel-checked statement, so **no dishonesty**.

**Status: CLOSED by this audit.** `audit_O_lean_emit.py` (in this directory) is a mechanical,
untrusted JSON→`W1Data` literal emitter; `Zeta23/W1/AuditOCases.lean` in the working tree carries
all ten acceptance transcripts, both positive controls and eight corruptions, and every one
kernel-evaluates to the verdict both Python checkers give (§3.3).

**Proposed repair (for the reconciler, not applied):**
1. Promote the emitter into the deliverable as `results/d1-m1/emit_lean.py` with the program header,
   and add a row to `FORMAT.md` §13's file inventory:
   `| emit_lean.py | JSON transcript → Lean W1Data literal (mechanical) | UNTRUSTED (producer-side; the kernel re-checks from the literals) |`.
2. Add a real-transcript instance file `Zeta23/W1/Instances.lean` carrying at least
   `w1-{mp,arb}-null-t100` and `w1-{mp,arb}-dh-livefire`, each with
   `theorem … : checkW1Floor … = true := by decide +kernel`, and cite it in
   `acceptance-report.md` §0 as a **third** checker column.
3. Amend `acceptance-report.md` §0's row 1 to read
   "**PASS** — all 8 transcripts ACCEPTED by both Python reference checkers **and by the Lean kernel
   checker (`decide +kernel`)**" only *after* (2) lands; until then leave the honest wording.

### MAJOR-2 — a Lean data module carrying ≳ 10³ transcript rows does not build at the default `maxRecDepth`: the **list literal in the emitted `def`** is what exceeds it, not `decide +kernel`

> **Correction notice (resumed run, 2026-09-02).** The first draft of this finding attributed the
> recursion-depth wall to `decide +kernel` evaluation of `checkW1`, and proposed a tail-recursive
> rewrite of `Checker.lean`'s folds. **That diagnosis was wrong, and the repair it implied would
> not have fixed anything.** The isolation experiments below were run on the resumed pass and
> overturn it. The *measured thresholds* in the first draft were right; the *cause* was not.

**Where:** the emitted data module (`Zeta23/W1/AuditOCases.lean`, and any `Zeta23/W1/Instances.lean`
that MAJOR-1's repair would add) — the ~1 000-element `rows := [⟨…⟩, …]` literal inside
`def mpNullT10000 : W1Data where`. `audit_O_lean_emit.py` **does not emit a `set_option maxRecDepth`
line**; the one at `AuditOCases.lean:13` was added by hand after generation, so the emitter as
shipped produces a file that does not build.

**Measured (three isolation experiments, resumed run).**

| experiment | file contents | `maxRecDepth` | result |
|---|---|---|---|
| A. **`decide +kernel` alone** | `import Zeta23.W1.AuditOCases` + `theorem : checkW1 mpNullT10000 = true := by decide +kernel` (1 294 rows, data **imported** from the `.olean`) | **default (512)** | **succeeds, 1.86 s**, `#print axioms` → no axioms |
| B. **`def` alone** | the `mpNullT10000` def literal only, **no `decide` anywhere in the file** | default (512) | **`maximum recursion depth has been reached` at the `def` line** |
| C. full 21-instance file | `AuditOCases.lean` with the option varied | 512 / 8 000 | 3 errors, at lines 444, 1757, 3623 — exactly the three `def`s with ≥ 983 rows (`mpNullT10000`, `arbNullT10000`, `arbNullT10000_c3`), and at **no** theorem |
| | | 40 000 / 100 000 | 0 errors, 13.9 s wall for ~2 900 rows |

Experiment A alone refutes the original claim: kernel evaluation of `checkW1` at 1 294 rows costs
under two seconds and needs **no** raised limit. Experiment B alone isolates the cause. The failure
is in the **definition compiler**, not the elaborator or the kernel: at the default limit Lean
records `mpNullT10000` as `noncomputable` (a later `#eval` fails with
`error(lean.dependsOnNoncomputable) … depends on 'mpNullT10000', which is 'noncomputable'`) while
`decide +kernel` on it still reduces correctly and `#print axioms` still reports no axioms. So the
proof terms produced at the default limit are *sound*; the module merely fails to **build**.

**Why it still matters (MAJOR, at reduced scope).**
1. It blocks MAJOR-1's own repair: the `Zeta23/W1/Instances.lean` proposed there will not build
   without the option, and the emitter that generates it does not write one.
2. It is a **data-packaging** question for M2a, not a checker question. The Gomila screen step 3
   lane is 3 149 013 rows; a single Lean list literal at that size is not viable at any
   `maxRecDepth` (experiment C already needs 40 000 for 1 294), and the answer will be chunking the
   data across several `def`s joined by `++`, or a compact byte/`ByteArray` encoding decoded inside
   the checker — a decision that must be made **before** `BarrierCert.lean` is written, because it
   changes `BarrierCertData`'s shape.
3. `Checker.lean`'s fold style is **not** implicated. No change to `densPos`, `chainLt`, `chainGt`,
   `lastOK`, `rowsOK`, `sumArgLo`, `sumArgHi` or `floorRowsOK` is warranted by this evidence, and
   the first draft's proposed rewrite of ~60 lines of `Soundness.lean` is **withdrawn** — it would
   have cost real work and fixed nothing.

**Proposed repair (not applied):**
1. Make the emitter write the option it needs. In `audit_O_lean_emit.py`'s header block (and in the
   `emit_lean.py` that MAJOR-1 promotes into the deliverable), after the `namespace W1` line, emit

   ```
   set_option maxRecDepth 100000
   ```

   and add to `FORMAT.md` §7.1:
   *"Compiling a Lean `W1Data` literal of R rows needs `maxRecDepth ≳ 30·R` (measured: R = 1 294
   fails at 8 000, passes at 40 000); the default 512 suffices only for the §11 micro-examples.
   The requirement is on elaborating/compiling the **data literal**, not on kernel evaluation of
   `checkW1`, which at R = 1 294 runs in under 2 s at the default limit once the data is imported."*
2. Before M2a: settle the bulk-data representation for `BarrierCertData` (chunked `def`s, or a
   decoded compact encoding), and record the choice in `m2a-m2b-design.md` §4. Do **not** spend
   effort on tail-recursion in `Checker.lean` for this reason.

### MINOR-1 — `reference_checker.py` prints the ζ trust sentence on `f_DH` files

**Where:** `reference_checker.py`, the ACCEPT banner (`run_file`): it prints
`VERDICT: ACCEPT (all checks pass; conclusion holds modulo the displayed hypotheses H-ENCL, H-AP)`
for an `f_DH` transcript too. Confirmed live on `acceptance/w1-mp-dh-livefire.json`.

Session 8 recorded this itself (`acceptance-report.md` §7 note 2) and chose not to repair it "to
keep the format author's checker byte-identical this session". I agree it is cosmetic and that the
transcript content is correct — but D-R8 exists precisely because this sentence is the one that
gets copied into a claim, and an untrusted tool that prints an H-AP-backed conclusion for `f_DH` is
a laundering hazard. **Proposed repair (not applied):** in `run_file`, replace the single banner by

```python
    label = ('conclusion holds modulo the displayed hypotheses H-ENCL, H-AP'
             if d['function'] == 'zeta' else
             'checker-level only (D-R8): format-checked modulo H-ENCL for f_DH; '
             'no Lean-backed conclusion')
    print(f'   VERDICT: ACCEPT (all checks pass; {label})')
```

and delete `acceptance-report.md` §7 note 2's "recorded, not repaired" clause.

### MINOR-2 — `ball.py --selftest` never enters the argument-reduction regime the producer actually uses

**Where:** `ball.py:396–404` (`rnd_point_ball`, `scale = 5`) — every self-test point has
`|Re|, |Im| ≤ 5`, so `iv.exp`, `iv.cos`, `iv.sin` are exercised only at small arguments. But
`pow_int_neg` (`zeta_encl.py:263–266`) calls `Ball.exp` with imaginary part `−t·log n`, which at the
suite's own `T = 10⁴` box reaches `|Im| ≈ 10⁴ · log 5015 ≈ 8.5 × 10⁴` — squarely in mpmath's
trigonometric argument-reduction path. The file's stated trust model ("PLATFORM TRUST in mpmath's
directed rounding … cross-validated by the self-test") therefore does not cover the regime that
matters most.

**No defect found.** `audit_O_ball_largearg.py` (mine): 1 640 checks of `Ball.exp`, `iv.cos`,
`iv.sin`, `pow_int_neg` at `|Im|` up to `2 × 10⁵` and of wide (multi-period) imaginary intervals,
against a dps-140 reference — **0 failures**. **Proposed repair:** fold that script's first loop
into `ball.py::_selftest` as a third block (`# large-argument block: the pow_int_neg regime`), so
the shipped self-test covers what production does.

### MINOR-3 — `checkW1` and the Python checkers have different accepted sets on floor-bearing transcripts

`FORMAT.md` §7 lists C11 inside the single normative check list, and both Python checkers fold C11
into one ACCEPT/REJECT verdict. Lean splits: `checkW1` = C1–C10, `checkW1Floor` = C1–C10 + C11.
Consequence, found by my differential fuzz (case `fz027`): a transcript carrying a `modulus_floor`
that fails C11 is **REJECTED** by both Python checkers and **ACCEPTED** by `checkW1`.

Not a soundness hole (C11 is a by-product, `FORMAT.md` §5.2/§6.3), and all ten shipped acceptance
transcripts pass C11 so no verdict is affected. But "both checkers accept" is not a well-defined
statement for floor-bearing transcripts, and every acceptance transcript carries a floor.
**Proposed repair:** in `FORMAT.md` §7, after the C11 bullet, add:

> **Floor variant.** C11 is not part of `check`; it is part of `checkFloor`. In Lean this is the
> `checkW1` / `checkW1Floor` split (§7.1). The reference checkers fold C11 into a single verdict, so
> for a transcript carrying `modulus_floor` their ACCEPT corresponds to `checkW1Floor`, not
> `checkW1`; a transcript whose floor row fails C11 is rejected by them and accepted by `checkW1`.

### MINOR-4 — the normative check list and the Lean checker are out of step on C10

`FORMAT.md` §7's C10 is the mode tie (`refutation ⟹ m ≥ 1`, `exclusion ⟹ m = 0`), which the Lean
structure cannot express (no `mode` field). `Checker.lean:146–147` instead requires `0 ≤ m` and
labels it "C10 (Lean remnant)" — a clause that appears **nowhere** in `FORMAT.md`'s normative list.
Both directions are individually documented (§12.5; `Checker.lean`'s header) but the list itself is
not. **Proposed repair:** replace `FORMAT.md` §7's C10 bullet with

> * **C10** mode/sign: in the JSON checker, mode `refutation` ⟹ m ≥ 1 and mode `exclusion` ⟹ m = 0.
>   The Lean `W1Data` has no `mode` field (§12.5), so `checkW1` carries instead the clause
>   **0 ≤ m**, and the refutation/exclusion split happens in the theorem (`1 ≤ m` vs `m = 0`).
>   Read mode-free, the two predicates coincide: a transcript is Lean-accepted iff it would be
>   JSON-accepted under some mode.

(That equivalence is what my 1 300-case differential test verifies, §3.4.)

### MINOR-5 — the checker's by-design blind spots are not stated in the contract

`K`, `A`, and the row↔segment correspondence are entirely producer declarations that no checker
clause constrains: halving `A` and doubling `m` is kernel-accepted (`mpDH_ahalf_check`), shrinking
`K` by 10⁶ is accepted by both Python checkers even with a floor present (C11 gets *weaker*), and
permuting the rows or negating every box is accepted. All four are harmless (each falsifies
H-ENCL, so the conclusion is vacuous), but the contract nowhere says so, and a reader may take
"the checker accepts" as evidence about the producer. **Proposed repair:** add to `FORMAT.md` §10:

> **What the checker cannot see (by design).** C1–C11 constrain only the integers in the file.
> They do **not** constrain `K` or `A` against the values they scale, nor the row↔segment
> correspondence: a transcript with a mis-scaled `K` or `A` (with `m` adjusted to match), with the
> rows permuted, or with every value box negated, is *accepted*. Each such transcript makes H-ENCL
> **false**, so the certified conclusion is vacuous rather than wrong — but the only detectors are
> the two-producer cross-check and the producers' own discipline, never the checker.

### MINOR-6 — `FORMAT.md` §0/§6.3 promise more than the shipped Lean theorem delivers

§0 and §6.3 step 5 say an accepted refutation transcript certifies "at least **m** zeros, counted
with multiplicity". `cert_of_checkW1` delivers `∃ ρ ∈ R°, ζ(ρ) = 0` — one zero, no multiplicity —
because H-AP is stated in consequence form. `Soundness.lean`'s header records this deferral
honestly ("the multiplicity-counting formalization is thereby deferred to v1.1, as §7.1 explicitly
permits"); `FORMAT.md` does not. **Proposed repair:** append to `FORMAT.md` §6.3 step 5:

> *(v1 scope: the Lean theorem `cert_of_checkW1` delivers the existential form — some ρ ∈ R° with
> ζ(ρ) = 0 and Re ρ > ½ — because H-AP is formalized in consequence form; the "at least m zeros
> with multiplicity" reading is the mathematical content of H-AP and is formalized at v1.1.)*

### INFO-1 — the schema's `mode ⟹ claimed_m` tie is enforced at C10, not at SHAPE

`w1-schema.json`'s third `allOf` ties `mode: "exclusion"` to `claimed_m: "0"`; neither Python
checker enforces it at the shape layer (both defer to C10, deliberately, so the §11 negative
control fails "at C10" as specified). So a file can be schema-invalid and be reported as
"REJECT at C10". Documented in `checker_ref.py:122–129`. No change needed; recorded so the two
readings are not confused.

### INFO-2 — two rounded figures in `acceptance-report.md` §5

"~0.7 s per segment evaluation at T = 10⁴" recomputes to 0.617 s (1564.7 s / 2 536 segment evals);
"both reference checkers verify the 983-segment t10000 transcript in ~0.03 s" recomputes to
0.005–0.008 s of check time (0.02–0.03 s including the JSON parse). Both are stated with "~" and
neither is load-bearing. No repair.

### INFO-3 — audit artifacts left in the Lean working tree

`Zeta23/W1/AuditO.lean` (the `#print axioms` scratch), `Zeta23/W1/AuditOCases.lean` (the ten
acceptance transcripts + two positive controls + eight corruptions as literals) and
`Zeta23/W1/AuditOFuzz.lean` (the 800-case differential batch) are **audit scratch**, not program
files, and were deliberately NOT copied into `rh-program/lean/Zeta23/`. The four throwaway modules
the resumed run used for the MAJOR-2 isolation experiments (`AuditORecDepth`, `AuditOCasesNoDepth`,
`AuditOCasesTmp`, `AuditODefOnly` — several contain deliberate errors) were **deleted** from the
working tree afterwards; no `.olean` of them remains. If the reconciler adopts
MAJOR-1's repair, `AuditOCases.lean` is the seed for `Zeta23/W1/Instances.lean`.

---

## 9. Scripts and outputs produced by this audit (all in `results/d1-m1/`)

| file | what it does | result |
|---|---|---|
| `audit_O_encl_honesty.py` / `.txt` | 395 fresh membership checks, 9 regimes, my own seed; κ identity | 0 failures |
| `audit_O_ball_largearg.py` / `.log` | 1 640 checks of `Ball.exp`/`iv.cos`/`iv.sin`/`pow_int_neg` at \|Im\| ≤ 2·10⁵ | 0 failures |
| `audit_O_corrupt.py` / `.txt` | 18 corruption classes × 5 accepted transcripts × 2 checkers | every intended corruption rejected at the intended check |
| `audit_O_lean_emit.py` | JSON transcript → Lean `W1Data` literal (the missing emitter) | generates `AuditOCases.lean` |
| `audit_O_lean_vs_py.py` / `.expect.json` | differential fuzz: Lean kernel `checkW1`/`checkW1Floor` vs `checker_ref.py` | 1 300 cases + 379 floor cases, full agreement |
| `audit_O_dh_winding.py` / `.txt` | from-scratch DH winding + H-ENCL spot test, unwrapping method | winding = 1.0 turns; 0 row violations |
| `audit_O_zeta_rows.py` / `.txt` | the same test for five ζ null transcripts | winding = 0; 0 row violations |
| `audit_O_report_check.py` / `.txt` | every printed figure in `acceptance-report.md` + `cost-curve.json` vs artifacts | all match |
| `audit_O_leancases_verify.py` / `.txt` | **(resumed run)** independent back-parse of `AuditOCases.lean` vs the JSON: 21 instances, 4 217 rows | 0 mismatches |

**No Session-8 file was modified.** (`git status` under `rh-program/results/d1-m1/` shows only
`audit_O_*` additions.)

---

## 10. Reproduction log (resumed run, 2026-09-02)

The first pass of this audit was killed by a usage limit after writing this report but before it
returned. The resumed pass re-executed everything and compared against the shipped logs.

| re-run | result |
|---|---|
| `audit_O_encl_honesty.py` | **byte-identical** to `audit_O_encl_honesty.log` except the wall-time line (10.9 s → 11.0 s); 395 checks, 0 failures |
| `audit_O_ball_largearg.py` / `.log` | 1 640 checks, 0 failures — reproduces §2 |
| `audit_O_corrupt.py` | **byte-identical** to `audit_O_corrupt.txt`. Exit status 1 is expected: the 2 flagged "MISMATCH" lines are a harness artifact — `mut_c9_m_big` sets `claimed_m := "1"` and `mode := "refutation"`, which on the two DH transcripts (already `m = 1`, refutation) is the **identity**, so ACCEPT is the correct verdict. Independently re-read the mutation source and confirmed. |
| `audit_O_report_check.py` | **byte-identical**. Exit 1 is expected: the 2 "mismatches" are the 3-significant-figure roundings 8.13195e−05 → "8.13e−05" and 7.63776e−06 → "7.64e−06" (INFO, §6) |
| `audit_O_dh_winding.py` | **byte-identical**; winding 1.0 turns, 0 row violations |
| `audit_O_zeta_rows.py` | **byte-identical**; winding 0, 0 row violations |
| both Python checkers × 12 acceptance transcripts | 8/8 null ACCEPT, 2/2 DH ACCEPT, 2/2 positive controls REJECT at C2 — reproduces `acceptance-report.md` §0/§1 exactly |
| `acceptance/crosscheck.py`, 4 pairs | overlaps 83 / 158 / 90 / 122, all CONSISTENT — reproduces §5 |
| `lake build Zeta23.W1.Soundness` | **exit 0, 3 142 jobs** |
| `lake env lean Zeta23/W1/AuditO.lean` | `#print axioms` block reproduced **line for line** (`propext, Classical.choice, Quot.sound`; no `sorryAx`) |
| `lake env lean Zeta23/W1/AuditOCases.lean` | 0 errors, 13.9 s — all 32 `decide +kernel` verdicts stand |
| `lake env lean Zeta23/W1/AuditOFuzz.lean` | 0 errors, 14.6 s — all 800 `checkW1` + 379 `checkW1Floor` differential cases stand; and the file's asserted verdicts were re-checked against `audit_O_lean_vs_py.expect.json` (800 + 379 assertions, **0 mismatches**), so the agreement is not self-referential |
| `audit_O_leancases_verify.py` | **new**: 21 instances, 4 217 rows, 0 literal mismatches (§3.3) |
| `c_sup` independent check | **new**: for n = 4, 10, 30, 42 the certified upper bound exceeds a 20 001-point dense sample of `sup\|B_n(x) − B_n\|` in every case (margin ≈ 1.2 %); `C_30 = 1.218048e9`, `\|B_30\| = 6.0158e8`, ratio 2.0247 — reproduces §1.2 |
| `maxRecDepth` isolation, experiments A/B/C | **overturned MAJOR-2's original diagnosis** — see the rewritten MAJOR-2 |

**Net effect on the verdict:** unchanged — 0 FATAL, 2 MAJOR. MAJOR-2's text, cause and proposed
repair are rewritten; its severity is retained because it blocks MAJOR-1's repair and forces an
M2a data-packaging decision, but its scope is narrower than first written and the `Checker.lean`
rewrite it proposed is withdrawn.

---

## 11. Gomila screen steps 3–4: what M1 v1 as built now clears

Reference: `results/d1-m0/gomila-screen.md` §4, steps 3 and 4; the screen's verdict is
**screen-open**, blocked on D1-side infrastructure. (Vocabulary, binding: the claim is unrefereed
and **NOT a record**; the bracket of record remains **0 ≤ Λ ≤ 0.2**.)

**Step 3 — "Format conversion + run `checkBarrier`": NOT CLEARED.** M1 v1 supplies the reusable
half — the enclosure convention is now fixed and exercised (integer `(lo, hi)` at a declared scale
`K`, **outward** rounding, exact-rational targets, all comparisons by cross-multiplication); the
modulus-excludes-0 scheme that `m2a-m2b-design.md` §4 left open is fixed and Lean-proved
(`FORMAT.md` §5.1 C6, `row_box_excludes_zero`); the winding-0 exclusion certificate that a barrier
t-slice *is* exists and is Lean-proved (`cert_of_checkW1`, `m = 0` branch); the integer-squares
modulus floor the t-interpolation gate consumes exists and is Lean-proved
(`floor_of_checkW1Floor`); and, from this audit, a working JSON→Lean literal emitter plus evidence
that kernel checking scales to ~1 300 rows (1.86 s, no raised `maxRecDepth`). What is still
missing is exactly: `Zeta23/W1/BarrierCert.lean` (`BarrierCertData`, `checkBarrier`,
`cert_of_check`) — design-note item (b), **not started, no file on disk**; the t-slice
Lipschitz/interpolation row and its soundness lemma; and a converter from the claim's printed
decimal balls to `BarrierCertData`. Settle MAJOR-2's **bulk-data representation** question before
writing `BarrierCertData`: kernel evaluation is not the bottleneck, but a single Lean list literal
of the claim's 3 149 013 rows is not viable, so the chunking/encoding choice belongs in the
structure's shape from the start.

**Step 4 — "Two-producer spot check (D1's own runs)": PARTIALLY CLEARED.** The *architecture* the
step needs is built, validated end-to-end, and re-run by me: two genuinely independent legs (no
shared module in either direction; different mathematics, not just different libraries), whole-
segment hull evaluation with adaptive bisection to C6, outward integer conversion, derivative-free
argument rows, honest stop-the-line aborts (exercised live in `producer-negative-controls.txt`),
and a cell-wise cross-check harness whose overlap counts I reproduced exactly (83/158/90/122, all
CONSISTENT). What is missing is the **target function**: both legs evaluate ζ and `f_DH` only,
and Gomila's certificates are about `f_t`/`H_t` (the Polymath15 Thm 1.3 effective A+B+C evaluator).
Neither leg implements it, so **not one Gomila mesh cell can be re-produced today**. M2a must add
design-note items (c) ~3–4 wk Arb-side and (d) ~2 wk mpmath-side on top of the M1 core.

**Net:** the screen stays **screen-open**, and the block remains D1-side, exactly as
`gomila-screen.md` §6 states. M2a must add, in order: the `f_t` evaluator on both legs (items c, d)
→ `BarrierCert.lean` + `checkBarrier` + soundness (item b, with MAJOR-2's data-packaging choice
   settled first)
→ the claim-format converter → `Instance02.lean` glue (item e) → comparator packaging (item f).
`Zeta23/DBN/Defs.lean` (item a) is done and clean.
