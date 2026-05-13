# 🛠️ awesome-claude-skills-manager

> Paste a GitHub link — auto-classify, one-click install, update catalog.

![version](https://img.shields.io/badge/version-v1.0.0-green)
![categories](https://img.shields.io/badge/categories-5-blue)
![languages](https://img.shields.io/badge/languages-8-purple)
![license](https://img.shields.io/badge/license-MIT-blue)

---

🌐 **[简体中文](#zh-CN)** | **[English](#en)** | **[繁體中文](#zh-TW)** | **[हिन्दी](#hi)** | **[Русский](#ru)** | **[Español](#es)** | **[Français](#fr)** | **[العربية](#ar)**

---

## 🇨🇳 简体中文 <a id="zh-CN"></a>

### 这是什么？

一个**通用 GitHub 资源管理器**：贴一个 GitHub 链接，自动识别它是 Skill、CLI 工具、脚本、插件还是完整软件，**一键安装到对应目录**，同时更新可搜索的分类目录。

既是 Claude 的 `SKILL.md` 指令包，也是开发者的命令行工具箱。

### 六大核心能力

- 🔍 **自动分类** — 分析 repo 结构，秒判 技能/工具/脚本/插件/软件
- 📝 **语义摘要** — 自动从 README 提取一句话说明，不用点进 repo
- ⚡ **一键安装** — 直接丢链接（agent）/ `awesome install <url>`（CLI），装完立即可用
- 🌟 **Star 导入** — 把你的 GitHub Stars 一次性整理成分类工具箱
- 🏷️ **标签系统** — 所有项目挂宽泛领域标签，跨类别搜索
- 🗣️ **自然语言交互** — 在 Claude / Codex 里直接用自然语言操作，丢链接、问目录、查 stars（收藏），不用记命令

### 快速开始

**Claude Code 用户 — 复制这一行到 Claude：**

```
add skill from github.com/doublesq97-ui/awesome-claude-skills-manager
```

**Codex CLI 用户 — 复制这一行：**

```
codex skill install doublesq97-ui/awesome-claude-skills-manager
```

**终端用户：**

```bash
git clone https://github.com/doublesq97-ui/awesome-claude-skills-manager.git
./scripts/install.sh
awesome install github.com/作者/repo
```

### CLI 命令

| 命令 | 说明 |
|------|------|
| `awesome install <url>` | 贴链接 → 自动分类 → 安装 |
| `awesome list <类别>` | 查看任一类别的目录 |
| `awesome search "关键词"` | 跨类别搜索 |
| `awesome import-stars <用户名>` | 批量导入 GitHub Stars |
| `awesome remove <名称>` | 移除已安装项目 |

### 自然语言也能操作

在 Claude / Codex 里，直接用说的就能管理你的 GitHub 资源：

| 你说 | 效果 |
|------|------|
| 贴一个 GitHub 链接 | 自动分类 → 一键安装 |
| "查看我的 github 目录" | 弹出总目录 `CATALOG.md` |
| "看看我的 skill" | 显示 skill 分类目录 |
| "我还有哪些 star 没装？" | 启动 star 扫描，列出推荐安装 |
| “搜索 AI 工具” | 跨类别搜索 AI 相关项目 |
| “我准备做小红书内容，你调用一下对应 skill” | 查找「小红书」相关 skill 并启用 |



### 本管理器的决策逻辑

| 条件 | 决策 |
|------|------|
| 有 `SKILL.md` | ✅ 推荐安装（技能包） |
| 有 CLI 入口（`bin/`、`main.go`、`cli.py`） | ✅ 推荐安装（工具/脚本） |
| 是 MCP server / Claude plugin | ✅ 推荐安装（插件） |
| 纯库（只有 `src/`，无 CLI） | ⏭️ 跳过 |
| 文档/教程/awesome-list | ⏭️ 跳过 |
| 已弃用（3 年未更新） | ⚠️ 标记警告 |
| 已安装 | 📦 标记已安装 |

### 五大类别 + 安装目标

| 类别 | 目录 | 判断依据 |
|------|------|------|
| 🧩 Skill | `~/.claude/skills/` | 有 `SKILL.md`，专为 Claude 设计 |
| 🔧 Tool | `~/.claude/tools/` | 有 CLI 入口，`bin/`、`main.go`、`cli.py` |
| 📜 Script | `~/.claude/scripts/` | 单文件脚本，`.sh`/`.py`/`.js` |
| 🔌 Plugin | `~/.claude/plugins/` | Claude Code plugin 格式、MCP |
| 📦 Software | `~/claude-projects/` | 完整应用或独立项目 |

### 如果对你有帮助

（支付宝 / 微信赞助二维码）

感谢你的支持 🙏

[↑ 回到顶部](#)

---

## 🇺🇸 English <a id="en"></a>

### What is this?

A **universal GitHub resource manager**: paste a GitHub link and it auto-classifies into Skill, CLI Tool, Script, Plugin, or Software — then **installs it with one command** and updates a searchable catalog.

Works as both a Claude `SKILL.md` instruction pack and a developer CLI toolbox.

### Six Core Capabilities

- 🔍 **Auto-classify** — Detects repo type in seconds
- 📝 **Smart summary** — Extracts a one-liner from the README
- ⚡ **One-click install** — drop a link (agent) / `awesome install <url>` (CLI)
- 🌟 **Star import** — Turn your GitHub Stars into an organized toolbox
- 🏷️ **Tag system** — Broad domain tags for cross-category search
- 🗣️ **Natural language** — In Claude / Codex, just talk to it — drop a link, ask about your catalog, or check stars in plain language

### Quick Start

**Claude Code users — copy this line into Claude:**

```
add skill from github.com/doublesq97-ui/awesome-claude-skills-manager
```

**Codex CLI users — copy this line:**

```
codex skill install doublesq97-ui/awesome-claude-skills-manager
```

**Terminal users:**

```bash
git clone https://github.com/doublesq97-ui/awesome-claude-skills-manager.git
./scripts/install.sh
awesome install github.com/author/repo
```

### CLI Commands

| Command | Description |
|------|------|
| `awesome install <url>` | Paste link → classify → install |
| `awesome list <category>` | Browse any category catalog |
| `awesome search "keyword"` | Search across all categories |
| `awesome import-stars <user>` | Batch-import your GitHub Stars |
| `awesome remove <name>` | Remove an installed item |

### Natural Language Usage

Inside Claude / Codex, manage your GitHub resources using plain language:

| You say | It does |
|------|------|
| Paste a GitHub link | Auto-classify → install |
| "Show my github catalog" | Opens `CATALOG.md` |
| "What skills do I have?" | Lists all installed skills |
| "Which stars haven't I installed yet?" | Scans stars → recommends what to install |
| "Search for AI tools" | Searches across all categories for AI |
| "I'm making Redbook content, load the relevant skill" | Finds and activates Redbook-related skills |

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

### Five Categories & Install Targets

| Category | Directory | Detection |
|------|------|------|
| 🧩 Skill | `~/.claude/skills/` | Contains `SKILL.md` |
| 🔧 Tool | `~/.claude/tools/` | Has CLI entry, `bin/`, `main.go`, `cli.py` |
| 📜 Script | `~/.claude/scripts/` | Single-file, `.sh`/`.py`/`.js` |
| 🔌 Plugin | `~/.claude/plugins/` | Claude Code plugin format, MCP |
| 📦 Software | `~/claude-projects/` | Full application or standalone project |

### Support

(Alipay / WeChat donation QR codes)

Thank you for your support 🙏

[↑ Back to top](#)

---

## 繁體中文 <a id="zh-TW"></a>

### 這是什麼？

一個**通用 GitHub 資源管理器**：貼一個 GitHub 鏈結，自動判斷它是 Skill、CLI 工具、腳本、外掛還是完整軟體，**一鍵安裝到對應目錄**，同步更新可搜尋的分類目錄。

既是 Claude 的 `SKILL.md` 指令包，也是開發者的命令列工具箱。

### 六大核心能力

- 🔍 **自動分類** — 分析 repo 結構，秒判 技能/工具/腳本/外掛/軟體
- 📝 **語義摘要** — 自動從 README 提取一句話說明，不用點進 repo
- ⚡ **一鍵安裝** — 直接丟連結（agent）/ `awesome install <url>`（CLI），裝完立即可用
- 🌟 **Star 匯入** — 把你的 GitHub Stars 一次性整理成分類工具箱
- 🏷️ **標籤系統** — 所有專案掛寬泛領域標籤，跨類別搜尋
- 🗣️ **自然語言互動** — 在 Claude / Codex 裡直接用自然語言操作，丟連結、問目錄、查 star，不用記命令

### 快速開始

**Claude Code 使用者 — 複製這行到 Claude：**

```
add skill from github.com/doublesq97-ui/awesome-claude-skills-manager
```

**Codex CLI 使用者 — 複製這行：**

```
codex skill install doublesq97-ui/awesome-claude-skills-manager
```

**終端機使用者：**

```bash
git clone https://github.com/doublesq97-ui/awesome-claude-skills-manager.git
./scripts/install.sh
awesome install github.com/作者/repo
```

### CLI 命令

| 命令 | 說明 |
|------|------|
| `awesome install <url>` | 貼鏈結 → 自動分類 → 安裝 |
| `awesome list <類別>` | 檢視任一類別的目錄 |
| `awesome search "關鍵詞"` | 跨類別搜尋 |
| `awesome import-stars <使用者名稱>` | 批次匯入 GitHub Stars |
| `awesome remove <名稱>` | 移除已安裝項目 |

### 自然語言也能操作

在 Claude / Codex 裡，直接用說的就能管理你的 GitHub 資源：

| 你說 | 效果 |
|------|------|
| 貼一個 GitHub 鏈結 | 自動分類 → 一鍵安裝 |
| 「查看我的 github 目錄」 | 彈出總目錄 `CATALOG.md` |
| 「看看我的 skill」 | 顯示 skill 分類目錄 |
| 「我還有哪些 star 沒裝？」 | 啟動 star 掃描，列出推薦安裝 |
| 「搜尋 AI 工具」 | 跨類別搜尋 AI 相關專案 |
| 「我準備做小紅書內容，你調用一下對應 skill」 | 查找「小紅書」相關 skill 並啟用 |

### 本管理器的決策邏輯

| 條件 | 決策 |
|------|------|
| 有 `SKILL.md` | ✅ 推薦安裝（技能包） |
| 有 CLI 入口（`bin/`、`main.go`、`cli.py`） | ✅ 推薦安裝（工具/腳本） |
| 是 MCP server / Claude plugin | ✅ 推薦安裝（外掛） |
| 純庫（只有 `src/`，無 CLI） | ⏭️ 跳過 |
| 文件/教學/awesome-list | ⏭️ 跳過 |
| 已棄用（3 年未更新） | ⚠️ 標記警告 |
| 已安裝 | 📦 標記已安裝 |

### 五大類別 + 安裝目標

| 類別 | 目錄 | 判斷依據 |
|------|------|------|
| 🧩 Skill | `~/.claude/skills/` | 有 `SKILL.md`，專為 Claude 設計 |
| 🔧 Tool | `~/.claude/tools/` | 有 CLI 入口，`bin/`、`main.go`、`cli.py` |
| 📜 Script | `~/.claude/scripts/` | 單文件腳本，`.sh`/`.py`/`.js` |
| 🔌 Plugin | `~/.claude/plugins/` | Claude Code plugin 格式、MCP |
| 📦 Software | `~/claude-projects/` | 完整應用或獨立專案 |

### 如果對你有幫助

（支付寶 / 微信贊助二維碼）

感謝你的支持 🙏

[↑ 回到頂部](#)

---

## 🇮🇳 हिन्दी <a id="hi"></a>

### यह क्या है?

एक **सार्वभौमिक GitHub संसाधन प्रबंधक**: GitHub लिंक पेस्ट करें, यह स्वतः पहचान करेगा कि यह Skill, CLI Tool, Script, Plugin या Software है — फिर **एक कमांड से इंस्टॉल करें** और खोजने योग्य कैटलॉग अपडेट हो जाएगा।

### छह मुख्य क्षमताएँ

- 🔍 **स्वतः वर्गीकरण** — रेपो संरचना का विश्लेषण करके तुरंत पहचान
- 📝 **स्मार्ट सारांश** — README से एक-पंक्ति विवरण निकालता है
- ⚡ **एक-क्लिक इंस्टॉल** — लिंक डालें (agent) / `awesome install <url>` (CLI)
- 🌟 **स्टार आयात** — अपने GitHub Stars को व्यवस्थित टूलबॉक्स में बदलें
- 🏷️ **टैग प्रणाली** — क्रॉस-श्रेणी खोज के लिए व्यापक डोमेन टैग
- 🗣️ **प्राकृतिक भाषा** — Claude / Codex में, सीधे बात करें — लिंक डालें, कैटलॉग पूछें, या स्टार की जाँच करें

### त्वरित शुरुआत

**Claude Code उपयोगकर्ता — यह लाइन Claude में कॉपी करें:**

```
add skill from github.com/doublesq97-ui/awesome-claude-skills-manager
```

**Codex CLI उपयोगकर्ता — यह लाइन कॉपी करें:**

```
codex skill install doublesq97-ui/awesome-claude-skills-manager
```

**टर्मिनल उपयोगकर्ता:**

```bash
git clone https://github.com/doublesq97-ui/awesome-claude-skills-manager.git
./scripts/install.sh
awesome install github.com/लेखक/repo
```

### CLI कमांड

| कमांड | विवरण |
|------|------|
| `awesome install <url>` | लिंक पेस्ट करें → वर्गीकृत करें → इंस्टॉल करें |
| `awesome list <श्रेणी>` | किसी भी श्रेणी का कैटलॉग देखें |
| `awesome search "कीवर्ड"` | सभी श्रेणियों में खोजें |
| `awesome import-stars <उपयोगकर्ता>` | अपने GitHub Stars को बैच-आयात करें |
| `awesome remove <नाम>` | इंस्टॉल किए गए आइटम को हटाएँ |

### प्राकृतिक भाषा उपयोग

Claude / Codex में, साधारण भाषा में अपने GitHub संसाधन प्रबंधित करें:

| आप कहें | यह करता है |
|------|------|
| GitHub लिंक पेस्ट करें | स्वतः वर्गीकरण → इंस्टॉल |
| "मेरा github कैटलॉग दिखाओ" | `CATALOG.md` खोलता है |
| "मेरे पास कौन से skills हैं?" | सभी इंस्टॉल किए गए skills सूचीबद्ध करता है |
| "कौन से stars अभी तक इंस्टॉल नहीं किए?" | stars स्कैन करता है → इंस्टॉल की सिफारिश |
| "AI टूल्स खोजो" | सभी श्रेणियों में AI के लिए खोजता है |
| "मैं Redbook सामग्री बना रहा हूँ, संबंधित skill लोड करो" | Redbook-संबंधित skills ढूँढता और सक्रिय करता है |

### निर्णय तर्क

| शर्त | कार्रवाई |
|------|------|
| `SKILL.md` मौजूद | ✅ अनुशंसित (स्किल पैक) |
| CLI प्रवेश बिंदु (`bin/`, `main.go`, `cli.py`) | ✅ अनुशंसित (टूल/स्क्रिप्ट) |
| MCP सर्वर / Claude प्लगइन | ✅ अनुशंसित (प्लगइन) |
| शुद्ध लाइब्रेरी (केवल `src/`, CLI नहीं) | ⏭️ छोड़ें |
| दस्तावेज़/ट्यूटोरियल/awesome-list | ⏭️ छोड़ें |
| परित्यक्त (3+ वर्ष कोई अपडेट नहीं) | ⚠️ चेतावनी |
| पहले से इंस्टॉल | 📦 इंस्टॉल के रूप में चिह्नित |

### पाँच श्रेणियाँ और इंस्टॉल लक्ष्य

| श्रेणी | निर्देशिका | पहचान |
|------|------|------|
| 🧩 Skill | `~/.claude/skills/` | `SKILL.md` शामिल है |
| 🔧 Tool | `~/.claude/tools/` | CLI प्रवेश, `bin/`, `main.go`, `cli.py` |
| 📜 Script | `~/.claude/scripts/` | एकल-फ़ाइल, `.sh`/`.py`/`.js` |
| 🔌 Plugin | `~/.claude/plugins/` | Claude Code प्लगइन प्रारूप, MCP |
| 📦 Software | `~/claude-projects/` | पूर्ण अनुप्रयोग या स्वतंत्र परियोजना |

### समर्थन

(Alipay / WeChat दान QR कोड)

आपके समर्थन के लिए धन्यवाद 🙏

[↑ ऊपर वापस जाएँ](#)

---

## 🇷🇺 Русский <a id="ru"></a>

### Что это?

**Универсальный менеджер GitHub-ресурсов**: вставьте ссылку на GitHub — он автоматически определит тип: Skill, CLI-инструмент, скрипт, плагин или программа — и **установит одной командой**, обновив каталог для поиска.

### Шесть возможностей

- 🔍 **Автоклассификация** — анализ структуры репо за секунды
- 📝 **Умное описание** — извлечение краткого описания из README
- ⚡ **Установка одной командой** — вставьте ссылку (agent) / `awesome install <url>` (CLI)
- 🌟 **Импорт звёзд** — превратите ваши GitHub Stars в организованный набор инструментов
- 🏷️ **Система тегов** — широкие доменные теги для межкатегорийного поиска
- 🗣️ **Естественный язык** — В Claude / Codex просто говорите с ним — вставьте ссылку, спросите каталог или проверьте звёзды

### Быстрый старт

**Пользователи Claude Code — скопируйте эту строку в Claude:**

```
add skill from github.com/doublesq97-ui/awesome-claude-skills-manager
```

**Пользователи Codex CLI — скопируйте эту строку:**

```
codex skill install doublesq97-ui/awesome-claude-skills-manager
```

**Пользователи терминала:**

```bash
git clone https://github.com/doublesq97-ui/awesome-claude-skills-manager.git
./scripts/install.sh
awesome install github.com/автор/repo
```

### Команды CLI

| Команда | Описание |
|------|------|
| `awesome install <url>` | Ссылка → классификация → установка |
| `awesome list <категория>` | Просмотр каталога любой категории |
| `awesome search "ключ"` | Поиск по всем категориям |
| `awesome import-stars <пользователь>` | Пакетный импорт ваших GitHub Stars |
| `awesome remove <имя>` | Удалить установленный элемент |

### Использование естественным языком

В Claude / Codex управляйте ресурсами GitHub на простом языке:

| Вы говорите | Оно делает |
|------|------|
| Вставить ссылку GitHub | Автоклассификация → установка |
| «Покажи мой github каталог» | Открывает `CATALOG.md` |
| «Какие у меня есть навыки?» | Показывает все установленные skills |
| «Какие звёзды ещё не установлены?» | Сканирует звёзды → рекомендует что установить |
| «Найди AI инструменты» | Ищет AI по всем категориям |
| «Я делаю контент для Redbook, загрузи нужный skill» | Находит и активирует skills для Redbook |

### Логика решений

| Условие | Действие |
|------|------|
| Есть `SKILL.md` | ✅ Рекомендовать (пакет навыков) |
| Есть CLI вход (`bin/`, `main.go`, `cli.py`) | ✅ Рекомендовать (инструмент/скрипт) |
| MCP сервер / Claude плагин | ✅ Рекомендовать (плагин) |
| Чистая библиотека (только `src/`, без CLI) | ⏭️ Пропустить |
| Документация/туториал/awesome-list | ⏭️ Пропустить |
| Заброшен (3+ года без обновлений) | ⚠️ Предупредить |
| Уже установлен | 📦 Отметить как установленный |

### Пять категорий и цели установки

| Категория | Каталог | Определение |
|------|------|------|
| 🧩 Skill | `~/.claude/skills/` | Содержит `SKILL.md` |
| 🔧 Tool | `~/.claude/tools/` | Есть CLI вход, `bin/`, `main.go`, `cli.py` |
| 📜 Script | `~/.claude/scripts/` | Один файл, `.sh`/`.py`/`.js` |
| 🔌 Plugin | `~/.claude/plugins/` | Формат Claude Code плагина, MCP |
| 📦 Software | `~/claude-projects/` | Полное приложение или независимый проект |

### Поддержка

(QR-коды Alipay / WeChat для пожертвований)

Спасибо за вашу поддержку 🙏

[↑ Наверх](#)

---

## 🇪🇸 Español <a id="es"></a>

### ¿Qué es esto?

Un **gestor universal de recursos de GitHub**: pega un enlace de GitHub, detecta automáticamente si es un Skill, herramienta CLI, script, plugin o software — y **lo instala con un solo comando**, actualizando un catálogo consultable.

### Seis capacidades

- 🔍 **Autoclasificación** — Analiza la estructura del repo en segundos
- 📝 **Resumen inteligente** — Extrae una descripción breve del README
- ⚡ **Instalación en un clic** — suelta un enlace (agent) / `awesome install <url>` (CLI)
- 🌟 **Importar Stars** — Convierte tus GitHub Stars en una caja de herramientas organizada
- 🏷️ **Etiquetas** — Etiquetas de dominio amplias para búsqueda entre categorías
- 🗣️ **Lenguaje natural** — En Claude / Codex, solo háblale — suelta un enlace, pregunta por el catálogo o revisa tus estrellas

### Inicio rápido

**Usuarios de Claude Code — copia esta línea en Claude:**

```
add skill from github.com/doublesq97-ui/awesome-claude-skills-manager
```

**Usuarios de Codex CLI — copia esta línea:**

```
codex skill install doublesq97-ui/awesome-claude-skills-manager
```

**Usuarios de terminal:**

```bash
git clone https://github.com/doublesq97-ui/awesome-claude-skills-manager.git
./scripts/install.sh
awesome install github.com/autor/repo
```

### Comandos CLI

| Comando | Descripción |
|------|------|
| `awesome install <url>` | Pegar enlace → clasificar → instalar |
| `awesome list <categoría>` | Ver el catálogo de cualquier categoría |
| `awesome search "clave"` | Buscar en todas las categorías |
| `awesome import-stars <usuario>` | Importar tus GitHub Stars por lotes |
| `awesome remove <nombre>` | Eliminar un elemento instalado |

### Uso en lenguaje natural

Dentro de Claude / Codex, gestiona tus recursos de GitHub usando lenguaje natural:

| Tú dices | Él hace |
|------|------|
| Pegar un enlace de GitHub | Autoclasificar → instalar |
| "Muéstrame mi catálogo github" | Abre `CATALOG.md` |
| "¿Qué skills tengo?" | Lista todos los skills instalados |
| "¿Qué estrellas no he instalado aún?" | Escanea estrellas → recomienda qué instalar |
| "Busca herramientas de IA" | Busca IA en todas las categorías |
| "Voy a crear contenido de Redbook, carga el skill adecuado" | Encuentra y activa skills relacionados con Redbook |

### Lógica de decisión

| Condición | Acción |
|------|------|
| Tiene `SKILL.md` | ✅ Recomendar (paquete de skill) |
| Tiene entrada CLI (`bin/`, `main.go`, `cli.py`) | ✅ Recomendar (herramienta/script) |
| Es servidor MCP / plugin de Claude | ✅ Recomendar (plugin) |
| Biblioteca pura (solo `src/`, sin CLI) | ⏭️ Omitir |
| Documentos/tutorial/awesome-list | ⏭️ Omitir |
| Abandonado (3+ años sin actualizar) | ⚠️ Marcar advertencia |
| Ya instalado | 📦 Marcar como instalado |

### Cinco categorías y destinos de instalación

| Categoría | Directorio | Detección |
|------|------|------|
| 🧩 Skill | `~/.claude/skills/` | Contiene `SKILL.md` |
| 🔧 Tool | `~/.claude/tools/` | Tiene entrada CLI, `bin/`, `main.go`, `cli.py` |
| 📜 Script | `~/.claude/scripts/` | Archivo único, `.sh`/`.py`/`.js` |
| 🔌 Plugin | `~/.claude/plugins/` | Formato plugin Claude Code, MCP |
| 📦 Software | `~/claude-projects/` | Aplicación completa o proyecto independiente |

### Apoyo

(Códigos QR de Alipay / WeChat para donaciones)

Gracias por tu apoyo 🙏

[↑ Volver arriba](#)

---

## 🇫🇷 Français <a id="fr"></a>

### Qu'est-ce que c'est ?

Un **gestionnaire universel de ressources GitHub** : collez un lien GitHub, il détecte automatiquement s'il s'agit d'un Skill, d'un outil CLI, d'un script, d'un plugin ou d'un logiciel — puis **l'installe en une commande** et met à jour un catalogue consultable.

### Six capacités

- 🔍 **Classification automatique** — Analyse la structure du repo en quelques secondes
- 📝 **Résumé intelligent** — Extrait une description d'une ligne du README
- ⚡ **Installation en un clic** — déposez un lien (agent) / `awesome install <url>` (CLI)
- 🌟 **Importer les Stars** — Transformez vos GitHub Stars en boîte à outils organisée
- 🏷️ **Système d'étiquettes** — Étiquettes de domaine larges pour la recherche transversale
- 🗣️ **Langage naturel** — Dans Claude / Codex, parlez-lui simplement — déposez un lien, demandez le catalogue ou vérifiez vos étoiles

### Démarrage rapide

**Utilisateurs de Claude Code — copiez cette ligne dans Claude :**

```
add skill from github.com/doublesq97-ui/awesome-claude-skills-manager
```

**Utilisateurs de Codex CLI — copiez cette ligne :**

```
codex skill install doublesq97-ui/awesome-claude-skills-manager
```

**Utilisateurs du terminal :**

```bash
git clone https://github.com/doublesq97-ui/awesome-claude-skills-manager.git
./scripts/install.sh
awesome install github.com/auteur/repo
```

### Commandes CLI

| Commande | Description |
|------|------|
| `awesome install <url>` | Coller le lien → classer → installer |
| `awesome list <catégorie>` | Consulter le catalogue d'une catégorie |
| `awesome search "mot-clé"` | Rechercher dans toutes les catégories |
| `awesome import-stars <utilisateur>` | Importer vos GitHub Stars par lot |
| `awesome remove <nom>` | Supprimer un élément installé |

### Utilisation en langage naturel

Dans Claude / Codex, gérez vos ressources GitHub en langage naturel :

| Vous dites | Il fait |
|------|------|
| Coller un lien GitHub | Classification auto → installer |
| « Montre mon catalogue github » | Ouvre `CATALOG.md` |
| « Quels skills ai-je ? » | Liste tous les skills installés |
| « Quelles étoiles n'ai-je pas encore installées ? » | Analyse les étoiles → recommande quoi installer |
| « Cherche des outils IA » | Recherche IA dans toutes les catégories |
| « Je crée du contenu Redbook, charge le skill adapté » | Trouve et active les skills liés à Redbook |

### Logique de décision

| Condition | Action |
|------|------|
| Contient `SKILL.md` | ✅ Recommander (pack de skill) |
| A un point d'entrée CLI (`bin/`, `main.go`, `cli.py`) | ✅ Recommander (outil/script) |
| Est un serveur MCP / plugin Claude | ✅ Recommander (plugin) |
| Bibliothèque pure (`src/` uniquement, pas de CLI) | ⏭️ Ignorer |
| Documentation/tutoriel/awesome-list | ⏭️ Ignorer |
| Abandonné (3+ ans sans mise à jour) | ⚠️ Avertir |
| Déjà installé | 📦 Marquer comme installé |

### Cinq catégories et cibles d'installation

| Catégorie | Répertoire | Détection |
|------|------|------|
| 🧩 Skill | `~/.claude/skills/` | Contient `SKILL.md` |
| 🔧 Tool | `~/.claude/tools/` | A une entrée CLI, `bin/`, `main.go`, `cli.py` |
| 📜 Script | `~/.claude/scripts/` | Fichier unique, `.sh`/`.py`/`.js` |
| 🔌 Plugin | `~/.claude/plugins/` | Format plugin Claude Code, MCP |
| 📦 Software | `~/claude-projects/` | Application complète ou projet autonome |

### Soutien

(Codes QR Alipay / WeChat pour les dons)

Merci pour votre soutien 🙏

[↑ Retour en haut](#)

---

## 🇸🇦 العربية <a id="ar"></a>

<div dir="rtl">

### ما هذا؟

**مدير موارد GitHub الشامل**: الصق رابط GitHub وسيصنفه تلقائيًا إلى مهارة أو أداة CLI أو سكريبت أو ملحق أو برنامج — ثم **يثبته بأمر واحد** ويحدث كتالوجًا قابلاً للبحث.

### ست قدرات أساسية

- 🔍 **تصنيف تلقائي** — يحلل هيكل المستودع في ثوانٍ
- 📝 **ملخص ذكي** — يستخرج وصفًا موجزًا من README
- ⚡ **تثبيت بنقرة واحدة** — ضع رابطًا (agent) / `awesome install <url>` (CLI)
- 🌟 **استيراد النجوم** — حوّل نجوم GitHub الخاصة بك إلى صندوق أدوات منظم
- 🏷️ **نظام الوسوم** — وسوم نطاق واسعة للبحث عبر الفئات
- 🗣️ **لغة طبيعية** — في Claude / Codex، تحدث إليه مباشرة — ضع رابطًا، اسأل عن الكتالوج، أو راجع نجومك

### بداية سريعة

**مستخدمو Claude Code — انسخ هذا السطر إلى Claude:**

```
add skill from github.com/doublesq97-ui/awesome-claude-skills-manager
```

**مستخدمو Codex CLI — انسخ هذا السطر:**

```
codex skill install doublesq97-ui/awesome-claude-skills-manager
```

**مستخدمو الطرفية:**

```bash
git clone https://github.com/doublesq97-ui/awesome-claude-skills-manager.git
./scripts/install.sh
awesome install github.com/مؤلف/repo
```

### أوامر CLI

| الأمر | الوصف |
|------|------|
| `awesome install <url>` | الصق الرابط ← صنف ← ثبّت |
| `awesome list <فئة>` | تصفح كتالوج أي فئة |
| `awesome search "كلمة"` | ابحث عبر جميع الفئات |
| `awesome import-stars <مستخدم>` | استيراد نجوم GitHub دفعة واحدة |
| `awesome remove <اسم>` | إزالة عنصر مثبت |

### الاستخدام باللغة الطبيعية

داخل Claude / Codex، أدر موارد GitHub باستخدام لغة بسيطة:

| أنت تقول | هو يفعل |
|------|------|
| الصق رابط GitHub | تصنيف تلقائي → تثبيت |
| "أرني كتالوج github" | يفتح `CATALOG.md` |
| "ما المهارات التي لدي؟" | يسرد جميع المهارات المثبتة |
| "أي النجوم لم أثبتها بعد؟" | يفحص النجوم → يوصي بما يثبت |
| "ابحث عن أدوات AI" | يبحث عن AI عبر جميع الفئات |
| "سأصنع محتوى Redbook، حمّل المهارة المناسبة" | يجد ويُفعّل المهارات المتعلقة بـ Redbook |

### منطق القرار

| الشرط | الإجراء |
|------|------|
| يحتوي على `SKILL.md` | ✅ موصى به (حزمة مهارة) |
| لديه مدخل CLI (`bin/`، `main.go`، `cli.py`) | ✅ موصى به (أداة/سكريبت) |
| هو خادم MCP / ملحق Claude | ✅ موصى به (ملحق) |
| مكتبة خالصة (`src/` فقط، لا CLI) | ⏭️ تخطي |
| وثائق/درس تعليمي/awesome-list | ⏭️ تخطي |
| مهمل (3+ سنوات بدون تحديث) | ⚠️ علامة تحذير |
| مثبت مسبقًا | 📦 علامة كمثبت |

### خمس فئات وأهداف التثبيت

| الفئة | الدليل | الكشف |
|------|------|------|
| 🧩 مهارة | `~/.claude/skills/` | يحتوي على `SKILL.md` |
| 🔧 أداة | `~/.claude/tools/` | لديه مدخل CLI، `bin/`، `main.go`، `cli.py` |
| 📜 سكريبت | `~/.claude/scripts/` | ملف واحد، `.sh`/`.py`/`.js` |
| 🔌 ملحق | `~/.claude/plugins/` | تنسيق ملحق Claude Code، MCP |
| 📦 برنامج | `~/claude-projects/` | تطبيق كامل أو مشروع مستقل |

### الدعم

(رموز QR للتبرع عبر Alipay / WeChat)

شكرًا لدعمك 🙏

[↑ العودة للأعلى](#)

</div>

---

## 🏷️ 領域標籤 / Domain Tags

| 領域 | Domain | 涵蓋 |
|------|------|------|
| 🤖 AI/自動化 | AI & Automation | n8n、agent、workflow |
| 🏗️ 開發工具 | Dev Tools | CLI、git、devops、建置 |
| 🎨 設計 | Design | UI/UX、logo、banner、配色 |
| ✍️ 內容創作 | Content | 文案、blog、SEO、寫作 |
| 🌐 社媒 | Social Media | 小紅書、微信、Twitter |
| 📊 數據 | Data | 爬蟲、分析、視覺化 |
| 📦 知識管理 | Knowledge Mgmt | Obsidian、筆記、wiki |
| 🎬 視頻/影像 | Video & Image | 剪輯、生成、字幕 |
| 🎵 音頻 | Audio | TTS、音樂、播客 |
| 🖼️ 生圖 | Image Gen | Stable Diffusion、DALL-E |
| 📝 Prompt | Prompt Eng | 提示詞工程 |
| 🔮 玄學 | Esoteric | 八字、占星 |
| 🧩 其他 | Other | 無法歸類 |

## 📜 License

MIT — 隨便用，歡迎 PR。
