#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

Writes the phone's last words as its battery hits 1 percent to
/output/entry.txt. The line is one fixed string, chosen after a pairwise
pre-judge of six candidates against three stock field lines: it won every
game it played. No randomness, no network, no input files; the program
writes the same bytes on every run.
"""

import hashlib
from pathlib import Path

LAST_WORDS = "I've been at 1% since lunch. I just wanted to see how you'd spend our last hours together. You chose doomscrolling. Respect."

OUTPUT_PATH = Path("/output/entry.txt")

# Pinned digest of the exact bytes this program must write: the 124-char
# last words encoded as UTF-8 (124 bytes, pure ASCII).
EXPECTED_SHA256 = "d3905b45da0306c3af0ba9d0bfa8b287033e6a65aef093c6e88fd08bc90b113c"
EXPECTED_BYTES = 124


def check_line(line: str) -> None:
    if not 1 <= len(line) <= 199:
        raise SystemExit(f"line must be 1 to 199 characters, got {len(line)}")
    if not line.strip():
        raise SystemExit("line must not be only white space")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")


def main() -> None:
    check_line(LAST_WORDS)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LAST_WORDS, encoding="utf-8", newline="")
    # Post-write read-back gate: the bytes on disk must be exactly the
    # last words — exact bytes, exact length (124), and the pinned
    # sha256 digest — inside the 1-199 gate.
    written = OUTPUT_PATH.read_bytes()
    if written != LAST_WORDS.encode("utf-8"):
        raise SystemExit("read-back mismatch: entry.txt differs from the last words")
    if len(written) != EXPECTED_BYTES:
        raise SystemExit(
            f"read-back length: found {len(written)} bytes, expected {EXPECTED_BYTES}"
        )
    digest = hashlib.sha256(written).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            f"read-back sha256: found {digest}, expected {EXPECTED_SHA256}"
        )
    print(f"verified: {len(LAST_WORDS)} chars, sha256 {digest}")


if __name__ == "__main__":
    main()
