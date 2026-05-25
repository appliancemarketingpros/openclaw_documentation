---
title: LiteLLM
source_url: https://docs.openclaw.ai/vi/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>) là một LLM Gateway mã nguồn mở cung cấp một API thống nhất cho hơn 100 nhà cung cấp mô hình. Định tuyến OpenClaw qua LiteLLM để có theo dõi chi phí tập trung, ghi log và khả năng linh hoạt chuyển backend mà không cần thay đổi cấu hình OpenClaw của bạn.

## Bắt đầu nhanh

### Thiết lập ban đầu (khuyến nghị)

**Phù hợp nhất cho:** đường đi nhanh nhất để có một thiết lập LiteLLM hoạt động.

* ### Chạy thiết lập ban đầu

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

Để thiết lập không tương tác với một proxy từ xa, hãy truyền URL proxy rõ ràng:

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Thiết lập thủ công

**Phù hợp nhất cho:** toàn quyền kiểm soát cài đặt và cấu hình.

* ### Khởi động LiteLLM Proxy

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### Trỏ OpenClaw đến LiteLLM

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

Vậy là xong. OpenClaw giờ sẽ định tuyến qua LiteLLM.

## Cấu hình

### Biến môi trường

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### Tệp cấu hình

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## Cấu hình nâng cao

### Tạo hình ảnh

LiteLLM cũng có thể hỗ trợ công cụ `image_generate` thông qua các route tương thích OpenAI `/images/generations` và `/images/edits`. Cấu hình một mô hình hình ảnh LiteLLM trong `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

Các URL LiteLLM loopback như `http://localhost:4000` hoạt động mà không cần ghi đè mạng riêng toàn cục. Với proxy được lưu trữ trên LAN, hãy đặt `models.providers.litellm.request.allowPrivateNetwork: true` vì API key sẽ được gửi đến máy chủ proxy đã cấu hình.

Khóa ảo

Tạo một khóa riêng cho OpenClaw với giới hạn chi tiêu:

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

Dùng khóa đã tạo làm `LITELLM_API_KEY`.

Định tuyến mô hình

LiteLLM có thể định tuyến các yêu cầu mô hình đến những backend khác nhau. Cấu hình trong `config.yaml` LiteLLM của bạn:

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw tiếp tục yêu cầu `claude-opus-4-6` — LiteLLM xử lý việc định tuyến.

Xem mức sử dụng

Kiểm tra bảng điều khiển hoặc API của LiteLLM:

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Ghi chú về hành vi proxy

  * LiteLLM mặc định chạy trên `http://localhost:4000`
  * OpenClaw kết nối qua endpoint `/v1` kiểu proxy tương thích OpenAI của LiteLLM
  * Việc định hình request chỉ dành cho OpenAI gốc không áp dụng qua LiteLLM: không có `service_tier`, không có Responses `store`, không có gợi ý prompt-cache và không có định hình payload tương thích reasoning của OpenAI
  * Các header ghi nhận nguồn OpenClaw ẩn (`originator`, `version`, `User-Agent`) không được chèn trên các URL cơ sở LiteLLM tùy chỉnh


## Liên quan

[**Tài liệu LiteLLM** Tài liệu LiteLLM chính thức và tài liệu tham chiếu API. ](<https://docs.litellm.ai>) [**Chọn mô hình** Tổng quan về tất cả nhà cung cấp, tham chiếu mô hình và hành vi chuyển dự phòng. ](</vi/concepts/model-providers>) [**Cấu hình** Tài liệu tham chiếu cấu hình đầy đủ. ](</vi/gateway/configuration>) [**Chọn mô hình** Cách chọn và cấu hình mô hình. ](</vi/concepts/models>)

Was this useful?YesNo