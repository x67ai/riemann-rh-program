#!/usr/bin/env python3
"""Apply the OLD/NEW pairs of a read file to a NOTE (Session 41).

usage: apply-read-pairs.py READ.md NOTE.md [--skip N,N,...] [--dry]

A pair is a line starting with "OLD" followed (after optional blank lines) by a
line starting with "NEW". The label in parentheses after OLD ("(l. 27-28)",
"(l. 409, fragment)") is dropped. OLD text is matched in the NOTE with every
run of whitespace allowed to be any whitespace (the NOTE wraps lines; readers
quote across the wrap). A pair is applied only if OLD matches exactly once.
Pairs are numbered from 1 in file order; --skip leaves the listed ones out.
The NOTE is rewritten in place unless --dry; the caller keeps the pre-reader copy.
"""
import io, re, sys

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry" in sys.argv
    skip = set()
    for a in sys.argv[1:]:
        if a.startswith("--skip"):
            val = a.split("=", 1)[1] if "=" in a else sys.argv[sys.argv.index(a) + 1]
            skip = {int(x) for x in val.split(",") if x.strip()}
    args = [a for a in args if not re.fullmatch(r"[0-9,]+", a)]
    read_path, note_path = args[0], args[1]
    lines = io.open(read_path, encoding="utf-8").read().split("\n")
    note = io.open(note_path, encoding="utf-8").read()
    pairs, i = [], 0
    old_re = re.compile(r"^\s*(?:[-*]\s*)?\**OLD\**\s*(\([^)]*\))?\s*\**:\**\s?(.*)$")
    new_re = re.compile(r"^\s*(?:[-*]\s*)?\**NEW\**\s*(\([^)]*\))?\s*\**:\**\s?(.*)$")
    while i < len(lines):
        m = old_re.match(lines[i])
        if m:
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            n = new_re.match(lines[j]) if j < len(lines) else None
            if n:
                o, w = m.group(2).strip(), n.group(2).strip()
                # some readers wrap the quoted text in one pair of backticks
                if len(o) > 1 and o[0] == "`" and o[-1] == "`" and len(w) > 1 and w[0] == "`" and w[-1] == "`":
                    o, w = o[1:-1], w[1:-1]
                pairs.append((o, w, i + 1))
                i = j
        i += 1
    applied = missed = ambiguous = skipped = 0
    for k, (old, new, ln) in enumerate(pairs, 1):
        if k in skip:
            skipped += 1
            print("pair %d (read l. %d): SKIPPED by request" % (k, ln))
            continue
        pat = r"\s+".join(re.escape(tok) for tok in old.split())
        hits = list(re.finditer(pat, note))
        if len(hits) == 1:
            h = hits[0]
            note = note[: h.start()] + new + note[h.end():]
            applied += 1
        elif not hits:
            missed += 1
            print("pair %d (read l. %d): OLD NOT FOUND: %s" % (k, ln, old[:90]))
        else:
            ambiguous += 1
            print("pair %d (read l. %d): OLD matches %d times: %s" % (k, ln, len(hits), old[:90]))
    print("pairs %d: applied %d, not found %d, ambiguous %d, skipped %d" % (len(pairs), applied, missed, ambiguous, skipped))
    if not dry:
        io.open(note_path, "w", encoding="utf-8").write(note)

if __name__ == "__main__":
    main()
