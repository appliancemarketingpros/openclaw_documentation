---
title: Hugging Face (suy luận)
source_url: https://docs.openclaw.ai/vi/providers/huggingface
scraped_at: 2026-05-25
---

[Nhà cung cấp suy luận Hugging Face](<https://huggingface.co/docs/inference-providers>) cung cấp chat completions tương thích OpenAI thông qua một router API duy nhất. Bạn có quyền truy cập vào nhiều mô hình (DeepSeek, Llama và nhiều mô hình khác) chỉ với một token. OpenClaw dùng **endpoint tương thích OpenAI** (chỉ chat completions); với text-to-image, embeddings hoặc speech, hãy dùng trực tiếp [HF inference clients](<https://huggingface.co/docs/api-inference/quicktour>).

  * Nhà cung cấp: `huggingface`
  * Xác thực: `HUGGINGFACE_HUB_TOKEN` hoặc `HF_TOKEN` (token chi tiết có quyền **Make calls to Inference Providers**)
  * API: tương thích OpenAI (`https://router.huggingface.co/v1`)
  * Thanh toán: Một token HF; [bảng giá](<https://huggingface.co/docs/inference-providers/pricing>) theo mức giá của nhà cung cấp, có gói miễn phí.


## Bắt đầu

* ### Tạo token chi tiết

Truy cập [Hugging Face Settings Tokens](<https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained>) và tạo một token chi tiết mới.

* ### Chạy onboarding

Chọn **Hugging Face** trong menu thả xuống nhà cung cấp, rồi nhập khóa API của bạn khi được nhắc:

bashCopy code
[code]
    openclaw onboard --auth-choice huggingface-api-key
[/code]

* ### Chọn mô hình mặc định

Trong menu thả xuống **Default Hugging Face model** , chọn mô hình bạn muốn. Danh sách được tải từ Inference API khi bạn có token hợp lệ; nếu không, danh sách tích hợp sẵn sẽ được hiển thị. Lựa chọn của bạn được lưu làm mô hình mặc định.

Bạn cũng có thể đặt hoặc thay đổi mô hình mặc định sau trong cấu hình:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/deepseek-ai/DeepSeek-R1" },    },  },}
[/code]

* ### Xác minh mô hình khả dụng

bashCopy code
[code]
    openclaw models list --provider huggingface
[/code]

### Thiết lập không tương tác

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice huggingface-api-key \  --huggingface-api-key "$HF_TOKEN"
[/code]

Lệnh này sẽ đặt `huggingface/deepseek-ai/DeepSeek-R1` làm mô hình mặc định.

## ID mô hình

Tham chiếu mô hình dùng dạng `huggingface/<org>/<model>` (ID kiểu Hub). Danh sách dưới đây lấy từ **GET** `https://router.huggingface.co/v1/models`; danh mục của bạn có thể có thêm mô hình.

Mô hình | Tham chiếu (thêm tiền tố `huggingface/`)  
---|---  
DeepSeek R1 | `deepseek-ai/DeepSeek-R1`  
DeepSeek V3.2 | `deepseek-ai/DeepSeek-V3.2`  
Qwen3 8B | `Qwen/Qwen3-8B`  
Qwen2.5 7B Instruct | `Qwen/Qwen2.5-7B-Instruct`  
Qwen3 32B | `Qwen/Qwen3-32B`  
Llama 3.3 70B Instruct | `meta-llama/Llama-3.3-70B-Instruct`  
Llama 3.1 8B Instruct | `meta-llama/Llama-3.1-8B-Instruct`  
GPT-OSS 120B | `openai/gpt-oss-120b`  
GLM 4.7 | `zai-org/GLM-4.7`  
Kimi K2.5 | `moonshotai/Kimi-K2.5`  
  
## Cấu hình nâng cao

Khám phá mô hình và menu thả xuống onboarding

OpenClaw khám phá mô hình bằng cách gọi trực tiếp **Inference endpoint** :

bashCopy code
[code]
    GET https://router.huggingface.co/v1/models
[/code]

(Tùy chọn: gửi `Authorization: Bearer $HUGGINGFACE_HUB_TOKEN` hoặc `$HF_TOKEN` để lấy danh sách đầy đủ; một số endpoint trả về tập con khi không xác thực.) Phản hồi theo kiểu OpenAI `{ "object": "list", "data": [ { "id": "Qwen/Qwen3-8B", "owned_by": "Qwen", ... }, ... ] }`.

Khi bạn cấu hình khóa API Hugging Face (qua onboarding, `HUGGINGFACE_HUB_TOKEN` hoặc `HF_TOKEN`), OpenClaw dùng GET này để khám phá các mô hình chat-completion khả dụng. Trong **thiết lập tương tác** , sau khi nhập token, bạn sẽ thấy menu thả xuống **Default Hugging Face model** được điền từ danh sách đó (hoặc danh mục tích hợp sẵn nếu yêu cầu thất bại). Khi chạy (ví dụ lúc khởi động Gateway), nếu có khóa, OpenClaw lại gọi **GET** `https://router.huggingface.co/v1/models` để làm mới danh mục. Danh sách được hợp nhất với danh mục tích hợp sẵn (cho metadata như cửa sổ ngữ cảnh và chi phí). Nếu yêu cầu thất bại hoặc không đặt khóa, chỉ danh mục tích hợp sẵn được dùng.

Tên mô hình, alias và hậu tố chính sách

  * **Tên từ API:** Tên hiển thị của mô hình được **bổ sung từ GET /v1/models** khi API trả về `name`, `title` hoặc `display_name`; nếu không, tên được suy ra từ ID mô hình (ví dụ `deepseek-ai/DeepSeek-R1` trở thành "DeepSeek R1").
  * **Ghi đè tên hiển thị:** Bạn có thể đặt nhãn tùy chỉnh cho từng mô hình trong cấu hình để nó hiển thị theo cách bạn muốn trong CLI và UI:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1 (fast)" },        "huggingface/deepseek-ai/DeepSeek-R1:cheapest": { alias: "DeepSeek R1 (cheap)" },      },    },  },}
[/code]

  * **Hậu tố chính sách:** Tài liệu và helper Hugging Face đi kèm OpenClaw hiện coi hai hậu tố này là các biến thể chính sách tích hợp sẵn:

    * **`:fastest`** — thông lượng cao nhất.
    * **`:cheapest`** — chi phí thấp nhất cho mỗi token đầu ra.

Bạn có thể thêm chúng làm mục riêng trong `models.providers.huggingface.models` hoặc đặt `model.primary` kèm hậu tố. Bạn cũng có thể đặt thứ tự nhà cung cấp mặc định trong [cài đặt Inference Provider](<https://hf.co/settings/inference-providers>) (không có hậu tố = dùng thứ tự đó).

  * **Hợp nhất cấu hình:** Các mục hiện có trong `models.providers.huggingface.models` (ví dụ trong `models.json`) được giữ lại khi cấu hình được hợp nhất. Vì vậy, mọi `name`, `alias` hoặc tùy chọn mô hình tùy chỉnh bạn đặt ở đó đều được giữ nguyên.


Thiết lập môi trường và daemon

Nếu Gateway chạy dưới dạng daemon (launchd/systemd), hãy đảm bảo `HUGGINGFACE_HUB_TOKEN` hoặc `HF_TOKEN` khả dụng cho tiến trình đó (ví dụ trong `~/.openclaw/.env` hoặc qua `env.shellEnv`).

Cấu hình: DeepSeek R1 với Qwen dự phòng json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-R1",        fallbacks: ["huggingface/Qwen/Qwen3-8B"],      },      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1" },        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },      },    },  },}
[/code]

Cấu hình: Qwen với các biến thể cheapest và fastest json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen3-8B" },      models: {        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },        "huggingface/Qwen/Qwen3-8B:cheapest": { alias: "Qwen3 8B (cheapest)" },        "huggingface/Qwen/Qwen3-8B:fastest": { alias: "Qwen3 8B (fastest)" },      },    },  },}
[/code]

Cấu hình: DeepSeek + Llama + GPT-OSS với alias json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-V3.2",        fallbacks: [          "huggingface/meta-llama/Llama-3.3-70B-Instruct",          "huggingface/openai/gpt-oss-120b",        ],      },      models: {        "huggingface/deepseek-ai/DeepSeek-V3.2": { alias: "DeepSeek V3.2" },        "huggingface/meta-llama/Llama-3.3-70B-Instruct": { alias: "Llama 3.3 70B" },        "huggingface/openai/gpt-oss-120b": { alias: "GPT-OSS 120B" },      },    },  },}
[/code]

Cấu hình: Nhiều Qwen và DeepSeek với hậu tố chính sách json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest" },      models: {        "huggingface/Qwen/Qwen2.5-7B-Instruct": { alias: "Qwen2.5 7B" },        "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest": { alias: "Qwen2.5 7B (cheap)" },        "huggingface/deepseek-ai/DeepSeek-R1:fastest": { alias: "DeepSeek R1 (fast)" },        "huggingface/meta-llama/Llama-3.1-8B-Instruct": { alias: "Llama 3.1 8B" },      },    },  },}
[/code]

## Liên quan

[**Lựa chọn mô hình** Tổng quan về tất cả nhà cung cấp, tham chiếu mô hình và hành vi failover. ](</vi/concepts/model-providers>) [**Lựa chọn mô hình** Cách chọn và cấu hình mô hình. ](</vi/concepts/models>) [**Tài liệu Inference Providers** Tài liệu chính thức về Hugging Face Inference Providers. ](<https://huggingface.co/docs/inference-providers>) [**Cấu hình** Tham chiếu cấu hình đầy đủ. ](</vi/gateway/configuration>)

Was this useful?YesNo