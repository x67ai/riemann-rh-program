#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""repatch_note.py -- after finalize_note.py: if a higher CERTIFIED value has landed, replace the formatted numbers in NOTE.md
(kappa_lb, gap factor, C at the certified end, the ell' threshold) and rebuild the section-5 table."""
import json, glob, numpy as np
old = json.load(open("verify/finalize_note_out.json")); KLB0 = old["KLB"]; GAPF0 = old["GAPF"]; CLB0 = old["CLB"]; best0 = old["best"]
rows = []
for f in sorted(glob.glob("verify/target_dual_eps_*_out.json")):
    d = json.load(open(f))
    for k, v in d.items():
        if not k.startswith("eps"): continue
        cert = v.get("verify"); rows.append(dict(U=v["U"], hu=v["hu"], eps=v["eps"], d=v["d_tilde"], kt=v["kappa_tilde_lp"], klp=v["kappa_lp"],
                                                 kc=(cert["kappa_cert"] if cert else None), eta=(cert["eta"] if cert else None),
                                                 cells=(cert["cells"] if cert else None), depth=(cert["depth"] if cert else None), file=f, margin=("m1e-4" in f)))
rows.sort(key=lambda r: (r["U"], r["hu"], -r["eps"], r["margin"]))
best = max([r for r in rows if r["kc"]], key=lambda r: r["kc"])
n = open("NOTE.md", encoding="utf-8").read()
tab = ["| U | hu | ε | LP margin | d̃ (LP) | κ̃ = 2 − d̃ | κ_lp = εκ̃ | certified κ | verification |", "|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    cert = f"**{r['kc']:.4e}**" if (r["kc"] and r is best) else (f"{r['kc']:.4e}" if r["kc"] else "none `[computed, not certified]`")
    ver = f"η = {r['eta']:.1e}, {r['cells']/1e6:.1f}·10⁶ cells, depth {r['depth']}" if r["kc"] else "failed at every η tried (or κ̃ ≤ 0)"
    tab.append(f"| {r['U']:g} | {r['hu']:g} | {r['eps']:g} | {'10⁻⁴' if r['margin'] else '2·10⁻⁵'} | {r['d']:.6f} | {r['kt']:.6f} | {r['klp']:.3e} | {cert} | {ver} |")
i0 = n.index("| U | hu | ε |"); i1 = n.index("**Reading the table.**"); n = n[:i0] + "\n".join(tab) + "\n\n" + n[i1:]
if best["kc"] > KLB0 + 1e-12:
    KLB = best["kc"]; KUB = old["KUB"]; iota = 0.241523; GAPF = KUB/KLB; CLB = 4*(1 + iota/KLB); ELL = 4*np.pi*(1 + iota/KLB); ELL0 = 4*np.pi*(1 + iota/KLB0)
    rep = [(f"{KLB0:.4e}", f"{KLB:.4e}"), (f"{KLB0:.3e}", f"{KLB:.3e}"), (f"factor {GAPF0:.1f}", f"factor {GAPF:.1f}"), (f"factor {GAPF0:.0f}", f"factor {GAPF:.0f}"),
           (f"{GAPF0:.0f} times below", f"{GAPF:.0f} times below"), (f"**{CLB0:.3g}**", f"**{CLB:.3g}**"), (f"C = {CLB0:.3g}", f"C = {CLB:.3g}"),
           (f"ℓ′ > {ELL0:.3g}", f"ℓ′ > {ELL:.3g}"), (f"e^{{{ELL0:.0f}}}", f"e^{{{ELL:.0f}}}"), (f"C(κ_lb) = {CLB0:.3g}", f"C(κ_lb) = {CLB:.3g}"),
           (f"U = {best0['U']:g}, hu = {best0['hu']:g}, ε = {best0['eps']:g}, η = {best0['eta']:.0e}; certificate `verify/target_dual_eps_s_U{best0['U']:g}_hu{best0['hu']:g}_eps{best0['eps']:g}.npy`, the LP value εκ̃ = {best0['klp']:.4e} less the repair",
            f"U = {best['U']:g}, hu = {best['hu']:g}, ε = {best['eps']:g}, LP margin 10⁻⁴, η = {best['eta']:.0e}; certificate `verify/target_dual_eps_s_U{best['U']:g}_hu{best['hu']:g}_eps{best['eps']:g}.npy` (the m1e-4 run), the LP value εκ̃ = {best['klp']:.4e} less the repair"),
           (f"(§5, U = {best0['U']:g}, ε = {best0['eps']:g})", f"(§5, U = {best['U']:g}, ε = {best['eps']:g}, LP margin 10⁻⁴)"),
           (f"has its certified maximum at ε = {best0['eps']:g}", f"has its certified maximum at ε = {best['eps']:g} (with the LP margin raised to 10⁻⁴; at margin 2·10⁻⁵ the ε ≥ 3·10⁻³ certificates failed the pointwise check)")]
    cnt = {}
    for a, b in rep:
        cnt[a] = n.count(a); n = n.replace(a, b)
    print("repatched:", {k: v for k, v in cnt.items() if v}); print(f"new best {KLB:.4e} (eps {best['eps']}, margin {best['margin']}), gap {GAPF:.1f}, C {CLB:.3g}")
    json.dump(dict(best=best, rows=rows, KLB=KLB, KUB=KUB, GAPF=GAPF, CLB=CLB), open("verify/finalize_note_out.json", "w"), indent=1)
else:
    print("no improvement; table rebuilt only")
open("NOTE.md", "w", encoding="utf-8").write(n); print(len(n.splitlines()), "lines")
