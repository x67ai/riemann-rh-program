# Second-model verification — witnesses (d) and (f), and companion §§5, 7

Machine clock at start: (see below). Independent re-derivation; the first referee's file
`refute-df.md` was read only for its list of rulings, and every ruling is re-checked here from
the note, the companion and the published text. Page numbers refer to the published JPDOA
article (`novelty/ALKL-2024-published.txt`, markers "Page k of 68").

Sun Sep  6 12:39:14 IST 2026


## Verdict

**HOLDS-WITH-REPAIR.** Witnesses (d) (Cor. 4.5, and Cor. 6.21 via (6.47)) and (f) (Cor. 3.6 for
non-compact U, the p. 18 bundle extension, and the memoir's §2.1.8) **hold in full as mathematics**;
every step was re-derived here from the note, the companion and the published text, and nothing was
found that breaks either. Repairs due: one wording clause in the note (`0 ≤ ρ ≤ 1`), one imprecise
parenthetical in the note (the §4.3.3 exception is for `I(M,L)`, not for non-compact M wholesale),
one false side-item in the companion (§7.5, not used by the note), and two local defects in the
companion's §5 (the neighborhood N; "η_0 ≠ 0 automatically") that the note itself does not have.
Section 6 below states this in full.


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

---

## 1. Witness (d) — the symbol of u_j from (4.7)–(4.8), re-derived from scratch

**Normalization and sign.** (4.8) as printed carries **no** constant and the exponent is
`e^{−i⟨x′,ξ⟩}`; the `(2π)^{−n′}` sits on the inverse transform (4.7). So

    a_j(x″,ξ) = ∫_{R^{n′}} e^{−i⟨x′,ξ⟩} j^{n′+m̄′} g(x″) ψ_*(j x′) dx′ .

Substitute `y = j x′`, `dx′ = j^{−n′} dy`:

    a_j(x″,ξ) = j^{n′+m̄′} · j^{−n′} · g(x″) ∫ e^{−i⟨y,ξ/j⟩} ψ_*(y) dy = **j^{m̄′} g(x″) ψ̂_*(ξ/j)**,

with `ψ̂_*(η) := ∫ e^{−i⟨y,η⟩}ψ_*(y) dy` — the same convention as (4.8). The `j^{n′}` in the
prefactor is exactly the Jacobian; the note's normalization is correct and **not** off by `(2π)^{n′}`
(a `(2π)^{n′}` would only rescale a_j by a constant and change nothing). AGREE with the first
referee.

**Fourier symbol of Δ^{N_0}.** With this sign convention `∫e^{−i⟨y,η⟩}∂_kψ dy = iη_k ψ̂(η)`
(integrate by parts), so `Δ ↦ Σ(iη_k)² = −|η|²` and `ψ̂_*(η) = (−|η|²)^{N_0} ψ̂(η)`. As printed.
Since `|η|^{2N_0} = (Ση_k²)^{N_0}` is a polynomial and `ψ̂` is Schwartz, `ψ̂_*` is Schwartz. For
`|β| ≤ 2N_0` Leibniz gives `∂^βψ̂_* = Σ_{β′≤β} C ∂^{β′}(±|η|^{2N_0}) ∂^{β−β′}ψ̂`; each
`∂^{β′}(|η|^{2N_0})` is a homogeneous polynomial of degree `2N_0−|β′| ≥ 2N_0−|β|`, so on `|η| ≤ 1`
`|∂^βψ̂_*(η)| ≤ C_β |η|^{2N_0−|β|}`: **vanishing to order 2N_0−|β| at 0**, as claimed.
*Numerically verified* (1-D, ψ = exp(−1/(1−y²)) on (−1,1), N_0 = 2, exact-Leibniz evaluation to
avoid cancellation): fitted vanishing orders at 0 are 4.0000, 3.0000, 2.0000, 1.0000, −0.0000 for
β = 0,…,4 — predicted 4,3,2,1,0.

**The seminorm identity.** `∂_{x″}^α ∂_ξ^β a_j = j^{m̄′−|β|} ∂^α g(x″) (∂^βψ̂_*)(ξ/j)`; with
`ξ = jη` the (3.1) weight is `(1+j|η|)^{|β|−m̄_1} = j^{|β|−m̄_1}(1/j+|η|)^{|β|−m̄_1}`. The two powers
of j combine to `j^{m̄′−m̄_1}`, giving **exactly** the note's

    ‖a_j‖_{K,α,β,m̄_1} = j^{m̄′−m̄_1} · sup_K|∂^α g| · Φ_{β,m̄_1}(j),
    Φ_{β,m̄_1}(j) = sup_η |∂^βψ̂_*(η)| (1/j+|η|)^{|β|−m̄_1}.

This is an identity, not an inequality (each factor is a genuine supremum over an independent
variable). Verified.

**Φ bounded for m̄_1 ≤ 2N_0.** Two regimes, both re-checked:
* `|β| ≥ m̄_1` (exponent ≥ 0): `(1/j+|η|)^{|β|−m̄_1} ≤ (1+|η|)^{|β|−m̄_1}` for `j ≥ 1`, and
  `ψ̂_*` Schwartz kills it. Bound independent of j.
* `|β| < m̄_1 ≤ 2N_0` (exponent < 0): `(1/j+|η|)^{|β|−m̄_1} ≤ |η|^{|β|−m̄_1}`. **The task asks
  precisely whether the vanishing order 2N_0−|β| is enough here.** It is, and exactly: on `|η| ≤ 1`,
  `|∂^βψ̂_*(η)||η|^{|β|−m̄_1} ≤ C_β |η|^{2N_0−|β|+|β|−m̄_1} = C_β|η|^{2N_0−m̄_1} ≤ C_β`, the last
  step because `2N_0 − m̄_1 ≥ 0`. On `|η| ≥ 1` the weight is ≤ 1 and `∂^βψ̂_*` is bounded. Note the
  hypothesis `|β| ≤ 2N_0` needed for the vanishing bound is automatic here (`|β| < m̄_1 ≤ 2N_0`),
  and the boundary case `m̄_1 = 2N_0` is admissible (exponent exactly 0). So `sup_η |∂^βψ̂_*(η)|
  |η|^{|β|−m̄_1} < ∞` near `η = 0`: **yes**.
* **Sharpness (my own addition; neither the note nor the first referee checks it).** The condition
  `m̄_1 ≤ 2N_0` is not an artifact: for `m̄_1 > 2N_0`, `Φ_{β,m̄_1}(j) ≍ j^{m̄_1−2N_0} → ∞`. Numerics
  (2N_0 = 4): `Φ_{β,m̄_1}(j)` is flat in j for m̄_1 = 4.0, 3.5, 2.5, −1.0 (e.g. m̄_1 = 4.0, β = 0:
  0.0676, 0.323, 0.422, 0.440, 0.443, 0.444 at j = 1,16,256,4096,65536,10⁶) and grows like
  `j^{1/2}` for m̄_1 = 4.5 (0.0369 → 0.363 → 1.478 → 5.913 → 23.65 → 92.39, ratios ≈ 4 = 16^{1/2})
  and like `j` for m̄_1 = 5.0. So the note's requirement `2N_0 ≥ m̄″` is exactly what is needed —
  and it is stated. HOLDS.

**Lower bound Φ_{0,m̄′}(j) ≥ c > 0.** `Φ_{0,m̄′}(j) ≥ |ψ̂_*(η_0)| (1/j+|η_0|)^{−m̄′}` for any
`η_0 ≠ 0`. If `m̄′ ≥ 0` then `(1/j+|η_0|)^{−m̄′} ≥ (1+|η_0|)^{−m̄′}` (j ≥ 1); if `m̄′ < 0` then
`(1/j+|η_0|)^{−m̄′} ≥ |η_0|^{−m̄′}`. Hence the note's `min{(1+|η_0|)^{−m̄′}, |η_0|^{−m̄′}}` covers
both signs. Such an `η_0` exists: `ψ ∈ C_c^∞`, `ψ ≢ 0` ⟹ `ψ̂` entire and `≢ 0` ⟹ its zero set has
empty interior, so some `η_0 ≠ 0` has `ψ̂(η_0) ≠ 0`, whence `ψ̂_*(η_0) ≠ 0`. (The note writes "for
any η_0 ≠ 0 with ψ̂_*(η_0) ≠ 0" and leaves existence implicit; it is immediate.) Numerics:
`Φ_{0,2.5}(j) = 0.537, 0.987, 1.040, 1.043, 1.044, 1.044` and the explicit constant from η_0
(c = 0.0459) is indeed ≤ every value. HOLDS.

**(4.9) monotone.** `m̄ = m + n/4 − n′/2` is m plus a constant depending only on (n, n′), so
`m < m′ < m″ ⟹ m̄ < m̄′ < m̄″` with the *same* gaps `m̄′−m̄ = m′−m`. HOLDS.

**Ruling.** The symbol computation, the Φ bounds in both regimes (including the exact question
posed in the task), the lower bound, and the monotonicity of (4.9): **HOLDS**. AGREE with the first
referee on all of these, and I add the sharpness check that pins `2N_0 ≥ m̄″` as necessary.

---

## 2. Witness (d) — membership, the partition of unity, and the refutation of Cor. 4.5

**Which printed statement gives `C^∞(M) ⊂ I^m` for every m?** Three lines, all quoted in §0:
(4.5) p. 20 gives `C^∞(M) ⊂ I^{(∞)}(M,L)`; p. 22 identifies `I^{(∞)}(M,L) = I^{−∞}(M,L) :=
⋂_m I^m(M,L)`; and Cor. 4.6's proof (p. 23) says in words "C^∞(M) is contained in the stated
spaces by (4.5)". The identification `I^{(∞)} = I^{−∞}` is itself a consequence of (4.12) (take
`⋂_m` of `I^{(−m−n/4+ε)} ⊂ I^m ⊂ I^{(−m−n/4−ε)}`), so it is not an extra unverified claim.
`u_j ∈ C_c^∞(U_1)`, extended by zero, is in `C^∞(M)` since M is compact and U_1 open. HOLDS.

**Support.** `supp ψ_* = supp Δ^{N_0}ψ ⊂ supp ψ ⊂ {|x′|<1}`, so `supp u_j ⊂ x^{-1}({|x′| ≤ 1/j} ×
supp g)`. These are compact, nested decreasing, with intersection `x^{-1}({0}×supp g) ⊂ L`, and
`N` is an open neighborhood of that intersection; compactness gives `supp u_j ⊂ N` for j large.
(One triviality the note glosses: `{|x′| < 1}` need not sit inside U′ — irrelevant, since
`ψ_*(j·)` is supported in `{|x′| < 1/j}`, which does sit inside U′ for j large.) HOLDS.

**The modified partition of unity is legitimate.** With `ρ ∈ C_c^∞(U_1)`, `ρ = 1` on N:
`(1−ρ)h + [ρ + (1−ρ)f_1] + Σ_{i≥2}(1−ρ)f_i = (1−ρ)(h + Σ_i f_i) + ρ = (1−ρ) + ρ = 1`. Supports:
`supp((1−ρ)h) ⊂ supp h ⊂ M∖L`; `supp(ρ+(1−ρ)f_1) ⊂ supp ρ ∪ supp f_1 ⊂ U_1`;
`supp((1−ρ)f_i) ⊂ supp f_i ⊂ U_i`. So it is subordinate to the same covering `{M∖L, U_j}` of
(4.10). On N: `(1−ρ)h = 0`, `(1−ρ)f_i = 0` (i ≥ 2), `ρ+(1−ρ)f_1 = 1`. Hence for j large
`h u_j = 0`, `f_i u_j = 0` (i ≥ 2), `f_1 u_j = u_j`. HOLDS.
*One cosmetic gap, confirming the first referee.* The note does not say `0 ≤ ρ ≤ 1`, and a
"C^∞ partition of unity" is normally required nonnegative; without the bound `(1−ρ)h` can be
negative. Such a ρ always exists (a standard bump), so this costs nothing. **Repair (note, one
clause):** write "ρ ∈ C_c^∞(U_1), 0 ≤ ρ ≤ 1, ρ = 1 on N". AGREE.

**The closed-graph remark.** `I^m(M,L) → C^{−∞}(M)` is continuous: (4.12) gives
`I^m ⊂ I^{(s)}` continuously for `s = −m−n/4−ε`, (4.3) with `P = 1 ∈ Diff(M,L)` gives
`I^{(s)} → H^s(M)` continuous, and `H^s(M) ⊂ C^{−∞}(M)` continuously. Two Fréchet topologies on
the same vector space, both continuously injected into a Hausdorff TVS, have closed identity graph,
hence coincide (closed graph theorem). So the topology of `I^m(M,L)` does not depend on the choice
of `{U_j}, {h,f_j}` and the refutation is choice-independent. Sound; and in any case the note's
family is itself an admissible choice, so the refutation does not need the remark. HOLDS.

**The refutation itself.** For j ≥ j_0 the (4.10)-image of u_j is `(0, (a_j, 0, 0, …))`.
`‖a_j‖_{K,α,β,m̄″} ≤ C_{α,β,K} j^{m̄′−m̄″} → 0` for every K, α, β (m̄′ < m̄″ ≤ 2N_0), and the
`C^∞(M∖L)` component vanishes identically, so **u_j → 0 in I^{m″}(M,L)**. Conversely
`‖a_j‖_{K,0,0,m̄′} = sup_K|g| · Φ_{0,m̄′}(j) ≥ c sup_K|g| > 0` for a compact `K ⊂ U″` meeting
`{g ≠ 0}`, and (4.10) is a TVS-embedding, so **u_j ↛ 0 in I^{m′}(M,L)**. All u_j lie in
`I^m(M,L)`. Therefore the `I^{m′}`- and `I^{m″}`-subspace topologies on `I^m(M,L)` differ:
**Cor. 4.5 is false**, for every compact (M,L) with `L ≠ ∅`, `codim L = n′ ≥ 1`, and every
`m < m′ < m″`. The degenerate case `n″ = 0` (L a finite set of points) is fine: `U″ = R^0`,
`g` a nonzero constant, only `α = 0` occurs. **HOLDS. AGREE.**

**Cor. 6.21 via (6.47).** `M̆` is "any closed manifold of dimension n which contains M as
submanifold" (p. 31), so `(M̆, ∂M)` is a compact pair with `codim ∂M = 1` and Cor. 4.5's setting
applies verbatim. `Ȧ^m(M) = I^m_M(M̆,∂M) ⊂ I^m(M̆,∂M)`, "closed subspaces" (6.47) — subspace
topology; the subscript means "supported in M" by (6.4)/(6.7). With `supp ψ ⊂ (½,1)` in the collar
coordinate `x` (so `n′ = 1`, `ψ_* = ψ^{(2N_0)}`, `supp ψ_* ⊂ [½,1]`), `supp u_j ⊂ {1/(2j) ≤ x ≤
1/j} × supp g`, which for j large is a compact subset of `M̊`; hence `u_j ∈ C_c^∞(M̊) ⊂ C^∞(M̆)
∩ {supported in M} ⊂ I^m_M(M̆,∂M) = Ȧ^m(M)` for every m. **A point the first referee passes over:**
`supp u_j` here is disjoint from `L = ∂M`, so one must still check `h u_j = 0`. It is fine — the
supports still shrink to `x^{-1}({0}×supp g) ⊂ ∂M`, so the same ρ-modified partition of unity has
`ρ = 1` on `supp u_j` for j large, exactly as in (d). The symbol computation is unchanged, so
`u_j → 0` in `I^{m″}(M̆,∂M)` hence in `Ȧ^{m″}(M)`, and `u_j ↛ 0` in `Ȧ^{m′}(M)`. **Cor. 6.21 is
false. HOLDS. AGREE**, with the added support check.

**Ruling for witness (d) as a whole: HOLDS**, with the one cosmetic wording repair (0 ≤ ρ ≤ 1).

---

## 3. Witness (f) — Cor. 3.6 for non-compact U

**`b_j = χ_j(x)(1+|ξ|²)^{j/2} ∈ S^j ∖ S^m` for `m < j`.** Upper: `∂_ξ^β(1+|ξ|²)^{j/2}` is a finite
sum of terms `c·ξ^{γ}(1+|ξ|²)^{j/2−k}` with `|γ| ≤ k`, `2k−|γ| = |β|`, hence
`≤ C_β(1+|ξ|)^{j−|β|}`; multiplied by `∂^αχ_j`, all (3.1) seminorms of order j are finite.
Lower: `(1+t)² ≤ 2(1+t²)` for `t ≥ 0`, so at `x = x_j` (where `χ_j = 1`)
`‖b_j‖_{K,0,0,m} ≥ sup_ξ 2^{−j/2}(1+|ξ|)^{j−m} = ∞` when `m < j`. Numerically confirmed
(`sup_{|ξ|≤10⁸} (1+ξ²)^{j/2}(1+|ξ|)^{−m}` = 1e8, 1e24, 1e40 for (j,m) = (1,0), (3,0), (5,0), and
exactly 1 at m = j). HOLDS.

**The choice of basic 0-neighborhoods is legitimate — the exact point the task flags.**
A 0-neighborhood W of `S^∞ = ind_k S^k` meets each step in a 0-neighborhood of that Fréchet step;
`W ∩ S^k` therefore contains a **finite** intersection
`⋂_{i≤p, (α,β)∈F_i} {‖a‖_{K_i,α,β,k} < ε_i}`. Since `‖·‖_{K,α,β,k}` is monotone increasing in K,
putting `K_k := ⋃_i K_i` (compact), `F_k := ⋃_i F_i` (finite), `ε_k := min_i ε_i`, the single-compact
set `W_k = {a ∈ S^k : ‖a‖_{K_k,α,β,k} < ε_k, (α,β) ∈ F_k}` is contained in that intersection, hence
in `W ∩ S^k`. So the note's form is not a restriction. *Neither the note nor the companion states
this monotonicity step; it is one line and correct.* AGREE with the first referee that the form is
legitimate.

**`2b_jρ_R ∈ W_1`.** `b_jρ_R ∈ C_c^∞(U×R^l) ⊂ S^{−∞} ⊂ S^1`. Local finiteness of
`{B̄(x_j,r_j)}` plus compactness of `K_1` give `j_0` with `supp χ_j ∩ K_1 = ∅` for `j ≥ j_0`;
`supp χ_j` is closed, so `χ_j ≡ 0` on the *open* set `U ∖ supp χ_j ⊃ K_1` and **all** x-derivatives
vanish on `K_1` too. Every W_1-seminorm of `2b_jρ_R` is therefore 0 < ε_1. HOLDS. (The note's phrase
"vanishes on `K_1 × R^l`" is enough only because the vanishing is on a neighborhood; it is.)

**The `O(1/R)` bound — computed, not asserted.** For `(α,β)` and any compact K,
`∂_x^α∂_ξ^β[b_j(1−ρ_R)] = ∂^αχ_j(x) Σ_{β′+β″=β} C ∂^{β′}(1+|ξ|²)^{j/2} ∂^{β″}(1−ρ_R)`.
* `β″ = 0`: supported in `|ξ| ≥ R`, bounded by `C(1+|ξ|)^{j−|β|} = C(1+|ξ|)^{j+1−|β|}(1+|ξ|)^{−1}
  ≤ C(1+|ξ|)^{j+1−|β|}/(1+R)`.
* `β″ ≠ 0`: `∂^{β″}(1−ρ_R)(ξ) = −R^{−|β″|}(∂^{β″}ρ)(ξ/R)`, supported in `R ≤ |ξ| ≤ 2R` (ρ = 1 on
  B(0,1), supp ρ ⊂ B(0,2)). There `(1+|ξ|)^{j−|β′|}R^{−|β″|} = (1+|ξ|)^{j−|β|}((1+|ξ|)/R)^{|β″|}
  ≤ 3^{|β″|}(1+|ξ|)^{j−|β|} ≤ 3^{|β″|}(1+|ξ|)^{j+1−|β|}/(1+R)` for `R ≥ 1`.
So `‖b_j(1−ρ_R)‖_{K,α,β,j+1} ≤ C(j,α,β)/(1+R)`. Since `F_{j+1}` is **finite**, one R = R_j serves
all of them, and `2b_j(1−ρ_{R_j}) ∈ W_{j+1}`.
*Numerically verified* (l = 1, explicit smooth ρ): `‖·‖_{0,0,β,j+1} × R` is essentially constant in
R over R = 4 … 1024 — e.g. j = 1: 0.423, 0.508, 0.534, 0.541, 0.542 (β = 0); 2.06, 2.28, 2.34,
2.36, 2.37 (β = 1); 16.3, 16.2, 16.2, 16.2, 16.2 (β = 2); 414, 374, 364, 362, 362 (β = 3). Same
picture at j = 3, 5. So the decay is exactly `Θ(1/R)`, not merely `O(1/R)`. HOLDS.

**Absolute convexity and the finitely many exceptions.** `b_j = ½(2b_jρ_{R_j}) + ½(2b_j(1−ρ_{R_j}))`
with `W_1, W_{j+1} ⊂ W` and W absolutely convex, so `b_j ∈ W` for `j ≥ j_0`. For `j < j_0` (finitely
many) `W` is absorbing, so `b_j ∈ λ_j W`; W is balanced, so `{b_j} ⊂ λW` with
`λ = max{1, λ_1,…,λ_{j_0−1}}`. Absolutely convex 0-neighborhoods form a base, so **{b_j} is bounded
in `S^∞(U×R^l)`**. HOLDS.

**Conclusion.** `{b_j}` lies in no step `S^m` (b_j ∉ S^m for j > m), so the spectrum is **not
regular**; by the paper's own definition on p. 4 regularity is part of bounded retractivity, so
**not boundedly retractive**; and by p. 5 ("acyclic LF-spaces are complete and regular [39,
Corollary 6.5]", with Fréchet steps, and "X is acyclic if and only if it is
boundedly/compactly/sequentially retractive") **not acyclic**, and not compactly or sequentially
retractive either. This holds for **every nonempty open `U ⊂ R^n` with `n ≥ 1`** (such a U is never
compact: R^n is connected and unbounded) and **every `l ≥ 1`**. Both hypotheses are needed and both
are stated: for `U = R^0 = {0}` there is no escaping sequence, and for `l = 0` the (3.1) seminorms
lose the ξ-weight so all `S^m(U×R^0) = C^∞(U)` coincide and `b_j = χ_j ∈ S^m` for all m.
**Cor. 3.6's acyclicity and bounded-retractivity clauses are false. HOLDS. AGREE.**

**The printed proof of Cor. 3.6 does route through them** — verbatim: "Corollary 3.4 gives the
property of being acyclic, and therefore complete and boundedly retractive"; and the semi-Montel
step opens "Since S^∞(U×R^l) is boundedly retractive, B is contained and bounded in some
S^m(U×R^l)". So the completeness and Montel clauses are unproved as printed. The note claims only
that the acyclicity and bounded-retractivity clauses are *false* and that the others' printed
derivations pass through them — correctly scoped. HOLDS.

**p. 18 bundle extension.** "Propositions 3.2 and 3.3 and Corollaries 3.4 to 3.6 can be directly
extended to this setting" — no compactness hypothesis, and p. 30 confirms compactness is imposed
only from §6 on ("For the sake of simplicity, in this section and in Sects. 7 and 8, we only
consider the case of compact manifolds unless otherwise stated"). The same construction runs in
chart domains of a non-compact base (take `x_j` leaving every compact set of M and a locally finite
family of trivializing balls); the basic-neighborhood step is unchanged, since a basic
0-neighborhood of `S^k(E)` again involves finitely many chart-compacts whose union avoids `supp χ_j`
for j large. HOLDS.

**Memoir §2.1.8.** Checked in **both** arXiv versions of 2402.06671 (r3s-17 = v1, r3s-39 = v2).
The running header immediately preceding §2.1.8 reads "2.1. SECTION SPACES AND OPERATORS ON
MANIFOLDS — 15" in each, so §2.1.8 begins on printed page 15 in both; the note's
"[ALKL24m, §2.1.8, p. 15]" and its bibliography note "the pages cited are the same in v1" are
correct here. Verbatim (v2, identical in v1): "**2.1.8. Symbols.** For any open U ⊂ R^n and
l ∈ N_0, a symbol of order at most m ∈ R on U × R^l … The following properties hold [ÁLKL23,
Corollaries 3.4–3.6 and Remark 3.8]: The topologies of S^∞(U×R^l) and C^∞(U×R^l) coincide on
S^m(U×R^l), however the second inclusion of (2.1.27) is not a TVS-embedding; C_c^∞(U×R^l) is dense
in S^∞(U×R^l); and S^∞(U×R^l) is an acyclic Montel space, and therefore complete,
boundedly/compactly/sequentially retractive and reflexive." So the memoir does restate Cors. 3.4–3.6
"for any open U ⊂ R^n", and even strengthens the retractivity clause to all three forms — all three
fail by the above. HOLDS. AGREE.

**The parenthetical "(Sect. 4.3.3, p. 23, excepts acyclicity for non-compact M; the symbol
statements do not.)"** p. 23 reads, verbatim: "Corollary 4.7 has extensions for ⋃_m I^m(M, L) and
I_{·/c}(M, L), **except acyclicity in the case of I(M, L)**." The exception is attached to one
space, `I(M,L)` (the arbitrary-support space of (4.6)), not to the non-compact case as a whole:
acyclicity *is* still claimed there for `⋃_m I^m(M,L)` and for `I_c(M,L)`. The note's sentence is
therefore imprecise — a reader (or the authors) can fairly object that they did not "except
acyclicity for non-compact M". The contrast the note is drawing is real and useful (§3 flags
nothing at all), so this is wording, not mathematics. **HOLDS-WITH-REPAIR.** Suggested wording:
"(Sect. 4.3.3, p. 23, excepts acyclicity in the case of I(M,L) for non-compact M; the symbol
statements of §3 make no exception of any kind.)" AGREE with the first referee that a repair is
due; my phrasing keeps the "non-compact" contrast the note wants.

**Ruling for witness (f): HOLDS**, with the one parenthetical repair above.

---

## 4. The companion, §5 (witness (d)) and §7 (witness (f))

**§5 — the mathematics is the same as the note's and is correct**, with the seminorm identity in
the general form `‖a_j‖_{K,α,β,m̄_1} = c_j j^{−n′−m̄_1}‖∂^αg‖_{L^∞(K)}Φ_{β,m̄_1}(j)`; with
`c_j = j^{n′+m̄′}` this is the note's `j^{m̄′−m̄_1}`. Verified line by line. **Two defects, both in
the companion only, neither reaching the note:**

* **§5, the neighborhood N — a real gap (missed by the first referee).** The companion writes
  "ρ ∈ C_c^∞(U_1) with ρ = 1 on a neighborhood **N of p_0**" and then "supp u_j ⊂ {|x′| ≤ 1/j} ×
  supp g ⊂ N for j ≥ j_0". That does not follow: the supports shrink to `{0} × supp g`, which is a
  *set*, not the point p_0, and is not contained in a small neighborhood of p_0 unless `supp g` is
  small. Concretely, take L = S¹ ⊂ M = T², `g` a bump whose support is an arc of length 1, and
  `ρ` supported in a ball of radius 1/100 around p_0: then `ρ = 0` on most of `supp u_j` for every
  j, `h̃u_j ≠ 0`, and the argument's first step collapses. **Repair (companion, §5):** take
  `ρ = 1` on a neighborhood N of the compact set `x^{−1}({0} × supp g) ⊂ L` — which is exactly what
  the **note** says ("a neighborhood N of the compact set x^{-1}({0}×supp g) ⊂ L"). So the note is
  right and the companion's paraphrase of it is wrong. **FALLS as written (companion §5 only);
  the note is unaffected.**
* **§5, "(η_0 ≠ 0 automatically)" — false in one admissible case.** `N_0 ∈ N_0` with `2N_0 ≥ m̄″`
  permits `N_0 = 0` whenever `m̄″ ≤ 0`, and then `ψ_* = ψ`, `ψ̂_*(0) = ∫ψ` need not vanish, so an
  `η_0` with `ψ̂_*(η_0) ≠ 0` need not be nonzero. The lower bound `min{(1+|η_0|)^{−m̄′},
  |η_0|^{−m̄′}}` is meaningless at `η_0 = 0`. **Repair:** either require `N_0 ≥ 1` (always allowed,
  since larger N_0 only strengthens `m̄_1 ≤ 2N_0`) or, as the **note** does, say "for any η_0 ≠ 0
  with ψ̂_*(η_0) ≠ 0" and note that such η_0 exists because `ψ̂` is entire and `≢ 0`. Again the note
  is right. **HOLDS-WITH-REPAIR (companion §5 only).**

**§7 items 1–4, 6 — verified**, exactly as in §3 above (the Leibniz split, the `3^{|β″|}` constant
on the annulus `R ≤ |ξ| ≤ 2R`, the `(1+t)² ≤ 2(1+t²)` lower bound, the compact-exhaustion
construction of the balls, the memoir sentence). One presentational gap: item 3's step "W ∩ S^k …
contains a basic set `W_k = {a : ‖a‖_{K_k,α,β,k} < ε_k, (α,β) ∈ F_k}`" needs the one-line remark
that `‖·‖_{K,α,β,k}` is monotone in K, so the finitely many compacts of a genuine basic
neighborhood can be replaced by their union. Not stated in either file; correct. **HOLDS.**

**§7 item 5 ("Direct failure of the criterion") — FALLS as written.** The side-witness
`a_j := (1+j)^{m′}ψ(x)θ(ξ − je_1)` is claimed to satisfy "a_j → 0 in S^{m″} (each seminorm is
O(j^{m′−m″}))". False. On `supp θ(·−je_1)` one has `1+|ξ| ≍ j`, and translating a bump gains
nothing in ξ-derivatives, so

    ‖a_j‖_{K′,0,β,m″} = (1+j)^{m′} sup|∂^βθ| · sup_{|ξ−je_1|≤r}(1+|ξ|)^{|β|−m″} ≍ j^{m′+|β|−m″},

which is `O(j^{m′−m″})` only for `β = 0`; it is bounded away from 0 at `|β| = m″−m′` and diverges
beyond. So **a_j does not converge to 0 in S^{m″} at all**, and the item's conclusion is not
established by its own witness. Numerically (m′ = 1, m″ = 2, θ a bump on (−1,1), l = 1):
`‖a_j‖_{0,β,2}` at j = 10, 40, 160, 640 is
β=0: 1.67e−3, 4.47e−4, 1.14e−4, 2.86e−5 (∼1/j, fine);
**β=1: 0.0402, 0.0392, 0.0389, 0.0388 (constant — does not tend to 0);**
β=2: 1.63, 6.06, 23.8, 94.7 (∝ j); β=3: 135, 1790, 2.7e4, 4.3e5 (∝ j²).
This is precisely the mechanism of the note's own witness (a), used here in the wrong direction.
**Repair (companion §7.5):** replace the translated bump by a *dilated* one,
`a_j := ψ(x) j^{m′}φ(ξ/j)` with `φ ∈ C_c^∞` supported in an annulus `1 < |η| < 2`. Then
`∂_ξ^β a_j = j^{m′−|β|}(∂^βφ)(ξ/j)` lives on `j ≤ |ξ| ≤ 2j`, so every seminorm is
`≍ j^{m′−|β|}·j^{|β|−m_1} = j^{m′−m_1}`: all `S^{m″}`-seminorms are `O(j^{m′−m″}) → 0` while
`‖a_j‖_{K′,0,0,m′} → const > 0`; and `a_j ∈ V` still, since `ψ ∈ C_c^∞(U∖K)`. Numerically with the
same parameters: m″-seminorms at j = 10,40,160,640 are β=0: 7.3e−4 → 1.3e−5, β=1: 5.5e−3 → 9.3e−5,
β=2: 5.9e−2 → 9.2e−4, β=3: 1.66 → 2.5e−2 (each ÷4 when j ×4, i.e. `Θ(1/j) = Θ(j^{m′−m″})`), while
`‖a_j‖_{0,0,m′}` = 0.0115, 0.0121, 0.0122, 0.0123 → a positive constant. **AGREE with the first
referee**: item 5 falls as written, the repair is the dilation, and **the note does not use item 5**
(the note's (f) rests on non-regularity, items 1–4), so nothing in the note changes.

**Ruling: companion §7 HOLDS except item 5, which FALLS as written (repair given); companion §5
HOLDS as mathematics but has two local defects (the neighborhood N, and "η_0 ≠ 0 automatically"),
both absent from the note.**

---

## 5. Does the external assessment describe (d) and (f) correctly?

**Its endorsement of (d) and the Cor. 6.21 corollary is correct but bare.** It says only that "the
witnesses for Proposition 3.2, Corollary 3.4, **Corollary 4.5**, Corollary 6.14, **Corollary 6.21**,
and Corollary 7.13 are substantially convincing, and they attack the exact statements printed in the
paper rather than peripheral details." No computation for (d) appears anywhere in the text — the
symbol `a_j = j^{m̄′}g(x″)ψ̂_*(ξ/j)`, the two Φ regimes, the vanishing order `2N_0 − |β|`, the
partition-of-unity modification, and the sharpness of `2N_0 ≥ m̄″` are all unexamined. Its verdict
happens to be right; it is not evidence.

**Its dependency quotes are verbatim-correct** (I re-checked all three):
p. 23, Cor. 4.7's proof — "Like in Corollary 3.6, **by Corollaries 4.2 and 4.5**, it is enough to
prove that I(M, L) is semi-Montel"; p. 40, before Cor. 6.22 — "The following result follows like
Corollary 3.6, **applying Corollary 6.21** and using that Ȧ(M) is barreled (Corollary 6.7) and a
closed subspace of the Montel space I(M̆, ∂M) (Corollary 4.7)"; p. 41, before Cor. 6.27 — "the
following analogs of Corollaries 6.21 and 6.22 hold true with formally the same proofs, **using
Corollaries 6.21, 6.22 and 6.26**".

**It is silent on witness (f) and everything around it.** Nowhere does it mention Cor. 3.6,
regularity, bounded retractivity, the non-compact case, the p. 18 bundle extension, or the memoir
[ALKL24m] §2.1.8. Its "Bottom line" list of witnesses omits (f) entirely. Since (f) is the one
witness that refutes a *conclusion* the paper draws (acyclicity), not only a coincidence statement,
and the one that reaches the memoir, the assessment is **incomplete on part (A)** of the sponsor's
question — not wrong, but it cannot be read as an endorsement of the note's §2 list, which includes
Cor. 3.6. **AGREE with the first referee on this reading.**

**Ruling: the external assessment is correct-but-unsupported on (d)/6.21, verbatim-correct on the
dependency claims, and silent on (f). HOLDS-WITH-REPAIR** (the repair being to the *assessment*:
it should not be relayed as covering the note's Cor. 3.6 claim).

---

## 6. Verdict (full statement)

**HOLDS-WITH-REPAIR.**

* **Witness (d) (Cor. 4.5) — HOLDS.** Every step re-derived independently: the (4.8) normalization
  and sign, the scaling `j^{n′+m̄′}ψ_*(jx′) ↦ j^{m̄′}ψ̂_*(ξ/j)`, the seminorm identity, both Φ
  regimes including the exact `|β| < m̄_1 ≤ 2N_0` question (the vanishing order `2N_0 − |β|` is
  exactly enough, with the boundary case `m̄_1 = 2N_0` admissible), the sharpness of `2N_0 ≥ m̄″`
  (new: Φ blows up like `j^{m̄_1−2N_0}` when `m̄_1 > 2N_0`), the lower bound for both signs of `m̄′`,
  membership `C^∞(M) ⊂ ⋂_m I^m` from (4.5)+p. 22+Cor. 4.6's proof, the support shrinkage, the
  modified partition of unity (sum, supports, subordination), the closed-graph choice-independence,
  and (4.9)'s monotonicity. One cosmetic repair to the note: state `0 ≤ ρ ≤ 1`.
* **Cor. 6.21 via (6.47) — HOLDS**, with one step the first referee passed over and I checked: the
  supports of `u_j` are disjoint from `∂M` here, so `h u_j = 0` needs the same ρ-argument, and it
  works because the supports still shrink to `x^{−1}({0}×supp g) ⊂ ∂M`.
* **Witness (f) (Cor. 3.6, non-compact U) — HOLDS.** `b_j ∈ S^j∖S^m`; the single-compact basic
  neighborhood is legitimate (monotonicity in K); `2b_jρ_R ∈ W_1` (vanishing on a *neighborhood* of
  K_1); the Leibniz bound is `Θ(1/R)` (verified numerically at j = 1, 3, 5 and β = 0…3); absolute
  convexity and absorption close it; non-regular ⟹ not boundedly retractive ⟹ not acyclic by the
  p. 4/p. 5 quotations. Scope `n ≥ 1`, `l ≥ 1` is exactly right. The p. 18 bundle extension and the
  memoir §2.1.8 (printed p. 15, checked in **both** arXiv v1 and v2, verbatim) fall with it.
* **One wording repair to the note:** the parenthetical "(Sect. 4.3.3, p. 23, excepts acyclicity for
  non-compact M; …)" — p. 23 excepts acyclicity only "in the case of I(M, L)", and still claims it
  for `⋃_m I^m(M,L)` and `I_c(M,L)`. Rephrase.
* **Companion §7 item 5 FALLS as written** (translated-bump witness; its `S^{m″}`-seminorms are
  `≍ j^{m′+|β|−m″}`, constant at `|β| = m″−m′` and divergent beyond — so `a_j ↛ 0` in `S^{m″}`).
  Repair: dilate instead of translate. The note does not use it.
* **Companion §5 has two local defects the first referee missed / did not raise**: `N` is taken to
  be a neighborhood of the point `p_0` rather than of the compact set `x^{−1}({0}×supp g)` (a real
  gap — with a large `supp g` the argument's first step fails), and "(η_0 ≠ 0 automatically)" is
  false when `N_0 = 0`. Both are correct in the **note**; only the companion needs fixing.
* **The external assessment**: right on (d)/6.21 but with no computation, verbatim-correct on the
  three dependency quotes, and entirely silent on (f), Cor. 3.6, regularity and the memoir.

Nothing found that breaks witness (d) or witness (f).
Sun Sep  6 12:54:56 IST 2026
