---
title: Inferrs
source_url: https://docs.openclaw.ai/vi/providers/inferrs
scraped_at: 2026-05-25
---

[inferrs](<https://github.com/ericcurtin/inferrs>) có thể phục vụ các mô hình cục bộ phía sau API `/v1` tương thích với OpenAI. OpenClaw hoạt động với `inferrs` thông qua đường dẫn `openai-completions` chung.

Thuộc tính | Giá trị  
---|---  
ID nhà cung cấp | `inferrs` (tùy chỉnh; cấu hình trong `models.providers.inferrs`)  
Plugin | không có — `inferrs` không phải Plugin nhà cung cấp đi kèm OpenClaw  
Biến môi trường xác thực | Tùy chọn. Giá trị nào cũng hoạt động nếu máy chủ inferrs của bạn không có xác thực  
API | tương thích với OpenAI (`openai-completions`)  
URL cơ sở đề xuất | `http://127.0.0.1:8080/v1` (hoặc nơi máy chủ inferrs của bạn chạy)  
  
## Bắt đầu

* ### Khởi động inferrs với một mô hình

bashCopy code
[code]
    inferrs serve google/gemma-4-E2B-it \  --host 127.0.0.1 \  --port 8080 \  --device metal
[/code]

* ### Xác minh máy chủ có thể truy cập được

bashCopy code
[code]
    curl http://127.0.0.1:8080/healthcurl http://127.0.0.1:8080/v1/models
[/code]

* ### Thêm mục nhà cung cấp OpenClaw

Thêm một mục nhà cung cấp tường minh và trỏ mô hình mặc định của bạn tới mục đó. Xem ví dụ cấu hình đầy đủ bên dưới.

## Ví dụ cấu hình đầy đủ

Ví dụ này dùng Gemma 4 trên một máy chủ `inferrs` cục bộ.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },      models: {        "inferrs/google/gemma-4-E2B-it": {          alias: "Gemma 4 (inferrs)",        },      },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

## Khởi động theo yêu cầu

Inferrs cũng có thể được OpenClaw khởi động chỉ khi một mô hình `inferrs/...` được chọn. Thêm `localService` vào cùng mục nhà cung cấp:

json5Copy code
[code]
    {  models: {    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

`command` phải là đường dẫn tuyệt đối. Dùng `which inferrs` trên máy chủ Gateway và đặt đường dẫn đó vào cấu hình. Để xem tham chiếu đầy đủ về các trường, hãy xem [Dịch vụ mô hình cục bộ](</vi/gateway/local-model-services>).

## Cấu hình nâng cao

Vì sao requiresStringContent quan trọng

Một số tuyến Chat Completions của `inferrs` chỉ chấp nhận `messages[].content` dạng chuỗi, không chấp nhận mảng phần nội dung có cấu trúc.

json5Copy code
[code]
    compat: {  requiresStringContent: true}
[/code]

OpenClaw sẽ làm phẳng các phần nội dung văn bản thuần thành chuỗi đơn giản trước khi gửi yêu cầu.

Lưu ý về Gemma và lược đồ công cụ

Một số tổ hợp `inferrs` \+ Gemma hiện tại chấp nhận các yêu cầu `/v1/chat/completions` trực tiếp nhỏ nhưng vẫn thất bại trên các lượt agent-runtime đầy đủ của OpenClaw.

Nếu điều đó xảy ra, hãy thử cách này trước:

json5Copy code
[code]
    compat: {  requiresStringContent: true,  supportsTools: false}
[/code]

Cách đó vô hiệu hóa bề mặt lược đồ công cụ của OpenClaw cho mô hình và có thể giảm áp lực prompt lên các backend cục bộ nghiêm ngặt hơn.

Nếu các yêu cầu trực tiếp rất nhỏ vẫn hoạt động nhưng các lượt agent OpenClaw bình thường tiếp tục gặp sự cố bên trong `inferrs`, vấn đề còn lại thường là hành vi của mô hình/máy chủ upstream thay vì lớp truyền tải của OpenClaw.

Kiểm thử smoke thủ công

Sau khi cấu hình, hãy kiểm thử cả hai lớp:

bashCopy code
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
[/code]

bashCopy code
[code]
    openclaw infer model run \  --model inferrs/google/gemma-4-E2B-it \  --prompt "What is 2 + 2? Reply with one short sentence." \  --json
[/code]

Nếu lệnh đầu tiên hoạt động nhưng lệnh thứ hai thất bại, hãy kiểm tra phần xử lý sự cố bên dưới.

Hành vi kiểu proxy

`inferrs` được xử lý như một backend `/v1` kiểu proxy tương thích với OpenAI, không phải một endpoint OpenAI gốc.

  * Định hình yêu cầu chỉ dành cho OpenAI gốc không áp dụng ở đây
  * Không có `service_tier`, không có Responses `store`, không có gợi ý prompt-cache, và không có định hình payload tương thích với reasoning của OpenAI
  * Các header quy thuộc OpenClaw ẩn (`originator`, `version`, `User-Agent`) không được chèn trên các URL cơ sở `inferrs` tùy chỉnh


## Xử lý sự cố

curl /v1/models thất bại

`inferrs` không chạy, không thể truy cập, hoặc không được bind vào host/port mong đợi. Hãy đảm bảo máy chủ đã được khởi động và đang lắng nghe tại địa chỉ bạn đã cấu hình.

messages[].content mong đợi một chuỗi

Đặt `compat.requiresStringContent: true` trong mục mô hình. Xem phần `requiresStringContent` ở trên để biết chi tiết.

Các lệnh gọi /v1/chat/completions trực tiếp thành công nhưng openclaw infer model run thất bại

Hãy thử đặt `compat.supportsTools: false` để vô hiệu hóa bề mặt lược đồ công cụ. Xem lưu ý về lược đồ công cụ của Gemma ở trên.

inferrs vẫn gặp sự cố trên các lượt agent lớn hơn

Nếu OpenClaw không còn gặp lỗi lược đồ nhưng `inferrs` vẫn gặp sự cố trên các lượt agent lớn hơn, hãy xem đó là giới hạn upstream của `inferrs` hoặc của mô hình. Giảm áp lực prompt hoặc chuyển sang một backend hay mô hình cục bộ khác.

## Liên quan

[**Mô hình cục bộ** Chạy OpenClaw với các máy chủ mô hình cục bộ. ](</vi/gateway/local-models>) [**Dịch vụ mô hình cục bộ** Khởi động máy chủ mô hình cục bộ theo yêu cầu cho các nhà cung cấp đã cấu hình. ](</vi/gateway/local-model-services>) [**Xử lý sự cố Gateway** Gỡ lỗi các backend cục bộ tương thích với OpenAI vượt qua probe nhưng thất bại khi chạy agent. ](</vi/gateway/troubleshooting#local-openai-compatible-backend-passes-direct-probes-but-agent-runs-fail>) [**Lựa chọn mô hình** Tổng quan về tất cả nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>)

Was this useful?YesNo