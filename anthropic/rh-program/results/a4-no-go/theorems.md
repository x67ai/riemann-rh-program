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

Eigenvalue data (ladder counts, inertia) come from the Hermitian frequency matrix B[j, j'] = sqrt(u_j u_{j'}) c_{j-j'} (j, j' in B), whose k-th trace equals the k-th trace row exactly (alias-free tight-frame compression; RUN-REPORT deviation 1). At the primary geometry N = 64, lambda = 1: M = 65 harmonics; lambda' = 1/2: M' = 33.

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

where the s-range {-N/2, ..., N/2} is a COMPLETE residue system mod (N+1) and c_s is the Z_{N+1} DFT of the mark vector. The weights (M' - |s|)/M'^2 are non-constant across residues (triangular, and zero for no s in the range only when |s| <= N/2 — at N = 64: weight 1/33 at s = 0 down to 1/33^2 at |s| = 32), so F' is a strictly position-sensitive functional of the grid configuration, subject only to the Parseval constraint Sum_r |c_r|^2 = (N+1) Sum m^2.

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

* Exactness on the grid: 40 random site-subsets with random marks 1..8, at N = 64 AND N = 128, evaluated through the Fourier double-sum route and independently through the eigenvalues of the frequency matrix B: max |F1 - Sum m^2| = 9.1e-13 (N = 64) and 4.1e-12 (N = 128); eig route agrees (max 9.1e-13). Matches AUDIT 3.1's independent 4.5e-13.
* General flat-band lemma (Lemma 1.1): 20 random (N, M, band offset j0) draws including asymmetric bands: max deviation 3.2e-12.
* Controls: off-grid uniform-position configurations give |F1 - Sum m^2| in [1.3e-2, 62.5] (identity genuinely fails off the grid); on-grid at lambda' = 1/2 gives |F' - Sum m^2| in [40.9, 120.8] (the half-band kernel is alive, Proposition 1.3).
* Continuum lattice: 20 random integer-lattice configurations, deviation 0.0 to machine precision; half-band lattice values match 2/(pi k)(-1)^{(k-1)/2} exactly.
* Worked value: 4096/33 + 32/33 = 4128/33 = 125.090909..., equal to the shipped witness column F' (dev < 3e-6, the optimizer's position rounding; the clean grid description is canonical).

<!-- CONTINUE:T2 -->
