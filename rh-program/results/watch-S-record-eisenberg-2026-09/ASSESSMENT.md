# Watch item — the Eisenberg S(t) record certificates (FYI only, 2026-09-15)

**Sponsor's ask (2026-09-15, chat, FYI only; the RH program itself is NOT resumed this session):**
"is there anything relevant to our RH program here?" — followed by the full text of an announcement
and its two certificates, and then the source: Avraham Eisenberg, X post of 14 Sep 2026,
https://x.com/avi_eisen/status/2099622967751663749 (the certificate is a reply on the same thread).
Independent corroboration of the same data seen in a public pull request titled "import S(t) records"
on github.com/GettysburgResearch/riemann (#891, 15 Sep 2026): "844 coarse brackets" = 427 + 417.

## 1. What is claimed

Two new extreme values of the argument S(t) = (1/π) arg ζ(½ + it), each with a Turing-method certificate:

| | height t | window | record |
|---|---|---|---|
| positive | t₁ = 763173730199776587433631628770 ≈ 7.63·10²⁹ | [t₁ − 20, t₁ + 20], 427 sign-change brackets of Z, width 0.002 | S(γ₁ + 0) ∈ (4.184313, 4.185380), γ₁ − t₁ ∈ [−.068203, −.068103] |
| negative | t₂ = 201016554543249943627430143193 ≈ 2.01·10²⁹ | [t₂ − 20, t₂ + 20], 417 brackets | S(γ₂ − 0) ∈ (−4.33869, −4.33837), γ₂ − t₂ ∈ [.078398, .078428] |

N(t₁) = 8012833507866431746081933196518; N(t₂) = 2067863069844908517322813360229. Turing data:
t₁: I₊ = .2506382, I₋ = .4650477, B = 6.1266298, E₊ = .210, E₋ = .217, D ∈ [−.3404339, .3042996] ⇒ D = 0;
t₂: I₊ = −.8865458, I₋ = .1980195, B = 6.0479180, E₊ = .212, E₋ = .205, D ∈ [−.3225469, .3573232] ⇒ D = 0.
Previous record quoted by the poster: 3.3455 (2016) — the Bober–Hiary value the program already carries
(directions/D1 item 4: "|S(t)| ≈ 3.3455 at t ≈ 7.75·10²⁷"). The larger new value in absolute terms is
the NEGATIVE one, |S| > 4.3383.

## 2. What was checked here, and what was not

**Checked (this session, `theta-check.py`, mpmath at 60 digits, exact Riemann–Siegel θ via log Γ):**
N(t) − θ(t)/π − 1 at the bracket endpoints reproduces the poster's S intervals to every printed digit:

    t1: log(t/2π) = 66.9694; S(t1) = 3.4584371; at γ endpoints 4.1853796 / 4.1843138
    t2: log(t/2π) = 65.6353; S(t2) = −3.5194107; at γ endpoints −4.3383706 / −4.3386839

So the posted N(t) values and the posted S claims are mutually consistent, and the bracket lists show
no zero between γ and t (t₁: brackets at −.0691 and +.3012; t₂: −.4593 and +.0775), as the reading requires.

**Not checked (and not checkable from the post):** the interval evaluations of Z at height 10²⁹–10³⁰
(the 844 sign brackets and the two record brackets with |Z| ≈ 2·10⁻⁵), the Turing integrals, and the
software that produced them. Label for any program use: **[external, sponsor-delivered; N/S arithmetic
verified; Z evaluations and Turing integrals unverified]**. Standing order 5 applies: no sentence in a
paper may rest on it until the producer's method is on disk and read.

## 3. Relevance to the program — three touchpoints, none load-bearing

**(a) D1, item 4 (the Farmer carrier-wave ceiling) — a record figure to update, dated insertion only.**
The file quotes the observed record |S(t)| ≈ 3.3455 at t ≈ 7.75·10²⁷ (Bober–Hiary). It is now
|S| > 4.3383 at t ≈ 2.01·10²⁹ and S > 4.1843 at t ≈ 7.63·10²⁹. The argument the figure serves is
unchanged: Odlyzko's anchor is S(t) routinely larger than 100; a move from 3.3 to 4.3 at 10²⁹ is the
√(½ log log t) growth doing what it should (√(½ log log 10²⁹) ≈ 1.45; the record is ≈ 3σ of the
Selberg CLT scale) and changes nothing in the honest prior that headlines D1.

**(b) D1 M3 ledger, §4.2(1) and the reserved `turing` grade — the entry format D1 said did not exist now
exists in the wild.** The pricing (`results/d1-m2a/dr8/PRICING-M3-ledger.md`) records that RH-in-a-range
needs a Turing-method zero count that the W1 box format does not carry, and reserves grade `turing`
"until such an entry format exists". Eisenberg's certificate is exactly that format: an exact N(T)
anchor, a complete list of sign-change brackets of Z across a window, the Turing integrals with error
terms, and an integer discrepancy D forced into an interval of width < 1 around 0 — hence "every zero
with imaginary part in [T − 20, T + 20] is simple and on the critical line". Two consequences and one
non-consequence:
  - it is a **template** for the `turing` grade if D1 is ever reopened (fields: anchor N(T), bracket list
    with widths, I±, B, E±, D-interval, and the Z-evaluation method with its error bound);
  - it shows certified Turing windows at 10²⁹–10³⁰, seventeen orders above the contiguous record and
    far above the ledger's own Arb practical ceiling (≈ 10¹⁵ per row), which the pricing already
    anticipated by citing the Bober–Hiary heights;
  - it does **not** move the rigorous contiguous verification record: that stays 3·10¹² (Platt–Trudgian).
    A window is not a range. The M3 "rows" NO-GO stands for its own three reasons.

**(c) C2, Theorem R1 (Sector-I confinement), clauses 4–5 — a calibration point, not an input.** Clause 5
consumes explicit UPPER bounds |S(t)| ≤ c₁ log t + c₂ log log t + c₃; the record is a lower-bound data
point and touches no constant (the 66.41 unconditional layer constant and the 4 at mean density stand).
The note's heuristic ε = O(sup|R|/ℓ) can now be read against the worst known point:
|S|/log(t/2π) ≈ 4.34/65.6 ≈ 0.066 at t₂ and 4.18/67.0 ≈ 0.062 at t₁ — i.e. the local density
deviation at the most extreme height ever examined is a few percent of ℓ/2π, consistent with clause 4's
(1 − ε) hypothesis being mild in practice. Illustrative only; clause 4 is a theorem conditional on the
window minimum of Ψ and uses nothing else.

**What it is not.** Not evidence for or against RH (the poster's title is a joke on the word "argument");
not a new route; not a change to any barrier, constant, no-go or paper; not a change to the Session 22
queue beyond the watch line below.

## 4. Actions taken (2026-09-15)

1. This directory: `ASSESSMENT.md`, `theta-check.py`, `theta-check.out`.
2. `directions/D1-certified-refutation-arm.md` item 4: dated insertion superseding the 3.3455 figure.
3. `results/d1-m2a/dr8/PRICING-M3-ledger.md`: no edit (immutable phase output); the pointer lives here
   and in STATUS.
4. STATUS.md: one watch line under the Session 22 queue; LOG.md: one FYI entry.
