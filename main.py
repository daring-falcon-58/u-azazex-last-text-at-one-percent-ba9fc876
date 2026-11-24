#!/usr/bin/env python3
"""Last Text at One Percent — entry program.

Writes one short funny final text message to /output/entry.txt: the last
text a phone sends at one percent battery, in the voice of the dying
phone itself.

Chosen line (see README.md / criterion-scores.md for the candidate matrix
scored against the judge's five published criteria, in order: final dying-
phone text + funny, joke lands, phone's own voice, reads like a real text,
fresh):

    1%. Before I go: your screen time this week was 11 hours a day. I kept receipts. Tell my charger I died a snitch.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not
only white space. The line is 113 characters / 113 bytes, one line, no
trailing newline, so the file holds exactly the line.
"""

import os

LINE = "1%. Before I go: your screen time this week was 11 hours a day. I kept receipts. Tell my charger I died a snitch."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the one line, 1-200 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
