---
title: Kiến trúc runtime của tác tử
source_url: https://docs.openclaw.ai/vi/agent-runtime-architecture
scraped_at: 2026-06-29
---

ReferenceTechnical reference

OpenClaw trực tiếp sở hữu runtime agent tích hợp sẵn. Mã runtime nằm trong `src/agents/`, các helper model/provider nằm trong `src/llm/`, và các hợp đồng hướng tới Plugin được xuất qua các barrel `openclaw/plugin-sdk/*`.

## Bố cục runtime

  * `src/agents/embedded-agent-runner/`: vòng lặp lần thử agent tích hợp sẵn, adapter luồng provider, Compaction, chọn model và nối dây phiên.
  * `src/agents/sessions/`: lưu bền phiên, tải extension, khám phá tài nguyên, Skills, prompt, theme và trình kết xuất công cụ dựa trên TUI.
  * `packages/agent-core/`: lõi agent tái sử dụng được, kiểu harness cấp thấp hơn, thông điệp, helper Compaction, mẫu prompt và hợp đồng công cụ/phiên.
  * `src/agents/runtime/`: facade OpenClaw cho `@openclaw/agent-core` cùng các tiện ích proxy cục bộ.
  * `src/agents/agent-tools*.ts`: định nghĩa công cụ, schema, policy, adapter hook trước/sau và hỗ trợ chỉnh sửa host do OpenClaw sở hữu.
  * `src/agents/agent-hooks/`: các hook runtime tích hợp sẵn như biện pháp bảo vệ Compaction và cắt tỉa ngữ cảnh.
  * `src/llm/`: registry model/provider, helper transport và các triển khai luồng dành riêng cho provider.


## Ranh giới

Mã core gọi runtime tích hợp sẵn thông qua các module OpenClaw và barrel SDK, không thông qua các gói agent bên ngoài cũ. Plugin dùng các entrypoint `openclaw/plugin-sdk/*` đã được tài liệu hóa và không import nội bộ `src/**`.

`@earendil-works/pi-tui` vẫn là một phụ thuộc TUI của bên thứ ba. Nó được dùng như bộ công cụ thành phần terminal bởi TUI cục bộ và các trình kết xuất phiên; nội bộ hóa nó sẽ là một nỗ lực vendoring riêng.

## Manifest

Các gói tài nguyên khai báo tài nguyên OpenClaw trong metadata gói:

jsonCopy code
[code]
    {  "openclaw": {    "extensions": ["extensions/index.ts"],    "skills": ["skills/*.md"],    "prompts": ["prompts/*.md"],    "themes": ["themes/*.json"]  }}
[/code]

Trình quản lý gói cũng khám phá các thư mục quy ước `extensions/`, `skills/`, `prompts/` và `themes/`.

## Chọn runtime

Id runtime tích hợp sẵn mặc định là `openclaw`. Các harness Plugin có thể đăng ký thêm id runtime. `auto` chọn một harness Plugin hỗ trợ khi có, nếu không thì dùng runtime OpenClaw tích hợp sẵn.

## Liên quan

  * [Quy trình runtime agent OpenClaw](</vi/openclaw-agent-runtime>)
  * [Runtime agent](</vi/concepts/agent-runtimes>)


Was this useful?YesNo

Open issue