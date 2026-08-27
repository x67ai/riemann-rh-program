# A4 M2 DECISION GATE — FULL SPECIFICATION (corrected per adjudication repair R5)

**Program:** RH program, direction A4 (merged A2+A4 cubic-certificate direction, adjudicated survives-with-repairs 5.5, binding).
**Contract:** repairs R5 (gate re-specification) and R7 (fallback row system, primary) of `results/adjudication-A4.json`; direction file `directions/A4-lindelof-lock.md` (Current frontier: ACTION ONE).
**Role of this document:** the formulator's complete mathematical specification of the gate LP — every object, row, constant, discretization, and the exact decision criterion — plus the implementation plan. The implementer works from this file alone.
**Status of every load-bearing number:** re-derived or computed in this session (standing order 5); verification code and outputs in `verify/` (`verify_constants.py`, `verify_out.json`). Recalled-but-unverified items are quarantined in §10 (Flags).
**Date:** 2026-08-26.

---

## 0. What the gate decides, in one paragraph

The parent method's two-moment certificate is provably exhausted (`lemmaR_tight`): with flat window at bandwidth 1, the configuration LP over {trace = N, Frobenius = (4/3)N, integer multiplicities, off-line pairs} has min N_d/N = 5/6, attained by the extremal configuration 2/3 simple + 1/6 on-line doubles. A4 proposes to add, at a second bandwidth lambda' = 1/2+ (theta < 1 strict, per R4), the unconditional third-trace equality and the repaired spectral-capacity rows. The gate asks: **does the joint system raise min N_d/N above 5/6 by a delta_0 > 0 that survives the corrected adversary class (marks up to W, depth-parametrized shallow pairs, clustered 3-point positional freedom, garnish capacity), or does an admissible adversary family absorb every new row at N_d = 5/6 + o(1)?** Either branch is a deliverable: bite -> the direction proceeds to the R2 bridge; absorption -> the publishable sharpened no-go "the bandwidth-one ceiling is robust under Rudnick–Sarnak-range cubic augmentation with capacity control," with the absorbing family as the witness. The gate runs BEFORE any bridge investment.

Honest prior, pre-registered (§8): the referee priced P(bite) <= 50%; the designer's own 2 = 2 admission is the identity G(1) = 0 of §2.4; and the window-optimized margin 2*m2 - m3 is NEGATIVE at lambda' = 1/2 for every window in the §2.5 family (verified). A bite, if it occurs, must come from the sign-split/ladder pricing of positional interference, not from the §7.3-style moment margin.

---

## 1. Objects and units

### 1.1 Window, kernel, and the master trace formula

Fix a window profile v >= 0 on [-1/2, 1/2] (the scale-free profile of phi^2; the parent's formalized taper class is C^3 — R7). Define the **normalized sampling kernel** at bandwidth lambda (positions x in mean-gap units, mean zero spacing = 1):

    psi_lambda(x) = ( Integral_{-1/2}^{1/2} v(sigma) e^{2 pi i lambda sigma x} d sigma ) / Integral v ,

an entire function of x with psi(0) = 1 and Fourier support [-lambda/2, lambda/2] (in Montgomery alpha-units). For the flat window v = 1: psi_lambda(x) = sinc(pi lambda x) = sin(pi lambda x)/(pi lambda x).

**Derivation (recorded; this is the paper's Poisson sampling identity in normalized units).** With windows tau_k at critical spacing 2 pi / L and Phi = (phi^2)^, the identity Sum_k phi-hat(tau - tau_k) phi-hat(tau' - tau_k) = L Phi(tau - tau') holds aliasing-free; in units G-hat = G/(a L^2), a = L^{-1} Integral phi^2, and mean-gap position units this becomes: for any finite configuration of points gamma_z (COMPLEX allowed, gamma = x + i w/lambda-units for off-line zeros) with multiplicities m_z,

    tr G-hat_lambda^k = Sum_{z_1, ..., z_k} ( Prod_j m_{z_j} ) psi_lambda(gamma_{z_1}-gamma_{z_2}) psi_lambda(gamma_{z_2}-gamma_{z_3}) ... psi_lambda(gamma_{z_k}-gamma_{z_1}).

This single formula generates every trace row on both sides (null budgets and configuration demands), including all clustering cross-terms and all depth effects; no isolated-block idealization enters the gate anywhere.

### 1.2 The exact off-line pair block (Prop 4.1, true spectrum — re-derived)

An off-line pair {rho, 1 - rho-bar} at depth delta (in the gamma-plane) with multiplicity m has evaluation vector x_k = phi-hat(gamma + i delta - tau_k); by the sampling identity (derived from scratch this session, verified against tx_082 verbatim):

    x^T x = L^2 a       (real, DEPTH-INDEPENDENT),
    |x|^2 = L^2 a * A(delta),   A(delta) = Integral phi^2(s) cosh(2 delta s) ds / Integral phi^2 >= 1.

Writing x = p + i q (real/imaginary parts), the block is M = m (x x^T + conj) = 2m (p p^T - q q^T), and x^T x real forces <p, q> = 0 exactly. Hence the **exact block spectrum in normalized units**:

    eigenvalues  m (1 + A)  and  m (1 - A);   trace 2m;  Frobenius 2 m^2 (1 + A^2);  cubic 2 m^3 (1 + 3 A^2).

In dimensionless depth w = delta * L' (so the R5 family u in [0, 1/L'] is w in [0,1]):

    A(w) = Integral v(sigma) cosh(2 w sigma) d sigma / Integral v;   flat window: A(w) = sinh(w)/w.
    Flat values: A(0)=1, A(1/8)=1.00261, A(1/4)=1.01045, A(1/2)=1.04219, A(3/4)=1.09642, A(1)=1.17520, A(2)=1.81343.

Verified by direct matrix assembly (verify V3): eigenvalues match m(1 +/- A(w)) to the window-truncation error 2e-3, and are **independent of the pair's position relative to the window grid** (the S = 0 orthogonality above; the adjudication computation-8 phase model, which gave (+1,-1) at u L = 1, is a heuristic gauge and is superseded by this exact law — its qualitative conclusions stand, its depth-decay of the cubic charge does not).

**Consequences fixed by this law (all verified, verify V6):**
* Block continuity: w -> 0 gives spectrum (+2m, -0m), cubic charge -> 8 m^3: shallow pairs mimic doubles in every row (adjudication upheld K2-major-5/referee-minor-3). The gate's pair family INCLUDES w = 0+.
* Per-zero isolated-block identity: with F = per-zero Frobenius charge and c = per-zero cubic charge,
      on-line atom of multiplicity m:  c = 3F - 2 + (m-1)(m-2);
      off-line pair of ANY depth:      c = 3F - 2  exactly.
  So on isolated blocks the signed cubic row measures exactly the second integrality level Sum m(m-1)(m-2) and is BLIND to pairs at every depth; pairs and doubles lie on the same affine plane c = 3F - 2. **All discriminating power of the cubic row therefore lives in (i) marks >= 3 and (ii) the clustering cross-terms of the master formula.** This sharpens R6 (the row is a nonlinear reading of bandwidth-one pair data) into a precise structural statement, and it is why the corrected gate — clustered null, positional freedom — is the only honest one: an isolated-block gate would return a tautological answer along the affine plane.

### 1.3 The two Gram readings (joint two-bandwidth structure)

One configuration, two matrices (A2's fatal is structurally excluded: no cross-window products anywhere):
* lambda = 1 reading: kernel psi_1, budgets tr = N, tr^2 = m2(1; v1) N.
* lambda' = 1/2 reading (primary; exploratory 0.55/0.60/0.65): kernel psi_{lambda'}, budgets tr = N, tr^2 = kappa(lambda') N, tr^3 = c3(lambda') N, plus ladder/fuzz.

### 1.4 Finite-circle geometry (the LP's discretization)

Period N (zeros per period; primary N = 64, confirmation N = 128) on the circle of circumference N. Configurations = N-periodic marked multisets. Fourier route for all traces: with harmonics u_j = psi-hat samples normalized so Sum_j u_j = 1 (DFT-consistent assembly; support |j| <= lambda N / 2),

    c_j = Sum_z m_z e^{-2 pi i j theta_z / N}   (for a pair at theta +/- i w-depth: 2 m e^{-2 pi i j theta / N} cosh(2 pi j w-tilde / N)),
    tr G-hat   = N,
    tr G-hat^2 = Sum_{j1,j2} u_{j1} u_{j2} |c_{j1+j2}|^2,
    tr G-hat^3 = Sum_{k1,k2} U3(k1,k2) c_{k1} c_{k2} c_{-k1-k2},  U3(k1,k2) = Sum_j u_{j+k1} u_{j+k1+k2} u_j.

Cost per configuration: O((lambda N)^2) after precomputing U3 — trivial at N = 64/128. Eigenvalue data (ladder counts n(V), the inertia split Sum_+/Sum_-, n_-) from dense eigh of the d' x d' assembled matrix, d' = lambda N. The null and every dictionary column are assembled by the SAME code path, so finite-geometry effects cancel in budget-vs-demand comparisons.

---

## 2. Null model: the clustered sine-process budgets

### 2.1 Analytic budget formulas (derived this session; the MC's convergence anchors)

For the sine process (determinantal, S(x) = sin(pi x)/(pi x); rho_2 = 1 - S^2; rho_3 = 1 - S_12^2 - S_13^2 - S_23^2 + 2 S_12 S_13 S_23), with u = psi-hat_lambda:

    m2(lambda; v) = 1 + Integral u^2 - Integral t (u*u),                      t(alpha) = (1-|alpha|)_+,
    m3(lambda; v) = 1 + 3 [ Integral u^2 - Integral t (u*u) ] + T3,
    T3 = Integral u^3 - 3 Integral (t*u) u^2 + 2 Integral (b*u)^3,           b = 1_{[-1/2,1/2]},

(all integrals over alpha; * = convolution; integrands compactly supported in |alpha| <= (1+lambda)/2). **Closed forms, flat window (derived by hand, confirmed by quadrature to <= 3e-4 and by CUE MC):**

    m2(lambda) = 1/lambda + lambda/3        [= the paper's unconditional prime-side kappa(lambda) EXACTLY, at every lambda <= 1]
    m3(lambda) = 1 + 1/lambda^2.

Anchor values: m2(1) = 4/3, m3(1) = 2 (the recalled sine moments — now VERIFIED, two independent routes each); kappa(1/2) = 13/6 = 2.16667; m3(1/2) = 5. The identity m2 = kappa at second order is the verification that the sine-process null equals the unconditional prime-side budget within the accessible band; the same identification at third order is Rudnick–Sarnak-range GUE n-level correlations (flag F2 of §10 for the polylog-window uniformity).

Additional cross-checks obtained free (verify V1/V2): min over the cos-window family of m2(1; v) = 1.327499 at vartheta = 1/sqrt(2), matching the Montgomery–Taylor constant 1/c* = 1.3274993; and 2 m2 - m3 = 0.685244 at v = cos(1.6 sigma), lambda = 1, matching v5 §7.3's recalled 0.68524 exactly.

### 2.2 The budget columns of the LP

* Density row (both bandwidths): tr = N exactly (Riemann–von Mangoldt; in the LP: total mark mass per period = N).
* lambda = 1 Frobenius row: E_w[F1(c)] in m2(1; v1) N [1 -/+ eps_F1].
* lambda' Frobenius row: E_w[F'(c)] in kappa(lambda') N [1 -/+ eps_F].
* lambda' signed cubic row: E_w[C'(c)] in c3(lambda') N [1 -/+ eps_3] -/+ Gamma_fuzz N (fuzz, §4.3), with the budget column
      c3(lambda') := m3(lambda'; v') as sampled/derived above.
  Decomposition fixed for the record (R6-honest): c3 = [1, the atom diagonal] + [3 Integral (1-S^2) psi^2, the two-point/band term = bandwidth-one pair data] + [T3, the three-point term determined by RS-range GUE 3-level correlations] + [O(1) ppp resonance, = 2.315762 recomputed (verify V7), an ADDITIVE O(1) on tr^3, i.e. O(1/N) per zero — folded into eps_3]. Flat lambda' = 1/2: 5 = 1 + 3.5 + 0.5.
* Budget intervals: centered at the matched-geometry MC values (§2.3), with half-width = 2 SE + |analytic - MC| (finite-size envelope); the analytic values above are the convergence anchors — if the MC at largest n deviates from them by > 3 SE the harness is bugged (halt condition).

### 2.3 Sampler and convergence justification

CUE eigenangles (exact circular geometry, no segment cutting): n x n Haar unitary via QR-with-phase-fix of complex Ginibre; angles unfolded to circumference n. This IS an n-periodic sine-process approximant; at n -> infinity its k-level correlations converge to the sine process at rate O(1/n) in the smoothed statistics used here.
* Budget grids: n in {64, 128, 512, 1024, 2048} — the first two matched to the LP geometry, the rest for the asymptote; R adaptive until SE(m3-hat) <= 0.005 * m3 (cap R = 5000 per (n, lambda', v)).
* Convergence justification (mandated by R5): (i) the fitted 1/n trend must extrapolate to the analytic closed forms within 2 SE (already demonstrated at n = 256/512: m2(1/2): 2.1519 -> 2.1602 -> 13/6; m3(1/2): 4.935 -> 4.975 -> 5); (ii) batch-means SE with jackknife check; (iii) both matched-n and asymptotic budget variants are run through the LP; delta_0 is reported under both (they must agree in sign for a verdict).
* Occupancy check (referee major-2 made quantitative): at lambda' = 1/2 the window width is 2 mean gaps; the null's cross-term shares are Frobenius 7/6 out of 13/6 (54%) and cubic 4 out of 5 (80%) — the discrimination signal rides on a cross-term-dominated background, which is exactly why budgets are sampled clustered and never from isolated blocks.

### 2.4 The doubles-plane diagnostic G(lambda; v)

Define G := m3 - (3 m2 - 2) (the budget's excess over the isolated-block doubles/pairs plane of §1.2). Flat window: G(lambda) = 3 + 1/lambda^2 - 3/lambda - lambda; G(1) = 0 — **the designer's "2 = 2" admission is precisely this identity** — and G(1/2) = +1/2. At lambda = 1 with cos windows, G < 0 (e.g. -0.0133 at vartheta = 0.8): the window-optimized §7.3 gain is the statement G < 0. At lambda' = 1/2, G > +0.49 for the whole window family: the null budget sits strictly ABOVE the doubles plane, i.e. matching the cubic budget requires positional cubic cross-terms, and the gate's crux is whether a doubles-saturated adversary can supply them within the Frobenius rows (quantified targets, flat, lambda' = 1/2: the 5/6-extremal must realize cross-Frobenius X2' = 13/6 - 4/3 = 5/6 per zero at lambda' while X2(1) ~ 0 at lambda = 1, and cross-cubic X3' = 5 - 2 = 3 per zero; the all-simple null realizes (7/6, 4) with X2(1) = 1/3).

### 2.5 Window family (certificate-side degree of freedom)

v in {flat (primary); cos(2 vartheta sigma), vartheta in {1/sqrt 2, 0.8}} at each bandwidth independently (v1 at lambda = 1, v' at lambda'). Primary decision configuration: v1 = v' = flat (this is what pegs the baseline at exactly 5/6, §5.1). Window scans are secondary: they change both budgets and baseline (Theorem-D effect: at v1 = MT-window the no-cubic baseline is already 0.83625 > 5/6), so all window-scan results are reported as the marginal value of the cubic block (§5.2), never as raw N_d.

---

## 3. Adversary class

### 3.1 Configuration space (explicit; realizability by construction)

A dictionary column is an explicit N-periodic marked configuration:
* on-line atoms: positions theta_i in [0, N) (continuous, optimizer-chosen; minimum separation for distinct atoms = 1/8 mean gap, a discretization parameter halved in refinement checks), integer marks m_i in {1, ..., W};
* off-line pairs: positions theta plus depth w in the grid {0+, 1/8, 1/4, 1/2, 3/4, 1} (R5's u in [0, 1/L']; "0+" = depth 1/64, distinct from an on-line double for N_d), pair multiplicity m <= floor(W/2) v 1;
* mass constraint per period: Sum_atoms m_i + 2 Sum_pairs m_p = N (density = Riemann–von Mangoldt);
* N_d(c) = #atoms + 2 #pairs (pairs are two distinct zeros; only on-line multiples reduce N_d).

The LP variable is a probability law w_c >= 0, Sum w_c = 1 over the dictionary; every row is E_w[row(c)]; the objective is E_w[N_d(c)]/N.

### 3.2 Realizability: exactly what is imposed, and why it is necessary and sufficient

Imposed: **(a)** every column is an explicit finite marked multiset (not a correlation datum); **(b)** integer multiplicities >= 1; **(c)** off-line points occur only in conjugate pairs {rho, 1 - rho-bar} with a common depth (functional-equation symmetry); **(d)** total mass N per period (density); **(e)** mixtures (laws) of explicit configurations.
NOT imposed: any local statistic beyond what the rows enforce (no sine-likeness, no minimum gap beyond the discretization floor, no correlation positivity axioms).

*Necessity.* The gate's absorption branch asserts an adversary WORLD consistent with everything the row-theorems know. If the adversary were allowed to specify aggregated spectral or correlation data directly (Tier A of §4.4), it could claim moment data realized by NO point configuration (the moment problem for point processes is not exhausted by any finite row list — e.g. unconstrained "cross-term variables" can sit outside the convex hull of realizable (X2, X3) pairs), and an "absorption" so produced would be vacuous — this is R5's honesty requirement in one direction. Constraints (b)-(d) are necessary because the true zero multiset provably has them (integrality, functional equation, RvM density), and dropping any of them hands the adversary provably-impossible worlds (e.g. fractional marks lower N_d demand below what integrality permits: the 5/6 baseline itself would be false).
*Sufficiency (at the LP's level of abstraction).* Conversely, nothing further may be imposed: every row of §4 is a theorem valid for an ARBITRARY configuration satisfying (b)-(d) — the trace identities are linear algebra plus the sampling identity; the budgets are the unconditional prime-side equalities; the ladder is Theorem 1(ii)-repaired (contingent on R2, §10 F4); inertia rows are Sylvester. Hence any explicit configuration meeting (b)-(d) and all rows is a world the certificate must defeat, and any additional constraint (e.g. imposing GUE 3-level correlations pointwise rather than through the c3 row) would smuggle in exactly the unproven correlation knowledge whose absence the gate is designed to respect — killing its meaning in the other direction (an over-constrained "bite"). The periodicity and the finite depth/mark grids are discretizations, not constraints: they are refined (N 64 -> 128, W-scan, depth-grid halving) and the verdict must be stable under refinement (§5.4).

### 3.3 Dictionary seeds and column generation

Seeds (structured families):
1. the 5/6-extremal: 2/3 simple + 1/6 doubles, positions (i) even-spaced (lattice), (ii) sine-sampled, (iii) optimizer-perturbed;
2. depth family: seed 1 with doubles -> pairs at each grid depth (block continuity probe);
3. cluster motifs: 2-4 atoms with mark patterns from the alphabet packed within one lambda'-window (occupancy exploitation), tiled periodically at varying local density;
4. finite sprinkling (K2's adversary): n = ceil(eps N / m^2) atoms of mark m = W plus mass-balancing simples, eps in {1/4, 1/2, 1};
5. garnish surrogates: deep-pair insertions at w in {1.5, 2} (heights beyond the R5 family, priced by ladder rows explicitly rather than by fuzz — checks fuzz-row consistency);
6. null-like columns: CUE-sampled all-simple configurations (feasibility anchors);
7. random marked perturbations of 1-6.

Column generation: master LP (HiGHS, float; final basis re-verified in rational arithmetic on the active rows) alternates with a pricing search: minimize the reduced cost over configuration space by multi-start local optimization in positions (analytic gradients of all kernel sums; depths and marks by discrete neighborhood moves). Stop when S = 200 restarts produce no column with reduced cost < -10^-6. The absorption branch REQUIRES an explicit optimal law (the witness); the bite branch reports "no improving column found" with the restart budget — stated honestly as heuristic adversary-optimality, upgradeable to a certified bound only by the (downstream, branch-dependent) formalization pass.

---

## 4. Row system

### 4.1 Tier-1 rows (THE decision system; primary configuration flat/flat, lambda' = 1/2, N = 64)

lambda = 1 side (the N_d-relevant rows of the parent certificate — the data class of lemmaR_tight, which pegs the no-cubic baseline at exactly 5/6):
  (R-1) mass/density: Sum_c w_c [mark mass per period](c) = N   [exact, by construction];
  (R-2) Frobenius at lambda = 1: E_w[F1] in (4/3) N (1 -/+ eps_F1);
  (R-3) integrality and pair structure: by construction (§3.2 (b)-(c));
  (R-4) objective: minimize E_w[N_d]/N.

lambda' side (the R7 fallback system, primary, in explicit form):
  (R-5) Frobenius: E_w[F'] in kappa(1/2) N (1 -/+ eps_F) = (13/6) N (1 -/+ eps_F);
  (R-6) signed cubic with capacity correction: |E_w[C'] - c3(1/2) N| <= eps_3 N + Gamma_fuzz N, c3(1/2) = 5 (flat);
  (R-7) all-V count ladder: E_w[n(V; c)] <= C_led N V^{-4} for every V in the grid {2, 3, 4, 6, 8, 12, 16}  [NOT a scalar tail row at divergent V0 — R1];
  (R-8) inertia: n_-(c) <= p(c) per column [automatic from Sylvester on explicit assembly; kept as a per-column assertion check];
  (R-9) Frobenius split, power-mean, Hoelder-with-o(N): automatically satisfied by explicit spectra (computed per column from eigh); retained as *assertion checks* per column and as literal rows only in Tier A (§4.4). This is R7's system made primary: in the explicit gate the linear-algebra-true rows cannot be violated, so their entire content is enforced, leak-free, by construction.

Notes. (i) The trace row at lambda' coincides with (R-1) (both count mark mass). (ii) The null (CUE all-simple columns) must be feasible for (R-7): the measured null exceedance defines the consistency floor C_led^min := max_V V^4 n_null(V)/N; the C_led scan starts at max(10, 2 C_led^min). (iii) eps-knobs: eps_F1, eps_F, eps_3 in {0.02, 0.05, 0.10} (the o(N)-precision of the consumed equalities at honest finite-T bookkeeping is O(1/L) ~ 0.02-0.05); delta_0 is reported as a function of the knob vector.

### 4.2 Garnish-capacity fuzz row — constant re-derived and corrected

Setting (adjudication squeeze, §(b) computations 4-5): unmodeled spectral mass at heights h >= C_abs may shift the cubic row; it is constrained by the all-V ladder n([h, infinity)) <= C_led N h^{-4} and by the Frobenius slack Sum n_h h^2 <= eps_g N. Sharp capacity (continuum LP, exact optimum):

    max |Delta cubic| / N  =  2 sqrt(2) * sqrt(C_led * eps_g)   ~= 2.828 sqrt(C_led eps_g),

attained by the count profile n([h, infinity)) = min(C_led a^{-4}, C_led h^{-4}), a = sqrt(2 C_led / eps_g) (mass spread from a/1 down the ladder boundary; derivation in §9.3). **Correction to the adjudication's bookkeeping:** the naive point-mass-plus-tail extremal (which gives 5/sqrt 3 ~ 2.887, and the adjudicator's two-term dyadic 2 sqrt(C eps)) violates the CUMULATIVE ladder just below the atom; the true optimum is the min-profile above. Numerically confirmed (verify V5): discretized LP = 2.775 + 0.050 truncation-tail = 2.825 vs 2 sqrt 2 = 2.8284; dyadic-height-restricted LP = 1.611 (the adjudicator's 2.0 was likewise a two-term estimate). The squeeze conclusion is unchanged and strengthened: capacity O(sqrt(eps C_led)) N = o(N) as eps -> 0 at fixed C_led; bounded heights are blocked by the Frobenius cost, divergent heights by the ladder cap.

**LP form (coupled, convex):** garnish Frobenius budget g_F >= 0 with
    (R-6') |E_w[C'] - c3 N| <= eps_3 N + 2 sqrt(2) sqrt(C_led * g_F) N,
    (R-5') |E_w[F'] - kappa N| + g_F N <= eps_F N,
the concave sqrt outer-approximated by 3 tangent cuts (exact at the reported optimum by re-solving with the active tangent refined). Additionally a decoupled parametric mode: Gamma in {0, 0.05, 0.10, 0.25} as a fixed cubic slack, reporting delta_0(Gamma) and the shadow price d delta_0 / d Gamma.

**Honest-effectivity note (pre-registered).** At honest finite-T constants (eps_g ~ 1/L, C_led ~ c_bridge^{-4} possibly 10^2-10^4), Gamma_fuzz dwarfs any O(0.1) margin until L is astronomically large; asymptotically Gamma -> 0 and the LP verdict is delta_0(Gamma -> 0) by continuity (piecewise-linear in Gamma). The gate therefore decides the ASYMPTOTIC system; the Gamma-slope and the crossover L are reported as the effectivity price any eventual theorem must pay. C_led scan: {max(10, 2 C_led^min), 100, 1000}; a bite that dies below C_led = 10^3 is fragile (bridge constant unknown, enters as c^{-4}) and must be reported as such.

### 4.3 Tier-2 rows (diagnostic only; not part of the primary verdict)

Add open-band form-factor pinning at lambda = 1 (PairCeiling near-CUE rows |N S(j) - j| <= tau_2 for 1 <= j < N, edge row free, tau_2 in {1, 4} grid-units) to both the with-cubic and without-cubic systems. Purpose: measure whether the cubic row's bite (if any) survives when linear bandwidth-one data is fully consumed — i.e. whether it is NEW leverage beyond the (c0, r) certificate class (R6: the formal ceiling-scope evasion), or a re-reading of pair correlation. Basis flag F1 (§10): the unconditional status and depth-weighting of open-band F(alpha) (BGSTB24) is recalled, not verified — hence diagnostic status.

### 4.4 Tier-A harness (abstract R7 rows, calibration only)

A small exact-rational LP in aggregated variables (per-zero fractions s_m, pair fractions q_{m,w} with the §1.2 block charges, garnish variables, NO cross-term variables): rows = R7 literally (trace, Frobenius split, signed cubic, all-V ladder, n_- <= p, power-mean, Hoelder, fuzz). Purpose: (i) reproduce the adjudicator's squeeze numbers and the K1-as-written vacuity (regression tests); (ii) exhibit the §1.2 affine degeneracy (cubic row adds nothing over marks {1,2} + pairs in isolated blocks — the expected Tier-A outcome at lambda = 1); (iii) shadow-price sanity for Tier B. Tier A has NO decision authority in either direction: with free cross-terms it is vacuous, with nonnegative cross-terms it is unsound (K2-major-4) — this is precisely why R5 demands the explicit gate.

---

## 5. Decision criterion

### 5.1 The two quantities

    P_full  := min E_w[N_d]/N  subject to Tier-1 rows (§4.1 + §4.2), at a parameter point (W, C_led, eps-vector, Gamma-mode, v1, v', lambda', N);
    P_base  := the same minimum with the lambda'-cubic block removed (rows R-6/R-6'/R-7/fuzz deleted; R-5 kept — Frobenius at lambda' is two-moment data and belongs to the baseline);
    delta_0 := P_full - P_base   (the marginal value of the cubic block; >= 0 always).

Calibration requirement (must hold before any verdict is read): at the primary configuration with the cubic block AND the lambda'-Frobenius row removed, the LP must reproduce P = 5/6 -/+ LP tolerance with the 2/3 + 1/6-doubles law optimal (lemmaR_tight); the CUE null columns must be feasible for all rows at centered budgets.

Primary decision point: flat/flat windows, lambda' = 1/2, N = 64 (confirm 128), coupled-fuzz mode, budgets matched-geometry, reported at every (W, C_led, eps) grid point. P_full is also reported against the R5 benchmark form "N_d >= 5/6 + delta_0" (at the primary configuration P_base = 5/6 + [value of the lambda'-Frobenius row], so both readings are published; if the lambda'-Frobenius row alone moves the baseline off 5/6 that is itself a reportable two-moment fact, distinct from the cubic verdict).

### 5.2 Error bars

Budgets enter as ranged rows (§2.2). Two solves per grid point:
    delta_0^lo: budget ranges adversary-favorable (worst case within bars) — the conservative bite measure;
    delta_0^ctr: centered budgets — the absorption measure.
LP-solver tolerance and column-generation gap are added to the bar; matched-n vs asymptotic budget variants must agree in sign.

### 5.3 W-scaling (the sprinkling question)

Grid W in {2 (calibration), 3, 4, 6, 8}. delta_0(W) must be reported with the fit delta_0(W) = delta_inf + c W^{-kappa}. The sprinkling adversary (m ~ loglog T) means only delta_inf carries asymptotic meaning.

### 5.4 Verdict rules (pre-registered)

* **BITE** iff delta_0^lo > 0 at the primary point for ALL W in {3,4,6,8}, the fitted delta_inf > 0 at 2 sigma, stability under N = 64 -> 128 (relative change < 30%), under depth-grid halving, and under the C_led scan up to 10^3, with the Gamma-slope reported. Deliverable: the delta_0 table + the dual certificate (row multipliers) as the blueprint for M3/M4 and the go-signal for the R2 bridge.
* **ABSORPTION** iff an explicit law (the witness: weights, positions, marks, depths — published as JSON) is feasible at centered budgets for every Tier-1 row with E_w[N_d]/N <= 5/6 + 0.01, stable under budget re-centering at N = 128. Deliverable: the sharpened no-go paper "the bandwidth-one ceiling is robust under RS-range cubic augmentation with capacity control" (the witness family = the paper's §-main object; PairCeiling-style formalization queued), PLUS the adjudication's positive complement (garnish-type escape is capped at 2 sqrt 2 sqrt(C_led eps) N — §4.2 — so the absorption necessarily runs through position/interference freedom; the witness will exhibit which channel).
* **INCONCLUSIVE at this scale** otherwise (in particular whenever 0 lies inside [delta_0^lo, delta_0^ctr + bar] on part of the W-grid): say so plainly; report the binding rows, the gap magnitude, and the scale-up cost estimate (N = 256 with the same architecture); do NOT force a verdict.

Tier-2 annotation (whatever the verdict): delta_0' := P_full^{T2} - P_base^{T2}; a Tier-1 bite with delta_0' ~ 0 is reported as "re-reading of linear pair data, no ceiling-class escape" (still a valid A4 bite for the 5/6-benchmark, but the R6 framing governs the claim's wording).

### 5.5 Relation to the R5 text

R5's "the N_d-extremal configuration is cut off by the cubic row against ALL admissible adversaries" == delta_0^lo > 0 in §5.4 (the extremal family is seed 1 of the dictionary; "cut off" = it and every repair of it priced by the LP cost N_d more). R5's absorption == the witness of §5.4. R5's "a result within error bars of 0 is 'gate inconclusive'" == the third rule.

---

## 6. Discretization summary (fixed choices)

| item | primary | scans / checks |
|---|---|---|
| period N (zeros) | 64 | 128 confirmation; verdict-stability required |
| bandwidths | lambda = 1 and lambda' = 1/2 | exploratory lambda' in {0.55, 0.60, 0.65} (M5 payoff-curve table; outside proven-ladder regime, labeled) |
| windows (v1, v') | flat, flat | cos(2 vartheta sigma), vartheta in {1/sqrt 2, 0.8}, each side independently |
| mark alphabet W | {2 calib; 3, 4, 6, 8} | fit delta_inf |
| pair-depth grid w | {0+(=1/64), 1/8, 1/4, 1/2, 3/4, 1} | halving check; deep probes {1.5, 2} as ladder-priced columns |
| ladder V-grid | {2, 3, 4, 6, 8, 12, 16} | C_led in {max(10, 2 C_led^min), 100, 1000} |
| eps knobs | eps_F1 = eps_F = eps_3 in {0.02, 0.05, 0.10} | fuzz: coupled mode + parametric Gamma in {0, .05, .10, .25} |
| null sampler | CUE eigenangles, n in {64, 128, 512, 1024, 2048} | R adaptive: SE(m3) <= 0.5%, cap 5000; anchors = §2.1 closed forms |
| LP | HiGHS float; rational re-verify of final basis; column generation with 200-restart stop | Tier A exact rational (Fraction simplex) |
| minimum atom separation | 1/8 gap | halving check |
| thermal | <= 4 concurrent heavy processes (MC batches of 4; single-threaded LP) | |

Estimated compute: null budgets ~ 6 CPU-hours; Tier B master + column generation across the full scan grid ~ 30-60 CPU-hours at N = 64 (batched 4-wide, well within policy); N = 128 confirmation ~ 4x the primary point only.

## 7. Implementation plan (file layout under results/a4-m2-gate/)

    SPEC.md                 (this file)
    verify/                 (formulator's verification suite — done: verify_constants.py, verify_out.json)
    code/kernels.py         psi/A(w)/U3 assembly, finite-circle traces, eigh reader (single code path for null and columns)
    code/null_budgets.py    CUE sampler, budget tables + SE + anchors check     -> runs/budgets_*.json
    code/tier_a.py          exact-rational R7 harness + adjudication regression -> runs/tier_a.json
    code/dictionary.py      seeds 1-7, column evaluator (all row values per configuration)
    code/master_lp.py       ranged-row LP, fuzz cuts, P_full/P_base, duals      -> runs/lp_*.json
    code/column_gen.py      pricing search (gradient in positions, discrete moves in marks/depths), 200-restart protocol
    code/report.py          delta_0 tables, W-fit, verdict rule application     -> REPORT.md + witness JSON (absorption branch)

Order of execution: (0) budgets + anchors halt-check; (1) Tier A regressions (must reproduce: K1-as-written vacuity; squeeze capacity ~ 2 sqrt 2 sqrt(C eps); lambda=1 affine degeneracy); (2) calibration solve (5/6 + lemmaR_tight extremal recovered); (3) primary decision point with column generation; (4) scans (W, C_led, eps, Gamma, windows); (5) N = 128 confirmation at the primary point; (6) exploratory lambda' table; (7) REPORT.md with the §5.4 rule applied verbatim. Any halt-condition trip (anchor mismatch, infeasible null, calibration failure) stops the run and is itself reported.

## 8. Pre-registered expectations (to test against, not assume)

1. Referee: P(bite) <= 50%. 2. G(1; flat) = 0 (the 2 = 2 saturation) — VERIFIED analytically; the lambda = 1 cubic row alone cannot cut the doubles corner. 3. The §7.3-margin analog 2 m2 - m3 at lambda' = 1/2 is NEGATIVE for every window in the family (flat: -2/3; best in family: -0.660) — VERIFIED; a bite cannot come from the omega(m)-moment route at the operating point and would have to be produced by the joint positional pricing (X2', X3', ladder) — this makes a bite LESS likely than the §7.3 intuition suggested and the spec records that prior shift. 4. Adjudication: garnish/spectral-escape absorption is capped (§4.2); absorption, if found, must exploit position/interference freedom (shallow pairs w -> 0+ mimicking doubles inside clusters is the leading candidate channel, per §1.2 block continuity). 5. The exploratory lambda'-scan should show the margin structure improving toward lambda' = 2/3 (G decreasing, 2 m2 - m3 sign flip near lambda' ~ 0.61 flat — computed) — the quantitative face of the M5 payoff curve.

## 9. Appendix: derivations recorded

### 9.1 Sine-Gram moments
m2: tr^2 per zero = psi(0)^2 + Integral rho_2 psi^2 = 1 + Integral u^2 - Integral t (u*u) (Parseval; t = (S^2)^). Flat: Integral u^2 = 1/lambda; Integral t(u*u) = (2/lambda) Integral_0^lambda (1-a)(1 - a/lambda) da = 1 - lambda/3 => m2 = 1/lambda + lambda/3. m3: ordered-triple decomposition 1 (all-equal) + 3 Integral rho_2 psi^2 (two-equal) + T3 (distinct; rho_3 determinantal): T3 pieces via Integral F-hat G-hat H-hat: Integral u^3 - 3 Integral (t*u) u^2 + 2 Integral (b*u)^3. Flat: 1/lambda^2 - 3(1/lambda - 1/3) + 2(1 - lambda/2) => m3 = 1 + 1/lambda^2. Checks: m3(1) = 2; MC (n = 512): m2(1/2) = 2.1602(13) -> 13/6, m3(1/2) = 4.975(8) -> 5 with 1/n trend.

### 9.2 Pair block
x^T x = L Phi(0) real depth-independent and |x|^2 = L Phi(2 i delta) from the sampling identity; x = p + iq => block 2m(p p^T - q q^T) with <p,q> = 0, P - Q = L^2 a, P + Q = L^2 a A => eigenvalues m(1 +/- A). Per-zero charges (block/2, m = 1): trace 1, Frobenius 1 + A^2, cubic 1 + 3 A^2; identity c = 3F - 2 exact at every depth; atoms: c = 3F - 2 + (m-1)(m-2), the second integrality level.

### 9.3 Fuzz capacity
In N(h) := ladder-cumulative parametrization: maximize N(1) + 3 Integral h^2 N s.t. N(1) + 2 Integral h N <= eps_g, N decreasing, N <= C h^{-4}. Pointwise Lagrangian: coefficient 3h^2 - 2 mu h changes sign at a = 2 mu/3; optimum N = C a^{-4} on [C_abs, a], C h^{-4} beyond; Frobenius constraint gives 2C/a^2 = eps_g, a = sqrt(2C/eps_g); value 4C/a = 2 sqrt 2 sqrt(C eps_g). The point-mass-plus-tail profile (5/sqrt 3 sqrt(C eps)) violates the cumulative ladder on (a/1.19, a) and is infeasible; LP confirmation §4.2.

### 9.4 Support arithmetic (R6, recorded)
tr G-hat'^3 data support (k-1) lambda' = 1 + o(1) (tx_081 verbatim); the genuinely cubic prime resonance is the absolute constant sum_p (log p)^3/(p-1)^2 = 2.315762 (re-sieved to 3e6), an O(1) additive term on tr^3 = O(1/N) per zero. All gate claims are worded per R6: nonlinear spectral reading of bandwidth-one pair data with capacity control.

## 10. Flags (standing order 5 quarantine)

* F1 (Tier 2 only): BGSTB24 (arXiv:2306.04799) unconditional open-band F(alpha) — statement form and off-line-zero depth-weighting recalled from the program literature file, not re-verified. Tier 2 is diagnostic until fetched and checked.
* F2: identification c3(lambda') = sine m3(lambda') rests on RS96-range GUE n-level correlations and on the §5 diagonal method's uniformity in the near-critical polylog window — the direction file's own standing flag; carried, not discharged, by this spec. The gate's budget column is the sine value with eps_3 tolerance.
* F3: v5 §7.3 items now VERIFIED here: m_k(1) = 1, 4/3, 2 (k <= 3) and the margin 0.68524 at v = cos(1.6 sigma); the k = 4 value 13/4 and the omega(m)/Schur–Horn construction remain recalled (not consumed by the gate).
* F4: the all-V ladder (R-7) and hence the fuzz constant's C_led rest on Theorem 1(ii)-repaired, whose bridge (R2) is UNPROVEN — the one load-bearing analytic gap. Gate semantics: bite branch is contingent on R2 (which is exactly why the gate runs first — it prices whether R2 is worth proving); absorption branch is strengthened by assuming the ladder (absorption even WITH the ladder).
* F5: Huxley 1972's exact form — flagged in the direction file; NOT load-bearing here (theta < 1 ladder is MVT-4-only, per the adjudication).
* F6: adjudication's squeeze constant "2 sqrt(eps C_led)" and my first-pass 5/sqrt 3 both corrected to the sharp 2 sqrt 2 sqrt(C_led eps_g) (§4.2, §9.3) — an update to the adjudication's bookkeeping, same order, conclusion unchanged.
* F7: verify V3's 2e-3 eigenvalue deviations are window-truncation artifacts of the check itself (nwin finite), not of the block law.
