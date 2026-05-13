---
name: skill-catalog-maintainer
description: 掃描、整理與維護本機 Claude skills 目錄與 SKILLS_CATALOG.md。當使用者想盤點 ~/.claude/skills、更新 skill 目錄、重新分類技能、找出重複/失效 skill，或在新增 skill 後同步總目錄時使用。
---

# Skill Catalog Maintainer

當使用者要整理 `~/.claude/skills/` 這個本機 skill 倉庫時，使用這個 skill。

## 核心目標

- 讓本機 skill 倉庫保持可讀、可掃描、可持續增長。
- 維護 `SKILLS_CATALOG.md` 作為分類目錄。
- 區分「安裝/匯入 skill」與「整理/盤點 skill 倉庫」這兩種不同工作。
- 在不破壞既有 skill 的前提下，補齊索引、分類與治理規則。

## 預設流程

1. 掃描 `~/.claude/skills/` 下的 skill 目錄。
2. 讀每個 `SKILL.md` 的 frontmatter 與前幾段正文。
3. 建立 skill 清單：名稱、主要用途、建議領域、是否重複或邊界模糊。
4. 讀現有 `SKILLS_CATALOG.md`。
5. 對比實際技能與目錄內容：缺了哪些、哪些描述過時、哪些分類不合理。
6. 小步更新目錄，而不是無差別重寫。
7. 回報：做了哪些更新、哪些 skill 值得再整理、哪些地方需要使用者決策。

## 分類原則

- 優先按「主要用途」分類，不按來源 repo 分類。
- 一個 skill 只放一個主分類，避免一份目錄重複出現多次。
- 如果 skill 跨多領域，按最常見觸發場景歸類。

## 目錄維護規則

- `SKILLS_CATALOG.md` 是總入口，不是長篇說明書。
- 每個 skill 在目錄中只保留：名稱、所屬領域、一句話簡介。
- 目錄內容要與實際磁碟狀態一致。
- 如果 skill 已刪除或失效，從目錄移除或標記。

## 何時應該更新目錄

- 新增 skill 之後
- 刪除或停用 skill 之後
- 同一類技能快速增長後
- 使用者要求盤點現有技能資產時
- 發現目錄與實際內容不一致時

## 好的觸發語句

- 「幫我整理 ~/.claude/skills」
- 「更新 SKILLS_CATALOG.md」
- 「盤點我現在有哪些 Claude skills」
- 「新增 skill 後幫我同步總目錄」
- 「找出這批 skills 有沒有重複」
- 「檢查目錄」→ 直接打開 `~/.claude/skills/SKILLS_CATALOG.md` 顯示表格內容
