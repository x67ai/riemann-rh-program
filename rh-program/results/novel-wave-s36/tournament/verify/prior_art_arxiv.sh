#!/bin/sh
# N4 prior-art searches for DD1-DD3 (charter rule 4; zoo V.2). One request at a time, 3 s apart, retry once a minute.
OUT="$(dirname "$0")/prior_art_arxiv.xml"; TMP="$(dirname "$0")/.arxiv_tmp.xml"
: > "$OUT"
while IFS= read -r q; do
  echo "=== QUERY: $q === $(date)" >> "$OUT"
  for t in $(seq 1 60); do curl -sL --max-time 60 "https://export.arxiv.org/api/query?search_query=$q&max_results=8" > "$TMP" 2>/dev/null && grep -q "totalResults" "$TMP" && break; sleep 60; done
  cat "$TMP" >> "$OUT"; echo "" >> "$OUT"; sleep 3
done <<'Q'
ti:Epstein+AND+ti:zeta
abs:%22von%20Mangoldt%22+AND+abs:Epstein
abs:%22Euler%20product%22+AND+abs:%22Epstein%22+AND+abs:%22Riemann%20hypothesis%22
abs:%22Weil%20bound%22+AND+abs:%22functional%20equation%22+AND+abs:%22Euler%20product%22+AND+abs:%22zeta%22
abs:%22negative%20squares%22+AND+abs:zeta
abs:Nevanlinna+AND+abs:%22Riemann%20hypothesis%22
abs:Krein+AND+abs:%22Riemann%20hypothesis%22
abs:Landau+AND+abs:%22Riemann%20hypothesis%22+AND+abs:nonnegative
abs:%22mean%20square%22+AND+abs:%22prime%20number%20theorem%22+AND+abs:%22Riemann%20hypothesis%22
abs:Deligne+AND+abs:%22Riemann%20hypothesis%22+AND+abs:%22tensor%20power%22
Q
rm -f "$TMP"
