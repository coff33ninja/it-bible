# 📖 The IT Bible

**Warnings From The Department** — 40 books, 267+ warnings covering every flavor of user error known to IT.

A collection of painful-but-true IT support warnings, formatted for reading, searching, and sharing.

## Structure

```
docs/it-bible/
├── 01-general-user-errors.md
├── 02-liquid-and-physical-damage.md
├── ...
├── 40-the-silent-saboteur.md
├── index.html          (frontend)
├── index.json          (search index)
├── serve.py            (dev server)
├── start.bat           (double-click launcher)
└── generate-index.ps1  (rebuild index.json)
```

## Quick Start

1. Open `docs/it-bible/`
2. Double-click `start.bat` or run `py serve.py`
3. Open http://localhost:3000

No build step, no dependencies — just a browser and Python.

## Generating the Index

After adding or editing warnings, regenerate the search index:
```
cd docs/it-bible
powershell -File generate-index.ps1
```
