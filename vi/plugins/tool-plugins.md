---
title: Plugin công cụ
source_url: https://docs.openclaw.ai/vi/plugins/tool-plugins
scraped_at: 2026-06-29
---

CapabilitiesBuilding plugins

Plugin công cụ thêm các công cụ mà agent có thể gọi vào OpenClaw mà không thêm kênh, nhà cung cấp mô hình, hook, dịch vụ hoặc backend thiết lập. Dùng `defineToolPlugin` khi plugin sở hữu một danh sách công cụ cố định và bạn muốn OpenClaw tạo metadata manifest giúp các công cụ đó có thể được khám phá mà không cần tải mã runtime.

Luồng được khuyến nghị là:

  1. Tạo khung package bằng `openclaw plugins init`.
  2. Viết công cụ bằng `defineToolPlugin`.
  3. Build JavaScript.
  4. Tạo metadata `openclaw.plugin.json` và `package.json` bằng `openclaw plugins build`.
  5. Xác thực metadata đã tạo trước khi phát hành hoặc cài đặt.


Đối với plugin nhà cung cấp, kênh, hook, dịch vụ hoặc plugin nhiều năng lực, hãy bắt đầu với [Xây dựng plugin](</vi/plugins/building-plugins>), [Plugin kênh](</vi/plugins/sdk-channel-plugins>), hoặc [Plugin nhà cung cấp](</vi/plugins/sdk-provider-plugins>).

## Yêu cầu

  * Node >= 22.
  * Đầu ra package TypeScript ESM.
  * `typebox` cho schema cấu hình và tham số công cụ.
  * `openclaw >=2026.5.17`, phiên bản OpenClaw đầu tiên export `openclaw/plugin-sdk/tool-plugin`.
  * Một thư mục gốc package có thể phân phối `dist/`, `openclaw.plugin.json`, và `package.json`.


Plugin được tạo import `typebox` ở runtime, vì vậy hãy giữ `typebox` trong `dependencies`, không chỉ trong `devDependencies`.

## Bắt đầu nhanh

Tạo một package plugin mới:

bashCopy code
[code]
    openclaw plugins init stock-quotes --name "Stock Quotes"cd stock-quotesnpm installnpm run plugin:buildnpm run plugin:validatenpm test
[/code]

Khung được tạo gồm:

  * `src/index.ts`: một entry `defineToolPlugin` với công cụ `echo`.
  * `src/index.test.ts`: một bài test metadata nhỏ.
  * `tsconfig.json`: đầu ra TypeScript NodeNext vào `dist/`.
  * `package.json`: script, dependency runtime, và `openclaw.extensions: ["./dist/index.js"]`.
  * `openclaw.plugin.json`: metadata manifest được tạo cho công cụ ban đầu.


Đầu ra xác thực dự kiến:

textCopy code
[code]
    Plugin stock-quotes is valid.
[/code]

## Viết một công cụ

`defineToolPlugin` nhận định danh plugin, một schema cấu hình tùy chọn, và một danh sách công cụ tĩnh. Kiểu tham số và cấu hình được suy luận từ các schema TypeBox.

typescriptCopy code
[code]
      export default defineToolPlugin({  id: "stock-quotes",  name: "Stock Quotes",  description: "Fetch stock quote snapshots.",  configSchema: Type.Object({    apiKey: Type.Optional(Type.String({ description: "Quote API key." })),    baseUrl: Type.Optional(Type.String({ description: "Quote API base URL." })),  }),  tools: (tool) => [    tool({      name: "stock_quote",      label: "Stock Quote",      description: "Fetch a stock quote snapshot.",      parameters: Type.Object({        symbol: Type.String({ description: "Ticker symbol, for example OPEN." }),      }),      async execute({ symbol }, config, context) {        context.signal?.throwIfAborted();        return {          symbol: symbol.toUpperCase(),          configured: Boolean(config.apiKey),          baseUrl: config.baseUrl ?? "https://api.example.com",        };      },    }),  ],});
[/code]

Tên công cụ là API ổn định. Hãy chọn tên duy nhất, viết thường, và đủ cụ thể để tránh xung đột với công cụ lõi hoặc plugin khác.

## Công cụ tùy chọn và công cụ factory

Đặt `optional: true` khi người dùng cần allowlist công cụ một cách rõ ràng trước khi nó được gửi tới mô hình:

typescriptCopy code
[code]
    tool({  name: "workflow_run",  description: "Run an external workflow.",  parameters: Type.Object({ goal: Type.String() }),  optional: true,  execute: ({ goal }) => ({ queued: true, goal }),});
[/code]

`openclaw plugins build` ghi entry manifest `toolMetadata.<tool>.optional` tương ứng, để OpenClaw có thể khám phá công cụ mà không cần tải mã runtime của plugin.

Dùng `factory` khi một công cụ cần ngữ cảnh công cụ runtime trước khi có thể được tạo. Factory giữ metadata ở dạng tĩnh trong khi cho phép công cụ từ chối một lần chạy cụ thể, kiểm tra trạng thái sandbox, hoặc bind các helper runtime.

typescriptCopy code
[code]
    tool({  name: "local_workflow",  description: "Run a local workflow outside sandboxed sessions.",  parameters: Type.Object({ goal: Type.String() }),  optional: true,  factory({ api, toolContext }) {    if (toolContext.sandboxed) {      return null;    }    return createLocalWorkflowTool(api);  },});
[/code]

Factory vẫn dành cho tên công cụ cố định. Dùng trực tiếp `definePluginEntry` khi plugin tính toán tên công cụ một cách động hoặc kết hợp công cụ với hook, dịch vụ, nhà cung cấp, lệnh, hoặc các bề mặt runtime khác.

## Giá trị trả về

`defineToolPlugin` bọc các giá trị trả về thuần vào định dạng kết quả công cụ của OpenClaw:

  * Trả về chuỗi khi mô hình cần thấy đúng văn bản đó.
  * Trả về một giá trị tương thích JSON khi bạn muốn mô hình thấy JSON đã định dạng và OpenClaw giữ giá trị gốc trong `details`.

typescriptCopy code
[code]
    tool({  name: "echo_text",  description: "Echo input text.",  parameters: Type.Object({    input: Type.String(),  }),  execute: ({ input }) => input,});
[/code]

typescriptCopy code
[code]
    tool({  name: "echo_json",  description: "Echo input as structured JSON.",  parameters: Type.Object({    input: Type.String(),  }),  execute: ({ input }) => ({ input, length: input.length }),});
[/code]

Dùng công cụ factory khi bạn cần trả về `AgentToolResult` tùy chỉnh hoặc tái sử dụng một implementation `api.registerTool` hiện có. Dùng `definePluginEntry` thay vì `defineToolPlugin` khi bạn cần công cụ hoàn toàn động hoặc plugin có nhiều năng lực.

## Cấu hình

`configSchema` là tùy chọn. Nếu bạn bỏ qua nó, OpenClaw dùng schema object rỗng nghiêm ngặt và manifest được tạo vẫn bao gồm `configSchema`.

typescriptCopy code
[code]
    export default defineToolPlugin({  id: "no-config-tools",  name: "No Config Tools",  description: "Adds tools that do not need configuration.",  tools: () => [],});
[/code]

Khi bạn thêm `configSchema`, đối số `execute` thứ hai được định kiểu từ schema:

typescriptCopy code
[code]
    const configSchema = Type.Object({  apiKey: Type.String(),}); export default defineToolPlugin({  id: "configured-tools",  name: "Configured Tools",  description: "Adds configured tools.",  configSchema,  tools: (tool) => [    tool({      name: "configured_ping",      description: "Check whether configuration is available.",      parameters: Type.Object({}),      execute: (_params, config) => ({ hasKey: config.apiKey.length > 0 }),    }),  ],});
[/code]

OpenClaw đọc cấu hình plugin từ entry plugin trong cấu hình Gateway. Không hard-code secret trong mã nguồn hoặc trong ví dụ tài liệu. Dùng cấu hình, biến môi trường, hoặc SecretRefs theo mô hình bảo mật của plugin.

## Metadata được tạo

OpenClaw khám phá các plugin đã cài đặt từ metadata lạnh. Nó phải có thể đọc manifest plugin trước khi import mã runtime của plugin. Vì vậy `defineToolPlugin` phơi bày metadata tĩnh, và `openclaw plugins build` ghi metadata đó vào package.

Chạy generator sau khi thay đổi id, tên, mô tả, schema cấu hình, activation, hoặc tên công cụ của plugin:

bashCopy code
[code]
    npm run buildopenclaw plugins build --entry ./dist/index.js
[/code]

Đối với plugin một công cụ, manifest được tạo trông như sau:

jsonCopy code
[code]
    {  "id": "stock-quotes",  "name": "Stock Quotes",  "description": "Fetch stock quote snapshots.",  "version": "0.1.0",  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {}  },  "activation": {    "onStartup": true  },  "contracts": {    "tools": ["stock_quote"]  }}
[/code]

`contracts.tools` là hợp đồng khám phá quan trọng. Nó cho OpenClaw biết plugin nào sở hữu từng công cụ mà không cần tải runtime của mọi plugin đã cài đặt. Nếu manifest đã lỗi thời, công cụ có thể bị thiếu khỏi khám phá hoặc plugin sai có thể bị quy trách nhiệm cho lỗi đăng ký.

## Metadata package

Đối với workflow plugin công cụ đơn giản, `openclaw plugins build` căn chỉnh `package.json` với entry runtime đơn đã chọn:

jsonCopy code
[code]
    {  "type": "module",  "files": ["dist", "openclaw.plugin.json", "README.md"],  "dependencies": {    "typebox": "^1.1.38"  },  "peerDependencies": {    "openclaw": ">=2026.5.17"  },  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

Dùng JavaScript đã build như `./dist/index.js` cho các package đã cài đặt. Entry mã nguồn hữu ích trong phát triển workspace, nhưng package đã phát hành không nên phụ thuộc vào việc tải runtime TypeScript.

## Xác thực trong CI

Dùng `plugins build --check` để làm CI thất bại khi metadata được tạo đã lỗi thời mà không ghi lại tệp:

bashCopy code
[code]
    npm run buildopenclaw plugins build --entry ./dist/index.js --checkopenclaw plugins validate --entry ./dist/index.jsnpm test
[/code]

`plugins validate` kiểm tra rằng:

  * `openclaw.plugin.json` tồn tại và vượt qua loader manifest thông thường.
  * Entry hiện tại export metadata `defineToolPlugin`.
  * Các trường manifest được tạo khớp với metadata entry.
  * `contracts.tools` khớp với tên công cụ đã khai báo.
  * `package.json` trỏ `openclaw.extensions` tới entry runtime đã chọn.


## Cài đặt và kiểm tra cục bộ

Từ một checkout OpenClaw riêng hoặc CLI đã cài đặt, cài đặt đường dẫn package:

bashCopy code
[code]
    openclaw plugins install ./stock-quotesopenclaw plugins inspect stock-quotes --runtime
[/code]

Đối với smoke package, hãy pack trước rồi cài đặt tarball:

bashCopy code
[code]
    npm packopenclaw plugins install npm-pack:./openclaw-plugin-stock-quotes-0.1.0.tgzopenclaw plugins inspect stock-quotes --runtime --json
[/code]

Sau khi cài đặt, khởi động hoặc khởi động lại Gateway và yêu cầu agent dùng công cụ. Nếu bạn đang debug khả năng hiển thị công cụ, hãy kiểm tra runtime plugin và catalog công cụ hiệu lực trước khi thay đổi mã.

## Phát hành

Phát hành qua ClawHub khi package đã sẵn sàng:

bashCopy code
[code]
    clawhub package publish your-org/stock-quotes --dry-runclawhub package publish your-org/stock-quotes
[/code]

Cài đặt bằng locator ClawHub rõ ràng:

bashCopy code
[code]
    openclaw plugins install clawhub:your-org/stock-quotes
[/code]

Spec package npm trần vẫn được hỗ trợ trong giai đoạn chuyển đổi ra mắt, nhưng ClawHub là bề mặt khám phá và phân phối được ưu tiên cho plugin OpenClaw.

## Khắc phục sự cố

### `plugin entry not found: ./dist/index.js`

Tệp entry đã chọn không tồn tại. Chạy `npm run build`, sau đó chạy lại `openclaw plugins build --entry ./dist/index.js` hoặc `openclaw plugins validate --entry ./dist/index.js`.

### `plugin entry does not expose defineToolPlugin metadata`

Entry không export một giá trị được tạo bởi `defineToolPlugin`. Kiểm tra rằng default export của module là kết quả `defineToolPlugin(...)`, hoặc truyền đúng entry bằng `--entry`.

### `openclaw.plugin.json generated metadata is stale`

Manifest không còn khớp với metadata entry. Chạy:

bashCopy code
[code]
    npm run buildopenclaw plugins build --entry ./dist/index.js
[/code]

Commit cả thay đổi `openclaw.plugin.json` và `package.json`.

### `package.json openclaw.extensions must include ./dist/index.js`

Metadata package trỏ tới một entry runtime khác. Chạy `openclaw plugins build --entry ./dist/index.js` để generator căn chỉnh metadata package với entry bạn định phân phối.

### `Cannot find package 'typebox'`

Plugin đã build import `typebox` ở runtime. Giữ `typebox` trong `dependencies`, cài đặt lại dependency package, build lại, và chạy lại xác thực.

### Công cụ không xuất hiện sau khi cài đặt

Kiểm tra những mục này theo thứ tự:

  1. `openclaw plugins inspect <plugin-id> --runtime`
  2. `openclaw plugins validate --root <plugin-root> --entry ./dist/index.js`
  3. `openclaw.plugin.json` có `contracts.tools` với tên công cụ dự kiến.
  4. `package.json` có `openclaw.extensions: ["./dist/index.js"]`.
  5. Gateway đã được khởi động lại hoặc tải lại sau khi cài đặt plugin.


## Xem thêm

  * [Xây dựng plugin](</vi/plugins/building-plugins>)
  * [Điểm entry plugin](</vi/plugins/sdk-entrypoints>)
  * [Đường dẫn con Plugin SDK](</vi/plugins/sdk-subpaths>)
  * [Manifest plugin](</vi/plugins/manifest>)
  * [CLI plugin](</vi/cli/plugins>)
  * [Phát hành ClawHub](</vi/clawhub/publishing>)


Was this useful?YesNo

Open issue