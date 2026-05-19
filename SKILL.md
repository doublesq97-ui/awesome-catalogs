---
name: awesome-catalogs
description: Universal GitHub resource manager — paste a link, auto-classify into Skill/Tool/Script/Plugin/Software, one-click install, maintain searchable catalogs. Also imports GitHub Stars and organizes them by domain tags.
---

# awesome-catalogs

When the user gives a GitHub link, wants to manage their local tools/skills, or asks about their GitHub Stars, use this skill.

## How to Use

This project is a **Python CLI** installed at `awesome`. All operations go through it.

```bash
awesome install <url>          # classify → install → update catalog
awesome install <url> --dry-run  # preview only
awesome classify <path>        # analyze local repo
awesome list [category]        # browse catalog
awesome search <keyword>       # search across catalogs
awesome import-stars <user>    # batch import GitHub Stars
awesome cleanup                # scan zombie items (0-1 score), confirm then delete
```

## Core Capabilities

1. **Auto-classify** — Analyze repo structure, classify into: skill / tool / script / plugin / software
2. **One-click install** — Install to the appropriate directory based on type
3. **Catalog maintenance** — Update the corresponding CATALOG.md after each install
4. **Star import** — Batch-scan GitHub Stars, classify and recommend
5. **Smart summary** — Extract a one-line description from each repo's README
6. **Activity tracking** — Track install time, usage count, 5-point scoring, zombie detection
7. **Natural language** — User can operate in plain language: drop a link, ask "what skills do I have?", etc.

## Classification Engine

See [references/classifier.md](references/classifier.md) for detailed detection rules.

### Five Categories & Install Targets

| Category | Directory | Detection |
|------|------|------|
| 🧩 Skill | `~/.claude/skills/` | Contains `SKILL.md`, designed for Claude |
| 🔧 Tool | `~/.claude/tools/` | Has CLI entry: `bin/`, `main.go`, `cli.py` |
| 📜 Script | `~/.claude/scripts/` | Single-file, `.sh`/`.py`/`.js` |
| 🔌 Plugin | `~/.claude/plugins/` | Claude Code plugin format, MCP server |
| 📦 Software | `~/claude-projects/` | Full application or standalone project |

## Catalog System

Maintain catalogs under `~/.claude/awesome-catalogs/`:

```
~/.claude/awesome-catalogs/
├── CATALOG.md           # Master catalog — all categories overview
├── SKILLS_CATALOG.md    # Skills only
├── TOOLS_CATALOG.md     # Tools only
├── SCRIPTS_CATALOG.md   # Scripts only
├── PLUGINS_CATALOG.md   # Plugins only
├── SOFTWARE_CATALOG.md  # Software only
└── activity.json        # Usage tracking data
```

## Activity Tracking (Phase 0)

Tracked in `~/.claude/awesome-catalogs/activity.json`:

- `installed_at` — when installed
- `times_used` — usage count (incremented by Claude Code when skill is invoked)
- `last_used_at` — last usage timestamp
- 5-point score: █████ (<7d) → ░░░░░ (never used)

Use `awesome cleanup` to scan for zombie items (score 0-1), confirm, then batch delete + update catalog.

## Domain Tags

| Tag | Covers |
|------|------|
| 🤖 AI/Automation | n8n, AI agents, workflow automation |
| 🏗️ Dev Tools | CLI, git, devops, build tools |
| 🎨 Design | UI/UX, logo, banner, color systems |
| ✍️ Content | Copywriting, blogging, SEO, writing |
| 🌐 Social Media | Redbook, WeChat, Twitter tools |
| 📊 Data | Scraping, analytics, visualization |
| 📦 Knowledge Mgmt | Obsidian, notes, wiki, PKM |
| 🎬 Video/Image | Editing, generation, subtitles |
| 🎵 Audio | TTS, music, podcast |
| 🖼️ Image Gen | Stable Diffusion, DALL-E |
| 📝 Prompt Eng | Prompt templates, prompt engineering |
| 🔮 Esoteric | Bazi, astrology, divination |
| 🧩 Other | Uncategorized |

## Natural Language Triggers

| User says (any language) | Action |
|------|------|
| Paste a GitHub link | `awesome install <url>` |
| "查看/显示目录" / "show catalog" | `awesome list` |
| "看看我的 skill" / "show skills" | `awesome list skills` |
| "搜索 <keyword>" / "search <keyword>" | `awesome search <keyword>` |
| "我还有哪些 star 没装" | `awesome import-stars <user>` |
| "清理僵尸 skill" / "cleanup" | `awesome cleanup` |
