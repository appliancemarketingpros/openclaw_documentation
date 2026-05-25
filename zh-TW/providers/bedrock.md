---
title: Amazon Bedrock
source_url: https://docs.openclaw.ai/zh-TW/providers/bedrock
scraped_at: 2026-05-25
---

OpenClaw 可以透過 pi-ai 的 **Bedrock Converse** 串流提供者使用 **Amazon Bedrock** 模型。Bedrock 驗證使用 **AWS SDK 預設憑證鏈** ， 而不是 API 金鑰。

屬性 | 值  
---|---  
提供者 | `amazon-bedrock`  
API | `bedrock-converse-stream`  
驗證 | AWS 憑證（環境變數、共享設定或執行個體角色）  
區域 | `AWS_REGION` 或 `AWS_DEFAULT_REGION`（預設：`us-east-1`）  
  
## 開始使用

選擇你偏好的驗證方法，並依照設定步驟操作。

### 存取金鑰 / 環境變數

**最適合：** 開發者機器、CI，或你直接管理 AWS 憑證的主機。

* ### 在 Gateway 主機上設定 AWS 憑證

bashCopy code
[code]
    export AWS_ACCESS_KEY_ID="AKIA..."export AWS_SECRET_ACCESS_KEY="..."export AWS_REGION="us-east-1"# Optional:export AWS_SESSION_TOKEN="..."export AWS_PROFILE="your-profile"# Optional (Bedrock API key/bearer token):export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

* ### 將 Bedrock 提供者與模型新增到你的設定

不需要 `apiKey`。使用 `auth: "aws-sdk"` 設定提供者：

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock": {        baseUrl: "https://bedrock-runtime.us-east-1.amazonaws.com",        api: "bedrock-converse-stream",        auth: "aws-sdk",        models: [          {            id: "us.anthropic.claude-opus-4-6-v1:0",            name: "Claude Opus 4.6 (Bedrock)",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 200000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "amazon-bedrock/us.anthropic.claude-opus-4-6-v1:0" },    },  },}
[/code]

* ### 確認模型可用

bashCopy code
[code]
    openclaw models list
[/code]

### EC2 執行個體角色 (IMDS)

**最適合：** 已附加 IAM 角色，並使用執行個體中繼資料服務進行驗證的 EC2 執行個體。

* ### 明確啟用探索

使用 IMDS 時，OpenClaw 無法只從環境標記偵測 AWS 驗證，因此你必須選擇啟用：

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1
[/code]

* ### 可選擇新增環境標記以用於自動模式

如果你也希望環境標記自動偵測路徑可運作（例如用於 `openclaw status` 介面）：

bashCopy code
[code]
    export AWS_PROFILE=defaultexport AWS_REGION=us-east-1
[/code]

你**不** 需要假的 API 金鑰。

* ### 確認模型已被探索

bashCopy code
[code]
    openclaw models list
[/code]

## 自動模型探索

OpenClaw 可以自動探索支援**串流** 與**文字輸出** 的 Bedrock 模型。探索會使用 `bedrock:ListFoundationModels` 與 `bedrock:ListInferenceProfiles`，且結果會快取（預設：1 小時）。

隱含提供者的啟用方式：

  * 如果 `plugins.entries.amazon-bedrock.config.discovery.enabled` 是 `true`， 即使沒有 AWS 環境標記，OpenClaw 也會嘗試探索。
  * 如果未設定 `plugins.entries.amazon-bedrock.config.discovery.enabled`， OpenClaw 只有在看到以下其中一個 AWS 驗證標記時，才會自動新增 隱含的 Bedrock 提供者： `AWS_BEARER_TOKEN_BEDROCK`、`AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`，或 `AWS_PROFILE`。
  * 實際的 Bedrock 執行階段驗證路徑仍使用 AWS SDK 預設鏈，因此 共享設定、SSO 與 IMDS 執行個體角色驗證可以運作，即使探索 需要 `enabled: true` 才能選擇啟用。


探索設定選項

設定選項位於 `plugins.entries.amazon-bedrock.config.discovery` 底下：

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          discovery: {            enabled: true,            region: "us-east-1",            providerFilter: ["anthropic", "amazon"],            refreshInterval: 3600,            defaultContextWindow: 32000,            defaultMaxTokens: 4096,          },        },      },    },  },}
[/code]

選項 | 預設 | 說明  
---|---|---  
`enabled` | auto | 在自動模式中，OpenClaw 只有在看到支援的 AWS 環境標記時，才會啟用隱含的 Bedrock 提供者。設定為 `true` 可強制探索。  
`region` | `AWS_REGION` / `AWS_DEFAULT_REGION` / `us-east-1` | 用於探索 API 呼叫的 AWS 區域。  
`providerFilter` | （全部） | 符合 Bedrock 提供者名稱（例如 `anthropic`、`amazon`）。  
`refreshInterval` | `3600` | 快取持續時間，以秒為單位。設定為 `0` 可停用快取。  
`defaultContextWindow` | `32000` | 用於已探索模型的上下文視窗（如果你知道模型限制，可覆寫）。  
`defaultMaxTokens` | `4096` | 用於已探索模型的最大輸出權杖數（如果你知道模型限制，可覆寫）。  
  
## 快速設定（AWS 路徑）

此逐步說明會建立 IAM 角色、附加 Bedrock 權限、關聯 執行個體設定檔，並在 EC2 主機上啟用 OpenClaw 探索。

bashCopy code
[code]
    # 1. Create IAM role and instance profileaws iam create-role --role-name EC2-Bedrock-Access \  --assume-role-policy-document '{    "Version": "2012-10-17",    "Statement": [{      "Effect": "Allow",      "Principal": {"Service": "ec2.amazonaws.com"},      "Action": "sts:AssumeRole"    }]  }' aws iam attach-role-policy --role-name EC2-Bedrock-Access \  --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess aws iam create-instance-profile --instance-profile-name EC2-Bedrock-Accessaws iam add-role-to-instance-profile \  --instance-profile-name EC2-Bedrock-Access \  --role-name EC2-Bedrock-Access # 2. Attach to your EC2 instanceaws ec2 associate-iam-instance-profile \  --instance-id i-xxxxx \  --iam-instance-profile Name=EC2-Bedrock-Access # 3. On the EC2 instance, enable discovery explicitlyopenclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1 # 4. Optional: add an env marker if you want auto mode without explicit enableecho 'export AWS_PROFILE=default' >> ~/.bashrcecho 'export AWS_REGION=us-east-1' >> ~/.bashrcsource ~/.bashrc # 5. Verify models are discoveredopenclaw models list
[/code]

## 進階設定

推論設定檔

OpenClaw 會在基礎模型旁同時探索**區域與全域推論設定檔** 。 當設定檔對應到已知的基礎模型時，該設定檔會繼承該模型的能力 （上下文視窗、最大權杖數、推理、視覺），且正確的 Bedrock 請求區域會自動注入。 這表示跨區域 Claude 設定檔不需要手動 覆寫提供者即可運作。

推論設定檔 ID 類似 `us.anthropic.claude-opus-4-6-v1:0`（區域） 或 `anthropic.claude-opus-4-6-v1:0`（全域）。如果後端模型已經 在探索結果中，該設定檔會繼承其完整能力集合； 否則會套用安全預設值。

不需要額外設定。只要探索已啟用，且 IAM 主體具有 `bedrock:ListInferenceProfiles`，設定檔就會與 基礎模型一起出現在 `openclaw models list` 中。

服務層級

部分 Bedrock 模型支援 `service_tier` 參數，以針對成本 或延遲進行最佳化。可用的層級如下：

層級 | 說明  
---|---  
`default` | 標準 Bedrock 層級  
`flex` | 適用於可容忍較長延遲之工作負載的折扣處理  
`priority` | 適用於延遲敏感工作負載的優先處理  
`reserved` | 適用於穩定狀態工作負載的保留容量  
  
透過 `agents.defaults.params` 為 Bedrock 模型請求設定 `serviceTier`（或 `service_tier`），或在 `agents.defaults.models["<model-key>"].params` 中針對每個模型設定：

json5Copy code
[code]
    {  agents: {    defaults: {      params: {        serviceTier: "flex", // applies to all models      },      models: {        "amazon-bedrock/mistral.mistral-large-3-675b-instruct": {          params: {            serviceTier: "priority", // per-model override          },        },      },    },  },}
[/code]

有效值為 `default`、`flex`、`priority` 與 `reserved`。並非所有 模型都支援所有層級，如果請求不支援的層級，Bedrock 會 回傳驗證錯誤。注意：錯誤訊息有些誤導； 它可能會說「The provided model identifier is invalid」，而不是指出 不支援的服務層級。如果你看到此錯誤，請檢查該模型 是否支援請求的層級。

Claude Opus 4.7 溫度

Bedrock 會拒絕 Claude Opus 4.7 的 `temperature` 參數。OpenClaw 會自動為任何 Opus 4.7 Bedrock 參照略過 `temperature`，包括 基礎模型 ID、具名推論設定檔、底層模型透過 `bedrock:GetInferenceProfile` 解析為 Opus 4.7 的應用程式推論 設定檔，以及帶有可選區域前綴（`us.`、`eu.`、`ap.`、`apac.`、`au.`、`jp.`、 `global.`）的點分 `opus-4.7` 變體。不需要設定旋鈕，且此略過會同時套用於 請求選項物件與 `inferenceConfig` 酬載欄位。

Guardrails

你可以將 [Amazon Bedrock Guardrails](<https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>) 套用到所有 Bedrock 模型叫用，方法是在 `amazon-bedrock` Plugin 設定中加入 `guardrail` 物件。Guardrails 可讓你強制執行內容篩選、 主題拒絕、字詞篩選、敏感資訊篩選，以及情境 grounding 檢查。

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          guardrail: {            guardrailIdentifier: "abc123", // guardrail ID or full ARN            guardrailVersion: "1", // version number or "DRAFT"            streamProcessingMode: "sync", // optional: "sync" or "async"            trace: "enabled", // optional: "enabled", "disabled", or "enabled_full"          },        },      },    },  },}
[/code]

選項 | 必填 | 說明  
---|---|---  
`guardrailIdentifier` | 是 | Guardrail ID（例如 `abc123`）或完整 ARN（例如 `arn:aws:bedrock:us-east-1:123456789012:guardrail/abc123`）。  
`guardrailVersion` | 是 | 已發布的版本號碼，或用於工作草稿的 `"DRAFT"`。  
`streamProcessingMode` | 否 | 串流期間進行 guardrail 評估時使用 `"sync"` 或 `"async"`。如果省略，Bedrock 會使用其預設值。  
`trace` | 否 | 用於偵錯的 `"enabled"` 或 `"enabled_full"`；正式環境請省略或設為 `"disabled"`。  
Embeddings for memory search

Bedrock 也可以作為 [記憶體搜尋](</zh-TW/concepts/memory-search>)的嵌入提供者。這會與推論提供者分開設定，請將 `agents.defaults.memorySearch.provider` 設為 `"bedrock"`：

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0", // default      },    },  },}
[/code]

Bedrock 嵌入會使用與推論相同的 AWS SDK 憑證鏈（執行個體 角色、SSO、存取金鑰、共用設定，以及 Web 身分）。不需要 API 金鑰。 當 `provider` 為 `"auto"` 時，如果該憑證鏈成功解析， Bedrock 會被自動偵測。

支援的嵌入模型包括 Amazon Titan Embed（v1、v2）、Amazon Nova Embed、Cohere Embed（v3、v4）和 TwelveLabs Marengo。完整模型清單與維度選項請參閱 [記憶體設定參考 -- Bedrock](</zh-TW/reference/memory-config#bedrock-embedding-config>)。

Notes and caveats

  * Bedrock 需要在你的 AWS 帳戶/區域啟用**模型存取權** 。
  * 自動探索需要 `bedrock:ListFoundationModels` 和 `bedrock:ListInferenceProfiles` 權限。
  * 如果你依賴自動模式，請在 Gateway 主機上設定其中一個受支援的 AWS 驗證環境標記。如果你偏好沒有環境標記的 IMDS/共用設定驗證，請設定 `plugins.entries.amazon-bedrock.config.discovery.enabled: true`。
  * OpenClaw 會依照以下順序呈現憑證來源：`AWS_BEARER_TOKEN_BEDROCK`， 接著是 `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`，再來是 `AWS_PROFILE`，最後是 預設 AWS SDK 鏈。
  * 推理支援取決於模型；請查看 Bedrock 模型卡以了解 目前功能。
  * 如果你偏好受管理的金鑰流程，也可以在 Bedrock 前方放置 OpenAI 相容 代理，並改將其設定為 OpenAI 提供者。


## 相關

[**Model selection** 選擇提供者、模型參照，以及容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**Memory search** 用於記憶體搜尋設定的 Bedrock 嵌入。 ](</zh-TW/concepts/memory-search>) [**Memory config reference** 完整的 Bedrock 嵌入模型清單與維度選項。 ](</zh-TW/reference/memory-config#bedrock-embedding-config>) [**Troubleshooting** 一般疑難排解與常見問題。 ](</zh-TW/help/troubleshooting>)

Was this useful?YesNo