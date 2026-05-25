---
title: Mistral
source_url: https://docs.openclaw.ai/vi/providers/mistral
scraped_at: 2026-05-25
---

OpenClaw bao gồm một Plugin Mistral được đóng gói sẵn, đăng ký bốn hợp đồng: hoàn tất trò chuyện, hiểu phương tiện (phiên âm hàng loạt Voxtral), STT thời gian thực cho Cuộc gọi thoại (Voxtral Realtime), và embedding bộ nhớ (`mistral-embed`).

Thuộc tính | Giá trị  
---|---  
ID nhà cung cấp | `mistral`  
Plugin | được đóng gói sẵn, `enabledByDefault: true`  
Biến môi trường xác thực | `MISTRAL_API_KEY`  
Cờ onboarding | `--auth-choice mistral-api-key`  
Cờ CLI trực tiếp | `--mistral-api-key <key>`  
API | tương thích OpenAI (`openai-completions`)  
URL cơ sở | `https://api.mistral.ai/v1`  
Mô hình mặc định | `mistral/mistral-large-latest`  
Mô hình embedding | `mistral-embed`  
Voxtral hàng loạt | `voxtral-mini-latest` (phiên âm âm thanh)  
Voxtral thời gian thực | `voxtral-mini-transcribe-realtime-2602`  
  
## Bắt đầu

* ### Lấy khóa API của bạn

Tạo khóa API trong [Mistral Console](<https://console.mistral.ai/>).

* ### Chạy onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice mistral-api-key
[/code]

Hoặc truyền khóa trực tiếp:

bashCopy code
[code]
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
[/code]

* ### Đặt mô hình mặc định

json5Copy code
[code]
    {  env: { MISTRAL_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },}
[/code]

* ### Xác minh mô hình có sẵn

bashCopy code
[code]
    openclaw models list --provider mistral
[/code]

## Danh mục LLM tích hợp

[Mistral Medium 3.5](<https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04>) là mô hình Medium kết hợp hiện tại trong danh mục được đóng gói sẵn: 128B trọng số dense, đầu vào văn bản và hình ảnh, ngữ cảnh 256K, gọi hàm, đầu ra có cấu trúc, lập trình, và reasoning có thể điều chỉnh thông qua Chat Completions API. Dùng `mistral/mistral-medium-3-5` khi bạn muốn mô hình tác nhân/lập trình hợp nhất mới hơn của Mistral thay vì mặc định `mistral/mistral-large-latest`.

OpenClaw hiện phát hành danh mục Mistral được đóng gói sẵn này:

Tham chiếu mô hình | Đầu vào | Ngữ cảnh | Đầu ra tối đa | Ghi chú  
---|---|---|---|---  
`mistral/mistral-large-latest` | văn bản, hình ảnh | 262,144 | 16,384 | Mô hình mặc định  
`mistral/mistral-medium-2508` | văn bản, hình ảnh | 262,144 | 8,192 | Mistral Medium 3.1  
`mistral/mistral-medium-3-5` | văn bản, hình ảnh | 262,144 | 8,192 | Mistral Medium 3.5; reasoning có thể điều chỉnh  
`mistral/mistral-small-latest` | văn bản, hình ảnh | 128,000 | 16,384 | Mistral Small 4; reasoning có thể điều chỉnh qua API `reasoning_effort`  
`mistral/pixtral-large-latest` | văn bản, hình ảnh | 128,000 | 32,768 | Pixtral  
`mistral/codestral-latest` | văn bản | 256,000 | 4,096 | Lập trình  
`mistral/devstral-medium-latest` | văn bản | 262,144 | 32,768 | Devstral 2  
`mistral/magistral-small` | văn bản | 128,000 | 40,000 | Có bật reasoning  
  
Sau khi onboarding, hãy smoke-test Medium 3.5 mà không khởi động Gateway:

bashCopy code
[code]
    openclaw infer model run --local \  --model mistral/mistral-medium-3-5 \  --prompt "Reply with exactly: mistral-ok" \  --json
[/code]

Để duyệt hàng trong danh mục được đóng gói sẵn trước khi thay đổi cấu hình:

bashCopy code
[code]
    openclaw models list --all --provider mistral --plain
[/code]

## Phiên âm âm thanh (Voxtral)

Dùng Voxtral để phiên âm âm thanh hàng loạt thông qua pipeline hiểu phương tiện.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "mistral", model: "voxtral-mini-latest" }],      },    },  },}
[/code]

## STT phát trực tuyến cho Cuộc gọi thoại

Plugin `mistral` được đóng gói sẵn đăng ký Voxtral Realtime làm nhà cung cấp STT phát trực tuyến cho Cuộc gọi thoại.

Cài đặt | Đường dẫn cấu hình | Mặc định  
---|---|---  
Khóa API | `plugins.entries.voice-call.config.streaming.providers.mistral.apiKey` | Dự phòng về `MISTRAL_API_KEY`  
Mô hình | `...mistral.model` | `voxtral-mini-transcribe-realtime-2602`  
Mã hóa | `...mistral.encoding` | `pcm_mulaw`  
Tốc độ lấy mẫu | `...mistral.sampleRate` | `8000`  
Độ trễ mục tiêu | `...mistral.targetStreamingDelayMs` | `800`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "mistral",            providers: {              mistral: {                apiKey: "${MISTRAL_API_KEY}",                targetStreamingDelayMs: 800,              },            },          },        },      },    },  },}
[/code]

## Cấu hình nâng cao

Reasoning có thể điều chỉnh

`mistral/mistral-small-latest` (Mistral Small 4) và `mistral/mistral-medium-3-5` hỗ trợ [reasoning có thể điều chỉnh](<https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable>) trên Chat Completions API qua `reasoning_effort` (`none` giảm thiểu phần suy nghĩ bổ sung trong đầu ra; `high` hiển thị đầy đủ dấu vết suy nghĩ trước câu trả lời cuối cùng). Mistral khuyến nghị `reasoning_effort="high"` cho các trường hợp dùng tác nhân và mã của Medium 3.5.

OpenClaw ánh xạ mức **thinking** của phiên sang API của Mistral:

Mức thinking của OpenClaw | `reasoning_effort` của Mistral  
---|---  
**off** / **minimal** | `none`  
**low** / **medium** / **high** / **xhigh** / **adaptive** / **max** | `high`  
  
Ví dụ cấu hình theo phạm vi mô hình cho reasoning của Medium 3.5:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "mistral/mistral-medium-3-5" },      models: {        "mistral/mistral-medium-3-5": {          params: { thinking: "high" },        },      },    },  },}
[/code]

Embedding bộ nhớ

Mistral có thể phục vụ embedding bộ nhớ qua `/v1/embeddings` (mô hình mặc định: `mistral-embed`).

json5Copy code
[code]
    {  memorySearch: { provider: "mistral" },}
[/code]

Xác thực và URL cơ sở

  * Xác thực Mistral dùng `MISTRAL_API_KEY` (header Bearer).
  * URL cơ sở của nhà cung cấp mặc định là `https://api.mistral.ai/v1` và chấp nhận dạng yêu cầu chat-completions tiêu chuẩn tương thích OpenAI.
  * Mô hình onboarding mặc định là `mistral/mistral-large-latest`.
  * Chỉ ghi đè URL cơ sở tại `models.providers.mistral.baseUrl` khi Mistral công bố rõ ràng một endpoint khu vực mà bạn cần.


## Liên quan

[**Chọn mô hình** Chọn nhà cung cấp, tham chiếu mô hình, và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Hiểu phương tiện** Thiết lập phiên âm âm thanh và chọn nhà cung cấp. ](</vi/nodes/media-understanding>)

Was this useful?YesNo