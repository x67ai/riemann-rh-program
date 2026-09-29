"""Checker-written (Session 33): 8 statements, challenge vs solution vs typing probe vs UNIT-BRIEF §0, and 7+5 trusted definitions.
Statement = text from `theorem <name>` to the ` := by`/` :=` that starts the proof, compared (a) byte for byte and (b) whitespace-normalized."""
import re, sys, os
C, RH = sys.argv[1], sys.argv[2]
N = "W2_eq sum_W2_mul pairRow_eq_gridRowQ sum_W2_cosh prop45 abar_sq_le floor_holds_integer floor_fails_anchor".split()
def rd(p): return open(p, encoding="utf-8").read()
def stmt(s, name):
    m = re.search(r"^theorem " + re.escape(name) + r"\b(.*?):=\s*(by|\n)", s, re.S | re.M)
    return None if not m else ("theorem " + name + m.group(1)).rstrip()
def norm(t): return re.sub(r"\s+", " ", t).strip()
ch = rd(os.path.join(C, "comparator/Challenge/PairChannel.lean"))
so = rd(os.path.join(C, "comparator/Solution/PairChannel.lean"))
pr = rd(os.path.join(RH, "results/h4-pair-typing-s32/typing-probe.lean"))
br = rd(os.path.join(RH, "results/h4-pair-typing-s32/UNIT-BRIEF.md"))
ok = True
for n in N:
    a, b, c = stmt(ch, n), stmt(so, n), stmt(pr, n)
    # brief: the backticked text starting with `<name> (` or `<name> :`
    m = re.search(r"`" + re.escape(n) + r"( [^`]*)`", br)
    bb = ("theorem " + n + m.group(1)) if m else None
    r = (a == b, a == c, norm(a) == norm(b) == norm(c), bb is not None and norm(bb) == norm(a))
    ok &= all(r[:3])
    print(f"{n:22s} ch==sol bytes:{r[0]}  ch==probe bytes:{r[1]}  normalized 3-way:{r[2]}  ==brief§0 (normalized):{r[3]}")
    if not r[3]: print("   brief:", bb); print("   chal :", norm(a))
def defn(s, name):
    m = re.search(r"^(noncomputable )?def " + re.escape(name) + r"\b.*?(?=\n\n|\n/--|\n--|\nend |\Z)", s, re.S | re.M)
    return m.group(0).rstrip() if m else None
td = rd(os.path.join(C, "comparator/ChallengeDeps/PairChannel.lean"))
ig = rd(os.path.join(C, "comparator/ChallengeDeps/IntegralityGap.lean"))
prw = rd(os.path.join(C, "Zeta23/PairCeiling/PairRow.lean"))
for n in "chi dftMark dftMarkQ zetaM gridRow gridRowQ fracMark".split():
    x, y = defn(td, n), defn(ig, n); same = x is not None and x == y; ok &= same
    print(f"trusted {n:15s} vs IntegralityGap: {'IDENTICAL' if same else 'DIFFER'} ({len(x or '')} bytes)")
for n in "W2 pairFormFactor pairRow abar vacancyMark".split():
    x, y, z = defn(td, n), defn(prw, n), defn(pr, n); same = x is not None and x == y; ok &= same
    print(f"trusted {n:15s} vs PairRow.lean: {'IDENTICAL' if same else 'DIFFER'} ({len(x or '')} bytes); vs probe: {'IDENTICAL' if x == z else 'DIFFER'}")
print("RESULT:", "PASS" if ok else "FAIL")
