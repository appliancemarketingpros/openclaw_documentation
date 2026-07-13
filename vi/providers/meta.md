---
title: Siêu dữ liệu
source_url: https://docs.openclaw.ai/vi/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

**Meta API** sử dụng **Responses API** tương thích với OpenAI (`POST /v1/responses`) cho mô hình suy luận `muse-spark-1.1`. Nhà cung cấp được phân phối dưới dạng plugin OpenClaw đi kèm.

Thuộc tính | Giá trị  
---|---  
ID nhà cung cấp | `meta`  
Plugin | nhà cung cấp đi kèm  
Biến môi trường xác thực | `MODEL_API_KEY`  
Cờ thiết lập ban đầu | `--auth-choice meta-api-key`  
Cờ CLI trực tiếp | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
URL cơ sở | `https://api.meta.ai/v1`  
Mô hình mặc định | `meta/muse-spark-1.1`  
Mức suy luận mặc định | `high` (`reasoning.effort`)  
  
## Bắt đầu

* ### Đặt khóa API

Thiết lập ban đầuCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Cờ trực tiếpCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Chỉ dùng biến môi trườngCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### Xác minh các mô hình khả dụng

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

Liệt kê mục danh mục tĩnh `muse-spark-1.1`. Nếu không thể phân giải `MODEL_API_KEY`, `openclaw models status --json` sẽ báo thông tin xác thực còn thiếu trong `auth.unusableProfiles`.

## Thiết lập không tương tác

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## Danh mục tích hợp sẵn

Tham chiếu mô hình | Tên | Suy luận | Cửa sổ ngữ cảnh | Đầu ra tối đa  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | có | 1,048,576 | 131,072  
  
Khả năng:

  * Đầu vào văn bản + hình ảnh
  * Gọi công cụ và truyền phát
  * Mức độ suy luận: `minimal`, `low`, `medium`, `high`, `xhigh` (mặc định: `high`)
  * Phát lại suy luận được mã hóa không lưu trạng thái (`store: false`, `include: ["reasoning.encrypted_content"]`)


## Cấu hình thủ công

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## Kiểm thử nhanh

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

Các kiểm thử trực tiếp sử dụng `muse-spark-1.1` với `POST /v1/responses`.

## Liên quan

[**Nhà cung cấp mô hình** Chọn nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Chế độ suy luận** Các mức độ suy luận cho muse-spark-1.1. ](</vi/tools/thinking>) [**Tham chiếu cấu hình** Giá trị mặc định của tác nhân và cấu hình mô hình. ](</vi/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue