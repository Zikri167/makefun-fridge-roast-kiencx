#!/usr/bin/env python3
"""Write the winning one-line fridge roast to /output/entry.txt."""
import os

ENTRY = "My smart fridge plays ads on its door for groceries already inside it, like a waiter upselling me my own leftovers."


def find_output_dir():
    for env in ("OUTPUT_DIR", "_OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        value = os.environ.get(env)
        if value:
            return value
    for path in ("/output", "./output", os.getcwd()):
        if os.path.isdir(path):
            return path
    return "/output"


def main():
    out_dir = find_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry mismatch"
    assert written == written.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in written and "\r" not in written, "entry must be exactly one line"
    assert 1 <= len(written) <= 160, f"entry length {len(written)} out of 1-160 range"
    print(f"wrote {len(written)} chars to {path}")


if __name__ == "__main__":
    main()
