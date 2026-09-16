# STATUS-campaign.md — the zero-side numerics campaign for Theorem M2 (C2; contract `results/c2-m2/followups/PRICING.md` §2; operating rules `BRIEF.md`)

**Written 2026-09-16 21:17 IST by the builder (Fable 5.1, Session 22). Purpose: ANY later session can harvest without the builder.** INSTRUMENT (standing order 4): every table decides constants and the detection-bandwidth law; nothing about RH. Paths contain spaces — quote them. Do not commit by hand (the watchdogs commit every ten minutes and push every minute).

## 1. State (updated 2026-09-16 21:33 IST): ALL FOUR HEIGHTS DONE; CAMPAIGN.md at v1; the DH sub-task is the only process still running

| height | zeros (±U_data) | s/zero | controls | stop conditions | run time | finished |
|---|---|---|---|---|---|---|
| 10³ (rehearsal) | 459 (±285.6), indices 427..885 | 0.166 | positive PASS (min W_{Z′} = 4.1·10⁻¹⁹), negative PASS | (i) 0.329 s/zero no; (ii) no; (iv) center-mean N_Z/model ∈ [0.42, 1.08] no; (iii) pending checker | 118 s (+ 76 s zeros) | 21:15 IST |
| 10⁴ | 681 (±290.3), 9804..10484 | 0.600 | PASS / PASS (min W_{Z′} = 1.2·10⁻¹²) | (ii) no; (iv) [0.89, 1.16] no | 451 s | 21:23 |
| 10⁵ | 905 (±294.1), 137617..138521 | 0.422 | PASS / PASS (3.4·10⁻²³) | (ii) no; (iv) [0.69, 1.04] no | 437 s | 21:23 |
| 10⁶ | 1133 (±297.2), 1746580..1747712 | 0.344 | PASS / PASS (2.3·10⁻¹⁹) | (ii) no; (iv) [0.91, 1.30] no | 458 s | 21:31 |

* The supervisor `launch_heights.sh` (pid 13906) ran batch 1 (10⁴ ‖ 10⁵, 21:15:40–21:23:15) then batch 2 (10⁶, 21:23:15–21:30:53), then `aggregate.py` → **`CAMPAIGN.md` v1 (21:31:16 IST)**, and exited (`logs/launch.log`). No stop condition fired at any height ((iii) is the checker's).
* **The DH sub-task is DONE (22:18 IST; nothing is running any more).** `dh_offline_scan.py` (attempt 4; attempts 1–3 are in the log with their defects) scanned f_DH in blocks of 10 from 46 to the 30-minute cap at T = 900: the known orbit at 85.699 RE-FOUND, and **25 further off-line orbits in the strip** (t = 114.16, 166.48, 176.70, 240.40, 320.88, 331.05, 366.64, 411.80, 440.48, 520.94, 531.28, 548.91, 566.51, 595.02, 611.78, 646.99, 657.11, 692.89, 737.77, 783.65, 811.77, … to 900; all to |f| ≤ 4·10⁻¹³; `dh_offline_scan.json`). The zero-side V.4 control was run at the first three new heights (`dh_control_new_heights.py`; rows in the JSON and in `CAMPAIGN.md` §1): the channel fires at the theorem's bandwidth at every one (ratio to δ²e^{δL/2} at L*: 30.7 at t = 114.16, 172.8 at t = 166.48, 14.2 at t = 176.70) and W_{Z′} stays at 10⁻¹⁴–10⁻²² there. Caveats as at 85.7 (window hypothesis not verified — the scan shows an orbit every ≈ 35 units; reflection condition fails; reflected points omitted). The record's "DH at one height only" is superseded: the negative control now stands at four heights.
* Checkpoints 1–3 (hashes of every zeros / rows / summary / log file, the controls and the stop-condition lines per height, CAMPAIGN.md v0 and v1) are in `results/c2-m2/SHARED.md` (appended by `checkpoint.sh`).
* Heavy-process check: `ps -Ao pcpu,comm | awk '$1>50'` (should show at most the DH scan now).

## 2. Where the outputs land and what each is

* `zeros_<tag>.json` — `{t, U_data, dps, date, checks{monotone, count, rvm_expected, index_lo, index_hi, seconds_per_zero, max_residual}, zeros: [[n, γ, |Z(γ)|], …]}`; every zero of ζ with |γ − t| ≤ U_data = 2·U(L_min = 4) (≈ 286–297).
* `rows_<tag>.csv` / `.json` — one row per (δ, L): the L-grid 4…120 step 2 plus L*(δ, t; C₁ = 1) and L*(δ, t; C₁ = 2.4·10⁹); columns: `inside_hypotheses` (L ≥ L*(C₁ = 1) and t ≥ 21L — rows with False are measurements below the theorem's hypotheses), `reflection_ok`, `deltaL_ge_25`, `n_zeros_used`, `U_row`, `U_kopt`, `k_opt`, `tail_bound_at_U_row`, `U_contract_k3` (the contract's k = 3 radius), `c_deltaL`, `main_term` (−2δ²c²), `N_Z` = `W_Zprime` (positive control), `W_Z` (= N_Z + main; E₋ excluded), `W_Zrep`, `near_gamma`, `near_term`, `W_Zdouble_minus_Zprime_bound_log10` (II.4 double, Lemma-G bound), `clause6_bound` (δ²e^{δL/2}), `sep_over_clause6`, `W_Z_negative`, `bal3`, `clause4_bound_C1_1` (2b₁ℓ_R/L²; asserted for L ≥ 50), `clause4_over_N`, `density_model` (16.62·log(t/2π)/L³), `N_over_model`, `N_Z_center_mean/median/min/max` and `center_mean_over_model` (143 centers t′ = t + 2j), `E_minus_bound_log10` (clause 1, rigorous), `E_minus_est_log10` (envelope, computed), `E_minus_direct` (where computed), `refl_online_bound_log10` / `_est_log10` (the reflected on-line points), `Lstar_C1_1`, `Lstar_C1_zeta`, `L_ann`.
* `summary_<tag>.json` — the per-height record: zeros checks, controls (`positive_pass`, `negative_pass`, min W_{Z′}, clause-4 violations), `derived` (L_sign, L_bal3 per δ at t; fine grid step 0.1), `ensemble` (per δ: median / p10 / p90 / min / max of L_sign and L_bal3 over the centers; per L: mean/min/max of N_Z and mean/model), `stop_conditions` (i, ii, iii pending, iv with the stated rule), timings, hashes of the row files.
* `finescan_<tag>.json` — N_Z(L) at t on the fine grid 3.0…120 step 0.1.
* `outwindow_test.json` — item (6): per (L, u ∈ {5, 50, 500, 81L}) the exact pair contribution, the clause-5 pointwise bound, the envelope estimate; `u_true` per L (the radius at which the true contamination reaches e^{−L}).
* `dh_offline_scan.json` — the DH sub-task: blocks, off-line zeros found (in the strip / outside), the control rows at any new height, `known_refound`.
* `logs/height_<tag>.log` — the human-readable record per height (self-tests at 10³, zeros, the full row printout, the ensemble table, the two V.4 controls, the four stop conditions quoted verbatim with their values).

## 3. The exact harvest recipe (when `summary_t1e6.json` exists, or whenever you want an interim table)

1. `cd "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/c2-m2/campaign"`
2. `python3 aggregate.py` — rebuilds `CAMPAIGN.md` from whatever `rows_*.json` / `summary_*.json` exist (v1 when all four heights are present): §1 per-height record (zeros, controls, stop conditions), §2 the twelve-point tables of L_sign and L_bal3 (at t, and median [p10, p90] over the centers), §3 the three-law comparison (δ-ratios against 1.12 : 2.9 : 5; least-squares exponents b, c of log L = a + b log(1/δ) + c log log(t/2π); each law with a free prefactor, "within a factor 1.5" yes/no), §4 the four §2(d) closes as filled-in sentences, §5 the record-point rows, §6 compact grid rows at δ = 0.1, §7 the Instruments-table row, §8 hashes. The supervisor runs this itself after t = 10⁶.
3. Read `logs/dh_offline_scan.log` (last line: "DH control available at N further height(s)" or "DH at one height only …"); if a new orbit was found, its control rows are in `dh_offline_scan.json` → add one line to `CAMPAIGN.md` §1 (the V.4 negative control at the second height) by hand, quoting the log.
4. Append a checkpoint block to `results/c2-m2/SHARED.md` with the SHA-256s printed at the end of `CAMPAIGN.md` §8 (`shasum -a 256 <file>`), dated (`date`), and the stop-condition lines of each height (grep `"(i) \|(ii) \|(iv) "` in `logs/height_<tag>.log`).
5. Checker (Opus, half slot): per height, 20 random zeros of `zeros_<tag>.json` re-verified at 30 digits (`mpmath.zetazero(n)` at mp.dps = 30 + Newton on `siegelz`), two rows of `rows_<tag>.json` recomputed with an INDEPENDENT transform (own quadrature of B̂ — not `campaign_lib.py`), compared to 10⁻⁸ relative on W_Z (the main term dominates; W_{Z′} at the record points is 10⁻⁸–10⁻¹⁴ in absolute size, so compare it absolutely at 10⁻¹⁰ or relatively against W_Z); verdict appended to `SHARED.md` and `CHECK-O.md`. A mismatch stops the leg (stop condition (iii)).
6. Then the orchestrator's items (BRIEF "On completion"): C2 Instruments row (CAMPAIGN.md §7) + work-log line; IV.9 rider if the closes change the visibility numbers (they do not move L*; they measure L_sign ≈ 7–32 at 10³ against the theorem's 121–862); STATUS/LOG (hashes); commit + push. Then Session 23 stream 2: M6 rung 1 (PRICING §3(d)); then M4 (i) (PRICING §1(b)).

## 4. Stop conditions (PRICING §2(e)), status

| | condition | rehearsal value | status |
|---|---|---|---|
| (i) | `zetazero` at n ≈ 1.75·10⁶ > 2 s/zero | 0.329 s/zero (5 consecutive zeros, n = 1 747 146–150) | does not fire |
| (ii) | positive control W_{Z′} < 0 at any L at 10³ | min 4.1·10⁻¹⁹ (183 rows + 1171 fine-grid L) | does not fire |
| (iii) | checker's independent transform off by > 10⁻⁸ relative | — | pending the checker |
| (iv) | density model vs measured N_Z off by > 10× at 10³ | center-mean N_Z/model ∈ [0.42, 1.08], geometric mean 0.65 (rule stated in the log: the model is an ensemble mean and is compared with the mean over the 143 centers; single-t dips to 0.003 at L = 48, 86, 120 are the zeros of B̂(0.208L) for the nearest zero — a configuration effect) | does not fire |

Each production height re-evaluates (ii) and (iv) for itself and prints them; (i) is the rehearsal's.

## 5. What the contract got wrong (for the orchestrator; also in SHARED.md checkpoint 1)

* **Data cost at L_min = 4 with the k = 3 tail:** PRICING §2(b)'s "≈ 25 min at 10³ / 1.7 h at 10⁶" are the L = 10 and L = 8 figures; at the contract's own L_min = 4 with ‖B‴‖₁ the radius is 1.7·10⁴–2.1·10⁴ (2·10⁴–8·10⁴ zeros per height, 1–6.5 h). The same clause-4 mechanism with k ≤ 13 (computed norms) gives U(4) ≈ 143–149 at every height: minutes. Adopted; both radii printed per row.
* **The "numerical decay rate 0.849"** (note §6, `lemma_G_constants_run.log`) is the pre-asymptotic local rate at η ≈ 256–8192; the transform's envelope is 9η^{−3/4}e^{−√(η/2)} (saddle-point form; local rate 0.80 at 10³ falling to 0.73 at 5·10⁴, asymptote 1/√2 = 0.707), checked by the Poisson-trapezoid rule at 3/2 the nodes (`logs/height_t1e3.log` (S)). The note's tabulated |B̂(16384)| = 1.76·10⁻³⁷ was quadrature noise at 30 digits (the true value is ≈ 10⁻⁴²). The record's (7/(8·0.85))² = 1.06 for the true R₀ becomes 1.53 asymptotically; the measured u_true/L = 1.09–1.10 at L = 30–120 (finite-L, with the polynomial prefactor).
* **Stop condition (iv) as written** compares an ensemble mean with a single-t measurement; at L ≳ 20 the single-t noise is dominated by the nearest zero and oscillates with the zeros of B̂ — the rule needs the center-mean (implemented and stated).
* **The 10⁻⁸ relative tolerance for the checker** cannot apply to W_{Z′} at the record points (10⁻⁸–10⁻¹⁴ absolute); apply it to W_Z (main-term-dominated) or absolutely at 10⁻¹⁰.
