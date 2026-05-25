---
title: Tổng hợp
source_url: https://docs.openclaw.ai/vi/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>) cung cấp các điểm cuối tương thích với Anthropic. OpenClaw đăng ký nó làm nhà cung cấp `synthetic` và sử dụng API Anthropic Messages.

Thuộc tính | Giá trị  
---|---  
Nhà cung cấp | `synthetic`  
Xác thực | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
URL cơ sở | `https://api.synthetic.new/anthropic`  
  
## Bắt đầu

* ### Lấy khóa API

Lấy `SYNTHETIC_API_KEY` từ tài khoản Synthetic của bạn, hoặc để trình hướng dẫn onboarding nhắc bạn nhập một khóa.

* ### Chạy onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### Xác minh mô hình mặc định

Sau khi onboarding, mô hình mặc định được đặt thành:

CodeCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## Ví dụ cấu hình

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## Danh mục tích hợp sẵn

Tất cả mô hình Synthetic dùng chi phí `0` (đầu vào/đầu ra/bộ nhớ đệm).

ID mô hình | Cửa sổ ngữ cảnh | Token tối đa | Suy luận | Đầu vào  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | không | văn bản  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | có | văn bản  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | không | văn bản  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | không | văn bản  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | không | văn bản  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | không | văn bản  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | không | văn bản  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | không | văn bản  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | không | văn bản  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | không | văn bản  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | không | văn bản  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | có | văn bản + hình ảnh  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | không | văn bản  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | không | văn bản  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | không | văn bản  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | không | văn bản + hình ảnh  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | không | văn bản  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | không | văn bản  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | có | văn bản + hình ảnh  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | không | văn bản  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | có | văn bản  
  
Danh sách cho phép mô hình

Nếu bạn bật danh sách cho phép mô hình (`agents.defaults.models`), hãy thêm mọi mô hình Synthetic mà bạn dự định dùng. Các mô hình không có trong danh sách cho phép sẽ bị ẩn khỏi tác nhân.

Ghi đè URL cơ sở

Nếu Synthetic thay đổi điểm cuối API, hãy ghi đè URL cơ sở trong cấu hình của bạn:

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

Hãy nhớ rằng OpenClaw tự động thêm `/v1`.

## Liên quan

[**Chọn mô hình** Quy tắc nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Tham chiếu cấu hình** Lược đồ cấu hình đầy đủ, bao gồm cài đặt nhà cung cấp. ](</vi/gateway/configuration-reference>) [**Synthetic** Bảng điều khiển Synthetic và tài liệu API. ](<https://synthetic.new>)

Was this useful?YesNo