---
title: Moonshot AI
source_url: https://docs.openclaw.ai/vi/providers/moonshot
scraped_at: 2026-05-25
---

Moonshot cung cấp API Kimi với các điểm cuối tương thích với OpenAI. Cấu hình provider và đặt mô hình mặc định thành `moonshot/kimi-k2.6`, hoặc sử dụng Kimi Coding với `kimi/kimi-for-coding`.

## Danh mục mô hình tích hợp sẵn

Tham chiếu mô hình | Tên | Lập luận | Đầu vào | Ngữ cảnh | Đầu ra tối đa  
---|---|---|---|---|---  
`moonshot/kimi-k2.6` | Kimi K2.6 | Không | văn bản, hình ảnh | 262,144 | 262,144  
`moonshot/kimi-k2.5` | Kimi K2.5 | Không | văn bản, hình ảnh | 262,144 | 262,144  
`moonshot/kimi-k2-thinking` | Kimi K2 Thinking | Có | văn bản | 262,144 | 262,144  
`moonshot/kimi-k2-thinking-turbo` | Kimi K2 Thinking Turbo | Có | văn bản | 262,144 | 262,144  
`moonshot/kimi-k2-turbo` | Kimi K2 Turbo | Không | văn bản | 256,000 | 16,384  
  
Ước tính chi phí đi kèm cho các mô hình K2 hiện tại được lưu trữ trên Moonshot sử dụng mức giá trả theo mức dùng do Moonshot công bố: Kimi K2.6 là $0.16/MTok cho lượt trúng bộ nhớ đệm, $0.95/MTok đầu vào, và $4.00/MTok đầu ra; Kimi K2.5 là $0.10/MTok cho lượt trúng bộ nhớ đệm, $0.60/MTok đầu vào, và $3.00/MTok đầu ra. Các mục danh mục cũ khác giữ placeholder chi phí bằng không trừ khi bạn ghi đè chúng trong cấu hình.

## Bắt đầu

Chọn provider của bạn và làm theo các bước thiết lập.

### Moonshot API

**Phù hợp nhất cho:** các mô hình Kimi K2 qua Moonshot Open Platform.

* ### Chọn vùng điểm cuối của bạn

Lựa chọn xác thực | Điểm cuối | Vùng  
---|---|---  
`moonshot-api-key` | `https://api.moonshot.ai/v1` | Quốc tế  
`moonshot-api-key-cn` | `https://api.moonshot.cn/v1` | Trung Quốc  
* ### Chạy onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key
[/code]

Hoặc cho điểm cuối Trung Quốc:

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key-cn
[/code]

* ### Đặt mô hình mặc định

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },    },  },}
[/code]

* ### Xác minh các mô hình có sẵn

bashCopy code
[code]
    openclaw models list --provider moonshot
[/code]

* ### Chạy kiểm thử khói trực tiếp

Sử dụng thư mục trạng thái cô lập khi bạn muốn xác minh quyền truy cập mô hình và theo dõi chi phí mà không chạm vào các phiên thông thường của bạn:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=/tmp/openclaw-kimi/openclaw.json \OPENCLAW_STATE_DIR=/tmp/openclaw-kimi \openclaw agent --local \  --session-id live-kimi-cost \  --message 'Reply exactly: KIMI_LIVE_OK' \  --thinking off \  --json
[/code]

Phản hồi JSON nên báo cáo `provider: "moonshot"` và `model: "kimi-k2.6"`. Mục bản ghi hội thoại của trợ lý lưu mức sử dụng token đã chuẩn hóa cùng với chi phí ước tính trong `usage.cost` khi Moonshot trả về siêu dữ liệu sử dụng.

### Ví dụ cấu hình

json5Copy code
[code]
    {  env: { MOONSHOT_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },      models: {        // moonshot-kimi-k2-aliases:start        "moonshot/kimi-k2.6": { alias: "Kimi K2.6" },        "moonshot/kimi-k2.5": { alias: "Kimi K2.5" },        "moonshot/kimi-k2-thinking": { alias: "Kimi K2 Thinking" },        "moonshot/kimi-k2-thinking-turbo": { alias: "Kimi K2 Thinking Turbo" },        "moonshot/kimi-k2-turbo": { alias: "Kimi K2 Turbo" },        // moonshot-kimi-k2-aliases:end      },    },  },  models: {    mode: "merge",    providers: {      moonshot: {        baseUrl: "https://api.moonshot.ai/v1",        apiKey: "${MOONSHOT_API_KEY}",        api: "openai-completions",        models: [          // moonshot-kimi-k2-models:start          {            id: "kimi-k2.6",            name: "Kimi K2.6",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.95, output: 4, cacheRead: 0.16, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2.5",            name: "Kimi K2.5",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.6, output: 3, cacheRead: 0.1, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking",            name: "Kimi K2 Thinking",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking-turbo",            name: "Kimi K2 Thinking Turbo",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-turbo",            name: "Kimi K2 Turbo",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 16384,          },          // moonshot-kimi-k2-models:end        ],      },    },  },}
[/code]

### Kimi Coding

**Phù hợp nhất cho:** các tác vụ tập trung vào mã qua điểm cuối Kimi Coding.

* ### Chạy onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kimi-code-api-key
[/code]

* ### Đặt mô hình mặc định

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },    },  },}
[/code]

* ### Xác minh mô hình có sẵn

bashCopy code
[code]
    openclaw models list --provider kimi
[/code]

### Ví dụ cấu hình

json5Copy code
[code]
    {  env: { KIMI_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },      models: {        "kimi/kimi-for-coding": { alias: "Kimi" },      },    },  },}
[/code]

## Tìm kiếm web Kimi

OpenClaw cũng cung cấp **Kimi** dưới dạng nhà cung cấp `web_search`, được hỗ trợ bởi tìm kiếm web của Moonshot.

* ### Chạy thiết lập tìm kiếm web tương tác

bashCopy code
[code]
    openclaw configure --section web
[/code]

Chọn **Kimi** trong phần tìm kiếm web để lưu `plugins.entries.moonshot.config.webSearch.*`.

* ### Cấu hình vùng và mô hình tìm kiếm web

Thiết lập tương tác sẽ nhắc nhập:

Cài đặt | Tùy chọn  
---|---  
Vùng API | `https://api.moonshot.ai/v1` (quốc tế) hoặc `https://api.moonshot.cn/v1` (Trung Quốc)  
Mô hình tìm kiếm web | Mặc định là `kimi-k2.6`  
  
Cấu hình nằm trong `plugins.entries.moonshot.config.webSearch`:

json5Copy code
[code]
    {  plugins: {    entries: {      moonshot: {        config: {          webSearch: {            apiKey: "sk-...", // or use KIMI_API_KEY / MOONSHOT_API_KEY            baseUrl: "https://api.moonshot.ai/v1",            model: "kimi-k2.6",          },        },      },    },  },  tools: {    web: {      search: {        provider: "kimi",      },    },  },}
[/code]

## Cấu hình nâng cao

Chế độ suy nghĩ gốc

Moonshot Kimi hỗ trợ chế độ suy nghĩ gốc nhị phân:

  * `thinking: { type: "enabled" }`
  * `thinking: { type: "disabled" }`


Cấu hình theo từng mô hình qua `agents.defaults.models.<provider/model>.params`:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "disabled" },          },        },      },    },  },}
[/code]

OpenClaw cũng ánh xạ các mức `/think` trong thời gian chạy cho Moonshot:

Mức `/think` | Hành vi của Moonshot  
---|---  
`/think off` | `thinking.type=disabled`  
Bất kỳ mức nào không phải off | `thinking.type=enabled`  
  
Kimi K2.6 cũng chấp nhận trường `thinking.keep` tùy chọn, trường này kiểm soát việc giữ lại `reasoning_content` qua nhiều lượt. Đặt thành `"all"` để giữ toàn bộ phần lập luận qua các lượt; bỏ qua trường này (hoặc để là `null`) để dùng chiến lược mặc định của máy chủ. OpenClaw chỉ chuyển tiếp `thinking.keep` cho `moonshot/kimi-k2.6` và loại bỏ nó khỏi các mô hình khác.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "enabled", keep: "all" },          },        },      },    },  },}
[/code]

Tool call id sanitization

Moonshot Kimi cung cấp các id tool_call có dạng `functions.<name>:<index>`. OpenClaw giữ nguyên chúng không thay đổi để các lệnh gọi công cụ nhiều lượt tiếp tục hoạt động.

Để buộc làm sạch nghiêm ngặt trên một nhà cung cấp tùy chỉnh tương thích với OpenAI, hãy đặt `sanitizeToolCallIds: true`:

json5Copy code
[code]
    {  models: {    providers: {      "my-kimi-proxy": {        api: "openai-completions",        sanitizeToolCallIds: true,      },    },  },}
[/code]

Streaming usage compatibility

Các endpoint Moonshot gốc (`https://api.moonshot.ai/v1` và `https://api.moonshot.cn/v1`) công bố khả năng tương thích sử dụng khi truyền trực tuyến trên phương thức truyền tải `openai-completions` dùng chung. OpenClaw xác định điều đó dựa trên năng lực của endpoint, vì vậy các id nhà cung cấp tùy chỉnh tương thích nhắm tới cùng các máy chủ Moonshot gốc sẽ kế thừa cùng hành vi sử dụng khi truyền trực tuyến.

Với mức giá K2.6 được tích hợp sẵn, dữ liệu sử dụng được truyền trực tuyến bao gồm token đầu vào, đầu ra và đọc từ bộ nhớ đệm cũng được chuyển đổi thành chi phí USD ước tính cục bộ cho `/status`, `/usage full`, `/usage cost` và kế toán phiên dựa trên bản ghi hội thoại.

Tham chiếu điểm cuối và tham chiếu mô hình Nhà cung cấp | Tiền tố tham chiếu mô hình | Điểm cuối | Biến môi trường xác thực  
---|---|---|---  
Moonshot | `moonshot/` | `https://api.moonshot.ai/v1` | `MOONSHOT_API_KEY`  
Moonshot CN | `moonshot/` | `https://api.moonshot.cn/v1` | `MOONSHOT_API_KEY`  
Kimi Coding | `kimi/` | Điểm cuối Kimi Coding | `KIMI_API_KEY`  
Tìm kiếm web | N/A | Giống vùng Moonshot API | `KIMI_API_KEY` hoặc `MOONSHOT_API_KEY`  
  
  * Tìm kiếm web Kimi sử dụng `KIMI_API_KEY` hoặc `MOONSHOT_API_KEY`, và mặc định là `https://api.moonshot.ai/v1` với mô hình `kimi-k2.6`.
  * Ghi đè giá và siêu dữ liệu ngữ cảnh trong `models.providers` nếu cần.
  * Nếu Moonshot công bố giới hạn ngữ cảnh khác cho một mô hình, hãy điều chỉnh `contextWindow` cho phù hợp.


## Liên quan

[**Lựa chọn mô hình** Chọn nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Tìm kiếm web** Cấu hình nhà cung cấp tìm kiếm web, bao gồm Kimi. ](</vi/tools/web>) [**Tham chiếu cấu hình** Lược đồ cấu hình đầy đủ cho nhà cung cấp, mô hình và Plugin. ](</vi/gateway/configuration-reference>) [**Moonshot Open Platform** Quản lý khóa Moonshot API và tài liệu. ](<https://platform.moonshot.ai>)

Was this useful?YesNo