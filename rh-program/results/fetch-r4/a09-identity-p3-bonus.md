# Round-4 ingest — agent a09-identity-p3-bonus (Session 18, 2026-09-09)

Scope: identity checks for the two P3 items (7 Ghys 1999, 8 Leichtnam 2008), the BONUS file
(Edwards–Millett–Sullivan 1977), the two re-deliveries in `fetched-r4/duplicates-of-r3/`, the
stray in `fetched-r4/not-on-list/`, and item 17 (zbMATH reviews of Epstein 1976, Cantwell–Conlon
1981, KMNT 2021).

Files handled:
- `fetched-r4/r4-07-ghys-1999-laminations-par-surfaces-de-riemann-AUTHOR-COPY-again.pdf`
  vs `fetched-r3/r3s-35-ghys-1999-laminations-par-surfaces-de-riemann-PS8-author-copy-SWEEP-F-FETCH.pdf`
- `fetched-r4/r4-08-leichtnam-2008-analogy-arithmetic-geometry-foliated-spaces-RMA-copy-UNVERIFIED-edition.pdf`
  vs `results/c3-r/s16/qs4prime/leichtnam-2008-analogy-arithmetic-geometry-foliated-spaces-RENDICONTI-author-copy-WAYBACK-2016-SCOUT-F-FETCH.pdf`
- `fetched-r4/r4-x1-edwards-millett-sullivan-1977-foliations-all-leaves-compact-topology-16-13-32-BONUS.pdf`
- `fetched-r4/duplicates-of-r3/cantwell-conlon-1981-AIF-31-113-135-DUP-of-r3s-32.pdf`
- `fetched-r4/duplicates-of-r3/epstein-1976-AIF-26-265-282-DUP-of-r3s-34.pdf`
- `fetched-r4/not-on-list/blinovsky-arxiv-1703.03827v16-math.GM-NOT-REQUESTED.pdf`

Sections are appended as each unit finishes. Written to disk as I go.

## ITEM 7 (P3) — Ghys 1999, "Laminations par surfaces de Riemann"

### §1 Identity
- `fetched-r4/r4-07-…-AUTHOR-COPY-again.pdf`: 50 pp, A4, PDF metadata Title "lamination", Author "ghys",
  Creator "Textures: AdobePS 8.6", Producer "Acrobat Distiller 4.05 for Macintosh", CreationDate
  2001-04-24. Title page: "Laminations par surfaces de Riemann / par Étienne GHYS"; p. 1 is folio 1;
  p. 50 closes with "Octobre 1997 — Étienne Ghys, École Normale Supérieure de Lyon, UMPA, U.M.R. 128 du
  CNRS, ghys@umpa.ens-lyon.fr". Text layer clean (French, accents OK). Folios printed 1–50; PDF page =
  printed page (offset 0). The table of contents on p. 2 is EMPTY (the "Table des matières" heading
  with nothing under it — a TeX `\tableofcontents` that never got its second pass).
- **Byte-identical to the Round-3 copy.** MD5 of both files = a5e5387848b117c04446df22be4a9436;
  `pdftotext -layout` output identical (154 806 chars each, `cmp` clean, `diff` empty); same page
  count (50), same metadata, same CreationDate.
- **No journal imprint anywhere.** grep for "Panoramas", "Synthèses", "SMF", "Société Mathématique",
  "1999" finds nothing except reference-list entries. The folios are 1–50, not 49–95. The only date on
  the file is "Octobre 1997" (author's date). This is the author's preprint distributed for the
  "État de la recherche" session of January 1997 (p. 1 says so: "Ce texte diffère peu de celui
  distribué aux participants de la session 'État de la recherche' de janvier 1997 ; nous avons ajouté
  le paragraphe 6.4 … et nous avons corrigé quelques énoncés qui étaient parfois un peu 'optimistes'
  dans la première version.").
- Match to the list citation (Panoramas et Synthèses 8 (1999) 49–95): **NOT the journal version.**
  Author copy, no pagination correspondence recoverable from the file itself.

### Verdict: item 7 STILL OPEN as to journal pagination
The sponsor re-delivered the same file. The text is the author's final version (post-1997 corrections,
dated October 1997), so its *content* is usable and was already ingested in Round 3 under r3s-35; but any
page citation to Panoramas et Synthèses 8 must be made by section/theorem number, not by folio, until a
journal copy arrives. Authoritative page range from network citation check: see §3 below.

## ITEM 8 (P3) — Leichtnam 2008, "On the analogy between arithmetic geometry and foliated spaces"

### §1 Identity
- `fetched-r4/r4-08-…-RMA-copy-UNVERIFIED-edition.pdf`: 21 pp, US letter, Creator TeX, Producer
  pdfeTeX-1.30.4, CreationDate 2008-11-27 16:04:33. p. 1: title "ON THE ANALOGY BETWEEN ARITHMETIC
  GEOMETRY AND FOLIATED SPACES / ERIC LEICHTNAM", abstract, contents; p. 1 footer "Date: November 27,
  2008." Running head on odd pages is the author's LaTeX placeholder **"TALK"** (e.g. p. 17), on even
  pages "ERIC LEICHTNAM". Folios 1–21; PDF page = printed page (offset 0). Text layer clean for prose;
  **math is garbled** (Hodge star rendered "?", overlines/superscripts displaced) — formula quotes below
  were verified by vision on a 110-dpi render of p. 17.
- **Byte-identical to the copy already on disk.** MD5 of both = 59aa627e5abcbf6eeafcb573cf245514;
  `pdftotext -layout` output identical (72 311 chars each, `cmp` clean, `diff` empty); same 21 pages,
  same metadata.
- **No journal imprint anywhere.** grep for "Rendiconti", "Rend. Mat", "163", "188", "Volume", "Serie"
  finds nothing but reference-list entries. There is no journal header, no received/accepted line, no
  DOI. This is the author's November 2008 preprint (the same file the Wayback 2016 scout retrieved).
- Match to the list citation (Rend. Mat. Appl. (7) 28 (2008) 163–188): **NOT the journal version.**
  Nothing on the file confirms or contradicts that page range. Both copies are the same preprint.

### §5.1 Assumptions 1]–7] — identical in both copies
The passage (printed p. 17 = PDF p. 17, from "5.1. Structural Assumptions and their consequences." to
the end of Comment 8) was extracted from both files and diffed: **identical, character for character**
(trivially so, since the two PDFs are the same bytes). Verbatim, verified by vision on p. 17:

> **5.1. Structural Assumptions and their consequences.**
> We assume, following Deninger (eg [De01b], [De01]), that to Spec Z ∪ {∞}, one can associate a
> Riemannian (laminated) foliated space (S_Q, F, g, φ^t) satisfying the following assumptions.
> **1].** The leaves are Riemann surfaces and the path connected components of S_Q are three
> dimensional. Moreover, g denotes a leafwise riemannian metric, (φ^t)_{t∈R} is a flow acting on
> (S_Q, F) and permuting the leaves.
> **2].** To each prime p ∈ P there corresponds a unique primitive closed orbit γ_p of φ^t of length
> log p. To the archimedean absolute value of Q there corresponds a unique fixed point
> x_∞ = φ^t(x_∞), ∀t ∈ R, of the flow. The flow is transverse to all the leaves different from the one
> containing x_∞.
> **3].** We assume that:
>   ∀t ∈ R,  e^{−t/2} D_y φ^t(x_∞)|_{T_{x_∞}F} ∈ SO_2(T_{x_∞}F)                (12)
> **4].** We have reduced real leafwise cohomology groups \overline{H}^j_F (0 ≤ j ≤ 2) on which
> (φ^t)_{t∈R} acts naturally such that \overline{H}^0_F ≃ R, \overline{H}^2_F ≃ R and
> \overline{H}^1_F is infinite dimensional. Let [λ_g] denote the class in \overline{H}^2_F of the
> leafwise kaehler metric λ_g associated to g. Then we assume that
>   ∀t ∈ R,  (φ^t)^*([λ_g]) = e^t [λ_g].                                          (13)
> **5]** The action of φ^t on \overline{H}^1_F commutes with the Hodge star ⋆ induced by g. Moreover
> there exists a transverse measure μ on (S_Q, F) such that ∫_{S_Q} (α ∧ ⋆β) μ defines a scalar
> product on \overline{H}^1_F
> **6].** For any α ∈ C^∞_{compact}(R; R), ∫_R α(t)(φ^t)^* dt acting on \overline{H}^1_F is trace
> class. The explicit formula (1) is interpreted as a Lefschetz trace formula for the riemannian
> foliated space (S_Q, F, g, φ^t) with respect to the leafwise cohomology groups \overline{H}^j_F
> (0 ≤ j ≤ 2).
> **7].** The fixed point x_∞ ∈ S_Q should be a limit point of a trajectory γ_∞ :
> lim_{t→+∞} φ^t(y) = x_∞ for any y ∈ γ_∞. Moreover, γ_∞ should have the following orbifold
> structure. Define an orbifold structure on R^{≥0} by requiring the following map to be an orbifold
> isomorphism:
>   Sq : R/{1, −1} → R^{≥0},  Sq(z) = z².
> Notice that Sq transforms the flow φ^t_{R/{1,−1}}(z) = z e^{−t} into the flow
> φ^t_{R^{≥0}}(v) = v e^{−2t}. Then we require that there exists an embedding Ψ : R^{≥0} → γ_∞ such
> that Ψ(0) = x_∞ and
>   ∀(t, v) ∈ R × R^{≥0},  Ψ(φ^t_{R^{≥0}}(v) = v e^{−2t}) = φ^t(Ψ(v)).             (14)
> Lastly we require that γ_∞ is transverse at x_∞ to T_{x_∞}F.
> **Comment 8.** *The stronger assumption ∀t ∈ R, (φ^t)^*(g) = e^t g implies (12) (because φ^0 = Id),
> (13) and the fact that φ^t commutes with the Hodge star not only on \overline{H}^1_F but also on the
> vector space of leafwise differential 1−forms. Deninger told us privately that this assumption
> (φ^t)^*(g) = e^t g might be too strong. Assumption 5] and (13) implies Equation (3) in Deninger's
> formalism. Therefore, the first six Assumptions imply the Riemann hypothesis as explained in
> Section 2!. Assumption 7] is stated here as a hint about a possible way to prove Assumption 6]. See
> the next subsection.*

Typographic quirks preserved from the source: "5]" has no period after the bracket (1]–4], 6], 7] have
"]."); "kaehler", "riemannian" lower-case; "Section 2!."; "(13) implies" (sic, singular). Note that in
this 2008 paper "Deninger told us privately that this assumption … might be too strong" is on **p. 17**
(the program's page-corrected citation of the *other* Leichtnam text, arXiv:math/0603576v2, puts the
parallel remark at p. 12 — different paper, do not conflate).

### Verdict: item 8 STILL OPEN as to journal pagination; CONTENT CONFIRMED STABLE
The sponsor re-delivered the identical preprint. The §5.1 hypotheses the program cites are exactly what
is on disk already. Journal page numbers (163–188) cannot be confirmed from either file; citations
should carry "preprint dated November 27, 2008, §5.1 p. 17" until a Rendiconti copy arrives. Authoritative
page range from network check: see §3 below.

## DUPLICATES — `fetched-r4/duplicates-of-r3/`

- `cantwell-conlon-1981-AIF-31-113-135-DUP-of-r3s-32.pdf` vs
  `fetched-r3/r3s-32-cantwell-conlon-1981-tischler-fibrations-open-foliated-sets-AIF-31-113-135-NUMDAM-ADJ-FETCH.pdf`:
  **byte-identical** (MD5 fa44f7b4d7d8669363999029dd5f65e9 both), 24 pp both, `pdftotext -layout` output
  identical (45 271 chars, `cmp` clean). NUMDAM cover sheet: "John Cantwell, Lawrence Conlon, Tischler
  fibrations of open foliated sets, Annales de l'institut Fourier, tome 31, no 2 (1981), p. 113-135,
  AIF_1981__31_2_113_0". Confirmed duplicate; nothing new.
- `epstein-1976-AIF-26-265-282-DUP-of-r3s-34.pdf` vs
  `fetched-r3/r3s-34-epstein-1976-foliations-all-leaves-compact-AIF-26-265-282-NUMDAM-SWEEP-F-FETCH.pdf`:
  **byte-identical** (MD5 573f41bcc66ec2f22552f0ea633f77b4 both), 19 pp both, text output identical
  (32 474 chars, `cmp` clean). NUMDAM cover sheet: "D. B. A. Epstein, Foliations with all leaves compact,
  Annales de l'institut Fourier, tome 26, no 1 (1976), p. 265-282, AIF_1976__26_1_265_0". Confirmed
  duplicate; nothing new.

## STRAY — `fetched-r4/not-on-list/blinovsky-arxiv-1703.03827v16-math.GM-NOT-REQUESTED.pdf`

Title page (12 pp): "Proof of Riemann hypothesis — Vladimir Blinovsky, Institute for Information
Transmission Problems, B. Karetnyi 19, Moscow, Russia — Abstract: We prove the Riemann hypothesis."
A math.GM preprint (arXiv:1703.03827v16). Not on `FETCH-LIST-ROUND4.md`; not read further, per brief.

## BONUS — Edwards–Millett–Sullivan 1977, "Foliations with all leaves compact"

### §1 Identity
`fetched-r4/r4-x1-…-topology-16-13-32-BONUS.pdf`: 20 pp, publisher scan with OCR text layer. p. 1 header
(verified by vision): "Topology Vol. 16, pp. 13–32. Pergamon Press, 1977. Printed in Great Britain /
FOLIATIONS WITH ALL LEAVES COMPACT* / ROBERT EDWARDS, KENNETH MILLETT and DENNIS SULLIVAN / (Received
20 October 1975)"; footnote *: IHES and NSF support; footnote †: "Let the volumes be determined by a
riemannian metric on the tangent bundle of the foliation, see §4." Last page signed "IHES,
Bures-sur-Yvette, France". Folios 13–32; **PDF page n = printed page n+12** (PDF 1 = p. 13, PDF 20 =
p. 32). Text layer: OCR of a 1977 typeset scan — prose readable, but **math and italics garbled**
(ω → "to", "halfspace" → "hal[space", "codimension" → "condimension", author names mangled). Theorem
statements below were transcribed by vision from 110-dpi renders of pp. 13–14. Matches the citation
Topology 16 (1977) 13–32 EXACTLY.

### §2 What the program uses Epstein for
`results/c3-r/s16/novelty/adjudication.md` §1 N-E and §4 item 3: the program's "closed leaf ⇒ compact
leaf on a compact foliated space" was graded ANTICIPATED by Epstein, Ann. Inst. Fourier 26 (1976)
265–282, §§2.2–2.4 printed p. 268 ("a leaf meets a coordinate neighbourhood in at most a countable
number of slices"; L ∩ T perfect by holonomy propagation, hence uncountable by Baire; "the subspace
topology is equal to the leaf topology on a closed leaf"), in Ehresmann's foliated-space generality.
Item 3 wants only a *second, textbook* citation for that point-set lemma. The program does NOT use
Epstein's volume-bound theorem for periodic flows on 3-manifolds.

### §3 EMS main results, verbatim (vision-verified)
Printed p. 13, the Question:
> *If M is a compact manifold foliated by compact submanifolds (everything smooth), is there an upper
> bound on the volume of the leaves?†*

Printed p. 13:
> **THEOREM 1.** *Suppose M is a compact smooth manifold which is smoothly foliated by compact leaves of
> dimension d. Suppose that the leaves are oriented in a continuous manner, and that the images of the
> fundamental classes of the leaves all lie in some open halfspace of the d-dimensional real homology of
> M. Then there is an upper bound on the volumes of the leaves of M. Consequently, all the holonomy groups
> of the foliation are finite.*
>
> Another way of stating the homological condition is to say there exists a closed d-form ω on M, such
> that ω has a positive integral along each leaf. Here M may have boundary, in which case we assume that
> the boundary is a union of leaves. The with-boundary version of the Theorem follows from the
> without-boundary version by doubling M along its boundary.

Printed pp. 13–14, the two named applications: "(i) each leaf of the foliation has positive
(respectively negative) euler characteristic, or (ii) the ambient manifold is kaehler and the foliation
is complex analytic." (Details §7, p. 27; case (ii) "actually follows from the first part of the proof
of the Theorem (the Moving Leaf Proposition, §5)".)

Printed p. 14, the sharpened form: "Theorem 1 does not require so sweeping a homological hypothesis as
stated above. The proof of the theorm [sic] deals only with a neighborhood of what Epstein calls the
*bad set* of M, which is the union of leaves of M near which the volume function is not bounded. … in
general one can at least say that it is closed and nowhere dense (see §§4, 6). Our proof reveals that it
must be empty if there is a closed d-form ω, defined on a neighborhood of the bad set, whose integral is
positive along each leaf of the bad set. For this argument M need not be compact, as long as the bad set
itself is compact."

Printed p. 14 (restated p. 27, §8, with "codimension 2" and "the volume of the leaves of the foliation …
all holonomy groups", and the remark "We note that there are no orientation assumptions here at all"):
> **THEOREM 2** (*extending* [3]). *Suppose M is a smooth compact manifold which is smoothly foliated by
> compact leaves of codimension two. Then there is an upper bound on the volumes of the leaves of M.
> Consequently, all the holonomy groups of the foliation are finite.*

Preceded on p. 14 by: "Our second principal result is that the Epstein argument mentioned above can be
adapted to hold in codimension two in general. This has also been done by Vogt." Here [3] = D. B. A.
Epstein, *Periodic flows on 3-manifolds*, Ann. Math. 95 (1972) 68–82 (reference list, p. 32) — NOT the
1976 AIF paper, which is their [4] and is cited as "I.H.E.S. preprint (December 1974)".

**The counterexample** (printed p. 13, §1): "After our research was completed, the third author found a
smooth flow on a closed 5-manifold [15, 16], which showed that the answer, in general, was no. … The
latter example shows that some additional hypothesis on M is required." [15] = D. Sullivan, *A new
flow*, Bull. Am. Math. Soc. 82 (1976) 331–332; [16] = D. Sullivan, *A counterexample to the periodic
orbit conjecture*, Publ. Math. IHES 46 (1976). And on p. 14: "in the counter example mentioned above
[15, 16], the bad set is S³ foliated as the Hopf bundle." Reeb's non-compact example (thesis, [12]) shows
the question "is global and cannot be answered by simply considering the structure of the foliation in
a neighborhood of individual compact leaves." Known positive cases listed on p. 13: codimension 1
"by a relatively elementary argument [12]"; periodic flows on compact 3-manifolds, Epstein [3].

Other statements a future session may want (page = printed):
- p. 13: "The boundedness of volume near any given leaf is equivalent to the finiteness of the holonomy
  group of that leaf, and also to the hausdroff [sic] separation property for the topology of the leaf
  space near the leaf ([4], [8], see also §4)." — cites Epstein 1976 [4] for exactly the
  local-structure equivalences.
- p. 13: "in the presence of a bound on the volume, a structure theorem due to Ehresmann [4, Theorem 4.3]
  provides a nice picture of the local behavior" — note they attribute Ehresmann's theorem *as stated in
  Epstein [4] Theorem 4.3*.
- p. 22 (PDF 10), §4 "Proposition 4.1 (Properties of the volume function)"; p. 24 (PDF 12), §5
  "MOVING LEAF PROPOSITION. If X₁ is compact and nonempty, then there exists a sequence of …" generic
  leaves approaching the bad set with volumes → ∞; remark 1 after it: "This Proposition remains true in
  the absence of any orientation assumptions whatever"; remark 2: it "in fact holds for topological
  foliations of topological manifolds".
- p. 25–26 (PDF 13–14), §6: the Epstein decreasing filtration {X_α} of the bad set by compact saturated
  subsets, "X_β is a closed nowhere dense subset of X_α" for β > α.
- p. 27 (PDF 15), §8: Transversal Proposition (transverse open 2-manifold T_α, properly embedded in a
  neighborhood of X_α, meeting every leaf of X_α), from which Theorem 2 follows by intersection numbers.
- p. 15: the geometric-current homology relation lim (1/n_i)[L_i] = Σ_α r_α [L_α] and the
  Ruelle–Sullivan current machinery (§§2–3, pp. 15–20), which is the same device the program's
  Sullivan-1976 item (r4-16a) concerns.

### §3 Relation to Epstein 1976 as the program uses it (my reading)
What the program takes from Epstein 1976 is the point-set lemma of his §2 (countable slices, holonomy
propagation, Baire, leaf topology = subspace topology on a closed leaf), valid for Ehresmann foliated
spaces; EMS 1977 does not restate or reprove that lemma — it cites Epstein's preprint [4] only for the
*downstream* local-structure facts (volume bound near a leaf ⇔ finite holonomy ⇔ Hausdorff leaf space
near the leaf; Ehresmann's local structure theorem as "[4, Theorem 4.3]"). EMS is a companion in the
sense that it takes Epstein's *global* question (is leaf volume bounded when every leaf is compact?) and
answers it in higher codimension: yes under a homological positivity hypothesis (Theorem 1), yes
unconditionally in codimension 2 (Theorem 2, generalizing Epstein's 1972 periodic-flow theorem from
3-manifolds to all dimensions), and no in general (Sullivan's 5-manifold flow, bad set = Hopf-fibered
S³). None of this bears on the N-E adjudication: EMS is a manifold-only, smooth, all-leaves-compact
paper, and it supplies **no second citation for the closed-leaf ⇒ compact-leaf lemma** — item 3 of §4
stays open as far as this file is concerned. Its only potential use to the program is elsewhere: the
geometric-current/transverse-measure language (§§2–3, after Ruelle–Sullivan) is the same one the
program's Sullivan-1976 and Plante-1975 items live in, and Theorem 1's "closed d-form positive on every
leaf" is the leaf-homology analogue of a "no invariant transverse measure" statement.

### §5 Caveats for corpus-routing.md
- r4-x1: OCR layer garbles ω as "to" and italics/superscripts throughout; PDF n = printed n+12; verify
  any formula by vision. Their reference [3] is Epstein 1972 (Ann. Math.), [4] is Epstein 1976 (cited as
  a 1974 IHES preprint) — do not confuse when following "extending [3]".
- r4-07: same bytes as r3s-35; no journal folios; the table of contents on p. 2 is empty.
- r4-08: same bytes as the s16/qs4prime Wayback copy; running head "TALK" is a LaTeX placeholder, not a
  venue; math in the text layer is unreliable (Hodge star → "?").

## §3 (items 7 and 8) — authoritative page ranges from zbMATH Open (read 2026-09-09)

Source: zbMATH Open API, `https://api.zbmath.org/v1/document/_search?search_string=…` (the zbmath.org
website returned HTTP 403 to the fetcher; the API answered 200 on the first try). Read-date 2026-09-09.

- **Item 7, Ghys.** Zbl 1018.37028. Title as indexed: "Riemann surface laminations." (zbMATH's English
  rendering; original French title "Laminations par surfaces de Riemann"). Source line verbatim:
  "Cerveau, Dominique et al., Dynamique et géométrie complexes. Paris: Société Mathématique de France.
  Panor. Synth. 8, 49-95 (1999)." Collection: Zbl 1010.00008. No DOI recorded. **Confirms the list's
  citation Panoramas et Synthèses 8 (1999) 49–95.** Implied folio offset for the on-disk author copy:
  author p. 1 ≈ journal p. 49, i.e. +48, *but the author copy's line breaks and page breaks are not the
  journal's* (author copy is 50 pp on A4 versus 47 journal pages), so this offset must NOT be used for
  page citations; cite by section number (§2 Exemples … §7) until a journal copy exists.
  Review (Viorel Vâjâitu), verbatim: "This very well-written paper contains a systematic analysis of the
  properties of laminations by Riemann surfaces. Roughly speaking, a lamination is a generalization of a
  foliation to compact spaces which are not manifolds. The paper begins with a series of examples, e.g.
  the construction by Sullivan of a lamination associated to a \(\mathbb{C}^r\) expanding map of the
  circle. Differential forms on a lamination are constructed in Section 3; then Section 4 is devoted to a
  Riemann-Roch formula for a lamination. Section 5 and 6 treat the problem of uniformization of a
  lamination. The last paragraph, Section 7, give three theorems on the existence of non-constant
  meromorphic functions on a lamination. / For the entire collection see [Zbl 1010.00008]."
  (The reviewer's section map — §3 forms, §4 Riemann–Roch, §§5–6 uniformization, §7 meromorphic
  functions — matches the author copy's section headings, a further check that the author copy is the
  published text.)

- **Item 8, Leichtnam.** Zbl 1173.14015. Title: "On the analogy between arithmetic geometry and foliated
  spaces". Source line verbatim: "Rend. Mat. Appl., VII. Ser. 28, No. 2, 163-188 (2008)." No DOI
  recorded. **Confirms the list's citation Rend. Mat. Appl. (7) 28 (2008) 163–188, and adds issue
  No. 2.** Implied offset preprint p. 1 ≈ journal p. 163 (+162), 21 preprint pages versus 26 journal
  pages — again the journal repaginates; cite "§5.1, Assumptions 1]–7]" rather than a folio.
  Review (Florin Nicolae), verbatim: "This is a survey on some results which support Deninger's point of
  view that expected properties of arithmetic zeta functions could be proved by a cohomology theory of
  suitable foliated spaces. In this theory, the explicit formulae for the arithmetic zeta functions
  should be interpreted as a Lefschetz trace formula. In Section 2 the author recalls Deninger's
  cohomological formalism in the case of the Riemann zeta function. Section 3 is devoted to the
  description of the Lefschetz trace formula for a flow acting on a codimension one foliated space. In
  Section 4 the author recalls the statement of Lichtenbaum's conjecture for a number field and explains
  briefly how Deninger proved an analogue of this conjecture in the case of a foliation
  \((X,{\mathcal F},\phi^t)\) with the following properties: \(X\) is a smooth compact 3-dimensional
  manifold endowed with a codimension 1 foliation \({\mathcal F}\) and the flow \(\phi^t\) preserves
  globally the foliation and is transverse to it. In Section 5 the author makes a synthesis of various
  results of Deninger. He states several axioms for a laminated foliated space, which, if satisfied,
  allow to construct the required cohomology groups for the Riemann zeta function."
  The reviewer's description of Section 5 ("several axioms for a laminated foliated space") matches
  §5.1 of the preprint; nothing in the review records a statement the preprint does not print.

## ITEM 17 — zbMATH Open records for Epstein 1976, Cantwell–Conlon 1981, KMNT 2021 (read 2026-09-09)

Method: zbMATH Open API, `https://api.zbmath.org/v1/document/_search?search_string=…` and
`https://api.zbmath.org/v1/document/<Zbl id>`; every call answered HTTP 200 on the first attempt.
The zbmath.org *website* was not usable from this session (HTTP 403 to the fetcher; curl got a 5.8 KB
bot-check page rather than the record). The API returns the complete document record including the
`editorial_contributions` array, which is where zbMATH Open keeps review and summary texts; an empty
array means zbMATH Open has no review/summary text on file for that item. Read-date 2026-09-09.

1. **Epstein 1976.** Zbl 0313.57017 (zbMATH internal id 3490112, `https://zbmath.org/3490112`).
   Source line: "Ann. Inst. Fourier 26, No. 1, 265-282 (1976)". DOI 10.5802/aif.607; NUMDAM
   AIF_1976__26_1_265_0; EuDML 74269. MSC 57R30. `editorial_contributions: []` — **zbMATH Open carries
   NO review text and no summary for this paper.** Keywords: none. (The record does carry the paper's
   reference list, e.g. [1] Ehresmann 1950 Bruxelles 29–55, [2] Epstein, Periodic flows on 3-manifolds,
   Ann. Math. 95 (1972) 68–82, [3] Haefliger 1962, [4] Haefliger 1958, [5] Montgomery–Zippin 1955,
   [6] Palais 1970.) So a reviewer's restatement of "closed leaf ⇒ compact leaf" cannot be obtained
   from zbMATH; the adjudication's §4 item 8 hope ("in case a reviewer recorded a statement the papers
   do not print") is closed on the zbMATH side for this paper — nothing there beyond the paper itself.
   MathSciNet (closed) remains the only other review venue and was not consulted (brief §6).

2. **Cantwell–Conlon 1981.** Zbl 0442.57007 (internal id 3690294, `https://zbmath.org/3690294`).
   Source line: "Ann. Inst. Fourier 31, No. 2, 113-135 (1981)". DOI 10.5802/aif.831; NUMDAM
   AIF_1981__31_2_113_0; EuDML 74492. MSC 57R30. `editorial_contributions: []` — **zbMATH Open carries
   NO review text and no summary for this paper.** Keywords: none. (Reference list present in the
   record: [1] Cantwell–Conlon, Nonexponential leaves at finite level (to appear, 1982); [2] Poincaré–
   Bendixson theory for leaves of codimension one, TAMS (to appear); [3] Growth of leaves, CMH 53 (1978)
   93–111; [4] Conlon, Transversally complete e-foliations of codimension two, TAMS 194 (1974) 79–102;
   [5] Dippolito, Ann. Math. 107 (1978) 403–453; [7] Fuchs, Infinite Abelian Groups I.) Same
   conclusion: no reviewer statement exists on zbMATH to supplement the paper.

3. **KMNT 2021.** Zbl 1492.37034 (internal id 7481094, `https://zbmath.org/7481094`). Title as indexed:
   "On 3-dimensional foliated dynamical systems and Hilbert type reciprocity law". Authors: Kim,
   Junhyeong; Morishita, Masanori; Noda, Takeo; Terashima, Yuji. Source line: "Münster J. Math. 14,
   No. 2, 323-348 (2021)". DOI 10.17879/06089649100. **Confirms the program's citation Münster J. Math.
   14 (2021) 323–348, adding issue No. 2.** The record carries an author SUMMARY (contribution_type
   "summary", no reviewer), not a third-party review. Verbatim:
   "Summary: We introduce a geometric analog of the Hilbert symbol and show a Hilbert type reciprocity
   law for a 3-dimensional foliated dynamical system (FDS\(^3\) for short). This answers the question
   posed by \textit{C. Deninger} [Doc. Math. Extra Vol., 163--186 (1998; Zbl 0899.14001); Prog. Math.
   171, 29--87 (2000; Zbl 1159.11310); Jahresber. Dtsch. Math.-Ver. 103, No. 3, 79--100 (2001;
   Zbl 1003.11029); Contemp. Math. 300, 99--114 (2002; Zbl 1077.14022); Lond. Math. Soc. Lect. Note
   Ser. 354, 174--190 (2008; Zbl 1163.37006)]. For this, we employ the theory of smooth Deligne
   cohomology and the integration theory of Deligne cohomology classes. We also present a structure
   theorem for an FDS\(^3\), which yields a classification of FDS\(^3\)'s, and we construct concrete
   examples of FDS\(^3\)'s for each type of the classification."
   Nothing in the summary bears on Lemma 1.9 / Def. 1.10 / Remark 2.8 / Cor. 2.9 / Prop. 2.10 beyond
   what the paper prints; it does confirm the "structure theorem … classification of FDS³'s" that the
   program's N-G discussion relies on exists as the authors describe it.

**Item 17 outcome:** reachable, answered. Two of the three have no zbMATH review text at all (this is a
fact about zbMATH's holdings, not a network failure — the records were retrieved in full); the third has
only the authors' summary. The "reviewer recorded a statement the papers do not print" possibility is
therefore exhausted on zbMATH for all three. Not consulted: MathSciNet (closed, per brief §6).

## SUMMARY OF VERDICTS

| Item | File | Same as on disk? | Journal imprint? | Verdict |
|---|---|---|---|---|
| 7 (P3) | r4-07 Ghys 1999 | byte-identical to r3s-35 (MD5 a5e5…9436) | none; author copy, folios 1–50, dated Oct 1997 | **STILL OPEN** for journal folios; page range 49–95 confirmed via Zbl 1018.37028 (Panor. Synth. 8) — cite by section |
| 8 (P3) | r4-08 Leichtnam 2008 | byte-identical to the s16/qs4prime Wayback copy (MD5 59aa…4514) | none; preprint dated 2008-11-27, running head "TALK" | **STILL OPEN** for journal folios; §5.1 Assumptions 1]–7] identical and vision-verified; range 163–188 confirmed via Zbl 1173.14015 (Rend. Mat. Appl. VII. Ser. 28, No. 2) |
| bonus | r4-x1 EMS 1977 | new | Topology 16 (1977) 13–32, Pergamon — exact match | identity confirmed; Theorems 1, 2 and the Sullivan counterexample recorded verbatim; no bearing on N-E |
| dup | cantwell-conlon DUP | byte-identical to r3s-32 | NUMDAM | ignore |
| dup | epstein DUP | byte-identical to r3s-34 | NUMDAM | ignore |
| stray | blinovsky | — | arXiv math.GM | not on list; not read |
| 17 | zbMATH reviews | — | — | delivered: Epstein and Cantwell–Conlon have NO review text on zbMATH Open; KMNT has the authors' summary (recorded) |

Nothing found contradicts the program's record. One page-citation hygiene note: Leichtnam's "might be too
strong" remark exists in TWO papers — Rend. Mat. 2008 preprint p. 17 (Comment 8, this file) and
arXiv:math/0603576v2 p. 12 (the one the adjudication corrected) — keep them apart.

*Agent a09-identity-p3-bonus, Session 18, 2026-09-09.*
