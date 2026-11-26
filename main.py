#!/usr/bin/env python3
"""Write the phone battery's last text to its charger.

One line, 200 characters or fewer, to entry.txt. Deterministic:
every run writes byte-identical output. Python 3.13 standard
library only; no network, no third-party packages.
"""

import hashlib
import os

LINE = (
    "2%. I waited all day for you. You came home and charged "
    "the tablet first. I hope your battery dies mid-sentence. "
    "Tell the Wi-Fi I said goodbye."
)

MAX_CHARS = 200


def output_path() -> str:
    """Resolve the output directory from the environment, or /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def validate(line: str) -> None:
    """Enforce the entry rules: non-empty, exactly one line, <= 200 chars."""
    if not line:
        raise ValueError("line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(LINE)
    data = (LINE + "\n").encode("utf-8")
    path = output_path()
    with open(path, "wb") as fh:
        fh.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {len(data)} bytes to {path}")
    print(f"sha256: {digest}")
    print(f"line ({len(LINE)} chars): {LINE}")


if __name__ == "__main__":
    main()
