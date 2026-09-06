# Second-model verification of witness (e) — Prop. 6.12, Cor. 6.14, Cor. 7.13, memoir restatements

**Role:** SECOND-MODEL VERIFIER (hostile referee), cross-checking `refute-e.md`.
**Machine clock at start:** Sun Sep  6 13:00:55 IST 2026 (`date`).
**Sources actually opened:** `alkl23-note.tex` (full), `alkl23-note-derivations.md` §§0, 1, 6, 11,
`novelty/ALKL-2024-published.txt`, and — because pdftotext drops primes, bold, and the big
operators ⋂/⋃ — the published PDF itself, rendered at 200 dpi with `pdftoppm` and read as images:
printed pages 5, 36, 38, 39, 56 (PDF page number = printed page number; verified).
Nothing below rests on `refute-e.md`, on the earlier internal reads, or on the companion's verdicts.

## Verdict

**HOLDS-WITH-REPAIR** for the item as a whole. Every mathematical claim of witness (e) in the
*note* is correct and refutes exactly the printed statements it names; I found no counterexample
to any step, and I re-derived all thirteen. The "-WITH-REPAIR" is not against the note: it is
against (i) one citation chain in the **companion** (§6, the J-membership route through (7.28)),
which is invalid as printed and is rescued only by the parenthetical direct argument beside it,
and (ii) the first referee's report, which certifies that chain (its item 10) without noticing.
Two further errors in the *published paper* that neither the note nor the first referee records
are reported below; they do not affect the note.

---

## Item 1. The setting: is the collar coordinate the boundary defining function? (referee item 1)

Published p. 30, read from the rendered page:

> "There exists a function x ∈ C^∞(M) so that x ≥ 0, ∂M = {x = 0} (i.e., x^{−1}(0)) and dx ≠ 0
> on ∂M, which is called a boundary defining function. … Take a collar neighborhood
> T ≡ [0, ε_0)_x × ∂M of ∂M, whose projection ϖ : T → ∂M is the second factor projection.
> (In a product expression, every factor projection may be indicated as subscript of the
> corresponding factor.) Given coordinates y = (y^1, …, y^{n−1}) on some open V ⊂ ∂M, we get
> via ϖ coordinates (x, y) = (x, y^1, …, y^{n−1}) adapted (to ∂M) on the open subset
> U ≡ [0, ε_0) × V ⊂ M."

The subscript `x` on the factor `[0, ε_0)_x` is the paper's own convention for naming the factor
projection, so the first coordinate of the adapted chart **is** the boundary defining function x
that appears in x^m L^∞(M) and in (6.41)–(6.43). No comparability constant is needed anywhere in
(e). (Even if the two were only comparable, c_1 x ≤ x_chart ≤ c_2 x, the witness would survive with
1 replaced by a j-independent c > 0.)

**AGREE** with the first referee.  **HOLDS**

## Item 2. A^m(M), its topology, and the legitimacy of "(6.41) with P = 1" (referee item 2)

Published p. 38, rendered image, verbatim:

> "For every m ∈ ℝ, let  𝒜^m(M) = { u ∈ C^{−∞}(M) | Diff_b(M) u ⊂ x^m L^∞(M) }.
> This is another C^∞(M)-module and LCS, with the projective topology given by the maps
> P : 𝒜^m(M) → x^m L^∞(M) (P ∈ Diff_b(M))."

and, lower on the same page,

> "Let { P_j | j ∈ ℕ_0 } be a countable C^∞(M)-spanning set of Diff_b(M). The topology of 𝒜^m(M)
> can be described by the semi-norms ‖·‖_{k,m} (k ∈ ℕ_0) given by
> (6.41)  ‖u‖_{k,m} = ‖P_k u‖_{x^m L^∞} = ess sup_M |x^{−m} P_k u| = sup_{M̊} |x^{−m} P_k u| ,"

The note's parenthetical — "the topology of A^m(M) is the projective one over all P ∈ Diff_b(M),
p. 38" — is therefore quoted correctly, and it is the correct justification: P = 1 is one of the
maps of the projective family, because Diff_b(M) is obtained from X_b(M) "like in Sect. 2.7"
(p. 35) and Sect. 2.7 (p. 6) states "In particular, Diff^0(M) ≡ C^∞(M)", so 1 ∈ Diff_b^0(M).
Hence u ↦ sup_{M̊} x^{−m}|u| is by definition one of the defining seminorms of A^m(M).

I also checked the stronger statement the referee asserts, that P = 1 is dominated by the printed
family {P_k} even though "P = 1" is not literally one of its indices. It is: {P_j} spans Diff_b(M)
as a C^∞(M)-module, so 1 = Σ_{j∈F} f_j P_j for a finite F and f_j ∈ C^∞(M), whence for every
u ∈ A^m(M),
  x^{−m}|u| = x^{−m}|Σ_{j∈F} f_j P_j u| ≤ Σ_{j∈F} ‖f_j‖_∞ · x^{−m}|P_j u| ,
so sup_{M̊} x^{−m}|u| ≤ Σ_{j∈F} ‖f_j‖_∞ ‖u‖_{j,m} < ∞ (M compact, so ‖f_j‖_∞ < ∞).
So the note's seminorm is continuous for the (6.41) family as well, and both readings work.
The residual "P = 1 is an index outside {P_k}" is a presentational nit, not an error, and the note
already carries its own correct justification in the same parenthesis.

**AGREE** with the first referee, and the domination computation above is an addition.  **HOLDS**

## Item 3. (6.42): is K compact in M or in M̊? (the brief's flagged question)

pdftotext renders the ring accent unreliably, so I read the rendered page. Published p. 39,
verbatim from the image:

> "From (2.1) and (6.33), we also get the continuous semi-norms ‖·‖_{K,k,m} (for any compact
> K ⊂ M̊ and k ∈ ℕ_0) on 𝒜^m(M) given by  (6.42) ‖u‖_{K,k,m} = sup_K |P_k u| ."

**K ⊂ M̊ — the interior — as printed.** The ring over M is visible in the rendering. This is also
forced by the paper's own derivation, "From (2.1) and (6.33)": (2.1) is the C^∞(U) seminorm over
compact K ⊂ U, and (6.33) is 𝒜(M) ⊂ C^∞(M̊); a sup over a compact set touching ∂M is not
continuous on A^m(M) for m < 0 (x^m ∈ A^m(M) is unbounded on M).

The witness therefore needs only: supp u_j leaves every compact K ⊂ M̊. It does — min_K x =: c > 0
because x > 0 on M̊ and K is compact, while supp u_j ⊂ {1/(2j) ≤ x ≤ 2/j} × supp g, so
supp u_j ∩ K = ∅ once 2/j < c; and P_k u_j is supported in supp u_j because differential operators
are local. So ‖u_j‖_{K,k,m} = 0 for all large j (j depending on K), which is exactly what
convergence to 0 in the (6.42)-family requires.

I also checked the hostile alternative reading K ⊂ M (which is *not* what is printed): with m' > 0
the witness still works, because sup_M |P_k u_j| ≤ C_k j^{−m'} → 0. Indeed on the collar every
P ∈ Diff_b is a C^∞-combination of products of x∂_x and ∂_{y_i}, and (x∂_x)^a ∂_y^b [j^{−m'}χ(jx)g(y)]
= j^{−m'} (jx)^a-type expressions: (x∂_x)χ(jx) = jxχ'(jx), which is bounded uniformly in j since
jx ∈ (1/2, 2) on the support. So every b-derivative of u_j is O(j^{−m'}) uniformly on M.
So Prop. 6.12 falls under either reading (for the printed reading, for every m; for the K ⊂ M
reading, for every m > 0).

**AGREE** with the first referee.  **HOLDS**
