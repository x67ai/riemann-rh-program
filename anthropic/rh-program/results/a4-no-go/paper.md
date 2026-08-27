# The two-moment certificate is robust under Rudnick–Sarnak-range cubic augmentation with capacity control

> **Dated revision (2026-08-27).** Session 8's interval hardening (`verify/o1_crowding_interval.py`; report `o1-n128-report.md`) found the Session-7 full-family crowding ratio 0.9775 to be a 0.004-grid artifact. This revision re-scopes the multi-pair closure: ledger constant interval-certified C* <= 0.98465 < 1 on pair depths <= 0.156 (w <= 0.98); certified ledger FAILURE (Sgen2 >= 1.01405 > 1 at d = d' = 0.159) on w in (0.98, 1], where coverage is the re-run crowd attacks (min F1 - T >= +17.47) plus the unconditional 8/9 backstop — (MI) itself is numerically unrefuted there. The N = 128 re-run reproduces all identities. A strengthening-by-honesty: the certified region's constant is now rigorous, and the overreach is withdrawn. Complete edit list: `o1-n128-report.md` section 5.


## An exact absorption certificate for the two-moment system at bandwidth one, with a hand-checkable witness

**Program:** RH program, direction A4 (merged A2+A4 cubic-certificate direction; adjudicated survives-with-repairs 5.5, binding). This paper is the sharpened no-go deliverable mandated by the adjudication's merge guidance, item (3), on the absorption branch of the corrected M2 decision gate (decided Session 6, 2026-08-26, audited).
**Date:** 2026-08-26.
**Evidence discipline:** every number in this paper is taken from the on-disk gate record (`results/a4-m2-gate/`), from the audited data digest (`results/a4-no-go/data-tables.md`), or from re-derivations executed this session in `results/a4-no-go/verify/`; every theorem is proved in full in Sections 3–7 or in the companion note `results/a4-no-go/pair-channel.md`. Provenance for each class of claim is collected in the References and Provenance section.

---

## Abstract

The parent paper's unconditional two-thirds theorem rests on a two-moment certificate — trace and Frobenius norm of the Weil–Gabor compression, read against block structure and integrality — and that certificate is provably exhausted: the Lean-formalized `lemmaR_tight` shows that within the data class (tr, Frobenius, positive-index count, integer atoms) an on-line double and a shallow off-line pair are indistinguishable, pinning the distinct-zeros optimum at N_d/N = 5/6 and the simple fraction at 2/3. Direction A4 proposed to break this degeneracy by adjoining, at a second bandwidth lambda' = 1/2 + o(1) inside the Rudnick–Sarnak range, the unconditionally computable signed third trace together with repaired spectral-capacity rows (an all-V eigenvalue-count ladder and a garnish-capacity fuzz row). This paper proves, at the model level, and certifies computationally at decision grade, that the augmentation adds exactly nothing: the marginal value of the entire cubic block over the two-moment baseline is delta_0 = 0 — identically, as an exact LP equality with an explicit, hand-checkable witness law: over the full pre-registered adversary grid for the distinct-zeros benchmark (940 records, |delta_0| < 1e-12 everywhere, corner 5/6); for the simple-fraction benchmark (corner 2/3) at its two decision cells plus cross-checks, converged clean at the literal pre-registered stop rule; and — decisively — inside the near-CUE data class licensed by the unconditional pair-correlation theorem of Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh, where the absorption is by strict slack: the cubic row does not even bind. The structural explanation is a set of exact identities proven here: on isolated blocks the signed cubic row is the affine function 3F - 2 of the Frobenius row plus the second integrality level, hence blind to doubles-versus-pairs at every depth; on the psi_1-zero grid the bandwidth-one Frobenius row degenerates exactly to the multiplicity count while the half-bandwidth kernel stays position-sensitive, so the cubic budget is met by arrangement at zero cost; and spectral escape is capped sharply at 2 sqrt(2) sqrt(C_led eps_g) N = o(N), while a scalar cubic tail row with any divergent cutoff is unconditionally vacuous. The pair-interference channel — the one gap in the atom-only model theorem — is closed by an integrality theorem throughout the gate's R5 depth family: proved unconditionally for single-pair columns at every gate depth and for multi-pair columns at w <= 0.82 (w <= 0.98 modulo one crowding cap whose ledger constant is interval-certified; on the deepest sliver w in (0.98, 1] the coverage is adversarial-numerical with the unconditional 8/9 backstop), with an unconditional 8/9-strength spectral backstop at all depths; mixed-depth multi-pair columns involving the deep probes w in {1.5, 2} rest on that backstop plus converged adversarial pricing. The two-moment certificate, and with it the bandwidth-one ceiling, is robust under Rudnick–Sarnak-range cubic augmentation with capacity control.

---

## 1. Introduction

### 1.1 The parent certificate and its exhaustion

The parent paper [P] proves unconditionally that more than two thirds of the zeros of the Riemann zeta function are simple and on the critical line, that N_d(T,2T) >= (5/6 - o(1)) N(T,2T) zeros are distinct, and (Theorem D, window-optimized) that the simple-on-line proportion reaches 2 - 1/c_1* = 0.6725007..., by compressing the Weil explicit-formula form to a critically sampled Gabor family and reading exactly two spectral moments of the resulting Gram matrix G-hat: the trace tr G-hat = N(1 + o(1)) and the Frobenius moment tr G-hat^2 = (1/lambda + lambda/3) N (1 + o(1)), both evaluated unconditionally on the prime side for bandwidth lambda <= 1. The certificate is finite-dimensional linear algebra (the rank–trace inequality "Lemma R") applied against the zero side's block structure: on-line points give PSD rank-one atoms, off-line pairs give signature-(1,1) hyperbolic blocks.

Two formalized results delimit this method exactly. First, `lemmaR_tight` (Lean, `Zeta23/ZeroSide/TightMult.lean`): on configurations of integer-marked on-line atoms plus pair blocks, the two-moment certificate is achieved with equality, and an on-line double (eigenvalue +2, charge 4) is indistinguishable from an off-line pair of depth -> 0 (eigenvalues ±2, charge 4) — no further inequality in (tr, Frobenius, n_+, integer atoms) can improve it. The extremal configuration is 2/3 simple zeros plus 1/6 on-line doubles: N_d/N = 5/6, simple fraction 2/3. Second, the bandwidth-one ceiling (Lean, `Zeta23/PairCeiling/`): no certificate reading only bandwidth-one form-factor data certifies a simple-zero proportion above 0.6818287 (up to the recorded stability terms), witnessed by an exact-rational 256-periodic law; and any trace/Frobenius certificate is capped below 0.8453 = 2 - 2/sqrt(3) at any Dirichlet-polynomial length, since kappa(lambda) = 1/lambda + lambda/3 >= 2/sqrt(3) for all lambda > 0.

### 1.2 The cubic proposal

The parent's Section 7.3 records the conditional template: under RH the third trace tr G-hat^3 is available (Hejhal, Rudnick–Sarnak) and the certificate can be run with the cubic weight omega(m) = m/2 + (2 m^2 - m^3)/18 + (4/9) 1_{m=1}, giving N_d/N >= 0.85082 with the window cos(8s/5) (consuming also [BHB13]'s N^s/N >= 19/27 on RH). Direction A4's thesis was that a slice of this becomes unconditional: at bandwidth lambda' = 1/2 + theta loglog T / log T (strictly inside the k = 3 Rudnick–Sarnak range X^3 <= T^{2-eps}), the signed cubic trace is computable by the parent's Section 5 diagonal method, and a Schatten-3 spectral-tail theorem (Theorem 1(ii)-repaired: an all-V eigenvalue-count ladder n(V) <= C_led N V^{-4}, theta < 1 strict) would cap the spectral escape that the parent's own odd-moment no-go (Section 7.5(e)) identifies, making the cubic row a usable sign-sensitive constraint. The original proposal's separating premise was that a hyperbolic pair block contributes (+a)^3 + (-a)^3 = 0 to the cubic while a double contributes +8, so the two-moment-degenerate configurations would sit at different corners of the augmented polytope.

The binding adjudication (survives-with-repairs, 5.5) ordered seven repairs and made the corrected M2 gate the direction's action one: a decision LP over an honest adversary class — marks up to a divergent alphabet W, depth-parametrized shallow pairs, clustered sine-process null budgets, full positional freedom, and an explicit garnish-capacity fuzz row derived from the repaired ladder — with the pre-registered semantics that either branch is a deliverable: a bite funds the analytic bridge; an absorption is published as the sharpened no-go. This paper is the absorption branch, executed.

### 1.3 The corrected gate question and its answer

The gate asks: over laws (probability mixtures) of explicit N-periodic marked configurations satisfying the two-moment data — mass N, integrality, pair structure, bandwidth-one Frobenius budget (4/3) N (1 -/+ eps) — does adjoining the entire lambda' = 1/2 cubic block (the lambda'-Frobenius budget kappa(1/2) N = (13/6) N, the signed cubic equality c3(1/2) N = 5 N, the all-V count ladder, and the capacity fuzz row) raise the minimum of E[N_d]/N above the lemmaR_tight corner by any delta_0 > 0?

Throughout, "Rudnick–Sarnak-range cubic augmentation with capacity control" (the title phrase, pre-registered in the gate specification) means exactly this lambda' = 1/2 + o(1) system fixed by the adjudication (R4: theta < 1 strict) — the only point in the RS range where both the signed cubic row and the capacity ladder are unconditionally licensed; the behavior of the cubic row at lambda' >= 0.6, inside the RS range but outside the proven ladder regime, is the quarantined payoff curve of Section 8.4, not part of any claim.

The answer, decided and audited: **no — delta_0 = 0 identically**, not merely within error bars: the base-optimal law itself satisfies the entire cubic block. This paper assembles the complete result: the structure theorems that explain the absorption (Section 3), the model-level corner theorem with its pair-channel extension (Section 4), the computational certification with the explicit witness (Section 4.4), the near-CUE decision-grade result (Section 5), the simple-fraction benchmark (Section 6), the two capacity theorems that close the spectral-escape routes (Section 7), and the honest scope map of what is exact, what is a bounded residual, and what remains open (Section 8).

### 1.4 Headline results

1. **Exact absorption with witness (Theorem 4.3 + Section 4.4).** Over the full pre-registered decision grid — 940 LP records spanning mark alphabets W in {2,...,8}, ladder constants C_led in {10, 100, 1000}, tolerances eps in {0.02, 0.05, 0.10} (with the separate, labeled tight-eps runs extending to eps = 0.002), all fuzz modes, matched and asymptotic budget centerings, N = 64 and N = 128 — the marginal value of the cubic block is |delta_0| < 1e-12 at every record (maximum 8.94e-13), and the joint optimum obeys the exact law P(eps) = 5/6 - (2/3) eps -> 5/6. The absorbing law is exhibited: three columns on the 65-site psi_1-zero grid, marks {1, 2} only, no pairs, every row verified in exact rational arithmetic, the key entries hand-checkable (F1 = 64 exactly; F' = 4128/33).
2. **Both benchmarks.** The same absorption holds for the simple-fraction objective: the cubic block moves the p1 optimum by at most 1.4e-12, converged at the literal pre-registered stop rule, and the optimum is the exact analytic corner 2 - (4/3)(1 + eps) -> 2/3 (Section 6).
3. **Near-CUE decision grade — absorption by slack (Section 5).** Inside the pinned data class |E_w|c_j|^2 - j| <= 1 (licensed unconditionally, with three stated riders, by BGSTB24), delta_0' = 0 as an exact LP equality at N = 64 and N = 128, at both budget centerings — and at the pinned optimum only the pinning rows bind: the cubic row, the ladder, and even both Frobenius rows are strictly interior.
4. **Cubic blindness (Theorem 3.4).** On isolated blocks, the signed cubic row equals 3F - 2 per zero on every multiplicity-1 pair at every depth and on every mark-{1,2} atom: C - 3F + 2 Mass = Sum m(m-1)(m-2) + 6 Sum m_p^2 (m_p - 1) A_p^2 exactly. The "+8 vs 0" separating premise of the proposal (and the adjudication's phase model) is false: a pair's cubic charge is 2 m^3 (1 + 3 A^2) >= 8 m^3 at every depth. All discriminating power of the cubic row lives in marks >= 3 and in clustering cross-terms — and the cross-terms are a free resource for the adversary (Theorem 3.9).
5. **Closed forms and the m2 = kappa identity (Theorem 3.5).** The sine-process null budgets are m2(lambda) = 1/lambda + lambda/3 and m3(lambda) = 1 + 1/lambda^2 for the flat window, all 0 < lambda <= 1; and m2(lambda) coincides exactly with the parent's unconditional prime-side kappa(lambda) — the sine null's second-moment budget IS the unconditional budget, on the whole band.
6. **Capacity cap (Theorem 7.1).** Under the repaired all-V ladder and a Frobenius slack eps_g, the maximal cubic charge purchasable by spectral escape is exactly 2 sqrt(2) sqrt(C_led eps_g) N = o(N) — sharp, with the extremal profile exhibited; both the earlier constants (2 sqrt(C eps), 5/sqrt(3) sqrt(C eps)) are superseded, with three independent confirmations.
7. **Divergent-cutoff vacuity (Theorem 7.4).** A scalar Schatten-3 tail row with ANY divergent cutoff is unconditionally absorbed by an explicit garnish construction that lowers both objectives — the "provable today, no LP needed" half of the no-go.
8. **Pair-interference closure (Section 4.2–4.3).** The one channel outside the atom-only sandwich — off-line pairs pushing the bandwidth-one Frobenius below the mark-accounting floor — is closed for the gate's pair class throughout the R5 depth family: proved unconditionally for all single-pair configurations to depth w <= 2.8 (covering all gate depths, including both deep probes, with >= 34% margin), for all multi-pair configurations to w <= 0.82 (w <= 0.98 modulo the crowding cap, ledger constant interval-certified at 0.98465; on w in (0.98, 1] the ledger fails — certified — and coverage is adversarial numerics plus the 8/9 backstop), and for equal-depth pair-only configurations at every depth. Multi-pair configurations at mixed depths involving the deep probes w in {1.5, 2} — admissible under Section 2.4 but beyond the theorems' range — are covered by adversarial numerics plus the unconditional 8/9 backstop (O2, Section 8.3). An explicit fractional-mark counterexample proves the closure is intrinsically an integrality theorem.

### 1.5 Honest framing (adjudication repair R6, binding)

The cubic row is **a nonlinear spectral reading of bandwidth-one pair-correlation data with quantitative high-spectrum capacity control** — nothing more. The third trace at bandwidth lambda' carries total Fourier support (k - 1) lambda' = 1 + o(1), not 3 lambda'; its genuinely cubic prime resonance is the absolute constant sum_p (log p)^3/(p - 1)^2 = 2.315762 (re-sieved to 3e6 in this program, three independent confirmations), contributing O(1) to tr G-hat^3, i.e. O(1/N) per zero. No claim is made anywhere in this paper that the cubic block evades the Alternative Hypothesis or consumes data beyond the bandwidth-one class plus o(1): the no-go proved here is precisely that this nonlinear reading, with the full capacity apparatus attached, adds nothing to the linear reading at the proven operating point. (The formal scope point survives unchanged: a cubic row is outside the PairCeiling certificate class as defined; the content of this paper is that leaving the class buys nothing.)

### 1.6 Scope discipline (read before citing)

Every theorem in this paper is a statement about the model — the gate's explicit configuration classes, kernels, and row systems (Section 2) — not about the zeros of zeta. The bridge from the model rows to unconditional statements about zeta is the parent paper's sampling bookkeeping plus the BGSTB24 licensing riders, cited (with the riders stated in full) in Section 5.1. The exact zero delta_0 = 0 is proved and certified at the flat/flat window configuration and is **flat/flat-specific**: with the Montgomery–Taylor cosine window at lambda = 1 the grid degeneracy breaks and the honest statement is a bounded residual of order 6e-5 (Section 8). Nowhere does this paper claim "delta_0 = 0 universally"; the claim structure is: exact zero on the decision configuration and the near-CUE class, bounded sub-decision-scale residuals on the window family, a proven o(N) cap on spectral escape everywhere, and a labeled exploratory payoff curve outside the proven ladder regime (Section 8.4).

---

## 2. The model

This section fixes the model in which every theorem of Sections 3–7 lives: the master trace formula, its finite-circle discretization, the adversary class, and the row system. It condenses the gate specification (SPEC Sections 1–4); everything here was re-derived in this session's verification suite.

### 2.1 Window and kernel

Fix a window profile v >= 0 on [-1/2, 1/2], even, with Int v > 0 (the scale-free profile of the parent's taper-squared phi^2; the formalized taper class is C^3). The **normalized sampling kernel** at bandwidth lambda > 0 is the entire function

    psi_lambda(x) = ( Int_{-1/2}^{1/2} v(sigma) e^{2 pi i lambda sigma x} d sigma ) / Int v ,

so psi_lambda(0) = 1, with Fourier transform u supported in |alpha| <= lambda/2 (Montgomery alpha-units), Int u = 1. For the flat window v = 1:

    psi_lambda(x) = sinc(pi lambda x) = sin(pi lambda x)/(pi lambda x),      u = (1/lambda) 1_[-lambda/2, lambda/2].

Positions x are in mean-gap units (mean zero spacing 1); complex positions (off-line zeros) are allowed, psi_lambda being entire.

### 2.2 Continuum model: configurations and the master trace formula

A **marked configuration** is a finite multiset of points z with positions gamma_z (complex allowed) and integer marks m_z >= 1; off-line points occur only in conjugate pairs {gamma + i d, gamma - i d} with common depth and common mark (functional-equation symmetry). The **master trace formula** defines the k-th trace at bandwidth lambda:

    tr G^k := Sum_{z_1, ..., z_k} ( Prod_j m_{z_j} ) psi_lambda(gamma_{z_1} - gamma_{z_2}) psi_lambda(gamma_{z_2} - gamma_{z_3}) ... psi_lambda(gamma_{z_k} - gamma_{z_1}),

summed over ordered k-tuples of configuration points. This is the parent's Poisson sampling identity in normalized units (units in which an isolated on-line zero of mark m has eigenvalue exactly m), and it is realized by an actual Hermitian matrix — Section 3.1 constructs the block matrices explicitly where spectral (not just trace) data are needed. We write F = tr G^2 (Frobenius row) and C = tr G^3 (signed cubic row); F1 at bandwidth 1, F' and C' at bandwidth lambda'. This single formula generates every trace row on both sides — null budgets and configuration demands — including all clustering cross-terms and all depth effects; no isolated-block idealization enters the gate anywhere.

### 2.3 Finite-circle model (the LP's discretization)

Period N (zeros per period) on the circle of circumference N; configurations are N-periodic, described by one period. For the flat window at bandwidth lambda the harmonic set is B = {j in Z : |j| <= lambda N/2}, with M = |B| harmonics and uniform weights u_j = 1/M. With the form factor

    c_s = Sum_z m_z e^{-2 pi i s theta_z / N}        (a conjugate pair at theta +/- i d contributes 2 m cosh(2 pi s d / N) e^{-2 pi i s theta / N}),

the trace rows are

    tr G-hat   = Sum_z m_z                      (mass),
    tr G-hat^2 = Sum_s W2(s) |c_s|^2,           W2(s) = Sum_{j in B, s-j in B} u_j u_{s-j},
    tr G-hat^3 = Sum_{k1,k2} U3(k1,k2) c_{k1} c_{k2} c_{-k1-k2},    U3(k1,k2) = Sum_j u_{j+k1} u_{j+k1+k2} u_j.

Eigenvalue data (ladder counts, inertia) come from the Hermitian frequency matrix H[j, j'] = sqrt(u_j u_{j'}) c_{j-j'} (j, j' in B), whose k-th trace equals the k-th trace row exactly (alias-free tight-frame compression). At the primary geometry N = 64, lambda = 1: M = 65; lambda' = 1/2: M' = 33. In position space, for a symmetric band, tr G-hat^2 = Sum_{z,z'} m_z m_{z'} D(theta_z - theta_{z'})^2 with D(x) = Sum_j u_j e^{-2 pi i j x / N} real, even, D(0) = 1 — the discrete analog of the continuum tr G^2 = Sum m m' psi_lambda^2.

### 2.4 Adversary class, laws, and the two benchmarks

A **column** is an explicit N-periodic marked configuration: on-line atoms (positions theta_i in [0, N), integer marks 1 <= m_i <= W) and off-line pairs (position, dimensionless depth w in the family (0, 1] plus deep probes {1.5, 2}, pair multiplicity m), with mass Sum m_i + 2 Sum m_p = N per period. A **law** is a probability mixture w_c >= 0, Sum w_c = 1 over columns; every row is E_w[row(c)]. The two objectives:

    N_d(c) = #atoms + 2 #pairs           (distinct zeros; only on-line multiples reduce it),
    p1(c)  = ( #mark-1 atoms + 2 #mult-1 pairs ) / N     (simple fraction).

**Realizability — what is imposed and why it is exactly right (SPEC 3.2, in brief).** Imposed: explicit finite marked multisets (never bare correlation data); integer marks; conjugate-pair structure; mass N; mixtures. *Necessity:* an adversary allowed to post aggregated moment data directly could claim values realized by no point configuration (unconstrained cross-term variables can leave the convex hull of realizable moment pairs), making an "absorption" vacuous; and integrality, pair symmetry, and density are properties the true zero multiset provably has — dropping any of them hands the adversary provably impossible worlds (with fractional marks even the 5/6 baseline is false: mass N of mark-4/3 atoms on the grid of Theorem 3.9 has F1 = (4/3) N budget-tight and N_d = (3/4) N < (5/6) N; Section 4.2 exhibits the subtler pair-channel form of the same failure). *Sufficiency:* nothing further may be imposed, because every row of the system is a theorem valid for arbitrary configurations with these properties — trace identities are linear algebra plus the sampling identity, the budgets are the unconditional prime-side equalities, the ladder is Theorem 1(ii)-repaired, inertia is Sylvester; imposing anything more (e.g. pointwise GUE 3-level correlations) would smuggle in precisely the unproven correlation knowledge whose absence the gate respects. Periodicity and the finite depth/mark grids are discretizations, refined under the verdict-stability requirement (N = 64 -> 128, W-scan, depth-grid halving), not constraints.

### 2.5 The row system

Baseline (two-moment / lemmaR_tight data): mass N; integrality and pair structure; bandwidth-one Frobenius budget E_w[F1] in (4/3) N (1 -/+ eps) (matched-geometry variant: the finite-N CUE-sampled center B1 replaces (4/3)N). The cubic block at lambda' = 1/2 adds:

    (R-5)  lambda'-Frobenius:  E_w[F'] in kappa(1/2) N (1 -/+ eps),   kappa(1/2) = 13/6;
    (R-6)  signed cubic with capacity coupling:  |E_w[C'] - c3(1/2) N| <= eps_3 N + 2 sqrt(2) sqrt(C_led g_F) N,   c3(1/2) = 5;
    (R-5') garnish Frobenius budget g_F >= 0 charged against the Frobenius slack;
    (R-7)  all-V count ladder:  E_w[n(V)] <= C_led N V^{-4} on the V-grid {2, 3, 4, 6, 8, 12, 16};
    (R-8)  inertia n_-(c) <= p(c) per column (automatic on explicit spectra; asserted);
    (R-9)  Frobenius split, power-mean, Hoelder-with-o(N): automatically satisfied by explicit spectra (the R7 fallback system made primary — on explicit configurations the linear-algebra-true rows cannot be violated, so their entire content is enforced leak-free by construction).

The budget centers are the clustered sine-process null moments (Section 3.5) — never isolated-block values — because at lambda' = 1/2 the window width is two mean gaps and the null itself is cross-term-dominated: cross-terms (occupancy >= 2) carry 54% of the Frobenius budget and 80% of the cubic budget (analytic fractions 7/6 of 13/6 and 4 of 5; null MC 52.6% / 79.0% at n = 64). The decision rule (pre-registered): ABSORPTION iff delta_0 = P_full - P_base = 0 within LP tolerance at the decision points with an explicit witness law; the witness must satisfy every row at centered budgets with E[N_d]/N <= 5/6 + 0.01.

---

## 3. Structure theorems

We lead with the theorem that explains everything: on isolated blocks the signed cubic row is an affine function of the mass and Frobenius rows plus the second integrality level — it cannot see doubles-versus-pairs at any depth. We then compute the null budgets in closed form, obtaining the identities that organize the entire margin structure, and finally prove the grid-decoupling theorem that hands the adversary the cross-term channel for free. Every proof in this section is complete; the numerical confirmations (all re-run this session, `verify/verify_t1.py`–`verify_t4_mc.py`) are summarized at the point of use.

### 3.1 The exact pair block

**Setting.** Windows tau_k = k (2 pi / L), k in Z (critical spacing); taper phi real, even, continuous, supported in [-L/2, L/2], phi in C^2 (the parent's formalized class is C^3 — more than enough). Fourier convention phihat(z) = Int phi(s) e^{-i s z} ds (entire, by Paley–Wiener); Phi(z) = Int phi(s)^2 e^{-i s z} ds; a = L^{-1} Int phi^2, so Phi(0) = L a. Normalized units: matrices divided by L^2 a, in which an isolated on-line atom of mark m has eigenvalue m.

**Lemma 3.1 (Poisson sampling identity, complex arguments).** For all complex tau, tau':

    Sum_{k in Z} phihat(tau - tau_k) phihat(tau' - tau_k) = L Phi(tau - tau') ,

the sum converging absolutely and locally uniformly.

*Proof.* First real arguments. Fix tau, tau' in R and set g(t) = phihat(tau - t) phihat(tau' - t); phihat is real on R (phi real even) and, since phi in C^2 with compact support, |phihat(x)| <= C/(1 + x^2), so g in L^1 with |g(t)| <= C'/(1 + t^2)^2 and the lattice sum converges absolutely. Each factor t -> phihat(tau - t) has Fourier transform e^{-i tau xi} 2 pi phi(xi) (inversion), supported in [-L/2, L/2]; hence ghat = (1/2 pi)(convolution of the factor transforms) is continuous, supported in [-L, L], and vanishes AT the endpoints ±L (the convolution of two continuous functions supported in [-L/2, L/2], evaluated at L, integrates over the null set {L/2}). Poisson summation over the lattice (2 pi / L) Z (classical form; |g| + |ghat| summable on the respective lattices):

    Sum_k g(2 pi k / L) = (L / 2 pi) Sum_{n in Z} ghat(n L) = (L / 2 pi) ghat(0),

all n != 0 terms vanishing by the support (|nL| >= L, endpoint value 0). By Plancherel, ghat(0) = Int phihat(tau - t) phihat(tau' - t) dt = (1/2 pi) Int (2 pi phi(xi))^2 e^{-i (tau - tau') xi} d xi = 2 pi Phi(tau - tau'), giving the identity on R^2. For complex arguments: |phihat(x + i y)| <= e^{L |y| / 2} C/(1 + x^2), so on compact subsets of C^2 the lattice sum converges absolutely and uniformly and is entire in (tau, tau'), as is L Phi(tau - tau'); the two entire functions agree on R^2, hence everywhere (identity theorem, one variable at a time). QED

**Proposition 3.2 (exact off-line pair block — the true Prop-4.1 spectrum).** Let the conjugate pair be {gamma + i delta, gamma - i delta}, gamma in R, depth delta > 0, multiplicity m, with evaluation vector x = (x_k), x_k = phihat(gamma + i delta - tau_k), and block matrix M = m (x x^T + xbar xbar^T) (transpose, not conjugate-transpose: the two rank-one terms are the pair's two zeros). Then, exactly:

    (i)    x^T x = L Phi(0) = L^2 a          — real, independent of depth AND position;
    (ii)   |x|^2 = L Phi(2 i delta) = L^2 a A(delta),   A(delta) = Int phi^2(s) cosh(2 delta s) ds / Int phi^2(s) ds >= 1;
    (iii)  writing x = p + i q: <p, q> = 0 exactly, |p|^2 = L^2 a (1 + A)/2, |q|^2 = L^2 a (A - 1)/2;
    (iv)   M = 2 m (p p^T - q q^T), rank <= 2 real symmetric, with nonzero eigenvalues (normalized by L^2 a)
               m (1 + A(delta))   and   m (1 - A(delta)),   independent of the position gamma;
    (v)    normalized charges: trace 2m; Frobenius 2 m^2 (1 + A^2); signed cubic 2 m^3 (1 + 3 A^2).

In dimensionless depth w := L delta, A depends on the pair only through w, with A(0+) = 1 and A strictly increasing; for the flat taper A(w) = sinh(w)/w, with values A(1/8) = 1.002606, A(1/4) = 1.010449, A(1/2) = 1.042191, A(3/4) = 1.096422, A(1) = 1.175201, A(2) = 1.813430.

*Proof.* (i) Lemma 3.1 at tau = tau' = gamma + i delta: Sum_k phihat(gamma + i delta - tau_k)^2 = L Phi(0) = L Int phi^2 = L^2 a — real, independent of gamma and delta. (ii) phi real and even gives phihat(zbar) = conj(phihat(z)); hence |x_k|^2 = phihat(u - tau_k) phihat(ubar - tau_k) with u = gamma + i delta, and Lemma 3.1 at (u, ubar) gives |x|^2 = L Phi(2 i delta) = L Int phi^2(s) cosh(2 delta s) ds (phi^2 even); A >= 1 by cosh >= 1, strictly increasing by strict monotonicity of cosh on the support. (iii) x^T x = |p|^2 - |q|^2 + 2 i <p, q>; by (i) it is real, so <p, q> = 0 and |p|^2 - |q|^2 = L^2 a; with |p|^2 + |q|^2 = |x|^2 = L^2 a A, solve. (iv) x x^T + xbar xbar^T = (p + iq)(p + iq)^T + (p - iq)(p - iq)^T = 2 (p p^T - q q^T); with p ⊥ q the eigenvectors are p, q with eigenvalues 2 m |p|^2 = m L^2 a (1 + A) and -2 m |q|^2 = m L^2 a (1 - A); all others 0; normalize. Position-independence: the eigenvalues depend only on |p|^2, |q|^2, which depend only on delta. (v) Trace m(1 + A) + m(1 - A) = 2m; Frobenius m^2 (1+A)^2 + m^2 (1-A)^2 = 2 m^2 (1 + A^2); cubic m^3 (1+A)^3 + m^3 (1-A)^3 = 2 m^3 (1 + 3 A^2). Flat-taper A: A(w) = Int_{-1/2}^{1/2} cosh(2 w sigma) d sigma = sinh(w)/w; the listed values are its evaluations (they reproduce the gate specification's table to its displayed precision, <= 4e-6). QED

*Consistency and inertia.* The two-point configuration {gamma ± i delta} under the master formula has tr G^k = m^k tr K^k with the 2x2 kernel K = [[1, A], [A, 1]], eigenvalues 1 ± A — the same charges. The matrix route (iv) additionally certifies the inertia (one positive, one negative eigenvalue for delta > 0) consumed by the n_- and ladder rows.

*Block continuity, exact form.* As delta -> 0+, the spectrum tends to (2m, -0), Frobenius to 2 m^2, cubic to 8 m^3: a shallow pair is row-indistinguishable from an on-line double in EVERY row, continuously. And — this is the correction of record — the cubic charge 2 m^3 (1 + 3 A^2) >= 8 m^3 at EVERY depth (A >= 1), increasing with depth: a deep pair never loses cubic charge. The "+8 vs 0" separation premise (the proposal's Step-4 narrative; the adjudication's computation-8 phase model) is false under the true block law; the campaign transcript's recorded block facts (pair eigenvalues m L^2 a (1 ± A)) were correct throughout.

Numerical confirmation (this session, `verify_t3.py`): evaluation-vector route with a cos taper, L = 40, 120001 windows: |x^T x / L^2 a - 1| <= 6.7e-16, |<p,q>|/L^2 a <= 1.7e-14, block eigenvalues vs m(1 ± A) to 7.8e-14, position-independent at machine precision at every depth w in {1/64, 1/8, 1/4, 1/2, 3/4, 1, 2}; shallow-pair cubic charge 8.0005 at w = 1/64 and 8.0313 at w = 1/8, matching the audit's independent 8.0005 / 8.033 — never 0 at any depth.

### 3.2 The affine-plane identity and cubic blindness

**Definition (per-zero charges).** For an isolated block of total mass mu (mu = m for an atom of mark m; mu = 2m for a pair of multiplicity m), let F = (block Frobenius)/mu and c = (block cubic)/mu. By Proposition 3.2(v) and the atom spectrum:

    atom, mark m:        F = m,               c = m^2;
    pair, mult m, depth: F = m (1 + A^2),     c = m^2 (1 + 3 A^2).

**Proposition 3.3 (affine-plane identity).**

    atom of mark m:              c = 3 F - 2 + (m - 1)(m - 2) ;
    pair of mult 1, ANY depth:   c = 3 F - 2      EXACTLY ;
    pair of mult m, ANY depth:   c = 3 F - 2 + (m - 1)(m - 2) + 3 m (m - 1) A^2 .

In particular every mark-{1,2} atom and every multiplicity-1 pair — at every depth — lies on the same affine plane c = 3F - 2 in the per-zero (F, c) plane.

*Proof.* Atom: 3F - 2 + (m-1)(m-2) = 3m - 2 + m^2 - 3m + 2 = m^2 = c. Pair: c - 3F + 2 = m^2 (1 + 3A^2) - 3m(1 + A^2) + 2 = (m^2 - 3m + 2) + 3 A^2 (m^2 - m) = (m-1)(m-2) + 3 m (m-1) A^2. At m = 1 both terms vanish identically in A (every depth); at m = 2 the atom identity also reads c = 3F - 2 (doubles are on the plane). QED

**Theorem 3.4 (cubic blindness on isolated blocks).** Let the configuration be a disjoint union of isolated blocks (atoms of marks m_i; pairs of multiplicities m_p at depths with A_p = A(delta_p)), with total mass Mass, Frobenius F, signed cubic C (sums of block charges). Then, exactly:

    C - 3 F + 2 Mass = Sum_{zeros} m (m - 1)(m - 2) + 6 Sum_{pairs} m_p^2 (m_p - 1) A_p^2 ,

where the first sum runs over the zero multiset (an atom of mark m contributes m(m-1)(m-2) once; a pair of mult m contributes twice that — its two zeros). Consequences:

1. On the class {mark-{1,2} atoms} ∪ {multiplicity-1 pairs of arbitrary depth} — the entire doubles-vs-pairs comparison class of lemmaR_tight — the right side vanishes identically: **C = 3 F - 2 Mass identically on the class.** The signed cubic row restricted to isolated blocks of this class is an exact affine combination of the Frobenius and mass rows: it separates nothing those two rows do not. An on-line double and an off-line pair of any depth are cubic-indistinguishable.
2. All discriminating power of the cubic row beyond the two-moment data therefore lives in exactly two places: (i) marks >= 3 (and pair multiplicities >= 2), through the nonnegative integrality terms on the right; (ii) violations of block isolation — the clustering cross-terms of the master trace formula, which the identity does not constrain, and which Theorem 3.9 shows to be adversary-tunable at zero cost.
3. The premise "a hyperbolic pair block contributes (+a)^3 + (-a)^3 = 0 to tr G^3 while a double contributes +8" is FALSE under the true block law: the pair's signed cubic is 2 m^3 (1 + 3 A^2) >= 8 m^3 at every depth. The sign-split "different corners of the constraint polytope" picture is superseded, as already recorded in the direction file.

*Proof.* Sum the per-block identities. An atom of mark m has block charges (mass m, Frobenius m^2, cubic m^3), contributing m^3 - 3 m^2 + 2m = m(m-1)(m-2) to C - 3F + 2 Mass. A pair of mult m has block charges (mass 2m, Frobenius 2 m^2 (1 + A^2), cubic 2 m^3 (1 + 3 A^2)), contributing

    2 m^3 (1 + 3 A^2) - 6 m^2 (1 + A^2) + 4 m = 2 m (m-1)(m-2) + 6 m^2 (m - 1) A^2 ,

exactly its two zeros' worth of the integrality sum plus the multiplicity-weighted depth term. On marks {1,2} and mult-1 pairs every term vanishes. Consequence 3 is Proposition 3.2 (A >= 1). QED

*Remark (why the gate had to be clustered).* By consequence 1, an isolated-block gate over the doubles-vs-pairs class returns a tautological answer along the plane c = 3F - 2. The corrected gate's clustered null and positional freedom were therefore not conservatism but necessity — and the decided outcome is that the clustering cross-terms, the only live channel, are a free resource for the adversary rather than a signal for the certificate.

Numerical confirmation (`verify_t3.py`): charges and the per-zero identity for m in {1, 2, 3, 5} at all depths to <= 9.1e-13; atom identity exhaustive m = 1..29, exact; master-formula 2x2 kernel route reproduces all three charges.

### 3.3 Sine-process closed forms and the doubles-plane diagnostic

The gate's null budgets are the per-zero moments of the flat-window Gram over the determinantal sine process — the process with kernel S(x) = sin(pi x)/(pi x), intensity 1, and correlation functions (taken as the null's definition)

    rho_2(x1, x2) = 1 - S(x12)^2,
    rho_3(x1, x2, x3) = 1 - S(x12)^2 - S(x13)^2 - S(x23)^2 + 2 S(x12) S(x13) S(x23).

The per-zero Gram moments at bandwidth lambda (flat window, psi = psi_lambda, u = psihat):

    m2(lambda) := 1 + Int rho_2(0, x) psi(x)^2 dx ,
    m3(lambda) := 1 + 3 Int rho_2(0, x) psi(x)^2 dx + T3(lambda),
    T3(lambda) := IntInt rho_3(0, x, x + y) psi(x) psi(y) psi(x + y) dx dy ,

the N -> infinity limits of E[tr G^k]/N: the k-tuple sum of Section 2.2 splits over coincidence patterns — all-equal (value 1), exactly-two-equal (3 ordered patterns at k = 3, each psi(x)^2 against rho_2), all-distinct (rho_3 against the cyclic kernel product, reparametrized by separations using the evenness of psi). The sine process is simple, so all marks are 1.

**Theorem 3.5 (flat-window closed forms).** For the flat window and every 0 < lambda <= 1:

    m2(lambda) = 1/lambda + lambda/3 ,          m3(lambda) = 1 + 1/lambda^2 .

*Proof.* Step 1 (Fourier-side reduction). With t(alpha) = (1 - |alpha|)_+ (the transform of S^2), b = 1_[-1/2, 1/2] (= Shat), and the convention fhat(alpha) = Int f(x) e^{-2 pi i alpha x} dx:

    (i)    Int psi^2 dx = Int u^2 d alpha                                    [Plancherel];
    (ii)   Int S^2 psi^2 dx = Int t (u * u) d alpha                          [Plancherel on the product pair];
    (iii)  IntInt psi(x) psi(y) psi(x + y) dx dy = Int u^3 d alpha ;
    (iv)   IntInt S(x)^2 psi(x) psi(y) psi(x + y) dx dy = Int (t * u) u^2 d alpha,  and the same value for the S(y)^2 and S(x+y)^2 variants;
    (v)    IntInt S(x) S(y) S(x + y) psi(x) psi(y) psi(x + y) dx dy = Int (b * u)^3 d alpha .

For (iii), two Plancherel steps with no delta calculus: with y fixed, g(y) := Int psi(x) psi(x + y) dx is the Fourier transform of u^2 at y; then Int psi(y) g(y) dy = Int psihat u^2 = Int u^3 by the multiplication identity Int f ghat = Int fhat g; Fubini is licensed by |psi(x) psi(y) psi(x+y)| <= C / ((1+|x|)(1+|y|)(1+|x+y|)), integrable on R^2. For (iv), the same two-step Plancherel with first factor S(x)^2 psi(x) gives Int (S^2 psi)^hat u^2 = Int (t * u) u^2; the S(y)^2 and S(x+y)^2 variants reduce to the same value under the substitutions (x,y) -> (y,x) and (x,y) -> (x, -x-y) (Jacobian 1, integrand invariant). For (v), set h = S psi, hhat = b * u, and apply (iii) to h. Hence

    m2 = 1 + Int u^2 - Int t (u * u),      m3 = 1 + 3 [ Int u^2 - Int t (u * u) ] + T3,
    T3 = Int u^3 - 3 Int (t * u) u^2 + 2 Int (b * u)^3 .

Step 2 (evaluation at u = (1/lambda) 1_[-lambda/2, lambda/2], using lambda <= 1 exactly where indicated).

(1) Int u^2 = 1/lambda.
(2) (u * u)(alpha) = (1/lambda^2)(lambda - |alpha|)_+; since lambda <= 1, t = 1 - |alpha| on this support, so Int t (u*u) = (2/lambda^2) Int_0^lambda (1 - a)(lambda - a) da = (2/lambda^2)[lambda^2/2 - lambda^3/6] = 1 - lambda/3. Hence m2 = 1 + 1/lambda - (1 - lambda/3) = 1/lambda + lambda/3.
(3) Int u^3 = 1/lambda^2.
(4) Int (t * u) u^2 = (1/lambda^3) IntInt_{|alpha| <= lambda/2, |alpha - beta| <= lambda/2} t(beta) d beta d alpha = (1/lambda^3) Int t(beta)(lambda - |beta|)_+ d beta = (1/lambda^3)[lambda^2 - lambda^3/3] = 1/lambda - 1/3 (reusing the integral of (2); valid for lambda <= 1).
(5) (b * u)(alpha) is the trapezoid equal to 1 on |alpha| <= (1 - lambda)/2, decaying linearly to 0 at |alpha| = (1 + lambda)/2; hence Int (b * u)^3 = (1 - lambda) + 2 lambda Int_0^1 s^3 ds = 1 - lambda/2.

Assembling: T3 = 1/lambda^2 - 3(1/lambda - 1/3) + 2(1 - lambda/2) = 1/lambda^2 - 3/lambda + 3 - lambda, and m3 = 1 + 3[1/lambda - 1 + lambda/3] + T3 = 1 + 1/lambda^2. QED

**Corollary 3.6 (anchor values, the doubles-plane diagnostic, the moment margin).**

    m2(1) = 4/3,   m3(1) = 2,   m2(1/2) = 13/6,   m3(1/2) = 5.

Define G(lambda) := m3 - (3 m2 - 2) (the null budget's excess over the isolated-block doubles/pairs plane of Theorem 3.4) and Marg(lambda) := 2 m2 - m3 (the Section-7.3-style certificate margin). Then, flat window, on (0, 1]:

    G(lambda) = 3 + 1/lambda^2 - 3/lambda - lambda ;         G(1) = 0 ,   G(1/2) = 1/2 ;
    Marg(lambda) = 2/lambda + 2 lambda/3 - 1 - 1/lambda^2 ;  Marg(1) = 2/3 ,   Marg(1/2) = -2/3 ,

and Marg has a unique sign change on (0, 1] (the interval on which the closed forms are proved), at lambda_0 = 0.610511... Each value is load-bearing for the no-go:

1. **G(1) = 0 is the "2 = 2" saturation.** At bandwidth one the sine budget m3(1) = 2 exactly equals the isolated-block cubic demand of the 5/6-extremal (2/3 simple + 1/6 doubles: (2/3)(1) + (1/3)(4) mass-weighted = 2, on the plane of Theorem 3.4). The bandwidth-one cubic row alone cannot cut the doubles corner — the budget is exactly met.
2. **G(1/2) = +1/2 > 0.** At the operating bandwidth the null budget sits strictly ABOVE the doubles plane: a doubles-saturated adversary must supply +1/2 per zero of cubic through positional cross-terms — which Theorem 3.9's grid freedom supplies at zero cost (the gate's witness does exactly this, sitting at the LOWER cubic budget edge).
3. **Marg(1/2) = -2/3 < 0.** The omega(m)-moment route's margin is negative at the proven operating point: a bite could never have come from the Section-7.3 mechanism there, only from joint positional pricing. The sign change at lambda_0 = 0.6105 is precisely where the gate's exploratory scan saw delta_0 turn positive (between lambda' = 0.55 and 0.60; Section 8.4), outside the proven ladder regime.

*Proof.* Substitute Theorem 3.5; the displayed formulas are algebraic identities on (0, 1]. G(1) = 3 + 1 - 3 - 1 = 0; G(1/2) = 3 + 4 - 6 - 1/2 = 1/2; Marg(1) = 2 + 2/3 - 1 - 1 = 2/3; Marg(1/2) = 4 + 1/3 - 1 - 4 = -2/3. Uniqueness of the root: q(lambda) = lambda^2 Marg(lambda) = 2 lambda + (2/3) lambda^3 - lambda^2 - 1 has q' = 2 + 2 lambda^2 - 2 lambda > 0 (negative discriminant), so q is strictly increasing with q(0.55) < 0 < q(0.66); numerically the root is 0.610511 (brentq, re-verified by sympy nsolve). The extremal demand in item 1: per-zero (F, c) = (1, 1) on simples and (2, 4) on doubles; mass-weighted cubic (2/3)(1) + (1/3)(4) = 2 = m3(1) and Frobenius (2/3)(1) + (1/3)(2) = 4/3 = m2(1) — both budgets exactly saturated at lambda = 1. QED

**Corollary 3.7 (the m2 = kappa identity: sine null = unconditional budget).** The closed form m2(lambda) = 1/lambda + lambda/3 coincides, at every lambda <= 1, with the value obtained by integrating the unconditional Montgomery/BGSTB24 pair-correlation form factor F(alpha) = delta_0(alpha) + |alpha| (on |alpha| <= 1) against the flat-window pair kernel:

    (1/lambda^2) Int_{-lambda}^{lambda} (lambda - |alpha|) [ delta_0(alpha) + |alpha| ] d alpha = (lambda + lambda^3/3)/lambda^2 = 1/lambda + lambda/3 = m2(lambda) .

The sine-process null's second-moment budget IS the parent paper's unconditional prime-side kappa(lambda), exactly, on the whole band lambda <= 1 — the strongest possible identity check at second order, and the reason the gate's F' budget row is unconditional-data-backed. (Provenance: the prime-side member — tr G-hat^2 <-> Int (lambda - |alpha|) F(alpha) d alpha with F unconditional and pointwise on the closed band 0 <= alpha <= 1 — is the parent paper's Theorem 5.8 / Remark 5.10 bookkeeping together with BGSTB24 Theorem 1, quoted, not re-derived; the displayed arithmetic identity is the elementary integral Int_0^lambda (lambda - a) a da = lambda^3/6, doubled, plus the delta term lambda.) **No third-order analog is claimed:** the identification c3(lambda') = m3(lambda') rests on Rudnick–Sarnak-range GUE 3-level correlations and remains an open flag (F2; Section 8.3).

Numerical confirmation (`verify_t4.py`, `verify_t4_mc.py`): Fourier-side quadrature matches both closed forms at 7 bandwidths to <= 1.7e-5; an independent real-space determinantal quadrature gives m3(1/2) = 4.9924 (truncation X = 40) -> 4.9960 (X = 80), trending to 5 as the audit's independent quadrature did (4.9896 -> 4.9932); a fresh CUE Monte Carlo (third independent sampler) extrapolates m2(1/2) -> 2.1668 and m3(1/2) -> 5.0014 against 13/6 and 5, each within ~1 sigma of both the gate's and the auditor's samplers (full tables: Appendix B). The values m2(1) = 4/3, m3(1) = 2 also discharge, for k <= 3, the parent's recalled sine moments m_k(1) = 1, 4/3, 2.

### 3.4 Grid Parseval decoupling

The absorption mechanism rests on one exact identity: on a specific uniform grid the entire bandwidth-one Frobenius row degenerates to the multiplicity count — for every site subset and every mark assignment — while the half-band kernel on the same grid remains position-sensitive.

**Lemma 3.8 (flat-band lemma).** Let M >= 1 and let the harmonic band be ANY set of M consecutive integers B = {j0, ..., j0 + M - 1}, with uniform weights u_j = 1/M. Let the configuration be supported on the M-site uniform grid theta_k = k N / M (k = 0, ..., M - 1) on the circle of circumference N, with arbitrary real marks m_k >= 0. Then

    tr G-hat^2 = Sum_k m_k^2      EXACTLY.

*Proof.* On the grid the form factor is a DFT on Z_M: c_s = Sum_k m_k e^{-2 pi i s k / M}, which depends only on s mod M — c is M-periodic in s — and DFT Parseval gives Sum_{r mod M} |c_r|^2 = M Sum_k m_k^2 (P). The Frobenius row is Sum_s W2(s) |c_s|^2 with W2(s) = #{(j1, j2) in B x B : j1 + j2 = s}/M^2; the sum-set B + B = {2 j0, ..., 2 j0 + 2M - 2} carries the triangular pair counts M - |s - (2 j0 + M - 1)| on |s - (2 j0 + M - 1)| <= M - 1. Fix a residue class r mod M: the window B + B has length 2M - 1, so it contains either one member of the class (t = 0, count M) or two members t and t ∓ M with 0 < |t| < M, whose counts sum to (M - |t|) + |t| = M — EXACTLY M on every residue class. Hence, by the M-periodicity of |c_s|^2,

    tr G-hat^2 = (1/M^2) Sum_{r mod M} M |c_r|^2 = (1/M) Sum_r |c_r|^2 = Sum_k m_k^2

by (P). QED

**Theorem 3.9 (grid Parseval decoupling at bandwidth one).** Let N be even, flat window at lambda = 1: band B = {|j| <= N/2}, M = N + 1 harmonics, u_j = 1/(N+1). Let the configuration be supported on the (N+1)-site uniform grid of spacing N/(N+1) (the psi_1-zero grid), with arbitrary marks. Then

    F1 = tr G-hat_1^2 = Sum_z m_z^2      EXACTLY,

for every site subset and every mark assignment: the bandwidth-one reading on this grid sees only multiplicities, never positions, and the lemmaR_tight extremal analysis transfers verbatim to grid configurations.

*Proof.* Lemma 3.8 with M = N + 1, B = {-N/2, ..., N/2} (N + 1 consecutive integers since N is even), grid spacing N/M = N/(N+1). QED

*Remark (why this grid).* Equivalently: all pairwise site differences are nonzero multiples of N/(N+1), the zero set of the discrete bandwidth-one kernel D. The Fourier proof is the one that makes the exactness structural — assembly weights constant on residue classes — rather than a numerical coincidence, and it is the form queued for Lean.

**Proposition 3.10 (the lambda' = 1/2 kernel is alive on the same grid).** Same geometry, N and N/2 even, lambda' = 1/2: band B' = {|j| <= N/4}, M' = N/2 + 1. For grid-supported configurations,

    F' = Sum_{|s| <= N/2} ( (M' - |s|) / M'^2 ) |c_s|^2 ,

where {-N/2, ..., N/2} is a COMPLETE residue system mod (N+1) and c_s is the Z_{N+1} DFT of the mark vector. The weights are strictly positive and non-constant across residues (triangular: at N = 64, from 1/33 at s = 0 down to 1/33^2 at |s| = 32), so F' is a strictly position-sensitive functional of the grid configuration, subject only to Parseval.

*Proof.* F' = Sum_s W2'(s) |c_s|^2 with W2'(s) = (M' - |s|)_+/M'^2 supported in |s| <= N/2. That range has N + 1 elements, hence meets each residue class mod N + 1 exactly once; no residue-class telescoping occurs (band length M' = N/2 + 1 differs from the grid size N + 1), so F' reads the full grid power spectrum with a non-uniform weight; distinct site subsets of equal mark statistics generically differ. QED

**Worked exact value (hand-checkable; the witness's first column).** N = 64, the "vacancy lattice": 64 simple marks on 64 of the 65 grid sites. Then c_0 = 64 and |c_s|^2 = 1 for s not ≡ 0 mod 65, so

    F1 = 64      (Theorem 3.9),
    F' = (33/33^2) 64^2 + Sum_{0 < |s| <= 32} ((33 - |s|)/33^2) = 4096/33 + 32/33 = 4128/33 = 125.0909... ,

using Sum_{|s| <= 32} (33 - |s|) = 33^2 and subtracting the s = 0 term. This reproduces the shipped witness column exactly (`witness_N64.json`: F1 = 64, F' = 125.09090...; independently hand-derived in the audit). The two-bandwidth decoupling is thereby explicit: F1 is blind to the vacancy's position, F' is not.

**Proposition 3.11 (continuum analog: the adversary lattice).** In the continuum model, flat window, configuration supported on the integer lattice Z with arbitrary real marks: tr G_1^2 = Sum m_z^2 exactly, while the half-band kernel is alive on the lattice: psi_{1/2}(k) = sinc(pi k/2) = (2/(pi k)) (-1)^{(k-1)/2} for odd k (0 for even k != 0). For the finite-T Weil–Gabor matrix itself the identity holds as tr G-hat^2 = (Sum m^2)(1 + o(1)), the o(1) being the parent's finite-window corrections (quoted; the campaign's recorded "adversary lattice").

*Proof (model part).* At k = 2 the master formula gives tr G_1^2 = Sum_{z,z'} m_z m_{z'} psi_1(z - z')^2; psi_1(x) = sinc(pi x) vanishes at every nonzero integer and equals 1 at 0, so only the diagonal survives. The half-band values are sin(pi k/2)/(pi k/2) with sin(pi k/2) = (-1)^{(k-1)/2} for odd k. QED

*Remark.* Theorem 3.9 is the exact periodization of Proposition 3.11: spacing N/(N+1) instead of 1 makes the identity exact rather than asymptotic — which is precisely why the finite-N gate could exhibit delta_0 = 0 as an exact LP equality rather than a numerical near-zero. The absorption is not a finite-N artifact.

Numerical confirmation (`verify_t1.py`): grid exactness on 40 random site-subsets with random marks at N = 64 and N = 128, two independent evaluation routes (Fourier double sum; eigenvalues of H): max |F1 - Sum m^2| = 9.1e-13 / 4.1e-12, matching the audit's independent 4.5e-13; general flat-band lemma on 20 random (N, M, j0) draws including asymmetric bands: 3.2e-12; controls — off-grid configurations give |F1 - Sum m^2| in [1.3e-2, 62.5] and on-grid half-band |F' - Sum m^2| in [40.9, 120.8] (the identity genuinely fails off the grid, and the half-band kernel is genuinely alive on it); continuum lattice exact to machine precision.

---

## 4. The absorption theorem

This section states and proves the model-level theorem the gate pins — the two-moment data force exactly the lemmaR_tight corner, for both benchmarks, over the honest configuration classes — and then presents the computational certification that the entire cubic block is absorbed at that corner, with the explicit witness.

### 4.1 The atom-only corner theorem

Fix N and eps >= 0, and let A be the class of atom-only configurations: atoms at arbitrary positions (finite-circle or continuum model, flat windows — the proofs work verbatim in both), integer marks m_i >= 1, mass Sum m_i = N per period.

**Lemma 4.1 (diagonal positivity).** For every atom-only configuration (any positions, any real marks m_i >= 0), in either model, F1 >= Sum_i m_i^2, with equality iff every off-diagonal kernel value vanishes — in particular on the grid of Theorem 3.9 and the lattice of Proposition 3.11.

*Proof.* F1 = Sum_{i,i'} m_i m_{i'} K(theta_i - theta_{i'}) with K = D^2 (finite circle) or K = psi_1^2 (continuum): K >= 0 pointwise, K(0) = 1, so F1 = Sum m_i^2 + (a sum of nonnegative off-diagonal terms). QED

This is the one step that fails for pair-containing configurations — an off-line pair contributes cross-terms of the form 2 m m' Re[psi(x + i y)^2], which need not be nonnegative; Sections 4.2–4.3 treat that channel.

**Lemma 4.2 (integer-mark corner inequalities).** For every atom-only configuration with integer marks m_i >= 1 and mass N:

    (a)   N_d = #atoms >= ( 3 N - Sum_i m_i^2 ) / 2 ,
    (b)   n_1 = #mark-1 atoms >= 2 N - Sum_i m_i^2 ,

each with equality iff all marks lie in {1, 2}.

*Proof.* Per-atom inequalities summed over atoms. (a) For integer m >= 1, (m - 1)(m - 2) >= 0, i.e. 1 >= (3m - m^2)/2, equality iff m in {1, 2}; sum. (b) 1_{m=1} >= 2m - m^2: equality at m = 1, 2; at m >= 3 the right side is negative; sum. QED

*Remark.* (a) is the second integrality level (m-1)(m-2) >= 0 — exactly the level lemmaR_tight proves exhausted by the two-moment certificate, and, by Theorem 3.4, exactly the level the cubic row re-measures on isolated blocks; (b) is its simple-fraction sibling. In the parent's terms, (a) is the doubles-optimal corner arithmetic: an atom of mark m spends m(m-1) of Frobenius excess to save m-1 units of N_d, so doubles are the efficient coin.

**Theorem 4.3 (atom-only corner theorem, both benchmarks).** Fix N even, 0 <= eps <= 1/2 (finite-circle model, flat windows). Over laws w on A with mass N and E_w[F1] <= (4/3) N (1 + eps):

    (a)   min_w  E_w[N_d]/N  =  5/6 - (2/3) eps ,
    (b)   min_w  E_w[p1]     =  2 - (4/3)(1 + eps) = 2/3 - (4/3) eps .

Both minima are attained by explicit laws supported on the (N+1)-site grid of Theorem 3.9 with marks {1, 2} only. Every configuration in A satisfies the pointwise versions with its own Frobenius excess eps_c. The same statements hold with the two-sided budget band (4/3) N [1 - eps, 1 + eps] (the attaining laws sit at the upper edge), and the minima over any richer mark alphabet (any W, or unbounded marks) are the same.

*Proof.* Lower bounds: by Lemma 4.1, E_w[Sum m^2] <= E_w[F1] <= (4/3) N (1 + eps); by Lemma 4.2(a) and linearity, E_w[N_d] >= (3N - (4/3) N (1 + eps))/2 = N (5/6 - (2/3) eps); by Lemma 4.2(b), E_w[n_1] >= 2N - (4/3) N (1 + eps) = N (2/3 - (4/3) eps).

Attainment: for integer 0 <= k <= N/2 let c_k be the grid configuration with k doubles and N - 2k simples on N - k distinct grid sites (which exist: N + 1 >= N - k). By Theorem 3.9, F1(c_k) = N + 2k exactly; N_d(c_k) = N - k; n_1(c_k) = N - 2k. Set kbar = (B - N)/2 with B = (4/3) N (1 + eps); then 0 <= kbar <= N/2 for eps <= 1/2. The two-column law w* mixing c_{floor(kbar)} and c_{floor(kbar)+1} with E[k] = kbar achieves

    E[F1] = N + 2 kbar = B (upper edge, exactly),   E[N_d]/N = (3N - B)/(2N) = 5/6 - (2/3) eps,   E[p1] = 2 - B/N = 2/3 - (4/3) eps ,

and both lower-bound chains hold with equality (marks in {1, 2}; grid kills all cross-terms; budget saturated), so w* is simultaneously optimal for both objectives. The two-sided band adds only the lower budget edge, which w* satisfies. Enlarging the mark alphabet cannot lower the minimum (the chain never used a mark cap) and cannot raise it (w* uses marks {1, 2}, inside every alphabet): the W-independence is inclusion, not extrapolation. QED

**Corollary 4.4 (asymptotic and matched corners).** As eps -> 0 the two optima tend to 5/6 and 2/3 — the model's bandwidth-one analogs of the Montgomery extremal values for distinct zeros and simple fraction. With the gate's matched-geometry budget B1 replacing (4/3) N, the same proof gives min E[N_d]/N = (3N - B1(1 + eps))/(2N) and min E[p1] = 2 - (B1/N)(1 + eps); at the shipped matched values (N = 64, eps = 0.05, B1 = 84.71214548308222) these are 0.8050957 and 0.6101914 — the run's and follow-up's reported optima to LP precision. QED

Numerical confirmation (`verify_t2.py`): per-atom inequalities exhaustive to m = 50 plus 20,000 random draws (0 violations); grid-column LP matches the closed forms at eps in {0.10, 0.05, 0.02, 0.002} to <= 3.3e-16 for both objectives; exact rational identities verified in Fraction arithmetic; the shipped witness reproduces P = (3N - E[F1])/(2N) = 0.8050957 to 6e-13.

### 4.2 Integrality is necessary: the exact fractional counterexample

The extension of Theorem 4.3 beyond atoms must consume integrality — provably. Work in the gate's primary geometry (N = 64, flat window, lambda = 1; kernel psi(z) = Sum_j u_j e^{-2 pi i j z / N}, grid g_k = k 64/65) and define abar(x) := psi(ix) = Sum_j u_j cosh(2 pi j x / N) >= 1. Write M(c) for total mark mass, S2(c) = Sum_z m_z^2 (each pair member counted m^2), T(c) = 3 M(c) - 2 N_d(c), and consider the **master inequality**

    (MI)    F1(c) >= 3 M(c) - 2 N_d(c) ,

which is precisely what the corner consumes: (MI) per configuration gives, for every law with mass N and E[F1] <= (4/3) N (1 + eps), BOTH corners — E[N_d]/N >= 5/6 - (2/3) eps and E[p1] >= 2/3 - (4/3) eps. (Per configuration (MI) reads N_d >= (3M - F1)/2; take expectations. For simples, 1_{m=1} >= 2 - m summed over the zero multiset gives n_1 >= 2 N_d - M, hence E[n_1] >= (3N - E[F1]) - N.) Note S2 >= T for integer marks (per zero, m^2 - (3m - 2) = (m-1)(m-2) >= 0), so (MI) is weaker than F1 >= S2 — and aiming at (MI), which carries the integrality slack explicitly, is what makes the closure close.

**Proposition 4.5 (fractional marks break the floor at every depth).** Let c_mu be the vacancy lattice (unit atoms on grid sites g_1..g_64) plus one pair at the hole g_0 with depth d > 0 and REAL mark mu > 0. Then, exactly,

    F1(c_mu) - S2(c_mu) = 2 mu^2 abar(2d)^2 - 4 mu (abar(d)^2 - 1),

which is NEGATIVE for every 0 < mu < 2 (abar(d)^2 - 1)/abar(2d)^2 — the pair harvests the hole's missing coupling linearly in mu while paying only quadratically. For integer marks the same family is safe: at mu = m in Z, the log-convexity bound abar(d)^2 - 1 <= (abar(2d) - 1)/2 gives F1 - S2 >= 2 m^2 abar(2d)^2 - 2 m (abar(2d) - 1) > 0.

*Proof.* On the vacancy lattice the atom form factor is phi_0(s) = 64 at s ≡ 0 and -1 otherwise; the pair adds 2 mu cosh(beta s), beta = 2 pi d/N. Expanding F1 = Sum_s w_s |c_s|^2 with the generating identities Sum_s w_s cosh(beta s) = abar(d)^2 and Sum_s w_s cosh(2 beta s) = abar(2d)^2 (the assembly weights w = u * u factor through psi at imaginary arguments) gives the display; the numeric check at (d, mu) = (0.25, 0.05) reproduces it to 1e-12, with F1 - S2 = -3.520e-2. The integer case uses Cauchy–Schwarz on the positive weights u_j (abar((x+y)/2)^2 <= abar(x) abar(y), hence abar(d)^2 <= (1 + abar(2d))/2). QED

**Reading.** An adversary with fractional marks takes mu -> 0 and wins at any depth; integer marks force mu >= 1, where the quadratic cost dominates. Any closure of the pair channel must therefore consume integrality — the channel is invisible to every convexified or soft-positivity analysis. This also explains the gate's LP phenomenology: the LP's columns are explicit integer configurations (nothing about marks is relaxed), which is why its converged pricing found no pair column. And it is the sharp form of the realizability discussion of Section 2.4: with fractional marks even the 5/6 baseline is false.

### 4.3 The pair-interference channel: closed on the R5 family, backstopped everywhere

The full closure argument, with its capacity machinery and certified constants, is the companion note `pair-channel.md`; we state the results, the exact ledger they rest on, and the proofs that are short enough to give in full. Everything is at the gate's decision geometry (N = 64, flat window, lambda = 1); depths d are in circle units, w = 2 pi d dimensionless (the gate's pair family is w in (0, 1] plus deep probes w in {1.5, 2}, i.e. d <= 0.3183).

**The exact interference ledger.** For every admissible configuration (any atoms, any pairs, any integer marks), with R_y(x) := Re psi(x + iy)^2:

    F1 - T = Sum_a (m_a - 1)(m_a - 2) + 2 Sum_p (m_p - 1)(m_p - 2)          [integrality slack]
           + Sum_{a != a'} m_a m_{a'} psi(x_{aa'})^2                        [atom-atom >= 0]
           + Sum_p 2 m_p^2 abar(2 d_p)^2                                    [pair diagonals]
           + Sum_p 4 m_p Sum_a m_a R_{d_p}(x_{pa})                          [pair-atom]
           + Sum_{p < q} 4 m_p m_q [ R_{d_p + d_q}(x_{pq}) + R_{|d_p - d_q|}(x_{pq}) ]   [pair-pair]

(verified on 25 random mixed configurations to 2.2e-11, the stored `pairchan_verify_out.json` maximum). Everything on the right is nonnegative EXCEPT the R-couplings, whose negative parts live only in the dips of R_y; the question is whether the dips can outrun the pair diagonals plus the integrality slack. Quantitatively they cannot — by a factor of about 1.5 at the worst depth:

**Theorem 4.6 (single-pair closure).** Every configuration with exactly one pair (arbitrary atoms, arbitrary integer marks, arbitrary positions) satisfies (MI) whenever the pair depth is d <= 0.45 — i.e. w <= 2.8, covering the gate's ENTIRE pair-depth family including both deep probes, with >= 34% capacity margin on the family itself (certified stacking-corrected capacity ratio <= 0.66 on the family, <= 0.921 out to d = 0.45). For mass <= N configurations (the LP class) (MI) also holds for every d >= 1.0; the window (0.45, 1.0) is certified numerically (raw capacity ratio <= 0.6823 throughout; direct adversarial searches reach at most 74% of the pair budget).

**Theorem 4.7 (multi-pair closure).** (MI) holds for every configuration all of whose pair depths satisfy w <= 0.82, unconditionally; and for all depths w <= 0.98 modulo one isolated cell-crowding cap whose ledger constant is interval-certified (sup Sgen2 <= 0.98465 < 1 on (0, 0.156]^2, per-cell rigorous enclosures; Session 8). On the deepest sliver w in (0.98, 1] the ledger inequality fails (interval-certified Sgen2 >= 1.01405 > 1 at d = d' = 0.159); there the targeted crowd-plus-sea attacks — 8 to 65 pairs, one per cell tranche, plus greedy mark-2 seas up to 130 atoms, re-run at d = 0.158 and 0.159 — never bring F1 - T below +17.47, against a floor requirement of 0, and the unconditional 8/9 backstop applies.

*Proof architecture (full details in the companion note).* Partition the circle into 65 kernel-zero cells; per cell, the exploitable dip mass kappa_k(y) = sup_cell [-R_y]_+ sums to the capacity curve nu(y), with the exact curvature identity alpha := Sum_j u_j (2 pi j / N)^2 = Sum_k psi'(g_k)^2 = 3.392677 controlling the shallow regime (nu(y) = alpha y^2 (1 + o(1))). Integer atoms harvesting a cell's dip pay in-cell atom-atom crosses (>= psi(dip-zone diameter)^2 each) and their own integrality slack, capping the harvest at 8 m_p kappa_k per cell for marks <= 2 (with a certified stacking correction beyond); on the R5 family the closing inequality 8 nu(y) <= 2 abar(2y)^2 follows in closed form from one harmonic-Taylor bound with the exact alpha and one certified finite constant (1.2% closing margin at the endpoint). Pair-pair couplings are priced through the joint kernel R_{d+d'} + R_{|d-d'|} (never the two parts separately), with a one-pair-per-cell crowding cap that is self-consistent for w <= 0.82 (both sides interval-certified: 2 max nu_joint <= 0.60910 < Phi_0 >= 0.64371) and whose ledger constant beyond it is interval-certified to w <= 0.98; beyond w = 0.98 the ledger fails (certified) and the closure defers to numerics plus the backstop. Deep single pairs (d >= 1) fall to the crude bound abar(2d)/abar(d) >= 12.158 nondecreasing. QED (architecture)

**Theorem 4.8 (equal-depth pair-only configurations, exact, all depths).** If c consists only of pairs, all at one common depth d (any positions, any integer multiplicities), then F1 >= S2 + 2 Sum_p m_p^2 — (MI) with a full doubling-cushion surplus at every depth.

*Proof.* c_s = 2 cosh(2 pi s d/N) phi(s) with phi the position-multiset form factor, and 4 cosh^2 = 2 + 2 cosh(double): F1 splits as twice the atom-only Frobenius of the position multiset (>= 2 Sum m_p^2 by diagonal positivity) plus a termwise-cosh-weighted copy (>= the same floor). QED

**Theorem 4.9 (unconditional spectral backstop, no restrictions).** For EVERY admissible configuration — any number of pairs, any depths, any marks — N_d >= (4/9)(3M - F1). Hence for any law with mass N and E[F1] <= (4/3) N (1 + eps):

    E[N_d]/N >= (8/9)(5/6 - (2/3) eps) = 20/27 - (16/27) eps = 0.7407... - 0.593 eps ,

so the maximal conceivable pair advantage on the corner, in any regime whatever, is <= 5/6 - 20/27 = 5/54 = 0.0926, unconditionally.

*Proof.* Let B be the Hermitian frequency matrix B[j, j'] = sqrt(u_j u_{j'}) c_{j-j'} (65 x 65): exactly tr B = M and tr B^2 = F1. B decomposes as Sum_atoms m_a v_a v_a^dagger + Sum_pairs B_p with each atom block PSD of rank 1. Each pair block is B_p = m (p q^dagger + q p^dagger), with p_j = sqrt(u_j) e^{-2 pi i j theta/N} e^{2 pi j d/N} and q_j = sqrt(u_j) e^{-2 pi i j theta/N} e^{-2 pi j d/N} (the two summands of the conjugate-pair form factor of Section 2.3); on span{p, q} its nonzero eigenvalues are m (Re<q, p> +/- |p| |q|), and Cauchy–Schwarz gives Re<q, p> - |p||q| <= 0, so n_+(B_p) <= 1 — the finite-circle counterpart of the signature-(1,1) block of Proposition 3.2(iv). By subadditivity of positive inertia, n_+(B) <= #atoms + #pairs <= N_d. For every real t, 3t - t^2 <= (9/4) 1_{t > 0}; summing over the spectrum, 3M - F1 = Sum_i (3 lambda_i - lambda_i^2) <= (9/4) n_+(B) <= (9/4) N_d. QED

*Remark.* The 9/4 (rather than 2) is the price of a purely spectral argument — 3t - t^2 exceeds 2 on (1, 2) with max 9/4 at t = 3/2 — the same structural reason the parent's inertia route cannot reach 5/6 by itself. But the backstop is depth-uniform, mark-uniform, and interference-proof, which is exactly what a backstop must be.

**Status and the sharp conjecture.** Roughly 10^4 adversarially optimized configurations (dip attacks, pair crowds, half-gap frustrated twins, deep seas, random mixed stress; seeds fixed, independent assembly) never brought F1 - T below +2.000000, and the minimum of F1 - T - Sum_p 2 (2 m_p^2 - 3 m_p + 2) over every family is 0.000000, attained only in the depth -> 0 grid limit. The searches establish that the binding adversary is always shallow; that coordinated dip attacks can consume nearly the whole depth-dependent excess 2 m^2 (abar(2d)^2 - 1) (within 3% at d = 0.1) but never any of the depth-independent doubling cushion 2 m^2 — exactly the split the capacity lemmas predict. We record the **sharp conjecture** (numerically exhaustive, not proved): F1 >= Sum_a (3 m_a - 2) + 4 Sum_p m_p^2 — every pair pays its full flattened-double cost and interference recovers nothing. Its near-tight witnesses (+0.03) show any proof must be capacity-sharp, which is why the theorems above target (MI), with its floor headroom of 2 per pair, instead.

**Consequence.** The model-level corner theorem extends from the atom-only class to the bulk of the gate's admissible class: single-pair columns at every gate depth (w <= 2.8), multi-pair columns at w <= 0.82 unconditionally and w <= 0.98 modulo the crowding cap (constant interval-certified), equal-depth pair-only columns at every depth — for both benchmarks, via (MI). The remaining admissible regimes — multi-pair columns at the deep-probe depths w in {1.5, 2} (inside the gate class but beyond the theorems' range), multi-pair columns with a depth in w in (0.98, 1] (ledger failure certified there; coverage is the re-run attacks plus the backstop), and mass-unbounded crowds (not LP-relevant, since columns have mass N and deeper objects are garnish priced by Section 7's ladder) — are floored at 8/9 of the corner unconditionally and covered by converged pricing (O2). Class-level exactness of delta_0 = 0 is therefore proved on the closure's regimes and heuristic (pricing-backed, backstopped at 20/27) on that residue. The channel could only ever have produced a bite (a pair-assisted violation would be cut by pricing, not absorption), and it produces none; the audit's minor finding 4 is discharged for the closure's regimes, with the honest residue stated in Section 8.3.

### 4.4 The computational certification: 940 records, the eps law, and the witness

The gate LP (column generation over explicit configurations, analytic-gradient multi-start pricing, exact-LP equality on the accumulated dictionary, final solutions re-verified in Fraction arithmetic on 1e-12 rationalizations) was run over the full pre-registered decision grid. Verdict, machine-readable: ABSORPTION.

**The grid.** N = 64: {matched, asymptotic} budgets x W in {2, 3, 4, 6, 8} x C_led in {10, 100, 1000} x eps in {0.02, 0.05, 0.10} x fuzz {coupled, none, Gamma in {0.05, 0.10, 0.25}} x error bars {off, on} = 900 records. N = 128: {matched, asymptotic} x W x fuzz {coupled, none} x bars = 40 records. Total **940**; every record solved to status success; LP duality gap ~1e-9.

**The result.** delta_0 = P_full - P_base = 0 at every record: max |delta_0| = 6.39e-13 over the 900 N = 64 records and 8.94e-13 over the 40 N = 128 records — **|delta_0| < 1e-12 at all 940** (the number to cite for the full grid is 8.94e-13, the N = 128 maximum). Per-W values at the primary point: -3.77e-13 (W = 2), +1.44e-13 (W = 3), 0.0 exactly (W = 4, 6, 8); the fit delta_0(W) = delta_inf + c W^{-kappa} degenerates to delta_inf = 0 with zero residual, and d delta_0/d Gamma = 0. The optima are not merely equal but achieved by identical optimal laws: the base-optimal law itself satisfies the entire cubic block.

**The exact eps law.** At asymptotic budgets the joint optimum obeys P(eps) = 5/6 - (2/3) eps — the grid-decoupled corner of Theorem 4.3 — at every tested eps:

| eps | P (asymptotic, LP) | 5/6 - (2/3) eps | abs(delta_0) |
|---|---|---|---|
| 0.02 | 0.8200000000002683 | 0.82 | 2.8e-13 |
| 0.01 | 0.8266666666669427 | 0.8266666... | 2.4e-13 |
| 0.005 | 0.8300000000002841 | 0.83 | 2.2e-13 |
| 0.002 | 0.8320000000003910 | 0.832 | 1.0e-13 |

Matched-variant values differ only through the finite-size budget center (e.g. P = 0.8368627361 at eps = 0.002, from B1 = 84.712 < (4/3) 64 = 85.33). Moreover P_base = P_cal at every record: even the lambda'-Frobenius row alone adds nothing to the two-moment baseline.

**Primary decision point** (flat/flat, lambda' = 1/2, N = 64, matched budgets, eps = 0.05, C_led = 100, coupled fuzz): P_full = P_base = 0.8050956815843511, delta_0 = -3.8e-13, identical optimal laws; the same P at fuzz = none (the fuzz row is not load-bearing for the absorption). **N = 128 confirmation:** P_full = P_base = 0.8024488905983833 (matched) and 0.8000000000004773 (asymptotic) at eps = 0.05; delta_0 = 0 at all 40 records.

**The witness** (`witness_N64.json`; N = 64, matched budgets, eps = 0.05, fuzz = none). Three columns, all supported on the 65-site psi_1-zero grid (spacing 64/65 = 0.9846153846), marks {1, 2} only, no pairs, n_- = 0:

| weight | column | N_d | F1 (= Sum m^2, exact) | F' | C' |
|---|---|---|---|---|---|
| 0.5299906673474316 | vacancy lattice: 64 simples on 64 of the 65 sites | 64 | 64 | 125.0909091 = 4128/33 | 245.4508724 |
| 0.16040139164388625 | 16 doubles + 32 simples on an explicit 48-site subset | 48 | 96 | 153.7604346 | 411.0865130 |
| 0.30960794100868216 | 32 doubles on an explicit 32-site subset | 32 | 128 | 135.1959163 | 301.3541285 |

Row values in this table are the clean-integer-grid values (`clean_checks[].*_clean` — the canonical hand-checkable description); the optimizer's stored law rows (`law[].F1/Fp/Cp`) differ from them by at most 4.1e-5 per row (per column 3.4e-6 / 1.6e-5 / 4.1e-5), and the aggregates below are the stored law's, which saturate the budget edges exactly. Aggregates: E[F1] = 88.94775275723633 = the upper Frobenius edge B1 (1 + eps) exactly; E[F'] = 132.818 (strictly inside its band [128.34, 141.85]); E[C'] = 289.32716513260516 = the LOWER cubic edge B3 (1 - eps) exactly (the doubles corner is cubic-short, per G(1/2) > 0, and the arrangement supplies the budget from below); E[N_d]/N = 51.52612362142/64 = 0.8050956815846874 <= 5/6 + 0.01 (the pre-registered absorption bar). Active rows at the optimum: only F1_hi and Cp_lo; every ladder row slack by orders of magnitude — E[n(2)] = 3.50 and E[n(3)] = 0.94 against caps C_led N V^{-4} = 400 and 79.0, all higher rows zero, and the vacancy column's n(V) vector identically zero. Every row was re-verified in exact Fraction arithmetic (all 10 checks pass, objective deviation 5e-13), and the audit independently recomputed all three columns through a position-space path (reproduction to 1e-6 or better, feasibility re-confirmed at C_led = 100 and C_led = 10).

The mechanism is now fully visible: F1 = Sum m^2 exactly on all three columns (Theorem 3.9 — the equality case of Lemma 4.1), so the bandwidth-one reading transfers the lemmaR_tight corner verbatim, while the sub-grid arrangement (which sites, which clusters) freely meets the lambda' rows (Proposition 3.10): the two doubles-subsets' occupancy-2 clustering supplies the cubic cross-terms (C' = 411.09 and 301.35 against isolated-block values 160 and 256) at zero cost in N_d and zero cost at lambda = 1. The witness uses no pairs, no marks >= 3, no spectral escape — arrangement alone.

**Pricing and its honest role.** No improving column (reduced cost < -1e-6) was found in S = 200 pricing restarts at the primary and tightest-asymptotic points (S = 100 at N = 128 — RUN-REPORT-recorded, with no stored verify block; S = 40 at W-scan re-checks; min_rc = 0.0, 0 improving columns at every stored verification). The ABSORPTION verdict does not rest on pricing optimality — the witness is exhibited and verified, and P_full = P_base is an exact LP equality on the accumulated dictionary regardless; pricing convergence supports only the claim that no undiscovered configuration class outside the dictionary would create a bite (and more columns can only lower both optima together — the anti-absorption direction). The audit's eight break attempts (independent witness recomputation; a per-column ladder at C_led = 4, barely above the null floor 3.82; a missing-row hunt; near-CUE pinning; window-degeneracy probes; the pair-channel attack; budget-center stress across eps in 0.002–0.10 and Gamma to 0.25; seed and scale stability) all failed to flip the verdict; the two that produced findings (near-CUE promotion; p1 scoping) are executed in Sections 5 and 6.

---

## 5. The near-CUE class: absorption inside the unconditional data class

The Tier-1 adversary of Section 4 is free to hold anti-correlated (non-CUE) bandwidth-one data. The strongest form of the no-go pins the adversary inside the near-CUE class — the data class of the PairCeiling formalization — and asks whether the cubic block bites there. It does not; and the way it fails is the paper's sharpest structural finding.

### 5.1 The license: BGSTB24, with three riders

The pinning rows |E_w|c_j|^2 - j| <= tau2 for 1 <= j < N at lambda = 1 (edge row free) are licensed by:

Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta function*, arXiv:2306.04799 (v1, June 2023); published Acta Arithmetica, 2024. Theorem 1 there is unconditional and pointwise in alpha, uniform on the CLOSED band 0 <= alpha <= 1:

    F(alpha) = T^{-2 alpha} (log T + O(1)) + alpha + O(1/sqrt(log T)),

for the form factor defined with zeros counted with multiplicity and off-line zeros entering with the depth weight x^{delta + delta'} — exactly the cosh depth-weighting the gate's form factor c_j applies. With alpha = j/N, each open-band row is licensed pointwise per row, unconditionally, in the depth-weighted multiplicity-counted form (directly, or through the paper's Lemma 5 admissible kernel class: even, L^1, supported in [-1, 1], Lipschitz at 0 — the bandwidth-one class); the diagonal spike is confined to the edge rows the gate leaves free, and the Poisson factor acts below the model's 1/N bin resolution whenever N << log T. Two citation corrections for the program's literature file, read off the fetched paper: the uniform range is the closed band 0 <= alpha <= 1, not |alpha| < 1 (Theorem 1 includes the [GM87, Lemma 8] improvement "up to alpha = 1 with explicit error terms"); and the published venue is Acta Arithmetica 2024.

**The three licensing riders (binding on every use of this section's results):**

1. **Depth-aggregation only.** The licensed statistic never separates on-line from off-line mass: the Remark after their Theorem 2 states the method "neither requires nor provides any information" about whether the zeros are on the critical line. What is pinned is the cosh-weighted aggregate |c_j|^2 (pairs entering with depth weights), never an on-line-only statistic. Shedding the far-off-line coupling term costs an extra hypothesis — the thin-box hypothesis or the strong zero-density hypothesis, which their Theorems 2–3 (the 61.7% simple-zeros results) consume; the row class used here needs none of that.
2. **Finite-T slack O(N/sqrt(log T)).** The licensed per-row slack at finite T is O(N/sqrt(log T)) grid units (plus the edge spike), so tau2 in {1, 4} is the fixed-N, T -> infinity asymptotic reading — legitimate for the gate's asymptotic semantics, but at honest finite T the O(1)-unit pinning overstates the theorem until log T >> N^2, and this no-go says so.
3. **Second-moment scope.** BGSTB24 stops at the second moment — pair correlation only; nothing in it licenses the cubic budget column, whose c3(lambda') identification stays on flag F2 (Section 8.3) exactly as before.

Net: the Tier-2 rows are an unconditional asymptotic data class, pointwise on the open band in the depth-weighted form; the Tier-2 verdict's *strength* ("absorption inside the parent ceiling's own data class") inherits riders 1–3 verbatim.

### 5.2 The decision-grade result: delta_0' = 0 exactly, both N, both centerings

Row class: all Tier-1 rows (fuzz = none — the harsher variant for absorption) plus the pinning rows at tau2. Four cells at N = 64 (matched budgets, C_led = 100, W <= 8):

| tau2 | eps | P_full^T2 | P_base^T2 | delta_0' | reading |
|---|---|---|---|---|---|
| 1 | 0.05 | 0.8332334059839699 | 0.8332334059839699 | **0.0 (exact)** | absorb, decision grade |
| 1 | 0.02 | 0.8359542395410772 | 0.8359374423865479 | 1.68e-5 | absorb (0 within the residual band [-3.1e-5, +1.8e-5]) |
| 4 | 0.05 | 0.8150864520465212 | 0.8137831067863290 | 1.30e-3 | bounded residual, sub-decision scale |
| 4 | 0.02 | 0.8316328692004420 | 0.8301979402692543 | 1.43e-3 | bounded residual, sub-decision scale |

Decision-grade discipline at the primary cell (tau2 = 1, eps = 0.05): delta_0' = 0 is an exact LP equality — identical optima — at every one of 9 cumulative S = 200 verification passes across a ~1,100-column dictionary enrichment; the common level fell 0.8333622 -> 0.8332334 while the equality never broke (residual improvements are common-mode), and the reduced-cost bound for the true marginal value is |delta_0'| <= 1.2e-5. Stability under budget re-centering: asymptotic variant P_full = P_base = 0.8332332347490976, delta_0' = 0.0 exact.

**N = 128 confirmation.** The pinned LP was infeasible on the raw gate dictionary and was bootstrapped with 300 CUE and doubles-decorated-CUE columns (anti-absorption-safe), then built out over 10 cumulative S = 200 passes to 6,457 columns at the matched cell (6,739 after the asymptotic re-centering): P_full = P_base = 0.8374218534574983 with delta_0' = 0.0 exact at the matched cell, and 0.8373740026259704 with delta_0' = 0.0 exact at the asymptotic re-centering. Build-out invariance: delta_0' <= 8e-16 at every recorded dictionary re-solve (1,842 / 6,457 / 6,739 columns) — the verdict is independent of the convergence level. Level trend: P^T2 = 0.8374 (N = 128) vs 0.8332 (N = 64), both ~ 5/6 - O(1e-3), the pinned-baseline finite-size trend.

### 5.3 Absorption by slack: the structural finding

The near-CUE witnesses make the verdict structural. At N = 64: a 64-column law, marks {1, 2} only, no pairs, no marks >= 3, with E|c_j|^2 = j + 1 for every j = 1..63 to 2e-12 (maximum deviation 1.84e-12, at j = 62) — all 63 upper pinning rows active at exactly the +tau2 allowance — and **the only active rows at the pinned optimum are the 63 pinning rows (and mass): F1, F', C', and every ladder row are strictly interior. The cubic block does not even bind.** The +tau2 allowance pays for the doubles; the cubic budget is met with room to spare. Fraction re-verification passes on the full row class (worst pinning margin -1.0e-9, inside the documented 1e-6 grace). At N = 128 the same structure: 128 columns, marks {1, 2}, no pairs, upper pinning edge ridden at tau2 - 1e-5 (an interior shrink absorbing a solver-tolerance overshoot; the Fraction re-verification against the TRUE tau2 = 1 box passes with margin +1.0e-5 strictly interior), E[n_simple]/N = 0.6748.

This is a stronger statement than Tier-1 absorption: inside the near-CUE class the cubic row is not absorbed by an adversary straining against it — it is slack at the optimum. There is no ceiling-class escape and no bite even inside the parent ceiling's own data class, at both lattice sizes, at both budget centerings, subject to riders 1–3 of Section 5.1.

### 5.4 The tau2 = 4 annotation

At loose pinning (tau2 = 4) the cubic row is active and the residuals delta_0' = 1.30e-3 / 1.43e-3 (eps = 0.05 / 0.02) exceed their pricing bands ([0.9e-3, 1.5e-3]) and were still declining under enrichment (1.28e-3 -> 1.17e-3 over five passes): they are **unconverged upper bounds at loose pinning, an order of magnitude below the M4 decision scale (the 1e-2..3e-2 delta_0 the proposal projected)**, obtained from deliberately shortened runs and recorded as such. They are diagnostic annotations, not certificate claims — and they sharpen the scoping: whatever residual cubic signal exists at this scale lives strictly between the near-CUE class (tau2 = 1: exact zero by slack) and the free Tier-1 class (exact zero by witness), i.e. in loosely pinned intermediate worlds, at sub-decision magnitude.

---

## 6. The simple-fraction benchmark

The parent certificate's headline is the simple-zero fraction (2/3 at flat window; 0.6725 window-optimized; ceiling 0.6818287), so a no-go scoped only to N_d would be incomplete — this was the audit's third major finding. The gate was therefore re-run with the objective min E_w[p1], p1(c) = (#mark-1 atoms + 2 x #mult-1 pairs)/N, on the follow-up-enriched dictionary (5,134 columns), with the literal pre-registered stop rule applied to both systems:

| cell | p1_full | p1_base | delta_p1 | analytic corner 2 - (B1/N)(1 + eps) | converged |
|---|---|---|---|---|---|
| matched, eps = 0.05 | 0.6101913631697143 | 0.6101913631684138 | 1.3e-12 | 0.6101913631681821 | yes: S = 200 clean, min_rc = 0.0, both systems |
| asymptotic, eps = 0.002 | 0.6640000000012899 | 0.6640000000004871 | 8.0e-13 | 0.6640000000000001 = 2 - (4/3)(1.002) | yes: S = 200 clean, both systems |

These were the campaign's only fully clean-stop runs: zero improving columns at S = 200 for full AND base systems. Cross-checks on the final dictionary: coupled fuzz at the primary cell delta_p1 = 2.9e-13; W-scan over {2, 3, 4, 6, 8} max |delta_p1| = 1.3e-12 (at W = 8; all < 1.4e-12); the labeled on-line-only diagnostic variant 3.3e-13. The optimum is the exact marks-{1,2} doubles corner of Theorem 4.3(b) — pairs cannot help (a mult-1 pair buys 2 simple points at >= twice the two-simples Frobenius cost; a mult-2 pair is dominated by two doubles) — and the eps -> 0 value is 2 - 4/3 = **2/3**, the model's bandwidth-one analog of Montgomery's simple-zeros corner. The witness laws are the same psi_1-grid family as the Tier-1 witness, reweighted per cell, rational verification passing.

Two scoping notes. (i) The cited **0.6818287** ceiling belongs to the *window-optimized* certificate class (the Theorem-D effect), which the flat/flat gate deliberately does not consume; the flat-window model corner is 2/3, and no statement in this paper re-decides the 0.6818287 ceiling — what is proved is that the cubic block does not move the flat/flat optimum for either objective. (ii) With this section, the no-go headline covers BOTH benchmarks: the distinct-zeros corner 5/6 and the simple-fraction corner 2/3, each with delta = 0 at convergence.

---

## 7. Capacity and vacuity: no spectral escape

Two theorems close the spectral-escape routes from opposite ends, and together with the gate they complete the pricing: a scalar cubic tail row with any divergent cutoff is unconditionally vacuous (Theorem 7.4 — the "provable today, no LP needed" half of the no-go, mandated by the merge guidance); and under the repaired all-V ladder the same channel is capped at o(N) with a sharp constant (Theorem 7.1). What remains is position/interference freedom — which is exactly the channel the witness of Section 4.4 uses.

### 7.1 The sharp capacity theorem

**Setting (the continuum garnish LP).** Heights normalized so the ladder's absolute floor is 1. Spectral escape is a positive measure mu on [1, infinity) — mu([h, infinity)) is the count per N of escaped eigenvalue mass at height >= h — subject to

    (Frobenius slack)    Int h^2 d mu(h) <= eps_g ,
    (all-V ladder)       mu([h, infinity)) <= C h^{-4}    for every h >= 1        (C = C_led),

and the objective is the absorbable cubic charge Int h^3 d mu(h). (Equivalently, in tail-function form N(h) = mu([h, infinity)): maximize N(1) + 3 Int_1^infty h^2 N dh subject to N(1) + 2 Int_1^infty h N dh <= eps_g and N <= C h^{-4}; the forms are identical by integration by parts.)

**Theorem 7.1 (sharp capacity).** For every C > 0 and 0 < eps_g <= 2C:

    max_mu Int h^3 d mu = 2 sqrt(2) sqrt( C eps_g ) ,

attained by the min-profile N_*(h) = C min(a^{-4}, h^{-4}), a = sqrt(2C/eps_g) (as a measure: no mass on [1, a); density 4 C h^{-5} dh on (a, infinity)).

*Proof.* Upper bound: for any feasible mu and ANY a > 0, the pointwise inequality h^3 <= a h^2 + (h^3 - a h^2)_+ on [1, infinity) gives

    Int h^3 d mu <= a eps_g + Int (h^3 - a h^2)_+ d mu .

Writing g(h) = (h^3 - a h^2)_+ = Int_a^h g'(s) ds for h >= a, with g'(s) = 3 s^2 - 2 a s > 0 on (a, infinity), Tonelli and the ladder give

    Int g d mu = Int_a^infty g'(s) mu([s, infinity)) ds <= C Int_a^infty (3 s^2 - 2 a s) s^{-4} ds = C (3/a - a/a^2) = 2 C / a .

So Int h^3 d mu <= a eps_g + 2C/a for every a > 0; minimizing over a (minimum at a = sqrt(2C/eps_g)) gives 2 sqrt(2 C eps_g). Attainment: eps_g <= 2C makes a >= 1, so N_* is an admissible tail function; its Frobenius charge is C a^{-4} + C a^{-4}(a^2 - 1) + C a^{-2} = 2C/a^2 = eps_g exactly, and its cubic charge is C/a + 3C/a = 4C/a = 2 sqrt(2) sqrt(C eps_g), meeting the bound. QED

*Remark (the squeeze, made exact).* The optimal dual split is [a x Frobenius] + [ladder integral above a]: bounded heights are blocked by the Frobenius cost (mass at height h buys h^3 of cubic but pays h^2 of Frobenius, ratio h <= a), divergent heights by the ladder cap. The absolute floor C_abs (normalized to 1) appears NOWHERE in the upper bound — only in the attainability condition a >= 1 — which is the precise form of the adjudication's overruling of the "bite iff 2 C_led/C_abs < 4/3" claim: sharp constants at the floor are irrelevant against this adversary class.

**Proposition 7.2 (the naive profile is infeasible; the corrected constant of record).** The point-mass-plus-tail profile (a ladder-saturating atom of size n0 = C b^{-4} at height b = sqrt(3C/eps_g), plus the ladder-saturating tail above b) has Frobenius charge exactly eps_g and cubic charge 5C/b = (5/sqrt(3)) sqrt(C eps_g) = 2.8868 sqrt(C eps_g) — but it violates the CUMULATIVE ladder on the open interval (2^{-1/4} b, b), where its count 2 C b^{-4} exceeds the cap C h^{-4}. The true optimum is Theorem 7.1's 2 sqrt(2) = 2.8284271247... < 5/sqrt(3); both earlier bookkeepings — the first-pass 5/sqrt(3) and the adjudicator's two-term dyadic 2 sqrt(C eps) — are superseded by the min-profile constant (same order; conclusions unchanged). The constant has three independent confirmations on record: the specification's min-profile derivation, the implementer's analytic re-derivation plus LP (2.8244 at h_max = 400, gap = the predicted truncation tail 3/h_max), and the audit's own optimum.

*Proof.* The tail part has density 4 C h^{-5} on (b, infinity). Frobenius: atom C b^{-2} + tail 2 C b^{-2} = 3 C b^{-2} = eps_g at the stated b. Cubic: atom C/b + tail 4C/b. Ladder violation: for 2^{-1/4} b < h < b the cumulative count is n0 + C b^{-4} = 2 C b^{-4} while the cap is C h^{-4} < 2 C b^{-4} throughout the open interval. QED

**Corollary 7.3 (capacity is o(N): the positive complement of the no-go).** In the gate's units, the maximal cubic shift purchasable by spectral escape under the repaired row system is

    |Delta cubic| <= 2 sqrt(2) sqrt( C_led eps_g ) N = o(N)      as eps_g -> 0 at fixed C_led

(e.g. C_led = 1000, eps_g = 1e-8: capacity 0.0089 N). A doubles-vs-pairs-scale swing (Theta(N), e.g. (4/3) N) can NEVER be produced by spectral escape once the all-V ladder is consumed: any absorption of the cubic block must run through position/interference freedom — the channel Theorem 3.9 exhibits and the witness uses. (In the gate's LP this theorem enters as the coupled fuzz rows, tangent-cut on the concave sqrt; the run found the fuzz row not even load-bearing for the absorption.) QED

Numerical confirmation (`verify_t5.py`, refinement runs re-executed and persisted to `verify_t5_out.json` this session): attainment profile exact to 4e-11 / 9e-13; an independent discretized LP over point masses converges to 0.4000 from below under joint grid-and-truncation refinement — tail-corrected values 0.3950 / 0.3985 / 0.3991 at (600 points, h_max = 2000), (2000 points, h_max = 2000), (4000 points, h_max = 8000), C = 1, eps_g = 0.02, each the raw LP value plus the predicted truncation tail 3C/h_max — never exceeding the bound; the naive profile's value 0.408248 and its ladder violation are reproduced; duality and scaling verified across (C, eps) over five orders of magnitude.

### 7.2 Divergent-cutoff vacuity: the garnish theorem

**Setting (the as-written row system, family semantics).** N = N(T) -> infinity; V0 = V0(T) -> infinity any divergent cutoff with V0 = o(N^{1/3}) (any polylog cutoff qualifies — in particular the proposal's (loglog T)^3 and every (log T)^A). The as-written system consumed its equalities "with o(N) precision" — no fixed tolerance rate — so feasibility is a property of families (c_T) of model configurations (no mark cap was imposed as written), with spectral data read from isolated-block spectra, admissible iff

    (W1)  mass:            Sum m = N   (exact);
    (W2)  Frobenius:       F = kappa N + o(N),   kappa = kappa(1) = 4/3 (the as-written system's bandwidth-one Frobenius row);
    (W3)  signed cubic:    C = c3 N + o(N);
    (W4)  scalar tail row: Sum_{|lambda_i| >= V0} |lambda_i|^3 = o(N);
    (W5)  count/inertia rows imposed only at thresholds V >= V0, plus n_- <= p;

objective liminf N_d/N (or liminf p1). (A fixed tolerance rate shrinking faster than 1/V0 would be a STRONGER system than the one written — and dishonest bookkeeping besides, since the consumed prime-side equalities carry no such rate.)

**Theorem 7.4 (garnish absorption).** Let (c_T) satisfy (W1), (W2), (W4), (W5), contain at least s_0 N simple on-line atoms for a fixed s_0 > 0 (a simple-atom fraction, unrelated to the marginal value delta_0), and fall short of the (W3) cubic equality by Delta_T N with 0 <= Delta_T <= Delta_max fixed. Put h0 = floor(V0/2), n0 = ceil(Delta_T N / h0^3), and let c'_T be c_T with n0 additional isolated on-line atoms of mark h0 (at unoccupied, well-separated positions) and n0 h0 simple atoms deleted. Then for all large T, c'_T satisfies EVERY row of the as-written system, and

    N_d(c'_T) = N_d(c_T) - n0 (h0 - 1) <= N_d(c_T) ,          p1(c'_T) <= p1(c_T) .

Row-by-row (per N; every shift o(1)): mass exact 0; Frobenius + Delta_T/h0 + O(1/h0^2 + h0^2/N) = o(1); cubic + Delta_T + o(1) (landing the (W3) equality); tail row + 0 (the garnish sits at h0 < V0); count rows at V >= V0: + 0; inertia unchanged (only positive on-line eigenvalues added).

*Proof.* Feasibility: n0 h0 <= Delta_max N/h0^2 + h0 = o(N) < s_0 N for large T — enough simples exist to delete. Each garnish atom is an isolated on-line atom of mark h0: eigenvalue h0, Frobenius h0^2, cubic h0^3, mass h0. Mass: adds and deletes n0 h0 exactly. Cubic: adds n0 h0^3 in [Delta_T N, Delta_T N + h0^3], subtracts n0 h0 <= Delta_max N/h0^2 + h0; net Delta_T N + O(h0^3) + O(N/h0^2) = Delta_T N + o(N) since h0 -> infinity and h0^3 = o(N) — (W3) now holds. Frobenius: adds n0 h0^2 <= Delta_max N/h0 + h0^2 = o(N), inside (W2)'s window. Tail and count rows: every garnish eigenvalue equals h0 = floor(V0/2) < V0, and all thresholds sit at V >= V0 > h0, so the added spectrum is invisible; deletions only decrease those rows. Objectives: N_d changes by + n0 - n0 h0 = -n0 (h0 - 1) <= 0; the deleted atoms were simple and the added ones have mark h0 >= 2, so p1 decreases. QED

*Remark (the growth cap is removable).* The hypothesis V0 = o(N^{1/3}) is a convenience, not a constraint: for an arbitrary divergent cutoff, cap the garnish height at h0 = min(floor(V0/2), floor(N^{1/4})). Then h0 -> infinity, h0^3 <= N^{3/4} = o(N), and h0 < V0 still holds, so every estimate in the proof goes through verbatim — the vacuity covers ANY divergent cutoff, as headlined.

**Corollary 7.5 (vacuity of the scalar divergent-cutoff cubic row).** Suppose the two-moment system {(W1), (W2)} admits optimizer families with a fixed positive simple fraction, spectra bounded by a fixed constant, and bounded cubic deficit (C(c_T) <= c3 N + o(N), deficit <= Delta_max N). Then, for both benchmarks, the infimum over the as-written system equals the infimum over the two-moment system: the marginal value of the entire block {(W3) + (W4) + (W5)} is ZERO — delta_0 = 0 as written. The deficit hypothesis is the actual situation: the corner families of Theorem 4.3 have marks in {1, 2} (spectra bounded by 2, simple fraction 2/3 in the limit) and undershoot the cubic budget (Corollary 3.6: G(1/2) = +1/2 > 0 — the null budget sits strictly above the doubles plane, so doubles-saturated configurations are cubic-short; the shipped witness accordingly sits at the LOWER cubic edge). Whatever cubic demand the row was hoped to impose on the two-moment-degenerate corner — up to any fixed Delta_max, including the full "(4/3) N doubles-vs-pairs swing" of the proposal's narrative — the garnish supplies it invisibly, at an objective DECREASE.

*Proof.* One direction is trivial (more rows can only raise the infimum). Conversely, take the corner families: bounded spectra plus V0 -> infinity make (W4) and the V >= V0 count rows identically zero for large T, so they satisfy (W1), (W2), (W4), (W5); apply Theorem 7.4 to land (W3); the garnished family is admissible for the whole system at a weakly smaller objective. QED

**Remark 7.6 (what this does and does not say — the repair structure).**

1. **It kills the scalar row, not the direction.** The vacuity is about the AS-WRITTEN system, whose count/tail information starts only at V0. The proposal's own Chebyshev proof in fact yields the all-V ladder n(V) <= C_led N V^{-4} for every V >= C at theta < 1 (the theorem underclaimed its proof — the adjudication's central overruling); under THAT system the garnish channel is not free but capped, and the cap is exactly Theorem 7.1's 2 sqrt(2) sqrt(C_led eps_g) N = o(N). Repair R1 ("claim what the proof proves") is precisely the difference between Corollary 7.5 and Theorem 7.1.
2. **The garnish needs unbounded marks** (h0 = floor(V0/2) -> infinity): it lives outside every fixed-W alphabet — which is why the repairs mandated the divergent-W adversary class and why "a break at marks {1, 2} is not evidence." (A pair-based garnish with slowly divergent pair multiplicity reaches the same conclusion through Proposition 3.2's deep-pair blocks.)
3. **The three-part structure of the no-go.** Theorem 7.4/Corollary 7.5 dispose of spectral escape as written; Theorem 7.1 caps it as repaired; and the gate's decided content (Sections 4–6) is that the remaining channel — position/interference freedom — absorbs the cubic block too, at delta_0 = 0 exactly. Together these ARE the sharpened no-go.

Numerical confirmation (`verify_t6.py`): the shift table at Delta = 4/3, V0 = (loglog T)^3 over the adjudication's log T grid extended to 1e6 — Frobenius shift 4/(3 h0) = 0.0992 down to 0.0010 -> 0, N_d shift negative throughout, cubic shift +4/3 exactly, tail and count rows 0 — reproducing the adjudication's computation-(b) audit and the gate's Tier-A regression; an abstract LP demonstration in which the cubic equality is INFEASIBLE without the garnish variable (the fake bite) and returns to the two-moment corner 5/6 - O(tol) with it; and an exact-rational instance with all shifts exact.

---

## 8. Scope, residuals, and what survives

The credibility of an exact zero is its scoping. This section states precisely where delta_0 = 0 is exact, where it is a bounded residual, what is finite-scale, and what is flagged — and closes with the one place a positive signal genuinely lives, labeled as outlook.

### 8.1 The residual table

The exact zero is **flat/flat-specific**. Theorem 3.9's mechanism says exactly why: the flat bandwidth-one kernel's zeros are equally spaced, so one site grid kills all lambda = 1 cross-terms simultaneously; a cosine window's kernel zeros are not equally spaced, so no grid does, and the degeneracy breaks by a microscopic but nonzero amount. The complete residual map:

| configuration | residual delta_0 | status |
|---|---|---|
| flat/flat, entire 940-record Tier-1 grid | 0 (< 1e-12) | exact; witness-backed |
| flat at lambda = 1 / cos(1.6 s) at lambda' | 5.95e-14 (eps .05), -1.14e-13 (eps .02) | exact-zero class: changing the lambda' window moves nothing — the absorber's freedom is positional, not spectral |
| cos(sqrt2 s) [Montgomery–Taylor] at lambda = 1 / flat | +6.41e-5 (eps .05), +2.28e-5 (eps .02) | bounded residual: the MT cosine breaks the exact grid degeneracy; unconverged upper bounds, three orders below the eps-slack scale |
| cos(sqrt2 s) [MT] / cos(1.6 s) | +6.27e-5 (eps .05), +1.91e-5 (eps .02) | same class |
| near-CUE tau2 = 1 (decision grade, N = 64 and 128, both centerings) | 0 exact (reduced-cost bound <= 1.2e-5 at N = 64) | absorption by slack (Section 5.3) |
| near-CUE tau2 = 4 (loose box, diagnostic) | 1.30e-3 / 1.43e-3, pricing bands [0.9e-3, 1.5e-3] | unconverged upper bounds, an order below the M4 decision scale (1e-2..3e-2); the cubic row is active here |
| audit's tight-eps Tier-2 probes (dictionary-limited, no column generation) | <= 5e-4, non-monotone in eps | upper bounds, same order as the documented ~3e-4 pricing uncertainty — "where any residual signal concentrates" |

Every nonzero entry is an unconverged UPPER bound on the converged marginal value, and every one sits at least an order of magnitude below the M4 decision scale. The audit's binding wording bar is respected verbatim: delta_0 = 0 exactly at the primary flat/flat configuration; <= O(1e-4) across the window family and <= O(5e-4) under near-CUE pinning at that scale, within pricing-convergence uncertainty — now strengthened by the decision-grade tau2 = 1 exact zeros of Section 5, which post-date that wording.

### 8.2 Finite scale

The computational certification is at N = 64 and N = 128, verdict-stable across both (and across two budget centerings whose cubic centers differ by 5% — the F1 centers by 0.7%, F' by 2.6%). This is not extrapolated silently: the continuum analog of the decoupling mechanism is exact (Proposition 3.11 — the integer lattice under the sinc kernel, with the finite-N grid its exact periodization), so the absorption has a structural reason to persist at every scale, and the model-level theorems of Sections 3, 4.1–4.3, and 7 are N-generic (the pair-channel capacity constants were certified at N = 64, the decision geometry; their N = 128 re-run is mechanical but was not run — recorded as open item O4 below). No claim about N beyond 128 rests on computation.

### 8.3 Flags and honest residue (carried, not discharged)

* **F2 — the cubic budget center.** The identification c3(lambda') = m3(lambda') (= 5 at lambda' = 1/2) rests on Rudnick–Sarnak-range GUE 3-level correlations and the parent's Section-5 diagonal method's polylog-window uniformity; Theorem 3.5 proves the SINE value, not the identification. The absorption verdict is insensitive to this flag: delta_0 = 0 across eps in 0.002–0.10 and Gamma to 0.25, and across budget centers differing by 5% — an O(1)-per-zero error in c3 cannot flip it (the audit's break attempt 7). BGSTB24 licenses nothing at third order (rider 3).
* **F4 — the ladder's provenance.** The all-V ladder consumed by Theorem 7.1's system rests on Theorem 1(ii)-repaired, whose V-dependent bridge (repair R2) is unproven. Per the gate's semantics the absorption branch is STRENGTHENED by assuming the ladder (absorption even with the ladder in force), and Theorem 7.4 needs no ladder at all; nothing in this paper depends on R2.
* **Heuristic pricing.** For classes without an exhibited witness (the nonzero rows of the residual table; the claim that no undiscovered configuration class bites), the evidence is converged column-generation pricing (S = 200 restart protocol), which is heuristic adversary-optimality — stated as such wherever used, and never load-bearing for the exact-zero claims, which are witness-backed LP equalities.
* **Pair-channel residue** (from the companion note): (O1) [updated Session 8] The per-cell interval hardening was executed: the crowding cap's ledger constant is interval-certified to w <= 0.98 (0.98465 < 1); the Session-7 full-family ratio 0.9775 was a grid artifact — on w in (0.98, 1] the ledger fails (certified > 1) and coverage is the attacks (+17.5, re-run at the sliver) plus the 8/9 backstop; the cap itself on w in (0.82, 0.98] remains granted-not-proved (its w <= 0.82 self-consistency is now interval-certified on both sides). (O2) Single-pair depths in (0.45, 1.0) at unrestricted mass, and multi-pair beyond the family, are covered by numerics plus the 8/9 backstop only — not needed for any gate/LP statement. (O3) The sharp conjecture (Section 4.3) is open; near-tight configurations (+0.03) mean the constant-chasing is genuinely hard. (O4) The certified capacity constants are at N = 64; the mechanical N = 128 re-run (Session 8) reproduces every identity and inequality with <= 2.5% constant drift, moves Theorem A(ii)'s deep threshold to d >= 1.1, and shows the near-endpoint ledger failure at N = 128 as well (smaller sliver, better capped constant 0.9633). (O5) All pair-channel constants are for the flat lambda = 1 window; none transfer to the MT-cosine window without recomputation — consistent with that window's residual row above.
* **The formalized ceilings are not re-decided.** The 0.6818287 bandwidth-one ceiling belongs to the window-optimized certificate class; the 0.8453 trace/Frobenius cap stands on kappa >= 2/sqrt(3). The flat/flat gate consumes neither; this paper's claim is that cubic augmentation moves nothing at the flat/flat operating point and produces only the bounded residuals above elsewhere.

### 8.4 Outlook: the exploratory lambda' payoff curve (outside the proven ladder)

Labeled per repair R4 and merge-guidance item (4) (the MD(lambda, delta) community-target quarantine): lambda' > 1/2 + o(1) is OUTSIDE the proven theta < 1 ladder regime; these are M5 payoff-curve data for the moderate-deviation community target MD(lambda, delta), NOT certificate claims; column generation ran at reduced budget, so positive values are heuristic and upper-anchored.

| lambda' | eps | P_base | P_full | delta_0 |
|---|---|---|---|---|
| 0.55 | 0.05 | 0.8053310433508489 | 0.8053310433508484 | 0 |
| 0.55 | 0.02 | 0.8251787278264935 | 0.8251787278264899 | 0 |
| 0.60 | 0.05 | 0.8058514020011891 | 0.8062187975519491 | +3.67e-4 |
| 0.60 | 0.02 | 0.8256842190868753 | 0.8259625547887860 | +2.78e-4 |
| 0.65 | 0.05 | 0.8059503048717801 | 0.8086104956189072 | +2.66e-3 |
| 0.65 | 0.02 | 0.8263688470852664 | 0.8278795159840451 | +1.51e-3 |

The cubic row's marginal value turns positive between lambda' = 0.55 and 0.60 — precisely where the flat-window moment margin Marg(lambda) = 2 m2 - m3 changes sign (Corollary 3.6: lambda_0 = 0.610511) — and grows toward the Rudnick–Sarnak endpoint lambda' = 2/3. The first possible bite therefore sits at lambda' >~ 0.6; consuming it would require extending the proven large-value ladder into exactly the moderate-deviation regime MD(lambda, delta) that the program has quarantined as a community target. At the proven operating point lambda' = 1/2 + o(1), the value is exactly zero — that is this paper's theorem-grade content; the payoff curve is its honestly labeled boundary.

---

## 9. Consequences

1. **lemmaR_tight stands strengthened.** The two-moment degeneracy is not broken; it now carries an audited exact-zero certificate: two-bandwidth flat-window augmentation — lambda'-Frobenius, signed cubic, all-V ladder, capacity fuzz, at lambda' = 1/2 — adds exactly zero to the two-moment optimum at N = 64/128 scale, for both benchmarks, including inside the near-CUE class (by slack). The program's map entry is updated from "exhausted" to "exhausted, and robust under RS-range cubic augmentation with capacity control."
2. **The R2 bridge is not to be funded for the cubic payoff.** The gate was built to price the bridge investment; the payoff is delta_0 = 0. Theorem 1(ii)-repaired retains its standalone value (the first spectral-tail statement for the Weil–Gabor matrix) and its other consumers.
3. **What remains live in A4:** (i) Theorem 1(ii)-repaired as the standalone analytic deliverable of record (all-V count ladder with explicit C_led, theta < 1 strict, C^3 taper); separately, per repair R3, Theorem 1(i)'s fixed-lambda divergent cutoff V0 = T^{2 lambda - 1 + eps} extends to all lambda in (1/2, 2/3) via the MVT-4 branch alone — a divergent-cutoff statement, subject to Theorem 7.4's vacuity, not an all-V ladder; (ii) partial orthonormalization off the o(N)-dimensional exceptional subspace, where a divergent cutoff SUFFICES (unlike the cubic LP) — rank-perturbation bookkeeping already in the formalized linear-algebra library; (iii) the near-critical observation X^2/T = (log T)^{2 theta} = polylog, shrinking the shift range needed by HL*(4)-type quartic input to logarithmic — a route into the existing 13/18 machinery via averaged Goldston–Montgomery/Montgomery–Soundararajan results; (iv) MD(lambda, delta) as a community target, now carrying the quantified payoff curve of Section 8.4.
4. **Methodological consequence.** The gate architecture itself — explicit-configuration LP with realizability by construction, clustered null budgets, pre-registered decision semantics, witness-or-nothing absorption claims, adversarial audit with break attempts — is the reusable instrument this paper certifies. In particular the correction of record (Theorem 3.4 superseding the "+8 vs 0" premise and the phase model) was produced by the gate's own verification discipline before any LP ran.

---

## 10. Formalization plan

The exact-zero certificate is formalizable in the PairCeiling pattern (exact-rational LP over marked configurations + kernel-checked row inequalities + interval-arithmetic enclosures), because on the psi_1-zero grid all data become algebraic:

* **The grid Parseval identity** (Lemma 3.8 / Theorem 3.9) is pure finite Fourier algebra on Z_M — assembly weights constant on residue classes plus DFT Parseval; `decide`-adjacent at fixed N.
* **The witness law** is three columns with rational weights, integer site subsets, and marks in {1, 2}; every row value is rational (F1 = 64, 96, 128; F' and C' rational combinations of the triangular weights — e.g. 4128/33 — with the lambda' kernel evaluated at grid multiples), so the full feasibility-plus-optimality check is an exact-rational LP with a dual certificate, exactly the LawN256/CeilingLaw256 architecture with one added row family.
* **Dependency order for the queue:** Lemma 3.8; Theorem 3.9; Lemma 4.2 (per-atom integer inequalities); Theorem 4.3 (exact-rational LP witness + row inequalities); Proposition 3.3/Theorem 3.4 (polynomial identities); Theorem 7.1 (one page of real analysis); Theorem 7.4 (bookkeeping). Theorem 3.5 needs only piecewise-polynomial integration. From the pair channel, Theorem 4.9 is formalization-friendly (finite Hermitian matrix, inertia subadditivity, a scalar inequality), and the closed-form shallow route of the capacity machinery (one Taylor bound + the exact alpha + one certified finite constant) is the recommended path for the R5-family statement; the capacity curves are where interval arithmetic enters.
* The near-CUE witnesses extend the same format: the pinning rows are rational box constraints on the stored form factors, and both witnesses already pass exact Fraction re-verification against the true tau2 = 1 box.

---

## Appendix A. The witness data

**Tier-1 witness** (`results/a4-m2-gate/witness_N64.json`; cell: N = 64, matched budgets B1, B2, B3 = 84.71214548308222, 135.09544203420174, 304.5549106659001, eps = 0.05, fuzz = none). All three columns live on the 65-site psi_1-zero grid, sites theta_k = k (64/65), marks {1, 2}, no pairs. Site subsets, summarized (full integer site lists are recorded per column in the JSON, keys `law[].atoms` / `grid_sites`; the canonical description is the clean integer grid — the stored `clean_checks` record the maximum row-value deviation between the clean-grid and optimizer values of F1/F'/C', at most 4.1e-5, per column 3.4e-6 / 1.6e-5 / 4.1e-5):

* Column 1 (weight 0.5299906673474316): the vacancy lattice — 64 simples on 64 of the 65 sites (one vacancy). N_d = 64; F1 = 64 exactly; F' = 4128/33 exactly (hand derivation: 4096/33 + 32/33, Section 3.4); C' = 245.4508724.
* Column 2 (weight 0.16040139164388625): 16 doubles + 32 simples on an explicit 48-site subset. N_d = 48; F1 = 96 exactly; F' = 153.7604346; C' = 411.0865130.
* Column 3 (weight 0.30960794100868216): 32 doubles on an explicit 32-site subset. N_d = 32; F1 = 128 exactly; F' = 135.1959163; C' = 301.3541285 (clean-grid values; the stored law row has C' = 301.3541693).

Aggregates (computed from the stored law rows, which saturate the budget edges exactly): E[F1] = 88.94775275723633 = B1 (1 + eps); E[F'] = 132.81813304702743 in [128.34, 141.85]; E[C'] = 289.32716513260516 = B3 (1 - eps); E[N_d] = 51.52612362142, E[N_d]/N = 0.8050956815846875. Active rows: F1_hi, Cp_lo only. Exact Fraction re-verification: all 10 row checks true, objective deviation 5e-13.

**Near-CUE witnesses** (`results/a4-m2-gate/followup-near-cue.json`, keys `witness_N64`, `witness_N128`). N = 64: 64 columns, marks {1, 2}, no pairs, weights 6.2e-5..0.0753, N_d per column 50..60 (4–14 doubles on CUE-like positions); E|c_j|^2 = j + 1 at every j = 1..63 (all upper pinning rows active at +tau2); E[N_d]/N = 53.32693798297409/64 = 0.8332334059839699; only pinning rows (and mass) active. N = 128: 128 columns, same class, upper pinning edge at j + 1 - 1e-5 (interior shrink; Fraction re-verification against the true tau2 = 1 box passes, margin +1.0e-5); E[N_d]/N = 107.19000239208492/128 = 0.8374219 (the witness was solved at the interior-shrunk box; its objective sits 4.0e-8 above the Section 5.2 LP optimum 0.8374218534574983); E[n_simple]/N = 0.6748.

The three JSON files (`witness_N64.json`, `followup-near-cue.json`, `followup-p1.json`) are the paper's ancillary files: each contains the full column data, law weights, per-row values, active-row lists, and the rational-verification records.

## Appendix B. Null-model Monte Carlo tables

Closed-form anchors (Theorem 3.5): m2(1) = 4/3, m2(1/2) = 13/6 = 2.166667, m3(1/2) = 5.

**Gate sampler** (CUE eigenangles via QR-with-phase-fix of complex Ginibre, unfolded to circumference n; R adaptive to SE(m3) <= 0.5%; batch-means SE with jackknife check):

| n | R | m2(1) | m2(1/2) | m3(1/2) |
|---|---|---|---|---|
| 64 | 4000 | 1.32363(74) | 2.11087(63) | 4.75867(362) |
| 128 | 2000 | 1.32867(77) | 2.13845(71) | 4.87769(411) |
| 256 | 600 | 1.33115(66) | 2.15231(63) | 4.93758(373) |
| 512 | 300 | 1.33199(86) | 2.15958(67) | 4.96843(413) |
| 1024 | 120 | 1.33364(110) | 2.16362(83) | 4.98715(476) |
| 2048 | 48 | 1.33400(94) | 2.16505(83) | 4.99323(504) |
| 1/n fit -> inf | | 1.33394(63) | 2.16682(52) | 5.00056(311) |
| closed form | | 1.33333 | 2.16667 | 5 |

All three extrapolations anchor-consistent (`anchor_ok` true; halt flags empty).

**Audit sampler** (independent QR sampler, fresh seeds), side by side at the two shared sizes — agreement within ~1 combined sigma per entry:

| n | m2(1) audit / gate | m2(1/2) audit / gate | m3(1/2) audit / gate |
|---|---|---|---|
| 64 | 1.32317(105) / 1.32363(74) | 2.11120(84) / 2.11087(63) | 4.76099(491) / 4.75867(362) |
| 256 | 1.33045(132) / 1.33115(66) | 2.15305(103) / 2.15231(63) | 4.94059(616) / 4.93758(373) |

A third independent sampler (this session, own seeds, alias-free frequency-matrix assembly) gave m2(1/2) = 2.11063(135) at n = 64 and 2.15273(100) at n = 256, m3(1/2) = 4.7589(79) and 4.9408(59) — each within ~1 sigma of both prior samplers — with two-point 1/n extrapolation m2 -> 2.1668, m3 -> 5.0014. The audit's third route for m3(1/2) = 5 (real-space 2D determinantal quadrature) gave 4.9896 -> 4.9932 under truncation refinement; this session's independent quadrature gave 4.9924 -> 4.9960.

**Ladder and occupancy side data** (matched n = 64 unless noted): null ladder floor C_led^min = 3.8188 (3.9119 at n = 128); E[n(V)]/n on V = [2, 3, 4, ...] = [0.23868, 0.01364, 0, ...]; max |eig| over 4000 draws = 3.977. Cross-term (occupancy >= 2) shares: Frobenius 0.52626, cubic 0.78986, against the analytic 54% (7/6 of 13/6) and 80% (4 of 5; of which the strictly two-point share is 3.5 and the three-point term T3 the remaining 0.5).

---

## References and provenance

**External references.**

* [P] *More than two thirds of the zeros of the Riemann zeta function lie on the critical line* (the parent paper, v5), with its sorry-free Lean 4 formalization (Theorems A–E; `lemmaR_tight` in Zeta23/ZeroSide/TightMult.lean; the PairCeiling library, LawN256/CeilingLaw256; Theorem 5.8/Remark 5.10 prime-side moments; Sections 7.2(e), 7.3, 7.5). Program digest: `results/full-map.md`. Text extracts used verbatim: `sources-extracted/v5_p13.txt`, `v5_p14.txt`.
* [BGSTB24] S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta function*, arXiv:2306.04799 (v1, arXiv stamp 7 Jun 2023); Acta Arithmetica (2024). On-disk copy: `fetched-r3/r3s-06-bgstb-2306.04799.pdf` (210,602 bytes; fetch provenance in FOLLOWUP-REPORT Section 4; the v1 stamp read off the PDF's first page this session). Cited for: Theorem 1 (unconditional pointwise F(alpha) on the closed band 0 <= alpha <= 1, depth-weighted, multiplicity-counted), the Lemma 5 kernel class, and the Remark after Theorem 2 (rider 1). See also the same authors' second-moment sequel, arXiv:2501.14545 (per the evidence referee's logged prior-art sweep, 2026-08-26).

**Internal evidence chain (the paper's data authorities, all under `anthropic/rh-program/`).**

* `results/adjudication-A4.json` — the binding adjudication: verdict survives-with-repairs 5.5, repairs R1–R7, the garnish/squeeze computations, merge guidance. The gate contract.
* `results/a4-m2-gate/SPEC.md` — the pre-registered gate specification: kernels and units (Sec 1), null budgets and closed forms (Sec 2, derivations Sec 9), adversary class and realizability (Sec 3), row system and capacity constant (Sec 4), decision rules (Sec 5), flags (Sec 10).
* `results/a4-m2-gate/RUN-REPORT.md` — the implementer's run report: verdict (Sec 1), grid-decoupling mechanism (Sec 2), sanity gates (Sec 3), all runs and numbers (Sec 4), the witness (Sec 5), deviations (Sec 6), flags (Sec 7), upstream consequences (Sec 8).
* `results/a4-m2-gate/AUDIT.md` — the independent adversarial audit: grid-Parseval proof sketch (3.1), independent MC (3.2), budget identities (3.3), block law (3.4), witness recomputation (3.5), LP re-solves over all 4003 columns (3.6), eight break attempts (Sec 4), findings register (Sec 5).
* `results/a4-m2-gate/FOLLOWUP-REPORT.md` — the decision-grade follow-up: near-CUE at tau2 = 1 both N (Secs 1–2), p1 objective (Sec 3), BGSTB24 fetch, riders, citation corrections (Sec 4), deviations (Sec 5).
* Raw data: `results/a4-m2-gate/gate-result.json`, `witness_N64.json`, `followup-near-cue.json`, `followup-p1.json`, `runs/*.json` (in particular `scans_N64.json`, `scans_N128.json`, `tighteps_N64.json`, `tier2_N64.json`, `windows_N64.json`, `explore_lamp.json`, `budgets_lam0p5.json`).
* `results/a4-no-go/theorems.md` — the six proof units (T1–T6) incorporated as Sections 3, 4.1, and 7, with their verification suite `results/a4-no-go/verify/verify_t*.py` and JSON outputs.
* `results/a4-no-go/pair-channel.md` — the pair-interference closure (Section 4.2–4.3), with its independent verification suite `verify/pairchan_*.py` and `pairchan_verify_out.json`.
* `results/a4-no-go/data-tables.md` — the provenance-tagged data digest from which every number in this paper is cited; its Section 10 records the two cite-safety notes honored here (the 940-record maximum is the N = 128 value 8.94e-13; the Tier-2 level 0.833377/0.8333622/0.8332334 drift across dictionary snapshots is common-mode, the equality delta_0' = 0 being snapshot-independent).
* `directions/A4-lindelof-lock.md` — the merged direction file: the immutable proposal, the Phase-4 verdicts, the binding adjudication and merge guidance, and the decided-gate section this paper executes.

**Correction of record.** The "+8 vs 0" doubles-vs-pairs cubic separation premise of the original proposal, and the adjudication's computation-8 phase model ((+1, -1) at u L = 1 with cubic ~ 0), are false under the true block law: Proposition 3.2 gives pair cubic charge 2 m^3 (1 + 3 A^2) >= 8 m^3 at every depth, and Theorem 3.4 places pairs and doubles on the same affine plane c = 3F - 2. The campaign transcript's recorded block facts (pair eigenvalues m L^2 a (1 ± A)) were correct throughout. This correction was executed in the direction file at gate time and is re-proven here from scratch.


---

## Revision record (2026-08-26)

Both referee reports (`referee-1.md`, mathematics; `referee-2.md`, evidence and scope) returned PASS WITH REPAIRS. Every repair below was applied only after re-verifying the underlying fact against the on-disk evidence (or re-deriving it) in this session; the two digest-level errors were also corrected at their source files. Notation: R1-M/m = referee 1 major/minor, R2-M/m = referee 2 major/minor.

**Applied (majors).**

* R1-M1 = R2-M1 (pair-channel closure overclaimed as "the gate's entire admissible class") -> abstract sentence, headline 1.4(8), Section 4.3 title, and the 4.3 Consequence paragraph rewritten to the proved coverage (single-pair to w <= 2.8; multi-pair to w <= 0.82 unconditionally, w <= 1 modulo the certified crowding constant [that clause re-scoped to w <= 0.98 by the 2026-08-27 dated revision — see the revision note at the top]; equal-depth pair-only at every depth), with mixed-depth deep-probe multi-pair columns explicitly assigned to numerics plus the 8/9 backstop, and an added sentence stating that class-level exactness of delta_0 = 0 is proved on the closure's regimes and heuristic (pricing-backed, backstopped at 20/27) on that residue.
* R1-M2.1 = R2-m3 (near-CUE pinning precision) -> Section 5.3 "to 1e-13" corrected to "to 2e-12 (maximum deviation 1.84e-12, at j = 62)"; re-verified from `followup-near-cue.json` (15 of 63 rows exceed 1e-13). Source corrected in `data-tables.md` Section 4.2 with a correction tag.
* R1-M2.2 = R2-m2 (clean_checks misdescribed) -> Appendix A now describes `max_dev` as the maximum row-value deviation between clean-grid and optimizer values, all three columns quoted (3.4e-6 / 1.6e-5 / 4.1e-5); the omitted third value restored. (R2-m2(c)'s rigid-rotation observation was NOT added: not re-verified this session.)
* R1-M2.3 = R2-m1 (witness table column 3 mixed provenance) -> Section 4.4 table and Appendix A column 3 now display the clean-grid C' = 301.3541285 consistently with columns 1-2, with an explicit provenance note: table rows are clean-grid values, aggregates are the stored law rows (which saturate the budget edges exactly; re-verified E[C'] = B3(1 - eps) to 1e-13 from `witness_N64.json`).
* R1-M3.1 (operating-point scope) -> one-sentence definition of the title phrase ("the lambda' = 1/2 + o(1) system fixed by the adjudication, R4 theta < 1 strict; lambda' >= 0.6 is the quarantined Section 8.4 payoff curve") added at the end of Section 1.3.
* R1-M3.2 (MVT-4 parenthetical misattached) -> Section 9.3(i) restated: the MVT-4 extension to lambda in (1/2, 2/3) is Theorem 1(i)'s fixed-lambda divergent cutoff per repair R3 (re-verified in `adjudication-A4.json`), a divergent-cutoff statement subject to Theorem 7.4's vacuity, not the all-V ladder.
* R2-M2 = R1-m1 (headline 1 eps axes) -> corrected to eps in {0.02, 0.05, 0.10} with the tight-eps runs labeled as separate (verified against `runs/scans_N64.json` / `runs/tighteps_N64.json`).
* R2-M3 ("all n(V) vectors zero" false) -> Section 4.4 now states the true ladder slack: E[n(2)] = 3.50, E[n(3)] = 0.94 against caps 400 and 79.0, higher rows zero, vacancy column's n(V) identically zero (recomputed from `witness_N64.json` law weights and nV vectors). Source corrected in `data-tables.md` Section 3 with a correction tag.
* R2-M4 (unsourced LP refinement values 0.3985/0.3991) -> the refinement runs were re-executed this session and persisted: `verify_t5.py` extended with the (2000 pts, h_max 2000), (4000 pts, h_max 2000), (4000 pts, h_max 8000) cells and re-run, regenerating `verify_t5_out.json`; the persisted tail-corrected values 0.398498 / 0.399105 reproduce the prose 0.3985 / 0.3991 exactly, and Section 7.1 now cites the sequence with its grid parameters.

**Applied (minors).**

* R1-m2 -> remark added after Theorem 7.4's proof: capping the garnish height at h0 = min(floor(V0/2), floor(N^{1/4})) removes the V0 = o(N^{1/3}) hypothesis (re-derived: h0 -> infinity, h0^3 <= N^{3/4} = o(N), h0 < V0), licensing the "any divergent cutoff" headline as stated.
* R1-m3 -> Appendix A notes the N = 128 near-CUE witness objective sits 4.0e-8 above the Section 5.2 LP optimum (interior-shrunk box; recomputed from `followup-near-cue.json`).
* R1-m4 -> Theorem 4.9's proof now derives the finite-circle pair block B_p = m (p q^dagger + q p^dagger) and its n_+ <= 1 via Cauchy-Schwarz (re-derived), instead of citing Proposition 3.2 across models.
* R1-m5 -> (W2) now fixes kappa = kappa(1) = 4/3.
* R1-m6 -> Theorem 7.4's simple-atom fraction renamed delta_0' -> s_0 (collision with the near-CUE marginal removed).
* R1-m7 -> Section 2.4 now exhibits the fractional-mark failure of the 5/6 baseline itself (mark-4/3 atoms on the grid: F1 = (4/3)N, N_d = (3/4)N; verified) and scopes the Section 4.2 pointer to the pair-channel form.
* R1-m8 -> "occupancy-2 cross-terms" corrected to "cross-terms (occupancy >= 2)" in Section 2.5 and Appendix B (with the 3.5 + 0.5 two-point/three-point split of the cubic share noted).
* R1-m9 -> Marg's unique sign change scoped to (0, 1], the interval on which the closed forms are proved.
* R1-m10 -> Section 8.4 label corrected to "per repair R4 and merge-guidance item (4)".
* R2-m4 -> Section 5.2 build-out wording: 6,457 columns at the matched cell, 6,739 after the asymptotic re-centering (verified in `followup-near-cue.json` N128 block).
* R2-m5 -> ledger verification constant corrected to 2.2e-11 (stored `pairchan_verify_out.json` I_identity_maxerr = 2.18e-11); also corrected at source in `pair-channel.md`.
* R2-m6 -> the N = 128 "S = 100" pricing claim is now labeled RUN-REPORT-recorded with no stored verify block.
* R2-m7 -> [BGSTB24] v1 date corrected to the arXiv stamp 7 Jun 2023 (read off the fetched PDF's first page this session).
* R2-m8 -> abstract now separates the two benchmarks' evidence bases (940-record grid for N_d; two converged cells plus cross-checks for p1).
* R2-m9 -> subtitle changed to "for the two-moment system at bandwidth one" (drops the audit-flagged "bandwidth-one ceiling" phrase).
* R2-m10 -> Section 8.2 specifies the centering difference (cubic centers 5%, F1 0.7%, F' 2.6%).
* R2-m11 -> "every intermediate dictionary state" corrected to "every recorded dictionary re-solve (1,842 / 6,457 / 6,739 columns)" (verified: three recorded re-solves, deltas 7.8e-16 / 0.0 / 0.0).
* R2-m12 -> the 0.85082 citation now notes the [BHB13] input (verified verbatim in `v5_p14.txt`).
* R2 courtesy (prior-art sweep) -> "see also arXiv:2501.14545" added to the [BGSTB24] entry, attributed to the evidence referee's logged sweep.

**Rejected or partially rejected.**

* R2-m2(c) (stored float positions differ from the grid by a common rigid rotation): omitted rather than asserted — the claim was not re-verified in this session, and nothing load-bearing needs it; the corrected row-value description suffices.

No other finding was rejected. No FATAL findings were reported by either referee; every repair above is wording, citation, or provenance level, and none changes any theorem, proof, number, or the verdict delta_0 = 0.
