# Session 36 (2026-09-30), orchestrator: apply the Opus reader's 29 OLD/NEW pairs (amendments.py) to NOTE.md,
# then the orchestrator's own dated insertions made while re-deriving the FIX-FIRST pairs at the line.
# Writes NOTE.md in place; NOTE.pre-reader.md is the untouched writer's copy (17717f15...).
import sys, os, hashlib
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
from amendments import A
src = os.path.join(here, '..', 'NOTE.md')
t = open(src, encoding='utf-8').read()
h0 = hashlib.sha256(t.encode()).hexdigest()
assert h0 == '17717f151638618ab6f026d896cc632c955ce6c0c1db6cf4c60ff2a25eb0aff5', h0
u = t
for i, kind, n, old, new in A:
    assert u.count(old) == n, (i, u.count(old), n)
    u = u.replace(old, new)
h1 = hashlib.sha256(u.encode()).hexdigest()
print('after the reader\'s 29 pairs:', h1)
assert h1 == 'c19e3446ce08ce2d34d162df7bd79c5ae97bce7a5f07ef43f2afee8edc114b73', h1

O = []
O.append(('O1', 1,
 "(i) n = pq, p ≠ q primes: L = Λ(pq) = 0, so",
 "(i) n = pq, p ≠ q primes: L = Λ(pq) = 0 [ORCHESTRATOR'S PRECISION at application, Session 36, 2026-09-30: this equality needs the fiber of c(Γ_{pq}) to contain no prime-power component — more than (H-inj) as worded above, which is injectivity on the prime-power components only; in route (b) read (H-inj) as \"φ injective on all of M\" (which a degree clause d(φ_n) = n gives). Route (a) uses only the prime-power form. Theorem R and T3 are untouched.], so"))
O.append(('O2', 1,
 "is what (D4) must break — the rank goes to infinity while the intersection numbers, including (Δ · Δ)_Y, stay finite real numbers.",
 "is what (D4) must break — the rank goes to infinity while the intersection numbers, including (Δ · Δ)_Y, stay finite real numbers. [ORCHESTRATOR'S FLAG at application, Session 36, 2026-09-30 — ERRATUM E11 candidate, `[single-check → the Session-36 unit's reader]`: this sentence, and A8′'s \"δ_B a finite real number not coupled to the rank\" below, are inconsistent with a Castelnuovo–Severi inequality on any real quadratic space containing the classes of Δ and the Γ_{φ_n} whenever the fibers of c over c(Γ_p) and c(Γ_{p²}) are singletons on prime powers (in particular under a degree clause d(φ_n) = n): with 2g := 2 − (Δ · Δ)_Y and x := d_p, the two inequalities (1 + x − log p/κ)² ≤ 4g²x and (1 + x² − log p/κ)² ≤ 4g²x² force log p ≤ κ(1 + 2g)(1 + r_g), r_g := (1 + √(1 + 8g))/2, for EVERY prime p — so (Δ · Δ)_Y is not a real number there, and the rank–degree coupling is not broken in (D4) but persists as ∞ = ∞. Derivation, the rung-1 check and the consequences for A8′/A13′ are the Session-36 unit `results/d4-infty-s36/` (Theorem S). Until that unit is read, A8′ is NOT inserted into the SPEC.]"))
O.append(('O3', 1,
 "- *A8′ (PRECISION on A8):* OLD",
 "- *A8′ (PRECISION on A8) — [HELD at application, Session 36, 2026-09-30: see the orchestrator's flag in §3.1 (ERRATUM E11 candidate) and `results/d4-infty-s36/`; not inserted into the SPEC as worded]:* OLD"))
for i, n, old, new in O:
    assert u.count(old) == n, (i, u.count(old), n)
    u = u.replace(old, new)
u = u.replace("*(β-shapes NOTE, writer Fable 5.1, Session 35. Pre-reader copy. U.S. English.)*",
 "*(β-shapes NOTE, writer Fable 5.1, Session 35; Opus 5 reader's 29 OLD/NEW pairs (F1–F14, M1–M12) applied by the orchestrator on 2026-09-30, Session 36, each FIX-FIRST re-derived at the line first (`verify-O/apply_s36.py`); three orchestrator's dated insertions O1–O3 at application. The writer's untouched copy is `NOTE.pre-reader.md`. U.S. English.)*")
for bad in ('at least two residue characteristics', '≥ 2 residue characteristics'):
    # F1's NEW text itself says "two residue characteristics do not make Theorem R bite" — allowed; the two wrong phrases must be gone
    assert bad not in u, bad
open(src, 'w', encoding='utf-8').write(u)
print('NOTE.md written:', hashlib.sha256(u.encode()).hexdigest(), 'lines', u.count('\n'))
