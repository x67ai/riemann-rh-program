#!/usr/bin/env python3
"""CHECK-O step 4: independent literal check of comparator/ChallengeDeps/DBN/Instance02.lean
against the JSON sources.  Written from scratch for Job 2 (the checker): it does NOT import,
call or re-use packaging/emit_challengedeps_instance02.py, emit_lean_m2a.py,
lane-a/emit_lean_lane_a.py, backparse_lane_a.py or packaging/cmp_literal_blocks.py.

It tokenizes the trusted Lean file directly (comments stripped first), reconstructs each
literal as Python integers, and compares integer by integer with:
  * results/d1-m2a/transcripts/row2/manifest.json + prism-*.json           (Lane B, mp leg)
  * results/d1-m2a/transcripts/row2-arb/instance02-barrier-manifest.json
      + instance02-prism-*.json                                            (Lane B, Arb leg)
  * results/d1-m2a/lane-a/asym-mp.json, asym-arb.json                      (Lane A, both legs)

Usage: check_literals.py <lean-tree> <results/d1-m2a dir>
"""
import json, os, re, sys

LEAN_TREE, RES = sys.argv[1], sys.argv[2]
LEAN = os.path.join(LEAN_TREE, "comparator/ChallengeDeps/DBN/Instance02.lean")

# ---------- 1. read + strip comments (nested /- -/ blocks and -- lines) ----------
src = open(LEAN, encoding="utf-8").read()

def strip_comments(s):
    out, i, depth, n = [], 0, 0, len(s)
    while i < n:
        if s.startswith("/-", i):
            depth += 1; i += 2; continue
        if s.startswith("-/", i) and depth:
            depth -= 1; i += 2; continue
        if depth:
            i += 1; continue
        if s.startswith("--", i):
            j = s.find("\n", i); i = n if j < 0 else j
            continue
        out.append(s[i]); i += 1
    return "".join(out)

code = strip_comments(src)

# ---------- 2. split into `def` blocks ----------
blocks = {}
starts = [(m.start(), m.group(1)) for m in re.finditer(r"(?m)^def\s+(\S+)", code)]
for k, (pos, name) in enumerate(starts):
    end = starts[k + 1][0] if k + 1 < len(starts) else len(code)
    blocks[name] = code[pos:end]

INT = re.compile(r"-?\d+")

def ints(t):
    return [int(x) for x in INT.findall(t)]

def field(block, name):
    """value text of `name := …` up to the next top-level field or end."""
    m = re.search(r"(?m)^\s{2}" + re.escape(name) + r"\s*:=\s*", block)
    if not m: raise KeyError(name + " in block")
    rest = block[m.end():]
    m2 = re.search(r"(?m)^\s{2}[A-Za-z_][A-Za-z0-9_']*\s*:=", rest)
    return rest[:m2.start()] if m2 else rest

def rec_field(block, name):
    """value text of `name := …` inside a `{ … }` record literal (4-space indent)."""
    m = re.search(re.escape(name) + r"\s*:=\s*", block)
    if not m: raise KeyError(name)
    rest = block[m.end():]
    m2 = re.search(r"[,}]\s*\n?\s*[A-Za-z_][A-Za-z0-9_']*\s*:=", rest)
    return rest[:m2.start()] if m2 else rest

cmp_count = 0
mismatch = []

def eq(where, got, want):
    global cmp_count
    cmp_count += 1
    if got != want:
        mismatch.append((where, got, want))

def eqs(where, got, want):
    """compare two integer lists elementwise, counting each"""
    if len(got) != len(want):
        mismatch.append((where + " [length]", len(got), len(want)))
        return
    for i, (a, b) in enumerate(zip(got, want)):
        eq("%s[%d]" % (where, i), a, b)

# ---------- 3. Lane B ----------
def check_laneB(leg, barrier_name, prism_prefix, tdir, manifest_name, nprism):
    man = json.load(open(os.path.join(RES, tdir, manifest_name)))
    b = blocks[barrier_name]
    # rect: row2Rect is shared; check it against this manifest too
    r = ints(blocks["row2Rect"].split(":=", 1)[1])
    mr = man["rect"]
    eqs("%s/rect" % leg, r,
        [int(mr["x1"]["n"]), int(mr["x1"]["d"]), int(mr["x2"]["n"]), int(mr["x2"]["d"]),
         int(mr["y1"]["n"]), int(mr["y1"]["d"]), int(mr["y2"]["n"]), int(mr["y2"]["d"])])
    eq("%s/t0n" % leg, ints(field(b, "t0n"))[0], int(man["t0"]["n"]))
    eq("%s/t0d" % leg, ints(field(b, "t0d"))[0], int(man["t0"]["d"]))
    names = re.findall(r"[A-Za-z_][A-Za-z0-9_']*", field(b, "prisms"))
    if len(names) != nprism:
        mismatch.append(("%s/prisms [count]" % leg, len(names), nprism))
    if len(man["prisms"]) != nprism:
        mismatch.append(("%s/manifest prisms [count]" % leg, len(man["prisms"]), nprism))
    nrows_total = 0
    for k, entry in enumerate(man["prisms"]):
        want_name = "%s%04d" % (prism_prefix, k)
        if names[k] != want_name:
            mismatch.append(("%s/prisms[%d] name" % (leg, k), names[k], want_name))
        pj = json.load(open(os.path.join(RES, tdir, entry["file"])))
        eq("%s/%s/index" % (leg, want_name), k, int(pj["index"]))
        pb = blocks[want_name]
        eq("%s/%s/tn" % (leg, want_name), ints(field(pb, "tn"))[0], int(pj["seam"]["n"]))
        eq("%s/%s/td" % (leg, want_name), ints(field(pb, "td"))[0], int(pj["seam"]["d"]))
        eq("%s/%s/K" % (leg, want_name), ints(field(pb, "K"))[0], int(pj["scales"]["K"]))
        eq("%s/%s/A" % (leg, want_name), ints(field(pb, "A"))[0], int(pj["scales"]["A"]))
        for side in ("bottom", "right", "top", "left"):
            got = ints(field(pb, side))
            want = []
            for q in pj["mesh"][side]:
                want += [int(q["n"]), int(q["d"])]
            eqs("%s/%s/%s" % (leg, want_name, side), got, want)
        # rows: the field names a chunk def (or a ++ of chunk defs)
        chunk_names = re.findall(r"[A-Za-z_][A-Za-z0-9_']*", field(pb, "rows"))
        got = []
        for cn in chunk_names:
            got += ints(blocks[cn].split(":=", 1)[1])
        want = []
        for s in pj["segments"]:
            want += [int(s["reLo"]), int(s["reHi"]), int(s["imLo"]),
                     int(s["imHi"]), int(s["argLo"]), int(s["argHi"])]
        nrows_total += len(pj["segments"])
        eqs("%s/%s/rows" % (leg, want_name), got, want)
        eq("%s/%s/Fn" % (leg, want_name), ints(field(pb, "Fn"))[0], int(pj["modulus_floor"]["Fn"]))
        eq("%s/%s/Fd" % (leg, want_name), ints(field(pb, "Fd"))[0], int(pj["modulus_floor"]["Fd"]))
        eq("%s/%s/E" % (leg, want_name), ints(field(pb, "E"))[0], int(pj["approx_defect"]))
        eq("%s/%s/D" % (leg, want_name), ints(field(pb, "D"))[0], int(pj["displacement"]))
    return nrows_total

# ---------- 4. Lane A ----------
def check_laneA(leg, name, jf):
    j = json.load(open(os.path.join(RES, "lane-a", jf)))
    b = blocks[name]
    eq("%s/K" % leg, ints(rec_field(b, "K"))[0], int(j["scales"]["K"]))
    for f, (a, bb) in (("t0n", ("t0", "n")), ("t0d", ("t0", "d")),
                       ("y0n", ("y0", "n")), ("y0d", ("y0", "d")),
                       ("yAn", ("yA", "n")), ("yAd", ("yA", "d"))):
        eq("%s/%s" % (leg, f), ints(rec_field(b, f))[0], int(j[a][bb]))
    got = ints(rec_field(b, "rows"))
    want = []
    for r in j["rows"]:
        want += [int(r["Nlo"]), int(r["Nhi"]), int(r["T"]), int(r["E"])]
    eqs("%s/rows" % leg, got, want)
    got = ints(rec_field(b, "tail"))
    t = j["tail"]
    eqs("%s/tail" % leg, got,
        [int(t["N1"]), int(t["Q1"]), int(t["Q2"]), int(t["Q3"]), int(t["Q4"]), int(t["E1"])])
    return len(j["rows"])

print("CHECK-O step 4 — independent literal check (Job 2's own parser)")
print("file: comparator/ChallengeDeps/DBN/Instance02.lean")
print("def blocks parsed: %d" % len(blocks))
n_mp = check_laneB("mp", "row2BarrierMP", "mp", "transcripts/row2", "manifest.json", 39)
print("Lane B mp : 39 prisms, %d segment rows" % n_mp)
n_arb = check_laneB("arb", "row2BarrierARB", "arb", "transcripts/row2-arb",
                    "instance02-barrier-manifest.json", 72)
print("Lane B arb: 72 prisms, %d segment rows" % n_arb)
a1 = check_laneA("asym-mp", "row2AsymMP", "asym-mp.json")
a2 = check_laneA("asym-arb", "row2AsymARB", "asym-arb.json")
print("Lane A    : %d + %d window rows + 2 tail rows" % (a1, a2))
print()
print("integers compared: %d" % cmp_count)
print("mismatches: %d" % len(mismatch))
for w, g, x in mismatch[:50]:
    print("  MISMATCH %s: lean=%s json=%s" % (w, g, x))
print("RESULT: %s" % ("IDENTICAL" if not mismatch else "MISMATCH"))
sys.exit(0 if not mismatch else 1)
