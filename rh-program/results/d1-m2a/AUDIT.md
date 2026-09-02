# M2a FINAL AUDIT (standing order 5) — everything built in Session 14 under `results/d1-m2a/` and `lean/Zeta23/DBN/`

**Date:** 2026-09-03 (Session 14, D1 M2a, workflow `d1-audit-m2a-s14`; adversarial final-audit agent, a different agent
from every builder). **Verdict: REPAIRED-CLEAN for what exists; the milestone itself is PARTIAL by its own honest
statement** — Lane B of the Λ ≤ 0.2 instance is kernel-checked from two independent producers, the theorem
`lambda_le_point2` is not proved (Lane A, `Defs.lean` v1.1 and L-B3 do not exist), and nothing about Λ changes:
**the bracket of record stays 0 ≤ Λ ≤ 0.2** (Rodgers–Tao; Platt–Trudgian Corollary 2, exact height 3 000 175 332 800).
**Fatals: 0.** Findings: 1 LOW defect repaired (a docstring transcription error that changes no number), 4 wording/record
items repaired by append-only errata, 5 observations recorded, 1 MEDIUM open item that is the milestone's cut line.

**Trust vocabulary (binding, D-R3/D-R8).** Everything accepted below is *"kernel-checked modulo the displayed
hypotheses H2-B and `hHol` (producers untrusted)"*. Never "fully machine-checked". The strict "Λ < 0.2" is never written.

**Inputs audited** (read from disk this session, in full unless a line range is given): `SPEC.md` v1.0 (all 1 175 lines),
`barrier-schema.json`, `barrier_ref_checker.py`, `checker_ref.py`, `checker_ref_controls.py`, `producer_arb.py` (docstring
lines 1–260 and `E_bound`, `ft_direct`, `log_gamma`, `N_of`), `ft_mp.py` (docstring lines 1–170, `alpha_ball`, `logM0_ball`,
`gamma_and_dt`, `check_N_constant`, `F_majorant`, `defect_bound`), `producer_mp.py` (`dt_bound`, `produce_prism` gate logic),
`arb-leg-notes.md`, `mp-leg-notes.md`, `lean-notes.md`, `INSTANCE-REPORT.md`, `row2_arith.log`, all run records named
below, `results/d1-m0/gomila-screen.md` §§4, 9, `results/d1-m0/m2a-m2b-design.md` §§1.6, 4, the D1 direction file's
"Current frontier", `results/d1-m1/RUN-REPORT.md` §§5–6; Lean: `Zeta23/DBN/BarrierCert.lean` (§§1–4 in full, §§11–12 in
full, the declaration index of the rest), `Zeta23/DBN/Defs.lean`, `Zeta23/W1/Checker.lean` (full), `W1/Soundness.lean`
lines 93–177, `Zeta23/DBN/Instance02.lean`, `Instance02/{Rect,mp_Barrier}.lean`, `Instance02/mp_0000.lean` (head and
tail); the transcripts' manifests and prisms 0/17/38 (mp), 0/40/71 (Arb) as data; Polymath15 (`fetched/p3-22a4`, PDF
page = printed page) pages 1–7, 19–21, 26–31, 38–42, 44–48, 64 by `pdftotext -layout`, and **pages 6 and 31 as page
images** (the overline in (14); the exponent of Prop. 6.6(iv)–(v)); Platt–Trudgian (`fetched/p3-22a1`) pages 2 and 5.

Every artifact this audit produced is in `results/d1-m2a/audit/` (scripts + run records; nothing here is a program file).

---

## 1. Task item (1): the effective-approximation error bound, re-derived from the on-disk paper, and both producers checked against it

### 1.1 What Theorem 1.3 says and where it is valid (P15 p3, p6, p30–31; quoted in SPEC §2, re-read here)

* **Validity region — exactly (5), p3:** `0 < t ≤ 1/2; 0 ≤ y ≤ 1; x ≥ 200`. Theorem 1.3 (p6) is stated "Let t, x, y lie in the
  region (5)"; its proof reduces to Corollary 6.4 (p29: "Let t, x, y obey (5)") and Proposition 6.6 (p31: "Let the notation
  and hypotheses be as above"). **No other range condition exists** in the statement: the constants 0.626, 6.66, 3.58,
  8.52, 1.24, 0.125, 6.92, 0.02 and the shape of N = ⌊√(x/4π + t/16)⌋ (19) are unconditional inside (5).
* **The instance box** R × [0, t₀] = [X, X+1] × [16733/100000, 1] × [0, 93/500] with X = 5 000 000 194 858 lies in (5)
  except for the single endpoint t = 0 (region (5) is open at t = 0). Both producers handle t = 0 by the limit argument
  (SPEC P-7; `producer_arb.py` D-A12, `ft_mp.py` D-F9), recorded in prism 0's `producer.comment` of each leg. **The
  argument was re-derived here and is valid:** for fixed z with |Im z| ≤ 1, |e^{tu²}Φ(u)cos(zu)| ≤ e^{u²/2}|Φ(u)|e^{u}
  for 0 < t ≤ 1/2 (|cos(x+iy)u| ≤ cosh(yu) ≤ e^{|y|u}), and Φ(u) = O(exp(−πe^{4u})) (P15 (3), p1) makes the dominant
  integrable, so H_t(z) → H_0(z); B_t(z) = M_t(s₊) → M_0(s₊) = B_0(z) ≠ 0 by continuity of (10) in t; f_t → f_0 is a
  finite sum continuous in t; the majorants of Prop. 6.6(iv)–(vi) are continuous in t at 0. Passing to the limit in
  |H_t/B_t − f_t| ≤ E(t) gives |H_0/B_0 − f_0| ≤ E(0). Both legs' seam-0 E is ≥ E(0) (the mp leg evaluates the majorant
  at t = 0 exactly; the Arb leg over the t-ball [0, t₀], which is larger). ✓
* **N constancy** (the holomorphy of f on R, p6): `row2_arith.log` brackets √(x/4π + t/16) ∈ [630783.14279635, 630783.14279643]
  at all four corners (mpmath intervals), monotone in x and t, so N ≡ N₀ = 630 783 on the closed box; both legs
  re-verify it by directed rounding (D-A13, D-F3). The mp leg's D-F4 additionally needs N₀² ≤ x₁/(4π): 630783² =
  397 887 193 089 against x₁/(4π) = 397 887 357 3xx — holds with margin ≈ 1.6·10⁵ and is checked by `check_N_constant`. ✓
* **Validation points of both legs** (arb-leg-notes §4: x ∈ {200, 1000, 3000, 10⁴}, t ∈ {0, 1/20, 93/500, 1/5},
  y ∈ {y₀, ½, 1}; mp-leg-notes §4: x ∈ [200, 330], y ∈ [0, 1], t ∈ (0, 0.5]) all lie in (5) or at its t = 0 limit
  (x = 200 is inside: (5) is x ≥ 200). **No producer was used outside Theorem 1.3's range.** The mp leg's `defect_bound`
  guards region (5) explicitly (`raise ValueError("defect_bound: box outside region (5)")`, allowing t ≥ 0 per D-F9);
  the Arb leg's `E_bound` has no guard, but its only call sites are the row-2 box and the validation points above.

### 1.2 The majorant, constant by constant (Prop. 6.6, p31, page image), and the two implementations

| quantity | paper (p31; (84) p40) | `ft_mp.py` `defect_bound` | `producer_arb.py` `E_bound` | verdict |
|---|---|---|---|---|
| (i) \|γ\| ≤ e^{0.02y}(x/4π)^{−y/2} | ✓ | used in D-F4 as \|γ\|n^y ≤ e^{0.02y} (n ≤ N ≤ √(x/4π)) | used in D-A3 (`pref_m = e^{0.02}(x₁/4π)^{−y₁/2}`) | both valid derivations (§1.3) |
| (iii) \|κ\| ≤ ty/(2(x−6)) | ✓ | `kap = t y/(2(x−6))` | `kap = tb*yb/(2*(xb-6))` | ✓ |
| (iv),(v) exponent ((t²/16)log²(x/(4πn²)) + 0.626)/(x − 6.66) | **n² in the page image** | docstring said `x/(4πn)` — **F-1**; code uses δ₁ of (84) (n = 1 case) | docstring n² ✓; code uses δ₁ | bound valid either way (§1.3) |
| δ₁ = ((t²/16)log²(x/4π) + 0.626)/(x − 6.66), (84) p40 | ✓ | `Fraction(626,1000)`, `Fraction(666,100)` ✓ | `arb("0.626")`, `arb("6.66")` ✓ | ✓ |
| (vi) e_{C,0} ≤ (x/4π)^{−(1+y)/4} exp(−(t/16)log²(x/4π) + (3\|log(x/4π)+iπ/2\| + 3.58)/(x − 8.52))·(1 + 1.24(3^y+3^{−y})/(N − 0.125) + 6.92/(x − 12)) | ✓ | as printed: 3.58, 8.52, 1.24, 1/8, 6.92 ✓ | the SPEC D-2.4 10.50 form: `(3·mod + 21/2)/(x − 12)`, `(1 + 1.24(3^y+3^{−y})/(N − 1/8))` ✓ | ✓; **D-2.4 re-derived here**: (1+a+b) ≤ (1+a)e^b for a, b ≥ 0 and 1/(x−8.52) ≤ 1/(x−12) for x > 12 — sound; the displayed 10.44 of (24) is NOT implied by (vi) and is used by neither leg ✓ |
| F_{N,t}(σ) majorant | (83) + integral test (p41) | D-F5: 1 + (N^{1−ρ}−1)/(1−ρ), ρ = σ − (t/4)log N, lower endpoint of ρ | D-A3/D-A9 R_k^±(t) sums with the box inf of Re α, monotone in t iff log N ≤ 2·inf Re α (checked: 13.35 vs 26.7) | ✓ both re-derived |

### 1.3 Two derivation details re-checked (the only places the legs go beyond the paper's displays)

* **The n-dependent exponent majorized by δ₁.** Needs |log(x/(4πn²))| ≤ log(x/4π) for 1 ≤ n ≤ N, i.e. 4π/x ≤ x/(4πn²) ≤ x/4π.
  The right inequality is n ≥ 1; the left is n² ≤ x²/(16π²), implied by n² ≤ N² ≤ x/(4π) + 1/32 < x²/(16π²) for x ≥ 200.
  Valid. (Under the mp docstring's mistaken reading `x/(4πn)` the same chain also holds — which is why F-1 changes nothing.)
* **The e_A factor.** From (iv), |γ| n^y n^{−Re s*} enters. mp: |γ|n^y ≤ e^{0.02y}(n/√(x/4π))^y ≤ e^{0.02y} (n ≤ N ≤ √(x/4π)),
  then N^{|κ|} ≤ N^{ty/(2(x−6))} by (iii); e_A + e_B ≤ (e^{δ₁} − 1)(1 + e^{0.02y}N^{|κ|})F(σ) with σ ≤ Re s* ✓ (F non-increasing
  in σ). Arb: n^{y − Re s*} = n^{−Re s** + Re κ} ≤ n^{−Re s**}N^{|κ|} with Re s** = Re s* − y + Re κ (p46, with the overline),
  so e_A ≤ (e^{δ₁} − 1)N^{2|κ|}·|γ|Σ b_n n^{−Re s**} ✓. Both are valid; the Arb form is the cruder (N^{2|κ|}, and R₀⁻ with
  the box infimum of Re α), which is why its e_A + e_B at seam 0 is 4.7·10⁻¹⁰ against the mp leg's 1.6·10⁻¹⁰ — both
  ≥ the true pointwise 1.3·10⁻¹⁰ (§1.4). Immaterial: e_{C,0} dominates by 10⁶.
* **The displacement D.** mp (D-F7): D/K = E_prism + Δt·DT + E_seam with DT ≥ sup_{∂R×[τ,τ′]}|∂_t f| from the evaluator
  with t an interval — |g_t − g_τ| ≤ |g_t − f_t| + |f_t − f_τ| + |f_τ − g_τ| and the mean-value inequality in t ✓.
  Arb (D-A15′): D/K = 2E_p + Δ·Mt, Mt ≥ |f_t(z_m,τ)| + h·sup_seg|f_zt(·,τ)| + Δ·sup_{seg×prism}|f_tt| — a mean-value bound along the
  segment then in t ✓. Neither leg uses Lemma 8.4's printed majorants (p46); both bound ∂_t f from their own rigorous
  evaluators, which their validation sections test against finite differences and the analytic D-F6 pipeline
  (mp: `dt0_recheck.py`, 12/12; Arb: section D, 46/46). Accepted as producer-side evidence; not a proof (H2-B stays displayed).

### 1.4 Independent recomputation of the paper's pointwise majorant at box corners (`audit/audit_E_corners.py`, record `audit-E-corners.txt`)

Own code, python-flint `arb` at 200 bits, the EXACT Dirichlet sums (630 783 terms each, no majorant), (iv)/(v) with the
printed n² exponent, (vi) as printed, in the 10.50 form, and with the displayed 10.44:

| corner (x, y, t) | e_A | e_B | e_{C,0} (printed / 10.50 / 10.44) | total (10.50 form) | the legs' E at that seam | E ≥ corner? |
|---|---|---|---|---|---|---|
| (X, y₀, 0) | 5.572·10⁻¹¹ | 7.790·10⁻¹¹ | 4.1192176·10⁻⁴ (all three agree to 8 digits) | **4.119218898·10⁻⁴** | mp 4.11923370·10⁻⁴, Arb 4.11923734·10⁻⁴ | ✓ both (slack 1.5·10⁻¹¹ / 5.2·10⁻¹¹) |
| (X+1, y₀, 0) | same to 5 digits | same | same | 4.119218898·10⁻⁴ | same | ✓ |
| (X, 1, 0) | 1.25·10⁻¹³ | 1.74·10⁻¹² | 1.5853413·10⁻⁶ | 1.585343·10⁻⁶ | (worst corner is y₀, not 1 — the sup is at y₀ as SPEC §5.2 says) | n/a |
| (X, y₀, 637/25000) | 1.87·10⁻¹¹ | 2.72·10⁻¹¹ | 1.3225788·10⁻⁴ | **1.3225792·10⁻⁴** | mp prism 17: 1.32258409·10⁻⁴ | ✓ (slack 4.9·10⁻¹¹) |
| (X, y₀, 3719/20000) | 1.22·10⁻¹³ | 8.36·10⁻¹³ | 1.0329757·10⁻⁷ | **1.0329853·10⁻⁷** | mp prism 38: 1.0330282·10⁻⁷ | ✓ (slack 4.3·10⁻¹²) |
| (X, y₀, 93/500) | 1.22·10⁻¹³ | 8.36·10⁻¹³ | 1.0306754·10⁻⁷ | 1.0306850·10⁻⁷ | (t₀ itself is not a seam) | n/a |

Every producer E dominates the paper's pointwise majorant at the corner it is a sup of, with relative slack ≤ 1.3·10⁻⁷:
**the E rows are correct and tight**; the 10.44/10.50/printed-(vi) distinction is invisible at this x (as SPEC D-2.4 says).
Also confirmed en route: |γ| = 0.107030 = e^{0.02y₀}(x/4π)^{−y₀/2} to within 3 %, Re s* = 0.583665 at t = 0 (= (1+y₀)/2 exactly),
|κ| ≤ 3.2·10⁻¹⁵ at t₀ against (iii)'s 3.1·10⁻¹⁵ — consistent.

### 1.5 Two paper-internal wrinkles, recorded (affect nothing)

* (14) as printed carries an overline on s_* in the second sum (page image of p6); `pdftotext` drops it, so SPEC §2.3 quotes
  `n^{s*+κ}`. Both legs implement the overline reading (= (92)); so does this audit's direct evaluator (§2), which
  contains every transcript box it was tested against — that is the strongest available evidence that the reading is
  the paper's. **Repaired:** SPEC §14 erratum 1 (append-only).
* (21) on p6 has `4y(1+y)/x²` where Prop. 6.6(ii) on p31 has `8y(1−y)/x²`. Neither producer uses either display (both
  enclose Re s_* from (17) directly). SPEC §14 erratum 2.

---

## 2. Task item (2): enclosure honesty at FRESH points, both legs, against direct evaluation (`audit/audit_direct.py`, record `audit-direct-run.txt`)

**Method.** An independent evaluator of f_τ — P15 (92) term by term, N₀ = 630 783 terms per sum, α from (9), log M₀ from (7),
γ = exp(log M₀(s₋) − log M₀(s₊) + (t/4)(α(s₋)² − α(s₊)²)) — in python-flint `acb` balls at 256 bits (1.6 s per point; ball radii
10⁻⁶⁰…10⁻⁶⁵), no code from any producer. Per chosen segment: the two endpoints and the interior point at parameter 0.37
(fresh: no producer evaluates there) are checked against the row's value box at scale K and the floor Fn/Fd; the argument
row is checked against A·Arg(f(w)/f(z))/2π — valid because C-B6 puts the segment's image in an open half-plane missing 0,
where the continuous argument increment equals the principal Arg of the endpoint ratio. All comparisons are certain ball
comparisons (`arb.__le__` is true only when every point of one ball is ≤ every point of the other).

**Result: 36 points and 12 argument rows across 6 prisms of BOTH legs — 0 failures.**

| prism | seam τ | segments (edge) | value boxes (K) | floor | argument rows (A) |
|---|---|---|---|---|---|
| mp 0 | 0 | 23 (bottom), 160 (left) | 6/6 contained | 6/6 | 2/2: e.g. row [14875846886, 14875846887] ∋ 14875846886.2121 |
| mp 17 | 637/25000 | 7 (bottom), 63 (right), 113 (top), 172 (left) | 12/12 | 12/12 | 4/4 |
| mp 38 | 3719/20000 | 40 (bottom), 150 (left) | 6/6 | 6/6 | 2/2: [3969408213, 3969408215] ∋ 3969408214.042 |
| Arb 0 | 0 | 137 (bottom), 240 (top) | 6/6 | 6/6 | 2/2: [2690, 2691] ∋ 2690.617 |
| Arb 40 | 58593521/10⁹ | 11, 70, 90, 110 (one per edge) | 12/12 | 12/12 | 4/4 |
| Arb 71 | 87737923/(5·10⁸) | 3 (bottom), 50 (left) | 6/6 | 6/6 | 2/2: [−519, −518] ∋ −518.208 |

The mp leg's argument rows are 1–2 units wide at A = 10¹² (10⁻¹² turn) and the direct values land inside every one — a
sharp test of that leg's thin-point evaluations; the Arb leg's rows are 1 unit wide at A = 10⁶. This is producer-side
evidence for the row half of H2-B on both legs (the E and D halves rest on §1); H2-B stays displayed.

---

## 3. Task item (3): corrupted transcripts must be rejected — by `checker_ref.py`, by `barrier_ref_checker.py`, and by the Lean kernel

**JSON level** (`audit/audit_json_corrupt.py`, record `audit-json-corrupt-run.txt`; copies of the real row-2 transcripts):

| mutation | clause | `checker_ref.py` | `barrier_ref_checker.py` |
|---|---|---|---|
| mp prism 17 row 7 box := [−1, 1]² | C-B6 | REJECT C-B6 row 7 | REJECT C-B6 row 7 |
| mp prism 17 E := Fn (Fd = K) | C-B12 | REJECT C-B12 | REJECT C-B12 |
| Arb prism 40 bottom[5] := bottom[4] | C-B3 | REJECT C-B3 bottom walk | REJECT C-B3 not strictly monotone |
| Arb prism 40 Fn := 10·Fn | C-B11 | REJECT C-B11 row 0 | REJECT C-B11 row 0 |
| mp manifest t₀ := 3719/20000 (= last seam) | C-B13 | REJECT C-B13 | REJECT C-B13 last seam not < t₀ |
| Arb manifest first prism dropped | C-B13 | REJECT C-B13 first seam ≠ 0 | REJECT C-B13 first seam ≠ 0 |
| mp prism 17 seam := 1/2 (manifest unchanged) | manifest/prism consistency | SHAPE ERROR (exit 2) | REJECT seam mismatch |
| mp prism 17 rows rotated by one | (checker-blind by design, SPEC P-11) | ACCEPT | ACCEPT |

The last row is the documented blindness (the checker cannot see row↔segment alignment; only the two-producer
cross-check can, FORMAT.md §8.1 / SPEC P-11) — it is why the cell-wise cross-check of §5 is mandatory, and it did run.

**Lean kernel** (`audit/audit-corrupt-scratch.lean`, `lake env lean` against the built Instance02 modules, record
`audit-lean-corrupt-run.txt`): eleven corrupted literals built from the real `mp0017`, `arb0040`, `row2BarrierMP`,
`row2BarrierARB` by `List.set`/`List.map`/`tail`/structure update, each proved **`= false` by `decide +kernel`** (axioms
`[propext]` or none): C-B6 box straddling 0; C-B12 E := Fn; C-B3 breakpoint moved; C-B11 floor ×10; C-B9 every argument
row shifted by +1 (S_lo = −108 + 184 > 0); C-B4 one row deleted; C-B13 t₀ lowered to the last seam; C-B13 first prism
dropped; C-B13 two prisms swapped; C-B2′ degenerate rectangle x₂ := x₁ (both the chain and a per-prism check reject).
The untouched `mp0017`, `arb0040` re-verify `= true` in the same file. **Harness control:** the deliberately false claim
`checkPrism row2Rect audit_bad_E = true` is refused by the kernel ("(kernel) application type mismatch") — the run is
meaningful, not a no-op. Whole file: 2.9 s.

---

## 4. Task item (4): the Lean predicate, `checker_ref.py`, `barrier_ref_checker.py` and SPEC §7.3, clause by clause

| SPEC §7.3 | `BarrierCert.lean` | `checker_ref.py` | `barrier_ref_checker.py` | match |
|---|---|---|---|---|
| C-B0 K ≥ 1, A ≥ 1, rectangle denominators ≥ 1, mesh denominators ≥ 1 | `checkPrismW1`: `1 ≤ w.K`, `1 ≤ w.A`, `1 ≤ q1,q2,b1,b2`, `densPos` ×4 | `check_prism_w1` same order | `check_prism` (K, A `POS` regex + `>= 1`), mesh `>= 1`; rectangle/t₀ in `check_barrier` | ✓ |
| C-B0 seam td ≥ 1, tn ≥ 0; Fn ≥ 0, Fd ≥ 1; E ≥ 0, D ≥ 0 | `checkPrism`: `1 ≤ p.td`, `0 ≤ p.tn`, `0 ≤ p.Fn`, `1 ≤ p.Fd`, `0 ≤ p.E`, `0 ≤ p.D` | `check_prism` same | `NAT`/`POS` regexes + `req` | ✓ |
| C-B2′ x₁ < x₂, y₁ < y₂ (cross-multiplied); y₁ > 0; t₀ > 0 (global) | `checkPrismW1` (x, y strict) AND `checkBarrierChain` (x, y strict, `0 < yn1`, `0 < t0n`, `1 ≤ t0d`) | both places, same | `check_barrier` | ✓ |
| C-B3 four edge walks | `W1.edgeOK` ×4 (≥ 2 points, `firstOK`, `lastOK`, `chainLt`/`chainGt`) | `edge_ok` (Fractions; denominators verified first) | `edge_ok` (cross-multiplied) | ✓ |
| C-B4 \|rows\| + 4 = Σ\|edge\| | `decide (w.rows.length + 4 = …)` | same | `len(rows) == Σ(len − 1)` | ✓ |
| C-B5, C-B6, C-B7 per row | `W1.rowsOK w.A` (`rowOK`: C5 ∧ C6 ∧ C7) | `row_ok` | inline `req` ×3 | ✓ |
| C-B8 2(S_hi − S_lo) < A | `decide (2 * (sumArgHi − sumArgLo) < w.A)` | same | same | ✓ |
| C-B9 S_lo ≤ 0 ≤ S_hi | `sumArgLo ≤ 0 ∧ 0 ≤ sumArgHi` (`m = 0` by `toW1`) | same | same | ✓ |
| C-B11 (mre² + mim²)Fd² ≥ Fn²K² | `W1.floorRowsOK p.K p.Fn p.Fd p.rows` (`mdist` = 0 iff the interval contains 0) | `floor_row_ok`/`mdist` | inline | ✓ |
| C-B12 (E + D)·Fd < Fn·K | `decide ((p.E + p.D) * p.Fd < p.Fn * p.K)` | same | same | ✓ |
| C-B13 first seam = 0; strictly increasing; last < t₀ | `densPos (seams d)`, `firstOK (0,1) (seams d)`, `chainLt (seams d ++ [(t0n, t0d)])` (empty list → `firstOK` false) | `first_ok`, `chain_lt(seams + [t0])` | `seams[0][0] == 0`, pairwise `lt`, `lt(last, t0)`, `len ≥ 1` | ✓ |
| manifest seam = prism seam | (one copy in the Lean data) | `Shape` error | `req` REJECT | ✓ (JSON-only) |

The Lean `checkBarrier = checkBarrierChain && prisms.all (checkPrism rect)` is mirrored by `check_barrier`. **H2-B
(`PrismEnclOK`, `BarrierEnclOK`) and the theorem statements `cert_of_checkBarrier`, `cert_of_checkBarrier_xy` are
verbatim the SPEC §8.1/§8.3 shapes** (compared line by line). The soundness proof consumes only `firstOK (0,1)` from
C-B13 (`seamTime_head_eq_zero`) and walks the `Forall₂` of H2-B (`cover_prisms`); C-B13's monotonicity and "last < t₀"
are reject-more checks — exactly as `lean-notes.md` §6 records. `W1/` is unmodified (git: last change at the license
commit `5655bc0`); `Defs.lean` is unchanged v1.0 (same commit). The `PrismEnclOK` E/D clauses are stated on ∂R only,
as SPEC §4.1 says; the row clause reuses `W1.RowEnclOK`/`W1.segs` unchanged.

---

## 5. Task item (5): every claim of `INSTANCE-REPORT.md` and the Gomila addendum (`gomila-screen.md` §9) against the artifacts

| claim | artifact | recomputed here | verdict |
|---|---|---|---|
| mp chain 39 prisms / 7 176 rows, seams 0 … 3719/20000 < 93/500; Arb 72 / 10 771 | manifests + `checker-ref-run.txt` | counted from the JSON: 39×184 = 7 176; 10 771 | ✓ |
| `checker_ref.py` ACCEPT on row2, row2-arb, mini, mini-arb, SPEC §12 | `checker-ref-run.txt` | five ACCEPT lines, exit 0 | ✓ |
| 21/21 controls, three control data wrong (checker right) | `checker-ref-controls-run.txt` | 21 lines "[as expected]" | ✓ |
| cross-check A: 39 seams, 13 729 pairs, 0 disjoint; B: 72 seams, 23 443 pairs, 0 disjoint; 111 seams, 37 172 pairs | `xcheck-*-run.txt` tails | 13 729 + 23 443 = 37 172; 39 + 72 = 111 | ✓ |
| E identical to all printed digits at every seam | same files | spot rows show 4.4704e-06/4.4704e-06 etc.; one seam in B differs in the 5th digit (6.7812e-07 vs 6.7813e-07) | ✓ (to the printed 4–5 digits; "all printed digits" is a hair strong) |
| back-parse 0 mismatches on 17 947 rows | `verify-lean-{mp,arb}-run.txt` | + this audit's own back-parse of `mp_0017`, `arb_0040`, `mp_0038` and both `_Barrier` prism lists: IDENTICAL (`audit-backparse.txt`) | ✓ |
| 116 modules, 23 965 lines | `lean/Zeta23/DBN/Instance02*` | 114 files in `Instance02/` + `Instance02.lean` = 115 files … the report's "116" counts `Rect` + 39 + 72 + 2 `_Barrier` + top = 115; **off by one** | ✓ lines (23 965 exactly); module count 115, not 116 (F-4) |
| serial builds 157 s (mp, 41 modules) / 217 s (Arb, 73) | `instance02-build.log` | log sums: mp 147.1 s for 40 modules + 3 s `mp_Barrier` (fixed) ≈ 150 s; Arb "total 217 s" as logged; clean rebuild 137 s / 237 s | ✓ within the report's rounding (F-4) |
| monolithic `decide +kernel` 28.2 s for 17 947 rows "≈ 1.4 ms/row" | `kernel-time.log` | 28.18/17 947 = **1.57 ms/row** wall; 1.4 nets out import loading, not stated | wording (F-4) |
| `#print axioms`: chains none; every `_check` and `_prisms` `[propext]`; monolithic `[propext, Quot.sound]`; theorems three standard | `instance02-axioms.log` (2 of 111 per-prism theorems printed) | **all 111** per-prism theorems printed this audit: 111 × `[propext]` (`audit/instance02-axioms-all.log`); the rest as claimed | ✓ (claim was justified transitively; now direct) |
| thermal breach ≈ 4 min, clean rebuild | `instance02-build.log` | log records the overlap and the clean rebuild 01:01–01:07 | ✓ honest |
| Gomila: main @ a74738d, log SHA-256 2d010f70…05f4 = `SHA256SUMS` | `~/rh-lean-work/gomila-ap/main-a74738d` | `git rev-parse HEAD` = a74738d…; `shasum -a 256` = 2d010f70…05f4; `SHA256SUMS` line matches | ✓ |
| 883 prisms, 0 replay failures, chain continuous/increasing from exactly 0, last ball ∋ 129/800; min margin 0.519850 at 882; min floor M − spatial 1.011949 at 883 | `gomila/gomila-scalars.json` | independent replay (`audit_gomila_stats.py`): 0 prisms differ from the record's `gate_replay_margin`/`cb12_floor` by > 10⁻⁹; min margin 0.519850 @ 882; min floor 1.011949 @ 883; first seam 0; increasing; last < t₀; continuity; t_hi(883) ∋ 129/800; all winding balls ⊂ (−¼, ¼) | ✓ |
| prism 1 gate: 4.278362 − 0.500052 − 52726·3.5818·10⁻⁵ − 0.00125 = 1.888530 | replay line 1 | 1.888530 (printed 1.888530…) | ✓ |
| sample = 10 thinnest (873–882) + 19 evenly spaced = 29; all relative margins in [0.332, 0.44] below 2× median 0.425 | `spot-sample.json`, scalars | thinnest ten = 873…882; min 0.3317, max 0.4414, median 0.4255, all < 2·median; sampled list = {1, 50, …, 850, 883} ∪ {873…882} | ✓ |
| spot: 8 198 pairs, 0 disjoint; 0 contradictions; DT ratio 0.019–0.30; gate at their Δt ok on 29/29 | `gomila/spot-compare-run.txt` | column sums: 8 198 pairs over 29 prisms; ratios 0.019…0.297; all "ok,ok" | ✓ |
| "hull floors 1–5 % below their point floors" | same | prism 1: 4.2 % (Arb) / 1.25 % (mp); prism 883: 0.58 % / 0.12 % | ✓ in spirit (0.1–5 %) |
| PT pairing: t₀ + y₀²/2 = 3999993289/2·10¹⁰ = 0.19999966445 ≤ 1/5, slack 6711/2·10¹⁰; X/2 = 2 500 000 097 429; PT − X/2 = 500 175 235 371; 2.51·10¹² − X/2 = 9 999 902 571; (1+y₀)/2 = 116733/200000; 58367/100000 is a round-UP; 1 − 2t₀ = 157/250; yA = 3962323/5·10⁶ satisfies C-A1 | `row2_arith.log` | **recomputed exactly with `fractions.Fraction`: every value identical**; PT footnote 2 (p5) "X in Table 1 corresponds to 2H" confirms X/2 = H; PT Theorem 1's exact height read from p2 | ✓ |

---

## 6. Task item (6): axioms and the grep

* `grep -rn -w "sorry\|admit\|native_decide\|sorryAx\|ofReduceBool"` over `rh-program/lean` (128 `.lean` files): **every hit
  is inside a comment or docstring** ("all sorry-free", "no `native_decide`") — no proof term, no `sorry`, no `admit`,
  no `native_decide` anywhere, including all 115 Instance02 modules.
* `#print axioms`: `barriercert-axioms.log` — 28 declarations, all ⊆ `[propext, Classical.choice, Quot.sound]`;
  `instance02-axioms.log` + `audit/instance02-axioms-all.log` — chains: no axioms; **111/111** per-prism `_check` and both
  `_prisms`: `[propext]`; both monolithic `_check`: `[propext, Quot.sound]`; the four instantiated theorems: the three
  standard axioms. No `sorryAx`, no `Lean.ofReduceBool` in any output.
* Program tree ↔ working tree: `cmp` over every program `.lean` file: **byte-identical** (the working tree additionally
  holds upstream `PairCeiling/*` and the M1 audit scratch `W1/AuditO*.lean`, as documented).

---

## 7. Findings, severities, repairs

| id | severity | finding | repair |
|---|---|---|---|
| **F-1** | LOW (record defect; no number affected) | `ft_mp.py` docstring transcribed Prop. 6.6(iv)/(v) with `log²(x/(4πn))`; the page has `log²(x/(4πn²))`. `mp-leg-notes.md` §6 item 9 called the transcription exact. The code majorizes the exponent by δ₁, valid under either reading (§1.3); every emitted E ≥ the paper's pointwise majorant (§1.4). | **APPLIED:** docstring corrected in place with a dated audit note (lines 42–47, 81–82); erratum §8 appended to `mp-leg-notes.md`. |
| **F-2** | LOW (wording) | SPEC §2.3 quotes (14) without the overline on s_* (pdftotext artifact); both legs and this audit's evaluator use the overline reading. | **APPLIED:** SPEC §14 erratum 1 (append-only). |
| **F-3** | INFO | P15 (21) vs Prop. 6.6(ii): `4y(1+y)` vs `8y(1−y)`; unused by both legs. | SPEC §14 erratum 2. |
| **F-4** | LOW (wording in `INSTANCE-REPORT.md`) | "116 modules" (115); "≈ 1.4 ms/row" (1.57 ms/row wall); "157 s" (≈ 150 s by the log); "E identical to all printed digits" (one seam differs in the 5th digit); "1–5 % below" (0.1–5 %). | Not edited (the report is a dated record); corrected here and in `RUN-REPORT.md`. |
| **F-5** | **MEDIUM — the cut line (open by design, correctly labeled everywhere)** | `lambda_le_point2` is not proved: `Defs.lean` v1.1 (`Polymath15Bridge'`, `Bt`, `HtEntire`), L-B3, Lane A (`checkAsym`, `cert_of_checkAsym`, a Lane-A transcript from either producer, Lemma T's constants) and the glue L-G do not exist. The instance theorems are generic in G. **Nothing about Λ is certified by M2a today.** | **DEMANDED:** the ordered next steps in `RUN-REPORT.md` §6; no public sentence may say more than "Lane B of the Λ ≤ 0.2 instance is kernel-checked modulo H2-B and hHol". |
| **F-6** | LOW (observation) | The Arb chain runs the integer gate C-B12 at (E+D)/floor up to **0.995** (prism 10: 0.9947; prisms 69, 70 ≈ 0.99), the mp chain ≤ 0.540. Sound (the gate is strict and kernel-checked; the slack lives inside the conservative majorant Mt), but `arb-leg-notes.md` D-A11's "holds with a margin" describes the float pre-check, not the integer gate. | Recorded; no change. A v1.1 producer should record its target θ as the mp leg does. |
| **F-7** | LOW (wording) | The schema's `trust_label` constant is the full-certificate label (H1, H2, H3); a barrier-lane transcript alone is kernel-checked modulo H2-B and `hHol`. | SPEC §14 erratum 4; per-lane label for a v1.1 schema. |
| **F-8** | INFO | `instance02-axioms.log` printed 2 of 111 per-prism theorems (the claim was justified transitively through `_prisms`). | **APPLIED:** all 111 printed, `audit/instance02-axioms-all.log`. |
| **F-9** | INFO | Thermal-policy breach of ≈ 4 min (three heavy processes) during the Arb module builds, self-reported and remedied by a clean rebuild. | None needed; the honest record stands. |
| **F-10** | INFO | The row-rotation blindness of the checker (§3, mutation (g)) is real and documented; the cell-wise cross-check that detects it ran on every seam of both chains (37 172 pairs). | None. |

**No FATAL finding.** Specifically: no producer was used outside Theorem 1.3's region (5) except at its t = 0 limit,
which is handled by a valid, recorded limit argument; every constant of the majorant is transcribed correctly in the
CODE of both legs (the one docstring slip is F-1); the two E implementations are ≥ the paper's pointwise majorant
wherever tested; the rows contain independent direct evaluations at every fresh point tested; corrupted transcripts
are rejected by all three checkers; the Lean predicate is the SPEC clause for clause; the theorems carry only the three
standard axioms; the Gomila numbers replay exactly; the PT pairing arithmetic is exact.

---

## 8. Verification ledger (standing order 5)

Derived in this audit (checkable above): the region-(5) validity of Theorem 1.3 and the t = 0 limit (§1.1); D-2.4 (§1.2);
the δ₁ majorization and the e_A factor on both legs (§1.3); the half-plane argument-increment identity used by §2.
Recomputed with independent code: the paper's pointwise majorant at six corners (200-bit balls, exact sums; §1.4);
f_τ at 36 fresh boundary points and 12 argument increments (256-bit balls; §2); the Gomila gate replay on 883 prisms
(exact `Fraction`; §5); the PT pairing arithmetic (exact `Fraction`; §5); the back-parse of three emitted modules and
both prism lists (§5). Kernel-checked this audit: 11 rejections of corrupted literals + 2 re-acceptances + 1 refused
false claim (§3); `#print axioms` on 119 Instance02 declarations (§6). Read from the page images: (14)'s overline (p6),
Prop. 6.6(iv)–(vi) (p31). Not verified: the analytic content of H2-B beyond the tests above (it is displayed); Gomila's
per-prism rows (they do not exist); the published Polymath15 page numbers (not on disk).

Files written by this audit: `AUDIT.md`, `RUN-REPORT.md`, `audit/` (8 scripts/scratch + 8 run records + the full axioms
log), the F-1 docstring correction in `ft_mp.py`, `mp-leg-notes.md` §8, `SPEC.md` §14. No program Lean file was touched.
