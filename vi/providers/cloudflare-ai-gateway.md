---
title: Gateway AI của Cloudflare
source_url: https://docs.openclaw.ai/vi/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway đứng trước các API của nhà cung cấp và cho phép bạn thêm phân tích, bộ nhớ đệm và các biện pháp kiểm soát. Với Anthropic, OpenClaw sử dụng Anthropic Messages API thông qua điểm cuối Gateway của bạn.

Thuộc tính | Giá trị  
---|---  
Nhà cung cấp | `cloudflare-ai-gateway`  
URL cơ sở | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
Mô hình mặc định | `cloudflare-ai-gateway/claude-sonnet-4-6`  
Khóa API | `CLOUDFLARE_AI_GATEWAY_API_KEY` (khóa API nhà cung cấp của bạn cho các yêu cầu thông qua Gateway)  
  
Khi bật tư duy cho các mô hình Anthropic Messages, OpenClaw sẽ loại bỏ các lượt điền trước cuối của trợ lý trước khi gửi payload qua Cloudflare AI Gateway. Anthropic từ chối điền trước phản hồi với tư duy mở rộng, trong khi điền trước thông thường không dùng tư duy vẫn khả dụng.

## Bắt đầu

* ### Đặt khóa API nhà cung cấp và thông tin Gateway

Chạy quy trình giới thiệu ban đầu và chọn tùy chọn xác thực Cloudflare AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

Lệnh này sẽ yêu cầu ID tài khoản, ID gateway và khóa API của bạn.

* ### Đặt mô hình mặc định

Thêm mô hình vào cấu hình OpenClaw của bạn:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### Xác minh mô hình khả dụng

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## Ví dụ không tương tác

Với các thiết lập dạng script hoặc CI, hãy truyền mọi giá trị trên dòng lệnh:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## Cấu hình nâng cao

Gateway đã xác thực

Nếu bạn đã bật xác thực Gateway trong Cloudflare, hãy thêm header `cf-aig-authorization`. Điều này **bổ sung cho** khóa API nhà cung cấp của bạn.

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

Ghi chú về môi trường

Nếu Gateway chạy dưới dạng daemon (launchd/systemd), hãy bảo đảm `CLOUDFLARE_AI_GATEWAY_API_KEY` khả dụng cho tiến trình đó.

## Liên quan

[**Lựa chọn mô hình** Chọn nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Khắc phục sự cố** Khắc phục sự cố chung và câu hỏi thường gặp. ](</vi/help/troubleshooting>)

Was this useful?YesNo