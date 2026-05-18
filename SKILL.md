---
name: awesome-catalogs
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
7. **Activity tracking** — Record install time + last-used time per item. Track usage across sessions via `activity.json`. Human model can't do this; persistence IS the skill's value-add.
8. **Cleanup assistant** — Detect low-score items (0–1 stars), offer batch cleanup with human review. All catalog views show ★☆☆☆☆ 5-point activity score.

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
7. Update the corresponding catalog file AND write/update entry in `activity.json` with `installed_at` set to now, `last_used_at` null, `times_used` 0
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

## Activity Tracking

Each installed item is tracked in `~/.claude/awesome-catalogs/activity.json`:

```json
{
  "items": {
    "<name>": {
      "type": "skill|tool|script|plugin|software",
      "name": "Display Name",
      "repo": "github.com/owner/repo",
      "domain": "🤖 AI/Automation",
      "installed_at": "ISO timestamp",
      "last_used_at": "ISO timestamp or null",
      "times_used": 0
    }
  },
  "last_cleanup_check": "ISO timestamp or null"
}
```

### Activity Score (5-Point → 10-Block Bar)

Computed at display time from `last_used_at` vs current date:

| Score | Progress Bar | Rule |
|:-----:|--------------|------|
| 5 | `[██████████]` | Used within 7 days |
| 4 | `[████████░░]` | Used within 14 days |
| 3 | `[██████░░░░]` | Used within 30 days |
| 2 | `[████░░░░░░]` | Used within 60 days |
| 1 | `[██░░░░░░░░]` | Used 60+ days ago |
| 0 | `[░░░░░░░░░░]` | Never used since install |

### When to Record Activity

- **Install**: Write `installed_at` immediately after successful install. Set `last_used_at` to null, `times_used` to 0.
- **Use**: When you see a skill invoked via the Skill tool in conversation, update its `last_used_at` and increment `times_used` in `activity.json`. When user explicitly says "我用了 X" or "刚用了 X", do the same.
- **List/Display**: Before displaying any catalog, ALWAYS read `activity.json`, compute star scores, and show them alongside each item. Do NOT display catalog without activity scores.
- **Self-track**: When `awesome-catalogs` itself is invoked, record its own usage.

### Updating Activity on Display

When user says "查看目录" / "show catalog" / "看看我的 skill" etc., read `activity.json` first, compute the star score for each item, then display entries with the score column. Format:

```
| Domain | Name | Repo | Summary | Score | Status |
|------|------|------|------|:--:|:--:|
| 🤖 AI | n8n-io/n8n | github.com/n8n-io/n8n | Workflow automation | [██████████] | 📦 |
| 🎨 Design | something | github.com/x/y | Design tool | [░░░░░░░░░░] | 📦 |
```

Sort 0-score ([░░░░░░░░░░]) items to the bottom so the user sees active items first.

## Cleanup Workflow

When user says "清理" / "cleanup" / "有什么没用的" / "what's unused" / "僵尸 skill" / "zombie skills":

1. Read `activity.json`
2. List all items with score 1 or below (last used >60 days ago, or never used)
3. Sort by score ascending (0 first), then by install date (oldest first)
4. Present as a table:

```
发现 N 个低活跃项目（60天+未使用或从未使用）：

| # | Name | Domain | Score | Installed | Last Used | Type |
|---|------|--------|:-----:|-----------|-----------|------|
| 1 | skill-a | 🎨 Design | [░░░░░░░░░░] | 2026-04-01 | never | skill |
| 2 | tool-b | 🤖 AI   | [██░░░░░░░░] | 2026-04-15 | 2026-04-16 (33d) | tool |
```

5. Ask: "要清理哪些？输入编号（如 1,3,5）、'all'、或 'cancel'"
6. For each item the user selects to remove:
   - Delete from its install directory (`~/.claude/skills/<name>/`, `~/.claude/tools/<name>/`, etc.)
   - Remove its line from the corresponding catalog file under `~/.claude/awesome-catalogs/`
   - Remove its entry from `activity.json`
   - Report: "✅ 已移除 skill-a — 释放 XX KB"
7. Update `last_cleanup_check` timestamp in `activity.json`

### Cleanup Safety Rules

- NEVER auto-delete without user confirmation
- Show exactly what will be deleted (name, path, size) before acting
- User MUST explicitly approve via number list or "all"
- If user says "cancel" / "不用" / "算了", stop immediately with no changes
- Skip items that have been used in the CURRENT conversation (even if their score would otherwise be 0–1)

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
| Domain | Name | Repo | Summary | Activity | Status |
|------|------|------|------|:--:|:--:|
| 🤖 AI | n8n-io/n8n | github.com/n8n-io/n8n | Workflow automation | [██████████] | 📦 |
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
| "清理无用 skill" / "cleanup" / "有什么没用的" / "僵尸" | Run cleanup workflow — scan zombies, offer batch removal |
| "最近用了什么" / "what's active" / "activity" | Show all items sorted by last-used time (most recent first) |
| "I'm making <type> content, load relevant skill" | Find and activate matching skills |

## CLI Commands

| Command | Description |
|------|------|
| `awesome install <url>` | Paste link → classify → install |
| `awesome list <category>` | Browse any category catalog |
| `awesome search "keyword"` | Search across all categories |
| `awesome import-stars <user>` | Batch-import GitHub Stars |
| `awesome cleanup` | Scan for zombie items, offer batch removal |
| `awesome activity` | Show all items sorted by last-used time |
| `awesome remove <name>` | Remove an installed item |
