#!/usr/bin/env python3
"""Session 27 zoo stream lint (10(g)): the five linted phrases must be absent from every BLOCK of the proposed
file (and are reported for the whole file), plus a British-spelling sweep outside direct quotations is printed
for the writer to judge. Usage: python3 results/zoo-s27/verify/lint_s27.py FILE [FILE ...]"""
import re, sys, pathlib
PHRASES = ("clearly", "obviously", "easy to see", "well known", "well-known")
BRIT = re.compile(r"\b(\w+(?:ise|ised|ising|isation|our|ours|ourable|yse|ysed|ysing|elled|elling|entre|metre|litre|licence|defence|offence|practise|programme|towards|whilst|amongst|grey|maths))\b", re.I)
BRIT_OK = {"exercise", "exercises", "precise", "precisely", "concise", "promise", "premise", "premises", "otherwise", "likewise", "arise", "arises", "raise", "raised", "rise", "rises", "noise", "wise", "advise", "devise", "revise", "revised", "surprise", "comprise", "comprises", "our", "hour", "hours", "four", "pour", "tour", "detour", "contour", "contours", "flour", "sour", "tours", "colours", "vapour", "genre", "cadre", "ogre", "acre", "mediocre", "massacre", "lucre", "timbre", "louvre", "theatre", "spectre", "fibre", "sabre", "expelled", "excelled", "compelled", "propelled", "rebelled", "dispelled", "impelled", "repelled", "labelled", "entre", "chapters", "premise", "compromise", "enterprise", "franchise", "supervise", "televise", "improvise", "despise", "exercised", "practised", "practise", "meagre", "dour", "amour", "velour", "troubadour", "paramour", "tumour", "sojourn", "sour", "scour", "devour", "flavour", "cancelled", "modelled", "travelled", "fuelled", "signalled", "totalled", "levelled", "channelled", "revelled", "dialled", "spiralled", "swivelled", "pencilled", "marvelled", "quarrelled", "shrivelled", "snivelled", "shovelled", "grovelled", "hovelled", "rivalled", "equalled", "initialled", "medalled"}
rc = 0
for fn in sys.argv[1:]:
    text = pathlib.Path(fn).read_text(encoding="utf-8")
    blocks = re.findall(r"<!-- BLOCK:(\w+) -->\n(.*?)\n<!-- END:\1 -->", text, re.S)
    for name, body in blocks:
        for ph in PHRASES:
            if ph in body.lower():
                print("LINT FAIL %s block %s: %r" % (fn, name, ph)); rc = 1
    for ph in PHRASES:
        n = text.lower().count(ph)
        if n:
            print("LINT NOTE %s whole file: %r occurs %d time(s) outside/inside blocks (see above for blocks)" % (fn, ph, n))
    hits = sorted({m.group(1) for m in BRIT.finditer(text) if m.group(1).lower() not in BRIT_OK and not m.group(1).lower().endswith(("wise", "rise", "ise")) or m.group(1).lower() in ("realise","recognise","analyse","organise","normalise","characterise","summarise","prioritise","minimise","maximise","optimise","emphasise","utilise")})
    print("%s: %d block(s) checked; British-spelling candidates (judge by hand; quotations keep their source): %s" % (fn, len(blocks), hits if hits else "none"))
sys.exit(rc)
