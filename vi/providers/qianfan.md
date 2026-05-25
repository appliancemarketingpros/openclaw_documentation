---
title: Qianfan
source_url: https://docs.openclaw.ai/vi/providers/qianfan
scraped_at: 2026-05-25
---

Qianfan là nền tảng MaaS của Baidu, cung cấp một **API hợp nhất** định tuyến yêu cầu đến nhiều mô hình phía sau một endpoint và khóa API duy nhất. Nền tảng này tương thích với OpenAI, nên hầu hết OpenAI SDK hoạt động bằng cách chuyển đổi base URL.

Thuộc tính | Giá trị  
---|---  
Nhà cung cấp | `qianfan`  
Xác thực | `QIANFAN_API_KEY`  
API | Tương thích với OpenAI  
Base URL | `https://qianfan.baidubce.com/v2`  
  
## Bắt đầu

* ### Tạo tài khoản Baidu Cloud

Đăng ký hoặc đăng nhập tại [Qianfan Console](<https://console.bce.baidu.com/qianfan/ais/console/apiKey>) và đảm bảo bạn đã bật quyền truy cập Qianfan API.

* ### Tạo khóa API

Tạo một ứng dụng mới hoặc chọn một ứng dụng hiện có, sau đó tạo khóa API. Định dạng khóa là `bce-v3/ALTAK-...`.

* ### Chạy quy trình onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice qianfan-api-key
[/code]

* ### Xác minh mô hình có sẵn

bashCopy code
[code]
    openclaw models list --provider qianfan
[/code]

## Danh mục tích hợp sẵn

Tham chiếu mô hình | Đầu vào | Ngữ cảnh | Đầu ra tối đa | Suy luận | Ghi chú  
---|---|---|---|---|---  
`qianfan/deepseek-v3.2` | văn bản | 98,304 | 32,768 | Có | Mô hình mặc định  
`qianfan/ernie-5.0-thinking-preview` | văn bản, hình ảnh | 119,000 | 64,000 | Có | Đa phương thức  
  
## Ví dụ cấu hình

json5Copy code
[code]
    {  env: { QIANFAN_API_KEY: "bce-v3/ALTAK-..." },  agents: {    defaults: {      model: { primary: "qianfan/deepseek-v3.2" },      models: {        "qianfan/deepseek-v3.2": { alias: "QIANFAN" },      },    },  },  models: {    providers: {      qianfan: {        baseUrl: "https://qianfan.baidubce.com/v2",        api: "openai-completions",        models: [          {            id: "deepseek-v3.2",            name: "DEEPSEEK V3.2",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 98304,            maxTokens: 32768,          },          {            id: "ernie-5.0-thinking-preview",            name: "ERNIE-5.0-Thinking-Preview",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 119000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

Truyền tải và tương thích

Qianfan chạy qua đường truyền tải tương thích với OpenAI, không phải định dạng yêu cầu OpenAI gốc. Điều này nghĩa là các tính năng OpenAI SDK tiêu chuẩn hoạt động, nhưng tham số dành riêng cho nhà cung cấp có thể không được chuyển tiếp.

Danh mục và ghi đè

Danh mục tích hợp hiện bao gồm `deepseek-v3.2` và `ernie-5.0-thinking-preview`. Chỉ thêm hoặc ghi đè `models.providers.qianfan` khi bạn cần base URL tùy chỉnh hoặc metadata mô hình.

Khắc phục sự cố

  * Đảm bảo khóa API của bạn bắt đầu bằng `bce-v3/ALTAK-` và đã bật quyền truy cập Qianfan API trong bảng điều khiển Baidu Cloud.
  * Nếu mô hình không được liệt kê, hãy xác nhận tài khoản của bạn đã kích hoạt dịch vụ Qianfan.
  * Base URL mặc định là `https://qianfan.baidubce.com/v2`. Chỉ thay đổi nếu bạn dùng endpoint hoặc proxy tùy chỉnh.


## Liên quan

[**Lựa chọn mô hình** Chọn nhà cung cấp, tham chiếu mô hình và hành vi failover. ](</vi/concepts/model-providers>) [**Tham chiếu cấu hình** Tham chiếu cấu hình OpenClaw đầy đủ. ](</vi/gateway/configuration-reference>) [**Thiết lập agent** Cấu hình mặc định của agent và việc gán mô hình. ](</vi/concepts/agent>) [**Tài liệu Qianfan API** Tài liệu Qianfan API chính thức. ](<https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb>)

Was this useful?YesNo