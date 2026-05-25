---
title: Amazon Bedrock Mantle
source_url: https://docs.openclaw.ai/vi/providers/bedrock-mantle
scraped_at: 2026-05-25
---

OpenClaw bao gồm nhà cung cấp **Amazon Bedrock Mantle** được tích hợp sẵn, kết nối tới điểm cuối tương thích OpenAI của Mantle. Mantle lưu trữ các mô hình mã nguồn mở và bên thứ ba (GPT-OSS, Qwen, Kimi, GLM và tương tự) thông qua bề mặt `/v1/chat/completions` tiêu chuẩn được hỗ trợ bởi hạ tầng Bedrock.

Thuộc tính | Giá trị  
---|---  
ID nhà cung cấp | `amazon-bedrock-mantle`  
API | `openai-completions` (tương thích OpenAI) hoặc `anthropic-messages` (tuyến Anthropic Messages)  
Xác thực | `AWS_BEARER_TOKEN_BEDROCK` rõ ràng hoặc tạo bearer-token từ chuỗi thông tin xác thực IAM  
Vùng mặc định | `us-east-1` (ghi đè bằng `AWS_REGION` hoặc `AWS_DEFAULT_REGION`)  
  
## Bắt đầu

Chọn phương thức xác thực bạn muốn và làm theo các bước thiết lập.

### Bearer token rõ ràng

**Phù hợp nhất cho:** các môi trường nơi bạn đã có bearer token Mantle.

* ### Đặt bearer token trên máy chủ gateway

bashCopy code
[code]
    export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

Tùy chọn đặt một vùng (mặc định là `us-east-1`):

bashCopy code
[code]
    export AWS_REGION="us-west-2"
[/code]

* ### Xác minh các mô hình đã được phát hiện

bashCopy code
[code]
    openclaw models list
[/code]

Các mô hình được phát hiện xuất hiện dưới nhà cung cấp `amazon-bedrock-mantle`. Không cần cấu hình bổ sung trừ khi bạn muốn ghi đè các mặc định.

### Thông tin xác thực IAM

**Phù hợp nhất cho:** sử dụng thông tin xác thực tương thích AWS SDK (cấu hình chia sẻ, SSO, web identity, vai trò instance hoặc task).

* ### Cấu hình thông tin xác thực AWS trên máy chủ gateway

Mọi nguồn xác thực tương thích AWS SDK đều hoạt động:

bashCopy code
[code]
    export AWS_PROFILE="default"export AWS_REGION="us-west-2"
[/code]

* ### Xác minh các mô hình đã được phát hiện

bashCopy code
[code]
    openclaw models list
[/code]

OpenClaw tự động tạo bearer token Mantle từ chuỗi thông tin xác thực.

## Tự động phát hiện mô hình

Khi `AWS_BEARER_TOKEN_BEDROCK` được đặt, OpenClaw dùng trực tiếp token đó. Nếu không, OpenClaw cố gắng tạo bearer token Mantle từ chuỗi thông tin xác thực mặc định của AWS. Sau đó, OpenClaw phát hiện các mô hình Mantle khả dụng bằng cách truy vấn điểm cuối `/v1/models` của vùng.

Hành vi | Chi tiết  
---|---  
Bộ nhớ đệm phát hiện | Kết quả được lưu trong bộ nhớ đệm trong 1 giờ  
Làm mới token IAM | Hằng giờ  
  
Để giữ Plugin Mantle được bật nhưng chặn việc tự động phát hiện và tạo bearer-token IAM, hãy tắt công tắc phát hiện do Plugin sở hữu:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock-mantle.config.discovery.enabled false
[/code]

### Các vùng được hỗ trợ

`us-east-1`, `us-east-2`, `us-west-2`, `ap-northeast-1`, `ap-south-1`, `ap-southeast-3`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-south-1`, `eu-north-1`, `sa-east-1`.

## Cấu hình thủ công

Nếu bạn muốn dùng cấu hình rõ ràng thay vì tự động phát hiện:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        baseUrl: "https://bedrock-mantle.us-east-1.api.aws/v1",        api: "openai-completions",        auth: "api-key",        apiKey: "env:AWS_BEARER_TOKEN_BEDROCK",        models: [          {            id: "gpt-oss-120b",            name: "GPT-OSS 120B",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## Cấu hình nâng cao

Hỗ trợ reasoning

Hỗ trợ reasoning được suy ra từ ID mô hình chứa các mẫu như `thinking`, `reasoner` hoặc `gpt-oss-120b`. OpenClaw tự động đặt `reasoning: true` cho các mô hình khớp trong quá trình phát hiện.

Điểm cuối không khả dụng

Nếu điểm cuối Mantle không khả dụng hoặc không trả về mô hình nào, nhà cung cấp sẽ được bỏ qua âm thầm. OpenClaw không báo lỗi; các nhà cung cấp đã cấu hình khác tiếp tục hoạt động bình thường.

Claude Opus 4.7 qua tuyến Anthropic Messages

Mantle cũng cung cấp một tuyến Anthropic Messages để truyền các mô hình Claude qua cùng đường dẫn phát trực tuyến được xác thực bằng bearer. Claude Opus 4.7 (`amazon-bedrock-mantle/claude-opus-4.7`) có thể được gọi qua tuyến này với streaming do nhà cung cấp sở hữu, vì vậy bearer token AWS không được xử lý như khóa API Anthropic.

Khi bạn ghim một mô hình Anthropic Messages trên nhà cung cấp Mantle, OpenClaw sử dụng bề mặt API `anthropic-messages` thay vì `openai-completions` cho mô hình đó. Xác thực vẫn đến từ `AWS_BEARER_TOKEN_BEDROCK` (hoặc bearer token IAM được tạo).

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        models: [          {            id: "claude-opus-4.7",            name: "Claude Opus 4.7",            api: "anthropic-messages",            reasoning: true,            input: ["text", "image"],            contextWindow: 1000000,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Quan hệ với nhà cung cấp Amazon Bedrock

Bedrock Mantle là một nhà cung cấp riêng biệt với nhà cung cấp [Amazon Bedrock](</vi/providers/bedrock>) tiêu chuẩn. Mantle sử dụng một bề mặt `/v1` tương thích OpenAI, trong khi nhà cung cấp Bedrock tiêu chuẩn sử dụng API Bedrock gốc.

Cả hai nhà cung cấp dùng chung cùng thông tin xác thực `AWS_BEARER_TOKEN_BEDROCK` khi có mặt.

## Liên quan

[**Amazon Bedrock** Nhà cung cấp Bedrock gốc cho Anthropic Claude, Titan và các mô hình khác. ](</vi/providers/bedrock>) [**Chọn mô hình** Chọn nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**OAuth và xác thực** Chi tiết xác thực và quy tắc tái sử dụng thông tin xác thực. ](</vi/gateway/authentication>) [**Khắc phục sự cố** Các vấn đề thường gặp và cách giải quyết. ](</vi/help/troubleshooting>)

Was this useful?YesNo