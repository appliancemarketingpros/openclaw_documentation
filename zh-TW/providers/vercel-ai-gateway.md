---
title: Vercel AI Gateway
source_url: https://docs.openclaw.ai/zh-TW/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

[Vercel AI Gateway](<https://vercel.com/ai-gateway>) 提供統一的 API，可透過單一端點 存取數百種模型。

屬性 | 值  
---|---  
提供者 | `vercel-ai-gateway`  
驗證 | `AI_GATEWAY_API_KEY`  
API | 與 Anthropic Messages 相容  
模型目錄 | 透過 `/v1/models` 自動探索  
  
## 開始使用

* ### 設定 API 金鑰

執行 onboarding，並選擇 AI Gateway 驗證選項：

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### 設定預設模型

將模型加入你的 OpenClaw 設定：

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### 確認模型可用

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## 非互動式範例

對於指令碼或 CI 設定，請在命令列傳入所有值：

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## 模型 ID 簡寫

OpenClaw 接受 Vercel Claude 簡寫模型參照，並會在執行階段將其正規化：

簡寫輸入 | 正規化模型參照  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## 進階設定

daemon 程序的環境變數

如果 OpenClaw Gateway 以 daemon（launchd/systemd）執行，請確保 `AI_GATEWAY_API_KEY` 可供該程序使用。

提供者路由

Vercel AI Gateway 會根據模型參照前綴，將請求路由至上游提供者。例如，`vercel-ai-gateway/anthropic/claude-opus-4.6` 會透過 Anthropic 路由， 而 `vercel-ai-gateway/openai/gpt-5.5` 會透過 OpenAI 路由，`vercel-ai-gateway/moonshotai/kimi-k2.6` 則透過 MoonshotAI 路由。你的單一 `AI_GATEWAY_API_KEY` 會處理所有 上游提供者的驗證。

思考等級

當 OpenClaw 知道上游提供者合約時，`/think` 選項會遵循可信任的上游模型前綴。`vercel-ai-gateway/anthropic/...` 會使用 Claude 思考設定檔，包括 Claude 4.6 模型的自適應預設值。 `vercel-ai-gateway/openai/gpt-5.4`、`gpt-5.5` 和 Codex 風格的參照會公開 `/think xhigh`，就像直接的 OpenAI/OpenAI Codex 提供者一樣。其他 命名空間參照會保留一般 reasoning 等級，除非其目錄 中繼資料宣告更多內容。

## 相關

[**模型選擇** 選擇提供者、模型參照和容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**疑難排解** 一般疑難排解與常見問題。 ](</zh-TW/help/troubleshooting>)

Was this useful?YesNo