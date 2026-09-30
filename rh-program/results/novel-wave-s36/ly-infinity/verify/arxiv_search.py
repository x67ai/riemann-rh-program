"""arxiv_search.py -- prior-art search for seed N1 (ly-infinity).

Queries the arXiv export API over https, ONE request at a time, 3 s apart,
retrying once a minute on network failure (up to 30 tries).  Saves every raw
Atom response under ../sources/arxiv-queries/ and prints id | date | title | authors.
Usage: python3 arxiv_search.py "<search_query>" [max_results]
"""
import sys, time, os, re, urllib.request, urllib.parse, xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'sources', 'arxiv-queries')
os.makedirs(OUT, exist_ok=True)
NS = {'a': 'http://www.w3.org/2005/Atom'}


def fetch(q, n):
    url = ('https://export.arxiv.org/api/query?search_query=' + urllib.parse.quote(q, safe=':()"')
           + f'&start=0&max_results={n}&sortBy=relevance&sortOrder=descending')
    for attempt in range(30):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read().decode('utf-8'), url
        except Exception as e:  # network failure: wait a minute and retry
            print(f'[retry {attempt+1}] {e}', file=sys.stderr)
            time.sleep(60)
    raise SystemExit('network failure after 30 tries')


def main():
    q = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 25
    time.sleep(3)  # politeness: 3 s before every request
    xml, url = fetch(q, n)
    tag = re.sub(r'[^A-Za-z0-9]+', '_', q)[:80]
    with open(os.path.join(OUT, tag + '.xml'), 'w') as fh:
        fh.write(xml)
    root = ET.fromstring(xml)
    tot = root.find('{http://a9.com/-/spec/opensearch/1.1/}totalResults')
    print(f'QUERY {q}\nURL {url}\ntotalResults={tot.text if tot is not None else "?"}')
    for e in root.findall('a:entry', NS):
        aid = e.find('a:id', NS).text.rsplit('/', 1)[-1]
        date = e.find('a:published', NS).text[:10]
        title = ' '.join(e.find('a:title', NS).text.split())
        au = ', '.join(a.find('a:name', NS).text for a in e.findall('a:author', NS))
        print(f'{aid} | {date} | {title} | {au[:120]}')


if __name__ == '__main__':
    main()
