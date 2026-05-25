---
title: Cloudflare AI Gateway
source_url: https://docs.openclaw.ai/zh-TW/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway 位於 Provider API 前方，讓你新增分析、快取與控制。對於 Anthropic，OpenClaw 會透過你的 Gateway 端點使用 Anthropic Messages API。

屬性 | 值  
---|---  
Provider | `cloudflare-ai-gateway`  
基礎 URL | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
預設模型 | `cloudflare-ai-gateway/claude-sonnet-4-6`  
API 金鑰 | `CLOUDFLARE_AI_GATEWAY_API_KEY`（你用於透過 Gateway 發出請求的 Provider API 金鑰）  
  
為 Anthropic Messages 模型啟用思考時，OpenClaw 會在透過 Cloudflare AI Gateway 傳送承載資料前，移除尾端的 assistant 預填回合。 Anthropic 會拒絕搭配延伸思考的回應預填，而一般 非思考預填仍可使用。

## 開始使用

* ### 設定 Provider API 金鑰與 Gateway 詳細資料

執行 onboarding 並選擇 Cloudflare AI Gateway 驗證選項：

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

這會提示你輸入帳戶 ID、Gateway ID 與 API 金鑰。

* ### 設定預設模型

將模型新增至你的 OpenClaw 設定：

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### 確認模型可用

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## 非互動式範例

對於指令碼或 CI 設定，請在命令列傳入所有值：

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## 進階設定

已驗證的 Gateway

如果你已在 Cloudflare 啟用 Gateway 驗證，請新增 `cf-aig-authorization` 標頭。這是 **除了** 你的 Provider API 金鑰以外的設定。

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

環境注意事項

如果 Gateway 以 daemon（launchd/systemd）執行，請確認 `CLOUDFLARE_AI_GATEWAY_API_KEY` 可供該程序使用。

## 相關

[**模型選擇** 選擇 Provider、模型 refs 與容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**疑難排解** 一般疑難排解與常見問題。 ](</zh-TW/help/troubleshooting>)

Was this useful?YesNo