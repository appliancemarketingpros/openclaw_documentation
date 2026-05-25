---
title: SGLang
source_url: https://docs.openclaw.ai/vi/providers/sglang
scraped_at: 2026-05-25
---

SGLang phục vụ các mô hình trọng số mở qua API HTTP tương thích OpenAI. OpenClaw kết nối với SGLang bằng nhóm nhà cung cấp `openai-completions` với khả năng tự động phát hiện các mô hình hiện có.

Thuộc tính | Giá trị  
---|---  
ID nhà cung cấp | `sglang`  
Plugin | được tích hợp sẵn, `enabledByDefault: true`  
Biến môi trường xác thực | `SGLANG_API_KEY` (bất kỳ giá trị không rỗng nào nếu máy chủ không có xác thực)  
Cờ onboarding | `--auth-choice sglang`  
API | tương thích OpenAI (`openai-completions`)  
URL cơ sở mặc định | `http://127.0.0.1:30000/v1`  
Trình giữ chỗ mô hình mặc định | `sglang/Qwen/Qwen3-8B`  
Mức sử dụng streaming | Có (`supportsStreamingUsage: true`)  
Giá | Được đánh dấu là miễn phí bên ngoài (`modelPricing.external: false`)  
  
OpenClaw cũng **tự động phát hiện** các mô hình hiện có từ SGLang khi bạn chọn tham gia bằng `SGLANG_API_KEY`. Dùng `sglang/*` trong `agents.defaults.models` để giữ việc phát hiện ở trạng thái động khi bạn cũng cấu hình URL cơ sở SGLang tùy chỉnh. Xem Phát hiện mô hình (nhà cung cấp ngầm định) bên dưới.

## Bắt đầu

* ### Start SGLang

Khởi chạy SGLang với một máy chủ tương thích OpenAI. URL cơ sở của bạn phải cung cấp các endpoint `/v1` (ví dụ `/v1/models`, `/v1/chat/completions`). SGLang thường chạy trên:

  * `http://127.0.0.1:30000/v1`


* ### Set an API key

Bất kỳ giá trị nào cũng hoạt động nếu máy chủ của bạn không cấu hình xác thực:

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### Run onboarding or set a model directly

bashCopy code
[code]
    openclaw onboard
[/code]

Hoặc cấu hình mô hình thủ công:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## Phát hiện mô hình (nhà cung cấp ngầm định)

Khi `SGLANG_API_KEY` được đặt (hoặc tồn tại hồ sơ xác thực) và bạn **không** định nghĩa `models.providers.sglang`, OpenClaw sẽ truy vấn:

  * `GET http://127.0.0.1:30000/v1/models`


và chuyển đổi các ID được trả về thành các mục mô hình.

## Cấu hình tường minh (mô hình thủ công)

Dùng cấu hình tường minh khi:

  * SGLang chạy trên host/cổng khác.
  * Bạn muốn ghim các giá trị `contextWindow`/`maxTokens`.
  * Máy chủ của bạn yêu cầu khóa API thật (hoặc bạn muốn kiểm soát header).

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Cấu hình nâng cao

Proxy-style behavior

SGLang được xử lý như một backend `/v1` tương thích OpenAI kiểu proxy, không phải một endpoint OpenAI gốc.

Hành vi | SGLang  
---|---  
Định hình yêu cầu chỉ dành cho OpenAI | Không áp dụng  
`service_tier`, Responses `store`, gợi ý prompt-cache | Không gửi  
Định hình payload tương thích reasoning | Không áp dụng  
Header quy thuộc ẩn (`originator`, `version`, `User-Agent`) | Không chèn trên các URL cơ sở SGLang tùy chỉnh  
Troubleshooting

**Không thể kết nối máy chủ**

Xác minh máy chủ đang chạy và phản hồi:

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**Lỗi xác thực**

Nếu yêu cầu thất bại do lỗi xác thực, hãy đặt một `SGLANG_API_KEY` thật khớp với cấu hình máy chủ của bạn, hoặc cấu hình nhà cung cấp một cách tường minh trong `models.providers.sglang`.

## Liên quan

[**Model selection** Chọn nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Configuration reference** Lược đồ cấu hình đầy đủ bao gồm các mục nhà cung cấp. ](</vi/gateway/configuration-reference>)

Was this useful?YesNo