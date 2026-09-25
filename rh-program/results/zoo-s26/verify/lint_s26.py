#!/usr/bin/env python3
"""Session 26 queue item 2 (D3 zoo note): 10(g) lint (clearly / obviously / easy to see / well known / trivially),
a U.S.-English scan, and a standing-order-7 scan (novelty / priority / prior-art words) over the note and the proposed file.
Lines that merely NAME the linted phrases (the lint rule itself, a quoted source) are listed so the reader can see them.
Log: logs/lint_s26_run.log. Usage: python3 lint_s26.py [file ...]  (default: the two deliverables)."""
import re, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
files = sys.argv[1:] or [os.path.join(ROOT, 'd3-mobius-note.md'), os.path.join(ROOT, 'zoo-entries-proposed.md')]
LOG = os.path.join(ROOT, 'logs', 'lint_s26_run.log')
out = open(LOG, 'a')
def P(s=''):
    print(s); out.write(s + '\n')
P(f'# lint_s26.py -- {time.strftime("%a %b %d %H:%M:%S %Z %Y")}')
LINT = re.compile(r'\b(clearly|obviously|easy to see|well[- ]known|trivially)\b', re.I)
BR = re.compile(r"\b(centre|centres|metre|metres|fibre|litre|calibre|spectre|sombre|lustre|meagre|theatre|towards|maths|grey|programme|programmes|whilst|amongst|licence|defence|offence|catalogue|modelling|modelled|labelled|labelling|travelled|cancelled|signalling|analyse|analysed|analysing|behaviour|colour|favour|neighbour|honour|practise|judgement|acknowledgement|artefact|sceptic|recognise|recognised|organise|organised|normalise|normalised|summarise|summarised|emphasise|emphasised|characterise|characterised|minimise|minimised|maximise|maximised|realise|realised|parametrise|parametrised|reparametrise|reparametrised|analogue|analogues)\b", re.I)
NOV = re.compile(r'\b(novel|novelty|new result|first (?:to|time|ever)|for the first time|we are the first|not previously|never before|priority|unprecedented|prior art|prior-art|new mathematical)\b', re.I)
total = 0
for p in files:
    if not os.path.exists(p):
        P(f'{os.path.basename(p)}: MISSING'); continue
    lines = open(p, encoding='utf-8').read().splitlines()
    hits = [(i, m.group(0), l.strip()[max(0, m.start() - 70):m.end() + 70]) for i, l in enumerate(lines, 1) for m in LINT.finditer(l)]
    P(f'10(g) lint, {os.path.basename(p)} ({len(lines)} lines): {len(hits)} hit(s)')
    for h in hits: P(f'    line {h[0]} "{h[1]}": …{h[2]}…')
    total += len(hits)
    br = [(i, m.group(0)) for i, l in enumerate(lines, 1) for m in BR.finditer(l)]
    P(f'U.S.-English scan, {os.path.basename(p)}: {len(br)} candidate(s)')
    for b in br: P(f'    line {b[0]}: {b[1]}')
    nov = [(i, m.group(0), l[max(0, m.start() - 80):m.end() + 80]) for i, l in enumerate(lines, 1) for m in NOV.finditer(l)]
    P(f'standing order 7 scan (novelty / priority / prior-art words), {os.path.basename(p)}: {len(nov)} line(s) to read')
    for n in nov: P(f'    line {n[0]} "{n[1]}": …{n[2]!r}…')
P(f'TOTAL 10(g) hits over {len(files)} file(s): {total}')
out.close()
