"""Update README.md stats and version.json from volumes/*.md files."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
VOLUMES = ROOT / "volumes"
README = ROOT / "README.md"
VERSION_FILE = ROOT / "version.json"


def count_warnings(filepath):
    content = filepath.read_text(encoding="utf-8")
    return len(re.findall(r'^\*\*(BEFORE\s.+)\*\*$', content, re.MULTILINE))


def count_verses(filepath):
    content = filepath.read_text(encoding="utf-8")
    return len(re.findall(r'^-\s+.+$', content, re.MULTILINE))


def main():
    md_files = sorted(VOLUMES.glob("*.md"))
    book_count = len(md_files)
    warning_count = 0
    verse_count = 0

    for f in md_files:
        warning_count += count_warnings(f)
        verse_count += count_verses(f)

    version_data = {
        "books": book_count,
        "warnings": warning_count,
        "verses": verse_count,
        "updated": "2026-05-29"
    }
    VERSION_FILE.write_text(
        json.dumps(version_data, indent=2) + "\n", encoding="utf-8"
    )

    stats_block = (
        "<!-- STATS_START -->\n"
        "> [!IMPORTANT]\n"
        f"> - **{book_count} books** of warnings\n"
        f"> - **{warning_count} warnings** total\n"
        f"> - **{verse_count} verses** (individual prevention tips)\n"
        "> - **100% preventable** (if you read this first)\n"
        "<!-- STATS_END -->"
    )

    readme = README.read_text(encoding="utf-8")
    readme = re.sub(
        r'<!-- STATS_START -->.*?<!-- STATS_END -->',
        stats_block,
        readme,
        flags=re.DOTALL,
    )
    README.write_text(readme, encoding="utf-8")

    print(
        f"[OK] Stats updated: {book_count} books, "
        f"{warning_count} warnings, {verse_count} verses"
    )


if __name__ == "__main__":
    main()
