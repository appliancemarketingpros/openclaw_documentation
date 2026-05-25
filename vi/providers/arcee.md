---
title: Arcee AI
source_url: https://docs.openclaw.ai/vi/providers/arcee
scraped_at: 2026-05-25
---

[Arcee AI](<https://arcee.ai>) cung cấp quyền truy cập vào dòng mô hình mixture-of-experts Trinity thông qua API tương thích với OpenAI. Tất cả mô hình Trinity đều được cấp phép Apache 2.0.

Có thể truy cập các mô hình Arcee AI trực tiếp qua nền tảng Arcee hoặc thông qua [OpenRouter](</vi/providers/openrouter>).

Thuộc tính | Giá trị  
---|---  
Provider | `arcee`  
Xác thực | `ARCEEAI_API_KEY` (trực tiếp) hoặc `OPENROUTER_API_KEY` (qua OpenRouter)  
API | Tương thích với OpenAI  
URL cơ sở | `https://api.arcee.ai/api/v1` (trực tiếp) hoặc `https://openrouter.ai/api/v1` (OpenRouter)  
  
## Bắt đầu

### Direct (Arcee platform)

* ### Get an API key

Tạo khóa API tại [Arcee AI](<https://chat.arcee.ai/>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### Via OpenRouter

* ### Get an API key

Tạo khóa API tại [OpenRouter](<https://openrouter.ai/keys>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

Các model ref tương tự hoạt động cho cả thiết lập trực tiếp và qua OpenRouter (ví dụ `arcee/trinity-large-thinking`).

## Thiết lập không tương tác

### Direct (Arcee platform)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### Via OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## Danh mục tích hợp sẵn

OpenClaw hiện đi kèm danh mục Arcee được đóng gói này:

Model ref | Tên | Đầu vào | Ngữ cảnh | Chi phí (vào/ra trên 1 triệu) | Ghi chú  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | text | 256K | $0.25 / $0.90 | Mô hình mặc định; đã bật reasoning  
`arcee/trinity-large-preview` | Trinity Large Preview | text | 128K | $0.25 / $1.00 | Đa dụng; 400B tham số, 13B active  
`arcee/trinity-mini` | Trinity Mini 26B | text | 128K | $0.045 / $0.15 | Nhanh và tiết kiệm chi phí; gọi hàm  
  
## Tính năng được hỗ trợ

Tính năng | Được hỗ trợ  
---|---  
Streaming | Có  
Sử dụng công cụ / gọi hàm | Có (Trinity Mini, Trinity Large Preview)  
Đầu ra có cấu trúc (chế độ JSON và schema JSON) | Có  
Extended thinking | Có (Trinity Large Thinking; đã tắt công cụ)  
  
Environment note

Nếu Gateway chạy dưới dạng daemon (launchd/systemd), hãy đảm bảo `ARCEEAI_API_KEY` (hoặc `OPENROUTER_API_KEY`) khả dụng cho tiến trình đó (ví dụ, trong `~/.openclaw/.env` hoặc qua `env.shellEnv`).

OpenRouter routing

Khi sử dụng mô hình Arcee qua OpenRouter, các model ref `arcee/*` tương tự được áp dụng. OpenClaw xử lý định tuyến một cách trong suốt dựa trên lựa chọn xác thực của bạn. Xem [tài liệu provider OpenRouter](</vi/providers/openrouter>) để biết chi tiết cấu hình dành riêng cho OpenRouter.

## Liên quan

[**OpenRouter** Truy cập các mô hình Arcee và nhiều mô hình khác thông qua một khóa API duy nhất. ](</vi/providers/openrouter>) [**Model selection** Chọn provider, model ref và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>)

Was this useful?YesNo