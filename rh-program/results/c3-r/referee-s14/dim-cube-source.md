# SOURCE RECORD — dim [0,1]^n = n (the Lebesgue covering theorem) and closed-subspace monotonicity, for probe A, Theorem B(b), part (b2)

**Program:** RH program, direction C3-r. **Session 14, 2026-09-02.** **Author:** source-fetching agent (Claude Fable 5.1). **Discharges:** `results/c3-r/referee-s14/A-thmB-adjudication.md`, finding M-4 and §8 action item 1 ("Fetch a dimension-theory source ... before any external circulation of 'Y₀ is infinite-dimensional' / 'dim S = ∞'; until then the (b2) sentence carries [RU]"). **Standing order 1/5:** every statement below was read from a page image on disk during this session; nothing is quoted from memory. Where a source was read but could *not* legitimately be kept on disk, the record says so and the sponsor block in §6 gives the data needed to obtain it.

---

## 0. Result

**The [RU] label on (b2) can be lifted to "on disk, free, legitimately held" on the strength of one fetched source, with a second fetched source for the classical Lebesgue statement itself:**

- **[r3s-25]** `fetched-r3/r3s-25-schultz-2012-notes-topological-dimension-theory-ucr-SESSION14-FETCH.pdf` — Reinhard Schultz, *Notes on Topological Dimension Theory*, University of California, Riverside, 2012, 18 pp.; posted by the author on his university site, `https://math.ucr.edu/~res/miscpapers/top-dimension-theory.pdf` (server Last-Modified 29 Jun 2013; 169,151 bytes; SHA-256 `8b6b3e506635d3a382ddcfdba0a37a9af70e999dd74c170bf21a9b4c450d2fed`). **Theorem 7 (i) and (iii), p. 7, with complete proofs on pp. 3 and 7–9:** the Lebesgue covering dimension of the disk D^n is n, and every compact A ⊂ R^n with nonempty interior — in particular [0,1]^n — has Lebesgue covering dimension n. The definition used (p. 2) is the finite-open-cover covering dimension of Munkres §50, i.e. the one used in the adjudication's §3.10.
- **[r3s-26]** `fetched-r3/r3s-26-karasev-2013-covering-dimension-toric-varieties-arxiv-1307.3437v1-SESSION14-FETCH.pdf` — Roman Karasev, *Covering dimension using toric varieties*, arXiv:1307.3437v1 (12 Jul 2013), 6 pp.; published as Topology and its Applications 177 (2014) 59–65, DOI 10.1016/j.topol.2014.08.006; arXiv non-exclusive distribution license (SHA-256 `16f1de620d122b97fd4eade1ba78f9e930835c1c9f0f61904c732d4295a6c2ed`). A refereed, legitimately free proof of Lebesgue's covering theorem in its closed-cover form (statement quoted in §2.3).

**The classical primary source, Hurewicz–Wallman (Princeton 1941; revised edition 1948), was located and read, and its statements are transcribed in §2.2 with page numbers — but it is NOT on disk.** The scan on archive.org (Digital Library of India item) is labeled "Copyright Permitted" on its page, on the strength of which it was downloaded for reading; the U.S. Copyright Office's *Catalog of Copyright Entries* then showed the copyright **renewed in 1969 (R468228, claimant Henry Wallman)**, so the book is still under U.S. copyright and the archive.org label is wrong. The scan was deleted from the scratchpad and was never placed in `fetched-r3/`. The transcribed statements stand as attributed short quotations; §6 gives the sponsor what is needed to buy the book. Engelking's *Dimension Theory* (1978) is lending-only on archive.org and otherwise not legitimately free; §6 covers it too.

**Recommended citation text for (b2) is in §4; the monotonicity statement's sources are in §5.**

---

## 1. What was searched, and what each page said

All fetches went through retry loops (network is patchy); each outcome below is what the page or server actually returned on 2026-09-02.

### 1.1 Hurewicz–Wallman, *Dimension Theory* (Princeton Mathematical Series 4)

| Where | What the page/record says (verbatim where quoted) | Outcome |
|---|---|---|
| archive.org, `https://archive.org/details/in.ernet.dli.2015.84609` (metadata API `https://archive.org/metadata/in.ernet.dli.2015.84609`) | `title => Dimension Theory`; `creator => Hurewicz,witold.`; `date => 1948`; `collection => ['digitallibraryindia', 'JaiGyan']`; description block: "dc.publisher: Princeton University Press", "dc.rights: Copyright Permitted", "dc.source.library: Osmania University", "dc.description.scanningcentre: RMSC, IIIT-H", "dc.description.totalpages: 184"; files offered for download: `2015.84609.Dimension-Theory.pdf` (Image Container PDF, 13,291,310 bytes), `2015.84609.Dimension-Theory_text.pdf` (Additional Text PDF, 12,742,538 bytes), `2015.84609.Dimension-Theory_djvu.txt`; no `access-restricted-item` flag. | Downloaded to the session scratchpad **only** because the page states "Copyright Permitted" and offers the files; read for the statements in §2.2; **deleted after the renewal record (below) showed the label to be wrong**. Not copied to `fetched-r3/`. |
| The scan's own copyright page (PDF p. 8) | "Copyright, 1941, by Princeton University Press / *Revised edition, 1948* / Printed in the United States of America" | Fixes the edition read: the 1948 revised edition. |
| **U.S. Copyright Office, *Catalog of Copyright Entries*, Third Series, vol. 23, part 1, no. 2, p. 2817 (renewals, 1969)** — via the New York Public Library's open transcription, `https://github.com/NYPL/cce-renewals`, file `data/1969-1.tsv` (README: "copyright renewals from the US Copyright Office's *Catalog of Copyright Entries* for the years 1950–1977 (based on Project Gutenberg transcriptions)") | Record `c02e05f5-a1a0-58f6-b3c1-1f992a5f1939`, full text: **"WALLMAN, HENRY. Dimension theory, by Henry Wallman & Witold Hurewicz. © 22Dec41; A160903. Henry Wallman (A); 8Sep69; R468228."** Parsed fields: original registration A160903, 1941-12-22; renewal R468228, 1969-09-08; claimant Henry Wallman (A). No hit for "Hurewicz", "Wallman", or "Dimension theory" in `data/1968-1.tsv` (9,356 renewal lines); the one hit above is in `data/1969-1.tsv` (7,439 lines). | **Copyright renewed.** A 1941 U.S. work whose copyright was renewed is protected for 95 years from publication, i.e. through 2036. The archive.org/DLI copy is therefore not a legitimately free copy, whatever its label says. |
| Stanford Copyright Renewals database, `https://exhibits.stanford.edu/copyrightrenewals/catalog?q=Hurewicz` | curl (HTTP 200): "Please enable JavaScript to view the page content. Your support ID is: …"; in Chrome: page heading "Traffic control and bot detection..." / "If this check is preventing you from making use of our resources, make sure you have cookies enabled." — did not clear after repeated waits. | **Not consulted** (bot-detection screen; not bypassed, per policy). The NYPL transcription of the same underlying Copyright Office catalog substitutes for it. |
| HathiTrust, `https://catalog.hathitrust.org/Search/Home?lookfor=Hurewicz+Wallman+dimension+theory` and `https://babel.hathitrust.org/cgi/ls?q1=…` | curl: HTTP 403, "Just a moment... Enable JavaScript and cookies to continue"; in Chrome: "catalog.hathitrust.org — Performing security verification — This website uses a security service to protect against malicious bots." — did not clear after repeated waits. Web search surfaced HathiTrust catalog records for Engelking's *Theory of dimensions, finite and infinite* (Record 003031306) but none for Hurewicz–Wallman. | **Not consulted** (bot-detection screen; not bypassed). Given the 1969 renewal, a HathiTrust copy could at most be "Limited (search-only)". |
| Princeton University Press / JSTOR / De Gruyter pages (web search) | Sold as *Dimension Theory (PMS-4)*, Princeton Legacy Library: paperback ISBN 9780691627748; hardcover ISBN 9780691653686; e-book ISBN 9781400875665, DOI 10.1515/9781400875665; JSTOR stable `j.ctt183pk8v`. Google Books id `_xTWCgAAQBAJ`. | Not free. Consistent with the renewal. Data carried into §6. |

### 1.2 Engelking, *Dimension Theory* (1978)

| Where | What the page/record says | Outcome |
|---|---|---|
| archive.org, `https://archive.org/details/dimensiontheory0000rysz` (metadata API) | `title => Dimension theory`; `creator => Ryszard, Engelking`; `publisher => Amsterdam ; New York : North-Holland Pub. Co.`; `date => 1978`; `isbn => 0444851763`; `lccn => 78012442`; `oclc-id => 4195058`; description "x, 314 p.", "Translation of Teoria wymiaru", "Errata slip inserted", "Bibliography: p. [289]-308"; `collection => ['internetarchivebooks', 'inlibrary', 'printdisabled']`; `access-restricted-item => true`; item page: "No suitable files to display here". | **Lending-library only; not downloadable; not downloaded.** |
| `https://webhomes.maths.ed.ac.uk/~v1ranick/papers/engelking.pdf` (the late Andrew Ranicki's paper archive at Edinburgh) | Server: HTTP 200, `Content-Type: application/pdf`, `Content-Length: 4693683`, `Last-Modified: Thu, 17 Mar 2011`. The index page `…/~v1ranick/papers/` carries no rights or permission statement for this file. | A scan of an in-copyright 1978 book on a personal page with no statement that it is freely available. **Not downloaded**, per the task's rule. Recorded here so the sponsor knows it exists. |
| Engelking, *Theory of Dimensions, Finite and Infinite* (Heldermann 1995) | HathiTrust catalog Record 003031306 exists (from web search); access level not readable (bot screen). | Not free. |

The theorem numbers named in the tasking (Engelking "Thm 1.8.2", Hurewicz–Wallman "Thm IV 1") were treated as untrusted. Hurewicz–Wallman's numbers were verified from the page images (§2.2: the cube statement is the *Corollary* on p. 42 following Theorem IV 1; the Lebesgue covering theorem is Theorem IV 2). **Engelking's numbers remain unverified** — no legitimate copy could be read — and are not cited below.

### 1.3 Free alternatives found

| Candidate | Where | What it contains | Outcome |
|---|---|---|---|
| **R. Schultz, *Notes on Topological Dimension Theory*, UC Riverside, 2012** | `https://math.ucr.edu/~res/miscpapers/top-dimension-theory.pdf` (author's university site) | Definition of Lebesgue covering dimension (p. 2, after Munkres §50); Theorem 50.6 of Munkres re-proved via Lemma 1 (upper bound for the hypercube, p. 3); Čech homology; Theorem 5, 6, 7 (p. 7) with proofs (pp. 7–9): dim D^n = n, and dim A = n for compact A ⊂ R^n with nonempty interior; Theorem 8 (dim R^n = n, p. 9). | **Fetched as [r3s-25].** Best free source: exact statement, complete proof, standard definition. |
| **R. Karasev, *Covering dimension using toric varieties*, arXiv:1307.3437** | arXiv; Topology Appl. 177 (2014) 59–65 | Proof of Lebesgue's covering theorem (closed-cover form) and of the KKM theorem from toric geometry. | **Fetched as [r3s-26].** Refereed, free, primary for the Lebesgue statement. |
| A. Freire, *Covering dimension and embedding theorems* (UTK, Math 561, Fall 2022) | `https://web.math.utk.edu/~afreire/teaching/m561f22/Covering_dimension.pdf` | Theorem 1: a σ-compact Hausdorff space all of whose compact subspaces have covering dimension ≤ m has covering dimension ≤ m (proof outlined as exercises after Munkres p. 316); Exercise 4 corollaries: every topological m-manifold has covering dimension ≤ m; every closed subspace of R^N has covering dimension ≤ N. | Read in the scratchpad; **upper bounds only** — no proof that dim [0,1]^n ≥ n. Not fetched. |
| Munkres, *Topology* (2nd ed.) §50 | not free | Theorems 50.1 (closed subspaces), 50.2 (finite unions of closed subspaces), 50.6 (compact subsets of R^n) — as cited by Schultz on pp. 3, 8, 9 | Not on disk; cited only through Schultz. |
| Hatcher, *Algebraic Topology* | free on the author's site | Used by Schultz for open stars/nerves (p. 3) and for H_n(D^n, S^{n−1}) ≅ Z (p. 8). | Not fetched (the program's need is the dimension statement, which Schultz carries). |

---

## 2. Verbatim statements, with page numbers

### 2.1 Schultz 2012 — [r3s-25], on disk

Page numbers are the printed ones (= PDF page numbers).

**p. 2, "The basic setting":**

> We shall base our discussion upon the material in Section 50 of Munkres, *Topology*. For the sake of clarity we shall state the main definition and mention some standard conventions.
>
> **Definition.** Let X be a topological space, let n be a nonnegative integer, and let 𝒰 be an indexed open covering of X. Then we shall say that *the open covering 𝒰 has order at most n* provided every intersection of the form U_{α(0)} ∩ ⋯ ∩ U_{α(n)} is empty, and we shall say that *the space X has Lebesgue covering dimension ≤ n* provided every open covering 𝒰 of X has a refinement 𝒱 of order ≤ n. Frequently we shall write dim X ≤ n if the Lebesgue covering dimension is at most n.

**p. 3:**

> We shall say that dim X = n (the Lebesgue covering dimension is equal to n) if dim X ≤ n is true but dim X ≤ n − 1 is not. By convention, the Lebesgue covering dimension of the empty set is taken to be −1, and we shall write dim X = ∞ if dim X ≤ n is false for all n.

> **THEOREM 50.6 in MUNKRES (*Topology*).** *If A is a compact subset of ℝ^n, then dim A ≤ n.*
>
> **Alternate proof.** We know that there is some very large hypercube K of the form [−M, M]^n which contains A, and we also know that A is closed in this hypercube. By Theorem 50.1 on pages 306–307 of Munkres, *Topology*, it is enough to show that the hypercube has dimension at most n. Since every hypercube has a simplicial decomposition with simplices of dimension ≤ n, it will suffice to prove the following result:
>
> **LEMMA 1.** *If P ⊂ ℝ^m is a polyhedron with an n-dimensional simplicial decomposition, then the topological dimension of P is at most n.*

and the proof of Lemma 1 (same page), which ends:

> … the n-dimensionality of the decomposition implies that every intersection of (n + 2) distinct open stars must be empty. This is exactly the criterion for the covering by open stars to have order at most (n + 1). Therefore we have shown that 𝒰 has a finite open refinement with at most this order, which means that the topological dimension of K is at most n.■

**p. 7:**

> **THEOREM 5.** *If X is a compact Hausdorff space whose Lebesgue covering dimension is ≤ n and A is a closed subset of X, then Ȟ_q(X, A) = 0 for all q > n.*

(its proof, same page, begins: "The condition on the Lebesgue covering dimension implies that every finite open covering 𝒰 of X has a (finite) refinement such that each subcollection of n + 2 open subsets from 𝒰 has an empty intersection.")

> **THEOREM 6.** *If X is a compact Hausdorff space and A ⊂ X is a closed subspace, then there is a canonical mapping φ_∞ from H_∗(X, A) to Ȟ_∗(X, A) (the* singular-Čech comparison map*), where the groups on the left are singular homology groups. If X is a polyhedron with some simplicial* **K** *such that A is a subcomplex with respect to this decomposition, then the singular-Čech comparison map is an isomorphism.*
>
> Before proving this result, we shall use the conclusion to derive the main implications for dimension theory.
>
> **THEOREM 7.** *(i) For all n ≥ 0, the Lebesgue covering dimension of the disk D^n is equal to n.*
>
> *(ii) If (P,* **K***) is a simplicial complex whose geometric definition is equal to n, then the Lebesgue covering dimension of P is also equal to n.*
>
> *(iii) If A ⊂ ℝ^n is a compact subset with a nonempty interior, then the Lebesgue covering dimension of A is equal to n.*
>
> *(iv) If* **Q** *= [0, 1]^∞ is the Cartesian product of countably infinitely many copies of the unit interval (the so-called* Hilbert cube*), then the Lebesgue covering dimension of* **Q** *is equal to ∞.*
>
> **Proof.** We shall take these in order.
>
> Proof of (i). By the discussion at the beginning of this section (or the corresponding discussion in Munkres, *Topology*), we know that the Lebesgue covering dimension of D^n is at most n, so we need to show that it cannot be ≤ (n−1). We shall exclude this by deriving a contradiction from it. If

**p. 8 (continuation):**

> the Lebesgue covering dimension was strictly less than n, then it would follow that Ȟ_n(D^n, A) would vanish for all closed subsets A ⊂ D^n. By Theorem 6 we know that Ȟ_n(D^n, S^{n−1}) ≅ H_n(D^n, S^{n−1}), and since the latter is isomorphic to ℤ it follows from Theorem 5 that the Lebesgue covering dimension cannot be ≤ n − 1. Therefore this dimension must be equal to n.■
>
> Proof of (ii). This follows immediately from (i) and Theorem 50.2 of Munkres, *Topology* (see page 307 for details).■
>
> Proof of (iii). By the discussion at the beginning of this section we know that the Lebesgue covering dimension of A is ≤ n. Since A has a nonempty interior, it follows that A contains a closed subset which is homeomorphic to D^n. This means that the Lebesgue covering dimension of A must be at least as large as the Lebesgue covering dimension of D^n, which is n. Combining these observations, we conclude that the Lebesgue covering dimension of A is equal to n.■
>
> Proof of (iv). Let H⟨n⟩ ⊂ **Q** be the subset of all points whose coordinates satisfy x_k = 0 for k ≥ n + 1. Then it follows that H⟨n⟩ is a closed subset of **Q** which is homeomorphic to D^n, and therefore we have n = dim H⟨n⟩ ≤ dim **Q** for all n.■

The proof of Theorem 6 occupies pp. 8–9 and closes on p. 9 with: "As noted before, this concludes the proof that the Lebesgue covering dimension of D^n is equal to n."

**p. 9:**

> **THEOREM 8.** *For every n ≥ 0 the Lebesgue covering dimension of ℝ^n is equal to n.*
>
> **Sketch of proof.** The exercises at the end of Section 50 in Munkres, *Topology* (see pages 315–316) provide machinery for extending results on covering dimensions to "reasonable" noncompact spaces. In particular, Exercise 8 shows that the Lebesgue covering dimension of ℝ^n is at most n. Since the dimension of the closed subspace D^n is equal to n, it follows that the Lebesgue covering dimension of ℝ^n is at least n, and therefore it must be exactly n.■

**A reading note that a citing text must carry (found while transcribing, not recalled).** The p. 2 definition as printed is off by one against the rest of the notes: it declares "order at most n" to mean that every (n+1)-fold intersection U_{α(0)} ∩ ⋯ ∩ U_{α(n)} is empty, and "dim ≤ n" to mean a refinement of order ≤ n exists. But the proofs use the standard Munkres convention throughout: Lemma 1 (p. 3) equates "(n+2) distinct open stars have empty intersection" with "order at most (n+1)" and concludes "dimension … at most n"; the proof of Theorem 5 (p. 7) reads "dim ≤ n" as "each subcollection of n + 2 open subsets … has an empty intersection". Under the printed p. 2 wording, Theorem 7(i) would say dim D^n = n − 1, which its own proof contradicts. So the convention in force in Theorems 5–8 is: **dim X ≤ n iff every open cover has an open refinement in which every n+2 distinct members have empty intersection (every point lies in at most n+1 members)** — exactly the adjudication's §3.10 "finite open refinement of order ≤ k+1". The citing sentence should say "in the convention of Schultz's proofs (Munkres §50)". (Whether Schultz's definition on p. 2 restricts to finite open covers is not stated; for the compact spaces of Theorem 7 every open cover has a finite subcover, so the finite-cover and all-cover definitions agree, and the adjudication's (D2a) is for finite covers of the closed cell K_n ⊆ S — no gap.)

### 2.2 Hurewicz–Wallman, *Dimension Theory*, revised edition 1948 (Copyright 1941, Princeton University Press) — read from the archive.org/DLI scan on 2026-09-02; scan since deleted (copyright renewed, §1.1); NOT on disk

Page numbers are the printed ones.

**p. 9 (Chapter I, §6 "Remarks"):**

> Throughout this book *all spaces are separable metric*, unless the contrary is explicitly stated. This limitation is made because there arise grave difficulties in extending dimension-theory to more general spaces. A brief discussion of some of these difficulties is given in the Appendix.

**p. 24 (Chapter III, §1):**

> **Definition III 1.** The empty set and only the empty set has *dimension* −1.
> A space X has *dimension* ≤ n (n ≥ 0) *at a point* p if p has arbitrarily small neighborhoods whose boundaries have dimension ≤ n − 1.
> X has *dimension* ≤ n, dim X ≤ n, if X has dimension ≤ n at each of its points.
> X has *dimension* n *at a point* p if it is true that X has dimension ≤ n at p and it is false that X has dimension ≤ n − 1 at p.
> X has *dimension* n if dim X ≤ n is true and dim X ≤ n − 1 is false.
> X has *dimension* ∞ if dim X ≤ n is false for each n.

**p. 26 (Chapter III, §1):**

> **Theorem III 1.** *A subspace of a space of dimension ≤ n has dimension ≤ n.*
>
> PROOF. (By induction.) The statement is obvious for n = −1. Assume it now for n − 1. Let X be a space of dimension ≤ n, X′ a subspace of X, and p any point of X′. Let U′ be a neighborhood in X′ of p. Then there exists a neighborhood U in X of p such that U′ = UX′. Because dim X ≤ n there exists a set V, open in X, and satisfying p ε V ⊂ U, dim bdry V ≤ n − 1. Let V′ = VX′. Then V′ is open in X′, p ε V′ ⊂ U′. Let B be the boundary of V in X, and B′ the boundary* of V′ in X′. Then, as one can easily see, B′ is contained in BX′. By the hypothesis of the induction, dim B′ ≤ n − 1, q.e.d.

**p. 40 (Chapter IV, §1):**

> D) Let I_n be a cube in E_n, e.g. the set of points each of whose n coordinates x_1, ⋯, x_n satisfies |x_i| ≤ 1. Let C_i be the face of I_n determined by the equation x_i = 1 and C′_i the face opposite. Let B_i be a closed set separating C_i and C′_i. Then B_1 ⋯ B_n ≠ 0.

**p. 41 (Chapter IV, §2 "Dimension of E_n"):**

> We now prove the most important results of this chapter.
>
> A) dim I_n ≥ n.
>
> PROOF. Suppose, to the contrary that dim I_n ≤ n − 1. Then by III 5 C) there would exist n closed subsets B_i of I_n, each separating a different pair of opposite faces with B_1B_2 ⋯ B_n = 0. But this contradicts 1 D).
>
> B) dim E_n ≥ n.
>
> PROOF. For I_n is a subset of E_n.
>
> **Theorem IV 1.** *Euclidean n-space has dimension n.**
>
> \* Proved first by Brouwer: Über den natürlichen Dimensionsbegriff, *Jour. f. Math.* 142 (1913), pp. 146–152. Brouwer as well as Menger and Urysohn base their proofs on Lebesgue's covering theorem (see below).

**p. 42:**

> PROOF. Combine B) with Example III 4.
>
> COROLLARY. *The Euclidean n-cube has dimension n.*
>
> PROOF. Combine A) with the fact that I_n is a subset of E_n.

(Example III 4, p. 25: "The Euclidean n-space E_n has dimension ≤ n. The inductive proof of this is left to the reader. The proof that the dimension of E_n is precisely n is by no means trivial, however, and will be the main concern of Chapter IV." — from the text layer of the scan.)

> **3. Lebesgue's covering theorem**
>
> **Theorem IV 2. Lebesgue's Covering Theorem.** *Suppose an n-dimensional cube is the sum of a finite number of closed sets, none of which contains points of two opposite faces. Then at least n + 1 of these closed sets have a common point.*
>
> Although this theorem is not used in this book we prove it in view of its great historical importance (see section 3 of Chapter I). The proof is based essentially on Proposition 1 D).

**p. 52 (Chapter V, §1):**

> **Definition V 1.** By a *covering*† of a space X we mean a *finite* collection U_1, ⋯, U_r of *open* sets of X whose sum is X. The *order* of a covering is the largest integer n such that there are n + 1 members of the covering which have a non-empty intersection. If X is bounded the *mesh* of a covering is the largest of the diameters‡ of the U_i.

**p. 67 (Chapter V, §8):**

> **Theorem V 8. Covering Theorem.** *A space has dimension ≤ n if and only if every covering has a refinement of order ≤ n.*
>
> PROOF. This is a combination of Theorems V 1 and V 7.
>
> COROLLARY. **Covering Theorem for Compact Spaces.** *A compact space has dimension ≤ n if and only if it has coverings of arbitrarily small mesh and order ≤ n.*

Reading notes. (a) Hurewicz–Wallman's "dimension" is the inductive (Menger–Urysohn) dimension of Definition III 1; Theorem V 8 identifies it, for the separable metric spaces the book treats, with the finite-open-cover covering dimension of Definition V 1. Their "order ≤ n" (no n+2 members meet) is the adjudication's "order ≤ n+1" (members counted), the same convention as Schultz's proofs. (b) Their I_n is [−1, 1]^n; the Corollary on p. 42 is the classical "dim [0,1]^n = n" (the two cubes are homeomorphic by a coordinatewise affine map). (c) Theorem III 1 is monotonicity for *arbitrary* subspaces of separable metric spaces — stronger than what (b2) needs.

### 2.3 Karasev 2013 — [r3s-26], on disk

Page numbers are the arXiv v1 printed ones (= PDF pages).

**p. 1 (Introduction):**

> In the theory of covering dimension there are lemmas showing that the Euclidean space ℝ^n has dimension at least n. One result is attributed to Lebesgue: If a unit cube [0, 1]^n is covered by compact sets so that no point is covered by more than n of them, then one of the sets must intersect two opposite facets of the cube.

**p. 3 (§4 "Lebesgues's theorem" [sic]):**

> We now see that the Lebesgue theorem has a very simple proof in the toric approach:
>
> **Theorem 4.1.** *Let the unit cube Q^n be covered by a family of closed sets X_i with covering multiplicity at most n. Then some X_i touches two opposite facets of Q^n.*
>
> *Proof.* Consider the moment map π : M → Q^n, where M = (ℂP^1)^n and the corresponding sets Y_i = π^{−1}(X). …

(The proof runs to the top of p. 4 and rests on Lemma 3.2 with Lemma 3.3 "(Palais, 1966)" — an open covering of a paracompact space of multiplicity ≤ k refines to a k-colorable open covering — and the Lusternik–Schnirelmann cup-length argument; "closed sets … by the standard technique we may pass to neighborhoods without increasing the covering multiplicity", p. 3.)

**p. 4, generalizations (for the record):**

> **Theorem 4.2.** *Let {X_i} be a family of subsets of the unit cube Q^n such that none of X_i touches a pair of opposite facets of Q^n. If the covering multiplicity of {X_i} is at most k then there exists a connected component Z of the complement Q^n ∖ ⋃_i X_i and a k-dimensional coordinate subspace L ⊆ ℝ^n such that Z intersects every k-face of Q^n parallel to L.*
>
> **Theorem 4.3.** *Let the unit cube Q^n be covered by a family of closed sets {X_i}_{i=1}^n. Then some connected component of X_i intersects both the corresponding opposite facets F_i^+ and F_i^−.*

Reading notes. (a) Karasev's "covering multiplicity at most n" = no point in more than n of the sets = Hurewicz–Wallman's "order ≤ n−1" = "every n+1 members have empty intersection". Theorem 4.1 is Hurewicz–Wallman's Theorem IV 2 (p. 42) in contrapositive form (their "at least n+1 of these closed sets have a common point" ⇔ multiplicity ≥ n+1). (b) Theorem 4.1 gives the lower bound dim [0,1]^n ≥ n as follows, and this is the only step a citing text must supply: the finite open cover of [0,1]^n by the 2n open sets {x_i < 2/3}, {x_i > 1/3} has no member meeting two opposite facets, and a shrinking of any finite open refinement to a closed cover (normality) keeps that property and does not increase multiplicity; so no refinement has multiplicity ≤ n, i.e. dim [0,1]^n ≥ n. Schultz's Theorem 7 (§2.1) makes this step unnecessary; [r3s-26] is on disk as the refereed free primary for the Lebesgue statement itself.

---

## 3. What the two on-disk sources establish, exactly

For (b2) the adjudication needs, for each n, **(D1)** dim [0,1]^n = n in the finite-open-cover covering dimension, and it re-derives **(D2a)** closed-subspace monotonicity itself (§3.10).

- **(D1) from [r3s-25]:** Theorem 7(iii) applied to A = [0,1]^n ⊂ ℝ^n (compact, nonempty interior) gives dim [0,1]^n = n outright; Theorem 7(i) gives it for D^n. Both proofs are on the page: the upper bound by Lemma 1 (Lebesgue number + barycentric subdivision, p. 3) with Munkres Thm 50.1 for passing from the hypercube to its closed subsets; the lower bound by Theorems 5 and 6 (Čech homology, pp. 7–9) plus H_n(D^n, S^{n−1}) ≅ ℤ. The step "A contains a closed subset homeomorphic to D^n" in the proof of (iii) is a closed ball inside the interior; for A = [0,1]^n one may instead apply (i) directly, since [0,1]^n is homeomorphic to D^n (a convex body with nonempty interior; radial map) — or avoid D^n entirely by taking K_n ≅ [0,1]^n ≅ [−M, M]^n and using Lemma 1 for the upper bound and (iii) for the lower.
- **(D1), the classical form, from [r3s-26]:** Lebesgue's theorem in the closed-cover form (addendum). It yields dim [0,1]^n ≥ n once one shrinks a finite open cover of order ≤ n to a closed cover of order ≤ n (a standard normality argument the adjudication would have to re-derive if it chose this route). Schultz's route needs no such step; [r3s-26] is kept as the refereed primary for the Lebesgue statement itself.
- **(D2a):** re-derived in the adjudication §3.10; classical sources in §5.

---

## 4. Recommended citation text for probe A, Theorem B(b), part (b2)

Replace the [RU] clause in (b2) by:

> **(b2)** Consequently dim S = ∞ for the covering dimension defined by finite open covers, and S admits no continuous injection into any metrizable space of finite covering dimension (in particular into any finite-dimensional compact metrizable lamination). The one external input is **dim [0,1]^n = n** for the finite-open-cover covering dimension (Lebesgue; Brouwer 1913), cited to a source on disk: R. Schultz, *Notes on Topological Dimension Theory* (UC Riverside, 2012), Theorem 7 (i) and (iii), p. 7, proofs pp. 3 and 7–9 — [r3s-25], `fetched-r3/r3s-25-schultz-2012-notes-topological-dimension-theory-ucr-SESSION14-FETCH.pdf`; convention as in Schultz's proofs (Munkres §50): dim X ≤ n iff every open cover has an open refinement in which every point lies in at most n+1 members (the printed definition on Schultz p. 2 is off by one; see `results/c3-r/referee-s14/dim-cube-source.md` §2.1). The classical statement is Hurewicz–Wallman, *Dimension Theory* (Princeton 1941; rev. ed. 1948), Ch. IV §2, Corollary to Theorem IV 1, p. 42 ("The Euclidean n-cube has dimension n"), with Theorem V 8, p. 67, identifying the inductive dimension there with the finite-open-cover covering dimension for separable metric spaces — read from a scan in Session 14 but not held on disk (copyright renewed 1969, R468228; see the source record §1.1). Lebesgue's covering theorem in its closed-cover form is R. Karasev, *Covering dimension using toric varieties*, Topology Appl. 177 (2014) 59–65, arXiv:1307.3437 — [r3s-26]. Closed-subspace monotonicity of finite-open-cover dimension is elementary and re-derived in §3.10 (D2a).

and drop the "[RU]" label from the (b2) line of the adjudication's §7 summary, replacing "[RU-conditional on dim [0,1]^n = n]" with "on disk: [r3s-25] Thm 7(i),(iii)".

The adjudication's §3.10 sentence "The note's two routes (…) are the standard [RU] statements (Hurewicz–Wallman III 1, IV 1, V 8; Engelking 3.1.4 — all [RU])" should be amended: Hurewicz–Wallman III 1, IV 1 (with its Corollary), IV 2, and V 8 are now **verified statements with page numbers (pp. 26, 41–42, 67) though not on disk**; "Engelking 3.1.4" stays unverified and should be dropped or left explicitly [RU].

---

## 5. The monotonicity statement — sources

What (b2) needs is only: for F closed in Z, dim F ≤ dim Z (finite-open-cover dimension, any space). The adjudication proves this in four lines (§3.10, D2a), and that re-derivation is the operative source. The classical statements, for the record:

- **Hurewicz–Wallman, Theorem III 1, p. 26** (verbatim in §2.2): "A subspace of a space of dimension ≤ n has dimension ≤ n" — for *all* subspaces, in the inductive dimension, for separable metric spaces; transfers to the covering dimension by Theorem V 8, p. 67. Verified from the page image; not on disk (§1.1).
- **Munkres, *Topology*, 2nd ed., Theorem 50.1, pp. 306–307** — closed subspaces, as cited on Schultz p. 3 ("By Theorem 50.1 on pages 306–307 of Munkres, *Topology*, it is enough to show that the hypercube has dimension at most n") and used on Schultz p. 8 (proof of (iii)) and p. 9 (Theorem 8). Munkres is not free and not on disk; the statement is known here only through Schultz's citation, so it is **not** to be quoted as Munkres' wording.
- **Engelking 1978:** the tasking's "monotonicity theorems in Ch. 1/3" could not be verified (no legitimate copy); not cited.

---

## 6. SPONSOR-FETCH — the two classical books, for purchase or library loan

Neither is legitimately free. Bibliographic data below is what the pages and records consulted actually state.

```
SPONSOR-FETCH 1
  Authors:    Witold Hurewicz and Henry Wallman
  Title:      Dimension Theory
  Series:     Princeton Mathematical Series, vol. 4 (PMS-4)
  Publisher:  Princeton University Press, Princeton
  Year:       1941; revised edition 1948 (copyright page: "Copyright, 1941, by
              Princeton University Press / Revised edition, 1948")
  Copyright:  original registration A160903 (22 Dec 1941); RENEWED R468228
              (8 Sep 1969), claimant Henry Wallman (A) — Catalog of Copyright
              Entries, 3rd ser., vol. 23, pt. 1, no. 2, p. 2817 (NYPL transcription)
  In print:   Princeton Legacy Library paperback ISBN 9780691627748;
              hardcover ISBN 9780691653686; e-book ISBN 9781400875665,
              DOI 10.1515/9781400875665; JSTOR j.ctt183pk8v
  Needed:     Ch. III §1 Definition III 1 (p. 24) and Theorem III 1 (p. 26);
              Ch. IV §2 Prop. A) "dim I_n ≥ n", Theorem IV 1 and its COROLLARY
              "The Euclidean n-cube has dimension n" (pp. 41–42);
              Ch. IV §3 Theorem IV 2, Lebesgue's Covering Theorem (p. 42);
              Ch. V §1 Definition V 1 (p. 52) and §8 Theorem V 8, Covering
              Theorem (p. 67).  Page numbers are those of the 1948 revised
              edition; the Legacy Library reprint is believed to keep them
              (unverified).

SPONSOR-FETCH 2
  Author:     Ryszard Engelking
  Title:      Dimension Theory (translation of "Teoria wymiaru")
  Publisher:  PWN — Polish Scientific Publishers, Warszawa, and North-Holland
              Publishing Co., Amsterdam / New York
  Year:       1978
  Extent:     x + 314 pp.; errata slip; bibliography pp. 289–308
  ISBN:       0-444-85176-3 (archive.org record); LCCN 78-12442; OCLC 4195058
  Needed:     the theorem stating dim I^n = n (tasking's "1.8.2" — UNVERIFIED),
              and the subspace/closed-subspace monotonicity theorems for the
              covering dimension (tasking's "3.1.4" — UNVERIFIED).
  Note:       archive.org holds a lending-only copy (dimensiontheory0000rysz);
              a scan sits on the late A. Ranicki's Edinburgh page with no
              rights statement — not used.
  Alternative: R. Engelking, Theory of Dimensions, Finite and Infinite,
              Sigma Series in Pure Mathematics, Heldermann, 1995 (HathiTrust
              Record 003031306; access level not readable through the bot screen).
```

---

## 7. Files touched

- Added: `fetched-r3/r3s-25-schultz-2012-notes-topological-dimension-theory-ucr-SESSION14-FETCH.pdf` (18 pp., 169,151 bytes, SHA-256 `8b6b3e50…50d2fed`).
- Added: `fetched-r3/r3s-26-karasev-2013-covering-dimension-toric-varieties-arxiv-1307.3437v1-SESSION14-FETCH.pdf` (6 pp., SHA-256 `16f1de62…95a6c2ed`).
- Added: this file.
- Not added, deliberately: the archive.org/DLI scan of Hurewicz–Wallman (copyright renewed; deleted from the scratchpad after reading); the Ranicki-hosted Engelking scan (never downloaded); Freire's UTK notes (upper bounds only).
- Not changed: `results/c3-r/probe-9.3-a.md` and `A-thmB-adjudication.md` — the citation text in §4 is ready to be installed by the adjudicating agent.
