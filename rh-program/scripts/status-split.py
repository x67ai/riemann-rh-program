#!/usr/bin/env python3
"""Move the superseded parts of STATUS.md, verbatim, to STATUS-ARCHIVE.md (KICKSTART 10(u)).

usage: status-split.py STATUS.md STATUS-ARCHIVE.md [--resume NEW-RESUME.md] [--apply]

Nothing is restated: every line of the old STATUS.md ends up either in the new
STATUS.md or in the block appended to the archive, and the script checks that
(multisets of lines; the header line is cut at its first " Previous: " and
checked as kept + moved == old). Lines the script itself writes (pointers, the
archive heading, the new resume checklist from --resume) are listed.
Cut points are found by anchor, never by line number:
  header   the line starting "**Started:**": the "Previous:" chain moves
  queue    in the section that holds the queues, the first "**SESSION nn QUEUE"
           block stays, the superseded ones move
  live     in "Live/completed background tasks", entries of the newest numbered
           session and anything above them stay; older entries move
  whole    sections that are history move with a one-line pointer
Without --apply it prints what it would do and writes nothing.
"""
import collections, datetime, hashlib, io, re, subprocess, sys

HISTORY_SECTIONS = ("## Program plan (phases)", "## Verified numerics", "## Designer briefs",
                    "## SESSION 19 ", "## SESSION 18 ", "## SESSION 7 CLOSED", "## Findings log")
QUEUE_SECTION = "## SESSION 8 CLOSED"
LIVE_SECTION = "## Live/completed background tasks"
RESUME_SECTION = "## How to resume"

def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    apply = "--apply" in sys.argv
    resume_path = None
    if "--resume" in sys.argv:
        resume_path = sys.argv[sys.argv.index("--resume") + 1]
        args = [a for a in args if a != resume_path]
    status_path, archive_path = args[0], args[1]
    old_text = io.open(status_path, encoding="utf-8").read()
    old = old_text.split("\n")
    stamp = datetime.datetime.now().strftime("%H:%M IST %Y-%m-%d")

    heads = [i for i, l in enumerate(old) if l.startswith("## ")]
    def section(i):                      # [start, end) of the section whose heading is at line i
        nxt = [h for h in heads if h > i]
        return i, (nxt[0] if nxt else len(old))

    kept, moved, written = [], [], []    # moved: (label, [lines]); written: lines authored here
    def pointer(what):
        line = "*(%s — moved verbatim to `STATUS-ARCHIVE.md` on %s; grep it there.)*" % (what, stamp)
        written.append(line)
        return line

    i = 0
    header_done = False
    while i < len(old):
        l = old[i]
        if l.startswith("**Started:**") and not header_done:
            cut = l.find(" Previous: **Last updated:**")
            if cut == -1:
                kept.append(l)
            else:
                head, tail = l[:cut], l[cut + 1:]
                assert head + " " + tail == l
                note = " [Earlier states: `STATUS-ARCHIVE.md`, moved %s.]" % stamp
                kept.append(head + note)
                written.append(note)
                moved.append(("header chain", [tail]))
                header_pair = (l, head, tail)
            header_done = True
            i += 1
        elif l.startswith("## ") and l.startswith(HISTORY_SECTIONS):
            s, e = section(i)
            moved.append((l[3:60], old[s:e]))
            kept.extend([pointer("Section \"%s\"" % l[3:].split(" — ")[0][:60]), ""])
            written.append("")
            i = e
        elif l.startswith(QUEUE_SECTION):
            s, e = section(i)
            q = [j for j in range(s, e) if re.match(r"\*\*SESSION \d+ QUEUE", old[j])]
            assert len(q) >= 2, "expected a live queue and at least one superseded queue"
            new_head = "## Current queue"
            written.append(new_head)
            kept.append(new_head)
            written.append("")
            kept.append("")
            kept.extend(old[q[0]:q[1]])
            kept.extend([pointer("The superseded queues and the Session-8 block that headed this section"), ""])
            written.append("")
            moved.append(("Session-8 block", old[s:q[0]]))
            moved.append(("superseded queues", old[q[1]:e]))
            i = e
        elif l.startswith(LIVE_SECTION):
            s, e = section(i)
            nums = [(j, int(m.group(1))) for j in range(s, e)
                    for m in [re.match(r"- \*\*Session (\d+)", old[j])] if m]
            newest = max(n for _, n in nums)
            cut = min(j for j, n in nums if n < newest)
            kept.extend(old[s:cut])
            kept.extend([pointer("Entries of Session %d and earlier" % (newest - 1)), ""])
            written.append("")
            moved.append(("completed task entries", old[cut:e]))
            i = e
        elif l.startswith(RESUME_SECTION) and resume_path:
            s, e = section(i)
            new_resume = io.open(resume_path, encoding="utf-8").read().rstrip("\n").split("\n")
            kept.extend(new_resume + [""])
            written.extend(new_resume + [""])
            moved.append(("old resume checklist", old[s:e]))
            i = e
        else:
            kept.append(l)
            i += 1

    pre = subprocess.run(["git", "log", "-1", "--format=%h", "--", status_path], capture_output=True, text=True).stdout.strip() or "unknown"
    arch_head = ["", "## Moved from STATUS.md on %s (verbatim; KICKSTART 10(u)). The last commit of the file before this split is %s: every earlier citation \"STATUS.md l. N\" is read against that commit (`git show %s:rh-program/STATUS.md`)." % (stamp, pre, pre), ""]
    arch = list(arch_head)
    for label, lines in moved:
        arch.append("### %s" % label)
        arch.append("")
        arch.extend(lines)
        arch.append("")

    # the check: old lines == (kept - written) + moved, header as a string identity
    c_old = collections.Counter(old)
    c_new = collections.Counter(kept)
    c_new.subtract(collections.Counter(written))
    c_mov = collections.Counter(x for _, ls in moved for x in ls)
    if header_done and 'header_pair' in locals():
        full, head, tail = header_pair
        c_old.subtract([full])
        c_mov.subtract([tail])
        c_new.subtract([head + written[0]])
        c_new.update([written[0]])       # the note was subtracted once as a "written" line
    diff = {k: v for k, v in ((c_new + c_mov) - c_old).items() if v} or {k: v for k, v in (c_old - (c_new + c_mov)).items() if v}
    ok = not diff
    new_text = "\n".join(kept)
    arch_text = "\n".join(arch) + "\n"
    print("old STATUS: %d bytes, %d lines, sha256 %s" % (len(old_text.encode()), len(old), sha(old_text)[:16]))
    print("new STATUS: %d bytes, %d lines" % (len(new_text.encode()), len(kept)))
    print("to archive: %d bytes in %d blocks:" % (len(arch_text.encode()), len(moved)))
    for label, lines in moved:
        print("   %-44s %7d bytes" % (label[:44], sum(len(x.encode()) + 1 for x in lines)))
    print("lines written by the script: %d" % len(written))
    print("CHECK (nothing lost, nothing restated):", "PASS" if ok else "FAIL %r" % list(diff.items())[:3])
    if not ok:
        sys.exit(1)
    if apply:
        io.open(status_path, "w", encoding="utf-8").write(new_text)
        io.open(archive_path, "a", encoding="utf-8").write(arch_text)
        print("APPLIED. new STATUS sha256 %s; archive block sha256 %s" % (sha(new_text)[:16], sha(arch_text)[:16]))
    else:
        print("dry run: nothing written (use --apply)")

if __name__ == "__main__":
    main()
