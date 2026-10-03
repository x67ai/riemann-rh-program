# Version 2 (PREPARED, NOT PUBLISHED) — what changed against the published version 1, and why

Third and final form, 18:03 IST 2026-10-03: the second form (the sponsor's instruction: say where the author had already corrected a point, remove a claim that adds nothing to his copy) with the six fixes of the independent check (`INTEGRITY-DIFF.md`: CLEAN-WITH-CORRECTIONS) applied. Version 1 is the published paper (Zenodo version DOI 10.5281/zenodo.23071931; `../main.tex`, `../main.pdf`, untouched). Publishing version 2 is the sponsor's step: a new version on the same Zenodo record and a new copy on x67.ai (`FETCH-LIST-ROUND9.md`, item 6).

**Why.** The author's own copy of the paper on his web page (title-page date February 9, 2011; server date the same; SHA-256 a8daaab8a5b68920aeb68c038acb8d8d35e79e6ba2143494aab074fc2f3988df) already has the table entry 31 at N = 4 and already states that the coefficient of 1/x² in Ξ_N "approaches zero from below as N → ∞". Version 1 announces both points, in the abstract and in a section heading, as corrections of "Haglund's paper"; on the two corrections themselves it has nothing that his copy does not have.

**Removed.** The claim of correcting his paper: the abstract's sentence "Two statements in Haglund's paper are corrected …"; the words "and two corrections to Haglund's paper" in the heading of the mechanism subsection (§1.4 in the PDF); "the two corrections" in the organization paragraph (§1.7); the sentences that call his table entry "inconsistent" and set his printed conclusion against the paper's.

**Kept, because they are the paper's own and its argument uses them.** Corollary odd (an odd number of positive real zeros; an even number in every positive lobe) and Proposition tail (the explicit negative limit of x²Ξ_N), with their proofs unchanged; the abstract now states them as results.

**Added.** The credit to his web copy at three places (the mechanism subsection; after Proposition tail; after Corollary odd), with its table and its sentence quoted; a reference [Hag11w] with the address and the read date; the date line; one sentence of thanks (the sponsor keeps or deletes it).

**After the independent check (six small fixes).** (1) "the later copy" → "the author's web copy" (no claim about the order of the journal version and his copy); (2) the note in reference [Hag09] on page numbers now excepts the places where [Hag11w] is cited; (3) the sentence on the near-cancellation of the three coefficients no longer reads as a diagnosis: their sum at N = 3 is below the resolution of the printed values "in either copy"; (4) one printed value of version 1 is given with one more digit, −0.0789975 for −0.078997, to match the list two lines above it (the number itself is unchanged); (5) "which is what Proposition tail shows for every N" → "shows: the limit is negative for every N and tends to 0"; (6) the heading "Proof of Theorem 1.1" now gives the PDF bookmark its number (the bookmark read "Theorem ??" in version 1 as well).

**No theorem, proof, hypothesis, constant or formula of version 1 is altered.**

**Checks.** `check-submittable.sh` on this folder: ALL CHECKS PASSED (15 pp.). A script of 14 fact checks of the new sentences against the web copy, arXiv v1 and the journal text: all pass (`LOG.md`, 17:42 IST 2026-10-03). The independent check by a second model (`INTEGRITY-DIFF.md`): integrity clean (its own diff equal to this one), every new sentence true at the page, six corrections, all applied here. Mechanical diff of `../main.tex` against `main.tex`: 15 hunks, 34 lines removed, 51 added; it follows.

```diff
47c47
< \date{October 1, 2026}
---
> \date{October 1, 2026; revised October 3, 2026}
70,74c70,73
< approximant departs from $\Xi$, can leave a non-real zero below real zeros. Two
< statements in Haglund's paper are corrected: the number of positive real zeros of
< $\Xi_N$, counted with multiplicity, is odd, so his table entry $32$ at $N = 4$ is inconsistent (a numerical
< census finds $31$), and the $1/x^2$ coefficient of $\Xi_N$ on the real axis is
< negative for every $N$.
---
> approximant departs from $\Xi$, can leave a non-real zero below real zeros. The same
> structure shows that the number of positive real zeros of $\Xi_N$, counted with
> multiplicity, is odd, and that $x^2\Xi_N(x)$ tends to a negative limit on the
> real axis for every $N$.
175c174
< \subsection{The mechanism, and two corrections to Haglund's paper}\label{sec:mech}
---
> \subsection{The mechanism}\label{sec:mech}
198c197,198
< The same sandwich corrects two statements in \cite{Hag}.
---
> The same sandwich gives two facts about the real zeros and the real-axis tail
> of $\Xi_N$.
201,205c201
< multiplicity, is odd for every $N$ (Corollary~\ref{cor:odd}). Haglund's table
< \cite[p.~4]{Hag} lists $1$, $7$, $15$, $32$, $53$, $79$, $113$, $155$, $207$, $263$ real zeros for
< $N = 1, \ldots, 10$; the even entry $32$ at $N = 4$ is inconsistent with this,
< and a numerical census of $\Xi_4$ finds $31$, the largest being
< $103.3679880094135$, in agreement with Haglund's printed $103.3679880094$.
---
> multiplicity, is odd for every $N$ (Corollary~\ref{cor:odd}).
207,209c203
< $N \ge 1$ (Proposition~\ref{prop:tail}), whereas \cite[p.~10]{Hag} states
< ``Thus the coefficient of $1/x^2$ in $\Xi_N(x)$ is positive for $k \ge 3$ and
< negative for $1 \le k < 3$'' (his $k$ is $N$).
---
> $N \ge 1$ (Proposition~\ref{prop:tail}).
210a205,213
> Both agree with the copy of Haglund's paper on the author's web page
> \cite{HagW}, dated February 9, 2011: its table lists $1$, $7$, $15$, $31$,
> $53$, $79$, $113$, $155$, $207$, $263$ real zeros for $N = 1, \ldots, 10$
> \cite[p.~4]{HagW}, and it states that the coefficient of $1/x^2$ in $\Xi_N(x)$
> ``approaches zero from below as $N \to \infty$'' \cite[p.~10]{HagW}. The arXiv
> version \cite{Hag} and the journal version \cite{HagJ} have $32$ at $N = 4$
> and, for the coefficient, ``positive for $k \ge 3$ and negative for
> $1 \le k < 3$'' \cite[p.~10]{Hag} (his $k$ is $N$); \cite{HagW} corrects
> both.
273c276
< theorems and the two corrections. Section~\ref{sec:structure} gives the
---
> theorems and their consequences for the real zeros and the tail. Section~\ref{sec:structure} gives the
464,474c467,479
< \cite[(52), p.~10]{Hag}; his values are one quarter of ours (at $N = 1$,
< $-.01974938206$ against $-0.078997$), because his (51) applies his (50) at $x$ although
< \eqref{eq:XiN} evaluates $G$ at $x/2$; the factor does not affect signs. He concludes that
< the coefficient of $1/x^2$ in $\Xi_N(x)$ ``is
< positive for $k \ge 3$ and negative for $1 \le k < 3$'' \cite[p.~10]{Hag}.
< Proposition~\ref{prop:tail} shows that it is negative for every $N$: the
< coefficients of $\Phi_1$, $\Phi_2$ and $\Phi_3$ nearly cancel, and ten-digit
< values of them cannot resolve their sum, which is of order $10^{-16}$, at
< $N = 3$. Haglund's use of these coefficients to exhibit non-monotone zeros of
< the pencil $t\Phi_1 + \Phi_2$ is unaffected: it needs only that the coefficient
< of $\Phi_2$ is positive and that of $\Xi_2$ negative, and both are.
---
> \cite[(52), p.~10]{Hag}, and to more digits in \cite[(52)]{HagW}; his values
> are one quarter of ours (at $N = 1$, $-.01974938206$ against $-0.0789975$),
> because his (51) applies his (50) at $x$ although \eqref{eq:XiN} evaluates $G$
> at $x/2$; the factor does not affect signs. The arXiv and journal versions
> conclude that the coefficient of $1/x^2$ in $\Xi_N(x)$ ``is positive for
> $k \ge 3$ and negative for $1 \le k < 3$'' \cite[p.~10]{Hag}; the author's web copy
> states instead that it ``approaches zero from below as $N \to \infty$''
> \cite[p.~10]{HagW}, which is what Proposition~\ref{prop:tail} shows: the limit
> is negative for every $N$ and tends to $0$. The coefficients of $\Phi_1$, $\Phi_2$ and $\Phi_3$ nearly cancel: their sum at $N = 3$, of
> order $10^{-16}$, is below the resolution of the printed values of (52) in
> either copy. Haglund's use of these coefficients to exhibit non-monotone zeros of
> the pencil $t\Phi_1 + \Phi_2$ needs only that the coefficient of $\Phi_2$ is
> positive and that of $\Xi_2$ negative, and both are.
495,496c500,501
< In Haglund's table \cite[p.~4]{Hag} (Section~\ref{sec:mech}) the entry $32$ at $N = 4$ is
< even, so by Corollary~\ref{cor:odd} it cannot count $32$ simple real zeros; a
---
> The ten entries of Haglund's table in \cite[p.~4]{HagW}
> (Section~\ref{sec:mech}) are odd, in agreement with Corollary~\ref{cor:odd}. A
498,499c503,505
< argument principle, not interval-rigorous) finds $31$, the largest being
< $103.3679880094135$. The other nine entries are odd.
---
> argument principle, not interval-rigorous) finds $31$ real zeros, the entry of
> \cite{HagW}, the largest being $103.3679880094135$; the arXiv and journal
> versions print $32$ there.
952c958
< \subsection{Proof of Theorem~\ref{thm:main}}
---
> \subsection{Proof of Theorem~\texorpdfstring{\ref{thm:main}}{1.1}}
1036a1043,1047
> 
> \section*{Acknowledgment}
> \addcontentsline{toc}{section}{Acknowledgment}
> 
> I thank J. Haglund for pointing out the corrected copy \cite{HagW} of his paper.
1083c1094
< refer to this version.
---
> refer to this version, except where \cite{HagW} is cited.
1089a1101,1106
> \bibitem[Hag11w]{HagW} J. Haglund, \emph{Some conjectures on the zeros of
> approximates to the Riemann $\Xi$-function and incomplete gamma functions},
> author's copy dated February 9, 2011,
> \url{https://www2.math.upenn.edu/~jhaglund/preprints/rh8.pdf} (read October 3,
> 2026).
> 
```
