#!/bin/bash
# Reader-O arXiv API sweep (one request at a time, 4 s spacing, retry loop). Output: arxiv/qO-*.xml
cd "$(dirname "$0")"
i=0
while IFS= read -r q; do
  i=$((i+1)); f="qO-$i.xml"; [ -s "$f" ] && continue
  for k in $(seq 1 20); do
    curl -s -m 60 -G "http://export.arxiv.org/api/query" --data-urlencode "search_query=$q" --data-urlencode "max_results=40" -o "$f" && [ -s "$f" ] && break
    sleep 30
  done
  echo "$i | $q | $(grep -c '<entry>' "$f") entries" >> index.txt
  sleep 4
done <<'Q'
all:"sifted" AND all:"omega"
all:Beurling AND abs:"prime zeta"
all:"natural boundary" AND all:"prime zeta"
all:Beurling AND all:"mean square" AND all:integers
all:"integers free of" AND all:primes AND all:"error term"
abs:"subset of the primes" AND abs:"integers"
all:Hilberdink AND all:Beurling
all:"generalized primes" AND all:"Omega"
all:Beurling AND all:"thinning"
all:"B-free" AND all:"error term" AND all:"lower bound"
Q
