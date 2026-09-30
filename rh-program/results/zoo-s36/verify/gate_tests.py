import hashlib, re, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path.cwd()
SP = Path(sys.argv[1])
SCRIPT = ROOT / "scripts" / "zoo-insert-s36.py"
ZOO = ROOT / "BARRIER-ZOO.md"
PROP = ROOT / "results" / "zoo-s36" / "zoo-entries-proposed.md"
DRY = ROOT / "results" / "zoo-s36" / "dryrun-BARRIER-ZOO.md"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
ZH = sha(ZOO); DH = sha(DRY)
def run(*a):
    r = subprocess.run([sys.executable, str(SCRIPT), *map(str, a)], capture_output=True, text=True)
    msg = (r.stdout + r.stderr).strip().replace(str(ROOT) + "/", "").replace(str(SP) + "/", "$SP/")
    return r.returncode, msg
def show(tag, want_ok, rc, msg):
    ok = (rc == 0) == want_ok
    print("[%s] %s  rc=%d  expected %s\n      %s" % ("PASS" if ok else "FAIL", tag, rc, "success" if want_ok else "refusal", msg[:400].replace("\n", "\n      ")))
    return ok
allok = True
# T1 default output (input = live zoo, read only): a scratch file in the temp dir, identical to the dry run.
rc, msg = run()
tmp_out = Path(tempfile.gettempdir()).resolve() / "zoo-insert-s36-out.md"
allok &= show("T1 default --out = temp scratch file", True, rc, msg)
allok &= (sha(ZOO) == ZH); print("      zoo unchanged:", sha(ZOO) == ZH, "| temp output == dry run:", tmp_out.exists() and sha(tmp_out) == DH)
allok &= tmp_out.exists() and sha(tmp_out) == DH
if tmp_out.name == "zoo-insert-s36-out.md" and tmp_out.parent == Path(tempfile.gettempdir()).resolve():
    tmp_out.unlink()   # the one scratch file T1 created in the system temp directory
    print("      T1's scratch output removed from the system temp directory")
# T2 idempotence: the dry run as input.
rc, msg = run("--input", DRY, "--out", SP / "t2.md"); allok &= show("T2 second run on the inserted file", False, rc, msg)
# T3 hash gate: one byte changed.
t3 = SP / "t3.md"; b = bytearray(ZOO.read_bytes()); b[100] ^= 0x20; t3.write_bytes(bytes(b))
rc, msg = run("--input", t3, "--out", SP / "t3o.md"); allok &= show("T3 tampered input (one byte)", False, rc, msg)
# T4 --out BARRIER-ZOO.md without --in-place.
cp = SP / "copy4.md"; shutil.copyfile(ZOO, cp)
rc, msg = run("--input", cp, "--out", ZOO); allok &= show("T4 --out BARRIER-ZOO.md", False, rc, msg); allok &= sha(ZOO) == ZH
# T5 --out = the input.
rc, msg = run("--input", cp, "--out", cp); allok &= show("T5 --out = --input", False, rc, msg); allok &= sha(cp) == ZH
# Helpers to edit only inside the block regions of a copy of the proposed file.
ptext = PROP.read_text(encoding="utf-8")
def edit_blocks(pairs):
    def fix(m):
        body = m.group(2)
        for old, new in pairs:
            body = body.replace(old, new)
        return m.group(1) + body + m.group(3)
    return re.sub(r"(<!-- BLOCK:(?:count|iv10|iv20|xref) -->\n)(.*?)(\n<!-- END:\w+ -->)", fix, ptext, flags=re.S)
ns = {}
src = SCRIPT.read_text(encoding="utf-8")
m = re.search(r"FIX_FIRST = \((.*?)\n\)\n", src, re.S)
FF = eval("(" + m.group(1) + "\n)")
allpairs = [(o, n) for _, _, o, n in FF]
# T6 all six FIX-FIRST pairs applied.
p6 = SP / "prop-ff-all.md"; p6.write_text(edit_blocks(allpairs), encoding="utf-8")
rc, msg = run("--input", cp, "--proposed", p6, "--out", SP / "t6.md"); allok &= show("T6 FF1-FF6 applied", True, rc, msg)
# T7 a subset: FF1 and FF3.
p7 = SP / "prop-ff13.md"; p7.write_text(edit_blocks([(o, n) for t, _, o, n in FF if t in ("FF1", "FF3")]), encoding="utf-8")
rc, msg = run("--input", cp, "--proposed", p7, "--out", SP / "t7.md"); allok &= show("T7 FF1 + FF3 applied", True, rc, msg)
# T8 drift: one character in the SOURCE bullet.
p8 = SP / "prop-drift.md"; p8.write_text(edit_blocks([("[1]–[8], [11]", "[1]–[8], [10]")]), encoding="utf-8")
rc, msg = run("--input", cp, "--proposed", p8, "--out", SP / "t8.md"); allok &= show("T8 drift in SOURCE ([11] -> [10])", False, rc, msg)
# T9 drift in the row separator.
p9 = SP / "prop-xref.md"; p9.write_text(edit_blocks([("IV.20; IV.10;", "IV.20, IV.10;")]), encoding="utf-8")
rc, msg = run("--input", cp, "--proposed", p9, "--out", SP / "t9.md"); allok &= show("T9 drift in the row", False, rc, msg)
# T10 a partial FF (half a pair) must be refused.
p10 = SP / "prop-half.md"; p10.write_text(edit_blocks([("program-derived — writer", "program-adjudicated — writer")]), encoding="utf-8")
rc, msg = run("--input", cp, "--proposed", p10, "--out", SP / "t10.md"); allok &= show("T10 a pair applied in part", False, rc, msg)
# T11 in place on a scratch copy, then again.
t11 = SP / "copy11.md"; shutil.copyfile(ZOO, t11)
rc, msg = run("--input", t11, "--in-place"); allok &= show("T11a --in-place on a scratch copy", True, rc, msg)
print("      in-place result == dry run:", sha(t11) == DH); allok &= sha(t11) == DH
rc, msg = run("--input", t11, "--in-place"); allok &= show("T11b second --in-place run", False, rc, msg)
print("\nALL GATE TESTS AS EXPECTED:", bool(allok), "| BARRIER-ZOO.md still", sha(ZOO)[:16] + "…", "=", sha(ZOO) == ZH)
