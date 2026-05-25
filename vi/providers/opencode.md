---
title: OpenCode
source_url: https://docs.openclaw.ai/vi/providers/opencode
scraped_at: 2026-05-25
---

OpenCode cung cấp hai danh mục được lưu trữ trong OpenClaw:

Danh mục | Tiền tố | Nhà cung cấp runtime  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
Cả hai danh mục dùng cùng một khóa API OpenCode. OpenClaw giữ các id nhà cung cấp runtime tách biệt để việc định tuyến theo từng mô hình ở upstream vẫn chính xác, nhưng quy trình onboarding và tài liệu xem chúng như một thiết lập OpenCode duy nhất.

## Bắt đầu

### Zen catalog

**Phù hợp nhất cho:** proxy đa mô hình OpenCode được tuyển chọn (Claude, GPT, Gemini).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

Hoặc truyền trực tiếp khóa:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Set a Zen model as the default

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Go catalog

**Phù hợp nhất cho:** nhóm Kimi, GLM và MiniMax do OpenCode lưu trữ.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

Hoặc truyền trực tiếp khóa:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Set a Go model as the default

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Ví dụ cấu hình

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## Danh mục tích hợp sẵn

### Zen

Thuộc tính | Giá trị  
---|---  
Nhà cung cấp runtime | `opencode`  
Mô hình ví dụ | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

Thuộc tính | Giá trị  
---|---  
Nhà cung cấp runtime | `opencode-go`  
Mô hình ví dụ | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## Cấu hình nâng cao

API key aliases

`OPENCODE_ZEN_API_KEY` cũng được hỗ trợ làm bí danh cho `OPENCODE_API_KEY`.

Shared credentials

Nhập một khóa OpenCode trong quá trình thiết lập sẽ lưu thông tin xác thực cho cả hai nhà cung cấp runtime. Bạn không cần onboard từng danh mục riêng biệt.

Billing and dashboard

Bạn đăng nhập vào OpenCode, thêm chi tiết thanh toán và sao chép khóa API. Việc thanh toán và tính khả dụng của danh mục được quản lý từ dashboard OpenCode.

Gemini replay behavior

Các ref OpenCode dựa trên Gemini vẫn đi theo đường dẫn proxy-Gemini, nên OpenClaw giữ việc làm sạch chữ ký suy nghĩ của Gemini ở đó mà không bật xác thực replay Gemini gốc hoặc viết lại bootstrap.

Non-Gemini replay behavior

Các ref OpenCode không phải Gemini giữ chính sách replay tối thiểu tương thích với OpenAI.

## Liên quan

[**Model selection** Chọn nhà cung cấp, ref mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Configuration reference** Tài liệu tham chiếu cấu hình đầy đủ cho agent, mô hình và nhà cung cấp. ](</vi/gateway/configuration-reference>)

Was this useful?YesNo