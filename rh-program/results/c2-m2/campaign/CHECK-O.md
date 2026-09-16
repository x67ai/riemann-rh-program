# CHECK-O.md — the Opus checker's report on the zero-side numerics campaign for Theorem M2 (C2)

**Written 2026-09-16, 22:47 IST (Session 22, the campaign CHECKER, Opus 5, half slot; machine clock via `date`).**
Contract: the checker paragraph of `results/c2-m2/campaign/BRIEF.md` and `results/c2-m2/followups/PRICING.md` §2(e).
Object under check: `CAMPAIGN.md` v1, SHA-256 `09239e0a606bf7ca3463f35b9b5166a1e1e913fdfcf21635fb5e35b7a9b4dfb8` (read; matches the
hash the orchestrator quoted), the four row / summary / zeros files, `logs/`, `outwindow_test.json`, `dh_offline_scan.json`.
**INSTRUMENT (standing order 4): everything below is about constants, a detection-bandwidth law and the accuracy of a
numerical instrument. Nothing here is a statement about RH.** Nothing was committed by hand; paths are quoted throughout.

**Independence.** `campaign_lib.py` is NOT imported anywhere in this check. The checker's transform is its own:
B̂(η) = ∫_{−½}^{½} B(v)cos(ηv)dv by **Gauss–Legendre quadrature** (`scipy.special.roots_legendre`, N = 12 000–16 000 nodes),
cross-checked against **mpmath tanh-sinh quadrature at 40 digits** with breakpoints at the nodes of cos(ηv); c(λ) = B̂(iλ) =
∫B(v)cosh(λv)dv by the same rule; complex arguments B̂(x − iy) = ∫B(v)e^{ixv}e^{yv}dv by the 40–110-digit oscillatory rule.
The builder's rule is a uniform trapezoid on 16 384 nodes plus an FFT/spline table and a Poisson-trapezoid rule in mpmath —
a different quadrature, different node family, different aliasing analysis. Scripts and logs: `check-O/` beside this file
(`ind_transform.py`, `verify_zeros.py`, `recompute_rows.py`, `deriv_norms.py`, `bhat_big.py`, `outwin_check.py`,
`dh_check.py`, `dh_control_check.py`, `closes_check.py`, and the matching `*.log` / `*.json`).

**Accuracy floor of the checker's own instrument, measured before anything was compared.** Against 40-digit mpmath
quadrature the Gauss–Legendre transform is accurate to **≤ 5.2·10⁻¹⁵ absolute** in B̂ over η ∈ [0, 2400] and to
**≤ 1.8·10⁻¹³ relative** in c(λ) up to λ = 132 (`check-O/ind_transform.py`; the run is reproduced in §1 of
`closes_check.log`). The constant Z = ∫exp(−1/(1 − 4v²))dv comes out 0.22199690808414 (N = 12 000) / 0.22199690808366
(N = 24 000) against the record's 0.2219969080840397 — agreement to 1.2·10⁻¹³ relative, from an entirely different rule.

---

## §1 Headline verdict

**PASS at all four heights. Stop condition (iii) does not fire.** Twenty random zeros per height re-verified at 30 digits
agree with the stored file to ≤ 8.2·10⁻¹¹ absolute in γ (the file's own dps = 15 working precision), the index → height map
is gap-free at every height, and the two rows recomputed per height with the independent transform agree with the builder's
to **≤ 1.7·10⁻¹² relative on W_Z** (tolerance 10⁻⁸), **≤ 1.0·10⁻¹³ relative on the main term** (tolerance 10⁻⁸) and
**≤ 5.7·10⁻¹⁶ absolute on W_{Z′}** (tolerance 10⁻¹⁰). The ratio to the clause-6 bound agrees to ≤ 9.8·10⁻¹⁴ relative.
No row is flagged.

**Closes:** close 1 **REPAIRED** (the verdict stands — the density model is the only one of the three laws inside a factor
1.5 — but two statements need correcting: the theorem's own δ-ratio is 6.95–7.13, not 5, and the refutation of the theorem's
law at "L_sign at t" has only a 1.3 % margin); close 2 **CONFIRMED** (every number reproduced exactly); close 3
**CONFIRMED** (the crossing is λ = 18.5828, i.e. 18.6 on the stated 0.1 grid, recomputed with the checker's own c);
close 4 **CONFIRMED** with one repair (the u_true bisection runs on a sign-oscillating quantity; at L = 120 the checker
finds the contamination already 5.8× below e^{−L} at the builder's u_true, so u_true/L ≤ 1.086 there — the close's
"R ≈ 1.1 L" is unaffected and if anything understated).

**Stop condition (iv):** the contract's literal form **FIRES at t = 10³, 10⁵ and 10⁶**; the builder's restatement on the
center mean is **legitimate mathematics but a genuine weakening of the contract's test**, and CAMPAIGN.md §1 does not
record that the literal form fired. §7 below gives the exact wording repair. The builder's `summary_*.json` does record
both forms (`single_t_geomean`, `single_t_outside_10x`), and `logs/height_t1e3.log` line 254 records the literal FIRES
verdict — so the record is honest at the file level and incomplete only in `CAMPAIGN.md`.

---

## §2 Per height: zeros verified, rows recomputed

### §2.1 Task (1) — twenty random zeros per height at 30 digits, and the index → height map

Method (`check-O/verify_zeros.py`, log `zeros_check.log`, data `zeros_check.json`; seed 20260916, `mp.dps = 30`): for each
sampled index n, `mpmath.zetazero(n)` at 30 digits, and independently a Newton iteration on Z = `mpmath.siegelz` started
from the stored γ. Map audit: indices consecutive, γ strictly increasing, count against the Riemann–von Mangoldt
θ(T)/π + 1 over the window and against the main term T/2π·log(T/2πe) + 7/8.

| t | stored zeros | index range | consecutive indices | γ monotone | RvM count over the window (θ/π) | max &#124;γ_stored − γ_30&#124; | max &#124;Z(γ_30)&#124; | Newton ≡ zetazero | verdict |
|---|---|---|---|---|---|---|---|---|---|
| 10³ | 459 | 427..885 | yes | yes | 458.710 (stored 459) | 1.069·10⁻¹³ | 8.08·10⁻²⁸ | to 0 at all 20 | **PASS** |
| 10⁴ | 681 | 9804..10484 | yes | yes | 680.973 (stored 681) | 1.202·10⁻¹² | 5.70·10⁻²⁷ | to 0 at all 20 | **PASS** |
| 10⁵ | 905 | 137617..138521 | yes | yes | 905.412 (stored 905) | 9.109·10⁻¹² | 1.60·10⁻²⁵ | to 0 at all 20 | **PASS** |
| 10⁶ | 1133 | 1746580..1747712 | yes | yes | 1133.408 (stored 1133) | 8.240·10⁻¹¹ | 8.54·10⁻²⁵ | to 1.03·10⁻²⁵ | **PASS** |

**Reading.** The index set is an unbroken run of integers at every height, so no zero of ζ inside the data window is
missing from the file by construction of `zetazero`; the RvM count over [γ_first, γ_last] reproduces the stored count to
better than half a zero at all four heights, which is the independent confirmation that the run of indices covers exactly
that γ-interval. The γ deviations track the builder's dps = 15 working precision (10⁻¹³ at t = 10³ rising to 10⁻¹⁰ at
t = 10⁶, i.e. ~15 significant digits throughout), and the stored |Z(γ)| residuals (9.7·10⁻¹³ … 2.9·10⁻⁹) are consistent
with that. The effect of a γ error ε on a row is ≤ 2·|u|·|B̂|·|B̂′|·L·ε ≲ 10⁻⁸ε in the worst case, i.e. below 10⁻¹⁸ —
far under every tolerance in play.

### §2.2 Task (2) — two rows per height with the independent transform

Rows chosen: a **small-L** row (δ = 0.1, L = 20 — a row a reader can check against CAMPAIGN.md §6) and the **record point**
(δ = 0.1, L = L*(δ, t; C₁ = 1) — the row where the theorem asserts its bound). A third, extreme row per height
(δ = 0.05, L = L*(δ, t; C₁ = 2.4·10⁹)) was added to test the builder's note (4) about tolerances; see §2.3.
Log: `check-O/rows_check.log`, data `rows_check.json`.

| t | row | n zeros / U_row | W_{Z′} = N_Z (checker) | W_{Z′} (builder) | abs diff | main (checker) | main (builder) | rel | W_Z (checker) | W_Z (builder) | rel | sep/clause-6 (chk / bld) | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10³ | δ = 0.1, L = 20 | 459 / 285.594 | 2.197408974542e−02 | 2.197408974542e−02 | 9.7e−17 | −2.338405169299e−02 | −2.338405169299e−02 | 4.4e−16 | −1.409961947569e−03 | −1.409961947569e−03 | 7.6e−14 | 0.8602511869 / 0.8602511869 | **PASS** |
| 10³ | δ = 0.1, L* = 375.79 | 171 / 106.443 | 1.693104790145e−08 | 1.693104790190e−08 | 4.6e−19 | −1.756895160549e+08 | −1.756895160550e+08 | 8.7e−14 | −1.756895160549e+08 | −1.756895160550e+08 | 8.7e−14 | 121.5057656 / 121.5057656 | **PASS** |
| 10⁴ | δ = 0.1, L = 20 | 681 / 290.344 | 9.080464332750e−03 | 9.080464332750e−03 | 5.7e−16 | −2.338405169299e−02 | −2.338405169299e−02 | 4.4e−16 | −1.430358736024e−02 | −1.430358736024e−02 | 3.9e−14 | 0.8602511869 / 0.8602511869 | **PASS** |
| 10⁴ | δ = 0.1, L* = 387.28 | 243 / 103.284 | 5.006784880725e−09 | 5.006784880729e−09 | 3.7e−21 | −4.397621977144e+08 | −4.397621977144e+08 | 9.1e−14 | −4.397621977144e+08 | −4.397621977144e+08 | 9.1e−14 | 171.2141881 / 171.2141881 | **PASS** |
| 10⁵ | δ = 0.1, L = 20 | 905 / 294.096 | 2.347555352617e−02 | 2.347555352617e−02 | 1.7e−16 | −2.338405169299e−02 | −2.338405169299e−02 | 4.4e−16 | 9.150183318501e−05 | 9.150183318486e−05 | 1.7e−12 | 0.8602511869 / 0.8602511869 | **PASS** |
| 10⁵ | δ = 0.1, L* = 396.20 | 312 / 100.958 | 1.133986121539e−09 | 1.133986121661e−09 | 1.2e−19 | −8.993077759647e+08 | −8.993077759648e+08 | 9.4e−14 | −8.993077759647e+08 | −8.993077759648e+08 | 9.4e−14 | 224.0970826 / 224.0970826 | **PASS** |
| 10⁶ | δ = 0.1, L = 20 | 1133 / 297.220 | 2.917166731869e−02 | 2.917166731869e−02 | 5.4e−16 | −2.338405169299e−02 | −2.338405169299e−02 | 4.4e−16 | 5.787615625701e−03 | 5.787615625700e−03 | 9.2e−14 | 0.8602511869 / 0.8602511869 | **PASS** |
| 10⁶ | δ = 0.1, L* = 403.50 | 378 / 99.133 | 8.313694272116e−09 | 8.313694271938e−09 | 1.8e−19 | −1.616420111724e+09 | −1.616420111724e+09 | 9.7e−14 | −1.616420111724e+09 | −1.616420111724e+09 | 9.7e−14 | 279.7188165 / 279.7188165 | **PASS** |

The zero count used, U_row, W_Zrep, the clause-6 bound, the density model and the clause-4 bound were recomputed as well and
agree to the same order. **No row is flagged at any height; stop condition (iii) does not fire.**

The tightest comparison is the t = 10⁵, L = 20 row, where W_Z = 9.15·10⁻⁵ is the difference of N_Z = 2.3476·10⁻² and
|main| = 2.3384·10⁻² — a cancellation of 2.4 digits. Even there the two implementations agree to 1.7·10⁻¹² relative on
W_Z, i.e. roughly four orders inside the tolerance.

### §2.3 The builder's note (4) on tolerances is correct and is now demonstrated

The builder recorded (STATUS-campaign.md §5) that "the 10⁻⁸ relative tolerance for the checker cannot apply to W_{Z′} at
the record points (10⁻⁸–10⁻¹⁴ absolute); apply it to W_Z or absolutely at 10⁻¹⁰". The extreme rows confirm this
quantitatively (checker's log `rows_check.log`, run of the third row):

| t | δ = 0.05, L*(C₁ = 2.4·10⁹) | W_{Z′} checker | W_{Z′} builder | **abs** diff | **rel** diff | main term, rel diff |
|---|---|---|---|---|---|---|
| 10³ | 2590.38 | 4.095295e−19 | 4.095307e−19 | 1.17e−24 | 2.9e−06 | 8.1e−14 |
| 10⁴ | 2613.36 | 1.169612e−12 | 1.169612e−12 | 3.01e−22 | 2.6e−10 | 8.6e−14 |
| 10⁵ | 2631.21 | 3.476637e−23 | 3.446238e−23 | 3.04e−25 | **8.8e−03** | 9.1e−14 |
| 10⁶ | 2645.80 | 2.333559e−19 | 2.333554e−19 | 5.49e−25 | 2.4e−06 | 9.5e−14 |

At those points W_{Z′} is a sum of 25–57 terms each of size ~10⁻²⁴ built from B̂ values of size ~10⁻¹³ whose absolute
quadrature noise is ~10⁻¹⁵ in **any** double-precision rule. A 10⁻⁸ relative agreement there is not attainable by two
independent implementations and is not a defect of either. The absolute agreement is ≤ 3.0·10⁻²⁵, twenty orders inside the
10⁻¹⁰ absolute tolerance. **The builder's note (4) is adopted as the correct reading of PRICING §2(e)(iii).**

---

## §3 Task (3) — the clause-4 truncation with k ≤ 13 derivative norms

### §3.1 The norms, recomputed independently

The contract priced the truncation with k = 3 (‖B‴‖₁); the builder used the k-optimized route with norms up to k = 13.
The checker re-derived the representation from scratch — with w := 1 − 4v², φ := −1/w, B_raw^{(k)} = e^{φ}P_k(v)/w^{2k} and
**P_{k+1} = −8vP_k + P_k′w² + 16k·vP_kw** (derived here; it agrees with the builder's recursion, which is the same
mathematics) — found the real roots of P_k in (−½, ½) with `mpmath.polyroots` (the builder used a scan plus bisection: a
different root finder), and integrated |B^{(k)}| piecewise at 60 working digits. Script `check-O/deriv_norms.py`,
log `deriv_norms.log`, data `deriv_norms.json`. Z = 0.22199690808403971891.

| k | deg P_k | real roots in (−½, ½) | ‖B^{(k)}‖₁ (checker, 14 digits) | builder's stored table | rel diff |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 3.3142753594764 | 3.31427535948 | 1.1e−12 |
| 2 | 4 | 2 | 28.772644041739 | 28.7726440417 | 1.4e−12 |
| 3 | 7 | 5 | 642.3011963066 | 642.301196307 | 6.2e−13 |
| 4 | 10 | 6 | 38779.967246487 | 38779.9672465 | 3.3e−13 |
| 5 | 13 | 9 | 4291724.3513817 | 4291724.35138 | 3.9e−13 |
| 6 | 16 | 10 | 766365507.97667 | 766365507.977 | 4.3e−13 |
| 7 | 19 | 11 | 201117898543.53 | 201117898544 | 2.3e−12 |
| 8 | 22 | 12 | 7.2865076555777e+13 | 7.28650765558e+13 | 3.1e−13 |
| 9 | 25 | 15 | 3.4842900715335e+16 | 3.48429007153e+16 | 1.0e−12 |
| 10 | 28 | 16 | 2.1257306706423e+19 | 2.12573067064e+19 | 1.1e−12 |
| 11 | 31 | 19 | 1.6113480094248e+22 | 1.61134800942e+22 | 3.0e−12 |
| 12 | 34 | 20 | 1.4856211088056e+25 | 1.48562110881e+25 | 3.0e−12 |
| 13 | 37 | 23 | 1.6370748561862e+28 | 1.63707485619e+28 | 2.3e−12 |

**All thirteen norms confirmed to twelve significant digits** — the residual differences are exactly the rounding of the
builder's stored 12-digit table. k = 1, 2, 3 reproduce the record's 3.31428, 28.7726, 642.301 (`verify/b1_constant_run.log`).

### §3.2 The tail bound is rigorous, by the note's clause-4 route with k in place of 3

The bound used per row is

  tail(U) ≤ 2C₁ℓ_R·‖B^{(k)}‖₁²·L^{−2k}·(U − 2)^{3−2k}/(2k − 3),  ℓ_R = log(4 + t + R₀L), R₀ = 81, C₁ = 1 operative.

The checker re-derived it: (a) k integrations by parts of ∫B(v)e^{iηv}dv, with B ∈ C_c^∞ so that no boundary term appears,
give |B̂(η)| ≤ ‖B^{(k)}‖₁/|η|^k — the note's §5 polynomial route verbatim with k in place of 3, valid for every k ≥ 1;
(b) each term of N_Z is (γ − t)²B̂(L(γ − t))² ≤ ‖B^{(k)}‖₁²L^{−2k}u^{2−2k}; (c) the shell k′ ≤ u < k′ + 1 holds at most
2C₁log(3.5 + t + k′) points (note §5 with D7); (d) Σ_{j ≥ ⌊U⌋} j^{2−2k} ≤ (⌊U⌋ − 1)^{3−2k}/(2k − 3) ≤ (U − 2)^{3−2k}/(2k − 3),
which needs k ≥ 2 and U ≥ 3. Both conditions hold at every row (the builder restricts to 2 ≤ k ≤ 13 and prints `nan` below
U = 3). **The route is the note's, the inequality is rigorous, and the checker reproduces every printed value:**

| t | L | builder U_kopt / k | checker U_kopt / k | rel diff in U | builder tail at U_row | checker tail at U_row |
|---|---|---|---|---|---|---|
| 10³ | 4 | 142.7970 / 9 | 142.7970 / 9 | 1.3e−13 | 2.744e−15 | 2.744e−15 |
| 10³ | 20 | 22.2795 / 8 | 22.2795 / 8 | 4.4e−14 | 1.278e−25 | 1.278e−25 |
| 10³ | 375.79 | 2.4925 / 6 | 2.4925 / 6 | 1.9e−14 | 1.152e−31 | 1.152e−31 |
| 10⁶ | 4 | 148.6099 / 10 | 148.6099 / 10 | 1.3e−13 | 6.797e−16 | 6.797e−16 |
| 10⁶ | 50 | 8.8562 / 8 | 8.8562 / 8 | 3.7e−14 | 5.718e−32 | 5.718e−32 |
| 10⁶ | 403.50 | 2.4626 / 6 | 2.4626 / 6 | 1.8e−14 | 1.261e−31 | 1.261e−31 |

and U_data = 2·U(L_min = 4) is 285.5941 / 290.3445 / 294.0963 / 297.2198 at the four heights, matching the zeros files to
all printed digits, with tail(U(4)) = 1.000·10⁻¹⁰ exactly as specified. The polynomial bound was also checked pointwise:
|B̂(η)| ≤ ‖B^{(k)}‖₁/η^k holds at η = 20, 50, 100, 300, 1000 for k = 3, 6, 9, 13 (`closes_check` preamble / §3 of
`deriv_norms.log`).

**One precision item (not an error in any printed number).** Step (c)–(d) replaces log(3.5 + t + j) by ℓ_R for **every**
shell j ≥ U, whereas ℓ_R = log(4 + t + R₀L) covers only j ≤ R₀L − ½. The checker computed the true ratio
Σ_{j≥U} j^{2−2k}log(3.5 + t + j) / (ℓ_R·Σ_{j≥U} j^{2−2k}) at the operating points: **0.9806** (t = 10³, L = 4),
**0.8808** (10³, L = 20), **0.99999** (10⁶, L = 4), **0.9993** (10⁶, L = 120). The ratio is below 1 at every point checked,
so the printed bounds are upper bounds; the derivation should nevertheless state the covering (or bound the j > R₀L part
separately) rather than leave it implicit. Effect on any number in CAMPAIGN.md: none.

**The operative C₁ = 1 is justified at every height** (the label "C₁ = 1 operative for ζ, stated as such"): the largest
count of stored zeros in a closed window of length 2 is 3 / 4 / 5 / 6 at t = 10³ / 10⁴ / 10⁵ / 10⁶, against
C₁log(3 + t) = 6.911 / 9.211 / 11.513 / 13.816, i.e. an implied operative C₁ = 0.4343 at all four heights — a factor 2.3
of margin inside the C₁ = 1 the truncation uses.

**The contract's k = 3 radius is printed and is as the builder says.** `U_contract_k3` at L = 4 is 1.7·10⁴ at t = 10³ and
2.1·10⁴ at t = 10⁶; PRICING §2(b)'s "≈ 25 min at 10³ / 1.7 h at 10⁶" are the L = 10 and L = 8 figures, not the L_min = 4
figures the contract's own grid asks for. The builder's correction (STATUS-campaign.md §5, first bullet) is upheld.

---

## §4 Task (4) — the four closes of CAMPAIGN.md

Everything in this section was recomputed from the row and summary files, and where a transform is involved, with the
checker's own. Log: `check-O/closes_check.log`.

### §4.1 Close 1 — the δ- and t-law of the detection bandwidth: **REPAIRED** (verdict unchanged)

* **The twelve-point tables of §2 are exactly the summary files' values.** All 24 cells (L_sign and L_bal3, at t and the
  median over centers, three depths × four heights) reproduce from `summary_*.json` with no transcription error.
* **The least-squares exponents reproduce exactly**: L_sign at t **b = 0.737, c = 0.262**, max residual factor 1.281;
  L_bal3 at t **b = 0.732, c = 0.003**, 1.443; L_sign median **b = 0.642, c = 0.368**, 1.119; L_bal3 median
  **b = 0.596, c = 0.434**, 1.179. The density model's (b, c) = (0.667, 0.333) sits inside the two median fits and just
  outside the two at-t fits; the theorem's (1, ≈ 0) and the transcript's (0.07, 0.89) are far from all four.
* **The three-law prefactor test reproduces exactly**, including every printed interval and every YES/NO:
  L_sign at t — density [0.790, 1.340] YES, theorem [0.694, 1.520] NO, transcript [0.491, 2.753] NO; L_sign median —
  density [0.862, 1.056] YES, theorem [0.571, 1.497] NO, transcript [0.484, 1.771] NO; L_bal3 at t — all NO; L_bal3
  median — density [0.767, 1.119] YES, the others NO.
* **Measured δ-ratios** at t: L_sign 4.79, 2.85, 2.72, 3.03; L_bal3 3.24, 5.30, 2.18, 2.89. On the medians (the ensemble
  instrument): L_sign 2.45, 3.02, 2.84, 2.91 (geometric mean **2.798**); L_bal3 2.14, 2.73, 2.62, 2.93 (geometric mean
  2.591). Against 5^{0.07} = 1.1193, 5^{2/3} = 2.9240, 5.

**Two repairs.**

1. **The "5" in "δ-ratios 1.12 : 2.9 : 5" is not the theorem's ratio; it is the ratio of the idealized δ⁻¹ scaling.**
   The theorem's L*(δ, t) = max(25/δ, 4δ⁻¹(log log(3 + t) + 2log(1/δ) + log(2b₁C₁))) carries a 2log(1/δ) inside the
   bracket, so its own tabulated δ-ratio is **L*(0.05)/L*(0.25) = 7.128 at t = 10³ and 6.950 at t = 10⁶** — read straight
   off CAMPAIGN.md's own reference table (862.48/120.99, 917.90/132.08). The campaign is measuring against a law it
   states as 5 while tabulating it as 7. The number 5 is inherited from PRICING §2(a); it should be labeled as the
   leading-order idealization and the tabulated 6.95–7.13 given beside it. **This makes the close firmer, not weaker.**
2. **The refutation of the theorem's law at "L_sign at t" has a 1.3 % margin.** Its interval [0.694, 1.520] exceeds the
   1.5 threshold only at the top end, by 0.020. Tested instead against the theorem's **exact** L*(δ, t) shape with a free
   prefactor, the checker gets [0.597, 1.754] (at t) and [0.504, 1.726] (median) — a refutation with real room. The
   sentence "the theorem's δ⁻¹ log log t [0.69, 1.52]" should carry the exact-shape figures beside it.

**Is "LANDS on the density model" supported at the stated tolerance? Yes, and the median is the statement to quote.**
On the ensemble median — the quantity the density model actually predicts — L_sign lands in [0.862, 1.056], a factor
1.06 either way; L_bal3 lands in [0.767, 1.119]. At a single t, L_sign lands in [0.790, 1.340] and L_bal3 does **not**
land ([0.710, 1.565]). CAMPAIGN.md says both of these correctly and identifies the median as the sharper instrument.

### §4.2 Close 2 — where the theorem's L* is spent: **CONFIRMED**

* L*(0.1, 10⁶) = 40·(2.6258 + 4.6052 + 2.8565) = **403.50**, shares **26.0 % / 45.7 % / 28.3 %** (printed 26/46/28);
  floor 4δ⁻¹(2log(1/δ) + log(2b₁C₁)) = 40·7.4616 = **298.5** (printed 298). Exact.
* Record-point ratios clause-4 bound / N_Z: **7.536·10⁴, 2.463·10⁵, 1.153·10⁶, 1.780·10⁵** at t = 10³…10⁶ (printed
  7.54e+04, 2.46e+05, 1.15e+06, 1.78e+05). Exact.
* The looseness factor (bound/N̄_Z)/L over the grid rows L ≥ 50, with N̄_Z the mean over the 143/145/147/149 centers:
  **[2.56, 4.54], [1.32, 1.57], [1.42, 1.83], [0.93, 1.16]** — every one of the eight printed endpoints reproduced to
  two decimals. The single-t ranges [1.38, 593], [0.25, 1], [3.20, 1817], [2.09, 122] also reproduce.
* The pricing's inferred "≈ 1.05·L" is confirmed at t = 10⁶ ([0.93, 1.16]) and is low by a factor 2.4–4.3 at t = 10³.
  CAMPAIGN.md states this honestly.

### §4.3 Close 3 — λ₀ = 25 and the crossing at 18.6: **CONFIRMED**

With the checker's own c(λ) (Gauss–Legendre; the record's route is a trapezoid rule), the least λ with 2c(λ)² ≥ e^{λ/2}
is **λ* = 18.582824** by bisection, hence **18.6** on the stated 0.1 grid — matching `zero_data_cost_run.log` (h) and the
per-height logs. The note's §3.3 margin c(25)²/e^{12.5} is **1.999107** against the note's "2.00". The statement
"proved from 23, contract 25" is a record fact and is correctly quoted.

### §4.4 Close 4 — R₀ = 81 and the true out-window radius: **CONFIRMED** with one repair

* **Arithmetic.** (7/(8·0.85))² = **1.0597** (note's "≈ 1.06"); (7/(8·(1/√2)))² = **1.5312** (CAMPAIGN's 1.53);
  (7/(8c_B))² = **37.4613** with c_B = 2/√(72e) = 0.14296065 (note D5's 37.4; CAMPAIGN's "asymptote 37.5"). The factor
  in R₀ between c_B and the numerical rate is (0.7071/c_B)² = **24.5** and (0.85/c_B)² = **35.4**, so CAMPAIGN's
  "a factor ≈ 25–35" is right.
* **The envelope 9η^{−3/4}e^{−√(η/2)}, checked at 40+ digits against the checker's own oscillatory quadrature**
  (`check-O/bhat_big.py`, log `bhat_big.log`; values stable under a 25-digit precision increase):
  B̂(1000) = **4.6771808548853636·10⁻¹²**, B̂(10000) = **−8.5705660470831506·10⁻³⁴**, B̂(16384) = **8.4373169428334·10⁻⁴³**.
  At η = 10³ and 10⁴ the envelope with A = 9 gives 9.843·10⁻¹² and 1.758·10⁻³³, i.e. **2.1× above the checker's
  point values** — the envelope is an upper envelope of an oscillating function, and the builder fitted it on
  max|B̂| over [η, η + 5] (A = 7.98, 8.60, 8.73, 8.60, 8.73, 8.67, 8.72 at η = 500 … 5·10⁴ in `logs/height_t1e3.log`).
  A = 9 is therefore a conservative envelope constant and the builder's use of it is sound. Local rate −log|B̂|/√η at the
  checker's points: 0.825 (η = 10³), 0.761 (10⁴) — consistent with the builder's 0.80 → 0.73 measured on the local maxima
  and with the saddle-point asymptote 1/√2 = 0.7071.
* **The note's tabulated |B̂(16384)| = 1.76·10⁻³⁷ was quadrature noise: CONFIRMED.** The true value is
  **8.437·10⁻⁴³**, smaller by a factor **2.1·10⁵**. The builder's "the true value is ≈ 10⁻⁴²" is right.
* **Clause-5 looseness, recomputed with the checker's own complex-argument quadrature** (log `outwin_check.log`;
  pair contribution 2Re[(u − i/2)²B̂(Lu − iL/2)²], clause-5 bound 2(u + ½)²e^{L/2}G(Lu)²): log₁₀(bound/|exact|) =
  **10.63** (L = 20, u = 5), **23.35** (20, 50), **14.33** (50, 5), **33.25** (50, 50), **19.84** (120, 5),
  **47.82** (120, 50) — against CAMPAIGN's 10.6, 23.4, 14.3, 33.3, 19.8, 47.8. Exact.
* **u_true, and the repair.** At the builder's u_true the checker's independent value of the true pair contamination is
  **0.9857·e^{−L}** at L = 20 and **0.9745·e^{−L}** at L = 50 — a 1.4–2.6 % difference in the value, which at the local
  decay rate corresponds to under 0.1 % in u. So **u_true/L = 1.09–1.10 at L = 30–120 is confirmed** and the close's
  "R ≈ 1.1·L against the proved 81L" stands. At L = 120, however, the checker finds **0.1728·e^{−L}** at the builder's
  u_true = 130.3613 (dps = 86): the contamination is already 5.8× below the target there, so the true crossing lies
  **below** 130.36 and u_true/L ≤ 1.086 at L = 120. The cause is that 2Re[(u − i/2)²B̂²] **changes sign** as u varies,
  so a plain bisection on its absolute value can land on a local dip rather than on the envelope crossing. The close is
  unaffected in substance (the radius is still ≈ 1.1·L, and the value quoted is if anything an overestimate); the
  sentence should say the bisection is on the oscillating value.

---

## §5 Task (5) — the V.4 controls

### §5.1 Positive control (ζ, silent): W_{Z′} ≥ 0 at every row of every height

| t | rows | min W_{Z′} over the rows | fine-grid points | min over the fine grid | clause-4 violations (L ≥ 50) |
|---|---|---|---|---|---|
| 10³ | 183 | 4.0953·10⁻¹⁹ | 1171 | 3.1256·10⁻⁸ | 0 |
| 10⁴ | 183 | 1.1696·10⁻¹² | 1171 | 1.7901·10⁻⁴ | 0 |
| 10⁵ | 183 | 3.4462·10⁻²³ | 1171 | 2.0325·10⁻⁸ | 0 |
| 10⁶ | 183 | 2.3336·10⁻¹⁹ | 1171 | 1.1430·10⁻⁶ | 0 |

**PASS at all 732 rows and all 4684 fine-grid bandwidths.** (W_{Z′} = Σ(γ − t)²B̂(L(γ − t))² is structurally a sum of
squares; the control's content is that the implementation is not sign-inverted and that the clause-4 bound is respected,
and both hold.) The negative control fires as recorded: at the record points the ratio |W_Z − W_{Z′}|/(δ²e^{δL/2}) is
15.2 … 1.44·10¹⁷ (CAMPAIGN §5), i.e. ≥ 1 at every L ≥ L*, and W_Z < 0 from L_sign upward.

### §5.2 The DH orbits — three of the 25 new off-line zeros of f_DH, re-verified at 30 digits

f_DH was re-coded from its definition (`results/ccm-dh-test/dh.py` docstring:
f_DH(s) = 5^{−s}[ζ(s, 1/5) + κζ(s, 2/5) − κζ(s, 3/5) − ζ(s, 4/5)], κ = (√(10 − 2√5) − 2)/(√5 − 1)) and evaluated with
`mp.dps = 30` (`check-O/dh_check.py`, log `dh_check.log`):

| stored ρ | &#124;f_DH(stored ρ)&#124; | refined ρ | &#124;f_DH(refined)&#124; | &#124;refined − stored&#124; | β | 0 < β < 1 | δ = &#124;β − ½&#124; (stored) |
|---|---|---|---|---|---|---|---|
| 0.650830080610 + 114.163342731 i | 1.758·10⁻¹⁵ | 0.650830080609737 + 114.163342730757 i | 4.09·10⁻³⁰ | 1.92·10⁻¹⁵ | 0.650830080610 | **yes** | 0.150830081 (0.150830081) |
| 0.846953803092 + 531.279726897 i | 5.023·10⁻¹⁴ | 0.846953803092049 + 531.279726896521 i | 2.27·10⁻²⁹ | 2.50·10⁻¹⁴ | 0.846953803092 | **yes** | 0.346953803 (0.346953803) |
| 0.688430136596 + 892.149034773 i | 3.131·10⁻¹⁴ | 0.688430136596400 + 892.149034773427 i | 3.19·10⁻²⁹ | 2.49·10⁻¹⁴ | 0.688430136596 | **yes** | 0.188430137 (0.188430137) |

All three are genuine zeros of f_DH (|f_DH| ≤ 3.2·10⁻²⁹ after a 30-digit Newton refinement that moves ρ by ≤ 2.5·10⁻¹⁴),
all three lie **strictly inside the strip 0 < β < 1**, none lies on the critical line, and the stored δ values are right
to nine decimals. **The claim "25 further off-line orbits in the strip" is supported at the three points sampled.**
(The scan's completeness — that no off-line orbit between the listed ones was missed — is not something a three-point
sample can establish, and the checker does not certify it; the builder's own method note in `dh_offline_scan.log`
describes the phase-count test that does.)

### §5.3 One of the three new-height control rows, recomputed with the checker's transform

t = 114.163343, δ = 0.150830, 39 DH on-line zeros in [t − 30, t + 30] (log `dh_control_check.log`). The builder's on-line
list was itself re-checked: max |Z_DH(γ)| over the 39 points at 25 digits is **1.857·10⁻³²**.

| L | W_Z (checker) | W_Z (builder) | rel | W_{Z′} (checker) | W_{Z′} (builder) | abs | main, rel | ratio to δ²e^{δL/2} (chk / bld) |
|---|---|---|---|---|---|---|---|---|
| 10 | −4.811630e−02 | −4.811630e−02 | 5.9e−14 | 1.6352e−03 | 1.6352e−03 | 2.9e−15 | 6.7e−16 | 1.0287 / 1.0287 |
| 20 | −6.428951e−02 | −6.428951e−02 | 4.1e−15 | 3.2235e−04 | 3.2235e−04 | 3.2e−16 | 8.9e−16 | 0.62848 / 0.62848 |
| 30 | −9.791593e−02 | −9.791593e−02 | 2.0e−15 | 3.7787e−06 | 3.7787e−06 | 2.6e−18 | 2.0e−15 | 0.44805 / 0.44805 |
| 40 | −1.692027e−01 | −1.692027e−01 | 2.2e−15 | 2.6563e−06 | 2.6563e−06 | 5.5e−17 | 1.8e−15 | 0.3642 / 0.3642 |
| 50 | −3.256405e−01 | −3.256405e−01 | 1.8e−15 | 1.8597e−07 | 1.8597e−07 | 1.2e−17 | 1.8e−15 | 0.32972 / 0.32972 |
| 60 | −6.836912e−01 | −6.836912e−01 | 1.3e−15 | 2.4473e−08 | 2.4473e−08 | 3.1e−18 | 1.3e−15 | 0.32564 / 0.32564 |
| 70 | −1.539834e+00 | −1.539834e+00 | 0 | 2.5974e−08 | 2.5974e−08 | 6.3e−18 | 0 | 0.34501 / 0.34501 |
| 80 | −3.671776e+00 | −3.671776e+00 | 1.6e−15 | 2.1945e−09 | 2.1945e−09 | 3.7e−19 | 1.6e−15 | 0.387 / 0.387 |
| **217.48 = L\*** | **−9.258755e+06** | **−9.258755e+06** | 6.7e−14 | 2.5684e−14 | 2.5684e−14 | 1.5e−21 | 6.7e−14 | **30.66 / 30.66** |
| 100 | −2.385146e+01 | −2.385146e+01 | 7.6e−15 | 6.5281e−10 | 6.5281e−10 | 7.9e−19 | 7.6e−15 | 0.5563 / 0.5563 |

**PASS**: every one of the ten rows reproduces to ≤ 6.7·10⁻¹⁴ relative on W_Z and ≤ 1.5·10⁻²¹ absolute on W_{Z′}. The
control fires at the theorem's bandwidth (ratio 30.66 ≥ 1 at L* = 217.48). The builder's caveats — the window hypothesis
is not verified (the scan finds an orbit roughly every 35 units), the reflection condition t ≥ 21L* fails at t = 114 as
it does at 85.7, the reflected points are omitted — are stated in the script docstring, in the log and in CAMPAIGN.md §1,
and are the same caveats the record already carries for t = 85.7 (MAJOR-2 of the note's referee corrections). With them,
"the negative control now stands at four heights" is a correct statement about the MECHANISM and the DATUM, not an
instance of the theorem's hypotheses.

---

## §6 Task (6) — the four stop conditions

| | condition, as PRICING §2(e) writes it | the builder's evaluation | the checker's | verdict |
|---|---|---|---|---|
| (i) | `zetazero` at n ≈ 1.75·10⁶ exceeds 2 s per zero in the rehearsal | 0.329 s/zero (5 consecutive zeros at n = 1 747 146–150) | the four production runs measured 0.166 / 0.600 / 0.422 / 0.344 s per zero, all far under 2 s; the checker's own 30-digit re-verification cost 1–4 s per zero, which is the 30-digit price, not the 15-digit one the condition names | **does not fire** |
| (ii) | the rehearsal's positive control at t = 10³ shows W_{Z′} < 0 at any L | min 4.095·10⁻¹⁹ over 183 rows and 1171 fine-grid L | §5.1: min over all 732 rows and 4684 fine-grid L across all four heights is 3.4462·10⁻²³ > 0 | **does not fire** |
| (iii) | the checker's independent transform disagrees with the builder's on any row by more than 10⁻⁸ relative | pending | §2.2: worst relative difference on W_Z over the eight contracted rows is **1.7·10⁻¹²**; worst absolute difference on W_{Z′} is **5.7·10⁻¹⁶** (and ≤ 3.0·10⁻²⁵ on the four extreme record rows) | **does not fire** |
| (iv) | the density model and the measured N_Z differ by more than a factor 10 at 10³ | restated on the center mean: [0.42, 1.08], geometric mean 0.65 → does not fire | **as written it FIRES**: see below | **fires as written; does not fire as restated** |

### §6.1 Stop condition (iv): is the builder's restatement legitimate, or a weakening?

The literal condition compares the model log(t/2π)·‖B′‖₂²/L³ with "the measured N_Z" at t. Recomputed over the 59 grid
bandwidths at each height (`closes_check.log` §6):

| t | single-t N_Z/model: min | max | geometric mean | grid rows outside [0.1, 10] | literal verdict | center-mean version | restated verdict |
|---|---|---|---|---|---|---|---|
| 10³ | 0.0032 | 2.5796 | 0.4217 | **10 of 59** | **FIRES** | [0.4222, 1.0815], gm 0.6524 | does not fire |
| 10⁴ | 0.3578 | 5.5245 | 2.4208 | 0 of 59 | does not fire | [0.8859, 1.1586], gm 0.9831 | does not fire |
| 10⁵ | 0.0007 | 1.2424 | 0.1276 | **25 of 59** | **FIRES** | [0.6868, 1.0371], gm 0.8150 | does not fire |
| 10⁶ | 0.0099 | 1.4353 | 0.2779 | **11 of 59** | **FIRES** | [0.9090, 1.2972], gm 1.1008 | does not fire |

**The answer is: legitimate as mathematics, a weakening as a stop condition, and under-recorded in CAMPAIGN.md.**

* **Legitimate.** PRICING §2(a)(4) states the model's derivation in the same sentence that introduces it: "**I infer** it
  from N_Z ≈ ∫|h_f(r)|²·(log(r/2π)/2π)dr and Parseval". Replacing the sum over ζ's zeros by an integral against the mean
  density is precisely an ensemble average, so the model predicts E[N_Z], not N_Z at one t. At L ≳ 20 the kernel
  (r − t)²B̂(L(r − t))² has width ≈ 5/L, far below the mean zero gap 2π/log(t/2π) ≈ 0.5–0.8 at these heights, so N_Z(t)
  is dominated by one or two nearest zeros and is a single draw from a broad distribution; it vanishes whenever the
  nearest zero sits near a zero of B̂ (the dips at L = 48, 86, 120 at t = 10³, which the builder identifies). Comparing a
  single draw with a mean at a factor-10 tolerance is not a test of the model. The builder's restatement is the correct
  comparison, it is implemented consistently (close 2's looseness factor is computed against the same center mean), and
  under it the model holds to within a factor 1.5 at every height.
* **A weakening.** The condition was restated **after** the literal form fired in the rehearsal. A stop condition exists
  to be fixed in advance; changing it on the evidence it was meant to gate is the failure mode it guards against, and
  the campaign then ran three more heights under the changed rule. The substantive cost is not zero: the literal reading
  is a true statement about the instrument — **at a single height and bandwidth the density model does not predict N_Z
  within a factor 10; it is off by up to a factor 1400 low at t = 10⁵** — and that is a finding, not a nuisance.
* **Mitigation, on the record.** The builder did not hide it. `logs/height_t1e3.log` line 254 prints the literal verdict
  "FIRES" verbatim with its numbers; `summary_*.json` carries `single_t_geomean` and `single_t_outside_10x` at every
  height; STATUS-campaign.md §5 states the restatement and its reason. What is missing is the same statement in
  **CAMPAIGN.md**, whose §1 column heading reads only "stop (iv): center-mean N_Z/model" and whose §4 close 2 rests on
  the same center mean. §7 gives the wording.
* **Does the restatement damage the closes?** No. Close 1 is about L_sign and L_bal3, which are **thresholds in L**;
  a threshold is far more stable than the quantity whose level it is read off, which is why L_sign at t lands within
  [0.79, 1.34] of the density law while N_Z at t scatters over three orders. Close 2's looseness factor is explicitly
  quoted with both the center-mean and the single-t ranges. §2(d) item 2's inference therefore survives in its ensemble
  form, which is the form CAMPAIGN.md states.

---

## §7 Corrections — exact wording for CAMPAIGN.md

Insertion-only; none of them changes a computed number, and none of them changes a close's verdict.

1. **§3 header is the one table header without the INSTRUMENT label** (the requirement of the brief and of standing
   order 4; §1, §2, §4, §5, §6 and §7 all carry it). Read:
   `## 3. The three-law comparison (PRICING §2(a) last paragraph; §2(d) item 1) — δ-ratios 1.12 : 2.9 : 5 (INSTRUMENT — decides the detection-bandwidth law; nothing about RH)`

2. **§3, first line, and §4 close 1 — the theorem's δ-ratio.** After
   "and 5 (theorem, L* ∝ δ⁻¹)" insert: **"— 5 is the ratio of the leading δ⁻¹ scaling; the theorem's L* as tabulated
   below carries 2log(1/δ) inside its bracket and its own δ-ratio is L*(0.05)/L*(0.25) = 7.13 at t = 10³ and 6.95 at
   t = 10⁶."**

3. **§4 close 1 — the theorem law's refutation margin.** After "(the theorem's δ⁻¹ log log t [0.69, 1.52]" insert:
   **"— a margin of 1.3 % over the 1.5 threshold; tested against the theorem's exact L*(δ, t) shape with a free
   prefactor the interval is [0.60, 1.75] at t and [0.50, 1.73] on the medians, so the refutation does not depend on
   the idealization"**.

4. **§1 — stop condition (iv).** Change the column heading to
   **"stop (iv): as written (single t) / as restated (center mean)"** and add the following sentence under the table:
   **"Stop condition (iv) as PRICING §2(e) writes it compares the density model with the measured N_Z at t, and in that
   form it FIRES: 10 of the 59 grid bandwidths at t = 10³ (also 25 of 59 at 10⁵ and 11 of 59 at 10⁶) are outside a
   factor 10 of the model, the geometric means being 0.42, 2.42, 0.13, 0.28. The rule was restated on the mean over the
   143–149 centers, because the model is an ensemble mean by construction (PRICING §2(a)(4) derives it by replacing the
   zero sum with an integral against the mean density) and the single-t value at L ≳ 20 is dominated by the nearest zero;
   in that form it does not fire at any height ([0.42, 1.08], [0.89, 1.16], [0.69, 1.04], [0.91, 1.30]). Both forms are
   in `summary_<tag>.json` (`single_t_*` keys) and in `logs/height_t1e3.log`. The restatement was made after the literal
   form fired in the rehearsal; the finding it carries — that the density model does not predict N_Z at a single height
   and bandwidth within a factor 10 — stands as a measured property of the instrument."**

5. **§4 close 4 — the u_true bisection.** After "the radius at which the TRUE contamination of a depth-½ orbit falls to
   e^{−L} is u_true/L = …" insert: **"(the bisection runs on the signed value 2Re[(u − i/2)²B̂(Lu − iL/2)²], which
   changes sign in u, so a listed u_true can sit on a local dip: the checker's independent 86-digit evaluation finds
   0.986·e^{−L} at L = 20 and 0.975·e^{−L} at L = 50 but 0.173·e^{−L} at L = 120, i.e. u_true/L ≤ 1.086 there)"**.

6. **§4 close 4 — "(7/(8·0.707))² = 1.53" is typed into `aggregate.py`'s template, not printed by any script or log.**
   Either compute it in `aggregate.py` from `math.sqrt(2)` and print it, or cite `check-O/closes_check.log` §4, which
   prints 1.5312, 1.0597 and 37.4613. (10(g): every number to a script and a log.)

7. **§0, the truncation paragraph — the shell-log covering.** After "with the shell count 2C₁ℓ_R" insert:
   **"(ℓ_R = log(4 + t + R₀L) covers the shells j ≤ R₀L − ½; beyond that the shell log exceeds ℓ_R, and the checker
   computed the true ratio Σ j^{2−2k}log(3.5 + t + j)/(ℓ_R Σ j^{2−2k}) at the operating points to be 0.88–0.99999, so
   the printed bounds are upper bounds — `check-O/closes_check.log`)"**.

8. **§5, the "N_Z/model" column at the record points** prints 0.000 at most rows. The density model is an L⁻³ law for the
   noise at bandwidths where several zeros contribute; at L = 400–2600 only 25–378 zeros survive the truncation and the
   kernel sees essentially none of them. Add a footnote to §5: **"N_Z/model at the record points is out of the model's
   regime (the model averages over zeros the kernel no longer reaches); it is printed for completeness, and close 1 and
   close 2 use the grid rows and the center means."**

**Lint and labels, checked (10(g)).** The four banned hedges ("clearly", "obviously", "easy to see", "well known") do not
occur in `CAMPAIGN.md` or `STATUS-campaign.md`. No British spelling occurs in either file: the checker grepped thirty
British forms (the -ise / -yse, -our, -re and -ll-before-suffix families, plus the usual lexical pairs) — zero hits. Every table header carries INSTRUMENT except §3 (item 1 above). Every number traced
to a script or log except the two of item 6. `date` stamps are present in `CAMPAIGN.md`'s preamble, `STATUS-campaign.md`
and every log.

---

## §8 What the checker did not check

* The **completeness** of the DH off-line scan (that no orbit between the 26 listed was missed) — three of 25 were
  re-verified as genuine off-line zeros; the absence of others is the builder's phase-count argument and is not
  independently confirmed here.
* The **ensemble machinery** (the 143–149 centers, the p10/p90 bands, `bhat_fast`'s spline) beyond the checks that the
  per-L means in `summary_*.json` reproduce close 2's printed intervals and that the per-height medians reproduce
  CAMPAIGN.md §2. The two contracted rows per height were computed with the exact transform, not the spline.
* The **direct E₋ values** and the reflected on-line terms (item (7)), which are excluded from W_Z by construction and
  enter no close.
* Any statement about **RH**. The campaign is an instrument; so is this report.

---

## §9 Traceability

| item | script | log / data |
|---|---|---|
| the checker's transform and its accuracy floor | `check-O/ind_transform.py` | quoted in `closes_check.log` |
| 20 zeros × 4 heights at 30 digits, map audit | `check-O/verify_zeros.py` | `zeros_check.log`, `zeros_check.json` |
| two (+ one extreme) rows × 4 heights | `check-O/recompute_rows.py` | `rows_check.log`, `rows_check.json` |
| ‖B^{(k)}‖₁, k = 1…13, and the tail bound | `check-O/deriv_norms.py` | `deriv_norms.log`, `deriv_norms.json` |
| B̂ at η = 10³, 10⁴, 16384 at 40+ digits | `check-O/bhat_big.py` | `bhat_big.log` |
| clause-5 looseness and u_true | `check-O/outwin_check.py`, `owosc.py` | `outwin_check.log` |
| three DH orbits at 30 digits | `check-O/dh_check.py` | `dh_check.log` |
| the t = 114.16 control row | `check-O/dh_control_check.py` | `dh_control_check.log` |
| closes 1–4, positive control, stop conditions, lint | `check-O/closes_check.py` | `closes_check.log` |

**Headline, restated in one line: the campaign's numbers are right — PASS at all four heights, stop condition (iii) does
not fire — closes 2, 3 and 4 are confirmed as stated, close 1 is confirmed with two wording repairs, and the one thing a
reader must be told that `CAMPAIGN.md` does not currently say is that stop condition (iv) fires in the form the contract
wrote it and was restated on an ensemble mean.**
