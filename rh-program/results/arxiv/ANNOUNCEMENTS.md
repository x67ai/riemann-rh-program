# Post text for the two papers

Every draft below is in a fenced block so it copies clean. Counts are measured, not
estimated. X replaces any URL with 23 characters no matter how long it is, so each count
below is followed by the total with a link and one space. All six fit in 280 with a link.
Re-measure if you edit.

Both papers are negative results. The drafts say so in the first sentence, because that is
the finding. A post shaped like progress on the Riemann hypothesis would be wrong on the
facts and would be corrected within a day.

---

## The cubic-augmentation paper

250 characters, 274 with a link.

```
Alpöge and Furman proved that more than two thirds of the zeta zeros are simple and on the critical line. Their certificate reads two moments. I checked whether a third moment adds anything. It adds exactly zero, with a witness you can check by hand.
```

248 characters, 272 with a link.

```
A third moment does not sharpen the Alpöge–Furman certificate for simple zeros of zeta. The marginal value is exactly zero, not merely small. The paper proves it as an LP equality, exhibits the witness, and machine-checks twelve theorems in Lean 4.
```

251 characters, 275 with a link. For a formalization audience.

```
New paper, a negative result. Adding the cubic trace row to the two-moment certificate behind the Alpöge–Furman theorem on simple zeros of zeta buys nothing. Twelve supporting theorems are machine-checked in Lean 4, with no sorry and no native_decide.
```

---

## The Tate-products paper

246 characters, 270 with a link.

```
Connes and Consani's per-prime Tate curves invite an obvious move: take the products E_p × E_q and look for a correspondence calculus for the Weil explicit formula. The products are empty. Néron–Severi has rank two, so there is no diagonal class.
```

246 characters, 270 with a link.

```
The obvious thing to try with Connes and Consani's per-prime Tate curves is the products E_p × E_q. They carry no correspondence calculus for the explicit formula, and the paper proves it. It also says where the key step was anticipated, in 2002.
```

231 characters, 255 with a link. This is the one to use. The
priority correction is the most interesting thing about the paper, and volunteering it
costs nothing.

```
I wrote a no-go for products of the per-prime Tate curves, then found that the rigidity it turns on is Jörg Winkelmann's, from 2002. The abstract says so. What is new is the Néron–Severi collapse and the no-go that follows from it.
```

---

## For the thread, not the first post

The AI disclosure. Both papers carry it in a footnote on page 1, and the repository states
it. Say it yourself rather than waiting to be asked:

```
Written with Claude (Anthropic) under my direction. The full program record, including every review and correction, is in the repo.
```

The links.

    https://x67.ai/cubic-augmentation-no-go.pdf
    https://x67.ai/tate-products-no-go.pdf
    https://github.com/x67ai/riemann-rh-program

Lead a post with the paper it is about. Put the repository in the thread and send people
to its README section on what a skeptical reader should check first, which points at the
Lean development. They can verify that without taking your word for anything.

## What not to claim

Neither paper proves anything about the Riemann hypothesis or moves toward it, and neither
claims to.

The Tate-products paper is not novel without qualification. Theorems 1 to 3 are
Winkelmann's, from 2002, and the abstract says so. Say it in the post as well.

Neither paper has a journal or an arXiv number. Do not imply one. Both have Zenodo DOIs (recorded 2026-09-02): the cubic-augmentation paper is 10.5281/zenodo.22171688 and the Tate-products paper is 10.5281/zenodo.22171136 (concept DOIs; details in `results/arxiv/README.md`). Cite those.
