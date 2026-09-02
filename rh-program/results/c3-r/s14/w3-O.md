# W3 (probe O) — Acyclicity of the C(T)-valued conormal spectra over a totally disconnected transversal: the transversal is transparent, but the source lemma it was to be transplanted from is false

**Program:** RH program, direction C3-r (geometric substrate), milestone M2c, Route 2, step S2, work item **W3** of `results/c3-r/s2-feasibility-note.md` §5 (= row **I-8** of that note's §4 table).
**Date:** 2026-09-02 (Session 14). **Author:** probe O (independent; a second probe ran in parallel on a different model and was not consulted, nor was any of its output seen).
**Scope guard:** S2 clause (i) only. Nothing below may be cited for positivity, Hodge theory, or M2c clause (ii) (guard Z2 of the S2 note). Nothing below asserts the existence of any arithmetic object (that is S4).
**Evidence discipline (standing order 5):** every source statement below is quoted from a PDF read on disk this session at a stated page, or from a primary text fetched this session at a stated location. Items recalled rather than read are tagged **[RU]** and carry no weight; where an [RU] item is load-bearing this is said explicitly and the consequence is downgraded.

---

## 0. VERDICT (stated first)

**PARTIAL.** W3 as commissioned asked to prove *or refute* that the transplanted C(T)-valued symbol/Sobolev spectra "have coinciding step topologies **as in** [ÁLKL23] Cor. 4.5 / 6.12 / 6.24, hence acyclic countable inductive limits by Wengenroth's criterion". The answer splits, and neither half may be rounded up:

**(V1) THEOREM (NO) — against the literal target.** The coincidence statements of [ÁLKL23] — Prop. 3.2, Cor. 3.4, Cor. 4.5, Prop. 6.10 / Cor. 6.12 (v1 numbering; = Prop. 6.12 / Cor. 6.14 in v3), and Cor. 6.24 — are **false as stated, already in the manifold case, i.e. already for a one-point transversal.** §6 gives an explicit counterexample (a single one-line family of symbols, **lying in C_c^∞ and hence in S^{−∞} = ∩_m S^m**, so that it refutes Cor. 3.4 for *every* pair m < m′ simultaneously) and, from it, a Cauchy sequence with no limit that refutes the completeness step on which the published proof of Prop. 3.2 rests. Verified against **both** the on-disk arXiv v1 and the current arXiv v3 (1 June 2024), whose §3 is textually identical. Consequently the transplanted literal statements are false too (the counterexample is constant in the transversal parameter, hence lifts verbatim). **No transplant of those statements exists, because there is nothing true to transplant.**

**(V2) THEOREM (YES) — for what W3 must actually deliver.** Acyclicity in the exact form of Wengenroth's criterion quoted at [ALKL] §2.1.1 p. 9 and [ÁLKL23] §2 p. 4 **is transparent to the transversal**: for any compact Hausdorff T (total disconnectedness neither needed nor harmful), the functor E ↦ C(T, E) preserves Fréchet-ness, continuous injections, closed subspaces, finite products, and Wengenroth's criterion *verbatim*; and the criterion descends along the closed subspace of constant functions. Hence

> **the transplanted spectrum is acyclic if and only if the manifold-level spectrum is** (§4, Theorem 1),

and when it is, the transplanted LF-spaces are boundedly / compactly / sequentially retractive, complete, regular, Hausdorff, barreled, ultrabornological and webbed — the entire package rows I-8, I-9 and I-13 of the S2 note consume. **This is the positive content W3 was commissioned for, and it is proved in full, unconditionally on the analysis and conditionally only on the W1/W2 outputs named in §3.4.**

**(V3) THEOREM (repair) — the manifold-level input is true and re-proved.** §7 supplies a correct proof of the acyclicity that [ÁLKL23] Cor. 3.6 / 4.7 / 6.14 / 6.20 / 6.25 assert: an anisotropic Landau–Kolmogorov interpolation verifying Wengenroth's 0-neighbourhood criterion for the symbol spectrum over a **compact** base, and its b-geometry analogue for the bounds spectrum A(M̄). The proof is pointwise in the base point and in the transversal parameter, so by (V2) it transplants with no loss. §7.4 also repairs the one place where the false coincidence statement is actually consumed downstream ([ÁLKL23] Claim 6.43 = v3 Claim 6.46, the "topological lifting of bounded sets" that carries the exactness of the dual-conormal sequence): the step "V ∩ A^m = W ∩ A^m" must be weakened to "A ∩ V ⊆ W", which follows from bounded retractivity applied to the bounded set A. §6.5 also supplies the one *other* repair the refutation forces and that the first draft of this note wrongly recorded as unnecessary: **[ÁLKL23] Cor. 3.5 (density of C_c^∞ in S^m with the S^{m′}-topology) is proved in the source *from* the false Cor. 3.4**, and is re-proved here directly (§6.5, Lemma 6.5.1). **With these repairs the memoir's Theorems 1.3.3 / 1.3.6 and the sequences (1.3.1)/(1.3.2) are not damaged.**

**(V4) THEOREM (NO) — a real, priced loss, now proved rather than asserted.** For T infinite, C(T, E) is **not semi-Montel and not semi-reflexive** (§5.1), and C(T, S) is **not a compact operator** for any S ≠ 0 (§5.2). Hence (a) the Montel/reflexivity halves of [ÁLKL23] Cor. 3.6 / 4.7 / 6.14 / 6.20 / 6.25 genuinely die under the transplant — confirming row I-10 of the S2 note with a proof where the note had an assertion — and (b) the "compact linking maps ⟹ acyclic" shortcut recorded at [ÁLKL23] §2 p. 4 is destroyed, so the interpolation/topology route is the *only* one available. Row I-8's instinct ("[ÁLKL23]'s acyclicity does NOT route through compact embeddings") is vindicated and is now a theorem about the transplant rather than a reading of the source.

**(V5) A further correction to the source, needed by the transplant.** [ÁLKL23] Cor. 3.6 (S^∞(U × R^l) acyclic) is **false for non-compact U** (§6.4, counterexample). The localisation used in (4.10) must therefore be read with symbol spaces of *fixed compact base support*; with that reading everything the memoir uses is correct. This matters for the transplant because the foliated-space charts U_i × T_i have non-compact U_i.

**Net effect on the S2 ledger.** W3 is **discharged as to its conclusion and corrected as to its mechanism.** The S2 note's verdict TRANSFERS-WITH-WORK is **not** reopened: no obstruction was found, and the item flagged as "the one place whose failure would reopen the verdict" does not fail. But the S2 note's row I-8 sentence — "the SAME mechanism proves the C(T)-valued coincidence" — must be struck: the mechanism it names does not exist even upstream. The corrected statement is: *Wengenroth's criterion, verified by interpolation, is preserved verbatim by C(T, −).* A new residual-risk item is created (§12): every future citation of [ALKL]/[ÁLKL23] coincidence statements in this program must go through §6–§7 of this note.

---

## 1. Sources read this session, with locations

**On disk (program corpus).**

- **[ALKL]** = `fetched-r3/r3s-17-alvarez-lopez-kordyukov-leichtnam-trace-formula-foliated-flows-arxiv-2402.06671v1-SESSION8-FETCH.pdf`. J. A. Álvarez López, Yu. A. Kordyukov, E. Leichtnam, *A trace formula for foliated flows*, arXiv:2402.06671v1, 176 printed pp. (PDF 177 pages; **PDF page = printed page + 6**). Read this session, fresh `pdftotext -layout` extraction: §2.1.1 in full (printed p. 9 = PDF p. 15) — the Wengenroth quote, verbatim in §2.1 below; §2.1.8 (printed p. 15 area, PDF p. 21) — the restatement of [ÁLKL23] Cors. 3.4–3.6; §2.2.2 (printed p. 21, PDF p. 27) — the property list for I(M, L); §2.6.7 (printed p. 44 area, PDF p. 50) — the restatement for J(M, L); §2.5/§2.6 A(M) property list (PDF p. 44 area); §5.2.1 and §2.6.7 compact-retractivity uses (PDF pp. 124, 130 area); index entries "acyclic, 9", "compactly retractive, 9", "partial extension map, 39" (PDF p. 176).
- **[ÁLKL23] v1** = `fetched-r3/r3s-18-alvarez-lopez-kordyukov-leichtnam-topology-space-conormal-distributions-arxiv-2304.00798v1-SESSION8-FETCH.pdf`, 54 printed pp. (PDF 55 pages; PDF page = printed page). Read this session in full for §2 (p. 4), §3 (pp. 13–15), §4 (pp. 15–19), §6.8–§6.15 (pp. 29–34), §6.23–§6.25 (pp. 38–39), §7.1 (p. 39).

**Fetched (primary text, network) — provenance stated exactly.**

- **[ÁLKL23] v3** = `https://arxiv.org/pdf/2304.00798v3`, saved in this session's scratchpad as `alkl23v3.pdf` (55 pages, 748 540 bytes; `pdfinfo` reports Creator "LaTeX with hyperref", Producer "GPL Ghostscript 10.01.2", CreationDate **2024-06-04**). **Not** added to the program corpus — it is a working copy. *Provenance note (this is a resumed run):* the PDF was downloaded by the earlier, usage-limit-killed run of this same probe, earlier on 2026-09-02, and was still present in the session scratchpad; **this run re-verified it directly** rather than trusting the earlier run's report — by `pdftotext -layout` extraction, a line-by-line `diff` of the §3 pages of v3 against the on-disk v1, and a `grep` of every statement number cited below.
- The arXiv abstract page `https://arxiv.org/abs/2304.00798` was **fetched again in this run** (2026-09-02) and its submission history reads, verbatim: "[v1] Mon, 3 Apr 2023 08:39:19 UTC (56 KB) … [v2] Sat, 29 Jul 2023 06:48:15 UTC (56 KB) … [v3] Sat, 1 Jun 2024 07:46:00 UTC (56 KB)". So **v3 is the current arXiv version**. The record shows no journal reference (only arXiv's own DataCite DOI).
- Read in v3 this run: §2 (p. 4), §3 (pp. 13–15), §4 (pp. 15–19), §6.10–§6.13 (pp. 30–33), §6.15 (p. 34), §6.23 (pp. 38–39). **v3 §3 is textually identical to v1 §3 up to line-breaking** (Props. 3.2, 3.3, Cors. 3.4–3.6, Rem. 3.8, *including the proofs*; the `diff` shows only reflowed lines and one added sentence in §2.12 about a partition of unity, before §3 begins). The §6 statements are the same modulo renumbering, each checked by `grep` this run: v1 Prop. 6.10 → v3 Prop. 6.12; v1 Cor. 6.12 → **v3 Cor. 6.14**; v1 Cor. 6.14 → v3 Cor. 6.16; v1 Cor. 6.19 → v3 Cor. 6.21; v1 Cor. 6.24 → v3 Cor. 6.27; v1 Cor. 6.25 → v3 Cor. 6.28; v1 Prop. 6.26 → v3 Prop. 6.29; v1 Prop. 6.42 → v3 Prop. 6.45; v1 Claim 6.43 → v3 Claim 6.46; v1 Cor. 7.20 → v3 Cor. 7.22. **The defect is present in v3 unchanged**: v3 Claim 6.46's proof still contains the sentence "By Corollary 6.14, there is some 0-neighborhood V ⊂ A(M) such that V ∩ A^m(M) = W ∩ A^m(M)".
- **v3 supplies one definition v1 omits**, which this note's §7.4 repair uses: v3 §6.15, p. 34, read verbatim — "Given linear subspaces, X ⊂ A(M) and Y ⊂ Ȧ(M), a map E : X → Y is called a **partial extension map** if R(Y) ⊂ X and **RE = 1 on X**."
- **The published version was NOT consulted.** `https://link.springer.com/article/10.1007/s11868-024-00617-y` (the DOI recorded in the S2 note §1 for J. Pseudo-Differ. Oper. Appl.) returned a bot-challenge page ("Client Challenge", 3 038 bytes) on the one attempt made this run. Whether the journal text differs from arXiv v3 is therefore **unknown to this note**, and §10 prices that.

**Program files read (not sources, context).** `results/c3-r/s2-feasibility-note.md` (all of §§1–8; §2.3 inventory, §3.1–§3.3 definitions, §4 rows I-1 … I-13, §5 W1–W7, §6 obstruction disposals, §8 citation table); `results/c3-r/probe-9.3-adjudication.md` (all; §6 is the binding S2 adjudication).

**Not on disk, and how it is handled.**

- **[Wen03]** J. Wengenroth, *Derived functors in functional analysis*, Springer LNM (bibliographic identity read at [ALKL] bibliography, printed p. 166). **Not on disk.** Every use below is through the two statements quoted verbatim in §2.1 from [ALKL] p. 9 and [ÁLKL23] p. 4. No property of [Wen03] beyond those quoted sentences is used anywhere in this note.
- **[Mel96]** R. B. Melrose, *Differential analysis on manifolds with corners* (identity from the same bibliography). Not on disk. It is cited by [ÁLKL23] for the Fréchet-ness of I^m(M, L) ([ÁLKL23] §4.3.2, "which becomes a Fréchet space [25, Sections 6.2 and 6.10]") and for A(M)-facts. Those citations are **flagged as unverified inputs** in §3.4 (H3) and §10, and the corresponding transplanted facts are hypotheses, not results, of this note.
- The classical Landau–Kolmogorov interpolation inequality used in §7 is elementary calculus; the one-dimensional base case is **proved in full** in §7.1 and the iteration to general order is stated with its recipe and tagged **[RU-standard]** in §10.

---

## 2. The manifold-level machinery, quoted verbatim

### 2.1 Wengenroth's criterion, exactly as the two papers state it

[ALKL] §2.1.1, printed p. 9 (PDF p. 15), read verbatim this session:

> "Now fix an inductive spectrum of LCSs of the form (X_k) = (X_0 ⊂ X_1 ⊂ · · ·), and let X = ⋃_k X_k. The condition on (X_k) to be **acyclic** means that, for all k, there is some k′ ≥ k such that, for all k′′ ≥ k′, the topologies of X_{k′} and X_{k′′} coincide on **some 0-neighborhood of X_k** [Wen03, Theorem 6.1]. In this case, X is Hausdorff if and only if all X_k are Hausdorff [Wen03, Proposition 6.3]. It is said that (X_k) is **regular** if any bounded B ⊂ X is contained and bounded in some step X_k. If moreover the topologies of X and X_k coincide on B, then (X_k) is said to be **boundedly retractive**. The conditions of being compactly retractive or sequentially retractive are similarly defined, using compact sets or convergent sequences.
> If the steps X_k are **Fréchet** spaces, the above properties of (X_k) only depend on the LF-space X [Wen03, Chapter 6, p. 111], and therefore they are considered as properties of X. In this case, X is acyclic if and only if it is boundedly/compactly/sequentially retractive [Wen03, Proposition 6.4]. As a consequence, acyclic LF-spaces are complete and regular [Wen03, Corollary 6.5]. A topological vector subspace Y ⊂ X is called a **limit subspace** if Y ≡ ⋃_k (X ∩ Y_k) as TVSs.
> Assume the steps X_k are LCHSs. It is said that (X_k) is **compact** if the inclusion maps are compact operators. Then (X_k) is acyclic, and so X is Hausdorff. Moreover X is a complete bornological DF Montel space [Kom67, Theorem 6′]."

[ÁLKL23] §2, p. 4 (v1 and v3 alike), read verbatim this session, is the same text with the extra sentence:

> "It is said that (X_k) is regular if any bounded B ⊂ X is contained and bounded in some step X_k. … A topological vector subspace Y ⊂ X is called a limit subspace if Y ≡ ⋃_k Y_k, where Y_k = X ∩ Y_k. This condition is satisfied if and only if the spectrum consisting of the spaces X_k/Y_k is acyclic [39, Chapter 6, p. 110]."

and, on compact spectra:

> "Assume the steps X_k are LCHSs. It is said that (X_k) is compact if the inclusion maps are compact operators. In this case, (X_k) is clearly acyclic, and so X is Hausdorff. Moreover X is a complete bornological DF Montel space [18, Theorem 6′]."

Three things are fixed by these quotations and are used below exactly as written and never beyond:

- **(W-a)** Acyclicity = for all k there is k′ ≥ k such that for all k′′ ≥ k′ the topologies of X_{k′} and X_{k′′} coincide on **some 0-neighbourhood of X_k**. (Not: on all of X_k.)
- **(W-b)** With **Fréchet steps**: acyclic ⟺ boundedly/compactly/sequentially retractive; acyclic ⟹ complete and regular; acyclic ⟹ (Hausdorff ⟺ all steps Hausdorff); and all of these depend only on the LF-space, not on the chosen cofinal spectrum of Fréchet steps.
- **(W-c)** A compact spectrum is acyclic. (This is a *sufficient* route only, and §5.2 shows the transplant destroys it.)

### 2.2 The symbol spaces and the coincidence statements

[ÁLKL23] §3, printed p. 13 (v1 and v3), read verbatim:

> "Recall that a symbol of order at most m ∈ R on U × R^l, or simply on U, is a function a ∈ C^∞(U × R^l) such that, for any compact K ⊂ U, and multi-indices α ∈ N_0^n and β ∈ N_0^l,
> (3.1)  ‖a‖_{K,α,β,m} := sup_{x∈K, ξ∈R^l} |∂_x^α ∂_ξ^β a(x, ξ)| / (1 + |ξ|)^{m−|β|} < ∞.
> The set of symbols of order at most m, S^m(U × R^l), becomes a Fréchet space with the semi-norms ‖·‖_{K,α,β,m} given by (3.1)."

and pp. 13–14:

> "(3.4)  ‖a‖_{Q,C^k} = sup_{(x,ξ)∈Q, |α|+|β|≤k} |∂_x^α ∂_ξ^β a(x, ξ)| .
> (3.5)  ‖a‖′_{K,α,β,m} = sup_{x∈K} limsup_{|ξ|→∞} |∂_x^α ∂_ξ^β a(x, ξ)| / |ξ|^{m−|β|} .
> **Proposition 3.2.** The semi-norms (3.4) and (3.5) together describe the topology of S^m(U × R^l).
> **Proposition 3.3.** For m, m′ ∈ N_0, α ∈ N_0^n, β ∈ N_0^l and any compact K ⊂ U, if m < m′, then ‖·‖′_{K,α,β,m′} = 0 on S^m(U × R^l).
> **Corollary 3.4.** For m < m′, the topologies of S^{m′}(U × R^l) and C^∞(U × R^l) coincide on S^m(U × R^l). Therefore the topologies of S^∞(U × R^l) and C^∞(U × R^l) coincide on S^m(U × R^l).
> Proof. The first assertion is a consequence of Propositions 3.2 and 3.3. …
> **Corollary 3.6.** S^∞(U × R^l) is an acyclic Montel space, and therefore complete, boundedly retractive and reflexive.
> Proof. Corollary 3.4 gives the property of being acyclic, and therefore complete and boundedly retractive (Section 2.1). …"

The proof of Prop. 3.2, quoted in full because §6 refutes it:

> "Proof. Let S′^m(U × R^l) denote the LCHS defined by endowing the vector space S^m(U × R^l) with the topology induced by the semi-norms (3.4) and (3.5) together; in fact, countably many semi-norms of these types are enough to describe its topology (taking exhausting increasing sequences of compact sets), and therefore S′^m(U × R^l) is metrizable. Let Ŝ′^m(U × R^l) denote its completion, where the stated semi-norms have continuous extensions. There is a continuous inclusion S′^m(U × R^l) ⊂ C^∞(U × R^l), which can be extended to a continuous map φ : Ŝ′^m(U × R^l) → C^∞(U × R^l) because C^∞(U × R^l) is complete. **For any a ∈ Ŝ′^m(U × R^l), and K, α and β like in (3.5), since ‖φ(a)‖′_{K,α,β,m} = ‖a‖′_{K,α,β,m} < ∞, there are C, R > 0 so that, if x ∈ K and |ξ| ≥ R, then |∂_x^α∂_ξ^β φ(a)(x,ξ)| / (1+|ξ|)^{m−|β|} ≤ C.** … This shows that ‖φ(a)‖_{K,α,β,m} < ∞, obtaining that a ≡ φ(a) ∈ S^m(U × R^l). Hence S′^m(U × R^l) is complete, and therefore it is a Fréchet space. Thus the identity map S^m(U × R^l) → S′^m(U × R^l) is a continuous linear isomorphism between Fréchet spaces, obtaining that it is indeed a homeomorphism by a version of the open mapping theorem …" (emphasis added; the emphasised sentence is the step §6.2 refutes).

[ÁLKL23] §4.3.2, printed p. 18, the localisation that carries Cor. 4.5 (v1 and v3):

> "Take a finite cover of L by relatively compact charts (U_j, x_j) of M adapted to L, and write L_j = L ∩ U_j. Let {h, f_j} be a C^∞ partition of unity of M subordinated to the open covering {M ∖ L, U_j}. Then I(M, L) consists of the distributions u ∈ C^{−∞}(M) such that hu ∈ C^∞(M ∖ L) and f_j u ∈ I_c(U_j, L_j) for all j. Then, according to Proposition 4.3, every f_j u is given by some a_j ∈ S^∞(N^*L_j; ΩN^*L_j). For
> (4.9)  m̄ = m + n/4 − n′/2 ,
> the condition a_j ∈ S^{m̄}(N^*L_j; ΩN^*L_j) describes the elements u of a C^∞(M)-submodule I^m(M, L) ⊂ I(M, L), which is independent of the choices involved … Moreover, applying the versions of semi-norms (2.1) on C^∞(M∖L) to hu and versions of semi-norms (3.1) on S^{m̄}(N^*L_j; ΩN^*L_j) to every a_j, we get semi-norms on I^m(M, L), which becomes a Fréchet space [25, Sections 6.2 and 6.10]. In other words, the following map is required to be a TVS-embedding:
> (4.10)  I^m(M, L) → C^∞(M ∖ L) ⊕ ∏_j S^{m̄}(N^*L_j; ΩN^*L_j),  u ↦ (hu, (a_j)) ."

and printed p. 19:

> "**Corollary 4.5.** For m < m′, m′′, the topologies of I^{m′}(M, L) and I^{m′′}(M, L) coincide on I^m(M, L).
> Proof. Use Corollary 3.4 and the TVS-embeddings (4.10)."

Also printed p. 19, for the record (its proof is *not* affected — see §6.5):

> "**Corollary 4.7.** I(M, L) is an acyclic Montel space, and therefore complete, boundedly retractive and reflexive.
> Proof. Like in Corollary 3.6, by Corollaries 4.2 and 4.5, it is enough to prove that I(M, L) is semi-Montel. The TVS-embedding (4.13) is closed because I(M, L) is complete. Then I(M, L) is semi-Montel because C^∞(M∖L) and S^∞(N^*L_j; ΩN^*L_j) are Montel spaces (Corollary 3.6) …"

### 2.3 The bounds filtration of A(M̄) and the coincidence statement there

[ÁLKL23] §6.10, printed p. 30 (v1), read verbatim:

> "For every m ∈ R, let A^m(M) = { u ∈ C^{−∞}(M) | Diff_b(M) u ⊂ x^m L^∞(M) }. This is another C^∞(M)-module and LCS, with the projective topology given by the maps P : A^m(M) → x^m L^∞(M) (P ∈ Diff_b(M))."

and printed p. 31:

> "Let { P_j | j ∈ N_0 } be a countable C^∞(M)-spanning set of Diff_b(M). The topology of A^m(M) can be described by the semi-norms ‖·‖_{k,m} (k ∈ N_0) given by
> (6.40)  ‖u‖_{k,m} = ‖P_k u‖_{x^m L^∞} = ess sup_M x^{−m}|P_k u| = sup_{M̊} x^{−m}|P_k u| ,
> using (6.32) in the last expression. From (2.1) and (6.32), we also get the continuous semi-norms ‖·‖_{K,k,m} (for any compact K ⊂ M̊ and k ∈ N_0) on A^m(M) given by
> (6.41)  ‖u‖_{K,k,m} = sup_K |P_k u| .
> Other continuous semi-norms ‖·‖′_{k,m} (k ∈ N_0) on A^m(M) are defined by
> (6.42)  ‖u‖′_{k,m} = lim_{ε↓0} sup_{{0<x<ε}} x^{−m}|P_k u| .
> The proofs of the following results are similar to the proofs of Propositions 3.2 and 3.3 and Corollaries 3.4 to 3.6, using (6.32).
> **Proposition 6.10.** The semi-norms (6.41) and (6.42) together describe the topology of A^m(M).
> **Proposition 6.11.** For m, m′, k ∈ N_0, if m′ < m, then ‖·‖′_{k,m′} = 0 on A^m(M).
> **Corollary 6.12.** If m′ < m, then the topologies of A^{m′}(M) and C^∞(M̊) coincide on A^m(M). Therefore the topologies of A(M) and C^∞(M̊) coincide on A^m(M).
> **Corollary 6.14.** A(M) is an acyclic Montel space, and therefore complete, boundedly retractive and reflexive."

Also read verbatim, [ÁLKL23] §6.8 p. 29: "(6.32) Ȧ(M)|_{M̊}, A(M) ⊂ C^∞(M̊)" (by elliptic regularity), and §6.13 p. 33: "**Corollary 6.24.** For m < m′, m′′, the topologies of K^{m′}(M) and K^{m′′}(M) coincide on K^m(M)", whose stated proof is "with formally the same proof, using Corollaries 6.19, 6.20 and 6.23", i.e. it descends from Cor. 4.5 through the closed-subspace chain K^m(M) = Ȧ^m_{∂M}(M) ⊂ Ȧ^m(M) = I^m_M(M̆, ∂M) ⊂ I^m(M̆, ∂M) (§6.12, printed p. 32: "(6.46) Ȧ^m(M) = I^m_M(M̆, ∂M) ⊂ I^m(M̆, ∂M) … which are closed subspaces").

### 2.4 The one place downstream that consumes a coincidence statement

[ÁLKL23] §6.23, printed pp. 38–39 (v1; = v3 §6.23, Prop. 6.45 / Claim 6.46 on the same printed pages), read verbatim:

> "**Proposition 6.42.** The sequence (6.59) is exact in the category of continuous linear maps between LCSs.
> Proof. By Proposition 6.7 and [39, Lemma 7.6], it is enough to prove that the map (6.35) satisfies the following condition of 'topological lifting of bounded sets.'
> **Claim 6.43.** For all bounded subset A ⊂ A(M), there is some bounded subset B ⊂ Ȧ(M) such that, for all 0-neighborhood U ⊂ Ȧ(M), there is a 0-neighborhood V ⊂ A(M) so that A ∩ V ⊂ R(B ∩ U).
> Since A(M) is boundedly retractive (Corollary 6.14), A is contained and bounded in some step A^m(M). For any m′ > m, let E_{m′} : A^m(M) → Ȧ^{(s)}(M) be the partial extension map given by Proposition 6.26. Then B := E_{m′}(A) is bounded in Ȧ^{(s)}(M), and therefore in Ȧ(M). Moreover, given any 0-neighborhood U ⊂ Ȧ(M), there is some 0-neighborhood W ⊂ A^{m′}(M) so that E_{m′}(W) ⊂ U ∩ Ȧ^{(s)}(M). **By Corollary 6.12, there is some 0-neighborhood V ⊂ A(M) such that V ∩ A^m(M) = W ∩ A^m(M).** Hence E_{m′}(V ∩ A^m(M)) ⊂ U ∩ Ȧ^{(s)}(M), yielding
> A ∩ V = R(E_{m′}(A ∩ V)) ⊂ R(E_{m′}(A) ∩ E_{m′}(V ∩ A^m(M))) ⊂ R(B ∩ U) ." (emphasis added; §7.4 repairs the emphasised step.)

This is the sole place in the material read this session where a coincidence statement is consumed by anything other than an acyclicity claim. The exactness of the *conormal* sequence itself ([ÁLKL23] Cor. 7.30 = v3 Cor. 7.30, printed p. 48: "The conormal sequence of M at L is exact in the category of continuous linear maps between LCSs", proved from Prop. 7.29, "The maps (7.30) and (7.31) are surjective topological homomorphisms") does not pass through a coincidence statement at all.

---

## 3. The transplant: objects, model, hypotheses

Throughout, **T** denotes a compact metrizable **totally disconnected** space (the transversal factor of the solenoid; in the intended arithmetic reading a Cantor group such as Ẑ^×_{(p)} or Z_p^m). Everything proved below about T uses only **compactness and Hausdorffness**; where total disconnectedness would help it is said so, and §9 audits every step for a transversal-induced failure.

### 3.1 The ambient category, quoted

[Den05] §7.1 (as transcribed in the S2 note §3.1, itself quoting the on-disk `fetched/x-20-…-2005-arithmetic-geometry-and-analysis-on-foliated-spaces.pdf` p. 28): a **foliated space** with d-dimensional leaves is a separable metrizable X with charts φ_i : U_i → F_i × T_i, F_i ⊂ R^d open, transitions φ_j φ_i^{−1}(x, y) = (f_{ij}(x, y), g_{ij}(y)), and "**All partial derivatives D_x^α f_{ij}(x, y) exist and are continuous as functions of x and y**"; a **solenoid** is such an X with T_i **totally disconnected**. (This note takes that quotation from the S2 note rather than re-reading [Den05]; it is used only to fix the category and nothing below depends on its exact wording — see §10.)

The S2 geometric axioms (A-i)–(A-vi) of the S2 note §3.2 are assumed *verbatim*, in particular:

- **(A-i)** X a compact smooth solenoid, dim 3, with codimension-one foliation F and F-compatible flow φ;
- **(A-iii)** a collar 𝒞 ≅ (−ε, ε)_x × X⁰ of foliated spaces, with X⁰ = {x = 0} and x tangentially smooth with non-vanishing leafwise differential on X⁰.

### 3.2 The chart hypothesis, isolated because everything rests on it

> **(H-chart).** X is compact, so it admits a **finite** atlas {(U_i × T_i)}_{i=1}^N of foliated-space charts, U_i ⊂ R^3 open and relatively compact in a slightly larger chart domain, T_i compact totally disconnected, together with a tangentially smooth partition of unity {ρ_i} subordinate to it; the charts meeting X⁰ may be taken *adapted*, i.e. of the form (−ε, ε)_x × V_i × T_i with X⁰ ∩ (U_i × T_i) = {0} × V_i × T_i, and the charts of the cut space X̄ likewise.

(H-chart) is immediate from compactness plus (A-iii): the collar is a product in the x-direction, so an atlas of X⁰ times (−ε, ε) is an adapted atlas of the collar. The partition of unity exists and is in fact *easier* than on a manifold: since each T_i is compact and totally disconnected, finite **clopen** partitions of T_i are available and their characteristic functions are tangentially smooth (locally constant transversally, so every condition on leafwise derivatives is vacuous). This is the one place in the whole of W3 where total disconnectedness is used, and it is used to make something easier, never harder.

### 3.3 The two candidate models, and why one of them is the right one

For a chart U × T (U ⊂ R^N open) and a manifold-level Fréchet space E = E(U) of functions/distributions on U, there are two inequivalent ways to define its transplant:

- **(D-unif)** *the uniform model*: E_τ(U × T) := **C(T, E)**, continuous maps T → E, with the seminorms p^T(a) := sup_{t∈T} p(a(t)) for p a continuous seminorm of E;
- **(D-joint)** *the joint-continuity model*: functions a(·, t) on U × T all of whose leafwise derivatives are **jointly** continuous on U × T, with the E-seminorms taken uniformly in t.

**Lemma 0.** If the seminorms defining E are suprema over **compact** subsets of U of finitely many derivatives (as for C^∞(U)), then (D-unif) and (D-joint) coincide: C^∞_τ(U × T) ≡ C(T, C^∞(U)).
*Proof.* If a ∈ C(T, C^∞(U)) then each ∂^γ a is jointly continuous, being a composition of continuous maps. Conversely, if all ∂^γ a are jointly continuous and Q ⊂ U is compact, then ∂^γ a is uniformly continuous on the compact Q × T, so t ↦ ∂^γ a(·, t)|_Q is continuous into C(Q); running over γ and an exhaustion by compacts gives continuity of t ↦ a(·, t) into C^∞(U). ∎

**They differ as soon as a seminorm involves a supremum over a non-compact region** — which is exactly the case for the symbol seminorms (3.1) (sup over ξ ∈ R^l) and for the weighted L^∞ seminorms (6.40) (sup over M̊ up to the boundary). For those, (D-joint) is strictly larger than (D-unif): boundedness plus local uniform convergence does not give convergence in the global weighted supremum.

**This note works throughout in (D-unif),** for four reasons, each checkable:

1. It is the model the S2 note already fixed: "**H^s_τ(X)**: in charts, C(T_i, H^s(R³-chart))-pieces glued by the clopen partition; equivalently, the completion of C^∞_τ in the norm sup_{t∈T} ‖·‖_{H^s(slice)}" (S2 note §3.3). The two descriptions there agree precisely because C(T, C^∞) is dense in C(T, H^s) (clopen-partition approximation of a uniformly continuous H^s-valued map by a locally constant one, then smoothing each value).
2. It is the model of the one published trace formula over a p-adic transversal ([Lei07a] Definitions 1–2, as recorded in the S2 note §3.1 and §8).
3. It is **stable under the construction that defines the conormal spaces.** If H^s_τ = C(T, H^s) in a product chart, then
 I^{(s)}_τ := { u ∈ C^{−∞}_τ : Diff_τ(X, X⁰) u ⊂ H^s_τ }, projective topology,
 equals C(T, I^{(s)}) in that chart as a TVS: t ↦ u(·, t) is continuous into I^{(s)} (which carries the projective topology of the maps P : I^{(s)} → H^s) **iff** t ↦ P u(·, t) is continuous into H^s for every P in a generating set — which is the defining condition. (Enlarging the generating set from t-independent P to all of Diff_τ, whose coefficients depend on t, changes nothing: multiplication by f ∈ C^∞_τ is bounded on H^s_τ with a t-uniform bound, by compactness of T and continuity of t ↦ f(·, t) in C^∞.)
4. It is stable under the flow: φ preserves X⁰ and is tangentially smooth, so in charts φ(x, t) = (ψ_t(x), h(t)) with h a homeomorphism of the transversal and t ↦ ψ_t continuous into C^∞; hence φ^* maps C(T, E) to C(T, E).

Since W3 is a lemma about a *definition we are choosing*, choosing (D-unif) is legitimate; the honest cost is recorded in §10 (the (D-joint) model is left undecided, and the arithmetic object, if it ever exists, must be checked against (D-unif)).

### 3.4 The transplanted objects, written out

Fix (H-chart). All spaces below carry the topologies stated; "slice" means the manifold-level object on the chart's U_i ⊂ R^3 (or on the corresponding piece of the cut space X̄).

- **C^∞_τ(X)**: tangentially smooth functions; Fréchet; in a chart, C(T_i, C^∞(U_i)) by Lemma 0.
- **Λ, C^{−∞}_τ(X)**: the strong dual of C^∞_τ(X; Ω_τ) with the Λ-twisted pairing of the S2 note §3.3 (axiom (A-v), full support, so C^∞_τ ↪ C^{−∞}_τ is injective and C^{−∞}_τ is Hausdorff).
- **H^s_τ(X)** (s ∈ R): in a chart, C(T_i, H^s(U_i)); glued by the clopen/tangentially smooth partition of unity. Banach.
- **Diff_τ(X, X⁰)**: the filtered algebra generated over C^∞_τ(X) by the tangential vector fields tangent to X⁰. In an adapted chart it is spanned by x∂_x and the leafwise fields along X⁰ — **exactly the slice algebra Diff(U_i, {x = 0} ∩ U_i)**, because all three of X's tangential directions (x and the two along X⁰) survive and the transversal contributes no vector fields at all. Compare [ÁLKL23] §7.1, printed p. 39, read verbatim: "For every k, Diff(U_j, L ∩ U_j) is spanned by x∂_x, ∂_{j1}, …, ∂_{j,n−1} using the operations of C^∞(U_j)-module and algebra". Countably (indeed, by (H-chart), finitely) generated over C^∞_τ(X) in each filtration degree.
- **I^{(s)}_τ(X, X⁰)** := { u ∈ C^{−∞}_τ(X) : Diff_τ(X, X⁰) u ⊂ H^s_τ(X) }, projective topology from the maps P. In a chart, C(T_i, I^{(s)}(U_i, L_{0,i})) by §3.3(3).
- **I^m_τ(X, X⁰)** (symbol order): defined by the transplant of (4.10). Writing {h, ρ_j} for the partition of unity of (H-chart) subordinate to {X ∖ X⁰, U_j × T_j}, and a_j for the partial-Fourier symbol of ρ_j u in the chart, I^m_τ is the space of u ∈ C^{−∞}_τ(X) with hu ∈ C^∞_τ(X ∖ X⁰) and a_j ∈ S^{m̄}_τ(N^*L_j × T_j; Ω) := **C(T_j, S^{m̄}_{K_j}(N^*L_j; Ω))**, where K_j := supp ρ_j ∩ X⁰-slice is a **fixed compact base support** (see (V5) and §6.4: the fixed compact support is not optional), topologised so that
 **(4.10)_τ**  I^m_τ(X, X⁰) → C^∞_τ(X ∖ X⁰) ⊕ ⊕_{j} C(T_j, S^{m̄}_{K_j}(N^*L_j; Ω)),  u ↦ (hu, (a_j))
 is a TVS-embedding. The direct sum is **finite** by (H-chart).
- **A^m_τ(X̄), Ȧ^m_τ(X̄), K^m_τ, J^m_τ, I′_τ, K′_τ, J′_τ**: the transplants of the S2 note §3.3 list, defined chart-wise as C(T_i, ·) of the slice objects and glued by the same partition of unity; for A^m_τ this reads A^m_τ(X̄) = { u ∈ C^{−∞}_τ(X̄) : Diff_{b,τ}(X̄) u ⊂ x^m L^∞_τ(X̄) } with x^m L^∞_τ := C(T, x^m L^∞(slice)) in charts, projective topology.

**Hypotheses inherited from W1/W2 (not proved here; W3 is conditional on them and on nothing else).**

- **(H1)** [W1] The parameterised scale exists with the standard properties: H^s_τ, the supported/extendible pairs on X̄, the b-Sobolev and weighted spaces, and the elliptic-regularity inclusion A_τ(X̄) ⊂ C^∞_τ(X̊̄) transplanting (6.32). *(Each is a per-slice statement with t-uniform constants; the S2 note rows I-4 and I-6 give the design.)*
- **(H2)** [W2] The parameterised partial Fourier transforms are defined and continuous — automatic: [ÁLKL23] Prop. 4.3 (printed p. 18, read verbatim: "If s < −m̄ − n′/2, then (4.7) has a continuous extension S^{m̄}(N^*U′′) → I^{(s)}(U, L_0). If m̄ > −s − n′/2, then (4.8) induces a continuous linear map I_c^{(s)}(U, L_0) → S^{m̄}(N^*U′′)") is a pair of continuous linear maps between Fréchet spaces, and any such map A : E → F induces a continuous C(T, A) : C(T, E) → C(T, F), a ↦ A ∘ a, with ‖C(T,A)a‖_{q^T} = sup_t q(A a(t)) ≤ sup_t (a continuous seminorm of E)(a(t)).
- **(H3)** [W2] I^m_τ is independent of the atlas and partition of unity, (4.10)_τ is a TVS-embedding, each I^m_τ is **complete** (hence Fréchet: metrizability is clear from (4.10)_τ and (H-chart)), and the symbol and Sobolev filtrations are mutually cofinal (transplant of (4.11)/(4.12)). *In the manifold case the completeness of I^m is cited by [ÁLKL23] to [Mel96], which is not on disk (§1); so this half of (H3) is a genuine open input, in the manifold case as much as in the transplant.* **Two Fréchet-ness statements are, by contrast, source-proved and need no [Mel96]:** (a) the **Sobolev** steps — [ÁLKL23] Prop. 4.1, printed p. 16, read verbatim with its proof this session ("I^{(s)}(M, L) is a totally reflexive Fréchet space"), proved there as a countable projective limit of the Hilbert spaces I_k^{(s)}(M, L); and (b) the **bounds** steps A^m(M̄), by the memoir's own general criterion at [ALKL] §2.1.1, printed p. 9, read verbatim: "Given a linear subspace A of closed operators, densely defined in X and with values in Y, we get the LCS (2.1.1) Z = { u ∈ ∩_{A∈A} dom A | A · u ⊂ Y } with the projective topology given by the maps A : Z → Y (A ∈ A). If Y is a Fréchet space, L(X, Y) ⊂ A and A/L(X, Y) is countably generated, then Z is easily seen to be a Fréchet space." Both criteria are stability statements about countable projective limits, so by Lemma 1.1(a) and §3.3(3) their transplants I^{(s)}_τ = C(T, I^{(s)}) and A^m_τ = C(T, A^m) are Fréchet as well, **unconditionally**. What remains genuinely open in (H3) is the Fréchet-ness (i.e. completeness) of the **symbol-order** steps I^m and I^m_τ, and the atlas-independence of I^m_τ.
- **(H4)** [W1] Each transplanted step space is Hausdorff (immediate from (A-v) and C^{−∞}_τ Hausdorff).

---

## 4. Theorem 1: the transversal is transparent to Wengenroth's criterion

This section is unconditional: it is pure functional analysis about C(T, −), with T compact Hausdorff and no other hypothesis.

### 4.1 The functor

For T compact Hausdorff and E an LCS, let **C(T, E)** be the space of continuous maps T → E with the topology of uniform convergence: a base of 0-neighbourhoods is
  **V^T := { a ∈ C(T, E) : a(T) ⊂ V }**, V a 0-neighbourhood of E,
equivalently the topology of the seminorms p^T(a) = sup_{t∈T} p(a(t)) (finite, since a(T) is compact hence bounded). For a linear subspace or a subset W ⊆ E write W^T := { a ∈ C(T, E) : a(T) ⊆ W }.

**Lemma 1.1 (basic preservation).** Let T be compact Hausdorff.
 (a) If E is Fréchet, so is C(T, E).
 (b) A continuous injection E ↪ F induces a continuous injection C(T, E) ↪ C(T, F).
 (c) If Y ⊆ E is a closed subspace, then C(T, Y) = Y^T is closed in C(T, E) and carries the subspace topology.
 (d) C(T, E_1 × ⋯ × E_r) ≡ C(T, E_1) × ⋯ × C(T, E_r), and likewise for finite direct sums.
 (e) The constants embedding ι : E → C(T, E), ι(e)(t) ≡ e, is a TVS-isomorphism onto a **closed** subspace, and ι(E) ∩ C(T, Y) = ι(Y) for every subspace Y ⊆ E.

*Proof.* (a) If (p_i)_{i∈N} is a countable generating family of seminorms of E, then (p_i^T) generates the topology of C(T, E) and is countable, so C(T, E) is metrizable; it is Hausdorff because E is (evaluate at a point); and it is complete because a uniformly Cauchy net of continuous E-valued maps converges uniformly (E complete) to a map that is again continuous. (b) Compose. Injectivity is pointwise. (c) A uniform limit of maps with values in the closed set Y again has values in Y; the seminorms of C(T, Y) are the restrictions of those of C(T, E). (d) Evaluate componentwise. (e) p^T(ι(e)) = p(e); ι(E) is the kernel of the continuous linear map a ↦ a − ι(a(t_0)) for any fixed t_0 ∈ T, hence closed; the last statement is immediate. ∎

### 4.2 The criterion transfers, verbatim

**Lemma 1.2 (coincidence transfer).** Let E′ ↪ E′′ be a continuous inclusion of LCSs, and let U ⊆ E′ be a subset such that

  (∗) for every 0-neighbourhood V′ of E′ there is a 0-neighbourhood V′′ of E′′ with **U ∩ V′′ ⊆ V′**.

Then U^T ⊆ C(T, E′) satisfies (∗) for the pair C(T, E′) ↪ C(T, E′′). If moreover U is a 0-neighbourhood of E′, then U^T is a 0-neighbourhood of C(T, E′).

*Proof.* Basic 0-neighbourhoods of C(T, E′) are the sets V′^T with V′ a 0-neighbourhood of E′; likewise for E′′. Given V′, choose V′′ by (∗). If a ∈ U^T ∩ V′′^T then for every t ∈ T we have a(t) ∈ U and a(t) ∈ V′′, hence a(t) ∈ U ∩ V′′ ⊆ V′; thus a ∈ V′^T. So U^T ∩ V′′^T ⊆ V′^T. The last sentence is the definition of the topology of uniform convergence. ∎

*Remark.* Property (∗) is exactly what "the topologies of E′ and E′′ coincide on U" means at the origin, which is the form in which Wengenroth's criterion is stated in both quotations of §2.1. For absolutely convex U it upgrades to coincidence at every point of ½U: if w, a ∈ ½U and a − w ∈ V′′ then a − w ∈ ½U − ½U ⊆ U (absolute convexity), so a − w ∈ U ∩ V′′ ⊆ V′. Hence nothing is lost by working with the 0-based form, here or in §4.3.

**Theorem 1 (transversal transparency).** Let T be a compact Hausdorff space and let (E_k)_{k∈N} = (E_0 ⊂ E_1 ⊂ ⋯) be an inductive spectrum of **Fréchet** spaces with continuous inclusions, E = ⋃_k E_k. Put E_{k,τ} := C(T, E_k) and E_τ := ⋃_k E_{k,τ}. Then:

1. each E_{k,τ} is Fréchet, the inclusions E_{k,τ} ⊂ E_{k+1,τ} are continuous, and E_τ is an LF-space;
2. **(E_{k,τ}) is acyclic if and only if (E_k) is acyclic**;
3. in that case E_τ is boundedly, compactly and sequentially retractive, complete, regular and Hausdorff, and barreled, ultrabornological and webbed.

*Proof.* (1) Lemma 1.1(a),(b).

(2) (⟸) Let (E_k) be acyclic. Fix k. By (W-a) choose k′ ≥ k such that for all k′′ ≥ k′ the topologies of E_{k′} and E_{k′′} coincide on some 0-neighbourhood U = U(k′′) of E_k, i.e. (∗) of Lemma 1.2 holds for U. By Lemma 1.2, U^T is a 0-neighbourhood of E_{k,τ} on which the topologies of E_{k′,τ} and E_{k′′,τ} coincide. As k and k′′ were arbitrary, (E_{k,τ}) satisfies (W-a).

(⟹) Let (E_{k,τ}) be acyclic. By Lemma 1.1(e), ι(E_k) = ι(E) ∩ E_{k,τ} is a closed subspace of E_{k,τ} carrying E_k's topology. Acyclicity passes to such subspaces: if the topologies of E_{k′,τ} and E_{k′′,τ} coincide on the 0-neighbourhood U of E_{k,τ} — i.e. (∗) holds — then for the 0-neighbourhood U ∩ ι(E_k) of ι(E_k) we have, for every 0-neighbourhood V′ of E_{k′,τ}, (U ∩ ι(E_k)) ∩ (V′′ ∩ ι(E_{k′′})) ⊆ V′ ∩ ι(E_{k′}), and 0-neighbourhoods of ι(E_{k′}), ι(E_{k′′}) are exactly the traces of 0-neighbourhoods of E_{k′,τ}, E_{k′′,τ}. Hence (ι(E_k)) is acyclic, i.e. (E_k) is.

(3) By (W-b), applicable because the steps E_{k,τ} are Fréchet by (1): acyclic ⟺ boundedly/compactly/sequentially retractive, and acyclic LF-spaces are complete and regular; Hausdorffness follows since each E_{k,τ} is Hausdorff. Barreled, ultrabornological and webbed hold for every countable inductive limit of Fréchet spaces — the reason [ÁLKL23] Prop. 3.1 and Cor. 4.2 give for I(M, L) ("Since S^∞(U × R^l) is an LF-space, we get the following", printed p. 13; "Since every I^{(s)}(M, L) is a Fréchet space (Proposition 4.1), the following analog of Proposition 3.1 holds true by the same reason", printed p. 17) — and that reason uses nothing but Fréchet-ness of the steps. ∎

**Corollary 1.3 (subspaces and finite products).** Under the hypotheses of Theorem 1: if (E_k) is acyclic and Y ⊆ E is a subspace with Y_k := Y ∩ E_k, then (C(T, Y_k)) is acyclic whenever (Y_k) is; and (Y_k) is acyclic whenever (E_k) is [same trace argument as in the proof of (2)(⟹)]. If (E_k^{(1)}), …, (E_k^{(r)}) are acyclic spectra of Fréchet spaces and F is a fixed Fréchet space, then the spectrum (F × ∏_{i≤r} E_k^{(i)})_k is acyclic, and so is any spectrum of subspaces of it of the form (Z ∩ (F × ∏ E_k^{(i)}))_k.

*Proof.* Traces of 0-neighbourhoods, as above; for the product, choose the 0-neighbourhood factorwise and note that the F-factor contributes the same topology at every step, so (∗) holds there trivially. ∎

**This is the whole of the positive answer to W3.** Note what it does *not* need: no Montel-ness, no reflexivity, no compactness of linking maps, no separability, no metrizability of T, and no property of T beyond compactness. In particular **total disconnectedness of T is neither used nor obstructive**.

### 4.3 Assembly for the transplanted conormal spectra

**Theorem 2 (the transplant statement).** Assume (H-chart), (H1)–(H4), and let T_1, …, T_N be the (compact) transversal factors of the finite atlas. Suppose that, for each chart, the manifold-level spectra
 (S^{m̄}_{K_j}(N^*L_j; Ω))_{m̄}, (I^m(U_j, L_{0,j}))_m, (A^m(Ū_j))_m, (Ȧ^m(Ū_j))_m, (K^m(Ū_j))_m
are acyclic (this is exactly what §7 proves). Then the transplanted spectra
 (I^m_τ(X, X⁰))_m, (A^m_τ(X̄))_m, (Ȧ^m_τ(X̄))_m, (K^m_τ)_m, (J^m_τ)_m
are acyclic, and consequently **I_τ, A_τ, Ȧ_τ, K_τ, J_τ are boundedly, compactly and sequentially retractive, complete, regular, Hausdorff, barreled, ultrabornological and webbed LF-spaces.** The same holds for the Sobolev-order spectra, and the two filtrations give the same properties by (W-b) ("the above properties of (X_k) only depend on the LF-space X") together with (H3)'s cofinality.

*Proof.* By (4.10)_τ, I^m_τ is a subspace of the fixed Fréchet space C^∞_τ(X ∖ X⁰) times the finite product ∏_j C(T_j, S^{m̄}_{K_j}(N^*L_j; Ω)), the embedding being the same map for every m. By Theorem 1(2)(⟸) each factor spectrum (C(T_j, S^{m̄}_{K_j}))_{m̄} is acyclic; by Corollary 1.3 the product-with-fixed-factor spectrum is acyclic; and by Corollary 1.3 again the spectrum of subspaces (I^m_τ)_m is acyclic. Fréchet-ness of the steps is (H3). Theorem 1(3) then gives the property package. For A^m_τ, Ȧ^m_τ, K^m_τ the same argument runs through the chart localisation of §3.4 (a finite direct sum of C(T_i, ·)-spaces of the slice objects, the compatibility conditions cutting out a closed subspace because C^{−∞}_τ is Hausdorff by (H4)); for K^m_τ and Ȧ^m_τ one may alternatively use the closed-subspace chain of §2.3 transplanted, since Lemma 1.1(c) preserves closed subspaces. J^m_τ = the extendible side is handled the same way, or by the transplant of Prop. 7.29's surjective topological homomorphism, which is category-level. ∎

**Corollary 2.1 (what the S2 note's rows I-9, I-10(c) and I-13 needed).** Under the hypotheses of Theorem 2:
 (i) I_τ is **compactly retractive**, which is the exact property [ALKL] §5.2.1 consumes ("because I(F) is compactly retractive (Section 2.2.2)", memoir printed p. 118) — and it is obtained **without Montel-ness**, exactly as row I-10(c) of the S2 note proposed;
 (ii) A_τ(X̄) is **boundedly retractive**, which is the exact property [ÁLKL23] Claim 6.43 consumes; and with §7.4's repair, the dual-conormal exactness argument goes through in the transplant;
 (iii) all five spaces are complete and regular, and barreled/ultrabornological/webbed, which is what the De Wilde open-mapping and closed-graph steps of row I-9 consume.

---

## 5. What the transversal genuinely destroys (proved)

Let T be an **infinite** compact Hausdorff space (so C(T) is an infinite-dimensional Banach space) and let E ≠ 0 be a Hausdorff LCS.

### 5.1 Montel-ness and reflexivity die

**Proposition 3.** C(T, E) is neither semi-Montel nor semi-reflexive.

*Proof.* Fix e ∈ E ∖ {0} and, by Hahn–Banach, λ ∈ E′ with λ(e) = 1. The map j : C(T) → C(T, E), f ↦ f·e, is linear and injective, and for every continuous seminorm p of E one has p^T(f e) = ‖f‖_∞ p(e); choosing p with p(e) > 0 (possible, E Hausdorff) shows that j is a TVS-isomorphism of the Banach space C(T) onto its image with the induced topology. The image is closed: it is the kernel of the continuous linear map C(T, E) → C(T, E), a ↦ a − (λ ∘ a)·e. Now semi-Montel-ness and semi-reflexivity are both inherited by closed subspaces, and an infinite-dimensional Banach space is neither semi-Montel (Riesz: its closed unit ball is bounded and not relatively compact) nor semi-reflexive (C(T) is not reflexive for infinite compact T). ∎

**Consequence.** The proofs of the Montel halves of [ÁLKL23] Cor. 3.6, Cor. 4.7, Cor. 6.14, Cor. 6.20 and Cor. 6.25 — each of which closes by embedding into a product of Montel spaces, as quoted in §2.2 for Cor. 4.7 — **cannot** be transplanted, and their conclusions are **false** in the transplant. This is exactly row I-10 of the S2 note ("FAILS — and is not consumed by the sequences"); the note asserted it, and Proposition 3 proves it. The inventory conclusion of that row is untouched by the present note: acyclicity, completeness, retractivity and regularity are all delivered by Theorem 2 without Montel-ness.

### 5.2 The "compact spectrum" shortcut dies

**Proposition 4.** Let S : E → F be a non-zero continuous linear map between Hausdorff LCSs. Then C(T, S) : C(T, E) → C(T, F), a ↦ S ∘ a, is **not** a compact operator (i.e. no 0-neighbourhood of C(T, E) has relatively compact image).

*Proof.* Let V^T be any basic 0-neighbourhood of C(T, E), V balanced. Pick e ∈ V with S e ≠ 0 (possible: V is absorbing and S ≠ 0) and λ ∈ F′ with λ(Se) = 1. For ‖f‖_∞ ≤ 1 the map f e has values in V (V balanced), so { f e : ‖f‖_∞ ≤ 1 } ⊆ V^T. Its image under C(T, S) is { f·Se }. The map C(T, F) → C(T), a ↦ λ ∘ a, is continuous and sends f·Se to f. If C(T, S)(V^T) were relatively compact, the closed unit ball of C(T) would be relatively compact, contradicting Riesz for infinite T. ∎

**Consequence.** The route to acyclicity recorded at [ÁLKL23] §2 p. 4 and [ALKL] §2.1.1 p. 9 — "(X_k) is compact if the inclusion maps are compact operators. In this case, (X_k) is clearly acyclic" — is unavailable in the transplant **even if it were available upstream**. Row I-8 of the S2 note guessed exactly this ("[ÁLKL23]'s acyclicity does NOT route through compact embeddings"); Proposition 4 turns the guess into a theorem about the transplanted spectra and shows that the topology/interpolation route of §7 is the only one on offer.

---

## 6. The refutation: the coincidence statements are false

Everything in this section is verified in **both** [ÁLKL23] v1 (on disk) and v3 (fetched this session); §3 of the two versions is textually identical.

### 6.1 The counterexample

Work with U = R^0 = {0} and l = 1, so that (per [ÁLKL23] p. 13, "The notation S^m(R^l) … is used when U = R^0 = {0}; in this case, the subscripts K and α are omitted") the space S^m(R) consists of a ∈ C^∞(R) with
  ‖a‖_{β,m} = sup_{ξ∈R} |a^{(β)}(ξ)| / (1 + |ξ|)^{m−β} < ∞ for all β ∈ N_0.
(The example is constant in x if one prefers U ⊆ R^n; nothing changes.)

Fix ψ ∈ C_c^∞(R) with supp ψ ⊂ [1, 2] and ψ(3/2) = 1, and set, for N ∈ N,

  **a_N(ξ) := N · ψ(ξ/N).**

**Claim 6.1.** (i) a_N ∈ S^0(R) for every N. (ii) ‖a_N‖_{Q,C^k} = 0 for every compact Q ⊂ R and every k, as soon as N > sup{|ξ| : ξ ∈ Q}. (iii) ‖a_N‖′_{β,0} = 0 for every β and every N. (iv) ‖a_N‖_{0,0} = N‖ψ‖_∞ → ∞. (v) ‖a_N‖_{0,1} = sup_ξ N|ψ(ξ/N)|/(1 + |ξ|) → ‖ψ‖_∞ ≠ 0 and, more generally, for every β, ‖a_N‖_{β,1} = sup_ξ |N^{1−β}ψ^{(β)}(ξ/N)| (1+|ξ|)^{β−1} is bounded above and below by positive constants independent of N. **(vi)** a_N ∈ C_c^∞(R), hence a_N ∈ S^{−∞}(R) = ∩_{m} S^m(R): *every* a_N lies in *every* step of the filtration.

*Proof.* (i) a_N^{(β)}(ξ) = N^{1−β}ψ^{(β)}(ξ/N), supported in [N, 2N], so ‖a_N‖_{β,0} = sup |N^{1−β}ψ^{(β)}(ξ/N)|(1+|ξ|)^{β} ≤ N^{1−β}‖ψ^{(β)}‖_∞ (1+2N)^β < ∞. (ii) supp a_N ⊂ [N, 2N] is disjoint from Q. (iii) Every a_N^{(β)} has compact support, so the limsup as |ξ| → ∞ vanishes identically. (iv) Immediate. (v) On supp a_N^{(β)} one has 1 + |ξ| ≍ N, so ‖a_N‖_{β,1} ≍ N^{1−β}·N^{β−1} = 1. (vi) a_N is smooth with support in [N, 2N]; by [ÁLKL23] (3.3), read verbatim at printed p. 13, "C_cv^∞(U × R^l) ⊂ S^{−∞}(U × R^l)". ∎

**Why (vi) matters.** Because all a_N lie in the *single* step S^m for every m, the family refutes Cor. 3.4 for **every** admissible pair m < m′ at once, and in the strongest possible form: not "the topologies differ on a large step" but "they differ on the smallest step there is". This also separates the counterexample from [ÁLKL23]'s own Remark 3.8 (printed p. 15, read verbatim: "Let a_m ∈ S^∞(U × R^l) (m ∈ N_0) such that a_m(x, ξ) = 0 if |ξ^1| ≤ m, and a_m(x, ξ) = (ξ^1 − m)^m if |ξ^1| ≥ m + 1. Then a_m ∈ S^m(U × R^l) ∖ S^{m−1}(U × R^l) and a_m → 0 in C^∞(U × R^l) as m ↑ ∞. However a_m ↛ 0 in S^∞(U × R^l); otherwise, since S^∞(U × R^l) is sequentially retractive (Corollary 3.6), all a_m would lie in some step S^{m_0}(U × R^l), a contradiction"), whose family deliberately **escapes** the filtration (a_m ∈ S^m ∖ S^{m−1}) and therefore does *not* contradict Cor. 3.4. Remark 3.8 is correct and survives — it consumes only sequential retractivity, which §7 restores.

### 6.2 [ÁLKL23] Prop. 3.2 is false, and its completeness step fails

By Claim 6.1(ii),(iii), a_N → 0 in the topology generated by (3.4) and (3.5) with m = 0. By Claim 6.1(iv), a_N does not converge to 0 in S^0(R); it is not even bounded there. Hence:

> **Theorem 5 (refutation of Prop. 3.2).** The seminorms (3.4) and (3.5) do **not** describe the topology of S^m(U × R^l). The identity map S^m → S′^m is continuous but not open. ∎

The failure is located precisely at the emphasised sentence of the quoted proof, "‖φ(a)‖′_{K,α,β,m} = ‖a‖′_{K,α,β,m}": the left-hand side is the *formula* (3.5) evaluated at the C^∞-limit φ(a), whereas the right-hand side is the *continuous extension* of that seminorm to the abstract completion, and the two need not agree, because (3.5) is not a supremum of C^∞-continuous linear functionals (it is a supremum of limsups, and a limsup is only upper semicontinuous under the relevant limits — it can drop in the limit, never rise).

**A second, independent gap in the same sentence.** Even granting the equality of the two sides, the printed conclusion "there are C, R > 0 so that, if x ∈ K and |ξ| ≥ R, then |∂_x^α∂_ξ^β φ(a)(x, ξ)| / (1 + |ξ|)^{m−|β|} ≤ C" does **not** follow from the finiteness of (3.5). The quantity (3.5) is sup_{x∈K} limsup_{|ξ|→∞}(…): for each *individual* x, finiteness of the limsup gives a threshold R(x), but a supremum over x of finite limsups gives no **uniform** R over K.

> **Counterexample to the inference (and a second witness for Theorem 5′).** Take n = l = 1, U = (−1, 2), K = [0, 1], χ ∈ C_c^∞(R) with supp χ ⊂ (−1, 1) and χ(0) = 1, and set
>  **b(x, ξ) := x^{−1} χ(ξ − x^{−1}) for x > 0,  b(x, ξ) := 0 for x ≤ 0.**
> *b is smooth*: near any (0, ξ_0) one has ξ − x^{−1} < −1 for all ξ in a neighbourhood of ξ_0 and all small x > 0, so b vanishes identically there; away from x = 0 it is a composition of smooth maps. *All (3.5)-seminorms of b vanish*: for each fixed x > 0, b(x, ·) and all its derivatives have compact ξ-support, so every limsup_{|ξ|→∞} is 0; and b ≡ 0 for x ≤ 0. *All (3.4)-seminorms of b are finite*: they are suprema over compact Q ⊂ U × R, and b is smooth. *Yet the printed conclusion fails at m = 0, α = β = 0*: for every R, taking x = 1/ξ with ξ ≥ R gives |b(x, ξ)|/(1 + |ξ|)^0 = ξ → ∞, so no pair (C, R) exists, and b ∉ S^0(U × R).
>
> The same b witnesses Theorem 5′ over a base of positive dimension: with a cutoff ρ_N ∈ C^∞(U), ρ_N ≡ 1 on {x ≥ 2/N}, ρ_N ≡ 0 on {x ≤ 1/N}, the functions b_N := ρ_N b lie in S^0(U × R), and b_N → b in S′^0(U × R) (all (3.5)-seminorms of b − b_N vanish; each (3.4)-seminorm over a compact Q ⊆ K̃ × {|ξ| ≤ M} vanishes once 1/N < 1/(M + 1), because b itself vanishes there). So (b_N) is a Cauchy sequence of S′^0 whose only possible limit, b, is not in S^0: **S′^0(U × R^l) is not complete**, over any base of dimension ≥ 1, by an example that is not a rescaling family at all.

So the argument would need repair even if the completion step were sound. It is not sound; here is the zero-dimensional-base version of that failure, which is the shortest:

**Theorem 5′ (S′^m is not complete).** Let c_N := ∑_{j=1}^{N} 4^j ψ(ξ/4^j) ∈ S^0(R) (the summands have pairwise disjoint supports [4^j, 2·4^j]). Then (c_N) is Cauchy in S′^0(R) and has no limit in S^0(R); a fortiori the completion Ŝ′^0 contains a point a with ‖a‖′_{β,0} = 0 for all β while ‖φ(a)‖′_{β,0} = +∞.

*Proof.* For N > M, c_N − c_M = ∑_{M<j≤N} 4^j ψ(·/4^j) is compactly supported in [4^{M+1}, ∞), so all (3.5)-seminorms of it vanish, and all (3.4)-seminorms vanish once 4^{M+1} exceeds the radius of the compact Q; hence (c_N) is Cauchy in S′^0 (indeed for each of the countably many generating seminorms it is eventually stationary at 0). The inclusion S′^0 ⊂ C^∞(R) is continuous (the (3.4)-seminorms *are* the C^∞-seminorms), and c_N → c := ∑_{j≥1} 4^j ψ(·/4^j) in C^∞(R) (locally finite sum). If (c_N) had a limit u ∈ S^0 in S′^0, then c_N → u in C^∞, so u = c; but sup|c| = sup_j 4^j = ∞, so c ∉ S^0. Contradiction. For the last assertion, take a := lim c_N in Ŝ′^0: the extended seminorms satisfy ‖a‖′_{β,0} = lim_N ‖c_N‖′_{β,0} = 0, whereas φ(a) = c has ‖c‖′_{β,0} = limsup_{|ξ|→∞}|c^{(β)}(ξ)||ξ|^{β} = limsup_j 4^{j(1−β)}·4^{jβ}|ψ^{(β)}| = ∞. ∎

### 6.3 [ÁLKL23] Cor. 3.4, Cor. 4.5, Prop. 6.10, Cor. 6.12, Cor. 6.24 are false as stated

> **Theorem 6.** (a) For m < m′, the topologies of S^{m′}(U × R^l) and C^∞(U × R^l) do **not** coincide on S^m(U × R^l). (b) The topologies of S^{m′} and S^{m′′} do not coincide on S^m for m < m′ < m′′. (c) The corresponding statements for the conormal spaces, [ÁLKL23] Cor. 4.5, and for the bounds filtration, [ÁLKL23] Prop. 6.10 and Cor. 6.12 (v3: Prop. 6.12, Cor. 6.14), and for K, Cor. 6.24, are false as stated. (d) The transplanted versions of all of these are false as well.

*Proof.* (a) With m = 0, m′ = 1 the sequence (a_N) of §6.1 lies in S^0, converges to 0 in C^∞ by Claim 6.1(ii), and does not converge to 0 in S^1 by Claim 6.1(v). (b) Same sequence, rescaled: put b_N := N^{m′}ψ(·/N)/N^{0}, i.e. b_N(ξ) := N^{m′} ψ(ξ/N). Then ‖b_N‖_{β,m′} ≍ 1 for every β, while ‖b_N‖_{β,m′′} ≍ N^{m′−m′′} → 0 and each b_N lies in S^m; so b_N → 0 in S^{m′′} but not in S^{m′}, while all b_N lie in S^m. (c) For the conormal spaces, transport (a) or (b) through a chart via the partial inverse Fourier transform (4.7)–(4.8) and a cutoff, using [ÁLKL23] Prop. 4.3 in both directions and the fact that (4.10) is by construction a TVS-embedding: a family of symbols witnessing (b) in the S^{m̄}-factor witnesses the failure in I^m. For the bounds filtration there are two independent routes, and both are given.

**(c1) Transport along the source's own model identification.** [ÁLKL23] Example 6.9, printed p. 30, read verbatim this session: "**Example 6.9** ([25, Exercises 4.2.23 and 4.2.24]). Via the injection of R^l into its stereographic compactification S^l_+ = { x ∈ S^l | x^{l+1} ≥ 0 }, the space A^{−m}(S^l_+) corresponds to the symbol space S^m(R^l) (Section 3)." Under that correspondence the seminorm families (6.40)/(6.41)/(6.42) of A^{−m} correspond to (3.1)/(3.4)/(3.5) of S^m — decay at the boundary {x = 0} of the compactification *is* growth in ξ. Hence the family a_N of §6.1, transported, refutes Prop. 6.10 and Cor. 6.12 on the **compact** manifold-with-boundary S^l_+ with no further computation. This is the cleanest form of the refutation for the bounds filtration, and it is anchored in the source's own statement rather than in a model of my choosing.

**(c2) A direct collar witness, for a general M̄.** In the collar M̄ ⊃ (0, 1)_x × Y with x a boundary-defining function, fix χ ∈ C_c^∞((1, 2)) with χ(3/2) = 1, fix the target order m′, and put
  u_N(x, y) := c_N · χ(Nx),  **c_N := N^{1−m′}**,  supp u_N ⊂ {1/N < x < 2/N}.
For every P_k ∈ Diff_b(M̄) one has |P_k u_N| ≤ C_k c_N (a b-vector field x∂_x costs nothing: x ≍ 1/N while ∂_x costs N; the Y-directions cost nothing at all, u_N being constant in y). Then: (6.42) gives ‖u_N‖′_{k,m} = 0 for every m and every N (for fixed N the support is bounded away from x = 0, so the ε ↓ 0 limit is a supremum over an empty region); (6.41) gives ‖u_N‖_{K,k,m} = 0 for every compact K ⊂ M̊̄ once N is large; each u_N lies in **every** A^m(M̄), being smooth and compactly supported in M̊̄ (the exact analogue of Claim 6.1(vi)); and
  ‖u_N‖_{k,m′} = sup_{M̊̄} x^{−m′}|P_k u_N| ≍ c_N N^{m′} = N → ∞ .
Taking m′ = m refutes **Prop. 6.10**: all the (6.41)- and (6.42)-seminorms of u_N vanish for large N while ‖u_N‖_{0,m} → ∞, so those two families do not describe the topology of A^m(M̄). Taking any m′ < m refutes **Cor. 6.12**: u_N → 0 in C^∞(M̊̄), all u_N lie in A^m(M̄), and ‖u_N‖_{k,m′} → ∞, so the topologies of A^{m′}(M̄) and C^∞(M̊̄) do not coincide on A^m(M̄). The direction of the inclusions is as the source has it — [ÁLKL23] (6.37), printed p. 31, read verbatim: "A^m(M) ⊂ A^{m′}(M) (m′ < m)" — so the *smaller* m′ names the *larger* step, and the witness is correctly placed. Cor. 6.24 is asserted with "formally the same proof" from Cor. 4.5 through the closed-subspace chain of §2.3, so it inherits the refutation of its stated derivation; and the closed-subspace chain carries the counterexample itself once the witnesses are taken supported near ∂M. (d) The witnesses are constant in t, so they lie in C(T, ·) and have the same seminorms there (sup over t of a constant). ∎

### 6.4 A further defect the transplant must avoid: non-compact base

> **Theorem 7.** For U ⊂ R^n open and non-compact, the spectrum (S^k(U × R^l))_{k∈N} is **not** acyclic; hence [ÁLKL23] Cor. 3.6 requires a compactness (or fixed-compact-support) hypothesis on the base.

*Proof.* Let U be a 0-neighbourhood of S^k: it contains a basic one determined by finitely many seminorms, hence by a single compact K̃ ⊂ U (the union of the finitely many) and a finite set of multi-indices. Choose p ∈ U ∖ K̃ and χ ∈ C_c^∞(U ∖ K̃) with χ(p) = 1, and set a_N(x, ξ) := N^{k′} χ(x) ψ(ξ/N) with ψ as in §6.1. Then all seminorms of a_N with base compact K̃ vanish, so a_N ∈ U for every N and every δ; a_N ∈ S^k; for every (α, β), ‖a_N‖_{K,α,β,k′′} ≍ N^{k′−k′′} → 0 for any compact K, so a_N lies eventually in every 0-neighbourhood of S^{k′′}; and ‖a_N‖_{K_p,0,0,k′} ≍ 1 for K_p a compact neighbourhood of p. So U ∩ (0-neighbourhood of S^{k′′}) ⊄ {‖·‖_{K_p,0,0,k′} < ½}, and (W-a) fails for every choice of k′, k′′ and U. ∎

Since the foliated-space charts of (H-chart) have non-compact U_i ⊂ R^3, **the transplanted localisation (4.10)_τ must use symbol spaces of fixed compact base support**, as it was written in §3.4. That is legitimate and in fact forced by the construction: the symbols a_j come from ρ_j u with ρ_j compactly supported, so a_j has base support inside the fixed compact K_j = supp ρ_j ∩ X⁰. On such a subspace the seminorms with K = K_j alone describe the topology, and the base is effectively compact. The same reading repairs the manifold-level (4.10).

### 6.5 A complete consumer audit: what is damaged, what is repaired here, what is untouched

The refutation is only useful if one knows exactly what rested on the false statements. This section reports a **mechanical** audit, not an impressionistic one: the `pdftotext -layout` extractions of [ÁLKL23] v1 and of the 176-page memoir [ALKL] were searched this run for every occurrence of the strings "coincide on", "Corollary 3.4", "Corollaries 3.4", "Corollary 4.5", "Corollaries 4.5", "Corollary 6.12", "Corollary 6.19", "Corollaries 6.19", "Corollary 6.24", "Corollaries 6.23", "Corollary 7.20". The audit below lists **every** hit. (Its one blind spot is named at the end: an implicit re-use hidden inside a phrase such as "with formally the same proof". Those phrases were followed wherever they occur in the enumerated hits.)

**A. Every occurrence of a coincidence statement in [ÁLKL23] v1.** Definition of acyclicity, §2 p. 4 (twice — that is Wengenroth's criterion itself, not a claim about symbols); **Cor. 3.4**, p. 14; the bounded-set use inside the proof of **Cor. 3.6**, p. 15; **Cor. 4.5**, p. 19; **Cor. 6.12**, p. 31; **Cor. 6.19**, p. 32; **Cor. 6.24**, p. 33; **Cor. 7.18** (J^m(M, L) vs C^∞(M ∖ L)), p. 45; **Cor. 7.20** (K^m(M, L)), p. 45. In [ALKL]: the definition at §2.1.1 p. 9 (twice), and three *restatements imported from* [ÁLKL23] — §2.1.8 p. 15 (symbols), §2.5.10 p. 38 (A(M̄)), §2.6.7 p. 44 (J(M, L)). **The memoir never uses a coincidence statement in a proof of its own**: all three memoir hits are declarative sentences of the form "The following properties hold [ÁLKL23, …]".

**B. Every consumer of Cor. 3.4 inside [ÁLKL23] v1**, with the verdict of this note.

| Site (v1) | What it uses Cor. 3.4 for | Verdict |
|---|---|---|
| Proof of **Cor. 3.5**, p. 14 ("The first assertion is given by Corollary 3.4 and the density of C_c^∞(U × R^l) in C^∞(U × R^l)") | density of C_c^∞ in S^m with the S^{m′}-topology | **Statement TRUE, published proof INVALID.** Re-proved directly in Lemma 6.5.1 below. *(The first draft of this note recorded density as "unaffected"; that was wrong — the source really does derive it from the false corollary. The statement survives; the derivation does not.)* |
| Proof of **Cor. 3.6**, p. 15, first sentence ("Corollary 3.4 gives the property of being acyclic") | acyclicity of (S^m) | **INVALID.** Replaced by Theorem 8 (§7.2), for a compact — or fixed-compact-support — base; and *false* for a non-compact base (Theorem 7). |
| Proof of **Cor. 3.6**, p. 15, last paragraph ("the topologies of S^∞ and S^m coincide on B … By Corollary 3.4, it follows that B is a complete bounded subspace of C^∞") | semi-Montel-ness | **VALID**, because here Cor. 3.4 is applied to a **bounded** set B, and the bounded-set form of the statement is true (Lemma 6.5.2). |
| **Rem. 3.8**, p. 15 | rhetorical ("Despite of Corollary 3.4 …") | **Unaffected**; the remark's own argument consumes only sequential retractivity (Cor. 3.6), restored in §7. |
| Proof of **Cor. 4.5**, p. 19 ("Use Corollary 3.4 and the TVS-embeddings (4.10)") | the conormal coincidence statement | **INVALID and the statement is FALSE** (Theorem 6(c)). |
| §3 closing paragraph, p. 15 ("Propositions 3.2 and 3.3 and Corollaries 3.4 to 3.6 can be directly extended to this setting" — symbols on a vector bundle) and §6.10, p. 31 ("The proofs of the following results are similar to the proofs of Propositions 3.2 and 3.3 and Corollaries 3.4 to 3.6, using (6.32)") | wholesale transport of the §3 package | **INVALID for the coincidence half; the acyclicity conclusions are restored** by Theorems 8–9. |

**C. Every consumer of the downstream coincidence statements.** Cor. 4.5 is cited twice: in the proof of **Cor. 4.7** ("by Corollaries 4.2 and 4.5") — acyclicity, restored by Cor. 9.1 — and at p. 32 to produce **Cor. 6.19** — likewise. Cor. 6.19 is cited once, in the derivation of **Cor. 6.20** — acyclicity again. Cor. 6.24 and Cor. 7.20 are cited only for the corresponding acyclicity corollaries (6.25 and 7.21). **Cor. 6.12 is cited exactly twice**: at p. 31 in the rhetorical Rem. 6.15-adjacent sentence ("The obvious analog of Remark 3.8 makes sense for (6.32) and Corollary 6.12"), and at p. 39 **inside the proof of Claim 6.43** — the single place in either document where a coincidence statement does real work that is not the word "acyclic". That is why §7.4 exists.

**Lemma 6.5.1 (repair of [ÁLKL23] Cor. 3.5; density, proved directly).** For m < m′, C_c^∞(U × R^l) is dense in S^m(U × R^l) with the topology of S^{m′}(U × R^l).

*Proof.* Two independent truncations.

*(ξ-truncation.)* Fix χ ∈ C_c^∞(R^l) with χ ≡ 1 on {|ξ| ≤ 1} and supp χ ⊆ {|ξ| ≤ 2}, and for R ≥ 1 put a_R(x, ξ) := χ(ξ/R) a(x, ξ). Then a − a_R = (1 − χ(ξ/R)) a is supported in {|ξ| ≥ R}. By Leibniz, ∂_x^α ∂_ξ^β[(1 − χ(ξ/R))a] = Σ_{β′ ≤ β} C_{β′} ∂_ξ^{β′}(1 − χ(ξ/R)) · ∂_x^α ∂_ξ^{β−β′} a. For β′ = 0 the factor is bounded by 1. For β′ ≠ 0, ∂_ξ^{β′}(1 − χ(ξ/R)) = −R^{−|β′|} χ^{(β′)}(ξ/R) is supported in {R ≤ |ξ| ≤ 2R}, where 1 + |ξ| ≍ R, so |∂_ξ^{β′}(1 − χ(ξ/R))| ≤ C (1 + |ξ|)^{−|β′|}. Since a ∈ S^m, |∂_x^α ∂_ξ^{β−β′} a| ≤ ‖a‖_{K,α,β−β′,m}(1 + |ξ|)^{m−|β|+|β′|}. Multiplying, every term is ≤ C(1 + |ξ|)^{m−|β|} with C a finite sum of ‖a‖_{K,α,·,m}. Hence, on {|ξ| ≥ R},
  |∂_x^α∂_ξ^β(a − a_R)| / (1 + |ξ|)^{m′−|β|} ≤ C (1 + |ξ|)^{m−m′} ≤ C R^{m−m′} → 0 (R → ∞),
i.e. ‖a − a_R‖_{K,α,β,m′} → 0 for every K, α, β. So a_R → a in S^{m′}.

*(x-truncation.)* A basic 0-neighbourhood of S^{m′} is cut out by finitely many seminorms, hence by a single compact K ⊂ U. Choose φ ∈ C_c^∞(U) with φ ≡ 1 on a neighbourhood of K; then a_R − φ a_R vanishes on K × R^l, so all those seminorms vanish on it. Thus φ a_R ∈ C_c^∞(U × R^l) lies in any prescribed S^{m′}-neighbourhood of a_R. Combining, C_c^∞ is S^{m′}-dense in S^m. ∎

*Remark.* [ÁLKL23] Rem. 3.7 ("Another proof of Corollary 3.5 could be given like in Proposition 6.8") and Rem. 6.15 ("Proposition 6.8 provides an alternative direct proof of Corollary 6.13") already point at coincidence-free proofs of the density statements; Lemma 6.5.1 supplies one explicitly for the symbol case, and the same two truncations (in x near ∂M̄, and by Prop. 6.8's weighted-L^∞ argument, which is read verbatim in the source at printed pp. 30–31 and uses **no** coincidence statement) give the A^m and I^m analogues. **So all density inputs of the S2 note's rows I-7 and I-13 survive** — but by this proof, not by the source's.

**Lemma 6.5.2 (the true, bounded-set form of the coincidence statement).** For m < m′ and every **bounded** B ⊆ S^m(U × R^l), the topologies of S^{m′}(U × R^l) and of C^∞(U × R^l) coincide on B.

*Proof.* Let C_{α,β} := sup_{a∈B} ‖a‖_{K,α,β,m} < ∞. For a ∈ B, R ≥ 1,
  ‖a‖_{K,α,β,m′} ≤ max( sup_{|ξ|≥R} C_{α,β}(1+|ξ|)^{m−m′}, (1+R)^{|β|−m′} ‖a‖_{K×B̄_R, C^{|α|+|β|}} )
  ≤ max( C_{α,β} R^{m−m′}, (1+R)^{|β|−m′} ‖a‖_{K×B̄_R, C^{|α|+|β|}} ) .
Given ε > 0 choose R with C_{α,β}R^{m−m′} < ε; the remaining term is a C^∞-seminorm times a constant. So on B the S^{m′}-topology is weaker than (hence, by (3.3), equal to) the C^∞-topology. ∎

This is exactly the form the proof of Cor. 3.6 uses for semi-Montel-ness, so **the Montel halves of the manifold-level corollaries survive** once acyclicity is available from §7. (They still die under the transplant, by Proposition 3 — for a different and genuine reason.)

**What is untouched.** [ALKL]'s Theorems 1.3.3 and 1.3.6 and the sequences (1.3.1)/(1.3.2) rest on the exactness statements Cor. 7.30 (via Prop. 7.29, which does not use a coincidence statement) and Prop. 6.42 / Prop. 8.8 (via Claim 6.43, repaired in §7.4), together with retractivity and density, which are restored above and in §7. The memoir's own arguments that consume anything from this circle consume **compact retractivity** — [ALKL] §5.2.1, printed p. 118, read verbatim this session: "{α, d_F β_l}_l is contained and compact in some step I^{(s′)}(F) (s′ ≤ s) because I(F) is compactly retractive (Section 2.2.2)"; and §5.5.3, printed p. 124: "Using that J(F) is compactly retractive (Section 2.6.7) and arguing like in Section 5.2.1 …"; and §5.5.4: "Since I(F) is compactly retractive, C^∞(M; ΛF) is dense in I(F) and every I^{(s)}(F) is a Fréchet space (Section 2.2.2)". Compact retractivity is **equivalent to acyclicity** for LF-spaces with Fréchet steps ([Wen03, Prop. 6.4] as quoted in §2.1), and acyclicity is what §7 restores. **Nothing in the material read this session shows the memoir's conclusions to be in doubt.**

**The blind spot, stated exactly.** The audit above is complete for the *explicit* cross-references listed in A–C, over the whole of [ÁLKL23] v1 and the whole of [ALKL], as extracted by `pdftotext -layout`. It is **not** a semantic audit: a proof that silently re-runs the argument of Cor. 3.4 without naming it would not be caught, and neither would a use hidden in a phrase of the form "with formally the same proof" attached to a statement I did not enumerate. I read [ÁLKL23] §§2–4, §6.8–§6.15, §6.23–§6.25, §7.1 and the memoir sections listed in §1 in full; the remaining pages I searched but did not read. This residual is logged in §10 and §12.

---

## 7. The repair: acyclicity, proved by interpolation, and transplanted

The purpose of this section is to supply the manifold-level input that Theorem 2 assumes and that §6 removed. The proofs are written so that every estimate is **pointwise in the base point** — which is what makes them survive Theorem 1 unchanged.

### 7.1 The interpolation input

**Lemma 7.1 (Landau, one variable, with proof).** Let g ∈ C^2(I) on an interval I of length L. Then sup_I |g′| ≤ (4/L) sup_I |g| + (L/4) sup_I |g″|.
*Proof.* Fix ξ ∈ I and 0 < h ≤ L/2 such that [ξ, ξ+h] ⊆ I or [ξ−h, ξ] ⊆ I; Taylor gives g(ξ ± h) = g(ξ) ± h g′(ξ) + (h²/2) g″(θ), so |g′(ξ)| ≤ 2 sup|g|/h + (h/2) sup|g″|. Take h = L/2. ∎

**Lemma 7.2 (Landau–Kolmogorov on a cube; iterated form).** For N ≥ 1 and M ∈ N there is C = C(N, M) such that for every f ∈ C^M(Q_2) (Q_r = (−r, r)^N), every 0 < h ≤ 1 and every multi-index γ with |γ| = j ≤ M,
  sup_{Q_1} |∂^γ f| ≤ C ( h^{−j} sup_{Q_2}|f| + h^{M−j} max_{|γ′|=M} sup_{Q_2}|∂^{γ′}f| ),
and consequently, optimising h,
  sup_{Q_1} |∂^γ f| ≤ C ( (sup_{Q_2}|f|)^{1−j/M} (max_{|γ′|=M} sup_{Q_2}|∂^{γ′}f|)^{j/M} + sup_{Q_2}|f| ).
*Status.* The two-term form follows from Lemma 7.1 applied coordinatewise on a nested family of cubes with geometrically decreasing steps; this is the classical iteration. I have **not** read it from a source on disk, so it is tagged **[RU-standard]** in §10: it is elementary calculus and re-provable, but this note does not contain its full induction. The optimisation step is: if sup|f| ≤ max|∂^{γ′}f| take h = (sup|f| / max|∂^{γ′}f|)^{1/M} ≤ 1, otherwise take h = 1.

### 7.2 Acyclicity of the symbol spectrum over a compact base

**Theorem 8.** Let l ≥ 0 and let the base be one of

- **(B1)** a **compact** manifold Y (possibly with boundary), or
- **(B2)** a **fixed compact** K ⊂ U ⊂ R^n with a chosen compact neighbourhood K^+ ⊂ U, in which case put
   **S^m_K(U × R^l) := { a ∈ S^m(U × R^l) : a(x, ξ) = 0 for x ∉ K }**, a closed subspace of S^m(U × R^l), whose subspace topology is described by the single compact-base family ‖·‖_{K^+,α,β,m} alone (for any compact K̃ ⊂ U, ‖a‖_{K̃,α,β,m} = ‖a‖_{K̃∩K,α,β,m} ≤ ‖a‖_{K^+,α,β,m}).

In either case write S^m(Y × R^l) for the resulting Fréchet space, whose seminorms are indexed by (α, β) alone. Then the spectrum (S^k(Y × R^l))_{k∈Z} is **acyclic** in the sense of (W-a). Consequently S^∞(Y × R^l) := ∪_k S^k(Y × R^l) is boundedly, compactly and sequentially retractive, complete, regular and Hausdorff.

*(Case (B2) is the one the transplant actually needs, by §6.4: the foliated-space charts have non-compact bases, and Theorem 7 says the full symbol spectrum over such a base is not acyclic. Case (B2) is also exactly what the source's own localisation delivers, because the symbols a_j of (4.10) come from f_j u with f_j compactly supported.)*

*Proof.* We verify (W-a) with k′ := k + 1 (any k′ > k does), and with the 0-neighbourhood
  **U_δ := { a ∈ S^k(Y × R^l) : ‖a‖_{0,0,k} < δ }**, δ > 0 arbitrary and fixed first.
Fix k′′ ≥ k′; if k′′ = k′ there is nothing to prove, so assume k′′ > k′. Fix a target seminorm ‖·‖_{α,β,k′}, put j := |α| + |β|, and fix ε > 0. Choose
  **M := ⌈ j (k′′ − k) / (k′ − k) ⌉**, θ := j/M ∈ (0, 1].
Let C = C(n, l, M, r_0, k) be the constant produced by the interpolation step below; it depends only on data already fixed (never on η, a or ξ_0). Now set **R := max(2, (2Cδ/ε)^{1/(k′−k)})**, and let η > 0 be chosen at the end. Put
  **W_η := { a ∈ S^{k′′} : ‖a‖_{α′,β′,k′′} < η for all |α′| + |β′| ≤ M }**,
a 0-neighbourhood of S^{k′′}. We claim U_δ ∩ W_η ⊆ { ‖·‖_{α,β,k′} ≤ ε }, which is (∗) and hence (W-a).

Let a ∈ U_δ ∩ W_η and fix ξ_0 ∈ R^l with ρ := 1 + |ξ_0| ≥ max(2, R). Work in a chart of Y, in a coordinate ball of a fixed radius r_0 > 0 — uniform over Y by compactness in case (B1); in case (B2) take r_0 := ½ dist(K, R^n ∖ K^+) > 0, so that B(x_0, 2r_0) ⊂ K^+ for every x_0 ∈ K and the W_η-bounds, which are suprema over K^+, are available there — and rescale:
  F(z, w) := ρ^{−k} a(x_0 + r_0 z, ξ_0 + (ρ/4) w), (z, w) ∈ Q_2 ⊂ R^{n} × R^{l}.
On this region 1 + |ξ| ∈ [¾ρ, (5/4)ρ], so:
- from a ∈ U_δ: |F| ≤ δ (5/4)^{|k|} =: C_1 δ on Q_2;
- from a ∈ W_η: for |γ′| = |(α′, β′)| = M, |∂_z^{α′}∂_w^{β′} F| = r_0^{|α′|}(ρ/4)^{|β′|}ρ^{−k}|∂_x^{α′}∂_ξ^{β′}a| ≤ C_2 η ρ^{|β′|−k}·ρ^{k′′−|β′|} = C_2 η ρ^{k′′−k}.
Lemma 7.2 with |γ| = j ≤ M gives on Q_1
  |∂_z^{α}∂_w^{β} F| ≤ C_3 [ (C_1δ)^{1−θ} (C_2 η ρ^{k′′−k})^{θ} + C_1 δ ].
Unwinding the scaling, |∂_x^α∂_ξ^β a(x_0, ξ_0)| = r_0^{−|α|}(4/ρ)^{|β|}ρ^{k}|∂_z^α∂_w^β F| ≤ C ρ^{k−|β|}[ δ^{1−θ}η^{θ}ρ^{(k′′−k)θ} + δ ], with C = C(n, l, M, r_0, k). Now:
- the first term is ≤ C δ^{1−θ}η^{θ} ρ^{k−|β|+(k′′−k)θ} ≤ C δ^{1−θ}η^{θ} ρ^{k′−|β|}, because (k′′−k)θ ≤ k′−k by the choice of M and ρ ≥ 1;
- the second term is C δ ρ^{k−|β|} = C δ ρ^{k−k′} ρ^{k′−|β|} ≤ (ε/2) ρ^{k′−|β|}, because ρ ≥ R.
Choosing η so small that C δ^{1−θ} η^{θ} ≤ ε/2 (possible since θ > 0 is fixed before η) gives
  |∂_x^α∂_ξ^β a(x_0, ξ_0)| ≤ ε ρ^{k′−|β|} ≤ C_4 ε (1+|ξ_0|)^{k′−|β|} for all |ξ_0| ≥ max(2, R) − 1.
For 1 + |ξ_0| ≤ max(2, R) use the W_η bound directly (note (α, β) is among the indices of W_η since j ≤ M): |∂_x^α∂_ξ^β a| ≤ η (1+|ξ_0|)^{k′′−|β|} ≤ η max(2, R)^{k′′−k′}(1+|ξ_0|)^{k′−|β|} ≤ ε(1+|ξ_0|)^{k′−|β|} after shrinking η once more. Hence ‖a‖_{α,β,k′} ≤ C_4 ε. Since a finite intersection of target seminorm conditions is handled by taking the largest M and the smallest η, and since C_4 depends on nothing that was chosen after ε, (∗) of Lemma 1.2 holds for the pair S^{k′} ↪ S^{k′′} on U_δ, and (W-a) is verified. The consequences are (W-b), the steps being Fréchet. ∎

**Remark 7.3.** The three ingredients of the proof are (i) the symbol seminorms are suprema of **pointwise** quantities in the base variable, (ii) the interpolation inequality is applied **at each base point separately** on a fixed-size neighbourhood, and (iii) the base is compact so r_0 and the chart constants are uniform. There is no step that differentiates, integrates or mollifies in the base variable. This is why the proof is transplant-stable: see §7.5.

### 7.3 Acyclicity of the bounds spectrum A(M̄), and of I, Ȧ, K, J

**Theorem 9 (sketch-grade for the b-geometry, see §10).** Let M̄ be a compact manifold with boundary, x a boundary-defining function, Diff_b(M̄) the b-differential operators, and A^m(M̄) as in §2.3, with (6.32) A(M̄) ⊂ C^∞(M̊̄). Then the spectrum (A^{−k}(M̄))_{k∈N} is acyclic; hence A(M̄) is boundedly, compactly and sequentially retractive, complete and regular.

*Proof (same scheme as Theorem 8, in the b-metric).* Take U_δ := {u ∈ A^{m}(M̄) : ‖u‖_{0,m} < δ}, i.e. |u| ≤ δ x^{m}. In the collar write s := −log x ∈ [0, ∞), so that x∂_x = −∂_s and the b-metric has unit scale in (s, y); Diff_b is generated by ∂_s and the tangential fields on the compact boundary, and every b-unit ball carries a fixed geometry. Assume |P u| ≤ η x^{m′′} for all P ∈ Diff_b of order ≤ M. Applying Lemma 7.2 on a b-unit ball around a point with parameter s (where x varies by a bounded factor):
  |P_j u| ≤ C[ (δ x^{m})^{1−θ}(η x^{m′′})^{θ} + δ x^{m} ] = C[ δ^{1−θ}η^θ x^{m+θ(m′′−m)} + δ x^{m} ], θ = j/M,
and, since m′′ < m′ < m and x ≤ 1 near the boundary, choosing M ≥ j(m − m′′)/(m − m′) makes m + θ(m′′−m) ≥ m′, so the first term is ≤ Cδ^{1−θ}η^θ x^{m′}, small for η small; the second is δ x^{m−m′}x^{m′} ≤ ε x^{m′} for x ≤ x_0 small; and on {x ≥ x_0}, a compact subset of M̊̄, the (6.41)-type bound coming from the m′′-neighbourhood suffices. Thus (∗) and (W-a) hold. ∎

**Corollary 9.1.** With Theorem 8 and (H3)'s manifold-level counterpart ((4.10) a TVS-embedding into a finite product of fixed-compact-support symbol spaces plus C^∞(M∖L), and I^m Fréchet), the spectrum (I^m(M, L))_m is acyclic by the product/subspace argument of Corollary 1.3 (with T a point). Ȧ^m(M̄) = I^m_{M̄}(M̆, ∂M̄) and K^m(M̄) = Ȧ^m_{∂M̄}(M̄) are closed subspaces, so their spectra are acyclic; J(M, L) then inherits the property from Prop. 7.29's surjective topological homomorphism, or directly from its own symbol filtration. All the conclusions [ÁLKL23] Cors. 3.6, 4.7, 6.14, 6.20, 6.25 assert about acyclicity, completeness, retractivity and regularity therefore stand; only their published derivations, and their Montel/reflexivity halves in the transplanted setting, are at issue.

### 7.4 Repair of Claim 6.43 (v3 Claim 6.46), the one downstream consumer

Two separate things must be said about the source's proof of Claim 6.43, quoted verbatim in §2.4.

**(i) An index slip, independent of the refutation.** The proof reads: "A is contained and bounded in some step A^m(M). **For any m′ > m**, let E_{m′} : A^m(M) → Ȧ^{(s)}(M) be the partial extension map given by Proposition 6.26. … there is some 0-neighborhood **W ⊂ A^{m′}(M)** so that E_{m′}(W) ⊂ U ∩ Ȧ^{(s)}(M). **By Corollary 6.12**, there is some 0-neighborhood V ⊂ A(M) such that V ∩ A^m(M) = W ∩ A^m(M)." But (a) Prop. 6.26 (v3 Prop. 6.29) produces E_{m′} on A^{m′}(M), not on A^m(M); (b) by (6.37) — "A^m(M) ⊂ A^{m′}(M) (m′ < m)" — the choice m′ > m makes A^{m′} a *sub*space of A^m, so E_{m′} is not defined on all of A^m; and (c) Cor. 6.12 is stated for m′ **<** m, the opposite inequality to the one the proof announces. The three slips partly cancel, and the intended argument is recoverable; but no repair should pretend the printed indices are consistent.

**(ii) The genuine gap.** The proof invokes Cor. 6.12, which §6 refutes. It uses it, however, only to obtain a 0-neighbourhood V ⊆ A(M̄) with **A ∩ V ⊆ W** (that is all that is needed for E(A ∩ V) ⊆ E(W) ⊆ U). And that inclusion follows from **bounded retractivity alone**, with no coincidence statement and no auxiliary order m′. Here is the whole claim, re-proved.

> **Lemma 7.4 (Claim 6.43 / v3 Claim 6.46, re-proved).** Assume A(M̄) is boundedly retractive (Theorem 9 with (W-b)) and that the partial extension maps of [ÁLKL23] Prop. 6.26 = v3 Prop. 6.29 exist. Then for every bounded A ⊆ A(M̄) there is a bounded B ⊆ Ȧ(M̄) such that for every 0-neighbourhood U ⊆ Ȧ(M̄) there is a 0-neighbourhood V ⊆ A(M̄) with **A ∩ V ⊆ R(B ∩ U)**.
>
> *Proof.* It suffices to prove the statement for the absolutely convex hull Γ(A) of A: Γ(A) is bounded (the absolutely convex hull of a bounded set in an LCS is bounded), contains A and contains 0, and A ∩ V ⊆ Γ(A) ∩ V. So assume A absolutely convex with 0 ∈ A.
>
> **Step 1.** A(M̄) boundedly retractive ⟹ A is contained and bounded in some step A^m(M̄), and the topology A(M̄) induces on A equals the topology A^m(M̄) induces on A.
>
> **Step 2.** Let E := E_m : A^m(M̄) → Ȧ^{(s)}(M̄) be the partial extension map of Prop. 6.26 for **this** m (no auxiliary m′ is needed). By the definition supplied in v3 §6.15, p. 34 — "a map E : X → Y is called a partial extension map if R(Y) ⊂ X and **RE = 1 on X**" — we have R ∘ E = id on A^m(M̄). Set **B := E(A)**: it is bounded in Ȧ^{(s)}(M̄) (continuous linear image of a bounded set), hence bounded in Ȧ(M̄).
>
> **Step 3.** Let U ⊆ Ȧ(M̄) be a 0-neighbourhood. Then U ∩ Ȧ^{(s)}(M̄) is a 0-neighbourhood of Ȧ^{(s)}(M̄), so by continuity of E the set **W := E^{−1}(U ∩ Ȧ^{(s)}(M̄))** is a 0-neighbourhood of A^m(M̄).
>
> **Step 4.** W ∩ A is a neighbourhood of 0 in A for the A^m-trace topology, hence (Step 1) also for the A(M̄)-trace topology; so there is a 0-neighbourhood V ⊆ A(M̄) with **V ∩ A ⊆ W ∩ A ⊆ W**.
>
> **Step 5.** Therefore E(A ∩ V) ⊆ E(A) = B and E(A ∩ V) ⊆ E(W) ⊆ U ∩ Ȧ^{(s)}(M̄) ⊆ U, so E(A ∩ V) ⊆ B ∩ U, and applying R and using R ∘ E = id on A^m ⊇ A,
>   A ∩ V = R(E(A ∩ V)) ⊆ R(B ∩ U) . ∎

Lemma 7.4 replaces the whole of the second paragraph of the source's proof; the surrounding argument of Prop. 6.42 (v3 Prop. 6.45) — "By Proposition 6.7 and [39, Lemma 7.6], it is enough to prove that the map (6.35) satisfies the following condition of 'topological lifting of bounded sets'" — is untouched. Hence **Prop. 6.42 (v3 Prop. 6.45), and with it [ÁLKL23] Prop. 8.8 which is asserted to hold "with formally the same proof", and hence the exactness of the memoir's dual-conormal sequence (1.3.2), are unaffected.**

**And the transplant.** Lemma 7.4 uses exactly three inputs: bounded retractivity of A_τ(X̄) (Theorem 2 + Theorem 9 + Theorem 1), the existence of a continuous partial extension map E_m with R ∘ E_m = id (row **I-6** of the S2 note, work item W1/W2 — *not* proved here), and the fact that the absolutely convex hull of a bounded set is bounded (true in every LCS). None of the three sees the transversal. So the repaired Claim 6.43 transplants verbatim, and row I-9's use of it survives.

### 7.5 The repair transplants

Theorems 8 and 9 verify (W-a) with 0-neighbourhoods of the form U_δ = {p < δ} for a *single* seminorm p, and with the "coincidence" inclusion established pointwise in the base variable. By **Theorem 1** it is not even necessary to re-run them with a transversal parameter: the conclusion (acyclicity of the manifold-level spectrum) is exactly the hypothesis of Theorem 2, and Lemma 1.2 carries it to C(T, −) with no estimate repeated. For the record, running them directly with the parameter also works and shows why: the transplanted seminorms are p^T = sup_{t∈T} p, the interpolation inequality of Lemma 7.2 holds for each fixed t with a constant independent of t, and a supremum over t of a family of inequalities with a uniform constant is again such an inequality. Nothing in Lemma 7.2 or in the scaling of Theorem 8 differentiates, integrates, mollifies or otherwise moves in t.

---

## 8. The theorem W3 was asked for, in final form

> **Theorem W3.** Assume the S2 axioms (A-i)–(A-vi), (H-chart), and the W1/W2 hypotheses (H1)–(H4) of §3.4, in the uniform model (D-unif) of §3.3. Then:
>
> **(a)** The transplanted spectra (I^m_τ)_m, (I^{(s)}_τ)_s, (A^m_τ)_m, (Ȧ^m_τ)_m, (K^m_τ)_m, (J^m_τ)_m over the totally disconnected transversal are **acyclic** in the sense of Wengenroth's criterion as quoted at [ALKL] §2.1.1 p. 9 / [ÁLKL23] §2 p. 4.
> **(b)** Hence I_τ, A_τ, Ȧ_τ, K_τ, J_τ are **boundedly, compactly and sequentially retractive, complete, regular and Hausdorff**, and are barreled, ultrabornological and webbed.
> **(c)** In particular I_τ is compactly retractive (the property [ALKL] §5.2.1 consumes) and A_τ is boundedly retractive (the property [ÁLKL23] Claim 6.43 consumes), and both are obtained without Montel-ness or reflexivity, which **fail** (Proposition 3), and without compact linking maps, which are **not** compact (Proposition 4).
> **(d)** The mechanism is **not** the one the S2 note's row I-8 named: the coincidence statements it proposed to transplant are false upstream (Theorems 5, 6). The correct mechanism is: acyclicity in Wengenroth's 0-neighbourhood form, established at manifold level by interpolation (Theorems 8, 9), is preserved verbatim by C(T, −) (Theorem 1), and reflected back by the constants embedding, so that the transplanted spectra are acyclic **if and only if** the manifold-level ones are.
> **(e)** No property of the transversal beyond compactness is used anywhere. Total disconnectedness enters exactly once, in (H-chart), and only to make partitions of unity easier.

*Proof.* (a) Theorem 2 with Theorem 8, Theorem 9 and Corollary 9.1 supplying its hypothesis. (b) Theorem 1(3). (c) Corollary 2.1 with Propositions 3 and 4. (d) Theorems 5, 6, 8, 9 and Theorem 1. (e) Inspection of §§4, 7. ∎

---

## 9. Step-by-step audit: where a totally disconnected parameter could have broken the argument

Each row states the manifold-level step, the risk, and the verdict, with the place it is settled.

| # | Step in the manifold proof | Risk from a totally disconnected T | Verdict |
|---|---|---|---|
| 1 | Finite atlas, partitions of unity subordinate to it | Smooth transversal bump functions do not exist | **No risk; easier.** Clopen partitions of a compact totally disconnected space give tangentially smooth partitions of unity (locally constant transversally). §3.2 |
| 2 | Each step space must be **Fréchet** for (W-b) | C(T, E) might fail metrizability or completeness | **No risk.** Lemma 1.1(a): countable base (p_i^T); uniform limits of continuous maps into a complete space are continuous. §4.1 |
| 3 | Diff(M, L) generators near L: x∂_x and the fields along L | A transversal-derivative generator would be lost | **No risk.** In an adapted chart, all three tangential directions of X are present and the transversal carries no vector fields; the generator list is *identical* to the slice list ([ÁLKL23] §7.1 p. 39, quoted §3.4). This re-verifies S2 row I-1 on the point that matters here. |
| 4 | Partial Fourier transform in the normal variable (Prop. 4.3) | Would need Fourier analysis in t | **No risk.** The transform acts in x only; t is a spectator; and C(T, −) of a continuous linear map is continuous. (H2), §3.4 |
| 5 | Symbol mollification for density (Cor. 3.5 / 4.6) | Mollification in t is impossible on a totally disconnected T | **No risk for W3** (density is not an input to acyclicity), and no risk downstream either: the direct proof of §6.5 mollifies only in ξ, and the transversal directions are approximated by clopen refinement, which converges in the C(T)-supremum norms. |
| 6 | Wengenroth's criterion (topology coincidence on a 0-neighbourhood) | The criterion might not survive the sup over t | **No risk.** Lemma 1.2: the criterion is a statement about **inclusions of sets defined pointwise in t**; a sup over t preserves it exactly. §4.2 |
| 7 | Interpolation estimates (Lemma 7.2) used in the repair | Interpolation in t is impossible | **No risk.** The estimates are applied at fixed t with a t-independent constant. §7.5 |
| 8 | "Compact linking maps ⟹ acyclic" shortcut | The shortcut might have been the real route | **Real loss, but harmless.** Proposition 4: C(T, S) is never compact for infinite T. The shortcut is not the route used upstream either. §5.2 |
| 9 | Montel-ness / reflexivity of the steps and limits | C(T) is an infinite-dimensional Banach space | **Real loss, proved.** Proposition 3. Priced already by S2 row I-10 and confirmed not to be consumed by the sequences. §5.1 |
| 10 | The choice of model (uniform vs joint continuity) | Symbol and weighted-L^∞ seminorms are sups over non-compact regions, where the two models differ | **Design decision, made and justified.** (D-unif) is stable under the construction of the conormal spaces and under the flow (§3.3); (D-joint) is left undecided (§10). |
| 11 | Non-compact chart bases U_i ⊂ R^3 | The symbol spectrum is not acyclic over a non-compact base | **Real risk, avoided.** Theorem 7 and the fixed-compact-support reading of (4.10)_τ. §6.4 |
| 12 | Duals: C(T, E)′ is transversally measure-valued | The dual sequence might collapse | **Out of scope of W3** (it is W4). Nothing in Theorem 1 or Theorem 2 concerns duals; the properties they deliver (completeness, retractivity, barreledness, webbedness) are precisely those the duality arguments of rows I-5/I-9 consume. |

**Conclusion of the audit.** Of twelve candidate failure points, ten are non-risks, one (row 11) is a real risk that the construction avoids by a forced reading, and two (rows 8, 9) are real losses that were already priced and are not consumed. **No obstruction to W3 arises from the transversal.** The only thing that broke is upstream and has nothing to do with the transversal at all.

---

## 10. Scope and honesty

**What was proved in full, from first principles, in this note.**
- Lemma 0, Lemma 1.1, Lemma 1.2, Theorem 1, Corollary 1.3 (§4): complete proofs, no external input beyond the two quoted Wengenroth sentences.
- Propositions 3 and 4 (§5): complete proofs.
- Claim 6.1, Theorem 5 (with both gaps in the source's proof exhibited), Theorem 5′ (two independent witnesses, one over a point and one over a base of dimension 1), Theorem 6, Theorem 7, Lemma 6.5.1 (density, re-proved) and Lemma 6.5.2 (the true bounded-set form) (§6): complete proofs; every computation is elementary and was carried out symbolically in this note.
- Lemma 7.1, Theorem 8, Lemma 7.4 (§7): complete proofs, modulo Lemma 7.2 and, for Lemma 7.4, the existence of the partial extension maps ([ÁLKL23] Prop. 6.26 = v3 Prop. 6.29, quoted, not re-proved).

**What is assumed and not proved here.**
- **(H1)–(H4)** of §3.4 — the outputs of the S2 note's W1 and W2. W3 is conditional on them and states so in Theorem W3. In particular (H3) includes the completeness of I^m_τ, whose manifold-level counterpart [ÁLKL23] cites to [Mel96], which is **not on disk**; that is an open input in the manifold case as much as in the transplant, and it is *not* repaired here.
- **Lemma 7.2** (Landau–Kolmogorov on a cube, iterated form) is used but not proved beyond the one-dimensional base case. **[RU-standard]**: elementary and classical, but not read from an on-disk source this session. Theorems 8 and 9 are therefore proved *modulo an elementary interpolation inequality*; a referee should either supply the induction or cite a source. Nothing else in the note depends on it — in particular Theorem 1, the entire positive transplant content, is independent of §7.
- **Theorem 9** is written at **proof-sketch grade** for the b-geometry: the scaling argument is given in full, but the uniformity of the b-geometry near the corner structure and the precise generating set of Diff_b are taken from [ÁLKL23] §6.7's statements rather than re-derived. Theorem 8 (the symbol case) is at full proof grade.
- **Chart independence** of I^m_τ, i.e. that the transplanted symbol filtration does not depend on the atlas, is (H3) and is not proved. It is W2's item.
- The **[Den05]** quotation in §3.1 is taken from the S2 note's transcription rather than re-read from the PDF this session. Nothing below §3.1 depends on its wording; it fixes the category only. **Judgment-grade reading, flagged.**
- The identification of the **transplanted geometry** with (H-chart) uses axiom (A-iii) of the S2 note, which is an axiom, not a theorem, and whose satisfaction by any arithmetic object is the S4 problem, not S2's. Nothing here bears on S4.

**Judgment-grade readings, flagged as such.**
- The claim that the defect of §6 does **not** damage [ALKL]'s Theorems 1.3.3/1.3.6 rests on the consumer audit of §6.5, which is **mechanically complete for explicit cross-references** (every occurrence of "coincide on" and of each corollary number, over the full `pdftotext` extractions of [ÁLKL23] v1 and of the 176-page memoir) but is **not** a semantic audit: a proof that re-runs the false argument without naming it would not be caught. §6.5 states this blind spot exactly. Recorded as an open item in §12.
- The assertion that (D-unif) is "the right" model is a design judgment, argued in §3.3 on four grounds, not a theorem. The (D-joint) model is **undecided**: its step spaces are Fréchet by the same argument, and Prop. 3.3's analogue holds there too, but I did not determine whether Wengenroth's criterion holds for the (D-joint) spectra, because Theorem 1 does not apply to them (they are not of the form C(T, E)). A referee wanting the (D-joint) model must redo §7 with the parameter carried explicitly; §7.5 explains why that is expected to work, but expectation is not proof, and it is not claimed.
- The counterexamples of §6.3(c) for the conormal and bounds filtrations are transported through the localisations rather than written out in the intrinsic spaces; the symbol-level counterexample (§6.1–§6.2), which carries the refutation, is complete and intrinsic.

**Prior-art check (standing order 1).** No literature search was run this session for the specific claim "[ÁLKL23] Prop. 3.2 is false". What *was* checked, this run, on disk and over the network: arXiv 2304.00798 has exactly three versions and **v3 (1 June 2024) is the current one**, its §3 is textually identical to v1's, and its Claim 6.46 still invokes the false Cor. 6.14 (§1). The **published** version (J. Pseudo-Differ. Oper. Appl., DOI 10.1007/s11868-024-00617-y, recorded in the S2 note §1) was **not** consulted: the SpringerLink page returned a bot challenge on the one attempt made. So it remains possible that the authors know the defect and that the journal text differs. **This is a live possibility and the novelty ledger prices it.** The mathematical content of §6 is independent of who knew it: the statements the program was about to transplant are false, and the program must not cite them.

**One further honesty item about provenance.** This note is the product of a **resumed run**. An earlier run of the same probe, killed by a usage limit, left an 86 KB draft on disk and several extractions and one downloaded PDF in the session scratchpad. This run did **not** trust that draft: every source quotation in §2, §3.1, §3.4, §6 and §7 was re-extracted from the on-disk PDFs and re-read this run; the v3 PDF was re-verified by `diff` and `grep` rather than by the earlier run's report; the arXiv abstract page was re-fetched. Three substantive corrections resulted, and are flagged where they occur: (1) the earlier draft recorded [ÁLKL23] Cor. 3.5 (density) as "true, by the standard direct argument … unaffected" — in fact the source *derives* it from the false Cor. 3.4, so the statement needed the new proof at Lemma 6.5.1; (2) the earlier draft's repair of Claim 6.43 reproduced the source's inconsistent indices (m′ > m together with an appeal to a corollary requiring m′ < m, and a partial extension map applied on the wrong space) — §7.4 now states and fixes that slip separately from the refutation; (3) the earlier draft's Theorem 8 was stated for a compact base only, whereas the object the transplant needs is the fixed-compact-support space S^m_K(U × R^l) inside a non-compact base, which is now case (B2) of Theorem 8. Two strengthenings also resulted: Claim 6.1(vi) (the witnesses lie in ∩_m S^m, so Cor. 3.4 fails for *every* pair m < m′), and the source-anchored transport of the refutation to the bounds filtration through [ÁLKL23] Example 6.9 (§6.3(c1)).

**What this note may NOT be cited for.** (1) Any positivity, Hodge or clause-(ii) claim (guard Z2). (2) Any claim that the S2 sequences (S2-1)/(S2-2) are established — W3 is one of seven work items, and W1, W2, W4, W5, W6, W7 remain. (3) Any claim about the existence of an arithmetic object (S4). (4) The hypotheses (H1)–(H4) as theorems. (5) Lemma 7.2 as a verified citation. (6) An exhaustive audit of [ALKL]/[ÁLKL23].

---

## 11. Novelty ledger

Every item below is believed new and is tagged for the dual-model sweep. Items N1–N4 are the ones a sweep should attack first; N1 and N2 carry the verdict.

- **[N1] [novelty: single-check] Theorem 1 (transversal transparency).** For T compact Hausdorff, the functor E ↦ C(T, E) preserves Fréchet-ness, continuous injections, closed subspaces and finite products, and preserves Wengenroth's acyclicity criterion **verbatim**, in both directions (forward by Lemma 1.2, backward by the closed subspace of constants). Hence a countable inductive spectrum of Fréchet spaces is acyclic if and only if its C(T, −)-image is, and the entire retractivity/completeness/regularity package transplants. *Believed new as a statement; the ingredients are elementary, so the likeliest prior-art outcome is "folklore, unstated". Its role here is decisive: it is the whole positive answer to W3, and it shows that no property of the transversal beyond compactness matters.*
- **[N2] [novelty: single-check] Theorems 5, 5′, 6 (refutation of [ÁLKL23] Prop. 3.2, Cor. 3.4, Cor. 4.5, Prop. 6.10, Cor. 6.12, Cor. 6.24, Cor. 7.20, in arXiv v1 and v3 alike).** The family a_N(ξ) = N ψ(ξ/N) lies in C_c^∞ ⊂ ∩_m S^m, converges to 0 in the topology generated by the seminorms (3.4) and (3.5), and is unbounded in S^0 — so Prop. 3.2 fails and Cor. 3.4 fails **for every pair m < m′**; c_N = ∑_{j≤N} 4^j ψ(·/4^j) is Cauchy in that topology with no limit, and so is b_N = ρ_N · x^{−1}χ(ξ − x^{−1}) over a base of dimension 1, so the completeness step of the published proof of Prop. 3.2 fails; and the same b exhibits a **second, independent** failure of that proof (finiteness of the sup-of-limsups seminorm (3.5) does not produce a threshold R uniform in the base point, which is what the printed argument needs). *A defect in a source the whole S2 design rests on. Prior-art risk: the authors or the published version may have corrected it; the published version could not be reached this run (§10).*
- **[N2′] [novelty: single-check] Lemma 6.5.1 (repair of [ÁLKL23] Cor. 3.5) and Lemma 6.5.2 (the true bounded-set coincidence statement), together with the complete cross-reference consumer audit of §6.5.** Density of C_c^∞ in S^m with the S^{m′}-topology is *derived from the false Cor. 3.4 in the source* and is re-proved here by two truncations; the coincidence statement is true on **bounded** subsets, which is exactly the form the semi-Montel proofs use; and the audit locates the single non-acyclicity consumer of a coincidence statement in either document (Claim 6.43). *The bounded-set statement is very likely classical symbol-calculus folklore; its role here is to separate what survives from what does not.*
- **[N3] [novelty: single-check] Theorem 7 (non-compact base).** For non-compact U, the symbol spectrum (S^k(U × R^l))_k is not acyclic, so [ÁLKL23] Cor. 3.6 needs a compactness or fixed-compact-support hypothesis; and the transplant must read (4.10)_τ with fixed compact base supports, which the foliated-space charts make non-optional.
- **[N4] [novelty: single-check] Theorems 8 and 9 with Lemma 7.4 (the repair).** *(Theorem 8 is stated in two cases: a compact base, and — the case the transplant needs — the fixed-compact-support subspace S^m_K(U × R^l) of a non-compact base.)* Acyclicity of the symbol spectrum over a compact base and of the b-bounds spectrum A(M̄), proved by anisotropic Landau–Kolmogorov interpolation verifying Wengenroth's 0-neighbourhood criterion with the one-seminorm neighbourhood U_δ = {‖·‖_{0,0,k} < δ} and the index bound M ≥ j(k′′−k)/(k′−k); plus the observation that [ÁLKL23] Claim 6.43 consumes only "A ∩ V ⊆ W", which follows from bounded retractivity applied to the bounded set A. This restores every conclusion of [ÁLKL23] Cors. 3.6, 4.7, 6.14, 6.20, 6.25 and Props. 6.42 / 8.8 that the memoir uses. §7.4 also records, separately from the refutation, a **three-fold index slip** in the printed proof of Claim 6.43 (m′ > m announced where Cor. 6.12 needs m′ < m; E_{m′} written on A^m where Prop. 6.26 defines it on A^{m′}; W taken in A^{m′} where the argument needs it in A^m), and gives a proof with no auxiliary order at all. *Prior-art risk: the acyclicity of symbol spectra may well be classical; the specific verification of Wengenroth's criterion by interpolation, and the Claim-6.43 repair, are believed new.*
- **[N5] [novelty: single-check] Propositions 3 and 4 (the priced losses, proved).** For infinite compact T and E ≠ 0, C(T, E) is neither semi-Montel nor semi-reflexive, and C(T, S) is not a compact operator for S ≠ 0. These convert S2 note rows I-8 and I-10 from asserted readings into theorems and identify the topology/interpolation route as the unique available one.
- **[N6] [novelty: single-check] Lemma 0 and the (D-unif)/(D-joint) dichotomy (§3.3).** Tangential smoothness in [Den05]'s sense (joint continuity of leafwise derivatives) coincides with C(T, C^∞) because the C^∞-seminorms are suprema over compacta; the coincidence **fails** for symbol and weighted-L^∞ seminorms, so the transplant of the conormal theory to a foliated space carries a genuine, previously unnamed model choice. *This is a definitional finding about the foliated-space transplant that the S2 note did not isolate.*
- **[N7] [novelty: single-check] Theorem W3 (§8), the assembled statement**, including clause (d): the S2 note's stated mechanism for row I-8 is void and is replaced.

---

## 12. Bookkeeping — what this result touches (no file is edited)

**`results/c3-r/s2-feasibility-note.md`.**
- **Row I-8 (§4 table) and work item W3 (§5).** Status changes from "TRANSFERS-WITH-WORK (the key step, W3)" to **executed, with its stated mechanism struck and replaced**. The sentence "[ÁLKL23] Cor. 4.5's mechanism is symbol-seminorm interpolation on S^{m̄}-scales … So the SAME mechanism proves the C(T)-valued coincidence" must be struck: Cor. 4.5 is false and has no mechanism. The replacement is Theorem W3 of §8 above. The row's *conclusion* — acyclicity, hence bounded/compact/sequential retractivity, completeness, regularity — **stands, and is now proved** (conditionally on (H1)–(H4) and Lemma 7.2).
- **Row I-10.** Its claims (a), (b), (c) are confirmed; (c) in particular ("compact retractivity is EQUIVALENT to acyclicity for LF-spaces and therefore follows from I-8/W3 without Montel") is now delivered. The FAILS verdict on Montel/reflexivity is upgraded from assertion to theorem (Proposition 3).
- **Row I-9 and row I-13.** Their inputs (barreled, ultrabornological, webbed; bounded retractivity; compact retractivity) are supplied by Theorem W3(b),(c). Row I-13's §5.2 dependence on compact retractivity is discharged.
- **§5, work items W1, W2.** Their scope grows by exactly the items (H1)–(H4) of §3.4, plus the two new obligations: use fixed compact base supports in the localisation (§6.4), and fix the model as (D-unif) (§3.3).
- **§6.5 ("What a genuine obstruction would have looked like"), item (ii).** Its disposal — "an exactness proof whose only known route uses compactness of Sobolev linking maps or Montel-ness — refuted at I-8/I-9/I-10 by proof-level inventory" — survives, and is strengthened: Propositions 3 and 4 show both alternatives are unavailable, and §7 shows the route that remains is available.
- **§7, discipline statements.** Item (4) ("in particular W3, the acyclicity lemma, is the note's single named point of residual risk") should be read as discharged **and replaced** by a new residual-risk item: *every citation in this program of a coincidence statement from [ALKL] or [ÁLKL23] must be routed through §6–§7 of this note.* The Z1/DH arithmetic-blindness statement of that section is untouched — nothing in W3 distinguishes {log p} from a Beurling spectrum, exactly as expected for a clause-(i) instrument item.

**`results/c3-r/probe-9.3-adjudication.md`.**
- **§1 row 3 and §6 (S2 / ledger §9.2).** "W3 (topology-coincidence/acyclicity of the C(T)-valued symbol spectra) is the single residual-risk item — its failure would reopen the verdict, and any future referee should press there first." **W3 does not fail.** The verdict TRANSFERS-WITH-WORK is **not** reopened. But the adjudication's phrasing "topology-coincidence" is now known to name a false statement and should be re-read as "acyclicity".
- **§7 row "§9.2 / S2".** "Residual risk = W3 only" is superseded: the residual risks are now (i) W1/W2's (H1)–(H4), including the [Mel96]-cited completeness of I^m; (ii) W4–W7; (iii) the new source-integrity item above.
- No other clause is touched. **Q\* (§5) is untouched: W3 is an S2 item and bears on nothing in S4.**

**`results/c3-r/m2c-feasibility-ledger.md`.**
- **§9 item 2 / §9.2 (Route 2 step S2).** Sub-item W3 executed; ledger status of S2 unchanged at TRANSFERS-WITH-WORK.
- **§8 (Route 2).** Route 2's unique blocker remains **S4**. Nothing in this note bears on it. The kill-criterion does **not** fire from this leg.
- A new ledger row is warranted (numbering left to the ledger's keeper): *"[ÁLKL]/[ÁLKL23] coincidence statements are false as stated; use §6–§7 of `results/c3-r/s14/w3-O.md` instead."* This is a **source-integrity** row, not an obstruction row.

**`directions/C3-geometric-substrate.md`, "Current frontier".** Unchanged as to direction: the frontier remains S4 / Q\*. The entry for S2 may record that its named residual-risk item is discharged and that a defect in the instrument literature was found and repaired.

**Corpus.** No file was added to `fetched/`, `fetched-r2/` or `fetched-r3/` this session. The arXiv v3 PDF of 2304.00798 was fetched to the session scratchpad only, and is identified in §1 by URL and retrieval date; if the program wants it durably it must be added under the Round-3 rules, which this note does not do.

— end of probe O, W3 —
