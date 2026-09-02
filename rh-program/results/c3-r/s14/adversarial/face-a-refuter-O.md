# ADVERSARIAL REFEREE REPORT — Q* FACE (a) — refuter O

**Direction:** C3-r, milestone M2c, Route 2, blocker S4. **Role:** adversarial refuter O of two (second model unknown to me; nothing assumed about it). **Date:** 2026-09-03 (Session 14 adversarial round).
**Target under attack:** the face-(a) theorem of `results/c3-r/s14/qstar-adjudication.md` §1/§3 — *every packet Γ^E_p of X₀ = X(Spec Z), and every single periodic orbit inside it, is an INDISCRETE subspace of X₀ in the quotient topology; hence no T₀ (a fortiori no Hausdorff) subspace of X₀ meets a packet in two points, and Q-a is NO.*
**Mandate:** assume the theorem is wrong; default to "refuted" if a step cannot be re-derived from the source.
**Sources read at printed page this session** (fresh `pdftotext -layout`; printed page = PDF page, checked against footers): `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` (119 pp.), `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`. Program notes (`qstar-adjudication.md`, `qa-kill.md` §9.4, `probe-9.3-adjudication.md` §2) were read as *inputs to attack*, never as authority. U.S. English.

---

## §0. VERDICT (stated first)

**STANDS-WITH-CAVEATS.**

Every step of the mechanism re-derives from [x-03] read at source; two of the five attack lines I was told to run in fact turned up evidence *for* the theorem that the program itself had not banked; the remaining three fail cleanly, one of them (attack line 6, Prop. 10.3) only after a genuinely delicate check that I record in full because it is the place where the theorem would have died. I could not construct a counterexample: not an open set, not a net, not an explicit point. I additionally verified the number-theoretic step numerically with explicit integers (§2.4).

**The single most important correction to the record, and it runs in the theorem's favor.** The adjudication (§2, "Topology of record") and probe `qa-kill.md` (§9.4(i)) both classify the identification of X₀'s topology with the quotient topology as **"judgment-grade, flagged, and load-bearing … the single reading both faces share"**, warranting it from [x-03] §10 p. 63 and [x-06] p. 11 — i.e. from side remarks. That classification is **wrong, and understates the program's own case.** [x-03] states it as a **definition, verbatim, on printed p. 59**:

> "Let E be an admissible class as in Definition 4.1. We give
> X = X̌(C)_E ×_{Q>0₀} R>0 and X₀ = X̌₀(C)_E ×_{Q>0₀} R>0
> the quotient topologies. The canonical G × R>0-action on X and the R>0-action on X₀ are continuous. The canonical R>0-equivariant projection X → X₀ is continuous and open and identifies X₀ with X/G as topological spaces."

This sentence sits in §9 under standing hypotheses that X₀ = Spec Z satisfies exactly (§9 opening, p. 55: "In this section C is the complex number field and our base scheme X₀ will be integral normal and of finite type over spec Z … char N₀ ⊃ char X₀"), and it precedes — so is not conditioned by — the later "In the following we will assume that char K₀ = 0". **No other topology on the suspension is defined anywhere in [x-03].** The load-bearing hypothesis of both faces is therefore *source-grade*, not judgment-grade. The register should be corrected; leaving "judgment-grade" on the record invites precisely the second-guessing that standing order 5 exists to prevent.

**Caveats named** (details §4): (C1) the theorem is a theorem about the **quotient** topology and is **false in the finer coproduct topology of Thm. 7.10 (p. 46)**, where each packet is *compact Hausdorff* ≅ (Ẑ^×_(p)/p^Ẑ) × (R>0/p^Z); face (a) therefore kills "**subspace of** X₀", not "Deninger's packet" as an object. (C2) The theorem is, read literally, incompatible with two printed adjectives in the survey [x-06] p. 12 ("The **compact** subsets Γ_{x₀} ⊂ X₀", "Γ_{x₀} **is a fibre space over the compact group** Aut(F̄_p)/Aut(F_p)"); the program must say out loud why that is not a contradiction with [x-03] (it is not: [x-03] p. 38 states these as *bijections*, and Thm. 7.10 Rem. 2, p. 47, disclaims homeomorphy), or an external referee will read the program as contradicting Deninger. (C3) Face (a) alone does not kill S4: Deninger's own S4 sentence (pp. 39–40) reads "Is there a sub-dynamical system Y₀ ⊂ X₀ … **or at least one which maps to X₀** …"; the "maps to" alternative is untouched by face (a) and is carried entirely by face (b), which I was not asked to referee.

---

## §1. The definitions and the topology, written out from the source

All page numbers are printed pages of [x-03] v4.

**1.1 Points (p. 22, verbatim).** X̊(C) = {(x, P^×) : x ∈ X, P^× : κ(x)^× → C^× a homomorphism}. Right G-action (x,P^×)^σ = (x^σ, P^×∘σ); commuting N-action **F_ν(x,P^×) = (x, P^×∘( )^ν)**. X̊₀(C) = X̊(C)/G. For X affine (Remark 3.4) a point is equivalently a multiplicative map P : R → C with P(0)=0, P(1)=1, whose zero set 𝔭_P = P^{-1}(0) is prime; here X₀ = Spec Z, X = Spec ℤ̄, R = ℤ̄ (countable — [x-03]'s standing "arithmetic scheme" hypothesis, p. 40).

**1.2 Admissibility (Def. 4.1, p. 27, verbatim).** A class E is (N₀-)admissible if for all σ ∈ Aut κ and ν ∈ N₀: χ ∈ E ⟺ χ∘σ ∈ E ⟺ χ∘( )^ν ∈ E; and every χ ∈ E satisfies **(Tors)**: ker(χ|_{μ(κ)}) finite of order in N₀. **(Image)** (p. 27, verbatim): *only if* char κ > 0 — if χ(κ^×) is torsion then κ^× is torsion. E_max = (Tors)+(Image); E_tors = (Tors).
*Consequence I checked, needed by Thm. 5.2:* over X = Spec ℤ̄ the residue fields are ℚ̄ (char 0, where (Image) imposes nothing) and F̄_p (where κ^× **is** torsion, so (Image)'s conclusion holds outright). Hence **on Spec Z, (Image) is vacuous and E_max = E_tors: every admissible E satisfies E ⊆ E_max**, so Thm. 5.2 applies to every admissible E. (This is the adjudication's claim; it is correct.)

**1.3 N₀ is forced (p. 24, l. "We always assume that char N₀ ⊃ char X₀, the set of positive residue characteristics of the points of X₀").** For X₀ = Spec Z that set is *all* primes, so char N₀ = all primes, **N₀ = N and Q>0₀ = Q>0**. There is no smaller-N₀ escape over Spec Z.

**1.4 Packet coordinates (pp. 32–33, verbatim).** (34) N x₀^Ẑ = Gal(κ(x)/κ(x₀)) ↪ Aut(κ(x)^×) = Ẑ^×_(p); (35) the surjection Ẑ^×_(p) × N₀ ↠ S, (a,ν) ↦ χ_x∘( )^a∘( )^ν, with (a,ν) ~ (a′,ν′) iff ν′ = νp^n, a = p^n a′; (38) (Ẑ^×_(p)/N x₀^Ẑ) ×_{p^Z} Q>0₀ ≅ C_{x₀}, "**It follows that all points P₀ ∈ C_{x₀} have isotropy subgroup (Q>0₀)_{P₀} = N x₀^Z**"; (39) C_{x₀} ≅ (Ẑ^×_(p)/N x₀^Ẑ) ×_{p^{Z/deg x₀}} (Q>0₀/N x₀^Z), and "The set C_{x₀} **fibres** over the compact group Ẑ^×_(p)/p^Ẑ = Aut(F̄_p)/Aut(F_p), and the fibres are the Q>0₀-orbits in C_{x₀}." **Note the grammar of the source: (38)/(39) are asserted as Q>0₀-equivariant *bijections of sets*; §6 (where they are used) precedes §7, where topology is first introduced. Deninger nowhere claims (38)/(39) is a homeomorphism, and (p. 33) says the fibration map "depend[s] on our choices of x and ι", whereas only the projection (40) to Q>0₀/p^Z is called canonical.**

**1.5 Isotropy (Thm. 5.2, p. 34, verbatim).** "Let E be an admissible class with E ⊂ E_max. … For any point P₀ ∈ C^E_{x₀} the isotropy group of P₀ is (Q>0₀)_{P₀} = N x₀^Z where N x₀ = |κ(x₀)|. If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}." For X₀ = Spec Z, x₀ = (p): N x₀ = p, isotropy = **p^Z ⊂ Q>0₀ = Q>0**, so F_{p^{-j}}(P₀) = P₀ for every j ∈ **Z** (the action of Q>0₀ is by bijections, p. 43 Prop. 7.4b).

**1.6 Suspension and flow (p. 38, verbatim).** X₀ = X̌₀(C)_E ×_{Q>0₀} R>0, "the quotient of X̌₀(C)_E × R>0 by the right Q>0₀-action given by **(P₀,u)q = (P₀ q, q^{-1}u) = (F_q(P₀), q^{-1}u)**"; orbit written [P₀,u]; [P₀,u]·v = [P₀,uv]; φ^t[P₀,u] = [P₀,ue^t]. Γ_{x₀} = C_{x₀} ×_{Q>0₀} R>0, Γ^E_{x₀} = C^E_{x₀} ×_{Q>0₀} R>0. Thm. 6.1 (p. 39): the points with non-trivial R>0-isotropy are exactly ⨿_{x₀} Γ^E_{x₀}, isotropy N x₀^Z.
*Identity I will use, derived from the display above:* taking q = r, **[P, rs] = [F_r P, s]** — i.e. [P₀,u] = [F_q P₀, q^{-1}u]. Direction and convention verified against the printed display, not from memory.

**1.7 Topologies (§7, pp. 40–47).** X̊(C) for affine X: **pointwise convergence** on R = ℤ̄ (subspace of the Tychonov C^R), metrizable (p. 40). pr_X continuous (Lemma 7.1). F_ν continuous, closed and open, with F_ν(X̊(C)) clopen (Lemma 7.3, p. 42). X̌(C) = colim_{N₀} X̊(C) with the **inductive-limit** topology (p. 43): Z ⊆ X̌(C) is open iff F_ν(Z) ∩ X̊(C) is open in X̊(C) for all ν. **Prop. 7.4(a): X̊(C) is a closed and open subspace of X̌(C)**; (b) F_q is a homeomorphism for q ∈ Q>0₀. X̌₀(C) = X̌(C)/G with the quotient topology; π and π̌ are continuous **and open** (p. 43). Cor. 7.8 (p. 45): metric δ on X̊₀(C) with δ(πP,πP′) ≤ d(P,P′), X̊₀(C) metrizable, separable, Hausdorff. Cor. 7.9 (p. 45): X̊(C), X̊₀(C), X̌(C), X̌₀(C) all Hausdorff when X₀ carries an ample invertible sheaf (Spec Z is affine ⇒ yes). E-loci (p. 47, verbatim): subspace topologies; X̌(C)_E = colim_{N₀} X̊(C)_E and X̌₀(C)_E = colim_{N₀} X̊₀(C)_E carry inductive-limit topologies that "**agree with the subspace topologies** … because the subspaces F_ν^{-1}X̊(C) and F_ν^{-1}X̊₀(C) are open"; "All preceding results in this section remain true if we replace X̊(C) etc. by X̊(C)_E etc."
**The suspension's topology: p. 59, quoted verbatim in §0 above — the quotient topology, by definition.** The quotient map q : X̌₀(C)_E × R>0 → X₀ is therefore continuous, and open (Q>0₀ acts by homeomorphisms).

**1.8 The two model theorems that any attack must respect.**
*Thm. 7.10 (p. 46).* The canonical R>0-equivariant maps
X̊₀(C)_{Q,in} × R>0 ∐ ⨿_{p} X̊₀(C)_{p,in} ×_{p^Z} R>0 → X₀ = X̌₀(C)_{Etors} ×_{Q>0₀} R>0
are **continuous bijections** (in = "P^×|_{μ(κ(x))} injective"). Rem. 2 (p. 47): "The continuous bijections in Theorem 7.10 are **not homeomorphisms in general**", the printed reason being connectedness of the fibre X_η on the right against uncountably many components on the left. *That a continuous bijection into X₀ is asserted at all presupposes a topology on X₀ independent of the left-hand side, and that it is not a homeomorphism says the right-hand topology is strictly coarser.*
*Prop. 10.3 and its Remark (p. 64).* With Q>0₀Ẑ^× × R>0 carrying the **adele** topology, Y = Q>0₀Ẑ^× ×_{Q>0₀} R>0 is **irreducible**; and the Remark: "By [LR00, Lemma 3.1], the orbits of the Q>0-action on Q>0Ẑ^× × R>0 are closed. … it follows that the **points of Y are closed, i.e. Y is a T₁-space**." Also p. 62: Y′ = Q>0₀Ẑ^×/Q>0₀ "carries the **coarse topology**", proved by strong approximation for Q.

---

## §2. Attack lines, each with its outcome

### 2.1 Attack line (1) — the topology: definition or reading? Does the argument survive the coproduct topology of Thm. 7.10?

**Outcome: the attack FAILS, and inverts.** It is a **definition**, printed at p. 59 (quoted §0), under §9 hypotheses that Spec Z satisfies. The adjudication's and probe A's warrants ([x-03] p. 63, [x-06] p. 11) are corroborating side remarks, not the load-bearing citation; the load-bearing citation exists and neither found it. Three further independent corroborations, all read this session:
- **Thm. 7.10 (p. 46) presupposes it.** A "continuous bijection … → X₀" is meaningless unless X₀ already has a topology, and Rem. 2 (p. 47) says it is not a homeomorphism — so X₀'s topology is *strictly coarser* than the coproduct's. Under the coproduct topology the theorem would be a triviality and the remark false.
- **[x-06] p. 11 verbatim:** "Set X₀ = (X̌₀(C) × R>0)/Q>0 where Q>0 acts diagonally", with the topology referred to [Den22a, §7] = [x-03].
- **§10 p. 63** builds R_X = (π_*R_X̃)^Q on X = M ×_Q R>0 and warns "the continuous bijection π|_{M×{u}} : M × {u} → π(M × {u}) **will not be a homeomorphism** if π(M × {u}) is equipped with the subspace topology of X" — again presupposing the quotient topology and its coarseness.

**Does the argument survive the coproduct topology?** *No — and it must not.* Under the Thm.-7.10 topology the packet summand is X̊₀(C)_{p,in} ×_{p^Z} R>0. I computed this summand explicitly: X̊₀(C)_{p,in} = {π(x, χ_x∘( )^a) : a ∈ Ẑ^×_(p)} ≅ Ẑ^×_(p)/p^Ẑ (compact, Hausdorff), and F_p acts on it **trivially**, because F_p(χ^a) = χ^{ap} and p ∈ p^Ẑ. So the summand is (Ẑ^×_(p)/p^Ẑ) × (R>0/p^Z) — **compact Hausdorff, one-dimensional**. So face (a) is *strictly* a statement about the quotient topology. Since the quotient topology is Deninger's definition, the attack fails; but this is a real scope boundary and I record it as caveat C1 (§4).

### 2.2 Attack line (2) — is convergence in the colimit topology pointwise convergence, or finer? Can an open set of the colimit topology separate the Frobenius translates of P^a from P^b?

**Outcome: attack FAILS. No such open set exists, and the reason is structural.** The whole net and its limit live in the ν = 1 stratum X̊₀(C)_E, which by Prop. 7.4(a) + p. 47 is an **open** subspace of X̌₀(C)_E carrying its own topology; convergence inside an open subspace implies convergence in the ambient. So only the pointwise topology of p. 40 is ever used, and no colimit subtlety arises. Concretely: with x fixed over p, P_k := π(x, χ^{a m_k}) and P^b := π(x, χ^{ac}), and for each r ∈ ℤ̄ either r ∈ 𝔭_x (both values 0) or r̄ ∈ F̄_p^× has finite order d **prime to p**; reduction Ẑ_(p) ↠ Z/d is a continuous ring map, so m_k → c gives a m_k ≡ ac (mod d) **eventually**, hence P_k(r) = P^b(r) **exactly, eventually**. Summable weights (Prop. 7.6, p. 44) then give d(P_k, P^b) → 0, and δ(πP_k, πP^b) ≤ d(P_k,P^b) (Cor. 7.8). Since X̊(C) is metrizable this is a *sequence*, not a net: no net/filter pathology is available to attack.
*I tried to build the separating open set anyway.* Any open U of X̊₀(C)_E containing P^b contains a basic δ-ball, i.e. is determined by finitely many test elements r ∈ ℤ̄ up to ε; the orders d(r) of their reductions are finitely many integers prime to p; choose m ≡ c modulo their l.c.m. — the resulting F_m(P^a) lies in U. **No finite-data open set can separate.** The only way to separate would be an open set depending on infinitely many test elements, which the pointwise topology does not have.

### 2.3 Attack line (3) — is F_r(P^a) = F_m(P^a) exactly, on the nose, for r = m p^{-j}? Which E, which points?

**Outcome: attack FAILS; the hypotheses are met exactly.** Thm. 5.2's hypothesis is "E admissible with E ⊂ E_max", and §1.2 above shows **every** admissible E over Spec Z satisfies E ⊆ E_max because (Image) is vacuous there. The conclusion is about points of C^E_{x₀}; P^a = π(x,χ^a) is such a point. The isotropy is N x₀^Z = p^Z **inside Q>0₀ = Q>0** (§1.3 forces N₀ = N), so p^{-j} is in it for every j ∈ Z, and F_{p^{-j}}(P^a) = P^a **on the nose**, not up to anything. Since Q>0₀ acts as a group, F_{m p^{-j}} = F_m ∘ F_{p^{-j}}, so F_{r}(P^a) = F_m(P^a) = π(x, χ^{am}) exactly.
*Independent check of the isotropy, done by hand rather than by citation:* F_p(π(x,χ)) = π(x, χ∘( )^p) and y ↦ y^p **is** the Frobenius of Gal(κ(x)/κ(x₀)) = Gal(F̄_p/F_p); by p. 32 ("It surjects onto Gal(κ(x)/κ(x₀))", [Bou64, V §2 no 3, Prop. 6]) there is σ ∈ G with σx = x inducing it, so π(x, χ∘( )^p) = π((x,χ)^σ) = π(x,χ). **The p^Z-isotropy is Frobenius invisibility after the G-quotient** — it is not an extra hypothesis, it is the defining feature of a packet point. This is also why it is unavailable upstairs in X̌(C)_E, and the argument correctly runs downstairs.

### 2.4 Attack line (4) — can m_k → c in Ẑ_(p) and m_k p^{-j_k} → t in R hold simultaneously? Prove or refute, with density; check p = 2, small c, t = 1/2 with actual numbers.

**Outcome: attack FAILS; the statement is true, elementary, and I verified it numerically.**
*Statement.* For every c ∈ Ẑ_(p) and t ∈ R>0 there are m_k ∈ **N** and j_k ∈ **Z** with m_k → c in Ẑ_(p) and m_k p^{-j_k} → t in R>0.
*Proof (my own).* Put M_k := ∏_{ℓ ≤ k, ℓ ≠ p} ℓ^k and let c_k ∈ [0, M_k) with c_k ≡ c (mod M_k) (possible: Ẑ_(p) = lim_{(M,p)=1} Z/M). Choose j_k ∈ Z with p^{j_k} > max(M_k/t, k·M_k). The half-open real window [t p^{j_k}, t p^{j_k} + M_k) has length exactly M_k, so it contains **exactly one** integer ≡ c_k (mod M_k); call it m_k. Then (i) m_k ≥ t p^{j_k} > M_k > 0, so m_k ∈ N; (ii) m_k ≡ c (mod M_k), and every M prime to p divides M_k for large k, so m_k → c in Ẑ_(p); (iii) 0 ≤ m_k p^{-j_k} − t < M_k p^{-j_k} < 1/k. ∎
*Why the freedom is exactly the isotropy.* The prime p is **absent** from the profinite constraint (Ẑ_(p) has no p-component) and **present** in the real constraint (p^{-j_k}); so the two conditions live at disjoint places and cannot obstruct each other. This is Chinese remainder + one free archimedean scale, i.e. strong approximation for Q with the place p removed — the same tool [x-03] uses on p. 62 and pp. 64–65.
*Numbers.* `scratchpad/approx2.py`, exact rational arithmetic. Sample (target real accuracy < 10^{-12} forced):

| p | c | t | k | M_k | j_k | m_k | m_k mod M_k vs c mod M_k | m_k p^{−j_k} − t |
|---|---|---|---|---|---|---|---|---|
| 2 | −1 | 1/2 | 5 | 759 375 | 60 | 576 460 752 304 162 499 | 759 374 = 759 374 ✓ | +6.4·10^{−13} |
| 2 | −1 | 1/2 | 6 | 11 390 625 | 64 | 9 223 372 036 863 562 499 | 11 390 624 = 11 390 624 ✓ | +4.8·10^{−13} |
| 2 | 7 | 3 | 6 | 11 390 625 | 64 | 55 340 232 221 135 812 507 | 7 = 7 ✓ | +3.9·10^{−13} |
| 3 | −1 | 1/5 | 5 | 100 000 | 36 | 30 018 927 059 399 999 | 99 999 = 99 999 ✓ | +1.2·10^{−15} |
| 5 | 2 | 7/11 | 6 | 46 656 | 24 | 37 930 228 493 459 906 | 2 = 2 ✓ | +5.0·10^{−13} |

A small hand-checkable instance of the *whole* mechanism (p = 2, a = 1, b = −1, w = u = 1, so c = −1, t = 1): M = 27, j = 10, m = 1025 (1025 mod 27 = 26 = −1 ✓), r = 1025/1024 = 1.0009765625. Then F_r(π(x,χ)) = F_{1025}F_{2^{-10}}(π(x,χ)) = F_{1025}π(x,χ) = π(x,χ^{1025}), which agrees with π(x,χ^{−1}) on every element of F̄_p^× of order dividing 27; and r^{−1}·1 = 1024/1025 → 1. The pair (π(x,χ^{1025}), 1024/1025) is in the **same Q>0-orbit** as (π(x,χ), 1), so both map to z, while the pair converges to (π(x,χ^{−1}), 1) ↦ z′.
*I also checked the non-degeneracy that makes this bite:* −1 ∉ 2^Ẑ, since the powers of 2 mod 7 are {1,2,4} and −1 ≡ 6. So z and z′ really are **distinct** points of the packet, on different fibres of the (39) fibration.

### 2.5 Attack line (5) — the quotient step: does q((P^a,w)·r_k) = z? Direction and conventions of the suspension identification.

**Outcome: attack FAILS; conventions verified at the printed display.** p. 38 prints (P₀,u)q = (F_q(P₀), q^{-1}u). Hence (P^a,w)·r_k = (F_{r_k}(P^a), r_k^{-1}w) is by construction in the *same* Q>0₀-orbit as (P^a,w), so q sends it to z for **every** k. The derived identity [P, rs] = [F_r P, s] (used for the normal form) is the same display with q = r, u = rs. I checked the direction twice, since a transposed convention (F_{q^{-1}}, or q·u) would break exactly this step: it does not — the inverse sits on the R>0 factor, which is what makes r_k^{-1}w → t^{-1}w = u.
*Normal form, re-derived (needed so that "z, z′ arbitrary in Γ^E_p" is not a restriction).* By (38)/(39) a point of C^E_p is [a, r] with a ∈ Ẑ^×_(p) and r ∈ Q>0₀/p^Z; acting by q = r^{-1} ∈ Q>0₀ (which preserves E by Prop. 4.2's *forward and backward* invariance, p. 27) gives [P₀,u] = [F_{r^{-1}}P₀, ru] = [π(x,χ^a), ru]. So **every** point of Γ^E_p is [π(x,χ^a), w] with a a unit and χ^a ∈ E. And any two points of Γ^E_p may be taken over the *same* x, since G acts transitively on the points of X over x₀ (p. 32, "Any point y in X over x₀ is conjugate to our chosen point x by an element of G").
*Assembled:* (F_{r_k}(P^a), r_k^{-1}w) = (π(x,χ^{a m_k}), r_k^{-1}w) → (π(x,χ^{ac}), u) = (P^b, u); q continuous (p. 59) ⇒ the **constant** sequence z = q(·) converges to z′; a constant sequence at z converges to z′ iff every neighborhood of z′ contains z, i.e. **z′ ∈ cl{z}**. Symmetric in (c ↦ ab^{-1}, t ↦ u/w). Hence any open set meeting Γ^E_p contains all of Γ^E_p: the subspace topology on Γ^E_p is {∅, Γ^E_p}. Taking b = a and w ≠ u (c = 1, t = w/u ≠ 1) gives it for a **single** orbit.

### 2.6 Attack line (6) — consequences check against [x-03]'s and [x-06]'s printed theorems

I checked every printed statement I could find that constrains the topology near a packet.

- **Thm. 8.2 (p. 50): X̌₀(C)_per = X̌₀(S¹).** This is a closure computed in **X̌₀(C)**, which is Hausdorff (Cor. 7.9). It says nothing about the suspension. The §8 identification Y₀ = X̌₀(S¹) ×_{Q>0} R>0 of "the closure of the union of all periodic orbits" is consistent: the preimage of the periodic locus is Q>0-saturated, and q is an **open** continuous surjection, so cl_{X₀}(q(S)) = q(cl(q^{-1}q(S))). **No contradiction.**
- **Cor. 9.7 (p. 62): X₀ is connected.** A non-T₀ space can be connected; and indiscrete packets *help* connectedness. **No contradiction.**
- **Thm. 10.2 (p. 64): H⁰_F(X₀) = R.** Proved via Prop. 10.3's irreducibility. Independent of packets. **No contradiction.**
- **Thm. 7.10 Rem. 2 (p. 47), the non-homeomorphism remark.** The theorem *predicts* a much stronger failure than the one Deninger prints (his reason is global connectedness): on each packet summand the continuous bijection goes from a **compact Hausdorff** space onto an **indiscrete** one. Deninger prints "not homeomorphisms **in general**", which accommodates this. **No contradiction**, but see C2.
- **X₀ is not itself indiscrete** (a sanity check I ran to make sure the theorem is not degenerate): pr_{X₀} : X̌₀(C)_E → X₀ = Spec Z is continuous (p. 43) and Q>0₀-invariant, hence descends to a continuous X₀ → Spec Z. The Zariski open D(p) pulls back to an open set of X₀ containing every packet Γ_q (q ≠ p) and missing Γ_p. So **distinct packets are separated** and the indiscreteness is strictly intra-packet. This also independently corroborates face (b)'s "each packet is clopen in the periodic locus".
- **[x-06] p. 12: "The compact subsets Γ_{x₀} ⊂ X₀ …" and "Γ_{x₀} is a fibre space over the compact group Aut(F̄_p)/Aut(F_p) with fibres the compact orbits".** *This is the one place where the theorem collides with print.* If Γ_p is indiscrete then (i) Γ_p **is** quasi-compact (indiscrete spaces always are), so "compact" survives on the weak reading but fails on the compact-Hausdorff reading; (ii) the projection Γ_p → Ẑ^×_(p)/p^Ẑ is **discontinuous** — a continuous map from an indiscrete space to a Hausdorff space is constant — so "fibre space over the compact group" is false as topology. I verified the discontinuity explicitly: the sequence π(x,χ^{1025}) → π(x,χ^{−1}) of §2.4 has constant first coordinate [1] (1025 = 5²·41 contributes only to the N-factor of (37); the unit part is 1) while its limit has first coordinate [−1] ≠ [1]. **Assessment:** this is a survey adjective with no proof attached; [x-03] states the same content on p. 38 as an *R>0-bijection* induced by the *Q>0-bijection* (39), and (p. 33) flags that the fibration map is choice-dependent while only (40) is canonical. So the theorem contradicts an unproved compression in a survey, not a theorem. **Not a refutation — but the program must state this openly (caveat C2).**
- **Prop. 10.3 + its Remark (p. 64): Y = Q>0₀Ẑ^× ×_{Q>0₀} R>0 is irreducible and T₁ (points closed).** *This is the strongest attack available and it gets its own section.*

---

## §3. The strongest attack I found, and exactly why it fails

**The attack.** [x-03] Prop. 10.3's Remark asserts, on the printed page, that a space built by precisely the construction under scrutiny — a Q>0₀-suspension of a subspace of the finite adeles by R>0 — has **closed points**: "the orbits of the Q>0-action on Q>0Ẑ^× × R>0 are closed. … the points of Y are closed, i.e. Y is a T₁-space." If the same argument applies to a packet, then packet points are closed, cl{z} = {z}, and **the theorem is refuted outright**. The packet is manifestly the same shape of object: by (63)/(64) (p. 48) the characteristic-p part of Ȟ_{Etors} is Q>0(Ẑ^×_(p) × 0) ⊂ A_f, and the packet is its R>0-suspension. So one must ask, in earnest, why Deninger's own T₁ theorem does not kill this.

**Why it fails — the one-line answer, then the check.** *Deninger's Y has every finite place present; a packet has the place p deleted. Q is discrete in A but dense in A with any one place removed.*

**The check, done from the definitions.**
1. *Deninger's Y.* Points are (a,u) ∈ Ẑ^× × R>0 ⊂ A_f × R; a Q>0₀-orbit is {(qa, q^{-1}u)}. Suppose (q_k a, q_k^{-1}u) converges. Then q_k^{-1}u → v > 0 in R forces q_k → u/v in R, and q_k a → β in A_f forces q_k → βa^{-1} in A_f (a is a unit at every finite place). So the rationals q_k converge in **A = A_f × R**, where Q is **discrete**; hence q_k is eventually constant and the orbit is closed. Points of Y are closed. ✓ Consistent with the printed Remark, and I can now see why [LR00, Lemma 3.1] is the right citation.
2. *A packet.* The p-component of every packet point is **identically 0** (p. 48: Q>0(Ẑ^×_(p) × 0)), and the Q>0-action preserves that (q·0 = 0). A basic open set of A_f imposes, at each place ℓ ∉ S, only "β_ℓ ∈ Z_ℓ", which at ℓ = p is satisfied automatically; and at p ∈ S it imposes |β_p − 0|_p < ε, also automatic. **So the place p imposes no condition whatsoever, and the packet's ambient is effectively A_f^{(p)} × R.** In A_f^{(p)} × R = A/Q_p the diagonal Q is **dense** (strong approximation for Q, deleting one place). The orbit-closedness argument therefore has nothing to bite on: the k-th orbit element can approximate a target profinitely at all ℓ ≠ p while the missing p-place supplies an unconstrained real rescaling p^{-j_k}. This is *exactly* the calculation Deninger runs on p. 62 to prove that Y′ = Q>0₀Ẑ^×/Q>0₀ "carries the coarse topology" ("The fact that Y carries the coarse topology follows from **strong approximation for Q** … strong approximation (excluding the infinite place, i.e. the Chinese remainder theorem)") and again on pp. 64–65. The theorem under review is that same argument run at a packet, where the deleted place is p instead of ∞.
3. *The bookkeeping that makes the deletion legitimate* is the p^Z-isotropy of Thm. 5.2, i.e. Frobenius invisibility after the G-quotient (§2.3). Without it, p^{-j_k} would move the point and the real coordinate could not be tuned freely.

**Net effect.** Deninger's own T₁ statement and the theorem under review are two sides of one dichotomy: *all finite places present ⟹ Q discrete ⟹ orbits closed ⟹ T₁ (but still irreducible); one place deleted ⟹ Q dense ⟹ orbits dense ⟹ not even T₀.* Far from refuting face (a), Prop. 10.3 read against p. 62 is the closest thing in the literature to an independent confirmation of its mechanism. **The strongest attack fails, and converts into corroboration.**

*Two weaker attacks I also ran and record for completeness.* (i) *Escape by shrinking E.* Blocked: Def. 4.1's ν-closure is a biconditional, so E always contains the whole Frobenius sweep χ^{a m} (m ∈ N) of any of its packet characters, which is all the argument needs; and a one-orbit cut class E(a₀) (units = a₀p^Ẑ) still has c = ba^{-1} ∈ p^Ẑ ⊂ Ẑ^×_(p), for which the approximation lemma applies verbatim, and the b = a case makes the single orbit indiscrete. (ii) *Escape by shrinking N₀.* Blocked over Spec Z by char N₀ ⊇ char X₀ = all primes (p. 24), forcing N₀ = N.

---

## §4. The theorem's honest scope

**Statement, as I would let it out of the building.**
> Let X₀ = Spec Z, C = ℂ, N₀ = N, and let E be any admissible class of characters in the sense of [x-03] Def. 4.1 (over Spec Z this automatically gives E ⊆ E_max, so [x-03] Thm. 5.2 applies). Give X₀ = X̌₀(C)_E ×_{Q>0} R>0 the quotient topology of [x-03] p. 59. Then for every prime p and any two points z, z′ of the packet Γ^E_p, z and z′ are topologically indistinguishable in X₀. Consequently every packet, and every single periodic orbit inside it, is an indiscrete subspace, and **no T₀ subspace of X₀ meets a packet in two points**. In particular no Hausdorff, metrizable, or laminated **subspace** of X₀ contains a periodic orbit.

**Which E:** every admissible E, with no exception, including E_f, E_max, E_tors and the one-orbit cut classes E(a₀). Dimension, one-orbit-per-packet, transverse measure, ε ≡ +1 and metrizability are **not used**.

**Which topology:** the quotient topology of [x-03] p. 59 — Deninger's printed definition, and the only topology on the suspension in the corpus. **The theorem is false in the finer coproduct topology of Thm. 7.10 (p. 46)** (C1), where the packet summand is X̊₀(C)_{p,in} ×_{p^Z} R>0 ≅ (Ẑ^×_(p)/p^Ẑ) × (R>0/p^Z), **compact Hausdorff of covering dimension 1** (F_p acts trivially on X̊₀(C)_{p,in} because p ∈ p^Ẑ). Any coarser topology strengthens the theorem; any strictly finer one contradicts p. 59.

**Compact vs quasi-compact vs non-compact.** The packet Γ^E_p **is quasi-compact** — indiscrete spaces are, and independently it is the continuous image of the compact space above under Thm. 7.10 — but it is **not compact Hausdorff** and not T₀. So "the packets are compact" is *true on the quasi-compact reading and false on the Hausdorff reading*; the program should never use the word "compact" unqualified here. This is consistent with face (b), which forbids quasi-compact invariant sets from meeting the characteristic-zero locus or infinitely many packets, not from being a single packet.

**What the theorem does NOT say (C3).** It constrains **subspaces** of X₀ only. It says nothing about **continuous equivariant maps into** X₀: a map into an indiscrete subspace is unconstrained, so face (a) is silent on Deninger's own second alternative at [x-03] pp. 39–40 ("…or at least one which **maps to** X₀…"). The S4-DEAD conclusion therefore rests on face (a) **and** face (b) jointly; face (a) alone kills only the "Y₀ ⊂ X₀" half of Deninger's question. The adjudication scopes this correctly; the point is worth restating loudly because it is the first thing an external reader will test.

**Residue that face (a) leaves open, and its disposition.** One may re-pose S4 against the Thm.-7.10 coproduct space X₀^♯ := X̊₀(C)_{Q,in} × R>0 ∐ ⨿_p X̊₀(C)_{p,in} ×_{p^Z} R>0, which is a genuine R>0-space with compact Hausdorff packets mapping continuously and bijectively onto X₀. Face (a) does not touch it. It is, however, a **coproduct over the primes**, so its summands are clopen and any quasi-compact invariant subset meets finitely many of them: the face-(b) mechanism kills X₀^♯ immediately and by a shorter argument. I record it so that the residue list in `qstar-adjudication.md` §8 (which names only the Arakelov compactification X̄₀) is complete.

**Record corrections owed** (all in the theorem's favor, none altering the verdict):
1. `qstar-adjudication.md` §2 last bullet and `qa-kill.md` §9.4(i): the quotient topology is **not** judgment-grade. Cite **[x-03] p. 59** verbatim.
2. Add to the consistency ledger: [x-06] p. 12's "compact subsets Γ_{x₀}" / "fibre space over the compact group" is incompatible with the theorem on the Hausdorff reading and must be pre-empted in any external write-up, with the p. 38 "bijection" wording and Thm. 7.10 Rem. 2 (p. 47) as the answer.
3. Add [x-03] **Prop. 10.3 + Remark (p. 64)** and **p. 62 ("Y carries the coarse topology … strong approximation for Q")** to the anchor list: the first is the sharpest printed near-miss an external referee will raise, the second is Deninger's own instance of the mechanism.

---

## §5. What would still refute this

For the record, so a third model knows where to aim. Face (a) dies if and only if one of these is established:
1. A printed or defensible topology on the suspension **strictly finer** than the p.-59 quotient topology, under which [x-03] §9–§10 (Cor. 9.7, Thm. 10.2, Prop. 10.3) remain true. I found none, and Thm. 7.10 Rem. 2 argues against the coproduct candidate.
2. A failure of Thm. 5.2's isotropy at Spec Z — i.e. an admissible E over Spec Z with E ⊄ E_max. Impossible: (Image) is vacuous over Spec ℤ̄ (§1.2).
3. An open set of X̊₀(C)_E, depending on infinitely many test elements of ℤ̄, separating {F_m(P^a) : m ∈ N} from P^b. The pointwise topology has no such open set (§2.2).
4. An error in the p. 38 action convention. Checked at the display (§2.5).

None is available. **STANDS-WITH-CAVEATS.**
