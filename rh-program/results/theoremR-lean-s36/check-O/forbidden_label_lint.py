#!/usr/bin/env python3
"""CHECK-O: label verbatim, forbidden phrasings, RH/zeros lines, 10(g) lint, U.S. spelling (checker-written, Session 36).

The label and the forbidden phrasings are READ from UNIT-BRIEF.md §1(3) (not typed here).  Scanned: the seven unit files of
rh-program/lean, lean/formalization.yaml, lean/README.md, and every file under results/theoremR-lean-s36/ except check-O/ (the
checker's own files are scanned separately with --self).  Comments and docstrings are INCLUDED.
"""
import re, sys, pathlib, unicodedata

RP = pathlib.Path("/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program")
U = RP / "results/theoremR-lean-s36"
brief = (U / "UNIT-BRIEF.md").read_text(encoding="utf-8")
sec = brief[brief.index("**(3) Label**"):brief.index("## §2")]
label = re.search(r"verbatim: \"(.+?)\"\. FORBIDDEN", sec, re.S).group(1)
forb_part = sec[sec.index("FORBIDDEN"):]
forbidden = re.findall(r"\"([^\"]+)\"", forb_part)
print("label (from the brief):", label)
print("forbidden phrasings (from the brief):", forbidden, "+ the clause:", forb_part.split(";")[-1].strip()[:80])

self_mode = "--self" in sys.argv
if self_mode:
    files = sorted(p for p in (U / "check-O").rglob("*") if p.is_file()) + [U / "CHECK-O.md"]
else:
    files = [RP / "lean" / f for f in ["Zeta23/ResidueRank/LogPrimes.lean", "Zeta23/ResidueRank/Pair.lean",
             "Zeta23/ResidueRank/GenusBound.lean", "comparator/Challenge/ResidueRank.lean", "comparator/Solution/ResidueRank.lean",
             "comparator/PrintAxioms/ResidueRank.lean", "comparator/config-residue-rank.json", "formalization.yaml", "README.md"]]
    files += sorted(p for p in U.rglob("*") if p.is_file() and "check-O" not in p.parts and p.name != "CHECK-O.md")

def norm(s):
    s = s.replace("**", "")
    s = re.sub(r"\s+", " ", s)
    return s

nlabel = norm(label)
BANNED = ["clearly", "obviously", "easy to see", "well known", "well-known"]
BRIT = [r"\b\w+is(e|es|ed|ing|ation|ations)\b", r"\b\w+ys(e|es|ed|ing)\b", r"colour", r"behaviour", r"favour", r"neighbour",
        r"\bcentre", r"\bmetre", r"\bfibre", r"modelling", r"labelled", r"travelled", r"cancelled", r"\bmaths\b", r"\bgrey\b",
        r"\btowards\b", r"programme", r"defence", r"offence", r"licence", r"\bpractise"]
BRIT_OK = {"otherwise", "precise", "precisely", "concise", "exercise", "exercises", "exercised", "promise", "promised", "promises",
           "premise", "premises", "raise", "raised", "raises", "noise", "wise", "likewise", "rise", "arise", "arises", "arising",
           "arisen", "surprise", "surprising", "comprise", "comprises", "comprised", "advise", "advised", "revise", "revised",
           "devise", "devised", "supervise", "expertise", "franchise", "compromise", "disguise", "enterprise", "merchandise",
           "concision", "precision", "decision", "decisions", "revision", "division", "divisions", "provision", "vision",
           "television", "excise", "incise", "incised", "demise", "improvise", "chastise", "despise", "poise", "cruise", "praise",
           "praised", "bruise", "guise", "paradise", "treatise", "anise", "valise", "reprise", "clockwise", "pairwise",
           "coordinatewise", "entrywise", "pointwise", "stepwise", "termwise", "elementwise", "componentwise", "piecewise",
           "rowwise", "columnwise", "counterclockwise", "analysed", "noisy", "ise", "Wise", "rise", "sunrise", "vise",
           "isomorphise", "imprecise", "noises", "raising", "praising", "promising", "comprising", "surprised", "surprises",
           "exercising", "otherwise's", "noise's"}
tot_forb = tot_ban = tot_brit = 0
for p in files:
    try:
        t = p.read_text(encoding="utf-8")
    except Exception as e:
        print(f"== {p.relative_to(RP)}: unreadable ({e})"); continue
    rel = p.relative_to(RP)
    nt = norm(t)
    nl = nt.count(nlabel)
    hits = []
    for f in forbidden:
        for m in re.finditer(re.escape(f), t, re.I):
            hits.append((f, t.count("\n", 0, m.start()) + 1))
    ban = [(b, t.count("\n", 0, m.start()) + 1) for b in BANNED for m in re.finditer(r"\b" + re.escape(b) + r"\b", t, re.I)]
    brit = []
    for pat in BRIT:
        for m in re.finditer(pat, t, re.I):
            w = m.group(0)
            if w.lower() in BRIT_OK or w in BRIT_OK:
                continue
            brit.append((w, t.count("\n", 0, m.start()) + 1))
    tot_forb += len(hits); tot_ban += len(ban); tot_brit += len(brit)
    print(f"== {rel}: label verbatim ×{nl}; forbidden {hits if hits else 0}; 10(g) banned {ban if ban else 0}; British {brit if brit else 0}")
    # RH / zeros lines — printed for reading (the unit's own files only; for the whole yaml/README only lines mentioning the unit)
    lines = t.splitlines()
    for i, line in enumerate(lines, 1):
        if re.search(r"\bRH\b|Riemann|\bzeros?\b|ζ", line):
            if p.name in ("formalization.yaml", "README.md"):
                window = "\n".join(lines[max(0, i - 25):i + 3])
                if not re.search(r"ResidueRank|theoremR-lean-s36|Theorem R", window):
                    continue
            neg = bool(re.search(r"\b(not|nothing|no|never|none|NOT|neither|nor|blind|without)\b|RH-blind", line))
            print(f"   {'neg' if neg else 'READ'} l.{i}: {line.strip()[:200]}")
print(f"\nTOTALS: forbidden-phrasing hits {tot_forb}; 10(g) banned hits {tot_ban}; British-spelling hits {tot_brit}")
