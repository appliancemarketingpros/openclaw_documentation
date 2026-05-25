---
title: Xây dựng Plugin
source_url: https://docs.openclaw.ai/vi/plugins/building-plugins
scraped_at: 2026-05-25
---

Plugins mở rộng OpenClaw với các năng lực mới: kênh, nhà cung cấp mô hình, giọng nói, phiên âm thời gian thực, thoại thời gian thực, hiểu nội dung phương tiện, tạo hình ảnh, tạo video, truy xuất web, tìm kiếm web, công cụ tác nhân, hoặc bất kỳ sự kết hợp nào.

Bạn không cần thêm Plugin của mình vào kho lưu trữ OpenClaw. Hãy phát hành lên [ClawHub](</vi/clawhub>) và người dùng cài đặt bằng `openclaw plugins install clawhub:<package-name>`. Các đặc tả gói trần vẫn cài đặt từ npm trong giai đoạn chuyển đổi ra mắt.

## Điều kiện tiên quyết

  * Node >= 22 và một trình quản lý gói (npm hoặc pnpm)
  * Quen thuộc với TypeScript (ESM)
  * Đối với Plugin trong kho: đã clone kho lưu trữ và chạy xong `pnpm install`. Phát triển Plugin từ checkout mã nguồn chỉ dùng pnpm vì OpenClaw tải các Plugin được đóng gói từ các gói workspace `extensions/*`.


## Loại Plugin nào?

[**Channel plugin** Kết nối OpenClaw với một nền tảng nhắn tin (Discord, IRC, v.v.) ](</vi/plugins/sdk-channel-plugins>) [**Provider plugin** Thêm một nhà cung cấp mô hình (LLM, proxy hoặc endpoint tùy chỉnh) ](</vi/plugins/sdk-provider-plugins>) [**CLI backend plugin** Ánh xạ một CLI AI cục bộ vào trình chạy dự phòng văn bản của OpenClaw ](</vi/plugins/cli-backend-plugins>) [**Tool / hook plugin** Đăng ký công cụ tác nhân, hook sự kiện hoặc dịch vụ - tiếp tục bên dưới ](</vi/plugins/hooks>)

Đối với một Plugin kênh không được bảo đảm là đã cài đặt khi chạy onboarding/thiết lập, hãy dùng `createOptionalChannelSetupSurface(...)` từ `openclaw/plugin-sdk/channel-setup`. Hàm này tạo ra một cặp adapter thiết lập + wizard thông báo yêu cầu cài đặt và đóng an toàn khi ghi cấu hình thật cho đến khi Plugin được cài đặt.

## Bắt đầu nhanh: Plugin công cụ

Hướng dẫn này tạo một Plugin tối thiểu để đăng ký một công cụ tác nhân. Plugin kênh và Plugin nhà cung cấp có các hướng dẫn riêng được liên kết ở trên.

* ### Create the package and manifest

package.jsonCopy code
[code]
    {"name": "@myorg/openclaw-my-plugin","version": "1.0.0","type": "module","openclaw": {  "extensions": ["./index.ts"],  "compat": {    "pluginApi": ">=2026.3.24-beta.2",    "minGatewayVersion": "2026.3.24-beta.2"  },  "build": {    "openclawVersion": "2026.3.24-beta.2",    "pluginSdkVersion": "2026.3.24-beta.2"  }}}
[/code]

openclaw.plugin.jsonCopy code
[code]
    {"id": "my-plugin","name": "My Plugin","description": "Adds a custom tool to OpenClaw","contracts": {  "tools": ["my_tool"]},"activation": {  "onStartup": true},"configSchema": {  "type": "object",  "additionalProperties": false}}
[/code]

Mọi Plugin đều cần một manifest, ngay cả khi không có cấu hình. Các công cụ được đăng ký lúc chạy phải được liệt kê trong `contracts.tools` để OpenClaw có thể phát hiện Plugin sở hữu mà không cần tải mọi runtime Plugin. Plugin cũng nên khai báo `activation.onStartup` một cách có chủ đích. Ví dụ này đặt thành `true`. Xem [Manifest](</vi/plugins/manifest>) để biết schema đầy đủ. Các đoạn mẫu phát hành ClawHub chuẩn nằm trong `docs/snippets/plugin-publish/`.

* ### Write the entry point

typescriptCopy code
[code]
    // index.tsimport { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import { Type } from "@sinclair/typebox"; export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Adds a custom tool to OpenClaw",  register(api) {    api.registerTool({      name: "my_tool",      description: "Do a thing",      parameters: Type.Object({ input: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: `Got: ${params.input}` }] };      },    });  },});
[/code]

`definePluginEntry` dành cho Plugin không phải kênh. Đối với kênh, hãy dùng `defineChannelPluginEntry` \- xem [Plugin kênh](</vi/plugins/sdk-channel-plugins>). Để biết đầy đủ tùy chọn entry point, xem [Entry point](</vi/plugins/sdk-entrypoints>).

* ### Test and publish

**Plugin bên ngoài:** xác thực và phát hành bằng ClawHub, sau đó cài đặt:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginopenclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

Các đặc tả gói trần như `@myorg/openclaw-my-plugin` cài đặt từ npm trong giai đoạn chuyển đổi ra mắt. Dùng `clawhub:` khi bạn muốn phân giải qua ClawHub.

**Plugin trong kho:** đặt dưới cây workspace Plugin được đóng gói - sẽ được tự động phát hiện.

bashCopy code
[code]
    pnpm test -- <bundled-plugin-root>/my-plugin/
[/code]

## Năng lực của Plugin

Một Plugin duy nhất có thể đăng ký bất kỳ số lượng năng lực nào thông qua đối tượng `api`:

Năng lực | Phương thức đăng ký | Hướng dẫn chi tiết  
---|---|---  
Suy luận văn bản (LLM) | `api.registerProvider(...)` | [Plugin nhà cung cấp](</vi/plugins/sdk-provider-plugins>)  
Backend suy luận CLI | `api.registerCliBackend(...)` | [Plugin Backend CLI](</vi/plugins/cli-backend-plugins>)  
Kênh / nhắn tin | `api.registerChannel(...)` | [Plugin kênh](</vi/plugins/sdk-channel-plugins>)  
Giọng nói (TTS/STT) | `api.registerSpeechProvider(...)` | [Plugin nhà cung cấp](</vi/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Phiên âm thời gian thực | `api.registerRealtimeTranscriptionProvider(...)` | [Plugin nhà cung cấp](</vi/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Thoại thời gian thực | `api.registerRealtimeVoiceProvider(...)` | [Plugin nhà cung cấp](</vi/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Hiểu nội dung phương tiện | `api.registerMediaUnderstandingProvider(...)` | [Plugin nhà cung cấp](</vi/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Tạo hình ảnh | `api.registerImageGenerationProvider(...)` | [Plugin nhà cung cấp](</vi/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Tạo nhạc | `api.registerMusicGenerationProvider(...)` | [Plugin nhà cung cấp](</vi/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Tạo video | `api.registerVideoGenerationProvider(...)` | [Plugin nhà cung cấp](</vi/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Truy xuất web | `api.registerWebFetchProvider(...)` | [Plugin nhà cung cấp](</vi/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Tìm kiếm web | `api.registerWebSearchProvider(...)` | [Plugin nhà cung cấp](</vi/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Middleware kết quả công cụ | `api.registerAgentToolResultMiddleware(...)` | [Tổng quan SDK](</vi/plugins/sdk-overview#registration-api>)  
Công cụ tác nhân | `api.registerTool(...)` | Bên dưới  
Lệnh tùy chỉnh | `api.registerCommand(...)` | [Entry point](</vi/plugins/sdk-entrypoints>)  
Hook Plugin | `api.on(...)` | [Hook Plugin](</vi/plugins/hooks>)  
Hook sự kiện nội bộ | `api.registerHook(...)` | [Entry point](</vi/plugins/sdk-entrypoints>)  
Tuyến HTTP | `api.registerHttpRoute(...)` | [Nội bộ](</vi/plugins/architecture-internals#gateway-http-routes>)  
Lệnh con CLI | `api.registerCli(...)` | [Entry point](</vi/plugins/sdk-entrypoints>)  
  
Để biết API đăng ký đầy đủ, xem [Tổng quan SDK](</vi/plugins/sdk-overview#registration-api>).

Plugin được đóng gói có thể dùng `api.registerAgentToolResultMiddleware(...)` khi chúng cần ghi lại kết quả công cụ bất đồng bộ trước khi mô hình nhìn thấy đầu ra. Khai báo các runtime mục tiêu trong `contracts.agentToolResultMiddleware`, ví dụ `["pi", "codex"]`. Đây là một seam đáng tin cậy dành cho Plugin được đóng gói; các Plugin bên ngoài nên ưu tiên hook Plugin OpenClaw thông thường trừ khi OpenClaw có thêm chính sách tin cậy rõ ràng cho năng lực này.

Nếu Plugin của bạn đăng ký các phương thức RPC Gateway tùy chỉnh, hãy giữ chúng trên một tiền tố riêng của Plugin. Các namespace quản trị lõi (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) vẫn được dành riêng và luôn phân giải thành `operator.admin`, ngay cả khi một Plugin yêu cầu phạm vi hẹp hơn.

Các ngữ nghĩa bảo vệ hook cần ghi nhớ:

  * `before_tool_call`: `{ block: true }` là kết thúc và dừng các handler có độ ưu tiên thấp hơn.
  * `before_tool_call`: `{ block: false }` được xử lý như không có quyết định.
  * `before_tool_call`: `{ requireApproval: true }` tạm dừng thực thi tác nhân và nhắc người dùng phê duyệt thông qua lớp phủ phê duyệt exec, nút Telegram, tương tác Discord, hoặc lệnh `/approve` trên bất kỳ kênh nào.
  * `before_install`: `{ block: true }` là kết thúc và dừng các handler có độ ưu tiên thấp hơn.
  * `before_install`: `{ block: false }` được xử lý như không có quyết định.
  * `message_sending`: `{ cancel: true }` là kết thúc và dừng các handler có độ ưu tiên thấp hơn.
  * `message_sending`: `{ cancel: false }` được xử lý như không có quyết định.
  * `message_received`: ưu tiên trường có kiểu `threadId` khi bạn cần định tuyến luồng/chủ đề đi vào. Giữ `metadata` cho các thông tin bổ sung riêng theo kênh.
  * `message_sending`: ưu tiên các trường định tuyến có kiểu `replyToId` / `threadId` thay vì các khóa metadata riêng theo kênh.


Lệnh `/approve` xử lý cả phê duyệt exec và phê duyệt Plugin với dự phòng có giới hạn: khi không tìm thấy id phê duyệt exec, OpenClaw thử lại cùng id đó qua phê duyệt Plugin. Chuyển tiếp phê duyệt Plugin có thể được cấu hình độc lập thông qua `approvals.plugin` trong cấu hình.

Nếu hệ thống phê duyệt tùy chỉnh cần phát hiện cùng trường hợp dự phòng có giới hạn đó, hãy ưu tiên `isApprovalNotFoundError` từ `openclaw/plugin-sdk/error-runtime` thay vì tự khớp chuỗi hết hạn phê duyệt thủ công.

Xem [Hook Plugin](</vi/plugins/hooks>) để biết ví dụ và tài liệu tham chiếu hook.

## Đăng ký công cụ tác nhân

Công cụ là các hàm có kiểu mà LLM có thể gọi. Chúng có thể là bắt buộc (luôn có sẵn) hoặc tùy chọn (người dùng chọn tham gia):

typescriptCopy code
[code]
    register(api) {  // Required tool - always available  api.registerTool({    name: "my_tool",    description: "Do a thing",    parameters: Type.Object({ input: Type.String() }),    async execute(_id, params) {      return { content: [{ type: "text", text: params.input }] };    },  });   // Optional tool - user must add to allowlist  api.registerTool(    {      name: "workflow_tool",      description: "Run a workflow",      parameters: Type.Object({ pipeline: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: params.pipeline }] };      },    },    { optional: true },  );}
[/code]

Các factory công cụ nhận một đối tượng ngữ cảnh do runtime cung cấp. Dùng `ctx.activeModel` khi một công cụ cần ghi log, hiển thị, hoặc thích ứng với mô hình đang hoạt động cho lượt hiện tại. Đối tượng này có thể bao gồm `provider`, `modelId`, và `modelRef`. Hãy xem nó là metadata runtime mang tính thông tin, không phải là ranh giới bảo mật chống lại toán tử cục bộ, mã plugin đã cài đặt, hoặc runtime OpenClaw đã bị sửa đổi. Với các công cụ cục bộ nhạy cảm, hãy giữ cơ chế plugin hoặc toán tử chọn tham gia rõ ràng và đóng an toàn khi metadata mô hình đang hoạt động bị thiếu hoặc không phù hợp.

Mọi công cụ được đăng ký bằng `api.registerTool(...)` cũng phải được khai báo trong manifest plugin:

jsonCopy code
[code]
    {  "contracts": {    "tools": ["my_tool", "workflow_tool"]  },  "toolMetadata": {    "workflow_tool": {      "optional": true    }  }}
[/code]

OpenClaw ghi nhận và lưu vào bộ nhớ đệm descriptor đã xác thực từ công cụ đã đăng ký, nên plugin không lặp lại dữ liệu `description` hoặc schema trong manifest. Hợp đồng manifest chỉ khai báo quyền sở hữu và khả năng khám phá; khi thực thi vẫn gọi implementation công cụ đã đăng ký đang chạy. Đặt `toolMetadata.<tool>.optional: true` cho các công cụ được đăng ký bằng `api.registerTool(..., { optional: true })` để OpenClaw có thể tránh tải runtime plugin đó cho đến khi công cụ được allowlist rõ ràng.

Người dùng bật các công cụ tùy chọn trong cấu hình:

json5Copy code
[code]
    {  tools: { allow: ["workflow_tool"] },}
[/code]

  * Tên công cụ không được xung đột với công cụ lõi (các xung đột sẽ bị bỏ qua)
  * Công cụ có đối tượng đăng ký sai định dạng, bao gồm thiếu `parameters`, sẽ bị bỏ qua và được báo cáo trong chẩn đoán plugin thay vì làm hỏng các lần chạy agent
  * Dùng `optional: true` cho các công cụ có hiệu ứng phụ hoặc yêu cầu binary bổ sung
  * Người dùng có thể bật tất cả công cụ từ một plugin bằng cách thêm id plugin vào `tools.allow`


## Đăng ký lệnh CLI

Plugin có thể thêm các nhóm lệnh gốc `openclaw` bằng `api.registerCli`. Cung cấp `descriptors` cho mọi gốc lệnh cấp cao nhất để OpenClaw có thể hiển thị và định tuyến lệnh mà không cần tải sẵn mọi runtime plugin.

typescriptCopy code
[code]
    register(api) {  api.registerCli(    ({ program }) => {      const demo = program        .command("demo-plugin")        .description("Run demo plugin commands");       demo        .command("ping")        .description("Check that the plugin CLI is executable")        .action(() => {          console.log("demo-plugin:pong");        });    },    {      descriptors: [        {          name: "demo-plugin",          description: "Run demo plugin commands",          hasSubcommands: true,        },      ],    },  );}
[/code]

Sau khi cài đặt, hãy xác minh đăng ký runtime và thực thi lệnh:

bashCopy code
[code]
    openclaw plugins inspect demo-plugin --runtime --jsonopenclaw demo-plugin ping
[/code]

## Quy ước import

Luôn import từ các đường dẫn `openclaw/plugin-sdk/<subpath>` tập trung:

typescriptCopy code
[code]
      // Wrong: monolithic root (deprecated, will be removed) 
[/code]

Để xem tham chiếu subpath đầy đủ, xem [Tổng quan SDK](</vi/plugins/sdk-overview>).

Trong plugin của bạn, dùng các file barrel cục bộ (`api.ts`, `runtime-api.ts`) cho import nội bộ - không bao giờ import chính plugin của bạn qua đường dẫn SDK của nó.

Đối với plugin nhà cung cấp, hãy giữ các helper riêng cho nhà cung cấp trong các barrel gốc package đó trừ khi seam thật sự mang tính chung. Các ví dụ được bundled hiện tại:

  * Anthropic: wrapper stream Claude và helper `service_tier` / beta
  * OpenAI: builder nhà cung cấp, helper mô hình mặc định, nhà cung cấp realtime
  * OpenRouter: builder nhà cung cấp cùng helper onboarding/cấu hình


Nếu một helper chỉ hữu ích bên trong một package nhà cung cấp bundled, hãy giữ nó trên seam gốc package đó thay vì đưa nó vào `openclaw/plugin-sdk/*`.

Một số seam helper `openclaw/plugin-sdk/<bundled-id>` được tạo tự động vẫn tồn tại để bảo trì bundled-plugin khi chúng theo dõi usage của owner. Hãy xem chúng là các bề mặt được dành riêng, không phải mẫu mặc định cho plugin bên thứ ba mới.

## Checklist trước khi gửi

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s **package.json** có metadata `openclaw` chính xác OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Manifest **openclaw.plugin.json** hiện diện và hợp lệ OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Entry point dùng `defineChannelPluginEntry` hoặc `definePluginEntry` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Mọi import dùng đường dẫn `plugin-sdk/<subpath>` tập trung OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo