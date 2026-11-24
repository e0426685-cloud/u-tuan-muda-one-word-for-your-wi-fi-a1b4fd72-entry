"""One Word for Your Wi-Fi.

Entry word: "Ghosting" -- home Wi-Fi that vanishes mid-call, mid-show,
mid-sentence, exactly when you need it most, then drifts back like
nothing happened. It describes the connection as the entrant lives it:
present one moment, gone the next, no explanation offered.

Why this word wins its pairings: every household knows the moment the
bars disappear for no reason. "Ghosting" names that exact behaviour in
one everyday word -- no setup, no pun to decode, no jargon. The joke
lands because the experience is universal: the network ghosts you.
"""

import os

WORD = "Ghosting"


def validate(word):
    """Check the entry word against the competition gate.

    The gate requires /output/entry.txt to hold UTF-8 text of 1 to 20
    characters, not only whitespace. A single word has no spaces, so
    checking length and non-blankness is enough.
    """
    if not isinstance(word, str):
        raise TypeError("entry word must be a string")
    if not word.strip():
        raise ValueError("entry word must not be blank")
    if len(word) < 1 or len(word) > 20:
        raise ValueError("entry word must be 1 to 20 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word")
    if not word.isalpha():
        raise ValueError("entry word must be letters only")
    return word


def main():
    word = validate(WORD)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(word)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
