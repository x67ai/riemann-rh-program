#!/usr/bin/env python3
"""p23_diff.py -- fidelity (r2) / stop line (b) of Unit B: the Lean definitions gammaPoly, Prelax, P2, P3, F13 of
comparator/ChallengeDeps/Separation5.lean (Zeta23/Separation/Clause5.lean has the same text), transcribed here term for term
(each Python line is annotated with the Lean text it transcribes), evaluated at L = 50, 100, 10^3, 10^4 and diffed against
r0_73_check.py lines 22-33 (gamma_poly, P_relaxed, Ftilde), whose source text is exec'd verbatim from the file.
Run from results/c2-m4/verify-B/.  Constants c_B, C_B, b1 as r0_73_check.py reads them (lemma_G_constants_out.json,
b1_constant_out.json); b1sym = (2 e^{-1}/Z)^2 with Z from b1_constant_out.json for the Lean F13 (Unit A's symbolic b1)."""
import json, sys, re
import mpmath as mp
mp.mp.dps = 40
V2 = "../../c2-m2/verify/"
gj = json.load(open(V2 + "lemma_G_constants_out.json")); bj = json.load(open(V2 + "b1_constant_out.json"))
cB = mp.mpf(gj["c_B"]); CB = mp.mpf(gj["C_B"]); b1 = mp.mpf(bj["b1_certified_upper"]); Z = mp.mpf(bj["Z"])
b1sym = (2 * mp.exp(-1) / Z) ** 2
# --- the record's functions, exec'd verbatim from r0_73_check.py lines 22-33 ---
src = open(V2 + "r0_73_check.py", encoding="utf-8").read().split("\n")
record_text = "\n".join(src[21:33])
print("r0_73_check.py lines 22-33, exec'd verbatim:\n" + record_text + "\n")
exec(record_text)
# --- the Lean definitions, transcribed term for term ---
def gammaPoly(n, a, s):
    # def gammaPoly (n : ℕ) (a s : ℝ) : ℝ := ∑ j ∈ Finset.range (n + 1), (n.factorial : ℝ) / (j.factorial : ℝ) * s ^ j / a ^ (n + 1 - j)
    return mp.fsum(mp.mpf(mp.factorial(n)) / mp.mpf(mp.factorial(j)) * s ** j / a ** (n + 1 - j) for j in range(n + 1))
def Prelax(m, L):
    L = mp.mpf(L)
    # def Prelax (m : ℕ) (L : ℝ) : ℝ :=
    #   (1 + 3 / (2 * (73 * 50 - 1))) ^ m * CB ^ 2 *
    #     ((73 * L) ^ m * (1 + cB / 2 * (Real.sqrt 73 * L)) ^ 2 +
    #       2 / L ^ (m + 1) * (gammaPoly (2 * m + 1) (2 * cB) (Real.sqrt 73 * L) + cB * gammaPoly (2 * m + 2) (2 * cB) (Real.sqrt 73 * L)
    #         + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) (Real.sqrt 73 * L)))
    return (1 + mp.mpf(3) / (2 * (73 * 50 - 1))) ** m * CB ** 2 * (
        (73 * L) ** m * (1 + cB / 2 * (mp.sqrt(73) * L)) ** 2 +
        2 / L ** (m + 1) * (gammaPoly(2 * m + 1, 2 * cB, mp.sqrt(73) * L) + cB * gammaPoly(2 * m + 2, 2 * cB, mp.sqrt(73) * L)
                            + cB ** 2 / 4 * gammaPoly(2 * m + 3, 2 * cB, mp.sqrt(73) * L)))
def P2(L): return Prelax(2, L)   # def P2 (L : ℝ) : ℝ := Prelax 2 L
def P3(L): return Prelax(3, L)   # def P3 (L : ℝ) : ℝ := Prelax 3 L
def F13(L, b):
    L = mp.mpf(L)
    # def F13 (L : ℝ) : ℝ := (13 / 8 - 2 * cB * Real.sqrt 73) * L + 2 * cB / Real.sqrt 73 + Real.log ((105 / 100 * P2 L + P3 L) / b1sym)
    return (mp.mpf(13) / 8 - 2 * cB * mp.sqrt(73)) * L + 2 * cB / mp.sqrt(73) + mp.log((mp.mpf(105) / 100 * P2(L) + P3(L)) / b)
ok = True
print(f"constants: c_B = {mp.nstr(cB, 12)}, C_B = {mp.nstr(CB, 12)}, b1 (record, certified upper) = {mp.nstr(b1, 8)}, b1sym = (2e^-1/Z)^2 = {mp.nstr(b1sym, 8)} (Z = {mp.nstr(Z, 12)})")
for L in (50, 100, 1000, 10000):
    for m in (2, 3):
        a = Prelax(m, L); b = P_relaxed(m, L, 73, 50)
        rel = abs(a - b) / abs(b)
        ok &= rel < mp.mpf('1e-30')
        print(f"L = {L:6d}  P_{m}:  Lean-transcription = {mp.nstr(a, 20)}   r0_73_check = {mp.nstr(b, 20)}   |rel diff| = {mp.nstr(rel, 3)}")
    fa = F13(L, b1); fb = Ftilde(L, 73, 50, mp.mpf(13) / 8)
    ok &= abs(fa - fb) < mp.mpf('1e-25')
    print(f"L = {L:6d}  F13 at the record's b1: Lean-transcription = {mp.nstr(fa, 15)}   r0_73_check Ftilde = {mp.nstr(fb, 15)}   diff = {mp.nstr(fa - fb, 3)}")
    print(f"L = {L:6d}  F13 at b1sym (the Lean F13): {mp.nstr(F13(L, b1sym), 15)}   (= record value - log(b1sym/b1) = {mp.nstr(fb - mp.log(b1sym / b1), 15)})")
print(f"decrease threshold 5/(2 c_B sqrt 73 - 13/8) = {mp.nstr(5 / (2 * cB * mp.sqrt(73) - mp.mpf(13) / 8), 8)}")
print("RESULT:", "PASS -- P2, P3 and F13 agree term for term at all four values of L" if ok else "FAIL")
sys.exit(0 if ok else 1)
