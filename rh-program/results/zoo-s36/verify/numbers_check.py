#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""zoo-s36 numbers check (writer, Session 36): every count, hash, byte comparison and record number the stream relies on,
recomputed from the files, independently of scripts/zoo-insert-s36.py (which it does not import; it only reads the script's
FIX_FIRST table as text to compare it with the proposed file). Read-only on every file it opens.
Usage: python3 results/zoo-s36/verify/numbers_check.py > results/zoo-s36/numbers-check.log"""
import hashlib
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ZOO = ROOT / "BARRIER-ZOO.md"
DRY = ROOT / "results/zoo-s36/dryrun-BARRIER-ZOO.md"
PROP = ROOT / "results/zoo-s36/zoo-entries-proposed.md"
BRIEF = ROOT / "results/zoo-s36/BRIEF.md"
SCRIPT = ROOT / "scripts/zoo-insert-s36.py"
STAGED = ROOT / "results/beta-shapes-s35/ZOO-LINES-STAGED.md"
NOTE = ROOT / "results/beta-shapes-s35/NOTE.md"
READO = ROOT / "results/beta-shapes-s35/read-O.md"
SPEC = ROOT / "results/f1-spec-s29/SPEC.md"
E3 = ROOT / "results/e3-borger-rung1/NOTE.md"
X18 = ROOT / "results/beta-shapes-s35/sources-txt/x-18-deninger-2007-analogies-foliated-spaces-and-arithmetic-geometry.txt"
QLOG = ROOT / "results/beta-shapes-s35/verify-O/quote-check.log"
NLOG = ROOT / "results/beta-shapes-s35/verify/numbers-check.log"
AX1 = ROOT / "results/beta-shapes-s35/verify/arxiv_search.sh"
AX2 = ROOT / "results/beta-shapes-s35/verify/arxiv_search2.sh"
LINT_S27 = ROOT / "results/zoo-s27/verify/lint_s27.py"
GATE_OUT = ROOT / "results/zoo-s36/verify/gate-tests.out"

FAILS = []
LINT_PHRASES = ("clearly", "obviously", "easy to see", "well known", "well-known")


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def rel(p):
    return str(Path(p).relative_to(ROOT))


def check(ok, what):
    print("  %s %s" % ("✓" if ok else "✗ FAIL:", what))
    if not ok:
        FAILS.append(what)


def lines_of(p):
    return Path(p).read_text(encoding="utf-8").split("\n")


print("# zoo-s36 — numbers check (writer, Opus 5.5): counts, hashes, byte identity, record numbers — %s"
      % datetime.now().astimezone().strftime("%a %b %d %H:%M:%S %Z %Y"))
print()
print("Generator: results/zoo-s36/verify/numbers_check.py (read-only). Every figure below is computed from the file named at run time.")
print()
print("## 0. Hashes at run time")
for p in (ZOO, DRY, PROP, BRIEF, SCRIPT, STAGED, NOTE, READO, SPEC, E3):
    print("  %s  %s" % (sha(p), rel(p)))
check(sha(ZOO) == "8e66cdc0de6f13f598191b5fd10c4a2e7220ef6d1af7397dd8f4157a25bdfae8", "BARRIER-ZOO.md is the brief's input 8e66cdc0de6f13f5… (full hash above) — stop line 1 does not fire; the zoo is untouched")
check(sha(STAGED) == "bc6e241120f5af37bd55c015bed107254f11205d4c09b363b1a662172df87001", "ZOO-LINES-STAGED.md is the file the script gates on (bc6e2411…)")
check(sha(NOTE).startswith("49eb8e12"), "NOTE.md is the brief's 49eb8e12…")

# ---------------------------------------------------------------------------------------------------------------------------
print()
print("## A. Heading tally (regex, re.M) and line counts, before (BARRIER-ZOO.md) and after (the dry run)")
tz, td = ZOO.read_text(encoding="utf-8"), DRY.read_text(encoding="utf-8")
for name, t in (("before", tz), ("after", td)):
    tally = {g: len(re.findall(r"^### %s\." % g, t, re.M)) for g in ("I", "II", "III", "IV", "V")}
    total = len(re.findall(r"^### ", t, re.M))
    print("  %-6s ^### I\\. %d | ^### II\\. %d | ^### III\\. %d | ^### IV\\. %d | ^### V\\. %d | ^### (all) %d | lines (\\n count) %d | bytes %d | ends with one \\n: %s"
          % (name, tally["I"], tally["II"], tally["III"], tally["IV"], tally["V"], total, t.count("\n"), len(t.encode("utf-8")),
             t.endswith("\n") and not t.endswith("\n\n")))
    if name == "before":
        check(tally == {"I": 8, "II": 5, "III": 21, "IV": 19, "V": 5} and total == 58 and t.count("\n") == 699, "before: 8/5/21/19/5 = 58 headings, 699 lines")
    else:
        check(tally == {"I": 8, "II": 5, "III": 21, "IV": 20, "V": 5} and total == 59 and t.count("\n") == 711, "after: 8/5/21/20/5 = 59 headings, 711 lines (+12)")
order_before = [int(x) for x in re.findall(r"^### IV\.(\d+) ", tz, re.M)]
order_after = [int(x) for x in re.findall(r"^### IV\.(\d+) ", td, re.M)]
print("  Group IV in file order, before: %s" % order_before)
print("  Group IV in file order, after:  %s" % order_after)
check(order_after == order_before + [20], "IV.20 is appended after IV.19, the last Group-IV entry in file order")
check(tz.count("IV.20") == 0 and sum(1 for ln in td.split("\n") if "IV.20" in ln) == 3, "'IV.20' on 0 lines before; on 3 lines after (heading, count paragraph, row)")

# ---------------------------------------------------------------------------------------------------------------------------
print()
print("## B. diff BARRIER-ZOO.md results/zoo-s36/dryrun-BARRIER-ZOO.md — hunk summary")
r = subprocess.run(["diff", str(ZOO), str(DRY)], capture_output=True, text=True)
hunks = [ln for ln in r.stdout.split("\n") if re.match(r"^\d", ln)]
print("  hunks: %s   (diff exit %d)" % (" / ".join(hunks), r.returncode))
check(hunks == ["36a37,38", "489a492", "587a591,598", "669a681"], "four pure-addition hunks, no 'c' or 'd' hunk (nothing changed or removed)")
check(all(("a" in h and "c" not in h and "d" not in h) for h in hunks), "every hunk is an addition")
print("  (the count block was inserted as a blank line + the paragraph after line 35; diff pairs that blank with the old blank 36 and prints the paragraph + a blank as 37–38 — the same file)")
dl = td.split("\n")
print("  added lines in the result (line: first 110 characters):")
for n in (36, 37, 492, 591, 592, 593, 594, 595, 596, 597, 598, 681):
    print("    %d: %s" % (n, dl[n - 1][:110] if dl[n - 1] else "(blank)"))
zl = tz.split("\n")
it = iter(dl)
survive = all(any(c == ln for c in it) for ln in zl)
check(survive, "every original line survives, in order, as an identical line (subsequence check)")

# ---------------------------------------------------------------------------------------------------------------------------
print()
print("## C. Byte identity — staged text vs NOTE §5, and the proposed blocks vs the staged text (the two sanctioned edits only)")
S = lines_of(STAGED)
N = lines_of(NOTE)
for s, n in ((7, 223), (8, 224), (9, 225), (10, 226), (11, 227), (12, 228), (16, 232)):
    check(S[s - 1] == N[n - 1], "ZOO-LINES-STAGED.md line %d == NOTE.md line %d (%d bytes)" % (s, n, len(S[s - 1].encode("utf-8"))))
P = PROP.read_text(encoding="utf-8")


def block(name):
    ms = re.findall(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (name, name), P, re.S)
    assert len(ms) == 1, name
    return ms[0]


iv20, iv10, count, xref = block("iv20").split("\n"), block("iv10"), block("count"), block("xref")
check(len(iv20) == 7 and iv20[1] == "", "block iv20: seven lines, the second blank (heading, blank, five bullets)")
head_expected = "### " + S[6][len("- **"):-len(")**")] + "; entered 2026-09-30, Session 36)"
check(S[6].startswith("- **IV.20 ") and S[6].endswith(")**") and iv20[0] == head_expected,
      "sanctioned edit 1: heading = staged line 7 with '- **' → '### ' and ')**' → '; entered 2026-09-30, Session 36)' — nothing else")
for pos, s in ((2, 8), (3, 9), (4, 10), (5, 11)):
    check(iv20[pos] == S[s - 1], "block iv20 line %d == staged line %d byte for byte (%s)" % (pos + 1, s, S[s - 1][:22]))
OLD_V = "(verdict to be entered by the zoo stream)"
NEW_V = ("AGREES-WITH-CORRECTIONS 2026-09-29 (Theorem R PROVED from A5 + A9 with real values and one fixed κ, Euclid and unique "
         "factorization; A7 only names the fibers; converse dim_Q G ≤ |char(B)| proved by the reader; 29 OLD/NEW pairs applied "
         "2026-09-30 with each FIX-FIRST re-derived at the line by the orchestrator)")
check(S[11].count(OLD_V) == 1 and iv20[6] == S[11].replace(OLD_V, NEW_V), "sanctioned edit 2: STATUS = staged line 12 with the placeholder replaced by the verdict — nothing else")
check(iv10 == S[15], "block iv10 == staged line 16 byte for byte (%d bytes)" % len(S[15].encode("utf-8")))
B = BRIEF.read_text(encoding="utf-8")
check("The finite-rank target kill (no surface over a field, and no target of finite Q-rank, can carry ζ's diagonal row)" in B,
      "the heading's title is verbatim in the brief (item 1)")
check("— NEW, Session 35 (β-shapes, `results/beta-shapes-s35/NOTE.md` §2.3; entered 2026-09-30, Session 36)" in B,
      "the heading's tail is verbatim in the brief (item 1)")
check('"' + NEW_V + '"' in B, "the verdict string is verbatim in the brief (item 1), quotes included")
check("β-shapes s35 (finite-rank / Weil-form targets for the F₁-square; End_β = {id} bases) | closed by theorem (Session 35; dual-model) | IV.20; IV.10; III.20; V.5" in B
      and xref == "| β-shapes s35 (finite-rank / Weil-form targets for the F₁-square; End_β = {id} bases) | closed by theorem (Session 35; dual-model) | IV.20; IV.10; III.20; V.5 |",
      "block xref = the brief's three cells verbatim inside '| … |'")
check(xref.count(" | ") == 2 and xref.startswith("| ") and xref.endswith(" |"), "the row has three cells, the table's shape")
check(any(ln.startswith("| ") and "IV.19; IV.9" in ln for ln in zl), "semicolon separator precedent in the third column (row 'IV.19; IV.9 …')")

# ---------------------------------------------------------------------------------------------------------------------------
print()
print("## D. The reader's required pairs (read-O.md §4: 'with F12 and M4–M7 applied') are in the staged text")
R = lines_of(READO)


def reader_new(label):
    i = next(k for k, ln in enumerate(R) if ln.startswith("**%s (" % label))
    j = next(k for k in range(i, len(R)) if R[k].strip() == "NEW:")
    assert R[j + 1].startswith("```")
    k = next(k for k in range(j + 2, len(R)) if R[k].startswith("```"))
    return "\n".join(R[j + 2:k])


for lab, where, line in (("F12", "KILLS / RETURNS", S[8]), ("M4", "STATUS", S[11]), ("M5", "the IV.10 rider", S[15]),
                         ("M6", "STATEMENT", S[7]), ("M7", "STATUS", S[11])):
    nv = reader_new(lab)
    n = line.count(nv)
    check(n == 1, "%s NEW found %d time(s) in the staged %s line (%s…)" % (lab, n, where, nv[:60]))

# ---------------------------------------------------------------------------------------------------------------------------
print()
print("## E. Every zoo entry cited in the new text exists, by number and first words; the attributed phrases are in place")
for tag, first in (("III.20", "The S6 doubled-object rule"), ("IV.10", "Tate-curve products carry no correspondence calculus"),
                   ("IV.13", "The closed-3-manifold length-group kill"), ("V.4", "The negative-control rule"),
                   ("V.5", "The Grossmann-condition rule")):
    hits = [k + 1 for k, ln in enumerate(zl) if ln.startswith("### %s %s" % (tag, first))]
    check(len(hits) == 1, "%s '%s' at line %s" % (tag, first, hits))


def span(tag):
    a = next(k for k, ln in enumerate(zl) if ln.startswith("### %s " % tag))
    b = next(k for k in range(a + 1, len(zl)) if zl[k].startswith("### ") or zl[k].startswith("## "))
    return "\n".join(zl[a:b])


check("Deligne's squeeze additionally needs RATIONALITY" in span("III.20"), "III.20 carries \"Deligne's squeeze additionally needs RATIONALITY\" (cited in IV.20 STATUS)")
check("{log p} is Q-linearly independent" in span("IV.13") and "Q-independence kill of {log p}" in span("IV.13"), "IV.13 carries the Q-independence of {log p} (cited in IV.20 STATUS)")
check("after R-b′" in zl[24] and zl[24].startswith("**Entry count (dated, Session 29"), "'R-b′' names IV.10's 2026-09-25 rider at zoo line 25 (IV.20 SOURCE: 'IV.10 rider R-b′')")
check("V.4 reading in NOTE §2.3 DH CHECK" in S[8] and "**Negative-control reading (V.4)" in N[120], "IV.20's 'V.4 reading in NOTE §2.3 DH CHECK' is at NOTE line 121")
El = lines_of(E3)
check(El[80].startswith("**Theorem 3.4 (H3 CONFIRMED"), "E3 NOTE line 81: Theorem 3.4 (cited 'E3 Theorem 3.4')")
check("its components are not Cartier divisors and have no self-intersection numbers (Theorem 4.1(b))" in El[122], "E3 NOTE line 123: Theorem 4.1(b) is the non-Cartier statement (the rider's 'non-Cartier statement')")
check("§2.2" not in E3.read_text(encoding="utf-8") and not any(re.match(r"#+ .*\b2\.2\b", ln) for ln in El) and El[30].startswith("## §2 The prior-art gate"),
      "E3 NOTE has no §2.2 anywhere (its §2 is the prior-art gate) — FF2's ground")
SP_ = lines_of(SPEC)
for k, head in ((34, "**A2 "), (40, "**A5 "), (44, "**A7 "), (48, "**A9 "), (52, "**A11 ")):
    check(SP_[k - 1].startswith(head), "SPEC line %d: %s…" % (k, head.strip()))
check("**(A11′ — the value-group clause, forced by Theorem R.)**" in SP_[148] and "**HELD — not adopted into this SPEC:** the note's A8′" in SP_[148] and "and A13′ (items 2′–4′)" in SP_[148],
      "SPEC line 149 (PRECISION 17:20 IST 2026-09-30): A11′ adopted; A8′ and A13′ HELD — FF1's ground")
for k, head in ((62, "### 2.0 Lemma F"), (73, "### 2.1 Theorem T1"), (87, "### 2.2 Theorem T2"), (103, "### 2.3 Theorem T3"), (109, "**Theorem R (the residue-characteristic bound).**"),
                (115, "**Corollary 3.1 "), (117, "**Corollary 3.2 "), (168, "### 3.4 Two sub-shapes of (D4)")):
    check(N[k - 1].startswith(head), "NOTE line %d: %s" % (k, head))
check("N! · Z^N ⊆ L_N" in N[92] and "(b)" in N[92], "NOTE line 93 (T2 (b)): the N!-lemma, N! · Z^N ⊆ L_N (the rider's 'NOTE §2.2 (b)')")
check("(D4-fin)" in N[169], "NOTE line 170 (§3.4): the sub-shape (D4-fin)")
check(R[56].startswith("### 2.9 Novelty"), "read-O.md line 57: §2.9 Novelty (cited in IV.20 STATUS)")
nl = NLOG.read_text(encoding="utf-8")
secs = re.findall(r"^\[(\d+)[a-z]?\]", nl, re.M)
check(all(str(k) in secs for k in list(range(1, 9)) + [11]), "NOTE's verify/numbers-check.log has sections [1]–[8] and [11] (cited in SOURCE); found %s" % sorted(set(secs), key=int))

# ---------------------------------------------------------------------------------------------------------------------------
print()
print("## F. Record numbers inside the inserted text")
labels = [re.match(r"\*\*((?:F|M)\d+[a-z]?) \(", ln).group(1) for ln in R[62:356] if re.match(r"\*\*((?:F|M)\d+[a-z]?) \(", ln)]
nF = sum(1 for x in labels if x.startswith("F")); nM = sum(1 for x in labels if x.startswith("M"))
print("  read-O.md §3 pair labels (%d): %s" % (len(labels), ", ".join(labels)))
check(len(labels) == 29 and nF == 14 and nM == 15, "29 OLD/NEW pairs = 14 FIX-FIRST (F1–F14) + 15 recommended (M1, M2, M3a–M3d, M4–M12)")
check("**Overall: AGREES-WITH-CORRECTIONS.**" in R[21] and "29 OLD/NEW pairs (14 FIX-FIRST, 15 recommended)" in R[21], "read-O.md line 22: 'Overall: AGREES-WITH-CORRECTIONS … 29 OLD/NEW pairs (14 FIX-FIRST, 15 recommended)'")
check("Tue Sep 29 16:05 IST 2026" in R[0], "read-O.md line 1: the reader began Tue Sep 29 16:05 IST 2026 (the verdict's date 2026-09-29)")
check("AGREE — PROVED from A5 + A9 (real-valued, one fixed κ) + H3.3" in R[12] and "Converse proved by the reader: dim_Q G ≤ |char(B)|" in R[12], "read-O.md line 13: Theorem R PROVED from A5 + A9 (real-valued, one fixed κ); converse proved by the reader")
check("A5 (Λ on prime powers), A9 with real values and one fixed κ > 0, Euclid, unique factorization" in R[39] and "A7 is idle in Theorem R" in R[39], "read-O.md line 40: A5, A9 with real values and one fixed κ, Euclid, unique factorization; A7 idle")
check("29 OLD/NEW pairs (F1–F14, M1–M12) applied by the orchestrator on 2026-09-30, Session 36, each FIX-FIRST re-derived at the line first" in N[272], "NOTE line 273: 29 pairs applied 2026-09-30, each FIX-FIRST re-derived at the line (M1–M12 with M3 split a–d = 15)")


def heredoc_queries(p):
    t = Path(p).read_text(encoding="utf-8")
    m = re.search(r"<<'Q'\n(.*?)\nQ\n", t, re.S)
    return [q for q in m.group(1).split("\n") if q.strip()]


q1, q2 = heredoc_queries(AX1), heredoc_queries(AX2)
print("  writer's queries: arxiv_search.sh %d + arxiv_search2.sh %d = %d" % (len(q1), len(q2), len(q1) + len(q2)))
check(len(q1) + len(q2) == 22, "writer 22 arXiv queries (IV.20 STATUS)")
check("20 queries" in R[343], "reader 20 queries (read-O.md line 344)")
nums_count = {"59 entries": "**59 entries**" in count, "8/5/21/20/5": "I: 8, II: 5, III: 21, IV: 20, V: 5" in count,
              "sum": "8 + 5 + 21 + 20 + 5 = 59" in count, "19 → 20": "Group IV 19 → 20" in count, "699 → 711": "699 → 711 lines" in count,
              "launch hash": "8e66cdc0…" in count}
check(all(nums_count.values()), "count paragraph figures = the recount in §A: %s" % nums_count)

# ---------------------------------------------------------------------------------------------------------------------------
print()
print("## G. FIX-FIRST pairs FF1–FF6 (proposed file, finding 8): each OLD once in its staged line, each OLD/NEW shown in the proposed file")
src = SCRIPT.read_text(encoding="utf-8")
m = re.search(r"FIX_FIRST = \((.*?)\n\)\n", src, re.S)
FF = eval("(" + m.group(1) + "\n)")
base = {"STATEMENT": S[7], "KILLS": S[8], "TEST": S[9], "SOURCE": S[10], "STATUS": S[11].replace(OLD_V, NEW_V), "RIDER": S[15]}
for tag, where, old, new in FF:
    check(base[where].count(old) == 1 and old in P and new in P, "%s (%s): OLD once in the staged line; OLD and NEW verbatim in the proposed file" % (tag, where))
x18 = X18.read_text(encoding="utf-8", errors="replace").split("\f")[3].split("\n")
check(x18[26].strip().startswith("Number of residue characteristics |char(X )| of") and "rank of period group Λ of (X, F , φt )" in x18[26] and x18[27].strip() == "X",
      "x-18 p. 4 lines 27–28: 'Number of residue characteristics |char(X )| of' / 'X' | 'rank of period group Λ of (X, F , φt )' — FF4's ground")
check("rank of the period group" not in "\n".join(x18), "x-18 p. 4 does not print 'rank of the period group' (the staged quotation adds 'the')")
check("the N γ are not all powers of the same" in x18[19] and x18[20].startswith("number."), "x-18 p. 4 lines 20–21: 'the N γ are not all powers of the same / number' (verbatim, line break)")
check(any("Of course this makes essential use of equal characteristic" in ln for ln in QLOG.read_text(encoding="utf-8").split("\n")), "reader's quote-check.log carries Borger p. 27 'Of course this makes essential use of equal characteristic'")
check("this rider claims no Z-form of Theorems 4.1(b) or 4.2" in zl[488], "zoo line 489 (the E3 rider): 'this rider claims no Z-form of Theorems 4.1(b) or 4.2' — FF5's ground")
check(zl[488].count("NOTE") >= 6 and "`results/e3-borger-rung1/NOTE.md`" in zl[488], "zoo line 489 uses 'NOTE' %d times for results/e3-borger-rung1/NOTE.md — FF2's ground" % zl[488].count("NOTE"))
check("0801.1691 p. 5" in zl[487] and "0906.3146 p. 5" in zl[487], "zoo line 488 cites Borger at p. 5 in two papers (0801.1691, 0906.3146) — FF6's ground")
vocab = zl[6]
check(vocab.startswith("**Status vocabulary**") and "program-derived" not in tz and "`program-adjudicated`" in vocab, "zoo line 7 status vocabulary lacks 'program-derived'; no entry uses it — FF3's ground")
riders = [(k + 1, ln) for k, ln in enumerate(zl) if ln.startswith("- **[RIDER ")]
parsed = [(k, ln, re.match(r"- \*\*\[RIDER (?:[A-Z0-9]+ )?\d{4}-\d\d-\d\d, Session (\d+)", ln)) for k, ln in riders]
unparsed = [k for k, _, mm in parsed if not mm]
late = [(k, ln) for k, ln, mm in parsed if mm and int(mm.group(1)) >= 28]
print("  top-level RIDER heads: %d; dated Session 28 or later: %d; heads not of the dated shape: %s" % (len(riders), len(late), unparsed or "none"))
check(all("zoo stream" in ln.split("]**", 1)[0] for _, ln in late), "every top-level RIDER dated Session 28 or later carries '… zoo stream' in its head — FF2's second ground")
check(sum(1 for ln in zl if re.search(r"entered at the Session-\d+ zoo stream", ln)) == 37, "37 zoo lines carry 'entered at the Session-N zoo stream'")

# ---------------------------------------------------------------------------------------------------------------------------
print()
print("## H. Lint (10(g)) and U.S. English")
for name in ("count", "iv10", "iv20", "xref"):
    b = block(name).lower()
    hits = [ph for ph in LINT_PHRASES if ph in b]
    check(not hits, "block %s: none of the five linted phrases %s" % (name, hits if hits else ""))
r = subprocess.run([sys.executable, str(LINT_S27), str(PROP)], capture_output=True, text=True)
for ln in (r.stdout + r.stderr).strip().split("\n"):
    print("  lint_s27.py: " + ln.replace(str(ROOT) + "/", ""))
check(r.returncode == 0, "lint_s27.py exit 0 on the proposed file (no linted phrase in any block)")
for p in (SCRIPT, Path(__file__).resolve()):
    t = p.read_text(encoding="utf-8")
    where = [k + 1 for k, ln in enumerate(t.split("\n")) if any(ph in ln.lower() for ph in LINT_PHRASES)]
    print("  %s: the five phrases occur only on line(s) %s (the lint tuple itself)" % (rel(p), where))
    check(len(where) == 1, "%s carries the linted phrases on exactly one line, its lint tuple" % rel(p))

# ---------------------------------------------------------------------------------------------------------------------------
print()
print("## I. Positions in the 711-line dry run (1-based)")
pos = {"count paragraph": 37, "IV.10 rider": 492, "IV.20 heading": 592, "STATEMENT": 594, "KILLS / RETURNS": 595, "EXECUTABLE TEST": 596,
       "SOURCE": 597, "STATUS": 598, "## GROUP V": 600, "cross-reference row": 681}
want = {"count paragraph": count, "IV.10 rider": iv10, "IV.20 heading": iv20[0], "STATEMENT": iv20[2], "KILLS / RETURNS": iv20[3],
        "EXECUTABLE TEST": iv20[4], "SOURCE": iv20[5], "STATUS": iv20[6],
        "## GROUP V": "## GROUP V — PROCESS BARRIERS (how briefs die for non-mathematical reasons)", "cross-reference row": xref}
for k, n in pos.items():
    check(dl[n - 1] == want[k], "%s at line %d" % (k, n))
check(dl[590] == "" and dl[592] == "" and dl[598] == "" and dl[35] == "" and dl[37] == "" and dl[38] == "---" and dl[492] == "" and dl[493].startswith("### IV.11 ") and dl[681] == "",
      "blank lines at 36, 38, 493, 591, 593, 599, 682; '---' at 39; '### IV.11' at 494")
check(dl[589].startswith("- **[PRECISION READ 2026-09-26, Session 28") and dl[490].startswith("- **[RIDER 2026-09-26, Session 28 (E3 Borger rung-1 step") and dl[679].startswith("| D2 design-axis scout"),
      "anchors directly above: IV.19's PRECISION READ (590), IV.10's E3 rider (491), the D2 row (680)")

# ---------------------------------------------------------------------------------------------------------------------------
print()
print("## J. Script gate tests (results/zoo-s36/verify/gate_tests.py on scratch copies; its output, verify/gate-tests.out)")
for ln in GATE_OUT.read_text(encoding="utf-8").strip().split("\n"):
    if ln.startswith("[") or ln.startswith("ALL "):
        print("  " + ln)

print()
print("RESULT: %s" % ("ALL CHECKS PASS" if not FAILS else "%d FAIL(S): %s" % (len(FAILS), FAILS)))
