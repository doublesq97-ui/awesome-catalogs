# Classification Engine

Detailed rules for auto-classifying GitHub repos.

## Detection Priority

Check in this order:

### 1. Skill Detection
- Contains `SKILL.md` at repo root → **Skill**
- Has frontmatter with `name:` and `description:` in SKILL.md → confirms
- Install to `~/.claude/skills/<skill-name>/`

### 2. Plugin Detection
- Is an MCP server (has `mcp.json`, or references MCP in description) → **Plugin**
- Is a Claude Code plugin (has plugin manifest) → **Plugin**
- Install to `~/.claude/plugins/<name>/`

### 3. Script Detection
- Single file repo with `.sh`, `.py`, `.js`, `.rb` extension → **Script**
- No `package.json`, `Cargo.toml`, `go.mod` at root → confirms
- Install to `~/.claude/scripts/<name>/`

### 4. Tool Detection
- Has CLI entry point: `bin/`, `cmd/`, `main.go`, `cli.py`, `src/cli.js`
- Has build system: `package.json` (with `bin` field), `Cargo.toml`, `Makefile`
- NOT a pure library (has executable output) → **Tool**
- Install to `~/.claude/tools/<name>/`

### 5. Software Detection
- Is a full application (has `package.json` with `electron`-like deps, or is a web app)
- Large repo with multiple directories, docs, etc.
- Does NOT fit Skill/Tool/Script/Plugin → **Software**
- Install to `~/claude-projects/<name>/`

## Edge Cases

- **Monorepo**: If repo has multiple packages, classify by primary entry. If ambiguous, ask user.
- **Library with CLI**: Counts as Tool (has CLI).
- **Empty/skeleton repo**: ⏭️ Skip with note "no content".
- **Archived repo**: ⚠️ Warn but still allow install.

## Summary Extraction

From README.md:
1. Read first `<h1>` or `<h2>` heading → use as name if no repo description
2. Read first paragraph after heading (max 120 chars) → use as summary
3. Fallback: use GitHub repo description field
4. If nothing found: "No description available"

## Domain Tag Assignment

Check keywords in README, description, topics:
- `n8n`, `workflow`, `agent`, `automation` → 🤖 AI/Automation
- `cli`, `git`, `devops`, `build`, `docker`, `kubernetes` → 🏗️ Dev Tools
- `ui`, `ux`, `logo`, `banner`, `color`, `design` → 🎨 Design
- `blog`, `seo`, `writing`, `markdown`, `content` → ✍️ Content
- `redbook`, `wechat`, `twitter`, `social`, `xiaohongshu` → 🌐 Social Media
- `scrape`, `crawl`, `analytics`, `visualization`, `data` → 📊 Data
- `obsidian`, `note`, `wiki`, `pkm`, `knowledge` → 📦 Knowledge Mgmt
- `video`, `image`, `subtitle`, `edit`, `ffmpeg` → 🎬 Video/Image
- `tts`, `audio`, `music`, `podcast`, `voice` → 🎵 Audio
- `stable-diffusion`, `dalle`, `image-generation`, `midjourney` → 🖼️ Image Gen
- `prompt`, `prompt-engineering` → 📝 Prompt Eng
- `bazi`, `astrology`, `tarot`, `divination`, `fortune` → 🔮 Esoteric
- None match → 🧩 Other
