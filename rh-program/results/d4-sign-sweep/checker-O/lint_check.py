#!/usr/bin/env python3
"""D4 Job 2 part C.7 (Opus 5): 10(g) lint on the note and CHECK-O-B.md; U.S.-English scan of the note; standing order 7 scan
(novelty / priority / prior-art sentences) of the note. Log: logs/lint_check_run.log."""
import re, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
files = {'note': os.path.join(ROOT, 'd4-sweep-note.md'), 'CHECK-O-B': os.path.join(ROOT, 'CHECK-O-B.md')}
LINT = re.compile(r'\b(clearly|obviously|easy to see|well[- ]known|trivially)\b', re.I)
for k, p in files.items():
    hits = [(i, m.group(0), l.strip()[max(0, m.start() - 60):m.end() + 60]) for i, l in enumerate(open(p), 1) for m in LINT.finditer(l)]
    print(f'10(g) lint, {k}: {len(hits)} hits'); [print('   ', h) for h in hits]
note = open(files['note']).read(); lines = note.splitlines()
OK_ISE = {'precise', 'rise', 'otherwise', 'exercise', 'promise', 'noise', 'concise', 'raise', 'surprise', 'likewise', 'wise', 'premise', 'expertise', 'advertise', 'compromise', 'enterprise', 'franchise', 'revise', 'supervise', 'televise', 'devise', 'disguise', 'guise', 'poise', 'praise', 'arise', 'demise', 'excise', 'improvise', 'merchandise', 'paradise', 'chastise', 'despise', 'incise', 'circumcise', 'bruise', 'cruise', 'imprecise', 'clockwise', 'pairwise', 'stepwise', 'piecewise', 'elementwise', 'termwise', 'componentwise', 'pointwise', 'coordinatewise', 'arisen', 'arises', 'arising', 'raised', 'raises', 'rises', 'noises', 'precisely', 'exercised', 'promised', 'revised', 'devised', 'otherwise', 'premises', 'disguised', 'enterprise', 'rising', 'noisy'}
US = []
for i, l in enumerate(lines, 1):
    for m in re.finditer(r"\b[A-Za-z]+(?:is|ys)(?:e|es|ed|ing|ation|ations|er|ers)\b", l):
        w = m.group(0); wl = w.lower()
        if wl in OK_ISE or any(wl.startswith(s) for s in ('precis', 'rais', 'nois', 'promis', 'exercis', 'otherwis', 'surpris', 'revis', 'devis', 'disguis', 'aris', 'premis', 'compromis', 'concis', 'imprecis', 'pointwis', 'likewis')): continue
        US.append((i, w))
    for m in re.finditer(r"\b[A-Za-z]*our\b", l):
        w = m.group(0).lower()
        if w not in ('four', 'hour', 'your', 'our', 'pour', 'tour', 'flour', 'sour', 'contour', 'detour', 'fourteen'): US.append((i, m.group(0)))
    for m in re.finditer(r"\b(centre|centres|metre|metres|fibre|litre|calibre|spectre|sombre|lustre|meagre|theatre|towards|maths|grey|programme|programmes|whilst|amongst|licence|defence|offence|catalogue|modelling|modelled|labelled|labelling|travelled|cancelled|signalling|analyse|analysed|behaviour|colour|favour|neighbour|practise|judgement|acknowledgement|artefact|sceptic)\b", l, re.I):
        US.append((i, m.group(0)))
print(f'U.S. English scan of the note: {len(US)} candidates'); [print('   ', u) for u in US]
NOV = re.compile(r'\b(novel|novelty|new result|first (?:to|time|ever)|for the first time|we are the first|no one|nobody|not previously|never before|priority|unprecedented|record[- ]breaking|largest ever|highest ever|original contribution|prior art|prior-art|new mathematical)\b', re.I)
print('standing order 7 scan (novelty / priority / prior-art words) of the note:')
for i, l in enumerate(lines, 1):
    for m in NOV.finditer(l):
        print(f'   line {i}: "{m.group(0)}" … {l[max(0, m.start() - 110):m.end() + 110]!r}')
print(f'kernel scale 1/L: {1/22:.4f} at L = 22, {1/28.35:.4f} at L = 28.35')
