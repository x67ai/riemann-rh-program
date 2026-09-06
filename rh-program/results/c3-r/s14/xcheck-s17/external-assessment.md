# External assessment of `alkl23-note.pdf` (ChatGPT, relayed by the sponsor 2026-09-06)

Source: https://chatgpt.com/s/t_6a9d0c96719c81918a2b8e57fd09c736 (share link). The reader had the note PDF and arXiv:2304.00798v3. Text as relayed, verbatim:

---

Yes. After checking the note against the uploaded v3 paper, I think the **core mathematical diagnosis is essentially right**, and several of the counterexamples are quite strong. But I would not yet describe the note as a fully established correction to the paper. The main weak point is §4, where the proposed replacement theorem is only sketched.

### What I think is solid

Your basic attack on Proposition 3.2 is convincing.

The paper defines the full symbol topology using the seminorms (3.1), then introduces the weaker-looking seminorms (3.4) and (3.5), and claims that those latter seminorms still describe the topology.

Your translated bump g_N(x,ξ)=θ(ξ−Ne_1) is exactly the right kind of witness. It goes to zero for the local C^∞-type seminorms and for the tail seminorms (3.5), while a sufficiently high ξ-derivative makes the genuine symbol seminorm blow up. Thus g_N→0 in the proposed weaker topology but is unbounded in S^m.

That directly contradicts Proposition 3.2 and the first assertion of Corollary 3.4. The paper's actual statement is that (3.4) and (3.5) describe the topology, followed by the claim that S^{m'} and C^∞ have the same topology on S^m.

Your completeness objection is also good. The finite sums b_j=Σ_{i=1}^j (1+iR)^{m+1}θ(ξ−iRe_1) are Cauchy for the weaker topology, but their C^∞-limit is not in S^m. The paper's proof of completeness explicitly extends the proposed seminorms to the completion and then asserts that the image remains in S^m. Your construction attacks exactly that step.

I also checked the boundary analogue. The paper explicitly says Proposition 6.12 gives the topology of A^m(M) from (6.42), (6.43), and then Corollary 6.14 asserts coincidence with C^∞(M°). Your u_j=j^{−m'}χ(jx)g(y) is a direct witness against that claim. The calculation using the global weighted seminorm (6.41) is particularly persuasive because it isolates exactly the seminorm the paper's Proposition 6.12 says is part of the topology.

Likewise, the paper's Corollary 7.13 really does assert the corresponding statement for J^m(M,L). Your collar example therefore propagates to J for exactly the reason you give.

### One particularly important point

Your note is right to distinguish **acyclicity** from the much stronger assertion that the whole step topology coincides with a C^∞ topology.

That distinction matters because the paper uses the false coincidence statements to prove later results. For example, Corollary 4.7 explicitly says its proof proceeds via Corollaries 4.2 and 4.5. Similarly, Corollary 6.22 is explicitly derived from Corollary 6.21, and Corollary 6.27 is explicitly said to have a proof using Corollaries 6.21 and 6.22.

So your observation that some downstream statements may remain true while their printed proofs are invalid is mathematically well-motivated.

### Where I would be more cautious

The biggest issue is §4.

You propose the compact-base estimate
N_{m'}(a;γ) ≤ C[ R^{−(m'−m)/2} N_m(a;0) + R^{m''−m'} max_{γ'∈Γ} N_{m''}(a;γ') ].
Then you say this follows from a Taylor/Landau-Kolmogorov argument and use it to recover acyclicity and bounded retractivity.

That may well be the right replacement, but **this is the part I would not yet call proved in the note as it stands**. The estimate is the essential new theorem. The sentence saying it follows from Taylor expansion is not enough for a reader to verify:

1. the precise choice of boxes in x and ξ,
2. how derivatives in both variables are controlled simultaneously,
3. why the finite set Γ is sufficient uniformly in ξ,
4. the dependence of C, R_0,
5. and exactly how (1) implies the topological coincidence criterion being invoked.

In other words, your §4 currently has a **credible repair strategy**, while §3 contains much more direct refutations.

### One small presentation issue

I would soften the sentence "The main package of the paper ... stands once this is done."

The counterexamples establish that the printed arguments fail. They do **not by themselves** establish every replacement theorem claimed in §4. Your later arguments appear to support the repaired conclusions, but until inequality (1) and its passage through the various initial-topology constructions are written out fully, "stands once this is done" is slightly stronger than what the note has actually demonstrated.

A safer formulation would be something like: "The principal conclusions appear recoverable after replacing the false topology-coincidence statements by bounded-set or compact-base estimates."

### Bottom line

**Yes, I think your central correction is mathematically justified.** In particular, the witnesses for Proposition 3.2, Corollary 3.4, Corollary 4.5, Corollary 6.14, Corollary 6.21, and Corollary 7.13 are substantially convincing, and they attack the exact statements printed in the paper rather than peripheral details. The paper really does make those topology-coincidence claims.

What I would **not** claim yet is that §4 has completely repaired all downstream results. The key estimate needs a full proof.

I also checked the current public record. The Springer page still lists the paper as the June 9, 2024 version of record, and the arXiv record still points to v3. I did not find a published erratum in the searches I ran.
