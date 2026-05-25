---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/vi/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway cung cấp một **API hợp nhất** định tuyến yêu cầu đến nhiều mô hình phía sau một endpoint và khóa API duy nhất. API này tương thích với OpenAI, vì vậy hầu hết OpenAI SDK hoạt động bằng cách đổi URL cơ sở.

Thuộc tính | Giá trị  
---|---  
Nhà cung cấp | `kilocode`  
Xác thực | `KILOCODE_API_KEY`  
API | Tương thích với OpenAI  
URL cơ sở | `https://api.kilo.ai/api/gateway/`  
  
## Bắt đầu

* ### Tạo tài khoản

Truy cập [app.kilo.ai](<https://app.kilo.ai>), đăng nhập hoặc tạo tài khoản, sau đó đi đến API Keys và tạo khóa mới.

* ### Chạy onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

Hoặc đặt trực tiếp biến môi trường:

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### Xác minh mô hình có sẵn

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## Mô hình mặc định

Mô hình mặc định là `kilocode/kilo/auto`, một mô hình định tuyến thông minh do nhà cung cấp sở hữu và được Kilo Gateway quản lý.

## Danh mục tích hợp sẵn

OpenClaw tự động phát hiện các mô hình có sẵn từ Kilo Gateway khi khởi động. Dùng `/models kilocode` để xem danh sách đầy đủ các mô hình có sẵn với tài khoản của bạn.

Mọi mô hình có sẵn trên Gateway đều có thể dùng với tiền tố `kilocode/`:

Ref mô hình | Ghi chú  
---|---  
`kilocode/kilo/auto` | Mặc định — định tuyến thông minh  
`kilocode/anthropic/claude-sonnet-4` | Anthropic qua Kilo  
`kilocode/openai/gpt-5.5` | OpenAI qua Kilo  
`kilocode/google/gemini-3.1-pro-preview` | Google qua Kilo  
...và nhiều mô hình khác | Dùng `/models kilocode` để liệt kê tất cả  
  
## Ví dụ cấu hình

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

Truyền tải và khả năng tương thích

Kilo Gateway được tài liệu hóa trong mã nguồn là tương thích với OpenRouter, vì vậy nó vẫn nằm trên đường dẫn kiểu proxy tương thích với OpenAI thay vì định dạng yêu cầu OpenAI gốc.

  * Các ref Kilo dựa trên Gemini vẫn nằm trên đường dẫn proxy-Gemini, vì vậy OpenClaw giữ việc làm sạch chữ ký suy nghĩ của Gemini tại đó mà không bật xác thực phát lại Gemini gốc hoặc viết lại bootstrap.
  * Kilo Gateway sử dụng Bearer token với khóa API của bạn ở bên dưới.

Trình bao stream và reasoning

Trình bao stream dùng chung của Kilo thêm header ứng dụng của nhà cung cấp và chuẩn hóa payload reasoning qua proxy cho các ref mô hình cụ thể được hỗ trợ.

Khắc phục sự cố

  * Nếu việc phát hiện mô hình thất bại khi khởi động, OpenClaw sẽ quay về danh mục tĩnh đi kèm chứa `kilocode/kilo/auto`.
  * Xác nhận khóa API của bạn hợp lệ và tài khoản Kilo của bạn đã bật các mô hình mong muốn.
  * Khi Gateway chạy như daemon, hãy đảm bảo `KILOCODE_API_KEY` có sẵn cho tiến trình đó (ví dụ trong `~/.openclaw/.env` hoặc qua `env.shellEnv`).


## Liên quan

[**Chọn mô hình** Chọn nhà cung cấp, ref mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Tham chiếu cấu hình** Tham chiếu cấu hình OpenClaw đầy đủ. ](</vi/gateway/configuration-reference>) [**Kilo Gateway** Bảng điều khiển Kilo Gateway, khóa API và quản lý tài khoản. ](<https://app.kilo.ai>)

Was this useful?YesNo