#!/bin/sh
# beta-shapes-s35 novelty searches, batch 2: positive controls (V.4) and looser phrasings. One at a time, 3 s apart, https, retry once a minute.
OUT="$(dirname "$0")/arxiv-searches-2.xml"
: > "$OUT"
i=12
while IFS= read -r q; do
  i=$((i+1))
  echo "=== QUERY $i: $q === $(date)" >> "$OUT"
  for t in $(seq 1 60); do curl -sL --max-time 60 "https://export.arxiv.org/api/query?search_query=$q&max_results=10" > /tmp/arxiv_q2.xml 2>/dev/null && grep -q "totalResults" /tmp/arxiv_q2.xml && break; sleep 60; done; cat /tmp/arxiv_q2.xml >> "$OUT"
  echo "" >> "$OUT"
  sleep 3
done <<'Q'
all:%22field%20with%20one%20element%22
all:%22Witt%20vectors%22%20AND%20all:%22field%20with%20one%20element%22
all:Borger%20AND%20all:%22lambda-rings%22
all:%22residue%20characteristics%22%20AND%20all:%22period%20group%22
all:%22logarithms%20of%20primes%22%20AND%20all:%22linearly%20independent%22
all:%22infinite%20genus%22%20AND%20all:%22zeta%20function%22
all:%22arithmetic%20surface%22%20AND%20all:%22von%20Mangoldt%22
all:%22Spec%20Z%22%20AND%20all:%22intersection%20theory%22%20AND%20all:%22Riemann%20hypothesis%22
all:%22ghost%20map%22%20AND%20all:%22Riemann%20hypothesis%22
all:Deninger%20AND%20all:%22foliated%22%20AND%20all:%22Witt%22
Q
echo "DONE $(date)" >> "$OUT"
