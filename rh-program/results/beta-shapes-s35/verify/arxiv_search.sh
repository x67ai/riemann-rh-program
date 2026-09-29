#!/bin/sh
# beta-shapes-s35 novelty searches (standing order 7; V.2). One request at a time, 3 s apart.
OUT="$(dirname "$0")/arxiv-searches.xml"
: > "$OUT"
i=0
while IFS= read -r q; do
  i=$((i+1))
  echo "=== QUERY $i: $q === $(date)" >> "$OUT"
  for t in $(seq 1 60); do curl -sL --max-time 60 "https://export.arxiv.org/api/query?search_query=$q&max_results=10" > /tmp/arxiv_q.xml 2>/dev/null && grep -q "totalResults" /tmp/arxiv_q.xml && break; sleep 60; done; cat /tmp/arxiv_q.xml >> "$OUT"
  echo "" >> "$OUT"
  sleep 3
done <<'Q'
all:%22field%20with%20one%20element%22%20AND%20all:%22intersection%22%20AND%20all:%22Spec%20Z%22
all:%22Witt%20vectors%22%20AND%20all:%22Riemann%20hypothesis%22%20AND%20all:intersection
all:%22square%20of%20Spec%20Z%22
all:%22residue%20characteristics%22%20AND%20all:%22Riemann%20hypothesis%22%20AND%20all:intersection
all:%22logarithms%20of%20primes%22%20AND%20all:%22linearly%20independent%22%20AND%20all:%22intersection%20number%22
all:%22lambda-ring%22%20AND%20all:Weil%20AND%20all:%22intersection%20theory%22
all:%22infinite%20genus%22%20AND%20all:%22Riemann%20hypothesis%22%20AND%20all:zeta
all:%22arithmetic%20degree%22%20AND%20all:%22von%20Mangoldt%22%20AND%20all:intersection
all:%22field%20with%20one%20element%22%20AND%20all:%22Weil%27s%20proof%22
all:%22absolute%20point%22%20AND%20all:Frobenius%20AND%20all:endomorphism%20AND%20all:%22Spec%20Z%22
all:%22Borger%22%20AND%20all:%22Witt%20space%22%20AND%20all:%22Riemann%20hypothesis%22
all:%22ghost%20components%22%20AND%20all:%22intersection%22
Q
echo "DONE $(date)" >> "$OUT"
