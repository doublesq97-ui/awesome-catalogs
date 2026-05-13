# 给创作者的 v1.1 修改建议

你好，我按 `catelogs-v1/README.md` 自己承诺的范围做了一次发布前审核。我的结论是：这个项目可以称为 v1，但建议不要把当前版本直接当最终稳定版发布；更合适的做法是发布一个 `v1.1`，把“最小闭环”打磨到可信。

## 为什么它可以叫 v1

- README 已经明确声明 v1 是最小闭环，不承诺 Stars 导入、自然语言协作、多语言完整体验等最终愿景能力。
- CLI 的核心链路已经跑通：`classify`、`install`、`--dry-run`、`list`、`search` 都能工作。
- 项目结构清晰，代码量小，适合继续迭代。

## 为什么建议先做 v1.1

当前 v1 最大的问题不是功能少，而是核心分类规则还不够可信。自动分类是项目的第一卖点，如果分类容易误判，用户会很快失去信任。

建议 v1.1 优先修这几件事：

1. 修复 plugin 误判：不要因为 README 里普通提到 `plugin`、`MCP`、`Claude plugin` 就直接判为插件，应优先相信真实配置文件，比如 `mcp.json`、`plugin.json`、`.codex-plugin/plugin.json`。
2. 修复中文目录名：本地 repo 名是中文时，不应全部退化成 `repo`，否则 catalog 和安装目录会冲突。
3. 收紧 tool 判断：不要因为有 `Makefile` 或 `Cargo.toml` 就判为 CLI 工具，很多普通库或软件也有这些文件。
4. 增加测试：至少覆盖 skill、tool、script、plugin、software、中文路径、README 摘要清洗。
5. README 改成 v1.1 真实能力：保留边界说明，把未实现功能放进后续路线图，不要混进当前能力。

## 我建议的发布表述

可以这样写：

> awesome-catalogs v1.1 是一个可运行的 GitHub 资源整理器。它聚焦最小可用闭环：输入 GitHub repo 或本地路径，基于结构化规则分类为 skill/tool/script/plugin/software，复制到对应本地目录，并更新可搜索的 Markdown catalog。Stars 批量导入、自然语言协作和更复杂的安装策略会放到后续版本。

## 不建议现在这样写

不建议把这些写成当前已实现能力：

- GitHub Stars 批量导入
- 自然语言自动协作
- 自动调用相关 skill
- remove 命令
- 依赖安装、二进制链接、权限检查
- 多语言 README 已完整覆盖并和功能保持同步

这些都可以作为 roadmap，但不要作为 v1.1 当前能力。

## v1.1 发布前验收清单

- `python3 -m awesome_catalogs --help` 能正常显示命令。
- `awesome classify /path/to/skill-repo` 能识别 skill。
- README 里提到 plugin 分类规则的普通项目不会被误判成 plugin。
- 中文目录名不会被安装成统一的 `repo`。
- `awesome install /local/repo --dry-run` 不写文件，只输出分类和目标路径。
- `awesome install /local/repo --force` 能复制并更新 catalog。
- `awesome list` 能看到总 catalog。
- `awesome search keyword` 能搜到已安装记录。
- `python3 -m unittest discover -s tests` 全部通过。

## 星标价值判断

如果按 v1.1 这个范围发布，我认为它已经具备“值得早期 star”的基础：概念清楚、能跑、有明确边界、后续空间大。它还不是成熟明星项目，但可以是一个值得关注的 early-stage 工具。
