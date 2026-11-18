#!/usr/bin/env python3
"""make.fun entry for news-image-20261117.

The repository holds the finished front-page image as ``entry.png``
(JPEG bytes under a .png name, which the competition rules allow:
the gate tells PNG from JPEG by the file's first bytes).

This program simply copies that image to the output directory --
``/output`` inside the grader, or ``$MAKEFUN_OUTPUT_DIR`` for a
local run. Standard library only, no network, deterministic:
two runs write byte-identical files.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / "entry.png"
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    # Sanity check: the copy must be byte-identical to the shipped image.
    assert target.read_bytes() == source.read_bytes()


if __name__ == "__main__":
    main()
