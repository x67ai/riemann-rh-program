#!/usr/bin/env python3
"""arXiv export-API query helper for the staircase literature read.

Usage:  python3 aq.py TAG 'search_query string (raw, will be URL-encoded)' [max_results]

- One request at a time; sleeps 3.5 s after every request (arXiv asks >= 3 s).
- On a network failure: retries once a minute, up to 20 tries.
- Saves the raw Atom XML to lit/api/TAG.xml and appends URL + hit count to lit/queries.log.
- Prints id | date | title | authors for every entry.
"""
import os, subprocess, sys, time, urllib.parse, xml.etree.ElementTree as ET, datetime

LIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NS = {"a": "http://www.w3.org/2005/Atom",
      "os": "http://a9.com/-/spec/opensearch/1.1/",
      "arxiv": "http://arxiv.org/schemas/atom"}


def fetch(url, out):
    for attempt in range(1, 21):
        r = subprocess.run(["curl", "-sS", "--max-time", "90", "-A",
                            "rh-program-literature-read/1.0 (mailto:none)",
                            "-w", "%{http_code}", "-o", out, url], capture_output=True, text=True)
        code = r.stdout.strip()
        ok = r.returncode == 0 and os.path.exists(out) and b"<feed" in open(out, "rb").read(4000)
        if ok:
            return True
        sys.stderr.write(f"attempt {attempt} failed: rc={r.returncode} http={code} {r.stderr.strip()[:200]}\n")
        if code.startswith("4") and code != "429":
            return False  # our own malformed query: do not hammer the server
        time.sleep(60)
    return False


def main():
    tag, q = sys.argv[1], sys.argv[2]
    mx = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    if q.startswith("ID_LIST:"):
        url = ("https://export.arxiv.org/api/query?id_list=" + q[len("ID_LIST:"):]
               + f"&start=0&max_results={mx}")
    else:
        url = ("https://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(q, safe=":()")
               + f"&start=0&max_results={mx}")
    out = os.path.join(LIT, "api", tag + ".xml")
    ok = fetch(url, out)
    time.sleep(3.5)
    if not ok:
        with open(os.path.join(LIT, "queries.log"), "a") as f:
            f.write(f"{datetime.datetime.now().isoformat(timespec='seconds')}\t{tag}\t{url}\tFAILED\n")
        print("FAILED"); return
    root = ET.parse(out).getroot()
    tot = root.find("os:totalResults", NS)
    total = tot.text if tot is not None else "?"
    entries = root.findall("a:entry", NS)
    with open(os.path.join(LIT, "queries.log"), "a") as f:
        f.write(f"{datetime.datetime.now().isoformat(timespec='seconds')}\t{tag}\t{url}\ttotalResults={total}\treturned={len(entries)}\n")
    print(f"totalResults={total} returned={len(entries)}  [{url}]")
    for e in entries:
        eid = e.find("a:id", NS).text.rsplit("/abs/", 1)[-1]
        pub = e.find("a:published", NS).text[:10]
        title = " ".join(e.find("a:title", NS).text.split())
        auth = ", ".join(a.find("a:name", NS).text for a in e.findall("a:author", NS))
        jr = e.find("arxiv:journal_ref", NS)
        jrs = f" || JREF: {' '.join(jr.text.split())}" if jr is not None else ""
        print(f"{eid} | {pub} | {title} | {auth}{jrs}")


if __name__ == "__main__":
    main()
