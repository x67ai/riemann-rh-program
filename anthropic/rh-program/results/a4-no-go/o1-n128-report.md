# O1 hardening + N = 128 re-run — Session 8 report

**Date:** 2026-08-26 (Session 8). **Task:** SESSION 8 QUEUE optional A4 polish — "harden the
pair-channel crowding constant 0.9775 by per-cell interval arithmetic (O1) + the mechanical
N = 128 re-run" (STATUS.md line 99; pair-channel.md items O1 and O4).
**Scripts (this directory, `verify/`):** `o1_crowding_interval.py` -> `o1_crowding_interval_out.json`
(rigorous, mpmath.iv end-to-end, directed rounding, exact rational box endpoints);
`n128_rerun.py` -> `n128_rerun_out.json` (float grade, N-parametric re-implementation of
`pairchan_verify_all.py`, N = 64 control + N = 128). Verification discipline: standing order 5 —
independent implementations, every number below re-derived this session; float hints never enter
the certified arithmetic.

---

## 1. Headline: the 0.9775 was a grid artifact, and the truth is sharper on one side, worse on the other

Theorem B(ii) of `pair-channel.md` (= paper.md Theorem 4.7) rests on the ledger condition

    Sgen2(d, d') = [ 8 nu(d) + 4 nu_joint(d, d') ] / (2 abar(2d)^2)  <=  1
    for all pair depths d, d' in the R5 family (0, 1/(2 pi)],

with the Session-7 float certification "sup = 0.9775, binding at d = 0.156". Session 8 finds:

* **The 0.004-step depth grid used in Session 7 has its last admissible point at d = 0.156**
  (next point 0.160 > 1/(2 pi) = 0.1591549...). The quantity actually maximized was therefore
  Sgen2 over the family CAPPED at d, d' <= 0.156 — not over the full R5 family. The value
  0.9774595791839 is real and reproducible (re-derived independently on 0.004 and 0.002 grids,
  identical to 2e-15), but it is the constant of the w <= 0.98 family, not the w <= 1 family.
* **On the continuum, Sgen2 crosses 1 INSIDE the R5 family**, at d* ~= 0.1577 (equal-depth float
  crossing between 0.157 and 0.158). At the family corner the certified failure is strict
  (Section 2, C2). The full-family constant is not 0.9775; it is > 1.
* **The (MI) inequality itself shows no sign of failing there** — the Session-7 crowd+sea attack
  protocol, re-run this session AT the failure sliver (d = 0.158 and 0.159; 8/16/32/65 pairs one
  per cell tranche + greedy mark-2 seas of 16..130 atoms), never brings F1 - T below **+17.47**
  (d = 0.158) / **+17.50** (d = 0.159), against a floor requirement of 0. What fails on the
  sliver is this ledger bookkeeping route, not (numerically) the inequality.

So the hardening does NOT certify w <= 1 — and not because enclosures were too wide: the true
continuum value genuinely exceeds 1 on the deepest ~1% of the family (float crossing d* ~= 0.1577;
certified bracket (0.156, 0.158)). The certified repair below re-scopes to d <= 0.156, so the
region the ledger no longer covers is the deepest 2% of the family, w in (0.98, 1]. The certified
repair is the re-scoped statement below.

## 2. What is now rigorously certified (`o1_crowding_interval.py`)

End-to-end mpmath.iv (dps 15), per-cell branch-and-bound in x with mean-value forms in
(x, s, t); derivative enclosures via psi psi' (dR/dx = 2 Re psi psi', dR/dy = -2 Im psi psi');
closed form psi = sin(65 pi z/64)/(65 sin(pi z/64)) on cells 1..32, 32-term harmonic sum on the
peak cell; mirror symmetry psi(-x+iy) = conj psi(x+iy) proved and used (cell 65-k = cell k);
all box endpoints exact rationals; upper bounds are .b endpoints, lower bounds .a endpoints.
Self-test: iv enclosures contain independent cmath values at 4 points (PASS).

* **(C1) REPAIR — certified.** For ALL d, d' in (0, 39/250] (39/250 = 0.156 exactly; w <= 0.98018):

      Sgen2(d, d')  <=  C* = 0.9846470880   ( < 1, margin 0.0153529 )

  via a 17-box rational partition of (0, 0.156] (coarse 0.02 boxes to 0.12, refining to 0.001 at
  the corner), per-box certified nu and nu_joint upper bounds (153 unordered box pairs) and the
  termwise-monotone lower bound abar(2 d_left). Binding d-box: (31/200, 39/250] = (0.155, 0.156], equal-depth corner pair. Per-cell enclosures
  at the corner box pair (0.155, 0.156]^2 are printed in the run log and stored in the JSON
  (dominant cells: cell 1 <= 0.15080, cell 2 <= 0.03544, cell 3 <= 0.01563, cells 4..32 tail <= 0.00880 each).
* **(C2) DISPROOF — certified.** Rigorous LOWER bounds at equal-depth points inside the family
  (witness x per cell from float hints, re-evaluated in iv; numerator lower ends over denominator
  upper end):

      Sgen2(0.158, 0.158)  >=  1.001823   > 1
      Sgen2(0.159, 0.159)  >=  1.014053   > 1
      Sgen2(0.1591, 0.1591) >= 1.015279  > 1

  (float reference values 1.00182 / 1.01405 / 1.01527). Hence the both-capped ledger condition
  fails for every cap Y >= 0.158, and the crossing sits in the certified bracket
  **d* in (0.156, 0.158)**: C1 passes at 0.156, C2 fails at 0.158. The ledger makes no statement
  on d in (0.156, 1/(2 pi)] — i.e. on w in (0.98018, 1].
* **(C3) BYPRODUCT — Theorem B(i)'s stream-3 self-consistency at Y = 0.13, BOTH sides now
  interval-certified** (previously float):

      max nu_joint over (0, 0.13]^2  <=  C13 = 0.304542     (float record 0.3003)
      Phi_0 = inf { R_s(x) + R_t(x) : |x| <= 32/65, s <= 5093/16000, t <= 5093/32000 }
                                     >=  0.643710          (note's float floor "0.6665")
      2 * C13 = 0.609084  <  Phi_0   =>  one-pair-per-cell cap SELF-CONSISTENT at Y = 0.13.

  Also certified from the same tables: sup Sgen2 over (0, 0.13]^2 <= 0.704577 (float record
  0.6852). Note: the note's Phi_0 line contains an addition slip — "0.2863 + 0.3812 = 0.6665"
  should read 0.6675; the slip is conservative (the smaller floor was used) and harmless.

**What (C1)-(C3) do and do not do to Theorem B(ii).** The "one certified constant" clause is now
resolved: the constant exists and is interval-certified, but only for the family w <= 0.98; on
w in (0.98, 1] the clause is unrepairable (the ledger inequality is false there, certified).
The OTHER granted ingredient of B(ii) — the one-pair-per-cell perturber cap on (0.13, 0.156]
(its self-consistency margin 2 nu_joint <= Phi_0 holds only to Y = 0.13, now certified) — remains
granted-not-proved, exactly as O1 stated. O1's stated hardening route ("per-cell joint
optimization over the two-parameter kernel family with interval arithmetic") has been executed;
what it revealed is recorded above.

## 3. The mechanical N = 128 re-run (O4) — `n128_rerun.py`

N-parametric re-implementation of the consolidated suite (M = N + 1 harmonics u_j = 1/M,
w_s = (M - |s|)/M^2, Delta = N/M, same depth family in mean-gap units, same seed 20260826).

**Control leg (N = 64): reproduces the stored `pairchan_verify_out.json` to <= 2e-15 on every
compared constant** (S1 max, S1corr x3, alpha, deep ratio, vacancy F1, fractional attack,
Sgen2 grid value 0.9774595791839). The re-implementation is faithful.

**N = 128 results (all sections PASS; 3.8 s):**

| quantity | N = 64 | N = 128 | verdict |
|---|---|---|---|
| grid Parseval max err (40 random) | 1.8e-12 | 4.5e-12 | identity holds |
| pair block law max err | 2.9e-11 | 2.3e-13 | identity holds |
| vacancy / doubles F1 | 64 / 128 exact | 128 / 256 exact | identity holds |
| translate identities max err | 2.7e-14 | 6.8e-14 | identity holds |
| interference identity (Prop 4.1) max err | 2.2e-11 | 1.5e-11 | identity holds |
| fractional counterexample F1 - S2 (d=.25, mu=.05) | -0.035200 (= closed form) | -0.034563 (= closed form) | violation persists; closed form exact |
| spectral backstop (D): n_+ <= #at + #pr; N_d >= (4/9)(3M - F1) | all 12 pass | all 12 pass | holds |
| alpha (exact closed form) | 3.392677 | 3.341272 | -1.5% toward pi^2/3 = 3.2899 |
| max S1 | 0.6823 | 0.6822 | inequality S1 < 1 holds |
| S1corr(0.45) | 0.9205 | 0.9111 | inequality < 1 holds |
| S1corr(0.3183) | 0.6561 | 0.6538 | holds |
| S1corr(0.159) | 0.2895 | 0.2858 | holds |
| Sgen2 sup, both capped at 0.156 | 0.97746 (binding 0.156) | **0.96329** (binding 0.156) | < 1 at both N; improves with N |
| Sgen2 corner points 0.158 / 0.159 / 0.1591 | 1.00176 / 1.01402 / 1.01524 | 0.98724 / 0.99930 / **1.00050** | ledger failure exists at BOTH N |
| equal-depth crossing d* | in (0.157, 0.158) | in (0.159, 0.1591) | sliver shrinks with N but does not vanish |
| capmult-8 largest OK dcap (B(i) route) | 0.12 | 0.12 | same |
| max nu_joint over (0, 0.13]^2 | 0.30029 | 0.29463 | self-consistency margin improves |
| Phi_0 floor at Delta/2 (float) | 0.6680 | 0.6705 | improves |
| deep ratio abar(2)/abar(1) vs A(ii) target sqrt(2(N-2)) | 12.16 >= 11.14 at y = 1.0 | 11.88 < 15.87 at y = 1.0; **met at y = 1.1** (16.28) | see below |

**Two honest N-dependences (the only deviations from "constants transfer"):**

1. **Theorem A(ii)'s deep-single-pair threshold moves with N**: the crude mass bound needs
   abar(2y)/abar(y) >= sqrt(2(N-2)), i.e. sqrt(124) = 11.14 at N = 64 (met at y = 1.0) but
   sqrt(252) = 15.87 at N = 128 (met at y = 1.1). At N = 128 the statement is "d >= 1.1", not
   "d >= 1.0". Structure N-generic, constant N-dependent — exactly the O4 caveat.
2. **The Session-8 corner failure is N-generic too**: at N = 128 the ledger also fails at the
   very end of the R5 family (Sgen2 = 1.00050 at d = d' = 0.1591), with a smaller sliver
   (~(0.1590, 0.15915] vs ~(0.1577, 0.15915] at N = 64) and a better capped constant (0.9633 vs
   0.9775). The re-scoped Theorem B(ii) (w <= 0.98 mod the cap) is safe at both N; the w <= 1
   version is wrong at both N.

## 4. Crowd attacks at the failure sliver (new, float)

Session 7's `pairchan_crowd.py` attacked only d = 0.156 (believed then to be ledger-binding).
Re-run this session at d = 0.158 and 0.159 (same protocol: k in {8,16,32,65} pairs one per cell
tranche, greedy mark-2 seas of 16/32/64/130 atoms at joint-field minima):
min F1 - T = **+17.4663** (d = 0.158), **+17.5007** (d = 0.159) — same +17.5 margin as at 0.156.
The sliver's (MI) status is therefore the same adversarial-numerical strength as before; only
its LEDGER status changed (from "certified 0.9775 < 1" to "certified > 1").

## 5. Sentences that must change (quote -> replacement)

Per the dated-revision process, these edits are NOT applied here; the paper package is refereed
and the orchestrator applies them with a revision record. Certified constants below use
C* = 0.98465, L159 = 1.01405 (the certified corner lower bound at 0.159),
C13 = 0.30455, PHI0 = 0.64371.

### 5.1 `pair-channel.md`

1. **Section 0, results box, item 3** — current:
   > "and on the full R5 family d <= 1/(2 pi) (w <= 1) modulo one isolated, numerically certified cell-crowding capacity constant (ledger ratio 0.9775 at the binding depth; the residual is bookkeeping slack, not truth — the targeted crowd attacks of Section 7 stay >= +17 above the (MI) floor there)."

   Replacement:
   > "and for all pair depths <= 0.156 (w <= 0.98) modulo one isolated cell-crowding cap whose ledger constant is interval-certified (Session 8): sup_{d,d' <= 0.156} Sgen2 <= 0.98465 < 1 by per-cell rigorous enclosures (`verify/o1_crowding_interval.py`). On the deepest sliver d in (0.156, 1/(2 pi)] (w in (0.98, 1]) the ledger inequality itself fails — interval-certified Sgen2(0.159, 0.159) >= 1.01405 > 1 — so the ledger route claims nothing there; coverage on the sliver is the Section-7 attacks (re-run at d = 0.158/0.159, min F1 - T >= +17.47) plus the unconditional 8/9 backstop of Theorem D. The Session-7 ratio 0.9775 was the 0.004-grid maximum, i.e. the constant of the family capped at d <= 0.156, not the full-family sup."

2. **Section 0, item "Consequence for the no-go paper" (the line-28 paragraph)** — current fragment:
   > "and multi-pair columns with all depths w <= 0.82 (unconditional) or w <= 1 (modulo the certified crowding constant)"

   Replacement fragment:
   > "and multi-pair columns with all depths w <= 0.82 (unconditional) or w <= 0.98 (modulo the crowding cap; ledger constant interval-certified); multi-pair columns with a depth in (0.98, 1] rest on the numerical record plus the 8/9 backstop"

3. **Theorem B(ii) statement (Section 6)** — current:
   > "(ii) If every pair depth is <= 1/(2 pi) (w <= 1, the full R5 family): (MI) holds modulo the cell-crowding refinement (below), whose content is certified numerically with ratio 0.9775."

   Replacement:
   > "(ii) If every pair depth is <= 0.156 (w <= 0.98): (MI) holds modulo the cell-crowding refinement (below); its ledger constant is interval-certified, sup_{d,d' <= 0.156} Sgen2 <= 0.98465 < 1 (Session 8, `verify/o1_crowding_interval.py`). On (0.156, 1/(2 pi)] the ledger inequality fails (interval-certified Sgen2(0.159, 0.159) >= 1.01405 > 1): no ledger-grade statement is made there, and coverage is Section 7's attacks plus Theorem D."

4. **Proof sketch of (ii), first sentence** — current:
   > "The identical ledger at Y = 1/(2 pi) gives sup_d Sgen2 = 0.9775 (binding at equal depths d = 0.156), PROVIDED the one-pair-per-cell perturber cap is granted there;"

   Replacement:
   > "The identical ledger at Y = 0.156 gives sup_d Sgen2 <= 0.98465 < 1 (interval-certified; binding at the corner d = d' = 0.156), PROVIDED the one-pair-per-cell perturber cap is granted there; at Y = 1/(2 pi) the ledger fails outright (interval-certified Sgen2 >= 1.01405 > 1 at d = d' = 0.159, crossing bracket (0.156, 0.158)), so the deepest sliver carries no ledger statement and rests on the attacks plus Theorem D;"

5. **B(i) proof, stream 3** — current:
   > "with the floor Phi_0 = R_{<=0.318}(0.4923) + R_{<=0.159}(0.4923) >= 0.2863 + 0.3812 = 0.6665 (verified values)"
   and
   > "At Y = 0.13: max nu_joint = 0.3003 (at equal depths d = d' = 0.13), and 2 * 0.3003 = 0.6006 <= 0.6665 — the one-pair-per-cell cap is SELF-CONSISTENT."

   Replacement:
   > "with the floor Phi_0 >= 0.64371 (interval-certified over the full family box, Session 8; the float components 0.2863 + 0.3812 sum to 0.6675, correcting a 0.6665 slip — conservative, so nothing downstream moves)"
   and
   > "At Y = 0.13: max nu_joint <= 0.30455 (interval-certified; float 0.3003 at equal depths d = d' = 0.13), and 2 * 0.30455 = 0.60910 < Phi_0 — the one-pair-per-cell cap is SELF-CONSISTENT, now with both sides interval-certified."

6. **Section 8 item 1** — current fragment:
   > "(b) all multi-pair columns with depths w <= 0.82 unconditionally, and w <= 1 (the full R5 family) modulo one certified crowding constant;"

   Replacement fragment:
   > "(b) all multi-pair columns with depths w <= 0.82 unconditionally, and w <= 0.98 modulo the crowding cap (ledger constant interval-certified); columns with a pair depth in the deepest ~2% of the family (w in (0.98, 1]) rest on the numerical record plus the 8/9 backstop;"

   and the suggested paper wording in the same item:
   > "the corner is proved for configurations with pairs throughout the admissible depth family; for configurations with two or more pairs in the deepest 20% of the family the capacity constant is certified numerically; all remaining regimes are floored at 8/9 of the corner unconditionally."

   becomes:
   > "the corner is proved for configurations with pairs through 98% of the admissible depth family (single-pair: all of it); for configurations with two or more pairs in depths w in (0.82, 0.98] the crowding cap's ledger constant is certified by interval arithmetic; for two or more pairs in the deepest 2% (w in (0.98, 1]) the coverage is adversarial-numerical; all remaining regimes are floored at 8/9 of the corner unconditionally."

7. **Section 9, O1** — current:
   > "(O1) Theorem B(ii)'s cell-crowding refinement on (0.13, 0.159]: one finite-dimensional capacity statement, certified numerically (ledger 0.9775; crowd attacks +17), not chain-proved. Hardening route: per-cell joint optimization over the two-parameter kernel family with interval arithmetic."

   Replacement:
   > "(O1) [EXECUTED WITH CORRECTION, Session 8 2026-08-26 — `verify/o1_crowding_interval.py`] The stated hardening route was run. Outcome: (a) the ledger constant is interval-certified on (0, 0.156]^2: sup Sgen2 <= 0.98465 < 1; (b) the Session-7 full-family ratio 0.9775 was a 0.004-grid artifact — on (0.156, 1/(2 pi)] the ledger inequality FAILS (interval-certified Sgen2 >= 1.01405 > 1 at d = d' = 0.159; crossing bracket (0.156, 0.158)); coverage there is the attacks (re-run at 0.158/0.159: >= +17.47) plus Theorem D. (c) Still open on (0.13, 0.156]: the one-pair-per-cell cap itself (granted, not chain-proved; its Y = 0.13 self-consistency is now interval-certified on both sides)."

8. **Section 9, O4** — append after the current text:
   > "[EXECUTED, Session 8 — `verify/n128_rerun.py`. All identities and inequalities reproduce at N = 128 (control leg reproduces the stored N = 64 record to <= 2e-15). Constant drifts <= ~2.5% toward continuum values (alpha 3.3927 -> 3.3413; capped-0.156 ledger constant 0.97746 -> 0.96329). Two honest N-dependences: Theorem A(ii)'s deep threshold is d >= 1.1 at N = 128 (ratio target sqrt(2(N-2))); the near-endpoint ledger failure exists at N = 128 too, on a smaller sliver (crossing in (0.159, 0.1591)).]"

9. **Section 10, key certified constants line** — current fragment:
   > "Sgen2 sup = 0.6852 at Y = 0.13 and 0.9775 at Y = 1/(2 pi);"

   Replacement fragment:
   > "Sgen2 sup = 0.6852 at Y = 0.13 (interval-certified <= 0.70458) and 0.97746 at Y = 0.156 (grid; interval-certified <= 0.98465 on the continuum); at Y = 1/(2 pi) the sup exceeds 1 (interval-certified >= 1.01405 at d = 0.159);"

### 5.2 `paper.md`

10. **Abstract (the pair-channel sentence)** — current fragment:
    > "proved unconditionally for single-pair columns at every gate depth and for multi-pair columns at w <= 0.82 (w <= 1 modulo one numerically certified crowding constant)"

    Replacement fragment:
    > "proved unconditionally for single-pair columns at every gate depth and for multi-pair columns at w <= 0.82 (w <= 0.98 modulo one crowding cap whose ledger constant is interval-certified; on the deepest sliver w in (0.98, 1] the coverage is adversarial-numerical with the unconditional 8/9 backstop)"

11. **Headline 1.4(8)** — current fragment:
    > "for all multi-pair configurations to w <= 0.82 (w <= 1 modulo one certified crowding constant, ratio 0.9775)"

    Replacement fragment:
    > "for all multi-pair configurations to w <= 0.82 (w <= 0.98 modulo the crowding cap, ledger constant interval-certified at 0.98465; on w in (0.98, 1] the ledger fails — certified — and coverage is adversarial numerics plus the 8/9 backstop)"

12. **Theorem 4.7** — current:
    > "**Theorem 4.7 (multi-pair closure).** (MI) holds for every configuration all of whose pair depths satisfy w <= 0.82, unconditionally; and on the full R5 depth family w <= 1 modulo one isolated, numerically certified cell-crowding capacity constant (ledger ratio 0.9775 at the binding depth d = 0.156; the targeted crowd-plus-sea attacks at that depth — 8 to 65 pairs, one per cell tranche, plus greedy mark-2 seas up to 130 atoms, mass-free and mass-64 — never bring F1 - T below +17.4, against a floor requirement of 0)."

    Replacement:
    > "**Theorem 4.7 (multi-pair closure).** (MI) holds for every configuration all of whose pair depths satisfy w <= 0.82, unconditionally; and for all depths w <= 0.98 modulo one isolated cell-crowding cap whose ledger constant is interval-certified (sup Sgen2 <= 0.98465 < 1 on (0, 0.156]^2, per-cell rigorous enclosures; Session 8). On the deepest sliver w in (0.98, 1] the ledger inequality fails (interval-certified Sgen2 >= 1.01405 > 1 at d = d' = 0.159); there the targeted crowd-plus-sea attacks — 8 to 65 pairs, one per cell tranche, plus greedy mark-2 seas up to 130 atoms, re-run at d = 0.158 and 0.159 — never bring F1 - T below +17.47, against a floor requirement of 0, and the unconditional 8/9 backstop applies."

13. **Theorem 4.7 proof architecture** — current fragment:
    > "with a one-pair-per-cell crowding cap that is self-consistent for w <= 0.82 and is the single numerically certified constant beyond it"

    Replacement fragment:
    > "with a one-pair-per-cell crowding cap that is self-consistent for w <= 0.82 (both sides interval-certified: 2 max nu_joint <= 0.60910 < Phi_0 >= 0.64371) and whose ledger constant beyond it is interval-certified to w <= 0.98; beyond w = 0.98 the ledger fails (certified) and the closure defers to numerics plus the backstop"

14. **Section 4.3 Consequence** — current fragment:
    > "multi-pair columns at w <= 0.82 unconditionally and w <= 1 modulo the certified crowding constant"

    Replacement fragment:
    > "multi-pair columns at w <= 0.82 unconditionally and w <= 0.98 modulo the crowding cap (constant interval-certified)"

    and in the same paragraph's residue list ("The remaining admissible regimes — ..."), add
    "multi-pair columns with a depth in w in (0.98, 1]" alongside the deep-probe mixed-depth
    regime.

15. **Section 8.3 pair-channel residue (O1/O4)** — current O1:
    > "(O1) Theorem 4.7's crowding refinement on the deepest ~20% of the R5 family is certified numerically (ratio 0.9775; attacks +17.4 above the floor), not chain-proved; the hardening route is a finite per-cell joint optimization with interval arithmetic."

    Replacement:
    > "(O1) [updated Session 8] The per-cell interval hardening was executed: the crowding cap's ledger constant is interval-certified to w <= 0.98 (0.98465 < 1); the Session-7 full-family ratio 0.9775 was a grid artifact — on w in (0.98, 1] the ledger fails (certified > 1) and coverage is the attacks (+17.5, re-run at the sliver) plus the 8/9 backstop; the cap itself on w in (0.82, 0.98] remains granted-not-proved (its w <= 0.82 self-consistency is now interval-certified on both sides)."

    Current O4:
    > "(O4) The certified capacity constants are at N = 64."

    Replacement:
    > "(O4) The certified capacity constants are at N = 64; the mechanical N = 128 re-run (Session 8) reproduces every identity and inequality with <= 2.5% constant drift, moves Theorem A(ii)'s deep threshold to d >= 1.1, and shows the near-endpoint ledger failure at N = 128 as well (smaller sliver, better capped constant 0.9633)."

### 5.3 Other files quoting the constant

16. `directions/A4-lindelof-lock.md` line 178 — "(to w <= 1 modulo one float-certified crowding
    constant 0.9775)" -> "(to w <= 0.98 modulo one crowding cap, ledger constant interval-certified
    0.98465; on w in (0.98, 1] the ledger fails — certified — and coverage is attacks +
    8/9 backstop)". STATUS.md line 99 is the queue item itself (no correction needed; mark done).
    `theorems.md` needs NO change (its model theorem is stated atom-only; Remark 2.6's caveat
    stands and is unaffected). The referee reports are dated records and stay as they are.

## 6. Provenance

* `verify/o1_crowding_interval.py` -> `verify/o1_crowding_interval_out.json` +
  `verify/o1_crowding_interval_run.log` (per-box tables, per-cell corner enclosures, C2/C3
  certificates; elapsed 3209 s). mpmath 1.3.0, iv context, dps 15.
* `verify/n128_rerun.py` -> `verify/n128_rerun_out.json` + `verify/n128_rerun_run.log`
  (both-N suites, control diff vs stored, comparison tables; 4 s).
* Sliver crowd attacks: `verify/crowd_at_sliver.py` -> `verify/crowd_at_sliver_out.txt` (float
  probe; protocol identical to `pairchan_crowd.py`, run at d = 0.158/0.159); headline numbers
  +17.4663 / +17.5007 quoted above.
* `data-tables.md` has no addendum section (only inline dated corrections), so per instructions
  no edit was made there; the provenance lives in this report.
* Float references re-derived this session (48001-point x-grid, independent vectorized assembly):
  Sgen2_eq(0.158/0.159/0.1591) = 1.001819 / 1.014046 / 1.015274; nu(0.159) = 0.100864;
  nu_joint(0.159, 0.159) = 0.504950; per-cell corner profile (cell 1: 0.158298, cell 2: 0.037311,
  cell 3: 0.016455, cells 4..32 tail 0.009269..0.000341).

## 7. Bottom line for the queue

O1: executed; outcome = **certified-with-correction**. The multi-pair theorem's "w <= 1 mod one
certified constant" clause must be re-scoped to "w <= 0.98 mod the cap (constant now
interval-certified 0.98465 < 1)"; the sliver w in (0.98, 1] moves to the
numerics-plus-backstop column (attacks re-run there: >= +17.47). O4: executed; N = 128 agrees
everywhere up to honest constant drift; two N-dependences recorded (A(ii) threshold d >= 1.1;
sliver present at both N). No edits applied to the refereed package; Section 5 above is the
complete edit list for the orchestrator's dated revision.
