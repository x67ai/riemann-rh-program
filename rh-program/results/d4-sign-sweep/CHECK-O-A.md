# CHECK-O-A — D4 Job 2 part A (Opus 5, the independent second model): the HARNESS GATE before the sweep runs at scale

**Opened Fri Sep 25 02:29 IST 2026 (machine clock). Contract: `results/d4-sign-sweep/BRIEF.md` "Job 2 — Part A", read in full, with the orchestrator's item list (a)–(g). Inputs read: BRIEF.md, SHARED.md checkpoints 0–4 and rows, `d4-sweep-note.md` §0–§5, §8, §10, `hashes.txt`, `harness/d4_twisted_sum.rs` (phase path lines 49–183, sum/self-test lines 286–500), `harness/d4_phase_selftest.py`, `harness/eps_phi.json`, `harness/sweep_plan.json`, `out/zeta_t*.json`, the prior-art texts and — for Odlyzko 1992 and 2001 — page images. Nothing of Job 1's was edited. Nothing committed by hand (watchdogs). Every number below is printed by a script under `results/d4-sign-sweep/checker-O/` whose log is named in place.**


## 1. The independent evaluator (deliverable 1) — `checker-O/twsumO.go`

**What it is.** A Go program (go 1.27.1, no modules, standard library only) written from `m6-rung1-note.md` §1 (identity (1.1) and (1.2), the weight w_n = 2Λ(n)n^{−1/2}a(log n), a(x) = L⁻³A(x/L)) and `separation-note.md` §0.1 — not from `d4_twisted_sum.rs`. Source SHA-256 90e144f502fbaf6d0214fe605d9923ee0f0111da27193b1d315f2be768ff1437, binary d57080a8eeee7da8e59322df2446c976a3b8ee64a18cf6064975dced489d0f45 (`checker-O/logs/build_hashes.txt`). The design differs from Job 1's at every stage:
* **Phase in turns, with the large pieces precomputed per height in 320-bit `math/big`.** t·log n/2π = k·frac(t ln 2/2π) + frac(t log m₀/2π) + t·u/2π, m₀ = 1 + i/4096, u = log(m/m₀) = 2 atanh z, |u| ≤ 1.23·10⁻⁴. π by Machin's formula and log by the atanh series, both in `math/big`; the 4 097 + 1 per-height residues are formed exactly there and stored as double-doubles. Per term only t·u/2π is formed in double-double, so no double-double image of log n (≤ 28.35) is ever built. This is the "higher-precision phase" the note §3 prices and does not build; it is built here and measured below.
* A(v) by tanh–sinh quadrature (step 1/128; A(0) = 16.62196534693396, 16.62196534693395 at step 1/256), A, A′, A″ tabulated on 8 193 points and interpolated by **quintic** Hermite (max |interpolated − direct| over 2 000 pseudo-random v: 4.6·10⁻¹⁴); Z computed, 0.22199690808403955; Parseval ∫η²B̂² = 104.43888844430172 against 2πA(0) = 104.43888844430369 (`checker-O/atest.json`).
* Odd-only segmented byte sieve with dynamic segment scheduling; double-double (two-sum) accumulation, not Neumaier.
* ARCH by composite Gauss–Legendre on η ∈ [0, 3000] (paired ±η), B̂ by composite Gauss–Legendre (40 000 nodes), bracket by an OWN complex digamma (recurrence to |z| ≥ 20, then the Stirling series to B₁₆) — no mpmath anywhere in the value; a second ARCH on [0, 2000] with half the panel width as the convergence check. Pole terms at t < 10³ by complex Gauss–Legendre quadrature of 2Re[h(i/2)·conj h(−i/2)]; at t ≥ 10³ set to 0 on the record's Lemma-G bound (not re-derived here).
* DH: own divisor recursion Λ(n) = a(n)log n − Σ_{d|n, 1<d<n}Λ(d)a(n/d), a = (1, κ, −κ, −1, 0) by n mod 5.

**A bug of the first build, found by its own self-test, and what it teaches about Go.** The first build's phase self-test at t = 10¹², 10¹⁶, 10²⁰ against mpmath gave errors of 1.7·10⁻²⁰·t (1.76 rad at 10²⁰). Cause: the Go compiler on arm64 fuses `a*b` with a later subtraction into one FMA **across statements** (the Go specification permits it); `p1 := t*v.h; f1 := p1 − round(p1)` became `fma(t, v.h, −round(p1))`, so the error term of the error-free product was counted twice. The fix forces rounding with `float64(a*b)` in `twoProd` and in the accumulator. The (10¹², 20) value of the first build differed from Job 1's by 4.4·10⁻¹¹ — inside the brief's 10⁻¹⁰ tolerance. The tolerance would not have caught this bug; the phase self-test did. Every number below is from the fixed build. (Rust does not contract floating-point operations by default, so Job 1's harness is not exposed to this; its self-test measures the whole path in any case — item (a).)

**Own phase self-test after the fix** (`checker-O/selftest_check.py`, 5 000 pseudo-random n ≤ X = e^{28.35}, seed 777, mpmath at 50 digits; `checker-O/out/selftestO_t*_L28.35.json`): max phase error **3.14·10⁻¹⁸ rad at t = 10¹², 3.15·10⁻¹⁸ at 10¹⁶, 3.48·10⁻¹⁶ at 10²⁰** — at 10²⁰ that is 3.5·10⁻³⁶·t, five orders below Job 1's path. At 10²⁰ the figure is the double rounding of the output in turns, not a t-proportional term.

## 2. The items Job 1 flagged (deliverable 2)

### (a) `reduced_phase_dd` — re-derived, and my own self-test of Job 1's whole phase path — GATE PASS
**Re-derivation (read at `harness/d4_twisted_sum.rs` lines 140–175).** t·(hi + lo) = p + e + q + f exactly (two `two_prod`s with `mul_add`; Rust does not contract, so these are error-free). Stage 1: k = round(p/2π) is an integer-valued double (above 2⁵³ every double is an integer, so k is exact whatever its size); k·c₀ = m₁ + m₂ exactly; r₀ = p − m₁ is exact by Sterbenz because m₁ is within a relative 2⁻⁵² of p; k·c₁ = n₁ + n₂ and k·c₂ = o₁ + o₂ exactly; the seven pieces are summed in double-double, magnitudes ≤ ≈ p·2⁻⁵² ≈ 6·10⁵ at t = 10²⁰, so the dd roundings are ≈ 2⁻¹⁰⁵·6·10⁵ ≈ 10⁻²⁶ rad. Stage 2 removes the ≤ ~10⁵ turns left by the double division, with exact products. The truncation of 2π: **c₀ + c₁ + c₂ differs from 2π by 2.245·10⁻⁴⁹** (mpmath at 50 digits), and c₂ = −5.989539619436679·10⁻³³ **is the double nearest to 2π − c₀ − c₁**, and c₁ the double nearest to 2π − c₀ (`checker-O/out/job1_phase_check.json`); times k ≤ 4.5·10²⁰ this is ≤ 10⁻²⁸ rad. The derivation holds.

**My own self-test of Job 1's path** (`checker-O/job1_phase_check.py`, log `checker-O/logs/job1_phase_check_run.log`): Job 1's own binary run with `--selftest-only` on MY seeds (777: 5 000 n at each of t = 10¹², 10¹⁶, 10²⁰; 31337: 200 000 n at t = 10²⁰), all n ≤ X = e^{28.35}, checked against mpmath at 50 digits:

| t | rows | max \|dd log − log n\| | max whole-path phase error | ÷ t | product + reduction residual (phase error − t·log error) |
|---|---|---|---|---|---|
| 10¹² | 5 000 | 5.972·10⁻³¹ | 5.972·10⁻¹⁹ rad | 5.97·10⁻³¹ | 1.2·10⁻³² rad |
| 10¹⁶ | 5 000 | 5.972·10⁻³¹ | 5.972·10⁻¹⁵ rad | 5.97·10⁻³¹ | 7.4·10⁻³¹ rad |
| 10²⁰ | 5 000 | 5.972·10⁻³¹ | 5.972·10⁻¹¹ rad | 5.97·10⁻³¹ | 9.1·10⁻²⁷ rad |
| 10²⁰ | **200 000** | **6.686·10⁻³¹** | 6.686·10⁻¹¹ rad (n = 594 894 023 059) | **6.69·10⁻³¹** | 1.3·10⁻²⁶ rad |

**Confirmed: the whole-path error is the dd log's alone.** The product and the reduction add ≤ 1.3·10⁻²⁶ rad at 10²⁰ (1.3·10⁻⁴⁶·t), fifteen orders below the log's contribution. Note the last row: over 200 000 sampled n the maximum, **6.686·10⁻³¹, exceeds the ε = 6.392·10⁻³¹ the harness carries** — item (b).

### (b) ε governance — BINDING DECISION: the a-priori worst case governs; ε = 1.027·10⁻³⁰ (derived here); t_ceil(28.35) = 6.63·10¹⁹
**The argument.** The phase line ε_φ·ℓ¹ is used as a worst-case bound (|cos(x + ε) − cos x| ≤ |ε| per term, summed with |w_n|), and the refusal rule and the Control-1 tolerance both use it as one. A worst-case bound needs a worst-case constant. A sample maximum is a statement about the n that were sampled, not about the 7.5·10¹⁰ that are summed, and my 200 000-row sample already exceeds the 5 000-row figure (6.686 against 6.392·10⁻³¹). So the sampled figure cannot govern. Job 1's a-priori figure "≈ 3·2⁻¹⁰⁵·28.35 = 2.1·10⁻³⁰" was stated as an estimate, not derived. I derived a bound instead.

**The derivation** (`checker-O/job1_ddlog_bound.py`, log `checker-O/logs/job1_ddlog_bound_run.log`, output `checker-O/out/job1_ddlog_bound.json`). I emulated `dd_log_u64` bit for bit in Python (IEEE doubles, round-to-nearest; `two_prod` by Veltkamp–Dekker, which returns the same exact error term as `mul_add`). The emulation reproduces Job 1's printed (hi, lo) on **all 205 000 self-test rows with 0 mismatches**. Job 1's dd log is S₂ = S₁ ⊕ R, with S₁ = (ln2_dd ⊗ k) ⊕ logm0[idx] and R the 7-term series for log(1 + r), |R| ≤ 0.0039.
* S₁ depends only on (k, idx). Its error is computed **exactly** (mpmath at 60 digits) for all 40 × 257 combinations: **max 4.250·10⁻³¹** at (k, idx) = (26, 178). The pieces: the dd ln 2 is off by −3.65·10⁻³³, and the table log m₀ is off by at most 2.48·10⁻³².
* The last add S₁ ⊕ R is exact except for two roundings. For |S₁|, |S₂| < 32, c = RN(e + t) has |e + t| < 2⁻⁴⁷ and errs by ≤ 2⁻¹⁰¹, and w = RN(e₂ + f) has |e₂ + f| < 2⁻⁴⁸ and errs by ≤ 2⁻¹⁰². So the add errs by **≤ 3·2⁻¹⁰² = 5.92·10⁻³¹**. (log n ≤ 28.35 < 32.)
* R's own error: measured ≤ 1.4·10⁻³⁴ on the rows; I carry a cap of 10⁻³² (dd arithmetic at |R| ≤ 0.0039).
* **ε_a-priori = 4.250·10⁻³¹ + 5.92·10⁻³¹ + 10⁻³² = 1.027·10⁻³⁰** per unit t. The product and the reduction add ≤ 1.3·10⁻⁴⁶·t (item (a)). This is a proven bound, and the measured maximum 6.69·10⁻³¹ sits below it. Job 1's 2.1·10⁻³⁰ is also a valid upper bound, only a looser one.

**Decision (binding on the sweep plan): ε_φ(t) = 1.027·10⁻³⁰·t** in every phase line, in every refusal and in the Control-1 tolerance. The measured figures stay in the JSONs as diagnostics.
* **t_ceil(28.35) = 10⁻⁸/(1.027·10⁻³⁰ × 146.9506) = 6.63·10¹⁹.** At L = 22, t_ceil = 10⁻⁸/(1.027·10⁻³⁰ × 21.81) = 4.47·10²⁰.
* Consequences, checked against `harness/sweep_plan.json`:
  * **tier 2 at t = 10²⁰, L = 28.35 is REFUSED** (phase line 1.51·10⁻⁸).
  * The plan's own fallback applies ("the largest accepted ladder height replaces it"). The replacement is **ladder k = 117, t = 61609351296641974272**: phase line 9.30·10⁻⁹. Ladder k = 118 (7.11·10¹⁹) would have a line of 1.07·10⁻⁸ and is refused.
  * The covered-range control 15202440115920748544 at L = 28.35 is accepted (2.29·10⁻⁹).
  * 10¹⁴, 10¹⁶, 10¹⁸ and the PT-edge point are accepted.
  * **All 121 tier-1 heights and both tier-1 controls at L = 22 are accepted** (largest line 2.1·10⁻⁹ at 9.49·10¹⁹).
* The looser 2.1·10⁻³⁰ would put t_ceil(28.35) at 3.24·10¹⁹. It would refuse the same 10²⁰ point and would also refuse ladder k = 113–117 as tier-2 replacements (the replacement would be k = 112, 3.0002·10¹⁹). It would not refuse the 1.52·10¹⁹ control, which sits below 3.24·10¹⁹ on either constant.
* **Change to apply** (by the orchestrator or Job 1's fix pass; I edited nothing):
  * `harness/eps_phi.json` `eps_phi_per_t` → 1.0266395604864687e-30, with basis "a-priori bound, checker-O/job1_ddlog_bound.py", keeping the measured maxima beside it.
  * `sweep_plan.json` tier 2: replace "100000000000000000000" by "61609351296641974272" (role: the ceiling, ladder k = 117, the largest height with phase line ≤ 10⁻⁸ at ε = 1.027·10⁻³⁰).
  * Note §3: the ceiling paragraph and the table line.
  * The compiled default `EPS_PHI_PER_T = 2.2e-31` (line 147) is the retired brief constant. It is used whenever `--eps-phi` is omitted, so set it to the binding value or make the flag mandatory.
* A way to keep 10²⁰ at L = 28.35, if the sponsor wants it later: the per-height `math/big` phase of checker-O (§1). Its measured error at 10²⁰ is 3.5·10⁻¹⁶ rad, so its phase line at 10²⁰ is ≈ 5·10⁻¹⁴. This is Job 1's own §3 priced design, now built and measured. It is not adopted here, because the refusal rule belongs to Job 1's harness and the change would be a harness rebuild.

### (c) The coverage map at the page — GATE PASS for the chosen heights; NOTE FIX required (four windows missing, one number wrong)
Sources re-read: the Gourdon 2004 §4.3.1 table at `prior-art/gourdon-2004-zetazeros1e13-1e24.txt` lines 1848–1859 (offsets as Job 1 quotes them: 10¹⁴: 3 … 2·10⁹; 10¹⁵: 0 … 2·10⁹ − 1; 10¹⁶: 1 … 2·10⁹ − 1; 10¹⁷: 0 … 2·10⁹; 10¹⁸: 1 … 2·10⁹ − 1; 10¹⁹: 0 … 2·10⁹ + 1; 10²⁰: 4 … 2·10⁹ − 1; "a precision of about 10⁻⁹", line 1697). Odlyzko 1992 **as page images**: PDF p. 4 (= p. 1, the 10²⁰-th zero 15202440115920747268.6290299…), PDF p. 8 (= p. 5), PDF p. 140 (Table 1.1 and **Table 1.2**). Odlyzko 2001, PDF p. 3, as a page image.

**What the page says that the map omits.** Odlyzko 1992 p. 5: "The main sets of zeros that were computed are listed in Table 1.2. The entry for N = 10²⁰, for example, means that 175,587,726 zeros were computed, starting with zero number 10²⁰ − 30,769,710, and ending with zero number 10²⁰ + 144,818,015". Table 1.2 (PDF p. 140) lists **eight** sets:

| N | zeros | first |
|---|---|---|
| 10⁶ | 1,001,052 | N + 1 |
| 10¹² | 1,592,196 | N − 6,032 |
| 10¹⁴ | 1,685,452 | N − 736 |
| 10¹⁶ | 16,480,973 | N − 5,946 |
| 10¹⁸ | 16,671,047 | N − 8,839 |
| 10¹⁹ | 16,749,725 | N − 13,607 |
| 10²⁰ | 175,587,726 | N − 30,769,710 |
| 2·10²⁰ | 101,305,325 | N − 633,984 |

The 10⁶ row is printed "1, 000, 1052" on the page. **The N = 10¹⁴, 10¹⁶, 10¹⁸ and 10¹⁹ sets lie inside [PT, 10²⁰] and are not in Job 1's map**, which carries "Odlyzko 1992 ×2". Each sits at the start of the matching Gourdon window and begins a few thousand zeros below it. The map therefore has **fourteen** windows, not ten. The covered measure changes by less than 10⁻³ of itself.

The 10²⁰ set, taken at the page, runs from −4.6·10⁶ to +2.15·10⁷ in t around the 10²⁰-th zero. Job 1's ±5.2·10⁷ contains it, so that window is conservative and correct. The Odlyzko 2001 quote is at the page ("1,006,374,896 zeros … starting with zero # 13,048,994,265,258,476 (at height approximately 2.51327412288·10¹⁵)").

**My recomputation** (`checker-O/coverage_check.py`, log `checker-O/logs/coverage_check_run.log`, output `checker-O/out/coverage_check.json`): the height of zero #n from the Riemann–von Mangoldt main term inverted in mpmath, each window padded by 1 000 mean spacings on both sides.
* **None of the 121 tier-1 heights lies in any of the fourteen windows. Nor do the tier-2 heights 3 000 175 332 900, 10¹⁴, 10¹⁶, 10¹⁸, 10²⁰, or the replacement 61609351296641974272** (it lies above the 2·10²⁰-th-zero set at 2.99·10¹⁹).
* **The controls are inside published sets.**
  * 15202440115920748544 is **8 592 zeros above zero #10²⁰**, inside Gourdon's #10²⁰ + 4 … and inside Odlyzko 1992's N − 30,769,710 … N + 144,818,015.
  * 2513274122900000 is inside Odlyzko 2001's window, **2.0·10⁴ in t (≈ 1.07·10⁵ zeros) above the window's start**. The note §5 says "2·10⁷ above its 12-digit start". That is a slip, three orders too large: the 12-digit start 2.51327412288·10¹⁵ is 2.0·10⁴ below the control. The conclusion (inside) stands with a margin of ≈ 10⁹ zeros on the other side, and ±5·10³ of rounding in the start does not move it.
* Stop line (5) does not fire.
* **Fix for the note §5:** add the four Odlyzko 1992 Table 1.2 sets (fourteen windows), cite Table 1.2 (PDF p. 140) and p. 5, and correct "2·10⁷" → "2·10⁴".

### (d) δ_vis with log t against log(t/2π) — GATE PASS
`checker-O/dvis_planted_check.py`, log `checker-O/logs/dvis_planted_check_run.log`. The law is L_sign(0.1, t) = 22.4·(ℓ(t)/ℓ(10⁶))^{1/3} with ℓ = log or log(·/2π), and δ_vis = 0.1·(L_sign/L)^{3/2}; the band on δ_vis is the factor 1.5 on L_sign, i.e. 1.5^{3/2} = 1.837. Across all 133 planned and rehearsal points (121 ladder + 2 tier-1 controls at L = 22, 6 tier-2 at 28.35, 4 rehearsal), the two variants differ by at most a **factor 1.0523** (at 9.49·10¹⁹ and 10²⁰). Both sit inside the band at every point. The values reproduce Job 1's (0.0993 and 0.1031 at (10¹², 28.35)) and the brief's (0.101 at 3·10¹², 0.128 at 10²⁰, L = 28.35).

### (e) Control 2 zero-side only — MET as the brief defines it; must carry the label (already in the note §4.5)
The brief (iv) specifies both parts of Control 2 and itself requires the label: a zero-side planted orbit at every height, and the DH coefficient-side regression at every checkpoint. Both are run at every point: the SHARED rows show the planted value against −2δ²c(δL)² and the DH (85.7, 10) regression firing. I evaluated the expected value independently (mpmath tanh–sinh at 30 digits): −2δ²c(δL)² = −0.026808559547114345 at (δ = 0.0993247…, L = 28.35), against Job 1's −0.026808559547114343; −0.027285723373488551 at δ = 0.1; −0.274612193776558 at DH's δ, L = 10. The differences are ≤ 8·10⁻¹⁸. **What the label must say, plainly:**
* h_f(t ± iδ) = ±iδ·B̂(±iLδ) = ±iδ·c(δL) does not depend on t. So the zero-side planted value checks the kernel at λ = δL; it exercises nothing height-dependent. The height enters only through the reflected pair, which is ≤ 10^{−934 982}.
* The only height-dependent check of the prime sum is Control 1, the agreement of the two implementations.
* A prime-side planted zero at the sweep's heights does not exist.

The note §4.5 states the last point. The first point should be added to it in one sentence. Control 2 is met, not failed.

### (f) `binary_sha256` against `binary_sha256_ran` on the (10¹², 28.35) JSON — FIX-FIRST (minor, before the tier-2 list runs)
`out/zeta_t1000000000000_L28.35.json` carries `binary_sha256` = f6256ded… (the second build, hashed by `d4_point.py` at assembly time) and `binary_sha256_ran` = f97fc582… (the first build, `harness/d4_twisted_sum.v1`, which produced the sum). I re-hashed both binaries and the source: f97fc582a546…023b for `.v1`, f6256dedf9a7…c2a4 for the current binary, c1149d5459…7507 for the source — as `hashes.txt` states. The annotation is honest, and my evaluator reproduces the value (§3), so nothing is lost. But the key a reader or a script will take, `binary_sha256`, names a binary that did not run. **Fix:**
* `binary_sha256` must be the binary that produced the sum. `d4_point.py` should hash it at launch, before the sum, and store the at-assembly hash under another key.
* The (10¹², 28.35) JSON should be re-annotated so that `binary_sha256` = f97fc582…, with the second-build hash moved to `binary_sha256_at_assembly`. `hashes.txt` then gets the re-hashed JSON.
* For the PT-edge point it does not arise (one build throughout).

## 3. Control 1 at the rehearsal points — checker-O against Job 1 (`checker-O/compare.py`, log `checker-O/logs/compare_run.log`, output `checker-O/out/compare.json`; tolerance 10⁻¹⁰ + the phase line at the BINDING ε = 1.027·10⁻³⁰)

| point | P (Job 1) | P (checker-O) | \|ΔP\| | W (checker-O) | \|ΔW\| | tolerance | verdict |
|---|---|---|---|---|---|---|---|
| zeta (85.7, 10) | 3.9608507012438988e-02 | 3.9608507012439245e-02 | 2.6e-16 | +3.822866509675067e-03 | 9.3e-16 | 1.00e-10 | **PASS** |
| zeta (85.7, 20) [M6 record] | 4.5629998247170003e-03 | 4.5629998247173629e-03 | 3.6e-16 | +8.660342318479756e-04 | 2.4e-17 | 1.00e-10 | **PASS** |
| zeta (1e6, 10) | -5.2207475557697010e-02 | -5.2207475557697426e-02 | 4.2e-16 | +2.512992843925873e-01 | 1.7e-15 | 1.00e-10 | **PASS** |
| zeta (1e6, 20) | -4.2851912159123789e-03 | -4.2851912159125186e-03 | 1.4e-16 | +2.917166732027457e-02 | 1.1e-16 | 1.00e-10 | **PASS** |
| zeta (1e12, 20) | -6.4571825725515371e-03 | -6.4571825725517002e-03 | 1.6e-16 | +6.004877589499902e-02 | 4.4e-16 | 1.00e-10 | **PASS** |
| zeta (1e12, 28.35) | -5.5556247806859364e-03 | -5.5556247806872027e-03 | 1.3e-15 | +2.437163180284393e-02 | 1.2e-15 | 1.00e-10 | **PASS** |
| zeta (3000175332900, 28.35) PT edge | -2.6490225778961545e-03 | -2.6490225778974144e-03 | 1.3e-15 | +2.226650599838479e-02 | 1.3e-15 | 1.00e-10 | **PASS** |
| DH (85.7, 10) | 3.3999546892892463e-01 | 3.3999546892892663e-01 | 2.0e-15 | -2.698120741982896e-01 | 2.6e-15 | 1.00e-10 | **PASS** |
| DH (85.7, 20) | 7.5700418200496356e-01 | 7.5700418200496788e-01 | 4.3e-15 | -7.482311452973375e-01 | 4.4e-15 | 1.00e-10 | **PASS** |

Notes on the table. At (10¹², 28.35) checker-O finds the same term count as Job 1: **75 148 949 134 = 75 148 837 837 primes + 111 297 prime powers**, over X = 2 052 336 466 859. It also finds the same ℓ¹, 146.95060754424256 against 146.95060754424162. ARCH = 0.018816007022156727 against Job 1's 0.01881600702215674; my own [0, 2000], half-panel ARCH check agrees to 4·10⁻¹⁷. Sum wall time: 1 800 s on 8 threads (1 792 s at the PT edge), run concurrently with Job 1's PT-edge process. Log: `checker-O/logs/zetaO_t1e12_L28.35_run.log`, JSON `checker-O/out/zetaO_t1e12_L28.35.json`. The (85.7, ·) ζ values are compared with Job 1's printed digits (SHARED checkpoint 1) and with the M6 record (§4), because Job 1 wrote no ζ JSON at 85.7. The DH witnesses from my own recursion are Λ_DH(3) = −0.31209272851616354, Λ_DH(4) = −1.4422319646064572, Λ_DH(6) = 1.9363560766210386 and Λ_DH(12) = −0.7628774719884115; all four reproduced. **Every difference is at the 10⁻¹⁵ level: five orders inside the tolerance at every point.** At 10¹² the phase lines are ≤ 1.5·10⁻¹⁶, so the agreement tests everything except the phase at large t. That part is tested by item (a) and by my own self-test (§1).

**The PT-edge point (item (g)).** Job 1's JSON `out/zeta_t3000175332900_L28.35.json` landed at 03:32:34 IST, with its SHARED row: W = +0.02226650599838353, verdict "silent (W > 0)", controls pass, stop_line null. It is not a STOP/BUG or CONTROL FAILED row. checker-O ran the full point independently: `checker-O/out/zetaO_t3000175332900_L28.35.json`, log `checker-O/logs/zetaO_t3000175332900_L28.35_run.log`, 75 148 949 134 terms. It gives **W = +0.022266505998384794, |ΔP| = |ΔW| = 1.3·10⁻¹⁵ — PASS**. The phase line at the binding ε is 4.5·10⁻¹⁶. The DH (85.7, 20) regression on my own recursion also reproduces Job 1 and the M6 record: W = −0.7482311452973375 (M6 −0.748231145297333), and I found 360 809 171 f64-nonzero terms against Job 1's 340 796 040. The difference is roundoff-level structural zeros that differ between the two recursions (M6 §2.2: the true nonzero count is 120 953 877). Their contribution to W is at the 10⁻¹⁵ level. Log: `checker-O/logs/dhO_L20_run.log`.

## 4. Verdict (deliverable 3)

**Overall: FIX-FIRST.** The fixes are small and none touches a computed value. The harness computes correctly: both implementations agree to ≤ 4.4·10⁻¹⁵ at all nine rehearsal points, and the phase path's error is the dd log's alone. The sweep may start at scale once the binding ε and the tier-2 change are applied (items (b), (f) below). The note fixes (c), (e) may land in the same fix pass without blocking the first tier-1 points.

| item | verdict | what I ran | log |
|---|---|---|---|
| Evaluator agreement, 9 points incl. (10¹², 28.35) and the PT edge | **GATE PASS** (max \|ΔW\| 4.4·10⁻¹⁵ against tolerance ≥ 10⁻¹⁰) | `checker-O/twsumO.go`, `compare.py` | `checker-O/logs/*_run.log`, `checker-O/out/compare.json` |
| (a) `reduced_phase_dd`, three-double 2π, whole-path self-test | **GATE PASS**: product + reduction ≤ 1.3·10⁻²⁶ rad at 10²⁰; c₂ is the nearest double; error = dd log's alone | `job1_phase_check.py` on Job 1's binary, seeds 777 / 31337 (215 000 rows) | `checker-O/logs/job1_phase_check_run.log` |
| (b) ε governance | **FIX-FIRST (binding)**: ε = 1.027·10⁻³⁰ (a-priori, derived); t_ceil(28.35) = 6.63·10¹⁹; tier-2 10²⁰ → 61609351296641974272; `eps_phi.json` and the compiled default updated | `job1_ddlog_bound.py` (bit-exact emulation, 0 mismatches on 205 000 rows) | `checker-O/logs/job1_ddlog_bound_run.log` |
| (c) coverage map | **GATE PASS** for the heights (no planned height in any of 14 windows; both controls inside published sets); **note FIX**: add the four Odlyzko 1992 Table 1.2 sets (N = 10¹⁴, 10¹⁶, 10¹⁸, 10¹⁹); "2·10⁷" → "2·10⁴" | `coverage_check.py`; page images Odlyzko 1992 PDF pp. 4, 8, 140; Odlyzko 2001 PDF p. 3 | `checker-O/logs/coverage_check_run.log` |
| (d) δ_vis, log t against log(t/2π) | **GATE PASS**: variants differ by ≤ 1.0523 against the band 1.837 at all 133 points | `dvis_planted_check.py` | `checker-O/logs/dvis_planted_check_run.log` |
| (e) Control 2 zero-side only | **MET, labeled**: the planted value reproduced independently to ≤ 8·10⁻¹⁸; add one sentence to note §4.5 (the planted value does not depend on t; the height-dependent check is Control 1) | same | same |
| (f) `binary_sha256` against `_ran` | **FIX-FIRST (minor)**: the primary key must name the binary that ran; hash at launch | `shasum` of both builds and the source | this file §2(f) |
| (g) PT-edge point | **PASS**: silent (W = +0.022266505998384 on both), \|ΔW\| = 1.3·10⁻¹⁵; Job 1's row is not STOP/BUG or CONTROL FAILED | full independent run, 1 792 s | `checker-O/logs/zetaO_t3000175332900_L28.35_run.log` |

**Binding ε decision, restated:** the a-priori worst case governs the refusal rule and the Control-1 tolerance, at **ε = 1.027·10⁻³⁰ per unit t** (the sampled 6.392·10⁻³¹ is exceeded by a larger sample, 6.686·10⁻³¹, and is not a bound). **Resulting ceiling: t_ceil(28.35) = 6.63·10¹⁹; t_ceil(22) = 4.47·10²⁰.**

**Change to `sweep_plan.json` (for the orchestrator or Job 1's fix pass to apply):**
* tier 2 "100000000000000000000" → "61609351296641974272" (ladder k = 117; phase line 9.30·10⁻⁹);
* tier 1 unchanged (121 + 2 controls, all accepted);
* the tier-2 covered-range control 15202440115920748544 unchanged (line 2.29·10⁻⁹).

After the fix pass I re-check only (b) and (f), per the brief.

**Reading, for the record.** Nothing here is a statement about RH. Every value is positive (silent). The sign channel stays an instrument, and the floating-point evaluation is a signal to certify, not a proof. The Go-contraction bug of §1 is a lesson for any future compiled second implementation in Go: it passed the brief's 10⁻¹⁰ tolerance at (10¹², 20) and was caught only by the phase self-test against mpmath. The self-test, not the tolerance, is what guards the phase above t ≈ 10¹².

*Closed Fri Sep 25 03:34:45 IST 2026 (machine clock).*
