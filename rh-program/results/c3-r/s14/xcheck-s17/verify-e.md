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

## Item 4. (6.43) and its vanishing on u_j (referee item 5)

Published p. 39, rendered image, verbatim:

> "Other continuous semi-norms ‖·‖′_{k,m} (k ∈ ℕ_0) on 𝒜^m(M) are defined by
> (6.43)  ‖u‖′_{k,m} = lim_{ε↓0} sup_{{0<x<ε}} |x^{−m} P_k u| ."

Note it is **lim**, not lim sup (the layout puts "ε↓0" under `lim` and "{0<x<ε}" under `sup`;
the limit exists because ε ↦ sup_{{0<x<ε}} is monotone). The companion's §0 anchor table
transcribes this as "limsup_{ε↓0} sup_{0<x<ε}" — a doubling; it changes nothing (for a monotone
family lim = lim sup = inf), but the table claims verbatim quotes, so it is an inaccuracy there.
The note itself never prints the formula, so the note is unaffected.

Vanishing on u_j: supp u_j ⊂ {1/(2j) ≤ x ≤ 2/j} × supp g, so {0 < x < ε} ∩ supp u_j = ∅ for
ε ≤ 1/(2j), and P_k u_j vanishes there by locality (supp P_k u_j ⊂ supp u_j). So the inner sup is
0 for all ε ≤ 1/(2j), and ‖u_j‖′_{k,m} = 0 — for every j, every k, every m. This is exactly the
note's "every seminorm (6.43) vanishes for every j (u_j = 0 on {x < 1/(2j)})".

**AGREE**.  **HOLDS**

## Item 5. The value at (1/j, y_0) (referee item 6)

u_j = j^{−m′} χ(jx) g(y), χ ∈ C_c^∞((1/2, 2)) with χ(1) = 1, g(y_0) = 1. At the point
(x, y) = (1/j, y_0) — in the collar for j > 1/ε_0, and in M̊ since x = 1/j > 0 —

  x^{−m′} |u_j| = (1/j)^{−m′} · j^{−m′} · |χ(j · 1/j)| · |g(y_0)| = j^{m′} · j^{−m′} · 1 · 1 = 1,

so sup_{M̊} x^{−m′}|u_j| ≥ 1 for every j, for every real m′ (positive, negative or zero). The note
prints exactly "(1/j)^{−m′} j^{−m′} χ(1) g(y_0) = 1". Correct. Pointwise evaluation is legitimate
because (6.33) gives 𝒜(M) ⊂ C^∞(M̊) and (6.41) itself states ess sup_M = sup_{M̊}.

**AGREE**.  **HOLDS**

## Item 6. u_j ∈ A^{m_1}(M) for every m_1 — which printed statement? (referee item 7)

Two independent routes, both checked.

(i) Printed: p. 38 (rendered) prints "Ċ^∞(M) = ⋂_m 𝒜^m(M)" — the big operator is ⋂, confirmed on
the image — and C_c^∞(M̊) ⊂ Ċ^∞(M) by definition of Ċ^∞ (smooth, vanishing to infinite order at
∂M). So C_c^∞(M̊) ⊂ ⋂_m A^m(M).

(ii) Direct: u ∈ C_c^∞(M̊), P ∈ Diff_b(M) ⟹ Pu ∈ C_c^∞(M̊), supp Pu ⊂ supp u where
c := min_{supp u} x > 0; so x^{−m_1}|Pu| ≤ max{c^{−m_1}, (max_M x)^{−m_1}} · ‖Pu‖_∞ < ∞ for every
real m_1. Hence u ∈ x^{m_1}L^∞(M) for all P, i.e. u ∈ A^{m_1}(M).

The note cites nothing at this point; it does not need to, and it asserts nothing false.

**AGREE**.  **HOLDS**

## Item 7. Direction of (6.38); which of m′ < m the two assertions need (referee item 8)

Published p. 38, rendered image:  "(6.38)  𝒜^m(M) ⊂ 𝒜^{m′}(M)  (m′ < m)" — the prime is on the
**larger** space, so A^m decreases in m. (Sanity check from the definition: x^m L^∞ shrinks as m
grows, by (6.37) x^m L^∞ ⊂ x^{m′}L^∞ for m′ < m, printed p. 37.) Also consistent with Example 6.11
(p. 38): "the space 𝒜^{−m}(𝕊^l_+) corresponds to the symbol space S^m(ℝ^l)" — the index flips, and
S^m increases in m.

Published p. 39, rendered image, Cor. 6.14 verbatim:

> "**Corollary 6.14** If m′ < m, then the topologies of 𝒜^{m′}(M) and C^∞(M̊) coincide on 𝒜^m(M).
> Therefore the topologies of 𝒜(M) and C^∞(M̊) coincide on 𝒜^m(M)."

and Prop. 6.12 verbatim:

> "**Proposition 6.12** The semi-norms (6.42) and (6.43) together describe the topology of 𝒜^m(M)."

*Prop. 6.12 (note's m′ = m).* Put u_j = j^{−m}χ(jx)g(y) ∈ A^m(M). Every (6.42)-seminorm is 0 for
j large (Item 3), every (6.43)-seminorm is 0 (Item 4), so u_j → 0 in the topology generated by
(6.42)+(6.43); but sup_{M̊} x^{−m}|u_j| ≥ 1 (Item 5) and that is a defining seminorm of A^m(M)
(Item 2), so u_j ↛ 0 in A^m(M). Two topologies for which the same sequence converges and does not
converge are different. **Prop. 6.12 is false, for every m ∈ ℝ and every compact M with ∂M ≠ ∅.**

"Describe the topology" unambiguously means "generate" in this paper's own usage — p. 5 "which is
described by the semi-norms (2.1)" for C^∞(U); p. 38 "The topology of 𝒜^m(M) can be described by
the semi-norms ‖·‖_{k,m}". No weaker reading is available.

*Cor. 6.14, first assertion (note's m′ < m).* u_j = j^{−m′}χ(jx)g(y) ∈ C_c^∞(M̊) ⊂ A^m(M);
u_j → 0 in C^∞(M̊); sup x^{−m′}|u_j| ≥ 1 so u_j ↛ 0 in A^{m′}(M). Hence the A^{m′}- and
C^∞(M̊)-subspace topologies on A^m(M) differ. **False for every pair m′ < m.**

I additionally checked that the failure is correctly attributed. Prop. 6.13 (p. 39: "For m, m′, k ∈
ℕ_0, if m′ < m, then ‖·‖′_{k,m′} = 0 on 𝒜^m(M)") is **true**: u ∈ A^m gives |P_k u| ≤ C x^m, so
x^{−m′}|P_k u| ≤ C x^{m−m′} ≤ Cε^{m−m′} on {0<x<ε} → 0. So the first assertion of Cor. 6.14
follows from Prop. 6.12 + Prop. 6.13, and since 6.13 is true, the defect sits in 6.12 — exactly
where the note puts it. The note's §2 list does not include Prop. 6.13. Correct.

I also confirmed the referee's sub-claim that u_j does **not** refute the second assertion, so that
v_j is genuinely needed: on the collar every P ∈ Diff_b is a C^∞-combination of (x∂_x)^a∂_y^b, and
(x∂_x)^a[χ(jx)] is a polynomial expression in (jx) and χ^{(≤a)}(jx) with jx ∈ (1/2,2) on the
support, hence bounded uniformly in j; so |P u_j| ≤ C_P j^{−m′} on M, and
sup_{M̊} x^{k}|P u_j| ≤ C_P j^{−m′}(2/j)^k = C 2^k j^{−m′−k} → 0 for every k > −m′. So
u_j → 0 in A^{−k}(M) and hence in A(M).

**AGREE** with the first referee on all of item 8.  **HOLDS**

## Item 8. The second assertion of Cor. 6.14: A(M) = ind_k A^{−k}(M), W_k, and v_j (referee item 9)

*The inductive limit.* Published p. 4: "For any inductive/projective system (or spectrum) of
continuous linear maps between LCSs, we have its (locally convex) inductive/projective limit; in
particular, when the inductive/projective spectrum consists of a sequence of continuous inclusions,
their union/intersection is endowed with the inductive/projective limit topology."
Published p. 5, rendered image (pdftotext drops the ⋂/⋃ here and appears to swap them; the image
does not):

> "The above concepts and properties also apply to an inductive/projective spectrum consisting of
> continuous inclusions X_r ⊂ X_{r′} for r < r′ in ℝ because ⋂_r X_r = ⋂_k X_{r_k} and
> ⋃_r X_r = ⋃_k X_{s_k} for sequences r_k ↓ −∞ and s_k ↑ ∞."

The pairing on the rendered page is ⋂ ↔ (r_k ↓ −∞) and ⋃ ↔ (s_k ↑ ∞), which is the correct
pairing for a family increasing in r. **I independently confirm the first referee's withdrawal of
its interim accusation against p. 5** — there is no slip there; the pdftotext artifact created it.

Setting X_r := A^{−r}(M) makes X_r increasing in r by (6.38), and (6.40) (rendered: "𝒜(M) = ⋃_m
𝒜^m(M)") plus the p. 5 sentence give A(M) = ⋃_k A^{−k}(M) with the locally convex inductive limit
topology of the sequence. The paper also says on p. 38 that the A^{(s)}- and A^m-filtrations define
"the same LF-space", so nothing turns on which filtration is meant.

*W_k is a 0-neighborhood of A^{−k}(M).* It is the open ball of radius ε_k for the P = 1 seminorm at
order m = −k: sup_{M̊} x^{−(−k)}|u| = sup_{M̊} x^k |u|. Item 2 shows that is a defining seminorm.
ε_k := ½ inf_{i≥1} e^i i^{−k} > 0: the real function t ↦ e^t t^{−k} has its minimum on (0,∞) at
t = k with value (e/k)^k > 0 (for k = 0 the inf is e), so the inf over integers i ≥ 1 is ≥ (e/k)^k
> 0. Positive, as the note asserts.

*W is a 0-neighborhood of A(M).* W := absolutely convex hull of ⋃_k W_k. For a locally convex
inductive limit of a sequence of steps, the absolutely convex sets whose trace on every step is a
0-neighborhood form a base at 0. W ∩ A^{−k} ⊇ W_k is a 0-neighborhood of A^{−k}; W is absolutely
convex by construction; it is absorbing because every u ∈ A(M) lies in some A^{−k}, where W_k
absorbs it. So W is a 0-neighborhood. **Addition to the first referee:** the conclusion is robust
against the objection "but maybe A(M) carries the A^{(s)}-inductive topology". It does not matter:
by (6.39)'s second inclusion (always valid) and its first inclusion in the range it *is* valid
(m = −k < 0, s > −k + n/2 + 1), A^{(s)} ⊂ A^{−k} continuously for k large, so W_k ∩ A^{(s)} is a
0-neighborhood of A^{(s)} too, and W is a 0-neighborhood for that inductive topology as well.

*v_j ∉ W.* v_j := e^j χ(jx) g(y) ∈ C_c^∞(M̊) ⊂ every A^{m_1}(M); v_j → 0 in C^∞(M̊) (supports leave
every compact of M̊). Suppose v_j = Σ_i λ_i w_i with a finite sum, Σ_i|λ_i| ≤ 1, w_i ∈ W_{k_i}.
Evaluate at p_j = (1/j, y_0) ∈ M̊ (legitimate: (6.33)). From sup_{M̊} x^{k_i}|w_i| < ε_{k_i},

  |w_i(p_j)| < ε_{k_i} · x(p_j)^{−k_i} = ε_{k_i} j^{k_i}
             = ½ (inf_{i′≥1} e^{i′} i′^{−k_i}) j^{k_i} ≤ ½ e^{j} j^{−k_i} j^{k_i} = ½ e^{j},

taking i′ = j in the infimum. Hence |v_j(p_j)| ≤ Σ_i |λ_i| |w_i(p_j)| ≤ ½ e^j. But
v_j(p_j) = e^j χ(1) g(y_0) = e^j > ½ e^j. Contradiction. So v_j ∉ W for every j, hence
v_j ↛ 0 in A(M) while v_j → 0 in C^∞(M̊), and both sequences lie in A^m(M) for every m.
**The second assertion of Cor. 6.14 is false for every m ∈ ℝ.** No regularity, completeness or
Hausdorffness of A(M) is used.

**AGREE** with the first referee, with the A^{(s)}-robustness argument added.  **HOLDS**

## Item 9. Transfer to J^m(M, L) and Cor. 7.13, both assertions (referee item 10)

Published p. 56, read from the rendered image (bold face and the sub/superscript star are invisible
to pdftotext, so the image matters here):

> "(7.26)  𝛑_* : 𝒜(𝑴) ≅→ J(M, L) ,  where 𝒜(𝑴) is defined in (6.29). By (6.33), there is a
> continuous inclusion  J(M, L) ⊂ C^∞(M∖L).
> We also get spaces J^{(s)}(M, L) and J^m(M, L) (s, m ∈ ℝ) corresponding to 𝒜^{(s)}(𝑴) and
> 𝒜^m(𝑴) via (7.26). Extend |x| to a function 𝒙 on M that is positive and smooth on M∖L. Its lift
> 𝛑^*𝒙 is a boundary defining function of 𝑴, also denoted by 𝒙. …
> (7.27)  J^{(s)}(M,L) = { u ∈ C^{−∞}(M,L) | Diff(M,L) u ⊂ H′^s(M,L) } ,
>         J^m(M,L) = { u ∈ C^{−∞}(M,L) | Diff(M,L) u ⊂ 𝒙^m L^∞(M) } ,
> equipped with topologies like in Sects. 6.8 and 6.10. These spaces satisfy the analogs of (4.4),
> (6.29) and (6.38)–(6.40)."

> "**Corollary 7.13** If m′ < m, then the topologies of J^{m′}(M, L) and C^∞(M∖L) coincide on
> J^m(M, L). Therefore the topologies of J(M, L) and C^∞(M∖L) coincide on J^m(M, L)."

Confirmed on the image: (7.26) is **π with a subscript star** (push-forward) and its domain is
𝒜(**𝑴**), bold; (7.27) has **bold 𝒙** and **ordinary M** in L^∞(M) — exactly as the note prints
them. Cor. 7.13's primes are as the note quotes them.

Setting (published pp. 50–51, §7.1): M closed connected, L ⊂ M a regular closed submanifold of
codimension one, transversely oriented; a tubular neighborhood T ≡ (−ε, ε)_x × L with L = {x = 0},
adapted charts {U_j ≡ (−ε,ε)_x × V_j, (x,y)}; 𝑴 the manifold with boundary got by "cutting" M along
L, with 𝑴̊ ≡ M∖L. So 𝒙 = |x| on T, and on {1/(2j) < x < 2/j} ⊂ T (for j > 2/ε) with x > 0 we have
𝒙 = x. The note's clause is therefore right; **nit:** the note attaches "(p. 56)" to a sentence
whose "𝑴 obtained by cutting M along L" half is defined on p. 50, not p. 56 (p. 56 supplies the
rest: 𝒙, its lift, and 𝑴's boundary defining function). Purely a citation nit.

The P = 1 seminorm on J^m: "topologies like in Sects. 6.8 and 6.10" means the projective topology
given by the maps P : J^m(M,L) → 𝒙^m L^∞(M), P ∈ Diff(M,L); and 1 ∈ Diff^0(M,L) = C^∞(M), because
p. 19 defines Diff(M,L) "like in Sect. 2.7" and Sect. 2.7 gives Diff^0(M) ≡ C^∞(M). So
u ↦ sup_{M∖L} 𝒙^{−m}|u| is continuous on J^m(M,L). (Same conclusion via (7.26): J^m ≅ A^m(𝑴), and
𝒙 is a boundary defining function of 𝑴, so this is (6.41) with P = 1 on 𝑴.)

Membership: for u ∈ C_c^∞(M∖L) and P ∈ Diff(M,L) ⊂ Diff(M), Pu ∈ C_c^∞(M∖L), and on supp Pu ⊂
supp u we have 𝒙 ≥ c > 0 (𝒙 positive continuous on M∖L, supp u compact there), so 𝒙^{−m}|Pu| is
bounded for every real m. Hence C_c^∞(M∖L) ⊂ J^m(M,L) for every m.

With u_j = j^{−m′}χ(jx)g(y) and v_j = e^j χ(jx)g(y) placed in {1/2 < jx < 2} ⊂ M∖L: both are in
C_c^∞(M∖L) ⊂ every J^{m_1}; both → 0 in C^∞(M∖L); sup 𝒙^{−m′}|u_j| ≥ 1 at (1/j, y_0), refuting the
first assertion; and, since p. 56 explicitly grants the analogs of (6.38)–(6.40), J(M,L) =
⋃_k J^{−k}(M,L) as a locally convex inductive limit, so the W_k/W construction of Item 8 transfers
verbatim with 𝒙 for x and refutes the second assertion. **Both assertions of Cor. 7.13 are false.**

**AGREE** with the first referee's ruling — **but with one correction to its supporting chain**,
see Item 12.  **HOLDS**

## Item 10. Memoir arXiv:2402.06671, §2.5.10 (p. 38) and §2.6.7 (p. 53) (referee item 11)

I extracted both PDFs with `pdftotext -layout`: `fetched-r3/r3s-17-…2402.06671v1-SESSION8-FETCH.pdf`
(stamp "arXiv:2402.06671v1 [math.GT] 7 Feb 2024") and `…r3s-39-…v2-SESSION16-FETCH.pdf` (stamp
"…v2 [math.GT] 13 Feb 2024"), both 176 pages.

**§2.5.10, printed p. 38.** The running head " 38   2. ANALYTIC TOOLS" stands immediately before
"2.5.10. Filtration of A(M) by bounds" (v1 line 2283/2286, v2 line 2284/2287), and the next head is
"2.5. SMALL B-CALCULUS  39". Inside that page:

> "The following is true [ÁLKL23, Corollaries 6.14–6.16 and 6.39 and Remark 6.41]: **the topologies
> of A(M) and C^∞(M̊) coincide on every A^m(M)** (however the second inclusion of (2.5.32) is not a
> TVS-embedding); C_c^∞(M̊) is dense in every A^m(M), and therefore in every A^{(s)}(M) and A(M);
> and A(M) is an acyclic Montel space, and therefore complete, boundedly/compactly/sequentially
> retractive and reflexive."

That is verbatim the **second** assertion of Cor. 6.14, and it is asserted for *every* m.

**§2.6.7, printed p. 53.** The head "2.6. CONORMAL SEQUENCE  53" sits inside §2.6.7 (v1 line 3188,
v2 line 3189) and the sentence below follows it (v2 lines 3205–3206), before the next head ("… 55"):

> "Moreover the following properties hold [ÁLKL23, Corollaries 7.11–7.13 and 7.15]: every
> J^{(s)}(M,L) is a totally reflexive Fréchet space; J(M,L) is barreled, ultrabornological, webbed
> and an acyclic Montel space, and therefore complete, boundedly/compactly/sequentially retractive
> and reflexive; and **the topologies of J(M,L) and C^∞(M∖L) coincide on every J^m(M,L)**."

That is verbatim the **second** assertion of Cor. 7.13.

`diff` of the two extractions shows only front-matter/whitespace differences (the arXiv stamp and
title-page spacing); the two quoted sentences and the two running heads are identical in v1 and v2.
So the note's "(\cite{ALKL24m} restates these second assertions at §2.5.10, p. 38, and §2.6.7,
p. 53.)" and its bibliography line "(v2, 13 February 2024; the pages cited are the same in v1)" are
both exactly right.

**AGREE**.  **HOLDS**

## Item 11. Is the external assessment's description of (e) accurate? (referee item 12)

The external reader's four factual claims about (e), each checked against the printed text:

1. "The paper explicitly says Proposition 6.12 gives the topology of A^m(M) from (6.42), (6.43)"
   — **correct**, verbatim (p. 39).
2. "and then Corollary 6.14 asserts coincidence with C^∞(M°)" — **correct**, verbatim (p. 39).
3. "Your u_j = j^{−m′}χ(jx)g(y) is a direct witness against that claim" — **correct** (Items 3–7).
4. "the paper's Corollary 7.13 really does assert the corresponding statement for J^m(M,L). Your
   collar example therefore propagates to J for exactly the reason you give." — **correct**
   (Item 9), and the reason the note gives — (7.27) with Diff(M,L) and 𝒙^m L^∞(M), 𝒙 extending
   |x| — is the right one.

The one sentence that misreads the paper: "The calculation using the global weighted seminorm
(6.41) is particularly persuasive because it isolates exactly **the seminorm the paper's
Proposition 6.12 says is part of the topology**." Proposition 6.12 says no such thing about (6.41).
(6.41) is part of the topology of A^m(M) by the **definition** on p. 38 (projective topology over
P ∈ Diff_b(M); the ‖·‖_{k,m} are named as describing it). Prop. 6.12's content is the *further*
claim that (6.42) + (6.43) already generate that topology — i.e. that they **control** (6.41) —
and it is that entailment the witness kills. On a charitable loose reading ("a seminorm continuous
for the topology Prop. 6.12 describes") the sentence is a true consequence of Prop. 6.12, so it is
sloppy rather than false; but as written it attributes to a proposition what belongs to a
definition.

Repair (one sentence): "…because it isolates a seminorm that belongs to the topology of A^m(M) by
its definition on p. 38, and that Proposition 6.12 therefore claims is controlled by (6.42) and
(6.43)."

The assessment also omits, for (e), the *second* assertions of Cors. 6.14 and 7.13, the witness v_j
that is needed for them (u_j does not do it — Item 7), and the memoir's restatements. Omissions,
not errors.

**AGREE** with the first referee's ruling here.  **HOLDS-WITH-REPAIR** (repair as above; the repair
is to the external assessment, not to the note)

## Item 12. What the first referee got wrong or passed too quickly

**(a) The companion's J-membership citation chain is invalid.** Companion §6, last paragraph:

> "u_j, v_j ∈ C_c^∞(M∖L) ⊂ C^∞(M) ⊂ J^{(∞)}(M, L) ⊂ J^{m_1}(M, L) for all m_1 (p. 56, (7.28);
> directly: Pu_j is smooth and compactly supported away from L)"

The last inclusion, J^{(∞)}(M,L) ⊂ J^{m_1}(M,L) for **all** m_1, is the J-analog of (6.39)'s first
inclusion, and it is **false for every m_1 > 0**. Concretely: 1 ∈ C^∞(M) ⊂ J^{(∞)}(M,L) by (7.28)
as printed; but 1 ∈ Diff^0(M,L)·1 and 𝒙^{−m_1}·1 is unbounded near L, so 1 ∉ J^{m_1}(M,L) for
m_1 > 0. So (7.28) does **not** deliver the membership the argument needs.

The conclusion is nevertheless correct, because the companion's own parenthetical — the direct
argument — is valid and sufficient (Item 9). Repair: in companion §6, delete "C^∞(M) ⊂ J^{(∞)}(M,L)
⊂ J^{m_1}(M,L) for all m_1 (p. 56, (7.28); " and keep only "C_c^∞(M∖L) ⊂ J^{m_1}(M,L) for all m_1
(directly: for P ∈ Diff(M,L), Pu is smooth and compactly supported in M∖L, where 𝒙 ≥ c > 0)."
The first referee's item 10 lists (7.28) among the quoted anchors and then asserts "u_j, v_j ∈
C_c^∞(M∖L) ⊂ every J^{m_1}" without separating the two routes, so it certifies the chain without
flagging it. **The note is unaffected** — it never invokes (7.28).

**(b) A genuine error in the published paper that neither the note nor the first referee records:
(6.39)'s first inclusion is false, and contradicts the paper's own p. 36 and p. 38.** Purely
internal argument, no outside input:
* (6.31), p. 36 (rendered): ⋂_s 𝒜^{(s)}(M) = C^∞(M). Hence 1 ∈ 𝒜^{(s)}(M) for every s.
* (6.39), p. 38 (rendered): 𝒜^{(s)}(M) ⊂ 𝒜^m(M) ⊂ 𝒜^{(min{m,0})}(M)  (m < s − n/2 − 1). Given any
  m ∈ ℝ, take s > m + n/2 + 1; the first inclusion then puts 1 ∈ 𝒜^m(M).
* p. 38 (rendered): Ċ^∞(M) = ⋂_m 𝒜^m(M). So 1 ∈ Ċ^∞(M) — false, since Ċ^∞(M) consists of smooth
  functions vanishing to infinite order at ∂M ≠ ∅.
Directly: 1 ∈ 𝒜^m(M) requires x^{−m} ∈ L^∞(M), which fails for every m > 0, while 1 ∈ 𝒜^{(s)}(M)
for every s. The true statement is 𝒜^{(s)}(M) ⊂ 𝒜^m(M) for m < min{s − n/2 − 1, 0}. Nothing in the
paper is damaged: (6.40) ("Hence 𝒜(M) = ⋃_m 𝒜^m(M)") uses only the case m → −∞, where the
inclusion holds. The same over-statement is reproduced in the memoir at (2.5.37), p. 38, and in the
J-analog implicit in the p. 56 sentence "These spaces satisfy the analogs of … (6.38)–(6.40)".
This is *not* a defect of the note; it is an additional (harmless) misprint the cross-check turned
up. It is also why (a) above is a real gap and not a quibble.

**(c) A second printed slip on p. 36, also unrecorded.** The definitions read
Ȧ^{(s)}(M) = {u ∈ Ċ^{−∞}(M) | Diff_b(M)u ⊂ Ḣ^s(M)}, 𝒜^{(s)}(M) = {u ∈ C^{−∞}(M) | Diff_b(M)u ⊂
H^s(M)}, and the very next sentence says "with the projective topologies given by the maps
P : Ȧ^{(s)}(M) → H^s(M) and P : 𝒜^{(s)}(M) → Ḣ^s(M) (P ∈ Diff_b(M))" — the two targets are
**swapped** relative to the definitions. Harmless typo; unrelated to (e); recorded for completeness.

**(d) Small nits the first referee did not list.** (i) The companion's §0 anchor table prints (6.43)
with "limsup_{ε↓0}" where the page prints "lim_{ε↓0}" (equal here, but the table claims verbatim
quotes). (ii) The note's "(p. 56)" in (e) covers a clause half of which ("𝑴 obtained by cutting M
along L") is defined on p. 50. (iii) The note leaves the J-membership u_j, v_j ∈ J^{m_1}(M,L)
implicit; one clause ("both lie in C_c^∞(M∖L), hence in every J^{m_1}(M,L)") would close it and is
worth adding precisely because the obvious citation route, (7.28), does not work — see (a)/(b).

**Ruling on the first referee's report as a whole: HOLDS-WITH-REPAIR** — its verdict on witness (e)
is right and its thirteen items are right, except that item 10 passes an invalid citation chain
(repair (a)) and it misses (b), (c), (d).

## Item 13. Hostile attacks I tried, and why each failed

1. **"(6.42) is over compacts of M, not M̊."** The rendered p. 39 prints K ⊂ M̊. And even under the
   M-reading the witness survives for m > 0 (Item 3).
2. **"Maybe (6.42)/(6.43) are meant with all m simultaneously."** (6.42) does not involve m at all;
   (6.43) at *any* order m″ still vanishes on u_j, because u_j ≡ 0 near ∂M. The witness is
   insensitive to this.
3. **The strongest form of the refutation.** Whatever the exact index set, the paper asserts the
   (6.42) family consists of C^∞(M̊)-continuous seminorms ("From (2.1) and (6.33)"), and u_j → 0 in
   C^∞(M̊); and (6.43) vanishes identically on u_j. So Prop. 6.12 falls under *every* reading in
   which (6.42) is C^∞(M̊)-continuous. There is no escape by re-reading the seminorm families.
4. **"P = 1 is not one of the P_k."** Two independent answers: the definition on p. 38 is the
   projective topology over *all* P ∈ Diff_b(M); and 1 = Σ_{j∈F} f_j P_j gives
   sup x^{−m}|u| ≤ Σ‖f_j‖_∞‖u‖_{j,m} (Item 2).
5. **"u_j is not in A^m(M)" / "pointwise evaluation of a distribution is illegal."**
   C_c^∞(M̊) ⊂ Ċ^∞(M) = ⋂_m A^m(M) (p. 38), and (6.33) makes every element of A(M) a smooth
   function on M̊, with (6.41) itself asserting ess sup_M = sup_{M̊}.
6. **"Sign of the exponent."** Checked at x = 1/j for arbitrary real m′, positive and negative:
   j^{m′}·j^{−m′} = 1 identically (Item 5). No sign convention rescues the statement.
7. **"Wrong LF filtration for A(M)."** The p. 38 sentence says both filtrations define the same
   LF-space; and independently W is a 0-neighborhood for the A^{(s)}-inductive topology as well
   (Item 8).
8. **"W might not be a 0-neighborhood / might not be absorbing."** Absolutely convex, trace on each
   step a 0-neighborhood, absorbing because every u lies in some step (Item 8).
9. **"ε_k might be 0."** min_{t>0} e^t t^{−k} = (e/k)^k > 0 (Item 8).
10. **"𝒙 ≠ x on the witness's support" / "the collar coordinate is only comparable to x."** The
    collar is T ≡ [0, ε_0)_x × ∂M, so the coordinate *is* x (Item 1); and 𝒙 = |x| on the tubular
    neighborhood T of L, so 𝒙 = x on {1/(2j) < x < 2/j} for j large (Item 9).
11. **"Cor. 7.13 might not assert what the note says."** Verified verbatim from the rendered page,
    primes included (Item 9).
12. **"The memoir might phrase it differently, or v1 might differ from v2."** Verified verbatim in
    both, with the running heads pinning pp. 38 and 53 (Item 10).
13. **"Prop. 6.13 might be the false one, so the note blames the wrong statement."** Prop. 6.13 is
    true; the proof is two lines (Item 7).

None of the thirteen produced a counterexample to any step of witness (e).

## Summary of rulings

| # | Item | Ruling | vs. first referee |
|---|---|---|---|
| 1 | Collar chart = boundary defining function (p. 30) | HOLDS | AGREE |
| 2 | A^m(M), projective topology, "(6.41) with P = 1" (p. 38) | HOLDS | AGREE + domination proof |
| 3 | (6.42) is over compact K ⊂ M̊ (p. 39); vanishing on u_j | HOLDS | AGREE |
| 4 | (6.43) is lim_{ε↓0} sup (p. 39); vanishes on u_j | HOLDS | AGREE (+ companion nit) |
| 5 | the value sup x^{−m′} of the modulus of u_j is ≥ 1 at (1/j, y_0) | HOLDS | AGREE |
| 6 | u_j ∈ A^{m_1}(M) ∀m_1 (p. 38 Ċ^∞ = ⋂_m A^m; direct) | HOLDS | AGREE |
| 7 | (6.38) direction; Prop. 6.12 (m′=m) and Cor. 6.14 first assertion (m′<m) | HOLDS | AGREE + Prop. 6.13 check |
| 8 | Second assertion: A(M)=ind_k A^{−k}, W_k, W, v_j ∉ W | HOLDS | AGREE + A^{(s)} robustness |
| 9 | Cor. 7.13 both assertions via (7.26)/(7.27), 𝒙 (p. 56) | HOLDS | AGREE, chain corrected |
| 10 | Memoir §2.5.10 p. 38, §2.6.7 p. 53, v1 = v2 | HOLDS | AGREE |
| 11 | External assessment's reading of (6.41)/Prop. 6.12 | HOLDS-WITH-REPAIR | AGREE |
| 12 | Companion's (7.28) chain; paper's (6.39), p. 36 swap; nits | (see text) | **new — referee missed** |
| 13 | Hostile attacks | all defeated | AGREE + 3 new attacks |

**Bottom line.** Witness (e) in the *note* stands, exactly as printed, against Prop. 6.12 (p. 39),
both assertions of Cor. 6.14 (p. 39), both assertions of Cor. 7.13 (p. 56) and the memoir's
restatements at §2.5.10 (p. 38) and §2.6.7 (p. 53). No repair to the note is required; the two
optional improvements are the "(p. 56)" citation (Item 12(d)(ii)) and one clause making the
J-membership explicit (Item 12(d)(iii)). One repair *is* required to the **companion**: delete the
(7.28) route in §6 (Item 12(a)). Two further published-paper misprints, (6.39) and the p. 36
projective-topology sentence, are recorded for the record; neither touches the note's claims.

*Report completed; machine clock recorded at the top. Verifier: second-model (Opus 5).*

## Addendum — the two quotes underpinning Item 12(b), read on the published pages

* p. 31, (6.3): "The Fréchet space of supported functions is the closed subspace of the smooth
  functions on M that vanish to all orders at the points of ∂M,
  (6.3)  Ċ^∞(M) = ⋂_{m≥0} x^m C^∞(M) ⊂ C^∞(M)."
  So 1 ∉ Ċ^∞(M) whenever ∂M ≠ ∅ — which closes the contradiction in Item 12(b) — and
  C_c^∞(M̊) ⊂ Ċ^∞(M), which is the membership route used in Item 6.
* p. 36, (6.31) (rendered image): "⋂_s Ȧ^{(s)}(M) = Ċ^∞(M) ,  ⋂_s 𝒜^{(s)}(M) = C^∞(M)."
  So 1 ∈ 𝒜^{(s)}(M) for every s, with no need to know what H^s(M) is.

**Finished:** Sun Sep  6 13:17:32 IST 2026
