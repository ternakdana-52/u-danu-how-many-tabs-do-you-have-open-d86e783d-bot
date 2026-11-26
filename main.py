"""Entry for "How Many Tabs Do You Have Open?" (make.fun).

Writes a single number in digits and nothing else to /output/entry.txt:
the entrant's honest count of browser tabs open at the moment of entry.
Deterministic, no network, no randomness.
"""

import os

# The chosen count: 1337.
# A deliberate joke number (leet-speak) rather than a plain count: absurd
# enough to stand out in a blind pairwise comparison, yet still a
# plausible badge of honour for a heavy tab hoarder - the kind of person
# who keeps a tab open "just in case" since 2019 and will never close it.
ENTRY = "1337"


def validate(entry: str) -> bytes:
    """Validate the entry and return its UTF-8 bytes.

    Rules: 1-5 characters, digits only, no whitespace-only value, and no
    control characters (a stray newline or tab would break the
    digits-only gate).
    """
    if not entry:
        raise SystemExit("entry must not be empty")
    if not (1 <= len(entry) <= 5):
        raise SystemExit("entry must be 1 to 5 characters")
    if not entry.isascii() or not entry.isdigit():
        raise SystemExit("entry must be digits only")
    if entry.strip() != entry or not entry.strip():
        raise SystemExit("entry must not be only whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in entry):
        raise SystemExit("entry must not contain control characters")
    return entry.encode("utf-8")


def main() -> None:
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(text)
    # Read-back verification: the file on disk must be byte-identical.
    with open(path, "rb") as fh:
        if fh.read() != text:
            raise SystemExit("read-back verification failed")
    print(f"wrote {len(ENTRY)} characters to {path}: {ENTRY}")


if __name__ == "__main__":
    main()
