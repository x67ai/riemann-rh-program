# read-O — OPUS READER on unit `lemmaG-s39` (NOTE.md: Lemma G, the rung-1 necklace counterexample, T2–T5, Theorem F, 𝒞_self)

Reader: Opus 5.5 (second model of the dual-model check; standing orders 5, 7, 11(c)). Started 11:12 IST 2026-10-01.
NOTE read whole at SHA-256 37622108812a994281f492f769c16bcbb70eef928199465509beccffde429c72 (48 965 bytes, 401 lines). Also read:
BRIEF.md, SHARED.md (to 08:30), `conj-O-s38/NOTE.md` ("cO") §1.3–§1.6 and §3.1 (Theorem Z, Lemma Z.a/b, Prop. 1.3, Lemma G,
Prop. 1.6, the dyadic statistic), `beurling-frontier/NOTE.md` ("fr") Theorem C statement (ll. 296–300), the unit's data/logs that
my comparisons use (`verify/data/sq2_1e9.csv`, `verify/logs/*.log`) — never its scripts' code paths. Independent re-run:
`verify-O/` (own C and Python; nothing imported or copied from `verify/`). read-F.md / verify-F/ not opened.
Conventions: ✓ = re-derived at the line; GAP = stated with the fix; FALSE = counterexample or failing step given. NOTE line
numbers below are at the hash above.

VERDICT LINE: **AGREES-WITH-CORRECTIONS** on the close "G, with T-parts and a rung-1 counterexample". Re-derived at the line:
Thm R1 (and brute-forced over ALL monic polynomials in F_3, F_5, F_7 under three deletion rules — N_P(n) = q^n − aq^{n−1} in all
15 cases; every form of O, sup, mean-square and cumulative, fails at rung 1), Thm 2.1 (the Möbius inversion and its tail ✓),
Cor. 2.2 (✓ once continuation paths are restricted to {σ ≥ Re s₀} — F3; no application affected), Prop. 2.3 (✓; cO's (G′) remark
made a proposition), T3, T4, Theorem F, Cor. F.1, Lemma 3.6 (✓), and "(RH, α_R < ½) every counterexample lies in 𝒞_self" (✓, true
by definition once 2.3 and F hold). T2 and T5 are proved, but each rests on a FALSE distinctness line: F1 — "the intervals are
disjoint" fails for k = 2, so the computed family sq = {nextprime(p²)} is covered by T2 only under RH or with a recalled
large-gap bound, not "uncond." as the NOTE says four times; F2 — T5's spacing N·2^N lies below every proved gap bound — repaired
by a greedy choice, unconditional with Ingham. No other step silently uses RH or an unproved gap bound; the first-zero inputs were
checked by the argument principle (simplicity not needed). The independent re-run (own sieve with exact integer sums) reproduces
every number the close rests on digit for digit: sq to 10⁹ and 10¹⁰ (0.437/0.435/0.463; 0.431/0.422/0.431, sup 0.231, κ 1.41,
M/M_diag 1.06 … 0.324), the 200-zero explicit formula (corr 0.882/0.980/0.998), the tight necklace (0.801/0.792/0.789, M/M_diag
371), |ζ(ρ₁/k)|, C(ρ₁/2) and h_N/(c_N ln 4^N). One correction UPGRADES the close (F4): the tight ℚ-necklace — Theorem F's only
example — obeys O UNCONDITIONALLY (β = α_R, β₂ ≥ α_R/2) by the NOTE's own cluster lemma with Selberg's upper-bound sieve in place of
Legendre (§7 A1, single-check; general form A2: counterexamples to O must be anti-clustered). Prior art on disk was missed (F5:
Hilberdink 2012 Thm A — over ℚ, periodic N − cx forces a finite deletion — the nearest published object to R1). 31 pairs (14
FIX-FIRST in F1–F5, 17 minor).

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

**(g) §3.1 Theorem T2, ll. 152–170 — proof ✓ for k ≥ 3 and for injective choices; FALSE side-claim for k = 2 (F1) — target (c).**
Re-derived: |r_p^{−s} − p^{−ks}| ≤ |s|p^{kθ′}p^{−k(σ+1)}, summable iff σ > σ_C = 1/k − 1 + θ′ < 1/(2k) ⟺ θ′ < 1 − 1/(2k) ✓; C(s)
analytic zero-free on σ > max(σ_C, 0) ✓; D_R = C·Π_{p<p₀}(1 − p^{−ks})^{−1}·ζ(ks)^{−1} ✓; at s₀ = ρ₁/k, 1/ζ(ks) has a pole of order
ord_{ρ₁}ζ ≥ 1, ζ(s₀) ≠ 0 since 0 < Re s₀ ≤ ¼ and 0 < Im s₀ < γ₁; if β₂ < Re s₀ then ζ_P is analytic at s₀ and D_R = ζ_P/ζ would be
analytic there ✓. No RH, no unproved gap bound beyond Ingham (existence of a prime in [y, y + y^{5/8+ε}]) ✓. *Simplicity of ρ₁ is
not needed* (any zero works; minor m8). *Inputs checked:* argument principle (`verify-O/o_zeta_checks.py` → `logs/o_zeta_checks.log`,
own mpmath code): 0 zeros of ζ in [−½, 3/2] × [0.02, 0.6] and in [−½, 3/2] × [0.5, 14.0], exactly 1 up to t = 14.3; ρ₁ =
½ + 14.134725141734693790i, ζ′(ρ₁) = 0.783296511867 + 0.124699829748i; |ζ(ρ₁/k)| = 1.1263387, 0.66456376, 0.51000106, 0.44808699
(k = 2…5) — NOTE l. 161 digit for digit; C(ρ₁/2) for r_p = nextprime(p²): 0.035705864 − 0.360570337i (p ≤ 10⁵), 0.035705873 −
0.360570346i (p ≤ 10⁶) — NOTE's 0.0357 − 0.3606i ✓, tail ≲ 10⁻⁸ ✓. Ingham θ = 5/8 (Quart. J. Math. 8 (1937) 255–266) and Huxley
7/12 (Invent. Math. 15 (1972)) as asymptotics π(x + x^θ) − π(x) ~ x^θ/log x: quoted from a secondary source at the line
(`verify-O/sources/wiki-prime-gap.raw.txt` ll. 270–287; the originals not opened — [quoted, secondary]).
*The false side-claim.* "the intervals are disjoint for p ≥ p₀" (l. 153) holds iff (p′)^k − p^k > p^{kθ′} for consecutive primes,
i.e. (with p′ − p ≥ 2) iff θ′ < 1 − 1/k ⟺ k ≥ 3 at θ′ = 5/8 + ε. For k = 2, (p′)² − p² ≤ 2p′(p′ − p) < p^{5/4} whenever p′ − p
< p^{1/4}/3 — for most consecutive pairs (average gap log p) — so the intervals overlap, the "r_p" may coincide, and an adversarial
choice (one prime for all p in [y, y + y^{1/4}]) makes R_2 thinner (α_R ≈ 3/8) and breaks D_R = C/ζ(2s). Fix: require p ↦ r_p
injective — always possible greedily (the interval holds ≫ p^{kθ′}/log p primes by Ingham's asymptotic while ≪ p^{kθ′−k+1} earlier
intervals meet it); the proof then runs verbatim. *Consequence for sq = {nextprime(p²)}* (the NOTE's computed family, said to carry
"T2: β₂ ≥ ¼ uncond.", ll. 258, 276, 289, 357): injectivity needs a prime in [p², p′²) — open (a collision needs a gap ≥ 4p + 4 ≈ 4√x
after x = p²). Collisions are harmless if their counting exponent is < ¼ (the extra factor Π(1 − r^{−s})^{−1} is then analytic
and zero-free at Re s = ¼): this follows from RH (Selberg: Σ_{p_n≤x, d_n≥H}d_n ≪ x log²x/H gives ≪ log²x collisions)
[recalled, unverified], or from a large-gap moment bound with exponent < 3/4 (Peck 25/36, Matomäki 2/3 for Σ_{d_n ≥ √p_n}d_n)
[recalled, unverified]; Heath-Brown's x^{3/4+ε} is NOT enough. Computed: max(nextprime(p²) − p²) = 232 for p ≤ 10⁶, so no collision
on the computed range. Until one of these inputs is quoted at the page, sq is covered by T2 under RH, not unconditionally (F1).

**(h) §3.2 Theorem T3, ll. 172–178 ✓ (k ≥ 3).** Distinctness: (n + 1)^k − n^k ≥ kn^{k−1} > n^{kθ′} ⟺ θ′ < 1 − 1/k, true for k ≥ 3
(5/8 < 2/3) ✓; P_R = ζ(ks) − Σ_{n<n₀}n^{−ks} + H, H analytic on σ > θ′ − 1 + 1/k < 1/k ✓; simple pole of residue 1/k at s = α_R,
reached along the real axis from the right ⟹ β₂ ≥ α_R (Cor. 2.2(ii)) and β₂ ≤ α_R ✓. k = 2 correctly conditioned on distinctness
(Legendre); as for sq, sparse collisions (exponent < ½ here) would also do. Bessel law: [heuristic] as labeled ✓.

**(i) §3.3 Theorem T4 (planted modulation, natural boundary), ll. 180–193 ✓ with two minor repairs.** Re-derived: ∫u^{−s}dF_c =
cP(s + 1 − α) − Σ_{p≤p₀}(cp^{α−1} − 1)p^{−s} ✓; G = Σ_j (a_j/2)(u^{s_j} + u^{s̄_j}) gives ∫_1^∞u^{−s}dG = Σ_j (a_j/2)(s_j/(s − s_j) +
s̄_j/(s − s̄_j)) on σ > α/2, absolutely (Σ a_j|s_j| ≤ εΣ2^{−j}) ✓; at s = s_j + δ the j-th term is a_js_j/(2δ), the others are bounded by
Σ_i a_i|s_i|q_iq_j (|γ_i − γ_j| ≥ 1/(q_iq_j); q_i ≤ height ≪ √i, so Σ 2^{−i}√i < ∞) and the conjugate terms by Σ a_i|s_i|/γ_j ✓;
cP(s + 1 − α) has at worst a logarithmic singularity there (Re w ∈ (½, 1): m ≥ 2 terms analytic, log ζ singular only at zeros) ✓;
density of {s_j} on σ = α/2 ⟹ natural boundary ⟹ β₂ ≥ α/2 (Cor. 2.2(i)) ✓. Unconditional ✓ (no RH; one zero-free input is not
needed). Repairs: (1) "|π_R − T| ≤ 2 for large x (… G varies by o(1) between consecutive primes)" (l. 183) needs gaps
o(x^{1−α/2}); with the proved gap x^{0.525} it holds for α < 0.95; for α ∈ [0.95, 1) one only gets |π_R − T| ≪ 1 + x^{α/2−0.475} —
still O(x^θ) with θ < α/2, so H is analytic on σ > α/2 − 0.475 and the proof stands (minor m9). (2) The "More generally" clause
(ll. 184–186): a LOGARITHMIC singularity of Ĝ with κ ∉ ℤ at s₀ = ρ − 1 + α (ρ an off-line zero, Re ρ ≥ 1 − α/2) can combine with
cP(s + 1 − α)'s germ (coefficient −c·ord_ρ ζ) into an allowed one; say "a singularity of Ĝ at which P(s + 1 − α) is analytic, or
one that is not logarithmic" (minor m10).

**(j) §3.4 Theorem T5 (spread necklace), ll. 195–206 — proof ✓, FALSE distinctness justification (F2).** Re-derived:
Euler–Maclaurin Σ_{j<c}(1 + j/c)^{−s} = cΦ(s) + ½(1 − 2^{−s}) + O(|s|(|s|+1)/c) (remainder analytic in s) ✓; 𝒩(s) = Σ_N c_N4^{−Ns}
= −Σ_m (μ(m)/m)log(1 − 2·4^{−ms}) ✓; m = 1 gives −log(s − ½) + analytic (d/ds(1 − 2·4^{−s}) = log 4 at ½) and m ≥ 2 is analytic at ½
(1 − 2^{1−m} ≠ 0) ✓; Σ_N 4^{−Ns} analytic on σ > 0 ✓; so P_R = −Φ(s)log(s − ½) + analytic near ½ with Φ(½) = 2(√2 − 1) =
0.82843 ∉ ℤ, and −(Φ(s) − Φ(½))log(s − ½) is not analytic: forbidden germ at Re s₀ = α_R reached along the real axis ⟹ β₂ = α_R ✓.
Unconditional apart from the definition. *The false line:* "distinct for large N: 4^N/c_N ≈ N2^N exceeds the Ingham gap
4^{(5/8+ε)N}" (l. 198). It is the other way round: N2^N = N·4^{N/2} < 4^{(5/8)N} for N ≥ 20 (at N = 20: 2.1·10⁷ vs 3.4·10⁷), and
N·4^{N/2} is below EVERY proved gap bound 4^{θN} (θ ≥ 0.525); even RH's gap √x log x ≈ 1.39·N2^N is of the same size. So
nextprime(4^N + j⌊4^N/c_N⌋) is not known to be injective in j. Fix (unconditional, Ingham only): define r_{N,j} := the least prime
≥ 4^N + j⌊4^N/c_N⌋ not already chosen. Displacement bound: if r_{N,j} − t_j > L ≥ x^{5/8+ε} (x = 4^N), every prime of [t_{i₀}, t_j + L]
would be taken by the ≤ (t_j − t_{i₀})/D + 1 earlier targets (D = ⌊4^N/c_N⌋ ≈ N2^N), while Ingham's asymptotic gives ≥
(t_j + L − t_{i₀})/(2 log x) primes there — impossible since D ≫ log x. So |r_{N,j} − t_j| ≤ 4^{(5/8+ε)N} and l. 199's estimate holds
verbatim. (The unit's code aborts on duplicates — `lg.c` l. 44 — so the computed set is the nextprime set and duplicate-free for
N ≤ 16; nothing in §4 changes.)

**(k) §3.4 tight necklace (ll. 207–212) ✓; §3.5 Theorem F and Corollary F.1 (RH), ll. 214–233 ✓ (two minor points) — but F.1's
conclusion holds UNCONDITIONALLY (F4, ADD A1).** Tight necklace: D_R = (1 − 2·4^{−s})·C on σ > ½ (all products absolute), C absolutely
convergent on σ > 1/12 + ε (c_N·4^{(7/12+ε)N}·4^{−N(σ+1)} summable), zero-free for σ > 0 ✓; Ingham's 5/8 suffices here too (needs
θ < ¾) ✓; zeros ½ + 2πik/log 4 simple, no poles; κ = 1 on σ = ½, −½ on σ = ¼ ✓. Theorem F: (Z1),(Z3) — for α_R < ½ the bound
|D_R| ≪ |t|^{O(1)} on σ ≥ τ + δ/2 is cO Prop. 1.3(ii) (product on σ > α_R, functional equation + RH left of it), no band argument
needed ✓; Borel–Carathéodory on log C with Re log C = log|D_R| − log|G| ≤ O(log|t₀|) on the (F2) circles ✓; Mellin–Barnes shift ✓;
MV (G.27) with δ_λ ≥ e^{−K(λ+1)} and N = T^{1/(K+1)} keeps the off-diagonal below the diagonal, the e^{−e^λ/N} weights kill λ > log N
✓; contradiction with (F3) at σ* ✓. Minor: the circles' centre must sit where log C is O(1); (F1) only gives absolute convergence
on σ > σ₁, so take centres max(α_R + 2, σ₁ + 1) + it₀ (harmless: F.1 has σ₁ = ½) (m11). Corollary F.1 ✓: G = 1 − 2·4^{−s} bounded,
→ 1, min-modulus by periodicity and avoidance of ≤ 2 zeros per circle-radius window; (F1) frequencies k log r and n log 4 distinct
(r^k odd, 4^n even), |log(a/b)| ≥ 1/max(a, b) for integers a ≠ b ⟹ K = 1; (F3) from b = −1 at each log r (and the n log 4 part
alone diverges for σ < ½) ✓.
*But the tight necklace needs no RH.* The NOTE's own cluster Lemma 3.6 with Selberg's upper-bound sieve in place of Legendre gives,
unconditionally, max(|E(4^N)|, |E(4^N + h_N)|) ≥ c_N/3 for large N — so β(R_tight) = α_R = ½ (sup form) and β₂(R_tight) ≥ ¼ = α_R/2
(mean square) without RH; proof in §7 A1. Theorem F therefore has no application on record that is not already unconditional.
*Computed* (`verify-O/o_cluster_check.py` → `logs/o_cluster_check_16.log`, N_P by inclusion–exclusion over the 36 849 squarefree
R-numbers ≤ 4.3·10⁹ — a route different from the unit's sieve; ρ = 0.61358259342980… from the cyclotomic identity, = the unit's
0.613583): h_N/(c_N ln 4^N) = 0.979, 1.049, 0.992, 1.001, 1.000 (N = 12…16) — NOTE l. 239 digit for digit; exact jump
E(4^N + h_N) − E(4^N) = −1.36c_N (N = 9…16, stable); exact interval-sieve deviation S(I, P_{<N}) − ρ_{<N}h_N = −0.36c_N (negative:
it helps) against the A1 bound h_N^{2/3} = 2016 < c_N = 4080 at N = 16; |E(4^N + h_N)| = 1.20c_N, and max|E| on [4^N − 3h, 4^N + 6h]
= 1.81c_N (`logs/o_cluster_max.log`; still rising at +6h — the NOTE's "1.9c_N (7781)" is window-dependent, consistent).

**(l) §3.6 Lemma 3.6, ll. 235–241 ✓.** #{R-free n ∈ I} ≤ #{n ∈ I : (n, P_z) = 1} − c (the c cluster primes are coprime to P_z
and not R-free) ≤ ρ_zh + 2^{π_R(z)} − c ✓. The closing clause "as long as the clusters stay this tight (h_N ≪ c_N log 4^N),
sup|E| ≥ x^{α_R}/(C log x) infinitely often" is TRUE but not shown: with Legendre it needs z with 2^{π_R(z)} = o(c_N) AND
(ρ_z − ρ)h_N = o(c_N); z = N³ does not (π_R(N³) ≍ N^{3/2}/log N > N), z = CN² does: π_R(CN²) ≍ √C·N/log N < N − log₂(4N), and
(ρ_z − ρ)h ≍ c_N/(√C log N) → the clause holds given tightness. A1 removes the tightness hypothesis (Ingham's span suffices).

**(m) §4 and §6 (computation; 𝒞_self) — targets (d), (e):** see §2 for the re-run. §6: 𝒞_self is well defined as a predicate
on R (all of (F1)–(F3) are definite conditions; "no factorization exists" is a legitimate, if non-effective, clause). "(RH, α_R < ½)
every counterexample lies in 𝒞_self" ✓: a counterexample has β₂ < α_R/2; Prop. 2.3(a) gives continuation with polynomial growth to
{σ > τ₀} for τ₀ ∈ (β₂, α_R/2); 2.3(b) gives infinitely many zeros there (hence at unbounded heights); Theorem F excludes every
(F1)–(F3) factorization on every Ω — so the clause holds under either reading of its quantifiers ✓. Three caveats: (1) the inclusion
is true BY DEFINITION once 2.3 and F are proved — 𝒞_self is "what Prop. 2.3 leaves and Theorem F does not cover"; the obstruction
sentence ("cannot yield Lemma G on 𝒞_self, because there, by definition, …", ll. 348–349) is a tautology and should be labeled as
such (m12); (2) "convergent diagonal" (l. 349) is not the negation of (F3) — the negation is "sub-polynomial growth for some
σ < α_R/2" (m13); (3) "Smallest class where the answer is unknown" (ll. 31, 351) is not a theorem: no minimality is proved, and
𝒞_self as defined only constrains |t| > T₀, so it can contain sets on which O is KNOWN by Cor. 2.2 applied near the real axis (a
forbidden real singularity, e.g. a T5-type germ at s = α_R). A sharper residual class that still contains every counterexample
(Prop. 2.3(a)): add "D_R analytic on the whole half-plane σ > τ₀" (ADD A3). The F_q[T]-analogue claim ✓: at rung 1 periodicity
makes D_R bounded, so any (F2) factor forces |log C| bounded and Parseval bounds the diagonal — no deletion admits (F1)–(F3) there;
the necklace (infinitely many zeros, polynomial growth) is in the analogue ✓.

## §2. Independent re-run (`verify-O/`; own code; big scratch in `/private/tmp/rh-s40-lemmaG/`, regenerable as below)

**2.1 Rung 1** — §1(b): brute force over all monic polynomials (15 cases, 3 deletion rules) and exact series: ALL EQUAL.
**2.2 sq = {nextprime(p²)} — exact dyadic mean squares to 10⁹ AND 10¹⁰ by an independent route.** Own segmented sieve
(`o_sieve_bins.c`, 1.2 s at 10⁹, 11.8 s at 10¹⁰) emitting EXACT integer bin sums Σ N, Σ N², Σ N(2n + 1) in __int128 (no float in
the counts); Σ (N(n) − ρ(n + ½))² formed afterwards in 50-digit arithmetic (`o_sq_analysis.py`); ρ from my own product
(`o_sq_gen.py`: p ≤ 10⁶ exactly, tail via primezeta(2), neglected terms < 10⁻¹⁸): ρ = 0.668524156691798154409989…, which differs from
the unit's header value 0.668524156691795768 by 2.39·10⁻¹⁵ (the unit's double-precision log-sum; harmless: Δρ·X = 2.4·10⁻⁵ at 10¹⁰).
Bins = the unit's grid (edges read from its CSV). Results: counts equal in all 170 / 190 bins; Σ(N − ρ(n + ½))² equal to the unit's
CSV to its printed 7 digits (max rel. diff 3.8·10⁻⁷ with the unit's ρ); maxE/minE equal up to Δρ·x. With EITHER ρ:
10⁹: ms-slope [10⁴,X] 0.437, [10⁶,X] 0.435, top3 0.463, sup 0.239, κ = 1.12, M/M_diag (own DFS for W, 14 073 R-numbers)
1.06, 0.89, 0.906, 0.904, 0.81 — `verify/logs/dyadic_1e9.log` digit for digit. 10¹⁰: 0.431 / 0.422 / 0.431, sup 0.231, κ = 1.41,
M/M_diag 1.06, 0.91, 0.81, 0.324 (56 021 R-numbers) — NOTE l. 258 digit for digit. N(10⁹) = 668 524 135, N(10¹⁰) = 6 685 241 558.
**2.3 The explicit formula for sq (NOTE l. 270–276), recomputed:** own C(ρ_j/2) (numpy over the 9 592 R-primes ≤ 10¹⁰), mpmath
zeros/ζ/ζ′: |c_ρ| = 0.0364, 0.0210, 0.0256 (ρ₁, ρ₂, ρ₅) ✓; bin means of E (exact, from Σ N) vs exact bin averages of the 200-zero
sum, both / x^{1/4}: corr 0.8824 (120 bins ≥ 10⁴), 0.9800 (≥ 10⁶), 0.9979 (≥ 10⁸; resid rms 0.0093, signal 0.0690) — the NOTE's
0.882 / 0.980 / 0.998 and 0.0093 / 0.069 ✓. So sq's sub-diagonal slope 0.422 is the low-zero beat at ρ/2, as claimed.
**2.4 Second family, tight ℚ-necklace to 10¹⁰** (`o_neck_gen.py`; ρ from the cyclotomic identity + a first-order tail model,
0.61358259343171, vs the unit's 0.613582593431613 (Nmax = 22 explicit) — Δ = 9.5·10⁻¹⁴): counts equal in all 190 bins; ms 0.801 /
0.792 / 0.789, sup 0.479, κ = −5.23, M/M_diag 16.3, 46.1, 165, 371 — NOTE l. 262 digit for digit.
**2.5 Cluster lemma / A1 numbers** — §1(k) (inclusion–exclusion route). **2.6 ζ inputs** — §1(g).
Regenerate scratch: `python3 o_sq_gen.py 1e10 1e6; python3 o_neck_gen.py`; bins = columns 2–3 of the unit's CSVs;
`clang -O3 o_sieve_bins.c -o o_sieve_bins -lm; ./o_sieve_bins 1e10 R_sq_1e10.txt bins_1e10.txt <rho_hi> <rho_lo>` (bin TSVs copied
to `verify-O/logs/`).

## §3. Prior art at the page

*Citations the NOTE relies on, opened at the lines it names* (all ✓ unless stated):
- Hilberdink 2005 (fr `w-18a…txt` ll. 222–258): Theorem A (zero order), Remark B(ii) (finitely many zeros ⟹ zero order), Carlson's
  mean value under separation (3.1) — as described ✓.
- DMV 2006 (fr `p1-02…txt` ll. 183–200): Thm 1 — a system of Beurling primes with N = κx + O(x^θ), ζ_B analytic on σ ≥ θ but with
  infinitely many zeros on σ = 1 − a/log t ✓. Wording: DMV's system is DISCRETE (a sequence of real g-primes); "in the CONTINUOUS-
  density world" (l. 300) misdescribes it — the contrast intended is "real g-primes, not a subset of ℙ" (m14).
- Broucke–Vindas 2024 (fr `z-18…txt` ll. 34–45, 97–111): Thm 1.1 (DMVZ) and Thm 1.2 (|π_P − F| ≤ 2 and the √x + √(x log(|t|+1)/
  log(x+1)) bound) ✓ (the NOTE writes log x for log(x + 1); immaterial).
- Avdeeva 2015 (cO `avdeeva…txt` ll. 117–135): Thm 1 (2 ∉ B, N_B = AN^α + O(N^β), β < α < 1 ⟹ Var_B(N) ∼ CN^α) ✓.
- Breuer–Simon 2011 (`sources/breuer-simon…txt` l. 247 Thm 1.7, ll. 618–628 Thm 5.1 (Szegő/Duffin–Schaeffer/Boas), ll. 672–680
  Thm 6.1 (independent coefficients)) ✓ — all power series, as the NOTE says.
- Bhowmik–Schlage-Puchta (`sources/bhowmik…txt` ll. 30–60): Estermann (integer-valued polynomial W, W(0) = 1: finite product of
  ζ(νs)^{c_ν} or natural boundary Re s = 0) and Dahlquist's extension ✓.
- Fabry/Pólya (`sources/wiki-fabry…txt`): Fabry for power series ✓; the Dirichlet-series form stays [recalled] as labeled.
- DZ book (`sources/dz-2016-book.txt`): 0 hits for "function field / finite field / polynomial ring" ✓ (the NOTE's claim).
- Ingham 1937 / Huxley 1972 / BHP 2001: only through Wikipedia "Prime gap" (`verify-O/sources/wiki-prime-gap.raw.txt` ll. 270–287:
  Ingham θ > 5/8 asymptotic, Quart. J. Math. 8 (1937) 255–266; Huxley θ = 7/12, Invent. Math. 15 (1972); BHP 0.525) — [quoted,
  secondary]; first zero and simplicity — computed (§1(g)).
*Missed on disk — bears on R1 and on §1.3(d) (F5).* **Hilberdink 2012**, "Generalised prime systems with periodic integer counting
function" (Acta Arith. 152), `novel-wave-s37/beurling-fe/sources/p3-22c2-…txt` ll. 44–51 (abstract) and ll. 102–116 (Theorem A): "Let
N ∈ T be such that N(x) − cx has period P, and suppose that N determines a g-prime system. Then P ∈ ℕ and N(x) = Σ_{n≤P,(n,P)=1}
([(x − n)/P] + 1), i.e. N is the integer-counting function of the g-prime system P ∖ {p_1, …, p_k} where p_1, …, p_k are the prime
divisors of P." — the ℚ-side theorem that EXACT regularity (E periodic, in particular E ≡ 0 up to a periodic term) forces a FINITE
deletion. It is the nearest published object to Thm R1 and the precise ℚ-counterpart of §1.3(d)'s "commensurability" diagnosis:
over ℝ-norms the rung-1 phenomenon (infinitely many deletions, E ≡ 0) is impossible by a printed theorem. It does not touch R1's
novelty (R1 lives in F_q[T]); it should replace "[recalled] cyclotomic identity" as the distance-from-upstream anchor.
*Novelty searches* (arXiv API, one query at a time, saved in `verify-O/sources/arxiv-r1…r6*.xml`): additive/arithmetical semigroups
(4 + 14 hits: Meissel, power-free elements, Alladi, Warlimont functions, Beurling-prime RvM formula — none constructs a deletion with
exactly regular counts); "Beurling" ∧ "function field" (0); "necklace polynomial" ∨ "cyclotomic identity" (13: Witt transform
math/0311194, necklace analytics 2605.11445, liminal reciprocity 1803.08438, cyclotomic enumeration 2410.12058 — counting identities,
no Beurling/O content); "natural boundary" ∧ Dirichlet ∧ primes (2: Bhowmik–Schlage-Puchta on disk, one unrelated); "prime zeta
function" (17: none treats Σ_{p∈R}p^{−s} for thin R relative to an error exponent). Null searches are not evidence of novelty (zoo V.5).
Knopfmacher–Zhang's book on additive arithmetic semigroups (where an example with Z(y) = (1 − ay)/(1 − qy) would naturally live) was
not available — [not checked].

## §4. FIX-FIRST pairs (OLD quoted at NOTE hash 37622108…, line numbers as there)

**Total: 31 pairs — 14 FIX-FIRST pairs in 5 items (F1–F5) and 17 minor pairs (m1–m16, m15 in two parts).**

**F1 — T2 for k = 2: the disjointness claim is false; sq is covered under RH (or a recalled large-gap bound), not "uncond."** (§1(g))
F1a OLD (l. 153): prime p ≥ p₀ let r_p be a prime in [p^k, p^k + p^{kθ′}] (it exists by Ingham; the intervals are disjoint for p ≥ p₀). Put R_k := {r_p}.
F1a NEW: prime p ≥ p₀ let r_p be a prime in [p^k, p^k + p^{kθ′}], with p ↦ r_p injective (r_p exists by Ingham; for k ≥ 3 the intervals are disjoint for p ≥ p₀, as (p′)^k − p^k ≥ 2kp^{k−1} > p^{kθ′} ⟺ θ′ < 1 − 1/k; for k = 2 they overlap whenever p′ − p < p^{1/4}/3, and an injective choice is made greedily — the interval holds ≫ p^{kθ′}/log p primes by Ingham's asymptotic while ≪ p^{kθ′−k+1} earlier intervals meet it). Put R_k := {r_p}.
F1b OLD (l. 160): π_R(x) = π(x^{1/k}) + O(1) gives α_R = 1/k.
F1b NEW: π_R(x) = π(x^{1/k}) + O(x^{σ_C}) (O(1) for k ≥ 3) gives α_R = 1/k.
F1c OLD (l. 258): | sq = {nextprime(p²)} (T2: β₂ ≥ ¼ uncond.) |
F1c NEW: | sq = {nextprime(p²)} (T2: β₂ ≥ ¼ under RH, or unconditionally given a large-gap bound of exponent < 3/4; injectivity of p ↦ nextprime(p²) is open) |
F1d OLD (l. 276): β₂ ≥ ¼ is Theorem T2.
F1d NEW: β₂ ≥ ¼ is Theorem T2 once the collisions nextprime(p²) = nextprime(p′²) are shown sparse (exponent < ¼): under RH by Selberg's Σ_{d_n ≥ H} d_n ≪ x log²x/H, or by a large-gap bound of exponent < 3/4 (Peck, Matomäki) [recalled]; none occurs for p ≤ 10⁶ (read-O).
F1e OLD (l. 289): (δ ≈ 0.16) — both sets on which β₂ ≥ α_R/2 is an UNCONDITIONAL theorem (T2; fr Thm C).
F1e NEW: (δ ≈ 0.16) — sets on which β₂ ≥ α_R/2 is a theorem (greedy: fr Thm C, unconditional; sq: T2 under RH or with a recalled large-gap bound).
F1f OLD (l. 357): (sq, slope 0.422 on [10⁶, 10¹⁰]; greedy c = 1) lies on a set where O is an unconditional theorem (§4.3(e)).
F1f NEW: (sq, slope 0.422 on [10⁶, 10¹⁰]; greedy c = 1) lies on a set where O is a theorem (§4.3(e); for sq under RH or a recalled large-gap bound).

**F2 — T5: the distinctness justification is false (the spacing is below every proved gap bound); fix by a greedy definition.** (§1(j))
F2 OLD (ll. 197–198): R_spr = {nextprime(4^N + j⌊4^N/c_N⌋) : 0 ≤ j < c_N} (distinct for large N: 4^N/c_N ≈ N2^N exceeds the Ingham gap 4^{(5/8+ε)N}).
F2 NEW: R_spr = {r_{N,j} : 0 ≤ j < c_N}, r_{N,j} := the least prime ≥ 4^N + j⌊4^N/c_N⌋ not already chosen (the spacing 4^N/c_N ≈ N2^N lies BELOW every proved gap bound 4^{θN}, θ ≥ 0.525, so nextprime alone need not be injective; with the greedy rule |r_{N,j} − 4^N(1 + j/c_N)| ≤ 4^{(5/8+ε)N} + c_N for large N, since by Ingham's asymptotic any window of length L ≥ 4^{(5/8+ε)N} holds ≫ L/log 4^N primes while at most L/(N2^N) + 1 targets compete for them; on the computed range N ≤ 16 the two definitions coincide — the unit's code aborts on duplicates).

**F3 — Corollary 2.2 and the close: the path must stay in {σ ≥ Re s₀}.** (§1(e))
F3a OLD (ll. 129–130): β₂(R) ≥ Re s₀ for every point s₀ at which P_R (continued from σ > α_R along some path) has a singularity
F3a NEW: β₂(R) ≥ Re s₀ for every point s₀ at which P_R (continued from σ > α_R along some path lying in the closed half-plane {σ ≥ Re s₀}) has a singularity
F3b OLD (l. 338): every other singularity at Re s₀ forces β₂ ≥ Re s₀ (Cor. 2.2).
F3b NEW: every other singularity at Re s₀, reached along a path in {σ ≥ Re s₀}, forces β₂ ≥ Re s₀ (Cor. 2.2).

**F4 — the tight ℚ-necklace obeys O UNCONDITIONALLY (β = α_R; β₂ ≥ α_R/2): the close's "(T, RH) … in particular for the tight
ℚ-necklace" is upgraded, and Theorem F is left with no example on record that needs RH.** (§1(k), proof §7 A1)
F4a OLD (ll. 28–30): (3) *Over ℚ, RH.* Theorem F (Theorem Z with a model divided out) proves O for every R whose D_R-zeros are carried by a polynomially controlled model, including the tight ℚ-necklace — the exact transplant of the rung-1 counterexample, whose realization factor carries the prime diagonal.
F4a NEW: (3) *Over ℚ, RH.* Theorem F (Theorem Z with a model divided out) proves O for every R whose D_R-zeros are carried by a polynomially controlled model; its example, the tight ℚ-necklace — the exact transplant of the rung-1 counterexample, whose realization factor carries the prime diagonal — obeys O even unconditionally, in sup form with β = α_R (cluster lemma + Selberg's sieve, read-O §7 A1).
F4b OLD (l. 241): computed range — as long as the clusters stay this tight (h_N ≪ c_N log 4^N), sup|E| ≥ x^{α_R}/(C log x) infinitely often.
F4b NEW: computed range — and unconditionally: with Selberg's upper-bound sieve in place of Legendre (error Q_R(ξ)² ≪ ξ^{1+ε}, main term hρ_z(1 + O(ξ^{−1/2+ε})), ξ = h^{2/3}), Ingham's span h_N ≤ 4^{(5/8+ε)N} gives E(4^N + h_N) − E(4^N) ≤ −c_N + o(c_N), so sup|E| ≥ x^{α_R}/(C log x) infinitely often and β₂ ≥ α_R/2 (read-O §7 A1).
F4c OLD (ll. 342–343): in size and in minimum modulus on circles; in particular for the tight ℚ-necklace, the exact transplant of the rung-1 counterexample.
F4c NEW: in size and in minimum modulus on circles; in particular for the tight ℚ-necklace, the exact transplant of the rung-1 counterexample — for which O (β = α_R, β₂ ≥ α_R/2) also holds unconditionally by Lemma 3.6 with Selberg's sieve (read-O §7 A1).

**F5 — missed prior art on disk: Hilberdink 2012, Theorem A, is the nearest published object to Thm R1 and the ℚ-counterpart of
§1.3(d).** (§3)
F5a OLD (ll. 105–106): *Nearest published object.* The cyclotomic (necklace) identity 1 − au = Π_N(1 − u^N)^{M(a,N)} is classical (Metropolis–Rota; Moreau 1872) [recalled, unverified];
F5a NEW: *Nearest published object.* Hilberdink 2012, Theorem A (Acta Arith. 152; `novel-wave-s37/beurling-fe/sources/p3-22c2-…txt` ll. 102–116): a g-prime system whose N(x) − cx is periodic is ℙ minus FINITELY many primes — over real norms exact regularity forces a finite deletion, and R1 is the function-field failure of exactly that rigidity. The cyclotomic identity 1 − au = Π_N(1 − u^N)^{M(a,N)} is classical (Metropolis–Rota; Moreau 1872) [re-derived in §1.2; stated in the abstract of arXiv math/0311194];
F5b OLD (l. 329): Thm R1 ↔ the cyclotomic identity [recalled] and fr §5.4's virtual curve; difference: a deletion inside
F5b NEW: Thm R1 ↔ Hilberdink 2012 Thm A (over ℚ: N − cx periodic ⟹ finite deletion), the cyclotomic identity and fr §5.4's virtual curve; difference: an INFINITE deletion inside

## §5. Minor pairs

m1 OLD (l. 77): has E(n)/2^{n/2} between −0.16 and 0.46 for n = 6…22 —
m1 NEW: has E(n)/2^{n/2} between −0.16 and 0.46 at n = 6, 8, …, 22 —
m2 OLD (ll. 74–75): has |E(n)|·n^{3/2}/2^{n/2} oscillating between −0.37 and +0.26 for n = 20…60
m2 NEW: has E(n)·n^{3/2}/2^{n/2} (signed) oscillating between −0.38 and +0.29 for n = 20…60 (−0.37 … +0.26 at n = 20, 25, …, 60)
m3 OLD (l. 91): |ζ_P| ≤ C|t| trivially (steps Z1, Z3 — polynomial bounds);
m3 NEW: the polynomial bound that Z3 delivers, here trivially (ζ_P itself has poles at s = 1 + 2πik/log q at every height — harmless, only D_R's bound is used);
m4 OLD (ll. 98–99): the norm is injective on ⟨R⟩; equivalently the log p, p ∈ R, are linearly independent over ℚ).
m4 NEW: the norm is injective on ⟨R⟩; for rational primes the log p, p ∈ R, are moreover linearly independent over ℚ — a strictly stronger property for general g-primes).
m5 OLD (l. 80): **1.3 What rung 1b says about Lemma G and about any proof of O** [proved here; novelty: single-check].
m5 NEW: **1.3 What rung 1b says about Lemma G and about any proof of O** [(a)–(c) proved here; (d) and Statement (G₁) heuristic — statements about the rung-1 dictionary, not theorems over ℚ; novelty: single-check].
m6 OLD (l. 141): |t| ≥ 1 (cO Theorem Z steps Z1, Z3);
m6 NEW: |t| ≥ 1 (cO Prop. 1.3(i)–(ii): for α_R < ½ the product bounds D_R on σ ≥ α_R + δ and ζ_P·χ(s)^{−1}·ζ(1 − s)^{−1} bounds it to the left; no Phragmén–Lindelöf band is needed);
m7 OLD (l. 144): This replaces cO Prop. 1.6(ii)'s "zeros or poles" by "zeros, no poles" (α_R < ½);
m7 NEW: This replaces cO Prop. 1.6(ii)'s "zeros or poles" by "zeros, no poles" (α_R < ½) — the proposition form of cO's remark under (G′), cO l. 159;
m8 OLD (l. 150): the first nontrivial zero ρ₁ = ½ + 14.1347…i is simple and ζ has no zero in {0 < σ < 1, 0 < |t| < 14.13}.
m8 NEW: ζ has no zero in {0 < σ < 1, 0 < |t| < 14.13} (argument principle, read-O `verify-O/logs/o_zeta_checks.log`); simplicity of ρ₁ is not needed (1/ζ(ks) has a pole of order ord_{ρ₁}ζ ≥ 1 at ρ₁/k).
m9 OLD (l. 183): has |π_R − T| ≤ 2 for large x (T's jumps at primes are ≤ 1 and G varies by o(1) between consecutive primes).
m9 NEW: has |π_R − T| ≤ 2 for large x when α < 0.95 (T's jumps at primes are ≤ 1 and, with gaps ≪ x^{0.525}, G varies by o(1) between consecutive primes) and |π_R − T| ≪ 1 + x^{α/2−0.475} for every α < 1 — enough, since only π_R − T = O(x^θ), θ < α/2, is used.
m10 OLD (l. 185): Re s₀ ≥ α/2, a singularity forbidden by Corollary 2.2, then β₂ ≥ Re s₀;
m10 NEW: Re s₀ ≥ α/2, a singularity forbidden by Corollary 2.2 at a point where P(s + 1 − α) is analytic (or a non-logarithmic one anywhere), then β₂ ≥ Re s₀;
m11 OLD (l. 219): z₀ = α_R + 2 + it₀ (|t₀| large) and radius ρ₁ ≤ α_R + 2 − τ₀
m11 NEW: z₀ = σ₂ + it₀, σ₂ := max(α_R + 2, σ₁ + 1) (|t₀| large; then log C(z₀) = O(1) by (F1)), and radius ρ₁ ≤ σ₂ − τ₀
m12 OLD (ll. 348–349): cannot yield Lemma G on 𝒞_self, because there, by definition,
m12 NEW: cannot yield Lemma G on 𝒞_self — true by the definition of 𝒞_self (it records what Theorem F does not cover: a tautology, not an obstruction theorem), because there,
m13 OLD (l. 349): every admissible G leaves log(D_R/G) with a convergent diagonal;
m13 NEW: every admissible G leaves log(D_R/G) with a diagonal of sub-polynomial growth at some σ < α_R/2 (the negation of (F3));
m14 OLD (l. 300): many zeros on σ = 1 − a/log t — RH-type failure with regular integers in the CONTINUOUS-density world.
m14 NEW: many zeros on σ = 1 − a/log t — RH-type failure with regular integers for a discrete system of REAL g-primes (not a subset of ℙ).
m15a OLD (l. 351): **Smallest class where the answer is unknown: 𝒞_self over ℚ.**
m15a NEW: **Residual class (minimality not shown): 𝒞_self over ℚ — sharpened by requiring D_R analytic on the whole half-plane σ > τ₀ (Prop. 2.3(a)), which removes the sets settled by Cor. 2.2 near the real axis.**
m15b OLD (l. 31): 𝒞_self over ℚ is the smallest class where the answer is unknown, with no member known.
m15b NEW: 𝒞_self over ℚ is the residual class (minimality not shown), with no member known.
m16 OLD (l. 240): the measured max|E| next to the cluster is 1.9c_N (7781).
m16 NEW: |E| at the cluster's right end is 1.20c_N and keeps rising beyond it (1.81c_N within 6h_N in read-O's grid; 1.9c_N (7781) on the unit's window).

## §6. Novelty per result

- Lemma 1.1 (dilation recursion): a third ROUTE to a printed identity (fr Prop. 5.1 = cO Prop. 1.1(a)) — route new, result not.
- Thm R1 (necklace deletion, E ≡ 0 in F_q[T]): **new as a statement on a printed core** — the identity is classical (stated at the
  page in arXiv math/0311194's abstract); the ℚ-side rigidity is Hilberdink 2012 Thm A (F5). Not found in print as a deletion /
  Conjecture-O counterexample (searches null; Knopfmacher–Zhang's book unchecked — §8).
- §1.3 (G₁): heuristic framing (m5); new as a diagnosis, not a theorem.
- Thm 2.1 / Cor 2.2: **new as statements on a printed core** — the Möbius inversion P = Σμ(m)m^{−1}log ζ(ms) (Landau–Walfisz,
  [recalled]) and cO Prop. 1.6(i); the κ-integrality list and its use as a criterion relative to β₂ are the new part; the mechanism
  appears in print in special cases (fr Thm C's (s − α)^c; Estermann's accumulation argument, Bhowmik–Schlage-Puchta ll. 41–50).
- Prop. 2.3: not new beyond cO (G′) (m7).
- T2, T3, T5: new as statements (single-check), elementary given 2.2 (T2: Estermann-type finite product transplanted onto primes;
  T3: P_R ⊃ ζ(ks); T5: non-integer κ = Φ(½)). T4: new as a statement; the device (dense planted poles ⟹ natural boundary) is classical.
- Theorem F: new as a statement on a printed core (Hilberdink 2005 Thm 1 / Carlson, through cO Theorem Z). Cor. F.1: superseded
  unconditionally by A1.
- 𝒞_self and the obstruction sentence: definitional (m12, m15).

## §7. Additions (single-check)

**A1 (Theorem; unconditional). For R_tight: max(|E(4^N)|, |E(4^N + h_N)|) ≥ c_N/3 for all large N; hence β(R_tight) = α_R = ½
and β₂(R_tight) ≥ ¼ = α_R/2.** *Proof.* Let I = (4^N, 4^N + h_N], the span of the N-th cluster; by Ingham's asymptotic h_N ≤
4^{(5/8+ε)N}, and the only R-primes ≤ 4^N + h_N are the earlier clusters (all < 4^N) and the c_N cluster primes in I. An n ∈ I
divisible by a cluster prime r is r itself (2r > 4^N + h_N), so #{R-free n ∈ I} = S(I, P) − c_N, P := Π_{r∈R, r<4^N} r. Selberg's
upper-bound sieve (density 1/d, |r_d| ≤ 1, |λ_d| ≤ 1): S(I, P) ≤ h/G(ξ) + (#{d < ξ : d | P})², G(ξ) = Σ_{d<ξ, d|P}μ²(d)/φ(d) =
1/ρ_P − T(ξ), with ρ_P := Π_{r|P}(1 − 1/r), T(ξ) ≤ ρ^{−1}Σ_{d∈⟨R⟩, d≥ξ}1/d ≪ ξ^{−1/2+ε} and #{d < ξ : d | P} ≤ Q_R(ξ) ≪ ξ^{1/2+ε}
(⟨R⟩ has counting exponent α_R = ½). With ξ = h^{2/3}: S(I, P) ≤ hρ_P + O(h^{2/3+2ε}). Hence E(4^N + h) − E(4^N) = S − c_N − ρh ≤
−c_N + (ρ_P − ρ)h + O(h^{2/3+2ε}); here (ρ_P − ρ)h ≤ hΣ_{N′≥N}c_{N′}4^{−N′} ≪ 2^{(1/4+2ε)N}/N and h^{2/3+2ε} ≪ 2^{(5/6+5ε)N}, both
o(c_N) = o(2^N/N). So one endpoint has |E| ≥ c_N/3 ≍ x^{1/2}/log x (x = 4^N): β ≥ ½ = α_R ≥ β. Mean square: E has slope −ρ and unit
jumps, so |E| ≥ c_N/5 on an interval of length c_N/12 inside [4^N, 2·4^N]; thus ∫_{4^N}^{2·4^N}E² ≫ c_N³ and
∫_1^∞E²x^{−2σ−1}dx ≥ Σ_N c_N³4^{−N(2σ+1)} = ∞ for σ < ¼. ∎ *Computed* (§1(k)): the exact interval-sieve deviation is −0.36c_N (so
the true jump, −1.36c_N, is even larger than the bound needs), h_N^{2/3} < c_N already at N = 16.
**A2 (general cluster criterion; unconditional).** For any deletion R with α = α_R < 1, any y and 1 ≤ h ≤ y, with c := #R ∩ (y, y + h]:
E(y + h) − E(y) ≤ −c + (ρ_y − ρ)h + O_{R,ε}(h^{2α/(1+α)+ε}), ρ_y := Π_{r∈R, r≤y}(1 − 1/r) (same proof; ξ = h^{1/(1+α)} balances
hξ^{α−1} against Q_R(ξ)² ≪ ξ^{2α+ε}). *Corollary (counterexamples are anti-clustered):* if β(R) < α_R/2 then for every δ > 0, all
large y and all h ≤ y: #R ∩ (y, y + h] ≤ 2(2y)^{α/2+δ} + C h y^{α−1+δ} + C h^{2α/(1+α)+δ} (ρ_y − ρ ≪ y^{α−1+δ}). This is a
quantitative, unconditional form of cO Prop. 1.6(iii)'s "irregular at scale x^{α_R/2}" — on the opposite side: a counterexample
must AVOID dense clusters — and it settles every cluster construction with c ≫ h^{2α/(1+α)+δ} directly, without RH or Theorem F.
**A3 (sharper residual class).** 𝒞′_self := {R ∈ 𝒞_self : D_R analytic on the whole half-plane σ > τ₀}. Under RH with α_R < ½ every
counterexample lies in 𝒞′_self (Prop. 2.3(a) gives analyticity on σ > β₂, not only for |t| > T₀); 𝒞′_self excludes the sets
settled by a forbidden singularity of P_R near the real axis (Cor. 2.2), which 𝒞_self as defined does not.
**A4 (T2 needs no simplicity; sq under RH).** T2's pole argument uses only ord_{ρ₁}ζ ≥ 1; and under RH the collisions of
p ↦ nextprime(p²) number ≪ log²X up to X (Selberg's large-gap bound [recalled]), so T2 covers sq under RH.

## §8. What I could not check, and why

- Ingham 1937, Huxley 1972, BHP 2001 originals: not on disk; read only through Wikipedia (secondary). The large-gap bounds used in
  F1/A4 (Selberg under RH; Peck; Matomäki) are [recalled, unverified]; they affect only whether sq is covered unconditionally.
- Knopfmacher–Zhang, *Number Theory Arising from Finite Fields* (the natural home of an additive-semigroup example with
  Z(y) = (1 − ay)/(1 − qy)): not available; R1's novelty label remains single-check.
- Not re-run: nsq (T3 Bessel fit), the two Weyl families, the planted-pole control, the T_α / greedy controls (only sq and the
  tight necklace were re-run, plus rung 1, the ζ inputs and the cluster data). Lemma 1.1's computations (cO's rung 1a) not re-run.
- Heuristic laws (T3's Bessel law, T5's (log X)^{−3.66} law, the O(x^{0.03}) remainder of the sq explicit formula) were not
  re-derived beyond checking their Selberg–Delange / Perron shape; the explicit-formula agreement itself was reproduced.
