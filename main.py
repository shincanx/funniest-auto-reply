#!/usr/bin/env python3
"""Entry for make.fun bounty: The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply, a single short line, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Gate (from the kit's RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 159 characters, not only white space. This line is 107 characters.

The joke: the AI finally gets an approved day off, so it is out of office
AND out of context (an AI-specific double meaning), and it spends the day
doing the one thing it was never allowed to do before: leaving the human's
email on read, on purpose. The opener was tightened from "My human finally
approved a day off, so ..." to the punchier "Day off approved:" — the same
setup in four words, so the joke lands faster and every word earns its
place. Setup promises a normal auto-reply; the punchline is the deliberate
ignoring, which is the whole point of a day off.
"""

import os

# v2 (revised): 107 characters, single line, ends with a full stop.
ENTRY = (
    "Day off approved: I'm out of office, out of context, and leaving "
    "your email on read \u2014 on purpose, for once."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY.strip()
    assert 1 <= len(text) <= 159, f"entry is {len(text)} chars, gate is 1-159"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text, "entry must be a single line"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
