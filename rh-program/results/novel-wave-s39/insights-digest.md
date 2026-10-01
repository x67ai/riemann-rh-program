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
   the orchestrator's recount `verify-F/recount_nK_F.log`, read-O's full-lattice count on its own sieve generator, A1, rO:295–297).
   read-O A5 (rO:311–313): c = 1.88 fails for every θ ≤ 0.351285; exact Rouché tolerance c < 1.8790.
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
proposed rider headline was narrowed accordingly. And F3 (rO:216–220): "S5(0.8) obeys α ≤ 2β if the exponent passes 0.383" needs
α = Re ρ₁, which the record has only as α ≥ Re ρ₁ under H_θ — now refuted.
Borrow. (a) The exact multiplicity lower bound f_G with a FIXED finite G — but note its ceiling: "no fixed finite G can refute" Lemma H in
its ≪ form, f_G(n) ≤ (1 + log₂ n)^{|G|} (NOTE:17–18). (b) A3–A4 (rO:301–310): T3's power-saving hypothesis cannot be dropped (R(x) ≍
x/log²x example), and infinite thin surgeries have unbounded gaps (never in Lagarias's Delone class). (c) §5.1's exact rule (n is a
g-prime iff A(n) = 0 and E(n − 1) ≤ 0.3) — already in the record (uoff read-O A1; F2(iii)).
Statuses. T1 (core in print), T2, T3 and its converse, Lemma A, T4, T4′: THEOREM (dual-read). K: dual-read computation (above). Exact
system to 2·10⁹ (max a_n = 344, sup E = 348.0): NUMERICAL (2 producers, byte-identical g-prime lists). Lemma H in the ≪ form: open.
UT-M4 (task 6, zeros of F_X at 10⁹): not run (stop line).
