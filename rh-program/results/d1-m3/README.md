# M3 exclusion ledger — `results/d1-m3/` (seeded 2026-09-10, Session 20)

**What this directory is.** The program's durable register of certified ζ-exclusion boxes: each row is one closed box R = [σ₁, σ₂] × [T₁, T₂] with ½ < σ₁ ≤ σ₂ < 1 in which ζ has no zero, kernel-checked modulo the displayed hypothesis H-ENCL, carried by TWO W1 exclusion transcripts (one per independent producer leg). Pricing and format of record: `results/d1-m2a/dr8/PRICING-M3-ledger.md` (§1 the row, the layout, the index; §4 what a row licenses and can never certify). Seeded by the D-R8/M3-seed build (`results/d1-m2a/dr8/BUILD-NOTES-fDH.md` §2) with the four M1 v1 acceptance null boxes — zero producer compute, every verdict already on disk and dated.

## Charter and honesty clause (quoted verbatim from `directions/D1-certified-refutation-arm.md`)

Charter, milestone ladder item 3:

> 3. **Exclusion ledger.** Every search-negative window becomes a **certified exclusion region** (RH verified in that box, machine-checked at the transcript level) — recorded in a durable ledger under `results/`. The poster tells us these negatives are exactly where they carry information (the only regime a counterexample could occupy).

D-R6:

> - **D-R6 (M3 ledger honesty):** every ledger entry records (window, certified depth floor δ₀); claims read "no zeros with Re ≥ 1/2 + δ₀ in W," never "RH verified in W" (a σ₁ > 1/2 box is structurally blind to the poster's own shallow δ ≲ 1/log γ regime; cost of δ₀ → 1/log γ boxes must be priced before M3 is funded). Delete the honesty-section "every classical conditional result inherits the improvement" clause — isolated boxes extend no contiguous record, and contiguous extension is outside the local-compute policy. Turing-method-grade entries marked separately.

Note on the charter's parenthesis "(RH verified in that box …)": D-R6 supersedes that wording. A row says "no zeros of ζ in the closed box"; it never says "RH verified" (see "What a row licenses").

## The licensed label, and the v1.0 string inside the transcripts

**Label, per row (binding):** *"no zeros of ζ in the closed box [σ₁, σ₂] × [T₁, T₂] — kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)"* — the v1.1 label of `lean/README.md` ("Honest label, binding"), since H-AP was discharged on 2026-09-02 (`Zeta23.W1.cert_of_checkW1_ap`). Every on-disk ζ transcript still carries the schema-fixed v1.0 string `kernel-checked modulo displayed hypotheses H-ENCL and H-AP (producers untrusted)` in its `trust_label` field: an accepted transcript is never edited (its hash is its identity), so the row carries the LICENSED label in its own `trust_label` and records the embedded v1.0 string in `legs.<leg>.embedded_trust_label`. The tension is resolved contract-side whenever `FORMAT.md` is bumped. (The f_DH label was amended on 2026-09-10 by the D-R8 build — a different function, not a ledger matter: f_DH transcripts are never rows.)

## What a row licenses — and the single-box sentence rule

For each leg's literal `d` (`lean/Zeta23/W1/Instances.lean`), the row's theorem is the m = 0 branch of `cert_of_checkW1_ap` instantiated in `lean/Zeta23/W1/Ledger.lean`:

    theorem <name>_exclusion (hEncl : W1EnclOK riemannZeta <name>) : ∀ s ∈ W1Rect <name>, riemannZeta s ≠ 0

— two legs, two theorems, two displayed hypotheses, never merged (D-R3). `#print axioms`: `[propext, Classical.choice, Quot.sound]` (`results/d1-m2a/dr8/fdh-axioms.log`). The `_check` theorems (`checkW1Floor … = true` by `decide +kernel`, `[propext]`) are the kernel facts about the literals; the back-parse `results/d1-m1/recon_instances_verify.py` ties the literals to the JSON (untrusted script, 0 mismatches).

**Single-box rule (PRICING §4.1).** D-R6's range form "no zeros with Re s ≥ ½ + δ₀ in [T₁, T₂]" is licensed only when a family of boxes covers [σ₁, 1) × [T₁, T₂] and the classical nonvanishing on Re s ≥ 1 (Mathlib `riemannZeta_ne_zero_of_one_le_re`) closes the gap. A single row's box stops at σ₂ < 1, so its licensed sentence is the BOX sentence — `sentence` in `ROW.json` — and `delta0` is recorded for the day a family exists; `delta0_form` spells out the honest single-box reading ("Re s ≥ ½ + δ₀ AND Re s ≤ σ₂"). (PRICING §1.4's example sentence used the range form; §4.1 corrected it; the seed follows §4.1.)

## What the ledger can never certify (PRICING §4.2, binding)

* **RH in a range** — not even with a tiling: C2 keeps σ₁ > ½ strictly and C6 fails on an edge through an on-line zero, so the strip ½ < Re s < ½ + δ₀ is never touched; a range statement needs a Turing-method zero count the format does not carry (grade `turing` is reserved and refused by `ledger-schema.json`). In particular the ledger can never discharge M2a's H1.
* **Λ > 0** (a row is m = 0), nor any bound on Λ.
* **Anything about ζ outside the boxes**: no aggregate field exists (schema-enforced); isolated boxes extend no contiguous record; the rigorous verification record stays 3·10¹² (Platt–Trudgian) whatever the ledger holds.
* **Anything about a claimed counterexample it did not box.**
* It creates **no barrier-zoo entry** (PRICING §4.3).

**The four seed rows are worth exactly this:** all four boxes lie far below 3·10¹², so as facts about ζ they are known; their value is that they are the program's OWN certificates in its own trust vocabulary (two independent untrusted producers, one kernel) and the ledger's format-validation rows — the role the acceptance suite played for the checker. Nobody should mistake four boxes below height 10⁴ for a verification result.

## Provenance kinds (`provenance.kind`; the poster names no box — PRICING §1.1)

`acceptance` (M1 null tests: instrument-validation boxes chosen for the cost curve, not by any prior) · `calibration` (boxes chosen to measure cost at a height) · `prior` (a box chosen by a search PRIOR the direction file names — Stopple's Lehmer-pair statistics near t = 10⁶, Bober–Hiary windows — with the prior cited) · `pointer` (a box aimed by a detector hit or an external claim that passed the claim screen, with the screen record cited). "Poster-guided" means the poster's PROFILE is what a `pointer` box is screened against; it is never a source of coordinates.

## Status values

`accepted` (both legs, both Python checkers ACCEPT, kernel `_check` per leg, cross-check CONSISTENT — enforced by `ledger_check.py`) · `one-leg` (one leg only; NOT citable in any sentence — FORMAT §8.1: the two-producer cross-check is the only detector of the checker's blind spots) · `pending`.

## Layout

    README.md            this file
    LEDGER.md            human-readable, APPEND-ONLY, one dated line per row
    index.json           machine-readable index = the ROW.json records sorted by (height, δ₀, row_id); regenerated by ledger_check.py, never hand-edited
    ledger-schema.json   JSON Schema 2020-12 for index.json (shape only)
    ledger_check.py      UNTRUSTED validator (re-hashes, re-runs both Python checkers and crosscheck.py, checks the Lean names and records, recomputes entry_sha256, regenerates index.json; exit nonzero on drift)
    seed_rows.py         the one-off seed generator (2026-09-10); later rows are added by the checklist below, not by this script
    rows/<row_id>/ROW.json        the row record (canonical; one index entry)
    rows/<row_id>/PROVENANCE.md   prose provenance, the sentence, the added-by/when stamp
    rows/<row_id>/REFS.txt        SHA-256 pointers to the transcripts and logs under results/d1-m1/ (seed rows POINT, they do not copy: the acceptance suite stays the single source of truth the Instances.lean back-parse was verified against); a new row copies its two transcripts and three logs into its directory instead

Row id (filesystem-safe, content-determined): `zeta_<σ₁>_<σ₂>_<T₁>_<T₂>`, each rational as `num-den` (integers as themselves). Two rows on one box are a versioning error, not two rows. `entry_sha256` = SHA-256 of the record serialized by `json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=False)` with `entry_sha256` set to `""`.

## How a row is added (every step is one command already on disk except the two Lean corollaries)

1. both producers on the box (`results/d1-m1/producer_mp.py`, `producer_arb.py`; mode `exclusion`) → 2. both Python checkers ACCEPT (`reference_checker.py`, `checker_ref.py`) → 3. `acceptance/crosscheck.py` CONSISTENT (a disjoint pair proves one leg's H-ENCL false: stop-the-line) → 4. `validate_arb_transcripts.py` (evidence, not certificate) → 5. emit the two Lean literals + `_check` theorems (`emit_lean.py`), build, back-parse (`recon_instances_verify.py`) → 6. the two 3-line corollaries in `Zeta23/W1/Ledger.lean`, `#print axioms` → 7. `rows/<row_id>/{ROW.json, PROVENANCE.md}` + copies of the transcripts and logs, hashes into `ROW.json` and `LOG.md` (KICKSTART 10(i)) → 8. `python3 ledger_check.py --write` then `python3 ledger_check.py` → 9. one line in `LEDGER.md` → commit.

## Never say

"RH verified in W" · "RH verified up to T" · "total height covered" · "the record inherits the improvement" · "fully machine-checked" · a `turing`-grade entry · a sentence from a `one-leg` row · anything about ζ outside a row's box · anything about Λ.
