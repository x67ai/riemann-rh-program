#!/bin/sh
# d4-infty-s36 novelty searches (standing order 7; zoo V.2). arXiv export API over https, one request at a time,
# 3 s apart, retry about once a minute on failure (patchy network). Positive controls first (V.4).
# Raw responses -> arxiv-searches.xml ; parsed by arxiv_parse.py -> arxiv-parsed.txt
DIR="$(cd "$(dirname "$0")" && pwd)"
OUT="$DIR/arxiv-searches.xml"
TMP="${TMPDIR:-/private/tmp}/d4s36_arxiv_q.xml"
: > "$OUT"
i=0
while IFS= read -r q; do
  [ -z "$q" ] && continue
  i=$((i+1))
  echo "=== QUERY $i: $q === $(date)" >> "$OUT"
  for t in $(seq 1 60); do
    curl -sL --max-time 60 "https://export.arxiv.org/api/query?search_query=$q&start=0&max_results=15" > "$TMP" 2>/dev/null && grep -q "totalResults" "$TMP" && break
    echo "   (retry $t at $(date))" >> "$OUT"; sleep 60
  done
  cat "$TMP" >> "$OUT"
  echo "" >> "$OUT"
  sleep 3
done <<'Q'
abs:%22Riemann-Roch%20strategy%22
abs:%22scaling%20site%22
ti:%22Riemann%20hypothesis%20over%20finite%20fields%22
abs:%22Castelnuovo-Severi%22
abs:%22Castelnuovo-Severi%22%20AND%20abs:%22field%20with%20one%20element%22
abs:%22Castelnuovo-Severi%22%20AND%20abs:%22Spec%20Z%22
abs:Castelnuovo%20AND%20abs:%22Riemann%20hypothesis%22%20AND%20abs:zeta
abs:Castelnuovo%20AND%20abs:%22explicit%20formula%22
abs:%22self-intersection%20of%20the%20diagonal%22%20AND%20abs:%22Riemann%20hypothesis%22
abs:%22self-intersection%20of%20the%20diagonal%22%20AND%20abs:arithmetic
abs:%22self-intersection%22%20AND%20abs:diagonal%20AND%20abs:%22Spec%20Z%22
abs:%22Hodge%20index%22%20AND%20abs:Beurling
abs:%22generalized%20primes%22%20AND%20abs:%22Hodge%20index%22
abs:Beurling%20AND%20abs:Weil%20AND%20abs:%22Riemann%20hypothesis%22%20AND%20abs:intersection
abs:%22Frobenius%20divisors%22
abs:%22Frobenius%20divisors%22%20AND%20abs:%22explicit%20formula%22
abs:%22Frobenius%20correspondences%22%20AND%20abs:%22explicit%20formula%22
abs:%22explicit%20formula%22%20AND%20abs:%22intersection%20number%22%20AND%20abs:%22Riemann%20hypothesis%22
abs:%22degree%20of%20Frobenius%22%20AND%20abs:correspondence
abs:%22Weil%20positivity%22%20AND%20abs:%22Hodge%20index%22
abs:%22equivalence%20defect%22
abs:%22infinite%20genus%22%20AND%20abs:%22Hodge%20index%22
abs:%22Weil%20criterion%22%20AND%20abs:intersection
abs:%22arithmetical%20semigroup%22%20AND%20abs:%22Riemann%20hypothesis%22
abs:Beurling%20AND%20abs:Castelnuovo
abs:%22two%20dimensional%20Riemann-Roch%22
abs:%22square%20of%20Spec%20Z%22%20AND%20abs:%22Hodge%20index%22
abs:%22Frobenius%20correspondences%22%20AND%20abs:%22degree%22%20AND%20abs:%22Riemann%20hypothesis%22
Q
echo "DONE $(date)" >> "$OUT"
