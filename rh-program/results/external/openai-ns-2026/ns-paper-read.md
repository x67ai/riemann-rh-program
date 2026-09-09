# Reader report: OpenAI, "Finite time blowup for Navier–Stokes" (2026-09-08)

Reader agent: `ns-paper`. Date: 2026-09-09.
Source: `fetched-r4/openai-ns/openai-navier-stokes-2026-09-08.pdf` (166 pp., pdfTeX, no author metadata).
Original URL: https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
Method: `pdftotext` per section; formulas quoted were vision-checked on page renders (pdftoppm -r 110).
Page numbers below are the paper's own printed page numbers unless marked "pdf p.".

Sponsor's question: "learn whatever you can from their approach" — for an AI-agent attack on RH with a barrier zoo and Lean formalization. Read for method as much as mathematics.

Status: COMPLETE (see end of file).

## 1. The theorem, verbatim

Front matter (p. 1): title "FINITE TIME BLOWUP FOR NAVIER–STOKES", author line "OPENAI" — no individual
authors, no affiliations, no date, no arXiv number, no acknowledgments on the title page. PDF metadata
has empty Title/Author fields; produced by pdfTeX 1.40.29 with hyperref, created 2026-09-09 00:36 IST
(i.e. 2026-09-08 evening UTC).

Abstract (p. 1, verbatim): "For every positive viscosity, we construct a solution of the three-dimensional
incompressible Navier–Stokes equations that starts from rest and develops unbounded velocity in finite
time while maintaining uniformly bounded kinetic energy."

**Theorem 1.1** (p. 1, verbatim, vision-checked against the page render):

> For every ν > 0 there exist a force f ∈ C_c^∞(R^3 × (0, ∞); R^3), a compact set K ⊂ R^3, and smooth
> velocity and pressure fields u, p on R^3 × [0, 1) satisfying
>
>     ∂_t u + (u·∇)u − ν∆u + ∇p = f,   ∇·u = 0,   u(·, 0) = 0,        (1.1)
>
> such that supp u(·,t) ∪ supp p(·,t) ⊂ K for every 0 ≤ t < 1,
>
>     sup_{0≤t<1} ‖u(t)‖_{L^2(R^3)} < ∞,   limsup_{t↑1} ‖u(t)‖_{L^∞(R^3)} = ∞.
>
> Consequently, there is no smooth solution (u, P) on R^3 × [0, ∞) with the same force and initial datum
> whose kinetic energy is uniformly bounded sup_{t≥0} ½ ∫_{R^3} |u(x,t)|^2 dx < ∞.

Immediately after (p. 1): "This establishes alternative (C) in the Millennium problem statement for
Navier–Stokes as stated by Fefferman in [13]. Compact support also yields the corresponding construction
on T^3 = R^3/Z^3, establishing alternative (D) in [13]; see Corollary 10.6."

There is no other theorem in §1. The only other top-level result statements are Corollary 10.6 (torus) and
the whole-space theorem in §10 (quoted in §1 of this report below, after reading §10).

### Reading the statement

* **Function spaces.** f is C^∞ with compact support in R^3 × (0, ∞) — so the force is smooth in space
  AND time, vanishes near t = 0 and for large t, and is compactly supported in space. This is strictly
  stronger than what Fefferman's (C) requires (Fefferman asks for f smooth with bounded derivatives
  of every order, |∂^α_x ∂^m_t f| ≤ C_{αmK}(1+|x|+t)^{−K}; compact support implies this). u, p are
  smooth on R^3 × [0, 1) only — the solution lives up to the singular time, not beyond.
* **Initial datum.** u(·,0) = 0. Zero initial velocity. So the datum is trivially in Fefferman's class
  (Schwartz, divergence-free). All the "content" is in the force.
* **Energy.** sup_{t<1} ‖u(t)‖_{L^2} < ∞ — kinetic energy bounded uniformly up to the blowup time. §2
  (p. 4) states the core kinetic energy is O(τ^{1/2−3h}) → 0, i.e. the singular core carries vanishing
  energy; the L^2 bound is not the delicate part.
* **Blowup.** limsup_{t↑1} ‖u(t)‖_{L^∞} = ∞. Note: limsup, not lim; and L^∞, not a gradient or vorticity
  norm. §2 (p. 4) gives the actual rates: |u_θ|, |u_z| ≍ τ^{−1/2−h}, |u_r| = O(τ^{−1/2}), τ = 1 − t,
  with a fixed 0 < h < 1/100. Note τ^{−1/2} is exactly the NS-critical (scale-invariant) blowup rate;
  the construction is SUPERCRITICAL by the small exponent h in the azimuthal/axial components
  (consistent with the Escauriaza–Seregin–Šverák type criteria that rule out blowup with bounded
  L^∞_t L^3_x — here L^3 is not bounded: ℓ_r^2 ℓ_z · τ^{−3(1/2+h)} ≍ τ^{3/2−h−3/2−3h} = τ^{−4h} → ∞).
* **Compact support in space.** supp u(t) ∪ supp p(t) ⊂ K for all t < 1 — a single compact K. This is
  what lets the paper transplant to the torus (Corollary 10.6) by periodizing.
* **The "consequently" clause is the Clay-(C) sentence.** Fefferman (C) is: there exist smooth
  divergence-free u^0 and smooth f such that there is NO smooth solution on R^3 × [0, ∞) with bounded
  energy. The paper argues: any such global smooth finite-energy solution would have to coincide with
  the constructed u on [0, 1) (uniqueness of smooth finite-energy solutions with the same data and
  force), and the constructed u is unbounded as t ↑ 1, so no global smooth solution exists. The
  uniqueness step is the hinge and is where a referee checks the class carefully — see §6 of this
  report.
* **Mapping to Clay (C)/(D).** (C) = breakdown on R^3 with force; (D) = breakdown on T^3 with force.
  Both are the DISPROOF ("breakdown") alternatives of the Millennium statement; (A)/(B) are the
  existence-and-smoothness alternatives. Fefferman's official statement lists four alternatives and
  asks for a proof of any one; the paper claims (C) and (D). The paper does NOT claim anything about
  the unforced problem.

### What is NOT claimed

* Nothing about f ≡ 0. The abstract says "starts from rest"; the singular behavior is entirely
  force-driven (the force is nonzero on (0, ∞) — and must be, since u(0) = 0 with f = 0 gives u ≡ 0).
  The paper never asserts anything about the unforced Cauchy problem; §1.1 (p. 2) cites
  Escauriaza–Seregin–Šverák [11] as "regularity for the unforced Cauchy problem under a bounded
  scale-invariant L^∞_t L^3_x norm" and leaves it there.
* Nothing about Leray–Hopf weak solutions beyond t = 1; the paper does not discuss continuation.
* No claim of a blowup for arbitrary data, no claim about generic data, no quantitative statement
  beyond the rates in §2.
* The force is NOT small: it is "an exponentially small external force seeds each pulse" (p. 6) plus
  the cutoff/localization force plus whatever the corrections leave — the paper describes f as the
  residual R(u,p) of a designed (u,p), so f is whatever is left, and the theorem asserts only that the
  leftover is smooth and compactly supported. Fefferman's (C) has no smallness requirement.

## 2. The proof architecture in plain terms

### 2.0 The one-line idea (p. 3, §2 opening — the "big yet cancel" balance)

The paper's own statement of its method (p. 3): "For any incompressible flow u and pressure p, we can
always define the external force f to be the residual in (1.1). The Navier–Stokes equations then hold
by construction. The challenge is to choose a flow that blows up while this residual remains smooth.
The individual terms in the momentum residual can diverge, but we must arrange sufficient cancellation
that their sum and all its derivatives extend smoothly through the singular time."

So the theorem is a DESIGN problem, not an evolution problem: pick (u, p) with u blowing up, define
f := R(u,p) = ∂_t u + (u·∇)u − ∆u + ∇p (eq. (3.1), p. 6, at ν = 1), and prove f is C^∞ through t = 1.
No PDE is ever solved forward in time; no stability of a blowup profile is ever proved. Everything is
an explicit or recursively defined ansatz plus estimates on its residual. The reduction to ν = 1 is
the standard scaling u_ν(x,t) = √ν u(x/√ν, t), p_ν = ν p(x/√ν, t), f_ν = √ν f(x/√ν, t) (p. 7; verified
in (10.22)–(10.23)); the singular time is unchanged.

The "big yet cancel" mechanism, in the paper's own words (pp. 5–6, §2.2): the self-similar collapsing
vortex core satisfies its leading momentum balance in the inner region, but joining it to a smooth
exterior "leaves an imbalance in the annulus. The external force needed to sustain the background
becomes unbounded as t ↑ 1, so it cannot serve as the smooth external force." So they add "a sequence
of spatially oscillatory pulses ... localized in radius, height, and time, but extend[ing] around a
complete ring. An exponentially small external force seeds each pulse; the background shear supplies
its subsequent growth. Their cylindrical velocity components have zero angular average, but their
momentum fluxes need not." The averaged Reynolds stress ⟨w_r w_θ⟩, ⟨w_r w_z⟩ of the pulses is chosen
to equal the annular stress T whose negative divergence is the singular part of the background
residual (p. 12: "⟨w̃_r w̃_θ⟩, ⟨w̃_r w̃_z⟩ = T + higher-order terms"). The force that appears in the
theorem is therefore (a) the exponentially small seeds of the pulses, (b) the cutoff terms far from
the singular point, and (c) a "flat" remainder — every Cartesian space-time derivative O(q^N) for
every N (Theorem 3.1(iii), eq. (3.4), p. 15) — which extends by zero through t = 1.

Scales (pp. 4, 7–8, 11): τ = 1 − t; concentration scale q ≍ τ near the singular point; A = 1/2 + h,
D = 1/2 − h, 0 < h < 1/100 fixed. Core radius ℓ_r ≍ τ^{1/2}, core height ℓ_z ≍ τ^{1/2−h}. Velocities
u_θ, u_z ≍ τ^{−A}. Pulse amplitude A_wave ≍ q^{−1/2−h/2}, wavelength ℓ_wave ≍ q^{1/2+h/2}, so
A_wave^2 ≍ q^{−1−h} ≍ |u_θ^{(0)}|/q^{1/2}, which is exactly the scale of the stress needed (p. 11).
The expansion parameter for the whole construction is ε = q^h (ratio of axial to radial diffusion,
p. 8): everything is a series in powers of q^h, i.e. in ε, and the small exponent h is what makes the
series terms separate. Note the scaling A_wave/u_θ ≍ q^{h/2} → 0: the pulses are asymptotically SMALLER
than the background velocity but their squared amplitude is the RIGHT size for the stress. This is
the numerology at the center of the paper.

### 2.1 Section-by-section

**§3 Proof outline (pp. 6–24).** 18 pages, but ~6 of them (pp. 18–24) are a "Guide to the principal
symbols" table (Table 1) plus notation conventions. The substantive outline is pp. 6–17: §3.1
concentrating leading field; §3.2 background stress and the four-step profile construction; §3.3
oscillations and momentum transport (with the exact residual identity R(u_B+w, p_B+π) = R(u_B,p_B) +
L_{u_B}(w,π) + ∇·(w⊗w), p. 11); §3.4 correction cycle and summation; §3.5 localization and completion;
plus Theorem 3.1 (p. 15) which is the "local" theorem that §§4–9 deliver and §10 consumes. Two flow
charts (Figures 5, 6, pp. 13, 15) map each box to a numbered proposition/equation. See §4 of this
report on whether it reads as a plan.

**§4 Constructing the leading order flow (pp. 24–45).** Object built: axisymmetric profiles E (swirl),
U (axial), V_0 (radial flux), Π (pressure) in similarity coordinates X = r^2/(2q), η = z/q^D, so that
u_θ^{(0)} = q^{−A} E, u_z^{(0)} = q^{−A} U, r u_r^{(0)} = V_0, p^{(0)} = q^{−2A} Π (p. 7). Output:
Theorem 4.6 (profiles exist with: regularity at the axis; stress T = (T_{rθ}, T_{rz}) supported
exactly in an annulus X_a < X < X_b; exact "heat exterior" beyond; and the "admissible stress cone
condition" of Lemma 4.5 holding throughout the annulus). The "five cumulative radial integrals" (4.15)
— pressure, radial velocity, and stress moments — are the invariants that let pieces built on
different radial intervals be glued without disturbing the exterior (Lemma 4.4). Four sub-steps (p. 10):
(1) exterior + axis pressure (App. A, Props A.4, A.6, A.7); (2) inner analytic solution near the axis
(App. B, Prop B.2 — "E/√(2X), U, Π analytic in X, η near the axis"); (3) joining and moment matching
(Cor B.10, Prop B.8); (4) enforcing the cone condition by adding a radial oscillation with phase
N log X, amplitude O(1/N), which changes the shear at order one while changing values and moments by
O(1/N) (App. C, Props C.2, C.3). Technique family: **matched asymptotics / self-similar ansatz with
explicit ODE-in-X profile construction** — closer in spirit to the self-similar-profile literature
(Elgindi; Chen–Hou) than to convex integration, though the paper cites neither; its own citations for
the inner core are none (it is presented as new) and the profiles are built by hand with an analytic
Cauchy–Kovalevskaya-type argument near the axis (App. B) and explicit heat-kernel formulas in the
exterior (App. A). [My inference: the "N log X oscillation to open the cone" trick in App. C is a
small-parameter perturbation, not a convex-integration step; it is the kind of device one uses when
the naïve profile fails a sign condition.]

**"Admissible stress cone"** (pp. 9–10, Lemma 4.5, Prop 7.5, Fig. 4): at each point of the annulus the
two pulse families have "covariance vectors" v_1, v_2 ∈ R^2 (the (rθ, rz) momentum-flux directions
per unit squared amplitude, determined by the local background shear). The required stress T must lie
in the OPEN positive cone {c_1 v_1 + c_2 v_2 : c_1, c_2 > 0}. Reason: squared amplitudes are
nonnegative, so the pulses can only supply stresses that are positive combinations of what each family
carries. This is the exact analog of the "positive-definiteness of the Reynolds stress / lies in a
convex cone of rank-one tensors" condition in convex integration (De Lellis–Székelyhidi's geometric
lemma), and the paper's Fig. 4 is essentially that lemma drawn in R^2. The paper attributes the
"use of oscillations to realize a prescribed stress" to Daneri–Székelyhidi [10] (p. 2), which is the
convex-integration lineage — but here the oscillations are physical linear instabilities amplified by
shear (Craik–Criminale [9], Lifschitz–Hameiri [17], Friedlander–Vishik [14]), not superimposed
Beltrami/Mikado flows.

**§5 Correcting the base flow to every order (pp. 45–62).** Object built: the axisymmetric background
(u_B, p_B) = formal series in ε^{2n} = q^{2nh}, n = 0, 1, 2, …, with coefficient profiles
(E_n, U_n, V_n, Π_n) (p. 11; Table 1 rows (5.1), (5.2)). Each order's source is determined by the
lower orders; the recursion absorbs "the radial momentum equation, axial viscosity, and the remaining
lower-order terms" (p. 11). The series is summed Borel-style: "coefficients are summed with smooth
cutoffs on their vector potentials and pressures, equal to one near the singularity and supported in
successively smaller neighborhoods" (p. 11) — Lemma 5.4 is the summation lemma, reused in §9. Output:
Prop 5.5 / eq. (5.41): R(u_B,p_B) = −(∂_r + 2/r) T_{phys,θ} e_θ − (∂_r + 1/r) T_{phys,z} e_z + E_B
with E_B "flat as q ↓ 0" (every derivative O(q^N) for all N). Technique family: **formal asymptotic
expansion in a small parameter with a Borel/cutoff summation to make the remainder flat** — the
classical "correct to all orders, then sum with shrinking cutoffs" device (as in constructions of
Gevrey/flat solutions, or in the Córdoba–Martínez-Zoroa IPM paper [7], which the paper explicitly
credits on p. 2 for "using approximations of increasing order to keep every spatial derivative of the
source uniformly bounded").

**§6 Auxiliary torus and separation of oscillatory supports (pp. 62–73).** Object built: bookkeeping.
Pulses are labeled γ = (ℓ, a, σ) = (dyadic band ℓ with Q = 2^{−ℓ}, slow box a, family σ ∈ {±1})
(Table 1, (6.8)). To keep products between distinct pulses from producing cross terms, the fields are
first built as functions of an extra auxiliary variable Y ∈ T^2 (an abstract torus) and only at the
end evaluated on the "phase map" Y(r,t) = v_r r^{d_r} + v_t t mod Z^2 (eq. (6.3), Table 1 p. 21).
Distinct pulses whose physical supports overlap get DISJOINT supports in Y, so their products vanish
identically (Lemma 6.1, p. 12). Averaging ⟨·⟩ = angular average composed with Haar average over Y
(eqs. (3.7)–(3.9), p. 17). §6 also fixes the normalized "chart" coordinates (R, Z, T) = (r/√Q, z/Q^D,
τ/Q), ε = Q^h, S_* = ℓ^2 (p. 17) and defines the coefficient classes W_α (wave amplitudes), M_α
(angular-mean coefficients), S_α (radial moments) — Definitions 6.4, 6.5 — that carry the bounds through
the induction. Technique family: **homogenization / two-scale (fast–slow) expansion with an auxiliary
torus**, the standard device of "extended fields F(x, Y) evaluated on Y = φ(x)/ε" from Nash–Kuiper /
convex-integration and from classical WKB/multiple-scale analysis; the disjoint-support-in-Y trick is
[my inference] a clean way to get the "no cross-interaction between building blocks" property that
Mikado flows provide in Euler convex integration.

**§7 Oscillatory realization and correction of the residual stress (pp. 73–88).** Object built: the
pulses themselves. Lemma 7.1: phase equations (wavevector transported by shear, radial wavenumber
grows linearly — the Craik–Criminale/Kelvin-mode kinematics). Lemma 7.4: amplitude equations — growth
rate from shear (Fig. 3(b)); viscous damping d = ε k^2 |n_Φ|^2 (Table 1 p. 22) with carrier frequency
k = ⌈ε^{−1/2}⌉ eventually wins, so each pulse "grows and then decays" and the temporal cutoff acts
"only in its exponentially small tails" (p. 12). Prop 7.5: positive squared weights c_1, c_2 exist
(the cone condition) so that ⟨covariance⟩ = T + h.o.t. Prop 7.6: signed amplitude increments whose
symmetrized cross-covariance with the leading pulses realizes a prescribed stress CORRECTION (needed
in the §9 cycle). Lemma 7.7: exactly divergence-free realization w = ∇ × A_wave with all chain-rule
terms from Y(r,t) retained; Cor 7.8: derivative bounds on the curl corrections. Technique family:
**linear WKB/geometric-optics along a shear flow (Lifschitz–Hameiri localized instability) used as
the building block of a Reynolds-stress-matching scheme** — the paper's explicit lineage (p. 2) is
[9, 14, 15, 17, 2, 3, 19] for the wave dynamics and [10] for realizing stress by oscillation.

**§8 Compactly supported mean corrections (pp. 88–100).** Object built: axisymmetric (angular-mean)
corrections (β, v, γ) to radial, azimuthal, axial velocity and mean pressure p_m, still possibly
depending on the auxiliary torus. Two mechanisms: (i) invert the fast auxiliary-time derivative
(operator N^{−1}, zero-Haar-mean inverse, (8.19), (8.23)) to kill the auxiliary-zero-mean part of the
angular-mean residual (8.20); (ii) solve "the five radial moment equations in (8.25)" — the same
five invariants as (4.15) — so that pressure and tangential-momentum "radial integral defects"
(P, J_θ, J_z, eq. (8.12), (8.15)) are canceled at linear order and the corrections stay compactly
supported in radius (via supported inverses T_e with cutoff remainders A_e, (8.6), (8.7)). Two of the
five equations preserve the zero angular-momentum and axial-flux integrals (9.10). Technique family:
**solvability/compatibility conditions of a linearized operator, handled by adjusting finitely many
moments** — classical Fredholm-alternative bookkeeping in a fast-slow setting.

**§9 Residual improvement and the local field (pp. 100–116).** Object built: the Newton-like
correction cycle and its summation. Stage j fields (u^{[j]}, p^{[j]}); increment (δu_j, δp_j)
divergence-free; residual identity R(u^{[j+1]}) = R(u^{[j]}) + L_{u^{[j]}}(δu_j, δp_j) + ∇·(δu_j⊗δu_j)
(p. 13). One cycle = four operations (p. 14): (1) solve inhomogeneous wave-amplitude equations for
nonzero angular harmonics (Prop 9.1, Lemma 9.2); (2) signed amplitude increments for the averaged
stress (Prop 7.6, (9.13)); (3) angular-mean correction via N^{−1} (8.20) with axial increment through
a vector potential (8.14); (4) five radial moment equations (8.25). After each operation the FULL
residual is recomputed (Prop 9.6) — "so newly created terms enter the next stage". Decay bookkeeping:
σ_0 = 1/5, σ_{j+1} = σ_j + 1/10, residual of order ε^{hσ_j}·q^{−K_m} for m-th derivatives, with K_m
independent of j (eq. (9.18), p. 14). Summation: cutoffs χ(a_j q) on potentials, curl after cutoff
(Lemma 5.4 again, (9.21)), giving (u_loc, p_loc) smooth for t < 1 with flat residual (9.20) and the
leading growth preserved (Prop 9.9 = Theorem 3.1). Technique family: **iterative residual improvement
with a fixed gain per step and a "flat remainder" summation** — structurally the Nash–Moser /
convex-integration induction ("each stage improves the Reynolds stress by a fixed factor; sum with
cutoffs"), but with LINEAR gain per step (σ_j += 1/10, i.e. a geometric improvement in ε-powers) rather
than the super-exponential frequency growth of Buckmaster–Vicol. [My inference: this is much closer
to a matched-asymptotics "correct to all orders" scheme (like [7]) than to convex integration proper;
there is no h-principle, no relaxation, no Onsager-type exponent bookkeeping. The pulses are physical
instabilities, and the stage index j indexes ORDER in ε, not frequency.]

**§10 Compact forcing and whole-space breakdown (pp. 116–126).** Object built: the global fields and
the actual force. Prop 10.1: multiply potentials by c = χ_x χ_t (χ_x compact axisymmetric, χ_t = 0
on [0, 1 − τ_0]), take curl after multiplication so u = curl(cA) + cB e_θ stays divergence-free
(p. 16). Lemma 10.2: compatible limits of all derivatives of f = R(u,p) as t ↑ 1 uniformly on R^3.
Lemma 10.3: extend f smoothly past t = 1 with support in K × [0, 2] (Whitney/Borel-type extension —
this is presumably where Stein [20] is cited). Lemma 10.4: global energy and dissipation bounds.
Lemma 10.5: uniqueness — "any smooth solution with the same force and zero initial datum whose kinetic
energy is uniformly bounded ... must agree with u on every [0, T], T < 1" (p. 17). Cor 10.6: torus.
Technique family: **standard cutoff/extension/weak-strong uniqueness**.

### 2.2 Which technique family, in one paragraph

What the paper's references and language say: the lineage claimed is (i) Córdoba–Martínez-Zoroa
[6, 7] and Córdoba–Martínez-Zoroa–Zheng [8] for "singularity formation based on amplification across
scales while controlling the regularity of the external force" (p. 2) and for "approximations of
increasing order to keep every spatial derivative of the source uniformly bounded" (p. 2); (ii)
Craik–Criminale, Lifschitz–Hameiri, Friedlander–Vishik, Leibovich–Stewartson, Billant–Gallaire,
Singh–Sridhar for the wave dynamics; (iii) Daneri–Székelyhidi for oscillations realizing a stress;
(iv) Tao [22], Buckmaster–Vicol [4], Albritton–Brué–Colombo [1] as context (averaged blowup;
nonuniqueness; forced nonuniqueness with singular force). The paper says its own distinctive point
is (p. 3): "Our construction also exploits dynamical amplification, with a different role for the
amplified disturbances: oscillatory pulses generate a mean momentum flux that supplies the missing
force on a collapsing background vortex."

What I infer: it is a **forced-blowup construction in the Córdoba–Martínez-Zoroa mold** (design the
solution, make the force the residual, control every derivative of the residual), whose core is a
**self-similar collapsing vortex** (matched-asymptotics style, with an inner analytic profile and an
exact exterior), and whose annulus is repaired by a **convex-integration-flavored Reynolds-stress
matching** in which the building blocks are **physical shear-amplified WKB pulses** instead of
Beltrami/Mikado flows. It is NOT self-similar-blowup-with-stability à la Elgindi/Chen–Hou (no
linearized stability, no spectral analysis, no computer assistance), and NOT convex integration in the
Buckmaster–Vicol sense (no weak solutions, no relaxation, everything C^∞ for t < 1). The paper neither
cites Elgindi, Chen–Hou, De Lellis–Székelyhidi, Isett, nor any computer-assisted-proof literature.

### 2.3 §10 in detail — the hinge lemmas (pp. 116–126, read in full)

* **Prop 10.1** (p. 117): cutoffs c = χ_x(x) χ_t(t), with χ_t = 0 for 1 − t ≥ τ_0 and = 1 for
  1 − t ≤ τ_0/2; u = curl(cA) + cB e_θ, p = c p_loc. The key inequality is q ≤ C_0(τ + |z|^{1/D})
  (10.3), which keeps the support inside the local domain Ω_* = {τ > 0, q < q_*}.
* **f := R(u,p)** (10.5, p. 118), "This definition includes every derivative of the cutoffs." The paper
  notes explicitly (p. 118) "the force may have nonzero divergence" — f is not projected.
* **Lemma 10.2** (p. 118): every ∂_x^α ∂_t^j f converges uniformly on R^3 as t ↑ 1 to ∂_x^α F_j with
  F_j ∈ C_c^∞ and ∂^α F_j(0) = 0. Proof splits R^3 × {t ≈ 1} into three regions: (a) q bounded below
  (Theorem 3.1(ii) gives bounded derivatives, FTC gives Cauchy); (b) r bounded below and q small
  (exterior heat field K = c_∞ s^{−A} H(2τ/s), explicit derivative bounds (10.8)); (c) near the origin
  (flatness (3.4) gives |∂^α ∂_t^j f| ≤ C (τ + |z|^{1/D})^N, eq. (10.9)).
* **Lemma 10.3** (p. 120): extension past t = 1 by a Borel-type series f(x, 1+σ) = Σ_j χ_0(b_j σ)
  σ^j F_j(x)/j! (10.11) with explicitly chosen integers b_j (a displayed min-formula) — support in
  K × [0, 2]. Then decay bounds |∂^α ∂_t^m f| ≤ M_{α,m}(3+R)^k (1+|x|+t)^{−k} — matched to "[13, (5)]",
  i.e. Fefferman's condition (5).
* **Lemma 10.4** (p. 121): energy: ‖u(t)‖_2^2 + 2∫_0^t ‖∇u‖_2^2 ≤ F(t)^2 with F(t) = ∫_0^t ‖f(s)‖_2 ds.
  Elementary.
* **Lemma 10.5** (p. 121–123) — the uniqueness/comparison lemma, and the single most load-bearing
  "classical" step: "Fix T < 1. If v, P is a smooth solution of (1.1) at viscosity one on R^3 × [0,T],
  with the force f of Lemma 10.3, zero initial velocity, and v ∈ L^∞([0,T]; L^2(R^3)), then v = u on
  that interval." Note the hypothesis class: SMOOTH, L^∞_t L^2_x, and NO growth condition on P or
  on ∇v at infinity ("These hypotheses leave the growth of spatial derivatives at infinity
  unrestricted", p. 121). The proof is a weak–strong-type argument on expanding balls: recover ∇P
  from the equation via Riesz transforms (π_* = Σ R_i R_j g_ij, (10.16)), show ∇π = ∇π_* by a
  Fourier-support-at-{0} argument (pp. 121–122), bound the pressure flux through ∂B_R by a
  commutator estimate ‖K_R‖_{4/3} ≤ C R^{−1} (p. 122) and interpolation (10.19), then a Gronwall on
  E_R(t) = ∫χ_R|w|^2 using ‖∇u‖_∞ < ∞ on [0,T] (u is the constructed smooth compactly supported
  field), giving E_R ≤ C'_T/R → 0. This is where the "Consequently" clause of Theorem 1.1 is earned.
  A referee will read this lemma line by line because it is the bridge from "we built one solution
  that blows up" to "no bounded-energy smooth solution exists" — see §6.
* **Proof of Theorem 1.1** (p. 124): also notes "The embedding H^3 ↪→ L^∞ excludes a classical H^3
  continuation through time one", and "The force is nonzero, since (10.13) would otherwise give
  u = 0" — a one-line sanity check that the theorem is not vacuous. Scaling (10.22)–(10.23) with
  ‖u_ν‖_2^2 = ν^{5/2} ‖u‖_2^2.
* **Cor 10.6** (p. 125): torus. Rescale by λ so λ^{−1}K_ν ⋐ Q_0 = (−1/2,1/2)^3, shift time by
  t_0 = 1 − λ^{−2}, periodize by summing translates (disjoint supports so the nonlinearity is exact).
  Uniqueness on T^3 is the trivial Gronwall (p. 126). Notes "The pressure is periodic as well, as
  required in the erratum to the problem statement [13]" — they read Fefferman's erratum.

## 3. What is genuinely new versus assembled

### 3.1 The paper's own attributions (§1.1, pp. 2–3; verbatim where it matters)

The bibliography has 22 entries. Of these, 6 are context/history (Euler 1757, Navier 1827, Stokes
1845, Leray 1934, CKN 1982, ESŠ 2003, Fefferman/Clay), 3 are "nearby results" (Tao [22] averaged
NS; Buckmaster–Vicol [4]; Albritton–Brué–Colombo [1]), 1 is a textbook (Stein [20], used once, p. 122,
for L^p-boundedness of Riesz transforms in Lemma 10.5), and the rest carry the method:

* Córdoba–Martínez-Zoroa [6] (forced 3D Euler blowup with C^{1,1/2−ε} ∩ L^2 force, arXiv 2023),
  Córdoba–Martínez-Zoroa–Zheng [8] (hypodissipative NS blowup with force in L^1_t C^{1,ε} ∩ L^∞_t L^2,
  ARMA 2026), Córdoba–Martínez-Zoroa [7] (IPM singularities with smooth source, arXiv 2024/25).
  The paper (p. 2): "These works established a strategy for singularity formation based on
  amplification across scales while controlling the regularity of the external force. In their
  constructions, larger-scale strain amplifies smaller-scale vorticity, with leading self-interactions
  and feedback on the larger scales suppressed." And on [7]: "using approximations of increasing order
  to keep every spatial derivative of the source uniformly bounded." Then (p. 3): "Our construction
  also exploits dynamical amplification, with a different role for the amplified disturbances:
  oscillatory pulses generate a mean momentum flux that supplies the missing force on a collapsing
  background vortex."
* Wave dynamics: Lifschitz–Hameiri [17], Friedlander–Vishik [14] ("describe the evolution of
  wavevectors and velocity polarizations along a background flow"), Craik–Criminale [9] ("exact
  finite-amplitude waves on affine background flows, exploiting the cancellation of the wave's
  quadratic self-interaction"), Leibovich–Stewartson [15], Billant–Gallaire [2, 3] (centrifugal
  instability criteria), Singh–Sridhar [19] (exact viscous shearing waves).
* Daneri–Székelyhidi [10]: "The use of oscillations to realize a prescribed stress is central to the
  Euler constructions of Daneri and Székelyhidi."

So the assembled ingredients are: (i) the "make the force the residual, control all derivatives"
strategy [6, 7, 8]; (ii) the Kelvin-mode / localized-instability kinematics of a WKB wave in shear
[9, 14, 17]; (iii) the Reynolds-stress-by-oscillation idea [10]; (iv) classical Whitney/Borel extension,
Riesz transforms, Gronwall.

### 3.2 What the paper presents as its own

The paper never uses the word "new" or "novel" about itself (grep: 0 hits for "novel"; "new" only in
technical senses like "new residual"). Its claim of originality is entirely implicit in the
attribution sentence quoted above ("a different role for the amplified disturbances"). Reading
between that line and the body, the steps that have no cited antecedent are:

1. **The specific self-similar collapsing vortex with anisotropic scaling** ℓ_r ≍ τ^{1/2}, ℓ_z ≍ τ^{1/2−h},
   A = 1/2 + h, D = 1/2 − h, and the deliberately ASYMMETRIC axial profile ("a slightly asymmetric
   axial profile, with a small upward bias and nonzero velocity at z = 0", p. 5) so that shear is
   available at every height. No citation. (§4, App. A, B.)
2. **The exact "heat exterior"** — an explicit swirl K(r,τ) = r^{−1−2h} H_ext(τ/r^2) solving the
   radial heat equation with H(Z) = Γ(1+h)^{−1} ∫_0^∞ e^{−v} v^h (1+Zv)^{−h} dv (eq. (4.29), p. 33),
   so the exterior residual vanishes identically and derivative limits at t = 1 are explicit. No
   citation. (App. A.)
3. **The five-moment gluing invariant** (4.15)/(Lemma 4.4/A.1/A.2): finitely many cumulative radial
   integrals whose preservation lets pieces built on different radial intervals be joined without
   changing the exterior. No citation.
4. **The admissible stress cone** (Lemma 4.5, (4.21)–(4.23)): the explicit 2D inequality system
   P_c > v_s, (v_s − 2) J_c^2 < 2(P_c − v_s)^2 — with the "v_s > 2" condition attributed to viscosity
   ("The additional inequality is required by the viscous waves", p. 31) — and the App. C device of
   an N log X phase oscillation to force the cone condition. No citation.
5. **The auxiliary-torus separation of pulse supports** (§6, Lemma 6.1). [My inference: this is a
   reinvention, in a fast–slow setting, of the "building blocks with disjoint supports" idea; it is
   not attributed to anyone.]
6. **The four-operation correction cycle** with gain σ_{j+1} = σ_j + 1/10 (Prop 9.6) and the
   "recompute the full residual after each operation" discipline. No citation.
7. **The uniqueness Lemma 10.5** in the class smooth ∩ L^∞_t L^2_x with no growth condition on the
   pressure. The technique is classical (expanding balls + Riesz commutator), but the paper works
   it out from scratch with only Stein [20] cited; the standard references (Serrin, Prodi, Lions,
   Galdi's book) are absent.

### 3.3 What is conspicuously NOT cited

No Elgindi (2021, C^{1,α} Euler blowup); no Chen–Hou (computer-assisted NS-boundary/Euler blowup);
no De Lellis–Székelyhidi (2009/2013), Isett, Buckmaster–De Lellis–Székelyhidi–Vicol (Onsager); no
Hou–Luo numerics; no Serrin/Prodi/Ladyzhenskaya uniqueness; no Whitney/Borel extension reference;
no Nash–Moser; no self-similar-profile literature (Nečas–Růžička–Šverák, Tsai). The bibliography is
lean to the point of austerity — 22 items for a 166-page paper claiming a Millennium Problem
alternative. [My inference: the bibliography was written to justify the specific steps taken and
nothing else; it reads like a dependency list, not a literature review. This is consistent with an
agent-produced document whose "related work" section was assembled from the actual inputs the
construction drew on rather than from a field survey.]

## 4. Signs of how it was produced

All counts are over the pdftotext layer (97,751 words; 8,656 layout lines).

**4.1 Vocabulary of hand-waving: essentially absent.**
"clearly" 0; "obviously" 0; "it is easy to see" 0; "easy to see" 0; "well known"/"well-known" 0;
"straightforward" 0; "routine" 0; "trivial" 0; "we omit" 0; "left to the reader" 0; "one checks" 0;
"should" 0; "expect" 0; "we believe" 0; "presumably" 0; "unable"/"do not know"/"not known" 0.
"standard" occurs ONCE (p. 122: "We use the standard L^p boundedness of Riesz transforms ... see
[20]"). "Note that" once (p. 28). "Remark" once (Remark B.9, p. 157 — and it is not a remark in the
usual sense; it is a dependency-order specification, see 4.4). "Indeed" 23, "Recall" 10. This
profile is far outside the norm for a human-written analysis paper of this length, where "clearly"
and "standard" typically appear dozens of times. I read it as a strong sign of either (a) a style
rule imposed on the writer ("no appeals to obviousness") or (b) generation by a system checked
against a rule of that kind.

**4.2 No human trace.** No author names, no affiliations, no acknowledgments ("acknowledg" 0,
"thank" 0), no funding, no date on the title page, no arXiv identifier, no "Data availability", no
mention of computers, numerics, or verification tools ("computer" 0, "numeric" 0, "Lean" 0,
"formal" only in "formal expansion/series"). No sentence anywhere describes how the proof was
found. The PDF metadata Author field is empty. The Euler companion in the same fetch
(`openai-euler-2026-09-08.pdf`, "Finite time blowup for the Euler equation", 60 pp., claims UNFORCED
Euler blowup from smooth compactly supported divergence-free data — a far stronger-sounding claim)
has the same author line "OPENAI" and the same house style; the NS paper does not cite it.

**4.3 Statement density and proof structure.**
8 Theorems, 42 Propositions, 73 Lemmas, 8 Corollaries, 5 Definitions, 1 Remark; 70 "Proof." and
72 "□" (the extra two end-of-proof marks close proofs stated as "Proof of Theorem 1.1" and
"This proves Theorem 3.1(iv), and completes its proof", p. 116). Numbered displayed equations:
§3: 11, §4: 43, §5: 46, §6: 32, §7: 42, §8: 27, §9: 21, App. A: 56, B: 40, C: 19. Proofs are organized
into explicitly labeled "Step 1: …", "Step 2: …" (64 occurrences), each step with a bold-face
sentence summarizing its goal, e.g. "Step 1: verify the summation hypotheses and choose the
cutoffs." (p. 60), "Step 4: verify the six conclusions." (p. 44), "Step 3: One-sided regularity away
from the singular point." (p. 115). Every proposition is cross-referenced forward and backward by
equation number; Fig. 5 and Fig. 6 (pp. 13, 15) are flowcharts whose boxes name the exact
proposition and equation that discharges them (e.g. "Lemma 7.7; (9.11)", "Proposition 9.6; (9.8),
(9.18)"). The hypertext links are live (hyperref).

**4.4 Explicit constants and explicit dependency order.** The paper tracks constants with an
unusual literalness: σ_0 = 1/5, σ_{j+1} = σ_j + 1/10 (p. 14); in the proof of Prop 9.5 (p. 107):
"These estimates imply (9.8) with B_0 = 0.7 and C_0^* = 1.2. The primary curl correction has
exponent 1 − κ_s > 0.68. All mean increments and pressure changes have exponent H_0 > 0.9, with
radial exponent H_0 + 1 > 1.9." — decimal exponents, with numerical slack stated ("gain greater than
0.8 above H_0"). Prop 9.6 (p. 108) tabulates the error exponents per interaction type in a 4-row
table (linear error B + 1/2 − 3κ_s; cross with old exact waves B + 1/2 − κ_s; self-interaction
2B − κ_s; cross with total mean B + 0.4). Lemma 10.3 gives b_j by an explicit min-formula (p. 120).
Theorem 4.6(v) gives H(Z) as an explicit integral (p. 33). Hext derivative bound: 2^A c_∞ 4^m (h)_m
(1+h)_m with rising factorials (p. 116). Definition 3.3 (p. 18) formalizes the parameter-choice
protocol: "we write α ≪ β when α/β is required to be sufficiently small, with the allowed size
depending on all data already fixed. In a chain of constants, choices proceed from right to left".
Remark B.9 (p. 157) then writes the actual dependency chain as a displayed diagram (B.40):
M_d, T_d, P_*, λ, h → tolerance, j_0 → δ_*, σ_*, Λ → (B_k), T_sh → C, X_R → κ_0, t_1, widths. This
is exactly the "parameter dependency graph" one writes when preparing a proof for mechanical
checking, or when many contributors must not accidentally create a circular choice.

**4.5 The Table 1 "Guide to the principal symbols"** (pp. 19–24, six pages, ~90 rows): every symbol
with role and the equation where it is defined. Includes disambiguations a human author would rarely
bother with: "The index n counts background expansion orders", "The background expansion order n,
correction stage j, dyadic band index ℓ, and Fourier harmonic index are distinct" (p. 17), "This
label is distinct from the axial mean-velocity component γ below" (p. 21), "Here ε denotes their
logarithmic width, independent of the physical scale q" (p. 21). [My inference: a symbol table of
this kind is what you produce when the document was written by many hands (or many agent
contexts) that needed a shared namespace; it is also what a formalizer asks for first.]

**4.6 Is §3 a plan the rest fulfils?** Yes, in a strong sense. §3 is 18 printed pages but only
~11 of prose (pp. 6–17); pp. 18–24 are notation and Table 1. The prose part is structured as
§3.1 (leading field) → §3.2 (four numbered construction steps, each naming the App. A/B/C result
that does it) → §3.3 (pulses; the exact residual identity; the numerology) → §3.4 (the four-operation
cycle, numbered 1–4, each naming its proposition) → Theorem 3.1 (the local contract, four clauses
(i)–(iv)) → §3.5 (how §10 consumes Theorem 3.1). Every box in Figs. 5–6 has a proposition number.
The body sections then open by restating the contract they fulfil: §4 (p. 24) "We first derive the
stress from the profiles, then identify the five cumulative radial integrals…"; §10 (p. 116) "In this
section we turn the fields supplied by Theorem 3.1 into the whole-space solution and force in
Theorem 1.1." The interface between §§4–9 and §10 is EXACTLY Theorem 3.1 — §10 uses nothing else
about the construction except (3.3)–(3.6). That is a clean module boundary. [My inference: Theorem
3.1 is the spec that the "construction" workstream had to deliver and the "completion" workstream
could assume; §§4–9 could have been developed and checked independently of §10, and vice versa.]

**4.7 Lean-shaped?** Not literally (no Lean, no Mathlib, no formal-statement blocks, and the
analysis — smooth functions of several variables, cutoffs, Riesz transforms, Gronwall — is far from
what Mathlib can currently host). But the statements ARE written in the shape a formalizer wants:
fully quantified hypotheses (Lemma 4.5: "Let a > 0, b_s ∈ R, p_s ∈ R^2, and define … by (4.20). If
v_s > 2, … is equivalent to (4.22). For every nonempty compact set K ⊂ {…} such that, for every
(a,b_s,w) ∈ K, [two displayed inequalities], there exists P_K > 0 with the following property…"),
explicit domains ("on the closed annulus [X_a, X_b] × [−1, 1]", "for every η ∈ [−1,1]"), explicit
uniformity claims ("The constants may depend on X_max"), explicit statements of what is preserved
across steps ("The cumulative bounds (9.9) and the exact moments (9.10) are preserved", Prop 9.6),
and one-sided-derivative conventions spelled out ("derivatives at the boundary are one-sided",
Thm 4.6(i)). Definition 9.4 ("Finite correction state") is an explicit invariant for the induction —
what a program would call the loop invariant.

**4.8 Redundancy.** Moderate and deliberate. §2 (physics) and §3 (outline) say the same things at
two levels of precision; §3 and Figs. 5–6 say them a third time; each body section re-summarizes
its role in its first paragraph. Sentences are short and declarative; there is almost no "we now
turn to" connective tissue beyond one sentence per subsection. The prose has the flat, uniform
register of a document generated under a strict style guide.

**4.9 What would a human editor have added?** A one-paragraph discussion of why the unforced
problem is different; a comparison with [1] (which also uses forcing and zero initial data) beyond
the single sentence "Their force lies in L^1_t L^2_x and is singular at the initial time"; a remark
on optimality of h or of the blowup rate; open questions; acknowledgments. None are present.

## 5. Transferable lessons for an AI-driven attack on RH

Each lesson names the feature of the paper it comes from; "the paper does X" is separated from
"I infer".

**L1. They attacked the disproof-shaped alternatives (C)/(D), not the proof-shaped (A)/(B), and
they chose the one where the free parameter (the force) lets you DESIGN the object.** The paper
does: pick (u,p), define f := R(u,p), prove f smooth (p. 3). The whole 166 pages is a
construction-plus-estimates, not an analysis of an unknown object. I infer: for RH the analogous
move is to look for statements in the RH orbit where a construction with a free parameter can be
DESIGNED rather than a fixed object analyzed — e.g. disproof-shaped variants (a counterexample to a
Selberg-class or Beurling-generalized-prime analog, a zero-free-region-violating Dirichlet series
with prescribed functional equation, a Beurling prime system with a specific zero). The barrier zoo
should carry, for each RH-adjacent conjecture, its DISPROOF-shaped form and a note on which
parameters are free in it. (Compare: Clay's NS statement offered four alternatives; the "cheapest"
one turned out to be the one with a free smooth force.)

**L2. A local "contract theorem" as the module boundary.** The paper does: Theorem 3.1 (p. 15) is
the only interface between the construction (§§4–9) and the completion (§10); §10 uses (3.3)–(3.6)
and nothing else. I infer: direction files in our program should be written as contract theorems
with numbered clauses that the downstream step consumes verbatim, so that agents on either side can
work (and be checked) independently. Our KICKSTART/direction files currently describe tasks; they
should also state the interface as a theorem-with-clauses.

**L3. The proof outline is a plan with a discharge map.** The paper does: every box in Figs. 5–6
names the proposition and equation that discharges it (pp. 13, 15); §3.2's four numbered steps and
§3.4's four numbered operations each cite the App./§9 result that does the work. I infer: we should
maintain a "discharge map" — a table from outline step to the file/lemma/Lean declaration that
discharges it — and treat an outline step without a discharge target as an open obligation. This is
a cheap artifact to keep current and it is the first thing a referee (or a verifier agent) wants.

**L4. Explicit parameter-dependency chains, written down as a diagram.** The paper does: Definition
3.3 (p. 18, "choices proceed from right to left") plus Remark B.9's chain (B.40) (p. 157). I infer:
circularity in parameter choice is the classic failure mode of long analytic constructions and of
multi-agent work (agent A fixes ε depending on N, agent B fixes N depending on ε). For any RH
sub-project with more than three parameters, a dependency chain file should exist and be checked
for acyclicity mechanically. For the Lean side this is automatic; for the informal side it must be
imposed.

**L5. Zero tolerance for "clearly".** The paper does: 0 occurrences of clearly/obviously/easy to
see/well known/standard(1) in 97k words (§4.1 above). I infer: a lint rule on our prose outputs that
rejects those words, forcing an agent either to write the argument or to cite. It costs nothing and
it is the one style feature of this document most obviously produced by a rule. It also makes the
text vastly easier to formalize later.

**L6. Numerical slack tracking in exponents.** The paper does: "B_0 = 0.7, C_0^* = 1.2", "exponent
1 − κ_s > 0.68", "gain greater than 0.8 above H_0", tabulated per-interaction exponents (pp. 107–108).
I infer: when an iteration must close with a fixed gain per step (here 1/10 in the ε-exponent), keep
a machine-readable ledger of every error term's exponent, so that the closing inequality is a
one-line check rather than a page of prose. For RH-adjacent analytic work (zero-density,
large-sieve, mollifier exponents), the same ledger discipline — exponent tables with explicit slack —
would let an agent verify closure mechanically and would surface exactly where a barrier bites.

**L7. Finitely many invariants as the gluing interface.** The paper does: the five cumulative
radial integrals (4.15)/Lemma 4.4 let pieces built on different radial intervals be glued without
disturbing the exterior; the same five moments reappear as the compatibility conditions in §8
(8.25). I infer: identify, for each RH sub-construction, the finite list of invariants that must be
preserved across a gluing/induction step, and make preserving them an explicit clause of every
lemma (as Prop 9.6 does: "The cumulative bounds (9.9) and the exact moments (9.10) are preserved").
This is also what makes the induction state (Definition 9.4) a checkable object.

**L8. The "big yet cancel" balance is a cone condition, and cone conditions are where sign
obstructions live.** The paper does: the required stress must lie in the OPEN positive cone of what
nonnegative squared amplitudes can supply (Lemma 4.5, Fig. 4); when the naive profile fails the
cone condition they perturb it (App. C, N log X oscillation) to force it. I infer: in the barrier
zoo, positivity/cone-type obstructions (e.g. the nonnegativity constraints in Beurling-Selberg /
Montgomery-pair-correlation extremal problems, the positivity in Weil's explicit-formula
criterion, sign constraints in de Branges-type approaches) should be catalogued as CONE conditions
with an explicit description of the generating vectors; the NS paper shows that a cone condition
which fails for the "natural" object can sometimes be forced by a cheap perturbation that changes
derivatives at order one while changing values at order 1/N. That is a general trick worth having
in the zoo as a "cone-opening perturbation".

**L9. Lean bibliography = dependency list, and that is a feature for verification.** The paper does:
22 references, of which about 10 carry weight, each cited at the exact step it supports (§3.1 above).
I infer: our output documents should carry a "load-bearing citations" list separate from context
citations, and each load-bearing citation should be tied to a lemma number in OUR text. A verifier
agent can then check the external inputs one by one. (The flip side, for the zoo: the NS paper's
absence of Elgindi/Chen–Hou citations means it did not go through the self-similar-stability
route; the zoo entry for "self-similar blowup" should record that a route AROUND the stability
barrier — design the solution, absorb the mismatch into a smooth force — exists.)

**L10. Flatness, not smallness, is the target.** The paper does: the residual is not made small in a
norm; it is made FLAT — every Cartesian space-time derivative O(q^N) for every N (Thm 3.1(iii),
(3.4)) — and then extended by zero through the singular time (Lemma 10.3). Flatness is achieved by
"correct to all orders in ε = q^h, then sum with shrinking cutoffs" (Lemma 5.4, reused in §9).
I infer: when an RH-adjacent construction needs a remainder that "does not matter", ask whether the
right notion is "flat at the boundary" (all derivatives vanish, Borel-summable) rather than "small in
L^2" — the former is what lets one glue across a singular point with C^∞ regularity. This is a
technique-family entry for the zoo ("all-orders correction + Borel/cutoff summation to flatness")
with this paper as the worked example.

## 6. Doubts

I did not referee 166 pages. What follows are places a referee would push, plus one structural
observation.

**D1. Lemma 10.5's uniqueness class (pp. 121–123).** The "Consequently" clause of Theorem 1.1 rests
entirely on: any SMOOTH solution with the same f, zero datum, and sup_t ‖v‖_2 < ∞ agrees with the
constructed u on [0,T], T < 1. Fefferman's (C) says "there exist … such that there is no solution
(p, u) on R^3 × [0,∞) satisfying (1), (2), (3), (6), (7)" — where (6)/(7) are smoothness and bounded
energy. So the hypothesis class matches Fefferman's. The proof recovers ∇P via Riesz transforms with
NO growth assumption on P; the argument that ∇π − ∇π_* has Fourier transform supported at {0} and
is therefore zero (p. 122) needs the difference to be a tempered distribution — smoothness alone does
not give temperedness of P. The paper handles this by working with ∫a∇π dt and the equation
(conservative form), deducing membership in H^{−3} from the OTHER terms, so temperedness of ∇π is
derived rather than assumed. That is correct in outline, but it is exactly the step where a
referee will want every line. Also: u is smooth with compact support and v ∈ L^∞_t L^2_x, so the
"difference energy on expanding balls" argument needs ‖∇u‖_∞ < ∞ on [0,T] (true, u is compactly
supported and smooth for t < 1) — fine.

**D2. The transfer from "u blows up" to "no global smooth v".** Once v = u on [0,1), v is unbounded
near (0,1) so it cannot be smooth on R^3 × [0,∞). This is sound. But note the subtlety the paper
itself flags (p. 124): the energy bound is on the HYPOTHETICAL v, so a Leray–Hopf weak continuation
past t = 1 is not excluded and is not discussed. Not a gap, but the statement is exactly as strong
as Fefferman's alternative (C) and no stronger.

**D3. The h < 1/100 constraint and its actual use.** h enters as the anisotropy exponent, the
expansion parameter ε = q^h, the pulse scaling, and the cone/viscosity inequalities. The proof
of Theorem 4.6 (Remark B.9) requires h ≪ λ and h ≪ e^{−T_d}, chosen after other parameters. A
referee would check that every "h sufficiently small" is consistent with h being fixed BEFORE q,
the bands, and the stages (the paper asserts this at the end of Theorem 4.6, p. 165: "The finite
frequency N was fixed in Proposition C.2 before the physical scale q and all later bands and
correction stages"). The dependency chain (B.40) is where I would start.

**D4. The auxiliary torus and the phase map Y(r,t).** The claim that products of distinct pulses
vanish identically after evaluation at Y(r,t) because their Y-supports are disjoint (Lemma 6.1) is
clean; but the physical derivatives then include chain-rule terms from Y(r,t) = v_r r^{d_r} + v_t t,
and the paper says (p. 12) "All chain-rule terms from Y(r,t) are included." The consistency of
angular/Haar averaging "before restriction to the physical phase map" (p. 17) with the actual
physical residual — i.e. that the averaged extended residual, evaluated at Y(r,t), equals the
physical residual up to terms that are controlled — is the kind of "the trick works" claim that a
referee checks by hand. Lemma 6.3 ("Number of relevant labels") bounds overlaps by O(S_ref^3); fine
in principle.

**D5. Per-stage constants vs. summation.** Prop 9.6 says constants "may depend on j, m" while K_m
(the derivative loss) is independent of j (p. 14). Summation with cutoffs χ(a_j q) then needs the
a_j chosen so that the tails satisfy (5.35). This is the standard place where "constants depending
on the stage" can silently defeat a summation; the paper's Lemma 5.4 is written to handle exactly
this (cutoff supports shrinking with the stage so each stage's constant is beaten by a power of q).
Plausible; would want to check that the derivative-loss exponent K_m really is j-independent in the
wave-amplitude equations, where each cycle adds harmonics.

**D6. The uniqueness/nonuniqueness landscape.** Albritton–Brué–Colombo [1] show NONUNIQUENESS of
Leray–Hopf solutions with zero data and a force in L^1_t L^2_x. The present paper's f is far more
regular (C_c^∞), and the uniqueness lemma is only used for t < 1 among SMOOTH bounded-energy
solutions, where uniqueness is classical. No conflict; just noting the two results sit side by side.

**D7. Provenance and checkability.** No author, no acknowledgment of any verification, no
companion code, no Lean, no numerics, and a 22-item bibliography. The Euler companion paper in the
same drop claims unforced Euler blowup from smooth compactly supported data — a claim that, if
correct, is at least as significant as this one and one that the field (Elgindi, Chen–Hou, Hou–Luo)
has been working toward for a decade with heavy computer assistance. Two such results released on
the same day with no stated verification process is itself a fact a referee must weigh. Nothing in
the NS text looked wrong to me at the level I read it (the outline is coherent, the numerology
closes, §10 is careful), but I read §§1–3 and §10 closely and only sampled §§4–9 and the
appendices (Thm 4.6, Lemma 4.5, Prop 5.5, Props 9.5–9.6, Remark B.9).

**D8. The one visible weakness of the writing as a verification artifact.** Because the correction
cycle "recomputes the full residual after each operation" and the exponents are tracked in prose
tables rather than in a single closed formula, checking closure of the induction (that σ_{j+1} =
σ_j + 1/10 really holds for every term) requires reconstructing the ledger by hand from pp. 101–111.
A machine-readable ledger would have made this a mechanical check. That is the same lesson as L6,
stated as a doubt.

---
Reading log: §§1–3 in full (pp. 1–24); §10 in full (pp. 116–126); references (pp. 165–166);
Theorem 4.6 + Lemma 4.5 (pp. 31–33); Prop 5.5 (pp. 60–61); Props 9.5–9.6 (pp. 107–108); Remark B.9
(p. 157); Euler companion p. 1. Vision-checked: pp. 1, 11, 14, 15 (Theorem 1.1, A_wave scaling,
σ_j recursion, Theorem 3.1).

Status: COMPLETE
