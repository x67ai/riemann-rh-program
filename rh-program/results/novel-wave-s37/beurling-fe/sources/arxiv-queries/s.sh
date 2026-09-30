#!/bin/bash
# usage: s.sh "<query>" <name>  -- arxiv.org HTML search (export API timing out 2026-09-30); saves html, prints id | title
q=$(python3 -c 'import sys,urllib.parse;print(urllib.parse.quote_plus(sys.argv[1]))' "$1")
for i in $(seq 1 4); do curl -s -m 50 "https://arxiv.org/search/?query=$q&searchtype=all&abstracts=show&order=-announced_date_first&size=50" -o "$2.html" && [ -s "$2.html" ] && break; sleep 20; done
python3 - "$2.html" << 'PY'
import re,sys,html
t=open(sys.argv[1],encoding='utf-8',errors='ignore').read()
items=re.findall(r'arxiv\.org/abs/([0-9a-z.\-/]+v?\d*)">.*?<p class="title is-5 mathjax">\s*(.*?)\s*</p>',t,re.S)
print(len(items),"hits")
for i,ti in items: print(i, "|", html.unescape(re.sub(r'<[^>]+>','',ti)).strip()[:130])
PY
