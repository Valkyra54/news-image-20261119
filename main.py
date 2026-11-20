#!/usr/bin/env python3
"""Copy entry.png to the output directory (make.fun news-image entry).

Stdlib only. Validates the image first: it must be a PNG, at most
1 MiB, and at most 1024x1024 pixels. Copies to /output by default,
or to $MAKEFUN_OUTPUT_DIR when set.
"""

import os
import shutil
import struct
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
MAX_BYTES = 1_048_576
MAX_DIM = 1024


def read_png_size(path):
    """Return (width, height) of a PNG file, or None if not a PNG."""
    with open(path, "rb") as f:
        head = f.read(33)
    if len(head) < 24 or head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    if head[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def main():
    if not os.path.isfile(SRC):
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    size = read_png_size(SRC)
    if size is None:
        print("entry.png is not a valid PNG file", file=sys.stderr)
        return 1
    width, height = size
    if width > MAX_DIM or height > MAX_DIM:
        print(
            "entry.png is %dx%d, over the 1024x1024 limit" % (width, height),
            file=sys.stderr,
        )
        return 1
    nbytes = os.path.getsize(SRC)
    if nbytes > MAX_BYTES:
        print(
            "entry.png is %d bytes, over the 1 MiB limit" % nbytes,
            file=sys.stderr,
        )
        return 1
    # Whole-file check: a PNG must end with its IEND chunk.
    with open(SRC, "rb") as f:
        f.seek(-12, os.SEEK_END)
        tail = f.read(12)
    if tail[4:8] != b"IEND":
        print("entry.png is truncated (no IEND chunk)", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))
    print(
        "copied entry.png (%dx%d, %d bytes) to %s"
        % (width, height, nbytes, OUT_DIR)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
