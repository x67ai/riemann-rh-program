"""audit_O_leancases_verify.py -- AUDITOR O (Session 14, resumed run).

Closes a gap the first pass of this audit left open: AuditOCases.lean's kernel
verdicts are only evidence about the ACCEPTANCE TRANSCRIPTS if the Lean literals
actually carry the JSON data.  audit_O_lean_emit.py is untrusted by construction
(FORMAT.md sec. 10, last bullet), so its output must be checked, not believed.

This script does NOT use the emitter.  It PARSES Zeta23/W1/AuditOCases.lean back
into Python dicts with an independent regex/tokenizer reader and compares, field
by field and row by row, against the JSON transcripts in acceptance/ (re-applying
the declared mutation for the corrupted instances, recomputed here from scratch
rather than imported from the emitter).

A single mismatch would make every kernel verdict in AUDIT-O.md sec. 3.3 vacuous.
"""
import copy, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LEAN = "/Users/jaytyagi/rh-lean-work/zeta-23-lean-main/Zeta23/W1/AuditOCases.lean"

# name -> (acceptance json file, mutation kind).  Read off AuditOCases.lean's own
# doc-comments and theorem names; the mutations are re-implemented below.
INSTANCES = [
    ("mpNullT100",          "w1-mp-null-t100.json",       "clean"),
    ("arbNullT100",         "w1-arb-null-t100.json",      "clean"),
    ("mpNullDeepT100",      "w1-mp-null-deep-t100.json",  "clean"),
    ("arbNullDeepT100",     "w1-arb-null-deep-t100.json", "clean"),
    ("mpNullT1000",         "w1-mp-null-t1000.json",      "clean"),
    ("arbNullT1000",        "w1-arb-null-t1000.json",     "clean"),
    ("mpNullT10000",        "w1-mp-null-t10000.json",     "clean"),
    ("arbNullT10000",       "w1-arb-null-t10000.json",    "clean"),
    ("mpDH",                "w1-mp-dh-livefire.json",     "clean"),
    ("arbDH",               "w1-arb-dh-livefire.json",    "clean"),
    ("posMP_rej",           "w1-poscontrol-mp.json",      "clean"),
    ("posARB_rej",          "w1-poscontrol-arb.json",     "clean"),
    ("mpDH_c6",             "w1-mp-dh-livefire.json",     "c6"),
    ("mpDH_c8",             "w1-mp-dh-livefire.json",     "c8"),
    ("mpDH_c9",             "w1-mp-dh-livefire.json",     "c9"),
    ("mpDH_c3",             "w1-mp-dh-livefire.json",     "c3"),
    ("mpDH_c2",             "w1-mp-dh-livefire.json",     "c2"),
    ("mpDH_ahalf",          "w1-mp-dh-livefire.json",     "ahalf"),
    ("arbNullT100_c6",      "w1-arb-null-t100.json",      "c6"),
    ("arbNullT100_c9",      "w1-arb-null-t100.json",      "c9"),
    ("arbNullT10000_c3",    "w1-arb-null-t10000.json",    "c3"),
]


def mutate(doc, kind):
    """Re-implemented HERE from the corruption descriptions, not imported."""
    d = copy.deepcopy(doc)
    if kind == "clean":
        return d
    if kind == "c6":
        r = d["segments"][len(d["segments"]) // 2]
        w = max(abs(int(r[k])) for k in ("reLo", "reHi", "imLo", "imHi")) or 1
        r["reLo"], r["reHi"], r["imLo"], r["imHi"] = str(-w), str(w), str(-w), str(w)
        return d
    if kind == "c8":
        A = int(d["scales"]["A"])
        d["segments"][0]["argLo"], d["segments"][0]["argHi"] = str(-(A // 2)), str(A // 2)
        return d
    if kind == "c9":
        d["claimed_m"] = str(int(d["claimed_m"]) + 1)
        return d
    if kind == "c3":
        b = d["mesh"]["bottom"]
        b[1], b[2] = b[2], b[1]
        return d
    if kind == "c2":
        d["rect"]["sigma1"] = {"n": "1", "d": "2"}
        d["mesh"]["bottom"][0] = {"n": "1", "d": "2"}
        d["mesh"]["top"][-1] = {"n": "1", "d": "2"}
        return d
    if kind == "ahalf":
        d["scales"]["A"] = str(int(d["scales"]["A"]) // 2)
        d["claimed_m"] = str(int(d["claimed_m"]) * 2)
        return d
    raise ValueError(kind)


# ---------------------------------------------------------------- Lean reader
def strip_parens(tok):
    tok = tok.strip()
    return tok[1:-1].strip() if tok.startswith("(") and tok.endswith(")") else tok


def parse_lean(path):
    """Independent reader: split the file on 'def NAME : W1Data where' blocks."""
    src = open(path).read()
    out = {}
    marks = [(m.start(), m.group(1), m.group(2))
             for m in re.finditer(r"^def (\w+) : (W1Data|W1Floor) where$", src, re.M)]
    for i, (pos, name, kind) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(src)
        body = src[pos:end]
        d = {}
        for fld in ("p1", "q1", "p2", "q2", "a1", "b1", "a2", "b2", "K", "A", "m", "Fn", "Fd"):
            mm = re.search(r"(?:^|\s)%s := ([^\s;\n]+)" % fld, body)
            if mm:
                d[fld] = int(strip_parens(mm.group(1)))
        for e in ("bottom", "right", "top", "left"):
            mm = re.search(r"^  %s\s*:= \[(.*)\]$" % e, body, re.M)
            if mm:
                d[e] = [tuple(int(strip_parens(x)) for x in p.split(","))
                        for p in re.findall(r"\(([^()]*(?:\([^()]*\)[^()]*)*)\)",
                                            mm.group(1).replace("(-", "@-").replace(")", ")"))
                        ] if False else _pairs(mm.group(1))
        mm = re.search(r"^  rows := \[\n(.*?)\]$", body, re.M | re.S)
        if mm:
            d["rows"] = [tuple(int(strip_parens(x)) for x in r.split(","))
                         for r in re.findall(r"⟨([^⟩]*)⟩", mm.group(1))]
        d["_kind"] = kind
        out[name] = d
    return out


def _pairs(s):
    """Parse '(a, b), (c, d), ...' where a,b may be '(-n)'."""
    res, depth, cur = [], 0, ""
    for ch in s:
        if ch == "(":
            depth += 1
            if depth == 1:
                cur = ""
                continue
        elif ch == ")":
            depth -= 1
            if depth == 0:
                res.append(tuple(int(strip_parens(x)) for x in cur.split(",")))
                continue
        if depth >= 1:
            cur += ch
    return res


def main():
    lean = parse_lean(LEAN)
    bad = 0
    print("AUDIT O -- AuditOCases.lean literals vs acceptance/*.json (independent back-parse)")
    print("%-20s %6s  %s" % ("instance", "rows", "field/row comparison"))
    for name, fn, kind in INSTANCES:
        with open(os.path.join(HERE, "acceptance", fn)) as fh:
            doc = mutate(json.load(fh), kind)
        L = lean.get(name)
        if L is None:
            print("  %-20s MISSING from Lean file" % name); bad += 1; continue
        errs = []
        r = doc["rect"]
        want = {"p1": r["sigma1"]["n"], "q1": r["sigma1"]["d"], "p2": r["sigma2"]["n"],
                "q2": r["sigma2"]["d"], "a1": r["T1"]["n"], "b1": r["T1"]["d"],
                "a2": r["T2"]["n"], "b2": r["T2"]["d"], "K": doc["scales"]["K"],
                "A": doc["scales"]["A"], "m": doc["claimed_m"]}
        for k, v in want.items():
            if L.get(k) != int(v):
                errs.append("%s: lean=%s json=%s" % (k, L.get(k), v))
        for e in ("bottom", "right", "top", "left"):
            jj = [(int(x["n"]), int(x["d"])) for x in doc["mesh"][e]]
            if L.get(e) != jj:
                errs.append("%s edge differs (lean %d pts, json %d pts)"
                            % (e, len(L.get(e) or []), len(jj)))
        jr = [tuple(int(s[k]) for k in ("reLo", "reHi", "imLo", "imHi", "argLo", "argHi"))
              for s in doc["segments"]]
        if L.get("rows") != jr:
            n = sum(1 for a, b in zip(L.get("rows") or [], jr) if a != b)
            errs.append("rows differ: lean %d rows, json %d rows, %d differing"
                        % (len(L.get("rows") or []), len(jr), n))
        if "modulus_floor" in doc and name + "_floor" in lean:
            F = lean[name + "_floor"]
            if F.get("Fn") != int(doc["modulus_floor"]["Fn"]) or \
               F.get("Fd") != int(doc["modulus_floor"]["Fd"]):
                errs.append("floor differs")
        print("  %-20s %6d  %s" % (name, len(jr), "OK" if not errs else "; ".join(errs)))
        bad += len(errs)
    print("\nTOTAL literal mismatches: %d" % bad)
    return bad


if __name__ == "__main__":
    sys.exit(0 if main() == 0 else 1)
