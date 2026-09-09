#!/usr/bin/env python3
"""Job 2 (Opus): the label sweep, re-derived over BUILD-NOTES-fDH.md 3's own table.

For each file the builder's table names:
  * does it carry the PRICING 3.2 sentence verbatim (where the table says it should)?
  * does it carry a DATED 2026-09-10 block (where the table says it got one)?
  * are the never-say phrases absent, or present only inside an explicit never-say list?
  * is the superseded v1.0 f_DH string ("checker-level only ... no Lean-backed conclusion") gone
    from every live constant, and where does it survive?
Repository-wide greps for the never-say phrases follow, so a stray claim anywhere is caught.
"""
import os, re, sys, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
def rd(p):
    with open(os.path.join(ROOT, p), encoding='utf-8', errors='replace') as f:
        return f.read()
def norm(t):
    return re.sub(r'\s+', ' ', t)

PR = rd('results/d1-m2a/dr8/PRICING-fDH.md')
LABEL = norm(re.search(r'\*\*"(f_DH has at least one zero.*?)"\*\*', PR, re.S).group(1)).strip()
OLD = "checker-level only (D-R8): format-checked modulo H-ENCL for f_DH; no Lean-backed conclusion"

# BUILD-NOTES 3 table: (path, must_have_label, must_have_dated_block)
TABLE = [
    ('results/d1-m1/w1-schema.json', True, True),
    ('results/d1-m1/producer_mp.py', True, True),
    ('results/d1-m1/producer_arb.py', True, True),
    ('results/d1-m1/checker_ref.py', True, False),
    ('results/d1-m1/reference_checker.py', True, True),
    ('results/d1-m1/acceptance/w1-mp-dh-livefire.json', True, True),
    ('results/d1-m1/acceptance/w1-arb-dh-livefire.json', True, True),
    ('results/d1-m1/FORMAT.md', True, True),
    ('results/d1-m1/acceptance-report.md', False, True),
    ('directions/D1-certified-refutation-arm.md', True, True),
    ('lean/README.md', True, True),
    ('lean/Zeta23/W1/Soundness.lean', False, True),
    # not in the table but written by this build and therefore in scope:
    ('lean/Zeta23/W1/FDH.lean', True, True),
    ('lean/Zeta23/W1/Ledger.lean', False, True),
    ('lean/formalization.yaml', True, True),
    ('results/d1-m3/README.md', False, True),
    ('results/d1-m3/LEDGER.md', False, True),
]
NEVER = ["RH-for-DH disproved", "RH for DH disproved", "disproof of RH", "fully machine-checked",
         "machine-checked disproof", "RH is false", "RH disproved"]

fails, warns = [], []
print("PRICING 3.2 sentence (%d chars):\n  %s\n" % (len(LABEL), LABEL))
print("%-52s %-6s %-6s %-8s %s" % ("file", "label", "dated", "old-str", "never-say"))
print("-" * 100)
for p, want_label, want_date in TABLE:
    t = rd(p)
    tn = norm(t)
    has_label = LABEL in tn
    has_date = '2026-09-10' in t
    has_old = OLD in tn
    hits = []
    for ph in NEVER:
        for m in re.finditer(re.escape(ph), tn, re.I):
            # a hit is acceptable only inside an explicit negation / never-say context
            ctx = tn[max(0, m.start() - 220):m.end() + 120]
            neg = re.search(r'never|not |must never|does NOT say|NOT say|no claim|is not', ctx, re.I)
            hits.append((ph, bool(neg)))
    bad_hits = [h for h, n in hits if not n]
    print("%-52s %-6s %-6s %-8s %s" % (
        p,
        ("OK" if has_label else ("--" if not want_label else "ABSENT")),
        ("OK" if has_date else ("--" if not want_date else "ABSENT")),
        ("PRESENT" if has_old else "gone"),
        ("clean" if not hits else ("%d hit(s), all negated" % len(hits) if not bad_hits else "UNNEGATED: %s" % bad_hits))))
    if want_label and not has_label:
        fails.append("%s: PRICING 3.2 sentence absent" % p)
    if want_date and not has_date:
        fails.append("%s: no dated 2026-09-10 block" % p)
    if bad_hits:
        fails.append("%s: never-say phrase(s) not negated: %s" % (p, bad_hits))
    if has_old and not p.endswith('.md'):
        warns.append("%s: the superseded v1.0 f_DH string is still present" % p)

print("\nRepository-wide grep for the never-say phrases (tracked files, case-insensitive)")
for ph in NEVER:
    r = subprocess.run(['git', 'grep', '-I', '-i', '-c', ph], cwd=ROOT, capture_output=True, text=True)
    lines = [l for l in r.stdout.strip().split('\n') if l]
    print("  %-28s %d file(s)%s" % ('"%s"' % ph, len(lines), (": " + ", ".join(l.split(':')[0] for l in lines)) if lines else ""))
    for l in lines:
        f = l.split(':')[0]
        t = norm(rd(f))
        for m in re.finditer(re.escape(ph), t, re.I):
            ctx = t[max(0, m.start() - 260):m.end() + 160]
            if not re.search(r'never|not |must never|does NOT say|NOT say|no claim|is not|Never say', ctx, re.I):
                fails.append('unnegated "%s" in %s: ...%s...' % (ph, f, ctx[200:400]))

print('\nWhere the superseded v1.0 f_DH string ("checker-level only ... no Lean-backed conclusion") survives')
r = subprocess.run(['git', 'grep', '-I', '-l', 'checker-level only'], cwd=ROOT, capture_output=True, text=True)
for f in sorted(x for x in r.stdout.strip().split('\n') if x):
    t = rd(f)
    n_old = norm(t).count(OLD)
    print("  %-56s occurrences of the full v1.0 f_DH string: %d" % (f, n_old))

print("\n" + "=" * 70)
if warns:
    print("NOTES:")
    for w in warns:
        print("  ~ " + w)
print("VERDICT: %s" % ("PASS" if not fails else "%d FINDING(S)" % len(fails)))
for f in fails:
    print("  - " + f)
sys.exit(1 if fails else 0)
