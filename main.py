"""Write the competition entry line to /output/entry.txt.

The gate accepts UTF-8 text of 1 to 240 characters, not only whitespace,
so the line is written exactly as-is, with no trailing newline.
"""

import os

LINE = "My grandmother kept every letter my grandfather wrote; I finally understand why, because I'd keep a grocery list if your handwriting was on it."

# The gate requires 1-240 characters of non-whitespace text.
assert 1 <= len(LINE.strip()) <= 240, "entry line must be 1-240 characters"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
