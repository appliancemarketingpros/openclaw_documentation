---
title: StepFun
source_url: https://docs.openclaw.ai/vi/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw bao gồm một Plugin nhà cung cấp StepFun được tích hợp sẵn với hai id nhà cung cấp:

  * `stepfun` cho endpoint tiêu chuẩn
  * `stepfun-plan` cho endpoint Step Plan


## Tổng quan về khu vực và endpoint

Endpoint | Trung Quốc (`.com`) | Toàn cầu (`.ai`)  
---|---|---  
Standard | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
Biến môi trường xác thực: `STEPFUN_API_KEY`

## Catalog tích hợp sẵn

Standard (`stepfun`):

Model ref | Ngữ cảnh | Đầu ra tối đa | Ghi chú  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | Model tiêu chuẩn mặc định  
  
Step Plan (`stepfun-plan`):

Model ref | Ngữ cảnh | Đầu ra tối đa | Ghi chú  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | Model Step Plan mặc định  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | Model Step Plan bổ sung  
  
## Bắt đầu

Chọn bề mặt nhà cung cấp của bạn và làm theo các bước thiết lập.

### Tiêu chuẩn

**Phù hợp nhất cho:** sử dụng đa mục đích thông qua endpoint StepFun tiêu chuẩn.

* ### Chọn khu vực endpoint của bạn

Lựa chọn xác thực | Endpoint | Khu vực  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | Quốc tế  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | Trung Quốc  
* ### Chạy onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

Hoặc cho endpoint Trung Quốc:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### Phương án không tương tác

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Xác minh model có sẵn

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### Model ref

  * Model mặc định: `stepfun/step-3.5-flash`


### Step Plan

**Phù hợp nhất cho:** endpoint suy luận Step Plan.

* ### Chọn khu vực endpoint của bạn

Lựa chọn xác thực | Endpoint | Khu vực  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | Quốc tế  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | Trung Quốc  
* ### Chạy onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

Hoặc cho endpoint Trung Quốc:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### Phương án không tương tác

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Xác minh model có sẵn

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### Model ref

  * Model mặc định: `stepfun-plan/step-3.5-flash`
  * Model thay thế: `stepfun-plan/step-3.5-flash-2603`


## Cấu hình nâng cao

Cấu hình đầy đủ: Nhà cung cấp Standard json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Cấu hình đầy đủ: Nhà cung cấp Step Plan json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Ghi chú

  * Nhà cung cấp này được tích hợp sẵn với OpenClaw, nên không có bước cài đặt Plugin riêng.
  * `step-3.5-flash-2603` hiện chỉ được cung cấp trên `stepfun-plan`.
  * Một luồng xác thực duy nhất ghi các hồ sơ khớp khu vực cho cả `stepfun` và `stepfun-plan`, nên có thể khám phá cả hai bề mặt cùng nhau.
  * Dùng `openclaw models list` và `openclaw models set <provider/model>` để kiểm tra hoặc chuyển đổi model.


## Liên quan

[**Lựa chọn model** Tổng quan về tất cả nhà cung cấp, model ref và hành vi failover. ](</vi/concepts/model-providers>) [**Tham chiếu cấu hình** Schema cấu hình đầy đủ cho nhà cung cấp, model và Plugin. ](</vi/gateway/configuration-reference>) [**Lựa chọn model** Cách chọn và cấu hình model. ](</vi/concepts/models>) [**Nền tảng StepFun** Quản lý khóa API StepFun và tài liệu. ](<https://platform.stepfun.com>)

Was this useful?YesNo