#!/usr/bin/env python3
"""Time stamps from the machine clock, never typed (KICKSTART 10(w)).

usage: stamp.py                      print the stamp, e.g. "01:55 IST 2026-10-03"
       stamp.py --fill FILE          replace every @@NOW@@ in FILE by the stamp
       stamp.py --append FILE TEXT   append TEXT to FILE, @@NOW@@ replaced by the stamp
       stamp.py --check REV          every stamp in lines added by the commits REV..HEAD
                                     must not be later than its commit; exit 1 if one is

A brief, a charter header or a LOG line is written with the placeholder @@NOW@@
where the time goes, and this script fills it. --check is the close-out test: a
stamp that is later than the commit which introduced it was not read from the clock.
Stamps a line QUOTES from elsewhere (an older entry, another file) are not at
fault: the check only fails on stamps of the commit's own day that run ahead of it.
"""
import datetime, io, re, subprocess, sys

STAMP = re.compile(r"\b([01]\d|2[0-3]):([0-5]\d) IST (\d{4})-(\d{2})-(\d{2})\b")
SLACK_MIN = 1

def now():
    return datetime.datetime.now().strftime("%H:%M IST %Y-%m-%d")

def fill(path):
    s = io.open(path, encoding="utf-8").read()
    n = s.count("@@NOW@@")
    if n:
        io.open(path, "w", encoding="utf-8").write(s.replace("@@NOW@@", now()))
    print("%s: %d placeholder(s) filled with %s" % (path, n, now()))

def append(path, text):
    io.open(path, "a", encoding="utf-8").write(text.replace("@@NOW@@", now()) + "\n")
    print("%s: appended at %s" % (path, now()))

def check(rev):
    out = subprocess.run(["git", "log", "--reverse", "-p", "--unified=0", "--format=@@COMMIT@@ %h %ct",
                          "%s..HEAD" % rev], capture_output=True, text=True, check=True).stdout
    bad, seen, commit, ctime = [], 0, None, None
    for line in out.split("\n"):
        if line.startswith("@@COMMIT@@ "):
            _, commit, ct = line.split()
            ctime = datetime.datetime.fromtimestamp(int(ct))
        elif line.startswith("+") and not line.startswith("+++") and ctime:
            for m in STAMP.finditer(line):
                hh, mm, y, mo, d = (int(x) for x in m.groups())
                t = datetime.datetime(y, mo, d, hh, mm)
                if t.date() != ctime.date():
                    continue                      # a quoted stamp of another day
                seen += 1
                if t > ctime + datetime.timedelta(minutes=SLACK_MIN):
                    bad.append((commit, m.group(0), ctime.strftime("%H:%M"), line[1:90]))
    print("stamps of the commit's own day in added lines: %d; ahead of their commit: %d" % (seen, len(bad)))
    for c, s, ct, ctx in bad:
        print("  AHEAD  commit %s at %s carries \"%s\"  | %s" % (c, ct, s, ctx))
    return 1 if bad else 0

def main():
    a = sys.argv[1:]
    if not a:
        print(now())
    elif a[0] == "--fill" and len(a) == 2:
        fill(a[1])
    elif a[0] == "--append" and len(a) == 3:
        append(a[1], a[2])
    elif a[0] == "--check" and len(a) == 2:
        sys.exit(check(a[1]))
    else:
        sys.exit(__doc__)

if __name__ == "__main__":
    main()
