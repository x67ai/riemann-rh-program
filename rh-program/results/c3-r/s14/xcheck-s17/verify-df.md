# Second-model verification — witnesses (d) and (f), and companion §§5, 7

Machine clock at start: (see below). Independent re-derivation; the first referee's file
`refute-df.md` was read only for its list of rulings, and every ruling is re-checked here from
the note, the companion and the published text. Page numbers refer to the published JPDOA
article (`novelty/ALKL-2024-published.txt`, markers "Page k of 68").

Sun Sep  6 12:39:14 IST 2026


## 0. Anchors quoted verbatim from the published text (all re-fetched here)

**(3.1), p. 15** — `‖a‖_{K,α,β,m} := sup_{x∈K, ξ∈R^l} |∂_x^α ∂_ξ^β a(x,ξ)| / (1+|ξ|)^{m−|β|} < ∞`.
So the weight is `(1+|ξ|)^{|β|−m}` in numerator form. (Used throughout.)

**Adapted chart, p. 19** — "Let (U, x) be a chart of M adapted to L; i.e., for open subsets
U′ ⊂ R^{n′} and U″ ⊂ R^{n″}, x = (x_1,…,x_n) ≡ (x′,x″) : U → U′ × U″, … L_0 := L ∩ U = {x′ = 0}."

**(4.7)–(4.8), p. 21** — verbatim:
"                                 C∞_cv (N∗U″) → C∞(U), a → u,                       (4.7)
                                 C∞_c (U) → C∞(N∗U″),   u → a,                       (4.8)
 by the following partial inverse Fourier transform and partial Fourier transform:
        u(x) = (2π)^{−n′} ∫_{R^{n′}} e^{i⟨x′,ξ⟩} a(x″, ξ) dξ ,
        a(x″, ξ) = ∫_{R^{n′}} e^{−i⟨x′,ξ⟩} u(x′, x″) dx′ ."
Normalization: **no** constant on the forward transform (4.8); `(2π)^{−n′}` sits on (4.7); the
sign in the exponent of (4.8) is **minus**. This is exactly what the note's computation uses.

**(4.9), p. 22** — "m̄ = m + n/4 − n′/2".

**(4.10), p. 22** — "Let {h, f_j} be a C^∞ partition of unity of M subordinated to the open
covering {M\L, U_j}. … applying the versions of semi-norms (2.1) on C^∞(M\L) to hu and versions
of semi-norms (3.1) on S^{m̄}(N∗L_j; Ω N∗L_j) to every a_j, we get semi-norms on I^m(M, L), which
becomes a Fréchet space … In other words, the following map is required to be a TVS-embedding:
I^m(M,L) → C^∞(M\L) ⊕ ∏_j S^{m̄}(N∗L_j; Ω N∗L_j), u ↦ (hu, (a_j))."

**(4.5), p. 20** — "C^∞(M) ⊂ I^{(∞)}(M, L), I(M, L) ⊂ C^{−∞}(M)".
**p. 22** — "I(M,L) = ⋃_m I^m(M,L), I^{(∞)}(M,L) = I^{−∞}(M,L) := ⋂_m I^m(M,L)."
**(4.12), p. 22** — "I^{(−m−n/4+ε)}(M,L) ⊂ I^m(M,L) ⊂ I^{(−m−n/4−ε)}(M,L)".

**Cor. 4.5, p. 23** — "For m < m′, m″, the topologies of I^{m′}(M, L) and I^{m″}(M, L) coincide on
I^m(M, L). *Proof* Use Corollary 3.4 and the TVS-embeddings (4.10)."

**Cor. 4.6 proof, p. 23** — "C^∞(M) is contained in the stated spaces by (4.5)."

**§4.3.3, p. 23** — "There are extensions of (4.10)–(4.13) and Corollaries 4.5 and 4.6, with
arbitrary/compact support … Corollary 4.7 has extensions for ⋃_m I^m(M, L) and I_{·/c}(M, L),
except acyclicity in the case of I(M, L)."

**(6.47) and Cor. 6.21, p. 40** — "Ȧ^m(M) = I^m_M(M̆, ∂M) ⊂ I^m(M̆, ∂M) (m ∈ R), (6.47) which are
closed subspaces satisfying the analogs of (4.11) and (4.12). … The following is a consequence of
Corollary 4.5 applied to (M̆, ∂M). **Corollary 6.21** For m < m′, m″, the topologies of Ȧ^{m′}(M)
and Ȧ^{m″}(M) coincide on Ȧ^m(M)."
**p. 31** — "Let M̆ be any closed manifold of dimension n which contains M as submanifold (for
instance, M̆ could be the double of M)"; subscript = support, by (6.4) `Ċ^∞(M) ≡ C^∞_M(M̆)` and
(6.7) `Ċ^{−∞}(M) ≡ C^{−∞}_M(M̆)`.

**Cor. 3.6 and its proof, p. 18** — "S^∞(U×R^l) is an acyclic Montel space, and therefore complete,
boundedly retractive and reflexive. *Proof* Corollary 3.4 gives the property of being acyclic, and
therefore complete and boundedly retractive (Sect. 2.1). Since S^∞(U×R^l) is barreled … it only
remains to prove that S^∞(U×R^l) is semi-Montel. Take any closed bounded subset B ⊂ S^∞(U×R^l); in
particular, B is complete because S^∞(U×R^l) is complete. Since S^∞(U×R^l) is boundedly retractive,
B is contained and bounded in some S^m(U×R^l), and the topologies of S^∞(U×R^l) and S^m(U×R^l)
coincide on B. …"
**Bundle sentence, p. 18** — "We can similarly define the norms (3.4) and (3.5) on S^m(E), and
Propositions 3.2 and 3.3 and Corollaries 3.4 to 3.6 can be directly extended to this setting."
(No compactness hypothesis on M anywhere in §3.)

**pp. 4–5 (Wengenroth)** — p. 4: "the condition of being acyclic can be described as follows
[39, Theorem 6.1]: for all k, there is some k′ ≥ k such that, for all k″ ≥ k′, the topologies of
X_{k′} and X_{k″} coincide on some 0-neighborhood of X_k." … "It is said that (X_k) is regular if
any bounded B ⊂ X is contained and bounded in some step X_k. If moreover the topologies of X and
X_k coincide on B, then (X_k) is said to be boundedly retractive."
p. 5: "If the steps X_k are Fréchet spaces, the above properties of (X_k) depend only on the
LF-space X … In this case, X is acyclic if and only if it is boundedly/compactly/sequentially
retractive [39, Proposition 6.4]. As a consequence, acyclic LF-spaces are complete and regular
[39, Corollary 6.5]." Also: "The above concepts and properties also apply to an
inductive/projective spectrum consisting of continuous inclusions X_r ⊂ X_{r′} for r < r′ in R
because ⋃_r X_r = ⋃_k X_{r_k} …" (so the R-indexed spectrum S^m is legitimately reduced to a
countable one).

All of these are verbatim-correct as the note cites them. **HOLDS** (anchors).
