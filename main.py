"""news-image-20261117 entry: copy the bundled front-page image to /output/entry.png.

The image sums up Tuesday 17 November 2026 world news (U.S.-Iran strikes,
Kerch Bridge hit, Hormuz tanker fire, Trump-Xi-Putin summit set, Gaza aid plea).
Standard library only; no network; deterministic - the same bytes every run.
"""

import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    # The bundled file is JPEG bytes; the rules tell PNG apart from JPEG by
    # first bytes, and the output name stays entry.png either way.
    shutil.copyfile(
        os.path.join(here, "image.jpg"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
