---
title: Groq
source_url: https://docs.openclaw.ai/vi/providers/groq
scraped_at: 2026-05-25
---

[Groq](<https://groq.com>) cung cấp suy luận siêu nhanh trên các mô hình open-weight (Llama, Gemma, Kimi, Qwen, GPT OSS và nhiều mô hình khác) bằng phần cứng LPU tùy chỉnh. OpenClaw bao gồm một Plugin Groq được đóng gói kèm, đăng ký cả nhà cung cấp trò chuyện tương thích OpenAI và nhà cung cấp hiểu phương tiện âm thanh.

Thuộc tính | Giá trị  
---|---  
ID nhà cung cấp | `groq`  
Plugin | được đóng gói kèm, `enabledByDefault: true`  
Biến môi trường xác thực | `GROQ_API_KEY`  
Cờ thiết lập ban đầu | `--auth-choice groq-api-key`  
API | tương thích OpenAI (`openai-completions`)  
URL cơ sở | `https://api.groq.com/openai/v1`  
Phiên âm âm thanh | `whisper-large-v3-turbo` (mặc định)  
Mặc định trò chuyện được đề xuất | `groq/llama-3.3-70b-versatile`  
  
## Bắt đầu

* ### Lấy khóa API

Tạo khóa API tại [console.groq.com/keys](<https://console.groq.com/keys>).

* ### Thiết lập khóa API

OnboardingCopy code
[code]
    openclaw onboard --auth-choice groq-api-key
[/code]

Env onlyCopy code
[code]
    export GROQ_API_KEY=gsk_...
[/code]

* ### Thiết lập mô hình mặc định

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

* ### Xác minh catalog có thể truy cập

bashCopy code
[code]
    openclaw models list --provider groq
[/code]

### Ví dụ tệp cấu hình

json5Copy code
[code]
    {  env: { GROQ_API_KEY: "gsk_..." },  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

## Catalog tích hợp sẵn

OpenClaw phát hành kèm catalog Groq dựa trên manifest với cả các mục có suy luận và không suy luận. Chạy `openclaw models list --provider groq` để xem các hàng được đóng gói kèm cho phiên bản bạn đã cài đặt, hoặc kiểm tra [console.groq.com/docs/models](<https://console.groq.com/docs/models>) để xem danh sách có thẩm quyền của Groq.

Tham chiếu mô hình | Tên | Suy luận | Đầu vào | Ngữ cảnh  
---|---|---|---|---  
`groq/llama-3.3-70b-versatile` | Llama 3.3 70B Versatile | không | văn bản | 131,072  
`groq/llama-3.1-8b-instant` | Llama 3.1 8B Instant | không | văn bản | 131,072  
`groq/meta-llama/llama-4-maverick-17b-128e-instruct` | Llama 4 Maverick 17B | không | văn bản + hình ảnh | 131,072  
`groq/meta-llama/llama-4-scout-17b-16e-instruct` | Llama 4 Scout 17B | không | văn bản + hình ảnh | 131,072  
`groq/llama3-70b-8192` | Llama 3 70B | không | văn bản | 8,192  
`groq/llama3-8b-8192` | Llama 3 8B | không | văn bản | 8,192  
`groq/gemma2-9b-it` | Gemma 2 9B | không | văn bản | 8,192  
`groq/mistral-saba-24b` | Mistral Saba 24B | không | văn bản | 32,768  
`groq/moonshotai/kimi-k2-instruct` | Kimi K2 Instruct | không | văn bản | 131,072  
`groq/moonshotai/kimi-k2-instruct-0905` | Kimi K2 Instruct 0905 | không | văn bản | 262,144  
`groq/openai/gpt-oss-120b` | GPT OSS 120B | có | văn bản | 131,072  
`groq/openai/gpt-oss-20b` | GPT OSS 20B | có | văn bản | 131,072  
`groq/openai/gpt-oss-safeguard-20b` | Safety GPT OSS 20B | có | văn bản | 131,072  
`groq/qwen-qwq-32b` | Qwen QwQ 32B | có | văn bản | 131,072  
`groq/qwen/qwen3-32b` | Qwen3 32B | có | văn bản | 131,072  
`groq/deepseek-r1-distill-llama-70b` | DeepSeek R1 Distill Llama 70B | có | văn bản | 131,072  
`groq/groq/compound` | Compound | có | văn bản | 131,072  
`groq/groq/compound-mini` | Compound Mini | có | văn bản | 131,072  
  
## Mô hình suy luận

OpenClaw ánh xạ các mức `/think` dùng chung của mình sang các giá trị `reasoning_effort` riêng theo mô hình của Groq:

  * Với `qwen/qwen3-32b`, suy nghĩ bị tắt sẽ gửi `none` và suy nghĩ được bật sẽ gửi `default`.
  * Với các mô hình suy luận Groq GPT OSS (`openai/gpt-oss-*`), OpenClaw gửi `low`, `medium` hoặc `high` dựa trên mức `/think`. Khi suy nghĩ bị tắt, `reasoning_effort` sẽ bị bỏ qua vì các mô hình đó không hỗ trợ giá trị tắt.
  * DeepSeek R1 Distill, Qwen QwQ và Compound dùng bề mặt suy luận gốc của Groq; `/think` kiểm soát khả năng hiển thị nhưng mô hình luôn suy luận.


Xem [Chế độ suy nghĩ](</vi/tools/thinking>) để biết các mức `/think` dùng chung và cách OpenClaw chuyển đổi chúng theo từng nhà cung cấp.

## Phiên âm âm thanh

Plugin được đóng gói kèm của Groq cũng đăng ký một **nhà cung cấp hiểu phương tiện âm thanh** để tin nhắn thoại có thể được phiên âm thông qua bề mặt `tools.media.audio` dùng chung.

Thuộc tính | Giá trị  
---|---  
Đường dẫn cấu hình dùng chung | `tools.media.audio`  
URL cơ sở mặc định | `https://api.groq.com/openai/v1`  
Mô hình mặc định | `whisper-large-v3-turbo`  
Độ ưu tiên tự động | 20  
Điểm cuối API | tương thích OpenAI `/audio/transcriptions`  
  
Để đặt Groq làm backend âm thanh mặc định:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [{ provider: "groq" }],      },    },  },}
[/code]

Khả dụng môi trường cho daemon

Nếu Gateway chạy như một dịch vụ được quản lý (launchd, systemd, Docker), `GROQ_API_KEY` phải hiển thị với tiến trình đó — không chỉ với shell tương tác của bạn.

ID mô hình Groq tùy chỉnh

OpenClaw chấp nhận mọi ID mô hình Groq khi chạy. Dùng đúng ID do Groq hiển thị và thêm tiền tố `groq/`. Catalog được đóng gói kèm bao phủ các trường hợp phổ biến; các ID không có trong catalog sẽ rơi về mẫu tương thích OpenAI mặc định.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/<your-model-id>" },    },  },}
[/code]

## Liên quan

[**Nhà cung cấp mô hình** Chọn nhà cung cấp, tham chiếu mô hình và hành vi chuyển dự phòng. ](</vi/concepts/model-providers>) [**Chế độ suy nghĩ** Các mức nỗ lực suy luận và tương tác với chính sách nhà cung cấp. ](</vi/tools/thinking>) [**Tham chiếu cấu hình** Schema cấu hình đầy đủ, bao gồm thiết lập nhà cung cấp và âm thanh. ](</vi/gateway/configuration-reference>) [**Groq Console** Bảng điều khiển Groq, tài liệu API và giá. ](<https://console.groq.com>)

Was this useful?YesNo