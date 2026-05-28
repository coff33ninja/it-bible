# 📖 The IT Bible

**Warnings From The Department** — 40 books, 267+ warnings covering every flavor of user error known to IT.

A collection of painful-but-true IT support warnings, formatted for reading, searching, and sharing.

## Structure

```
docs/it-bible/
├── 01-general-user-errors/README.md
├── 02-liquid-and-physical-damage/README.md
├── ...
└── 40-the-silent-saboteur/README.md
```

Each book is a subfolder with its own `README.md` so GitHub renders them beautifully.

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
