# A4 no-go paper — citable data tables with provenance

**Prepared:** 2026-08-26, for the A4 no-go paper.
**Scope:** every table and number the paper cites from the decision run and its follow-up,
each row tagged with its on-disk source (file + JSON key or report section). All paths are relative
to `results/a4-m2-gate/` unless noted; paths that begin `results/` or `directions/` are relative
to `rh-program/` in the repository. `RUN` = `RUN-REPORT.md`, `AUD` = `AUDIT.md`,
`FUP` = `FOLLOWUP-REPORT.md`, `SPEC` = `SPEC.md`.
**Verification discipline:** every number below was read from the named on-disk
file while this digest was being prepared. Numbers additionally re-verified here — either opened directly in
the raw JSON and compared against the report, or re-derived by an independent computation — are
marked **[V]**. Numbers taken from a report/spec claim without an independent raw-data or analytic
check are marked **[R]** (report-sourced). One benign bookkeeping discrepancy is
flagged loudly in Section 10; **no substantive discrepancy was found.**

Raw JSONs opened directly: `gate-result.json`, `witness_N64.json`, `followup-near-cue.json`,
`followup-p1.json`, `runs/tighteps_N64.json`, `runs/scans_N64.json`, `runs/scans_N128.json`,
`runs/tier2_N64.json`, `runs/windows_N64.json`, `runs/explore_lamp.json`, `runs/budgets_lam0p5.json`.
Independent re-derivations run here: eps law, p1 corners, 4128/33, 2·sqrt(2), the block-law
identity c = 3F − 2 (+ atom correction term, m = 1..8, exact integer check), ppp resonance re-sieve
to 3e6, sign change of 2·m2 − m3 (flat), closed forms m2 = 1/lambda + lambda/3 and
m3 = 1 + 1/lambda^2 at lambda in {1/2, 1}, and the E[N_d]/N ratios.

---

## 1. The decision grid: 940 records, delta_0 = 0

**Verdict: ABSORPTION** — machine-readable `"verdict": "absorb"`, `bite_rule: false`,
`absorb64: true`, `absorb128: true` [V: `gate-result.json: verdict`].

| item | value | provenance |
|---|---|---|
| Grid axes, N = 64 | budget variant {matched, asymptotic} x W {2,3,4,6,8} x C_led {10,100,1000} x eps {0.02,0.05,0.10} x fuzz {coupled, none, Gamma 0.05/0.10/0.25} x bars {off,on} = **900 records** | [V: `runs/scans_N64.json: grid` — counted 900 records here; axes RUN Sec 1 + SPEC Sec 5] |
| Grid axes, N = 128 | variant {matched, asymptotic} x W {2,3,4,6,8} x fuzz {coupled, none} x bars {off,on} = **40 records** | [V: `runs/scans_N128.json: grid` — counted 40; RUN 4.2 "all 40 N=128 records"] |
| Total records | **940** | [V: 900 + 40; RUN Sec 1 "940 grid records"] |
| max abs(delta_0), N = 64 grid | **6.394884621840902e-13** | [V: computed max over all 900 records of `runs/scans_N64.json: grid[].delta_0` here; equals `gate-result.json: verdict.d0_max_abs_over_grid`] |
| max abs(delta_0), N = 128 grid | **8.93507490218326e-13** | [V: computed max over all 40 records of `runs/scans_N128.json: grid[].delta_0` here] |
| Headline bound | abs(delta_0) < 1e-12 at every one of the 940 records | [V: both maxima above are < 1e-12; RUN Sec 1] |
| LP duality gap | ~ 1e-9 | [R: RUN Sec 1; not independently recomputed] |
| Infeasibility / solver failures | none: every record's status = (0,0,0) | [V: set of status tuples over all 940 records = {(0,0,0)}, checked here] |
| delta_0(W) per W (primary point) | W=2: −3.77e-13; W=3: +1.44e-13; W=4,6,8: 0.0 exactly; fit delta_inf = 0, zero residual | [V: `gate-result.json: delta_0_per_W`, `W_fit`] |
| Gamma-slope | d delta_0 / d Gamma = 0.0 | [V: `gate-result.json: gamma_slope`] |

**Citation note on the max:** `gate-result.json`'s `d0_max_abs_over_grid` = 6.39e-13 is the N = 64
grid max; the overall 940-record max is the N = 128 value 8.94e-13. Both are < 1e-12, so the
RUN Sec 1 headline "abs(delta_0) < 1e-12 at every one of the 940 grid records" is correct; the paper
should cite < 1e-12 (or 8.94e-13) for the full grid, not 6.39e-13.

### 1.1 The exact eps law (asymptotic budgets)

Law: **P(eps) = 5/6 − (2/3)·eps**, the grid-decoupled lemmaR_tight corner; limit 5/6 as eps -> 0
[`gate-result.json: eps_law`; RUN 4.2; analytic identification AUD 3.6].

| eps | P (asymptotic, LP) | 5/6 − (2/3)·eps (re-derived) | abs(delta_0) | provenance |
|---|---|---|---|---|
| 0.02 | 0.8200000000002683 | 0.8200000000000001 | 2.8e-13 | [V: `runs/tighteps_N64.json: eps_trend` (asymptotic, fuzz none); closed form recomputed here] |
| 0.01 | 0.8266666666669427 | 0.8266666666666667 | 2.4e-13 | [V: same] |
| 0.005 | 0.8300000000002841 | 0.8300000000000001 | 2.2e-13 | [V: same] |
| 0.002 | 0.8320000000003910 | 0.8320000000000001 | 1.0e-13 | [V: same] |

Matched-variant values differ only through the finite-size budget center (e.g. P = 0.8368627361
at eps = 0.002, from B1 = 84.712 < (4/3)·64 = 85.33) [V: `runs/tighteps_N64.json` matched records;
RUN 4.2 "0.83686"]. Pricing at the tightest asymptotic point converged clean: S = 200,
0 improving columns, min_rc = 0.0 for both full and base systems
[V: `runs/tighteps_N64.json: verify_tightest`].

Auditor's independent LP re-solve of the eps cells (own linprog, re-derived row data):
primary 0.80509568 (delta −4e-14), asymptotic eps .002: 0.83200000 (−1e-13), asymptotic eps .05:
0.80000000 (−5e-14), W-scan all < 4e-13 [R: AUD 3.6 table; auditor's own run, matches the raw JSONs
opened here].

---

## 2. Primary decision point and N = 128 confirmation

**Primary point:** flat/flat windows, lambda' = 1/2, N = 64, matched budgets, eps = 0.05,
C_led = 100, coupled fuzz.

| item | value | provenance |
|---|---|---|
| P_full = P_base | **0.8050956815843511** (report: 0.80510), delta_0 = −3.8e-13; identical optimal laws | [V: `runs/scans_N64.json` record (matched, W=2, C_led=100, eps=.05, coupled, bars off); RUN 4.2] |
| Witness-law P | **0.8050956815846874** = 51.52612362142/64 | [V: `gate-result.json: verdict.witness_P` and `witness_N64.json: P`; ratio recomputed here] |
| Matched budgets (B1, B2, B3) | (84.71214548308222, 135.09544203420174, 304.5549106659001) | [V: `witness_N64.json: budgets`] |
| Coupled-fuzz usage | g* = 1.5e-4; cubic slack 22.1 = 7% of budget at Frobenius cost 0.0095; same P at fuzz = none (fuzz row not load-bearing) | [R: RUN 4.2 primary-point block] |
| Error-bars-on variant | P = 0.7994992161 (bars shift the level, not delta_0 = 0) | [V: `runs/scans_N64.json` bars=true record] |
| P depends only on (variant, eps); P_base = P_cal at every record — the lambda'-Frobenius row alone adds nothing to the two-moment baseline | confirmed | [V: spot-checked P_cal = P_base = P_full across opened records; RUN 4.2 "whole grid" paragraph] |

**N = 128 confirmation** (same anchors, seed + column generation; 40 records, delta_0 = 0 throughout):

| variant | eps | P_full = P_base | provenance |
|---|---|---|---|
| matched | 0.05 | **0.8024488905983833** (report: 0.80245), delta_0 = 0.0 exactly at the (W=2, coupled, bars off) record | [V: `runs/scans_N128.json: grid[0]`; RUN 4.2] |
| asymptotic | 0.05 | **0.8000000000004773** (report: 0.80000), delta_0 = 2.9e-13 | [V: `runs/scans_N128.json`; RUN 4.2] |

Pricing verification at decision points: no improving column (reduced cost < −1e-6) in S = 200
restarts at the primary and tightest-asymptotic points; S = 100 at N = 128; S = 40 at W-scan
re-checks, all with min_rc = 0.0, n_improving = 0 [V: `runs/scans_N64.json: verify` (W3–W8 blocks,
S = 40) and `runs/tighteps_N64.json: verify_tightest` (S = 200); RUN 4.2].

---

## 3. The primary witness (absorbing law, `witness_N64.json`)

Three columns, all supported on the 65-site psi_1-zero grid, spacing 64/65 = **0.9846153846153847**
[V: `witness_N64.json: psi1_zero_step`; 64/65 recomputed]. Marks {1, 2} only, no pairs, n_ = 0.
Cell: N = 64, matched budgets, eps = 0.05, fuzz = none [V: `witness_N64.json: description`].

| weight | column | N_d | F1 (= sum m^2) | F' | C' | provenance |
|---|---|---|---|---|---|---|
| 0.5299906673474316 | vacancy lattice: 64 simples on 64 of the 65 grid sites | 64 | **64 exact** (float 64.000000000007) | **125.0909091 = 4128/33 exact** | 245.4508724 | [V: `witness_N64.json: law[0]` + `clean_checks[0]` (F1_clean 64.00000000000003, Fp_clean 125.09090909090911, Cp_clean 245.4508723599633); 4128/33 = 125.09090909... recomputed here; exact-rational F' also hand-derived by the auditor, AUD 3.5] |
| 0.16040139164388625 | 16 doubles + 32 simples on an explicit 48-site subset | 48 | 96 exact | 153.7604346 | 411.0865130 | [V: `witness_N64.json: law[1]` + `clean_checks[1]`] |
| 0.30960794100868216 | 32 doubles on an explicit 32-site subset | 32 | 128 exact | 135.1959163 | 301.3541693 | [V: `witness_N64.json: law[2]` + `clean_checks[2]`] |

Site subsets (atom positions) recorded per column in `witness_N64.json: law[].atoms` /
`grid_sites` [V: opened; canonical clean integer grid description vs optimizer float positions
agree to max_dev 3.4e-6 / 1.6e-5 / (col 3 same class) per `clean_checks[].max_dev`].

**Aggregates** [V: `witness_N64.json: E`]:
E[F1] = 88.94775275723633 (= upper edge B1·(1+eps) = 84.712·1.05 = 88.9478 [V: product recomputed]);
E[F'] = 132.81813304702743 (inside [128.34, 141.85]); E[C'] = 289.32716513260516 (= lower edge
B3·(1−eps) = 304.555·0.95 = 289.327 [V: product recomputed]); E[N_d] = 51.52612362142, i.e.
**E[N_d]/N = 0.8050956815846875** [V: ratio recomputed] <= 5/6 + 0.01 (SPEC 5.4 absorption bar).

Active rows at the optimum: only F1_hi and Cp_lo (margins −7.8e-3·scale and 1.9e-15); every ladder
row slack by orders of magnitude — law[1].nV = [16, 2, 0, ...], law[2].nV = [3, 2, 0, ...], the
vacancy column's nV all zero; E[n(2)] = 3.50 and E[n(3)] = 0.94 against caps C_led·N·V^-4 = 400
and 79.0 [V: `witness_N64.json: active_rows`, `law[].nV`; expectations recomputed 2026-08-26 —
CORRECTED from the earlier "nV = 0 vectors", which was false against the file on disk]. Fraction-arithmetic
re-verification: all 10 row checks true, objective_exact = 0.8050956815845, obj_dev 5e-13,
all_ok = true [V: `witness_N64.json: rational_verify`]. Auditor independently recomputed all three
columns through a position-space path: every row value reproduces to 1e-6 or better, feasibility
re-confirmed at C_led = 100 **and** C_led = 10 [R: AUD 3.5].

---

## 4. The near-CUE (pinned) class at decision grade (FUP Sec 2; `followup-near-cue.json`)

Row class: the unpinned decision rows (fuzz = none, the harsher variant for absorption) + open-band pinning
abs(E_w|c_j|^2 − j) <= tau2 for 1 <= j < N at lambda = 1, edge row free; unconditional basis
BGSTB24 Theorem 1 in the depth-weighted reading [V: `followup-near-cue.json: row_class`].

### 4.1 N = 64 four-cell table (matched budgets, C_led = 100, W <= 8)

| tau2 | eps | P_full^pin | P_base^pin | delta_0' | last S=200 residuals (full/base) | reading | provenance |
|---|---|---|---|---|---|---|---|
| 1 | 0.05 | 0.8332334059839699 | 0.8332334059839699 | **0.0 (exact)** | −1.18e-5 / −9.31e-6 | absorb, decision grade | [V: `followup-near-cue.json: N64.cells[0]` incl. `colgen.verify`; FUP 2.2] |
| 1 | 0.02 | 0.8359542395410772 | 0.8359374423865479 | 1.6797e-5 | −4.74e-5 / −1.34e-6 | absorb (0 within residual band [−3.1e-5, +1.8e-5]) | [V: cells[1]; band from FUP 2.2] |
| 4 | 0.05 | 0.8150864520465212 | 0.8137831067863290 | 1.3033e-3 | −3.98e-4 / −2.43e-4 | bounded residual, sub-decision scale | [V: cells[2]] |
| 4 | 0.02 | 0.8316328692004420 | 0.8301979402692543 | 1.4349e-3 | −6.95e-4 / −4.41e-4 | bounded residual, sub-decision scale | [V: cells[3]] |

Decision-grade discipline at the primary cell: delta_0' = 0 is an exact LP equality (identical
optima) at every one of 9 cumulative S = 200 verification passes across a ~1,100-column dictionary
enrichment (P fell 0.8333622 -> 0.8332334 with the equality never breaking — residual improvements
are common-mode); reduced-cost bound for the true marginal value: abs(delta_0') <= 1.2e-5
[R: FUP 1, 2.2; pass structure in `runs/followup_t2n64.log`; final-pass residuals [V] above].
tau2 = 4 residuals exceed their pricing bands ([0.9e-3, 1.5e-3]) and were still declining with
enrichment (1.28e-3 -> 1.17e-3 over five passes): **unconverged upper bounds at loose pinning, an
order below the decision scale (1e-2..3e-2)**, with the cubic row active there [R: FUP 1, 2.2].

Asymptotic re-centering (stability): P_full = P_base = **0.8332332347490976**, delta_0' = 0.0 exact
[V: `followup-near-cue.json: N64.recenter_asymptotic`].

### 4.2 The near-CUE witness, N = 64

**64 columns, marks {1, 2} only, no pairs, no marks >= 3**; weights 6.2e-5..0.0753, N_d per column
50..60 (4–14 doubles on CUE-like positions) [V: `followup-near-cue.json: witness_N64.law` — counted
64 columns, weight and N_d ranges computed here; FUP 2.3 states "1e-4..0.075, N_d 50..60"].

Aggregates [V: `witness_N64: E`]: E[N_d]/N = 53.32693798297409/64 = **0.8332334059839699**
[V: ratio recomputed]; E[F1] = 87.24729; E[F'] = 136.08081; E[C'] = 311.35710;
E|c_j|^2 = j + 1 for every j = 1..63 (S1 array = [2.000000, 3.000000, ..., 64] to 2e-12; max
deviation 1.84e-12 at j = 62 — CORRECTED 2026-08-26 from "to 1e-13") — **all 63
upper pinning rows active at exactly the +tau2 allowance**; max abs(E|c_j|^2 − j) = 1.0000 uniformly
[V: `witness_N64: E.S1` opened and inspected; `active_rows` lists t2_hi_j1..j63 only].

**Structural finding (absorption by slack):** the only active rows at the pinned optimum are the
63 pinning rows (and mass); F1, F', C', and every ladder row are strictly interior — the cubic
block does not even bind [V: `witness_N64: active_rows` contains only t2_hi_j* entries;
FUP 2.3]. Fraction re-verification: all row-class checks true incl. `tier2_all_j`,
all_ok = true, worst pinning margin −1.0e-9 inside the documented 1e-6 grace
[V: `witness_N64: rational_verify`; margin figure R: FUP 2.3].

### 4.3 N = 128 confirmation

| item | value | provenance |
|---|---|---|
| Bootstrap | pinned LP infeasible on the 527-column dictionary of the main decision run; feasible after +300 CUE/doubles-decorated-CUE columns; build-out to 6,739 columns | [V: `followup-near-cue.json: N128.bootstrap`] |
| First-pass cell (1842 cols) | P_full = P_base = 0.8941703559642387, delta_0' = 7.8e-16 | [V: `N128.first_pass_cell`] |
| Matched cell (tau2=1, eps=.05) | P_full = P_base = **0.8374218534574983**, delta_0' = **0.0 exact**, 6,457 columns, 10 cumulative S = 200 passes | [V: `N128.continuation_cell`; pass count R: FUP 2.5] |
| Final S=200 residuals | full −6.1e-4, base −8.7e-4 (plateau, common-mode; equality held at every pass while P fell 0.894 -> 0.8374) | [R: FUP 2.5; endpoint P values V above] |
| Build-out invariance | delta_0' <= 8e-16 at every intermediate dictionary state; only pinning rows ever active — verdict independent of convergence level | [R: FUP 2.4] |
| Witness | 128 columns, marks {1,2}, no pairs; E|c_j|^2 = j + 1 − 1e-5 at every j = 1..127 (interior-shrunk upper edge; witness LP solved at tau2 − 1e-5); Fraction re-verification against the TRUE tau2 = 1 box: all rows pass incl. tier2_all_j, worst pinning margin +1.0e-5 strictly interior | [V: `followup-near-cue.json: witness_N128` — 128 columns counted, S1 = j + 0.99999 inspected, cell note and rational_verify.all_ok = true opened; margin figure R: FUP 2.5] |
| Witness aggregates | E[N_d]/N = 107.19000239208492/128 = **0.8374219** [V: ratio recomputed]; E[F1] = 172.596; E[F'] = 274.708; E[C'] = 632.559; E[n_simple]/N = 86.380/128 = 0.6748 | [V: `witness_N128: E`] |
| Asymptotic re-centering | P_full = P_base = **0.8373740026259704**, delta_0' = 0.0 exact (5 passes at S = 100, residuals ~1.0–1.4e-3) | [V: `N128.recenter_asymptotic`; pass detail R: FUP 2.5] |

Level trend: P^pin = 0.8374 (N = 128) vs 0.8332 (N = 64), both ~ 5/6 − O(1e-3) (pinned-baseline
finite-size trend); delta_0' = 0 exactly at both sizes and both budget centerings, with the same
only-pinning-rows-active structure [V: table values above; FUP 2.5].

**tau2 = 4 pricing bands for the paper's residual table:** delta_0' = 1.30e-3 (eps .05, band
[0.9e-3, 1.5e-3]) and 1.44e-3 (eps .02); final verification residuals −4.0e-4/−2.4e-4 and
−6.9e-4/−4.4e-4; shortened runs (max_outer = 2, max_rounds = 8), recorded deviation
[V: cell records incl. `deviation` field; bands R: FUP 2.2].

---

## 5. p1-objective (simple-fraction benchmark; FUP Sec 3; `followup-p1.json`)

Objective: minimize E_w[p1], p1(c) = (#mark-1 atoms + 2 x #multiplicity-1 pairs)/N — the model
analog of the simple-zero fraction; on-line-only variant a labeled diagnostic
[V: `followup-p1.json: objective_definition`]. Dictionary: `runs/dict_N64_fu.json`, 5,134 columns
(followup-enriched); stop rule SPEC 3.3 applied to both systems [V: `configuration`].

| cell | p1_full | p1_base | p1_cal | delta_p1 | analytic corner 2 − (B1/N)(1+eps) | converged | provenance |
|---|---|---|---|---|---|---|---|
| matched, eps = .05 | 0.6101913631697143 | 0.6101913631684138 | 0.6101913631688707 | 1.3e-12 | **0.6101913631681821** [V: recomputed 2 − (84.71214548308222/64)·1.05 here, matches to 1e-16] | **yes**: S = 200 clean, min_rc = 0.0, 0 improving, both systems | [V: `cells[0]` incl. `colgen_verify`] |
| asymptotic, eps = .002 | 0.6640000000012899 | 0.6640000000004871 | 0.6640000000007121 | 8.0e-13 | **0.6640000000000001** [V: recomputed 2 − (4/3)·1.002; -> 2/3 as eps -> 0] | **yes**: S = 200 clean, both systems | [V: `cells[1]`] |

Cross-checks (LP-only over the final dictionary) [V: `followup-p1.json: cross_checks`]:
coupled fuzz at the primary cell delta_p1 = 2.9e-13; W-scan W in {2,3,4,6,8}:
max abs(delta_p1) = 1.3e-12 (at W = 8; all < 1.4e-12); on-line-only objective delta_p1 = 3.3e-13
(P_full 0.6101913631687432, "no colgen under this objective" per its note).
Witness laws: the same psi_1-grid family as the unpinned witness of Section 3 — vacancy lattice (64 simples,
weight 0.4435 matched / 0.2414 asymptotic), a doubles grid column, the 32-doubles lattice —
reweighted per cell; rational verification passes [V: `cells[].witness_law` opened (vacancy column
weight and row values match the Section 3 witness's clean values); R: FUP 3 for "10-doubles" naming].

Notes the paper will cite [R: FUP 3 notes (i)–(iii)]: the p1 optimum is the exact marks-{1,2}
doubles corner (pairs cannot help — a mult-1 pair buys 2 simple points at F1 >= 2x the two-simples
cost; a mult-2 pair is dominated by two doubles); the eps -> 0 value 2 − 4/3 = **2/3** is the
model's bandwidth-one analog of Montgomery's simple-zeros corner, while the cited **0.6818287**
ceiling belongs to the window-optimized certificate (Theorem-D effect), which the flat/flat
decision program deliberately does not consume [cross-ref `results/full-map.md` lines 35/54: 0.6818287 =
PairCeiling 256-law cap, p0 = 0.68182868746... exactly rational].

---

## 6. Null-budget Monte Carlo: implementer vs auditor, with closed-form anchors

Closed forms (budget centers), all re-derived here from m2 = 1/lambda + lambda/3,
m3 = 1 + 1/lambda^2 [V]: m2(1) = 4/3, m3(1) = 2, m2(1/2) = 13/6 = 2.166667, m3(1/2) = 5.
The identity m2(lambda) = kappa(lambda) (the paper's unconditional prime-side second-moment
constant) is the second-order verification [R: SPEC Sec 2 line 91; AUD 3.3].

**Implementer's CUE MC** (QR-with-phase-fix Ginibre, R adaptive to SE(m3) <= 0.5%, batch-means SE
+ jackknife) [V: all rows opened in `runs/budgets_lam0p5.json: sizes` and match RUN 4.1's table]:

| n | R | m2(1) | m2(1/2) | m3(1/2) |
|---|---|---|---|---|
| 64 | 4000 | 1.32363(74) | 2.11087(63) | 4.75867(362) |
| 128 | 2000 | 1.32867(77) | 2.13845(71) | 4.87769(411) |
| 256 | 600 | 1.33115(66) | 2.15231(63) | 4.93758(373) |
| 512 | 300 | 1.33199(86) | 2.15958(67) | 4.96843(413) |
| 1024 | 120 | 1.33364(110) | 2.16362(83) | 4.98715(476) |
| 2048 | 48 | 1.33400(94) | 2.16505(83) | 4.99323(504) |
| 1/n fit -> inf | | 1.33394(63) | 2.16682(52) | 5.00056(311) | 
| closed form | | 1.33333 (4/3) | 2.16667 (13/6) | 5 |

[V: extrapolation row from `budgets_lam0p5.json: extrapolation` (1.3339390(6.27e-4),
2.1668186(5.21e-4), 5.0005576(3.11e-3), `anchor_ok: true` for all three); halt_flags = [] (empty).]

**Auditor's independent MC** (own QR sampler, fresh seeds 777001/777002) side by side
[R: AUD 3.2 — auditor's own run; agreement within ~1 combined sigma per entry]:

| n | m2(1) auditor / implementer | m2(1/2) auditor / implementer | m3(1/2) auditor / implementer |
|---|---|---|---|
| 64 | 1.32317(105) / 1.32363(74) | 2.11120(84) / 2.11087(63) | 4.76099(491) / 4.75867(362) |
| 256 | 1.33045(132) / 1.33115(66) | 2.15305(103) / 2.15231(63) | 4.94059(616) / 4.93758(373) |

**Ladder/occupancy side data** [V: `budgets_lam0p5.json: sizes.64/.128`, `occupancy_check`]:
null ladder floor C_led^min = 3.8188 at n = 64 (RUN: 3.82), 3.9119 at n = 128 (RUN: 3.91);
E[n(V)]/n on V = [2,3,4,...] = [0.23868, 0.01364, 0, ...] (n = 64); max abs(eig) over 4000 draws
= 3.977 (RUN: 3.98). Occupancy-2 cross-term shares: Frobenius 0.52626 (52.6%), cubic 0.78986
(79.0%) — vs the SPEC's analytic 54% / 80% (7/6 of 13/6; 4 of 5) [V: json; SPEC line 113].
Implementer's own sine-moment sanity MC (independent of the budgets run): m2(1) = 1.33383(114),
m3(1) = 2.00255(396) at n = 256; lambda' = 1/2 extrapolations 2.16682(52) / 5.00056(311)
[R: RUN Sec 3 bullet 1]. Auditor's third route for m3(1/2) = 5: real-space 2D determinantal
quadrature 4.9896 -> 4.9932 trending to 5 with truncation X = 40/80 [R: AUD 3.3].

---

## 7. Residual-scoping table: "exact zero is flat/flat-specific; bounded residuals elsewhere"

The paper's central honesty table (AUD finding 1 wording bar: claim "delta_0 = 0 exactly at the
primary flat/flat configuration; <= O(1e-4) across the window family and <= O(5e-4) under near-CUE
pinning at this scale, within pricing-convergence uncertainty" — plus the decision-grade tau2 = 1
zeros of Section 4, which post-date and strengthen that wording).

| configuration | residual delta_0 | status | provenance |
|---|---|---|---|
| flat/flat, entire 940-record decision grid | **0 (< 1e-12)** | exact; witness-backed | [V: Section 1] |
| flat / cos(1.6 s) at lambda' (v' changed) | 5.95e-14 (eps .05), −1.14e-13 (eps .02) — **0** | exact-zero class: lambda' window change moves nothing (the absorber's freedom is positional, not spectral) | [V: `runs/windows_N64.json` combo flat_cos08; RUN 4.4] |
| cos(sqrt2 s) [MT] / flat (lambda = 1 window changed) | **+6.41e-5** (eps .05), +2.28e-5 (eps .02) | bounded residual: MT cosine breaks the exact grid degeneracy (kernel zeros not equally spaced); unconverged upper bounds, three orders below eps-slack scale | [V: `runs/windows_N64.json` cosMT_flat; RUN 4.4 "+6.4e-5 / +2.3e-5"] |
| cos(sqrt2 s) [MT] / cos(1.6 s) | +6.27e-5 (eps .05), +1.91e-5 (eps .02) | same class | [V: `runs/windows_N64.json` cosMT_cos08; RUN 4.4 "+6.3e-5 / +1.9e-5"] |
| near-CUE tau2 = 1 (decision grade, N = 64 and 128, both centerings) | **0 exact** (bound abs(delta) <= 1.2e-5 at N = 64) | absorption by slack | [V: Section 4] |
| near-CUE tau2 = 4 (loose box, diagnostic) | 1.30e-3 / 1.44e-3 (eps .05/.02), pricing bands [0.9e-3, 1.5e-3]; earlier values from the main decision run, 1.28e-3 / 1.48e-3 | unconverged upper bounds, order below the decision scale (1e-2..3e-2); cubic row active here | [V: Section 4.1 + `runs/tier2_N64.json` (0.0012824, 0.0014840); FUP 1] |
| auditor's tight-eps pinned probes (dictionary-limited, no column generation) | 6.0e-6 (eps .02), 5.0e-4 (eps .01), 3.9e-4 (eps .005) — **<= 5e-4**, non-monotone, same order as the documented ~3e-4 pricing uncertainty | upper bounds; "where any residual signal concentrates" | [R: AUD 4.4 / finding 1] |
| pinned-class table from the main decision run (pre-followup snapshot) | tau2 = 1: 0 (eps .05), 6.0e-6 (eps .02); tau2 = 4: 1.28e-3, 1.48e-3; pinned pricing then-unconverged at −2.9e-4 | superseded by Section 4's decision-grade rerun; cite only as the audit-time state | [V: `runs/tier2_N64.json`; RUN 4.3] |

---

## 8. Exploratory lambda' scan (OUTSIDE THE PROVEN LADDER; payoff-curve data only)

**Labeling (binding):** lambda' > 1/2 + o(1) is OUTSIDE the proven theta < 1 ladder regime, and
values there are quarantined from every certificate claim; these are payoff-curve data, NOT
certificate claims; column generation ran at reduced budget, so positive values are heuristic
upper-anchored [R: RUN 4.4 label; the quarantine is recorded in
`results/adjudication-A4.json: mandatory_repairs`].

| lambda' | eps | P_base | P_full | delta_0 | provenance |
|---|---|---|---|---|---|
| 0.55 | 0.05 | 0.8053310433508489 | 0.8053310433508484 | **0** (−5.6e-16) | [V: `runs/explore_lamp.json`] |
| 0.55 | 0.02 | 0.8251787278264935 | 0.8251787278264899 | **0** (−3.6e-15) | [V: same] |
| 0.60 | 0.05 | 0.8058514020011891 | 0.8062187975519491 | **+3.67e-4** | [V: same; RUN "+3.7e-4"] |
| 0.60 | 0.02 | 0.8256842190868753 | 0.8259625547887860 | **+2.78e-4** | [V: same; RUN "+2.8e-4"] |
| 0.65 | 0.05 | 0.8059503048717801 | 0.8086104956189072 | **+2.66e-3** | [V: same; RUN "+2.7e-3"] |
| 0.65 | 0.02 | 0.8263688470852664 | 0.8278795159840451 | **+1.51e-3** | [V: same; RUN "+1.5e-3"] |

Interpretation for the paper: the cubic row's marginal value turns positive between lambda' = 0.55
and 0.60 — precisely where the flat-window moment margin 2·m2 − m3 = 2/lambda + 2·lambda/3 − 1
− 1/lambda^2 changes sign, at lambda = **0.6105** [V: sign-change root recomputed here by
sympy nsolve (0.610511...); RUN 4.4 says "~ 0.61"] — and grows toward lambda' = 2/3 (the
Rudnick–Sarnak-range endpoint). Consuming it requires progress on the moderate-deviation
large-value estimate MD(lambda, delta), which is exactly what the quarantine above excludes; at the
proven operating point lambda' = 1/2 + o(1) the value is exactly zero
[R: RUN 4.4; SPEC 8.5 pre-registered expectation confirmed].

---

## 9. BGSTB24: the citation behind the pinning rows, previously recalled but unverified, checked here (FUP Sec 4)

**Source provenance** [V where marked]: a direct arXiv download was refused from this network, so
the file was taken from the arXiv dataset mirror
`https://storage.googleapis.com/arxiv-dataset/arxiv/arxiv/pdf/2306/2306.04799v1.pdf`
(v2/v3: 404) [R: FUP 4]; **210,602 bytes** [V: size of the retrieved file checked = 210602],
PDF 1.4, 13 pages [R: FUP 4]. The PDF is not redistributed with this repository for copyright
reasons; retrieve it from arXiv:2306.04799v1, or cite the published version (Acta Arithmetica,
2024).

**Bibliographic identification** [R: FUP 4, read off the title page of arXiv:2306.04799v1]:
Siegfred Alan C. Baluyot, Daniel Alan Goldston, Ade Irma Suriajaya, Caroline L. Turnage-Butterbaugh,
"An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta function",
arXiv:2306.04799v1 (June 9, 2023; dedicated to Iwaniec's 75th birthday). **Two citation
corrections** to the way this source had previously been cited [R: FUP 4]: (1) the uniform range is the **closed**
band 0 <= alpha <= 1, not abs(alpha) < 1 (the paper notes Theorem 1 includes the [GM87, Lemma 8]
improvement "up to alpha = 1 with explicit error terms", p. 2); (2) the published version is
**Acta Arithmetica 2024** — cite as BGSTB24, arXiv v1 June 2023.

**What is licensed** [R: FUP 4, tightly paraphrased]: Theorem 1 ((1.4)) is unconditional and
pointwise in alpha, uniformly on 0 <= alpha <= 1: F(alpha) = T^(−2 alpha)(log T + O(1)) + alpha
+ O(1/sqrt(log T)), for F defined with zeros counted with multiplicity and off-line zeros entering
with the depth weight x^(delta+delta') — exactly the cosh depth-weighting the model's form factor c_j applies. With
alpha = j/N, each open-band row is licensed **pointwise per row, unconditionally**, in the
depth-weighted multiplicity-counted form (directly, or through the Lemma 5 admissible kernel class
(3.3)–(3.4): even, L^1, supported in [−1,1], Lipschitz at 0 — the bandwidth-1 class); the diagonal
spike is confined to the edge rows the pinning class leaves free; the Poisson factor w acts below the model's
1/N bin resolution whenever N << log T.

**The THREE LICENSING RIDERS** (the paper must carry all three; FUP 4 riders (i)–(iii),
tightly paraphrased [R]):

1. **Depth-aggregation only.** The licensed statistic never separates on-line from off-line mass —
   the Remark after Theorem 2 states the method "neither requires nor provides any information"
   about whether the zeros are on the critical line. What is pinned is the model's cosh-weighted
   aggregate abs(c_j)^2 (pairs entering with depth weights), never an on-line-only S(j). Shedding
   the far-off-line coupling term S(T) ((5.2)) costs an extra hypothesis — the thin box (1.5)/(6.1)
   or the strong zero-density hypothesis (1.6)/(6.2), via (6.3) — which Theorems 2–3 (the 61.7%
   simple-zeros results) consume; the row class itself needs none of that.
2. **Finite-T slack O(N/sqrt(log T)).** The licensed per-row slack at finite T is O(N/sqrt(log T))
   grid units (plus the edge spike), so tau2 in {1, 4} is the fixed-N, T -> infinity asymptotic
   reading — legitimate for the asymptotic semantics of the decision program, but at honest finite T the
   O(1)-unit pinning overstates the theorem until log T >> N^2, **and the no-go must say so.**
3. **Second-moment scope.** The paper stops at the second moment — pair correlation only; nothing
   in it licenses the cubic budget column, whose c_3(lambda') identification stays on flag F2
   (Rudnick–Sarnak-range GUE 3-level correlations) exactly as before.

Net wording [R: FUP 4 closing]: the pinning rows are an unconditional asymptotic data class,
pointwise on the open band in the depth-weighted form; BGSTB24 is the correct citation, now
checked rather than merely recalled, in this precise sense — while the pinned verdict's
*strength* ("absorption inside
the parent ceiling's own data class") inherits riders (i)–(iii) verbatim.

---

## 10. Audit trail digest

**The auditor's 8 break attempts** (AUD Sec 4; one line + outcome each) [R: AUD 4.1–4.8]:

1. Independent witness recomputation (different code path, exact-rational spot check) — reproduces
   exactly, feasible. FAILED to break.
2. Harsher ladder: imposed **per column** at C_led = 4 (below the SPEC minimum 10, barely above the
   null floor 3.82) — absorption survives, P_full = P_base = 0.8 (asymptotic eps .05),
   delta_0 = 8e-14. FAILED.
3. Missing-row hunt: every constraint row of the system either imposed or automatic on explicit spectra; n_- <= (number of pairs) confirmed
   on all 4003 columns. PARTIAL (led to major finding 2, the near-CUE promotion — since executed,
   Section 4).
4. Near-CUE pinning with the auditor's own |c_j|^2 rows: tau2 = 1, eps .05 reproduces
   P = 0.8333622, delta_0' = 0 exact; tight-eps probes leave <= 5e-4 upper-bound residuals.
   No decision-relevant bite. (Feeds Section 7's scoping row.)
5. Window-degeneracy probe: MT-cosine residuals ~2e-5–6.4e-5, three orders below decision scale.
   (Feeds finding 1 / Section 7.)
6. Base-corner attack via pairs: the atom-only sandwich is airtight (F1 >= sum m^2 proven); the
   pair-interference channel (negative lambda = 1 cross-terms lowering F1) is not analytically
   excluded and rests on converged pricing (min_rc = 0 at S = 200). FAILED to break — **the one
   channel not closed analytically** (= minor finding 4; the paper's model-level theorem should
   restrict to atom-only configurations or close it analytically).
7. Budget-center stress (flag F2): delta_0 = 0 across eps 0.002–0.10, Gamma to 0.25, matched vs
   asymptotic centers differing by 5% — an O(1)-per-zero c_3 error cannot flip the verdict. FAILED.
8. Seed/scale stability: fresh-seed MC within 1 sigma; N = 64 -> 128 stable; W-independence exact
   by inclusion (marks {1,2} witness lies inside every W-class). FAILED.

**Independent recomputation stats** [R: AUD 3.6]: the auditor recomputed the row data for **all
4003 dictionary columns** through a position-space Gram path (vs the implementation's Fourier/W3
assembly): max relative deviation **3.3e-15**; ladder-count mismatches 0; stored pinned-class form
factors exact match; n_ <= p violations 0 of 4003; own linprog re-solves match `gate-result.json`
to LP tolerance (Section 1.1 table). Grid Parseval identity independently re-derived (DFT Parseval
on Z_65) and checked on 40 random grid configurations: max abs(F1 − sum m^2) = 4.5e-13 [R: AUD 3.1].
Pair block law independently rebuilt: cubic charge 2·m^3·(1 + 3·A'^2), never 0 at any depth
(8.0005 at w = 1/64, 8.033 at w = 1/8), c = 3F − 2 exact at every depth — falsifying the "+8 vs 0"
premise this computation had been set up to test, and superseding the earlier phase model that
premise came from [R: AUD 3.4].

**Audit findings register** [R: AUD 5]: FATAL none. MAJOR (wording of the write-up, not the verdict):
(1) the exact zero is window-specific (Section 7 wording bar); (2) promote a near-CUE witness to
decision grade — **executed**, Section 4; (3) scope the headline to the N_d benchmark or run the
p1 variant — **executed**, Section 5. MINOR: (4) the pair-interference channel (above);
(5) the W = 2 infeasibility reason reported for the aggregated calibration harness (`SPEC.md` Section 4.4;
`runs/tier_a.json`) is cosmetic (correct sharper reason: the iso world is confined
to c = 3F − 2, forcing 4.5 != 5); (6) bookkeeping drift, next paragraph; (7) the "+8 vs 0" premise
falsified (a finding *for* the implementation).

**Known bookkeeping drift (cite-safe note):** RUN 4.3's pinned-class value 0.833377 (= `runs/tier2_N64.json`
0.8333765 [V]) vs the `gate-result.json` verify block's 0.8333622 reflect different dictionary snapshots
(AUD minor 6); the followup's decision-grade value at that cell is 0.8332334 on the enriched
dictionary (Section 4.1) — the common level moves with the dictionary, the equality delta_0' = 0
does not. Witness column tags (cg_rc-...) are not unique identifiers; the recorded content is.

**Followup deviations-from-SPEC, one paragraph** [R: FUP 5]: at the tau2 = 1 N = 64 cells the
literal S = 200 zero-improving stop was never attained (the position-continuum pricer keeps finding
~1e-5 common-mode improvements), so 8 cumulative S = 200 passes + a re-certification pass were
applied with the exact equality holding at every pass and the reduced-cost bound <= 1.2e-5
reported; the tau2 = 4 cells ran shortened (max_outer = 2, max_rounds = 8) after a wrapper-process
kill (~05:12) whose in-memory columns were lost and re-found, with all completed-cell results on
disk; N = 128 needed a feasibility bootstrap (+300 CUE/doubles-decorated columns, anti-absorption-
safe) and its witness LP was solved at tau2 − 1e-5 interior shrink after a −3.4e-6 HiGHS-tolerance
overshoot on one row; the p1 phase needed no reductions (literal S = 200 clean pass, both systems,
both cells); thermal pools of 2. Deviations in the main decision run are RUN Sec 6 items 1–8 (alias-free
tight-frame eigenvalue assembly; 1e-12-rationalization Fraction re-verification rather than
exact-rational end-to-end; reduced pricing budgets at non-decision points; the 1/8 atom-separation
gap not enforced in pricing — strictly adversary-favorable, witness min gap 0.985; reduced window
scans; labeled beyond-SPEC tight-eps points; the pinned class then-unconverged; adaptive MC counts).

---

## 11. Verified constants block

| constant | value | status | provenance |
|---|---|---|---|
| m2(lambda) closed form | 1/lambda + lambda/3; m2(1) = 4/3, m2(1/2) = 13/6 | [V: recomputed exactly here; MC-confirmed Section 6; auditor hand re-derivation AUD 3.3] | SPEC Sec 2 (derivation Sec 9); RUN Sec 3 |
| m3(lambda) closed form | 1 + 1/lambda^2; m3(1) = 2, m3(1/2) = 5 | [V: recomputed; MC + auditor's 2D determinantal quadrature] | SPEC Sec 2/9; AUD 3.3 |
| kappa identity | m2(lambda) = kappa(lambda) (unconditional prime-side second moment) exactly, every lambda <= 1 | [R: SPEC line 91 "= the paper's unconditional prime-side kappa(lambda) EXACTLY"; AUD 3.3 calls it "the strongest possible identity check at second order"] | SPEC Sec 2; AUD 3.3 |
| Montgomery–Taylor cross-check | min over cos-window family of m2(1; v) = 1.327499 at vartheta = 1/sqrt(2), matching 1/c* = **1.3274993** | [R: SPEC line 96, verify V1/V2; not recomputed here] | SPEC Sec 2 |
| Window-margin cross-check | 2·m2 − m3 = **0.685244** at v = cos(1.6 s), lambda = 1, confirming the previously recorded 0.68524 | [R: SPEC line 96 / SPEC Sec 10 F3 "now VERIFIED here"; not recomputed here] | SPEC Sec 2, Sec 10 |
| ppp resonance | sum_p (log p)^3/(p−1)^2 = **2.315762** (sieved to 3e6) | [V: re-sieved here: 2.3157616478; third independent confirmation after SPEC, RUN, and AUD] | SPEC Sec 2/9; RUN Sec 3; AUD 3.7 |
| Fuzz capacity constant | 2·sqrt(2)·sqrt(C_led·eps_g) = spectral-escape cap per N; 2·sqrt(2) = **2.8284271247** [V: recomputed]; LP-confirmed 2.8244 at h_max = 400 (gap = truncation tail 3/h_max, as predicted); **three independent confirmations** (SPEC 4.2/9.3 min-profile derivation; implementer's analytic re-derivation + LP, RUN Sec 3; auditor's own min-profile optimum, AUD Sec 2 row 5). Corrects two earlier values for this constant, both withdrawn: 2·sqrt(C·eps) and a first-pass 5/sqrt(3) (SPEC flag F6) | [V constant; R derivations] | SPEC 4.2/9.3/F6; RUN Sec 3; AUD 2 |
| Block-law identity | pair at ANY depth: c = 3F − 2 exactly (per zero: F = 1 + A'^2, c = 1 + 3·A'^2); atom of mark m: c = 3F − 2 + (m−1)(m−2); pair cubic charge 2·m^3·(1 + 3·A'^2) >= 8·m^3 at every depth ("+8 vs 0" premise false) | [V: atom identity 3m − 2 + (m−1)(m−2) = m^2 checked exactly for m = 1..8 here; pair identity 3(1 + A^2) − 2 = 1 + 3A^2 is algebraic; numeric depth scan R: AUD 3.4 (8.0005 at w = 1/64), RUN Sec 3] | SPEC 1.2 (lines 56–58), Sec 9; RUN Sec 3; AUD 3.4 |
| Cubic-row content | isolated-block content = sum m(m−1)(m−2): zero on marks {1,2} and on ALL pairs; all discriminating power in marks >= 3 + clustering cross-terms | [V: immediate corollary of the verified identities above] | SPEC 1.2; AUD 3.4 |
| Doubles-plane diagnostic | G(lambda) = m3 − (3·m2 − 2): G(1) = 0 ("2 = 2"), G(1/2) = +1/2 | [V: G(1) = 2 − (4 − 2) = 0 and G(1/2) = 5 − (13/2 − 2) = 1/2 recomputed] | SPEC Sec 2 line 117; AUD 3.3 |
| 2·m2 − m3 sign change (flat) | at lambda = **0.6105** (RUN: "~ 0.61") | [V: sympy nsolve here] | RUN 4.4 |
| Grid step | 64/65 = **0.9846153846** (psi_1-zero grid, 65 sites at N = 64) | [V: `witness_N64.json: psi1_zero_step` + recomputed] | RUN Sec 2/5 |
| Vacancy-lattice exact rationals | F1 = 64 exact; F' = **4128/33** = 125.090909... | [V: `witness_N64.json: clean_checks[0]`; 4128/33 recomputed; auditor's hand derivation 4096/33 + 32/33, AUD 3.5] | witness_N64.json; AUD 3.5 |
| Occupancy-2 shares (lambda' = 1/2) | analytic 54% (Frobenius, 7/6 of 13/6) / 80% (cubic, 4 of 5); null MC 52.6% / 79.0% at n = 64 | [V: MC values from `budgets_lam0p5.json: occupancy_check` (0.52626/0.78986); analytic fractions recomputed] | SPEC line 113; RUN Sec 2 |
| Formalized parent ceilings (context; NOT outputs of this computation) | bandwidth-one certificate ceiling **0.6818287** (PairCeiling 256-law, p0 = 0.68182868746... exact rational, hypothesis EnclOK only); lemmaR_tight two-moment tightness; second-moment barrier **0.8453**: 2 − kappa(lambda) is maximized at lambda = sqrt(3) with value 2 − 2/sqrt(3) = 0.845299... [V: recomputed here], and kappa >= 2/sqrt(3) > 1 for all lambda > 0, so the trace/Frobenius certificate caps below 0.8453 at ANY Dirichlet-polynomial length | [V: 0.6818287 and lemmaR_tight in `results/full-map.md` lines 6, 35, 54, 101; 0.8453 in full-map.md lines 311, 315 and `directions/A4-lindelof-lock.md` line 36; 2 − 2/sqrt(3) recomputed] | results/full-map.md; directions/A4-lindelof-lock.md |
| Model p1 corner | eps -> 0 value 2 − 4/3 = **2/3** (bandwidth-one analog of Montgomery's simple-zeros corner); distinct from the 0.6818287 window-optimized ceiling | [V: Section 5] | FUP 3 |

---

## Verification tally (standard applied: at least 15 load-bearing numbers re-verified from raw JSON)

Re-verified directly from raw JSON against the reports while preparing this digest (all matched; see [V] tags):
(1) 900 N = 64 grid records and their max abs(delta_0) = 6.39e-13; (2) 40 N = 128 records, max
8.94e-13; (3) primary P = 0.8050956815843511; (4) witness_P = 0.8050956815846874 and E[N_d]/N
ratio; (5) N = 128 matched 0.8024488906 and asymptotic 0.8000000000; (6) all four tight-eps
asymptotic P values vs the recomputed law 5/6 − (2/3)eps; (7) tightest-point S = 200 clean verify;
(8) all three witness columns of Section 3 (weights, N_d, F1 = 64/96/128, F', C', 4128/33); (9) witness
aggregates and rational_verify all_ok; (10) the main run's pinned four-cell table; (11) all four
followup near-CUE N = 64 cells incl. residuals; (12) N = 64 asymptotic re-centering 0.8332332347;
(13) N = 128 continuation cell 0.8374218535 / delta 0.0 / 6,457 columns and re-centering
0.8373740026; (14) both near-CUE witnesses (64/128 columns, marks {1,2}, S1 = j+1 resp. j+1−1e-5,
aggregates, rational_verify); (15) both p1 cells vs the recomputed analytic corners, plus the
coupled-fuzz/W-scan/on-line-only cross-checks; (16) the full null-MC table incl. extrapolations,
C_led floors, occupancy shares; (17) all six window-scan records; (18) all six lambda'-scan
records; (19) the size of the BGSTB24 PDF retrieved in Section 9, 210,602 bytes. Independent re-derivations: eps law, p1 corners,
closed forms, ppp resonance, 2·sqrt(2), c = 3F − 2 identities, G-diagnostic, sign-change root,
grid step, 4128/33.

**Discrepancies found: none substantive.** Two cite-safety notes: (a) the 6.39e-13 in
`gate-result.json` is the N = 64-only max — the 940-record max is 8.94e-13 (Section 1);
(b) the pinned-class snapshot drift 0.833377 / 0.8333622 / 0.8332334 across dictionary states (Section
10, AUD minor 6). The constant 0.8453 was located and verified (2 − 2/sqrt(3) at lambda = sqrt(3);
full-map.md lines 311/315), closing the last open item.
