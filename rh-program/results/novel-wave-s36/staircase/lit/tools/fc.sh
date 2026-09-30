#!/bin/bash
# Firecrawl scrape helper. Usage: fc.sh URL OUTFILE.md
# The API key is read at run time from ~/Downloads/assets/firecrawl.md and never written anywhere.
# Sequential use only (the caller runs at most one at a time; the limit is 2 in flight).
URL="$1"; OUT="$2"
KEY=$(grep -oE 'fc-[A-Za-z0-9]+' "$HOME/Downloads/assets/firecrawl.md" | head -1)
TMP="$OUT.json.tmp"
for i in $(seq 1 10); do
  curl -sS --max-time 180 -X POST "https://api.firecrawl.dev/v1/scrape" \
    -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
    -d "{\"url\": \"$URL\", \"formats\": [\"markdown\"]}" -o "$TMP" && \
  python3 -c "import json,sys; d=json.load(open(sys.argv[1])); assert d.get('success'), d; open(sys.argv[2],'w').write(d['data'].get('markdown') or '')" "$TMP" "$OUT" && { rm -f "$TMP"; echo "OK $(wc -c < "$OUT") bytes -> $OUT"; exit 0; }
  echo "attempt $i failed: $(head -c 300 "$TMP" 2>/dev/null)"; sleep 60
done
rm -f "$TMP"; echo "FAILED $URL"; exit 1
