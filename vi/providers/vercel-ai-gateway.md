---
title: Gateway AI của Vercel
source_url: https://docs.openclaw.ai/vi/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

[Vercel AI Gateway](<https://vercel.com/ai-gateway>) cung cấp một API hợp nhất để truy cập hàng trăm mô hình thông qua một endpoint duy nhất.

Thuộc tính | Giá trị  
---|---  
Nhà cung cấp | `vercel-ai-gateway`  
Xác thực | `AI_GATEWAY_API_KEY`  
API | Tương thích với Anthropic Messages  
Danh mục mô hình | Tự động phát hiện qua `/v1/models`  
  
## Bắt đầu

* ### Set the API key

Chạy quy trình onboarding và chọn tùy chọn xác thực AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### Set a default model

Thêm mô hình vào cấu hình OpenClaw của bạn:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## Ví dụ không tương tác

Đối với thiết lập bằng script hoặc CI, truyền tất cả giá trị trên dòng lệnh:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## Cách viết tắt ID mô hình

OpenClaw chấp nhận các tham chiếu mô hình viết tắt Vercel Claude và chuẩn hóa chúng khi chạy:

Đầu vào viết tắt | Tham chiếu mô hình đã chuẩn hóa  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## Cấu hình nâng cao

Environment variable for daemon processes

Nếu OpenClaw Gateway chạy dưới dạng daemon (launchd/systemd), hãy đảm bảo `AI_GATEWAY_API_KEY` khả dụng cho tiến trình đó.

Provider routing

Vercel AI Gateway định tuyến yêu cầu đến nhà cung cấp upstream dựa trên tiền tố tham chiếu mô hình. Ví dụ, `vercel-ai-gateway/anthropic/claude-opus-4.6` định tuyến qua Anthropic, trong khi `vercel-ai-gateway/openai/gpt-5.5` định tuyến qua OpenAI và `vercel-ai-gateway/moonshotai/kimi-k2.6` định tuyến qua MoonshotAI. Một `AI_GATEWAY_API_KEY` duy nhất của bạn xử lý xác thực cho tất cả nhà cung cấp upstream.

Thinking levels

Các tùy chọn `/think` tuân theo tiền tố mô hình upstream đáng tin cậy khi OpenClaw biết hợp đồng nhà cung cấp upstream. `vercel-ai-gateway/anthropic/...` dùng hồ sơ suy nghĩ Claude, bao gồm các mặc định thích ứng cho mô hình Claude 4.6. `vercel-ai-gateway/openai/gpt-5.4`, `gpt-5.5`, và các tham chiếu kiểu Codex cung cấp `/think xhigh` giống như các nhà cung cấp OpenAI/OpenAI Codex trực tiếp. Các tham chiếu có namespace khác giữ các mức suy luận thông thường trừ khi siêu dữ liệu danh mục của chúng khai báo thêm.

## Liên quan

[**Model selection** Chọn nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Troubleshooting** Khắc phục sự cố chung và câu hỏi thường gặp. ](</vi/help/troubleshooting>)

Was this useful?YesNo