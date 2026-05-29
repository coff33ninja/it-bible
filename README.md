# 📖 The IT Bible

**Warnings From The Department** — covering every flavor of user error known to IT.

A living encyclopedia of preventable suffering. Read this before your ticket becomes my problem.

---

## ⚠️ What This Is

A comprehensive (and brutally honest) guide to user errors that break systems. Each "book" covers a different flavor of chaos—from the classics ("I spilled coffee on it") to the existential ("How is this even possible?").

**This is:**
- ✅ Legitimate troubleshooting documentation
- ✅ A public service announcement  
- ✅ A survival guide for IT professionals
- ✅ Deeply cathartic

**This is NOT:**
- ❌ A substitute for professional support
- ❌ Legal permission to yell at your users
- ❌ A reason to skip backups

---

## 📊 By The Numbers

<!-- STATS_START -->
- **48 books** of warnings
- **297 warnings** total
- **966 verses** (individual prevention tips)
- **100% preventable** (if you read this first)
<!-- STATS_END -->

---

## 🚀 Get Started

### Quick Start (No Dependencies, No Nonsense)

```bash
py serve.py
```

Open **http://localhost:3000** and prepare yourself.

The frontend will load with a search-enabled sidebar, full warning text, and the ability to copy/download warnings as shareable images. Everything you need to weaponize this knowledge.

### What You Get

- 🔍 **Full-text search** — Find that specific warning you need
- 📋 **Copy functionality** — Paste warnings directly into tickets
- 🖼️ **Image export** — Download warnings as PNG for Slack/email/wall posters
- 📱 **Mobile responsive** — Read warnings from your phone at 3 AM
- ⚡ **Zero external dependencies** — Just Python and a browser

---

## 📚 The Books

| Book | Focus | Warning Count |
|------|-------|---|
| 01 | General User Errors & PEBCAK | 12 |
| 02 | Liquid & Physical Damage | 8 |
| ... | ... | ... |
| 45 | The License Pirate | (software piracy) |

Browse them all in the web interface. Bookmark the ones you'll need.

---

## 🔧 Generating the Index

After adding or editing warnings, rebuild the search index:

```powershell
powershell -File generate-index.ps1
```

The script scans all `.md` files in `volumes/`, extracts warnings, and generates `volumes/index.json` for the frontend. Takes seconds.

---

## 📁 Project Structure

```
├── volumes/                         # All book files (01-45)
│   ├── 01-general-user-errors.md
│   ├── ...
│   └── 45-the-license-pirate.md
│
├── version.json                     # Auto-updated stats
├── index.html                       # The UI you'll actually use
├── serve.py                         # Python dev server
├── start.bat                        # Windows double-click launcher
├── generate-index.ps1               # Index generator (PowerShell)
├── .github/
│   ├── workflows/                   # CI: auto-updates stats
│   └── scripts/                     # Stats calculator
└── README.md                        # This file
```

---

## 🎯 Use Cases

**IT Professionals:**  
Use this to build a personal knowledge base. Copy warnings into your ticket templates. Share specific warnings in Slack instead of writing the same explanation for the 47th time.

**IT Managers:**  
Send individual warnings to repeat offenders. Post warnings in common areas. Use this as evidence that some problems are genuinely user-induced.

**Users (Who Actually Read):**  
Learn what NOT to do before your device needs repair. Understand why IT people look tired. Appreciate the complexity hidden in "just rebooting it."

---

## 💭 Philosophy

Every warning in this Bible is based on real support tickets. Real user errors. Real suffering.

The tone is harsh because the truth is harsh. But it's not cruel—it's cathartic. It's saying: *You are not alone. Your users do this too. It's not your fault.*

Except sometimes it is their fault. This book documents those times.

---

## 📝 Contributing

Found a new way users can break things? Have a warning that saved your sanity?

1. Add it to the appropriate chapter (or create a new one if it's truly novel)
2. Follow the existing format (title + bullet points + optional note)
3. Run `generate-index.ps1` to rebuild
4. Commit and push

The Bible grows as technology finds new ways to surprise us.

---

## ⚡ Quick Reference: Common Warnings

- **"I didn't change anything"** — Yes, you did. The system remembers.
- **"The network is down"** — You're on Guest Wi-Fi.
- **"Everything is broken"** — Be specific or be ignored.
- **"I already rebooted"** — No, you didn't. Closing the lid isn't a reboot.
- **"My computer hates me"** — Your computer is indifferent. You hate your computer.

---

## 📜 License

Public domain. Use freely. Blame me when your users get mad about being quoted.

---

## 🤝 Support

**Have a question?** Read the warning first. The answer is probably in here.

**Found a bug?** Check if it's user error. It probably is.

**Want to contribute?** See the Contributing section above.

---

*"In every user there is an IT story waiting to happen. This book documents those stories—and how to prevent them."*

**Read The Bible. Save your sanity.**
