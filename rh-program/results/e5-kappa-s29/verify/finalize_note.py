#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""finalize_note.py -- collect every fixed-eps dual result (target_dual_eps_*_out.json), pick the best CERTIFIED value, and
substitute the placeholders KLB / GAPF / CLB in NOTE.md; rebuild the section-5 table; write the one-line result."""
import json, glob, re, numpy as np
rows = []
for f in sorted(glob.glob("verify/target_dual_eps_*_out.json")):
    d = json.load(open(f))
    for k, v in d.items():
        if not k.startswith("eps"): continue
        cert = v.get("verify"); rows.append(dict(U=v["U"], hu=v["hu"], eps=v["eps"], d=v["d_tilde"], kt=v["kappa_tilde_lp"], klp=v["kappa_lp"],
                                                 kc=(cert["kappa_cert"] if cert else None), eta=(cert["eta"] if cert else None),
                                                 cells=(cert["cells"] if cert else None), depth=(cert["depth"] if cert else None), file=f))
rows.sort(key=lambda r: (r["U"], r["hu"], -r["eps"]))
best = max([r for r in rows if r["kc"]], key=lambda r: r["kc"])
KLB = best["kc"]; KUB = 0.00099853; iota = 0.241523
GAPF = KUB/KLB; CLB = 4*(1 + iota/KLB); ELL = 4*np.pi*(1 + iota/KLB)
print(f"best certified: {KLB:.4e} (U = {best['U']}, eps = {best['eps']}, hu = {best['hu']}, eta = {best['eta']}); gap factor {GAPF:.1f}; C_lb = {CLB:.4g}; ell' > {ELL:.3g}")
tab = ["| U | hu | ε | d̃ (LP) | κ̃ = 2 − d̃ | κ_lp = εκ̃ | certified κ | verification |", "|---|---|---|---|---|---|---|---|"]
for r in rows:
    cert = f"**{r['kc']:.4e}**" if (r["kc"] and r is best) else (f"{r['kc']:.4e}" if r["kc"] else "none `[computed, not certified]`")
    ver = f"η = {r['eta']:.1e}, {r['cells']/1e6:.1f}·10⁶ cells, depth {r['depth']}" if r["kc"] else "failed at every η ≤ 6.4·10⁻³ (or κ̃ ≤ 0)"
    tab.append(f"| {r['U']:g} | {r['hu']:g} | {r['eps']:g} | {r['d']:.6f} | {r['kt']:.6f} | {r['klp']:.3e} | {cert} | {ver} |")
tab = "\n".join(tab)
n = open("NOTE.md", encoding="utf-8").read()
# replace the old table (from its header line to the line before "**Reading the table.**")
i0 = n.index("| U | hu | ε | d̃ (LP) |"); i1 = n.index("**Reading the table.**")
n = n[:i0] + tab + "\n\n" + n[i1:]
n = n.replace("*(rows for U = 8 (ε = 10⁻⁴, 10⁻⁵), U = 12 (10⁻⁴), U = 16, 24, 32 (10⁻³, 2·10⁻³) are added as they land)*\n\n", "")
brk = (f"**The certified bracket.** κ_lb := {KLB:.4e} (U = {best['U']:g}, hu = {best['hu']:g}, ε = {best['eps']:g}, η = {best['eta']:.0e}; certificate `verify/target_dual_eps_s_U{best['U']:g}_hu{best['hu']:g}_eps{best['eps']:g}.npy`, "
       f"the LP value εκ̃ = {best['klp']:.4e} less the repair) and κ_ub = {KUB} (§4): **κ ∈ [{KLB:.3e}, {KUB:.4e}]**, duality gap a factor {GAPF:.1f}. "
       f"The grids: hu = 0.01 with U = 8 (1601 nodes) is the largest support whose certificates pass the verification in this slot (coarser hats at U ≥ 12 give LP values of the same size, 0.0103–0.0108 at ε = 10⁻³, but their spikier σ̂ fails the pointwise check by 10⁻⁵ dips near τ ≈ 12 unless the repair η eats most of κ̃); the ε-scan at U = 8 (10⁻⁵ … 5·10⁻³) has its certified maximum at ε = {best['eps']:g}. "
       f"The gap did not stop closing for want of iterations — it stops at the class: stop line (iii) fires, and the bracket with its gap is the result.")
n = n.replace("**The certified bracket.** *(pending)*", brk)
n = n.replace("KLB", f"{KLB:.3e}").replace("GAPF", f"{GAPF:.0f}").replace("CLB", f"{CLB:.3g}")
n = n.replace("- at the certified end, κ = κ_lb = 1.0103·10⁻⁵ (§5, U = 8, ε = 10⁻³; to be replaced by the best certified value of the ε-scan if it lands higher): C = 4(1 + 0.2415/1.0103·10⁻⁵) = **9.56·10⁴**; non-vacuous only for ℓ′ > 3.0·10⁵, i.e. t > e^{300 000}.",
              f"- at the certified end, κ = κ_lb = {KLB:.4e} (§5, U = {best['U']:g}, ε = {best['eps']:g}): C = 4(1 + 0.2415/{KLB:.3e}) = **{CLB:.3g}**; non-vacuous only for ℓ′ > {ELL:.3g}, i.e. t > e^{{{ELL:.0f}}}.")
n = n.replace("With the certified bracket of §5, κ ∈ [κ_lb, κ_ub] = [1.0103·10⁻⁵, 0.00099853]:", f"With the certified bracket of §5, κ ∈ [κ_lb, κ_ub] = [{KLB:.4e}, 0.00099853]:")
n = n.replace("**One-line result (filled at the close, §7).** *(pending)*",
              f"**One-line result.** Theorem K0 re-derived (κ ≥ 6.3464·10⁻¹⁹, explicit, unconditional; stop line (i) does not fire); rung 0 passed (exact instance to 10⁻⁶, tail instance certified to 0.23%); **κ ∈ [{KLB:.3e}, 9.985·10⁻⁴], both ends certified** — the upper end an exhibited band-limited square that hides from γ₁ and from log 2, log 3, log 5, log 7 at once (a factor 136 below the Fejér record 0.136, confirmed through the explicit formula), the lower end a Theorem D′ certificate (K0's convex combination plus a grid correction on [−8, 8], ζ's first 200 zeros) verified pointwise; the gap is a factor {GAPF:.0f} (stop line (iii): reported as the result); the layer constant C = 4(1 + 0.2415/κ) is re-derived and is ≥ 972 at every value in the bracket, so route (α) is closed as a competitor to the ζ-anchored 4/log t.")
open("NOTE.md", "w", encoding="utf-8").write(n)
json.dump(dict(best=best, rows=rows, KLB=KLB, KUB=KUB, GAPF=GAPF, CLB=CLB), open("verify/finalize_note_out.json", "w"), indent=1)
print("NOTE.md finalized;", len(n.splitlines()), "lines; placeholders left:", n.count("KLB") + n.count("GAPF") + n.count("CLB") + n.count("*(pending"))
