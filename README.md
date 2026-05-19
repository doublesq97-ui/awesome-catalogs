# 🛠️ awesome-catalogs

> Paste a GitHub link — auto-classify, extract a summary, install it, and update your catalog.

![version](https://img.shields.io/badge/version-v1.3.0-green)
![categories](https://img.shields.io/badge/categories-5-blue)
![status](https://img.shields.io/badge/status-minimal%20stable-brightgreen)
![license](https://img.shields.io/badge/license-MIT-blue)

---

## ✨ 这是什么？

`awesome-catalogs` 1.1 是一个 GitHub 资源整理器。

你给它一个 GitHub 链接或本地 repo 路径，它会：

- 🔍 判断它属于 `skill`、`tool`、`script`、`plugin` 还是 `software`
- 📝 从 `README.md` 提取一句话摘要
- 📦 安装到对应的本地目录
- 🗂️ 更新 `~/.claude/awesome-catalogs/` 下的 Markdown 目录
- 🔎 提供基础的目录查看和搜索能力

1.1 的目标不是一次性做完所有宏大愿景，而是先把最核心的闭环做稳：**能识别、能安装、能记录、能找回。**

## 🚀 快速开始

### 安装

```bash
git clone https://github.com/doublesq97-ui/awesome-catalogs.git
cd awesome-catalogs/catelogs-v1.1
./scripts/install.sh
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

## ✅ v1.1 已实现能力

- 🔍 自动分类：基于 repo 文件结构做规则判断
- 📝 摘要提取：从 README 提取第一段有效描述
- 📦 本地安装：复制 repo 到对应目标目录
- 🗂️ catalog 更新：写入总目录和分类目录
- 🔎 基础查询：支持 `list` 和 `search`
- 🚫 重复检测：安装时自动提示 catalog 中已有的相同来源
- 🧪 试运行：支持 `--dry-run`，先看判断结果再安装
- 🧱 基础测试：覆盖 skill、plugin、script、tool、software、中文目录名和摘要清洗

### 当前命令状态

| 命令 | 状态 | 说明 |
|---|---|---|
| `awesome --version` | ✅ 已实现 | 显示当前版本号 |
| `awesome install <url-or-path>` | ✅ 已实现 | 贴链接或本地路径 → 自动分类 → 安装 → 更新 catalog |
| `awesome install <url-or-path> --dry-run` | ✅ 已实现 | 只预览分类和目标目录，不复制文件 |
| `awesome install <url-or-path> --force` | ✅ 已实现 | 目标已存在时强制覆盖安装 |
| `awesome classify <local-path>` | ✅ 已实现 | 只分析本地 repo，不安装 |
| `awesome list [category]` | ✅ 已实现 | 查看总目录或某个分类目录 |
| `awesome search <keyword>` | ✅ 已实现 | 跨 catalog 搜索关键词 |
| `awesome import-stars <username>` | ✅ 已实现 | 批量导入 GitHub Stars，按领域分组，自动推荐/已安装/跳过分类 |
| `awesome remove <name>` | 🗓️ 规划中 | 移除已安装项目，并同步更新 catalog |
| `awesome cleanup` | ✅ 已实现 | 扫描僵尸项目（score 0-1），确认后批量删除 |
| `awesome record-usage <name>` | ✅ 已实现 | 记录 skill/tool 使用次数与最后使用时间 |

## 🧭 命令

```bash
awesome install https://github.com/owner/repo
awesome install https://github.com/owner/repo --dry-run
awesome install https://github.com/owner/repo --force
awesome classify /path/to/local/repo
awesome list skills
awesome search agent
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
| `awesome cleanup` | 扫描并清理僵尸项目 |
| `awesome cleanup --force` | 确认后直接删除僵尸项目 |
| `awesome record-usage <name>` | 记录一次使用 |

## 🎬 示例：操作与反馈

### 示例 1：分类一个本地 skill

```bash
awesome classify ~/claude-projects/my-skill
```

可能输出：

```text
Name:      my-skill
Category:  skill (Skills)
Domain:    AI/Automation
Summary:   Helps Claude run a repeatable research workflow.
Source:    ~/claude-projects/my-skill
Target:    ~/.claude/skills/my-skill
Status:    ready
```

### 示例 2：安装一个 GitHub repo

```bash
awesome install github.com/owner/useful-cli
```

可能输出：

```text
Name:      useful-cli
Category:  tool (Tools)
Domain:    Dev Tools
Summary:   A command-line utility for everyday automation.
Source:    github.com/owner/useful-cli
Target:    ~/.claude/tools/useful-cli
Status:    already installed
```

安装后，catalog 会出现一条记录：

```markdown
| Domain | Name | Repo | Summary | Status |
|---|---|---|---|---|
| Dev Tools | useful-cli | github.com/owner/useful-cli | A command-line utility for everyday automation. | installed |
```

### 示例 3：查看和搜索 catalog

```bash
awesome list tools
awesome search automation
```

可能输出：

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

> v1.1 优先相信结构化信号。README 里普通提到 “plugin” 或 “MCP” 不会直接触发 plugin 分类，避免把分类说明文档误判成插件。

## 🗂️ Catalog 目录

v1.1 会维护这些 Markdown 目录：

```text
~/.claude/awesome-catalogs/
├── CATALOG.md
├── SKILLS_CATALOG.md
├── TOOLS_CATALOG.md
├── SCRIPTS_CATALOG.md
├── PLUGINS_CATALOG.md
└── SOFTWARE_CATALOG.md
```

如果你是 GitHub 新手，可以把它理解成一个**自动更新的工具清单**：

- 你运行 `awesome install <url-or-path>` 后，程序会自动判断分类，并把记录写进对应的 Markdown 文件。
- 平时你不用手动维护这些目录，也不用自己复制粘贴表格。
- 想查看全部资源，用 `awesome list`。
- 想查看某一类资源，用 `awesome list skills`、`awesome list tools`、`awesome list plugins`。
- 想找回某个资源，用 `awesome search <keyword>`。

也就是说，你只负责把 GitHub 链接丢进去；剩下的分类、归档、记录，交给它这个小仓库管理员就好。

每条记录的格式是：

```markdown
| Domain | Name | Repo | Summary | Status |
```

示例：

```markdown
| AI/Automation | my-skill | github.com/owner/my-skill | Helps Claude run a repeatable workflow. | installed |
```

## 🧪 测试

```bash
python3 -m unittest discover -s tests
```

## 🧭 后续路线

v1.1 先保证最小闭环可用。后续会逐步靠近原始愿景，把它从“能整理 GitHub repo 的 CLI”升级成“能和 Claude / Codex 协作的个人 AI 工具箱”。

### 近期增强

- 🧹 更完整的重复项清理：避免同一个 repo 被重复写进 catalog。
- 🧯 更稳定的错误处理：clone 失败、路径冲突、权限问题时给出更清楚的提示。
- 🧭 更可靠的分类规则：继续打磨 `skill / tool / script / plugin / software` 的边界。
- 🧾 更好看的 catalog 输出：让 `list` 和 `search` 的结果更适合人眼阅读。
- 🧪 更多测试：覆盖失败回退、跨平台路径、已安装判断等边界情况。

### 原始愿景方向

- 🌟 GitHub Stars 导入：把你收藏过的 repo 批量整理成分类工具箱。
- 🏷️ 标签系统：给项目打上更宽泛的领域标签，方便跨类别搜索。
- 🗣️ Claude / Codex 自然语言协作：不用记命令，直接说“帮我看看有哪些 AI 工具”。
- 🔁 更完整的安装策略：未来支持依赖安装、二进制链接、权限检查和失败回退。
- 🌐 更完整的多语言 README：让不同语言用户都能快速理解项目价值。

## 🌟 如果你也被收藏夹淹没了

如果你的 GitHub Stars 已经像阁楼里的纸箱一样越堆越高，里面明明有宝贝，但每次要找都像考古现场，那这个项目就是为了这件事来的。

`awesome-catalogs` 想做的事情很简单：

- 把散落的 GitHub repo 变成可搜索的工具箱。
- 把“我记得我收藏过一个东西”变成“我现在就能找到它”。
- 把 Claude / Codex 能用的 skill、tool、script、plugin 都归好类。
- 最后，把你的开发收藏夹变成一个真的能被 AI agent 调用和理解的资源库。

如果这个方向也戳中你，欢迎给一个 star ⭐。  
这颗星不会自动整理你的收藏夹，但它会让这个小仓库管理员更有动力继续进化。🧰✨
