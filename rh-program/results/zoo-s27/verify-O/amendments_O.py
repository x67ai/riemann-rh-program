#!/usr/bin/env python3
"""Reader (Opus 5), zoo-s27: the EXACT amendments of results/zoo-s27/zoo-entries-read-O.md, machine-readable.
Each is (block, old, new): `old` must occur exactly once inside the named block of the proposed file.
Run: python3 amendments_O.py CHECK   -> asserts every `old` once, applies all to a scratch copy
     (results/zoo-s27/verify-O/proposed-amended-O.md), lints the new text, and prints the SHA-256.
It never writes the proposed file itself; the orchestrator applies the same pairs verbatim."""
import hashlib, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
PROP = ROOT / "results/zoo-s27/zoo-entries-proposed.md"
OUT = ROOT / "results/zoo-s27/verify-O/proposed-amended-O.md"
DM = "`[dual-model check, 2026-09-25: Opus reader, results/zoo-s27/zoo-entries-read-O.md]`"
AM = [
 # A1, A2 -- the packaging-label flip in the byte-identity-locked D3 blocks (with the stale "until" clause dropped)
 ("i5", "no sign test\" is `[novelty: single-check]` until this stream's Opus reader has read the note.",
        "no sign test\" is " + DM + "."),
 ("iv4", "The packaging sentence is `[novelty: single-check]` until this stream's Opus reader has read the note.",
         "The packaging sentence is " + DM + "."),
 # A3-A6 -- block ra
 ("ra", "On every printed doubled object for Spec Z that carries any pairing at all, the pairing is DEFINED",
        "On every printed doubled object for Spec Z named in the pool P1–P9 or by either scout that carries any pairing at all, the pairing is DEFINED"),
 ("ra", "X = spec Z ∏_{F[±1]} spec Z",
        "X = spec Z̄ ∏_{F[±1]} spec Z̄ (the compactified spec Z, overlined on the page)"),
 ("ra", "concerning the spectrum of that operator\"",
        "concerning the spectrum of that operator\" (an axiomatic intersection theory for a Hilbert-space operator, not a scheme; the zeros enter as that operator's spectrum)"),
 ("ra", "the packaging of this rider is `[novelty: single-check]` until this stream's Opus reader has read it.",
        "the packaging of this rider is " + DM + "."),
 # A7, A8 -- block ra_ptr
 ("ra_ptr", "— the prime-computable observable IS the classical Weil test with multiplier 1 on every band (s(f, f) = N(f ⋆ f̃) with N the explicit-formula distribution; ⟨f, g⟩ = W(f ∗ g*)),",
            "— the pairing IS the classical Weil test with multiplier 1 on every band wherever it has a prime side (s(f, f) = N(f ⋆ f̃) with N the explicit-formula distribution; ⟨f, g⟩ = W(f ∗ g*)); Haran's (8.7.7) is the zero side of the same explicit formula, and Banaszak–Uetake's theory is axiomatic on an operator's spectrum, with no prime side —"),
 ("ra_ptr", "`[the pair's agreed close; packaging novelty: single-check]` until this stream's Opus reader has read it.",
            "`[the pair's agreed close; packaging dual-model check, 2026-09-25: Opus reader, results/zoo-s27/zoo-entries-read-O.md]`."),
 # A9-A16 -- block rb
 ("rb", "for all j ≥ 1 and all primes p\". Write Γ_n",
        "for all j ≥ 1 and all primes p\"; since Z is torsion-free this ring is W(Z), the classical big Witt vectors (§1.15, p. 12: with E all the maximal ideals of Z, \"W agrees with the classical big Witt vector functor\"). Write Γ_n"),
 ("rb", "re-verified from (1.10) by this stream's writer]`",
        "re-verified from (1.10) by this stream's writer; re-derived a third time by the Opus reader — the ghost lattice on indices ≤ N has the Z-basis v_d = (d·[d | n])_{n≤N}, d ≤ N (each v_d satisfies (1.10); determinant N! = the index fixed by (1.10)), so I_n = gcd{d : d | n, d > 1}·Z for every n, and 4 000 random big-Witt vectors pushed through the ghost map w_n = Σ_{d|n} d·x_d^{n/d} give gcd(w₁ − w_n) = e^{Λ(n)} at every n ≤ 40, 11 and 13 included (results/zoo-s27/verify-O/witt_diag_O.py and its _run.log)]`"),
 ("rb", "the convention under which log p enters every Arakelov intersection number (III.21), not by hand insertion",
        "the convention under which the closed point (p) has arithmetic degree log p (Durov, arXiv:0704.2030, p. 63: CH¹(Spec Ẑ) = log Q*₊ = Pic(Spec Ẑ), deg the \"arithmetic degree\"; Kapranov–Smirnov's \"the degree of (p) should be log(p)\", as Le Bruyn, arXiv:1304.6532, p. 2, records it), not by hand insertion"),
 ("rb", "glued at closed points (0801.1691 p. 10; in print as geometry in",
        "glued at closed points (0801.1691 p. 5, Figure 1: \"Spec W₁(A) … is two copies of Spec A glued along Spec A/pA. This is also true as schemes if we assume that A is p-torsion free\"; 1006.0092 p. 5: W₁*(X) is the coequalizer of X₀ ⇉ X ∐ X, and \"the space W_n*(X) can be constructed by gluing n+1 copies of X together … along their fibers modulo p, …, pⁿ\"; in print as geometry in"),
 ("rb", "Prop. 16.5(d), W_n* preserves Krull dimension",
        "Prop. 16.5(d), p. 31, W_n* preserves Krull dimension"),
 ("rb", "and Thm. 17.3, single-ideal case,",
        "and Thm. 17.3, p. 39, single-ideal case,"),
 ("rb", "— NOT FOUND in print: `[novelty: single-check — the writer's search, 2026-09-25; the Opus reader's independent search decides the dual-model label]`. Nearest published objects (10(n)): Borger's own hope,",
        "— and independently by the Opus reader (Borger's three papers re-fetched and read in full text; Connes–Consani 1103.4672 and 1502.05580; Manin 0809.1564; López Peña–Lorscheid 0909.0069; Jeffries 2311.13551; web searches — `results/zoo-s27/zoo-entries-read-O.md` §4). The case n = p IS in print, as geometry and without the words \"degree\" or \"Λ\": Borger 0801.1691 p. 5, Figure 1 (for A p-torsion free, Spec W₁(A) is two copies of Spec A glued transversely along Spec A/pA — for A = Z the ghost components Γ₁ and Γ_p meet in Spec F_p, of degree log p) and 1006.0092 p. 5 (W₁*(X) the coequalizer of X₀ ⇉ X ∐ X) `[printed: Borger 0801.1691 p. 5, Fig. 1; 1006.0092 p. 5 — the case n = p]`. The statement for every n ≥ 2 on the big Witt vectors — degree log p at every prime power p^k (not the k·log p of the printed chain \"Spec W_n(A) as Spec W_{n−1}(A) glued with Spec A along Spec A/pⁿA\", which measures the new copy against the whole previous union), empty intersection at every n with two distinct prime factors, i.e. deg(Γ₁ ∩ Γ_n) = Λ(n) — is NOT FOUND in print by either search: `[novelty: dual-model check, 2026-09-25: the writer's finding 7 and the Opus reader's §4, results/zoo-s27/zoo-entries-read-O.md]`. Nearest published objects (10(n)): Borger 0801.1691 p. 5, Figure 1 and 1006.0092 p. 5 (the case n = p, above); Borger's own hope,"),
 ("rb", "decide which steps live on S ×_{F₁^S} S = W_S*(S) rather than on S ×_k S",
        "decide which steps live on S ×_{F₁^S} S = W_S*(S) (the Λ_S analog of p. 7's definition, inferred; pp. 4–5 print the Λ_S-structure and the translation task, not this equation) rather than on S ×_k S"),
 ("rb", "The packaging of this rider is `[novelty: single-check]` until this stream's Opus reader has read it.",
        "The packaging of this rider is " + DM + "."),
]

def blk(t, k):
    a = t.index("<!-- BLOCK:%s -->" % k); b = t.index("<!-- END:%s -->" % k, a); return a, b

if __name__ == "__main__":
    t = PROP.read_text(encoding="utf-8")
    print("proposed SHA-256", hashlib.sha256(t.encode()).hexdigest())
    for i, (k, old, new) in enumerate(AM, 1):
        a, b = blk(t, k)
        body = t[a:b]
        n = body.count(old)
        assert n == 1, ("A%d" % i, k, n, old[:60])
        t = t[:a] + body.replace(old, new) + t[b:]
        for bad in ("clearly", "obviously", "easy to see", "well known", "well-known"):
            assert bad not in new.lower(), ("lint", i, bad)
    OUT.write_text(t, encoding="utf-8")
    print("applied %d amendments -> %s ; SHA-256 %s" % (len(AM), OUT.name, hashlib.sha256(t.encode()).hexdigest()))
