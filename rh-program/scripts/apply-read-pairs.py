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
    def collect(idx, first):
        """text of a pair side; a side opened with a double quote runs to the line that closes it."""
        text = first.strip()
        if text.startswith('"') and not (len(text) > 1 and text.endswith('"')):
            j = idx + 1
            while j < len(lines):
                text += "\n" + lines[j]
                if lines[j].rstrip().endswith('"'):
                    break
                j += 1
            idx = j
        text = text.strip()
        for q in ('`', '"'):
            if len(text) > 1 and text[0] == q and text[-1] == q:
                text = text[1:-1]
                break
        return text, idx
    while i < len(lines):
        m = old_re.match(lines[i])
        if m:
            o, j = collect(i, m.group(2))
            j += 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            n = new_re.match(lines[j]) if j < len(lines) else None
            if n:
                w, j2 = collect(j, n.group(2))
                pairs.append((o, w, i + 1))
                i = j2
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
