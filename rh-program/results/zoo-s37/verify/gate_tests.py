#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""zoo-s37 gate tests for scripts/zoo-insert-s37.py — every run on scratch copies in the directory given as argv[1];
BARRIER-ZOO.md is only read (its hash is checked before and after). Writes verify/gate-tests.out and prints it.
Usage: python3 results/zoo-s37/verify/gate_tests.py SCRATCH_DIR"""
import hashlib
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ZOO = ROOT / "BARRIER-ZOO.md"
PROP = ROOT / "results/zoo-s37/zoo-entries-proposed.md"
SCRIPT = ROOT / "scripts/zoo-insert-s37.py"
OUT = ROOT / "results/zoo-s37/verify/gate-tests.out"
SD = Path(sys.argv[1]).resolve() / "gate-tests"
if SD.exists():
    shutil.rmtree(SD)
SD.mkdir(parents=True)
H0 = hashlib.sha256(ZOO.read_bytes()).hexdigest()
TOKEN = "<PRODUCER-B-VERDICT>"
VERDICT = "from two producers (A, Arb; B, a second method), agreeing [test text]"
ENV = dict(os.environ, TMPDIR=str(SD))
rows = []


def run(*a):
    r = subprocess.run([sys.executable, str(SCRIPT)] + [str(x) for x in a], capture_output=True, text=True, env=ENV, cwd=str(ROOT))
    return r.returncode, (r.stdout + r.stderr).strip()


def prop_variant(name, *edits):
    """A scratch copy of the proposed file with (block, old, new, count) edits applied INSIDE the named block only;
    each old must occur `count` times in that block's body."""
    t = PROP.read_text(encoding="utf-8")
    for blk, old, new, n in edits:
        m = re.search(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (blk, blk), t, re.S)
        body = m.group(1)
        if body.count(old) != n:
            sys.exit("gate_tests: edit %r occurs %d times in block %s, expected %d" % (old[:60], body.count(old), blk, n))
        t = t[:m.start(1)] + body.replace(old, new) + t[m.end(1):]
    p = SD / name
    p.write_text(t, encoding="utf-8")
    return p


def zoo_copy(name):
    p = SD / name
    shutil.copyfile(ZOO, p)
    return p


def test(tag, what, want_ok, rc, text, must=None):
    good = (rc == 0) == want_ok and (must is None or must in text)
    last = ([ln for ln in text.split("\n") if ln][-1] if text else "").replace(str(SD), "<scratch>")
    rows.append("[%s] %s %s  rc=%d  expected %s | %s" % ("PASS" if good else "FAIL", tag, what, rc,
                                                         "success" if want_ok else "refusal", last[:150]))
    return good


z = zoo_copy("zoo-a.md")
rc, t = run("--input", z)
test("T1", "default --out = scratch file in TMPDIR (token still in place)", True, rc, t, "WARNING: block iv9 still carries")
test("T1b", "the default output exists in TMPDIR", True, 0 if (SD / "zoo-insert-s37-out.md").exists() else 1, "")
rc, t = run("--input", SD / "zoo-insert-s37-out.md", "--out", SD / "twice.md")
test("T2", "second run on the inserted file", False, rc, t, "refusing to insert twice")
zt = zoo_copy("zoo-tampered.md")
zt.write_bytes(zt.read_bytes().replace(b"THE RULE (binding)", b"THE RULE (binding) ", 1))
rc, t = run("--input", zt, "--out", SD / "x.md")
test("T3", "tampered input (one byte)", False, rc, t, "someone edited the zoo")
rc, t = run("--input", z, "--out", ZOO)
test("T4", "--out BARRIER-ZOO.md", False, rc, t, "--out names")
rc, t = run("--input", z, "--out", z)
test("T5", "--out = --input", False, rc, t, "--out names the input file")
zi = zoo_copy("zoo-inplace.md")
rc, t = run("--input", zi, "--in-place")
test("T6", "--in-place while the token remains", False, rc, t, "replace it with Producer B's verdict")
test("T6b", "the scratch copy is unchanged after T6", True, 0 if zi.read_bytes() == ZOO.read_bytes() else 1, "")
pv = prop_variant("prop-verdict.md", ("iv9", TOKEN, VERDICT, 1))
rc, t = run("--input", zi, "--proposed", pv, "--in-place")
test("T7", "token replaced; --in-place on a scratch copy", True, rc, t, "OK: the token is replaced")
test("T7b", "the scratch copy now has 745 lines", True, 0 if zi.read_text(encoding="utf-8").count("\n") == 745 else 1, "")
rc, t = run("--input", zi, "--proposed", pv, "--in-place")
test("T7c", "second --in-place run", False, rc, t, "refusing to insert twice")
P2_OLD = "`results/haglund-cert-s37/producer-A/CERT.md`; entered at the Session-37 zoo stream)"
P2_NEW = "`results/haglund-cert-s37/producer-A/CERT.md`, `results/haglund-cert-s37/producer-B/CERT.md`; entered at the Session-37 zoo stream)"
LIT = "2026-09-30 (Session 37)"
FILL5 = (("count", "(dated, Session 37, 2026-09-30).**", "(dated, Session 37, %s).**" % LIT, 1),
         ("i9", "entered 2026-09-30, Session 37)", "entered %s, Session 37)" % LIT, 1),
         ("iv22", "entered 2026-09-30, Session 37)", "entered %s, Session 37)" % LIT, 1),
         ("iv9", "[RIDER 2026-09-30, Session 37 (", "[RIDER %s, Session 37 (" % LIT, 1),
         ("iii15", "[RIDER 2026-09-30, Session 37 (", "[RIDER %s, Session 37 (" % LIT, 1))
V = ("iv9", TOKEN, VERDICT, 1)
cases = (
    ("T8", "P1 + P2 + P3 applied, token replaced", True, "optional pairs applied: P1, P2, P3",
     (V, ("iv9", P2_OLD, P2_NEW, 1), ("xref", "one producer so far", "two producers [test text]", 1),
      ("iv21", "IV.20 as staged (Theorem R)", "IV.20 (Theorem R)", 1))),
    ("T9", "the brief's literal <ENTRY-DATE> fill at all five sites", True, "fill: '2026-09-30 (Session 37)'", (V,) + FILL5),
    ("T10", "the literal fill at four of the five sites", False, "STOP", (V,) + FILL5[:4]),
    ("T11", "drift in IV.22 SOURCE (one path)", False, "block iv22 is not staged Block (i)",
     (V, ("iv22", "`fingerprint/verify-F/rerun_theoremD.log`", "`fingerprint/verify-F/rerun_theoremD2.log`", 1))),
    ("T12", "drift in the d4-infty row", False, "block xref is not the brief's d4-infty row",
     (V, ("xref", "read at the line Session 37, dual-model", "read at the line, Session 37, dual-model", 1))),
    ("T13", "P3 applied in part", False, "block iv21's STATUS",
     (V, ("iv21", "IV.20 as staged (Theorem R)", "IV.20 as (Theorem R)", 1))),
    ("T14", "a malformed token replacement ('<…>')", False, "malformed", (("iv9", TOKEN, "<to be filled>", 1),)),
    ("T15", "the renumbering undone in row N3", False, "STOP", (V, ("xref", "| IV.22 face 2 (Theorem D)", "| IV.21 face 2 (Theorem D)", 1))),
    ("T16", "wrong line arithmetic in the count paragraph", False, "block count is not staged Block C",
     (V, ("count", "711 → 745 lines", "711 → 744 lines", 1))),
    ("T17", "the I.9 heading demoted to '####'", False, "STOP", (V, ("i9", "### I.9 The rung-1 twin", "#### I.9 The rung-1 twin", 1))),
    ("T18", "P1's slot filled with a '|' (would break the table)", False, "P1's replacement in the N2 row is malformed",
     (V, ("xref", "one producer so far", "two | producers", 1))),
)
for tag, what, ok, must, edits in cases:
    pv = prop_variant("prop-%s.md" % tag, *edits)
    rc, t = run("--input", z, "--proposed", pv, "--out", SD / ("out-%s.md" % tag))
    test(tag, what, ok, rc, t, must)
H1 = hashlib.sha256(ZOO.read_bytes()).hexdigest()
allok = all(r.startswith("[PASS]") for r in rows)
rows.append("ALL GATE TESTS AS EXPECTED: %s | BARRIER-ZOO.md still %s… = %s" % (allok, H0[:16], H1 == H0 == "90d0ad6afa093388317a71cd89daf4c10ea755978943027fb61c5f06c237cc0c"))
OUT.write_text("\n".join(rows) + "\n", encoding="utf-8")
print("\n".join(rows))
sys.exit(0 if allok and H1 == H0 else 1)
