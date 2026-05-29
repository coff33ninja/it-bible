"""
Update README.md stats and version.json from volumes/*.md files.
Runs as a GitHub Action on every push to master.
"""

import json
import re
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
VOLUMES = ROOT / "volumes"
README = ROOT / "README.md"
VERSION_FILE = ROOT / "version.json"

def count_warnings(filepath):
    content = filepath.read_text(encoding="utf-8")
    before_count = len(re.findall(r'^\*\*(BEFORE\s.+)\*\*$', content, re.MULTILINE))
    return before_count

def count_verses(filepath):
    content = filepath.read_text(encoding="utf-8")
    bullets = re.findall(r'^-\s+.+$', content, re.MULTILINE)
    return len(bullets)

def main():
    md_files = sorted(VOLUMES.glob("*.md"))
    book_count = len(md_files)
    warning_count = 0
    verse_count = 0

    for f in md_files:
        warning_count += count_warnings(f)
        verse_count += count_verses(f)

    # Update version.json
    version_data = {
        "books": book_count,
        "warnings": warning_count,
        "verses": verse_count,
        "updated": "2026-05-29"
    }
    VERSION_FILE.write_text(json.dumps(version_data, indent=2) + "\n", encoding="utf-8")

    # Update README.md stats section
    readme = README.read_text(encoding="utf-8")

    readme = re.sub(
        r'\*\*(\d+) books\*\*',
        f'**{book_count} books**',
        readme
    )
    readme = re.sub(
        r'\*\*(\d+) warnings?\*\*',
        f'**{warning_count} warnings**',
        readme
    )
    readme = re.sub(
        r'\*\*(\d+) verses?\*\*',
        f'**{verse_count} verses**',
        readme
    )

    # Update the By The Numbers section
    readme = re.sub(
        r'- \*\*(\d+) books\*\* of warnings',
        f'- **{book_count} books** of warnings',
        readme
    )
    readme = re.sub(
        r'- \*\*(\d+) warnings?\*\* total',
        f'- **{warning_count} warnings** total',
        readme
    )
    readme = re.sub(
        r'- \*\*(\d+) verses?\*\*',
        f'- **{verse_count} verses**',
        readme
    )

    README.write_text(readme, encoding="utf-8")

    print(f"[OK] Stats updated: {book_count} books, {warning_count} warnings, {verse_count} verses")

if __name__ == "__main__":
    main()
