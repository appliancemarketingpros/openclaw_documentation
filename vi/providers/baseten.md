---
title: Baseten
source_url: https://docs.openclaw.ai/vi/providers/baseten
scraped_at: 2026-07-20
---

Get started

[API Mô hình Baseten](<https://docs.baseten.co/inference/model-apis/overview>) cung cấp quyền truy cập được lưu trữ, tương thích với OpenAI vào các mô hình tiên tiến. Plugin bên ngoài chính thức sử dụng cơ chế khám phá có xác thực, vì vậy OpenClaw sử dụng toàn bộ tập hợp mô hình được bật cho tài khoản Baseten của bạn. Phương án dự phòng ngoại tuyến của Plugin chứa mọi API Mô hình có sẵn tại thời điểm bản phát hành OpenClaw này được xây dựng.

Thuộc tính | Giá trị  
---|---  
ID nhà cung cấp | `baseten`  
Plugin | gói bên ngoài chính thức (`@openclaw/baseten-provider`)  
Biến môi trường xác thực | `BASETEN_API_KEY`  
Cờ thiết lập ban đầu | `--auth-choice baseten-api-key`  
Cờ CLI trực tiếp | `--baseten-api-key <key>`  
API | tương thích với OpenAI (`openai-completions`)  
URL cơ sở | `https://inference.baseten.co/v1`  
Mô hình mặc định | `baseten/thinkingmachines/inkling`  
  
## Cài đặt Plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/baseten-provideropenclaw gateway restart
[/code]

## Bắt đầu

* ### Tạo tài khoản Baseten và khóa API

Gói Basic của Baseten không có phí nền tảng hằng tháng; các lệnh gọi API Mô hình được tính phí theo mức sử dụng. Tạo khóa trong [phần cài đặt khóa API Baseten](<https://app.baseten.co/settings/api_keys>) và kiểm tra mức giá hiện tại trên [trang giá](<https://www.baseten.co/pricing>).

* ### Chạy quy trình thiết lập ban đầu

Thiết lập ban đầuCopy code
[code]
    openclaw onboard --auth-choice baseten-api-key
[/code]

Cờ trực tiếpCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice baseten-api-key \--baseten-api-key "$BASETEN_API_KEY"
[/code]

Chỉ dùng biến môi trườngCopy code
[code]
    export BASETEN_API_KEY=...
[/code]

* ### Xác minh danh mục trực tiếp

bashCopy code
[code]
    openclaw models list --provider baseten
[/code]

Khi có thông tin xác thực hợp lệ, Plugin yêu cầu `GET /v1/models` và liệt kê mọi mô hình được trả về cho tài khoản. Khi không có thông tin xác thực, Plugin vẫn ở chế độ ngoại tuyến và sử dụng phương án dự phòng đi kèm.

## Inkling

[Inkling của Thinking Machines Lab](<https://thinkingmachines.ai/news/introducing-inkling/>) là mô hình mặc định. Trong OpenClaw, mô hình này hỗ trợ đầu vào văn bản và hình ảnh, gọi công cụ, lược đồ công cụ có cấu trúc, mức độ suy luận có thể cấu hình, cửa sổ ngữ cảnh 1.048M token và tối đa 32k token đầu ra:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "baseten/thinkingmachines/inkling" },    },  },}
[/code]

Sử dụng `/model baseten/thinkingmachines/inkling` để chuyển đổi một cuộc trò chuyện hiện có.

## Danh mục dự phòng đi kèm

Danh mục trực tiếp đã xác thực là nguồn có thẩm quyền. Các hàng này giúp quy trình thiết lập và lựa chọn mô hình vẫn hữu ích trước khi quá trình khám phá thành công:

Tham chiếu mô hình | Đầu vào | Ngữ cảnh | Đầu ra tối đa  
---|---|---|---  
`baseten/deepseek-ai/DeepSeek-V4-Pro` | văn bản | 262k | 262k  
`baseten/zai-org/GLM-4.7` | văn bản | 200k | 200k  
`baseten/zai-org/GLM-5` | văn bản | 202k | 202k  
`baseten/zai-org/GLM-5.1` | văn bản | 202k | 202k  
`baseten/zai-org/GLM-5.2` | văn bản | 202k | 202k  
`baseten/thinkingmachines/inkling` | văn bản, hình ảnh | 1.048M | 32k  
`baseten/moonshotai/Kimi-K2.5` | văn bản, hình ảnh | 262k | 262k  
`baseten/moonshotai/Kimi-K2.6` | văn bản, hình ảnh | 262k | 262k  
`baseten/moonshotai/Kimi-K2.7-Code` | văn bản, hình ảnh | 262k | 262k  
`baseten/nvidia/Nemotron-120B-A12B` | văn bản | 202k | 202k  
`baseten/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B` | văn bản | 202k | 202k  
`baseten/openai/gpt-oss-120b` | văn bản | 128k | 128k  
  
Tất cả mô hình đi kèm đều hỗ trợ gọi công cụ và suy luận. OpenClaw ánh xạ các cấp độ tư duy của mình sang những mô hình có `reasoning_effort` gốc. Các mô hình GLM, Kimi và Nemotron cần chủ động bật của Baseten mặc định tắt chế độ tư duy; phần lớn cung cấp chế độ điều khiển nhị phân tắt/bật, còn GLM 5.2 cung cấp các mức tắt, cao và tối đa. OpenClaw gửi các lựa chọn này qua cơ chế điều khiển `chat_template_args.enable_thinking` của Baseten và, đối với GLM 5.2, qua tham số cấp cao nhất `reasoning_effort` đã được xác thực.

## Cấu hình thủ công

Hầu hết quy trình thiết lập chỉ cần khóa API. Để chỉ định rõ nhà cung cấp:

json5Copy code
[code]
    {  env: { BASETEN_API_KEY: "..." },  agents: {    defaults: {      model: { primary: "baseten/thinkingmachines/inkling" },    },  },  models: {    mode: "merge",    providers: {      baseten: {        baseUrl: "https://inference.baseten.co/v1",        apiKey: "${BASETEN_API_KEY}",        api: "openai-completions",        models: [          {            id: "thinkingmachines/inkling",            name: "Inkling",            reasoning: true,            input: ["text", "image"],            contextWindow: 1048000,            maxTokens: 32000,            compat: {              supportsStore: false,              supportsDeveloperRole: false,              supportsUsageInStreaming: true,              supportsStrictMode: true,              supportsTools: true,              supportsReasoningEffort: true,              supportedReasoningEfforts: ["none", "minimal", "low", "medium", "high", "xhigh"],              reasoningEffortMap: {                off: "none",                none: "none",                adaptive: "xhigh",                max: "xhigh",              },              maxTokensField: "max_tokens",            },          },        ],      },    },  },}
[/code]

## Liên quan

[**Nhà cung cấp mô hình** Lựa chọn nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Chế độ tư duy** Chọn các mức độ suy luận của OpenClaw. ](</vi/tools/thinking>) [**CLI mô hình** Liệt kê, kiểm tra và chọn các mô hình đã được khám phá. ](</vi/cli/models>) [**Câu hỏi thường gặp về mô hình** Khắc phục sự cố về hồ sơ xác thực và lựa chọn mô hình. ](</vi/help/faq-models>)

Was this useful?YesNo

Open issue