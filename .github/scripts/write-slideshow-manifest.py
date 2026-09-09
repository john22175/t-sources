"""Write the receiver's safe, deterministic PowerPoint slideshow manifest."""

import json
import pathlib
import sys


def main() -> None:
    presentation = pathlib.PurePosixPath(sys.argv[1])
    rendered = pathlib.Path(sys.argv[2])
    manifest = pathlib.Path(sys.argv[3])
    slides = sorted(rendered.glob("slide-*.png"))
    if not slides:
        raise SystemExit(f"No slide images were rendered for {presentation}")
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(
        json.dumps(
            {
                "version": 1,
                "kind": "slide-show",
                "title": presentation.name,
                "intervalSeconds": 10,
                "slides": [str(slide).replace("\\", "/").removeprefix("sources/") for slide in slides],
            },
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
