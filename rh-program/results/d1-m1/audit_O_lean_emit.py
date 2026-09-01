"""audit_O_lean_emit.py -- AUDITOR O: JSON -> Lean W1Data literal emitter.

Session 8 shipped NO JSON->Lean emitter: Zeta23/W1/Examples.lean carries only the
two ARTIFICIAL 8-row micro-examples of FORMAT.md sec. 11, so the Lean kernel
checker was never run on a producer-emitted transcript.  This auditor tool
supplies the missing translation so that the SAME acceptance transcripts (and the
SAME corruptions) can be put through `checkW1` by `decide +kernel`.

The emitter is UNTRUSTED and mechanical (FORMAT.md sec. 10, last bullet): it reads the
integer strings verbatim and prints them as Lean integer literals; the kernel
re-checks everything from the literals.

Usage:  python3 audit_O_lean_emit.py OUT.lean NAME=FILE.json[:mutation] ...
        mutation in {clean, c6, c8, c9, c3, c2, ahalf}
"""
import copy, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def mutate(doc, kind):
    d = copy.deepcopy(doc)
    if kind == "clean":
        return d
    if kind == "c6":
        k = len(d["segments"]) // 2
        r = d["segments"][k]
        w = max(abs(int(r["reLo"])), abs(int(r["reHi"])),
                abs(int(r["imLo"])), abs(int(r["imHi"])), 1)
        r["reLo"], r["reHi"], r["imLo"], r["imHi"] = str(-w), str(w), str(-w), str(w)
        return d
    if kind == "c8":
        A = int(d["scales"]["A"])
        d["segments"][0]["argLo"] = str(-(A // 2))
        d["segments"][0]["argHi"] = str(A // 2)
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
        # halve A and double m: no checker clause ties A to the rows' meaning,
        # so this must be ACCEPTED -- it falsifies H-ENCL(b), not the checker.
        A = int(d["scales"]["A"])
        d["scales"]["A"] = str(A // 2)
        d["claimed_m"] = str(int(d["claimed_m"]) * 2)
        return d
    raise ValueError(kind)


def lean_int(s):
    n = int(s)
    return "(%d)" % n if n < 0 else "%d" % n


def rat_list(lst):
    return "[" + ", ".join("(%s, %s)" % (lean_int(r["n"]), lean_int(r["d"])) for r in lst) + "]"


def emit(name, doc):
    r = doc["rect"]
    rows = ",\n    ".join(
        "⟨%s, %s, %s, %s, %s, %s⟩" % tuple(
            lean_int(s["%s" % k]) for k in ("reLo", "reHi", "imLo", "imHi", "argLo", "argHi"))
        for s in doc["segments"])
    out = []
    out.append("/-- auditor-O instance %s (%s / %s, %d rows) -/" %
               (name, doc["function"], doc["mode"], len(doc["segments"])))
    out.append("def %s : W1Data where" % name)
    out.append("  p1 := %s;  q1 := %s" % (lean_int(r["sigma1"]["n"]), lean_int(r["sigma1"]["d"])))
    out.append("  p2 := %s;  q2 := %s" % (lean_int(r["sigma2"]["n"]), lean_int(r["sigma2"]["d"])))
    out.append("  a1 := %s;  b1 := %s" % (lean_int(r["T1"]["n"]), lean_int(r["T1"]["d"])))
    out.append("  a2 := %s;  b2 := %s" % (lean_int(r["T2"]["n"]), lean_int(r["T2"]["d"])))
    out.append("  K := %s" % lean_int(doc["scales"]["K"]))
    out.append("  A := %s" % lean_int(doc["scales"]["A"]))
    out.append("  m := %s" % lean_int(doc["claimed_m"]))
    for e in ("bottom", "right", "top", "left"):
        out.append("  %-6s := %s" % (e, rat_list(doc["mesh"][e])))
    out.append("  rows := [\n    %s]" % rows)
    if "modulus_floor" in doc:
        out.append("")
        out.append("def %s_floor : W1Floor where" % name)
        out.append("  Fn := %s" % lean_int(doc["modulus_floor"]["Fn"]))
        out.append("  Fd := %s" % lean_int(doc["modulus_floor"]["Fd"]))
    return "\n".join(out)


def main(argv):
    out_path = argv[0]
    blocks = ["""/-
audit_O_lean_cases.lean -- AUDITOR O (Session 14): the M1 v1 ACCEPTANCE TRANSCRIPTS and
their corruptions as Lean literals, run through the kernel checker `checkW1`.
Generated mechanically by audit_O_lean_emit.py from results/d1-m1/acceptance/*.json.
Scratch/audit artifact: NOT a deliverable, and it asserts NOTHING about zeta or f_DH
(H-ENCL is never certified in Lean; an f_DH transcript carries no theorem at all, D-R8).
-/
import Zeta23.W1.Checker

namespace Zeta23
namespace W1
"""]
    thms = []
    for spec in argv[1:]:
        name, rhs = spec.split("=", 1)
        if ":" in rhs:
            fn, kind = rhs.split(":", 1)
        else:
            fn, kind = rhs, "clean"
        with open(os.path.join(HERE, "acceptance", fn)) as fh:
            doc = json.load(fh)
        doc = mutate(doc, kind)
        blocks.append(emit(name, doc))
        # a name ending in _rej is a transcript expected to be REJECTED even unmutated
        expect = "true" if (kind in ("clean", "ahalf") and not name.endswith("_rej")) else "false"
        thms.append("theorem %s_check : checkW1 %s = %s := by decide +kernel" % (name, name, expect))
        if "modulus_floor" in doc and expect == "true":
            thms.append("theorem %s_floor_check : checkW1Floor %s %s_floor = true := by decide +kernel"
                        % (name, name, name))
    blocks.append("\n".join(thms))
    blocks.append("end W1\nend Zeta23")
    with open(out_path, "w") as fh:
        fh.write("\n\n".join(blocks) + "\n")
    print("wrote %s (%d instances)" % (out_path, len(argv) - 1))


if __name__ == "__main__":
    main(sys.argv[1:])
