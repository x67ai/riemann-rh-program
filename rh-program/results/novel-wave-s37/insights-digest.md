# Insights digest — Session-37 novel-approach wave 2 (KICKSTART 10(a)): how much additivity forces RH

Consolidation agent (Opus 5.5), 2026-10-01, Session 38. Brief: `DIGEST-BRIEF.md`. Inputs, in the brief's order: `WAVE-CHARTER.md`; per seed
`NOTE.md`, `read-F.md` (Fable 5.1, with `verify-F/`), `read-O.md` (Opus 5.5, with `verify-O/`), `SHARED.md`; the wave-1 digest and staged
zoo lines (`results/novel-wave-s36/`); `directions/README.md` and the Instruments/Untried tables of D1, B2, C2, C3; `BARRIER-ZOO.md` (745
lines, SHA-256 fa0d7293…, 62 entries); `results/conj-O-s38/BRIEF.md`, `results/qcond-s38/BRIEF.md`. SHA-256 prefixes of every input are in
`SHARED.md` block 0. Nothing here is new mathematics unless marked `[consolidator's reading]`; every other statement is quoted or pointed to.

Folders: `fe/` = seed M1a `beurling-fe`, `fr/` = M1b `beurling-frontier`, `pm/` = M2 `proof-mine`, all under `results/novel-wave-s37/`.
Line numbers refer to the NOTEs as on disk at 02:05 IST 2026-10-01 — every NOTE is POST-READ (pairs applied; `NOTE.pre-reader.md` kept):
fe/NOTE 41 470 B (F1, m1–m8, P1–P2 applied, §12 added at 02:01), fr/NOTE 53 943 B, pm/NOTE 43 838 B.
M1a's `read-O.md` was complete when read (verdict line and §1–§6 on disk at 01:59); all of its sections were used.
Status labels (as the reads leave them): **THEOREM (dual-read)** = proved in the NOTE and re-derived at the line by both read-F and read-O;
**THEOREM (dual-read, repaired)** = the same after a FIX-FIRST proof repair, now applied; **CONJECTURE (dual-read)**; **K**; **N**;
**single-check** = one model only. "Dual-read (O + orchestrator)" = read-O's addition re-derived by the orchestrator when it applied it.
Seed verdicts: M1a close T — read-F AGREES, read-O AGREES-WITH-CORRECTIONS. M1b close T (+ K on the pre-derivation's unconditional
clause) — read-F AGREES, read-O AGREES-WITH-CORRECTIONS. M2 close T — read-F AGREES, read-O AGREES-WITH-CORRECTIONS. No FIX-FIRST in the
wave falsifies a theorem; no read-F/read-O pair contradicts the other on a theorem's validity (the one disagreement is §E item E-M1a-3).

## §A Per seed

### A.1 M1a `beurling-fe` — is Spec Z rigid among Beurling systems with Riemann's FE? Close T, UPHELD (read-F:4 "AGREES"; read-O:7 "AGREES-WITH-CORRECTIONS … no FIX-FIRST against any theorem").

Three most useful findings.
1. **Theorem T (positive Hamburger)**, fe/NOTE.md:106–111 (proof 113–133, close 288–296): dN ≥ 0 carried by [1, ∞), polynomial growth,
   π^{−s/2}Γ(s/2)∫x^{−s}dN with Riemann's FE, poles only at 0, 1 (simple), growth (G′) ⟹ dN = ρΣ_{n≥1}δ_n. T1: the rational primes are the
   only discrete Beurling system with the FE; T2: no continuous or mixed one (polynomial growth now explicit, m2); T3: positive general
   Dirichlet series with frequencies ≥ 1 are multiples of ζ. Proof: the Fejér pairing gives ∫(sin πt/πt)²dN = 0 (fe/NOTE.md:120), then
   Siegel's periodicity. **THEOREM (dual-read)**. Novelty (read-O:10–12): "NOT in print in any source read (NEW, dual-checked; three bodies
   unverified, §3)"; the measure core is "a routine adaptation of Cohn–Elkies 2003 p. 695 plus Siegel's periodicity (Bochner–Chandrasekharan
   1956 p. 336) — not 'KNOWN', but not deep". Companion **Theorem T′** (two systems, ξ₁(s) = ξ₂(1 − s) ⟹ dN₁ = dN₂ = ρΣδ_n),
   fe/NOTE.md:337–348 — **THEOREM (dual-read: O + orchestrator)**, the positive answer to Hamburger's "f and g both general" problem.
2. **Theorem C (conductor ≥ 1, equality only for ζ) and the identity (C_q)**, fe/NOTE.md:215–227: ρ_q(1 − q^{−1/2}) = 2q^{−1/2}∫(sin(πt/q)/(πt/q))²dN(t).
   Both readers found it exact on the printed examples by Poisson summation: both sides equal √q − 1/√q for ζ(s)(1 + q^{1/2−s}) at every
   integer q (read-F §2; read-O §1(e) "(q−1)/√q exactly"), and 8.8 = 8.8 for F_{5,5} (q = 25). **THEOREM (dual-read)**. It locates the open
   question **Q_cond** (fe/NOTE.md:228–232): a Beurling system (dΠ ≥ 0) with Riemann's FE at conductor q > 1; every positive-coefficient
   solution found fails Λ ≥ 0 at powers of its largest frequency.
3. **Positivity is the rigidifying input — not the FE, not the gap** (read-O §6 R1, read-O:204–219; applied as fe/NOTE.md:247–255):
   F = 5^{s/2}L(s, χ₅) + D(s)ζ(s) has Riemann's exact FE, simple poles at 0, 1 only, every frequency ≥ √5/2 > 1, real signed coefficients,
   and a zero at s₀ = 1.32691215092364 + 33.2635142708346i. With the accounting R3 (positivity enters twice: linear growth and the vanishing
   step; the gap once; (G′) once — m1, fe/NOTE.md:130–133), T's hypotheses are each shown to bear load. Construction and self-duality
   **dual-read (O + orchestrator, fe/NOTE.md:247)**; the zero's location **single-check** (one producer, `fe/verify-O/o4`, `o4b`).

Most useful failure. The charter's least-squares exotic search (fe/NOTE.md:193–202): at double precision the theta relation on 42 points of
[½, 2] is fitted to RMS 1e−16 by {2, 3, 8.470247} and similar sets — "NUMERICAL NEAR-SOLUTIONS, NOT EXAMPLES": a generalized integer n enters
ψ with weight ≤ e^{−πn²/2}, below double precision for n ≥ 5. Their Fejér sums are 1.654343e−3 … 8.744635e−3 in closed form (read-O §2 o1)
against 0 exactly for Z. Lesson (fe/NOTE.md:200–202): Gaussian tests on a bounded range are exponentially blind to large generalized
integers; the Fejér function, whose transform decays like ξ^{−2}, sees every n_k with weight ≍ n_k^{−2}. `qcond-s38` task 2 is bound by it.

What the others should borrow. (i) The Fejér/Cohn–Elkies pairing as a detector of non-integral frequencies, with the closed-form Fejér
sum for Euler-factor modifications (read-O o1: S_F = Σ_e E(e)T(e), T(e) = Σ_{n≥1}sinc²(ne) by Poisson). (ii) Rigidity read as the equality
case of an LP inequality, and the defect as a positive form in the positions of the generalized integers (fe/NOTE.md:317–319; read-F
§4(c): "nothing is claimed about the zeros"). (iii) Hypothesis accounting — say where each input enters (R3); M1b's Conjecture O and M2's
class C lack a written one. (iv) The genus-1 F₅ admissibility scan (b_d ≥ 0 to d = 60 exactly for t ∈ {−5, …, 6}; RH-false admissible
t = ±5; fe/NOTE.md:266–270, confirmed by read-O o6) as the rung-1 calibration of any Q_cond inequality.

### A.2 M1b `beurling-frontier` — does integer regularity below the square-root barrier force RH? Close T with K on the pre-derivation's unconditional clause, UPHELD (read-F:4 "AGREES … the (K) … is CORRECT"; read-O:6–12 "AGREES-WITH-CORRECTIONS"; F1–F5, m1–m10 applied, fr/NOTE.md:3).

Three most useful findings.
1. **The price of a zero under surgery is integer error x^{α/2}.** Theorem B (fr/NOTE.md:215–238): Bernoulli thinning T_α (delete p with
   probability p^{α−1}) has a.s. N_P(x) − ρ_Px ≠ O(x^τ) for every τ < α/2 — unconditional. **THEOREM (dual-read, repaired by F2**: μ_R is
   the coprime convolution, not μ_w ∗ μ_η; read-O:48–55). Theorem C (fr/NOTE.md:296–322): a regular deletion of density c·p^{α−1} has
   β ≥ max(α/k_c, α − ½), k_c = min{k ≥ 2 : c/k ∉ Z}; for c ∉ Z already β ≥ α. **THEOREM (dual-read, repaired by F4)**; read-O:184–185:
   "NEW but elementary — … Landau's non-negative-coefficient argument". Data (§6.2–6.4): T_α exponents at α/2 on full windows (0.299 ± 0.010,
   0.357 ± 0.011, 0.456 ± 0.015 at 10¹⁰), reproduced by two independent re-runs (read-O §2.2 to 10⁸; read-F §2 to 10⁷).
2. **Theorem A / Corollary A′ (under RH)**, fr/NOTE.md:184–213: T_α is a.s. an [α, β]-system with α/2 ≤ β ≤ 1/(3 − α), and with padding by
   ℙ^{1/β} every ½ < α < 1, 1/(3 − α) < β < ½ is populated — strictly larger than BDR's region III (½ < α < 2/3, 2α/(α+2) ≤ β < ½).
   **THEOREM (dual-read, repaired by F3**, the grid of mesh X^{1−α/2}), conditional on RH; novelty NEW as statements (read-O:180–182).
3. **Conjecture U — the line, not a threshold**, fr/NOTE.md:454–466: every DISCRETE Beurling [α, β]-system has α ≤ max{½, 2β}. It implies RH
   ((P, N) is a [Θ, 0]-system); it contradicts BDR's printed populating conjecture on {β < ½, α > 2β}; read-O §4 made 11 attempts and did not
   refute it; U implies a quasi-GRH at level ⅔ for every quadratic field (read-F §4(b), read-O A2) and fails for continuous systems (m7).
   **CONJECTURE (dual-read)**, NEW (read-O:186–187). With it, Cor. 2.2 and Prop. 2.3 (fr/NOTE.md:86–102; **THEOREM (dual-read)**): a valid
   threshold β* implies RH and is ≤ 2/5; an obstruction β ≥ f(α) over all systems implies "no Θ in (½, a)" — any provable obstruction must be
   relative, and Conjecture O (fr/NOTE.md:268–278; **CONJECTURE (dual-read)**, proved for Bernoulli and regular c ∉ 2Z deletions) is that.

Most useful failure. The orchestrator's pre-derivation (charter §M1b) was wrong on its unconditional clause: "E[added − removed] = dν" treats
the deleted mean as absolutely continuous, but a deletion of actual primes has mean Σ_p w_pδ_p, whose Mellin transform is P(s + 1 − α) and
carries ζ's zeros shifted by α − 1 (Prop. 3.2, fr/NOTE.md:119–134). **K (dual-read)**, worded by read-O F1: "cannot be asserted
unconditionally (it is true under RH)". read-F §4(d): "found the pre-derivation wrong, correctly — the correction is a theorem, not a
loss". A second, smaller failure: the first draft omitted the [10⁷, 10¹⁰] window, where α = 0.75 gives 0.450 ± 0.009 — on Theorem A's
bound and 8σ above α/2 (read-O F5, fr/NOTE.md:408–412); finite-range sup-slopes carry a ±0.03–0.05 systematic (read-O §2.1).

What the others should borrow. (i) The one-scale anti-concentration of Theorem B (the conditional variance of the top dyadic block of
primes (x/2, x]); read-O A3 already ported it to Diamond–Zhang Thm 17.14 (β₀ = ½ a.s., single-check sketch). (ii) The Landau branch-point
test on the prime squares of a deleted set — a free lower bound for any structured surgery (M1a's Q_cond constructions are surgeries of ζ
at a conductor). (iii) The relative-obstruction frame (Prop. 2.3): an obstruction that holds over all systems is RH-hard; state it relative
to a surgery — M2's class-C question has the same shape (PNT-level existence vs RH-level rate). (iv) Statistics: the dyadic mean square,
which Theorem B and Prop. 5.1 actually bound, instead of running-sup slopes (conj-O-s38 task 3 adopts this).

### A.3 M2 `proof-mine` — the virtual-curve line in every proof of RH for curves. Close T, UPHELD (read-F:4 "AGREES"; read-O:7 "AGREES-WITH-CORRECTIONS … No number is wrong"; F1–F5, m1–m6, m9 applied, pm/NOTE.md:4).

Three most useful findings.
1. **Theorem P (the partition)**, pm/NOTE.md:266–288: each of the 10 proofs whose positivity step was read at the page (7 independent:
   Hasse, Weil–Rosati, Weil's correspondences, Mattuck–Tate–Grothendieck, Bombieri–Stepanov, Deligne Weil I, Weil II via Laumon)
   derives RH through exactly one inequality — I_A surface (def ≥ 0 on span(Δ, Γ_{πⁿ})), I_B family (Deligne (7.1) / Laumon purity), I_C
   coordinates (Bombieri's twisted counts), I_D group (deg ≥ 0, Rosati) — and V = (5, 5) violates each at an explicit place (def −2 and
   index (2, 2); α² = 13.090 > 11.180; 41 against "< 41" and "≤ 40" at Q = 25; deg(π − 2) = −1) while E₀: y² = x³ + 2x passes.
   **THEOREM (dual-read)**: read-O:11–13 "theorem-grade in each claim, survey-grade in scope"; the partition is by INEQUALITY, not by
   input (F3: in R3, R8, R9, R12, R13 the first object V lacks is a class-C object); (iii) "follows from V's existence alone" (m6).
2. **For g = 1 the four inputs are one zeta-level binary form**, pm/NOTE.md:65–67, 284–288: deg(m + nπ) = m² + tmn + qn² =
   ½def(mΔ + nΓ_π) = ½Tr((m + nπ)(m + nπ)†), the norm form of Q(π); its positivity is t² < 4q, i.e. RH for g = 1. V's form is the norm form
   of Q(√5) and represents −1 at π − 2 = φ, a unit of norm −1. So on rung 1 "every positivity proof proves the positivity of a zeta-level
   form from an object the zeta datum does not supply". **THEOREM (dual-read)** (read-F §1 (A), (D); read-O §2).
3. **Over Z only class C is not dead, and one-sided RH suffices there.** pm/NOTE.md:231–236 (§3 table), 303–318: A, B, D are REFUTED in
   their lattice / rationality / End forms and RH-RESTATED in their smeared / squeeze / positivity forms; read-O §4.1 grep: "the record neither
   kills nor bounds class C's integer-polynomial object". Lemma Z1 (pm/NOTE.md:238–249): ζ(σ) < 0 on (0, 1), so a one-sided bound
   ψ(x) ≤ x + Cx^θ gives ζ ≠ 0 on Re s > θ (Landau's oscillation theorem is the nearest object, m5). **THEOREM (dual-read)** for Z1; the
   record verdicts are lookups (dual-read). The live object: Gelfond–Schnirelman / Nair–Chudnovsky / Pritsker weighted capacities —
   "OPEN" at PNT strength (Pritsker 2013 p. 4, Problem 1.4, read at the page by both writer and read-O).

Most useful failure. The NOTE's "cheapest construction-or-refutation unit" for class C (Pritsker's B(w) over integer-Chebyshev product
weights) was pre-empted at the very page it quotes: Pritsker p. 4, "we did not observe a numerical improvement of the estimate (1.11) when
using further factors of the one-dimensional integer Chebyshev polynomials … beyond the factors x and 1 − x" (read-O F5, read-O:236–242).
With it, Lemma Z4's scope was overstated: FIXED finite supports have κ > 1, but SEQUENCES reach every 1 + ε (Diamond, Bull. AMS 7 (1982) §9
pp. 578–579, existence via the PNT; read-O F4) — so the Chebyshev sequence form is settled at PNT strength and RH-restated at RH strength.

What the others should borrow. (i) The "exact line" method: for any mechanism, name the first object the RH-false twin lacks, as a lemma,
with the numerical place of the violation and the control passing there. (ii) The twin-choice rule (pm/NOTE.md:320–330): two-sided and
positivity mechanisms are tested on V; one-sided mechanisms on V₂ = 1 − u + 11u² − 5u³ + 25u⁴ (non-real off-line roots; caught by
Bombieri's one-sided Theorem 1 at Q = 5⁶, 693 > 625) — **dual-read** (read-F §1; read-O o_twin). (iii) Lemma Z1's one-sidedness over Z,
which any auxiliary-integer or Beurling-side upper-bound route inherits. (iv) read-O's rate reframing (read-O §7(b)): a finite auxiliary
object is RH-relevant only through its RATE — error ≤ x^{1−δ} at scale x is a zero-free strip by Z1; PNT-level existence is not.

## §B Cross-seed propositions (numbered; one sentence each, then the evidence and the status as the reads leave it)

B1 (the wave's question at conductor 1). At conductor 1 the additive structure plus bare positivity determine everything — {dN ≥ 0 on
   [1, ∞), polynomial growth, Riemann's exact FE} has exactly the models ρζ, and with the Euler product exactly ζ — so the question "how much
   additivity forces RH" has a sharp answer there (the class has one member, no RH-false control, and therefore no leverage beyond a proof for
   ζ itself) and moves to conductor q > 1 (Q_cond) and to the (α, β) frontier. Evidence: Theorem T, T′ (fe/NOTE.md:106–133, 337–348);
   Theorem C, q = 1 only for ζ (fe/NOTE.md:215–227); fe/NOTE.md:306–316 as amended by m3 ("the multiplicative structure is never tested");
   read-F §4(b) (the scope sentence for the zoo line). Status: THEOREM (dual-read); the "no leverage" clause is the NOTE's reading, read by both.
B2 (the price of a zero; the line). Under surgery on the rational primes a zero at Re s = α > ½ costs integer error at least x^{α/2} —
   proved for random and for regular deletions, conjectured for every deletion — and RH is the endpoint β = 0 of the line α = 2β, not the
   β = 0 case of a threshold. Evidence: Theorems B, C (fr/NOTE.md:215–238, 296–322); Conjecture O (fr/NOTE.md:268–278); Conjecture U
   (fr/NOTE.md:454–466); Cor. 2.2, any valid threshold implies RH and is ≤ 2/5 (fr/NOTE.md:86–92); read-F §4(c): "integer regularity does not
   force RH at any fixed exponent β* … but the record's evidence points to a LINE, α ≤ max{½, 2β}". Status: THEOREM (dual-read, repaired) for
   B and C; CONJECTURE (dual-read) for O and U; U is a statement about DISCRETE systems only (m7: it fails for continuous ones).
B3 (rung-1 separation, and the one live class over Z). Every proof of RH for curves read at the page separates genuine curves from V
   through an object the zeta datum does not supply, and over Z only class C's inequality is not dead on the record, its RH-strength form being
   one-sided RH. Evidence: Theorem P (pm/NOTE.md:266–288); §3 table and "the one input" (pm/NOTE.md:231–236, 303–318); Lemma Z1
   (pm/NOTE.md:238–249); read-O §4.1 (29 grep hits, "none on the object"). Status: THEOREM (dual-read) for P and Z1; record verdicts dual-read.
B4 (the one-sided caveat for the rung-1 twin). The rule "a mechanism the virtual curve passes cannot be the generator" holds for two-sided and
   positivity mechanisms and fails for one-sided ones, because V's off-line reciprocal roots are real positive (a_r > 0 for every r) — test
   one-sided mechanisms on V₂ = 1 − u + 11u² − 5u³ + 25u⁴, and note that over Z the world V represents (a real zero in (½, 1)) is empty.
   Evidence: pm/NOTE.md:320–330; Z1(a)–(b) (pm/NOTE.md:239–242); read-F §4(b) ("a real correction to the control protocol"); read-O o_twin
   (111 genus-2 hits; 105 caught by (5) at some Q ∈ {5⁴, 5⁶, 5⁸}, 6 not). Status: dual-read.
B5 (T's hypotheses each bear load; the prices of an RH-false object with Riemann's Γ-factor). An RH-false object with Riemann's exact
   Γ-factor exists once any one hypothesis of Theorem T is dropped — positivity (the signed R1 solution), the pole structure (continuous
   systems with double poles at a, 1 − a), frequencies ≥ 1 (Nakamura's f(s, χ)), or conductor 1 (F_{5,5}) — and the only drop not yet
   paid WITH Λ ≥ 0 and a discrete system is conductor q > 1 (Q_cond; discrete systems with extra poles are the other open case, fe §8(d)).
   Evidence: fe/NOTE.md:247–255 (R1), 206–213 (§8(a), dΠ ≥ 0 iff a ≥ β), 238–244 (§8(d)), 278–285 (F_{5,5}: Λ(25)/log 5 = −14); Nakamura's
   f(s, χ) = 7^s·L(s, χ) + G(χ)·L(s, χ̄) (wave-1 digest §C4; its first term Σχ(n)(n/7)^{−s} has frequencies n/7 < 1 — [consolidator's
   reading], immediate from the quoted formula). Status: each item dual-read in its source; the synthesis is the consolidator's.
B6 (where the rung-1 twin lives on the Q side). The Q-side location of the virtual curve is conductor q > 1, not conductor 1: over F_q the
   completed zeta's "conductor" q^{2g−2} is minimal and rigid at g = 0 (Liouville) and V (g = 1) sits one step above; over Q the minimal
   conductor 1 is rigid (Theorem C) and T forbids a twin there. Evidence: fe/NOTE.md:262–277 (§9 (i)–(iii)); read-O §1(f) (genus 0 and
   genus 1 re-derived); read-F §4(b). Corollary on the controls: F_{5,5}'s Euler factor 1 + 5u + 5u² is the L-polynomial of the t = −5 genus-1
   datum over F₅ (same real parts 0.79899, 0.20101 as V), and over Q it sits on one prime, where it breaks Λ ≥ 0 (fe/NOTE.md:278–285).
   Status: dual-read.
B7 (the decisive object in each seed is a zeta-level quadratic form). Each seed's decisive quantity is a quadratic form fixed by the zeta
   datum whose sign or size is the content: the Fejér defect 2Σ_k sinc²(n_k) in the positions of the generalized integers (M1a — its
   vanishing is the rigidity), the norm form m² + tmn + qn² (M2 — its positivity is RH for g = 1), and the Franel/GCD kernel (m, m′)²/(12mm′)
   over the squarefree R-numbers (M1b — its diagonal dominance on dyadic ranges is Conjecture O in mean square); only the first is positive
   for free. Evidence: fe/NOTE.md:120, 317–319; pm/NOTE.md:65–67, 284–288; fr/NOTE.md:256–265 (Prop. 5.1, exact over a period); fr read-F
   §4(a) and fr read-O §7 (the kernel is positive definite, Σ_d J₂(d)(·)²; the open step is the pairs with lcm(m, m′) > X). Status:
   [consolidator's reading; single-check]; each ingredient dual-read in its source.
B8 (no Beurling-side threshold theorem is formal; the archimedean input decides the model, not RH). V has perfect integer regularity
   (A_n = (5ⁿ − 1)/4), the FE and RH false, so any threshold theorem over Q needs an archimedean input V lacks (fr/NOTE.md:287–294); M1a shows
   that the archimedean input "the integers have a gap (0, 1)", with positivity, is already decisive at conductor 1 — but it decides the
   MODEL (ζ), not the location of its zeros. Evidence: fr/NOTE.md:287–294; fe/NOTE.md:271–277, 306–316. Status: each half dual-read; the
   pairing of the two is [consolidator's reading].
B9 (Theorem P refines zoo III.20, and class C is its exception as worded). Classes A, B and D are III.20(B)'s positivity on a doubled
   object (C × C; tensor powers; endomorphisms as correspondences), while class C's inequality (Bombieri (5), (7), (8)) is proved on the curve
   C′ itself by Riemann–Roch dimension counts and "zeros ≤ poles" for one auxiliary function — no doubled object is used at the page — so
   III.20's "in every fully-proven RH case, BOTH hold" is true of every CASE (curves also have Weil's proof) but not of every PROOF.
   Evidence: pm/NOTE.md:120–136 (R6 chain at the page), read-O §1 row R6 "VERIFIED", §2 (C); zoo line 378 (III.20 STATEMENT). Status:
   [consolidator's reading; single-check] — staged for the zoo stream as a proposed clarifying rider (ZOO-LINES-STAGED block (iv)).
B10 (the orchestrator's working reading, sharpened by all three seeds). "RH needs the MULTIPLICATIVE structure … and the ADDITIVE structure
   of N … together" (charter line 19) becomes: the multiplicative structure can act only through what the additive structure leaves free —
   nothing at conductor 1 (T), the self-dual measures with a gap (−q^{−1/2}, q^{−1/2}) at conductor q > 1 (Q_cond), the integer error β in the
   frontier (a deletion pays x^{α_R/2}), and, on rung 1, an object outside the zeta datum (Theorem P). Evidence: B1, B2, B3, B6. Status:
   [consolidator's reading] — a summary sentence for the next briefs, not a claim.

## §C Controls — what each seed used, and flags on their use

C1 M1a. (a) The virtual curve (fe/NOTE.md:260–277): the genus-0 analog of T holds by Liouville without positivity; at g = 1 positivity
   (b_d ≥ 0) is cheap — the F₅ scan admits t ∈ {−5, …, 6}, Hasse only t ∈ {−4, …, 4}; RH-false admissible t = ±5 (t = 6 is Z ≡ 1); V is t = 5.
   (b) F_{5,5} (fe/NOTE.md:278–285): theta relation to 1e−60, (C_q) 8.8 = 8.8, Λ(5^k)/log 5 = 6, −14, 51, −174, 626, −2249. (c) Z itself:
   S_F = 0 exactly (read-O o1), theta defect 1.8e−40 (o2). (d) Near-misses 2 → 2.01, Olofsson's (ℙ∖{2}) ∪ {√2}, ℙ ∪ {1.5}: S_F = 2.049e−3,
   6.066e−2, 8.897e−2 (read-O o6). (e) Conductor-q examples ζ(s)(1 + q^{1/2−s}), q = 2, 4, 9, and read-O's new q = 5 example
   ζ(s)(1 + 5^{1/2−s}) + L(s, χ₅), coefficients 1 + χ₅(m) + √5·1_{5|m} ≥ 0 (o5: 4/√5 on both sides) — "a Selberg-class-free positive
   solution" failing Λ ≥ 0. (f) NEW control, read-O R1 (§A.1 item 3). FLAGS: the charter and wave 1 call F_{5,5} "the exact twin" of V; its
   factor is the L-polynomial of the t = −5 datum, not of V (t = +5) — same real parts, different datum (fe/NOTE.md:280–281); the double-
   precision least-squares search is not a control of anything (§A.1 failure).
C2 M1b. (a) The unmodified primes: sup|E| ≡ 1, slope 0.000, RMS 0.5773 = 1/√3 (fr §6.2; read-O §2.2). (b) The Cramér model (a full random
   discretization, β = ½ expected): 0.497 ± 0.006 over [10⁴, 2·10⁸], but its window range is [0.428, 0.628] (fr/NOTE.md:357) — the control
   itself shows the ±0.1 finite-window swing that read-O §2.1 later measured on every data set. (c) Finite R = {2, …, 13}: mean square 1.02299
   against Prop. 5.1's ρ·2⁶/12 = 1.022977 (read-O §2.2). (d) The mean system T(y) (gap G1): 0.117 / 0.247 / 0.390 against α − ½ = 0.10 / 0.25 /
   0.40 (fr/NOTE.md:368–372). (e) The virtual curve, used logically only: not an [α, β]-system over R (fr/NOTE.md:287–292). FLAGS: the
   c = 6 designs and c = 2 at α = 0.9 delete every prime below 88 / 1296 / 1024 and sit in the fundamental-lemma transient at X ≤ 10¹⁰ —
   uninformative, excluded (fr/NOTE.md:401–404); no control exists OFF the surgery class for Conjecture U (read-F P2: "the corner {β < α/2}
   is untested rather than empty").
C3 M2. (a) V = (5, 5) (pm/NOTE.md:40–43): N₁..₈, b₁..₈ exact; a_n > 2·5^{n/2} for every n. (b) E₀: y² = x³ + 2x over F₅, the unique short
   Weierstrass curve with trace 4 (pm/NOTE.md:44–47; read-O `o_trace4.log`), brute-force counts to F₆₂₅, twist sums 2(Q + 1) at Q = 5, 25,
   625 — passes every line. (c) V₂ (pm/NOTE.md:320–330), the twin for one-sided mechanisms. (d) Bombieri's printed formal example ω₁ = q,
   ω₂ = 1 (Bourbaki 430 p. 239: Z ≡ 1, no points, h = 0), which V sharpens (N_n ≥ 1, b_d ≥ 1, h = 1) — `[novelty: single-check]`
   (pm/NOTE.md:48–51). (e) Z-side checks: ζ(σ) < 0 at 99 points of (0, 1); #{n mod p² : n^p ≡ n} = p for the 29 primes < 110; C(2n, n)
   ratio 1.40532 → 1.38614 (n = 10³..10⁶). FLAGS: E₀ is the CM curve j = 1728, so class D's input is available for it (fine for a positive
   control, but it is not a "generic" genus-1 control); V₂ is "the first with a₁ = −1", not the first hit in any stated order (read-O m3);
   6 of the 111 genus-2 hits are not caught by Theorem 1 at Q ≤ 5⁸, so "non-real off-line roots" does not mean "caught early".
C4 Across the wave. All three seeds used the same rung-1 twin V in three roles — the function-field analog of a Beurling system one
   conductor step above the minimum (M1a), the witness that no threshold theorem can be formal (M1b), the common violator (M2). None used
   the wave-1 in-strip control F_{2.9,2}; M1a's F_{5,5} is in-strip (2√5 < 5 < 6). The Cramér model entered only M1b. No charter stop condition
   fired: M1a was settled by proof, not by print (fe/NOTE.md:323); M1b's simulation did not contradict the prediction at all three β₀
   (fr/NOTE.md:440–441); M2 found no proof that V passes — Dwork's theorem is rationality, which V has (pm/NOTE.md:340–341).

## §D Instruments rows — ready to append (column shape of every `directions/*.md` "Instruments" table; records, never ranks; files not edited)

Paths relative to `results/`. Status words are the sources'. No D1 row: nothing in the wave is interval-certified; read-O R1's zero
(C2 row 4) becomes a D1 candidate only after an Arb/interval producer.

→ `directions/C2-rigidity-conservation.md` (positive prime data with an exact FE: Theorem T, Theorem C, Q_cond)

| Quantity | Current best value | Result file | Dated |
|---|---|---|---|
| Fejér defect S_F = Σ_k c_k·sinc²(λ_k) of a positive Dirichlet series (Theorem T: Riemann's FE at conductor 1 forces S_F = 0, i.e. every frequency in N) | Z: 0 exactly (closed form). The charter's least-squares near-solutions K = 3..7: 1.654343e−3, 5.358231e−3, 2.612375e−3, 3.075454e−3, 8.744635e−3 (closed form by Poisson + Euler-factor convolution, atoms ≤ 1e10; the writer's truncated values sit 2e−7..1.4e−6 below; read-F 1.637e−3 at K = 3 to 10⁶). Near-misses 2 → 2.01, (ℙ∖{2}) ∪ {√2}, ℙ ∪ {1.5}: 2.049e−3, 6.066e−2, 8.897e−2. Three producers (writer, read-O, read-F at K = 3) | `novel-wave-s37/beurling-fe/NOTE.md` §4, §5(h), §7; `beurling-fe/verify/v1_theta_fejer_conductor.log`, `v2b_near_solutions_exposed.log`; `beurling-fe/verify-O/o1_fejer_exact.log`, `o6_extra_checks.log`; `beurling-fe/verify-F/rerun_conductor_identity.log` | 2026-10-01 |
| Conductor identity (C_q): ρ_q(1 − q^{−1/2}) = 2q^{−1/2}∫sinc²(t/q)dN(t), ρ_q = √q·Res_{s=1}F (Theorem C) | ζ(s)(1 + q^{1/2−s}): both sides = √q − 1/√q EXACTLY for every integer q (Poisson: Σ_{n≥1}sinc²(n/q) = (q − 1)/2); q = 2, 4, 9: 0.70711, 1.5, 2.66667. F_{5,5} (q = 25): 8.8 = 8.8 exactly. ζ(s)(1 + 5^{1/2−s}) + L(s, χ₅) (q = 5): 4/√5 = 1.788854382 both sides, Σχ₅(m)sinc²(m/5) = 0 to 2e−16. Theorem C dual-read; values three producers (q = 5 example: read-O only) | `beurling-fe/NOTE.md` §8(b); `beurling-fe/verify/v1_theta_fejer_conductor.log` Part 3; `beurling-fe/verify-F/rerun_conductor_identity.log`; `beurling-fe/verify-O/o5_conductor_new_example.log` | 2026-10-01 |
| Λ-sign of the known positive-coefficient solutions at conductor q > 1 (the Q_cond screen) | F_{5,5}: Λ(5^k)/log 5 = 6, −14, 51, −174, 626, −2249 (first negative at 25). ζ(s)(1 + q^{1/2−s}): mass −q^j/(2j) at q^{2j}, so Λ < 0 at high powers for EVERY q > 1; q = √2: Λ(8)/log 8 = 1/3 − 2^{3/2}/6 = −0.138. No Beurling system (dΠ ≥ 0) with an exact FE at q > 1 is known. Dual-read | `beurling-fe/NOTE.md` §8(b), §9 CONTROL 2; `beurling-fe/verify/v3_continuous_sketch_and_controls.log` Part C; `beurling-fe/read-O.md` §1(f) | 2026-10-01 |
| Signed RH-false solution of Riemann's exact FE at conductor 1 with every frequency > 1 (read-O R1: F = 5^{s/2}L(s, χ₅) + D(s)ζ(s)) | zero s₀ = 1.32691215092364 + 33.2635142708346i, \|F(s₀)\| = 5e−41, inside the half-plane of absolute convergence; FE partner 1 − s̄₀; argument principle on [−1, 2] × [0.5, 40]: 5 zeros, 3 on the line (t = 19.1868, 25.6164, 36.5260); theta relation 5.5e−40; ξ_F(s) = ξ_F(1 − s) to 1e−41; Res_{s=1}F = 1; smallest frequency √5/2 = 1.1180. Construction dual-read (O + orchestrator); numbers ONE producer (mpmath, 40 digits; not interval-certified) | `beurling-fe/read-O.md` §6 R1; `beurling-fe/NOTE.md` §8(e); `beurling-fe/verify-O/o3_signed_counterexample.log`, `o4_signed_rh_false.log`, `o4b_locate_offline.log` | 2026-10-01 |
| Continuous RH-false systems with Riemann's FE and extra poles (the orchestrator's sketch, ζ·G) | prime density f ≥ 0 iff a ≥ β (proved); min f on (1, 1e8] = 2e−9, 8e−4, 7e−11 for (β, γ, a) = (.8, 20, .8), (.8, 20, .9), (.6, 14.1, .6); −0.077 at a = 0.7 < β = 0.8; G(1 − s) = G(s) to 1e−27. An ENTIRE completed function is impossible (T2). Dual-read | `beurling-fe/NOTE.md` §8(a); `beurling-fe/verify/v3_continuous_sketch_and_controls.log` Part A | 2026-09-30 |
| Genus-1 admissibility over F₅ (L = 1 − tu + 5u²; the rung-1 calibration of any Q_cond inequality, `qcond-s38` task 3) | b_d ≥ 0 for all d ≤ 60 exactly for t ∈ {−5, …, 6} (scan t ∈ {−12, …, 12}); Hasse holds for t ∈ {−4, …, 4}; RH-false admissible t = ±5; t = 6 is Z ≡ 1. V = t = 5: N₁..₆ = 1, 11, 76, 451, 2501, 13376; b₁..₆ = 1, 5, 25, 110, 500, 2215; zeros at Re s = 0.79899, 0.20101. Two producers (writer v3; read-O o6 "exactly") | `beurling-fe/NOTE.md` §9 CONTROL 1 (ii); `beurling-fe/verify/v3_continuous_sketch_and_controls.log`; `beurling-fe/verify-O/o6_extra_checks.log` | 2026-10-01 |

→ `directions/B2-refutation-program.md` (the visibility price of an off-line zero in the integer counting function of a Beurling world — the IV.9 shape)

| Quantity | Current best value | Result file | Dated |
|---|---|---|---|
| Integer-error exponent β of Bernoulli thinning T_α (delete p with probability p^{α−1}; zero at s = α): running-sup slopes | Writer, X = 10⁹, 8 seeds, [10⁴, 10⁹]: 0.303 ± 0.008, 0.353 ± 0.013, 0.457 ± 0.012 (α = 0.60, 0.75, 0.90); X = 10¹⁰, 4 seeds: 0.299 ± 0.010, 0.357 ± 0.011, 0.456 ± 0.015; top window [10⁷, 10¹⁰]: 0.312 ± 0.015, **0.450 ± 0.009**, 0.476 ± 0.026. read-O (numpy, PCG64, X = 10⁸, 8 seeds, [10⁴, 10⁸]): 0.308 ± 0.008, 0.378 ± 0.012, 0.465 ± 0.016. read-F (X = 10⁷): 0.321 ± 0.030; 0.337 ± 0.013; 0.406 ± 0.025 (Y = 10⁹). Candidates α/2 = 0.300, 0.375, 0.450; 1/(3 − α) = 0.417, 0.444, 0.476. ± = seed s.e.; systematic ±0.03–0.05 (local two-decade slopes swing ±0.1–0.15). Controls: ℙ 0.000; Cramér 0.497 ± 0.006. Three producers; α = 0.75 top window OPEN between α/2 and 1/(3 − α) | `novel-wave-s37/beurling-frontier/NOTE.md` §6.2, §6.4; `beurling-frontier/verify/logs/fit.log`, `fit_big.log`; `beurling-frontier/verify-O/logs/fit_O_1e8.log`, `local_O.log`; `beurling-frontier/verify-F/rerun_thinning_numpy.log`, `rerun_thinning_numpy_Y1e9.log` | 2026-10-01 |
| Integer-error exponent of structured (greedy, \|π_R − F\| < 1) deletions of density c·p^{α−1} | c = 1, X = 10¹⁰: raw 0.238, 0.308, 0.395; slopes of log(M(x)·ln x): 0.302, 0.373, 0.459 — E ≈ x^{α/2}/log x; RMS 0.17–0.31 × √(ρQ/12) (random runs: 0.75–4.4×). c = 2, α = 0.6, X = 10¹⁰: 0.278 → 0.299 in [10⁷, 10¹⁰] (Theorem C allows α/3 = 0.20). Theorem-C branch term −0.206·x^{0.30}(ln x)^{−3/2} (α = 0.6) … 1%, 6%, 28% of sup\|E\| at 10¹⁰. c = 6 (α = 0.6, 0.75), c = 2 (α = 0.9): uninformative (fundamental-lemma transient). One producer (writer; logs audited by read-O) | `beurling-frontier/NOTE.md` §6.3, §6.4(5); `beurling-frontier/verify/logs/fit_big.log`, `greedy_logpower.log`, `analyze_extra.log`, `branch_constant.log`, `run_c2.log` | 2026-10-01 |
| Proved bounds on the frontier {α > ½, β < ½} (surgery on ℙ) | Unconditional: Theorem B β(T_α) ≥ α/2 a.s.; Theorem C β ≥ max(α/k_c, α − ½) for c ∈ Z (c = 1: α/2; c = 2: α/3; c = 6: α/4), β ≥ α for c ∉ Z; Prop. 3.2 β ≥ Re ρ + α − 1 if ζ has a zero with Re ρ > 1 − α/2. Under RH: Theorem A α/2 ≤ β(T_α) ≤ 1/(3 − α); Cor. A′ every ½ < α < 1, 1/(3 − α) < β < ½ populated (BDR Thm 1.3: ½ < α < 2/3, 2α/(α+2) ≤ β < ½). Any valid threshold β* ≤ 2/5 and implies RH (Cor. 2.2). Dual-read (A, B, C repaired by F3, F2, F4) | `beurling-frontier/NOTE.md` §2, §3.2, §4, §5.5; `beurling-frontier/read-F.md` §1; `beurling-frontier/read-O.md` §1 | 2026-10-01 |
| Mean-system error T(y) = Σ_{n≤y}Π_{p\|n}(1 − p^{α−1}) − y/ζ(2 − α) (gap G1 of Conjecture R) | X = 2·10⁸ sup-slopes 0.117 (window range 0.113–0.127), 0.247 (0.247–0.298), 0.390 (0.390–0.451) at α = 0.6, 0.75, 0.9; explicit-formula heuristic α − ½ = 0.10, 0.25, 0.40; proved contour bound (RH) 1/(4 − 2α) = 0.357, 0.400, 0.455. One producer | `beurling-frontier/NOTE.md` §4.4, §6.2′; `beurling-frontier/verify/logs/fit.log` | 2026-09-30 |
| Exact mean square of the integer error for a FINITE deletion R (Prop. 5.1; the ladder rung of `conj-O-s38`) | (1/Q)∫₀^Q E(x)²dx = ρ·2^{\|R\|}/12, Q = Π_{p∈R}p, ρ = φ(Q)/Q (Franel's integral + Jordan's J₂); exact rational check on eight sets up to Q = 2310 (writer); R = {2, …, 13}: 1.02299 measured vs 1.022977 (read-O); sup\|E\| ≡ 3.547 there. Dual-read; "may well be classical" (fr/NOTE.md:479) | `beurling-frontier/NOTE.md` §5.1; `beurling-frontier/verify/logs/finite_R_variance.log`; `beurling-frontier/verify-O/logs/fit_O_1e8.log` | 2026-10-01 |

→ `directions/C3-geometric-substrate.md` (the rung-1 anatomy: where each proof of RH for curves separates the virtual curve from a curve)

| Quantity | Current best value | Result file | Dated |
|---|---|---|---|
| The virtual curve V = (5, 5) against each positivity inequality of Theorem P (control E₀: y² = x³ + 2x over F₅, the unique short Weierstrass curve with trace 4) | I_D: deg(π − 2) = −1 (E₀: 1); Rosati Tr((π − 2)(π − 2)†) = −2 (E₀: 2). I_A: def(Γ_π − 2Δ) = −2 (E₀: 2); inertia of ⟨C₁, C₂, Δ, Γ_π⟩ (2, 2) (E₀: (1, 3)); Cor. 1.6 \|1 − 6\| = 5 > 2√5 = 4.472; Castelnuovo–Severi fails on span(Δ, Γ_{πⁿ}) for n = 1..12. I_B: α² = 13.090 > q^{3/2} = 11.180, β² = 1.910 < 2.236 (E₀: 5); Rankin step holds at 2k = 2 (13.090 ≤ 25), fails at 2k = 4 (171.353 > 125). I_C: formal twist over F₂₅ has 41 points against (5) "< 41" and (7) "≤ 40"; (8) as printed fails at 5⁴ (801 > 701), 5⁶ (17876 > 16001); E₀'s twist 32, 612, 15392. Three producers (writer, read-F sympy, read-O disjoint code) | `novel-wave-s37/proof-mine/NOTE.md` §1, §2, §4; `proof-mine/verify/lines.log`, `baseline.log`; `proof-mine/verify-F/rerun_lines.log`; `proof-mine/verify-O/o_lines.log`, `o_fields.log`, `o_trace4.log` | 2026-10-01 |
| V₂ — the rung-1 twin for ONE-SIDED mechanisms (genus 2, non-real off-line roots) | L(u) = 1 − u + 11u² − 5u³ + 25u⁴; h = 31; N₁..₆ = 5, 47, 143, 507, 2950, 16319; b₁..₆ = 5, 21, 46, 115, 589, 2689 (N_n, b_d ≥ 5 to 40); \|α\| = 2.7138, 1.8425; zeros at Re s = 0.6203, 0.3797; Bombieri Theorem 1 passes at Q = 5⁴ (N − Q − 1 = −119), fails at Q = 5⁶: 693 > 625 (and (7): 16319 > 16212). Box \|a₁\| ≤ 20, \|a₂\| ≤ 60: 111 genus-2 data with non-real off-line roots, N_n, b_d ≥ 0, h ≥ 1; 105 caught by (5) at some Q ∈ {5⁴, 5⁶, 5⁸}, 6 not. Three producers | `proof-mine/NOTE.md` §4 (caveat); `proof-mine/verify/twin_g2.log`; `proof-mine/verify-F/rerun_lines.log`; `proof-mine/verify-O/o_twin.log` | 2026-10-01 |
| Chebyshev-type auxiliary integers F_x = Π_k(⌊x/k⌋!)^{c_k} (Lemma Z4; class C over Z) | κ = AT/(T − 1) > 1 for every fixed finite support; Chebyshev (c on 1, 2, 3, 5, 30; T = 6): A = 0.921292, κ = 1.105550; C(2n, n): κ = 2 log 2 = 1.386294; LP minimum of κ over supports div(M): 1.170533 (M = 6), 1.105550 (30 — Chebyshev's weights are optimal there), 1.073965 (210), 1.069854 (2310) — decreasing toward 1, consistent with Diamond 1982 §9 (sequences reach 1 + ε, via the PNT). Z3: log C(2n, n)/Σ_{n<p≤2n}log p = 1.40532, 1.39846, 1.38854, 1.38614 (n = 10³..10⁶). Z2: #{n mod p² : n^p ≡ n} = p for all 29 primes < 110. κ values three producers; LP minima ONE producer (read-O) | `proof-mine/NOTE.md` §3–§4 (Lemma Z4); `proof-mine/verify/z_side.log`; `proof-mine/verify-F/rerun_lines.log`; `proof-mine/verify-O/o_z4.log` | 2026-10-01 |

## §E Errata — every pair from read-F and read-O with its status, and the charter / pre-derivation errors the seeds caught

E.1 M1a (`fe/`; applied by the orchestrator at 02:01, fe/NOTE.md:3). All pairs are prose, hypotheses or record verdicts; no theorem changed.
- E-M1a-1 read-F P1 (Theorem C, the q < 1 case: drop "forcing 1/√q ∈ √qZ (1/q ∈ N)") — APPLIED (fe/NOTE.md:221–222). Residual prose slip
  introduced by the edit: "so μ̂_q = μ_q is 1/√q-periodic, so μ_q is 1/√q-periodic" (line 221) — cosmetic. read-O §1(e) re-derived the same
  step keeping "1/q ∈ N" (true when the atom exists, and unnecessary): no disagreement on validity.
- E-M1a-2 read-F P2 (headline ⟨μ, φ⟩ = ⟨μ̂, φ⟩ = ⟨μ, φ̂⟩) — APPLIED (line 24).
- E-M1a-3 read-O F1 (§8(e): the verdict "open" is FALSE — signed RH-false solutions with the gap exist) — APPLIED, "re-derived by the
  orchestrator" (fe/NOTE.md:247–255). THE ONE READ-F/READ-O DISAGREEMENT OF THE WAVE: read-F marked "§8(c), (d), (e) ✓ as printed"
  (read-F:16), checking the one-line frequency-inversion argument; read-O re-derived the verdict itself at the line, with a construction and
  a computed zero (verify-O o3, o4, o4b). read-O is the read that re-derives the point; a recorded verdict, not a theorem's validity.
- E-M1a-4 read-O F1′ (§10 successor question (3): "Classify the signed solutions … twisted and dilated Poisson combs") — PARTIALLY APPLIED:
  the content is in §12 (fe/NOTE.md:346–347), but §10 line 322 still reads the OLD "(3) The signed (complex-coefficient) general-frequency
  Hamburger problem with frequencies ≥ 1 (§8(e))", which now contradicts §8(e). Recommend applying the NEW text.
- E-M1a-5 read-O m1 (positivity enters twice) APPLIED (lines 130–131); m2 (T2 needs ∫x^{−σ}dΠ < ∞) APPLIED (109–110); m3 (the second
  axiom set has the models ρζ) APPLIED (308); m4 (42 log-spaced points) APPLIED (194); m5 (gate update) APPLIED (62–65); m6 (Cohn–Elkies
  p. 695 at the page) APPLIED (159–162); m7 (the third price: signed coefficients) APPLIED (315–316); m8 (novelty tags) APPLIED at §4 (133)
  and §10 (299) — but Theorem C's own tag in §8(b) (line 223) still reads `[novelty: single-check]` while line 299 extends the dual-checked
  tag to C: a residual inconsistency.
- E-M1a-6 read-O R2 → §12 Theorem T′ ADDED (fe/NOTE.md:337–348), re-derived by the orchestrator.
- Charter errors M1a caught (fe/NOTE.md §5(f)): (f1) charter item (1) writes μ = δ₀ + …; the mass at 0 is ρ = Res_{s=1}ξ_P, and ρ = 1 is a
  CONCLUSION (T1) — harmless. (f2) "expected tools: Lev–Olevskii; Serre–Stark …": none is needed for T; Serre–Stark is irrelevant at
  conductor 1. (f4) the orchestrator's Phragmén–Lindelöf worry (G = ζ_P/ζ entire "not automatic") — SUPERSEDED by T2, which needs no
  hypothesis on G. (f5) charter §0(f) "Beurling systems … no FE" — now a theorem at conductor 1. The orchestrator's continuous sketch
  (charter (5)) is CORRECT (§8(a)). Writer's own error, self-caught (fe/SHARED block 5): "q irrational: q = √2 has q² = 2 prime" — replaced
  by the q^{2k} argument (Λ(8)/log 8 = −0.138).

E.2 M1b (`fr/`; applied, fr/NOTE.md:3; `NOTE.pre-reader.md` kept).
- read-F P1 (Theorem B step (3): name the L² norm; read-F adds "/log x") — APPLIED in substance through read-O F2's NEW text
  (fr/NOTE.md:229, "(E Z²)^{1/2} ≪ … ≪ x^{α−1}"); read-F's sharper /log x not carried (harmless). read-F P2 (Conjecture U: "every construction
  on the RECORD … the corner {β < α/2} is untested rather than empty") — APPLIED as status (f) (lines 461–463).
- read-O F1 (K wording: "cannot be asserted unconditionally (it is true under RH)") APPLIED (130–131, 430–431); F2 (Theorem B: coprime
  convolution T_d, κ_p → ρ_P) APPLIED (219–234, 245); F3 (Theorem A (i): grid of mesh X^{1−α/2}) APPLIED (192–193); F4 (Theorem C: the j = 1
  term; c ∉ Z gives β ≥ α) APPLIED (300, 308–309); F5 (the omitted [10⁷, 10¹⁰] window) APPLIED (408–412, 437–440); m1–m10 APPLIED; m11
  (Ingham / MV I not on disk; the `[recalled, unverified]` label stays) — no change, by design.
- A tension in the data, not an erratum: read-F's rung (X = 10⁷, [10⁴, 10⁷]) puts α = 0.75 at 0.337 ± 0.013, 8σ BELOW 1/(3 − α) = 0.444;
  the writer's top window [10⁷, 10¹⁰] puts it at 0.450 ± 0.009, ON it. Different windows; the question is open and is `conj-O-s38` task 3.
- Charter / pre-derivation errors M1b caught: (a) "E[added − removed] = dν" is impossible as stated (an atomic deleted mean cannot cancel
  an absolutely continuous ν; fr/NOTE.md:119–122); (b) "h … analytic for Re s > β₀/2 a.s." holds for the fluctuation only; for the mean it
  is equivalent to a quasi-RH (K, Prop. 3.2); (c) "[β₀, β₀/2]-systems for every β₀ ∈ (½, 1)" — unconditionally K; under RH only
  β ≤ 1/(3 − β₀) is proved and β = β₀/2 needs G1 + G2 (Conjecture R); (d) the construction is BDR §5's own (fr/NOTE.md:106–108) — the novelty
  is in the analysis only; (e) charter §0(f) "Beurling systems … integer error exponent β ≥ ½" is imprecise: {α > ½, β < ½} is populated
  under RH (BDR Thm 1.3) and, non-constructively, unconditionally (Prop. 2.1) — the same imprecision sits in zoo I.2(b) ("β < 1/2 only under
  RH"), corrected in the staged I.2 rider.

E.3 M2 (`pm/`; applied 2026-10-01, pm/NOTE.md:4; `NOTE.pre-reader.md` kept).
- read-F P1 (§0: keep the two statuses, "dead … in their lattice / rationality / End forms and RH-restated in their smeared / squeeze /
  positivity forms") — APPLIED (pm/NOTE.md:26). read-F P2 (add Diamond–Erdős 1980, recalled) — SUPERSEDED by read-O F4, which read Diamond,
  Bull. AMS 7 (1982) §9 at the page; applied in F4's form (lines 297–301).
- read-O F1 (Hrushovski pages 3/10/114 → 4/11/115) APPLIED (213–216); F2 (the count: 10 proofs with the positivity step at the page, 7
  independent; R10 recalled at its positivity step; R11 a negative row) APPLIED (17–20, 266–267, 332–333); F3 (a partition by INEQUALITY; in
  R3, R8, R9, R12, R13 the first object V lacks is a class-C object) APPLIED (20–22, 267–269); F4 (Z4: fixed supports only; sequences reach
  PNT) APPLIED (28–30, 297–301, 305–306, 337–338); F5 (the class-C unit pre-empted at Pritsker p. 4) APPLIED as a bracketed Session-38 note
  after the original unit text (316–318). m1–m6, m9 APPLIED; m7 (Hrushovski's |S·S^t| must be read signed for g ≥ 2 — a note on the source)
  and m8 (at Q = 25 the twist meets (8) with equality — "flagged only so no one 'fixes' it") — no change, by design.
- Charter / record errors M2 caught: (a) tournament T24's G-line ("the tower over F_{q^n} upgrades the bound to RH") is wrong at the page —
  Bombieri p. 239: the upper bound for all r never gives RH (ν_r = 0 satisfies it); the twists (8)–(10) give the lower bound; T24's verdict
  DEAD is unaffected (read-O §4.5 "the NOTE's flag is RIGHT"; replacement wording keeps the tower, m2, pm/NOTE.md:139–142). The tournament
  NOTE (`results/novel-wave-s36/tournament/NOTE.md` line 75) is not yet annotated. (b) The rung-1 twin rule of `tournament/read-F.md` §3 and
  zoo I.9 KILLS needs the one-sided caveat (B4). (c) Charter M2: "p-adic (Dwork/Kedlaya: only if a complete proof … is in print — check)":
  Kedlaya is complete and is Laumon transcribed (class B); Dwork is rationality only, which V has. (d) The charter's expected partition
  ("a surface with Riemann–Roch; a family with monodromy; honest sections + a Frobenius endomorphism; a group law") survives as A/B/C/D,
  but as a partition by inequality (F3). (e) The orchestrator's reader brief wrote "q − a + 1" for the degree at π − 2; it is deg(π − 1) =
  N₁ = 1 (read-O §2 (D)).

E.4 Errata to the wave-1 record surfaced by this wave.
- Zoo I.9 STATEMENT quotes "the exact twin of the control F_{5,5}" (from `tournament/NOTE.md` §2.1). With u = q^{−s}, F_{a,q}'s factor is
  1 + au + qu², the L-polynomial of trace t = −a; V is t = +5, so F_{5,5} is the Q-side twin of V's quadratic twist (t = −5; same real parts
  of zeros), not of V (fe/NOTE.md:280–281). Wording only; staged in the I.9 rider.
- Wave-1 digest §F survivor property (4) ("it fails at rung 1 on a single curve") and zoo I.9 KILLS ("a mechanism the virtual curve passes
  cannot be the generator") need the one-sided caveat (B4), staged.
- Zoo I.2(b) "β < 1/2 only under RH" — see E.2(e); I.2(d) (the discretization machine) cannot keep an exact FE (fe §8(d)) and cannot reach
  β < ½ (BDR p. 4, lines 171–179, fr/NOTE.md:54–55) — both staged in the I.2 rider.

## §F The survivor filter and the funding recommendation

F.1 KICKSTART 10(d), applied with the brief's three triggers (a theorem surviving two reads; a new Group-I control; a new conjecture that
implies RH). [KICKSTART's own list is "a new zoo Group-IV barrier, a lemma surviving two blind referees, or a Lean-checked statement"; the
second item is the brief's first. No Group-IV barrier and no Lean statement came out of this wave.] Graded ABOVE threshold:
- (a) **Theorem T** with T1–T3, T′ and Theorem C — two reads, no FIX-FIRST against any theorem (§A.1). It is also the one new Group-I entry
  candidate of the wave (a CALIBRATION bracket beside I.7; ZOO-LINES-STAGED block (i)). Follow-ups: Q_cond (U2); Lean (U3); read-O R4(2)
  ((G′) droppable?) and R4(4) (T′ at conductor q) — both Untried, the second folded into U2.
- (b) **M1b Theorems B and C (unconditional) and A, A′ (under RH)** — two reads, repaired (F2, F4, F3). Follow-ups: Conjecture O for all
  deletions (U1); the A3 lemma (U5a); G1 (U5b).
- (c) **Conjecture U** — a new conjecture that implies RH, dual-read, not refuted in 11 attempts (fr read-O §4). Follow-up: the refutation
  hunt, which has exactly one open surgery corner — integer c ≥ 2, α < ¾ (read-O A8) — inside U1, and a non-surgery, non-number-field
  corner (Untried UT-9, F.3).
- (d) **Theorem P** — two reads ("theorem-grade in each claim, survey-grade in scope"). Follow-up: class C over Z (U4, re-scoped).
- (e) **New controls**: read-O R1 (signed, RH-false, Riemann's exact Γ-factor, conductor 1, gap intact) — construction dual-read (O +
  orchestrator), zero single-producer — a Group-I control (clause of block (i)); V₂ (dual-read) — a rider on I.9.
Below threshold (recorded, not funded): Lemma Z1 (Landau's oscillation theorem in effect), Lemma Z4 (routine; Pritsker Prop. 1.3 in
effect), Prop. 5.1 ("may well be classical"), Props. 2.1–2.3 (routine), Prop. U and Lemma TB (second proof; Olevskii–Ulanovskii in spirit).
Consequence under 10(d): the Session-38 budget belongs to the follow-ups of (a)–(d) — which is what the two launched units are (U2 =
`qcond-s38`, U1 = `conj-O-s38`); every other lane stays paused and noted as paused in STATUS.

F.2 Ranking of the candidate next units (contract clause; price in agent-slots; stop line). Reads = the standing dual read (read-F by the
orchestrator + one Opus read-O slot) after each writer.
1. **U2 — Q_cond** (`results/qcond-s38/BRIEF.md`, LAUNCHED). Contract clause: "a Beurling system (dΠ ≥ 0) with Riemann's exact FE at some
   q > 1, verified by the Fejér test (a new Group-I control — the Q-side twin of V), or a rigidity theorem for every q in [1, Q₀] with the
   infeasibility certificate on disk (or for all q)". Price: 1 writer slot + 1 read-O slot + the orchestrator's read-F; one session.
   Stop line: the brief's (a printed theorem, a verified system, or a certificate for every q ∈ [1, Q₀], Q₀ ≥ 25). Why first: both outcomes
   are theorems; the construction branch gives the program's first Q-side control with {Euler product, Λ ≥ 0, exact FE} (B5, B6); the
   refutation branch extends B1 to every conductor (then {Euler product, Λ ≥ 0, exact Riemann FE at any conductor} has one model).
   Consolidator's notes for the unit: (i) the brief's q = 4 example is self-dual — FT(Σ_{n∈Z}δ_{n/2}) = 2Σ_{n∈Z}δ_{2n} and conversely, so
   Σδ_{n/2} + 2Σδ_{2n} is self-dual; it is the image of ζ(s)(1 + 4^{1/2−s}) with ρ_q = 3 [consolidator's check, Poisson]; (ii) read-O o5's
   q = 5 positive solution ζ(s)(1 + 5^{1/2−s}) + L(s, χ₅) (non-Euler, (C_q) exact at 4/√5) belongs in task 1's list; (iii) read-O R4(4)
   (can ρ₁ ≠ ρ₂ in T′ at conductor q?) is a one-paragraph side question for task 1; (iv) theta values on a bounded range are not a test
   (fe/NOTE.md:200–202); (v) rung 1: t ∈ {−5, …, 6} admissible, t = ±5 RH-false (C2 row 6).
2. **U1 — Conjecture O by the Franel/Landau mean-square route, with a structured-R counterexample hunt** (`results/conj-O-s38/BRIEF.md`,
   LAUNCHED). Contract clause: "β(R) ≥ α_R/2 for every set R of primes with Σ_{p∈R}1/p < ∞, with or without added generalized primes (T); or a
   structured R whose dyadic mean square M(X) ≪ X^{α_R−δ} over ≥ 3 decades together with a mechanism (K — refutes U inside surgery and
   confirms BDR's printed conjecture in the corner); or the exact missing mean-value lemma (G)". Price: 1 writer slot + reads; compute: one
   process at a time, ≤ 30 min per run; the 4–8 extra seeds of T_{0.75} at X = 10¹⁰ are the only heavy leg (the NOTE's 10¹⁰ runs peaked at
   2.5 GB). Stop line: the brief's (task 1 closes either way, or a structured R below X^{α_R−δ} over three decades). Why second: its proof
   branch is RELATIVE — by Prop. 2.3 it cannot bear on ζ, whose own α_R is 0 — so only its refutation branch touches the line α = 2β that
   contains RH; still the cheapest theorem-grade unit on the table. Consolidator's notes: (i) the refutation corner is A8 of fr read-O §4
   (integer c ≥ 2, α < ¾ — "the only surgery corner where a counterexample is not excluded by a theorem"); (ii) task 1's gap — a mean value
   in a strip where the Dirichlet expansion is unavailable — is the classical Carlson obstruction the brief already names; (iii) the α = 0.75
   top-window tension (§E.2) is decided by the dyadic mean square, not by more sup-slopes.
3. **U4 — class C over Z, RE-SCOPED** (pm read-O §7(c); the brief's U4 as written — "Pritsker's B(w) over product weights" — is pre-empted
   at Pritsker p. 4, read-O F5). Contract clause: "U-C1: the frontier of κ_c − 1 against the support size S(c) = Σ|c_k|log k for Chebyshev
   factorial weights (primorial M = 30 … 510510; Diamond's μ_T, T ≤ 10⁴) and the implied best error ε(x) at scale x — a numerical refutation
   of the power-saving form with the lemma to prove, or a zero-free-strip candidate to refute at once; U-C2: the same for Pritsker's B(w)
   with weights OUTSIDE the integer-Chebyshev family, after the prior-art gate (Pritsker's post-2013 papers; Montgomery, Ten Lectures ch. 10;
   Diamond–McCurley)". Price: 2 writer slots, sequential, one session each, + reads. Stop line: U-C1 — ε(x) ≥ x/(log x)^{O(1)} on the whole
   computed range, or ε(x) ≤ x^{1−δ}, or the Diamond §9 control fails to reproduce; U-C2 — Problem 1.4 settled in print, or a plateau of
   B(w_n) below 1 with an upper-bound proof. Why third: cheap and decisive for the one class not dead over Z (B3), but RH-relevant only at
   power-saving strength (Z1: a rate x^{1−δ} is a zero-free strip; PNT-level existence is not).
4. **U5a — Diamond–Zhang Theorem 17.14 has β₀ = ½ almost surely** (fr read-O §4 A3, §7(a)). Contract clause: "for almost every realization
   of the DZ construction (Bernoulli selection from the grid v_k = n + ℓ/2ⁿ), N_B(x) − k₂x ≠ O(x^τ) for every τ < ½ — the Theorem-B
   one-scale mechanism at α = 1". Price: 1 slot, one session. Stop line: the Theorem-B decomposition fails on DZ's grid (dependence across
   (x/2, x]), or a paper after BDR settles their footnote 4. Why here: it settles in print-grade form "the sharpest in-print test of U"
   (BDR p. 3 fn. 4, "Most likely the value of β₀ equals 1/2") — consistent with U — at the price of one slot.
5. **U3 — Theorem T in Lean (statement + stability clause).** Contract clause: "a Comparator-style pair (10(j)) for T's measure core in
   discrete form (a positive locally finite atomic measure on [1, ∞) whose even extension with the atom ρ at 0 is self-dual is ρΣδ_n) and,
   as the stability clause, the identity (F_R) 2∫sinc²dN = ⟨R, φ⟩ (fe/NOTE.md:238–244: non-integrality is paid by residual mass in the gap)
   [consolidator's reading of 'stability clause']; an independent checker (10(f))". Price: 2 slots (builder + checker), 1–2 sessions. First
   rung: grep Mathlib for Fourier transforms of measures / tempered distributions and for Poisson summation `[recalled, unverified]` that a
   Schwartz-class Poisson formula exists there. Stop line: the tempered-distribution layer is missing — then formalize the discrete core with
   C_c test functions and the Fejér pair only. Why fifth: T is already dual-read; Lean never gates exploration (10(f)); it would add the
   wave's one Lean-checked statement (a 10(d) trigger) at a price of two slots.
6. **U5b — gap G1 under RH** (fr/NOTE.md:249; read-O §7(c)): Σ_{n≤y}Π_{p|n}(1 − p^{α−1}) = y/ζ(2 − α) + O(y^{α/2+ε}), which lowers Theorem A's
   1/(3 − α) and, with G2, gives Conjecture R. Price: 1 slot. Stop line: a printed bound at ≤ y^{α/2+ε} for this squarefree-type sum is found
   (then it is a citation), or the contour abscissa α − ½ + δ cannot be crossed without a zero-density input. Why sixth: instrument-grade;
   it sharpens the frontier but does not move the line.
Not ranked (Untried, below): signed-solution classification, (G′) removal, extra poles, double pole, Conjecture R as a zero detector.

F.3 Untried — every idea in the three NOTEs and six reads not yet attempted (format of the directions' "Untried" lists; S1–S5 as in
STATUS "The specification for new machinery"; the fit reasons are this digest's reading of the cited lines, not new claims).
- **UT-1 Discrete Beurling systems with Riemann's FE and finitely many extra poles** (fe/NOTE.md:238–244; successor (2), line 320–322).
  S1–S5 fit: S1 (Λ ≥ 0 consumed); an RH-false member would be a control, not a mechanism. First rung: discretize the continuous systems
  of fe §8(a) (double poles at a, 1 − a) at small x (Broucke–Vindas style) and test the exact identity (F_R) 2∫sinc²dN = ⟨R, φ⟩ — a
  discretization either keeps it or visibly breaks it. Target: C2.
- **UT-2 Can (G′) be dropped for dN ≥ 0?** (read-O R4(2); fe/NOTE.md §5(d)). Fit: none of S1–S5 (hypothesis hygiene for T). First rung:
  F is bounded on Re s ≥ c > 1 and the FE controls Re s ≤ 1 − c; "the whole difficulty is the strip" — try Mellin inversion with the
  monotonicity of ψ in place of Phragmén–Lindelöf. Target: C2.
- **UT-3 Classify the signed solutions with the gap** (fe/NOTE.md:247–255; read-O F1′, R4(3)): is every one a finite combination of
  twisted and dilated Poisson combs? Fit: a control library for any test that consumes only the FE and the gap (they fail the Euler
  product; S1-negative); R1's member carries a known off-line pair (S2 calibration). First rung: even real primitive χ mod 5 (R1), 8, 12, 13.
  Target: C2 (controls); B2 (the zero as a live-fire target).
- **UT-4 The Fejér defect as a positive form, transported to the zeros** (fe/NOTE.md:317–319; read-F §4(c): "Recorded for the digest as an
  Untried entry, not as a route") — the concrete instance of wave-1's "Extremal characterization of ξ". Fit: S4 would be the whole content
  (a positivity generator in the zeros) and none is shown; S1 through dN ≥ 0. First rung: rung 1 — an LP inequality over positive zeta data
  on the norm group q^Z with equality exactly at genus 0, whose defect at g = 1 is a form in the Frobenius angles (V must violate it,
  E₀ satisfy it). Target: C2.
- **UT-5 Double pole at s = 1 with Riemann's Γ-factor** (fe/NOTE.md §8(f), "Not pursued"). Fit: a relaxation to a verdict; S1 marginal.
  First rung: (F_R) with R ∋ c₁ + c₂ log|t|. Target: C2.
- **UT-6 Gap G1 under RH** = ranked unit U5b (§F.2 item 6). Target: B2.
- **UT-7 Gap G2 — moments of the Bernoulli chaos Σ_d μ_η(d)T_d(x/d)** (fr/NOTE.md:250–251). Fit: instrument (a.s. uniformity; with G1 it
  gives Conjecture R). First rung: the degree-2 chaos at α = 0.6, where G1's data are strongest (0.117 against α/2 = 0.30). Target: B2.
- **UT-8 Conjecture R's unconditional form as a zero detector** (fr/NOTE.md:449–451: a.s. β(T_α) = max(α/2, Θ + α − 1)): thinning reads
  Θ through integer counts. Fit: S2 — one off-line zero of the base with Re ρ > 1 − α/2 lifts β above α/2 (the lower bound is Prop. 3.2,
  proved); S1 (the base's Λ ≥ 0 is consumed). First rung (a known answer, 10(b)): thin a Beurling base with a PLANTED zero (a discretized
  continuous system of zoo I.2(c)–(d)) and measure β against max(α/2, Re ρ + α − 1). Target: B2.
- **UT-9 Conjecture U off the surgery class** (fr/NOTE.md:480–482; fr read-F §4(b); fr read-O §4). Fit: S1 (discrete, Λ ≥ 0); a
  refutation is a new Group-I control, a confirmation is RH-hard (U implies RH). First rung: number-field ideal systems (BDR Rem. 5.3(3))
  as the known-answer calibration — quadratic fields have β_K ∈ [¼, ⅓] and U there is a quasi-GRH at level ⅔ (undecidable on the record);
  then non-number-field discrete constructions, of which none with α > ½ and β < ½ is known (fr read-F P2). Target: B2.
- **UT-10 The A3 lemma** = ranked unit U5a (§F.2 item 4). Target: B2.
- **UT-11 Is there any finite auxiliary-integer certificate of a zero-free strip?** (pm read-O §7(d)) — the question behind U4. Fit: S4
  (Chebyshev / Gelfond–Schnirelman positivity is not Weil's); S1: log⌊y⌋! = ΣΛ(n)⌊y/n⌋ and lcm(1, …, n) = e^{ψ(n)} pin Λ exactly, so the
  object passes III.4's parity test (pm read-O §4.1); S5: III.4 does not kill it. First rung: U-C1, with Diamond 1982 §9 as the known
  PNT-level control. Target: C3 (nearest; no direction owns class C — open a direction file only if U-C1 returns a candidate).
- **UT-12 The unread rows of Theorem P** (pm/NOTE.md:220–224, R14; R5; R10's positivity step): Manin 1956, Igusa 1949, Quigley 1953,
  Roquette 1953, Kani 1984, Weil II 1980, Stark's g = 2 refinement, Stöhr–Voloch; Stepanov 1969 and Schmidt; Weil 1949 (BAMS behind a
  bot wall — Firecrawl first). Fit: none of S1–S5 (survey completeness; "none is expected to open a fifth class, but that expectation is a
  guess, labeled as one"). First rung: Manin 1956 (class D expected) and Weil 1949 (R10's step). Target: C3.
- **UT-13 Prior art for Prop. 5.1** (a Franel-type exact mean square for sifted sets; "may well be classical", fr/NOTE.md:479). Fit: none;
  hygiene before `conj-O-s38` builds on it. First rung: Franel 1924 and the sieve-variance literature, read at the page. Target: B2.
Folded, not listed separately: T′ at conductor q (read-O R4(4)) → U2; eight more seeds at 10¹⁰, α = 0.75 (fr read-O §7(b)) → U1 task 3.
Wave-1's six Untried entries (wave-1 digest §F) remain Untried; wave 2 drew none of them, and UT-4 is the concrete instance of the first.

## §G The waste line (KICKSTART 10(o), with 10(m)'s three labels; from the three seed `SHARED.md` files and the six reads)

Spent on the wrong thing. M1b's three structured runs in the fundamental-lemma regime — greedy c = 6 at α = 0.6 and 0.75, and c = 2 at
α = 0.9 — which delete every prime below 88, 1296 and 1024, so that at X ≤ 10¹⁰ (u = log x/log y ≈ 3–4.6) the error is the sieve
transient, not an exponent: "these three runs are uninformative and excluded" (fr/NOTE.md:401–404). Label (i): obstruction stated and
re-derived — a design pitfall, not a zoo candidate; the missing input for the next structured design (`conj-O-s38` task 3) is "keep
c·p^{α−1} < 1 from the first prime, or start the fit window beyond the transient".
Caught before spending. M2's proposed class-C unit (Pritsker's B(w) over integer-Chebyshev products) is pre-empted at Pritsker p. 4
(read-O F5); funding it as written would have replicated a printed negative. The ranking above funds only the re-scoped U-C1/U-C2.
Found nothing, correctly (not waste). M1a's least-squares exotic search (its null is Theorem T's content, and it fixed the Fejér-versus-
Gaussian lesson, fe/NOTE.md:200–202); M1b's add/delete surgery, never simulated because Prop. 3.2 refuted its unconditional form first
("found the pre-derivation wrong, correctly", fr read-F §4(d)); M2's Dwork row (rationality, which V has; not a proof of RH, pm/NOTE.md:179–181).
(ii) budget / tool / time — re-queued with the missing input named. M1a: the arXiv export API timed out all session (HTML search used;
fe/SHARED block 2); bodies not read — Bochner–Chandrasekharan 1956 beyond p. 336, Chandrasekharan–Mandelbrojt 1957, Córdoba 1988/89,
Lagarias 1999 (JSTOR / De Gruyter access). M2: Weil 1949 BAMS (bot wall — Firecrawl), Stepanov 1969, Schmidt, Mattuck–Tate 1958,
Grothendieck 1958, Weil 1948a/b, Katz's Weil II lectures (library access) → UT-12. M1b read-F: the cheap rung α = 0.9 at Y = 10⁸ was
flattened by the ρ tail (std ≈ 9·10⁻⁶) and re-run at Y = 10⁹ (fr read-F §2).
(iii) unexplained — none. Self-corrections, each explained in its log: M1a's "q = √2 has q² = 2 prime" slip (fe/SHARED block 5); M1a
read-O's first o4 grid keyed by floats missed the zero (fixed, logged in the script); M2's R8 misapplication of Laumon Cor. (4.3.1.1) to a
sheaf ramified at ∞ and R10's root-level form relabeled `[recalled, unverified]` (pm/SHARED block 8); Milne page numbers (block 7).
Candidate LOG line: "Spent for nothing: M1b's three fundamental-lemma-regime structured runs (c = 6 at α = 0.6, 0.75; c = 2 at α = 0.9),
because (i) the design put X inside the sieve transient (stated and re-derived, fr/NOTE.md:401–404; not a zoo candidate). Found nothing,
correctly: M1a's least-squares search, M1b's never-run add/delete surgery, M2's Dwork row. Caught before spending: M2's pre-empted class-C
unit. (ii) re-queued: paywalled and walled sources (UT-12; BC56, CM57, Córdoba, Lagarias 1999)."
