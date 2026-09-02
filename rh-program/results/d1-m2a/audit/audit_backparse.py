#!/usr/bin/env python3
"""AUDIT (2026-09-03): independent back-parse (own regexes) of emitted Instance02 Lean modules against their JSON.
Run record: audit-backparse.txt.  usage: audit_backparse.py <rh-program root>"""
import re, json, sys
P=sys.argv[1]
def parse_lean(path):
    s=open(path).read()
    rows=[tuple(int(v) for v in m.groups()) for m in re.finditer(r"⟨\s*(-?\d+),\s*(-?\d+),\s*(-?\d+),\s*(-?\d+),\s*(-?\d+),\s*(-?\d+)\s*⟩", s)]
    def field(n): return re.search(r"\n  %s := (-?\d+)" % n, s).group(1)
    def mesh(n):
        body=re.search(r"\n  %s := \[(.*?)\]\n" % n, s, re.S).group(1)
        return [(int(a),int(b)) for a,b in re.findall(r"\((-?\d+), (-?\d+)\)", body)]
    return {"tn":int(field("tn")),"td":int(field("td")),"K":int(field("K")),"A":int(field("A")),"Fn":int(field("Fn")),"Fd":int(field("Fd")),"E":int(field("E")),"D":int(field("D")),
            "mesh":{e:mesh(e) for e in ("bottom","right","top","left")},"rows":rows}
def parse_json(path):
    p=json.load(open(path))
    return {"tn":int(p["seam"]["n"]),"td":int(p["seam"]["d"]),"K":int(p["scales"]["K"]),"A":int(p["scales"]["A"]),"Fn":int(p["modulus_floor"]["Fn"]),"Fd":int(p["modulus_floor"]["Fd"]),"E":int(p["approx_defect"]),"D":int(p["displacement"]),
            "mesh":{e:[(int(r["n"]),int(r["d"])) for r in p["mesh"][e]] for e in ("bottom","right","top","left")},
            "rows":[tuple(int(r[k]) for k in ("reLo","reHi","imLo","imHi","argLo","argHi")) for r in p["segments"]]}
for lean, js in [("lean/Zeta23/DBN/Instance02/mp_0017.lean","results/d1-m2a/transcripts/row2/prism-0017.json"),("lean/Zeta23/DBN/Instance02/arb_0040.lean","results/d1-m2a/transcripts/row2-arb/instance02-prism-0040.json"),("lean/Zeta23/DBN/Instance02/mp_0038.lean","results/d1-m2a/transcripts/row2/prism-0038.json")]:
    a=parse_lean(P+"/"+lean); b=parse_json(P+"/"+js)
    print(lean, "vs", js, ":", "IDENTICAL" if a==b else "MISMATCH", "| rows", len(a["rows"]), len(b["rows"]))
for bar, man in [("lean/Zeta23/DBN/Instance02/mp_Barrier.lean","results/d1-m2a/transcripts/row2/manifest.json"),("lean/Zeta23/DBN/Instance02/arb_Barrier.lean","results/d1-m2a/transcripts/row2-arb/instance02-barrier-manifest.json")]:
    s=open(P+"/"+bar).read(); lst=re.search(r"prisms := \[(.*?)\]", s).group(1).split(", ")
    m=json.load(open(P+"/"+man)); print(bar, "prism list length", len(lst), "manifest", len(m["prisms"]), "t0", re.search(r"t0n := (\d+)", s).group(1), re.search(r"t0d := (\d+)", s).group(1), m["t0"])
