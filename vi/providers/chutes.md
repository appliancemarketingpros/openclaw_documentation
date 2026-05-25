---
title: Chutes
source_url: https://docs.openclaw.ai/vi/providers/chutes
scraped_at: 2026-05-25
---

[Chutes](<https://chutes.ai>) cung cấp các danh mục mô hình nguồn mở thông qua một API tương thích với OpenAI. OpenClaw hỗ trợ cả xác thực OAuth trên trình duyệt và xác thực trực tiếp bằng khóa API cho provider `chutes` được tích hợp sẵn.

Thuộc tính | Giá trị  
---|---  
Provider | `chutes`  
API | Tương thích với OpenAI  
URL cơ sở | `https://llm.chutes.ai/v1`  
Xác thực | OAuth hoặc khóa API (xem bên dưới)  
  
## Bắt đầu

### OAuth

* ### Chạy luồng onboarding OAuth

bashCopy code
[code]
    openclaw onboard --auth-choice chutes
[/code]

OpenClaw khởi chạy luồng trình duyệt cục bộ, hoặc hiển thị URL + luồng dán chuyển hướng trên các máy chủ từ xa/không có giao diện. Token OAuth tự động làm mới thông qua hồ sơ xác thực OpenClaw.

* ### Xác minh mô hình mặc định

Sau khi onboarding, mô hình mặc định được đặt thành `chutes/zai-org/GLM-4.7-TEE` và danh mục Chutes được tích hợp sẵn sẽ được đăng ký.

### Khóa API

* ### Lấy khóa API

Tạo khóa tại [chutes.ai/settings/api-keys](<https://chutes.ai/settings/api-keys>).

* ### Chạy luồng onboarding khóa API

bashCopy code
[code]
    openclaw onboard --auth-choice chutes-api-key
[/code]

* ### Xác minh mô hình mặc định

Sau khi onboarding, mô hình mặc định được đặt thành `chutes/zai-org/GLM-4.7-TEE` và danh mục Chutes được tích hợp sẵn sẽ được đăng ký.

## Hành vi khám phá

Khi có xác thực Chutes, OpenClaw truy vấn danh mục Chutes bằng thông tin xác thực đó và sử dụng các mô hình được khám phá. Nếu khám phá thất bại, OpenClaw sẽ quay về danh mục tĩnh được tích hợp sẵn để onboarding và khởi động vẫn hoạt động.

## Bí danh mặc định

OpenClaw đăng ký ba bí danh tiện dụng cho danh mục Chutes được tích hợp sẵn:

Bí danh | Mô hình đích  
---|---  
`chutes-fast` | `chutes/zai-org/GLM-4.7-FP8`  
`chutes-pro` | `chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes-vision` | `chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
  
## Danh mục khởi đầu tích hợp sẵn

Danh mục dự phòng được tích hợp sẵn bao gồm các ref Chutes hiện tại:

Ref mô hình  
---  
`chutes/zai-org/GLM-4.7-TEE`  
`chutes/zai-org/GLM-5-TEE`  
`chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes/deepseek-ai/DeepSeek-R1-0528-TEE`  
`chutes/moonshotai/Kimi-K2.5-TEE`  
`chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
`chutes/Qwen/Qwen3-Coder-Next-TEE`  
`chutes/openai/gpt-oss-120b-TEE`  
  
## Ví dụ cấu hình

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "chutes/zai-org/GLM-4.7-TEE" },      models: {        "chutes/zai-org/GLM-4.7-TEE": { alias: "Chutes GLM 4.7" },        "chutes/deepseek-ai/DeepSeek-V3.2-TEE": { alias: "Chutes DeepSeek V3.2" },      },    },  },}
[/code]

Ghi đè OAuth

Bạn có thể tùy chỉnh luồng OAuth bằng các biến môi trường tùy chọn:

Biến | Mục đích  
---|---  
`CHUTES_CLIENT_ID` | ID client OAuth tùy chỉnh  
`CHUTES_CLIENT_SECRET` | Secret client OAuth tùy chỉnh  
`CHUTES_OAUTH_REDIRECT_URI` | URI chuyển hướng tùy chỉnh  
`CHUTES_OAUTH_SCOPES` | Phạm vi OAuth tùy chỉnh  
  
Xem [tài liệu OAuth của Chutes](<https://chutes.ai/docs/sign-in-with-chutes/overview>) để biết yêu cầu về ứng dụng chuyển hướng và nhận trợ giúp.

Ghi chú

  * Khám phá bằng khóa API và OAuth đều dùng cùng id provider `chutes`.
  * Các mô hình Chutes được đăng ký dưới dạng `chutes/<model-id>`.
  * Nếu khám phá thất bại khi khởi động, danh mục tĩnh được tích hợp sẵn sẽ được dùng tự động.


## Liên quan

[**Lựa chọn mô hình** Quy tắc provider, ref mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Tham chiếu cấu hình** Schema cấu hình đầy đủ bao gồm cài đặt provider. ](</vi/gateway/configuration-reference>) [**Chutes** Bảng điều khiển Chutes và tài liệu API. ](<https://chutes.ai>) [**Khóa API Chutes** Tạo và quản lý khóa API Chutes. ](<https://chutes.ai/settings/api-keys>)

Was this useful?YesNo