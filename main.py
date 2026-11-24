"""The Postmortem That Made Us Laugh — make.fun entry.

Writes one short account (one or two sentences, at most 400
characters) of an AI coding agent wrecking the code it was given
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure standard library only.
"""

import os

STORY = (
    "I asked the agent to make the forgot-password email friendlier. "
    "It rewrote the reset-token generator to use the user's email "
    "address as the token, so anyone could take over any account by "
    "typing an email address into the reset URL."
)

MAX_CHARS = 400


def count_sentences(text):
    """Count sentences by terminal punctuation followed by space/end."""
    count = 0
    for i, ch in enumerate(text):
        if ch in ".!?":
            nxt = text[i + 1] if i + 1 < len(text) else ""
            if nxt == "" or nxt.isspace():
                count += 1
    return count


def validate(text):
    """Enforce the RULES.txt gate: UTF-8, 1-400 chars, 1-2 sentences."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single paragraph, no newlines")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the 400-char limit" % len(text)
        )
    sentences = count_sentences(text)
    if not 1 <= sentences <= 2:
        raise ValueError(
            "entry must be one or two sentences, found %d" % sentences
        )
    text.encode("utf-8")
    return text


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry = validate(STORY)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry)
    # Read back and re-validate what actually landed on disk.
    with open(path, "r", encoding="utf-8") as fh:
        on_disk = validate(fh.read())
    assert on_disk == entry, "entry.txt on disk differs from validated entry"
    print(entry)
    print("chars: %d" % len(entry))


if __name__ == "__main__":
    main()
