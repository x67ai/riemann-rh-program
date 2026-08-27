# Closing the pair-interference channel (AUDIT finding MINOR-4 / break-attempt 6)

> **Dated revision (2026-08-27).** Session 8's interval hardening (`verify/o1_crowding_interval.py`; report `o1-n128-report.md`) found the Session-7 full-family crowding ratio 0.9775 to be a 0.004-grid artifact. This revision re-scopes the multi-pair closure: ledger constant interval-certified C* <= 0.98465 < 1 on pair depths <= 0.156 (w <= 0.98); certified ledger FAILURE (Sgen2 >= 1.01405 > 1 at d = d' = 0.159) on w in (0.98, 1], where coverage is the re-run crowd attacks (min F1 - T >= +17.47) plus the unconditional 8/9 backstop — (MI) itself is numerically unrefuted there. The N = 128 re-run reproduces all identities. A strengthening-by-honesty: the certified region's constant is now rigorous, and the overreach is withdrawn. Complete edit list: `o1-n128-report.md` section 5.


**Program:** RH program, direction A4 (merged A2+A4, adjudicated survives-with-repairs 5.5, binding). **Task:** close analytically the one channel of the M2-gate no-go model theorem not closed by the atom-only sandwich: whether off-line pairs can push the bandwidth-one Frobenius F1 below the mark-accounting floor and thereby beat the lemmaR_tight corner (AUDIT.md Section 4 item 6 and Section 5 finding 4; `theorems.md` Remark 2.6).
**Date:** 2026-08-26. **Model:** the gate's finite-circle geometry, N = 64, lambda = 1, flat window (the primary decision configuration of `results/a4-m2-gate/SPEC.md` Sections 1.4 and 5.1).
**Verification discipline (standing order 5):** every number and every identity in this note was re-derived or re-computed in this session with an independent implementation of the Fourier assembly (NOT the gate's `code/`; the gate's published values are used only as cross-checks). Scripts and raw outputs: `verify/pairchan_*.py`, `verify/pairchan_verify_out.json` (this directory). Where a constant is a certified finite computation rather than a closed form, that status is stated at the point of use.

---

## 0. Results in one box

Write, for an admissible configuration c (Section 1), M(c) = total mark mass, N_d(c) = number of distinct zeros, and

    T(c) := 3 M(c) - 2 N_d(c),      S2(c) := Sum_z m_z^2   (each pair member counted m^2).

The single inequality that extends the no-go model theorem from the atom-only class to pair-containing configurations is

    (MI)    F1(c) >= T(c),

because (Lemma 1.1) (MI) per configuration gives, for every law with mass N and E[F1] <= (4/3) N (1 + eps), BOTH corners: E[N_d]/N >= 5/6 - (2/3) eps and E[p1] >= 2/3 - (4/3) eps. What is proved here:

1. **(MI) is FALSE for real (fractional) marks** — an explicit vacancy-lattice + shallow-pair family violates even F1 >= S2 for every depth d > 0 at small real pair mark (Proposition 3.1, exact closed-form margin). Any closure MUST use mark integrality. This explains structurally why the channel resisted soft convexity arguments: the inequality is not a positivity of the quadratic form but a lattice-point property of it.
2. **Theorem A (single pair, unconditional):** every configuration with EXACTLY ONE pair (arbitrary atoms, arbitrary integer marks, arbitrary positions) satisfies (MI) whenever the pair depth is d <= 0.45 in circle units — i.e. dimensionless w = 2 pi d <= 2.8, covering the gate's ENTIRE pair-depth family (w in (0,1], deep probes w in {1.5, 2}, i.e. d <= 0.3183) with >= 34% capacity margin. For mass <= N configurations (the LP class) it also holds for every d >= 1.0. The window (0.45, 1.0) is certified numerically (worst capacity ratio 0.68; direct adversarial searches, Section 7).
3. **Theorem B (any number of pairs):** (MI) holds for every configuration all of whose pair depths are <= 0.13 (w <= 0.82), unconditionally; and for all pair depths <= 0.156 (w <= 0.98) modulo one isolated cell-crowding cap whose ledger constant is interval-certified (Session 8): sup_{d,d' <= 0.156} Sgen2 <= 0.98465 < 1 by per-cell rigorous enclosures (`verify/o1_crowding_interval.py`). On the deepest sliver d in (0.156, 1/(2 pi)] (w in (0.98, 1]) the ledger inequality itself fails — interval-certified Sgen2(0.159, 0.159) >= 1.01405 > 1 — so the ledger route claims nothing there; coverage on the sliver is the Section-7 attacks (re-run at d = 0.158/0.159, min F1 - T >= +17.47) plus the unconditional 8/9 backstop of Theorem D. The Session-7 ratio 0.9775 was the 0.004-grid maximum, i.e. the constant of the family capped at d <= 0.156, not the full-family sup.
4. **Theorem C (equal-depth pair-only, exact):** all pairs at one common depth and no atoms: F1 >= S2 + 2 Sum_p m_p^2, at EVERY depth, by a one-line cosh^2 factorization.
5. **Theorem D (unconditional backstop, no restrictions):** for EVERY admissible configuration — any number of pairs, any depths, any marks — N_d >= (4/9)(3M - F1). Hence even in the regimes not covered by A/B the LP value cannot drop below (8/9)(5/6 - (2/3) eps) = 20/27 - (16/27) eps = 0.7407 - 0.593 eps: the maximal conceivable pair advantage on the corner is <= 5/6 - 20/27 = 5/54 ~= 0.0926, unconditionally.
6. **Sharp conjecture (numerically exhaustive, Section 7):** F1 >= Sum_atoms (3m - 2) + 4 Sum_pairs m_p^2 — every pair pays its full flattened-double cost 4 m^2 and interference recovers NOTHING; the global minimum of F1 - T over ~10^4 adversarially optimized configurations is EXACTLY Sum_p 2(2 m_p^2 - 3 m_p + 2) (>= 2 per pair), attained only in the depth->0 grid limit.

**Consequence for the no-go paper:** the model-level corner theorem no longer needs the atom-only scoping for the gate's adversary class. For laws over columns whose pairs lie in the R5 depth family (w <= 1) with at most... — precisely: single-pair columns of any gate depth (w <= 2.8), and multi-pair columns with all depths w <= 0.82 (unconditional) or w <= 0.98 (modulo the crowding cap; ledger constant interval-certified); multi-pair columns with a depth in (0.98, 1] rest on the numerical record plus the 8/9 backstop — the exact corner 5/6 - (2/3) eps and the simple-fraction corner 2/3 - (4/3) eps hold with pairs allowed. Everything else is floored at 8/9 of the corner unconditionally. AUDIT finding MINOR-4 is discharged for the gate's class; the honest residue is listed in Section 9.

---

## 1. Setting

Finite circle of circumference N = 64 (positions in mean-gap units, N-periodic). Flat window at bandwidth lambda = 1: harmonics u_j = 1/65 for |j| <= J = 32; assembly weights w_s = (65 - |s|)/65^2 for |s| <= 64 (the autocorrelation w = u * u; Sum_s w_s = 1). An **admissible configuration** c consists of

* on-line atoms: positions theta_a in [0, N), integer marks m_a >= 1;
* off-line conjugate pairs: position theta_p, depth d_p > 0 (circle units; the SPEC's dimensionless depth is w = 2 pi d, so the R5 family u in [0, 1/L'] is d in (0, 1/(2 pi)] and the deep probes w in {1.5, 2} are d in {0.2387, 0.3183}), integer pair multiplicity m_p >= 1.

Fourier data and the lambda = 1 Frobenius row (SPEC 1.4, re-implemented independently):

    c_s = Sum_a m_a e^{-2 pi i s theta_a / N} + Sum_p 2 m_p cosh(2 pi s d_p / N) e^{-2 pi i s theta_p / N},
    F1  = Sum_{|s| <= 64} w_s |c_s|^2 .

Counting: M = Sum_a m_a + 2 Sum_p m_p (mass), N_d = #atoms + 2 #pairs (distinct zeros), n_1 = #(mark-1 atoms) + 2 #(mult-1 pairs) (simple zeros, the convention of `theorems.md` Section 0.4). Targets: T = 3M - 2 N_d = Sum_a (3 m_a - 2) + Sum_p (6 m_p - 4); S2 = Sum_a m_a^2 + 2 Sum_p m_p^2. For integer marks S2 >= T (per zero: m^2 - (3m - 2) = (m-1)(m-2) >= 0), so F1 >= S2 implies F1 >= T but not conversely; (MI) is the weaker and sufficient target.

**Verified basic facts** (`pairchan_verify_all.py`, section V): grid Parseval F1 = Sum m^2 on the 65-site grid to 1.8e-12 (40 random subsets/marks — matches AUDIT 3.1); isolated-pair block F1 = 2 m^2 (1 + abar(2d)^2) to 2.9e-11 (matches SPEC 1.2 / tx_082 with the discrete A = abar(2d)); witness columns F1 = 64 and 128 exactly (matches RUN-REPORT Section 5).

### Lemma 1.1 (reduction: (MI) implies both corners, pairs included)

Let every configuration in the support of a law w satisfy (MI). If E_w[M] = N and E_w[F1] <= (4/3) N (1 + eps), then

    E_w[N_d] / N >= 5/6 - (2/3) eps        and        E_w[n_1] / N >= 2/3 - (4/3) eps.

*Proof.* Per configuration, (MI) reads N_d >= (3M - F1)/2; take expectations (all quantities linear in the law): E[N_d] >= (3N - (4/3)N(1+eps))/2 = N(5/6 - (2/3) eps). For simples: for every integer m >= 1, 1_{m=1} >= 2 - m (equality at m = 1, 2); summing over the zero multiset (pair members are zeros of multiplicity m_p and mult-1 pair members are simple), n_1 >= Sum_z (2 - m_z) = 2 N_d - M; hence E[n_1] >= 2 E[N_d] - N >= (3N - E[F1]) - N >= N(2/3 - (4/3) eps). QED

*Remark.* The 5/6-corner step "N_d >= (3M - S2)/2 when F1 >= S2" of the atom-only proof is here bypassed: (MI) is exactly the inequality the corner consumes, and it is strictly weaker than F1 >= S2 on marks >= 3. This matters: the sharp fractional counterexample of Section 3 kills F1 >= S2 for real marks, and near-tight integer configurations exist for the sharp form (Section 7), so aiming at (MI), which carries the (m-1)(m-2) integrality slack explicitly, is what makes the capacity proofs close.

---

## 2. Kernel toolbox (exact identities, all verified to <= 1e-10)

Let psi(z) := Sum_j u_j e^{-2 pi i j z / N} (entire; the discrete bandwidth-one kernel; on the reals psi(x) = sin(65 pi x/64) / (65 sin(pi x/64))). Let g_k = k * 64/65, k = 0..64, be the psi-zero grid, Delta = 64/65 the grid spacing, and

    abar(x) := psi(ix) = Sum_j u_j cosh(2 pi j x / N) >= 1,        alpha := Sum_j u_j (2 pi j / N)^2 = (pi/64)^2 (65^2 - 1)/3 = 3.392677 (exact).

(T1) **Generating identity.** Sum_s w_s q^s = (Sum_j u_j q^j)^2 for every q != 0 (w = u * u). Hence Sum_s w_s e^{-2 pi i s zeta / N} = psi(zeta)^2 for every complex zeta, and the member expansion

    F1 = Sum_{z, z'} m_z m_{z'} psi(gamma_z - conj(gamma_{z'}))^2 ,

over the zero multiset with complex positions gamma (atoms: gamma = theta; pair members: theta +/- i d), each unordered off-diagonal pair contributing 2 m m' Re psi(x + iy)^2 with x the position offset and y = d_z + d_{z'} the depth sum. Define R_y(x) := Re psi(x + iy)^2; R_0 = psi^2 >= 0.

(T2) **Curvature identity.** abar(x) >= 1 + (alpha/2) x^2 (from cosh t >= 1 + t^2/2), and alpha = Sum_{k=1}^{64} psi'(g_k)^2 (via Sum_{k=1}^{n-1} 1/sin^2(pi k/n) = (n^2 - 1)/3 at n = 65): the total squared slope of the kernel at its zeros EQUALS the quadratic growth rate of the pair diagonal. This equality is why the shallow-pair capacity race (Section 5) is decided by the constant terms, not the slopes.

(T3) **Log-convexity chain.** abar((x + y)/2)^2 <= abar(x) abar(y) (Cauchy-Schwarz on the positive weights); in particular abar(y)^2 <= (1 + abar(2y))/2. Also |psi(x + iy)| <= abar(y) for all real x. Consequently the ratio abar(2y)/abar(y) is nondecreasing in y.

(T4) **Translate identities.** For EVERY complex argument x + iy:

    Sum_{k=0}^{64} psi(x + g_k + iy)^2 = 1            (only s = 0 survives the 65-point sum),
    Sum_{k=0}^{64} |psi(x + g_k + iy)|^2 = abar(2y)   (only j = j' survives).

Verified to 1e-12 at y in {0.1, 0.3, 0.7}. These are the master capacity bounds: the first says the pair-atom coupling field has grid-average exactly its s = 0 value regardless of depth; the second caps the total translate mass of |psi|^2 by the pair's own diagonal growth. In particular, for any x: Sum_k [-R_y(x + g_k)]_+ <= (abar(2y) - 1)/2.

(T5) **Isolated blocks.** Atom mark m: F1-block = m^2. Pair (m, d): F1-block = 2 m^2 (1 + abar(2d)^2) — diagonal 2 m^2 abar(2d)^2 plus the within-pair conjugate coupling 2 m^2 psi(0)^2 = 2 m^2. Against the T-share 6m - 4 the pair block alone carries surplus 2 m^2 abar(2d)^2 + 2 (m-1)(m-2); against the S2-share 2 m^2 it carries 2 m^2 abar(2d)^2. The depth-independent within-pair term 2 m^2 = "the doubling cushion" is what the fractional attack (Section 3) shows is exactly the non-convex resource.

---

## 3. Integrality is necessary: the exact fractional counterexample

### Proposition 3.1

Let c_mu be the vacancy lattice (unit atoms on grid sites g_1..g_64) plus one pair at the hole g_0 = 0 with depth d > 0 and REAL mark mu > 0. Then, exactly,

    F1(c_mu) - S2(c_mu) = 2 mu^2 abar(2d)^2 - 4 mu (abar(d)^2 - 1),

which is NEGATIVE for every 0 < mu < 2 (abar(d)^2 - 1)/abar(2d)^2. For integer marks the same family is safe: at mu = m in Z, using (T3),

    F1 - S2 = 2 m^2 abar(2d)^2 - 4 m (abar(d)^2 - 1) >= 2 m^2 abar(2d)^2 - 2 m (abar(2d) - 1) > 0 .

*Proof.* On the vacancy lattice phi_0(s) = -1 for s != 0 and 64 at s = 0; the pair adds 2 mu cosh(beta s), beta = 2 pi d/N. Expanding Sum_s w_s |c_s|^2 with Sum_s w_s cosh(beta s) = abar(d)^2 and Sum_s w_s cosh(2 beta s) = abar(2d)^2 (both from (T1) at imaginary arguments) gives the display; the numeric check at (d, mu) = (0.25, 0.05) reproduces it to 1e-12 with F1 - S2 = -3.520e-2 (`verify` section X). QED

**Reading.** The linear term is the pair's coupling to the hole (the missing site's positive coupling is absent, leaving a net gain 4 mu (abar(d)^2 - 1) at every depth), while the pair's own cost is quadratic in mu. An adversary with fractional marks takes mu -> 0 and wins at any depth; integer marks force mu >= 1, where the quadratic cost 2 abar(2d)^2 beats the maximal linear gain by the chain abar(d)^2 - 1 <= (abar(2d) - 1)/2. **Every proof below must therefore consume integrality, and does so through exactly two devices: the per-zero slack (m-1)(m-2) >= 0 and the mark-1 floor m^2 >= m inside the cell-capacity counts.** This also explains the LP phenomenology: the gate's LP relaxes nothing about marks (columns are explicit integer configurations), which is why its pricing found no pair column — the channel is closed by integrality, invisible to any convexified analysis.

---

## 4. The exact interference identity

### Proposition 4.1 (the ledger)

For every admissible configuration (any atoms, any pairs), with x_{zz'} the position offsets:

    F1 - T = Sum_a (m_a - 1)(m_a - 2) + 2 Sum_p (m_p - 1)(m_p - 2)          [integrality slack]
           + Sum_{a != a'} m_a m_{a'} psi(x_{aa'})^2                        [atom-atom  >= 0]
           + Sum_p 2 m_p^2 abar(2 d_p)^2                                    [pair diagonals]
           + Sum_p 4 m_p Sum_a m_a R_{d_p}(x_{pa})                          [pair-atom]
           + Sum_{p < q} 4 m_p m_q [ R_{d_p + d_q}(x_{pq}) + R_{|d_p - d_q|}(x_{pq}) ]   [pair-pair]

*Proof.* Expand the member form (T1) and collect: atom diagonals Sum m_a^2 and pair blocks 2 m_p^2 (1 + abar(2 d_p)^2) against T as in (T5); each pair-atom member coupling doubles to 4 m m' R_d (the two members give conjugate psi^2 values); each pair-pair coupling gives the depth-sum and depth-difference terms (four member pairs: (+,+) and (-,-) give R_{d+d'}, (+,-) and (-,+) give R_{|d-d'|}). Verified on 25 random mixed configurations to 2.2e-11 (`verify` section I; the stored `pairchan_verify_out.json` I_identity_maxerr = 2.18e-11 — CORRECTED 2026-08-26 from an unpersisted 5.8e-11). QED

Everything on the right is nonnegative EXCEPT the R-couplings, whose negative parts live only in the dips of R_y (Section 5). The theorem-grade question is exactly: can the dips outrun the pair diagonals plus the integrality slack? The answer, quantitatively, is no — by a factor of ~1.5 at the worst depth, and the doubling cushion 2 m_p^2 (inside 2 m_p^2 abar^2) is never breached at all.

---

## 5. Capacity machinery

Partition the circle into 65 cells of width Delta centered at the grid sites; the peak cell contains the psi-peak, each other cell exactly one kernel zero. For y > 0 define per-cell dip sups and the **capacity curve**

    kappa_k(y) := sup_{cell k} [-R_y]_+ ,        nu(y) := Sum_k kappa_k(y).

nu is the total SIMULTANEOUSLY exploitable dip mass (cells are disjoint, so per-cell sups are jointly attainable by one adversarial atom per cell). Certified values (grid 12001 x-points, refinement-stable to <1e-3; Lipschitz in y bounded by Sum_k sup_cell |(psi^2)'(x+iy)| = 7.5 at y = 0.2, 15.6 at y = 0.4 — so the 0.01-step tables are honest to ~0.1):

    y     : 0.05    0.10    0.159   0.20    0.25    0.318   0.40    0.50    0.70    1.00    1.50     2.00
    nu(y) : 0.0086  0.0364  0.1009  0.1723  0.2977  0.5563  1.0557  2.1003  8.0034  45.619  783.17   14301.2

Shallow behavior: nu(y) = alpha y^2 (1 + o(1)) — the dips sit at the kernel zeros with depths ~ psi'(g_k)^2 y^2 and (T2) sums them to alpha; deep behavior: nu(y) <= 65 abar(y)^2 (pointwise [-R_y]_+ <= |psi(x+iy)|^2 <= abar(y)^2).

### Lemma 5.1 (cell stacking; how much dip mass integer atoms can harvest)

Fix a cell with dip sup kappa and exposure weight m_p (one exposing pair; for several, kappa means the summed weighted dip K of all exposing kernels at this cell). Let atoms with integer marks sit in the cell's dip zone (diameter zw(y), so pairwise crosses >= c_0 := psi(zw)^2 each — psi^2 is decreasing out to the first zero). Then the cell's net harvest (coupling gain minus in-cell atom-atom crosses minus the atoms' own integrality slack) is at most:

* marks <= 2 and 4 m_p K <= 3 c_0: **8 m_p K** (worst case: a single mark-2 atom at the dip; a third unit of mass already pays 4 m_p K - c_0 (2 Lambda - 3) < 0 marginally);
* marks <= 2, general: (Lhat/2) * 8 m_p K, Lhat = argmax_{Lambda in Z} [4 m_p K Lambda - c_0 Lambda(Lambda-2)];
* one atom of mark m >= 3: 4 m_p K m - (m-1)(m-2), maximized over integer m at <= 4 m_p^2 K^2 + 6 m_p K - 2; for m_p K <= 1 this is dominated by the mark-2 value 8 m_p K.

Verified constants: zw(0.159) = 0.293, c_0 = 0.740; zw(0.318) = 0.491, c_0 = 0.408; kappa_max(0.159) = 0.0319, kappa_max(0.318) = 0.1827, kappa_max(0.45) = 0.4880. At the gate's depth family (y <= 0.3183): 4 kappa_max = 0.73 <= 3 c_0 = 1.22 and kappa_max <= 1, so the clean **8 m_p K per cell** rule applies for m_p <= 5 (and m_p >= 4 is separately closed by the crude mass bound in Theorem A's proof). The peak cell has no dip at all for y <= 0.40 (min over the peak cell of R_y = +0.187 at y = 0.40, +0.287 at 0.318 — verified).

### Lemma 5.2 (certified capacity ratios)

Define the single-pair ratio and its stacking-corrected version

    S1(y) := 8 nu(y) / (2 abar(2y)^2),        S1corr(y) := S1(y) * max(1, Lhat(y)/2).

Certified on (0, 2] (0.01-grid to 1.0 plus {1.25, 1.5, 1.75, 2.0}; refinement-stable):

    max_y S1(y) = 0.6823   (attained at y ~= 0.37; S1 -> 0 both shallow and deep);
    S1corr(y) <= 0.921 for y <= 0.45;   S1corr(0.318) = 0.656;   S1corr(0.159) = 0.289.

Deep tail: for y >= 1.0, abar(2y)/abar(y) >= 12.158 (value at y = 1.0; nondecreasing by (T3)).

*Shallow closed form.* On y <= 1/(2 pi) the bound nu(y) <= alpha* y^2 with the certified constant alpha*(1/(2 pi)) = 13.394 (:= Sum_k sup_{cell, t <= y} |psi'|^2 + |psi psi''| at x + it; the harmonic-Taylor bound -R_y(x) <= -psi(x)^2 + 2 Int_0^y (y - t) (|psi'|^2 + |psi psi''|)(x + it) dt, using that Re psi^2(x+it) is harmonic so its t-Taylor remainder is the x-Laplacian) gives the fully quantified shallow inequality

    8 nu(y) <= 8 alpha* y^2 <= 2 (1 + 2 alpha y^2)^2 <= 2 abar(2y)^2       for all y <= 1/(2 pi),

with 1.2% closing margin at the right endpoint (4 * 13.394 * y^2 = 1.357 vs (1 + 2 alpha y^2)^2 = 1.373 at y = 1/(2 pi)). So on the R5 family the capacity inequality needs no curve lookup at all — one Taylor bound, the exact alpha, and one certified finite constant.

---

## 6. The theorems

### Theorem A (single-pair closure)

Let c contain exactly one pair (mark m_p, depth d) and arbitrary atoms (any integer marks, any positions). Then (MI) holds — F1(c) >= 3M(c) - 2N_d(c) — in each of the following regimes:

(i) **d <= 0.45** (w = 2 pi d <= 2.8), unconditionally in the atom background and in m_p. This covers the gate's entire depth family, including both deep probes, with S1corr <= 0.921 (and <= 0.66 on the family itself).

(ii) **d >= 1.0**, for configurations of mass M <= N = 64 (the LP class).

(iii) 0.45 < d < 1.0: not chain-proved; certified numerically (S1 <= 0.6823 throughout; direct zone-stacked sea attacks reach at most 74% of the pair budget — Section 7).

*Proof of (i).* By Proposition 4.1 it suffices to bound the negative part of the pair-atom coupling by the pair diagonal plus the listed nonnegative terms:

    4 m_p Sum_a m_a [-R_d(x_pa)]_+ - (in-cell atom crosses) - (atom slack)  <=  2 m_p^2 abar(2d)^2 .

Split the atoms by cell. Marks <= 2 and single atoms of mark >= 3 with m_p kappa <= 1 harvest at most 8 m_p kappa_k per cell (Lemma 5.1, with the Lhat-correction folded into S1corr for 0.318 < d <= 0.45); atoms of mark m >= 3 in cells where the mark-m optimum exceeds the mark-2 value contribute at most 4 m_p^2 kappa_k^2 + 6 m_p kappa_k - 2 each, and summing that branch over cells costs at most 4 m_p^2 kappa_max nu + 14 m_p nu, which at d <= 0.45 is below 2 m_p^2 abar(2d)^2 for every m_p >= 3 (kappa_max = 0.488, nu = 1.50, abar(0.9)^2 = 8.66: 2 kappa_max nu + 7 nu / m_p <= 1.46 + 3.5 < 8.66). For m_p in {1, 2} the mark-2 branch dominates everywhere in this window and the total harvest is at most (Lhat/2) 8 m_p nu(d); the required inequality is exactly S1corr(d) <= 1, certified <= 0.921 on (0, 0.45] — and on the R5 family it is the CLOSED-FORM shallow inequality of Lemma 5.2, needing only alpha, alpha*, and (T2)-(T3). Different cells are disjoint, in-cell crosses are spent only in their own cell, and atoms outside every dip zone couple nonnegatively, so no resource is double-spent. QED (i)

*Proof of (ii).* Crudely, [-R_d]_+ <= |psi(x + id)|^2 <= abar(d)^2 pointwise (T3), so the coupling is >= -4 m_p (M - 2 m_p) abar(d)^2 >= -4 m_p * 62 * abar(d)^2. It suffices that 248 abar(d)^2 <= 2 abar(2d)^2, i.e. abar(2d)/abar(d) >= sqrt(124) = 11.14, which holds for d >= 1.0 (ratio 12.158, nondecreasing). QED (ii)

*Remark.* The gap (0.45, 1.0) is a deficiency of the cell-capacity bookkeeping only: the uncorrected ratio S1 stays <= 0.68 there, but deep dips are wide enough that the mark-2-per-cell cap needs the zone-resolved profile, which we did not formalize. The LP consequence is unaffected: gate columns have depths <= 0.3183.

### Theorem B (multi-pair closure)

Let c be any admissible configuration (any number of pairs, any atoms, any integer marks).

(i) If every pair depth is <= 0.13 (w <= 0.82): (MI) holds unconditionally.

(ii) If every pair depth is <= 0.156 (w <= 0.98): (MI) holds modulo the cell-crowding refinement (below); its ledger constant is interval-certified, sup_{d,d' <= 0.156} Sgen2 <= 0.98465 < 1 (Session 8, `verify/o1_crowding_interval.py`). On (0.156, 1/(2 pi)] the ledger inequality fails (interval-certified Sgen2(0.159, 0.159) >= 1.01405 > 1): no ledger-grade statement is made there, and coverage is Section 7's attacks plus Theorem D.

*Proof of (i).* Ledger on Proposition 4.1. Three exposure streams against the pair budgets Sum_p 2 m_p^2 abar(2 d_p)^2:

1. *Pair-atom.* As in Theorem A, but the per-cell exposure weight is now K_k = Sum_p m_p kappa_{p,k} (all pairs exposing cell k). The mark-2 cap 8 K_k per cell needs 4 K_infty <= 3 c_0 with K_infty := max_k K_k. Each cell holds at most one mult-1 pair's worth of perturbing mass (stream 3 below), so K_infty <= 2 nu(0.159) = 0.202, and 4 K_infty = 0.81 <= 3 c_0 = 2.22 (c_0 = 0.740 at this window). Summing: total pair-atom harvest <= Sum_p 8 m_p nu(d_p).
2. *Pair-pair.* The coupling negativity of the unordered pair (p, q) is governed by the JOINT kernel Phi(d_p, d_q; x) = R_{d_p + d_q}(x) + R_{|d_p - d_q|}(x) (never by the two parts separately — their dips do not coincide, and capping them separately is what loses the last 20% of window). Charging half to each side and capping perturbers per cell (stream 3): pair p's exposure <= 4 m_p sup_{d' <= Y} nu_joint(d_p, d'), nu_joint := Sum_k sup_cell [-Phi]_+.
3. *Perturber stacking (the crowding cap).* Two mult-1 pairs stacked in one cell have separation <= the joint dip-zone diameter (<= 0.49 at these windows) and hence mutual coupling >= 4 Phi_0 with the floor Phi_0 >= 0.64371 (interval-certified over the full family box, Session 8; the float components 0.2863 + 0.3812 sum to 0.6675, correcting a 0.6665 slip — conservative, so nothing downstream moves). A second in-cell pair is therefore unprofitable as soon as its maximal marginal gain 8 K_infty <= 4 Phi_0, and with the self-consistent bound K_infty <= nu_joint this holds whenever 2 nu_joint <= Phi_0. At Y = 0.13: max nu_joint <= 0.30455 (interval-certified; float 0.3003 at equal depths d = d' = 0.13), and 2 * 0.30455 = 0.60910 < Phi_0 — the one-pair-per-cell cap is SELF-CONSISTENT, now with both sides interval-certified. The ledger condition is then

       Sgen2(d) := [ 8 nu(d) + 4 sup_{d' <= Y} nu_joint(d, d') ] / (2 abar(2d)^2)  <=  1   for all d <= Y,

   certified: sup_d Sgen2 = 0.6852 at Y = 0.13 (binding at d = 0.13). All streams charge disjoint resources (atom crosses in-cell only; pair budgets once). QED (i)

*Proof sketch and status of (ii).* The identical ledger at Y = 0.156 gives sup_d Sgen2 <= 0.98465 < 1 (interval-certified; binding at the corner d = d' = 0.156), PROVIDED the one-pair-per-cell perturber cap is granted there; at Y = 1/(2 pi) the ledger fails outright (interval-certified Sgen2 >= 1.01405 > 1 at d = d' = 0.159, crossing bracket (0.156, 0.158)), so the deepest sliver carries no ledger statement and rests on the attacks plus Theorem D; the self-consistency margin 2 nu_joint <= Phi_0 fails beyond Y = 0.13 (2 * 0.4775 = 0.955 vs a floor of 0.6675 float, 0.64371 certified), because the worst-case assumption "every neighbor cell crowded to cap with every dip simultaneously realized" over-counts — a pair cannot sit in the dip of every neighbor's kernel at once. The missing statement is a single finite-dimensional capacity refinement (the joint per-cell optimization over the kernel family {Phi(d, d'), d, d' <= 1/(2 pi)}), which we certify by direct adversarial computation instead: the targeted crowd+sea attacks at the binding depth d = 0.156 (8-65 pairs, one per cell tranche, plus greedy mark-2 seas of 16-130 atoms at the joint-field minima, both mass-free and mass-64) never bring F1 - T below +17.4 — see Section 7 — versus a floor requirement of 0. We therefore state (ii) as proved modulo one certified constant, and flag it in Section 9. QED (sketch)

### Theorem C (equal-depth pair-only, exact, all depths)

If c consists only of pairs, all at one common depth d (any positions, any integer multiplicities), then

    F1 = 2 Sum_s w_s |phi(s)|^2 + 2 Sum_s w_s cosh(4 pi s d / N) |phi(s)|^2 >= S2 + 2 Sum_p m_p^2 ,

where phi(s) = Sum_p m_p e^{-2 pi i s theta_p / N}. In particular (MI) holds with a full doubling-cushion surplus at every depth.

*Proof.* c_s = 2 cosh(2 pi s d/N) phi(s) and 4 cosh^2 = 2 + 2 cosh(double); the first term is twice the atom-only Frobenius of the position multiset, >= 2 Sum m_p^2 by diagonal positivity (grid Parseval logic: psi^2 crosses >= 0); the second is termwise >= 2 Sum_s w_s |phi|^2 >= 2 Sum m_p^2 as well — keep the weaker floor stated. QED

*Remark.* This kills the "equal-depth pair crowd" channel — the a priori worst case for pair-pair interference (half-gap phased deep twins etc.) — exactly and at every depth. The multi-pair difficulty is genuinely the mixed-depth + atom-sea combination, which is what Theorem B's ledger prices.

### Theorem D (unconditional spectral backstop; all depths, all configurations)

For EVERY admissible configuration: N_d >= (4/9)(3M - F1). Hence for any law with mass N and E[F1] <= (4/3)N(1 + eps):

    E[N_d]/N >= (8/9)(5/6 - (2/3) eps) = 20/27 - (16/27) eps .

*Proof.* Let B be the Hermitian frequency matrix B[j, j'] = sqrt(u_j u_{j'}) c_{j - j'} (65 x 65; the alias-free compression of the gate's own spectral assembly). Exactly: tr B = c_0 Sum u_j = M and tr B^2 = Sum_{j,j'} u_j u_{j'} |c_{j-j'}|^2 = F1 (verified to 1e-10 on random pair configurations, `verify` section D). B decomposes as Sum_atoms m_a v_a v_a^dagger + Sum_pairs B_p with each atom block PSD of rank 1 and each pair block of signature (1,1) (the exact block law, eigenvalues m(1 +/- abar(2d))); by subadditivity of positive inertia, n_+(B) <= #atoms + #pairs <= N_d. For every real t: 3t - t^2 <= (9/4) 1_{t > 0}. Summing over the spectrum: 3M - F1 = Sum_i (3 lambda_i - lambda_i^2) <= (9/4) n_+(B) <= (9/4) N_d. (Numerically: n_+ <= #atoms + #pairs held with equality-or-less on all 12 random configurations, and the bound held with slack.) QED

*Remark.* The 9/4 (rather than 2) is the price of a purely spectral argument: the function 3t - t^2 exceeds 2 on (1, 2) with max 9/4 at t = 3/2, and no spectral-only bound can exclude eigenvalue mass there. This is the same structural reason the parent's inertia route (tx_082: n_on >= 4 tr - 2N - F, the 2/3-distinct bound) cannot reach 5/6 — but it is depth-uniform, mark-uniform, and interference-proof, which is exactly what a backstop must be.

---

## 7. The numerical record (adversarial searches; all with the independent assembly)

Scripts: `verify/pairchan_attack.py` (families A-F), `verify/pairchan_stress.py` (G1-G5), `verify/pairchan_identity.py` (I1-I4), `verify/pairchan_crowd.py` (crowd+sea, cap constants), `verify/pairchan_windows.py`, `verify/pairchan_joint.py`, `verify/pairchan_constants.py`, consolidated re-run `verify/pairchan_verify_all.py` -> `pairchan_verify_out.json`. Optimizers: Nelder-Mead multi-start over continuous positions and log-depths, integer marks enumerated; seeds fixed in-file. Roughly 10^4 optimized configurations total.

**Global minimum of F1 - T: +2.000000, never lower, across every family.** More precisely the minimum of F1 - T - Sum_p 2(2 m_p^2 - 3 m_p + 2) is 0.000000, attained only at depth -> 0 on the grid (pairs degenerate to doubles). Highlights (values = minima found):

| family | description | min F1 - T |
|---|---|---|
| A | vacancy lattice + 1 pair (position, depth free), m = 1/2/3/4 | 2.000 / 8.000 / 22.000 / 44.000 (= 2(2m^2-3m+2) exactly) |
| B | multi-vacancy lattices + k <= 3 pairs at/near holes | 2k m-scaled floors, never below |
| C | dip attacks: pair + atoms at ALL dips of R_d, d = 0.1..1.2 | 2.063 (d = 0.1, mark-2 dips) |
| D | pair crowds, k <= 6, no atoms, free positions/depths | 4.000 (k=2) .. 12.5 (k=6): = 2k floor |
| E | 60 random mixed configs, local-opt | 2.000 |
| F | anti-phased two-class probes (half-circle offsets) | 4.000 |
| G1 | pair chains sharing joint dip fields, k <= 4, d <= 0.5, mark-2 seas | sharp margin >= +0.0295 (d=0.1, k=2) |
| G2 | free chains, 8 free atoms, k <= 3 | sharp margin = 0.0000 only at d -> 0 |
| G3 | half-gap deep twins (the frustration channel), d <= 1.8 | >= +15.5 |
| G5 | 150 random deep/high-mark stress | >= +7.0 |
| crowd | 8/16/32/65 pairs at d = 0.156 + greedy mark-2 seas (16..130 atoms), incl. mass-64 | >= +17.40 |
| deep sea | single pair d = 0.45..1.0 + zone-stacked mark-2 seas up to 120 atoms | >= +8.25 (d=0.45); attacks capture <= 74% of budget |
| I4 | depth-resolved single-pair worst case (free atoms + vacancy backgrounds) | 2.06 (d=.05), 2.18 (.10), 2.50 (.159), 3.53 (.25), 5.18 (.318), 23.0 (.5), 475 (.8) — monotone in d |

Three structural facts the searches establish beyond the theorems: (a) the binding adversary is always shallow (the sharp floor is approached only as d -> 0); (b) coordinated dip attacks can consume nearly the entire depth-dependent excess 2m^2(abar(2d)^2 - 1) (to within 3% at d = 0.1) but never any of the doubling cushion 2m^2 — exactly the split the capacity lemmas predict; (c) crowding, frustration (half-gap phasing), depth-splitting, anti-phasing, high marks, and mass-free scaling all fail by wide margins.

**Sharp conjecture** (all depths, all configurations): F1 >= Sum_a (3 m_a - 2) + 4 Sum_p m_p^2, with equality iff the flattened configuration is a marks-{1,2} grid configuration and all depths are 0+. Status: supported by every search above; the near-tight witnesses (G1: +0.03) show any proof must be capacity-sharp, which is why the theorems above target (MI) (floor headroom 2 per pair) instead.

---

## 8. Consequences for the no-go paper and the gate record

1. **Remark 2.6 of `theorems.md` can be upgraded.** The model-level corner theorem (T2 there) extends verbatim from the atom-only class to: (a) all single-pair columns with w <= 2.8 — which includes every pair column the gate's dictionary actually contains, the deep probes w in {1.5, 2} included; (b) all multi-pair columns with depths w <= 0.82 unconditionally, and w <= 0.98 modulo the crowding cap (ledger constant interval-certified); columns with a pair depth in the deepest ~2% of the family (w in (0.98, 1]) rest on the numerical record plus the 8/9 backstop; (c) equal-depth pair-only columns at every depth. Both benchmarks (N_d and simple-fraction) extend, via Lemma 1.1. Suggested wording for the paper: "the corner is proved for configurations with pairs through 98% of the admissible depth family (single-pair: all of it); for configurations with two or more pairs in depths w in (0.82, 0.98] the crowding cap's ledger constant is certified by interval arithmetic; for two or more pairs in the deepest 2% (w in (0.98, 1]) the coverage is adversarial-numerical; all remaining regimes are floored at 8/9 of the corner unconditionally."
2. **The channel could only ever have produced a bite, and it produces none** (confirming AUDIT Section 5 finding 4's direction): the fractional counterexample shows where the bite would have lived (real marks), and integrality is precisely what the true zero multiset has (SPEC 3.2 necessity list). The gate's pricing null result on pair columns is now explained, not just observed.
3. **The deep-pair regime beyond the family** (d > 0.45 multi-pair, or mass-unbounded crowds) is not LP-relevant (columns have mass N and the R5 family caps depths; deeper objects are garnish, priced by the ladder/fuzz rows — SPEC 4.2's 2 sqrt2 sqrt(C_led eps) cap), but Theorem D covers even those unconditionally at 8/9 strength.
4. **Lean note:** Theorem D is formalization-friendly (finite Hermitian matrix, inertia subadditivity, a scalar inequality); Proposition 4.1 and the grid identities (T1)/(T4) are algebraic on the grid and PairCeiling-shaped. The capacity curves are where interval arithmetic would enter; the closed-form shallow route of Lemma 5.2 (one Taylor bound + alpha exact + one finite constant alpha*) is the recommended formalization path for the R5-family statement.

## 9. Honest open remainder

* (O1) [EXECUTED WITH CORRECTION, Session 8 2026-08-26 — `verify/o1_crowding_interval.py`] The stated hardening route was run. Outcome: (a) the ledger constant is interval-certified on (0, 0.156]^2: sup Sgen2 <= 0.98465 < 1; (b) the Session-7 full-family ratio 0.9775 was a 0.004-grid artifact — on (0.156, 1/(2 pi)] the ledger inequality FAILS (interval-certified Sgen2 >= 1.01405 > 1 at d = d' = 0.159; crossing bracket (0.156, 0.158)); coverage there is the attacks (re-run at 0.158/0.159: >= +17.47) plus Theorem D. (c) Still open on (0.13, 0.156]: the one-pair-per-cell cap itself (granted, not chain-proved; its Y = 0.13 self-consistency is now interval-certified on both sides).
* (O2) Theorem A's window (0.45, 1.0) at unrestricted mass, and multi-pair beyond the R5 family: covered by numerics + Theorem D only. Not needed for any gate/LP statement.
* (O3) The sharp conjecture (Section 7). Its truth would make every pair strictly wasteful for the adversary (full 4m^2 flattened cost), turning the no-go's pair discussion into one line; near-tight configurations (+0.03) mean the constant-chasing is genuinely hard.
* (O4) N-uniformity: all constants certified at N = 64 (the gate's decision geometry; the structure — translate identities, curvature identity, log-convexity — is N-generic and the continuum analogs are classical, but the certified curves were not re-run at N = 128). The N = 128 re-run is mechanical (`pairchan_verify_all.py` is N-parametric up to the grid constants). [EXECUTED, Session 8 — `verify/n128_rerun.py`. All identities and inequalities reproduce at N = 128 (control leg reproduces the stored N = 64 record to <= 2e-15). Constant drifts <= ~2.5% toward continuum values (alpha 3.3927 -> 3.3413; capped-0.156 ledger constant 0.97746 -> 0.96329). Two honest N-dependences: Theorem A(ii)'s deep threshold is d >= 1.1 at N = 128 (ratio target sqrt(2(N-2))); the near-endpoint ledger failure exists at N = 128 too, on a smaller sliver (crossing in (0.159, 0.1591)).]
* (O5) All statements are for the flat window at lambda = 1, matching the gate's primary decision configuration; the MT-cosine lambda = 1 window (AUDIT major-1's residual regime) changes the kernel zero set and none of this note's constants transfer without recomputation.

## 10. Files

* This note: `results/a4-no-go/pair-channel.md`.
* Consolidated verification (re-runnable, ~3 min): `results/a4-no-go/verify/pairchan_verify_all.py` -> `pairchan_verify_out.json` (all identity checks, spectral-backstop checks, capacity curves, certified windows).
* Search/attack scripts (as run this session, seeds fixed): `pairchan_core.py` (model + basic suite), `pairchan_attack.py`, `pairchan_stress.py`, `pairchan_identity.py`, `pairchan_crowd.py`, `pairchan_joint.py`, `pairchan_windows.py`, `pairchan_constants.py` — all in `results/a4-no-go/verify/`.
* Key certified constants (also in the JSON): alpha = 3.392677 (exact closed form); max S1 = 0.6823; S1corr(0.45) = 0.9205; Sgen2 sup = 0.6852 at Y = 0.13 (interval-certified <= 0.70458) and 0.97746 at Y = 0.156 (grid; interval-certified <= 0.98465 on the continuum); at Y = 1/(2 pi) the sup exceeds 1 (interval-certified >= 1.01405 at d = 0.159); Phi_0 >= 0.64371 (interval-certified; float 0.6675, correcting the 0.6665 slip); nu-table of Section 5; abar table: abar(0.318) = 1.1809, abar(0.6366) = 1.8439, abar(2)/abar(1) = 12.158.
