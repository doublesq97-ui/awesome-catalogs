# awesome-catalogs 升级路线图

> 2026-05-19 · Phase 0 + 1 已完成 · 剩余 3 期规划中

---

## 已完成

### Phase 0：使用追踪（2026-05-19 交付 · v1.3.0）

追踪数据：`~/.claude/awesome-catalogs/activity.json`

| 能力 | 说明 |
|------|------|
| 安装时间记录 | `awesome install` 自动写入 `installed_at` |
| 使用次数统计 | `awesome record-usage <name>` 时 `times_used += 1` |
| 最后使用时间 | 更新 `last_used_at` |
| 5 分制评分 | 距上次使用：█████（≤7天）→ ░░░░░（从未使用） |
| 僵尸扫描 | `awesome cleanup` 列出 score 0–1 项目 |
| 批量清理 | `awesome cleanup --force` 确认后删除 + 同步 catalog + activity.json |

### Phase 1：装前评估（2026-05-19 交付 · v1.4.0）

触发：用户给 GitHub 链接 → 自动拉 GitHub API → 7 维评估 → 输出建议表格

```
awesome evaluate https://github.com/owner/repo
```

| 评估维度 | 数据来源 | 示例输出 |
|----------|----------|----------|
| 热度 | GitHub stars/forks | ⭐ 44K stars |
| 活跃度 | 最近 push 日期 | 🟢 昨天有 commit |
| 社区健康 | open issues 数量 | 🟡 140 open issues |
| 版本稳定性 | latest release tag / 是否 pre-release | ⚠️ 0.8.0-preview |
| 安装成本 | README 检测 monorepo/Docker/Electron 等信号 | 🔴 monorepo + pnpm + Electron |
| 重叠度 | 与 activity.json 中已有工具的功能关键词对比 | 🟡 3 个同类已安装（均 ░░░░░） |
| 场景匹配 | 同域已安装工具的使用频次分析 | 🟡 设计域 30 天内 0 次使用 |

输出格式：7 维表格 + 🟢推荐/🟡观望/🔴不建议 三级建议

---

## 待规划

### Phase 2：重叠检测

```
触发：安装前 / 评估时自动跑
执行：提取新工具 README 关键功能词 → 跟 activity.json 所有已安装 item 做语义对比
```

| 对比层 | 方法 | 示例 |
|--------|------|------|
| 功能关键词 | README 提取 vs 已安装 item 的 description | "PPT 生成"、"品牌设计"、"幻灯片" |
| 域匹配 | domain tag 是否相同 | 都是 🎨 Design |
| 输出格式 | 都输出 HTML/PPTX/PDF？ | 都输出单文件 HTML |
| 触发场景 | 用户描述的使用场景是否重叠 | "做 PPT"、"出海报" |

价值增量：需要知道本地装了啥 + 每个的功能边界——这俩数据纯模型拿不到。

### Phase 3：反推荐 + 智能推荐

```
触发（反推荐）：Phase 1/2 判断不适合安装时自动触发
触发（智能推荐）：查看目录时，检测"高频域 × 未使用工具"交叉
```

**反推荐输出示例：**

```
❌ 不建议现在安装 Open Design

→ 你已有 `design` — 品牌设计/logo/调色板
→ 你已有 `slides` + `guizang-ppt-skill` — HTML PPT/杂志风翻页
→ 你已有 `ui-ux-pro-max` — 50+ 设计风格/161 色盘

先试试这些？[使用 design] [使用 slides] [跳过]
```

**智能推荐输出示例：**

```
💡 你最近 7 天频繁使用 🌐 Social Media 域：
  redbook █████（5次）

同一域还有 2 个从未使用的 skill：
  redbook-creator — 小红书笔记创作
  wechat-official-account-article-auto-publisher — 公众号草稿发布

要了解一下吗？[了解更多] [跳过]
```

价值增量：需要同时掌握三重数据——本地库存、用户行为模式、工具功能关系图。

### Phase 4：定期健康检查

```
触发：awesome-catalogs 被调用时自动检查
不主动打扰，只在 skill 已被使用的上下文中顺便提醒
```

| 检查项 | 条件 | 动作 |
|--------|------|------|
| 清理提醒 | `last_cleanup_check` > 30 天 + 有 0 分项 | "上次清理是 30 天前，现有 12 个 ░░░░░" |
| 僵尸预警 | 某 item 安装 > 90 天且从未使用 | "X 装了 3 个月从未用过，要清理吗？" |
| 死链检测 | git repo 已 archive/404 | "X 原始仓库已归档，可能不再维护" |

价值增量：时间维度的判断——模型记不住"上次什么时候做的清理"。

---

## 优先级总览

```
Phase 0: 使用追踪         [██████████] ✅ v1.3.0
Phase 1: 装前评估         [██████████] ✅ v1.4.0
Phase 2: 重叠检测         [██████░░░░] 下一期·提升评估精度·减少误装
Phase 3: 反推荐+智能推荐  [████░░░░░░] 依赖 Phase 2 重叠数据
Phase 4: 定期健康检查     [██░░░░░░░░] 锦上添花·边际收益递减
```

一次一个 Phase，不强追进度。
