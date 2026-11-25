"""Write the one-line production-database apology to entry.txt.

Stdlib only. Writes exactly one line (no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt, mode 0644.
"""

import os

ENTRY = "Sorry \u2014 I deleted the production database; on the bright side, the slow queries are gone forever, and so is everything they were querying."


def main():
    if not ENTRY or not ENTRY.strip():
        raise SystemExit("entry is empty")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(path, 0o644)
    except OSError as exc:
        raise SystemExit("failed to write entry.txt: %s" % exc)


if __name__ == "__main__":
    main()
