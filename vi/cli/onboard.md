---
title: Thiết lập ban đầu
source_url: https://docs.openclaw.ai/vi/cli/onboard
scraped_at: 2026-05-25
---

# `openclaw onboard`

Quy trình thiết lập ban đầu được hướng dẫn đầy đủ cho thiết lập Gateway cục bộ hoặc từ xa. Dùng lệnh này khi bạn muốn OpenClaw hướng dẫn qua xác thực mô hình, không gian làm việc, Gateway, kênh, Skills và tình trạng trong một luồng duy nhất.

## Hướng dẫn liên quan

[**Trung tâm thiết lập ban đầu CLI** Hướng dẫn từng bước về luồng CLI tương tác. ](</vi/start/wizard>) [**Tổng quan thiết lập ban đầu** Cách các phần thiết lập ban đầu của OpenClaw kết hợp với nhau. ](</vi/start/onboarding-overview>) [**Tham chiếu thiết lập CLI** Đầu ra, nội bộ và hành vi theo từng bước. ](</vi/start/wizard-cli-reference>) [**Tự động hóa CLI** Cờ không tương tác và thiết lập bằng script. ](</vi/start/wizard-cli-automation>) [**Thiết lập ban đầu ứng dụng macOS** Luồng thiết lập ban đầu cho ứng dụng thanh menu macOS. ](</vi/start/onboarding>)

## Ví dụ

bashCopy code
[code]
    openclaw onboardopenclaw onboard --modernopenclaw onboard --flow quickstartopenclaw onboard --flow manualopenclaw onboard --flow importopenclaw onboard --import-from hermes --import-source ~/.hermesopenclaw onboard --skip-bootstrapopenclaw onboard --mode remote --remote-url wss://gateway-host:18789
[/code]

`--flow import` dùng các nhà cung cấp di trú do Plugin sở hữu, chẳng hạn như Hermes. Lệnh này chỉ chạy với một thiết lập OpenClaw mới; nếu đã có cấu hình, thông tin xác thực, phiên hoặc tệp bộ nhớ/định danh không gian làm việc, hãy đặt lại hoặc chọn một thiết lập mới trước khi nhập.

`--modern` khởi động bản xem trước thiết lập ban đầu dạng hội thoại Crestodian. Nếu không có `--modern`, `openclaw onboard` giữ luồng thiết lập ban đầu cổ điển.

Đối với các đích `ws://` dạng văn bản thuần trên mạng riêng (chỉ dành cho mạng đáng tin cậy), hãy đặt `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` trong môi trường tiến trình thiết lập ban đầu. Không có mục tương đương trong `openclaw.json` cho cơ chế phá kính khẩn cấp của truyền tải phía máy khách này.

Nhà cung cấp tùy chỉnh không tương tác:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --secret-input-mode plaintext \  --custom-compatibility openai \  --custom-image-input
[/code]

`--custom-api-key` là tùy chọn trong chế độ không tương tác. Nếu bỏ qua, thiết lập ban đầu sẽ kiểm tra `CUSTOM_API_KEY`. OpenClaw tự động đánh dấu các ID mô hình thị giác phổ biến là có khả năng xử lý hình ảnh. Truyền `--custom-image-input` cho các ID thị giác tùy chỉnh chưa biết, hoặc `--custom-text-input` để buộc siêu dữ liệu chỉ văn bản.

LM Studio cũng hỗ trợ cờ khóa riêng cho nhà cung cấp trong chế độ không tương tác:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice lmstudio \  --custom-base-url "http://localhost:1234/v1" \  --custom-model-id "qwen/qwen3.5-9b" \  --lmstudio-api-key "$LM_API_TOKEN" \  --accept-risk
[/code]

Ollama không tương tác:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice ollama \  --custom-base-url "http://ollama-host:11434" \  --custom-model-id "qwen3.5:27b" \  --accept-risk
[/code]

`--custom-base-url` mặc định là `http://127.0.0.1:11434`. `--custom-model-id` là tùy chọn; nếu bỏ qua, thiết lập ban đầu dùng các mặc định do Ollama đề xuất. Các ID mô hình đám mây như `kimi-k2.5:cloud` cũng hoạt động ở đây.

Lưu khóa nhà cung cấp dưới dạng tham chiếu thay vì văn bản thuần:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

Với `--secret-input-mode ref`, thiết lập ban đầu ghi các tham chiếu dựa trên env thay vì giá trị khóa văn bản thuần. Đối với các nhà cung cấp dựa trên auth-profile, thao tác này ghi các mục `keyRef`; đối với nhà cung cấp tùy chỉnh, thao tác này ghi `models.providers.<id>.apiKey` dưới dạng tham chiếu env (ví dụ `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`).

Hợp đồng chế độ `ref` không tương tác:

  * Đặt biến env của nhà cung cấp trong môi trường tiến trình thiết lập ban đầu (ví dụ `OPENAI_API_KEY`).
  * Không truyền cờ khóa nội tuyến (ví dụ `--openai-api-key`) trừ khi biến env đó cũng được đặt.
  * Nếu một cờ khóa nội tuyến được truyền mà không có biến env bắt buộc, thiết lập ban đầu sẽ thất bại nhanh kèm hướng dẫn.


Tùy chọn token Gateway trong chế độ không tương tác:

  * `--gateway-auth token --gateway-token <token>` lưu một token văn bản thuần.
  * `--gateway-auth token --gateway-token-ref-env <name>` lưu `gateway.auth.token` dưới dạng SecretRef env.
  * `--gateway-token` và `--gateway-token-ref-env` loại trừ lẫn nhau.
  * `--gateway-token-ref-env` yêu cầu một biến env không rỗng trong môi trường tiến trình thiết lập ban đầu.
  * Với `--install-daemon`, khi xác thực token yêu cầu token, các token Gateway do SecretRef quản lý được xác thực nhưng không được lưu bền dưới dạng văn bản thuần đã phân giải trong siêu dữ liệu môi trường dịch vụ supervisor.
  * Với `--install-daemon`, nếu chế độ token yêu cầu token và SecretRef token đã cấu hình không phân giải được, thiết lập ban đầu sẽ đóng thất bại kèm hướng dẫn khắc phục.
  * Với `--install-daemon`, nếu cả `gateway.auth.token` và `gateway.auth.password` đều được cấu hình và `gateway.auth.mode` chưa được đặt, thiết lập ban đầu sẽ chặn cài đặt cho đến khi chế độ được đặt rõ ràng.
  * Thiết lập ban đầu cục bộ ghi `gateway.mode="local"` vào cấu hình. Nếu một tệp cấu hình sau này thiếu `gateway.mode`, hãy xem đó là cấu hình bị hỏng hoặc chỉnh sửa thủ công chưa hoàn chỉnh, không phải là lối tắt chế độ cục bộ hợp lệ.
  * Thiết lập ban đầu cục bộ cài đặt các Plugin có thể tải xuống đã chọn khi đường dẫn thiết lập được chọn yêu cầu chúng.
  * Thiết lập ban đầu từ xa chỉ ghi thông tin kết nối cho Gateway từ xa và không cài đặt các gói Plugin cục bộ.
  * `--allow-unconfigured` là một cửa thoát riêng cho runtime Gateway. Điều đó không có nghĩa là thiết lập ban đầu có thể bỏ qua `gateway.mode`.


Ví dụ:

bashCopy code
[code]
    export OPENCLAW_GATEWAY_TOKEN="your-token"openclaw onboard --non-interactive \  --mode local \  --auth-choice skip \  --gateway-auth token \  --gateway-token-ref-env OPENCLAW_GATEWAY_TOKEN \  --accept-risk
[/code]

Tình trạng Gateway cục bộ không tương tác:

  * Trừ khi bạn truyền `--skip-health`, thiết lập ban đầu sẽ chờ một Gateway cục bộ có thể truy cập được trước khi thoát thành công.
  * `--install-daemon` khởi động đường dẫn cài đặt Gateway được quản lý trước. Nếu không có cờ này, bạn phải đã có một Gateway cục bộ đang chạy, ví dụ `openclaw gateway run`.
  * Nếu trong tự động hóa bạn chỉ muốn ghi cấu hình/không gian làm việc/bootstrap, hãy dùng `--skip-health`.
  * Nếu bạn tự quản lý tệp không gian làm việc, hãy truyền `--skip-bootstrap` để đặt `agents.defaults.skipBootstrap: true` và bỏ qua việc tạo `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md`, và `BOOTSTRAP.md`.
  * Trên Windows gốc, `--install-daemon` thử Scheduled Tasks trước và chuyển sang mục đăng nhập Startup-folder theo từng người dùng nếu việc tạo tác vụ bị từ chối.


Hành vi thiết lập ban đầu tương tác với chế độ tham chiếu:

  * Chọn **Dùng tham chiếu bí mật** khi được nhắc.
  * Sau đó chọn một trong hai: 
    * Biến môi trường
    * Nhà cung cấp bí mật đã cấu hình (`file` hoặc `exec`)
  * Thiết lập ban đầu thực hiện xác thực preflight nhanh trước khi lưu tham chiếu. 
    * Nếu xác thực thất bại, thiết lập ban đầu hiển thị lỗi và cho phép bạn thử lại.


### Lựa chọn endpoint [Z.AI](<http://Z.AI>) không tương tác

bashCopy code
[code]
    # Promptless endpoint selectionopenclaw onboard --non-interactive \  --auth-choice zai-coding-global \  --zai-api-key "$ZAI_API_KEY" # Other Z.AI endpoint choices:# --auth-choice zai-coding-cn# --auth-choice zai-global# --auth-choice zai-cn
[/code]

Ví dụ Mistral không tương tác:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY"
[/code]

## Ghi chú về luồng

Loại luồng

  * `quickstart`: lời nhắc tối thiểu, tự động tạo token Gateway.
  * `manual`: lời nhắc đầy đủ cho cổng, bind và xác thực (bí danh của `advanced`).
  * `import`: chạy một nhà cung cấp di trú đã phát hiện, xem trước kế hoạch, rồi áp dụng sau khi xác nhận.

Lọc trước nhà cung cấp

Khi một lựa chọn xác thực ngụ ý nhà cung cấp ưu tiên, thiết lập ban đầu lọc trước các bộ chọn mô hình mặc định và allowlist theo nhà cung cấp đó. Đối với Volcengine và BytePlus, điều này cũng khớp với các biến thể coding-plan (`volcengine-plan/*`, `byteplus-plan/*`).

Nếu bộ lọc nhà cung cấp ưu tiên chưa trả về mô hình đã tải nào, thiết lập ban đầu sẽ quay về danh mục chưa lọc thay vì để bộ chọn trống.

Theo dõi tìm kiếm web

Một số nhà cung cấp tìm kiếm web kích hoạt các lời nhắc theo dõi riêng cho nhà cung cấp:

  * **Grok** có thể cung cấp thiết lập `x_search` tùy chọn với cùng `XAI_API_KEY` và lựa chọn mô hình `x_search`.
  * **Kimi** có thể hỏi vùng API Moonshot (`api.moonshot.ai` so với `api.moonshot.cn`) và mô hình tìm kiếm web Kimi mặc định.

Hành vi khác

  * Hành vi phạm vi DM của thiết lập ban đầu cục bộ: [Tham chiếu thiết lập CLI](</vi/start/wizard-cli-reference#outputs-and-internals>).
  * Cuộc trò chuyện đầu tiên nhanh nhất: `openclaw dashboard` (Control UI, không cần thiết lập kênh).
  * Nhà cung cấp tùy chỉnh: kết nối bất kỳ endpoint tương thích OpenAI hoặc Anthropic nào, bao gồm các nhà cung cấp được lưu trữ không được liệt kê. Dùng Unknown để tự động phát hiện.
  * Nếu phát hiện trạng thái Hermes, thiết lập ban đầu sẽ cung cấp luồng di trú. Dùng [Di trú](</vi/cli/migrate>) cho kế hoạch chạy thử, chế độ ghi đè, báo cáo và ánh xạ chính xác.


## Lệnh theo dõi thường dùng

bashCopy code
[code]
    openclaw channels addopenclaw configureopenclaw agents add <name>
[/code]

Dùng `openclaw setup` thay thế khi bạn chỉ cần cấu hình/không gian làm việc cơ sở. Dùng `openclaw configure` sau đó cho các thay đổi có mục tiêu và `openclaw channels add` cho thiết lập chỉ kênh.

Was this useful?YesNo