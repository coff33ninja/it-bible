"""Update README.md stats and version.json from volumes/*.md files."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
VOLUMES = ROOT / "volumes"
README = ROOT / "README.md"
VERSION_FILE = ROOT / "version.json"

WARNING_PATTERN = re.compile(r'^\*\*(BEFORE\s.+)\*\*$', re.MULTILINE)
VERSE_PATTERN = re.compile(r'^-\s+.+$', re.MULTILINE)
TITLE_PATTERN = re.compile(r'^##\s+(.+)$', re.MULTILINE)
FILE_SORT = re.compile(r'^(\d+)')


def count_warnings(content):
    return len(WARNING_PATTERN.findall(content))


def count_verses(content):
    return len(VERSE_PATTERN.findall(content))


def extract_title(content):
    m = TITLE_PATTERN.search(content)
    return m.group(1) if m else "Untitled"


def main():
    md_files = sorted(VOLUMES.glob("*.md"))
    book_count = len(md_files)
    warning_count = 0
    verse_count = 0

    books = []
    for f in md_files:
        content = f.read_text(encoding="utf-8")
        wc = count_warnings(content)
        vc = count_verses(content)
        warning_count += wc
        verse_count += vc

        num_match = FILE_SORT.match(f.stem)
        num = int(num_match.group(1)) if num_match else 0
        title = extract_title(content)

        books.append({
            "num": num,
            "title": title,
            "file": f.name,
            "warnings": wc,
        })

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

    rows = []
    for b in books:
        link = f"[{b['title']}](volumes/{b['file']})"
        rows.append(f"| {b['num']:02d} | {link} | {b['warnings']} |")
    table = "\n".join(rows)

    books_block = (
        "<!-- BOOKS_START -->\n"
        "<details>\n"
        "<summary><strong>📚 Click to expand book list</strong></summary>\n"
        "\n"
        "| # | Book | Warnings |\n"
        "|---|------|---|\n"
        f"{table}\n"
        "\n"
        "</details>\n"
        "<!-- BOOKS_END -->"
    )

    readme = README.read_text(encoding="utf-8")
    readme = re.sub(
        r'<!-- STATS_START -->.*?<!-- STATS_END -->',
        stats_block,
        readme,
        flags=re.DOTALL,
    )
    readme = re.sub(
        r'<!-- BOOKS_START -->.*?<!-- BOOKS_END -->',
        books_block,
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
