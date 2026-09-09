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

