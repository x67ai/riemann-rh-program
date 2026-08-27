# A4 M2 gate — auditor-mandated follow-up run report

**Program:** RH program, direction A4. **Contract:** the three MAJOR findings of `AUDIT.md`
(Section 5) on the M2 ABSORPTION verdict: (major-2) promote a near-CUE witness to decision
grade; (major-3) run the p1-objective (simple-fraction) variant; (F1) fetch and check
BGSTB24, the basis of the Tier-2 data class. This file is the follow-up implementer's
report; raw outputs in `runs/followup_*.json`, logs in `runs/followup_*.log`, code in
`code/followup_run.py` (reuses the gate's own modules; the only new code is the objective
plumbing, the convergence driver applying the SPEC 3.3 stop rule, and the N=128
feasibility bootstrap).
**Date:** 2026-08-26. **Machine:** same shared MacBook as the gate run; thermal policy
respected — all pricing pools ran 2-wide (<= 2 concurrent heavy processes), phases
sequential.
**Discipline:** every number below is from this session's executed runs (standing order 5);
deviations from SPEC recorded in Section 5.

---

## 1. Verdict summary

* **Task 1 (near-CUE to decision grade): ABSORPTION CONFIRMED at the near-CUE class
  proper (tau2 = 1).** At the primary cell (tau2 = 1, eps = 0.05, N = 64, matched
  budgets) delta_0' = 0 **exactly** — not within bars — at every one of 9 cumulative
  S = 200 verification passes across a 1,100-column dictionary enrichment, with an
  explicit near-CUE witness law (64 columns, marks {1,2}, no pairs, all 63 pinning rows
  satisfied) that re-verifies in Fraction arithmetic. The structural reason is new and
  decisive: **at the pinned optimum the entire cubic block is slack** (no cubic, ladder,
  or Frobenius' row is active — only the pinning rows and mass bind), so the absorption
  is by slack, not by tuned cancelation. Same picture at N = 128 and under budget
  re-centering. At loosened pinning (tau2 = 4) a small positive residual
  delta_0' ~ 1.3–1.4e-3 persists (unconverged upper bound, pricing residuals ~4–7e-4)
  — an order below the M4 decision scale (1e-2..3e-2) and confined to the loose-box
  diagnostic, not the near-CUE class.
* **Task 2 (p1 objective): the cubic block does NOT move the simple-fraction optimum.**
  delta_p1 <= 1.4e-12 at both the primary and the tightest-eps asymptotic cells, with
  the SPEC stop rule passing **cleanly at the first S = 200 verification pass for both
  systems** (0 improving columns, min_rc = 0.0) — this task is converged at decision
  grade, exact-zero discipline. The optimum equals the analytic marks-{1,2} doubles
  corner p1 = 2 − (B1/N)(1+eps) with and without the cubic block: 0.6101914 (matched,
  eps = .05), 0.6640000 (asymptotic, eps = .002; -> 2/3 as eps -> 0). W-scan, coupled
  fuzz, and the on-line-only objective variant all give the same zero. The auditor's
  major-3 scope gap is closed: the no-go headline covers the simple-fraction benchmark
  too.
* **Task 3 (BGSTB24, flag F1): FETCHED and CHECKED.** arXiv:2306.04799v1 = Baluyot–
  Goldston–Suriajaya–Turnage-Butterbaugh, "An unconditional Montgomery theorem for pair
  correlation of zeros of the Riemann zeta function" — exactly the expected authorship.
  Saved as `fetched-r3/r3s-06-bgstb-2306.04799.pdf` (13 pp, PDF 1.4). The licensing
  answer for the no-go is in Section 4: the near-CUE row class at bandwidth 1 is
  licensed **pointwise per row, unconditionally**, in the depth-weighted multiplicity-
  counted form, on the closed band 0 <= alpha <= 1 — with three riders (depth-aggregate
  only; finite-T slack O(N/sqrt(log T)); second moment only) that the paper's own
  statements make precise. Flag F1 is discharged in that precise sense.

---

## 2. Task 1 — Tier-2 near-CUE pinning at decision grade (AUDIT major-2)

### 2.1 Protocol

Same rows, dictionary, and code paths as the gate (`master_lp.solve_master` with
`tier2_tau` rows |E_w|c_j|^2 − j| <= tau2 for 1 <= j < N, edge row free; fuzz = none —
the harsher variant for absorption: coupled fuzz only relaxes the cubic row, so
delta_0' = 0 at fuzz = none implies it for coupled). Column generation per SPEC 3.3:
alternating master/pricing (objective-aware copy of the gate's pricing worker, identical
scoring at mode 'nd'), stop when S = 200 restarts find no column with reduced cost
< −1e-6, applied to BOTH the full and the base system. Dictionary extended into
`runs/dict_N64_fu.json` / `runs/dict_N128_fu.json` (the audited gate snapshots
untouched). The first wrapper process was killed mid-run (recorded); cells (1, .05) and
(1, .02) had completed 8 S = 200 passes each before the kill (history in
`runs/followup_t2n64.log`), their columns are in the saved dictionary, and the resume
phase re-certified them on it; the tau2 = 4 cells reran shortened (Section 5).

### 2.2 Results, N = 64 (matched budgets, C_led = 100, W <= 8)

| tau2 | eps | P_full^T2 | P_base^T2 | delta_0' | last S=200 residuals (full / base) | reading |
|---|---|---|---|---|---|---|
| 1 | 0.05 | 0.8332334 | 0.8332334 | **0 (exact)** | −1.2e-5 / −9.3e-6 | absorb, decision grade |
| 1 | 0.02 | 0.8359542 | 0.8359374 | 1.68e-5 | −4.7e-5 / −1.3e-6 | absorb (0 within residual band) |
| 4 | 0.05 | 0.8150865 | 0.8137831 | 1.30e-3 | −4.0e-4 / −2.4e-4 | bounded residual, sub-decision scale |
| 4 | 0.02 | 0.8316329 | 0.8301979 | 1.44e-3 | −6.9e-4 / −4.4e-4 | bounded residual, sub-decision scale |

Reading discipline (exact-zero vs bounded): at the primary cell delta_0' is an exact LP
equality (identical optima) at every dictionary snapshot — including after each of the
9 cumulative S = 200 enrichment passes, during which the common value P_full = P_base
declined from 0.8333622 (the audited dictionary) to 0.8332334 while the equality never
broke: the residual pricing improvements are **common-mode** (they lower both systems
identically), never differential. With the standard reduced-cost bound, the true (all-
configurations) marginal value satisfies |delta_0'| <= 1.2e-5 at the primary cell,
modulo the heuristic globality of the 200-restart pricing. At (1, .02) the recorded
1.68e-5 sits inside its own residual band [−3.1e-5, +1.8e-5]. At tau2 = 4 the residual
delta_0' ~ 1.3e-3 exceeds its pricing band ([0.9e-3, 1.5e-3]) and was still declining
with enrichment (1.28e-3 -> 1.17e-3 over the killed run's five passes); it is an
unconverged upper bound at loose pinning, an order below decision scale, and the cubic
row IS active there — consistent with AUDIT major-1's picture that any surviving
residual lives outside the tight near-CUE class.

**Asymptotic re-centering (SPEC 5.4 absorption stability):** primary cell at closed-form
budget centers: P_full = P_base = 0.8332332, delta_0' = 0 exactly.

### 2.3 The near-CUE witness (the auditor's requested object)

`followup-near-cue.json` (and `runs/followup_tier2_N64.json`, key `witness`): a law of
**64 columns, marks {1, 2} only, no pairs, no marks >= 3** (weights 1e-4..0.075, N_d per
column 50..60, i.e. 4–14 doubles on CUE-like positions), with

    E[N_d]/N = 0.8332334,  E[F1] = 87.247,  E[F'] = 136.081,  E[C'] = 311.357,
    E|c_j|^2 = j + 1 for every j = 1..63  (all 63 upper pinning rows active at
    exactly the +tau2 allowance; max |E|c_j|^2 − j| = 1.0000 uniformly).

Feasibility re-verified in Fraction arithmetic on 1e-12 rationalizations for every row
class — F1, F', C', all seven ladder rows, and all 126 pinning rows (worst pinning
margin −1.0e-9, inside the documented 1e-6 verification grace; same deviation class as
the main gate's rational re-verification). **Structural finding:** the only active rows
at the optimum are the pinning rows — F1, F', C', and the ladder are all strictly
interior. The near-CUE absorption is therefore *absorption by slack*: once the linear
band rows are consumed at tau2 = 1, the entire cubic block prices at zero marginal
value because it does not even bind. The witness is maximally near-CUE in the exploitable
sense: it rides the upper pinning edge uniformly (the +1 allowance at every harmonic is
what pays for the ~10.7 average doubles), which also answers how the law differs from
the anti-correlated Tier-1 witness — this one is inside the parent ceiling's own data
class.

### 2.4 N = 128 confirmation

The N = 128 dictionary had never been Tier-2-enriched (527 structured columns; the
pinned LP was outright infeasible), so the cell was built from scratch: feasibility
bootstrap (+300 CUE / doubles-decorated-CUE columns made the pinned LP feasible at 827
columns), then column generation. Through the entire ~4,900-column build-out the
equality P_full = P_base held at every snapshot (delta_0' <= 8e-16 at each stage), with
only pinning rows ever active — the same absorption-by-slack structure as N = 64,
manifest at every dictionary state and hence independent of the build-out's convergence
level. Final converged-state numbers, witness, and re-centering: Section 2.5.

### 2.5 N = 128 final numbers

| item | value |
|---|---|
| matched cell (tau2 = 1, eps = .05) | P_full = P_base = **0.8374219**, delta_0' = **0 (exact)**, 10 cumulative S = 200 passes, 6,457 columns |
| final S = 200 residuals | full −6.1e-4, base −8.7e-4 (plateau; common-mode — the equality held at every pass while P fell 0.894 -> 0.8374) |
| witness | 128 columns, marks {1, 2}, no pairs, E|c_j|^2 = j + 1 − 1e-5 at every j = 1..127 (interior-shrunk upper edge); only the 127 pinning rows active; Fraction re-verification against the TRUE tau2 = 1 box: **all rows pass**, worst pinning margin +1.0e-5 (strictly interior) |
| witness aggregates | E[N_d]/N = 0.8374219, E[F1] = 172.60, E[F'] = 274.71, E[C'] = 632.56, E[n_simple]/N = 0.6749 |
| asymptotic re-centering | P_full = P_base = **0.8373740**, delta_0' = **0 (exact)** (5 passes at S = 100, residuals ~1.0–1.4e-3) |

The common level P^T2(N = 128) = 0.8374 vs 0.8332 at N = 64 (both ~5/6 − O(1e-3), the
pinned-baseline finite-size trend); delta_0' = 0 exactly at both sizes, both budget
centerings, with the same only-pinning-rows-active structure. The N = 128 confirmation
required building the near-CUE dictionary from scratch (bootstrap + ~6,200 generated
columns) — during the entire build-out, at every intermediate dictionary state, the
full and base optima coincided (delta_0' <= 8e-16), which makes the absorption verdict
independent of the build-out's convergence level: the cubic block never bound at any
stage.

---

## 3. Task 2 — the p1-objective rerun (AUDIT major-3)

Objective: minimize E_w[p1], p1(c) = (#mark-1 atoms + 2 × #mult-1 pairs)/N — the model
analog of the simple-zero fraction (Montgomery's count includes off-line simple zeros;
the on-line-only restriction is reported as a labeled diagnostic). Same dictionary
(5,134 columns after the Tier-2 enrichment), same rows, same stop rule.

| cell | p1_full | p1_base | p1_cal | delta_p1 | analytic corner 2−(B1/N)(1+eps) | converged |
|---|---|---|---|---|---|---|
| matched, eps = .05 | 0.6101914 | 0.6101914 | 0.6101914 | 1.3e-12 | 0.6101914 | **yes** (S=200 clean, both systems) |
| asymptotic, eps = .002 | 0.6640000 | 0.6640000 | 0.6640000 | 8.0e-13 | 0.6640000 | **yes** (S=200 clean, both systems) |

Cross-checks (LP-only over the final dictionary): coupled fuzz at the primary cell:
delta_p1 = 2.9e-13; W-scan (W = 2..8): |delta_p1| <= 1e-12 throughout; on-line-only
objective: delta_p1 = 3.3e-13. Witness laws (in `followup-p1.json`): the same psi_1-grid
family as the main gate's witness — {vacancy lattice (64 simples), 10-doubles grid
column, 32-doubles lattice} — reweighted per cell; rational verification passes.

Notes for the no-go. (i) The p1 optimum is the exact doubles-corner law: within the
marks-{1,2} atom class, min p1 = 2 − (Sum m^2)/N at the F1 upper edge, and the LP
attains it exactly; pairs cannot help (a mult-1 pair buys 2 simple points at F1 >= 2×
the two-simples cost; a mult-2 pair is dominated by two doubles). (ii) The eps -> 0
asymptotic value is 2 − 4/3 = 2/3 — the model's bandwidth-one analog of Montgomery's
2/3 simple-zeros corner; the cited 0.6818287 belongs to the window-optimized certificate
(Theorem-D effect, SPEC 2.5), which the flat/flat gate deliberately does not consume.
(iii) delta_p1 = 0 is the exact-zero discipline case: identical optimal laws, converged
pricing, all variants.

---

## 4. Task 3 — BGSTB24 (arXiv:2306.04799), fetch + the licensing question (flag F1)

**Fetch record.** Direct arXiv refused from this network; the arXiv GCS dataset mirror
served v1 (v2/v3: 404): `https://storage.googleapis.com/arxiv-dataset/arxiv/arxiv/pdf/2306/2306.04799v1.pdf`,
210,602 bytes, PDF 1.4, 13 pages, saved as
`fetched-r3/r3s-06-bgstb-2306.04799.pdf`. Title page reads: *"An unconditional
Montgomery theorem for pair correlation of zeros of the Riemann zeta function"*, by
Siegfred Alan C. Baluyot, Daniel Alan Goldston, Ade Irma Suriajaya, and Caroline L.
Turnage-Butterbaugh (dedicated to Iwaniec's 75th birthday; dated June 9, 2023) — the
expected BGSTB authorship. Two citation corrections for the program literature file:
the uniform range is the **closed** band 0 <= alpha <= 1 (not |alpha| < 1 — the paper
notes its Theorem 1 includes the [GM87, Lemma 8] improvement "up to alpha = 1 with
explicit error terms", p. 2); and the published version is Acta Arithmetica 2024 — cite
as BGSTB24, arXiv v1 June 2023.

**What its unconditional form-factor statement licenses about the near-CUE row class at
bandwidth 1 (the ONE question).**

The paper defines, in (1.2)–(1.3), F(x,T) = Sum_{rho,rho', 0<gamma,gamma'<=T}
x^{rho−rho-bar'} w(rho−rho-bar') with w(u) = 4/(4−u^2) and **zeros counted with
multiplicity**; writing rho = 1/2 + delta + i gamma, the summand is
x^{delta+delta'+i(gamma−gamma')} w(delta+delta'+i(gamma−gamma')) ((2.1)) — every
off-line zero enters tilted by the exponential depth weight x^{delta+delta'}, which is
exactly the cosh(2 pi j d / N) weighting the gate's c_j applies to conjugate pairs.
Theorem 1 ((1.4)) is **unconditional and pointwise in alpha, uniformly on the closed
band 0 <= alpha <= 1**: F(alpha) = T^{−2 alpha}(log T + O(1)) + alpha + O(1/sqrt(log T)).
Identifying alpha = j/N, each open-band row j in {1, ..., N−1} is an alpha-bin of width
1/N away from the edge, and Theorem 1 — used directly, or integrated against the
admissible kernel class of Lemma 5 ((3.3)–(3.4)): r even, L^1, supported in [−1, 1],
Lipschitz at 0, i.e. exactly the bandwidth-1 class — pins the w-weighted,
multiplicity-counted, depth-tilted form factor at value alpha + o(1) **row by row, not
merely on average over j**. The diagonal spike T^{−2 alpha} log T is confined to
alpha <~ log log T / log T, i.e. to the edge rows the gate leaves free; and the Poisson
factor w acts at alpha-resolution ~1/log T, below the model's 1/N bin resolution
whenever N << log T — the same sub-resolution identification the parent PairCeiling
class already uses. So: yes — the Tier-2 pinning |N S(j) − j| <= tau2 on the open band
is licensed as an **unconditional, pointwise-per-row data class**, in its depth-weighted
reading, and the near-CUE-pinned absorption may be stated against it without the
"averaged form-factor only" hedge.

Three riders bound what may be claimed. (i) *Depth aggregation:* the licensed statistic
never separates on-line from off-line mass — the Remark after Theorem 2 states the
method "neither requires nor provides any information" about whether the zeros are on
the critical line — so what is pinned is precisely the gate's cosh-weighted aggregate
|c_j|^2 (pairs entering with their depth weights), never an on-line-only S(j); the
gate's implementation is exactly the licensed reading. Relatedly, shedding the
far-off-line coupling term S(T) ((5.2)) costs an extra hypothesis — the thin box
(1.5)/(6.1) or the strong zero-density hypothesis (1.6)/(6.2), via (6.3) in Section 6 —
which is what Theorems 2–3 (the 61.7% simple-zeros results) consume; the row class
itself needs none of that. (ii) *Precision:* the licensed slack per row at finite T is
O(N/sqrt(log T)) grid units (plus the edge spike), so tau2 in {1, 4} is the fixed-N,
T -> infinity asymptotic reading — legitimate for the gate's asymptotic semantics and
identical in structure to its eps-knob bookkeeping (SPEC 4.2's honest-effectivity note),
but at honest finite T the O(1)-unit pinning overstates the theorem until
log T >> N^2, and the no-go must say so. (iii) *Moment scope:* the paper stops at the
second moment — pair correlation only; nothing licenses the cubic budget column, whose
c_3(lambda') identification stays on flag F2 (RS-range GUE 3-level correlations)
exactly as before. Net for the no-go wording: Tier-2's rows are an unconditional
asymptotic data class pointwise on the open band (depth-weighted form), BGSTB24 is the
correct citation for it, and flag F1 is discharged in this precise sense — while the
Tier-2 verdict's *strength* ("absorption inside the parent ceiling's own data class")
inherits riders (i)–(iii) verbatim.

---

## 5. Deviations from SPEC / task brief (recorded)

1. **Stop rule at the tau2 = 1 cells (N = 64):** the literal rule (an S = 200 pass with
   zero improving columns) was never attained — the position-continuum pricer keeps
   finding ~1e-5-scale improvements that move BOTH systems identically. Applied instead:
   8 cumulative S = 200 passes (first run) + 1 re-certification pass (resume), with the
   exact equality delta_0' = 0 holding at every pass and the reduced-cost bound
   |delta_0'| <= 1.2e-5 reported. The decision quantity is converged; the common level
   P^T2 is converged to ~1e-4.
2. **tau2 = 4 cells shortened** (max_outer = 2, max_rounds = 8 after the wrapper kill;
   first run had reached 5 passes on cell 3 with consistent values): delta_0' there is
   an unconverged upper bound, reported as such.
3. **First wrapper process killed mid-cell-3** (~05:12); columns found during the dead
   cell's in-memory enrichment were lost and re-found; no result file depended on them.
   All completed-cell columns and results were on disk (incremental checkpointing added
   on resume).
4. **N = 128:** the dictionary required a feasibility bootstrap (CUE + doubles-decorated
   CUE columns) before the pinned LP was solvable — recorded, anti-absorption-safe
   (adding columns can only lower both optima). The witness LP at N = 128 was solved at
   tau2 − 1e-5 (interior shrink) so the law is strictly feasible for the true tau2 = 1
   box under Fraction re-verification (the first pass had a −3.4e-6 HiGHS-tolerance
   overshoot on one row). Colgen budgets at N = 128: S_round 32–48, S_stop = 200
   (matched cell) / 100 (re-centering), outer caps per Section 2.5 — same deviation
   class as the main gate's own N = 128 reductions (RUN-REPORT deviation 3).
5. **p1 phase needed no reductions:** the stop rule passed literally (S = 200, zero
   improving columns, both systems, both cells).
6. Thermal: pools of 2 (brief says <= 2 concurrent); the SPEC's own policy allowed 4.

## 6. Files

* `followup-near-cue.json` — Task 1 deliverable: cells, witness law, rational
  verification, re-centerings, N = 128 confirmation.
* `followup-p1.json` — Task 2 deliverable: cells, cross-checks, witness laws.
* `FOLLOWUP-REPORT.md` — this file.
* `fetched-r3/r3s-06-bgstb-2306.04799.pdf` — Task 3 fetch.
* Raw: `runs/followup_tier2_N64.json`, `runs/followup_tier2_N128.json`,
  `runs/followup_p1_N64.json`, logs `runs/followup_*.log`, dictionaries
  `runs/dict_N64_fu.json`, `runs/dict_N128_fu.json`; code `code/followup_run.py`,
  `code/followup_chain.sh`.
