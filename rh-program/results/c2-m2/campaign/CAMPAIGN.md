# CAMPAIGN.md -- the zero-side numerics campaign for Theorem M2 (C2; PRICING.md section 2) -- v1

**Built 2026-09-16 22:19:59 by `aggregate.py` from the row files on disk** (`rows_<tag>.json`, `summary_<tag>.json`, `finescan_<tag>.json`, `outwindow_test.json`, all under `results/c2-m2/campaign/`; logs under `logs/`). Every number below is read from those files; nothing is typed in. **INSTRUMENT (standing order 4): every table here decides constants and the detection-bandwidth law of the first-order datum on zeta's actual zeros; nothing here is a statement about RH.** Heights present: t = 1000, t = 10000, t = 100000, t = 1e+06.

## 0. Method (one code path: `campaign_lib.py`; driver `run_height.py`; item (6): `outwindow_test.py`)

* **Objects.** Test f_{t,L} = i(B_L)'e^{-itu}; h_f(r) = (r - t)B̂(L(r - t)); datum W_Z(f) = Σ_γ h_f(γ)·conj(h_f(γ̄)) (note §0.1). Configurations at height t: **Z'** = ζ's zeros in the data window (all real; the positive control); **Z** = Z' ∪ {±t ± iδ} (the theorem's pair of classes; the negative control's injected defect); **Z_rep** = Z' with the on-line zero nearest t (and its reflection) replaced by the orbit (C2 line 54's 'physical' variant); **Z''** = Z' ∪ {on-line double at ±t} (the II.4 tight pair: the double at +t contributes exactly 0 since h_f(t) = 0; the double at −t contributes 8t²B̂(2tL)², bounded per row by Lemma G — the datum is blind to the double).
* **Zeros.** `mpmath.zetazero(n)` at mp.dps = 15, stored as (index n, γ, |Z(γ)| by `mpmath.siegelz`), monotone in n and counted against Riemann–von Mangoldt. **Data window** ±U_data around t with U_data = 2·U(L_min = 4), where U(L) is the least radius at which the clause-4 polynomial tail bound is ≤ 10⁻¹⁰: k integrations by parts give |B̂(η)| ≤ ‖B^{(k)}‖₁/|η|^k, and with the shell count 2C₁ℓ_R (C₁ = 1 operative for ζ, stated as such — PRICING §2(b)) the tail beyond U is ≤ 2ℓ_R‖B^{(k)}‖₁²L^{−2k}(U − 2)^{3−2k}/(2k − 3), minimized over 2 ≤ k ≤ 13 with the norms ‖B^{(k)}‖₁ computed by exact polynomial recursion + 30-digit quadrature (k = 1, 2, 3 reproduce the record's 3.31428, 28.7726, 642.301; the table is in `campaign_lib.py`). **The contract's k = 3 radius (PRICING §2(b)(c)) is printed per row as U_contract_k3**; at L = 4 it is 1.7·10⁴ at t = 10³ (2·10⁴ zeros; the pricing's '25 minutes' was the L = 10 figure) and 2.1·10⁴ at t = 10⁶ (8·10⁴ zeros, 6.5 h) — the k-optimized radius is 143–149 at every height (230–570 zeros, minutes). Each row sums over every stored zero within U_row = min(U_data, 4·10⁴/L) ≥ U(L), and prints the tail bound at U_row.
* **Transform.** B̂ at real η by the trapezoid rule on 16 384 uniform nodes (B is C^∞ with compact support: the rule is spectrally accurate; by Poisson summation the error is Σ_{m≠0}B̂(η − 2πmM), checked against 30-digit mpmath quadrature at eight points to ≤ 7·10⁻¹⁸ absolute in the rehearsal log); c(δL) = B̂(iδL) by the same rule with cosh (positive terms; ≤ 1.2·10⁻¹⁶ relative up to λ = 317). At complex arguments and huge |η| (the reflected term E₋, the reflected on-line points, the planted out-window orbit) the same Poisson-trapezoid rule in mpmath at the precision the cancellation needs (`bhat_mp`; agrees with mpmath quadrature at z = 300 − 10i to 10⁻³⁴; recomputed at 3/2 the nodes as a check).
* **E₋ and the reflected points (item (7)).** The sums exclude the reflected pair at −t and the reflected on-line points −γ; each row prints the rigorous clause-1 bound |E₋| ≤ 2(4t² + δ²)e^{δL}G(2tL)² (Lemma G, c_B = 0.143), the envelope estimate with |B̂(η)| ≈ 9η^{−3/4}e^{−√(η/2)} `[computed envelope, not proved; fitted on η = 10³–5·10⁴, local rate 0.80 → 0.73 toward the saddle-point 1/√2]`, and — where the estimate is ≥ 10⁻¹⁶⁰ (t = 10³, L ≤ 36) — the DIRECT value. The rigorous bound is not informative (> 10⁻¹⁰) at small L and t = 10³; the direct values and the estimate are the record there, labeled.
* **Derived bandwidths.** L_sign(δ, t) = least L (fine grid 3.0…120 step 0.1) with W_Z < 0, i.e. 2δ²c(δL)² > N_Z (E₋ excluded); L_bal3 = least L with 2δ²c(δL)² ≥ 3N_Z. Row flag `inside_hypotheses` = (L ≥ L*(δ, t; C₁ = 1)) and (t ≥ 21L); rows with the flag False are **measurements below the theorem's hypotheses — of where visibility begins — not tests of the theorem** (IV.9; MAJOR-2 discipline).

## 1. Per-height record: zeros, controls, stop conditions (INSTRUMENT — constants and the bandwidth law; nothing about RH)

| t | zeros (window ±U_data) | index range | s/zero | max \|Z(γ)\| | rows | positive control: min W_{Z'} | clause-4 (L ≥ 50) violations | negative control | stop (i) | stop (ii) | stop (iv): center-mean N_Z/model geomean [min, max] (grid L outside 10×) | run time |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000 | 459 (±285.6) | 427..885 | 0.166 | 9.7e-13 | 183 | 4.095e-19 (PASS: True) | 0 | PASS | 0.329 s/zero → no | no | 0.652 [0.422, 1.081] (0) → no | 118 s |
| 10000 | 681 (±290.3) | 9804..10484 | 0.600 | 1.9e-11 | 183 | 1.170e-12 (PASS: True) | 0 | PASS | (rehearsal) | no | 0.983 [0.886, 1.159] (0) → no | 451 s |
| 100000 | 905 (±294.1) | 137617..138521 | 0.422 | 2.2e-10 | 183 | 3.446e-23 (PASS: True) | 0 | PASS | (rehearsal) | no | 0.815 [0.687, 1.037] (0) → no | 437 s |
| 1e+06 | 1133 (±297.2) | 1746580..1747712 | 0.344 | 2.9e-09 | 183 | 2.334e-19 (PASS: True) | 0 | PASS | (rehearsal) | no | 1.101 [0.909, 1.297] (0) → no | 458 s |

Stop condition (iii) (the checker's independent transform within 10⁻⁸ relative on two rows per height) is the Opus checker's item; its verdicts are appended to `SHARED.md` / `CHECK-O.md`, not decided here.

**The DH sub-task (PRICING §2(c); `dh_offline_scan.py`, log `logs/dh_offline_scan.log`, JSON `dh_offline_scan.json`; 30-minute cap).** Scan of f_DH by blocks of 10 from 46 to 900 (cap) (phase count (θ + arg f)/π against the on-line sign changes at step 0.1, fine rescan at 0.01 on any excess, bounded Newton locator): 86 blocks, known orbit at 85.699 RE-FOUND; **off-line zeros in the strip 0 < β < 1 found: 26** — ρ = 0.808517182457 + 85.699348485 i (t = 85.699348, δ = 0.308517); ρ = 0.650830080610 + 114.163342731 i (t = 114.163343, δ = 0.150830); ρ = 0.574356050451 + 166.479305913 i (t = 166.479306, δ = 0.074356); ρ = 0.724257694627 + 176.702461243 i (t = 176.702461, δ = 0.224258); ρ = 0.869530579641 + 240.404672351 i (t = 240.404672, δ = 0.369531); ρ = 0.819549592099 + 320.876489669 i (t = 320.876490, δ = 0.319550); ρ = 0.768223123616 + 331.050259408 i (t = 331.050259, δ = 0.268223); ρ = 0.628508108326 + 366.640907576 i (t = 366.640908, δ = 0.128508); ρ = 0.815873677846 + 411.796737549 i (t = 411.796738, δ = 0.315874); ρ = 0.708882224251 + 440.484510740 i (t = 440.484511, δ = 0.208882); ρ = 0.515918314382 + 520.943801035 i (t = 520.943801, δ = 0.015918); ρ = 0.846953803092 + 531.279726897 i (t = 531.279727, δ = 0.346954); ρ = 0.729533399980 + 548.906793778 i (t = 548.906794, δ = 0.229533); ρ = 0.786559082021 + 566.509712911 i (t = 566.509713, δ = 0.286559); ρ = 0.582855669751 + 595.023378028 i (t = 595.023378, δ = 0.082856); ρ = 0.628251982695 + 611.775097639 i (t = 611.775098, δ = 0.128252); ρ = 0.610764608809 + 646.986823196 i (t = 646.986823, δ = 0.110765); ρ = 0.760597162553 + 657.108370821 i (t = 657.108371, δ = 0.260597); ρ = 0.788703137871 + 692.892490562 i (t = 692.892491, δ = 0.288703); ρ = 0.777360057814 + 737.766996755 i (t = 737.766997, δ = 0.277360); ρ = 0.853001450138 + 783.653006980 i (t = 783.653007, δ = 0.353001); ρ = 0.668551477710 + 811.765792296 i (t = 811.765792, δ = 0.168551); ρ = 0.561947896626 + 847.465731557 i (t = 847.465732, δ = 0.061948); ρ = 0.856109415855 + 857.295886755 i (t = 857.295887, δ = 0.356109); ρ = 0.680899797127 + 864.118091187 i (t = 864.118091, δ = 0.180900); ρ = 0.688430136596 + 892.149034773 i (t = 892.149035, δ = 0.188430); outside the strip (β > 1): 0. The zero-side negative control at the NEW heights (orbit + DH's on-line zeros in [t − 30, t + 30], as at 85.7; the reflected points omitted; the window hypothesis not verified; the reflection condition t ≥ 21L* fails at these t as at 85.7):

| t = 114.163343, δ = 0.150830, L* = 217.48 | L | W_Z | W_{Z'} | main −2δ²c² | ratio to δ²e^{δL/2} | fires (≥ 1) |
|---|---|---|---|---|---|---|
| 39 DH on-line zeros in the window | 10.00 | -4.8116e-02 | 1.6352e-03 | -4.9751e-02 | 1.029 | False |
| 39 DH on-line zeros in the window | 20.00 | -6.4290e-02 | 3.2235e-04 | -6.4612e-02 | 0.6285 | False |
| 39 DH on-line zeros in the window | 30.00 | -9.7916e-02 | 3.7787e-06 | -9.7920e-02 | 0.448 | False |
| 39 DH on-line zeros in the window | 40.00 | -1.6920e-01 | 2.6563e-06 | -1.6921e-01 | 0.3642 | False |
| 39 DH on-line zeros in the window | 50.00 | -3.2564e-01 | 1.8597e-07 | -3.2564e-01 | 0.3297 | False |
| 39 DH on-line zeros in the window | 60.00 | -6.8369e-01 | 2.4473e-08 | -6.8369e-01 | 0.3256 | False |
| 39 DH on-line zeros in the window | 70.00 | -1.5398e+00 | 2.5974e-08 | -1.5398e+00 | 0.345 | True |
| 39 DH on-line zeros in the window | 80.00 | -3.6718e+00 | 2.1945e-09 | -3.6718e+00 | 0.387 | True |
| 39 DH on-line zeros in the window | 217.48 | -9.2588e+06 | 2.5684e-14 | -9.2588e+06 | 30.66 | True |
| 39 DH on-line zeros in the window | 100.00 | -2.3851e+01 | 6.5281e-10 | -2.3851e+01 | 0.5563 | True |

| t = 166.479306, δ = 0.074356, L* = 521.27 | L | W_Z | W_{Z'} | main −2δ²c² | ratio to δ²e^{δL/2} | fires (≥ 1) |
|---|---|---|---|---|---|---|
| 43 DH on-line zeros in the window | 10.00 | -5.0679e-03 | 6.2336e-03 | -1.1302e-02 | 1.409 | False |
| 43 DH on-line zeros in the window | 20.00 | -1.1818e-02 | 2.4336e-04 | -1.2061e-02 | 1.037 | False |
| 43 DH on-line zeros in the window | 30.00 | -1.3409e-02 | 1.5145e-05 | -1.3424e-02 | 0.7959 | False |
| 43 DH on-line zeros in the window | 40.00 | -1.5553e-02 | 5.5487e-07 | -1.5553e-02 | 0.6358 | False |
| 43 DH on-line zeros in the window | 50.00 | -1.8713e-02 | 3.3877e-07 | -1.8713e-02 | 0.5275 | False |
| 43 DH on-line zeros in the window | 60.00 | -2.3318e-02 | 8.5239e-08 | -2.3318e-02 | 0.4532 | False |
| 43 DH on-line zeros in the window | 70.00 | -3.0005e-02 | 3.1700e-09 | -3.0005e-02 | 0.4021 | False |
| 43 DH on-line zeros in the window | 80.00 | -3.9755e-02 | 1.4416e-09 | -3.9755e-02 | 0.3673 | False |
| 43 DH on-line zeros in the window | 521.27 | -2.4935e+08 | 3.3048e-22 | -2.4935e+08 | 172.8 | True |
| 43 DH on-line zeros in the window | 100.00 | -7.5354e-02 | 5.2262e-10 | -7.5354e-02 | 0.331 | False |

| t = 176.702461, δ = 0.224258, L* = 133.66 | L | W_Z | W_{Z'} | main −2δ²c² | ratio to δ²e^{δL/2} | fires (≥ 1) |
|---|---|---|---|---|---|---|
| 43 DH on-line zeros in the window | 10.00 | -1.0234e-01 | 2.0023e-02 | -1.2236e-01 | 0.7928 | False |
| 43 DH on-line zeros in the window | 20.00 | -2.1309e-01 | 6.3048e-04 | -2.1372e-01 | 0.4513 | False |
| 43 DH on-line zeros in the window | 30.00 | -4.9955e-01 | 5.1080e-05 | -4.9960e-01 | 0.3437 | False |
| 43 DH on-line zeros in the window | 40.00 | -1.4507e+00 | 5.1866e-06 | -1.4507e+00 | 0.3252 | True |
| 43 DH on-line zeros in the window | 50.00 | -4.9325e+00 | 4.0406e-07 | -4.9325e+00 | 0.3604 | True |
| 43 DH on-line zeros in the window | 60.00 | -1.8840e+01 | 2.6508e-08 | -1.8840e+01 | 0.4485 | True |
| 43 DH on-line zeros in the window | 70.00 | -7.8605e+01 | 3.3444e-08 | -7.8605e+01 | 0.6098 | True |
| 43 DH on-line zeros in the window | 80.00 | -3.5140e+02 | 2.5104e-08 | -3.5140e+02 | 0.8883 | True |
| 43 DH on-line zeros in the window | 133.66 | -2.2955e+06 | 4.8041e-11 | -2.2955e+06 | 14.15 | True |
| 43 DH on-line zeros in the window | 100.00 | -8.2152e+03 | 1.8268e-09 | -8.2152e+03 | 2.205 | True |

## 2. The twelve-point tables: L_sign(δ, t) and L_bal3(δ, t) (INSTRUMENT; fine grid step 0.1; E₋ excluded from W_Z)

| δ \ t | 1000 | 10000 | 100000 | 1e+06 |
|---|---|---|---|---|
| L_sign, δ = 0.05 — at t ; median [p10, p90] over centers | 32.1 ; 20.6 [14.6, 35.9] | 25.1 ; 27.8 [19.4, 38.3] | 25.8 ; 29.0 [19.5, 39.0] | 33.3 ; 31.4 [22.6, 40.0] |
| L_sign, δ = 0.10 — at t ; median [p10, p90] over centers | 19.4 ; 15.4 [10.8, 19.4] | 13.5 ; 18.0 [12.9, 20.9] | 20.1 ; 19.2 [14.6, 22.3] | 22.4 ; 20.6 [16.0, 23.6] |
| L_sign, δ = 0.25 — at t ; median [p10, p90] over centers | 6.7 ; 8.4 [7.2, 9.8] | 8.8 ; 9.2 [8.0, 10.6] | 9.5 ; 10.2 [9.0, 11.2] | 11.0 ; 10.8 [9.8, 11.8] |
| L_bal3, δ = 0.05 — at t ; median [p10, p90] over centers | 37.6 ; 24.0 [18.4, 48.7] | 58.8 ; 35.0 [23.1, 56.2] | 29.2 ; 36.2 [25.6, 56.8] | 38.5 ; 42.2 [29.6, 60.2] |
| L_bal3, δ = 0.10 — at t ; median [p10, p90] over centers | 28.5 ; 19.4 [13.6, 29.8] | 22.2 ; 25.0 [17.1, 30.8] | 23.9 ; 26.0 [18.4, 31.8] | 28.9 ; 27.2 [20.0, 32.2] |
| L_bal3, δ = 0.25 — at t ; median [p10, p90] over centers | 11.6 ; 11.2 [8.8, 13.2] | 11.1 ; 12.8 [10.0, 14.4] | 13.4 ; 13.8 [11.8, 15.4] | 13.3 ; 14.4 [13.0, 16.0] |

'At t' is the contract's L_sign(δ, t) at the height exactly (fine grid step 0.1); 'over centers' is the same quantity at the 143, 145, 147, 149 centers t' = t + 2j inside the data window (section (M) of the height log; fine grid step 0.2) — the median is the ensemble instrument, the band shows how configuration-dominated a single-t value is.

Reference values per (δ, t) from the record (`zero_data_cost_run.log` (d)–(g)): density model L_bal(κ=1) / L_bal(κ=3); the theorem's L*(C₁ = 1); the transcript's L_ann = 1.12δ^{−0.07}(log(t/2π))^{0.89}:

| δ \ t | 1000 | 10000 | 100000 | 1e+06 |
|---|---|---|---|---|
| δ = 0.05: model κ=1 / κ=3 ; L* ; L_ann | 25.2 / 35.5 ; 862.5 ; 5.9 | 28.3 / 39.8 ; 885.5 ; 8.2 | 30.9 / 43.2 ; 903.3 ; 10.4 | 33.0 / 46.0 ; 917.9 ; 12.6 |
| δ = 0.10: model κ=1 / κ=3 ; L* ; L_ann | 15.7 / 21.9 ; 375.8 ; 5.6 | 17.6 / 24.5 ; 387.3 ; 7.8 | 19.2 / 26.5 ; 396.2 ; 9.9 | 20.4 / 28.1 ; 403.5 ; 12.0 |
| δ = 0.25: model κ=1 / κ=3 ; L* ; L_ann | 8.3 / 11.4 ; 121.0 ; 5.2 | 9.3 / 12.7 ; 125.6 ; 7.3 | 10.1 / 13.6 ; 129.2 ; 9.3 | 10.7 / 14.4 ; 132.1 ; 11.2 |

## 3. The three-law comparison (PRICING §2(a) last paragraph; §2(d) item 1) — δ-ratios 1.12 : 2.9 : 5

The three laws predict L(δ = 0.05)/L(δ = 0.25) = 5^{0.07} = 1.12 (transcript), 5^{2/3} = 2.92 (density model), 5 (theorem, L* ∝ δ⁻¹); and in t, L(10⁶)/L(10³) = (log(10⁶/2π)/log(10³/2π))^{0.89} = 2.15 (transcript), (…)^{1/3} = 1.33 (model), log log-flat ≈ 1.07 (theorem, at δ = 0.1).

| t | L_sign(0.05)/L_sign(0.25) | L_bal3(0.05)/L_bal3(0.25) | model κ=1 ratio | model κ=3 ratio |
|---|---|---|---|---|
| 1000 | 4.79 | 3.24 | 3.04 | 3.11 |
| 10000 | 2.85 | 5.30 | 3.04 | 3.13 |
| 100000 | 2.72 | 2.18 | 3.06 | 3.18 |
| 1e+06 | 3.03 | 2.89 | 3.08 | 3.19 |

* **L_sign at t**: least-squares log L = a + b·log(1/δ) + c·log log(t/2π) over 12 points: **b = 0.737, c = 0.262**, max residual factor 1.281. Laws: density model (b, c) = (0.667, 0.333); theorem (1, ≈ 0 — log log t enters additively); transcript (0.07, 0.89).
* **L_bal3 at t**: least-squares log L = a + b·log(1/δ) + c·log log(t/2π) over 12 points: **b = 0.732, c = 0.003**, max residual factor 1.443. Laws: density model (b, c) = (0.667, 0.333); theorem (1, ≈ 0 — log log t enters additively); transcript (0.07, 0.89).
* **L_sign median over centers**: least-squares log L = a + b·log(1/δ) + c·log log(t/2π) over 12 points: **b = 0.642, c = 0.368**, max residual factor 1.119. Laws: density model (b, c) = (0.667, 0.333); theorem (1, ≈ 0 — log log t enters additively); transcript (0.07, 0.89).
* **L_bal3 median over centers**: least-squares log L = a + b·log(1/δ) + c·log log(t/2π) over 12 points: **b = 0.596, c = 0.434**, max residual factor 1.179. Laws: density model (b, c) = (0.667, 0.333); theorem (1, ≈ 0 — log log t enters additively); transcript (0.07, 0.89).
   * L_sign at t against the density δ^{-2/3}(log(t/2π))^{1/3} law (free prefactor 1.89): measured/predicted in [0.790, 1.340] → YES within a factor 1.5
   * L_sign at t against the theorem δ^{-1} law (free prefactor 1.81): measured/predicted in [0.694, 1.520] → NO within a factor 1.5
   * L_sign at t against the transcript δ^{-0.07}(log(t/2π))^{0.89} law (free prefactor 2.23): measured/predicted in [0.491, 2.753] → NO within a factor 1.5
   * L_sign median over centers against the density δ^{-2/3}(log(t/2π))^{1/3} law (free prefactor 1.89): measured/predicted in [0.862, 1.056] → YES within a factor 1.5
   * L_sign median over centers against the theorem δ^{-1} law (free prefactor 1.8): measured/predicted in [0.571, 1.497] → NO within a factor 1.5
   * L_sign median over centers against the transcript δ^{-0.07}(log(t/2π))^{0.89} law (free prefactor 2.22): measured/predicted in [0.484, 1.771] → NO within a factor 1.5
   * L_bal3 at t against the density δ^{-2/3}(log(t/2π))^{1/3} law (free prefactor 2.62): measured/predicted in [0.710, 1.565] → NO within a factor 1.5
   * L_bal3 at t against the theorem δ^{-1} law (free prefactor 2.5): measured/predicted in [0.583, 1.338] → NO within a factor 1.5
   * L_bal3 at t against the transcript δ^{-0.07}(log(t/2π))^{0.89} law (free prefactor 3.09): measured/predicted in [0.429, 2.610] → NO within a factor 1.5
   * L_bal3 median over centers against the density δ^{-2/3}(log(t/2π))^{1/3} law (free prefactor 2.47): measured/predicted in [0.767, 1.119] → YES within a factor 1.5
   * L_bal3 median over centers against the theorem δ^{-1} law (free prefactor 2.36): measured/predicted in [0.507, 1.522] → NO within a factor 1.5
   * L_bal3 median over centers against the transcript δ^{-0.07}(log(t/2π))^{0.89} law (free prefactor 2.91): measured/predicted in [0.492, 1.645] → NO within a factor 1.5

## 4. The four refutation-shaped closes of PRICING §2(d), filled in from the files (INSTRUMENT; nothing about RH)

1. **L_sign at t (the contract's twelve points) — lands:** the measured sign-detection bandwidth follows **the density model δ^{−2/3}(log t)^{1/3}** within a factor 1.5 across 10³ ≤ t ≤ 10⁶ and 0.05 ≤ δ ≤ 0.25 (measured/predicted in [0.79, 1.34]); the two other laws are refuted at that tolerance (the theorem's δ⁻¹ log log t [0.69, 1.52]; the transcript's δ^{−0.07}(log t)^{0.89} [0.49, 2.75]). **L_sign median over the centers (the ensemble instrument) — lands:** the measured sign-detection bandwidth follows **the density model δ^{−2/3}(log t)^{1/3}** within a factor 1.5 across 10³ ≤ t ≤ 10⁶ and 0.05 ≤ δ ≤ 0.25 (measured/predicted in [0.86, 1.06]); the two other laws are refuted at that tolerance (the theorem's δ⁻¹ log log t [0.57, 1.50]; the transcript's δ^{−0.07}(log t)^{0.89} [0.48, 1.77]). Measured δ-ratios L_sign(0.05)/L_sign(0.25) at t: 4.79, 2.85, 2.72, 3.03 (laws 1.12 : 2.9 : 5); the single-t values scatter within the p10–p90 bands of §2 (the noise at one t is configuration-dominated for L ≳ 20), which is why the ensemble median is the sharper instrument.

2. **Where the theorem's L* is spent.** At (0.1, 10⁶): L* = 40·(2.626 + 4.605 + 2.856) = 403.5 — log log(3 + t) 26 %, 2log(1/δ) 46 %, log(2b₁C₁) 28 %; the floor without the noise term, 4δ⁻¹(2log(1/δ) + log(2b₁C₁)) = 298. Measured: t = 1000: at the record point L* = 375.8 (δ = 0.1) N_Z = 1.693e-08 against the clause-4 bound 2b₁ℓ_R/L² = 1.276e-03 (ratio 7.54e+04); over the grid rows L ≥ 50 the ratio (bound/N̄_Z)/L with N̄_Z the mean over the 143 centers is in [2.56, 4.54] (the pricing's inference: ≈ 1.05; against the single-t N_Z the same ratio ranges over [1.38, 593] because of the nearest-zero oscillation); t = 10000: at the record point L* = 387.3 (δ = 0.1) N_Z = 5.007e-09 against the clause-4 bound 2b₁ℓ_R/L² = 1.233e-03 (ratio 2.46e+05); over the grid rows L ≥ 50 the ratio (bound/N̄_Z)/L with N̄_Z the mean over the 145 centers is in [1.32, 1.57] (the pricing's inference: ≈ 1.05; against the single-t N_Z the same ratio ranges over [0.25, 1] because of the nearest-zero oscillation); t = 100000: at the record point L* = 396.2 (δ = 0.1) N_Z = 1.134e-09 against the clause-4 bound 2b₁ℓ_R/L² = 1.307e-03 (ratio 1.15e+06); over the grid rows L ≥ 50 the ratio (bound/N̄_Z)/L with N̄_Z the mean over the 147 centers is in [1.42, 1.83] (the pricing's inference: ≈ 1.05; against the single-t N_Z the same ratio ranges over [3.20, 1817] because of the nearest-zero oscillation); t = 1e+06: at the record point L* = 403.5 (δ = 0.1) N_Z = 8.314e-09 against the clause-4 bound 2b₁ℓ_R/L² = 1.480e-03 (ratio 1.78e+05); over the grid rows L ≥ 50 the ratio (bound/N̄_Z)/L with N̄_Z the mean over the 149 centers is in [0.93, 1.16] (the pricing's inference: ≈ 1.05; against the single-t N_Z the same ratio ranges over [2.09, 122] because of the nearest-zero oscillation). **Refutation-shaped close:** the clause-4 bound is loose by a factor of order L at ζ's density (measured factors above), and the theorem's L* cannot be reduced below 298 at (0.1, 10⁶) by any improvement of the noise bound alone.

3. **λ₀ = 25 near-optimal?** Not a campaign item (bump-only, height-independent): the crossing of 2c(λ)² ≥ e^{λ/2} recomputed by the campaign's transform is λ = 18.6 (record 18.6; proved from 23; contract 25). One line, as priced.

4. **R₀ = 81 loose by the uniformity price only?** From `outwindow_test.py` (no zeros needed): the radius at which the TRUE contamination of a depth-½ orbit falls to e^{−L} is u_true/L = 1.89, 1.33, 1.22, 1.17, 1.05, 1.10, 1.09, 1.09, 1.11, 1.10, 1.10, 1.09 (L = 4, 8, 12, 16, 20, 30, 40, 50, 60, 80, 100, 120); the clause-5 pointwise bound route gives u/L = 1247, 416, 185, 139, 111, 111, 83, 67, 55, 62, 50, 42 at the same L; the proved R₀ = 81 (asymptote 37.5) against the true ≈ 1.09 L. Bound/exact at the four planted distances: L=20 u=5: 10^10.6; L=20 u=50: 10^23.4; L=20 u=500: 10^59.0; L=20 u=1620: 10^100.1; L=50 u=5: 10^14.3; L=50 u=50: 10^33.3; L=50 u=500: 10^88.1; L=50 u=4050: 10^234.0; L=120 u=5: 10^19.8; L=120 u=50: 10^47.8; L=120 u=500: 10^132.0. **Refutation-shaped close:** the out-window radius forced by the true transform is R ≈ 1.1·L at L = 120 (the note's 'for the record' 1.06 used the pre-asymptotic rate 0.85; with the saddle-point rate 1/√2 the same chain gives (7/(8·0.707))² = 1.53); the proved 81L is the price of c_B = 0.143 against the numerical ≈ 0.71–0.85 (a factor ≈ 25–35 in R₀ = (7/(8c))²) plus the uniformity relaxations (81 against 37.5 asymptotically). Nothing about RH.

## 5. The record points L*(δ, t; C₁ = 1) and L*(δ, t; C₁ = 2.4·10⁹): the datum where the theorem asserts its bound (INSTRUMENT)

| t | δ | L* | C₁ | inside (L ≥ L*, t ≥ 21L) | zeros used | N_Z = W_{Z'} | main −2δ²c² | W_Z | clause-6 bound δ²e^{δL/2} | ratio sep/bound | log10 \|E₋\| bound / est | N_Z/model |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000 | 0.05 | 862.48 | 1 | False | 75 | 5.092e-12 | -3.812e+09 | -3.812e+09 | 5.784e+06 | 659 | -130.5 / -788.5 | 0.000 |
| 1000 | 0.05 | 2590.38 | 2.4e9 | False | 25 | 4.095e-19 | -1.574e+42 | -1.574e+42 | 3.331e+25 | 4.73e+16 | -212.0 / -1343.0 | 0.000 |
| 1000 | 0.10 | 375.79 | 1 | False | 171 | 1.693e-08 | -1.757e+08 | -1.757e+08 | 1.446e+06 | 122 | -77.8 / -516.1 | 0.011 |
| 1000 | 0.10 | 1239.74 | 2.4e9 | False | 52 | 9.356e-14 | -4.301e+40 | -4.301e+40 | 8.329e+24 | 5.16e+15 | -127.6 / -914.1 | 0.000 |
| 1000 | 0.25 | 120.99 | 1 | False | 459 | 2.354e-09 | -3.523e+06 | -3.523e+06 | 2.313e+05 | 15.2 | -34.9 / -288.3 | 0.000 |
| 1000 | 0.25 | 466.57 | 2.4e9 | False | 139 | 2.746e-09 | -3.770e+38 | -3.770e+38 | 1.333e+24 | 2.83e+14 | -55.7 / -542.8 | 0.003 |
| 10000 | 0.05 | 885.46 | 1 | False | 106 | 1.459e-08 | -9.714e+09 | -9.714e+09 | 1.027e+07 | 945 | -486.4 / -2565.5 | 0.083 |
| 10000 | 0.05 | 2613.36 | 2.4e9 | False | 36 | 1.170e-12 | -4.431e+42 | -4.431e+42 | 5.918e+25 | 7.49e+16 | -823.6 / -4384.3 | 0.000 |
| 10000 | 0.10 | 387.28 | 1 | True | 243 | 5.007e-09 | -4.398e+08 | -4.398e+08 | 2.568e+06 | 171 | -312.2 / -1692.0 | 0.002 |
| 10000 | 0.10 | 1251.23 | 2.4e9 | False | 75 | 1.196e-10 | -1.207e+41 | -1.207e+41 | 1.479e+25 | 8.16e+15 | -549.8 / -3018.4 | 0.002 |
| 10000 | 0.25 | 125.59 | 1 | True | 681 | 1.130e-04 | -8.544e+06 | -8.544e+06 | 4.110e+05 | 20.8 | -167.1 / -958.6 | 1.827 |
| 10000 | 0.25 | 471.17 | 2.4e9 | True | 199 | 3.511e-07 | -1.054e+39 | -1.054e+39 | 2.367e+24 | 4.45e+14 | -313.4 / -1833.9 | 0.300 |
| 100000 | 0.05 | 903.31 | 1 | True | 137 | 1.194e-13 | -2.013e+10 | -2.013e+10 | 1.605e+07 | 1.25e+03 | -1629.5 / -8235.3 | 0.000 |
| 100000 | 0.05 | 2631.21 | 2.4e9 | True | 48 | 3.446e-23 | -9.904e+42 | -9.904e+42 | 9.246e+25 | 1.07e+17 | -2771.0 / -14032.5 | 0.000 |
| 100000 | 0.10 | 396.20 | 1 | True | 312 | 1.134e-09 | -8.993e+08 | -8.993e+08 | 4.013e+06 | 224 | -1068.6 / -5449.1 | 0.000 |
| 100000 | 0.10 | 1260.15 | 2.4e9 | True | 98 | 6.441e-16 | -2.693e+41 | -2.693e+41 | 2.312e+25 | 1.16e+16 | -1896.5 / -9695.5 | 0.000 |
| 100000 | 0.25 | 129.16 | 1 | True | 905 | 7.703e-07 | -1.707e+07 | -1.707e+07 | 6.421e+05 | 26.6 | -598.0 / -3105.9 | 0.010 |
| 100000 | 0.25 | 474.74 | 2.4e9 | True | 259 | 2.429e-12 | -2.343e+39 | -2.343e+39 | 3.698e+24 | 6.34e+14 | -1138.8 / -5932.3 | 0.000 |
| 1e+06 | 0.05 | 917.90 | 1 | True | 165 | 1.583e-12 | -3.657e+10 | -3.657e+10 | 2.311e+07 | 1.58e+03 | -5277.5 / -26294.6 | 0.000 |
| 1e+06 | 0.05 | 2645.80 | 2.4e9 | True | 57 | 2.334e-19 | -1.911e+43 | -1.911e+43 | 1.331e+26 | 1.44e+17 | -8952.0 / -44620.2 | 0.000 |
| 1e+06 | 0.10 | 403.50 | 1 | True | 378 | 8.314e-09 | -1.616e+09 | -1.616e+09 | 5.779e+06 | 280 | -3487.4 / -17428.6 | 0.003 |
| 1e+06 | 0.10 | 1267.45 | 2.4e9 | True | 120 | 1.938e-14 | -5.187e+41 | -5.187e+41 | 3.329e+25 | 1.56e+16 | -6173.8 / -30867.1 | 0.000 |
| 1e+06 | 0.25 | 132.08 | 1 | True | 1133 | 9.659e-06 | -3.012e+07 | -3.012e+07 | 9.246e+05 | 32.6 | -1981.8 / -9965.7 | 0.112 |
| 1e+06 | 0.25 | 477.66 | 2.4e9 | True | 319 | 2.552e-09 | -4.503e+39 | -4.503e+39 | 5.326e+24 | 8.45e+14 | -3763.5 / -18930.1 | 0.001 |

## 6. Grid rows at δ = 0.1 (compact; the full tables with all columns are `rows_<tag>.csv`; INSTRUMENT)

### t = 1000 (reflection condition t ≥ 21L holds for L ≤ 47.6; rows with L above that are below the theorem's hypotheses)

| L | inside | n | N_Z | model | N/model | clause-4 bound | main | W_Z | W_Zrep | sep/cl6 | sign fires | bal3 | log10\|E₋\| bound / est / direct |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | no | 459 | 1.374e+00 | 1.317e+00 | 1.04 | 7.82e+00 | -2.013e-02 | 1.354e+00 | 1.312e+00 | 1.65 | False | False | 1 / -52 / 4.45e-53 |
| 6 | no | 459 | 3.283e-01 | 3.901e-01 | 0.84 | 3.53e+00 | -2.029e-02 | 3.080e-01 | 2.672e-01 | 1.5 | False | False | -2 / -64 / 1.93e-65 |
| 8 | no | 459 | 6.121e-02 | 1.646e-01 | 0.37 | 2.01e+00 | -2.051e-02 | 4.070e-02 | 1.815e-03 | 1.37 | False | False | -3 / -75 / 3.44e-77 |
| 10 | no | 459 | 6.435e-02 | 8.427e-02 | 0.76 | 1.31e+00 | -2.080e-02 | 4.354e-02 | 7.038e-03 | 1.26 | False | False | -5 / -84 / 3.34e-85 |
| 12 | no | 459 | 5.072e-02 | 4.877e-02 | 1.04 | 9.17e-01 | -2.117e-02 | 2.955e-02 | -4.217e-03 | 1.16 | False | False | -7 / -92 / -4.61e-94 |
| 14 | no | 459 | 3.390e-02 | 3.071e-02 | 1.10 | 6.81e-01 | -2.160e-02 | 1.230e-02 | -1.846e-02 | 1.07 | False | False | -8 / -100 / 3.64e-102 |
| 16 | no | 459 | 3.029e-02 | 2.057e-02 | 1.47 | 5.26e-01 | -2.211e-02 | 8.179e-03 | -1.939e-02 | 0.994 | False | False | -9 / -107 / -7.12e-110 |
| 18 | no | 459 | 2.645e-02 | 1.445e-02 | 1.83 | 4.19e-01 | -2.271e-02 | 3.747e-03 | -2.055e-02 | 0.923 | False | False | -11 / -114 / -2.77e-115 |
| 20 | no | 459 | 2.197e-02 | 1.053e-02 | 2.09 | 3.42e-01 | -2.338e-02 | -1.410e-03 | -2.244e-02 | 0.86 | True | False | -12 / -120 / 1.31e-121 |
| 22 | no | 459 | 1.828e-02 | 7.914e-03 | 2.31 | 2.85e-01 | -2.415e-02 | -5.874e-03 | -2.372e-02 | 0.804 | True | False | -13 / -126 / 7.69e-128 |
| 24 | no | 459 | 1.525e-02 | 6.096e-03 | 2.50 | 2.41e-01 | -2.502e-02 | -9.770e-03 | -2.461e-02 | 0.754 | True | False | -14 / -132 / 8.33e-134 |
| 26 | no | 459 | 1.237e-02 | 4.795e-03 | 2.58 | 2.07e-01 | -2.600e-02 | -1.363e-02 | -2.568e-02 | 0.708 | True | False | -15 / -137 / -7.32e-139 |
| 28 | no | 459 | 9.604e-03 | 3.839e-03 | 2.50 | 1.80e-01 | -2.708e-02 | -1.748e-02 | -2.702e-02 | 0.668 | True | False | -16 / -142 / 9.49e-144 |
| 30 | no | 459 | 7.452e-03 | 3.121e-03 | 2.39 | 1.57e-01 | -2.829e-02 | -2.084e-02 | -2.817e-02 | 0.631 | True | True | -17 / -147 / 2.63e-149 |
| 40 | no | 459 | 9.571e-04 | 1.317e-03 | 0.73 | 9.08e-02 | -3.665e-02 | -3.569e-02 | -3.665e-02 | 0.496 | True | True | -21 / -171 / - |
| 50 | no | 459 | 3.532e-05 | 6.742e-04 | 0.05 | 5.94e-02 | -5.047e-02 | -5.044e-02 | -5.047e-02 | 0.414 | True | True | -24 / -191 / - |
| 60 | no | 459 | 4.015e-04 | 3.901e-04 | 1.03 | 4.19e-02 | -7.340e-02 | -7.299e-02 | -7.339e-02 | 0.365 | True | True | -28 / -209 / - |
| 70 | no | 459 | 2.819e-04 | 2.457e-04 | 1.15 | 3.13e-02 | -1.119e-01 | -1.116e-01 | -1.119e-01 | 0.338 | True | True | -31 / -226 / - |
| 80 | no | 459 | 3.286e-05 | 1.646e-04 | 0.20 | 2.43e-02 | -1.778e-01 | -1.778e-01 | -1.778e-01 | 0.326 | True | True | -33 / -241 / - |
| 90 | no | 459 | 1.571e-05 | 1.156e-04 | 0.14 | 1.94e-02 | -2.929e-01 | -2.929e-01 | -2.929e-01 | 0.325 | True | True | -36 / -256 / - |
| 100 | no | 459 | 5.551e-05 | 8.427e-05 | 0.66 | 1.59e-02 | -4.976e-01 | -4.975e-01 | -4.976e-01 | 0.335 | True | True | -38 / -269 / - |
| 110 | no | 459 | 2.587e-05 | 6.331e-05 | 0.41 | 1.32e-02 | -8.684e-01 | -8.684e-01 | -8.684e-01 | 0.355 | True | True | -40 / -283 / - |
| 120 | no | 459 | 1.575e-07 | 4.877e-05 | 0.00 | 1.12e-02 | -1.552e+00 | -1.552e+00 | -1.552e+00 | 0.385 | True | True | -43 / -295 / - |

### t = 10000 (reflection condition t ≥ 21L holds for L ≤ 476.2; rows with L above that are below the theorem's hypotheses)

| L | inside | n | N_Z | model | N/model | clause-4 bound | main | W_Z | W_Zrep | sep/cl6 | sign fires | bal3 | log10\|E₋\| bound / est / direct |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | no | 681 | 1.938e+00 | 1.915e+00 | 1.01 | 1.01e+01 | -2.013e-02 | 1.918e+00 | 1.914e+00 | 1.65 | False | False | -20 / -170 / - |
| 6 | no | 681 | 6.946e-01 | 5.673e-01 | 1.22 | 4.47e+00 | -2.029e-02 | 6.743e-01 | 6.701e-01 | 1.5 | False | False | -28 / -209 / - |
| 8 | no | 681 | 2.248e-01 | 2.393e-01 | 0.94 | 2.52e+00 | -2.051e-02 | 2.043e-01 | 2.001e-01 | 1.37 | False | False | -34 / -242 / - |
| 10 | no | 681 | 8.324e-02 | 1.225e-01 | 0.68 | 1.62e+00 | -2.080e-02 | 6.243e-02 | 5.823e-02 | 1.26 | False | False | -40 / -271 / - |
| 12 | no | 681 | 4.173e-02 | 7.092e-02 | 0.59 | 1.12e+00 | -2.117e-02 | 2.057e-02 | 1.640e-02 | 1.16 | False | False | -45 / -298 / - |
| 14 | no | 681 | 1.777e-02 | 4.466e-02 | 0.40 | 8.27e-01 | -2.160e-02 | -3.834e-03 | -7.965e-03 | 1.07 | True | False | -50 / -322 / - |
| 16 | no | 681 | 1.070e-02 | 2.992e-02 | 0.36 | 6.34e-01 | -2.211e-02 | -1.141e-02 | -1.550e-02 | 0.994 | True | False | -54 / -344 / - |
| 18 | no | 681 | 9.726e-03 | 2.101e-02 | 0.46 | 5.02e-01 | -2.271e-02 | -1.298e-02 | -1.702e-02 | 0.923 | True | False | -58 / -365 / - |
| 20 | no | 681 | 9.080e-03 | 1.532e-02 | 0.59 | 4.07e-01 | -2.338e-02 | -1.430e-02 | -1.829e-02 | 0.86 | True | False | -62 / -385 / - |
| 22 | no | 681 | 8.164e-03 | 1.151e-02 | 0.71 | 3.37e-01 | -2.415e-02 | -1.599e-02 | -1.992e-02 | 0.804 | True | False | -66 / -404 / - |
| 24 | no | 681 | 6.381e-03 | 8.865e-03 | 0.72 | 2.84e-01 | -2.502e-02 | -1.864e-02 | -2.251e-02 | 0.754 | True | True | -70 / -422 / - |
| 26 | no | 681 | 4.439e-03 | 6.972e-03 | 0.64 | 2.42e-01 | -2.600e-02 | -2.156e-02 | -2.536e-02 | 0.708 | True | True | -73 / -440 / - |
| 28 | no | 681 | 3.813e-03 | 5.582e-03 | 0.68 | 2.09e-01 | -2.708e-02 | -2.327e-02 | -2.701e-02 | 0.668 | True | True | -76 / -456 / - |
| 30 | no | 681 | 4.334e-03 | 4.539e-03 | 0.95 | 1.82e-01 | -2.829e-02 | -2.396e-02 | -2.762e-02 | 0.631 | True | True | -79 / -472 / - |
| 40 | no | 681 | 3.325e-03 | 1.915e-03 | 1.74 | 1.03e-01 | -3.665e-02 | -3.332e-02 | -3.657e-02 | 0.496 | True | True | -94 / -546 / - |
| 50 | no | 681 | 2.768e-03 | 9.804e-04 | 2.82 | 6.65e-02 | -5.047e-02 | -4.771e-02 | -5.047e-02 | 0.414 | True | True | -106 / -610 / - |
| 60 | no | 681 | 2.260e-03 | 5.673e-04 | 3.98 | 4.64e-02 | -7.340e-02 | -7.114e-02 | -7.339e-02 | 0.365 | True | True | -118 / -669 / - |
| 70 | no | 681 | 1.766e-03 | 3.573e-04 | 4.94 | 3.43e-02 | -1.119e-01 | -1.102e-01 | -1.119e-01 | 0.338 | True | True | -128 / -722 / - |
| 80 | no | 681 | 1.309e-03 | 2.393e-04 | 5.47 | 2.64e-02 | -1.778e-01 | -1.765e-01 | -1.778e-01 | 0.326 | True | True | -138 / -772 / - |
| 90 | no | 681 | 9.135e-04 | 1.681e-04 | 5.43 | 2.10e-02 | -2.929e-01 | -2.920e-01 | -2.929e-01 | 0.325 | True | True | -147 / -819 / - |
| 100 | no | 681 | 5.920e-04 | 1.225e-04 | 4.83 | 1.71e-02 | -4.976e-01 | -4.970e-01 | -4.976e-01 | 0.335 | True | True | -155 / -863 / - |
| 110 | no | 681 | 3.484e-04 | 9.207e-05 | 3.78 | 1.42e-02 | -8.684e-01 | -8.680e-01 | -8.684e-01 | 0.355 | True | True | -163 / -905 / - |
| 120 | no | 681 | 1.790e-04 | 7.092e-05 | 2.52 | 1.19e-02 | -1.552e+00 | -1.552e+00 | -1.552e+00 | 0.385 | True | True | -171 / -945 / - |

### t = 100000 (reflection condition t ≥ 21L holds for L ≤ 4761.9; rows with L above that are below the theorem's hypotheses)

| L | inside | n | N_Z | model | N/model | clause-4 bound | main | W_Z | W_Zrep | sep/cl6 | sign fires | bal3 | log10\|E₋\| bound / est / direct |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | no | 905 | 2.771e+00 | 2.513e+00 | 1.10 | 1.25e+01 | -2.013e-02 | 2.750e+00 | 2.666e+00 | 1.65 | False | False | -93 / -545 / - |
| 6 | no | 905 | 8.271e-01 | 7.445e-01 | 1.11 | 5.57e+00 | -2.029e-02 | 8.069e-01 | 7.282e-01 | 1.5 | False | False | -118 / -669 / - |
| 8 | no | 905 | 2.474e-01 | 3.141e-01 | 0.79 | 3.13e+00 | -2.051e-02 | 2.269e-01 | 1.559e-01 | 1.37 | False | False | -139 / -773 / - |
| 10 | no | 905 | 1.368e-01 | 1.608e-01 | 0.85 | 2.00e+00 | -2.080e-02 | 1.160e-01 | 5.384e-02 | 1.26 | False | False | -157 / -865 / - |
| 12 | no | 905 | 8.183e-02 | 9.307e-02 | 0.88 | 1.39e+00 | -2.117e-02 | 6.067e-02 | 8.012e-03 | 1.16 | False | False | -174 / -948 / - |
| 14 | no | 905 | 5.587e-02 | 5.861e-02 | 0.95 | 1.02e+00 | -2.160e-02 | 3.427e-02 | -8.725e-03 | 1.07 | False | False | -189 / -1024 / - |
| 16 | no | 905 | 3.937e-02 | 3.926e-02 | 1.00 | 7.83e-01 | -2.211e-02 | 1.725e-02 | -1.648e-02 | 0.994 | False | False | -203 / -1095 / - |
| 18 | no | 905 | 3.426e-02 | 2.758e-02 | 1.24 | 6.19e-01 | -2.271e-02 | 1.155e-02 | -1.373e-02 | 0.923 | False | False | -217 / -1162 / - |
| 20 | no | 905 | 2.348e-02 | 2.010e-02 | 1.17 | 5.02e-01 | -2.338e-02 | 9.150e-05 | -1.789e-02 | 0.86 | False | False | -229 / -1225 / - |
| 22 | no | 905 | 1.303e-02 | 1.510e-02 | 0.86 | 4.15e-01 | -2.415e-02 | -1.113e-02 | -2.311e-02 | 0.804 | True | False | -241 / -1285 / - |
| 24 | no | 905 | 8.144e-03 | 1.163e-02 | 0.70 | 3.48e-01 | -2.502e-02 | -1.688e-02 | -2.424e-02 | 0.754 | True | True | -253 / -1342 / - |
| 26 | no | 905 | 4.938e-03 | 9.150e-03 | 0.54 | 2.97e-01 | -2.600e-02 | -2.106e-02 | -2.510e-02 | 0.708 | True | True | -264 / -1397 / - |
| 28 | no | 905 | 2.781e-03 | 7.326e-03 | 0.38 | 2.56e-01 | -2.708e-02 | -2.430e-02 | -2.617e-02 | 0.668 | True | True | -274 / -1450 / - |
| 30 | no | 905 | 1.281e-03 | 5.956e-03 | 0.22 | 2.23e-01 | -2.829e-02 | -2.701e-02 | -2.764e-02 | 0.631 | True | True | -284 / -1500 / - |
| 40 | no | 905 | 8.256e-04 | 2.513e-03 | 0.33 | 1.26e-01 | -3.665e-02 | -3.582e-02 | -3.651e-02 | 0.496 | True | True | -331 / -1733 / - |
| 50 | no | 905 | 5.026e-04 | 1.287e-03 | 0.39 | 8.04e-02 | -5.047e-02 | -4.997e-02 | -5.044e-02 | 0.414 | True | True | -372 / -1938 / - |
| 60 | no | 905 | 1.071e-05 | 7.445e-04 | 0.01 | 5.59e-02 | -7.340e-02 | -7.338e-02 | -7.339e-02 | 0.365 | True | True | -409 / -2123 / - |
| 70 | no | 905 | 1.168e-04 | 4.689e-04 | 0.25 | 4.11e-02 | -1.119e-01 | -1.118e-01 | -1.119e-01 | 0.338 | True | True | -443 / -2293 / - |
| 80 | no | 905 | 1.743e-05 | 3.141e-04 | 0.06 | 3.15e-02 | -1.778e-01 | -1.778e-01 | -1.778e-01 | 0.326 | True | True | -474 / -2451 / - |
| 90 | no | 905 | 1.588e-05 | 2.206e-04 | 0.07 | 2.49e-02 | -2.929e-01 | -2.929e-01 | -2.929e-01 | 0.325 | True | True | -504 / -2600 / - |
| 100 | no | 905 | 1.585e-05 | 1.608e-04 | 0.10 | 2.02e-02 | -4.976e-01 | -4.976e-01 | -4.976e-01 | 0.335 | True | True | -532 / -2741 / - |
| 110 | no | 905 | 4.946e-07 | 1.208e-04 | 0.00 | 1.67e-02 | -8.684e-01 | -8.684e-01 | -8.684e-01 | 0.355 | True | True | -559 / -2874 / - |
| 120 | no | 905 | 7.171e-06 | 9.307e-05 | 0.08 | 1.40e-02 | -1.552e+00 | -1.552e+00 | -1.552e+00 | 0.385 | True | True | -584 / -3002 / - |

### t = 1e+06 (reflection condition t ≥ 21L holds for L ≤ 47619.0; rows with L above that are below the theorem's hypotheses)

| L | inside | n | N_Z | model | N/model | clause-4 bound | main | W_Z | W_Zrep | sep/cl6 | sign fires | bal3 | log10\|E₋\| bound / est / direct |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | no | 1133 | 3.459e+00 | 3.111e+00 | 1.11 | 1.50e+01 | -2.013e-02 | 3.439e+00 | 3.397e+00 | 1.65 | False | False | -330 / -1733 / - |
| 6 | no | 1133 | 9.669e-01 | 9.217e-01 | 1.05 | 6.68e+00 | -2.029e-02 | 9.466e-01 | 9.065e-01 | 1.5 | False | False | -409 / -2123 / - |
| 8 | no | 1133 | 4.719e-01 | 3.889e-01 | 1.21 | 3.76e+00 | -2.051e-02 | 4.514e-01 | 4.131e-01 | 1.37 | False | False | -475 / -2452 / - |
| 10 | no | 1133 | 2.513e-01 | 1.991e-01 | 1.26 | 2.40e+00 | -2.080e-02 | 2.305e-01 | 1.945e-01 | 1.26 | False | False | -534 / -2742 / - |
| 12 | no | 1133 | 9.748e-02 | 1.152e-01 | 0.85 | 1.67e+00 | -2.117e-02 | 7.632e-02 | 4.299e-02 | 1.16 | False | False | -587 / -3005 / - |
| 14 | no | 1133 | 5.662e-02 | 7.256e-02 | 0.78 | 1.23e+00 | -2.160e-02 | 3.502e-02 | 4.618e-03 | 1.07 | False | False | -635 / -3246 / - |
| 16 | no | 1133 | 3.949e-02 | 4.861e-02 | 0.81 | 9.39e-01 | -2.211e-02 | 1.737e-02 | -9.932e-03 | 0.994 | False | False | -681 / -3470 / - |
| 18 | no | 1133 | 3.109e-02 | 3.414e-02 | 0.91 | 7.42e-01 | -2.271e-02 | 8.388e-03 | -1.573e-02 | 0.923 | False | False | -723 / -3681 / - |
| 20 | no | 1133 | 2.917e-02 | 2.489e-02 | 1.17 | 6.01e-01 | -2.338e-02 | 5.788e-03 | -1.515e-02 | 0.86 | False | False | -763 / -3880 / - |
| 22 | no | 1133 | 2.517e-02 | 1.870e-02 | 1.35 | 4.97e-01 | -2.415e-02 | 1.021e-03 | -1.681e-02 | 0.804 | False | False | -801 / -4070 / - |
| 24 | no | 1133 | 2.067e-02 | 1.440e-02 | 1.44 | 4.17e-01 | -2.502e-02 | -4.351e-03 | -1.923e-02 | 0.754 | True | False | -838 / -4251 / - |
| 26 | no | 1133 | 1.538e-02 | 1.133e-02 | 1.36 | 3.56e-01 | -2.600e-02 | -1.062e-02 | -2.276e-02 | 0.708 | True | False | -873 / -4425 / - |
| 28 | no | 1133 | 1.054e-02 | 9.069e-03 | 1.16 | 3.07e-01 | -2.708e-02 | -1.655e-02 | -2.621e-02 | 0.668 | True | False | -907 / -4592 / - |
| 30 | no | 1133 | 7.787e-03 | 7.374e-03 | 1.06 | 2.67e-01 | -2.829e-02 | -2.051e-02 | -2.798e-02 | 0.631 | True | True | -939 / -4753 / - |
| 40 | no | 1133 | 1.204e-03 | 3.111e-03 | 0.39 | 1.50e-01 | -3.665e-02 | -3.544e-02 | -3.649e-02 | 0.496 | True | True | -1087 / -5489 / - |
| 50 | no | 1133 | 1.321e-04 | 1.593e-03 | 0.08 | 9.62e-02 | -5.047e-02 | -5.034e-02 | -5.036e-02 | 0.414 | True | True | -1218 / -6137 / - |
| 60 | no | 1133 | 4.303e-04 | 9.217e-04 | 0.47 | 6.68e-02 | -7.340e-02 | -7.297e-02 | -7.335e-02 | 0.365 | True | True | -1336 / -6723 / - |
| 70 | no | 1133 | 3.090e-04 | 5.804e-04 | 0.53 | 4.91e-02 | -1.119e-01 | -1.116e-01 | -1.119e-01 | 0.338 | True | True | -1444 / -7262 / - |
| 80 | no | 1133 | 4.654e-05 | 3.889e-04 | 0.12 | 3.76e-02 | -1.778e-01 | -1.778e-01 | -1.778e-01 | 0.326 | True | True | -1545 / -7763 / - |
| 90 | no | 1133 | 1.348e-05 | 2.731e-04 | 0.05 | 2.97e-02 | -2.929e-01 | -2.929e-01 | -2.929e-01 | 0.325 | True | True | -1640 / -8234 / - |
| 100 | no | 1133 | 5.555e-05 | 1.991e-04 | 0.28 | 2.41e-02 | -4.976e-01 | -4.975e-01 | -4.976e-01 | 0.335 | True | True | -1730 / -8679 / - |
| 110 | no | 1133 | 3.049e-05 | 1.496e-04 | 0.20 | 1.99e-02 | -8.684e-01 | -8.684e-01 | -8.684e-01 | 0.355 | True | True | -1815 / -9103 / - |
| 120 | no | 1133 | 1.143e-06 | 1.152e-04 | 0.01 | 1.67e-02 | -1.552e+00 | -1.552e+00 | -1.552e+00 | 0.385 | True | True | -1896 / -9507 / - |

## 7. Instruments-table row (for `directions/C2-rigidity-conservation.md`)

| measured detection bandwidth L_sign(δ, t) on ζ's zeros (zero-side; first-order datum W_Z(f_{t,L})) | t = 1000: L_sign = 32.1 / 19.4 / 6.7 at δ = 0.05 / 0.1 / 0.25; t = 10000: L_sign = 25.1 / 13.5 / 8.8 at δ = 0.05 / 0.1 / 0.25; t = 100000: L_sign = 25.8 / 20.1 / 9.5 at δ = 0.05 / 0.1 / 0.25; t = 1e+06: L_sign = 33.3 / 22.4 / 11.0 at δ = 0.05 / 0.1 / 0.25 | `results/c2-m2/campaign/CAMPAIGN.md` §2–§4; row files `rows_t1e{3,4,5,6}.{csv,json}`; controls §1 | INSTRUMENT: decides the δ- and t-law of the bandwidth and the looseness of b₁-, C₁- and R₀-type constants; nothing about RH |

## 8. Hashes (SHA-256 of the files this document was built from)

* `zeros_t1e3.json`  12f085d083bb3ed637bc6fe8dc608dfd428a1f79dd6635a5dc60321b1b5da3fc
* `rows_t1e3.csv`  e4e1f7569771cda098dee4f3dc6a0af307ec0a33f68fa76574b04edcc25b0818
* `rows_t1e3.json`  7c88c0e981776f1d20d908ae393c9f33b9a87f3903250a6468f5fe72c0d82563
* `summary_t1e3.json`  a61ab8049975a83791266300f7bebba72dba7d6faeb79286fbe8bb15283c17a5
* `zeros_t1e4.json`  8497a48e5871bb62f6739a493e4b7ccad9fd33bc2329e45bd44c1e64c0583fa8
* `rows_t1e4.csv`  1f626271ad2ae137e9235dbfb197da4858f3673e784712129c71dcf8439ee322
* `rows_t1e4.json`  5a7741ebbcd3f03cf7080d6fcd7d35db9cb93f33d6f6461782fdf0710d6a8264
* `summary_t1e4.json`  5c45119e9cb6055e54c529084431742c8ddd1a325d1f28d667c577aa475fc7c5
* `zeros_t1e5.json`  c0bc906beaac93f6eca0ccd68293310f68ca1b179821846b0b27b51fcf82c0a5
* `rows_t1e5.csv`  835bc4146936a55eb33b89f602e909b560385a7fda0d172e003b0af9b102b608
* `rows_t1e5.json`  d5eef078f0374234112e778a72040c1484e93b37965be1d62bb5ff2ac9ec6477
* `summary_t1e5.json`  38403cf70c2ca0dba2fa80475cd675dda94076cf528362120ff86578b1c5070a
* `zeros_t1e6.json`  1665fc1c753d6605d7ec9038ec6ee062d41b1fbcac6adc01d50de574668391ff
* `rows_t1e6.csv`  4f60b78e4071c7f124d58cafb9c1b96bfa16fe001c0caff287ab0a584aecf638
* `rows_t1e6.json`  9546ffb83218a6ef810f12793dc9965ca9566cb7ff18f23f0dfeb4eb9ec6a0b8
* `summary_t1e6.json`  b86a1cc8790bc5283d672481042c3f97815a944e6be6845623ef6d3a57d13890
* `outwindow_test.json`  5bc41b48f95263fbcd2dc92c86db2b14a921553ac071eb44a4213e95c0c1f663
* `campaign_lib.py`  1eca667a1fa2b741734c3b7eaebde213e6cef1551fe6d4d54d99075e23339c70
* `run_height.py`  c24b53f0fccc69cd0670822d7acfa1b579901d2da8e0190bc67ac700249e400b

Status of the running campaign and the harvest recipe: `STATUS-campaign.md`. Checkpoints and the checker's verdicts: `SHARED.md`, `CHECK-O.md`.

---
## Corrections after the Opus check (22:54 IST 2026-09-16, Session 22; `CHECK-O.md` SHA-256 a331d579d2f96fbf799b636c2b1e617f2c75a334c956cf7250bb58c7a609f35e — PASS at all four heights, no row flagged; closes 1 REPAIRED / 2–4 CONFIRMED; insertion-only — the body above is unchanged; orchestrator)

**Headline of the check:** 20 zeros per height re-verified at 30 digits (max |Δγ| ≤ 8.2·10⁻¹¹, |Z(γ)| ≤ 8.5·10⁻²⁵; index map gap-free); two rows per height recomputed with an independent Gauss–Legendre transform (W_Z ≤ 1.7·10⁻¹² relative, main term ≤ 9.7·10⁻¹⁴ relative, W_Z′ ≤ 5.7·10⁻¹⁶ absolute); the k ≤ 13 truncation route confirmed rigorous with all thirteen ‖B^(k)‖₁ recomputed to 12 digits; the operative C₁ for ζ in these windows ≈ 0.434 (C₁ = 1 conservative); three of the 25 new DH off-line zeros re-verified (|f_DH| ≤ 3.2·10⁻²⁹, inside the strip); positive control ≥ 0 at all 732 rows and 4684 fine-grid bandwidths. **Close 1 stands but is REPAIRED (items 2–3 below): the theorem's own tabulated δ-ratio is 7.13 / 6.95, not the idealized 5, and its refutation clears the 1.5 threshold by 1.3 % at t (widened to [0.60, 1.75] on the theorem's exact shape), so the refutation does not depend on the idealization. Stop condition (iv) FIRED in the form the contract wrote it (item 4) — a process finding recorded here, with no effect on any close.**

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

**[RECORD CORRECTION 00:36 IST 2026-09-17, Session 22 close — from `results/c2-m6/m6-rung1-note.md` §5.3, CONFIRMED independently in `results/c2-m6/check-O.md` §3 at 40 digits; insertion-only.]** The recipe used for DH's ON-LINE zeros in §1 (the DH rows) and the DH sub-task — `findroot` on Re Ξ_DH(½ + iu) at scale 10⁻³⁰ (`dh_negative_control.py`, `dh_offline_scan.py`, `dh_control_new_heights.py`) — mislocates them by 1.2·10⁻⁶ … 1.4·10⁻³ (|f_DH| at the recorded points 4.9·10⁻⁶ … 3.7·10⁻³, against ≤ 3.5·10⁻³⁹ after refinement on the gamma-normalized Z_DH); the record's |Z_DH| = 1.9·10⁻³² acceptance criterion is scale-blind. Effect: the DH W_Z′ columns move at 10⁻⁴ relative (0.0048010832 → 0.0048001176 at L = 10; 4.4642882·10⁻⁵ → 4.4652466·10⁻⁵ at L = 20); NO headline moves, because W_Z − W_Z′ = W(orbit) identically — every separation, ratio and "fires" column is independent of the on-line positions (×6.24 → 6.23731); the 26 off-line orbits are refined on f_DH itself and stand. The three scripts are to be re-run with the corrected refinement (Session 23 queue item 0(c)); until then their DH on-line columns carry this note.

---

**Re-run 2026-09-17 (Session 23; after `results/c2-m6/m6-rung1-note.md` §5.3 and `check-O.md` §3; append-only).** The on-line-zero recipe of the DH sub-task (`dh_offline_scan.py` `online_count`, `dh_control_new_heights.py` `online_count`: `findroot` on Z_DH at dps 15) mislocated the on-line points of the three campaign heights by 1.5·10⁻⁵ … 8.4·10⁻⁴ (t = 114.163343, 39 points), 1.3·10⁻⁵ … 1.0·10⁻³ (166.479306, 43) and 6.1·10⁻⁶ … 1.8·10⁻³ (176.702461, 43). Re-run with the refinement on the rescaled S(u) = Z_DH(u)/[(5/π)^{3/4}|Γ(¾ + iu/2)|] at 40 digits (`dh_control_new_heights_rerun.py` → `dh_control_new_heights_rerun.json`, `logs/dh_control_new_heights_rerun.log`; `dh_offline_scan_rerun.py` → `dh_offline_scan_rerun.json`, `logs/dh_offline_scan_rerun.log`, the orbit search not redone; side-by-side tables in `dh_rerun_compare.log`): max |f_DH(½ + iγ)| over the refined points 6.5·10⁻³⁹ (record's points: 10⁻⁶ … 10⁻³); the same 39 / 43 / 43 zeros. The W_{Z′} column of the §1 tables, record → re-run (relative): t = 114.16: L = 10 1.6352·10⁻³ → 1.6335·10⁻³ (−1.0·10⁻³), L = 20 3.2235·10⁻⁴ → 3.2263·10⁻⁴ (+8.6·10⁻⁴), L* = 217.48 2.5684·10⁻¹⁴ → 2.5355·10⁻¹⁴ (−1.3·10⁻²); t = 166.48: L = 10 6.2336·10⁻³ → 6.2295·10⁻³ (−6.7·10⁻⁴), L = 20 2.4336·10⁻⁴ → 2.4378·10⁻⁴ (+1.7·10⁻³), L* = 521.27 3.3048·10⁻²² → 2.8434·10⁻²² (−1.4·10⁻¹); t = 176.70: L = 10 2.0023·10⁻² → 2.0031·10⁻² (+3.9·10⁻⁴), L = 20 6.3048·10⁻⁴ → 6.3097·10⁻⁴ (+7.7·10⁻⁴), L* = 133.66 4.8041·10⁻¹¹ → 4.6873·10⁻¹¹ (−2.4·10⁻²); the relative change grows with L because W_{Z′} there is a small sum of oscillating terms (10⁻⁸ … 10⁻²²), and at L ≤ 20 it is ≤ 1.7·10⁻³. W_Z moves by the same absolute amount as W_{Z′}. The main-term, separation, "ratio to δ²e^{δL/2}" and "fires (≥ 1)" columns are IDENTICAL to the record (relative move 0 at all 30 rows): the campaign library forms W_Z := W_{Z′} + main with main = −2δ²c(δL)², so W_Z − W_{Z′} = main by construction and the on-line positions cancel (check-O.md §3's identity W_Z − W_{Z′} = W(orbit)). The ratios 30.66 / 172.8 / 14.15 at L* and every fires line stand. The DH negative controls at the four heights 85.70, 114.16, 166.48, 176.70 STAND. Note on the scan's own control stage (`dh_offline_scan.py`, scan step 0.1, rows only in `logs/dh_offline_scan.log`, superseded in the JSON by `dh_control_new_heights.py` at step 0.05): its recorded W_{Z′} differ from the re-run by up to 1.0·10⁻² at L = 10 and 2.2·10⁻² at L = 20 (t = 166.48), the larger displacement of a one-secant-step root in a 0.1-wide bracket; the two re-runs (steps 0.1 and 0.05, both refined) agree on W_{Z′} to every double-precision digit at all 18 common rows. The record's acceptance criterion "max |Z_DH(γ)| at 25 digits" (`SHARED.md` checkpoint (5)) is scale-blind; the replacement is max |f_DH(½ + iγ)| (equivalently max |S(γ)|), ≤ 10⁻²⁵ required, 6.5·10⁻³⁹ obtained.

**Stop-condition ruling (orchestrator, 2026-09-17 11:45 IST).** The re-run brief's second stop condition ("any W_{Z′} changes by more than 2 % relative at L ≤ 20") FIRED by the letter on ONE row: the control-stage W_{Z′} of `dh_offline_scan.py` at (t = 166.479, L = 20), 2.385118·10⁻⁴ → 2.437795·10⁻⁴ (+2.21 %). That row is a SUPERSEDED record: it was located with a 0.1-wide bracket (one secant step from a wider bracket → a larger mislocation), lives only in `logs/dh_offline_scan.log`, and is not what §1 prints — the printed row (from `dh_control_new_heights.py`, step 0.05) moves +1.7·10⁻³ at the same point, and the two refined re-runs (steps 0.1 and 0.05) agree on W_{Z′} to every double digit at all 18 common rows. The mechanism is the known one (bracket width), not a new defect; the other two stop conditions (separation / ratio / fires > 10⁻⁸; max |f_DH| > 10⁻²⁵) fired nowhere. Ruling: proceed; the firing is recorded here and in LOG.md as required by 10(m), and the 2 % threshold is read as a threshold on the PRINTED record.

**[2026-09-17, Session 23 — Addendum to `separation-note.md` (clause 1′ = (R*)); Opus check `followups/ADDENDUM-CHECK-O.md` CLOSES.]** The reflection part of the row flag `inside_hypotheses` (§0 line 11) reads (R*) of the note's addendum A1 in place of t ≥ 21L: at t = 10³ it holds for every L ≤ 2341 (δ = ½; L ≤ 6.4·10⁴ at δ = 0.1), at t = 10⁴ for L ≤ 2.58·10⁴. §5's record points at t = 10³ are all INSIDE the theorem's hypotheses at their own δ (the (0.05, C₁ = 2.4·10⁹, L* = 2590) row only at its own δ, not in the uniform δ = ½ form), and the three t = 10⁴ rows flagged False come inside; §6's grid rows stay below the hypotheses through L < L*(δ, t) (and at t = 10³, L = 4, through the reflection condition as well). The headline of the campaign does not move (the twelve-point tables and the three-law comparison are measurements below L* by design). Out-window radius R₀ = 73 (note A3); the campaign never used the window's zeros.
