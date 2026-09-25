import re,sys
AM=[
("A1","iv7","entered at the Session-28 zoo stream) — rider B one level up: no FINITE and no WINDOWED configuration hosts first-order (explicit-formula) equality rows either. `[novelty: dual-model check 2026-09-25]`",
 "entered at the Session-28 zoo stream) — Theorem F1: rider B one level up. `[novelty: dual-model check 2026-09-25]`"),
("A2","iv7","Scope, as rider B's: first-order EQUALITY rows with a free positive prime datum — the A4 gate's LP",
 "Scope: first-order EQUALITY rows with a free positive prime datum (rider B reaches further on PERIODIC hosts: its two-tooth rows (1.4) are strip-positive cone rows, that is, inequalities) — the A4 gate's LP"),
("A3","ii1","Label per `results/c2-m5b/read-O.md` §12 row 5: the (0.5) statement and the Poltoratski clause `[dual-model check 2026-09-25]`;",
 "Label per `results/c2-m5b/read-O.md` §12 row 5, Z-2–Z-4 applied: the (0.5) statement and the Poltoratski clause `[novelty: dual-model check 2026-09-25]` (their text is the Opus reader's Z-2 and Z-3, re-derived at read-O verdict rows 1 and 5);"),
("A4","i3","`[printed: Lagarias–Rodgers 2020 = `fetched/w-09`, Theorem 2.4 p. 3, §3 p. 4, Theorem 4.7 p. 9]` (read-O §12 row 6)",
 "`[printed: Lagarias–Rodgers 2020, Theorem 2.4 p. 3, §3 p. 4, Theorem 4.7 p. 9]` (read-O §12 row 6; the paper is `fetched/w-09`)"),
("A5","iii2","At the page the sentence is Connes–Consani 2021 (`fetched/y-03` = arXiv:2006.13771v1, p. 2):",
 "At the page the sentence is Connes–Consani's (the record's \"Connes–Consani 2021\"; the copy on disk and opened is `fetched/y-03` = arXiv:2006.13771v1, dated June 25, 2020, p. 2 — the journal version was not opened):"),
("A6","iii2","is unchanged and is Bombieri's (Theorem 12, p. 226,",
 "is unchanged and is printed in Bombieri 2000 (Theorem 12, p. 226,"),
("A7","iv19","one process at a time (D4 note lines 71, 250–254):",
 "one process at a time (D4 note lines 71, 92, 250–255):"),
("A8","iv19","and its check (`results/d4-sign-sweep/CHECK-O-B.md` line 258) passed that sentence CLEAN.",
 "and its check (`results/d4-sign-sweep/CHECK-O-B.md` line 258) passed that sentence's IV.19 item (\"does not bind — this is the evaluation route\") CLEAN."),
]
SC=[
("S1","SCOPE_RE = re.compile(r\"Scope, as rider B's: first-order EQUALITY rows with a free positive prime datum — .*?",
 "SCOPE_RE = re.compile(r\"Scope: first-order EQUALITY rows with a free positive prime datum \\(rider B reaches further on PERIODIC hosts: its two-tooth rows \\(1\\.4\\) are strip-positive cone rows, that is, inequalities\\) — .*?"),
("S2","\"`[printed: Lagarias–Rodgers 2020 = `fetched/w-09`, Theorem 2.4 p. 3, §3 p. 4, Theorem 4.7 p. 9]`\"",
 "\"`[printed: Lagarias–Rodgers 2020, Theorem 2.4 p. 3, §3 p. 4, Theorem 4.7 p. 9]`\""),
]
src,dst,ssrc,sdst,zoo_dry=sys.argv[1:6]
p=open(src,encoding="utf-8").read()
for aid,blk,old,new in AM:
    m=re.search(r"(<!-- BLOCK:%s -->\n)(.*?)(\n<!-- END:%s -->)"%(blk,blk),p,re.S)
    body=m.group(2)
    n=body.count(old); print(aid,blk,"occurrences in block:",n,"in whole file:",p.count(old))
    assert n==1
    p=p[:m.start(2)]+body.replace(old,new)+p[m.end(2):]
open(dst,"w",encoding="utf-8").write(p)
s=open(ssrc,encoding="utf-8").read()
for sid,old,new in SC:
    print(sid,"occurrences:",s.count(old)); assert s.count(old)==1
    s=s.replace(old,new)
s=s.replace('ROOT = Path(__file__).resolve().parent.parent','ROOT = Path(%r)'%__import__("os").getcwd())
s=s.replace('PROPOSED = ROOT / "results" / "zoo-s28" / "zoo-entries-proposed.md"','PROPOSED = Path(%r)'%dst)
open(sdst,"w",encoding="utf-8").write(s)
