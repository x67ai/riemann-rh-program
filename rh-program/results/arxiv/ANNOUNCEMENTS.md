# Post text for the two circulating papers

Written 2026-08-27. Each entry is under 280 characters **excluding the link** — X counts any URL
as 23 characters regardless of length, so add 23 to the counts below if the link goes in the same
post. Counts were measured, not estimated; re-measure if you edit.

A note on framing before the drafts. Both papers are **negative results**, and both are stronger
when that is the hook rather than something the reader discovers in paragraph two. "We tried the
obvious thing and it pays exactly zero, here is the proof" is a good post. "Breakthrough in the
Riemann hypothesis" would be false and would be caught within a day. The drafts below lead with
the negative on purpose.

---

## A4 — the two-moment certificate

**Primary — 263 characters.**

> Alpöge–Furman's two-thirds theorem rests on a two-moment certificate. Does adjoining the cubic
> trace at a second bandwidth buy anything? Exactly nothing: the marginal value is 0 as an LP
> equality, not a small number. Explicit witness, 12 theorems checked in Lean.

**Shorter, sharper — 212 characters.**

> Does a third moment sharpen the certificate behind "more than 2/3 of zeta's zeros are simple and
> on the line"? No — and not approximately. The marginal value is exactly zero, with a witness you
> can check by hand.

**Method-forward, for a formalization audience — 212 characters.**

> A negative result, machine-checked: adjoining the cubic trace row to the two-moment certificate
> for zeta's zeros adds exactly nothing. δ₀ = 0 as an exact LP equality. 12 theorems in Lean 4,
> clean axiom footprint.

---

## Seed no-go — products of the per-prime Tate curves

**Primary — 254 characters.**

> Connes–Consani's new per-prime Tate curves make the products E_p × E_q look like a home for the
> Weil explicit formula. They're empty: Néron–Severi has rank 2 — no diagonal, no graph classes,
> Castelnuovo–Severi vacuous. The rigidity is Winkelmann's, 2002.

**Shorter — 184 characters.**

> The obvious thing to try with Connes–Consani's new per-prime Tate curves is products E_p × E_q.
> Don't: they carry no correspondence calculus at all. Here's the proof, and the priority.

**Priority-forward — the most honest hook, and the most interesting — 226 characters.**

> Wrote up a no-go for products of the per-prime Tate curves, then found the key rigidity is Jörg
> Winkelmann's, from 2002. So the paper says that, in the abstract. What's new is the Néron–Severi
> collapse and the no-go it forces.

---

## Two things to get right in the thread, not the first post

1. **The AI disclosure.** Every paper carries it in a page-1 footnote and the repository states it.
   Putting it in the thread yourself is better than being asked; it reads as confidence rather than
   omission. Something like: *"Written with Claude (Anthropic) under my direction — the full
   program record, including every review and correction, is in the repo."*
2. **The link.** `https://github.com/x67ai/riemann-rh-program` — the README's "what a skeptical
   reader should check first" section is the landing point that does the most work, because it
   sends people to the Lean development, which they can verify without trusting anything you say.

## What not to claim

* Not a proof of, or progress toward, RH. Neither paper claims either.
* Not "novel" without qualification for the seed paper — Theorems 1–3 are Winkelmann's, and the
  paper says so in its abstract. Leading with that is a strength; being caught omitting it is not.
* No journal or arXiv status until there is one.
