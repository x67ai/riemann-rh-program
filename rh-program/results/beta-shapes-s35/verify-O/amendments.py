# Reader (Opus 5) OLD/NEW amendments to results/beta-shapes-s35/NOTE.md, machine-applicable.
# Each entry: (id, kind, expected_count, OLD, NEW). kind FIX = FIX-FIRST; AMEND = recommended.
# Apply with apply_check.py (writes only to a scratch copy unless --apply-to is given by the orchestrator).
A = []
def add(i, kind, n, old, new): A.append((i, kind, n, old, new))

# ---------------- FIX-FIRST ----------------
add('F1', 'FIX', 1,
 "What a (D4) rung would have to be: a base with at least two residue characteristics (so that Theorem R bites) and a target",
 "What a (D4) rung would have to be: a base with infinitely many residue characteristics (Theorem R with its converse, §2.3: over a base with finitely many, dim_Q G ≤ |char(B)| < ∞, so (D4) is empty there — two residue characteristics do not make Theorem R bite) and a target")
add('F2', 'FIX', 1,
 "It does NOT have (b) a rung-1 model: rung 1 is (D3)-shaped by Theorem R's arithmetic (one residue characteristic), no infinite-genus pair is on the record on any rung (§3.5), and the only base on which (D4) can be tested is the arithmetic case itself.",
 "Its axioms keep the SPEC's rung-1 model only in (D3) form: the curve pair satisfies A8′, A11′, A13′ in their rung-1 specializations (δ_S = 2g − 2; G = Q · log q; h = 2g), but it is (D3)-shaped by Theorem R's arithmetic (one residue characteristic), so it tests the reduction of the primed clauses to A8, A11, A13 and never their (D4) content; no infinite-genus pair is on the record on any rung (§3.5), and by Theorem R with its converse (§2.3) the only bases on which (D4)'s content can be tested have infinitely many residue characteristics — the arithmetic case itself. And the thing the s28 definition asks to be PROPOSED is absent: its own gloss reads \"the SPEC supplies the axioms and the rung-1 model, and no candidate for the target over Z is on the record\" (`results/program-digest-s28.md` line 266) — a candidate object is a proposed target (β, Y, c) over Z, and (D4) is a shape such a proposal must have, not a proposal (§0; V.1).")
add('F3', 'FIX', 1,
 "**a base B with at least two residue characteristics for which a target (β, Y, c) satisfying A6, A7, A9, A11′ and A8′/A13′ is KNOWN**",
 "**a PROPOSED target (β, Y, c) of shape (D4) over a base B with infinitely many residue characteristics (Spec Z or a number ring) satisfying A6, A7, A9, A11′ and A8′/A13′ — with no rung below the arithmetic case on which its (D4) content could first be checked**")
add('F4', 'FIX', 1,
 "The candidate-object question is NO: (D4) has axioms and a written DH failure (A5, unchanged) and no rung-1 model, and it can have none — rung 1 is finite-rank by the arithmetic of one residue characteristic; the missing piece is a base with at least two residue characteristics on which a (D4) target is KNOWN, and no page prints one.",
 "The candidate-object question is NO: the s28 candidate is a PROPOSED target over Z (\"the SPEC supplies the axioms and the rung-1 model, and no candidate for the target over Z is on the record\", `results/program-digest-s28.md` line 266), and (D4) is a shape, not a proposal; the amended axioms keep the curve pair as their rung-1 model only in its (D3)-shaped specialization, because by Theorem R and its converse (D4)'s content lives exactly over bases with infinitely many residue characteristics — the arithmetic case — so no lower rung can test it; no page prints a (D4) target.")
add('F5', 'FIX', 1,
 "(a) a (D4) rung — a base with ≥ 2 residue characteristics carrying a KNOWN target (§3.5)",
 "(a) a (D4) rung — a base with infinitely many residue characteristics carrying a KNOWN target (§3.5)")
add('F6', 'FIX', 1,
 "candidate object NO (no rung; the rung would be a base with ≥ 2 residue characteristics)",
 "candidate object NO (no proposed target over Z; (D4)'s content is testable only over bases with infinitely many residue characteristics — the arithmetic case)")
add('F7', 'FIX', 1,
 "(a) a (D4) rung — a base with at least two residue characteristics carrying a KNOWN target",
 "(a) a (D4) rung — a base with infinitely many residue characteristics carrying a KNOWN target")
add('F8', 'FIX', 1,
 "the rung for (D4) is a base with ≥ 2 residue characteristics",
 "the rung for (D4) is a base with infinitely many residue characteristics")
add('F9', 'FIX', 1,
 "NEW (A11′): the same, plus: the pairing is real-valued; its diagonal-row span G is infinite-dimensional over Q; and for every prime p",
 "NEW (A11′): the same, plus: the pairing is real-valued; over a base with infinitely many residue characteristics its diagonal-row span G is infinite-dimensional over Q (over a base with finitely many, dim_Q G ≤ |char(B)| and this part of the clause is void — which is what lets the rung-1 specialization below hold); and for every prime p")
add('F10', 'FIX', 1,
 "**Claim.** Every triple (β, Y, c) satisfying A6, A7, A8 and A11 lies in exactly one of (D1), (D3), (D4); (D2) is a named sub-shape of (D1).",
 "**Claim.** Every triple (β, Y, c) satisfying A6, A7, A8 and A11 whose diagonal-row intersection numbers (Δ · c(Γ_n))_Y, n ≥ 2, are real numbers lies in exactly one of (D1), (D3), (D4); (D2) is a named sub-shape of (D1). (A11 as printed does not name the value group; A9's equation with a real κ > 0 forces real diagonal-row values, so a triple whose diagonal row is not real-valued fails A9 by type and needs no theorem — it is the only triple outside the four cells, and it is outside the question. The shapes are properties of TRIPLES: one β may carry triples in several cells, which is harmless because (D1)–(D3) are empty.)")
add('F11', 'FIX', 1,
 "A8 and A11 supply the real-valued pairing on Y's divisor classes",
 "A8 and A11 supply the pairing on Y's divisor classes, and the Claim's hypothesis makes its diagonal row real")
add('F12', 'FIX', 1,
 "any brief presenting Deligne-style rationality (finitely many eigenvalues of fixed weight) as available on a square of Spec Z;",
 "any brief presenting Deligne-style rationality (finitely many eigenvalues whose traces are integers — a characteristic polynomial over Z, (H-Lef_Z)) as available on a square of Spec Z (finitely many transcendental eigencharacters with non-injective c — the sub-shape (D4-fin) of NOTE §3.4 — is NOT killed);")
add('F13', 'FIX', 1,
 "p. 3, 2.7: \"There is a canonical anti-linear automorphism",
 "p. 3, 2.7: \"There is a canononical [sic] anti-linear automorphism")
add('F14', 'FIX', 1,
 "p. 5: \"Finally we expect a C-antilinear Hodge",
 "pp. 4–5: \"Finally we expect a C-antilinear Hodge")

# ---------------- AMEND (recommended) ----------------
add('M1', 'AMEND', 1,
 "*Proof of T3.*",
 "**Converse, and the hypotheses the proof actually uses (reader, 2026-09-29).** Under H3.1–H3.2 every N_D has its prime support inside char(B) (Λ_B is supported on the log N(𝔪), and N(𝔪) is a power of a residue characteristic), so dim_Q G ≤ |char(B)|; with Theorem R, dim_Q G < ∞ exactly when char(B) is finite — (D3) is the finite-characteristic case and (D4) is non-empty only over bases with infinitely many residue characteristics. The proof reads only the fibers of c on components: A7's graph structure is not used (it enters Lemma F(b)–(c), not Theorem R). The ONE fixed κ of A9 is used: with a normalization κ_D allowed to depend on D, every value could be 1 and the theorem fails; H3.2 states the fixed κ, as SPEC A9 prints it. *Proof of T3.*")
add('M2', 'AMEND', 1,
 "`[novelty: single-check]` — arXiv searches recorded in SHARED.md; nothing found by title words (§6.1).",
 "(5) Borger 0906.3146 §7.7 p. 27 (read at the page by the reader): \"So, objects of F^S_1 are generalized—but not weakened—versions of separated reduced algebraic spaces over the point Spec k. Of course this makes essential use of equal characteristic. The corresponding interpretation of Λ-spaces in the usual sense, over Z, would be that while it is possible to say what it means to descend an algebraic space to F1—that is, to give it a Λ-action—we do not know if there is a uniformity property, which is what we would need to create a true arithmetic analogue of the base point Spec k.\" — the printed free slot, and the printed remark that rung 1 uses equal characteristic; exact difference: Borger's remark is about descent (a uniformity PROPERTY), Theorem R is a theorem on the pair's PAIRING at the same coordinate (one residue characteristic versus infinitely many). (6) x-18 p. 4: \"So the foliation setting allows for a product formula where the N γ are not all powers of the same number.\" — Corollary 3.2's dynamical twin (on rung 1 every fiber product is a power of q). (7) Connes–Consani 1603.03191 abstract, p. 1: \"prove the Riemann-Roch formula which involves real valued dimensions, as in the type II index theory\" — a printed real-valued invariant on the per-prime orbit C_p = R*_+/p^Z, not a pairing on a square. `[novelty: dual-model check 2026-09-29]` — writer's 22 arXiv queries (SHARED.md, §6.1) and the reader's 20 (`verify-O/arxiv-O-parsed.txt`, positive controls passing); nothing prints Theorem R, Lemma F or Proposition 2.2.1; the arithmetic core (Q-linear independence of {log p}) is classical and is not claimed.")
add('M3a', 'AMEND', 1, "`[novelty: single-check]` for Lemma F as a statement", "`[novelty: dual-model check 2026-09-29]` for Lemma F as a statement")
add('M3b', 'AMEND', 1, "carries no fiber sum. `[novelty: single-check]`.", "carries no fiber sum. `[novelty: dual-model check 2026-09-29]`.")
add('M3c', 'AMEND', 1, "`[novelty: single-check]` for (i)–(iii) as a statement", "`[novelty: dual-model check 2026-09-29]` for (i)–(iii) as a statement")
add('M3d', 'AMEND', 1, "neither printed over Z. `[novelty: single-check]`.", "neither printed over Z. `[novelty: dual-model check 2026-09-29]`.")
add('M4', 'AMEND', 1, "`[novelty: single-check → the reader flips]`", "`[novelty: dual-model check 2026-09-29]` (writer 22 arXiv queries, reader 20, positive controls passing; `results/beta-shapes-s35/read-O.md` §2.9)")
add('M5', 'AMEND', 2, "`[novelty: single-check → reader]`", "`[novelty: dual-model check 2026-09-29]`")
add('M6', 'AMEND', 1,
 "**Theorem R:** if the Q-linear span G of the diagonal row {(Δ · c(Γ_n))_Y : n ≥ 2} is finite-dimensional, then B has finitely many residue characteristics.",
 "**Theorem R:** if the Q-linear span G of the diagonal row {(Δ · c(Γ_n))_Y : n ≥ 2} is finite-dimensional, then B has finitely many residue characteristics; conversely dim_Q G ≤ |char(B)| always, so dim_Q G < ∞ exactly when char(B) is finite (A9's one fixed κ is used; A7 only names the fibers of c).")
add('M7', 'AMEND', 1,
 "Durov 0704.2030 p. 43 (the F₁-square is the diagonal).",
 "Durov 0704.2030 p. 43 (the F₁-square is the diagonal); Borger 0906.3146 §7.7 p. 27 (\"Of course this makes essential use of equal characteristic\" — the printed remark at Theorem R's coordinate, on descent, not on a pairing); Deninger x-18 p. 4 (\"the N γ are not all powers of the same number\" — Corollary 3.2's dynamical twin).")
add('M8', 'AMEND', 1,
 "evaluating on Γ_n ≅ B: for b ∈ B, c(Γ_n) ∋ (b, φ_n(b))",
 "evaluating on Γ_n ≅ B, with c restricted to Γ_n written as b ↦ (b, φ_n(b)) — the rung-1 form (pr, Fr^n_T) of p. 25, taken here as part of A7(T2b)'s graph identification (A7 fixes the image of Γ_n, not its parametrization; with c|Γ_n = (σ_n, φ_n ∘ σ_n) for β-automorphisms σ_n of B the computation below changes) — for b ∈ B, c(Γ_n) ∋ (b, φ_n(b))")
add('M9', 'AMEND', 1,
 "Hodge index gives an inequality on the square, and A13 item 4 over Z gives the tower Λ(n) and no rationality.",
 "Hodge index gives an inequality on the square, and A13 item 4 over Z gives the tower Λ(n) and no rationality. (Reader's precision: on a finite-rank Num(Y) the identity (Δ · Γ) = 1 + d(Γ) − σ(Γ), with Weil's σ(D) := d₁(D) + d₂(D) − (D · Δ) (Milne p. 11), is a DEFINITION of σ and holds tautologically; the content of (H-Lef) is that n ↦ σ(Γ_{φ_n}) is the trace of a MULTIPLICATIVE family on a finite-dimensional space, which needs the composition of correspondences through the triple product (Milne pp. 10–11, D₁ ∘ D₂ = p₁₃*(p₁₂*D₁ · p₂₃*D₂) and (8)) — structure beyond the square and beyond A6–A13.)")
add('M10', 'AMEND', 1,
 "hence at most ONE prime has d_p > C_g (two such primes would give d_p d_q > C_g² ≥ C_g)",
 "hence NO prime has d_p > C_g (for any second prime q, d_q ≥ 1 gives d_p d_q > C_g), and g = 0 is excluded at the first composite (d + 1 ≤ 0)")
add('M11', 'AMEND', 1,
 "and nothing more; the Opus reader's independent search is the second check.",
 "and nothing more; the Opus reader's independent search is the second check. **Reader's check (2026-09-29, `verify-O/arxiv_O.sh`, `arxiv_O2.sh` → `arxiv-O.xml`, `arxiv-O-2.xml`, parsed in `arxiv-O-parsed.txt`; 20 queries, https, one at a time, 3 s apart, positive controls \"lambda-rings\" + \"field with one element\" (3, incl. 0906.3146) and \"arithmetic site\" (15) PASS):** the non-control hits (1603.03191, 1502.05580, 1204.3129) are on disk and on the record and do not state Theorem R, Lemma F, Proposition 2.2.1, Corollaries 3.1–3.2 or T2 (b) over Z; the labels are flipped to `[novelty: dual-model check 2026-09-29]`; V.5 governs what the null search licenses.")
add('M12', 'AMEND', 1,
 "no candidate object, and the missing piece is now the rung, not the axioms.",
 "no candidate object: the missing piece is a proposed (D4) target over Z, and no rung below the arithmetic case can test one.")
