# REFEREE REPORT: "A counterexample to Haglund's monotonic-zeros conjecture for the Riemann Ξ approximants"

Blind referee, 2026-10-01. Object: `main.pdf` (16 pp.) / `main.tex` as of 2026-10-01 00:51. Brief: `REFEREE-BRIEF.md`.
Built incrementally; sections land in order §1 (first read, before any source was opened), §2 (brief items 1-8), §3, §4, then §0.

## §0 Verdict

(pending: written last)

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
`\begin{tabular}{>{\raggedright\arraybackslash}p{0.30\textwidth}>{\raggedright\arraybackslash}p{0.30\textwidth}>{\raggedright\arraybackslash}p{0.30\textwidth}}` (needs `array`).

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

<!-- END -->
