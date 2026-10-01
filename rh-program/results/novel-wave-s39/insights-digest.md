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

### A.3 uoff — Conjecture U off the surgery class: the integer-greedy systems S5(ρ). Close CHANGED at the dual read: K-conditional + T + G
Verdicts: read-F AGREES on every finite fact and on K′ as a conditional, DISAGREES with the close's weight, F1–F2 (rF:5); read-O DISAGREES
with the close as stated — "the theorems stand, the numerical crossing does not", F1–F14 (rO:7). The two reads agree (rF §7); NOTE:13.
Three most useful findings.
1. **The multiplicity mechanism (the burst inequality).** At ρ = 0.8 the late records of E are single integers of high multiplicity
   (n = 902538000 has a_n = 276; E jumps from −0.4 to 274.8), so sup_{u≤x}E ≥ max_{n≤x}a_n − 1.3 and β ≥ limsup log a_n/log n (rF C1–C2;
   rO A2, :234). Refused rational primes enter only through composite "carriers" (20, 30, 110, … for 5), and integers divisible by a refused
   prime and many carrier cofactors have many factorizations. Dual-read (two independent generators, exact counts).
2. **Rigorous lower bounds beyond the computed range.** The factorizations of n into the g-primes ≤ 10⁹ bound a_n below forever (later
   g-primes only add) (rF C3): a_n ≥ 13,461,378,553 at n₃ (exponent 0.3327 at 10^{30.45}) and ≥ 7,047,237,674,851 at 10^{37.86} (0.3394,
   local 0.367) (rO A3–A4, :235–236). Dual-read; carried to n_K in s5m (A.10).
3. **§3.2 and §3.3 (T).** Tracking discretizations of rational templates have β ≥ ½ (a corollary of Hilberdink 2005 Remark C, rF:12;
   "new as a statement on a printed core", rO §6); periodic designs are abelian number fields or cross U only through an off-line
   Dirichlet zero (§3.3(b), rF:13). THEOREM (dual-read; read-O: "correct, each with a one-line gap", rO:7).
Most useful failure. The numerical crossing of U's line by S5(0.8) — "β ≈ 0.30 over six decades" — is WITHDRAWN (NOTE:13): 0.30 was the
slope of the running sup on [10³, 10⁹], a pre-asymptotic transient; the crossing needs β < Re ρ₁/2 ≈ 0.383 (rO A8, :238) and is
undetermined. The fitted exponent of a greedy system is not evidence until the multiplicity growth beyond the range is bounded.
Borrow. (a) The exact lower-bound ascent as the standard test of any "integer exponent" of a feedback system. (b) read-O A5 (:237):
ρ-dependence — exact ascents stay flat near 0.27 (ρ = 0.95, to 10^{38.8}) and 0.285 (ρ = 1.05, to 10^{40.8}); the smallest refused prime
(5, 13, 23) is what compounds, so "a variant that never refuses small primes" is the better β-candidate (the seed of lg's S7). (c) A6
(Rankin): over y-smooth n ≤ x, max a_n = x^{o(1)} — power growth of multiplicity needs records with growing prime support (rO:239).
Statuses. Theorem K′ (NOTE:169–172): CONDITIONAL THEOREM (on H_θ and the floating-point box evaluation), dual-read; the zero ρ₁ =
0.7658722 + 30.3260650i, NUMERICAL (3 producers: writer, read-F, read-O), floating point only (rO §8). H_θ: false for θ ≤ 0.3227 (rO A3)
and — since s5m's n_K — false for every θ ≤ 0.35 with any constant below 1.88, so for K′'s stated constant 1 (s5m NOTE:15, 101; rF §7):
K′ is a correct theorem with a false hypothesis. Record lag: NOTE:22 still reads "at exponent 0.35 unrefuted and unsupported" (§E).
Lemma H in its ≪ form: not refuted, unsupported (s5m NOTE:103). Novelty: S5 "new (single-check)" — no printed feedback construction in
22 arXiv queries; nearest Olofsson 2010, Lagarias 1999 (rO §6).

### A.4 lemG — Lemma G on deterministic irregular classes; the rung-1 test. Close G with T-parts and a rung-1 counterexample
Verdicts: read-F AGREES, no FIX-FIRST (rF:5); read-O AGREES-WITH-CORRECTIONS, F1–F5 (14 FIX-FIRST pairs) + 17 minor (rO:11–27). read-F's
reconciliation: "the reader's F1 and F2 are real and were MISSED here" (rF §4) — read-O re-derives both at the line.
Three most useful findings.
1. **Theorem R1 — Conjecture O is FALSE at the function-field rung** (NOTE:24–26; close NOTE:339–341): deleting M(a, N) irreducibles of
   each degree N from F_q[T] gives D_R = 1 − au, E ≡ 0, α_R = log a/log q, and the deletion satisfies every input of Theorem Z's proof
   except zero-freeness of D_R — so "a proof must use the injectivity of the norm on ⟨R⟩" (NOTE:345–346). THEOREM (dual-read): brute force
   by read-F in three cases (rF:8–9) and by read-O over all monic polynomials of F₃, F₅, F₇, 15 cases (rO:12–13). Novelty: "new as a
   statement on a printed core" (rO §6; the Q-side rigidity is Hilberdink 2012 Thm A, F5).
2. **Theorem 2.1 / Corollary 2.2 — the singularity criterion** (close NOTE:332–337): right of β₂ the singularities of P_R are exactly
   −κ log(s − s₀) + analytic with κ = Σμ(m)ord_{ms₀}D_R/m; any other singularity at Re s₀ forces β₂ ≥ Re s₀. It proves O unconditionally on
   four deterministic classes irregular at scale x^{α_R/2}: T2, T3, T4 (natural boundary on σ = α_R/2), T5. THEOREM (dual-read; Cor. 2.2
   with the path restriction {σ ≥ Re s₀}, F3; T2 and T5 repaired, F1–F2).
3. **The cluster criterion** (read-O A1–A2, rO:363–380): the tight ℚ-necklace obeys O UNCONDITIONALLY (β = α_R = ½, β₂ ≥ ¼) by Selberg's
   upper-bound sieve — dual-read (read-O proved; the orchestrator re-derived it before applying, rF §4 F4); and in general "counterexamples
   to O must be anti-clustered": #R ∩ (y, y + h] ≤ 2(2y)^{α/2+δ} + C h y^{α−1+δ} + C h^{2α/(1+α)+δ} if β(R) < α_R/2 — single-check (A2).
Most useful failure. The natural-boundary route for hash-defined / pseudo-random R is blocked by a named missing input: every
natural-boundary theorem read at the page needs gaps, shift structure, independence or one local factor per prime; for the Weyl family the
input is a bilinear equidistribution estimate for {pθ} at scale p^{α−1} (NOTE:357–363). And the brief's dichotomy "P_R continues past
α_R/2, or has a natural boundary there" is not one: T2's R_k and the tight necklace have neither, and O holds for both (NOTE:352–355).
Borrow. (a) The sq family {nextprime(p²)} as a second calibration of the stop trigger beside conjO's κ: sub-diagonal slope 0.422 on
[10⁶, 10¹⁰] on a set where O is a theorem (under RH, F1), with E the sum over ζ's zeros at ρ/2 (200-zero explicit formula, correlation
0.998 for x ≥ 10⁸; rO:21–24 reproduces 0.882/0.980/0.998). (b) The rung-1 necklace as a control for any argument that consumes only
Theorem Z's inputs. (c) A2 as a cheap first filter on any proposed counterexample to O.
Statuses. R1, Thm 2.1, Cor. 2.2, Prop. 2.3, T3, T4: THEOREM (dual-read). T2: THEOREM (dual-read, repaired) — for sq only under RH or a
recalled large-gap bound, "not 'uncond.' as the NOTE says four times" (F1, rO:16–18; A4). T5: THEOREM (dual-read, repaired by a greedy
choice, F2). Theorem F: CONDITIONAL THEOREM (RH), dual-read (read-F "structure only", rF:5; read-O re-derived); Cor. F.1 superseded by
A1. 𝒞_self: definitional — "a tautology, not an obstruction theorem" (NOTE:342–343). Computation to 10¹⁰: NUMERICAL (2 producers, digit
for digit), no K-candidate (NOTE:356–357).

### A.5 dzh — Diamond–Zhang's random Beurling systems have β = ½ almost surely (BDR fn. 4). Close T
Verdicts: read-F AGREES, no FIX-FIRST (rF:5); read-O AGREES-WITH-CORRECTIONS, F1–F2 record-level + 7 minor (rO:15–28); applied (NOTE:11).
Three most useful findings.
1. **Theorem 1 / Corollary 2** (NOTE:13–21): for almost every realization of DZ Thm 17.14, lim sup |N_B(x) − k₂x|/(x/log x)^{1/2} > 0, so
   "β₀ = ½ and P_B is a [1, ½]-system" (NOTE:18), and Thm 17.11's P_R is a [½, ½]-system (Cor. 2.6). THEOREM (dual-read; rF:9–13; rO:15–19
   "valid"). Novelty: "new — answers BDR fn. 4 and DZ p. 196 (θ < ½) for a.e. realization" (rO §6); not settled in print (dual-checked).
2. **The one-scale method** (NOTE:23–27): the dependence across (x/2, x] is exact and one-dimensional — every g-integer ≤ x holds at most
   one block prime (Lemma 2.1) — so conditional Gaussian anti-concentration at a single scale gives the a.s. statement "with no
   independence across scales and no 0–1 law" (rF:9, the point the brief asked to press; rO:17–18, the Fatou bound, A3).
3. **Addition A1** (rO:300–315): a.s. lim sup |N − ρx|/(x/log x)^{1/2} = +∞ and (A1′, one-sided) lim inf = −∞ — single-check; it answers
   the NOTE's U-2. What it does not reach (A2): θ = ½, "is N − ρx = O(x^{1/2})?" — the Mellin route cannot decide it.
Most useful failure. The NOTE's own limits (NOTE:39–41): nothing about the exceptional null set — a particular subsequence of the grid
satisfying DZ's (17.46) with β < ½ is not excluded, "that is Conjecture U at α = 1 in DZ's class" (U-1). Random selection lands EXACTLY on
U's boundary α = 2β (β = ½ at α = 1), so it is consistent with U and cannot test it. Record-level: a quoted 10⁻⁶ gap was a quadrature
artifact (F1, rO:235–242).
Borrow. (a) The one-block decomposition plus conditional anti-concentration, for any random discretization whose dependence is confined to
one dyadic block (the device that s5m/fgT need for their random controls). (b) The deterministic grid P_det: β ≥ ½ from the
(2s − 1)^{−1/2} branch point of the prime squares, constant −0.5998 predicted and −0.5995 measured (NOTE:35–37, 43–44) — a known-answer
control for integer-error estimators. (c) F2's reading of Remark 17.12 (the book's normalization may add an infinite O(log x)-sparse
sequence; Theorem 1 covers it, rO:244–252).
Statuses. Theorem 1, Cor. 2, Prop. 2.4, Cor. 2.6: THEOREM (dual-read). Lemma 2.5: dual-read, "not new" (rO §6). A1, A1′: single-check
(A1′ uses a recalled Landau/Widder theorem). Finite rung (X = 10⁸, five seeds; read-O at 10⁷): NUMERICAL (2 producers) — sup-slopes 0.492 ±
0.012 (P_R), 0.479 ± 0.020 (P_B) (NOTE:31–33); read-O 0.496 ± 0.022 / 0.485 ± 0.026 (rO:24–26). Remark 5.1 (Broucke Thm 1.6 systems exact
[1, ½]): conditional on an unchecked template property (U-3).
