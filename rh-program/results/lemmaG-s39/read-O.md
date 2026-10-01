# read-O — OPUS READER on unit `lemmaG-s39` (NOTE.md: Lemma G, the rung-1 necklace counterexample, T2–T5, Theorem F, 𝒞_self)

Reader: Opus 5.5 (second model of the dual-model check; standing orders 5, 7, 11(c)). Started 11:12 IST 2026-10-01.
NOTE read whole at SHA-256 37622108812a994281f492f769c16bcbb70eef928199465509beccffde429c72 (48 965 bytes, 401 lines). Also read:
BRIEF.md, SHARED.md (to 08:30), `conj-O-s38/NOTE.md` ("cO") §1.3–§1.6 and §3.1 (Theorem Z, Lemma Z.a/b, Prop. 1.3, Lemma G,
Prop. 1.6, the dyadic statistic), `beurling-frontier/NOTE.md` ("fr") Theorem C statement (ll. 296–300), the unit's data/logs that
my comparisons use (`verify/data/sq2_1e9.csv`, `verify/logs/*.log`) — never its scripts' code paths. Independent re-run:
`verify-O/` (own C and Python; nothing imported or copied from `verify/`). read-F.md / verify-F/ not opened.
Conventions: ✓ = re-derived at the line; GAP = stated with the fix; FALSE = counterexample or failing step given. NOTE line
numbers below are at the hash above.

VERDICT LINE: (written at the close; see end of file for the running state)

## §1. Re-derivations at the line

**(a) §1.1 Lemma 1.1 (finite R, dilation recursion), ll. 42–53 ✓.** (i) is fr Thm B step (2) (E_{R∪{q}}(x) = E_R(x) − E_R(x/q):
N_{R∪{q}}(x) = N_R(x) − N_R(x/q), ρ_{R∪{q}} = ρ_R(1 − 1/q)) ✓. (ii) c(qa/b) = c(a/b)/q since (q, b) = 1 keeps qa/b reduced and
c(a/b) ∝ 1/a ✓; Parseval over the period Qq ✓. (iii) 2MS − 2MS/q ✓; MS(∅) = 1/12 ✓. Not re-run (rung 1a is cO's, read twice).

**(b) §1.2 Theorem R1 (the necklace deletion), ll. 55–69 ✓, and the computations reproduced by brute force.**
Re-derived: log(1 − au) = −Σ_n a^n u^n/n and Σ_N M(a,N) log(1 − u^N) = −Σ_n (u^n/n) Σ_{N|n} N·M(a,N); Σ_{N|n} N·M(a,N) = a^n is
Möbius inversion of N·M(a,N) = Σ_{d|N} μ(N/d)a^d ✓. Generating function (1 − au)/(1 − qu) ⟹ N_P(n) = q^n − aq^{n−1} (n ≥ 1) ✓;
ρ_R = 1 − a/q from the identity at u = 1/q (Σ_N M(a,N)q^{−N} < ∞ gives absolute convergence) ✓; Σ_n E(n)u^n = (a/q − au)/(1 − qu)
= a/q, i.e. E(0) = a/q and E(n) = 0 for n ≥ 1 ✓. M(a,N) ≤ M(q,N) for a < q: M(x,N) counts primitive necklaces of length N on
x letters, monotone in x ✓ (checked for every (q, a, N) used below). α_R = log a/log q ✓ (π_R is constant on [q^n, q^{n+1})).
*Independent brute force* (`verify-O/o_rung1_bruteforce.py` → `logs/o_rung1_bruteforce.log`; own trial-division code, ALL monic
polynomials enumerated): F_3[T], a = 2, deg ≤ 8; F_5[T], a = 2, 3, 4, deg ≤ 5; F_7[T], a = 3, deg ≤ 4 — each under THREE rules for
WHICH M(a,N) irreducibles are deleted (first / last in lex order / random): N_P(n) = q^n − aq^{n−1} in all 15 cases (n ≤ nmax).
F_3: irreducible counts 3, 3, 8, 18, 48, 116, 312, 810 and N_P = 1, 3, 9, …, 2187 — the NOTE's numbers digit for digit (l. 70–72).
(F_2[T] admits no case: R1 needs 2 ≤ a < q.) *Second route* (`o_rung1_genfun.py` → `logs/o_rung1_genfun.log`; exact integer series
mod u^61, ρ in 120-digit mpmath to N = 600): D_R ≡ 1 − 2u mod u^61, ρ − 1/3 = 2·10⁻¹⁰⁹ (truncation), max_{n≤60}|E(n)| = 1·10⁻⁸⁰.
Controls: regular r_N = round(2^N/N): ρ = 0.28090918095125851173… and d_1..d_12 = −2, −1, 1, 1, 3, −3, 3, −2, 0, 1, −1, −3 — equal to
the unit's log digit for digit; but E(n)n^{3/2}/2^{n/2} over ALL n = 20…60 ranges over [−0.382, +0.288], not [−0.37, +0.26]: the
NOTE's range is the step-5 sample n = 20, 25, …, 60 (unit log) — minor m2. Random control (own draw): E(n)/2^{n/2} ∈ [−0.217, 0.454]
on n = 6…22 (all n; the NOTE's "−0.16 … 0.46" is the step-2 sample) — same order 2^{n/2} ✓.
*Which form of O is false at rung 1 (target (a)).* EVERY form: E(n) = 0 for all n ≥ 1, so the degree-wise sup form
(|E(n)| ≥ q^{n(α_R/2−ε)} i.o.), the degree-wise mean-square form (Σ_n E(n)²q^{−2σn} = ∞ for σ < α_R/2) and even "E ≠ 0 i.o." all
fail; the cumulative form Σ_{m≤n}E(m) = a/q fails too. The only convention-dependence is the rung-1 dictionary itself (degree-wise
counts replace x; fr §5.4) — over ℝ the count at real x is a step function and no other main term is natural.

**(c) §1.3 (what rung 1 says), ll. 80–108.** (a) ✓: P_R(u) = −Σ_m (μ(m)/m) log(1 − au^m) (Möbius inversion of L = −Σ_k P_R(u^k)/k);
m = 2 gives branch points at u = ±a^{−1/2}, i.e. s = α_R/2 + iπk/log q ✓; already m = 1 puts branch points at s = α_R + 2πik/log q,
so P_R has no single-valued continuation to {σ > τ₀, |t| > T₀} for any τ₀ < α_R ✓. (b) ✓ (κ = 1 at the zeros, κ = −½ at the halves,
κ = −⅓ at σ = α_R/3, …). (c) ✓ with one false item: "|ζ_P| ≤ C|t| trivially" (l. 91) is wrong at rung 1 — ζ_P = (1 − au)/(1 − qu)
has poles at s = 1 + 2πik/log q at EVERY height; harmless, since Theorem Z's proof only uses the bound for D_R (|D_R| ≤ 1 + a ✓) —
minor m3. The Pringsheim + periodicity argument that Theorem Z's HYPOTHESIS is void at rung 1 for every R with α_R > 0 ✓ (P_R itself
has nonnegative coefficients and radius q^{−α_R}, so it is singular at s = α_R + 2πik/log q for all k). (d) ✓ as a diagnosis, with
one inaccuracy: "the norm is injective on ⟨R⟩; equivalently the log p, p ∈ R, are linearly independent over ℚ" (ll. 98–99) — the two
are not equivalent in general (injectivity on SQUAREFREE products is weaker: g-primes 2, 4 have injective squarefree products 1, 2, 4,
8 but dependent logarithms); for rational primes both hold, so nothing downstream changes — minor m4. *Statement (G₁)* is a META
statement (the listed inputs hold in the rung-1 dictionary, where O fails); it is correct as such but is not a theorem about ℚ —
its force depends on the dictionary; it should be labeled [heuristic/no-go], not [proved here] — minor m5.

**(d) §2.1 Theorem 2.1 (local structure), ll. 112–128 ✓ — target (b).** β₂ ≤ α_R: |E| ≤ Q_R(x) + xΣ_{m∈⟨R⟩,m>x}1/m and
Σ_{m∈⟨R⟩}m^{−σ} = Π_{p∈R}(1 + p^{−σ}) < ∞ for σ > α_R give E ≪ x^{α_R+ε} ✓. (a) ζ_P(s) = ρs/(s − 1) + s∫_1^∞E x^{−s−1}dx on σ > β₂
(Cauchy–Schwarz against the weight, cO Prop. 1.3(i)) ✓; D_R(1) = ρ ✓; n(w) = 0 for Re w > α_R (absolutely convergent nonzero
product) ✓; poles of D_R only at zeros of ζ, order ≤ ord_w ζ ✓. (b) *The Möbius inversion and its tail:* for σ > α_R,
−Σ_m μ(m)m^{−1}L(ms) = Σ_{m,k} μ(m)(mk)^{−1}P_R(mks) = Σ_n n^{−1}P_R(ns)Σ_{m|n}μ(m) = P_R(s), the rearrangement justified by
Σ_{m,k}(mk)^{−1}|P_R(mks)| ≤ Σ_n d(n)n^{−1}P_R(nσ) < ∞ ✓. On a compact K ⊂ {σ > β₂} with σ_K := min_K σ (> 0; the NOTE tacitly uses
β₂ ≥ 0, true for R ≠ ∅), every m > (α_R + 2)/σ_K has |L(ms)| ≤ 2Σ_{p∈R}p^{−mσ_K} ≪ 2^{−mσ_K}: the tail is a uniformly convergent
series of functions analytic on K that need NO continuation; only the finitely many m ≤ (α_R + 2)/σ_K need L continued, and L = log D_R
continues along any path in {σ > β₂} avoiding the zeros/poles of the meromorphic D_R ✓. Σ_R ∩ K finite ✓ (mK ⊂ {σ > β₂} since
Re(ms) ≥ Re s). Local germ: L(ms) = n(ms₀)log(s − s₀) + n(ms₀)log m + log g_m(ms) ✓; branches differ by constants ✓. (c) ✓
(m ≥ 2 has Re(ms₀) > α_R when Re s₀ > α_R/2; at Re s₀ = α_R/2 only m = 2 joins, μ(2) = −1; in general squarefree m ≤ α_R/Re s₀).

**(e) §2.2 Corollary 2.2, ll. 129–138 — GAP in the quantifier (F3 below), all four applications unaffected.** The contrapositive of
Thm 2.1 controls only continuations along paths INSIDE {σ > β₂}; the statement allows "continued from σ > α_R along SOME path". A path
that leaves {σ > β₂} and returns can reach s₀ on a different sheet (D_R is single-valued on {σ > β₂}, but its continuation around a
branch point left of β₂ need not return to the same germ), so the corollary as worded is not implied. Fix: restrict to paths in the
closed half-plane {σ ≥ Re s₀} (then β₂ < Re s₀ puts the whole path in {σ > β₂}); (i) is fine with the usual meaning of "natural
boundary of the function defined on σ > σ_b". T2 (a pole of the single-valued D_R), T3 and T5 (real axis from the right) and T4
(horizontal approach s_j + δ, δ ↓ 0) all use such paths ✓. Items (ii)–(iv) ✓ given 2.1(a),(c); (iii) at Re s₀ = α_R/2 tacitly
needs D_R meromorphic at 2s₀ (Re = α_R) — automatic under the contrary hypothesis β₂ < α_R/2 ✓. Consistency check: for regular
deletions P_R ≈ −c log(s − α), so (iii) gives β₂ ≥ α_R when c ∉ ℤ — exactly fr Theorem C's "(s − α)^c" case (fr l. 300) ✓.

**(f) §2.3 Proposition 2.3 (RH), ll. 139–145 ✓.** (a) Under RH the zeros of ζ in σ > β₂ lie on σ = ½ > α_R where n = 0 ✓. The
growth bound needs NO Phragmén–Lindelöf band: for α_R < ½, D_R is the absolutely convergent product (bounded) on σ ≥ α_R + δ, and on
β₂ + δ ≤ σ ≤ α_R + δ < ½, |D_R| ≤ |ζ_P||χ(s)|^{−1}|ζ(1 − s)|^{−1} ≪ |t|^{1+ε} (cO Prop. 1.3(ii): Stirling + the RH bound for
1/ζ on Re ≥ ½ + δ″) ✓ — the NOTE's pointer "(Z1, Z3)" should be "cO Prop. 1.3(i)–(ii)", since Z3's band argument used Theorem Z's
hypothesis (minor m6). (b) ✓: zero-free D_R on U (two simply connected components) ⟹ L analytic, Re L ≤ O(log|t|) ⟹ |L| ≪ log|t|
on σ ≥ τ₀ + η (Lemma Z.a) ⟹ P_R = −Σ_m μ(m)L(ms)/m analytic on U (ms ∈ U) with |P_R| ≪ log|t| (finitely many m matter) ⟹ Theorem Z
⟹ β₂ ≥ α_R/2, contradiction ✓; zeros with σ > α_R are impossible and only finitely many lie below any height ✓. Novelty note: cO's
(G′) (cO l. 159) already records "for α_R < ½ the critical-line clause is automatic", i.e. no poles; 2.3 is that remark made a
proposition — the NOTE should cite it (minor m7).

