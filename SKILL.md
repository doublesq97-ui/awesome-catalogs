---
name: awesome-claude-skills-manager
description: Universal GitHub resource manager — paste a link, auto-classify into Skill/Tool/Script/Plugin/Software, one-click install, maintain searchable catalogs. Also imports GitHub Stars and organizes them by domain tags.
---

# Awesome Claude Skills Manager

When the user gives a GitHub link, wants to manage their local tools/skills, or asks about their GitHub Stars, use this skill.

## Core Capabilities

1. **Auto-classify** — Analyze repo structure, classify into: skill / tool / script / plugin / software
2. **One-click install** — Install to the appropriate directory based on type
3. **Catalog maintenance** — Update the corresponding CATALOG.md after each install
4. **Star import** — Batch-scan GitHub Stars, classify and recommend
5. **Smart summary** — Extract a one-line description from each repo's README
6. **Natural language** — User can operate in plain language: drop a link, ask "what skills do I have?", etc.

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

## Install Workflow

1. User pastes a GitHub link (or says "install from github.com/xxx/yyy")
2. Clone to `/tmp/awesome-import/<repo-name>/`
3. Analyze repo structure → determine category
4. Extract one-line summary from README
5. Assign a broad domain tag (see Domain Tags below)
6. Install to the appropriate directory
7. Update the corresponding catalog file under `~/.claude/awesome-catalogs/`
8. Report: what was installed, where, its summary, and its domain tag
9. Clean up `/tmp/awesome-import/`

## Star Import Workflow

When user says "import my stars", "check my stars", or `awesome import-stars <username>`:

1. Fetch starred repos via `gh api users/<username>/starred --paginate`
2. For each repo: analyze structure → classify → extract summary → assign domain tag
3. Group results by domain tag
4. Mark each as: ✅ Recommended | 📦 Already installed | ⏭️ Skip (with reason)
5. Skipped items are hidden by default — show only the count breakdown
6. User must say "展开跳过" / "show skipped" to see skipped details
7. Offer batch install for recommended items

### Decision Logic

| Condition | Action |
|------|------|
| Has `SKILL.md` | ✅ Recommend (skill pack) |
| Has CLI entry (`bin/`, `main.go`, `cli.py`) | ✅ Recommend (tool/script) |
| Is MCP server / Claude plugin | ✅ Recommend (plugin) |
| Pure library (`src/` only, no CLI) | ⏭️ Skip |
| Docs/tutorial/awesome-list | ⏭️ Skip |
| Abandoned (3+ years no update) | ⚠️ Flag warning |
| Already installed | 📦 Mark as installed |

## Domain Tags

Assign one broad domain tag per item:

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

## Catalog System

Maintain catalogs under `~/.claude/awesome-catalogs/`:

```
~/.claude/awesome-catalogs/
├── CATALOG.md           # Master catalog — all categories overview
├── SKILLS_CATALOG.md    # Skills only
├── TOOLS_CATALOG.md     # Tools only
├── SCRIPTS_CATALOG.md   # Scripts only
├── PLUGINS_CATALOG.md   # Plugins only
└── SOFTWARE_CATALOG.md  # Software only
```

Each catalog entry format:
```
| Domain | Name | Repo | Summary | Status |
|------|------|------|------|------|
| 🤖 AI | n8n-io/n8n | github.com/n8n-io/n8n | Workflow automation | 📦 Installed |
```

When user says "查看目录" / "show catalog" → display CATALOG.md
When user says "查看 skill" / "show skills" → display SKILLS_CATALOG.md

## Natural Language Triggers

| User says (any language) | Action |
|------|------|
| Paste a GitHub link | Auto-classify → install |
| "查看/显示目录" / "show catalog" | Open CATALOG.md |
| "看看我的 skill" / "show skills" | Open SKILLS_CATALOG.md |
| "搜索 <keyword>" / "search <keyword>" | Cross-category search |
| "我还有哪些 star 没装" / "check uninstalled stars" | Star import workflow |
| "展开跳过" / "show skipped" | Reveal skipped items from last star scan |
| "I'm making <type> content, load relevant skill" | Find and activate matching skills |

## CLI Commands

| Command | Description |
|------|------|
| `awesome install <url>` | Paste link → classify → install |
| `awesome list <category>` | Browse any category catalog |
| `awesome search "keyword"` | Search across all categories |
| `awesome import-stars <user>` | Batch-import GitHub Stars |
| `awesome remove <name>` | Remove an installed item |
