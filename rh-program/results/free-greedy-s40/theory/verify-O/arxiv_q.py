# Opus reader: one arXiv API query (https), retried on HTTP 429 / "Rate exceeded" (60 s wait, up to 20 tries).
# Usage: python3 arxiv_q.py <outfile-stem> '<search_query>'   -> sources/<stem>.xml, prints id | date | title
import sys, time, re, urllib.request, urllib.parse, os
stem, q = sys.argv[1], sys.argv[2]
url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": q, "start": 0, "max_results": 50})
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sources", stem + ".xml")
for attempt in range(20):
    try:
        with urllib.request.urlopen(url, timeout=60) as r: t = r.read().decode("utf-8", "replace")
        if "Rate exceeded" in t or "<feed" not in t: raise RuntimeError("rate/empty")
        break
    except Exception as e:
        print("retry", attempt + 1, e, file=sys.stderr); time.sleep(60)
else:
    sys.exit("arXiv query failed 20 times")
open(out, "w").write(t)
ents = re.findall(r"<entry>(.*?)</entry>", t, re.S)
print(f"# query: {q}  -> {len(ents)} entries  (saved {os.path.basename(out)})")
for e in ents:
    i = re.search(r"<id>(.*?)</id>", e).group(1).split("/abs/")[-1]
    d = re.search(r"<published>(.*?)</published>", e).group(1)[:10]
    ti = " ".join(re.search(r"<title>(.*?)</title>", e, re.S).group(1).split())
    print(f"{i} | {d} | {ti[:120]}")
