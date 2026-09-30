"""lint_10g.py -- Session 36, theoremR-lean-s36 builder: the KICKSTART 10(g) lint and the UNIT-BRIEF §1(3) forbidden-phrasing check over every
file this job wrote, and over the lines it added to lean/formalization.yaml and lean/README.md (diff against the pre-edit copies given).
The four banned words/phrases are assembled from fragments and the brief's forbidden phrasings are READ FROM THE BRIEF (the quoted strings of
its §1(3) FORBIDDEN sentence), so that neither this tool nor its log quotes them.
usage: lint_10g.py <rh-program root> <yaml.pre> <README.pre>"""
import re, sys, os, difflib
root, yaml_pre, readme_pre = sys.argv[1:4]
U = os.path.join(root, "results/theoremR-lean-s36")
banned = ["clear" + "ly", "obvious" + "ly", "easy " + "to see", "well" + " known", "well" + "-known"]
brief = open(os.path.join(U, "UNIT-BRIEF.md"), encoding="utf-8").read()
fsent = brief[brief.index("FORBIDDEN phrasings"):]
fsent = fsent[:fsent.index("\n")]
forbidden = re.findall(r'"([^"]+)"', fsent)
print("forbidden phrasings read from UNIT-BRIEF §1(3): %d quoted strings (not printed); plus the clause on RH / the zeros (checked below)" % len(forbidden))
british = [r"\b\w+is(e|es|ed|ing|ation|ations)\b", r"\b\w+ys(e|es|ed|ing)\b", r"\b\w+our(s)?\b", r"\b(centre|metre|fibre|theatre)s?\b",
           r"\b\w+ll(ing|ed)\b", r"\bmaths\b", r"\bgrey\b", r"\btowards\b", r"\bprogramme\b", r"\b(defence|offence|licence)\b"]
allow = {"otherwise", "precise", "precisely", "exercise", "rise", "wise", "raise", "promise", "noise", "premise", "surprise", "revise",
         "comprise", "comprises", "compromise", "concise", "concisely", "advise", "expertise", "arise", "arises", "arising", "paradise",
         "enterprise", "devise", "disguise", "improvise", "franchise", "merchandise", "supervise", "televise", "chastise", "treatise",
         "praise", "poise", "bruise", "cruise", "guise", "likewise", "clockwise", "pairwise", "stepwise", "termwise", "entrywise",
         "coordinatewise", "elementwise", "pointwise", "componentwise", "piecewise", "rowwise", "columnwise", "noisewise", "raised",
         "promised", "revised", "exercised", "arisen", "precision", "our", "ours", "four", "hour", "hours", "your", "yours", "tour",
         "pour", "sour", "flour", "fours", "contour", "contours", "detour", "analyses", "analysed", "installing", "installed", "filled",
         "filling", "killed", "killing", "called", "calling", "spelled", "spelling", "rolled", "rolling", "polled", "polling", "pulled",
         "pulling", "stalled", "stalling", "controlled", "controlling", "compelled", "fulfilled", "fulfilling", "distilled", "billed",
         "spilled", "drilled", "skilled", "thrilled", "willing", "telling", "selling", "falling", "dwelling", "swelling", "shelled",
         "smelled", "yelled", "dispelled", "expelled", "propelled", "repelled", "rebelled", "excelled", "enrolled", "patrolled",
         "scrolled", "trolled", "tolled", "walled", "called", "recalled", "installed", "stalled", "balled", "mulled", "culled", "dulled",
         "gulled", "hulled", "lulled", "nulled", "annulled", "labelling_no"}
files = [os.path.join("results/theoremR-lean-s36", f) for f in
         ["PREDERIVATION-ERRATA.md", "BUILD-NOTES.md", "FIDELITY.md", "SHARED.md", "rung1-axioms.lean", "program-axioms.lean",
          "tools/errata_numbers.py", "tools/statement_identity_s36.py", "tools/trust_greps_s36.py", "tools/run.sh", "tools/prerun-cleanup.sh"]] + \
        ["lean/Zeta23/ResidueRank/LogPrimes.lean", "lean/Zeta23/ResidueRank/Pair.lean", "lean/Zeta23/ResidueRank/GenusBound.lean",
         "lean/comparator/Challenge/ResidueRank.lean", "lean/comparator/Solution/ResidueRank.lean",
         "lean/comparator/PrintAxioms/ResidueRank.lean", "lean/comparator/config-residue-rank.json"]
texts = [(f, open(os.path.join(root, f), encoding="utf-8").read()) for f in files]
def added(pre, cur):
    a = open(pre, encoding="utf-8").read().splitlines(); b = open(os.path.join(root, cur), encoding="utf-8").read().splitlines()
    return "\n".join(l[1:] for l in difflib.unified_diff(a, b, lineterm="", n=0) if l.startswith("+") and not l.startswith("+++"))
texts.append(("lean/formalization.yaml (added lines)", added(yaml_pre, "lean/formalization.yaml")))
texts.append(("lean/README.md (added lines)", added(readme_pre, "lean/README.md")))
bad = 0
print("== the four banned phrases (case-insensitive) — count per file")
for f, t in texts:
    n = sum(len(re.findall(re.escape(w), t, re.I)) for w in banned); bad += n
    print("%-60s %d" % (f, n))
print("== the brief's forbidden phrasings (case-insensitive) — count per file")
for f, t in texts:
    n = sum(len(re.findall(re.escape(w), t, re.I)) for w in forbidden); bad += n
    print("%-60s %d" % (f, n))
print("== RH / zeros clause: every line mentioning RH, zeros or ζ must be a disclaimer (a negation on the line) — exceptions printed")
neg = re.compile(r"\b(nothing|not|NOT|no|No|never|none|blind|RH-blind|Nothing)\b")
exc = 0
for f, t in texts:
    for i, line in enumerate(t.splitlines(), 1):
        if re.search(r"\bRH\b|\bzeros?\b|ζ", line) and not neg.search(line):
            print("   REVIEW %s:%d: %s" % (f, i, line.strip()[:160])); exc += 1
print("   lines to review:", exc)
print("== British spellings spot check (-ise/-yse/-our/-re/-ll- forms, maths, grey, towards, programme, defence/offence/licence); hits printed")
bh = 0
for f, t in texts:
    for i, line in enumerate(t.splitlines(), 1):
        for pat in british:
            for m in re.finditer(pat, line, re.I):
                w = m.group(0).lower()
                if w in allow or w.startswith("lean") or w.endswith("wise"): continue
                print("   %s:%d: %s" % (f, i, m.group(0))); bh += 1
print("   British-form hits:", bh)
print("VERDICT:", "PASS" if bad == 0 and bh == 0 else "REVIEW", "(banned + forbidden count %d; British-form hits %d; RH/zeros lines without a negation %d, reviewed by hand below)" % (bad, bh, exc))
