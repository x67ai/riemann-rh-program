#!/usr/bin/env python3
"""verify_lean_m2a.py -- independent BACK-PARSE of the Lean modules written by emit_lean_m2a.py against the JSON
transcript (FORMAT.md section 10 discipline, as recon_instances_verify.py did for W1): reads each
Zeta23/DBN/Instance02/<prefix>_NNNN.lean with regular expressions (no shared code with the emitter), rebuilds the
PrismData (seam, K, A, four mesh edges, the concatenated row chunks, Fn, Fd, E, D) and compares field by field and
row by row with the JSON prism file; also checks Rect.lean against the manifest's rect/t0 and <prefix>_Barrier.lean's
prism list order and t0.  Exit 0 = 0 mismatches.

usage: verify_lean_m2a.py <manifest.json> <lean-root> <prefix>
"""
import json, os, re, sys
from fractions import Fraction

def rat(o): return Fraction(int(o["n"]), int(o["d"]))

def parse_prism_module(path, name):
    src = open(path).read()
    chunks = {}
    for m in re.finditer(r"def " + name + r"_rows_(\d+) : List W1\.W1Row := \[(.*?)\]\n", src, re.S):
        body = m.group(2)
        rows = [tuple(int(x) for x in t.split(",")) for t in re.findall(r"⟨([^⟩]*)⟩", body)]
        chunks[int(m.group(1))] = rows
    m = re.search(r"def " + name + r" : PrismData where\n(.*?)\n\n", src, re.S)
    if not m: raise SystemExit(f"{path}: PrismData block not found")
    blk = m.group(1)
    def field(f):
        mm = re.search(r"^  " + f + r" := (.*)$", blk, re.M)
        if not mm: raise SystemExit(f"{path}: field {f} missing")
        return mm.group(1).strip()
    edges = {}
    for e in ("bottom", "right", "top", "left"):
        edges[e] = [Fraction(int(a), int(b)) for a, b in re.findall(r"\((-?\d+), (\d+)\)", field(e))]
    rows_expr = field("rows")
    order = [int(x) for x in re.findall(name + r"_rows_(\d+)", rows_expr)]
    if rows_expr == "[]": order = []
    rows = []
    for c in order: rows.extend(chunks[c])
    if sorted(order) != list(range(len(chunks))): raise SystemExit(f"{path}: chunk order {order} vs {len(chunks)} chunks")
    thm = re.search(r"theorem " + name + r"_check : checkPrism row2Rect " + name + r" = true := by decide \+kernel", src)
    if not thm: raise SystemExit(f"{path}: kernel theorem missing or altered")
    return {"seam": Fraction(int(field("tn")), int(field("td"))), "K": int(field("K")), "A": int(field("A")),
            "mesh": edges, "rows": rows, "Fn": int(field("Fn")), "Fd": int(field("Fd")), "E": int(field("E")), "D": int(field("D"))}

def main():
    man_path, root, prefix = sys.argv[1:4]
    m = json.load(open(man_path)); base = os.path.dirname(os.path.abspath(man_path))
    d = os.path.join(root, "Zeta23", "DBN", "Instance02")
    mism = 0; nrows = 0
    # Rect.lean
    rs = open(os.path.join(d, "Rect.lean")).read()
    mm = re.search(r"def row2Rect : RectData :=\n  ⟨([^⟩]*)⟩", rs)
    vals = [int(x) for x in mm.group(1).split(",")]
    jr = [rat(m["rect"][k]) for k in ("x1", "x2", "y1", "y2")]
    lr = [Fraction(vals[2 * i], vals[2 * i + 1]) for i in range(4)]
    if jr != lr: mism += 1; print("MISMATCH rect", jr, lr)
    # Barrier.lean
    bs = open(os.path.join(d, f"{prefix}_Barrier.lean")).read()
    t0n = int(re.search(r"^  t0n := (-?\d+)", bs, re.M).group(1)); t0d = int(re.search(r"^  t0d := (\d+)", bs, re.M).group(1))
    if Fraction(t0n, t0d) != rat(m["t0"]): mism += 1; print("MISMATCH t0")
    plist = re.search(r"^  prisms := \[(.*)\]", bs, re.M).group(1).split(", ")
    expect = [f"{prefix}{int(e['index']):04d}" for e in m["prisms"]]
    if plist != expect: mism += 1; print("MISMATCH prism list order", plist[:3], expect[:3])
    for e in m["prisms"]:
        j = int(e["index"]); name = f"{prefix}{j:04d}"
        p = json.load(open(os.path.join(base, e["file"])))
        L = parse_prism_module(os.path.join(d, f"{prefix}_{j:04d}.lean"), name)
        J = {"seam": rat(p["seam"]), "K": int(p["scales"]["K"]), "A": int(p["scales"]["A"]),
             "mesh": {k: [rat(r) for r in p["mesh"][k]] for k in ("bottom", "right", "top", "left")},
             "rows": [tuple(int(r[k]) for k in ("reLo", "reHi", "imLo", "imHi", "argLo", "argHi")) for r in p["segments"]],
             "Fn": int(p["modulus_floor"]["Fn"]), "Fd": int(p["modulus_floor"]["Fd"]), "E": int(p["approx_defect"]), "D": int(p["displacement"])}
        if rat(e["seam"]) != J["seam"]: mism += 1; print(f"MISMATCH manifest seam prism {j}")
        for k in J:
            if J[k] != L[k]:
                mism += 1; print(f"MISMATCH prism {j} field {k}" + (f": {len(J[k])} vs {len(L[k])} rows" if k == "rows" else f": {J[k]!s:.60} vs {L[k]!s:.60}"))
        nrows += len(J["rows"])
    print(f"verify_lean_m2a: {len(m['prisms'])} prisms, {nrows} rows compared field by field, row by row: {mism} mismatches")
    sys.exit(0 if mism == 0 else 1)

if __name__ == "__main__":
    main()
