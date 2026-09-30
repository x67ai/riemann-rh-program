#!/usr/bin/env python3
"""Session 35 watch poll (orchestrator, zero agents). Queries the arXiv API for every
externally pollable watch item on the SESSION 35 QUEUE (item 6 -> SESSION 34 item 6 -> SESSION 32 item 7 ->
SESSION 30 item 6, plus s32 digest §E (a)-(e)). Raw Atom saved to raw/; summary printed."""
import urllib.request, urllib.parse, time, re, sys, os, json, xml.etree.ElementTree as ET
SINCE="202609290000"; TO="202612312359"
BASE="https://export.arxiv.org/api/query?"
NS={'a':'http://www.w3.org/2005/Atom'}
OUT=os.path.join(os.path.dirname(__file__),'raw')
def fetch(params,name):
    url=BASE+urllib.parse.urlencode(params)
    for k in range(6):
        try:
            with urllib.request.urlopen(url,timeout=40) as r: data=r.read()
            open(os.path.join(OUT,name+'.xml'),'wb').write(data); return data
        except Exception as e:
            print(f"  [{name}] attempt {k+1} failed: {e}",file=sys.stderr); time.sleep(20)
    return None
def entries(data):
    if not data: return None
    root=ET.fromstring(data); out=[]
    for e in root.findall('a:entry',NS):
        out.append(dict(id=e.find('a:id',NS).text.strip(), title=' '.join(e.find('a:title',NS).text.split()),
            published=e.find('a:published',NS).text[:10], updated=e.find('a:updated',NS).text[:10],
            authors=[x.find('a:name',NS).text for x in e.findall('a:author',NS)]))
    return out
ids={'2509.09771':'Dong et al. (watch)','2609.02882':'Lamzouri (watch: later versions)',
     '2606.09096':'Suzuki screw function (rider written at v3, 23 Sep 2026)','2204.03107':'Haran (watch)','2501.14545':'BGSTB (watch: later versions; v3 at the s34 poll)','2609.20367':'Desogus (external noted s34; not a watch)'}
searches=[
 ('cc7','au:Connes AND au:Consani'),
 ('suzuki','au:Suzuki AND (all:screw OR all:"Weil" )'),
 ('exactwkb','all:"exact WKB" AND (all:zeta OR all:Riemann)'),
 ('mitkovski_poltoratski','au:Mitkovski OR au:Poltoratski'),
 ('rh_claims','all:"Riemann hypothesis" AND (all:counterexample OR all:disproof OR all:refutation OR all:"is false")'),
 ('absolute_point','all:"absolute point" OR all:"field with one element" OR all:"F_1-geometry"'),
 ('lehmer','all:"Lehmer pair" OR all:"Lehmer pairs"'),
 ('goldston_suriajaya','au:Goldston OR au:Suriajaya'),
 ('eisenberg','au:Eisenberg AND all:zeta'),
 ('gomila','au:Gomila'),
 ('lamzouri','au:Lamzouri'),
 ('prismatic','all:prismatic AND (all:Riemann OR all:zeta OR all:"Spec Z")'),
 ('krein_debranges','all:Krein AND all:"de Branges"'),
 ('borger','au:Borger'),
 ('weil_positivity','all:"Weil positivity" OR all:"Weil explicit formula" AND all:positivity'),
]
print("== ID version checks (latest version on arXiv) ==")
for aid,label in ids.items():
    d=fetch({'id_list':aid,'max_results':1},'id_'+aid.replace('.','_')); es=entries(d)
    if not es: print(f"{aid} {label}: FETCH FAILED"); continue
    e=es[0]; v=re.search(r'v(\d+)$',e['id']); print(f"{aid} {label}: latest {e['id'].split('/')[-1]}  updated {e['updated']}  published {e['published']}")
    time.sleep(3)
print(f"\n== searches, submitted since {SINCE[:4]}-{SINCE[4:6]}-{SINCE[6:8]}, newest first (max 30) ==")
for name,q in searches:
    d=fetch({'search_query':f'({q}) AND submittedDate:[{SINCE} TO {TO}]','sortBy':'submittedDate','sortOrder':'descending','max_results':30},'q_'+name)
    es=entries(d)
    if es is None: print(f"\n[{name}] FETCH FAILED"); continue
    print(f"\n[{name}] {q}  -> {len(es)} hits")
    for e in es: print(f"  {e['id'].split('/')[-1]}  {e['published']}  {'; '.join(e['authors'][:3])}{' et al.' if len(e['authors'])>3 else ''}  — {e['title'][:110]}")
    time.sleep(3)
