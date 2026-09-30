#!/bin/sh
# N4 prior-art searches for DD1-DD3 (charter rule 4; zoo V.2). One request at a time, 3 s apart, retry once a minute.
OUT="$(dirname "$0")/prior_art_arxiv.xml"; TMP="$(dirname "$0")/.arxiv_tmp.xml"
: > "$OUT"
while IFS= read -r q; do
  echo "=== QUERY: $q === $(date)" >> "$OUT"
  for t in $(seq 1 60); do curl -sL --max-time 60 "https://export.arxiv.org/api/query?search_query=$q&max_results=8" > "$TMP" 2>/dev/null && grep -q "totalResults" "$TMP" && break; sleep 60; done
  cat "$TMP" >> "$OUT"; echo "" >> "$OUT"; sleep 3
done <<'Q'
all:%22Epstein%20zeta%22%20AND%20all:%22von%20Mangoldt%22
all:%22Epstein%22%20AND%20all:%22Euler%20product%22%20AND%20all:%22logarithmic%20derivative%22
all:%22von%20Mangoldt%22%20AND%20all:nonnegative%20AND%20all:%22functional%20equation%22%20AND%20all:%22Riemann%20hypothesis%22
all:%22Hasse%22%20AND%20all:%22virtual%22%20AND%20all:%22zeta%20function%22%20AND%20all:%22point%20counts%22
all:Krein%20AND%20all:%22negative%20squares%22%20AND%20all:zeta
all:%22generalized%20Nevanlinna%22%20AND%20all:%22Riemann%20hypothesis%22
all:Pick%20AND%20all:kernel%20AND%20all:%22Riemann%20hypothesis%22%20AND%20all:%22xi%22
all:%22mean%20square%22%20AND%20all:Landau%20AND%20all:%22Riemann%20hypothesis%22%20AND%20all:Mellin
all:%22tensor%20power%20trick%22%20AND%20all:%22Riemann%20hypothesis%22
all:Deligne%20AND%20all:%22Landau%22%20AND%20all:%22tensor%20power%22%20AND%20all:zeta
Q
rm -f "$TMP"
