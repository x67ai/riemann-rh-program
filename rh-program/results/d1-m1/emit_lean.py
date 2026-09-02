"""emit_lean.py -- W1 JSON transcript -> Lean `W1Data` literal emitter (UNTRUSTED, producer-side).

Copyright 2026 Kunal Tyagi.  Released under the Apache License 2.0 (see the repository's
LICENSE and NOTICE).

STATUS.  Promoted into the M1 v1 deliverable at the reconciled audit of 2026-09-02
(`AUDIT.md`, finding O MAJOR-1: FORMAT.md sec. 10 names a JSON->Lean emitter that Session 8
never wrote, so the Lean kernel checker had never been run on a producer-emitted transcript).
This is auditor O's emitter (`audit_O_lean_emit.py`, whose output was verified against the JSON
by the independent back-parse `audit_O_leancases_verify.py`: 21 instances, 4 217 rows,
0 mismatches) with the corruption modes removed and the `set_option maxRecDepth` line added
(finding O MAJOR-2 / F-3: a `W1Data` literal of >~ 900 rows does not compile at Lean's default
recursion limit -- the limit is hit by the DEFINITION COMPILER on the list literal, not by
`decide +kernel`, which evaluates `checkW1` on 1 294 rows in ~2 s at the default limit once
the data is imported; see FORMAT.md sec. 7.1).

TRUST.  This script is outside the trust boundary (FORMAT.md sec. 10, last bullet): it reads
the transcript's integer strings verbatim and prints them as Lean integer literals; the kernel
re-checks everything that matters from the literals (`decide +kernel` on `checkW1` /
`checkW1Floor`), and the analytic meaning of the fields enters the trusted statement only
through the displayed hypotheses (Soundness.lean).  A theorem `checkW1 d = true` proved from an
emitted literal asserts C1-C10 (C11) of the literal and NOTHING about zeta or f_DH; whether
the literal is the transcript is a question for the back-parse, never for this script.

Usage:
    python3 emit_lean.py OUT.lean [--module-doc FILE] [--program-header] NAME=FILE.json[:EXPECT] ...

    NAME     the Lean identifier of the instance (`def NAME : W1Data`; the optional floor is
             `def NAME_floor : W1Floor`);
    EXPECT   `true` (default) or `false` -- the asserted verdict of `checkW1 NAME`; a NAME ending
             in `_rej` defaults to `false` (positive controls, corruptions).  For EXPECT = true
             and a transcript carrying `modulus_floor`, the emitted theorem is
             `checkW1Floor NAME NAME_floor = true` (the floor variant, which implies `checkW1`);
             otherwise `checkW1 NAME = EXPECT`.
    --program-header   prepend the program's copyright header (for files copied into
             rh-program/lean/Zeta23/); --module-doc FILE inserts FILE's text as the module
             doc-comment after the header.

The output imports `Zeta23.W1.Checker` and lives in namespace `Zeta23.W1`.
"""
import json
import os
import sys

PROGRAM_HEADER = """/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library; it imports it.
-/
"""

MAX_REC_DEPTH = 100000


def lean_int(s):
    """Integer string -> Lean literal; negatives parenthesized so they parse inside tuples."""
    n = int(s)
    return "(%d)" % n if n < 0 else "%d" % n


def rat_list(lst):
    return "[" + ", ".join("(%s, %s)" % (lean_int(r["n"]), lean_int(r["d"])) for r in lst) + "]"


def emit_instance(name, doc, src_name):
    r = doc["rect"]
    rows = ",\n    ".join(
        "⟨%s, %s, %s, %s, %s, %s⟩" % tuple(
            lean_int(s[k]) for k in ("reLo", "reHi", "imLo", "imHi", "argLo", "argHi"))
        for s in doc["segments"])
    out = []
    out.append("/-- `%s`: %s / %s, claimed m = %s, %d rows, K = %s, A = %s.  Mechanically emitted by "
               "emit_lean.py (untrusted); asserts nothing analytic. -/"
               % (src_name, doc["function"], doc["mode"], doc["claimed_m"], len(doc["segments"]),
                  doc["scales"]["K"], doc["scales"]["A"]))
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
        out.append("/-- the optional modulus floor of `%s` (FORMAT.md sec. 5.2). -/" % src_name)
        out.append("def %s_floor : W1Floor where" % name)
        out.append("  Fn := %s" % lean_int(doc["modulus_floor"]["Fn"]))
        out.append("  Fd := %s" % lean_int(doc["modulus_floor"]["Fd"]))
    return "\n".join(out)


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    out_path = argv[0]
    specs = []
    module_doc = None
    program_header = False
    i = 1
    while i < len(argv):
        a = argv[i]
        if a == "--module-doc":
            with open(argv[i + 1]) as fh:
                module_doc = fh.read().rstrip("\n")
            i += 2
        elif a == "--program-header":
            program_header = True
            i += 1
        else:
            specs.append(a)
            i += 1
    parts = []
    if program_header:
        parts.append(PROGRAM_HEADER.rstrip("\n"))
    if module_doc is not None:
        parts.append("/-\n%s\n-/" % module_doc)
    parts.append("import Zeta23.W1.Checker\n\nnamespace Zeta23\nnamespace W1\n\n"
                 "-- Required by the definition compiler for literals of more than a few hundred rows\n"
                 "-- (FORMAT.md sec. 7.1; AUDIT.md O MAJOR-2): the limit is on the list literal, not on\n"
                 "-- `decide +kernel`.\nset_option maxRecDepth %d" % MAX_REC_DEPTH)
    thms = []
    n = 0
    for spec in specs:
        name, rhs = spec.split("=", 1)
        if ":" in rhs:
            fn, expect = rhs.rsplit(":", 1)
        else:
            fn, expect = rhs, ("false" if name.endswith("_rej") else "true")
        if expect not in ("true", "false"):
            raise SystemExit("emit_lean: EXPECT must be true or false (got %r)" % expect)
        with open(fn) as fh:
            doc = json.load(fh)
        parts.append(emit_instance(name, doc, os.path.basename(fn)))
        n += 1
        if expect == "true" and "modulus_floor" in doc:
            thms.append("/-- `%s`: C1-C11 hold on the literal (kernel evaluation; no `native_decide`). -/"
                        % os.path.basename(fn))
            thms.append("theorem %s_check : checkW1Floor %s %s_floor = true := by decide +kernel"
                        % (name, name, name))
        else:
            thms.append("/-- `%s`: `checkW1` evaluates to %s on the literal (kernel evaluation). -/"
                        % (os.path.basename(fn), expect))
            thms.append("theorem %s_check : checkW1 %s = %s := by decide +kernel" % (name, name, expect))
    parts.append("\n".join(thms))
    parts.append("end W1\nend Zeta23")
    with open(out_path, "w") as fh:
        fh.write("\n\n".join(parts) + "\n")
    print("emit_lean: wrote %s (%d instances, maxRecDepth %d)" % (out_path, n, MAX_REC_DEPTH))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
