#!/usr/bin/env python3
"""Print the abstract of given arXiv ids from the saved API XML files in lit/api/.
Usage: python3 abs.py ID [ID ...]   (ids without version suffix are matched by prefix)"""
import glob, os, sys, xml.etree.ElementTree as ET

LIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
want = sys.argv[1:]
seen = set()
for f in sorted(glob.glob(os.path.join(LIT, "api", "*.xml"))):
    try:
        root = ET.parse(f).getroot()
    except Exception:
        continue
    for e in root.findall("a:entry", NS):
        eid = e.find("a:id", NS).text.rsplit("/abs/", 1)[-1]
        base = eid.rsplit("v", 1)[0]
        for w in want:
            if (eid.startswith(w) or base == w) and base not in seen:
                seen.add(base)
                title = " ".join(e.find("a:title", NS).text.split())
                auth = ", ".join(a.find("a:name", NS).text for a in e.findall("a:author", NS))
                summ = " ".join(e.find("a:summary", NS).text.split())
                jr = e.find("arxiv:journal_ref", NS)
                cm = e.find("arxiv:comment", NS)
                print(f"## {eid} | {e.find('a:published', NS).text[:10]} | {title} | {auth}")
                if jr is not None: print("JREF:", " ".join(jr.text.split()))
                if cm is not None: print("COMMENT:", " ".join(cm.text.split()))
                print("ABSTRACT:", summ, "\n")
for w in want:
    if not any(s.startswith(w.rsplit('v', 1)[0]) for s in seen):
        print(f"## {w}: not in saved XML")
