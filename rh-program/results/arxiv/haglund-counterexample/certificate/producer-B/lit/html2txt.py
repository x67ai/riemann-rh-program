"""Convert a saved DLMF page to plain text: every <math alttext="..."> becomes its LaTeX alttext."""
import re, sys, html
for fn in sys.argv[1:]:
    s = open(fn, encoding='utf-8', errors='replace').read()
    s = re.sub(r'<math[^>]*?alttext="([^"]*)"[^>]*>.*?</math>', lambda m: ' $' + html.unescape(m.group(1)) + '$ ', s, flags=re.S)
    s = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', s, flags=re.S)
    s = re.sub(r'<br\s*/?>|</p>|</div>|</tr>|</h\d>', '\n', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    open(fn.replace('.html', '.txt'), 'w').write(s)
