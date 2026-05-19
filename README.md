# 🛠️ awesome-catalogs

> Paste a GitHub link — auto-classify, extract a summary, install it, and update your catalog.

![version](https://img.shields.io/badge/version-v1.3.0-green)
![categories](https://img.shields.io/badge/categories-5-blue)
![status](https://img.shields.io/badge/status-minimal%20stable-brightgreen)
![license](https://img.shields.io/badge/license-MIT-blue)

---

## ✨ 这是什么？

`awesome-catalogs` 是一个 GitHub 资源整理器。

你给它一个 GitHub 链接或本地 repo 路径，它会：

- 🔍 判断它属于 `skill`、`tool`、`script`、`plugin` 还是 `software`
- 📝 从 `README.md` 提取一句话摘要
- 📦 安装到对应的本地目录
- 🗂️ 更新 `~/.claude/awesome-catalogs/` 下的 Markdown 目录
- 📊 追踪每个工具的使用频率，5 分制评分
- 🧹 扫描僵尸项目（从未使用 / 长期闲置），一键清理
- 🔎 提供目录查看和搜索能力
- 🌟 批量导入 GitHub Stars，按领域分组推荐

v1.3.0 在 v1.2.0 的「能识别、能安装、能记录、能找回」基础上，加入了 **使用追踪** 和 **僵尸清理**，让工具箱不再只进不出。

## 🚀 快速开始

### 安装

```bash
git clone https://github.com/doublesq97-ui/awesome-catalogs.git
cd awesome-catalogs
pip install .
```

安装后可以运行：

```bash
awesome --help
```

### 第一次试运行

先用 `--dry-run` 看看它会如何判断，不会复制文件，也不会写 catalog：

```bash
awesome install https://github.com/owner/repo --dry-run
```

你会看到类似反馈：

```text
Name:      repo
Category:  tool (Tools)
Domain:    Dev Tools
Summary:   A small CLI helper for developer workflows.
Source:    https://github.com/owner/repo
Target:    ~/.claude/tools/repo
Status:    ready
```

确认没问题后再正式安装：

```bash
awesome install https://github.com/owner/repo
```

## ✅ 已实现能力

### v1.2.0（分类 + 安装 + Stars 导入）

- 🔍 自动分类：基于 repo 文件结构做规则判断
- 📝 摘要提取：从 README 提取第一段有效描述
- 📦 本地安装：复制 repo 到对应目标目录
- 🗂️ catalog 更新：写入总目录和分类目录
- 🔎 基础查询：支持 `list` 和 `search`
- 🚫 重复检测：安装时自动提示 catalog 中已有的相同来源
- 🧪 试运行：支持 `--dry-run`，先看判断结果再安装
- 🌟 Stars 导入：`import-stars` 批量导入 + 按领域分组 + 推荐/跳过分类
- 🧱 基础测试：22 个测试覆盖分类、决策、摘要清洗

### v1.3.0（使用追踪 + 僵尸清理）🆕

- 📊 安装追踪：`awesome install` 自动写入 `activity.json`（安装时间、类型、来源）
- 🔢 使用计数：`awesome record-usage <name>` 记录使用次数和最后使用时间
- ⭐ 5 分制评分：距上次使用 ≤7 天 = █████，>365 天 = █░░░░，从未使用 = ░░░░░
- 🧹 僵尸扫描：`awesome cleanup` 列出所有 score ≤1 的项目
- 🗑️ 批量清理：`awesome cleanup --force` 确认后删除 + 同步更新 catalog + activity.json

### 当前命令状态

| 命令 | 状态 | 说明 |
|---|---|---|
| `awesome --version` | ✅ 已实现 | 显示当前版本号 (v1.3.0) |
| `awesome install <url-or-path>` | ✅ 已实现 | 贴链接或本地路径 → 自动分类 → 安装 → 更新 catalog → 写入 activity.json |
| `awesome install <url-or-path> --dry-run` | ✅ 已实现 | 只预览分类和目标目录，不复制文件 |
| `awesome install <url-or-path> --force` | ✅ 已实现 | 目标已存在时强制覆盖安装 |
| `awesome classify <local-path>` | ✅ 已实现 | 只分析本地 repo，不安装 |
| `awesome list [category]` | ✅ 已实现 | 查看总目录或某个分类目录 |
| `awesome search <keyword>` | ✅ 已实现 | 跨 catalog 搜索关键词 |
| `awesome import-stars <username>` | ✅ 已实现 | 批量导入 GitHub Stars，按领域分组，自动推荐/已安装/跳过分类 |
| `awesome cleanup` | ✅ 已实现 | 扫描僵尸项目（score ≤1），列出清单 |
| `awesome cleanup --force` | ✅ 已实现 | 确认后批量删除 + 同步清理 catalog 和 activity.json |
| `awesome record-usage <name>` | ✅ 已实现 | 手动记录一次使用（通常由 Claude Code 自动调用） |

## 🧭 命令速查

```bash
# 安装
awesome install https://github.com/owner/repo
awesome install https://github.com/owner/repo --dry-run
awesome install https://github.com/owner/repo --force

# 分析
awesome classify /path/to/local/repo

# 浏览
awesome list
awesome list skills
awesome search agent

# Stars
awesome import-stars <username>
awesome import-stars <username> --limit 50
awesome import-stars <username> --show-skipped

# 使用追踪 (v1.3.0)
awesome cleanup
awesome cleanup --force
awesome record-usage <name>
```

| 命令 | 说明 |
|---|---|
| `awesome install <url-or-path>` | 分类、安装并更新 catalog |
| `awesome install <url-or-path> --dry-run` | 只预览判断结果，不写入 |
| `awesome install <url-or-path> --force` | 覆盖已有安装目标 |
| `awesome classify <local-path>` | 只分类本地 repo |
| `awesome list [category]` | 查看总目录或某个分类目录 |
| `awesome import-stars <username>` | 批量导入 GitHub Stars |
| `awesome import-stars <username> --show-skipped` | 查看被跳过的 star 及原因 |
| `awesome import-stars <username> --limit 50` | 限制处理数量 |
| `awesome search <keyword>` | 跨 catalog 搜索关键词 |
| `awesome cleanup` | 扫描僵尸项目（score ≤1），预览清单 |
| `awesome cleanup --force` | 确认后批量删除僵尸项目 |
| `awesome record-usage <name>` | 记录一次使用（+1 次数，更新最后使用时间） |

## 🎬 示例

### 示例 1：安装 + 使用追踪

```bash
awesome install https://github.com/owner/my-skill
awesome record-usage my-skill
```

### 示例 2：清理僵尸项目

```bash
awesome cleanup
```

输出：

```text
Found 32 zombie items (score <= 1):

| Score | Name | Type | Installed | Last Used |
| --- | --- | --- | --- | --- |
| ░░░░░ | claude-code-sub-agents | skill | 2026-05-13 | never |
| ░░░░░ | n8n-code-javascript | skill | 2026-05-13 | never |
| █░░░░ | old-cli-tool | tool | 2026-01-10 | 2026-01-12 |
...

Run `awesome cleanup --force` to delete these items.
```

确认后执行：

```bash
awesome cleanup --force
# Deleted 32 items: claude-code-sub-agents, n8n-code-javascript, ...
```

### 示例 3：查看 catalog

```bash
awesome list tools
awesome search automation
```

```markdown
| Domain | Name | Repo | Summary | Status |
|---|---|---|---|---|
| Dev Tools | useful-cli | github.com/owner/useful-cli | A command-line utility for everyday automation. | installed |
```

## 🧠 分类规则

| 判断信号 | 分类 | 安装目标 |
|---|---|---|
| 根目录有 `SKILL.md` | `skill` | `~/.claude/skills/<name>/` |
| 有 MCP 或 Claude/Codex plugin 配置文件 | `plugin` | `~/.claude/plugins/<name>/` |
| 单文件 `.sh`、`.py`、`.js`、`.rb` 脚本仓库 | `script` | `~/.claude/scripts/<name>/` |
| 有 `bin/`、`cmd/`、`main.go`、`cli.py` 或 package `bin` | `tool` | `~/.claude/tools/<name>/` |
| 其他完整应用或独立项目 | `software` | `~/claude-projects/<name>/` |

> 优先相信结构化信号。README 里普通提到 "plugin" 或 "MCP" 不会直接触发 plugin 分类，避免把说明文档误判成插件。

## 🗂️ Catalog 目录

```text
~/.claude/awesome-catalogs/
├── CATALOG.md           # 总目录
├── SKILLS_CATALOG.md    # Skills
├── TOOLS_CATALOG.md     # Tools
├── SCRIPTS_CATALOG.md   # Scripts
├── PLUGINS_CATALOG.md   # Plugins
├── SOFTWARE_CATALOG.md  # Software
└── activity.json        # 使用追踪数据 (v1.3.0)
```

- 运行 `awesome install` 后，程序自动判断分类并写入对应 Markdown 文件
- 想查看全部资源：`awesome list`
- 想查看某一类：`awesome list skills`
- 想找回某个资源：`awesome search <keyword>`
- 想清理僵尸：`awesome cleanup`

## 📊 使用追踪与评分 (v1.3.0)

`activity.json` 记录每条工具的完整生命周期：

```json
{
  "items": {
    "my-skill": {
      "type": "skill",
      "name": "my-skill",
      "repo": "github.com/owner/my-skill",
      "domain": "🤖 AI/Automation",
      "installed_at": "2026-05-19T16:00:00+08:00",
      "last_used_at": "2026-05-19T18:30:00+08:00",
      "times_used": 3
    }
  }
}
```

5 分制评分：

| 评分 | 条件 |
|------|------|
| █████ (5) | 7 天内使用过 |
| ████░ (4) | 30 天内使用过 |
| ███░░ (3) | 90 天内使用过 |
| ██░░░ (2) | 180 天内使用过 |
| █░░░░ (1) | 365 天内使用过 |
| ░░░░░ (0) | 从未使用或超过一年 |

僵尸清理规则：
- 不自动删除，必须先 `awesome cleanup` 预览
- `awesome cleanup --force` 确认后才执行
- 删除时同步清理本地文件 + catalog + activity.json

## 🧪 测试

```bash
python3 -m unittest discover -s tests
```

## 🧭 后续路线

### 已完成

| Phase | 内容 | 状态 |
|-------|------|------|
| 核心闭环 | 分类、安装、catalog、搜索、Stars 导入 | ✅ v1.2.0 |
| 使用追踪 | activity.json、5 分制评分、僵尸扫描清理 | ✅ v1.3.0 |

### 待规划

| Phase | 内容 | 依赖 |
|-------|------|------|
| 装前评估 | GitHub API 拉取 stars/活跃度/版本 → 7 维评估 → "值得装吗" | Phase 0 |
| 重叠检测 | 新工具 vs 已安装工具功能对比 → 重合度报告 | Phase 1 |
| 反推荐 + 智能推荐 | "你已有 3 个设计类 skill 且均未使用，确定要装第 4 个？" | Phase 2 |
| 定期健康检查 | 30 天未清理提醒 / 90 天僵尸预警 / 死链检测 | Phase 3 |

```
Phase 0: 使用追踪         [██████████] ✅ v1.3.0
Phase 1: 装前评估         [████████░░] 下一期
Phase 2: 重叠检测         [██████░░░░] 依赖 Phase 1
Phase 3: 反推荐+智能推荐  [████░░░░░░] 依赖 Phase 2
Phase 4: 定期健康检查     [██░░░░░░░░] 锦上添花
```

---

如果这个方向也戳中你，欢迎给一个 star ⭐。
