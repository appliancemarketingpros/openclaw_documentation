---
title: CLI 自動化
source_url: https://docs.openclaw.ai/zh-TW/start/wizard-cli-automation
scraped_at: 2026-05-25
---

使用 `--non-interactive` 來自動化 `openclaw onboard`。

## 基準非互動範例

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --secret-input-mode plaintext \  --gateway-port 18789 \  --gateway-bind loopback \  --install-daemon \  --daemon-runtime node \  --skip-bootstrap \  --skip-skills
[/code]

加入 `--json` 可取得機器可讀的摘要。

當你的自動化流程已預先植入工作區檔案，且不希望上線流程建立預設啟動檔案時，請使用 `--skip-bootstrap`。

使用 `--secret-input-mode ref` 可在驗證設定檔中儲存由環境支援的參照，而不是明文值。 上線流程中可互動選擇環境參照與已設定的提供者參照（`file` 或 `exec`）。

在非互動 `ref` 模式中，提供者環境變數必須設定在程序環境中。 如果傳入內嵌金鑰旗標但沒有相符的環境變數，現在會快速失敗。

範例：

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

## 提供者特定範例

Anthropic API 金鑰範例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Gemini 範例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Z.AI 範例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice zai-api-key \  --zai-api-key "$ZAI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Vercel AI Gateway 範例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Cloudflare AI Gateway 範例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Moonshot 範例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice moonshot-api-key \  --moonshot-api-key "$MOONSHOT_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Mistral 範例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Synthetic 範例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice synthetic-api-key \  --synthetic-api-key "$SYNTHETIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

OpenCode 範例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice opencode-zen \  --opencode-zen-api-key "$OPENCODE_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

若要使用 Go 目錄，請改用 `--auth-choice opencode-go --opencode-go-api-key "$OPENCODE_API_KEY"`。

Ollama 範例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ollama \  --custom-model-id "qwen3.5:27b" \  --accept-risk \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

自訂提供者範例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

`--custom-api-key` 是選用的。如果省略，上線流程會檢查 `CUSTOM_API_KEY`。 OpenClaw 會自動將常見的視覺模型 ID 標記為支援圖片。對於未知的自訂視覺 ID，請加入 `--custom-image-input`；或加入 `--custom-text-input` 來強制使用僅文字中繼資料。

參照模式變體：

bashCopy code
[code]
    export CUSTOM_API_KEY="your-key"openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --secret-input-mode ref \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

在此模式中，上線流程會將 `apiKey` 儲存為 `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`。

Anthropic setup-token 仍可作為受支援的上線權杖路徑使用，但 OpenClaw 現在會在可用時優先重用 Claude CLI。 在生產環境中，建議使用 Anthropic API 金鑰。

## 新增另一個代理

使用 `openclaw agents add <name>` 建立一個獨立代理，並擁有自己的工作區、 工作階段和驗證設定檔。不使用 `--workspace` 執行會啟動精靈。

bashCopy code
[code]
    openclaw agents add work \  --workspace ~/.openclaw/workspace-work \  --model openai/gpt-5.5 \  --bind whatsapp:biz \  --non-interactive \  --json
[/code]

它會設定：

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


注意事項：

  * 預設工作區遵循 `~/.openclaw/workspace-<agentId>`。
  * 加入 `bindings` 可路由傳入訊息（精靈也可以執行此操作）。
  * 非互動旗標：`--model`、`--agent-dir`、`--bind`、`--non-interactive`。


## 相關文件

  * 上線中心：[上線（CLI）](</zh-TW/start/wizard>)
  * 完整參考：[CLI 設定參考](</zh-TW/start/wizard-cli-reference>)
  * 指令參考：[`openclaw onboard`](</zh-TW/cli/onboard>)


Was this useful?YesNo