# Referee report: `results/c3-r/m1-noncircularity.md` (C3-r M1, the non-circularity note)

**Referee pass owed per the binding reduced recommission** (`directions/C3-geometric-substrate.md`,
Current frontier: "both notes then face a referee pass before any external circulation").
Independent referee — wrote none of the inputs. Date: 2026-08-26 (Session 6).

**VERDICT: PASS WITH REPAIRS — no fatal. The mathematics is correct and complete; the
non-circularity claim (S4) survives full re-derivation with NO hidden zeta/L-function/RH input
found anywhere. Three majors (all one-sentence fixes: an input-list completeness gap around
Nakai–Moishezon, one scope sentence falsified by the note's own §7, one historical overclaim)
and six minors block external circulation until repaired; nothing blocks program-internal use
as the S4 gate citation.**

---

## 1. Protocol

Per standing orders 5 (no load-bearing claim on recall) and 1 (prior-art/bibliography online):

- **Every proof in §§3–7 re-derived line by line from scratch** (this report, §2). The
  recommission-record repair (auxiliary-ample H′ = D + mH) audited against the loose sketch it
  claims to fix (§3 below).
- **Every input's "zeta/RH content: none" column verified input-by-input** (§4 below) — the
  note's entire point; a hidden RH input would have been fatal.
- **Numerical spot checks executed** (§5 below): 13 independent checks, all passing (script
  stored at `results/c3-r/referee_m1_checks.py`, rerunnable: `python3 referee_m1_checks.py`,
  13/13 PASS), including full independent recomputation of the F₇/F₄₉/F₃₄₃ counts 5/55/380
  the note cites from the adjudication.
- **Bibliography verified online this session** (§6 below): Mattuck–Tate 1958 and Grothendieck
  1958 pinned to page level via Springer/mathnet.ru and EuDML; the Hartshorne exercise pair
  V.1.9–1.10 pinned via an independent published citation; direct github.com/arxiv.org were
  unreachable (known IPv6 issue) — the GCS arXiv mirror and WebSearch were used instead, as
  the recommission instructed. Nothing was silently skipped; the two pins that remain
  substance-verified-only are flagged explicitly in §6.
- Context read in full: `directions/C3-geometric-substrate.md`, `results/adjudication-C3.json`,
  the relevant kill:C3/kill2:C3 findings and literature flags in `results/verdicts-c3d1.json`,
  `results/corpus-routing.md` header caveats, `results/c3-r/m0-axiom-note.md` §3.5,
  `BARRIER-ZOO.md` IV.10.

## 2. Line-by-line re-derivation (Duty 1)

**Conventions.** Sound. Intersection numbers and h^i are stable under base field extension
(flat base change), so the descent sentence is correct; "numerically nontrivial" = nonzero in
Num(X) is used consistently throughout.

**§2 inputs (IN1)–(IN6).** Each is a correct statement of a standard theorem: (IN1) is
Hartshorne Thm. V.1.6 exactly (χ(D) = χ(O_X) + ½D·(D−K)); (IN2) h²(D) = h⁰(K−D) is Serre
duality specialized to a smooth surface; (IN3) is correct with the correct easy proof (degree
in a projective embedding; for E = Σnᵢcᵢ effective nonzero and H ample, E·H = Σnᵢ(Cᵢ·H) > 0
via a very ample multiple); (IN4) is Ex. II.7.14(b) as recalled; (IN5) trivial; (IN6)
nondegeneracy is definitional. **One completeness gap: see MAJOR 1** — §6 consumes the HARD
direction of Nakai–Moishezon, which is not among IN1–IN6.

**§3 Lemma (= Hartshorne Cor. V.1.8 in substance).** Re-derived, correct and complete:
χ(nD) = (n²/2)D² − (n/2)D·K + χ(O_X) → ∞ (needs D² > 0 only); (K−nD)·H = K·H − n(D·H) → −∞
(needs D·H > 0 — the exact locus the note flags); h⁰(K−nD) > 0 would force
(K−nD)·H ≥ 0 by (IN3) (with the E = 0 case correctly split off) — contradiction; then
h⁰(nD) ≥ χ(nD) − h²(nD) = χ(nD) → ∞ by (IN5) with h² = h⁰(K−nD) = 0. No gaps. No zeta
contact.

**§3 parenthetical — the claimed repair of the compressed sketch. VERIFIED, and the
diagnosis is right.** The verdict-file sketch (kill2:C3 fatal-adjacent minor: "χ(nD) → ∞
forces ±nD effective for large n, and effective nonzero meets ample H positively —
contradiction") is genuinely loose as literally stated: under the Theorem's hypothesis
D·H = 0, RR gives only h⁰(nD) + h⁰(K−nD) → ∞, and the K−nD branch has
(K−nD)·H = K·H **constant in n**, so no contradiction arises from it, and nothing forces
"±nD" effective. The note's repair — apply the Lemma to D with the auxiliary ample
H′ = D + mH (so D·H′ = D² > 0 kills the h² term against H′), then contradict against the
ORIGINAL H via (IN3) — is exactly Hartshorne's actual V.1.9 route and is correct and
complete as written.

**§4 Theorem (Hodge index).** Correct. Case 1: H′ = D + mH ample by (IN4);
D·H′ = D² + m(D·H) = D² > 0 ✓ (uses D·H = 0); Lemma applies (both hypotheses verified);
nD ~ E effective, E ≠ 0 since nD ≢ 0 (numerical nontriviality); (IN3) gives nD·H = E·H > 0
contradicting n(D·H) = 0. Case 2 (the D² = 0 perturbation): all four identities re-derived
and machine-checked on 200 random rank-4 lattices (§5, check 13): E′·H = 0;
D·E′ = (H²)(D·E) ≠ 0 (uses D·H = 0 and H² > 0); D′ = nD + E′ has D′·H = 0 and
D′² = 2n(D·E′) + E′² > 0 for n large of the right sign; D′² > 0 forces D′ numerically
nontrivial (D′·D′ ≠ 0), so Case 1 applies to D′. Airtight. H² > 0 is correctly grounded
(very ample multiple is effective nonzero + (IN3)) — though the "(IN1)" in that parenthetical
is spurious (minor 3).

**§5 Corollary (signature (1, ρ−1)).** Correct, including the two subtle steps done right:
(i) rational ⟶ real passes through negative SEMIdefiniteness by density/continuity (definite
does not transfer by density — the note correctly does not claim it does); (ii) a real
isotropic vector of a semidefinite form lies in the radical (Cauchy–Schwarz for the
semidefinite form — correct), the radical of a Q-defined form on a Q-defined subspace is a
rational subspace, and a nonzero rational radical vector would be numerically trivial via
w = λH + w^⊥ (valid since H² ≠ 0), contradicting nondegeneracy (IN6). Machine spot checks:
Gram [[0,1],[1,0]] on ⟨ξ₁,ξ₂⟩ has signature (1,1); the E×E (End = Z) Gram
[[0,1,1],[1,0,1],[1,1,0]] on ⟨ξ₁,ξ₂,Δ⟩ has eigenvalues {2,−1,−1}, signature (1,2) = (1,ρ−1) ✓.
Note ρ < ∞ (Néron–Severi theorem) is consumed here and only here — see minor 4; §§6–7 never
use §5, so the load-bearing chain to the Weil bound is independent of finite generation.

**§6 Corollary (Castelnuovo–Severi with equality clause).** Correct. ξ₁² = ξ₂² = 0,
ξ₁·ξ₂ = 1 ✓; the ampleness of H = ξ₁ + ξ₂ is TRUE and the NM verification sketch is right
(every irreducible curve meets ξ₁ or ξ₂ positively and neither negatively — including the
fiber cases), **but this consumes the hard direction of Nakai–Moishezon — MAJOR 1**. The
bidegree normalization is self-consistent (d₁ = D·ξ₁, d₂ = D·ξ₂; graph of f gets (1, deg f) —
re-derived, correct, and matching the convention in independent sources). The computation
D′ = D − d₁ξ₂ − d₂ξ₁ ⟹ D′·H = 0 ⟹ 0 ≥ D′² = D² − 4d₁d₂ + 2d₁d₂ re-derived term by term:
exact. The equality clause is the correct contrapositive of the Theorem (D′² = 0 with
D′·H = 0 forces D′ ≡ 0), and the converse direction is trivially consistent
((d₂ξ₁ + d₁ξ₂)² = 2d₁d₂).

**§7 F_q degeneration.** All three geometric inputs re-derived: (W1) Γ·ξ₁ = 1, Γ·ξ₂ = deg F
= q ✓; (W2) Δ² = deg T_C = 2−2g and Γ² = q(2−2g) via γ*T_S ≅ T_C ⊕ F*T_C, deg F*T_C =
q·deg T_C ✓ (the chain in the note is exactly right; T_Γ ≅ T_C under the graph isomorphism);
(W3) transversality from dF = 0 (T_Γ ∩ T_Δ = {(v,0)} ∩ {(v,v)} = 0, complementary dimensions
⟹ multiplicity 1), fixed points of the relative Frobenius = C(F_q) ✓. The discriminant step:
the identity 2(r+s)(r+sq) − D² = 2[g·r² − rs(t−1−q) + gq·s²] verified SYMBOLICALLY (exact
polynomial arithmetic in r,s,g,q,t — §5 check 5); integers → reals by homogeneity + density ✓;
psd binary form with nonnegative outer coefficients ⟺ discriminant ≤ 0 ⟹
(t−(q+1))² ≤ 4g²q ✓; the g = 0 edge case degenerates correctly (forces N₁ = q+1, true for
conics over F_q by Chevalley–Warning). Replacing F by F^k: all three W-inputs re-scale
correctly (deg F^k = q^k, dF^k = 0). The closing equivalence with |αᵢ| = √q is TRUE
(generating-function/no-pole-cancellation argument + the FE pairing αᵢ ↦ q/αᵢ; both
rationality and FE are F.K. Schmidt-style RR-on-the-curve facts with no RH input) — the note
cites it as "standard bookkeeping" rather than proving it; acceptable, see minor 5.
**Consistency note with M0 §3.5: verified verbatim consistent** with
`results/c3-r/m0-axiom-note.md` §3.5 and adjudication computation b; the F₇ numbers
independently recomputed (§5).

**§8 ledger + claim statement.** The claim as scoped in the boxed statement is TRUE for
§§3–6 exactly as written. The scope-of-claim paragraph is honest and correctly does NOT
confer substrate credit. One wording defect in §2's supporting sentence — MAJOR 2.

**§9 lineage.** All three items verified this session (see §6 below). The quoted killer-2
literature flag exists verbatim in `results/verdicts-c3d1.json` (elision fair). One
attribution imprecision — minor 1.

**§10 E_p × E_p remark.** Verified against `BARRIER-ZOO.md` IV.10 and adjudication
computation a, point for point: the lattice E_p = C/(Z ⊕ Z·i·log p/2π), End(E_p) = Z barring
(log p)² ∈ 4π²Q, NS = Zξ₁ ⊕ Zξ₂ ⊕ ZΔ (correct basis change from the Birkenhake–Lange
Hom-summand form), Lefschetz data deg([m]−1) = (m−1)² (re-derived: deg of x ↦ (m−1)x on an
elliptic curve), off-diagonal NS rank 2, prime-blindness scoping. The remark stays inside
IV.10's fence and revives nothing. Correct.

**§11 traceability.** All six rows spot-checked against the named files; all resolve.

## 3. The repair audit (the recommission's compressed sketch)

The direction file's work log records the writer's claim: "the recommission record's
compressed M1 sketch is loose as literally stated (with D·H = 0, (K−nD)·H is constant — the
correct argument runs through an auxiliary ample H′ = D + mH …); the D² = 0 case needs a
perturbation argument." **Both halves verified as stated** (§2 above, items §3/§4): the
looseness is real, the diagnosis "(K−nD)·H is constant" is exactly right, the repair is the
textbook-correct route, and the perturbation case is complete. The note also correctly
demotes the sketch's provenance: killer-1's outline (kill:C3 finding, item (4)) had the
Lemma's hypotheses right (D·H > 0) and only compressed the reduction; killer-2's is the one
with the "±nD" slip. The note's blanket phrase "the compressed sketch recorded in the verdict
files" covers both without blaming either — fine.

## 4. Input ledger verification (Duty 2 — the note's entire point)

Verified input-by-input that nothing consumed has zeta/L-function/RH content:

| Input | RH-free? | Basis of verification |
|---|---|---|
| (IN1) RR on surfaces | YES | proved via intersection theory + cohomology (Zariski/Serre any characteristic); no zeta anywhere in any standard proof |
| (IN2) Serre duality | YES | sheaf cohomology; no zeta |
| (IN3) ample·effective > 0 | YES | projective degree; no zeta |
| (IN4) D + nH ample | YES | Serre-type cohomological argument; no zeta |
| (IN5) h^i ≥ 0 | YES | trivial |
| (IN6) Num pairing | YES | definitional + (for §5's ρ < ∞ only) Néron–Severi theorem — proved via Picard-variety/finiteness arguments, no zeta |
| Nakai–Moishezon, hard direction (§6, UNLISTED — MAJOR 1) | YES | Hartshorne Thm. V.1.10's proof is cohomological (RR + effectivity bootstrapping); no zeta |
| §7 (W1)–(W3) | YES | pure intersection theory/normal bundles/tangent computations |
| §7 closing: rationality + FE of Z(C,T) | YES (no RH) | F.K. Schmidt route from RR on the curve; RH is the OUTPUT — ledger row already states this honestly |

**No hidden RH input found. The S4 non-circularity claim is verified in full.** The one
defect is bookkeeping (MAJOR 1: an RH-free input missing from the "exactly" list), not
circularity.

## 5. Numerical spot checks (Duty 3)

Script: `results/c3-r/referee_m1_checks.py` (self-contained python3, integer/exact
arithmetic except final √ bounds; rerun output 13/13 PASS). Results:

1. **F₇ elliptic curve y² = x³+x+1: N₁,N₂,N₃ = 5, 55, 380** — independently recomputed by
   brute force over GF(7), GF(49) = F₇[x]/(x²+1), GF(343) = F₇[x]/(x³+2). Matches the note's
   §7 consistency note and adjudication computation b exactly. PASS
2. Trace recursion from a = 3 reproduces N₂, N₃. PASS
3. Weil bound |N_k − (q^k+1)| ≤ 2g·q^{k/2} at k = 1,2,3 (margins −2.29, −9.0, −1.04). PASS
4. Curve smooth over F₇ (disc ≢ 0). PASS
5. **Symbolic identity** 2(r+s)(r+sq) − D² = 2[g·r² − rs(t−1−q) + gq·s²] as exact
   polynomials in (r,s,g,q,t). PASS — §7's expansion is exact, not just numerically checked.
6. F₇ instance form r² + 3rs + 7s² positive definite on the ±20 grid (disc −19 < 0). PASS
7. CS instance D² ≤ 2d₁d₂ for D = rΔ + sΓ on the ±20 grid (F₇ curve, g = 1). PASS
8. Genus-2 Weil bound, y² = x⁵+x+3 over F₇ (squarefree verified incl. over F₄₉): N₁ = 11,
   |N₁−8| = 3 ≤ 4√7 ≈ 10.58. PASS. (Referee's first test curve x⁵+x+1 is genuinely singular
   mod 7 — x = 4 is a shared root of its factors x²+x+1 and x³−x²+1 — caught by the
   harness's smoothness guard and replaced; no reflection on the note, which never uses it.)
9. Genus-2 y² = x⁵+x+3 over F₁₁: N₁ = 13, |N₁−12| = 1 ≤ 4√11. PASS (the first run also
   checked y² = x⁵+x+1 over F₁₁/F₁₃, squarefree there: N₁ = 8 and 15, bounds hold)
10. Genus-2 y² = x⁵+x+3 over F₁₃: N₁ = 10, |N₁−14| = 4 ≤ 4√13. PASS
11. Signature check ⟨ξ₁,ξ₂⟩: (1,1). PASS
12. Signature check E×E ⟨ξ₁,ξ₂,Δ⟩: eigenvalues {2,−1,−1} = (1,2) = (1,ρ−1). PASS
13. §4 Case-2 identities (E′·H = 0; D·E′ = (H²)(D·E) − (E·H)(D·H)) on 200 random rank-4
    integer lattices. PASS

## 6. Bibliographic verification (online, standing order 1)

Direct github.com/arxiv.org unreachable this session (known IPv6 issue); WebSearch, WebFetch
on reachable hosts, and the GCS arXiv mirror used instead.

- **Mattuck–Tate, "On the inequality of Castelnuovo-Severi", Abh. Math. Sem. Univ. Hamburg 22
  (1958), 295–299** — CONFIRMED (Springer article page BF02941959; mathnet.ru record; Milne's
  "Work of John Tate" corroborates the RR-on-the-surface content claim). Note's §9 content
  claim ("first modern non-circular derivation" of CS from RR) consistent with these sources.
- **Grothendieck, "Sur une note de Mattuck-Tate", J. reine angew. Math. 200 (1958), 208–215**
  — CONFIRMED (EuDML doc 150382; content "index theorem on an arbitrary surface" confirmed —
  matches the note's §9 description).
- **Hartshorne Ex. V.1.9–V.1.10 as the CS + Weil-bound exercise pair** — CONFIRMED via an
  independent published citation: arXiv:1409.2357 ("From Hodge Index Theorem to the number of
  points of curves over finite fields", fetched via the GCS mirror, text-extracted locally)
  cites the classical route as "[Har77, exercice 1.9, 1.10 p. 368]". Thm. V.1.6 = RR for
  surfaces and Thm. V.1.9 = Hodge index CONFIRMED via independent lecture-note citations
  (UMD 808J notes; Voisin CMSA notes). "[III, 7.6]" as the Serre-duality citation CONFIRMED
  (Stanford/Vakil seminar note; UMN course outline).
- **Two pins verified in substance but not letter-checked against the book this session**
  (book not on disk; flagged per standing order 5, both non-load-bearing since the note
  re-proves the statements in full): (i) "Cor. V.1.8" as the number of the effectivity
  criterion — the statement is standard and the note proves it; (ii) Ex. II.7.14 sub-item
  "(b)" — the II.7.14 = ample-tensor-powers exercise is confirmed by search, the sub-item
  letter is recalled. Neither affects correctness; both worth a 30-second check against any
  physical copy before external circulation.
- **Referee's own counter-pin for MAJOR 3**: Stepanov 1969 + Bombieri, Sém. Bourbaki
  Exp. 430 (1972/73), LNM 383, 234–241 ("Counting points on curves over finite fields
  (d'après S. A. Stepanov)") — an ELEMENTARY proof of RH for curves from RR on the curve,
  with no surface, no Hodge index — CONFIRMED online (Tao's 2014 exposition; numdam record;
  Milne pRH survey).

## 7. Findings

### FATAL — none.

The proof is correct and complete at every step; no hidden zeta/L-function/RH input exists in
any consumed statement; the F_q degeneration computation is exact; the adjudicated fence
around the Tate-curve material (§10) is respected.

### MAJOR (external circulation blocked until fixed; each is a one-sentence repair)

- **MAJOR 1 — the hard direction of Nakai–Moishezon is consumed but missing from the input
  list.** §2 claims "The proof uses exactly the following" (IN1)–(IN6), and (IN3) is
  explicitly only "the easy direction of Nakai–Moishezon"; but §6 certifies H = ξ₁ + ξ₂ ample
  BY the numerical criterion ("H := ξ₁ + ξ₂ is ample (Nakai–Moishezon: H² = 2 > 0, and every
  irreducible curve …)") — the hard direction, an additional theorem. The §8 ledger row even
  names it ("Nakai–Moishezon for H"), so the ledger and §2 currently contradict each other.
  NM is RH-free (its proof is cohomological), so non-circularity is untouched — but in a
  document whose sole deliverable is exact input accounting, "exactly" must be true. **Fix
  (either):** add "(IN7) Nakai–Moishezon criterion [Hartshorne Thm. V.1.10; no zeta content]"
  to §2; or avoid NM entirely — m(ξ₁+ξ₂) = p₁*(mP) + p₂*(mP′) is very ample for m ≫ 0 as the
  Segre-composed embedding of very ample divisors on the factors, an (IN4)-grade elementary
  fact.
- **MAJOR 2 — "No step below mentions them" is falsified by the note's own §7 and §10.** §2's
  "Not inputs" paragraph ends: "No step below mentions them." But §7 mentions and consumes
  the rationality + FE of the zeta function of C (as flagged honestly in the ledger) and
  mentions point counts throughout (N₁ = Γ·Δ is a point count — as an output), and §10
  mentions the explicit formula. The intended scope is §§3–6, where the sentence is TRUE.
  **Fix:** "No step of the proof (§§3–6) mentions them; §7 consumes rationality and the
  functional equation of Z(C,T) — RR-on-the-curve facts with no RH content — exactly as
  itemized in the ledger."
- **MAJOR 3 — "the only mechanism in history that has proved an RH" is a historical
  overclaim.** §1's status paragraph drops the direction file's qualifier ("The only
  POSITIVITY mechanism that has ever proved an RH"). As printed the claim is false:
  Stepanov (1969)/Bombieri (Sém. Bourbaki 430, 1973) proved RH for curves over finite fields
  by elementary auxiliary-polynomial methods consuming only RR on the CURVE — no square, no
  Hodge index; and Deligne's Weil I amplification is likewise a distinct engine. An external
  referee will seize on this sentence first. **Fix:** restore the qualifier ("the positivity
  engine of the only geometric positivity mechanism that has proved an RH") or add the
  Stepanov–Bombieri footnote. (The same phrase recurs in §1's first paragraph region — fix
  both occurrences.)

### MINOR (six)

1. **§9/status quote attribution.** The quoted sentence "M1's [RU] non-circularity fact TRUE
   (Hodge index from RR + ampleness re-derived; Mattuck–Tate … confirmed)" lives in the
   direction file's Phase-4 verdicts section (`directions/C3-geometric-substrate.md`,
   "Verified in the brief's favor" paragraph), not in `results/adjudication-C3.json`, whose
   own wording is "the M1 gate is verified sound by both killers" / "M1 non-circularity gate
   unchanged (verified sound…)". Repoint the citation for the quoted string.
2. **"Both Session-6 killers … verified the lineage at tier 1"** slightly overstates
   killer-1's role: killer-1 re-derived the argument and confirmed "Hartshorne V.1.9-1.10
   lineage … a genuine standard theorem" but the tier-1 RECORDS check (Crelle/EuDML) was
   killer-2's (and the adjudicator's). Suggested: "both killers re-derived the argument;
   the lineage was tier-1-verified (killer-2, adjudicator)".
3. **§4 Case 2 parenthetical "(IN3)/(IN1) standard" for H² > 0**: (IN1) plays no role in the
   argument actually given (effective multiple + (IN3)); delete "(IN1)".
4. **(IN6) provenance for finite generation.** "Hartshorne V.1" carries nondegeneracy by
   definition, but finite generation of Num is the Néron–Severi theorem (a
   remark-with-references there, not a proved result of V.1). It is consumed only for ρ < ∞
   in §5 — off the load-bearing chain to §§6–7. Either pin it (Néron–Severi/SGA 6) or add
   "(finite generation is used only for the signature statement §5)".
5. **§7 closing equivalence**: "equivalent to |αᵢ| = √q" is true but the ⟹ direction
   silently uses the generating-function/no-pole-cancellation lemma (the log-derivative
   generating function has residue −m_α at T = 1/α, so poles at distinct points of equal
   modulus cannot cancel; radius-of-convergence ≥ q^{−1/2} then bounds max|αᵢ| ≤ √q before
   the FE pairing pins equality). One clause naming this would make the sketch
   self-contained.
6. **Numbering-coincidence guard.** "Thm. V.1.9" (Hodge index) and "Exercises V.1.9–V.1.10"
   (CS + Weil bound) coexist in §9; a half-sentence noting that Hartshorne's theorem and
   exercise numbering are distinct series would pre-empt a confused external reader — and
   while there, letter-check "Cor. V.1.8" and "Ex. II.7.14(b)" against a physical copy
   (§6 above, last bullet).

## 8. External-circulation readiness

**Not yet — repair the three majors first (estimated: under fifteen minutes of edits; no
mathematical content changes).** After those edits the note is, in this referee's judgment,
externally circulable: the mathematics is textbook-correct and completely re-derived here; the
input accounting (post-fix) is exact; the honesty apparatus (status paragraph, scope-of-claim
paragraph, IV.10 fence) is exemplary; the classical bibliography is now pinned online at page
level. Program-internal use as the S4 gate citation is sound as-is: none of the findings
touches the substance of the non-circularity claim.

*(Referee pass, C3-r M1. Independent re-derivation + 13-check numeric audit + online
bibliography. U.S. English. 2026-08-26, Session 6.)*
