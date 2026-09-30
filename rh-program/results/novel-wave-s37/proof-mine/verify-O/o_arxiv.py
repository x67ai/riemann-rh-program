# Opus reader: arXiv API search, ONE request at a time, >= 3.5 s spacing, retries with backoff. Results -> verify-O/sources/.
import time, urllib.request, urllib.parse, re, os, sys
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sources'); os.makedirs(OUT, exist_ok=True)
QUERIES = [
    'all:"Gelfond-Schnirelman"',
    'all:Gelfond AND all:Schnirelman',
    'abs:"integer Chebyshev" AND abs:prime',
    'abs:"integer Chebyshev constant"',
    'all:Nair AND all:Chebyshev AND abs:prime',
    'abs:"weighted capacity" AND abs:prime',
    'abs:"least common multiple" AND abs:"prime number theorem"',
    'abs:"Chebyshev-type" AND abs:"prime number theorem" AND abs:elementary',
]
def fetch(q, tries=6):
    url = 'http://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': q, 'start': 0, 'max_results': 40,
                                                                         'sortBy': 'submittedDate', 'sortOrder': 'descending'})
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'rh-program-reader/1.0'}), timeout=60) as r:
                return r.read().decode('utf-8', 'replace')
        except Exception as e:
            print('  retry', i + 1, e, file=sys.stderr); time.sleep(10 * (i + 1))
    return ''
log = []
for j, q in enumerate(QUERIES):
    if j: time.sleep(3.5)
    x = fetch(q)
    open(os.path.join(OUT, f'arxiv_q{j}.xml'), 'w').write(x)
    ents = re.findall(r'<entry>(.*?)</entry>', x, re.S)
    log.append(f'Q{j} {q}: {len(ents)} entries')
    for e in ents:
        tid = re.search(r'<id>http://arxiv.org/abs/([^<]+)</id>', e).group(1)
        pub = re.search(r'<published>(\d{4}-\d\d)', e).group(1)
        tit = ' '.join(re.search(r'<title>(.*?)</title>', e, re.S).group(1).split())
        log.append(f'   {pub} {tid} {tit[:120]}')
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'o_arxiv.log'), 'w').write('\n'.join(log) + '\n')
print('\n'.join(log))
