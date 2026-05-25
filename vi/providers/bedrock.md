---
title: Amazon Bedrock
source_url: https://docs.openclaw.ai/vi/providers/bedrock
scraped_at: 2026-05-25
---

OpenClaw có thể sử dụng các mô hình **Amazon Bedrock** thông qua nhà cung cấp phát trực tuyến **Bedrock Converse** của pi-ai. Xác thực Bedrock sử dụng **chuỗi thông tin xác thực mặc định của AWS SDK** , không phải khóa API.

Thuộc tính | Giá trị  
---|---  
Nhà cung cấp | `amazon-bedrock`  
API | `bedrock-converse-stream`  
Xác thực | Thông tin xác thực AWS (biến môi trường, cấu hình dùng chung hoặc vai trò phiên bản)  
Vùng | `AWS_REGION` hoặc `AWS_DEFAULT_REGION` (mặc định: `us-east-1`)  
  
## Bắt đầu

Chọn phương thức xác thực bạn muốn dùng và làm theo các bước thiết lập.

### Khóa truy cập / biến môi trường

**Phù hợp nhất cho:** máy của nhà phát triển, CI hoặc các máy chủ nơi bạn trực tiếp quản lý thông tin xác thực AWS.

* ### Thiết lập thông tin xác thực AWS trên máy chủ gateway

bashCopy code
[code]
    export AWS_ACCESS_KEY_ID="AKIA..."export AWS_SECRET_ACCESS_KEY="..."export AWS_REGION="us-east-1"# Optional:export AWS_SESSION_TOKEN="..."export AWS_PROFILE="your-profile"# Optional (Bedrock API key/bearer token):export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

* ### Thêm nhà cung cấp Bedrock và mô hình vào cấu hình của bạn

Không cần `apiKey`. Cấu hình nhà cung cấp với `auth: "aws-sdk"`:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock": {        baseUrl: "https://bedrock-runtime.us-east-1.amazonaws.com",        api: "bedrock-converse-stream",        auth: "aws-sdk",        models: [          {            id: "us.anthropic.claude-opus-4-6-v1:0",            name: "Claude Opus 4.6 (Bedrock)",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 200000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "amazon-bedrock/us.anthropic.claude-opus-4-6-v1:0" },    },  },}
[/code]

* ### Xác minh các mô hình có sẵn

bashCopy code
[code]
    openclaw models list
[/code]

### Vai trò phiên bản EC2 (IMDS)

**Phù hợp nhất cho:** các phiên bản EC2 có gắn vai trò IAM, sử dụng dịch vụ siêu dữ liệu phiên bản để xác thực.

* ### Bật khám phá một cách rõ ràng

Khi dùng IMDS, OpenClaw không thể phát hiện xác thực AWS chỉ từ các dấu hiệu môi trường, nên bạn phải chọn tham gia:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1
[/code]

* ### Tùy chọn thêm dấu hiệu môi trường cho chế độ tự động

Nếu bạn cũng muốn đường dẫn tự động phát hiện bằng dấu hiệu môi trường hoạt động (ví dụ: cho các bề mặt `openclaw status`):

bashCopy code
[code]
    export AWS_PROFILE=defaultexport AWS_REGION=us-east-1
[/code]

Bạn **không** cần khóa API giả.

* ### Xác minh các mô hình được khám phá

bashCopy code
[code]
    openclaw models list
[/code]

## Khám phá mô hình tự động

OpenClaw có thể tự động khám phá các mô hình Bedrock hỗ trợ **phát trực tuyến** và **đầu ra văn bản**. Quá trình khám phá sử dụng `bedrock:ListFoundationModels` và `bedrock:ListInferenceProfiles`, và kết quả được lưu vào bộ nhớ đệm (mặc định: 1 giờ).

Cách bật nhà cung cấp ngầm định:

  * Nếu `plugins.entries.amazon-bedrock.config.discovery.enabled` là `true`, OpenClaw sẽ thử khám phá ngay cả khi không có dấu hiệu môi trường AWS nào.
  * Nếu `plugins.entries.amazon-bedrock.config.discovery.enabled` chưa được đặt, OpenClaw chỉ tự động thêm nhà cung cấp Bedrock ngầm định khi phát hiện một trong các dấu hiệu xác thực AWS sau: `AWS_BEARER_TOKEN_BEDROCK`, `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`, hoặc `AWS_PROFILE`.
  * Đường dẫn xác thực runtime Bedrock thực tế vẫn dùng chuỗi mặc định của AWS SDK, vì vậy cấu hình dùng chung, SSO và xác thực vai trò phiên bản IMDS vẫn có thể hoạt động ngay cả khi bước khám phá cần `enabled: true` để chọn tham gia.


Tùy chọn cấu hình khám phá

Các tùy chọn cấu hình nằm trong `plugins.entries.amazon-bedrock.config.discovery`:

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          discovery: {            enabled: true,            region: "us-east-1",            providerFilter: ["anthropic", "amazon"],            refreshInterval: 3600,            defaultContextWindow: 32000,            defaultMaxTokens: 4096,          },        },      },    },  },}
[/code]

Tùy chọn | Mặc định | Mô tả  
---|---|---  
`enabled` | tự động | Ở chế độ tự động, OpenClaw chỉ bật nhà cung cấp Bedrock ngầm định khi phát hiện một dấu hiệu môi trường AWS được hỗ trợ. Đặt `true` để buộc khám phá.  
`region` | `AWS_REGION` / `AWS_DEFAULT_REGION` / `us-east-1` | Vùng AWS dùng cho các lệnh gọi API khám phá.  
`providerFilter` | (tất cả) | Khớp tên nhà cung cấp Bedrock (ví dụ `anthropic`, `amazon`).  
`refreshInterval` | `3600` | Thời lượng bộ nhớ đệm tính bằng giây. Đặt thành `0` để tắt bộ nhớ đệm.  
`defaultContextWindow` | `32000` | Cửa sổ ngữ cảnh dùng cho các mô hình được khám phá (ghi đè nếu bạn biết giới hạn mô hình của mình).  
`defaultMaxTokens` | `4096` | Số token đầu ra tối đa dùng cho các mô hình được khám phá (ghi đè nếu bạn biết giới hạn mô hình của mình).  
  
## Thiết lập nhanh (đường dẫn AWS)

Hướng dẫn này tạo một vai trò IAM, đính kèm quyền Bedrock, liên kết hồ sơ phiên bản và bật khám phá OpenClaw trên máy chủ EC2.

bashCopy code
[code]
    # 1. Create IAM role and instance profileaws iam create-role --role-name EC2-Bedrock-Access \  --assume-role-policy-document '{    "Version": "2012-10-17",    "Statement": [{      "Effect": "Allow",      "Principal": {"Service": "ec2.amazonaws.com"},      "Action": "sts:AssumeRole"    }]  }' aws iam attach-role-policy --role-name EC2-Bedrock-Access \  --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess aws iam create-instance-profile --instance-profile-name EC2-Bedrock-Accessaws iam add-role-to-instance-profile \  --instance-profile-name EC2-Bedrock-Access \  --role-name EC2-Bedrock-Access # 2. Attach to your EC2 instanceaws ec2 associate-iam-instance-profile \  --instance-id i-xxxxx \  --iam-instance-profile Name=EC2-Bedrock-Access # 3. On the EC2 instance, enable discovery explicitlyopenclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1 # 4. Optional: add an env marker if you want auto mode without explicit enableecho 'export AWS_PROFILE=default' >> ~/.bashrcecho 'export AWS_REGION=us-east-1' >> ~/.bashrcsource ~/.bashrc # 5. Verify models are discoveredopenclaw models list
[/code]

## Cấu hình nâng cao

Hồ sơ suy luận

OpenClaw khám phá **hồ sơ suy luận khu vực và toàn cầu** cùng với các mô hình nền tảng. Khi một hồ sơ ánh xạ đến một mô hình nền tảng đã biết, hồ sơ sẽ kế thừa các khả năng của mô hình đó (cửa sổ ngữ cảnh, token tối đa, suy luận, thị giác) và vùng yêu cầu Bedrock chính xác được chèn tự động. Điều này có nghĩa là các hồ sơ Claude liên vùng hoạt động mà không cần ghi đè nhà cung cấp thủ công.

ID hồ sơ suy luận có dạng `us.anthropic.claude-opus-4-6-v1:0` (khu vực) hoặc `anthropic.claude-opus-4-6-v1:0` (toàn cầu). Nếu mô hình nền bên dưới đã có trong kết quả khám phá, hồ sơ sẽ kế thừa toàn bộ tập khả năng của mô hình; nếu không, các giá trị mặc định an toàn sẽ được áp dụng.

Không cần cấu hình bổ sung. Miễn là khám phá được bật và chủ thể IAM có `bedrock:ListInferenceProfiles`, các hồ sơ sẽ xuất hiện cùng với các mô hình nền tảng trong `openclaw models list`.

Cấp dịch vụ

Một số mô hình Bedrock hỗ trợ tham số `service_tier` để tối ưu hóa chi phí hoặc độ trễ. Các cấp sau có sẵn:

Cấp | Mô tả  
---|---  
`default` | Cấp Bedrock tiêu chuẩn  
`flex` | Xử lý giảm giá cho khối lượng công việc có thể chấp nhận độ trễ dài hơn  
`priority` | Xử lý ưu tiên cho khối lượng công việc nhạy cảm với độ trễ  
`reserved` | Dung lượng dành riêng cho khối lượng công việc ổn định  
  
Đặt `serviceTier` (hoặc `service_tier`) qua `agents.defaults.params` cho các yêu cầu mô hình Bedrock, hoặc theo từng mô hình trong `agents.defaults.models["<model-key>"].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      params: {        serviceTier: "flex", // applies to all models      },      models: {        "amazon-bedrock/mistral.mistral-large-3-675b-instruct": {          params: {            serviceTier: "priority", // per-model override          },        },      },    },  },}
[/code]

Các giá trị hợp lệ là `default`, `flex`, `priority` và `reserved`. Không phải mô hình nào cũng hỗ trợ mọi cấp — nếu yêu cầu một cấp không được hỗ trợ, Bedrock sẽ trả về lỗi xác thực. Lưu ý: thông báo lỗi có phần gây hiểu nhầm; nó có thể nói "The provided model identifier is invalid" thay vì chỉ ra một cấp dịch vụ không được hỗ trợ. Nếu bạn thấy lỗi này, hãy kiểm tra xem mô hình có hỗ trợ cấp được yêu cầu hay không.

Nhiệt độ Claude Opus 4.7

Bedrock từ chối tham số `temperature` cho Claude Opus 4.7. OpenClaw tự động bỏ qua `temperature` cho bất kỳ tham chiếu Bedrock Opus 4.7 nào, bao gồm ID mô hình nền tảng, hồ sơ suy luận được đặt tên, hồ sơ suy luận ứng dụng có mô hình bên dưới phân giải thành Opus 4.7 qua `bedrock:GetInferenceProfile`, và các biến thể `opus-4.7` dạng dấu chấm có tiền tố vùng tùy chọn (`us.`, `eu.`, `ap.`, `apac.`, `au.`, `jp.`, `global.`). Không cần nút cấu hình nào, và việc bỏ qua áp dụng cho cả đối tượng tùy chọn yêu cầu lẫn trường tải trọng `inferenceConfig`.

Guardrails

Bạn có thể áp dụng [Amazon Bedrock Guardrails](<https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>) cho mọi lần gọi mô hình Bedrock bằng cách thêm đối tượng `guardrail` vào cấu hình Plugin `amazon-bedrock`. Guardrails cho phép bạn thực thi lọc nội dung, từ chối chủ đề, bộ lọc từ, bộ lọc thông tin nhạy cảm và kiểm tra nền tảng ngữ cảnh.

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          guardrail: {            guardrailIdentifier: "abc123", // guardrail ID or full ARN            guardrailVersion: "1", // version number or "DRAFT"            streamProcessingMode: "sync", // optional: "sync" or "async"            trace: "enabled", // optional: "enabled", "disabled", or "enabled_full"          },        },      },    },  },}
[/code]

Tùy chọn | Bắt buộc | Mô tả  
---|---|---  
`guardrailIdentifier` | Có | ID Guardrail (ví dụ `abc123`) hoặc ARN đầy đủ (ví dụ `arn:aws:bedrock:us-east-1:123456789012:guardrail/abc123`).  
`guardrailVersion` | Có | Số phiên bản đã phát hành, hoặc `"DRAFT"` cho bản nháp đang làm việc.  
`streamProcessingMode` | Không | `"sync"` hoặc `"async"` để đánh giá guardrail trong khi truyền phát. Nếu bỏ qua, Bedrock dùng mặc định của nó.  
`trace` | Không | `"enabled"` hoặc `"enabled_full"` để gỡ lỗi; bỏ qua hoặc đặt `"disabled"` cho môi trường sản xuất.  
Embedding cho tìm kiếm bộ nhớ

Bedrock cũng có thể đóng vai trò là nhà cung cấp embedding cho [tìm kiếm bộ nhớ](</vi/concepts/memory-search>). Phần này được cấu hình riêng với nhà cung cấp suy luận -- đặt `agents.defaults.memorySearch.provider` thành `"bedrock"`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0", // default      },    },  },}
[/code]

Embedding của Bedrock dùng cùng chuỗi thông tin xác thực AWS SDK như suy luận (vai trò phiên bản, SSO, khóa truy cập, cấu hình dùng chung và danh tính web). Không cần khóa API. Khi `provider` là `"auto"`, Bedrock được tự động phát hiện nếu chuỗi thông tin xác thực đó phân giải thành công.

Các mô hình embedding được hỗ trợ bao gồm Amazon Titan Embed (v1, v2), Amazon Nova Embed, Cohere Embed (v3, v4) và TwelveLabs Marengo. Xem [Tham chiếu cấu hình bộ nhớ -- Bedrock](</vi/reference/memory-config#bedrock-embedding-config>) để biết danh sách mô hình đầy đủ và các tùy chọn số chiều.

Ghi chú và lưu ý

  * Bedrock yêu cầu bật **quyền truy cập mô hình** trong tài khoản/khu vực AWS của bạn.
  * Tự động khám phá cần các quyền `bedrock:ListFoundationModels` và `bedrock:ListInferenceProfiles`.
  * Nếu bạn dựa vào chế độ tự động, hãy đặt một trong các dấu hiệu env xác thực AWS được hỗ trợ trên máy chủ Gateway. Nếu bạn muốn dùng xác thực IMDS/cấu hình dùng chung mà không có dấu hiệu env, hãy đặt `plugins.entries.amazon-bedrock.config.discovery.enabled: true`.
  * OpenClaw hiển thị nguồn thông tin xác thực theo thứ tự này: `AWS_BEARER_TOKEN_BEDROCK`, sau đó `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`, rồi `AWS_PROFILE`, rồi chuỗi AWS SDK mặc định.
  * Hỗ trợ suy luận phụ thuộc vào mô hình; hãy kiểm tra thẻ mô hình Bedrock để biết năng lực hiện tại.
  * Nếu bạn muốn luồng khóa được quản lý, bạn cũng có thể đặt một proxy tương thích OpenAI phía trước Bedrock và cấu hình nó như một nhà cung cấp OpenAI.


## Liên quan

[**Chọn mô hình** Chọn nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Tìm kiếm bộ nhớ** Embedding của Bedrock cho cấu hình tìm kiếm bộ nhớ. ](</vi/concepts/memory-search>) [**Tham chiếu cấu hình bộ nhớ** Danh sách mô hình embedding Bedrock đầy đủ và các tùy chọn số chiều. ](</vi/reference/memory-config#bedrock-embedding-config>) [**Khắc phục sự cố** Khắc phục sự cố chung và câu hỏi thường gặp. ](</vi/help/troubleshooting>)

Was this useful?YesNo