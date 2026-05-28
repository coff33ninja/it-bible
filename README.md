# 📖 The IT Bible

**Warnings From The Department** — 40 books, 260+ warnings covering every flavor of user error known to IT.

## Structure

```
├── 01-general-user-errors.md
├── 02-liquid-and-physical-damage.md
├── ...
├── 40-the-silent-saboteur.md
├── index.html          (frontend)
├── index.json          (search index)
├── serve.py            (dev server)
├── start.bat           (double-click launcher)
├── generate-index.ps1  (rebuild index.json)
└── README.txt          (server options)
```

## Quick Start

```
py serve.py
```
Open http://localhost:3000. No dependencies, no build step.

## Generating the Index

After adding or editing warnings:
```
powershell -File generate-index.ps1
```
