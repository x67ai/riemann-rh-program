#!/bin/bash
# one arXiv API query with retry on 429 / rate limit; saves raw XML and prints id + title lines. Usage: arxiv_q.sh NAME 'QUERY'
N="$1"; Q="$2"
for i in $(seq 1 20); do
  curl -s -L -m 60 -G "https://export.arxiv.org/api/query" --data-urlencode "search_query=$Q" --data-urlencode "max_results=50" -o "aq-$N.xml" -w "%{http_code}" > "aq-$N.code"
  c=$(cat "aq-$N.code"); if [ "$c" = "200" ] && ! grep -q "Rate exceeded" "aq-$N.xml"; then break; fi; sleep 60
done
echo "Q[$N] = $Q  (HTTP $(cat aq-$N.code)); results: $(grep -c '<entry>' aq-$N.xml)"
python3 - "$N" <<'PY'
import sys, re
x = open(f"aq-{sys.argv[1]}.xml").read()
for e in re.findall(r"<entry>(.*?)</entry>", x, re.S):
    i = re.search(r"<id>(.*?)</id>", e).group(1).rsplit("/", 1)[-1]; t = " ".join(re.search(r"<title>(.*?)</title>", e, re.S).group(1).split())
    print(f"  {i}  {t[:150]}")
PY
rm -f "aq-$N.code"
