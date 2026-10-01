#!/bin/zsh
# usage: arxq.sh outfile 'search_query'   (one request; retry on 429 / "Rate exceeded" every 60 s, up to 20 times)
out="sources/$1"; url="https://export.arxiv.org/api/query?search_query=$2&sortBy=submittedDate&sortOrder=descending&max_results=60"
for i in $(seq 1 20); do
  code=$(curl -s -o "$out" -w '%{http_code}' "$url")
  if [ "$code" = "200" ] && ! grep -q "Rate exceeded" "$out"; then break; fi
  echo "retry $i ($code)"; sleep 60
done
python3 - "$out" <<'PY'
import re, sys
s = open(sys.argv[1]).read()
m = re.search(r'<opensearch:totalResults[^>]*>(\d+)<', s); print("total", m.group(1) if m else "?")
for e in s.split('<entry>')[1:]:
    t = ' '.join(re.search(r'<title>(.*?)</title>', e, re.S).group(1).split()); i = re.search(r'<id>(.*?)</id>', e).group(1)
    d = re.search(r'<published>(.*?)</published>', e).group(1)[:10]
    print(d, i.split('/abs/')[1], t[:100])
PY
