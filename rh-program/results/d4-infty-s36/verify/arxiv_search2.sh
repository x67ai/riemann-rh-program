#!/bin/sh
# d4-infty-s36 novelty searches, batch 2: all-field (title+abstract+comments) phrasings, one control first.
# https, one request at a time, 3 s apart, retry about once a minute. Raw -> arxiv-searches-2.xml
DIR="$(cd "$(dirname "$0")" && pwd)"
OUT="$DIR/arxiv-searches-2.xml"
TMP="${TMPDIR:-/private/tmp}/d4s36_arxiv_q2.xml"
: > "$OUT"
i=28
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
all:%22Frobenius%20correspondences%22%20AND%20all:%22Riemann%20hypothesis%22
all:%22Frobenius%20divisors%22
all:%22self-intersection%20of%20the%20diagonal%22%20AND%20all:zeta
all:Castelnuovo%20AND%20all:%22field%20with%20one%20element%22
all:%22Hodge%20index%22%20AND%20all:%22Spec%20Z%22
all:%22Hodge%20index%22%20AND%20all:%22explicit%20formula%22
all:%22Weil%20positivity%22%20AND%20all:%22intersection%22
all:%22explicit%20formula%22%20AND%20all:%22Frobenius%22%20AND%20all:%22degree%22%20AND%20all:%22Spec%20Z%22
all:%22Beurling%22%20AND%20all:%22Hodge%20index%22
all:%22non-additive%22%20AND%20all:%22Riemann%20hypothesis%22
Q
echo "DONE $(date)" >> "$OUT"
