# mpmath-ball f_t / H_t producer leg (M2a item (d)) — build record, derivation map, validation, run record, cut lines

**Status:** built, validated and run 2026-09-02 (Session 14, D1 M2a; workflow `d1-audit-m2a-s14`, item (d)).
**Trust language (binding, D-R3/D-R8; SPEC.md §0):** everything in this leg is UNTRUSTED producer-side work by
design. An accepted transcript is "kernel-checked modulo the displayed hypotheses" (H1, H2 = H2-B here, H3) once
the Lean checker of the M2a Lean stream lands; today's acceptances are by the untrusted reference checker
`barrier_ref_checker.py` only. Nothing here is "fully machine-checked". The Λ bracket of record is 0 ≤ Λ ≤ 0.2
(never "Λ < 0.2").

## 1. What was built (files in this directory)

| component | file | status |
|---|---|---|
| f_t evaluator layer on the M1 ball core (`../d1-m1/ball.py`, imported; no code shared with the Arb leg) | `ft_mp.py` | DONE — module docstring carries every transcribed formula at PDF page and the derivations D-F1…D-F9 |
| stored-moment computation (block-Taylor, D-F8) | `ft_mp.py moments` → `moments/row2-{plus,minus}.json` (and `mini-*`) | DONE — N₀ = 630783, 20 blocks, R = 48, 288 bits; 421 s per series |
| barrier transcript producer (SPEC.md lane B, `barrier-schema.json`) | `producer_mp.py` | DONE — per-prism files + manifest + progress, resumable |
| validation harness | `ft_mp_validate.py` | DONE — logs `validation-ft-mp.txt`, `validation-ft-mp-integral.txt`, `validation-ft-mp-instance.txt` |
| transcripts | `transcripts/row2/` (row 2), `transcripts/mini/` (N = 5000 test instance) | see §5 |

## 2. Where the load-bearing mathematics lives (standing order 5)

All of it is in the module docstring of `ft_mp.py`, transcribed from the on-disk arXiv v2
(`fetched/p3-22a4-polymath15-2019-upper-bound-debruijn-newman.pdf`, PDF page = printed page):
(6), (7), (9), (10), (11) p4; Theorem 1.3 (13)–(22) p6; Proposition 6.6 (i)–(vi) p31 — (vi) used AS PRINTED
(SPEC D-2.4 allows "the 10.50 form (or 6.6(vi) itself)"; the displayed (24)/10.44 is never used); (92) and the
time-derivative identities of Lemma 8.4's proof p46–48. Derivations (each cited at the code line that uses it):

* **D-F1** the second sum of (14) is Σ b_n n^{−s**} with s** = s₋ + (t/2)α(s₋) (from (17), (18) and
  conj(α(s)) = α(conj s)); hence f_t = A_t(s₊) + γ A_t(s₋), A_t(s) := Σ_{n≤N} b_n^t n^{−(s + (t/2)α(s))}.
  **Finding (source-text): eq. (14) carries an OVERLINE on s_* in the second sum** (`n^{\overline{s_*}+κ}`),
  read from the page image this session (`scratchpad p6crop.png`); `pdftotext` drops it, so SPEC.md §2.3's
  quotation of (14) shows `n^{s*+κ}`. Without the overline the exponent would carry −ix instead of +ix and f_t
  would not be holomorphic; P15's own (69)–(70) (from Corollary 6.5) and (92) fix the reading. **Both legs must
  implement the overline reading; the SPEC quotation should be annotated** (a wording fix, not a check change).
* **D-F2** γ = exp((t/4)(α(s₋)² − α(s₊)²) + log M₀(s₋) − log M₀(s₊)) from (7), (10), (16); exp(log M₀) = M₀ for
  every branch, and `Ball.log`'s branches on IM+/IM−/RE+ are principal (RE− refused).
* **D-F3** N constant on the box (monotone in x and t; two corners by directed rounding) and N₀² ≤ x₁/(4π).
* **D-F4** e_A + e_B ≤ (e^{δ₁} − 1)(1 + e^{0.02y} N^{ty/(2(x−6))}) F_{N,t}(σ) for σ ≤ Re s* — from 6.6(iv),(v)
  with the n-dependent exponent majorized by δ₁ (needs N² ≤ x/4π), |γ|n^y ≤ e^{0.02y} from (20) and N ≤ √(x/4π),
  (22) for |κ|. Every factor evaluated by interval arithmetic over the whole box (x, y, t intervals).
* **D-F5** F_{N,t}(σ) ≤ 1 + (N^{1−ρ} − 1)/(1 − ρ), ρ = σ − (t/4) log N (b_n^t ≤ n^{(t/4)log N}; integral test).
* **D-F6** ∂_t f_t at fixed z (Lemma 8.4's identities) and the mean-value inequality |f_t − f_τ| ≤ (t−τ) sup|∂_t f|.
* **D-F7** the displacement clause: D/K := E_prism + (τ′−τ)·DT + E(τ), E_prism the majorant with t = [τ, τ′].
* **D-F8** the block-Taylor evaluator with the frozen-α correction — the fast rigorous evaluator (§3).
* **D-F9** the seam at t = 0 (SPEC P-7): Theorem 1.3 by the limit t ↓ 0 (dominated convergence for H_t,
  continuity of B_t, f_t and of the majorant); recorded in prism 0's `producer.comment`.

Exact emission as in M1: iv endpoints → `Fraction` losslessly, scaled by K / A, floor/ceil exactly; no float
touches any emitted number. Platform trust = M1's (ball.py `_inflate`: every transcendental endpoint within
2^−(prec−16) relative of the truth; ring primitives correctly directed-rounded).

## 3. The evaluator (D-F8) — why it is fast and what makes it rigorous

Direct summation of (14) costs 2·N₀ ≈ 1.3·10⁶ complex-ball terms per evaluation (≈ 100 s); a seam needs
≈ 10³ evaluations. Instead, with z_c the box center, u := s₊(z_c), a := α(u) and L := log n, the n-th term of
A_t(s₊(z)) is exp(−uL + (iδ/2)L + t(L²/4 − aL/2))·ρ_n with δ = z − z_c and ρ_n := exp(−(t/2)(α(s₊(z)) − a)L)
the α-freezing factor (|ρ_n − 1| ≤ e^η − 1, η = (t/2)|α(s₊(z)) − a| log N ≈ 10⁻¹² at X ≈ 5·10¹², because
|α′| ≈ 1/(2|s|)). Blocks [2^i, 2^{i+1}) with exact dyadic centers L_c and ℓ := L − L_c ∈ [−0.35, 0.35]
turn the frozen sum into Σ_blocks BF_B · Σ_{j<J,k<K} v^j t^k m_{j+2k}(B)/(j!k!4^k) with STORED MOMENTS
m_r(B) = Σ_{n∈B} n^{−u} ℓ^r (computed once per series, 421 s; 20 blocks × 49 moments as exact interval
endpoints), v = iδ/2 + t p_c, BF_B = exp((iδ/2)L_c + tQ_c). Truncation remainders are the standard exp-tail
bounds T_J(a) = a^J/J!·e^a summed with the block weights w(B) = Σ n^{−Re u}; the freezing correction is
(e^η − 1)·F_{N,t}(σ_fr) by D-F5; both are added as [−r, r]² boxes. The time derivative comes from the same
moments shifted by r ∈ {1, 2} (∂_t of the frozen term = (Q_c + p_c ℓ + ℓ²/4) × term). Orders (J, K) are chosen
per block to make the truncation ≤ 10⁻²⁸ at |δ| ≤ 0.66, t ≤ t₀ (typically (15–22, 1–10)). Evaluation cost:
≈ 45 ms per box or point (≈ 2000× the direct sum's speed), widths at thin points 10⁻²⁷ (t = 0) to 10⁻¹² (t > 0,
freezing-dominated); segment boxes of x-width h have widths ≈ 450h on the bottom edge (|f₀| ≈ 45 there) —
a factor ≈ 3–5 above the true derivative from the block-wise interval evaluation, acceptable.

The same object evaluated with t an INTERVAL [τ, τ′] gives the prism-uniform bound DT on |∂_t f| (D-F7); the
interval-t overestimate is small for the prism lengths used (≈ 1%).

## 4. Validation record (all membership decided in exact rational arithmetic; logs in this directory)

| test | file | result |
|---|---|---|
| Ball.exp at imaginary parts up to 10¹⁴ (the γ regime at X ≈ 5·10¹²: Im(log M₀ difference) ≈ 7·10¹³) vs dps-150 reference, 200 thin + 40 wide boxes × 5 interior points | `validation-ft-mp.txt` | 400/400 contained, thin relative widths < 10⁻⁶⁰ |
| α, log M₀, γ, f_t (direct) vs the independent mp float pipeline (dps 60), 40 random (x, y, t) with x ∈ [200, 10¹³], plus f_t at true N for x ≤ 2·10⁴ | `validation-ft-mp.txt` | 209/209 contained |
| **Theorem 1.3 end-to-end (the task's ≥ 30 points):** H_t/B_t by `mp.quad` of the defining integral (dps 130, piecewise Gauss–Legendre, two cuts as a consistency check ≈ 10⁻¹⁰⁰) vs the enclosure f_t-box + E·disk, x ∈ [200, 330], y ∈ [0, 1], t ∈ (0, 0.5] | `validation-ft-mp-integral.txt` | **32/32 contained**, 0 failures; actual \|g − f_t\|/E ∈ [0.170, 0.478] (max 0.478); f-box widths ≤ 7.7·10⁻⁷⁹; quadrature self-consistency 10⁻⁸⁶–10⁻¹⁰⁶; 1536 s |
| block-Taylor evaluator vs direct summation and the reference on the N = 5000 mini-instance (thin points at 4 times, segment boxes h ∈ {10⁻², 10⁻³}, ∂_t f vs central difference, an interval-t box) | `validation-ft-mp.txt` | 93/93 |
| the same at row 2 (N₀ = 630783; direct sums ≈ 100 s each) | `validation-ft-mp-instance.txt` | 69 checks, **68 pass, 1 harness artifact** (explained and re-checked below): every f-box contains the direct sum and the reference (Taylor widths 10⁻²⁷ at t = 0, 10⁻¹²–10⁻¹⁴ at t > 0; direct widths 10⁻⁶⁶–10⁻⁷⁰; direct sums 138–155 s each); the one flagged line is the d/dt f check at (x₁, y₁), t = 0 |
| **d/dt f at t = 0 re-check** (`dt0_recheck.py` → `validation-ft-mp-dt0.txt`): the harness clamps the lower finite-difference point to t = 0, so at t = 0 its "central difference" is a ONE-SIDED forward difference with step 10⁻¹², truncation h·\|∂²_t f\|/2 ≈ 10⁻¹²·45²·33/2 ≈ 3·10⁻⁸ against a derivative ball 10⁻⁹ wide (observed discrepancy 2.0·10⁻⁸; the mini instance passed only because its ball was 1.4·10⁻⁶ wide). Replaced by (R1) the analytic D-F6 derivative in an independent mp float pipeline and (R2) a genuine two-sided central difference (f_t is a finite sum, defined for t < 0), exact-Fraction membership, at the failing point and three others | **12/12, 0 failures**: at all four points the derivative ball CONTAINS R1, and R1 = R2 to \|R1 − R2\| ≤ 3.5·10⁻¹⁹ (at the failing point: ball [864.6401330051, 864.6401330061] + i[985.7084483854, 985.7084483865] ∋ R1 = 864.640133005614 + 985.708448385932i); f-value balls contain R1's f at 10⁻³⁰. **The evaluator's derivative is right; the harness line is the artifact.** (The script's first run mis-reported the three t = 0 f-value checks through a helper that re-rounded the dps-60 reference to 53 bits; kept as `validation-ft-mp-dt0-run1-helperbug.txt`, fixed, rerun.) |
| mini-instance end-to-end transcript (3 prisms) through the reference checker | `transcripts/mini/` | ACCEPT (C-B0..C-B13) |

Why the integral test cannot be sharper than it is: H_t(x+iy) ≈ e^{−πx/8} against an O(1) integrand, so the
quadrature needs ~x/6 digits of cancellation headroom (x ≤ 330 at dps 130); at such x the theorem's own error
term e_{C,0} ≈ (x/4π)^{−(1+y)/4}(1 + 1.24(3^y+3^{−y})/(N−0.125)) is 0.5–1.5. The test therefore verifies the
transcription of Theorem 1.3 (f_t, γ, α, M₀ and the majorant) as a THEOREM — the reference must lie inside the
enclosure, and it does with |g − f_t|/E ≈ 0.25–0.45 — while the evaluator's arithmetic is validated to 10⁻⁴⁰ by the
pieces test and to 10⁻⁷⁰ (direct) / 10⁻²⁷ (Taylor, t = 0) by the instance tests.

## 5. Run record — the row-2 barrier transcript

**COMPLETE.** Run 23:06:27–23:27:00 IST 2026-09-02 (second agent, after the 19:40 usage death; the first agent had
built and validated the leg and died before this run). Command:
`python3 producer_mp.py --instance row2 --out transcripts/row2 --max-seconds 10800` — K = 10²⁴, A = 10¹², h₀ = 1/50,
maxdepth 12, θ = 1/2, prec 288, one process (the second allowed process ran `dt0_recheck.py` alongside).

| quantity | value |
|---|---|
| instance | P15 Table 1 row 2 (SPEC §9): R = [5000000194858, 5000000194859] × [16733/100000, 1], t₀ = 93/500, N₀ = 630783 (P-3 re-verified by directed rounding, and N₀² ≤ x₁/4π) |
| chain | **39 prisms, seams 0 = τ₀ < … < τ₃₈ = 3719/20000 < t₀; τ₃₉ = t₀ — COMPLETE (0 → t₀)** |
| rows | 184 per prism (50 + 42 + 50 + 42 uniform h₀ = 1/50 segments; **no bisection was needed at any seam**), 7176 rows total |
| wall | 1233 s = 20.6 min; 26–36 s per prism (rising slowly with t as the Taylor orders in t grow) |
| per-prism cost (prism 0 log) | prepare 0.8 s; 184 segment boxes 3.7 s; 184 thin endpoints 4 s; 184 derivative boxes at the seam 8.4 s; interval-t prepare + 184 derivative boxes for the gate 9.9 s; JSON write < 0.1 s |
| prism lengths Δt | 1.14·10⁻³ (t = 0) growing ≈ 3–4 %/prism to 3.1·10⁻² (prism 37); prism 38 is a 5·10⁻⁵ sliver (the 3-significant-digit `nice_floor` remainder before t₀ — cosmetic) |
| gate | **every prism length passed C-B12 at the FIRST try** (39 tries, 0 halvings); (E + D)/floor ∈ [0.477, 0.540] (θ = 1/2 plus the interval-t growth of DT), max 0.540 |
| floors Fn/K | 4.629 (t = 0) decreasing to 1.445 (τ₃₈); max \|f\| box on ∂R 58.5 (t = 0) → 2.2 |
| E/K | 4.119·10⁻⁴ at t = 0 (e_{C,0}-dominated; e_A + e_B = 1.6·10⁻¹⁰) → 1.03·10⁻⁷ at τ₃₈ — matches SPEC §9's indicative 4.12·10⁻⁴ / 1.0·10⁻⁷ |
| D/K | 2.34 (prism 0) → 0.75 (prism 37); DT = sup\|∂_t f\| 2053 → 13.9 |
| argument rows | max row width 2 (turn units at A = 10¹²); winding sums S ∈ [−104, 103] ∋ 0, width ≤ 2·10⁻¹⁰ turn |
| reference checker | `barrier_ref_checker.py transcripts/row2/manifest.json` → **ACCEPT (barrier lane, 39 prisms): C-B0..C-B13** (`ref-checker-row2-run.txt`) |
| shape | all 40 files valid against `barrier-schema.json` (`schema_shape_check.py`, a hand-rolled 2020-12-subset validator with four negative controls, since `jsonschema` is not installed; `shape-check-row2-run.txt`) |
| size | 2.0 MB JSON (39 prism files + manifest + progress + log); per-prism table `row2-summary.md` |
| extrapolation vs. outcome | from the first 9 prisms (Δt growth 3.5 %/prism) the estimate was 40–55 prisms / ≈ 25 min; actual 39 / 20.6 min — the full mesh was feasible, no sub-box cut was needed |

What the transcript asserts (SPEC §4, modulo H2-B and H3, checker-verified integer facts only): for every t ∈ [0, t₀]
and z ∈ R, H_t(z) ≠ 0 — the barrier lane of Instance02. It is the mpmath leg's transcript ONLY; the P-11 two-producer
cross-check against the Arb leg (cell-wise rows on the common refinement, Fn/Fd, E, D as intervals) is still owed:
**no Arb row-2 transcript existed in this directory at 23:35 IST** (the Arb producer agent was running side by side).

Reproduction: the moments (`moments/row2-{plus,minus}.json`, 421 s each) then the command above; resume after a death
with `--resume`.

## 6. Cut lines and what is NOT in this leg (honest)

1. **Lane A (the asymptotic region at t₀: window rows + the Lemma-T tail row)** is not produced here; the task
   item is the barrier transcript. The evaluator layer (`defect_bound`, `F_majorant`, `ft_direct`) is what a lane-A
   producer needs; the mollified floor T (SPEC P-9) and the tail quantities Q₁…Q₄ (P-10) are not implemented.
2. **The Arb leg's cross-check (SPEC P-11)** is the other leg's / the comparator's business; this leg records per
   prism the pre-inflation diagnostics (`producer` block: E parts, DT, Δt, floor, orders, winding sum, timings).
3. **The frozen-α correction** dominates thin-point widths at t > 0 (≈ 10⁻¹² at X ≈ 5·10¹²); a first-order α
   expansion would remove it. Not needed: the widths are 10⁸ below the E scale.
4. **No parallelism** inside the producer (one process; the two moment series ran as the two allowed processes).
5. **The mesh is not minimal**: h₀ = 1/50 uniform then bisection; segment boxes are plain interval evaluations
   (a midpoint-Taylor box would be ≈ 3× tighter). Row counts are what they are (§5).
6. **Theorem 1.3 at t = 0** is by the limit argument D-F9 (producer obligation P-7), flagged for M2b as in SPEC §13.2.
7. **The P-11 cross-check is owed to the instance stage** (§5): this leg's row-2 transcript has not been compared with
   the Arb leg's. Until it is, a mis-scaled or rotated transcript is undetectable by the checker (SPEC P-11).
8. **The harness's derivative check is one-sided at t = 0** (`ft_mp_validate.py` clamps t − h to 0); its FAIL line in
   `validation-ft-mp-instance.txt` stands in the log as written and is superseded by `validation-ft-mp-dt0.txt` (§4).
   The harness itself was not edited (its other 68 checks are the record); a future run should use a two-sided
   difference at t = 0 or the analytic pipeline of `dt0_recheck.py`.
9. **Independent re-verification by the second agent (this session):** D-F8's block-Taylor derivation (remainder split
   S_J R_K + R_J S_K + R_J R_K, the Q_c/p_c expansion, the modulus σ_fr, the derivative bookkeeping and the freezing
   corrections) re-derived line by line against the code; Prop. 6.6(iv)–(vi) re-read on PDF p31 (constants 0.626,
   6.66, 3.58, 8.52, 1.24, 0.125, 6.92, the n^y and N^{|κ|} factors) — the docstring transcription is exact; the
   overline on s_* in (14) re-read from a 200-dpi render of PDF p6 (`n^{\overline{s_*}+κ}` is on the page) — D-F1's
   reading is the paper's, and SPEC.md §2.3's quotation of (14) (from pdftotext) should be annotated (wording only).
10. **The last prism is a 5·10⁻⁵ sliver** (τ₃₈ = 0.18595 → t₀ = 0.186), an artifact of the 3-significant-digit
    step rounding; harmless (one extra prism), fixable by snapping the step to t₀ when within one step of it.

## 7. Files added by the second agent

`dt0_recheck.py` + `validation-ft-mp-dt0.txt` (and the kept first-run log `validation-ft-mp-dt0-run1-helperbug.txt`);
`schema_shape_check.py` + `shape-check-row2-run.txt`; `row2_summary.py` + `row2-summary.md`; `ref-checker-row2-run.txt`;
`transcripts/row2/` (39 prisms, manifest, progress, producer.log, stdout.txt). No program Lean file was touched.
