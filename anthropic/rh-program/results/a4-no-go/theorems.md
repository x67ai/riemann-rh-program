# A4 sharpened no-go — the theorem units, with complete proofs

**Program:** RH program, direction A4 (merged A2+A4 cubic-certificate direction; adjudicated survives-with-repairs 5.5, binding). **Deliverable context:** the mathematical core of the sharpened no-go paper mandated by the merge guidance item (3) and decided by the M2 gate (ABSORPTION, Session 6, audited): *the two-moment (lemmaR_tight) class is robust under Rudnick–Sarnak-range cubic augmentation with capacity control.* These six units are also the blueprint for the queued Lean formalization (PairCeiling-style; grid data algebraic).
**Evidence base:** `results/a4-m2-gate/{SPEC.md, RUN-REPORT.md, AUDIT.md, FOLLOWUP-REPORT.md, gate-result.json, witness_N64.json}`, `results/adjudication-A4.json`, `directions/A4-lindelof-lock.md`, `results/full-map.md`, `sources-extracted/{v5_p13.txt, v5_p14.txt, tx_081.txt, tx_082.txt}`, `fetched-r3/r3s-06-bgstb-2306.04799.pdf` (present on disk, 210,602 bytes, PDF 1.4 — matching the FOLLOWUP fetch record).
**Discipline (standing order 5):** every proof below is written out in full in this document; every load-bearing number was re-computed in this session by the scripts in `results/a4-no-go/verify/` (`verify_t1.py` … `verify_t6.py`, `verify_t4_mc.py`, with JSON outputs alongside). The few statements that are *quoted rather than re-derived* are confined to Section 8 (Provenance and flags) and are marked at their point of use.
**Scope (read first):** every theorem here is a statement about the *model* — the gate's explicit configuration classes, kernels, and row systems (Section 0) — not about the zeros of zeta. The bridge from the model rows to unconditional statements about zeta is the parent paper's sampling bookkeeping plus the BGSTB24 licensing riders, and it is cited, not re-proven, here (Section 8).
**Date:** 2026-08-26.

---

## 0. Setting: normalized units, the two models, the two benchmarks

### 0.1 Window and kernel

Fix a window profile v >= 0 on [-1/2, 1/2], v even, Int v > 0. The **normalized sampling kernel** at bandwidth lambda > 0 is the entire function

    psi_lambda(x) = ( Int_{-1/2}^{1/2} v(sigma) e^{2 pi i lambda sigma x} d sigma ) / Int v ,

so psi_lambda(0) = 1 and psi_lambda has Fourier transform u(alpha) = v-hat samples supported in |alpha| <= lambda/2 (Montgomery alpha-units), normalized to Int u = 1. For the **flat window** v = 1:

    psi_lambda(x) = sinc(pi lambda x) = sin(pi lambda x) / (pi lambda x),      u = (1/lambda) 1_[-lambda/2, lambda/2].

Positions x are in mean-gap units (mean zero spacing 1). Complex positions are allowed (off-line zeros); psi_lambda extends to an entire function.

### 0.2 Continuum model: configurations and the master trace formula

A **marked configuration** is a finite multiset of points z with positions gamma_z (complex allowed) and multiplicities (marks) m_z >= 1. Structural constraints, when imposed (Section 0.4): integer marks; off-line points only in conjugate pairs {gamma + i d, gamma - i d} with common depth d and common mark. The **master trace formula** defines the k-th trace of the configuration at bandwidth lambda:

    tr G^k := Sum_{z_1, ..., z_k} ( Prod_j m_{z_j} ) psi_lambda(gamma_{z_1} - gamma_{z_2}) psi_lambda(gamma_{z_2} - gamma_{z_3}) ... psi_lambda(gamma_{z_k} - gamma_{z_1}),

the sum over ordered k-tuples of configuration points (SPEC 1.1; this is the paper's Poisson sampling identity in normalized units, and it is realized by an actual matrix — Section 3 constructs the matrix for the blocks that need spectral, not just trace, data). We write F = tr G^2 (Frobenius row) and C = tr G^3 (signed cubic row); at bandwidth 1 we write F1, at bandwidth lambda' we write F', C'.

### 0.3 Finite-circle model (the LP's discretization; SPEC 1.4)

Period N (zeros per period) on the circle of circumference N; configurations are N-periodic marked multisets, described by one period. For the flat window at bandwidth lambda the harmonic set is B = {j in Z : |j| <= lambda N / 2}, with M = |B| harmonics and uniform weights u_j = 1/M. With the form factor

    c_s = Sum_z m_z e^{-2 pi i s theta_z / N}        (for a conjugate pair at theta +/- i d: 2 m cosh(2 pi s d / N) e^{-2 pi i s theta / N}),

the trace rows are

    tr G-hat   = Sum_z m_z                      (mass),
    tr G-hat^2 = Sum_{j1, j2 in B} u_{j1} u_{j2} |c_{j1+j2}|^2 = Sum_s W2(s) |c_s|^2,     W2(s) = Sum_{j in B, s - j in B} u_j u_{s-j},
    tr G-hat^3 = Sum_{k1, k2} U3(k1, k2) c_{k1} c_{k2} c_{-k1-k2},                        U3(k1, k2) = Sum_j u_{j+k1} u_{j+k1+k2} u_j.

Eigenvalue data (ladder counts, inertia) come from the Hermitian frequency matrix H[j, j'] = sqrt(u_j u_{j'}) c_{j-j'} (j, j' in B), whose k-th trace equals the k-th trace row exactly (alias-free tight-frame compression; RUN-REPORT deviation 1). At the primary geometry N = 64, lambda = 1: M = 65 harmonics; lambda' = 1/2: M' = 33.

**Position-space form of the Frobenius row.** For a symmetric band (u_{-j} = u_j) put D(x) = Sum_{j in B} u_j e^{-2 pi i j x / N} = u_0 + 2 Sum_{j > 0} u_j cos(2 pi j x / N), a real even function with D(0) = 1. Expanding |c_s|^2 in the second trace row and re-summing,

    tr G-hat^2 = Sum_{z, z'} m_z m_{z'} D(theta_z - theta_{z'})^2        (on-line configurations),

since Sum_s W2(s) e^{-2 pi i s x / N} = ( Sum_j u_j e^{-2 pi i j x / N} )^2 = D(x)^2. The continuum analog is tr G^2 = Sum_{z,z'} m_z m_{z'} psi_lambda(gamma_z - gamma_{z'})^2 (Section 0.2 at k = 2, psi even).

### 0.4 Adversary class and the two benchmarks

A **column** is an explicit N-periodic marked configuration: on-line atoms (positions theta_i in [0, N), integer marks m_i >= 1) and off-line pairs (position theta, depth parameter, pair multiplicity m). Mass constraint per period: Sum_atoms m_i + 2 Sum_pairs m_p = N. A **law** is a probability mixture w_c >= 0, Sum w_c = 1 over columns; every row is E_w[row(c)]. The two objectives (benchmarks):

    N_d(c) = #atoms + 2 #pairs           (distinct-zeros count; only on-line multiples reduce it),
    p1(c)  = ( #mark-1 atoms + 2 #mult-1 pairs ) / N     (simple fraction; atom-only: #mark-1 atoms / N).

The **two-moment (lemmaR_tight) baseline data** are: mass = N, integrality, pair structure, and the bandwidth-one Frobenius budget F1 in (4/3) N (1 -/+ eps). The **cubic block** at lambda' = 1/2 adds: F' near kappa(1/2) N = (13/6) N, the signed cubic C' near c3(1/2) N = 5 N, the all-V count ladder n(V) <= C_led N V^{-4}, and the garnish-capacity fuzz row. The gate's decided verdict (not re-litigated here; it is the *context* of these units) is that the cubic block's marginal value over the baseline is delta_0 = 0 identically, for both benchmarks.

---

## 1. T1 — Grid Parseval decoupling

The absorption mechanism rests on one exact identity: on a specific uniform grid the entire bandwidth-one Frobenius row degenerates to the multiplicity count, for *every* site subset and *every* mark assignment — while the half-band kernel on the same grid remains position-sensitive. This section proves both halves.

### Lemma 1.1 (flat-band lemma)

Let M >= 1 and let the harmonic band be ANY set of M consecutive integers B = {j0, j0 + 1, ..., j0 + M - 1}, with uniform weights u_j = 1/M. Let the configuration be supported on the M-site uniform grid, sites theta_k = k N / M (k = 0, 1, ..., M - 1) on the circle of circumference N, with arbitrary real marks m_k >= 0 (any subset of sites: absent sites have m_k = 0). Then

    tr G-hat^2 = Sum_{k} m_k^2      EXACTLY.

**Proof.** On the grid the form factor is a discrete Fourier transform on Z_M: for s in Z,

    c_s = Sum_k m_k e^{-2 pi i s (k N / M) / N} = Sum_k m_k e^{-2 pi i s k / M},

which depends only on s mod M; in particular c is M-periodic in s, and by DFT Parseval on Z_M,

    Sum_{r = 0}^{M - 1} |c_r|^2 = M Sum_k m_k^2.       (P)

The Frobenius row is tr G-hat^2 = Sum_s W2(s) |c_s|^2 with W2(s) = #{(j1, j2) in B x B : j1 + j2 = s} / M^2. The sum-set B + B = {2 j0, ..., 2 j0 + 2M - 2} and the pair counts are the triangular weights

    #{(j1, j2) : j1 + j2 = s} = M - | s - (2 j0 + M - 1) |     for |s - (2 j0 + M - 1)| <= M - 1,  else 0.

Fix a residue class r mod M. The window B + B has length 2M - 1, so it contains either one or two members of the class r; writing t = s - (2 j0 + M - 1), the members correspond to two values t and t' with t' = t - M or t + M (when both lie in [-(M-1), M-1]) or to the single value t = 0. The triangular counts on a residue class therefore sum to

    (M - |t|) + (M - |t -/+ M|) = (M - |t|) + |t| = M      (0 < |t| < M),      or      M     (t = 0),

i.e. EXACTLY M on every residue class mod M. Hence, using the M-periodicity of |c_s|^2,

    tr G-hat^2 = (1/M^2) Sum_{r mod M} ( Sum_{s ≡ r, s in B + B} #pairs(s) ) |c_r|^2 = (1/M^2) Sum_{r mod M} M |c_r|^2 = (1/M) Sum_r |c_r|^2 = Sum_k m_k^2

by (P). QED.

### Theorem 1.2 (grid Parseval decoupling at bandwidth one; general even N)

Let N be even, and consider the finite-circle model (Section 0.3) with the flat window at bandwidth lambda = 1: harmonic band B = {j : |j| <= N/2}, M = N + 1 harmonics, u_j = 1/(N + 1). Let the configuration be supported on the (N+1)-site uniform grid of spacing N/(N+1) (sites theta_k = k N/(N+1), k = 0, ..., N), with arbitrary marks. Then

    F1 = tr G-hat_1^2 = Sum_z m_z^2      EXACTLY,

for every site subset and every mark assignment. In particular the bandwidth-one reading on this grid sees only multiplicities, never positions: the lemmaR_tight extremal analysis transfers verbatim to grid configurations (Section 2).

**Proof.** This is Lemma 1.1 with M = N + 1 and B = {-N/2, ..., N/2} (a set of N + 1 consecutive integers because N is even), grid spacing N/M = N/(N+1). QED.

*Remark (why this grid).* Equivalently: all pairwise site differences are integer multiples of N/(N+1), and the position-space kernel D(x) of Section 0.3 satisfies D(k N/(N+1)) = 0 for k not ≡ 0 mod (N+1) — the grid is the zero set of the discrete bandwidth-one kernel (the "psi_1-zero grid" of the RUN-REPORT). The Fourier proof above is the one that makes the exactness structural (weights constant on residue classes) rather than a numerical coincidence, and it is the form queued for Lean.

### Proposition 1.3 (the lambda' = 1/2 kernel is alive on the same grid)

Same geometry, N even, N/2 even (e.g. N = 64, 128), lambda' = 1/2: band B' = {j : |j| <= N/4}, M' = N/2 + 1 harmonics. For grid-supported configurations,

    F' = tr G-hat_{1/2}^2 = Sum_{|s| <= N/2} ( (M' - |s|) / M'^2 ) |c_s|^2 ,

where the s-range {-N/2, ..., N/2} is a COMPLETE residue system mod (N+1) and c_s is the Z_{N+1} DFT of the mark vector. The weights (M' - |s|)/M'^2 are strictly positive on the whole range and non-constant across residues (triangular — at N = 64: 1/33 at s = 0 down to 1/33^2 at |s| = 32), so F' is a strictly position-sensitive functional of the grid configuration, subject only to the Parseval constraint Sum_r |c_r|^2 = (N+1) Sum m^2.

**Proof.** The trace row gives F' = Sum_s W2'(s)|c_s|^2 with W2'(s) = (M' - |s|)_+ / M'^2 supported in |s| <= N/2 (sum-set of B' + B'). The range {-N/2, ..., N/2} has N + 1 elements, hence meets each residue class mod N + 1 exactly once; no residue-class telescoping occurs (the weights are not constant on classes because the band length M' = N/2 + 1 differs from the grid size N + 1), so F' reads the full grid power spectrum {|c_r|^2} with a non-uniform weight. Distinct site subsets of equal mark statistics generically have different {|c_r|^2}, hence different F'. QED.

**Worked exact value (hand-checkable; the witness's first column).** N = 64, the "vacancy lattice": 64 simple marks on 64 of the 65 sites (one vacancy). Then c_0 = 64 and |c_s|^2 = 1 for s != 0 mod 65 (the full lattice has c_s = 65 delta_{s ≡ 0}; removing one site subtracts a unit phase). Hence

    F1 = 64      (Theorem 1.2: = Sum m^2),
    F' = (33/33^2) 64^2 + Sum_{0 < |s| <= 32} ((33 - |s|)/33^2) * 1 = 4096/33 + (33^2 - 33)/33^2 = 4096/33 + 32/33 = 4128/33 = 125.0909...,

using Sum_{|s| <= 32}(33 - |s|) = 33 + 2(32 + 31 + ... + 1) = 33^2 and subtracting the s = 0 term. This reproduces the shipped witness column (`witness_N64.json`: F1 = 64, F' = 125.09090...; AUDIT 3.5's exact-rational spot check 4128/33). The two-bandwidth decoupling is thereby explicit: F1 is blind to the vacancy's position, F' is not.

### Proposition 1.4 (continuum analog: the adversary lattice)

In the continuum model (Section 0.2) with the flat window: let the configuration be supported on the integer lattice Z (mean-gap units), arbitrary real marks m_z. Then at bandwidth 1

    tr G_1^2 = Sum_z m_z^2      EXACTLY,

while the half-band kernel is alive on the lattice: psi_{1/2}(k) = sinc(pi k / 2) = (2 / (pi k)) (-1)^{(k-1)/2} for odd k (and 0 for even k != 0). For the finite-T Weil–Gabor matrix itself the identity holds as tr G-hat^2 = (Sum m^2)(1 + o(1)), the o(1) being the parent paper's finite-window corrections; this is the campaign record's "adversary lattice" (tx_081 lines 6–8: the near-extremal unconditional world with n_dist/N = 0.657 at T = 1000).

**Proof.** At k = 2 the master formula gives tr G_1^2 = Sum_{z,z'} m_z m_{z'} psi_1(z - z')^2 (psi even, positions real). psi_1(x) = sinc(pi x) vanishes at every nonzero integer and equals 1 at 0; on the lattice every off-diagonal difference is a nonzero integer, so only the diagonal survives: tr G_1^2 = Sum m_z^2. The half-band values are sinc(pi k/2) = sin(pi k/2)/(pi k/2), and sin(pi k/2) = (-1)^{(k-1)/2} for odd k, 0 for even k. The finite-T statement is the same computation performed under the paper's sampling identity with its recorded o(1) error budget (quoted; Section 8, item Q3). QED (model part).

*Remark.* Theorem 1.2 is the exact periodization of Proposition 1.4: spacing N/(N+1) instead of 1 makes the finite-geometry identity exact rather than asymptotic — which is precisely why the finite-N gate could exhibit delta_0 = 0 as an exact LP equality rather than a numerical near-zero.

### Numerical confirmation (T1) — `verify/verify_t1.py`, run this session

* Exactness on the grid: 40 random site-subsets with random marks 1..8, at N = 64 AND N = 128, evaluated through the Fourier double-sum route and independently through the eigenvalues of the frequency matrix H: max |F1 - Sum m^2| = 9.1e-13 (N = 64) and 4.1e-12 (N = 128); eig route agrees (max 9.1e-13). Matches AUDIT 3.1's independent 4.5e-13.
* General flat-band lemma (Lemma 1.1): 20 random (N, M, band offset j0) draws including asymmetric bands: max deviation 3.2e-12.
* Controls: off-grid uniform-position configurations give |F1 - Sum m^2| in [1.3e-2, 62.5] (identity genuinely fails off the grid); on-grid at lambda' = 1/2 gives |F' - Sum m^2| in [40.9, 120.8] (the half-band kernel is alive, Proposition 1.3).
* Continuum lattice: 20 random integer-lattice configurations, deviation 0.0 to machine precision; half-band lattice values match 2/(pi k)(-1)^{(k-1)/2} exactly.
* Worked value: 4096/33 + 32/33 = 4128/33 = 125.090909..., equal to the shipped witness column F' (dev < 3e-6, the optimizer's position rounding; the clean grid description is canonical).

---

## 2. T2 — The atom-only corner theorem, both benchmarks

This is the baseline the gate's absorption pins: over atom-only configurations the two-moment data force exactly the lemmaR_tight corner, for the distinct-zeros benchmark AND the simple-fraction benchmark, and the grid of Theorem 1.2 attains both corners. The audit's scoping (AUDIT finding 4) is respected: the theorem is stated for the atom-only class, where the sandwich is airtight; the pair-interference caveat is Remark 2.6.

**Setting.** Fix N and eps >= 0. Let A be the class of atom-only configurations (Section 0.4): atoms at arbitrary positions (finite-circle model, Section 0.3, flat windows; or continuum model — the proofs below work verbatim in both), integer marks m_i >= 1, mass Sum_i m_i = N per period. For a law w over A the constraint set is

    E_w[ F1 ] <= (4/3) N (1 + eps)        (bandwidth-one Frobenius, upper edge),

and the objectives are E_w[N_d]/N (N_d = #atoms) and E_w[p1] (p1 = #mark-1 atoms / N).

### Lemma 2.1 (diagonal positivity: F1 >= Sum m^2 on atom-only configurations)

For every atom-only configuration c (any positions, any real marks m_i >= 0), in either model,

    F1(c) >= Sum_i m_i^2 ,

with equality iff every off-diagonal kernel value vanishes (in particular, equality holds on the grid of Theorem 1.2 and on the lattice of Proposition 1.4).

**Proof.** By Section 0.3 (position-space form), F1 = Sum_{i, i'} m_i m_{i'} K(theta_i - theta_{i'}), where K = D^2 (finite circle, symmetric band, D real even, D(0) = 1) or K = psi_1^2 (continuum). In both cases K >= 0 pointwise and K(0) = 1. Hence F1 = Sum_i m_i^2 + Sum_{i != i'} m_i m_{i'} K(theta_i - theta_{i'}) >= Sum_i m_i^2, the off-diagonal sum being a sum of nonnegative terms. QED.

*Remark.* This is the one step that fails for pair-containing configurations: an off-line pair contributes cross-terms 2 Re[psi(x + i y)^2]-type, which need not be nonnegative. See Remark 2.6.

### Lemma 2.2 (integer-mark corner inequalities — the two integrality levels)

For every atom-only configuration with integer marks m_i >= 1 and mass Sum m_i = N:

    (a)   N_d = #atoms >= ( 3 N - Sum_i m_i^2 ) / 2 ,
    (b)   n_1 = #mark-1 atoms >= 2 N - Sum_i m_i^2 ,

with equality in (a) iff all marks lie in {1, 2}, and equality in (b) iff all marks lie in {1, 2}.

**Proof.** Both are per-atom inequalities summed over atoms.
(a) For each integer m >= 1: (m - 1)(m - 2) >= 0, i.e. m^2 - 3m + 2 >= 0, i.e. 1 >= (3 m - m^2)/2, with equality iff m in {1, 2}. Summing over atoms: N_d = Sum_i 1 >= Sum_i (3 m_i - m_i^2)/2 = (3 N - Sum m_i^2)/2.
(b) For each integer m >= 1: 1_{m = 1} >= 2 m - m^2. Indeed at m = 1: 1 = 1; at m = 2: 0 = 0; at m >= 3: 2 m - m^2 = m(2 - m) < 0 <= 0. Equality iff m in {1, 2}. Summing: n_1 >= 2 N - Sum m_i^2. QED.

*Remark.* (a) is the second integrality level (m-1)(m-2) >= 0 — exactly the level lemmaR_tight proves exhausted by the two-moment certificate and the level the cubic row re-measures (Theorem 3.4); (b) is its simple-fraction sibling. In the parent's terms, (a) is the doubles-optimal ("cost ratio 1/m maximized at m = 2") corner arithmetic: an atom of mark m spends m(m-1) of Frobenius excess to save m-1 units of N_d, so doubles are the efficient coin.

### Theorem 2.3 (atom-only corner theorem)

Fix N even, 0 <= eps <= 1/2 (finite-circle model, flat windows). Over laws w on the atom-only class A with mass N and E_w[F1] <= (4/3) N (1 + eps):

    (a)   min_w  E_w[N_d]/N  =  5/6 - (2/3) eps ,
    (b)   min_w  E_w[p1]     =  2 - (4/3)(1 + eps) = 2/3 - (4/3) eps .

Both minima are attained by explicit laws supported on the (N+1)-site grid of Theorem 1.2 with marks {1, 2} only. Moreover every configuration in A satisfies pointwise N_d/N >= 5/6 - (2/3) eps_c and p1 >= 2/3 - (4/3) eps_c, where eps_c is its own Frobenius excess F1 = (4/3)N(1 + eps_c). The same statements hold with the two-sided budget band E_w[F1] in (4/3) N [1 - eps, 1 + eps] (the attaining laws sit at the upper edge, which is inside the band), and the minima over any richer mark alphabet (any W, or unbounded marks) are the same.

**Proof.** *Lower bounds.* Let w be feasible. By Lemma 2.1, E_w[Sum m^2] <= E_w[F1] <= (4/3) N (1 + eps). By Lemma 2.2(a) and linearity of expectation,

    E_w[N_d] >= ( 3 N - E_w[Sum m^2] ) / 2 >= ( 3 N - (4/3) N (1 + eps) ) / 2 = N ( 3 - 4/3 - (4/3) eps ) / 2 = N ( 5/6 - (2/3) eps ).

By Lemma 2.2(b),

    E_w[N p1] = E_w[n_1] >= 2 N - E_w[Sum m^2] >= 2 N - (4/3) N (1 + eps) = N ( 2/3 - (4/3) eps ).

The pointwise statements are the same two chains applied to a single configuration with its own eps_c.

*Attainment.* For an integer 0 <= k <= N/2 let c_k be the grid configuration with k doubles and N - 2k simples on any k + (N - 2k) = N - k distinct grid sites (there are N + 1 >= N - k sites, so c_k exists). By Theorem 1.2, F1(c_k) = Sum m^2 = (N - 2k) + 4k = N + 2k exactly; N_d(c_k) = N - k; n_1(c_k) = N - 2k. Set kbar = (B - N)/2 with B = (4/3) N (1 + eps); then kbar = N (1/6 + (2/3) eps) >= 0, and eps <= 1/2 gives kbar <= N/2. Choose the two-column law w* = (1 - t) delta_{c_{k-}} + t delta_{c_{k+}} with k- = floor(kbar), k+ = min(k- + 1, N/2), t chosen so that E[k] = kbar (t = kbar - k- when k+ = k- + 1; if kbar is an integer, the single column c_kbar suffices). Then

    E_{w*}[F1] = N + 2 kbar = B = (4/3) N (1 + eps)      (upper edge, exactly),
    E_{w*}[N_d]/N = 1 - kbar/N = 1 - (B - N)/(2N) = (3N - B)/(2N) = 5/6 - (2/3) eps,
    E_{w*}[p1] = 1 - 2 kbar/N = 2 - B/N = 2/3 - (4/3) eps.

Both chains of the lower bound hold with equality (marks in {1, 2}; grid kills all cross-terms; budget saturated), so w* is optimal for both objectives simultaneously. The two-sided band adds only E_w[F1] >= (4/3)N(1 - eps), which w* satisfies (it sits at the upper edge). Enlarging the mark alphabet cannot lower the minimum (the lower-bound chain never used a mark cap) and cannot raise it (w* uses marks {1,2}, inside every alphabet): the W-independence is inclusion, not extrapolation. QED.

### Corollary 2.4 (asymptotic corners)

As eps -> 0 the two optima tend to 5/6 and 2/3 respectively — the model's bandwidth-one analogs of the Montgomery extremal 5/6 (distinct zeros) and 2/3 (simple fraction). At the gate's matched-geometry budgets (B1 replacing (4/3)N) the same proof gives min E[N_d]/N = (3N - B1(1 + eps))/(2N) and min E[p1] = 2 - (B1/N)(1 + eps); with the shipped matched values this is 0.8050957 and 0.6101914 at N = 64, eps = 0.05 — the run's and follow-up's reported optima to LP precision.

**Proof.** Substitute in Theorem 2.3; the matched-budget variant replaces (4/3)N by B1 throughout (nothing in the proofs used the numerical value of B). QED.

### Remark 2.5 (what the gate adds to this theorem)

Theorem 2.3 is the BASELINE. The gate's decided content — not re-proven here, but now structurally explained by T1 + T3 — is that adding the entire lambda' = 1/2 cubic block (F', signed C', all-V ladder, capacity fuzz) to the constraint set does not move either optimum: delta_0 = 0 identically over the 940-record grid (RUN-REPORT Sec 1; AUDIT Sec 3.6: fresh LP re-solves, delta_0 < 4e-13; FOLLOWUP Sec 3: p1 objective, delta_p1 <= 1.4e-12, converged at the literal stop rule). The witness laws achieving the corners with the full block feasible are grid laws with marks {1, 2}: the T1 decoupling supplies F1 = Sum m^2 (Lemma 2.1's equality case) while the sub-grid arrangement freely meets the lambda' rows (Proposition 1.3).

### Remark 2.6 (scope: the pair-interference channel)

For pair-containing configurations Lemma 2.1 is not available: bandwidth-one cross-terms involving complex positions are of the form m m' 2 Re[psi_1(x + i y)^2] and can be negative, so "F1 below Sum m^2, freeing budget for more doubles" is not excluded by this argument (AUDIT finding 4). Within the gate this channel was priced by converged column generation and produced nothing; but the *theorem-grade* statement is the atom-only one above. Any future strengthening should either close this channel analytically or keep the atom-only scoping in the paper's model-level theorem. Note the channel could only produce a BITE (a pair-assisted configuration violating the corner would be cut by pair-pricing, not absorption), so it does not threaten the no-go's verdict — only the sharpness constant of the model theorem for the wider class.

### Numerical confirmation (T2) — `verify/verify_t2.py`, run this session

* Per-atom inequalities: exhaustive over m = 1..50, both hold, equality exactly at m in {1, 2}; 20,000 random integer-mark draws: zero violations of either aggregated bound.
* LP over grid k-doubles columns at N = 64: min N_d and min p1 match the closed forms at eps in {0.10, 0.05, 0.02, 0.002} to <= 3.3e-16 (e.g. eps = 0.002: 0.8320000000 and 0.6640000000, the RUN-REPORT/FOLLOWUP values); the two-sided band gives the same optimum (dev 0.0).
* Exact Fraction arithmetic: P = 5/6 - (2/3)eps and p1 = 2 - (4/3)(1+eps) verified as rational identities at eps = 1/20, 1/50, 1/500.
* Cross-check against the shipped witness: E[F1] = 88.9478 (recomputed from `witness_N64.json` law weights), and (3N - E[F1])/(2N) = 0.8050957 = the shipped P to 6e-13; per column, F1 = Sum m^2 and N_d = #atoms verified for all three columns.

---

## 3. T3 — The exact pair block and cubic blindness (the affine-plane identity)

This unit re-derives the true Prop-4.1 block spectrum and proves the identity that explains the absorption structurally: on isolated blocks the signed cubic row is an affine function of the trace and Frobenius rows plus the second integrality level — it cannot see doubles-vs-pairs at ANY depth. This supersedes the direction file's Step-4 "+8 vs 0" narrative and the adjudication's computation-8 phase model (both recorded as corrected in the direction file's decided-gate section); tx_082's block facts were right all along.

**Setting.** Windows tau_k = k (2 pi / L), k in Z (critical spacing); taper phi real, even, continuous, supported in [-L/2, L/2], phi in C^2 (the parent's formalized class is C^3 — more than enough). Fourier convention: phihat(z) = Int phi(s) e^{-i s z} ds (entire, by Paley–Wiener); Phi(z) = Int phi(s)^2 e^{-i s z} ds; a = L^{-1} Int phi^2, so Phi(0) = L a. Normalized units: matrices divided by L^2 a (units in which an isolated on-line atom of mark m has eigenvalue m).

### Lemma 3.1 (Poisson sampling identity, complex arguments)

For all complex tau, tau':

    Sum_{k in Z} phihat(tau - tau_k) phihat(tau' - tau_k) = L Phi(tau - tau') ,

the sum converging absolutely and locally uniformly.

**Proof.** *Real arguments.* Fix tau, tau' in R and set g(t) = phihat(tau - t) phihat(tau' - t); phihat is real on R (phi real even) and, since phi in C^2 with compact support, |phihat(x)| <= C/(1 + x^2), so g in L^1 with |g(t)| <= C'/(1 + t^2)^2 and the lattice sum converges absolutely. The Fourier transform ghat(xi) = Int g(t) e^{-i t xi} dt: each factor t -> phihat(tau - t) has spectrum supported in [-L/2, L/2] (its transform is e^{-i tau xi} 2 pi phi(xi), by Fourier inversion), so ghat = (1/2pi) (convolution of the two factor transforms) is supported in [-L, L], is continuous, and vanishes AT the endpoints +/-L: the convolution of two continuous functions supported in [-L/2, L/2] evaluated at L integrates over the single point s = L/2 — a null set — hence 0. Poisson summation over the lattice (2 pi / L) Z (classical form, valid since g in C^0 ∩ L^1 with |g| + |ghat| summable on the respective lattices):

    Sum_k g(2 pi k / L) = (L / 2 pi) Sum_{n in Z} ghat(n L) = (L / 2 pi) ghat(0),

all n != 0 terms vanishing by the support (|nL| >= L, with the endpoint value 0). Finally, by Plancherel with the factor transforms computed above,

    ghat(0) = Int phihat(tau - t) phihat(tau' - t) dt = (1/2 pi) Int (2 pi phi(xi))^2 e^{-i (tau - tau') xi} d xi = 2 pi Phi(tau - tau'),

so Sum_k g(tau_k) = L Phi(tau - tau').
*Complex arguments.* For z = x + i y, |phihat(x + i y)| <= e^{L |y| / 2} C/(1 + x^2) (integrate the defining integral; the C^2 decay survives with the exponential factor bounded by the support). Hence for (tau, tau') in a compact subset of C^2 the lattice sum converges absolutely and uniformly; it is therefore an entire function of (tau, tau'), as is L Phi(tau - tau'). The two entire functions agree on R^2, hence everywhere (identity theorem, one variable at a time). QED.

### Proposition 3.2 (exact off-line pair block — the true Prop-4.1 spectrum)

Let the conjugate pair be {gamma + i delta, gamma - i delta}, gamma in R, depth delta > 0, multiplicity m, with evaluation vector x = (x_k), x_k = phihat(gamma + i delta - tau_k), and block matrix M = m ( x x^T + xbar xbar^T ) (transpose, not conjugate-transpose: the two rank-one terms are the pair's two zeros). Then, exactly:

    (i)    x^T x = L Phi(0) = L^2 a          — real, independent of depth AND position;
    (ii)   |x|^2 = L Phi(2 i delta) = L^2 a A(delta),      A(delta) = Int phi^2(s) cosh(2 delta s) ds / Int phi^2(s) ds >= 1;
    (iii)  writing x = p + i q (real and imaginary parts): <p, q> = 0 exactly, |p|^2 = L^2 a (1 + A)/2, |q|^2 = L^2 a (A - 1)/2;
    (iv)   M = 2 m ( p p^T - q q^T ), a rank-<= 2 real symmetric matrix with nonzero eigenvalues (normalized by L^2 a)

               m (1 + A(delta))     and     m (1 - A(delta)) ,

           independent of the position gamma;
    (v)    normalized charges: trace 2m; Frobenius 2 m^2 (1 + A^2); signed cubic 2 m^3 (1 + 3 A^2).

In dimensionless depth w := L delta: A depends on the pair only through w, with A(0+) = 1 and A strictly increasing; for the flat taper (phi = 1 on [-L/2, L/2]) A(w) = sinh(w)/w, with values A(1/8) = 1.002606, A(1/4) = 1.010449, A(1/2) = 1.042191, A(3/4) = 1.096422, A(1) = 1.175201, A(2) = 1.813430.

**Proof.** (i) Lemma 3.1 at tau = tau' = gamma + i delta: Sum_k phihat(gamma + i delta - tau_k)^2 = L Phi(0) = L Int phi^2 = L^2 a. Real and independent of gamma, delta.
(ii) Since phi is real and even, phihat(zbar) = conj(phihat(z)); hence |x_k|^2 = phihat(u - tau_k) phihat(ubar - tau_k) with u = gamma + i delta, and Lemma 3.1 at (u, ubar) gives |x|^2 = L Phi(u - ubar) = L Phi(2 i delta) = L Int phi^2(s) e^{2 delta s} ds = L Int phi^2(s) cosh(2 delta s) ds (phi^2 even). A >= 1 by cosh >= 1, strictly increasing in delta by strict monotonicity of cosh in |2 delta s| on the support (phi not a.e. 0).
(iii) x^T x = |p|^2 - |q|^2 + 2 i <p, q>; by (i) it is real, so <p, q> = 0, and |p|^2 - |q|^2 = L^2 a. Also |p|^2 + |q|^2 = |x|^2 = L^2 a A. Solve.
(iv) x x^T + xbar xbar^T = (p + iq)(p + iq)^T + (p - iq)(p - iq)^T = 2 (p p^T - q q^T). With p ⊥ q, the matrix 2 m (p p^T - q q^T) has eigenvectors p, q with eigenvalues 2 m |p|^2 = m L^2 a (1 + A) and -2 m |q|^2 = m L^2 a (1 - A); all other eigenvalues 0. Normalize by L^2 a. Position-independence: the eigenvalues depend only on |p|^2, |q|^2, which by (i)-(ii) depend only on delta.
(v) trace: m(1 + A) + m(1 - A) = 2m. Frobenius: m^2 (1 + A)^2 + m^2 (1 - A)^2 = 2 m^2 (1 + A^2). Cubic: m^3 (1 + A)^3 + m^3 (1 - A)^3 = m^3 [2 + 6 A^2] = 2 m^3 (1 + 3 A^2).
Flat-window A: with v = 1, A(w) = Int_{-1/2}^{1/2} cosh(2 w sigma) d sigma = sinh(w)/w; the listed values are sinh(w)/w evaluated (verify_t3.py; they reproduce SPEC 1.2's table to its displayed precision, <= 4e-6). QED.

*Consistency with the master formula.* The two-point configuration {gamma ± i delta} under the master formula (Section 0.2) has tr G^k = m^k tr K^k with the 2x2 kernel K = [[psi(0), psi(2 i delta)], [psi(-2 i delta), psi(0)]] = [[1, A], [A, 1]] (psi(2 i delta) = Phi(2 i delta)/Phi(0) = A for the normalized kernel), whose eigenvalues are 1 ± A — the same charges. The matrix route (iv) is what additionally certifies the INERTIA data (one positive, one negative eigenvalue for delta > 0) consumed by the n_- and ladder rows.

*Block continuity (the shallow-pair mimicry, exact form).* As delta -> 0+: spectrum -> (2m, -0), Frobenius -> 2m^2, cubic -> 8 m^3: a shallow pair is row-indistinguishable from an on-line double in EVERY row, continuously. But note — and this is the correction — the cubic charge 2 m^3 (1 + 3 A^2) >= 8 m^3 at EVERY depth (A >= 1), increasing with depth: a deep pair does not lose cubic charge; the "+8 vs 0" separation premise (adjudication computation 8's phase model, the direction file's Step-4 narrative) is false under the true block law.

### Definition (per-zero charges)

For an isolated block of total mass mu (mu = m for an atom of mark m; mu = 2m for a pair of multiplicity m), the per-zero (per unit mass) Frobenius and cubic charges are F = (block Frobenius)/mu and c = (block cubic)/mu. From Proposition 3.2(v) and the atom spectrum (single eigenvalue m):

    atom, mark m:        F = m,               c = m^2;
    pair, mult m, depth: F = m (1 + A^2),     c = m^2 (1 + 3 A^2).

### Proposition 3.3 (affine-plane identity)

    atom of mark m:              c = 3 F - 2 + (m - 1)(m - 2) ;
    pair of mult 1, ANY depth:   c = 3 F - 2      EXACTLY ;
    pair of mult m, ANY depth:   c = 3 F - 2 + (m - 1)(m - 2) + 3 m (m - 1) A^2 .

In particular every mark-{1,2} atom and every multiplicity-1 pair — at every depth — lies on the same affine plane c = 3 F - 2 in the per-zero (F, c) plane.

**Proof.** Atom: 3F - 2 + (m-1)(m-2) = 3m - 2 + m^2 - 3m + 2 = m^2 = c. Pair: c - 3F + 2 = m^2 (1 + 3A^2) - 3m(1 + A^2) + 2 = (m^2 - 3m + 2) + 3 A^2 (m^2 - m) = (m-1)(m-2) + 3 m (m-1) A^2. At m = 1 both terms vanish identically in A (i.e. at every depth); at m = 2 the atom identity reads c = 3F - 2 as well (doubles are on the plane). QED.

### Theorem 3.4 (cubic blindness on isolated blocks)

Let the configuration be a disjoint union of isolated blocks (atoms of marks m_i; pairs of multiplicities m_p at depths with A_p = A(delta_p)), with total mass Mass = Sum_i m_i + 2 Sum_p m_p, Frobenius F = Sum blocks, signed cubic C = Sum blocks. Then, exactly:

    C - 3 F + 2 Mass = Sum_{zeros} m (m - 1)(m - 2) + 6 Sum_{pairs} m_p^2 (m_p - 1) A_p^2 ,

where Sum_{zeros} runs over the zero multiset (an atom of mark m contributes m(m-1)(m-2) once; a pair of mult m contributes 2 · m(m-1)(m-2), its two zeros). Consequences:

1. On the class {marks-{1,2} atoms} ∪ {multiplicity-1 pairs of arbitrary depth} — the entire doubles-vs-pairs comparison class of lemmaR_tight — the right side vanishes identically:

       C = 3 F - 2 Mass       identically on the class.

   The signed cubic row restricted to isolated blocks of this class is an EXACT affine combination of the Frobenius and mass rows: it separates nothing those two rows do not. An on-line double and an off-line pair of any depth are cubic-indistinguishable.
2. All discriminating power of the cubic row beyond the two-moment data therefore lives in exactly two places: (i) marks >= 3 (and pairs of multiplicity >= 2), through the nonnegative integrality terms on the right; (ii) violations of block isolation — the clustering cross-terms of the master trace formula, which the identity does not constrain and which the gate showed to be adversary-tunable at zero cost (T1 + the witness).
3. The task-level premise "a hyperbolic pair block contributes (+a)^3 + (-a)^3 = 0 to tr G^3 while a double contributes +8" is FALSE under the true block law: the pair's signed cubic is 2 m^3 (1 + 3 A^2) >= 8 m^3 at every depth. The sign-split "different corners of the constraint polytope" picture (Step 4 of the proposal; adjudication computation 8) is hereby superseded, as already recorded in the direction file's decided-gate section.

**Proof.** Sum the per-block identities. An atom of mark m has block charges (mass m, Frobenius m^2, cubic m^3), so its contribution to C - 3F + 2 Mass is m^3 - 3 m^2 + 2m = m(m-1)(m-2). A pair of mult m has block charges (mass 2m, Frobenius 2m^2(1 + A^2), cubic 2m^3(1 + 3A^2)), contributing

    2 m^3 (1 + 3 A^2) - 6 m^2 (1 + A^2) + 4 m = 2 [ m^3 - 3 m^2 + 2 m ] + A^2 [ 6 m^3 - 6 m^2 ] = 2 m (m-1)(m-2) + 6 m^2 (m - 1) A^2 .

Summing gives the displayed identity (the pair's 2 m(m-1)(m-2) is exactly its two zeros' worth of the integrality sum). On marks {1,2} and mult-1 pairs every term vanishes: m(m-1)(m-2) = 0 for m in {1, 2}; m_p^2(m_p - 1) = 0 for m_p = 1. Consequence 1 is then immediate; 2 is the statement that the identity accounts for the entire isolated-block cubic content, leaving only the listed residues; 3 was proven in Proposition 3.2 (A >= 1). QED.

*Remark (why the gate had to be clustered).* By consequence 1, an isolated-block gate over the doubles-vs-pairs class would return a tautological answer along the plane c = 3F - 2 (SPEC 1.2's own observation). The corrected gate's clustered null and positional freedom are therefore not conservatism but necessity — and the decided outcome is that the clustering cross-terms, the only live channel, are a free resource for the adversary (grid decoupling, T1) rather than a signal for the certificate.

### Numerical confirmation (T3) — `verify/verify_t3.py`, run this session

* Evaluation-vector route, cos taper (fast-decaying phihat), L = 40, 120001 windows: |x^T x / L^2 a - 1| <= 6.7e-16, |<p,q>|/L^2 a <= 1.7e-14, A_numeric vs quadrature A(delta) <= 1.1e-15, block eigenvalues vs m(1 ± A) <= 7.8e-14 — at every depth w in {1/64, 1/8, 1/4, 1/2, 3/4, 1, 2} and three unrelated positions each (position-independence at machine precision). Flat taper (slow 1/x decay of phihat): same checks pass at the truncation level 1.3e-5 (window-truncation artifact of the check, not of the law — SPEC flag F7's point, reproduced).
* Flat A-values sinh(w)/w reproduce SPEC 1.2's table to <= 4e-6 (its displayed precision).
* Charges and the per-zero identity: for m in {1, 2, 3, 5} and all depths, trace/Frobenius/cubic match (2m, 2m^2(1+A^2), 2m^3(1+3A^2)) and c - (3F - 2) matches (m-1)(m-2) + 3m(m-1)A^2, all to <= 9.1e-13; at m = 1 the identity c = 3F - 2 is exact at every depth. Atom identity exhaustive m = 1..29: exact.
* Shallow-pair continuity: w = 1/64: eigenvalues (2.000041, -0.000041), cubic charge 8.0005; w = 1/8: 8.0313 — matching AUDIT 3.4's independent values (8.0005, 8.033); never 0 at any depth.
* Master-formula 2x2 kernel route reproduces all three charges (consistency of the trace and matrix routes).

---

## 4. T4 — Sine-process closed forms and the doubles-plane diagnostic

The gate's null budgets are the per-zero moments of the flat-window Gram over the determinantal sine process. This unit computes them in closed form — the derivations of SPEC 9.1 written out in full — and proves the corollaries that organize the whole margin structure: the doubles-plane diagnostic G(lambda), the designer's "2 = 2" identity G(1) = 0, and the moment-margin sign change near lambda = 0.61.

**Setting.** The sine process: the determinantal point process on R with kernel S(x) = sin(pi x)/(pi x) — intensity rho_1 = 1, and correlation functions (standard determinantal facts, taken as the DEFINITION of the null per SPEC 2.1)

    rho_2(x1, x2) = 1 - S(x12)^2,
    rho_3(x1, x2, x3) = 1 - S(x12)^2 - S(x13)^2 - S(x23)^2 + 2 S(x12) S(x13) S(x23),      x_ij = x_i - x_j.

The per-zero Gram moments at bandwidth lambda with kernel psi = psi_lambda (flat window; u = psihat = (1/lambda) 1_[-lambda/2, lambda/2], Int u = 1):

    m2(lambda) := psi(0)^2 + Int_R rho_2(0, x) psi(x)^2 dx ,
    m3(lambda) := psi(0)^3 + 3 Int_R rho_2(0, x) psi(x)^2 dx + T3(lambda),
    T3(lambda) := IntInt_{R^2} rho_3(0, x, x + y) psi(x) psi(y) psi(x + y) dx dy .

(These are the N -> infinity limits of E[tr G^k]/N for the process restricted to long windows: the k-tuple sum of Section 0.2 splits over coincidence patterns — all-equal (N terms, value psi(0)^k = 1), exactly-two-equal (3 ordered patterns at k = 3, each psi(0) psi(x) psi(-x) = psi(x)^2 against rho_2), all-distinct (rho_3 against the cyclic product psi(x12) psi(x23) psi(x31), reparametrized by the separations x = x12, y = x23, x + y = -x31 and evenness of psi). The sine process is simple, so all marks are 1.)

### Lemma 4.1 (Fourier-side reduction)

With t(alpha) = (1 - |alpha|)_+ (= the Fourier transform of S^2) and b = 1_[-1/2, 1/2] (= Shat):

    (i)    Int psi^2 dx = Int u^2 d alpha ;
    (ii)   Int S^2 psi^2 dx = Int t (u * u) d alpha ;
    (iii)  IntInt psi(x) psi(y) psi(x + y) dx dy = Int u^3 d alpha ;
    (iv)   IntInt S(x)^2 psi(x) psi(y) psi(x + y) dx dy = Int (t * u) u^2 d alpha    (and the same value for the S(y)^2 and S(x + y)^2 terms);
    (v)    IntInt S(x) S(y) S(x + y) psi(x) psi(y) psi(x + y) dx dy = Int (b * u)^3 d alpha .

Hence  m2 = 1 + Int u^2 - Int t (u * u)  and  m3 = 1 + 3 [ Int u^2 - Int t (u * u) ] + T3,  with  T3 = Int u^3 - 3 Int (t * u) u^2 + 2 Int (b * u)^3.

**Proof.** Convention: fhat(alpha) = Int f(x) e^{-2 pi i alpha x} dx; then psihat = u, Shat = b, and (S^2)^hat = b * b = t. All functions here are real, even, and in L^2 with compactly supported transforms, so every step is Plancherel or Fourier inversion on nice functions.
(i) Plancherel.
(ii) Plancherel on the product pair: Int (S^2)(psi^2) = Int (S^2)^hat (psi^2)^hat = Int t (u * u).
(iii) Write each factor by inversion, psi(x) = Int u(alpha) e^{2 pi i alpha x} d alpha, and integrate over (x, y):

    IntInt psi(x) psi(y) psi(x + y) dx dy = IntIntInt u(a) u(b') u(c) [Int e^{2 pi i (a + c) x} dx] [Int e^{2 pi i (b' + c) y} dy] da db' dc
                                          = Int u(-c) u(-c) u(c) dc = Int u^3        (u even),

the inner integrals collapsing to delta functions. (Rigorously, in two Plancherel steps, no deltas: with y fixed, g(y) := Int psi(x) psi(x + y) dx is the L^2 pairing of psi(·) and psi(· + y), = Int u(alpha)^2 e^{-2 pi i alpha y} d alpha — the Fourier transform of u^2 at y; then Int psi(y) g(y) dy = Int psihat u^2 = Int u^3 by the multiplication identity Int f ghat = Int fhat g. Fubini is licensed by absolute convergence: |psi(x) psi(y) psi(x + y)| <= C / ((1 + |x|)(1 + |y|)(1 + |x + y|)), integrable over R^2.)
(iv) Same two-step Plancherel with the first factor S(x)^2 psi(x): Int_y psi(y) psi(x + y) dy = g(x) with ghat = u^2; then Int S^2 psi g dx = Int (S^2 psi)^hat ghat-bar = Int (t * u) u^2. The S(y)^2 and S(x + y)^2 variants reduce to the same value by the symmetry of the integrand under the substitutions (x, y) -> (y, x) and (x, y) -> (x, -x - y) (Jacobian 1, psi and the measure invariant).
(v) Set h = S psi, hhat = b * u; the integral is IntInt h(x) h(y) h(x + y) dx dy = Int (b * u)^3 by (iii) applied to h.
The moment formulas follow by substituting into the definitions, with psi(0) = 1. QED.

### Theorem 4.2 (flat-window closed forms)

For the flat window and every 0 < lambda <= 1:

    m2(lambda) = 1/lambda + lambda/3 ,          m3(lambda) = 1 + 1/lambda^2 .

**Proof.** Evaluate the five integrals of Lemma 4.1 for u = (1/lambda) 1_[-lambda/2, lambda/2]. Throughout, lambda <= 1 is used exactly where indicated.

(1) Int u^2 = (1/lambda^2)(lambda) = 1/lambda.

(2) (u * u)(alpha) = (1/lambda^2) |[-lambda/2, lambda/2] ∩ [alpha - lambda/2, alpha + lambda/2]| = (1/lambda^2)(lambda - |alpha|)_+, the triangular kernel on [-lambda, lambda]. Since lambda <= 1, t(alpha) = 1 - |alpha| on this support, so

    Int t (u * u) = (2/lambda^2) Int_0^lambda (1 - a)(lambda - a) da = (2/lambda^2) [ lambda^2 - lambda^2/2 - lambda^3/2 + lambda^3/3 ] = (2/lambda^2) [ lambda^2/2 - lambda^3/6 ] = 1 - lambda/3 .

Hence m2 = 1 + 1/lambda - (1 - lambda/3) = 1/lambda + lambda/3.

(3) Int u^3 = (1/lambda^3)(lambda) = 1/lambda^2.

(4) Int (t * u) u^2 = (1/lambda^2) Int_{-lambda/2}^{lambda/2} (t * u)(alpha) d alpha = (1/lambda^3) IntInt_{|alpha| <= lambda/2, |alpha - beta| <= lambda/2} t(beta) d beta d alpha. Exchanging the order, the alpha-measure of {|alpha| <= lambda/2} ∩ {|alpha - beta| <= lambda/2} is (lambda - |beta|)_+, so

    Int (t * u) u^2 = (1/lambda^3) Int t(beta) (lambda - |beta|)_+ d beta = (1/lambda^3) [ lambda^2 - lambda^3/3 ] = 1/lambda - 1/3 ,

reusing the integral computed in (2) (valid for lambda <= 1).

(5) (b * u)(alpha) = (1/lambda) |[-1/2, 1/2] ∩ [alpha - lambda/2, alpha + lambda/2]|: for lambda <= 1 this is the trapezoid equal to 1 on |alpha| <= (1 - lambda)/2, decaying linearly to 0 at |alpha| = (1 + lambda)/2. Hence

    Int (b * u)^3 = (1 - lambda) · 1^3 + 2 · lambda Int_0^1 s^3 ds = (1 - lambda) + 2 (lambda/4) = 1 - lambda/2 ,

the plateau of length 1 - lambda contributing 1 each, and the two linear ramps of width lambda each contributing lambda Int_0^1 s^3 ds = lambda/4.

Assembling: T3 = 1/lambda^2 - 3 (1/lambda - 1/3) + 2 (1 - lambda/2) = 1/lambda^2 - 3/lambda + 3 - lambda, and

    m3 = 1 + 3 [ 1/lambda - 1 + lambda/3 ] + 1/lambda^2 - 3/lambda + 3 - lambda = 1 + 1/lambda^2 .   QED.

### Corollary 4.3 (anchor values, the doubles-plane diagnostic, and the moment margin)

    m2(1) = 4/3,   m3(1) = 2,   m2(1/2) = 13/6,   m3(1/2) = 5.

Define the doubles-plane diagnostic G(lambda) := m3 - (3 m2 - 2) — the excess of the null's cubic budget over the isolated-block doubles/pairs plane c = 3F - 2 of Theorem 3.4 — and the moment margin Marg(lambda) := 2 m2 - m3 (the section-7.3-style certificate margin). Then, for the flat window on (0, 1]:

    G(lambda) = 3 + 1/lambda^2 - 3/lambda - lambda ;         G(1) = 0 ,   G(1/2) = 1/2 ;
    Marg(lambda) = 2/lambda + 2 lambda/3 - 1 - 1/lambda^2 ;  Marg(1) = 2/3 ,   Marg(1/2) = -2/3 ,

and Marg has a unique sign change on [0.55, 0.66], at lambda_0 = 0.610511... (Marg < 0 below, > 0 above on that interval). Interpretations, each load-bearing for the no-go:

1. **G(1) = 0 is the "2 = 2" saturation:** at bandwidth one the sine budget m3(1) = 2 EXACTLY equals the isolated-block cubic demand of the 5/6-extremal (2/3 simple + 1/6 doubles: (2/3)·1 + (1/6)·8 = 2). The bandwidth-one cubic row alone cannot cut the doubles corner — the budget is exactly met.
2. **G(1/2) = +1/2 > 0:** at the operating bandwidth the null budget sits strictly ABOVE the doubles plane; a doubles-saturated adversary must supply +1/2 per zero of cubic through positional cross-terms — which T1's grid freedom supplies at zero cost (the gate's witness does exactly this).
3. **Marg(1/2) = -2/3 < 0:** the omega(m)-moment route's margin is negative at the proven operating point — a bite could never have come from the section-7.3 mechanism there, only from joint positional pricing; and the sign change at lambda_0 = 0.6105 is precisely where the gate's exploratory scan saw delta_0 turn positive (between lambda' = 0.55 and 0.60; RUN-REPORT 4.4), outside the proven ladder regime.

**Proof.** Substitute Theorem 4.2 into the definitions; the two displayed formulas are algebraic identities on (0, 1]. Values: G(1) = 3 + 1 - 3 - 1 = 0; G(1/2) = 3 + 4 - 6 - 1/2 = 1/2; Marg(1) = 2 + 2/3 - 1 - 1 = 2/3; Marg(1/2) = 4 + 1/3 - 1 - 4 = -2/3. Sign change: lambda^2 Marg(lambda) = 2 lambda + (2/3) lambda^3 - lambda^2 - 1 =: q(lambda) has q(0.55) < 0 < q(0.66) and q'(lambda) = 2 + 2 lambda^2 - 2 lambda > 0 (discriminant of 2 lambda^2 - 2 lambda + 2 is negative), so q is strictly increasing: the root is unique on the interval (indeed on (0, infinity)); numerically lambda_0 = 0.610511 (brentq, verify_t4.py). The extremal demand in interpretation 1 is Theorem 3.4's plane evaluated at the extremal (2/3 of zeros simple: per-zero F = 1, c = 1; 1/3 of zeros in doubles: per-zero F = 2, c = 4): mass-weighted cubic (2/3)(1) + (1/3)(4) = 2 = m3(1), and Frobenius (2/3)(1) + (1/3)(2) = 4/3 = m2(1) — both budgets exactly saturated at lambda = 1. QED.

### Corollary 4.4 (the m2 = kappa identity — sine budget equals the unconditional prime-side budget)

The closed form m2(lambda) = 1/lambda + lambda/3 coincides, at every lambda <= 1, with the value obtained by integrating the unconditional Montgomery/BGSTB24 pair-correlation form factor F(alpha) = delta_0(alpha) + |alpha| (on |alpha| <= 1) against the flat-window pair kernel:

    (1/lambda^2) Int_{-lambda}^{lambda} (lambda - |alpha|) [ delta_0(alpha) + |alpha| ] d alpha = (lambda + lambda^3/3)/lambda^2 = 1/lambda + lambda/3 = m2(lambda) .

That is: the sine-process null's second-moment budget IS the parent paper's unconditional prime-side kappa(lambda), exactly, on the whole band lambda <= 1 — the strongest possible identity check at second order (AUDIT 3.3), and the reason the gate's F' budget row is unconditional-data-backed. (Provenance: the prime-side statement — tr G-hat^2 <-> Int (lambda - |alpha|) F(alpha) d alpha with F unconditional and pointwise on the closed band 0 <= alpha <= 1 — is the parent paper's Remark 5.10 / Theorem 5.8 bookkeeping together with BGSTB24 Theorem 1, quoted from the evidence files, not re-derived here: Section 8, items Q1–Q2. The arithmetic identity displayed above is proven by the elementary integral: Int_0^lambda (lambda - a) a da = lambda^3/6, doubled, plus the delta term lambda.) No third-order analog is claimed: the identification c3(lambda') = m3(lambda') rests on RS-range GUE 3-level correlations and remains flag F2 (Section 8).

### Numerical confirmation (T4) — `verify/verify_t4.py` and `verify/verify_t4_mc.py`, run this session

* Fourier-side quadrature (dalpha = 2e-4) of the Lemma 4.1 integrals at lambda in {0.40, 0.50, 0.55, 0.61, 2/3, 0.75, 1.00}: matches both closed forms at every point, max deviation 1.7e-5 (at the piecewise-corner point 2/3; elsewhere <= 2e-6).
* Real-space determinantal quadrature (the route independent of Lemma 4.1): m2(1/2) = 2.166565 vs 13/6 (dev 1.0e-4, tail truncation); m3(1/2) via the 2D rho_3 integral = 4.9924 at truncation X = 40 and 4.9960 at X = 80, trending to 5 exactly as AUDIT 3.3's independent quadrature did (4.9896 -> 4.9932); m3(1) = 1.9999.
* Fresh CUE Monte Carlo (third independent sampler, own seeds; alias-free frequency-matrix assembly): m2(1/2) = 2.11063(135) at n = 64 and 2.15273(100) at n = 256; m3(1/2) = 4.7589(79) and 4.9408(59) — each within ~1 sigma of BOTH the gate's sampler and the auditor's (RUN-REPORT 4.1, AUDIT 3.2); two-point 1/n extrapolation: m2 -> 2.1668 (13/6 = 2.16667), m3 -> 5.0014 (5).
* Corollary values m2(1) = 4/3, m3(1) = 2, 13/6, 5, G(1) = 0, G(1/2) = 1/2, Marg(1) = 2/3, Marg(1/2) = -2/3: all exact in floating point; formula identities for G and Marg checked on an 81-point lambda-grid (dev <= 1.8e-15); margin root 0.610511.
* The values m2(1) = 4/3, m3(1) = 2 also discharge (for k <= 3) the v5-recalled sine moments m_k(1) = 1, 4/3, 2 (v5_p13.txt), as the gate and audit already recorded.

---

## 5. T5 — The capacity theorem: spectral escape is capped

With the repaired all-V ladder in place, how much cubic mass can spectral escape ever buy? This unit proves the sharp continuum capacity 2 sqrt(2) sqrt(C_led eps_g) — correcting both the adjudicator's 2 sqrt(C eps) two-term estimate and the naive 5/sqrt(3) point-mass profile — and thereby the positive complement of the no-go: absorption cannot be evaded by moving mass up the spectrum; only position/interference freedom remains (and T1 shows that channel suffices for the adversary).

**Setting (the continuum garnish LP; SPEC 4.2/9.3).** Heights are normalized so the ladder's absolute floor is 1. Spectral escape is a positive measure mu on [1, infinity) — mu([h, infinity)) is the count (per N) of escaped eigenvalue mass at height >= h — subject to:

    (Frobenius slack)    Int h^2 d mu(h) <= eps_g ,
    (all-V ladder)       mu([h, infinity)) <= C h^{-4}    for every h >= 1        (C = C_led).

The objective is the absorbable cubic charge  Cap(mu) = Int h^3 d mu(h). (Equivalently, in the SPEC's tail-function parametrization N(h) = mu([h, infinity)): maximize N(1) + 3 Int_1^infty h^2 N(h) dh subject to N(1) + 2 Int_1^infty h N(h) dh <= eps_g, N nonincreasing, N <= C h^{-4} — the two forms are identical by integration by parts, Int h^k d mu = N(1) + k Int_1^infty h^{k-1} N dh, and "N nonincreasing" is automatic for a tail function.)

### Theorem 5.1 (sharp capacity)

For every C > 0 and 0 < eps_g <= 2C:

    max_mu Int h^3 d mu = 2 sqrt(2) sqrt( C eps_g ) ,

attained by the min-profile  N_*(h) = C min( a^{-4}, h^{-4} ),  a = sqrt( 2 C / eps_g ). (As a measure: the constant tail on [1, a] carries NO mass; mu_* puts all its mass on the ladder boundary from a upward, density 4 C h^{-5} dh on (a, infinity), total mass C a^{-4}.)

**Proof.** *Upper bound.* Let mu be feasible and let a > 0 be arbitrary. Pointwise on [1, infinity):

    h^3 <= a h^2 + ( h^3 - a h^2 )_+            (h <= a: h^3 <= a h^2;  h > a: equality),

so, integrating and using the Frobenius constraint,

    Int h^3 d mu <= a eps_g + Int ( h^3 - a h^2 )_+ d mu .

For the second term write g(h) = (h^3 - a h^2)_+ = Int_a^h g'(s) ds for h >= a (g = 0 for h <= a), with g'(s) = 3 s^2 - 2 a s > 0 on (a, infinity). By Tonelli and the ladder,

    Int g d mu = Int_{h >= a} Int_a^h g'(s) ds d mu(h) = Int_a^infty g'(s) mu([s, infinity)) ds
              <= Int_a^infty ( 3 s^2 - 2 a s ) C s^{-4} ds = C ( 3/a - a · (1/a^2) ) = 2 C / a .

Hence Int h^3 d mu <= a eps_g + 2 C / a for EVERY a > 0; minimizing over a (calculus: minimum at a = sqrt(2C/eps_g)) gives Int h^3 d mu <= 2 sqrt(2 C eps_g) = 2 sqrt(2) sqrt(C eps_g).

*Attainment.* eps_g <= 2C makes a = sqrt(2C/eps_g) >= 1, so N_* is an admissible tail function with N_* <= C h^{-4} everywhere (equality beyond a). Its Frobenius charge:

    N_*(1) + 2 Int_1^infty h N_* dh = C a^{-4} + 2 C a^{-4} (a^2 - 1)/2 + 2 C Int_a^infty h^{-3} dh = C a^{-4} + C a^{-4}(a^2 - 1) + C a^{-2} = 2 C / a^2 = eps_g .

Its cubic charge:

    N_*(1) + 3 Int_1^infty h^2 N_* dh = C a^{-4} + C a^{-4}(a^3 - 1) + 3 C Int_a^infty h^{-2} dh = C/a + 3 C/a = 4 C / a = 2 sqrt(2) sqrt(C eps_g),

using 4C/a = 4C sqrt(eps_g/2C) = 2 sqrt(2) sqrt(C eps_g). Both constraints hold with equality where they bind (Frobenius exactly; ladder exactly on [a, infinity)), and the value meets the upper bound. QED.

*Remark (where each constraint bites — the squeeze, made exact).* The optimal dual split is Int h^3 d mu <= a · [Frobenius] + [ladder integral above a]: bounded heights (h <= a) are blocked by the Frobenius cost (the a eps_g term — mass at height h buys h^3 of cubic but pays h^2 of Frobenius, ratio h <= a), divergent heights by the ladder cap (the 2C/a term). The absolute floor C_abs (here normalized to 1) appears NOWHERE in the upper bound — only in the attainability condition a >= 1 — which is the precise form of the adjudication's overruling of the "bite iff 2 C_led / C_abs < 4/3" claim: sharp constants at the floor are irrelevant against this adversary class.

### Proposition 5.2 (the naive point-mass-plus-tail profile is infeasible)

The profile mu_naive = (ladder-saturating atom at b) + (ladder-saturating tail above b), i.e. an atom of size n0 = C b^{-4} at height b plus tail mu([h, infinity)) = C h^{-4} for h > b, with b = sqrt(3C/eps_g), has Frobenius charge exactly eps_g and cubic charge

    n0 b^3 + 4 C / b = C/b + 4C/b = 5 C / b = (5 / sqrt(3)) sqrt( C eps_g )  =  2.8868 sqrt(C eps_g) ,

BUT it violates the cumulative ladder on the interval ( 2^{-1/4} b, b ): there mu_naive([h, infinity)) = n0 + C b^{-4} = 2 C b^{-4} > C h^{-4}. Hence the true optimum is Theorem 5.1's 2 sqrt(2) = 2.8284... < 5/sqrt(3), and the earlier bookkeepings — the formulator's first-pass 5/sqrt(3) and the adjudicator's two-term dyadic 2 sqrt(C eps) — are both superseded by the min-profile constant (as the SPEC's F6 flag records; same order, conclusions unchanged).

**Proof.** The tail part has density 4 C h^{-5} dh on (b, infinity) (so that its cumulative count is C h^{-4}). Frobenius: atom n0 b^2 = C b^{-2}; tail Int_b^infty h^2 · 4 C h^{-5} dh = 2 C b^{-2}; total 3 C b^{-2} = eps_g exactly at b = sqrt(3C/eps_g). Cubic: atom n0 b^3 = C/b; tail Int_b^infty h^3 · 4 C h^{-5} dh = 4C/b. Total 5C/b = 5 C sqrt(eps_g / 3C) = (5/sqrt 3) sqrt(C eps_g). Ladder violation: for 2^{-1/4} b < h < b the cumulative count is n0 + C b^{-4} = 2 C b^{-4}, while the cap is C h^{-4} < C (2^{-1/4} b)^{-4} = 2 C b^{-4} — strictly smaller than the count throughout the OPEN interval, since C h^{-4} < 2 C b^{-4} iff h > 2^{-1/4} b. (2^{1/4} = 1.1892 — the SPEC's "(a/1.19, a)".) QED.

### Corollary 5.3 (capacity is o(N): the positive complement of the no-go)

In the gate's units (capacities per N), the maximal cubic shift purchasable by spectral escape under the repaired row system is

    |Delta cubic| <= 2 sqrt(2) sqrt( C_led eps_g ) N = o(N)      as eps_g -> 0 at fixed C_led

(and still o(N) for any C_led = O(1) ladder constant; e.g. C_led = 1000, eps_g = 1e-8: capacity 0.0089 N). Consequently a doubles-vs-pairs-scale swing (Theta(N), e.g. (4/3)N) can NEVER be produced by spectral escape once the all-V ladder is consumed: any absorption of the cubic block must run through position/interference freedom — which is exactly the channel T1 exhibits and the gate's witness uses. (In the gate's coupled LP form this theorem enters as rows (R-5')/(R-6'): garnish Frobenius budget g_F with cubic slack 2 sqrt 2 sqrt(C_led g_F) N, the concave sqrt handled by tangent cuts; the run found the fuzz row not even load-bearing for the absorption — RUN-REPORT Sec 4.2.)

**Proof.** Immediate from Theorem 5.1 (the bound scales linearly in N by homogeneity of all rows); the numeric is 2 sqrt 2 sqrt(1000 · 1e-8) = 0.008944. QED.

### Numerical confirmation (T5) — `verify/verify_t5.py`, run this session

* Attainment profile at C = 1, eps_g = 0.02 (a = 10): quadrature gives Frobenius = 0.02000000 (dev 4e-11) and cubic = 0.40000000 = 2 sqrt 2 sqrt(C eps) (dev 9e-13).
* Discretized LP over point masses on a geometric height grid (the independent route): value 0.3684/0.3887/0.3935 at h_max = 100/400/2000 with 600 grid points, plus the truncation tail 3C/h_max: 0.3984/0.3962/0.3950; refining the grid (2000 points, h_max = 2000; 4000 points, h_max = 8000): 0.3985, 0.3991 -> 0.4000 from below, never exceeding the theorem's bound. (Same convergence pattern as SPEC verify V5's 2.775 + 0.050 = 2.825 vs 2 sqrt 2 = 2.8284 and RUN-REPORT's 2.8244 at h_max = 400, at their (C, eps) normalization.)
* LP optimal profile shape: cumulative tail matches C min(a^{-4}, h^{-4}) to < 3e-2 relative on the plateau and to machine precision on the ladder branch (h >= a).
* Naive profile: reproduces 5/sqrt(3) sqrt(C eps) = 0.408248 exactly at Frobenius exactly eps; its cumulative count 2 C b^{-4} = 8.89e-5 exceeds the ladder cap C h^{-4} in [4.44e-5, 8.89e-5) throughout (2^{-1/4} b, b) — infeasible, and strictly above the LP optimum 0.3950 < 0.4082.
* Duality identity a eps + 2C/a = 4C/a at a = sqrt(2C/eps) and the scaling law verified across (C, eps) in {(10, 1e-3), (100, 1e-4), (1000, 1e-8)}.

---

## 6. T6 — Divergent-cutoff vacuity (the garnish theorem)

The "provable today, no LP needed" half of the no-go, mandated by merge-guidance item (3): a scalar Schatten-3 tail row with ANY divergent cutoff — however slowly divergent — is unconditionally absorbed by the garnish construction. This is killer 1's layer-1 finding, VERIFIED by the adjudication (computation (b), upheld as K1-fatal LAYER 1) and reproduced in the gate's Tier-A regressions; here it is stated and proven as a clean theorem. Its counterpart is T5: replacing the scalar tail row by the all-V ladder caps the same channel at o(N) — together they are the complete pricing of spectral escape.

**Setting (the as-written row system, family semantics).** Let N = N(T) -> infinity be the normalization (zeros per period) and V0 = V0(T) -> infinity a divergent cutoff with V0 = o(N^{1/3}) (any polylog cutoff against N ≍ T log T qualifies — in particular the proposal's V0 = (loglog T)^3 and every (log T)^A). The as-written system consumed its equalities "with o(N) precision" — no fixed tolerance rate — so feasibility is a property of FAMILIES: a family of model configurations (c_T) (Section 0.4; NO mark-alphabet cap was imposed as written), with spectral data read from isolated-block spectra (atoms of mark m: eigenvalue m; the abstract aggregated system of the proposal's Step 4, in which the adjudication audited the construction), is admissible for S_written iff

    (W1)  mass:               Sum m = N   (exact, each T);
    (W2)  Frobenius:          F = kappa N + o(N) ;
    (W3)  signed cubic:       C = c3 N + o(N) ;
    (W4)  scalar tail row:    Sum_{|lambda_i| >= V0} |lambda_i|^3 = o(N) ;
    (W5)  count/inertia rows imposed only at thresholds V >= V0 (as the proposal stated them), plus n_- <= p;
    objective: liminf N_d / N (or liminf p1).

(This is the semantics under which the adjudication verified the construction; a fixed tolerance RATE eta(T) shrinking faster than 1/V0 would be a STRONGER system than the one written — and would anyway be dishonest bookkeeping, since the consumed prime-side equalities carry no such rate.)

### Theorem 6.1 (garnish absorption)

Let (c_T) be any family of configurations satisfying (W1), (W2), (W4), (W5), containing at least delta_0' N simple on-line atoms for some fixed delta_0' > 0, and whose signed cubic falls short of the (W3) equality by Delta_T N: C(c_T) = c3 N - Delta_T N + o(N), with 0 <= Delta_T <= Delta_max for a fixed constant Delta_max. Put

    h0 = floor( V0 / 2 ),      n0 = ceil( Delta_T N / h0^3 ) ,

and let c'_T be c_T with n0 additional isolated on-line atoms of mark h0 (placed at unoccupied, well-separated positions) and n0 h0 simple atoms deleted (mass rebalance). Then for all T large enough, c'_T satisfies EVERY row of S_written(T), and

    N_d(c'_T) = N_d(c_T) - n0 (h0 - 1) <= N_d(c_T) ,          p1(c'_T) <= p1(c_T) .

Row-by-row bookkeeping (all per N; each shift is o(1) as T -> infinity):

    mass:        + n0 h0 - n0 h0 = 0                                        (exact);
    Frobenius:   + n0 h0^2 / N - n0 h0 / N = Delta_T / h0 + O(1/h0^2 + h0^2/N) = o(1)   ((W2) still holds: the shift is o(N));
    cubic:       + n0 h0^3 / N - n0 h0 / N = Delta_T + O(h0^3 / N) + O(1/h0^2) = Delta_T + o(1)   (lands the (W3) equality; the O-terms are o(1) since h0 -> infinity and h0^3 = o(N));
    tail row:    + 0     (the garnish eigenvalues sit at h0 = floor(V0/2) < V0: no mass at or above the cutoff; deleting simples only removes below-cutoff mass);
    count rows at V >= V0:  + 0   (same reason);
    n_- <= p:    unchanged (the garnish adds only positive on-line eigenvalues, no pairs).

**Proof.** *Feasibility of the construction.* n0 h0 <= (Delta_max N / h0^3 + 1) h0 = Delta_max N / h0^2 + h0 = o(N) < delta_0' N for T large: enough simples exist to delete. The garnish atoms are isolated on-line atoms of mark h0, each contributing eigenvalue h0 (Section 0.2 normalized units), Frobenius h0^2, cubic h0^3, mass h0.
*Row shifts.* Mass: adds n0 h0, deletes n0 h0 — exact. Cubic: adds n0 h0^3 in [Delta_T N, Delta_T N + h0^3], subtracts n0 h0 <= Delta_max N/h0^2 + h0 (each deleted simple had cubic charge 1); the net shift is Delta_T N + O(h0^3) + O(N/h0^2) = Delta_T N + o(N), since h0 -> infinity and h0^3 = o(N). Hence C(c'_T) = [c3 N - Delta_T N + o(N)] + [Delta_T N + o(N)] = c3 N + o(N): (W3) holds for the garnished family. Frobenius: adds n0 h0^2 <= Delta_max N / h0 + h0^2 = o(N), subtracts n0 h0 = o(N); (W2)'s o(N) window absorbs it. Tail and count rows: every garnish eigenvalue equals h0 < V0, and V-thresholds of (W4)/(W5) all sit at V >= V0 > h0, so the added spectrum is invisible to them; deleted simples only decrease those rows. Inertia: no negative eigenvalues added. *Objectives.* N_d: + n0 (the new atoms) - n0 h0 (deleted simples) = -n0(h0 - 1) <= 0. p1: the deleted atoms were simple (count decreases by n0 h0); the added atoms have mark h0 >= 2, contributing 0 to p1. QED.

### Corollary 6.2 (vacuity of the scalar divergent-cutoff cubic row: delta_0 = 0 as written)

Suppose the two-moment system {(W1), (W2)} admits optimizer families (c_T) (objective within o(1) of its infimum) that have a fixed positive simple fraction, spectra bounded by a fixed constant, and a bounded cubic DEFICIT: C(c_T) <= c3 N + o(N), with c3 N - C(c_T) <= Delta_max N. Then, for both benchmarks,

    inf over S_written of the objective  =  inf over the two-moment system {(W1), (W2)} of the objective ,

i.e. the marginal value of the entire block {(W3) signed cubic + (W4) scalar tail + (W5) high-threshold count rows} is ZERO: delta_0 = 0 as written. The deficit hypothesis is the actual situation of the gate's classes: the corner families of Theorem 2.3 undershoot the cubic budget (Corollary 4.3, G(1/2) = +1/2 > 0: the null budget sits strictly ABOVE the doubles plane, so doubles-saturated configurations are short, not long — the shipped witness accordingly sits at the LOWER cubic edge, E[C'] = B3(1 - eps)), and the 5/6-extremal family has simple fraction 2/3. In particular, whatever cubic demand (up to any fixed Delta_max — e.g. the full "4/3 N doubles-vs-pairs swing" of the proposal's Step-4 narrative) the cubic row was hoped to impose on the two-moment-degenerate corner, the garnish supplies it invisibly, at an objective DECREASE.

**Proof.** One direction is trivial (more rows can only raise the inf). For the other, take an optimizer family (c_T) as hypothesized — e.g. the marks-{1,2} corner laws of Theorem 2.3, whose spectra lie in {1, 2}. Bounded spectra plus V0 -> infinity make (W4) and the V >= V0 count rows identically zero for T large, so (c_T) satisfies (W1), (W2), (W4), (W5). Its cubic deficit Delta_T = (c3 N - C(c_T))/N + o(1) lies in [0, Delta_max]. Apply Theorem 6.1: the garnished family (c'_T) is admissible for ALL of S_written, with objective liminf N_d(c'_T)/N <= liminf N_d(c_T)/N (the construction strictly lowers N_d and p1). Hence inf over S_written <= inf over the two-moment system; delta_0 = 0. QED.

### Remark 6.3 (what this theorem does and does not say — the repair structure)

1. **It kills the scalar row, not the direction.** The vacuity is a statement about the AS-WRITTEN system, whose count/tail information starts only at V0. The proposal's own Chebyshev proof in fact yields the all-V ladder n(V) <= C_led N V^{-4} for every V >= C at theta < 1 (the theorem underclaimed its proof — adjudication (b)); under THAT system the garnish channel is not free but capped, and the cap is exactly T5's 2 sqrt(2) sqrt(C_led eps_g) N = o(N). Repair R1 ("claim what the proof proves") is the difference between Corollary 6.2 and Theorem 5.1.
2. **The garnish needs unbounded marks** (h0 = floor(V0/2) -> infinity): it lives outside every fixed-W alphabet — which is why R4/R5 mandated the divergent-W adversary class and why "a break at marks-{1,2} is not evidence." (A pair-based garnish variant with slowly divergent pair multiplicity reaches the same conclusion through Proposition 3.2's deep-pair blocks; the atom form above is the cleanest.)
3. **Together with the gate:** T6 disposes of spectral escape as written; T5 caps it as repaired; the gate's decided content is that the remaining channel — position/interference freedom — absorbs the cubic block too (T1 grid decoupling + occupancy-2 clustering), at delta_0 = 0 exactly. That three-part structure IS the sharpened no-go.

### Numerical confirmation (T6) — `verify/verify_t6.py`, run this session

* Shift table at Delta = 4/3, V0 = (loglog T)^3, h0 = V0/2, over the adjudication's own log T grid {18.4, 41.4, 92.1, 230.3} extended to {1000, 1e6}: Frobenius shift 4/(3 h0) = 0.0992, 0.0497, 0.0282, 0.0164, 0.0080, 0.0010 -> 0; trace shift Delta/h0^2 = 8.7e-3 ... 7.7e-7 -> 0; N_d shift NEGATIVE (-8.0e-3 ... -7.7e-7); cubic shift +4/3 exactly; tail row 0; count rows at V >= V0: 0. This reproduces the adjudication's computation-(b) audit ("trace +Delta/h0^2 -> 0, Frobenius +Delta/h0 -> 0, cubic +4/3 full swing, tail row 0, count row 0") and RUN-REPORT Tier-A regression (ii)'s "Frobenius cost 4/(3 h0) -> 0".
* Abstract LP demonstration (variables: simple fraction, double fraction, garnish count at height h0; rows: mass, Frobenius band, cubic equality at the demand c_target = 2 + 4/3 that the doubles corner misses by 4/3): WITHOUT the garnish variable the system is INFEASIBLE (the cubic row appears to cut the corner — the fake bite); WITH it, min N_d/N = 0.8298 / 0.8273 / 0.8321 at h0 = 200 / 1000 / 10000 — i.e. 5/6 - O(tol) - o(1), the two-moment corner restored (at tol = 0.002, h0 = 1e4: 0.832066 vs the T2 corner 5/6 - (2/3)(0.002) = 0.832000).
* Exact rational instance (N = 120000, h0 = 20, Delta = 4/3, Fraction arithmetic): mass 1 -> 1 exactly; Frobenius/N 4/3 -> 1.396667 (shift = Delta/h0 - Delta/h0^2 exactly); cubic/N 2 -> 3.33 (shift = Delta - Delta/h0^2 exactly); N_d/N 0.833333 -> 0.830167 (a DECREASE); tail and count rows untouched (h0 < V0 = 2 h0).

---

## 7. Consolidated numerical log (this session)

All scripts in `results/a4-no-go/verify/`; outputs in the JSON files named below. Total compute: < 1 minute.

| unit | script | key outputs | output file |
|---|---|---|---|
| T1 | `verify_t1.py` | grid exactness 9.1e-13 (N=64) / 4.1e-12 (N=128), 40 random configs each, two evaluation routes; general-band lemma 3.2e-12; off-grid and half-band controls nonzero; continuum lattice exact (0.0); 4128/33 worked value | `verify_t1_out.json` |
| T2 | `verify_t2.py` | per-atom inequalities exhaustive m <= 50 + 20k random draws, 0 violations; LP = closed forms to 3e-16 at eps in {.10, .05, .02, .002}, both objectives; two-sided band identical; Fraction identities; witness cross-check P = (3N - E[F1])/(2N) to 6e-13 | `verify_t2_out.json` |
| T3 | `verify_t3.py` | block law at machine precision (cos taper: eigs to 7.8e-14, <p,q> to 1.7e-14, position-independent), flat taper at truncation 1.3e-5; A-table vs SPEC <= 4e-6; per-zero identity to 9.1e-13 (m <= 5, all depths); shallow-pair 8.0005 / 8.0313 matching AUDIT | `verify_t3_out.json` |
| T4 | `verify_t4.py`, `verify_t4_mc.py` | Fourier quadrature = closed forms (<= 2e-6 away from corner points) at 7 lambdas; real-space determinantal m3(1/2): 4.9924 (X=40) -> 4.9960 (X=80) -> 5; fresh CUE MC n=64/256 within 1 sigma of both prior samplers, 1/n extrapolation 2.1668 / 5.0014; margin root 0.610511 | `verify_t4_out.json`, `verify_t4_mc_out.json` |
| T5 | `verify_t5.py` | attainment profile exact (4e-11 / 9e-13); discrete LP -> 0.4000 from below (0.3950 / 0.3985 / 0.3991 under refinement); naive 5/sqrt3 profile reproduced and ladder violation exhibited on (2^{-1/4} b, b); duality and scaling checks | `verify_t5_out.json` |
| T6 | `verify_t6.py` | shift table -> 0 on the adjudication grid; abstract LP: infeasible without garnish, 5/6 - O(tol) with; exact-rational instance, all shifts exact | `verify_t6_out.json` |

---

## 8. Provenance, flags, and how these units may be cited (standing order 5)

**Proven in full in this document (no external input beyond elementary analysis):** Lemma 1.1, Theorem 1.2, Propositions 1.3–1.4 (model part), Lemmas 2.1–2.2, Theorem 2.3, Corollary 2.4, Lemma 3.1, Propositions 3.2–3.3, Theorem 3.4, Lemma 4.1, Theorem 4.2, Corollaries 4.3 and 4.4 (arithmetic part), Theorem 5.1, Proposition 5.2, Corollary 5.3, Theorem 6.1, Corollary 6.2.

**Quoted from the evidence base (NOT re-derived here), each used only where marked:**

* Q1 — The determinantal correlation functions of the sine process (rho_2, rho_3) and the identification of the gate's null budgets with the sine-process moments: standard theory, stated as the null's DEFINITION per SPEC 2.1; the CUE -> sine convergence used to interpret the MC is likewise standard and enters no proof.
* Q2 — The prime-side member of Corollary 4.4's identity: that tr G-hat^2 for zeta is unconditionally Int (lambda - |alpha|) F(alpha) d alpha with F(alpha) = delta_0 + |alpha| + o(1) pointwise on the closed band — parent paper Remark 5.10/Theorem 5.8 bookkeeping plus BGSTB24 Theorem 1 (Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh, arXiv:2306.04799, fetched: `fetched-r3/r3s-06-bgstb-2306.04799.pdf`, on disk, 210,602 bytes — presence and size re-verified this session; statement read per FOLLOWUP-REPORT Sec 4, with its three riders: depth-aggregate only, O(N/sqrt(log T)) finite-T slack, second moment only).
* Q3 — The finite-T o(1) in Proposition 1.4's Weil–Gabor statement: the parent paper's window-correction bookkeeping (tx_081's adversary-lattice record is the campaign evidence).
* Q4 — The gate outcome itself (delta_0 = 0 over the 940-record grid; the witness; the near-CUE decision-grade follow-up; the p1 rerun): quoted from RUN-REPORT/AUDIT/FOLLOWUP as context in Remarks 2.5 and 6.3 — these units explain and bound the outcome; they do not re-run it. (Cross-checks re-run here: the witness columns' F1 = Sum m^2, the corner law reproducing P = 0.8050957, and the p1 corners.)

**Flags carried (unchanged by this document):**

* F2 — the identification c3(lambda') = m3(lambda') (third-order budget) rests on RS-range GUE 3-level correlations and the section-5 diagonal method's polylog-window uniformity. T4 proves the SINE value; nothing here upgrades the identification. (The gate's absorption was verified insensitive to the c3 center — AUDIT break attempt 7.)
* F4 — the all-V ladder consumed by T5's system rests on Theorem 1(ii)-repaired, whose R2 bridge is unproven; per the gate semantics the absorption branch is STRENGTHENED by assuming the ladder, and T6 needs no ladder at all.
* Scope riders for the paper (from AUDIT Sec 5, binding on wording): (i) the exact delta_0 = 0 is flat/flat-window-specific — with the Montgomery–Taylor cosine window at lambda = 1 the grid degeneracy breaks, leaving O(1e-4)-bounded unconverged residuals (T1's mechanism shows exactly why: a cosine window's kernel zeros are not equally spaced, so no site grid kills all lambda = 1 cross-terms simultaneously); (ii) the model-level theorem class is atom-only (Remark 2.6); (iii) the no-go headline is scoped to the two benchmarks of Theorem 2.3 — the N_d >= 5/6 benchmark and the simple-fraction 2/3 corner — both now covered (FOLLOWUP Task 2); the formalized 0.6818287 ceiling belongs to the window-optimized certificate class and is NOT re-decided by the flat/flat gate.

**Correction of record embedded in these units (already executed in the direction file, re-proven here):** the "+8 vs 0" doubles-vs-pairs cubic separation premise of the original proposal, and the adjudication's computation-8 phase model ((+1, -1) at u L = 1 with cubic ~ 0), are FALSE under the true block law: Proposition 3.2 gives pair cubic charge 2 m^3 (1 + 3 A^2) >= 8 m^3 at every depth, and Theorem 3.4 places pairs and doubles on the same affine plane c = 3F - 2. tx_082's recorded block facts (pair eigenvalues m L^2 a (1 ± A)) were correct throughout.

**Lean queue note.** The formalization-ready units, in dependency order: Lemma 1.1 (pure finite Fourier algebra on Z_M — `decide`-adjacent), Theorem 1.2, Lemma 2.2 (per-atom integer inequalities), Theorem 2.3 (exact-rational LP witness + row inequalities, PairCeiling architecture with the two kernels evaluated on the grid: all data rational), Proposition 3.3/Theorem 3.4 (polynomial identities), Theorem 5.1 (one-page real analysis), Theorem 6.1 (bookkeeping). Theorem 4.2 needs real integration but only of piecewise polynomials.



