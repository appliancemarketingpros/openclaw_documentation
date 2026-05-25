---
title: OpenCode Go
source_url: https://docs.openclaw.ai/vi/providers/opencode-go
scraped_at: 2026-05-25
---

OpenCode Go là danh mục Go trong [OpenCode](</vi/providers/opencode>). Nó dùng cùng `OPENCODE_API_KEY` như danh mục Zen, nhưng giữ id provider runtime `opencode-go` để định tuyến theo từng mô hình ở upstream luôn chính xác.

Thuộc tính | Giá trị  
---|---  
Provider runtime | `opencode-go`  
Xác thực | `OPENCODE_API_KEY`  
Thiết lập cha | [OpenCode](</vi/providers/opencode>)  
  
## Danh mục tích hợp sẵn

OpenClaw lấy hầu hết các hàng trong danh mục Go từ registry mô hình pi được đóng gói kèm và bổ sung các hàng upstream hiện tại trong khi registry bắt kịp. Chạy `openclaw models list --provider opencode-go` để xem danh sách mô hình hiện tại.

Provider bao gồm:

Tham chiếu mô hình | Tên  
---|---  
`opencode-go/glm-5` | GLM-5  
`opencode-go/glm-5.1` | GLM-5.1  
`opencode-go/kimi-k2.5` | Kimi K2.5  
`opencode-go/kimi-k2.6` | Kimi K2.6 (giới hạn 3x)  
`opencode-go/deepseek-v4-pro` | DeepSeek V4 Pro  
`opencode-go/deepseek-v4-flash` | DeepSeek V4 Flash  
`opencode-go/mimo-v2-omni` | MiMo V2 Omni  
`opencode-go/mimo-v2-pro` | MiMo V2 Pro  
`opencode-go/minimax-m2.5` | MiniMax M2.5  
`opencode-go/minimax-m2.7` | MiniMax M2.7  
`opencode-go/qwen3.5-plus` | Qwen3.5 Plus  
`opencode-go/qwen3.6-plus` | Qwen3.6 Plus  
  
## Bắt đầu

### Interactive

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

* ### Set a Go model as default

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

### Non-interactive

* ### Pass the key directly

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Ví dụ cấu hình

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret  agents: { defaults: { model: { primary: "opencode-go/kimi-k2.6" } } },}
[/code]

## Cấu hình nâng cao

Routing behavior

OpenClaw tự động xử lý định tuyến theo từng mô hình khi tham chiếu mô hình dùng `opencode-go/...`. Không cần cấu hình provider bổ sung.

Runtime ref convention

Tham chiếu runtime vẫn rõ ràng: `opencode/...` cho Zen, `opencode-go/...` cho Go. Điều này giữ cho định tuyến theo từng mô hình ở upstream chính xác trên cả hai danh mục.

Shared credentials

Cùng một `OPENCODE_API_KEY` được dùng bởi cả danh mục Zen và Go. Việc nhập khóa trong quá trình thiết lập sẽ lưu thông tin xác thực cho cả hai provider runtime.

## Liên quan

[**OpenCode (parent)** Onboarding dùng chung, tổng quan danh mục và ghi chú nâng cao. ](</vi/providers/opencode>) [**Model selection** Chọn provider, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>)

Was this useful?YesNo