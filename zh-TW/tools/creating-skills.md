---
title: 建立 Skills
source_url: https://docs.openclaw.ai/zh-TW/tools/creating-skills
scraped_at: 2026-05-25
---

Skills 會教導代理如何以及何時使用工具。每個技能都是一個目錄， 其中包含一個 `SKILL.md` 檔案，內含 YAML frontmatter 與 Markdown 指示。

若要了解 Skills 如何載入與排定優先順序，請參閱 [Skills](</zh-TW/tools/skills>)。

## 建立你的第一個技能

* ### 建立技能目錄

Skills 位於你的工作區中。建立新資料夾：

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

* ### 撰寫 SKILL.md

在該目錄中建立 `SKILL.md`。frontmatter 會定義中繼資料， Markdown 主體則包含給代理的指示。

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that says hello.--- # Hello World Skill When the user asks for a greeting, use the `echo` tool to say"Hello from your custom skill!".
[/code]

技能 `name` 請使用由小寫字母、數字與連字號組成的 hyphen-case。 請讓資料夾名稱與 frontmatter `name` 保持一致。

* ### 新增工具（選用）

你可以在 frontmatter 中定義自訂工具結構描述，或指示代理 使用現有的系統工具（例如 `exec` 或 `browser`）。Skills 也可以 隨 Plugin 一起發佈，與其所記錄的工具並列。

* ### 載入技能

啟動新的工作階段，讓 OpenClaw 偵測到該技能：

bashCopy code
[code]
    # From chat/new # Or restart the gatewayopenclaw gateway restart
[/code]

確認技能已載入：

bashCopy code
[code]
    openclaw skills list
[/code]

* ### 測試它

傳送一則應該觸發該技能的訊息：

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

或者直接與代理聊天並要求問候語。

## 技能中繼資料參考

YAML frontmatter 支援下列欄位：

欄位 | 必填 | 說明  
---|---|---  
`name` | 是 | 使用小寫字母、數字與連字號的唯一識別碼  
`description` | 是 | 顯示給代理的一行描述  
`metadata.openclaw.os` | 否 | 作業系統篩選器（`["darwin"]`、`["linux"]` 等）  
`metadata.openclaw.requires.bins` | 否 | PATH 上所需的二進位檔  
`metadata.openclaw.requires.config` | 否 | 必要的設定鍵  
  
## 最佳實務

  * **保持精簡** — 指示模型要做 _什麼_ ，而不是如何當 AI
  * **安全優先** — 如果你的技能使用 `exec`，請確保提示不會允許來自不受信任輸入的任意命令注入
  * **在本機測試** — 分享前先使用 `openclaw agent --message "..."` 測試
  * **使用 ClawHub** — 在 [ClawHub](<https://clawhub.ai>) 瀏覽並貢獻 Skills


## Skills 的位置

位置 | 優先順序 | 範圍  
---|---|---  
`\<workspace\>/skills/` | 最高 | 每個代理  
`\<workspace\>/.agents/skills/` | 高 | 每個工作區代理  
`~/.agents/skills/` | 中 | 共用代理設定檔  
`~/.openclaw/skills/` | 中 | 共用（所有代理）  
Bundled（隨 OpenClaw 發佈） | 低 | 全域  
`skills.load.extraDirs` | 最低 | 自訂共用資料夾  
  
## 相關

  * [Skills 參考](</zh-TW/tools/skills>) — 載入、優先順序與控管規則
  * [Skills 設定](</zh-TW/tools/skills-config>) — `skills.*` 設定結構描述
  * [ClawHub](</zh-TW/clawhub>) — 公開技能登錄檔
  * [建置 Plugin](</zh-TW/plugins/building-plugins>) — Plugin 可以隨附 Skills


Was this useful?YesNo