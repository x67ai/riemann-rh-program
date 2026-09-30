# REFEREE REPORT: "A counterexample to Haglund's monotonic-zeros conjecture for the Riemann Ξ approximants"

Blind referee, 2026-10-01. Object: `main.pdf` (16 pp.) / `main.tex` as of 2026-10-01 00:51. Brief: `REFEREE-BRIEF.md`.
Built incrementally; sections land in order §1 (first read, before any source was opened), §2 (brief items 1-8), §3, §4, then §0.

## §0 Verdict

**MINOR REVISION for posting — with one MAJOR, non-mathematical item (O1) that must be settled before the paper goes out.**

Summary for the author. The result stands. I re-derived every proof in §§2-4 and §6 by hand and found no wrong step and no
missing hypothesis that the text does not already supply elsewhere; every number in Tables 1-3, §6 and §7 agrees with both
certificates, and the checkable ones agree with my own 60-digit recomputation; both CERT hashes and the zip hash are right;
every quotation and all 17 references check out at the page, and Riemann's 1859 page range 671-680 is now confirmed on a
scan of the Monatsberichte itself. Your factor-4 remark on Haglund's (51)-(52) is right (CONFIRM, item 5). What must change:
(O1) the Data-availability sentence saying the fetched literature is not redistributed is false for the public repository,
which holds publisher PDFs in the very folders the paper cites; either those files leave the repository or the sentence goes,
and that is the sponsor's decision. (F3.1) The five "limits" printed after Prop. 3.4 are values of t²Ξ_N(t) at t = 8000, not
the limits; three are wrong in the fourth digit; exact values are given. The rest is presentation: a strict inequality Thm 3.1
should state because Cor. 3.2 uses it (F3.2); Burnol's hypotheses should be stated, and the Knopp sentence made harmless
(F3.4); the failing-lobe mechanism should be called a heuristic (F4.1); certificate A's N = 24 squares need the symmetry
sentence (F2.1); and about twenty small wording, notation and table fixes, each given below as an OLD/NEW pair. Add a commit
pin and name the zip's home before posting (§3.3).

## §1 First-read findings (written after reading main.pdf cover to cover, before opening any source file)

Method: read pp. 1-16 as an outside analytic-number-theory referee; re-derived by hand every displayed identity of §§1-4 and
§6.1-6.2 (formula (2) from the integral, (3) from Riemann's kernel, Lemma 2.1 line by line, the kernel derivatives in Thm 3.3,
the 1/t² limits of Prop 3.4, the u → −∞ coefficients in Thm 4.1, the proof of Thm 4.2, Lemmas 6.1-6.3, the Euler-Maclaurin
and incomplete-gamma remainders, the Taylor-model error E, and the inequalities of §6.4). The mathematics holds up. What follows
are the defects found on that first read; places are page/section here and get `main.tex` line numbers in §2.

R1 (MINOR, abstract; §1.4(i)). "the number of real zeros of Ξ_N is odd": Ξ_N is even, so its real zeros on R are symmetric
and (0 not being a zero) even in number. The body is right ("on (0,∞), counted with multiplicity", Cor. 3.5); the abstract must
say "positive real zeros, counted with multiplicity".

R2 (MINOR, §1.5). "no member of the family ξ_w with 0 ≤ w_n ≤ 1 and w ≢ 1, or with w finitely supported, has all its zeros on
the critical line" is false for w ≡ 0: ξ_0 = 1/2 has no zeros, so all of them are (vacuously) on the line. Thm 4.1 correctly
assumes w ≢ 0; §1.5 must too.

R3 (TYPO, §2, (4)). "valid for all s ∈ C": both sides have poles at s = 0, 1. Say "as an identity of meromorphic functions".

R4 (MINOR, §2, (5)). ξ_w is defined for arbitrary w: N → R; the series converges only under a growth condition (polynomial
bounds suffice and are all the paper uses). State it at (5).

R5 (MINOR, Thm 3.1 vs Cor 3.2). Thm 3.1 states only "P_w ≥ 0, with equality for all t only if w ≡ 1", but the proof of
Cor 3.2 needs P_w(t) > 0 at every t when w ≢ 1 ("at the ends of a lobe ξ_w = P_w > 0"). The proof of 3.1 gives the strict
pointwise inequality (g_n > 0 and 1 − w_m > 0 for some m); the statement should say it.

R6 (MINOR, §1.4 and Cor 3.5). "0 < γ_1 < γ_2 < ... the positive zeros of Ξ" should read "positive real zeros": the corollary
is unconditional, and without RH Ξ could have non-real zeros too.

R7 (MINOR, proof of Thm 4.2). "δ ... decays super-exponentially at 0 and at ∞": at ∞, δ(x) = Σ(w_n − 1)e^{−πn²x} decays only
exponentially. What is needed (and true) is decay faster than every power of x at both ends (at 0 through δ(x) = x^{−1/2}δ(1/x)).

R8 (MINOR, pending the source check in §2 item 3/6, paragraph after Thm 4.2). "Burnol's extension needs convergence only for
Re s large. Some such hypothesis is needed: with absolute convergence only in some half-plane, Knopp exhibits infinitely many
linearly independent solutions" reads as self-contradictory: the reader cannot tell which further hypothesis of Burnol's
Corollaire 2 excludes Knopp's examples, nor check that it holds here. State Burnol's hypotheses and verify each. A
self-contained alternative (referee's, checked): μ := Σ_{n≥1}(w_n − 1)(δ_n + δ_{−n}) is an even tempered measure;
δ(1/x) = √x δ(x) says μ and μ̂ agree on every Gaussian e^{−πxt²}, whose span is dense in the even Schwartz functions (Hermite
functions), so μ̂ = μ; μ̂ is 1-periodic while supp μ ⊂ Z∖{0}, so μ = 0 and w ≡ 1. This needs only polynomially bounded w.

R9 (MINOR, paragraph after Prop 4.3). The application to F_N = ξ_N is heuristic ("≈", "below the size of ξ on the line up to
T ≈ 4(N+1)²") and "(ii) holds for all large N" is only sketched; label it a remark, or prove it. "Theorem 3.1: real zeros are
never lost as N grows" is imprecise: Thm 3.1 gives that {t : ξ_N(1/2+it) < 0} increases with N, so a lobe that carries real
zeros of ξ_N carries real zeros of every ξ_M, M > N; the count itself can drop (two negative dips in one lobe can merge).

R10 (MINOR, §1.4, §5). "a lobe that stays below the level, followed by a lobe that rises above it, leaves a pair of non-real
zeros below real zeros" is stated as a fact; nothing in §§3-4 proves it (the violation is proved by computation). Qualify
("in every case computed", "typically").

R11 (MINOR, §6.1). "near z_0 all these terms are about 10^{−1066} or smaller (Φ_28 ≈ Ξ ≈ 1.49·10^{−1066}, ...)": §6.2 gives
|Ξ| = 1.4923...·10^{−1066} and |Φ_28| = 1.4925...·10^{−1066} at x = 3144.8946, 1.67 away from z_0. Say which point.

R12 (TYPO, Lemma 6.3 proof). "For n ≥ 1, U_{n+1}/U_n ≤ ...": U_n has a positive denominator only for n ≥ M+1; say "for n > M".
Also one clause is missing: Lemma 6.1 is applied with Y/2 ≥ |Im(z/2)|, which needs Γ(β,a)/a^β = ∫_1^∞ x^{β−1}e^{−ax}dx to be
increasing in β (it is).

R13 (MINOR, §6.2). "every truncation adds a disk whose radius is a proved bound, each targeting 2^{−190}": the values are
~10^{−1066}, so an absolute 2^{−190} would be useless; say "relative to the size of the leading term" (or whatever is meant).

R14 (MINOR, §6.2, Taylor model). E is defined for |z − c| ≤ r' with x = r'/R, but the text quotes E "for r ≤ 10^{−5}" and
"at r = 10^{−3}" where r is the half-width of a square. Recomputed: x = r/R gives E = 2.1·10^{−1089} at r = 10^{−3}; the printed
1.36·10^{−1087} is x = √2·r/R (the circumscribed disc). Say r' = √2 r.

R15 (MINOR, §7). Certificate A's squares are in the s-plane about 0.8159896243 + 2508.2839748053 i = ρ_24, which is the
z-plane square about 2508.2839748053 − 0.3159896243 i, the complex conjugate of the square in Thm 7.1(b). The transfer uses
ξ_w(1/2 + i z̄) = conj ξ_w(1/2 + iz); say so, since "Both certificates prove this" otherwise overstates A.

R16 (TYPO, Tables 2-3). Table 2, row "B, z*": empty "boundary pieces" cell (fill in or "n/a"). Table 3: the first and third
columns are fully justified in narrow p-columns, leaving large gaps ("Ξ_1 at 14.04543957 and"); use \raggedright.

R17 (MINOR, §6.3 cross-checks). "|L − T| ≤ 1.18·10^{−1288} at 1024 bits at the fourteen contour points": of the 18 points,
14 are not Table 1 points, but only 12 of those lie on contours (the center and the reference zero do not). Check the source.

R18 (MINOR, Provenance). The zip's host is not named (arXiv ancillary files? Zenodo?); no commit or tag of the repository is
pinned; the internal labels in the paths (s36, s37, producer-A, rerun-F, verify-F) are opaque to a reader. Name the host, pin
a tag or commit, and add a one-line glossary.

R19 (MINOR, Thm 1.1(b), abstract). The 10^{−48} enclosure is certified by B only (Table 2, row z*); the abstract's "certified
twice" is about the two facts, which is right, but Thm 1.1(b)/§6.4(b) should say "(certificate B)" for the 10^{−48} square.

R20 (TYPO, Thm 1.1(b)). The notation w + [−r, r]² is used in Thm 1.1 but defined only in §6.3.

R21 (MINOR, §6.2). "integration by parts where it converges": the expansion h(w) = e^{−X}Σ_{k<K}τ_k + ρ_K is finite with a
remainder bound (asymptotic, not convergent); say "where the remainder bound ρ_K is small enough".

R22 (MINOR, §1.3). "Nor does the paper decide Conjecture 1 for N ≤ 26": it decides nothing for N ≥ 28 either (scan windows
only, N ≤ 30). Say "for any N other than 27".

R23 (MINOR, Prop 3.4). "Since the full kernel Σφ̃_n is even" is used without source or proof. One line suffices, from the
paper's own Thm 4.2 computation: K(u) = e^{u/2}ψ(e^{2u}) satisfies K(u) − K(−u) = −sinh(u/2) (Jacobi), so K'' − K/4 is even.

R24 (TYPO, abstract). "a shallow lobe followed by a deeper one": the lobes are positive; "a low lobe followed by a higher one".

R25 (TYPO, §5). "for N = 6, ..., 29 (and N = 30)": say why N = 30 is separate, or write N = 6, ..., 30.

R26 (TYPO, §6.1). Route T "uses Riemann's series Ξ = Σ Φ_n [Hag09, (12), p. 3]": the paper proves it itself (Lemma 2.1 with
(4)); cite Lemma 2.1 as well.

Items to settle against the sources (§2): the factor 4 in Haglund's (52); every quotation; Ki's and LMOZ's statements;
Burnol's Corollaire 2; the Riemann 1859 pages; the arXiv 1920-character abstract limit (abstract.txt is 1939 bytes);
the author name on p. 1 against the writer's brief; the public repository URL.

## §2 Findings by brief item (sources opened only after §1 was on disk)

Update to §1: R11 is WITHDRAWN. Recomputed with mpmath (60 digits): |Φ_28(z*)| = |Ξ(z*)| = 1.4929509e−1066 and
|Φ_29(z*)| = 2.83e−1144, so "near z_0 ... Φ_28 ≈ Ξ ≈ 1.49·10^{−1066}, Φ_29 ≈ 3·10^{−1144}" (l. 706-708) is right, as
producer A's CERT §2 says; B's figures at x = 3144.8946 (l. 795-796) are also right (recomputed 1.4923145e−1066, 1.49249e−1066).

### Item 1 — Theorem 1.1 and §6 against producer-A/CERT.md, producer-B/CERT.md, haglund-cert-s37/NOTE.md

Every number in Tables 1-3 and §6.1-6.2 was matched to the CERTs digit by digit (list in §4), and the checkable ones were
recomputed independently. Findings:

F1.1 (MINOR, §6.3 Cross-checks, l. 927-931). Two slips. (a) "the squares of half-width 10^{−3}": there is one square.
(b) "at the fourteen contour points": A's CERT §6 table has 14 non-Table-1 points, of which 12 lie on contours; the other two
are the center c and the reference zero z0*. OLD: `the corners and midpoints of
the squares of half-width $10^{-3}$` NEW: `the corners and midpoints of
the square of half-width $10^{-3}$`; OLD: `at $1024$ bits at the fourteen contour points.` NEW: `at $1024$ bits at the
fourteen points other than those of Table~\ref{tab:real}.`

F1.2 (MINOR, §6.2 Taylor model, l. 810-821). The quoted E values use r' = |w − c| + √2 r for a square of half-width r about w
(B's CERT B7: "r' ≥ |sc − c| + √2 r"); the text never relates r' to r. Recomputed: x = r/R would give E = 2.11·10^{−1089} at
r = 10^{−3}; x = √2 r/R gives 1.358·10^{−1087} as printed. OLD: `giving $E = 3.51\cdot10^{-1106}$ for $r \le 10^{-5}$ and`
NEW: `giving, with $r' = \sqrt2\,r$ for a square of half-width $r$ about $c$, $E = 3.51\cdot10^{-1106}$ for $r \le 10^{-5}$ and`

F1.3 (MINOR, §6.2, l. 769-770). "each targeting 2^{−190}": per B's CERT B2-B3 the target is absolute for ζ (of size ~1) and
relative to e^{−X} for h; an absolute 2^{−190} would be useless at 10^{−1066}. OLD: `each
targeting $2^{-190}$ at a working precision of $200$ bits.` NEW: `each
targeting $2^{-190}$ relative to the size of the truncated quantity ($|\zeta| \approx 1$, and $e^{-X}$ for $h$), at a
working precision of $200$ bits.`

F1.4 (TYPO, Lemma 6.3 proof, l. 743-746). OLD: `give $|\Phi_n| \le U_n$. For $n \ge 1$,` NEW: `give $|\Phi_n| \le U_n$
(since $\Gamma(\beta,a)/a^\beta = \int_1^\infty x^{\beta-1}e^{-ax}\,dx$ increases with $\beta$, $|\im(z/2)|$ may be replaced
by $Y/2$). For $n > M$,` (A's CERT §3.3 has the same "For n ≥ 1".) Recomputed 2U_32 = 1.948·10^{−1393} ≤ 2·10^{−1393}: right.

F1.5 (TYPO, Tables 2-3, l. 883, 900). Row "B, z*" has an empty boundary-pieces cell; B's CERT §D (H2*) gives no count: put
"--" (or the count from `logs/cert27.log`). Table 3 is set in justified p-columns and prints with large gaps: OLD
`\begin{tabular}{p{0.30\textwidth}p{0.30\textwidth}p{0.30\textwidth}}` NEW
`\begin{tabular}{>{\raggedright\arraybackslash}p{0.30\textwidth}>{\raggedright\arraybackslash}p{0.30\textwidth}>{\raggedright\arraybackslash}p{0.30\textwidth}}` (`array` is already loaded, l. 8).

F1.6 (MINOR, Thm 1.1(b) l. ~140 and §6.4(b) l. 958-961). The 10^{−48} square is certified by B alone (B's CERT H2*; A stops
at 4·10^{−11}). OLD: `$1$ there locates the same zero $z_0$.` NEW: `$1$ there (certificate B) locates the same zero $z_0$.`

F1.7 (MINOR, §6.3, l. 939-940). "... and Haglund's two ladder zeros": no archived log backs this for the third evaluation
(`verify-F/rerun_N27.log` has only the N = 27 points; `haglund_direct_arb.py` prints the ladder only when run as a script).
I ran it (scratch copy, 300 bits): Ξ_1(14.04543957) = +1.34706045614673e−11, Ξ_1(14.04543959) = −1.70410212531455e−11,
Ξ_2 at 39.5324810797/…799 = +3.605517254e−21 / −4.593418771e−21. The claim is TRUE; archive that output as
`verify-F/haglund_direct_arb.log` (and add it to SHA256SUMS and the zip), or drop the four words.

F1.8 (TYPO, §6.2, l. 801). "integration by parts where it converges": the expansion is finite with a remainder bound ρ_K.
OLD: `integration by parts where it converges,` NEW: `integration by parts where its remainder bound is small,`

### Item 2 — Theorem 7.1 against A's CERT §8 and B's CERT "H5"

All four enclosures on the line (A: ±5, 3, 4, 4·10^{−866/867}; B's 16-digit values), the squares (A: s-plane, r = 10^{−3}
(151 pieces), 10^{−10} (174); B: z-plane, r = 10^{−3}, 10^{−6}, 10^{−9}, 10^{−10}), the controls, M_R = 4.07·10^{−849},
1.16·10^{−852}, E = 2.6·10^{−871} (recomputed 2.64·10^{−871}), and ρ_24 (B's model zero 0.184010375695657531105913643468 +
2508.28397480532415320152284309 i is the mirror; 1 − 0.18401... = 0.8159896243043424688941 as printed) all match.

F2.1 (MINOR, §7, l. 992 ff.). A's squares are centered at 0.8159896243 + 2508.2839748053 i in the s-plane, i.e. at ρ_24,
whose z-image is 2508.2839748053 − 0.3159896243 i: the conjugate of the Thm 7.1(b) square. A proves (b) only through
ξ_w(1/2 + i z̄) = conj ξ_w(1/2 + iz). OLD: `Certificate A finds winding` NEW: `Certificate A finds (in the $s$-plane; the
symmetry $\xi_{24}(\tfrac12 + i\bar z) = \overline{\xi_{24}(\tfrac12 + iz)}$ carries its squares to those of (b)) winding`

(Place of F2.1: main.tex l. 1009-1010, "Certificate A finds / winding number 1 along the s-plane squares".)

### Item 3 — §§2-4 against staircase NOTE §1-§2 as corrected by read-F F1-F5

Map checked: Lemma 2.1 ↔ PRIOR-ART §0 (relation and c_N; the printed recurrence proof re-derived line by line, correct:
h(a+1) = (a h(a) + e^{−X})/X, 2X²h(a+2) − 3Xh(a+1) = (2a² − a)h(a) + (2a − 1 + 2X)e^{−X}, 2a² − a = ½s(s−1) at a = s/2 and
(1−s)/2, 2a − 1 summing to 4X − 1; Σ(4πn² − 1)e^{−πn²} = ½ recomputed to 60 digits). Thm 3.1 ↔ D; Cor 3.2 ↔ D1 (counts 2, 6, 16,
32, 52, 80); Thm 3.3 ↔ D′ with F1 applied (+0.291, +0.0395; recomputed 0.290944, 0.0394988); Prop 3.4 ↔ D′(2); Cor 3.5 ↔ D′(1)
with F5 applied (Ξ(0) = 0.497120778 recomputed); Thm 4.1 ↔ A with F2; Thm 4.2 ↔ B; Prop 4.3 ↔ F with F3 for (ii). All faithful.
Brief's Thm 4.1 note: CONFIRMED. From φ̃_n = (4y² − 6y)e^{u/2}Σ_k(−y)^k/k!, the coefficient of y^{k+1}e^{u/2} is −2(2k+3)(−1)^k/k!,
so Φ_w = Σ w_n φ̃_n has coefficient −2π(2k+3)(−π)^k/k!·Σ w_n n^{2k+2} of e^{(5/2+2k)u}: twice the NOTE's (whose φ_n = φ̃_n/2).

F3.1 (MINOR, after Prop 3.4, l. 465-468; same slip in NOTE D′(2)). The five numbers are not the limits: they are t²Ξ_N(t) at
t = 8000 (`verify/haglund_coeff.log`, last column). The limits, from the closed form −2Σ_{n>N}(8X³ − 30X² + 15X)e^{−X} at
50 digits (and equal to +2Σ_{n≤N}(...) as the evenness requires; Σ_{all n} = −9e−51): −0.078997531, −1.6530559·10^{−7},
−2.7834517·10^{−16}, −5.7394724·10^{−28}, −1.707458·10^{−42}. The printed N = 3, 4, 5 values are wrong in the 4th digit and
the N = 2 value misrounds. OLD: `Evaluated at $40$ digits the
limits are $-0.078997$,
$-1.6530\cdot10^{-7}$, $-2.7831\cdot10^{-16}$, $-5.7375\cdot10^{-28}$ and
$-1.7062\cdot10^{-42}$ for $N = 1, \ldots, 5$.` NEW: `The limits are $-0.0789975$,
$-1.65306\cdot10^{-7}$, $-2.78345\cdot10^{-16}$, $-5.73947\cdot10^{-28}$ and
$-1.70746\cdot10^{-42}$ for $N = 1, \ldots, 5$ (at $t = 8000$, $t^2\Xi_N(t)$ agrees with them to a relative $10^{-3}$).` (Relative gaps
in the log: 1.3·10^{−4}, 3.5·10^{−4}, 7.5·10^{−4} for N = 3, 4, 5.)
(The abstract's and §1.4's claim, "negative for every N", is unaffected.)

F3.2 (MINOR, Thm 3.1, l. 363; same in NOTE D). The statement is weaker than what Cor 3.2's proof uses (P_w > 0 at every t).
OLD: `with equality for all $t$ only if $w \equiv 1$. In particular` NEW: `and $P_w(t) > 0$ for every real $t$ unless
$w \equiv 1$. In particular`

F3.3 (MINOR, proof of Thm 4.2, l. 581; same in NOTE B). OLD: `decays super-exponentially at $0$ and at
$\infty$,` NEW: `decays faster than every power of $x$ at $0$ and at
$\infty$ (exponentially at $\infty$, and like $x^{-1/2}\delta(1/x)$ at $0$),`

F3.4 (MINOR, l. 593-597). Burnol verified at the page (`lit/burnol-1106.4749.txt` l. 102-134, pp. 2-3): Corollaire 2 assumes
(1) meromorphic continuation with finitely many poles, (2) f = O(e^{exp ε|s|}) in vertical strips, (3) g(s) = χ(s)f(1−s) =
O(|s|^N y^{−s}) as Re s → +∞ for some y > ½, (4) g(σ) = c + O(σ^{−k}) for all k; conclusion f = cζ. All four hold here
(f entire; f = π^{s/2}M(s)/Γ(s/2) with M bounded in strips; g = f = (w_1 − 1) + O(2^{−σ}), y = 1), so the proof is sound. But
the paper states none of (1)-(4), and its Knopp sentence (Knopp not read; reported from Nakamura p. 4, whose (K) keeps his (H2)
and (H3)) makes Burnol look contradicted. OLD: `needs convergence only
for $\re s$ large. Some such hypothesis is needed: with absolute convergence only
in \emph{some} half-plane, Knopp exhibits infinitely many linearly independent
solutions of the functional equation (as reported in \cite[p.~4]{Nak}).` NEW: `needs convergence only
for $\re s$ large, together with finitely many poles, $f(s) = O(e^{\exp\epsilon|s|})$ in vertical strips, and, for
$g(s) = \chi(s)f(1-s)$, $g(s) = O(|s|^N y^{-s})$ with $y > \tfrac12$ and $g(\sigma) = c + O(\sigma^{-k})$ for every $k$; here
$g = f = (w_1 - 1) + O(2^{-\sigma})$, so all of these hold. (Hamburger's theorem needs more than the functional equation:
see \cite[p.~4]{Nak} for Knopp's solutions when absolute convergence for $\sigma > 1$ is weakened.)` A self-contained alternative is in §1 R8.

F3.5 (MINOR, l. 613-623). (a) "(Theorem 3.1: real zeros are never lost as N grows)": what Thm 3.1 gives is nesting of the
negative sets (NOTE §4 item 4: "their negative sets increase with N"); zero counts can drop by merging. OLD: `(Theorem~\ref{thm:polya}:
real zeros are never lost as $N$ grows)` NEW: `(Theorem~\ref{thm:polya}: the set where $\xi_N(\tfrac12+it) < 0$ grows with $N$,
so a lobe that carries real zeros keeps carrying them)`. (b) "(ii) holds for all large N" is a one-line sketch of read-F F3,
whose two-regime estimate is correct (re-derived); add its two inequalities or label the paragraph a remark.

F3.6 (TYPO, l. 295). OLD: `valid for all $s \in \Cx$:` NEW: `valid for all $s \in \Cx \setminus \{0, 1\}$:`

F3.7 (MINOR, l. 306). OLD: `For weights $w\colon \N \to \R$ put` NEW: `For weights $w\colon \N \to \R$ with
$|w_n| \le Cn^A$ put` (this is all that Thms 4.1-4.2 use; the series then converges absolutely and locally uniformly).

F3.8 (MINOR, l. 197 and l. 483). OLD (both): `the positive zeros of` NEW: `the positive real zeros of`

F3.9 (MINOR, l. 462). OLD: `Since the full kernel $\sum_{n \ge 1}\tphi_n$ is even,` NEW: `Since the full kernel
$\sum_{n \ge 1}\tphi_n$ is even (with $K(u) = e^{u/2}\psi(e^{2u})$, the theta relation gives $K(u) - K(-u) = -\sinh(u/2)$,
so $K'' - K/4$ is even),`

F3.10 (MINOR, §1.5, l. 236-237). OLD: `$\xi_w = \tfrac12 + \tfrac12 s(s-1)\sum_n w_n g_n$ with $0 \le w_n \le 1$ and
$w \not\equiv 1$,` NEW: `$\xi_w = \tfrac12 + \tfrac12 s(s-1)\sum_n w_n g_n$ with $w \not\equiv 0$ and either $0 \le w_n \le 1$,
$w \not\equiv 1$,` (ξ_0 = ½ has no zeros at all).

### Item 4 — §5 against NOTE §3 (departure lobes, lobe count to 320) and §4.1 (scan)

Every figure matches: the seven departure lobes and depth ratios (NOTE §3 l. 74), "4(N+1)² + 6 to + 10", Re s ≥ 1.39, the
counts 2, 6, 16, 32, 52, 80; the scan windows, tally, N = 21 (0.93) and N = 20 (0.48); the N = 27 lobes (0.411, 1.325), real
zeros 3144.8946622186 and 3145.5998495765, box, "2.0 at 30 and 45 digits", s = 0.8152587993782148453823 + 3143.2206...i; the
N = 24 lobes (0.595, 1.130), Re s = 0.8160. Haglund's largest zeros (14.05 ... 489.39) match his p. 4 table.

F4.1 (MINOR, l. 199-201 and l. 658-660). The failing-lobe mechanism is a heuristic, stated as fact. OLD (l. 658-660): `A lobe that
fails the level, followed by a lobe that passes it,
leaves a pair of non-real zeros over the first lobe with real zeros above it,
which violates the ordering.` NEW: `A lobe that
fails the level, followed by a lobe that passes it, is expected to leave (and in both cases below does leave) a pair of
non-real zeros over the first lobe with real zeros above it,
which violates the ordering.` Same repair in §1.4 (l. 200-201: `leaves a pair` → `is expected to leave a pair`) and in the
abstract (l. 70: `leaves a non-real zero` → `can leave a non-real zero`).

F4.2 (TYPO, l. 664). "for N = 6, ..., 29 (and N = 30)": per NOTE §4.1, N = 30 was scanned afterwards with no violation.
OLD: `for $N = 6, \ldots, 29$ (and $N = 30$), counting` NEW: `for $N = 6, \ldots, 30$, counting`

### Item 5 — the two errata, and the factor-4 remark

Haglund's text on disk: the p. 4 table (l. 199-209) reads 1, 7, 15, 32, 53, 79, 113, 155, 207, 263 with largest real zeros
14.0454395788 ... 489.3900649445, as printed in the paper; (52) and the p. 10 sentence (l. 541-547) are quoted exactly. The
census `verify/census_haglund_N4_T200.json` has n_real = 31, largest 103.367988009413489008, complete = True (Z_total 89 =
31 + 2·29); Cor. 3.5 makes the count with multiplicity odd, so both errata stand.

Factor 4: CONFIRM. Haglund's (50) (l. 526-528), G(x; a, b) = 2(a − b)e^{−a}/x² + O(x^{−4}), is right in G's own argument
(4∫cos(2xu)f(u)du with f = e^{2bu − ae^{2u}} gives −f'(0)/x², f'(0) = 2(b − a)e^{−a}). But (14) evaluates G at x/2, which
multiplies the 1/x² coefficient by 4: the true coefficient of Φ_n is [16π²n⁴(a − 9/4) − 24πn²(a − 5/4)]e^{−a}, a = n²π,
while his (51) prints [4n⁴π²(n²π − 9/4) − 6n²π(n²π − 5/4)]/e^{n²π}, which is (50) applied at x. Numbers: 4 × (52) = −0.07899752824,
+0.07899736484, +1.6530559012·10^{−7}; the closed form 2(8X³ − 30X² + 15X)e^{−X} gives −0.0789975305, +0.0789973652,
+1.6530559·10^{−7} (ratios 4.0000001, 4.00000002); a direct evaluation gives t²Ξ_1(8000) = −0.07899720 (`haglund_coeff.log`).
Suggested sharper wording (l. 471-472): OLD `a constant factor that comes from the
argument $z/2$ in \eqref{eq:XiN} and does not affect signs.` NEW `because his (51) applies his (50) at $x$ although
\eqref{eq:XiN} evaluates $G$ at $x/2$; the factor does not affect signs.`

### Item 6 — quotations at the page

Exact (character for character, modulo typesetting): Haglund l. 144-148 ("We say ... nondecreasing"; the side assumption),
l. 151 (Conjecture 1), l. 153 (Proposition 1), l. 190-191 and 195-196 (Remark 1), l. 143 ("no attempt ..."), l. 546-547;
Platt-Trudgian arXiv abstract ("all zeroes β + iγ ... have β = 1/2"); Baccaro's Zenodo record ("The result covers only the
first interpolation.", title, author Mayk Loide Baccaro, v1.0.0, August 22, 2026, preprint, DOI 10.5281/zenodo.22059236);
Ahn l. 511-514; Lagarias-Montague p. 24 l. 1349-1350 ("involving the ξ-function, where such a monotonicity implies the RH");
LMOZ Theorem 1.7 (l. 110-111); Ki p. 198 l. 66-71 (paraphrase accurate); Nakamura p. 4 Theorem D (H1)-(H3) and Knopp's (K);
Burnol pp. 2-3 (Théorème 1 l. 102-117, Corollaire 2 l. 131-134). Page numbers all right, including [Hag09, p. 16] for the
appendix (text l. 728-732: page 15 ends at l. 728; producer A's CERT l. 103 says p. 15, wrongly; the paper is right).

F6.1 (MINOR, §1.6, l. ~250). Ahn's thesis numbers the conjecture 1.5 (l. 393) but calls it "Conjecture 1.6" in Remark 1.9
(l. 507, 514); the verbatim quote therefore names a conjecture the reader cannot find. Add "[sic]" or "(his Conjecture 1.5)".

F6.2 (MINOR, §1.6). Lagarias-Montague ask whether monotonicity would be sufficient "to imply that the zeros of its derivative
ξ(s) would all lie on the critical line" (p. 24), not for the family's own zeros. OLD (paraphrase) `would be a sufficient
condition for all zeros to be on the line` NEW `would be a sufficient condition for the zeros of its derivative $\xi$ to lie on
the critical line`.

F6.3 (MINOR, §1.6). The Ki result is proved in his Proc. LMS paper and only restated at [Ki06, p. 198] ("the author [6,
Corollary 1] has shown"). Cite it as "[Ki05, Corollary 1], restated in [Ki06, p. 198]", with Ki05 = H. Ki, All but finitely
many nontrivial zeros of the approximations of the Epstein zeta function are simple and on the critical line, Proc. London
Math. Soc. 90 (2005), 321-344 (data as listed in Ki06's reference [6], l. 364-366; not checked against Crossref).

F6.4 (MINOR, Prop 3.4 / F3.9). Haglund p. 2 (l. 53) states "The function φ(t) is known to be an even function of t": citing it
is the shortest repair for the unsupported "the full kernel is even".

(Places: F6.1 is main.tex l. 253-254; F6.2 l. 264, OLD string exact; F6.3 l. 268-272.)

### Item 7 — scope

Satisfied. Abstract l. 74-78 ("refutes a sufficient condition for the Riemann hypothesis and says nothing about the Riemann
hypothesis itself"), §1.3 l. 173-176, and §7 ("it says nothing about the zeros of ζ") say it plainly; Conjecture 1 ⟹ RH is
Haglund's Proposition 1 (l. 153), so "sufficient condition" is exact.
F7.1 (MINOR, §1.3, l. 181-182). OLD: `Nor does the paper decide Conjecture~\ref{conj:H}
for $N \le 26$:` NEW: `Nor does the paper decide Conjecture~\ref{conj:H}
for any $N \ne 27$:` (the scan reached N = 30 and nothing is proved for N ≥ 28 either).

### Item 8 — bibliography, entry by entry

All 17 entries checked; all CORRECT as printed. Sources: Ahn (thesis title page: Surl-Hee (Shirley) Ahn, M.A., Penn, 2012);
Bac26 (Zenodo record: title, M. L. Baccaro, v1.0.0, 22 Aug 2026, DOI); Bur12 (arXiv metadata journal-ref: Expo. Math. 30
(2012) 295-308, DOI 10.1016/j.exmath.2012.03.003; title and subtitle from the text); DLMF (saved pages: "Release date
2026-09-15"; 5.11.1 Stirling, 2.10.1 Euler-Maclaurin, 24.9.2 = (2 − 2^{1−2n})|B_2n| ≥ |B_2n(x) − B_2n|); Edw74 (Haglund's
[Edw01]: Dover 2001, "Reprint of the 1974 original [Academic Press, New York]"); FLINT and mpm (versions as in both CERTs);
Hag09 (arXiv:0910.5228v1, 27 Oct 2009); Hag11 (De Gruyter page "Cent. Eur. J. Math. • 9(2) • 2011 • 302-318", Crossref DOI);
Ham21 (Burnol's [7] and Nakamura's [5] agree: Math. Z. 10 (1921), no. 3-4, 240-254); Joh17 and PT21 (Crossref: IEEE TC 66(8)
1281-1292; BLMS 53(3) 792-797); Ki06 (Crossref, DOI 10.4064/aa124-3-1); LM11 (arXiv journal-ref: Comment. Math. Univ. St.
Pauli 60 (2011), No. 1-2, 143-169); LMOZ24 (arXiv 2406.00786v1, 2 June 2024); Nak20 (arXiv 2008.02570v4, 10 Sep 2021).
Riemann 1859, pp. 671-680: VERIFIED against a primary source. The page range on disk came only from reference lists (Shi,
arXiv:1502.06844 and 1706.08868; Lagarias-Montague and Matiyasevich-Saidak-Zvengrowski give no pages; the Wilkins
transcription and the Werke reprint say only "Monatsberichte der Berliner Akademie, November 1859"). I then read the scan of
the 1859 volume in the BBAW library (Monatsberichte ... 1859, Berlin 1860; digilib.bbaw.de, 09-mon/1859): scan 680 is printed
p. 668, scan 692 is printed p. 680 and ends Riemann's text ("... im Mittel übereinstimmend erkennen läfst."), and scan 683,
the unnumbered opening page of the November report, starts it ("Hierauf trug Hr. Kummer folgende von Hrn. Riemann ...
Mittheilung „über die Anzahl der Primzahlen unter einer gegebenen Gröfse" vor"). So 671-680 is right. Reliability: high; the
end page is printed, the start page follows from the constant scan offset 12 (two printed anchors). Saved:
`lit/referee-monatsber-1859-scan680-p668.png`, `-scan683-p671.png`, `-scan692-p680.png`.
Optional additions: DOIs for Bur12 and Ki06, "no. 1-2" for LM11, and Ki05 (F6.3).

### Other findings (outside items 1-8)

O1 (MAJOR for posting, Provenance, l. 1080-1082). "the working corpus of fetched literature is not redistributed, for
copyright reasons" is false for the repository the paper points to. Checked 2026-10-01 through the GitHub API: the public
repository contains `rh-program/results/novel-wave-s36/staircase/lit/` with publisher PDFs and full texts (e.g.
`ki-AA-124-2006-chowla-selberg.pdf`, `ki-CRAS-342-2006-modified-epstein.pdf`, `lagarias-AA-120-2005-differenced.pdf`,
`haglund-CEJM-2011-degruyter-fulltext.md`, and arXiv PDFs) and `rh-program/results/haglund-cert-s37/novelty-F/ahn-thesis-penn.pdf`;
the paper's own component list sends the reader to both folders. The mathematics is unaffected, but posting a false data
statement that points at redistributed copyrighted files is a legal exposure for the author and is hard to undo. Fix, before
posting: remove those files from the public repository (history included, if the sponsor wants the statement to be true of
past commits), then keep the sentence; or, if they stay, delete the sentence. This decision is the sponsor's, not the writer's.
The certificate zip is clean (58 files; its only third-party texts are DLMF pages; DLMF's reuse terms were not checked).

O2 (MINOR, Provenance, l. 1040-1050). The program's own convention (`results/arxiv/README.md` l. 137-139: "with a commit pin")
is not met; the zip's host is not named; paths carry internal labels. See §3 for the ruling and the text to add.

O3 (MINOR, abstract l. 71-72 and abstract.txt; first-read R1). OLD: `the number of real zeros of
$\Xi_N$ is odd,` NEW: `the number of positive real zeros of
$\Xi_N$, counted with multiplicity, is odd,` (Ξ_N is even, so the count on all of R is even).

O4 (TYPO, abstract l. 68-70; R24). OLD: `a
shallow lobe followed by a deeper one` NEW: `a
low lobe followed by a higher one` (the lobes are positive). With O3 and F4.1 the abstract grows from 1845 to about 1881
characters, still under arXiv's 1920 (counted on abstract.txt); make every abstract change in both main.tex and abstract.txt.

O5 (TYPO, Thm 1.1(b), l. 146; R20). OLD: `$z_0 \in z^* + [-10^{-48}, 10^{-48}]^2$ with` NEW: `$z_0 \in z^* + [-10^{-48},
10^{-48}]^2$ (where $w + [-r, r]^2$ is the closed square $\{w + a + bi : |a|, |b| \le r\}$) with`

O6 (TYPO, §6.1, l. 710; R26). OLD: `series $\Xi = \sum_{n\ge1}\Phi_n$ \cite[(12), p.~3]{Hag}; route L does not.` NEW: `series
$\Xi = \sum_{n\ge1}\Phi_n$ \cite[(12), p.~3]{Hag}, which also follows from \eqref{eq:riemann} and Lemma~\ref{lem:relation};
route L does not.`

## §3 Rulings on "Points the writer could not settle alone"

1. AI footnote. KEEP the README wording (main.tex l. 40-46 matches `results/arxiv/README.md` l. 130-133 verbatim). It is the
   program's recorded standard, settled 2026-08-27 with the instruction that later sessions must not undo it, and it is the
   more accurate text for this paper: the later wording on the two posted papers says the author "made the technical and
   editorial decisions", which claims more than a footnote that credits Claude with the derivations, computations and text
   should. Harmonizing the older papers is the sponsor's call, not a defect here.
2. Length (16 pp. against 8-12). ACCEPT. arXiv sets no limit, and the full proofs of Thms 3.1, 3.3, 4.1, 4.2 and Lemmas
   6.1-6.3 are what make the paper checkable without the program's files. If trimming is wanted, move the §6.2 bullet bounds
   and the Taylor-model paragraph to an appendix; cut no proof.
3. Data availability. ACCEPT the real directory names and the SHA-256 pin of the zip (50/50 SHA256SUMS entries verify inside
   `certificate/`, and the zip's hash matches the paper), on three conditions before posting: (a) resolve O1; (b) whoever
   can run git adds the commit (or tag) of the posted state, as `results/arxiv/README.md` l. 137-139 requires; (c) name where
   the zip lives. Suggested text after "in that repository": `(commit \texttt{<hash>}; directory names are the program's
   internal unit labels)`, and after the SHA-256: `, deposited at \url{<Zenodo DOI>}`.
4. `producer-B/logs/ladder.log`. ACCEPT as documented. Verified: the file's SHA-256 ee71d58d... equals the hash in the final
   block of B's SHARED.md (l. 116), the first run's 461538ee... (l. 92) is superseded, the re-run output
   `rerun-F/B-ladder-rerun.log` (cc4a6f28...) is kept separately, and `certificate/README.md` l. 112-120 says so.
5. Haglund's appendix page. CONFIRM p. 16: in `haglund-0910.5228.txt` the page-15 footer is l. 728 and "7 Appendix" opens
   p. 16 at l. 729, with the zero 20.6253...+2.6971...i at l. 732. Keep the paper as is; do not edit A's hashed CERT (l. 103
   "App. p. 15"); add one erratum line to `certificate/README.md`.
6. The writer's re-runs. CONFIRMED where I could check: `rerun-F/A-h1-diff.txt` differs only in timings, the re-run log
   values equal the CERT's, and my own run of `verify-F/haglund_direct_arb.py` reproduces the ladder values (F1.7). I did
   not re-run certificate B (not needed: its CERT, logs and hashes agree).

## §4 Checked and found CORRECT (coverage)

Mathematics, re-derived step by step by the referee (not compared): Riemann's kernel in §1.1 with 8π²n⁴, 12πn² for
Ξ = ∫₀^∞cos(zt)φ(t)dt (matches Haglund (2)-(3)); formula (2) for G; (3) for Φ_n; identity (4), ξ = ½ + ½s(s−1)Σg_n,
|g_n(s)| ≤ g_n(Re s); Lemma 2.1 every line; Thm 3.1 (k′, k″, root (3+2√2)/4, the alternating half-period argument, t = 0,
the P_w formula); Cor 3.2; Thm 3.3 (both integrations by parts, −2k′(0), φ̃_n = ½φ_n, φ̃′ and φ̃″ polynomials, positivity for
y ≥ 4π, the n = 1 values); Prop 3.4 (limit via Riemann-Lebesgue, signs of the summands, n = 1 negative); Cor 3.5 (parity at
lobe ends, Ξ_N(0) ≥ 0.4971 − c_1, finiteness); Thm 4.1 (a) growth and Hadamard, (b)(i) the k = 0, 1 terms giving
½(¼+t²)g_m → (4πm² − 1)e^{−πm²} and the O(|t|^{7/4}e^{−π|t|/4}) Γ-part, (b)(ii) C_w, the t^{−2j−2} expansion, evenness, the
u → −∞ coefficients, Vandermonde; C_w = c_N and the Ξ_N case; Thm 4.2 (D″ = D/4, α = −½, δ(1/x) = √xδ(x), the Mellin
transform, Burnol's (1)-(4)); Prop 4.3 (Rouché and the s ↦ 1 − s̄ symmetry) and read-F F3's two regimes for (ii); the Hurwitz
transfer in §7; Lemmas 6.1-6.3 and the half-plane fact; B's remainders (Stirling per DLMF 5.11, Euler-Maclaurin with DLMF
24.9.2, integration-by-parts ρ_K, lower-series remainder, |Φ_n| ≤ 9Xe^{−X} and 18π(M+1)²e^{−π(M+1)²}); the Taylor model
(aliasing identity, |D_k − a_k|, E); proofs of Thm 1.1(a)-(c) and Thm 7.1(a)-(c), including the mirror 1 − ρ̄_24.

Numbers recomputed independently (mpmath, 60 digits; script in the referee's scratch space): c_1 ... c_5 to all printed
digits; Σ(4πn² − 1)e^{−πn²} = ½; 0.290944 and 0.0394988; 1.45711; 16e^{−3π} = 1.29·10^{−3}; 2U_32 = 1.948·10^{−1393};
18π·31²e^{−961π} = 3.711·10^{−1307}; E = 3.511·10^{−1106}, 1.358·10^{−1087}, 2.093·10^{−1145}, 2.642·10^{−871};
z* − c = 3.65853·10^{−11} − 2.17852·10^{−11} i; Ξ(0) = 0.497120778; |Φ_1|, |Φ_2| at 3144.8946 = 7.987·10^{−9};
|Φ_27| = 1.458·10^{−991}; |Φ_28| = 1.49249·10^{−1066} and |Ξ| = 1.4923145·10^{−1066} there; |Φ_28(z*)| = |Ξ(z*)| =
1.49295·10^{−1066}; |Φ_29(z*)| = 2.83·10^{−1144}; the Haglund ratios (item 5); Thm 1.1(c) inequalities.

Numbers matched digit by digit to the sources: Table 1 (both columns, all radii), Table 2 (every row, piece count, k, the
caption's ΔArg, E and lower moduli), Table 3 (every entry), all of §6.1-6.2, the §6.3 cross-checks (18 points, 6.43·10^{−1137},
1.18·10^{−1288}; third evaluation ±2.49, ±1.71·10^{−1082}, 1.7·10^{−1084}, 6.1·10^{−1072}), §7 (enclosures, squares, M_R, E,
lower modulus, ρ_24 digits, lobes), z* to all printed digits, §5 and §1.4 figures, Haglund's table, the N = 4 census.

Files and hashes: SHA-256 of both CERT.md files and of the zip equal the printed ones; `certificate/SHA256SUMS` 50/50 OK;
re-run diffs are timing-only; the public repository answers (HTTP 200) and has `rh-program/` with every cited path;
abstract.txt is 1845 characters (limit 1920); author name and footnote follow `results/arxiv/README.md`.

Quotations (item 6), bibliography (item 8, all 17 entries, Riemann's pages against the 1859 scan), and scope (item 7).

End of report. Referee, 2026-10-01. Nothing outside this report was edited except the three evidence scans saved under
`lit/referee-monatsber-1859-*.png` (as the brief's network rule asks) and the dated blocks appended to `SHARED.md`.
