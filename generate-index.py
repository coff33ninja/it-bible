"""Generate volumes/index.json from markdown files in volumes/."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VOLUMES = ROOT / "volumes"
OUTPUT = VOLUMES / "index.json"

WARNING_START_DOTS = re.compile(r'^\*\*(BEFORE\s.+)\*\*\.\.\.$')
WARNING_START = re.compile(r'^\*\*(BEFORE\s.+)\*\*$')
BULLET = re.compile(r'^-\s+(.+)$')
NOTE = re.compile(r'^\*Note:\s+(.+)\*$')
CHAPTER_TITLE = re.compile(r'^##\s+(.+)$')

result = []

for md_file in sorted(VOLUMES.glob("*.md")):
    if not re.match(r'^\d{2}', md_file.stem):
        continue

    content = md_file.read_text(encoding="utf-8")
    lines = content.split("\n")

    title = ""
    warnings = []
    current_title = ""
    current_bullets = []
    in_warning = False

    for line in lines:
        trimmed = line.strip()

        m = CHAPTER_TITLE.match(trimmed)
        if m:
            title = m.group(1)

        m = WARNING_START_DOTS.match(trimmed) or WARNING_START.match(trimmed)
        if m:
            if in_warning and current_title:
                warnings.append({
                    "title": current_title,
                    "bullets": current_bullets,
                })
            current_title = m.group(1)
            current_bullets = []
            in_warning = True
            continue

        m = BULLET.match(trimmed)
        if m and in_warning:
            current_bullets.append(m.group(1))
            continue

        m = NOTE.match(trimmed)
        if m and in_warning:
            current_bullets.append(f"Note: {m.group(1)}")
            continue

    if in_warning and current_title:
        warnings.append({
            "title": current_title,
            "bullets": current_bullets,
        })

    chapter_num = int(re.sub(r'^(\d+).*', r'\1', md_file.stem))

    total_bullets = sum(len(w["bullets"]) for w in warnings)

    result.append({
        "id": md_file.stem,
        "number": chapter_num,
        "file": md_file.name,
        "title": title,
        "description": title,
        "warningCount": len(warnings),
        "totalBullets": total_bullets,
        "warnings": warnings,
    })

OUTPUT.write_text(
    json.dumps(result, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)

total_warnings = sum(ch["warningCount"] for ch in result)
print(f"Generated index.json with {len(result)} chapters, {total_warnings} warnings")
