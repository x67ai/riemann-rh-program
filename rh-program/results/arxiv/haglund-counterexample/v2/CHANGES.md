# Version 2 (PREPARED, NOT PUBLISHED) — what changed against the published version 1, and why

Prepared 16:25 IST 2026-10-03. Version 1 is the published paper (Zenodo version DOI 10.5281/zenodo.23071931; `../main.tex`, `../main.pdf`, untouched). Publishing version 2 is the sponsor's decision: a new version on the same Zenodo record and a new copy on x67.ai (`FETCH-LIST-ROUND9.md`, open items).

**Why.** The author's own copy of the paper on his web page (dated February 9, 2011; server date the same; SHA-256 a8daaab8a5b68920aeb68c038acb8d8d35e79e6ba2143494aab074fc2f3988df) already has the table entry 31 at N = 4 and already states that the coefficient of 1/x² in Ξ_N "approaches zero from below". Version 1 presents both points as corrections of "Haglund's paper" without saying that the author had made them himself; that is accurate for arXiv v1 and for the journal version only. Read at the page by the orchestrator (`LOG.md`, 16:23 IST 2026-10-03; `results/haglund-conj4/L-lit/PRIOR-ART.md` §3).

**What changed (nine spans; no theorem, proof, constant or number of version 1 is altered).**
1. Abstract (and `abstract.txt`): the last sentence now says the two statements belong to the arXiv and journal versions, are corrected in the author's later copy, and are proved here in corrected form.
2. §1.3 heading: "two corrections to Haglund's paper" → "two statements of Haglund's paper".
3. §1.3, the sentence before items (i), (ii): replaced by four sentences naming the three versions and quoting the corrected sentence of the web copy (p. 10).
4. §1.5 (Organization): "the two corrections" → "the two statements of Section 1.3".
5. After Proposition tail: two sentences added — the later copy gives the coefficients to more digits and the corrected conclusion, for the same reason.
6. After Corollary odd: one sentence added — the table in the later copy has 31.
7. Bibliography: new entry [Hag11w], the author's copy with its URL and read date.
8. Date line: "October 1, 2026; revised October 3, 2026".
9. A one-sentence Acknowledgment (for the sponsor to keep or delete: it thanks the author for pointing to his corrected copy).

**Checks.** `check-submittable.sh` on this folder: ALL CHECKS PASSED (compiles clean, 16 pp.; no RH-verdict sentence; no internal reference). Integrity diff (KICKSTART 10(t)), mechanical: the complete line diff of `../main.tex` against `main.tex` follows; every changed line is one of the nine spans above.

```diff
47c47
< \date{October 1, 2026}
---
> \date{October 1, 2026; revised October 3, 2026}
71,74c71,75
< statements in Haglund's paper are corrected: the number of positive real zeros of
< $\Xi_N$, counted with multiplicity, is odd, so his table entry $32$ at $N = 4$ is inconsistent (a numerical
< census finds $31$), and the $1/x^2$ coefficient of $\Xi_N$ on the real axis is
< negative for every $N$.
---
> statements of the arXiv and journal versions of Haglund's paper, both corrected
> in the author's own later copy, are proved in their corrected form: the number
> of positive real zeros of $\Xi_N$, counted with multiplicity, is odd (the table
> entry at $N = 4$ is $31$, not $32$), and the $1/x^2$ coefficient of $\Xi_N$ on
> the real axis is negative for every $N$.
175c176
< \subsection{The mechanism, and two corrections to Haglund's paper}\label{sec:mech}
---
> \subsection{The mechanism, and two statements of Haglund's paper}\label{sec:mech}
198c199,206
< The same sandwich corrects two statements in \cite{Hag}.
---
> The same sandwich settles two statements on which the versions of Haglund's
> paper differ. The arXiv version \cite{Hag} and the journal version \cite{HagJ}
> print the statements quoted in (i) and (ii) below. The copy of the paper on the
> author's web page \cite{HagW}, dated February 9, 2011, corrects both: its table
> has $31$ at $N = 4$, and its paragraph on the coefficient of $1/x^2$ ends ``Thus
> the coefficient of $1/x^2$ in $\Xi_N(x)$ approaches zero from below as
> $N \to \infty$'' \cite[p.~10]{HagW}. Corollary~\ref{cor:odd} and
> Proposition~\ref{prop:tail} prove the corrected statements, for every $N$.
273c281
< theorems and the two corrections. Section~\ref{sec:structure} gives the
---
> theorems and the two statements of Section~\ref{sec:mech}. Section~\ref{sec:structure} gives the
474c482,486
< of $\Phi_2$ is positive and that of $\Xi_2$ negative, and both are.
---
> of $\Phi_2$ is positive and that of $\Xi_2$ negative, and both are. The later
> copy \cite{HagW} gives the three coefficients to more digits and states the
> corrected conclusion quoted in Section~\ref{sec:mech}, for the reason used
> here: the coefficients of $\Phi_k$ are positive for $k > 3$, and $\Xi$ decays
> exponentially on the real axis \cite[p.~10]{HagW}.
499c511,512
< $103.3679880094135$. The other nine entries are odd.
---
> $103.3679880094135$. The other nine entries are odd. The table in \cite{HagW}
> has $31$.
1037a1051,1055
> \section*{Acknowledgment}
> \addcontentsline{toc}{section}{Acknowledgment}
> 
> I thank J. Haglund for pointing out the corrected copy \cite{HagW} of his paper.
> 
1089a1108,1113
> \bibitem[Hag11w]{HagW} J. Haglund, \emph{Some conjectures on the zeros of
> approximates to the Riemann $\Xi$-function and incomplete gamma functions},
> author's copy dated February 9, 2011,
> \url{https://www2.math.upenn.edu/~jhaglund/preprints/rh8.pdf} (read October 3,
> 2026).
> 
```
