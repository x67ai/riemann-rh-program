# read-F — the orchestrator's read at the line of `results/fejer-form-s39/NOTE.md` (Fable 5.1, Session 40, written 11:28 IST 2026-10-01)

NOTE read: SHA-256 3ad9a31e775ccece… (330 lines): §0 and §3 (Theorem W and the LP computation) whole at the line; §4 (Theorem F, the transport), §5 (the disguise audit and the page citations), §6 (the Z side), §7 (Theorem K), §11 (the proposed zoo riders) left to the Opus reader (`read-O.md`, in flight), whose targets (a)–(e) cover them, including the census recount and the three page checks. Pairs are applied only after reconciliation.

**VERDICT LINE: AGREES on the close K ("found nothing new, correctly"): the separating rung-1 inequality is Weil's bound. Theorem W re-derived; the two decisive numbers and V's closed form recomputed by hand. No FIX-FIRST from this side.**

## 1. Re-derived at the line
- **Theorem W(i)** ✓: N_n = qⁿ + 1 − q^{n/2}Σ_j 2cos nθ_j, so q^{−n/2}(qⁿ + 1 − N_n) = p_n and c₀g + Σc_n p_n = Σ_j f_c(θ_j); an affine functional vanishing at P¹ is of this form. **(ii)** ✓: x*T_M x = ℓ_Z(|P_x|²), Fejér–Riesz, so λ_min(T_M) is twice the minimum of I_c over nonnegative cosine polynomials of mean 1; **(iii)** ✓.
- **By hand:** V (q = 5, L = 1 − 5u + 5u², N₁ = 1): I = 1 − 5/(2√5) = 1 − √5/2 = −0.11803 ✓; E₀ (N₁ = 2): I = 1 − 4/(2√5) = +0.10557 ✓; V's angle θ = iy, e^y = φ gives p_n = φⁿ + φ⁻ⁿ, T_M = uvᵀ + vuᵀ, λ_min = (M + 1) − |u||v|; at M = 1: |u|²|v|² = (1 + φ⁻²)(1 + φ²) = 5, λ_min = 2 − √5 = −0.2361 ✓ (the printed first value).
- The reading "class (B) (nonnegative only at the genuine angles) uses RH plus integrality of the trace and is a refinement of the Weil test, not a new generator" is accepted as stated.

## 2. Independent computation
The census (4591 data; the 111) and the Z-side numbers are recounted by the Opus reader with its own code (targets (b), (d)); this side recomputed the three closed-form values above.

## 3. Minor
None from this side.

## 4. Close
K by theorem; UT-4 closed; the two riders of §11 go to the zoo stream after read-O's check against entries IV.1 and I.9.

## 5. Reconciliation with read-O (11:46 IST 2026-10-01)
read-O: AGREES-WITH-CORRECTIONS, 29 pairs (2 FIX-FIRST items of 7 pairs each; 9 minor items, 15 pairs). Both FIX-FIRST concern the wording of the close, which this side accepted as written — verified by hand before applying:
- **F1** ✓: from D_k = h(q^{g−1+k} − 1), on P¹ (g = 0, h = 1) D_k = q^{k−1} − 1 = 0, 4, 24 at q = 5 for k = 1, 2, 3; so 'equality exactly at genus 0' is a statement about D₁, and 'D_k > 0 on every zeta datum' needs 'of genus ≥ 1'.
- **F2** ✓: over F₅ the functional I = 17g/4 + N₁ − 6 vanishes at P¹, is ≥ g/4 > 0 on every genuine curve of genus ≥ 1 (Serre: N₁ ≥ q + 1 − g⌊2√q⌋ = 6 − 4g) and equals −3/4 on V; its f(θ) = 17/4 − 2√5 cos θ is negative at θ = 0 (4.25 − 4.472). So a separating affine inequality need not be a Weil test; Theorem W(ii) is correct as stated (separation from the Weil region), and the close's shorthand 'the separating ones are the Toeplitz cone' overreached. The boundary of the new inequality is the printed Weil–Serre bound, so stop line 2 still fires and K stands.
All 29 pairs applied; NOTE 3ad9a31e… → 0ab5f19e… (`NOTE.pre-reader.md` kept). The two zoo riders of §11 are accurate after F1, F2 and m9 (read-O checked them against the zoo's IV.1 and I.9 text by grep) and go to the zoo stream.
