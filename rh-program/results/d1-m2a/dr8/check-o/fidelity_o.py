#!/usr/bin/env python3
"""Job 2 (Opus): statement fidelity + numeric-box fidelity for D-R8.

(A) The three BINDING objects of PRICING-fDH.md 3.1 -- `fDH`, `cert_of_checkW1_fDH`, `mpDH_zero`
    (and `arbDH_zero` by the pricing's "and likewise") -- are lifted OUT of the pricing's own
    fenced code blocks by regex and compared CHARACTER BY CHARACTER with the corresponding
    declarations lifted out of lean/Zeta23/W1/FDH.lean.  Whitespace is normalized only in the
    sense that a run of spaces/newlines is one space (Lean line breaks carry no meaning); every
    other character must match.  Divergences are listed, not summarized.
(B) The numeric box in mpDH_zero / arbDH_zero is compared with (i) the W1Data literal's a1/b1,
    a2/b2 in Instances.lean, and (ii) the `rect` field of the two DH live-fire transcripts, both
    parsed here by my own parsers -- no producer or checker code is imported.
(C) The 3.2 label sentence is compared character by character with the string actually carried by
    every place it is now printed.
"""
import re, json, sys, os, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
def rd(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f:
        return f.read()

fails, notes = [], []
def norm(t):
    return re.sub(r'\s+', ' ', t).strip()

PR = rd('results/d1-m2a/dr8/PRICING-fDH.md')
LN = rd('lean/Zeta23/W1/FDH.lean')

# ---------- (A) statement fidelity ----------
print("=" * 78)
print("(A) STATEMENT FIDELITY vs PRICING-fDH.md 3.1 (character by character)")
print("=" * 78)

def grab(text, kind, name, upto=None):
    """the declaration `kind name ... := ...` from `text`, statement part only (up to `:=` at
    the top level of the signature, i.e. the last `:=` before the proof)."""
    m = re.search(r'^(?:noncomputable\s+)?%s\s+%s\b' % (kind, re.escape(name)), text, re.M)
    if not m:
        return None
    start = m.start()
    # the declaration ends at the next top-level declaration keyword or a doc comment
    rest = text[start + 1:]
    e = re.search(r'\n(?:```|/--|/-!|@\[|theorem |lemma |def |noncomputable |end |import |namespace )', rest)
    end = start + 1 + (e.start() if e else len(rest))
    return text[start:end].rstrip()

def stmt_only(decl):
    """cut the proof: everything after the LAST ':=' that is not inside the statement.
    For our four objects the statement ends at the first ':=' that follows a balanced signature,
    which for `def` is the first ':=' and for `theorem` is the ':=' or ':= by' ending the type."""
    return decl

pairs = []
# fDH: the pricing block gives the def; take it from the fence that contains `def fDH`
for name, kind in [('fDH', 'def'), ('cert_of_checkW1_fDH', 'theorem'), ('mpDH_zero', 'theorem')]:
    pm = grab(PR, kind, name)
    lm = grab(LN, kind, name)
    pairs.append((name, kind, pm, lm))
# kappaDH: the pricing states it inline, not in a fence
kap_pr = re.search(r'`?(kappaDH\s*:\s*ℝ\s*:=\s*\(Real\.sqrt \(10 - 2 \* Real\.sqrt 5\) - 2\) / \(Real\.sqrt 5 - 1\))`?', PR)
pairs.append(('kappaDH', 'def', ('def ' + kap_pr.group(1)) if kap_pr else None, grab(LN, 'def', 'kappaDH')))

for name, kind, pm, lm in pairs:
    print("\n--- %s ---" % name)
    if pm is None:
        fails.append("%s: not found in PRICING 3.1" % name); print("  PRICING: NOT FOUND"); continue
    if lm is None:
        fails.append("%s: not found in FDH.lean" % name); print("  FDH.lean: NOT FOUND"); continue
    # the pricing's blocks carry the statement and (for mpDH_zero) a proof term; compare the
    # STATEMENT, i.e. everything up to and including the final ':' clause before ':='
    def sig(t, kind):
        # `def`: compare the WHOLE declaration, body included -- for fDH and kappaDH the body IS
        # the object under audit.  `theorem`: compare the statement (everything up to the ':='
        # that ends the type; our statements contain no ':=' inside the type), because the proof
        # term is the builder's business and the pricing calls only the SHAPE binding.
        if kind == 'def':
            return norm(t)
        i = t.find(':=')
        return norm(t[:i] if i >= 0 else t)
    ps, ls = sig(pm, kind), sig(lm, kind)
    if ps == ls:
        print("  IDENTICAL (%d chars, whitespace-normalized)" % len(ps))
        print("  %s" % ps)
    else:
        print("  PRICING : %s" % ps)
        print("  FDH.lean: %s" % ls)
        # character-level divergence report
        n = min(len(ps), len(ls))
        k = next((i for i in range(n) if ps[i] != ls[i]), n)
        print("  first divergence at char %d: pricing %r vs lean %r" % (k, ps[k:k+40], ls[k:k+40]))
        fails.append("%s: statement differs from PRICING 3.1" % name)

# arbDH_zero: the pricing says "and arbDH_zero likewise"; check it is mpDH_zero with mp->arb
mz, az = grab(LN, 'theorem', 'mpDH_zero'), grab(LN, 'theorem', 'arbDH_zero')
print("\n--- arbDH_zero (pricing: \"and `arbDH_zero` likewise\") ---")
def sig2(t):
    i = t.find(':=')
    return norm(t[:i] if i >= 0 else t)
if sig2(mz).replace('mpDH', 'XDH') == sig2(az).replace('arbDH', 'XDH'):
    print("  arbDH_zero is mpDH_zero with mpDH -> arbDH and nothing else. OK")
else:
    fails.append("arbDH_zero is not mpDH_zero with mpDH -> arbDH")
    print("  mp : %s" % sig2(mz)); print("  arb: %s" % sig2(az))

# ---------- (B) the numeric box ----------
print("\n" + "=" * 78)
print("(B) THE NUMERIC BOX: mpDH_zero / arbDH_zero  vs  W1Data literal  vs  transcript rect")
print("=" * 78)
INST = rd('lean/Zeta23/W1/Instances.lean')

def lean_literal(name):
    m = re.search(r'^def\s+%s\s*:\s*W1Data\s+where\s*\n((?:\s+.+\n)+)' % re.escape(name), INST, re.M)
    if not m:
        return None
    body = m.group(1)
    out = {}
    for fld in ('p1', 'q1', 'p2', 'q2', 'a1', 'b1', 'a2', 'b2', 'm', 'K', 'A'):
        mm = re.search(r'\b%s\s*:=\s*(-?\d+)' % fld, body)
        if mm:
            out[fld] = int(mm.group(1))
    return out

def transcript_rect(p):
    d = json.loads(rd(p))
    r = d['rect']
    g = lambda k: (int(r[k]['n']), int(r[k]['d']))
    return {'sigma1': g('sigma1'), 'sigma2': g('sigma2'), 'T1': g('T1'), 'T2': g('T2'),
            'claimed_m': d['claimed_m'], 'function': d['function'], 'mode': d['mode'],
            'trust_label': d['trust_label']}

# the numeric box literally written in the Lean corollary statements
box = {}
for nm in ('mpDH_zero', 'arbDH_zero'):
    t = grab(LN, 'theorem', nm)
    lo = re.search(r'\((\d+)/(\d+)\s*:\s*ℝ\)\s*<\s*ρ\.im', t)
    hi = re.search(r'ρ\.im\s*<\s*(\d+)/(\d+)', t)
    re_lo = re.search(r'(\d+)/(\d+)\s*<\s*ρ\.re', t)
    re_hi = re.search(r'ρ\.re\s*<\s*(\d+)', t)
    box[nm] = {'im_lo': (int(lo.group(1)), int(lo.group(2))) if lo else None,
               'im_hi': (int(hi.group(1)), int(hi.group(2))) if hi else None,
               're_lo': (int(re_lo.group(1)), int(re_lo.group(2))) if re_lo else None,
               're_hi': int(re_hi.group(1)) if re_hi else None}

for lean_name, cor, js in (('mpDH', 'mpDH_zero', 'results/d1-m1/acceptance/w1-mp-dh-livefire.json'),
                           ('arbDH', 'arbDH_zero', 'results/d1-m1/acceptance/w1-arb-dh-livefire.json')):
    lit = lean_literal(lean_name)
    tr = transcript_rect(js)
    b = box[cor]
    print("\n--- %s / %s / %s ---" % (lean_name, cor, os.path.basename(js)))
    print("  transcript rect : sigma1 %d/%d  sigma2 %d/%d  T1 %d/%d  T2 %d/%d  claimed_m %s  function %s  mode %s"
          % (tr['sigma1'] + tr['sigma2'] + tr['T1'] + tr['T2'] + (tr['claimed_m'], tr['function'], tr['mode'])))
    print("  Lean W1Data lit : p1/q1 %d/%d  p2/q2 %d/%d  a1/b1 %d/%d  a2/b2 %d/%d  m %d"
          % (lit['p1'], lit['q1'], lit['p2'], lit['q2'], lit['a1'], lit['b1'], lit['a2'], lit['b2'], lit['m']))
    print("  corollary box   : %s/%s < Im rho < %s/%s ;  %s/%s < Re rho < %s"
          % (b['im_lo'] + b['im_hi'] + b['re_lo'] + (b['re_hi'],)))
    checks = [
        ("literal sigma1 == transcript sigma1", (lit['p1'], lit['q1']) == tr['sigma1']),
        ("literal sigma2 == transcript sigma2", (lit['p2'], lit['q2']) == tr['sigma2']),
        ("literal T1     == transcript T1",     (lit['a1'], lit['b1']) == tr['T1']),
        ("literal T2     == transcript T2",     (lit['a2'], lit['b2']) == tr['T2']),
        ("literal m      == transcript claimed_m", str(lit['m']) == str(tr['claimed_m'])),
        ("corollary Im-lower == T1 (%d/%d)" % tr['T1'], b['im_lo'] == tr['T1']),
        ("corollary Im-upper == T2 (%d/%d)" % tr['T2'], b['im_hi'] == tr['T2']),
        ("corollary Re-lower is 1/2",            b['re_lo'] == (1, 2)),
        ("corollary Re-upper is 1",              b['re_hi'] == 1),
        ("transcript function is f_DH",          tr['function'] == 'f_DH'),
        ("transcript mode is refutation",        tr['mode'] == 'refutation'),
        ("m >= 1 (the witness branch)",          lit['m'] >= 1),
    ]
    for lbl, ok in checks:
        print("    %-45s %s" % (lbl, "OK" if ok else "MISMATCH"))
        if not ok:
            fails.append("%s: %s" % (cor, lbl))
    # the label the box sentence quotes
    if '[4/5, 41/50]' not in tr['trust_label'] or '[85.69, 85.71]' not in tr['trust_label']:
        fails.append("%s: trust_label does not quote the box it belongs to" % js)

# ---------- (C) the 3.2 label ----------
print("\n" + "=" * 78)
print("(C) THE 3.2 LABEL, character by character, everywhere it is now printed")
print("=" * 78)
m = re.search(r'\*\*"(f_DH has at least one zero.*?)"\*\*', PR, re.S)
if not m:
    fails.append("PRICING 3.2 label sentence not located"); print("  NOT FOUND in PRICING 3.2")
else:
    label = norm(m.group(1))
    print("  PRICING 3.2 (%d chars): %s" % (len(label), label))
    targets = [
        ('results/d1-m1/w1-schema.json', None),
        ('results/d1-m1/producer_mp.py', None),
        ('results/d1-m1/producer_arb.py', None),
        ('results/d1-m1/checker_ref.py', None),
        ('results/d1-m1/reference_checker.py', None),
        ('results/d1-m1/acceptance/w1-mp-dh-livefire.json', None),
        ('results/d1-m1/acceptance/w1-arb-dh-livefire.json', None),
        ('lean/Zeta23/W1/FDH.lean', None),
        ('lean/formalization.yaml', None),
        ('results/d1-m1/FORMAT.md', None),
        ('lean/README.md', None),
        ('directions/D1-certified-refutation-arm.md', None),
    ]
    for p, _ in targets:
        t = norm(rd(p))
        n = t.count(label)
        # also count with the JSON/py escapes for the apostrophe and the em dash removed
        print("    %-52s occurrences of the verbatim sentence: %d %s"
              % (p, n, "OK" if n >= 1 else "ABSENT"))
        if n < 1:
            fails.append("3.2 label sentence absent (verbatim) from %s" % p)

print("\n" + "=" * 78)
if fails:
    print("VERDICT: %d FINDING(S)" % len(fails))
    for f in fails:
        print("  - " + f)
    sys.exit(1)
print("VERDICT: PASS (no divergences)")
