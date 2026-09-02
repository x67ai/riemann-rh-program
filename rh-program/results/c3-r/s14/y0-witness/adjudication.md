# ADJUDICATION — refuter F's Y₀-witness, verified as a construction — Session 14, 2026-09-03

**Program:** RH research program, direction C3-r, milestone M2c, Route 2 residue (R-ii) of
`results/c3-r/m2c-feasibility-ledger.md` §14. **Role:** binding adjudicator over the two independent
verification reports `verify-O.md` (verdict REPAIRED / partly) and `verify-F.md` (verdict VERIFIED /
no). **Model:** Claude Opus 5 (1M). Standing orders 5 and 7 in force: nothing below about a source is
from memory; every source claim is tagged to a page read on disk this session; where I ratify a
verifier's proof I say so and say whether I re-derived it. U.S. English.

**Inputs read in full this session.** `results/c3-r/s14/y0-witness/verify-O.md` (all),
`verify-F.md` (all), `results/c3-r/s14/adversarial/face-b-refuter-F.md` §3 (the object under
verification), `results/c3-r/m2c-feasibility-ledger.md` §§3 (T1–T3), 8 (S1–S5 rows), 14,
`results/c3-r/s2-feasibility-note.md` §§3.1–3.2.

**Source pages read verbatim this session** (fresh `pdftotext -layout`, one file per page; printed
page = PDF page):
- **[x-03]** `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`
  pp. 27, 32, 33, 37, 38, 39, 40, 42, 43, 49, 50, 59.
- **[x-06]** `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf` pp. 10–13.
- **[Den05]** `fetched/x-20-deninger-2005-arithmetic-geometry-and-analysis-on-foliated-spaces.pdf`
  pp. 22–25 (Cor. 5.5 and its remarks), 28–31 (§7.1–7.6), 33–35 (§7.7 and Thm. 7.8).
- **[ALKL]** `fetched-r3/r3s-17-alvarez-lopez-kordyukov-leichtnam-trace-formula-foliated-flows-arxiv-2402.06671v1-SESSION8-FETCH.pdf`
  pp. 1–5 of the memoir body (§§1.1–1.3.2), i.e. PDF pp. 7–13.

---

## §0. VERDICTS, STATED FIRST

### 0.1 Construction: **CONSTRUCTION-REPAIRED**

I rule with verifier O against verifier F on the verdict word, and with both on the mathematics.
After the repairs of §2 below — which the two verifiers found **independently and compatibly** —
every property refuter F claims for (Y, φ, f) is true and proved. But refuter F's §3.4 as printed is
not a complete construction, and one legal reading of what it leaves open **falsifies** its own
claim, so "VERIFIED" overstates:

- **(D1) Regularity of the tube field is load-bearing, not cosmetic.** F specifies only
  "∂_θ + α(r)∂_ψ − h(r)∂_r with α(0) = 0, α(1) an irrational multiple of 2π/log p,
  h(0) = h(1) = 0, h > 0 on (0,1)". Take h(r) = √r: then ṙ = −√r has the solutions
  r(t) = ((c−t)/2)² for t < c, r ≡ 0 for t ≥ c, so backward trajectories leave the core, the ODE
  does not define an ℝ-action, and "the core is the only closed orbit" is not even a statement about
  a flow. A Lipschitz (better: leafwise-smooth) choice must be imposed. Both verifiers imposed one.
- **(D2) "Thin closed tubular neighborhood … a solid torus" is wrong as printed in a 4-dimensional
  ambient.** T² × ℝ² has dimension 4; a tubular neighborhood of a circle there is S¹ × D³. The
  construction needs an explicit rank-2 normal frame — and the frame is not free: the joint
  continuity of the flow at the torus depends on the tube's θ-motion being carried to the
  T²-translation t·v_p. Both verifiers supplied the same frame (a T²-direction w_p ⊥ v_p and the
  ℝ²-radial direction).
- **(D3) The printed radius bound is insufficient for the property it is invoked for.** F writes
  "tube radius ≪ 1/p, so the N_p are pairwise disjoint". Disjointness needs the ℝ²-moduli to
  separate: |1/p − 1/q| ≥ 1/(p(p+1)) ≍ p^{−2} for consecutive primes, so the radius must be
  O(p^{−2}), not o(p^{−1}).
- **(D4) The citation carrying the continuity of f is out of scope.** F's continuity at points of N_p
  cites "packet indiscreteness — face (a)". The record proves face (a) for **admissible** E; the
  witness lives in the non-admissible E-free system. Both verifiers supplied E-free proofs
  (different ones); I re-derived the statement myself in §3.3 below, and it is true.
- Additionally **(D5)**, minor and internal to verify-F: its (2.3) writes the angular term as
  "α_p r ∂_ψ" with ∂_ψ declared to be the coordinate field −y∂_x + x∂_y, then converts it to the
  *smooth* field α_p(−y∂_x + x∂_y) (an r has been dropped) and derives the linearization
  p^{−k}R(2πkλ). Under its own convention the field is α_p r(−y∂_x + x∂_y), which is C^1 but not
  C^∞ at the core and whose linearization has **no** rotation part (A_p = p^{−k}·Id). Both repairs
  are legal; both give a conformal return derivative and ε ≡ +1, so nothing downstream changes.

Nothing in F's §3.4 is *false*; the design is sound and original. But a construction is verified only
when its data are specified, and here they were not. **REPAIRED**, with the final construction
written out in §2.

### 0.2 S4: **PARTLY S4-shaped** — and the partial credit is confined to arithmetic-free bookkeeping

I rule with verifier O against verifier F on the word, and with verifier F on the substance of what
the object is worth. The clause table is §5. Summary:

**Met:** compact; metrizable; covering dimension 3; **exactly one closed orbit of least period log p
for every prime and no others, no fixed points**; each such orbit **simple in [ALKL]'s sense with
ε ≡ +1**; and — after O's §3.7 repair, which I verified at the source and which is stronger than
either refuter or verifier F saw — the **α = 1 leafwise datum**: with a *repelling* core of transverse
rate 1/2 the leafwise return derivative is p^{1/2}·O_k, so
det(−T_xφ^{k log p}|T_xF) = p^k, and the orbital side of a [Den05] (32)-type formula would read
Σ_p log p (Σ_{k≥1} δ_{k log p} + Σ_{k≤−1} p^k δ_{k log p}) = **T1 + T2 of ledger §3 exactly**. This is
precisely the local model [Den05] p. 33 prescribes for the arithmetic case ("the eigenvalues of
T_xφ^{log Np} on T_xF for x ∈ γ_p would therefore be complex conjugate numbers of absolute value
Np^{1/2}"). F's own sign (attracting core) gives the wrong weight; O's correction is right.

**Failed:** foliated space / Riemann-surface lamination "dim 3 in the lamination sense" —
**proved impossible** (§4.1, ratifying verify-F's Theorem B and sharpening it by leaf dimension);
S3/T3 archimedean data — **absent and structurally so** (no fixed points; the only invariant
accumulation set is a 2-torus, χ = 0, so even a repair that made it a preserved leaf would
contribute 0); invariant transverse measure of full support — fails across the accumulation;
leafwise trace formula with the T1 orbital side — no leafwise cohomology exists on Y.

**And the met clauses are the cheap ones.** I ratify verify-F's Theorem C (the map is inert) and
verify-O's Theorem O-3 (continuity is automatic), and add the decisive structural fact both missed
(§4.3): **the target Y₀ is itself not T1, hence not metrizable, hence not a foliated space.** So
residue (R-ii)'s framing — "Deninger's own printed E-free unitary system Y₀" as an S4 escape — is
wrong at the target, not only at the map. Y₀ is not a candidate S4 object; only a *source* can be.

**Verdict word: PARTLY.** "No" would suppress a real and source-confirmed positive (T1 + T2 with the
printed p^{1/2} local model, on a compact object). "Yes" is absurd. The honest sentence for the
record replaces ledger §14's "the first positive S4-shaped object in the program's record" with:

> A compact metrizable fixed-point-free flow whose closed-orbit data — one simple orbit of least
> period log p per prime, ε ≡ +1, leafwise return derivative p^{1/2}·O — reproduce T1 + T2 exactly,
> and which maps continuously and equivariantly onto one Deninger periodic orbit in every packet of
> the E-free unitary system. It is **not** a foliated space, it carries no leafwise trace formula,
> it has no archimedean datum, and the map into Y₀ is structurally inert (any compact
> prime-indexed clopen-decomposed flow admits one). It relocates S4's open part from the orbit
> spectrum to the foliated structure at the accumulation set and the archimedean leaf.

### 0.3 Two binding readings, ruled

**(J1) The E-free reading of Y₀ is the printed one — RULED, not left open.** Both verifiers left this
as a flagged judgment call. It is decidable from the text:
1. [x-03] p. 49: "Y₀ = X̌₀(S¹) ×_{ℚ>0} ℝ^{>0}. Here X̌₀(S¹) = X̌(S¹)/G where X̌(S¹) = colim_ℕ X̊(S¹)
   and X̊(S¹) is the subspace of X̊(C) consisting of points (x, P^×) with P^× : κ(x)^× → S¹ a unitary
   character." The same page writes the ambient as "X₀ = X̌₀(C) ×_{ℚ>0} ℝ^{>0}", and §8 opens by
   restating its conventions ("In this section C denotes the complex number field, and we take
   N₀ = ℕ"), i.e. it does not inherit p. 39's suppression.
2. **Decisive:** [x-03] p. 50, Thm. 8.2 and its proof. X̊(C)_per is defined with **no** E — "{(x,P^×)
   ∈ X̊(C) | κ(x) ≅ F̄_p for some p and ker P^× is finite}" — the closure is computed in X̊(C)
   ("Since X̊(S¹) is closed in X̊(C) the subspace X̌(S¹) is closed in X̌(C)"), and the density half
   proves that **every** point of X̊(S¹) is approximated, the proof taking an arbitrary prime ideal
   p of R (not necessarily maximal), i.e. including generic-point unitary characters. Under an
   E-restricted reading the printed equality X̌(C)_per = X̌(S¹) would be false.
3. [x-06] p. 12: "The closure is the subsystem obtained by **replacing** X̊(C)_E in the previous
   constructions **with** the subspace of pairs (x,P^×) with P^× : κ(x)^× → S¹ a unitary character."
4. The counter-anchor, [x-03] p. 39 "In the following observation we omit E from the notation",
   introduces *that observation* (the Arakelov-compactification paragraph running to the top of
   p. 40) and not §8.

**Robustness note (mine):** the witness does not actually depend on the notation. Under the
alternative definition of Y₀ as "the topological closure of the union of all periodic orbits coming
from closed points" (p. 49's own words), the trivial generic character 1_η lies in that closure —
the witness's own net P_p → 1_η (§3.2) exhibits it, and it is an instance of Thm. 8.2's density.
The reading is load-bearing only for the *ambient* in which the closure is taken; [x-03] p. 50 takes
it in the E-free X̌(C).

**(J2) The quotient topology on the E-free suspension.** [x-03] p. 59 defines the quotient topology
for admissible E: "We give X = X̌(C)_E ×_{ℚ>0₀} ℝ^{>0} and X₀ = X̌₀(C)_E ×_{ℚ>0₀} ℝ^{>0} the
quotient topologies." The E-free suspension receives the same recipe by analogy; [x-03] pp. 39–40
and [x-06] p. 11 both handle X₀ = X̌₀(C) ×_{ℚ>0} ℝ^{>0} as a topological dynamical system. Ratified
as the only reasonable convention, flagged as convention.

### 0.4 The next decidable question — stated in §6

Q-b″ as posed in ledger §14 ("whether that source lamination carries a trace formula with the T1
orbital side, and what Ω's contribution is") is **decided negatively and is retired**: the source is
not a lamination, so no leafwise trace formula is defined on it, and Ω is a point-set of the target,
not a term of anything. Its replacement, **Q-b‴**, is stated precisely in §6 with the two published
facts that already bound it.

---

## §1. The two reports: agreement, disagreement, rulings

**Agreed by both, and ratified by me** (each independently proved twice): the closed-orbit inventory
of Y; compactness, metrizability, covering dimension 3; joint continuity of the flow; that each N_p
is clopen in Y; the well-definedness, equivariance and continuity of f; that f(C_p) is a genuine
Deninger periodic orbit in Γ_p through a character in E_f, so [x-03] Thms. 5.2/6.1 certify it; the
absorption lemma; Ω's isotropy ℚ>0 and indiscreteness; that **Y is not a lamination**; that the S3
archimedean datum is absent; that the map carries no structure.

| # | Contested | verify-O | verify-F | Ruling |
|---|---|---|---|---|
| 1 | Verdict word | REPAIRED (D1–D3) | VERIFIED ("choices, not errors") | **REPAIRED** (§0.1; F's own text admits a choice that breaks the flow) |
| 2 | Non-primitive n_p / strand separation | a repair (D1a) | not needed (ℝ²-argument) | **F is right**: the ℝ²-coordinate's argument determines θ mod log p, so ι_p is injective irrespective of primitivity; O's bound 4/(p k_p) is true and harmless but unnecessary |
| 3 | α = 1 / T2 | new repair: repelling core, g′(0) = 1/2 ⟹ det = p^k | not seen; called the k ≤ −1 shape "unweighted … unless the α-weights are imposed" | **O is right, and confirmed at the source** ([Den05] p. 31 Rem. 7.6(4) and (34); p. 33 "absolute value Np^{1/2}") |
| 4 | "Not a foliated space" | argued (leaf dimension not locally constant; no product decomposition) | **proved** (Theorem B, uniform convergence of plaques vs. thin geodesic strips) | **F's proof is the one that stands**; I ratify it and sharpen it by leaf dimension (§4.1) |
| 5 | What the map buys | Theorem O-3 (continuity automatic) + Kolmogorov quotient {0} ∪ {1/p} | Theorem C (forced clopen shape + converse) | **Both correct; F's is strictly stronger.** I ratify both and add §4.3 (the target is not T1) |
| 6 | E-reading (J1) | both readings recorded | both readings recorded | **Ruled E-free** (§0.3) |
| 7 | S4 word | partly | no | **partly** (§0.2, §5) |

---

## §2. The final construction, written out

Everything in §2 is elementary geometry/ODE and consumes no source. I re-derived each item; where a
verifier's argument is the cleanest I say whose.

### 2.1 Data

Fix v = (1, β) ∈ ℝ², β irrational. For each prime p:
- n_p ∈ ℤ² an integer vector nearest to (log p)·v; v_p := n_p / log p, so |v_p − v| ≤ √2/(2 log p) → 0;
- θ_p ∈ T² = ℝ²/ℤ² arbitrary; w_p ∈ ℝ² a unit vector with w_p ⊥ v_p (a T²-direction);
- e(θ) := (cos(2πθ/log p), sin(2πθ/log p)) ∈ ℝ²;
- a radius ε_p with **0 < ε_p ≤ 1/(4p(p+1))**  (2.1)
  (this alone suffices for everything in §2.2–2.5 and §3; the *additional* bound
  ε_p ≤ 1/(4p|n_p|) is used only by Theorem B in §4.1, and I keep it: **ε_p ≤ min{1/(4p(p+1)), 1/(4p|n_p|)}**).

**Embedding (the rank-2 normal frame — repair D2).** For (θ, x, ρ) ∈ (ℝ/(log p)ℤ) × ℝ²,
> **ι_p(θ, x, ρ) := ( θ_p + θ v_p + x·w_p , (1/p + ρ)·e(θ) ) ∈ T² × ℝ².**  (2.2)

Put V := {(θ,x,ρ) : x² + ρ² ≤ ε_p²}, **N_p := ι_p(V)**, **C_p := ι_p({x = ρ = 0})**, and
> **Y := (T² × {0}) ∪ ⋃_p N_p ⊂ T² × ℝ².**

*ι_p is an embedding on V.* The argument of the ℝ²-coordinate determines θ mod log p exactly; its
modulus determines ρ (as ε_p < 1/p, the modulus 1/p + ρ > 0 is injective in ρ); the T²-coordinate
then determines x·w_p with |x| ≤ ε_p < 1/2, hence x. Injective and continuous on a compact set,
hence an embedding; N_p is an embedded solid torus (a 3-manifold with boundary), C_p an embedded
circle. **Primitivity of n_p is irrelevant** (ruling 2 above).

*Disjointness.* The ℝ²-modulus on N_p lies in [1/p − ε_p, 1/p + ε_p], and for p < q,
1/p − 1/q ≥ 1/(p(p+1)) > ε_p + ε_q by (2.1); and N_p ∩ (T² × {0}) = ∅. (Repair D3.)

### 2.2 The flow

*On T² × {0}:* ψ^t(θ,0) = (θ + tv, 0). No fixed points; no closed orbits (tv ∈ ℤ² with t ≠ 0 would
make β rational).

*On N_p,* in the coordinates (θ, r, ψ) with (x, ρ) = ε_p r(cos ψ, sin ψ), r ∈ [0,1]:
> **Z_p := ∂_θ + a_p(r)·∂_ψ + g(r)·∂_r,  a_p(r) := (2π/log p)·λ,  g(r) := ½·r(1 − r²)**  (2.3)
> with λ a fixed irrational number.

(Repair D1.) Both coefficient functions are smooth and the Cartesian form
a_p(−y∂_x + x∂_y) + ½(1 − x²−y²)(x∂_x + y∂_y) is smooth on the disc, tangent to ∂V at r = 1
(g(1) = 0), so Z_p generates a unique global flow φ_p on the compact V, transported to N_p by ι_p.
Two admissible variants, both used in the record and both fine: a_p constant (rotation rate λ·2π/log p
at the core, return derivative p^{1/2}R(2πkλ)) or a_p(0) = 0 with a_p(1) ≠ 0 irrational (return
derivative p^{k/2}·Id). *The sign of g is O's repair and is the one that matters* (see §2.6).

*On Y:* φ^t := ψ^t on T² × {0} and φ_p^t on N_p. Each piece is invariant.

### 2.3 Topology

- **Compact, metrizable.** Y is bounded and closed in T² × ℝ² (a limit of points from infinitely many
  distinct N_p has ℝ²-modulus ≤ lim(1/p + ε_p) = 0, hence lies in T² × {0}); a closed bounded subset
  of a compact metric space.
- **Each N_p is clopen in Y**; T² × {0} is closed and **not** open (dist(N_p, T²×{0}) ≤ 1/p → 0, and
  the T²-projection of C_p is 1/(2|m_p|)-dense where m_p is the primitive part of n_p, with
  |m_p| → ∞ — verify-F's argument, ratified: if m_p stayed in a finite set along a subsequence then
  dist((log p)v, ℝm_p) = (log p)·dist(v, ℝm_p) → ∞ would contradict |(log p)v − n_p| ≤ √2/2).
- **Covering dimension 3** (countable closed sum theorem; N_2 contains a 3-ball). This is *not*
  "dimension 3 in the lamination sense" (§4.1).

### 2.4 Joint continuity of the flow (verify-F's formula argument; ratified and re-derived)

At (t,y) with y ∈ N_p: N_p is clopen and φ_p is the flow of a smooth field on a compact manifold with
boundary. At (t,y) with y = (θ,0): let (t_k,y_k) → (t,y) with y_k ∈ N_{p_k}, p_k → ∞ (any other case
is the torus flow). Writing y_k = ι_{p_k}(θ_k, x_k, ρ_k), the θ-coordinate advances at unit rate, so
by (2.2)
  pr_{T²}φ^{t_k}(y_k) − pr_{T²}(y_k) = t_k v_{p_k} + (x_k′ − x_k)w_{p_k},  |x_k|,|x_k′| ≤ ε_{p_k},
which → tv, while the ℝ²-modulus stays ≤ 1/p_k + ε_{p_k} → 0. Hence φ^{t_k}(y_k) → (θ + tv, 0). ∎
**This is exactly what the cabling is for:** the tube's θ-advance is carried to a T²-translation by
t·v_p → t·v, so the tube flows converge to the linear flow and the limit is not stationary.

### 2.5 Closed orbits — THEOREM A (both verifiers; ratified)

*The closed orbits of (Y, φ) are exactly the cores C_p, p prime, C_p of least period log p; there are
no others and no fixed points.* Proof: a closed orbit lies in one invariant piece. T² × {0}: none.
N_p: θ̇ = 1 forces any period into (log p)ℤ_{>0}; on 0 < r < 1, ṙ = g(r) has a fixed sign so r is
strictly monotone — no closed orbit; on r = 1 the flow is θ̇ = 1, ψ̇ = a_p(1) on a torus and closes
only if a_p(1)·log p/2π ∈ ℚ, excluded; on r = 0 the core closes with least period log p (injectivity
of θ ↦ ι_p(θ,0,0) on [0, log p)). ∎ Least periods log p are pairwise distinct, so **exactly one
closed orbit per prime, of length log p, and nothing else**.

**Lemma O-2a** (verify-O; re-derived and correct): in a compact metrizable fixed-point-free flow,
isolated closed orbits force finitely many closed orbits of least period ≤ T for every T. Here the
count is π(e^T), the T1 counting function.

### 2.6 What the pieces carry: the local ALKL/[Den05] datum with ε ≡ +1 and α = 1

On N_p take **F_p := the meridian-disc foliation {θ = const}**: 2-dimensional leaves (discs, trivially
Riemann surfaces), transverse to the flow, φ^t(D(θ)) = D(θ + t) — an F-compatible foliated flow with
**no preserved leaves** ([Den05] §7.3 p. 30; [ALKL] p. 1: "A flow φ = {φ^t} on M is said to be
foliated if it maps leaves to leaves"). Linearizing the disc return map at the core after time
k log p gives the conformal map
> **A_p^k = e^{k g′(0) log p}·O_k = p^{k/2}·O_k,  O_k ∈ SO(2),**
since g′(0) = ½ by (2.3). Consequences, each checked against the source:
- **Simple** in [ALKL]'s sense (p. 3, verbatim): "The condition on c to be simple means that
  id − φ_*^{kℓ(c)} : T_pF → T_pF is an isomorphism for any p ∈ c and k ∈ ℤ^×, whose determinant is
  independent of p, and its sign denoted by ε_c(k)." Here det(id − p^{k/2}O_k) = |1 − p^{k/2}e^{iϑ}|²
  > 0 for k ≠ 0. **ε_{C_p}(k) = +1 for all k ∈ ℤ^×.**
- **α = 1.** [Den05] p. 31, Rem. 7.6(4): "Assuming we are in such a situation and that F is
  2-dimensional, we have: |det(T_xφ^{kl(γ)} | T_xF)| = e^{kl(γ)} for x ∈ γ, k ∈ ℤ"; and (34):
  the k ≤ −1 coefficient of (32) equals ε_γ(|k|)det(−T_xφ^{kl(γ)}|T_xF) = ε_γ(k)|det(T_xφ^{kl(γ)}|T_xF)|.
  Here |det A_p^k| = p^k = e^{k log p} ✓. So the orbital side of a [Den05] §7.5-type formula would be
  **Σ_p log p (Σ_{k≥1} δ_{k log p} + Σ_{k≤−1} p^k δ_{k log p}) = T1 + T2** (ledger §3 lines 69–70).
- This is the printed arithmetic prescription: [Den05] p. 33, "In the number theoretical case the
  eigenvalues of T_xφ^{log Np} on T_xF for x ∈ γ_p would therefore be complex conjugate numbers of
  absolute value Np^{1/2}. If they are real then T_xφ^{log Np} would simply be multiplication by
  ±Np^{1/2}." The repaired core realizes exactly this.
- **Invariant transverse measure** on the piece: dθ on the leaf space ℝ/(log p)ℤ (trivial holonomy).
- **Why this is not obstructed here although R11 says it is on manifolds.** [Den05] p. 23, Rem. 2 to
  Cor. 5.5: "Actually the conditions of the corollary force α = 0 i.e. the flow must be isometric" —
  the conditions being a **compact 3-manifold** with a surface foliation **having a dense leaf** and a
  conformal transverse flow. N_p is a manifold with boundary whose leaves are discs, none dense; the
  obstruction does not reach it. The α = 1 datum is bought by *locality*, not by any new phenomenon.

**Honest weight of §2.6:** g′(0) = ½ is a free real parameter of the design, dialed to the target.
Nothing derives it. What the section establishes is that the T1 + T2 orbital data are *realizable*
on a compact object in the topological-dynamics category — which the record had not exhibited before
— not that anything explains them.

---

## §3. The target, and the map f : Y → Y₀

Notation: X₀^full := X̌₀(ℂ) ×_{ℚ>0} ℝ>0 and Y₀ := X̌₀(S¹) ×_{ℚ>0} ℝ>0, both with the quotient
topology of the product ([x-03] p. 59 recipe; J2), Q the quotient map, which is **open** (orbit map:
Q^{−1}(Q(U)) = ⋃_q U·q).

### 3.1 The orbits γ̃_p and the character (re-derived)

Fix a closed point x_p over (p) and the injective character χ_p : F̄_p^× ↪ μ(ℂ) of [x-03] p. 32; let
L_p be the prime-to-p part of lcm(1, …, p^p), ν_p := L_p², **P_p := F_{ν_p}(x_p, χ_p) = (x_p, χ_p∘( )^{ν_p})**.
- ker(P_p^×) = μ_{ν_p}(F̄_p), of order ν_p (p ∤ ν_p): **finite kernel**, so P_p ∈ **E_f**, hence in
  every admissible E ⊇ E_f, and (Tors) holds ([x-03] p. 27 verbatim: "(Tors) the group ker(χ)_tors =
  ker(χ|_{μ(κ)}) is finite and |(ker χ)_tors| ∈ ℕ₀").
- Values are roots of unity: **P_p is unitary**, so π(P_p) ∈ X̌₀(S¹) and
  **γ̃_p := {[π(P_p), u] : u > 0} ⊂ Γ_{(p)} ∩ Y₀**.
- Isotropy exactly p^ℤ, so γ̃_p is a periodic orbit of least period log p ([x-03] p. 38: "all ℝ>0-orbits
  in Γ_{x₀} are circles ℝ>0/N x₀^ℤ"; Thm. 6.1 p. 39: "For any point x₀ ∈ Γ^E_{x₀} the isotropy group
  … is (ℝ>0)_{x₀} = N x₀^ℤ"; and p. 38 "If e.g. E_f ⊂ E then Γ^E_{x₀} = Γ_{x₀}"). The isotropy is
  E-independent because the E-locus is ℚ>0-invariant ([x-03] Prop. 4.2 p. 27), so the equation
  F_qP₀ = P₀ has the same solutions computed in X̌₀(ℂ)_E or in X̌₀(ℂ) — verify-O's one-line
  justification, ratified.
- γ̃_p is the orbit through π(χ_p) itself ([π(P_p),u] = [π(χ_p), ν_p u]); ν_p is needed only for §3.2.

### 3.2 P_p → 1_η, and Ω (re-derived)

1_η := (η, 1), the trivial unitary character of ℚ̄^× (a point of X̊(S¹) by [x-03] Remark 3.4 p. 23 and
the p. 49 definition; (Tors) fails, ker = μ_∞). For r ∈ ℤ̄ ∖ {0} of degree f: r ∈ 𝔭_{x_p} forces
p | N_{ℚ(r)/ℚ}(r) ≠ 0, so only finitely many p; otherwise ord(r̄) | p^{f′} − 1 with f′ ≤ f, is prime
to p and < p^p for p ≥ f, hence divides L_p | ν_p, and P_p(r) = χ_p(r̄)^{ν_p} = 1. So P_p → 1_η
pointwise, i.e. in X̊(ℂ) ([x-03] p. 40: the topology of pointwise convergence on ℤ̄, metrizable).
F_q(1_η) = 1_η for all q, so **Ω := {[π(1_η), u] : u > 0} ≅ ℝ>0/ℚ>0** is a single ℝ-orbit with
isotropy the dense group ℚ>0 — not a fixed point, not a circle. This is exactly the pathology
(Tors) exists to remove ([x-03] p. 37: "(Tors) does force the points P₀ ∈ X̌₀(C)_E over
characteristic zero points of X₀ to have trivial stabilizer"; [x-06] p. 11: "In general, the
dynamical system (X₀, φ^t) has too many periodic orbits … What we know for certain is that the
restrictions of P^× to μ(κ(x)) must have finite kernels").

### 3.3 The two topological inputs, re-derived by me

**(a) Ω is indiscrete.** Q^{−1}(U) ⊇ W₀ × (a,b) ∋ (π(1_η), u₀); for any u pick q ∈ ℚ>0 ∩ (u/b, u/a);
then (F_qπ(1_η), q^{−1}u) = (π(1_η), q^{−1}u) ∈ W₀ × (a,b), so [π(1_η), u] ∈ U. ∎

**(b) γ̃_p is indiscrete in X₀^full — E-FREE (repair D4).** Let U ∋ [π(P_p), u₀] be open;
Q^{−1}(U) ⊇ W₀ × (a,b). Since π̌ is continuous and X̊(ℂ) is open in X̌(ℂ) ([x-03] Prop. 7.4a p. 43),
π̌^{−1}(W₀) ∩ X̊(ℂ) contains a basic set V = {P : |P(r_j) − P_p(r_j)| < ε, j ≤ k} with
r_j ∈ ℤ̄ ∖ 𝔭_{x_p} (test elements inside 𝔭_{x_p} impose nothing: every point over x_p kills them).
All candidate values are roots of unity of order dividing M := lcm_j ord(r̄_j) (prime to p), so it
suffices to achieve *equality* of values. Which translates stay in the first chart? By (51)
([x-03] p. 42: "F_ν(X̊(C)) = {P ∈ X̊(C) | P(μ_ν(K)) = 1}"), for q = m/n in lowest terms
F_qP_p ∈ X̊(ℂ) iff the prime-to-p part of n divides mν_p; in particular **q = m/p^j always works**,
because F̄_p^× has no p-torsion, so ( )^{p} is an automorphism of it (elementary; checked here, not
cited). Then F_{m/p^j}P_p = (x_p, χ_p∘( )^{ν_p m p^{−j}}), whose value at r_j equals P_p(r_j) as soon
as **m ≡ p^j (mod M)**. For fixed j these q form an arithmetic progression scaled by p^{−j}, with
gaps M p^{−j} → 0, hence are dense in ℝ>0. Choose one with q^{−1}u ∈ (a,b); then
[π(P_p), u] = [F_qπ(P_p), q^{−1}u] ∈ U. ∎
*(This is verify-O's Lemma O-5; verify-F proves the stronger statement for the whole packet Γ_p by
the same inverse-Frobenius mechanism. I re-derived this version line by line; it is correct, and it
uses no (Tors) anywhere.)*

**(c) Uniform absorption (refuter F §3.2; both verifiers; re-derived by me).** *If U ⊂ X₀^full is
open and meets Ω, there is p₀ with γ̃_p ⊂ U for all p ≥ p₀.* By (a), U ⊇ Ω, so Q^{−1}(U) ⊇ W₀ × (a,b)
∋ (π(1_η), 1) and π̌^{−1}(W₀) ∩ X̊(ℂ) ⊇ V = {P : |P(r_j) − 1| < ε}. Fix an integer N₀ > 2/(1/a − 1/b)
and p₀ with: p > N₀ (so N₀ | L_p | ν_p), p ≥ deg r_j and p ∤ N(r_j) for all j. For p ≥ p₀ and
u′ ∈ [1, p), the interval (N₀u′/b, N₀u′/a) has length > 2 and contains an integer m; put q := m/N₀,
so q^{−1}u′ ∈ (a,b). Then F_qP_p = F_{mν_p/N₀}(x_p, χ_p) ∈ X̊(ℂ) with value
χ_p(r̄_j)^{mν_p/N₀} = 1 (as ord(r̄_j) | L_p | ν_p/N₀). Hence [π(P_p), u′] ∈ U, and u′ ∈ [1,p)
exhausts γ̃_p. ∎ **Every step verified against the printed pages cited.**

### 3.4 The map

Choose a base point on each orbit (axiom of choice) and set f(φ^t y_O) := [π(P_p), e^t] for orbits
O ⊂ N_p, f(ψ^t y_O) := [π(1_η), e^t] for orbits O ⊂ T² × {0}. Well defined (on C_p because
e^{log p} = p lies in the isotropy; elsewhere because the orbits are injective lines), **equivariant**
by construction, **f(C_p) = γ̃_p ⊂ Γ_p** bijectively, **f(T²×{0}) = Ω**.
**Continuity:** on N_p (clopen) the image lies in the indiscrete γ̃_p, so preimages of opens are ∅ or
N_p; at y ∈ T² × {0}, for U ∋ f(y) open, (a) gives U ⊇ Ω and (c) gives U ⊇ γ̃_p for p ≥ p₀, so
f^{−1}(U) ⊇ Y ∖ ⋃_{p<p₀} N_p, open. Since X̌(S¹) is closed and ℚ>0-invariant in X̌(ℂ) ([x-03] p. 50:
"Since X̊(S¹) is closed in X̊(C) the subspace X̌(S¹) is closed in X̌(C)"), Q^{−1}(Y₀) is saturated and
Y₀'s quotient topology is its subspace topology, so f : Y → Y₀ is continuous. ∎

**§3 verdict: item (2) of the brief holds in full, E-free, with the citation gap closed.**

---

## §4. What Y is not, what Y₀ is not, and what f buys

### 4.1 Y is not a foliated space — Theorem B ratified and sharpened

The definition the program uses ([Den05] §7.1 p. 28, verbatim; quoted in `s2-feasibility-note` §3.1):
"Consider a separable metrizable topological space X with a covering by open sets U_i and
homeomorphisms φ_i : U_i → F_i × T_i with F_i open in ℝ^d … a φ_j∘φ_i^{−1}(x,y) = (f_{ij}(x,y),
g_{ij}(y)); b All partial derivatives D_x^α f_{ij}(x,y) exist and are continuous as functions of x
and y."

**Theorem B (verify-F §2.6; I re-derived every step and ratify it).** Y admits no foliated-space
structure with **2-dimensional** leaves, for any choice of foliation on the pieces. Proof sketch as
verified: plaques are connected and each N_p is clopen, so every plaque lies in T² × {0} or in one
N_p; a chart at y₀ ∈ T² × {0} has its plaque in the torus, and nearby plaques in N_{p_k} with
p_k → ∞; joint continuity on a compact F̄ × ({t_k} ∪ {t₀}) gives **uniform** convergence
h(·,t_k) → h(·,t₀); a small round circle γ ⊂ F̄ maps to a Jordan curve J in the torus bounding a
Jordan domain containing a disc of radius 3δ, hence J is not within δ of any straight segment
(a Jordan domain lies in the convex hull of its boundary, and a δ-neighborhood of a segment is
convex of width 2δ); but h(γ, t_k) ⊂ N_{p_k} projects into the ε_{p_k}-strip around a closed
geodesic whose passes through a disc of radius ¼ are separated by 1/|m_{p_k}| > 4ε_{p_k}, so the
connected projection lies in one straight band — contradiction. ∎

**Sharpening (mine), by leaf dimension.** d = 3 is impossible by invariance of domain (the plaque
through y₀ would embed an open subset of ℝ³ in the 2-manifold T² × {0}); d = 0 is impossible (Y
contains a 3-ball, not totally disconnected); d = 2 is Theorem B. **d = 1 is possible** — a
fixed-point-free continuous flow on a compact metric space has flow boxes, so the orbit partition is
a 1-dimensional foliated structure — but it is not the S4 clause and is worthless for the trace
formula: [Den05] (32) sums over "closed orbits **not contained in a leaf**", and with d = 1 every
closed orbit *is* a leaf, so the orbital side is empty; and α = 1 needs dim F = 2 ([Den05] p. 31
Rem. 7.6(4)). So the correct statement is: **Y carries no foliated structure of the kind S4 requires,
and the only one it does carry is trace-formula-empty.**

**Record correction, binding.** Ledger §14's "refuter F strengthens the source to a compact metrizable
3-dimensional **lamination** (torus + cabled solid tori)" and this task's brief's "source lamination"
are **wrong** and must be struck. Refuter F said so himself (face-b-refuter-F §3.5(i): "Y is not a
lamination in the local-product sense"); both verifiers proved it; I ratify.

### 4.2 f collapses, and is injective only along the cores

f maps the **whole 2-torus** — a 2-dimensional compact minimal set, every orbit dense — onto the
single orbit Ω, each single torus orbit already surjecting onto Ω (via ℝ ↠ ℝ>0 ↠ ℝ>0/ℚ>0). Ω is not
a point, not a circle, not a leaf image; it is an indiscrete set of continuum cardinality. Each
3-dimensional N_p collapses onto the circle γ̃_p. f is injective exactly on each core, and even there
it is a continuous bijection C_p → γ̃_p that is **not** a homeomorphism (γ̃_p is indiscrete). f is
nowhere locally injective, nowhere open, nowhere an embedding.

### 4.3 The target is not T1 — THEOREM T (adjudicator; new)

> **Theorem T.** Let Z be any topological space with a ℚ>0-action by homeomorphisms and let
> X = (Z × ℝ>0)/ℚ>0 with (z,u)·q = (qz, q^{−1}u) carry the quotient topology. Suppose z ∈ Z has a
> ℚ>0-orbit with compact closure (in particular, suppose z is a fixed point of the action, or Z is
> compact). Then the ℚ>0-orbit of (z,u) is **not closed** in Z × ℝ>0, so the point [z,u] is not
> closed in X: **X is not T1**, hence not metrizable, hence **not a foliated space** in the
> [Den05] §7.1 sense and not a Riemann surface lamination.
>
> *Proof.* Pick v ∈ ℝ>0 ∖ uℚ>0 (possible: uℚ>0 is countable). Pick q_n ∈ ℚ>0 with q_n → u/v, so
> q_n^{−1}u → v. By compactness of the orbit closure, a subnet has q_{n_j}z → w. Then
> (q_{n_j}z, q_{n_j}^{−1}u) → (w, v), whose second coordinate is not in uℚ>0, so (w,v) is in the
> closure of the orbit and not in it. Since Q^{−1}([z,u]) is exactly that orbit, [z,u] is not a
> closed point. ∎

**Corollary T1 (the target).** Y₀ is not T1: take z = π(1_η), whose ℚ>0-orbit is a single point
(F_q(1_η) = 1_η), so the orbit of (π(1_η), u) is {π(1_η)} × uℚ>0, whose closure contains
{π(1_η)} × ℝ>0. **Y₀ is not metrizable and is not a foliated space / Riemann-surface lamination.**
Deninger's §8 already shows Y₀ is the *wrong* object for another reason — p. 49: "In this section we
will show that the system Y₀ is **still infinite-dimensional**" — i.e. §8 is a negative result about
the closure idea, not a proposal. Theorem T adds that Y₀ fails the ambient category too.

**Corollary T2 (the design shape).** No ℚ>0-suspension of a **compact** base is T1. So the S4 object
cannot be built as Z ×_{ℚ>0} ℝ>0 with Z compact — Deninger's own construction shape is incompatible
with the compact-metrizable-foliated-space requirement, and this is independent of dimension, of E,
and of all arithmetic. It also explains, in one line, the scare quotes in [x-06] p. 11 ("The
1-codimensional 'foliation' F") and the packet-indiscreteness phenomenon that face (a) and both
verifiers proved by hand: a packet character's ℚ>0-orbit has values in fixed finite sets of roots of
unity, hence relatively compact orbit closure, and Theorem T applies.

**Consequence for residue (R-ii), binding.** The residue was framed as "Deninger's own printed E-free
unitary system Y₀ … the first positive S4-shaped object". Y₀ is not an S4-shaped object at all:
it is not T1. What exists is a compact **source** with the right orbit data and an inert map into
Y₀. R-ii must be rewritten accordingly.

**[NOVELTY — dual-model check 2026-09-03]** **Theorem T (C2): PARTIAL.** The criterion "T₁ ⟺ orbits closed" is definition-level and printed (Yokoyama arXiv:2012.00849 Lemma 7.2 proof: a point of the orbit space "is S₁ if and only if O(x) is closed with respect to the quotient topology"; Akin–Auslander arXiv:1004.0323 Thm 6.3, closed orbit relation ⟹ Hausdorff quotient). The same question is on Deninger's page with the **opposite** answer for the adelic base: [x-03] p. 64 Remark "By [LR00, Lemma 3.1], the orbits of the ℚ^{>0}-action on ℚ^{>0}Ẑ^× × ℝ^{>0} are closed … Y is a T₁-space" — Laca–Raeburn, Math. Ann. 318 (2000) = arXiv:math/9911134 Lemma 3.1 "If u is an invertible adele, then the orbit ℚ*u is closed in 𝔸" (proof uses the non-compact adelic base: "(r_n − r_m)u ∈ ∏_p ℤ_p implies r_n − r_m ∈ ℤ"). Also printed: [x-03] p. 49 "not properly discontinuous", p. 61 coarse quotient, p. 63 non-homeomorphism. New: the uniform relatively-compact-orbit statement for any ℚ^{>0}-space Z, and Y₀ not T₁ / not metrizable / not a foliated space; no source states either. Say explicitly that Theorem T and the p. 64 Remark do not conflict (compact profinite base versus adelic base). Record: `results/c3-r/s14/novelty/adjudication.md` §2 C2.

### 4.4 The map is inert — Theorems O-3 and C ratified

- **verify-O Theorem O-3:** *any* function g : Y → X₀^full with g(N_p) ⊂ γ̃_p and g(T²×{0}) ⊂ Ω is
  continuous — continuity uses neither the flow nor equivariance. Re-derived; correct.
- **verify-F Theorem C:** for any compact space with a continuous ℝ-action and any continuous
  equivariant f into Y₀: (i) Y = Y_η ⊔ ⨆_p Y_p with Y_p := f^{−1}(Y₀(p)) clopen and, if infinitely
  many packets are met, Y_η ≠ ∅ by compactness; (iii) conversely every compact fixed-point-free flow
  with such a clopen decomposition and the trivial period bookkeeping (periods in (log p)ℤ on Y_p,
  in log ℚ>0 on Y_η) admits such a map. Its Lemma D (Y₀(p) = V_p ∩ Y₀ clopen, with
  V_p = Q(π̌({|P(p)| < ½}) × ℝ>0) open by openness of π̌ ([x-03] p. 43) and of F_q (Prop. 7.4b), and
  |P(p)| ∈ {0,1} on ℚ>0-translates of unitary points) I re-derived and ratify.
- **Therefore:** "there is a continuous flow-equivariant map from a compact source into Y₀ hitting a
  genuine periodic orbit in every packet" is *equivalent to* "the source is compact,
  fixed-point-free, and decomposes into clopen prime-indexed pieces with the right periods". It
  transports no leafwise, transverse, cohomological or conformal datum in either direction — and by
  §4.3 there is no such datum on the target to transport. **The map's entire content is the
  bookkeeping.**

*(One clause of verify-F's Theorem C, part (ii) — f(Y_η) lands in {W = ∞} — rests on the face-(b)
W-machinery, which I did not re-derive. It is not load-bearing for anything above. I also note it
cannot be strengthened to "Y₀(η) is entirely (Tors)-violating": ℚ̄^× is divisible and S¹ is an
injective ℤ-module, so unitary generic characters with finite μ-kernel exist.)*

---

## §5. S4, clause by clause

Specification: ledger §8, row S4 (read verbatim this session) — "a compact foliated space /
Riemann-surface lamination Y₀ (dim 3 in the lamination sense), with (per §3): one simple closed
orbit of length log p per prime with ε ≡ +1, the S3 fixed-point data at the archimedean place,
α = 1 leafwise conformal structure, and a transverse measure making the counting exact" — together
with [x-03] p. 40's question, verbatim: "Is there a sub-dynamical system Y₀ ⊂ X₀ … **or at least one
which maps to X₀** such that dim Y₀ = 2d + 1 … and such that Y₀ contains at least one periodic orbit
in Γ_{x₀} for every closed point x₀ of X₀? If d = 1, is there such a Y₀ which is a Riemann surface
lamination in the sense of [Ghy99]?" (no occurrence of "compact"), and [ALKL] p. 1: "Assume M is
closed, codim F = 1, the closed orbits are simple, the preserved leaves are transversely simple, and
φ is transverse to the non-preserved leaves."

| Clause | Status on the repaired Y | Grade |
|---|---|---|
| compact, metrizable | proved (§2.3) | **MET** |
| dimension 3 | covering dimension 3 (§2.3) — **not** "dim 3 in the lamination sense" | MET in the weak sense only |
| foliated space with 2-dim leaves / Riemann-surface lamination ([Den05] §7.1; ALKL H1–H2) | **no such structure exists** (§4.1, proved); pieces are manifolds with boundary; d = 1 possible but trace-formula-empty | **FAILS (proved)** |
| foliated flow (H3) | holds on each N_p with the disc foliation; vacuous on Y | fails globally |
| exactly one closed orbit of length log p per prime, none other, no fixed points | Theorem A (§2.5) | **MET** |
| closed orbits simple, ε ≡ +1 (H4a) | A_p^k = p^{k/2}O_k, det(id − A_p^k) > 0 (§2.6) — relative to the piece's foliation | **MET on the pieces**, undefined globally |
| α = 1 leafwise conformal ⟹ T2 weights | |det A_p^k| = p^k = e^{k log p} ([Den05] p. 31 Rem. 7.6(4), (34)); orbital side = T1 + T2 exactly | **MET on the pieces** (dialed, not derived) |
| invariant transverse measure, counting exact (H6; R15) | dθ on each piece; no extension across the accumulation, so not of full support | fails globally |
| S3 archimedean / preserved leaf, transversely simple, κ_L (H4b; T3) | no fixed points; no preserved leaf; the only invariant accumulation set is T² with χ = 0, so even as a leaf it would contribute 0 | **FAILS, structurally** |
| leafwise trace formula with the T1 orbital side (S1/S2 on the object) | no leafwise cohomology on Y (no F); [ALKL] needs a closed manifold; [Den05] §7.5 needs a compact smooth solenoid | **FAILS** |
| maps equivariantly into a Deninger space, reaching every packet ([x-03] p. 40's second alternative) | yes, into the E-free Y₀ (§3) | **MET, and inert** (§4.4) |
| the target is itself an S4-type object | **no**: Y₀ is not T1 (§4.3), and [x-03] p. 49 proves it "still infinite-dimensional" | **FAILS at the target** |

**s4_shaped = PARTLY.** Everything met is the orbit/weight bookkeeping, realizable by design with no
arithmetic input; everything with geometric content fails, two clauses provably.

---

## §6. The next decidable question (Q-b‴), and why it is the right one

Q-b″ is retired (§0.4). The genuinely open point, isolated by both verifiers and sharpened here by
two printed facts, is **whether the infinite-rank orbit-length spectrum and the foliated structure
can coexist on a compact object**. What is already known:

- **On compact 3-manifolds it cannot.** [Den05] p. 23, Remark 3 to Cor. 5.5, verbatim: "One can show
  that the group generated by the lengths of closed orbits is a **finitely generated** subgroup of ℝ
  under the assumptions of the corollary" (compact 3-manifold, foliation by surfaces with a dense
  leaf, non-degenerate F-compatible flow everywhere transverse, conformal). The group generated by
  {log p : p prime} is free abelian of infinite rank.
- **In the only class where the foliated trace formula is a theorem it cannot either.** [Den05] §7.7
  (pp. 34–35): for the suspension X = M̄ ×_Λ ℝ of a profinite tower over a compact manifold with
  Λ = lℤ, "The map γ ↦ γ_M = γ ∩ (M̄ ×_Λ Λ) gives a bijection between the closed orbits γ of the flow
  on X and the finite orbits γ_M of the f̄- or Λ-action … We have: **l(γ) = |γ_M| l**." So every
  closed-orbit length is an integer multiple of a single l, and the length group is **cyclic** — of
  ℚ-rank 1. **Theorem (adjudicator, immediate from the quoted line): no [Den05] §7.7 suspension
  solenoid has closed-orbit length spectrum of ℚ-rank ≥ 2, a fortiori none has {log p}.** Hence the
  S4 object, if it exists, lies strictly outside the class in which S1 ("Trace formula on smooth
  solenoids … EXISTS", ledger §8) is proved; S1's "TRANSFERS" must be read as "the machinery
  transfers", never as "the theorem covers the needed object".
- **Refuter F's Y shows the spectrum is achievable if the foliated structure is dropped** (§2.5),
  and Theorem B shows this particular Y is not repairable into a foliated space.
- **Theorem T (§4.3) closes off the obvious design:** no ℚ>0-suspension of a compact base can be the
  object, because it is never T1.

> **Q-b‴ (next decidable).** Does there exist a **compact** foliated space (X, F) of dimension 3 with
> 2-dimensional leaves ([Den05] §7.1–7.2 — in particular separable metrizable) carrying an
> F-compatible flow φ, transverse to F, whose closed orbits are all simple and whose **length group
> has infinite ℚ-rank**?
> **Q1** — the bare question above (no prime structure). **Q2** — Q1 with exactly one closed orbit of
> least period log p for each prime and no others. **Q3** — Q2 with ε ≡ +1 and leafwise return
> derivative p^{1/2}·O ([Den05] p. 33's printed prescription; §2.6 shows it is free once the pieces
> exist). **Q4** — Q3 with a preserved leaf L, χ(L) ≠ 0, transversely simple with κ_L = −2 (the T3
> datum; O's Euler-characteristic constraint: a torus limit set contributes 0, so any repair must
> change the limit set, not thicken it).

Q1 is the smallest and is a pure foliated-dynamics question with no arithmetic in it; it is
publishable either way; and by the two facts above the answer is NO for compact 3-manifolds and NO
for §7.7 suspensions, so a YES needs a genuinely new class of compact solenoid, while a NO would
**close S4 outright** and with it Route 2. Two subsidiary items, both decidable and both cheap:
(i) verify-F's §5.4(a) Lefschetz obstruction (a mapping torus of a closed surface cannot have exactly
one simple closed orbit — complete for h ≃ id on every surface and for S², T² on every h; genus ≥ 2
with h_* of spectrum {1,1} ∪ μ_{2g−2} left open) — this is a first instalment of "NO" for Q2 in the
global-cross-section sub-case, and finishing it is a bounded task; (ii) whether [Ghy99]'s "Riemann
surface lamination" includes compactness and Hausdorffness — needed to state Deninger's p. 40
question exactly; the source is not on disk ([RU]).

---

## §7. Novelty ledger — everything below is **[novelty: single-check]** unless marked

1. **Theorem T and Corollaries T1, T2** (§4.3, adjudicator, new this session): a ℚ>0-suspension of a
   base with a relatively compact orbit is never T1; hence **Y₀ is not metrizable and not a foliated
   space**, and no ℚ>0-suspension of a compact base can be the S4 object. Explains packet
   indiscreteness and Deninger's scare quotes uniformly. *This is the item that changes the reading
   of residue (R-ii): the failure is at the target, not only at the map.*
2. **The §7.7 length-spectrum theorem** (§6, adjudicator, new): l(γ) = |γ_M|·l ([Den05] p. 35)
   ⟹ every §7.7 suspension solenoid has cyclic closed-orbit length group, so the class in which S1
   is proved can never carry T1. Read off one printed line; graded **CONFIRMED-FROM-SOURCE**, not
   speculative.
3. **The ruling on (J1)** (§0.3): the E-free reading of Y₀ is the printed one, on the strength of
   Thm. 8.2's statement *and proof* ([x-03] p. 50), not merely notation; plus the robustness note
   that Ω lies in Y₀ under the "closure of the periodic orbits" definition as well.
4. **α = 1 is the printed local model** (§2.6): verify-O's repaired core (g′(0) = ½, A_p = p^{1/2}O)
   is exactly [Den05] p. 33's "complex conjugate numbers of absolute value Np^{1/2}", and the T2
   weight follows from p. 31 Rem. 7.6(4) + (34). Verifier O derived the repair; the source
   confirmation and the identification with p. 33's prescription are added here.
5. **Why α = 1 is not obstructed on the pieces** (§2.6, last bullet): [Den05] p. 23 Rem. 2 forces
   α = 0 only under Cor. 5.5's hypotheses (compact 3-manifold, **dense leaf**, conformal); disc
   leaves in a solid torus with boundary evade it. This locates R11's obstruction precisely.
6. **Theorem B sharpened by leaf dimension** (§4.1): d = 3 and d = 0 excluded outright; d = 2 is
   verify-F's proof (ratified in full); **d = 1 exists** (flow boxes) but yields an empty orbital
   side in [Den05] (32) and cannot carry α = 1. So "Y is not a foliated space" must be stated as
   "not with the leaf dimension S4 needs".
7. **Ruling that non-primitivity of n_p is a non-issue** (§2.1): the ℝ²-argument coordinate
   determines θ mod log p, so ι_p is injective regardless; verify-O's strand-separation repair is
   correct but unnecessary.
8. **The internal inconsistency in verify-F (2.3)/§2.7** (§0.1 D5): "α_p r ∂_ψ" with the coordinate
   convention is C^1, not smooth, and linearizes with no rotation; the displayed p^{−k}R(2πkλ)
   belongs to the constant-α variant. Harmless; recorded for the record's accuracy.
9. **Inherited and ratified, not new here:** verify-F's Theorem B (proof), Theorem C, Lemma D;
   verify-O's Lemma O-2a, Lemma O-5, Theorem O-3 and Corollary O-3a, §7.5's Euler-characteristic
   design constraint, and the §3.7 α = 1 repair. Each was re-derived by me except where §8 says
   otherwise.

**[NOVELTY — dual-model check 2026-09-03]** **Re-grading of items 1–9** (`results/c3-r/s14/novelty/adjudication.md`, binding). Item 1 (Theorem T): **PARTIAL** — criterion printed (Yokoyama Lemma 7.2; Akin–Auslander 6.3); printed opposite answer for the adelic base ([x-03] p. 64 via Laca–Raeburn Lemma 3.1); statement new. Item 2 (cyclic length group of §7.7 suspensions): **ANTICIPATED** — Deninger [x-18] = *Groups and Analysis*, LMS LNS 354 (2008), p. 3: "Its image Λ ⊂ ℝ is called the group of periods of (X, F, φ^t). It is known that F is a fibration if and only if rank Λ = 1"; Kim–Morishita–Noda–Terashima, Münster J. Math. 14 (2021) = arXiv:1906.02424 Prop. 2.2.5 ("If S is of type I or of type III-1, then the period group Λ_S = ℤ. Conversely …"), which they grade folklore ("Although this may be known (cf. [CCI; 9.3], [Fa; 2.1])"). Item 4 (α = 1 / p^{1/2}·O): ANTICIPATED verbatim, [Den05] pp. 32–33 "Fact … T_xφ^{kl(γ)} = e^{(k/2)l(γ)}·O_k for O_k ∈ SO(T_xF)"; "absolute value Np^{1/2}" — as this item already says; `verify-O.md` §9 item 2's single-check tag must be re-attributed to Den05. Item 6 (Theorem B by leaf dimension), item 9's Theorem C, Theorem O-3, and the construction itself: **NOVEL-DUAL-CHECKED** — no realization of {log p} and no such decomposition theorem found (nearest print: KMNT Thm 2.2.2/Cor. 2.2.4, Lemma 3.2 — the surgery shape of the witness, to be credited; Yokoyama 2020 Ex. 2; Wilson/Kuperberg plugs). [x-18] p. 3's "If one wants an infinitely generated Λ, one must allow the flow to have fixed points" is the printed structural constraint on S4′ and must be cited in §15 of the ledger.

---

## §8. Honesty record (standing order 5)

**Re-derived by me this session, in full:** the embedding and disjointness of the tubes (§2.1); the
closed-orbit inventory (§2.5); joint continuity (§2.4); the linearization, simplicity, ε ≡ +1 and the
α = 1 identification (§2.6, against [Den05] pp. 23, 31, 33); P_p ∈ E_f and the isotropy argument
(§3.1); P_p → 1_η (§3.2); Ω's indiscreteness (§3.3a); **the E-free packet-orbit indiscreteness,
including the chart bookkeeping via (51) and the density of {m/p^j : m ≡ p^j mod M}** (§3.3b); the
absorption lemma line by line (§3.3c); the continuity and equivariance of f (§3.4); verify-F's
Lemma D and Theorem C(i)(iii) (§4.4); verify-O's Lemma O-2a and Theorem O-3 (§2.5, §4.4);
**Theorem T** (§4.3) and the §7.7 length-spectrum consequence (§6), both mine.

**Read as printed, proofs not re-derived:** [x-03] Lemma 7.3 and (51) (p. 42), Prop. 7.4 (p. 43),
openness of π̌ (p. 43), Thms. 5.2/6.1 (pp. 34, 38–39) — used through the printed isotropy statement —
Thm. 8.2 (p. 50; used to identify Y₀ and to rule (J1), its Claim 8.1 dependency noted: unconditional
for one-dimensional X₀ flat over Spec ℤ via [Per11]); [Den05] Cor. 5.5 (p. 23), the working
hypothesis 7.5 and Thm. 7.8 (pp. 30, 35) — Thm. 7.8's proof is attributed there and not checked
here; [ALKL] §§1.1–1.3.1 definitions (pp. 1–3). Verify-F's Theorem B I re-derived step by step but
did not independently re-invent; verify-F's §5.4(a) Lefschetz computation I spot-checked only in the
T² case (L(h^{mk}) = 2 − tr(B^m) constant forces λ = 1 and L = 0 ≠ ±k) and otherwise inherit.
Verify-F's Theorem C(ii) (the W-locus clause) is inherited from the face-(b) machinery, not
re-derived, and is not load-bearing.

**Judgment calls, flagged:** (J1) ruled in §0.3 — a ruling on a reading, not a theorem; (J2) the
quotient topology on the E-free suspension is applied by analogy with [x-03] p. 59, which is printed
for admissible E.

**[RU] items:** [Ghy99] is not on disk, so whether "Riemann surface lamination in the sense of
[Ghy99]" carries compactness/Hausdorffness by definition is unverified — it does not affect any
verdict, since Theorem B and Theorem T both fail the [Den05] §7.1 definition, which is the one the
program's S2/S4 specification uses. Standard facts used without a source: the countable closed sum
theorem for covering dimension, invariance of domain, restriction of a quotient map to a saturated
closed set, and the flow-box theorem for fixed-point-free flows on compact metric spaces.

**Model note (standing order 7):** I am a third model (Opus 5) adjudicating two reports written on
Fable 5.1 — one of them by the same model as the refuter. I treated agreement between them as
evidence of nothing and re-derived the contested steps myself; the two places where I depart from
both (§4.3 Theorem T, §6's §7.7 consequence) are the places where re-derivation from the sources
found something neither report contains.

**Nothing rounded.** The construction is real and is now specified. Its S4 content is the orbit and
weight bookkeeping and nothing else. The map into Y₀ buys nothing, and — the finding that matters
most — the target of that map is not even in the category S4 is stated in: Y₀ is not T1.

— end of adjudication.md —
