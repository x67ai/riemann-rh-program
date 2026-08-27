# Castelnuovo–Severi/Hodge index on a surface from Riemann–Roch + ampleness: the non-circularity re-derivation

**Deliverable:** C3-r M1 — the non-circularity gate. Per the direction file and the binding
adjudication (`results/adjudication-C3.json`), **no C3-r substrate work may claim S4 credit
before this document exists**; it is the discharge, in writing, of the load-bearing [RU] flag
raised by the wave-1 arakelov scout ("the load-bearing non-circularity claim … should be
re-derived in the design phase").

> **DATED CITATION PASS (2026-08-27). Read before citing.** An independent novelty re-check
> (`results/arxiv/novelty-check.md`) returned **ANTICIPATED-BY** for this note — correctly, and the
> note says so itself in the next paragraph. Its ~14 citation obligations were re-verified against
> primary sources before being applied (Crossref, zbMATH Open, the arXiv abstract pages, Numdam,
> the Clay Mathematics Institute's own PDF, and a publisher-grade scan of Grothendieck 1958);
> per-source evidence in `results/arxiv/citation-verification/`. The note now carries §12, a
> reference list of 22 verified entries, and the §9 lineage has been rewritten against them. Six of
> the re-check's own claims did **not** survive verification and were **not** executed as written:
> (i) "Milne says *avoid the Weil conjecture*" — the string "avoid" occurs **zero** times in his
> paper; (ii) the Bombieri passage is on **p. 9 alone**, not pp. 9–10, and the live CMI URL is under
> `/2022/05/`, not `/2022/06/`; (iii) Kleiman's **Remark 3.10** is a characteristic-zero remark
> about homological versus numerical equivalence and cannot carry the sentence it was cited for —
> his **Remark 4.5** is the dependency-ledger remark, and it is the one used here; (iv) Ito–Ito–
> Koshikawa's Remark 1.3 is not a "non-circularity audit" whose verdict was clean — it is a
> published disclosure that they *did not* attempt to avoid the Weil conjecture, which is a
> stronger precedent, quoted here as what it is; (v) Ancona's §1 does not publish this note's §9
> "verbatim" and makes no independence claim at all; (vi) "Grothendieck's Prop. 2.1 needs no
> positivity hypothesis on D" overstates — it assumes `D² > 0`, which *is* a positivity hypothesis,
> just a much weaker one than this note's Lemma. Two further corrections of record: the
> "G. Bronowski / (1958)" bibliographic corruption is in **Grothendieck's own 1958 printed
> bibliography**, not in a later retranscription (and his Segre start page, 167, is also wrong —
> the true range is 157–163); and Segre 1937 predates Weil 1948 by **eleven** years, not ten.

**Status (read before citing).** This is a **re-derivation of standard material for the program
record; zero novelty is claimed.** Every statement below is graduate-textbook algebraic
geometry. Its value to the program is precisely the audit trail: the Hodge-index/
Castelnuovo–Severi inequality — the positivity engine of the only **positivity mechanism** that
has ever proved an RH† — is proved from Riemann–Roch on the surface, Serre duality, and
ampleness, **with no zeta-function, L-function, or RH input anywhere**. Both Session-6 killers
re-derived this argument independently; the lineage was tier-1-verified (killer-2 and the
adjudicator). The verification is recorded as "Verified in the brief's favor" in the direction
file's Phase-4 verdicts (`directions/C3-geometric-substrate.md`); the adjudication's own
wording is "the M1 gate is verified sound by both killers" (`results/adjudication-C3.json`;
`results/verdicts-c3d1.json` kill:C3 minor finding item (4), kill2:C3 minor finding item (1)).

† "Positivity mechanism" is the operative qualifier (restored per referee pass; it is the
direction file's own phrasing): RH for curves over finite fields was ALSO proved by the
elementary auxiliary-polynomial method of Stepanov (1969), streamlined and completed by
Bombieri, "Counting points on curves over finite fields (d'après S. A. Stepanov)," Sém.
Bourbaki Exp. 430 (1972/73), Springer LNM 383 (1974), 234–241 — a proof consuming only
Riemann–Roch on the *curve*: no surface, no Hodge index, no positivity engine. Deligne's
Weil I amplification is likewise a distinct engine. The claim above concerns the Hodge-index
positivity route only.

**Conventions.** X is a smooth projective (geometrically irreducible) surface over an
algebraically closed field k of **arbitrary characteristic** (char p included; nothing below is
characteristic-zero). Divisors are considered up to numerical equivalence where stated; K = K_X
is the canonical divisor; D·E is the intersection number; h^i(D) = dim_k H^i(X, O_X(D));
χ(D) = h⁰ − h¹ + h². "D numerically nontrivial" means D·E ≠ 0 for some divisor E. For a
non-closed base field, all quantities below are stable under base change to the algebraic
closure, so the inequalities descend; we work over k = k̄ throughout.

---

## 1. What is being certified and why

The C3-r mechanism template loads ALL of its Riemann-hypothesis content on a Hodge-index-type
inequality (S4). The known trap — enforced by barrier zoo IV.1 and the C1 precedent — is a
positivity step that is Weil positivity in disguise, i.e. an inequality whose proof secretly
consumes the statement to be proved. The function-field template is the existence proof that the
trap is avoidable: there, the master inequality has a proof whose inputs are
**Riemann–Roch on the surface, Serre duality, and ampleness** — nothing else. This document
re-derives that proof in full, itemizes the provenance of every input (§8), and states the
F_q-degeneration clause (§7): the inequality proved here is exactly the inequality Weil's proof
of RH for curves consumes, and it is proved before and independently of that application. That
is the non-circularity claim the direction leans on, now on paper rather than recalled.

**The published record, named here rather than left implicit (2026-08-27).** None of §§3–7 is new,
and the note has always said so; what the 2026-08-27 citation pass adds is the specific published
loci, so that a reader can check the claim without taking this document's word for anything.
Milne's survey [Mil16] publishes §§3–7 end to end and in the same order — Riemann–Roch on a
surface, Serre duality and adjunction (§1, p. 7); the ample-meets-effective lemma (Lemma 1.1,
p. 8); the Hodge index theorem proved from Riemann–Roch (Theorem 1.2, p. 8); the signature
corollaries (1.3–1.4, p. 9); the Castelnuovo–Severi inequality on `C₁ × C₂` (Theorem 1.5, p. 9);
and the deduction of `|N − q − 1| ≤ 2g√q` (p. 10) — closing with the observation this note's §7
clause restates: *"Note that, except for the last few lines, the proof is purely geometric and
takes place over an algebraically closed field. This is typical: study of the Riemann hypothesis
over finite fields suggests questions in algebraic geometry whose resolution proves the
hypothesis"* [Mil16, Aside 1.8, p. 10].

Independently, and with a **different** Weil-free input list, Bombieri's official Clay problem
description states the same thing about the same theorem [Bom00, p. 9]: *"The algebraic index
theorem for surfaces is essentially due to Severi in 1906 [Sev, §2, Teo. I]. The proof uses the
Riemann–Roch theorem on X and the finiteness of families of curves on X of a given degree; no
other proof by algebraic methods is known up to now, although much later several authors
independently rediscovered Severi's argument."* His inputs are Riemann–Roch **plus finiteness of
families of curves of given degree**; this note's are Riemann–Roch **plus ampleness** (with Serre
duality and Nakai–Moishezon). Neither list contains the Weil conjectures. Note also, because the
note must not have it both ways: on Bombieri's reading Segre 1937, Bronowski 1938, Mattuck–Tate
1958 and Grothendieck 1958 are *rediscoveries of Severi's argument*, not methodologically
independent routes. What the record supports is that several **published, Weil-free** derivations
exist — not that they are independent of one another.

Finally, the certification is not academic: the leading contemporary RH program adopts exactly
this route and states the same logical requirement in its own words. Connes and Consani [CC19]
describe the "Riemann–Roch strategy" as trading the location of the zeros for the non-positivity
of a quadratic form `s(f, f)`, note that in the function-field case *"the most conceptual proof was
obtained by applying the Riemann–Roch formula on the square of the curve defining the function
field … if one assumes the positivity of s(f, f) > 0 for some f, it is the existence part of the
Riemann–Roch theorem which yields a contradiction"* [CC19, §3], and identify what is missing as
*"the implementation of a Riemann–Roch formula whose topological side is ½ D · D"* [CC19, §3.1].
That is this note's (IN1)-upstream-of-RH claim, made by the program that needs it.

## 2. Inputs, with provenance (and what is NOT an input)

The proof uses exactly the following, each a standard theorem with no analytic or arithmetic
content about zeta or L-functions:

- **(IN1) Riemann–Roch on a surface.** χ(D) = χ(O_X) + ½·D·(D − K). [Hartshorne, *Algebraic
  Geometry*, Thm. V.1.6; valid over any algebraically closed field.]
- **(IN2) Serre duality.** h²(D) = h⁰(K − D). [Hartshorne III.7.6.]
- **(IN3) Ample meets effective positively.** If H is ample and E is a nonzero effective
  divisor, then E·H > 0. [Degree of a nonzero curve in a projective embedding is positive;
  equivalently the easy direction of Nakai–Moishezon.]
- **(IN4) Ampleness absorbs any divisor.** For H ample and D arbitrary, D + nH is ample for all
  n ≫ 0. [Hartshorne, Exercise II.7.14(b); standard.]
- **(IN5) Trivial positivity.** h⁰, h¹, h² ≥ 0, hence h⁰(D) + h²(D) ≥ χ(D).
- **(IN6) The intersection pairing on Num(X)** is a well-defined, nondegenerate symmetric
  bilinear form on a finitely generated group. [Hartshorne V.1; nondegeneracy is the definition
  of numerical equivalence. Finite generation of Num(X) is the Néron–Severi theorem — proved by
  Picard-variety/finiteness arguments, no zeta input; it is consumed ONLY for ρ < ∞ in the
  signature statement §5, which sits off the load-bearing chain to §§6–7.] **This scoping is
  Grothendieck's own**, in one sentence, in the paragraph immediately following his Théorème 1.1:
  *"Ce théorème semble utiliser, dans son énoncé, le théorème de Néron [5] impliquant que E est de
  dimension finie. Il serait évident comment formuler le théorème 1 si on voulait ignorer le
  théorème de Néron."* [Gro58, p. 208] — the finiteness input enters the *statement*, not the
  *proof*, and the statement can be reformulated without it.]
- **(IN7) Nakai–Moishezon criterion (hard direction).** On a surface, if H² > 0 and H·C > 0 for
  every irreducible curve C ⊂ X, then H is ample. [Hartshorne Thm. V.1.10; the proof is
  cohomological (Riemann–Roch plus effectivity bootstrapping) — no zeta content. Consumed only
  in §6, to certify H = ξ₁ + ξ₂ ample. An elementary route avoiding it exists —
  m(ξ₁ + ξ₂) = p₁*(mP) + p₂*(mP′) is very ample for m ≫ 0 as the Segre-composed embedding of
  very ample divisors on the factors, an (IN4)-grade fact — but the criterion is what §6's
  printed verification uses, so it is listed as the input it is. **Ledger note (2026-08-27).**
  Grothendieck's own route to the index theorem [Gro58, §2] uses neither (IN4) nor (IN7): his
  auxiliary Proposition 2.1 assumes **only** `D² > 0` — no ampleness, no hyperplane section, no
  effectivity, and no sign condition on `D` itself (he replaces `D` by `−D` if need be) — and he
  gets the single positive square directly from a hyperplane section `H`, since `l(H) > 1` gives
  `H² > 0` by his (2.4). Adopting that route would shorten this ledger, but §6 would still need
  `m(ξ₁ + ξ₂)` very ample, so the honest accounting is that **(IN7) can be replaced by the
  Segre-embedding fact already named here**, not that two inputs disappear.]

**Not inputs:** the zeta function of any curve or surface; point counts; the Weil conjectures
in any form; positivity of any explicit-formula functional; any spectral or Hilbert-space
statement; any characteristic-zero comparison. No step of the proof (§§3–6) mentions them.
§7's degeneration clause consumes rationality and the functional equation of Z(C, T) —
Riemann–Roch-on-the-curve facts with no RH content — and produces point counts as OUTPUTS
(N₁ = Γ·Δ), exactly as itemized in the §8 ledger; §10 mentions the explicit formula only
inside the IV.10 fence, to state what the Tate-curve surfaces cannot host.

## 3. Lemma (effectivity criterion; Hartshorne V.1.8 lineage)

**Lemma.** Let H be ample on X and let D be a divisor with D² > 0 and D·H > 0. Then nD is
effective (h⁰(nD) > 0) for all sufficiently large n.

*Proof.* By (IN1), χ(nD) = χ(O_X) + ½·nD·(nD − K) = (n²/2)·D² − (n/2)·D·K + χ(O_X) → ∞ as
n → ∞, since D² > 0. By (IN2), h²(nD) = h⁰(K − nD). Since D·H > 0,
(K − nD)·H = K·H − n·(D·H) < 0 for all n ≫ 0; but h⁰(K − nD) > 0 would make K − nD linearly
equivalent to an effective divisor E ≥ 0 with (K − nD)·H = E·H ≥ 0 (zero only for E = 0,
positive otherwise by (IN3)) — impossible. So h⁰(K − nD) = 0 for all n ≫ 0, and by (IN5),
h⁰(nD) ≥ χ(nD) − h²(nD) = χ(nD) → ∞. ∎

*(This is the exact locus where the hypothesis D·H > 0 is consumed: it kills the h² term. The
compressed sketch recorded in the verdict files — "χ(nD) → ∞ forces ±nD effective" — silently
routes through this Lemma applied to an auxiliary ample divisor; the full route is Theorem 4.)*

## 4. Theorem (Hodge index; Hartshorne Thm. V.1.9 lineage)

**Theorem.** Let H be ample on X and let D be a divisor with D·H = 0 and D numerically
nontrivial. Then D² < 0.

*Proof.* Suppose for contradiction D² ≥ 0.

**Case 1: D² > 0.** By (IN4) choose m ≫ 0 with H′ := D + mH ample. Then
D·H′ = D² + m·(D·H) = D² > 0, so the Lemma applies to D with the ample divisor H′: nD is
effective and nonzero (D is numerically nontrivial, so nD ≢ 0) for some large n. By (IN3),
nD·H > 0, contradicting D·H = 0.

**Case 2: D² = 0.** Since D is numerically nontrivial, pick E with D·E ≠ 0. Replace E by
E′ := (H²)·E − (E·H)·H; then E′·H = (H²)(E·H) − (E·H)(H²) = 0 and
D·E′ = (H²)(D·E) − (E·H)(D·H) = (H²)(D·E) ≠ 0 (H² > 0 by (IN3): H ample ⟹ some multiple of H
is effective and nonzero, and it meets H positively, so H² = H·H > 0). For an integer n, set
D′ := nD + E′. Then D′·H = n·(D·H) + E′·H = 0 and
D′² = n²·D² + 2n·(D·E′) + E′² = 2n·(D·E′) + E′². Choosing n large with the sign of n·(D·E′)
positive gives D′² > 0 with D′·H = 0. If D′ is numerically nontrivial this contradicts Case 1;
and D′ numerically trivial is impossible since D′² > 0. Contradiction either way.

Hence D² < 0. ∎

## 5. Corollary (the signature statement)

**Corollary.** On Num(X) ⊗ R (rank ρ), the intersection form has signature (1, ρ − 1): it is
positive definite on the line R·H and negative definite on H^⊥.

*Proof.* H² > 0 gives the positive line. For the negative-definiteness of H^⊥: the Theorem
gives x² < 0 for every nonzero **rational** class x ∈ H^⊥ (clear denominators and apply the
Theorem to the resulting integral divisor class; numerical nontriviality is exactly nonvanishing
in Num). Negative *semi*definiteness on the real span follows by density and continuity of the
quadratic form. If some nonzero real x ∈ H^⊥ had x² = 0, then x would lie in the radical of the
semidefinite form restricted to H^⊥ (an isotropic vector of a semidefinite form is radical);
the radical is a rational subspace (the form and H^⊥ are defined over Q), so it would contain a
nonzero rational class y ∈ H^⊥ with y·z = 0 for all z ∈ H^⊥ and y·H = 0 — i.e. y numerically
trivial (write any w as λH + w^⊥), contradicting y ≠ 0 in Num(X) ⊗ Q. ∎

## 6. Corollary (Castelnuovo–Severi on C × C′)

Let C, C′ be smooth projective curves over k, S = C × C′, ξ₁ = {pt} × C′, ξ₂ = C × {pt}. Then
ξ₁² = ξ₂² = 0, ξ₁·ξ₂ = 1, and H := ξ₁ + ξ₂ is ample ((IN7) Nakai–Moishezon: H² = 2 > 0, and
every irreducible curve on S meets ξ₁ or ξ₂ positively and neither negatively). For a divisor D on S
write the **bidegree** (d₁, d₂) := (D·ξ₁, D·ξ₂) (for the graph Γ_f of a morphism f: C → C′,
(d₁, d₂) = (1, deg f)).

**Corollary (Castelnuovo–Severi inequality).** D² ≤ 2·d₁·d₂, with equality only if D is
numerically equivalent to d₂ξ₁ + d₁ξ₂.

*Proof.* Set D′ := D − d₁ξ₂ − d₂ξ₁. Then D′·ξ₁ = d₁ − d₁ = 0 and D′·ξ₂ = d₂ − d₂ = 0, hence
D′·H = 0. By the Theorem (and its trivial extension: D′² ≤ 0, with < 0 unless D′ ≡ 0),
0 ≥ D′² = D² − 2(d₁·(D·ξ₂) + d₂·(D·ξ₁)) + (d₁ξ₂ + d₂ξ₁)² = D² − 4d₁d₂ + 2d₁d₂ = D² − 2d₁d₂. ∎

The classical "equivalence defect" formulation and the positivity of Weil's trace form on
correspondences are algebraic reformulations of this inequality; the historical order (§9) ran
through exactly this statement.

## 7. The F_q degeneration clause: this is the inequality Weil's proof consumes

This section states, with the short computation, that the inequality of §6 — proved above from
(IN1)–(IN6) only — is the entire positivity input of Weil's proof of RH for curves over finite
fields. **That is the point of M1:** the same inequality the C3-r template must produce on an
arithmetic substrate is, in its home territory, proved with no RH input, so demanding an
RR + ampleness derivation (rather than a posited positivity) is a coherent, historically
grounded non-circularity contract.

Let C be a smooth projective geometrically irreducible curve of genus g over F_q, S = C × C
(base-changed to F̄_q for the intersection theory), F: C → C the q-power Frobenius, Γ = Γ_F its
graph, Δ the diagonal, N₁ = #C(F_q). The three standard geometric facts consumed — each an
intersection-theoretic computation with no zeta input:

- **(W1)** Γ has bidegree (1, q); Δ has bidegree (1, 1).
- **(W2)** Δ² = 2 − 2g (self-intersection = degree of the normal bundle N_Δ ≅ T_C) and
  Γ² = q(2 − 2g): via the embedding (id, F): C ≅ Γ ⊂ S one has T_S|_Γ ≅ T_C ⊕ F*T_C, so
  deg N_{Γ/S} = deg(T_S|_Γ) − deg T_Γ = deg F*T_C = q·deg T_C = q(2 − 2g).
- **(W3)** N₁ = (Γ·Δ): Γ and Δ meet transversally because dF = 0, so 1 is never an eigenvalue
  of the tangent map; the intersection points are exactly the F_q-rational points.

Apply §6 to D = rΔ + sΓ for integers r, s: bidegree (r + s, r + sq), and with t := (Γ·Δ),

D² = r²(2−2g) + 2rst + s²q(2−2g) ≤ 2(r+s)(r+sq).

Expanding and simplifying: g·r² − rs·(t − 1 − q) + g·q·s² ≥ 0 for all integers r, s, hence (by
homogeneity and density) for all real r, s; the discriminant condition gives

(t − (q+1))² ≤ 4g²q, i.e. **|N₁ − (q + 1)| ≤ 2g·√q.**

Replacing F by F^k gives |N_k − (q^k + 1)| ≤ 2g·q^{k/2} for every k ≥ 1; by the standard
power-sum/functional-equation bookkeeping (rationality of the zeta function of C and the α ↦ q/α
pairing — both consequences of Riemann–Roch on the *curve*, again with no RH input) this is
equivalent to |α_i| = √q for every Frobenius eigenvalue, i.e. RH for C. (The ⟹ direction is
the generating-function no-cancellation fact: the log-derivative generating function has
residue −m_α at T = 1/α, so poles at distinct points of equal modulus cannot cancel; the
uniform bound then forces radius of convergence ≥ q^{−1/2}, i.e. max_i |α_i| ≤ √q, and the
α ↦ q/α pairing pins equality.) Every input in this
chain is listed in §8; none is a zeta positivity.

**Consistency note with the M0 note (`results/c3-r/m0-axiom-note.md` §3.5).** The bidegrees
(1, q^k) of Γ_{F^k} are only the MAIN terms q^k + 1 of N_k; the zero side −Σα_i^k lives
exclusively in the Δ-intersection (W3). The positivity engine acts on the trace side through
§6's inequality — degrees alone never see a zero. (Numerically spot-verified in the
adjudication on y² = x³ + x + 1 over F₇: bidegrees (1,7), (1,49), (1,343) against counts
5, 55, 380.)

## 8. Non-circularity audit (step-by-step input ledger)

| Step | Uses | Provenance | Zeta/RH content |
|---|---|---|---|
| Lemma §3 growth of χ(nD) | (IN1) RR on surfaces | Hartshorne V.1.6 | none |
| Lemma §3 killing h² | (IN2) Serre duality + (IN3) | Hartshorne III.7.6; projective degree | none |
| Theorem §4 Case 1 | Lemma + (IN4) D+mH ample + (IN3) | Hartshorne Ex. II.7.14(b) | none |
| Theorem §4 Case 2 | (IN6) linear algebra in Num(X) | Hartshorne V.1 | none |
| Corollary §5 | Theorem + Q-rationality of Num | linear algebra | none |
| Corollary §6 (CS) | Theorem on C × C′ + (IN7) ampleness of H = ξ₁+ξ₂ | (IN7) Nakai–Moishezon, Hartshorne Thm. V.1.10 (cohomological proof) | none |
| §7 (W1)–(W3) | bidegree/normal-bundle/transversality computations | standard; dF = 0 | none |
| §7 discriminant step | §6 applied to rΔ + sΓ | quadratic forms | none |
| §7 closing equivalence | rationality + FE of Z(C, T) from RR on the curve | Weil rationality (RR-based) | none (no RH input; RH is the OUTPUT) |

**Statement of the non-circularity claim (the deliverable).** The Hodge-index/
Castelnuovo–Severi inequality on a surface, in any characteristic, **has a proof** from
Riemann–Roch on the surface, Serre duality, and ampleness alone — **a** proof, not **the** proof:
Bombieri's Clay description records a different Weil-free route through Riemann–Roch plus
finiteness of families of curves of given degree, attributed to Severi 1906 [Bom00, p. 9; Sev06],
and Segre 1937 and Bronowski 1938 are two more, which Grothendieck credits by name in the very
statement of his theorem — *"Théorème 1.1 (Hodge–Segre–Bronowski)"* [Gro58, p. 208], alongside
Hodge's analytic proof of the same year [Hod37]. No zeta function, no L-function, no point
count, no explicit-formula positivity, and no statement equivalent to or implied by any Riemann
hypothesis appears among its inputs. In particular, in the function-field template the
positivity engine is demonstrably **not Weil positivity in disguise**: it exists prior to, and
is consumed by, the RH proof — not conversely. This is the fact the C3-r S4 contract references,
and with this document on disk the contract's [RU] debt is discharged.

**Scope of the claim.** This certifies non-circularity of the *function-field template's*
engine. It does NOT assert that any arithmetic substrate exists on which the analogous
inequality can be derived (that is M2c/M3/M4, all open), and it confers no S4 credit by itself
on any substrate proposal — it is the gate such proposals must pass through, in the form: an
index inequality claimed on a substrate must be DERIVED from RR + effectivity/theta input on
that substrate and must degenerate to the present statement over F_q.

**Why the arithmetic Hodge index theorem is not the missing piece (rewritten 2026-08-27).** The
one-line objection to the paragraph above is that an arithmetic analogue of the Hodge index
theorem is already a theorem, so the substrate problem must be solved. It is not, and the reason
is a matter of codimension, in the published record. The arithmetic Hodge index theorem is a
statement about **codimension-one** arithmetic cycles: on a regular arithmetic variety
`X → Spec O_K` of relative dimension `n`, if `M̄` is a Hermitian line bundle whose generic-fiber
class is primitive against an ample `L̄` (`M_K · L_K^{n−1} = 0`), then `M̄² · L̄^{n−1} ≤ 0`, with
equality exactly when `M̄` is pulled back from the base — Faltings [Fal84] and Hriljac [Hri85] for
arithmetic surfaces, Moriwaki [Mor96] for all `n`, and in the adelic-line-bundle setting
Yuan–Zhang [YZ17]. Three things follow, each with a source.

1. It is an inequality of **one sign, in codimension one** — Moriwaki's Theorem A(2) is
   `deg̑(x · L^{d−1}(x)) < 0`, the `p = 1` instance of the Gillet–Soulé sign
   `(−1)^p deg̑(x · L^{d+1−2p}(x)) > 0` [GS94]. It is the Arakelov shadow of the classical index
   theorem **for divisors**, not a positivity statement about a pairing in the middle dimension.
2. Everything above codimension one — which is exactly where a Weil-positivity argument on a
   *surface-like* arithmetic object would have to live — is open: *"the high-codimensional case of
   the Gillet–Soulé conjecture is still wide open"* [YZ17, arXiv:1304.3538v1, p. 2], and
   Künnemann's survey confirms only `p = 0`, arithmetic surfaces, and Moriwaki's codimension-one
   part [Kün95, p. 115].
3. Faltings–Hriljac **is** the arithmetic-surface case — *"when X is an arithmetic surface … the
   conjecture is a consequence of the Hodge index theorem of Faltings and Hriljac"* [Kün95, p. 115]
   — so it cannot supply more on a surface than the codimension-one inequality already gives.

The gate above therefore stands as written: what a substrate must supply is not a codimension-one
negativity statement, which exists, but a middle-dimensional positivity calculus on a doubled
object, which does not.

**The reading §8 must answer, and its answer.** Deninger reads the Néron–Tate positivity in the
opposite direction — as *support* for a positivity route to RH: with the height pairing on
`CH¹(E)₀ = E(**Q**) ⊗ **Q**` negative definite by Néron and Tate, *"the restriction of the Hodge
inner product to the 1-eigenspace of θ would be identified with the negative of the
(negative-definite) Néron–Tate height pairing"*, and *"hence our remark may be interpreted as
support for the Hilbert–Pólya strategy of proving the Riemann hypotheses via positivity"*
[Den10, §1]. Two features of his own wording contain the answer and are worth preserving. His
formalism is **conjectural** throughout — "would imply", "would also help" — so the identification
is an expectation about a cohomology theory that does not yet exist; and the *support* runs from a
known positivity in codimension one **back** to the plausibility of that formalism, not forward
from any substrate to the inequality this note certifies. Read that way his remark and this note
agree: the positivity engine is real, RH-free, and upstream — and it is still waiting for a
substrate to run on.

**Two published precedents for this exact bookkeeping, so the exercise is not mistaken for an
idiosyncrasy.** Kleiman's 1968 exposé keeps the same ledger explicitly, separating what is proved
outright from what is conditional: *"By the Lefschetz fixed-point formula, χ = (Δ²) … Hence, the
functional equation, derived with the aid of a Weil cohomology, is independent of cohomology.
Furthermore, this derivation does not depend on any unproved conjectures"* [Kle68, Rmk. 4.5,
p. 385], while his Theorem 4.7 is the template in which Hodge-type positivity sits logically
upstream of RH. And Ito, Ito and Koshikawa raise the identical dependency question about their own
proof of a Hodge-type positivity statement — and answer it in the negative, in print:
*"Let us recall again that if X is defined over a finite field, the Hodge standard conjecture for
X² and the Lefschetz standard conjecture for X imply the Weil conjecture for X, and Theorem 1.2
justifies the assumption. However, we did not attempt to avoid the Weil conjecture in our proof of
Theorem 1.2"* [IIK25, Rmk. 1.3]. That is the stronger precedent, because it establishes both that
the question is a recognized one *and* that answering it affirmatively is not automatic. Ancona's
Lemma 7.10 is the matching case where the proof *does* consume the Weil conjectures — its first
step invokes the functional-equation relation `ᾱ = q/α` on Frobenius eigenvalues — which is
entirely legitimate for him, since Deligne proved them, and is precisely the contrast this section
draws [Anc21, Lem. 7.10]. Milne keeps the same ledger twice more, in the abstract of [Mil22] and at
[Mil07, footnote 4 and Aside 9.4].

## 9. Lineage (as verified in the Session-6 adjudication cycle)

**(Rewritten 2026-08-27 against primary sources; the previous version's phrase "the first modern
non-circular derivation" for Mattuck–Tate 1958 was wrong by twenty-one years and is withdrawn.)**

- **F. Severi**, *Sulla totalità delle curve algebriche tracciate sopra una superficie algebrica*,
  Math. Ann. 62 (1906), 194–225 — on Bombieri's reading [Bom00, p. 9] the algebraic index theorem
  is "essentially due to Severi in 1906 [Sev, §2, Teo. I]", proved from Riemann–Roch on X plus
  finiteness of families of curves of a given degree. Milne's genealogy runs Severi 1903
  (the bi-additive form and its non-degeneracy conjecture) → Castelnuovo 1906 (σ(D, D) ≥ 0) →
  Zariski 1952 (Riemann–Roch for normal surfaces in characteristic p) [Mil16, pp. 12–13].
- **W. V. D. Hodge** (analytic, 1937), **B. Segre** (algebraic, 1937) and **J. Bronowski**
  (algebraic, 1938) — the index theorem itself, more than two decades before Mattuck–Tate and
  eleven years before Weil 1948. Grothendieck names his own theorem *"Théorème 1.1
  (Hodge–Segre–Bronowski)"* [Gro58, p. 208] and says of the positive-square half that
  Segre and Bronowski *"en donnent des démonstrations assez simples, valables en toute
  caractéristique"* — the characteristic-free claim is **Grothendieck's**, and is cited as his,
  not asserted as the two papers' own. Milne records the same in footnote 16: *"The Hodge index
  theorem was first proved by analytic methods in Hodge 1937, and by algebraic methods in Segre
  1937 and in Bronowski 1938."* (**Bibliographic warning.** Grothendieck's own 1958 printed
  bibliography carries the corruption "G. Bronowski … (1958)" and gives Segre's start page as 167.
  The correct entries are B. Segre, Ann. Mat. Pura Appl. (4) **16** (1937), **157**–163, and
  J. Bronowski, J. London Math. Soc. **13** (**1938**), 86–90. The error is in the 1958 original,
  not in any later retranscription.)
- **A. Mattuck, J. Tate**, *On the inequality of Castelnuovo–Severi*, Abh. Math. Sem. Univ. Hamburg
  22 (1958), 295–299 — the Castelnuovo–Severi inequality from Riemann–Roch on the product surface.
  Milne, footnote 15: in their introduction they ask "whether it does not follow from the general
  theory of surfaces", "apparently … forgotten that Weil had answered this question in 1941".
- **A. Grothendieck**, *Sur une note de Mattuck–Tate*, J. reine angew. Math. 200 (1958), 208–215;
  doi:10.1515/crll.1958.200.208 — the generalization to an arbitrary surface, with the numbered
  input list of §2 that this note's §2 parallels: (2.1) the Riemann–Roch inequality (which he
  derives from the RR *equality* plus Serre duality — i.e. it already folds in this note's (IN1),
  (IN2) and (IN5)), (2.2) Serre duality, (2.3) `l(D + D′) ≥ l(D′) if l(D) > 0`, and (2.4)
  `l(D) > 1 ⟹ D·H > 0` for a hyperplane section (this note's (IN3)). Milne's summary of what he
  did: *"In trying to understand the exact scope of the method of Mattuck and Tate, Grothendieck
  (1958a) stumbled on the Hodge index theorem. In particular, he showed that the
  Castelnuovo–Severi–Weil inequality follows from a general statement, valid for all surfaces,
  which itself is a simple consequence of the Riemann–Roch theorem for surfaces"* [Mil16, p. 13].
  (Grothendieck's (2.3) has **no** counterpart in this note's (IN1)–(IN7) list; anyone mapping the
  two ledgers should note that rather than force a match.)
- **E. Kani**, *On Castelnuovo's equivalence defect*, J. reine angew. Math. 352 (1984), 24–70;
  doi:10.1515/crll.1984.352.24 — an independent route to the defect inequality in characteristic
  p, extending Castelnuovo's more precise result (Milne, footnote 14).
- **I. Vainsencher, J. F. Voloch**, *On the Castelnuovo–Severi inequality*, J. reine angew. Math.
  390 (1988), 114–116; doi:10.1515/crll.1988.390.114 — a further short published treatment,
  sharpening Kani. *(Not read: De Gruyter paywall. Characterized from the zbMATH review only, and
  therefore described as a sharpening rather than as an independent proof.)*
- **E. Hallouin, M. Perret**, *From Hodge Index Theorem to the number of points of curves over
  finite fields*, arXiv:1409.2357 — the modern continuation, and an independent confirmation of
  this section's Hartshorne pins: they cite "[Har77, exercice 1.9, 1.10 p. 368]" for exactly the
  exercises named below. *(Unpublished preprint as of 2026-08; do not add a journal reference.)*
- **R. Hartshorne**, *Algebraic Geometry*, GTM 52, Ch. V §1 — the textbook consolidation used
  above: Thm. V.1.6 (Riemann–Roch), Thm. V.1.9 (Hodge index), Thm. V.1.10 (Nakai–Moishezon,
  = (IN7)), Exercises V.1.9–V.1.10 (Castelnuovo–Severi on C × C′ and Weil's bound
  |N − (q+1)| ≤ 2g√q along exactly the route of §7). N.B. Hartshorne's theorem and exercise
  numbering are distinct series: "Thm. V.1.9" (the Hodge index theorem) and "Ex. V.1.9" (the
  CS exercise) are different items that happen to share a number. Two sub-item pins in this
  note — "Cor. V.1.8" for the effectivity criterion and the "(b)" of "Ex. II.7.14" — are
  recalled at the letter level only (the statements themselves are re-proved in full above, so
  nothing load-bearing depends on them); an online letter-check was attempted 2026-08-26
  without a conclusive page image, and a 30-second check against a physical copy remains
  worthwhile before print citation.

Verification record: both killers independently re-derived the argument of §3–§4 and confirmed
the lineage (`results/verdicts-c3d1.json` kill:C3 minor finding item (4); kill2:C3 minor
finding item (1) and its literature flag "Mattuck–Tate … and Grothendieck … verified to exist
with content as recalled — the brief's M1 [RU] is discharged"); the direction file's Phase-4
verdicts ("Verified in the brief's favor," `directions/C3-geometric-substrate.md`) record
"M1's [RU] non-circularity fact TRUE (Hodge index from RR + ampleness re-derived;
Mattuck–Tate Abh. Hamburg 22 (1958) + Grothendieck Crelle 200 (1958) 208–215 confirmed)";
the adjudication file's own wording is "the M1 gate is verified sound by both killers"
(`results/adjudication-C3.json`).

## 10. The E_p × E_p baseline remark (scoped by barrier zoo IV.10)

The only surviving contact between this gate and the former Tate-curve material is the
following remark, scoped strictly by `BARRIER-ZOO.md` IV.10. On the **diagonal** surfaces
E_p × E_p (E_p = C/(Z ⊕ Z·i·log p/2π) the per-prime Tate curve of arXiv:2606.06604;
End(E_p) = Z — the coincidence (log p)² ∈ 4π²Q is refuted unconditionally via Gelfond–Schneider, Theorem 5 of the companion note "Products of the per-prime Tate curves of absolute geometry carry no correspondence calculus for the Weil explicit formula"; dated amendment 2026-08-27, this line previously hedged), the Néron–Severi group is
generically Zξ₁ ⊕ Zξ₂ ⊕ ZΔ, and the index inequality of §4–§6 **holds classically** — these
are classical complex abelian surfaces and nothing in §3–§6 is special to them. But per IV.10
the available correspondence data on them is **prime-blind**: the graphs of multiplication-by-m
carry Lefschetz data deg([m] − 1) = (m − 1)² — integer polynomials in m with no log p weight —
so no intersection number on these surfaces can host the explicit formula's transcendentally
weighted prime terms without hand-inserting the answer key (barrier IV.1 re-entry). The
cross-prime surfaces E_p × E_q are dead as substrate (off-diagonal NS rank 2: no diagonal, no
graphs — zoo IV.10; M2b/N2 struck by the adjudication) and **nothing in this document revives
them**. The baseline therefore contributes to M1 exactly one sentence: the index inequality is
available on the diagonal Tate-curve surfaces for whatever classical purpose a future brief can
state — with zero prime-facing content, per IV.10.

## 11. Traceability

All paths relative to `anthropic/rh-program/`.

| Item | Source |
|---|---|
| M1 mandate; "gates all S4 credit"; [RU] flag origin | `directions/C3-geometric-substrate.md` (Milestone ladder M1; S4 row; adjudication + recommission sections) |
| Adjudicated verification of the argument and lineage | `directions/C3-geometric-substrate.md` Phase-4 verdicts ("Verified in the brief's favor"); `results/adjudication-C3.json` ("the M1 gate is verified sound by both killers"); `results/verdicts-c3d1.json` kill:C3 minor finding (4), kill2:C3 minor finding (1) + literature flags |
| Hodge-index proof skeleton as re-derived by the killers | `results/verdicts-c3d1.json` (both killers; reproduced here in full with the auxiliary-ample and D² = 0 steps made explicit — see the report note accompanying this deliverable) |
| F₇ spot-check numbers (1,7)/(1,49)/(1,343) vs 5/55/380 | `results/adjudication-C3.json` computation b |
| IV.10 scope of the E_p × E_p remark; (m−1)² Lefschetz data; NS ranks | `BARRIER-ZOO.md` IV.10; `results/adjudication-C3.json` computation a |
| Non-circularity contract language (derive from RR + effectivity; F_q degeneration clause) | `directions/C3-geometric-substrate.md` S4 row (f1-scout contract clause) |

*(C3-r M1 deliverable. Standard material re-derived for the record; zero novelty claimed.
U.S. English. Written Session 6, 2026-08-26.)*

---

## 12. References (added 2026-08-27)

Every field below was verified against a primary source in the 2026-08-27 citation pass —
Crossref, zbMATH Open, Numdam, the arXiv abstract pages, the Clay Mathematics Institute's own
PDF, and the Göttingen (GDZ) publisher-grade scan of Grothendieck 1958. Per-source evidence:
`results/arxiv/citation-verification/`. Items not obtained in full text are marked.

- **[Anc21]** G. Ancona, *Standard conjectures for abelian fourfolds*, Invent. Math. **223**
  (2021), no. 1, 149–212; doi:10.1007/s00222-020-00990-7; arXiv:1806.03216. §1 ("Brief historical
  panorama") and Lemma 7.10; numbering as in arXiv:1806.03216v3. *(v3 post-dates Springer's
  online publication by four days and is very likely the published text, but that is an inference,
  not a verification.)*
- **[Bom00]** E. Bombieri, *Problems of the Millennium: the Riemann Hypothesis*, official problem
  description, Clay Mathematics Institute, 2000, 11 pp.;
  https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf. The passage used here is on
  **p. 9**. Reprinted as *The Riemann hypothesis*, in *The Millennium Prize Problems* (J. Carlson,
  A. Jaffe and A. Wiles, eds.), Amer. Math. Soc. and Clay Mathematics Institute, 2006, 107–124.
  *(The reprint's internal pagination for this passage was not independently verified; cite the CMI
  PDF's p. 9.)*
- **[Bro38]** J. Bronowski, *Curves whose grade is not positive in the theory of the base*,
  J. London Math. Soc. **13** (1938), 86–90; doi:10.1112/jlms/s1-13.2.86. *(Not read; fields from
  Crossref and zbMATH.)*
- **[CC19]** A. Connes and C. Consani, *The Riemann–Roch strategy: Complex lift of the Scaling
  Site*, in: *Advances in Noncommutative Geometry: On the Occasion of Alain Connes' 70th Birthday*
  (A. Chamseddine, C. Consani, N. Higson, M. Khalkhali, H. Moscovici and G. Yu, eds.), Springer,
  Cham, 2019, 53–125; doi:10.1007/978-3-030-29597-4_2; arXiv:1805.10501, §3 and §3.1.
- **[Den10]** C. Deninger, *The Hilbert–Polya strategy and height pairings*, in: *Casimir Force,
  Casimir Operators and the Riemann Hypothesis: Mathematics for Innovation in Industry and
  Science* (G. van Dijk and M. Wakayama, eds.), de Gruyter, Berlin, 2010, 275–284;
  doi:10.1515/9783110226133.275; arXiv:1001.1621, §1. (zbMATH Zbl 1225.14018 prints 275–283; the
  title is set "Polya", without the accent, in both the arXiv and De Gruyter records.)
- **[Fal84]** G. Faltings, *Calculus on arithmetic surfaces*, Ann. of Math. (2) **119** (1984),
  no. 2, 387–424; doi:10.2307/2007043.
- **[Gro58]** A. Grothendieck, *Sur une note de Mattuck–Tate*, J. reine angew. Math. **200**
  (1958), 208–215; doi:10.1515/crll.1958.200.208. Open-access scan:
  http://resolver.sub.uni-goettingen.de/purl?GDZPPN002178125.
- **[GS94]** H. Gillet and C. Soulé, *Arithmetic analogs of the standard conjectures*, in:
  *Motives* (Seattle, WA, 1991), Proc. Sympos. Pure Math. **55**, Part 1, Amer. Math. Soc.,
  Providence, RI, 1994, 129–140; doi:10.1090/pspum/055.1/1265527.
- **[Har77]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics **52**,
  Springer-Verlag, New York, 1977. Ch. V §1: Thm. V.1.6 (Riemann–Roch), Thm. V.1.9 (Hodge index),
  Thm. V.1.10 (Nakai–Moishezon), Exercises V.1.9–V.1.10 (Castelnuovo–Severi on `C × C′` and Weil's
  bound), p. 368.
- **[Hod37]** W. V. D. Hodge, *The base for algebraic varieties of given dimension*,
  J. London Math. Soc. **12** (1937), 58–63; doi:10.1112/jlms/s1-12.45.58 — the analytic proof of
  the index theorem, named alongside Segre and Bronowski by Grothendieck and by Milne. *(Not read;
  fields from Crossref.)*
- **[Hri85]** P. Hriljac, *Heights and Arakelov's intersection theory*, Amer. J. Math. **107**
  (1985), no. 1, 23–38; doi:10.2307/2374455.
- **[IIK25]** K. Ito, T. Ito and T. Koshikawa, *The Hodge standard conjecture for self-products of
  K3 surfaces*, J. Algebraic Geom. **34** (2025), no. 2, 299–330; doi:10.1090/jag/840;
  arXiv:2206.10086. Remark 1.3; numbering as in arXiv:2206.10086v1 (the published version is
  paywalled and was not read).
- **[Kan84]** E. Kani, *On Castelnuovo's equivalence defect*, J. reine angew. Math. **352** (1984),
  24–70; doi:10.1515/crll.1984.352.24; Zbl 0536.14016. *(Not read; content from the zbMATH
  review.)*
- **[Kle68]** S. L. Kleiman, *Algebraic cycles and the Weil conjectures*, in: *Dix exposés sur la
  cohomologie des schémas*, Advanced Studies in Pure Mathematics **3**, North-Holland, Amsterdam,
  and Masson & Cie, Paris, 1968, 359–386. Theorem 4.7 and **Remark 4.5** (p. 385). (His Remark
  3.10 is a characteristic-zero remark about homological versus numerical equivalence and is not
  what this note cites.)
- **[Kün95]** K. Künnemann, *Some remarks on the arithmetic Hodge index conjecture*, Compositio
  Math. **99** (1995), no. 2, 109–128; http://www.numdam.org/item?id=CM_1995__99_2_109_0.
- **[Mil07]** J. S. Milne, *The Tate conjecture over finite fields (AIM talk)*, preprint,
  arXiv:0709.3040 (2007), v2, 24 pp.; footnote 4 (p. 6) and Aside 9.4 (pp. 19–20).
- **[Mil16]** J. S. Milne, *The Riemann hypothesis over finite fields: from Weil to the present
  day*, in: *The Legacy of Bernhard Riemann After One Hundred and Fifty Years*, Vol. II (L. Ji,
  F. Oort and S.-T. Yau, eds.), Adv. Lect. Math. (ALM) **35**, part 2, International Press,
  Somerville, MA, and Higher Education Press, Beijing, 2016, 487–565; reprinted in ICCM Notices
  **4** (2016), no. 2, 14–52; doi:10.4310/ICCM.2016.v4.n2.a4; arXiv:1509.00797. Page pins above
  are to §1 of the arXiv version.
- **[Mil22]** J. S. Milne, *Grothendieck's standard conjecture of Lefschetz type over finite
  fields*, preprint, arXiv:2011.06563 (2020); revised version v1.1, 14 July 2022, at
  https://www.jmilne.org/math/articles/LFF.pdf. (arXiv carries v1 only; "v1.1" is the author's own
  revision, not an arXiv version.)
- **[Mor96]** A. Moriwaki, *Hodge index theorem for arithmetic cycles of codimension one*,
  Math. Res. Lett. **3** (1996), no. 2, 173–183; doi:10.4310/MRL.1996.v3.n2.a4;
  arXiv:alg-geom/9403011.
- **[MT58]** A. Mattuck and J. Tate, *On the inequality of Castelnuovo–Severi*, Abh. Math. Sem.
  Univ. Hamburg **22** (1958), 295–299.
- **[Seg37]** B. Segre, *Intorno ad un teorema di Hodge sulla teoria della base per le curve di una
  superficie algebrica*, Ann. Mat. Pura Appl. (4) **16** (1937), 157–163; doi:10.1007/BF02414291.
  *(Not read; fields from Crossref and zbMATH. Note that Grothendieck's own 1958 bibliography
  prints the start page as 167; 157 is correct.)*
- **[Sev06]** F. Severi, *Sulla totalità delle curve algebriche tracciate sopra una superficie
  algebrica*, Math. Ann. **62** (1906), 194–225; doi:10.1007/BF01449978. *(Not read; fields from
  Crossref and the JFM review, JFM 37.0647.02.)*
- **[Ste72]** E. Bombieri, *Counting points on curves over finite fields (d'après S. A. Stepanov)*,
  Sém. Bourbaki Exp. 430 (1972/73), Springer Lecture Notes in Math. **383** (1974), 234–241 — the
  elementary auxiliary-polynomial route named in the footnote to the Status paragraph above.
- **[VV88]** I. Vainsencher and J. F. Voloch, *On the Castelnuovo–Severi inequality*, J. reine
  angew. Math. **390** (1988), 114–116; doi:10.1515/crll.1988.390.114; Zbl 0646.14003. *(Not read;
  De Gruyter paywall, EuDML 403, GDZ a JavaScript shell. The zbMATH review reports a sharpened
  inequality improving Kani rather than a re-proof of the bare Castelnuovo–Severi bound, and that
  is how it is described here.)*
- **[YZ17]** X. Yuan and S.-W. Zhang, *The arithmetic Hodge index theorem for adelic line
  bundles*, Math. Ann. **367** (2017), no. 3–4, 1123–1171; doi:10.1007/s00208-016-1414-1;
  arXiv:1304.3538 (there titled "… for adelic line bundles I: number fields"). The published
  title carries **no** roman numeral.
- **[YZ-II]** X. Yuan and S.-W. Zhang, *The arithmetic Hodge index theorem for adelic line bundles
  II: finitely generated fields*, preprint, arXiv:1304.3539 (2013; v2, 2021). Unpublished as of
  August 2026 — a separate paper, not part of [YZ17].
- **[HP14]** E. Hallouin and M. Perret, *From Hodge Index Theorem to the number of points of curves
  over finite fields*, arXiv:1409.2357 (2014). Unpublished preprint as of August 2026.


---

## Referee pass + repairs (2026-08-26)

**Referee verdict** (`results/c3-r/referee-m1.md`, independent, same date): PASS WITH REPAIRS —
no fatal, 3 major, 6 minor. Every proof re-derived line by line; the input ledger verified
input-by-input with NO hidden zeta/L-function/RH content found anywhere; 13/13 numerical checks
pass (`results/c3-r/referee_m1_checks.py`); classical bibliography pinned online at page level.
All repairs below applied 2026-08-26.

- **MAJOR 1 (Nakai–Moishezon missing from the input list) — FIXED.** (IN7) Nakai–Moishezon
  criterion, hard direction [Hartshorne Thm. V.1.10; cohomological proof, no zeta content]
  added to §2, with the elementary Segre-embedding alternative noted; §6's invocation now tagged
  (IN7); the §8 ledger row for §6 updated to match. The listed-input route was chosen over
  rewriting §6 because the printed verification sketch uses the criterion, and the ledger
  already named it — §2, §6, and §8 now agree, and "exactly" in §2 is true.
- **MAJOR 2 ("No step below mentions them" falsified by §7/§10) — FIXED.** Scope sentence
  rewritten: no step of the PROOF (§§3–6) mentions the excluded items; §7 consumes rationality
  + FE of Z(C, T) (RR-on-the-curve facts, no RH content) and produces point counts as outputs;
  §10 mentions the explicit formula only inside the IV.10 fence.
- **MAJOR 3 (historical overclaim) — FIXED.** The "only POSITIVITY mechanism" qualifier
  restored in the status paragraph (the phrase's single occurrence in this note; a grep for
  variants found no second one), with the Stepanov–Bombieri footnote added: Stepanov (1969) /
  Bombieri, Sém. Bourbaki Exp. 430 (1972/73), LNM 383 (1974), 234–241 — an elementary RH-for-
  curves proof from RR on the curve, no surface, no Hodge index; Deligne's amplification noted
  as likewise distinct. Bombieri's exposé/volume/pages re-verified online this pass (numdam
  record SB_1972-1973__15__234_0; Springer LNM 383, 1974).
- Minor 1 (quote misattribution) — fixed in the status block, §9, AND the §11 row: "Verified
  in the brief's favor" now attributed to the direction file's Phase-4 verdicts; the
  adjudication cited for its own wording "the M1 gate is verified sound by both killers".
- Minor 2 (killer-1 tier-1 overstatement) — fixed: "both killers re-derived the argument; the
  lineage was tier-1-verified (killer-2 and the adjudicator)".
- Minor 3 (spurious "(IN1)" in §4 Case 2) — fixed: H² > 0 now credited to (IN3) alone.
- Minor 4 ((IN6) finite-generation provenance) — fixed: Néron–Severi theorem named inside
  (IN6), with the scope note that it is consumed only for ρ < ∞ in §5, off the load-bearing
  chain.
- Minor 5 (silent lemma in §7's closing equivalence) — fixed: the generating-function
  no-pole-cancellation clause added (residue −m_α at T = 1/α; radius ≥ q^{−1/2}; FE pairing
  pins equality).
- Minor 6 (numbering-coincidence guard + letter-checks) — fixed: §9 now states that
  Hartshorne's theorem and exercise numbering are distinct series. The two letter-level pins
  ("Cor. V.1.8", the "(b)" of Ex. II.7.14) remain recalled-only: an online letter-check was
  attempted 2026-08-26 (three targeted searches; no conclusive page image) and both are flagged
  in §9 as re-proved-in-full/non-load-bearing, pending a 30-second physical-copy check.

**Rejected/deferred:** none rejected. One residue deferred, exactly as the referee left it: the
two Hartshorne sub-item letter-checks above await a physical copy (non-load-bearing; both
statements proved in full in this note).

*(Repairs editor, Session 6+, 2026-08-26. With the three majors landed, this note is
external-circulation ready per the referee's §8 assessment; program-internal S4-gate use was
already sound.)*
