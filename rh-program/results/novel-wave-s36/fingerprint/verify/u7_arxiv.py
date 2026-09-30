"""
u7_arxiv.py -- prior-art search (arXiv export API over https, one request at a time, 3 s apart, retry once a
minute on failure).  Saves raw Atom XML under verify/arxiv/ and prints id | date | title | first 300 chars.
"""
import os, sys, time, urllib.request, urllib.parse, re, json
here = os.path.dirname(os.path.abspath(__file__))
outdir = os.path.join(here, 'arxiv'); os.makedirs(outdir, exist_ok=True)
queries = [
    ('grommer', 'all:Grommer AND all:zeta'),
    ('hankel_rh', 'abs:"Hankel determinants" AND abs:"Riemann hypothesis"'),
    ('li_toeplitz', 'abs:"Li coefficients" AND (abs:Toeplitz OR abs:Caratheodory OR abs:Schur OR abs:Verblunsky)'),
    ('li_positivity', 'abs:"Li\'s criterion" AND abs:positive'),
    ('jacobi_zeros', 'abs:"Jacobi matrix" AND abs:"Riemann zeros"'),
    ('jacobi_zeta', 'abs:"Jacobi matrix" AND abs:"zeta function" AND abs:zeros'),
    ('romik', 'au:Romik AND abs:"xi function"'),
    ('cf_xi', 'abs:"continued fraction" AND abs:"Riemann xi"'),
    ('stieltjes_cf_zeros', 'abs:"continued fraction" AND abs:"zeros of the Riemann zeta"'),
    ('keiper_li', 'abs:"Keiper-Li" OR abs:"Keiper Li"'),
    ('verblunsky_zeta', 'abs:Verblunsky AND abs:zeta'),
    ('schur_zeta', 'abs:"Schur parameters" AND abs:zeta'),
    ('lagarias_positivity', 'au:Lagarias AND abs:"positivity" AND abs:xi'),
    ('power_sums_zeros', 'abs:"sums over zeros" AND abs:"Riemann zeta" AND abs:"negative powers"'),
    ('secondary_zeta', 'abs:"secondary zeta functions" OR abs:"superzeta"'),
    ('hilbert_polya_tridiagonal', 'abs:"Hilbert-Polya" AND abs:tridiagonal'),
    ('turan_jensen', 'abs:"Jensen polynomials" AND abs:"Riemann"'),
    ('spectral_transformation_euler', 'abs:"Christoffel transformation" AND abs:zeta'),
]
res = {}
for key, q in queries:
    url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': q, 'start': 0, 'max_results': 25})
    for attempt in range(30):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                data = r.read().decode('utf-8')
            break
        except Exception as e:
            print('retry', key, e, flush=True)
            time.sleep(60)
    else:
        print('FAILED', key); continue
    open(os.path.join(outdir, key + '.xml'), 'w').write(data)
    entries = re.findall(r'<entry>(.*?)</entry>', data, re.S)
    rows = []
    for e in entries:
        idm = re.search(r'<id>http[s]?://arxiv.org/abs/(.*?)</id>', e)
        tt = re.search(r'<title>(.*?)</title>', e, re.S)
        pub = re.search(r'<published>(.*?)</published>', e)
        ab = re.search(r'<summary>(.*?)</summary>', e, re.S)
        au = re.findall(r'<name>(.*?)</name>', e)
        rows.append({'id': idm.group(1) if idm else '?', 'date': pub.group(1)[:10] if pub else '?',
                     'title': ' '.join(tt.group(1).split()) if tt else '?', 'authors': au[:4],
                     'abstract': ' '.join(ab.group(1).split()) if ab else ''})
    res[key] = rows
    print('==', key, '(%d)' % len(rows), q, flush=True)
    for r in rows:
        print('  %s | %s | %s | %s' % (r['id'], r['date'], ', '.join(r['authors']), r['title']), flush=True)
    time.sleep(3)
json.dump(res, open(os.path.join(outdir, 'summary.json'), 'w'), indent=1)
print('saved')
