---
title: Pháo hoa
source_url: https://docs.openclaw.ai/vi/providers/fireworks
scraped_at: 2026-05-25
---

[Fireworks](<https://fireworks.ai>) cung cấp các mô hình open-weight và mô hình định tuyến thông qua một API tương thích OpenAI. OpenClaw bao gồm một Plugin nhà cung cấp Fireworks được đóng gói sẵn, đi kèm hai mô hình Kimi đã được lập danh mục trước và chấp nhận mọi id mô hình hoặc router của Fireworks khi chạy.

Thuộc tính | Giá trị  
---|---  
Id nhà cung cấp | `fireworks` (bí danh: `fireworks-ai`)  
Plugin | được đóng gói sẵn, `enabledByDefault: true`  
Biến môi trường xác thực | `FIREWORKS_API_KEY`  
Cờ onboarding | `--auth-choice fireworks-api-key`  
Cờ CLI trực tiếp | `--fireworks-api-key <key>`  
API | Tương thích OpenAI (`openai-completions`)  
URL cơ sở | `https://api.fireworks.ai/inference/v1`  
Mô hình mặc định | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
Bí danh mặc định | `Kimi K2.5 Turbo`  
  
## Bắt đầu

* ### Đặt khóa API Fireworks

OnboardingCopy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

Onboarding lưu khóa cho nhà cung cấp `fireworks` trong hồ sơ xác thực của bạn và đặt router Kimi K2.5 Turbo **Fire Pass** làm mô hình mặc định.

* ### Xác minh mô hình có sẵn

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

Danh sách nên bao gồm `Kimi K2.6` và `Kimi K2.5 Turbo (Fire Pass)`. Nếu `FIREWORKS_API_KEY` chưa được phân giải, `openclaw models status --json` sẽ báo thông tin xác thực bị thiếu trong `auth.unusableProfiles`.

## Thiết lập không tương tác

Đối với cài đặt bằng script hoặc CI, truyền mọi thứ trên dòng lệnh:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Danh mục tích hợp sẵn

Tham chiếu mô hình | Tên | Đầu vào | Ngữ cảnh | Đầu ra tối đa | Thinking  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | văn bản + hình ảnh | 262,144 | 262,144 | Bắt buộc tắt  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | văn bản + hình ảnh | 256,000 | 256,000 | Bắt buộc tắt (mặc định)  
  
## Id mô hình Fireworks tùy chỉnh

OpenClaw chấp nhận mọi id mô hình hoặc router của Fireworks khi chạy. Dùng đúng id do Fireworks hiển thị và thêm tiền tố `fireworks/`. Cơ chế phân giải động sao chép mẫu Fire Pass (đầu vào văn bản + hình ảnh, API tương thích OpenAI, chi phí mặc định bằng không) và tự động tắt thinking khi id khớp mẫu Kimi.

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

Cách tiền tố id mô hình hoạt động

Mọi tham chiếu mô hình Fireworks trong OpenClaw đều bắt đầu bằng `fireworks/`, theo sau là id chính xác hoặc đường dẫn router từ nền tảng Fireworks. Ví dụ:

  * Mô hình router: `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * Mô hình trực tiếp: `fireworks/accounts/fireworks/models/<model-name>`


OpenClaw loại bỏ tiền tố `fireworks/` khi tạo yêu cầu API và gửi phần đường dẫn còn lại đến endpoint Fireworks dưới dạng trường `model` tương thích OpenAI.

Vì sao thinking bị buộc tắt cho Kimi

Fireworks K2.6 trả về 400 nếu yêu cầu mang các tham số `reasoning_*`, dù Kimi hỗ trợ thinking thông qua API riêng của Moonshot. Chính sách đóng gói sẵn (`extensions/fireworks/thinking-policy.ts`) chỉ quảng bá mức thinking `off` cho id mô hình Kimi, nên các chuyển đổi `/think` thủ công và bề mặt chính sách nhà cung cấp luôn khớp với hợp đồng runtime.

Để dùng suy luận Kimi từ đầu đến cuối, hãy cấu hình [nhà cung cấp Moonshot](</vi/providers/moonshot>) và định tuyến cùng mô hình qua nhà cung cấp đó.

Tính sẵn có của môi trường cho daemon

Nếu Gateway chạy như một dịch vụ được quản lý (launchd, systemd, Docker), khóa Fireworks phải hiển thị với tiến trình đó — không chỉ với shell tương tác của bạn.

Trên macOS, `openclaw gateway install` đã nối `~/.openclaw/.env` vào tệp môi trường LaunchAgent. Chạy lại install (hoặc `openclaw doctor --fix`) sau khi xoay vòng khóa.

## Liên quan

[**Nhà cung cấp mô hình** Chọn nhà cung cấp, tham chiếu mô hình và hành vi failover. ](</vi/concepts/model-providers>) [**Chế độ thinking** Các mức `/think`, chính sách nhà cung cấp và định tuyến mô hình có khả năng suy luận. ](</vi/tools/thinking>) [**Moonshot** Chạy Kimi với đầu ra thinking gốc thông qua API riêng của Moonshot. ](</vi/providers/moonshot>) [**Khắc phục sự cố** Khắc phục sự cố chung và câu hỏi thường gặp. ](</vi/help/troubleshooting>)

Was this useful?YesNo