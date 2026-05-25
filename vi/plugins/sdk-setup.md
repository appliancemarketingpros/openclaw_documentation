---
title: Thiết lập và cấu hình Plugin
source_url: https://docs.openclaw.ai/vi/plugins/sdk-setup
scraped_at: 2026-05-25
---

Tài liệu tham chiếu cho đóng gói Plugin (metadata `package.json`), manifest (`openclaw.plugin.json`), mục thiết lập và schema cấu hình.

## Metadata gói

`package.json` của bạn cần có trường `openclaw` cho hệ thống Plugin biết Plugin của bạn cung cấp những gì:

### Plugin kênh

jsonCopy code
[code]
    {  "name": "@myorg/openclaw-my-channel",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "setupEntry": "./setup-entry.ts",    "channel": {      "id": "my-channel",      "label": "My Channel",      "blurb": "Short description of the channel."    }  }}
[/code]

### Plugin nhà cung cấp / đường cơ sở ClawHub

openclaw-clawhub-package.jsonCopy code
[code]
    {  "name": "@myorg/openclaw-my-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "compat": {      "pluginApi": ">=2026.3.24-beta.2",      "minGatewayVersion": "2026.3.24-beta.2"    },    "build": {      "openclawVersion": "2026.3.24-beta.2",      "pluginSdkVersion": "2026.3.24-beta.2"    }  }}
[/code]

### Các trường `openclaw`

Các tệp điểm vào (tương đối với gốc gói).

Điểm vào gọn nhẹ chỉ dùng cho thiết lập (tùy chọn).

Metadata danh mục kênh cho các bề mặt thiết lập, bộ chọn, khởi động nhanh và trạng thái.

Các id nhà cung cấp được Plugin này đăng ký.

Gợi ý cài đặt: `npmSpec`, `localPath`, `defaultChoice`, `minHostVersion`, `expectedIntegrity`, `allowInvalidConfigRecovery`.

Các cờ hành vi khởi động.

### `openclaw.channel`

`openclaw.channel` là metadata gói nhẹ cho việc khám phá kênh và các bề mặt thiết lập trước khi runtime tải.

Trường | Kiểu | Ý nghĩa  
---|---|---  
`id` | `string` | Id kênh chuẩn.  
`label` | `string` | Nhãn kênh chính.  
`selectionLabel` | `string` | Nhãn bộ chọn/thiết lập khi cần khác với `label`.  
`detailLabel` | `string` | Nhãn chi tiết phụ cho danh mục kênh phong phú hơn và các bề mặt trạng thái.  
`docsPath` | `string` | Đường dẫn tài liệu cho các liên kết thiết lập và lựa chọn.  
`docsLabel` | `string` | Ghi đè nhãn dùng cho liên kết tài liệu khi cần khác với id kênh.  
`blurb` | `string` | Mô tả ngắn cho onboarding/danh mục.  
`order` | `number` | Thứ tự sắp xếp trong danh mục kênh.  
`aliases` | `string[]` | Bí danh tra cứu bổ sung cho lựa chọn kênh.  
`preferOver` | `string[]` | Các id Plugin/kênh có độ ưu tiên thấp hơn mà kênh này nên xếp trên.  
`systemImage` | `string` | Tên biểu tượng/system-image tùy chọn cho danh mục UI kênh.  
`selectionDocsPrefix` | `string` | Văn bản tiền tố trước liên kết tài liệu trong các bề mặt lựa chọn.  
`selectionDocsOmitLabel` | `boolean` | Hiển thị trực tiếp đường dẫn tài liệu thay vì liên kết tài liệu có nhãn trong bản sao lựa chọn.  
`selectionExtras` | `string[]` | Các chuỗi ngắn bổ sung được nối thêm trong bản sao lựa chọn.  
`markdownCapable` | `boolean` | Đánh dấu kênh là hỗ trợ markdown cho các quyết định định dạng gửi đi.  
`exposure` | `object` | Điều khiển hiển thị kênh cho thiết lập, danh sách đã cấu hình và bề mặt tài liệu.  
`quickstartAllowFrom` | `boolean` | Đưa kênh này vào luồng thiết lập khởi động nhanh `allowFrom` tiêu chuẩn.  
`forceAccountBinding` | `boolean` | Yêu cầu liên kết tài khoản rõ ràng ngay cả khi chỉ có một tài khoản tồn tại.  
`preferSessionLookupForAnnounceTarget` | `boolean` | Ưu tiên tra cứu phiên khi phân giải mục tiêu thông báo cho kênh này.  
  
Ví dụ:

jsonCopy code
[code]
    {  "openclaw": {    "channel": {      "id": "my-channel",      "label": "My Channel",      "selectionLabel": "My Channel (self-hosted)",      "detailLabel": "My Channel Bot",      "docsPath": "/channels/my-channel",      "docsLabel": "my-channel",      "blurb": "Webhook-based self-hosted chat integration.",      "order": 80,      "aliases": ["mc"],      "preferOver": ["my-channel-legacy"],      "selectionDocsPrefix": "Guide:",      "selectionExtras": ["Markdown"],      "markdownCapable": true,      "exposure": {        "configured": true,        "setup": true,        "docs": true      },      "quickstartAllowFrom": true    }  }}
[/code]

`exposure` hỗ trợ:

  * `configured`: đưa kênh vào các bề mặt liệt kê kiểu đã cấu hình/trạng thái
  * `setup`: đưa kênh vào các bộ chọn thiết lập/cấu hình tương tác
  * `docs`: đánh dấu kênh là công khai trong các bề mặt tài liệu/điều hướng


### `openclaw.install`

`openclaw.install` là metadata gói, không phải metadata manifest.

Trường | Kiểu | Ý nghĩa  
---|---|---  
`clawhubSpec` | `string` | Spec ClawHub chuẩn cho các luồng cài đặt/cập nhật và cài đặt theo nhu cầu trong onboarding.  
`npmSpec` | `string` | Spec npm chuẩn cho các luồng dự phòng cài đặt/cập nhật.  
`localPath` | `string` | Đường dẫn cài đặt cục bộ cho phát triển hoặc gói đi kèm.  
`defaultChoice` | `"clawhub"` | `"npm"` | `"local"` | Nguồn cài đặt ưu tiên khi có nhiều nguồn khả dụng.  
`minHostVersion` | `string` | Phiên bản OpenClaw tối thiểu được hỗ trợ ở dạng `>=x.y.z` hoặc `>=x.y.z-prerelease`.  
`expectedIntegrity` | `string` | Chuỗi integrity dist npm kỳ vọng, thường là `sha512-...`, cho các cài đặt đã ghim.  
`allowInvalidConfigRecovery` | `boolean` | Cho phép các luồng cài đặt lại Plugin đi kèm khôi phục từ những lỗi cấu hình lỗi thời cụ thể.  
  
Hành vi onboarding

Onboarding tương tác cũng dùng `openclaw.install` cho các bề mặt cài đặt theo nhu cầu. Nếu Plugin của bạn hiển thị lựa chọn xác thực nhà cung cấp hoặc metadata thiết lập/danh mục kênh trước khi runtime tải, onboarding có thể hiển thị lựa chọn đó, nhắc cài đặt qua ClawHub, npm hoặc cục bộ, cài đặt hoặc bật Plugin, rồi tiếp tục luồng đã chọn. Các lựa chọn onboarding ClawHub dùng `clawhubSpec` và được ưu tiên khi có; lựa chọn npm yêu cầu metadata danh mục đáng tin cậy với `npmSpec` registry; phiên bản chính xác và `expectedIntegrity` là các ghim npm tùy chọn. Nếu có `expectedIntegrity`, các luồng cài đặt/cập nhật sẽ thực thi nó cho npm. Giữ metadata "hiển thị gì" trong `openclaw.plugin.json` và metadata "cách cài đặt" trong `package.json`.

Thực thi minHostVersion

Nếu `minHostVersion` được đặt, cả quá trình cài đặt và tải manifest-registry không đi kèm đều thực thi nó. Host cũ hơn sẽ bỏ qua Plugin bên ngoài; chuỗi phiên bản không hợp lệ bị từ chối. Plugin nguồn đi kèm được giả định là cùng phiên bản với checkout host.

Cài đặt npm đã ghim

Với cài đặt npm đã ghim, giữ phiên bản chính xác trong `npmSpec` và thêm integrity artifact kỳ vọng:

jsonCopy code
[code]
    {  "openclaw": {    "install": {      "npmSpec": "@wecom/wecom-openclaw-plugin@1.2.3",      "expectedIntegrity": "sha512-REPLACE_WITH_NPM_DIST_INTEGRITY",      "defaultChoice": "npm"    }  }}
[/code]

Phạm vi allowInvalidConfigRecovery

`allowInvalidConfigRecovery` không phải là cơ chế bỏ qua tổng quát cho cấu hình hỏng. Nó chỉ dành cho khôi phục hẹp của Plugin đi kèm, để cài đặt lại/thiết lập có thể sửa các phần còn sót lại sau nâng cấp đã biết như thiếu đường dẫn Plugin đi kèm hoặc mục `channels.<id>` lỗi thời cho cùng Plugin đó. Nếu cấu hình bị hỏng vì lý do không liên quan, cài đặt vẫn thất bại đóng và yêu cầu operator chạy `openclaw doctor --fix`.

### Trì hoãn tải đầy đủ

Plugin kênh có thể chọn tải trì hoãn với:

jsonCopy code
[code]
    {  "openclaw": {    "extensions": ["./index.ts"],    "setupEntry": "./setup-entry.ts",    "startup": {      "deferConfiguredChannelFullLoadUntilAfterListen": true    }  }}
[/code]

Khi được bật, OpenClaw chỉ tải `setupEntry` trong giai đoạn khởi động trước khi lắng nghe, ngay cả với các kênh đã được cấu hình. Điểm vào đầy đủ sẽ tải sau khi Gateway bắt đầu lắng nghe.

Nếu điểm vào thiết lập/đầy đủ của bạn đăng ký các phương thức RPC Gateway, hãy đặt chúng dưới tiền tố dành riêng cho Plugin. Các namespace quản trị lõi dành riêng (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) vẫn thuộc sở hữu của lõi và luôn phân giải thành `operator.admin`.

## Manifest Plugin

Mọi Plugin native phải cung cấp `openclaw.plugin.json` trong gốc gói. OpenClaw dùng tệp này để xác thực cấu hình mà không thực thi mã Plugin.

jsonCopy code
[code]
    {  "id": "my-plugin",  "name": "My Plugin",  "description": "Adds My Plugin capabilities to OpenClaw",  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {      "webhookSecret": {        "type": "string",        "description": "Webhook verification secret"      }    }  }}
[/code]

Với Plugin kênh, hãy thêm `kind` và `channels`:

jsonCopy code
[code]
    {  "id": "my-channel",  "kind": "channel",  "channels": ["my-channel"],  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {}  }}
[/code]

Ngay cả Plugin không có cấu hình cũng phải cung cấp schema. Schema rỗng là hợp lệ:

jsonCopy code
[code]
    {  "id": "my-plugin",  "configSchema": {    "type": "object",    "additionalProperties": false  }}
[/code]

Xem [Manifest Plugin](</vi/plugins/manifest>) để biết tài liệu tham chiếu schema đầy đủ.

## Phát hành ClawHub

Với các gói Plugin, dùng lệnh ClawHub dành riêng cho gói:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-plugin
[/code]

## Mục nhập thiết lập

Tệp `setup-entry.ts` là một lựa chọn thay thế nhẹ cho `index.ts` mà OpenClaw tải khi chỉ cần các bề mặt thiết lập (onboarding, sửa cấu hình, kiểm tra kênh bị tắt).

typescriptCopy code
[code]
    // setup-entry.ts  export default defineSetupPluginEntry(myChannelPlugin);
[/code]

Điều này tránh tải mã runtime nặng (thư viện mã hóa, đăng ký CLI, dịch vụ nền) trong các luồng thiết lập.

Các kênh workspace được đóng gói giữ các export an toàn cho thiết lập trong module phụ có thể dùng `defineBundledChannelSetupEntry(...)` từ `openclaw/plugin-sdk/channel-entry-contract` thay cho `defineSetupPluginEntry(...)`. Hợp đồng được đóng gói đó cũng hỗ trợ export `runtime` tùy chọn để wiring runtime lúc thiết lập có thể luôn nhẹ và rõ ràng.

When OpenClaw uses setupEntry instead of the full entry

  * Kênh bị tắt nhưng cần các bề mặt thiết lập/onboarding.
  * Kênh được bật nhưng chưa cấu hình.
  * Tải trì hoãn được bật (`deferConfiguredChannelFullLoadUntilAfterListen`).

What setupEntry must register

  * Đối tượng Plugin kênh (qua `defineSetupPluginEntry`).
  * Mọi route HTTP cần thiết trước khi gateway listen.
  * Mọi phương thức Gateway cần trong lúc khởi động.


Các phương thức Gateway lúc khởi động đó vẫn nên tránh các namespace quản trị lõi dành riêng như `config.*` hoặc `update.*`.

What setupEntry should NOT include

  * Đăng ký CLI.
  * Dịch vụ nền.
  * Import runtime nặng (crypto, SDK).
  * Phương thức Gateway chỉ cần sau khi khởi động.


### Import helper thiết lập hẹp

Đối với các đường dẫn nóng chỉ dành cho thiết lập, ưu tiên các seam helper thiết lập hẹp thay vì umbrella `plugin-sdk/setup` rộng hơn khi bạn chỉ cần một phần của bề mặt thiết lập:

Đường dẫn import | Dùng cho | Export chính  
---|---|---  
`plugin-sdk/setup-runtime` | helper runtime lúc thiết lập vẫn có trong `setupEntry` / khởi động kênh trì hoãn | `createPatchedAccountSetupAdapter`, `createEnvPatchedAccountSetupAdapter`, `createSetupInputPresenceValidator`, `noteChannelLookupFailure`, `noteChannelLookupSummary`, `promptResolvedAllowFrom`, `splitSetupEntries`, `createAllowlistSetupWizardProxy`, `createDelegatedSetupWizardProxy`  
`plugin-sdk/setup-adapter-runtime` | bí danh tương thích đã lỗi thời; dùng `plugin-sdk/setup-runtime` | `createEnvPatchedAccountSetupAdapter`  
`plugin-sdk/setup-tools` | helper CLI/cài đặt/lưu trữ/tài liệu cho thiết lập | `formatCliCommand`, `detectBinary`, `extractArchive`, `resolveBrewExecutable`, `formatDocsLink`, `CONFIG_DIR`  
  
Dùng seam `plugin-sdk/setup` rộng hơn khi bạn muốn toàn bộ hộp công cụ thiết lập dùng chung, bao gồm các helper vá cấu hình như `moveSingleAccountChannelSectionToDefaultAccount(...)`.

Các adapter vá thiết lập vẫn an toàn trên đường dẫn nóng khi import. Tra cứu bề mặt hợp đồng thăng cấp một tài khoản được đóng gói của chúng là lazy, nên việc import `plugin-sdk/setup-runtime` không tải háo hức việc khám phá bề mặt hợp đồng được đóng gói trước khi adapter thật sự được dùng.

### Thăng cấp một tài khoản do kênh sở hữu

Khi một kênh nâng cấp từ cấu hình cấp cao nhất một tài khoản sang `channels.<id>.accounts.*`, hành vi dùng chung mặc định là di chuyển các giá trị phạm vi tài khoản được thăng cấp vào `accounts.default`.

Các kênh được đóng gói có thể thu hẹp hoặc ghi đè việc thăng cấp đó qua bề mặt hợp đồng thiết lập của chúng:

  * `singleAccountKeysToMove`: các khóa cấp cao nhất bổ sung nên được di chuyển vào tài khoản được thăng cấp
  * `namedAccountPromotionKeys`: khi các tài khoản có tên đã tồn tại, chỉ các khóa này được di chuyển vào tài khoản được thăng cấp; các khóa chính sách/phân phối dùng chung vẫn ở gốc kênh
  * `resolveSingleAccountPromotionTarget(...)`: chọn tài khoản hiện có nào nhận các giá trị được thăng cấp


## Schema cấu hình

Cấu hình Plugin được xác thực với JSON Schema trong manifest của bạn. Người dùng cấu hình plugin qua:

json5Copy code
[code]
    {  plugins: {    entries: {      "my-plugin": {        config: {          webhookSecret: "abc123",        },      },    },  },}
[/code]

Plugin của bạn nhận cấu hình này dưới dạng `api.pluginConfig` trong khi đăng ký.

Đối với cấu hình dành riêng cho kênh, hãy dùng phần cấu hình kênh thay thế:

json5Copy code
[code]
    {  channels: {    "my-channel": {      token: "bot-token",      allowFrom: ["user1", "user2"],    },  },}
[/code]

### Xây dựng schema cấu hình kênh

Dùng `buildChannelConfigSchema` để chuyển đổi schema Zod thành wrapper `ChannelConfigSchema` được dùng bởi các artifact cấu hình do plugin sở hữu:

typescriptCopy code
[code]
      const accountSchema = z.object({  token: z.string().optional(),  allowFrom: z.array(z.string()).optional(),  accounts: z.object({}).catchall(z.any()).optional(),  defaultAccount: z.string().optional(),}); const configSchema = buildChannelConfigSchema(accountSchema);
[/code]

Nếu bạn đã viết hợp đồng dưới dạng JSON Schema hoặc TypeBox, hãy dùng helper trực tiếp để OpenClaw có thể bỏ qua chuyển đổi Zod sang JSON Schema trên các đường dẫn metadata:

typescriptCopy code
[code]
      const configSchema = buildJsonChannelConfigSchema(  Type.Object({    token: Type.Optional(Type.String()),    allowFrom: Type.Optional(Type.Array(Type.String())),  }),);
[/code]

Đối với plugin bên thứ ba, hợp đồng đường dẫn lạnh vẫn là manifest plugin: phản chiếu JSON Schema đã tạo vào `openclaw.plugin.json#channelConfigs` để schema cấu hình, thiết lập và các bề mặt UI có thể kiểm tra `channels.<id>` mà không cần tải mã runtime.

## Trình hướng dẫn thiết lập

Plugin kênh có thể cung cấp trình hướng dẫn thiết lập tương tác cho `openclaw onboard`. Trình hướng dẫn là đối tượng `ChannelSetupWizard` trên `ChannelPlugin`:

typescriptCopy code
[code]
     const setupWizard: ChannelSetupWizard = {  channel: "my-channel",  status: {    configuredLabel: "Connected",    unconfiguredLabel: "Not configured",    resolveConfigured: ({ cfg }) => Boolean((cfg.channels as any)?.["my-channel"]?.token),  },  credentials: [    {      inputKey: "token",      providerHint: "my-channel",      credentialLabel: "Bot token",      preferredEnvVar: "MY_CHANNEL_BOT_TOKEN",      envPrompt: "Use MY_CHANNEL_BOT_TOKEN from environment?",      keepPrompt: "Keep current token?",      inputPrompt: "Enter your bot token:",      inspect: ({ cfg, accountId }) => {        const token = (cfg.channels as any)?.["my-channel"]?.token;        return {          accountConfigured: Boolean(token),          hasConfiguredValue: Boolean(token),        };      },    },  ],};
[/code]

Kiểu `ChannelSetupWizard` hỗ trợ `credentials`, `textInputs`, `dmPolicy`, `allowFrom`, `groupAccess`, `prepare`, `finalize` và nhiều hơn nữa. Xem các gói plugin được đóng gói (ví dụ Plugin Discord `src/channel.setup.ts`) để có ví dụ đầy đủ.

Shared allowFrom prompts

Đối với lời nhắc danh sách cho phép DM chỉ cần luồng chuẩn `note -> prompt -> parse -> merge -> patch`, ưu tiên các helper thiết lập dùng chung từ `openclaw/plugin-sdk/setup`: `createPromptParsedAllowFromForAccount(...)`, `createTopLevelChannelParsedAllowFromPrompt(...)` và `createNestedChannelParsedAllowFromPrompt(...)`.

Standard channel setup status

Đối với các khối trạng thái thiết lập kênh chỉ khác nhau theo nhãn, điểm số và các dòng bổ sung tùy chọn, ưu tiên `createStandardChannelSetupStatus(...)` từ `openclaw/plugin-sdk/setup` thay vì tự viết cùng đối tượng `status` trong từng plugin.

Optional channel setup surface

Đối với các bề mặt thiết lập tùy chọn chỉ nên xuất hiện trong một số ngữ cảnh nhất định, dùng `createOptionalChannelSetupSurface` từ `openclaw/plugin-sdk/channel-setup`:

typescriptCopy code
[code]
    import { createOptionalChannelSetupSurface } from "openclaw/plugin-sdk/channel-setup"; const setupSurface = createOptionalChannelSetupSurface({  channel: "my-channel",  label: "My Channel",  npmSpec: "@myorg/openclaw-my-channel",  docsPath: "/channels/my-channel",});// Returns { setupAdapter, setupWizard }
[/code]

`plugin-sdk/channel-setup` cũng cung cấp các builder cấp thấp hơn `createOptionalChannelSetupAdapter(...)` và `createOptionalChannelSetupWizard(...)` khi bạn chỉ cần một nửa của bề mặt cài đặt tùy chọn đó.

Adapter/trình hướng dẫn tùy chọn được tạo sẽ fail closed trên các thao tác ghi cấu hình thật. Chúng tái sử dụng một thông báo yêu cầu cài đặt trên `validateInput`, `applyAccountConfig` và `finalize`, đồng thời thêm liên kết tài liệu khi `docsPath` được đặt.

Binary-backed setup helpers

Đối với UI thiết lập dựa trên binary, ưu tiên các helper ủy quyền dùng chung thay vì sao chép cùng phần glue binary/trạng thái vào từng kênh:

  * `createDetectedBinaryStatus(...)` cho các khối trạng thái chỉ khác nhau theo nhãn, gợi ý, điểm số và phát hiện binary
  * `createCliPathTextInput(...)` cho input văn bản dựa trên đường dẫn
  * `createDelegatedSetupWizardStatusResolvers(...)`, `createDelegatedPrepare(...)`, `createDelegatedFinalize(...)` và `createDelegatedResolveConfigured(...)` khi `setupEntry` cần chuyển tiếp lazy tới một trình hướng dẫn đầy đủ nặng hơn
  * `createDelegatedTextInputShouldPrompt(...)` khi `setupEntry` chỉ cần ủy quyền quyết định `textInputs[*].shouldPrompt`


## Phát hành và cài đặt

**Plugin bên ngoài:** phát hành lên [ClawHub](</vi/clawhub>), rồi cài đặt:

### npm

bashCopy code
[code]
    openclaw plugins install @myorg/openclaw-my-plugin
[/code]

Các package spec trần cài đặt từ npm trong giai đoạn chuyển đổi ra mắt.

### ClawHub only

bashCopy code
[code]
    openclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

### npm package spec

Dùng npm khi một gói chưa chuyển sang ClawHub, hoặc khi bạn cần một đường dẫn cài đặt npm trực tiếp trong quá trình di chuyển:

bashCopy code
[code]
    openclaw plugins install npm:@myorg/openclaw-my-plugin
[/code]

**Plugin trong repo:** đặt dưới cây workspace Plugin đi kèm và chúng sẽ tự động được phát hiện trong quá trình build.

**Người dùng có thể cài đặt:**

bashCopy code
[code]
    openclaw plugins install <package-name>
[/code]

Siêu dữ liệu package đi kèm là tường minh, không được suy luận từ JavaScript đã build khi Gateway khởi động. Các phụ thuộc runtime thuộc về package Plugin sở hữu chúng; quá trình khởi động OpenClaw đã đóng gói không bao giờ sửa chữa hoặc phản chiếu các phụ thuộc của Plugin.

## Liên quan

  * [Xây dựng Plugin](</vi/plugins/building-plugins>) — hướng dẫn bắt đầu từng bước
  * [Manifest Plugin](</vi/plugins/manifest>) — tài liệu tham khảo đầy đủ về schema manifest
  * [Điểm vào SDK](</vi/plugins/sdk-entrypoints>) — `definePluginEntry` và `defineChannelPluginEntry`


Was this useful?YesNo