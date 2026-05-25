---
title: Together AI
source_url: https://docs.openclaw.ai/vi/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) cung cấp quyền truy cập vào các mô hình nguồn mở hàng đầu, bao gồm Llama, DeepSeek, Kimi, và nhiều mô hình khác thông qua một API hợp nhất.

Thuộc tính | Giá trị  
---|---  
Nhà cung cấp | `together`  
Xác thực | `TOGETHER_API_KEY`  
API | Tương thích với OpenAI  
URL cơ sở | `https://api.together.xyz/v1`  
  
## Bắt đầu

* ### Lấy khóa API

Tạo khóa API tại [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>).

* ### Chạy onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### Đặt mô hình mặc định

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### Ví dụ không tương tác

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## Danh mục tích hợp sẵn

OpenClaw cung cấp danh mục Together đi kèm này:

Tham chiếu mô hình | Tên | Đầu vào | Ngữ cảnh | Ghi chú  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | văn bản, hình ảnh | 262,144 | Mô hình mặc định; đã bật reasoning  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | văn bản | 202,752 | Mô hình văn bản đa dụng  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | văn bản | 131,072 | Mô hình chỉ dẫn nhanh  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | văn bản, hình ảnh | 10,000,000 | Đa phương thức  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | văn bản, hình ảnh | 20,000,000 | Đa phương thức  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | văn bản | 131,072 | Mô hình văn bản đa dụng  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | văn bản | 131,072 | Mô hình reasoning  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | văn bản | 262,144 | Mô hình văn bản Kimi phụ  
  
## Tạo video

Plugin `together` đi kèm cũng đăng ký tính năng tạo video thông qua công cụ `video_generate` dùng chung.

Thuộc tính | Giá trị  
---|---  
Mô hình video mặc định | `together/Wan-AI/Wan2.2-T2V-A14B`  
Chế độ | văn bản thành video, tham chiếu một hình ảnh  
Tham số được hỗ trợ | `aspectRatio`, `resolution`  
  
Để dùng Together làm nhà cung cấp video mặc định:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

Ghi chú về môi trường

Nếu Gateway chạy như một daemon (launchd/systemd), hãy bảo đảm `TOGETHER_API_KEY` có sẵn cho tiến trình đó (ví dụ: trong `~/.openclaw/.env` hoặc qua `env.shellEnv`).

Khắc phục sự cố

  * Xác minh khóa của bạn hoạt động: `openclaw models list --provider together`
  * Nếu mô hình không xuất hiện, hãy xác nhận khóa API được đặt trong đúng môi trường cho tiến trình Gateway của bạn.
  * Tham chiếu mô hình dùng dạng `together/<model-id>`.


## Liên quan

[**Chọn mô hình** Quy tắc nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Tạo video** Tham số công cụ tạo video dùng chung và lựa chọn nhà cung cấp. ](</vi/tools/video-generation>) [**Tham chiếu cấu hình** Schema cấu hình đầy đủ, bao gồm cài đặt nhà cung cấp. ](</vi/gateway/configuration-reference>) [**Together AI** Bảng điều khiển Together AI, tài liệu API và giá. ](<https://together.ai>)

Was this useful?YesNo