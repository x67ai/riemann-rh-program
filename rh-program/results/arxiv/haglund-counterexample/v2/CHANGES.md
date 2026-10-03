# Version 2 (PREPARED, NOT PUBLISHED) — what changed against the published version 1, and why

Second form, 16:59 IST 2026-10-03, after the sponsor's instruction in chat the same hour: where the author had already corrected a point in his own copy, the paper is updated to say so, and a claim that adds nothing to his copy is removed. (The first form of this folder, of 16:2x IST, only re-attributed the two "corrections"; it is superseded.) Version 1 is the published paper (Zenodo version DOI 10.5281/zenodo.23071931; `../main.tex`, `../main.pdf`, untouched). Publishing version 2 is the sponsor's step: a new version on the same Zenodo record and a new copy on x67.ai (`FETCH-LIST-ROUND9.md`, open items).

**Why.** The author's own copy of the paper on his web page (title-page date February 9, 2011; server date the same; SHA-256 a8daaab8a5b68920aeb68c038acb8d8d35e79e6ba2143494aab074fc2f3988df) already has the table entry 31 at N = 4 and already states that the coefficient of 1/x² in Ξ_N "approaches zero from below as N → ∞". Read at the page by the orchestrator (`LOG.md`, 16:23 IST 2026-10-03; `results/haglund-conj4/L-lit/PRIOR-ART.md` §3). Version 1 announces both points, in the abstract and in a section heading, as corrections of "Haglund's paper"; on the two corrections themselves it has nothing that his copy does not have.

**What is removed.** The claim of correcting his paper: the abstract's sentence "Two statements in Haglund's paper are corrected …", the words "and two corrections to Haglund's paper" in the heading of §1.3, "the two corrections" in §1.5, and the sentences that call his table entry "inconsistent" and set his printed conclusion against ours.

**What stays, because it is the paper's own and the argument uses it.** Corollary odd (the number of positive real zeros of Ξ_N, with multiplicity, is odd; an even number in every positive lobe) and Proposition tail (x²Ξ_N(x) tends to an explicit negative limit for every N) — stated as results, with their proofs unchanged. The abstract now states them as results.

**What is added.** The credit: §1.3 says that both facts agree with the author's web copy, quotes its table and its sentence, and says that the arXiv and journal versions differ and that his copy corrects both; the paragraph after Proposition tail and the paragraph after Corollary odd say the same at the place of use; a reference [Hag11w] with the URL and read date; the date line; one sentence of thanks (the sponsor keeps or deletes it).

**No theorem, proof, constant or number of version 1 is altered.**

**Checks.** `check-submittable.sh` on this folder: ALL CHECKS PASSED (compiles clean, 15 pp.; no RH-verdict sentence; no internal reference). Integrity diff (KICKSTART 10(t)), mechanical: the complete line diff of `../main.tex` against `main.tex` follows (82 changed lines); every changed line belongs to one of the spans above.

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
> are one quarter of ours (at $N = 1$, $-.01974938206$ against $-0.078997$),
> because his (51) applies his (50) at $x$ although \eqref{eq:XiN} evaluates $G$
> at $x/2$; the factor does not affect signs. The arXiv and journal versions
> conclude that the coefficient of $1/x^2$ in $\Xi_N(x)$ ``is positive for
> $k \ge 3$ and negative for $1 \le k < 3$'' \cite[p.~10]{Hag}; the later copy
> states instead that it ``approaches zero from below as $N \to \infty$''
> \cite[p.~10]{HagW}, which is what Proposition~\ref{prop:tail} shows for every
> $N$. The coefficients of $\Phi_1$, $\Phi_2$ and $\Phi_3$ nearly cancel, and
> ten-digit values of them cannot resolve their sum, which is of order $10^{-16}$,
> at $N = 3$. Haglund's use of these coefficients to exhibit non-monotone zeros of
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
1036a1043,1045
> 
> \section*{Acknowledgment}
> \addcontentsline{toc}{section}{Acknowledgment}
1037a1047,1048
> I thank J. Haglund for pointing out the corrected copy \cite{HagW} of his paper.
> 
1089a1101,1106
> \bibitem[Hag11w]{HagW} J. Haglund, \emph{Some conjectures on the zeros of
> approximates to the Riemann $\Xi$-function and incomplete gamma functions},
> author's copy dated February 9, 2011,
> \url{https://www2.math.upenn.edu/~jhaglund/preprints/rh8.pdf} (read October 3,
> 2026).
> 
```
