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
   real axis, then β₂(R) ≥ α_R/2. CONDITIONAL THEOREM (RH), dual-read: rF:12 (Z1–Z5 step by step), rO:8–9 ("re-derived at the line …
   NEW"). The device: Hilberdink's order-zero passage, the logarithm with Borel–Carathéodory (NOTE:24; m10, rO:306).
2. **Corollary Z.1 (RH)** (NOTE:313–315): every regular deletion, every c — "read-O's corner A8 is closed as a refutation corner".
   CONDITIONAL THEOREM (RH), dual-read (rF:14; rO:9–10); its c = 1 analytic input is already BDR §5 (m11, rO:307).
3. **Proposition O1** (read-O's addition, rO:312–324; recorded NOTE:342): β₂(R) ≥ α_R(1 − α_R)/4 for EVERY R with Σ1/p < ∞, α_R < 1,
   unconditionally. single-check (read-O proved it; the orchestrator recorded it, NOTE:342). Its ceiling is α_R/4, the same as Prop. 1.3
   (RH; β₂ ≥ α_R/4, dual-read, rF:10, rO:12), because both see only the resolved denominators b ≤ √X (rO:327–331).
Most useful failure. Remark 1.3′ (NOTE:316–317): the brief's gap lemma — a mean value for a function known only as analytic of finite
order in a strip — is false (η(2s)); "no mean-value theorem driven by growth alone reaches α/2" (m3, rO:299). Second: the task-3 trigger
could not separate a counterexample from a log-power (NOTE:330–331) — the greedy sets fall below X^{α−δ} in pure-power slope while β₂ ≥ α/2
is proved for them (NOTE:327–328; F4, rO:287–293).
Borrow. (a) Logarithm + Borel–Carathéodory converts polynomial growth into order zero (the repair of the Carlson obstruction, NOTE:31).
(b) The κ-calibrated stop trigger: "below X^{α_R−δ} over three decades AND M/M_diag not fitted by a log-power κ ≤ 4" (rF:21, m3).
(c) The resolved/unresolved split: every route stops at α_R/4 until the incomplete-period Franel pairs (b, b′ ∈ (√X, X]) are handled
(rO:329–331, 338–341).
Statuses. Prop. 1.1 (corrected by the coprimality factor (1 − p^{2σ−2})): dual-read (rF:8, independent mpmath check; rO:11–12, F1 adds the
b = 1 frequencies). Lemma G: under RH EQUIVALENT to O₂ set by set — a reformulation, not a weaker input (F2, rO:266–273; NOTE:311). The
α = 0.75 data: NUMERICAL (2 producers) — sup tension resolved (12 seeds 0.392 ± 0.016; read-O's 8 independent seeds 0.399 ± 0.011),
top-window mean square UNDECIDED between α and 2/(3 − α) (20 seeds 0.816 ± 0.039; NOTE:326–327). Disagreement: read-F accepted the
12-seed resolution "at the report level" (rF:16); read-O re-ran it with its own code and RNG and found the mean-square half undecided
(rO:275–277, F3) — read-O re-derives the point. The "any A" addition clause: HEURISTIC, flagged for amendment (NOTE:323–324; rF m2).

### A.3 uoff — Conjecture U off the surgery class: the integer-greedy systems S5(ρ). Close CHANGED at the dual read: K-conditional + T + G
Verdicts: read-F AGREES on every finite fact and on K′ as a conditional, DISAGREES with the close's weight, F1–F2 (rF:5); read-O DISAGREES
with the close as stated — "the theorems stand, the numerical crossing does not", F1–F14 (rO:7). The two reads agree (rF §7); NOTE:13.
Three most useful findings.
1. **The multiplicity mechanism (the burst inequality).** At ρ = 0.8 the late records of E are single integers of high multiplicity
   (n = 902538000 has a_n = 276; E jumps from −0.4 to 274.8), so sup_{u≤x}E ≥ max_{n≤x}a_n − 1.3 and β ≥ limsup log a_n/log n (rF C1–C2;
   rO A2, :235). Refused rational primes enter only through composite "carriers" (20, 30, 110, … for 5), and integers divisible by a refused
   prime and many carrier cofactors have many factorizations. Dual-read (two independent generators, exact counts).
2. **Rigorous lower bounds beyond the computed range.** The factorizations of n into the g-primes ≤ 10⁹ bound a_n below forever (later
   g-primes only add) (rF C3): a_n ≥ 13,461,378,553 at n₃ (exponent 0.3327 at 10^{30.45}) and ≥ 7,047,237,674,851 at 10^{37.86} (0.3394,
   local 0.367) (rO A3–A4, :236–237). Dual-read; carried to n_K in s5m (A.10).
3. **§3.2 and §3.3 (T).** Tracking discretizations of rational templates have β ≥ ½ (a corollary of Hilberdink 2005 Remark C, rF:10;
   "new as a statement on a printed core", rO §6); periodic designs are abelian number fields or cross U only through an off-line
   Dirichlet zero (§3.3(b), rF:11). THEOREM (dual-read; read-O: "correct, each with a one-line gap", rO:7).
Most useful failure. The numerical crossing of U's line by S5(0.8) — "β ≈ 0.30 over six decades" — is WITHDRAWN (NOTE:13): 0.30 was the
slope of the running sup on [10³, 10⁹], a pre-asymptotic transient; the crossing needs β < Re ρ₁/2 ≈ 0.383 (rO A8, :241) and is
undetermined. The fitted exponent of a greedy system is not evidence until the multiplicity growth beyond the range is bounded.
Borrow. (a) The exact lower-bound ascent as the standard test of any "integer exponent" of a feedback system. (b) read-O A5 (:238):
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
Verdicts: read-F AGREES, no FIX-FIRST (rF:5); read-O AGREES-WITH-CORRECTIONS, F1–F5 (14 FIX-FIRST pairs) + 17 minor (rO:12–28). read-F's
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
3. **The cluster criterion** (read-O A1–A2, rO:365–382): the tight ℚ-necklace obeys O UNCONDITIONALLY (β = α_R = ½, β₂ ≥ ¼) by Selberg's
   upper-bound sieve — dual-read (read-O proved; the orchestrator re-derived it before applying, rF §4 F4); and in general "counterexamples
   to O must be anti-clustered": #R ∩ (y, y + h] ≤ 2(2y)^{α/2+δ} + C h y^{α−1+δ} + C h^{2α/(1+α)+δ} if β(R) < α_R/2 — single-check (A2).
Most useful failure. The natural-boundary route for hash-defined / pseudo-random R is blocked by a named missing input: every
natural-boundary theorem read at the page needs gaps, shift structure, independence or one local factor per prime; for the Weyl family the
input is a bilinear equidistribution estimate for {pθ} at scale p^{α−1} (NOTE:357–363). And the brief's dichotomy "P_R continues past
α_R/2, or has a natural boundary there" is not one: T2's R_k and the tight necklace have neither, and O holds for both (NOTE:352–355).
Borrow. (a) The sq family {nextprime(p²)} as a second calibration of the stop trigger beside conjO's κ: sub-diagonal slope 0.422 on
[10⁶, 10¹⁰] on a set where O is a theorem (under RH, F1), with E the sum over ζ's zeros at ρ/2 (200-zero explicit formula, correlation
0.998 for x ≥ 10⁸; rO:22–23 reproduces 0.882/0.980/0.998). (b) The rung-1 necklace as a control for any argument that consumes only
Theorem Z's inputs. (c) A2 as a cheap first filter on any proposed counterexample to O.
Statuses. R1, Thm 2.1, Cor. 2.2, Prop. 2.3, T3, T4: THEOREM (dual-read). T2: THEOREM (dual-read, repaired) — for sq only under RH or a
recalled large-gap bound, "not 'uncond.' as the NOTE says four times" (F1, rO:17–19; A4). T5: THEOREM (dual-read, repaired by a greedy
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
   independence across scales and no 0–1 law" (rF:11, the point the brief asked to press; rO:17–18, the Fatou bound, A3).
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

### A.6 qtw — Q_cond's last corner: weighted, clustering systems with Riemann's exact FE at q > 1. Close G stated as a theorem; no construction
Verdicts: read-F AGREES, no FIX-FIRST (rF:5); read-O AGREES-WITH-CORRECTIONS, F1–F6 + 10 minor (rO:13–26); reconciled (rF §5).
Three most useful findings.
1. **Theorem G1** (NOTE:128; close NOTE:53): a finite generalized Dirac comb with ANY weights is rigid — μ_q is never one at q > 1; with
   Cor. G1′ (purely atomic, finitely many mass values) (NOTE:153). THEOREM (dual-read; rF:8, Step 3 the new step; rO §6 "NEW as a
   statement … re-derived ✓ → dual-checked"). read-O's control A6 (rO:337–341): a positive, self-dual, gapped comb with an irrational
   frequency, μ_c = Σ(2 + 2cos2πθn)δ_n + δ_{θ+Z} + δ_{−θ+Z}, θ = √2 − 1 — G1's Step 3 is not vacuous (single-check).
2. **Theorem L‴ with Proposition S** (NOTE:203, 269, 280; close NOTE:55–57): if F/ζ converges absolutely on some Re s > σ₀ < ½, the
   rational primes in the group of its atoms have abscissa σ_S ≥ ½ — the whole Poisson-pair cone 𝒦_r with thin atoms, continuous parts
   included. THEOREM (dual-read; rF:10; rO §6 "NEW in its infinite-atom / real-frequency / continuous-part statement"; the finite-S
   mechanism is printed, Hilberdink 2012 Thm 4.3, F2).
3. **The class 𝒯 and its one-condition reduction** (NOTE:67–69): m ≥ 0 atomic on [1, q], m({1}) = 1, J-symmetric, atom group with
   σ_S ≥ ½ — the exact FE, self-duality, dN ≥ 0 and the gap hold automatically, and Q_cond on 𝒯 ⟺ Π_ζ + log*(m) ≥ 0. Dual-read (rF:11;
   rO §6). read-O A2 (rO:306–314, single-check): a member of 𝒯 with Π ≥ 0 has D zero-free on Re s ≥ 1 and Re s ≤ 0 (Mertens
   3-4-1), with every zero of D_a ON Re s = ½ when σ_S = ½ exactly — a necessary condition any construction must meet.
Most useful failure. The 𝒯 probe (q = 4, window [1, 64]): the max-min of Π_F rises −0.680, −0.401, ≥ −0.294, ≥ −0.219, ≥ −0.185 as atom
pairs are added, while a third to a half of the atoms stay negative and the M = 4 optimum falls to −1.129 on [1, 256] (rO A5,
:327–336); every finite design is excluded anyway, by L′ and by Hilberdink 2012 Prop. 3.4 without the FE (A4, rO:321–326) — "evidence
of nothing about 𝒯" (NOTE:73). Also F6: §5.2's mechanism (b) was a heuristic labeled (P); smooth self-dual weights vanishing on Z_j exist
(KNS Lemma 6), so §0.4(3)'s exclusion is downgraded to the families of the §7.1 table (rF §5 F6).
Borrow. (a) Hilberdink 2012 Prop. 3.4 as a free certificate: any ζ·D with finite rational atoms, m ≥ 0 and a non-integer atom is not a
weighted Beurling system — no FE needed (A4); only limit-periodic N − D(1)x escapes (the C2 Untried draft (b), already applied).
(b) The Mertens 3-4-1 inequality to push zeros of a Beurling multiplier off Re s = 1 (A2). (c) G1's Poisson step for modulated combs
against finitely many Q-lines.
Statuses. G1, G1′, Lemma A, Prop. S, L‴ (both forms), the 𝒯 reduction: THEOREM (dual-read). Lemma M, Cor. M1 and Theorem D
unconditional: NOT NEW — first proved in qcond's dual read (F1, credit; rF §5 F1 confirms from the Session-39 LOG); Cor. M1 corrected by
"μ̂ purely atomic" (F4: μ = δ₀ has μ̂ = Lebesgue). (W1) weighted rung 1 = [−5, 6]: exact for d ≤ 60 (two producers), all d by read-O A1
(single-check). (W3): in print (Hilberdink 2012 Thm 4.4). Probe values: NUMERICAL (2 producers to M = 3; read-O alone M = 4–6, F3).

### A.7 fej — the Fejér defect as a positive form transported to the zeros (UT-4). Close K: "found nothing new, correctly"
Verdicts: read-F AGREES, no FIX-FIRST (rF:5); read-O AGREES-WITH-CORRECTIONS, F1–F2 on the close's wording + 9 minor (rO:14–28); the
label "found nothing new, correctly" UPHELD (rO §6). read-F had accepted the wording; it verified F1–F2 by hand before applying (rF §5).
Three most useful findings.
1. **Theorem K** (NOTE:258–276): no form of the Fejér defect built here is a positivity generator outside Weil's cone — "its POSITIONS form
   is positive for free and blind, its ZEROS form is RH-sensitive and is Weil's functional, and the explicit formula maps one to the
   other" (NOTE:273–275). THEOREM (dual-read; rO:14–16 "none is false as stated"); "packaging … no new mathematics" (rO §6).
2. **Theorem F** (NOTE:146; close NOTE:24–27): M1a's Fejér defect on q^Z is D_k = h(q^{g−1+k} − 1) (AHL Lemma 3.4); D_1 vanishes exactly
   at genus 0 and is > 0 on every datum of genus ≥ 1, V included (D_1(V) = 4): "V sits at h = 1, the extreme point of free positivity,
   strictly below the RH floor (√5 − 1)² = 1.528" (NOTE:27). Dual-read (in the D_1-only form, F1; rF §5). In print (AHL).
3. **Theorem W** (NOTE:90; close NOTE:18–22): every affine functional in (g, N_1, …, N_M) vanishing at genus 0 is the Weil functional
   Σ_j f(θ_j); separators from the Weil region are exactly the Toeplitz cone (= Hallouin–Perret's Gram cone on X × X); separators from the
   genuine integer data alone form the larger class (B), Weil + integrality (F2). Dual-read; "in print as a statement on a printed core"
   (rO §6: HP 1409.2357, HPM).
Most useful failure. The literal transport is V-blind (K(iii)), and the Z-forms split the same way: Z1 (M1a's (C_Q)) and Z2 are passed by
F_{2.9,2}, DH and Epstein x² + 5y² (RH-blind); Z3 is violated by F_{2.9,2} (−872.45) and DH (−681.66) and is Weil's criterion (NOTE:30–34).
UT-4 is CLOSED (NOTE:39); stop line 2 fired (the best inequality is a printed Weil/Weil–Serre bound).
Borrow. (a) Before funding any "positive form" proposal, evaluate it on V: a form whose positivity is dN ≥ 0 is V-blind by Theorem F
(D_1(V) = 4 > 0). (b) read-O A1 (rO:292–305, single-check): over F₅, 17g/4 + N_1 − 6 separates V (−3/4), is not a Weil test, and at
g = 1 has an RH-free proof through a Weierstrass model — an OBJECT V lacks (proof-mine's class C) — but it is the integrality boundary,
does not extend in q and has no Z-analog. (c) A5: exact certificates through HPM's integer Gram matrix H_M (all 3825 exits, 766 PSD
statements, no rounding).
Statuses. W, F, K and the Clifford claims: THEOREM (dual-read), no new mathematics. Census (4591 data, the 111, 115 + 192 genuine L-
polynomials), I(V) = −0.1180339887, I(E₀) = +0.1055728090, Z3 values: NUMERICAL (2 producers, rO:16–19). A1, A2 (class-(B) window for
non-square q ≤ 13), A3 (λ_min(T_M(V)) in Lucas/Fibonacci closed form): single-check. The two zoo riders of §11 (on IV.1 and I.9): accurate
after F1, F2e, m9 (rO:27–28) — already entered at the Session-40 zoo stream (BARRIER-ZOO.md:153, the I.9 rider; :443, the IV.1
rider); not restaged here.

### A.8 fgT — S8, the free greedy system: identities, mechanism, proof problem. Close T + G (Lemma B_ρ)
Verdicts: read-F (partial Session 40, Theorem 1.6 only; completed Session 41 "BEFORE the Opus read-O was opened") AGREES-WITH-CORRECTIONS
(rF:3–9, 16–35); read-O AGREES-WITH-CORRECTIONS, F1–F3 + 13 minor, 27 pairs (rO:11–27). All 27 pairs applied (rF:35).
Three most useful findings.
1. **Theorem 1.6 — one-sided integer regularity forces a real zero** (NOTE:103; §0 NOTE:11–14): if N(u) − ρu ≥ r₀ > 0 for all u ≥ 1 and
   N − ρu = O(u^θ), θ < r₀/(r₀ + ρ), then ζ_P has a real zero σ* ∈ [r₀/(r₀ + ρ), 1) and α ≥ σ*. THEOREM (dual-read; rF:5–8, rO:13–16).
   It uses discreteness nowhere (rF:7, 9; rO A1, :372–374: valid for every Beurling system; for discrete systems the zero is strictly
   right of r₀/(r₀ + ρ)); the template dN = δ₁ + ρdx shows it is sharp (rF:9). Novelty: "new as a statement on a printed core"
   (Bateman–Grosswald 1964 p. 367; Phragmén, as in Révész 2023) (rO:221–224; rF:35).
2. **Corollary 1.7 and the Dichotomy** (NOTE:113, 208; §0 NOTE:14–18): S8's rule gives r₀ = ½ − ρ for free (E > −½), so for ρ < ¼
   "Conjecture U is false as soon as S8(ρ) has N(x) − ρx = O(x^θ) for some θ ≤ ½ − ρ"; with the finite certificates (F_{10⁷}(0.79) =
   +0.0222 for π/16, F_{10⁶}(0.89) = +0.0434 for π/32) the needed exponent relaxes to θ < 0.395 and θ < 0.445. THEOREM (dual-read;
   rO:16–19 "correct as stated"). Conjecture U for never-undershooting systems is thereby ONE integer bound: Lemma B_ρ (NOTE:25), G.
3. **Prop. 2.1, the gap identity** (NOTE:143): E = ½ + composites − ρ·elapsed on every g-prime gap, so E ≤ ρ·(largest gap) − ½. Dual-read.
   read-F adds the Lindley form (proved there, not in the NOTE): e_k = max(e_{k−1} + c_k − 1, 0) — "S8 is a single-server queue, one
   service per lattice step, fed by composites; the g-primes are its idle steps" (rF:22; single-check).
Most useful failure. **The two-sided sieve form of Lemma B_ρ is false** (read-O F1, rO:19–21; NOTE:26): square-root cancellation in the
Legendre remainder S(I) would force ψ_P ~ 2e^{−γ}x through the Beurling Mertens theorem (Diamond–Zhang Thm 5.10, read at the page);
S(u, 2u] carries the bias (1 − 2e^{−γ} + o(1))u/log u, 12.3 % of the prime count (A3, rO:379–381). read-F upheld it: "I had not seen this
in my own read" (rF:26) — read-O re-derives the point. Also: routes (a) and (b) break at the compensator (a short-interval PNT), and
randomization is counterproductive (offsets of width 50 raise sup E at 10⁷ from 12.8 to 58–171; NOTE:27–30).
Borrow. (a) Theorem 1.6 as a Siegel-zero test for any positive-coefficient zeta with a residue (UT-F5); its contrapositive A2 (rO:375–
378): no real zero in (θ, 1) and O(u^θ) give inf(N − ρu) ≤ ρθ/(1 − θ). (b) The bias A3: any probabilistic model of S(I) must be centered
on (1 − 2e^{−γ})u/log u. (c) read-F's price of B_ρ (rF:31–32, single-check): by Prop. 2.1, B_ρ has the strength of a g-prime gap bound
x^θ, θ < ½ − ρ; a zero-density estimate N(σ, T) ≪ T^{A(1−σ)} gives gaps x^{1−1/A+ε}, so no zero-density bootstrap reaches B_ρ for S8 as it
stands — "this is why the stream lemmaB-s41 carries two design units".
Statuses. Lemmas 1.0–1.5, Theorem 1.6, Remark 1.6′, Cor. 1.7, Prop. 2.1, the Legendre form, the Dichotomy, Theorems 4.1–4.2: THEOREM
(dual-read). Certificates: NUMERICAL (2 producers; read-O double-double with a 60-digit recheck of every close decision, rO:17–19); the
stated ordering margins were 9–21× too large (F2) and survive. "sup E ≈ (0.20–0.37)·ρ·log²x" (F3, corrected from 0.37–0.53). Lemma B_ρ:
NOT proved (G). Label lag: NOTE:11 and :103 still read "[novelty: single-check — not found in print]" (§E).

### A.9 fgC — S8 at scale: the integer error and the zeros, to 10¹¹. Close: a numerical record (nothing proved, as the NOTE says)
Verdicts: read-F AGREES-WITH-CORRECTIONS (rF:3); read-O AGREES-WITH-CORRECTIONS, F1–F2 (5 pairs) + 7 minor (rO:11). 12/12 pairs applied
(rF:16–17). "Unit CLOSED DUAL-READ as a numerical record: two producers to 10¹⁰ (10¹¹ single producer)" (rF:17).
Three most useful findings.
1. **The law of E for S8(π/4)** (NOTE:11): sup_{u≤x}E = 8.22, 13.33, 26.63, 39.53, 47.86, 95.86, 95.86, 113.20, 123.62 at 10³ … 10¹¹;
   best two-parameter description ≈ 0.2·log²x; sup E/x^{1/4} falls 1.25 → 0.22 over 10⁶–10¹¹, so β < ¼ on the observed range (F2 wording).
   NUMERICAL: three producers to 10⁷ (unit, the orchestrator's prototype, rF:6), two to 10¹⁰ (read-O's 128-bit generator with a
   per-decision ordering proof, rO A1, :189), one at 10¹¹. read-O A5 (:197, heuristic): "sup E ≈ c·log²x" and "E = O(log x) in
   distribution" are one statement, and the second is the stronger evidence.
2. **The zero ρ₁ = 0.8962124913 + 14.5499355887i of F_X** (NOTE:13–27): stable to 10 digits, the only zero with σ > 0.85 up to
   t = 5000; it is a zero of ζ_P "provided |E(u)| ≤ 39,928·log²u for all u > 10¹¹" (Rouché; NOTE:28), and from the proved range alone
   provided |E(u)| ≤ 6531·log²u beyond 10¹⁰ (rO A2, :191); observed max E/log²u = 0.307. The explicit formula over 44 zeros + the real
   zero 0.51474 reproduces ψ_P − x on [10⁴, 10¹¹] to 0.2 % rms: α(S8(π/4)) = 0.8962 numerically. NUMERICAL (2 producers to 10¹⁰;
   B_max 40,028 by read-O's second route; read-F's crude form gives 35,144 — "Either way the margin … five orders of magnitude", rF:8).
3. **Small densities** (NOTE:30): S8(π/16), S8(π/32) to 10¹¹ have sup E = 33.27, 20.36 (≈ 0.05, 0.03·log²x) and rightmost zeros REAL at
   0.7947553732, 0.8950765177 (read-O 0.7947553701, 0.8950765176 at 10¹⁰) — fgT's Theorem 1.6 regime. NUMERICAL (2 producers to 10¹⁰).
Most useful failure. The claims beyond the data (read-O F1–F2, rO:123–143): the event ordering was called "certified" on an asserted
double-double error the code never bounds (now proved to 10¹⁰ by read-O's generator, 0 flags), and "β = 0 numerically; no power law
fits" overstated nine correlated running-maximum points (b = 0.145 fits with rms 0.21; the last three decades grew more slowly than
log²x). Waste: the first zero scan ran its box edge through the real zero 0.5147 (NaN; NOTE:49).
Borrow. (a) read-O's rigorous generator `compute/verify-O/s8o.cpp` (128-bit fixed point, per-decision ordering proof; A1) as the
reference for every later S8 run. (b) A3 (:193): a rigorous bound on |F_X′| certifies the winding without a sampled derivative (min|F|
≥ 0.1076 on the box). (c) A4 (:195): the √2-lattice is not free (L₄L₂₀L₂₃ = L₆²L₅₁) — free-monoid claims need transcendence of 1/ρ.
Consistency note [consolidator's check]: fgC's "θ ≤ 0.304 (π/16), 0.402 (π/32)" (NOTE:30) is Cor. 1.7's floor ½ − ρ; fgT's "θ < 0.395,
0.445" uses the finite certificates (fgT NOTE:16). Both correct; they answer different hypotheses.
Statuses. Every number: NUMERICAL (producers as above). The zero of ζ_P: conditional on the tail hypothesis only. Untried (NOTE:43–47):
interval Rouché, X = 10¹², the θ → 0 and ρ → 1 limits, zeros with σ < ½.

### A.10 s5m — the fate of Lemma H: multiplicity in S5(0.8) and in every dense ℕ-supported system. Close K (stop line (b)) + T
Verdicts: read-F AGREES-WITH-CORRECTIONS (rF:3); read-O AGREES-WITH-CORRECTIONS, F1–F3 (5 pairs) + 12 minor (rO:12–21). 18/18 pairs
applied; "Unit CLOSED DUAL-READ: K (n_K, four code paths) + T (T1 on a printed core; T2, T3, T4, T4′ new as statements)" (rF:17).
Three most useful findings.
1. **K: the integer n_K** (NOTE:11–16): n_K = 2⁸·3⁵·5⁹·7³·11²·13·17·19³·23·29²·37·41²·59·61·79·89·109·149 (≈ 3.78·10⁴²) has a_{n_K} ≥
   f_G(n_K) = 3,403,961,916,617,140 > 3.76·n_K^{0.35} + 3, so "hypothesis H_θ of Theorem K′ is false for every θ ≤ 0.35 and every
   constant c < 1.88; Theorem K′ is vacuous as stated" (NOTE:15–16). Dual-read; four code paths (fcert 128-bit, checkK mod three primes,
   the orchestrator's recount `verify-F/recount_nK_F.log`, read-O's full-lattice count on its own sieve generator, A1, rO:295–298).
   read-O A5 (rO:310–312): c = 1.88 fails for every θ ≤ 0.351285; exact Rouché tolerance c < 1.8790.
2. **T1–T3: bounded multiplicity forces a thin surgery** (NOTE:160, 171, 180): sup a_n < ∞ ⇔ a_n ≤ 1 ⇔ free g-primes with m_q ≤ 1 (T1;
   a relation forces a_{n₀^k} ≥ k + 1); in a free ℕ-supported system K(x) ≤ R(x/2) (T2); free + N = ρx + O(x^θ), θ < 1 ⇒ refused primes and
   added composites are both O(x e^{−c√log x}) (T3, via Landau's PNT quoted from DMV 2006 pp. 2–3). THEOREM (dual-read; rF:6–8; rO:16–17).
   Prior art (F2): T1's core is Olofsson 2010 pp. 10–11 (checked at the line by the orchestrator, rF:13); Lagarias 1999 is the nearest
   printed relative of T2–T3 ("[quoted from the review]" — neither reader opened it).
3. **The certified climb** (NOTE:21–22; Instruments row 3): the exponent of the exact lower bound f_G(n) is 0.2726 (10⁹), 0.3294 (10^20.3),
   0.3493 (10^29.9), 0.3617 (10^40.0), 0.3648 (10^42.6), marginal 0.37–0.46 from 10¹⁵ on, no decline — exact at all six points (rO A2,
   :299–300). NUMERICAL (2 producers). Model crossing of n^{0.383} at 10⁶⁴–10⁸⁸ [model].
Most useful failure. What T does NOT give (read-O F1, rO:201–207): T4′ (rank excess ⇒ max a_n ≥ x^{κ/log log x}) allows β = 0, so "integer-
level feedback cannot keep β small" for every dense non-surgery system on ℕ is unproved (the open case 4(b), NOTE:197–198; UT-M5); the
proposed rider headline was narrowed accordingly. And F3 (rO:218–224): "S5(0.8) obeys α ≤ 2β if the exponent passes 0.383" needs
α = Re ρ₁, which the record has only as α ≥ Re ρ₁ under H_θ — now refuted.
Borrow. (a) The exact multiplicity lower bound f_G with a FIXED finite G — but note its ceiling: "no fixed finite G can refute" Lemma H in
its ≪ form, f_G(n) ≤ (1 + log₂ n)^{|G|} (NOTE:17–18). (b) A3–A4 (rO:302–309): T3's power-saving hypothesis cannot be dropped (R(x) ≍
x/log²x example), and infinite thin surgeries have unbounded gaps (never in Lagarias's Delone class). (c) §5.1's exact rule (n is a
g-prime iff A(n) = 0 and E(n − 1) ≤ 0.3) — already in the record (uoff read-O A1; F2(iii)).
Statuses. T1 (core in print), T2, T3 and its converse, Lemma A, T4, T4′: THEOREM (dual-read). K: dual-read computation (above). Exact
system to 2·10⁹ (max a_n = 344, sup E = 348.0): NUMERICAL (2 producers, byte-identical g-prime lists). Lemma H in the ≪ form: open.
UT-M4 (task 6, zeros of F_X at 10⁹): not run (stop line).

### A.11 lg — S7, integer-level feedback acting only at prime powers (the prime-local class on ℕ). Close K-candidate + K-conditional theorems + G
Verdicts: read-F AGREES-WITH-CORRECTIONS (rF:3); read-O AGREES-WITH-CORRECTIONS, F1–F2 record-level + 14 minor, 18 pairs (rO:14–30). 18/18
applied; "Unit CLOSED DUAL-READ: K-candidate (numerical; two producers) + T (Lemmas 1.1, 1.2, 4.1; K₇ and K₇^{≤2} conditional on H and on
floating-point boxes) + G (Lemmas H₇, H₇^{≤2})" (rF:21). m12–m13 deleted two sentences about the Riemann hypothesis (rF:15).
Three most useful findings.
1. **S7^{≤2}(3/5), the capped prime-local system** (NOTE:29–33, 230, 254): every m ≤ 2, so a_n ≪ n^ε is PROVED (Lemma 4.1, the Ramanujan
   condition; rF:8), and at X = 10⁹ β ≈ 0.19–0.22, α ≈ 0.79–0.83, a boxed zero z₁ = 0.8243658 + 11.0306646i of F_X, γ = 0.78–0.82:
   α − 2β = +0.36…+0.44, with |C(u)| ≤ 0.93·u^{0.40} on all of [10³, 10⁹]. Lemma 4.1: THEOREM (dual-read); the numbers: NUMERICAL (2
   producers — read-O's sieve and additive-DP generators agree byte for byte with the unit's dumps to 10⁹, rO:16–22).
2. **Theorems K₇^{≤2} and K₇** (NOTE:208, 254; close NOTE:35–39): if |N_P(u) − 0.6⌊u⌋| ≤ u^{0.40} for all u > 10⁹ then Conjecture U is
   false (for S7^{≤2}(3/5) and for S7(3/5)). CONDITIONAL THEOREM (on H₇^{≤2} / H₇ and on the floating-point box values), dual-read (rF:9;
   rO:22–25 "the conditional refutations of U are correct as stated"); the Taylor truncation is rigorously ≤ 3.4·10⁻²⁹ (A4), only the
   double-precision summation and sampling remain floating-point. Rouché thresholds θ < 0.4005 (B₁), 0.4022 (B^{≤2}) (A6, rO:353–354).
3. **Lemma 1.2 — the downward side is bounded by prime-power gaps** (NOTE:64): multiplicities ≤ ρ·(prime-power gap) + 1 + ρ, so S5's
   factorization-counting explosion cannot occur in S7 (NOTE:40–42). THEOREM (dual-read; rF:7). But read-O A2 (rO:341–344): the cap
   breaks it — S7^{≤2}(0.6) reaches inf E = −197.8 below the gap bound −169.7, so H₇^{≤2}'s lower half needs a different mechanism.
Most useful failure. F1 (rO:218–228): the close turned a scan of the approximant F_X at X = 10⁷ into "no other zero [of ζ_P] in σ ≥ 0.70
below height 100" — not available even conditionally (at 0.70 + 94.63i the H_{0.40} tail 0.629 exceeds |F_X| = 0.138). F2 (rO:229–
240): Révész–Pintz's zero-density theorem needs Axiom A, which for S7^{≤2} is the open H. And the brief's expectation "multiplicities
small" was corrected: bounded by gaps, not small (m_p up to 79–219; NOTE:40–42).
Borrow. (a) The cap m ≤ 2 as the cheap way to prove Ramanujan for a feedback system (Lemma 4.1; A3 extends it to μ_P). (b) A1
(rO:336–340): ζ_P converges absolutely on σ > 1 and N(x) ≪ x^{1+ε} unconditionally for every S7(ρ). (c) Direct-sum boxes with a sampled
Lipschitz lower bound (A5) as the standard second route for any boxed zero.
Statuses. Lemmas 1.1, 1.2, 4.1: THEOREM (dual-read); K₇, K₇^{≤2}: CONDITIONAL THEOREM (dual-read), "new as statements on a printed core"
(rO §6). Constructions S7, S7^{≤2}: new (dual-checked search). Numerical crossing: NUMERICAL (2 producers), "new (numerical)". Lemmas H₇,
H₇^{≤2}: open (G). S7 is an ℕ-supported counterpart of S8; read-F's ranking: "S8 has no downward half to prove (E > −½ by
construction), which is why S8 is the better target" (rF:18).

## §B Cross-unit propositions (numbered; one sentence each, then evidence and status as the reads leave them)

B1 (rigidity at every conductor, discrete class). Every DISCRETE Beurling system with Riemann's exact FE at any conductor is ζ, and the
   rigidity reaches finite generalized Dirac combs with any weights and ζ-divisible solutions with thin rational part — so a Q-side twin of
   the virtual curve must leave discreteness (weighted or mixed, clustering, infinitely many masses: (R1)–(R4), smallest 𝒯) or leave the
   exact equation. Evidence: qcond Theorem D (NOTE:351–358; rF:18; rO:13–15), U_q, L′, E2 (NOTE:440–446); qtw G1, G1′, L‴, the 𝒯
   reduction (NOTE:51–69, 128, 153, 203). Status: THEOREM (dual-read). It pays s37 digest B5's "only unpaid price" in the negative and
   moves B6's Q-side twin out of the discrete class (qtw NOTE:76–78). On 𝒯 a solution must have all zeros of D_a on Re s = ½ when σ_S = ½
   (qtw rO A2, single-check) — [consolidator's reading] the last open corner carries a line condition on its multiplier's zeros.
B2 (Conjecture O: a proof must use norm-injectivity, and every route stops at α_R/4 without the unresolved pairs). O is a theorem under
   RH for every regular deletion and every c, and unconditionally on four deterministic irregular classes; it is FALSE at the
   function-field rung, where every input of Theorem Z's proof except zero-freeness of D_R holds. Evidence: conjO Theorem Z, Cor. Z.1
   (NOTE:24–26, 312–315); lemG T2–T5 and R1 (NOTE:24–26, 332–346; zoo I.11); counterexamples must be anti-clustered (lemG rO A2); the
   common ceiling α_R/4 of Prop. 1.3 (RH) and Prop. O1 (unconditional) — "both see only the resolved denominators b ≤ √X" (conjO
   rO:327–331). Status: Z, Z.1 CONDITIONAL THEOREM (RH, dual-read); R1, T2–T5 THEOREM (dual-read; T2 for sq under RH or a recalled
   large-gap bound); O1 and A2 single-check. Lemma G is a reformulation of O, not a weaker input (conjO F2).
B3 (on ℕ: multiplicity or thin surgery). An ℕ-supported discrete system pays its largest multiplicity in integer error (sup E ≥
   max a_n − 1.3), bounded multiplicity is freeness, and a free ℕ-supported system with N = ρx + O(x^θ), θ < 1, is a thin surgery of ℙ —
   so a dense non-surgery system on ℕ must carry UNBOUNDED multiplicities; S5's grow like a power (certified exponent 0.3648 at
   10^{42.6}), and the capped S7^{≤2} sits in the only room left, a_n unbounded but ≪ n^ε. Evidence: uoff rO A2 (:235); s5m T1–T3
   (NOTE:160, 171, 180), n_K (NOTE:11–16); lg Lemma 4.1 (NOTE:230). Status: T1–T3, Lemma 4.1 THEOREM (dual-read); n_K dual-read
   computation. Open (s5m 4(b), NOTE:197–198; UT-M5): whether every dense non-surgery system on ℕ has β bounded below. [consolidator's
   reading] S7^{≤2}(3/5) is a concrete member of that open case (dense refusal + Ramanujan) exactly when its Lemma H₇^{≤2} holds.
B4 (one-sided regularity forces a real zero; U on never-undershooting systems is ONE integer bound; its two-sided sieve form is false).
   A Beurling system whose count never falls below ρu + r₀ and has error O(u^θ), θ < r₀/(r₀ + ρ), has a real zero ≥ r₀/(r₀ + ρ) —
   "ℕ escapes only because ⌊u⌋ − u ≤ 0" (fgT NOTE:13–14) — so for S8(ρ), ρ < ¼, Conjecture U fails as soon as Lemma B_ρ (E = O(x^θ),
   θ ≤ ½ − ρ) holds, with no zero location and no certificate needed. Evidence: fgT Theorem 1.6, Cor. 1.7, the Dichotomy (NOTE:11–18,
   103, 113, 208); the sieve form's Mertens bias (1 − 2e^{−γ})u/log u (fgT rO F1, A3; rF:26); the price — B_ρ has the strength of a
   g-prime gap bound x^θ, θ < ½ − ρ, beyond any zero-density bootstrap (fgT rF:31–32, single-check). Data: sup E ≈ 0.05·log²x (π/16),
   0.03·log²x (π/32) to 10¹¹ (fgC NOTE:30; 2 producers to 10¹⁰). Status: Theorem 1.6, Cor. 1.7 THEOREM (dual-read); B_ρ NOT proved;
   "not even E = o(x) is proved" (lemmaB CHARTER §1).
B5 (random discretization sits exactly on U's line; only feedback or additive structure can cross it). Almost every realization of
   Diamond–Zhang's construction is a [1, ½]-system — on α = 2β, consistent with U — and the one-scale mechanism (Lemma 2.1) shows the
   ½ is the variance of the selection itself; every candidate on the record that crosses the line numerically (S5, S7, S7^{≤2}, S8) is a
   FEEDBACK system. Evidence: dzh Theorem 1, Cor. 2 (NOTE:13–21; rF:11; rO:15–19), the null set untested (NOTE:39–41, U-1); lemmaB
   CHARTER §2(c) ("Generic or randomly discretized systems have integer error x^{½+o(1)}" — the orchestrator's reading, no proof on
   disk). Status: THEOREM (dual-read) for DZ; the general sentence is a reading, not a theorem.
B6 (positive forms in the positions of generalized integers are blind to the virtual curve). The positions form of the Fejér defect is
   positive because dN ≥ 0 and is therefore V-blind (D_1(V) = 4), its zeros form is Weil's functional, and the explicit formula maps one
   to the other; a separator of V needs an object V lacks (a Weierstrass model: class C) or integrality (class (B)). Evidence: fej Theorem
   K (NOTE:258–276), Theorem F (NOTE:24–27), Theorem W (NOTE:18–22); fej rO A1 (:292–305). Status: THEOREM (dual-read), no new
   mathematics; A1 single-check. With s37 B4 and zoo I.9, this closes UT-4 and the first rung of "Extremal characterization of ξ".
B7 (where positivity enters; linear or growth-only inputs never decide). In every unit of the wave the decisive step consumed a POSITIVITY
   that linear constraints cannot see: Π ≥ 0 on the q-part's monoid (the Landau obstruction; qcond NOTE:447–450, qtw L‴), the one-sided
   R ≥ r₀ (fgT Theorem 1.6), the order-zero device on log D_R (conjO NOTE:24); while the sieved identities hold for every SIGNED sieve
   (qcond rO R4), affine data functionals vanishing at genus 0 are exactly Weil functionals (fej W), and growth-only mean-value lemmas
   fail (conjO Remark 1.3′). Status: [consolidator's reading; single-check]; each ingredient dual-read in its source.
B8 (feedback numerics are not exponents until the mechanism of E is bounded beyond the range). All three greedy units, and conjO's
   structured sets, had an exponent inference downgraded at the dual read: S5's 0.30 was a transient (uoff NOTE:13; s5m 0.3648 at
   10^{42.6}); S8's "β = 0 numerically" became "β < ¼ on [10³, 10¹¹]" (fgC F2); S7's "no other zero of ζ_P" was a scan of F_X (lg F1);
   greedy deletions' pure-power deficits are log-powers (conjO F4, κ ≈ 2.3–3); sq's sub-diagonal slope is ζ's zeros at ρ/2 (lemG). Status:
   dual-read (each item). Rule for briefs: a feedback system's integer exponent is reported with its mechanism (multiplicity, queue,
   clustering) and a lower-bound instrument beyond the computed range, or not at all.
B9 (the program's working reading, sharpened; s37 B10 updated). The multiplicative structure acts only through what the additive
   structure leaves free: at every conductor in the discrete class it leaves nothing (B1); in deletions what is left must be read through
   the injectivity of the norm (B2); in never-undershooting systems ONE-SIDED additive regularity alone already forces a real zero (B4),
   and ℕ escapes only through the sign of ⌊u⌋ − u. Status: [consolidator's reading] — a summary sentence for briefs, not a claim.

## §C Controls — what each unit used, and flags on their use

C1 The virtual curve V over F₅ (zoo I.9). Used: qcond rung 1 — the linear Q-side constraints admit the RH-false t = ±5, the Landau
   obstruction (F2 with the pole term removed) admits no t (NOTE:463–465); qtw rung 1 — weighted admissibility is exactly t ∈ [−5, 6]
   (W1; all d by rO A1) and Q-side positivity is empty there (W3, in print: Hilberdink 2012 Thm 4.4); fej — I(V) = −0.11803, D_1(V) = 4,
   λ_min(T_M(V)) in Lucas/Fibonacci closed form (rO A3); uoff §3.1 and the free-greedy charter §3 — S5 and S8 as "virtual ℕ" analogs.
   FLAG (for lemmaB-s41 U5-obstruction) [consolidator's check, exact]: V is a discrete rung-1 system with constant integer error and a
   REAL off-line zero (Re s = 0.79899), so any proof that (A) and (B) of the lemmaB charter cannot hold together must use an archimedean
   input V lacks (s37 digest B8). V is not a rung-1 instance of (A): A_n − 5ⁿ/4 = −¼ for every n ≥ 1; its zero comes from the same sign
   change as Theorem 1.6's proof — Z(5^{−½}) = (2 − √5)/((1 − 5^{−½})(1 − √5)) = +0.345 and Z → −∞ as σ → 1⁻ — with the positivity
   supplied by the degree-0 term (R_0 = ¾), not by a one-sided bound.
C2 F_{2.9,2}, DH, Epstein x² + 5y² (zoo I.1, I.9). Used by fej's Z side only: Z1 (M1a's (C_Q)) is passed by F_{2.9,2} (2.95 = 2.95),
   F_{5,5} and Epstein (1.139355 vs 1.139353); Z2 by F_{2.9,2}, DH, Epstein; Z3 is violated by F_{2.9,2} (−872.45) and DH (−681.66;
   complete zero list, argument principle 47.0000) (fej NOTE:30–34; reproduced by rO with a full-rectangle argument principle).
   FLAG: Epstein zeta's real zeros are the PRINTED CORE of Theorem 1.6 (Bateman–Grosswald 1964 p. 367, fgT rO:215–224); fgT's read-O
   tested ℚ(√−3), ℚ(√−163) and ℚ(√5) against Theorem 1.6 — each violates hypothesis (A), consistent with no real zero (rO:15–17; the
   ℚ(√5) case rests on a recalled fact, rO §8). No Session-40 unit ran F_{2.9,2} or DH: they have no integer-count side to test.
C3 The necklace deletion (zoo I.11). lemG Theorem R1 (NOTE:24–26) — the rung-1 control for any proof of O or Lemma G. FLAG: its exact
   ℚ-transplant, the tight ℚ-necklace, OBEYS O unconditionally (lemG rO A1), so R1 controls proofs, not counterexamples over ℚ.
C4 The template dN = δ₁ + ρdx (Diamond 1970 p. 24). fgT Lemma 1.5: ζ_c = (s − 1 + ρ)/(s − 1), zero exactly 1 − ρ, the equality case of
   Theorem 1.6 (rF:9; rO §3(c)); lemmaB CHARTER §1 (U5): "the continuous template has E ≡ 0 and the zero 1 − ρ, so discreteness must
   enter". FLAG: Conjecture U is false for continuous systems (s37 digest B2, m7), so the template is the control every proof of U must
   break; S8's real zero is the template zero displaced by ρζ_P(1 − ρ) (first-order law good to 4·10⁻⁴ for ρ ≤ π/16; fgT NOTE:33–34).
C5 The rational primes through each generator (ρ = 1). S5 returns ℙ (uoff rF:8); S7 returns the 664,579 primes ≤ 10⁷ (lg NOTE:13, 85);
   S8's code path run on ℕ gives N(x) = ⌊x⌋, E ∈ [−1, 0] (fgC NOTE:62), and ℕ (ρ = 1, E = −{x}) has ζ < 0 on (0, 1), no real zero —
   the Theorem 1.6 control (fgT NOTE:139). FLAG: S8 at ρ = 1 places its g-primes on the lattice 1 + (k − ½), not on ℕ, so S8 has no
   "returns ℙ" limit; its ℕ-control is the separate code path of fgC NOTE:62 [consolidator's reading of CHARTER §1].
C6 Other controls. dzh: ℙ (0.000), T_0.90 (0.440 ± 0.011), T_0.95, the deterministic grid P_det (constant −0.5998 predicted, −0.5995
   measured), T₁ (NOTE:35–37). lemG: the planted-pole control at slope 0.906–0.940 against 0.90 (NOTE:24–30). qtw: read-O's G1 control
   μ_c (A6). conjO: the c = 1 greedy sets, where β₂ ≥ α/2 is unconditional, calibrate the κ trigger (NOTE:327–328).

## §D Instruments rows — the four Session-40 units only (B2's column shape; records, never ranks; ready to append; files not edited)

Target: `directions/B2-refutation-program.md` "Instruments" (all four units write their rows in B2's shape). Numbers as the dual reads
leave them (corrected NOTEs: fgT 9c5a8886…, fgC 25a78d32…, s5m ca102d85…, lg e8dc8e87…). Where two units measured the same quantity the
rows are MERGED (fgT row 2 + fgC row 5; fgT row 1 + fgC's real zeros) and both result files are named. Producer counts are corrected to
the reads: the NOTE rows of s5m (row 1) and lg (rows 1–4) say "One producer", written before read-O reproduced them.

| Quantity | Current best value | Result file | Dated |
|---|---|---|---|
| Real zero of ζ_P for the free greedy system S8(ρ) (Theorem 1.6: forced in [r₀/(r₀ + ρ), 1) by E > −½ plus any bound E = O(x^θ), θ < 1 − 2ρ; dual-read) | σ* of F_X: π/64 0.947634, π/32 0.895076, π/16 0.794755 (X = 10⁷), π/8 0.656529, π/6 0.521753, π/4 0.514036, 0.95π/3 0.402156 (X = 10⁶); at X = 10¹¹ the rightmost zeros of S8(π/16), S8(π/32) are REAL, 0.7947553732, 0.8950765177 (read-O 0.7947553701, 0.8950765176 at 10¹⁰). Certified brackets: π/16 F_{10⁷}(0.79) = +0.022231 > 0 given only qualitative (B), zero in (0.79, 0.80) if E ≤ 33.7 log²u beyond 10⁷; π/4 F_{10⁷}(½) = +0.067067, zero in (0.50, 0.55) if E ≤ 3.78 log²u. First-order law σ* ≈ (1 − ρ) + ρζ_P(1 − ρ), good to 4·10⁻⁴ for ρ ≤ π/16. Two producers (theory, double precision; read-O, double-double with every close decision re-decided at 60 digits); ordering margins 9–21× smaller than first stated (F2), certificates stand | `free-greedy-s40/theory/NOTE.md` §1.6–1.8, §4.1; `theory/verify/bracket_pi16_1e7.log`, `bracket_pi4_1e7.log`; `free-greedy-s40/compute/verify/logs/zeros_pi{16,32}_X1.000000e+11.txt` | 2026-10-01 |
| Integer error of S8(ρ) in the U-relevant range ρ < ¼ (Lemma B_ρ: θ ≤ ½ − ρ refutes U by Cor. 1.7; with the certificates θ < 0.395 (π/16), θ < 0.445 (π/32)) | π/16: sup E = 3.04, 3.54, 6.88, 9.64, 12.84, 14.71 at 10³…10⁷, 10^7.5 (theory), 33.27 at 10¹¹ (compute); sup E/log²x ≈ 0.05 throughout (best polylog fit log^{2.0}); largest g-prime gap 336.1 at 10⁷, 432.9 at 10^7.5 (1.3–1.5 log²x). π/32: 6.39 at 10⁶, 9.86 at 10⁸, 20.36 at 10¹¹ (≈ 0.03·log²x). π/64: 3.51 at 10⁶. sup E/x^θ at 10¹¹ ≈ 0.015 (π/16, θ = 0.304) and 0.0008 (π/32, θ = 0.402). Producers: two to 10¹⁰ (the units; read-O's 128-bit generator with a per-decision ordering proof), one at 10¹¹ | `free-greedy-s40/theory/NOTE.md` §1.8, §3.0; `theory/verify/mech_pi16_1e7.log`, `mech_pi16_5e7.log`, `mech_pi32_1e8.log`; `free-greedy-s40/compute/NOTE.md` §0 (Small densities); `compute/verify/logs/win_pi16_1e11.log`, `win_pi32_1e11.log`; `compute/verify-O/logs/` | 2026-10-01 |
| Law of E of S8 vs the Poisson-queue heuristic (tail e^{−κh}, κ ≈ 2/(ρ log x)) | measured tail rate = (1.45–1.65)·2/(ρ log x): π/16 on [10³, 10⁷] (theory), π/4 on [10⁶, 10⁹] (compute, λ·log x ≈ 3.7–3.9 vs 2.55; 4.25 at 10¹¹); time-mean of E = 0.57·ρ log x/2 (π/16); sup E ≈ (0.20–0.37)·ρ·log²x for ρ ∈ [π/64, π/4] at 10⁶ (F3-corrected); composite arrivals sub-Poissonian, effective variance ≈ 0.6. Two producers | `free-greedy-s40/theory/NOTE.md` §2.3; `theory/verify/mech_pi16_1e7.log`; `free-greedy-s40/SHARED.md` compute batch 1 | 2026-10-01 |
| Mertens law and Legendre remainder of S8 (the sieve margin of §3.4) | π/16: M(z)·log z = 2.54, 2.70, 2.78, 2.81 at z = 10³…10⁶ (one producer); proved floor M(z) ≥ M_lat(z), M_lat(z)·z^ρ → 1.0127; PROVED (read-O F1, A3, single-check): if E = o(x/log x), S(u, 2u] = (1 − 2e^{−γ} + o(1))·u/log u — two-sided square-root cancellation in S(I) is false for S8 | `free-greedy-s40/theory/NOTE.md` §3.4; `theory/verify/mertens_pi16_1e6.log`; `theory/read-O.md` §4 F1, §7 A3 | 2026-10-01 |
| S8(π/4) integer error sup_{u≤x}E(u) (numerical; not an exponent) | 8.22, 13.33, 26.63, 39.53, 47.86, 95.86, 95.86, 113.20, 123.62 at 10³…10¹¹; best two-parameter description ≈ 0.2·log²x (c·log^k x: k = 2.19; C·x^b: b = 0.145, over-predicting 10¹¹ by 46 %); sup E/x^{1/4} = 1.25, 0.96, 0.36, 0.22 at 10⁶, 10⁸, 10¹⁰, 10¹¹ — β < ¼ on [10³, 10¹¹] (read-O F2: not "β = 0"); windowed mean E ≈ 0.24·log x, exponential tail λ·log x ≈ 3.5–4.3. Producers: three to 10⁷ (unit; orchestrator's prototype; read-O), two to 10¹⁰, one at 10¹¹ | `free-greedy-s40/compute/NOTE.md` §0.1; `compute/verify/logs/win_pi4_1e11.log`, `win_pi4_1e11.Eanalysis.txt`; `compute/verify-O/logs/o_pi4_1e10.log`; `free-greedy-s40/proto/` | 2026-10-01 |
| S8(π/4) rightmost zero of F_X, t ≤ 5000 | ρ₁ = 0.8962124913 + 14.5499355887i (X = 10¹¹; moves 3.4·10⁻¹⁰ from 10¹⁰; 12 digits by a direct sum at 10⁶ and 10⁸, 10 digits at 10⁹–10¹⁰ by read-O); the only zero with σ > 0.85 up to t = 5000; 44 zeros in 0.5 < σ < 1.05, t ≤ 200, plus the real zero 0.51474. Two producers to 10¹⁰ | `free-greedy-s40/compute/verify/logs/zeros_pi4_X1.000000e+11.txt`, `count_strip_pi4_1e11.txt`; `compute/read-O.md` §2 | 2026-10-01 |
| Rouché margin for ρ₁ as a zero of ζ_P(S8(π/4)) (box \|σ − 0.8962\| ≤ 0.03, \|t − 14.5499\| ≤ 0.03, winding 1) | B_max = 39,928 for \|E(u)\| ≤ B·log²u, u > 10¹¹ (unit; read-O's second route 40,028; read-F's crude form 35,144); 601 for B·u^{0.4}; from the proved range alone B_max = 6531 beyond 10¹⁰ (206 for B·u^{0.4}; read-O A2); a rigorous \|F′\| bound gives min\|F_{10¹⁰}\| ≥ 0.1076 on the boundary (read-O A3). Observed max E/log²u = 0.307 on [10⁴, 10¹¹]. Floating-point samples; no interval certificate | `free-greedy-s40/compute/verify/logs/rouche_pi4_1e11_z1.txt`; `compute/verify-O/derivbound_o.py`, `logs/derivbound_o.txt` | 2026-10-01 |
| α(S8(π/4)) by the explicit formula | 0.8962 numerically (≥ 0.8962 under the tail hypothesis): 44 zeros + the real zero 0.51474 reproduce ψ_P − x on [10⁴, 10¹¹] to 0.2 % of its rms (per-decade correlation ≥ 0.995); read-O checked 17 half-decade points to 10¹⁰ (differences 0.06–1.9 %) | `free-greedy-s40/compute/verify/logs/explicit_pi4_1e11.txt`; `compute/verify-O/logs/explicit_o_partial.txt` | 2026-10-01 |
| S8 generator capacity and ordering proof | 7.85·10¹⁰ g-integers (X = 10¹¹, ρ = π/4) in 57 min, 3.25 GB, double-double, ordering safe under the ESTIMATED dd error (F1); PROVED to 10¹⁰ for π/4, π/16, π/32 (and 4/5 to 10⁸, 4,019,495 ties) by read-O's 128-bit fixed-point generator with a rigorous per-decision bound (0 flags; 17 min, 1.6 GB at 10¹⁰) | `free-greedy-s40/compute/verify/s8win.c`; `compute/verify-O/s8o.cpp`, `logs/o_pi4_1e10.log` | 2026-10-01 |
| Certified multiplicity of S5(0.8) beyond the computed range (lower bound a_n ≥ f_G(n), G = g-primes ≤ 10⁹, exact integers) | a_n ≥ 3,403,961,916,617,140 = 4.2647·n^{0.35} = n^{0.36479} at n_K = 2⁸·3⁵·5⁹·7³·11²·13·17·19³·23·29²·37·41²·59·61·79·89·109·149 (log₁₀ = 42.577); kills H_θ of Theorem K′ for θ ≤ 0.35 and every c < 1.88 (c = 1.88 fails for θ ≤ 0.351285; exact Rouché tolerance c < 1.8790, read-O A5). Four code paths, three producers: the unit (fcert 128-bit; checkK mod three primes), the orchestrator's recount, read-O's full-lattice checked-uint64 count on its own sieve generator; dump re-certified by the Ω-identity, 0 failures to 10⁹ | `s5-multiplicity-s40/NOTE.md` §2.3, §2.5; `…/verify/logs/fcert_K1.log`, `checkK_K1.log`, `omega_check.log`; `…/verify-F/recount_nK_F.log`; `…/verify-O/lattice_O.c` | 2026-10-01 |
| Exact S5(0.8) beyond 10⁹ | to 2·10⁹: N = 1,600,000,009, C(2·10⁹) = 9, max a_n = 344 at 1,805,076,000, sup E = 348.0; two code paths (Ω-recursion generator; read-O's multiplicative sieve, byte-identical g-prime list SHA c3aee0f9…9c35) | `s5-multiplicity-s40/NOTE.md` §3; `…/verify/logs/omega_check.log` | 2026-10-01 |
| Growth of max a_n (S5(0.8)): exponent of the exact lower bound f_G(n) vs log₁₀ n | 0.2726 (9.0), 0.3294 (20.3), 0.3493 (29.9), 0.3617 (40.0), 0.3648 (42.6); marginal 0.37–0.46 from 10¹⁵ on, no decline; exact at all six points (NOTE §2.3; read-O A2). Two producers. Model crossing of n^{0.383} = n^{Re ρ₁/2} at 10⁶⁴–10⁸⁸ [model] | `s5-multiplicity-s40/NOTE.md` §2.4, §5.3; `…/verify/logs/search2_rate_K60.log` | 2026-10-01 |
| (α, β) of the prime-local integer-greedy system S7(ρ) (g-primes are prime powers, a_n multiplicative; numerical, not proved) | ρ = 0.6, X = 4·10⁹: β ≈ 0.26–0.31 (running sup of \|E\|, windows 10³…10⁷ → 4·10⁹: .307 .295 .276 .272 .259, falling), α ≈ 0.80–0.81 (running sup of \|ψ_P − x\|), γ (Beurling Möbius sums) 0.80–0.82; α − 2β = +0.18…+0.29 on every window. X = 10⁹: ρ = 0.75 / 0.8 / 0.9 / 1.1 above the line from 10⁴ / 10⁴ / 10⁵ / 10⁵ (+0.07…+0.31); ρ = 1.25 below (−0.02…−0.10); ρ = 1.5 runs away. Two producers (read-O's sieve and additive-DP generators agree byte for byte with the unit's dumps to 10⁹; slopes ±0.002 at ρ = 0.6) | `local-greedy-s40/NOTE.md` §2; `…/verify/logs/sweep/fits_v0_1e9.log`, `fits_v0_r06_4e9.log`; `local-greedy-s40/read-O.md` §2 | 2026-10-01 |
| Off-line zeros of S7(0.6)'s F_X (route 2; the zeros behind Theorem K₇) | ρ₁ = 0.8209965 + 11.0877411i, ρ₂ = 0.8052963 + 20.2490762i (Newton at X = 10⁷, 10⁸, 10⁹; stable to 2·10⁻⁵); winding number 1 on B₁ = [0.8010, 0.8410] × [11.0677, 11.1077] (min\|F_X\| = 0.0654 vs tail ≤ 0.0068 under H_0.40) and on B₂ (0.0838 vs 0.018); Taylor truncation ≤ 3.4·10⁻²⁹ (read-O A4); F_X at X = 10⁷ has no other zero in σ ≥ 0.70, t ≤ 100 — a statement about the approximant, not about ζ_P (F1). ρ = 0.75 / 0.8 / 1.1 top zeros 0.80563 + 92.34370i / 0.74647 + 30.69772i / 0.83989 + 20.33964i (X = 10⁸, not boxed). Two producers (read-O by direct sums, no Taylor moments) | `local-greedy-s40/NOTE.md` §3; `…/verify/logs/zeros/cert_r06_z1_1e9.log`, `newton_r06_X1e9.log`, `zcount_r06_1e7.log`; `local-greedy-s40/verify-O/logs/box_*_X1e9_K40.log` | 2026-10-01 |
| (α, β) of the capped prime-local system S7^{≤2}(ρ) (m_n ≤ 2; a_n ≪ n^ε PROVED, Lemma 4.1, dual-read; the K-candidate with tame multiplicities; numerical, not proved) | ρ = 0.6, X = 10⁹: β ≈ 0.19–0.22 (b_sup .215 .207 .204 .204 .192), α ≈ 0.79–0.83 (a_sup), zero z₁ = 0.8243658 + 11.0306646i of F_X (Newton 10⁷…10⁹, stable to 9·10⁻⁶; winding 1 on [0.8044, 0.8444] × [11.0107, 11.0507], min\|F_X\| = 0.0692 (read-O 0.06933) vs tail 0.0063 under H_0.40), γ = 0.78–0.82; α − 2β = +0.36…+0.44; max\|C(n)\|/n^{0.40} ≤ 0.93 on [10³, 10⁹], 0.10 in the top decade; inf E = −197.8, below the S7 gap bound −169.7 (read-O A2: Lemma 1.2 has no analog for the cap). Rouché threshold for refuting U: θ < 0.4022 (read-O A6). Two producers | `local-greedy-s40/NOTE.md` §4.2; `…/verify/logs/sweep/fits_v2_r06_1e9.log`, `…/logs/zeros/cert_v2r06_z1_1e9.log`, `hcheck_v2r06_1e9.log`; `local-greedy-s40/verify-O/logs/box_Bcap2_X1e9_K40.log` | 2026-10-01 |
| Lemma H₇ on the computed range (the one hypothesis of Theorem K₇) | max\|N(u) − 0.6⌊u⌋\|/u^{0.40} per decade 10³…10⁹: 1.05, 0.86, 0.93, 0.60, 0.45, 0.35 (needed: ≤ 1 for all u > 10⁹); Rouché threshold θ < 0.4005 for B₁ (read-O A6). Two producers (read-O reproduced the H-ratios) | `local-greedy-s40/verify/logs/zeros/hcheck_r06_1e9.log`; `local-greedy-s40/read-O.md` §2 | 2026-10-01 |

Not rowed (no number of their own, or already in B2): s5m's §5.2 carrier statistics (c_ℓ(10⁹) ≈ 0.043·10⁹/ℓ; carrier probability
(1.6–1.8)/ln n) — a heuristic model input, one producer (s5m NOTE:27–28); fgC's exploratory complex zero of S8(π/16) at 0.5733 + 30.7797i
(fgT NOTE:35; not re-run by read-O, rO §8). Column check: every row above has 4 cells; absolute-value bars are escaped as `\|`.

## §E Errata — every FIX-FIRST of the eleven dual reads (one line each, with status), record residues, and brief errors caught

No read-F/read-O pair contradicts the other on a theorem's validity (stop condition not met). Every FIX-FIRST below is APPLIED in the
NOTE on disk (the reconciliation sections: qcond NOTE:3; conjO NOTE:3; uoff rF §7; lemG rF §4; dzh NOTE:11; qtw rF §5; fej rF §5; fgT
rF:35; fgC rF:16–17; s5m rF:17; lg rF:21) unless marked otherwise. "R" = a residue found by this consolidation, not in either read.
E.1 qcond (read-F: none, P1–P3 minor; read-O F1–F3)
- F1 Theorem D is unconditional (Meyer LNM 117 p. 25, unit masses, μ_q − (ρ_q − 1)·Lebesgue) — an UPGRADE, found by both reads. Applied.
- F2 Prior art on disk missed (Hilberdink 2012 §4: Prop. 4.2 = U_q Step 4; Thms 4.3–4.4; Thm C, squarefree conductors) — novelty split.
  Applied.
- F3 The (Q4) quote replaced by Meyer's page. Applied.
- R1 Application slip of F1: the corrected Theorem D block stands FIVE times (NOTE:219, 252, 335, 351, 451; the pre-reader NOTE has one);
  at 218–219 it cuts L′'s COVERAGE sentence after "It strengthens BFE" (the lost tail, pre-reader 215–216: "§11(i) (finite Euler
  factors) to all finite Dirichlet-polynomial multipliers. `[novelty: single-check]`"); at 458 the G residue follows step (2) without
  steps (3)–(6). The complete proof is at 351–358ff. OPEN — a record repair, no statement changes.
- R2 NOTE:439 "T (unconditional, proved here; `[novelty: single-check]`)" against NOTE:435 "`[novelty: dual-checked]`" and rO:23–24's
  split labels. OPEN (label).
- Normalization note (not an erratum): read-F subtracts ρ_q·Lebesgue (comb on Λ∖{0}, rF:18), read-O (ρ_q − 1)·Lebesgue (comb on Λ,
  rO:13–15); both valid; the NOTE uses read-O's.
E.2 conjO (read-F: none, m1–m3; read-O F1–F4)
- F1 Prop. 1.1(a) omitted the b = 1 frequencies (c(a) = ρ/(2πia)); the Parseval product already contained them. Applied.
- F2 Under RH Lemma G is EQUIVALENT to O₂ set by set — a reformulation, not a weaker input. Applied.
- F3 α = 0.75: the sup tension is resolved, the top-window mean square is undecided (20 seeds 0.816 ± 0.039). Applied. (read-F had
  accepted the 12-seed resolution at the report level, rF:16.)
- F4 "provably log-powers" is a fit (κ ≈ 2.3–3); what is proved is β₂ ≥ α/2 on those sets. Applied.
E.3 uoff (read-F F1–F2; read-O F1–F14, 24 pairs; both reads agree — rF §7)
- rF F1 = rO F1, F2, F3, F4, F9, F11, F14: "β ≈ 0.30" is the slope of the running sup on [10³, 10⁹], not an exponent; the stop condition
  "met" becomes "reported but not established"; K′'s bullet and the consequences for DMV/BDR/read-F P2 are qualified. Applied (NOTE:13–28).
- rF F2 = rO F8: the integer exponent is set by multiplicity spikes, not by the one-sided overshoot of the rule. Applied.
- rO F5–F7: "clean power laws, not transients"; "the brief's stop condition … is met"; "H_0.32 holds with room" — each qualified by
  the multiplicity data beyond 10⁹. Applied.
- rO F10 (logic): Lemma H for one system refutes U; its failure for all leaves U open — not "U holds or fails exactly as Lemma H". Applied.
- rO F12–F13: the Instruments row's first cell and value cell (the β-leg "undetermined"). Applied (B2 row, digest-APPLIED §1).
- R3 NOTE:22 and :170 still read "at exponent 0.35 unrefuted and unsupported" / "(necessarily θ > 0.3227)"; since s5m's n_K, H_θ is
  false for every θ ≤ 0.35 with any c < 1.88, in particular for K′'s stated c = 1 (s5m NOTE:15, 101; rF §7). OPEN (record lag; the
  zoo's I.2 rider, BARRIER-ZOO.md:92, already states it).
E.4 lemG (read-F: none — "F1 and F2 are real and were MISSED here", rF §4; read-O F1–F5, 14 pairs)
- F1 T2's "intervals are disjoint" is false at k = 2, so sq = {nextprime(p²)} is covered only under RH or a recalled large-gap bound,
  not "uncond." (four places). Applied.
- F2 T5's spacing N·2^N lies below every proved gap bound; repaired by a greedy choice (unconditional with Ingham). Applied.
- F3 Cor. 2.2 needs continuation paths in {σ ≥ Re s₀}; no application affected. Applied.
- F4 The tight ℚ-necklace obeys O UNCONDITIONALLY (cluster lemma + Selberg's sieve; A1) — an UPGRADE. Applied.
- F5 Prior art on disk: Hilberdink 2012 Thm A (periodic N − cx forces a finite deletion), the nearest published object to R1. Applied.
E.5 dzh (read-F: none, m1–m2; read-O F1–F2)
- F1 A quoted gap (7.6·10⁻⁷) and a percentage range in §3.1 do not reproduce — a quadrature artifact; no conclusion depends on it. Applied.
- F2 The book's §17.10 normalization may add an INFINITE O(log x)-sparse sequence; Theorem 1 covers it in one sentence. Applied.
E.6 qtw (read-F: none, m1; read-O F1–F6, 30 pairs + one table row)
- F1 Credit: Lemma M, Cor. M1 and the unconditional Theorem D were proved first in qcond's dual read. Applied.
- F2 Prior art on disk: Hilberdink 2012 Prop. 3.4, Thms 4.3, 4.4, C — labels of L‴ and (W3) split. Applied.
- F3 The M = 4 probe value is ≥ −0.293651, not −0.31 (M = 5, 6 added). Applied (accepted as read-O's values).
- F4 Cor. M1 false as written (μ = δ₀ has μ̂ = Lebesgue): add "μ̂ purely atomic". Applied.
- F5 Zeta-zero repairs fail hypothesis (i) of Prop. S; covered by the direct splitting plus §4. Applied.
- F6 §5.2's mechanism (b) was a heuristic labeled (P); smooth self-dual weights vanishing on Z_j exist (KNS Lemma 6): §0.4(3)'s exclusion
  narrowed to the §7.1 families — a DOWNGRADE. Applied.
E.7 fej (read-F: none; read-O F1–F2, 14 pairs)
- F1 Only D_1 vanishes exactly at genus 0 (D_k(P¹) = q^{k−1} − 1 > 0 for k ≥ 2); "D_k > 0 on every zeta datum" needs "of genus ≥ 1". Applied.
- F2 "The separating inequalities are exactly the Toeplitz cone" holds for separation from the Weil region only; class (B) (Weil +
  integrality, e.g. 17g/4 + N_1 − 6 over F₅) also separates V; Oesterlé/HP19 descriptions corrected. Applied.
E.8 fgT (read-F completed AGREES-WITH-CORRECTIONS; read-O F1–F3, 13 pairs of 27)
- F1 Two-sided square-root cancellation in the Legendre remainder S(I) is FALSE for S8 (Mertens bias 2e^{−γ}); only one-sided forms
  survive — binding on lemmaB-s41 (CHARTER §0 item 3). Applied.
- F2 The floating-point audit omitted one of two decision classes; stated ordering margins 9–21× too large; certificates stand. Applied.
- F3 "sup E ≈ (0.37–0.53)·ρ·log²x" is (0.20–0.37)·ρ·log²x. Applied.
- R4 NOTE:11 and :103 label Theorem 1.6 "[novelty: single-check — not found in print]"; both reads: "new as a statement on a printed core
  (Bateman–Grosswald 1964 p. 367; Phragmén)" (rO:221–224; rF:35). OPEN (label).
E.9 fgC (read-O F1–F2, 5 pairs)
- F1 "Certified" ordering rested on an asserted double-double error the code never bounds; now PROVED to 10¹⁰ by read-O's generator. Applied.
- F2 "β = 0 numerically; no power law fits" overstated nine running-max points; β < ¼ on [10³, 10¹¹] is what the data carry. Applied.
E.10 s5m (read-O F1–F3, 5 pairs)
- F1 The proposed zoo rider's headline asserted a barrier the NOTE lists as open (dense non-surgery systems on ℕ); narrowed to S5. Applied.
- F2 Prior art on disk: T1's core is Olofsson 2010 pp. 10–11; Lagarias 1999 the nearest relative of T2–T3; §5.1 already in the record. Applied.
- F3 "β > 0.383 ⇒ α ≤ 2β" needs α = Re ρ₁, which the record has only as α ≥ Re ρ₁ under the refuted H_θ. Applied.
- R5 Instruments row 1 (NOTE:307) says "One producer"; four code paths, three producers since the reads. OPEN (corrected in §D).
E.11 lg (read-O F1–F2, 2 of 18 pairs)
- F1 §0 turned a scan of F_X at X = 10⁷ into a statement about ζ_P ("no other zero in σ ≥ 0.70 below height 100"). Applied.
- F2 Révész–Pintz's zero-density theorem assumes Axiom A, which for S7^{≤2} is the open H. Applied.
- R6 Instruments rows (NOTE:327–330) say "One producer"; read-O reproduced every number (two). OPEN (corrected in §D).
E.12 Errors of the orchestrator's briefs and charters that the units caught
- conjO: the brief's reflected identity lacked the coprimality factor (1 − p^{2σ−2}), and its gap lemma ("mean value for a function
  known only as analytic of finite order in a strip") is false (η(2s)) (NOTE:21–23; rF:5).
- lemG: the brief's dichotomy "P_R continues past α_R/2, or has a natural boundary there" is not one (NOTE:352–355).
- lg: the brief's expectation that prime-local multiplicities are small — they are bounded by gaps, not small (NOTE:40–42).
- free-greedy: the charter's prototype drifts its g-primes by float error (fgC NOTE:9; fgT waste line, NOTE:416–417), and the
  orchestrator's question on Diamond 1970 is settled — "quite simple examples" are continuous (fgT NOTE:37–39).
- uoff: the brief's stop trigger ("α > max{½, 2β} + 0.05 numerically over two decades") accepted a pre-asymptotic fit (rO F1, F6) —
  caught by the reads, not by the unit.

## §F The survivor filter (KICKSTART 10(d)) and the ranking of candidate next units

F.1 Filter. KICKSTART 10(d): "A result graded above threshold (a new zoo Group-IV barrier, a lemma surviving two blind referees, or a
Lean-checked statement) pulls the NEXT session's full agent budget into its follow-ups". Applied with the brief's three triggers (a
theorem surviving two reads; a new control; a conjecture's refutation or conditional refutation). No Group-IV barrier and no Lean
statement came out of this wave. ABOVE threshold:
- (a) **Theorem 1.6 with Cor. 1.7 and the Dichotomy** (fgT) — two reads; a CONDITIONAL REFUTATION of Conjecture U reduced to one integer
  bound with no zero location (B4). The wave's lead; its follow-up is the running stream `lemmaB-s41` (seven units).
- (b) **Theorems K₇ and K₇^{≤2}** (lg) — two reads; conditional refutations of U (on H₇ / H₇^{≤2} and floating-point boxes), with
  Lemma 4.1 (a_n ≪ n^ε for the cap) proved. Follow-up: §F.2 item 2.
- (c) **Theorem D, U_q, L′, E2** (qcond) and **G1, G1′, L‴, the 𝒯 reduction** (qtw) — two reads; rigidity at every conductor in the
  discrete class (B1). Zoo: the I.10 rider (entered Session 40). Follow-up: §F.2 item 5.
- (d) **Theorem R1** (lemG) — two reads; a NEW CONTROL (zoo I.11, entered) and, with T2–T5 and conjO's Theorem Z / Cor. Z.1 (RH), the
  theorem-grade state of Conjecture O (B2). Follow-up: §F.2 item 6.
- (e) **dzh Theorem 1 / Cor. 2** — two reads; BDR fn. 4 answered for a.e. realization (zoo I.2 rider, entered). Follow-up: §F.2 item 3.
- (f) **s5m T1–T3 and the n_K certificate** — two reads (T1's core printed, Olofsson 2010); a refutation of Theorem K′'s hypothesis
  (the S5 candidate withdrawn; zoo I.2 rider, entered) and the structure theorem of B3. Zoo: the T2–T3 rider is staged here (block (ii)).
Below threshold (recorded, not funded on their own): fej Theorem K (correct, "found nothing new, correctly" — it closes UT-4); conjO
Prop. O1, lemG A2, qtw A2 and A6, fgT A1–A4, s5m A3–A4, lg A1–A3 (single-check additions); every number of fgC, lg and s5m (NUMERICAL);
uoff Theorem K′ (correct, now vacuous). WITHDRAWN: the S5(0.8) numerical crossing (uoff NOTE:13).
Consequence under 10(d): the budget belongs to the follow-ups of (a) — which is what `lemmaB-s41` is — and of (b), which is NOT in
lemmaB's charter (S7^{≤2} undershoots, inf E = −197.8, so it fails (A); lg rF:18). Other lanes stay paused.

F.2 Ranking of candidate next units (contract clause; price; stop line). Reads = the standing dual read after each writer.
1. **`lemmaB-s41` — Lemma B for S8 and never-undershooting variants** (RUNNING, seven units U1–U7; CHARTER §3). Contract (charter §1):
   "(B) proved for a system with (A)", or "proof class X cannot yield (B) because Z", with the control that defeats X. Do not duplicate.
   Inputs this digest hands it: B4's price (no zero-density bootstrap reaches B_ρ, fgT rF:31–32); F1 is binding (no two-sided sieve
   form); for U5-obstruction, V as a discrete rung-1 control with constant integer error and a real zero (§C C1).
2. **S7^{≤2}(3/5): Lemma H₇^{≤2} and an interval certificate of B^{≤2}** (lg UT-L0, UT-L2). Contract: "prove |N_P(u) − 0.6⌊u⌋| ≤ u^{0.40}
   for u > 10⁹ — with B^{≤2} certified in interval arithmetic this refutes U (K₇^{≤2}) — or prove the lower half fails (E ≤ −u^{θ} i.o. for
   some θ > 0.4022)". Price: 1 writer (theory) + 1 slot (arb certificate) + reads; one session. Stop line: a proof, a theorem that the
   cap's deficit grows past u^{0.4022}, or the arb box failing at X = 10⁹. Why second: the only above-threshold result whose follow-up is
   outside lemmaB's charter; read-O A2 says its downward half needs a NEW mechanism (inf E = −197.8 below the gap bound), and read-F
   ranks S8 above it because S8 has no downward half (lg rF:18).
3. **Feedback selection on Diamond–Zhang's grid, inside (17.46)** (dzh U-1 sharpened) [consolidator's reading; single-check]. dzh
   NOTE:72–74: DZ select by Lemma 17.2 "then argue deterministically", so every subsequence meeting (17.46) inherits (iii)–(iv): zeros on
   σ = 1 − 1/log t, α = 1. A selection that meets (17.46) AND tracks N to O(x^θ), θ < ½, refutes U — a weaker integer bound than B_ρ.
   Contract: "first rung, at the page: does (17.46) alone give DZ 17.14(iii)–(iv) for every subsequence? Then a deterministic rule on the
   grid with (17.46) and β < ½ (K), or a theorem that (17.46) forces β ≥ ½ (T, settling U-1)". The named obstacle: the deterministic grid
   P_det has β ≥ ½ from the prime-square branch point (2s − 1)^{−1/2} (dzh NOTE:42–44), so the rule must cancel it — as ℕ does by counting
   prime powers. Price: 1 writer + reads. Stop line: (17.46) does not carry (iv) deterministically (then the route is the random one only).
4. **Theorem 1.6 and Cor. 1.7 in Lean** (KICKSTART 10(d)'s third trigger). Contract: "a Comparator-style pair (10(j)) for Theorem 1.6 in
   discrete form (N a nondecreasing step function, N(u) − ρu ≥ r₀ > 0 and = O(u^θ) ⇒ a real zero of σ ↦ ρσ/(σ − 1) + σ∫R u^{−σ−1}du in
   [r₀/(r₀ + ρ), 1)) with an independent checker". Price: 2 slots, one session; elementary analysis (fgT rF:5–8). Why: the program's
   central lever after this wave, cheap to formalize; Lean never gates exploration (10(f)).
5. **The 𝒯 corner of Q_cond: a limit-periodic Hilberdink Prop. 3.4** (qtw rO A4; C2 Untried draft (b), applied). Contract: "close the
   rational part of 𝒯 by a limit-periodic version of Hilberdink 2012 Prop. 3.4 (T), or exhibit m ∈ 𝒯 with Π_ζ + log*(m) ≥ 0 on [1, Y] for
   growing Y whose D meets qtw A2's necessary condition (zeros on Re s = ½ when σ_S = ½) (K-candidate)". Price: 1 slot. Stop line: the
   probe's negative mass keeps growing with the atom count (rO A5) and a structural reason is written.
6. **Conjecture O past α_R/4: the unresolved Franel pairs** (conjO rO §7.3). Contract: "unconditional β₂(R) ≥ α_R/4 for every R, then a
   step past α_R/4 through b, b′ ∈ (√X, X], lcm > X; or the theorem that method X cannot pass α_R/4, with the rung-1 necklace (zoo I.11)
   as the control". Price: 1 slot. Why sixth: RELATIVE — by s37 Prop. 2.3 it cannot bear on ζ (α_R(ζ) = 0); only its refutation branch
   touches the line, and lemG A2 says a counterexample must be anti-clustered.
7. **Theorem 1.6 as a Siegel-zero criterion elsewhere** (fgT UT-F5): prior-art check first (Bateman–Grosswald, Rosser; number fields
   fail (A) by Ω₋ lattice-point results). Price: ½ slot (a scout). Instrument-grade.
Not ranked (Untried, §G): s5m UT-M2/M3 (S5's certified exponent past 0.383 — the candidate is withdrawn), lg UT-L3 (three unrun variants).
