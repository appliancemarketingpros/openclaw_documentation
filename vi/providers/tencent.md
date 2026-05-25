---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/vi/providers/tencent
scraped_at: 2026-05-25
---

Tencent Cloud được cung cấp dưới dạng plugin nhà cung cấp được đóng gói kèm trong OpenClaw. Nó cho phép truy cập Tencent Hy3 preview thông qua điểm cuối TokenHub (`tencent-tokenhub`) bằng API tương thích OpenAI.

Thuộc tính | Giá trị  
---|---  
Id nhà cung cấp | `tencent-tokenhub`  
Plugin | được đóng gói kèm, `enabledByDefault: true`  
Biến env xác thực | `TOKENHUB_API_KEY`  
Cờ onboarding | `--auth-choice tokenhub-api-key`  
Cờ CLI trực tiếp | `--tokenhub-api-key <key>`  
API | tương thích OpenAI (`openai-completions`)  
URL cơ sở mặc định | `https://tokenhub.tencentmaas.com/v1`  
URL cơ sở toàn cầu | `https://tokenhub-intl.tencentmaas.com/v1` (ghi đè)  
Mô hình mặc định | `tencent-tokenhub/hy3-preview`  
  
## Bắt đầu nhanh

* ### Tạo khóa API TokenHub

Tạo khóa API trong Tencent Cloud TokenHub. Nếu bạn chọn phạm vi truy cập giới hạn cho khóa, hãy bao gồm **Hy3 preview** trong các mô hình được phép.

* ### Chạy onboarding

OnboardingCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Env onlyCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### Xác minh mô hình

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## Thiết lập không tương tác

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Catalog tích hợp

Tham chiếu mô hình | Tên | Đầu vào | Ngữ cảnh | Đầu ra tối đa | Ghi chú  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | văn bản | 256,000 | 64,000 | Mặc định; hỗ trợ reasoning  
  
Hy3 preview là mô hình ngôn ngữ MoE lớn của Tencent Hunyuan dành cho reasoning, làm theo chỉ dẫn với ngữ cảnh dài, mã và quy trình tác vụ agent. Các ví dụ tương thích OpenAI của Tencent dùng `hy3-preview` làm id mô hình và hỗ trợ gọi công cụ chat-completions tiêu chuẩn cùng với `reasoning_effort`.

## Giá theo bậc

Catalog được đóng gói kèm cung cấp metadata chi phí theo bậc, thay đổi theo độ dài cửa sổ đầu vào, nên các ước tính chi phí được điền sẵn mà không cần ghi đè thủ công.

Phạm vi token đầu vào | Giá đầu vào | Giá đầu ra | Đọc cache  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
Mức giá tính theo mỗi triệu token bằng USD như Tencent công bố. Chỉ ghi đè giá trong `models.providers.tencent-tokenhub` khi bạn cần một bề mặt khác.

## Cấu hình nâng cao

Ghi đè điểm cuối

OpenClaw mặc định dùng điểm cuối `https://tokenhub.tencentmaas.com/v1` của Tencent Cloud. Tencent cũng tài liệu hóa một điểm cuối TokenHub quốc tế:

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

Chỉ ghi đè điểm cuối khi tài khoản hoặc khu vực TokenHub của bạn yêu cầu.

Khả dụng môi trường cho daemon

Nếu Gateway chạy như một dịch vụ được quản lý (launchd, systemd, Docker), `TOKENHUB_API_KEY` phải hiển thị với tiến trình đó. Đặt nó trong `~/.openclaw/.env` hoặc thông qua `env.shellEnv` để các môi trường launchd, systemd hoặc Docker exec có thể đọc được.

## Liên quan

[**Nhà cung cấp mô hình** Chọn nhà cung cấp, tham chiếu mô hình và hành vi failover. ](</vi/concepts/model-providers>) [**Tham chiếu cấu hình** Schema cấu hình đầy đủ, bao gồm cài đặt nhà cung cấp. ](</vi/gateway/configuration>) [**Tencent TokenHub** Trang sản phẩm TokenHub của Tencent Cloud. ](<https://cloud.tencent.com/product/tokenhub>) [**Thẻ mô hình Hy3 preview** Chi tiết và benchmark của Tencent Hunyuan Hy3 preview. ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo