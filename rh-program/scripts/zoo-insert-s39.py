#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Session 39 zoo stream `zoo-s39` (2026-10-01): insert into BARRIER-ZOO.md the Group-I entry I.10 (rigidity at conductor 1),
the two I.2 riders (the (alpha, beta) frontier; thresholds and obstructions), the I.9 rider (the one-sided caveat, V2, E0), the
III.20 rider (Theorem P and class C, with the T24 record correction), the V.4 pointer, an in-line dated correction bracket on
I.2's clause (b), five cross-reference rows and a dated count paragraph. Entries 62 -> 63 (I 10, II 5, III 21, IV 22, V 5);
745 -> 765 lines (+20; the bracket adds none).

The nine blocks are read AT RUN TIME from results/zoo-s39/zoo-entries-proposed.md (<!-- BLOCK:name --> ... <!-- END:name -->):
  count     a blank line + the paragraph after the Session-37 count paragraph (line 39), before the blank line and '---' (+2);
  i2b       in-line, inside I.2's STATEMENT (line 80): one space + the bracket after clause (b)'s last words (+0);
  i2alpha   the rider after I.2's STATUS (line 84), I.2's last line (+1);   i2thresh  the rider after i2alpha (+1);
  i9        the rider after I.9's STATUS (line 142), I.9's last line (+1);
  i10       a blank line + heading, blank, five bullets after the i9 rider (+8);
  iii20     the rider after III.20's last line, the Kapranov-Smirnov NOTE (line 387) (+1);
  v4        the pointer after V.4's last line, its Session-24 rider (line 662) (+1);
  xref      five rows after the row "| novel wave s36 N4 `tournament` ..." (line 715) (+5).

Gates, in order, before anything is written:
  1. idempotence: the input carries none of this stream's markers;
  2. full SHA-256 of the input zoo (fa0d7293...), of results/novel-wave-s37/ZOO-LINES-STAGED.md (93e7e394...), of the digest
     results/novel-wave-s37/insights-digest.md (e86f642a...) and of results/novel-wave-s37/beurling-fe/NOTE.md (c3e46d12...);
  3. every block but i2b re-derived from the staged file with only the sanctioned pairs (H1 H2 L1 D1 E1 C1-C5, see the
     proposed file's finding 3), plus any whole subset of the optional pairs O1-O3 (finding 5); <ENTRY-DATE> -> "2026-10-01" or
     the brief's literal "2026-10-01 (Session 39)", the same at all five rider/pointer sites; i2b checked for shape, date and
     its quotation of the digest (whitespace-normalized); L1 checked against the M1a NOTE's lines 340 and 342;
  4. every anchor asserted unique (full-text line heads) and its neighbors verified.
Insertion only. Afterwards: every original line survives, in order (line 80 exactly as before once the bracket is removed);
63 '### ' headings, 10/5/21/22/5; Group I in order I.1-I.10 with I.10 the last entry before '## GROUP II'; each inserted line
once and at its expected line; +20, 745 -> 765; one trailing newline; none of the 10(g) linted phrases.

Usage:
  python3 scripts/zoo-insert-s39.py [--input PATH] [--proposed PATH] [--out PATH | --in-place]
    --input PATH     the zoo to read (default: BARRIER-ZOO.md); it must hash to fa0d7293... .
    --proposed PATH  the blocks file (default: results/zoo-s39/zoo-entries-proposed.md; another path is for testing).
    --out PATH       where to write (default: a scratch file, <system temp dir>/zoo-insert-s39-out.md); never the input or
                     BARRIER-ZOO.md.
    --in-place       write over the input file. The script NEVER writes over its input without this flag.
Modeled on scripts/zoo-insert-s37.py. Prints the result's SHA-256 (the post-insertion hash for STATUS and LOG)."""
import argparse
import hashlib
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "zoo-s39" / "zoo-entries-proposed.md"
STAGED = ROOT / "results" / "novel-wave-s37" / "ZOO-LINES-STAGED.md"
DIGEST = ROOT / "results" / "novel-wave-s37" / "insights-digest.md"
FE_NOTE = ROOT / "results" / "novel-wave-s37" / "beurling-fe" / "NOTE.md"
ZOO_HASH_BEFORE = "fa0d729377df6a53566d19cf80bc0ad9bbdd22648135135467de75d3601f393e"
STAGED_HASH = "93e7e394b2dd4406b57772d6e5a33adf775674f289fe1c6fcfcc117075261f6c"
DIGEST_HASH = "e86f642a47cf4bdedad83efd61cd307b34fa55b87e60501faca2a9b3b0c6c981"
FE_NOTE_HASH = "c3e46d120337c8c30c54a6688a160de9359a3ff36f6aaeb812575bb6650989d4"
LINES_BEFORE, LINES_AFTER, ADDED = 745, 765, 20
LINT = ("clearly", "obviously", "easy to see", "well known", "well-known")
DATE_FILLS = ("2026-10-01", "2026-10-01 (Session 39)")


def die(msg: str) -> None:
    sys.exit("zoo-insert-s39: STOP -- %s Nothing written." % msg)


ap = argparse.ArgumentParser(description="zoo-s39 insertion (I.10, four riders, the V.4 pointer, the I.2(b) bracket, five rows, the count).")
ap.add_argument("--input", default=str(ZOO), help="the zoo to read (default: BARRIER-ZOO.md)")
ap.add_argument("--proposed", default=str(PROPOSED), help="the proposed-blocks file (default: results/zoo-s39/zoo-entries-proposed.md)")
mode = ap.add_mutually_exclusive_group()
mode.add_argument("--out", help="write the result here (default: a scratch file in the system temp directory)")
mode.add_argument("--in-place", action="store_true", help="write the result over the input file")
args = ap.parse_args()
