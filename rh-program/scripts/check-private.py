#!/usr/bin/env python3
"""Fail if text about to be committed shares a run of seven words with private correspondence (BRIEF-WARNINGS W7).

usage: check-private.py [--broad]            compare the staged changes and the unstaged tracked changes
       check-private.py [--broad] FILE ...   compare the named files, whole

Private correspondence = every file under a folder named `correspondence/` anywhere in the
repository (local-only by .gitignore). The third party's words in such a file are the
QUOTED lines, those that begin with ">" — the program keeps a received message that way —
and the comparison is made against those lines only, minus any run of words that the
program itself wrote elsewhere in the same file (the subject line carries the title of a
published paper, which his message repeats and which the record cites everywhere: 20 false
hits on 2026-10-03 before this subtraction). The rest of such a file is the
program's own text (its drafted answer, its notes, titles and citations), which also
appears in tracked files; comparing against it gave 41 false hits in 809 files on
2026-10-03. --broad compares against the whole file anyway, for a manual look.
Runs listed in check-private.allow (beside this script) are public and are not counted:
a run goes there only after a check that it stood in the tracked record before the
private file existed.
Prints positions only, never the shared words. Exit 1 on a hit.
"""
import io, os, re, subprocess, sys

N = 7
WORD = re.compile(r"[A-Za-zÀ-ÿ0-9']+")

def grams(text):
    w = [x.lower() for x in WORD.findall(text)]
    return {" ".join(w[i:i + N]) for i in range(len(w) - N + 1)}

def main():
    root = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
    broad = "--broad" in sys.argv
    private = set()
    nfiles = 0
    for d, _, files in os.walk(root):
        if os.sep + ".git" in d or os.path.basename(d) != "correspondence":
            continue
        for f in files:
            lines = io.open(os.path.join(d, f), encoding="utf-8", errors="replace").read().split("\n")
            quoted = [l for l in lines if l.lstrip().startswith(">")]
            own = [l for l in lines if not l.lstrip().startswith(">")]
            if broad:
                private |= grams(" ".join(l for l in lines if not l.startswith(("**", "#"))))
            else:                                    # his words, minus runs the program itself wrote in the same file
                private |= grams(" ".join(quoted)) - grams(" ".join(own))   # (a paper's title in the subject line is not private)
            nfiles += 1
    allow = os.path.join(os.path.dirname(os.path.abspath(__file__)), "check-private.allow")
    if os.path.exists(allow):                    # runs that are public (a published title his message repeats), each with its reason
        private -= {l.strip() for l in io.open(allow, encoding="utf-8") if l.strip() and not l.startswith("#")}
    targets = [a for a in sys.argv[1:] if a != "--broad"]
    hits = 0
    if targets:
        texts = [(t, io.open(t, encoding="utf-8", errors="replace").read().split("\n")) for t in targets]
    else:
        out = subprocess.run(["git", "diff", "HEAD", "--unified=0", "--no-color"], capture_output=True, text=True, cwd=root).stdout
        texts, name, lines = [], None, []
        for l in out.split("\n"):
            if l.startswith("+++ "):
                if name:
                    texts.append((name, lines))
                name, lines = l[6:], []
            elif l.startswith("+") and not l.startswith("+++"):
                lines.append(l[1:])
        if name:
            texts.append((name, lines))
    for name, lines in texts:
        if "/correspondence/" in "/" + name:
            continue
        for i, l in enumerate(lines, 1):
            if grams(l) & private:
                hits += 1
                print("  HIT  %s  (added or listed line %d): a run of %d words is shared with a private file" % (name, i, N))
    print("private files: %d; texts compared: %d; hits: %d" % (nfiles, len(texts), hits))
    sys.exit(1 if hits else 0)

if __name__ == "__main__":
    main()
