#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""zoo-s37 numbers check (writer, Opus 5.5, Session 37): every count, hash, byte comparison and record number the stream relies
on, recomputed from the files, independently of scripts/zoo-insert-s37.py and of verify/build_blocks.py (it imports neither).
Read-only on every file it opens. Usage: python3 results/zoo-s37/verify/numbers_check.py > results/zoo-s37/numbers-check.log"""
import difflib
import hashlib
import math
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ZOO = ROOT / "BARRIER-ZOO.md"
DRY = ROOT / "results/zoo-s37/dryrun-BARRIER-ZOO.md"
PROP = ROOT / "results/zoo-s37/zoo-entries-proposed.md"
BRIEF = ROOT / "results/zoo-s37/BRIEF.md"
SCRIPT = ROOT / "scripts/zoo-insert-s37.py"
BUILDER = ROOT / "results/zoo-s37/verify/build_blocks.py"
NOTE = ROOT / "results/d4-infty-s36/NOTE.md"
READF = ROOT / "results/d4-infty-s36/read-F.md"
STAGED = ROOT / "results/novel-wave-s36/ZOO-LINES-STAGED.md"
WAVE = ROOT / "results/novel-wave-s36"
CHECKO = ROOT / "results/theoremR-lean-s36/CHECK-O.md"
UBRIEF = ROOT / "results/theoremR-lean-s36/UNIT-BRIEF.md"
CERTA = ROOT / "results/haglund-cert-s37/producer-A/CERT.md"
CERTB = ROOT / "results/haglund-cert-s37/producer-B/CERT.md"
SPEC = ROOT / "results/f1-spec-s29/SPEC.md"
CHARTER37 = ROOT / "results/novel-wave-s37/WAVE-CHARTER.md"
YAML = ROOT / "lean/formalization.yaml"
LINT_S27 = ROOT / "results/zoo-s27/verify/lint_s27.py"
GATE_OUT = ROOT / "results/zoo-s37/verify/gate-tests.out"
LINT_PHRASES = ("clearly", "obviously", "easy to see", "well known", "well-known")
FAILS = []


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def check(cond, msg):
    print(("  ✓ " if cond else "  ✗ FAIL: ") + msg)
    if not cond:
        FAILS.append(msg)


def rel(p):
    return str(Path(p).relative_to(ROOT))


def norm(s):
    return re.sub(r"\s+", " ", s)


zoo = ZOO.read_text(encoding="utf-8")
dry = DRY.read_text(encoding="utf-8")
zl, dl = zoo.split("\n"), dry.split("\n")
prop = PROP.read_text(encoding="utf-8")
note = NOTE.read_text(encoding="utf-8").split("\n")
staged = STAGED.read_text(encoding="utf-8").split("\n")
brief = BRIEF.read_text(encoding="utf-8")
BLK = {m.group(1): m.group(2).split("\n") for m in re.finditer(r"<!-- BLOCK:(\w+) -->\n(.*?)\n<!-- END:\1 -->", prop, re.S)}

print("# zoo-s37 — numbers check (writer, Opus 5.5): counts, hashes, byte identity, cited entries, record numbers — %s"
      % datetime.now().strftime("%a %b %d %H:%M:%S IST %Y"))
print("\nGenerator: results/zoo-s37/verify/numbers_check.py (read-only). Every figure below is computed from the file named at run time.")

print("\n## 0. Hashes at run time")
HASHED = [ZOO, DRY, PROP, BRIEF, SCRIPT, BUILDER, NOTE, READF, STAGED] + sorted(WAVE.glob("*/NOTE.md")) + \
         sorted(WAVE.glob("*/read-F.md")) + [CHECKO, UBRIEF, CERTA, CERTB, SPEC, CHARTER37]
H = {}
for p in HASHED:
    H[p] = sha(p)
    print("  %s  %s" % (H[p], rel(p)))
check(H[ZOO] == "90d0ad6afa093388317a71cd89daf4c10ea755978943027fb61c5f06c237cc0c",
      "BARRIER-ZOO.md is the brief's input 90d0ad6afa093388… (full hash above) — stop line 1 does not fire; the zoo is untouched")
check(H[ZOO].startswith("90d0ad6afa093388") and "90d0ad6afa093388" in brief, "the brief prints the input-hash prefix 90d0ad6afa093388…")
check(H[NOTE] == "7a1dc42eb73e2f5811c84409c4564776281a71eca6edd439c6487f47f31f36ca", "the d4-infty NOTE is the file the script gates on (7a1dc42e…)")
check(H[STAGED] == "0a26acaab4cfe2a0fd32178cab34d9817e66b3030b6a2296541c0a867af6ef5d", "ZOO-LINES-STAGED.md is the file the script gates on (0a26acaa…)")
check(H[CHECKO] == "e7d5e881ee025610abb005009812863b9a2e13870b5c380b6af49a3fa8535f59",
      "CHECK-O.md = the full hash block (v) prints (e7d5e881ee025610…, the brief's prefix)")
check("`90d0ad6afa093388317a71cd89daf4c10ea755978943027fb61c5f06c237cc0c`" in "\n".join(staged[:12]),
      "the staged file's header records the same input zoo (90d0ad6a…, read 23:20)")


def tally(lines):
    return {g: sum(1 for ln in lines if re.match(r"### %s\." % g, ln)) for g in ("I", "II", "III", "IV", "V")}


print("\n## A. Heading tally (regex ^### G\\.) and line counts, before (BARRIER-ZOO.md) and after (the dry run)")
for tag, text, lines, want, n in (("before", zoo, zl, {"I": 8, "II": 5, "III": 21, "IV": 20, "V": 5}, 711),
                                   ("after ", dry, dl, {"I": 9, "II": 5, "III": 21, "IV": 22, "V": 5}, 745)):
    t = tally(lines)
    allh = sum(1 for ln in lines if ln.startswith("### "))
    print("  %s ^### I\\. %d | ^### II\\. %d | ^### III\\. %d | ^### IV\\. %d | ^### V\\. %d | ^### (all) %d | lines (\\n count) %d | "
          "bytes %d | ends with one \\n: %s" % (tag, t["I"], t["II"], t["III"], t["IV"], t["V"], allh, text.count("\n"),
                                                  len(text.encode()), text.endswith("\n") and not text.endswith("\n\n")))
    check(t == want and allh == sum(want.values()) and text.count("\n") == n,
          "%s: %s = %d headings, %d lines" % (tag.strip(), "/".join(str(want[g]) for g in want), sum(want.values()), n))
for g in ("I", "IV"):
    for tag, lines in (("before", zl), ("after ", dl)):
        print("  Group %s in file order, %s: %s" % (g, tag, [int(m.group(1)) for ln in lines for m in [re.match(r"### %s\.(\d+) " % g, ln)] if m]))
oiv = [int(m.group(1)) for ln in dl for m in [re.match(r"### IV\.(\d+) ", ln)] if m]
check(oiv == list(range(1, 16)) + [18, 16, 17, 19, 20, 21, 22], "Group IV after: IV.1–IV.15, IV.18, IV.16, IV.17, IV.19, IV.20, IV.21, IV.22")
for x, nb, na in (("IV.21", 0, 3), ("IV.22", 0, 5), ("I.9", 0, 5)):
    pat = re.compile(r"(?<![\w.])%s(?!\d)" % re.escape(x))
    b = sum(1 for ln in zl if pat.search(ln))
    a = [i + 1 for i, ln in enumerate(dl) if pat.search(ln)]
    check(b == nb and len(a) == na, "'%s' on %d lines before; on %d lines after, at %s" % (x, b, len(a), a))

print("\n## B. diff BARRIER-ZOO.md results/zoo-s37/dryrun-BARRIER-ZOO.md — hunk summary")
r = subprocess.run(["diff", str(ZOO), str(DRY)], capture_output=True, text=True)
hunks = [ln for ln in r.stdout.split("\n") if re.match(r"^\d", ln)]
print("  hunks: %s   (diff exit %d)" % (" / ".join(hunks), r.returncode))
check(all(re.match(r"^\d+a\d+(,\d+)?$", h) for h in hunks), "every hunk is a pure addition (no 'c' or 'd' hunk: nothing changed or removed)")
added = sum(1 for ln in r.stdout.split("\n") if ln.startswith("> "))
removed = sum(1 for ln in r.stdout.split("\n") if ln.startswith("< "))
check((added, removed) == (34, 0), "34 lines added, 0 removed (found %d, %d)" % (added, removed))
print("  (diff pairs each inserted leading blank line with an old blank line — 38a39,40, 133a136,143, 598a611,619 + 599a621,628 — the same file)")
it = iter(dl)
check(all(any(c == ln for c in it) for ln in zl), "every original line survives, in order, as an identical line (subsequence check)")
new_idx = []
j = 0
for i, ln in enumerate(dl):
    if j < len(zl) and ln == zl[j]:
        j += 1
    else:
        new_idx.append(i + 1)
print("  added lines in the result (greedy alignment; line: first 100 characters):")
for n in new_idx:
    print("    %d: %s" % (n, dl[n - 1][:100] if dl[n - 1] else "(blank)"))

print("\n## C. Byte identity — each block against its source line, with only the sanctioned edits")
S = lambda n: staged[n - 1]
N = lambda n: note[n - 1]
DATE = "2026-09-30"
TOKEN = "<PRODUCER-B-VERDICT>"
SPAN = ("from ONE producer (A, Arb) — the second producer of `results/haglund-cert-s37/BRIEF.md` §3 is owed before external use")
BRIEF_HEAD = ("### IV.21 The degree clause and the lattice-index kill (no square of Spec Z graded by ζ carries a real self-intersection of the "
              "diagonal) — NEW, Session 36 (`results/d4-infty-s36/NOTE.md` §2–§3; entered 2026-09-30, Session 37)")
check(BRIEF_HEAD in brief, "the IV.21 heading is verbatim in the brief (item 1)")
check(N(190) == "- **" + BRIEF_HEAD[4:].replace("; entered 2026-09-30, Session 37)", ")") + "**",
      "NOTE line 190 is the brief's heading in the NOTE's staged form ('- **…§2–§3)**')")
check(BLK["iv21"][0] == BRIEF_HEAD and BLK["iv21"][1] == "", "block iv21 heading = the brief's heading; second line blank")
for k, n in zip(range(2, 7), range(191, 196)):
    check(BLK["iv21"][k] == N(n), "block iv21 line %d == NOTE line %d byte for byte (%d bytes; %s)" % (k + 1, n, len(N(n).encode()), N(n)[:22]))
check(N(195).startswith("- **STATUS.** program-adjudicated — dual-model (writer Opus 5.5, Session 36; the orchestrator's read at the line "
                        "`read-F.md`, Session 37; the real-algebra core of Theorem S(a) kernel-checked as statements 7–8 of `ResidueRank`);"),
      "the NOTE's STATUS carries read-F's F1 NEW (the status vocabulary corrected)")
e40 = S(40).replace("### IV.21 ", "### IV.22 ", 1).replace("<ENTRY-DATE>", DATE)
check(S(40).count("IV.21") == 1 and S(40).count("<ENTRY-DATE>") == 1 and BLK["iv22"][0] == e40,
      "block iv22 heading = staged line 40 with '### IV.21 ' → '### IV.22 ' and <ENTRY-DATE> → 2026-09-30 — nothing else")
for k, n in zip(range(2, 7), range(42, 47)):
    check(BLK["iv22"][k] == S(n), "block iv22 line %d == staged line %d byte for byte (%d bytes)" % (k + 1, n, len(S(n).encode())))
check(BLK["i9"][0] == S(58).replace("<ENTRY-DATE>", DATE) and S(58).count("<ENTRY-DATE>") == 1,
      "block i9 heading = staged line 58 with <ENTRY-DATE> → 2026-09-30 — nothing else")
for k, n in zip(range(2, 7), range(60, 65)):
    check(BLK["i9"][k] == S(n), "block i9 line %d == staged line %d byte for byte (%d bytes)" % (k + 1, n, len(S(n).encode())))
check(S(52).count(SPAN) == 1 and BLK["iv9"][0] == S(52).replace("<ENTRY-DATE>", DATE).replace(SPAN, TOKEN),
      "block iv9 = staged line 52 with <ENTRY-DATE> → 2026-09-30 and the one-producer span → the token — nothing else")
check(BLK["iii15"][0] == S(70).replace("<ENTRY-DATE>", DATE) and S(70).count("<ENTRY-DATE>") == 1,
      "block iii15 = staged line 70 with <ENTRY-DATE> → 2026-09-30 — nothing else")
check(BLK["iv20"][0] == S(76), "block iv20 == staged line 76 byte for byte (%d bytes)" % len(S(76).encode()))
ROW_CELLS = ("d4-infty s36 (the (D4) residual: lattice Hodge index under the degree clause) | closed by theorem (Session 36; read at the "
             "line Session 37, dual-model) | IV.21; IV.20; III.20; IV.1; I.2")
check(('"%s"' % ROW_CELLS) in brief and BLK["xref"][0] == "| %s |" % ROW_CELLS, "xref row 1 = the brief's d4-infty cells verbatim inside '| … |'")
for k, n, c in ((1, 82, 1), (2, 83, 0), (3, 84, 1), (4, 85, 1)):
    check(S(n).count("IV.21") == c and BLK["xref"][k] == S(n).replace("IV.21", "IV.22"),
          "xref row %d = staged line %d%s" % (k + 1, n, " with IV.21 → IV.22 (once)" if c else " byte for byte"))
check(all(ln.count("|") == 4 for ln in BLK["xref"]), "each row has three cells, the table's shape")
CP = (("C0", "<ENTRY-DATE>", DATE),
      ("C1", "** IV.21 (prime channels add density", None),
      ("C2", "make **61 entries** — I: 9, II: 5, III: 21, IV: 21, V: 5", None),
      ("C3", "four cross-reference rows \"novel wave s36\"", "five cross-reference rows, \"d4-infty s36\" and four \"novel wave s36\""),
      ("C4", "711 → 736 lines if entered as staged, SHA-256 at launch <HASH>, <STREAM-FOLDER>)",
       "711 → 745 lines, SHA-256 at launch 90d0ad6a…, `results/zoo-s37/`)"))
csec = prop[prop.index("## Block `count`"):prop.index("<!-- BLOCK:count -->")]
c91, cb = S(91), BLK["count"][0]
for tag, old, new in CP:
    check(c91.count(old) == 1 and old in csec, "%s: OLD occurs once in staged line 91 and is printed in the block's section" % tag)
    if new:
        check(new in csec, "%s: NEW printed in the block's section" % tag)
sm = difflib.SequenceMatcher(None, c91, cb, autojunk=False)
regions = [(c91[i1:i2], cb[j1:j2]) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]
print("  block count vs staged line 91: %d differing regions (character level); staged %d bytes → block %d bytes"
      % (len(regions), len(c91.encode()), len(cb.encode())))
m1 = re.search(r"\*\* IV\.21 \(the degree clause and the lattice-index kill — (.*?), IV\.22 \(prime channels add density", cb)
check(m1 is not None and
      cb.replace(m1.group(0), "** IV.21 (prime channels add density").replace("make **62 entries** — I: 9, II: 5, III: 21, IV: 22, V: 5 (recounted from this file's `###` headings at insertion: 9 + 5 + 21 + 22 + 5 = 62; Group IV 20 → 22, the new entries placed after IV.20, the last Group-IV entry in file order, IV.21 before IV.22; Group I 8 → 9, placed after I.8)",
      "make **61 entries** — I: 9, II: 5, III: 21, IV: 21, V: 5 (recounted from this file's `###` headings at insertion: 9 + 5 + 21 + 21 + 5 = 61; Group IV 20 → 21, the new entry placed after IV.20, the last Group-IV entry in file order; Group I 8 → 9, placed after I.8)")
      .replace(CP[3][2], CP[3][1]).replace(CP[4][2], CP[4][1]).replace("(dated, Session 37, 2026-09-30)", "(dated, Session 37, <ENTRY-DATE>)") == c91,
      "block count reverts to staged line 91 exactly when C4, C3, C2, C1 and C0 are undone — no other change")
check(m1 is not None and m1.group(0) in csec, "C1's NEW (the d4-infty clause) is printed verbatim in the block's section")
for need in ("make **62 entries**", "I: 9, II: 5, III: 21, IV: 22, V: 5", "9 + 5 + 21 + 22 + 5 = 62",
             "Group IV 20 → 22", "Group I 8 → 9", "711 → 745 lines", "SHA-256 at launch 90d0ad6a…", "`results/zoo-s37/`", "move no count"):
    check(need in cb, "block count carries %r" % need)

print("\n## D. Every zoo entry cited by number in the new text exists (heading first words; input line, or dry-run line for the new)")
ref = re.compile(r"(?<![\w.])((?:I|II|III|IV|V)\.\d+)(?!\d)")
cited = {}
for k, v in BLK.items():
    if k == "verification":
        continue
    for x in ref.findall("\n".join(v)):
        cited.setdefault(x, set()).add(k)


def head_of(lines, x):
    hits = [(i + 1, ln) for i, ln in enumerate(lines) if ln.startswith("### %s " % x)]
    return hits


for x in sorted(cited, key=lambda s: (["I", "II", "III", "IV", "V"].index(s.split(".")[0]), int(s.split(".")[1]))):
    hi, hd = head_of(zl, x), head_of(dl, x)
    where = ("input line %d" % hi[0][0]) if hi else ("NEW — dry-run line %d" % hd[0][0] if hd else "MISSING")
    first = (hi or hd or [(0, "### %s ?" % x)])[0][1][len(x) + 5:len(x) + 5 + 60]
    check(len(hd) == 1 and len(hi) <= 1, "%s '%s…' — %s; cited in %s" % (x, first, where, ", ".join(sorted(cited[x]))))
check(sorted(x for x in cited if not head_of(zl, x)) == ["I.9", "IV.21", "IV.22"], "the only cited entries absent from the input are the three entered here")
for x in ("I.1", "I.2", "I.7", "I.8", "III.15", "III.20", "IV.1", "IV.9", "IV.10", "IV.20", "V.4", "V.5"):
    hi = head_of(zl, x)
    check(len(hi) == 1, "the brief's list: %s exists (input line %s)%s" % (x, hi[0][0] if hi else "—", "" if x in cited else " — not cited by the new text"))

print("\n## E. Record checks behind the staged words (the stream's confirmations)")
ub = UBRIEF.read_text(encoding="utf-8")
mu = re.search(r'\*\*\(3\) Label\*\*, only if everything lands with no displayed hypothesis, verbatim: "(.*?)"\. FORBIDDEN', ub)
v5 = BLK["iv20"][0]
mv = re.search(r'which the checker finds "earned verbatim": "(.*?)"\. Checker:', v5)
check(mu is not None and mv is not None and mu.group(1) == mv.group(1),
      "block iv20's label == UNIT-BRIEF §1(3)'s label, character for character (%d characters)" % (len(mv.group(1)) if mv else -1))
check(mv is not None and len(mv.group(1)) == 417, "the label is 417 characters, as the staged file's check records")
alltext = "\n".join("\n".join(v) for k, v in BLK.items() if k != "verification")
for bad in ("IV.20 is formalized", "no target exists"):
    check(bad not in alltext, "UNIT-BRIEF §1(3)'s forbidden phrasing %r occurs in no block" % bad)
co = norm(CHECKO.read_text(encoding="utf-8"))
for q in ("FIX-FIRST — prose only (F1–F3)", "the label of UNIT-BRIEF §1(3) is earned verbatim; no forbidden phrasing appears anywhere",
          "It is the B = Spec Z instance only — not the general-base Theorem R (\"if dim_Q G < ∞ then char(B) is finite\")",
          "Lemma F (a: finiteness; b)", "33/33", "3635e74", "51e6992e", "27 program declarations"):
    check(q in co, "CHECK-O.md carries %r (quoted or cited in block iv20)" % q[:90])
NEWS = {"F1 r6 (FIDELITY.md)": ("results/theoremR-lean-s36/FIDELITY.md", "weaker hypothesis at 1) — but `hmul` is demanded at the index 0 too"),
        "F1 aa1 (lean/formalization.yaml)": ("lean/formalization.yaml", "without φ(1) = 1 but over all of ℕ (index 0 included"),
        "F1 §1(5) (PREDERIVATION-ERRATA.md)": ("results/theoremR-lean-s36/PREDERIVATION-ERRATA.md", "weaker there; but `hmul` ranges over all a, b : ℕ, the index 0 included"),
        "F1 §4 (BUILD-NOTES.md)": ("results/theoremR-lean-s36/BUILD-NOTES.md", "without φ(1) = 1 but with `hmul` over all of ℕ, index 0 included (CHECK-O F1);"),
        "F2 (BUILD-NOTES.md)": ("results/theoremR-lean-s36/BUILD-NOTES.md", "(lines 104–157 of the shipped `LogPrimes.lean`, 103–156 of the rung-1 file;"),
        "F3 (PREDERIVATION-ERRATA.md)": ("results/theoremR-lean-s36/PREDERIVATION-ERRATA.md", "(For κ < 0 the hypotheses are also contradictory at every large prime — by h1 alone when g > 0; when g = 0, h1 is met by d p = log p/κ − 1 and it is h2 that fails — not needed.)")}
for tag, (f, s) in NEWS.items():
    check(s in co and norm((ROOT / f).read_text(encoding="utf-8")).count(s) >= 1, "CHECK-O §11 %s NEW string applied (found in %s)" % (tag, f))
spec = SPEC.read_text(encoding="utf-8").split("\n")
check(spec[150].startswith("**[SPEC PRECISION, 23:09 IST 2026-09-30 (Session 37)") and all(x in spec[150] for x in ("A9⁺", "A8″", "A13″")),
      "SPEC line 151: the PRECISION of 23:09 IST 2026-09-30 carries A9⁺, A8″, A13″ (IV.21's BINDS clause)")
check(norm("a genuine curve with the same (q, g) (e.g. an elliptic curve over F₅ with a = 4) must pass every line the virtual curve fails")
      in norm(CHARTER37.read_text(encoding="utf-8")), "I.9's positive control is verbatim in results/novel-wave-s37/WAVE-CHARTER.md (seed M2)")
ca = CERTA.read_text(encoding="utf-8")
for q in ("x₁ ∈ (3144.8946, 3144.8947)", "c = 3143.2206824215 + 0.3152587994 i", "**r = 4·10⁻¹¹**", "**k = 1**", "## 8. Optional H5: the seed's chain ξ_N (staircase NOTE §1, §4), N = 24"):
    check(q in ca, "producer-A CERT carries %r (the IV.9 rider's Theorem H / §8 figures)" % q)
rf = READF.read_text(encoding="utf-8")
check("AGREES-WITH-CORRECTIONS (prose only)" in rf and "Zoo: OPTION A" in rf and "(a) Zoo: Option A." in rf,
      "read-F.md: 'AGREES-WITH-CORRECTIONS (prose only)', 'Zoo: OPTION A', §3(a) 'Zoo: Option A.' (C1, the brief's decision)")
check("is equivalent, for multiplicative degrees, to" in N(191) and "(the target's graded Dirichlet series is −ζ′/ζ) and makes c injective" in N(191),
      "NOTE line 191 carries Proposition N as C1 renders it")
check("no real self-intersection of the diagonal is compatible with Castelnuovo–Severi and product adjunction, and no canonical class sits "
      "in an index-one space with Δ and the graphs" in N(198), "NOTE line 198 carries Theorem S in C1's words")
check("(B) only real zeros of the characteristic function" in zl[324], "zoo line 325 (III.15's READ) carries Newman's clause (B), as the III.15 rider says")
check(zl[480].endswith("(arithmetic: `results/zoo-s25/verify-O/r7_r0_gap_run.log`).") and zl[325].endswith("Not a 10(d) trigger.")
      and zl[131].endswith("proportion claims, anything about ζ."), "the staged map's anchor endings match zoo lines 481, 326, 132")

print("\n## F. Numbers inside the new text, recomputed (mpmath at 30 digits; exact integers where the text says so)")
import mpmath as mp
mp.mp.dps = 30
def primes_of(n):
    ps, d = [], 2
    while d * d <= n:
        if n % d == 0:
            ps.append(d)
            while n % d == 0:
                n //= d
        d += 1
    return ps + ([n] if n > 1 else [])


lam = lambda n: math.log(primes_of(n)[0]) if n > 1 and len(primes_of(n)) == 1 else 0.0  # von Mangoldt: log p on prime powers
for n, want in ((6, "1.4289"), (210, "7.2802"), (2 ** 20, "512.0")):
    g = abs(1 + n - lam(n)) / (2 * math.sqrt(n))
    check(("%.4f" % g) == want or ("%.1f" % g) == want, "IV.21 TEST (2): g*(%d) = |1 + n − Λ(n)|/(2√n) at κ = 1 = %.6f (text: %s)" % (n, g, want))
check("%.5f" % (2 * math.pi / math.log(2)) == "9.06472", "IV.22 Corollary 2: 2π/log 2 = %.6f (text: 9.06472)" % (2 * math.pi / math.log(2)))
x = 28.2 * math.log(2) / (2 * math.pi) - 1
check("%.3f" % x == "2.111" and x - 1 >= 1.1, "IV.22 TEST (1): on (−14.1, 14.1), L·log 2/2π − 1 = %.4f (text: 2.111), and 2.111 − 1 ≥ 1.1" % x)
a5 = (5 + mp.sqrt(5)) / 2
b5 = (5 - mp.sqrt(5)) / 2
check(mp.nstr(mp.log(a5) / mp.log(5), 5) == "0.79899" and mp.nstr(mp.log(b5) / mp.log(5), 5) == "0.20101" and mp.nstr(a5, 4) == "3.618",
      "I.9: zeros of 1 − 5u + 5u² at σ = log α/log 5 = %s and %s, α = %s > √5" % (mp.nstr(mp.log(a5) / mp.log(5), 8), mp.nstr(mp.log(b5) / mp.log(5), 8), mp.nstr(a5, 6)))
Nn = {}
# power sums s_n = α^n + β^n: s_0 = 2, s_1 = 5, s_n = 5 s_{n−1} − 5 s_{n−2}
s = [2, 5]
for n in range(2, 61):
    s.append(5 * s[-1] - 5 * s[-2])
for n in range(1, 61):
    Nn[n] = 1 + 5 ** n - s[n]
mob = lambda n: 0 if any(n % (q * q) == 0 for q in primes_of(n)) else (-1) ** len(primes_of(n))
bd = {d: sum(mob(d // e) * Nn[e] for e in range(1, d + 1) if d % e == 0) for d in range(1, 61)}
check(all(bd[d] % d == 0 for d in bd), "I.9: d·b_d = Σ μ(d/e) N_e is divisible by d for every d ≤ 60 (b_d integers)")
bd = {d: bd[d] // d for d in bd}
check([Nn[n] for n in range(1, 5)] == [1, 11, 76, 451] and [bd[d] for d in range(1, 6)] == [1, 5, 25, 110, 500],
      "I.9: N_N = 1, 11, 76, 451 and b_d = 1, 5, 25, 110, 500 (exact integers)")
check(all(Nn[n] >= 1 for n in Nn) and all(bd[d] >= 0 for d in bd), "I.9: N_n ≥ 1 and b_d ≥ 0 for all n, d ≤ 60 (the reader's re-run range)")
u = (-mp.mpf("2.9") + mp.sqrt(mp.mpf("2.9") ** 2 - 8)) / 4
sig, tt = -mp.log(abs(u)) / mp.log(2), mp.pi / mp.log(2)
check(mp.nstr(sig, 19) == "0.8238766801660445817" and mp.nstr(tt, 20) == "4.5323601418271938096",
      "I.9 TEST: F_{2.9,2}'s in-strip zeros at Re s = %s, t = (2j+1)·%s (text: 0.8238766801660445817, 4.5323601418271938096)" % (mp.nstr(sig, 19), mp.nstr(tt, 20)))
check(1 - 2.9 ** 2 + 2 * 2 < 1 - 2 * 2 < 0, "I.9: at (q, a) = (2, 2.9), Λ_F(q²)/log q = 1 − a² + 2q = %.2f < 1 − 2q = −3 < 0" % (1 - 2.9 ** 2 + 4))
check(9 + 5 + 21 + 22 + 5 == 62 and 2 + 8 + 1 + 1 + 1 + 8 + 8 + 5 == 34 and 711 + 34 == 745,
      "the count: 9 + 5 + 21 + 22 + 5 = 62; the lines: 2 (count) + 8 (I.9) + 1 + 1 (riders) + 1 (IV.20 bullet) + 8 + 8 (IV.21, IV.22) + 5 (rows) = 34; 711 + 34 = 745")

print("\n## G. The token and the optional pairs P1–P3 (proposed file, finding 5): each OLD once where it applies; each printed")
iv9 = BLK["iv9"][0]
check(iv9.count(TOKEN) == 1 and sum(("\n".join(v)).count(TOKEN) for v in BLK.values()) == 1, "the token occurs once, in block iv9, and nowhere else")
check(("the N = 27 counterexample rigorous (H1–H4) %s; novelty single-check" % TOKEN) in iv9, "the token's clause reads '… rigorous (H1–H4) <PRODUCER-B-VERDICT>; novelty single-check …'")
check(S(52).count(SPAN) == 1 and SPAN in prop, "the replaced one-producer span occurs once in staged line 52 and is printed in the proposed file")
for tag, where, old, new in (("P1", BLK["xref"][2], "one producer so far", None),
                             ("P2", iv9, "`results/haglund-cert-s37/producer-A/CERT.md`; entered at the Session-37 zoo stream)",
                              "`results/haglund-cert-s37/producer-A/CERT.md`, `results/haglund-cert-s37/producer-B/CERT.md`; entered at the Session-37 zoo stream)"),
                             ("P3", BLK["iv21"][6], "IV.20 as staged (Theorem R)", "IV.20 (Theorem R)")):
    check(where.count(old) == 1 and old in prop and (new is None or new in prop), "%s: OLD once in its block line; OLD%s printed in the proposed file" % (tag, "" if new is None else " and NEW"))
check(sum(ln.count("roducer") for ln in BLK["xref"]) == 1, "the only other producer statement in the new text is the N2 row's (P1)")

print("\n## H. Lint (10(g)) and U.S. English")
for k in ("count", "i9", "iii15", "iv9", "iv20", "iv21", "iv22", "xref"):
    low = "\n".join(BLK[k]).lower()
    check(not any(w in low for w in LINT_PHRASES), "block %s: none of the five linted phrases" % k)
check(not any(w in prop.lower() for w in LINT_PHRASES), "the proposed file carries none of the five phrases anywhere (blocks, findings, headings)")
r = subprocess.run([sys.executable, str(LINT_S27), str(PROP)], capture_output=True, text=True)
for ln in r.stdout.strip().split("\n"):
    print("  lint_s27.py: " + ln.replace(str(ROOT) + "/", ""))
check(r.returncode == 0, "lint_s27.py exit 0 on the proposed file (its one spelling candidate, 'spelling', is the same word in U.S. English)")
for f, nlines in ((SCRIPT, 1), (Path(__file__), 1), (BUILDER, 0), (GATE_OUT.parent / "gate_tests.py", 0)):
    hits = [i + 1 for i, ln in enumerate(f.read_text(encoding="utf-8").split("\n")) if any(w in ln.lower() for w in LINT_PHRASES)]
    check(len(hits) == nlines, "%s: the five phrases on %d line(s) %s%s" % (rel(f), len(hits), hits, " (the lint tuple itself)" if nlines else ""))

print("\n## I. Positions in the 745-line dry run (1-based)")
PP = lambda n: dl[n - 1]
for n, what, ok in ((39, "count paragraph", PP(39) == BLK["count"][0]), (41, "'---' after the header", PP(41) == "---"),
                    (136, "I.9 heading", PP(136) == BLK["i9"][0]), (138, "I.9 STATEMENT … STATUS at 138–142", [PP(k) for k in range(138, 143)] == BLK["i9"][2:]),
                    (144, "'---' closing Group I", PP(144) == "---" and PP(143) == "" and PP(146).startswith("## GROUP II")),
                    (337, "III.15 rider", PP(337) == BLK["iii15"][0] and PP(336).startswith("- **[RE-SCOUT RETURN 2026-09-24") and PP(339).startswith("### III.16 ")),
                    (493, "IV.9 rider", PP(493) == BLK["iv9"][0] and PP(492).startswith("- **[READ 2026-09-24, Opus 5:") and PP(495).startswith("### IV.10 ")),
                    (611, "IV.20 bullet (after IV.20's STATUS at 610)", PP(611) == BLK["iv20"][0] and PP(610).startswith("- **STATUS.** program-adjudicated — dual-model: writer Fable 5.1")),
                    (613, "IV.21 heading; bullets 615–619", PP(613) == BLK["iv21"][0] and [PP(k) for k in range(615, 620)] == BLK["iv21"][2:]),
                    (621, "IV.22 heading; bullets 623–627", PP(621) == BLK["iv22"][0] and [PP(k) for k in range(623, 628)] == BLK["iv22"][2:]),
                    (629, "## GROUP V", PP(629).startswith("## GROUP V — PROCESS BARRIERS") and PP(628) == ""),
                    (711, "rows 711–715 after the β-shapes row at 710", [PP(k) for k in range(711, 716)] == BLK["xref"] and PP(710).startswith("| β-shapes s35 (") and PP(716) == ""),
                    (745, "file-discipline paragraph", PP(745).startswith("*(File discipline"))):
    check(ok, "%s at line %d" % (what, n))
check([PP(k) for k in (38, 40, 135, 137, 143, 338, 494, 612, 614, 620, 622, 628, 716)] == [""] * 13,
      "blank lines at 38, 40, 135, 137, 143, 338, 494, 612, 614, 620, 622, 628, 716")

print("\n## J. Script gate tests (results/zoo-s37/verify/gate_tests.py on scratch copies; its output, verify/gate-tests.out)")
if GATE_OUT.exists():
    gl = GATE_OUT.read_text(encoding="utf-8").strip().split("\n")
    for ln in gl:
        print("  " + ln)
    check(any(ln.startswith("ALL GATE TESTS AS EXPECTED: True") for ln in gl), "every gate test behaved as expected")
else:
    check(False, "verify/gate-tests.out is absent (run gate_tests.py first)")

print("\nRESULT: %s" % ("ALL CHECKS PASS" if not FAILS else "%d CHECK(S) FAILED: %s" % (len(FAILS), "; ".join(FAILS))))
