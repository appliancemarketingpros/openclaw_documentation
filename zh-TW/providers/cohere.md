---
title: Cohere
source_url: https://docs.openclaw.ai/zh-TW/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) 透過其 Compatibility API 提供與 OpenAI 相容的推論。OpenClaw 在外部化轉換期間隨附 Cohere 提供者，並也將其作為官方外部外掛發布，附帶 Command A 模型目錄。

屬性 | 值  
---|---  
提供者 id | `cohere`  
外掛 | 轉換期間內建；官方外部套件  
驗證環境變數 | `COHERE_API_KEY`  
初始設定旗標 | `--auth-choice cohere-api-key`  
直接命令列介面旗標 | `--cohere-api-key <key>`  
API | 與 OpenAI 相容（`openai-completions`）  
基礎 URL | `https://api.cohere.ai/compatibility/v1`  
預設模型 | `cohere/command-a-03-2025`  
  
## 開始使用

  1. Cohere 已包含在目前的 OpenClaw 套件中。如果無法使用，請安裝外部套件並重新啟動閘道：

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. 建立 Cohere API 金鑰。
  3. 執行初始設定：

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. 確認目錄可用：

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

只有在尚未設定主要模型時，才會設定預設模型。

## 僅使用環境變數設定

讓 `COHERE_API_KEY` 可供閘道程序使用，然後選取 Cohere 模型：

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## 相關

  * [模型提供者](</zh-TW/concepts/model-providers>)
  * [模型命令列介面](</zh-TW/cli/models>)
  * [提供者目錄](</zh-TW/providers>)


Was this useful?YesNo

Open issue