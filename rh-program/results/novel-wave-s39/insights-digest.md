# Insights digest — wave 3 (Sessions 38–40, eleven units; KICKSTART 10(a)): rigidity, the line α = 2β, and integer-greedy systems

Consolidation agent (Opus 5.5), 2026-10-01, Session 41. Brief: `DIGEST-BRIEF.md` (this folder). Inputs in the brief's order: the wave-2
digest and staged zoo lines (`results/novel-wave-s37/`, the baseline: its §B B1–B10, §F ranking, UT-1 … UT-13); per unit `NOTE.md` (as
corrected by its dual read), `read-F.md` (Fable 5.1, the orchestrator), `read-O.md` (Opus 5.5); `results/lemmaB-s41/CHARTER.md` (its unit
folders not read — in flight); `directions/README.md` and the Instruments tables of B2 and C2; `digest-APPLIED.md` (what is already
applied for the five Session-39 units); `BARRIER-ZOO.md` (788 lines; the Session-40 count paragraph, I.2, I.9, I.10, I.11 only).
SHA-256 prefixes of every input: `SHARED.md` block 11. Nothing here is new mathematics unless marked `[consolidator's reading]`.

Unit folders (all under `results/`): qcond = `qcond-s38/`, conjO = `conj-O-s38/`, uoff = `u-offsurgery-s39/`, lemG = `lemmaG-s39/`,
dzh = `dz-half-s39/`, qtw = `qtwin-s39/`, fej = `fejer-form-s39/`, fgT = `free-greedy-s40/theory/`, fgC = `free-greedy-s40/compute/`,
s5m = `s5-multiplicity-s40/`, lg = `local-greedy-s40/`. "NOTE:n" = line n of that unit's NOTE.md as on disk at 16:57 IST (post-read);
"rF:n", "rO:n" = lines of its read-F.md, read-O.md.
Status labels (as the reads leave them): **THEOREM (dual-read)** = proved in the NOTE and re-derived at the line by both reads;
**(dual-read, repaired)** = the same after a FIX-FIRST repair now applied; **CONDITIONAL THEOREM** (hypothesis named); **NUMERICAL (k
producers)**; **WITHDRAWN**; **single-check** = one model only. Where read-F and read-O differ, the entry says so and names the read that
re-derives the point at the line.

## §A Per unit

### A.1 qcond — Q_cond: a Beurling system with Riemann's exact FE at conductor q > 1? Close T (stated classes, every conductor) + G
Verdicts: read-F AGREES with ONE UPGRADE (rF:5); read-O AGREES-WITH-CORRECTIONS, F1–F3 (rO:9–24). Both found the upgrade of Theorem D
independently at Meyer 1970 LNM 117 p. 25 (NOTE:3).
Three most useful findings.
1. **Theorem D** (NOTE:351–358, the complete copy; close NOTE:451–452): every DISCRETE Beurling system with Riemann's exact FE at any
   conductor q > 0 is the rational primes, q = 1. THEOREM (dual-read, upgraded to unconditional): rF:18, rO:13–15 (F1, rO:230–243).
   Remaining off-disk input: Rosenthal, Mem. AMS 63 Th. 1.6, cited inside Meyer's printed proof (NOTE:470; rO:350–352).
2. **Theorem U_q** (NOTE:228; close NOTE:440–441): the uniformly discrete class is rigid at every conductor. THEOREM (dual-read; rF:11,
   rO:10). Novelty split by read-O F2 (rO:16–19, 23–24): "new reduction … on a printed core (Hilberdink 2012 §4)", whose Thm C already
   excludes every squarefree conductor in the u.d. family.
3. **Theorem L′** (NOTE:199; close NOTE:442–444) — no ζ·(finite generalized Dirichlet polynomial) has Riemann's FE at any conductor — and
   **Corollary E2** (NOTE:178; close NOTE:445–446) — no purely continuous system does. THEOREM (dual-read; rF:9–10; rO:10). L′ "new in its
   real-frequency statement, method printed for integer divisor-supported multipliers" (rO:23–24).
Most useful failure. The finite Euler-side LP (§2.5) "could never see Π ≥ 0": the sieved identity (E) holds for every finite SIGNED sieve
(rO:344–345, R4), and on F₅ the linear Q-side constraints admit the RH-false t = ±5 (NOTE:463–465). Linear constraints are blind to positivity.
Borrow. (a) The subtraction μ′ = μ_q − (ρ_q − 1)·Lebesgue turns a self-dual measure with unit masses off 0 into Meyer's unit-mass comb
(NOTE:353–354; by-product ρ_q ∈ Z for any discrete candidate, rO:338–339). read-F subtracts ρ_q·Lebesgue and gets the comb on Λ∖{0}
(rF:18); both normalizations are valid [consolidator's check: 𝔉(cλ) = cδ₀]; the NOTE uses read-O's. (b) The Landau (Pringsheim)
obstruction on the finitely generated "q-part" of the frequencies, where ζ's pole is invisible (NOTE:447–450) — the rung-1 F2 condition
with the pole term removed (NOTE:463–465).
Statuses. U_q, L′, E1–E3, Prop. E/E′, §1.4 Cor. 1–3, §1.6, Lemma Q, Theorem D: THEOREM (dual-read; D upgraded). Lemma S–W′: read-F
`[single-check]` pending (rF:12); read-O re-derived it against S–W §4 at the page (rO:10–11) — dual-read. Novelty: E2, D, §1.6 "not found
in print (dual-checked)" (rO:24). Open residue G: weighted/mixed systems with clustering integers and infinitely many distinct masses
(NOTE:458–459, 466–469) — inherited by qtw.

### A.2 conjO — Conjecture O (relative square-root law for deletions) by the mean-square route. Close G (Lemma G) with T-parts
Verdicts: read-F AGREES, no FIX-FIRST (rF:5); read-O AGREES-WITH-CORRECTIONS, F1–F4, m1–m12, none falsifies a theorem (rO:8–18).
Three most useful findings.
1. **Theorem Z (RH)** (NOTE:24–25; close NOTE:312–313): if the prime zeta function P_R continues with finite order past α_R/2 off the
   real axis, then β₂(R) ≥ α_R/2. CONDITIONAL THEOREM (RH), dual-read: rF:11 (Z1–Z5 step by step), rO:8–9 ("re-derived at the line …
   NEW"). The device: Hilberdink's order-zero passage, the logarithm with Borel–Carathéodory (NOTE:24; m10, rO:306).
2. **Corollary Z.1 (RH)** (NOTE:313–315): every regular deletion, every c — "read-O's corner A8 is closed as a refutation corner".
   CONDITIONAL THEOREM (RH), dual-read (rF:13; rO:9–10); its c = 1 analytic input is already BDR §5 (m11, rO:307).
3. **Proposition O1** (read-O's addition, rO:312–324; recorded NOTE:342): β₂(R) ≥ α_R(1 − α_R)/4 for EVERY R with Σ1/p < ∞, α_R < 1,
   unconditionally. single-check (read-O proved it; the orchestrator recorded it, NOTE:342). Its ceiling is α_R/4, the same as Prop. 1.3
   (RH; β₂ ≥ α_R/4, dual-read, rF:9, rO:12), because both see only the resolved denominators b ≤ √X (rO:327–331).
Most useful failure. Remark 1.3′ (NOTE:316–317): the brief's gap lemma — a mean value for a function known only as analytic of finite
order in a strip — is false (η(2s)); "no mean-value theorem driven by growth alone reaches α/2" (m3, rO:299). Second: the task-3 trigger
could not separate a counterexample from a log-power (NOTE:330–331) — the greedy sets fall below X^{α−δ} in pure-power slope while β₂ ≥ α/2
is proved for them (NOTE:327–328; F4, rO:287–293).
Borrow. (a) Logarithm + Borel–Carathéodory converts polynomial growth into order zero (the repair of the Carlson obstruction, NOTE:31).
(b) The κ-calibrated stop trigger: "below X^{α_R−δ} over three decades AND M/M_diag not fitted by a log-power κ ≤ 4" (rF:18, m3).
(c) The resolved/unresolved split: every route stops at α_R/4 until the incomplete-period Franel pairs (b, b′ ∈ (√X, X]) are handled
(rO:329–331, 338–341).
Statuses. Prop. 1.1 (corrected by the coprimality factor (1 − p^{2σ−2})): dual-read (rF:8, independent mpmath check; rO:11–12, F1 adds the
b = 1 frequencies). Lemma G: under RH EQUIVALENT to O₂ set by set — a reformulation, not a weaker input (F2, rO:266–273; NOTE:311). The
α = 0.75 data: NUMERICAL (2 producers) — sup tension resolved (12 seeds 0.392 ± 0.016; read-O's 8 independent seeds 0.399 ± 0.011),
top-window mean square UNDECIDED between α and 2/(3 − α) (20 seeds 0.816 ± 0.039; NOTE:326–327). Disagreement: read-F accepted the
12-seed resolution "at the report level" (rF:12); read-O re-ran it with its own code and RNG and found the mean-square half undecided
(rO:275–277, F3) — read-O re-derives the point. The "any A" addition clause: HEURISTIC, flagged for amendment (NOTE:323–324; rF m2).
