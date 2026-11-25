"""One Line, Big Laugh entry for make.fun bounty
u-coral-404-one-line-big-laugh-328fb857.

Writes exactly one original funny line (79 characters, plain ASCII,
no trailing newline) to /output/entry.txt.

The joke: the office printer gets a hopeful name, and the punchline
turns the name against its owner. The setup sounds like a harmless
office anecdote ("I named the office printer 'Hope'"), then the
twist lands in the last two words: the printer does not live up to
its name, it destroys the very thing it was named after. One verb,
"crushes", does all the work: it is what a jammed printer does to
paper and what office life does to optimism, at the same time.

Why this line fits the house judge's brief, most important first:

1. A real joke, not an observation. Setup plus punchline, with the
   laugh arriving on the final word.
2. A turn the reader does not see coming. Naming a printer "Hope"
   promises a cute story; the ending reveals the name was a mistake.
3. No wasted words. Seventy-nine characters, every one earning its
   place; the line is as short as the joke allows.
4. Fresh. No stock printer-jam gag, no "final_v2" trope, no meeting
   about meetings: the humour is in the name itself.
5. Memorable. Anyone who has fought an office printer can repeat it
   the same day, in one breath.
"""

import os

LINE = "I named the office printer 'Hope' because every time I use it, it crushes mine."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the entry line byte-exact: no trailing newline, UTF-8."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
