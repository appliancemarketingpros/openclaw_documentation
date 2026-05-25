---
title: DeepSeek
source_url: https://docs.openclaw.ai/vi/providers/deepseek
scraped_at: 2026-05-25
---

[DeepSeek](<https://www.deepseek.com>) cung cấp các mô hình AI mạnh mẽ với API tương thích với OpenAI.

Thuộc tính | Giá trị  
---|---  
Nhà cung cấp | `deepseek`  
Xác thực | `DEEPSEEK_API_KEY`  
API | Tương thích với OpenAI  
URL cơ sở | `https://api.deepseek.com`  
  
## Bắt đầu

* ### Lấy khóa API của bạn

Tạo khóa API tại [platform.deepseek.com](<https://platform.deepseek.com/api_keys>).

* ### Chạy quy trình onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice deepseek-api-key
[/code]

Lệnh này sẽ yêu cầu khóa API của bạn và đặt `deepseek/deepseek-v4-flash` làm mô hình mặc định.

* ### Xác minh các mô hình có sẵn

bashCopy code
[code]
    openclaw models list --provider deepseek
[/code]

Để kiểm tra danh mục tĩnh đi kèm mà không cần Gateway đang chạy, hãy dùng:

bashCopy code
[code]
    openclaw models list --all --provider deepseek
[/code]

Thiết lập không tương tác

Với các bản cài đặt theo script hoặc không có giao diện, truyền trực tiếp tất cả cờ:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice deepseek-api-key \  --deepseek-api-key "$DEEPSEEK_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Danh mục tích hợp sẵn

Tham chiếu mô hình | Tên | Đầu vào | Ngữ cảnh | Đầu ra tối đa | Ghi chú  
---|---|---|---|---|---  
`deepseek/deepseek-v4-flash` | DeepSeek V4 Flash | text | 1,000,000 | 384,000 | Mô hình mặc định; bề mặt V4 hỗ trợ suy nghĩ  
`deepseek/deepseek-v4-pro` | DeepSeek V4 Pro | text | 1,000,000 | 384,000 | Bề mặt V4 hỗ trợ suy nghĩ  
`deepseek/deepseek-chat` | DeepSeek Chat | text | 131,072 | 8,192 | Bề mặt DeepSeek V3.2 không suy nghĩ  
`deepseek/deepseek-reasoner` | DeepSeek Reasoner | text | 131,072 | 65,536 | Bề mặt V3.2 hỗ trợ lập luận  
  
## Suy nghĩ và công cụ

Các phiên suy nghĩ của DeepSeek V4 có hợp đồng phát lại nghiêm ngặt hơn hầu hết nhà cung cấp tương thích với OpenAI: sau khi một lượt bật suy nghĩ sử dụng công cụ, DeepSeek kỳ vọng các thông điệp assistant được phát lại từ lượt đó bao gồm `reasoning_content` trong các yêu cầu tiếp theo. OpenClaw xử lý việc này bên trong Plugin DeepSeek, nên việc dùng công cụ nhiều lượt thông thường hoạt động với `deepseek/deepseek-v4-flash` và `deepseek/deepseek-v4-pro`.

Nếu bạn chuyển một phiên hiện có từ một nhà cung cấp tương thích với OpenAI khác sang mô hình DeepSeek V4, các lượt gọi công cụ cũ của assistant có thể không có `reasoning_content` gốc của DeepSeek. OpenClaw điền trường còn thiếu đó trên các thông điệp assistant được phát lại cho yêu cầu suy nghĩ DeepSeek V4 để nhà cung cấp có thể chấp nhận lịch sử mà không cần `/new`.

Khi suy nghĩ bị tắt trong OpenClaw (bao gồm lựa chọn **None** trong UI), OpenClaw gửi DeepSeek `thinking: { type: "disabled" }` và loại bỏ `reasoning_content` được phát lại khỏi lịch sử gửi đi. Điều này giữ các phiên tắt suy nghĩ trên đường dẫn DeepSeek không suy nghĩ.

Dùng `deepseek/deepseek-v4-flash` cho đường dẫn nhanh mặc định. Dùng `deepseek/deepseek-v4-pro` khi bạn muốn mô hình V4 mạnh hơn và có thể chấp nhận chi phí hoặc độ trễ cao hơn.

## Kiểm thử live

Bộ kiểm thử live mô hình trực tiếp bao gồm DeepSeek V4 trong tập mô hình hiện đại. Để chỉ chạy các kiểm tra mô hình trực tiếp DeepSeek V4:

bashCopy code
[code]
    OPENCLAW_LIVE_PROVIDERS=deepseek \OPENCLAW_LIVE_MODELS="deepseek/deepseek-v4-flash,deepseek/deepseek-v4-pro" \pnpm test:live src/agents/models.profiles.live.test.ts
[/code]

Kiểm tra live đó xác minh cả hai mô hình V4 có thể hoàn tất và các lượt tiếp theo suy nghĩ/công cụ bảo toàn payload phát lại mà DeepSeek yêu cầu.

## Ví dụ cấu hình

json5Copy code
[code]
    {  env: { DEEPSEEK_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "deepseek/deepseek-v4-flash" },    },  },}
[/code]

## Liên quan

[**Chọn mô hình** Chọn nhà cung cấp, tham chiếu mô hình và hành vi failover. ](</vi/concepts/model-providers>) [**Tham chiếu cấu hình** Tham chiếu cấu hình đầy đủ cho agent, mô hình và nhà cung cấp. ](</vi/gateway/configuration-reference>)

Was this useful?YesNo