#!/usr/bin/env python3
"""AUDIT (2026-09-03): independent replay of Gomila's printed gate from the converted scalars (gomila/gomila-scalars.json)
with the conventions of INSTANCE-REPORT §5.1: spatial = D_z/(2(num-1)), mesh = 4(num-1) segments;
margin = M- - spatial - D_t*Delta+ - eps+.  Compared against the record's own gate_replay_margin / cb12_floor fields.
Run record: audit-gomila-stats.txt.  usage: audit_gomila_stats.py <results/d1-m2a>"""
import json, sys, statistics
from fractions import Fraction as F
P=sys.argv[1]
sc=json.load(open(P+"/gomila/gomila-scalars.json")); pr=sc["prisms"]
def fr(s): return F(s)
res=[]
for q in pr:
    M_lo=fr(q["min_mesh"][0]); Dz=int(q["Dz"]); Dt=int(q["Dt"]); mesh=int(q["mesh"]); Delta=fr(q["Delta_plus"])
    spatial = F(Dz) / (2*F(mesh, 4))
    eps = fr(q["eps"]) if isinstance(q["eps"], str) else fr(q["eps"][1])
    margin = M_lo - spatial - Dt*Delta - eps
    res.append((q["k"], margin, margin/M_lo, M_lo - spatial, fr(q["gate_replay_margin"]), fr(q["cb12_floor"])))
print("my replayed margin vs record's gate_replay_margin: %d prisms differ by > 1e-9" % len([r for r in res if abs(r[1]-r[4]) > F(1,10**9)]))
print("my M-spatial vs record's cb12_floor: %d differ" % len([r for r in res if abs(r[3]-r[5]) > F(1,10**9)]))
mn=min(res, key=lambda r:r[1]); mnf=min(res, key=lambda r:r[3])
print("min replayed margin: prism", mn[0], "%.6f" % float(mn[1]), " | min C-B12 floor M-spatial: prism", mnf[0], "%.6f" % float(mnf[3]))
rels=[float(r[2]) for r in res]; med=statistics.median(rels)
print("relative margins: min %.4f max %.4f median %.4f; all below 2*median: %s" % (min(rels), max(rels), med, all(r < 2*med for r in rels)))
print("10 thinnest relative:", sorted([r[0] for r in sorted(res, key=lambda r:r[2])[:10]]))
print("prism 1 margin %.6f; prism 883 t_hi contains 129/800: %s" % (float(res[0][1]), fr(pr[-1]["t_hi"][0]) <= F(129,800) <= fr(pr[-1]["t_hi"][1])))
print("chain: first seam 0:", pr[0]["seam_mid"]=="0", "| strictly increasing:", all(fr(pr[i]["seam_mid"]) < fr(pr[i+1]["seam_mid"]) for i in range(len(pr)-1)), "| last < t0:", fr(pr[-1]["seam_mid"]) < F(129,800), "| continuity:", all(fr(pr[i]["next_mid"]) == fr(pr[i+1]["seam_mid"]) for i in range(len(pr)-1)))
print("all gate margins > 0:", all(r[1] > 0 for r in res), "| all winding balls inside (-1/4,1/4):", all(F(-1,4) < fr(q["winding"][0]) and fr(q["winding"][1]) < F(1,4) for q in pr))
