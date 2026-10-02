#!/usr/bin/env python3
"""Check a charter or brief for the lines KICKSTART says it is returned without (10(z)).

usage: check-brief.py FILE [--kind charter|unit|reader]     (default: guessed from the file name)

What is checked, and the rule behind each line:
  warnings   the pointer to BRIEF-WARNINGS.md                      10(p)   all kinds
  sources    a SOURCES.md beside a charter                         10(s)   charter
  stop       a line "Stop and report when"                         10(m)   charter, unit
  bearing    a line starting "Bearing" that names a contract
             clause, or a chain with steps marked proved /
             conjectured / heuristic                               10(g), 10(z)   charter, unit
  output     the clause "HARD OUTPUT RULE"                         item 16 unit, reader
  stamp      no unfilled @@NOW@@ placeholder                       10(w)   all kinds
  effort     no duration of effort given to an agent
             ("try ... for an hour")                               10(w)   all kinds
A line "WAIVED <name>: <reason>" in the file turns that check into WAIVED.
Exit 1 if any check FAILS. The orchestrator runs this before every launch and
puts the output in the live entry. It checks that the lines exist, not that
they are right: that is the reads' job.
"""
import io, os, re, sys

EFFORT = re.compile(r"\b(try|tries|work|think|attempt|spend|keep)\b[^.\n]{0,80}?\bfor (an|one|two|three|\d+) (hours?|minutes?)\b", re.I)

def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    if not a:
        sys.exit(__doc__)
    path = a[0]
    kind = None
    if "--kind" in sys.argv:
        kind = sys.argv[sys.argv.index("--kind") + 1]
        a = [x for x in a if x != kind]
        path = a[0]
    name = os.path.basename(path).upper()
    if kind is None:
        kind = "charter" if "CHARTER" in name else "reader" if "READ" in name else "unit"
    s = io.open(path, encoding="utf-8").read()
    waived = {m.group(1).lower(): m.group(2).strip() for m in re.finditer(r"WAIVED (\w+):\s*(.+)", s)}

    checks = []
    def add(key, kinds, ok, rule, detail=""):
        if kind in kinds:
            checks.append((key, ok, rule, detail))

    add("warnings", ("charter", "unit", "reader"), "BRIEF-WARNINGS.md" in s, "10(p)")
    add("sources", ("charter",), os.path.exists(os.path.join(os.path.dirname(path) or ".", "SOURCES.md")), "10(s)")
    add("stop", ("charter", "unit"), "Stop and report when" in s, "10(m)")
    bearing = [l for l in s.split("\n") if re.match(r"\s*(\*\*|#+\s*)?Bearing", l)]
    marked = any(re.search(r"clause|proved|conjectured|heuristic", l, re.I) for l in bearing)
    add("bearing", ("charter", "unit"), bool(bearing) and marked, "10(g), 10(z)",
        "" if bearing else "no line starting 'Bearing'")
    add("output", ("unit", "reader"), "HARD OUTPUT RULE" in s, "item 16")   # a charter's units get the clause in their prompts
    add("stamp", ("charter", "unit", "reader"), "@@NOW@@" not in s, "10(w)")
    m = EFFORT.search(s)
    add("effort", ("charter", "unit", "reader"), m is None, "10(w)", "" if m is None else '"%s"' % m.group(0)[:70])

    fails = 0
    print("%s  (kind: %s)" % (path, kind))
    for key, ok, rule, detail in checks:
        if ok:
            verdict = "PASS"
        elif key in waived:
            verdict = "WAIVED (%s)" % waived[key][:60]
        else:
            verdict = "FAIL"
            fails += 1
        print("  %-9s %-8s %-13s %s" % (key, verdict if len(verdict) < 9 else verdict, rule, detail))
    print("  => %s" % ("OK" if not fails else "%d FAIL" % fails))
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
