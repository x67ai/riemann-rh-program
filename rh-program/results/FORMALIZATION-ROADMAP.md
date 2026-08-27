# Formalization roadmap — how far can the four circulation-ready papers be machine-checked?

**Written 2026-08-27**, in answer to the sponsor's question: *if the papers can be backed by
formalization, that is better — can we formalize all of it?*

**Short answer.** For the A4 no-go paper, yes — the headline result is reachable end-to-end, and
roughly half of the supporting mathematics is *already* machine-checked (see
`results/a4-no-go/formalization-status.md`). For the three C3-r notes, mostly no, and the reason
is not effort but **Mathlib coverage**: the mathematics those notes consume has not been built in
any proof assistant yet. Details and costings below, with the checks that establish them.

**No Magma is involved anywhere in this program.** The stack is Lean 4, Python, and Wolfram.

---

## What was actually checked (2026-08-27, against the pinned Mathlib rev `51e6992`)

| Query | Result |
|---|---|
| Gelfond–Schneider / Baker / six-exponentials in Mathlib | **absent** (grep over all of `Mathlib/`) |
| Lindemann–Weierstrass | directory `NumberTheory/Transcendental/Lindemann/` exists, **analytical part only** — the theorem itself is not finished |
| Liouville | present |
| Riemann–Roch (any form) | **absent** from `Mathlib/AlgebraicGeometry/` |
| Intersection theory / algebraic surfaces | **absent** |
| `Matrix.PosSemidef`, `Matrix.IsHermitian`, `Matrix.rank` | present |
| Matrix **inertia** (signature) and its subadditivity | **absent** — would have to be built |

---

## Paper 1 — the A4 no-go paper. Feasible, and half done.

Already machine-checked, sorry-free, axiom footprint `[propext, Classical.choice, Quot.sound]`:
Lemma 3.8, Theorem 3.9, the 4128/33 witness value for every vacancy position, the "alive" half of
Proposition 3.10, Lemma 4.2, and Theorem 4.3 pointwise + in law form + with exact attainment.

### Tier 1 — cheap. Days of work each, high confidence.

* **Proposition 3.3 (affine-plane identity) and Theorem 3.4 (cubic blindness).** These are
  *polynomial identities* over finite sums. The configuration infrastructure already exists in
  `GridParseval.lean`/`GridCorner.lean`; the mathematical content reduces to `ring` plus a
  bookkeeping induction. The underlying reason is elementary and worth stating in the Lean too:
  `p(t) = t(t-1)(t-2)` vanishes on `{0,1,2}` and `p(1+u) = u³ - u` is odd in `u`, so a
  signature-(1,1) pair spectrum annihilates it at every depth.
* **Corollaries 3.6 and 3.7** — arithmetic consequences once Theorem 3.5 is in place.
* **Lemma 4.1 on the grid** — already implied by `trace_sq_grid`; needs only to be stated.

### Tier 2 — moderate. Weeks each, well-defined.

* **The exact-rational LP witness with its dual certificate** — this is the headline. It is the
  *best* item on the list because the pattern is already proven in this repo: the parent paper's
  `LawN256.lean` / `CeilingLaw256.lean` do exactly this, and the A4 witness is three columns with
  rational weights, integer site subsets, marks in {1,2}, and every row value rational
  (F1 = 64, 96, 128; F′ and C′ rational combinations of triangular weights). This is *porting a
  working architecture with one added row family*, not inventing one.
* **Theorem 4.9 (the 8/9 spectral backstop).** Finite Hermitian matrix, one scalar inequality, and
  subadditivity of positive inertia. Mathlib has `IsHermitian` and `PosSemidef` but **not inertia
  subadditivity** — that lemma has to be built first. It is a clean, reusable target.
* **Theorem 4.3 off the grid** (atom-only, arbitrary positions) — needs the position-space form of
  Lemma 4.1, i.e. `F1 ≥ Σ m²` with kernel `K = D² ⪰ 0`. A Gram/PSD argument; `Matrix.PosSemidef`
  covers the tools.
* **Theorem 3.5** — piecewise-polynomial integration against `intervalIntegral`. Fiddly, not deep.
* **Theorem 7.4 (garnish)** — combinatorial bookkeeping; most of the cost is in stating it
  precisely enough to be provable.
* **Proposition 3.10 in general** (not just the witness) — needs a cyclotomic non-vanishing
  certificate. Mathlib has cyclotomic polynomials; the specific non-vanishing is a genuine lemma.

### Tier 3 — hard. This is where "formalize everything" stops being a task and becomes a project.

* **Theorem 7.1 (sharp capacity, constant 2√2).** Tonelli against the ladder plus a one-variable
  optimization plus attainment. Mathlib has the measure theory; this is real work but bounded.
* **The pair-channel capacity apparatus of Section 4.3** — certified interval arithmetic over
  continuous parameter ranges, per-cell rigorous enclosures, the crowding ledger. There is no
  turnkey interval-arithmetic layer in Mathlib at this scale. **This is the only genuine
  research-engineering item in the paper**, and it is worth being clear about what it supports: it
  underwrites Theorem 4.7's cap, a *subsidiary* claim, not the headline δ₀ = 0.

### The strategic point

The headline of this paper is an **LP marginal value** — δ₀ = 0, certified by a primal witness and
a dual bound. Both sides are exact-rational. So **the main theorem is reachable at Tier 1 + Tier 2
effort**, without touching Tier 3. A defensible milestone is: *"the exact-zero certificate,
machine-checked end-to-end, with the capacity results left as Python-certified numerics."* That is
a strictly stronger claim than any comparable paper in this area currently makes, and it does not
require solving the interval-arithmetic problem.

---

## Papers 2–4 — the C3-r notes. Blocked on Mathlib, not on effort.

### `seed-no-go` — partially feasible.

* **Theorem 1 (the isogeny criterion)** — `Hom(E_p, E_q) ≠ 0` iff `log p · log q ∈ 4π²Q` — is
  elementary lattice arithmetic over ℂ. Formalizable now, Tier 2.
* **Theorem 2 (at most one exceptional partner per prime)** — elementary. Formalizable now.
* **Theorem 3 (the {2,3,5} coherence kill)** — finite arithmetic. Formalizable now.
* **Theorem 5's unconditional half** — this is the strongest result in the note (`End(E_p) = Z`
  for every prime, unconditionally) and it rests on **Gelfond–Schneider**, which **is not in
  Mathlib**. Formalizing it means formalizing Gelfond–Schneider first. That is a well-known,
  well-defined target — and note that Mathlib's transcendence corner is live but unfinished
  (the Lindemann–Weierstrass directory currently contains only the analytical part). This is a
  worthwhile contribution in its own right, but it is a project, not a step.
* **Theorem 4 (Néron–Severi rank 2 off the matching)** — needs Néron–Severi groups of complex
  tori. Not in Mathlib.

### `m1-noncirc` — not feasible now, and least worth it.

It consumes Riemann–Roch on surfaces, Serre duality, Nakai–Moishezon, and the Néron–Severi group.
**None of these exist in Mathlib.** Formalizing them is a multi-year algebraic-geometry programme
that others are already pursuing. And the note itself claims **zero novelty** — it is an audit of
graduate-textbook material, whose value is the dependency ledger, not the theorems. Formalizing it
would be the most expensive item on this page and would add the least.

### `m0-axiom` — not feasible now.

It is an axiom class over *proper adelic curves* in the Chen–Moriwaki sense, with nef adelic line
bundles in the Yuan–Zhang calculus. Arakelov geometry over adelic curves is not in Mathlib in any
form. The one piece that *is* formalizable is the **P¹ × P¹ counterexample** — a concrete finite
object showing axioms (PF1)–(PF4) can be satisfied while touching no coefficient of any Dirichlet
series. That is the note's sharpest negative and it could stand alone as a checked artifact.

---

## Recommendation

1. **Do not block circulation on any of this.** The four papers are ready to post once the
   citation repairs land; formalization is an upgrade, not a prerequisite. arXiv does not ask for
   it, and the A4 paper's Section 10 now states the true position honestly.
2. **If one thing is done, do Tier 1 for A4** — the polynomial identities. Cheap, and it converts
   Section 10's "not formalized" list into a shorter one at low cost.
3. **If a real target is wanted, aim at the exact-rational LP witness** (Tier 2). It is the
   headline, the architecture already exists in this repo, and finishing it would let the paper
   claim its main theorem as machine-checked.
4. **Treat Gelfond–Schneider as a separate, publishable Mathlib contribution** if the seed note's
   Theorem 5 is to be formalized. Do not fold it into a paper's timeline.
5. **Do not attempt m1 or m0.** The prerequisites are missing from every proof assistant, and for
   m1 the note itself claims no novelty.
