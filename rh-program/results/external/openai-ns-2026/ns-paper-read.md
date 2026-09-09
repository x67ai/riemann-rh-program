# Reader report: OpenAI, "Finite time blowup for Navier–Stokes" (2026-09-08)

Reader agent: `ns-paper`. Date: 2026-09-09.
Source: `fetched-r4/openai-ns/openai-navier-stokes-2026-09-08.pdf` (166 pp., pdfTeX, no author metadata).
Original URL: https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
Method: `pdftotext` per section; formulas quoted were vision-checked on page renders (pdftoppm -r 110).
Page numbers below are the paper's own printed page numbers unless marked "pdf p.".

Sponsor's question: "learn whatever you can from their approach" — for an AI-agent attack on RH with a barrier zoo and Lean formalization. Read for method as much as mathematics.

Status: IN PROGRESS (sections appended as read).

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

