# Zoo stream `zoo-s27`, Session 27 — READER report (Opus 5, independent second model, standing order 7)

**Opened Fri Sep 25 20:49:47 IST 2026 (machine clock, `date`).** IN PROGRESS — sections land one at a time; the verdict table is written last.
**Brief:** `results/zoo-s27/BRIEF.md` (`cf239a80…`, recomputed, matches), section "The reader (Opus 5)". FORMAT precedent `results/zoo-s25/zoo-entries-read-O.md`.
**Writer's deliverables checked:** `results/zoo-s27/zoo-entries-proposed.md` `38986446…` (recomputed, matches); `scripts/zoo-insert-s27.py`; `results/zoo-s27/SHARED.md`; `results/zoo-s27/dryrun-BARRIER-ZOO.md`; the writer's `prior-art/` folder and finding 7 were NOT opened until §4 (my own search) was on disk.

---

## §1 Computations (my own scripts, `results/zoo-s27/verify-O/`)

- **`zeros200_O.py` → `zeros200_O_run.log`** (mpmath 1.3.0, dps 30; written without opening `results/zoo-s26/verify/*`): at the first 200 zeros, c_k = Re[1/(ρ_kζ′(ρ_k))] is **positive at 96 and negative at 104**, **108 sign changes in 199 steps**; the residue of 1/ξ, 1/ξ′(ρ) with ξ′(ρ) = ½ρ(ρ−1)π^{−ρ/2}Γ(ρ/2)ζ′(ρ), has max | |arg| − π/2 | = **5.96·10⁻²⁹** and Im alternates at **199 of 199** consecutive pairs (Im < 0 at k = 1); arg(1/ζ′(ρ))/π ∈ **[−0.506529, +0.506296]**, Re(1/ζ′(ρ)) < 0 at **k = 127, 136, 196**. Every number the blocks `i5`/`iv4` and note §3.2 quote is reproduced to the printed digit.
- **`witt_diag_O.py` → `witt_diag_O_run.log`** (see §3 for the derivation it checks): Part A, the Z-basis v_d = (d·[d | n])_n of the truncated ghost lattice, 0 congruence violations at N = 120; Part A2, gcd{d : d | n, d > 1} = e^{Λ(n)} at every 2 ≤ n ≤ 20 000 (0 mismatches); Part B, 4 000 random big-Witt vectors in Witt coordinates, ghost map from the definition w_n = Σ_{d|n} d·x_d^{n/d}: (1.10) holds for all 4 000, and gcd(w₁ − w_n) over the samples equals e^{Λ(n)} at every n = 2 … 40 (11 → 11, 13 → 13).

## §4 Prior art — MY OWN search, written before opening the writer's finding 7, block `rb` or `prior-art/` (on disk Fri Sep 25 20:52:21 IST 2026)

**Claim searched:** "on Borger's W*(Spec Z) the ghost components Γ_n meet Γ₁ in arithmetic degree Λ(n)" or any equivalent (the ghost components of W(Z) pairwise intersecting in Spec F_p; I_n = pZ / Z).

**Opened (my own fetches, curl from arXiv, saved to `results/zoo-s27/verify-O/pa/` with `pdftotext -layout` text beside each):** Borger 0801.1691 (SHA-256 d8d7c8f6…, byte-identical to `sources/O-arxiv-0801.1691.pdf`), 0906.3146 (acf748e4…, byte-identical to `sources/O-arxiv-0906.3146.pdf`), 1006.0092 (3b799398…) — full text grepped for diagonal / Mangoldt / intersect / ghost component / log p / degree / glu / coequal / copies; Manin 0809.1564 (Cyclotomy and analytic geometry over F₁); Connes–Consani 1103.4672 (On the arithmetic of the BC-system) and 1502.05580 (Geometry of the arithmetic site); Jeffries 2311.13551 ("Differentiating by prime numbers", surfaced by the web search); López Peña–Lorscheid 0909.0069 (Mapping F₁-land). Web searches (WebSearch, six queries): "Witt vectors ghost components diagonal intersection von Mangoldt Spec Z"; "Spec Z F_1 Witt vectors arithmetic degree log p ghost diagonal Borger"; "Borger Frobenius lifts diagonal intersection absolute Spec Z × Spec Z Witt space degree"; "von Mangoldt Witt vectors ghost intersection Spec Z F_un"; "W(Z) big Witt copies of Spec Z glued ghost components F_p intersection"; "Connes Consani lambda-rings Witt Spec Z over F_1 arithmetic surface Borger ghost"; plus two on Buium / Le Bruyn / Borger–Saha. (arXiv has no full-text search endpoint; Google Scholar was not used.) No page failed to fetch, so Firecrawl was not needed.

**What is in print (read at the page, as images):**
- **Borger, "The basic geometry of Witt vectors, I: The affine case" (arXiv:0801.1691), p. 5 (PDF page 5), Figure 1 caption:** "As a topological space, Spec W₁(A) (traditionally denoted W₂(A)) is two copies of Spec A glued along Spec A/pA. This is also true as schemes if we assume that A is p-torsion free and we glue transversely and with a Frobenius twist, as indicated. There is a similar description of Spec W_n(A) as Spec W_{n−1}(A) glued with Spec A along Spec A/pⁿA."
- **Borger, "The basic geometry of Witt vectors, II: Spaces" (arXiv:1006.0092), p. 5 (PDF page 5):** for X flat over Z locally at p, "W₁*(X) is the coequalizer in the category of algebraic spaces of the two maps X₀ ⇉ X ∐ X" (i₁∘F, i₂; X₀ the fiber mod p), and "For general n, the space W_n*(X) can be constructed by gluing n+1 copies of X together in a similar but more complicated way along their fibers modulo p, …, pⁿ. See 17.3."

For X = Spec Z these print the **n = p case** of the claim as geometry: the two ghost components of the p-typical W₁*(Spec Z) are two copies of Spec Z meeting exactly in Spec F_p, i.e. in arithmetic degree log #F_p = log p = Λ(p). They do NOT print (i) the big-Witt pairwise statement for general n (Γ₁ ∩ Γ_{p^k} = Spec F_p, of degree log p, not the Spec Z/p^k of the "glued along Spec A/pⁿA" chain, which is the intersection of the NEW copy with the whole previous union, not with Γ₁); (ii) Γ₁ ∩ Γ_n = ∅ for n not a prime power; (iii) the words "degree", "Λ(n)" or "von Mangoldt" anywhere in the three Borger papers (grep: "degree" occurs only for field degrees / Frobenius degree, 0906.3146 lines 533–560; "Mangoldt" nowhere).
- **Nearest object with Λ(n) in print, different mechanism:** Connes–Consani 1103.4672, p. 51 (PDF page 52), (205)–(206): N(u) = (d/du)φ(u) + κ(u), φ(u) = Σ_{n<u} nΛ(n), and "The value log(p) coming from the von-Mangoldt function Λ(n) corresponds to the length of the orbit in the mapping torus" — Λ(n) as a periodic-orbit length in the adèle class space, not as an intersection degree on W*(Spec Z).
- Manin 0809.1564, 1502.05580, 2311.13551, 0909.0069: no sentence on ghost-component intersections or Λ(n) (grep; 1502.05580's "diagonal" is the diagonal of the Connes–Consani square, not of a Witt space).

**My outcome:** the Λ(n) statement (all n ≥ 2, big Witt vectors, as an arithmetic degree) is **NOT FOUND in print**; its **n = p (p-typical length-1) case IS in print as geometry** — Borger 0801.1691 p. 5 Figure 1 and 1006.0092 p. 5 (two copies of Spec Z glued transversely along Spec F_p) — without the words "degree" or "Λ". The rider should cite those two pages as the nearest published object (10(n)) and as the printed form of the p-case, and keep the dual-model novelty label only for the general-n / von Mangoldt packaging.

## §2 The D3 note's packaging sentence — CLOSES

**Read:** note §0 (lines 7–19), §1 (21–43), §2 (44–71), §3 (73–105), §4 (107–124), §7 (142–148); blocks `i5`, `iv4` whole (byte-identical to the s26 blocks — checked by my own comparison and by the script). **At the page, as images this session:** Odlyzko–te Riele 1985 pp. 139, 141, 142 (PDF pages 3, 5, 6): p. 139 prints "lim sup M(x)x^{−1/2} > 1.06, lim inf M(x)x^{−1/2} < −1.009" and the "does not imply anything about the possible falsity of the Riemann hypothesis" paragraph; p. 141 prints hypotheses i)–iii) and (2.3) with |ρζ′(ρ)| in bars (the note's recorded print slip is real); p. 142 prints (2.4)–(2.8) without bars, m(y) = h(y) + O(min(1, e^{−y/2})). Wintner 1944 p. 269 (PDF page 3): (11), (12) and Theorem (I) as quoted. Conrey–Ghosh–Gonek 1998 pp. 499–500 (PDF pages 3–4): (2.1)–(2.8) as `iv4` quotes. **At the line:** `BARRIER-ZOO.md` 84, 86, 108–110, 161; `check-O.md` 308; `adjudication-B1.json` 12; B1 94–95; B3 89–90. **Computed:** §1 above — 96 / 104 / 108 / 199 / 5.96·10⁻²⁹ / [−0.506529, +0.506296] / n = 127, 136, 196 all reproduced by my own script.

**Clause by clause.** (1) The consumed axiom set {inverse-series abscissa ≤ 1, FE, RvM} holds in I.2 (Euler product over Beurling primes, absolutely convergent inverse for σ > 1), in I.5 with FE as the added input, and in I.8 (ζ_K has an Euler product) with RH or GRH false; so any separation claim resting on that set is S1-nil — correct, and it is I.8's KILLS (ii) transported, as the note says. (2) The lemma of §2.1 is correct (P_X = {n ≤ X : Λ(n) = log n}; Λ = μ ∗ log on divisors ≤ X), so the μ-band is a function of the Λ-band; the note's own correction (§2.3: IV.4 prices the ground by its open question, not by its KILLS letter; IV.1's expression fails by support) is what `iv4` carries, and the §0 phrase "which IV.4 kills" does not enter the zoo. (3) Ξ real and even ⇒ ξ′(ρ) = −iΞ′(γ) ⇒ Res 1/ξ purely imaginary and alternating; Res 1/ζ and the Mertens weight are the same alternation rotated by arg H(ρ) and arg(1/ρ); with ĝ(γ) = |h_f(γ)|² ≥ 0 the on-line summand has the residue's sign, which is not fixed — so a negative μ-side value certifies nothing. The derivation is complete and the computation agrees. **The implication** "(1) ∧ (2) ∧ (3) ⇒ no S1-positive separation instrument and no sign test on Möbius-side first-order data in the M6 normalization" follows, with its two scope words doing real work: "first-order data" (the datum with its consumed axioms — an instrument that consumes a further input is a different datum, which is I.8's EXECUTABLE TEST) and "in the M6 normalization" (g = f ⋆ f̃; a test weighting chosen from the zeros themselves is not a first-order sum rule). **Novelty:** my own search (one web query on μ-side explicit-formula positivity criteria, plus the Odlyzko–te Riele p. 143 Ingham-kernel form the note names) finds no printed statement of the packaging; the residue non-sign itself is classical and in print (pp. 139, 142), which the blocks already say. **Verdict: CLOSES.** No amended sentence. The orchestrator's label flip needs one mechanical precision (amendments A1, A2 in §6): the blocks end "… is `[novelty: single-check]` until this stream's Opus reader has read the note."; flipping only the label would leave "is `[dual-model check …]` until this stream's Opus reader has read the note", which is false once the reader has read it, so the flip replaces the label AND drops the "until" clause, and the script's `LABEL_OLD` / `LABEL_NEW_RE` widen by exactly that clause (tested, §8).

**One wording precision recorded, not amended (byte-identity lock):** `i5` says "the 1/ξ residues are ±π/2 to 6·10⁻²⁹", meaning their arguments are ±π/2 to 6·10⁻²⁹; `iv4` has the same phrase. The reading is unambiguous in context and the numbers are exact; it is not worth breaking the byte-identity for.

## §3 The Witt computation, as the THIRD model — CLOSES

**My derivation (different from scout O's constant-shift argument and from the writer's chained-congruence-plus-witness argument).** Let L_N ⊂ Z^N be the set of ghost vectors on the divisor-closed index set {1, …, N}, i.e. the vectors satisfying Borger's (1.10) congruences a_j ≡ a_{pj} (mod p^{1+ord_p(j)}) for pj ≤ N (0801.1691 p. 10, read at the page; W^fl(Z) = W(Z), the classical big Witt vectors, by §1.15, p. 12, read at the page). (i) For each d ≤ N the vector v_d := (d·[d | n])_{n ≤ N} lies in L_N: if d | j then d | pj and the two entries agree; if d ∤ j but d | pj then d = p·d′ with d′ | j and ord_p(d) = ord_p(j) + 1, so p^{1+ord_p(j)} divides the difference d. (ii) The v_d are lower-triangular with diagonal d, so they span a sublattice of index N!. (iii) L_N itself has index N!: given a₁, …, a_{n−1}, the congruences that involve a_n fix it modulo p^{ord_p(n)} for each p | n, i.e. modulo n by CRT (one class). Hence L_N = ⊕ Z·v_d. Then I_n = {a₁ − a_n} = the ideal generated by (v_d)₁ − (v_d)_n = [d = 1]·1 − d[d | n] over d ≤ n, i.e. by {d : d | n, d > 1}, so **I_n = gcd{d : d | n, d > 1}·Z = pZ if n = p^k and Z otherwise**, for every n ≥ 2, and log #(Z/I_n) = Λ(n). With the constant vector (1, 1, …) = v₁ ∈ L_N, a ↦ a − a_n·1 shows I_n = {a₁ : a_n = 0}, so Z/I_n = Z ⊗_{W(Z)} Z along Γ₁, Γ_n — the scheme-theoretic intersection, as the rider defines it.

**My script** `results/zoo-s27/verify-O/witt_diag_O.py` → `witt_diag_O_run.log` (§1): Part A checks (i) at N = 120; A2 checks the gcd formula against Λ(n) for 2 ≤ n ≤ 20 000; Part B is independent of (1.10): 4 000 random big-Witt vectors in Witt coordinates, ghost map computed from its definition, (1.10) verified on every sample and gcd(w₁ − w_n) = e^{Λ(n)} at every n ≤ 40. **At n = 11 and 13 my run gives I_11 = 11Z and I_13 = 13Z** (Part A2 table and Part B). **The orchestrator's logs, read in full:** the N = 12, [−6, 6] run prints the primary gcd = Λ(n) at every n ≤ 12 and the auxiliary gcd(a₁ | a_n = 0) = 0 at n = 7, 11; the N = 16, [−4, 4] run prints the primary gcd 0 (deg = inf, MISMATCH) at n = 11, 13 and the auxiliary gcd wrong at n = 5, 7, 10, 11, 13, 14, 15 — exactly as the writer's finding 6 and NOTE (1) say, and the brief's "confounded at n = 7, 11, 15" merges the two runs. Both are box artifacts (a box of side 8 cannot hold a difference of 11). **The hand proofs — the writer's and mine — settle every n; the box numbers are not needed and are not evidence at n = 11, 13.** Verdict: **CLOSES**; the rider's computation label gains the third model (amendment A10).

## §5 Prior art — reconciliation with the writer's finding 7 (read after §4 was on disk)

The writer's search (finding 7; `prior-art/` — 10 PDFs, the nLab, six web searches) and mine agree on the core: **the statement deg(Γ₁ ∩ Γ_n) = Λ(n) for every n ≥ 2 — the big-Witt, all-n, von Mangoldt form — is NOT FOUND in print by either model.** They differ on one point, which I adjudicate at the page: the writer reports Borger 0801.1691 as having "no intersection of components" and 1006.0092 as "the gluing and the dimension are printed, no intersection number". **At the page (images, this session): 0801.1691 p. 5, Figure 1 caption — "Spec W₁(A) … is two copies of Spec A glued along Spec A/pA. This is also true as schemes if we assume that A is p-torsion free" — and 1006.0092 p. 5 — W₁*(X) the coequalizer of X₀ ⇉ X ∐ X.** For A = Z this IS the case n = p of the claim, stated as geometry: the two ghost components of the p-typical W₁*(Spec Z) are copies of Spec Z meeting exactly in Spec F_p, whose arithmetic degree is log p. What is not printed is the word "degree", the function Λ, the prime-power case p^k with Γ₁ (log p, not the k·log p the "glued along Spec A/pⁿA" chain measures against the whole previous union), and the empty intersection at composite non-prime-powers. **Adjudicated outcome:** `[printed: Borger 0801.1691 p. 5, Fig. 1; 1006.0092 p. 5 — the case n = p]` for the prime case, and `[novelty: dual-model check, 2026-09-25: the writer's finding 7 and the Opus reader's §4]` for the all-n von Mangoldt statement. The nearest published object (10(n)) becomes Borger's own Figure 1 (closer than Smirnov's deg (p) = log p or Connes–Consani's orbit lengths, which the writer names and which stay as further near objects). Stop line (3) of the brief fires only in part (the p-case is printed; the all-n statement is not), so the rider cites Figure 1 at the page and keeps the computation — amendment A15. The writer's other page quotations I checked at the page and they are exact: Durov 0704.2030 p. 63 (CH¹(Spec Ẑ) = log Q*₊ = Pic), Le Bruyn 1304.6532 p. 2 ("the degree of (p) should be log(p)", attributed there to Kapranov and Smirnov), Connes–Consani 1502.05580 p. 16 ("we are simply considering an intersection number"; (15) Σ log p g(p^m)), 1103.4672 p. 51 (the "length of the orbit in the mapping torus" sentence — which I also found independently).

## §6 The EXACT amendments (17), per block — the orchestrator applies each verbatim to `results/zoo-s27/zoo-entries-proposed.md` before insertion

Each amendment replaces the exact string OLD, which occurs exactly once inside the named block, by NEW. The same seventeen pairs are machine-readable in `results/zoo-s27/verify-O/amendments_O.py` (run it with `CHECK`: it asserts each OLD once in its block, applies all seventeen to the scratch copy `verify-O/proposed-amended-O.md` — SHA-256 `b6ed69072f592755cf594608891fb90a2d591f4db3bc8d1578bc6d6a70be07f3` from the proposed file `38986446…` — and lints the NEW text; it never writes the proposed file). Blocks `verification` and `xref`: no amendment.

**Script change that A1–A2 require (for the orchestrator's `--allow-label-flip` run):** in `scripts/zoo-insert-s27.py` set `LABEL_OLD = "`[novelty: single-check]` until this stream's Opus reader has read the note."` and append `\.` to `LABEL_NEW_RE` (so it matches the new label with its closing period). Tested: a copy with exactly these two edits and `PROPOSED` pointed at the amended scratch copy (`verify-O/zoo-insert-s27-flipsim-O.py`) runs `--allow-label-flip --dry-run` cleanly — both NOTE lines print, +6 lines (649 → 655), 58 entries (8/5/21/19/5), zoo untouched, dry-run SHA-256 `ba6c7aec0ad63cdb703b7108318a77f227361968eb4829cad99dcd23628ef8aa` (`verify-O/dryrun-amended-O.md`); no inserted block carries "single-check" afterwards.

**A1 — block `i5`.** Why: packaging-label flip in `i5` (the stale "until" clause dropped; §2).

OLD:

    no sign test" is `[novelty: single-check]` until this stream's Opus reader has read the note.

NEW:

    no sign test" is `[dual-model check, 2026-09-25: Opus reader, results/zoo-s27/zoo-entries-read-O.md]`.

**A2 — block `iv4`.** Why: packaging-label flip in `iv4` (same).

OLD:

    The packaging sentence is `[novelty: single-check]` until this stream's Opus reader has read the note.

NEW:

    The packaging sentence is `[dual-model check, 2026-09-25: Opus reader, results/zoo-s27/zoo-entries-read-O.md]`.

**A3 — block `ra`.** Why: "every printed doubled object" bounded to the pool the pair actually closed (P1–P9 and the scouts' further candidates) — the rider's own record sentence is bounded the same way.

OLD:

    On every printed doubled object for Spec Z that carries any pairing at all, the pairing is DEFINED

NEW:

    On every printed doubled object for Spec Z named in the pool P1–P9 or by either scout that carries any pairing at all, the pairing is DEFINED

**A4 — block `ra`.** Why: Haran's X is the product of the COMPACTIFIED spec Z (overlined on p. 88 / folio 87, image).

OLD:

    X = spec Z ∏_{F[±1]} spec Z

NEW:

    X = spec Z̄ ∏_{F[±1]} spec Z̄ (the compactified spec Z, overlined on the page)

**A5 — block `ra`.** Why: Banaszak–Uetake's object is an axiomatic theory on an operator's spectrum, not a doubled scheme (p. 1, image); the rider lists it among "doubled objects".

OLD:

    concerning the spectrum of that operator"

NEW:

    concerning the spectrum of that operator" (an axiomatic intersection theory for a Hilbert-space operator, not a scheme; the zeros enter as that operator's spectrum)

**A6 — block `ra`.** Why: packaging label of `ra`: CLOSES.

OLD:

    the packaging of this rider is `[novelty: single-check]` until this stream's Opus reader has read it.

NEW:

    the packaging of this rider is `[dual-model check, 2026-09-25: Opus reader, results/zoo-s27/zoo-entries-read-O.md]`.

**A7 — block `ra_ptr`.** Why: `ra_ptr` said the prime-computable observable IS the Weil test on all three objects; true at the page for Connes–Consani (p. 17 (12)–(13)) and Haran 1991 (p. 259); Haran 2009's (8.7.7) is a zero-side formula and Banaszak–Uetake has no prime side.

OLD:

    — the prime-computable observable IS the classical Weil test with multiplier 1 on every band (s(f, f) = N(f ⋆ f̃) with N the explicit-formula distribution; ⟨f, g⟩ = W(f ∗ g*)),

NEW:

    — the pairing IS the classical Weil test with multiplier 1 on every band wherever it has a prime side (s(f, f) = N(f ⋆ f̃) with N the explicit-formula distribution; ⟨f, g⟩ = W(f ∗ g*)); Haran's (8.7.7) is the zero side of the same explicit formula, and Banaszak–Uetake's theory is axiomatic on an operator's spectrum, with no prime side —

**A8 — block `ra_ptr`.** Why: packaging label of `ra_ptr`: CLOSES.

OLD:

    `[the pair's agreed close; packaging novelty: single-check]` until this stream's Opus reader has read it.

NEW:

    `[the pair's agreed close; packaging dual-model check, 2026-09-25: Opus reader, results/zoo-s27/zoo-entries-read-O.md]`.

**A9 — block `rb`.** Why: (1.10) names W^fl(Z); §1.15 (p. 12, read) identifies it with the classical big Witt vectors W(Z) — both the harvest's and the writer's wording are right, and the rider now says why.

OLD:

    for all j ≥ 1 and all primes p". Write Γ_n

NEW:

    for all j ≥ 1 and all primes p"; since Z is torsion-free this ring is W(Z), the classical big Witt vectors (§1.15, p. 12: with E all the maximal ideals of Z, "W agrees with the classical big Witt vector functor"). Write Γ_n

**A10 — block `rb`.** Why: third model on the computation (§3).

OLD:

    re-verified from (1.10) by this stream's writer]`

NEW:

    re-verified from (1.10) by this stream's writer; re-derived a third time by the Opus reader — the ghost lattice on indices ≤ N has the Z-basis v_d = (d·[d | n])_{n≤N}, d ≤ N (each v_d satisfies (1.10); determinant N! = the index fixed by (1.10)), so I_n = gcd{d : d | n, d > 1}·Z for every n, and 4 000 random big-Witt vectors pushed through the ghost map w_n = Σ_{d|n} d·x_d^{n/d} give gcd(w₁ − w_n) = e^{Λ(n)} at every n ≤ 40, 11 and 13 included (results/zoo-s27/verify-O/witt_diag_O.py and its _run.log)]`

**A11 — block `rb`.** Why: III.21 does not state the Arakelov convention (read at lines 348–357); the convention is cited to the two pages that print it, both opened this session.

OLD:

    the convention under which log p enters every Arakelov intersection number (III.21), not by hand insertion

NEW:

    the convention under which the closed point (p) has arithmetic degree log p (Durov, arXiv:0704.2030, p. 63: CH¹(Spec Ẑ) = log Q*₊ = Pic(Spec Ẑ), deg the "arithmetic degree"; Kapranov–Smirnov's "the degree of (p) should be log(p)", as Le Bruyn, arXiv:1304.6532, p. 2, records it), not by hand insertion

**A12 — block `rb`.** Why: 0801.1691 p. 10 prints the ring, not the gluing; the gluing is printed at 0801.1691 p. 5 (Fig. 1) and 1006.0092 p. 5 (images).

OLD:

    glued at closed points (0801.1691 p. 10; in print as geometry in

NEW:

    glued at closed points (0801.1691 p. 5, Figure 1: "Spec W₁(A) … is two copies of Spec A glued along Spec A/pA. This is also true as schemes if we assume that A is p-torsion free"; 1006.0092 p. 5: W₁*(X) is the coequalizer of X₀ ⇉ X ∐ X, and "the space W_n*(X) can be constructed by gluing n+1 copies of X together … along their fibers modulo p, …, pⁿ"; in print as geometry in

**A13 — block `rb`.** Why: page number for Prop. 16.5 (PDF page 31 = folio 31).

OLD:

    Prop. 16.5(d), W_n* preserves Krull dimension

NEW:

    Prop. 16.5(d), p. 31, W_n* preserves Krull dimension

**A14 — block `rb`.** Why: page number for Thm. 17.3 (folio 39).

OLD:

    and Thm. 17.3, single-ideal case,

NEW:

    and Thm. 17.3, p. 39, single-ideal case,

**A15 — block `rb`.** Why: prior art adjudicated (§5): the case n = p is printed; the all-n statement is dual-model NOT FOUND.

OLD:

    — NOT FOUND in print: `[novelty: single-check — the writer's search, 2026-09-25; the Opus reader's independent search decides the dual-model label]`. Nearest published objects (10(n)): Borger's own hope,

NEW:

    — and independently by the Opus reader (Borger's three papers re-fetched and read in full text; Connes–Consani 1103.4672 and 1502.05580; Manin 0809.1564; López Peña–Lorscheid 0909.0069; Jeffries 2311.13551; web searches — `results/zoo-s27/zoo-entries-read-O.md` §4). The case n = p IS in print, as geometry and without the words "degree" or "Λ": Borger 0801.1691 p. 5, Figure 1 (for A p-torsion free, Spec W₁(A) is two copies of Spec A glued transversely along Spec A/pA — for A = Z the ghost components Γ₁ and Γ_p meet in Spec F_p, of degree log p) and 1006.0092 p. 5 (W₁*(X) the coequalizer of X₀ ⇉ X ∐ X) `[printed: Borger 0801.1691 p. 5, Fig. 1; 1006.0092 p. 5 — the case n = p]`. The statement for every n ≥ 2 on the big Witt vectors — degree log p at every prime power p^k (not the k·log p of the printed chain "Spec W_n(A) as Spec W_{n−1}(A) glued with Spec A along Spec A/pⁿA", which measures the new copy against the whole previous union), empty intersection at every n with two distinct prime factors, i.e. deg(Γ₁ ∩ Γ_n) = Λ(n) — is NOT FOUND in print by either search: `[novelty: dual-model check, 2026-09-25: the writer's finding 7 and the Opus reader's §4, results/zoo-s27/zoo-entries-read-O.md]`. Nearest published objects (10(n)): Borger 0801.1691 p. 5, Figure 1 and 1006.0092 p. 5 (the case n = p, above); Borger's own hope,

**A16 — block `rb`.** Why: the equation S ×_{F₁^S} S = W_S*(S) is not printed on pp. 4–5 (read); it is the Λ_S analog of p. 7, labeled inferred.

OLD:

    decide which steps live on S ×_{F₁^S} S = W_S*(S) rather than on S ×_k S

NEW:

    decide which steps live on S ×_{F₁^S} S = W_S*(S) (the Λ_S analog of p. 7's definition, inferred; pp. 4–5 print the Λ_S-structure and the translation task, not this equation) rather than on S ×_k S

**A17 — block `rb`.** Why: packaging label of `rb`: CLOSES.

OLD:

    The packaging of this rider is `[novelty: single-check]` until this stream's Opus reader has read it.

NEW:

    The packaging of this rider is `[dual-model check, 2026-09-25: Opus reader, results/zoo-s27/zoo-entries-read-O.md]`.

## §7 Checks per row (R-a, R-b′, xref)

**`ra` (III.20) — CLOSES after A3–A6.** Every quotation opened at the page as an image this session: Connes–Consani 1805.10501 pp. 17–18 ((12), (13) with c = ½(log π + γ), (14), "D • D′ := ⟨D ⋆ D̃′, Δ⟩ … obtained using the distribution N(u) and the fact that Ψ_λ is of degree λ", and the Riemann–Roch sentence) — exact; Haran 0911.3522 PDF page 88, printed folio 87 ((8.7.1)–(8.7.7), "There should exist an intersection pairing", "the sum is over the non-trivial zeros of Riemann's zeta ξ(α)") — exact except that X is the product of the overlined (compactified) spec Z (A4); Haran 1991 p. 259 (PDF page 3; W_p(f) = log p · Σ_{n≠0} f(pⁿ)·min(1, pⁿ); the Fundamental inequality; "the surface reduces to the diagonal! Nevertheless … ⟨f, g⟩ := W(f ∗ g*)") — exact, and the file is on disk (d3dc72ae…, matches); Banaszak–Uetake 0908.2909 p. 1 — exact (A5 adds what kind of object it is). The P1–P9 record sentence is HARVEST line 3 verbatim (capital N there, lower case mid-sentence here — fine), and it is present at C3 line 221 and C1 line 89 (read). The record corrections (titles of 1405.4527 / 1502.05580 / 1507.05818; Compositio 143 (2007) 618–688 open access) are HARVEST line 28 verbatim. The III.20-over-IV.1 placement (finding 4) is right: R-a is about the doubled objects' pairings — III.20's (B) and item 2 — and IV.1 gets the one-line pointer, the s25 precedent. The only overreach was the unbounded "every printed doubled object" (A3).

**`ra_ptr` (IV.1) — CLOSES after A7–A8.** The pointer's claim that the observable "IS the classical Weil test with multiplier 1" is exact at the page for Connes–Consani (s(f, g) := N(f ⋆ g̃), p. 17) and Haran 1991 (⟨f, g⟩ = W(f ∗ g*), p. 259); A7 says how the other two differ.

**`rb` (IV.10) — CLOSES after A9–A17.** At the page (images or full-text extraction with the page located): 0906.3146 p. 1 ("a surface bearing some kind of intersection theory"), p. 5 ("since the current version of our theory says nothing about the archimedean place of Q … Even so, it should be done"), p. 6 (W*(Spec A) = colim_n Spec W_n(A), W_n "(big) Witt vectors of length n"), p. 7 ("must be defined to be the Witt space W*(Spec Z)"), p. 8 ("the absolute point") — all exact; End = Hom_Λ(Z, Z) = {id} follows from "initial object" on p. 8. 0801.1691 p. 10 (1.10) — exact (W^fl, A9); p. 5 Figure 1 — the gluing (A12). 1006.0092 Prop. 16.5(d) (p. 31) and its proof ("integral and surjective on spectra … which is d"), Thm. 17.3 (p. 39) and diagram (17.1.1) — exact (A13, A14 add the pages). The Witt proof in the block is correct (my §3 re-derives it differently); the orchestrator's log numbers quoted in the block are exactly the logs' (read in full). The HOST-DIMENSION addition is stated as an addition and the existing EXECUTABLE TEST line (451's entry, line 448) is untouched in the dry run. Two sentences needed their citations repaired (A11: III.21 does not carry the Arakelov convention; A16: the Λ_S equation is inferred), and the prior-art sentence is replaced by the adjudicated one (A15). The claim that the component intersections carry "no quadratic form with a sign to be negative on a fiber-orthogonal part" is the scouts' agreed reading (HARVEST adjudication paragraph) and a derivation, not a quotation; it stands as written.

**`xref` — CLOSES, no amendment.** The table's heading (line 596) and the two Session-24 rows (624–625, scouted corners closed by blind pairs) admit a scouted-corner row; the cells are the brief's; the pointers III.20 / IV.10 / V.5 are the harvest's.

## §8 The writer's six-item NOTE, per item — which wording enters

1. HARVEST's "for every n ≤ 16" vs the N = 16 log (gcd 0 at n = 11, 13): **the record's (the logs')** — the writer's rider already quotes the logs as printed; confirmed by my full read of both logs.
2. Brief's "0908.2909 NOT on disk": **the record's** — on disk at `fetched-r2/t-43b-…pdf`, SHA-256 e5399476… = `sources/S27-0908.2909.pdf` (recomputed, identical).
3. Brief's "Haran 1991 if not on disk": **the record's** — `fetched-r3/haran1991.pdf` d3dc72ae… on disk; p. 259 read as an image; load-bearing at the page.
4. "0911.3522 p. 88": **both, as the rider has it** — PDF page 88, printed folio 87 (image: "87" at the foot).
5. W(Z) vs W^fl(Z): **the page's W^fl(Z) at (1.10), with the identification W^fl(Z) = W(Z) from §1.15 (p. 12)** — A9; the harvest's W(Z) is not wrong, only unexplained.
6. "B1 line 94 and B3 line 89 already carry the D3 closure lines": **the record's** — the closure lines are at B1 95 and B3 90, directly after the salvage line (iv) and the Untried entry at 94 and 89 (read); `iv4` cites 94 and 89 for those two items, correctly.

## §9 Hashes, dry run, the zoo untouched

- **The writer's `verification` block:** all 47 SHA-256 values recomputed this session by my own script (paths resolved as the block names them) — **47 of 47 match**; the block's "same hash" claim for `fetched-r2/t-43b-…pdf` also matches (e5399476…). Also recomputed: BRIEF `cf239a80…` ✓, proposed file `38986446…` ✓, `scripts/zoo-insert-s27.py` `8d61671f07a07feabedfc23c2311933fdd62f3d387af9989e34524c1c1d44836` ✓.
- **Dry run:** `python3 scripts/zoo-insert-s27.py --dry-run "results/zoo-s27/verify-O/dryrun-O.md"` → "+6 lines (649 -> 655); entries 58 (I 8, II 5, III 21, IV 19, V 5)"; `cmp` against `results/zoo-s27/dryrun-BARRIER-ZOO.md`: **byte-identical** (both SHA-256 `33d01ad868c6b5b4d85dfaa481038aff39f234b10530d21f1054d53fad3ce64c`); `BARRIER-ZOO.md` still `576dbd44…` afterwards; `diff` shows 6 added lines, 0 removed. Blocks `i5`, `iv4` byte-identical to the s26 blocks (my own comparison: True, True).
- **Amended dry run (§6):** `ba6c7aec…`, 655 lines, 58 entries; the zoo again untouched.

## §10 Group-IV decision on R-b′ — NO

NO: the candidate statement ("a one-dimensional doubled object carries no Hodge-type form, so no Castelnuovo–Severi step, whatever its correspondences' degrees") is not a new "class X cannot yield Y because Z" — it is III.20's (B) ("Hodge index/Castelnuovo on C×C") read as a precondition on the host, and it enters the zoo as the HOST-DIMENSION check added to IV.10's EXECUTABLE TEST by `rb`, which is the place a per-design test belongs; no proposed IV.20 BLOCK is written.

## §11 Files written by the reader (nothing else touched; nothing committed)

`results/zoo-s27/zoo-entries-read-O.md` (this file); `results/zoo-s27/verify-O/`: `zeros200_O.py` (c4ca3ecf…) + `zeros200_O_run.log` (819d1ce2…), `witt_diag_O.py` + `witt_diag_O_run.log`, `amendments_O.py`, `proposed-amended-O.md` (scratch), `zoo-insert-s27-flipsim-O.py` (scratch copy of the insert script with the two label lines widened and `PROPOSED` redirected), `dryrun-O.md`, `dryrun-amended-O.md`, `pa/` (my prior-art fetches with text extractions and the page images I read); a dated block in `results/zoo-s27/SHARED.md`. The proposed file, the insert script, the zoo and every direction file are untouched. Lint: none of "clearly / obviously / easy to see / well known" in this file or in any NEW text (checked by script, below in SHARED).
