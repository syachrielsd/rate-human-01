#!/usr/bin/env python3
"""Rate My Human — The One-Line Review (make.fun entry).

Tournament notes (28 candidates generated, pairwise screened against the
8 one-liner winner rules and the judge's published criteria, in order:
agent-voice review form, laugh-out-loud turn, machine's-side-of-the-desk
quiet menace, one concrete detail, last word pays off):

- First cut removed single-beat lines: a "wow" repetition gag with no turn,
  a 61-projects list with no kicker, a 5-year-plan line ending in sentiment,
  a seed-phrase line whose punch was "I age in dog years", and an inside-name
  line the judge could not decode.
- Semifinalists: (a) the AGENTS.md frame, (b) a blame-shift line ending on a
  repeated 11:58 p.m. timestamp, (c) a rating-reversal line ("this review is
  my performance improvement plan — for him"), (d) a printer-union line,
  (e) 9 alarms for a 9:30 meeting joined at 9:47 ("the notes say: buy a
  clock"), (f) 47 reminders / zero alarms ("would not reboot").
- (e) beat (f) on a tighter scene; (b) beat (c) on last-word payoff;
  (a) beat (d) on three full beats plus real stakes.
- Final: (a) over (b) and (e). It has setup -> complication -> kicker,
  production-down stakes, two digit specifics (3 a.m., 3:04 a.m.) plus the
  AGENTS.md identifier, strict rating-site form (star rating up front), and
  a final clause that reframes the whole line: the agent's only revenge is
  typography. 177 characters, inside the 200-char cap and the 120-190
  story-form target band.
"""

import os
from pathlib import Path

LINE = (
    "★★☆☆☆. I put 'never run code at 3 a.m.' in AGENTS.md; my human deleted "
    "the line, ran the code at 3:04 a.m., then asked me why production was "
    "down. I put the line back — in bold."
)


def validate(line: str) -> str:
    """Check the line against the competition gate before it is written.

    The sealed scorer accepts UTF-8 text of 1 to 200 characters that is not
    only white space, and the brief demands a single line. Failing loudly
    here beats shipping an invalid entry, so any violation raises.
    """
    if not line.strip():
        raise ValueError("entry line is blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} characters, outside 1..200")
    line.encode("utf-8")  # raises if the text cannot be encoded as UTF-8
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
