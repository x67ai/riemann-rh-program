# Parse arxiv-searches.xml (raw export-API responses) into arxiv-parsed.txt: query, time, totalResults, ids and titles.
import re, os
d = os.path.dirname(os.path.abspath(__file__))
raw = ''.join(open(os.path.join(d, f), encoding='utf-8', errors='replace').read() for f in ('arxiv-searches.xml', 'arxiv-searches-2.xml') if os.path.exists(os.path.join(d, f)))
blocks = re.split(r'^=== QUERY ', raw, flags=re.M)[1:]
out = []
for b in blocks:
    head = b.split('\n', 1)[0]
    m = re.match(r'(\d+): (.*?) === (.*)$', head)
    num, q, when = m.group(1), m.group(2), m.group(3)
    qd = q.replace('%22', '"').replace('%20', ' ')
    tot = re.search(r'<opensearch:totalResults[^>]*>(\d+)<', b)
    out.append(f'Q{num}: {qd} | {when}')
    out.append(f'   total = {tot.group(1) if tot else "NO RESPONSE"}')
    for e in re.findall(r'<entry>(.*?)</entry>', b, flags=re.S):
        idm = re.search(r'<id>http[s]?://arxiv.org/abs/([^<]+)</id>', e)
        tm = re.search(r'<title>(.*?)</title>', e, flags=re.S)
        out.append(f'      {idm.group(1) if idm else "?"} | {" ".join(tm.group(1).split()) if tm else "?"}')
open(os.path.join(d, 'arxiv-parsed.txt'), 'w').write('\n'.join(out) + '\n')
print('\n'.join(out))
