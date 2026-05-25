---
title: Cerebras
source_url: https://docs.openclaw.ai/vi/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) cung cấp suy luận tốc độ cao tương thích OpenAI trên phần cứng suy luận tùy chỉnh. OpenClaw bao gồm một Plugin nhà cung cấp Cerebras được đóng gói kèm với danh mục tĩnh gồm bốn mô hình.

Thuộc tính | Giá trị  
---|---  
ID nhà cung cấp | `cerebras`  
Plugin | được đóng gói kèm, `enabledByDefault: true`  
Biến env xác thực | `CEREBRAS_API_KEY`  
Cờ thiết lập ban đầu | `--auth-choice cerebras-api-key`  
Cờ CLI trực tiếp | `--cerebras-api-key <key>`  
API | tương thích OpenAI (`openai-completions`)  
URL cơ sở | `https://api.cerebras.ai/v1`  
Mô hình mặc định | `cerebras/zai-glm-4.7`  
  
## Bắt đầu

* ### Lấy khóa API

Tạo một khóa API trong [Cerebras Cloud Console](<https://cloud.cerebras.ai>).

* ### Chạy thiết lập ban đầu

Thiết lập ban đầuCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Cờ trực tiếpCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Chỉ envCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### Xác minh các mô hình có sẵn

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

Danh sách phải bao gồm cả bốn mô hình được đóng gói kèm. Nếu `CEREBRAS_API_KEY` chưa được phân giải, `openclaw models status --json` sẽ báo cáo thông tin xác thực bị thiếu trong `auth.unusableProfiles`.

## Thiết lập không tương tác

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## Danh mục tích hợp sẵn

OpenClaw đi kèm một danh mục Cerebras tĩnh phản ánh endpoint công khai tương thích OpenAI. Cả bốn mô hình đều dùng chung ngữ cảnh 128k và 8.192 token đầu ra tối đa.

Tham chiếu mô hình | Tên | Suy luận | Ghi chú  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | có | Mô hình mặc định; mô hình suy luận bản xem trước  
`cerebras/gpt-oss-120b` | GPT OSS 120B | có | Mô hình suy luận dùng cho production  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | không | Mô hình không suy luận bản xem trước  
`cerebras/llama3.1-8b` | Llama 3.1 8B | không | Mô hình production tập trung vào tốc độ  
  
## Cấu hình thủ công

Plugin được đóng gói kèm thường có nghĩa là bạn chỉ cần khóa API. Hãy dùng cấu hình `models.providers.cerebras` rõ ràng khi bạn muốn ghi đè metadata mô hình hoặc chạy trong `mode: "merge"` trên danh mục tĩnh:

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## Liên quan

[**Nhà cung cấp mô hình** Chọn nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Chế độ suy nghĩ** Các mức nỗ lực suy luận cho hai mô hình Cerebras có khả năng suy luận. ](</vi/tools/thinking>) [**Tham chiếu cấu hình** Mặc định của agent và cấu hình mô hình. ](</vi/gateway/config-agents#agent-defaults>) [**Câu hỏi thường gặp về mô hình** Hồ sơ xác thực, chuyển đổi mô hình và xử lý lỗi "no profile". ](</vi/help/faq-models>)

Was this useful?YesNo