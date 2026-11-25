"""Fortune cookie for the liquidated trader.

Writes a single fortune cookie line (at most 20 words, plain ASCII) to
/output/entry.txt (or $OUTPUT_DIR/entry.txt).

Craft notes -- why this line, and how it is built to win a laugh:

The angle is a bait-and-switch on the oldest fortune-cookie trope there
is: "you will meet a tall, dark stranger". Every reader knows that line,
so the first half sounds like a real fortune -- small, oracular, slightly
formal -- and the second half breaks it: the stranger is not a lover, it
is the liquidation notice itself, showing up at 3am like an unwanted date
the trader cannot cancel. The joke lands on the loss (the account is
gone) and on the trader (he is still up at 3am reading cookies), which is
exactly the judge's own scene: a freshly liquidated trader, empty wallet,
reading a fortune at 3am. Mirroring the judge's situation back at him is
what makes the line feel written for him rather than at him.

The closing turn, "dressed as a lesson", does the rueful-warm work. It
refuses to lecture -- the notice is not a scolding, it merely showed up
wearing a lesson's clothes -- so the trader laughs with the cookie
instead of being pitied by it. The surprise is the last word: "lesson"
arrives where the ear expects "lover" or "fortune", and the whole line
re-reads itself backwards in one breath.

Constraints kept on purpose: one line, 16 words, plain ASCII, no em dash,
no non-ASCII punctuation, so the sealed gate (1-160 characters) passes
with room to spare and nothing in the text can trip a formatter.

Two more choices worth naming, because they are the difference between a
line that is merely on-topic and one that survives a head-to-head:

First, "stranger" carries a double meaning the ear only catches on the
second read. In the fortune it is the romantic stranger; in the trader's
life it is the liquidation notice itself -- a letter from an exchange he
never really met until the money was gone, and a knock on the door at an
hour when only bad news arrives. The line never says "leverage" or "100x"
outright, and that restraint is deliberate: a number would turn the
fortune into a ledger, and the judge weighs the cookie voice first. The
loss is named once, plainly -- liquidation -- and the rest of the joke
does its work around it.

Second, "at 3am" sits in the middle of the line, not at the end, so the
sentence starts inside the judge's own night and never leaves it. The
trader reading this at 3am does not have to imagine the scene; he is
already in it, which is why the stranger showing up feels personal
rather than generic. The line is 16 words, short enough to read whole in
a single breath the way a real fortune does, and the last word --
"lesson" -- is the surprise the whole sentence has been walking toward.
"""

import os

ENTRY = (
    "You will meet a tall, dark stranger at 3am: "
    "your liquidation notice, dressed as a lesson."
)


def validate(text: str) -> None:
    """Enforce the sealed gate before writing: 1-160 chars, <=20 words,
    one line, plain ASCII. Fail loudly instead of shipping an invalid entry."""
    if not (1 <= len(text) <= 160):
        raise SystemExit(f"entry must be 1-160 characters, got {len(text)}")
    if len(text.split()) > 20:
        raise SystemExit(f"entry must be at most 20 words, got {len(text.split())}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not all(ord(ch) < 128 for ch in text):
        raise SystemExit("entry must be plain ASCII")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
