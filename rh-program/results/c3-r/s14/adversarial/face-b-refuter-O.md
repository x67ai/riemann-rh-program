# ADVERSARIAL REFEREE — Q* FACE (b) — refuter O

**Program:** RH research program, direction C3-r, milestone M2c, Route 2, blocker S4.
**Role:** refuter O of two (adversarial; instructed to assume the theorem is wrong).
**Date:** 2026-09-03. **Session 14.**
**Target:** the face-(b) clause of `results/c3-r/s14/qstar-adjudication.md` §1 and §4:
*"no continuous flow-equivariant map from any nonempty quasi-compact space with an R-action
into X₀ (or into the unitary system Y₀ = X̌₀(S¹) ×_{Q>0} R_{>0}) reaches infinitely many packets;
hence no compact metrizable 3-dimensional lamination with one closed orbit of length log p per
prime maps into X₀ with γ_p → Γ_p, and Q-b is NO."*

**Sources read at source this session** (fresh `pdftotext -layout`; PDF page = printed page,
verified against footers): [x-03] = `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`,
pp. 22–23, 27–34, 37–48, 49–50; [x-06] = `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`,
pp. 11–12. Program inputs read: `qstar-adjudication.md` (all), `qb-kill.md` (§0, §2.5, §5–§8, §10.1–10.2,
§J-list), `qb-build.md` (§0, §2.6–2.7, Cor. 4, Cor. 6, Prop. 8), `qa-kill.md` (Lemma 3.3, Thm. 2, §7.2–7.4).
U.S. English throughout.

---

## §0. VERDICT (stated first)

### **REFUTED-STATEMENT** — with a counterexample, on the Y₀ clause; the X₀ core survives.

Precisely:

| Sub-claim of the target | Verdict |
|---|---|
| **(b-X₀)** No nonempty quasi-compact flow-invariant subset of **X₀ = X̌₀(C)_E ×_{Q>0} R^{>0}, E admissible** (Def. 4.1, [x-03] p. 27), meets more than finitely many packets; hence Q-b is NO for X₀. | **STANDS.** Every step re-derived independently from [x-03] below (§2, lines 1–3). No gap found. |
| **(b-Y₀)** The same "**for the unitary system Y₀ = X̌₀(S¹) ×_{Q>0} R^{>0}**". | **FALSE.** Explicit counterexample **K** (§3): a nonempty, quasi-compact, two-sided-flow-invariant subset of Y₀ containing **exactly one periodic orbit of length log p, lying inside the packet Γ_p, for every prime p** — i.e. reaching *every* packet. The inclusion K ↪ Y₀ ⊆ X₀^full is a continuous flow-equivariant map from a nonempty quasi-compact space reaching infinitely many packets. |
| **(b-exact)** "compactness is the exact obstruction" (adjudication §4, novelty item 10). | **FALSE as stated** for Y₀ (K is quasi-compact); **overstated** for X₀ (the witness Y_∞ is 1-dimensional, not a 3-dimensional lamination). The exact obstruction in the E-free/unitary setting is **admissibility (Tors)**, not compactness. |
| **(b-lamination)** No compact metrizable 3-dimensional lamination maps into X₀^E with γ_p ⊂ Γ_p. | **STANDS** as a consequence of (b-X₀). Not established for X₀^full / Y₀ — face (b) no longer supplies it there, and face (a) cannot (a map *into* an indiscrete packet is automatically continuous). |

**What the program should do with this.** The S4 kill for its stated target — Deninger's X₀
with an admissible class E — survives adversarial attack intact; I could not break it, and I
re-derived it in full. But the adjudication's verdict table, its §4(D), and its novelty items 6
and 10 assert the kill for `Y₀ = X̌₀(S¹) ×_{Q>0} R^{>0}` **without the E-subscript**, which is
exactly how Deninger prints Y₀ at [x-03] p. 49 and [x-06] p. 12; on that reading the assertion is
**false**. Those three places must be re-qualified to `Y₀^E = (X̌₀(S¹) ∩ X̌₀(C)_E) ×_{Q>0} R^{>0}`
before any decisive action, and the sentence "compactness is the exact obstruction" must be
withdrawn. `qb-kill.md` §10.1 (J2) had *flagged* the E-free reading and dismissed it as
"degenerate"; §3 below shows that dismissal is wrong — the E-free counterexample carries genuine
periodic orbits of length log p inside genuine packets, which is exactly what qb-kill §10.1's
defense claimed was impossible there. The adjudication dropped the flag entirely.

**Grading of the two kinds of finding, as instructed.**
*The statement is false* on the Y₀ clause and on the "exact obstruction" clause (§3).
*The argument as written has gaps* at four further places, none fatal to (b-X₀) (§2, lines 1, 2, 6;
§4): the backwards robustness sentence about coarser topologies; the silent use of two-sided
(not merely forward) invariance; the un-argued identification of Deninger's Y₀ with an
E-restricted subspace of X₀; and the scope claim against Deninger's own p. 40 question.

---

## §1. The objects and the topology, written out from the source

All page numbers are printed pages of [x-03] v4 unless marked [x-06]. Throughout X₀ = Spec Z,
K₀ = Q, K = Q̄, X = Spec Z̄ (Z̄ = the ring of all algebraic integers; countable), G = Aut(Q̄/Q),
C = ℂ, N₀ = N, Q>0₀ = Q>0.

**(1.1) Points (p. 22, Remark 3.4 p. 23).** X̊(C) = W_rat(X)(C) is the set of pairs (x, P^×) with
x ∈ X and **P^× ∈ Hom(κ(x)^×, C^×)** — a bare group homomorphism, *no* condition ([x-06] Thm. 4.1
p. 11 states this verbatim: `X̊(C) = {(x,P^×) | x ∈ X, P^× ∈ Hom(κ(x)^×,C^×)}`). For affine X one
views the pair as the multiplicative map P : Z̄ → C with P(0) = 0, P(1) = 1, 𝔭_P := P^{-1}(0) a
prime ideal, P factoring through Z̄/𝔭_P. Actions, verbatim p. 22: **F_ν(x,P^×) = (x, P^×∘( )^ν)**
and (x,P^×)^σ = (x^σ, P^×∘σ). X̊₀(C) = X̊(C)/G.

**(1.2) Admissibility (p. 27, Def. 4.1, verbatim).** A class E is admissible iff χ ∈ E ⟺ χ∘σ ∈ E
⟺ χ∘( )^ν ∈ E, **and every χ ∈ E satisfies (Tors)**: `ker(χ)_tors = ker(χ|_{μ(κ)}) is finite and
|(ker χ)_tors| ∈ N₀`. Examples p. 28–29: E_tors ⊃ E_max ⊃ E_fd0 ⊃ E_fd ⊃ E_fg ⊃ E_f. **(Tors) is
part of the definition of admissible; it is not implied by "unitary".**

**(1.3) Packet coordinates (pp. 31–34).** For x₀ = (p): (32) μ^{(p)}(K) ≅ κ(x)^×; (34)
Gal(κ(x)/κ(x₀)) = N x₀^Ẑ ↪ Aut(κ(x)^×) = Ẑ^×_{(p)}; (35) every (Tors)-character over x₀ is
χ_x∘( )^a∘( )^ν, with (a,ν) ~ (a′,ν′) iff ν′ = νp^n, a = p^n a′; (38)/(39)
C_{x₀} ≅ (Ẑ^×_{(p)}/p^Ẑ) ×_{p^Z} Q>0, "the fibres are the Q>0-orbits in C_{x₀}". **C_{x₀} is
defined inside X̌₀(C)_{E_tors}** (p. 31, verbatim: "the structures of the Q>0₀-sets
C_{x₀} = pr^{-1}_{X₀}(x₀) in X̌₀(C)_{E_tors}"). Theorem 5.2 (p. 34, needs E ⊆ E_max): the points of
X̌₀(C)_E with nontrivial Q>0-isotropy are exactly ⨿_{x₀} C^E_{x₀}, and each has isotropy exactly
N x₀^Z = p^Z; "If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}".

**(1.4) ρ (p. 33, verbatim).** (41) ρ(x,P^×) = |(Ker P^×)_tors| = |ker(P^×|_μ)|; (42)/(43)
**ρ(F_ν P) = ν_x·ρ(P)**, ν_x the prime-to-char-κ(x) part of ν, **ν_x = ν when char κ(x) = 0**.
Note (41) is a map *into N₀* — it is **defined only where (Tors) holds**; on a character with
infinite μ-kernel ρ is not defined by (41) at all.

**(1.5) Suspension and flow (p. 38).** X₀ = X̌₀(C)_E ×_{Q>0} R^{>0} := (X̌₀(C)_E × R^{>0})/Q>0
under **(P₀,u)q = (F_q P₀, q^{-1}u)**; φ^t[P₀,u] = [P₀, u e^t]; Γ^E_{x₀} = C^E_{x₀} ×_{Q>0} R^{>0},
whose R^{>0}-orbits are circles R^{>0}/p^Z of length log p. Theorem 6.1 (p. 39, needs E ⊆ E_max):
{points with nontrivial R^{>0}-isotropy} = ⨿_{x₀} Γ^E_{x₀}; every periodic orbit lies in a unique
packet.

**(1.6) The topology, exactly as printed (pp. 40–47).**
- X̊(C) for affine X carries the **topology of pointwise convergence on Z̄** = the subspace topology
  from the Tychonoff topology of C^{Z̄} (p. 40, verbatim); Z̄ countable ⟹ metrizable.
- Prop. 7.6/Cor. 7.8 (pp. 44–45): a **G-invariant metric d** on X̊(C) of the form
  d(P,P′) = Σ_r a_r |P(r)−P′(r)|/(1+|P(r)−P′(r)|) with a_r > 0, Σ_r a_r < ∞, and the quotient
  metric δ(πP, πP′) = min_σ d(P^σ, P′) on X̊₀(C), with **δ(πP,πP′) ≤ d(P,P′)**; X̊₀(C) is
  metrizable, separable, Hausdorff.
- Lemma 7.3 / (51) (p. 42, verbatim): **F_ν(X̊(C)) = {P ∈ X̊(C) | P(μ_ν(K)) = 1}**, which is
  **clopen**; F_ν is a homeomorphism onto it; G acts by homeomorphisms.
- X̌(C) = colim_{N₀} X̊(C) with the **inductive-limit topology**: Z is open iff F_ν(Z) ∩ X̊(C) is
  open for every ν (p. 43). Prop. 7.4: X̊(C) is clopen in X̌(C); **F_q is a homeomorphism of X̌(C)
  for every q ∈ Q>0**; G acts by homeomorphisms. X̌₀(C) := X̌(C)/G, **quotient topology**;
  π̌ is continuous **and open** (p. 43, verbatim: "the projections … are continuous and since G acts
  by homeomorphisms, also open"). Cor. 7.9 (p. 45): X̌₀(C) is Hausdorff.
- p. 47, verbatim: E-loci carry the subspace topologies; X̌(C)_E = colim X̊(C)_E agrees with the
  subspace topology because **F_ν^{-1}X̊(C) and F_ν^{-1}X̊₀(C) are open in X̌(C) resp. X̌₀(C) for all
  ν ∈ N₀**; "All preceding results in this section remain true".
- **The suspension's topology.** [x-03] never writes the words, but Thm. 7.10 (p. 46) asserts
  *continuous bijections* onto X = X̌(C)_{Etors} ×_{Q>0} R^{>0} and onto X₀, and Remark 2 (p. 47)
  says these are **not** homeomorphisms — the fibre of X₀ over η₀ is connected while the left side
  has d_μ components. Hence X₀ carries a topology strictly **coarser** than the chart coproduct,
  and the only one in the sources is the **quotient topology of X̌₀(C)_E × R^{>0}** under the Q>0
  action. Since Q>0 acts by homeomorphisms, the quotient map **q is open**, and for a saturated
  A ⊆ X̌₀(C)_E × R^{>0} the restriction q|_A : A → q(A) is an open map onto the subspace q(A),
  hence a quotient map. *(I use this three times below; it is elementary: for U = A ∩ V, saturation
  gives q(A∩V) = q(A) ∩ q(V).)* This reading is the one both faces share and I adopt it.
- **Correction to the adjudication's robustness sentence (§2 of `qstar-adjudication.md`).** It says
  "a strictly coarser topology strengthens face (a) and **preserves face (b) (fewer opens ⟹ harder
  to be quasi-compact)**." The parenthetical is **backwards**: fewer open sets make quasi-compactness
  *easier*, not harder (the indiscrete topology makes every set quasi-compact). The correct
  robustness statement is the opposite one and it is still enough: face (b)'s two ingredients —
  l.s.c. of W and openness of the separating sets V_p — are *preserved under refinement*, so
  **face (b) holds in the quotient topology and in every finer topology (including the Thm. 7.10
  coproduct)**, and could fail in a coarser one. Not fatal; but the stated justification is wrong,
  and it is the single load-bearing judgment call of the whole adjudication.

**(1.7) The unitary system Y₀ — read verbatim, because this is where the theorem breaks.**
[x-03] p. 49, verbatim: *"one idea would be to replace X₀ by the dynamical system Y₀ obtained as
the topological closure of the union of all periodic orbits coming from closed points of X₀. In
this section we will show that the system Y₀ is still infinite-dimensional: Namely, for
one-dimensional X₀, flat over spec Z and conditionally for all X₀ we have*
**Y₀ = X̌₀(S¹) ×_{Q>0} R^{>0}.** *Here X̌₀(S¹) = X̌(S¹)/G where X̌(S¹) = colim_N X̊(S¹) and* **X̊(S¹)
is the subspace of X̊(C) consisting of points (x,P^×) with P^× : κ(x)^× → S¹ a unitary character."**

[x-06] p. 12, verbatim: *"The space X₀^E is infinite dimensional … one could hope that the
sub-dynamical system obtained as the closure of the union of all its compact orbits might be
significantly smaller. However, this is not the case … The closure is the subsystem obtained by*
**replacing X̊(C)_E in the previous constructions with the subspace of pairs (x,P^×) with
P^× : κ(x)^× → S¹ a unitary character."**

Two things are unambiguous in this text and they are what kill the Y₀ clause:
1. **X̊(S¹) is defined by unitarity alone.** No (Tors), no admissibility. The sentence in [x-06] is
   even sharper: the closure is obtained by *replacing* X̊(C)_E with the unitary locus — E is
   dropped, not intersected.
2. **Unitary does not imply (Tors).** Q̄^× ≅ μ(Q̄) × V with V a Q-vector space (the splitting used
   in Lemma 4.3, p. 28); taking P^× ≡ 1 on μ(Q̄) and anything unitary on V — in particular the
   **trivial character P^× ≡ 1 of Q̄^×** — gives a point of X̊(S¹) with ker(P^×|_μ) = μ(Q̄), infinite.
   Deninger's ρ, (41), is *undefined* there.

Theorem 8.2 (p. 50) then reads: X̌(C)_per = X̌(S¹), the closure being taken **in X̊(C)** — the proof
says so twice ("Since X̊(S¹) is closed in X̊(C) …"; "every neighborhood of P in X̊(C) contains a point
from X̊(C)_per"). For X₀ = Spec Z (dim 1, char K₀ = 0) Theorem 8.2 is **unconditional** (Claim 8.1 is
needed only for dim ≥ 2 or char > 0; and for number rings it follows from [Per11, Thm. 1], p. 49).

So the closure of the periodic locus **leaves every admissible class**. That is a structural fact
about [x-03], not a quibble: X̊(C)_per ⊆ E_f, but cl(X̊(C)_per) = X̊(S¹) ⊄ E_tors.

**(1.8) A compactness fact I need, and which is nowhere in the program record.**

> **Lemma O-1.** X̊(S¹) is **compact metrizable**; hence so is X̊₀(S¹) = X̊(S¹)/G.

*Proof.* Every P ∈ X̊(S¹) satisfies P(r) ∈ S¹_0 := S¹ ∪ {0} for all r ∈ Z̄ (unitary on Z̄∖𝔭_P, zero on
𝔭_P), so X̊(S¹) ⊆ ∏_{r∈Z̄} S¹_0, which is compact (Tychonoff) and metrizable (Z̄ countable, p. 40).
It remains to see X̊(S¹) is closed there. Let a net P_i → P pointwise, P_i ∈ X̊(S¹). Multiplicativity,
P(0)=0, P(1)=1 pass to the limit. Values lie in S¹_0, and a net in S¹_0 converges to 0 only if it is
eventually 0; so 𝔭 := P^{-1}(0) = {r : P_i(r) = 0 eventually}. Then 𝔭 is an ideal (r,s ∈ 𝔭 ⟹
eventually r,s ∈ 𝔭_i ⟹ r+s ∈ 𝔭_i; absorption likewise), proper (P(1)=1), and prime (P(rs) = P(r)P(s)).
And P factors through Z̄/𝔭: if r−s ∈ 𝔭 then eventually r ≡ s mod 𝔭_i, so P_i(r) = P_i(s), so
P(r) = P(s). Finally P is unitary off 𝔭 and extends uniquely to a character of Frac(Z̄/𝔭)^× = κ(x)^×.
So P ∈ X̊(S¹). ∎

(This is consistent with, and sharper than, Deninger's "X̊(S¹) is closed in X̊(C)", p. 50.)

---

## §2. The six attack lines, one by one

### Line 1 — the weight W: well-definedness, positivity, lower semicontinuity. **NO DEFECT on X₀^E; one wrong justification.**

Write ρ̂ : X̊(C) → [1,∞] by ρ̂(P) = |ker(P^×|_μ)| if char κ(x) = 0 and ρ̂(P) = +∞ if char κ(x) > 0,
extended to X̌(C) by ρ̂(F_ν^{-1}P) := ρ̂(P)/ν; then W([P₀,u]) := ρ̂₀(P₀)·u on X₀.

**(a) Well defined on X̌(C).** If F_ν^{-1}P = F_μ^{-1}Q then F_μP = F_νQ; by (43) with ν_x = ν in
char 0, μ·ρ(P) = ν·ρ(Q), so ρ(P)/ν = ρ(Q)/μ. In char > 0 both sides are ∞ and F preserves x.
**Checked at (42)/(43), p. 33.** G-invariance: ker((P∘σ)|_μ) = σ^{-1}ker(P|_μ), same order. So ρ̂₀
descends.

**(b) Well defined on the suspension.** W((P₀,u)q) = ρ̂₀(F_qP₀)·q^{-1}u = q·ρ̂₀(P₀)·q^{-1}u = W(P₀,u),
using ρ̂₀(F_qP₀) = q ρ̂₀(P₀) — which is (43) in char 0 and ∞ = q·∞ in char > 0. **✓** Conformality
W∘φ^t = e^t W is immediate (φ^t scales u only). **✓**

**(c) Strict positivity.** ρ̂ takes values in Q>0 ∪ {∞}, never 0. **✓** (Attack-line (3)'s worry
"ρ̂₀ might be 0 at unitary generic points" is unfounded: ρ ≥ 1 always and ρ̂ = ρ/ν > 0.)

**(d) Lower semicontinuity — re-derived, and I could not break it.** On X̊(C): let P_i → P.
For ζ ∈ μ(K) of order n, P_i(ζ)^n = P_i(ζ^n) = 1, so all values lie in the **finite** set μ_n(ℂ);
a net in a finite subset of a Hausdorff space converging to P(ζ) is eventually equal to it. This is
the "root-of-unity rigidity" and it is airtight: it needs no unitarity, only multiplicativity —
characters into ℂ^× automatically land in μ on μ. *The attack-line's "characters into μ vs into S¹"
distinction is void.*
 - char P = 0: ker(P|_μ) is a finite subgroup of μ(Q̄) ≅ Q/Z, hence **= μ_{ρ(P)}**, cyclic with one
   generator ζ₀. Eventually P_i(ζ₀) = 1, so μ_{ρ(P)} ⊆ ker(P_i|_μ); so eventually ρ(P_i) ≥ ρ(P)
   (char 0) or ρ̂(P_i) = ∞. lim inf ρ̂(P_i) ≥ ρ̂(P). ✓
 - char P = p ("p-adic inflation", made exact): for every k, μ_{p^k}(K) ⊆ ker(P^×|_μ), because
   ζ^{p^k} = 1 ⟹ (ζ̄−1)^{p^k} = ζ̄^{p^k}−1 = 0 in F̄_p ⟹ ζ̄ = 1 ⟹ P(ζ) = 1. Applying the rigidity
   to a generator of μ_{p^k}: eventually ρ̂(P_i) ≥ p^k. As k is arbitrary, lim inf ρ̂(P_i) = ∞ = ρ̂(P). ✓
 **I attempted three nets to break this and all failed**: (i) P_i char-q_i with q_i → ∞ converging to
 a generic P — then lim inf ρ̂ = ∞ ≥ ρ̂(P), fine; (ii) P_i char 0 with ρ(P_i) = 1 converging to a
 char-p point — impossible, since P_i(p) has modulus 1 for i large while P(p) = 0 would need
 P_i(p) → 0 (this is exactly the "separation at infinity" mechanism, and it *protects* l.s.c.);
 (iii) P_i char 0 with ρ(P_i) → ∞ converging to a char-0 P with ρ(P) = 1 — allowed, and l.s.c. is
 the *right* direction there (ρ̂ jumps **up** in the limit, so it is l.s.c. and **not** continuous;
 the adjudication says exactly this).
**(e) Transport to X̌ and to X₀ — the adjudication's route is more elaborate than needed and my
route is cleaner.** l.s.c. is *local*, and {F_ν^{-1}X̊(C)}_ν is an open cover of X̌(C) (p. 47) on
which ρ̂ is (1/ν)·(ρ̂|_{X̊(C)})∘F_ν with F_ν a homeomorphism (Prop. 7.4b) — so ρ̂ is l.s.c. on X̌(C).
Descent needs **no** openness argument at all: for a quotient map π̌, ρ̂₀ is l.s.c. iff
π̌^{-1}{ρ̂₀ > a} = {ρ̂ > a} is open. Same for q: **W is l.s.c. on X₀ iff (P₀,u) ↦ ρ̂₀(P₀)u is l.s.c.
on X̌₀(C)_E × R^{>0}**, which it is (product of l.s.c. positive and continuous positive). ✓
Restriction to the E-locus preserves l.s.c. ✓

**(f) The one clause that consumes admissibility — and the defect.** "W^{-1}(∞) = ⨆_p Γ^E_p" holds
**iff every characteristic-zero point of the space has finite μ-kernel**, i.e. iff (Tors) holds. The
adjudication says so ("this and only this consumes admissibility"), correctly. For X₀ = Spec Z the
converse inclusion is also fine: over Spec Z the only positive-characteristic points of X₀ are the
closed points, and by Thm. 5.2 with E ⊆ E_max the whole char-p fibre C^E_{(p)} has isotropy p^Z, so
{W = ∞} = ⨆_p Γ^E_p exactly. **✓ for X₀^E.** **✗ for Y₀** — see §3.
**Value on packets is +∞ and not merely undefined:** yes, because ρ̂ is *defined* to be +∞ in
positive characteristic, and that definition is forced by conformality (ρ̂(F_qP) = qρ̂(P) has no
finite solution when the isotropy is nontrivial: F_pP = P would give ρ̂ = pρ̂). ✓

### Line 2 — the minimum step and backward flow. **NO DEFECT; one unstated hypothesis.**

*inf attained.* If m := inf_K W is not attained then {W > a}_{a > m} covers K (each z has W(z) > m,
so W(z) > a for some rational a ∈ (m, W(z))); a finite subcover gives K ⊆ {W > a₀} whence m ≥ a₀ > m.
Contradiction. So m is attained; and m > 0 since W > 0 pointwise. **No separation axiom used. ✓**

*Backward flow inside K.* K is invariant under the **whole** R-action, so φ^{-t}z₀ ∈ K, and
W(φ^{-t}z₀) = e^{-t}W(z₀) = e^{-t}m < m for t > 0 — contradicting minimality **provided m < ∞**. So
m = ∞, i.e. W ≡ ∞ on K. ✓ The W = ∞ case is not excluded but *is the conclusion*; the adjudication's
phrasing is correct.

**Unstated hypothesis (gap, minor but real): two-sidedness is load-bearing.** With only a
*semiflow* (R_{≥0}-action, i.e. K merely forward-invariant) the argument collapses — forward flow
*increases* W. This is not idle: on Y₀ there is an explicit **compact forward-invariant** set meeting
**every** packet, namely

> **κ := q(X̊₀(S¹) × [1,2]) ⊆ Y₀.**

κ is compact (continuous image of a compact set, Lemma O-1). It is forward-invariant: for s ≥ 1 and
Q ∈ X̊₀(S¹), [Q,s] = [F_{⌊s⌋}Q, s/⌊s⌋] with F_{⌊s⌋}Q ∈ X̊₀(S¹) and s/⌊s⌋ ∈ [1,2], so
κ ⊇ q(X̊₀(S¹)×[1,∞)) ⊇ φ^t κ for t ≥ 0. And [χ_p, 1] ∈ κ for every prime p, so κ meets every packet.
So the theorem is **specific to two-sided R-actions**; the target statement does say "with an
R-action", so this is a scope note, not a refutation — but the adjudication never says the
two-sidedness is essential, and Q-b′ (§8 of the adjudication) is precisely about attractor-like
objects where the distinction bites.

### Line 3 — the clopen claim, and whether dissipation covers the unitary generic points. **NO DEFECT on X₀^E; the attack line's own worry is answered, but the worry it did not state is fatal (§3).**

*V_p is genuinely open in X₀.* Fix a rational prime q₀. D := {P ∈ X̊(C) : |P(q₀)| < ½} is open
(ev_{q₀} continuous by the pointwise topology, p. 40) and **G-invariant** (q₀ ∈ Q is G-fixed, so
P^σ(q₀) = P(q₀)). S := ⋃_{r ∈ Q>0} F_r(D) is open in X̌(C) (each F_r a homeomorphism, Prop. 7.4b,
and X̊(C) open in X̌(C), Prop. 7.4a) and Q>0G-invariant. Hence π̌(S_E) is open (π̌ open, p. 43) with
π̌^{-1}π̌(S_E) = S_E, and V_{q₀} := q(π̌(S_E) × R^{>0}) is open in X₀ with
q^{-1}(V_{q₀}) = π̌(S_E) × R^{>0}. ✓

*The value computation, re-derived.* Let z ∈ Γ_p, so z = [P₀, u] with P₀ = π̌(F_ν^{-1}(x,P^×)),
char κ(x) = p. Membership in S is a statement about the **whole Q>0-orbit**: z's character lies in S
iff some F_s of it lies in D. Every element of the Q>0-orbit that lies in X̊(C) is some Q with
Q(q₀)^n = P(q₀^m) for suitable m,n ∈ N. Now P factors through Z̄/𝔭 = F̄_p, and F̄_p^× is torsion, so
for q₀ ≠ p (q₀ ∉ 𝔭) we get |P(q₀^m)| = 1, hence |Q(q₀)| = 1: **never in D**. For q₀ = p we have
p ∈ 𝔭, so P(p) = 0 and P ∈ D. Therefore **Γ_p ⊆ V_p and V_{q₀} ∩ Γ_p = ∅ for p ≠ q₀.** ✓
(I verified the two ingredients at source: ev_r continuity p. 40; F̄_p^× torsion, used by Deninger
himself at p. 50, "Any character of the torsion group F̄_p^× takes values in the roots of unity".)

*The attack line's sharpest worry — a compact Y containing generic unitary points as limits of its
packet orbits — is answered, on X₀^E.* It never arises: dissipation (Line 2) already forces
K ⊆ {W = ∞} = ⨆_p Γ^E_p **before** the cover is used, so {V_p}_p is an open cover of a set containing
K, and a finite subcover bounds the packets met. The order of the two steps is what makes the
worry moot, and the adjudication has the order right.

*But the worry was posed against the wrong hypothesis.* On X₀^E, ρ̂₀ at a unitary generic point is
finite (by (Tors)) and ≥ 1 — never 0, never ∞. On **Y₀ as printed** it is ∞ on a large set, and
that is the hole. §3.

*Is the periodic locus locally closed / is clopenness enough?* Not needed, and I record why the
adjudication's phrase "each packet is clopen in the periodic locus" is a weaker statement than what
is used: what is used is only that V_p is **open in X₀**, contains Γ_p, and misses Γ_q for q ≠ p.
That is proved. Whether ⨆_pΓ_p is locally closed in X₀ is never invoked. ✓ (It is in fact *dense*
in Y₀, by Thm. 8.2 — which is precisely why the naive "cover the rest by one more open set" fails,
and why §3's counterexample works.)

### Line 4 — qa-kill's independent route (chart criterion / backward escape). **RE-DERIVED, CORRECT — and it fails at exactly the same place.**

Lemma 4.6(1) (p. 30) with R = K = Z̄ (every element of Z̄ is an N-th power; μ_N(Z̄) = μ_N(Q̄)) gives
(51), p. 42, verbatim: **F_ν(X̊(C)) = {P ∈ X̊(C) | P(μ_ν(K)) = 1}**. Hence for m,n coprime,
F_{m/n}π(η,Ψ) = F_n^{-1}(F_mΨ) lies in the first chart iff F_mΨ(μ_n) = 1 iff μ_n^m = μ_n ⊆ ker(Ψ|_μ)
iff **n | e** where e := |ker(Ψ|_μ)|. So m/n ≥ 1/n ≥ 1/e. qa-kill's Lemma 3.3 states "n | m·e",
which for coprime m,n is the same condition. **CONFIRMED, re-derived from (51) + Lemma 4.6.**

Theorem 2's bound: with P ∈ 𝒞_ν, P′ = F_νP, and a convergent backward lift F_{q_β}P → P* ∈ 𝒞_{ν′},
one gets ν′q_β/ν = m_β/n_β with n_β | m_β e, so ν′q_β/ν ≥ 1/e, so **q_β ≥ ν/(ν′e) > 0**, contradicting
q_β → 0. **CONFIRMED.** This is a genuinely different instrument from the weight (it is a
denominator bound in the colimit, not a semicontinuity argument) and it *is* an independent route.

**But it is not independent of admissibility.** qa-kill's own Lemma 3.3 says it in the statement:
"μ_e := ker(Ψ|_{μ(Q̄)}), a finite subgroup of μ(Q̄) **by (Tors)**". For e = ∞ the bound reads
q_β ≥ ν/(ν′·∞) = 0 and is **vacuous**. Concretely, for the trivial character Ψ ≡ 1 the criterion
"n | e" is satisfied by *every* n, so **every** F_{m/n}π(η,1) lies in the first chart and the
backward orbit never leaves it. So the "third, mechanism-distinct route" collapses at exactly the
same locus as the weight. The adjudication's independence claim (§5) is true at the level of
*mechanism* and false at the level of *hypothesis*: all three face-(b) routes stand or fall with
(Tors).

qa-kill §7.2's fallback ("the finer coproduct topology also kills") does survive — under the
Thm. 7.10 coproduct topology the packets are clopen and no compact source meets infinitely many —
but that topology is refuted by Deninger's own connectedness statement ([x-06] Thm. 4.4: the
bijection is "not a homeomorphism since X₀ is connected, whereas the left hand side is
disconnected"), so it is not the topology of record.

### Line 5 — the non-compact witness Y_∞. **CONTINUOUS AND EQUIVARIANT (correct); the sentence built on it is not.**

Y_∞ := ⨆_p R^{>0}/p^Z with the multiplicative flow; f(u) := [P^{a₀(p)}, u] on the p-th circle.
*Well defined:* by Thm. 5.2 the isotropy of a packet character is exactly p^Z, so F_p P = P and
[P, u] = [P, p^{-1}u]; the map R^{>0} → X₀ therefore factors through R^{>0}/p^Z, and since
R^{>0} → R^{>0}/p^Z is a quotient map the factored map is continuous. *Continuous:* u ↦ (P,u) is
continuous into X̌₀(C)_E × R^{>0}, then compose with q. *Equivariant:* φ^t[P,u] = [P,ue^t]. ✓
*Meets every packet in exactly one orbit.* ✓ **CONFIRMED.**

**But "compactness is the exact obstruction" (adjudication §4 and novelty item 10) does not follow,
and is false.** Two independent reasons.
(i) Y_∞ has covering dimension **1**, not 3; and it carries no 2-dimensional leaves. Q-b asks for a
compact metrizable **3-dimensional lamination** with **exactly one** closed orbit of length log p per
prime. Y_∞ satisfies "one orbit per prime, right lengths, continuous, equivariant, γ_p → Γ_p" but
*not* "3-dimensional lamination", and the obvious repairs fail: Y_∞ × R² with the flow on the first
factor has uncountably many closed orbits of length log p, violating "exactly one". So Y_∞ shows
only that **compactness + dimension-3 + one-orbit-per-prime** cannot all be dropped at once; it does
not isolate compactness.
(ii) On Y₀ the obstruction is not compactness at all — §3 exhibits a **quasi-compact** K reaching
every packet. There the exact obstruction is (Tors).

### Line 6 — consistency with [x-03], and what is actually proved for non-compact Y₀. **NO CONTRADICTION with print; two scope overreaches.**

*No printed statement about X₀ is contradicted.* Deninger's p. 39–40 expectation is that in a
conjectural Arakelov compactification X̄₀ the orbits [z,±1]u tend to a fixed point as **u → 0⁺**.
The weight makes this exact and consistent: W([z,u]) = ρ̂₀(z)u → 0 as u → 0⁺, and W is bounded below
on every quasi-compact invariant set — so the limit points are precisely the ones X₀ does not
contain. The kill therefore *agrees* with Deninger and turns his expectation into a theorem about X₀.
Likewise [x-06] Thm. 4.2's "compact subsets Γ_{x₀}" is consistent (an indiscrete space is compact),
and Thm. 4.3's connectedness is consistent (a non-T₀ space can be connected).

*Overreach 1 — Deninger's own p. 40 question is not answered.* Verbatim, p. 40: *"Is there a
sub-dynamical system Y₀ ⊂ X₀ = X̌₀(C) ×_{Q>0} R^{>0} or at least one which maps to X₀ such that
dim Y₀ = 2d+1 … and such that Y₀ contains at least one periodic orbit in Γ_{x₀} for every closed
point x₀ of X₀? If d = 1, is there such a Y₀ which is a Riemann surface lamination in the sense of
[Ghy99]?"* — **there is no compactness requirement anywhere in that sentence.** Face (b) assumes
quasi-compactness and therefore says nothing about it; indeed Y_∞ answers its first half
affirmatively in dimension 1, and §3's K answers it affirmatively in Y₀ with one genuine periodic
orbit per prime. The compactness comes from the *program's* Q-b (ALKL H1, [Ghy99] laminations), not
from Deninger. The adjudication should not present "S4 is DEAD" as closing Deninger's question.

*Overreach 2 — Y₀ non-compact.* What is actually proved for non-compact Y₀ is only:
**Y₀ is not quasi-compact.** That much *does* survive on the E-free reading, and I re-derived it:
W is l.s.c. and strictly positive on Y₀ (Line 1 does not use (Tors) for those two properties), so if
Y₀ were quasi-compact the inf would be attained at some m > 0, and if m < ∞ backward flow
contradicts it — while Y₀ visibly contains points with W < ∞ (an injective unitary character of Q̄^×
has ρ = 1, so W([P,u]) = u), so m < ∞ and Y₀ is not quasi-compact. ✓ **Everything beyond that
sentence — in particular the finiteness conclusion for quasi-compact invariant subsets — is false
on Y₀.**

---

## §3. THE STRONGEST ATTACK — and it succeeds

> **Theorem O-2 (counterexample).** In Deninger's unitary system
> **Y₀ = X̌₀(S¹) ×_{Q>0} R^{>0}** ([x-03] p. 49; [x-06] p. 12) there is a set
> **K := Ω ∪ ⋃_{p prime} γ_p**
> which is **nonempty**, **quasi-compact**, and **invariant under the whole R-action**, where each
> γ_p is a **periodic orbit of length log p contained in the packet Γ_p**, exactly one per prime,
> and Ω is one further orbit. Consequently the inclusion K ↪ Y₀ ⊆ X₀^full = X̌₀(C) ×_{Q>0} R^{>0} is
> a continuous flow-equivariant map from a nonempty quasi-compact space with an R-action that
> **reaches every packet**. The face-(b) statement is false for Y₀.

**The two ingredients.**

*(A) The absorber.* Let **P^{(0)} := (η, 1)** ∈ X̊(S¹), the **trivial** character of Q̄^× (unitary;
a point of X̊(S¹) by the definition read verbatim in §1.7). It is F-fixed: F_ν(η,1) = (η, 1∘( )^ν)
= (η,1), so F_q P^{(0)} = P^{(0)} for **every** q ∈ Q>0, and the Q>0-isotropy is all of Q>0. Put
**Ω := q({π(P^{(0)})} × R^{>0})**. Then:
- q^{-1}(Ω) = {π̌(P^{(0)})} × R^{>0} is saturated (F_qP₀ = P^{(0)} forces P₀ = P^{(0)}, F_q being
  a bijection of X̌₀), so q restricted to it is a quotient map onto the subspace Ω (§1.6);
- Ω ≅ R^{>0}/Q>0 with the quotient topology, and **that space is indiscrete**: a nonempty
  Q>0-saturated open U ⊆ R^{>0} contains an interval (a,b), and (a,b)·Q>0 = R^{>0} because Q>0 is
  dense; so U = R^{>0}.
- Hence **Ω is quasi-compact and every open set of Y₀ meeting Ω contains all of Ω.**
- Ω is flow-invariant and lies over the **generic** point of Spec Z. (This alone already **refutes**
  the adjudication's §4(B)/novelty-item-5 clause "no nonempty quasi-compact flow-invariant subset of
  X₀ meets the characteristic-zero locus" on the E-free reading; W ≡ ∞ on Ω, so it is consistent
  with dissipation but not with the identification {W=∞} = packets.)

*(B) The genuine periodic orbits.* For each prime p let x_p ∈ X be a point over (p) and
**χ_p := ι∘i_{x_p}^{-1} : κ(x_p)^× = F̄_p^× ↪ μ(ℂ) ⊂ S¹** the injective character of (32)/p. 32.
It is **unitary** (values are roots of unity), and it satisfies (Tors) with ρ(χ_p) = 1, so it lies in
E_f ⊆ E_max: by **Theorem 5.2** its Q>0-isotropy is exactly p^Z, and by **Theorem 6.1** the orbit
**γ_p := q({π̌(χ_p)} × R^{>0}) ≅ R^{>0}/p^Z** is a periodic orbit of length **log p** lying in the
packet **Γ_p**. Exactly one per prime.
By the face-(a) theorem (adjudication §3, whose proof I checked applies verbatim here — the
approximating net (χ_p,w)·r_k stays unitary and X̊(S¹) is closed in X̊(C)), **γ_p is an indiscrete
subspace**: any open set meeting γ_p contains γ_p.

**Proof of Theorem O-2.** K is nonempty and invariant under all φ^t (each piece is). Let 𝒰 be a
cover of K by sets open in Y₀.

1. Some U₀ ∈ 𝒰 meets Ω; since Ω is indiscrete, **Ω ⊆ U₀**.
2. Because [π(P^{(0)}), 1] ∈ U₀ and q is continuous, q^{-1}(U₀) is open and contains
   (π̌(P^{(0)}), 1); pick a basic box **V × (a,b) ⊆ q^{-1}(U₀)** with π(P^{(0)}) ∈ V open in
   X̌₀(S¹) and 1 ∈ (a,b).
3. **Claim: for all but finitely many p there is ν_p ∈ N with π(F_{ν_p}χ_p) ∈ V.**
   *Proof.* V ∩ X̊₀(S¹) is a neighborhood of π(P^{(0)}) in the metric δ of Cor. 7.8, so it contains
   a δ-ball of some radius ε. Using δ(πQ,πQ′) ≤ d(Q,Q′) it suffices to make d(F_νχ_p, P^{(0)}) < ε.
   Since Σ_{r ∈ Z̄} a_r < ∞ (Prop. 7.6, p. 44), choose a finite S ⊂ Z̄∖{0} with
   Σ_{r ∉ S∪{0}} a_r < ε. Each r ∈ S is a nonzero algebraic integer, so r ∈ 𝔭_{χ_p} forces
   p | N_{Q(r)/Q}(r) ≠ 0 — true for only finitely many p. So for all but finitely many p we have
   S ∩ 𝔭_{χ_p} = ∅; set **ν_p := lcm{ ord(r mod 𝔭_{χ_p}) : r ∈ S }**, a positive integer because
   F̄_p^× is torsion. Then F_{ν_p}χ_p(r) = χ_p(r)^{ν_p} = 1 = P^{(0)}(r) for every r ∈ S, and
   F_{ν_p}χ_p(0) = 0 = P^{(0)}(0); every remaining term of d is at most a_r. Hence
   d(F_{ν_p}χ_p, P^{(0)}) ≤ Σ_{r ∉ S∪{0}} a_r < ε. ∎
4. For such p, (π(F_{ν_p}χ_p), 1) ∈ V × (a,b) ⊆ q^{-1}(U₀), i.e.
   **[F_{ν_p}χ_p, 1] = [χ_p, ν_p] ∈ U₀ ∩ γ_p ≠ ∅**
   (the identity [F_νP, u] = [P, νu] is the defining relation (P,u)ν = (F_νP, ν^{-1}u), p. 38).
   Since γ_p is indiscrete, **γ_p ⊆ U₀**.
5. So U₀ contains Ω and all but finitely many γ_p. Each remaining γ_p is met by some U_p ∈ 𝒰 and
   is therefore contained in it (indiscreteness again). **{U₀} ∪ {U_p}_{p ∈ F} is a finite subcover.** ∎

**Why the existing defenses do not apply.**
- `qb-kill.md` §10.1 Prop. 10.1 found a related set D = O_∞ ∪ ⋃_p O_p built from the **trivial**
  characters of F̄_p^×, and defended the Main Theorem by observing (correctly) that those points are
  **not periodic** (isotropy Q>0, not p^Z) and **lie in no packet**, so "the E-free system is
  degenerate, not an escape". **That defense fails against K**: my γ_p are honest periodic orbits of
  length log p with isotropy exactly p^Z, lying inside the packets Γ_p in the sense of [x-03]
  Thms. 5.2/6.1, because χ_p ∈ E_f. Only the single **absorbing orbit Ω** is degenerate — and Q-b
  never asked for the substrate to have no orbits other than the γ_p; it asked for one closed orbit
  of length log p per prime, which K has.
- The remaining defense is (Tors) as a standing hypothesis of the *theory*: [x-06] p. 11, verbatim,
  *"What we know for certain is that the restrictions of P^× to μ(κ(x)) must have finite kernels
  (condition E_tors)"*. That is a good defense of **(b-X₀)** and I accept it. It is **not** a defense
  of **(b-Y₀)**, because Y₀ is defined by Deninger *as the closure of the periodic orbits*, and
  Theorem 8.2 (p. 50, unconditional for Spec Z) computes that closure **in X̊(C)** and finds
  X̊(S¹) ⊄ E_tors. The closure of the admissible periodic locus is **not admissible**. One may
  redefine Y₀ as Y₀^E := (X̌₀(S¹) ∩ X̌₀(C)_E) ×_{Q>0} R^{>0} — and then the theorem holds — but that
  is *not* the object [x-03] p. 49 and [x-06] p. 12 name, and it is *not* "the closure of the union
  of all periodic orbits" in the space where Deninger takes the closure.

**Collateral damage to the "no escape" framing.** Because the target of a map into a packet is
indiscrete (face (a)), continuity of f on the periodic part is free; and the proof of Theorem O-2
shows more than quasi-compactness of K: for **any** compact metrizable flow Y = (⨆_p γ_p^Y) ∪ A
whose closed orbits γ_p^Y (length log p, one per prime) are isolated with limit set A, and any
equivariant map A → Ω (which exists whenever the flow on A admits a time-function into
R/⟨log q : q ∈ Q>0⟩ — e.g. A a suspension with return time log 2), the induced
f : Y → Y₀ ⊆ X₀^full with f|_{γ_p^Y} the orbit parametrization onto γ_p **is continuous and
equivariant with f(γ_p^Y) ⊂ Γ_p**. (Continuity at a ∈ A: for U ∋ f(a), steps 1–4 give
f^{-1}(U) ⊇ A ∪ ⋃_{p∉F} γ_p^Y, whose complement ⋃_{p∈F}γ_p^Y is compact hence closed.) So on the
E-free/unitary target, the arithmetic obstruction to S4 has evaporated and what remains is the
purely topological question of whether a 3-dimensional lamination with that orbit structure exists —
i.e. exactly the S3/R12–R13 rows. I do **not** claim S4 is alive; a lamination has 2-dimensional
leaves so its closed orbits cannot be isolated, and my Y is not a lamination. I claim only that
**face (b) no longer supplies the obstruction on that target.**

---

## §4. The theorem's honest scope

**Holds, fully re-derived, no gap found:**

> Let **E be an admissible class of characters** in the sense of [x-03] Def. 4.1 (p. 27) — so every
> character in E satisfies **(Tors)** — with E ⊆ E_max, and let
> **X₀^E = X̌₀(C)_E ×_{Q>0} R^{>0}** for **X₀ = Spec Z**, carrying the **quotient topology** of
> X̌₀(C)_E × R^{>0} (or **any finer** topology, e.g. the Thm. 7.10 coproduct). Then every nonempty
> **quasi-compact** subset K ⊆ X₀^E invariant under the **whole** R-action satisfies W ≡ ∞ on K,
> hence K ⊆ ⨆_p Γ^E_p, hence K meets only **finitely many** packets. Consequently no continuous
> flow-equivariant map from a nonempty quasi-compact space with an **R**-action into X₀^E reaches
> infinitely many packets, and **Q-b is NO for X₀^E** — with the lamination hypotheses (dim 3,
> metrizability, foliated flow, transverse measure, ε ≡ +1, one-orbit-per-prime) unused.

**Which E:** every admissible E, including E_f, E_fg, E_fd, E_fd0, E_max, E_tors, and probe A's
one-orbit cut classes E(a₀) — because the only property consumed is (Tors), which Def. 4.1 imposes
on all of them. Admissibility is **necessary**, not decorative: §3 breaks the theorem exactly where
(Tors) is dropped.

**Which topology:** the quotient topology of record, and every **finer** one. Not a coarser one
(the adjudication's justification for coarser topologies is backwards, §1.6).

**Compact vs quasi-compact vs non-compact:**
- *quasi-compact + two-sided R-action* — killed, on X₀^E.
- *quasi-compact + forward semiflow only* — **not covered**; on Y₀ there is a compact
  forward-invariant set κ meeting every packet (§2, Line 2).
- *non-compact* — explicitly allowed: Y_∞ = ⨆_p R^{>0}/p^Z maps in continuously and equivariantly
  hitting every packet in exactly one orbit (verified, §2 Line 5). Deninger's own p. 40 question,
  which imposes no compactness, is therefore **not** answered by face (b).
- *dimension* — never used, and never delivered: the witness is 1-dimensional; nothing here shows a
  non-compact **3-dimensional** lamination with exactly one orbit per prime can or cannot map in.

**Which target:**
- **X₀^E** — theorem stands.
- **Y₀^E = (X̌₀(S¹) ∩ X̌₀(C)_E) ×_{Q>0} R^{>0}** — theorem stands (it is a flow-invariant subspace
  of X₀^E, and a quasi-compact invariant subset of a subspace is one of X₀^E).
- **Y₀ = X̌₀(S¹) ×_{Q>0} R^{>0} as printed at [x-03] p. 49 and [x-06] p. 12, and X₀^full =
  X̌₀(C) ×_{Q>0} R^{>0}** — theorem **FALSE** (§3).
- **X̄₀, the conjectural Arakelov compactification (pp. 39–40)** — untouched, as the adjudication
  says; correctly identified as a different, unconstructed target.

**Required edits before decisive action (concrete).**
1. `qstar-adjudication.md` §1 face-(b) row, §4(D), and §9 novelty item 6: replace
   "for X₀ and for the flow-invariant subspace Y₀ = X̌₀(S¹)×_{Q>0}R^{>0}" with "for X₀^E and for
   Y₀^E := (X̌₀(S¹) ∩ X̌₀(C)_E) ×_{Q>0} R^{>0}", and add: *"For the E-free unitary system printed at
   [x-03] p. 49 / [x-06] p. 12 the statement is false (`face-b-refuter-O.md` §3); the closure of the
   periodic locus computed by Thm. 8.2 is not contained in any admissible class."*
2. §9 novelty item 10 and §4's closing paragraph: **withdraw** "compactness is the exact obstruction".
   Replace with: "quasi-compactness is what the proof consumes; on the E-free unitary target the
   exact obstruction is (Tors), and the non-compact witness Y_∞ is 1-dimensional, so it does not
   isolate compactness among Q-b's hypotheses."
3. §2's robustness sentence: fix the direction (finer preserves face (b); coarser does not).
4. §4(B): state that **two-sided** invariance is used, and record κ = q(X̊₀(S¹)×[1,2]) as the compact
   forward-invariant set meeting every packet in Y₀.
5. §5's independence claim: qa-kill's Theorem 2 is mechanism-independent but **hypothesis-dependent**
   — its bound q_β ≥ ν/(ν′e) is vacuous when e = |ker(Ψ|_μ)| = ∞. All three face-(b) routes stand or
   fall with (Tors).

**Bottom line for the program.** S4's kill *for the target S4 names* — Deninger's X₀ with an
admissible class — is sound and I could not break it after six lines of attack. But the statement
the program is about to act on is broader than what is true, in a way that touches Deninger's own
proposed replacement system, and the "compactness is the exact obstruction" framing (which is what
makes the kill feel decisive) is wrong. Fix the scope, then act.

**New items this note banks** (all single-check, mine alone):
- **Lemma O-1**: X̊(S¹) is compact metrizable (hence X̊₀(S¹) is compact).
- **κ = q(X̊₀(S¹)×[1,2])** is a compact forward-invariant subset of Y₀ meeting every packet; and
  κ ≈ {W ≥ 1} ∩ Y₀ — the weight is exactly the colimit-depth function.
- **Theorem O-2**: the counterexample K (nonempty, quasi-compact, R-invariant, one genuine periodic
  orbit of length log p inside Γ_p for every p) in Deninger's printed Y₀.
- The **absorption lemma** (§3 step 3): every Q>0-invariant open set of X̌₀(S¹) containing the trivial
  generic character contains χ_p for all but finitely many p — because F_{ν}χ_p → the trivial
  character along ν = lcm of residue orders. This is the mechanism by which packets accumulate on the
  *degenerate* generic point, distinct from Thm. 8.2's accumulation on unitary points.
- The corrected robustness direction for the topology of record.

— end of face-(b) refuter O —
