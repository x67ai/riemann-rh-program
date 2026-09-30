#!/bin/bash
# usage: s.sh "<query words>" <name>   -- arxiv.org HTML search (export API down 2026-09-30); saves html, prints id + title
q=$(echo "$1" | sed 's/ /+/g')
for i in $(seq 1 5); do curl -s -m 60 "https://arxiv.org/search/?query=$q&searchtype=all&abstracts=show&order=-announced_date_first&size=50" -o "$2.html" && [ -s "$2.html" ] && break; sleep 30; done
python3 - "$2.html" << 'PY'
import re,sys,html
t=open(sys.argv[1],encoding='utf-8',errors='ignore').read()
items=re.findall(r'arxiv\.org/abs/([0-9a-z.\-/]+v?\d*)">.*?<p class="title is-5 mathjax">\s*(.*?)\s*</p>',t,re.S)
print(len(items),"hits")
for i,ti in items: print(i, "|", html.unescape(re.sub(r'<[^>]+>','',ti)).strip()[:130])
PY
