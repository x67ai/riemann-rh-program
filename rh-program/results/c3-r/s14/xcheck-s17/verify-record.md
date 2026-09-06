# SECOND-MODEL VERIFICATION — item: citation / dependency audit + public record
Verifier: independent second referee (hostile). Started 2026-09-06 14:00 IST (machine clock stamped below).
Target of verification: `refute-record.md` (first referee), plus the original task spec items (1)-(5).

Method note. All page attributions in this report were recomputed from scratch. The published
`.txt` is a `pdftotext -layout` dump in which each page carries a RUNNING HEAD line
("… Page k of 68  47" or "47   Page k of 68  …") as its FIRST line. Page k therefore spans from
the line carrying "Page k of 68" up to (not including) the line carrying "Page k+1 of 68";
page 1 = lines 1..51 (no head). I built `pg.sh` implementing exactly this and sanity-checked it
(L839 -> p15, L840 -> p16, L893 -> p16, L894 -> p17). Every "p." below is this computation, not a
copy of the first referee's.

Sun Sep  6 14:01:43 IST 2026

---

## ITEM 1 — every statement number, page and gist the NOTE cites, checked verbatim

I first built an independent inventory of every numbered statement in the published `.txt`
(`grep -nE '^ *(Proposition|Corollary|Remark|Claim|Theorem|Lemma|Definition|Example) +[0-9]+\.[0-9]+'`),
mapped each hit to a page with `pg.sh`, and then compared against the note's citations
(inventoried by `grep -oE '(Prop|Cor|Remark|Claim|Thm)s?\.~?[0-9]+\.[0-9]+'` and
`grep -oE 'pp?\.~[0-9]+'` on `alkl23-note.tex`). Beyond the `.txt` I rendered pp. 17, 38, 48,
49, 56, 58 of the published PDF at 400 dpi and read the glyphs, because `pdftotext` silently
drops primes, hats and bold — three of the note's quotations turn on exactly those glyphs.

**Independent page map of every statement the note names** (line -> page, computed here):

| cited | line | page computed | note's page | verdict |
|---|---|---|---|---|
| Prop. 3.2 | 884 | 16 | 16 | OK |
| Cor. 3.4 | 934 | 17 | 17 | OK |
| Cor. 3.5 | 947 | 17 | (none) | OK |
| Cor. 3.6 | 963 | 18 | 18 | OK |
| Remark 3.8 | 980 | 18 | 18 | OK |
| bundle-extension sentence | 993-994 | 18 | 18 | OK |
| Cor. 4.5 | 1217 | 23 | 23 | OK |
| Cor. 4.7 | 1238 | 23 | (none) | OK |
| Sect. 4.3.3 acyclicity exception | 1266-1267 | 23 | 23 | OK |
| Prop. 6.10 | 2016 | 37 | (none) | OK |
| Prop. 6.12 | 2097 | 39 | 39 | OK |
| Cor. 6.14 | 2101 | 39 | 39 | OK |
| Cor. 6.15 | 2104 | 39 | (none) | OK |
| Cor. 6.16 | 2106 | 39 | (none) | OK |
| Remark 6.17 | 2108 | 39 | (none) | OK |
| Cor. 6.21 | 2164 | 40 | 40 | OK |
| Cor. 6.22 | 2169 | 40 | (none) | OK |
| Cor. 6.27 | 2224 | 41 | 41 | OK |
| Cor. 6.28 | 2227 | 41 | (none) | OK |
| Prop. 6.29 | 2253 | 42 | (none) | OK |
| Cor. 6.39 | 2605 | 47 | (none) | OK |
| Remark 6.41 | 2608 | 47 | (none) | OK |
| Claim 6.46 | 2691 (proof ends 2707) | 48-49 | 48-49 | OK |
| Cor. 7.13 | 3173 | 56 | 56 | OK |
| Cor. 7.14 | 3177 | 56 | (none) | OK |
| Cor. 7.15 | 3183 | 57 | (none) | OK |
| Cor. 7.17 | 3197 | 57 | (none) | OK |
| "analog of Remark 6.17/6.41" sentences | 3185, 3201 | 57, 57 | 57 | OK |
| Cor. 7.22 | 3270 | 58 | 58 | OK |
| Cor. 7.23 | 3273 | 58 | (none) | OK |
| Prop. 7.26 | 3330 | 59 | (none) | OK |
| Cor. 7.31 | 3388 | 60 | (none) | OK |
| Prop. 8.8 | 3579 | 64 | 64 | OK |
| Wengenroth Thm 6.1 quote | ~199 | 4 | 4 | OK |
| Wengenroth Cor. 6.5 quote | ~217 | 5 | 5 | OK |
| compact-spectrum remark | ~233 | 5 | 5 | OK |
| adapted-chart definition | 1025-1032 | 19 | 19 | OK |
| (3.1) | 830 | 15 | (none) | OK |
| (3.4)/(3.5) | 870 / 878 | 16 / 16 | (none) | OK |
| (4.8) | 1142 | 21 | (none) | OK |
| (4.9) | 1177 | 22 | (none) | OK |
| (4.10) | 1186 | 22 | (none) | OK |
| (6.33) | 1971 | 36 | (none) | OK |
| (6.41) + projective-topology sentence | 2078 / 2049 | 38 / 38 | 38 | OK |
| (6.42)/(6.43) | 2086 / 2091 | 39 / 39 | (none) | OK |
| (6.47) | 2154 | 40 | (none, "pp. 41, 58" is for the K-cases) | OK |
| (6.49) | 2231 | 41 | (none) | OK |
| (7.26) | 3139 | 56 | (none) | OK |
| (7.27) + bold-x sentence | 3151 / 3146 | 56 / 56 | 56 | OK |
| K-closed-subspace sentence | 3244-3245 | 58 | 58 | OK |
| K(M) closed in Ȧ | 2180 | 41 | 41 | OK |

**(4.12) is never cited by the note** (`grep -c '4\.12' alkl23-note.tex` = 0), so the task-spec
entry for it is vacuous. I record its location anyway: (4.12) is at L1202, p. 22.

**The three glyph-critical quotations, checked on the rendered PDF, not on `pdftotext`:**

1. p. 17, l. 2 of the body (rendered): "For any a ∈ **Ŝ′^m**(U × R^l), and K, α and β like in
   (3.5), since **‖φ(a)‖′_{K,α,β,m} = ‖a‖′_{K,α,β,m} < ∞**, there are C, R > 0 so that …"
   The note quotes ``$\|\varphi(a)\|'_{K,\alpha,\beta,m}=\|a\|'_{K,\alpha,\beta,m}<\infty$''
   "at the top of p. 17". EXACT, including both primes, and it really is the second line of the
   page. The completion carries a **hat** (Ŝ′^m), not a bar.
2. p. 17: "Hence **S′^m**(U × R^l) is complete, and therefore it is a Fréchet space." — the
   hat is ABSENT on this occurrence. The note's quotation ``Hence $S'^m(U\times\R^l)$ is
   complete'' (p. 17) is therefore verbatim. (Had the paper written Ŝ′^m here the note's
   quotation would have been wrong; it does not.)
3. pp. 48-49 (rendered): p. 48 ends "… By Corollary 6.14," and p. 49 opens "there is some
   0-neighborhood V ⊂ 𝒜(M) such that V ∩ 𝒜^m(M) = W ∩ 𝒜^m(M)." Both occurrences of 𝒜^m are
   UNPRIMED. The note's quotation is verbatim and its "pp. 48-49" is exactly right — the
   sentence straddles the break.

**Gist checks that are not mere number/page matching:**

- Prop. 3.2 (p. 16) reads "The semi-norms (3.4) and (3.5) together describe the topology of
  S^m(U × R^l)." The note's §3 preamble names (3.1), (3.4), (3.5) and their symbols
  ‖·‖_{K,α,β,m}, ‖·‖_{Q,C^k}, ‖·‖′_{K,α,β,m}: all three match the printed definitions
  (L830, L870, L878) symbol for symbol.
- Cor. 3.4 (rendered p. 17): "For m < m′, the topologies of **S^{m′}**(U × R^l) and C^∞(U × R^l)
  coincide on **S^m**(U × R^l). Therefore the topologies of S^∞(U × R^l) and C^∞(U × R^l)
  coincide on S^m(U × R^l)." Both assertions exactly as the note describes them, primes where
  the note puts them.
- Cor. 3.6's proof (p. 18): "Corollary 3.4 gives the property of being acyclic, and therefore
  complete and boundedly retractive (Sect. 2.1)." and, in the semi-Montel step, "Since
  S^∞(U × R^l) is boundedly retractive, B is contained and bounded in some S^m(U × R^l) …
  By Corollary 3.4, it follows that B is a complete bounded subspace of C^∞(U × R^l)".
  The note's §4 description ("applies Cor. 3.4 to a bounded subset B of some S^m") is exact.
- The bundle sentence (p. 18): "We can similarly define the norms (3.4) and (3.5) on S^m(E),
  and **Propositions 3.2 and 3.3 and Corollaries 3.4 to 3.6 can be directly extended** to this
  setting." The note's §2 splits it correctly into the parts it does and does not attack
  (3.2, 3.4, 3.6-over-non-compact-base attacked; 3.3, 3.5 untouched).
- Remark 3.8 (p. 18) ends "…since S^∞(U × R^l) is **sequentially retractive** (Corollary 3.6),
  all a_m would lie in some step S^{m_0}(U × R^l), a contradiction." The note's §4 ("…without
  the sequential retractivity of S^∞(U × R^l), which is what its printed argument uses") is exact.
- Cor. 4.5's proof (p. 23) is exactly one sentence: "Use Corollary 3.4 and the TVS-embeddings
  (4.10)."
- Sect. 4.3.3 (p. 23): "There are extensions of (4.10)–(4.13) and Corollaries 4.5 and 4.6 …
  Corollary 4.7 has extensions for ⊕_m I^m(M,L) and I_{·/c}(M,L), **except acyclicity in the
  case of I(M,L)**." The note's parenthetical in (f) — "Sect. 4.3.3, p. 23, excepts acyclicity
  for non-compact M; the symbol statements do not" — is exact: the exception is stated only
  for Cor. 4.7, and Cors. 4.5/4.6 and the p.-18 bundle sentence carry no such exception.
- p. 19: "Let L is a regular submanifold of M of **codimension n′ and dimension n″** … Let
  (U, x) be a chart of M adapted to L; i.e., for open subsets U′ ⊂ R^{n′} and U″ ⊂ R^{n″},
  x = (x^1,…,x^n) ≡ (x′,x″) : U → U′ × U″ … L_0 := L ∩ U = {x′ = 0}." The note's (d) uses
  codim L = n′, dim L = n″ and "x : U_1 → U′ × U″ (p. 19)" — the paper's own convention,
  page correct.
- (4.8) (p. 21) is `C_c^∞(U) → C^∞(N*U′), u ↦ a` with a(x″,ξ) = ∫ e^{−i⟨x′,ξ⟩} u(x′,x″) dx′.
  The note's (d) computes the symbol of u_j = j^{n′+m̄′} g(x″) ψ_*(jx′) as
  a_j = j^{m̄′} g(x″) ψ̂_*(ξ/j); substituting x′ = z/j gives j^{n′+m̄′} g j^{−n′} ψ̂_*(ξ/j),
  i.e. exactly that. The citation and the use agree.
- (6.41) (p. 38) is ‖u‖_{k,m} = ‖P_k u‖_{x^m L^∞} = ess sup_M x^{−m}|P_k u| = sup_{M̊} x^{−m}|P_k u|,
  and the sentence the note cites for "projective over all P ∈ Diff_b(M)" is on the same page
  (rendered): "This is another C^∞(M)-module and LCS, with the projective topology given by
  the maps P : 𝒜^m(M) → x^m L^∞(M) (P ∈ Diff_b(M))." Both p. 38. The note's use of the
  seminorm "with P = 1" is licensed by that sentence, not only by the countable spanning set.
- Prop. 6.12 / Cor. 6.14 (p. 39) both state exactly what the note says, and Cor. 6.14 does have
  two assertions (A^{m′} vs C^∞ on A^m; then A(M) vs C^∞ on A^m).
- Cor. 6.21 (p. 40) is preceded by "The following is **a consequence of Corollary 4.5 applied
  to (M̆, ∂M)**", and Cors. 6.27/6.28 (p. 41) by "Now the following analogs of Corollaries 6.21
  and 6.22 hold true with formally the same proofs, **using Corollaries 6.21, 6.22 and 6.26**."
  The note's §2 chain "Cor. 6.27 … pass through Cor. 6.21, hence through Cor. 4.5" is exactly
  what the printed text says.
- (6.47) (p. 40): "Ȧ^m(M) = I^m_M(M̆, ∂M) ⊂ I^m(M̆, ∂M) (m ∈ R), **which are closed subspaces**".
  The note's (d) writes "Ȧ^m(M) = I^m_M(M̆, ∂M) (6.47)" — identical.
- p. 41: "These are closed subspaces of Ȧ^{(s)}(M), Ȧ^m(M) and Ȧ(M), respectively" (for
  𝒦^{(s)}, 𝒦^m, 𝒦). p. 58: "These are closed subspaces of I^{(s)}(M,L), I^m_L(M,L) and I(M,L),
  respectively" (for K^{(s)}, K^m, K). The note's "((6.47), pp. 41, 58)" is right on both pages.
  **Paper typo, immaterial to the note:** the p.-58 middle entry prints I^m_L(M,L), which is
  K^m(M,L) itself; the intended (and true) statement is K^m(M,L) closed in I^m(M,L), which is
  what the note says.
- Prop. 6.29 (p. 42): "For all m ∈ R, there is a continuous linear partial extension map
  E_m : 𝒜^m(M) → 𝒜̇^{(s)}(M) …". (6.38) (rendered p. 38): "𝒜^m(M) ⊂ 𝒜^{m′}(M)  (m′ < m)".
  Together these make the note's parenthetical on Claim 6.46 correct — see below.
- (7.26)/(7.27) (p. 56): (7.26) is π^*: 𝒜(**M**) ≅→ J(M,L); (7.27) is the two-line display whose
  second line is J^m(M,L) = {u ∈ C^{−∞}(M,L) | Diff(M,L) u ⊂ 𝐱^m L^∞(M)}. The note's "given by
  (7.27) with Diff(M,L) and 𝐱^m L^∞(M)" is exact, and the sentence it paraphrases for 𝐱 —
  "Extend |x| to a function 𝐱 on M that is positive and smooth on M\L. Its lift π^*𝐱 is a
  boundary defining function of 𝐌" — is on p. 56.
- Prop. 7.26 (p. 59) gives K(M,L) ≅ ⊕_{m=0}^∞ C^∞(L; Ω^{−1}NL) (a direct SUM, hence finite
  sums) and its proof writes u = ∂_x^m δ_L^v. The note's §4 "every element of K(M,L) is a
  finite sum of Dirac layers ∂_x^k δ_L ⊗ v_k" is exactly this.
- Prop. 8.8 (p. 64) is preceded, on the same page, by "The following analog of Proposition
  6.45 holds true with formally the same proof, **using Proposition 7.29 and Corollaries 7.13,
  7.15 and 7.31**." The note's "Prop. 8.8 (p. 64) is repaired identically with Cor. 7.31;
  Cor. 7.13 is not needed there" is a correct reading of that sentence.
- p. 4 (Wengenroth Thm 6.1): "the condition of being acyclic can be described as follows
  [39, Theorem 6.1]: for all k, there is some k′ ≥ k such that, for all k″ ≥ k′, the topologies
  of X_{k′} and X_{k″} coincide on some 0-neighborhood of X_k." [39] = Wengenroth (L3801 of
  the reference list), so the note's `\cite[Thm.~6.1]{Wen03}` maps correctly.
- p. 5: "As a consequence, acyclic LF-spaces are complete and regular [39, Corollary 6.5]."
  and "It is said that (X_k) is **compact** if the inclusion maps are compact operators. In this
  case, (X_k) is clearly acyclic …". Both on p. 5. The note's use of each is exact. (Its side
  claim that the inclusions S^m_K → S^{m′}_K are not compact operators is right: a basic
  0-neighborhood of a Fréchet space constrains only finitely many seminorms, so its image is
  not even bounded in S^{m′}_K.)

**Extra finding the first referee only mentioned in passing — and it is a real error IN THE
PAPER that the note correctly diagnoses.** Rendered p. 48: "Since 𝒜(M) is boundedly retractive
(Corollary 6.16), A is contained and bounded in some step 𝒜^m(M). **For any m′ > m**, let
E_{m′} : 𝒜^m(M) → 𝒜̇^{(s)}(M) be the partial extension map given by Proposition 6.29 … there is
some 0-neighborhood **W ⊂ 𝒜^{m′}(M)** so that E_{m′}(W) ⊂ U ∩ 𝒜̇^{(s)}(M)."
Prop. 6.29 gives E_{m′} on 𝒜^{m′}(M); by (6.38) 𝒜^m(M) ⊂ 𝒜^{m′}(M) **iff m′ < m**. So with the
printed m′ > m the map E_{m′} is not defined on the set A it is applied to (and the printed
domain "𝒜^m(M)" contradicts the W ⊂ 𝒜^{m′}(M) two lines later). The note's parenthetical —
"with E_{m′} from Prop. 6.29 (whose domain is A^{m′}(M) ⊃ A^m(M), so m′ < m rather than m′ > m
is the index needed)" — is verified correct on the rendered page. I confirm the first referee's
one-clause ruling and record the full evidence here, because this is an independent defect of
the paper, not merely a citation.

**Notation deviations in the note (cosmetic, recorded for completeness, not repairs).**
The paper sets A(M), Ȧ(M), K(M), K′(M) in **calligraphic** 𝒜, 𝒜̇, 𝒦, 𝒦′ (verified on the
rendered pp. 38, 48), and K(M,L) in plain italic K. The note writes plain A, Ȧ for the boundary
spaces and 𝒦 for K(M), i.e. it keeps the paper's 𝒦(M)-vs-K(M,L) distinction but drops the
calligraphic A. Unambiguous; no reader can be misled. Similarly the note says "the partition of
unity {h, f_i} of (4.10)" where {h, f_j} is in fact introduced in the sentence preceding (4.10)
and used by it. Neither is a citation error.

### Ruling on ITEM 1: HOLDS.
Every statement number, every page, every equation label and every quoted sentence the note
cites is correct against the published text, including the three quotations that depend on
glyphs `pdftotext` destroys. AGREE with the first referee's ITEM 1, on an independent
recomputation of the page map and independent renders. I found no mismatch either.
Sun Sep  6 14:10:47 IST 2026

---

## ITEM 2 — every claim the EXTERNAL ASSESSMENT makes about what the paper says

Each claim is quoted from `external-assessment.md`, then the published text it is about, then a
ruling. I re-derived all of these; I did not read the first referee's Item 2 before doing so.

**A2.1** "The paper defines the full symbol topology using the seminorms (3.1), then introduces
the weaker-looking seminorms (3.4) and (3.5), and claims that those latter seminorms still
describe the topology."
Published p. 15: "The set of symbols of order at most m, S^m(U × R^l), becomes a Fréchet space
with the semi-norms ‖·‖_{K,α,β,m} given by (3.1)." p. 16: (3.4) over compact Q ⊂ U × R^l,
(3.5) the limsup family; Prop. 3.2 "The semi-norms (3.4) and (3.5) together describe the
topology of S^m(U × R^l)." — **ACCURATE**, including "weaker-looking": (3.4) never sees
|ξ| → ∞ and (3.5) is a limsup, so both are continuous on S^m and neither controls (3.1).

**A2.2** "The paper's actual statement is that (3.4) and (3.5) describe the topology, followed
by the claim that S^{m′} and C^∞ have the same topology on S^m."
Rendered p. 17, Cor. 3.4: "For m < m′, the topologies of S^{m′}(U × R^l) and C^∞(U × R^l)
coincide on S^m(U × R^l)." — **ACCURATE**, with the primes exactly where the assessment puts
them (this is one of the places `pdftotext` drops the prime; I checked the render).

**A2.3** "The paper's proof of completeness explicitly extends the proposed seminorms to the
completion and then asserts that the image remains in S^m."
Published p. 16-17 (proof of Prop. 3.2): "Let Ŝ′^m(U × R^l) denote its completion, **where the
stated semi-norms have continuous extensions**. There is a continuous inclusion S′^m ⊂ C^∞,
which can be extended to a continuous map φ : Ŝ′^m → C^∞ … For any a ∈ Ŝ′^m, and K, α and β
like in (3.5), since ‖φ(a)‖′ = ‖a‖′ < ∞, there are C, R > 0 … This shows that ‖φ(a)‖_{K,α,β,m}
< ∞, **obtaining that a ≡ φ(a) ∈ S^m(U × R^l)**. Hence S′^m(U × R^l) is complete."
— **ACCURATE.** One caveat of wording only: the paper does not bare-facedly "assert" that the
image is in S^m, it *derives* it in two estimates. But the derivation's first line is the
identity ‖φ(a)‖′_{K,α,β,m} = ‖a‖′_{K,α,β,m}, which is the very step the note's (b) breaks, so
the assessment's characterization of where the argument lives is right. No repair needed.

**A2.4** "The paper explicitly says Proposition 6.12 gives the topology of A^m(M) from (6.42),
(6.43), and then Corollary 6.14 asserts coincidence with C^∞(M°)."
Published p. 39: Prop. 6.12 "The semi-norms (6.42) and (6.43) together describe the topology of
𝒜^m(M)."; Cor. 6.14 "If m′ < m, then the topologies of 𝒜^{m′}(M) and C^∞(M̊) coincide on
𝒜^m(M). Therefore the topologies of 𝒜(M) and C^∞(M̊) coincide on 𝒜^m(M)." — **ACCURATE.**

**A2.5** "The calculation using the global weighted seminorm (6.41) is particularly persuasive
because it isolates exactly the seminorm the paper's Proposition 6.12 says is part of the
topology."
(6.41) is defined on p. 38, one page BEFORE Prop. 6.12, as the family describing the *defining*
projective topology ("the topology of 𝒜^m(M) can be described by the semi-norms ‖·‖_{k,m}
(k ∈ N_0) given by …"). Prop. 6.12 names (6.42) and (6.43), not (6.41). — **IMPRECISE, and I
agree with the first referee that it is imprecise, but I rank it lower than they do.** Read
strictly, Prop. 6.12 asserts that (6.42)+(6.43) describe *the* topology of 𝒜^m(M), i.e. the
one (6.41) defines; so (6.41) *is* part of that topology by Prop. 6.12's own content, and the
witness's role — kill (6.42) and (6.43) while keeping (6.41) ≥ 1 — is exactly a refutation of
Prop. 6.12. The sentence attributes the definition to the wrong item; it does not misdescribe
the mathematics. Repair (optional, one word): "…the seminorm (6.41), which p. 38 makes part of
the defining topology and which Proposition 6.12 claims (6.42) and (6.43) capture."

**A2.6** "Likewise, the paper's Corollary 7.13 really does assert the corresponding statement
for J^m(M,L)."
Published p. 56, Cor. 7.13: "If m′ < m, then the topologies of J^{m′}(M,L) and C^∞(M\L)
coincide on J^m(M,L). Therefore the topologies of J(M,L) and C^∞(M\L) coincide on J^m(M,L)."
— **ACCURATE.**

**A2.7** "Corollary 4.7 explicitly says its proof proceeds via Corollaries 4.2 and 4.5."
Published p. 23, proof of Cor. 4.7: "Like in Corollary 3.6, **by Corollaries 4.2 and 4.5**, it
is enough to prove that I(M,L) is semi-Montel." — **ACCURATE, verbatim.**

**A2.8** "Corollary 6.22 is explicitly derived from Corollary 6.21."
Published p. 40, immediately before Cor. 6.22: "The following result follows like Corollary
3.6, **applying Corollary 6.21** and using that 𝒜̇(M) is barreled (Corollary 6.7) and a closed
subspace of the Montel space I(M̆, ∂M) (Corollary 4.7)." — **ACCURATE.**

**A2.9** "Corollary 6.27 is explicitly said to have a proof using Corollaries 6.21 and 6.22."
Published p. 41, immediately before Cors. 6.27 and 6.28: "Now the following analogs of
Corollaries 6.21 and 6.22 hold true with formally the same proofs, **using Corollaries 6.21,
6.22 and 6.26**." — **ACCURATE BUT INCOMPLETE**: the printed sentence names three corollaries,
not two, and it covers Cors. 6.27 *and* 6.28 jointly. Nothing the assessment says is false;
it simply omits 6.26 (which is only "K(M) is barreled, ultrabornological and webbed" and plays
no role in the note's argument). Repair, if one is wanted: "…using Corollaries 6.21, 6.22 and
6.26" and "…said of Corollaries 6.27 and 6.28 together." I would not bother.

**A2.10** Quotations of the NOTE inside the assessment (these are claims about the note, not
about the paper, but they belong here because they are checkable text):
- "g_N(x,ξ)=θ(ξ−Ne_1)" — note (a) verbatim.
- "b_j=Σ_{i=1}^j (1+iR)^{m+1}θ(ξ−iRe_1)" — note (b) verbatim (c_i = (1+iR)^{m+1}).
- "u_j=j^{−m′}χ(jx)g(y)" — note (e) verbatim. **The task spec's suspicion that this is the
  wrong witness is unfounded**: (e) IS the boundary witness, and the assessment quotes it in
  the paragraph about Prop. 6.12 / Cor. 6.14, which is the right place. (The Cor.-4.5 witness
  is (d), u_j = j^{n′+m̄′} g(x″)ψ_*(jx′); the assessment never quotes it.)
- "N_{m′}(a;γ) ≤ C[ R^{−(m′−m)/2} N_m(a;0) + R^{m″−m′} max_{γ′∈Γ} N_{m″}(a;γ′) ]" — the note's
  (1) verbatim.
- Calling it "(1)": the note has exactly **one** numbered display
  (`grep -n 'begin{equation}' alkl23-note.tex` -> one hit, line 64; the other three displays are
  `\[ … \]`), and `pdftotext alkl23-note.pdf` shows it printed as "(1)". **Not a discrepancy.**
- "The main package of the paper … stands once this is done." — the note's §1 final sentence,
  verbatim.

### Ruling on ITEM 2: HOLDS-WITH-REPAIR.
Nine of the assessment's nine claims about the paper are accurate as to substance. Two are
loose: A2.5 attributes (6.41) to Prop. 6.12 when p. 38 is where it is defined, and A2.9 names
two of the three corollaries the paper cites and splits a joint sentence. Neither changes any
conclusion. AGREE with the first referee on both flags; I additionally note that A2.3's word
"asserts" understates the paper's two-line derivation, which is a fairness point rather than an
error. No claim FALLS.
Sun Sep  6 14:12:41 IST 2026

---

## ITEM 3 — the note's §1 version claim, and the memoir bibliography entry

**arXiv stamps, read off the PDFs themselves** (`pdftotext | head`):
`arXiv:2304.00798v1 [math.FA] 3 Apr 2023`; `v2 [math.FA] 29 Jul 2023`; `v3 [math.FA] 1 Jun 2024`;
`arXiv:2402.06671v1 [math.GT] 7 Feb 2024`; `v2 [math.GT] 13 Feb 2024`.
Internal dates: v2 "Date: August 1, 2023", v3 "Date: June 4, 2024".
The note's bibliography says "arXiv:2304.00798 (v3, 1 June 2024)" and "arXiv:2402.06671
(v2, 13 February 2024)". **Both dates correct.**

**Claim (i): "arXiv:2304.00798v2 and v3 carry the same numbering" [as the published version].**
I extracted the full anchored header list from each version
(`grep -nE '^(Proposition|Corollary|Remark|Claim|Theorem|Lemma|Example) [0-9]+\.[0-9]+\.'` on the
whitespace-normalized text) and diffed.
- v2 vs v3 header lists: **identical in every number and in every statement text except three
  cosmetic fixes** — Remark 6.47 "becase"→"because"; Cor. 7.16 "x^{m+1/2}H^m(M̊)"→"H^∞(M̊)"
  (a typo fix); Cor. 8.3 "≡"→"=". None of the three is cited by the note.
- v3 vs published: the label sets for §§3-8 coincide exactly. (The five apparent mismatches my
  first grep threw up — Cor. 4.6, Example 6.11, Prop. 4.3, Prop. 6.29, Remark 7.9 — are all
  headers whose number is followed by "(" instead of ".", present in both; and "Proposition 6.7"
  / "Theorem 4.6" are false positives from the cross-references "[25, Proposition 6.7.2]" and
  "[25, Theorem 4.6.1]".)
- I additionally spot-checked the exact statements the note relies on, in v3: Prop. 6.10,
  Prop. 6.12, Cor. 6.14, 6.15, 6.16, Remark 6.17, Cor. 6.21, 6.22, 6.27, 6.28, Prop. 6.29,
  Cor. 6.39, Remark 6.41, Claim 6.46, Cor. 7.13, 7.14, 7.15, 7.17, 7.22, 7.23, Prop. 7.26,
  Cor. 7.31, Prop. 8.8 — every one carries the published number and the published statement.
**Claim (i) HOLDS.**

**The restriction to v2/v3 is not caution for its own sake — v1 really is renumbered.** From my
own header extraction, v1 -> published in §6 shifts by +2 and then by +3:
v1 Prop. 6.8 = pub. Prop. 6.10; v1 Prop. 6.10 ("The semi-norms (6.41) and (6.42) together
describe the topology") = pub. Prop. 6.12; v1 Cor. 6.12 = pub. 6.14; v1 Cor. 6.13 = pub. 6.15;
v1 Cor. 6.14 = pub. 6.16; v1 Remark 6.15 = pub. Remark 6.17; v1 Cor. 6.19 = pub. 6.21;
v1 Cor. 6.20 = pub. 6.22; v1 Cor. 6.24 = pub. 6.27; v1 Cor. 6.25 = pub. 6.28;
v1 Cor. 6.36 = pub. 6.39; v1 Remark 6.38 = pub. Remark 6.41; v1 Claim 6.43 = pub. Claim 6.46.
§7 likewise: v1 Cor. 7.11 = pub. 7.13; v1 Cor. 7.20 = pub. 7.22; v1 Prop. 7.24 = pub. 7.26;
v1 Cor. 7.28 = pub. 7.31. (§8 happens to agree: v1 Prop. 8.8 = pub. Prop. 8.8, though the
wording changed from "The bottom row of (8.4) is exact…" to "The dual-conormal sequence of M
at L is exact…".) Note that v1's equation labels also shift: v1's (6.41)/(6.42) are the
published (6.42)/(6.43), and v1's (6.60) is the published (6.59). **So a reader who opened v1
with the note's numbers in hand would land on the wrong statements — which is precisely why
the note's §1 says "v2 and v3", and it is right to.**

**Claim (ii): "every proposition, corollary, remark and equation cited here from §§3-4 has the
same number and wording in all three arXiv versions."**
I diffed the entire §3-through-§4.3.3 block of v1 against v3 after whitespace normalization.
Substantive differences, complete list:
1. **Remark 3.7**: "…could be given like in Proposition **6.8**" (v1) -> "**6.10**" (v2, v3,
   published). This is the §6 renumbering leaking into a §3 cross-reference. **The note never
   cites Remark 3.7.**
2. "The notation S^m(R^l), S^{±∞}(R^l), etc. is used when U = R^0 = {0}" -> "When U = R^0 = {0},
   the notation S^m(R^l), S^{±∞}(R^l) and S^{(m)}(R^l) is used" (uncited prose).
3. "the Fréchet space I_c^{(∞)}(M,L)" -> "the LCHS I_c^{(∞)}(M,L)" (uncited).
4. "Then, according to Proposition 4.3" -> "According to Proposition 4.3" (uncited).
5. §4.3.3: "Corollary 4.7 **can be extended with** ⊕_m I^m(M,L) and I_{·/c}(M,L), except
   acyclicity in the case of I(M,L)" -> "**has extensions for** …, except acyclicity …".
   The clause the note relies on ("excepts acyclicity") is present, unchanged in force, in all
   three versions; the note paraphrases rather than quotes, so this is not a quotation error.
Everything the note actually cites from §§3-4 — Props. 3.2, 3.3, Cors. 3.4, 3.5, 3.6,
Remark 3.8, the p.-18 bundle sentence, Cors. 4.5, 4.7 and the equations (3.1), (3.4), (3.5),
(4.8), (4.9), (4.10) — is **word-for-word and label-for-label identical in v1, v2, v3 and the
published article**. I confirmed the equation labels directly: (3.1), (4.8) "C_c^∞(U) →
C^∞(N^*U″), u ↦ a", (4.9) "m̄ = m + n/4 − n′/2", (4.10) all sit at the same numbers in all
three. Cor. 4.5's one-line proof "Use Corollary 3.4 and the TVS-embeddings (4.10)." and
Cor. 4.7's "Like in Corollary 3.6, by Corollaries 4.2 and 4.5, …" are identical in v1 and
published. **Claim (ii) HOLDS.**

**Journal metadata.** The PDF's own Subject field reads "Journal of Pseudo-Differential
Operators and Applications, https://doi.org/10.1007/s11868-024-00617-y"; page 1 carries
"J. Pseudo-Differ. Oper. Appl. (2024) 15:47"; the running head carries "Page k of 68" and the
article number 47. The note's entry — "J. Pseudo-Differ. Oper. Appl. 15 (2024), article 47,
68 pp." — matches on every field.

**Memoir arXiv:2402.06671, the five cited places.** PDF page = printed page + 6 in both v1 and
v2 (pdf 21 carries the running head "…15"). Verified verbatim in v2:
- **§2.1.8, printed p. 15** ("Symbols"): "For any open U ⊂ R^n and l ∈ N_0, a symbol of order at
  most m ∈ R on U × R^l …" and then "The following properties hold [ÁLKL23, **Corollaries
  3.4–3.6 and Remark 3.8**]: The topologies of S^∞(U×R^l) and C^∞(U×R^l) coincide on
  S^m(U×R^l), however the second inclusion of (2.1.27) is not a TVS-embedding; C_c^∞(U×R^l) is
  dense in S^∞(U×R^l); and **S^∞(U×R^l) is an acyclic Montel space, and therefore complete,
  boundedly/compactly/sequentially retractive and reflexive**." The note's (f) — "…and to
  [ALKL24m, §2.1.8, p. 15], which restates Cors. 3.4–3.6 for arbitrary open U ⊂ R^n" — is
  exact, and the restatement really is for arbitrary open U, which is what (f) attacks.
  (Under-inclusive by one item: the memoir also restates Remark 3.8 there. Harmless.)
- **§2.5.10, printed p. 38**: "The following is true [ÁLKL23, Corollaries 6.14–6.16 and 6.39 and
  Remark 6.41]: **the topologies of A(M) and C^∞(M̊) coincide on every A^m(M)** …" — that is
  the second assertion of Cor. 6.14, exactly as the note's (e) says.
- **§2.6.7**: the section opens on printed p. **52**; the restating sentence — "Moreover the
  following properties hold [ÁLKL23, Corollaries 7.11–7.13 and 7.15]: … and **the topologies of
  J(M,L) and C^∞(M\L) coincide on every J^m(M,L)**" — is on printed p. **53**. The note cites
  "§2.6.7, p. 53", i.e. the page of the restated claim. Correct as written; a reader who took
  "p. 53" for the section's opening page would be off by one. Not worth changing.
- **§5.2.1, printed p. 119**: "…because **I(F) is compactly retractive** (Section 2.2.2)."
- **§§5.5.3–5.5.4, printed p. 122**: §5.5.3 "Using that **J(F) is compactly retractive**
  (Section 2.6.7) …"; §5.5.4 "Since **I(F) is compactly retractive**, …". Both on p. 122.
- The memoir defines "I(F) = I_{Λ^•}(F) := **I(M, M^0; ΛF)**" and "J(F) := J(M, M^0; ΛF)",
  exactly the note's notation, and its standing hypothesis is a **compact (closed)** foliated
  manifold (M, F) — so the note's "concern a closed M and are covered by the above" is right.
- **"the pages cited are the same in v1"**: I diffed pdf pages 21, 44, 59, 125, 128 of v1
  against v2. Pages 44, 59, 125, 128 are byte-identical after whitespace normalization; p. 21
  differs by exactly one uncited clause ("(l and l′ **being** the ranks…)" -> "…**are** the
  ranks…"). **The claim holds.**

**Repair carried over from ITEM 4 (see below): the memoir is no longer only a preprint.** The
arXiv entry is now published as Springer *Lecture Notes in Mathematics* vol. 2387 (see ITEM 4
for the live evidence and the date). The note's arXiv page numbers do not carry over to the
book, so the entry should either name the book and anchor by **section number** (§2.1.8,
§2.5.10, §2.6.7, §5.2.1, §§5.5.3–5.5.4 — all stable) or keep the arXiv v2 page numbers while
saying explicitly that they are the arXiv v2 pages.

### Ruling on ITEM 3: HOLDS for the paper's version claim; HOLDS-WITH-REPAIR for the memoir entry.
AGREE with the first referee on every sub-claim, on an independent extraction. I add: the exact
list of five v1-vs-v3 differences in §§3-4 (only one, Remark 3.7's cross-reference, is a
statement at all, and it is uncited); the v1 equation-label shift (v1 (6.41)/(6.42) = published
(6.42)/(6.43)), which the first referee did not record and which strengthens the case for the
note's v2/v3 restriction; and the §2.6.7 p.-52-vs-53 point, which I rule harmless.
Sun Sep  6 14:19:03 IST 2026
